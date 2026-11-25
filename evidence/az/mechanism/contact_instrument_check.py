#!/usr/bin/env python3
"""AZ token resonance, mechanism design - check of the first-contact instrument (PR #281 §4). [SESSION]

    python3 -I evidence/az/mechanism/contact_instrument_check.py

Development check only: synthetic initial states from this script's own fixed seed, no registered
tag, no registered data; the engine is stepped only until the first contact and the first counted
event, so no growth outcome (M, births, t100) is produced or printed.

1. Closed form vs direct modular scan: tau_contact from the per-pair congruences (gcd and modular
   inverse; b = 0 handled) against a scan of t = 1..N of the defect predicate, on 4-node states and
   on targeted cases (zero advance, b = 0 in band / out of band, no solution, t = N, edges at t = 0,
   simultaneous first contacts).
2. Closed form vs the pinned engine (P1 orientation, policy bound_symmetric): the first processed
   tick whose post-advance, pre-interaction defect graph has an edge, observed with step_universe.
3. tau_contact vs the runner's clock fe (first nonzero of single_edge_swaps, path_interactions,
   births, multistar_seen, path_ties_seen), counted, with the component type at tau_contact.
Exit code 0 iff (1) and (2) agree in every case.
"""
import hashlib, math, os, random, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "evidence", "az", "scripts"))
import az_tokres_run as R  # noqa: E402  (hash-checked loader of the pinned engine)

CELLS = ((120, 8), (122, 8), (240, 16), (242, 16), (480, 32))
SEED = 20261116


def in_band(x, N, k):
    y = x % N
    y = y - N if y > N // 2 else y
    return abs(y) <= k


def pair_first(a, b, N, k):
    """first t >= 1 with a + t b = e (mod N) for some |e| <= k; None if never."""
    b %= N
    if b == 0:
        return 1 if in_band(a, N, k) else None
    g = math.gcd(N, b)
    L = N // g
    inv = pow((b // g) % L, -1, L) if L > 1 else 0
    best = None
    for e in range(-k, k + 1):
        r = (e - a) % N
        if r % g:
            continue
        t = ((r // g) * inv) % L if L > 1 else 0
        t = t if t else L
        best = t if best is None or t < best else best
    return best


def tau_closed(theta, delta, N, k):
    best = None
    n = len(theta)
    for i in range(n):
        for j in range(i + 1, n):
            t = pair_first(theta[i] - theta[j] - N // 2, delta[i] - delta[j], N, k)
            if t is not None and (best is None or t < best):
                best = t
    return best


def tau_scan(theta, delta, N, k):
    for t in range(1, N + 1):
        th = [(x + t * d) % N for x, d in zip(theta, delta)]
        if any(in_band(th[i] - th[j] - N // 2, N, k) for i in range(4) for j in range(i + 1, 4)):
            return t
    return None


def engine_first(eng, theta, delta, N, k):
    """step the pinned engine; return (tau_contact_engine, fe, component types at the first contact)."""
    u = eng.Universe(N=N, k=k, theta={i: t % N for i, t in enumerate(theta)}, delta={i: d % N for i, d in enumerate(delta)})
    tc = fe = None
    types = None
    while u.steps < N + 2 and fe is None:
        pre_t, pre_d = dict(u.theta), dict(u.delta)
        if tc is None:
            th = {x: (pre_t[x] + pre_d[x]) % N for x in pre_t}
            nodes = list(th)
            edges = eng.graph_edges_for(nodes, th, N, k)
            if edges:
                adj = eng.build_adj(nodes, edges)
                types = tuple(sorted(eng.classify_component(c, adj)[0] for c in eng.connected_components(nodes, adj) if len(c) > 1))
        eng.step_universe(u, multistar_policy="bound_symmetric")
        if tc is None and u.edge_history[-1] > 0:
            tc = u.steps
            if not types:
                raise SystemExit("engine reported an edge that the replicated pre-interaction graph does not show")
        if u.single_edge_swaps or u.path_interactions or u.births or u.multistar_seen or u.path_ties_seen:
            fe = u.steps
        if tc is None and u.steps >= N:
            break
    return tc, fe, types


def main():
    eng, info = R.load_engine(os.path.join(ROOT, "upload/tdrg-records/genesis_mode_b_mc.py"),
                              os.path.join(ROOT, "evidence/tdrg/scripts/tdrg_orient_v2_12_14.py"), "P1")
    print("AZ mechanism design - first-contact instrument check ([SESSION], development)")
    print("script sha256 %s" % hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest())
    print("engine %s  orientation %s  profile %s  policy bound_symmetric  seed %d" % (info["engine_sha256"][:16], info["orient_sha256"][:16], info["profile"], SEED))
    rng = random.Random(SEED)
    ok = True
    # targeted cases
    tgt = 0
    for N, k in CELLS:
        cases = []
        h = N // 2
        cases.append(([0, 0, 0, 0], [0, 0, 0, 0]))                       # all phases equal, b = 0, out of band: never
        cases.append(([0, h, 3, 7], [5, 5, 9, 11]))                      # pair (0,1) in band at every tick (b = 0)
        cases.append(([0, h + k, 1, 2], [0, 0, 0, 0]))                   # edge at t = 0 and every tick, zero advance
        cases.append(([0, h, 1, 2], [1, 0, 1, 1]))                       # edge at t = 0; moves out and back
        cases.append(([0, 1, 2, 3], [0, h, 0, h]))                       # resonant advances 0 and N/2
        cases.append(([0, h - k - 1, 5, 9], [0, N - 1, 0, 0]))           # first time N-ish with unit step
        cases.append(([0, h + 2 * k + 1, 0, h + 2 * k + 1], [0, 1, 0, 1]))  # simultaneous first contacts, two pairs
        for th, de in cases:
            a, b = tau_closed(th, de, N, k), tau_scan(th, de, N, k)
            ok &= a == b
            tgt += 1
    print("targeted cases: %d, closed form = scan in all: %s" % (tgt, ok))
    # random states, plus slot replacements by resonant and detuned values as in the registered arms
    per_cell = 600
    agree_scan = agree_eng = n_states = 0
    fe_eq = fe_gt = fe_none = never = 0
    lag = Counter()
    first_types = Counter()
    for N, k in CELLS:
        for _ in range(per_cell):
            th = [rng.randrange(N) for _ in range(4)]
            de = [rng.randrange(N) for _ in range(4)]
            variants = [de]
            s = rng.randrange(4)
            for v in ((0, N // 2) + ((N // 4, 3 * N // 4) if N % 4 == 0 else ())):
                for w in (v, (v + 1) % N, (v - 1) % N):
                    d2 = list(de); d2[s] = w; variants.append(d2)
            for d in variants:
                n_states += 1
                a = tau_closed(th, d, N, k)
                b = tau_scan(th, d, N, k)
                agree_scan += a == b
                ok &= a == b
                if d is de or rng.random() < 0.25:            # engine on the native state and a sample of variants
                    tc, fe, types = engine_first(eng, th, d, N, k)
                    agree_eng += 1 if tc == a else 0
                    if tc != a:
                        ok = False
                        print("MISMATCH engine N=%d k=%d theta=%s delta=%s closed=%s engine=%s" % (N, k, th, d, a, tc))
                    if tc is None:
                        never += 1
                        continue
                    first_types[types] += 1
                    if fe is None:
                        fe_none += 1
                    elif fe == tc:
                        fe_eq += 1
                    else:
                        fe_gt += 1
                        lag[min(fe - tc, 10)] += 1
    print("random states: %d cells x %d native states, each with its slot variants; closed form = scan: %d of %d" % (len(CELLS), per_cell, agree_scan, n_states))
    print("closed form = pinned engine (first post-advance, pre-interaction edge): %d agreements" % agree_eng)
    print("engine-checked states with no contact in ticks 1..N: %d" % never)
    print("runner clock fe vs tau_contact: fe = tau_contact %d; fe > tau_contact %d; no counted event within N+2 ticks %d" % (fe_eq, fe_gt, fe_none))
    print("  lag fe - tau_contact (10 = 10 or more): %s" % dict(sorted(lag.items())))
    print("component types at tau_contact (most common 8): %s" % first_types.most_common(8))
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
