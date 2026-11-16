#!/usr/bin/env python3
"""AZ Action 1, Stage 2: timing and calibration pilot - [SESSION] NONCANONICAL, EXPLORATORY.

Not a confirmatory run. It runs the NATIVE arm only (the engine's own initial draw, no token
replacement), so that the Stage 2 registration can fix its horizon and its tail threshold
without seeing any exposure contrast at the new N.

    python3 -I az_tokres_s2_pilot.py run     --engine E --orient O --runner R --out DIR [--plan pilot|test] [--resume]
    python3 -I az_tokres_s2_pilot.py summary --out DIR [--plan pilot|test]
    python3 -I az_tokres_s2_pilot.py selftest --engine E --orient O --runner R

`run` uses the registered runner as a library (its SHA-256 is asserted; it is not changed):
load_engine (profile P1: pinned engine + TDRG-DEF-ORIENT reference), base_draw and run_state.
Seeds derive from the pilot tag below, so no base draw is shared with Stage 1 or with a later
registered Stage 2 tag. Each cell writes DIR/<cell>.jsonl (one record per native run) and, when
complete, a line in DIR/MANIFEST.jsonl; DIR/PILOT_COMPLETE.json is written only when every cell
is complete.

`summary` prints, per cell: run time; and for native draws WITHOUT a resonant seed token only,
the distribution of the final node count M. It does not print anything about draws that carry
a resonant token (4x = 0 mod N); those records are in the files and are left for a registered
analysis.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import platform
import sys
import time

TAG = "S2-CALIB-PILOT-20261112"
RUNNER_SHA256 = "75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992"
POLICY = "bound_symmetric"
CAP = 300
# (N, k, T, number of native draws). k/N = 1/15 as in Stage 1 (N = 242: k = 16, as N = 122 used k = 8).
# T = 800 is the Stage 1 horizon; the second horizon scales it by (N/120)^0.87, the owner's
# full-range exponent for the bulk birth rate (TDR-G v2.12.14 §1), rounded to 10.
PLANS = {
    "pilot": [(120, 8, 800, 3000),
              (240, 16, 800, 3000), (240, 16, 1460, 3000),
              (242, 16, 800, 3000), (242, 16, 1460, 3000),
              (480, 32, 800, 3000), (480, 32, 2670, 3000)],
    "test": [(120, 8, 800, 12), (240, 16, 800, 8), (242, 16, 1460, 8)],
}
SCHEMA = "az_tokres_s2_pilot_v1"


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def load_runner(path):
    if sha256_file(path) != RUNNER_SHA256:
        sys.exit("REFUSED: runner is not the registered runner %s" % RUNNER_SHA256)
    spec = importlib.util.spec_from_file_location("az_tokres_run", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["az_tokres_run"] = mod
    spec.loader.exec_module(mod)
    return mod


def cell_name(N, k, T):
    return "N%dk%dT%d" % (N, k, T)


def identity(rn, info, N, k, T):
    return {"schema": SCHEMA, "tag": TAG, "cell": cell_name(N, k, T), "N": N, "k": k, "T": T, "cap": CAP, "profile": "P1",
            "policy": POLICY, "arm": "BASE", "engine_sha256": info["engine_sha256"], "orient_sha256": info["orient_sha256"],
            "runner_sha256": RUNNER_SHA256, "pilot_sha256": sha256_file(os.path.abspath(__file__))}


def one(rn, eng, N, k, T, b):
    seed, th0, d0 = rn.base_draw(eng, TAG, N, k, b)
    t1 = time.time()
    res = rn.run_state(eng, N, k, th0, d0, T, CAP, POLICY, tdr26=False)
    return {"base": b, "seed": seed, "d0": d0, "native_class": rn.alphabet_class(d0, N), "M": res["M"],
            "hit_cap": res["hit_cap"], "t100": res["t100"], "births": res["births"], "steps": res["steps"],
            "M_at": res["M_at"], "law_viol": res["law_viol"], "secs": round(time.time() - t1, 4)}


def cmd_run(a):
    rn = load_runner(a.runner)
    eng, info = rn.load_engine(a.engine, a.orient, "P1")
    os.makedirs(a.out, exist_ok=True)
    man_path = os.path.join(a.out, "MANIFEST.jsonl")
    done_cells = {}
    if os.path.exists(man_path):
        for line in open(man_path):
            m = json.loads(line)
            done_cells[m["identity"]["cell"]] = m
    t_all = time.time()
    for (N, k, T, n) in PLANS[a.plan]:
        ident = identity(rn, info, N, k, T)
        path = os.path.join(a.out, ident["cell"] + ".jsonl")
        if ident["cell"] in done_cells:
            m = done_cells[ident["cell"]]
            if m["identity"] != ident or m["n"] != n or sha256_file(path) != m["file_sha256"]:
                sys.exit("REFUSED: %s was completed under another identity, size or content" % ident["cell"])
            print("cell %s: complete (%d runs), skipped" % (ident["cell"], n), flush=True)
            continue
        have = 0
        if os.path.exists(path):
            if not a.resume:
                sys.exit("REFUSED: %s exists; use --resume" % path)
            for i, line in enumerate(open(path)):
                r = json.loads(line)
                if {x: r[x] for x in ident} != ident or r["base"] != i:
                    sys.exit("REFUSED: %s line %d was written under another identity or order" % (path, i + 1))
                have = i + 1
        t0 = time.time()
        with open(path, "a", newline="\n") as f:
            for b in range(have, n):
                rec = dict(ident)
                rec.update(one(rn, eng, N, k, T, b))
                f.write(json.dumps(rec, sort_keys=True) + "\n")
                f.flush()
                if (b + 1) % 500 == 0:
                    print("cell %s: %d/%d  (%.0f s)" % (ident["cell"], b + 1, n, time.time() - t0), flush=True)
        rows = sum(1 for _ in open(path))
        if rows != n:
            sys.exit("STOP: %s has %d rows, expected %d" % (path, rows, n))
        with open(man_path, "a", newline="\n") as f:
            f.write(json.dumps({"identity": ident, "n": n, "file_sha256": sha256_file(path), "seconds_this_invocation": round(time.time() - t0, 1),
                                "python": sys.version.split()[0], "platform": platform.platform(),
                                "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, sort_keys=True) + "\n")
        print("cell %s: done, %d runs" % (ident["cell"], n), flush=True)
    cells = [cell_name(N, k, T) for (N, k, T, n) in PLANS[a.plan]]
    mans = {json.loads(l)["identity"]["cell"]: json.loads(l) for l in open(man_path)}
    if sorted(mans) != sorted(cells):
        sys.exit("STOP: manifest cells differ from the plan")
    with open(os.path.join(a.out, "PILOT_COMPLETE.json"), "w") as f:
        json.dump({"schema": SCHEMA, "tag": TAG, "plan": a.plan, "cells": {c: {"n": mans[c]["n"], "file_sha256": mans[c]["file_sha256"]} for c in cells},
                   "manifest_sha256": sha256_file(man_path), "python": sys.version.split()[0],
                   "seconds_this_invocation": round(time.time() - t_all, 1),
                   "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, f, indent=1, sort_keys=True)
    print("PILOT COMPLETE: %d cells" % len(cells))
    return 0


def quantile(sorted_vals, p):
    """Smallest value v with at least a fraction p of the sample <= v."""
    n = len(sorted_vals)
    i = max(0, min(n - 1, int(-(-p * n // 1)) - 1))
    return sorted_vals[i]


def cmd_summary(a):
    man_path = os.path.join(a.out, "MANIFEST.jsonl")
    mans = {json.loads(l)["identity"]["cell"]: json.loads(l) for l in open(man_path)}
    print("AZ Action 1 Stage 2 pilot summary - native arm; outcomes shown for draws WITHOUT a resonant seed token only")
    print("tag %s" % TAG)
    ok = True
    ref = None
    rows = []
    for (N, k, T, n) in PLANS[a.plan]:
        c = cell_name(N, k, T)
        path = os.path.join(a.out, c + ".jsonl")
        if c not in mans or sha256_file(path) != mans[c]["file_sha256"]:
            print("%s: missing or not matching its manifest hash" % c)
            ok = False
            continue
        R = [json.loads(l) for l in open(path)]
        if len(R) != n or [r["base"] for r in R] != list(range(n)) or any(r["law_viol"] for r in R):
            print("%s: wrong number or order of records, or a law violation" % c)
            ok = False
            continue
        secs = sorted(r["secs"] for r in R)
        NR = sorted(r["M"] for r in R if r["native_class"] == "NR")
        rows.append((c, N, k, T, n, sum(secs), secs[len(secs) // 2], secs[-1], NR))
        if (N, k, T) == (120, 8, 800):
            ref = NR
    alpha = None
    if ref:
        alpha = sum(1 for m in ref if m >= 100) / len(ref)
    print("\n%-14s %6s %9s %8s %8s | %6s %5s %5s %5s %5s %5s %5s | %8s %s" % (
        "cell", "runs", "secs_sum", "secs_med", "secs_max", "n_NR", "q50", "q90", "q95", "q99", "q99.5", "max", "P(M>=100)", "theta_ref"))
    for (c, N, k, T, n, ssum, smed, smax, NR) in rows:
        q = lambda p: quantile(NR, p)
        f100 = sum(1 for m in NR if m >= 100) / len(NR)
        theta = ""
        if alpha is not None:
            # smallest integer m with exceedance fraction of M >= m not above alpha (at the reference cell m <= 100)
            m = 1
            while sum(1 for x in NR if x >= m) / len(NR) > alpha and m <= CAP:
                m += 1
            theta = str(m)
        print("%-14s %6d %9.0f %8.2f %8.1f | %6d %5d %5d %5d %5d %5d %5d | %8.4f %s" % (
            c, n, ssum, smed, smax, len(NR), q(0.5), q(0.9), q(0.95), q(0.99), q(0.995), NR[-1], f100, theta))
    if alpha is not None:
        print("\nreference exceedance alpha = P(M >= 100 | no resonant seed token) at N120k8T800 = %.4f (%d of %d)" % (
            alpha, sum(1 for m in ref if m >= 100), len(ref)))
        print("theta_ref = smallest integer m whose exceedance fraction among non-resonant native draws is <= alpha")
    print("\nRESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def cmd_selftest(a):
    """The pilot's native run equals the registered runner's own BASE arm for the same tag and base draw."""
    rn = load_runner(a.runner)
    eng, info = rn.load_engine(a.engine, a.orient, "P1")
    ok = True
    for (N, k, T) in ((120, 8, 800), (242, 16, 300)):
        for b in range(4):
            mine = one(rn, eng, N, k, T, b)
            seed, th0, d0 = rn.base_draw(eng, TAG, N, k, b)
            th, d = rn.arm_state("BASE", th0, d0, rn.arm_choices(TAG, N, k, b), N)
            ref = rn.run_state(eng, N, k, th, d, T, CAP, POLICY, tdr26=True)
            same = all(mine[x] == ref[x] for x in ("M", "hit_cap", "t100", "births", "steps", "M_at", "law_viol")) and d == d0 and th == th0
            ok &= same
            print("N=%d k=%d T=%d base=%d: pilot M=%d births=%d | runner BASE M=%d births=%d | %s" % (
                N, k, T, b, mine["M"], mine["births"], ref["M"], ref["births"], "equal" if same else "DIFFERENT"))
    # the seed of a pilot draw differs from the Stage 1 seed of the same index
    d1 = rn.derive_int(TAG, "N120", "k8", "base", 0) != rn.derive_int("AZ-TOKRES-S1", "N120", "k8", "base", 0)
    print("pilot seed differs from the Stage 1 seed of the same index: %s" % d1)
    ok &= d1
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run", "summary", "selftest"])
    ap.add_argument("--engine")
    ap.add_argument("--orient")
    ap.add_argument("--runner")
    ap.add_argument("--out")
    ap.add_argument("--plan", default="pilot", choices=sorted(PLANS))
    ap.add_argument("--resume", action="store_true")
    a = ap.parse_args()
    return {"run": cmd_run, "summary": cmd_summary, "selftest": cmd_selftest}[a.cmd](a)


if __name__ == "__main__":
    raise SystemExit(main())
