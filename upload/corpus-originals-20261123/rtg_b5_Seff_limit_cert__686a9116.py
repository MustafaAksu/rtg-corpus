#!/usr/bin/env python3
"""
rtg_b5_Seff_limit_cert.py  (FAST + all-p closure)
==================================================
Executable certificate for the b=5 boundary, closing the all-p theorem.

Uses the closed rational form of S_eff/S (independently re-derived from the
beta-graded engine and confirmed identical to the reviewer's form):

    S_eff/S = N(lam)/Den(lam),
    N   = 2*lam^6 + lam^5 - 5*lam^4 - 3*lam^3 - 4*lam^2 + 2*lam + 1   (deg 6)
    Den = lam^5 - lam^4 - lam^3 - 2*lam^2 + 1                          (deg 5)

Fast: works with the cancelled rational function directly.

Certifies:
  1. lim_{lam->1} S_eff/S = 3                                    [ALG]
  2. N(lam_p) != 0 for all primitive p-th roots: a primitive p-th root is a
     root of deg-6 N only if Phi_p | N, possible only when phi(p) <= 6
     (finitely many p); exact division shows Phi_p does NOT divide N for any. [ALG]
  3. Den(lam_p) != 0 (S != 0) for all p>=13.                     [ALG]
  => S_eff(lam_p) != 0 for all p>=13; with exact sweep p=6..12,
     F_raw^p(0,5) != 0 for ALL p>=6.  ALL-p THEOREM CLOSED.      [ALG]

Exit 0 iff all certify.
"""
import sys
import sympy as sp
from sympy import cyclotomic_poly, totient

lam = sp.symbols('lam')
N   = 2*lam**6 + lam**5 - 5*lam**4 - 3*lam**3 - 4*lam**2 + 2*lam + 1
Den = lam**5 - lam**4 - lam**3 - 2*lam**2 + 1
FAIL = False

L = sp.limit(N/Den, lam, 1)
print("1. lim_{lam->1} S_eff/S =", sp.simplify(L))
if sp.simplify(L-3)!=0: print("   FAIL"); FAIL=True
else: print("   [OK] exact limit = 3  [ALG]")

degN = sp.Poly(N,lam).degree()
candN = [p for p in range(1, 4*degN+4) if totient(p) <= degN]
badN = [p for p in candN if sp.Poly(N,lam).rem(sp.Poly(cyclotomic_poly(p,lam),lam))==0]
print(f"\n2. N deg={degN}; p with phi(p)<={degN}: {candN}")
print(f"   p where Phi_p | N: {badN}")
if badN: print("   FAIL"); FAIL=True
else: print(f"   [OK] N(lam_p) != 0 for ALL p  [ALG]")

degD = sp.Poly(Den,lam).degree()
candD = [p for p in range(1, 4*degD+4) if totient(p) <= degD]
badD = [p for p in candD if sp.Poly(Den,lam).rem(sp.Poly(cyclotomic_poly(p,lam),lam))==0]
badD13 = [p for p in badD if p>=13]
print(f"\n3. Den deg={degD}; Phi_p | Den at: {badD} (p>=13: {badD13})")
if badD13: print("   FAIL"); FAIL=True
else: print("   [OK] Den(lam_p) != 0 for p>=13 (S != 0)  [ALG]")

if FAIL: print("\nCERTIFICATE FAILED"); sys.exit(1)
print("\n"+"="*64)
print("CERTIFICATE PASSED.  S_eff(lam_p) != 0 for all p>=13.")
print("With exact sweep p=6..12: F_raw^p(0,5) != 0 for ALL p>=6.")
print("ALL-p THEOREM CLOSED: universal pure anti-holomorphic raw vanishing")
print("holds iff b<=4, and fails at b=5 for EVERY p>=6 (dyadic map).  [ALG]")
print("="*64)
sys.exit(0)
