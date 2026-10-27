#!/usr/bin/env python3
"""
tdr_motif_analysis.py
Reads TDR-G motif CSV logs and computes the TDR-24 factorization aggregates.

Key quantities (Document 18 / collaborator factorization):
  C_birth     = births / occ_clean_pairs            (total precursor-to-birth rate)
  C_component = occ_clean_in_clean_star / occ_clean  (topological filtering)
  chi         = occ_clean_in_clean_star / clean_star_components (pair-to-component compression)
  V_pair      = occ_multistar_pairs / occ_clean_pairs (multistar vacuum fraction)

Identity (ALG): C_birth = C_component / chi  (up to rounding)

Usage:
  python tdr_motif_analysis.py motif_N120_k8.csv motif_N240_k16.csv ...
  python tdr_motif_analysis.py --glob "motif_*.csv"
  python tdr_motif_analysis.py --dir /path/to/csvs
"""

from __future__ import annotations
import csv
import sys
import os
import glob
import argparse
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# CSV reader
# ---------------------------------------------------------------------------

def read_motif_csv(path: str) -> list[dict]:
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({k: v.strip() for k, v in row.items()})
    return rows


def to_float(v: str) -> float:
    try:
        return float(v)
    except (ValueError, TypeError):
        return 0.0


# ---------------------------------------------------------------------------
# Column detection
# ---------------------------------------------------------------------------

REQUIRED_COLS = {
    "births_step",
    "clean_star_components",
    "occ_clean_pairs",
}

OPTIONAL_COLS = {
    "occ_multistar_pairs",
    "occ_clean_pairs_in_clean_star",
    "occ_clean_pairs_in_multistar",
    "multistar_components",
    "M_pre",
    "rho",
    "run_id",
    "step",
    "N",
    "k",
}


def check_columns(rows: list[dict], path: str) -> set[str]:
    if not rows:
        print(f"  WARNING: {path} is empty")
        return set()
    available = set(rows[0].keys())
    missing = REQUIRED_COLS - available
    if missing:
        print(f"  WARNING: {path} missing required columns: {missing}")
    return available


# ---------------------------------------------------------------------------
# Aggregate computation
# ---------------------------------------------------------------------------

def compute_aggregates(rows: list[dict], available: set[str]) -> dict:
    """Pool-level aggregate computation. Avoid Jensen artifacts."""

    sum_births = 0.0
    sum_clean_stars = 0.0
    sum_occ_clean = 0.0
    sum_occ_ms = 0.0
    sum_occ_in_clean_star = 0.0
    sum_occ_in_ms = 0.0
    sum_ms_components = 0.0
    n_rows = 0
    n_rows_with_births = 0
    n_rows_with_ms = 0

    # For M_pre binning
    m_bins = defaultdict(lambda: defaultdict(float))

    for row in rows:
        n_rows += 1
        b = to_float(row.get("births_step", 0))
        cs = to_float(row.get("clean_star_components", 0))
        occ = to_float(row.get("occ_clean_pairs", 0))
        oms = to_float(row.get("occ_multistar_pairs", 0))
        oics = to_float(row.get("occ_clean_pairs_in_clean_star", 0))
        oims = to_float(row.get("occ_clean_pairs_in_multistar", 0))
        msc = to_float(row.get("multistar_components", 0))
        m_pre = to_float(row.get("M_pre", 0))

        sum_births += b
        sum_clean_stars += cs
        sum_occ_clean += occ
        sum_occ_ms += oms
        sum_occ_in_clean_star += oics
        sum_occ_in_ms += oims
        sum_ms_components += msc

        if b > 0 or cs > 0:
            n_rows_with_births += 1
        if msc > 0:
            n_rows_with_ms += 1

        # M_pre binning (round to nearest 10)
        if m_pre > 0:
            bin_key = int(round(m_pre / 10.0)) * 10
            m_bins[bin_key]["births"] += b
            m_bins[bin_key]["occ_clean"] += occ
            m_bins[bin_key]["multistars"] += msc
            m_bins[bin_key]["occ_in_clean"] += oics
            m_bins[bin_key]["count"] += 1

    # Pool-level rates
    C_birth = sum_births / sum_occ_clean if sum_occ_clean > 0 else 0.0
    C_component = sum_occ_in_clean_star / sum_occ_clean if sum_occ_clean > 0 else None
    chi = sum_occ_in_clean_star / sum_clean_stars if sum_clean_stars > 0 else None
    V_pair = sum_occ_ms / sum_occ_clean if sum_occ_clean > 0 else None

    # Identity check: C_birth = C_component / chi
    identity_err = None
    if C_component is not None and chi is not None and chi > 0:
        C_birth_reconstructed = C_component / chi
        identity_err = abs(C_birth - C_birth_reconstructed)

    # Birth identity: births_step == clean_star_components for nonzero rows
    # Check from rows
    birth_identity_matches = 0
    birth_identity_total = 0
    for row in rows:
        b = to_float(row.get("births_step", 0))
        cs = to_float(row.get("clean_star_components", 0))
        if b > 0 or cs > 0:
            birth_identity_total += 1
            if abs(b - cs) < 0.5:
                birth_identity_matches += 1

    ms_prevalence = n_rows_with_ms / n_rows if n_rows > 0 else 0.0

    return {
        "n_rows": n_rows,
        "sum_births": sum_births,
        "sum_clean_stars": sum_clean_stars,
        "sum_occ_clean": sum_occ_clean,
        "sum_occ_ms": sum_occ_ms,
        "sum_occ_in_clean_star": sum_occ_in_clean_star,
        "C_birth": C_birth,
        "C_component": C_component,
        "chi": chi,
        "V_pair": V_pair,
        "identity_err": identity_err,
        "birth_identity_matches": birth_identity_matches,
        "birth_identity_total": birth_identity_total,
        "ms_prevalence": ms_prevalence,
        "m_bins": dict(m_bins),
        "has_occ_in_clean": "occ_clean_pairs_in_clean_star" in available,
    }


# ---------------------------------------------------------------------------
# DSN tag assignment
# ---------------------------------------------------------------------------

def dsn_tag(agg: dict) -> str:
    """
    Assign DSN epistemic tag based on data quality.
    [NUM] if birth identity passes and occ_in_clean tracked.
    [HEUR] if occ_in_clean absent (C_component not computable).
    """
    if agg["birth_identity_total"] > 0:
        frac = agg["birth_identity_matches"] / agg["birth_identity_total"]
        if frac >= 0.99 and agg["has_occ_in_clean"]:
            return "[NUM]"
        elif frac >= 0.95:
            return "[HEUR-strong]"
    return "[HEUR]"


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def format_report(path: str, agg: dict, available: set[str]) -> str:
    name = Path(path).stem
    tag = dsn_tag(agg)

    lines = [
        f"=== {name} {tag} ===",
        f"  rows={agg['n_rows']}  births={agg['sum_births']:.0f}  clean_stars={agg['sum_clean_stars']:.0f}",
        f"  occ_clean_pairs={agg['sum_occ_clean']:.0f}",
    ]

    # Birth identity
    bi = agg["birth_identity_total"]
    bm = agg["birth_identity_matches"]
    if bi > 0:
        lines.append(f"  birth_identity: {bm}/{bi} = {bm/bi:.4f}  "
                     f"{'[NUM] PASS' if bm==bi else '[FAIL] MISMATCH'}")

    # Core factorization
    lines.append("")
    lines.append("  TDR-24 factorization:")
    lines.append(f"    C_birth     = {agg['C_birth']:.6f}  (births / occ_clean)")

    if agg["C_component"] is not None:
        lines.append(f"    C_component = {agg['C_component']:.6f}  (occ_in_clean_star / occ_clean)")
    else:
        lines.append("    C_component = N/A  (occ_clean_pairs_in_clean_star not logged)")

    if agg["chi"] is not None:
        lines.append(f"    chi         = {agg['chi']:.4f}   (occ_in_clean_star / clean_star_components)")
    else:
        lines.append("    chi         = N/A")

    if agg["V_pair"] is not None:
        lines.append(f"    V_pair      = {agg['V_pair']:.6f}  (occ_multistar / occ_clean)")

    if agg["identity_err"] is not None:
        err_tag = "[ALG OK]" if agg["identity_err"] < 1e-9 else f"[ERR={agg['identity_err']:.2e}]"
        lines.append(f"    C_birth = C_component/chi: err={agg['identity_err']:.2e} {err_tag}")

    if agg["sum_occ_clean"] > 0:
        survival_pct = agg["C_birth"] * 100
        lines.append(f"    survival: {survival_pct:.4f}% of occ_clean candidates become births")

    # Multistar prevalence
    lines.append("")
    lines.append(f"  ms_prevalence = {agg['ms_prevalence']:.4f} ({agg['ms_prevalence']*100:.1f}% of steps have multistar component)")

    # M_pre binning
    if agg["m_bins"]:
        lines.append("")
        lines.append("  M_pre bins:")
        lines.append(f"  {'M_pre':>8} {'C_birth':>10} {'V_pair_approx':>14} {'ms/step':>8} {'count':>7}")
        for m_key in sorted(agg["m_bins"].keys()):
            b = agg["m_bins"][m_key]
            occ = b["occ_clean"]
            cb = b["births"] / occ if occ > 0 else 0.0
            ms = b["multistars"] / b["count"] if b["count"] > 0 else 0.0
            lines.append(f"  {m_key:>8}   {cb:>10.6f}  {'N/A':>14}   {ms:>8.3f}  {int(b['count']):>7}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Scaling summary across files
# ---------------------------------------------------------------------------

def print_scaling_summary(results: list[tuple[str, dict]]) -> None:
    if len(results) < 2:
        return

    print("\n" + "="*70)
    print("SCALING SUMMARY (pool-level, sorted by filename)")
    print("="*70)
    header = f"{'file':>30} {'C_birth':>10} {'C_comp':>10} {'chi':>8} {'V_pair':>8}"
    print(header)
    print("-"*70)

    for path, agg in sorted(results, key=lambda x: x[0]):
        name = Path(path).stem[:30]
        cb = f"{agg['C_birth']:.6f}" if agg["C_birth"] is not None else "N/A"
        cc = f"{agg['C_component']:.6f}" if agg["C_component"] is not None else "N/A"
        ch = f"{agg['chi']:.4f}" if agg["chi"] is not None else "N/A"
        vp = f"{agg['V_pair']:.4f}" if agg["V_pair"] is not None else "N/A"
        print(f"{name:>30} {cb:>10} {cc:>10} {ch:>8} {vp:>8}")

    # Power-law fit on C_birth if N can be extracted from filename
    import re
    N_vals = []
    cb_vals = []
    for path, agg in results:
        m = re.search(r'N(\d+)', Path(path).stem)
        if m and agg["C_birth"] > 0:
            N_vals.append(int(m.group(1)))
            cb_vals.append(agg["C_birth"])

    if len(N_vals) >= 3:
        import math
        # Log-log fit
        log_N = [math.log(n) for n in N_vals]
        log_cb = [math.log(c) for c in cb_vals]
        n = len(log_N)
        mean_lN = sum(log_N)/n
        mean_lcb = sum(log_cb)/n
        num = sum((log_N[i]-mean_lN)*(log_cb[i]-mean_lcb) for i in range(n))
        den = sum((log_N[i]-mean_lN)**2 for i in range(n))
        alpha = -num/den if den > 0 else None
        if alpha is not None:
            print(f"\n  [HEUR] Power-law fit C_birth ~ N^(-alpha): alpha = {alpha:.3f}")
            print(f"         (from {n} files with N extracted from filename)")
            print(f"         N values: {sorted(N_vals)}")


# ---------------------------------------------------------------------------
# DSN patch output
# ---------------------------------------------------------------------------

def print_dsn_patch(results: list[tuple[str, dict]]) -> None:
    print("\n" + "="*70)
    print("DSN PATCH BLOCK (copy into TDR-G DSN)")
    print("="*70)

    for path, agg in sorted(results, key=lambda x: x[0]):
        name = Path(path).stem
        tag = dsn_tag(agg)
        bi = agg["birth_identity_total"]
        bm = agg["birth_identity_matches"]
        print(f"""
{tag} Motif log: {name}
  births_step == clean_star_components: {bm}/{bi} rows {'' if bi==0 else ('PASS' if bm==bi else 'FAIL')}
  C_birth     = {agg['C_birth']:.5f}  (births / occ_clean_pairs)""")
        if agg["C_component"] is not None:
            print(f"  C_component = {agg['C_component']:.5f}  (topological filter)")
        if agg["chi"] is not None:
            print(f"  chi         = {agg['chi']:.3f}   (pair-to-component compression)")
        if agg["V_pair"] is not None:
            print(f"  V_pair      = {agg['V_pair']:.5f}  (multistar vacuum fraction)")
        print(f"  ms_prevalence = {agg['ms_prevalence']:.4f}")

    print("""
[OPEN TDR-24A] Derive C_component from defect-graph combinatorics and multistar locking.
[OPEN TDR-24B] Derive chi, the pair-to-component compression factor.
[OPEN TDR-24C] Determine whether C_birth(N) -> 0 at fixed k/N as N -> inf.
""")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="TDR-G motif analysis — TDR-24 factorization")
    parser.add_argument("files", nargs="*", help="CSV files to analyse")
    parser.add_argument("--glob", help="Glob pattern for CSV files")
    parser.add_argument("--dir", help="Directory to scan for CSV files")
    parser.add_argument("--dsn-patch", action="store_true", help="Print DSN patch block")
    args = parser.parse_args()

    paths = list(args.files)
    if args.glob:
        paths += glob.glob(args.glob)
    if args.dir:
        paths += glob.glob(os.path.join(args.dir, "*.csv"))

    if not paths:
        print("No files specified. Usage: python tdr_motif_analysis.py file1.csv file2.csv")
        print("  or: python tdr_motif_analysis.py --glob 'motif_*.csv'")
        sys.exit(0)

    results = []
    for path in paths:
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping")
            continue
        rows = read_motif_csv(path)
        available = check_columns(rows, path)
        agg = compute_aggregates(rows, available)
        print(format_report(path, agg, available))
        print()
        results.append((path, agg))

    if len(results) > 1:
        print_scaling_summary(results)

    if args.dsn_patch or len(results) >= 1:
        print_dsn_patch(results)


if __name__ == "__main__":
    main()