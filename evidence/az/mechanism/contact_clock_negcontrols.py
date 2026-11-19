#!/usr/bin/env python3
"""Negative controls for az_tokres_contact_clock.py: each control injects one fault and runs the self-test with
60 randomized trajectories (explicit fixtures included; the coverage assertions, which need the full 400, are
skipped); a control passes iff the self-test FAILS. NC00 is the
unmodified clock and must PASS. Synthetic only.

    python3 -I evidence/az/mechanism/contact_clock_negcontrols.py
"""
import contextlib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import az_tokres_contact_clock as K                                  # noqa: E402

TRIALS = 60


def run_selftest():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            rc = K.selftest(trials=TRIALS, coverage=False)
        except Exception as e:
            print("raised: %r" % e)
            rc = 1
    out = buf.getvalue()
    fails = [ln for ln in out.splitlines() if ln.startswith("FAIL")]
    tags = sorted({ln.split()[1] for ln in fails})
    return rc, len(fails), tags, "raised" in out


def patch(obj, name, new):
    old = getattr(obj, name)
    setattr(obj, name, new)
    return lambda: setattr(obj, name, old)


def nc_graph_one_tick_late():
    """prediction uses the phases two ticks ahead (tick shift)"""
    def bad(peng, st):
        u = st.u
        nodes = list(u.theta)
        th = {x: (u.theta[x] + 2 * u.delta[x]) % st.N for x in nodes}
        return nodes, th, sorted(peng.graph_edges_for(nodes, th, st.N, st.k))
    return patch(K, "predicted_graph", bad)


def nc_graph_post_interaction():
    """prediction uses the current (already-interacted) phases without the advance"""
    def bad(peng, st):
        u = st.u
        nodes = list(u.theta)
        th = dict(u.theta)
        return nodes, th, sorted(peng.graph_edges_for(nodes, th, st.N, st.k))
    return patch(K, "predicted_graph", bad)


def nc_stale_carrier_plus():
    """C+ target taken as the pre-tick carrier (stale identity)"""
    orig = K.contact_clock

    def bad(*a, **kw):
        r = orig(*a, **kw)
        if r["status"] == "contact":
            r["carrier_plus"] = r["carrier_pre"]
        return r
    return patch(K, "contact_clock", bad)


def nc_tau_free():
    """tau_slot^free substituted for the dynamic contact time"""
    orig = K.contact_clock

    def bad(peng, ieng, run, st, j, L, q=100):
        th0 = [st.u.theta[i] for i in sorted(st.u.theta)]
        d0 = [st.u.delta[i] for i in sorted(st.u.delta)]
        tf = K.tau_free(peng, st.N, st.k, th0, d0, j, L)
        r = orig(peng, ieng, run, st, j, L, q)
        if r["status"] == "contact":
            r["tau_C"] = tf
        return r
    return patch(K, "contact_clock", bad)


def nc_eligibility_ignores_cap():
    """boundary eligibility ignores the node cap"""
    return patch(K, "eligible", lambda st: (not st.done or st.hit_cap) and st.iters < st.T)


def nc_minus_after_contact():
    """C- boundary taken after the contact tick (off-by-one boundary)"""
    orig = K.contact_clock

    def bad(*a, **kw):
        r = orig(*a, **kw)
        if r["status"] == "contact":
            r["minus"] = r["plus"]
        return r
    return patch(K, "contact_clock", bad)


def nc_prediction_mutates():
    """prediction advances the live phases in place"""
    def bad(peng, st):
        u = st.u
        nodes = list(u.theta)
        for x in nodes:
            u.theta[x] = (u.theta[x] + u.delta[x]) % st.N
        th = dict(u.theta)
        for x in nodes:
            u.theta[x] = (u.theta[x] - u.delta[x] + (1 if x == nodes[-1] else 0)) % st.N
        return nodes, th, sorted(peng.graph_edges_for(nodes, th, st.N, st.k))
    return patch(K, "predicted_graph", bad)


def nc_registered_path():
    """the self-test tries to open a path under the registered campaign uploads"""
    orig = K.check_pins

    def bad():
        orig()
        try:
            open(os.path.join(K.P.ROOT, "upload", "az-token-resonance-stage9", "absent.jsonl"))
        except OSError:
            pass
    return patch(K, "check_pins", bad)


CONTROLS = [nc_graph_one_tick_late, nc_graph_post_interaction, nc_stale_carrier_plus, nc_tau_free,
            nc_eligibility_ignores_cap, nc_minus_after_contact, nc_prediction_mutates, nc_registered_path]


def main():
    ok = True
    rc, nfail, _, _ = run_selftest()
    good = rc == 0 and nfail == 0
    ok &= good
    print("NC00 unmodified clock: self-test %s" % ("PASS" if good else "FAIL"), flush=True)
    for i, ctl in enumerate(CONTROLS, 1):
        undo = ctl()
        try:
            rc, nfail, tags, raised = run_selftest()
        finally:
            undo()
        det = rc != 0
        ok &= det
        print("NC%02d %-70s %s (%d failed checks: %s%s)" % (i, ctl.__doc__.strip(), "DETECTED" if det else "MISSED",
                                                            nfail, " ".join(tags), "; raised" if raised else ""),
              flush=True)
    print("NEGCONTROLS PASS" if ok else "NEGCONTROLS FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
