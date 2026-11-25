"""
APEX-RATIO COMPUTATION (certified-input scope).

Question: can the out-of-plane apex source channel (T-6t, independent) supply the
x2 factor the in-plane SU(2) channel cannot (AUDIT-1-DIMENSIONAL: OPEN-M ~2x short)?

Ratio: Rho_apex = ||H_apex|| / ||H_in-plane||, denominator = T-6s certified value 1.

CERTIFIED INPUTS:
 - T-6t: 3 orthogonal Jacobi modes; canonical Gram G_can = diag(2, 8/3, 3) for
   (s, c, d); apex d out-of-plane, chirality free. (verified, 13/13 checks)
 - T-6s: in-plane source ||H||_B = |1-g_2| <= 1, max 1 at g_2=0. Denominator = 1.
 - Genesis HINDEX: ||H||_B^2 = lam_max(B^{-1} H^T B^{-1} H), B = [[1,-1/2],[-1/2,1]] (2x2).

DEFINITIONAL FINDING: the HINDEX B-norm is 2x2 (in-plane). Norming an out-of-plane
apex source B-natively would require a 3x3 extension of B, which NO project DSN
defines. The ONLY certified 3-mode metric is G_can. So the certified-input ratio
uses canonical-Gram weights; a B-native apex norm is UV content (OPEN-M), not
computable now without invention.
"""
import sympy as sp
from sympy import Rational as R, sqrt, diag

G_can = diag(2, R(8,3), 3)      # (s, c, d) canonical weights, T-6t verified
w_s, w_c, w_d = 2, R(8,3), 3

ratio_vs_s = sqrt(R(w_d, w_s))        # sqrt(3/2)
ratio_vs_c = sqrt(w_d / w_c)          # sqrt(9/8)
target = 2

print("Canonical mode weights (s,c,d):", w_s, w_c, w_d)
print(f"apex/in-plane amplitude ratio:")
print(f"  vs s-anchor: sqrt(w_d/w_s) = sqrt(3/2) = {float(ratio_vs_s):.4f}")
print(f"  vs c-anchor: sqrt(w_d/w_c) = sqrt(9/8) = {float(ratio_vs_c):.4f}")
print(f"target to close OPEN-M gap: {target}")
print(f"VERDICT: max apex ratio sqrt(3/2) ~ {float(ratio_vs_s):.3f} < 2 -> FALLS SHORT")
assert float(ratio_vs_s) < 2
print("\nCERTIFIED-INPUT RESULT: apex channel supplies at most ~1.22x under canonical-")
print("Gram normalization; does NOT close the missing x2. A B-native apex norm is")
print("OPEN-M UV content (needs a 3x3 B-extension no DSN defines) -> that branch OPEN.")
print("ALL CHECKS PASS")
