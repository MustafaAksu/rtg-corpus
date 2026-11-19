#!/usr/bin/env python3
"""AZ mechanism study, fork design sections 3-5 - matched R/D operator, intervention epoch, H continuation (synthetic).

[SESSION] NONCANONICAL instrument; second Gate I deliverable of records/az/AZ_TOKEN_RESONANCE_FORK_DESIGN.md r2
(PR #322, head 08ef706, Gate D PASS 5960841961). PI, 19 Nov 2026, 23:28 +03:00: "sıradaki adım önerin uygun .
uygulayalım." (the proposal: R/D operator - absolute write, O1 only -, intervention epoch in the ledger, H-tick
continuation, post-fork alphabet and census; synthetic tests only). Parameters as recorded in PR #322 comment
7008416095 (source-reported PI decision). Written by the Claude AZ lane; reviewed by ChatGPT. It reads no registered
record and runs no campaign; the BASE pilot for the final L is not part of it.

Operator and boundary accounting (design 3-5)
  * Boundary: a C- or C+ state from az_tokres_contact_clock.contact_clock (deep checkpoint, eligible).
  * Each arm starts from its own deep copy of the SAME boundary; the boundary itself is never modified.
  * Target: v_s = carrier_s(c_j), the current carrier of the original slot copy (after a slot-copy birth: the
    centre, by the 6.1 convention). Absolute write delta[v_s] <- x_a, x_R = r, x_D = (r + eps) mod N, O1 only:
    r in {0, N/2}, eps in {-1, +1}, drawn before any prefix (az_tokres_run.arm_choices law: r1, s1).
  * No tick, advance, birth, swap or counter change is injected. Absolute clocks (u.steps, iters, fe, fb, t100,
    M_at, TDR-26 window) and every Universe history field are kept.
  * Intervention epoch (ledger): the replaced copy is RETIRED (kept, with its birth ancestry and descendants
    untouched); a NEW value-origin copy (parent None, root = itself, root value x, sign +1) is created at the same
    carrier, with an explicit 'intervention' link to the retired copy and its own event in the log. Later births
    from that carrier descend from the new copy under the unchanged birth convention.
  * Census reset to Counter(delta after the write); common post-fork alphabet S_* = S_BASE U {+-r, +-d} (both
    arms); configuration boundary T_fork = iters + H. The BASE reference arm (no write) keeps S_BASE.
  * Endpoint Y_{H,q} = 1{M at the stop >= q} (M is non-decreasing: the engine never removes nodes); secondary
    G = M_stop - M_s; h_stop = u.steps - s.

    python3 -I evidence/az/mechanism/az_tokres_fork.py --selftest

Exit 0 iff every self-test check passes ("SELFTEST PASS").
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import az_tokres_contact_clock as K                                  # noqa: E402  (installs the audit hook first)

import copy                                                          # noqa: E402
import random                                                        # noqa: E402
from collections import Counter                                      # noqa: E402

P = K.P
CLOCK = os.path.join(HERE, "az_tokres_contact_clock.py")
CLOCK_SHA = "4cdd9a7d66d3ddc083b0e45f699ffe743b35d69463b09c7aa34541f08df48eee"    # PR #328 r2 (c73dc6a)
SYNTH_TAG = "AZ-FORK-OPERATOR-SYNTH"         # synthetic seeds only
REGISTERED_PREFIX = "AZ-TOKRES"              # registered campaign tags start with this; refused


def check_pins():
    K.check_pins()
    if P.sha256_file(CLOCK) != CLOCK_SHA:
        sys.exit("STOP: pin mismatch for az_tokres_contact_clock.py")


# ---------------------------------------------------------------- provenance with intervention epochs
class ForkProvenance(P.Provenance):
    """Provenance plus intervention epochs: retired copies and intervention value origins."""

    @classmethod
    def from_provenance(cls, prov):
        fp = cls.__new__(cls)
        fp.__dict__ = copy.deepcopy(prov.__dict__)
        return fp

    def intervene(self, v, x, tick, arm):
        c_old, _ = self.labels[v]
        old_val = self.value(v)
        c_new = len(self.copies)
        x %= self.N
        self.copies.append({"root": c_new, "root_value": x, "parent": None, "birth": None,
                            "intervention": {"tick": tick, "carrier": v, "replaces": c_old, "old_value": old_val,
                                             "new_value": x, "arm": arm}})
        self.copies[c_old]["retired"] = {"tick": tick, "by": c_new}
        self.labels[v] = [c_new, 1]
        del self.carrier[c_old]
        self.carrier[c_new] = v
        self.sign_history[c_new] = [(tick, 1)]
        self.events.append((tick, "intervention", (v, c_old, c_new, old_val, x)))
        return c_old, c_new, old_val

    def active(self):
        return [c for c, x in enumerate(self.copies) if "retired" not in x]

    def check(self, u):
        errs = []
        if set(self.labels) != set(u.delta):
            errs.append("labelled nodes differ from engine nodes")
        if sorted(l[0] for l in self.labels.values()) != self.active():
            errs.append("labels are not a bijection onto the active copies")
        if sorted(self.carrier) != self.active():
            errs.append("carrier map is not exactly the active copies")
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
        errs = []
        births = [(t, d) for t, kind, d in self.events if kind == "birth"]
        ivs = [(t, d) for t, kind, d in self.events if kind == "intervention"]
        by_child, flips = {}, {}
        for t, (centre, newborn, parent, child) in births:
            if child in by_child:
                errs.append("two birth events for copy %d" % child)
            by_child[child] = (t, centre, newborn, parent)
            flips.setdefault(parent, []).append(t)
        by_origin = {}
        for t, (v, c_old, c_new, old_val, x) in ivs:
            if c_new in by_origin:
                errs.append("two intervention events for copy %d" % c_new)
            by_origin[c_new] = (t, v, c_old, old_val, x)
        for c, x in enumerate(self.copies):
            if x["parent"] is None and "intervention" not in x:              # initial root
                if c >= self.n_roots or x["birth"] is not None or x["root"] != c or c in by_child or c in by_origin:
                    errs.append("root copy %d malformed" % c)
                first = (0, 1)
            elif x["parent"] is None:                                          # intervention value origin
                ev = by_origin.get(c)
                iv = x["intervention"]
                if (ev is None or c < self.n_roots or x["birth"] is not None or x["root"] != c or c in by_child
                        or ev != (iv["tick"], iv["carrier"], iv["replaces"], iv["old_value"], iv["new_value"])
                        or x["root_value"] != iv["new_value"] or not (0 <= iv["replaces"] < c)
                        or self.copies[iv["replaces"]].get("retired") != {"tick": iv["tick"], "by": c}):
                    errs.append("intervention origin %d malformed or not matching its event" % c)
                first = (iv["tick"], 1) if ev else (None, None)
            else:                                                              # birth child
                p = x["parent"]
                ev = by_child.get(c)
                if c < self.n_roots or not (0 <= p < c) or ev is None or "intervention" in x:
                    errs.append("copy %d: parent or birth event missing" % c)
                    continue
                t, centre, newborn, ep = ev
                if ep != p or x["birth"] != {"tick": t, "centre": centre, "newborn": newborn}:
                    errs.append("copy %d: parent/birth record disagrees with the event log" % c)
                if x["root"] != self.copies[p]["root"] or x["root_value"] != self.copies[p]["root_value"]:
                    errs.append("copy %d: root differs from its parent's" % c)
                rp = self.copies[p].get("retired")
                if rp is not None and t > rp["tick"]:
                    errs.append("copy %d born from copy %d after its retirement" % (c, p))
                sp = [sg for tt, sg in self.sign_history[p] if tt < t]
                first = (t, sp[-1] if sp else None)
            h = self.sign_history.get(c, [])
            want = [first]
            for t in flips.get(c, []):
                want.append((t, -want[-1][1]))
            if h != want:
                errs.append("copy %d: sign history disagrees with the birth events" % c)
            r = x.get("retired")
            if r is not None and (r["by"] not in by_origin or by_origin[r["by"]][2] != c):
                errs.append("copy %d: retirement without a matching intervention" % c)
        if len(by_child) != sum(1 for x in self.copies if x["parent"] is not None):
            errs.append("birth events and birth children differ in number")
        if len(by_origin) != sum(1 for x in self.copies if "intervention" in x):
            errs.append("intervention events and intervention origins differ in number")
        return errs


# ---------------------------------------------------------------- operator, fork, continuation, endpoint
LANDMARKS = ("C-", "C+")
ARMS = ("R", "D", "BASE")


def _is_int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def o1_values(ch, N):
    """O1 values of a draw (az_tokres_run.arm_choices law): x_R = r1, x_D = (r1 + s1) mod N. Validated: N even,
    r1 in {0, N/2}, s1 in {-1, +1}; anything else is refused (only the PI-selected O1 family is supported)."""
    if not (_is_int(N) and N > 0 and N % 2 == 0):
        raise ValueError("N must be a positive even integer")
    r, e = ch.get("r1"), ch.get("s1")
    if not (_is_int(r) and r in (0, N // 2)) or not (_is_int(e) and e in (1, -1)):
        raise ValueError("O1 needs r1 in {0, N/2} and s1 in {-1, +1}")
    return {"R": r, "D": (r + e) % N}


def check_values(values, N):
    """The R/D value pair must be an O1 pair: R in {0, N/2}, D = (R + eps) mod N with eps = +-1."""
    if not isinstance(values, dict) or set(values) != {"R", "D"}:
        raise ValueError("values must be exactly {'R': x_R, 'D': x_D}")
    r, d = values["R"], values["D"]
    if not (_is_int(r) and r in (0, N // 2)) or not (_is_int(d) and d in ((r + 1) % N, (r - 1) % N)):
        raise ValueError("values outside the O1 family")
    return (d - r) % N == 1 and 1 or -1


def check_boundary(boundary, j, landmark, tau_C):
    """A complete, eligible, provenance-bearing BASE contact boundary whose annotation matches the fork tick."""
    if landmark not in LANDMARKS:
        raise ValueError("landmark must be C- or C+")
    if not (_is_int(tau_C) and tau_C >= 1):
        raise ValueError("tau_C must be a positive integer")
    want = tau_C - 1 if landmark == "C-" else tau_C
    if hasattr(boundary, "fork") or boundary.prov is None or isinstance(boundary.prov, ForkProvenance) \
            or any(kd == "intervention" for _, kd, _ in boundary.prov.events):
        raise ValueError("boundary is not a BASE prefix state with provenance")
    if not (_is_int(boundary.landmark_tick) and boundary.landmark_tick == boundary.u.steps == want):
        raise ValueError("boundary annotation does not match the %s fork tick %d" % (landmark, want))
    if not (_is_int(j) and 0 <= j < boundary.prov.n_roots and j in boundary.prov.carrier):
        raise ValueError("j is not an active initial root copy")
    if not K.eligible(boundary):
        raise ValueError("boundary state not eligible")


def fork(boundary, j, arm, values, H, landmark, *, tau_C):
    """A new RunState: deep copy of `boundary`, absolute O1 write for arm R or D (none for BASE), configuration
    boundary T = iters + H. Every argument is validated; `boundary` is not modified."""
    if arm not in ARMS:
        raise ValueError("arm must be R, D or BASE")
    if not (_is_int(H) and H >= 1):
        raise ValueError("H must be a positive integer")
    check_values(values, boundary.N)
    check_boundary(boundary, j, landmark, tau_C)
    return _apply(boundary, j, arm, None if arm == "BASE" else values[arm], values, H, landmark)


def _apply(boundary, j, arm, x, values, H, landmark):
    """The fork itself, after validation (also used directly by the metamorphic self-tests)."""
    st = copy.deepcopy(boundary)
    s, N = st.u.steps, st.N
    v = st.prov.carrier[j]
    info = {"arm": arm, "landmark": landmark, "s": s, "H": H, "target": v, "old_value": st.u.delta[v],
            "x": None, "noop": None, "M_s": len(st.u.theta)}
    if x is not None:
        x %= N
        st.u.delta[v] = x
        st.prov = ForkProvenance.from_provenance(st.prov)
        st.prov.intervene(v, x, s, arm)
        st.census = Counter(st.u.delta.values())
        r, d = values["R"] % N, values["D"] % N
        st.alphabet = set(st.alphabet) | {r, (-r) % N, d, (-d) % N}
        info.update(x=x, noop=info["old_value"] == x)
    st.T = st.iters + H
    st.fork = info
    return st


def continue_fork(eng, run, st):
    P.run_to(eng, run, st)
    return st


def endpoint(st, q):
    """Y_{H,q}, G, h_stop and the stop reason of a COMPLETED fork continuation. Refused (ValueError) for an
    unfinished run, an h_stop outside [0, H], a stop that is neither the horizon nor a cap stop, or a positive
    cap below q (a cap-stopped run would then be censored)."""
    if not (_is_int(q) and q >= 1):
        raise ValueError("q must be a positive integer")
    f = getattr(st, "fork", None)
    if f is None or not st.done:
        raise ValueError("endpoint of an unfinished or non-fork run")
    H, h = f["H"], st.u.steps - f["s"]
    m = len(st.u.theta)
    if not 0 <= h <= H or st.T - (st.iters - h) != H:
        raise ValueError("h_stop or the configuration boundary is inconsistent")
    if st.cap > 0 and st.cap < q:
        raise ValueError("positive cap below q")
    if st.hit_cap:
        if not (st.cap > 0 and m >= st.cap):
            raise ValueError("cap stop without a reached cap")
        reason = "cap"
    elif h == H and st.iters == st.T:
        reason = "horizon"
    else:
        raise ValueError("run stopped neither at H nor at the cap")
    return {"Y": int(m >= q), "G": m - f["M_s"], "M": m, "h_stop": h, "hit_cap": st.hit_cap, "stop": reason}


# ================================================================ self-test (synthetic only)
class ForkOracle(P.OracleLedger):
    """Independent ledger extended with intervention epochs (own representation)."""

    def __init__(self, delta0):
        super().__init__(delta0)
        self.retired, self.origin = {}, {}

    def intervene(self, v, x, tick, arm, old_val):
        c_old, _ = self.label[v]
        c = self.next_copy
        self.next_copy += 1
        self.root[c], self.root_value[c], self.parent[c], self.born[c] = c, x, None, None
        self.origin[c] = {"tick": tick, "carrier": v, "replaces": c_old, "old_value": old_val, "new_value": x,
                          "arm": arm}
        self.retired[c_old] = {"tick": tick, "by": c}
        self.signs[c] = [(tick, 1)]
        self.label[v] = (c, 1)

    def as_sidecar(self):
        copies, labels, carrier, signs = super().as_sidecar()
        for c, x in enumerate(copies):
            if c in self.origin:
                x["intervention"] = dict(self.origin[c])
            if c in self.retired:
                x["retired"] = dict(self.retired[c])
        return copies, labels, carrier, signs


def drive(eng, run, peng, st, led, N, k, check_every=True):
    """Continue st to its end, advancing the oracle ledger; returns (ok_oracle, ok_check, monotone)."""
    ok_o = ok_c = mono = True
    m_prev = len(st.u.theta)
    while not st.done:
        pre_th, pre_d, it0 = dict(st.u.theta), dict(st.u.delta), st.iters
        try:
            P.tick(eng, run, st)
        except P.ProvenanceError:
            return False, False, mono
        if st.iters == it0:
            break
        exp_d = P.oracle_tick(peng, pre_th, pre_d, led, N, k, st.u.steps)
        copies, labels, carrier, signs = led.as_sidecar()
        if (exp_d != st.u.delta or labels != st.prov.labels or copies != st.prov.copies
                or carrier != st.prov.carrier or signs != st.prov.sign_history):
            ok_o = False
        if check_every and st.prov.check(st.u):
            ok_c = False
        m = len(st.u.theta)
        mono &= m >= m_prev
        m_prev = m
    return ok_o, ok_c, mono


def selftest(trials=300, verbose=True, coverage=True):
    check_pins()
    if SYNTH_TAG.startswith(REGISTERED_PREFIX):
        sys.exit("STOP: synthetic tag collides with a registered tag")
    run = P.load_runner()
    peng = P.load_engine("frk_engine_plain")
    ieng = P.load_engine("frk_engine_instr")
    P.install(ieng)
    C = P.Checks()
    say = print if verbose else (lambda *a: None)
    say("pins: engine 4c94d874, orientation ca59e9b9, runner 75c5f139, provenance 5d5ca8ac, clock 4cdd9a7d - OK")

    def base_with_oracle(N, k, th0, d0, j, L, cap):
        """Contact clock on one run; an oracle ledger replayed from tick 0 to each boundary on a second run."""
        st = P.RunState(ieng, run, N, k, th0, d0, L + 1, cap, provenance=True, strict=True)
        r = K.contact_clock(peng, ieng, run, st, j, L)
        return r

    def oracle_at(N, k, th0, d0, L, cap, s):
        """An oracle ledger advanced through the BASE prefix to tick s, and the replayed state (must equal C-/C+)."""
        st = P.RunState(ieng, run, N, k, th0, d0, L + 1, cap, provenance=True, strict=True)
        led = ForkOracle({i: x % N for i, x in enumerate(d0)})
        ok = True
        while st.u.steps < s:
            pre_th, pre_d = dict(st.u.theta), dict(st.u.delta)
            P.tick(ieng, run, st)
            exp_d = P.oracle_tick(peng, pre_th, pre_d, led, N, k, st.u.steps)
            copies, labels, carrier, signs = led.as_sidecar()
            ok &= (exp_d == st.u.delta and labels == st.prov.labels and copies == st.prov.copies)
        return led, st, ok

    def physical_except_delta(a, b):
        fa = [(f.name, getattr(a.u, f.name)) for f in P.dataclasses.fields(a.u) if f.name != "delta"]
        fb = [(f.name, getattr(b.u, f.name)) for f in P.dataclasses.fields(b.u) if f.name != "delta"]
        return P.canon(fa) == P.canon(fb)

    def phys(st):
        """Physical and runner outcome of a finished continuation, without arm labels and provenance."""
        return (P.canon(st.u), st.fb, st.fe, st.t100, sorted(st.m_at.items()), st.w_n, st.w_b, st.w_occ, st.w_oims,
                st.law_viol, st.hit_cap, st.iters, st.T, st.done)

    def runner_clocks(st):
        return (st.fb, st.fe, st.t100, sorted(st.m_at.items()), st.w_n, st.w_b, st.w_occ, st.w_oims, st.law_viol,
                st.hit_cap, st.iters, st.u.steps, st.N, st.k, st.cap, st.tdr26, st.check_law, st.window,
                st.checkpoints, st.strict)

    def full_case(N, k, th0, d0, j, ch, L, cap, H, q, cover, label):
        """All B checks for one seed; returns number of boundaries processed."""
        vals = o1_values(ch, N)
        r = base_with_oracle(N, k, th0, d0, j, L, cap)
        if r["status"] != "contact":
            cover[r["status"]] += 1
            return 0
        n = 0
        for lm, bnd, elig in (("C-", r["minus"], r["eligible_minus"]), ("C+", r["plus"], r["eligible_plus"])):
            if not elig:
                cover["ineligible_" + lm] += 1
                continue
            n += 1
            fp_b = P.fingerprint(bnd)
            s = bnd.u.steps
            led0, rep, rep_ok = oracle_at(N, k, th0, d0, L, cap, s)
            C.ok(rep_ok and P.fingerprint(rep) == fp_b,
                 "B0 %s %s: oracle-replayed BASE prefix equals the %s boundary" % (label, lm, lm))
            arms = {}
            for arm in ("R", "D", "BASE"):
                st = fork(bnd, j, arm, vals, H, lm, tau_C=r["tau_C"])
                arms[arm] = st
                pre = copy.deepcopy(bnd)
                C.ok(physical_except_delta(st, pre) and runner_clocks(st) == runner_clocks(pre)
                     and st.T - st.iters == H and st.u.steps == s and st.iters == pre.iters
                     and all(st.u.delta[x] == pre.u.delta[x] for x in pre.u.delta if x != st.fork["target"]),
                     "B1 trial %s %s %s: only the target token changes; clocks, histories and steps kept; "
                     "T - iters = H" % (label, lm, arm))
                if arm != "BASE":
                    v = st.fork["target"]
                    C.ok(st.u.delta[v] == vals[arm] and v == rep.prov.carrier[j] and not st.prov.check(st.u)
                         and st.census == Counter(st.u.delta.values())
                         and st.alphabet == set(bnd.alphabet) | {vals["R"], (-vals["R"]) % N, vals["D"],
                                                                 (-vals["D"]) % N},
                         "B2 trial %s %s %s: written value x, target = carrier of c_j, ledger check passes, census "
                         "reset, common alphabet S_*" % (label, lm, arm))
                    cover["noop_arm"] += bool(st.fork["noop"])
                    cover["target_not_j"] += v != j
                    cover["sign_invisible_x"] += (2 * vals[arm]) % N == 0
            C.ok(P.fingerprint(bnd) == fp_b, "B3 trial %s %s: boundary unchanged by forking" % (label, lm))
            res = {}
            for arm, st in arms.items():
                led = copy.deepcopy(led0)
                if arm != "BASE":
                    led.intervene(st.fork["target"], vals[arm], s, arm, st.fork["old_value"])
                    c, l, ca, sg = led.as_sidecar()
                    C.ok(c == st.prov.copies and l == st.prov.labels and ca == st.prov.carrier
                         and sg == st.prov.sign_history,
                         "B4 trial %s %s %s: intervention epoch equals the oracle ledger" % (label, lm, arm))
                lv0 = st.law_viol
                mid = copy.deepcopy(st)
                ok_o, ok_c, mono = drive(ieng, run, peng, st, led, N, k)
                C.ok(ok_o and ok_c, "B5 trial %s %s %s: every continuation tick equals the oracle ledger; ledger "
                                    "check holds" % (label, lm, arm))
                e = endpoint(st, q)
                C.ok(mono and st.law_viol == lv0 and e["h_stop"] <= H and (e["h_stop"] == H or st.hit_cap)
                     and (not st.hit_cap or cap < q or e["Y"] == 1),
                     "B6 trial %s %s %s: M non-decreasing, no new law violation under S_*, stop at H or cap, "
                     "cap >= q implies Y = 1" % (label, lm, arm))
                hh = random.Random(run.derive_int(SYNTH_TAG, label, lm, arm)).randint(1, max(1, e["h_stop"]))
                P.run_to(ieng, run, mid, s + hh)
                cp = P.checkpoint(mid)
                P.run_to(ieng, run, cp)
                C.ok(P.fingerprint(cp) == P.fingerprint(st), "B7 trial %s %s %s: restart inside the continuation "
                                                             "(h = %d) equals the uninterrupted one" % (label, lm, arm, hh))
                res[arm] = (e, P.fingerprint(st))
                cover["cap_hit"] += st.hit_cap
                cover["birth_after_intervention"] += arm != "BASE" and any(
                    kd == "birth" and t > s and st.prov.copies[d[3]]["root"] >= st.prov.n_roots
                    for t, kd, d in st.prov.events)
                cover["descendants_of_retired"] += arm != "BASE" and bool(
                    st.prov.descendants(st.prov.events[[kd for _, kd, _ in st.prov.events].index("intervention")][2][1]))
            again = fork(bnd, j, "R", vals, H, lm, tau_C=r["tau_C"])
            continue_fork(ieng, run, again)
            C.ok(P.fingerprint(again) == res["R"][1], "B8 trial %s %s: R rerun after D and BASE gives the same "
                                                      "result (independent deep copies)" % (label, lm))
            ref = run.run_state(peng, N, k, th0, d0, s + H, cap, P.POLICY)
            C.ok(P.result(arms["BASE"]) == ref, "B9 trial %s %s: BASE reference arm = BASE run_state to tick s + H"
                 % (label, lm))
            if s == 0:
                for arm, name in (("R", "O1R"), ("D", "O1D")):
                    tha, da = run.arm_state(name, th0, d0, ch, N)
                    C.ok(P.result(arms[arm]) == run.run_state(peng, N, k, tha, da, H, cap, P.POLICY),
                         "B10 trial %s %s: s = 0 fork result = run_state(arm_state(%s)) over H" % (label, arm, name))
                cover["s0_identity"] += 1
            if lm == "C-":
                for arm in ("R", "D"):
                    st2 = fork(bnd, j, arm, vals, H, lm, tau_C=r["tau_C"])
                    _, _, edges = K.predicted_graph(peng, st2)
                    cover["contact_removed_by_write"] += not any(st2.fork["target"] in ed for ed in edges)
            # R3 metamorphic relations (validated values; _apply used only to build the relabelled arms)
            fin = {a: arms[a] for a in arms}
            eqR = continue_fork(ieng, run, _apply(bnd, j, "R", vals["R"], vals, H, lm))
            eqD = continue_fork(ieng, run, _apply(bnd, j, "D", vals["R"], vals, H, lm))
            C.ok(phys(eqR) == phys(eqD) == phys(fin["R"]) and endpoint(eqR, q) == endpoint(eqD, q),
                 "M1 trial %s %s: I_R = I_D (both write x_R): identical physical and runner continuations and "
                 "endpoints" % (label, lm))
            swR = continue_fork(ieng, run, _apply(bnd, j, "R", vals["D"], vals, H, lm))
            swD = continue_fork(ieng, run, _apply(bnd, j, "D", vals["R"], vals, H, lm))
            C.ok(phys(swR) == phys(fin["D"]) and phys(swD) == phys(fin["R"])
                 and endpoint(swR, q) == res["D"][0] and endpoint(swD, q) == res["R"][0],
                 "M3 trial %s %s: swapping the R/D assignments only swaps the paired outcomes" % (label, lm))
            for a in ("R", "D"):
                if fin[a].fork["noop"]:
                    C.ok(phys(fin[a]) == phys(fin["BASE"]) and res[a][0] == res["BASE"][0],
                         "M2 trial %s %s %s: a physical no-op write reproduces the BASE continuation and endpoint"
                         % (label, lm, a))
                    cover["M2_noop_" + lm] += 1
            cover["Y_differs"] += res["R"][0]["Y"] != res["D"][0]["Y"]
            cover["already_positive_at_boundary"] += len(bnd.u.theta) >= q
            cover["fork_" + lm] += 1
            cover["slot_birth_before_Cplus"] += lm == "C+" and bool(r["slot_birth_at_contact"])
        return n

    # ---- A. explicit fixtures (N = 24, k = 2)
    def section_a():
        N, k = 24, 2
        th, d = P.fixture_state(N, [0, 12], [5, 7])
        r = base_with_oracle(N, k, th, d, 0, 40, 0)
        ch = {"slot": 0, "r1": 12, "s1": -1}
        vals = o1_values(ch, N)
        stR = fork(r["minus"], 0, "R", vals, 30, "C-", tau_C=r["tau_C"])
        C.ok(r["minus"].u.steps == 0 and (list(stR.u.theta.values()), list(stR.u.delta.values()))
             == tuple(run.arm_state("O1R", th, d, ch, N)) and stR.u.delta[0] == 12,
             "A1 s = 0 (contact at tick 1, C-): the absolute write equals arm_state('O1R') per seed")
        continue_fork(ieng, run, stR)
        C.ok(P.result(stR) == run.run_state(peng, N, k, *run.arm_state("O1R", th, d, ch, N), 30, 0, P.POLICY),
             "A2 s = 0: the R continuation over H = 30 equals run_state on the arm_state initial values")
        th, d = P.fixture_state(N, [0, 12, 11, 13], [5, 2, 3, 4])
        r = base_with_oracle(N, k, th, d, 0, 40, 0)
        stD = fork(r["plus"], 0, "D", vals, 20, "C+", tau_C=r["tau_C"])
        pv = stD.prov
        C.ok(r["slot_birth_at_contact"] and stD.fork["target"] == 0 and stD.fork["old_value"] == (-5) % N
             and stD.u.delta.get(0) == 11 and stD.u.delta.get(4) == 5 and len(pv.copies) == 6
             and pv.copies[0].get("retired") == {"tick": 1, "by": 5} and pv.copies[4].get("parent") == 0
             and pv.copies[5].get("intervention", {}).get("replaces") == 0 and not pv.check(stD.u),
             "A3 C+ after a slot-centred birth: target = centre (token -x); newborn keeps x and its parent link to the "
             "retired copy; new origin copy 5; ledger check passes")
        th, d = P.fixture_state(N, [0, 12], [0, 7])
        r = base_with_oracle(N, k, th, d, 0, 40, 0)
        st0 = fork(r["minus"], 0, "R", {"R": 0, "D": 1}, 10, "C-", tau_C=r["tau_C"])
        C.ok(st0.fork["noop"] and st0.u.delta == r["minus"].u.delta and st0.prov.events[-1][1] == "intervention"
             and not st0.prov.check(st0.u), "A4 no-op arm (pre-existing value = x): no value change, epoch still logged")
        th, d = P.fixture_state(N, [0, 12, 11, 13], [5, 2, 3, 4])
        r = base_with_oracle(N, k, th, d, 1, 40, 5)
        stc = fork(r["minus"], 1, "BASE", vals, 200, "C-", tau_C=r["tau_C"])
        continue_fork(ieng, run, stc)
        e = endpoint(stc, 5)
        C.ok(stc.hit_cap and e["Y"] == 1 and e["h_stop"] == 1, "A5 cap 5 reached at h = 1 < H with cap >= q = 5: "
                                                                "Y = 1, h_stop recorded")
        th, d = P.fixture_state(N, [0, 12, 11, 13], [5, 2, 3, 4])
        r = base_with_oracle(N, k, th, d, 0, 40, 5)
        okm = fork(r["minus"], 0, "R", vals, 10, "C-", tau_C=r["tau_C"]) is not None
        try:
            fork(r["plus"], 0, "R", vals, 10, "C+", tau_C=r["tau_C"])
            refused = False
        except ValueError:
            refused = True
        C.ok(r["slot_birth_at_contact"] and not r["eligible_plus"] and refused and okm,
             "A6 slot-centred birth at contact reaching cap 5: the C+ fork is refused, the C- fork is accepted")
        # A7 C+ post-birth no-op: centre token after the birth is -12 = 12 = x_R
        th, d = P.fixture_state(N, [0, 12, 11, 13], [12, 2, 3, 4])
        r = base_with_oracle(N, k, th, d, 0, 40, 0)
        v7 = {"R": 12, "D": 13}
        a7 = continue_fork(ieng, run, fork(r["plus"], 0, "R", v7, 40, "C+", tau_C=r["tau_C"]))
        b7 = continue_fork(ieng, run, fork(r["plus"], 0, "BASE", v7, 40, "C+", tau_C=r["tau_C"]))
        C.ok(r["slot_birth_at_contact"] and a7.fork["noop"] and P.canon(a7.u) == P.canon(b7.u)
             and endpoint(a7, 5) == endpoint(b7, 5),
             "A7 C+ after a slot-centred birth with a no-op write (-x = x_R = N/2): continuation and endpoint equal "
             "the BASE reference arm")

        # ---- E. fail-closed contracts (R1, R2)
        def refused(fn):
            try:
                fn()
                return False
            except ValueError:
                return True
        th, d = P.fixture_state(N, [0, 12], [5, 7])
        r = base_with_oracle(N, k, th, d, 0, 40, 0)
        mi, pl, tc = r["minus"], r["plus"], r["tau_C"]
        part = fork(mi, 0, "R", vals, 30, "C-", tau_C=tc)
        C.ok(refused(lambda: endpoint(part, 5)), "E1 endpoint of an unadvanced fork is refused")
        P.run_to(ieng, run, part, 10)
        C.ok(refused(lambda: endpoint(part, 5)), "E2 endpoint of a partial continuation (h = 10 < H = 30) is refused")
        P.run_to(ieng, run, part)
        C.ok(endpoint(part, 5)["stop"] == "horizon" and all(refused(lambda qq=qq: endpoint(part, qq))
                                                            for qq in (0, -3, True, 2.5, "5")),
             "E3 completed continuation: stop = horizon; q not a positive integer is refused")
        th, d = P.fixture_state(N, [0, 12, 11, 13], [5, 2, 3, 4])
        r5 = base_with_oracle(N, k, th, d, 1, 40, 5)
        cs = continue_fork(ieng, run, fork(r5["minus"], 1, "BASE", vals, 50, "C-", tau_C=r5["tau_C"]))
        C.ok(cs.hit_cap and refused(lambda: endpoint(cs, 6)) and endpoint(cs, 5)["stop"] == "cap",
             "E4 cap-stopped run: refused when 0 < cap < q (censoring), accepted with stop = cap when cap >= q")
        bad_ch = [{"r1": 6, "s1": 1}, {"r1": 0, "s1": 2}, {"r1": 0, "s1": True}, {"r1": 12.0, "s1": 1}, {"r1": 0}]
        C.ok(all(refused(lambda c=c: o1_values(c, N)) for c in bad_ch) and refused(lambda: o1_values(ch, 23)),
             "E5 o1_values refuses off-family r, invalid epsilon, non-integers, missing keys and odd N")
        bad_v = [{"R": 6, "D": 7}, {"R": 0, "D": 2}, {"R": 12, "D": 12}, {"R": 0, "D": 1, "X": 3}, {"R": 0}]
        C.ok(all(refused(lambda vv=vv: fork(mi, 0, "R", vv, 10, "C-", tau_C=tc)) for vv in bad_v),
             "E6 fork refuses value pairs outside O1 (off-family r, |D - R| != 1, extra or missing keys)")
        C.ok(all(refused(lambda lmk=lmk: fork(mi, 0, "R", vals, 10, lmk, tau_C=tc)) for lmk in ("B", "C", None)),
             "E7 fork refuses landmarks other than C- and C+")
        unannotated = copy.deepcopy(mi)
        unannotated.landmark_tick = None
        C.ok(refused(lambda: fork(mi, 0, "R", vals, 10, "C+", tau_C=tc)) and
             refused(lambda: fork(pl, 0, "R", vals, 10, "C-", tau_C=tc)) and
             refused(lambda: fork(mi, 0, "R", vals, 10, "C-", tau_C=tc + 1)) and
             refused(lambda: fork(unannotated, 0, "R", vals, 10, "C-", tau_C=tc)),
             "E8 fork refuses a boundary whose landmark_tick does not match the C-/C+ fork tick (or is missing)")
        C.ok(all(refused(lambda hh=hh: fork(mi, 0, "R", vals, hh, "C-", tau_C=tc)) for hh in (0, -5, 2.0, True)),
             "E9 fork refuses H that is not a positive integer")
        C.ok(refused(lambda: fork(mi, 7, "R", vals, 10, "C-", tau_C=tc)) and
             refused(lambda: fork(mi, 0, "X", vals, 10, "C-", tau_C=tc)) and
             refused(lambda: fork(fork(mi, 0, "R", vals, 10, "C-", tau_C=tc), 0, "R", vals, 10, "C-", tau_C=tc)),
             "E10 fork refuses a non-root slot, an unknown arm and an already forked state")

    try:
        section_a()
    except Exception as e:                                           # fail closed, but keep counting
        C.ok(False, "A* fixtures raised %s: %s" % (type(e).__name__, str(e)[:80]))

    # ---- B. randomized synthetic seeds
    rng = random.Random(SYNTH_TAG)
    cover = Counter()
    nb = 0
    for trial in range(trials):
        if trial % 3 == 0:
            N, k = 120, 8
            _, th0, d0 = run.base_draw(peng, SYNTH_TAG, N, k, trial)
            ch = run.arm_choices(SYNTH_TAG, N, k, trial)
            j = ch["slot"]
            L, cap, q = 400, rng.choice([0, 300]), 100
            H = 800 if trial % 30 == 0 else rng.choice([40, 120])
            cover["native_120_8"] += 1
        else:
            N, k = (24, 2) if trial % 3 == 1 else (60, 6)
            m0 = rng.randint(3, 6)
            d0 = [rng.choice([0, N // 2]) if rng.random() < 0.3 else rng.randrange(N) for _ in range(m0)]
            th0 = [rng.randrange(N) for _ in range(m0)]
            j = rng.randrange(m0)
            ch = {"slot": j, "r1": rng.choice([0, N // 2]), "s1": rng.choice([1, -1])}
            L, cap = rng.choice([10, 40]), rng.choice([0, 0, 30, 60])
            q = rng.choice([8, 20]) if cap == 0 else rng.choice([8, cap])
            H = rng.choice([20, 60])
        try:
            nb += full_case(N, k, th0, d0, j, ch, L, cap, H, q, cover, str(trial))
        except Exception as e:                                       # fail closed, but keep counting
            C.ok(False, "B* trial %d raised %s: %s" % (trial, type(e).__name__, str(e)[:80]))
    say("randomized: %d seeds, %d forked boundaries" % (trials, nb))
    need = ["fork_C-", "fork_C+", "s0_identity", "noop_arm", "target_not_j", "sign_invisible_x", "cap_hit",
            "birth_after_intervention", "descendants_of_retired", "contact_removed_by_write", "Y_differs",
            "slot_birth_before_Cplus", "native_120_8", "M2_noop_C-", "M2_noop_C+"]
    for key in (need if coverage else []):
        C.ok(cover[key] > 0, "C coverage: %s (%d)" % (key, cover[key]))
    say("coverage: " + ", ".join("%s %d" % (key, cover[key]) for key in sorted(cover)))

    # ---- D. registered inputs
    root_files = sorted({p for p in K.OPENED if p.startswith(P.ROOT + os.sep)})
    allowed = {P.ENGINE, P.ORIENT, P.RUNNER, K.LIB, CLOCK, os.path.abspath(__file__)}

    def permitted(p):
        if p in allowed:
            return True
        dd, b = os.path.split(p)
        return os.path.basename(dd) == "__pycache__" and any(
            os.path.dirname(dd) == os.path.dirname(a) and b.startswith(os.path.splitext(os.path.basename(a))[0] + ".")
            for a in allowed)
    C.ok(all(permitted(p) for p in root_files) and not any("/upload/az-token-resonance" in p for p in K.OPENED),
         "D1 files opened inside the repository: only the pinned files, the clock, the provenance library and this "
         "script (%d paths)" % len(root_files))
    say("checks: %d, failed: %d" % (C.n, C.bad))
    say("SELFTEST PASS" if C.bad == 0 else "SELFTEST FAIL")
    return 0 if C.bad == 0 else 1


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        raise SystemExit(selftest())
    print(__doc__)
    raise SystemExit(2)
