#!/usr/bin/env python3
"""Triadic v1.6.1 reconciliation, row 1: the two root-equivalent five-variable extensions. SESSION algebra.

Inputs as in evidence/triad/scripts/triad_coowner_row1_row3_check.py (§6.4 displayed coefficients; T-6l producer H_0;
dOmega_1, dOmega_2 = the Q_c-free values fixed by the Gram identity on the root, since H_1, H_2 bytes are not in the repository).

Extension (a) LITERAL: dQc^(1) = 6 Q_c/(7 sqrt Q_s)(5 sqrt14 Omega - sqrt42 I), Q_c the independent variable.
Extension (b) Q_c-FREE: the same coefficient with Q_c replaced by Qhat_c = (I^2+Omega^2)/Q_s (equal on the root).
Both give the same root model. For each, report G-dot, D-dot (D = G/Q_s), K-dot on K = 1, and the f_s, f_c of L742.
Exit 0 iff: (a) D-dot = r q1 D, f_s = Qdot_s + r Q_s q1, f_c = Qdot_c - r Q_c q1;
            (b) D-dot = 0,      f_s = Qdot_s,          f_c = Qdot_c;
            both: K-dot = 0 on K = 1 and the two fields agree on the root.
Row 2 bookkeeping: with weights Q_s, Q_c, I_sc, Omega -> 1 and r -> 1/2, every retained r^j increment (j = 0, 1, 2) of
Q_s, Q_c, I_sc, Omega is homogeneous of degree 2 (so the Gram first variation is degree 3 and the discarded products
dQs dQc - dI^2 - dOmega^2 are degree 4). Checked by scaling Q, I, Omega -> t*(.), r -> sqrt(t)*r."""
import sys
import sympy as sp

Qs, Qc, I, W, r = sp.symbols('Q_s Q_c I_sc Omega r', positive=True)
s3 = sp.sqrt(3)
Qhat = (I**2 + W**2)/Qs
dQs = [-18*I**2 + 18*I*Qs - 12*s3*I*W - 24*Qs**2 + 6*s3*Qs*W - 6*W**2,
       -sp.Rational(6, 7)*sp.sqrt(42)*Qs**sp.Rational(3, 2), -sp.Rational(26, 7)*Qs]
dQc0 = 6/Qs**2*(-4*I**4 - 8*I**2*W**2 + Qs**2*(-3*I**2 + 2*s3*I*W - W**2) + Qs*(3*I**3 - s3*I**2*W + 3*I*W**2 - s3*W**3) - 4*W**4)
q1 = 6*(5*sp.sqrt(14)*W - sp.sqrt(42)*I)/(7*sp.sqrt(Qs))
dQc2 = sp.Rational(2, 7)/Qs*(-13*I**2 + 20*s3*I*W - 57*W**2)
dI = [3/Qs*(-7*I**3 - 3*s3*I**2*W - 7*I*W**2 + Qs*(6*I**2 - 7*I*Qs + 3*s3*Qs*W + 2*W**2) - 3*s3*W**3),
      (-3*sp.sqrt(42)*I**2 - 6*sp.sqrt(14)*I*W + 3*Qs*(-sp.sqrt(42)*I + 7*sp.sqrt(14)*W) + 7*sp.sqrt(42)*W**2)/(7*sp.sqrt(Qs)),
      -sp.Rational(26, 7)*I + 20*s3/7*W]
H0 = (-3*I**3 + 5*s3*I**2*W - 3*I*W**2 + Qs*(3*I*Qs - 4*s3*I*W + 5*s3*Qs*W) + 5*s3*W**3)/Qs
G = Qs*Qc - I**2 - W**2
K = (I**2 + W**2)/(Qs*Qc)
ok = True

def field(dQc1):
    dQc = [dQc0, dQc1, dQc2]
    dW = [-s3*H0] + [sp.simplify((Qhat*dQs[j] + Qs*dQc[j].subs(Qc, Qhat) - 2*I*dI[j])/(2*W)) for j in (1, 2)]
    S = lambda L: sum(r**j*L[j] for j in range(3))
    return S(dQs), S(dQc), S(dI), S(dW)

res = {}
for name, dQc1 in (('a LITERAL', Qc*q1), ('b Q_c-FREE', Qhat*q1)):
    DQs, DQc, DI, DW = field(dQc1)
    Gdot = Qc*DQs + Qs*DQc - 2*I*DI - 2*W*DW
    Ddot = sp.simplify(Gdot/Qs - G*DQs/Qs**2)
    Kdot = sp.diff(K, Qs)*DQs + sp.diff(K, Qc)*DQc + sp.diff(K, I)*DI + sp.diff(K, W)*DW
    on_K1 = sp.simplify(Kdot.subs(Qc, Qhat)) == 0
    if name.startswith('a'):
        fs, fc, want_D = DQs + r*Qs*q1, DQc - r*Qc*q1, r*q1*G/Qs
    else:
        fs, fc, want_D = DQs, DQc, 0
    L742 = sp.simplify(Gdot - fs/Qs*G) == 0 and sp.simplify(Kdot - (1 - K)*fc/Qc) == 0
    Dok = sp.simplify(Ddot - want_D) == 0
    print(f'({name}) D-dot = {sp.factor(Ddot)} | expected form: {Dok} | L742 with stated f_s,f_c: {L742} | K-dot=0 on K=1: {on_K1}')
    ok &= Dok and L742 and on_K1
    res[name] = (DQs, DQc, DI, DW)
same_root = all(sp.simplify((x - y).subs(Qc, Qhat)) == 0 for x, y in zip(res['a LITERAL'], res['b Q_c-FREE']))
print('(a) and (b) agree on the root Q_c = Qhat_c:', same_root)
ok &= same_root
t = sp.symbols('t', positive=True)
sc = {Qs: t*Qs, Qc: t*Qc, I: t*I, W: t*W, r: sp.sqrt(t)*r}
hom = all(sp.simplify(X.subs(sc, simultaneous=True) - t**2*X) == 0 for X in res['a LITERAL'] + res['b Q_c-FREE'])
print('Row 2: all retained increments homogeneous of degree 2 under (Q,I,Omega) weight 1, r weight 1/2:', hom)
ok &= hom
print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
