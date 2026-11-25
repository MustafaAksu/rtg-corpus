#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
az/lib/manifest.py
==================
Run-manifest validator enforcing CONV-AZ-MANIFEST. No manifest, no DSN import.
"""
from __future__ import annotations
from typing import Dict, Any, List

REQUIRED_TOP = [
    "run_id", "N", "k", "k_over_N_actual", "regime", "canonical_scaling",
    "policy", "T", "seed", "graph_export", "hashimoto", "nulls", "statistics",
]
REGIMES = {"A", "B1", "B2"}
POLICIES = {"bound_symmetric", "largest_center", "all_centers"}
EXPORT_TYPES = {"final_time", "recurrent_core", "birth_window", "cumulative"}
SPECTRUM_MODES = {"full-spectrum", "leading-K", "trace-moment"}


class ManifestError(ValueError):
    pass


def validate_manifest(m: Dict[str, Any]) -> List[str]:
    """Return [] if valid, else list of problems."""
    problems = []
    for key in REQUIRED_TOP:
        if key not in m:
            problems.append(f"missing top-level key: {key}")
    if problems:
        return problems

    if m["regime"] not in REGIMES:
        problems.append(f"regime must be one of {REGIMES}")
    if m["policy"] not in POLICIES:
        problems.append(f"policy must be one of {POLICIES}")

    # SG-PLAN-5: canonical only for N divisible by 30 with k=N/15
    if m["regime"] == "B1":
        if m["N"] % 30 != 0:
            problems.append("regime B1 requires N divisible by 30")
        if m["k"] != m["N"] // 15:
            problems.append("regime B1 requires k = N/15")
        if not m["canonical_scaling"]:
            problems.append("regime B1 must set canonical_scaling=true")
    else:
        if m.get("canonical_scaling", False):
            problems.append("only regime B1 may set canonical_scaling=true")

    # N must be even (SG-PLAN-1)
    if m["N"] % 2 != 0:
        problems.append("N must be even (SG-PLAN-1)")

    ge = m["graph_export"]
    if ge.get("type") not in EXPORT_TYPES:
        problems.append(f"graph_export.type must be one of {EXPORT_TYPES}")
    if ge.get("directed_edges") != "both_orientations":
        problems.append("graph_export.directed_edges must be 'both_orientations'")
    if ge.get("type") == "birth_window":
        if ge.get("window_w") is None:
            problems.append("birth_window export requires window_w")
        if m.get("birth_window_status") not in {"available", "no_birth", "cap_truncated"}:
            problems.append("birth_window export requires birth_window_status field")

    hz = m["hashimoto"]
    if hz.get("spectrum_mode") not in SPECTRUM_MODES:
        problems.append(f"hashimoto.spectrum_mode must be one of {SPECTRUM_MODES}")
    if "script_version" not in hz:
        problems.append("hashimoto.script_version required")

    # null discipline
    nl = m["nulls"]
    total_null = sum(int(nl.get(f"null{i}_count", 0)) for i in range(5))
    if total_null == 0:
        problems.append("at least one null model required for any candidate claim")

    return problems
