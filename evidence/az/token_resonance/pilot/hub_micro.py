#!/usr/bin/env python3
"""[SESSION] scratch micro-test: an isolated hub K_{1,3} whose four nodes share one token x. Births over T ticks.
usage: python3 -I hub_micro.py ENGINE.py ORIENT.py N k T"""
import sys, importlib.util
def load(path, name):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m; sp.loader.exec_module(m); return m
eng = load(sys.argv[1], "eng"); ori = load(sys.argv[2], "ori"); eng.orient_path = ori.make_orient(eng)
N, k, T = map(int, sys.argv[3:6])
from math import gcd
res = {}
for x in range(N):
    # state given AFTER an advance is what the engine sees after its own advance; start one tick earlier
    th = {0: (0 - x) % N, 1: (N // 2 - x) % N, 2: (N // 2 - x) % N, 3: (N // 2 - x) % N}
    u = eng.Universe(N=N, k=k, theta=dict(th), delta={i: x for i in range(4)})
    for _ in range(T): eng.step_universe(u, multistar_policy="bound_symmetric")
    res[x] = u.births
by = {}
for x, b in res.items(): by.setdefault(b, []).append(x)
for b in sorted(by, reverse=True)[:8]:
    xs = by[b]; print(f"births in {T} ticks = {b:4d}: {len(xs):3d} tokens; e.g. {xs[:10]}; orders of 2x: {sorted({N//gcd(2*x%N,N) if 2*x%N else 1 for x in xs})[:10]}")
