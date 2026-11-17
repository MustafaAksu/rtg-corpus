#!/usr/bin/env python3
"""Negative controls for az_tokres_provenance.py: each control injects one fault into the instrument and runs the
self-test (40 randomized trajectories); the control passes iff the self-test FAILS (the fault is detected).
NC00 runs the unmodified instrument and must PASS. Synthetic only.

    python3 -I evidence/az/mechanism/provenance_negcontrols.py
"""
import contextlib
import copy
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import az_tokres_provenance as P                                    # noqa: E402

TRIALS = 40


def run_selftest():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            rc = P.selftest(trials=TRIALS)
        except Exception as e:                                       # a guard that raises also counts as detection
            print("raised: %r" % e)
            rc = 1
    out = buf.getvalue()
    return rc, sum(1 for line in out.splitlines() if line.startswith("FAIL")), "raised" in out


def patch(obj, name, new):
    old = getattr(obj, name)
    setattr(obj, name, new)
    return lambda: setattr(obj, name, old)


def nc_rotation_raw():
    """rotation applied along the RAW path (ignores the engine's orientation)"""
    orig = P.Provenance.on_rotation

    def bad(self, path, how):
        return orig(self, list(reversed(path)) if how == "reversed" else path, how)
    return patch(P.Provenance, "on_rotation", bad)


def nc_rotation_backwards():
    """rotation applied in the opposite direction"""
    orig = P.Provenance.on_rotation
    return patch(P.Provenance, "on_rotation", lambda self, path, how: orig(self, list(reversed(path)), how))


def nc_birth_post_labels():
    """birth leaves the centre's sign unflipped"""
    def bad(self, centre, newborn):
        c, s = self._pre[centre]
        child = len(self.copies)
        self.copies.append({"root": self.copies[c]["root"], "root_value": self.copies[c]["root_value"], "parent": c,
                            "birth": {"tick": self._tick, "centre": centre, "newborn": newborn}})
        self.labels[newborn] = [child, s]
        self.carrier[child] = newborn
        self.sign_history[child] = [(self._tick, s)]
        self.events.append((self._tick, "birth", (centre, newborn, c, child)))
    return patch(P.Provenance, "on_birth", bad)


def nc_birth_same_copy():
    """newborn and centre share one copy id (no distinct copy identity)"""
    def bad(self, centre, newborn):
        c, s = self._pre[centre]
        self.labels[newborn] = [c, s]
        self.labels[centre] = [c, -s]
        self.events.append((self._tick, "birth", (centre, newborn, c, c)))
    return patch(P.Provenance, "on_birth", bad)


def nc_swap_by_value():
    """swap transports labels only when the values differ (value matching)"""
    orig = P.Provenance.on_swap

    def bad(self, a, b):
        if self.value(a) != self.value(b):
            return orig(self, a, b)
        self.events.append((self._tick, "swap", (a, b)))
    return patch(P.Provenance, "on_swap", bad)


def nc_double_orient():
    """the sidecar calls orient_path a second time on the live state"""
    orig_install = P.install

    def bad_install(eng):
        holder = orig_install(eng)
        wrapped = eng.orient_path

        def twice(path, theta, delta, N, u):
            wrapped(path, theta, delta, N, u)
            return wrapped(path, theta, delta, N, u)
        eng.orient_path = twice
        return holder
    return patch(P, "install", bad_install)


def nc_shallow_checkpoint():
    """checkpoint by shallow copy (shares the Universe with the original)"""
    return patch(P, "checkpoint", lambda st: (lambda c: (setattr(c, "landmark_tick", st.u.steps), c)[1])(copy.copy(st)))


def nc_checkpoint_drops_runner_state():
    """checkpoint copies the Universe and provenance but resets fb (runner state outside the Universe)"""
    def bad(st):
        c = copy.deepcopy(st)
        c.landmark_tick = st.u.steps
        c.fb = None
        return c
    return patch(P, "checkpoint", bad)


def nc_tick_skips_window():
    """the held loop never collects the TDR-26 window (diverges from run_state)"""
    def bad(eng, run, st):
        saved = st.tdr26
        st.tdr26 = False
        try:
            return orig(eng, run, st)
        finally:
            st.tdr26 = saved
    orig = P.tick
    return patch(P, "tick", bad)


def nc_tick_checks_cap_late():
    """the held loop omits the cap test before the step"""
    def bad(eng, run, st):
        saved = st.cap
        if st.cap > 0 and len(st.u.theta) >= st.cap and not st.done:
            st.cap = 0
        try:
            return orig(eng, run, st)
        finally:
            st.cap = saved
    orig = P.tick
    return patch(P, "tick", bad)


CONTROLS = [nc_rotation_raw, nc_rotation_backwards, nc_birth_post_labels, nc_birth_same_copy, nc_swap_by_value,
            nc_double_orient, nc_shallow_checkpoint, nc_checkpoint_drops_runner_state,
            nc_tick_skips_window, nc_tick_checks_cap_late]


def main():
    ok = True
    rc, nfail, _ = run_selftest()
    good = rc == 0 and nfail == 0
    ok &= good
    print("NC00 unmodified instrument: self-test %s" % ("PASS" if good else "FAIL"))
    for i, ctl in enumerate(CONTROLS, 1):
        undo = ctl()
        try:
            rc, nfail, raised = run_selftest()
        finally:
            undo()
        detected = rc != 0
        ok &= detected
        print("NC%02d %-62s %s (%d failed checks%s)" % (i, ctl.__doc__.strip(), "DETECTED" if detected else "MISSED",
                                                         nfail, ", guard raised" if raised else ""))
    print("NEGCONTROLS PASS" if ok else "NEGCONTROLS FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
