#!/usr/bin/env python3
"""
tdr24b_field_structure.py

Tests a proposed minimal scaling-field basis for the TDR-24 system against v17 data.

REVIEW PROPOSAL (tested here):
  F1 rho   ~ N^-alpha  (node availability)
  F2 sigma ~ N^-beta   (binding suppression, multistar locking)
  F3 kappa ~ N^+1      (geometric fan-out)
  with  clean_star_components ~ rho*sigma,  occ_in_clean_star ~ rho*kappa,
        chi = occ_in_cs/clean_stars ~ kappa/sigma,
  and the separability test:  chi * sigma  ≈  kappa ~ N^+1   (sigma := clean_stars/row / N).

RESULT (v17 bulk, run-level final_M<=500, step>=4001, N=480..1440): REJECTED.
  - chi*sigma ~ N^-1.03, NOT N^+1 (off by two powers).
  - The suppression field is absent: multistar absorption fraction is flat (N^-0.02);
    occ in clean-star / multistar / other channels all scale ~N^+0.90, so the channel
    split is N-independent (no N-dependent suppression to factor out).
  - (availability x suppression) = (occ_clean/row) x (1 - absorb_frac) ~ N^+0.88,
    while clean_star_components/row ~ N^-0.73: gap +1.6. Not this factorization.

WHAT IS ACTUALLY TRUE:
  clean_star_components/row IS TDR-24A's cs_rate (clean stars are births, <=1/step),
  already decomposed as flat burst-hazard x P(cs|burst) ~ N^-0.6. It is composite
  (review's intuition correct) but it is the EXISTING residual, not a new latent.

  The system reduces to TWO independent scaling inputs:
    (A) occupancy/row              ~ N^+0.90   (slot/geometry field)
    (B) clean-star birth rate      ~ N^-0.73   (= TDR-24A cs_rate; the open residual)
  and chi, C_component, C_birth are all quotients of (A) and (B). No third field.

STANDING METHOD NOTE: most reported exponents are quotients of a few underlying
fields; test primitive-vs-ratio before promoting any exponent (explains the recurring
window drift in chi, C_component, q_proj).
"""

import csv
import math
import argparse
from collections import defaultdict

COLS = ["occ_clean_pairs_in_clean_star", "occ_clean_pairs", "clean_star_components",
        "occ_clean_pairs_in_multistar", "occ_clean_pairs_other", "multistar_components"]


def pools(path, step_min=4001, tail_threshold=500):
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    bulk = {r for r, m in rf.items() if m <= tail_threshold}
    a = defaultdict(float)
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            if v[C["run_id"]] not in bulk: continue
            if int(v[C["step"]]) < step_min: continue
            for col in COLS:
                a[col] += float(v[C[col]])
            a["rows"] += 1
            if a["N"] == 0: a["N"] = int(v[C["N"]])
    return a


def fit(pts):
    lx = [math.log(p[0]) for p in pts]; ly = [math.log(p[1]) for p in pts]
    n = len(lx); mx = sum(lx)/n; my = sum(ly)/n
    sxx = sum((x-mx)**2 for x in lx)
    a = sum((lx[i]-mx)*(ly[i]-my) for i in range(n))/sxx
    b = my - a*mx
    ss = sum((y-my)**2 for y in ly); sr = sum((ly[i]-(a*lx[i]+b))**2 for i in range(n))
    return a, (1 - sr/ss if ss else 1.0)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--step-min", type=int, default=4001)
    p.add_argument("--tail-threshold", type=float, default=500)
    args = p.parse_args()

    D = {}
    for path in args.csvs:
        a = pools(path, args.step_min, args.tail_threshold)
        D[int(a["N"])] = a
    Ns = sorted(D)

    def per(c): return [(N, D[N][c]/D[N]["rows"]) for N in Ns]

    print("Channel exponents (per-row, v17 bulk):")
    for c in ["occ_clean_pairs", "occ_clean_pairs_in_clean_star",
              "occ_clean_pairs_in_multistar", "occ_clean_pairs_other",
              "clean_star_components", "multistar_components"]:
        e, r = fit(per(c))
        print(f"  {c:34s} ~ N^{e:+.3f} (R²{r:.2f})")

    print("\nReview's separability test (chi * sigma ~ kappa ~ N^+1):")
    sigma = {N: (D[N]["clean_star_components"]/D[N]["rows"])/N for N in Ns}
    chi = {N: D[N]["occ_clean_pairs_in_clean_star"]/D[N]["clean_star_components"] for N in Ns}
    kap = {N: chi[N]*sigma[N] for N in Ns}
    e_k, r_k = fit([(N, kap[N]) for N in Ns])
    print(f"  implied kappa = chi*sigma ~ N^{e_k:+.3f} (R²{r_k:.2f})  "
          f"-> {'PASS' if abs(e_k-1) < 0.15 else 'FAIL (claim was +1)'}")

    print("\nSuppression-field test (clean_star_count = availability x (1-absorb)?):")
    e_av, _ = fit(per("occ_clean_pairs"))
    e_su, _ = fit([(N, 1 - D[N]["occ_clean_pairs_in_multistar"]/D[N]["occ_clean_pairs"])
                   for N in Ns])
    e_cs, _ = fit(per("clean_star_components"))
    print(f"  availability {e_av:+.3f} + suppression {e_su:+.3f} = {e_av+e_su:+.3f} "
          f"vs clean_star_count {e_cs:+.3f}  -> "
          f"{'MATCH' if abs(e_av+e_su-e_cs) < 0.1 else 'FAIL (gap %+.3f)' % (e_av+e_su-e_cs)}")

    print("\nReduced basis (two independent inputs):")
    print(f"  (A) occupancy/row        ~ N^{e_av:+.3f}")
    print(f"  (B) clean-star birth rate ~ N^{e_cs:+.3f}  (= TDR-24A cs_rate)")
    print("  chi, C_component, C_birth are quotients of (A) and (B); no third field.")


if __name__ == "__main__":
    main()
