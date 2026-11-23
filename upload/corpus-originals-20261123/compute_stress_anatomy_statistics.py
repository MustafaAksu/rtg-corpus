# -*- coding: utf-8 -*-
"""
compute_stress_anatomy_statistics.py

Purpose
-------
Two independent checks for Phase-3 κ3 anatomy:

A) Stress Anatomy (PRIMARY, always runs)
   - Uses π/2 probe outputs (E_ref_same/E_ref_opp, ratio_E, gap_opp, n_active_faces).
   - Computes kappa3_dens := (E_opp - E_same)/n_active_faces.
   - Filters Type-I(A) using the validated π/2 gate:
       n_active_faces>=2 AND percolation_ratio_E>=ratio_min AND gap_ref_opp<=gap_max
   - Compares Boundary vs Core:
       Boundary := n_active_faces<=2
       Core     := n_active_faces>=3
   - Reports: Mann–Whitney U (two-sided), bootstrap 95% CI for medians,
              effect sizes (Cliff's delta + Cohen's d).

B) Softening / Yielding (OPTIONAL, only if Q_opp exists)
   - If Q_opp is present in the loaded CSVs, reports % of Type-I(A) faces with Q_opp<0.
   - IMPORTANT: Q_opp is NOT produced by the π/2 shear probe by default.
     It typically comes from symmetric ±α small-angle quartic scans.
   - Therefore: missing Q_opp is normal and should NOT skip the analysis.

Usage
-----
python scripts/esm/compute_stress_anatomy_statistics.py --data-dir data_phase3 --save-samples

Outputs
-------
- stress_anatomy_stats.json
- stress_anatomy_samples.csv (if --save-samples)
"""

from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path
from typing import List, Tuple, Optional

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu


# Required for PRIMARY stress anatomy (π/2 dataset)
REQUIRED_COLS_PRIMARY = [
    "seed", "face_id", "n_active_faces",
    "percolation_ratio_E", "gap_ref_opp",
    "E_ref_same", "E_ref_opp",
]

# Optional column for softening check
OPTIONAL_COLS = ["Q_opp"]


def bootstrap_median_ci(
    x: np.ndarray,
    n_boot: int = 10000,
    ci: float = 0.95,
    rng: Optional[np.random.Generator] = None
) -> Tuple[float, float]:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if x.size == 0:
        return (float("nan"), float("nan"))
    if rng is None:
        rng = np.random.default_rng(12345)

    # Vectorized bootstrap
    idxs = rng.integers(0, x.size, size=(n_boot, x.size))
    meds = np.median(x[idxs], axis=1)

    lo = np.percentile(meds, (1 - ci) / 2 * 100)
    hi = np.percentile(meds, (1 + ci) / 2 * 100)
    return float(lo), float(hi)


def cohens_d(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    x = x[np.isfinite(x)]
    y = y[np.isfinite(y)]
    if x.size < 2 or y.size < 2:
        return float("nan")

    mx, my = float(np.mean(x)), float(np.mean(y))
    sx, sy = float(np.std(x, ddof=1)), float(np.std(y, ddof=1))
    pooled = np.sqrt(((x.size - 1) * sx * sx + (y.size - 1) * sy * sy) / (x.size + y.size - 2))
    if pooled == 0:
        return float("nan")
    return float((mx - my) / pooled)


def cliffs_delta(x: np.ndarray, y: np.ndarray) -> float:
    """
    Cliff's delta: P(X>Y) - P(X<Y), range [-1, 1].
    Vectorized O(n*m) sign matrix; fine for typical Phase-3 sizes.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    x = x[np.isfinite(x)]
    y = y[np.isfinite(y)]
    if x.size == 0 or y.size == 0:
        return float("nan")
    m, n = x.size, y.size
    dom = np.sign(x[:, None] - y[None, :])
    return float(np.sum(dom) / (m * n))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", type=str, default="data_phase3")
    ap.add_argument("--ratio-min", type=float, default=2.6)
    ap.add_argument("--gap-max", type=float, default=1e-2)
    ap.add_argument("--out-json", type=str, default="stress_anatomy_stats.json")
    ap.add_argument("--save-samples", action="store_true")
    ap.add_argument("--boot", type=int, default=10000)
    ap.add_argument("--ci", type=float, default=0.95)
    args = ap.parse_args()

    data_dir = Path(args.data_dir).resolve()
    files = sorted(glob.glob(str(data_dir / "k3_scan_seed*.csv")))

    if not files:
        print(f"No files found in {data_dir}")
        return

    print(f"--- Loading {len(files)} seeds ---")

    dfs: List[pd.DataFrame] = []
    q_present_any = False

    for f in files:
        try:
            df = pd.read_csv(f)

            missing_primary = [c for c in REQUIRED_COLS_PRIMARY if c not in df.columns]
            if missing_primary:
                print(f"Skipping {Path(f).name}: missing {missing_primary}")
                continue

            # Normalize types
            df["seed"] = df["seed"].astype(int)
            df["face_id"] = df["face_id"].astype(int)
            df["n_active_faces"] = df["n_active_faces"].astype(int)

            # Optional Q_opp
            if "Q_opp" in df.columns:
                q_present_any = True

            dfs.append(df)

        except Exception as e:
            print(f"Error reading {f}: {e}")

    if not dfs:
        print("No valid dataframes loaded.")
        return

    full = pd.concat(dfs, ignore_index=True)

    # Compute stress density
    full["dE"] = full["E_ref_opp"] - full["E_ref_same"]
    full["kappa3_dens"] = full["dE"] / full["n_active_faces"].clip(lower=1)

    # Apply Type-I(A) Gate
    gate = (
        (full["n_active_faces"] >= 2) &
        (full["percolation_ratio_E"] >= float(args.ratio_min)) &
        (full["gap_ref_opp"] <= float(args.gap_max))
    )
    typeI = full[gate].copy()

    # Split boundary vs core by n_active
    boundary = typeI[typeI["n_active_faces"] <= 2]["kappa3_dens"].to_numpy()
    core = typeI[typeI["n_active_faces"] >= 3]["kappa3_dens"].to_numpy()

    # --- A) Stress Anatomy (PRIMARY) ---
    print("\n=== A. Stress Anatomy Statistics (PRIMARY) ===")
    print(f"Seeds included (loaded): {full['seed'].nunique()}")
    print(f"Total rows (all faces in CSVs): {len(full)}")
    print(f"Type-I rows: {len(typeI)} | Boundary: {len(boundary)} | Core: {len(core)}")

    # Guard: need both groups
    if len(boundary) < 5 or len(core) < 5:
        print("Not enough samples in boundary/core after gate to run statistics reliably.")
        print("Consider increasing face range or verifying gate thresholds.")
        return

    # Stats
    u_stat, p_val = mannwhitneyu(boundary, core, alternative="two-sided", method="asymptotic")
    d = cohens_d(boundary, core)
    cd = cliffs_delta(boundary, core)

    rng = np.random.default_rng(20260209)
    b_ci = bootstrap_median_ci(boundary, n_boot=args.boot, ci=args.ci, rng=rng)
    c_ci = bootstrap_median_ci(core, n_boot=args.boot, ci=args.ci, rng=rng)

    b_med = float(np.median(boundary))
    c_med = float(np.median(core))

    print(f"\nBoundary κ3^dens: median={b_med:.4f}  {int(args.ci*100)}% CI=[{b_ci[0]:.4f},{b_ci[1]:.4f}]  mean={float(np.mean(boundary)):.4f}  N={len(boundary)}")
    print(f"Core     κ3^dens: median={c_med:.4f}  {int(args.ci*100)}% CI=[{c_ci[0]:.4f},{c_ci[1]:.4f}]  mean={float(np.mean(core)):.4f}  N={len(core)}")
    print(f"\nMann–Whitney U: U={float(u_stat):.3f}, p={float(p_val):.6g}")
    print(f"Cliff's delta: {cd:.4f}")
    print(f"Cohen's d:     {d:.4f}")

    # --- B) Softening (OPTIONAL) ---
    print("\n=== B. Softening / Yielding Check (OPTIONAL) ===")
    physics_result = "NOT_EVALUATED"
    soft_count = None
    soft_pct = None
    median_q = None

    if q_present_any and ("Q_opp" in typeI.columns):
        qvals = pd.to_numeric(typeI["Q_opp"], errors="coerce").to_numpy()
        qvals = qvals[np.isfinite(qvals)]
        if qvals.size == 0:
            print("Q_opp present but empty/non-numeric after filtering. Skipping.")
        else:
            soft_count = int(np.sum(qvals < 0.0))
            soft_pct = float(100.0 * soft_count / qvals.size)
            median_q = float(np.median(qvals))
            print(f"Type-I faces with Q_opp available: {qvals.size}")
            print(f"Softening (Q_opp < 0): {soft_pct:.1f}%")
            print(f"Median Q_opp: {median_q:.4e}")
            # Only a diagnostic; do not over-interpret without symmetric ±α protocol.
            physics_result = "DIAGNOSTIC_ONLY"
    else:
        print("Q_opp not found in π/2 scan CSVs (normal). To evaluate softening, run symmetric ±α quartic fits on Type-I subset.")

    # Save report
    report = {
        "scope": {
            "data_dir": str(data_dir),
            "files": [Path(f).name for f in files],
            "gate": {"ratio_min": float(args.ratio_min), "gap_max": float(args.gap_max), "n_active_min": 2},
            "split": {"boundary": "n_active_faces <= 2", "core": "n_active_faces >= 3"},
        },
        "counts": {
            "total_rows": int(len(full)),
            "typeI_rows": int(len(typeI)),
            "boundary_rows": int(len(boundary)),
            "core_rows": int(len(core)),
            "n_seeds_loaded": int(full["seed"].nunique()),
        },
        "stress_anatomy": {
            "boundary": {
                "median": b_med,
                "median_ci": {"ci": float(args.ci), "lo": b_ci[0], "hi": b_ci[1]},
                "mean": float(np.mean(boundary)),
                "n": int(len(boundary)),
            },
            "core": {
                "median": c_med,
                "median_ci": {"ci": float(args.ci), "lo": c_ci[0], "hi": c_ci[1]},
                "mean": float(np.mean(core)),
                "n": int(len(core)),
            },
            "tests": {
                "mann_whitney_u": {"U": float(u_stat), "p_value": float(p_val), "alternative": "two-sided", "method": "asymptotic"},
                "effect_sizes": {"cliffs_delta": float(cd), "cohens_d": float(d)},
            },
        },
        "softening_optional": {
            "q_present_any": bool(q_present_any),
            "evaluated": (soft_pct is not None),
            "softening_pct": soft_pct,
            "median_Q_opp": median_q,
            "verdict": physics_result,
            "notes": "Q_opp is not produced by π/2 probe by default; treat as diagnostic unless derived from symmetric ±α quartic scans.",
        },
    }

    out_json = Path(args.out_json).resolve()
    out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nWrote: {out_json}")

    if args.save_samples:
        out_samples = Path("stress_anatomy_samples.csv").resolve()
        keep_cols = REQUIRED_COLS_PRIMARY + ["dE", "kappa3_dens"]
        # If Q exists, keep it too
        if "Q_opp" in typeI.columns:
            keep_cols.append("Q_opp")
        typeI[keep_cols].to_csv(out_samples, index=False)
        print(f"Wrote: {out_samples} (Type-I samples)")

if __name__ == "__main__":
    main()
