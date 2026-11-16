#!/usr/bin/env python3
"""Negative controls of az_tokres_contact_tables.py on copies of a Stage 1 TEST campaign (tag SMOKE). [SESSION]

    python3 -I contact_tables_negcontrols.py --campaign TESTDIR --work EMPTYDIR
One positive control and twelve controls that damage a copy (or the manifest) in one way; each must be refused with
exit code 2 and no table. NC09-NC12 point at the registered Stage 1 records and must be refused before any of them
is looked up (the manifest is unfrozen, or the cell/plan/pin/input is wrong).
"""
import argparse, glob, hashlib, json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "az_tokres_contact_tables.py")
M = os.path.join(HERE, "contact_tables_manifest.json")
OK = True


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def read(p):
    return [json.loads(x) for x in open(p) if x.strip()]


def write(p, recs, restamp=True, hashes=False):
    with open(p, "w", newline="\n") as f:
        f.write("".join(json.dumps(r, sort_keys=True) + "\n" for r in recs))
    if restamp:
        mp = p + ".manifest.json"
        mans = read(mp)
        mans[-1]["file_sha256"] = sha(p)
        mans[-1]["rows_total"] = len(recs)
        with open(mp, "w", newline="\n") as f:
            f.write("".join(json.dumps(m, sort_keys=True) + "\n" for m in mans))
    if hashes:                                   # also re-stamp the directory's own trusted list (test plan only)
        d = os.path.dirname(p)
        hp = os.path.join(d, "HASHES.txt")
        lines = []
        for ln in open(hp):
            h, n = ln.split()
            lines.append("%s  %s\n" % (sha(os.path.join(d, n)) if os.path.exists(os.path.join(d, n)) else h, n))
        open(hp, "w", newline="\n").writelines(lines)


def run(d, plan="test", manifest=M):
    p = subprocess.run([sys.executable, "-I", T, "--manifest", manifest, "--dir", d, "--plan", plan], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def check(name, rc, text, want_rc, want):
    global OK
    good = rc == want_rc and want in text and (want_rc == 0 or ("T1 population" not in text and "T2 first-contact" not in text))
    OK &= good
    print("%s  %s (exit %d, expected %d; %r)" % ("PASS" if good else "FAIL", name, rc, want_rc, want))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--campaign", required=True)
    ap.add_argument("--work", required=True)
    a = ap.parse_args()
    src, work = os.path.abspath(a.campaign), os.path.abspath(a.work)
    if os.path.exists(work) and os.listdir(work):
        sys.exit("--work must be empty")
    os.makedirs(work, exist_ok=True)

    def case(n):
        d = os.path.join(work, n)
        shutil.copytree(src, d)
        return d
    first = lambda d, c: sorted(glob.glob(os.path.join(d, c + "_*.jsonl")))[0]

    d = case("nc00"); rc, t = run(d); check("NC00 positive control: untouched copy is tabulated", rc, t, 0, "INTEGRITY: PASS")
    # binding to the trusted list (R2)
    d = case("nc01"); p = first(d, "TEST-C1"); r = read(p); write(p, r[:-1]); rc, t = run(d)
    check("NC01 one record dropped, side manifest re-stamped: not the listed bytes", rc, t, 2, "does not have the listed hash")
    d = case("nc02"); p = first(d, "TEST-C1"); q = p.replace("_00000_", "_99999_"); shutil.copyfile(p, q); shutil.copyfile(p + ".manifest.json", q + ".manifest.json"); rc, t = run(d)
    check("NC02 an unlisted copy of a record file in the directory", rc, t, 2, "is not in the trusted list")
    d = case("nc03"); p = first(d, "TEST-C1"); os.remove(p + ".manifest.json"); rc, t = run(d)
    check("NC03 a listed side manifest missing", rc, t, 2, "is missing")
    d = case("nc04"); p = first(d, "TEST-C1"); r = read(p)
    i = next(j for j, x in enumerate(r) if x["arm"] == "O1R"); j = next(j for j, x in enumerate(r) if x["arm"] == "O1R" and x["base"] != r[i]["base"])
    r[i]["th0"], r[j]["th0"] = r[j]["th0"], r[i]["th0"]; write(p, r); rc, t = run(d)
    check("NC04 pairing keys swapped, record and side manifest re-stamped together", rc, t, 2, "does not have the listed hash")
    # deeper layers, reached only by also re-stamping the test directory's own list
    d = case("nc05"); p = first(d, "TEST-C1"); r = read(p)
    i = next(j for j, x in enumerate(r) if x["arm"] == "O1R"); j = next(j for j, x in enumerate(r) if x["arm"] == "O1R" and x["base"] != r[i]["base"])
    r[i]["th0"], r[j]["th0"] = r[j]["th0"], r[i]["th0"]; write(p, r, hashes=True); rc, t = run(d)
    check("NC05 swapped pairing keys with every hash re-stamped: Stage 1 state re-derivation", rc, t, 2, "INTEGRITY: FAIL")
    d = case("nc06"); p = first(d, "TEST-C1"); r = read(p); r[0]["fe"] = 801; write(p, r, hashes=True); rc, t = run(d)
    check("NC06 fe = 801 with every hash re-stamped: clock layer", rc, t, 2, "is not None or an integer in 1..steps")
    d = case("nc07"); p = first(d, "TEST-C1"); r = read(p)
    i = next(j for j, x in enumerate(r) if x["fe"] is not None and x["fe"] > 1 and not x["arm"].endswith("_P")); r[i]["fe"] = 1; r[i]["fb"] = 1 if r[i]["fb"] is not None else None
    write(p, r, hashes=True); rc, t = run(d)
    check("NC07 fe moved before tau_contact with every hash re-stamped: clock layer", rc, t, 2, "fe < tau_contact")
    d = case("nc08"); p = first(d, "TEST-C1"); r = read(p)
    i = next(j for j, x in enumerate(r) if x["steps"] == 800 and not x["arm"].endswith("_P")); r[i]["M_at"] = {key: 4 for key in r[i]["M_at"]}   # the reviewer's case: steps 800, M >= 4, every checkpoint 4
    write(p, r, hashes=True); rc, t = run(d)
    check("NC08 tick-800 checkpoint below the final M at steps = 800, re-stamped: clock layer", rc, t, 2, "checkpoint at the last tick differs from M")
    # plan, cells, freeze and pins (R1, R2): refused before any record is looked up
    man = json.load(open(M))
    mp = os.path.join(work, "m_testS1.json"); json.dump(dict(man, cells_test=["S1-C1"]), open(mp, "w"))
    reg = os.path.join(os.path.dirname(os.path.dirname(HERE)), "..", "upload", "az-token-resonance-stage1")
    rc, t = run(os.path.normpath(reg), manifest=mp)
    check("NC09 test plan naming S1-C1 pointed at the registered records: refused, nothing validated", rc, t, 2, "REFUSED: cells for plan test")
    rc, t = run(os.path.normpath(reg), plan="registered")
    check("NC10 registered plan with the unfrozen manifest", rc, t, 2, "REFUSED: manifest is not frozen")
    fz = dict(man, frozen_script_sha256=sha(T))
    mp = os.path.join(work, "m_badinput.json"); json.dump(dict(fz, inputs=[dict(fz["inputs"][0], sha256="0" * 64)]), open(mp, "w"))
    rc, t = run(os.path.normpath(reg), plan="registered", manifest=mp)
    check("NC11 registered plan, frozen hash right, input hash wrong", rc, t, 2, "does not have the manifest's hash")
    mp = os.path.join(work, "m_badpin.json"); json.dump(dict(fz, pins=dict(fz["pins"], engine="0" * 64)), open(mp, "w"))
    rc, t = run(os.path.normpath(reg), plan="registered", manifest=mp)
    check("NC12 registered plan, frozen hash right, manifest engine pin wrong", rc, t, 2, "manifest pin engine differs")
    print("NEGCONTROLS", "PASS" if OK else "FAIL")
    return 0 if OK else 1


if __name__ == "__main__":
    raise SystemExit(main())
