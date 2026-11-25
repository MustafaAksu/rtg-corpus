#!/usr/bin/env python3
"""[SESSION] exploratory pilot for the BOOTSTRAP 4 advisory; not evidence, not a result, seeds must not be reused in a
confirmatory run. Records seed tokens and outcomes of bound_symmetric runs (v2.12.14 orientation).
usage: python3 -I pilot.py ENGINE.py ORIENT.py OUT.jsonl N k T CAP BUDGET_SECONDS MASTER_SEED"""
import sys, importlib.util, random, time, json
from collections import Counter
def load(path, name):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m; sp.loader.exec_module(m); return m
eng = load(sys.argv[1], "eng"); ori = load(sys.argv[2], "ori"); eng.orient_path = ori.make_orient(eng)
out, N, k, T, cap, budget, ms = sys.argv[3], *map(int, sys.argv[4:10])
master = random.Random(ms); t0 = time.time(); n = 0
with open(out, "w") as f:
    while time.time() - t0 < budget:
        seed = master.randrange(10**12); rng = random.Random(seed)
        u = eng.init_universe(N=N, k=k, rng=rng)
        th0 = [u.theta[i] for i in range(4)]; d0 = [u.delta[i] for i in range(4)]
        fb = None; first_event = None
        for _ in range(T):
            if len(u.theta) >= cap: break
            eng.step_universe(u, multistar_policy="bound_symmetric")
            if first_event is None and (u.single_edge_swaps or u.path_interactions or u.births or u.multistar_seen or u.path_ties_seen):
                first_event = u.steps
            if fb is None and u.births: fb = u.steps
        f.write(json.dumps(dict(seed=seed, th0=th0, d0=d0, births=u.births, M=len(u.theta), steps=u.steps, fb=fb,
                                fe=first_event, ms_bound=u.multistar_bound, census=sorted(Counter(u.delta.values()).items()))) + "\n")
        f.flush(); n += 1
print("runs", n, "time", round(time.time() - t0, 1))
