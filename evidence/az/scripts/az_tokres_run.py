#!/usr/bin/env python3
"""AZ token-resonance runner - [SESSION] NONCANONICAL test instrument (AZ Action 1; preregistration
records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md).

It drives the pinned TDR-G engine WITHOUT changing it: the engine module is loaded from its placed path, its SHA-256 is
checked against the pin, and the only exchange is the documented drop-in of `orient_path` (profile P1). Initial states
are the engine's own native draw (`init_universe`) with, per arm, one declared token replaced. The run loop repeats the
engine's `run_one` loop line for line and adds read-only bookkeeping (token census, law check, birth-anchored window).

Profiles
  P1  engine 4c94d874...a608 + TDRG-DEF-ORIENT as amended in tdrg-v2.12.14 (reference orient_path ca59e9b9...d59c)   primary
  P2  engine 4c94d874...a608 with its built-in orient_path ("v18 path orientation", superseded)                sensitivity

Arms (one base draw b = native (theta0, delta0); slot j and all choices from a second, independent stream)
  BASE   native state
  O1R    delta_j := r1,       r1 in {0, N/2}                       (2x = 0,   order 1)
  O1D    delta_j := r1 + s1,  s1 in {+1, -1}                       (detuned neighbour of r1)
  O2R    delta_j := r2,       r2 in {N/4, 3N/4}        (4 | N)     (2x = N/2, order 2)
  O2D    delta_j := r2 + s2
  Q2R    delta_j := q,        q in {floor(N/4), ceil(N/4), floor(3N/4), ceil(3N/4)}   (N = 2 mod 4: no order-2 token)
  SHAM   delta_j := delta_j + s3                                   (perturbation of the native token)
  BASE_P, O1R_P   BASE and O1R with the four initial node labels permuted (first --n-perm base draws)

usage
  python -I az_tokres_run.py --engine ENGINE.py --orient ORIENT.py --out OUT.jsonl --tag TAG --N 120 --k 8
         [--T 800] [--cap 300] [--profile P1] [--policy bound_symmetric] [--start 0] [--stop 1500] [--n-perm 200]
         [--arms BASE,O1R,...] [--no-tdr26] [--resume] [--confirmatory]
Registered campaign tags (AZ-TOKRES-*) are refused without --confirmatory; that flag is for the PI-authorised run only.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import platform
import random
import sys
import time
from collections import Counter

ENGINE_SHA256 = "4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608"
ORIENT_SHA256 = "ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c"
M0 = 4                      # engine default number of initial nodes (init_universe m0)
TDR26_WINDOW = 200          # birth-anchored window of the TDR-26 rule (tdr26_early_basin_classifier.py --rule-w)
CHECKPOINTS = (100, 200, 300, 400, 500, 600, 700, 800)
SCHEMA = "az_tokres_run_v1"


# ---------------------------------------------------------------- loading and pins
def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_module(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_engine(engine_path: str, orient_path: str, profile: str, allow_unpinned: bool = False):
    """Return (engine module, info). The engine file is never written; P1 rebinds the module attribute orient_path."""
    es, os_ = sha256_file(engine_path), sha256_file(orient_path)
    if not allow_unpinned and (es != ENGINE_SHA256 or os_ != ORIENT_SHA256):
        raise SystemExit(f"pin mismatch: engine {es} orient {os_}")
    sys.dont_write_bytecode = True
    eng = load_module(engine_path, "tdrg_engine_pinned")
    ori = load_module(orient_path, "tdrg_orient_reference")
    native = eng.orient_path
    if profile == "P1":
        eng.orient_path = ori.make_orient(eng)
    elif profile == "P2":
        eng.orient_path = native
    else:
        raise SystemExit(f"unknown profile {profile}")
    return eng, {"engine_sha256": es, "orient_sha256": os_, "profile": profile}


# ---------------------------------------------------------------- arithmetic
def cabs(x: int, N: int) -> int:
    x %= N
    return min(x, N - x)


def res_class(x: int, N: int) -> str:
    """'O1' if 2x = 0, 'O2' if 2x = N/2 (mod N), else 'NR'."""
    y = (2 * x) % N
    return "O1" if y == 0 else "O2" if y == N // 2 else "NR"


def alphabet_class(tokens, N: int) -> str:
    cl = {res_class(x, N) for x in tokens}
    has1, has2 = "O1" in cl, "O2" in cl
    return "O1+O2" if has1 and has2 else "O1" if has1 else "O2" if has2 else "NR"


# ---------------------------------------------------------------- seeds and arms
def derive_int(*parts) -> int:
    """Platform-independent integer in [0, 10**12) from the registered tag and indices."""
    s = "|".join(str(p) for p in parts).encode()
    return int.from_bytes(hashlib.sha256(s).digest()[:8], "big") % 10**12


def base_draw(eng, tag: str, N: int, k: int, b: int):
    """Native initial state of base draw b, exactly as the engine's run_one draws it from its run seed."""
    seed = derive_int(tag, f"N{N}", f"k{k}", "base", b)
    u = eng.init_universe(N=N, k=k, rng=random.Random(seed))
    return seed, [u.theta[i] for i in range(M0)], [u.delta[i] for i in range(M0)]


def arm_choices(tag: str, N: int, k: int, b: int) -> dict:
    """Slot and intervention values of base draw b; a stream independent of the native draw."""
    rng = random.Random(derive_int(tag, f"N{N}", f"k{k}", "arm", b))
    j = rng.randrange(M0)
    r1 = rng.choice([0, N // 2])
    s1 = rng.choice([1, -1])
    if N % 4 == 0:
        r2 = rng.choice([N // 4, 3 * N // 4])
    else:
        r2 = rng.choice([N // 4, N // 4 + 1, (3 * N) // 4, (3 * N) // 4 + 1])
    s2 = rng.choice([1, -1])
    s3 = rng.choice([1, -1])
    perm = list(range(M0))
    rng.shuffle(perm)
    return {"slot": j, "r1": r1, "s1": s1, "r2": r2, "s2": s2, "s3": s3, "perm": perm}


def arms_for(N: int):
    return ("BASE", "O1R", "O1D", "O2R", "O2D", "SHAM") if N % 4 == 0 else ("BASE", "O1R", "O1D", "Q2R", "SHAM")


def arm_state(arm: str, th0, d0, ch: dict, N: int):
    """Initial (theta, delta) lists of an arm."""
    th, d, j = list(th0), list(d0), ch["slot"]
    core = arm[:-2] if arm.endswith("_P") else arm
    if core == "O1R":
        d[j] = ch["r1"]
    elif core == "O1D":
        d[j] = (ch["r1"] + ch["s1"]) % N
    elif core in ("O2R", "Q2R"):
        d[j] = ch["r2"]
    elif core == "O2D":
        d[j] = (ch["r2"] + ch["s2"]) % N
    elif core == "SHAM":
        d[j] = (d[j] + ch["s3"]) % N
    elif core != "BASE":
        raise ValueError(arm)
    if arm.endswith("_P"):                       # node i of the permuted state carries the data of node perm[i]
        th = [th[p] for p in ch["perm"]]
        d = [d[p] for p in ch["perm"]]
    return th, d


# ---------------------------------------------------------------- one run
def run_state(eng, N: int, k: int, theta0, delta0, T: int, cap: int, policy: str, tdr26: bool = True,
              check_law: bool = True, keep_final: bool = False) -> dict:
    """The engine's run_one loop on a given initial state, with read-only bookkeeping."""
    if N % 2 or not (k < N / 6):
        raise ValueError("N must be even and k < N/6")
    u = eng.Universe(N=N, k=k, theta={i: t % N for i, t in enumerate(theta0)},
                     delta={i: d % N for i, d in enumerate(delta0)})
    alphabet = {d % N for d in delta0} | {(-d) % N for d in delta0}
    census = Counter(u.delta.values())
    law_viol = 0
    fb = fe = t100 = None
    m_at = {}
    w_n = w_b = 0
    w_occ = w_oims = 0.0
    hit_cap = False
    for _ in range(T):
        if cap > 0 and len(u.theta) >= cap:
            hit_cap = True
            break
        nxt = u.steps + 1
        want_motif = tdr26 and (fb is None or nxt < fb + TDR26_WINDOW)
        b0 = u.births
        motif = eng.step_universe(u, multistar_policy=policy, collect_motif=want_motif)
        db = u.births - b0
        if fe is None and (u.single_edge_swaps or u.path_interactions or u.births or u.multistar_seen
                           or u.path_ties_seen):
            fe = u.steps
        if fb is None and db:
            fb = u.steps
        if want_motif and fb is not None and motif is not None and fb <= u.steps < fb + TDR26_WINDOW:
            w_n += 1
            w_b += int(motif.get("births_step", db))
            w_occ += float(motif.get("occ_clean_pairs", 0))
            w_oims += float(motif.get("occ_clean_pairs_in_multistar", 0))
        if check_law:
            c2 = Counter(u.delta.values())
            if not set(c2) <= alphabet:
                law_viol += 1
            if any(c2[y] < n for y, n in census.items()):
                law_viol += 1
            if sum(c2.values()) - sum(census.values()) != db:
                law_viol += 1
            census = c2
        m = len(u.theta)
        if t100 is None and m >= 100:
            t100 = u.steps
        if u.steps in CHECKPOINTS:
            m_at[u.steps] = m
        if cap > 0 and m >= cap:
            hit_cap = True
            break
    final = Counter(u.delta.values())
    cls = Counter()
    for y, n in final.items():
        cls[cabs(y, N)] += n
    top_a, top_n = max(cls.items(), key=lambda kv: (kv[1], -kv[0]))
    out = {
        "M": len(u.theta), "births": u.births, "steps": u.steps, "hit_cap": hit_cap, "fb": fb, "fe": fe, "t100": t100,
        "M_at": m_at, "census": sorted(final.items()), "top_class": top_a, "top_share": top_n / len(u.theta),
        "law_viol": law_viol if check_law else None,
        "swaps": u.single_edge_swaps, "paths": u.path_interactions, "path_ties": u.path_ties_seen,
        "ms_seen": u.multistar_seen, "ms_bound": u.multistar_bound, "ambiguous": u.ambiguous_events,
        "tdr26": None,
    }
    if tdr26 and fb is not None:
        out["tdr26"] = {"n": w_n, "births": w_b, "occ": w_occ, "oims": w_oims,
                        "complete": w_n == TDR26_WINDOW,
                        "b_per_step": w_b / w_n if w_n else None,
                        "ms_abs": (w_oims / w_occ) if w_occ > 0 else None}
    if keep_final:
        out["_theta"] = dict(u.theta)
        out["_delta"] = dict(u.delta)
    return out


# ---------------------------------------------------------------- campaign driver
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--engine", required=True)
    ap.add_argument("--orient", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--T", type=int, default=800)
    ap.add_argument("--cap", type=int, default=300)
    ap.add_argument("--profile", default="P1", choices=["P1", "P2"])
    ap.add_argument("--policy", default="bound_symmetric")
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--stop", type=int, required=True)
    ap.add_argument("--n-perm", type=int, default=0, help="base draws b < n-perm also run BASE_P and O1R_P")
    ap.add_argument("--arms", default=None, help="comma list; default: all arms of the cell")
    ap.add_argument("--no-tdr26", action="store_true")
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--confirmatory", action="store_true")
    a = ap.parse_args()

    if a.tag.startswith("AZ-TOKRES-") and not a.confirmatory:
        raise SystemExit("registered campaign tag: refused without --confirmatory (PI-authorised run only)")
    eng, info = load_engine(a.engine, a.orient, a.profile)
    arms = tuple(a.arms.split(",")) if a.arms else arms_for(a.N)
    done = set()
    if os.path.exists(a.out):
        if not a.resume:
            raise SystemExit(f"{a.out} exists; use --resume or another --out")
        with open(a.out) as f:
            for line in f:
                r = json.loads(line)
                if r.get("schema") == SCHEMA:
                    done.add((r["base"], r["arm"]))
    cell = f"N{a.N}k{a.k}"
    t0 = time.time()
    n_new = 0
    with open(a.out, "a", newline="\n") as f:
        for b in range(a.start, a.stop):
            seed, th0, d0 = base_draw(eng, a.tag, a.N, a.k, b)
            ch = arm_choices(a.tag, a.N, a.k, b)
            todo = list(arms) + (["BASE_P", "O1R_P"] if b < a.n_perm else [])
            for arm in todo:
                if (b, arm) in done:
                    continue
                th, d = arm_state(arm, th0, d0, ch, a.N)
                t1 = time.time()
                res = run_state(eng, a.N, a.k, th, d, a.T, a.cap, a.policy, tdr26=not a.no_tdr26)
                rec = {"schema": SCHEMA, "tag": a.tag, "cell": cell, "N": a.N, "k": a.k, "T": a.T, "cap": a.cap,
                       "profile": a.profile, "policy": a.policy, "base": b, "arm": arm, "seed": seed,
                       "slot": ch["slot"], "choices": ch, "th0": th, "d0": d, "d0_base": d0,
                       "alphabet_class": alphabet_class(d, a.N), "slot_class": res_class(d[ch["perm"].index(ch["slot"])]
                                                                                       if arm.endswith("_P") else d[ch["slot"]], a.N),
                       "secs": round(time.time() - t1, 4)}
                rec.update(res)
                f.write(json.dumps(rec, sort_keys=True) + "\n")
                f.flush()
                n_new += 1
    man = {"schema": "az_tokres_manifest_v1", "args": vars(a), "arms": list(arms), "runs_written": n_new,
           "runs_present_before": len(done), "seconds": round(time.time() - t0, 1),
           "runner_sha256": sha256_file(os.path.abspath(__file__)), "python": sys.version.split()[0],
           "platform": platform.platform(), "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), **info}
    with open(a.out + ".manifest.json", "a", newline="\n") as f:
        f.write(json.dumps(man, sort_keys=True) + "\n")
    print(json.dumps({"runs_written": n_new, "seconds": man["seconds"], "out": a.out}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
