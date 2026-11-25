#!/usr/bin/env python3
"""[SESSION] scratch check for the BOOTSTRAP 4 advisory; not evidence, not placed in the repository.
A: token-alphabet containment and monotone census on the placed TDR-G engine, all policies, both orientation rules.
usage: python3 -I alphabet_check.py ENGINE.py ORIENT.py"""
import sys, importlib.util, random, time
from collections import Counter
def load(path, name):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m; sp.loader.exec_module(m); return m
eng = load(sys.argv[1], "eng"); ori = load(sys.argv[2], "ori")
v18_orient = eng.orient_path
POL = ["trap", "bound_multistar", "bound_symmetric", "largest_center", "all_centers"]
def run(N, k, T, seed, pol, cap=400):
    rng = random.Random(seed); u = eng.init_universe(N=N, k=k, rng=rng)
    A0 = set(u.delta.values()) | {(-d) % N for d in u.delta.values()}
    cen = Counter(u.delta.values()); viol = 0; births_seen = 0
    for _ in range(T):
        if len(u.theta) >= cap: break
        b0 = u.births
        eng.step_universe(u, multistar_policy=pol)
        c2 = Counter(u.delta.values())
        if not set(c2) <= A0: viol += 1
        if any(c2[y] < cen[y] for y in cen): viol += 1
        if sum(c2.values()) - sum(cen.values()) != u.births - b0: viol += 1
        cen = c2
    return viol, u.births, len(set(u.delta.values())), len(u.theta)
t0 = time.time(); tot = 0; bad = 0; maxdistinct = 0; births = 0
for oname, of in (("v18", v18_orient), ("v2.12.14", ori.make_orient(eng))):
    eng.orient_path = of
    for N, k in ((24, 1), (24, 3), (60, 4), (120, 8), (240, 16)):
        for pol in POL:
            for r in range(60):
                v, b, nd, M = run(N, k, 300, 7_000_000 + 1000*N + 17*k + r, pol)
                tot += 1; bad += (v > 0); maxdistinct = max(maxdistinct, nd); births += b
print(f"runs={tot} runs_with_violation={bad} total_births={births} max_distinct_tokens={maxdistinct} (bound 8) time={time.time()-t0:.1f}s")
