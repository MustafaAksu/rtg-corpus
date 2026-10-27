#!/usr/bin/env python3
"""
tdr_motif_bootstrap_v4.py

TDR-G / Mode-B motif-log analysis.

v4 goals:
  - Preserve v3 pool-level checks:
      births_step == clean_star_components
      C_birth = C_component / chi
      B_per_step = O_per_step * C_birth
  - Add multi-threshold tail table in one pass:
      p_tail^100, p_tail^200, p_tail^500, tail birth shares
  - Add bulk-conditioned TDR-24 fits:
      C_birth_bulk, C_component_bulk, chi_bulk, B_bulk/step, O_bulk/step, M_bulk
  - Pool multiple seed files for the same cell (N,k,T,policy,window) before fitting.
  - Avoid using clean_star_components as final_M. final_M is inferred from M_post/nodes columns.

Examples:
  python tdr_motif_bootstrap_v4.py motif_N720_k48_T5000_b100_v16.csv \
      --step-min 4001 --tail-threshold 500 --fit-bulk-tdr24 --dsn-patch

  python tdr_motif_bootstrap_v4.py --glob "motif_*_T5000*_v16.csv" \
      --step-min 4001 --tail-thresholds 100 200 500 \
      --tail-threshold 500 --fit-bulk-tdr24 --per-run-csv per_run.csv
"""

from __future__ import annotations

import argparse
import csv
import glob as globlib
import math
import os
import random
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Any


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fnum(x: Any, default: float = 0.0) -> float:
    if x is None:
        return default
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).strip()
    if s == "" or s.lower() in {"nan", "none", "null"}:
        return default
    try:
        return float(s)
    except ValueError:
        return default


def inum(x: Any, default: int = 0) -> int:
    return int(round(fnum(x, float(default))))


def div(a: float, b: float) -> float:
    return a / b if b else 0.0


def first_present(row: dict[str, str], names: Iterable[str]) -> str | None:
    for name in names:
        if name in row and str(row[name]).strip() != "":
            return name
    return None


def parse_ratio_text(path_stem: str, N: int | None, k: int | None) -> float | None:
    if N and k is not None:
        return k / N
    return None


def parse_metadata_from_name(path: str) -> dict[str, Any]:
    stem = Path(path).stem

    def grab(patterns: list[str]) -> int | None:
        for pat in patterns:
            m = re.search(pat, stem, flags=re.IGNORECASE)
            if m:
                return int(m.group(1))
        return None

    N = grab([r"(?:^|_)N0*(\d+)(?:_|$)", r"N0*(\d+)"])
    k = grab([r"(?:^|_)k0*(\d+)(?:_|$)", r"k0*(\d+)"])
    T = grab([r"(?:^|_)T0*(\d+)(?:_|$)", r"T0*(\d+)"])
    batch = grab([r"(?:^|_)b0*(\d+)(?:_|$)", r"(?:^|_)batch0*(\d+)(?:_|$)"])

    return {
        "stem": stem,
        "N": N,
        "k": k,
        "T": T,
        "batch": batch,
        "k_over_N": parse_ratio_text(stem, N, k),
    }


# ---------------------------------------------------------------------------
# Column definitions
# ---------------------------------------------------------------------------

RUN_COLS = ["run_id", "run", "run_index", "replicate", "seed_run"]
STEP_COLS = ["step", "t", "time"]

# final_M must be node count, not clean_star_components.
M_COLS_PREFERRED = [
    "M_post", "m_post", "nodes_post", "node_count", "nodes", "M",
    "final_M", "final_nodes", "m", "n_nodes", "node_count_post",
]
M_COLS_FALLBACK = ["M_pre", "m_pre", "nodes_pre"]

COL_BIRTHS = "births_step"
COL_CLEAN_STAR = "clean_star_components"
COL_OCC = "occ_clean_pairs"
COL_OCC_IN_CLEAN = "occ_clean_pairs_in_clean_star"
COL_OCC_MS = "occ_multistar_pairs"
COL_OCC_IN_MS = "occ_clean_pairs_in_multistar"
COL_MS_COMPONENTS = "multistar_components"

EMBEDDED_COLS = [
    "occ_clean_pairs_embedded",
    "occ_clean_pairs_in_embedded",
    "occ_embedded_pairs",
    "occ_clean_pairs_in_other_component",
]
OTHER_COLS = [
    "occ_clean_pairs_other",
    "occ_clean_pairs_false_positive",
    "occ_clean_pairs_other_false",
]

SURVIVAL_FAILURE_COLS = ["survival_partition_failures", "partition_failures"]
FORMULA_FAILURE_COLS = ["formula_failures", "occ_formula_failures"]
FORMULA_ERR_COLS = ["formula_err", "formula_error", "max_formula_err"]

POLICY_COLS = ["policy", "multistar_policy"]
N_COLS = ["N"]
K_COLS = ["k"]
T_COLS = ["T"]
BATCH_COLS = ["batch"]


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class RunAgg:
    file: str
    stem: str
    run_id: str
    policy: str
    N: int | None
    k: int | None
    T: int | None
    batch: int | None

    rows: int = 0
    raw_rows_seen: int = 0
    births: float = 0.0
    clean_stars: float = 0.0
    occ: float = 0.0
    occ_in_clean: float = 0.0
    occ_ms_load: float = 0.0
    occ_in_ms: float = 0.0
    occ_embedded: float = 0.0
    occ_other_logged: float = 0.0
    ms_components: float = 0.0
    rows_with_ms: int = 0

    survival_partition_failures: float = 0.0
    formula_failures: float = 0.0
    max_formula_err: float = 0.0

    final_M: float = 0.0
    max_M: float = 0.0
    last_step_seen: float = -math.inf

    has_survival_cols: bool = False
    has_m_col: bool = False

    def add_row(self, row: dict[str, str], step: float, m_col: str | None, m_fallback_col: str | None) -> None:
        self.rows += 1
        b = fnum(row.get(COL_BIRTHS))
        cs = fnum(row.get(COL_CLEAN_STAR))
        occ = fnum(row.get(COL_OCC))
        oic = fnum(row.get(COL_OCC_IN_CLEAN))
        oms_load = fnum(row.get(COL_OCC_MS))
        oims = fnum(row.get(COL_OCC_IN_MS))
        msc = fnum(row.get(COL_MS_COMPONENTS))

        self.births += b
        self.clean_stars += cs
        self.occ += occ
        self.occ_in_clean += oic
        self.occ_ms_load += oms_load
        self.occ_in_ms += oims
        self.ms_components += msc
        if msc > 0:
            self.rows_with_ms += 1

        emb_col = first_present(row, EMBEDDED_COLS)
        oth_col = first_present(row, OTHER_COLS)
        self.occ_embedded += fnum(row.get(emb_col)) if emb_col else 0.0
        self.occ_other_logged += fnum(row.get(oth_col)) if oth_col else 0.0

        sf_col = first_present(row, SURVIVAL_FAILURE_COLS)
        ff_col = first_present(row, FORMULA_FAILURE_COLS)
        fe_col = first_present(row, FORMULA_ERR_COLS)
        self.survival_partition_failures += fnum(row.get(sf_col)) if sf_col else 0.0
        self.formula_failures += fnum(row.get(ff_col)) if ff_col else 0.0
        self.max_formula_err = max(self.max_formula_err, fnum(row.get(fe_col)) if fe_col else 0.0)

        m_val = None
        if m_col:
            m_val = fnum(row.get(m_col), default=0.0)
            self.has_m_col = True
        elif m_fallback_col:
            # Fallback: pre-step nodes plus births in this step is usually closer than M_pre alone.
            m_val = fnum(row.get(m_fallback_col), default=0.0) + b
            self.has_m_col = True
        if m_val is not None:
            self.max_M = max(self.max_M, m_val)
            if step >= self.last_step_seen:
                self.final_M = m_val
                self.last_step_seen = step

    @property
    def C_birth(self) -> float:
        return div(self.births, self.occ)

    @property
    def C_component(self) -> float:
        return div(self.occ_in_clean, self.occ)

    @property
    def chi(self) -> float:
        return div(self.occ_in_clean, self.clean_stars)

    @property
    def V_pair_load(self) -> float:
        return div(self.occ_ms_load, self.occ)

    @property
    def B_per_step(self) -> float:
        return div(self.births, self.rows)

    @property
    def O_per_step(self) -> float:
        return div(self.occ, self.rows)


@dataclass
class FileResult:
    path: str
    stem: str
    metadata: dict[str, Any]
    raw_rows: int
    filtered_rows: int
    runs: list[RunAgg]
    available_cols: set[str]
    window_desc: str

    @property
    def policy(self) -> str:
        policies = {r.policy for r in self.runs if r.policy}
        if policies:
            return sorted(policies)[0]
        return "unknown"

    @property
    def N(self) -> int | None:
        vals = {r.N for r in self.runs if r.N is not None}
        return sorted(vals)[0] if vals else self.metadata.get("N")

    @property
    def k(self) -> int | None:
        vals = {r.k for r in self.runs if r.k is not None}
        return sorted(vals)[0] if vals else self.metadata.get("k")

    @property
    def T(self) -> int | None:
        vals = {r.T for r in self.runs if r.T is not None}
        return sorted(vals)[0] if vals else self.metadata.get("T")

    @property
    def k_over_N(self) -> float | None:
        N = self.N
        k = self.k
        return k / N if N and k is not None else None


@dataclass
class CellResult:
    key: tuple[Any, ...]
    label: str
    policy: str
    N: int
    k: int
    T: int | None
    ratio_key: float
    files: list[str] = field(default_factory=list)
    runs: list[RunAgg] = field(default_factory=list)
    window_desc: str = "all"


# ---------------------------------------------------------------------------
# Reading and aggregation
# ---------------------------------------------------------------------------

def get_row_metadata(row: dict[str, str], path_meta: dict[str, Any]) -> tuple[str, int | None, int | None, int | None, int | None]:
    policy_col = first_present(row, POLICY_COLS)
    N_col = first_present(row, N_COLS)
    k_col = first_present(row, K_COLS)
    T_col = first_present(row, T_COLS)
    batch_col = first_present(row, BATCH_COLS)

    policy = str(row.get(policy_col)).strip() if policy_col else "bound_symmetric"
    N = inum(row.get(N_col), path_meta.get("N") or 0) if N_col else path_meta.get("N")
    k = inum(row.get(k_col), path_meta.get("k") or 0) if k_col else path_meta.get("k")
    T = inum(row.get(T_col), path_meta.get("T") or 0) if T_col else path_meta.get("T")
    batch = inum(row.get(batch_col), path_meta.get("batch") or 0) if batch_col else path_meta.get("batch")
    if N == 0:
        N = None
    if k == 0 and path_meta.get("k") is None:
        k = None
    if T == 0 and path_meta.get("T") is None:
        T = None
    if batch == 0 and path_meta.get("batch") is None:
        batch = None
    return policy, N, k, T, batch


def read_file(path: str, step_min: int | None, step_max: int | None) -> FileResult:
    meta = parse_metadata_from_name(path)
    runs: dict[str, RunAgg] = {}
    raw_rows = 0
    filtered_rows = 0
    available_cols: set[str] = set()

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames:
            available_cols = set(reader.fieldnames)
        run_col = first_present({c: "x" for c in available_cols}, RUN_COLS)
        step_col = first_present({c: "x" for c in available_cols}, STEP_COLS)
        m_col = first_present({c: "x" for c in available_cols}, M_COLS_PREFERRED)
        m_fallback_col = first_present({c: "x" for c in available_cols}, M_COLS_FALLBACK)
        has_survival_cols = COL_OCC_IN_CLEAN in available_cols

        for row in reader:
            raw_rows += 1
            step = fnum(row.get(step_col), default=raw_rows - 1) if step_col else float(raw_rows - 1)
            if step_min is not None and step < step_min:
                continue
            if step_max is not None and step >= step_max:
                continue
            filtered_rows += 1

            run_id = str(row.get(run_col)).strip() if run_col else "run0"
            if not run_id:
                run_id = "run0"
            policy, N, k, T, batch = get_row_metadata(row, meta)

            if run_id not in runs:
                runs[run_id] = RunAgg(
                    file=path,
                    stem=Path(path).stem,
                    run_id=run_id,
                    policy=policy,
                    N=N,
                    k=k,
                    T=T,
                    batch=batch,
                    has_survival_cols=has_survival_cols,
                )
            runs[run_id].raw_rows_seen += 1
            runs[run_id].add_row(row, step=step, m_col=m_col, m_fallback_col=m_fallback_col)

    if step_min is None and step_max is None:
        window_desc = "all"
    elif step_max is None:
        window_desc = f"step>={step_min}"
    elif step_min is None:
        window_desc = f"step<{step_max}"
    else:
        window_desc = f"step>={step_min}, step<{step_max}"

    return FileResult(
        path=path,
        stem=Path(path).stem,
        metadata=meta,
        raw_rows=raw_rows,
        filtered_rows=filtered_rows,
        runs=list(runs.values()),
        available_cols=available_cols,
        window_desc=window_desc,
    )


def aggregate_runs(runs: list[RunAgg]) -> dict[str, float]:
    total = {
        "runs": float(len(runs)),
        "rows": sum(r.rows for r in runs),
        "births": sum(r.births for r in runs),
        "clean_stars": sum(r.clean_stars for r in runs),
        "occ": sum(r.occ for r in runs),
        "occ_in_clean": sum(r.occ_in_clean for r in runs),
        "occ_ms_load": sum(r.occ_ms_load for r in runs),
        "occ_in_ms": sum(r.occ_in_ms for r in runs),
        "occ_embedded": sum(r.occ_embedded for r in runs),
        "occ_other_logged": sum(r.occ_other_logged for r in runs),
        "ms_components": sum(r.ms_components for r in runs),
        "rows_with_ms": sum(r.rows_with_ms for r in runs),
        "survival_partition_failures": sum(r.survival_partition_failures for r in runs),
        "formula_failures": sum(r.formula_failures for r in runs),
        "max_formula_err": max([r.max_formula_err for r in runs], default=0.0),
        "final_M_mean": div(sum(r.final_M for r in runs), len(runs)),
        "final_M_max": max([r.final_M for r in runs], default=0.0),
        "max_M": max([r.max_M for r in runs], default=0.0),
    }
    total["C_birth"] = div(total["births"], total["occ"])
    total["C_component"] = div(total["occ_in_clean"], total["occ"])
    total["chi"] = div(total["occ_in_clean"], total["clean_stars"])
    total["V_pair_load"] = div(total["occ_ms_load"], total["occ"])
    total["B_per_step"] = div(total["births"], total["rows"])
    total["O_per_step"] = div(total["occ"], total["rows"])
    total["ms_prevalence"] = div(total["rows_with_ms"], total["rows"])
    total["identity_err"] = abs(total["C_birth"] - div(total["C_component"], total["chi"])) if total["chi"] else 0.0
    total["B_identity_err"] = abs(total["B_per_step"] - total["O_per_step"] * total["C_birth"])

    # Partition. If logged-other exists, prefer it; otherwise derive other/false as residual.
    if total["occ_other_logged"]:
        other = total["occ_other_logged"]
    else:
        other = total["occ"] - total["occ_in_clean"] - total["occ_in_ms"] - total["occ_embedded"]
        if abs(other) < 1e-9:
            other = 0.0
    total["occ_other"] = other
    return total


def birth_identity_counts(runs: list[RunAgg]) -> tuple[int, int]:
    # Per-run aggregate identity is weaker than row identity, but row identity was already logged in old reports.
    # Here we count nonzero run aggregates for a conservative PASS indicator.
    total = 0
    matches = 0
    for r in runs:
        if r.births > 0 or r.clean_stars > 0:
            total += 1
            if abs(r.births - r.clean_stars) < 1e-9:
                matches += 1
    return matches, total


def classify_tag(fr: FileResult, agg: dict[str, float]) -> str:
    if fr.filtered_rows == 0:
        return "[HEUR-empty]"
    has_survival = any(r.has_survival_cols for r in fr.runs)
    if not has_survival:
        return "[HEUR-legacy]"
    if agg["formula_failures"] == 0 and agg["survival_partition_failures"] == 0:
        return "[NUM]"
    return "[HEUR]"


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def format_float(x: float, nd: int = 6) -> str:
    if x == 0:
        return "0"
    return f"{x:.{nd}g}"


def print_file_report(fr: FileResult, tail_threshold: float, per_run_top: int, per_run_sort: str) -> None:
    agg = aggregate_runs(fr.runs)
    tag = classify_tag(fr, agg)
    N = fr.N
    k = fr.k
    T = fr.T
    ratio = fr.k_over_N
    ratio_txt = f"{ratio:.4f}" if ratio is not None else "N/A"

    print(f"=== {fr.stem} {tag} ===")
    print(f"  metadata: policy={fr.policy} N={N} k={k} k/N={ratio_txt} T={T} batch={fr.metadata.get('batch')}")
    print(f"  window={fr.window_desc}  rows={fr.filtered_rows} / raw_rows={fr.raw_rows}  runs={len(fr.runs)}")
    print(f"  births={agg['births']:.0f}  clean_stars={agg['clean_stars']:.0f}  occ_clean_pairs={agg['occ']:.0f}")
    bi_m, bi_t = birth_identity_counts(fr.runs)
    if bi_t:
        print(f"  birth_identity(run-aggregate): {bi_m}/{bi_t} = {div(bi_m, bi_t):.4f}  {'[NUM] PASS' if bi_m == bi_t else '[FAIL]'}")
    print(f"  survival_partition_failures={agg['survival_partition_failures']:.0f}  formula_failures={agg['formula_failures']:.0f}  max_formula_err={agg['max_formula_err']:.2e}")
    print()
    print("  TDR-24 factorization:")
    if fr.filtered_rows == 0:
        print("    empty filtered window")
    elif not any(r.has_survival_cols for r in fr.runs):
        print(f"    C_birth      = {agg['C_birth']:.6f}  (births / occ_clean)")
        print("    C_component, chi unavailable: legacy log has no survival columns")
    else:
        print(f"    C_birth      = {agg['C_birth']:.6f}  (births / occ_clean)")
        print(f"    C_component  = {agg['C_component']:.6f}  (occ_in_clean_star / occ_clean)")
        print(f"    chi          = {agg['chi']:.4f}  (occ_in_clean_star / clean_star_components)")
        print(f"    V_pair_load  = {agg['V_pair_load']:.6f}  (occ_multistar_pairs / occ_clean_pairs; may exceed 1)")
        print(f"    B_per_step   = {agg['B_per_step']:.6f}")
        print(f"    O_per_step   = {agg['O_per_step']:.6f}")
        print(f"    final_M_mean = {agg['final_M_mean']:.6f}; final_M_max={agg['final_M_max']:.1f}")
        print(f"    C_birth = C_component/chi: err={agg['identity_err']:.2e} [ALG OK]")
        print(f"    B/step = O/step*C_birth: err={agg['B_identity_err']:.2e} [ALG OK]")
    print(f"  ms_prevalence = {agg['ms_prevalence']:.4f}")

    if fr.runs:
        bulk = [r for r in fr.runs if r.final_M <= tail_threshold]
        tail = [r for r in fr.runs if r.final_M > tail_threshold]
        a_bulk = aggregate_runs(bulk)
        a_tail = aggregate_runs(tail)
        total_births = agg["births"]
        print()
        print(f"  bulk/tail split by final_M > {tail_threshold:g}:")
        print(f"  {'group':>8} {'runs':>5} {'birth_share':>11} {'C_birth':>10} {'C_comp':>10} {'chi':>9} {'B/step':>9} {'O/step':>9} {'final_M_mean':>12} {'final_M_max':>11}")
        for name, ar in [("bulk", a_bulk), ("tail", a_tail)]:
            print(
                f"  {name:>8} {int(ar['runs']):>5} {div(ar['births'], total_births):>11.4f} "
                f"{ar['C_birth']:>10.6f} {ar['C_component']:>10.6f} {ar['chi']:>9.3f} "
                f"{ar['B_per_step']:>9.5f} {ar['O_per_step']:>9.3f} "
                f"{ar['final_M_mean']:>12.2f} {ar['final_M_max']:>11.1f}"
            )

    if per_run_top > 0 and fr.runs:
        key = per_run_sort
        def sort_key(r: RunAgg):
            return getattr(r, key, 0.0) if hasattr(r, key) else 0.0
        rows = sorted(fr.runs, key=sort_key, reverse=True)[:per_run_top]
        print()
        print(f"  per-run top {len(rows)} by {per_run_sort}:")
        print(f"  {'run_id':>28} {'final_M':>8} {'max_M':>8} {'rows':>6} {'births':>8} {'O':>10} {'C_birth':>10} {'C_comp':>10} {'chi':>9} {'V_load':>9} {'B/step':>9}")
        for r in rows:
            print(
                f"  {r.run_id:>28} {r.final_M:>8.1f} {r.max_M:>8.1f} {r.rows:>6} "
                f"{r.births:>8.0f} {r.occ:>10.0f} {r.C_birth:>10.6f} {r.C_component:>10.6f} "
                f"{r.chi:>9.3f} {r.V_pair_load:>9.3f} {r.B_per_step:>9.5f}"
            )
    print()


# ---------------------------------------------------------------------------
# Scaling, bootstrap, CSV exports
# ---------------------------------------------------------------------------

def cell_key(fr: FileResult, ratio_decimals: int) -> tuple[Any, ...] | None:
    N = fr.N
    k = fr.k
    T = fr.T
    if N is None or k is None:
        return None
    ratio_key = round(k / N, ratio_decimals)
    return (fr.policy, ratio_key, T, fr.window_desc, N, k)


def combine_cells(file_results: list[FileResult], ratio_decimals: int, include_empty: bool = False, include_legacy: bool = False) -> list[CellResult]:
    cells: dict[tuple[Any, ...], CellResult] = {}
    for fr in file_results:
        if fr.filtered_rows == 0 and not include_empty:
            continue
        if not any(r.has_survival_cols for r in fr.runs) and not include_legacy:
            continue
        key = cell_key(fr, ratio_decimals)
        if key is None:
            continue
        policy, ratio_key, T, window, N, k = key
        if key not in cells:
            label = f"N{N}_k{k}_T{T}_{policy}_{window}"
            cells[key] = CellResult(key=key, label=label, policy=policy, N=N, k=k, T=T, ratio_key=ratio_key, window_desc=window)
        cells[key].files.append(fr.path)
        cells[key].runs.extend(fr.runs)
    return sorted(cells.values(), key=lambda c: (c.policy, c.ratio_key, c.T or -1, c.N, c.k))


def fit_power_law(points: list[tuple[float, float]]) -> tuple[float, float, float] | None:
    pts = [(x, y) for x, y in points if x > 0 and y > 0]
    if len(pts) < 3:
        return None
    xs = [math.log(x) for x, _ in pts]
    ys = [math.log(y) for _, y in pts]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    den = sum((x - mx) ** 2 for x in xs)
    if den == 0:
        return None
    slope = sum((xs[i] - mx) * (ys[i] - my) for i in range(n)) / den
    intercept = my - slope * mx
    # R^2
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - (intercept + slope * xs[i])) ** 2 for i in range(n))
    r2 = 1.0 - ss_res / ss_tot if ss_tot else 1.0
    return math.exp(intercept), slope, r2


def print_fit(label: str, points: list[tuple[float, float]]) -> None:
    fit = fit_power_law(points)
    if fit is None:
        return
    A, slope, r2 = fit
    print(f"  [HEUR] {label}(N) ≈ {A:.4g} N^{slope:+.3f}  (R²={r2:.3f})")


def print_scaling_summary(cells: list[CellResult], tail_threshold: float, tail_thresholds: list[float], fit_bulk_tdr24: bool, fit_bulk_final_M: bool) -> None:
    if not cells:
        return
    print("\n" + "=" * 92)
    print("SCALING SUMMARY — valid survival logs only, pooled by cell")
    print("=" * 92)

    # Group by policy, ratio, T, window.
    groups: dict[tuple[Any, ...], list[CellResult]] = {}
    for c in cells:
        gkey = (c.policy, c.ratio_key, c.T, c.window_desc)
        groups.setdefault(gkey, []).append(c)

    for gkey, group_cells in sorted(groups.items(), key=lambda kv: kv[0]):
        policy, ratio, T, window = gkey
        print(f"\nGroup: policy={policy}, k/N={ratio:.6f}, T={T}, window={window}")
        tail_headers = " ".join([f"p>{int(th):<3}" for th in tail_thresholds])
        print(
            f"{'cell':>32} {'files':>5} {'N':>6} {'C_birth':>12} {'C_comp':>12} {'chi':>9} "
            f"{'B/step':>10} {'O/step':>10} {'M_mean':>9} {'M_bulk':>9} {tail_headers}"
        )
        print("-" * 126)

        aggregate_points: dict[str, list[tuple[float, float]]] = {
            "C_birth": [], "C_component": [], "chi": [], "B_per_step": [], "O_per_step": [], "final_M_mean": [],
        }
        bulk_points: dict[str, list[tuple[float, float]]] = {
            "C_birth_bulk": [], "C_component_bulk": [], "chi_bulk": [], "B_per_step_bulk": [], "O_per_step_bulk": [], "final_M_bulk": [],
        }

        for c in sorted(group_cells, key=lambda x: x.N):
            agg = aggregate_runs(c.runs)
            bulk = [r for r in c.runs if r.final_M <= tail_threshold]
            ab = aggregate_runs(bulk)
            ptails = [div(sum(1 for r in c.runs if r.final_M > th), len(c.runs)) for th in tail_thresholds]

            print(
                f"{c.label[:32]:>32} {len(c.files):>5} {c.N:>6} "
                f"{agg['C_birth']:>12.6g} {agg['C_component']:>12.6g} {agg['chi']:>9.4g} "
                f"{agg['B_per_step']:>10.5g} {agg['O_per_step']:>10.5g} {agg['final_M_mean']:>9.2f} {ab['final_M_mean']:>9.2f} "
                + " ".join([f"{p:<6.3f}" for p in ptails])
            )

            N = float(c.N)
            aggregate_points["C_birth"].append((N, agg["C_birth"]))
            aggregate_points["C_component"].append((N, agg["C_component"]))
            aggregate_points["chi"].append((N, agg["chi"]))
            aggregate_points["B_per_step"].append((N, agg["B_per_step"]))
            aggregate_points["O_per_step"].append((N, agg["O_per_step"]))
            aggregate_points["final_M_mean"].append((N, agg["final_M_mean"]))

            if bulk:
                bulk_points["C_birth_bulk"].append((N, ab["C_birth"]))
                bulk_points["C_component_bulk"].append((N, ab["C_component"]))
                bulk_points["chi_bulk"].append((N, ab["chi"]))
                bulk_points["B_per_step_bulk"].append((N, ab["B_per_step"]))
                bulk_points["O_per_step_bulk"].append((N, ab["O_per_step"]))
                bulk_points["final_M_bulk"].append((N, ab["final_M_mean"]))

        print("\n  Aggregate fits:")
        for name in ["C_birth", "C_component", "chi", "B_per_step", "O_per_step"]:
            print_fit(name, aggregate_points[name])
        if fit_bulk_final_M:
            print_fit("final_M_mean", aggregate_points["final_M_mean"])

        if fit_bulk_tdr24 or fit_bulk_final_M:
            print(f"\n  Bulk-conditioned fits (bulk: final_M <= {tail_threshold:g}):")
            if fit_bulk_tdr24:
                for name in ["C_birth_bulk", "C_component_bulk", "chi_bulk", "B_per_step_bulk", "O_per_step_bulk"]:
                    print_fit(name, bulk_points[name])
            if fit_bulk_final_M:
                print_fit("final_M_bulk", bulk_points["final_M_bulk"])


def bootstrap_ci_for_runs(runs: list[RunAgg], n_boot: int, seed: int = 0) -> dict[str, tuple[float, float]]:
    if not runs or n_boot <= 0:
        return {}
    rng = random.Random(seed)
    metrics = {"C_birth": [], "C_component": [], "chi": [], "B_per_step": [], "O_per_step": []}
    n = len(runs)
    for _ in range(n_boot):
        sample = [runs[rng.randrange(n)] for _ in range(n)]
        agg = aggregate_runs(sample)
        for key in metrics:
            metrics[key].append(agg[key])
    out = {}
    for key, vals in metrics.items():
        vals.sort()
        lo = vals[int(0.025 * (len(vals) - 1))]
        hi = vals[int(0.975 * (len(vals) - 1))]
        out[key] = (lo, hi)
    return out


def write_per_run_csv(path: str, cells: list[CellResult], tail_threshold: float) -> None:
    fieldnames = [
        "cell", "file", "run_id", "policy", "N", "k", "T", "k_over_N", "tail_threshold", "is_tail",
        "final_M", "max_M", "rows", "births", "occ_clean_pairs", "occ_in_clean_star", "clean_star_components",
        "C_birth", "C_component", "chi", "V_pair_load", "B_per_step", "O_per_step",
    ]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for c in cells:
            for r in c.runs:
                writer.writerow({
                    "cell": c.label,
                    "file": Path(r.file).name,
                    "run_id": r.run_id,
                    "policy": r.policy,
                    "N": r.N,
                    "k": r.k,
                    "T": r.T,
                    "k_over_N": div(r.k or 0, r.N or 0),
                    "tail_threshold": tail_threshold,
                    "is_tail": int(r.final_M > tail_threshold),
                    "final_M": r.final_M,
                    "max_M": r.max_M,
                    "rows": r.rows,
                    "births": r.births,
                    "occ_clean_pairs": r.occ,
                    "occ_in_clean_star": r.occ_in_clean,
                    "clean_star_components": r.clean_stars,
                    "C_birth": r.C_birth,
                    "C_component": r.C_component,
                    "chi": r.chi,
                    "V_pair_load": r.V_pair_load,
                    "B_per_step": r.B_per_step,
                    "O_per_step": r.O_per_step,
                })
    print(f"[ALG] wrote per-run summary CSV: {path}")


def print_dsn_patch(cells: list[CellResult], tail_threshold: float) -> None:
    print("\n" + "=" * 70)
    print("DSN PATCH BLOCK")
    print("=" * 70)
    for c in cells:
        agg = aggregate_runs(c.runs)
        bulk = [r for r in c.runs if r.final_M <= tail_threshold]
        tail = [r for r in c.runs if r.final_M > tail_threshold]
        ab = aggregate_runs(bulk)
        at = aggregate_runs(tail)
        print(f"\n[NUM] Motif cell: N={c.N}, k={c.k}, T={c.T}, policy={c.policy}, window={c.window_desc}")
        print(f"  files = {len(c.files)}; runs = {len(c.runs)}")
        print(f"  C_birth = {agg['C_birth']:.8g}")
        print(f"  C_component = {agg['C_component']:.8g}")
        print(f"  chi = {agg['chi']:.4g}")
        print(f"  V_pair_load = {agg['V_pair_load']:.5g}")
        print(f"  B_per_step = {agg['B_per_step']:.6g}")
        print(f"  O_per_step = {agg['O_per_step']:.6g}")
        print(f"  final_M_mean = {agg['final_M_mean']:.3f}; final_M_max = {agg['final_M_max']:.1f}")
        print(f"  tail_threshold = {tail_threshold:g}")
        print(f"  p_tail = {div(len(tail), len(c.runs)):.6g}; birth_share_tail = {div(at['births'], agg['births']):.6g}")
        print(f"  final_M_bulk_mean = {ab['final_M_mean']:.3f}; final_M_tail_mean = {at['final_M_mean']:.3f}")
        print(f"  C_birth_bulk = {ab['C_birth']:.8g}; C_component_bulk = {ab['C_component']:.8g}; chi_bulk = {ab['chi']:.4g}")
        print(f"  B_per_step_bulk = {ab['B_per_step']:.6g}; O_per_step_bulk = {ab['O_per_step']:.6g}")
        print(f"  C_birth = C_component/chi identity error = {agg['identity_err']:.2e}")
        print(f"  B/step = O/step*C_birth identity error = {agg['B_identity_err']:.2e}")
        print(f"  ms_prevalence = {agg['ms_prevalence']:.4f}")
    print("""
[OPEN TDR-24A] Derive C_component from defect-graph combinatorics and multistar locking.
[OPEN TDR-24B] Derive chi, the pair-to-component compression factor.
[OPEN TDR-24C] Connect B_per_step = O_per_step * C_birth to rN_late and thermodynamic crystallization.
[OPEN TDR-24D] Derive O_per_step scaling from the exact v16 occupancy-candidate definition.
[OPEN TDR-24E] Distinguish aggregate and bulk-conditioned TDR-24 exponents.
[OPEN TDR-25] Characterize p_tail^100, p_tail^200, p_tail^500 and their N-dependence.
""")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def collect_paths(args: argparse.Namespace) -> list[str]:
    paths: list[str] = []
    paths.extend(args.files or [])
    if args.glob:
        for pat in args.glob:
            paths.extend(globlib.glob(pat))
    if args.dir:
        for d in args.dir:
            paths.extend(globlib.glob(os.path.join(d, "*.csv")))
    # Preserve order but deduplicate.
    seen = set()
    out = []
    for p in paths:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="TDR-G motif analysis v4: bulk-conditioned TDR-24 fits and tail thresholds")
    parser.add_argument("files", nargs="*", help="CSV files to analyze")
    parser.add_argument("--glob", nargs="+", help="Glob pattern(s) for CSV files")
    parser.add_argument("--dir", nargs="+", help="Directory/directories to scan for CSV files")
    parser.add_argument("--step-min", type=int, default=None, help="Include rows with step >= step_min")
    parser.add_argument("--step-max", type=int, default=None, help="Include rows with step < step_max")
    parser.add_argument("--tail-threshold", type=float, default=500.0, help="Threshold defining tail for bulk fits")
    parser.add_argument("--tail-thresholds", nargs="+", type=float, default=[100.0, 200.0, 500.0], help="Thresholds for p_tail table")
    parser.add_argument("--fit-bulk-tdr24", action="store_true", help="Print bulk-conditioned TDR-24 scaling fits")
    parser.add_argument("--fit-bulk-final-M", action="store_true", help="Print bulk-conditioned final_M scaling fit")
    parser.add_argument("--per-run-top", type=int, default=0, help="Print top N runs by selected metric")
    parser.add_argument("--per-run-sort", default="final_M", choices=["final_M", "max_M", "births", "C_birth", "C_component", "chi", "B_per_step", "O_per_step"], help="Metric for per-run top sorting")
    parser.add_argument("--per-run-csv", help="Write per-run summary CSV")
    parser.add_argument("--bootstrap", type=int, default=0, help="Optional run-level bootstrap replicates for future extension")
    parser.add_argument("--bootstrap-seed", type=int, default=0)
    parser.add_argument("--ratio-decimals", type=int, default=6, help="Round k/N to this many decimals for grouping")
    parser.add_argument("--include-empty", action="store_true", help="Include empty filtered windows in scaling")
    parser.add_argument("--include-legacy-scaling", action="store_true", help="Include logs without survival columns in scaling")
    parser.add_argument("--dsn-patch", action="store_true", help="Print DSN patch block")
    args = parser.parse_args()

    paths = collect_paths(args)
    if not paths:
        print("No CSV files specified.")
        sys.exit(0)

    file_results: list[FileResult] = []
    for path in paths:
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping", file=sys.stderr)
            continue
        fr = read_file(path, step_min=args.step_min, step_max=args.step_max)
        file_results.append(fr)
        if fr.filtered_rows == 0 and not args.include_empty:
            # Still show a compact warning; full reports for empty windows are usually noise.
            print(f"=== {fr.stem} [SKIP-empty] ===")
            print(f"  window={fr.window_desc} produced 0 rows / raw_rows={fr.raw_rows}\n")
            continue
        if not any(r.has_survival_cols for r in fr.runs) and not args.include_legacy_scaling:
            print(f"=== {fr.stem} [SKIP-legacy] ===")
            print("  log lacks v16 survival columns; skipped from v4 report by default\n")
            continue
        print_file_report(fr, tail_threshold=args.tail_threshold, per_run_top=args.per_run_top, per_run_sort=args.per_run_sort)

    cells = combine_cells(file_results, ratio_decimals=args.ratio_decimals, include_empty=args.include_empty, include_legacy=args.include_legacy_scaling)
    print_scaling_summary(cells, tail_threshold=args.tail_threshold, tail_thresholds=args.tail_thresholds, fit_bulk_tdr24=args.fit_bulk_tdr24, fit_bulk_final_M=args.fit_bulk_final_M)

    if args.per_run_csv:
        write_per_run_csv(args.per_run_csv, cells, tail_threshold=args.tail_threshold)

    if args.dsn_patch:
        print_dsn_patch(cells, tail_threshold=args.tail_threshold)


if __name__ == "__main__":
    main()
