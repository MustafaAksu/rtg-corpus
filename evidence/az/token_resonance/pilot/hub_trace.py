import sys, importlib.util
from collections import Counter
def load(path, name):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m; sp.loader.exec_module(m); return m
eng = load(sys.argv[1], "eng"); ori = load(sys.argv[2], "ori"); eng.orient_path = ori.make_orient(eng)
N, k, T, x = map(int, sys.argv[3:7])
th = {0: (0 - x) % N, 1: (N // 2 - x) % N, 2: (N // 2 - x) % N, 3: (N // 2 - x) % N}
u = eng.Universe(N=N, k=k, theta=dict(th), delta={i: x for i in range(4)})
for t in range(T):
    b0 = u.births; eng.step_universe(u, multistar_policy="bound_symmetric")
    sites = Counter((u.theta[i], u.delta[i]) for i in u.theta)
    print(t + 1, "births", u.births - b0, "M", len(u.theta), "sites(theta,delta):count", sorted(sites.items())[:10])
