# Independent audit: q=4,(0,3) cascade norm N+(M_p) from the Dyadic closed form
# Q(L,I) = L^5 (I L^2 + I - L^2 + 1) / (2 (L+1)^4 (L^2+L+1)),  I = zeta_p^{p/4}
# M_p = Q_p / (i zeta_p^3);  N+ = prod over Gal(Q(zeta_p)^+/Q) of conjugates.
# Checks: (a) anomaly law: odd part of numerator = ell^2 iff p = 8*ell^a, ell^a = 1 mod 4, else 1
#         (b) denominator law: d_p = phi(p)/4 + [p=2^k] + [p=3*2^k]
from mpmath import mp, mpc, exp, pi, fabs
from math import gcd
mp.dps = 60

def phi(n):
    r, m, d = 1, n, 2
    res = n
    while d*d <= m:
        if m % d == 0:
            res -= res // d
            while m % d == 0: m //= d
        d += 1
    if m > 1: res -= res // m
    return res

def is_pow2(n):
    return n & (n-1) == 0

def odd_prime_power(n):
    # return (ell, a) if n = ell^a with ell odd prime, else None
    if n % 2 == 0 or n < 3: return None
    d = 3
    m = n
    while d*d <= m:
        if m % d == 0:
            a = 0
            while m % d == 0: m //= d; a += 1
            return (d, a) if m == 1 else None
        d += 2
    return (n, 1)

def Qval(L, I):
    return L**5 * (I*L**2 + I - L**2 + 1) / (2*(L+1)**4*(L**2+L+1))

results = []
for p in range(12, 252, 4):
    z = exp(2j*pi/p)
    s = p//4
    reps = [k for k in range(1, p//2) if gcd(k, p) == 1]
    N = mp.mpf(1)
    ok_real = True
    for k in reps:
        Lk = z**k
        Ik = z**(k*s)
        Mk = Qval(Lk, Ik) / (Ik * Lk**3)
        if fabs(Mk.imag) > mp.mpf(10)**(-40): ok_real = False
        N *= Mk.real
    # predicted denominator exponent
    d_pred = phi(p)//4 + (1 if is_pow2(p) else 0) + (1 if (p % 3 == 0 and is_pow2(p//3)) else 0)
    scaled = N * mp.mpf(2)**d_pred
    num = int(mp.nint(scaled))
    exact = fabs(scaled - num) < mp.mpf(10)**(-30)
    # predicted numerator
    opp = odd_prime_power(p//8) if p % 8 == 0 else None
    anomalous = opp is not None and pow(opp[0], opp[1], 4) == 1
    num_pred = opp[0]**2 if anomalous else 1
    results.append((p, d_pred, num, num_pred, exact, ok_real, anomalous))

print(f"{'p':>4} {'d_p':>4} {'num(2^d*N+)':>12} {'pred':>6} {'int?':>5} {'real?':>6} {'anom?':>6} {'match':>6}")
fails = 0
for p, d, num, npred, exact, okr, anom in results:
    match = (abs(num) == npred)
    if not (match and exact and okr): fails += 1
    flag = "" if (match and exact and okr) else "  <-- MISMATCH"
    print(f"{p:>4} {d:>4} {num:>12} {npred:>6} {str(exact):>5} {str(okr):>6} {str(anom):>6} {str(match):>6}{flag}")
print(f"\nPoints audited: {len(results)}, mismatches: {fails}")
print("Anomalous points found:", [p for p,_,n,_,_,_,a in results if a])
