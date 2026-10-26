#!/usr/bin/env python3
# DISC-1 LABEL-NEUTRALITY + VERDICT-STATE REGRESSION  v2
# Enforces [PI-RULING] DISC-1D is label-neutral (2026-08-31) mechanically,
# so the ruling cannot be silently violated by a later harness edit.
# v1 -> v2: added CASE 4 (PASS/PASS) and CASE 5 (FAIL/FAIL) so that all four
#   logically distinct verdict states enumerated in the review are actually
#   exercised, not merely asserted to be representable.
# Exit 0 iff all cases behave as ruled.
import sys, json, importlib.util
spec=importlib.util.spec_from_file_location("h","disc1_analysis_harness_v1.py")
h=importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
F=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: F.append(n)
def rec(s,k,a,b):
    return {"seed_id":s,"k":k,"dual_active":a>0 and b>0,"n_swap":a,"n_p3":b,"cycle_len":a+b}

# CASE 1 — the ruled mixed verdict: every dual-active base cycle is 1:1
# (DISC-1B must FAIL) while seed P is stable at k=2 and destroyed at k=3
# (DISC-1D must PASS, admitting 1 in Q^dyn).
case1=[ rec("P",0,1,1), rec("P",1,1,1), rec("P",2,2,2), rec("P",3,3,1),
        rec("Q",0,1,1), rec("Q",1,1,1), rec("Q",2,1,1), rec("Q",3,1,1),
        rec("R",0,2,1), rec("R",1,5,0), rec("R",2,1,1), rec("R",3,1,1) ]
r1=h.analyse(case1)
ck("L1 DISC-1B FAILS when every dual-active base cycle reduces to 1:1 "
   "(original v1.15 falsifier intact)", r1["disc1b"]["verdict"].startswith("FAIL"))
ck("L2 DISC-1D still RUNS on 1:1 base candidates and is not halted by the "
   "DISC-1B failure", r1["disc1d"]["n_eligible_after_stability_fence"]>=1)
ck("L3 DISC-1D PASSES at 1:1 for the same realization (stable at k=2, "
   "destroyed at k=3) -> admits 1 in Q^dyn",
   r1["disc1d"]["verdict"]=="PASS" and r1["disc1d"]["n_pass_interior_k3"]==1)
ck("L4 the admitted class is recorded as 1:1, so a label-1 admission is "
   "visible in the report rather than hidden",
   any("(1, 1)" in str(k) for k,_ in r1["disc1d"]["admitted_class_multiset"]))
ck("L5 the DISC-1D pass does NOT repair DISC-1B: its verdict is untouched "
   "and still records the non-1 breadth failure",
   r1["disc1b"]["n_non1"]==0 and r1["disc1b"]["verdict"].startswith("FAIL"))

# CASE 2 — the converse mixed verdict: non-1 breadth exists (DISC-1B PASS)
# but no seed is both locally stable and contingent (DISC-1D FAIL).
case2=[ rec("A",0,3,2), rec("A",1,3,2), rec("A",2,5,1), rec("A",3,5,1),
        rec("B",0,7,2), rec("B",1,7,2), rec("B",2,7,2), rec("B",3,7,2) ]
r2=h.analyse(case2)
ck("L6 converse verdict is representable: DISC-1B PASSES on non-1 breadth "
   "while DISC-1D FAILS (a bounded periodic control that does not meet the "
   "discrimination criterion)",
   r2["disc1b"]["verdict"].startswith("PASS") and r2["disc1d"]["verdict"].startswith("FAIL"))
ck("L7 that DISC-1D failure is diagnosed observationally, not causally",
   "FAIL —" in r2["disc1d"]["verdict"])

# CASE 3 — label neutrality is structural: relabelling a passing 1:1 seed's
# counts to a non-1 class with identical transport pattern gives the same
# DISC-1D verdict, i.e. the numeral plays no role in admission.
case3=[ rec("P",0,3,2), rec("P",1,3,2), rec("P",2,6,4), rec("P",3,3,1),
        rec("Q",0,1,1), rec("Q",1,1,1), rec("Q",2,1,1), rec("Q",3,1,1),
        rec("R",0,2,1), rec("R",1,5,0), rec("R",2,1,1), rec("R",3,1,1) ]
r3=h.analyse(case3)
ck("L8 admission is mechanism-determined, not numeral-determined: the same "
   "transport pattern passes identically whether the base class is 1:1 or 3:2",
   r3["disc1d"]["verdict"]==r1["disc1d"]["verdict"]
   and r3["disc1d"]["n_pass_interior_k3"]==r1["disc1d"]["n_pass_interior_k3"])

# CASE 4 — PASS/PASS: non-1 breadth exists AND a same realization is both
# locally stable and contingent.
case4=[ rec("A",0,3,2), rec("A",1,3,2), rec("A",2,6,4), rec("A",3,5,1),
        rec("B",0,7,2), rec("B",1,7,2), rec("B",2,7,2), rec("B",3,7,2) ]
r4=h.analyse(case4)
ck("L9 PASS/PASS state representable: DISC-1B PASSES on non-1 breadth and "
   "DISC-1D PASSES for the same realization",
   r4["disc1b"]["verdict"].startswith("PASS") and r4["disc1d"]["verdict"]=="PASS")

# CASE 5 — FAIL/FAIL: no non-1 breadth and no discriminating realization.
case5=[ rec("A",0,1,1), rec("A",1,1,1), rec("A",2,1,1), rec("A",3,1,1),
        rec("B",0,2,2), rec("B",1,3,3), rec("B",2,4,4), rec("B",3,5,5) ]
r5=h.analyse(case5)
ck("L10 FAIL/FAIL state representable: neither breadth nor dynamic admission "
   "achieved on the tested route",
   r5["disc1b"]["verdict"].startswith("FAIL") and r5["disc1d"]["verdict"].startswith("FAIL"))
ck("L11 all four logically distinct states are therefore reachable through "
   "the frozen harness without conflation: (FAIL,PASS), (PASS,FAIL), "
   "(PASS,PASS), (FAIL,FAIL)",
   len({(r1["disc1b"]["verdict"][:4], r1["disc1d"]["verdict"][:4]),
        (r2["disc1b"]["verdict"][:4], r2["disc1d"]["verdict"][:4]),
        (r4["disc1b"]["verdict"][:4], r4["disc1d"]["verdict"][:4]),
        (r5["disc1b"]["verdict"][:4], r5["disc1d"]["verdict"][:4])})==4)

print("-"*70)
if F: print("FAILURES:",F); sys.exit(1)
print("RESULT: ALL PASS — label-neutrality ruling enforced mechanically; "
      "all four verdict states exercised; DISC-1B and DISC-1D verdicts are "
      "independent.")
sys.exit(0)
