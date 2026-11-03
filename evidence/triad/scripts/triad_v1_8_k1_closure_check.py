#!/usr/bin/env python3
"""Triadic v1.8 cycle, T8-06 K1 C3: does the unprojected lift close on (Q_s, Q_c, I_sc, Omega, r) [and K]? SESSION algebra.

The model is the session extension of the T-6c2 producer used in `triad_v1_8_k1_lift_check.py`: the producer's forces,
step rule, truncation (state total degree 3 in s_rho, s_eta, c_rho, c_eta, r) and apex D0, with the z-components of
S and C kept. Here S and C start out of the plane, with vertical parts (a0, b0) = lam * (a1, b1), where (a1, b1) are the
one-step vertical kicks from the planar start and lam is a real parameter (so the initial vertical parts have the same
degree as the kicks and fit the truncation).

Checks
  G1  after one six-step block, a = (lam + 6) a1 and b = (lam + 6) b1 at this truncation;
  G2  the five quantities Q_s = |u|^2 + a^2, Q_c = |v|^2 + b^2, I_sc = <u,v> + a b, Omega (planar area) and r, and
      also K, are the same at lam = +6 and lam = -6 (the map (a,b) -> (-a,-b) leaves them unchanged);
  G3  after one block, 1 - K is (lam + 6)^2 / 36 times the planar-start value: 144/36 = 4 times at lam = +6 and 0 at
      lam = -6. Two states with equal (Q_s, Q_c, I_sc, Omega, r, K) therefore evolve to different K, so there is no
      autonomous closure on these variables. The sign (direction) of w = b u - a v relative to the apex-driven kick
      is extra state.
Exit 0 iff G1-G3 hold.
"""
import sys, time
import sympy as sp

sr, se, cr, ce, r = sp.symbols('s_rho s_eta c_rho c_eta r', real=True)
lam = sp.symbols('lam', real=True)
V = [sr, se, cr, ce, r]
def B(u, v): return 2*u[0]*v[0] - u[0]*v[1] - u[1]*v[0] + 2*u[1]*v[1] + u[2]*v[2]
def trunc(e, deg):
    e = sp.expand(e)
    if e == 0: return sp.S.Zero
    P = sp.Poly(e, *V); out = sp.S.Zero
    for m, cf in P.terms():
        if sum(m) <= deg: out += cf*sp.prod([v**p for v, p in zip(V, m)])
    return sp.expand(out)
def forces(S, C, D):
    Z = sp.Matrix([0, 0, 0])
    F0 = B(S, S)*S + B(C, C)*C + B(D, D)*D
    F1 = B(Z-S, Z-S)*(Z-S) + B(C-S, C-S)*(C-S) + B(D-S, D-S)*(D-S)
    F2 = B(Z-C, Z-C)*(Z-C) + B(S-C, S-C)*(S-C) + B(D-C, D-C)*(D-C)
    F3 = B(Z-D, Z-D)*(Z-D) + B(S-D, S-D)*(S-D) + B(C-D, C-D)*(C-D)
    return F1 - F0, F2 - F0, F3 - F0
D0 = sp.Matrix([-r/sp.sqrt(21), 2*r/sp.sqrt(21), r/sp.sqrt(3)])
def run(n, S, C, D, deg=3):
    for _ in range(n):
        Gs, Gc, Gd = forces(S, C, D)
        nxt = lambda X, G: sp.Matrix([trunc(X[0]-X[1]+G[0], deg), trunc(X[0]+G[1], deg), trunc(X[2]+G[2], deg)])
        S, C, D = nxt(S, Gs), nxt(C, Gc), nxt(D, Gd)
    return S, C, D
# one-step kicks from the planar start
S1, C1, _ = run(1, sp.Matrix([sr, se, 0]), sp.Matrix([cr, ce, 0]), D0)
a1, b1 = S1[2], C1[2]
Qs, I, W = sp.symbols('Q_s I_sc Omega', real=True)
srs = sp.sqrt(Qs/2); ces = W/(sp.sqrt(3)*srs); crs = (ces + I/srs)/2
ax = {se: 0, sr: srs, ce: ces, cr: crs}
def invariants(S, C):
    Qs_ = B(S, S); Qc_ = B(C, C); I_ = B(S, C); Om = -sp.sqrt(3)*(S[1]*C[0] - S[0]*C[1])
    return Qs_, Qc_, I_, Om
def one_minus_K(S, C):
    u = sp.Matrix([S[0], S[1], 0]); v = sp.Matrix([C[0], C[1], 0])
    w = C[2]*u - S[2]*v
    w4 = sp.Matrix([trunc(w[0], 4), trunc(w[1], 4), 0])
    return sp.simplify(sp.expand(trunc(B(w4, w4), 8).subs(ax))/(I**2 + W**2))
ok = True
t0 = time.time()
S0 = sp.Matrix([sr, se, lam*a1]); C0 = sp.Matrix([cr, ce, lam*b1])
S6, C6, _ = run(6, S0, C0, D0)
g1 = sp.simplify(S6[2] - (lam + 6)*a1) == 0 and sp.simplify(C6[2] - (lam + 6)*b1) == 0
print(f"G1 after one block a = (lam+6) a1, b = (lam+6) b1: {g1}  [{time.time()-t0:.1f}s]")
ok &= g1
inv0 = invariants(S0, C0)
g2 = all(sp.simplify(sp.expand(x.subs(lam, 6) - x.subs(lam, -6))) == 0 for x in inv0)
K0p, K0m = one_minus_K(S0.subs(lam, 6), C0.subs(lam, 6)), one_minus_K(S0.subs(lam, -6), C0.subs(lam, -6))
g2 &= sp.simplify(K0p - K0m) == 0
print(f"G2 (Q_s, Q_c, I_sc, Omega, r) and 1-K equal at lam = +6 and lam = -6: {g2}")
ok &= g2
base = one_minus_K(*run(6, sp.Matrix([sr, se, 0]), sp.Matrix([cr, ce, 0]), D0)[:2])
kp = one_minus_K(S6.subs(lam, 6), C6.subs(lam, 6)); km = one_minus_K(S6.subs(lam, -6), C6.subs(lam, -6))
g3 = sp.simplify(kp - 4*base) == 0 and sp.simplify(km) == 0 and sp.simplify(base) != 0
print(f"G3 after one block: 1-K(lam=+6) = 4 x planar-start value: {sp.simplify(kp - 4*base) == 0}; 1-K(lam=-6) = 0: {sp.simplify(km) == 0}; so no closure on (Q_s,Q_c,I,Omega,r,K): {g3}")
ok &= g3
print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
