#!/usr/bin/env python3
"""AZ token-resonance Stage 2 campaign driver - [SESSION] NONCANONICAL. One command for the whole plan, fail-fast.

It runs, from the repository root derived from its own location:
  1. the Stage 2 analysis self-test and, for the registered plan, the check of the pilot files (hashes and structure
     only), BEFORE any run, so that a missing or altered input is found at the start and not after the campaign;
  2. the Stage 1 fixtures on this machine (unchanged script; exit code must be 0; log kept as fixtures_output.txt);
  3. every cell of the plan with the registered runner (unchanged), as shards; every worker's exit code must be 0;
  4. a check of every shard (record file, manifest, expected record count);
  5. the registered Stage 2 analysis over all cells (exit code must be 0: integrity and gates passed);
  6. HASHES.txt over the output directory and, only if everything above succeeded, CAMPAIGN_COMPLETE.json.
On the first failure it writes CAMPAIGN_FAILED.txt, writes no completion marker and exits with code 1. A directory
without CAMPAIGN_COMPLETE.json is not a campaign result.

usage
  python -I az_tokres_s2_campaign.py --plan stage2 --out DIR --pilot-dir PILOT --jobs 1 --confirmatory   (PI-authorised run only)
  python -I az_tokres_s2_campaign.py --plan s2test --out DIR --jobs 2 [--skip-fixtures LOG] [--pilot-dir PILOT]
  add --resume to continue an interrupted run in the same DIR (workers refuse records of another identity).
The registered parameters are read from the Stage 2 analysis script's REGISTRY; this file adds none.
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
ANALYSE_S1 = os.path.join(HERE, "az_tokres_analyse.py")
ANALYSE_S2 = os.path.join(HERE, "az_tokres_s2_analyse.py")
GOLDEN = os.path.join(ROOT, "evidence", "az", "token_resonance", "fixtures", "golden.json")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Failed(Exception):
    pass


def main() -> int:
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("az_tokres_s2_analyse", ANALYSE_S2)
    an = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(an)

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", required=True, choices=sorted(an.PLANS))
    ap.add_argument("--out", required=True)
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--pilot-dir", default=None)
    ap.add_argument("--confirmatory", action="store_true")
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--skip-fixtures", default=None, help="test plan only: use this existing fixtures log")
    a = ap.parse_args()

    registered = a.plan == "stage2"
    if registered and not a.confirmatory:
        print("REFUSED: plan stage2 needs --confirmatory (PI-authorised run only)", file=sys.stderr)
        return 2
    if not registered and a.confirmatory:
        print("REFUSED: --confirmatory is reserved for plan stage2", file=sys.stderr)
        return 2
    if registered and not a.pilot_dir:
        print("REFUSED: plan stage2 needs --pilot-dir (the unchanged pilot output directory)", file=sys.stderr)
        return 2
    if a.skip_fixtures and registered:
        print("REFUSED: --skip-fixtures is for the test plan only", file=sys.stderr)
        return 2
    if a.jobs < 1:
        print("REFUSED: --jobs must be at least 1", file=sys.stderr)
        return 2
    out = os.path.abspath(a.out)
    pilot = os.path.abspath(a.pilot_dir) if a.pilot_dir else None
    if os.path.exists(out) and os.listdir(out) and not a.resume:
        print("REFUSED: output directory exists and is not empty; use --resume or another --out", file=sys.stderr)
        return 2
    os.makedirs(os.path.join(out, "logs"), exist_ok=True)
    for stale in ("CAMPAIGN_COMPLETE.json", "CAMPAIGN_FAILED.txt", "HASHES.txt"):
        if os.path.exists(os.path.join(out, stale)):
            os.remove(os.path.join(out, stale))

    py = [sys.executable, "-I"]
    t0 = time.time()
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    steps = []

    def note(msg):
        print(msg, flush=True)
        steps.append(msg)

    def run_to(name, cmd):
        with open(os.path.join(out, name), "w", newline="\n") as f:
            return subprocess.call(cmd, stdout=f, stderr=subprocess.STDOUT)

    try:
        # ---- 1. self-test of the Stage 2 analysis; pilot files (before any run)
        rc = run_to("s2_selftest_output.txt", py + [ANALYSE_S2, "--selftest", "--analysis-s1", ANALYSE_S1])
        if rc != 0:
            raise Failed("Stage 2 analysis self-test exited with code %d (see s2_selftest_output.txt)" % rc)
        note("Stage 2 analysis self-test: exit code 0")
        if registered:
            rc = run_to("pilot_check_output.txt", py + [ANALYSE_S2, "--analysis-s1", ANALYSE_S1, "--check-pilot", pilot])
            if rc != 0:
                raise Failed("pilot files: check exited with code %d (see pilot_check_output.txt)" % rc)
            note("pilot files: hashes and structure as registered")

        # ---- 2. fixtures (Stage 1 script, unchanged)
        flog = os.path.join(out, "fixtures_output.txt")
        if a.skip_fixtures:
            shutil.copyfile(a.skip_fixtures, flog)
            note("fixtures: log copied from %s (test plan)" % os.path.basename(a.skip_fixtures))
        else:
            rc = run_to("fixtures_output.txt", py + [FIXTURES, "--engine", ENGINE, "--orient", ORIENT, "--runner", RUNNER,
                                                     "--analysis", ANALYSE_S1, "--golden", GOLDEN])
            if rc != 0:
                raise Failed("fixtures exited with code %d (see fixtures_output.txt)" % rc)
            note("fixtures: exit code 0")

        # ---- 3-4. shards, cell after cell
        files = {}
        s1 = an.load_s1(ANALYSE_S1)
        for cell in an.PLANS[a.plan]:
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
            arms = s1.arms_for(cfg["N"])
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

        # ---- 5. analysis over all cells (fail-closed inside the analysis script)
        cmd = py + [ANALYSE_S2, "--plan", a.plan, "--dir", out, "--engine", ENGINE, "--orient", ORIENT, "--runner", RUNNER,
                    "--analysis-s1", ANALYSE_S1, "--fixtures-log", flog]
        if pilot:
            cmd += ["--pilot-dir", pilot]
        name = "analysis_%s.txt" % a.plan
        rc = run_to(name, cmd)
        if rc != 0:
            raise Failed("the Stage 2 analysis exited with code %d (2 = integrity, 3 = gate); see %s" % (rc, name))
        note("analysis %s: exit code 0" % a.plan)
    except Failed as ex:
        with open(os.path.join(out, "CAMPAIGN_FAILED.txt"), "w", newline="\n") as f:
            f.write("CAMPAIGN FAILED: %s\n" % ex + "".join("  done before the failure: %s\n" % s for s in steps))
        print("CAMPAIGN FAILED: %s" % ex, file=sys.stderr)
        return 1

    # ---- 6. hashes and completion marker
    listing = []
    for d, _, fs in os.walk(out):
        for name in fs:
            p = os.path.join(d, name)
            listing.append((os.path.relpath(p, out).replace(os.sep, "/"), sha256_file(p)))
    listing.sort()
    with open(os.path.join(out, "HASHES.txt"), "w", newline="\n") as f:
        f.write("".join("%s  %s\n" % (h, rel) for rel, h in listing))
    marker = {"schema": "az_tokres_s2_campaign_v1", "plan": a.plan, "cells": list(an.PLANS[a.plan]), "jobs": a.jobs,
              "confirmatory": bool(a.confirmatory), "resumed": bool(a.resume), "fixtures_skipped": bool(a.skip_fixtures),
              "pilot_supplied": bool(pilot),
              "started_utc": started, "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "seconds": round(time.time() - t0, 1), "python": sys.version.split()[0], "platform": platform.platform(),
              "records": {c: sum(1 for p in files[c] for _ in open(p, "rb")) for c in files},
              "sha256": {"engine": sha256_file(ENGINE), "orient": sha256_file(ORIENT), "runner": sha256_file(RUNNER),
                         "fixtures": sha256_file(FIXTURES), "analysis_s1": sha256_file(ANALYSE_S1), "analysis_s2": sha256_file(ANALYSE_S2),
                         "golden": sha256_file(GOLDEN), "driver": sha256_file(os.path.abspath(__file__)),
                         "HASHES.txt": sha256_file(os.path.join(out, "HASHES.txt"))},
              "steps": steps}
    with open(os.path.join(out, "CAMPAIGN_COMPLETE.json"), "w", newline="\n") as f:
        json.dump(marker, f, sort_keys=True, indent=1)
        f.write("\n")
    print("CAMPAIGN COMPLETE: %s" % json.dumps(marker["records"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
