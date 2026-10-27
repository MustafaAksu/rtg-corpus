#!/usr/bin/env python3
"""
tdr26_early_basin_classifier.py

TDR-26 early-basin discriminator study: can defective-basin (runaway) runs be
detected in the first 100-300 steps, before T=5000 reveals them via final_M?

METHOD: per-run early-window metrics over windows {50,100,200,300}, comparing
tail runs (final_M > tail_threshold) against the bulk-run distribution
(mean, sd, min/max, z-score, count of bulk runs at-or-beyond in the tail's
direction).

FINDINGS (N=720 v17, 1 tail run r43 vs 99 bulk):

1. Discriminator TIMELINE:
   w=50:  r43 NOT separable (cs_frac z=1.36, rank 12/99 -- inside bulk range).
   w=100: r43 is an extreme z-score outlier (z~3.1-3.2 on cs_frac and b/step)
          but RANK-2 in both raw metrics, still not separated: r48 exceeds it
          on cs_frac (0.867 vs 0.715) and r3 on b/step (0.420 vs 0.350).
   w=200: CLEAN GAP on b/step: r43=0.490 vs bulk max 0.250 (1.96x margin).
   w=300: gap widens: r43=0.550 vs bulk max 0.200 (2.75x margin).

2. cs_frac ALONE IS NOT THE DISCRIMINATOR. Several bulk runs show high early
   cs_frac (r48: 0.867, r90: 0.713, r92: 0.699 at w=100) on FEW candidates --
   idle pre-lock noise -- and all engage the lock by w=200 (ms_abs jumps to
   0.41-0.47, cs_frac collapses to ~0.1-0.19). The defective run differs in
   SUSTAINED PRODUCTION: b/step keeps RISING (0.35 -> 0.49 -> 0.55) while
   every contender's collapses.

3. ABSOLUTE-STEP RULE [w=200]: b/step >= 0.30 AND ms_abs <= 0.25
   N=720: TP=1 FP=0 FN=0 TN=99. *** FAILED on N=722: TP=0 FN=1. ***
   The N=722 tail run r31 was DORMANT for 433 steps (M=4, zero occupancy --
   four mutually non-interacting nodes), then entered the SAME defective
   attractor (late cs 0.812, ms-abs 0.090, b/row 0.652 vs r43's 0.782/0.110/
   0.633) directly from its first interaction. Absolute-step windows read its
   dormancy as zeros. Also REJECTED: first-birth-before-first-multistar as a
   discriminator (universal: all 198 bulk runs also birth first); and dormancy
   duration itself (r43's first birth is EARLY, step 9; r31's LATE, step 434 --
   opposite extremes).

4. BIRTH-ANCHORED RULE (canonical after N=722): over steps [fb, fb+200)
   where fb = first-birth step:  b/step >= 0.30 AND ms_abs <= 0.25.
   N=720: TP=1 FP=0 TN=99 (tail: 0.520/0.120; bulk max b/step 0.265)
   N=722: TP=1 FP=0 TN=99 (tail: 0.660/0.092; bulk max b/step 0.240)
   Combined: TP=2 FP=0 FN=0 TN=198 -- >=2x clean margin at both cells.

CAVEAT [load-bearing]: n=2 defective runs, one per cell. Cross-cell support is
real but still small-sample; the rule thresholds were chosen on n=1 and merely
SURVIVED n=2. Validation at batch >=500 remains required before the rule is
classifier-grade. Basin selection is decided and detectable within ~200 steps
OF FIRST BIRTH (not absolute time -- dormancy shifts the clock).

Usage:
  python tdr26_early_basin_classifier.py motif_N720_*.csv \
      --tail-threshold 500 --windows 50 100 200 300 \
      [--out-csv early_metrics.csv] [--rule-b 0.30 --rule-ms 0.25 --rule-w 200]
"""

import csv
import math
import argparse
import statistics
from collections import defaultdict


METRIC_KEYS = ["cs_frac", "ms_abs", "other_frac", "b_per_step", "cen_mean", "M_slope"]


def classify_runs(path, tail_threshold):
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    return rf, {r for r, m in rf.items() if m > tail_threshold}


def accumulate(path, windows):
    acc = defaultdict(lambda: {w: defaultdict(float) for w in windows})
    wmax = max(windows)
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            step = int(v[C["step"]])
            if step > wmax: continue
            rid = v[C["run_id"]]
            occ = float(v[C["occ_clean_pairs"]])
            oic = float(v[C["occ_clean_pairs_in_clean_star"]])
            oims = float(v[C["occ_clean_pairs_in_multistar"]])
            ooth = float(v[C["occ_clean_pairs_other"]])
            b = float(v[C["births_step"]])
            cen = float(v[C["multistar_centers_total"]])
            mpost = float(v[C["M_post"]])
            mpre = float(v[C["M_pre"]])
            for w in windows:
                if step <= w:
                    a = acc[rid][w]
                    a["occ"] += occ; a["oic"] += oic; a["oims"] += oims
                    a["ooth"] += ooth; a["b"] += b; a["cen"] += cen; a["n"] += 1
                    if step == w: a["M_at_w"] = mpost
                    if step == 1: a["M_at_1"] = mpre
    return acc


def metrics(a, w):
    occ = a["occ"] or 1e-12
    n = a["n"] or 1
    return {
        "cs_frac": a["oic"]/occ,
        "ms_abs": a["oims"]/occ,
        "other_frac": a["ooth"]/occ,
        "b_per_step": a["b"]/n,
        "cen_mean": a["cen"]/n,
        "M_slope": (a.get("M_at_w", 0) - a.get("M_at_1", 0)) / w,
    }



def birth_anchored_metrics(path, w):
    """Per-run (b/step, ms_abs) over [first_birth, first_birth+w)."""
    firstb = {}
    rows_by_run = defaultdict(list)
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]
            step = int(v[C["step"]])
            b = float(v[C["births_step"]])
            if rid not in firstb and b > 0: firstb[rid] = step
            rows_by_run[rid].append((step, b,
                                     float(v[C["occ_clean_pairs"]]),
                                     float(v[C["occ_clean_pairs_in_multistar"]])))
    out = {}
    for rid, rows in rows_by_run.items():
        fb = firstb.get(rid)
        if fb is None: continue
        W = [r for r in rows if fb <= r[0] < fb + w]
        n = len(W) or 1
        occ = sum(r[2] for r in W) or 1e-12
        out[rid] = (sum(r[1] for r in W)/n, sum(r[3] for r in W)/occ)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--tail-threshold", type=float, default=500)
    p.add_argument("--windows", type=int, nargs="*", default=[50, 100, 200, 300])
    p.add_argument("--out-csv", default=None)
    p.add_argument("--rule-w", type=int, default=200)
    p.add_argument("--rule-b", type=float, default=0.30)
    p.add_argument("--rule-ms", type=float, default=0.25)
    p.add_argument("--anchor-birth", action="store_true",
                   help="evaluate the rule on [first_birth, first_birth+rule_w) "
                        "instead of absolute steps (canonical after N=722 test)")
    args = p.parse_args()

    all_out_rows = []
    for path in args.csvs:
        rf, tails = classify_runs(path, args.tail_threshold)
        acc = accumulate(path, args.windows)
        print(f"\n=== {path}: {len(rf)} runs, {len(tails)} tail ===")

        out_rows = []
        for w in args.windows:
            bulkvals = {k: [] for k in METRIC_KEYS}
            tailvals = {}
            for rid, per in acc.items():
                m = metrics(per[w], w)
                out_rows.append({"source_file": path, "run_id": rid,
                                 "window": w, "is_tail": int(rid in tails), **m})
                if rid in tails:
                    tailvals[rid] = m
                else:
                    for k in METRIC_KEYS: bulkvals[k].append(m[k])
            print(f"\n  window<= {w}")
            print(f"  {'metric':>12} {'bulk_mean':>10} {'bulk_sd':>9} {'bulk_max':>9}"
                  + "".join(f" {rid.split('_')[-1]:>8}" for rid in tailvals)
                  + "  z(first tail)")
            for k in METRIC_KEYS:
                bv = bulkvals[k]
                mu = statistics.mean(bv); sd = statistics.stdev(bv) if len(bv) > 1 else 0.0
                line = f"  {k:>12} {mu:>10.4f} {sd:>9.4f} {max(bv):>9.4f}"
                zs = []
                for rid, m in tailvals.items():
                    line += f" {m[k]:>8.4f}"
                    zs.append((m[k]-mu)/sd if sd else float("inf"))
                if zs: line += f"  {zs[0]:+.2f}"
                print(line)

        # rule evaluation (absolute-step or birth-anchored)
        w = args.rule_w
        if args.anchor_birth:
            tp = fp = fn = tn = 0
            details = {}
            per_run = birth_anchored_metrics(path, w)
            for rid, (bps, ms) in per_run.items():
                flag = bps >= args.rule_b and ms <= args.rule_ms
                details[rid] = (bps, ms, flag)
                if rid in tails and flag: tp += 1
                elif rid in tails: fn += 1
                elif flag: fp += 1
                else: tn += 1
            print(f"\n  BIRTH-ANCHORED RULE [fb..fb+{w}: b/step>={args.rule_b} "
                  f"AND ms_abs<={args.rule_ms}]: TP={tp} FP={fp} FN={fn} TN={tn}")
            for rid in tails:
                if rid in details:
                    bps, ms, _ = details[rid]
                    print(f"    tail {rid.split('_')[-1]}: b/step={bps:.3f} ms_abs={ms:.3f}")
            bulk_b = sorted(v[0] for r, v in details.items() if r not in tails)
            if bulk_b:
                print(f"    bulk b/step max={bulk_b[-1]:.3f}")
        else:
            tp = fp = fn = tn = 0
            for rid, per in acc.items():
                m = metrics(per[w], w)
                flag = m["b_per_step"] >= args.rule_b and m["ms_abs"] <= args.rule_ms
                if rid in tails and flag: tp += 1
                elif rid in tails: fn += 1
                elif flag: fp += 1
                else: tn += 1
            print(f"\n  ABSOLUTE-STEP RULE [w={w}: b/step>={args.rule_b} AND ms_abs<={args.rule_ms}]: "
                  f"TP={tp} FP={fp} FN={fn} TN={tn}")
            print("  (absolute-step windows misread dormant starts; "
                  "prefer --anchor-birth, canonical after the N=722 test)")

        all_out_rows.extend(out_rows)

    if args.out_csv:
        keys = ["source_file", "run_id", "window", "is_tail"] + METRIC_KEYS
        with open(args.out_csv, "w", newline="") as f:
            wtr = csv.DictWriter(f, fieldnames=keys)
            wtr.writeheader()
            for r in all_out_rows: wtr.writerow(r)
        print(f"\nper-run metrics ({len(all_out_rows)} rows, all files) written to {args.out_csv}")


if __name__ == "__main__":
    main()
