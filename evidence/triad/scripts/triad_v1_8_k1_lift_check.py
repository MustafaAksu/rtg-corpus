#!/usr/bin/env python3
"""Triadic v1.8 cycle, T8-06 K1: out-of-plane content in the producer's own R^3 lifted model. SESSION algebra.

Source: the recovered T-6c2 producer `evidence/triad/scripts/tetrahedral_six_step_cross_phase_t6c2_patched.py`
(SHA-256 afb4525c...d80e, = Triadic §8 TRIAD-ART-T6C-CROSSPHASE). Its graph_forces(S, C, D) act on 3-vectors with the
metric B_3 = diag(B_T, 1) (B_dot), the apex starts at D0 = (-r/sqrt21, 2r/sqrt21, r/sqrt3), s and c start planar, and
each step applies hex_step_pair to the planar parts. After every step the producer sets the z-components of S and C to
0 (planar projection) and keeps D_z. This script reuses the same forces, step rule and truncation (state total degree 3
in s_rho, s_eta, c_rho, c_eta, r), but keeps S_z and C_z ("unprojected lift"), and evaluates
G = Q_s Q_c - I_sc^2 - Omega^2 = beta |w|^2_{B_T}, w = b u - a v (beta = 1), on the producer's axis representative.

Checks
  F1  the forces are equivariant under the reflection z -> -z of all three vectors (so the all-planar set D_z = 0 is
      invariant), and the projected run keeps K = 1 identically (a = b = 0);
  F2  one step, unprojected: a = (r/21)(7 sqrt3 Q_s + 4 sqrt14 sqrt(Q_s) r) on the axis, and the leading r^2 term of
      1 - K is (r^2/3)(Q_s + Q_c - 2 I_sc) = d_z^2 |s - c|^2_{B_T} (d_z = r/sqrt3);
  F3  six steps (one block): a_6 = 6 a_1, b_6 = 6 b_1, and 1 - K is exactly 36 times the one-step expression at this
      truncation (the planar hex map has order six, so u, v return at leading order);
  F4  the ChatGPT example (review 5747869312): in B_T-orthonormal plane coordinates s = (1,0,0), c = (0,1,t) gives
      K = 1/(1 + beta t^2): K(0) = 1 and dK/dt(0) = 0, yet K < 1 for t != 0 (vanishing derivative is not invariance).
Exit 0 iff F1-F4 hold.
"""
import sys, time
import sympy as sp

sr, se, cr, ce, r = sp.symbols('s_rho s_eta c_rho c_eta r', real=True)
V = [sr, se, cr, ce, r]
def B(u, v): return 2*u[0]*v[0] - u[0]*v[1] - u[1]*v[0] + 2*u[1]*v[1] + u[2]*v[2]   # producer B_dot
def trunc(e, deg):
    e = sp.expand(e)
    if e == 0: return sp.S.Zero
    P = sp.Poly(e, *V); out = sp.S.Zero
    for m, cf in P.terms():
        if sum(m) <= deg: out += cf*sp.prod([v**p for v, p in zip(V, m)])
    return sp.expand(out)
def forces(S, C, D):                                                                   # producer graph_forces
    Z = sp.Matrix([0, 0, 0])
    F0 = B(S, S)*S + B(C, C)*C + B(D, D)*D
    F1 = B(Z-S, Z-S)*(Z-S) + B(C-S, C-S)*(C-S) + B(D-S, D-S)*(D-S)
    F2 = B(Z-C, Z-C)*(Z-C) + B(S-C, S-C)*(S-C) + B(D-C, D-C)*(D-C)
    F3 = B(Z-D, Z-D)*(Z-D) + B(S-D, S-D)*(S-D) + B(C-D, C-D)*(C-D)
    return F1 - F0, F2 - F0, F3 - F0
def run(n, project, deg=3):
    S = sp.Matrix([sr, se, 0]); C = sp.Matrix([cr, ce, 0]); D = sp.Matrix([-r/sp.sqrt(21), 2*r/sp.sqrt(21), r/sp.sqrt(3)])
    for _ in range(n):
        Gs, Gc, Gd = forces(S, C, D)
        nxt = lambda X, G, keepz: sp.Matrix([trunc(X[0]-X[1]+G[0], deg), trunc(X[0]+G[1], deg), trunc(X[2]+G[2], deg) if keepz else 0])
        S, C, D = nxt(S, Gs, not project), nxt(C, Gc, not project), nxt(D, Gd, True)
    return S, C, D
Qs, I, W = sp.symbols('Q_s I_sc Omega', real=True)
srs = sp.sqrt(Qs/2); ces = W/(sp.sqrt(3)*srs); crs = (ces + I/srs)/2                # producer axis representative
ax = {se: 0, sr: srs, ce: ces, cr: crs}
Qc = (I**2 + W**2)/Qs
def one_minus_K(S, C):
    u = sp.Matrix([S[0], S[1], 0]); v = sp.Matrix([C[0], C[1], 0])
    w = C[2]*u - S[2]*v
    w4 = sp.Matrix([trunc(w[0], 4), trunc(w[1], 4), 0])
    return sp.simplify(sp.expand(trunc(B(w4, w4), 8).subs(ax))/(I**2 + W**2))       # G/(Q_s Q_c), leading order
ok = True

# F1
X = [sp.Matrix(sp.symbols(f'{n}0:3', real=True)) for n in 'xyz']
refl = lambda M: sp.Matrix([M[0], M[1], -M[2]])
Gf = forces(*X); Gr = forces(*[refl(x) for x in X])
f1a = all(sp.expand(refl(g) - h) == sp.zeros(3, 1) for g, h in zip(Gf, Gr))
Sp, Cp, _ = run(6, project=True)
f1b = Sp[2] == 0 and Cp[2] == 0
print(f"F1 z -> -z equivariance of the forces: {f1a}; projected run keeps S_z = C_z = 0: {f1b}")
ok &= f1a and f1b

# F2
t0 = time.time()
S1, C1, _ = run(1, project=False)
a1, b1 = sp.simplify(S1[2].subs(ax)), sp.simplify(C1[2].subs(ax))
f2a = sp.simplify(a1 - r*(7*sp.sqrt(3)*Qs + 4*sp.sqrt(14)*sp.sqrt(Qs)*r)/21) == 0
k1 = one_minus_K(S1, C1)
lead = sp.simplify(sp.limit(k1/r**2, r, 0))
f2b = sp.simplify(lead - sp.Rational(1, 3)*(Qs + Qc - 2*I)) == 0
print(f"F2 one step: a_1 = {sp.factor(a1)} ({f2a}); leading 1-K = r^2 * {sp.factor(lead)}; equals (r^2/3)(Q_s+Q_c-2I): {f2b}  [{time.time()-t0:.1f}s]")
ok &= f2a and f2b

# F3
t0 = time.time()
S6, C6, _ = run(6, project=False)
a6, b6 = sp.simplify(S6[2].subs(ax)), sp.simplify(C6[2].subs(ax))
f3a = sp.simplify(a6 - 6*a1) == 0 and sp.simplify(b6 - 6*b1) == 0
k6 = one_minus_K(S6, C6)
f3b = sp.simplify(k6 - 36*k1) == 0
print(f"F3 six steps: a_6 = 6 a_1 and b_6 = 6 b_1: {f3a}; 1-K(six) = 36 (1-K)(one): {f3b}; leading 1-K(six) = 12 r^2 (Q_s+Q_c-2I)  [{time.time()-t0:.1f}s]")
ok &= f3a and f3b

# F4
t, beta = sp.symbols('t beta', positive=True)
Kt = 1/(1 + beta*t**2)
f4 = Kt.subs(t, 0) == 1 and sp.diff(Kt, t).subs(t, 0) == 0 and sp.simplify(Kt - 1) != 0
print(f"F4 K(t) = 1/(1+beta t^2): K(0) = 1, K'(0) = 0, K < 1 for t != 0: {f4}")
ok &= f4

print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
