#!/usr/bin/env python3
"""Triadic v1.8 cycle, first pass: SESSION checks for T8-08, T8-09 and the T-6r carrier design note (T8-06).
Exact SymPy unless stated. These are SESSION algebra checks, not owner certificates.

Inputs, all from the repository:
  * Triadic v1.7 (`triad-v1.7`, 506f3403...e64a) §6.4 displayed coefficients Delta I_sc^(0,1,2), Delta Q_s^(0);
    §2 T-6m2 (Race-A r_0 = sqrt(7/1024) Q_s^(3/2)); §6.12 recorded forcing polynomial Q_s^3 (24 Q_s^2 + 8 Q_s - 18).
  * Genesis v2.9 (`gen-v2.9`) §6.5 L961 shadow drift dQ_s^(4) = 1/4 Q_s^2 + 5/9 Q_s Q_c - 2/9 I^2 - 19/36 I w;
    §6.6 L982 J_Q = (1/sqrt3) [[1,-2],[2,-1]], a^T B_G J_Q b = (sqrt3/2) w_ab, w_ab = a2 b1 - a1 b2.

Checks
  A  (T8-08) The reference ansatz I=0, Omega=-(2/sqrt3) q^2 (that is K=1, nu=-1, Q_c=(4/3)q^3), r=0 reproduces the recorded
     T-6m polynomial q^3(24q^2+8q-18) and its root (2 sqrt7 - 1)/6. With r = sqrt(7)/32 q^(3/2) (Race-A) the r^1 and r^2
     terms of §6.4 give q^3[-18 + (8 - 7 sqrt6/16) q + (24 + 7 sqrt6/24 - 5/128) q^2]; its positive root is computed.
  B  (T8-09) Genesis shadow drift at I=0 and Q_c = kappa^2 Q_s^3 (shear 4/3, recoil 1/4): leading coefficient 1/4 Q_s^2,
     as for T-1's isolated quartic pump +1/4 Q_s^2. (Coefficient match only.)
  C  (T8-06) On the producer plane (B_T = 2 B_G), h(s,c) := s^T B_T c - i s^T B_T J_Q c equals I + i Omega with
     Omega = -sqrt3 omega_raw, and |h|^2 = Q_s Q_c (so K = 1 for any planar pair, as §6.18 states).
  D  (T8-06) Enlarged carriers: for m planar blocks (or an ensemble average) with aggregated Q, I, Omega,
     Q_s Q_c - I^2 - Omega^2 >= 0 (Cauchy-Schwarz for h), with equality iff the blocks are complex-collinear; an explicit
     m = 2 example has K < 1. For the R^3 apex lift with metric diag(B_T, beta), beta > 0, and Omega the planar
     oriented area, Q_s Q_c - I^2 - Omega^2 is a sum of squares (zero iff s ^ c lies in the plane).
  E  (T8-06) Closure obstruction: under blockwise evolution with the §6.4 r^0 coefficient Delta Q_s^(0) on each block,
     two m = 2 configurations with the same aggregate (Q_s, Q_c, I, Omega) have different aggregate Delta Q_s. So the
     aggregate five-variable field is not autonomous on such a carrier; a closure must be supplied (T-6r C3).
Exit 0 iff A-E hold.
"""
import sys
import sympy as sp

ok = True
s3, s6 = sp.sqrt(3), sp.sqrt(6)

# ---------------------------------------------------------------- A  T-6m2
q = sp.symbols('q', positive=True)
Qs, I, W = sp.symbols('Q_s I_sc Omega', real=True)
dI = [3/Qs*(-7*I**3 - 3*s3*I**2*W - 7*I*W**2 + Qs*(6*I**2 - 7*I*Qs + 3*s3*Qs*W + 2*W**2) - 3*s3*W**3),
      (-3*sp.sqrt(42)*I**2 - 6*sp.sqrt(14)*I*W + 3*Qs*(-sp.sqrt(42)*I + 7*sp.sqrt(14)*W) + 7*sp.sqrt(42)*W**2)/(7*sp.sqrt(Qs)),
      -sp.Rational(26, 7)*I + 20*s3/7*W]
ans = {Qs: q, I: 0, W: -2/s3*q**2}
r = sp.sqrt(7)/32*q**sp.Rational(3, 2)
assert sp.simplify(r**2 - sp.Rational(7, 1024)*q**3) == 0
p0 = sp.expand(sp.simplify(dI[0].subs(ans)))
a1 = p0 == sp.expand(q**3*(24*q**2 + 8*q - 18))
p012 = sp.expand(sp.simplify(sum(r**j*dI[j].subs(ans) for j in range(3))))
target = sp.expand(q**3*(-18 + (8 - 7*s6/16)*q + (24 + 7*s6/24 - sp.Rational(5, 128))*q**2))
a2 = sp.simplify(p012 - target) == 0
root0 = [x for x in sp.solve(24*q**2 + 8*q - 18, q) if x.is_positive][0]
a3 = sp.simplify(root0 - (2*sp.sqrt(7) - 1)/6) == 0
quad = sp.expand(sp.simplify(p012/q**3))
roots = sp.solve(quad, q)
root12 = [x for x in roots if float(x) > 0]
a4 = len(root12) == 1
print(f"A  r=0 polynomial reproduces q^3(24q^2+8q-18): {a1}; r^1+r^2 polynomial as stated: {a2}")
print(f"   root r=0 = (2 sqrt7 - 1)/6 = {float(root0):.10f} ({a3}); positive root with r^1+r^2 = {float(root12[0]):.10f}"
      f"; shift {float(root12[0]-root0):+.10f} ({float((root12[0]-root0)/root0)*100:+.4f} %)")
ok &= a1 and a2 and a3 and a4

# ---------------------------------------------------------------- B  T-1 versus Genesis shadow
Qc, w = sp.symbols('Q_c omega_sc', real=True)
shadow = sp.Rational(1, 4)*Qs**2 + sp.Rational(5, 9)*Qs*Qc - sp.Rational(2, 9)*I**2 - sp.Rational(19, 36)*I*w
b_ok = True
for name, k2 in (("shear", sp.Rational(4, 3)), ("recoil", sp.Rational(1, 4))):
    e = sp.expand(shadow.subs({I: 0, Qc: k2*Qs**3}))
    lead = sp.Poly(e, Qs).coeff_monomial(Qs**2)
    print(f"B  Genesis shadow at I=0, Q_c={k2} Q_s^3 ({name}): {e}; leading coefficient {lead}")
    b_ok &= lead == sp.Rational(1, 4)
ok &= b_ok

# ---------------------------------------------------------------- C  Hermitian form on the producer plane
sr, se, cr, ce = sp.symbols('s_rho s_eta c_rho c_eta', real=True)
BG = sp.Matrix([[1, -sp.Rational(1, 2)], [-sp.Rational(1, 2), 1]]); BT = 2*BG
JQ = sp.Matrix([[1, -2], [2, -1]])/s3
S, C = sp.Matrix([sr, se]), sp.Matrix([cr, ce])
wab = lambda a, b: a[1]*b[0] - a[0]*b[1]
c1 = sp.simplify(JQ**2 + sp.eye(2)) == sp.zeros(2) and sp.simplify(JQ.T*BG*JQ - BG) == sp.zeros(2) \
    and sp.simplify((S.T*BG*JQ*C)[0] - s3/2*wab(S, C)) == 0
Qs_, Qc_, I_ = (S.T*BT*S)[0], (C.T*BT*C)[0], (S.T*BT*C)[0]
Om = -s3*(se*cr - sr*ce)                            # Omega = -sqrt3 omega_raw (Triadic §6.18)
c2 = sp.expand(-(S.T*BT*JQ*C)[0] - Om) == 0          # so h = I + i Omega
c3 = sp.expand(Qs_*Qc_ - I_**2 - Om**2) == 0
print(f"C  J_Q^2=-1, J_Q B_G-orthogonal, Genesis identity: {c1}; h(s,c) = I + i Omega: {c2}; |h|^2 = Q_s Q_c: {c3}")
ok &= c1 and c2 and c3

# ---------------------------------------------------------------- D  enlarged carriers: K <= 1
def inv(Sv, Cv):
    return (Sv.T*BT*Sv)[0], (Cv.T*BT*Cv)[0], (Sv.T*BT*Cv)[0], -s3*(Sv[1]*Cv[0] - Sv[0]*Cv[1])
blocks = [(sp.Matrix([1, 0]), sp.Matrix([1, 0])), (sp.Matrix([0, 1]), sp.Matrix([1, 1]))]
agg = [sum(x) for x in zip(*[inv(*b) for b in blocks])]
GA = sp.simplify(agg[0]*agg[1] - agg[2]**2 - agg[3]**2); KA = sp.nsimplify((agg[2]**2 + agg[3]**2)/(agg[0]*agg[1]))
# complex-collinear blocks (c_k = (a + b J_Q) s_k, same a, b) give K = 1
a_, b_ = sp.Rational(2, 3), sp.Rational(-1, 5)
Lmap = a_*sp.eye(2) + b_*JQ
blocks2 = [(sp.Matrix([1, 0]), Lmap*sp.Matrix([1, 0])), (sp.Matrix([1, 2]), Lmap*sp.Matrix([1, 2]))]
agg2 = [sp.simplify(sum(x)) for x in zip(*[inv(*b) for b in blocks2])]
G2 = sp.simplify(agg2[0]*agg2[1] - agg2[2]**2 - agg2[3]**2)
# R^3 apex lift: metric diag(B_T, beta)
beta = sp.symbols('beta', positive=True); sz, cz = sp.symbols('s_z c_z', real=True)
B3 = sp.diag(BT, beta)
S3, C3 = sp.Matrix([sr, se, sz]), sp.Matrix([cr, ce, cz])
G3 = sp.expand((S3.T*B3*S3)[0]*(C3.T*B3*C3)[0] - (S3.T*B3*C3)[0]**2 - (-s3*(se*cr - sr*ce))**2)
# orthonormal planar coordinates for B_T: x = L^T s with L L^T = B_T
Lc = BT.cholesky(); x1, x2 = sp.symbols('x1 x2', real=True); y1, y2 = sp.symbols('y1 y2', real=True)
sub = sp.solve(list(Lc.T*sp.Matrix([sr, se]) - sp.Matrix([x1, x2])) + list(Lc.T*sp.Matrix([cr, ce]) - sp.Matrix([y1, y2])), [sr, se, cr, ce])
G3o = sp.expand(G3.subs(sub))
sos = sp.expand(beta*((x1*cz - y1*sz)**2 + (x2*cz - y2*sz)**2))
d1 = GA > 0 and KA < 1; d2 = G2 == 0; d3 = sp.simplify(G3o - sos) == 0
print(f"D  m=2 example: Q_sQ_c-I^2-Omega^2 = {GA} > 0, K = {KA} < 1: {d1}; complex-collinear blocks give 0: {d2}")
print(f"   R^3 lift: Q_sQ_c-I^2-Omega^2 = beta[(x1 c_z - y1 s_z)^2 + (x2 c_z - y2 s_z)^2] in B_T-orthonormal plane coordinates: {d3}")
ok &= d1 and d2 and d3

# ---------------------------------------------------------------- E  closure obstruction
dQs0 = lambda Q, Ii, Ww: -18*Ii**2 + 18*Ii*Q - 12*s3*Ii*Ww - 24*Q**2 + 6*s3*Q*Ww - 6*Ww**2
def block_from(Qsk, Qck, th):           # planar block with given Q_s, Q_c and angle: I = sqrt(QsQc) cos, Omega = sqrt(QsQc) sin
    m = sp.sqrt(Qsk*Qck); return Qsk, Qck, m*sp.cos(th), m*sp.sin(th)
# configuration P: two identical blocks; configuration R: different Q_s split with the same aggregate (Q_s, Q_c, I, Omega)
P = [block_from(1, 1, 0), block_from(1, 1, 0)]                       # aggregate (2, 2, 2, 0), K = 1
t = sp.symbols('t', real=True)
# R: blocks (1+t, (1-t)... ) chosen collinear-real (Omega_k = 0): I_k = sqrt(Qs_k Qc_k); need sum I = 2 with Qs = (1+t, 1-t), Qc = (1+t, 1-t)
R = [(1 + t, 1 + t, 1 + t, 0), (1 - t, 1 - t, 1 - t, 0)]
aggP = [sum(x) for x in zip(*P)]; aggR = [sp.simplify(sum(x)) for x in zip(*R)]
same = all(sp.simplify(a - b) == 0 for a, b in zip(aggP, aggR))
dP = sp.simplify(sum(dQs0(b[0], b[2], b[3]) for b in P)); dR = sp.simplify(sum(dQs0(b[0], b[2], b[3]) for b in R))
e1 = same and sp.simplify(dP - dR) != 0
print(f"E  same aggregate (Q_s,Q_c,I,Omega) = {aggP} for all t: {same}; aggregate Delta Q_s^(0): P = {dP}, R(t) = {sp.expand(dR)}; differ for t != 0: {e1}")
ok &= e1

print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
