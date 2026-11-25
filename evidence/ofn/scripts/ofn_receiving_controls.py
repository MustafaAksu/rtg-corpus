#!/usr/bin/env python3
"""OFN receiving-pass SESSION controls, 2026-11-24.

Exact algebraic controls only. No TDR-G engine or recovered FMS producer
script is executed. The synthetic elimination ideal is a control for the
P4 success predicate, not the actual FMS ideal or a refutation of P4.
"""
from collections import Counter
from itertools import combinations
import sympy as sp


def require(ok, label):
    if not ok:
        raise AssertionError(label)
    print(label + ': PASS')


def spectrum(tokens, n):
    return sorted(min((x-y) % n, (y-x) % n) for x, y in combinations(tokens, 2))


# TDR-G v2.13, TOKEN-CENSUS-LAW and BIRTH-SPECTRUM-INJECTION.
# Conditional on the selected centre token(s); not an engine fixture.
N = 24
C = [1, 3, 4, 5]
D0 = spectrum(C, N)
outputs = []
for x in (1, 3):
    successor = C + [(-x) % N]
    c, c_next = Counter(C), Counter(successor)
    b = Counter([x])
    recovered = {y: c_next[(-y) % N]-c[(-y) % N] for y in range(N)}
    require(all(recovered[y] == b[y] for y in range(N)), f'Census interface inverse, centre={x}')
    ds = spectrum(successor, N)
    injection = sorted(D0 + [min((x+y) % N, (-x-y) % N) for y in C])
    require(ds == injection, f'Spectrum injection, centre={x}')
    outputs.append(ds)
    print(f'  next spectrum = {ds}')
require(outputs[0] != outputs[1], 'Same input census, different prescribed centre tokens, different output spectra')

# Exact predicate used in FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1.py,
# line 349 at blob 6af53f0a254727c328b434e2f8470eb3563e96da.
r, T = sp.symbols('r T', real=True)
fixed = sp.expand(sp.Rational(19, 12)*r-sp.Rational(17, 648)*sp.sqrt(3)-sp.sqrt(3)*T/9)


def source_predicate(el):
    return len(el) > 0 and all(
        sp.rem(sp.expand(sp.numer(sp.together(g))),
               sp.expand(fixed*sp.Rational(12, 19)*1026), r) == 0
        or sp.simplify(sp.numer(sp.together(g))/fixed).is_number
        for g in el)


def membership(el):
    G = sp.groebner(el, r, T, domain=sp.QQ.algebraic_field(sp.sqrt(3), sp.I))
    return sp.expand(G.reduce(fixed)[1]) == 0


bad = sp.expand(fixed*(r-1))
require(source_predicate([bad]), 'P4 predicate accepts synthetic product ideal')
require(not membership([bad]), 'Ideal-membership test rejects synthetic product ideal')
require(sp.simplify(bad.subs({r: 1, T: 0})) == 0 and sp.simplify(fixed.subs({r: 1, T: 0})) != 0,
        'Extra solution branch in synthetic control')
require(source_predicate([fixed]) and membership([fixed]), 'Linear-ideal positive control')
print('RESULT: PASS (SESSION controls only; actual FMS P4 not executed)')
