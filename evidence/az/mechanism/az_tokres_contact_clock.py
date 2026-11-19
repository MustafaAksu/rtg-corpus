#!/usr/bin/env python3
"""AZ mechanism study, fork design section 2.2 - BASE contact clock tau_C and the C-/C+ boundary states (synthetic stage).

[SESSION] NONCANONICAL instrument. Fork design records/az/AZ_TOKEN_RESONANCE_FORK_DESIGN.md r2 (PR #322, head 08ef706,
Gate D PASS 5960841961); first Gate I deliverable as specified in PR #322 comment 7008416095 (PI decision of
19 Nov 2026, source-reported there). Written by the Claude AZ lane; reviewed by ChatGPT. Synthetic only: it reads
no registered record, implements no fork operator and no intervention epoch, and runs no R/D arm.

Definitions (design 2.2-2.4)
  * c_j = j is the original copy of slot node j (four-node initialisation; root copy id = initial node id).
  * From the complete end-of-tick BASE state S_{t-1}: theta_pre(t) = (theta + delta) mod N for every node,
    E_t = graph_edges_for(nodes, theta_pre(t), N, k) (pinned engine function, pure), v = carrier_{t-1}(c_j) from the
    section 6.1 provenance sidecar. tau_C = min{t >= 1 : v has an incident edge in E_t}; bound, tied and event-free
    contacts count (a graph-contact clock, not an event clock).
  * C- boundary: the complete state S_{tau_C - 1} (no BASE tick past it); C+ boundary: S_{tau_C} after the BASE
    contact tick. Each is a deep checkpoint (az_tokres_provenance.checkpoint); absolute ticks are never reset.
  * Eligibility of a boundary state: done is False, iters < T_ref and, for a positive cap, M < cap. The reference
    runner uses T_ref = L + 1 so that a contact at tick L is reachable and its C+ state is not T-terminal.
  * Status of a seed: contact (tau_C <= L), no_contact_by_L, or terminated_before_contact (cap reached first).
  * The prediction is read-only: it advances copies of the phases and calls the pure graph helper of the plain
    engine instance; it never steps the engine, never calls orient_path and needs no hook in the engine.

    python3 -I evidence/az/mechanism/az_tokres_contact_clock.py --selftest

Exit 0 iff every self-test check passes ("SELFTEST PASS").
"""
from __future__ import annotations

import copy
import hashlib
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import az_tokres_provenance as P                                     # noqa: E402

LIB = os.path.join(HERE, "az_tokres_provenance.py")
LIB_SHA = "5d5ca8ac50e5223c12db904b2225ab23983ce01af56a543b39dfc37e8ed13f68"     # merged at 8de175c (PR #313)
SYNTH_TAG = "AZ-FORK-CLOCK-SYNTH"            # synthetic seeds only; never a registered campaign tag


def check_pins():
    P.check_pins()
    if P.sha256_file(LIB) != LIB_SHA:
        sys.exit("STOP: pin mismatch for az_tokres_provenance.py")


# ---------------------------------------------------------------- the clock
def predicted_graph(peng, st):
    """Pure prediction of the next tick's pre-interaction defect graph from the complete state st (not modified)."""
    u = st.u
    nodes = list(u.theta)
    th = {x: (u.theta[x] + u.delta[x]) % st.N for x in nodes}
    return nodes, th, sorted(peng.graph_edges_for(nodes, th, st.N, st.k))


def eligible(st):
    """Fork eligibility of a boundary state: nonterminal, within the reference budget, below a positive cap."""
    return (not st.done) and st.iters < st.T and (st.cap <= 0 or len(st.u.theta) < st.cap)


def contact_clock(peng, ieng, run, st, j, L, q=100):
    """Run the BASE prefix st (fresh RunState on the provenance-instrumented instance, T = L + 1) until the first
    graph contact of copy c_j, or until L / termination. Returns a dict; st is advanced (to tau_C at most)."""
    if st.prov is None or st.T < L + 1 or st.u.steps != 0:
        raise ValueError("contact_clock needs a fresh provenance RunState with T >= L + 1")
    c = j
    base_token = st.u.delta[j]
    out = {"status": None, "tau_C": None, "edges": None, "carrier_pre": None, "minus": None, "plus": None,
           "eligible_minus": False, "eligible_plus": False, "pos_minus": None, "pos_plus": None,
           "carrier_plus": None, "carrier_minus_is_j": None, "token_minus_is_base": None,
           "slot_birth_at_contact": None, "slot_events_before": None}
    while True:
        t = st.u.steps + 1
        if t > L:
            out["status"] = "no_contact_by_L"
            return out
        if not eligible(st):
            out["status"] = "terminated_before_contact"
            return out
        _, _, edges = predicted_graph(peng, st)
        v = st.prov.carrier[c]
        inc = [e for e in edges if v in e]
        if inc:
            break
        it0 = st.iters
        P.tick(ieng, run, st)
        if st.iters == it0:                                      # fail closed: no progress means the run has ended
            out["status"] = "terminated_before_contact"
            return out
    out.update(status="contact", tau_C=t, edges=inc, carrier_pre=v)
    minus = P.checkpoint(st)
    out["minus"] = minus
    out["eligible_minus"] = eligible(minus)
    out["pos_minus"] = len(minus.u.theta) >= q
    out["carrier_minus_is_j"] = v == j
    out["token_minus_is_base"] = minus.u.delta[j] == base_token
    out["slot_events_before"] = sum(1 for _, kind, d in minus.prov.events
                                    if (kind == "birth" and d[2] == c) or (kind != "birth" and j in d))
    P.tick(ieng, run, st)                                            # the BASE contact tick
    plus = P.checkpoint(st)
    out["plus"] = plus
    out["eligible_plus"] = eligible(plus)
    out["pos_plus"] = len(plus.u.theta) >= q
    out["carrier_plus"] = plus.prov.carrier[c]
    out["slot_birth_at_contact"] = any(tt == t and kind == "birth" and d[2] == c for tt, kind, d in plus.prov.events)
    return out


def tau_free(peng, N, k, th0, d0, j, L):
    """Counterfactual free-flight first contact of node j (every node keeps its initial token). NOT tau_C."""
    for t in range(1, L + 1):
        pj = (th0[j] + t * d0[j]) % N
        for i in range(len(th0)):
            if i != j and peng.is_defect(pj, (th0[i] + t * d0[i]) % N, N, k):
                return t
    return None


# ================================================================ self-test (synthetic only)
def install_graph_observer(eng):
    """Test only: wrap graph_edges_for of a separate instance; the original is called once, its result recorded."""
    rec = []
    orig = eng.graph_edges_for

    def graph_edges_for(nodes, theta, N, k):
        res = orig(nodes, theta, N, k)
        rec.append((list(nodes), dict(theta), sorted(res)))
        return res
    eng.graph_edges_for = graph_edges_for
    return rec


def observe(oeng, run, rec, peng, N, k, th0, d0, j, T, cap):
    """Independent reference: run BASE on the observed instance, record per tick the engine's own graph, the carrier
    at the start of the tick (provenance pre-tick labels), the pure prediction and the state fingerprints."""
    st = P.RunState(oeng, run, N, k, th0, d0, T, cap, provenance=True, strict=True)
    ticks, fps, phys = [], [P.fingerprint(st)], [P.fingerprint(st, with_prov=False)]
    rng_state = random.getstate()
    while not st.done:
        pred = predicted_graph(peng, st)
        n0, it0 = len(rec), st.iters
        P.tick(oeng, run, st)
        if st.iters == it0:
            break
        calls = rec[n0:]
        carrier = next(v for v, (cp, _) in st.prov._pre.items() if cp == j)
        ticks.append({"t": st.u.steps, "calls": calls, "pred": pred, "carrier": carrier})
        fps.append(P.fingerprint(st))
        phys.append(P.fingerprint(st, with_prov=False))
    return st, ticks, fps, phys, random.getstate() == rng_state


def selftest(trials=400, verbose=True, coverage=True):
    opened = []

    def hook(event, args):
        if event == "open" and args and isinstance(args[0], str):
            opened.append(os.path.abspath(args[0]))
    sys.addaudithook(hook)                                # before anything is read (audit hooks cannot be removed)
    check_pins()
    run = P.load_runner()
    peng = P.load_engine("clk_engine_plain")
    ieng = P.load_engine("clk_engine_instr")
    P.install(ieng)
    oeng = P.load_engine("clk_engine_observed")
    P.install(oeng)
    rec = install_graph_observer(oeng)
    C = P.Checks()
    say = print if verbose else (lambda *a: None)
    say("pins: engine 4c94d874, orientation ca59e9b9, runner 75c5f139, provenance library 5d5ca8ac - OK")

    def clock(N, k, th0, d0, j, L, cap, q=100):
        st = P.RunState(ieng, run, N, k, th0, d0, L + 1, cap, provenance=True, strict=True)
        return contact_clock(peng, ieng, run, st, j, L, q), st

    # ---- A. explicit fixtures (N = 24, k = 2: an edge iff the separation is 10..14)
    N, k = 24, 2
    fx = P.fixture_state
    th, d = fx(N, [0, 12], [5, 7])
    r, _ = clock(N, k, th, d, 0, 50, 0)
    C.ok(r["status"] == "contact" and r["tau_C"] == 1 and r["edges"] == [(0, 1)] and r["minus"].iters == 0
         and r["carrier_pre"] == 0 and r["carrier_plus"] == 1 and r["eligible_minus"] and r["eligible_plus"],
         "A1 tick-1 contact (swap): tau_C = 1, C- = S_0, edge (0,1), carrier moves to node 1 at C+")
    th, d = [0, 6], [1, 0]
    r, _ = clock(N, k, th, d, 0, 50, 0)
    C.ok(r["status"] == "contact" and r["tau_C"] == 16 and r["edges"] == [(0, 1)] and r["minus"].u.steps == 15
         and tau_free(peng, N, k, th, d, 0, 50) == 16,
         "A2 delayed contact: slot at 0 moving +1, partner fixed at 6: tau_C = 16 = tau_free, C- = S_15")
    th, d = fx(N, [0, 12, 1, 13], [3, 3, 3, 3])
    r, _ = clock(N, k, th, d, 0, 50, 0)
    C.ok(r["tau_C"] == 1 and r["edges"] == [(0, 1), (0, 3)] and r["carrier_plus"] == 0
         and r["plus"].u.bound_cycle_hits == 1 and not r["plus"].prov.events,
         "A3 contact in a bound 4-cycle (no event): counted; carrier stays; both slot edges listed")
    th, d = fx(N, [0, 12, 11, 13], [5, 2, 3, 4])
    r, _ = clock(N, k, th, d, 0, 50, 5)
    C.ok(r["tau_C"] == 1 and r["slot_birth_at_contact"] and r["carrier_plus"] == 0 and r["eligible_minus"]
         and not r["eligible_plus"] and r["plus"].hit_cap,
         "A4 slot is the centre of a birth at contact, cap 5: C+ carrier = centre (6.1 convention); C+ ineligible "
         "(cap reached on the contact tick), C- eligible")
    th, d = [0, 3], [4, 4]
    r, _ = clock(N, k, th, d, 0, 30, 0)
    C.ok(r["status"] == "no_contact_by_L" and r["tau_C"] is None, "A5 never in contact (equal velocities): "
         "no_contact_by_L, no time substituted")
    th, d = fx(N, [0, 12], [12, 12])
    r, _ = clock(N, k, th, d, 0, 50, 0)
    C.ok(r["tau_C"] == 1 and r["carrier_plus"] == 1 and r["plus"].u.delta == {0: 12, 1: 12},
         "A6 equal, sign-invisible tokens (x = N/2): values unchanged at contact, carrier still tracked to node 1")
    th, d = fx(N, [0, 12, 5, 17], [5, 7, 9, 2])
    r, _ = clock(N, k, th, d, 0, 50, 0)
    C.ok(r["tau_C"] == 1 and r["edges"] == [(0, 1)] and len(r["plus"].prov.events) == 2,
         "A7 two components in the contact tick: only the slot's edges; both events happen")
    th, d = fx(N, [0, 12, 11, 13, 5], [5, 2, 3, 4, 1])
    r, _ = clock(N, k, th, d, 4, 50, 5)
    C.ok(r["status"] == "terminated_before_contact" and r["tau_C"] is None,
         "A8 cap reached by another component before the slot's contact: terminated_before_contact")

    # ---- B. randomized synthetic trajectories: clock vs the engine's own graph, and on/off identity
    rng = random.Random(SYNTH_TAG)
    cover = {key: 0 for key in ("contact", "no_contact_by_L", "terminated_before_contact", "tau1", "events_before",
                                "birth_before", "free_differs", "free_earlier", "free_later_or_none",
                                "contact_no_slot_event", "carrier_moved", "slot_birth", "plus_ineligible",
                                "multi_component_contact_tick", "equal_tokens", "sign_invisible", "pos_minus",
                                "native_120_8")}
    n_ticks = 0
    for trial in range(trials):
        kind = trial % 4
        if kind == 0:                                               # native draws in the chosen cell
            N, k, L = 120, 8, 400
            seed = int.from_bytes(hashlib.sha256(("%s|%d" % (SYNTH_TAG, trial)).encode()).digest()[:8], "big")
            u0 = peng.init_universe(N=N, k=k, rng=random.Random(seed))
            th0, d0 = [u0.theta[i] for i in range(4)], [u0.delta[i] for i in range(4)]
            cap = rng.choice([0, 100, 300])
            q = 100
            cover["native_120_8"] += 1
        else:
            N, k = [(24, 2), (60, 6), (120, 8)][kind - 1]
            m0 = rng.randint(3, 7)
            special = [0, N // 2]
            d0 = [rng.choice(special) if rng.random() < 0.3 else rng.randrange(N) for _ in range(m0)]
            if rng.random() < 0.4:
                d0[rng.randrange(m0)] = d0[rng.randrange(m0)]
            th0 = [rng.randrange(N) for _ in range(m0)]
            L = rng.choice([3, 20, 60, 150])
            cap = rng.choice([0, 0, m0 + 1, m0 + 2, 8, 12, 40])
            q = rng.choice([5, 8, 100])
        j = rng.randrange(len(th0))
        r, st = clock(N, k, th0, d0, j, L, cap, q)
        so, ticks, fps, phys, rng_ok = observe(oeng, run, rec, peng, N, k, th0, d0, j, L + 1, cap)
        n_ticks += len(ticks)
        cover[r["status"]] += 1
        # independent tau from the engine's own graphs and pre-tick carriers
        tau_obs = None
        graphs_ok = True
        for tk in ticks:
            if len(tk["calls"]) != 1:
                graphs_ok = False
                continue
            nodes, theta, edges = tk["calls"][0]
            pn, pth, pe = tk["pred"]
            if (nodes, theta, edges) != (pn, pth, pe) or pe != peng.graph_edges_bruteforce(pn, pth, N, k):
                graphs_ok = False
            if tau_obs is None and any(tk["carrier"] in e for e in edges):
                tau_obs = tk["t"]
                obs_edges = [e for e in edges if tk["carrier"] in e]
                obs_carrier = tk["carrier"]
        C.ok(graphs_ok, "B1 trial %d: one engine graph call per tick; pure prediction = engine graph (nodes, phases, "
                        "edges) = brute-force graph at every tick" % trial)
        if r["status"] == "contact":
            t = r["tau_C"]
            C.ok(tau_obs == t and r["edges"] == obs_edges and r["carrier_pre"] == obs_carrier,
                 "B2 trial %d: tau_C, its incident edge set and the pre-tick carrier equal the engine-observed ones"
                 % trial)
            C.ok(t < len(fps) and P.fingerprint(r["minus"]) == fps[t - 1] and P.fingerprint(r["plus"]) == fps[t],
                 "B3 trial %d: C- and C+ states equal the independent run at ticks tau_C - 1 and tau_C" % trial)
            C.ok(r["carrier_minus_is_j"] and r["token_minus_is_base"] and r["slot_events_before"] == 0,
                 "B4 trial %d: before tau_C the slot copy took part in no event: carrier j, original token" % trial)
            C.ok(t <= len(ticks) and r["carrier_plus"] == so_carrier_at(fps, ticks, t, j, so) and
                 r["eligible_plus"] == (not so_done_at(ticks, t, so, cap, L)),
                 "B5 trial %d: C+ carrier and C+ eligibility agree with the independent run" % trial)
            pre_ev = [e for e in r["minus"].prov.events]
            cover["tau1"] += t == 1
            cover["events_before"] += bool(pre_ev)
            cover["birth_before"] += any(kd == "birth" for _, kd, _ in pre_ev)
            tf = tau_free(peng, N, k, th0, d0, j, L)
            cover["free_differs"] += tf != t
            cover["free_earlier"] += tf is not None and tf < t
            cover["free_later_or_none"] += tf is None or tf > t
            moved = r["carrier_plus"] != r["carrier_pre"]
            cover["carrier_moved"] += moved
            cover["slot_birth"] += bool(r["slot_birth_at_contact"])
            cover["contact_no_slot_event"] += (not moved) and not r["slot_birth_at_contact"]
            cover["plus_ineligible"] += not r["eligible_plus"]
            comps = ticks[t - 1]["calls"][0][2] if t <= len(ticks) and ticks[t - 1]["calls"] else []
            cover["multi_component_contact_tick"] += len({e for e in comps if r["carrier_pre"] not in e}) > 0
            dj = r["minus"].u.delta[j]
            cover["equal_tokens"] += sum(1 for v in r["minus"].u.delta.values() if v == dj) >= 2
            cover["sign_invisible"] += (2 * dj) % N == 0
            cover["pos_minus"] += bool(r["pos_minus"])
        else:
            C.ok(tau_obs is None or (r["status"] == "no_contact_by_L" and tau_obs > L) or
                 (r["status"] == "terminated_before_contact"),
                 "B2 trial %d: no contact found by the clock and none by tick L in the engine graphs" % trial)
            if r["status"] == "terminated_before_contact":
                C.ok(so.hit_cap and tau_obs is None, "B3 trial %d: termination before contact confirmed" % trial)
        # the clock run must not differ from the observed and from a plain run (prediction is read-only)
        while not st.done:
            P.tick(ieng, run, st)
        sp = P.RunState(peng, run, N, k, th0, d0, L + 1, cap, strict=True)
        plain = [P.fingerprint(sp, with_prov=False)]
        while not sp.done:
            it0 = sp.iters
            P.tick(peng, run, sp)
            if sp.iters > it0:
                plain.append(P.fingerprint(sp, with_prov=False))
        C.ok(P.fingerprint(st) == P.fingerprint(so) and plain == phys and rng_ok,
             "B6 trial %d: clock run = observed run (full state incl. provenance and orientation counters) = plain "
             "run (physical trajectory, every tick); global RNG untouched" % trial)
    say("randomized: %d trajectories, %d observed ticks" % (trials, n_ticks))
    need = list(cover) if coverage else []             # coverage is asserted on the full run (negative controls skip it)
    for key in need:
        C.ok(cover[key] > 0, "C coverage: %s (%d)" % (key, cover[key]))
    say("coverage: " + ", ".join("%s %d" % kv for kv in cover.items()))

    # ---- D. no registered input was opened
    root_files = sorted({p for p in opened if p.startswith(P.ROOT + os.sep)})
    allowed = {P.ENGINE, P.ORIENT, P.RUNNER, LIB, os.path.abspath(__file__)}

    def permitted(p):                                   # a source file, or its (attempted) bytecode cache entry
        if p in allowed:
            return True
        d, b = os.path.split(p)
        return os.path.basename(d) == "__pycache__" and any(
            os.path.dirname(d) == os.path.dirname(a) and b.startswith(os.path.splitext(os.path.basename(a))[0] + ".")
            for a in allowed)
    C.ok(all(permitted(p) for p in root_files) and not any("/upload/az-token-resonance" in p for p in opened),
         "D1 files opened inside the repository: only the pinned engine, orientation, runner, provenance library and "
         "this script (%d paths)" % len(root_files))
    say("checks: %d, failed: %d" % (C.n, C.bad))
    say("SELFTEST PASS" if C.bad == 0 else "SELFTEST FAIL")
    return 0 if C.bad == 0 else 1


def so_carrier_at(fps, ticks, t, j, so):
    """Carrier of c_j at the end of tick t in the observed run: the pre-tick carrier of tick t+1, or the final one."""
    if t < len(ticks):
        return ticks[t]["carrier"]
    return so.prov.carrier[j]


def so_done_at(ticks, t, so, cap, L):
    """Was the observed run terminal (or cap-reached) at the end of tick t?"""
    if t == len(ticks):
        return so.done and (so.hit_cap or so.iters >= so.T)
    return False


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        raise SystemExit(selftest())
    print(__doc__)
    raise SystemExit(2)
