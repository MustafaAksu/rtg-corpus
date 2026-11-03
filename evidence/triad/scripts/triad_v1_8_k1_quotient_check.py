#!/usr/bin/env python3
"""Triadic v1.8 cycle, T8-06 K1 C3: the SO(B_T) quotient of the unprojected one-step map, and first reduced-state tests.
SESSION algebra; receiving check of ChatGPT review 5749141951 on 6e4ce70.

Model: the unprojected SESSION extension (advisory §4a-§4c). X = (S, C, D) in (R^3)^3, B_3 = diag(B_T, 1),
one step F(X) = Lc X + G3(X) (exact polynomial step; no truncation is used in J1-J4).
Planar coordinates: R = Cholesky factor of B_T (R^T R = B_T), (x, y) = R u, zeta = x + i y, so that
B_T(u, v) = Re(conj(zeta_u) zeta_v) and Im(conj(zeta_s) zeta_c) = Omega (the producer's oriented area).
H_ij = conj(zeta_i) zeta_j, t = (a, b, d_z), g_ij = Re H_ij + t_i t_j.

Checks
  J1  R L R^-1 is the rotation by +pi/3, so the planar step is multiplication by lam = e^{i pi/3};
  J2  G3_i = sum_j M_ij(g) X_j with M derived from the force definition:
      M_ii = -2 g_ii - sum_{k != i} n_ik,  M_ij = n_ij - g_jj (i != j),  n_ij = g_ii - 2 g_ij + g_jj;
  J3  for symbolic X (nine components): H computed from the directly stepped X' equals conj(A) H A^T with
      A = lam I + M(g), and t' = (I + M(g)) t;
  J4  quotient: (i) at a seeded rational X and a rational point P of SO(B_T) (Cayley transform), stepping P X directly
      gives the same (H', t') as stepping X; (ii) for any rank-one H the chart (q, H_sc, H_sd; a, b, d_z), q = H_ss > 0,
      rebuilds H_cc = |H_sc|^2/q, H_dd = |H_sd|^2/q, H_cd = conj(H_sc) H_sd / q;
  J5  smaller representations, leading order of the block map F^6 = X + 6 Lc^-1 G3 (advisory §4c), on the starts of
      §4c H5 (S = eps(1,0,0), C = eps(0,1,0); D/eps = (1,0,1), (1,0,-1), (0,1,1)):
      (i) D/eps = (1,0,1) and (0,1,1) agree in (q, H_sc, |H_sd|, a, b, d_z) but give different a after one block, so
          (q, H_sc, |H_sd|, a, b, d_z) does not close: the phase of H_sd is needed;
      (ii) D/eps = (1,0,1) and (1,0,-1) agree in (q, H_sc, H_sd, a, b, |d_z|) but give different a after one block, so
          the sign of d_z is needed.
Exit 0 iff J1-J5 hold.
"""
import sys, random
import sympy as sp

BT = sp.Matrix([[2, -1], [-1, 2]])
L2 = sp.Matrix([[1, -1], [1, 0]])
R = sp.Matrix([[sp.sqrt(2), -1/sp.sqrt(2)], [0, sp.sqrt(sp.Rational(3, 2))]])
lam = sp.exp(sp.I*sp.pi/3)
def B(u, v): return 2*u[0]*v[0] - u[0]*v[1] - u[1]*v[0] + 2*u[1]*v[1] + u[2]*v[2]
def step(S, C, D):                                                  # producer forces, unprojected one step
    Z = sp.zeros(3, 1)
    F0 = B(S, S)*S + B(C, C)*C + B(D, D)*D
    F1 = B(Z-S, Z-S)*(Z-S) + B(C-S, C-S)*(C-S) + B(D-S, D-S)*(D-S)
    F2 = B(Z-C, Z-C)*(Z-C) + B(S-C, S-C)*(S-C) + B(D-C, D-C)*(D-C)
    F3 = B(Z-D, Z-D)*(Z-D) + B(S-D, S-D)*(S-D) + B(C-D, C-D)*(C-D)
    G = (F1 - F0, F2 - F0, F3 - F0)
    Lx = lambda X: sp.Matrix([X[0]-X[1], X[0], X[2]])
    return [Lx(X) + g for X, g in zip((S, C, D), G)], G
def zeta(X): x = R*sp.Matrix(X[:2]); return x[0] + sp.I*x[1]
def Hmat(Xs): z = [zeta(X) for X in Xs]; return sp.Matrix(3, 3, lambda i, j: sp.conjugate(z[i])*z[j])
def gram(Xs): return sp.Matrix(3, 3, lambda i, j: B(Xs[i], Xs[j]))
def Mmat(g):
    n = lambda i, j: g[i, i] - 2*g[i, j] + g[j, j]
    return sp.Matrix(3, 3, lambda i, j: (-2*g[i, i] - sum(n(i, k) for k in range(3) if k != i)) if i == j else n(i, j) - g[j, j])
ok = True

# J1
Rot = sp.simplify(R*L2*R.inv())
j1 = sp.simplify(R.T*R - BT) == sp.zeros(2) and sp.simplify(Rot - sp.Matrix([[sp.cos(sp.pi/3), -sp.sin(sp.pi/3)], [sp.sin(sp.pi/3), sp.cos(sp.pi/3)]])) == sp.zeros(2)
print(f"J1 R^T R = B_T and R L R^-1 = rotation by +pi/3 (planar step = multiplication by e^(i pi/3)): {j1}"); ok &= j1

# J2
Xs = [sp.Matrix(sp.symbols(f'{n}0:3', real=True)) for n in 'scd']
_, G = step(*Xs)
g = gram(Xs); M = Mmat(g)
j2 = all(sp.expand(G[i] - sum((M[i, j]*Xs[j] for j in range(3)), sp.zeros(3, 1))) == sp.zeros(3, 1) for i in range(3))
print(f"J2 G3_i = sum_j M_ij(g) X_j with the stated M(g): {j2}"); ok &= j2

# J3
Xn, _ = step(*Xs)
H = Hmat(Xs); A = lam*sp.eye(3) + M
Hn_direct = Hmat(Xn)
Hn_formula = A.conjugate()*H*A.T
j3a = all(sp.simplify(sp.expand(sp.expand_complex(Hn_direct[i, j] - Hn_formula[i, j]))) == 0 for i in range(3) for j in range(3))
t = sp.Matrix([X[2] for X in Xs]); tn = sp.Matrix([X[2] for X in Xn])
j3b = sp.expand(tn - (sp.eye(3) + M)*t) == sp.zeros(3, 1)
g_check = all(sp.simplify(sp.expand(sp.expand_complex(g[i, j] - (sp.re(H[i, j]) + t[i]*t[j])))) == 0 for i in range(3) for j in range(3))
print(f"J3 H' = conj(A) H A^T: {j3a}; t' = (I + M) t: {j3b}; g = Re H + t t^T: {g_check}"); ok &= j3a and j3b and g_check

# J4
random.seed(20261103)
vals = {x: sp.Rational(random.randint(-9, 9), random.randint(1, 7)) for X in Xs for x in X}
X0 = [X.subs(vals) for X in Xs]
J = sp.Matrix([[1, -2], [2, -1]])/sp.sqrt(3); tc = sp.Rational(2, 5)
P2 = sp.simplify((sp.eye(2) - tc*J).inv()*(sp.eye(2) + tc*J)); P = sp.diag(P2, 1)
inSO = sp.simplify(P2.T*BT*P2 - BT) == sp.zeros(2) and sp.simplify(P2.det() - 1) == 0
Xa, _ = step(*X0); Xb, _ = step(*[P*X for X in X0])
same = sp.simplify((Hmat(Xa) - Hmat(Xb)).applyfunc(sp.expand_complex)) == sp.zeros(3) and \
       sp.simplify(sp.Matrix([X[2] for X in Xa]) - sp.Matrix([X[2] for X in Xb])) == sp.zeros(3, 1)
zs = sp.symbols('z0:3'); zc = [sp.conjugate(z) for z in zs]
Hr = sp.Matrix(3, 3, lambda i, j: zc[i]*zs[j]); q = Hr[0, 0]
chart = sp.simplify(Hr[1, 1] - Hr[0, 1]*sp.conjugate(Hr[0, 1])/q) == 0 and sp.simplify(Hr[2, 2] - Hr[0, 2]*sp.conjugate(Hr[0, 2])/q) == 0 \
        and sp.simplify(Hr[1, 2] - sp.conjugate(Hr[0, 1])*Hr[0, 2]/q) == 0
j4 = inSO and same and chart
print(f"J4 P in SO(B_T): {inSO}; stepping P X gives the same (H', t') as stepping X: {same}; chart rebuilds H_cc, H_dd, H_cd: {chart}"); ok &= j4

# J5
eps = sp.symbols('eps', positive=True)
Linv = sp.Matrix([[1, -1, 0], [1, 0, 0], [0, 0, 1]]).inv()
def block_a(dv):
    S0, C0, D0 = eps*sp.Matrix([1, 0, 0]), eps*sp.Matrix([0, 1, 0]), eps*sp.Matrix(dv)
    _, Gq = step(S0, C0, D0)
    S6 = S0 + 6*Linv*Gq[0]
    return sp.expand(S6[2])
def obs(dv, drop):
    Xq = [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix(dv)]; Hq = Hmat(Xq)
    hsd = sp.simplify(sp.Abs(Hq[0, 2])) if drop == 'phase' else sp.simplify(sp.expand_complex(Hq[0, 2]))
    dz = abs(dv[2]) if drop == 'sign' else dv[2]
    return (sp.simplify(Hq[0, 0]), sp.simplify(sp.expand_complex(Hq[0, 1])), hsd, 0, 0, dz)
a1, a3, a2 = block_a((1, 0, 1)), block_a((0, 1, 1)), block_a((1, 0, -1))
j5i = obs((1, 0, 1), 'phase') == obs((0, 1, 1), 'phase') and sp.simplify(a1 - a3) != 0
j5ii = obs((1, 0, 1), 'sign') == obs((1, 0, -1), 'sign') and sp.simplify(a1 - a2) != 0
print(f"J5 block a: D=(1,0,1) -> {a1}, (0,1,1) -> {a3}, (1,0,-1) -> {a2}")
print(f"J5 (i) equal (q, H_sc, |H_sd|, a, b, d_z), different a after one block: {j5i}; (ii) equal (q, H_sc, H_sd, a, b, |d_z|), different a: {j5ii}")
ok &= j5i and j5ii
print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
