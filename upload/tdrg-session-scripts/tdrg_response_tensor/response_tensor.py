#!/usr/bin/env python3
"""
response_tensor.py  —  TDR-G response-tensor formalism (branch, exploratory).

[RID: TDRG-RESPONSE-TENSOR]  [BRANCH/NUM diagnostic]

Builds the unnormalized observable response tensor over the control manifold and reads
its intrinsic dimension from the singular-value spectrum, GATED against a null model so
that apparent dimensions from finite-sample noise are not counted as real structure.

Design (per BRANCH_CHARTER):
  - Tensor T[c, o] = log observable o at control cell c.  Controls = (N, k/N, policy).
  - NO normalization, NO baseline division, NO factorization ansatz. Raw log-observables.
  - Centering: subtract per-observable mean (removes units, not structure).
  - Intrinsic dimension = # singular values of centered T exceeding the null ceiling.
  - Null ceiling: resample each observable's cell-values under the null hypothesis of
    "no genuine cross-control structure beyond the dominant trend" (permutation of
    residuals across cells), recompute SVD, take a high quantile of the k-th singular
    value. A direction is REAL only if it clears that ceiling.

This separates the PI's two cases:
  - genuine new dimension  -> singular value above null ceiling (kept, even if count rises);
  - representation noise    -> singular value below ceiling (not counted).

Consolidation tracking: report the cumulative explained variance so that if two
directions later merge under a richer control set, the change is visible as a spectrum
shift, not a silent deletion.
"""

from __future__ import annotations

import csv
import math
import random
from collections import defaultdict


OBSERVABLES = ["C_birth", "chi", "B_per_step", "O_per_step", "occ_in_cs_per_row",
               "ms_abs"]


def pool_cell(path, step_min=4001, tail_threshold=500):
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    bulk = {r for r, m in rf.items() if m <= tail_threshold}
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
            a["oims"] += float(v[C["occ_clean_pairs_in_multistar"]])
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
        "occ_in_cs_per_row": a["oic"] / a["rows"],
        "ms_abs": a["oims"] / a["occ"],
    }
    return {**meta, "k_over_N": meta["k"] / meta["N"], "obs": obs}


def _singular_values(M):
    """Singular values of M (rows x cols) via Jacobi eigen-decomposition of M^T M."""
    rows = len(M); cols = len(M[0]) if rows else 0
    if not rows or not cols:
        return []
    A = [[sum(M[r][i] * M[r][j] for r in range(rows)) for j in range(cols)]
         for i in range(cols)]
    n = cols
    for _ in range(200):
        off = 0.0; p = q = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > off:
                    off = abs(A[i][j]); p, q = i, j
        if off < 1e-15:
            break
        app, aqq, apq = A[p][p], A[q][q], A[p][q]
        phi = 0.5 * math.atan2(2 * apq, aqq - app) if (aqq - app) else math.pi / 4
        c, s = math.cos(phi), math.sin(phi)
        for i in range(n):
            aip, aiq = A[i][p], A[i][q]
            A[i][p] = c * aip - s * aiq; A[i][q] = s * aip + c * aiq
        for i in range(n):
            api, aqi = A[p][i], A[q][i]
            A[p][i] = c * api - s * aqi; A[q][i] = s * api + c * aqi
    return sorted((math.sqrt(max(A[i][i], 0.0)) for i in range(n)), reverse=True)


def _center_columns(T):
    rows = len(T); cols = len(T[0])
    means = [sum(T[r][j] for r in range(rows)) / rows for j in range(cols)]
    return [[T[r][j] - means[j] for j in range(cols)] for r in range(rows)], means


def build_tensor(cells):
    """Return centered log-observable matrix (cells x observables) and labels."""
    obs_names = [o for o in OBSERVABLES if all(o in c["obs"] for c in cells)]
    T = [[math.log(c["obs"][o]) for o in obs_names] for c in cells]
    Tc, _ = _center_columns(T)
    return Tc, obs_names


def null_ceiling(Tc, n_null=500, quantile=0.95, seed=0):
    """Null: independently permute each observable column across cells, destroying any
    genuine cross-observable (shared-direction) structure while preserving each column's
    marginal spread. The surviving singular values are what noise+marginals alone produce."""
    rng = random.Random(seed)
    rows = len(Tc); cols = len(Tc[0]) if rows else 0
    null_sv = [[] for _ in range(cols)]
    cols_data = [[Tc[r][j] for r in range(rows)] for j in range(cols)]
    for _ in range(n_null):
        shuffled = []
        for j in range(cols):
            col = cols_data[j][:]
            rng.shuffle(col)
            shuffled.append(col)
        M = [[shuffled[j][r] for j in range(cols)] for r in range(rows)]
        sv = _singular_values(M)
        for k in range(cols):
            null_sv[k].append(sv[k] if k < len(sv) else 0.0)
    ceil = []
    for k in range(cols):
        s = sorted(null_sv[k])
        idx = min(len(s) - 1, int(quantile * len(s)))
        ceil.append(s[idx])
    return ceil


def intrinsic_dimension(cells, n_null=500, quantile=0.95, seed=0):
    Tc, obs_names = build_tensor(cells)
    sv = _singular_values(Tc)
    ceil = null_ceiling(Tc, n_null=n_null, quantile=quantile, seed=seed)
    total = sum(s * s for s in sv) or 1.0
    s0 = sv[0] if sv else 0.0
    floor = 1e-6 * s0  # numerical-zero guard relative to leading singular value
    real = []
    for k, s in enumerate(sv):
        c = ceil[k] if k < len(ceil) else 0.0
        real.append(s > c and s > floor)
    dim = sum(1 for r in real if r)
    # cumulative explained variance (for consolidation tracking)
    cum = []
    run = 0.0
    for s in sv:
        run += s * s
        cum.append(run / total)
    return {
        "n_cells": len(cells),
        "n_observables": len(obs_names),
        "observables": obs_names,
        "singular_values": sv,
        "null_ceiling": ceil,
        "real_direction": real,
        "intrinsic_dimension": dim,
        "cumulative_variance": cum,
        "control_levers": _active_levers(cells),
    }


def _active_levers(cells):
    levers = []
    if len({c["N"] for c in cells}) > 1: levers.append("N")
    if len({round(c["k_over_N"], 6) for c in cells}) > 1: levers.append("k/N")
    if len({c["policy"] for c in cells}) > 1: levers.append("policy")
    return levers


def report(cells, n_null=500, quantile=0.95, seed=0):
    r = intrinsic_dimension(cells, n_null, quantile, seed)
    print(f"control levers active: {r['control_levers'] or ['(none — single cell)']}")
    print(f"cells={r['n_cells']}  observables={r['n_observables']}  "
          f"max possible dim={min(r['n_cells']-1, r['n_observables'])}")
    print(f"\n{'k':>3} {'sing.val':>10} {'null_ceil':>10} {'real?':>6} {'cum.var':>8}")
    for k, s in enumerate(r["singular_values"]):
        c = r["null_ceiling"][k] if k < len(r["null_ceiling"]) else 0.0
        print(f"{k:>3} {s:>10.4f} {c:>10.4f} {'YES' if r['real_direction'][k] else 'no':>6} "
              f"{r['cumulative_variance'][k]:>8.3f}")
    print(f"\nINTRINSIC DIMENSION (null-gated) = {r['intrinsic_dimension']}")
    # Calibration (synthetic recovery, permutation null): reliable for dim<=1 at any
    # cell count; higher dims are UNDER-counted until ~40-80 cells. Report confidence.
    nc = r["n_cells"]
    if r["intrinsic_dimension"] <= 1:
        conf = "HIGH (dim<=1 reliable at all cell counts)"
    elif nc >= 40:
        conf = "MODERATE (>=40 cells; higher-dim recovery improving but still noisy)"
    else:
        conf = (f"LOW ({nc} cells; permutation null under-counts dim>=2 below ~40 cells — "
                f"treat as a LOWER BOUND on intrinsic dimension)")
    print(f"  confidence: {conf}")
    if len(r["control_levers"]) < 2:
        print(f"  [SCOPE] control manifold has {len(r['control_levers'])} active lever(s); "
              f"intrinsic dimension is UPPER-BOUNDED by control rank, not fully resolved. "
              f"Add k/N and/or policy variation to resolve.")
    return r


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("usage: response_tensor.py motif_*.csv [n_null] [quantile]"); sys.exit(2)
    paths = [a for a in sys.argv[1:] if a.endswith(".csv")]
    nums = [a for a in sys.argv[1:] if not a.endswith(".csv")]
    n_null = int(nums[0]) if nums else 500
    quantile = float(nums[1]) if len(nums) > 1 else 0.95
    cells = [c for c in (pool_cell(p) for p in paths) if c]
    report(cells, n_null=n_null, quantile=quantile)
