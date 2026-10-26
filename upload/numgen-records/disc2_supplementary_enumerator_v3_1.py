#!/usr/bin/env python3
# =============================================================================
# C7B-DISC-2 SUPPLEMENTARY-DOMAIN ENUMERATOR  v3.1
# =============================================================================
# Governed by NG_C7B_DISC2_PREREG_v1.md
#   (sha256 db87b45565f6c5e59ef4797abde8514d89586c1b56bfe303d29ec6fb33919da9)
#
# THIS FILE IS INERT ON IMPORT. All execution is under __main__. Hashing,
# syntax checking and static inspection cannot cause domain inspection.
#
# Domain            registered supplementary one-pass family, |d|_c = 3,4,5,
#                   six rows x 1728 = 10368 seeds. The 32832-IC extrapolated
#                   extension beyond |d|_c = 5 is EXCLUDED.
# Panel             generated ONCE, identical frozen seed coordinates reused at
#                   every k. No k-specific regeneration.
# Dynamics          canonical v18 conventions, bound_symmetric. The fast core is
#                   used ONLY after an exhaustive one-step equivalence check
#                   against genesis_mode_b_mc_v18.py over all 24^4 reduced
#                   states for every k in {0,1,2,3}. Any mismatch ABORTS.
#
# v1 -> v2 [COR], three fixes:
#   (1) LOAD-BEARING. The v1 gateway compared only the next reduced STATE.
#       State equality does NOT imply event-label equality: a SWAP or P3 acting
#       on equal delta-tokens can increment a v18 counter while leaving the
#       reduced state fixed. Since n_swap / n_P3 are the quantities from which
#       Q^dyn is decided, the gateway now certifies the TRIPLE
#           (next reduced state, delta n_swap, delta n_P3)
#       exhaustively. DISC-1 survived a state-only S1 check only because S2
#       later recounted admitted witnesses through v18's own counters; DISC-2
#       certifies counter semantics BEFORE the untouched domain is inspected.
#   (2) v18 pinned by SHA-256 and loaded from an explicit path rather than
#       ordinary module resolution. (v2 still used the alias filename v18.py.)
#   (3) The panel assertion now decides all SIX SIGNED registered rows. The v1
#       assertion collapsed signs, so a bug giving 3456 at +3 and 0 at -3 would
#       have passed.
#
# v2 -> v3 [COR], provenance-only:
#   The pinned owner source is now required under its CANONICAL filename
#   genesis_mode_b_mc_v18.py rather than the alias v18.py. Hash, filename, run
#   manifest and governance record therefore identify the same artifact.
#   No dynamics, domain, admission, counting or reporting logic changed.
#
# v3 -> v3.1 [COR], execution defect (EXECUTABLE change, not comment-only):
#   load_pinned_v18 called exec_module without first registering the module in
#   sys.modules. The owner source defines @dataclass classes, and
#   dataclasses._is_type resolves sys.modules[cls.__module__]; unregistered,
#   that returns None and the decorator raises
#     AttributeError: 'NoneType' object has no attribute '__dict__'
#   before any domain evaluation. Fixed by registering spec.name first. The
#   SHA-256 pin, canonical filename, gateway, panel, counting, blindness and
#   reporting logic are all unchanged; only module loading is repaired.
# Cycle detection   exact, in the canonical reduced 4-coordinate state; cycle-only
#                   n_swap / n_P3, plus preperiod and period.
# dual_active       (n_swap > 0 and n_P3 > 0), exactly as DISC-1.
# Outputs           (1) DISC-1 schema UNCHANGED -> consumed by the sealed
#                       disc1_analysis_harness_v1.py (57a15421...)
#                   (2) companion transport artifact carrying raw seed
#                       coordinates, blindness flags and cycle provenance.
#                       The harness never reads file (2).
# Blindness         realization-level: comparison k is trajectory-blind iff
#                   F_k^t(x) = F_1^t(x) for all t, decided by evolving the PAIR
#                   (F_1^t(x), F_k^t(x)) from the SAME original seed until the
#                   pair-state repeats. Eventual-cycle equality is NOT used.
#                   Reporting only; never an admission fence.
# Excluded          bond-transfer classifier; any post-hoc mechanism feature;
#                   prevalence thresholds; early stopping; sampling; dropping
#                   non-dual rows.
# Abort policy      ANY cycle-detection anomaly (step cap reached on a single
#                   or paired orbit) aborts the entire campaign. No partial
#                   emission, no timeout-classified orbits. This sector is
#                   finite; truncation has no legitimate reading.
# =============================================================================

import os, sys, json, itertools, hashlib, importlib.util

N = 24
STEP_CAP = 200_000            # generous; reaching it is an anomaly, not a result
EXPECTED_SEEDS = 10368
EXPECTED_RECORDS = 41472      # 10368 x 4
K_SET = (0, 1, 2, 3)
K_BASE = 1
V18_SHA256 = "9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e"
OWNER_FILENAME = "genesis_mode_b_mc_v18.py"   # canonical name; no alias
EXPECTED_PER_D = {-5: 1728, -4: 1728, -3: 1728, 3: 1728, 4: 1728, 5: 1728}


# ---------------------------------------------------------------- primitives
def sc(x, n=N):
    """v18 signed_centered: representative in (-n/2, n/2]."""
    y = x % n
    return y - n if y > n // 2 else y


def shell(D):
    return abs(sc(D - N // 2))


def sde(ta, tb):
    return sc((ta - tb) % N - N // 2)


PAIR = ((0, 1), (0, 2), (1, 2))


def step(state, k):
    """One CONV-TICK. Returns (new_state, event) with event in {S,P,T,K,.}."""
    th, dl = state
    th = tuple((th[i] + dl[i]) % N for i in range(3))
    sh = tuple(shell((th[a] - th[b]) % N) for a, b in PAIR)
    E = [PAIR[i] for i in range(3) if sh[i] <= k]
    old = dl
    if len(E) == 1:
        i, j = E[0]
        d = list(dl); d[i], d[j] = old[j], old[i]
        return (th, tuple(d)), 'S'
    if len(E) == 2:
        nodes = [x for e in E for x in e]
        c = [v for v in set(nodes) if nodes.count(v) == 2][0]
        ends = sorted(v for v in set(nodes) if v != c)
        path = [ends[0], c, ends[1]]
        S = sde(th[path[0]], th[path[1]]) + sde(th[path[1]], th[path[2]])
        if S < 0:
            path = path[::-1]
        elif S == 0:
            Ee = sc(old[path[2]] - old[path[0]])
            if Ee < 0:
                path = path[::-1]
            elif Ee == 0:
                return (th, dl), 'T'          # balanced tie inert (bound_symmetric)
        d = list(dl)
        for i, v in enumerate(path):
            d[v] = old[path[(i + 1) % 3]]
        return (th, tuple(d)), 'P'
    if len(E) == 3:
        return (th, dl), 'K'
    return (th, dl), '.'


def canon(s):
    th, dl = s
    return ((th[0] - th[1]) % N, (th[0] - th[2]) % N,
            (dl[0] - dl[1]) % N, (dl[0] - dl[2]) % N)


def lift(r):
    a, b, c, d = r
    return ((0, (0 - a) % N, (0 - b) % N), (0, (0 - c) % N, (0 - d) % N))


class Anomaly(Exception):
    pass


# ------------------------------------------------- owner-equivalence gateway
def load_pinned_v18(path):
    """Load the owner source from an EXPLICIT path after verifying its SHA-256.
    Module resolution is not used: 'verified against v18' must mean this file."""
    if not os.path.exists(path):
        raise SystemExit(f"ABORT: owner source not found at {path}")
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    if h != V18_SHA256:
        raise SystemExit(f"ABORT: v18 hash {h} != pinned {V18_SHA256}")
    spec = importlib.util.spec_from_file_location("pinned_v18", path)
    mod = importlib.util.module_from_spec(spec)
    # MUST register before exec_module: the owner source defines @dataclass
    # classes, and dataclasses._is_type resolves sys.modules[cls.__module__].
    # Without this the decorator raises AttributeError on NoneType.
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    print(f"    v18 pinned and verified: {h}")
    return mod


def verify_against_v18(v18):
    """Exhaustive one-step equivalence of the TRIPLE
       (next reduced state, delta n_swap, delta n_P3)
    over all 24^4 reduced states, every k. Raises Anomaly on any mismatch.
    State-only comparison is insufficient: see [COR] (1) in the header."""
    allr = list(itertools.product(range(N), repeat=4))
    for k in K_SET:
        bad = 0
        for r in allr:
            DAB, DAC, dAB, dAC = r
            u = v18.Universe(N=N, k=k,
                             theta={0: 0, 1: (0 - DAB) % N, 2: (0 - DAC) % N},
                             delta={0: 0, 1: (0 - dAB) % N, 2: (0 - dAC) % N})
            s0, p0 = u.single_edge_swaps, u.path_interactions
            v18.step_universe(u, multistar_policy="bound_symmetric")
            ds = u.single_edge_swaps - s0
            dp = u.path_interactions - p0
            t, d = u.theta, u.delta
            theirs = ((t[0] - t[1]) % N, (t[0] - t[2]) % N,
                      (d[0] - d[1]) % N, (d[0] - d[2]) % N)
            ours_state, ev = step(lift(r), k)
            if canon(ours_state) != theirs or (int(ev == 'S'), int(ev == 'P')) != (ds, dp):
                bad += 1
        if bad:
            raise Anomaly(f"v18 triple-equivalence FAILED at k={k}: {bad} mismatches")
        print(f"    k={k}: 0 mismatches / {len(allr)} (state + both counters)")


# --------------------------------------------------------------- seed panel
def supplementary_panel():
    """The six REGISTERED rows |d|_c = 3,4,5. Generated once; reused at all k.
    Deterministic IDs encode the full reduced coordinates."""
    B = set(range(-1, 2))                      # B_k at k=1, the registered band
    out = []
    for d in range(-N // 2, N // 2):
        if d == 0:
            continue
        if abs(sc(d)) not in (3, 4, 5):        # registered rows ONLY
            continue
        for eps in sorted(B):                  # overlap empty -> all band offsets
            DAB = (N // 2 + eps) % N
            for DAC, dAC in itertools.product(range(N), repeat=2):
                r = (DAB, DAC, (-d) % N, (-dAC) % N)
                out.append((f"sup_{r[0]}_{r[1]}_{r[2]}_{r[3]}", r))
    return out


# ------------------------------------------------------------- measurements
def cycle_record(r, k):
    """Exact eventual cycle in reduced coordinates. Cycle-only event counts."""
    s = lift(r); seen = {}; ev = []; t = 0
    while t < STEP_CAP:
        key = canon(s)
        if key in seen:
            pre = seen[key]
            c = ev[pre:t]
            return (c.count('S'), c.count('P'), pre, t - pre)
        seen[key] = t
        s, e = step(s, k)
        ev.append(e); t += 1
    raise Anomaly(f"cycle detection hit STEP_CAP for seed {r} at k={k}")


def trajectory_blind(r, k):
    """Realization-level blindness: evolve the PAIR (F_1^t(x), F_k^t(x)) from the
    SAME original seed until the pair-state repeats. Blind iff the pair never
    leaves the diagonal. Eventual-cycle equality is NOT used."""
    if k == K_BASE:
        return None
    a = b = lift(r); seen = set(); t = 0
    while t < STEP_CAP:
        key = (canon(a), canon(b))
        if key in seen:
            return True
        if key[0] != key[1]:
            return False
        seen.add(key)
        a, _ = step(a, K_BASE)
        b, _ = step(b, k)
        t += 1
    raise Anomaly(f"paired blindness detection hit STEP_CAP for seed {r} at k={k}")


# --------------------------------------------------------------------- main
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    print("[1/4] pinning and verifying the owner source ...")
    v18 = load_pinned_v18(os.path.join(here, OWNER_FILENAME))
    print("      exhaustive triple-equivalence (state + n_swap + n_P3) ...")
    verify_against_v18(v18)

    print("[2/4] generating the registered supplementary panel ...")
    panel = supplementary_panel()
    if len(panel) != EXPECTED_SEEDS:
        raise SystemExit(f"ABORT: panel size {len(panel)} != {EXPECTED_SEEDS}")
    if len({sid for sid, _ in panel}) != EXPECTED_SEEDS:
        raise SystemExit("ABORT: seed IDs are not unique")
    from collections import Counter
    per_d = dict(sorted(Counter(sc((-r[2]) % N) for _, r in panel).items()))
    if per_d != EXPECTED_PER_D:
        raise SystemExit(f"ABORT: signed supplementary-row counts {per_d} "
                         f"!= {EXPECTED_PER_D}")
    print(f"    {len(panel)} seeds; signed per-d counts {per_d}")

    print("[3/4] enumerating all trajectories ...")
    harness_rows, transport_rows = [], []
    for sid, r in panel:
        for k in K_SET:
            a, b, pre, per = cycle_record(r, k)
            harness_rows.append({"seed_id": sid, "k": k,
                                 "dual_active": (a > 0 and b > 0),
                                 "n_swap": a, "n_p3": b,
                                 "cycle_len": per, "preperiod": pre})
            transport_rows.append({"seed_id": sid, "domain_id": "SUP_d345",
                                   "k": k, "raw_reduced_state": list(r),
                                   "n_swap": a, "n_p3": b,
                                   "preperiod": pre, "period": per,
                                   "dual_active": (a > 0 and b > 0),
                                   "blind_vs_base": trajectory_blind(r, k)})
    if len(harness_rows) != EXPECTED_RECORDS:
        raise SystemExit(f"ABORT: {len(harness_rows)} records != {EXPECTED_RECORDS}")

    print("[4/4] writing artifacts ...")
    for name, rows in (("disc2_enumeration_sup_d345.json", harness_rows),
                       ("disc2_transport_sup_d345.json", transport_rows)):
        json.dump(rows, open(name, "w"))
        h = hashlib.sha256(open(name, "rb").read()).hexdigest()
        print(f"    {name}  ({len(rows)} rows)  sha256 {h}")
    print("DONE. No verdict is computed here; the sealed harness decides.")


if __name__ == "__main__":
    main()
