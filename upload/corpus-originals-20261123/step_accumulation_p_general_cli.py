#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RTG general p step-accumulation / bridge-gap CLI
================================================

Thin CLI wrapper around homological_solver_p_general_numeric.py.

For each p:
  1. builds the one-step generalized RTG map,
  2. solves the one-step homological normal form N_p,
  3. computes F_1^p = N_p^p,
  4. computes raw f_p^p,
  5. compares them on 1-step resonant channels.

This is the bridge-gap test for the prime/composite horizon program.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import mpmath as mp

from homological_solver_p_general_numeric import run_p, write_summary_csv, write_summary_md


def main():
    parser = argparse.ArgumentParser(description="General p bridge-gap CLI: F1^p vs raw f_p^p.")
    parser.add_argument("--p", type=int, nargs="*", default=[5, 6, 7, 8])
    parser.add_argument("--D", type=int, default=5)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--tol", type=str, default="1e-50")
    parser.add_argument("--out-dir", type=str, default="")
    parser.add_argument("--summary-csv", type=str, default="bridge_gap_summary.csv")
    parser.add_argument("--summary-md", type=str, default="bridge_gap_summary.md")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    mp.mp.dps = args.dps
    tol = mp.mpf(args.tol)
    out_dir = Path(args.out_dir) if args.out_dir else None

    summaries = []
    for p in args.p:
        summaries.append(run_p(p, args.D, tol, out_dir=out_dir, quiet=args.quiet))

    if args.summary_csv:
        write_summary_csv(Path(args.summary_csv), summaries)
        print(f"Wrote summary CSV: {args.summary_csv}")
    if args.summary_md:
        write_summary_md(Path(args.summary_md), summaries)
        print(f"Wrote summary Markdown: {args.summary_md}")


if __name__ == "__main__":
    main()
