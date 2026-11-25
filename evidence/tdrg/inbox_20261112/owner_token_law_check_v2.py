#!/usr/bin/env python3
"""TDR-G owner-session check, round 2 (12 Nov 2026), answering the ChatGPT co-owner review of PR #243.

Same engine, scope, seeds and run plan as owner_token_law_check.py (v1). Changes:
  - Cor. 1.1 / 1.2 (unlabelled |d_ij|_c multiset) are compared on EVERY tick (v1 skipped ticks with M_post > 70);
  - the parent of each birth is taken from the engine's own blow_up_star_with_snapshot call (wrapped, not
    re-implemented), so Prop. 2 is checked with exact birth provenance (v1 matched candidate parents);
  - every claim reports the number of ticks / events on which it was actually checked;
  - fixtures: (F1) the ChatGPT N4 example, a five-node tailed tree that the engine blows up as a single star;
          (F2) the ChatGPT TDR-6 counterexample, D(C) = D(C') but different birth increments, realised on the
          engine with one shared post-advance defect geometry.
usage: python3 -I owner_token_law_check_v2.py ENGINE_V18.py ORIENT_REF.py [RUNS_PER_CELL]
"""
import importlib.util, json, random, sys
from collections import Counter

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); sys.modules[n] = m
    s.loader.exec_module(m); return m

eng = load(sys.argv[1], "eng"); ref = load(sys.argv[2], "ref")
eng.orient_path = ref.make_orient(eng)
RUNS = int(sys.argv[3]) if len(sys.argv) > 3 else 30
POL = ["trap", "bound_multistar", "bound_path_tie", "bound_symmetric", "largest_center", "all_centers"]

BIRTHS = []   # (centre, child id) from the engine's own call
_orig_blow = eng.blow_up_star_with_snapshot
def blow_spy(u, center, theta_pre, delta_pre, next_id):
    BIRTHS.append((center, next_id)); return _orig_blow(u, center, theta_pre, delta_pre, next_id)
eng.blow_up_star_with_snapshot = blow_spy

shapes = Counter()
_orig_cls = eng.classify_component
def cls_spy(comp, adj):
    ctype, centers = _orig_cls(comp, adj); s = set(comp)
    if ctype.startswith("star_k1c_"):
        deg = len(adj[centers[0]] & s); e = sum(len(adj[v] & s) for v in comp) // 2
        shapes[("star pure K_1,3" if deg == 3 else "star pure K_1,>=4") if len(comp) == deg + 1 else
               ("star with extra nodes, tree" if e == len(comp) - 1 else "star with extra nodes, contains a cycle")] += 1
    elif ctype.startswith("multistar_"):
        shapes["multistar"] += 1
    return ctype, centers
eng.classify_component = cls_spy

def cd(a, b, N):
    d = (a - b) % N; return min(d, N - d)

def D_of(toks, N):
    t = sorted(toks); return Counter(cd(t[i], t[j], N) for i in range(len(t)) for j in range(i + 1, len(t)))

n = Counter(); viol = Counter()
rng = random.Random(20261112)          # same seed and draw order as v1
for pol in POL:
    for N, k in ((24, 1), (30, 2), (60, 4), (120, 8)):
        for r in range(RUNS):
            u = eng.Universe(N=N, k=k, theta={i: rng.randrange(N) for i in range(4)},
                             delta={i: rng.randrange(N) for i in range(4)})
            S0 = set(u.delta.values()) | {(-x) % N for x in u.delta.values()}
            pc = {}
            for t in range(400):
                if len(u.theta) >= 70: break
                C = Counter(u.delta.values()); dpre = dict(u.delta); BIRTHS.clear()
                eng.step_universe(u, multistar_policy=pol); n["ticks"] += 1
                xs = [dpre[c] for c, _ in BIRTHS]
                if any(u.delta[ch] != dpre[c] or u.delta[c] != (-dpre[c]) % N for c, ch in BIRTHS): viol["star map"] += 1
                n["births"] += len(BIRTHS); n["birth_ticks" if BIRTHS else "birth_free_ticks"] += 1
                n["P1 census checked"] += 1
                if Counter(u.delta.values()) != C + Counter((-x) % N for x in xs): viol["P1 census"] += 1
                n["P1a alphabet checked"] += 1
                if not set(u.delta.values()) <= S0: viol["P1a alphabet"] += 1
                Dexp = D_of(list(C.elements()), N)
                for a, x in enumerate(xs):
                    for y in C.elements(): Dexp[cd((-x) % N, y, N)] += 1
                    for b in range(a + 1, len(xs)): Dexp[cd(x, xs[b], N)] += 1
                ok = D_of(list(u.delta.values()), N) == Dexp
                if BIRTHS:
                    n["Cor1.1 injection checked (birth ticks)"] += 1; viol["Cor1.1 injection"] += not ok
                    n["max M_post on a checked birth tick"] = max(n["max M_post on a checked birth tick"], len(u.theta))
                else:
                    n["Cor1.2 conservation checked (birth-free ticks)"] += 1; viol["Cor1.2 conservation"] += not ok
                for c, ch in BIRTHS:
                    pc[ch] = (c, dpre[c], 0)
                    if (u.theta[ch] - u.theta[c]) % N != N // 2: viol["P2 j=0"] += 1
                for ch, (pa, x, j) in list(pc.items()):
                    if any(ch == b for _, b in BIRTHS): continue
                    if dpre.get(ch) == x and dpre.get(pa) == (-x) % N:   # tokens used by this tick's advance
                        j += 1; pc[ch] = (pa, x, j); n["P2 phase checked (provenance-exact)"] += 1
                        if (u.theta[ch] - u.theta[pa]) % N != (N // 2 + 2 * j * x) % N: viol["P2 phase"] += 1
                        if not (u.delta.get(ch) == x and u.delta.get(pa) == (-x) % N): del pc[ch]
                    else:
                        del pc[ch]

fx = {}
# F1: ChatGPT N4 example, post-advance theta=(0,11,12,13,22), N=24, k=1, tokens 0 -> theta_pre = theta_post
BIRTHS.clear(); shapes_before = dict(shapes)
u = eng.Universe(N=24, k=1, theta={0: 0, 1: 11, 2: 12, 3: 13, 4: 22}, delta={i: 0 for i in range(5)})
eng.step_universe(u, multistar_policy="bound_symmetric")
fx["F1 tailed tree blown up as single star (centre 0)"] = (BIRTHS == [(0, 5)])
fx["F1 classified as star with extra nodes, tree"] = shapes["star with extra nodes, tree"] == shapes_before.get("star with extra nodes, tree", 0) + 1
# F2: TDR-6 counterexample on one shared geometry: centre 0 (post-advance theta 0) with leaves at 12 (k=1 band)
def realise(C):
    post = {0: 0, 1: 11, 2: 12, 3: 13}
    th = {i: (post[i] - C[i]) % 24 for i in range(4)}
    u = eng.Universe(N=24, k=1, theta=th, delta={i: C[i] for i in range(4)})
    D0 = D_of(C, 24); BIRTHS.clear(); eng.step_universe(u, multistar_policy="bound_symmetric")
    return D0, D_of(list(u.delta.values()), 24) - D0, list(BIRTHS)
d0a, inca, ba = realise([1, 3, 4, 5]); d0b, incb, bb = realise([2, 4, 5, 6])
fx["F2 D(C) == D(C')"] = d0a == d0b
fx["F2 D(C)"] = sorted(d0a.elements())
fx["F2 birth increment C"] = sorted(inca.elements()); fx["F2 birth increment C'"] = sorted(incb.elements())
fx["F2 increments differ"] = inca != incb
fx["F2 both birth at centre 0"] = (ba == [(0, 4)] and bb == [(0, 4)])

out = {"counts": dict(n), "violations": {k: v for k, v in viol.items() if v}, "star_shapes (campaign, fixtures excluded)": shapes_before,
       "fixtures": fx}
print(json.dumps(out, indent=1, sort_keys=True))
