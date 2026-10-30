#!/usr/bin/env python3
"""check_dyad_v6_4_23_controls.py -- negative controls for check_dyad_v6_4_23.py.
Each control mutates a temporary copy of the candidate and runs the checker with --norebuild. A control is as expected
when the checker exits 1 and the expected gate is among the failing gates.
usage: check_dyad_v6_4_23_controls.py --base V6422 --cand CANDIDATE [--out JSON]    exit 0 all as expected / 1 otherwise
"""
import argparse, json, os, subprocess, sys, tempfile, shutil
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))


def one(s, old, new):
    assert s.count(old) >= 1, old
    return s.replace(old, new, 1)


CONTROLS = [
 ("Q1", "C5", "scope note of DYAD-THM-OPEN18 dropped", lambda s: one(s, " `[scope: historical first-footprint formulation;", " `[note: historical first-footprint formulation;")),
 ("Q2", "C2", "403/250 changed in the L-PHASE theorem", lambda s: one(s, "|r_m|\\le\\tfrac{403}{250}\\,Q_m^{3/2}", "|r_m|\\le\\tfrac{403}{251}\\,Q_m^{3/2}")),
 ("Q3", "C3", "an existing RID tag removed", lambda s: one(s, "[RID: DYAD-ALG-P5-RADIAL]", "DYAD-ALG-P5-RADIAL")),
 ("Q4", "C4", "old c'_Q display restored in the proof outline", lambda s: one(s, "$c'_Q=0.36916$, from the exact polynomial", "$c'_Q=0.36915$, from the exact polynomial")),
 ("Q5", "C2", "unlogged change outside the edits (OPEN 11 range)", lambda s: one(s, "Chirality closure on scoped canonical family $(\\rho_0,\\eta_0)=(0,q)$, $q\\in(0,2]$", "Chirality closure on scoped canonical family $(\\rho_0,\\eta_0)=(0,q)$, $q\\in(0,3]$")),
 ("Q6", "C7", "a section 2 Status line changed", lambda s: one(s, "Status: ", "Status:  ")),
 ("Q7", "C6", "footer marked ADOPTED", lambda s: one(s, "(DRAFT candidate, 30 October 2026).*", "(ADOPTED, 30 October 2026).*")),
 ("Q8", "C5", "successor interval widened to a non-outward value", lambda s: one(s, "1.260214202563477114872438560958]", "1.26021420256347711487243856096]")),
 ("Q9", "C3", "a fifth RID added", lambda s: one(s, "**Sharper $C_7$ rows.**", "[RID: DYAD-THM-EXTRA] **Sharper $C_7$ rows.**")),
]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--base", required=True); ap.add_argument("--cand", required=True)
    ap.add_argument("--out", default="check_dyad_v6_4_23_controls.json"); a = ap.parse_args()
    C = open(a.cand, encoding="utf-8").read(); res = {}; ok = True
    for cid, gate, what, f in CONTROLS:
        td = tempfile.mkdtemp()
        try:
            p = os.path.join(td, "cand.md"); open(p, "w", encoding="utf-8", newline="").write(f(C))
            r = subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, "check_dyad_v6_4_23.py"), "--base", os.path.abspath(a.base),
                                "--cand", p, "--norebuild", "--out", os.path.join(td, "o.json")], capture_output=True, text=True)
            fails = [l.split()[0] for l in r.stdout.splitlines() if l.endswith(" FAIL") and l.startswith("C")]
            good = r.returncode == 1 and gate in fails
        finally:
            shutil.rmtree(td)
        res[cid] = {"what": what, "expected_gate": gate, "exit": r.returncode, "failing_gates": fails, "as_expected": good}
        ok = ok and good
        print(cid, "as expected" if good else "NOT AS EXPECTED", gate, fails)
    print("ALL CONTROLS AS EXPECTED" if ok else "CONTROL FAILURE")
    with open(a.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"controls": res, "all_as_expected": ok}, fh, indent=1, sort_keys=True, ensure_ascii=False); fh.write("\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
