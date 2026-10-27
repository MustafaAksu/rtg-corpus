#!/usr/bin/env python3
"""Atlas check (TDR-G advisory, 26 Oct 2026): relabelling covariance of the TDR-G path-orientation rule at S=0, |E|=N/2.

Independent contribution (Methodology v1.4 §12.3), not a rerun of any owner campaign. It re-implements the three-node
TDR-G step from the owner definitions (TDRG v2.12.13 §6.1, §6.3: CONV-TICK, antipodal swap, CONV-P3CYC successor shift,
path orientation rule; signed_centered / signed_defect_error as in genesis_mode_b_mc_v18.py lines 38–55, which the owner
text uses but does not define) and the DISC-2 verdict logic of NUMGEN's audit script
upload/numgen-records/disc2_p2_antipodal_exposure_audit_v1.py (sha256 89a1466f…). It reads only the ratified witness
report upload/numgen-records/disc2_witness_report.json (sha256 ccc84570…); it changes no rule and no verdict.

Claims checked (N=24, three nodes, k in {0,1,2,3}):
  C1  exhaustive over all gauge-reduced three-node states whose defect graph is a two-edge path: S is antisymmetric under
      path reversal and E=signed_centered(delta_end-delta_start) is antisymmetric except exactly when
      delta_end-delta_start ≡ N/2, where E=+N/2 under both listings (the v18 rule then orients by node-ID listing).
  C2  on that degenerate set the pair of centre-relative advances is never reversal-symmetric: G := sc(delta_v1-delta_c)
      - sc(delta_v3-delta_c) is antisymmetric under reversal and never 0 there (because delta_v3-delta_v1 ≡ N/2 ≠ 0).
      Hence a relabelling-covariant orientation exists on the whole degenerate set for P_3.
  C3  rerun of the 136 ratified DISC-2 witnesses under four policies at the degenerate set — v18 (ID listing), reverse,
      inert (tie), covariant-G — counting verdict/class changes and the admitted label set.
usage: python3 -I atlas_tdrg_orientation_covariance_check.py PATH/disc2_witness_report.json
"""
import json, sys, itertools
from math import gcd
from collections import defaultdict
N = 24
def sc(x, n=N):
    y = x % n
    return y - n if y > n // 2 else y
def sde(ta, tb): return sc((ta - tb) % N - N // 2)
def shell(D): return abs(sc(D - N // 2))
PAIR = ((0, 1), (0, 2), (1, 2))

def orient(path, th, old, policy):
    """path = [end, centre, end] in listing order. Returns (oriented path or None for tie, degenerate flag)."""
    S = sde(th[path[0]], th[path[1]]) + sde(th[path[1]], th[path[2]])
    if S > 0: return path, False
    if S < 0: return path[::-1], False
    E = sc(old[path[2]] - old[path[0]])
    if abs(E) == N // 2:
        if policy == 'v18': return path, True
        if policy == 'reverse': return path[::-1], True
        if policy == 'inert': return None, True
        if policy == 'covariant-G':
            G = sc(old[path[0]] - old[path[1]]) - sc(old[path[2]] - old[path[1]])
            assert G != 0
            return (path if G > 0 else path[::-1]), True
        raise ValueError(policy)
    if E > 0: return path, False
    if E < 0: return path[::-1], False
    return None, False

def make_step(policy):
    def step(state, k):
        th, dl = state
        th = tuple((th[i] + dl[i]) % N for i in range(3))
        sh = {PAIR[a]: shell((th[PAIR[a][0]] - th[PAIR[a][1]]) % N) for a in range(3)}
        E = [p for p, m in sh.items() if m <= k]; old = dl
        if len(E) == 1:
            i, j = E[0]; d = list(dl); d[i], d[j] = old[j], old[i]; return (th, tuple(d)), 'S', False
        if len(E) == 2:
            nodes = [x for e in E for x in e]
            c = [v for v in set(nodes) if nodes.count(v) == 2][0]
            ends = sorted(v for v in set(nodes) if v != c); path = [ends[0], c, ends[1]]   # v18 listing: sorted node IDs
            path, flag = orient(path, th, old, policy)
            if path is None: return (th, dl), 'T', flag
            d = list(dl)
            for i, v in enumerate(path): d[v] = old[path[(i + 1) % 3]]
            return (th, tuple(d)), 'P', flag
        return (th, dl), '.', False
    return step

def canon(s):
    th, dl = s
    return ((th[0] - th[1]) % N, (th[0] - th[2]) % N, (dl[0] - dl[1]) % N, (dl[0] - dl[2]) % N)
def lift(r):
    a, b, c, d = r; return ((0, (0 - a) % N, (0 - b) % N), (0, (0 - c) % N, (0 - d) % N))
def run(step, r, k):
    s = lift(r); seen = {}; ev = []; fl = False; t = 0
    while t < 200000:
        key = canon(s)
        if key in seen: break
        seen[key] = t; s, e, f = step(s, k); ev.append(e); fl |= f; t += 1
    pre = seen[canon(s)]; c = ev[pre:t]; a = c.count('S'); b = c.count('P')
    return (None if (a == 0 or b == 0) else (a // gcd(a, b), b // gcd(a, b))), fl
def verdict(step, r):
    out = {}; touched = False
    for k in (0, 1, 2, 3):
        out[k], f = run(step, r, k); touched |= f
    r1 = out[1]
    if r1 is None: v = 'NO_BASE_DUAL'
    elif out[2] is None: v = 'STABILITY_UNAVAILABLE'
    elif out[2] != r1: v = 'UNSTABLE'
    elif out[3] is not None and out[3] != r1: v = 'PASS_INT'
    elif out[0] is not None and out[0] != r1: v = 'PASS_BDY_ONLY'
    else: v = 'STABLE_NO_CONTINGENCY'
    return v, r1, touched

def main():
    out = {}
    # ---- C1, C2: exhaustive over gauge-reduced three-node states (theta_0 = 0, delta_0 = 0) ----
    n_path = n_degen = 0; c1 = c2 = True
    for t1, t2, d1, d2 in itertools.product(range(N), repeat=4):
        th = (0, t1, t2); dl = (0, d1, d2)
        for k in (0, 1, 2, 3):
            sh = {PAIR[a]: shell((th[PAIR[a][0]] - th[PAIR[a][1]]) % N) for a in range(3)}
            E = [p for p, m in sh.items() if m <= k]
            if len(E) != 2: continue
            n_path += 1
            nodes = [x for e in E for x in e]; c = [v for v in set(nodes) if nodes.count(v) == 2][0]
            ends = [v for v in set(nodes) if v != c]; p = [ends[0], c, ends[1]]; q = p[::-1]
            S_p = sde(th[p[0]], th[p[1]]) + sde(th[p[1]], th[p[2]]); S_q = sde(th[q[0]], th[q[1]]) + sde(th[q[1]], th[q[2]])
            E_p = sc(dl[p[2]] - dl[p[0]]); E_q = sc(dl[q[2]] - dl[q[0]])
            degen = (S_p == 0 and abs(E_p) == N // 2)
            c1 &= (S_p == -S_q) and (S_p != 0 or (E_p == -E_q) or degen) and (not degen or (E_p == E_q == N // 2))   # E is consulted only when S=0
            if degen:
                n_degen += 1
                G_p = sc(dl[p[0]] - dl[p[1]]) - sc(dl[p[2]] - dl[p[1]]); G_q = sc(dl[q[0]] - dl[q[1]]) - sc(dl[q[2]] - dl[q[1]])
                c2 &= (G_p != 0) and (G_p == -G_q)
    out['C1_S_antisymmetric_E_antisymmetric_except_degenerate'] = c1
    out['C2_covariant_G_nonzero_and_antisymmetric_on_degenerate_set'] = c2
    out['path_states_checked'] = n_path; out['degenerate_path_states'] = n_degen
    print(f"[{'PASS' if c1 else 'FAIL'}] C1 S antisymmetric under reversal; E antisymmetric except exactly on the degenerate set (E=+N/2 under both listings) — {n_path} (state,k) path cases, {n_degen} degenerate")
    print(f"[{'PASS' if c2 else 'FAIL'}] C2 on the degenerate set G=sc(δ_v1−δ_c)−sc(δ_v3−δ_c) is never 0 and flips sign under reversal (covariant orientation exists everywhere there for P_3)")
    # ---- C3: witness rerun ----
    rep = json.load(open(sys.argv[1]))
    W = [s for s, v in rep['per_seed'].items() if v['verdict'].startswith('PASS')]
    seeds = {s: tuple(int(z) for z in s.split('_')[1:]) for s in W}
    res = {pol: {s: verdict(make_step(pol), seeds[s]) for s in W} for pol in ('v18', 'reverse', 'inert', 'covariant-G')}
    base = res['v18']; exposed = [s for s in W if base[s][2]]
    out['ratified_witnesses'] = len(W); out['exposed_witnesses'] = len(exposed)
    print(f"[INFO] C3 ratified witnesses {len(W)}; exposed to the degenerate set under v18: {len(exposed)}")
    for pol in ('reverse', 'inert', 'covariant-G'):
        ch = [s for s in W if res[pol][s][:2] != base[s][:2]]
        labels = {res[pol][s][1] for s in W if res[pol][s][0].startswith('PASS')}
        base_labels = {base[s][1] for s in W if base[s][0].startswith('PASS')}
        out[f'changes_{pol}'] = len(ch); out[f'labels_identical_{pol}'] = (labels == base_labels)
        print(f"[INFO] C3 policy {pol:12s}: verdict/class changes {len(ch):3d} of {len(W)}; admitted label set identical to v18: {labels == base_labels}")
    out['base_label_set'] = sorted(f'{a}:{b}' for a, b in {base[s][1] for s in W if base[s][0].startswith('PASS')})
    unexp = defaultdict(int)
    for s in W:
        if not base[s][2]: unexp[base[s][1]] += 1
    out['labels_without_unexposed_witness'] = [f'{a}:{b}' for a, b in {base[s][1] for s in W} if unexp[(a, b)] == 0]
    print(f"[INFO] labels lacking an unexposed witness: {out['labels_without_unexposed_witness']}")
    # ---- C4: census of the whole gauge-reduced three-node state space at k=1 (N=24): how much of the TDR-G three-node
    #      universe (the BIND3 certification universe, §6.12) passes through the degenerate set, and how many eventual
    #      cycles differ between the v18 listing rule and a covariant rule. Memoised orbit following; no horizon cut.
    if '--census' in sys.argv:
        for pol in ('v18', 'covariant-G', 'inert'):
            step = make_step(pol); cyc = {}; touched_states = 0; n_cycles = 0; cyc_touch = 0
            cycle_of = {}
            for t1, t2, d1, d2 in itertools.product(range(N), repeat=4):
                s0 = ((0, t1, t2), (0, d1, d2)); key0 = canon(s0)
                if key0 in cycle_of: continue
                path = []; seen = {}; s = s0; flags = []
                while True:
                    key = canon(s)
                    if key in cycle_of: cid, tflag = cycle_of[key]; break
                    if key in seen:
                        start = seen[key]; cid = len(cyc); members = path[start:]; tflag = any(flags[start:])
                        cyc[cid] = (tuple(sorted(members)), tflag); n_cycles += 1; cyc_touch += tflag
                        for m in path[start:]: cycle_of[m] = (cid, tflag)
                        break
                    seen[key] = len(path); path.append(key); s, e, f = step(s, 1); flags.append(f)
                for m in path:
                    if m not in cycle_of: cycle_of[m] = (cid, tflag)
            states = len(cycle_of); st_touch = sum(1 for v in cycle_of.values() if v[1])
            out[f'census_k1_{pol}'] = dict(states=states, cycles=n_cycles, cycles_with_degenerate_event=cyc_touch, states_whose_cycle_has_degenerate_event=st_touch,
                                           cycle_member_multiset_sha=__import__('hashlib').sha256(json.dumps(sorted(v[0] for v in cyc.values())).encode()).hexdigest()[:16])
            print(f"[INFO] C4 census k=1 {pol:12s}: {states} gauge-reduced states, {n_cycles} eventual cycles, {cyc_touch} cycles contain a degenerate event, {st_touch} states flow into such a cycle")
    json.dump(out, open('atlas_tdrg_orientation_covariance_check.json', 'w'), indent=1)
    print('RESULT:', 'PASS' if (c1 and c2) else 'FAIL')
    sys.exit(0 if (c1 and c2) else 1)

if __name__ == '__main__':
    main()
