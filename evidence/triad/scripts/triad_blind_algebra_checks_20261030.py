#!/usr/bin/env python3
"""Blind Triadic advisory: exact spot checks of adopted formula displays.

Scope: finite-dimensional algebra and conditional implications only.
NOT a replay of Triadic producer dynamics, owner certificates, trajectories,
physical realization, or the historical source packages.
Run: python -B evidence/triad/scripts/triad_blind_algebra_checks_20261030.py
"""
import sympy as sp

S = sp.sqrt
x, y, g = sp.symbols("x y g", real=True)
B = sp.Matrix([[1, -sp.Rational(1, 2)], [-sp.Rational(1, 2), 1]])
J = sp.Matrix([[1, -2], [2, -1]]) / S(3)
s = sp.Matrix([x, y])
Q = (s.T * B * s)[0]
assert sp.simplify(J.T * B * J - B) == sp.zeros(2)
assert sp.simplify(J * J + sp.eye(2)) == sp.zeros(2)
assert sp.simplify(sp.det(sp.Matrix.hstack(s, J * s)) / Q - 2 / S(3)) == 0

# T-6s: operator norm under the declared covector metric.
H = (1 - g) * B * J
assert sp.simplify(B.inv() * H.T * B.inv() * H -
                   (1 - g)**2 * sp.eye(2)) == sp.zeros(2)

# T-6t: row orthogonality is label-space, not a 3D physical carrier.
rows = sp.Matrix([[1, -1, 0, 0],
                  [sp.Rational(1, 2), sp.Rational(1, 2), -1, 0],
                  [sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3), -1]])
assert rows * rows.T == sp.diag(2, sp.Rational(3, 2), sp.Rational(4, 3))
R = sp.diag(1, sp.Rational(4, 3), sp.Rational(3, 2))
assert R * rows * rows.T * R == sp.diag(2, sp.Rational(8, 3), 3)

# T-6u: vector-seed norms and increment-channel numerator are distinct.
Vs = -Q * s / 16 - S(3) * Q * J * s / 32
Vc = -Q * s / 54 + 7 * Q * J * s / (108 * S(3))
assert sp.simplify((Vs.T * B * Vs)[0] / Q**3 - sp.Rational(7, 1024)) == 0
assert sp.simplify((Vc.T * B * Vc)[0] / Q**3 - sp.Rational(61, 34992)) == 0
assert sp.simplify((Vs.T * B * s)[0] / Q**2 + sp.Rational(1, 16)) == 0
assert sp.simplify((Vs[1] * x - Vs[0] * y) / Q**2 + sp.Rational(1, 16)) == 0
assert sp.simplify((sp.Rational(7, 512) * Q**3) /
                   (Vs.T * B * Vs)[0] - 2) == 0
for policy, expected_v, expected_delta in [
    (-2 * S(3) / 3, S(21) / 64, S(42) / 64),
    (-sp.Rational(1, 2), S(7) / 16, S(14) / 16),
]:
    value = S(7) / (32 * sp.Abs(policy))
    assert sp.simplify(value - expected_v) == 0
    assert sp.simplify(S(2) * value - expected_delta) == 0
assert sp.simplify((16 / S(7))**2 - 36 - sp.Rational(4, 7)) == 0

# §6.9 leading-torsion coercivity (not a global finite-u/r bound).
A = sp.Matrix([[3 * S(3), 3], [3, 9 * S(3)]])
assert set(A.eigenvals()) == {6 * S(3) - 6, 6 * S(3) + 6}

# §6.18: D=G/Qs first integral conditional on the printed ODE identity.
qs, qc, I, Om, fs, fc, fI, fOm = sp.symbols(
    "qs qc I Om fs fc fI fOm", real=True)
G = qs * qc - I**2 - Om**2
K = (I**2 + Om**2) / (qs * qc)
Gdot = qc * fs + qs * fc - 2 * I * fI - 2 * Om * fOm
sol = sp.solve(sp.Eq(Gdot, fs * G / qs), fOm)[0]  # Om != 0 here
D = G / qs
ddot = sum(sp.diff(D, v) * f for v, f in
           ((qs, fs), (qc, fc), (I, fI), (Om, fOm)))
kdot = sum(sp.diff(K, v) * f for v, f in
           ((qs, fs), (qc, fc), (I, fI), (Om, fOm)))
assert sp.simplify(ddot.subs(fOm, sol)) == 0
assert sp.simplify((kdot - (1 - K) * fc / qc).subs(fOm, sol)) == 0

# Exact six-step finite differences contain second-order cross terms.
dqs, dqc, dI, dOm = sp.symbols("dqs dqc dI dOm", real=True)
Gnext = (qs + dqs) * (qc + dqc) - (I + dI)**2 - (Om + dOm)**2
linear = qc * dqs + qs * dqc - 2 * I * dI - 2 * Om * dOm
assert sp.expand(Gnext - G - linear) == dqs * dqc - dI**2 - dOm**2

# A hypothetical same-vector metric change Q_T=2Q_G changes a Q^2 coefficient.
QT = sp.symbols("QT")
assert sp.simplify(2 * sp.Rational(1, 4) * (QT / 2)**2 - QT**2/8) == 0
print("PASS: T6s / T6t / T6u; coercivity; conditional invariant;")
print("      finite-increment correction; metric-scale example")
print("LIMIT: source producer/certificates/physical model NOT replayed")
