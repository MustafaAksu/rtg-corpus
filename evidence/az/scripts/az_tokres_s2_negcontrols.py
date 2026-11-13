#!/usr/bin/env python3
"""AZ token-resonance Stage 2 - negative controls of the analysis and the driver. [SESSION] NONCANONICAL.

Each control takes a copy of a finished TEST campaign (plan s2test), damages it in one way, and checks that the Stage 2
analysis refuses it with the expected exit code and message. A control that is not refused is a failure of this script.

usage
  python -I az_tokres_s2_negcontrols.py --campaign TESTDIR --work EMPTYDIR
Exit code 0 iff every control behaves as stated.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
ENGINE = os.path.join(ROOT, "upload", "tdrg-records", "genesis_mode_b_mc.py")
ORIENT = os.path.join(ROOT, "evidence", "tdrg", "scripts", "tdrg_orient_v2_12_14.py")
RUNNER = os.path.join(HERE, "az_tokres_run.py")
S1 = os.path.join(HERE, "az_tokres_analyse.py")
S2 = os.path.join(HERE, "az_tokres_s2_analyse.py")
DRIVER = os.path.join(HERE, "az_tokres_s2_campaign.py")
OK = True


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def read(path):
    with open(path) as f:
        return [json.loads(x) for x in f if x.strip()]


def write(path, recs, restamp=True):
    with open(path, "w", newline="\n") as f:
        f.write("".join(json.dumps(r, sort_keys=True) + "\n" for r in recs))
    if restamp:                                    # make the manifest agree, so that the deeper check is the one tested
        mp = path + ".manifest.json"
        mans = read(mp)
        mans[-1]["file_sha256"] = sha(path)
        mans[-1]["rows_total"] = len(recs)
        with open(mp, "w", newline="\n") as f:
            f.write("".join(json.dumps(m, sort_keys=True) + "\n" for m in mans))


def analyse(d, plan="s2test", s1=S1, pilot=None):
    cmd = [sys.executable, "-I", S2, "--plan", plan, "--dir", d, "--engine", ENGINE, "--orient", ORIENT, "--runner", RUNNER,
           "--analysis-s1", s1, "--fixtures-log", os.path.join(d, "fixtures_output.txt")]
    if pilot:
        cmd += ["--pilot-dir", pilot]
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def check(name, rc, text, want_rc, want_text=None, forbid="registered reading"):
    global OK
    good = rc == want_rc and (want_text is None or want_text in text)
    if want_rc != 0:
        good = good and "reading:" not in text and "RD=" not in text      # nothing estimated, nothing read
    OK &= good
    print("%s  %s  (exit code %d, expected %d%s)" % ("PASS" if good else "FAIL", name, rc, want_rc,
                                                    "" if want_text is None else "; message: %r" % want_text))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--campaign", required=True)
    ap.add_argument("--work", required=True)
    a = ap.parse_args()
    src = os.path.abspath(a.campaign)
    work = os.path.abspath(a.work)
    if os.path.exists(work) and os.listdir(work):
        print("REFUSED: --work must be empty", file=sys.stderr)
        return 2
    os.makedirs(work, exist_ok=True)

    def case(name):
        d = os.path.join(work, name)
        shutil.copytree(src, d)
        return d

    first = lambda d, cell: sorted(glob.glob(os.path.join(d, cell + "_*.jsonl")))[0]

    d = case("nc00")
    rc, text = analyse(d)
    check("NC0  untouched copy of the test campaign is analysed", rc, text, 0, "INTEGRITY: PASS")

    d = case("nc01")
    p = first(d, "T2-C240")
    recs = read(p)
    recs[3]["M"] += 1
    write(p, recs)
    rc, text = analyse(d)
    check("NC1  final M of one record changed (manifest re-stamped)", rc, text, 2, "M != 4 + births")

    d = case("nc02")
    p = first(d, "T2-C480")
    recs = read(p)
    recs[0]["secs"] = 0.0
    write(p, recs, restamp=False)
    rc, text = analyse(d)
    check("NC2  record file changed after the run", rc, text, 2, "SHA-256 differs from the manifest")

    d = case("nc03")
    for q in glob.glob(os.path.join(d, "T2-C242_*")):
        os.remove(q)
    rc, text = analyse(d)
    check("NC3  one cell missing", rc, text, 2, "T2-C242: no record file")

    d = case("nc04")
    for q in glob.glob(os.path.join(d, "T2-C240_*")):
        os.remove(q)
    for q in glob.glob(os.path.join(d, "T2-C480_*")):
        shutil.copyfile(q, os.path.join(d, os.path.basename(q).replace("T2-C480", "T2-C240")))
    rc, text = analyse(d)
    check("NC4  records of another cell under this cell's name", rc, text, 2, "identity differs")

    d = case("nc05")
    p = first(d, "T2-C240")
    recs = read(p)
    i = next(j for j, r in enumerate(recs) if not r["hit_cap"])
    del recs[i]["M_at"]["800"]
    write(p, recs)
    rc, text = analyse(d)
    check("NC5  tick-800 checkpoint removed from a run that did not reach the cap", rc, text, 2, "no tick-800 checkpoint")

    d = case("nc06")
    p = first(d, "T2-C242")
    recs = read(p)
    recs[1]["law_viol"] = 1
    write(p, recs)
    rc, text = analyse(d)
    check("NC6  one law violation", rc, text, 3, "GATE FAILURE")

    d = case("nc07")
    fl = os.path.join(d, "fixtures_output.txt")
    with open(fl) as f:
        lines = f.read().rstrip("\n").split("\n")
    with open(fl, "w", newline="\n") as f:
        f.write("\n".join(lines[:-1]) + "\nFIXTURES FAIL\n")
    rc, text = analyse(d)
    check("NC7  fixtures log does not end with FIXTURES PASS", rc, text, 3, "GATE FAILURE")

    d = case("nc08")
    p = first(d, "T2-C480")
    recs = read(p)
    write(p, recs[:-1])
    rc, text = analyse(d)
    check("NC8  one registered record missing", rc, text, 2, "missing record")

    d = case("nc09")
    p = first(d, "T2-C240")
    recs = read(p)
    for r in recs:
        r["T"] = 800
    write(p, recs)
    rc, text = analyse(d)
    check("NC9  records of another horizon", rc, text, 2, "identity differs")

    d = case("nc10")
    fake = os.path.join(d, "s1_modified.py")
    with open(S1) as f:
        body = f.read()
    with open(fake, "w", newline="\n") as f:
        f.write(body + "\n# changed\n")
    rc, text = analyse(d, s1=fake)
    check("NC10 Stage 1 library changed", rc, text, 2, "does not hash to its pin")

    d = case("nc11")
    rc, text = analyse(d, plan="stage2")
    check("NC11 registered plan on a test directory, no pilot directory", rc, text, 2, "--pilot-dir is required")

    # stand-in pilot files made from the test campaign's own BASE records: exercises the pilot path of the analysis
    d = case("nc12")
    pil = os.path.join(d, "pilot_standin")
    os.makedirs(pil)
    sys.dont_write_bytecode = True
    import importlib.util
    spec = importlib.util.spec_from_file_location("s2", S2)
    s2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(s2)
    for cell in s2.PLANS["s2test"]:
        cfg = s2.REGISTRY[cell]
        base = sorted((r for q in sorted(glob.glob(os.path.join(d, cell + "_*.jsonl"))) for r in read(q) if r["arm"] == "BASE"),
                      key=lambda r: r["base"])
        out = [{"N": r["N"], "k": r["k"], "T": r["T"], "arm": "BASE", "base": i, "d0": r["d0"], "native_class": r["alphabet_class"],
                "M": r["M"], "hit_cap": r["hit_cap"], "steps": r["steps"], "M_at": r["M_at"], "law_viol": r["law_viol"]}
               for i, r in enumerate(base)]
        with open(os.path.join(pil, cfg["pilot_file"]), "w", newline="\n") as f:
            f.write("".join(json.dumps(x, sort_keys=True) + "\n" for x in out))
    rc, text = analyse(d, pilot=pil)
    check("NC12 stand-in pilot files are read and reported", rc, text, 0, "pooled p1 (campaign BASE + pilot)")
    pf = os.path.join(pil, s2.REGISTRY["T2-C240"]["pilot_file"])
    recs = read(pf)
    recs[0]["native_class"] = "O1" if recs[0]["native_class"] == "NR" else "NR"
    with open(pf, "w", newline="\n") as f:
        f.write("".join(json.dumps(x, sort_keys=True) + "\n" for x in recs))
    rc, text = analyse(d, pilot=pil)
    check("NC13 pilot class label contradicts the seed tokens", rc, text, 2, "class label differs")
    os.remove(pf)
    rc, text = analyse(d, pilot=pil)
    check("NC14 a pilot file missing", rc, text, 2, "missing")

    # the driver
    def drive(*args):
        p = subprocess.run([sys.executable, "-I", DRIVER] + list(args), capture_output=True, text=True)
        return p.returncode, p.stdout + p.stderr
    rc, text = drive("--plan", "stage2", "--out", os.path.join(work, "drv1"), "--pilot-dir", work)
    check("NC15 driver refuses the registered plan without --confirmatory", rc, text, 2, "REFUSED")
    rc, text = drive("--plan", "s2test", "--out", os.path.join(work, "drv2"), "--confirmatory")
    check("NC16 driver refuses --confirmatory with the test plan", rc, text, 2, "REFUSED")
    rc, text = drive("--plan", "stage2", "--out", os.path.join(work, "drv3"), "--confirmatory")
    check("NC17 driver refuses the registered plan without the pilot directory", rc, text, 2, "REFUSED")
    rc, text = drive("--plan", "stage2", "--out", os.path.join(work, "drv4"), "--confirmatory", "--pilot-dir", os.path.join(work, "nc12", "pilot_standin"))
    check("NC18 driver stops before any run when the pilot files are not the registered ones", rc, text, 1, "pilot files")
    left = [x for x in os.listdir(os.path.join(work, "drv4")) if x.endswith(".jsonl")]
    good = left == []
    globals()["OK"] = OK and good
    print("%s  NC18b no record file was written by the refused registered plan" % ("PASS" if good else "FAIL"))

    print("NEGCONTROLS", "PASS" if OK else "FAIL")
    return 0 if OK else 1


if __name__ == "__main__":
    raise SystemExit(main())
