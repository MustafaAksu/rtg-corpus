#!/usr/bin/env python3
"""TDR-G owner-session check (27 Oct 2026): node-relabelling equivariance of the pinned engine step.

Independent of the atlas script: it does not re-implement the dynamics. It loads the pinned engine
genesis_mode_b_mc_v18.py (sha256 9d787b43...) and calls its own step_universe, replacing only orient_path by
one of three variants:
  v18     the pinned rule (negative control: must FAIL on the stratum S=0, E=+N/2)
  tie_b   option (b): balanced tie extended to 2E = 0 mod N (S=0 and E in {0, N/2} -> tie)
  G_a     option (a): on S=0, E=N/2 for P_3 orient by sign(G), G = sc(d_v1-d_c) - sc(d_v3-d_c); n>3 falls back to tie
Test: step(pi s) == pi step(s) for the generators (01),(12) of S_3 (three nodes, exhaustive over the gauge-reduced
states theta_0 = delta_0 = 0) and for random permutations of S_4 (four nodes, random sample). New-born nodes are
compared as a multiset of (theta, delta). A global-phase-shift control (theta -> theta + c) is run on the same states.
usage: python3 -I owner_relabel_equivariance_check.py ENGINE.py [--n4 SAMPLES]
"""
import importlib.util, sys, random, itertools, json
from collections import Counter

eng_path = sys.argv[1]
spec = importlib.util.spec_from_file_location("eng", eng_path)
eng = importlib.util.module_from_spec(spec); sys.modules["eng"] = eng; spec.loader.exec_module(eng)
ORIG = eng.orient_path
sc = eng.signed_centered

def orient_tie_b(path, theta, delta, N, u):
    if len(path) == 2: return path
    s = sum(eng.signed_defect_error(theta[path[i]], theta[path[i+1]], N) for i in range(len(path)-1))
    if s > 0: return path
    if s < 0: return list(reversed(path))
    u.orientation_ties += 1
    e = sc(delta[path[-1]] - delta[path[0]], N)
    if 0 < e < N // 2: return path
    if e < 0: return list(reversed(path))
    u.path_ties_seen += 1          # e == 0 or e == N/2: no reversal-odd invariant -> balanced tie
    return None

def orient_G_a(path, theta, delta, N, u):
    if len(path) == 2: return path
    s = sum(eng.signed_defect_error(theta[path[i]], theta[path[i+1]], N) for i in range(len(path)-1))
    if s > 0: return path
    if s < 0: return list(reversed(path))
    u.orientation_ties += 1
    e = sc(delta[path[-1]] - delta[path[0]], N)
    if 0 < e < N // 2: return path
    if e < 0: return list(reversed(path))
    if e == N // 2 and len(path) == 3:
        c = path[1]
        g = sc(delta[path[0]] - delta[c], N) - sc(delta[path[2]] - delta[c], N)
        assert g != 0
        return path if g > 0 else list(reversed(path))
    u.path_ties_seen += 1
    return None

VARIANTS = {"v18": ORIG, "tie_b": orient_tie_b, "G_a": orient_G_a}

def run(theta, delta, N, k, policy):
    u = eng.Universe(N=N, k=k, theta=dict(theta), delta=dict(delta))
    eng.step_universe(u, multistar_policy=policy)
    return u

def canon(u, perm, n0):
    """Map old node i -> perm[i]; new nodes as a sorted multiset."""
    old = tuple(sorted((perm[i], u.theta[i], u.delta[i]) for i in range(n0)))
    new = tuple(sorted((u.theta[i], u.delta[i]) for i in u.theta if i >= n0))
    return old, new

def equiv(theta, delta, N, k, policy, perm):
    n0 = len(theta)
    u0 = run(theta, delta, N, k, policy)
    th = {perm[i]: theta[i] for i in range(n0)}; dl = {perm[i]: delta[i] for i in range(n0)}
    u1 = run(th, dl, N, k, policy)
    a = canon(u0, perm, n0)
    b = canon(u1, list(range(n0)), n0)
    return a == b

def phase_equiv(theta, delta, N, k, policy, c):
    u0 = run(theta, delta, N, k, policy)
    u1 = run({i: (t + c) % N for i, t in theta.items()}, delta, N, k, policy)
    a = canon(u0, list(range(len(theta))), len(theta)); a = (tuple((i, (t + c) % N, d) for i, t, d in a[0]), tuple(sorted(((t + c) % N, d) for t, d in a[1])))
    return a == canon(u1, list(range(len(theta))), len(theta))

def main():
    N = 24
    out = {}
    gens = [(1, 0, 2), (0, 2, 1)]
    for name, fn in VARIANTS.items():
        eng.orient_path = fn
        for k in (1, 3):
            fails = Counter(); stratum = 0; total = 0; phase_fail = 0
            for t1, t2, d1, d2 in itertools.product(range(N), repeat=4):
                theta = {0: 0, 1: t1, 2: t2}; delta = {0: 0, 1: d1, 2: d2}
                total += 1
                for g in gens:
                    if not equiv(theta, delta, N, k, "bound_symmetric", g): fails[g] += 1
                if total % 97 == 0 and not phase_equiv(theta, delta, N, k, "bound_symmetric", 5): phase_fail += 1
            out[f"n3_{name}_k{k}"] = dict(states=total, fail_gen01=fails[gens[0]], fail_gen12=fails[gens[1]], phase_shift_fail_sampled=phase_fail)
            print(f"[n3] {name:6s} k={k}: states {total}, equivariance failures (01): {fails[gens[0]]}, (12): {fails[gens[1]]}, phase-shift failures (1/97 sample): {phase_fail}", flush=True)
    if "--n4" in sys.argv:
        S = int(sys.argv[sys.argv.index("--n4") + 1]); rng = random.Random(20261027)
        perms = list(itertools.permutations(range(4)))
        for name, fn in VARIANTS.items():
            eng.orient_path = fn
            for policy in ("bound_symmetric", "largest_center"):
                fails = 0; paths = 0
                rng.seed(20261027)
                for _ in range(S):
                    k = rng.choice((1, 2, 3))
                    theta = {i: rng.randrange(N) for i in range(4)}; delta = {i: rng.randrange(N) for i in range(4)}
                    if not equiv(theta, delta, N, k, policy, rng.choice(perms)): fails += 1
                out[f"n4_{name}_{policy}"] = dict(samples=S, fail=fails)
                print(f"[n4] {name:6s} {policy:16s}: {S} random (state, k, perm) samples, equivariance failures: {fails}", flush=True)
    json.dump(out, open("owner_relabel_equivariance_check.json", "w"), indent=1, sort_keys=True)

main()
