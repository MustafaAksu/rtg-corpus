#!/usr/bin/env python3
"""check_dyad_v6_4_24_controls.py -- negative controls for check_dyad_v6_4_24.py.
Each control mutates a temporary copy of the candidate and runs the checker with --norebuild. A control is as expected
when the checker exits 1 and the expected gate is among the failing gates.
usage: check_dyad_v6_4_24_controls.py --base V6423 --cand CANDIDATE [--out JSON]    exit 0 all as expected / 1 otherwise
"""
import argparse, json, os, subprocess, sys, tempfile, shutil
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))


def one(s, old, new):
    assert s.count(old) >= 1, old
    return s.replace(old, new, 1)


CONTROLS = [
 ("Q1", "C5", "an adopted OPEN 21 table constant changed (8831/250 -> 8831/251 in the adopted row)",
  lambda s: one(s, "| $517$ | $\\tfrac{33882112}{50625}$ | $\\tfrac{8831}{250}$ |", "| $517$ | $\\tfrac{33882112}{50625}$ | $\\tfrac{8831}{251}$ |")),
 ("Q2", "C4", "S_A rounded down in the new result (492/25 -> 491/25, every occurrence)", lambda s: s.replace("\\tfrac{492}{25}", "\\tfrac{491}{25}")),
 ("Q3", "C3", "an existing RID tag removed", lambda s: one(s, "[RID: DYAD-ALG-P5-RADIAL]", "DYAD-ALG-P5-RADIAL")),
 ("Q4", "C3", "an eighth RID added", lambda s: one(s, "**Primitive-variable phase remainder, sharpened R9 rows.**", "[RID: DYAD-THM-EXTRA] **Primitive-variable phase remainder, sharpened R9 rows.**")),
 ("Q5", "C7", "a section 2 Status line changed", lambda s: one(s, "Status: ", "Status:  ")),
 ("Q6", "C6", "footer marked ADOPTED", lambda s: one(s, "(DRAFT candidate, 11 November 2026).*", "(ADOPTED, 11 November 2026).*")),
 ("Q7", "C8", "a cited artifact hash altered", lambda s: one(s, "325c2a8a787a5660d5acc243e5b27fcfc91fc225460b0ada9d4b52464c0130ef", "325c2a8a787a5660d5acc243e5b27fcfc91fc225460b0ada9d4b52464c0130ee")),
 ("Q8", "C2", "an undeclared second retag ([THM] -> [ALG] on the smooth flow embedding readout)", lambda s: one(s, "`[THM]` `[v6.4.18]` `[scope: $C^\\infty$ local germs at $P_1$]` **Smooth flow embedding", "`[ALG]` `[v6.4.18]` `[scope: $C^\\infty$ local germs at $P_1$]` **Smooth flow embedding")),
 ("Q9", "C4", "a superseded register wording restored", lambda s: one(s, "(current edition v0.3.27, §7.0;", "(current edition v0.3.26, §7.0);(")),
 ("Q10", "C11", "the Triadic hash altered", lambda s: one(s, "506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a", "506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64b")),
 ("Q11", "C5", "the R9 assumption dropped from the new result", lambda s: one(s, "`[THM]` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]` [RID: DYAD-THM-OPEN21-SHARP-ROWS]", "`[THM]` [RID: DYAD-THM-OPEN21-SHARP-ROWS]")),
 ("Q12", "C9", "the stage-2b figure overstated (1.6e-5 -> 1.6e-3)", lambda s: one(s, "1.6\\cdot10^{-5}", "1.6\\cdot10^{-3}")),
]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--base", required=True); ap.add_argument("--cand", required=True)
    ap.add_argument("--out", default="check_dyad_v6_4_24_controls.json"); a = ap.parse_args()
    C = open(a.cand, encoding="utf-8").read(); res = {}; ok = True
    for cid, gate, what, f in CONTROLS:
        td = tempfile.mkdtemp()
        try:
            p = os.path.join(td, "cand.md"); open(p, "w", encoding="utf-8", newline="").write(f(C))
            r = subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, "check_dyad_v6_4_24.py"), "--base", os.path.abspath(a.base),
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
