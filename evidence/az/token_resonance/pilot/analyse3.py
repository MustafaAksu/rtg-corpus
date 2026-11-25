#!/usr/bin/env python3
"""[SESSION] exploratory: tail rate by resonance order of seed tokens, o(x) = order of 2x in Z_N = N/gcd(2x,N).
usage: python3 -I analyse3.py PILOT.jsonl N k TAIL_M"""
import sys, json
from math import gcd, comb
from collections import Counter
R = [json.loads(l) for l in open(sys.argv[1])]; N, k, TAIL = map(int, sys.argv[2:5])
def c(x): x %= N; return min(x, N - x)
def o(x): return N // gcd(2 * x % N, N) if (2 * x) % N else 1
def dom(r):
    cl = Counter()
    for y, m in r["census"]: cl[c(y)] += m
    a, m = cl.most_common(1)[0]; return a, m / sum(cl.values())
n = len(R); tails = [r for r in R if r["M"] >= TAIL]
print(f"runs={n} tails(M>={TAIL})={len(tails)} rate={len(tails)/n:.4f}; capped={sum(r['steps']<800 for r in R)}")
print("order of 2a* for the dominant class of tail runs:", sorted(Counter(o(dom(r)[0]) for r in tails).items()))
print("dominant class a* of tail runs:", sorted(Counter(dom(r)[0] for r in tails).items()))
print("min top-class share among tail runs: %.3f ; bulk runs with share>=0.9: %d of %d" % (min(dom(r)[1] for r in tails), sum(dom(r)[1] >= .9 for r in R if r["M"] < TAIL), n - len(tails)))
def wilson(s, m, z=1.96):
    if m == 0: return (0, 0)
    p = s / m; d = 1 + z * z / m; ce = (p + z * z / (2 * m)) / d; h = z * ((p * (1 - p) / m + z * z / (4 * m * m)) ** .5) / d
    return (max(0, ce - h), min(1, ce + h))
def row(name, f):
    a = [r for r in R if f(r)]; t = sum(r["M"] >= TAIL for r in a); lo, hi = wilson(t, len(a))
    print(f"  {name:38s} n={len(a):5d} tails={t:4d} rate={t/max(1,len(a)):.4f}  95% [{lo:.4f},{hi:.4f}]")
print("tail rate by seed alphabet:")
row("no seed with o(x)<=2 (4x!=0)", lambda r: all(o(x) > 2 for x in r["d0"]))
row("some seed with o(x)<=2 (4x=0)", lambda r: any(o(x) <= 2 for x in r["d0"]))
row("  some seed x=0", lambda r: any(x % N == 0 for x in r["d0"]))
row("  some seed x=N/2", lambda r: any(x % N == N // 2 for x in r["d0"]))
row("  some seed x=+-N/4", lambda r: N % 4 == 0 and any(c(x) == N // 4 for x in r["d0"]))
for q in (3, 4, 5, 6, 8, 10, 12):
    row(f"min seed order o(x)=={q}", lambda r, q=q: min(o(x) for x in r["d0"]) == q)
row("min seed order o(x)>12", lambda r: min(o(x) for x in r["d0"]) > 12)
row("two seeds equal or opposite, all o>2", lambda r: all(o(x) > 2 for x in r["d0"]) and len({c(x) for x in r["d0"]}) < 4)
# median M by min order
print("median final M by min seed order:", [(q, sorted(r["M"] for r in R if min(o(x) for x in r["d0"]) == q)[len([r for r in R if min(o(x) for x in r["d0"]) == q]) // 2]) for q in sorted({min(o(x) for x in r["d0"]) for r in R})][:14])
# Fisher exact (one-sided) for 4x=0 vs not
A = [r for r in R if any(o(x) <= 2 for x in r["d0"])]; a = sum(r["M"] >= TAIL for r in A); b = len(A) - a
B = [r for r in R if all(o(x) > 2 for x in r["d0"])]; c_ = sum(r["M"] >= TAIL for r in B); d = len(B) - c_
tot = comb(a + b + c_ + d, a + c_); p = sum(comb(a + b, i) * comb(c_ + d, a + c_ - i) for i in range(a, min(a + b, a + c_) + 1)) / tot
print(f"Fisher exact one-sided p (4x=0 seeds enrich tails) = {p:.3e}; expected share of runs with a 4x=0 seed = {1-(1-(4 if N%4==0 else 2)/N)**4:.4f}, observed {len(A)/n:.4f}")
