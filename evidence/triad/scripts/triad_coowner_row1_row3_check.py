#!/usr/bin/env python3
"""Triadic co-owner check (Claude), rows 1-3 of the v1.6.1 reconciliation list. SESSION algebra, not an owner certificate.

Inputs, all from the repository:
  * Triadic v1.6.1 (triad-v1.6.1, 95340abe...451f) §6.4: displayed Delta Q_s^(j), Delta Q_c^(j), Delta I_sc^(j), j = 0,1,2.
  * Recovered T-6l producer bytes (evidence/triad/scripts/triad_analytic_phase_steering_t6l_patched.py, 2e0317bf...11cd):
    the r^0 T-6e raw polynomial w_r0 = H_0(Q_s, I_sc, Omega).
  * §6.18: Delta Omega = -sqrt(3) * sum_j r^j H_j  (T-6e H_1, H_2 are not in the repository).

Checks:
  C1  Gram identity at r^0 with the producer H_0:  2 Omega dOmega0 = Qhat_c dQs0 + Q_s dQc0 - 2 I dI0  on the root, Qhat_c = (I^2+Omega^2)/Q_s,
      and the factor 1 (uncorrected) violates it.
  C2  The extension's G-dot. Extension = the displayed formulas with Q_c independent (§6.18 "Q_c independent, reduced coefficient formulas
      retained"); dOmega_j for j = 1, 2 taken as the unique Q_c-free value that satisfies the Gram identity on the root (the §6.18 claim).
      Compute G-dot = Q_c dQs + Q_s dQc - 2 I dI - 2 Omega dOmega and compare with (dQs/Q_s) G and with D-dot for D = G/Q_s.
  C3  K-dot on and off K = 1, and the f_s, f_c that make the §6.18 L742 identities hold.
  C4  Coercive bound for A_theta^corr: eigenvalues of [[3 sqrt3, 3], [3, 9 sqrt3]].
  C5  Corrected leading torsion from the producer bytes: with dOmega0 = -sqrt3 H_0 and dI0 (r = 0, I = mu sqrt(u) Q_s, Omega = nu sqrt(u) Q_s),
      [u^1] (mu dOmega0 - nu dI0)/(Q_s^2 sqrt u) = 3K(sqrt3 mu^2 + 2 mu nu + 3 sqrt3 nu^2)  (§6.9 B_theta^corr).
Exit 0 iff C1-C5 hold (C2/C3 assert the structural result printed below)."""
import sys
import sympy as sp

Qs, Qc, I, W, r = sp.symbols('Q_s Q_c I_sc Omega r', positive=True)
s3, s7 = sp.sqrt(3), sp.sqrt(7)
# §6.4 displayed coefficients (Q_c appears only in dQc1)
dQs = [-18*I**2 + 18*I*Qs - 12*s3*I*W - 24*Qs**2 + 6*s3*Qs*W - 6*W**2,
       -sp.Rational(6, 7)*sp.sqrt(42)*Qs**sp.Rational(3, 2),
       -sp.Rational(26, 7)*Qs]
dQc = [6/Qs**2*(-4*I**4 - 8*I**2*W**2 + Qs**2*(-3*I**2 + 2*s3*I*W - W**2) + Qs*(3*I**3 - s3*I**2*W + 3*I*W**2 - s3*W**3) - 4*W**4),
       6*Qc/(7*sp.sqrt(Qs))*(5*sp.sqrt(14)*W - sp.sqrt(42)*I),
       sp.Rational(2, 7)/Qs*(-13*I**2 + 20*s3*I*W - 57*W**2)]
dI = [3/Qs*(-7*I**3 - 3*s3*I**2*W - 7*I*W**2 + Qs*(6*I**2 - 7*I*Qs + 3*s3*Qs*W + 2*W**2) - 3*s3*W**3),
      (-3*sp.sqrt(42)*I**2 - 6*sp.sqrt(14)*I*W + 3*Qs*(-sp.sqrt(42)*I + 7*sp.sqrt(14)*W) + 7*sp.sqrt(42)*W**2)/(7*sp.sqrt(Qs)),
      -sp.Rational(26, 7)*I + 20*s3/7*W]
# T-6l producer r^0 raw T-6e polynomial (variable w = Omega)
H0 = (-3*I**3 + 5*s3*I**2*W - 3*I*W**2 + Qs*(3*I*Qs - 4*s3*I*W + 5*s3*Qs*W) + 5*s3*W**3)/Qs
Qhat = (I**2 + W**2)/Qs
ok = True

# C1
lhs_corr = 2*W*(-s3*H0); lhs_raw = 2*W*H0
rhs0 = Qhat*dQs[0] + Qs*dQc[0].subs(Qc, Qhat) - 2*I*dI[0]
c1 = sp.simplify(lhs_corr - rhs0) == 0 and sp.simplify(lhs_raw - rhs0) != 0
print('C1 Gram identity at r^0 with producer H_0: factor -sqrt3 holds:', sp.simplify(lhs_corr - rhs0) == 0, '| factor 1 fails:', sp.simplify(lhs_raw - rhs0) != 0)
ok &= c1

# dOmega_j: j=0 from producer; j=1,2 from the identity on the root (Q_c-free by construction)
dW = [-s3*H0]
for j in (1, 2):
    dW.append(sp.simplify((Qhat*dQs[j] + Qs*dQc[j].subs(Qc, Qhat) - 2*I*dI[j])/(2*W)))
print('   implied Q_c-free dOmega_1 =', sp.simplify(dW[1]))
print('   implied Q_c-free dOmega_2 =', sp.simplify(dW[2]))

# C2: extension field, Q_c independent
DQs = sum(r**j*dQs[j] for j in range(3)); DQc = sum(r**j*dQc[j] for j in range(3)); DI = sum(r**j*dI[j] for j in range(3)); DW = sum(r**j*dW[j] for j in range(3))
G = Qs*Qc - I**2 - W**2
Gdot = sp.expand(Qc*DQs + Qs*DQc - 2*I*DI - 2*W*DW)
res_fs_eq_Qsdot = sp.simplify(Gdot - DQs/Qs*G)
q1 = sp.simplify(dQc[1]/Qc)                      # Q_c-free factor of the r^1 Q_c channel
res_corrected = sp.simplify(Gdot - (DQs + r*Qs*q1)/Qs*G)
Ddot = sp.simplify(Gdot/Qs - G*DQs/Qs**2)
print('C2 G-dot - (Qdot_s/Q_s) G =', sp.factor(res_fs_eq_Qsdot))
print('   G-dot - ((Qdot_s + r Q_s q1)/Q_s) G =', res_corrected, '  with q1 = dQc^(1)/Q_c =', q1)
print('   D-dot (D = G/Q_s) =', sp.factor(Ddot))
c2 = res_corrected == 0 and sp.simplify(res_fs_eq_Qsdot - r*q1*G) == 0
ok &= c2
# C3: K-dot
K = (I**2 + W**2)/(Qs*Qc)
Kdot = sp.diff(K, Qs)*DQs + sp.diff(K, Qc)*DQc + sp.diff(K, I)*DI + sp.diff(K, W)*DW
fc = DQc - r*dQc[1]                             # Q_c-free part of Qdot_c
c3a = sp.simplify(Kdot - (1 - K)*fc/Qc) == 0
c3b = sp.simplify(Kdot.subs(Qc, Qhat)) == 0
print('C3 K-dot = (1-K) f_c/Q_c with f_c = Qdot_c - r dQc^(1) (Q_c-free part):', c3a, '| K-dot = 0 on K = 1:', c3b)
print('   K-dot = (1-K) Qdot_c/Q_c holds only if r dQc^(1) = 0:', sp.simplify(Kdot - (1 - K)*DQc/Qc - (-(1 - K)*r*q1)) == 0)
ok &= c3a and c3b
# C4
M = sp.Matrix([[3*s3, 3], [3, 9*s3]])
ev = sorted(M.eigenvals().keys(), key=lambda e: float(e))
c4 = sp.simplify(ev[0] - (6*s3 - 6)) == 0 and sp.simplify(ev[1] - (6*s3 + 6)) == 0
print('C4 eigenvalues of A_theta^corr form:', ev, '->', c4)
ok &= c4
# C5
mu, nu, u, v = sp.symbols('mu nu u v', real=True)
sub = {I: mu*v*Qs, W: nu*v*Qs}
num = sp.expand(((mu*(-s3*H0) - nu*dI[0]).subs(sub))/(Qs**2*v))
lead = sp.simplify(sp.Poly(num, v).coeff_monomial(v**2))
c5 = sp.simplify(lead - 3*(mu**2 + nu**2)*(s3*mu**2 + 2*mu*nu + 3*s3*nu**2)) == 0
print('C5 corrected leading torsion numerator [u^1] =', sp.factor(lead), '->', c5)
ok &= c5
print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
