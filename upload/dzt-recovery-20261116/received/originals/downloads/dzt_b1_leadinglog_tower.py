#!/usr/bin/env python3
"""
dzt_b1_leadinglog_tower.py — Track B1 (DZT-B1-1 extension): the controlled leading-log hierarchy.

FINDING: the W^(B) log-corrected local zeta splits into
  (i) a CONTROLLED leading-log tower determined by the certified backbone A alone (B-FREE), and
  (ii) orbit-dependent plain-polylog companions (NOT germ invariants).

Radial recurrence Q_{m+1}=Q_m-Q_m^2+A Q_m^3+B Q_m^4+..., A=47/54 certified.
Leading-log coefficients of Q_m = 1/m + sum_r c_r (ln m)^r/m^{r+1} + (orbit-dependent + subleading):
  c_1 = A-1            [symbolically certified, 1/m^3 L^0 balance]
  c_2 = (A-1)^2        [symbolically certified, 1/m^4 L^2 balance: c1^2 - c2 = 0]
  c_r = (A-1)^r        [all-order: closed-form leading-log resummation, verified below]

CLOSED-FORM leading-log resummation:
  Q_m^{LL} = 1/(m - (A-1) ln m)   (geometric sum of c_r=(A-1)^r terms)
  -> satisfies the recurrence to leading-log order at every power of 1/m; the residual is
     SUBLEADING-log (~ ln m / m^4) and B-INSENSITIVE -> leading-log tower is A-determined, B-free.

Mapping to the zeta exponent (via sum_m (ln m)^r z^m/m^k = (-1)^r d_s^r Li_s|_{s=k}, |z|<1):
  controlled exponent = Im(c21) * sum_{r>=0} (1-A)^r d_s^r Li_s(z)|_{s=r+2}
    r=0: Li_2 ;  r=1: (1-A) d_s Li_s|_3 = (7/54) d_s Li_s|_3 ;  r=2: (1-A)^2 d_s^2 Li_s|_4 ; ...
  orbit-dependent companions: d*Li_3 + ... (coeffs NOT germ-invariant; from the 1/m^2 constant etc.)

CONSEQUENCE: the leading-log hierarchy is DZT-native (needs only the certified A), no Dyadic
request required. The quartic B affects only subleading-log / orbit-dependent terms.
"""
import mpmath as mp
mp.mp.dps = 30

def residual_scaled(M, A, B):
    L = mp.log(M)
    q  = 1/(M - (A-1)*L)
    q1 = 1/((M+1) - (A-1)*mp.log(M+1))
    r  = q1 - (q - q*q + A*q**3 + B*q**4)
    return r / (L/M**3)   # residual relative to the leading-log order ln m/m^3

if __name__ == "__main__":
    A = mp.mpf(47)/54
    print(f"A = 47/54 = {mp.nstr(A,10)},  A-1 = {mp.nstr(A-1,10)},  1-A = 7/54 = {mp.nstr(1-A,10)}")
    print("\nleading-log resummation residual / (ln m / m^3)  [-> 0 means LL-tower exact, B-free]:")
    for B in [mp.mpf(0), mp.mpf(5)]:
        for e in [6, 8, 10]:
            M = mp.mpf(10)**e
            print(f"  B={float(B):>3}  m=1e{e:<2}: {mp.nstr(residual_scaled(M,A,B),6)}")
    print("\n=> residual ~ ln m/m^4 (one power below leading-log) and B-insensitive at leading-log")
    print("   => Q^LL = 1/(m-(A-1)ln m) is the closed-form leading-log tower, A-determined, B-free.")
