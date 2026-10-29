#!/usr/bin/env python3
"""
tdr24a_decomposition.py

TDR-24A: decompose C_component^bulk (the topological-filtering suppressor) into
its numerator and denominator to expose the suppression mechanism.

C_component = occ_clean_pairs_in_clean_star / occ_clean_pairs
            = (birth-producing clean candidates) / (all clean antipodal candidates)

Finding (from v17 bulk data, N=480,840,1200,1440):
  denominator  occ_clean/row        ~ N^+0.95   (candidate pool grows ~linearly)
  numerator    occ_in_clean_star/row~ N^+0.10   (clean-star supply ~ saturated/flat)
  => C_component ~ N^(0.10-0.95) ~ N^-0.85

Mechanism: GEOMETRIC DILUTION. The candidate pool = (N/2 antipodal axes) x
(per-axis clean-candidate probability). The per-axis probability is N-independent
because window occupancy lambda = M*(2k+1)/N is fixed at fixed k/N with M bounded;
so the pool grows ~ N/2 ~ N simply because there are more antipodal axes to scan.
Meanwhile the supply of genuine clean (single-center) stars saturates because
multistar locking (f_ms ~ 1, ms_components/row ~ const) absorbs hub structure.
A fixed numerator over a linearly-growing denominator yields the ~N^-0.85 falloff.

Status:
  [ALG candidate] denominator ~ N^1 (clean counting argument).
  [HEUR strong]   numerator ~ const (mechanism identified; first-principles cap
                  on clean-star supply not yet derived from Z_N combinatorics).
  The composite "N^-0.757" is a fitted convenience over a specific N-range, not a
  true power law: C_component is a ratio of two different N-behaviours, so its
  apparent exponent drifts with the fitting window (-0.72 over 120-1080,
  -0.85 over 480-1440).
"""

import csv
import math
import argparse
from collections import defaultdict


WANT = ["step", "M_pre", "M_post", "N", "k",
        "occ_clean_pairs", "occ_clean_pairs_in_clean_star",
        "occ_clean_pairs_in_multistar", "occ_clean_pairs_embedded",
        "occ_clean_pairs_other", "clean_star_components",
        "multistar_components", "multistar_centers_total"]


def process(path, step_min=4001, tail_threshold=500):
    # run-level bulk filter (final_M <= tail_threshold)
    run_final = {}
    with open(path) as f:
        h = f.readline().strip().split(",")
        C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]
            mp = float(v[C["M_post"]])
            if mp > run_final.get(rid, 0.0):
                run_final[rid] = mp
    bulk = {r for r, m in run_final.items() if m <= tail_threshold}

    s = defaultdict(float)
    N = k = None
    policy = "unknown"; T = -1
    with open(path) as f:
        h = f.readline().strip().split(",")
        C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            if v[C["run_id"]] not in bulk:
                continue
            if int(v[C["step"]]) < step_min:
                continue
            if N is None:
                N, k = int(v[C["N"]]), int(v[C["k"]])
                policy = v[C["policy"]] if "policy" in C else "unknown"
                T = int(v[C["T"]]) if "T" in C else -1
            s["occ"]       += float(v[C["occ_clean_pairs"]])
            s["occ_in_cs"] += float(v[C["occ_clean_pairs_in_clean_star"]])
            s["occ_in_ms"] += float(v[C["occ_clean_pairs_in_multistar"]])
            s["occ_other"] += float(v[C["occ_clean_pairs_other"]])
            s["cs_comp"]   += float(v[C["clean_star_components"]])
            s["ms_comp"]   += float(v[C["multistar_components"]])
            s["M"]         += float(v[C["M_pre"]])
            s["rows"]      += 1
    return (policy, T, N, k), dict(s)


def fit(xs, ys):
    lx = [math.log(x) for x in xs]; ly = [math.log(y) for y in ys]
    n = len(lx); mx = sum(lx)/n; my = sum(ly)/n
    sxx = sum((a-mx)**2 for a in lx); sxy = sum((lx[i]-mx)*(ly[i]-my) for i in range(n))
    a = sxy/sxx; b = my - a*mx
    ss = sum((ly[i]-my)**2 for i in range(n)); sr = sum((ly[i]-(b+a*lx[i]))**2 for i in range(n))
    return a, (1 - sr/ss if ss else 1.0)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--step-min", type=int, default=4001)
    p.add_argument("--tail-threshold", type=float, default=500)
    args = p.parse_args()

    # Pool by full cell (policy, T, N, k): sum raw counts across files sharing a
    # cell so multiple seeds/batches combine. Different policies/T at the same N
    # remain separate cells (canonical-tooling convention).
    cells = {}
    for c in args.csvs:
        cell, s = process(c, args.step_min, args.tail_threshold)
        if cell in cells:
            for key, v in s.items():
                cells[cell][key] = cells[cell].get(key, 0.0) + v
        else:
            cells[cell] = s
    # Exponent fits must stay within one (policy, T, k/N) slice. Group cells by
    # slice; refuse to silently mix slices in a single fit.
    by_slice = {}
    for (policy, T, N, k), s in cells.items():
        slc = (policy, T, round(k / N, 6))
        if N in by_slice.setdefault(slc, {}):
            for key, v in s.items():
                by_slice[slc][N][key] = by_slice[slc][N].get(key, 0.0) + v
        else:
            by_slice[slc][N] = s
    if len(by_slice) > 1:
        print(f"NOTE: {len(by_slice)} distinct (policy,T,k/N) slices supplied; "
              f"each is analyzed separately below, never mixed.")

    for slc in sorted(by_slice):
        if len(by_slice) > 1:
            print(f"\n=== slice (policy, T, k/N) = {slc} ===")
        analyze_slice(by_slice[slc])


def analyze_slice(data):
    Ns = sorted(data)

    print(f"{'N':>5} {'C_comp':>9} {'occ/row':>9} {'occ_cs/row':>11} "
          f"{'ms_comp/row':>11} {'per-axis p':>11}")
    for N in Ns:
        s = data[N]; r = s["rows"]
        cc = s["occ_in_cs"]/s["occ"]
        print(f"{N:>5} {cc:>9.5f} {s['occ']/r:>9.3f} {s['occ_in_cs']/r:>11.4f} "
              f"{s['ms_comp']/r:>11.4f} {(s['occ']/r)/(N/2):>11.5f}")

    if len(Ns) >= 2:
        print("\nExponents (run-level bulk):")
        for label, fn in [
            ("C_component",            lambda N: data[N]["occ_in_cs"]/data[N]["occ"]),
            ("occ_clean/row (denom)",  lambda N: data[N]["occ"]/data[N]["rows"]),
            ("occ_in_clean_star/row (numer)", lambda N: data[N]["occ_in_cs"]/data[N]["rows"]),
            ("ms_components/row",      lambda N: data[N]["ms_comp"]/data[N]["rows"]),
        ]:
            ys = [fn(N) for N in Ns]
            if all(y > 0 for y in ys):
                a, r2 = fit(Ns, ys)
                print(f"  {label:34s} ~ N^{a:+.3f}  (R²={r2:.3f})")
        an, _ = fit(Ns, [data[N]["occ_in_cs"]/data[N]["rows"] for N in Ns])
        ad, _ = fit(Ns, [data[N]["occ"]/data[N]["rows"] for N in Ns])
        print(f"\n  => C_component predicted exp = {an:+.3f} - ({ad:+.3f}) = {an-ad:+.3f}")
        print("  Mechanism: geometric dilution — flat clean-star supply over a")
        print("  candidate pool that grows ~ N/2 (number of antipodal axes).")


if __name__ == "__main__":
    main()
