#!/usr/bin/env python3
"""AZ token-resonance fixtures - [SESSION] NONCANONICAL; bounded deterministic tests of the runner and of the two
kinematic statements of records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md section 2 on the pinned TDR-G engine.

usage
  python -I az_tokres_fixtures.py --engine ENGINE.py --orient ORIENT.py --runner az_tokres_run.py
         --analysis az_tokres_analyse.py --golden GOLDEN.json [--write-golden] [--exhaustive N6k0|N8k1]
Exit code 0 iff every test passes. --write-golden (re)creates the golden file from this machine's results; it is used
once when the package is frozen and never by a verifier. --exhaustive runs one extra, longer enumeration.
"""
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import random
import sys
import time
from math import gcd

FIX_TAG = "FIXTURE"
OK = True


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def report(name, cond, detail=""):
    global OK
    OK &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (" :: " + detail if detail else ""))


def key(r):
    return (r["M"], r["births"], r["steps"], r["fb"], tuple(sorted(r["M_at"].items())))


def cabs(x, N):
    x %= N
    return min(x, N - x)


def tau(x, N, k):
    """First j >= 1 with |2jx|_c <= k (first return of a free parent-child pair to the defect band)."""
    for j in range(1, N + 1):
        if cabs(2 * j * x, N) <= k:
            return j


def order2x(x, N):
    y = (2 * x) % N
    return 1 if y == 0 else N // gcd(y, N)


def hub_births(R, eng, N, k, T, x):
    """Isolated hub: centre and three co-located antipodal leaves, all with token x; births in T ticks."""
    th = [(0 - x) % N] + [(N // 2 - x) % N] * 3
    return R.run_state(eng, N, k, th, [x] * 4, T, 0, "bound_symmetric", tdr26=False)["births"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", required=True)
    ap.add_argument("--orient", required=True)
    ap.add_argument("--runner", required=True)
    ap.add_argument("--analysis", required=True)
    ap.add_argument("--golden", required=True)
    ap.add_argument("--write-golden", action="store_true")
    ap.add_argument("--exhaustive", default=None, choices=["N6k0", "N8k1"])
    a = ap.parse_args()
    sys.dont_write_bytecode = True
    R = load_module(a.runner, "az_tokres_run")
    t0 = time.time()
    print("bytes under test (SHA-256):")
    for label, path in (("engine", a.engine), ("orientation reference", a.orient), ("runner", a.runner),
                        ("fixtures script", __file__), ("analysis script", a.analysis)) + (
                            () if a.write_golden else (("golden file", a.golden),)):
        print("  %-22s %s" % (label, R.sha256_file(path)))

    # T1 pins
    report("T1 engine pin", R.sha256_file(a.engine) == R.ENGINE_SHA256, R.ENGINE_SHA256[:12])
    report("T1 orientation-reference pin", R.sha256_file(a.orient) == R.ORIENT_SHA256, R.ORIENT_SHA256[:12])

    eng, _ = R.load_engine(a.engine, a.orient, "P2")         # engine as placed: built-in orient_path
    native_orient = eng.orient_path
    p1_orient = sys.modules["tdrg_orient_reference"].make_orient(eng)
    report("T1 two orientation bindings on one unmodified engine module", p1_orient is not native_orient)

    def use(profile):
        eng.orient_path = p1_orient if profile == "P1" else native_orient
        return eng

    golden = {}
    if not a.write_golden:
        with open(a.golden) as f:
            golden = json.load(f)
    new = {}

    # T2 the runner's loop equals the engine's run_one on the native draw (both profiles, two policies)
    bad = n = 0
    for prof in ("P2", "P1"):
        e = use(prof)
        for pol in ("bound_symmetric", "largest_center"):
            for b in range(6):
                seed, th, d = R.base_draw(e, FIX_TAG, 120, 8, b)
                u = e.run_one(N=120, k=8, T=250, seed=seed, multistar_policy=pol, max_nodes=150)
                r = R.run_state(e, 120, 8, th, d, 250, 150, pol, tdr26=False, keep_final=True)
                bad += (dict(u.theta), dict(u.delta), u.births, u.steps, u.hit_node_cap) != (
                    r["_theta"], r["_delta"], r["births"], r["steps"], r["hit_cap"])
                n += 1
    report("T2 runner loop == engine run_one (final theta, delta, births, steps, cap flag)", bad == 0, f"{n} runs, {bad} differ")

    # T3 the orientation exchange takes effect exactly on the antipodal-endpoint stratum (S = 0, E = N/2)
    def p3_state():
        post_theta, delta = [13, 0, 13], [0, 5, 12]                    # N = 24, k = 1; path 0-1-2, centre 1
        return [(t - d) % 24 for t, d in zip(post_theta, delta)], delta
    out = {}
    for prof in ("P2", "P1"):
        e = use(prof)
        th, d = p3_state()
        u = e.Universe(N=24, k=1, theta=dict(enumerate(th)), delta=dict(enumerate(d)))
        e.step_universe(u, multistar_policy="bound_symmetric")
        out[prof] = ([u.delta[i] for i in range(3)], u.path_interactions, u.path_ties_seen, u.path_ties_bound)
    report("T3 built-in orientation rotates the tokens on S=0, E=N/2", out["P2"] == ([5, 12, 0], 1, 0, 0), str(out["P2"]))
    report("T3 TDRG-DEF-ORIENT (v2.12.14) returns the balanced tie there", out["P1"] == ([0, 5, 12], 0, 1, 1), str(out["P1"]))

    # T4 collecting the motif row does not change the dynamics; T8 half-turn token shift; T9 label permutation
    e = use("P1")
    d_motif = d_shift = d_perm = n = 0
    for b in range(10):
        _, th, d = R.base_draw(e, FIX_TAG, 120, 8, b)
        ch = R.arm_choices(FIX_TAG, 120, 8, b)
        for arm in ("BASE", "O1R", "O2R"):
            th1, d1 = R.arm_state(arm, th, d, ch, 120)
            r0 = R.run_state(e, 120, 8, th1, d1, 300, 200, "bound_symmetric", tdr26=False, keep_final=True)
            r1 = R.run_state(e, 120, 8, th1, d1, 300, 200, "bound_symmetric", tdr26=True, keep_final=True)
            d_motif += (r0["_theta"], r0["_delta"]) != (r1["_theta"], r1["_delta"])
            rs = R.run_state(e, 120, 8, th1, [(x + 60) % 120 for x in d1], 300, 200, "bound_symmetric", tdr26=False)
            d_shift += key(rs) != key(r0)
            if arm in ("BASE", "O1R"):
                thp, dp = R.arm_state(arm + "_P", th, d, ch, 120)
                d_perm += key(R.run_state(e, 120, 8, thp, dp, 300, 200, "bound_symmetric", tdr26=False)) != key(r0)
            n += 1
    report("T4 motif collection is dynamically neutral", d_motif == 0, f"{n} runs")
    report("T8 delta -> delta + N/2 on all nodes leaves (M, births, steps, fb, M_at) unchanged", d_shift == 0, f"{n} runs")
    report("T9 permuting the four initial labels leaves (M, births, steps, fb, M_at) unchanged (P1)", d_perm == 0, "20 runs")

    # T5 law check: zero violations on fixture runs, and the checker is not vacuous
    viol = births = 0
    for b in range(10):
        _, th, d = R.base_draw(e, FIX_TAG, 120, 8, b)
        ch = R.arm_choices(FIX_TAG, 120, 8, b)
        for arm in R.arms_for(120):
            th1, d1 = R.arm_state(arm, th, d, ch, 120)
            for pol in ("bound_symmetric", "all_centers"):
                r = R.run_state(e, 120, 8, th1, d1, 200, 200, pol, tdr26=False)
                viol += r["law_viol"]
                births += r["births"]
    report("T5 token alphabet, exact class update c(-x) += 1 per birth, centre witness: no violation", viol == 0,
           f"120 runs, {births} births")

    class Corrupt:                                                   # engine shim that breaks the law at tick 5
        Universe = eng.Universe

        @staticmethod
        def step_universe(u, multistar_policy="bound_symmetric", collect_motif=False):
            m = eng.step_universe(u, multistar_policy=multistar_policy, collect_motif=collect_motif)
            if u.steps == 5:
                u.delta[0] = (max(u.delta.values()) + 7) % u.N
            return m
    r = R.run_state(Corrupt, 120, 8, [0, 10, 20, 30], [3, 5, 9, 11], 10, 0, "bound_symmetric", tdr26=False)
    report("T5 negative control: an injected foreign token is detected", r["law_viol"] > 0, f"counter {r['law_viol']}")

    def hub_state(x, N=120):                                         # first tick: clean star, one birth
        return [(0 - x) % N] + [(N // 2 - x) % N] * 3, [x] * 4

    def make_shim(mutate):
        state = {"done": False}

        class Shim:
            Universe = eng.Universe

            @staticmethod
            def step_universe(u, multistar_policy="bound_symmetric", collect_motif=False):
                before = set(u.theta)
                m = eng.step_universe(u, multistar_policy=multistar_policy, collect_motif=collect_motif)
                new = [i for i in u.theta if i not in before]
                if new and not state["done"]:
                    state["done"] = True
                    mutate(u, new[0])
                return m
        return Shim

    def unflip_centre(u, child):                                     # the centre keeps x instead of taking -x
        x = u.delta[child]
        for i in u.theta:
            if i != child and u.theta[i] == (u.theta[child] + u.N // 2) % u.N and u.delta[i] == (-x) % u.N:
                u.delta[i] = x
                return

    def flip_child(u, child):                                        # the child takes -x instead of x
        u.delta[child] = (-u.delta[child]) % u.N

    th, d = hub_state(7)
    u = eng.Universe(N=120, k=8, theta=dict(enumerate(th)), delta=dict(enumerate(d)))
    make_shim(unflip_centre).step_universe(u)
    weak_ok = set(u.delta.values()) <= {7, 113} and sorted(u.delta.values()) == [7] * 5 and u.births == 1
    r = R.run_state(make_shim(unflip_centre), 120, 8, th, d, 3, 0, "bound_symmetric", tdr26=False)
    report("T5b negative control: a birth that adds its count at x instead of -x passes the weak checks "
           "(alphabet, no decrease, total) and is caught by the exact class update", weak_ok and r["law_viol"] > 0,
           f"weak checks pass: {weak_ok}; counter {r['law_viol']}")
    r = R.run_state(make_shim(flip_child), 120, 8, th, d, 3, 0, "bound_symmetric", tdr26=False)
    report("T5c negative control: a child born with -x instead of x is caught", r["law_viol"] > 0, f"counter {r['law_viol']}")
    r = R.run_state(eng, 120, 8, th, d, 3, 0, "bound_symmetric", tdr26=False)
    report("T5d the same hub without the shim: no violation", r["law_viol"] == 0 and r["births"] >= 1, f"births {r['births']}")

    # T6 free parent-child phase law on the engine: post-birth pair (centre -x, child x at the antipode)
    bad = n = 0
    for N, k in ((24, 1), (24, 3), (120, 8), (122, 8)):
        for x in range(N):
            u = eng.Universe(N=N, k=k, theta={0: 0, 1: N // 2}, delta={0: (-x) % N, 1: x})
            t = tau(x, N, k)
            for j in range(1, t + 1):
                eng.step_universe(u, multistar_policy="bound_symmetric")
                ok = (u.theta[1] - u.theta[0]) % N == (N // 2 + 2 * j * x) % N
                ok &= (u.single_edge_swaps == 0) if j < t else (u.single_edge_swaps == 1)
                bad += not ok
            ok = (t == 1 and (2 * x) % N == 0) == (order2x(x, N) == 1)
            ok &= ((4 * x) % N == 0) == (order2x(x, N) <= 2)
            bad += not ok
            n += 1
    report("T6 Delta(j) = N/2 + 2jx until the first band return at j = tau(x); 4x = 0 <=> ord(2x) <= 2", bad == 0, f"{n} tokens")

    # T12 the analysis script's independent re-derivation of every registered initial state equals the runner's
    A = load_module(a.analysis, "az_tokres_analyse")
    bad = n = 0
    for N in (120, 122):
        for b in range(40):
            seed, th, d = R.base_draw(e, FIX_TAG, N, 8, b)
            ch = R.arm_choices(FIX_TAG, N, 8, b)
            for arm in R.arms_for(N) + ("BASE_P", "O1R_P"):
                th1, d1 = R.arm_state(arm, th, d, ch, N)
                mine = {"seed": seed, "slot": ch["slot"], "choices": ch, "th0": th1, "d0": d1, "d0_base": d,
                        "alphabet_class": R.alphabet_class(d1, N), "slot_class": R.res_class(R.slot_token(arm, d1, ch), N)}
                bad += A.expected_state(FIX_TAG, N, 8, b, arm) != mine
                n += 1
    report("T12 analysis-side re-derivation of seed, phases, tokens, slot, choices and classes == runner (engine draw)",
           bad == 0 and A.arms_for(120) == R.arms_for(120) and A.arms_for(122) == R.arms_for(122), f"{n} states, {bad} differ")
    report("T12 analysis pins: engine and orientation reference equal the runner's",
           A.ENGINE_SHA256 == R.ENGINE_SHA256 and A.ORIENT_SHA256 == R.ORIENT_SHA256 and A.SCHEMA == R.SCHEMA
           and A.MANIFEST_SCHEMA == R.MANIFEST_SCHEMA)

    # T7 regression: isolated same-token hub, births in 60 ticks for every token; T10 seed derivation
    for N in (120, 122):
        new[f"hub_N{N}_k8_T60"] = [hub_births(R, e, N, 8, 60, x) for x in range(N)]
    new["seeds"] = []
    for N in (120, 122):
        for b in range(3):
            seed, th, d = R.base_draw(e, FIX_TAG, N, 8, b)
            new["seeds"].append({"N": N, "b": b, "seed": seed, "th0": th, "d0": d, "choices": R.arm_choices(FIX_TAG, N, 8, b)})
    new["run_keys"] = []
    for b in range(4):
        _, th, d = R.base_draw(e, FIX_TAG, 120, 8, b)
        ch = R.arm_choices(FIX_TAG, 120, 8, b)
        for arm in ("BASE", "O1R", "O2R"):
            th1, d1 = R.arm_state(arm, th, d, ch, 120)
            r = R.run_state(e, 120, 8, th1, d1, 300, 200, "bound_symmetric", tdr26=True)
            new["run_keys"].append({"b": b, "arm": arm, "M": r["M"], "births": r["births"], "fb": r["fb"],
                                    "top_class": r["top_class"], "tdr26": r["tdr26"]})
    if a.write_golden:
        with open(a.golden, "w", newline="\n") as f:
            json.dump(new, f, sort_keys=True, indent=1)
            f.write("\n")
        print("golden written:", a.golden)
    else:
        norm = lambda o: json.loads(json.dumps(o, sort_keys=True))
        report("T7 hub table equals the golden file (N = 120, 122; 60 ticks)",
               all(norm(new[q]) == golden.get(q) for q in ("hub_N120_k8_T60", "hub_N122_k8_T60")))
        report("T10 seed derivation and native draws equal the golden file", norm(new["seeds"]) == golden.get("seeds"))
        report("T10 fixture run summaries equal the golden file", norm(new["run_keys"]) == golden.get("run_keys"))
    h = new["hub_N120_k8_T60"]
    report("T7 a hub with 2x = 0 gives one birth per tick (N = 120: x = 0, 60)", h[0] == 60 and h[60] == 60, f"{h[0]}, {h[60]}")

    # T11 optional exhaustive enumeration of four-node universes (theta_0 = 0 by phase gauge)
    if a.exhaustive:
        N, k = (6, 0) if a.exhaustive == "N6k0" else (8, 1)
        T, cap = 16, 24
        viol = births = states = with_birth = 0
        for th in itertools.product(range(N), repeat=3):
            for d in itertools.product(range(N), repeat=4):
                r = R.run_state(e, N, k, (0,) + th, d, T, cap, "bound_symmetric", tdr26=False)
                viol += r["law_viol"]
                births += r["births"]
                with_birth += r["births"] > 0
                states += 1
        report(f"T11 exhaustive N={N}, k={k}, T={T}, cap={cap}: token alphabet, exact class update, centre witness",
               viol == 0, f"{states} states, {with_birth} with a birth, {births} births, {viol} violations")

    print(f"FIXTURES {'PASS' if OK else 'FAIL'} ({time.time() - t0:.1f} s; python {sys.version.split()[0]})")
    return 0 if OK else 1


if __name__ == "__main__":
    raise SystemExit(main())
