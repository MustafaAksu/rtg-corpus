#!/usr/bin/env python3
"""Exact cubic-jet and finite type-logic checks for the SESSION channel carrier.
No trajectory, seed search, campaign, physical admission or M2 verdict.
"""
from fractions import Fraction as F
from itertools import product

Z = (F(0),) * 4


def add(*p):
    return tuple(sum(v) for v in zip(*p))


def scale(p, k):
    return tuple(k * a for a in p)


def mul(p, q):
    return tuple(sum(p[i] * q[d-i] for i in range(d+1)) for d in range(4))


def poly(*c):
    return tuple(F(v) for v in (0,) + c) + (F(0),) * (3-len(c))


def sin3(p):
    return add(p, scale(mul(mul(p, p), p), -F(1, 6)))


def expm1_3(p):
    return add(p, scale(mul(p, p), F(1, 2)), scale(mul(mul(p, p), p), F(1, 6)))


def T(x):
    r, e = x
    sn = sin3(e)
    return add(r, scale(sn, -1)), add(e, expm1_3(r), scale(sn, -1))


def observable(x, key):
    r, e = x
    if key == "P":
        return e
    if key == "M":
        return r
    return add(expm1_3(r), scale(sin3(e), -1))


def leading(p):
    return next((d, c) for d, c in enumerate(p) if c)


# Exact zero-curve jets, parameter t>0; ordered by limiting W-angle.
# h=0: eta=arcsin(exp(rho)-1)=rho+rho^2/2+rho^3/3+O(rho^4).
rays = [
    ("P+", "P", (poly(1), Z)),
    ("H-", "H", (poly(1), poly(1, F(1, 2), F(1, 3)))),
    ("M-", "M", (Z, poly(1))),
    ("P-", "P", (poly(-1), Z)),
    ("H+", "H", (poly(-1), poly(-1, F(1, 2), -F(1, 3)))),
    ("M+", "M", (Z, poly(-1))),
]
# Expected leading terms (degree, coefficient), columns k=1..5.
# All cubic coefficients are nonzero, with magnitude <4/3.
expected = [
    [(3,F(1,6)), (2,-F(1,2)), (2,-F(1,2)), (2,F(1,2)), (3,-F(7,6))],
    [(2,-F(1,2)), (2,-F(1,2)), (2,F(1,2)), (3,-F(1)), (3,-F(7,6))],
    [(3,F(1,6)), (3,-F(1,3)), (2,-F(1,2)), (2,-F(1,2)), (2,F(1,2))],
    [(3,-F(1,6)), (2,-F(1,2)), (2,-F(1,2)), (2,F(1,2)), (3,F(7,6))],
    [(2,-F(1,2)), (2,-F(1,2)), (2,F(1,2)), (3,F(1)), (3,F(7,6))],
    [(3,-F(1,6)), (3,F(1,3)), (2,-F(1,2)), (2,-F(1,2)), (2,F(1,2))],
]
for i, (name, key, x) in enumerate(rays):
    assert observable(x, key) == Z
    row = []
    for k in range(1, 6):
        x = T(x)
        target, key2, _ = rays[(i+k) % 6]
        d, c = leading(observable(x, key2))
        assert (d,c) == expected[i][k-1]
        assert d in (2,3) and c != 0
        if d == 3:
            assert abs(c) < F(4,3)
        row.append(f"{target}:{c}*t^{d}")
    print(name, " ".join(row))
print("JET PASS: 30/30 nonzero leading coefficients; cubic magnitudes <4/3")

# Abstract type logic: channel separation is imposed before any label test.
# Physical event admission is a hypothesis, not checked by this enumeration.
events = list(product(("P","M","H"), ("up","down","both")))


def key(e):
    return e[0], "both" if e[1] == "both" else "one"


def pair_key(p):
    return key(p[0]), key(p[1])


def pairs_ok(p):
    return p[0][0] != p[1][0]


def compatible(x, y):
    return key(x[1]) == key(y[0]) and x[0][0] != y[1][0]


def multiplicity(e):
    # Derived from the one-per-directed-ray count theorem, not used for typing.
    return 2 if e[1] == "both" else 1


def label(p):
    return F(multiplicity(p[0]), multiplicity(p[1]))


pairs = [p for p in product(events, repeat=2) if pairs_ok(p)]
fibres = {}
for p in pairs:
    fibres.setdefault(pair_key(p), []).append(p)
assert len(pairs) == 54 and len(fibres) == 24
nchains = nchecks = 0
for x, y in product(pairs, repeat=2):
    if not compatible(x,y):
        continue
    nchains += 1
    z = x[0], y[1]
    assert z in pairs
    assert label(z) == label(x)*label(y)
    for xp, yp in product(fibres[pair_key(x)], fibres[pair_key(y)]):
        nchecks += 1
        zp = xp[0], yp[1]
        assert compatible(xp,yp) and zp in pairs
        assert pair_key(zp) == pair_key(z)
        assert label(xp)==label(x) and label(yp)==label(y)
        assert label(zp)==label(z)
assert nchains == 270 and nchecks == 2550
# Nontrivial representatives in the same physical prefix context.
pplus, pminus, mdown, mup, hdown = (
    ("P","up"),("P","down"),("M","down"),("M","up"),("H","down"))
x, xp, y = (pplus,mdown),(pminus,mdown),(mup,hdown)
assert x != xp and pair_key(x)==pair_key(xp)
assert compatible(x,y) and compatible(xp,y)
# Negative fixture: drop channel separation, keep all distinct oriented pairs.
# Same-instance outer collision: (P+, M-) (M-, P-) -> (P+, P-);
# replace first P+ by P- and the outer pair repeats one stream.
z = (mdown,pminus)
assert key(x[1])==key(z[0])
assert x[0]!=z[1] and xp[0]==z[1]
assert not compatible(x,z) and not compatible(xp,z)
# Nonunit bounded control; not dynamic admission.
a,b = (("P","both"),mdown),(mup,("H","both"))
assert compatible(a,b)
assert (label(a),label(b),label((a[0],b[1]))) == (2,F(1,2),1)
print(f"TYPE LOGIC PASS: {len(pairs)} pairs, {len(fibres)} typed classes, "
      f"{nchains} chains, {nchecks} representative replacement checks")
print("N1/N2 fixture and same-instance outer-collision negative control PASS")
print("NONUNIT CONTROL PASS: 2 * (1/2) = 1")
print("SESSION ALG ONLY: no trajectory run; physical admission and adopted WD-DOM OPEN")
