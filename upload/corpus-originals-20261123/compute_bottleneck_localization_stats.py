# -*- coding: utf-8 -*-
"""
compute_bottleneck_localization_stats.py

Purpose
-------
Quantify the "bottleneck dominance" interaction effect:

  BOTTLENECK = (is_core == True) & (n_active_faces == 2)

Compare bottleneck κ3^dens against:
  - rest (everything else)
  - core bulk (is_core & n_active>=3)
  - shell (~is_core)

Works per adjacency mode (edge/vertex) and can optionally do per-seed stats.

Inputs
------
  k3_relational_faces.csv from k3_relational_anatomy.py

Outputs
-------
  bottleneck_localization_stats.json
  bottleneck_localization_stats.csv
  bottleneck_localization_by_seed.csv  (if --by-seed)

Usage
-----
  python scripts/esm/compute_bottleneck_localization_stats.py ^
    --infile k3_relational_faces.csv ^
    --out-json bottleneck_localization_stats.json ^
    --out-csv  bottleneck_localization_stats.csv ^
    --by-seed
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu


REQ_COLS = ["seed", "adjacency", "n_active_faces", "is_core", "kappa3_dens"]


def _finite(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return x[np.isfinite(x)]


def bootstrap_median_ci(
    x: np.ndarray,
    n_boot: int = 20000,
    ci: float = 0.95,
    seed: int = 12345,
) -> Tuple[float, float]:
    x = _finite(x)
    if x.size == 0:
        return (np.nan, np.nan)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, x.size, size=(n_boot, x.size))
    meds = np.median(x[idx], axis=1)
    lo = np.percentile(meds, (1 - ci) / 2 * 100)
    hi = np.percentile(meds, (1 + ci) / 2 * 100)
    return float(lo), float(hi)


def cohens_d(x: np.ndarray, y: np.ndarray) -> float:
    x = _finite(x)
    y = _finite(y)
    if x.size < 2 or y.size < 2:
        return np.nan
    mx, my = float(np.mean(x)), float(np.mean(y))
    sx, sy = float(np.std(x, ddof=1)), float(np.std(y, ddof=1))
    denom = (x.size + y.size - 2)
    if denom <= 0:
        return np.nan
    pooled = np.sqrt(((x.size - 1) * sx**2 + (y.size - 1) * sy**2) / denom)
    return float((mx - my) / pooled) if pooled != 0 else np.nan


def cliffs_delta(x: np.ndarray, y: np.ndarray) -> float:
    x = _finite(x)
    y = _finite(y)
    if x.size == 0 or y.size == 0:
        return np.nan
    # Vectorized sign matrix; OK for our N (~100s)
    s = np.sign(x[:, None] - y[None, :])
    return float(np.sum(s) / (x.size * y.size))


def mw_test(x: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    x = _finite(x)
    y = _finite(y)
    if x.size == 0 or y.size == 0:
        return (np.nan, np.nan)
    u, p = mannwhitneyu(x, y, alternative="two-sided")
    return float(u), float(p)


def summarize_pair(name: str, x: np.ndarray, y: np.ndarray) -> Dict:
    u, p = mw_test(x, y)
    return {
        "comparison": name,
        "Nx": int(np.isfinite(x).sum()),
        "Ny": int(np.isfinite(y).sum()),
        "median_x": float(np.nanmedian(x)) if np.isfinite(x).any() else np.nan,
        "median_y": float(np.nanmedian(y)) if np.isfinite(y).any() else np.nan,
        "mean_x": float(np.nanmean(x)) if np.isfinite(x).any() else np.nan,
        "mean_y": float(np.nanmean(y)) if np.isfinite(y).any() else np.nan,
        "U": u,
        "p": p,
        "cohens_d": cohens_d(x, y),
        "cliffs_delta": cliffs_delta(x, y),
        "median_ci_x": bootstrap_median_ci(x),
        "median_ci_y": bootstrap_median_ci(y),
        "median_ratio_x_over_y": (
            float(np.nanmedian(x) / np.nanmedian(y))
            if np.isfinite(x).any() and np.isfinite(y).any() and np.nanmedian(y) != 0
            else np.nan
        ),
    }


def analyze_block(df: pd.DataFrame) -> Dict:
    # Populations
    bottleneck = df[(df["is_core"] == True) & (df["n_active_faces"] == 2)]["kappa3_dens"].values
    core_bulk = df[(df["is_core"] == True) & (df["n_active_faces"] >= 3)]["kappa3_dens"].values
    shell = df[(df["is_core"] == False)]["kappa3_dens"].values
    rest = df[~((df["is_core"] == True) & (df["n_active_faces"] == 2))]["kappa3_dens"].values

    out = {
        "counts": {
            "N_total": int(len(df)),
            "N_bottleneck": int(np.isfinite(bottleneck).sum()),
            "N_core_bulk": int(np.isfinite(core_bulk).sum()),
            "N_shell": int(np.isfinite(shell).sum()),
            "N_rest": int(np.isfinite(rest).sum()),
        },
        "medians": {
            "bottleneck": float(np.nanmedian(bottleneck)) if np.isfinite(bottleneck).any() else np.nan,
            "core_bulk": float(np.nanmedian(core_bulk)) if np.isfinite(core_bulk).any() else np.nan,
            "shell": float(np.nanmedian(shell)) if np.isfinite(shell).any() else np.nan,
            "rest": float(np.nanmedian(rest)) if np.isfinite(rest).any() else np.nan,
        },
        "primary_test": summarize_pair("bottleneck vs rest", bottleneck, rest),
        "secondary_tests": [
            summarize_pair("bottleneck vs core_bulk", bottleneck, core_bulk),
            summarize_pair("bottleneck vs shell", bottleneck, shell),
            summarize_pair("core_bulk vs shell", core_bulk, shell),
        ],
    }
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--infile", default="k3_relational_faces.csv")
    ap.add_argument("--out-json", default="bottleneck_localization_stats.json")
    ap.add_argument("--out-csv", default="bottleneck_localization_stats.csv")
    ap.add_argument("--by-seed", action="store_true")
    args = ap.parse_args()

    infile = Path(args.infile).resolve()
    if not infile.exists():
        raise FileNotFoundError(infile)

    df = pd.read_csv(infile)
    missing = [c for c in REQ_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"{infile.name} missing {missing}")

    # Keep only Type-I (already) and finite dens
    df = df.copy()
    df["kappa3_dens"] = pd.to_numeric(df["kappa3_dens"], errors="coerce")
    df = df[np.isfinite(df["kappa3_dens"].values)].copy()

    results = []
    full_report: Dict = {"infile": str(infile), "by_adjacency": {}}

    for adj in sorted(df["adjacency"].unique()):
        sub = df[df["adjacency"] == adj].copy()
        block = analyze_block(sub)
        full_report["by_adjacency"][adj] = block

        # Flat rows for CSV
        prim = block["primary_test"]
        results.append({
            "adjacency": adj,
            "comparison": prim["comparison"],
            "Nx": prim["Nx"], "Ny": prim["Ny"],
            "median_x": prim["median_x"], "median_y": prim["median_y"],
            "median_ratio_x_over_y": prim["median_ratio_x_over_y"],
            "U": prim["U"], "p": prim["p"],
            "cohens_d": prim["cohens_d"], "cliffs_delta": prim["cliffs_delta"],
        })

    pd.DataFrame(results).to_csv(args.out_csv, index=False)
    with open(args.out_json, "w", encoding="utf-8") as f:
        json.dump(full_report, f, indent=2)

    print("Wrote:", args.out_csv)
    print("Wrote:", args.out_json)

    if args.by_seed:
        by_seed_rows = []
        for (seed, adj), g in df.groupby(["seed", "adjacency"]):
            block = analyze_block(g)
            prim = block["primary_test"]
            by_seed_rows.append({
                "seed": int(seed),
                "adjacency": str(adj),
                "N_total": block["counts"]["N_total"],
                "N_bottleneck": block["counts"]["N_bottleneck"],
                "N_rest": block["counts"]["N_rest"],
                "median_bottleneck": block["medians"]["bottleneck"],
                "median_rest": block["medians"]["rest"],
                "ratio": prim["median_ratio_x_over_y"],
                "p": prim["p"],
                "cohens_d": prim["cohens_d"],
                "cliffs_delta": prim["cliffs_delta"],
            })
        out_seed = "bottleneck_localization_by_seed.csv"
        pd.DataFrame(by_seed_rows).sort_values(["adjacency", "seed"]).to_csv(out_seed, index=False)
        print("Wrote:", out_seed)


if __name__ == "__main__":
    main()
