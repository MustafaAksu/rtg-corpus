#!/usr/bin/env python3
"""
tdr_motif_analysis_v3.py
TDR-G / Discrete Relational Genesis motif-log analysis.

Purpose
-------
Reads motif CSV logs emitted by genesis_mode_b_mc.py v14+ and computes
TDR-24 birth-rate factorization diagnostics:

    C_birth      = births / occ_clean_pairs
    C_component  = occ_clean_pairs_in_clean_star / occ_clean_pairs
    chi          = occ_clean_pairs_in_clean_star / clean_star_components
    V_pair_load  = occ_multistar_pairs / occ_clean_pairs

with the aggregate identity, when v15/v16 survival columns are present:

    C_birth = C_component / chi.

Important terminology
---------------------
V_pair_load is a ratio/load, not a probability. It may exceed 1 because
sliding-window occupancy counts can overlap.

Usage
-----
    python tdr_motif_analysis_v3.py motif_N240_k16_v16.csv
    python tdr_motif_analysis_v3.py --glob "motif_*_v16.csv"
    python tdr_motif_analysis_v3.py --dir ./logs --dsn-patch
    python tdr_motif_analysis_v3.py --glob "motif_*_T5000_v16.csv" --step-min 2500 --dsn-patch
    python tdr_motif_analysis_v3.py --glob "motif_*_T5000_v16.csv" --late-frac 0.2 --dsn-patch

Notes
-----
Legacy motif logs lacking occ_clean_pairs_in_clean_star cannot compute
C_component or chi. They are treated as [HEUR-legacy] and excluded from
scaling fits by default.
"""

from __future__ import annotations

import argparse
import csv
import glob
import math
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


REQUIRED_COLS = {
    "births_step",
    "clean_star_components",
    "occ_clean_pairs",
}

SURVIVAL_COLS = {
    "occ_clean_pairs_in_clean_star",
    "occ_clean_pairs_in_multistar",
    "occ_clean_pairs_embedded",
}

OTHER_COLS = ["occ_clean_pairs_other", "occ_clean_pairs_false"]


def to_float(v: Any) -> float:
    if v is None:
        return 0.0
    try:
        if isinstance(v, str):
            v = v.strip()
            if v == "":
                return 0.0
        return float(v)
    except (ValueError, TypeError):
        return 0.0


def to_intish(v: Any) -> int:
    return int(round(to_float(v)))


def read_motif_csv(path: str) -> list[dict[str, str]]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return [{k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()} for row in reader]


def version_score(path: str) -> int:
    stem = Path(path).stem.lower()
    m = re.search(r"v(\d+)", stem)
    if m:
        return int(m.group(1))
    if "stride1" in stem:
        return 14
    return 0


def infer_metadata(path: str, rows: list[dict[str, str]]) -> dict[str, Any]:
    meta: dict[str, Any] = {
        "file": Path(path).stem,
        "version_score": version_score(path),
        "N": None,
        "k": None,
        "k_over_N": None,
        "T_requested": None,
        "batch": None,
        "policy": None,
    }

    if rows:
        r0 = rows[0]
        for key in ["N", "k", "T_requested", "batch", "policy", "k_over_N"]:
            if key in r0 and r0[key] != "":
                if key == "policy":
                    meta[key] = r0[key]
                else:
                    meta[key] = to_float(r0[key])

    # Fallback filename parse: motif_N240_k16...
    stem = Path(path).stem
    if meta["N"] is None:
        m = re.search(r"N(\d+)", stem)
        if m:
            meta["N"] = float(m.group(1))
    if meta["k"] is None:
        m = re.search(r"k(\d+)", stem)
        if m:
            meta["k"] = float(m.group(1))
    if meta["k_over_N"] is None and meta["N"] and meta["k"]:
        meta["k_over_N"] = meta["k"] / meta["N"]

    # normalize integer-ish fields
    for key in ["N", "k", "T_requested", "batch"]:
        if meta[key] is not None:
            meta[key] = int(round(float(meta[key])))
    if meta["k_over_N"] is not None:
        meta["k_over_N"] = float(meta["k_over_N"])

    return meta


def check_columns(rows: list[dict[str, str]], path: str) -> tuple[set[str], list[str]]:
    warnings: list[str] = []
    if not rows:
        warnings.append(f"{path} is empty")
        return set(), warnings
    available = set(rows[0].keys())
    missing = sorted(REQUIRED_COLS - available)
    if missing:
        warnings.append(f"missing required columns: {missing}")
    return available, warnings



def infer_step_range(rows: list[dict[str, str]], meta: dict[str, Any]) -> tuple[int | None, int | None]:
    """Infer min/max integer step in rows, if available."""
    if not rows or "step" not in rows[0]:
        return None, None
    steps = [to_intish(r.get("step")) for r in rows if r.get("step") not in (None, "")]
    if not steps:
        return None, None
    return min(steps), max(steps)


def apply_step_filter(
    rows: list[dict[str, str]],
    meta: dict[str, Any],
    step_min: int | None = None,
    step_max: int | None = None,
    late_frac: float | None = None,
) -> tuple[list[dict[str, str]], dict[str, Any], list[str]]:
    """
    Return rows restricted to a time window.

    Semantics:
      --step-min A keeps rows with step >= A.
      --step-max B keeps rows with step < B.  (half-open upper bound)
      --late-frac f keeps the last f fraction of steps, using T_requested if present,
        otherwise max(step)+1.  It combines with step-min/step-max if both are supplied.

    Filtering is applied per row using the logged `step` column. If `step` is absent,
    no filtering is applied and a warning is returned.
    """
    warnings: list[str] = []
    raw_n = len(rows)
    meta2 = dict(meta)
    meta2["raw_rows"] = raw_n

    if late_frac is not None:
        if not (0.0 < late_frac <= 1.0):
            raise ValueError("--late-frac must satisfy 0 < late_frac <= 1")

    need_filter = step_min is not None or step_max is not None or late_frac is not None
    if not need_filter:
        meta2["row_filter"] = "all"
        meta2["filtered_rows"] = raw_n
        return rows, meta2, warnings

    if not rows or "step" not in rows[0]:
        warnings.append("time-window filter requested but CSV has no step column; using all rows")
        meta2["row_filter"] = "all_no_step_column"
        meta2["filtered_rows"] = raw_n
        return rows, meta2, warnings

    min_step_seen, max_step_seen = infer_step_range(rows, meta)
    if max_step_seen is None:
        warnings.append("time-window filter requested but no valid step values found; using all rows")
        meta2["row_filter"] = "all_no_valid_steps"
        meta2["filtered_rows"] = raw_n
        return rows, meta2, warnings

    lo = step_min
    hi = step_max

    if late_frac is not None:
        T = meta.get("T_requested")
        if T is None or T <= 0:
            T = max_step_seen + 1
        late_lo = int(math.floor(float(T) * (1.0 - late_frac)))
        lo = late_lo if lo is None else max(lo, late_lo)

    if lo is None:
        lo = min_step_seen if min_step_seen is not None else 0
    if hi is None:
        hi = (max_step_seen + 1) if max_step_seen is not None else None

    if hi is not None and hi <= lo:
        raise ValueError(f"empty step window: step_min={lo}, step_max={hi}")

    filtered: list[dict[str, str]] = []
    for row in rows:
        st = to_intish(row.get("step"))
        if st < lo:
            continue
        if hi is not None and st >= hi:
            continue
        filtered.append(row)

    meta2["row_filter"] = f"step>={lo}" + (f", step<{hi}" if hi is not None else "")
    if late_frac is not None:
        meta2["row_filter"] += f", late_frac={late_frac}"
    meta2["filtered_rows"] = len(filtered)
    meta2["step_min_filter"] = lo
    meta2["step_max_filter"] = hi

    if not filtered:
        warnings.append(f"time-window filter kept 0/{raw_n} rows")

    return filtered, meta2, warnings


def compute_aggregates(rows: list[dict[str, str]], available: set[str], path: str) -> dict[str, Any]:
    has_survival = SURVIVAL_COLS <= available
    has_logged_formulas = {"occ_clean_survival_rate", "occ_clean_birth_survival_rate", "occ_clean_component_compression"} <= available
    other_col = "occ_clean_pairs_other" if "occ_clean_pairs_other" in available else (
        "occ_clean_pairs_false" if "occ_clean_pairs_false" in available else None
    )

    sums = defaultdict(float)
    n_rows = 0
    rows_with_birth_or_clean = 0
    birth_identity_matches = 0
    rows_with_multistar = 0
    row_formula_failures = 0
    partition_failures = 0
    max_formula_err = 0.0

    m_bins: dict[int, dict[str, float]] = defaultdict(lambda: defaultdict(float))

    for row in rows:
        n_rows += 1
        births = to_float(row.get("births_step"))
        clean = to_float(row.get("clean_star_components"))
        occ = to_float(row.get("occ_clean_pairs"))
        occ_ms = to_float(row.get("occ_multistar_pairs"))
        ms_comp = to_float(row.get("multistar_components"))
        M_pre = to_float(row.get("M_pre"))
        rho = to_float(row.get("rho"))

        occ_in_clean = to_float(row.get("occ_clean_pairs_in_clean_star"))
        occ_in_ms = to_float(row.get("occ_clean_pairs_in_multistar"))
        occ_embedded = to_float(row.get("occ_clean_pairs_embedded"))
        occ_other = to_float(row.get(other_col)) if other_col else 0.0

        sums["births"] += births
        sums["clean_stars"] += clean
        sums["occ_clean"] += occ
        sums["occ_ms"] += occ_ms
        sums["occ_in_clean"] += occ_in_clean
        sums["occ_in_ms"] += occ_in_ms
        sums["occ_embedded"] += occ_embedded
        sums["occ_other"] += occ_other
        sums["ms_components"] += ms_comp
        sums["rho"] += rho
        sums["M_pre"] += M_pre

        if births > 0 or clean > 0:
            rows_with_birth_or_clean += 1
            if abs(births - clean) < 0.5:
                birth_identity_matches += 1

        if ms_comp > 0:
            rows_with_multistar += 1

        if has_survival and occ > 0:
            part_sum = occ_in_clean + occ_in_ms + occ_embedded + occ_other
            if abs(part_sum - occ) > 0.5:
                partition_failures += 1

            # Validate v16 logged row formulas only if those columns exist.
            if has_logged_formulas:
                logged_ccomp = to_float(row.get("occ_clean_survival_rate"))
                logged_cbirth = to_float(row.get("occ_clean_birth_survival_rate"))
                logged_chi = to_float(row.get("occ_clean_component_compression"))

                calc_ccomp = occ_in_clean / occ
                calc_cbirth = births / occ
                calc_chi = (occ_in_clean / clean) if clean > 0 else 0.0

                for logged, calc in [(logged_ccomp, calc_ccomp), (logged_cbirth, calc_cbirth), (logged_chi, calc_chi)]:
                    err = abs(logged - calc)
                    max_formula_err = max(max_formula_err, err)
                    if err > 1e-9:
                        row_formula_failures += 1
                        break

        if "M_pre" in available:
            bkey = int(M_pre // 10) * 10
            b = m_bins[bkey]
            b["count"] += 1
            b["births"] += births
            b["clean_stars"] += clean
            b["occ_clean"] += occ
            b["occ_ms"] += occ_ms
            b["occ_in_clean"] += occ_in_clean
            b["occ_in_ms"] += occ_in_ms
            b["occ_embedded"] += occ_embedded
            b["occ_other"] += occ_other
            b["ms_components"] += ms_comp
            b["rho"] += rho

    C_birth = sums["births"] / sums["occ_clean"] if sums["occ_clean"] > 0 else None
    C_component = sums["occ_in_clean"] / sums["occ_clean"] if has_survival and sums["occ_clean"] > 0 else None
    chi = sums["occ_in_clean"] / sums["clean_stars"] if has_survival and sums["clean_stars"] > 0 else None
    V_pair_load = sums["occ_ms"] / sums["occ_clean"] if sums["occ_clean"] > 0 else None
    identity_err = None
    if C_birth is not None and C_component is not None and chi and chi > 0:
        identity_err = abs(C_birth - C_component / chi)

    # Bucket derived quantities.
    bucket_rows = []
    for bkey in sorted(m_bins):
        b = m_bins[bkey]
        occ = b["occ_clean"]
        clean = b["clean_stars"]
        count = b["count"]
        b_C_birth = b["births"] / occ if occ > 0 else None
        b_C_component = b["occ_in_clean"] / occ if has_survival and occ > 0 else None
        b_chi = b["occ_in_clean"] / clean if has_survival and clean > 0 else None
        b_V = b["occ_ms"] / occ if occ > 0 else None
        bucket_rows.append({
            "M_bin": bkey,
            "count": int(count),
            "mean_births": b["births"] / count if count > 0 else 0.0,
            "mean_multistars": b["ms_components"] / count if count > 0 else 0.0,
            "mean_occ_clean": occ / count if count > 0 else 0.0,
            "C_birth": b_C_birth,
            "C_component": b_C_component,
            "chi": b_chi,
            "V_pair_load": b_V,
        })

    return {
        "n_rows": n_rows,
        "has_survival": has_survival,
        "has_logged_formulas": has_logged_formulas,
        "other_col": other_col,
        "sums": dict(sums),
        "C_birth": C_birth,
        "C_component": C_component,
        "chi": chi,
        "V_pair_load": V_pair_load,
        "identity_err": identity_err,
        "birth_identity_matches": birth_identity_matches,
        "birth_identity_total": rows_with_birth_or_clean,
        "ms_prevalence": rows_with_multistar / n_rows if n_rows else 0.0,
        "partition_failures": partition_failures,
        "row_formula_failures": row_formula_failures,
        "max_formula_err": max_formula_err,
        "bucket_rows": bucket_rows,
    }


def dsn_tag(agg: dict[str, Any]) -> str:
    total = agg["birth_identity_total"]
    matches = agg["birth_identity_matches"]
    if total > 0 and matches == total and agg["has_survival"] and agg["partition_failures"] == 0:
        return "[NUM]"
    if total > 0 and matches == total:
        return "[HEUR-legacy]"
    return "[HEUR]"


def fmt(x: Any, nd: int = 6) -> str:
    if x is None:
        return "N/A"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return str(x)


def format_report(path: str, meta: dict[str, Any], agg: dict[str, Any], warnings: list[str]) -> str:
    name = Path(path).stem
    tag = dsn_tag(agg)
    s = agg["sums"]
    lines = [
        f"=== {name} {tag} ===",
        f"  metadata: policy={meta.get('policy') or 'N/A'} N={meta.get('N') or 'N/A'} k={meta.get('k') or 'N/A'} "
        f"k/N={fmt(meta.get('k_over_N'), 4)} T={meta.get('T_requested') or 'N/A'} batch={meta.get('batch') or 'N/A'}",
        f"  window={meta.get('row_filter', 'all')}  rows={agg['n_rows']}"
        + (f" / raw_rows={meta.get('raw_rows')}" if meta.get('raw_rows') is not None and meta.get('raw_rows') != agg['n_rows'] else ""),
        f"  births={s.get('births',0):.0f}  clean_stars={s.get('clean_stars',0):.0f}",
        f"  occ_clean_pairs={s.get('occ_clean',0):.0f}",
    ]
    for w in warnings:
        lines.append(f"  WARNING: {w}")

    bi = agg["birth_identity_total"]
    bm = agg["birth_identity_matches"]
    if bi > 0:
        lines.append(f"  birth_identity: {bm}/{bi} = {bm/bi:.4f}  {'[NUM] PASS' if bm == bi else '[FAIL] MISMATCH'}")

    if agg["has_survival"]:
        if agg["has_logged_formulas"]:
            lines.append(
                f"  survival_partition_failures={agg['partition_failures']}  "
                f"formula_failures={agg['row_formula_failures']}  max_formula_err={agg['max_formula_err']:.2e}"
            )
        else:
            lines.append(f"  survival_partition_failures={agg['partition_failures']}  formula_check=N/A (v16 columns absent)")
    else:
        lines.append("  survival_partition: N/A (legacy log; v15/v16 columns absent)")

    lines.append("")
    lines.append("  TDR-24 factorization:")
    lines.append(f"    C_birth      = {fmt(agg['C_birth'])}  (births / occ_clean)")
    lines.append(f"    C_component  = {fmt(agg['C_component'])}  (occ_in_clean_star / occ_clean)")
    lines.append(f"    chi          = {fmt(agg['chi'], 4)}  (occ_in_clean_star / clean_star_components)")
    lines.append(f"    V_pair_load  = {fmt(agg['V_pair_load'], 6)}  (occ_multistar_pairs / occ_clean_pairs; may exceed 1)")
    if agg["identity_err"] is not None:
        tag = "[ALG OK]" if agg["identity_err"] < 1e-9 else "[CHECK]"
        lines.append(f"    C_birth = C_component/chi: err={agg['identity_err']:.2e} {tag}")

    if agg["C_birth"] is not None:
        lines.append(f"    birth survival: {100*agg['C_birth']:.4f}% of occ_clean candidates become births")

    if agg["has_survival"] and s.get("occ_clean", 0) > 0:
        occ = s["occ_clean"]
        lines.append("")
        lines.append("  occ_clean partition:")
        for label, key in [
            ("clean_star", "occ_in_clean"),
            ("multistar", "occ_in_ms"),
            ("embedded", "occ_embedded"),
            ("other/false", "occ_other"),
        ]:
            val = s.get(key, 0.0)
            lines.append(f"    {label:12s}: {val:10.0f}  ({val/occ:.5f})")

    lines.append("")
    lines.append(f"  ms_prevalence = {agg['ms_prevalence']:.4f} ({100*agg['ms_prevalence']:.1f}% of rows have multistar component)")

    if agg["bucket_rows"]:
        lines.append("")
        lines.append("  M_pre bins:")
        if agg["has_survival"]:
            lines.append(f"  {'M_pre':>8} {'C_birth':>10} {'C_comp':>10} {'chi':>8} {'V_load':>10} {'ms/step':>8} {'count':>7}")
            for b in agg["bucket_rows"]:
                lines.append(
                    f"  {b['M_bin']:>8} {fmt(b['C_birth'],6):>10} {fmt(b['C_component'],6):>10} "
                    f"{fmt(b['chi'],3):>8} {fmt(b['V_pair_load'],4):>10} {b['mean_multistars']:>8.3f} {b['count']:>7}"
                )
        else:
            lines.append(f"  {'M_pre':>8} {'C_birth':>10} {'V_load':>10} {'ms/step':>8} {'count':>7}")
            for b in agg["bucket_rows"]:
                lines.append(
                    f"  {b['M_bin']:>8} {fmt(b['C_birth'],6):>10} {fmt(b['V_pair_load'],4):>10} "
                    f"{b['mean_multistars']:>8.3f} {b['count']:>7}"
                )
    return "\n".join(lines)


def choose_representatives(results: list[tuple[str, dict[str, Any], dict[str, Any]]]) -> list[tuple[str, dict[str, Any], dict[str, Any]]]:
    """Choose one representative per (N,k,T,policy), preferring higher script version and more rows."""
    groups: dict[tuple[Any, Any, Any, Any], tuple[str, dict[str, Any], dict[str, Any]]] = {}
    for path, meta, agg in results:
        if not agg["has_survival"] or agg["C_birth"] is None or agg["C_birth"] <= 0:
            continue
        key = (meta.get("N"), meta.get("k"), meta.get("T_requested"), meta.get("policy"), meta.get("row_filter", "all"))
        current = groups.get(key)
        if current is None:
            groups[key] = (path, meta, agg)
            continue
        _, cmeta, cagg = current
        score_new = (meta.get("version_score") or 0, agg.get("n_rows") or 0)
        score_old = (cmeta.get("version_score") or 0, cagg.get("n_rows") or 0)
        if score_new > score_old:
            groups[key] = (path, meta, agg)
    return list(groups.values())


def fit_power_law(points: list[tuple[float, float]]) -> tuple[float, float] | None:
    # y ~ C N^-alpha. returns (alpha, C)
    pts = [(N, y) for N, y in points if N > 0 and y > 0]
    if len(pts) < 3:
        return None
    xs = [math.log(N) for N, _ in pts]
    ys = [math.log(y) for _, y in pts]
    n = len(pts)
    mx = sum(xs) / n
    my = sum(ys) / n
    den = sum((x - mx) ** 2 for x in xs)
    if den == 0:
        return None
    slope = sum((xs[i] - mx) * (ys[i] - my) for i in range(n)) / den
    alpha = -slope
    C = math.exp(my + alpha * mx)
    return alpha, C


def print_scaling_summary(results: list[tuple[str, dict[str, Any], dict[str, Any]]]) -> None:
    if len(results) < 2:
        return
    print("\n" + "=" * 84)
    print("SCALING SUMMARY — valid survival logs only, one representative per (N,k,T,policy)")
    print("=" * 84)
    reps = choose_representatives(results)
    print(f"representatives used: {len(reps)} / total files: {len(results)}")
    print(f"{'file':>28} {'N':>6} {'k':>5} {'T':>7} {'window':>14} {'C_birth':>10} {'C_comp':>10} {'chi':>8} {'V_load':>8}")
    print("-" * 102)
    for path, meta, agg in sorted(reps, key=lambda x: (x[1].get("N") or 0, x[1].get("k") or 0, x[1].get("T_requested") or 0, x[0])):
        win = str(meta.get('row_filter', 'all'))[:14]
        print(
            f"{Path(path).stem[:28]:>28} {str(meta.get('N')):>6} {str(meta.get('k')):>5} {str(meta.get('T_requested')):>7} {win:>14} "
            f"{fmt(agg['C_birth'],6):>10} {fmt(agg['C_component'],6):>10} {fmt(agg['chi'],4):>8} {fmt(agg['V_pair_load'],4):>8}"
        )

    # Group power-law fits by (k/N rounded, T, policy)
    groups: dict[tuple[Any, Any, Any, Any], list[tuple[float, float]]] = defaultdict(list)
    for _, meta, agg in reps:
        N = meta.get("N")
        kor = meta.get("k_over_N")
        T = meta.get("T_requested")
        pol = meta.get("policy")
        if N and kor is not None and T and agg["C_birth"]:
            groups[(round(float(kor), 4), T, pol, meta.get("row_filter", "all"))].append((float(N), float(agg["C_birth"])))

    for key, pts in sorted(groups.items(), key=lambda x: str(x[0])):
        fit = fit_power_law(pts)
        if fit:
            alpha, C = fit
            Ns = sorted(int(N) for N, _ in pts)
            print(
                f"\n  [HEUR] C_birth(N) fit for k/N={key[0]}, T={key[1]}, policy={key[2]}, window={key[3]}: "
                f"C_birth ≈ {C:.4g} N^(-{alpha:.3f}); N={Ns}"
            )


def print_dsn_patch(results: list[tuple[str, dict[str, Any], dict[str, Any]]]) -> None:
    print("\n" + "=" * 70)
    print("DSN PATCH BLOCK")
    print("=" * 70)
    for path, meta, agg in sorted(results, key=lambda x: x[0]):
        name = Path(path).stem
        tag = dsn_tag(agg)
        bi = agg["birth_identity_total"]
        bm = agg["birth_identity_matches"]
        print(f"\n{tag} Motif log: {name}")
        print(f"  metadata: N={meta.get('N')}, k={meta.get('k')}, T={meta.get('T_requested')}, policy={meta.get('policy')}, window={meta.get('row_filter', 'all')}")
        print(f"  births_step == clean_star_components: {bm}/{bi} rows {'PASS' if bi and bm == bi else 'CHECK'}")
        print(f"  C_birth = {fmt(agg['C_birth'],5)}")
        if agg["has_survival"]:
            print(f"  C_component = {fmt(agg['C_component'],5)}")
            print(f"  chi = {fmt(agg['chi'],3)}")
            print(f"  V_pair_load = {fmt(agg['V_pair_load'],5)}")
            if agg["identity_err"] is not None:
                print(f"  C_birth = C_component/chi identity error = {agg['identity_err']:.2e}")
        else:
            print("  C_component/chi unavailable: legacy motif log lacks v15/v16 survival columns.")
        print(f"  ms_prevalence = {agg['ms_prevalence']:.4f}")

    print("""
[OPEN TDR-24A] Derive C_component from defect-graph combinatorics and multistar locking.
[OPEN TDR-24B] Derive chi, the pair-to-component compression factor.
[OPEN TDR-24C] Determine whether C_birth(N) -> 0 at fixed k/N as N -> infinity.
""")


def main() -> None:
    parser = argparse.ArgumentParser(description="TDR-G motif analysis v3 — TDR-24 factorization with time-window filters")
    parser.add_argument("files", nargs="*", help="CSV files to analyze")
    parser.add_argument("--glob", help="Glob pattern for CSV files")
    parser.add_argument("--dir", help="Directory to scan for CSV files")
    parser.add_argument("--dsn-patch", action="store_true", help="Print DSN patch block")
    parser.add_argument("--no-scaling", action="store_true", help="Suppress scaling summary")
    parser.add_argument("--step-min", type=int, default=None, help="Keep rows with step >= this value.")
    parser.add_argument("--step-max", type=int, default=None, help="Keep rows with step < this value (half-open upper bound).")
    parser.add_argument("--late-frac", type=float, default=None, help="Keep the last fraction of each run, e.g. 0.5 for second half or 0.2 for last 20%%.")
    args = parser.parse_args()

    paths: list[str] = []
    paths.extend(args.files)
    if args.glob:
        paths.extend(glob.glob(args.glob))
    if args.dir:
        paths.extend(glob.glob(os.path.join(args.dir, "*.csv")))

    # Stable unique order.
    paths = sorted(dict.fromkeys(paths))

    if not paths:
        print("No files specified. Examples:")
        print("  python tdr_motif_analysis_v3.py motif_N240_k16_v16.csv")
        print("  python tdr_motif_analysis_v3.py --glob 'motif_*_v16.csv'")
        sys.exit(0)

    results: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    for path in paths:
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping")
            continue
        raw_rows = read_motif_csv(path)
        meta0 = infer_metadata(path, raw_rows)
        rows, meta, filter_warnings = apply_step_filter(
            raw_rows,
            meta0,
            step_min=args.step_min,
            step_max=args.step_max,
            late_frac=args.late_frac,
        )
        available, warnings = check_columns(rows, path)
        warnings = filter_warnings + warnings
        agg = compute_aggregates(rows, available, path)
        print(format_report(path, meta, agg, warnings))
        print()
        results.append((path, meta, agg))

    if not args.no_scaling:
        print_scaling_summary(results)

    if args.dsn_patch:
        print_dsn_patch(results)


if __name__ == "__main__":
    main()
