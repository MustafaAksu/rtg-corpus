#!/usr/bin/env python3
"""
tdr24_policy_geometry_classify.py

Auto-classifies the TDR-24 policy / k-N separation experiment (EXPERIMENT_DESIGN.md)
against the pre-registered decision thresholds. Consumes motif logs produced by
genesis_mode_b_mc.py across policies and k/N values.

Reads each motif CSV, pools late-window bulk observables per (policy, N, k/N) cell:
  C_birth   = births/occ_clean
  chi       = occ_in_clean_star/clean_star_components
  B_per_step= births/row
  O_per_step= occ_clean/row
Then:
  - Experiment 1 (policy at fixed N,k/N): amplitude-gap test -> DISCRETE-CLEAN / ENTANGLED
  - Experiment 2 (k/N sweep at fixed policy): per-N k/N-exponent; cross-N drift test
    -> Case 1 (pure smooth) / Case 2 (structural bending) / Case 3 (regime crossover)

Branch-local [NUM diagnostic]. No promotion; SG-PROG firewall applies.

Usage:
  python tdr24_policy_geometry_classify.py motif_*.csv
"""

import csv
import sys
import math
from collections import defaultdict


def pool_cell(path, step_min=4001, tail_threshold=500, max_nodes=10000):
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    bulk = {r for r, m in rf.items() if m <= tail_threshold}
    n_runs = len(rf)
    # cap-conditioning detection: runs at/above ~90% of the node cap are cap-pressured;
    # high tail-exclusion fraction under an avalanche policy signals cap-conditioned dynamics.
    n_cap = sum(1 for m in rf.values() if m >= 0.9 * max_nodes)
    frac_excluded = 1.0 - len(bulk) / n_runs if n_runs else 0.0
    cap_conditioned = (n_cap > 0) or (frac_excluded > 0.20)
    a = defaultdict(float); meta = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            if v[C["run_id"]] not in bulk: continue
            if int(v[C["step"]]) < step_min: continue
            a["oic"] += float(v[C["occ_clean_pairs_in_clean_star"]])
            a["occ"] += float(v[C["occ_clean_pairs"]])
            a["cs"] += float(v[C["clean_star_components"]])
            a["b"] += float(v[C["births_step"]])
            a["rows"] += 1
            if not meta:
                meta = {"N": int(v[C["N"]]), "k": int(v[C["k"]]),
                        "policy": v[C["policy"]] if "policy" in C else "unknown"}
    if not a["rows"] or not a["occ"] or not a["cs"]:
        return None
    obs = {
        "C_birth": a["b"] / a["occ"],
        "chi": a["oic"] / a["cs"],
        "B_per_step": a["b"] / a["rows"],
        "O_per_step": a["occ"] / a["rows"],
    }
    return {**meta, "k_over_N": meta["k"] / meta["N"], "obs": obs, "n_bulk": len(bulk),
            "n_runs": n_runs, "n_cap": n_cap, "frac_excluded": frac_excluded,
            "cap_conditioned": cap_conditioned}


def fit(pts):
    lx = [math.log(p[0]) for p in pts]; ly = [math.log(p[1]) for p in pts]
    n = len(lx); mx = sum(lx)/n; my = sum(ly)/n
    sxx = sum((x-mx)**2 for x in lx)
    a = sum((lx[i]-mx)*(ly[i]-my) for i in range(n))/sxx
    b = my - a*mx
    ss = sum((y-my)**2 for y in ly); sr = sum((ly[i]-(a*lx[i]+b))**2 for i in range(n))
    return a, (1 - sr/ss if ss else 1.0)


OBS = ["C_birth", "chi", "B_per_step", "O_per_step"]


def main(paths):
    cells = [c for c in (pool_cell(p) for p in paths) if c]
    if not cells:
        print("no valid cells"); return 2

    # ---- Experiment 0: N-anchor at fixed (k/N, policy) ----
    print("=== Experiment 0: N-scaling anchor (fixed k/N, fixed policy) ===")
    by_polkn = defaultdict(list)
    for c in cells:
        by_polkn[(c["policy"], round(c["k_over_N"], 5))].append(c)
    for (policy, kn), cs in sorted(by_polkn.items()):
        Ns = sorted(set(c["N"] for c in cs))
        if len(Ns) < 3:
            continue
        print(f"  policy={policy} k/N={kn} ({len(Ns)} N): N-exponents")
        for o in OBS:
            pts = [(c["N"], c["obs"][o]) for c in sorted(cs, key=lambda x: x["N"])]
            a, r = fit(pts)
            print(f"     {o:12s} ~ N^{a:+.3f} (R²{r:.2f})")
    print()

    # ---- Experiment 1: policy at fixed (N, k/N) ----
    by_ctrl = defaultdict(dict)
    for c in cells:
        by_ctrl[(c["N"], round(c["k_over_N"], 5))][c["policy"]] = c["obs"]
    print("=== Experiment 1: policy-sliced invariance (fixed N, k/N) ===")
    exp1_seen = False
    for (N, kn), pol in by_ctrl.items():
        if len(pol) < 2:
            continue
        exp1_seen = True
        print(f"  (N={N}, k/N={kn}): policies {sorted(pol)}")
        base = "bound_symmetric" if "bound_symmetric" in pol else sorted(pol)[0]
        big_gaps = 0
        for o in OBS:
            vals = {p: pol[p][o] for p in pol}
            lo = min(vals.values()); hi = max(vals.values())
            ratio = hi/lo if lo else float("inf")
            if ratio > 2: big_gaps += 1
            print(f"     {o:12s}: " + ", ".join(f"{p.split('_')[0]}={vals[p]:.4g}" for p in sorted(vals))
                  + f"   max/min={ratio:.2f}")
        # Factorization probe: if O = f(N,k/N)*g(pi), then for each policy the ratio
        # O_pi / O_base should be the SAME across all observables (a pure g(pi) factor).
        # Observable-dependent ratios => policy couples beyond a scalar amplitude.
        print("     factorization probe (O_pi/O_base per observable; equal across obs => multiplicative):")
        for p in sorted(pol):
            if p == base: continue
            ratios = {o: (pol[p][o]/pol[base][o] if pol[base][o] else float('inf')) for o in OBS}
            rv = [r for r in ratios.values() if r != float('inf')]
            spread = (max(rv)/min(rv)) if rv and min(rv) > 0 else float('inf')
            tag = "consistent (multiplicative)" if spread < 1.5 else "observable-dependent (coupling)"
            print(f"       {p.split('_')[0]:8s}: " + ", ".join(f"{o.split('_')[0]}={ratios[o]:.2f}" for o in OBS)
                  + f"  spread={spread:.2f} -> {tag}")
        # cap-conditioning: find which policies in this slice are cap-pressured
        cap_pols = []
        for c in cells:
            if (c["N"], round(c["k_over_N"], 5)) == (N, kn) and c.get("cap_conditioned"):
                cap_pols.append(c["policy"])
        verdict = "AMPLITUDE-GAP PRESENT" if big_gaps >= 2 else "weak gaps"
        if cap_pols:
            print(f"     [CAP-CONDITIONED policies: {sorted(set(cap_pols))} — "
                  f"n_cap/frac_excluded triggered]")
            print(f"     -> {verdict} ({big_gaps}/4) but verdict DOWNGRADED to "
                  f"[NUM, cap-censored]: amplitude gaps vs a cap-censored policy are NOT "
                  f"clean multiplicative separability. Pre-registered guard.")
        else:
            print(f"     -> {verdict} ({big_gaps}/4 observables differ >2x). "
                  f"Case A/B/C requires Exp2 exponent-invariance; this slice only tests "
                  f"multiplicativity.")
    if not exp1_seen:
        print("  (no fixed-(N,k/N) cell has >=2 policies; supply Experiment-1 runs)")

    # ---- Experiment 2: k/N sweep at fixed policy ----
    print("\n=== Experiment 2: k/N-exponent geometry (fixed policy) ===")
    by_polN = defaultdict(list)
    for c in cells:
        by_polN[(c["policy"], c["N"])].append(c)
    # per (policy,N) fit each observable vs k/N
    exps = defaultdict(dict)  # (policy) -> obs -> {N: exponent}
    for (policy, N), cs in by_polN.items():
        cs = [c for c in cs if c["k_over_N"] > 0]
        kns = sorted(set(round(c["k_over_N"], 5) for c in cs))
        if len(kns) < 3:
            continue
        for o in OBS:
            pts = [(c["k_over_N"], c["obs"][o]) for c in sorted(cs, key=lambda x: x["k_over_N"])]
            a, r = fit(pts)
            exps[policy].setdefault(o, {})[N] = (a, r)
            print(f"  policy={policy} N={N}: {o:12s} ~ (k/N)^{a:+.3f} (R²{r:.2f}) over {len(pts)} pts")

    # cross-N drift test per policy/observable
    print("\n  --- exponent drift across N (Case classification) ---")
    any_case = False
    for policy, od in exps.items():
        for o, byN in od.items():
            if len(byN) < 2:
                continue
            any_case = True
            es = [v[0] for v in byN.values()]
            drift = max(es) - min(es)
            if drift <= 0.05:
                case = "Case 1 (pure smooth control: exponent constant)"
            elif drift <= 0.10:
                case = "borderline (Case 1/2)"
            else:
                case = "Case 2 (structural bending: k/N is a geometry modifier)"
            print(f"  {policy} {o}: k/N-exponents at N={sorted(byN)} = "
                  f"{[round(byN[N][0],3) for N in sorted(byN)]}  drift={drift:.3f} -> {case}")
    if not any_case:
        print("  (need the same observable's k/N-exponent at >=2 N values; "
              "add the second-N sweep rows from the design matrix)")
    print("\n  Case 3 (regime crossover) requires the piecewise-vs-power-law residual "
          "test; flagged manually if any single-N k/N fit shows R²<0.8 with visible kink.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: tdr24_policy_geometry_classify.py motif_*.csv"); sys.exit(2)
    sys.exit(main(sys.argv[1:]))
