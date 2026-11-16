#!/usr/bin/env python3
"""Negative controls of az_tokres_contact_tables.py on copies of a Stage 1 TEST campaign (tag SMOKE). [SESSION]

    python3 -I contact_tables_negcontrols.py --campaign TESTDIR --work EMPTYDIR
Each control damages a copy in one way; the table script must refuse it (exit code 2, no table printed).
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


def write(p, recs, restamp=True):
    with open(p, "w", newline="\n") as f:
        f.write("".join(json.dumps(r, sort_keys=True) + "\n" for r in recs))
    if restamp:
        mp = p + ".manifest.json"
        mans = read(mp)
        mans[-1]["file_sha256"] = sha(p)
        mans[-1]["rows_total"] = len(recs)
        with open(mp, "w", newline="\n") as f:
            f.write("".join(json.dumps(m, sort_keys=True) + "\n" for m in mans))


def run(d, plan="test", manifest=M):
    p = subprocess.run([sys.executable, "-I", T, "--manifest", manifest, "--dir", d, "--plan", plan], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def check(name, rc, text, want_rc, want):
    global OK
    good = rc == want_rc and want in text and (want_rc == 0 or "T2 first-contact" not in text)
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

    d = case("nc0"); rc, t = run(d); check("NC0 untouched copy is tabulated", rc, t, 0, "INTEGRITY: PASS")
    d = case("nc1"); p = first(d, "TEST-C1"); r = read(p); write(p, r[:-1]); rc, t = run(d)
    check("NC1 one record dropped (a non-attainer or any other)", rc, t, 2, "missing record")
    d = case("nc2"); p = first(d, "TEST-C1"); shutil.copyfile(p, p.replace("_00000_", "_99999_")); shutil.copyfile(p + ".manifest.json", p.replace("_00000_", "_99999_") + ".manifest.json"); rc, t = run(d)
    check("NC2 record file duplicated under another name", rc, t, 2, "INTEGRITY: FAIL")
    d = case("nc3"); p = first(d, "TEST-C1"); r = read(p)
    i = next(j for j, x in enumerate(r) if x["arm"] == "O1R")
    j = next(j for j, x in enumerate(r) if x["arm"] == "O1R" and x["base"] != r[i]["base"])
    r[i]["th0"], r[j]["th0"] = r[j]["th0"], r[i]["th0"]; write(p, r); rc, t = run(d)
    check("NC3 pairing keys swapped between two base draws (manifest re-stamped)", rc, t, 2, "INTEGRITY: FAIL")
    d = case("nc4"); p = first(d, "TEST-C1"); r = read(p)
    for x in r:
        x["engine_sha256"] = "0" * 64
    write(p, r); rc, t = run(d)
    check("NC4 records carry a wrong engine pin", rc, t, 2, "INTEGRITY: FAIL")
    d = case("nc5"); p = first(d, "TEST-C1"); r = read(p); r[0]["fb"] = (r[0]["fb"] or 0) + 1; write(p, r, restamp=False); rc, t = run(d)
    check("NC5 record file changed after the run (clock field edited, manifest not re-stamped)", rc, t, 2, "INTEGRITY: FAIL")
    rc, t = run(case("nc6"), plan="registered")
    check("NC6 registered plan with the unfrozen manifest", rc, t, 2, "REFUSED: manifest is not frozen")
    man = json.load(open(M)); man["frozen_script_sha256"] = sha(T); man["inputs"][0]["sha256"] = "0" * 64
    mp = os.path.join(work, "manifest_badinput.json"); json.dump(man, open(mp, "w"))
    rc, t = run(case("nc7"), plan="registered", manifest=mp)
    check("NC7 registered plan, frozen hash right, input hash wrong", rc, t, 2, "does not have the manifest's hash")
    print("NEGCONTROLS", "PASS" if OK else "FAIL")
    return 0 if OK else 1


if __name__ == "__main__":
    raise SystemExit(main())
