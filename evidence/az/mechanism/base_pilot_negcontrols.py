#!/usr/bin/env python3
"""Negative controls for az_fork_base_pilot.py: each control injects one fault and runs the self-test (synthetic
test tag only); a control passes iff the self-test FAILS. NC00 is the unmodified driver and must PASS.

    python3 -I evidence/az/mechanism/base_pilot_negcontrols.py
"""
import contextlib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import az_fork_base_pilot as D                                       # noqa: E402


def run_selftest():
    buf = io.StringIO()
    raised = ""
    with contextlib.redirect_stdout(buf):
        try:
            rc = D.selftest(verbose=True)
        except Exception as e:
            raised = "%s: %s" % (type(e).__name__, str(e)[:60])
            rc = 1
    fails = [ln for ln in buf.getvalue().splitlines() if ln.startswith("FAIL")]
    return rc, len(fails), sorted({ln.split()[1] for ln in fails}), raised


def patch(obj, name, new):
    old = getattr(obj, name)
    setattr(obj, name, new)
    return lambda: setattr(obj, name, old)


def nc_verify_disabled():
    """clock results accepted without verification"""
    return patch(D, "verify", lambda peng, ieng, run, r, *a: (D.state_id(r["minus"]), D.state_id(r["plus"]))
                 if r["status"] == "contact" else (None, None))


def nc_denominator_contacts_only():
    """F(L) computed over contact seeds only"""
    orig = D.summarize

    def bad(records, man):
        s = orig(records, man)
        nc = sum(1 for r in records if r["status"] == "contact") or 1
        for row in s["rows"]:
            row["F"] = row["k"] / nc
        qual = [row["L"] for row in s["rows"] if row["F"] >= man["threshold"]]
        s["L_star"] = qual[0] if qual else "no qualifying L"
        return s
    return patch(D, "summarize", bad)


def nc_auto_Lmax():
    """L_max chosen automatically when no L qualifies"""
    orig = D.summarize

    def bad(records, man):
        s = orig(records, man)
        if s["L_star"] == "no qualifying L":
            s["L_star"] = man["L_grid"][-1]
        return s
    return patch(D, "summarize", bad)


def nc_strict_less():
    """tau_C < L used instead of tau_C <= L"""
    orig = D.summarize

    def bad(records, man):
        recs = [dict(r, tau_C=r["tau_C"] + 1) if r["status"] == "contact" and r["tau_C"] in man["L_grid"] else r
                for r in records]
        return orig(recs, man)
    return patch(D, "summarize", bad)


def nc_wilson_wrong_z():
    """Wilson interval computed with the one-sided z (1.645)"""
    return patch(D, "_z", lambda level: 1.6448536269514722)


def nc_timing_in_summary():
    """run time written into the deterministic summary"""
    orig = D.summary_text
    import time

    def bad(s, man):
        return orig(s, man) + "elapsed %.6f\n" % time.perf_counter()
    return patch(D, "summary_text", bad)


def nc_freeze_gate_off():
    """pilot plan does not require a frozen manifest"""
    orig = D.check_manifest

    def bad(man, plan):
        if plan == "pilot":
            man = dict(man, frozen_script_sha256=D.P.sha256_file(D.__file__))
        return orig(man, plan)
    return patch(D, "check_manifest", bad)


def nc_tag_guard_off():
    """any tag accepted in either plan"""
    orig = D.check_manifest

    def bad(man, plan):
        return orig(dict(man, tag=D.TEST_TAG), "test") if plan == "test" else orig(
            dict(man, tag="AZ-FORK-BASEPILOT-P1"), plan)
    return patch(D, "check_manifest", bad)


def nc_output_overwrite():
    """an existing output directory is accepted"""
    made = []

    def bad(out):
        t = os.path.abspath(out)
        if not os.path.exists(t):
            made.append(t)
        os.makedirs(t, exist_ok=True)
        return t
    undo = patch(D, "make_out", bad)

    def undo_and_clean():
        undo()
        for t in made:
            if os.path.realpath(t).startswith(os.path.join(D.P.ROOT, "upload") + os.sep):
                try:
                    os.rmdir(os.path.realpath(t))
                except OSError:
                    pass
    return undo_and_clean


def nc_tau_free_substituted():
    """tau_slot^free recorded as tau_C"""
    orig = D.seed_record

    def bad(peng, ieng, run, man, b, verifier=None):
        rec = orig(peng, ieng, run, man, b, verifier)
        if rec["status"] == "contact" and rec["tau_free"] is not None:
            rec["tau_C"] = rec["tau_free"]
        return rec
    return patch(D, "seed_record", bad)


def nc_audit_disabled():
    """complete audit always passes"""
    return patch(D, "audit_dir", lambda peng, ieng, run, d, raw, sha: [])


def nc_audit_no_field_compare():
    """audit checks only the replay, not every stored field"""
    return patch(D, "_audit_records", lambda peng, ieng, run, man, records: [
        "record %d: replay differs" % b for b in D.audit(peng, ieng, run, man, records)])


def nc_audit_no_summary():
    """audit does not recompute the summaries"""
    return patch(D, "_audit_summary", lambda d, records, man, raw: [])


def nc_audit_no_sums():
    """audit does not check the file set and SHA256SUMS"""
    return patch(D, "_audit_sums", lambda d: [])


def nc_audit_no_identity():
    """audit does not bind the approved manifest"""
    return patch(D, "_audit_identity", lambda d, raw, sha: [])


def nc_run_no_identity():
    """run accepts manifest bytes that differ from the approved SHA-256"""
    return patch(D, "check_manifest_identity", lambda raw, sha: None)


def nc_no_git_binding():
    """pilot manifest need not be committed at HEAD"""
    return patch(D, "check_git_committed", lambda path: None)


def nc_output_no_realpath():
    """output check ignores symbolic links in the parent path"""
    def bad(out):
        t = os.path.abspath(out)
        for bad_ in ("upload", "records", "dsn"):
            b = os.path.join(D.P.ROOT, bad_)
            if t == b or t.startswith(b + os.sep):
                raise D.Refused("inside")
        if os.path.lexists(t):
            raise D.Refused("exists")
        os.mkdir(t)
        made.append(t)
        return t
    made = []
    undo = patch(D, "make_out", bad)

    def undo_and_clean():
        undo()
        for t in made:
            try:
                os.rmdir(t)
            except OSError:
                pass
    return undo_and_clean


CONTROLS = [nc_verify_disabled, nc_denominator_contacts_only, nc_auto_Lmax, nc_strict_less, nc_wilson_wrong_z,
            nc_timing_in_summary, nc_freeze_gate_off, nc_tag_guard_off, nc_output_overwrite, nc_tau_free_substituted,
            nc_audit_disabled, nc_audit_no_field_compare, nc_audit_no_summary, nc_audit_no_sums,
            nc_audit_no_identity, nc_run_no_identity, nc_no_git_binding, nc_output_no_realpath]


def main():
    ok = True
    rc, nfail, _, raised = run_selftest()
    good = rc == 0 and nfail == 0
    ok &= good
    print("NC00 unmodified driver: self-test %s%s" % ("PASS" if good else "FAIL", raised), flush=True)
    for i, ctl in enumerate(CONTROLS, 1):
        undo = ctl()
        try:
            rc, nfail, tags, raised = run_selftest()
        finally:
            undo()
        det = rc != 0
        ok &= det
        print("NC%02d %-55s %s (%d failed checks: %s%s)" % (i, ctl.__doc__.strip(), "DETECTED" if det else "MISSED",
                                                            nfail, " ".join(tags), "; raised " + raised if raised
                                                            else ""), flush=True)
    print("NEGCONTROLS PASS" if ok else "NEGCONTROLS FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
