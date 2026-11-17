#!/usr/bin/env python3
"""
dzt_casev_norm_from_closed_form.py

DZT closed-form Case-V amplitude-norm audit.

Uses the Dyadic-imported closed form for the q=4,(0,3) cascade:
    Q(L,I) = L^5( I L^2 + I - L^2 + 1 ) / ( 2 (L+1)^4 (L^2+L+1) )
with L = zeta_p, I = L^(p/4) = i, p = 4s, s >= 2.

DZT object:
    M_p = Q_p / (i zeta_p^3) in Q(zeta_p)^+
    N_+(M_p) = N_{Q(zeta_p)^+/Q}(M_p)

This script computes the norm directly from the closed form using cyclotomic
resultants. It does not rely on transcribed Q_p polynomials.

Method:
    M = unit * A / [2 (L+1)^4 (L^2+L+1)]
    A = I L^2 + I - L^2 + 1 = L^(s+2) + L^s - L^2 + 1

    N_full = N_{Q(zeta_p)/Q}(M)
           = Res(Phi_p, A) / [2^phi(p) Res(Phi_p,L+1)^4 Res(Phi_p,L^2+L+1)]

    Since M is real under the imported Dyadic theorem, N_full = N_+(M)^2.
    Thus N_+(M) = sqrt(abs(N_full)).

Tags intended for DSN:
    [ALG finite horizon] for audited p-ranges.
    [HEUR diagnostic] for pattern observations.
    [FAIL] already established for universal support-on-2 via p=40.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass

import sympy as sp

z = sp.symbols("z")


@dataclass
class NormRow:
    p: int
    s: int
    phi: int
    half_degree: int
    n_plus: sp.Rational | sp.Integer
    is_2_power: bool
    numerator_factor: dict
    denominator_factor: dict
    anomaly: bool


def is_power_of_two_int(n: int) -> bool:
    n = abs(int(n))
    return n == 0 or (n > 0 and (n & (n - 1)) == 0)


def is_pure_2_power_rat(r) -> bool:
    r = sp.Rational(r)
    num, den = sp.fraction(r)
    return is_power_of_two_int(num) and is_power_of_two_int(den)


def exact_sqrt_abs_rational(q):
    """Exact sqrt(abs(q)) for rational q known to be a square."""
    q = sp.Rational(q)
    if q == 0:
        return sp.Integer(0)
    num, den = sp.fraction(abs(q))
    num_fac = sp.factorint(abs(int(num)))
    den_fac = sp.factorint(abs(int(den)))
    if any(e % 2 for e in num_fac.values()) or any(e % 2 for e in den_fac.values()):
        raise ArithmeticError(f"N_full is not a rational square: {q}")
    nroot = 1
    droot = 1
    for prime, exp in num_fac.items():
        nroot *= prime ** (exp // 2)
    for prime, exp in den_fac.items():
        droot *= prime ** (exp // 2)
    return sp.Rational(nroot, droot)


def norm_plus_from_closed_form(p: int):
    if p % 4 != 0 or p < 8:
        raise ValueError(f"p must be 4s with s>=2; got p={p}")

    Phi = sp.Poly(sp.cyclotomic_poly(p, z), z, domain=sp.QQ)
    phi = int(sp.totient(p))
    s = p // 4

    # A = I L^2 + I - L^2 + 1 with I=L^s.
    A = z ** (s + 2) + z ** s - z ** 2 + 1

    # Full norm of M. Unit factors L^2/I do not affect absolute norm.
    res_A = sp.resultant(Phi.as_expr(), A, z)
    res_Lp1 = sp.resultant(Phi.as_expr(), z + 1, z)
    res_tri = sp.resultant(Phi.as_expr(), z ** 2 + z + 1, z)

    n_full = sp.factor(
        sp.Rational(res_A, (2 ** phi) * (res_Lp1 ** 4) * res_tri)
    )
    n_plus = sp.factor(exact_sqrt_abs_rational(n_full))
    return n_full, n_plus, res_A, res_Lp1, res_tri


def audit_range(max_p: int, start_p: int = 8) -> list[NormRow]:
    rows: list[NormRow] = []
    for p in range(start_p, max_p + 1, 4):
        n_full, n_plus, _, _, _ = norm_plus_from_closed_form(p)
        is2 = is_pure_2_power_rat(n_plus)
        num, den = sp.fraction(sp.Rational(n_plus))
        num_fac = sp.factorint(abs(int(num))) if n_plus != 0 else {}
        den_fac = sp.factorint(abs(int(den))) if n_plus != 0 else {}
        rows.append(
            NormRow(
                p=p,
                s=p // 4,
                phi=int(sp.totient(p)),
                half_degree=int(sp.totient(p)) // 2,
                n_plus=n_plus,
                is_2_power=is2,
                numerator_factor=num_fac,
                denominator_factor=den_fac,
                anomaly=(not is2),
            )
        )
    return rows


def write_csv(rows: list[NormRow], path: str):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "p", "s", "phi", "phi_over_2", "N_plus", "is_2_power",
            "numerator_factor", "denominator_factor", "anomaly"
        ])
        for r in rows:
            w.writerow([
                r.p, r.s, r.phi, r.half_degree, str(r.n_plus), r.is_2_power,
                str(r.numerator_factor), str(r.denominator_factor), r.anomaly
            ])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-p", type=int, default=200)
    ap.add_argument("--start-p", type=int, default=8)
    ap.add_argument("--csv", default="")
    ap.add_argument(
        "--fail-on-odd",
        action="store_true",
        help="Exit 1 if any non-2-power norm appears.",
    )
    args = ap.parse_args(argv)

    rows = audit_range(args.max_p, args.start_p)

    print(f"{'p':>5} {'s':>5} {'phi/2':>7} {'N_+':>24} {'2pow':>6} {'numfac':>18} {'denfac':>18}")
    for r in rows:
        marker = "N" if r.anomaly else "Y"
        print(
            f"{r.p:>5} {r.s:>5} {r.half_degree:>7} {str(r.n_plus):>24} "
            f"{marker:>6} {str(r.numerator_factor):>18} {str(r.denominator_factor):>18}"
        )

    anomalies = [r for r in rows if r.anomaly]
    print("\nSUMMARY:")
    print(f"  audited points: {len(rows)}")
    print(f"  anomalies     : {len(anomalies)}")
    if anomalies:
        print("  anomaly p-values:")
        for r in anomalies:
            print(f"    p={r.p}: N_+={r.n_plus}, numerator={r.numerator_factor}, denominator={r.denominator_factor}")
    else:
        print("  no odd-prime anomalies in audited range")

    # Observed diagnostic, not theorem:
    pp_anoms = []
    for r in anomalies:
        q = r.p // 8
        fac = sp.factorint(q) if q > 0 else {}
        if len(fac) == 1:
            ell = next(iter(fac))
            pp_anoms.append((r.p, q, ell))
    if anomalies and len(pp_anoms) == len(anomalies):
        print("\nHEUR diagnostic:")
        print("  In this audited range, every anomaly has p=8*q with q an odd prime power.")
        print("  The odd numerator is ell^2 where q=ell^a. This is an observed pattern only.")

    if args.csv:
        write_csv(rows, args.csv)
        print(f"\nCSV written: {args.csv}")

    return 1 if (args.fail_on_odd and anomalies) else 0


if __name__ == "__main__":
    raise SystemExit(main())
