#!/usr/bin/env python3
"""Session-only independent rational gate for RECOG R2 source-constant discharge.

This checks sufficient rational bounds for the explicit NF6/NF-REM majorant
formulas used in RECOG v0.3.26 §6.13b (COMBINED-TAIL G2). It does not
re-execute owner certificates or establish physical interpretation.
"""
from fractions import Fraction as F

q = F(256, 140625)
# All square-root comparisons below are exact rational square comparisons.
sqrt3_hi = F(1732051, 1000000)
mu_lo, mu_hi = F(12583, 10000), F(1259, 1000)
a32_lo, a32_hi = F(10768, 10000), F(1077, 1000)
a05_lo, a05_hi = F(2128, 100000), F(213, 10000)
mu2 = F(19, 12)
a32_2 = F(97, 432)**2 + 3*F(197, 324)**2
a05_2 = F(49, 8640)**2 + 3*F(307, 25920)**2
assert sqrt3_hi**2 > 3
assert mu_lo**2 < mu2 < mu_hi**2
assert a32_lo**2 < a32_2 < a32_hi**2
assert a05_lo**2 < a05_2 < a05_hi**2
A5_lo = a32_lo + a05_lo
A5_hi = a32_hi + a05_hi
assert A5_lo == F(109808,100000)
assert A5_hi == F(10983,10000)

def c7_of_u(u):
    w = 100*q**3/(1-u)
    assert 0 <= u < 1 and w < 1
    return F(100)/(1-u)/(1-w)

u_lo = mu_lo*q + A5_lo*q*q
u_hi = mu_hi*q + A5_hi*q*q
c7_lo, c7_hi = c7_of_u(u_lo), c7_of_u(u_hi)
# For cJ we bound: |Im(a32-mu^2/2)| + |a05| + |mu|A5 q
# + A5^2 q^2/2 + |u|^3/[3(1-|u|)q^2].
cJ_hi = (F(89,324)*sqrt3_hi + a05_hi + mu_hi*A5_hi*q
         + A5_hi**2*q**2/2 + u_hi**3/(3*(1-u_hi)*q*q))

checks = {
    "R2_CJ_CERTIFIABLE_BELOW_DYAD_0.50220": cJ_hi < F(50220,100000),
    "R2_C7_CERTIFIABLE_BELOW_DYAD_157.58": c7_hi < F(15758,100),
    "R2_C7_CERTIFIABLE_AT_OUTWARD_100.231": c7_hi < F(100231,1000),
    "R2_C7_FORMULA_EXCEEDS_PRINTED_100.23": c7_lo > F(10023,100),
    "NEG_CONTROL_TOO_SMALL_100.23_REJECTED": not (c7_hi <= F(10023,100)),
    "R2_JET_DISK_WITHIN_ROW_A": q < F(1,400),
}
for label, yes in checks.items():
    print(f"{label}: {'PASS' if yes else 'FAIL'}")
print("CJ_UPPER_approx", format(float(cJ_hi), '.12f'))
print("C7_FORMULA_LOWER_approx", format(float(c7_lo), '.12f'))
print("C7_FORMULA_UPPER_approx", format(float(c7_hi), '.12f'))
assert all(checks.values())
