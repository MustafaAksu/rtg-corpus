#!/usr/bin/env python3
"""[SESSION] exploratory analysis of pilot.py output. Covariates were fixed before the pilot data were looked at.
usage: python3 -I analyse.py PILOT.jsonl N k TAIL_M"""
import sys, json, random, math
from collections import Counter
R = [json.loads(l) for l in open(sys.argv[1])]; N, k, TAIL = map(int, sys.argv[2:5])
def c(x): x %= N; return min(x, N - x)
def tau(x):
    for t in range(1, N + 1):
        if c(2 * x * t) <= k: return t
def cov(r):
    d = r["d0"]; P = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    return dict(deg=int(any(c(d[i] - d[j]) == 0 or c(d[i] + d[j]) == 0 for i, j in P)),
                n_slow=sum(c(2 * x) <= k for x in d),
                tau_min=min(tau(x) for x in d),
                n_diff_bind=sum(c(d[i] - d[j]) <= 2 * k for i, j in P),
                n_sum_bind=sum(c(d[i] + d[j]) <= 2 * k for i, j in P))
C = [cov(r) for r in R]; M = [r["M"] for r in R]; tail = [int(m >= TAIL) for m in M]
n = len(R); print(f"runs={n} N={N} k={k} tail(M>={TAIL})={sum(tail)} ({sum(tail)/n:.4f})  births>0: {sum(r['births']>0 for r in R)}  median M={sorted(M)[n//2]}  frozen(M<=5)={sum(m<=5 for m in M)}")
def rank(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); rk = [0.0] * len(v); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]: j += 1
        for t in range(i, j + 1): rk[o[t]] = (i + j) / 2
        i = j + 1
    return rk
def corr(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    sa = math.sqrt(sum((x - ma) ** 2 for x in a)); sb = math.sqrt(sum((y - mb) ** 2 for y in b))
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb) if sa and sb else float("nan")
rng = random.Random(1); rM = rank(M)
for name in C[0]:
    x = [ci[name] for ci in C]; rx = rank(x); rho = corr(rx, rM)
    perm = 0; B = 2000; y = rM[:]
    for _ in range(B):
        rng.shuffle(y); perm += abs(corr(rx, y)) >= abs(rho)
    lv = Counter(x); line = []
    for v in sorted(lv):
        idx = [i for i in range(n) if x[i] == v]
        line.append(f"{v}:n={len(idx)},tail={sum(tail[i] for i in idx)},medM={sorted(M[i] for i in idx)[len(idx)//2]}")
    print(f"{name:12s} spearman(M)={rho:+.3f} perm_p={(perm+1)/(B+1):.4f} | " + "  ".join(line[:16]))
# descriptive: token census concentration at end, tail vs bulk
def conc(r):
    cs = dict(r["census"]); tot = sum(cs.values()); cl = Counter()
    for y, m in cs.items(): cl[c(y)] += m
    return max(cl.values()) / tot, len(cl), len(cs)
for lab, sel in (("tail", [r for r, t in zip(R, tail) if t]), ("bulk", [r for r, t in zip(R, tail) if not t and r["births"] > 0])):
    if sel:
        cc = [conc(r) for r in sel]
        print(f"{lab}: n={len(sel)} mean top-class share={sum(x[0] for x in cc)/len(cc):.3f} mean #abs classes={sum(x[1] for x in cc)/len(cc):.2f} mean #distinct tokens={sum(x[2] for x in cc)/len(cc):.2f}")
