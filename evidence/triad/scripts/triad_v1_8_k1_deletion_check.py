#!/usr/bin/env python3
"""Triadic v1.8 cycle, T8-06 K1 C3: direct coordinate-deletion tests on the eight-coordinate chart. SESSION algebra.
Receiving check of ChatGPT review 5749303513 on 9e0ac3f, and the further deletions it proposes (q, Re H_sc, Im H_sc).

Model: the unprojected SESSION extension (advisory §4a-§4d). Chart (q, H_sc, H_sd; a, b, d_z), q = H_ss > 0, with
zeta = x + i y, (x, y) = R u, R the Cholesky factor of B_T, H_ij = conj(zeta_i) zeta_j, t = (a, b, d_z) (advisory §4d).

For each deleted coordinate k a pair of starts eps*X, eps*X' is given that agree in the other seven chart coordinates
and differ in k. Two maps are tested:
  one-step  the exact one-step polynomial map F (no truncation); the kept outputs are compared exactly;
  block     the leading-order block map F^6 = X + 6 Lc^-1 G3(X) + O(eps^5) (advisory §4c); kept outputs are compared
            where the jet is reliable: H entries up to eps^4, t entries up to eps^3.
If a kept output differs, the representation without k does not close under that map (a direct deletion only; other
seven-coordinate representations, for example nonlinear ones or coordinate changes such as Q_d for |H_sd|, are not
tested).

Checks
  K1  the three pairs of review 5749303513 reproduce its one-step values: deleting a, b' = 8 eps^3 / 0; deleting b,
      a' = 2 eps^3 / -6 eps^3; deleting |H_sd|, a' = -2 eps^3 / -6 eps^3;
  K2  every pair agrees in the seven kept chart coordinates and differs in the deleted one;
  K3  for each of the eight deletions (a, b, |H_sd|, phase of H_sd, sign of d_z, q, Re H_sc, Im H_sc) a kept output
      differs under the one-step map, and under the block map.
Exit 0 iff K1-K3 hold. The table printed below lists the first differing kept output and its leading values.
"""
import sys
import sympy as sp

eps = sp.symbols('eps', positive=True)
R = sp.Matrix([[sp.sqrt(2), -1/sp.sqrt(2)], [0, sp.sqrt(sp.Rational(3, 2))]])
L3 = sp.Matrix([[1, -1, 0], [1, 0, 0], [0, 0, 1]]); Linv = L3.inv()
def B(u, v): return 2*u[0]*v[0] - u[0]*v[1] - u[1]*v[0] + 2*u[1]*v[1] + u[2]*v[2]
def G3(S, C, D):
    Z = sp.zeros(3, 1)
    F0 = B(S, S)*S + B(C, C)*C + B(D, D)*D
    F1 = B(Z-S, Z-S)*(Z-S) + B(C-S, C-S)*(C-S) + B(D-S, D-S)*(D-S)
    F2 = B(Z-C, Z-C)*(Z-C) + B(S-C, S-C)*(S-C) + B(D-C, D-C)*(D-C)
    F3 = B(Z-D, Z-D)*(Z-D) + B(S-D, S-D)*(S-D) + B(C-D, C-D)*(C-D)
    return F1 - F0, F2 - F0, F3 - F0
def one_step(X): return [L3*x + g for x, g in zip(X, G3(*X))]
def block(X):    return [x + 6*Linv*g for x, g in zip(X, G3(*X))]
def zeta(x): v = R*sp.Matrix(x[:2]); return v[0] + sp.I*v[1]
def chart(X):
    zs, zc, zd = (zeta(x) for x in X)
    re_im = lambda z: (sp.expand(sp.re(sp.expand_complex(z))), sp.expand(sp.im(sp.expand_complex(z))))
    q = sp.expand(sp.expand_complex(sp.conjugate(zs)*zs))
    hsc = re_im(sp.conjugate(zs)*zc); hsd = re_im(sp.conjugate(zs)*zd)
    return {'q': q, 'ReH_sc': hsc[0], 'ImH_sc': hsc[1], 'ReH_sd': hsd[0], 'ImH_sd': hsd[1],
            'a': sp.expand(X[0][2]), 'b': sp.expand(X[1][2]), 'd_z': sp.expand(X[2][2])}
def cut(e, deg):
    P = sp.Poly(sp.expand(e), eps)
    return sp.expand(sum((c*eps**m[0] for m, c in P.terms() if m[0] <= deg), sp.S.Zero))
def mod_sd(c): return sp.sqrt(c['ReH_sd']**2 + c['ImH_sd']**2)
def kept(c, k):
    """Seven kept chart coordinates as functions of the full chart, for deletion k."""
    base = dict(c)
    if k == 'abs_sd':  base.pop('ReH_sd'); base.pop('ImH_sd'); base['arg_sd'] = sp.atan2(c['ImH_sd'], c['ReH_sd'])
    elif k == 'arg_sd': base.pop('ReH_sd'); base.pop('ImH_sd'); base['abs_sd'] = mod_sd(c)
    elif k == 'sign_dz': base['d_z'] = sp.Abs(c['d_z'])
    else: base.pop(k)
    return base
V = lambda *v: sp.Matrix(v)
S0, C0, D0 = V(1, 0, 0), V(0, 1, 0), V(1, 0, 1)
pairs = {   # deletion: (X, X')
    'a':       ([V(1, 0, 1), C0, D0], [V(1, 0, -1), C0, D0]),
    'b':       ([S0, V(0, 1, 1), D0], [S0, V(0, 1, -1), D0]),
    'abs_sd':  ([S0, C0, V(1, 0, 1)], [S0, C0, V(2, 0, 1)]),
    'arg_sd':  ([S0, C0, V(1, 0, 1)], [S0, C0, V(0, 1, 1)]),
    'sign_dz': ([S0, C0, V(1, 0, 1)], [S0, C0, V(1, 0, -1)]),
    'q':       ([S0, C0, D0], [V(2, 0, 0), V(0, sp.Rational(1, 2), 0), V(sp.Rational(1, 2), 0, 1)]),  # zeta_s*2, zeta_c/2, zeta_d/2
    'ReH_sc':  ([S0, C0, D0], [S0, V(1, 1, 0), D0]),                                              # zeta_c + zeta_s
    'ImH_sc':  ([S0, C0, D0], [S0, V(1, 3, 0), D0]),                                              # zeta_c + sqrt3 i zeta_s
}
ok = True; k2 = True; k3 = True; rows = []
for k, (Xa, Xb) in pairs.items():
    Xa = [eps*x for x in Xa]; Xb = [eps*x for x in Xb]
    ca, cb = chart(Xa), chart(Xb)
    ka, kb = kept(ca, k), kept(cb, k)
    agree = all(sp.simplify(ka[n] - kb[n]) == 0 for n in ka)
    full_a, full_b = ca, cb
    differs = any(sp.simplify(full_a[n] - full_b[n]) != 0 for n in full_a)
    k2 &= agree and differs
    res = {}
    for name, mp, degs in (('one-step', one_step, None), ('block', block, {'H': 4, 't': 3})):
        oa, ob = kept(chart(mp(Xa)), k), kept(chart(mp(Xb)), k)
        diff = None
        for n in oa:
            if degs is None: x, y = oa[n], ob[n]
            else:
                d = degs['t'] if n in ('a', 'b', 'd_z') else degs['H']
                if n in ('arg_sd', 'abs_sd'): x, y = sp.simplify(oa[n]), sp.simplify(ob[n])   # functions of H entries
                else: x, y = cut(oa[n], d), cut(ob[n], d)
            if n in ('arg_sd', 'abs_sd') and degs is not None:
                hx = [cut(chart(mp(Xa))[m], 4) for m in ('ReH_sd', 'ImH_sd')]; hy = [cut(chart(mp(Xb))[m], 4) for m in ('ReH_sd', 'ImH_sd')]
                x = sp.atan2(hx[1], hx[0]) if n == 'arg_sd' else sp.sqrt(hx[0]**2 + hx[1]**2)
                y = sp.atan2(hy[1], hy[0]) if n == 'arg_sd' else sp.sqrt(hy[0]**2 + hy[1]**2)
            if sp.simplify(x - y) != 0:
                lx = sp.factor(sp.simplify(x)); ly = sp.factor(sp.simplify(y)); diff = (n, lx, ly); break
        res[name] = diff
        k3 &= diff is not None
    rows.append((k, agree, res))
    if k == 'a': k1a = sp.expand(one_step(Xa)[1][2]) == 8*eps**3 and sp.expand(one_step(Xb)[1][2]) == 0
    if k == 'b': k1b = sp.expand(one_step(Xa)[0][2]) == 2*eps**3 and sp.expand(one_step(Xb)[0][2]) == -6*eps**3
    if k == 'abs_sd': k1c = sp.expand(one_step(Xa)[0][2]) == -2*eps**3 and sp.expand(one_step(Xb)[0][2]) == -6*eps**3
k1 = k1a and k1b and k1c
print(f"K1 review 5749303513 one-step values: delete a: b' = 8 eps^3 / 0: {k1a}; delete b: a' = 2 / -6 eps^3: {k1b}; delete |H_sd|: a' = -2 / -6 eps^3: {k1c}")
for k, agree, res in rows:
    print(f"  delete {k:8s} kept coordinates agree at start: {agree}")
    for name in ('one-step', 'block'):
        n, x, y = res[name]
        print(f"      {name:8s}: first differing kept output {n}: {x}  vs  {y}")
print(f"K2 every pair agrees in the seven kept chart coordinates and differs in the deleted one: {k2}")
print(f"K3 every direct deletion fails to close under the one-step map and under the block map: {k3}")
ok = k1 and k2 and k3
print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
