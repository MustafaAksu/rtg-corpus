#!/usr/bin/env python3
"""
tdr24a_provenance.py

TDR-24A Level-1 clean-star provenance extraction from v17 motif CSVs.

Splits run-level-bulk late-window rows into clean-star rows
(clean_star_components > 0) vs ordinary locked rows, compares state variables,
and builds an event-centered +-W step profile.

FINDINGS (v17, N=480/840/1200/1440, run-level bulk, step>=4001):

1. Provenance signature (clean-star rows vs ordinary rows, N-stable):
   - occ_clean_pairs elevated 7-10x; excess almost entirely in the 'other'
     channel (occ_clean_pairs_other elevated 22-33x): non-star fragments
     (paths/dyads/irregular) flood the candidate count.
   - multistar_centers_total DEPLETED ~30% (0.67-0.72x) while
     multistar_components stays ~1: the locked cluster persists but
     transiently sheds center mass.
   - births_step = 1.000 exactly (birth law).

2. Event-centered profile (N=1440, +-5 steps): the anomaly is STRICTLY
   single-step. 'other' flood (31x) and center depletion (0.71x) exist only
   at offset 0 and vanish at +-1. Clean-star exposure is an instantaneous
   reorganize-and-snap-back event, not an extended episode. (Snapshot is
   pre-birth in the simulator, so offset 0 is the state that PRODUCED the
   star, not an artifact of the blow-up.)

3. Burstiness: gap_mean/(1/rate) falls from 0.79 (N=480) to 0.41 (N=1440):
   events are increasingly clustered in time at high N.

4. Numerator decomposition (exact):
     occ_in_clean_star/row = cs_rate x E[occ_in_cs | event]
     cs_rate  ~ N^-0.669 (R^2=0.938)   exposure events become rarer
     E[..]    ~ N^+0.766 (R^2=0.983)   per-event attachment grows (band ~N wide)
     sum      = +0.096 vs measured +0.095  -- closes exactly.
   The "flat numerator" is itself a compensation, structurally analogous to
   the q_proj ~ (2k+1) cancellation in TDR-24F.

Remaining open: derive cs_rate ~ N^-0.67 (the unlock-exposure rate of the
locked cluster) from the stationary measure. Level-2 (event-local simulator
logging: new_node_in_component, nearest_competing_center_distance, ...) is
specified if the rate law needs microscopic origin attribution.
"""

import csv
import math
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
    return {r for r, m in rf.items() if m <= tail_threshold}


VARS = ["M_pre", "occ_clean_pairs", "occ_clean_pairs_in_multistar",
        "occ_clean_pairs_other", "multistar_components",
        "multistar_centers_total", "births_step"]


def provenance(path, step_min, tail_threshold):
    bulk = bulk_runs(path, tail_threshold)
    cs = defaultdict(float); ncs = defaultdict(float)
    cs_n = no_n = 0
    last = {}; gaps = []
    N = None
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]
            if rid not in bulk: continue
            step = int(v[C["step"]])
            if step < step_min: continue
            if N is None: N = int(v[C["N"]])
            c = float(v[C["clean_star_components"]])
            tgt = cs if c > 0 else ncs
            for var in VARS: tgt[var] += float(v[C[var]])
            if c > 0:
                cs_n += 1
                if rid in last: gaps.append(step - last[rid])
                last[rid] = step
            else:
                no_n += 1
    res = {"N": N, "cs_n": cs_n, "no_n": no_n,
           "cs_rate": cs_n / (cs_n + no_n) if cs_n + no_n else 0.0,
           "gap_mean": sum(gaps) / len(gaps) if gaps else 0.0}
    for var in VARS:
        res[f"cs_{var}"] = cs[var] / cs_n if cs_n else 0.0
        res[f"no_{var}"] = ncs[var] / no_n if no_n else 0.0
    return res


def profile(path, step_min, tail_threshold, W=5):
    bulk = bulk_runs(path, tail_threshold)
    series = defaultdict(dict)
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]
            if rid not in bulk: continue
            step = int(v[C["step"]])
            if step < step_min - W: continue
            series[rid][step] = (float(v[C["clean_star_components"]]),
                                 float(v[C["occ_clean_pairs_other"]]),
                                 float(v[C["multistar_centers_total"]]))
    prof = defaultdict(lambda: [0.0, 0.0, 0.0, 0])
    base = [0.0, 0.0, 0]
    for rid, ts in series.items():
        for s, (c, o, cen) in ts.items():
            if s >= step_min:
                base[0] += o; base[1] += cen; base[2] += 1
        for e in [s for s, (c, _, _) in ts.items() if c > 0 and s >= step_min + W]:
            for d in range(-W, W + 1):
                if e + d in ts:
                    c, o, cen = ts[e + d]
                    p = prof[d]; p[0] += o; p[1] += cen; p[2] += c; p[3] += 1
    bo, bc = base[0] / base[2], base[1] / base[2]
    print(f"\nEvent-centered profile (normalized to background o={bo:.2f}, cen={bc:.2f}):")
    print(f"{'offset':>7} {'other':>7} {'centers':>8} {'cs':>6}")
    for d in range(-W, W + 1):
        p = prof[d]
        if p[3]:
            print(f"{d:>+7} {p[0]/p[3]/bo:>7.2f} {p[1]/p[3]/bc:>8.2f} {p[2]/p[3]:>6.3f}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--step-min", type=int, default=4001)
    p.add_argument("--tail-threshold", type=float, default=500)
    p.add_argument("--profile", action="store_true", help="event-centered +-5 profile per file")
    args = p.parse_args()
    rows = [provenance(c, args.step_min, args.tail_threshold) for c in args.csvs]
    rows.sort(key=lambda r: r["N"])
    print(f"{'N':>5} {'cs_rate':>9} {'gap_mean':>9} | ratios cs/non-cs:")
    for r in rows:
        rat = {v: (r[f'cs_{v}'] / r[f'no_{v}'] if r[f'no_{v}'] else float('inf')) for v in VARS}
        print(f"{r['N']:>5} {r['cs_rate']:>9.5f} {r['gap_mean']:>9.1f} | "
              f"occ={rat['occ_clean_pairs']:.2f} other={rat['occ_clean_pairs_other']:.2f} "
              f"centers={rat['multistar_centers_total']:.2f} M={rat['M_pre']:.2f}")
    if args.profile:
        for c in args.csvs:
            profile(c, args.step_min, args.tail_threshold)


if __name__ == "__main__":
    main()
