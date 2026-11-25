#!/usr/bin/env python3
"""[SESSION] exploratory: arithmetic of the dominant token class in tail runs versus the seed-token baseline.
usage: python3 -I analyse2.py PILOT.jsonl N k TAIL_M"""
import sys, json
from math import gcd
from collections import Counter
R = [json.loads(l) for l in open(sys.argv[1])]; N, k, TAIL = map(int, sys.argv[2:5])
def c(x): x %= N; return min(x, N - x)
def tau(x):
    for t in range(1, N + 1):
        if c(2 * x * t) <= k: return t
def dom(r):
    cl = Counter()
    for y, m in r["census"]: cl[c(y)] += m
    a, m = cl.most_common(1)[0]; return a, m / sum(cl.values())
def feat(a): return (c(2 * a), gcd(2 * a, N), tau(a))
tails = [r for r in R if r["M"] >= TAIL]; bulk = [r for r in R if r["M"] < TAIL and r["births"] > 0]
print("tail runs:", len(tails), " bulk:", len(bulk))
share_t = sorted(dom(r)[1] for r in tails); share_b = sorted(dom(r)[1] for r in bulk)
q = lambda v, p: v[min(len(v) - 1, int(p * len(v)))] if v else None
print("top-class share  tail: min/median/max = %.3f / %.3f / %.3f" % (share_t[0], q(share_t, .5), share_t[-1]) if tails else "no tails")
print("top-class share  bulk: q05/median/q95/max = %.3f / %.3f / %.3f / %.3f" % (q(share_b, .05), q(share_b, .5), q(share_b, .95), share_b[-1]))
thr = 0.9
print(f"classifier 'share>={thr}': tail TP={sum(s>=thr for s in share_t)}/{len(share_t)}  bulk FP={sum(s>=thr for s in share_b)}/{len(share_b)}")
print("tail runs: dominant class a*, share, |2a*|_c, gcd(2a*,N), tau(a*), seeds |d0|_c, M, fb")
for r in tails[:40]:
    a, s = dom(r); print("  a*=%3d share=%.3f |2a|=%3d gcd=%3d tau=%2d seeds=%s M=%d fb=%s" % (a, s, *feat(a), sorted(c(x) for x in r["d0"]), r["M"], r["fb"]))
# baseline: features over all seed tokens of all runs, vs dominant classes of tail runs
base = Counter(); tl = Counter()
for r in R:
    for x in r["d0"]: base["slow(|2a|<=k)" if c(2 * x) <= k else "mid(k<|2a|<=2k+1)" if c(2 * x) <= 2 * k + 1 else "fast(|2a|>2k+1)"] += 1
for r in tails:
    a, _ = dom(r); tl["slow(|2a|<=k)" if c(2 * a) <= k else "mid(k<|2a|<=2k+1)" if c(2 * a) <= 2 * k + 1 else "fast(|2a|>2k+1)"] += 1
nb = sum(base.values()); nt = sum(tl.values()) or 1
for key in ("slow(|2a|<=k)", "mid(k<|2a|<=2k+1)", "fast(|2a|>2k+1)"):
    print(f"  {key:20s} seed baseline {base[key]/nb:.3f}   tail dominant class {tl[key]/nt:.3f} (n={tl[key]})")
# is the dominant class a seed class? and tail rate by 'has a slow seed'
print("dominant class is a seed class in all tail runs:", all(dom(r)[0] in {c(x) for x in r["d0"]} for r in tails))
for name, f in (("has slow seed", lambda r: any(c(2 * x) <= k for x in r["d0"])), ("has seed with tau<=2", lambda r: any(tau(x) <= 2 for x in r["d0"]))):
    a = [r for r in R if f(r)]; b = [r for r in R if not f(r)]
    print(f"  {name}: yes n={len(a)} tail={sum(r['M']>=TAIL for r in a)} ({sum(r['M']>=TAIL for r in a)/max(1,len(a)):.4f}) | no n={len(b)} tail={sum(r['M']>=TAIL for r in b)} ({sum(r['M']>=TAIL for r in b)/max(1,len(b)):.4f})")
