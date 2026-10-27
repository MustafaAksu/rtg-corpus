#!/usr/bin/env python3
"""
tdr_motif_bootstrap_v1.py
Run-level bootstrap analysis for TDR-G v15/v16 motif logs.

Purpose:
  - Compute TDR-24 factorization on motif CSV logs:
      C_birth      = sum(births_step) / sum(occ_clean_pairs)
      C_component  = sum(occ_clean_pairs_in_clean_star) / sum(occ_clean_pairs)
      chi          = sum(occ_clean_pairs_in_clean_star) / sum(clean_star_components)
      V_pair_load  = sum(occ_multistar_pairs) / sum(occ_clean_pairs)
  - Bootstrap confidence intervals by resampling runs, not rows.
  - Fit scaling exponents y ~ A N^p by grouped (policy, k/N, T, window).

Examples:
  python tdr_motif_bootstrap_v1.py --glob "motif_*_T5000_v16.csv" --step-min 4001 --bootstrap 1000 --dsn-patch
  python tdr_motif_bootstrap_v1.py --glob "motif_*_v16.csv" --only-T 5000 --step-min 4001 --bootstrap 1000 --dsn-patch

Notes:
  - Legacy logs without v15/v16 survival columns are tagged [HEUR-legacy].
  - V_pair_load may exceed 1; it is a load ratio, not a probability.
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
from typing import Any


# ---------------------------------------------------------------------------
# Helpers
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
    return ys[lo] * (1 - w) + ys[hi] * w


def fmt_ci(x: float, ci: tuple[float, float] | None, digits: int = 6) -> str:
    if ci is None:
        return f"{x:.{digits}f}"
    return f"{x:.{digits}f} [{ci[0]:.{digits}f}, {ci[1]:.{digits}f}]"


def parse_ratio(x: str) -> float:
    x = x.strip()
    if "/" in x:
        a, b = x.split("/", 1)
        return float(a) / float(b)
    return float(x)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class RunAgg:
    run_id: str
    rows: int = 0
    rows_with_multistar: int = 0
    births: float = 0.0
    clean_stars: float = 0.0
    occ_clean: float = 0.0
    occ_in_clean: float = 0.0
    occ_in_multistar: float = 0.0
    occ_embedded: float = 0.0
    occ_other: float = 0.0
    occ_multistar_pairs: float = 0.0


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

    # computed metrics
    metrics: dict[str, float] = field(default_factory=dict)
    ci: dict[str, tuple[float, float]] = field(default_factory=dict)


SURVIVAL_COLS = {
    "occ_clean_pairs_in_clean_star",
}

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
    # policy is usually in column; do not infer aggressively from filename.
    return out


def update_meta_from_row(meta: dict[str, Any], row: dict[str, str]) -> None:
    for key in ["N", "k", "T", "batch"]:
        if key in row and str(row[key]).strip() != "":
            meta[key] = inum(row[key])
    for key in ["policy", "multistar_policy"]:
        if key in row and str(row[key]).strip() != "":
            meta["policy"] = str(row[key]).strip()
    if "k_over_N" in row and str(row["k_over_N"]).strip() != "":
        meta["k_over_N"] = fnum(row["k_over_N"])


def read_rows(path: str) -> tuple[list[dict[str, str]], set[str]]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        rows = [{k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()} for row in reader]
    cols = set(rows[0].keys()) if rows else set()
    return rows, cols


def filter_rows(rows: list[dict[str, str]], *, step_min: int | None, step_max: int | None,
                late_frac: float | None) -> tuple[list[dict[str, str]], str]:
    if not rows:
        return rows, "all"
    if "step" not in rows[0]:
        return rows, "all(no_step_col)"

    # explicit filters first
    filtered = rows
    label_parts = []

    if late_frac is not None:
        # Per-run late window. Uses step column and run_id/run grouping.
        run_col = "run_id" if "run_id" in rows[0] else ("run" if "run" in rows[0] else None)
        if run_col is None:
            max_step = max(inum(r.get("step")) for r in rows)
            threshold = int(math.floor(max_step * (1.0 - late_frac))) + 1
            filtered = [r for r in filtered if inum(r.get("step")) >= threshold]
            label_parts.append(f"late_frac={late_frac}, step>={threshold}")
        else:
            max_by_run: dict[str, int] = {}
            min_by_run: dict[str, int] = {}
            for r in rows:
                rid = str(r.get(run_col))
                st = inum(r.get("step"))
                max_by_run[rid] = max(max_by_run.get(rid, st), st)
                min_by_run[rid] = min(min_by_run.get(rid, st), st)
            thresholds: dict[str, int] = {}
            for rid, mx in max_by_run.items():
                mn = min_by_run[rid]
                span = mx - mn + 1
                keep = max(1, int(math.ceil(span * late_frac)))
                thresholds[rid] = mx - keep + 1
            filtered = [r for r in filtered if inum(r.get("step")) >= thresholds[str(r.get(run_col))]]
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

    C_birth = births / occ if occ > 0 else 0.0
    C_comp = oic / occ if occ > 0 else 0.0
    chi = oic / clean if clean > 0 else 0.0
    V_load = oms / occ if occ > 0 else 0.0
    identity_err = abs(C_birth - (C_comp / chi)) if chi > 0 else 0.0

    return {
        "rows": rows,
        "births": births,
        "clean_stars": clean,
        "occ_clean": occ,
        "occ_in_clean": oic,
        "occ_in_multistar": oims,
        "occ_embedded": oe,
        "occ_other": oo,
        "occ_multistar_pairs": oms,
        "C_birth": C_birth,
        "C_component": C_comp,
        "chi": chi,
        "V_pair_load": V_load,
        "identity_err": identity_err,
        "ms_prevalence": rows_ms / rows if rows > 0 else 0.0,
        "B_per_step": births / rows if rows > 0 else 0.0,
        "O_per_step": occ / rows if rows > 0 else 0.0,
    }


def analyze_file(path: str, *, step_min: int | None, step_max: int | None,
                 late_frac: float | None, bootstrap: int, seed: int) -> FileAgg:
    raw_rows, cols = read_rows(path)
    filtered, window = filter_rows(raw_rows, step_min=step_min, step_max=step_max, late_frac=late_frac)

    meta = infer_from_filename(path)
    if raw_rows:
        update_meta_from_row(meta, raw_rows[0])
    if "k_over_N" not in meta and "N" in meta and "k" in meta and meta["N"]:
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

    run_col = "run_id" if "run_id" in cols else ("run" if "run" in cols else "__single_run__")
    by_run: dict[str, RunAgg] = {}

    for row in filtered:
        rid = str(row.get(run_col, "0"))
        ragg = by_run.setdefault(rid, RunAgg(run_id=rid))

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
        ragg.births += b
        ragg.clean_stars += cs
        ragg.occ_clean += occ
        ragg.occ_in_clean += oic
        ragg.occ_in_multistar += oims
        ragg.occ_embedded += oe
        ragg.occ_other += oo
        ragg.occ_multistar_pairs += oms

        if b > 0 or cs > 0:
            agg.birth_identity_total += 1
            if abs(b - cs) < 0.5:
                agg.birth_identity_matches += 1

        if agg.has_partition:
            if abs(occ - (oic + oims + oe + oo)) > 0.5:
                agg.survival_partition_failures += 1

        if agg.has_formula_cols:
            errs = []
            logged_surv = fnum(row.get("occ_clean_survival_rate"))
            logged_birth = fnum(row.get("occ_clean_birth_survival_rate"))
            logged_comp = fnum(row.get("occ_clean_component_compression"))
            calc_surv = oic / occ if occ > 0 else 0.0
            calc_birth = b / occ if occ > 0 else 0.0
            calc_comp = oic / cs if cs > 0 else 0.0
            errs.extend([abs(logged_surv - calc_surv), abs(logged_birth - calc_birth), abs(logged_comp - calc_comp)])
            me = max(errs)
            agg.max_formula_err = max(agg.max_formula_err, me)
            if me > 1e-9:
                agg.formula_failures += 1

    agg.run_aggs = list(by_run.values())
    agg.metrics = compute_metrics_from_runs(agg.run_aggs)

    if bootstrap > 0 and len(agg.run_aggs) >= 2:
        rng = random.Random(seed)
        samples: dict[str, list[float]] = defaultdict(list)
        n = len(agg.run_aggs)
        keys = ["C_birth", "C_component", "chi", "V_pair_load", "B_per_step", "O_per_step"]
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
    # y = A N^slope. For decays report alpha=-slope.
    return math.exp(intercept), -slope


def bootstrap_exponent(files: list[FileAgg], metric: str, n_boot: int, seed: int) -> tuple[float, float] | None:
    if n_boot <= 0 or len(files) < 3:
        return None
    if any(len(f.run_aggs) < 2 for f in files):
        return None
    rng = random.Random(seed)
    alphas = []
    for _ in range(n_boot):
        boot_files = []
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
        # one representative per (N,k,T,policy,window), prefer latest lexicographic name by default
        groups[key].append(a)
    # Deduplicate inside each group by N; keep last sorted by name.
    out = {}
    for key, vals in groups.items():
        byN: dict[int, FileAgg] = {}
        for a in sorted(vals, key=lambda x: x.name):
            byN[a.N] = a
        out[key] = sorted(byN.values(), key=lambda x: x.N or 0)
    return out


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def dsn_tag(a: FileAgg) -> str:
    if not a.has_survival:
        return "[HEUR-legacy]"
    if a.birth_identity_total > 0 and a.birth_identity_matches == a.birth_identity_total and a.survival_partition_failures == 0:
        return "[NUM]"
    return "[HEUR]"


def report_file(a: FileAgg, show_bins: bool = False) -> str:
    m = a.metrics
    ci = a.ci
    lines = []
    lines.append(f"=== {a.name} {dsn_tag(a)} ===")
    lines.append(f"  metadata: policy={a.policy} N={a.N} k={a.k} k/N={(a.k_over_N or 0):.4f} T={a.T} batch={a.batch}")
    lines.append(f"  window={a.window}  rows={a.rows} / raw_rows={a.raw_rows}")
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
        lines.append(f"    C_birth = C_component/chi: err={m.get('identity_err',0):.2e} [ALG OK]")
    else:
        lines.append("    C_component, chi unavailable: legacy log has no survival columns")
    lines.append(f"  ms_prevalence = {m.get('ms_prevalence',0):.4f}")
    if show_bins:
        lines.append("  [bins omitted in bootstrap script; use tdr_motif_analysis_v3 for full M_pre bin table]")
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
        print(f"{'file':>34} {'N':>6} {'C_birth':>11} {'C_comp':>11} {'chi':>10} {'V_load':>10} {'B/step':>10} {'O/step':>10}")
        print("-" * 100)
        for a in vals:
            m = a.metrics
            print(f"{a.name[:34]:>34} {a.N:>6} {m['C_birth']:>11.6g} {m['C_component']:>11.6g} {m['chi']:>10.4g} {m['V_pair_load']:>10.4g} {m['B_per_step']:>10.6g} {m['O_per_step']:>10.6g}")
        if len(vals) >= 3:
            for metric in ["C_birth", "C_component", "chi", "B_per_step", "O_per_step"]:
                fit = fit_power(vals, metric)
                if fit is None:
                    continue
                A, alpha = fit
                ci = bootstrap_exponent(vals, metric, bootstrap, seed + hash((key, metric)) % 1000000)
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
  C_birth = C_component/chi identity error = {m.get('identity_err',0):.2e}
  ms_prevalence = {m.get('ms_prevalence',0):.4f}""")
    print("""
[OPEN TDR-24A] Derive C_component from defect-graph combinatorics and multistar locking.
[OPEN TDR-24B] Derive chi, the pair-to-component compression factor.
[OPEN TDR-24C] Connect B_per_step = O_per_step * C_birth to rN_late and thermodynamic crystallization.
""")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(description="Run-level bootstrap for TDR-G motif factorization logs.")
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
        a = analyze_file(path, step_min=args.step_min, step_max=args.step_max,
                         late_frac=args.late_frac, bootstrap=args.bootstrap, seed=args.seed + i * 1009)
        if args.only_T is not None and a.T != args.only_T:
            continue
        if args.only_policy is not None and a.policy != args.only_policy:
            continue
        print(report_file(a))
        print()
        results.append(a)

    print_scaling(results, bootstrap=args.bootstrap, seed=args.seed)
    if args.dsn_patch:
        print_dsn_patch(results)


if __name__ == "__main__":
    main()
