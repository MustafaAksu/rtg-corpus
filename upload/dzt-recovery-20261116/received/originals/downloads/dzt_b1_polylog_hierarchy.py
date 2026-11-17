#!/usr/bin/env python3
"""
dzt_b1_polylog_hierarchy.py — Track B1, DZT-B1-1 log-corrected polylog audit.

After the pure-Li_2 W^(B) lead was falsified (v0.12: A=47/54 != 1 forces a log-correction),
this audits whether the log-corrected object is still transform-level or coefficient noise.

Radial asymptotics (from DYAD-RESP-DZT-004, DZT-verified):
  Q_m = 1/m - (7/54) ln m / m^2 + O(1/m^2),   7/54 = 1 - A,  A = 47/54.

W^(B) exponent series, to first correction:
  sum_m W_m z^m/m ~ Im(c21) [ Li_2(z) - (7/54) sum_m (ln m) z^m/m^3 + ... ]

KEY IDENTITY (verified here, algebraic + numeric):
  sum_{m>=1} (ln m) z^m / m^3 = - d/ds Li_s(z) |_{s=3}
  (since d/ds Li_s = sum z^m d/ds m^{-s} = - sum (ln m) z^m m^{-s}).

=> sum_m W_m z^m/m ~ Im(c21) [ Li_2(z) + (7/54) d/ds Li_s(z)|_{s=3} + O(next tower) ]
   a CONTROLLED polylog-derivative hierarchy; coefficient 7/54 = 1-A tied to certified A.

VERDICT (first correction): PASS — derivable from the recurrence, coefficient tied to a certified
germ invariant, expressible via the polylog-derivative Li_2, d_s Li_s|_{s=3}. Higher terms (quartic
B from c43/c16) REMAIN OPEN. Tag [ALG] for the first correction; full hierarchy [HEUR] pending B.
"""
import mpmath as mp
mp.mp.dps = 30

def verify_identity(z_test='0.5'):
    z = mp.mpf(z_test)
    direct = mp.nsum(lambda m: mp.log(m)*z**m/m**3, [1, mp.inf])
    h = mp.mpf('1e-8')
    minus_dLi = -(mp.polylog(3+h, z) - mp.polylog(3-h, z))/(2*h)
    return direct, minus_dLi, abs(direct - minus_dLi) < mp.mpf('1e-12')

if __name__ == "__main__":
    print("DZT-B1-1: log-corrected polylog audit")
    print("A = 47/54, log-correction coeff 1-A = 7/54\n")
    for zt in ['0.3','0.5','0.7']:
        d, md, ok = verify_identity(zt)
        print(f"  z={zt}: sum(ln m)z^m/m^3 = {mp.nstr(d,18)}  vs  -d_s Li_s|_3 = {mp.nstr(md,18)}  match={ok}")
    print("\nFirst-corrected exponent:")
    print("  sum W_m z^m/m ~ Im(c21)[ Li_2(z) + (7/54) d/ds Li_s(z)|_{s=3} + O(next tower) ]")
    print("VERDICT: first correction CONTROLLED [ALG] (polylog-derivative hierarchy, coeff = 1-A).")
    print("         higher terms REMAIN OPEN (need quartic B from c43/c16).")
