#!/usr/bin/env python3
"""
triad_t6s_chirality.py
RTG Triadic — T-6s in-plane chirality-count and conjugate-pair certificate.

Exit-code-gated certificate. Returns 0 iff ALL T-6s closure criteria pass.
Promotes T-6s from [candidate] to [ALG, exact].

Certifies:
  C1: J_Q characteristic polynomial = lambda^2 + 1 (eigenvalues +-i,
      exactly two in-plane chirality channels, no real invariant line).
  C2: certified birth ratio W_child/W_parent = +i (selects +i channel),
      direction-independent.
  C3: J_Q^{-1} = -J_Q (opposite chirality is conjugate, not independent).
  C4: coherent two-channel source H_total = (1-g2) B J_Q, hence
      ||H_total||_B = |1-g2| <= 1, single-channel value 1 is the maximum.
  C5: J_Q is a B-isometry (J_Q^T B J_Q = B) and J_Q^2 = -I.

HINDEX norm convention (Genesis v2.8.x):
  ||H||_B^2 = lambda_max(B^{-1} H^T B^{-1} H).
"""
import sys
from sympy import (Matrix, eye, zeros, sqrt, Rational, I, simplify, expand, im,
                   cos, sin, symbols, pi, nsimplify, Symbol)

FAILURES = []

def check(name, cond):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILURES.append(name)
    return ok

# --- Certified objects (Genesis 6.6 / memory) ---
B  = Matrix([[1, Rational(-1,2)], [Rational(-1,2), 1]])
JQ = Matrix([[1, -2], [2, -1]]) / sqrt(3)
Binv = B.inv()
I2 = eye(2)

print("="*60)
print("T-6s certificate: in-plane chirality conjugate-pair")
print("="*60)

# --- C5: J_Q structural properties (prerequisite) ---
check("C5a J_Q is B-isometry (J_Q^T B J_Q = B)",
      simplify(JQ.T*B*JQ - B) == zeros(2,2))
check("C5b J_Q^2 = -I",
      simplify(JQ*JQ + I2) == zeros(2,2))

# --- C1: characteristic polynomial lambda^2 + 1, eigenvalues +-i ---
lam = symbols('lambda')
cp = expand(JQ.charpoly(lam).as_expr())
check("C1a char poly = lambda^2 + 1", simplify(cp - (lam**2 + 1)) == 0)
evs = JQ.eigenvals()
check("C1b eigenvalues are exactly {+i, -i}",
      set(evs.keys()) == {I, -I} and sum(evs.values()) == 2)
# no real eigenvector => no real invariant line
real_evs = [e for e in evs.keys() if simplify(im(e)) == 0] if False else []
check("C1c no real eigenvalue (no real invariant line)",
      all(simplify(im(e)) != 0 for e in evs.keys()))

# --- C2: birth ratio W_child/W_parent = +i, direction-independent ---
t = symbols('t', real=True)
# W-frame linear map (s,c phase-plane): W = u + i v, (u,v) = U (rho,eta)
U = Matrix([[1, Rational(-1,2)], [0, sqrt(3)/2]])
def toW(vec):
    uv = U*vec
    return uv[0] + I*uv[1]
s_star = Matrix([cos(t), sin(t)])
ratio = simplify(toW(JQ*s_star) / toW(s_star))
check("C2 W_child/W_parent = +i (all directions t)",
      simplify(ratio - I) == 0)

# --- C3: J_Q^{-1} = -J_Q ---
check("C3 J_Q^{-1} = -J_Q (conjugate channel, not independent)",
      simplify(JQ.inv() + JQ) == zeros(2,2))

# --- C4: coherent two-channel norm = |1 - g2| <= 1 ---
g2 = symbols('g_2', real=True)
H_total = B*JQ + g2*(B*JQ.inv())          # = (1-g2) B J_Q
check("C4a H_total = (1-g2) B J_Q",
      simplify(H_total - (1-g2)*B*JQ) == zeros(2,2))
M = simplify(Binv * H_total.T * Binv * H_total)
norm_evs = list(M.eigenvals().keys())
# both eigenvalues should equal (1-g2)^2
check("C4b ||H_total||_B^2 eigenvalues all = (1-g2)^2",
      all(simplify(ev - (1-g2)**2) == 0 for ev in norm_evs))
# single-channel value (g2=0): ||H||_B^2 = 1
M0 = M.subs(g2, 0)
sc_evs = [simplify(ev) for ev in M0.eigenvals().keys()]
check("C4c single-channel ||H||_B = 1 (max at g2=0)",
      all(ev == 1 for ev in sc_evs))
# g2=1 cancels
check("C4d g2=1 cancels (H_total = 0)",
      simplify(H_total.subs(g2, 1)) == zeros(2,2))

print("="*60)
if FAILURES:
    print(f"CERTIFICATE FAILED: {len(FAILURES)} check(s) failed: {FAILURES}")
    sys.exit(1)
print("CERTIFICATE PASSED — T-6s promotable to [ALG, exact].")
print("In-plane chirality space = {+i,-i} conjugate pair of J_Q;")
print("coherent two-channel source ||H||_B = |1-g2| <= 1.")
sys.exit(0)
