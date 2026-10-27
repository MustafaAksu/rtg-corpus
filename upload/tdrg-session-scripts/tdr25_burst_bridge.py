#!/usr/bin/env python3
"""
tdr25_burst_bridge.py

TDR-24A -> TDR-25/26 bridge study, part 1 (clean cells).

Question: are ordinary shedding bursts, extreme bursts, and the N~720 runaway
locking failures different quantiles of ONE shedding/recapture distribution?

Method (v17 clean cells N=480,840,1200,1440; run-level bulk; step>=4001):
  1. Burst-size survival functions P(O_other >= x*Obar), normalized per cell.
  2. Per-burst-band conditional composition: frac_cs, frac_ms, frac_other,
     births/row, multistar_centers_total -- the "unlock gradient".
  3. Extrapolation of frac_cs vs burst size toward the runaway composition.

FINDINGS:
  [NUM strong] One N-stable shedding family. Normalized survival curves
    collapse across N (e.g. P(>=10x) = 4.3-4.5% at every N). Distribution
    truncates sharply: max observed burst 42-55x Obar; P(>=50x) ~ 6e-5; no
    heavy/power-law tail in clean cells.
  [NUM strong] Monotone unlock gradient with burst size (shown N=480, 1440):
    births/row 0 -> 0.39-0.41, centers 53 -> 29-35, frac_cs 0 -> 0.042-0.045
    across bands [0,1) ... [30,100) x Obar. Extreme bursts are genuinely
    "more unlocked" -- a continuous gradient exists.
  [NUM] BUT the gradient does NOT reach the runaway: top-band frac_cs <= 0.05
    vs runaway frac_cs ~ 0.78-0.81 (N=720 r43 / N=722). Within-range power-law
    extrapolation (frac_cs ~ size^1.7 at N=1440) would need bursts ~300x Obar,
    ~6x beyond the observed truncation, to reach runaway composition.

VERDICT after N=720 part 2 [NUM strong / HEUR strong]:
  Quantile hypothesis PARTIALLY supported for the locked bulk: one N-stable
  shedding family and one unlock gradient exist. However, the N=720 r43
  runaway is NOT a smooth extreme quantile of single-step burst size.
  r43's maximum burst is 26.95x Obar, smaller than the N=720 bulk maximum
  43.8x, with zero rows >=30x, >=50x, or >=100x.

  The v2.8 failed-relock hypothesis is therefore revised. r43 is not a
  mature locked run suffering a late snap-back failure. It enters a
  clean-star-producing mode during the pre-lock transient (cs-frac 0.72 at
  steps 1-100 vs bulk 0.19) and never converges to the multistar-absorbing
  basin (ms-absorption pinned ~0.110 vs bulk 0.734 over all 5000 steps).
  Current mechanism: early lock-nonengagement / persistent relock-defective
  attractor.

CURRENT TDR-26 TARGET:
  Derive or bound the probability that a run fails to enter the stable
  multistar-locked absorbing basin during early growth. The --onset mode is
  retained as a guarded diagnostic; use --onset-min-M or --onset-min-step to
  avoid the step-9 pre-lock artifact.

Usage:
  python tdr25_burst_bridge.py motif_N*.csv [--bands ...] [--xs ...]
  Part 2 (with N=720 log): python tdr25_burst_bridge.py motif_N720*.csv --onset --onset-min-M 50
"""

import csv
import math
import bisect
import argparse
from collections import defaultdict


def bulk_runs(path, tail_threshold):
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    return rf, {r for r, m in rf.items() if m <= tail_threshold}


def load(path, step_min, tail_threshold, tail_side=False):
    rf, bulk = bulk_runs(path, tail_threshold)
    keep = (set(rf) - bulk) if tail_side else bulk
    rows = []
    N = None
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            if v[C["run_id"]] not in keep: continue
            step = int(v[C["step"]])
            if not tail_side and step < step_min: continue
            if N is None: N = int(v[C["N"]])
            rows.append((step, v[C["run_id"]],
                         float(v[C["occ_clean_pairs_other"]]),
                         float(v[C["occ_clean_pairs"]]),
                         float(v[C["occ_clean_pairs_in_clean_star"]]),
                         float(v[C["occ_clean_pairs_in_multistar"]]),
                         float(v[C["births_step"]]),
                         float(v[C["multistar_centers_total"]]),
                         float(v[C["M_pre"]])))
    return N, rows


def survival(rows, xs):
    vals = sorted(r[2] for r in rows)
    Obar = sum(vals)/len(vals)
    out = {}
    for x in xs:
        i = bisect.bisect_left(vals, x*Obar)
        out[x] = (len(vals)-i)/len(vals)
    return Obar, out, vals[-1]/Obar


def bands_table(rows, Obar, bands):
    print(f"  {'band xObar':>10} {'rows':>7} {'frac_cs':>8} {'frac_ms':>8} "
          f"{'b/row':>7} {'centers':>8}")
    for lo, hi in bands:
        a = defaultdict(float)
        for _, _, oo, occ, oic, oims, b, cen, _ in rows:
            if lo*Obar <= oo < hi*Obar:
                a["occ"] += occ; a["oic"] += oic; a["oims"] += oims
                a["b"] += b; a["cen"] += cen; a["n"] += 1
        if a["n"] and a["occ"]:
            print(f"  {f'[{lo},{hi})':>10} {int(a['n']):>7} "
                  f"{a['oic']/a['occ']:>8.4f} {a['oims']/a['occ']:>8.4f} "
                  f"{a['b']/a['n']:>7.3f} {a['cen']/a['n']:>8.1f}")


def onset_profile(rows, Obar, W=10, min_M=0, min_step=0):
    """For tail runs: profile burst size and centers around runaway onset
    (first step with M_pre>=min_M, step>=min_step, and
    occ_in_clean_star/occ_clean > 0.2).

    GUARD RATIONALE: the unguarded detector fires on the pre-lock transient
    (e.g. N=720 r43: step 9, M=4) which is not a mature-vacuum onset. Use
    --onset-min-M 50/500 or --onset-min-step 100+ for lock-engagement tests."""
    byrun = defaultdict(list)
    for r in rows: byrun[r[1]].append(r)
    for rid, rs in byrun.items():
        rs.sort()
        onset = next((i for i, r in enumerate(rs)
                      if r[0] >= min_step and r[8] >= min_M
                      and r[3] > 0 and r[4]/r[3] > 0.2), None)
        if onset is None:
            print(f"  run {rid}: no onset found"); continue
        print(f"  run {rid}: onset at step {rs[onset][0]}")
        print(f"  {'offset':>7} {'O_oth/Obar':>11} {'frac_cs':>8} {'centers':>8} {'births':>7}")
        for d in range(-W, W+1):
            i = onset + d
            if 0 <= i < len(rs):
                _, _, oo, occ, oic, _, b, cen, _ = rs[i]
                print(f"  {d:>+7} {oo/Obar:>11.1f} "
                      f"{(oic/occ if occ else 0):>8.3f} {cen:>8.0f} {b:>7.0f}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--step-min", type=int, default=4001)
    p.add_argument("--tail-threshold", type=float, default=500)
    p.add_argument("--xs", type=float, nargs="*", default=[1, 2, 5, 10, 20, 30, 50, 80])
    p.add_argument("--onset", action="store_true",
                   help="analyze TAIL runs' runaway onset (part 2; needs a cell with tails)")
    p.add_argument("--onset-min-M", type=float, default=0,
                   help="onset guard: require M_pre >= this (e.g. 50 or 500)")
    p.add_argument("--onset-min-step", type=int, default=0,
                   help="onset guard: require step >= this")
    args = p.parse_args()

    for path in args.csvs:
        if args.onset:
            N, rows = load(path, args.step_min, args.tail_threshold, tail_side=True)
            if not rows:
                print(f"{path}: no tail runs"); continue
            # Obar from the BULK side of the same cell
            _, brows = load(path, args.step_min, args.tail_threshold)
            Obar = sum(r[2] for r in brows)/len(brows) if brows else 1.0
            print(f"\n=== {path} N={N} TAIL-RUN ONSET (Obar_bulk={Obar:.2f}) ===")
            onset_profile(rows, Obar, min_M=args.onset_min_M, min_step=args.onset_min_step)
        else:
            N, rows = load(path, args.step_min, args.tail_threshold)
            Obar, surv, mx = survival(rows, args.xs)
            print(f"\n=== {path} N={N} (Obar={Obar:.2f}, max={mx:.1f}x, n={len(rows)}) ===")
            print("  survival: " + "  ".join(f"P(>={x}x)={surv[x]:.2e}" for x in args.xs))
            bands_table(rows, Obar, [(0, 1), (1, 5), (5, 10), (10, 20), (20, 30), (30, 100)])


if __name__ == "__main__":
    main()
