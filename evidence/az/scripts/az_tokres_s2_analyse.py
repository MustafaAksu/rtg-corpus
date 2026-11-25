#!/usr/bin/env python3
"""AZ token-resonance Stage 2 analysis - [SESSION] NONCANONICAL; implements the registered analysis plan of
records/az/AZ_TOKEN_RESONANCE_STAGE2_PREREGISTRATION.md section 6 and nothing else. Standard library only; deterministic.

It uses the Stage 1 analysis script as a library, unchanged and hash-pinned (state re-derivation, record checks, custody
checks, fixtures-log gate, paired statistics). What is new here is registered in this file: the Stage 2 cells, their
horizons and thresholds, the two endpoints, the family of ten and its readings, and the descriptive outputs.

FAIL-CLOSED, as in Stage 1. Nothing is estimated until every input has passed:
  identity, custody, states, records, set   per cell, by the Stage 1 validator (unchanged);
  Stage 2 record checks                     the tick-800 checkpoint exists unless the run reached the cap before it;
  pilot files                               the three pilot record files hash to the registered values.
Any failure prints the errors, no estimate and no reading, exit code 2.
Gates: G1 fixtures log of the campaign machine; G2 law-violation counter zero. A failed gate: exit code 3.

Endpoints (both from the same run; M never decreases)
  E_theta   Y = 1{M >= theta(N)} when the run stops (at the registered horizon T(N), or at the cap of 300)
  E_100     Y = 1{M >= 100 at tick 800}: the Stage 1 endpoint. A run that reached the cap before tick 800 has no
            tick-800 checkpoint and is positive; such runs are counted and reported.

Family of ten (the only confirmatory family): five contrasts (resonant value against its +-1 neighbour, paired on the
base draw) x two endpoints.
  tests of RD = 0      exact two-sided McNemar, Holm over the ten;
  minimum effect       simultaneous two-sided intervals for RD at 1 - 0.05/10 = 99.5 % each (Bonferroni; Agresti-Min
                       adjusted Wald for matched proportions - an approximation, unlike the exact McNemar test);
  reading              SUPPORTED: Holm p < 0.05 and lower limit > 0.05; NOT SUPPORTED AT THE REGISTERED SIZE: upper
                       limit < 0.05; otherwise INCONCLUSIVE.
The familywise guarantee for "RD > 0.05" rests on the simultaneous intervals, not on Holm.

usage
  python -I az_tokres_s2_analyse.py --plan stage2 --dir OUT --engine E --orient O --runner R --analysis-s1 A
         --fixtures-log LOG --pilot-dir PILOT [--exclude-base S2-C240:17,S2-C480:203]
  python -I az_tokres_s2_analyse.py --plan s2test --dir OUT ... (--pilot-dir optional; no evidential value)
  python -I az_tokres_s2_analyse.py --check-pilot PILOT      (hashes and structure only; tabulates no outcome)
  python -I az_tokres_s2_analyse.py --selftest --analysis-s1 A
Exit codes: 0 analysis printed; 2 integrity failure; 3 gate failure; 1 self-test failure.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import importlib.util
import json
import math
import os
import sys
import tempfile
from collections import Counter, defaultdict

# ------------------------------------------------------------------ registered constants
S1_ANALYSIS_SHA256 = "490b3d4f06ef52d6d39b217d0821bd8361d0a8ed37941f32f9c154113c91dc80"
ENGINE_SHA256 = "4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608"
ORIENT_SHA256 = "ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c"
RUNNER_SHA256 = "75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992"
PILOT_SCRIPT_SHA256 = "ccc9e776fc5586d8636d7d4b00da3c537e6661428c82332d8f3141870b9e9a95"
PILOT_TAG = "S2-CALIB-PILOT-20261112"
PILOT_ALPHA = (14, 2620)               # reference rate of the pilot: non-resonant native draws with M >= 100 at N = 120
DELTA_STAR = 0.05                      # registered minimal risk difference (as in Stage 1)
DELTA_NEUTRAL = 0.025                  # registered neutrality margin of the control contrasts G4, G5 (as in Stage 1)
FAMILY_SIZE = 10
Z_FAMILY = 2.8070337683438114          # two-sided 99.5 % = 1 - 0.05/10 (Bonferroni over the family of ten)
Z_95 = 1.959963984540054
Y100, TICK = 100, 800                  # the Stage 1 endpoint
LADDER = (60, 80, 100, 150, 200, 300)
LOW_ORDER = 6                          # cut of the descriptive order breakdown (chosen post hoc on the pilot)
_S2 = {"tag": "AZ-TOKRES-S2", "cap": 300, "policy": "bound_symmetric", "profile": "P1", "confirmatory": True, "n_base": 1500}
_T2 = {"tag": "S2SMOKE", "cap": 300, "policy": "bound_symmetric", "profile": "P1", "confirmatory": False}
REGISTRY = {
    # Stage 2 (preregistration section 5). theta and T: pilot intake section 4; band: intake section 5.
    "S2-C240": dict(_S2, N=240, k=16, T=1460, theta=106, band=(92, 127), n_perm=200,
                    pilot_file="N240k16T1460.jsonl", pilot_sha256="f4ab8c57733ee0ed8d60ba62de6672785c954353ab5092f8ab27fd7d56fd86cf"),
    "S2-C242": dict(_S2, N=242, k=16, T=1460, theta=84, band=(78, 98), n_perm=0,
                    pilot_file="N242k16T1460.jsonl", pilot_sha256="baeb4640d7f30f8491f76b2a3309c3e3b44e58374869573b650ade256ae482ec"),
    "S2-C480": dict(_S2, N=480, k=32, T=2670, theta=114, band=(104, 131), n_perm=200,
                    pilot_file="N480k32T2670.jsonl", pilot_sha256="18233c683617d81bfb3f81e7f1b9c7e3d176c2f41a6cdffd9943ada23304c877"),
    # Test configuration (tag S2SMOKE): instrument validation and negative controls only; no evidential value.
    "T2-C240": dict(_T2, N=240, k=16, T=900, theta=45, band=(40, 50), n_base=10, n_perm=2, pilot_file="N240k16T900.jsonl", pilot_sha256=None),
    "T2-C242": dict(_T2, N=242, k=16, T=900, theta=45, band=(40, 50), n_base=8, n_perm=0, pilot_file="N242k16T900.jsonl", pilot_sha256=None),
    "T2-C480": dict(_T2, N=480, k=32, T=900, theta=45, band=(40, 50), n_base=6, n_perm=2, pilot_file="N480k32T900.jsonl", pilot_sha256=None),
}
PLANS = {"stage2": ("S2-C240", "S2-C242", "S2-C480"), "s2test": ("T2-C240", "T2-C242", "T2-C480")}
# the five contrasts, in the fixed order of the family: (cell index in the plan, label, resonant arm, detuned arm)
CONTRASTS = ((0, "order 1 (2x = 0)", "O1R", "O1D"), (0, "order 2 (2x = N/2)", "O2R", "O2D"),
             (1, "order 1 (2x = 0)", "O1R", "O1D"),
             (2, "order 1 (2x = 0)", "O1R", "O1D"), (2, "order 2 (2x = N/2)", "O2R", "O2D"))
ENDPOINTS = ("E_theta", "E_100")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_s1(path: str):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("az_tokres_analyse", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ------------------------------------------------------------------ endpoints
def m800(r: dict) -> int:
    """Node count at tick 800. A run stopped at the cap before tick 800 has no checkpoint there; M never decreases,
    so its value at tick 800 would be at least its final M (>= cap)."""
    at = r["M_at"]
    return at[str(TICK)] if str(TICK) in at else r["M"]


def cap_before_800(r: dict) -> bool:
    return str(TICK) not in r["M_at"]


def y_theta(r: dict, theta: int) -> int:
    return int(r["M"] >= theta)


def y_100(r: dict) -> int:
    return int(m800(r) >= Y100)


def s2_record_errors(r: dict, cfg: dict) -> list:
    """Stage 2 checks on top of the Stage 1 record checks: the tick-800 checkpoint."""
    e = []
    try:
        at, steps = r["M_at"], r["steps"]
        if not isinstance(at, dict) or not all(isinstance(v, int) for v in at.values()):
            return ["M_at is not a mapping to integers"]
        if str(TICK) in at:
            if steps < TICK:
                e.append("tick-800 checkpoint present although the run stopped before tick 800")
            if at[str(TICK)] > r["M"]:
                e.append("tick-800 checkpoint above the final M")
        else:
            if not (r["hit_cap"] is True and steps < TICK and r["M"] >= cfg["cap"]):
                e.append("no tick-800 checkpoint although the run did not reach the cap before tick 800")
    except (KeyError, TypeError) as ex:
        e.append("malformed record: %r" % (ex,))
    return e


# ------------------------------------------------------------------ small statistics not in the Stage 1 library
def binom_cdf(k: int, n: int, p: float) -> float:
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    if p <= 0.0:
        return 1.0
    if p >= 1.0:
        return 0.0
    lp, lq = math.log(p), math.log1p(-p)
    return min(1.0, sum(math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) + i * lp + (n - i) * lq)
                        for i in range(k + 1)))


def clopper_pearson(x: int, n: int, conf: float = 0.95):
    """Exact two-sided binomial interval."""
    if n == 0:
        return (float("nan"), float("nan"))
    a = (1 - conf) / 2

    def solve(f):
        lo, hi = 0.0, 1.0
        for _ in range(100):
            mid = (lo + hi) / 2
            if f(mid):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    lower = 0.0 if x == 0 else solve(lambda p: 1 - binom_cdf(x - 1, n, p) < a)
    upper = 1.0 if x == n else solve(lambda p: binom_cdf(x, n, p) > a)
    return lower, upper


def sign_test(gt: int, lt: int) -> float:
    """Exact two-sided sign test on the non-tied pairs."""
    m = gt + lt
    if m == 0:
        return 1.0
    lo = min(gt, lt)
    return min(1.0, 2 * sum(math.comb(m, i) for i in range(lo + 1)) / 2 ** m)


def median(vals):
    v = sorted(vals)
    if not v:
        return float("nan")
    h = len(v) // 2
    return v[h] if len(v) % 2 else (v[h - 1] + v[h]) / 2


def ord2(x: int, N: int) -> int:
    """Additive order of 2x in Z_N: 1 and 2 are the resonant classes."""
    y = (2 * x) % N
    return N // math.gcd(y, N) if y else 1


def reading(res: dict, p_holm: float) -> str:
    if res["n"] == 0:
        return "INCONCLUSIVE (no pairs)"
    if p_holm < 0.05 and res["lo"] > DELTA_STAR:
        return "SUPPORTED (Holm p < 0.05 and simultaneous lower limit > %.2f)" % DELTA_STAR
    if res["hi"] < DELTA_STAR:
        return "NOT SUPPORTED AT THE REGISTERED SIZE (simultaneous upper limit < %.2f)" % DELTA_STAR
    return "INCONCLUSIVE (simultaneous interval contains %.2f)" % DELTA_STAR


# ------------------------------------------------------------------ pilot files (native draws; descriptive supplement)
PILOT_KEYS = ("N", "k", "T", "arm", "base", "d0", "native_class", "M", "hit_cap", "steps", "M_at", "law_viol")


def pilot_structure_errors(r: dict, cfg: dict, registered: bool) -> list:
    """Structure and identity of one pilot record. Evaluates no outcome."""
    e = []
    if any(q not in r for q in PILOT_KEYS):
        return ["missing field(s) %s" % [q for q in PILOT_KEYS if q not in r]]
    if (r["N"], r["k"], r["T"], r["arm"]) != (cfg["N"], cfg["k"], cfg["T"], "BASE"):
        e.append("cell identity differs")
    if registered and (r.get("tag") != PILOT_TAG or r.get("engine_sha256") != ENGINE_SHA256 or r.get("orient_sha256") != ORIENT_SHA256
                       or r.get("runner_sha256") != RUNNER_SHA256 or r.get("pilot_sha256") != PILOT_SCRIPT_SHA256):
        e.append("tag or pinned hashes differ")
    if not (isinstance(r["M"], int) and isinstance(r["steps"], int) and isinstance(r["hit_cap"], bool)
            and isinstance(r["law_viol"], int) and isinstance(r["native_class"], str) and isinstance(r["base"], int)):
        e.append("field types")
    if not (isinstance(r["M_at"], dict) and all(isinstance(v, int) for v in r["M_at"].values())):
        e.append("M_at is not a mapping to integers")
    if not (isinstance(r["d0"], list) and len(r["d0"]) == 4 and all(isinstance(x, int) for x in r["d0"])):
        e.append("d0 is not four integers")
    return e


def load_pilot(pilot_dir: str, cfg: dict, s1, registered: bool):
    """Return (records, errors). The file must hash to the registered value (registered cells); every record must
    have the pilot's structure and identity, and its class label must equal a re-derivation from its seed tokens."""
    path = os.path.join(pilot_dir, cfg["pilot_file"])
    if not os.path.exists(path):
        return None, ["pilot file %s missing" % cfg["pilot_file"]]
    if cfg["pilot_sha256"] is not None and sha256_file(path) != cfg["pilot_sha256"]:
        return None, ["pilot file %s does not hash to the registered value" % cfg["pilot_file"]]
    recs, errors = [], []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            try:
                r = json.loads(line)
            except ValueError:
                errors.append("%s:%d unreadable" % (cfg["pilot_file"], i + 1))
                continue
            bad = pilot_structure_errors(r, cfg, registered)
            if not bad and r["base"] != i:
                bad.append("draw index out of order")
            if not bad and r["native_class"] != s1.alphabet_class(r["d0"], cfg["N"]):
                bad.append("class label differs from its seed tokens")
            if bad:
                if len(errors) < 20:
                    errors.append("%s:%d %s" % (cfg["pilot_file"], i + 1, "; ".join(bad)))
                continue
            recs.append(r)
    return recs, errors


# ------------------------------------------------------------------ the registered analysis
def fmt(res: dict) -> str:
    return ("n=%d  p1=%.4f  p0=%.4f  RD=%+.4f [%+.4f, %+.4f]  discordant %d/%d  McNemar p=%.3e"
            % (res["n"], res["p1"], res["p0"], res["rd"], res["lo"], res["hi"], res["only1"], res["only0"], res["p_mcnemar"]))


def analyse(s1, plan: str, data: dict, pilots: dict, exclude: dict, out=sys.stdout):
    """data[cell] = rows[base][arm]; pilots[cell] = list of pilot records or None."""
    w = lambda s="": print(s, file=out)
    cells = PLANS[plan]
    test = plan != "stage2"
    label = "test-configuration reading, no evidential value" if test else "registered reading"
    B, Yt, Y1 = {}, {}, {}
    for c in cells:
        cfg = REGISTRY[c]
        arms = s1.arms_for(cfg["N"])
        B[c] = [b for b in sorted(data[c]) if b not in exclude.get(c, ()) and all(a in data[c][b] for a in arms)]
        Yt[c] = {a: [y_theta(data[c][b][a], cfg["theta"]) for b in B[c]] for a in arms}
        Y1[c] = {a: [y_100(data[c][b][a]) for b in B[c]] for a in arms}
        w("cell %s  N=%d k=%d  horizon T=%d  theta=%d  base draws analysed=%d  excluded=%s"
          % (c, cfg["N"], cfg["k"], cfg["T"], cfg["theta"], len(B[c]), sorted(exclude.get(c, ()))))
    Y = {"E_theta": Yt, "E_100": Y1}
    edesc = {"E_theta": "M >= theta(N) at the registered horizon", "E_100": "M >= 100 at tick 800 (the Stage 1 endpoint)"}

    # ---- controls (qualifiers), per cell and endpoint
    quals = defaultdict(list)          # (cell, endpoint) -> [(name, status, detail)]
    g3 = {}
    key = lambda r: (r["M"], r["births"], r["steps"], r["fb"], json.dumps(r["M_at"], sort_keys=True))
    for c in cells:
        cfg, rows = REGISTRY[c], data[c]
        if cfg["n_perm"]:
            tot = bad = 0
            for b in B[c]:
                for a in ("BASE", "O1R"):
                    if a + "_P" in rows[b]:
                        tot += 1
                        bad += key(rows[b][a]) != key(rows[b][a + "_P"])
            g3[c] = ("PASS" if tot and bad == 0 else "FAIL", "%d of %d permuted runs differ in (M, births, steps, fb, M_at)" % (bad, tot))
        nr = lambda b, arm, rows=rows: rows[b][arm]["slot_class"] == "NR"
        for e in ENDPOINTS:
            def sub(a1, a0, keep, c=c, e=e):
                idx = [i for i, b in enumerate(B[c]) if keep(b)]
                return s1.paired([Y[e][c][a1][i] for i in idx], [Y[e][c][a0][i] for i in idx], Z_95)
            if c in g3:
                quals[(c, e)].append(("G3 node-label permutation",) + g3[c])
            sham = sub("SHAM", "BASE", lambda b: nr(b, "BASE") and nr(b, "SHAM"))
            quals[(c, e)].append(("G4 sham perturbation vs BASE (native and perturbed slot token non-resonant)",
                                  s1.equivalence(sham, DELTA_NEUTRAL), fmt(sham)))
            for a in ("O1D", "O2D"):
                if a in Y[e][c]:
                    det = sub(a, "BASE", lambda b: nr(b, "BASE"))
                    quals[(c, e)].append(("G5 detuned arm %s vs BASE (native slot token non-resonant)" % a,
                                          s1.equivalence(det, DELTA_NEUTRAL), fmt(det)))
    w("\n[control contrasts, per cell and endpoint; Agresti-Min intervals 95 %%, not adjusted for multiplicity; "
      "neutrality margin +-%.3f; readings EQUIVALENT / DIFFERENT / INCONCLUSIVE]" % DELTA_NEUTRAL)
    for c in cells:
        for e in ENDPOINTS:
            w("%s, %s:" % (c, e))
            for name, status, detail in quals[(c, e)]:
                w("  %s: %s\n      %s" % (name, status, detail))

    def qualifier_line(c, e, relevant):
        notes = [("%s %s" % (n.split()[0], s)) for n, s, _ in quals[(c, e)]
                 if s not in ("PASS", "EQUIVALENT") and any(n.startswith(q) for q in relevant)]
        if exclude.get(c):
            notes.append("DEVIATION: base draws excluded")
        return ("UNQUALIFIED (every control of this cell and endpoint reads PASS or EQUIVALENT)" if not notes
                else "QUALIFIED BY " + "; ".join(notes))

    # ---- the family of ten
    w("\n[the confirmatory family: five contrasts x two endpoints = %d; paired on the base draw]" % FAMILY_SIZE)
    w("[tests of RD = 0: exact two-sided McNemar, Holm over the ten]")
    w("[minimum effect: simultaneous Agresti-Min intervals, 99.5 % two-sided each (Bonferroni over the ten; approximate)]")
    fam = []
    for e in ENDPOINTS:
        for ci, olabel, a1, a0 in CONTRASTS:
            c = cells[ci]
            fam.append((e, c, olabel, a1, a0, s1.paired(Y[e][c][a1], Y[e][c][a0], Z_FAMILY)))
    assert len(fam) == FAMILY_SIZE
    adj = s1.holm([x[5]["p_mcnemar"] for x in fam])
    verdict = {}
    for (e, c, olabel, a1, a0, res), pa in zip(fam, adj):
        text = reading(res, pa)
        verdict[(c, a1, e)] = text.split(" (")[0]
        w("%s | %s N=%d | %s | %s vs %s\n    %s  Holm p=%.3e" % (e, c, REGISTRY[c]["N"], olabel, a1, a0, fmt(res), pa))
        w("    %s: %s" % (label, text))
        w("    qualifiers: %s" % qualifier_line(c, e, ("G3", "G4", "G5 detuned arm %s" % a0)))
    w("\n[the two endpoints of each contrast, side by side]")
    for ci, olabel, a1, a0 in CONTRASTS:
        c = cells[ci]
        w("%s N=%d %s: E_theta %s; E_100 %s" % (c, REGISTRY[c]["N"], olabel, verdict[(c, a1, "E_theta")], verdict[(c, a1, "E_100")]))

    # ---- near-quarter control (N = 2 mod 4), separate from the family
    for c in cells:
        if "Q2R" in Yt[c]:
            w("\n[near-quarter control at N=%d, separate from the family: Q2R vs BASE; Agresti-Min interval 99.5 %% two-sided; "
              "equivalence margin +-%.2f]" % (REGISTRY[c]["N"], DELTA_STAR))
            for e in ENDPOINTS:
                r = s1.paired(Y[e][c]["Q2R"], Y[e][c]["BASE"], Z_FAMILY)
                eq = s1.equivalence(r, DELTA_STAR)
                w("%s | Q2R vs BASE (no order-2 token exists)\n    %s" % (e, fmt(r)))
                w("    %s: %s" % (label, {"EQUIVALENT": "EQUIVALENT TO BASE within +-%.2f" % DELTA_STAR,
                                           "DIFFERENT": "DIFFERENT FROM BASE by more than %.2f" % DELTA_STAR,
                                           "INCONCLUSIVE": "INCONCLUSIVE (interval neither inside nor outside +-%.2f)" % DELTA_STAR}[eq]))
                w("    qualifiers: %s" % qualifier_line(c, e, ("G3", "G4")))

    # ---- descriptive outputs
    w("\n[descriptive outputs; nominal 95 %; no reading and no decision is attached to any of them]")
    w("D1  the contrasts at the two band thresholds of the pilot (intake section 5):")
    for ci, olabel, a1, a0 in CONTRASTS:
        c = cells[ci]
        for th in REGISTRY[c]["band"]:
            r = s1.paired([y_theta(data[c][b][a1], th) for b in B[c]], [y_theta(data[c][b][a0], th) for b in B[c]], Z_95)
            w("      %s %s vs %s, M >= %3d: %s" % (c, a1, a0, th, fmt(r)))
    w("D2  threshold ladder, rate of M >= c by arm: at the end of the run / at tick 800:")
    for c in cells:
        arms = s1.arms_for(REGISTRY[c]["N"])
        n = len(B[c])
        for th in LADDER:
            w("      %s c=%3d  " % (c, th) + "  ".join("%s %.4f/%.4f" % (
                a, sum(int(data[c][b][a]["M"] >= th) for b in B[c]) / n, sum(int(m800(data[c][b][a]) >= th) for b in B[c]) / n) for a in arms))
    w("D3  threshold-free paired comparison of M, resonant against detuned (exact sign test on non-tied pairs; M is capped at 300):")
    for ci, olabel, a1, a0 in CONTRASTS:
        c = cells[ci]
        for name, f in (("end of run", lambda r: r["M"]), ("tick 800", m800)):
            d = [f(data[c][b][a1]) - f(data[c][b][a0]) for b in B[c]]
            gt, lt = sum(1 for x in d if x > 0), sum(1 for x in d if x < 0)
            w("      %s %s vs %s, %-10s: greater %d, smaller %d, equal %d; sign test p=%.3e; median difference %s"
              % (c, a1, a0, name, gt, lt, len(d) - gt - lt, sign_test(gt, lt), median(d)))
    a_x, a_n = PILOT_ALPHA
    a_lo, a_hi = clopper_pearson(a_x, a_n)
    w("D4  out-of-sample check of the pilot calibration (BASE arm, draws without a resonant seed token). Report only: "
      "the thresholds are registered constants and are not changed by this output.")
    w("      pilot reference rate alpha = %d/%d = %.5f, exact 95 %% [%.5f, %.5f]" % (a_x, a_n, a_x / a_n, a_lo, a_hi))
    for c in cells:
        nrb = [data[c][b]["BASE"] for b in B[c] if data[c][b]["BASE"]["alphabet_class"] == "NR"]
        x = sum(y_theta(r, REGISTRY[c]["theta"]) for r in nrb)
        lo, hi = clopper_pearson(x, len(nrb))
        x1 = sum(y_100(r) for r in nrb)
        lo1, hi1 = clopper_pearson(x1, len(nrb))
        rate = x / len(nrb) if nrb else float("nan")
        w("      %s: M >= %d at the end: %d of %d = %.5f, exact 95 %% [%.5f, %.5f]; point estimate %s the pilot interval of alpha; "
          "M >= 100 at tick 800: %d of %d, exact 95 %% [%.5f, %.5f]"
          % (c, REGISTRY[c]["theta"], x, len(nrb), rate, lo, hi, "inside" if a_lo <= rate <= a_hi else "outside", x1, len(nrb), lo1, hi1))
    w("D5  native decomposition P(Y) = p0 + P(R) (p1 - p0), from native (BASE) draws only: R = at least one seed token with 4x = 0.")
    w("    The risks of the intervention arms are not used in it. Wilson 95 % intervals.")
    for c in cells:
        cfg = REGISTRY[c]
        nres = 4 if cfg["N"] % 4 == 0 else 2
        pr_theory = 1 - (1 - nres / cfg["N"]) ** 4
        base = [data[c][b]["BASE"] for b in B[c]]
        pil = pilots.get(c)
        for e, yf in (("E_theta", lambda r, th=cfg["theta"]: y_theta(r, th)), ("E_100", y_100)):
            n0 = sum(1 for r in base if r["alphabet_class"] == "NR")
            n1 = len(base) - n0
            x0 = sum(yf(r) for r in base if r["alphabet_class"] == "NR")
            x1 = sum(yf(r) for r in base if r["alphabet_class"] != "NR")
            p0 = x0 / n0 if n0 else float("nan")
            p1 = x1 / n1 if n1 else float("nan")
            pr = n1 / len(base)
            lo0, hi0 = s1.wilson(x0, n0)
            lo1, hi1 = s1.wilson(x1, n1)
            w("      %s %s campaign BASE: p0 = %d/%d = %.4f [%.4f, %.4f]; p1 = %d/%d = %.4f [%.4f, %.4f]; P(R) = %d/%d = %.4f (law: %.4f); "
              "P(Y) = %.4f = p0 + P(R)(p1 - p0) = %.4f"
              % (c, e, x0, n0, p0, lo0, hi0, x1, n1, p1, lo1, hi1, n1, len(base), pr, pr_theory, (x0 + x1) / len(base),
                 (p0 + pr * (p1 - p0)) if n0 and n1 else float("nan")))
            if pil is None:
                w("      %s %s pilot supplement: not supplied (test configuration)" % (c, e))
            else:
                q0 = sum(1 for r in pil if r["native_class"] == "NR")
                q1 = len(pil) - q0
                z0 = sum(yf(r) for r in pil if r["native_class"] == "NR")
                z1 = sum(yf(r) for r in pil if r["native_class"] != "NR")
                l1, h1 = s1.wilson(z1, q1)
                lp, hp = s1.wilson(x1 + z1, n1 + q1)
                w("      %s %s pilot native draws (other seeds; theta was chosen on their non-resonant part, so its p0 is in-sample): "
                  "p0 = %d/%d; p1 = %d/%d = %.4f [%.4f, %.4f]; pooled p1 (campaign BASE + pilot) = %d/%d = %.4f [%.4f, %.4f]"
                  % (c, e, z0, q0, z1, q1, z1 / q1 if q1 else float("nan"), l1, h1, x1 + z1, n1 + q1,
                     (x1 + z1) / (n1 + q1) if n1 + q1 else float("nan"), lp, hp))
    w("D6  BASE draws without a resonant seed token, by the smallest additive order of 2x among the four seed tokens "
      "(exploratory; the cut at %d was chosen post hoc on the pilot; no mechanism is claimed): positives E_theta / E_100 of n" % LOW_ORDER)
    for c in cells:
        cfg = REGISTRY[c]
        tab = defaultdict(lambda: [0, 0, 0])
        for b in B[c]:
            r = data[c][b]["BASE"]
            if r["alphabet_class"] != "NR":
                continue
            o = min(ord2(x, cfg["N"]) for x in r["d0"])
            t = tab[o if o <= 12 else 13]
            t[0] += 1
            t[1] += y_theta(r, cfg["theta"])
            t[2] += y_100(r)
        w("      %s  " % c + "  ".join("ord %s: %d/%d of %d" % (str(o) if o <= 12 else ">12", t[1], t[2], t[0]) for o, t in sorted(tab.items())))
        lo_ = [sum(t[i] for o, t in tab.items() if o <= LOW_ORDER) for i in range(3)]
        hi_ = [sum(t[i] for o, t in tab.items() if o > LOW_ORDER) for i in range(3)]
        w("      %s  smallest order <= %d: %d/%d of %d;  every order > %d: %d/%d of %d"
          % (c, LOW_ORDER, lo_[1], lo_[2], lo_[0], LOW_ORDER, hi_[1], hi_[2], hi_[0]))
    w("D7  resonant arms by value, E_theta / E_100 (Wilson 95 % for E_theta):")
    for c in cells:
        for arm, k_ in (("O1R", "r1"), ("O2R", "r2"), ("Q2R", "r2")):
            if arm in Yt[c]:
                byv = defaultdict(lambda: [0, 0, 0])
                for i, b in enumerate(B[c]):
                    t = byv[data[c][b][arm]["choices"][k_]]
                    t[0] += 1
                    t[1] += Yt[c][arm][i]
                    t[2] += Y1[c][arm][i]
                for v in sorted(byv):
                    n_, x_, z_ = byv[v]
                    lo, hi = s1.wilson(x_, n_)
                    w("      %s %s value %4d: n=%5d  E_theta %.4f [%.4f, %.4f]  E_100 %.4f" % (c, arm, v, n_, x_ / n_, lo, hi, z_ / n_))
    w("D8  the contrasts on pairs whose three other seed tokens are non-resonant:")
    for ci, olabel, a1, a0 in CONTRASTS:
        c = cells[ci]
        N = REGISTRY[c]["N"]
        clean = [i for i, b in enumerate(B[c])
                 if all(s1.res_class(x, N) == "NR" for q, x in enumerate(data[c][b]["BASE"]["d0"]) if q != data[c][b]["BASE"]["slot"])]
        for e in ENDPOINTS:
            w("      %s %s vs %s %s (n=%d): %s" % (c, a1, a0, e, len(clean), fmt(s1.paired(
                [Y[e][c][a1][i] for i in clean], [Y[e][c][a0][i] for i in clean], Z_95))))
    w("D9  runs that reached the cap of 300, by arm: all / before tick 800 (the latter are positive on E_100 without a tick-800 checkpoint):")
    for c in cells:
        arms = s1.arms_for(REGISTRY[c]["N"])
        w("      %s  " % c + "  ".join("%s %d/%d" % (a, sum(int(data[c][b][a]["hit_cap"]) for b in B[c]),
                                                    sum(int(cap_before_800(data[c][b][a])) for b in B[c])) for a in arms))
    w("D10 mean run time by arm, seconds (record field; planning information only):")
    for c in cells:
        arms = s1.arms_for(REGISTRY[c]["N"])
        w("      %s  " % c + "  ".join("%s %.2f" % (a, sum(data[c][b][a]["secs"] for b in B[c]) / len(B[c])) for a in arms))


# ------------------------------------------------------------------ self-test on synthetic input
def selftest(s1_path: str) -> int:
    from statistics import NormalDist
    ok = True

    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond)
        print(("PASS " if cond else "FAIL ") + name)

    chk("Stage 1 analysis library hashes to its pin", sha256_file(s1_path) == S1_ANALYSIS_SHA256)
    s1 = load_s1(s1_path)
    chk("pins equal the Stage 1 pins", (s1.ENGINE_SHA256, s1.ORIENT_SHA256, s1.RUNNER_SHA256) == (ENGINE_SHA256, ORIENT_SHA256, RUNNER_SHA256))
    chk("margins equal the Stage 1 margins", (s1.DELTA_STAR, s1.DELTA_NEUTRAL) == (DELTA_STAR, DELTA_NEUTRAL))
    chk("family quantile is the two-sided 1 - 0.05/10 normal quantile", abs(Z_FAMILY - NormalDist().inv_cdf(1 - 0.05 / (2 * FAMILY_SIZE))) < 1e-12)
    chk("family: five contrasts x two endpoints = ten", len(CONTRASTS) * len(ENDPOINTS) == FAMILY_SIZE)
    reg = {c: (REGISTRY[c]["N"], REGISTRY[c]["k"], REGISTRY[c]["T"], REGISTRY[c]["theta"], REGISTRY[c]["band"]) for c in PLANS["stage2"]}
    chk("registry: horizons, thresholds and bands of the pilot intake",
        reg == {"S2-C240": (240, 16, 1460, 106, (92, 127)), "S2-C242": (242, 16, 1460, 84, (78, 98)), "S2-C480": (480, 32, 2670, 114, (104, 131))})
    chk("registry: Stage 2 cells are confirmatory with 1500 base draws, test cells are not confirmatory",
        all(REGISTRY[c]["confirmatory"] and REGISTRY[c]["n_base"] == 1500 for c in PLANS["stage2"])
        and not any(REGISTRY[c]["confirmatory"] for c in PLANS["s2test"]))
    chk("registry: every horizon is at least 800 ticks", all(v["T"] >= TICK for v in REGISTRY.values()))
    chk("registry: contrasts name arms that exist in their cell",
        all(a in s1.arms_for(REGISTRY[PLANS[p][ci]]["N"]) for p in PLANS for ci, _, a1, a0 in CONTRASTS for a in (a1, a0)))
    seeds = {s1.derive_int(t, "N240", "k16", "base", 0) for t in ("AZ-TOKRES-S2", "AZ-TOKRES-S1", PILOT_TAG, "S2SMOKE")}
    chk("seed of a Stage 2 draw differs from Stage 1, the pilot and the test tag", len(seeds) == 4)
    # endpoints
    full = {"M": 150, "steps": 1460, "hit_cap": False, "M_at": {"100": 5, "800": 99}}
    early = {"M": 300, "steps": 512, "hit_cap": True, "M_at": {"100": 9, "500": 290}}
    at800 = {"M": 300, "steps": 800, "hit_cap": True, "M_at": {"800": 300}}
    cfg = REGISTRY["S2-C240"]
    chk("E_theta and E_100 can differ: M = 150 at the end, 99 at tick 800", (y_theta(full, 106), y_100(full)) == (1, 0))
    chk("a run capped before tick 800 is positive on E_100 and is counted as cap-decided", y_100(early) == 1 and cap_before_800(early))
    chk("a run capped at tick 800 has its checkpoint and is not cap-decided", y_100(at800) == 1 and not cap_before_800(at800))
    chk("record check accepts the three", all(s2_record_errors(r, cfg) == [] for r in (full, early, at800)))
    chk("record check rejects a missing checkpoint in an uncapped run",
        s2_record_errors({"M": 150, "steps": 1460, "hit_cap": False, "M_at": {"100": 5}}, cfg) != [])
    chk("record check rejects a checkpoint in a run stopped before tick 800",
        s2_record_errors({"M": 300, "steps": 512, "hit_cap": True, "M_at": {"800": 300}}, cfg) != [])
    chk("record check rejects a checkpoint above the final M", s2_record_errors(dict(full, M_at={"800": 151}), cfg) != [])
    # statistics
    lo, hi = clopper_pearson(14, 2620)
    chk("exact interval 14/2620 -> [0.0029243, 0.0089493]", abs(lo - 0.0029243) < 2e-7 and abs(hi - 0.0089493) < 2e-7)
    lo, hi = clopper_pearson(0, 1201)
    chk("exact interval 0/1201 -> [0, 0.003067]", lo == 0.0 and abs(hi - 0.003067) < 2e-6)
    chk("sign test 3 against 1 -> 0.625; no non-tied pair -> 1", abs(sign_test(3, 1) - 0.625) < 1e-12 and sign_test(0, 0) == 1.0)
    chk("order of 2x: resonant classes are orders 1 and 2", [ord2(x, 240) for x in (0, 120, 60, 180)] == [1, 1, 2, 2])
    chk("order of 2x at N = 242 takes the values 1, 11, 121 only", {ord2(x, 242) for x in range(242)} == {1, 11, 121})
    chk("order of 2x: 3 at N/6 and N/3, 4 at N/8", (ord2(40, 240), ord2(80, 240), ord2(30, 240)) == (3, 3, 4))
    y1 = [1] * 10 + [1] * 200 + [0] * 5 + [0] * 1285
    y0 = [1] * 10 + [0] * 200 + [1] * 5 + [0] * 1285
    r = s1.paired(y1, y0, Z_FAMILY)
    chk("reading: supported", reading(r, 1e-9).startswith("SUPPORTED"))
    chk("reading: a lower limit above 0.05 without a significant Holm p is not supported", reading(r, 0.06).startswith("INCONCLUSIVE"))
    chk("reading: not supported", reading(s1.paired([0] * 1490 + [1] * 10, [0] * 1485 + [1] * 15, Z_FAMILY), 1.0).startswith("NOT SUPPORTED"))
    mid = s1.paired([1] * 90 + [0] * 1410, [0] * 1500, Z_FAMILY)
    chk("reading: inconclusive when the simultaneous interval contains 0.05", mid["lo"] < 0.05 < mid["hi"] and reading(mid, 1e-9).startswith("INCONCLUSIVE"))
    narrow = s1.paired(y1, y0, s1.Z_975)
    chk("the family interval is wider than the Stage 1 interval on the same counts", r["lo"] < narrow["lo"] and r["hi"] > narrow["hi"])
    chk("Holm over ten: smallest p is multiplied by ten", abs(s1.holm([1e-4] + [0.5] * 9)[0] - 1e-3) < 1e-15)
    # pilot loader
    with tempfile.TemporaryDirectory() as d:
        recs = []
        for i, d0 in enumerate(([1, 2, 3, 5], [0, 7, 9, 11], [60, 7, 9, 11], [13, 17, 19, 23])):
            recs.append({"N": 240, "k": 16, "T": 900, "arm": "BASE", "base": i, "d0": d0, "native_class": s1.alphabet_class(d0, 240),
                         "M": 40 + 70 * i, "hit_cap": False, "steps": 900, "M_at": {"800": 39 + 70 * i}, "law_viol": 0})
        path = os.path.join(d, "N240k16T900.jsonl")
        with open(path, "w", newline="\n") as f:
            f.write("".join(json.dumps(x, sort_keys=True) + "\n" for x in recs))
        tcfg = dict(REGISTRY["T2-C240"])
        got, errs = load_pilot(d, tcfg, s1, registered=False)
        chk("pilot loader reads a well-formed file", errs == [] and len(got) == 4 and [x["native_class"] for x in got] == ["NR", "O1", "O2", "NR"])
        got, errs = load_pilot(d, dict(tcfg, pilot_sha256=sha256_file(path)), s1, registered=False)
        chk("pilot loader accepts the registered hash", errs == [] and got is not None)
        got, errs = load_pilot(d, dict(tcfg, pilot_sha256="0" * 64), s1, registered=False)
        chk("pilot loader refuses a file that does not hash to the registered value", got is None and errs)
        got, errs = load_pilot(d, tcfg, s1, registered=True)
        chk("pilot loader refuses records without the pilot tag and pins in registered mode", errs != [])
        recs[1]["native_class"] = "NR"
        with open(path, "w", newline="\n") as f:
            f.write("".join(json.dumps(x, sort_keys=True) + "\n" for x in recs))
        got, errs = load_pilot(d, tcfg, s1, registered=False)
        chk("pilot loader refuses a class label that contradicts the seed tokens", errs != [])
        got, errs = load_pilot(d, dict(tcfg, pilot_file="absent.jsonl"), s1, registered=False)
        chk("pilot loader reports a missing file", got is None and errs)
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def check_pilot(pilot_dir: str, s1) -> int:
    """Hashes and structure of the three registered pilot files. Tabulates no outcome."""
    bad = 0
    for c in PLANS["stage2"]:
        cfg = REGISTRY[c]
        recs, errs = load_pilot(pilot_dir, cfg, s1, registered=True)
        if errs:
            bad += 1
            print("%s: FAIL - %s" % (cfg["pilot_file"], "; ".join(errs[:5])))
        else:
            n1 = sum(1 for r in recs if r["native_class"] != "NR")
            print("%s: SHA-256 as registered; %d records, structure and identity as expected; %d with a resonant seed token, %d without"
                  % (cfg["pilot_file"], len(recs), n1, len(recs) - n1))
    print("PILOT CHECK", "PASS" if not bad else "FAIL")
    return 0 if not bad else 2


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", choices=sorted(PLANS))
    ap.add_argument("--dir")
    ap.add_argument("--engine")
    ap.add_argument("--orient")
    ap.add_argument("--runner")
    ap.add_argument("--analysis-s1")
    ap.add_argument("--fixtures-log")
    ap.add_argument("--pilot-dir")
    ap.add_argument("--exclude-base", default="")
    ap.add_argument("--check-pilot")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if not a.analysis_s1:
        ap.error("--analysis-s1 (the Stage 1 analysis script, used as a library) is required")
    if a.selftest:
        return selftest(a.analysis_s1)
    print("Stage 2 analysis script SHA-256 %s" % sha256_file(os.path.abspath(__file__)))
    s1_sha = sha256_file(a.analysis_s1)
    if s1_sha != S1_ANALYSIS_SHA256:
        print("INTEGRITY: FAIL. The Stage 1 analysis library does not hash to its pin. No estimate and no reading is produced.")
        return 2
    s1 = load_s1(a.analysis_s1)
    if a.check_pilot:
        return check_pilot(a.check_pilot, s1)
    if not (a.plan and a.dir and a.engine and a.orient and a.runner):
        ap.error("--plan with --dir, --engine, --orient, --runner is required")
    cells = PLANS[a.plan]
    registered = a.plan == "stage2"
    exclude = defaultdict(set)
    for item in (x for x in a.exclude_base.split(",") if x):
        c, _, b = item.partition(":")
        if c not in cells or not b.isdigit():
            ap.error("--exclude-base takes CELL:base items of this plan")
        exclude[c].add(int(b))
    for c in cells:
        print("registered configuration %s: %s" % (c, json.dumps(REGISTRY[c], sort_keys=True)))
    if not registered:
        print("*** TEST CONFIGURATION (tag %s): instrument validation only; no evidential value ***" % REGISTRY[cells[0]]["tag"])
    pins = {"engine": sha256_file(a.engine), "orient": sha256_file(a.orient), "runner": sha256_file(a.runner),
            "fixtures": s1.FIXTURES_SHA256, "golden": s1.GOLDEN_SHA256}
    errors = []
    for lab, got, want in (("engine", pins["engine"], ENGINE_SHA256), ("orientation reference", pins["orient"], ORIENT_SHA256),
                           ("runner", pins["runner"], RUNNER_SHA256)):
        if got != want:
            errors.append("%s file does not hash to the registered pin" % lab)
    data, n_rec, n_files = {}, 0, 0
    for c in cells:
        cfg = REGISTRY[c]
        files = sorted(glob.glob(os.path.join(glob.escape(a.dir), c + "_*.jsonl")))
        if not files:
            errors.append("%s: no record file" % c)
            data[c] = {}
            continue
        for p in files:
            print("input %s  SHA-256 %s" % (os.path.basename(p), sha256_file(p)))
        rows, errs = s1.validate(files, cfg, pins, frozenset(exclude[c]))
        errors += ["%s: %s" % (c, x) for x in errs]
        for b in rows:
            for arm, r in rows[b].items():
                for msg in s2_record_errors(r, cfg):
                    if len(errors) < 200:
                        errors.append("%s: base %d arm %s: %s" % (c, b, arm, msg))
        data[c] = rows
        n_rec += sum(len(v) for v in rows.values())
        n_files += len(files)
    pilots = {c: None for c in cells}
    if a.pilot_dir:
        for c in cells:
            recs, errs = load_pilot(a.pilot_dir, REGISTRY[c], s1, registered)
            errors += ["pilot: " + x for x in errs]
            pilots[c] = recs
    elif registered:
        errors.append("--pilot-dir is required for the registered plan")
    if errors:
        print("INTEGRITY: FAIL (%d error(s)%s). No estimate and no reading is produced." % (len(errors), "" if len(errors) < 200 else ", list truncated"))
        for x in errors[:40]:
            print("  - " + x)
        return 2
    print("INTEGRITY: PASS (%d records in %d file(s) of %d cells; identity, custody, states, records, set, tick-800 checkpoint%s checked)"
          % (n_rec, n_files, len(cells), ", pilot files" if a.pilot_dir else ""))
    if any(exclude.values()):
        print("DEVIATION: base draws excluded from all arms: %s" % {c: sorted(v) for c, v in exclude.items() if v})
    gate = s1.check_fixtures_log(a.fixtures_log, pins)
    print("G1 fixtures on the campaign machine: %s" % ("PASS" if not gate else "FAIL - " + "; ".join(gate)))
    viol = sum(r["law_viol"] for c in cells for v in data[c].values() for r in v.values())
    viol += sum(r["law_viol"] for c in cells for r in (pilots[c] or []))
    print("G2 token law (alphabet, exact class update, centre witness), summed violation counter%s: %d -> %s"
          % (" (campaign and pilot files)" if a.pilot_dir else "", viol, "PASS" if viol == 0 else "FAIL"))
    if gate or viol:
        print("GATE FAILURE. No estimate and no reading is produced.")
        return 3
    analyse(s1, a.plan, data, pilots, exclude)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
