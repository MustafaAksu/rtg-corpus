#!/usr/bin/env python3
"""
tdr24b_chi_refit.py

TDR-24B chi re-fit on the v17 corpus (run-level bulk filtering), superseding the
v4-era chi_bulk ~ N^+0.836.

chi := occ_clean_pairs_in_clean_star / clean_star_components   (v6 bootstrap definition:
the per-clean-star-component occupancy compression).

FINDINGS (v17 bulk, run-level final_M<=500, late window step>=4001, N=480..1440):

1. chi is NOT a clean power law. Its apparent exponent is window-dependent:
       480-1440: +0.697 (R^2 0.858)     720-1440: +0.512 (R^2 0.652)
       480-1200: +0.641 (R^2 0.757)     840-1440: +0.866 (R^2 0.954)
   The v4-era +0.836 is one window's reading of a composite ratio, not a law.
   Same failure class as C_component (-0.72..-0.85) and q_proj (1.06..1.371):
   a ratio of two differently-scaling quantities gives a range-dependent pseudo-exponent.

2. Decomposition (the structural result):
       numerator  occ_in_clean_star/row ~ N^-0.03  (R^2 0.004 -- FLAT)
       denominator clean_star_components/row ~ N^-0.73 (R^2 0.86)
   => chi ~ N^(+0.70) arises ENTIRELY from the collapse of the clean-star COUNT per
      step (denominator), not from growth of per-star occupancy (numerator is flat).
   Mechanism: occupancy that lands in clean stars is a roughly fixed per-row amount,
   but it is concentrated into fewer and fewer clean-star components as N grows
   (multistar locking absorbs the rest), so occupancy-per-clean-star rises.

3. Internal consistency (the factorization C_birth = C_component / chi):
   This is an EXACT value-wise identity, not a fit:
       C_component / chi = (occ_in_cs/occ_clean) / (occ_in_cs/clean_stars)
                         = clean_stars / occ_clean
                         = births / occ_clean              [births == clean_stars, certified]
                         = C_birth.
   In log space the exponents therefore satisfy (RATIO, not difference of observables):
       exp(C_birth) = exp(C_component) - exp(chi) = -0.936 - (+0.697) = -1.633,
   matching the directly-measured C_birth ~ N^-1.633 (R^2 0.976). The script's
   identity-check line prints "C_component - chi" meaning this log-space exponent
   relation of the ratio; it is NOT a subtraction of the observables.

CONSEQUENCE FOR TDR-24B:
   The derivation target is NOT "derive chi ~ N^+0.836". It is:
   derive clean_star_components/row ~ N^-0.73 (the clean-star COUNT collapse), since
   the numerator is flat. This is the same object as TDR-24A's clean-star supply cap
   viewed per-row -- TDR-24A and TDR-24B share the clean-star-count denominator.
   The flat numerator should be tagged a range-dependent diagnostic, not promoted.

NOTE: N=840 (7-divisible clean control) sits slightly off-trend; excluding it barely
moves the full-window exponent (+0.693 vs +0.697), so it is not the source of the
window dependence -- the composite-ratio structure is.
"""

import csv
import math
import argparse
from collections import defaultdict


def chi_components(path, step_min=4001, tail_threshold=500):
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    bulk = {r for r, m in rf.items() if m <= tail_threshold}
    acc = defaultdict(float)
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            if v[C["run_id"]] not in bulk: continue
            if int(v[C["step"]]) < step_min: continue
            acc["oic"] += float(v[C["occ_clean_pairs_in_clean_star"]])
            acc["occ_clean"] += float(v[C["occ_clean_pairs"]])
            acc["cs"] += float(v[C["clean_star_components"]])
            acc["births"] += float(v[C["births_step"]])
            acc["rows"] += 1
            if acc["N"] == 0:
                acc["N"] = int(v[C["N"]])
    return acc


def fit(pts):
    lx = [math.log(p[0]) for p in pts]; ly = [math.log(p[1]) for p in pts]
    n = len(lx); mx = sum(lx)/n; my = sum(ly)/n
    sxx = sum((a-mx)**2 for a in lx)
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
        acc = chi_components(path, args.step_min, args.tail_threshold)
        D[int(acc["N"])] = acc
    Ns = sorted(D)

    print(f"{'N':>6} {'chi':>9} {'oic/row':>9} {'cs/row':>9} {'C_comp':>9} {'C_birth':>10}")
    for N in Ns:
        a = D[N]
        chi = a["oic"]/a["cs"] if a["cs"] else float("nan")
        print(f"{N:>6} {chi:>9.3f} {a['oic']/a['rows']:>9.4f} {a['cs']/a['rows']:>9.5f} "
              f"{a['oic']/a['occ_clean']:>9.4f} {a['births']/a['occ_clean']:>10.6f}")

    def series(fn): return [(N, fn(D[N])) for N in Ns]
    chi_s = series(lambda a: a["oic"]/a["cs"])
    num_s = series(lambda a: a["oic"]/a["rows"])
    den_s = series(lambda a: a["cs"]/a["rows"])
    cc_s = series(lambda a: a["oic"]/a["occ_clean"])
    cb_s = series(lambda a: a["births"]/a["occ_clean"])

    print("\nFits (full window):")
    for label, s in [("chi", chi_s), ("occ_in_cs/row (numerator)", num_s),
                     ("clean_stars/row (denominator)", den_s),
                     ("C_component", cc_s), ("C_birth", cb_s)]:
        a, r = fit(s)
        print(f"  {label:32s} ~ N^{a:+.3f} (R²{r:.3f})")

    a_cc, _ = fit(cc_s); a_chi, _ = fit(chi_s); a_cb, _ = fit(cb_s)
    print(f"\nIdentity check (C_birth = C_component/chi, exact value-wise):")
    print(f"  log-space exponent of the RATIO: exp(C_comp) - exp(chi) = "
          f"{a_cc:+.3f} - ({a_chi:+.3f}) = {a_cc-a_chi:+.3f}")
    print(f"  C_birth exponent measured directly = {a_cb:+.3f}  "
          f"(matches; this is a ratio relation, not observable subtraction)")

    print("\nWindow-dependence of chi exponent (composite-ratio test):")
    for lo, hi in [(Ns[0], Ns[-1]), (Ns[0], Ns[-2]), (Ns[1], Ns[-1])]:
        pts = [(N, D[N]["oic"]/D[N]["cs"]) for N in Ns if lo <= N <= hi]
        if len(pts) >= 3:
            a, r = fit(pts)
            print(f"  N in [{lo},{hi}] ({len(pts)}pts): chi~N^{a:+.3f} (R²{r:.3f})")


if __name__ == "__main__":
    main()
