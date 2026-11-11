#!/usr/bin/env python3
"""AZ token-resonance analysis - [SESSION] NONCANONICAL; implements the registered analysis plan of
records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md section 6 and nothing else. Standard library only; deterministic.

usage
  python -I az_tokres_analyse.py --cell N120k8 --profile P1 --n-base 1500 FILE.jsonl [FILE.jsonl ...]
         [--n-perm 200] [--partial] [--exclude-base 17,203] [--compare-profile P2]
  python -I az_tokres_analyse.py --selftest

Primary endpoint  Y = 1{ M >= 100 }  (M = node count when the run stops; M never decreases, so M = max_t M_t).
Without --partial the script refuses a data set in which a registered (base, arm) is missing or duplicated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import sys
from collections import Counter, defaultdict

Y_THRESHOLD = 100
DELTA_STAR = 0.05                      # registered minimal risk difference
Z_975 = 2.241402727604947              # two-sided 97.5 % (two primary contrasts, simultaneous 95 %)
Z_95 = 1.959963984540054
TDR26_B, TDR26_MS = 0.30, 0.25         # TDR-26 birth-anchored rule thresholds (source: TDR-G section 2, classifier script)
SECONDARY_THRESHOLDS = (60, 80, 150, 200, 300)
SCHEMA = "az_tokres_run_v1"


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


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


def decision(res, p_holm: float) -> str:
    if p_holm < 0.05 and res["lo"] > DELTA_STAR:
        return "SUPPORTED (Holm p < 0.05 and lower limit > %.2f)" % DELTA_STAR
    if res["hi"] < DELTA_STAR:
        return "NOT SUPPORTED AT THE REGISTERED SIZE (upper limit < %.2f)" % DELTA_STAR
    return "INCONCLUSIVE (interval contains %.2f)" % DELTA_STAR


# ------------------------------------------------------------------ data
def load(files, cell: str, profile: str):
    rows = defaultdict(dict)
    dup = 0
    for path in files:
        with open(path) as f:
            for line in f:
                r = json.loads(line)
                if r.get("schema") != SCHEMA or r["cell"] != cell or r["profile"] != profile:
                    continue
                if r["arm"] in rows[r["base"]]:
                    dup += 1
                rows[r["base"]][r["arm"]] = r
    return rows, dup


def y_of(r, thr: int = Y_THRESHOLD) -> int:
    return int(r["M"] >= thr)


def res_class(x: int, N: int) -> str:
    y = (2 * x) % N
    return "O1" if y == 0 else "O2" if y == N // 2 else "NR"


def fmt(res) -> str:
    return ("n=%d  p1=%.4f  p0=%.4f  RD=%+.4f [%+.4f, %+.4f]  discordant %d/%d  McNemar p=%.3e"
            % (res["n"], res["p1"], res["p0"], res["rd"], res["lo"], res["hi"], res["only1"], res["only0"],
               res["p_mcnemar"]))


def analyse(rows, N: int, n_base: int, n_perm: int, partial: bool, exclude, out=sys.stdout, label: str = ""):
    w = lambda s="": print(s, file=out)
    arms = ("BASE", "O1R", "O1D", "O2R", "O2D", "SHAM") if N % 4 == 0 else ("BASE", "O1R", "O1D", "Q2R", "SHAM")
    bases = [b for b in range(n_base) if b not in exclude]
    missing = [(b, a) for b in bases for a in arms if a not in rows.get(b, {})]
    missing += [(b, a) for b in bases if b < n_perm for a in ("BASE_P", "O1R_P") if a not in rows.get(b, {})]
    if partial:
        w("*** PARTIAL DATA - NOT A CONFIRMATORY ANALYSIS - no registered decision may be read from this output ***")
        bases = [b for b in bases if all(a in rows.get(b, {}) for a in arms)]
    elif missing:
        w("INCOMPLETE: %d registered (base, arm) records missing, first %s" % (len(missing), missing[:5]))
        return 2
    w("%scell N=%d  base draws analysed=%d  excluded=%s" % (label, N, len(bases), sorted(exclude)))
    if not bases:
        w("no base draw with all arms present")
        return 2
    Y ={a: [y_of(rows[b][a]) for b in bases] for a in arms}

    # ---- integrity
    viol = sum((rows[b][a].get("law_viol") or 0) for b in bases for a in rows[b])
    w("law check: runs with a token-alphabet or census violation, summed counter = %d (registered expectation 0)" % viol)

    # ---- primary / family contrasts
    w("\n[registered contrasts, paired on base draw; Agresti-Min intervals, 97.5 % two-sided; Holm over the "
      "superiority tests of the family]")
    if N % 4 == 0:
        sup = [("PC1  O1R vs O1D  (2x = 0)", paired(Y["O1R"], Y["O1D"], Z_975)),
               ("PC2  O2R vs O2D  (2x = N/2)", paired(Y["O2R"], Y["O2D"], Z_975))]
        equ = []
    else:
        sup = [("PC3  O1R vs O1D  (2x = 0)", paired(Y["O1R"], Y["O1D"], Z_975))]
        equ = [("PC4  Q2R vs BASE (no order-2 token exists)", paired(Y["Q2R"], Y["BASE"], Z_975))]
    adj = holm([r["p_mcnemar"] for _, r in sup])
    for (name, r), pa in zip(sup, adj):
        w("%s\n    %s  Holm p=%.3e" % (name, fmt(r), pa))
        w("    registered reading: %s" % decision(r, pa))
    for name, r in equ:
        w("%s\n    %s" % (name, fmt(r)))
        eq = -DELTA_STAR < r["lo"] and r["hi"] < DELTA_STAR
        w("    registered reading: %s" % ("EQUIVALENT TO BASE within +-%.2f" % DELTA_STAR if eq else
                                          "NOT SHOWN EQUIVALENT (interval leaves +-%.2f)" % DELTA_STAR))

    # ---- secondary (nominal 95 %; descriptive)
    w("\n[secondary, nominal 95 %; no confirmatory reading]")
    if N % 4 == 0:
        comb = [(u + v) / 2 for u, v in zip(Y["O1R"], Y["O2R"])]
        comd = [(u + v) / 2 for u, v in zip(Y["O1D"], Y["O2D"])]
        diffs = [u - v for u, v in zip(comb, comd)]
        rng = random.Random(20261111)
        n = len(diffs)
        boots = sorted(sum(diffs[rng.randrange(n)] for _ in range(n)) / n for _ in range(2000)) if n else [float("nan")]
        w("S1  combined 4x = 0 (mean of the two resonant arms minus mean of the two detuned arms): RD=%+.4f "
          "bootstrap 95%% [%+.4f, %+.4f] (2000 resamples of base draws, seed 20261111)"
          % (sum(diffs) / n, boots[int(0.025 * len(boots))], boots[min(len(boots) - 1, int(0.975 * len(boots)))]))
    cls = Counter()
    tails = Counter()
    for b in bases:
        r = rows[b]["BASE"]
        c = r["alphabet_class"]
        cls[c] += 1
        tails[c] += y_of(r)
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
    for name, a1, a0 in (("S3a O1D vs BASE", "O1D", "BASE"), ("S3b O2D vs BASE", "O2D", "BASE"),
                         ("S3c O1R vs BASE", "O1R", "BASE"), ("S3d O2R vs BASE", "O2R", "BASE")):
        if a1 in Y:
            w("%s: %s" % (name, fmt(paired(Y[a1], Y[a0], Z_95))))
    elig = [i for i, b in enumerate(bases) if rows[b]["BASE"]["alphabet_class"] == "NR"
            and rows[b]["SHAM"]["alphabet_class"] == "NR"]
    w("S3e SHAM vs BASE on base draws whose native and sham alphabets are both non-resonant: %s"
      % fmt(paired([Y["SHAM"][i] for i in elig], [Y["BASE"][i] for i in elig], Z_95)))
    w("S4  resonant arms by the value set (the engine is exactly invariant under delta -> delta + N/2 on all nodes):")
    for arm, key in (("O1R", "r1"), ("O2R", "r2"), ("Q2R", "r2")):
        if arm in Y:
            byv = defaultdict(list)
            for i, b in enumerate(bases):
                byv[rows[b][arm]["choices"][key]].append(Y[arm][i])
            for v in sorted(byv):
                lo, hi = wilson(sum(byv[v]), len(byv[v]))
                w("      %s value %4d: n=%5d rate=%.4f [%.4f, %.4f]" % (arm, v, len(byv[v]), sum(byv[v]) / len(byv[v]), lo, hi))
    clean = []
    for i, b in enumerate(bases):
        r = rows[b]["BASE"]
        j = r["slot"]
        if all(res_class(x, N) == "NR" for q, x in enumerate(r["d0"]) if q != j):
            clean.append(i)
    w("S5  pairs whose three other tokens are non-resonant (n=%d):" % len(clean))
    for name, a1, a0 in (("O1R vs O1D", "O1R", "O1D"), ("O2R vs O2D", "O2R", "O2D")):
        if a1 in Y and a0 in Y:
            w("      %s: %s" % (name, fmt(paired([Y[a1][i] for i in clean], [Y[a0][i] for i in clean], Z_95))))
    w("S6  threshold sensitivity, rate of M >= c by arm:")
    for c in SECONDARY_THRESHOLDS:
        w("      c=%3d  " % c + "  ".join("%s %.4f" % (a, sum(int(rows[b][a]["M"] >= c) for b in bases) / len(bases))
                                           for a in arms))
    w("S7  mean share of the largest signed token class at the end, by arm and outcome (Y=1 / Y=0):")
    for a in arms:
        t1 = [rows[b][a]["top_share"] for b in bases if y_of(rows[b][a])]
        t0 = [rows[b][a]["top_share"] for b in bases if not y_of(rows[b][a])]
        w("      %-5s Y=1: n=%4d mean=%s   Y=0: n=%5d mean=%s"
          % (a, len(t1), "%.3f" % (sum(t1) / len(t1)) if t1 else "-", len(t0), "%.3f" % (sum(t0) / len(t0)) if t0 else "-"))
    w("S8  TDR-26 birth-anchored rule (b/step >= %.2f and ms_abs <= %.2f over [fb, fb+200)); separate output:" % (TDR26_B, TDR26_MS))
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
    if n_perm:
        mm = tot = 0
        key = lambda r: (r["M"], r["births"], r["steps"], r["fb"], json.dumps(r["M_at"], sort_keys=True))
        for b in bases:
            for a in ("BASE", "O1R"):
                if a + "_P" in rows[b]:
                    tot += 1
                    mm += key(rows[b][a]) != key(rows[b][a + "_P"])
        w("S9  node-label permutation control: %d of %d permuted runs differ from the unpermuted run in (M, births, steps, fb, M_at)" % (mm, tot))
    fbs = {a: sorted(rows[b][a]["fb"] for b in bases if rows[b][a]["fb"] is not None) for a in arms}
    w("S10 first-birth step, median by arm (runs with a birth): " + "  ".join(
        "%s %s (n=%d)" % (a, fbs[a][len(fbs[a]) // 2] if fbs[a] else "-", len(fbs[a])) for a in arms))
    return 0


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
    chk("decision: supported", decision(r, 1e-9).startswith("SUPPORTED"))
    chk("decision: not supported", decision(paired([0] * 995 + [1] * 5, [0] * 990 + [1] * 10, Z_975), 0.5).startswith("NOT SUPPORTED"))
    chk("decision: inconclusive", decision(paired([1] * 3 + [0] * 17, [0] * 20, Z_975), 0.25).startswith("INCONCLUSIVE"))
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--cell")
    ap.add_argument("--profile", default="P1")
    ap.add_argument("--n-base", type=int)
    ap.add_argument("--n-perm", type=int, default=0)
    ap.add_argument("--partial", action="store_true")
    ap.add_argument("--exclude-base", default="")
    ap.add_argument("--compare-profile", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.files and a.cell and a.n_base):
        ap.error("--cell, --n-base and at least one file are required")
    N = int(a.cell[1:a.cell.index("k")])
    exclude = {int(x) for x in a.exclude_base.split(",") if x}
    print("analysis script SHA-256 %s" % sha256_file(__file__))
    for path in a.files:
        with open(path, "rb") as f:
            n_lines = sum(1 for _ in f)
        print("input %s  SHA-256 %s  lines %d" % (path.replace("\\", "/").split("/")[-1], sha256_file(path), n_lines))
    rows, dup = load(a.files, a.cell, a.profile)
    if dup and not a.partial:
        print("DUPLICATE records: %d" % dup)
        return 2
    rc = analyse(rows, N, a.n_base, a.n_perm, a.partial, exclude, label="profile %s  " % a.profile)
    if rc == 0 and a.compare_profile:
        rows2, _ = load(a.files, a.cell, a.compare_profile)
        common = [(b, arm) for b in rows2 for arm in rows2[b] if arm in rows.get(b, {})]
        same = sum(rows[b][arm]["M"] == rows2[b][arm]["M"] and rows[b][arm]["births"] == rows2[b][arm]["births"]
                   for b, arm in common)
        print("\n[sensitivity] profile %s versus %s on %d common (base, arm) runs: identical (M, births) in %d; "
              "Y differs in %d" % (a.profile, a.compare_profile, len(common), same,
                                   sum(y_of(rows[b][arm]) != y_of(rows2[b][arm]) for b, arm in common)))
        nb2 = max(rows2) + 1 if rows2 else 0
        print("--- registered contrasts recomputed under profile %s (descriptive) ---" % a.compare_profile)
        analyse(rows2, N, nb2, 0, True, exclude, label="profile %s  " % a.compare_profile)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
