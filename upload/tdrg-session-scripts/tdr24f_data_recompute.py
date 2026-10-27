#!/usr/bin/env python3
"""
tdr24f_data_recompute.py

Recomputes the TDR-24F slot-volume and structural-reservoir quantities directly
from v17 motif CSVs, using the EXACT definitions in genesis_mode_b_mc.py (v17).

Definitions confirmed from the simulator source:
  occ_clean_pairs : count of antipodal window-pairs c in [0, N/2) with
                    (|window(c)|==1 and |window(c+N/2)|>=3) or symmetric.
                    Natural ceiling is N/2, NOT (2k+1)*M.
  struct_leaf_incidence_total : sum over star/multistar centers of within-component degree.
  struct_unique_leaves_total  : sum of unique non-center nodes in star/multistar comps.
  struct_component_count      : clean_star_components + multistar_components.
  struct_center_count         : star_centers_total + multistar_centers_total.

Slot-volume model (DSN):
  S_slot   = (2k+1) * sum(M_pre)        [modeling normalization]
  psi_slot = sum(occ_clean_pairs) / S_slot
  cbar_slot= sum(occ_clean_pairs) / sum(M_pre) = (2k+1)*psi_slot

Structural reservoir (three candidate definitions, all reported):
  cbar_struct_per_comp   = struct_unique_leaves / struct_component_count   [the "4.5-5.8" metric]
  cbar_struct_node       = struct_leaf_incidence / sum(M_pre)              [simulator comment]
  cbar_struct_per_center = struct_leaf_incidence / struct_center_count

Projection factor:
  q_proj = cbar_slot / cbar_struct   (definition depends on which cbar_struct)

Run on multiple CSVs to fit N-scaling exponents; a single CSV verifies the
single-point (bounded / intensive) claims only.
"""

import csv
import math
import sys
import argparse


WANT = [
    "step", "M_pre", "N", "k", "births_step",
    "occ_clean_pairs", "occ_clean_pairs_in_clean_star", "clean_star_components",
    "struct_leaf_incidence_total", "struct_unique_leaves_total",
    "struct_component_count", "struct_center_count",
    "multistar_leaf_incidence_total", "multistar_centers_total",
]


def process(path, step_min=4001, tail_threshold=500):
    """Two-pass, RUN-LEVEL bulk filtering.

    Pass 1: determine each run's final_M (max M_post over the run).
    Pass 2: a run is BULK iff final_M <= tail_threshold; aggregate only bulk
            runs' late-window (step >= step_min) rows.

    This is the canonical TDR-24 bulk definition. Row-level M_pre filtering is
    NOT equivalent: a tail run's early low-M rows would leak into the bulk pool.
    """
    # Pass 1: run-level final_M
    run_final = {}
    with open(path) as f:
        header = f.readline().strip().split(",")
        C = {c: i for i, c in enumerate(header)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]
            mpost = float(v[C["M_post"]])
            if mpost > run_final.get(rid, 0.0):
                run_final[rid] = mpost

    bulk_runs = {rid for rid, fm in run_final.items() if fm <= tail_threshold}
    tail_runs = len(run_final) - len(bulk_runs)

    # Pass 2: aggregate bulk runs' late-window rows
    s = {key: 0.0 for key in [
        "occ", "occ_in_cs", "cs", "births", "M",
        "sl_inc", "s_uniq", "s_comp", "s_cen", "ms_inc", "ms_cen"]}
    n = 0
    N = k = None
    with open(path) as f:
        header = f.readline().strip().split(",")
        C = {c: i for i, c in enumerate(header)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            if v[C["run_id"]] not in bulk_runs:
                continue
            if int(v[C["step"]]) < step_min:
                continue
            if N is None:
                N, k = int(v[C["N"]]), int(v[C["k"]])
            s["occ"]    += float(v[C["occ_clean_pairs"]])
            s["occ_in_cs"] += float(v[C["occ_clean_pairs_in_clean_star"]])
            s["cs"]     += float(v[C["clean_star_components"]])
            s["births"] += float(v[C["births_step"]])
            s["M"]      += float(v[C["M_pre"]])
            s["sl_inc"] += float(v[C["struct_leaf_incidence_total"]])
            s["s_uniq"] += float(v[C["struct_unique_leaves_total"]])
            s["s_comp"] += float(v[C["struct_component_count"]])
            s["s_cen"]  += float(v[C["struct_center_count"]])
            s["ms_inc"] += float(v[C["multistar_leaf_incidence_total"]])
            s["ms_cen"] += float(v[C["multistar_centers_total"]])
            n += 1

    band = 2 * k + 1
    O, M = s["occ"], s["M"]
    res = {
        "N": N, "k": k, "band": band, "rows": n,
        "tail_runs": tail_runs, "bulk_runs": len(bulk_runs),
        "psi_slot": O / (band * M) if M else 0.0,
        "cbar_slot": O / M if M else 0.0,
        "cbar_struct_per_comp": s["s_uniq"] / s["s_comp"] if s["s_comp"] else 0.0,
        "cbar_struct_node": s["sl_inc"] / M if M else 0.0,
        "cbar_struct_per_center": s["sl_inc"] / s["s_cen"] if s["s_cen"] else 0.0,
        "C_birth": s["births"] / O if O else 0.0,
        "C_component": s["occ_in_cs"] / O if O else 0.0,
    }
    res["q_proj_per_comp"]   = res["cbar_slot"] / res["cbar_struct_per_comp"] if res["cbar_struct_per_comp"] else 0.0
    res["q_proj_node"]       = res["cbar_slot"] / res["cbar_struct_node"] if res["cbar_struct_node"] else 0.0
    res["q_proj_per_center"] = res["cbar_slot"] / res["cbar_struct_per_center"] if res["cbar_struct_per_center"] else 0.0
    return res

def fit(xs, ys):
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    n = len(lx); mx = sum(lx)/n; my = sum(ly)/n
    sxx = sum((a-mx)**2 for a in lx); sxy = sum((lx[i]-mx)*(ly[i]-my) for i in range(n))
    a = sxy/sxx; b = my - a*mx
    ss = sum((ly[i]-my)**2 for i in range(n))
    sr = sum((ly[i]-(b+a*lx[i]))**2 for i in range(n))
    return a, (1 - sr/ss if ss else float("nan"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--step-min", type=int, default=4001)
    p.add_argument("--tail-threshold", type=float, default=500)
    p.add_argument("--min-n-fit", type=int, default=0, help="exclude N below this from exponent fits (e.g. 480 to drop transients)")
    args = p.parse_args()

    raw = [process(c, args.step_min, args.tail_threshold) for c in args.csvs]
    # pool same-N cells (recompute ratios from summed counts is ideal, but here
    # files are distinct N; if duplicates exist, keep the one with more rows)
    by_n = {}
    for r in raw:
        if r["N"] not in by_n or r["rows"] > by_n[r["N"]]["rows"]:
            by_n[r["N"]] = r
    rows = list(by_n.values())
    rows.sort(key=lambda r: r["N"])

    print(f"{'N':>5} {'band':>5} {'psi_slot':>10} {'cbar_slot':>10} "
          f"{'cbar_str/comp':>13} {'cbar_str/cen':>12} {'q_proj/comp':>11}")
    for r in rows:
        print(f"{r['N']:>5} {r['band']:>5} {r['psi_slot']:>10.6f} {r['cbar_slot']:>10.4f} "
              f"{r['cbar_struct_per_comp']:>13.4f} {r['cbar_struct_per_center']:>12.4f} "
              f"{r['q_proj_per_comp']:>11.5f}")

    if len(rows) >= 2:
        fit_rows = [r for r in rows if r["N"] >= args.min_n_fit]
        Ns = [r["N"] for r in fit_rows]
        tag = f" (N>={args.min_n_fit})" if args.min_n_fit else ""
        print(f"\nN-scaling exponents{tag} (y ~ N^alpha):")
        for key in ["psi_slot", "cbar_slot", "cbar_struct_per_comp",
                    "cbar_struct_per_center", "q_proj_per_comp", "q_proj_per_center"]:
            ys = [r[key] for r in fit_rows]
            if len(ys) >= 2 and all(y > 0 for y in ys):
                a, r2 = fit(Ns, ys)
                print(f"  {key:24s} ~ N^{a:+.3f}  (R^2={r2:.3f})")
    else:
        print("\n[single CSV: single-point claims only — bounded/intensive verifiable, "
              "exponents need >=2 N values]")


if __name__ == "__main__":
    main()
