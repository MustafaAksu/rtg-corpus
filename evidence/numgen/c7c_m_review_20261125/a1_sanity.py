# Review sanity check for PR #383 A1/P2 (NUM, not a proof input). Canonical seed (1/100, 1/250) in U_D,base.
from mpmath import mp, mpf, sin, exp, atan2, sqrt, pi, floor
from collections import Counter
mp.dps = 40
def T(r, e): return r - sin(e), e + exp(r) - 1 - sin(e)
def theta(r, e): return atan2(sqrt(3)*e, 2*r - e)
r, e = mpf(1)/100, mpf(1)/250
N = 120000
th0 = theta(r, e); lift = th0; beta = 2*pi/3
nC = nP = nM = 0; maxdiff = 0; last_Bp = None; lags = Counter(); only = Counter(); dmin, dmax = 10, 0
for n in range(N):
    r1, e1 = T(r, e)
    d = theta(r1, e1) - theta(r, e)
    d = d - 2*pi*floor((d + pi)/(2*pi))          # principal value
    dmin, dmax = min(dmin, d), max(dmax, d)
    lift += d
    C = (r > 0) and (r1 <= 0)
    Bp = (e < 0) and (e1 >= 0) and (r > 0) and (r1 > 0)
    Bm = (e > 0) and (e1 <= 0) and (r < 0) and (r1 < 0)
    nC += C; nP += Bp; nM += Bm
    if Bp: last_Bp = n + 1
    if C and last_Bp is not None: lags[n + 1 - last_Bp] += 1; last_Bp = None
    only[(C, Bp, Bm)] += 1
    # floor formula check for C
    fC = int(floor((lift - beta)/(2*pi)) - floor((th0 - beta)/(2*pi)))
    if fC != nC: raise SystemExit(f"floor formula mismatch at step {n}")
    maxdiff = max(maxdiff, abs(nC - nP))
    r, e = r1, e1
print("steps", N, "N_C", nC, "N_+", nP, "N_-", nM, "max|N_C-N_+|", maxdiff)
print("delta_T range", float(dmin), float(dmax), "(L-MONO: pi/6..pi/2 =", float(pi/6), float(pi/2), ")")
print("same-revolution lag B+ -> next C_r:", dict(lags))
print("token classes (C, B+, B-):", {str(k): v for k, v in only.items()})
