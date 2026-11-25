#!/usr/bin/env python3
"""AZ token-resonance negative controls - [SESSION] NONCANONICAL. Bounded tests that the runner, the analysis and the
campaign driver REFUSE what they must refuse. Uses the test configuration only (tag SMOKE; no evidential value).

Every case states the expected exit code and a text the output must contain; for every rejected input the output must
contain neither an estimate ("RD=") nor a reading ("SUPPORTED", "EQUIVALENT", ...).

usage
  python -I az_tokres_negcontrols.py --work EMPTY_DIR [--fixtures-log LOG]
Exit code 0 iff every control behaves as stated. About five minutes on two cores.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
REL = {"engine": ("upload", "tdrg-records", "genesis_mode_b_mc.py"),
       "orient": ("evidence", "tdrg", "scripts", "tdrg_orient_v2_12_14.py"),
       "runner": ("evidence", "az", "scripts", "az_tokres_run.py"),
       "fixtures": ("evidence", "az", "scripts", "az_tokres_fixtures.py"),
       "analyse": ("evidence", "az", "scripts", "az_tokres_analyse.py"),
       "driver": ("evidence", "az", "scripts", "az_tokres_campaign.py"),
       "golden": ("evidence", "az", "token_resonance", "fixtures", "golden.json")}
P = {k: os.path.join(ROOT, *v) for k, v in REL.items()}
PY = [sys.executable, "-I"]
FORBIDDEN = ("RD=", "SUPPORTED", "EQUIVALENT", "DIFFERENT", "registered reading", "test-configuration reading")
OK = True
N_CASES = 0


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def run(cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.returncode, p.stdout.decode("utf-8", "replace")


def report(name, cond, detail=""):
    global OK, N_CASES
    N_CASES += 1
    OK &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (" :: " + detail if detail else ""), flush=True)


def runner_cmd(out, tag="SMOKE", N=120, profile="P1", start=0, stop=24, n_perm=6, extra=(), engine=None):
    return PY + [P["runner"], "--engine", engine or P["engine"], "--orient", P["orient"], "--out", out, "--tag", tag,
                 "--N", str(N), "--k", "8", "--profile", profile, "--start", str(start), "--stop", str(stop),
                 "--n-perm", str(n_perm)] + list(extra)


def analyse_cmd(files, cell="TEST-C1", flog=None, sens=(), runner=None, extra=()):
    cmd = PY + [P["analyse"], "--registered", cell, "--engine", P["engine"], "--orient", P["orient"],
                "--runner", runner or P["runner"]]
    if flog:
        cmd += ["--fixtures-log", flog]
    cmd += list(extra) + list(files)
    if sens:
        cmd += ["--sensitivity"] + list(sens)
    return cmd


def read_rows(path):
    with open(path) as f:
        return [json.loads(x) for x in f if x.strip()]


def write_rows(path, rows, refresh=True):
    with open(path, "w", newline="\n") as f:
        f.write("".join(json.dumps(r, sort_keys=True) + "\n" for r in rows))
    if refresh:                                   # make the manifest agree, so that the ROW check is what must fire
        mp = path + ".manifest.json"
        with open(mp) as f:
            mans = [json.loads(x) for x in f if x.strip()]
        mans[-1]["file_sha256"] = sha256_file(path)
        mans[-1]["rows_total"] = len(rows)
        with open(mp, "w", newline="\n") as f:
            f.write("".join(json.dumps(m, sort_keys=True) + "\n" for m in mans))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--fixtures-log", default=os.path.join(ROOT, "evidence", "az", "token_resonance", "fixtures",
                                                           "fixtures_output.txt"))
    a = ap.parse_args()
    work = os.path.abspath(a.work)
    if os.path.exists(work) and os.listdir(work):
        print("REFUSED: --work must be an empty or new directory", file=sys.stderr)
        return 2
    os.makedirs(work, exist_ok=True)
    flog = a.fixtures_log
    t0 = time.time()
    print("bytes under test (SHA-256):")
    for k in ("engine", "orient", "runner", "fixtures", "analyse", "driver", "golden"):
        print("  %-9s %s" % (k, sha256_file(P[k])))

    # ---------------- A. runner refusals
    rc, out = run(runner_cmd(os.path.join(work, "a1.jsonl"), tag="AZ-TOKRES-S1", stop=1, n_perm=0))
    report("A1 runner refuses the registered tag without --confirmatory", rc == 2 and not os.path.exists(os.path.join(work, "a1.jsonl")), "exit %d" % rc)
    rc, out = run(runner_cmd(os.path.join(work, "a2.jsonl"), stop=1, n_perm=0, extra=["--confirmatory"]))
    report("A2 runner refuses --confirmatory with a non-registered tag", rc == 2, "exit %d" % rc)
    bad_engine = os.path.join(work, "engine_modified.py")
    shutil.copyfile(P["engine"], bad_engine)
    with open(bad_engine, "ab") as f:
        f.write(b"\n# one byte more\n")
    rc, out = run(runner_cmd(os.path.join(work, "a3.jsonl"), stop=1, n_perm=0, engine=bad_engine))
    report("A3 runner refuses an engine that does not hash to the pin", rc == 2 and "pin mismatch" in out, "exit %d" % rc)

    # ---------------- B. a valid test data set (two shards of TEST-C1, one of TEST-C3)
    good = os.path.join(work, "good")
    os.makedirs(good)
    s1, s2, s3 = (os.path.join(good, n) for n in ("TEST-C1_00000_00012.jsonl", "TEST-C1_00012_00024.jsonl", "TEST-C3_00000_00012.jsonl"))
    procs = [subprocess.Popen(runner_cmd(s1, stop=12), stdout=subprocess.DEVNULL),
             subprocess.Popen(runner_cmd(s2, start=12), stdout=subprocess.DEVNULL)]
    codes = [p.wait() for p in procs]
    rc3, _ = run(runner_cmd(s3, profile="P2", stop=12, n_perm=0))
    report("B0 test data generated (TEST-C1 in two shards, TEST-C3)", codes == [0, 0] and rc3 == 0, "exit codes %s, %d" % (codes, rc3))
    rc, out = run(analyse_cmd([s1, s2], flog=flog))
    report("B1 valid input: integrity and gates pass; readings are marked as test configuration",
           rc == 0 and "INTEGRITY: PASS" in out and "G1 fixtures on the campaign machine: PASS" in out
           and "test-configuration reading, no evidential value" in out and "registered reading" not in out, "exit %d" % rc)
    rc, out = run(analyse_cmd([s2, s1], flog=flog, sens=[s3]))
    report("B2 valid input with the sensitivity set, shards in any order", rc == 0 and "[sensitivity]" in out
           and "reading: none (sensitivity profile; descriptive)" in out, "exit %d" % rc)
    rc, out = run(runner_cmd(s1, stop=12))
    report("B3 runner refuses an existing output without --resume", rc == 2, "exit %d" % rc)
    rc, out = run(runner_cmd(s1, stop=12, extra=["--resume", "--T", "700"]))
    report("B4 runner refuses --resume under a changed T", rc == 2 and "another identity" in out, "exit %d" % rc)
    rc, out = run(runner_cmd(s1, stop=13, extra=["--resume"]))
    report("B5 runner refuses --resume under a changed shard range", rc == 2 and "other shard arguments" in out, "exit %d" % rc)
    rc, out = run(runner_cmd(s1, stop=12, n_perm=0, extra=["--resume"]))
    report("B6 runner refuses --resume under a changed --n-perm", rc == 2, "exit %d" % rc)
    h_before = sha256_file(s1)
    rc, out = run(runner_cmd(s1, stop=12, extra=["--resume"]))
    rc2, out2 = run(analyse_cmd([s1, s2], flog=flog))
    report("B7 --resume with identical arguments adds nothing and the set still validates",
           rc == 0 and '"runs_written": 0' in out and sha256_file(s1) == h_before and rc2 == 0, "exit %d, %d" % (rc, rc2))
    rows = read_rows(s1)
    with open(s1, "a", newline="\n") as f:
        f.write(json.dumps(rows[0])[:57])                       # a record cut off by an interruption
    rc, out = run(runner_cmd(s1, stop=12, extra=["--resume"]))
    report("B8 --resume drops a cut-off last record and restores the file", rc == 0 and sha256_file(s1) == h_before, "exit %d" % rc)

    # ---------------- C. the analysis rejects tampered or wrong input (exit 2) and failed gates (exit 3)
    def case(name, want_rc, must, mutate, files=None, flog_=flog, runner=None, refresh=True):
        d = os.path.join(work, "case_%02d" % (N_CASES + 1))
        shutil.copytree(good, d)
        f1, f2 = os.path.join(d, os.path.basename(s1)), os.path.join(d, os.path.basename(s2))
        ctx = {"f1": f1, "f2": f2, "dir": d}
        if mutate:
            mutate(ctx)
        rc, out = run(analyse_cmd(files(ctx) if files else [f1, f2], flog=ctx.get("flog", flog_), runner=runner))
        clean = not any(x in out for x in FORBIDDEN)
        report(name, rc == want_rc and must in out and clean,
               "exit %d%s%s" % (rc, "" if must in out else "; expected text missing", "" if clean else "; ESTIMATE OR READING PRINTED"))

    def edit(pred, fn, which="f1", refresh=True):
        def m(ctx):
            rows = read_rows(ctx[which])
            hit = [r for r in rows if pred(r)][:1]
            assert hit, "negative control found no record to edit"
            fn(hit[0], rows)
            write_rows(ctx[which], rows, refresh)
        return m

    any_row = lambda r: True
    o1r = lambda r: r["arm"] == "O1R"
    setk = lambda k, v: (lambda r, rows: r.__setitem__(k, v))
    ID = "identity differs from the registered one"
    case("C01 wrong tag in a record", 2, ID, edit(any_row, setk("tag", "AZ-TOKRES-S1")))
    case("C02 wrong T in a record", 2, ID, edit(any_row, setk("T", 801)))
    case("C03 wrong cap in a record", 2, ID, edit(any_row, setk("cap", 301)))
    case("C04 wrong policy in a record", 2, ID, edit(any_row, setk("policy", "largest_center")))
    case("C05 wrong profile in a record", 2, ID, edit(any_row, setk("profile", "P2")))
    case("C06 wrong engine pin in a record", 2, ID, edit(any_row, setk("engine_sha256", "0" * 64)))
    case("C07 wrong runner pin in a record", 2, ID, edit(any_row, setk("runner_sha256", "0" * 64)))
    case("C08 wrong confirmatory flag in a record", 2, ID, edit(any_row, setk("confirmatory", True)))
    ST = "initial state differs from the registered derivation"
    case("C09 tampered initial phases", 2, ST, edit(any_row, lambda r, rows: r["th0"].__setitem__(0, (r["th0"][0] + 1) % 120)))
    case("C10 tampered initial token of a resonant arm", 2, ST, edit(o1r, lambda r, rows: r["d0"].__setitem__(r["slot"], 1)))
    case("C11 arm label changed (O1R recorded as O1D)", 2, ST, edit(o1r, setk("arm", "O1D")))
    case("C12 seed changed", 2, ST, edit(any_row, setk("seed", 1)))
    case("C13 class label changed", 2, ST, edit(o1r, setk("slot_class", "NR")))
    case("C14 outcome edited (M raised by one)", 2, "M != 4 + births", edit(any_row, lambda r, rows: r.__setitem__("M", r["M"] + 1)))
    case("C15 census with a token outside S0", 2, "outside S0",
         edit(lambda r: r["M"] > 4, lambda r, rows: r["census"].__setitem__(0, [(max(r["d0"]) + 7) % 120, r["census"][0][1]])))
    case("C16 a record removed", 2, "missing record", edit(o1r, lambda r, rows: rows.remove(r)))
    case("C17 a record duplicated", 2, "duplicate record", edit(any_row, lambda r, rows: rows.append(dict(r))))
    case("C18 a record of an unregistered base draw", 2, "not a registered record", edit(any_row, lambda r, rows: rows.append(dict(r, base=999))))
    case("C19 record file edited after the run (manifest not updated)", 2, "SHA-256 differs from the manifest",
         edit(any_row, setk("secs", 0.0), refresh=False))
    case("C20 manifest missing", 2, "manifest missing", lambda ctx: os.remove(ctx["f1"] + ".manifest.json"))

    def manifest_T(ctx):
        mp = ctx["f1"] + ".manifest.json"
        with open(mp) as f:
            mans = [json.loads(x) for x in f if x.strip()]
        mans[-1]["identity"]["T"] = 700
        with open(mp, "w", newline="\n") as f:
            f.write("".join(json.dumps(m, sort_keys=True) + "\n" for m in mans))
    case("C21 manifest of another identity", 2, "manifest identity differs", manifest_T)
    case("C22 one shard missing", 2, "shards cover base draws up to 12", None, files=lambda c: [c["f1"]])
    case("C23 one shard given twice", 2, "given more than once", None, files=lambda c: [c["f1"], c["f2"], c["f1"]])
    bad_runner = os.path.join(work, "runner_modified.py")
    shutil.copyfile(P["runner"], bad_runner)
    with open(bad_runner, "ab") as f:
        f.write(b"\n# one byte more\n")
    case("C24 runner file that does not hash to the registered pin", 2, "runner file does not hash to the registered pin", None, runner=bad_runner)
    case("C25 law-violation counter > 0 in one record: gate G2 stops everything", 3, "GATE FAILURE", edit(any_row, setk("law_viol", 1)))

    def bad_log(transform):
        def m(ctx):
            with open(flog, encoding="utf-8") as f:
                text = f.read()
            ctx["flog"] = os.path.join(ctx["dir"], "fixtures_log.txt")
            with open(ctx["flog"], "w", newline="\n") as f:
                f.write(transform(text))
        return m
    case("C26 fixtures log with a failed test: gate G1 stops everything", 3, "GATE FAILURE",
         bad_log(lambda t: t.replace("PASS T2 ", "FAIL T2 ", 1).replace("FIXTURES PASS", "FIXTURES FAIL")))
    case("C27 fixtures log of other runner bytes", 3, "does not show the pinned runner",
         bad_log(lambda t: t.replace(sha256_file(P["runner"]), "0" * 64)))
    case("C28 fixtures log missing", 3, "fixtures log missing", None, flog_=os.path.join(work, "no_such_log.txt"))
    rc, out = run(PY + [P["analyse"], "--exploratory", "--cell", "N120k8", "--profile", "P1", s1, s2])
    report("C29 exploratory mode prints estimates but no reading of any kind",
           rc == 0 and "EXPLORATORY INPUT" in out and "reading: SUPPRESSED" in out
           and not any(x in out for x in ("SUPPORTED", "EQUIVALENT", "DIFFERENT", "registered reading", "test-configuration reading")),
           "exit %d" % rc)
    rc, out = run(analyse_cmd([s3], cell="TEST-C3", flog=flog))
    report("C30 the sensitivity profile analysed on its own gets no reading",
           rc == 0 and "reading: none (sensitivity profile; descriptive)" in out
           and not any(x in out for x in ("SUPPORTED", "registered reading", "test-configuration reading")), "exit %d" % rc)

    d = os.path.join(work, "case_exclude")
    shutil.copytree(good, d)
    f1, f2 = os.path.join(d, os.path.basename(s1)), os.path.join(d, os.path.basename(s2))
    write_rows(f1, [r for r in read_rows(f1) if r["base"] != 5])
    rc, out = run(analyse_cmd([f1, f2], flog=flog))
    rc2, out2 = run(analyse_cmd([f1, f2], flog=flog, extra=["--exclude-base", "5"]))
    report("C31 a base draw missing in all arms is rejected, and accepted only as a declared deviation that qualifies every reading",
           rc == 2 and "missing record" in out and rc2 == 0 and "DEVIATION: base draws excluded from all arms: [5]" in out2
           and out2.count("DEVIATION: base draws excluded") >= 3, "exit %d, %d" % (rc, rc2))

    # ---------------- D. campaign driver: exit codes enforced, no completion marker on failure
    drv = lambda outdir, *extra: PY + [P["driver"], "--out", outdir] + list(extra)
    rc, out = run(drv(os.path.join(work, "d1"), "--plan", "stage1"))
    report("D1 driver refuses plan stage1 without --confirmatory", rc == 2 and not os.path.exists(os.path.join(work, "d1")), "exit %d" % rc)
    d2 = os.path.join(work, "d2")
    rc, out = run(drv(d2, "--plan", "test", "--jobs", "2", "--skip-fixtures", flog))
    ok2 = rc == 0 and os.path.exists(os.path.join(d2, "CAMPAIGN_COMPLETE.json")) and not os.path.exists(os.path.join(d2, "CAMPAIGN_FAILED.txt"))
    report("D2 driver completes the test plan: marker written, analyses exit 0", ok2, "exit %d" % rc)
    same = ok2 and all(
        [{k: v for k, v in r.items() if k != "secs"} for r in read_rows(os.path.join(d2, os.path.basename(x)))]
        == [{k: v for k, v in r.items() if k != "secs"} for r in read_rows(x)] for x in (s1, s2))
    report("D2b the driver's records equal the directly generated ones in every field except secs", same)
    rc, out = run(drv(d2, "--plan", "test", "--jobs", "2", "--skip-fixtures", flog))
    report("D3 driver refuses a non-empty output directory without --resume", rc == 2, "exit %d" % rc)

    def driver_failure(name, mutate, must, extra=("--resume",), flog_=flog):
        d = os.path.join(work, "d_%02d" % (N_CASES + 1))
        shutil.copytree(d2, d)
        mutate(d)
        rc, out = run(drv(d, "--plan", "test", "--jobs", "2", "--skip-fixtures", flog_, *extra))
        failed = os.path.join(d, "CAMPAIGN_FAILED.txt")
        text = open(failed).read() if os.path.exists(failed) else ""
        report(name, rc == 1 and must in text and not os.path.exists(os.path.join(d, "CAMPAIGN_COMPLETE.json")),
               "exit %d; marker absent: %s" % (rc, not os.path.exists(os.path.join(d, "CAMPAIGN_COMPLETE.json"))))

    def tamper_identity(d):
        p = os.path.join(d, os.path.basename(s1))
        rows = read_rows(p)
        rows[0]["T"] = 801
        write_rows(p, rows)
    driver_failure("D4 a worker that exits non-zero fails the campaign (record of another identity in a shard)",
                   tamper_identity, "worker exit codes")

    def tamper_law(d):
        p = os.path.join(d, os.path.basename(s1))
        rows = read_rows(p)
        rows[0]["law_viol"] = 1
        write_rows(p, rows)
    driver_failure("D5 an analysis that exits non-zero fails the campaign (gate G2)", tamper_law, "analysis of TEST-C1 exited with code 3")

    def drop_shard_record(d):
        p = os.path.join(d, os.path.basename(s2))
        rows = read_rows(p)
        write_rows(p, rows[:-1])
        os.remove(p + ".manifest.json")
    d = os.path.join(work, "d_incomplete")
    shutil.copytree(d2, d)
    drop_shard_record(d)
    rc, out = run(drv(d, "--plan", "test", "--jobs", "2", "--skip-fixtures", flog, "--resume"))
    report("D6 an incomplete shard is completed by --resume and the campaign then validates",
           rc == 0 and os.path.exists(os.path.join(d, "CAMPAIGN_COMPLETE.json")), "exit %d" % rc)

    # a real fixtures failure: a copy of the needed tree with a changed golden file
    tree = os.path.join(work, "tree")
    for k, rel in REL.items():
        dst = os.path.join(tree, *rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(P[k], dst)
    with open(os.path.join(tree, *REL["golden"])) as f:
        g = json.load(f)
    g["hub_N120_k8_T60"][0] += 1
    with open(os.path.join(tree, *REL["golden"]), "w", newline="\n") as f:
        json.dump(g, f, sort_keys=True, indent=1)
    d7 = os.path.join(work, "d7")
    rc, out = run(PY + [os.path.join(tree, *REL["driver"]), "--plan", "test", "--jobs", "2", "--out", d7])
    failed = os.path.join(d7, "CAMPAIGN_FAILED.txt")
    report("D7 a failing fixtures run stops the campaign before any shard is started",
           rc == 1 and os.path.exists(failed) and "fixtures exited with code 1" in open(failed).read()
           and not any(n.endswith(".jsonl") for n in os.listdir(d7)), "exit %d" % rc)

    print("NEGATIVE CONTROLS %s (%d cases; %.1f s; python %s)" % ("PASS" if OK else "FAIL", N_CASES, time.time() - t0, sys.version.split()[0]))
    return 0 if OK else 1


if __name__ == "__main__":
    raise SystemExit(main())
