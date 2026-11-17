#!/usr/bin/env python3
"""Compare the C++ kernel's enclosures of F^k (k = 1, 10, 20) at one complex point with 320-digit mpmath values.
Usage: python3 -I check_oracle.py probe_oracle_endpoints.txt"""
import sys, mpmath as mp
mp.mp.dps = 320
S = mp.mpf(2) ** 256
r = mp.mpc(mp.mpf(3) / 100, mp.mpf(1) / 100); e = mp.mpc(mp.mpf(-2) / 100, mp.mpf(1) / 200)
def T(r, e):
    s = mp.sin(e); return r - s, e + mp.exp(r) - 1 - s
def F(r, e):
    for _ in range(6):
        r, e = T(r, e)
    return r, e
h = mp.mpf('1e-150'); vals = {}; x = (r, e); xp = (r + h, e); xm = (r - h, e)
for k in range(1, 21):
    x = F(*x); xp = F(*xp); xm = F(*xm)
    if k in (1, 10, 20):
        vals[k] = dict(rr=x[0].real, ri=x[0].imag, er=x[1].real, ei=x[1].imag, dr=((xp[0] - xm[0]) / (2 * h)).real)
k, bad = None, 0
for L in open(sys.argv[1]).read().split('\n'):
    t = L.split()
    if not t:
        continue
    if t[0] == 'k':
        k = int(t[1]); continue
    lo, hi = mp.mpf(int(t[1])) / S, mp.mpf(int(t[2])) / S
    ok = lo <= vals[k][t[0]] <= hi; bad += not ok
    print(k, t[0], 'contained' if ok else 'NOT CONTAINED', 'width %.3e' % float(hi - lo))
print('RESULT', 'PASS' if bad == 0 else 'FAIL'); sys.exit(1 if bad else 0)
