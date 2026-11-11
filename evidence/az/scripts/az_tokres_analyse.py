#!/usr/bin/env python3
"""AZ token-resonance analysis - [SESSION] NONCANONICAL; implements the registered analysis plan of
records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md section 6 and nothing else. Standard library only; deterministic.

The analysis is FAIL-CLOSED. In registered mode nothing is estimated until every input has passed, in this order:
  1. identity   every manifest line and every record carries the registered tag, cell parameters, profile, policy,
                confirmatory flag and the three pinned SHA-256 values; the files given as --engine/--orient/--runner
                hash to the same pins;
  2. custody    every record file has a manifest whose last line states the file's SHA-256 and record count; the
                shards' ranges are disjoint and cover the registered base draws exactly;
  3. states     seed, initial phases, initial tokens, slot, choices and class labels of every record equal an
                independent re-derivation from (tag, N, k, base, arm) made in this file;
  4. records    internal consistency (births = M - 4, stop rule, t100, census total, census inside S0, ...);
  5. set        every registered (base, arm) exactly once, nothing else.
Any failure prints the errors, prints no estimate and no reading, and exits with code 2.
Then the gates G1 (fixtures log of the campaign machine: FIXTURES PASS with the pinned bytes) and G2 (law-violation
counter zero). A failed gate prints no estimate and no reading and exits with code 3.
Only then are the registered contrasts computed; every registered reading is printed together with the qualifiers
G3 (label permutation), G4 (sham) and G5 (detuned comparator).

usage
  python -I az_tokres_analyse.py --registered S1-C1 --engine E --orient O --runner R --fixtures-log LOG FILES...
         [--sensitivity FILES...] [--exclude-base 17,203]
  python -I az_tokres_analyse.py --exploratory --cell N120k8 --profile P1 FILES...     (no validation, no readings)
  python -I az_tokres_analyse.py --selftest
Exit codes: 0 analysis printed; 2 integrity failure; 3 gate failure; 1 self-test failure.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import sys
from collections import Counter, defaultdict

# ------------------------------------------------------------------ registered constants
ENGINE_SHA256 = "4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608"
ORIENT_SHA256 = "ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c"
RUNNER_SHA256 = "75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992"
FIXTURES_SHA256 = "da9256dc01d786355e2fc28938647b1b800d54b1425e2e927af1febff2f9cb86"
GOLDEN_SHA256 = "40eba43073fba138130244f75cc0790ef20bffcbeda7599ff4e372b95427c134"
SCHEMA = "az_tokres_run_v2"
MANIFEST_SCHEMA = "az_tokres_manifest_v2"
M0 = 4
Y_THRESHOLD = 100
DELTA_STAR = 0.05                      # registered minimal risk difference (superiority; PC4 equivalence margin)
DELTA_NEUTRAL = 0.025                  # registered neutrality margin of the control contrasts G4, G5
Z_975 = 2.241402727604947              # two-sided 97.5 %
Z_95 = 1.959963984540054
TDR26_B, TDR26_MS = 0.30, 0.25         # TDR-26 birth-anchored rule thresholds (source: TDR-G section 2, classifier)
SECONDARY_THRESHOLDS = (60, 80, 150, 200, 300)
_COMMON = {"k": 8, "T": 800, "cap": 300, "policy": "bound_symmetric"}
REGISTRY = {
    # Stage 1 (preregistration section 5). role: primary = confirmatory family; supportive = replication family.
    "S1-C1": dict(_COMMON, tag="AZ-TOKRES-S1", N=120, profile="P1", n_base=1500, n_perm=200, confirmatory=True, role="primary"),
    "S1-C2": dict(_COMMON, tag="AZ-TOKRES-S1", N=122, profile="P1", n_base=1500, n_perm=0, confirmatory=True, role="supportive"),
    "S1-C3": dict(_COMMON, tag="AZ-TOKRES-S1", N=120, profile="P2", n_base=500, n_perm=0, confirmatory=True, role="sensitivity"),
    # Test configuration (tag SMOKE): instrument validation and negative controls only; no evidential value.
    "TEST-C1": dict(_COMMON, tag="SMOKE", N=120, profile="P1", n_base=24, n_perm=6, confirmatory=False, role="test"),
    "TEST-C2": dict(_COMMON, tag="SMOKE", N=122, profile="P1", n_base=12, n_perm=0, confirmatory=False, role="test"),
    "TEST-C3": dict(_COMMON, tag="SMOKE", N=120, profile="P2", n_base=12, n_perm=0, confirmatory=False, role="test"),
}
SENSITIVITY_OF = {"S1-C1": "S1-C3", "TEST-C1": "TEST-C3"}


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ------------------------------------------------------------------ independent re-derivation of the registered states
def derive_int(*parts) -> int:
    s = "|".join(str(p) for p in parts).encode()
    return int.from_bytes(hashlib.sha256(s).digest()[:8], "big") % 10**12


def res_class(x: int, N: int) -> str:
    y = (2 * x) % N
    return "O1" if y == 0 else "O2" if y == N // 2 else "NR"


def alphabet_class(tokens, N: int) -> str:
    cl = {res_class(x, N) for x in tokens}
    return "O1+O2" if {"O1", "O2"} <= cl else "O1" if "O1" in cl else "O2" if "O2" in cl else "NR"


def arms_for(N: int):
    return ("BASE", "O1R", "O1D", "O2R", "O2D", "SHAM") if N % 4 == 0 else ("BASE", "O1R", "O1D", "Q2R", "SHAM")


def expected_state(tag: str, N: int, k: int, b: int, arm: str) -> dict:
    """What a record of (tag, N, k, base b, arm) must contain, derived without the runner and without the engine.

    The native draw of the pinned engine is four phases then four tokens, each `randrange(N)` of `random.Random(seed)`
    (init_universe, m0 = 4, exclude_zero_delta = False); fixture T12 checks this function against the runner."""
    seed = derive_int(tag, f"N{N}", f"k{k}", "base", b)
    rng = random.Random(seed)
    th0 = [rng.randrange(N) for _ in range(M0)]
    d0 = [rng.randrange(N) for _ in range(M0)]
    r = random.Random(derive_int(tag, f"N{N}", f"k{k}", "arm", b))
    j = r.randrange(M0)
    r1 = r.choice([0, N // 2])
    s1 = r.choice([1, -1])
    r2 = r.choice([N // 4, 3 * N // 4]) if N % 4 == 0 else r.choice([N // 4, N // 4 + 1, (3 * N) // 4, (3 * N) // 4 + 1])
    s2 = r.choice([1, -1])
    s3 = r.choice([1, -1])
    perm = list(range(M0))
    r.shuffle(perm)
    ch = {"slot": j, "r1": r1, "s1": s1, "r2": r2, "s2": s2, "s3": s3, "perm": perm}
    th, d = list(th0), list(d0)
    core = arm[:-2] if arm.endswith("_P") else arm
    new = {"BASE": d[j], "O1R": r1, "O1D": (r1 + s1) % N, "O2R": r2, "Q2R": r2, "O2D": (r2 + s2) % N,
           "SHAM": (d[j] + s3) % N}[core]
    d[j] = new
    if arm.endswith("_P"):
        th = [th[p] for p in perm]
        d = [d[p] for p in perm]
    return {"seed": seed, "slot": j, "choices": ch, "th0": th, "d0": d, "d0_base": d0,
            "alphabet_class": alphabet_class(d, N), "slot_class": res_class(new, N)}


# ------------------------------------------------------------------ validation (fail-closed)
def identity_of(cfg: dict, pins: dict) -> dict:
    return {"schema": SCHEMA, "tag": cfg["tag"], "cell": "N%dk%d" % (cfg["N"], cfg["k"]), "N": cfg["N"], "k": cfg["k"],
            "T": cfg["T"], "cap": cfg["cap"], "profile": cfg["profile"], "policy": cfg["policy"],
            "confirmatory": cfg["confirmatory"], "engine_sha256": pins["engine"], "orient_sha256": pins["orient"],
            "runner_sha256": pins["runner"]}


def check_record(r: dict, cfg: dict) -> list:
    """Internal consistency of one record. Returns a list of error strings."""
    e = []
    N, T, cap = cfg["N"], cfg["T"], cfg["cap"]
    try:
        M, births, steps = r["M"], r["births"], r["steps"]
        if not (isinstance(M, int) and isinstance(births, int) and isinstance(steps, int)):
            return ["M, births, steps must be integers"]
        if M != M0 + births:
            e.append("M != 4 + births")
        if not (0 <= steps <= T):
            e.append("steps outside [0, T]")
        if r["hit_cap"] != (M >= cap):
            e.append("hit_cap inconsistent with M and cap")
        if not r["hit_cap"] and steps != T:
            e.append("run stopped before T without reaching the cap")
        if (r["t100"] is None) != (M < Y_THRESHOLD):
            e.append("t100 inconsistent with M")
        if (r["fb"] is None) != (births == 0):
            e.append("fb inconsistent with births")
        census = {int(y): int(n) for y, n in r["census"]}
        if sum(census.values()) != M or any(n <= 0 for n in census.values()):
            e.append("census total != M")
        s0 = {x % N for x in r["d0"]} | {(-x) % N for x in r["d0"]}
        if not set(census) <= s0:
            e.append("final census contains a token outside S0")
        ms = [r["M_at"][q] for q in sorted(r["M_at"], key=int)]
        if any(a > b for a, b in zip(ms, ms[1:])) or (ms and ms[-1] > M):
            e.append("M_at not monotone")
        if not (isinstance(r["law_viol"], int) and r["law_viol"] >= 0):
            e.append("law_viol missing or not a non-negative integer")
        t = r["tdr26"]
        if (t is None) != (births == 0):
            e.append("tdr26 block inconsistent with births")
        if t is not None and (t["complete"] != (t["n"] == 200) or not (0 < t["n"] <= 200)):
            e.append("tdr26 window inconsistent")
    except (KeyError, TypeError, ValueError) as ex:
        e.append("malformed record: %r" % (ex,))
    return e


def validate(files, cfg: dict, pins: dict, exclude=frozenset()):
    """Return (rows, errors). rows[base][arm] = record. Nothing is trusted that is not checked here."""
    errors = []
    err = lambda s: errors.append(s) if len(errors) < 200 else None
    ident = identity_of(cfg, pins)
    arms = arms_for(cfg["N"])
    rows = defaultdict(dict)
    ranges = []
    if len(set(os.path.abspath(p) for p in files)) != len(files):
        err("a record file is given more than once")
    for path in files:
        name = os.path.basename(path)
        man_path = path + ".manifest.json"
        if not os.path.exists(path):
            err("%s: record file missing" % name)
            continue
        if not os.path.exists(man_path):
            err("%s: manifest missing" % name)
            continue
        try:
            with open(man_path) as f:
                mans = [json.loads(line) for line in f if line.strip()]
        except ValueError:
            err("%s: manifest unreadable" % name)
            continue
        if not mans:
            err("%s: manifest empty" % name)
            continue
        shard = mans[0].get("shard")
        for m in mans:
            if m.get("schema") != MANIFEST_SCHEMA:
                err("%s: manifest schema" % name)
            if m.get("identity") != ident:
                bad = [q for q in ident if (m.get("identity") or {}).get(q) != ident[q]]
                err("%s: manifest identity differs from the registered one in %s" % (name, bad))
            if m.get("shard") != shard:
                err("%s: manifest lines disagree on the shard arguments" % name)
        if not isinstance(shard, dict):
            err("%s: manifest without shard block" % name)
            continue
        if shard.get("n_perm") != cfg["n_perm"] or shard.get("arms") != list(arms) or shard.get("tdr26") is not True:
            err("%s: shard arguments (n_perm, arms, tdr26) differ from the registered ones" % name)
        start, stop = shard.get("start"), shard.get("stop")
        if not (isinstance(start, int) and isinstance(stop, int) and 0 <= start < stop <= cfg["n_base"]):
            err("%s: shard range [%s, %s) outside the registered base draws" % (name, start, stop))
            continue
        ranges.append((start, stop, name))
        digest = sha256_file(path)
        with open(path, "rb") as f:
            lines = f.read().decode("utf-8").split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        if mans[-1].get("file_sha256") != digest:
            err("%s: SHA-256 differs from the manifest (file changed after the run, or run not finished)" % name)
        if mans[-1].get("rows_total") != len(lines):
            err("%s: record count differs from the manifest" % name)
        for idx, line in enumerate(lines):
            where = "%s:%d" % (name, idx + 1)
            try:
                r = json.loads(line)
            except ValueError:
                err("%s: unreadable record" % where)
                continue
            bad = [q for q in ident if r.get(q) != ident[q]]
            if bad:
                err("%s: identity differs from the registered one in %s" % (where, bad))
                continue
            b, arm = r.get("base"), r.get("arm")
            allowed = set(arms) | ({"BASE_P", "O1R_P"} if isinstance(b, int) and b < cfg["n_perm"] else set())
            if not (isinstance(b, int) and start <= b < stop) or arm not in allowed:
                err("%s: (base %r, arm %r) is not a registered record of this shard" % (where, b, arm))
                continue
            if arm in rows[b]:
                err("%s: duplicate record (base %d, arm %s)" % (where, b, arm))
                continue
            exp = expected_state(cfg["tag"], cfg["N"], cfg["k"], b, arm)
            diff = [q for q in exp if r.get(q) != exp[q]]
            if diff:
                err("%s: initial state differs from the registered derivation in %s" % (where, diff))
                continue
            for msg in check_record(r, cfg):
                err("%s: %s" % (where, msg))
            rows[b][arm] = r
    ranges.sort()
    pos = 0
    for start, stop, name in ranges:
        if start != pos:
            err("shards do not tile the base draws: gap or overlap at %d (%s starts at %d)" % (pos, name, start))
        pos = max(pos, stop)
    if pos != cfg["n_base"]:
        err("shards cover base draws up to %d, registered %d" % (pos, cfg["n_base"]))
    for b in range(cfg["n_base"]):
        need = list(arms) + (["BASE_P", "O1R_P"] if b < cfg["n_perm"] else [])
        miss = [a for a in need if a not in rows.get(b, {})]
        if miss and b not in exclude:
            err("missing record(s) for base %d: %s" % (b, miss))
    return rows, errors


def check_fixtures_log(path: str, pins: dict) -> list:
    """G1: the fixtures log of the campaign machine must show the pinned bytes and end with FIXTURES PASS."""
    if not path or not os.path.exists(path):
        return ["fixtures log missing"]
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read().replace("\r\n", "\n")
    lines = [x.strip() for x in text.split("\n") if x.strip()]
    e = []
    want = {"engine": pins["engine"], "orientation reference": pins["orient"], "runner": pins["runner"],
            "fixtures script": pins["fixtures"], "golden file": pins["golden"]}
    for label, digest in want.items():
        if ("%s %s" % (label, digest)) not in [" ".join(x.split()) for x in lines]:
            e.append("fixtures log does not show the pinned %s" % label)
    if not lines or not lines[-1].startswith("FIXTURES PASS"):
        e.append("fixtures log does not end with FIXTURES PASS")
    if any(x.startswith("FAIL ") for x in lines):
        e.append("fixtures log contains a failed test")
    return e


# ------------------------------------------------------------------ statistics
def wilson(s: int, n: int, z: float = Z_95):
    if n == 0:
        return (float("nan"), float("nan"))
    p = s / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def mcnemar_exact(b: int, c: int) -> float:
    """Two-sided exact McNemar p-value: 2 * P(Bin(b+c, 1/2) <= min(b, c)), capped at 1."""
    m = b + c
    if m == 0:
        return 1.0
    lo = min(b, c)
    tail = sum(math.comb(m, i) for i in range(lo + 1)) / 2 ** m
    return min(1.0, 2 * tail)


def paired(y1, y0, z: float):
    """Paired binary contrast y1 - y0 over the same units.

    Returns the 2x2 counts, the two risks, the unadjusted risk difference RD = (b - c)/n, the exact McNemar p-value
    and the Agresti-Min adjusted Wald interval for the difference of matched proportions (0.5 added to each of the
    four cells; never of zero width)."""
    n = len(y1)
    a = sum(1 for u, v in zip(y1, y0) if u and v)
    b = sum(1 for u, v in zip(y1, y0) if u and not v)
    c = sum(1 for u, v in zip(y1, y0) if not u and v)
    if n == 0:
        nan = float("nan")
        return {"n": 0, "both": 0, "only1": 0, "only0": 0, "neither": 0, "p1": nan, "p0": nan, "rd": nan,
                "lo": nan, "hi": nan, "p_mcnemar": 1.0}
    ba, ca, na = b + 0.5, c + 0.5, n + 2.0
    mid = (ba - ca) / na
    se = math.sqrt(ba + ca - (ba - ca) ** 2 / na) / na
    return {"n": n, "both": a, "only1": b, "only0": c, "neither": n - a - b - c,
            "p1": (a + b) / n, "p0": (a + c) / n, "rd": (b - c) / n,
            "lo": max(-1.0, mid - z * se), "hi": min(1.0, mid + z * se), "p_mcnemar": mcnemar_exact(b, c)}


def holm(pvals):
    """Holm step-down adjusted p-values, in the input order."""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    adj = [0.0] * m
    run = 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (m - rank) * pvals[i]))
        adj[i] = run
    return adj


def katz_rr(s1: int, n1: int, s0: int, n0: int, z: float = Z_95):
    """Risk ratio with Katz log interval; 0.5 is added to every cell when a count is zero."""
    if n1 == 0 or n0 == 0:
        return (float("nan"),) * 3
    if s1 == 0 or s0 == 0:
        s1, s0, n1, n0 = s1 + 0.5, s0 + 0.5, n1 + 0.5, n0 + 0.5
    rr = (s1 / n1) / (s0 / n0)
    se = math.sqrt(1 / s1 - 1 / n1 + 1 / s0 - 1 / n0)
    return rr, rr * math.exp(-z * se), rr * math.exp(z * se)


def superiority(res, p_holm: float) -> str:
    if res["n"] == 0:
        return "INCONCLUSIVE (no pairs)"
    if p_holm < 0.05 and res["lo"] > DELTA_STAR:
        return "SUPPORTED (Holm p < 0.05 and lower limit > %.2f)" % DELTA_STAR
    if res["hi"] < DELTA_STAR:
        return "NOT SUPPORTED AT THE REGISTERED SIZE (upper limit < %.2f)" % DELTA_STAR
    return "INCONCLUSIVE (interval contains %.2f)" % DELTA_STAR


def equivalence(res, margin: float) -> str:
    """Three-way reading of a control contrast against a declared margin. 'Contains zero' is never used."""
    if res["n"] == 0:
        return "INCONCLUSIVE"
    if -margin < res["lo"] and res["hi"] < margin:
        return "EQUIVALENT"
    if res["lo"] >= margin or res["hi"] <= -margin:
        return "DIFFERENT"
    return "INCONCLUSIVE"


def y_of(r, thr: int = Y_THRESHOLD) -> int:
    return int(r["M"] >= thr)


def fmt(res) -> str:
    return ("n=%d  p1=%.4f  p0=%.4f  RD=%+.4f [%+.4f, %+.4f]  discordant %d/%d  McNemar p=%.3e"
            % (res["n"], res["p1"], res["p0"], res["rd"], res["lo"], res["hi"], res["only1"], res["only0"],
               res["p_mcnemar"]))


# ------------------------------------------------------------------ the registered analysis
def analyse(rows, cfg: dict, mode: str, exclude=frozenset(), out=sys.stdout):
    """mode: 'registered' (Stage 1 cells C1, C2), 'test' (test configuration), 'sensitivity' (profile P2:
    descriptive) or 'exploratory' (unvalidated input). Readings are printed in the first two modes only."""
    w = lambda s="": print(s, file=out)
    N = cfg["N"]
    arms = arms_for(N)
    bases = [b for b in sorted(rows) if b not in exclude and all(a in rows[b] for a in arms)]
    if not bases:
        w("no base draw with all arms present")
        return
    Y = {a: [y_of(rows[b][a]) for b in bases] for a in arms}
    w("cell N=%d  profile %s  base draws analysed=%d  excluded=%s" % (N, cfg["profile"], len(bases), sorted(exclude)))

    def nr_slot(b, arm):
        return rows[b][arm]["slot_class"] == "NR"

    def sub(a1, a0, keep):
        idx = [i for i, b in enumerate(bases) if keep(b)]
        return paired([Y[a1][i] for i in idx], [Y[a0][i] for i in idx], Z_95)

    # ---- qualifiers G3-G5 (computed first; attached to every reading)
    quals = []
    perm_tot = perm_bad = 0
    key = lambda r: (r["M"], r["births"], r["steps"], r["fb"], json.dumps(r["M_at"], sort_keys=True))
    for b in bases:
        for a in ("BASE", "O1R"):
            if a + "_P" in rows[b]:
                perm_tot += 1
                perm_bad += key(rows[b][a]) != key(rows[b][a + "_P"])
    if cfg["n_perm"]:
        g3 = "PASS" if perm_bad == 0 and perm_tot else "FAIL"
        quals.append(("G3 node-label permutation", g3,
                      "%d of %d permuted runs differ in (M, births, steps, fb, M_at)" % (perm_bad, perm_tot)))
    sham = sub("SHAM", "BASE", lambda b: nr_slot(b, "BASE") and nr_slot(b, "SHAM"))
    quals.append(("G4 sham perturbation vs BASE (native and perturbed slot token non-resonant)",
                  equivalence(sham, DELTA_NEUTRAL), fmt(sham)))
    det = {}
    for a in ("O1D", "O2D"):
        if a in Y:
            det[a] = sub(a, "BASE", lambda b: nr_slot(b, "BASE"))
            quals.append(("G5 detuned arm %s vs BASE (native slot token non-resonant)" % a,
                          equivalence(det[a], DELTA_NEUTRAL), fmt(det[a])))
    w("\n[control contrasts; Agresti-Min intervals 95 %%; neutrality margin +-%.3f%s]"
      % (DELTA_NEUTRAL, "; readings EQUIVALENT / DIFFERENT / INCONCLUSIVE" if mode in ("registered", "test") else ""))
    for name, status, detail in quals:
        w("%s: %s\n    %s" % (name, status if mode in ("registered", "test") else "(no reading in this mode)", detail))

    def qualifier_line(relevant):
        notes = [("%s %s" % (n.split()[0], s)) for n, s, _ in quals
                 if s not in ("PASS", "EQUIVALENT") and any(n.startswith(q) for q in relevant)]
        if exclude:
            notes.append("DEVIATION: base draws excluded")
        return ("UNQUALIFIED (every control of this cell reads PASS or EQUIVALENT)" if not notes
                else "QUALIFIED BY " + "; ".join(notes))

    def reading(label, text, relevant):
        if mode == "exploratory":
            w("    reading: SUPPRESSED (exploratory input; no reading is defined for it)")
        elif mode == "sensitivity":
            w("    reading: none (sensitivity profile; descriptive)")
        elif mode == "test":
            w("    test-configuration reading, no evidential value: %s" % text)
            w("    qualifiers: %s" % qualifier_line(relevant))
        else:
            w("    registered reading (%s): %s" % (label, text))
            w("    qualifiers: %s" % qualifier_line(relevant))

    # ---- registered contrasts
    if N % 4 == 0:
        w("\n[family 1, confirmatory: PC1 and PC2, paired on the base draw; Agresti-Min intervals 97.5 % two-sided; "
          "Holm over the two tests]")
        sup = [("PC1  O1R vs O1D  (2x = 0)", paired(Y["O1R"], Y["O1D"], Z_975), ("G3", "G4", "G5 detuned arm O1D")),
               ("PC2  O2R vs O2D  (2x = N/2)", paired(Y["O2R"], Y["O2D"], Z_975), ("G3", "G4", "G5 detuned arm O2D"))]
        adj = holm([r["p_mcnemar"] for _, r, _ in sup])
        for (name, r, rel), pa in zip(sup, adj):
            w("%s\n    %s  Holm p=%.3e" % (name, fmt(r), pa))
            reading("family 1", superiority(r, pa), rel)
    else:
        w("\n[family 2, supportive replication, separate from family 1: PC3 superiority and PC4 equivalence; "
          "Agresti-Min intervals 97.5 % two-sided (Bonferroni over the two)]")
        r = paired(Y["O1R"], Y["O1D"], Z_975)
        w("PC3  O1R vs O1D  (2x = 0)\n    %s  Bonferroni p=%.3e" % (fmt(r), min(1.0, 2 * r["p_mcnemar"])))
        reading("family 2", superiority(r, min(1.0, 2 * r["p_mcnemar"])), ("G3", "G4", "G5 detuned arm O1D"))
        r = paired(Y["Q2R"], Y["BASE"], Z_975)
        w("PC4  Q2R vs BASE (no order-2 token exists)\n    %s" % fmt(r))
        eq = equivalence(r, DELTA_STAR)
        reading("family 2", {"EQUIVALENT": "EQUIVALENT TO BASE within +-%.2f" % DELTA_STAR,
                             "DIFFERENT": "DIFFERENT FROM BASE by more than %.2f" % DELTA_STAR,
                             "INCONCLUSIVE": "INCONCLUSIVE (interval neither inside nor outside +-%.2f)" % DELTA_STAR}[eq],
                ("G3", "G4"))

    # ---- secondary (nominal 95 %; descriptive)
    w("\n[secondary, nominal 95 %; descriptive, no reading]")
    n = len(bases)
    if N % 4 == 0:
        diffs = [(u + v) / 2 - (x + y) / 2 for u, v, x, y in zip(Y["O1R"], Y["O2R"], Y["O1D"], Y["O2D"])]
        rng = random.Random(20261111)
        boots = sorted(sum(diffs[rng.randrange(n)] for _ in range(n)) / n for _ in range(2000))
        w("S1  combined 4x = 0 (mean of the two resonant arms minus mean of the two detuned arms): RD=%+.4f "
          "bootstrap 95%% [%+.4f, %+.4f] (2000 resamples of base draws, seed 20261111)"
          % (sum(diffs) / n, boots[int(0.025 * len(boots))], boots[min(len(boots) - 1, int(0.975 * len(boots)))]))
    cls = Counter()
    tails = Counter()
    for b in bases:
        r = rows[b]["BASE"]
        cls[r["alphabet_class"]] += 1
        tails[r["alphabet_class"]] += y_of(r)
    w("S2  native association in the BASE arm (alphabet class of the four native tokens):")
    for c in ("NR", "O1", "O2", "O1+O2"):
        if cls[c]:
            lo, hi = wilson(tails[c], cls[c])
            w("      %-6s n=%5d tails=%4d rate=%.4f [%.4f, %.4f]" % (c, cls[c], tails[c], tails[c] / cls[c], lo, hi))
    n1 = sum(cls[c] for c in ("O1", "O2", "O1+O2"))
    s1 = sum(tails[c] for c in ("O1", "O2", "O1+O2"))
    rr, lo, hi = katz_rr(s1, n1, tails["NR"], cls["NR"])
    w("      any 4x = 0 seed versus none: %d/%d against %d/%d, risk ratio %.2f [%.2f, %.2f] (Katz)"
      % (s1, n1, tails["NR"], cls["NR"], rr, lo, hi))
    for name, a1, a0 in (("S3a O1R vs BASE", "O1R", "BASE"), ("S3b O2R vs BASE", "O2R", "BASE"),
                         ("S3c O1D vs BASE, all base draws", "O1D", "BASE"), ("S3d O2D vs BASE, all base draws", "O2D", "BASE")):
        if a1 in Y:
            w("%s: %s" % (name, fmt(paired(Y[a1], Y[a0], Z_95))))
    w("S4  resonant arms by the value set (the engine is exactly invariant under delta -> delta + N/2 on all nodes):")
    for arm, k_ in (("O1R", "r1"), ("O2R", "r2"), ("Q2R", "r2")):
        if arm in Y:
            byv = defaultdict(list)
            for i, b in enumerate(bases):
                byv[rows[b][arm]["choices"][k_]].append(Y[arm][i])
            for v in sorted(byv):
                lo, hi = wilson(sum(byv[v]), len(byv[v]))
                w("      %s value %4d: n=%5d rate=%.4f [%.4f, %.4f]" % (arm, v, len(byv[v]), sum(byv[v]) / len(byv[v]), lo, hi))
    clean = []
    for i, b in enumerate(bases):
        r = rows[b]["BASE"]
        if all(res_class(x, N) == "NR" for q, x in enumerate(r["d0"]) if q != r["slot"]):
            clean.append(i)
    w("S5  pairs whose three other tokens are non-resonant (n=%d):" % len(clean))
    for name, a1, a0 in (("O1R vs O1D", "O1R", "O1D"), ("O2R vs O2D", "O2R", "O2D")):
        if a1 in Y and a0 in Y:
            w("      %s: %s" % (name, fmt(paired([Y[a1][i] for i in clean], [Y[a0][i] for i in clean], Z_95))))
    w("S6  threshold sensitivity, rate of M >= c by arm:")
    for c in SECONDARY_THRESHOLDS:
        w("      c=%3d  " % c + "  ".join("%s %.4f" % (a, sum(int(rows[b][a]["M"] >= c) for b in bases) / n) for a in arms))
    w("S7  mean share of the largest signed token class at the end, by arm and outcome (Y=1 / Y=0):")
    for a in arms:
        t1 = [rows[b][a]["top_share"] for b in bases if y_of(rows[b][a])]
        t0 = [rows[b][a]["top_share"] for b in bases if not y_of(rows[b][a])]
        w("      %-5s Y=1: n=%4d mean=%s   Y=0: n=%5d mean=%s"
          % (a, len(t1), "%.3f" % (sum(t1) / len(t1)) if t1 else "-", len(t0), "%.3f" % (sum(t0) / len(t0)) if t0 else "-"))
    w("S8  TDR-26 birth-anchored rule (b/step >= %.2f and ms_abs <= %.2f over [fb, fb+200)); separate output, "
      "outside the rule's source scope:" % (TDR26_B, TDR26_MS))
    for a in arms:
        st = Counter()
        for b in bases:
            r = rows[b][a]
            t = r.get("tdr26")
            if r["fb"] is None:
                st["not applicable (no birth)"] += 1
            elif t is None:
                st["not collected"] += 1
            elif not t["complete"]:
                st["censored (window incomplete)"] += 1
            else:
                pos = t["b_per_step"] >= TDR26_B and (t["ms_abs"] is not None and t["ms_abs"] <= TDR26_MS)
                st["rule+ Y=%d" % y_of(r) if pos else "rule- Y=%d" % y_of(r)] += 1
        w("      %-5s %s" % (a, "  ".join("%s: %d" % kv for kv in sorted(st.items()))))
    fbs = {a: sorted(rows[b][a]["fb"] for b in bases if rows[b][a]["fb"] is not None) for a in arms}
    w("S10 first-birth step, median by arm (runs with a birth); descriptive only, not a mediation analysis: "
      + "  ".join("%s %s (n=%d)" % (a, fbs[a][len(fbs[a]) // 2] if fbs[a] else "-", len(fbs[a])) for a in arms))


# ------------------------------------------------------------------ self-test on synthetic counts
def selftest() -> int:
    ok = True

    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond)
        print(("PASS " if cond else "FAIL ") + name)

    y1 = [1] * 10 + [1] * 200 + [0] * 5 + [0] * 785
    y0 = [1] * 10 + [0] * 200 + [1] * 5 + [0] * 785
    r = paired(y1, y0, Z_975)
    chk("paired counts", (r["both"], r["only1"], r["only0"], r["neither"]) == (10, 200, 5, 785))
    chk("paired RD", abs(r["rd"] - 0.195) < 1e-12)
    chk("paired Agresti-Min 97.5 % interval", abs(r["lo"] - 0.165612) < 2e-5 and abs(r["hi"] - 0.223609) < 2e-5)
    z0 = paired([0] * 40, [0] * 40, Z_975)
    chk("interval has positive width when there is no discordant pair", z0["lo"] < 0 < z0["hi"] and z0["rd"] == 0)
    chk("McNemar exact b=3,c=1 -> 0.625", abs(mcnemar_exact(3, 1) - 0.625) < 1e-12)
    chk("McNemar exact b=0,c=0 -> 1", mcnemar_exact(0, 0) == 1.0)
    chk("McNemar exact b=10,c=0 -> 2/1024", abs(mcnemar_exact(10, 0) - 2 / 1024) < 1e-15)
    chk("Holm (0.01, 0.04) -> (0.02, 0.04)", holm([0.01, 0.04]) == [0.02, 0.04])
    chk("Holm (0.04, 0.03) -> (0.06, 0.06)", holm([0.04, 0.03]) == [0.06, 0.06])
    lo, hi = wilson(61, 258)
    chk("Wilson 61/258 -> [0.1887, 0.2919]", abs(lo - 0.1887) < 5e-4 and abs(hi - 0.2919) < 5e-4)
    rr, lo, hi = katz_rr(61, 258, 11, 1865)
    chk("Katz RR 61/258 vs 11/1865 -> 40.09 [21.38, 75.17]", abs(rr - 40.09) < 0.01 and abs(lo - 21.38) < 0.02 and abs(hi - 75.17) < 0.05)
    chk("superiority: supported", superiority(r, 1e-9).startswith("SUPPORTED"))
    chk("superiority: not supported", superiority(paired([0] * 995 + [1] * 5, [0] * 990 + [1] * 10, Z_975), 0.5).startswith("NOT SUPPORTED"))
    chk("superiority: inconclusive", superiority(paired([1] * 3 + [0] * 17, [0] * 20, Z_975), 0.25).startswith("INCONCLUSIVE"))
    near = paired([1] * 12 + [0] * 1488, [0] * 6 + [1] * 12 + [0] * 1482, Z_95)
    chk("equivalence: EQUIVALENT when the interval is inside the margin", equivalence(near, DELTA_NEUTRAL) == "EQUIVALENT")
    wide = paired([1] * 2 + [0] * 28, [0] * 30, Z_95)
    chk("equivalence: an interval that contains zero but is wider than the margin is INCONCLUSIVE, not neutral",
        wide["lo"] < 0 < wide["hi"] and equivalence(wide, DELTA_NEUTRAL) == "INCONCLUSIVE")
    far = paired([1] * 300 + [0] * 1200, [0] * 1500, Z_95)
    chk("equivalence: DIFFERENT when the interval lies beyond the margin", equivalence(far, DELTA_NEUTRAL) == "DIFFERENT")
    e1 = expected_state("FIXTURE", 120, 8, 0, "O1R")
    e2 = expected_state("FIXTURE", 120, 8, 0, "O1R_P")
    chk("expected_state: O1R sets the slot to r1 and keeps the other three tokens",
        e1["d0"][e1["slot"]] == e1["choices"]["r1"] and sum(a != b for a, b in zip(e1["d0"], e1["d0_base"])) <= 1)
    chk("expected_state: the permuted arm is the same multiset of (phase, token) pairs",
        sorted(zip(e1["th0"], e1["d0"])) == sorted(zip(e2["th0"], e2["d0"])) and e1["slot_class"] == e2["slot_class"] == "O1")
    rec = {"M": 104, "births": 100, "steps": 800, "hit_cap": False, "t100": 700, "fb": 30, "census": [[0, 104]],
           "d0": [0, 5, 7, 9], "M_at": {"100": 5, "800": 104}, "law_viol": 0,
           "tdr26": {"n": 200, "complete": True, "b_per_step": 0.1, "ms_abs": 0.5}}
    cfg = REGISTRY["TEST-C1"]
    chk("check_record accepts a consistent record", check_record(rec, cfg) == [])
    chk("check_record rejects M != 4 + births", check_record(dict(rec, M=105), cfg) != [])
    chk("check_record rejects a census token outside S0", check_record(dict(rec, census=[[1, 104]]), cfg) != [])
    chk("check_record rejects a missing law counter", check_record(dict(rec, law_viol=None), cfg) != [])
    chk("registry: Stage 1 cells are confirmatory, test cells are not",
        all(REGISTRY[c]["confirmatory"] == c.startswith("S1-") for c in REGISTRY))
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--registered", choices=sorted(REGISTRY))
    ap.add_argument("--engine")
    ap.add_argument("--orient")
    ap.add_argument("--runner")
    ap.add_argument("--fixtures-log")
    ap.add_argument("--sensitivity", nargs="*", default=[])
    ap.add_argument("--exclude-base", default="")
    ap.add_argument("--exploratory", action="store_true")
    ap.add_argument("--cell")
    ap.add_argument("--profile", default="P1")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    print("analysis script SHA-256 %s" % sha256_file(__file__))
    for path in list(a.files) + list(a.sensitivity):
        if os.path.exists(path):
            print("input %s  SHA-256 %s" % (os.path.basename(path), sha256_file(path)))

    if a.exploratory:
        if a.registered or not (a.cell and a.files):
            ap.error("--exploratory needs --cell and files, and excludes --registered")
        print("*** EXPLORATORY INPUT: not validated, not confirmatory; no reading is printed ***")
        N = int(a.cell[1:a.cell.index("k")])
        rows = defaultdict(dict)
        for path in a.files:
            with open(path) as f:
                for line in f:
                    r = json.loads(line)
                    if r.get("cell") == a.cell and r.get("profile") == a.profile:
                        rows[r["base"]][r["arm"]] = r
        analyse(rows, {"N": N, "profile": a.profile, "n_perm": 1}, "exploratory")
        return 0

    if not (a.registered and a.files and a.engine and a.orient and a.runner):
        ap.error("--registered CELL with --engine, --orient, --runner and record files is required")
    cfg = REGISTRY[a.registered]
    mode = "sensitivity" if cfg["role"] == "sensitivity" or cfg["profile"] != "P1" else \
        "registered" if cfg["confirmatory"] else "test"
    exclude = frozenset(int(x) for x in a.exclude_base.split(",") if x)
    print("registered configuration %s: %s" % (a.registered, json.dumps(cfg, sort_keys=True)))
    if mode == "test":
        print("*** TEST CONFIGURATION (tag %s): instrument validation only; no evidential value ***" % cfg["tag"])
    pins = {"engine": sha256_file(a.engine), "orient": sha256_file(a.orient), "runner": sha256_file(a.runner),
            "fixtures": FIXTURES_SHA256, "golden": GOLDEN_SHA256}
    errors = []
    for label, got, want in (("engine", pins["engine"], ENGINE_SHA256), ("orientation reference", pins["orient"], ORIENT_SHA256),
                             ("runner", pins["runner"], RUNNER_SHA256)):
        if got != want:
            errors.append("%s file does not hash to the registered pin" % label)
    rows, errs = validate(a.files, cfg, pins, exclude)
    errors += errs
    rows2 = None
    if a.sensitivity:
        if a.registered not in SENSITIVITY_OF:
            errors.append("--sensitivity is defined for %s only" % sorted(SENSITIVITY_OF))
        else:
            rows2, errs2 = validate(a.sensitivity, REGISTRY[SENSITIVITY_OF[a.registered]], pins)
            errors += ["sensitivity set: " + x for x in errs2]
    if errors:
        print("INTEGRITY: FAIL (%d error(s)%s). No estimate and no reading is produced." % (len(errors), "" if len(errors) < 200 else ", list truncated"))
        for x in errors[:40]:
            print("  - " + x)
        return 2
    n_rec = sum(len(v) for v in rows.values())
    print("INTEGRITY: PASS (%d records in %d file(s); identity, custody, states, records and set checked)" % (n_rec, len(a.files)))
    if exclude:
        print("DEVIATION: base draws excluded from all arms: %s" % sorted(exclude))
    gate = check_fixtures_log(a.fixtures_log, pins)
    print("G1 fixtures on the campaign machine: %s" % ("PASS" if not gate else "FAIL - " + "; ".join(gate)))
    viol = sum(r["law_viol"] for v in rows.values() for r in v.values())
    viol += sum(r["law_viol"] for v in (rows2 or {}).values() for r in v.values())
    print("G2 token law (alphabet, exact class update, centre witness), summed violation counter: %d -> %s"
          % (viol, "PASS" if viol == 0 else "FAIL"))
    if gate or viol:
        print("GATE FAILURE. No estimate and no reading is produced.")
        return 3
    analyse(rows, cfg, mode, exclude)
    if rows2 is not None:
        cfg2 = REGISTRY[SENSITIVITY_OF[a.registered]]
        common = [(b, arm) for b in rows2 for arm in rows2[b] if arm in rows.get(b, {})]
        same = sum(rows[b][arm]["M"] == rows2[b][arm]["M"] and rows[b][arm]["births"] == rows2[b][arm]["births"] for b, arm in common)
        print("\n[sensitivity] profile %s versus %s on %d common (base, arm) runs: identical (M, births) in %d; Y differs in %d"
              % (cfg["profile"], cfg2["profile"], len(common), same, sum(y_of(rows[b][arm]) != y_of(rows2[b][arm]) for b, arm in common)))
        print("--- the contrasts recomputed under profile %s: descriptive, no reading ---" % cfg2["profile"])
        analyse(rows2, cfg2, "sensitivity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
