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



def raw_sup(radius):
    """Uniform upper bound on |F_z| and |F_w| for |z|,|w|<=radius.

    The inverse frame has coefficients of modulus 1/sqrt(3), so initially
    |rho|, |eta| <= 2*radius/sqrt(3). Each sixfold step is majorized by
    r_new=r+exp(t)-1, t_new=t+(exp(r)-1)+(exp(t)-1).
    """
    r = u(2 * radius / iv.sqrt(3))
    t = r
    for _ in range(6):
        er, et = sinh_upper(r), sinh_upper(t)
        r, t = u(r + et), u(t + er + et)
    return u(r + t)


def geometric_tail(q, n):
    """Sum_{d>=n} (d+1)q**d, with upper bounds, 0<=q<1."""
    if not certain_lt(q, cf(1)):
        raise ValueError('Cauchy radius ratio must be below one')
    return u(q ** n * (n + 1 - n * q) / (1 - q) ** 2)


def weighted_tail(q, n):
    """Conservative bound on Sum_{d>=n} d(d+1)q**d."""
    if not certain_lt(q, cf(1)):
        raise ValueError('Cauchy radius ratio must be below one')
    return u(q ** n * (n * (n + 1) / (1 - q) ** 2 +
                       2 * (n + 1) * q / (1 - q) ** 3))


def jet_majorants(d, z, v, raw_R, sup_diff, njet=7):
    """Absolute analytic bound for J_d(z,v)=(F_component(z,z^2*v)-linear)/z^d,
    and the partial derivatives in (z,v). The exact Stage-1 S3 zero gates
    prove that every excluded monomial (p+2q<d) has coefficient zero.

    The global Cauchy estimate is |c_pq| <= sup_diff/raw_R**(p+q).
    No Taylor polynomial is substituted for the actual analytic function.
    """
    j, dz, dv = cf(0), cf(0), cf(0)
    for n in range(3, njet + 1):
        cb = u(sup_diff / raw_R ** n)
        for q in range(n + 1):
            p = n - q
            power = p + 2 * q - d
            if power < 0:
                continue  # exact vanishing certified by Stage-1 gate S3
            mono = u(cb * z ** power * v ** q)
            j = u(j + mono)
            if power > 0:
                dz = u(dz + cb * power * z ** (power - 1) * v ** q)
            if q > 0:
                dv = u(dv + cb * q * z ** power * v ** (q - 1))
    ratio = imax(u(z / raw_R), u(z * z * v / raw_R))
    tail = geometric_tail(ratio, njet + 1)
    wt = weighted_tail(ratio, njet + 1)
    j = u(j + sup_diff * tail / z ** d)
    dz = u(dz + 2 * sup_diff * wt / z ** (d + 1))
    dv = u(dv + sup_diff * wt / (z ** d * v))
    return j, dz, dv


def inverse_branch_bounds(raw_R, inverse_R, sup_diff):
    q = u(inverse_R / raw_R)
    residual = u(sup_diff * geometric_tail(q, 3))
    jac = u(sup_diff / raw_R * weighted_tail(q, 3))
    feasible = certain_lt(jac, cf(1)) and certain_lt(residual, inverse_R)
    target = inverse_R - residual if feasible else cf(0)
    return {'contractive': feasible, 'displacement_upper': upper_decimal(residual),
            'jacobian_row_sum_upper': upper_decimal(jac),
            'target_bidisc_radius_lower': None if not feasible else lower_decimal(target),
            'warning': 'Target radius rounded downward from a validated interval; normalized inverse bounds not established.'}


def interval_constants():
    """Enclose a_pil, c, b1, alpha via exact algebraic defining relations."""
    I = iv.j
    root3 = iv.sqrt(3)
    MU = -cf('0.5') - cf(2) / 3 * I * root3
    C40 = -cf(1) / 16 + cf(7) / 144 * I * root3
    D31 = cf(1) / 3 - I * root3 / 9
    CC = -cf(61) / 2160 + cf(43) / 6480 * I * root3
    A = iv.mpc(MU.real, -MU.imag) - 2 * MU
    B = D31 - 2 * C40
    discr = B ** 2 - 4 * A * CC
    # Main-stage root has Im(discriminant)>0; construct principal sqrt
    dr, di = discr.real, discr.imag
    dabs = iv.sqrt(dr * dr + di * di)
    dsqrt = iv.mpc(iv.sqrt((dabs + dr) / 2), iv.sqrt((dabs - dr) / 2))
    a = (-B - dsqrt) / (2 * A)
    ell = C40 + MU * a
    c = iv.exp(iv.log(-ell) / 3)  # principal cube root, |arg(-ell)| < pi
    b1 = (1 - I * root3) * (cf(1) / 108 - a / 6)
    alpha = -cf(102) / 19 - cf(16) / 19 * I * root3
    if not certain_gt(a.imag, cf(0)):
        raise ValueError('selected root does not have positive imaginary part')
    if not certain_gt(abs(c), cf(0)):
        raise ValueError('horizontal rescaling not invertible')
    return a, b1, c, alpha


def stage1_source(path):
    p = Path(path)
    data = p.read_bytes()
    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != STAGE1_JSON_SHA256:
        raise ValueError('Stage-1 evidence SHA-256 does not match the pinned owner artifact')
    obj = json.loads(data.decode('utf-8'))
    expected = ['S1', 'S2', 'S3_div', 'S3_order', 'S4', 'S5_comp', 'S5_form', 'S6', 'S7']
    if obj.get('all_pass') is not True or any(obj.get('gates', {}).get(k) is not True for k in expected):
        raise ValueError('stage1 exact zero/normalization gates not all PASS')
    if obj.get('k') != 3 or obj.get('m') != 2:
        raise ValueError('unexpected k, m in Stage-1 certificate')
    if obj.get('alpha') != '(-102/19 + -16/19*i*sqrt3)':
        raise ValueError('unexpected exact alpha in Stage-1 certificate')
    return actual_sha256


def derive_bounds(params):
    a, b1, c, alpha = interval_constants()
    Rraw = cf(params['raw_cauchy_radius'])
    Rx = cf(params['outer_xi_radius'])
    Ry = cf(params['outer_Y_radius'])
    rx = cf(params['inner_xi_radius'])
    ry = cf(params['inner_Y_radius'])
    ri = cf(params['raw_inverse_radius'])
    if not (certain_gt(Rx, rx) and certain_gt(Ry, ry) and certain_gt(rx, cf(0)) and certain_gt(ry, cf(0))):
        raise ValueError('inner polydisc must be strictly inside outer normalized polydisc')
    M = raw_sup(Rraw)
    raw_diff = u(M + Rraw)
    inverse = inverse_branch_bounds(Rraw, ri, raw_diff)
