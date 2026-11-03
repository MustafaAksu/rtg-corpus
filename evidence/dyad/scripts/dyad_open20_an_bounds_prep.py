#!/usr/bin/env python3
"""DYAD OPEN20: bounded analytic-envelope PREPARATION, not a Stage-3 campaign.

Uses the ENTIRE primitive T, not a Taylor truncation, for dynamics. Builds
conservative Cauchy coefficient majorants for F=T^6, the exact lift, and the
forward normalized map using the exact-jet vanishing facts of Stage 1 S1--S7.
Arithmetic of scalar bounds uses mpmath.iv (directed interval arithmetic).
Output is intentionally NOT_CERTIFIED for Stage 3: inverse normalized maps,
E6 fixed-point residuals, E7 transported jumps and all owner dispositions
remain unproved. No sampled orbit can change that status.

Commands (run from repository root; Windows PowerShell):
  python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --self-test
  python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --out prep.json
  python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --control wrong-alpha

Requires: python -m pip install mpmath
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

from mpmath import iv, mp

iv.dps = 75
mp.dps = 80

# Source-reported exact artifact pin, from DYAD's adopted Stage-1 design §7.
STAGE1_JSON_SHA256 = '2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739'


# This is the adopted raw primitive in the lifted analytic complexification.
# rho, eta are complex-independent on the source bidisc; z and w are not conjugate.

def primitive(rho, eta, ctx):
    sine = ctx.sin(eta)
    return rho - sine, eta + ctx.exp(rho) - 1 - sine


def full_map(z, w, ctx):
    omega = (-1 + ctx.j * ctx.sqrt(3)) / 2
    ombar = (-1 - ctx.j * ctx.sqrt(3)) / 2
    den = omega - ombar
    rho = (-ombar * z + omega * w) / den
    eta = (z - w) / den
    for _ in range(6):
        rho, eta = primitive(rho, eta, ctx)
    return rho + omega * eta, rho + ombar * eta


def frac_hi(x):
    """Exact rational representation of binary upper endpoint (nonnegative)."""
    raw = x._mpi_[1]
    sign, mant, exp, _ = raw
    q = Fraction(-mant if sign else mant, 1)
    return q * (2 ** exp) if exp >= 0 else q / (2 ** (-exp))


def _scientific(q, digits, is_upper):
    """Safely round exact rational endpoint to significant decimal digits."""
    if q < 0:
        raise ValueError('expected nonnegative magnitude')
    if q == 0:
        return '0'
    exponent = len(str(q.numerator)) - len(str(q.denominator))
    def pow10(n):
        return Fraction(10 ** n, 1) if n >= 0 else Fraction(1, 10 ** (-n))
    while q < pow10(exponent):
        exponent -= 1
    while q >= pow10(exponent + 1):
        exponent += 1
    places = digits - 1 - exponent
    scaled = q * pow10(places)
    if is_upper:
        n = (scaled.numerator + scaled.denominator - 1) // scaled.denominator
    else:
        n = scaled.numerator // scaled.denominator
    with localcontext() as ctx:
        ctx.prec = digits + 20
        value = Decimal(n).scaleb(-places)
        return format(value.normalize(), 'E')


def upper_decimal(x, digits=32):
    return _scientific(frac_hi(x), digits, True)


def lower_decimal(x, digits=32):
    raw = x._mpi_[0]
    sign, mant, exp, _ = raw
    q = Fraction(-mant if sign else mant, 1)
    q = q * (2 ** exp) if exp >= 0 else q / (2 ** (-exp))
    return _scientific(q, digits, False)


def u(x):
    return x.b


def certain_lt(x, y):
    return bool(x.b < y.a)


def certain_gt(x, y):
    return bool(x.a > y.b)


def imax(a, b):
    return a if certain_gt(a, b) else b if certain_gt(b, a) else a + b


def cf(x):
    return iv.mpf(str(x))


def sinh_upper(x):
    # |sin z| <= sinh(|z|) <= exp(|z|)-1; use the latter as monotone envelope.
    return u(iv.exp(x) - 1)


