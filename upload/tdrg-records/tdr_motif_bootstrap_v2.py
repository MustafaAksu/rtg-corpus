#!/usr/bin/env python3
"""
tdr_motif_bootstrap_v2.py
Run-level bootstrap and per-run tail diagnostics for TDR-G v15/v16 motif logs.

Purpose:
  - Compute TDR-24 motif factorization on motif CSV logs:
      C_birth      = sum(births_step) / sum(occ_clean_pairs)
      C_component  = sum(occ_clean_pairs_in_clean_star) / sum(occ_clean_pairs)
      chi          = sum(occ_clean_pairs_in_clean_star) / sum(clean_star_components)
      V_pair_load  = sum(occ_multistar_pairs) / sum(occ_clean_pairs)
      B_per_step   = sum(births_step) / logged_rows
      O_per_step   = sum(occ_clean_pairs) / logged_rows

  - Bootstrap confidence intervals by resampling runs, not rows.
  - Fit power-law exponents y ~= A N^(-alpha) by grouped (policy, k/N, T, window).
  - Diagnose heavy tails via per-run summaries and optional bulk/tail conditioning.

Examples:
  python tdr_motif_bootstrap_v2.py --glob "motif_*_T5000_v16.csv" --step-min 4001 --bootstrap 1000 --dsn-patch
  python tdr_motif_bootstrap_v2.py motif_N720_k48_T5000_v16.csv motif_N960_k64_T5000_v16.csv --step-min 4001 --bootstrap 5000 --per-run-top 20 --tail-threshold 100
  python tdr_motif_bootstrap_v2.py --glob "motif_*_v16.csv" --only-T 5000 --late-frac 0.2 --bootstrap 1000

Notes:
  - Legacy logs without v15/v16 survival columns are tagged [HEUR-legacy].
  - V_pair_load may exceed 1; it is a load ratio, not a probability.
  - Tail conditioning uses final_M from the raw full run when M_post/M_pre is available.
"""

from __future__ import annotations

import argparse
import csv
import glob
import math
import os
import random
import re
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


# ---------------------------------------------------------------------------
# Numeric helpers
# ---------------------------------------------------------------------------

def fnum(x: Any, default: float = 0.0) -> float:
    if x is None:
        return default
    try:
        s = str(x).strip()
        if s == "":
            return default
        return float(s)
    except Exception:
        return default


def inum(x: Any, default: int = 0) -> int:
    return int(round(fnum(x, default)))


def percentile(xs: list[float], q: float) -> float:
    if not xs:
        return 0.0
    ys = sorted(xs)
    if len(ys) == 1:
        return ys[0]
    pos = q * (len(ys) - 1)
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return ys[lo]
    w = pos - lo
    return ys[lo] * (1.0 - w) + ys[hi] * w


def fmt_ci(x: float, ci: tuple[float, float] | None, digits: int = 6) -> str:
    if ci is None:
        return f"{x:.{digits}f}"
    return f"{x:.{digits}f} [{ci[0]:.{digits}f}, {ci[1]:.{digits}f}]"


def ratio_str(x: float | None) -> str:
    return f"{x:.4f}" if x is not None else "unknown"


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class RawRunInfo:
    run_id: str
    raw_rows: int = 0
    first_step: int | None = None
    last_step: int | None = None
    final_M: float = 0.0
    max_M: float = 0.0


@dataclass
class RunAgg:
    run_id: str
    rows: int = 0
    rows_with_multistar: int = 0
    first_step: int | None = None
    last_step: int | None = None

    # raw-run terminal diagnostics
    final_M: float = 0.0
    max_M: float = 0.0

    births: float = 0.0
    clean_stars: float = 0.0
    occ_clean: float = 0.0
    occ_in_clean: float = 0.0
    occ_in_multistar: float = 0.0
    occ_embedded: float = 0.0
    occ_other: float = 0.0
    occ_multistar_pairs: float = 0.0
    multistar_components: float = 0.0
    clean_star_rows: int = 0

    def metrics(self) -> dict[str, float]:
        c_birth = self.births / self.occ_clean if self.occ_clean > 0 else 0.0
        c_comp = self.occ_in_clean / self.occ_clean if self.occ_clean > 0 else 0.0
        chi = self.occ_in_clean / self.clean_stars if self.clean_stars > 0 else 0.0
        v_load = self.occ_multistar_pairs / self.occ_clean if self.occ_clean > 0 else 0.0
        return {
            "rows": float(self.rows),
            "births": self.births,
            "clean_stars": self.clean_stars,
            "occ_clean": self.occ_clean,
            "occ_in_clean": self.occ_in_clean,
            "C_birth": c_birth,
            "C_component": c_comp,
            "chi": chi,
            "V_pair_load": v_load,
            "B_per_step": self.births / self.rows if self.rows > 0 else 0.0,
            "O_per_step": self.occ_clean / self.rows if self.rows > 0 else 0.0,
            "ms_prevalence": self.rows_with_multistar / self.rows if self.rows > 0 else 0.0,
            "final_M": self.final_M,
            "max_M": self.max_M,
        }


@dataclass
class FileAgg:
    path: str
    name: str
    policy: str = "unknown"
    N: int | None = None
    k: int | None = None
    T: int | None = None
    batch: int | None = None
    k_over_N: float | None = None
    window: str = "all"
    raw_rows: int = 0
    rows: int = 0
    run_aggs: list[RunAgg] = field(default_factory=list)
    has_survival: bool = False
    has_partition: bool = False
    has_formula_cols: bool = False
    birth_identity_total: int = 0
    birth_identity_matches: int = 0
    survival_partition_failures: int = 0
    formula_failures: int = 0
    max_formula_err: float = 0.0
    metrics: dict[str, float] = field(default_factory=dict)
    ci: dict[str, tuple[float, float]] = field(default_factory=dict)


SURVIVAL_COLS = {"occ_clean_pairs_in_clean_star"}
PARTITION_COLS = {
    "occ_clean_pairs_in_clean_star",
    "occ_clean_pairs_in_multistar",
    "occ_clean_pairs_embedded",
    "occ_clean_pairs_other",
}
FORMULA_COLS = {
    "occ_clean_survival_rate",
    "occ_clean_birth_survival_rate",
    "occ_clean_component_compression",
}


# ---------------------------------------------------------------------------
# Metadata and loading
# ---------------------------------------------------------------------------

def infer_from_filename(path: str) -> dict[str, Any]:
    stem = Path(path).stem
    out: dict[str, Any] = {}
    m = re.search(r"N(\d+)", stem)
    if m:
        out["N"] = int(m.group(1))
    m = re.search(r"k(\d+)", stem)
    if m:
        out["k"] = int(m.group(1))
    m = re.search(r"T(\d+)", stem)
    if m:
        out["T"] = int(m.group(1))
    m = re.search(r"b(\d+)", stem)
    if m:
        # only use if no explicit batch column later
        out["batch"] = int(m.group(1))
    return out


def update_meta_from_row(meta: dict[str, Any], row: dict[str, str]) -> None:
    for key in ["N", "k", "batch"]:
        if key in row and str(row[key]).strip() != "":
            meta[key] = inum(row[key])
    # motif logs use T_requested; some analysis logs may use T.
    if "T" in row and str(row["T"]).strip() != "":
        meta["T"] = inum(row["T"])
    if "T_requested" in row and str(row["T_requested"]).strip() != "":
        meta["T"] = inum(row["T_requested"])
    for key in ["policy", "multistar_policy"]:
        if key in row and str(row[key]).strip() != "":
            meta["policy"] = str(row[key]).strip()
    if "k_over_N" in row and str(row["k_over_N"]).strip() != "":
        meta["k_over_N"] = fnum(row["k_over_N"])


def read_rows(path: str) -> tuple[list[dict[str, str]], set[str]]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [
            {k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
            for row in reader
        ]
    cols = set(rows[0].keys()) if rows else set()
    return rows, cols


def row_run_id(row: dict[str, str], run_col: str) -> str:
    return str(row.get(run_col, "0"))


def infer_run_col(cols: set[str]) -> str:
    if "run_id" in cols:
        return "run_id"
    if "run" in cols:
        return "run"
    return "__single_run__"


def compute_raw_run_info(rows: list[dict[str, str]], cols: set[str]) -> dict[str, RawRunInfo]:
    run_col = infer_run_col(cols)
    info: dict[str, RawRunInfo] = {}
    for row in rows:
        rid = row_run_id(row, run_col)
        ri = info.setdefault(rid, RawRunInfo(run_id=rid))
        step = inum(row.get("step", ri.raw_rows + 1))
        m_pre = fnum(row.get("M_pre"))
        m_post = fnum(row.get("M_post", m_pre))
        m_val = m_post if "M_post" in row and str(row.get("M_post", "")).strip() != "" else m_pre
        ri.raw_rows += 1
        ri.max_M = max(ri.max_M, m_pre, m_post, m_val)
        if ri.first_step is None or step < ri.first_step:
            ri.first_step = step
        if ri.last_step is None or step >= ri.last_step:
            ri.last_step = step
            ri.final_M = m_val
    return info


def filter_rows(
    rows: list[dict[str, str]],
    *,
    step_min: int | None,
    step_max: int | None,
    late_frac: float | None,
) -> tuple[list[dict[str, str]], str]:
    if not rows:
        return rows, "all"
    if "step" not in rows[0]:
        return rows, "all(no_step_col)"

    filtered = rows
    label_parts: list[str] = []

    if late_frac is not None:
        cols = set(rows[0].keys())
        run_col = infer_run_col(cols)
        if run_col == "__single_run__":
            max_step = max(inum(r.get("step")) for r in rows)
            min_step = min(inum(r.get("step")) for r in rows)
            span = max_step - min_step + 1
            keep = max(1, int(math.ceil(span * late_frac)))
            threshold = max_step - keep + 1
            filtered = [r for r in filtered if inum(r.get("step")) >= threshold]
            label_parts.append(f"late_frac={late_frac}, step>={threshold}")
        else:
            max_by_run: dict[str, int] = {}
            min_by_run: dict[str, int] = {}
            for r in rows:
                rid = row_run_id(r, run_col)
                st = inum(r.get("step"))
                max_by_run[rid] = max(max_by_run.get(rid, st), st)
                min_by_run[rid] = min(min_by_run.get(rid, st), st)
            thresholds: dict[str, int] = {}
            for rid, mx in max_by_run.items():
                mn = min_by_run[rid]
                span = mx - mn + 1
                keep = max(1, int(math.ceil(span * late_frac)))
                thresholds[rid] = mx - keep + 1
            filtered = [r for r in filtered if inum(r.get("step")) >= thresholds[row_run_id(r, run_col)]]
            label_parts.append(f"late_frac={late_frac}")

    if step_min is not None:
        filtered = [r for r in filtered if inum(r.get("step")) >= step_min]
        label_parts.append(f"step>={step_min}")
    if step_max is not None:
        filtered = [r for r in filtered if inum(r.get("step")) < step_max]
        label_parts.append(f"step<{step_max}")

    return filtered, ", ".join(label_parts) if label_parts else "all"


# ---------------------------------------------------------------------------
# Aggregation and bootstrap
# ---------------------------------------------------------------------------

def compute_metrics_from_runs(runs: list[RunAgg]) -> dict[str, float]:
    rows = sum(r.rows for r in runs)
    births = sum(r.births for r in runs)
    clean = sum(r.clean_stars for r in runs)
    occ = sum(r.occ_clean for r in runs)
    oic = sum(r.occ_in_clean for r in runs)
    oims = sum(r.occ_in_multistar for r in runs)
    oe = sum(r.occ_embedded for r in runs)
    oo = sum(r.occ_other for r in runs)
    oms = sum(r.occ_multistar_pairs for r in runs)
    rows_ms = sum(r.rows_with_multistar for r in runs)
    ms_components = sum(r.multistar_components for r in runs)

    C_birth = births / occ if occ > 0 else 0.0
    C_comp = oic / occ if occ > 0 else 0.0
    chi = oic / clean if clean > 0 else 0.0
    V_load = oms / occ if occ > 0 else 0.0
    identity_err = abs(C_birth - (C_comp / chi)) if chi > 0 else 0.0

    final_vals = [r.final_M for r in runs if r.final_M is not None]
    max_vals = [r.max_M for r in runs if r.max_M is not None]

    return {
        "n_runs": float(len(runs)),
        "rows": float(rows),
        "births": births,
        "clean_stars": clean,
        "occ_clean": occ,
        "occ_in_clean": oic,
        "occ_in_multistar": oims,
        "occ_embedded": oe,
        "occ_other": oo,
        "occ_multistar_pairs": oms,
        "multistar_components": ms_components,
        "C_birth": C_birth,
        "C_component": C_comp,
        "chi": chi,
        "V_pair_load": V_load,
        "identity_err": identity_err,
        "ms_prevalence": rows_ms / rows if rows > 0 else 0.0,
        "B_per_step": births / rows if rows > 0 else 0.0,
        "O_per_step": occ / rows if rows > 0 else 0.0,
        "final_M_mean": sum(final_vals) / len(final_vals) if final_vals else 0.0,
        "final_M_max": max(final_vals) if final_vals else 0.0,
        "max_M_mean": sum(max_vals) / len(max_vals) if max_vals else 0.0,
        "max_M_max": max(max_vals) if max_vals else 0.0,
    }


def analyze_file(
    path: str,
    *,
    step_min: int | None,
    step_max: int | None,
    late_frac: float | None,
    bootstrap: int,
    seed: int,
) -> FileAgg:
    raw_rows, cols = read_rows(path)
    filtered, window = filter_rows(raw_rows, step_min=step_min, step_max=step_max, late_frac=late_frac)

    meta = infer_from_filename(path)
    if raw_rows:
        update_meta_from_row(meta, raw_rows[0])
    if "k_over_N" not in meta and "N" in meta and "k" in meta and meta.get("N"):
        meta["k_over_N"] = meta["k"] / meta["N"]

    agg = FileAgg(
        path=path,
        name=Path(path).stem,
        policy=str(meta.get("policy", "unknown")),
        N=meta.get("N"),
        k=meta.get("k"),
        T=meta.get("T"),
        batch=meta.get("batch"),
        k_over_N=meta.get("k_over_N"),
        window=window,
        raw_rows=len(raw_rows),
        rows=len(filtered),
        has_survival=bool(SURVIVAL_COLS <= cols),
        has_partition=bool(PARTITION_COLS <= cols),
        has_formula_cols=bool(FORMULA_COLS <= cols),
    )

    raw_info = compute_raw_run_info(raw_rows, cols)
    run_col = infer_run_col(cols)
    by_run: dict[str, RunAgg] = {}

    for row in filtered:
        rid = row_run_id(row, run_col)
        if rid not in by_run:
            rinfo = raw_info.get(rid, RawRunInfo(run_id=rid))
            by_run[rid] = RunAgg(
                run_id=rid,
                final_M=rinfo.final_M,
                max_M=rinfo.max_M,
            )
        ragg = by_run[rid]

        step = inum(row.get("step", ragg.rows + 1))
        b = fnum(row.get("births_step"))
        cs = fnum(row.get("clean_star_components"))
        occ = fnum(row.get("occ_clean_pairs"))
        oic = fnum(row.get("occ_clean_pairs_in_clean_star"))
        oims = fnum(row.get("occ_clean_pairs_in_multistar"))
        oe = fnum(row.get("occ_clean_pairs_embedded"))
        oo = fnum(row.get("occ_clean_pairs_other"))
        oms = fnum(row.get("occ_multistar_pairs"))
        ms_components = fnum(row.get("multistar_components"))

        ragg.rows += 1
        ragg.rows_with_multistar += int(ms_components > 0)
        ragg.multistar_components += ms_components
        ragg.births += b
        ragg.clean_stars += cs
        ragg.occ_clean += occ
        ragg.occ_in_clean += oic
        ragg.occ_in_multistar += oims
        ragg.occ_embedded += oe
        ragg.occ_other += oo
        ragg.occ_multistar_pairs += oms
        ragg.clean_star_rows += int(cs > 0)
        if ragg.first_step is None or step < ragg.first_step:
            ragg.first_step = step
        if ragg.last_step is None or step > ragg.last_step:
            ragg.last_step = step

        if b > 0 or cs > 0:
            agg.birth_identity_total += 1
            if abs(b - cs) < 0.5:
                agg.birth_identity_matches += 1

        if agg.has_partition:
            if abs(occ - (oic + oims + oe + oo)) > 0.5:
                agg.survival_partition_failures += 1

        if agg.has_formula_cols:
            logged_surv = fnum(row.get("occ_clean_survival_rate"))
            logged_birth = fnum(row.get("occ_clean_birth_survival_rate"))
            logged_comp = fnum(row.get("occ_clean_component_compression"))
            calc_surv = oic / occ if occ > 0 else 0.0
            calc_birth = b / occ if occ > 0 else 0.0
            calc_comp = oic / cs if cs > 0 else 0.0
            me = max(abs(logged_surv - calc_surv), abs(logged_birth - calc_birth), abs(logged_comp - calc_comp))
            agg.max_formula_err = max(agg.max_formula_err, me)
            if me > 1e-9:
                agg.formula_failures += 1

    agg.run_aggs = list(by_run.values())
    agg.metrics = compute_metrics_from_runs(agg.run_aggs)

    if bootstrap > 0 and len(agg.run_aggs) >= 2:
        rng = random.Random(seed)
        samples: dict[str, list[float]] = defaultdict(list)
        n = len(agg.run_aggs)
        keys = [
            "C_birth",
            "C_component",
            "chi",
            "V_pair_load",
            "B_per_step",
            "O_per_step",
            "final_M_mean",
            "final_M_max",
        ]
        for _ in range(bootstrap):
            picked = [agg.run_aggs[rng.randrange(n)] for _ in range(n)]
            m = compute_metrics_from_runs(picked)
            for key in keys:
                samples[key].append(m[key])
        for key, vals in samples.items():
            agg.ci[key] = (percentile(vals, 0.025), percentile(vals, 0.975))

    return agg


# ---------------------------------------------------------------------------
# Scaling fits
# ---------------------------------------------------------------------------

def fit_power(files: list[FileAgg], metric: str) -> tuple[float, float] | None:
    pts = []
    for a in files:
        if a.N is not None:
            y = a.metrics.get(metric, 0.0)
            if y > 0 and a.N > 0:
                pts.append((float(a.N), y))
    if len(pts) < 3:
        return None
    xs = [math.log(p[0]) for p in pts]
    ys = [math.log(p[1]) for p in pts]
    mx = statistics.mean(xs)
    my = statistics.mean(ys)
    den = sum((x - mx) ** 2 for x in xs)
    if den <= 0:
        return None
    slope = sum((xs[i] - mx) * (ys[i] - my) for i in range(len(xs))) / den
    intercept = my - slope * mx
    return math.exp(intercept), -slope


def bootstrap_exponent(files: list[FileAgg], metric: str, n_boot: int, seed: int) -> tuple[float, float] | None:
    if n_boot <= 0 or len(files) < 3:
        return None
    if any(len(f.run_aggs) < 2 for f in files):
        return None
    rng = random.Random(seed)
    alphas: list[float] = []
    for _ in range(n_boot):
        boot_files: list[FileAgg] = []
        for f in files:
            n = len(f.run_aggs)
            picked = [f.run_aggs[rng.randrange(n)] for _ in range(n)]
            fake = FileAgg(path=f.path, name=f.name, N=f.N, k=f.k, T=f.T, policy=f.policy, window=f.window)
            fake.run_aggs = picked
            fake.metrics = compute_metrics_from_runs(picked)
            boot_files.append(fake)
        fit = fit_power(boot_files, metric)
        if fit is not None:
            _, alpha = fit
            alphas.append(alpha)
    if not alphas:
        return None
    return percentile(alphas, 0.025), percentile(alphas, 0.975)


def scaling_groups(results: list[FileAgg]) -> dict[tuple[Any, ...], list[FileAgg]]:
    groups: dict[tuple[Any, ...], list[FileAgg]] = defaultdict(list)
    for a in results:
        if not a.has_survival or a.N is None or a.k is None:
            continue
        ratio = round((a.k_over_N if a.k_over_N is not None else a.k / a.N), 6)
        key = (a.policy, ratio, a.T, a.window)
        groups[key].append(a)
    out: dict[tuple[Any, ...], list[FileAgg]] = {}
    for key, vals in groups.items():
        byN: dict[int, FileAgg] = {}
        for a in sorted(vals, key=lambda x: x.name):
            byN[a.N or -1] = a
        out[key] = sorted(byN.values(), key=lambda x: x.N or 0)
    return out


# ---------------------------------------------------------------------------
# Conditional and per-run reporting
# ---------------------------------------------------------------------------

def sort_run_key(run: RunAgg, key: str) -> float:
    m = run.metrics()
    if key in m:
        return m[key]
    if key == "late_births":
        return run.births
    if key == "final_M":
        return run.final_M
    if key == "max_M":
        return run.max_M
    return run.births


def format_run_table(a: FileAgg, *, top_n: int, sort_key: str) -> str:
    if top_n <= 0:
        return ""
    runs = sorted(a.run_aggs, key=lambda r: sort_run_key(r, sort_key), reverse=True)[:top_n]
    lines = []
    lines.append(f"  per-run top {len(runs)} by {sort_key}:")
    lines.append(f"  {'run_id':>28} {'final_M':>8} {'max_M':>8} {'rows':>6} {'births':>8} {'O':>10} {'C_birth':>10} {'C_comp':>10} {'chi':>9} {'V_load':>9} {'B/step':>9}")
    for r in runs:
        m = r.metrics()
        lines.append(
            f"  {r.run_id[-28:]:>28} {r.final_M:>8.1f} {r.max_M:>8.1f} {r.rows:>6} "
            f"{r.births:>8.0f} {r.occ_clean:>10.0f} {m['C_birth']:>10.6f} "
            f"{m['C_component']:>10.6f} {m['chi']:>9.3f} {m['V_pair_load']:>9.3f} {m['B_per_step']:>9.5f}"
        )
    return "\n".join(lines)


def format_tail_split(a: FileAgg, threshold: int | None) -> str:
    if threshold is None:
        return ""
    bulk = [r for r in a.run_aggs if r.final_M <= threshold]
    tail = [r for r in a.run_aggs if r.final_M > threshold]
    allm = a.metrics
    lines = []
    lines.append(f"  bulk/tail split by final_M > {threshold}:")
    lines.append(f"  {'group':>8} {'runs':>5} {'birth_share':>11} {'C_birth':>10} {'C_comp':>10} {'chi':>9} {'B/step':>9} {'O/step':>9} {'final_M_mean':>12} {'final_M_max':>11}")
    total_births = allm.get("births", 0.0)
    for label, subset in [("bulk", bulk), ("tail", tail)]:
        m = compute_metrics_from_runs(subset) if subset else {}
        bshare = (m.get("births", 0.0) / total_births) if total_births > 0 else 0.0
        lines.append(
            f"  {label:>8} {len(subset):>5} {bshare:>11.4f} "
            f"{m.get('C_birth',0.0):>10.6f} {m.get('C_component',0.0):>10.6f} {m.get('chi',0.0):>9.3f} "
            f"{m.get('B_per_step',0.0):>9.5f} {m.get('O_per_step',0.0):>9.3f} "
            f"{m.get('final_M_mean',0.0):>12.2f} {m.get('final_M_max',0.0):>11.1f}"
        )
    return "\n".join(lines)


def export_per_run_csv(results: list[FileAgg], path: str) -> None:
    fields = [
        "file", "policy", "N", "k", "k_over_N", "T", "window", "run_id",
        "final_M", "max_M", "rows", "births", "clean_stars", "occ_clean",
        "occ_in_clean", "C_birth", "C_component", "chi", "V_pair_load",
        "B_per_step", "O_per_step", "ms_prevalence", "multistar_components",
        "first_step", "last_step",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for a in results:
            for r in a.run_aggs:
                m = r.metrics()
                writer.writerow({
                    "file": a.name,
                    "policy": a.policy,
                    "N": a.N,
                    "k": a.k,
                    "k_over_N": a.k_over_N,
                    "T": a.T,
                    "window": a.window,
                    "run_id": r.run_id,
                    "final_M": r.final_M,
                    "max_M": r.max_M,
                    "rows": r.rows,
                    "births": r.births,
                    "clean_stars": r.clean_stars,
                    "occ_clean": r.occ_clean,
                    "occ_in_clean": r.occ_in_clean,
                    "C_birth": m["C_birth"],
                    "C_component": m["C_component"],
                    "chi": m["chi"],
                    "V_pair_load": m["V_pair_load"],
                    "B_per_step": m["B_per_step"],
                    "O_per_step": m["O_per_step"],
                    "ms_prevalence": m["ms_prevalence"],
                    "multistar_components": r.multistar_components,
                    "first_step": r.first_step,
                    "last_step": r.last_step,
                })


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def dsn_tag(a: FileAgg) -> str:
    if not a.has_survival:
        return "[HEUR-legacy]"
    if (
        a.birth_identity_total > 0
        and a.birth_identity_matches == a.birth_identity_total
        and a.survival_partition_failures == 0
    ):
        return "[NUM]"
    return "[HEUR]"


def report_file(a: FileAgg, *, per_run_top: int = 0, per_run_sort: str = "births", tail_threshold: int | None = None) -> str:
    m = a.metrics
    ci = a.ci
    lines: list[str] = []
    lines.append(f"=== {a.name} {dsn_tag(a)} ===")
    lines.append(f"  metadata: policy={a.policy} N={a.N} k={a.k} k/N={ratio_str(a.k_over_N)} T={a.T} batch={a.batch}")
    lines.append(f"  window={a.window}  rows={a.rows} / raw_rows={a.raw_rows}  runs={len(a.run_aggs)}")
    lines.append(f"  births={m.get('births',0):.0f}  clean_stars={m.get('clean_stars',0):.0f}  occ_clean_pairs={m.get('occ_clean',0):.0f}")
    if a.birth_identity_total:
        frac = a.birth_identity_matches / a.birth_identity_total
        lines.append(f"  birth_identity: {a.birth_identity_matches}/{a.birth_identity_total} = {frac:.4f}  {'[NUM] PASS' if frac == 1.0 else '[FAIL]'}")
    lines.append(f"  survival_partition_failures={a.survival_partition_failures}  formula_failures={a.formula_failures}  max_formula_err={a.max_formula_err:.2e}")
    lines.append("")
    lines.append("  TDR-24 factorization:")
    lines.append(f"    C_birth      = {fmt_ci(m.get('C_birth',0), ci.get('C_birth'))}  (births / occ_clean)")
    if a.has_survival:
        lines.append(f"    C_component  = {fmt_ci(m.get('C_component',0), ci.get('C_component'))}  (occ_in_clean_star / occ_clean)")
        lines.append(f"    chi          = {fmt_ci(m.get('chi',0), ci.get('chi'), digits=4)}  (occ_in_clean_star / clean_star_components)")
        lines.append(f"    V_pair_load  = {fmt_ci(m.get('V_pair_load',0), ci.get('V_pair_load'))}  (occ_multistar_pairs / occ_clean_pairs; may exceed 1)")
        lines.append(f"    B_per_step   = {fmt_ci(m.get('B_per_step',0), ci.get('B_per_step'))}")
        lines.append(f"    O_per_step   = {fmt_ci(m.get('O_per_step',0), ci.get('O_per_step'))}")
        lines.append(f"    final_M_mean = {fmt_ci(m.get('final_M_mean',0), ci.get('final_M_mean'))}; final_M_max={m.get('final_M_max',0):.1f}")
        lines.append(f"    C_birth = C_component/chi: err={m.get('identity_err',0):.2e} [ALG OK]")
    else:
        lines.append("    C_component, chi unavailable: legacy log has no survival columns")
    lines.append(f"  ms_prevalence = {m.get('ms_prevalence',0):.4f}")

    tail_txt = format_tail_split(a, tail_threshold)
    if tail_txt:
        lines.append("")
        lines.append(tail_txt)

    run_txt = format_run_table(a, top_n=per_run_top, sort_key=per_run_sort)
    if run_txt:
        lines.append("")
        lines.append(run_txt)

    return "\n".join(lines)


def print_scaling(results: list[FileAgg], bootstrap: int, seed: int) -> None:
    groups = scaling_groups(results)
    if not groups:
        return
    print("\n" + "=" * 92)
    print("SCALING SUMMARY — valid survival logs only")
    print("=" * 92)
    for key, vals in sorted(groups.items(), key=lambda kv: str(kv[0])):
        policy, ratio, T, window = key
        if len(vals) < 2:
            continue
        print(f"\nGroup: policy={policy}, k/N={ratio:.6f}, T={T}, window={window}")
        print(f"{'file':>38} {'N':>6} {'C_birth':>11} {'C_comp':>11} {'chi':>10} {'V_load':>10} {'B/step':>10} {'O/step':>10} {'final_M':>9}")
        print("-" * 112)
        for a in vals:
            m = a.metrics
            print(
                f"{a.name[:38]:>38} {a.N:>6} {m['C_birth']:>11.6g} {m['C_component']:>11.6g} "
                f"{m['chi']:>10.4g} {m['V_pair_load']:>10.4g} {m['B_per_step']:>10.6g} "
                f"{m['O_per_step']:>10.6g} {m['final_M_mean']:>9.2f}"
            )
        if len(vals) >= 3:
            for metric in ["C_birth", "C_component", "chi", "B_per_step", "O_per_step", "final_M_mean"]:
                fit = fit_power(vals, metric)
                if fit is None:
                    continue
                A, alpha = fit
                ci = bootstrap_exponent(vals, metric, bootstrap, seed + abs(hash((key, metric))) % 1000000)
                ci_txt = f" [{ci[0]:.3f}, {ci[1]:.3f}]" if ci else ""
                print(f"  [HEUR] {metric}(N) ≈ {A:.4g} N^(-alpha), alpha={alpha:.3f}{ci_txt}")


def print_dsn_patch(results: list[FileAgg]) -> None:
    print("\n" + "=" * 70)
    print("DSN PATCH BLOCK")
    print("=" * 70)
    for a in sorted(results, key=lambda x: (x.T or 0, x.N or 0, x.name, x.window)):
        m = a.metrics
        print(f"""
{dsn_tag(a)} Motif log: {a.name}
  metadata: N={a.N}, k={a.k}, T={a.T}, policy={a.policy}, window={a.window}
  births_step == clean_star_components: {a.birth_identity_matches}/{a.birth_identity_total} rows {'PASS' if a.birth_identity_total and a.birth_identity_matches == a.birth_identity_total else ''}
  C_birth = {m.get('C_birth',0):.6g}
  C_component = {m.get('C_component',0):.6g}
  chi = {m.get('chi',0):.4g}
  V_pair_load = {m.get('V_pair_load',0):.6g}
  B_per_step = {m.get('B_per_step',0):.6g}
  O_per_step = {m.get('O_per_step',0):.6g}
  final_M_mean = {m.get('final_M_mean',0):.3f}; final_M_max = {m.get('final_M_max',0):.1f}
  C_birth = C_component/chi identity error = {m.get('identity_err',0):.2e}
  ms_prevalence = {m.get('ms_prevalence',0):.4f}""")
    print("""
[OPEN TDR-24A] Derive C_component from defect-graph combinatorics and multistar locking.
[OPEN TDR-24B] Derive chi, the pair-to-component compression factor.
[OPEN TDR-24C] Connect B_per_step = O_per_step * C_birth to rN_late and thermodynamic crystallization.
[OPEN TDR-25] Separate bulk crystallization from rare high-growth tails using per-run late-window diagnostics.
""")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(description="Run-level bootstrap and tail diagnostics for TDR-G motif factorization logs.")
    p.add_argument("files", nargs="*", help="CSV files")
    p.add_argument("--glob", help="Glob pattern for CSV files")
    p.add_argument("--dir", help="Directory to scan for CSV files")
    p.add_argument("--step-min", type=int, default=None, help="Keep rows with step >= step-min")
    p.add_argument("--step-max", type=int, default=None, help="Keep rows with step < step-max")
    p.add_argument("--late-frac", type=float, default=None, help="Keep last fraction of each run, e.g. 0.2")
    p.add_argument("--only-T", type=int, default=None, help="Only include files with metadata T equal to this value")
    p.add_argument("--only-policy", default=None, help="Only include this policy")
    p.add_argument("--bootstrap", type=int, default=0, help="Run-level bootstrap replicates")
    p.add_argument("--seed", type=int, default=12345, help="Bootstrap seed")
    p.add_argument("--dsn-patch", action="store_true", help="Print DSN patch block")
    p.add_argument("--per-run-top", type=int, default=0, help="Print top N per-run diagnostics for each file")
    p.add_argument(
        "--per-run-sort",
        default="births",
        choices=["births", "late_births", "final_M", "max_M", "C_birth", "C_component", "chi", "B_per_step", "O_per_step", "V_pair_load"],
        help="Sort key for --per-run-top",
    )
    p.add_argument("--tail-threshold", type=int, default=None, help="Print bulk/tail split using final_M > threshold")
    p.add_argument("--per-run-csv", default=None, help="Export combined per-run summary CSV")
    args = p.parse_args()

    paths = list(args.files)
    if args.glob:
        paths.extend(glob.glob(args.glob))
    if args.dir:
        paths.extend(glob.glob(os.path.join(args.dir, "*.csv")))
    paths = sorted(set(paths))

    if not paths:
        print("No files specified. Use files, --glob, or --dir.")
        sys.exit(0)

    results: list[FileAgg] = []
    for i, path in enumerate(paths):
        if not os.path.exists(path):
            print(f"WARNING: missing {path}")
            continue
        a = analyze_file(
            path,
            step_min=args.step_min,
            step_max=args.step_max,
            late_frac=args.late_frac,
            bootstrap=args.bootstrap,
            seed=args.seed + i * 1009,
        )
        if args.only_T is not None and a.T != args.only_T:
            continue
        if args.only_policy is not None and a.policy != args.only_policy:
            continue
        print(report_file(a, per_run_top=args.per_run_top, per_run_sort=args.per_run_sort, tail_threshold=args.tail_threshold))
        print()
        results.append(a)

    print_scaling(results, bootstrap=args.bootstrap, seed=args.seed)
    if args.dsn_patch:
        print_dsn_patch(results)
    if args.per_run_csv:
        export_per_run_csv(results, args.per_run_csv)
        print(f"\n[ALG] wrote per-run summary CSV: {args.per_run_csv}")


if __name__ == "__main__":
    main()
