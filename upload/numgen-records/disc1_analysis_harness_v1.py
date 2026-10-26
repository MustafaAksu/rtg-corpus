#!/usr/bin/env python3
# =============================================================================
# DISC-1B / DISC-1D ANALYSIS HARNESS  v1   —  FROZEN BEFORE DATA
# =============================================================================
# Base: RTG_NUMBER_GENESIS_DSN_v1.15 + frozen discrimination architecture
#       (NG_N5_DISCRIMINATION_CRITERION_v5/v6, PI ruling 2026-08-31).
#
# PURPOSE. Consume a per-seed/per-k BIND3 cycle enumeration and emit the
# DISC-1B census and the DISC-1D transport audit under the ALREADY-FROZEN pass
# rule. Freezing the analysis code before the artifact exists is the point:
# no thresholds, no witness sets and no pass conditions can be tuned after
# seeing ratios.
#
# THIS HARNESS DOES NOT SIMULATE TDR-G. It deliberately implements no swap/P3
# kinematics, no CONV-TICK, no CONV-P3CYC. Those are owner mechanisms and
# guessing them here would fabricate an owner result. The harness consumes an
# enumeration produced by the owner simulator.
#
# INPUT CONTRACT (JSON list of records; one per (seed, k)):
#   {"seed_id": <str>,        # frozen raw relational initial state id
#    "k": <int in {0,1,2,3}>,
#    "dual_active": <bool>,   # eventual cycle has BOTH counts > 0
#    "n_swap": <int>,         # per-cycle SWAP count a
#    "n_p3":   <int>,         # per-cycle active-P3 count b
#    "cycle_len": <int>}      # optional, for reporting only
#   Records with dual_active=false must still be present (null marker).
#
# FROZEN PARAMETERS — DO NOT EDIT AFTER DATA IS SEEN:
K_DISC     = (0, 1, 2, 3)   # admissible deformation set, fixed N=24
K_BASE     = 1              # base (DISC-1B preregistration point)
K_STAB     = (2,)           # elementary positive-band neighbour of base
K_CONT     = (0, 3)         # contingency witnesses (0 = boundary control)
# Rationale (PI ruling): k=0 is admissible but is a zero-width boundary
# stratum for the retrigger structure feeding BIND3, so it is a boundary
# comparison control, not a stability edge. Adjacency is inside the
# positive-band stratum: 1~2, 2~3.
# =============================================================================
import json, sys
from math import gcd
from collections import defaultdict

def reduced(a, b):
    if a <= 0 or b <= 0: return None
    g = gcd(a, b)
    return (a // g, b // g)

def load(records):
    tab = {}
    for r in records:
        tab[(r["seed_id"], r["k"])] = r
    return tab

def analyse(records):
    tab = load(records)
    seeds = sorted({r["seed_id"] for r in records})
    cls = {}
    for (s, k), r in tab.items():
        cls[(s, k)] = reduced(r["n_swap"], r["n_p3"]) if r.get("dual_active") else None

    out = {"n_seeds": len(seeds)}

    # ---------------- DISC-1B: non-1 census at the base -------------------
    base_active = [s for s in seeds if cls.get((s, K_BASE)) is not None]
    base_classes = [cls[(s, K_BASE)] for s in base_active]
    non1 = [c for c in base_classes if c != (1, 1)]
    out["disc1b"] = {
        "n_base_dual_active": len(base_active),
        "class_multiset": sorted({c: base_classes.count(c) for c in set(base_classes)}.items()),
        "n_non1": len(non1),
        "verdict": "PASS (non-1 class present)" if non1 else
                   "FAIL (all dual-active base cycles reduce to 1:1)",
    }

    # ---------------- DISC-1D: same-realization transport audit -----------
    per_k_active = {k: sum(1 for s in seeds if cls.get((s, k)) is not None) for k in K_DISC}
    eligible, passes = [], []
    for s in base_active:
        r = cls[(s, K_BASE)]
        # local stability fence: elementary positive-band move 1 -> 2
        stab = any(cls.get((s, k)) == r for k in K_STAB)
        if not stab:
            continue
        eligible.append(s)
        wit_int = [k for k in K_CONT if k == 3 and cls.get((s, k)) not in (None, r)]
        wit_bdy = [k for k in K_CONT if k == 0 and cls.get((s, k)) not in (None, r)]
        if wit_int or wit_bdy:
            passes.append({
                "seed_id": s, "class": r,
                "subtype": "DISC-1D-PASS-INT" if wit_int else "DISC-1D-PASS-BDY",
                "contingency_k": (wit_int or wit_bdy),
            })

    # frozen null taxonomy, stated observationally
    if passes:
        verdict = "PASS"
    elif not eligible:
        verdict = ("FAIL — no base candidate survives the positive-band "
                   "elementary move 1->2 (no local stability)")
    else:
        any_cont = any(cls.get((s, k)) not in (None, cls[(s, K_BASE)])
                       for s in base_active for k in K_CONT)
        verdict = ("FAIL — stability and contingency both present on the panel "
                   "but never on one seed (same-realization guard binding)"
                   if any_cont else
                   "FAIL — no contingency witness on the frozen k axis")

    out["disc1d"] = {
        "n_dual_active_by_k": per_k_active,
        "n_eligible_after_stability_fence": len(eligible),
        "n_pass_interior_k3": sum(1 for p in passes if p["subtype"].endswith("INT")),
        "n_pass_boundary_only_k0": sum(1 for p in passes if p["subtype"].endswith("BDY")),
        "admitted_class_multiset": sorted({str(p["class"]): 
            sum(1 for q in passes if q["class"] == p["class"]) for p in passes}.items()),
        "verdict": verdict,
    }
    out["transport_tuples"] = {
        s: [cls.get((s, k)) for k in K_DISC] for s in seeds
    }
    return out

# ------------------------- self-test on synthetic input ---------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps(analyse(json.load(open(sys.argv[1]))), indent=2, default=str))
        sys.exit(0)
    def rec(s, k, a, b):
        return {"seed_id": s, "k": k, "dual_active": a > 0 and b > 0,
                "n_swap": a, "n_p3": b, "cycle_len": a + b}
    synth = [
        # seed A: class 3:2 at k=1, stable at k=2, destroyed at k=3 -> PASS-INT
        rec("A",0,3,2), rec("A",1,3,2), rec("A",2,6,4), rec("A",3,5,2),
        # seed B: stable at k=2, destroyed only at k=0 -> PASS-BDY
        rec("B",0,2,1), rec("B",1,3,2), rec("B",2,3,2), rec("B",3,3,2),
        # seed C: not stable at k=2 -> ineligible
        rec("C",0,1,1), rec("C",1,5,1), rec("C",2,4,1), rec("C",3,4,1),
        # seed D: 1:1 everywhere -> eligible, no contingency
        rec("D",0,1,1), rec("D",1,1,1), rec("D",2,1,1), rec("D",3,1,1),
        # seed E: not dual-active at base
        rec("E",0,1,1), rec("E",1,4,0), rec("E",2,2,1), rec("E",3,2,1),
    ]
    res = analyse(synth)
    print(json.dumps(res, indent=2, default=str))
    ok = (res["disc1b"]["verdict"].startswith("PASS")
          and res["disc1d"]["n_pass_interior_k3"] == 1
          and res["disc1d"]["n_pass_boundary_only_k0"] == 1
          and res["disc1d"]["n_eligible_after_stability_fence"] == 3)
    print("\nSELF-TEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
