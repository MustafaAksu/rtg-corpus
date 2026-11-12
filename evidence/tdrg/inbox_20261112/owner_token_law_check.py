#!/usr/bin/env python3
"""TDR-G owner-session check (12 Nov 2026): AZ token-alphabet offer (pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md)
on the pinned engine itself, all six policies, with the adopted TDRG-DEF-ORIENT.

Drives the engine's own step_universe (no re-implementation); only orient_path is set to the v2.12.14 reference
implementation. Per tick it checks:
  P1   C_{t+1} = C_t (+) {-x_a : a born this tick}   (token multiset, x_a = centre's pre-event token)
  P1a  every token lies in S_0 = A_0 u (-A_0)
  P1.1 D_{t+1} = D_t (+) {|x_a + y|_c : y in C_t} (+) {|x_a - x_b|_c : a<b}   (unlabelled |d_ij|_c multiset)
  P1.2 birth-free tick: D_{t+1} = D_t
  P2   parent-child phase: while centre and child keep tokens (-x, x), theta_E - theta_A = N/2 + 2 j x (j ticks after birth)
and records the shape of every component the engine classifies as a single star (exactly one node of degree >= 3)
or a multistar, to compare with the TDRG-DEF-STAR text (K_{1,3}).
usage: python3 -I owner_token_law_check.py ENGINE_V18.py ORIENT_REF.py [RUNS_PER_CELL]
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

shapes = Counter()
orig_classify = eng.classify_component
def classify_spy(comp, adj):
    ctype, centers = orig_classify(comp, adj)
    s = set(comp)
    if ctype.startswith("star_k1c_"):
        c = centers[0]; deg = len(adj[c] & s)
        pure = len(comp) == deg + 1
        e = sum(len(adj[v] & s) for v in comp) // 2
        shapes["star pure K_1,%s" % ("3" if deg == 3 else ">=4") if pure else
               ("star with extra nodes, tree" if e == len(comp) - 1 else "star with extra nodes, contains a cycle")] += 1
    elif ctype.startswith("multistar_"):
        shapes["multistar"] += 1
    return ctype, centers
eng.classify_component = classify_spy

def cdist(a, b, N):
    d = (a - b) % N; return min(d, N - d)

def D_of(C, N):
    toks = sorted(C.elements())
    return Counter(cdist(toks[i], toks[j], N) for i in range(len(toks)) for j in range(i + 1, len(toks)))

viol = Counter(); ticks = births = birth_ticks = bf_ticks = 0; p2_checked = 0
rng = random.Random(20261112)
for pol in POL:
    for N, k in ((24, 1), (30, 2), (60, 4), (120, 8)):
        for r in range(RUNS):
            u = eng.Universe(N=N, k=k, theta={i: rng.randrange(N) for i in range(4)},
                             delta={i: rng.randrange(N) for i in range(4)})
            S0 = set(u.delta.values()) | {(-x) % N for x in u.delta.values()}
            pc = {}   # child -> (parent, x, j, theta diff at birth)
            for t in range(400):
                if len(u.theta) >= 70: break
                pre_ids = set(u.theta); C = Counter(u.delta.values()); dpre = dict(u.delta)
                eng.step_universe(u, multistar_policy=pol); ticks += 1
                new = [i for i in u.theta if i not in pre_ids]
                xs = [u.delta[i] for i in new]          # newborn token = centre's pre-event token
                births += len(new)
                exp = C + Counter((-x) % N for x in xs)
                if Counter(u.delta.values()) != exp: viol["P1"] += 1
                if not set(u.delta.values()) <= S0: viol["P1a"] += 1
                if len(u.theta) <= 70:
                    Dexp = D_of(C, N)
                    for a, x in enumerate(xs):
                        for y in C.elements(): Dexp[cdist((-x) % N, y, N)] += 1
                        for b in range(a + 1, len(xs)): Dexp[cdist(x, xs[b], N)] += 1
                    if D_of(Counter(u.delta.values()), N) != Dexp: viol["P1.1"] += 1
                if not new:
                    bf_ticks += 1
                else:
                    birth_ticks += 1
                # parent-child phase law
                for ch in new:
                    par = [c for c in pre_ids if dpre[c] == u.delta[ch] and u.delta[c] == (-dpre[c]) % N
                           and (u.theta[c] + N // 2) % N == u.theta[ch]]
                    if par: pc[ch] = (par[0], u.delta[ch], 0)
                for ch, (pa, x, j) in list(pc.items()):
                    if ch in new: continue
                    if u.delta.get(ch) == x and u.delta.get(pa) == (-x) % N:
                        j += 1; pc[ch] = (pa, x, j); p2_checked += 1
                        if (u.theta[ch] - u.theta[pa]) % N != (N // 2 + 2 * j * x) % N: viol["P2"] += 1
                    else:
                        del pc[ch]
out = {"ticks": ticks, "births": births, "birth_ticks": birth_ticks, "birth_free_ticks": bf_ticks,
       "p2_phase_checks": p2_checked, "violations": dict(viol), "star_shapes": dict(shapes)}
print(json.dumps(out, indent=1, sort_keys=True))
