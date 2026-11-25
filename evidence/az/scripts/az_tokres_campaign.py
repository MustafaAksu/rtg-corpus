#!/usr/bin/env python3
"""AZ token-resonance campaign driver - [SESSION] NONCANONICAL. One command for a whole plan, fail-fast.

It runs, from the repository root derived from its own location:
  1. the fixtures on this machine                      (exit code must be 0; log kept as fixtures_output.txt);
  2. every cell of the plan as parallel shards         (every worker's exit code must be 0);
  3. a check of every shard (record file, manifest, expected record count);
  4. the registered analysis of every cell             (exit code must be 0: integrity and gates passed);
  5. HASHES.txt over the output directory and, only if everything above succeeded, CAMPAIGN_COMPLETE.json.
On the first failure it writes CAMPAIGN_FAILED.txt, writes no completion marker and exits with code 1. A directory
without CAMPAIGN_COMPLETE.json is not a campaign result.

usage
  python -I az_tokres_campaign.py --plan stage1 --out DIR --jobs 4 --confirmatory     (PI-authorised run only)
  python -I az_tokres_campaign.py --plan test   --out DIR --jobs 2 [--skip-fixtures LOG]
  add --resume to continue an interrupted run in the same DIR (workers refuse records of another identity).
The registered parameters are read from the analysis script's REGISTRY; this file adds none.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import platform
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
ENGINE = os.path.join(ROOT, "upload", "tdrg-records", "genesis_mode_b_mc.py")
ORIENT = os.path.join(ROOT, "evidence", "tdrg", "scripts", "tdrg_orient_v2_12_14.py")
RUNNER = os.path.join(HERE, "az_tokres_run.py")
FIXTURES = os.path.join(HERE, "az_tokres_fixtures.py")
ANALYSE = os.path.join(HERE, "az_tokres_analyse.py")
GOLDEN = os.path.join(ROOT, "evidence", "az", "token_resonance", "fixtures", "golden.json")
PLANS = {"stage1": ("S1-C1", "S1-C2", "S1-C3"), "test": ("TEST-C1", "TEST-C2", "TEST-C3")}
SENSITIVITY_OF = {"S1-C1": "S1-C3", "TEST-C1": "TEST-C3"}


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Failed(Exception):
    pass


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", required=True, choices=sorted(PLANS))
    ap.add_argument("--out", required=True)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--confirmatory", action="store_true")
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--skip-fixtures", default=None, help="test plan only: use this existing fixtures log")
    a = ap.parse_args()

    if a.plan == "stage1" and not a.confirmatory:
        print("REFUSED: plan stage1 needs --confirmatory (PI-authorised run only)", file=sys.stderr)
        return 2
    if a.plan != "stage1" and a.confirmatory:
        print("REFUSED: --confirmatory is reserved for plan stage1", file=sys.stderr)
        return 2
    if a.skip_fixtures and a.plan != "test":
        print("REFUSED: --skip-fixtures is for the test plan only", file=sys.stderr)
        return 2
    if a.jobs < 1:
        print("REFUSED: --jobs must be at least 1", file=sys.stderr)
        return 2
    out = os.path.abspath(a.out)
    if os.path.exists(out) and os.listdir(out) and not a.resume:
        print("REFUSED: output directory exists and is not empty; use --resume or another --out", file=sys.stderr)
        return 2
    os.makedirs(os.path.join(out, "logs"), exist_ok=True)
    for stale in ("CAMPAIGN_COMPLETE.json", "CAMPAIGN_FAILED.txt", "HASHES.txt"):
        if os.path.exists(os.path.join(out, stale)):
            os.remove(os.path.join(out, stale))

    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("az_tokres_analyse", ANALYSE)
    an = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(an)
    py = [sys.executable, "-I"]
    t0 = time.time()
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    steps = []

    def note(msg):
        print(msg, flush=True)
        steps.append(msg)

    try:
        # ---- 1. fixtures
        flog = os.path.join(out, "fixtures_output.txt")
        if a.skip_fixtures:
            shutil.copyfile(a.skip_fixtures, flog)
            note("fixtures: log copied from %s (test plan)" % os.path.basename(a.skip_fixtures))
        else:
            with open(flog, "w", newline="\n") as f:
                rc = subprocess.call(py + [FIXTURES, "--engine", ENGINE, "--orient", ORIENT, "--runner", RUNNER,
                                           "--analysis", ANALYSE, "--golden", GOLDEN], stdout=f, stderr=subprocess.STDOUT)
            if rc != 0:
                raise Failed("fixtures exited with code %d (see fixtures_output.txt)" % rc)
            note("fixtures: exit code 0")

        # ---- 2-3. shards
        files = {}
        for cell in PLANS[a.plan]:
            cfg = an.REGISTRY[cell]
            n_base, jobs = cfg["n_base"], min(a.jobs, cfg["n_base"])
            bounds = [round(i * n_base / jobs) for i in range(jobs + 1)]
            procs = []
            for i in range(jobs):
                lo, hi = bounds[i], bounds[i + 1]
                path = os.path.join(out, "%s_%05d_%05d.jsonl" % (cell, lo, hi))
                # workers run inside the output directory and get the bare file name: no local path enters a log
                cmd = py + [RUNNER, "--engine", ENGINE, "--orient", ORIENT, "--out", os.path.basename(path), "--tag", cfg["tag"],
                            "--N", str(cfg["N"]), "--k", str(cfg["k"]), "--T", str(cfg["T"]), "--cap", str(cfg["cap"]),
                            "--profile", cfg["profile"], "--policy", cfg["policy"], "--start", str(lo), "--stop", str(hi),
                            "--n-perm", str(cfg["n_perm"])]
                if cfg["confirmatory"]:
                    cmd.append("--confirmatory")
                if a.resume and (os.path.exists(path) or os.path.exists(path + ".manifest.json")):
                    cmd.append("--resume")
                log = open(os.path.join(out, "logs", "%s_%05d.log" % (cell, lo)), "a", newline="\n")
                procs.append((subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, cwd=out), log, path, lo, hi))
            codes = []
            for p, log, path, lo, hi in procs:
                codes.append(p.wait())
                log.close()
            if any(codes):
                raise Failed("cell %s: worker exit codes %s (see logs)" % (cell, codes))
            arms = an.arms_for(cfg["N"])
            for p, log, path, lo, hi in procs:
                want = (hi - lo) * len(arms) + 2 * max(0, min(hi, cfg["n_perm"]) - lo)
                if not os.path.exists(path) or not os.path.exists(path + ".manifest.json"):
                    raise Failed("cell %s: shard %d-%d has no record file or no manifest" % (cell, lo, hi))
                with open(path, "rb") as f:
                    got = sum(1 for _ in f)
                if got != want:
                    raise Failed("cell %s: shard %d-%d has %d records, expected %d" % (cell, lo, hi, got, want))
            files[cell] = [x[2] for x in procs]
            note("cell %s: %d shard(s), all exit codes 0, record counts as expected" % (cell, jobs))

        # ---- 4. analysis (fail-closed inside the analysis script)
        for cell in PLANS[a.plan]:
            if cell in SENSITIVITY_OF.values():
                continue
            cmd = py + [ANALYSE, "--registered", cell, "--engine", ENGINE, "--orient", ORIENT, "--runner", RUNNER,
                        "--fixtures-log", flog] + files[cell]
            if cell in SENSITIVITY_OF:
                cmd += ["--sensitivity"] + files[SENSITIVITY_OF[cell]]
            with open(os.path.join(out, "analysis_%s.txt" % cell), "w", newline="\n") as f:
                rc = subprocess.call(cmd, stdout=f, stderr=subprocess.STDOUT)
            if rc != 0:
                raise Failed("analysis of %s exited with code %d (2 = integrity, 3 = gate); see analysis_%s.txt" % (cell, rc, cell))
            note("analysis %s: exit code 0" % cell)
    except Failed as ex:
        with open(os.path.join(out, "CAMPAIGN_FAILED.txt"), "w", newline="\n") as f:
            f.write("CAMPAIGN FAILED: %s\n" % ex + "".join("  done before the failure: %s\n" % s for s in steps))
        print("CAMPAIGN FAILED: %s" % ex, file=sys.stderr)
        return 1

    # ---- 5. hashes and completion marker
    listing = []
    for d, _, fs in os.walk(out):
        for name in fs:
            p = os.path.join(d, name)
            listing.append((os.path.relpath(p, out).replace(os.sep, "/"), sha256_file(p)))
    listing.sort()
    with open(os.path.join(out, "HASHES.txt"), "w", newline="\n") as f:
        f.write("".join("%s  %s\n" % (h, rel) for rel, h in listing))
    marker = {"schema": "az_tokres_campaign_v1", "plan": a.plan, "cells": list(PLANS[a.plan]), "jobs": a.jobs,
              "confirmatory": bool(a.confirmatory), "resumed": bool(a.resume), "fixtures_skipped": bool(a.skip_fixtures),
              "started_utc": started, "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "seconds": round(time.time() - t0, 1), "python": sys.version.split()[0], "platform": platform.platform(),
              "records": {c: sum(1 for p in files[c] for _ in open(p, "rb")) for c in files},
              "sha256": {"engine": sha256_file(ENGINE), "orient": sha256_file(ORIENT), "runner": sha256_file(RUNNER),
                         "fixtures": sha256_file(FIXTURES), "analysis": sha256_file(ANALYSE), "golden": sha256_file(GOLDEN),
                         "driver": sha256_file(os.path.abspath(__file__)), "HASHES.txt": sha256_file(os.path.join(out, "HASHES.txt"))},
              "steps": steps}
    with open(os.path.join(out, "CAMPAIGN_COMPLETE.json"), "w", newline="\n") as f:
        json.dump(marker, f, sort_keys=True, indent=1)
        f.write("\n")
    print("CAMPAIGN COMPLETE: %s" % json.dumps(marker["records"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
