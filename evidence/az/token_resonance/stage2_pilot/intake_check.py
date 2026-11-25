#!/usr/bin/env python3
"""Intake check and calibration table for the AZ Action 1 Stage 2 pilot - [SESSION], exploratory.

    python3 -I intake_check.py --dir upload/az-token-resonance-s2-pilot --pilot-script PATH [--sums SHA256SUMS]

Custody: HASHES.txt, MANIFEST.jsonl and PILOT_COMPLETE.json agree with the files; every record
carries the identity of its cell and the hashes of the engine, orientation reference, runner
and pilot script named in SHA256SUMS; records are complete, in order, with no law violation;
the stored summary equals a rerun of the pilot script's own summary.

Calibration (plan §3, §4, §8): outcomes are read ONLY for native draws without a resonant
seed token (native_class == "NR"). For every other record this script reads identity fields
(including the draw index and the law-violation counter) and the run time, never M, hit_cap,
t100, births or M_at.
"""
import argparse, hashlib, json, math, os, subprocess, sys

PLAN = [(120, 8, 800), (240, 16, 800), (240, 16, 1460), (242, 16, 800), (242, 16, 1460), (480, 32, 800), (480, 32, 2670)]
REF = (120, 8, 800)
SCALED = {240: 1460, 242: 1460, 480: 2670}
N_RUNS = 3000
ID_KEYS = ("schema", "tag", "cell", "N", "k", "T", "cap", "profile", "policy", "arm", "engine_sha256", "orient_sha256", "runner_sha256", "pilot_sha256")


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def binom_cdf(k, n, p):
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    # sum of pmf, in logs
    s = 0.0
    lp, lq = math.log(p), math.log1p(-p)
    for i in range(0, k + 1):
        s += math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) + i * lp + (n - i) * lq)
    return min(1.0, s)


def clopper_pearson(x, n, conf=0.95):
    a = (1 - conf) / 2
    def solve(f, lo, hi):
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    lower = 0.0 if x == 0 else solve(lambda p: 1 - binom_cdf(x - 1, n, p) < a, 0.0, 1.0)
    upper = 1.0 if x == n else solve(lambda p: binom_cdf(x, n, p) > a, 0.0, 1.0)
    return lower, upper


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--pilot-script", required=True)
    ap.add_argument("--sums", default=None)
    a = ap.parse_args()
    D = a.dir
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print("%s  %s%s" % ("PASS" if cond else "FAIL", name, ("  - " + detail) if detail else ""))

    print("AZ Action 1 Stage 2 pilot - intake check and calibration table ([SESSION], exploratory)")
    print("intake script sha256 %s" % sha(os.path.abspath(__file__)))
    # ---- custody
    listed = {}
    for ln in open(os.path.join(D, "HASHES.txt")):
        h, p = ln.split()
        listed[p.lstrip("*")] = h
    check("HASHES.txt lists the 7 record files, MANIFEST.jsonl, PILOT_COMPLETE.json and summary.txt", len(listed) == 10)
    check("every listed file has its listed hash", all(sha(os.path.join(D, p)) == h for p, h in listed.items()))
    mans = {}
    for ln in open(os.path.join(D, "MANIFEST.jsonl")):
        m = json.loads(ln)
        mans[m["identity"]["cell"]] = m
    comp = json.load(open(os.path.join(D, "PILOT_COMPLETE.json")))
    cells = ["N%dk%dT%d" % c for c in PLAN]
    check("manifest and completion marker name exactly the 7 planned cells", sorted(mans) == sorted(cells) and sorted(comp["cells"]) == sorted(cells))
    check("manifest hash in the completion marker", comp["manifest_sha256"] == sha(os.path.join(D, "MANIFEST.jsonl")))
    check("record-file hashes agree in manifest, completion marker and files",
          all(mans[c]["file_sha256"] == comp["cells"][c]["file_sha256"] == sha(os.path.join(D, c + ".jsonl")) for c in cells))
    want = {}
    if a.sums:
        for ln in open(a.sums):
            h, p = ln.split()
            want[os.path.basename(p)] = h
    pilot_sha = sha(a.pilot_script)
    check("pilot script used for the rerun is the one named in SHA256SUMS", (not want) or want.get("az_tokres_s2_pilot.py") == pilot_sha, pilot_sha)

    NR = {}
    secs = {}
    BANDS = {}
    ORD = {}

    def ord2(x, N):
        # additive order of 2x in Z_N (1 for 2x = 0, 2 for 2x = N/2: the two resonant classes; larger otherwise)
        y = (2 * x) % N
        return N // math.gcd(y, N) if y else 1
    for (N, k, T) in PLAN:
        c = "N%dk%dT%d" % (N, k, T)
        ident = mans[c]["identity"]
        good = ident["N"] == N and ident["k"] == k and ident["T"] == T and ident["cap"] == 300 and ident["profile"] == "P1" \
            and ident["policy"] == "bound_symmetric" and ident["arm"] == "BASE" and ident["pilot_sha256"] == pilot_sha
        if want:
            good = good and ident["engine_sha256"] == want["genesis_mode_b_mc.py"] and ident["orient_sha256"] == want["tdrg_orient_v2_12_14.py"] \
                and ident["runner_sha256"] == want["az_tokres_run.py"]
        n = 0
        nr = []
        ss = []
        viol = 0
        order = True
        for i, ln in enumerate(open(os.path.join(D, c + ".jsonl"))):
            r = json.loads(ln)
            n += 1
            order &= (r["base"] == i)
            good &= all(r[x] == ident[x] for x in ID_KEYS)
            viol += r["law_viol"]
            ss.append(r["secs"])
            if r["native_class"] == "NR":          # outcomes are read for these records only
                nr.append(r["M"])
                ORD.setdefault((N, k, T), []).append((min(ord2(x, N) for x in r["d0"]), r["M"]))
                band = "cap" if r["hit_cap"] else ("100-299" if r["M"] >= 100 else "<100")
                BANDS.setdefault((N, k, T), {}).setdefault(band, []).append(r["secs"])
        check("%s: %d records, in order, cell identity and pinned hashes on every record, law violations %d" % (c, n, viol),
              good and order and n == N_RUNS and viol == 0)
        NR[(N, k, T)] = sorted(nr)
        secs[(N, k, T)] = ss
    r = subprocess.run([sys.executable, "-I", a.pilot_script, "summary", "--out", D], capture_output=True, text=True)
    check("stored summary.txt equals a rerun of the pilot script's summary", r.returncode == 0 and r.stdout == open(os.path.join(D, "summary.txt")).read())

    # ---- calibration
    ref = NR[REF]
    x_ref = sum(1 for m in ref if m >= 100)
    alpha = x_ref / len(ref)
    lo, hi = clopper_pearson(x_ref, len(ref))
    print("\nreference cell N120k8T800: non-resonant native draws %d, with M >= 100: %d" % (len(ref), x_ref))
    print("alpha = %.5f, exact 95 %% interval [%.5f, %.5f]" % (alpha, lo, hi))
    print("\n%-14s %6s %6s %9s %9s %22s %9s %8s %7s %7s" % ("cell", "n_NR", "theta", "exceed", "realised", "exact 95% of realised", "- alpha", "in CI(a)", "th<=200", "gap"))
    table = {}
    for (N, k, T) in PLAN:
        v = NR[(N, k, T)]
        m = 1
        while sum(1 for x in v if x >= m) / len(v) > alpha and m <= 300:
            m += 1
        x = sum(1 for y in v if y >= m)
        rate = x / len(v)
        l2, h2 = clopper_pearson(x, len(v))
        below = max([y for y in v if y < m] or [0])
        in_ci = lo <= rate <= hi
        table[(N, k, T)] = (m, x, rate, in_ci, m <= 200)
        print("%-14s %6d %6d %9d %9.5f     [%.5f, %.5f] %+9.5f %8s %7s %7s" % (
            "N%dk%dT%d" % (N, k, T), len(v), m, x, rate, l2, h2, rate - alpha, "yes" if in_ci else "no", "yes" if m <= 200 else "no",
            "%d..%d" % (below, m)))
    print("\ngap = largest non-resonant M below theta .. theta (the step of the integer threshold)")

    print("\nhorizon and threshold by the rules fixed before the pilot (plan §4 and §8 item 2):")
    for N in (240, 242, 480):
        k = {240: 16, 242: 16, 480: 32}[N]
        Ts = SCALED[N]
        m, x, rate, in_ci, small = table[(N, k, Ts)]
        if small and in_ci:
            print("  N = %d: scaled horizon T = %d, theta = %d  (valid: theta <= 200 and realised rate inside the interval of alpha)" % (N, Ts, m))
        else:
            m8, x8, rate8, in8, small8 = table[(N, k, 800)]
            if small8 and in8:
                print("  N = %d: scaled horizon not valid (theta = %d, in interval: %s); fallback T = 800, theta = %d" % (N, m, in_ci, m8))
            else:
                print("  N = %d: NOT A VALID CALIBRATION at either horizon (scaled: theta = %d, in interval %s; T = 800: theta = %d, in interval %s)" % (
                    N, m, in_ci, m8, in8))

    # ---- how firmly the pilot fixes the thresholds (non-resonant draws only)
    def theta_at(v, a_):
        m = 1
        while sum(1 for x in v if x >= m) / len(v) > a_ and m <= 300:
            m += 1
        return m
    print("\nsensitivity of theta (the in-sample check above holds almost by construction; these do not):")
    print("%-14s %7s %16s %16s | %s" % ("cell", "theta", "theta at CI-hi(a)", "theta at CI-lo(a)", "split by parity of the draw index: theta from one half, exceedances in the other half"))
    for (N, k, T) in PLAN:
        c = "N%dk%dT%d" % (N, k, T)
        ev, od = [], []
        for ln in open(os.path.join(D, c + ".jsonl")):
            r = json.loads(ln)
            if r["native_class"] == "NR":
                (ev if r["base"] % 2 == 0 else od).append(r["M"])
        v = NR[(N, k, T)]
        te, to = theta_at(ev, alpha), theta_at(od, alpha)
        xe = sum(1 for y in od if y >= te)
        xo = sum(1 for y in ev if y >= to)
        print("%-14s %7d %16d %16d | even->odd theta %3d: %2d of %4d (%.5f);  odd->even theta %3d: %2d of %4d (%.5f)" % (
            c, table[(N, k, T)][0], theta_at(v, hi), theta_at(v, lo), te, xe, len(od), xe / len(od), to, xo, len(ev), xo / len(ev)))
    print("\nfraction of native draws with a resonant seed token (identity field only): " + ", ".join(
        "N=%d: %d of %d" % (N, N_RUNS - len(NR[(N, k, T)]), N_RUNS) for (N, k, T) in PLAN if T == 800))
    x91 = sum(1 for m in ref if m >= 91)
    print("reference cell: non-resonant draws with M >= 91: %d, with M >= 100: %d (no non-resonant value in 91..99: %s)" % (
        x91, x_ref, "yes" if x91 == x_ref else "no"))

    def fisher2(a_, b_, c_, d_):
        # two-sided Fisher exact test for the table [[a, b], [c, d]] (sum of tables no more probable than the observed)
        n1, n2, m1 = a_ + b_, c_ + d_, a_ + c_
        def lp(x):
            return (math.lgamma(n1 + 1) - math.lgamma(x + 1) - math.lgamma(n1 - x + 1) + math.lgamma(n2 + 1) - math.lgamma(m1 - x + 1)
                    - math.lgamma(n2 - m1 + x + 1) - (math.lgamma(n1 + n2 + 1) - math.lgamma(m1 + 1) - math.lgamma(n1 + n2 - m1 + 1)))
        l0 = lp(a_)
        return min(1.0, sum(math.exp(lp(x)) for x in range(max(0, m1 - n2), min(n1, m1) + 1) if lp(x) <= l0 + 1e-9))
    print("\nfixed threshold M >= 100 among non-resonant native draws (count of n_NR), and N = 240 against N = 242 (exploratory, post hoc):")
    for T in (800, 1460):
        v0, v2 = NR[(240, 16, T)], NR[(242, 16, T)]
        a0, a2 = sum(1 for y in v0 if y >= 100), sum(1 for y in v2 if y >= 100)
        print("  T = %4d: N = 240: %2d of %d;  N = 242: %2d of %d;  Fisher exact two-sided p = %.4f" % (
            T, a0, len(v0), a2, len(v2), fisher2(a0, len(v0) - a0, a2, len(v2) - a2)))
    print("  N = 480: T = 800: %d of %d;  T = 2670: %d of %d" % (
        sum(1 for y in NR[(480, 32, 800)] if y >= 100), len(NR[(480, 32, 800)]), sum(1 for y in NR[(480, 32, 2670)] if y >= 100), len(NR[(480, 32, 2670)])))

    print("\nnon-resonant native draws by the smallest additive order of 2x among the four seed tokens")
    print("(exploratory, post hoc: the classification and the cut at 6 were chosen after the calibration table was seen;")
    print(" orders 1 and 2 are the resonant classes and do not occur here)")
    for (N, k, T) in PLAN:
        c = "N%dk%dT%d" % (N, k, T)
        th = 100 if (N, k, T) == REF else table[(N, k, T)][0]
        tab = {}
        for o, m in ORD[(N, k, T)]:
            key = o if o <= 12 else 13
            t = tab.setdefault(key, [0, 0, 0])
            t[0] += 1
            t[1] += m >= th
            t[2] += m >= 100
        print("  %s  (theta = %d)" % (c, th))
        for key in sorted(tab):
            n_, a_, b_ = tab[key]
            print("      min order %-4s n = %4d   M >= theta: %2d   M >= 100: %2d" % (str(key) if key <= 12 else ">12", n_, a_, b_))
        lo_n = sum(v[0] for q, v in tab.items() if q <= 6)
        lo_x = sum(v[1] for q, v in tab.items() if q <= 6)
        hi_n = sum(v[0] for q, v in tab.items() if q > 6)
        hi_x = sum(v[1] for q, v in tab.items() if q > 6)
        gen = sorted(m for o, m in ORD[(N, k, T)] if o > 6)
        q = lambda f: gen[min(len(gen) - 1, int(f * len(gen)))]
        if lo_n:
            print("      order <= 6: %d of %d;  order > 6: %d of %d;  Fisher exact two-sided p = %.2e (post hoc cut)" % (
                lo_x, lo_n, hi_x, hi_n, fisher2(lo_x, lo_n - lo_x, hi_x, hi_n - hi_x)))
        else:
            print("      no seed token of order <= 6 exists at this N;  order > 6: %d of %d" % (hi_x, hi_n))
        print("      draws with every order > 6: n = %d, M quantiles 50 / 90 / 99 / 99.5 %% = %d / %d / %d / %d, max %d" % (
            len(gen), q(0.5), q(0.9), q(0.99), q(0.995), gen[-1]))

    print("\nrun time by final size, non-resonant native draws only (count, mean seconds):")
    for (N, k, T) in PLAN:
        b_ = BANDS[(N, k, T)]
        print("  %-14s " % ("N%dk%dT%d" % (N, k, T)) + ";  ".join(
            "%s: %4d, %7.2f s" % (nm, len(b_.get(nm, [])), (sum(b_[nm]) / len(b_[nm])) if b_.get(nm) else float("nan")) for nm in ("<100", "100-299", "cap")))

    print("\nrun time, native arm, all draws (seconds): cell, sum, mean, median, max")
    for (N, k, T) in PLAN:
        ss = sorted(secs[(N, k, T)])
        print("  %-14s %8.0f %7.3f %7.3f %8.1f" % ("N%dk%dT%d" % (N, k, T), sum(ss), sum(ss) / len(ss), ss[len(ss) // 2], ss[-1]))
    print("\nRESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
