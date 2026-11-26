# Review check (one step only; no trajectory or cycle computed): the #386 comment-7174411169 sector lemma,
# with the pinned v18 engine + tdrg-v2.13 reference orient, N=24, k=1, bound_symmetric, births NOT suppressed.
import importlib.util, sys, hashlib, itertools
root = sys.argv[1]
def load(n, p):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); sys.modules[n] = m; s.loader.exec_module(m); return m
ep, op = f"{root}/upload/tdrg-records/genesis_mode_b_mc_v18.py", f"{root}/evidence/tdrg/scripts/tdrg_orient_v2_12_14.py"
for p in (ep, op): print(p.split('/')[-1], hashlib.sha256(open(p, 'rb').read()).hexdigest())
eng = load("eng", ep); ref = load("ref", op); eng.orient_path = ref.make_orient(eng)
N, k = 24, 1
def in_sector(th, dl):
    return len(th) == 4 and all(th[j] % 6 == j for j in range(4)) and sorted(dl) == [0, 6, 12, 18]
def step(pre, dl):
    u = eng.Universe(N=N, k=k, theta=dict(enumerate(pre)), delta=dict(enumerate(dl)))
    c0 = (u.single_edge_swaps, u.path_interactions, u.path_ties_bound)
    eng.step_universe(u, multistar_policy="bound_symmetric")
    c1 = (u.single_edge_swaps, u.path_interactions, u.path_ties_bound)
    return u, tuple(u.theta[i] for i in sorted(u.theta)), tuple(u.delta[i] for i in sorted(u.delta)), tuple(b - a for a, b in zip(c0, c1))
bad, stats, n = [], {}, 0
for a in itertools.product(range(4), repeat=4):
    for b in itertools.permutations(range(4)):
        dl = tuple(6 * x for x in b); pre = tuple((j + 6 * a[j]) % N for j in range(4)); n += 1
        post = tuple((pre[j] + k * dl[j]) % N for j in range(4))
        edges = [(i, j) for i in range(4) for j in range(i + 1, 4) if eng.is_defect(post[i], post[j], N, k)]
        pred = [(j, j + 1) for j in range(3) if (b and ((a[j + 1] + b[j + 1]) - (a[j] + b[j])) % 4 == 2)]
        u, th, d2, dc = step(pre, dl)
        deg = max([sum(1 for e in edges if v in e) for v in range(4)] or [0])
        ok = in_sector(th, d2) and u.births == 0 and set(edges) <= {(0, 1), (1, 2), (2, 3)} and edges == pred and deg <= 2 and dc[2] == 0
        if not ok: bad.append((a, b, edges, th, d2, u.births, dc))
        comp = tuple(sorted(len(c) for c in __import__('collections').Counter() or [] ))
        key = ("edges=%d" % len(edges), dc[:2]); stats[key] = stats.get(key, 0) + 1
print("states checked", n, "failures", len(bad), bad[:3])
print("one-step (edge count, (swap, path) increments):", dict(sorted(stats.items())))
# the three static controls (snapshot tokens (0,6,12,18) -> pre = post - tokens)
for post in [(0, 13, 14, 15), (0, 13, 2, 3), (0, 13, 2, 15)]:
    dl = (0, 6, 12, 18); pre = tuple((p - k * x) % N for p, x in zip(post, dl))
    u, th, d2, dc = step(pre, dl); print("post", post, "->", d2, "(swap, path, tie) +", dc, "births", u.births)
