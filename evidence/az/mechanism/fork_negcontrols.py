#!/usr/bin/env python3
"""Negative controls for az_tokres_fork.py: each control injects one fault and runs the self-test with 40 randomized
seeds (explicit fixtures included; coverage assertions skipped), once with the fail-closed provenance guard on and
once with it off; a control passes iff the self-test FAILS in both modes. NC00 is the unmodified instrument and
must PASS in both modes. Synthetic only.

    python3 -I evidence/az/mechanism/fork_negcontrols.py
"""
import contextlib
import copy
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import az_tokres_fork as F                                           # noqa: E402

TRIALS = 40
P = F.P


def run_selftest(guard=True):
    """guard=False switches the fail-closed provenance guard off (P.FORCE_STRICT), so that detection must come from
    the self-test's own comparisons (oracle ledger, ledger check, state comparisons)."""
    P.FORCE_STRICT = None if guard else False
    buf = io.StringIO()
    raised = ""
    with contextlib.redirect_stdout(buf):
        try:
            rc = F.selftest(trials=TRIALS, coverage=False)
        except Exception as e:
            raised = "%s: %s" % (type(e).__name__, str(e)[:60])
            rc = 1
    P.FORCE_STRICT = None
    out = buf.getvalue()
    fails = [ln for ln in out.splitlines() if ln.startswith("FAIL")]
    return rc, len(fails), sorted({ln.split()[1] for ln in fails}), raised


def patch(obj, name, new):
    old = getattr(obj, name)
    setattr(obj, name, new)
    return lambda: setattr(obj, name, old)


def wrap_fork(post):
    """Run the real fork, then apply `post(st, boundary, j, arm, values)` to the result."""
    orig = F.fork

    def bad(boundary, j, arm, values, H, landmark):
        st = orig(boundary, j, arm, values, H, landmark)
        post(st, boundary, j, arm, values)
        return st
    return patch(F, "fork", bad)


def nc_sign_covariant():
    """sign-covariant write sigma*x instead of the absolute write"""
    def post(st, b, j, arm, values):
        if arm != "BASE":
            v = st.fork["target"]
            sg = b.prov.labels[v][1]
            st.u.delta[v] = (sg * values[arm]) % st.N
            c = st.prov.labels[v][0]
            st.prov.copies[c]["root_value"] = st.u.delta[v]
            st.prov.copies[c]["intervention"]["new_value"] = st.u.delta[v]
            t, kind, d = st.prov.events[-1]
            st.prov.events[-1] = (t, kind, d[:4] + (st.u.delta[v],))
            st.census = P.Counter(st.u.delta.values())
    return wrap_fork(post)


def nc_no_epoch():
    """token written without an intervention epoch (plain delta mutation)"""
    orig = F.fork

    def bad(boundary, j, arm, values, H, landmark):
        st = orig(boundary, j, "BASE", values, H, landmark)
        if arm != "BASE":
            v = st.fork["target"]
            st.u.delta[v] = values[arm] % st.N
            st.fork.update(arm=arm, x=values[arm] % st.N)
        return st
    return patch(F, "fork", bad)


def nc_recycle_old_copy():
    """the old copy is recycled: its root value overwritten, no new origin"""
    orig_iv = F.ForkProvenance.intervene

    def bad(self, v, x, tick, arm):
        c_old, s = self.labels[v]
        old = self.value(v)
        self.copies[c_old]["root_value"] = (s * x) % self.N
        self.events.append((tick, "intervention", (v, c_old, c_old, old, x % self.N)))
        return c_old, c_old, old
    return patch(F.ForkProvenance, "intervene", bad)


def nc_T_not_set():
    """configuration boundary omitted (T stays the prefix budget)"""
    def post(st, b, j, arm, values):
        st.T = b.T
    return wrap_fork(post)


def nc_clock_reset():
    """historic clock reset at the fork (fb cleared)"""
    def post(st, b, j, arm, values):
        st.fb = None
    return wrap_fork(post)


def nc_shallow_copy():
    """arms share the boundary's Universe (shallow copy)"""
    def post(st, b, j, arm, values):
        if arm == "BASE":
            st.u = b.u
    return wrap_fork(post)


def nc_alphabet_not_expanded():
    """post-fork alphabet left at S_BASE"""
    def post(st, b, j, arm, values):
        st.alphabet = set(b.alphabet)
    return wrap_fork(post)


def nc_census_not_reset():
    """census not reset after the write"""
    def post(st, b, j, arm, values):
        st.census = copy.deepcopy(b.census)
    return wrap_fork(post)


def nc_target_node_j():
    """target fixed to node id j instead of the current carrier of c_j"""
    orig = F.fork

    def bad(boundary, j, arm, values, H, landmark):
        b2 = copy.deepcopy(boundary)
        if j in b2.prov.labels and b2.prov.carrier.get(j) != j:
            cj = b2.prov.labels[j][0]
            vj = b2.prov.carrier[j]
            b2.prov.carrier[j], b2.prov.carrier[cj] = j, vj
            b2.prov.labels[j], b2.prov.labels[vj] = [j, b2.prov.labels[vj][1]], [cj, b2.prov.labels[j][1]]
        return orig(b2, j, arm, values, H, landmark)
    return patch(F, "fork", bad)


def nc_virtual_tick():
    """a virtual engine tick is injected at the fork"""
    orig = F.fork

    def bad(boundary, j, arm, values, H, landmark):
        st = orig(boundary, j, arm, values, H, landmark)
        P.tick(sys.modules["frk_engine_instr"], sys.modules["az_tokres_run_frozen"], st)
        return st
    return patch(F, "fork", bad)


def nc_retired_still_carried():
    """the retired copy is left in the carrier map"""
    orig_iv = F.ForkProvenance.intervene

    def bad(self, v, x, tick, arm):
        res = orig_iv(self, v, x, tick, arm)
        self.carrier[res[0]] = v
        return res
    return patch(F.ForkProvenance, "intervene", bad)


def nc_origin_as_birth_child():
    """the new segment is linked to the old copy as a birth parent"""
    orig_iv = F.ForkProvenance.intervene

    def bad(self, v, x, tick, arm):
        res = orig_iv(self, v, x, tick, arm)
        self.copies[res[1]]["parent"] = res[0]
        return res
    return patch(F.ForkProvenance, "intervene", bad)


CONTROLS = [nc_sign_covariant, nc_no_epoch, nc_recycle_old_copy, nc_T_not_set, nc_clock_reset, nc_shallow_copy,
            nc_alphabet_not_expanded, nc_census_not_reset, nc_target_node_j, nc_virtual_tick,
            nc_retired_still_carried, nc_origin_as_birth_child]


def main():
    ok = True
    for guard in (True, False):
        rc, nfail, _, raised = run_selftest(guard)
        good = rc == 0 and nfail == 0
        ok &= good
        print("NC00 unmodified instrument, guard %s: self-test %s%s" % ("on" if guard else "off",
                                                                     "PASS" if good else "FAIL", raised), flush=True)
    for i, ctl in enumerate(CONTROLS, 1):
        line = []
        for guard in (True, False):
            undo = ctl()
            try:
                rc, nfail, tags, raised = run_selftest(guard)
            finally:
                undo()
            det = rc != 0
            ok &= det
            line.append("guard %s: %s (%d failed checks: %s%s)" % ("on" if guard else "off",
                                                                  "DETECTED" if det else "MISSED", nfail,
                                                                  " ".join(tags), "; raised " + raised if raised
                                                                  else ""))
        print("NC%02d %s\n     %s\n     %s" % (i, ctl.__doc__.strip(), line[0], line[1]), flush=True)
    print("NEGCONTROLS PASS" if ok else "NEGCONTROLS FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
