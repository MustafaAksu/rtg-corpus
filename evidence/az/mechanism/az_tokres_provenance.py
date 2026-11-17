#!/usr/bin/env python3
"""AZ mechanism study, design section 6 - token provenance sidecar and full checkpoint/restart (synthetic stage).

[SESSION] NONCANONICAL instrument (records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md section 6, r2).
Written by the Claude AZ lane on the PI's decision of 17 Nov 2026 ("aracı sen yaz ChatGPT denetlesin"); first delivery
is synthetic only: it reads no registered record, runs no campaign and selects no fork operator.

What it is
  * Provenance (6.1): a read-only sidecar on a SEPARATE instance of the pinned engine. It wraps four module functions
    of that instance (orient_path, apply_single_edge_swap, apply_path_cycle, blow_up_star_with_snapshot); each wrapper
    calls the original exactly once with the same arguments and only observes. It records, per node, the label
    (copy id, sign) of the token it carries; per copy, its root (initial node), the root value, its parent copy and
    birth event, its sign history and its current carrier. Swaps transport labels; a path rotation uses the oriented
    path actually returned by the engine's orient_path call (no second call); a birth gives the newborn a NEW copy
    (child of the centre's pre-event copy, same sign) and flips the sign of the centre's copy, both from the pre-tick
    labels (the engine uses delta_pre). Nothing is reconstructed by value matching; the value identity
    delta[v] == sign * root_value (mod N) is only CHECKED after every tick.
    Birth provenance is a declared bookkeeping convention, not a physical identity claim.
  * Checkpoint/restart (6.2): the loop of the frozen runner az_tokres_run.run_state (75c5f139...8992) is held in a
    RunState object (Universe, alphabet, census, law counter, fe, fb, t100, M_at, TDR-26 window accumulators, cap flag,
    loop count) plus the provenance; checkpoint = copy.deepcopy at the end of a complete tick. Absolute tick (u.steps)
    is never reset; the checkpoint tick is kept as `landmark_tick`, and post-landmark tick = u.steps - landmark_tick.
    No post-landmark reset fields are defined. Serialization is not used (deepcopy only).

    python3 -I evidence/az/mechanism/az_tokres_provenance.py --selftest

Exit 0 iff every self-test check passes ("SELFTEST PASS").
"""
from __future__ import annotations

import copy
import dataclasses
import hashlib
import importlib.util
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ENGINE = os.path.join(ROOT, "upload", "tdrg-records", "genesis_mode_b_mc.py")
ORIENT = os.path.join(ROOT, "evidence", "tdrg", "scripts", "tdrg_orient_v2_12_14.py")
RUNNER = os.path.join(ROOT, "evidence", "az", "scripts", "az_tokres_run.py")
PINS = {ENGINE: "4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608",
        ORIENT: "ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c",
        RUNNER: "75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992"}
POLICY = "bound_symmetric"
FORCE_STRICT = None          # negative controls only: None = as constructed; False = guard off (to test the oracle)


# ---------------------------------------------------------------- loading
def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def check_pins():
    for p, want in PINS.items():
        got = sha256_file(p)
        if got != want:
            sys.exit("STOP: pin mismatch for %s: %s" % (os.path.relpath(p, ROOT), got))


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_engine(name):
    """A fresh instance of the pinned engine under module name `name`, with the P1 orientation (as the runner does)."""
    sys.dont_write_bytecode = True
    eng = _load(ENGINE, name)
    ori = _load(ORIENT, name + "_orient")
    eng.orient_path = ori.make_orient(eng)
    return eng


def load_runner():
    sys.dont_write_bytecode = True
    return _load(RUNNER, "az_tokres_run_frozen")


# ---------------------------------------------------------------- provenance sidecar
class Provenance:
    """Labels (copy id, sign) per node; copy table; event log. Plain data, deep-copyable."""

    def __init__(self, delta0, N):
        self.N = N
        self.copies = []                     # copy id -> dict
        self.labels = {}                     # node -> [copy id, sign]
        self.carrier = {}                    # copy id -> node
        self.sign_history = {}               # copy id -> [(tick, sign)]
        for node, x in delta0.items():
            c = len(self.copies)
            self.copies.append({"root": node, "root_value": x % N, "parent": None, "birth": None})
            self.labels[node] = [c, 1]
            self.carrier[c] = node
            self.sign_history[c] = [(0, 1)]
        self.n_roots = len(self.copies)
        self.events = []                     # (tick, kind, details)
        self._pre = None
        self._tick = 0
        self._orient_calls = 0
        self._last_raw = None
        self._last_oriented = None

    # -- tick boundary (called by the driver)
    def begin_tick(self, tick):
        self._tick = tick
        self._pre = {v: tuple(l) for v, l in self.labels.items()}

    def value(self, node):
        c, s = self.labels[node]
        return (s * self.copies[c]["root_value"]) % self.N

    # -- observed events
    def on_swap(self, a, b):
        self.labels[a], self.labels[b] = self.labels[b], self.labels[a]
        self.carrier[self.labels[a][0]] = a
        self.carrier[self.labels[b][0]] = b
        self.events.append((self._tick, "swap", (a, b)))

    def on_rotation(self, path, how):
        old = {v: self.labels[v] for v in path}
        n = len(path)
        for i, v in enumerate(path):
            self.labels[v] = old[path[(i + 1) % n]]
            self.carrier[self.labels[v][0]] = v
        self.events.append((self._tick, "path_" + how, tuple(path)))

    def on_tie(self, path):
        self.events.append((self._tick, "path_tie_bound", tuple(path)))

    def on_birth(self, centre, newborn):
        c, s = self._pre[centre]                    # pre-event provenance, as the engine uses delta_pre
        child = len(self.copies)
        self.copies.append({"root": self.copies[c]["root"], "root_value": self.copies[c]["root_value"], "parent": c,
                            "birth": {"tick": self._tick, "centre": centre, "newborn": newborn}})
        self.labels[newborn] = [child, s]
        self.carrier[child] = newborn
        self.sign_history[child] = [(self._tick, s)]
        self.labels[centre] = [c, -s]
        self.sign_history[c].append((self._tick, -s))
        self.events.append((self._tick, "birth", (centre, newborn, c, child)))

    # -- queries for later fork operators
    def descendants(self, c):
        out, frontier = [], [c]
        while frontier:
            p = frontier.pop()
            kids = [i for i, x in enumerate(self.copies) if x["parent"] == p]
            out += kids
            frontier += kids
        return sorted(out)

    def lineage(self, c):
        out = [c]
        while self.copies[out[-1]]["parent"] is not None:
            out.append(self.copies[out[-1]]["parent"])
        return out

    # -- consistency (checked, never used to assign provenance)
    def check(self, u):
        errs = []
        if set(self.labels) != set(u.delta):
            errs.append("labelled nodes differ from engine nodes")
        if sorted(l[0] for l in self.labels.values()) != list(range(len(self.copies))):
            errs.append("labels are not a bijection onto copies")
        for v, (c, s) in self.labels.items():
            if self.carrier.get(c) != v:
                errs.append("carrier of copy %d is not node %d" % (c, v))
            if v in u.delta and u.delta[v] != (s * self.copies[c]["root_value"]) % self.N:
                errs.append("value identity fails at node %d" % v)
            if s not in (1, -1) or self.sign_history[c][-1][1] != s:
                errs.append("sign history of copy %d" % c)
        errs += self.check_ledger()
        return errs

    def check_ledger(self):
        """Lineage metadata against the event log: roots, parents, birth records, full sign histories."""
        errs = []
        births = [(t, d) for t, kind, d in self.events if kind == "birth"]
        by_child = {}
        for t, (centre, newborn, parent, child) in births:
            if child in by_child:
                errs.append("two birth events for copy %d" % child)
            by_child[child] = (t, centre, newborn, parent)
        flips = {}
        for t, (centre, newborn, parent, child) in births:
            flips.setdefault(parent, []).append(t)
        for c, x in enumerate(self.copies):
            if x["parent"] is None:
                if c >= self.n_roots or x["birth"] is not None or x["root"] != c or c in by_child:
                    errs.append("root copy %d malformed" % c)
                first = (0, 1)
            else:
                p = x["parent"]
                ev = by_child.get(c)
                if c < self.n_roots or not (0 <= p < c) or ev is None:
                    errs.append("copy %d: parent or birth event missing" % c)
                    continue
                t, centre, newborn, ep = ev
                if ep != p or x["birth"] != {"tick": t, "centre": centre, "newborn": newborn}:
                    errs.append("copy %d: parent/birth record disagrees with the event log" % c)
                if x["root"] != self.copies[p]["root"] or x["root_value"] != self.copies[p]["root_value"]:
                    errs.append("copy %d: root differs from its parent's" % c)
                sp = [sg for tt, sg in self.sign_history[p] if tt < t]
                first = (t, sp[-1] if sp else None)
            h = self.sign_history.get(c, [])
            want = [first]
            for t in flips.get(c, []):
                want.append((t, -want[-1][1]))
            if h != want:
                errs.append("copy %d: sign history disagrees with the birth events" % c)
        if len(by_child) != len(self.copies) - self.n_roots:
            errs.append("birth events and non-root copies differ in number")
        return errs


def install(eng):
    """Wrap four functions of this engine instance; returns the holder whose 'prov' field activates observation."""
    holder = {"prov": None}
    o_orient, o_swap = eng.orient_path, eng.apply_single_edge_swap
    o_cycle, o_birth = eng.apply_path_cycle, eng.blow_up_star_with_snapshot

    def orient_path(path, theta, delta, N, u):
        res = o_orient(path, theta, delta, N, u)
        p = holder["prov"]
        if p is not None:
            p._orient_calls += 1
            p._last_raw, p._last_oriented = list(path), (None if res is None else list(res))
        return res

    def apply_single_edge_swap(comp, delta, u):
        before = u.single_edge_swaps
        ok = o_swap(comp, delta, u)
        p = holder["prov"]
        if p is not None and ok and u.single_edge_swaps == before + 1:
            p.on_swap(comp[0], comp[1])
        return ok

    def apply_path_cycle(comp, adj, u, bind_ties=False):
        p = holder["prov"]
        if p is not None:
            p._orient_calls, p._last_raw, p._last_oriented = 0, None, None
        before = u.path_interactions
        ok = o_cycle(comp, adj, u, bind_ties=bind_ties)
        if p is not None:
            if p._orient_calls > 1:
                raise AssertionError("orient_path called more than once in one path event")
            if u.path_interactions == before + 1:
                path = p._last_oriented
                if path is None or sorted(path) != sorted(comp):
                    raise AssertionError("rotation without a captured oriented path")
                how = "forward" if path == p._last_raw else "reversed"
                p.on_rotation(path, how)
            elif ok and p._last_raw is not None and p._last_oriented is None:
                p.on_tie(p._last_raw)
        return ok

    def blow_up_star_with_snapshot(u, center, theta_pre, delta_pre, next_id):
        ret = o_birth(u, center, theta_pre, delta_pre, next_id)
        p = holder["prov"]
        if p is not None:
            p.on_birth(center, ret - 1)
        return ret

    eng.orient_path = orient_path
    eng.apply_single_edge_swap = apply_single_edge_swap
    eng.apply_path_cycle = apply_path_cycle
    eng.blow_up_star_with_snapshot = blow_up_star_with_snapshot
    eng._az_prov_holder = holder
    return holder


# ---------------------------------------------------------------- runner state with checkpoint (loop of run_state)
class RunState:
    """Every mutable quantity of az_tokres_run.run_state, plus provenance. Deep-copyable; holds no module."""

    def __init__(self, eng, run, N, k, theta0, delta0, T, cap, tdr26=True, check_law=True, provenance=False,
                 strict=True):
        if N % 2 or not (k < N / 6):
            raise ValueError("N must be even and k < N/6")
        self.N, self.k, self.T, self.cap, self.tdr26, self.check_law = N, k, T, cap, tdr26, check_law
        self.u = eng.Universe(N=N, k=k, theta={i: t % N for i, t in enumerate(theta0)},
                              delta={i: d % N for i, d in enumerate(delta0)})
        self.alphabet = {d % N for d in delta0} | {(-d) % N for d in delta0}
        self.census = Counter(self.u.delta.values())
        self.law_viol = 0
        self.fb = self.fe = self.t100 = None
        self.m_at = {}
        self.w_n = self.w_b = 0
        self.w_occ = self.w_oims = 0.0
        self.hit_cap = False
        self.iters = 0
        self.done = False
        self.landmark_tick = None
        self.window = run.TDR26_WINDOW
        self.checkpoints = run.CHECKPOINTS
        self.prov = Provenance(self.u.delta, N) if provenance else None
        self.strict = strict if FORCE_STRICT is None else FORCE_STRICT  # fail closed: check every tick, raise


class ProvenanceError(RuntimeError):
    pass


def tick(eng, run, st):
    """One iteration of run_state's loop. Returns False once the loop has ended."""
    if st.done:
        return False
    u, N = st.u, st.N
    if st.iters >= st.T:
        st.done = True
        return False
    if st.cap > 0 and len(u.theta) >= st.cap:
        st.hit_cap, st.done = True, True
        return False
    holder = getattr(eng, "_az_prov_holder", None)
    if holder is not None:
        holder["prov"] = st.prov
        if st.prov is not None:
            st.prov.begin_tick(u.steps + 1)
    elif st.prov is not None:
        raise RuntimeError("provenance requested on an engine instance without the sidecar")
    nxt = u.steps + 1
    want_motif = st.tdr26 and (st.fb is None or nxt < st.fb + st.window)
    b0 = u.births
    ids_before = set(u.theta) if st.check_law else None
    try:
        motif = eng.step_universe(u, multistar_policy=POLICY, collect_motif=want_motif)
    finally:
        if holder is not None:
            holder["prov"] = None
    st.iters += 1
    if st.prov is not None and st.strict:
        errs = st.prov.check(u)
        if errs:
            raise ProvenanceError("tick %d: %s" % (u.steps, "; ".join(errs[:3])))
    db = u.births - b0
    if st.fe is None and (u.single_edge_swaps or u.path_interactions or u.births or u.multistar_seen
                          or u.path_ties_seen):
        st.fe = u.steps
    if st.fb is None and db:
        st.fb = u.steps
    if want_motif and st.fb is not None and motif is not None and st.fb <= u.steps < st.fb + st.window:
        st.w_n += 1
        st.w_b += int(motif.get("births_step", db))
        st.w_occ += float(motif.get("occ_clean_pairs", 0))
        st.w_oims += float(motif.get("occ_clean_pairs_in_multistar", 0))
    if st.check_law:
        v, st.census = run.law_check_tick(u, N, st.alphabet, st.census, ids_before)
        st.law_viol += v
        if len(u.theta) - len(ids_before) != db:
            st.law_viol += 1
    m = len(u.theta)
    if st.t100 is None and m >= 100:
        st.t100 = u.steps
    if u.steps in st.checkpoints:
        st.m_at[u.steps] = m
    if st.cap > 0 and m >= st.cap:
        st.hit_cap, st.done = True, True
    return not st.done


def run_to(eng, run, st, abs_tick=None):
    """Advance until u.steps == abs_tick (or the end)."""
    while (abs_tick is None or st.u.steps < abs_tick) and tick(eng, run, st):
        pass
    return st


def checkpoint(st):
    """Full checkpoint at the end of a complete tick (deep copy of every field, provenance included)."""
    c = copy.deepcopy(st)
    c.landmark_tick = st.u.steps
    return c


def result(st):
    """The output dict of run_state (same keys and values)."""
    u, N = st.u, st.N
    final = Counter(u.delta.values())
    cls = Counter()
    for y, n in final.items():
        cls[min(y % N, N - y % N)] += n
    top_a, top_n = max(cls.items(), key=lambda kv: (kv[1], -kv[0]))
    out = {"M": len(u.theta), "births": u.births, "steps": u.steps, "hit_cap": st.hit_cap, "fb": st.fb, "fe": st.fe,
           "t100": st.t100, "M_at": st.m_at, "census": sorted(final.items()), "top_class": top_a,
           "top_share": top_n / len(u.theta), "law_viol": st.law_viol if st.check_law else None,
           "swaps": u.single_edge_swaps, "paths": u.path_interactions, "path_ties": u.path_ties_seen,
           "ms_seen": u.multistar_seen, "ms_bound": u.multistar_bound, "ambiguous": u.ambiguous_events, "tdr26": None}
    if st.tdr26 and st.fb is not None:
        out["tdr26"] = {"n": st.w_n, "births": st.w_b, "occ": st.w_occ, "oims": st.w_oims,
                        "complete": st.w_n == st.window, "b_per_step": st.w_b / st.w_n if st.w_n else None,
                        "ms_abs": (st.w_oims / st.w_occ) if st.w_occ > 0 else None}
    return out


ANNOTATION_FIELDS = ("landmark_tick",)    # set only on a checkpoint copy; compared separately, never continued from


def canon(x):
    """Canonical, order-preserving representation of a state object (dataclasses, plain objects, containers)."""
    if dataclasses.is_dataclass(x) and not isinstance(x, type):
        return ("dc", type(x).__name__, tuple((f.name, canon(getattr(x, f.name))) for f in dataclasses.fields(x)))
    if isinstance(x, dict):
        return ("dict", type(x).__name__, tuple((canon(k), canon(v)) for k, v in x.items()))
    if isinstance(x, (list, tuple)):
        return (type(x).__name__, tuple(canon(v) for v in x))
    if isinstance(x, (set, frozenset)):
        return ("set", tuple(sorted(canon(v) for v in x)))
    if hasattr(x, "__dict__"):
        return ("obj", type(x).__name__, tuple((k, canon(v)) for k, v in sorted(vars(x).items())
                                             if k not in ANNOTATION_FIELDS))
    return (type(x).__name__, x)


def fingerprint(st, with_prov=True):
    """Full tick-boundary snapshot: every Universe field (dict order kept), every runner field including the
    configuration (N, k, T, cap, tdr26, check_law, window, checkpoints) and, with_prov, the whole provenance object
    (copies with parent/root/birth, labels, carriers, full sign histories, event log, scratch fields).
    Only ANNOTATION_FIELDS are excluded."""
    snap = canon(st)
    if not with_prov:
        snap = snap[:2] + (tuple(kv for kv in snap[2] if kv[0] != "prov"),)
    return snap


# ================================================================ self-test (synthetic only)
class OracleLedger:
    """Independent lineage reference for the self-test, in its own representation (separate field maps), advanced
    only by oracle_tick from the engine's pre-tick physical state. Never reads the sidecar after initialisation."""

    def __init__(self, delta0):
        self.label = {v: (v, 1) for v in delta0}            # node -> (copy, sign); root copy id = initial node id
        self.root = {v: v for v in delta0}
        self.root_value = dict(delta0)
        self.parent = {v: None for v in delta0}
        self.born = {v: None for v in delta0}
        self.signs = {v: [(0, 1)] for v in delta0}
        self.next_copy = len(delta0)

    def as_sidecar(self):
        copies = [{"root": self.root[c], "root_value": self.root_value[c], "parent": self.parent[c],
                   "birth": self.born[c]} for c in range(self.next_copy)]
        labels = {v: list(l) for v, l in self.label.items()}
        carrier = {c: v for v, (c, _) in self.label.items()}
        return copies, labels, carrier, {c: list(h) for c, h in self.signs.items()}


def oracle_tick(peng, theta, delta, led, N, k, t):
    """Independent expectation for tick t from the pre-tick engine state (theta, delta) and the oracle ledger:
    returns the expected delta and advances the ledger. Uses the engine's pure graph helpers and an own counter-free
    copy of the v2.12.14 orientation rule."""
    th = {x: (theta[x] + delta[x]) % N for x in theta}
    nodes = list(th)
    edges = peng.graph_edges_for(nodes, th, N, k)
    adj = peng.build_adj(nodes, edges)
    pre = dict(led.label)
    dl = dict(delta)
    nid = max(theta) + 1
    for comp in peng.connected_components(nodes, adj):
        ctype, centers = peng.classify_component(comp, adj)
        if ctype.startswith("star_k1c_") and len(centers) == 1:
            c = centers[0]
            cc, sg = pre[c]
            new = led.next_copy
            led.next_copy += 1
            led.root[new], led.root_value[new] = led.root[cc], led.root_value[cc]
            led.parent[new] = cc
            led.born[new] = {"tick": t, "centre": c, "newborn": nid}
            led.signs[new] = [(t, sg)]
            led.signs[cc].append((t, -sg))
            led.label[nid], led.label[c] = (new, sg), (cc, -sg)
            dl[nid], dl[c] = delta[c], (-delta[c]) % N
            nid += 1
        elif ctype == "single_edge":
            a, b = comp
            led.label[a], led.label[b] = pre[b], pre[a]
            dl[a], dl[b] = delta[b], delta[a]
        elif ctype.startswith("path_p"):
            raw = peng.raw_ordered_path(comp, adj)
            if raw is None:
                continue
            S = sum(peng.signed_defect_error(th[raw[i]], th[raw[i + 1]], N) for i in range(len(raw) - 1))
            if S > 0:
                path = raw
            elif S < 0:
                path = raw[::-1]
            else:
                e = peng.signed_centered(delta[raw[-1]] - delta[raw[0]], N)
                path = raw if 0 < e < N // 2 else raw[::-1] if e < 0 else None
            if path is None:
                continue
            for i, v in enumerate(path):
                w = path[(i + 1) % len(path)]
                led.label[v], dl[v] = pre[w], delta[w]
    return dl


class Checks:
    def __init__(self):
        self.n = self.bad = 0

    def ok(self, cond, msg):
        self.n += 1
        if not cond:
            self.bad += 1
            print("FAIL:", msg)
        elif " trial " not in msg:
            print("pass:", msg)
        return cond


def fixture_state(N, posts, deltas):
    """Initial (theta, delta) whose positions after the first advance are `posts`."""
    return [(p - d) % N for p, d in zip(posts, deltas)], [d % N for d in deltas]


def one_tick(ieng, run, N, k, posts, deltas):
    th, d = fixture_state(N, posts, deltas)
    st = RunState(ieng, run, N, k, th, d, T=1, cap=0, provenance=True)
    tick(ieng, run, st)
    return st


def selftest(trials=240):
    check_pins()
    run = load_runner()
    peng = load_engine("tdrg_engine_plain")           # never instrumented
    ieng = load_engine("tdrg_engine_instr")
    install(ieng)
    C = Checks()
    print("pins: engine 4c94d874, orientation ca59e9b9, runner 75c5f139 - OK")

    # ---- A. explicit fixtures (N = 24, k = 2; antipode 12, an edge iff the separation is 10..14)
    N, k = 24, 2
    st = one_tick(ieng, run, N, k, [0, 3, 6], [5, 7, 9])
    C.ok(st.prov.events == [] and [tuple(st.prov.labels[v]) for v in range(3)] == [(0, 1), (1, 1), (2, 1)],
         "A1 isolated nodes: no event, labels unchanged")
    st = one_tick(ieng, run, N, k, [0, 12], [5, 5])
    C.ok(st.u.delta == {0: 5, 1: 5} and st.prov.labels == {0: [1, 1], 1: [0, 1]},
         "A2 swap of EQUAL values: values unchanged, labels exchanged")
    for e_val, want in ((3, "forward"), (-3, "reversed")):
        st = one_tick(ieng, run, N, k, [0, 12, 0], [4, 9, (4 + e_val) % N])
        kinds = [x[1] for x in st.prov.events]
        if want == "forward":
            exp = {0: [1, 1], 1: [2, 1], 2: [0, 1]}
        else:
            exp = {2: [1, 1], 1: [0, 1], 0: [2, 1]}
        C.ok(kinds == ["path_" + want] and st.prov.labels == exp, "A3 P3 path, E = %+d: %s rotation" % (e_val, want))
    for e_val in (0, 12):
        st = one_tick(ieng, run, N, k, [0, 12, 0], [4, 9, (4 + e_val) % N])
        C.ok([x[1] for x in st.prov.events] == ["path_tie_bound"] and st.u.path_ties_bound == 1
             and st.prov.labels == {0: [0, 1], 1: [1, 1], 2: [2, 1]},
             "A4 balanced path tie (E = %d): bound, no rotation, labels unchanged" % e_val)
    st = one_tick(ieng, run, N, k, [0, 12, 1, 13], [3, 3, 3, 3])
    C.ok(st.u.bound_cycle_hits == 1 and st.prov.events == [], "A5 bound 4-cycle with four equal values: no event")
    for x in (0, 12, 5):
        st = one_tick(ieng, run, N, k, [0, 12, 11, 13], [x, 2, 3, 4])
        nb = 4
        good = (st.u.births == 1 and st.prov.labels[nb] == [4, 1] and st.prov.labels[0] == [0, -1]
                and st.prov.copies[4]["parent"] == 0 and st.prov.copies[4]["root"] == 0
                and st.u.delta[nb] == x % N and st.u.delta[0] == (-x) % N
                and st.prov.sign_history[0] == [(0, 1), (1, -1)] and st.prov.sign_history[4] == [(1, 1)])
        C.ok(good, "A6 birth with centre token x = %d: newborn new copy (child of the centre's copy, sign +), "
                   "centre sign flipped%s" % (x, " (flip invisible in the value)" if (2 * x) % N == 0 else ""))
    st = one_tick(ieng, run, N, k, [0, 12, 11, 13, 5, 17], [12, 2, 3, 4, 7, 7])
    kinds = sorted(x[1] for x in st.prov.events)
    C.ok(kinds == ["birth", "swap"] and st.prov.labels[6] == [6, 1] and st.prov.labels[0] == [0, -1]
         and st.prov.labels[4] == [5, 1] and st.prov.labels[5] == [4, 1] and not st.prov.check(st.u),
         "A7 simultaneous birth (x = N/2) and equal-value swap in one tick; newborn id 6")
    st = one_tick(ieng, run, N, k, [0, 12, 11, 13], [12, 2, 3, 4])
    st2 = RunState(ieng, run, N, k, *fixture_state(N, [0, 12, 11, 13], [12, 2, 3, 4]), T=1, cap=0)
    tick(ieng, run, st2)
    st2.strict = st.strict
    C.ok(fingerprint(st, with_prov=False) == fingerprint(st2, with_prov=False),
         "A8 same fixture with provenance off: identical state")

    th, d = [0, 5, 9, 14], [3, 3, 7, 11]
    st = RunState(ieng, run, 24, 2, th, d, T=50, cap=4, provenance=True)
    run_to(ieng, run, st)
    C.ok(result(st) == run.run_state(peng, 24, 2, th, d, 50, 4, POLICY) and st.u.steps == 0 and st.hit_cap,
         "A9 cap already reached at the start (M0 = 4, cap = 4): no tick, hit_cap, as run_state")

    # ---- B. randomized trajectories: oracle, on/off, restart, frozen runner
    rng = random.Random(20261117)
    cover = Counter()
    n_traj = n_ticks = 0
    for trial in range(trials):
        if trial % 3 == 0:
            N, k = 24, rng.choice([2, 3])
        elif trial % 3 == 1:
            N, k = 60, rng.choice([4, 6, 9])
        else:
            N, k = 120, 8
        m0 = rng.randint(3, 8)
        special = [0, N // 2, N // 4, 3 * N // 4]
        d0 = [rng.choice(special) if rng.random() < 0.35 else rng.randrange(N) for _ in range(m0)]
        if rng.random() < 0.5:                                     # repeated equal values
            d0[rng.randrange(m0)] = d0[rng.randrange(m0)]
        th0 = [rng.randrange(N) for _ in range(m0)]
        T, cap = rng.choice([40, 120, 220]), rng.choice([0, 60, 150])
        if len(set(d0)) < m0:
            cover["init_equal_values"] += 1

        st = RunState(ieng, run, N, k, th0, d0, T, cap, provenance=True, strict=False)
        led = OracleLedger({i: d % N for i, d in enumerate(d0)})
        fp_i = [fingerprint(st, with_prov=False)]
        orc_ok = cons_ok = True
        g_state = random.getstate()
        while not st.done:
            pre_th, pre_d = dict(st.u.theta), dict(st.u.delta)
            n_ev, it0 = len(st.prov.events), st.iters
            bc0, ms0 = st.u.bound_cycle_hits, st.u.multistar_bound
            tick(ieng, run, st)
            if st.iters == it0:                                   # loop ended without a tick
                continue
            n_ticks += 1
            exp_d = oracle_tick(peng, pre_th, pre_d, led, N, k, st.u.steps)
            copies, labels, carrier, signs = led.as_sidecar()
            if (exp_d != st.u.delta or labels != st.prov.labels or copies != st.prov.copies
                    or carrier != st.prov.carrier or signs != st.prov.sign_history):
                orc_ok = False
            if st.prov.check(st.u):
                cons_ok = False
            new = st.prov.events[n_ev:]
            for _, kind, det in new:
                cover[kind] += 1
                if kind == "swap" and pre_d[det[0]] == pre_d[det[1]]:
                    cover["swap_equal_values"] += 1
                if kind == "birth":
                    centre, _nb, pc, child = det
                    x = pre_d[centre]
                    cover["birth_x0" if x == 0 else "birth_xhalf" if x == N // 2 else "birth_other"] += 1
                    if st.prov.copies[pc]["parent"] is not None:
                        cover["birth_from_descended_copy"] += 1
                    if len(st.prov.lineage(child)) >= 4:
                        cover["lineage_depth>=4"] += 1
                    if sum(1 for v in pre_d.values() if v == x) >= 2:
                        cover["birth_centre_value_shared"] += 1
                    if pc != centre:
                        cover["birth_centre_carries_foreign_copy"] += 1
                if kind.startswith("path_") and len(det) >= 4:
                    cover["path_rotation_or_tie_n>=4"] += 1
            if len(new) >= 2:
                cover["tick_with_>=2_events"] += 1
            if st.u.bound_cycle_hits > bc0:
                cover["bound_cycle"] += 1
            if st.u.multistar_bound > ms0:
                cover["multistar_bound"] += 1
            fp_i.append(fingerprint(st, with_prov=False))
        sp = RunState(peng, run, N, k, th0, d0, T, cap, strict=False)
        fp_p = [fingerprint(sp, with_prov=False)]
        while not sp.done:
            it0 = sp.iters
            tick(peng, run, sp)
            if sp.iters > it0:
                fp_p.append(fingerprint(sp, with_prov=False))
        C.ok(orc_ok, "B1 trial %d: values, labels, carriers, whole copy table (root, parent, birth) and full sign "
                     "histories equal the independent oracle ledger at every tick" % trial)
        C.ok(cons_ok, "B2 trial %d: value identity, bijection, carriers and the ledger check hold at every tick" % trial)
        C.ok(fp_i == fp_p, "B3 trial %d: instrumented and plain engine: identical full state at every tick" % trial)
        C.ok(random.getstate() == g_state, "B4 trial %d: global random state untouched" % trial)
        ref = run.run_state(peng, N, k, th0, d0, T, cap, POLICY)
        C.ok(result(st) == ref and result(sp) == ref,
             "B5 trial %d: result equals the frozen runner's run_state (instrumented and plain)" % trial)

        # restart at up to three tick boundaries; full snapshots compared (only landmark_tick excluded, checked apart)
        end = st.u.steps
        for c in sorted({1, max(1, end // 2), rng.randint(1, max(1, end))}):
            if c > end:
                continue
            for eng_, prov_, whole in ((ieng, True, st), (peng, False, sp)):
                a = RunState(eng_, run, N, k, th0, d0, T, cap, provenance=prov_, strict=False)
                run_to(eng_, run, a, c)
                cp = checkpoint(a)
                cp_fp = fingerprint(cp)
                same_at_boundary = cp_fp == fingerprint(a) and a.landmark_tick is None and cp.landmark_tick == c
                trail_a, trail_b = [], []
                while not a.done:
                    tick(eng_, run, a)
                    trail_a.append(fingerprint(a))
                C.ok(fingerprint(cp) == cp_fp and same_at_boundary,
                     "B6 trial %d c=%d: checkpoint equals the live state at the boundary (landmark_tick apart) and is "
                     "unaffected by continuing the original" % (trial, c))
                b = copy.deepcopy(cp)
                while not b.done:
                    tick(eng_, run, b)
                    trail_b.append(fingerprint(b))
                C.ok(trail_a == trail_b and result(a) == result(b) == ref and b.landmark_tick == c
                     and b.u.steps - b.landmark_tick == end - c,
                     "B7 trial %d c=%d %s: restarted trajectory equals the uninterrupted one in full snapshot at every "
                     "tick; absolute tick kept" % (trial, c, "instr" if prov_ else "plain"))
                C.ok(fingerprint(b) == fingerprint(a) == fingerprint(whole),
                     "B8 trial %d c=%d %s: final full snapshot (provenance included) equals the uninterrupted run"
                     % (trial, c, "instr" if prov_ else "plain"))
        n_traj += 1

    print("randomized: %d trajectories, %d ticks; B1-B5 per trajectory, B6-B8 per restart point (failures listed above)"
          % (n_traj, n_ticks))
    need = ["swap", "swap_equal_values", "path_forward", "path_reversed", "path_tie_bound", "path_rotation_or_tie_n>=4",
            "bound_cycle", "multistar_bound", "birth", "birth_x0", "birth_xhalf", "birth_other",
            "birth_from_descended_copy", "birth_centre_carries_foreign_copy", "birth_centre_value_shared",
            "lineage_depth>=4", "tick_with_>=2_events", "init_equal_values"]
    for key in need:
        C.ok(cover[key] > 0, "C coverage: %s occurs (%d)" % (key, cover[key]))
    print("coverage:", ", ".join("%s %d" % (key, cover[key]) for key in need))

    # ---- D. negative checks: the consistency check and the orientation guard do detect faults
    st = one_tick(ieng, run, 24, 2, [0, 12], [5, 6])
    bad = copy.deepcopy(st)
    bad.prov.labels[0], bad.prov.labels[1] = bad.prov.labels[1], bad.prov.labels[0]
    C.ok(bool(bad.prov.check(bad.u)), "D1 a wrong permutation of distinct values is detected by the value identity")
    st = one_tick(ieng, run, 24, 2, [0, 12, 11, 13], [0, 2, 3, 4])
    bad = copy.deepcopy(st)
    bad.prov.labels[0][1] = 1
    C.ok(bool(bad.prov.check(bad.u)), "D2 an unflipped centre sign with x = 0 is detected (sign history)")
    bad = copy.deepcopy(st)
    bad.prov.sign_history[0] = bad.prov.sign_history[0][-1:]
    C.ok(bool(bad.prov.check(bad.u)), "D2b centre's early sign history dropped, last entry kept: detected")
    try:
        tick(peng, run, RunState(peng, run, 24, 2, [0], [0], 1, 0, provenance=True))
        C.ok(False, "D3 provenance on the plain engine is refused")
    except RuntimeError:
        C.ok(True, "D3 provenance on the plain engine is refused")

    # a synthetic trajectory with several generations of births, for the ledger checks D4-D8
    rng2 = random.Random(7)
    deep = []
    for _attempt in range(200):                      # bounded search (a faulty instrument may never produce one)
        d0 = [rng2.randrange(24) for _ in range(6)]
        th0 = [rng2.randrange(24) for _ in range(6)]
        base = run_to(ieng, run, RunState(ieng, run, 24, 2, th0, d0, 60, 80, provenance=True))
        deep = [c for c in range(len(base.prov.copies)) if len(base.prov.lineage(c)) >= 3]
        if deep:
            break
    if not deep:
        C.ok(False, "D4a no synthetic trajectory with a lineage of depth 3 found in 200 attempts")
        print("checks: %d, failed: %d" % (C.n, C.bad))
        print("SELFTEST FAIL")
        return 1
    child = deep[-1]
    par = base.prov.copies[child]["parent"]
    alt = [c for c in range(len(base.prov.copies)) if c not in (child, par)
           and base.prov.copies[c]["root_value"] == base.prov.copies[child]["root_value"]
           and base.prov.copies[c]["root"] == base.prov.copies[child]["root"] and c < child]
    C.ok(not base.prov.check(base.u) and bool(alt),
         "D4a ledger fixture: copy %d of depth %d, an alternative parent with the same root and root value exists"
         % (child, len(base.prov.lineage(child))))
    bad = copy.deepcopy(base)
    bad.prov.copies[child]["parent"] = alt[0]
    C.ok(bool(bad.prov.check(bad.u)) and bad.prov.descendants(par) != base.prov.descendants(par),
         "D4 parent redirected to another copy with the same root and value (labels and engine unchanged): detected")
    bad = copy.deepcopy(base)
    bad.prov.copies[child]["birth"] = dict(bad.prov.copies[child]["birth"], tick=bad.prov.copies[child]["birth"]["tick"] - 1)
    C.ok(bool(bad.prov.check(bad.u)), "D5 birth record with a wrong tick: detected")
    flipped = [c for c, h in base.prov.sign_history.items() if len(h) >= 3]
    bad = copy.deepcopy(base)
    c0 = flipped[0] if flipped else par
    bad.prov.sign_history[c0] = bad.prov.sign_history[c0][-1:]
    C.ok(bool(bad.prov.check(bad.u)), "D6 early sign-history entries dropped, last kept (copy %d): detected" % c0)
    bad = copy.deepcopy(base)
    bad.T, bad.done = bad.T + 5, False
    bad.prov.copies[child]["parent"] = alt[0]
    try:
        tick(ieng, run, bad)
        C.ok(False, "D7 strict mode raises at the next tick on a corrupted ledger")
    except ProvenanceError:
        C.ok(True, "D7 strict mode raises at the next tick on a corrupted ledger")
    other = copy.deepcopy(base)
    other.checkpoints = tuple(other.checkpoints) + (10 ** 6,)
    C.ok(result(other) == result(base) and fingerprint(other) != fingerprint(base),
         "D8 a changed continuation field (checkpoint grid) with unchanged outputs: the full snapshot differs")
    other = copy.deepcopy(base)
    other.landmark_tick = 17
    C.ok(fingerprint(other) == fingerprint(base), "D9 landmark_tick alone is excluded from the snapshot (annotation)")

    print("checks: %d, failed: %d" % (C.n, C.bad))
    print("SELFTEST PASS" if C.bad == 0 else "SELFTEST FAIL")
    return 0 if C.bad == 0 else 1


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        raise SystemExit(selftest())
    print(__doc__)
    raise SystemExit(2)
