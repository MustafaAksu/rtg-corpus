#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RTG general p homological normalizer (numeric)
==============================================

Generalizes the legacy p=6 homological solver.

Given the generalized RTG resonance family

    rho' = rho - sin(eta)
    eta' = eta + K_p (exp(rho)-1) - K_p sin(eta)
    K_p = 2 - 2 cos(2*pi/p)

this script:
  1. builds the one-step jet f_p in the eigen-coordinate W = rho + gamma eta,
  2. solves the one-step discrete homological normalization through degree D,
  3. exports Phi_1 and the normalized one-step map N_p,
  4. optionally accumulates N_p^p and compares it with the raw p-step jet f_p^p.

DSN interpretation
------------------
- This is a ONE-STEP homological solver.
- Its p-fold iterate is F_1^p = (Phi_1^{-1} f_p Phi_1)^p.
- F_1^p is distinct from raw f_p^p and from a p-step Lie-gauge normalized object
  unless a bridge theorem/convention explicitly identifies them.

Status target:
  [ENG] / [NUM] for broad p scans; exact promotion requires PSLQ/cyclotomic field work.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Dict, Iterable, Tuple, Any

import mpmath as mp

Poly = Dict[Tuple[int, int], mp.mpc]

TOL_DEFAULT = mp.mpf("1e-50")

# -----------------------------------------------------------------------------
# Numeric helpers
# -----------------------------------------------------------------------------

def cmplx(re=0, im=0) -> mp.mpc:
    return mp.mpc(re, im)


def total_deg(m: Tuple[int, int]) -> int:
    return m[0] + m[1]


def fmt(z: mp.mpc, digits: int = 30) -> str:
    return mp.nstr(z, digits)


def parse_complex_obj(obj: Any) -> mp.mpc:
    if isinstance(obj, dict):
        return mp.mpc(obj.get("re", "0"), obj.get("im", "0"))
    if isinstance(obj, (list, tuple)) and len(obj) == 2:
        return mp.mpc(obj[0], obj[1])
    return mp.mpc(str(obj))


def poly_to_jsonable(P: Poly) -> dict:
    return {
        f"({a},{b})": {"re": mp.nstr(mp.re(v), 80), "im": mp.nstr(mp.im(v), 80)}
        for (a, b), v in sorted(P.items(), key=lambda kv: (sum(kv[0]), kv[0][0], kv[0][1]))
    }


def jsonable_to_poly(data: dict, max_deg: int | None = None) -> Poly:
    out: Poly = {}
    for k_str, v in data.items():
        k = k_str.strip().replace("(", "").replace(")", "")
        a, b = [int(x.strip()) for x in k.split(",")]
        if max_deg is None or a + b <= max_deg:
            out[(a, b)] = parse_complex_obj(v)
    return clean_poly(out)

# -----------------------------------------------------------------------------
# Polynomial dictionary algebra
# -----------------------------------------------------------------------------

def clean_poly(P: Poly, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    return {k: v for k, v in P.items() if abs(v) > tol}


def add_poly(*args, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    """Add polynomial dictionaries. Backward-compatible with add_poly(A, B, tol)."""
    if args and not isinstance(args[-1], dict):
        tol = args[-1]
        polys = args[:-1]
    else:
        polys = args
    out: Poly = {}
    for P in polys:
        for k, v in P.items():
            out[k] = out.get(k, cmplx(0)) + v
    return clean_poly(out, tol)


def sub_poly(A: Poly, B: Poly, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    return add_poly(A, scale_poly(B, -1, tol), tol)


def scale_poly(A: Poly, c, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    return clean_poly({k: c * v for k, v in A.items()}, tol)


def mul_poly(A: Poly, B: Poly, max_deg: int, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    out: Poly = {}
    for (a1, b1), c1 in A.items():
        for (a2, b2), c2 in B.items():
            m = (a1 + a2, b1 + b2)
            if total_deg(m) <= max_deg:
                out[m] = out.get(m, cmplx(0)) + c1 * c2
    return clean_poly(out, tol)


def pow_poly(A: Poly, n: int, max_deg: int, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    if n == 0:
        return {(0, 0): cmplx(1)}
    out: Poly = {(0, 0): cmplx(1)}
    for _ in range(n):
        out = mul_poly(out, A, max_deg, tol)
    return clean_poly(out, tol)


def compose_poly(F: Poly, X: Poly, Y: Poly, max_deg: int, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    out: Poly = {}
    for (a, b), c in F.items():
        if a + b > max_deg:
            continue
        term = mul_poly(pow_poly(X, a, max_deg, tol), pow_poly(Y, b, max_deg, tol), max_deg, tol)
        term = scale_poly(term, c, tol)
        out = add_poly(out, term, tol)
    return clean_poly(out, tol)


def conj_poly(P: Poly, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    return clean_poly({(b, a): mp.conj(v) for (a, b), v in P.items()}, tol)


def coeff(P: Poly, a: int, b: int) -> mp.mpc:
    return P.get((a, b), cmplx(0))


def degree_part(P: Poly, deg: int) -> Poly:
    return {m: c for m, c in P.items() if total_deg(m) == deg}


def degree_leq(P: Poly, D: int) -> Poly:
    return {m: c for m, c in P.items() if total_deg(m) <= D}

# -----------------------------------------------------------------------------
# Series utilities
# -----------------------------------------------------------------------------

def sin_poly(P: Poly, max_deg: int, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    out: Poly = {}
    sign = 1
    for k in range(1, max_deg + 1, 2):
        term = scale_poly(pow_poly(P, k, max_deg, tol), mp.mpf(sign) / mp.factorial(k), tol)
        out = add_poly(out, term, tol)
        sign *= -1
    return clean_poly(out, tol)


def expm1_poly(P: Poly, max_deg: int, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    out: Poly = {}
    for k in range(1, max_deg + 1):
        out = add_poly(out, scale_poly(pow_poly(P, k, max_deg, tol), mp.mpf(1) / mp.factorial(k), tol), tol)
    return clean_poly(out, tol)

# -----------------------------------------------------------------------------
# General p resonance family
# -----------------------------------------------------------------------------

def p_constants(p: int):
    theta = 2 * mp.pi / p
    lam = mp.e ** (1j * theta)
    lamb = mp.conj(lam)
    K = 2 - 2 * mp.cos(theta)
    gamma = (lam - 1) / K
    gammab = (lamb - 1) / K
    return theta, lam, lamb, K, gamma, gammab


def rho_eta_from_W(P: Poly, Q: Poly, gamma, gammab, tol: mp.mpf = TOL_DEFAULT) -> tuple[Poly, Poly]:
    denom = gamma - gammab
    eta = scale_poly(sub_poly(P, Q, tol), 1 / denom, tol)
    rho = scale_poly(add_poly(scale_poly(Q, gamma, tol), scale_poly(P, -gammab, tol), tol), 1 / denom, tol)
    return clean_poly(rho, tol), clean_poly(eta, tol)


def one_step_map_p(p: int, D: int, tol: mp.mpf = TOL_DEFAULT) -> tuple[Poly, Poly]:
    _, lam, lamb, K, gamma, gammab = p_constants(p)
    P = {(1, 0): cmplx(1)}
    Q = {(0, 1): cmplx(1)}
    rho, eta = rho_eta_from_W(P, Q, gamma, gammab, tol)
    s = sin_poly(eta, D, tol)
    e = expm1_poly(rho, D, tol)
    rho1 = sub_poly(rho, s, tol)
    eta1 = add_poly(eta, scale_poly(e, K, tol), scale_poly(s, -K, tol), tol)
    W1 = add_poly(rho1, scale_poly(eta1, gamma, tol), tol)
    Wb1 = add_poly(rho1, scale_poly(eta1, gammab, tol), tol)
    return clean_poly(W1, tol), clean_poly(Wb1, tol)


def compose_maps(F: tuple[Poly, Poly], G: tuple[Poly, Poly], D: int, tol: mp.mpf = TOL_DEFAULT) -> tuple[Poly, Poly]:
    Fz, Fzb = F
    Gz, Gzb = G
    return compose_poly(Fz, Gz, Gzb, D, tol), compose_poly(Fzb, Gz, Gzb, D, tol)


def iterate_map(F: tuple[Poly, Poly], n: int, D: int, tol: mp.mpf = TOL_DEFAULT) -> tuple[Poly, Poly]:
    G = ({(1, 0): cmplx(1)}, {(0, 1): cmplx(1)})
    for _ in range(n):
        G = compose_maps(F, G, D, tol)
    return G


def resonant(a: int, b: int, p: int) -> bool:
    return ((a - b - 1) % p) == 0


def resonant_channels(p: int, D: int) -> list[tuple[int, int]]:
    out = []
    for deg in range(2, D + 1):
        for a in range(deg + 1):
            b = deg - a
            if resonant(a, b, p):
                out.append((a, b))
    return out


def proper_divisors(n: int) -> list[int]:
    return [d for d in range(2, n) if n % d == 0]


def subreturn_complexity(p: int, D: int, tol: mp.mpf = TOL_DEFAULT) -> tuple[int, int | None, dict[int, int]]:
    F = one_step_map_p(p, D, tol)
    _, lam, _, _, _, _ = p_constants(p)
    total = 0
    min_deg = None
    by_d: dict[int, int] = {}
    for d in proper_divisors(p):
        Fd = iterate_map(F, d, D, tol)
        Gz = scale_poly(Fd[0], lam ** (-d), tol)
        disp = sub_poly(Gz, {(1, 0): cmplx(1)}, tol)
        count = len(disp)
        by_d[d] = count
        total += count
        if disp:
            md = min(total_deg(m) for m in disp)
            min_deg = md if min_deg is None else min(min_deg, md)
    return total, min_deg, by_d

# -----------------------------------------------------------------------------
# Homological normalization
# -----------------------------------------------------------------------------

def normalize_one_step(F1: Poly, p: int, D: int, tol: mp.mpf = TOL_DEFAULT):
    """Return H, N, and per-degree h/n dictionaries for one-step homological normalization."""
    _, lam, _, _, _, _ = p_constants(p)
    H: Poly = {(1, 0): cmplx(1)}
    N: Poly = {(1, 0): lam}
    h_by_degree: dict[int, Poly] = {}
    n_by_degree: dict[int, Poly] = {}

    for k in range(2, D + 1):
        F_trunc = {m: c for m, c in F1.items() if total_deg(m) <= k}
        F_H = compose_poly(F_trunc, H, conj_poly(H, tol), k, tol)
        H_N = compose_poly(H, N, conj_poly(N, tol), k, tol)
        Efull = sub_poly(F_H, H_N, tol)
        Ek = degree_part(Efull, k)

        hk: Poly = {}
        nk: Poly = {}
        for (a, b), c in Ek.items():
            if resonant(a, b, p):
                nk[(a, b)] = nk.get((a, b), cmplx(0)) + c
            else:
                denom = lam - (lam ** a) * (mp.conj(lam) ** b)
                hk[(a, b)] = hk.get((a, b), cmplx(0)) - c / denom

        H = add_poly(H, hk, tol)
        N = add_poly(N, nk, tol)
        h_by_degree[k] = clean_poly(hk, tol)
        n_by_degree[k] = clean_poly(nk, tol)

    return H, N, h_by_degree, n_by_degree


def raw_p_step_displacement(p: int, D: int, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    F = one_step_map_p(p, D, tol)
    Fp = iterate_map(F, p, D, tol)
    return sub_poly(Fp[0], {(1, 0): cmplx(1)}, tol)


def normalized_accumulated_displacement(N: Poly, p: int, D: int, tol: mp.mpf = TOL_DEFAULT) -> Poly:
    F = (N, conj_poly(N, tol))
    Fp = iterate_map(F, p, D, tol)
    return sub_poly(Fp[0], {(1, 0): cmplx(1)}, tol)


def bridge_gap_metrics(raw_disp: Poly, f1_disp: Poly, channels: Iterable[Tuple[int, int]], tol: mp.mpf = TOL_DEFAULT):
    rows = []
    l2 = mp.mpf("0")
    max_abs = mp.mpf("0")
    max_channel = None
    nonzero = 0
    for ch in channels:
        gap = f1_disp.get(ch, cmplx(0)) - raw_disp.get(ch, cmplx(0))
        ag = abs(gap)
        if ag > tol:
            nonzero += 1
        l2 += ag ** 2
        if ag > max_abs:
            max_abs = ag
            max_channel = ch
        rows.append({
            "channel": ch,
            "raw": raw_disp.get(ch, cmplx(0)),
            "F1p": f1_disp.get(ch, cmplx(0)),
            "gap": gap,
            "abs_gap": ag,
        })
    return rows, mp.sqrt(l2), max_abs, max_channel, nonzero

# -----------------------------------------------------------------------------
# CLI operations
# -----------------------------------------------------------------------------

def run_p(p: int, D: int, tol: mp.mpf, out_dir: Path | None = None, quiet: bool = False):
    F_pair = one_step_map_p(p, D, tol)
    F1 = F_pair[0]
    H, N, h_by_deg, n_by_deg = normalize_one_step(F1, p, D, tol)
    raw_disp = raw_p_step_displacement(p, D, tol)
    f1_disp = normalized_accumulated_displacement(N, p, D, tol)
    channels = resonant_channels(p, D)
    gap_rows, gap_l2, gap_max, gap_ch, gap_nonzero = bridge_gap_metrics(raw_disp, f1_disp, channels, tol)
    C_sub, sub_min_deg, sub_by_d = subreturn_complexity(p, D, tol)

    _, lam, _, K, gamma, _ = p_constants(p)
    summary = {
        "p": p,
        "D": D,
        "prime": len(proper_divisors(p)) == 0,
        "divisors": proper_divisors(p),
        "proper_divisor_count": len(proper_divisors(p)),
        "K": K,
        "lambda": lam,
        "gamma": gamma,
        "resonant_channels": channels,
        "raw_res_count": sum(1 for ch in channels if abs(raw_disp.get(ch, cmplx(0))) > tol),
        "F1p_res_count": sum(1 for ch in channels if abs(f1_disp.get(ch, cmplx(0))) > tol),
        "gap_nonzero_res_count": gap_nonzero,
        "bridge_gap_l2": gap_l2,
        "bridge_gap_max": gap_max,
        "bridge_gap_max_channel": gap_ch,
        "sub_complexity": C_sub,
        "sub_min_degree": sub_min_deg,
        "sub_by_d": sub_by_d,
    }

    if not quiet:
        sep = "=" * 80
        print(f"\n{sep}\np={p}, D={D}, divisors={summary['divisors']}\n{sep}")
        print(f"K_p={fmt(K, 16)} lambda={fmt(lam, 16)} gamma={fmt(gamma, 16)}")
        print(f"resonant_channels={channels}")
        print(f"sub_complexity={C_sub}, sub_min_degree={sub_min_deg}, sub_by_d={sub_by_d}")
        print(f"bridge_gap_l2={fmt(gap_l2, 20)}, bridge_gap_max={fmt(gap_max, 20)}, channel={gap_ch}")
        print("channel gaps:")
        for r in gap_rows:
            print(f"  {r['channel']}: gap={fmt(r['gap'], 24)} |abs|={fmt(r['abs_gap'], 12)}")

    if out_dir is not None:
        out_dir.mkdir(parents=True, exist_ok=True)
        export = {
            "metadata": {
                "type": "one_step_homological_normalization",
                "source": "homological_solver_p_general_numeric.py",
                "p": p,
                "D": D,
                "dps": int(mp.mp.dps),
                "meaning": "Phi1 and N_p for generalized RTG resonance family; p-fold N_p gives F1^p, not raw p-step normalized object.",
            },
            "raw_one_step_z": poly_to_jsonable(F1),
            "Phi1": poly_to_jsonable(H),
            "N_one_step": poly_to_jsonable(N),
            "h_by_degree": {str(k): poly_to_jsonable(v) for k, v in h_by_deg.items()},
            "n_by_degree": {str(k): poly_to_jsonable(v) for k, v in n_by_deg.items()},
            "raw_p_step_disp_z": poly_to_jsonable(raw_disp),
            "F1p_disp_z": poly_to_jsonable(f1_disp),
            "bridge_gap_channels": [
                {
                    "channel": str(r["channel"]),
                    "raw": {"re": mp.nstr(mp.re(r["raw"]), 80), "im": mp.nstr(mp.im(r["raw"]), 80)},
                    "F1p": {"re": mp.nstr(mp.re(r["F1p"]), 80), "im": mp.nstr(mp.im(r["F1p"]), 80)},
                    "gap": {"re": mp.nstr(mp.re(r["gap"]), 80), "im": mp.nstr(mp.im(r["gap"]), 80)},
                    "abs_gap": mp.nstr(r["abs_gap"], 80),
                }
                for r in gap_rows
            ],
            "summary": {
                "bridge_gap_l2": mp.nstr(gap_l2, 80),
                "bridge_gap_max": mp.nstr(gap_max, 80),
                "bridge_gap_max_channel": str(gap_ch),
                "gap_nonzero_res_count": gap_nonzero,
                "sub_complexity": C_sub,
                "sub_min_degree": sub_min_deg,
                "sub_by_d": sub_by_d,
            },
        }
        with (out_dir / f"phi1_p{p}_D{D}.json").open("w", encoding="utf-8") as f:
            json.dump(export, f, indent=2)

    return summary


def write_summary_csv(path: Path, summaries: list[dict]):
    with path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "p", "D", "prime", "proper_divisor_count", "divisors", "raw_res_count",
            "F1p_res_count", "gap_nonzero_res_count", "bridge_gap_l2", "bridge_gap_max",
            "bridge_gap_max_channel", "sub_complexity", "sub_min_degree", "sub_by_d",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for s in summaries:
            w.writerow({
                "p": s["p"],
                "D": s["D"],
                "prime": s["prime"],
                "proper_divisor_count": s["proper_divisor_count"],
                "divisors": " ".join(map(str, s["divisors"])),
                "raw_res_count": s["raw_res_count"],
                "F1p_res_count": s["F1p_res_count"],
                "gap_nonzero_res_count": s["gap_nonzero_res_count"],
                "bridge_gap_l2": mp.nstr(s["bridge_gap_l2"], 30),
                "bridge_gap_max": mp.nstr(s["bridge_gap_max"], 30),
                "bridge_gap_max_channel": str(s["bridge_gap_max_channel"]),
                "sub_complexity": s["sub_complexity"],
                "sub_min_degree": s["sub_min_degree"],
                "sub_by_d": str(s["sub_by_d"]),
            })


def write_summary_md(path: Path, summaries: list[dict]):
    lines = []
    lines.append("| p | prime | divisors | C_sub | bridge_gap_l2 | bridge_gap_max | max channel |")
    lines.append("|---:|:---:|---|---:|---:|---:|---|")
    for s in summaries:
        lines.append(
            f"| {s['p']} | {str(s['prime']).lower()} | {s['divisors']} | {s['sub_complexity']} | "
            f"{mp.nstr(s['bridge_gap_l2'], 12)} | {mp.nstr(s['bridge_gap_max'], 12)} | {s['bridge_gap_max_channel']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="General RTG p-homological solver and bridge-gap auditor.")
    parser.add_argument("--p", type=int, nargs="*", default=[5, 6, 7, 8])
    parser.add_argument("--D", type=int, default=5)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--tol", type=str, default="1e-50")
    parser.add_argument("--out-dir", type=str, default="")
    parser.add_argument("--summary-csv", type=str, default="")
    parser.add_argument("--summary-md", type=str, default="")
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
