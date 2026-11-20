#!/usr/bin/env python3
"""AZ mechanism study, fork design - BASE-only pilot for the observation bound L (driver, protocol and tests).

[SESSION] NONCANONICAL. Protocol: records/az/AZ_TOKEN_RESONANCE_FORK_BASE_PILOT_PROTOCOL.md. Written by the Claude
AZ lane, reviewed by ChatGPT (task split as proposed and supported in the 20 Nov exchange; source-reported).
The PILOT RUN itself needs a separate PI authorisation and a frozen manifest; until then only --selftest runs.

What the pilot measures (BASE prefixes only; no R/D fork is ever built)
  For each pre-fixed seed b = 0 .. n-1 of a NEW tag: the native initial state base_draw(tag, N, k, b), the slot
  j = arm_choices(tag, N, k, b)['slot'], and one BASE prefix run with the merged contact clock at L_max = max(grid)
  (T_ref = L_max + 1, cap C). From that single run every candidate L is evaluated: tau_C does not depend on T_ref
  or L, and C+ eligibility at tau_C <= L is the same for T_ref = L + 1 and L_max + 1 (tested).
  Each contact result is VERIFIED before use: tau_C is taken only from the clock output, the C-/C+ annotations
  must equal tau_C - 1 / tau_C, and an independent replay of the same seed must reproduce both boundary states
  (full fingerprints) and find no earlier slot contact; the boundary fingerprints are stored as checkpoint ids.

L rule (fixed before the run; design section 8)
  F(L) = #{seeds with status contact and tau_C <= L} / n   (denominator: ALL pilot seeds)
  L* = min{L in grid : F(L) >= threshold}, else the result is "no qualifying L" (never an automatic L_max).
  With wilson_in_rule = true the comparison uses the lower Wilson bound instead of F(L). The manifest must state
  true or false before the run (null is refused). C-/C+ eligibility, centre cases and already-positive counts are
  reported but never change the rule.

    python3 -I evidence/az/mechanism/az_fork_base_pilot.py --selftest
    python3 -I evidence/az/mechanism/az_fork_base_pilot.py --run --manifest evidence/az/mechanism/base_pilot_manifest.json --out DIR
    python3 -I evidence/az/mechanism/az_fork_base_pilot.py --audit DIR --manifest evidence/az/mechanism/base_pilot_manifest.json
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import az_tokres_contact_clock as K                                  # noqa: E402  (audit hook first)

import argparse                                                      # noqa: E402
import hashlib                                                       # noqa: E402
import json                                                          # noqa: E402
import math                                                          # noqa: E402
import time                                                          # noqa: E402

P = K.P
CLOCK_SHA = "4cdd9a7d66d3ddc083b0e45f699ffe743b35d69463b09c7aa34541f08df48eee"    # merged with PR #328
TEST_TAG = "AZ-FORK-BASEPILOT-TEST"
FORBIDDEN_TAGS = ("AZ-FORK-CLOCK-SYNTH", "AZ-FORK-OPERATOR-SYNTH", TEST_TAG)
REGISTERED_PREFIX = "AZ-TOKRES"
DETERMINISTIC = ("seeds.jsonl", "summary.json", "summary.txt")


class Refused(Exception):
    pass


def check_pins():
    K.check_pins()
    if P.sha256_file(os.path.join(HERE, "az_tokres_contact_clock.py")) != CLOCK_SHA:
        raise Refused("pin mismatch for az_tokres_contact_clock.py")


# ---------------------------------------------------------------- manifest and output gates
def check_manifest(man, plan):
    need = {"schema", "frozen_script_sha256", "tag", "N", "k", "profile", "policy", "cap", "q", "n_seeds", "L_grid",
            "threshold", "wilson_level", "wilson_in_rule"}
    if set(man) - {"study", "notes"} != need:
        raise Refused("manifest keys differ from the protocol")
    if man["schema"] != 1 or man["profile"] != "P1" or man["policy"] != P.POLICY:
        raise Refused("schema/profile/policy differ from the protocol")
    tag = man["tag"]
    if plan == "pilot":
        if not isinstance(tag, str) or tag.startswith(REGISTERED_PREFIX) or tag in FORBIDDEN_TAGS:
            raise Refused("pilot tag must be new (not registered, not a synthetic test tag)")
        if man["frozen_script_sha256"] != P.sha256_file(os.path.abspath(__file__)):
            raise Refused("manifest is not frozen for this script")
        if not isinstance(man["wilson_in_rule"], bool):
            raise Refused("wilson_in_rule must be decided (true/false) before the run")
    elif tag != TEST_TAG:
        raise Refused("the test plan uses only the synthetic test tag")
    g = man["L_grid"]
    if not (isinstance(g, list) and g and all(isinstance(x, int) and not isinstance(x, bool) for x in g)
            and g == sorted(set(g)) and g[0] >= 1):
        raise Refused("L_grid must be a strictly increasing list of positive integers")
    for key in ("N", "k", "cap", "q", "n_seeds"):
        if not (isinstance(man[key], int) and not isinstance(man[key], bool) and man[key] >= 1):
            raise Refused("%s must be a positive integer" % key)
    if man["cap"] < man["q"]:
        raise Refused("cap must be >= q")
    if not (0 < man["threshold"] < 1 and 0 < man["wilson_level"] < 1):
        raise Refused("threshold and wilson_level must lie in (0, 1)")


def make_out(out):
    """A NEW directory outside upload/, records/, dsn/ and evidence/az/scripts/; created atomically (mkdir)."""
    t = os.path.abspath(out)
    for bad in ("upload", "records", "dsn", os.path.join("evidence", "az", "scripts")):
        b = os.path.join(P.ROOT, bad)
        if t == b or t.startswith(b + os.sep):
            raise Refused("output directory inside %s/" % bad)
    if os.path.lexists(t):
        raise Refused("output directory exists; it must be new")
    if not os.path.isdir(os.path.dirname(t)):
        raise Refused("parent of the output directory does not exist")
    os.mkdir(t)
    return t


def write_new(path, text):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    with os.fdopen(fd, "w") as f:
        f.write(text)


# ---------------------------------------------------------------- one seed
def state_id(st):
    return hashlib.sha256(repr(P.fingerprint(st)).encode()).hexdigest()


def replay(peng, ieng, run, N, k, th0, d0, j, Lmax, cap):
    """Independent replay of one seed (own loop, not contact_clock): status, first slot-contact tick, and the
    checkpoint ids of the states at tau_C - 1 and tau_C."""
    st = P.RunState(ieng, run, N, k, th0, d0, Lmax + 1, cap, provenance=True, strict=True)
    while True:
        t = st.u.steps + 1
        if t > Lmax:
            return "no_contact_by_L", None, None, None
        if not K.eligible(st):
            return "terminated_before_contact", None, None, None
        _, _, edges = K.predicted_graph(peng, st)
        if any(st.prov.carrier[j] in e for e in edges):
            id_minus = state_id(st)
            P.tick(ieng, run, st)
            return "contact", t, id_minus, state_id(st)
        it0 = st.iters
        P.tick(ieng, run, st)
        if st.iters == it0:
            return "terminated_before_contact", None, None, None


def verify(peng, ieng, run, r, N, k, th0, d0, j, Lmax, cap):
    """Refuse a clock result unless an independent replay reproduces its status, tau_C, annotations and both
    boundary states (full fingerprints)."""
    status, t, id_minus, id_plus = replay(peng, ieng, run, N, k, th0, d0, j, Lmax, cap)
    if status != r["status"]:
        raise Refused("replay status %s differs from the clock's %s" % (status, r["status"]))
    if status != "contact":
        if r["tau_C"] is not None or r["minus"] is not None:
            raise Refused("a non-contact result carries a contact time or boundary")
        return None, None
    tau = r["tau_C"]
    if not (isinstance(tau, int) and tau == t and 1 <= tau <= Lmax):
        raise Refused("tau_C %r is not the replayed first contact %d" % (tau, t))
    mi, pl = r["minus"], r["plus"]
    if not (mi.landmark_tick == mi.u.steps == tau - 1 and pl.landmark_tick == pl.u.steps == tau):
        raise Refused("boundary annotations do not match tau_C")
    if state_id(mi) != id_minus:
        raise Refused("C- boundary is not the replayed state at tau_C - 1")
    if state_id(pl) != id_plus:
        raise Refused("C+ boundary is not the replayed state at tau_C")
    return id_minus, id_plus


def audit(peng, ieng, run, man, records):
    """Post-hoc audit of stored records: every seed is replayed independently and its status, tau_C and checkpoint
    ids must equal the stored ones; the draw (theta0, delta0, j) must equal the manifest's seed law."""
    bad = []
    for rec in records:
        b = rec["b"]
        _, th0, d0 = run.base_draw(peng, man["tag"], man["N"], man["k"], b)
        j = run.arm_choices(man["tag"], man["N"], man["k"], b)["slot"]
        st, t, im, ip = replay(peng, ieng, run, man["N"], man["k"], th0, d0, j, man["L_grid"][-1], man["cap"])
        if (rec["theta0"], rec["delta0"], rec["j"], rec["status"], rec["tau_C"]) != (th0, d0, j, st, t) or \
                (st == "contact" and (rec["id_minus"], rec["id_plus"]) != (im, ip)):
            bad.append(b)
    return bad


def seed_record(peng, ieng, run, man, b, verifier=None):
    tag, N, k, cap, q = man["tag"], man["N"], man["k"], man["cap"], man["q"]
    Lmax = man["L_grid"][-1]
    _, th0, d0 = run.base_draw(peng, tag, N, k, b)
    j = run.arm_choices(tag, N, k, b)["slot"]
    st = P.RunState(ieng, run, N, k, th0, d0, Lmax + 1, cap, provenance=True, strict=True)
    r = K.contact_clock(peng, ieng, run, st, j, Lmax, q)
    ids = (verifier or verify)(peng, ieng, run, r, N, k, th0, d0, j, Lmax, cap)
    rec = {"b": b, "j": j, "theta0": th0, "delta0": d0, "status": r["status"], "tau_C": r["tau_C"],
           "tau_free": K.tau_free(peng, N, k, th0, d0, j, Lmax)}
    if r["status"] == "contact":
        rec.update(n_edges=len(r["edges"]), carrier_pre=r["carrier_pre"], carrier_plus=r["carrier_plus"],
                   eligible_minus=r["eligible_minus"], eligible_plus=r["eligible_plus"],
                   M_minus=len(r["minus"].u.theta), M_plus=len(r["plus"].u.theta),
                   pos_minus=bool(r["pos_minus"]), pos_plus=bool(r["pos_plus"]),
                   centre_case=bool(r["slot_birth_at_contact"]), id_minus=ids[0], id_plus=ids[1])
    return rec


# ---------------------------------------------------------------- summary and L rule
def wilson(kk, n, level):
    """Wilson score interval for kk successes out of n (two-sided, given level)."""
    z = _z(level)
    if n == 0:
        return (None, None)
    p = kk / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, c - h), min(1.0, c + h))


def _z(level):
    """Standard normal quantile for (1 + level) / 2, by bisection on erf (no external library)."""
    target = (1 + level) / 2
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if 0.5 * (1 + math.erf(mid / math.sqrt(2))) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def summarize(records, man):
    n = len(records)
    if n != man["n_seeds"] or [r["b"] for r in records] != list(range(n)):
        raise Refused("records are not exactly the pre-fixed seeds 0 .. n-1")
    st = {s: sum(1 for r in records if r["status"] == s) for s in ("contact", "no_contact_by_L",
                                                                    "terminated_before_contact")}
    rows = []
    for L in man["L_grid"]:
        hit = [r for r in records if r["status"] == "contact" and r["tau_C"] <= L]
        kk = len(hit)
        lo, hi = wilson(kk, n, man["wilson_level"])
        rows.append({"L": L, "k": kk, "n": n, "F": kk / n, "wilson_lo": lo, "wilson_hi": hi,
                     "eligible_minus": sum(r["eligible_minus"] for r in hit),
                     "eligible_plus": sum(r["eligible_plus"] for r in hit),
                     "eligible_both": sum(r["eligible_minus"] and r["eligible_plus"] for r in hit),
                     "centre_cases": sum(r["centre_case"] for r in hit),
                     "pos_minus": sum(r["pos_minus"] for r in hit), "pos_plus": sum(r["pos_plus"] for r in hit)})
    use_lo = man["wilson_in_rule"] is True
    qual = [row["L"] for row in rows if (row["wilson_lo"] if use_lo else row["F"]) >= man["threshold"]]
    taus = sorted(r["tau_C"] for r in records if r["status"] == "contact")

    def qt(p):
        return taus[min(len(taus) - 1, max(0, math.ceil(p * len(taus)) - 1))] if taus else None
    return {"n": n, "status_counts": st, "rows": rows, "rule": "wilson_lo" if use_lo else "F",
            "threshold": man["threshold"], "L_star": qual[0] if qual else "no qualifying L",
            "tau_C_quantiles": {"min": taus[0] if taus else None, "p50": qt(0.5), "p90": qt(0.9), "p95": qt(0.95),
                                "max": taus[-1] if taus else None},
            "tau_free_differs": sum(1 for r in records if r["status"] == "contact" and r["tau_free"] != r["tau_C"])}


def summary_text(s, man):
    lines = ["AZ fork BASE-only pilot - tag %s, N=%d, k=%d, cap=%d, q=%d, n=%d" % (man["tag"], man["N"], man["k"],
                                                                                  man["cap"], man["q"], s["n"]),
             "status: contact %(contact)d, no_contact_by_L %(no_contact_by_L)d, terminated_before_contact "
             "%(terminated_before_contact)d" % s["status_counts"],
             "%6s %5s %7s %17s %8s %8s %8s %7s %6s %6s" % ("L", "k", "F(L)", "Wilson", "elig C-", "elig C+",
                                                          "both", "centre", "pos-", "pos+")]
    for r in s["rows"]:
        lines.append("%6d %5d %7.4f [%7.4f,%7.4f] %8d %8d %8d %7d %6d %6d" % (
            r["L"], r["k"], r["F"], r["wilson_lo"], r["wilson_hi"], r["eligible_minus"], r["eligible_plus"],
            r["eligible_both"], r["centre_cases"], r["pos_minus"], r["pos_plus"]))
    lines.append("rule: min L with %s >= %s  ->  L* = %s" % (s["rule"], s["threshold"], s["L_star"]))
    lines.append("tau_C quantiles (contacts): %s; tau_free != tau_C in %d contacts" % (
        json.dumps(s["tau_C_quantiles"], sort_keys=True), s["tau_free_differs"]))
    return "\n".join(lines) + "\n"


def run_pilot(man, out, peng, ieng, run, plan):
    check_manifest(man, plan)
    d = make_out(out)
    recs, timing = [], []
    for b in range(man["n_seeds"]):
        t0 = time.perf_counter()
        recs.append(seed_record(peng, ieng, run, man, b))
        timing.append("%d %.4f" % (b, time.perf_counter() - t0))
    s = summarize(recs, man)
    write_new(os.path.join(d, "seeds.jsonl"), "".join(json.dumps(r, sort_keys=True) + "\n" for r in recs))
    write_new(os.path.join(d, "summary.json"), json.dumps(s, sort_keys=True, indent=1) + "\n")
    write_new(os.path.join(d, "summary.txt"), summary_text(s, man))
    write_new(os.path.join(d, "timing.txt"), "\n".join(timing) + "\n")
    sums = "".join("%s  %s\n" % (P.sha256_file(os.path.join(d, f)), f) for f in DETERMINISTIC + ("timing.txt",))
    write_new(os.path.join(d, "SHA256SUMS"), sums)
    return d, s


def load_engines(prefix):
    run = P.load_runner()
    peng = P.load_engine(prefix + "_plain")
    ieng = P.load_engine(prefix + "_instr")
    P.install(ieng)
    return peng, ieng, run


# ================================================================ self-test (synthetic tag only)
def test_manifest(n=16):
    return {"schema": 1, "frozen_script_sha256": None, "tag": TEST_TAG, "N": 120, "k": 8, "profile": "P1",
            "policy": P.POLICY, "cap": 300, "q": 100, "n_seeds": n, "L_grid": [100, 200, 400, 800],
            "threshold": 0.95, "wilson_level": 0.95, "wilson_in_rule": False}


def selftest(n=16, verbose=True):
    check_pins()
    peng, ieng, run = load_engines("plt")
    C = P.Checks()
    say = print if verbose else (lambda *a: None)
    import tempfile
    tmp = tempfile.mkdtemp(prefix="az_base_pilot_selftest_")       # a fresh directory per self-test run

    def refused(fn):
        try:
            fn()
            return False
        except (Refused, ValueError):
            return True

    # ---- A. L rule on hand-made records (denominator = all seeds; no automatic L_max)
    def recs(taus, extra_nc=0, extra_term=0):
        out = []
        for i, t in enumerate(taus):
            out.append({"b": i, "status": "contact", "tau_C": t, "tau_free": t, "eligible_minus": True,
                        "eligible_plus": True, "centre_case": False, "pos_minus": False, "pos_plus": False})
        for i in range(extra_nc):
            out.append({"b": len(out), "status": "no_contact_by_L", "tau_C": None, "tau_free": None})
        for i in range(extra_term):
            out.append({"b": len(out), "status": "terminated_before_contact", "tau_C": None, "tau_free": None})
        return out
    m = test_manifest(20)
    s = summarize(recs([1] * 16 + [100, 150, 300], extra_nc=1), m)
    C.ok([r["k"] for r in s["rows"]] == [17, 18, 19, 19] and s["rows"][2]["F"] == 19 / 20 and s["L_star"] == 400,
         "A1 20 seeds, contacts at 1 (x16), 100 (= L, counted), 150, 300 and one no-contact seed: k(L) = 17, 18, 19, 19; "
         "F(400) = 19/20 >= 0.95, so L* = 400 (the no-contact seed counts in the denominator)")
    s = summarize(recs([1] * 16 + [100, 150, 300], extra_nc=1), dict(m, threshold=0.96))
    C.ok(s["L_star"] == "no qualifying L", "A2 same records, threshold 0.96: 'no qualifying L'")
    s = summarize(recs([1] * 17, extra_nc=2, extra_term=1), m)
    C.ok(s["L_star"] == "no qualifying L" and s["rows"][-1]["F"] == 17 / 20,
         "A3 17/20 at every L: 'no qualifying L' (no automatic L = 800); terminated seeds stay in the denominator")
    s = summarize(recs([1] * 20), dict(m, wilson_in_rule=True))
    lo, hi = wilson(20, 20, 0.95)
    z = 1.959963984540054
    lo_ref = (1 + z * z / 40 - z * math.sqrt(z * z / 1600)) / (1 + z * z / 20)
    C.ok(abs(lo - lo_ref) < 1e-9 and hi == 1.0 and s["rule"] == "wilson_lo" and s["L_star"] == "no qualifying L",
         "A4 Wilson bound (z = 1.96): 20/20 gives lower bound %.4f < 0.95, so with wilson_in_rule the rule does not "
         "qualify" % lo)
    C.ok(refused(lambda: summarize(recs([1] * 19), m)) and refused(lambda: summarize(
        [dict(r, b=r["b"] + 1) for r in recs([1] * 20)], m)),
         "A5 summary refuses a record set that is not exactly the pre-fixed seeds 0 .. n-1")

    # ---- B. manifest and output gates
    man = test_manifest()
    C.ok(refused(lambda: check_manifest(dict(man, tag="AZ-FORK-BASEPILOT-P1"), "test")),
         "B1 the test plan refuses any tag but the synthetic test tag (pilot seeds are never touched by tests)")
    pm = dict(man, tag="AZ-FORK-BASEPILOT-P1")
    C.ok(refused(lambda: check_manifest(pm, "pilot")),
         "B2 the pilot plan refuses a manifest that is not frozen for this script")
    frozen = dict(pm, frozen_script_sha256=P.sha256_file(os.path.abspath(__file__)))
    C.ok(refused(lambda: check_manifest(dict(frozen, wilson_in_rule=None), "pilot")) and
         not refused(lambda: check_manifest(frozen, "pilot")),
         "B3 the pilot plan refuses wilson_in_rule = null and accepts a frozen, decided manifest")
    C.ok(all(refused(lambda t=t: check_manifest(dict(frozen, tag=t), "pilot"))
             for t in ("AZ-TOKRES-S1", "AZ-TOKRES-S2", "AZ-FORK-CLOCK-SYNTH", TEST_TAG)),
         "B4 the pilot plan refuses registered and synthetic tags")
    C.ok(refused(lambda: check_manifest(dict(man, L_grid=[200, 100]), "test")) and
         refused(lambda: check_manifest(dict(man, cap=50), "test")) and
         refused(lambda: check_manifest(dict(man, extra=1), "test")),
         "B5 manifest refuses an unsorted grid, cap < q and unknown keys")
    C.ok(refused(lambda: make_out(os.path.join(P.ROOT, "upload", "x"))) and
         refused(lambda: make_out(os.path.join(P.ROOT, "records", "x"))) and
         refused(lambda: make_out(tmp)),
         "B6 output refused inside upload/ or records/, and when the directory already exists")

    # ---- C. verification of the clock output (forged or mismatched results are refused)
    seeds = []
    for b in range(40):
        _, th0, d0 = run.base_draw(peng, TEST_TAG, 120, 8, b)
        j = run.arm_choices(TEST_TAG, 120, 8, b)["slot"]
        st = P.RunState(ieng, run, 120, 8, th0, d0, 801, 300, provenance=True, strict=True)
        r = K.contact_clock(peng, ieng, run, st, j, 800, 100)
        if r["status"] == "contact" and r["tau_C"] >= 2:
            seeds.append((b, th0, d0, j, r))
        if len(seeds) >= 3:
            break
    b, th0, d0, j, r = seeds[0]
    ok = verify(peng, ieng, run, r, 120, 8, th0, d0, j, 800, 300)
    C.ok(ok == (state_id(r["minus"]), state_id(r["plus"])),
         "C1 a genuine clock result is verified; its C-/C+ checkpoint ids are returned")
    forged = dict(r, tau_C=r["tau_C"] + 1)
    swapped = dict(r, minus=r["plus"])
    other = dict(r, minus=seeds[1][4]["minus"])
    ann = dict(r, minus=P.copy.deepcopy(r["minus"]))
    ann["minus"].landmark_tick += 1
    C.ok(all(refused(lambda x=x: verify(peng, ieng, run, x, 120, 8, th0, d0, j, 800, 300))
             for x in (forged, swapped, other, ann, dict(r, status="no_contact_by_L"))),
         "C2 refused: forged tau_C, swapped C-/C+, a boundary from another seed, a wrong annotation, a wrong status")
    for L in (r["tau_C"], 800):
        st = P.RunState(ieng, run, 120, 8, th0, d0, L + 1, 300, provenance=True, strict=True)
        rL = K.contact_clock(peng, ieng, run, st, j, L, 100)
        C.ok(rL["tau_C"] == r["tau_C"] and rL["eligible_plus"] == r["eligible_plus"]
             and P.canon(rL["minus"].u) == P.canon(r["minus"].u)
             and P.canon(rL["minus"].prov) == P.canon(r["minus"].prov),
             "C3 seed %d: tau_C, C+ eligibility and the C- state (engine and provenance; T_ref differs by design) "
             "are the same with L = %d (T_ref = L + 1) as with L_max = 800" % (b, L))

    # ---- D. end-to-end test plan, twice: deterministic outputs
    outs = []
    for rep in (1, 2):
        d, s = run_pilot(test_manifest(n), os.path.join(tmp, "run%d" % rep), peng, ieng, run, "test")
        outs.append(d)
    same = all(open(os.path.join(outs[0], f), "rb").read() == open(os.path.join(outs[1], f), "rb").read()
               for f in DETERMINISTIC)
    C.ok(same, "D1 two test-plan runs (%d seeds): seeds.jsonl, summary.json, summary.txt byte-identical" % n)
    recs1 = [json.loads(x) for x in open(os.path.join(outs[0], "seeds.jsonl"))]
    C.ok(all(x["status"] != "contact" or (x["id_minus"] and x["id_plus"]) for x in recs1) and len(recs1) == n,
         "D2 every contact record carries verified C-/C+ checkpoint ids")
    C.ok(audit(peng, ieng, run, test_manifest(n), recs1) == [],
         "D4 post-hoc audit: an independent replay of every stored seed reproduces its draw, status, tau_C and "
         "checkpoint ids")
    tampered = [dict(x, tau_C=x["tau_C"] + 1) if x["b"] == 0 and x["status"] == "contact" else x for x in recs1]
    C.ok(audit(peng, ieng, run, test_manifest(n), tampered) == [0], "D5 the audit flags a tampered stored tau_C")
    say(open(os.path.join(outs[0], "summary.txt")).read().rstrip())
    root_files = sorted({p for p in K.OPENED if p.startswith(P.ROOT + os.sep)})
    allowed = {P.ENGINE, P.ORIENT, P.RUNNER, K.LIB, os.path.join(HERE, "az_tokres_contact_clock.py"),
               os.path.abspath(__file__)}

    def permitted(p):
        if p in allowed:
            return True
        dd, bb = os.path.split(p)
        return os.path.basename(dd) == "__pycache__" and any(
            os.path.dirname(dd) == os.path.dirname(a) and bb.startswith(os.path.splitext(os.path.basename(a))[0] + ".")
            for a in allowed)
    C.ok(all(permitted(p) for p in root_files) and not any("/upload/az-token-resonance" in p for p in K.OPENED),
         "D3 repository files opened: only the pinned engine, orientation, runner, provenance library, clock and "
         "this script (%d paths); nothing under upload/az-token-resonance-*" % len(root_files))
    say("checks: %d, failed: %d" % (C.n, C.bad))
    say("SELFTEST PASS" if C.bad == 0 else "SELFTEST FAIL")
    return 0 if C.bad == 0 else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--manifest")
    ap.add_argument("--out")
    ap.add_argument("--audit", help="stored pilot output directory to re-verify against the manifest")
    a = ap.parse_args()
    if a.audit and a.manifest:
        check_pins()
        with open(a.manifest) as f:
            man = json.load(f)
        peng, ieng, run = load_engines("audit")
        recs = [json.loads(x) for x in open(os.path.join(a.audit, "seeds.jsonl"))]
        bad = audit(peng, ieng, run, man, recs)
        print("AUDIT %s: %d records, %d mismatching %s" % ("PASS" if not bad else "FAIL", len(recs), len(bad), bad[:20]))
        return 0 if not bad else 1
    if a.selftest:
        return selftest()
    if not (a.run and a.manifest and a.out):
        print(__doc__)
        return 2
    try:
        check_pins()
        with open(a.manifest) as f:
            man = json.load(f)
        peng, ieng, run = load_engines("pilot")
        d, s = run_pilot(man, a.out, peng, ieng, run, "pilot")
    except Refused as e:
        print("REFUSED:", e)
        return 3
    print(summary_text(s, man), end="")
    print("outputs:", d)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
