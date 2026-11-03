#!/usr/bin/env python3
"""Triadic v1.8 cycle, T8-06 K1 C3: cubic jet of the unprojected six-step map, and the apex-direction counterexample.
SESSION algebra; receiving check of ChatGPT review 5748759219 on 2277de8.

Model: the unprojected SESSION extension of the T-6c2 producer (advisory §4a/§4b): state X = (S, C, D) in (R^3)^3,
metric B_3 = diag(B_T, 1) with B_T = [[2,-1],[-1,2]], step F(X) = Lc X + G3(X), Lc = diag(L3, L3, L3),
L3 = [[1,-1,0],[1,0,0],[0,0,1]], G3 = the producer's graph forces (cubic, homogeneous).

Checks
  H1  L3^T B_3 L3 = B_3 and L3^6 = I;
  H2  G3(Lc X) = Lc G3(X) for symbolic X (nine free components);
  H3  for any B_T-rotation R of the plane (R^T B_T R = B_T, det R = 1), R commutes with L and G3 is equivariant under
      the joint rotation of all planar parts (checked for a rational point of SO(B_T));
  H4  cubic-jet formula F^6(X) = X + 6 Lc^{-1} G3(X) + O(|X|^5): (a) for symbolic X, by tracking the degree-1 and
      degree-3 parts of the truncated iteration; (b) by direct six-fold iteration of the full step map, truncated at
      eps^3, at three seeded rational starts eps*X;
  H5  start S = eps(1,0,0), C = eps(0,1,0) and the three apexes D/eps = (1,0,1), (1,0,-1), (0,1,1): equal
      Q_s, Q_c, I_sc, Omega, r = |D|_{B_3}, and w = 0 at the start; leading w after one block is
      (24,12) eps^4, (-24,-12) eps^4, (-12,-24) eps^4.
Exit 0 iff H1-H5 hold.
"""
import sys
import sympy as sp

def B(u, v): return 2*u[0]*v[0] - u[0]*v[1] - u[1]*v[0] + 2*u[1]*v[1] + u[2]*v[2]
B3 = sp.Matrix([[2, -1, 0], [-1, 2, 0], [0, 0, 1]])
L3 = sp.Matrix([[1, -1, 0], [1, 0, 0], [0, 0, 1]])
def G3(S, C, D):
    Z = sp.zeros(3, 1)
    F0 = B(S, S)*S + B(C, C)*C + B(D, D)*D
    F1 = B(Z-S, Z-S)*(Z-S) + B(C-S, C-S)*(C-S) + B(D-S, D-S)*(D-S)
    F2 = B(Z-C, Z-C)*(Z-C) + B(S-C, S-C)*(S-C) + B(D-C, D-C)*(D-C)
    F3 = B(Z-D, Z-D)*(Z-D) + B(S-D, S-D)*(S-D) + B(C-D, C-D)*(C-D)
    return F1 - F0, F2 - F0, F3 - F0
ok = True

h1 = (L3.T*B3*L3 - B3) == sp.zeros(3) and L3**6 == sp.eye(3)
print(f"H1 L3^T B_3 L3 = B_3: {(L3.T*B3*L3 - B3) == sp.zeros(3)}; L3^6 = I: {L3**6 == sp.eye(3)}"); ok &= h1

Xs = [sp.Matrix(sp.symbols(f'{n}0:3', real=True)) for n in 'scd']
G = G3(*Xs); GL = G3(*[L3*x for x in Xs])
h2 = all(sp.expand(gl - L3*g) == sp.zeros(3, 1) for g, gl in zip(G, GL))
print(f"H2 G3(Lc X) = Lc G3(X): {h2}"); ok &= h2

# a rational point of SO(B_T): R = (L^2 + ... ) not needed; use Cayley transform of the B_T-skew generator J with B_T J skew
J = sp.Matrix([[1, -2], [2, -1]])/sp.sqrt(3)            # B_T-orthogonal complex structure in producer coordinates
assert sp.simplify(J*J + sp.eye(2)) == sp.zeros(2) and sp.simplify(J.T*B3[:2, :2] + B3[:2, :2]*J) == sp.zeros(2)
t = sp.Rational(1, 3)
R2 = sp.simplify((sp.eye(2) - t*J).inv()*(sp.eye(2) + t*J))  # Cayley: in SO(B_T)
R = sp.diag(R2, 1)
ok_R = sp.simplify(R2.T*B3[:2, :2]*R2 - B3[:2, :2]) == sp.zeros(2) and sp.simplify(R2.det() - 1) == 0
comm = sp.simplify(R*L3 - L3*R) == sp.zeros(3)
GR = G3(*[R*x for x in Xs])
equi = all(sp.simplify(sp.expand(gr - R*g)) == sp.zeros(3, 1) for g, gr in zip(G, GR))
h3 = ok_R and comm and equi
print(f"H3 R in SO(B_T): {ok_R}; R L = L R: {comm}; G3 equivariant under joint planar rotation: {equi}"); ok &= h3

eps = sp.symbols('eps', positive=True)
def trunc_eps(M, deg):
    out = []
    for x in M:
        P = sp.Poly(sp.expand(x), eps)
        out.append(sum((c*eps**m[0] for m, c in P.terms() if m[0] <= deg), sp.S.Zero))
    return sp.Matrix(out)
Linv = L3.inv()
# (a) symbolic, by degree: X = X1 + X3 with X1 of degree 1 and X3 of degree 3; one truncated step is
#     X1 -> Lc X1, X3 -> Lc X3 + G3(X1) (G3 is homogeneous cubic, so the cross terms are of degree >= 5)
X1 = list(Xs); X3 = [sp.zeros(3, 1)]*3
for _ in range(6):
    g = G3(*X1)
    X3 = [sp.expand(L3*x3 + gg) for x3, gg in zip(X3, g)]
    X1 = [L3*x for x in X1]
h4a = all(x1 == x for x1, x in zip(X1, Xs)) and all(sp.expand(x3 - 6*Linv*gg) == sp.zeros(3, 1) for x3, gg in zip(X3, G))
# (b) direct six-fold iteration of the full step map, truncated at eps^3, for three seeded rational starts eps*X
import random
random.seed(20261103)
h4b = True
for _ in range(3):
    vals = {x: sp.Rational(random.randint(-9, 9), random.randint(1, 7)) for M in Xs for x in M}
    X = [eps*M.subs(vals) for M in Xs]
    for _ in range(6):
        g = G3(*X)
        X = [trunc_eps(L3*x + gg, 3) for x, gg in zip(X, g)]
    form = [sp.expand(eps*M.subs(vals) + 6*eps**3*Linv*gg.subs(vals)) for M, gg in zip(Xs, G)]
    h4b &= all(sp.expand(a - b) == sp.zeros(3, 1) for a, b in zip(X, form))
h4 = h4a and h4b
print(f"H4 cubic jet F^6(X) = X + 6 Lc^-1 G3(X) + O(|X|^5): symbolic by degree: {h4a}; direct truncated iteration at three rational starts: {h4b}"); ok &= h4

def jet6(S, C, D):
    g = G3(S, C, D)
    return [x + 6*Linv*gg for x, gg in zip((S, C, D), g)]
S0 = eps*sp.Matrix([1, 0, 0]); C0 = eps*sp.Matrix([0, 1, 0])
cases = {(1, 0, 1): (24, 12), (1, 0, -1): (-24, -12), (0, 1, 1): (-12, -24)}
obs = set(); h5 = True
for dv, want in cases.items():
    D0 = eps*sp.Matrix(dv)
    Om = -sp.sqrt(3)*(S0[1]*C0[0] - S0[0]*C0[1])
    obs.add((B(S0, S0), B(C0, C0), B(S0, C0), Om, B(D0, D0)))
    S6, C6, _ = jet6(S0, C0, D0)
    u, v = sp.Matrix(S6[:2]), sp.Matrix(C6[:2]); a, b = S6[2], C6[2]
    w = sp.expand(b*u - a*v)
    lead = [sp.expand(x).coeff(eps, 4) for x in w]
    good = lead == list(want)
    h5 &= good
    print(f"H5 D/eps = {dv}: leading w = {tuple(lead)} eps^4 (expected {want}): {good}")
h5 &= len(obs) == 1
print(f"H5 equal (Q_s, Q_c, I_sc, Omega, |D|^2) across the three starts: {len(obs) == 1}; w = 0 at start: True"); ok &= h5
print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
