#!/usr/bin/env python3
"""Exact finite algebra for the Lopez-Hernanz (2012) -> DYAD hypothesis map.
Independent real-coordinate Fraction composition through degree 5; SymPy is
used only for exact coordinate conversion and field identities. This checks
finite input identities, not the infinite-order summability theorem.
Exit 0: gates pass; 1: an intentional or unintentional gate failure; 3: crash.
"""
from fractions import Fraction as Q
from math import factorial
import argparse
import json
from pathlib import Path
import sys
import sympy as s

D = 5

def add(p, q, sign=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, Q(0)) + sign * v
    return {k: v for k, v in r.items() if v}

def mul(p, q):
    r = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            if i+j+k+l <= D:
                m = (i+k, j+l)
                r[m] = r.get(m, Q(0)) + a*b
    return {k: v for k, v in r.items() if v}

def fun(p, coeff):
    r, power = {}, {(0, 0): Q(1)}
    for n in range(D+1):
        if n:
            power = mul(power, p)
        if coeff[n]:
            r = add(r, {k: coeff[n]*v for k, v in power.items()})
    return r

def step(r, e):
    sn = fun(e, [Q(0) if n % 2 == 0 else Q((-1)**(n//2), factorial(n)) for n in range(D+1)])
    ex = fun(r, [Q(0)] + [Q(1, factorial(n)) for n in range(1, D+1)])
    return add(r, sn, -1), add(add(e, ex), sn, -1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--negative', choices=['ratio', 'branch', 'coefficient'])
    ap.add_argument('--out', default='transfer_checks.json')
    args = ap.parse_args()
    r0, e0 = {(1, 0): Q(1)}, {(0, 1): Q(1)}
    r1, e1 = step(r0, e0)
    r, e = r0, e0
    for _ in range(6):
        r, e = step(r, e)
    z, w, a, u = s.symbols('z w a u')
    om = s.I*s.sqrt(3)
    omega = (-1+om)/2
    lam = (1+om)/2
    rho = ((3-om)*z+(3+om)*w)/6
    eta = (z-w)/om
    def expr(p):
        return s.expand(sum(s.Rational(v.numerator,v.denominator)*rho**i*eta**j for (i,j),v in p.items()))
    fz = s.Poly(s.expand(expr(r)+omega*expr(e)), z, w, extension=om)
    fw = s.Poly(s.expand(expr(r)+s.conjugate(omega)*expr(e)), z, w, extension=om)
    tw = s.Poly(s.expand(expr(r1)+s.conjugate(omega)*expr(e1)), z, w, extension=om)
    mu = -s.Rational(1,2)-2*om/3
    c40 = -s.Rational(1,16)+7*om/144
    d31 = s.Rational(1,3)-om/9
    C = -s.Rational(61,2160)+43*om/6480
    A = s.conjugate(mu)-2*mu
    B = d31-2*c40
    P = s.expand(A*a*a+B*a+C)
    ell = c40+mu*a
    ks = -s.Rational(64,19)-16*om/19
    alpha = ks-2
    def zero(v):
        return s.simplify(s.expand(v)) == 0
    def rem(v):
        return s.Poly(s.expand(v),a,extension=om).rem(s.Poly(P,a,extension=om)).as_expr()
    gates = {}
    for name, poly, expected_linear in [('z', fz, z), ('w', fw, w)]:
        low = sum(c*z**i*w**j for (i,j),c in poly.terms() if i+j<=2)
        gates['linear_quadratic_'+name] = zero(low-expected_linear)
    expected_c40 = c40+(1 if args.negative=='coefficient' else 0)
    gates['raw_coefficients'] = all([
        zero(fz.coeff_monomial(z**2*w)-mu),
        zero(fw.coeff_monomial(z*w**2)-s.conjugate(mu)),
        zero(fz.coeff_monomial(z**4)-expected_c40),
        zero(fw.coeff_monomial(z**3*w)-d31),
        zero(fw.coeff_monomial(z**5)-C)])
    # Higher total degree >=6 automatically has weighted order >=6.
    dz, dw = s.Poly(fz.as_expr()-z,z,w), s.Poly(fw.as_expr()-w,z,w)
    gates['weighted_divisibility'] = (
        all(i+2*j>=4 for (i,j),c in dz.terms() if c) and
        all(i+2*j>=5 for (i,j),c in dw.terms() if c))
    g0 = c40+mu*u
    h0 = C+d31*u+s.conjugate(mu)*u*u
    gates['exceptional_polynomial'] = zero((h0-2*u*g0).subs(u,a)-P)
    alpha_checked = alpha+(1 if args.negative=='ratio' else 0)
    gates['BB_ratio_for_both_roots'] = zero(rem(s.diff(P,a)-alpha_checked*ell))
    # ell is a unit in the quadratic field, checked by a nonzero constant norm.
    suma = s.simplify(-B/A)
    ell_product = zero(rem(ell*(c40+mu*(suma-a))))
    gates['nonzero_ell'] = not ell_product
    gates['opposite_ell'] = zero(2*c40+mu*suma)
    ta = s.simplify((s.conjugate(lam)*a+tw.coeff_monomial(z**2))/lam**2)
    expected_ta = (1+om)/12-a
    if args.negative=='branch':
        expected_ta = a
    gates['T_exchanges_a2'] = zero(ta-expected_ta) and zero(rem(P.subs(a,ta)))
    result = {'scope':'finite exact hypothesis-map identities; not a summability proof',
              'degree':D, 'gates':gates,'all_pass':all(gates.values()),
              'alpha':s.sstr(alpha),'k':3,
              'a2_sum':s.sstr(s.simplify(suma)),
              'primitive_T_a2_action':s.sstr(s.simplify(ta)),
              'exceptional_polynomial':s.sstr(P)}
    Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result['all_pass'] else 1

if __name__=='__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print('CRASH',type(exc).__name__,str(exc),file=sys.stderr)
        sys.exit(3)
