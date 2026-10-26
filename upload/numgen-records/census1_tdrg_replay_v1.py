#!/usr/bin/env python3
# =============================================================================
# CENSUS-1 U-TDRG REPLAY  v1  — evidence for fields F3, F4, F5 only
# =============================================================================
# Governed by NG_C7C_M2_CENSUS_PROTOCOL_v1.md (f2a4a9a4…5795), rule E-rederive
# (frozen replay contract, C-1):
#   1. Frozen input tuple: seed from the frozen universe; k = 1 (K_BASE); code =
#      the record's own frozen campaign enumerator; owner v18 for lockstep.
#      Every input is SHA-256 verified before use; any mismatch aborts.
#   2. Preregistered extraction only: prefix order (tick index) and the event
#      sequence over preperiod + one cycle, from which the single-stream count
#      functions N_SWAP(t), N_P3(t) follow for every t. Nothing else — no ratio,
#      label, class, diagnostic or selection metric is computed.
#   3. Replay consistency: the record's own enumerator cycle function must
#      reproduce the sealed k=1 fields (n_swap, n_p3, cycle_len, preperiod,
#      dual_active) EXACTLY; the stepwise trajectory must agree with it; every
#      step must agree with owner v18 step_universe on the ABSOLUTE state
#      (theta, delta), with no birth. Any mismatch -> R3-REPLAY. No other code,
#      parameter or convention is ever tried.
#   4. Hashed evidence: outputs and an invocation/config manifest are hashed.
# The script evaluates no interface equivalence, no Pi, no N1/N2, no WD-DOM.
# =============================================================================
import argparse, hashlib, importlib.util, json, os, platform, sys

PINS = {
    "owner":   "9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e",
    "d1_code": "41a86011c6ad7ccb",   # prefix pins as recorded in the frozen result docs
    "d1_data": "dab769a075400d55fbadfb0aa3324286244a614a6e802f465e4e520a53efc83d",
    "d2_code": "b7cee9220f73252a",
    "d2_data": "6840f822e967",
    "universe": "80b0c3b17349e8746b939c241007b7a0a67c2e69160badc4ebbfa3f1973513e9",
}
N, K_BASE = 24, 1
SYM = {"swap": "S", "p3": "P", "tie": "T", "k3": "K", None: ".",
       "S": "S", "P": "P", "T": "T", "K": "K", ".": "."}

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def verify(tag, path):
    got = sha(path)
    if not got.startswith(PINS[tag]):
        sys.exit(f"ABORT: {tag} {path} sha256 {got[:16]} does not match pin {PINS[tag][:16]}")
    return got

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m)
    return m

def replay(rec, E, sealed, V18):
    r = tuple(int(x) for x in rec["seed_id"].split("_")[1:])
    out = {"record_id": rec["record_id"], "campaign": rec["campaign"], "seed_id": rec["seed_id"], "k": K_BASE}
    # (3a) the record's own frozen cycle function vs the sealed record
    if rec["campaign"] == "C7B-DISC-1":
        a, b, per, pre = E.cycle_counts(r, K_BASE)
    else:
        a, b, pre, per = E.cycle_record(r, K_BASE)
    fn = {"n_swap": a, "n_p3": b, "cycle_len": per, "preperiod": pre, "dual_active": (a > 0 and b > 0)}
    out["sealed_match"] = {f: fn[f] == sealed[f] for f in fn}
    # (2) stepwise trajectory with the same frozen step, extracting only prefix order + events
    s = E.lift(r); seen = {}; ev = []; t = 0; lock_ok = True; lock_first_fail = None
    while True:
        c = E.canon(s)
        if c in seen: break
        seen[c] = t
        th, dl = s
        u = V18.Universe(N=N, k=K_BASE, theta={i: th[i] for i in range(3)}, delta={i: dl[i] for i in range(3)})
        V18.step_universe(u, multistar_policy="bound_symmetric")
        s, e = E.step(s, K_BASE)
        # (3c) lockstep on the ABSOLUTE state, no birth
        if (len(u.theta) != 3 or u.births or
                tuple(u.theta[i] for i in range(3)) != s[0] or tuple(u.delta[i] for i in range(3)) != s[1]):
            if lock_ok: lock_first_fail = t
            lock_ok = False
        ev.append(SYM[e]); t += 1
    pre2 = seen[E.canon(s)]; cyc = ev[pre2:t]
    step_fields = {"n_swap": cyc.count("S"), "n_p3": cyc.count("P"), "cycle_len": t - pre2, "preperiod": pre2}
    out["stepwise_matches_fn"] = all(step_fields[f] == fn[f] for f in step_fields)
    out["v18_lockstep_ok"] = lock_ok
    if not lock_ok: out["v18_lockstep_first_fail_tick"] = lock_first_fail
    out["preperiod"], out["cycle_len"] = pre2, t - pre2
    out["events_preperiod_plus_one_cycle"] = "".join(ev)          # the F3/F4 extraction
    ok = all(out["sealed_match"].values()) and out["stepwise_matches_fn"] and lock_ok
    out["replay_contract"] = "PASS" if ok else "FAIL"
    if not ok: out["reason"] = "R3-REPLAY"
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--universe", required=True); ap.add_argument("--owner", required=True)
    ap.add_argument("--d1-code", required=True); ap.add_argument("--d1-data", required=True)
    ap.add_argument("--d2-code", required=True); ap.add_argument("--d2-data", required=True)
    ap.add_argument("--out", default="census1_tdrg_replay")
    ap.add_argument("--limit", type=int, default=None, help="smoke test only: first N records per campaign")
    a = ap.parse_args()
    hashes = {k: verify(k, p) for k, p in (("universe", a.universe), ("owner", a.owner), ("d1_code", a.d1_code),
                                            ("d1_data", a.d1_data), ("d2_code", a.d2_code), ("d2_data", a.d2_data))}
    V18 = load("v18owner", a.owner)
    E1 = load("d1enum", a.d1_code); E2 = load("d2enum", a.d2_code)
    S1 = {(x["seed_id"], x["k"]): x for x in json.load(open(a.d1_data))}
    S2 = {(x["seed_id"], x["k"]): x for x in json.load(open(a.d2_data))}
    U = json.load(open(a.universe))["records"]
    if a.limit:
        U = [r for r in U if r["campaign"] == "C7B-DISC-1"][:a.limit] + [r for r in U if r["campaign"] == "C7B-DISC-2"][:a.limit]
    os.makedirs(a.out, exist_ok=True)
    recs_path = os.path.join(a.out, "census1_tdrg_replay_records.jsonl")
    n_pass = 0
    with open(recs_path, "w", encoding="utf-8", newline="\n") as f:
        for rec in U:
            E, S = (E1, S1) if rec["campaign"] == "C7B-DISC-1" else (E2, S2)
            sealed = S.get((rec["seed_id"], K_BASE))
            if sealed is None:
                o = {"record_id": rec["record_id"], "replay_contract": "FAIL", "reason": "R0-MISSING"}
            else:
                o = replay(rec, E, sealed, V18)
            n_pass += o["replay_contract"] == "PASS"
            f.write(json.dumps(o, sort_keys=True) + "\n")
    man = {"script": os.path.basename(__file__), "script_sha256": sha(__file__), "input_sha256": hashes,
           "argv": sys.argv[1:], "python": sys.version, "platform": platform.platform(),
           "records": len(U), "replay_contract_pass": n_pass, "records_file": os.path.basename(recs_path),
           "records_sha256": sha(recs_path), "smoke_test_limit": a.limit}
    mp = os.path.join(a.out, "census1_tdrg_replay_manifest.json")
    json.dump(man, open(mp, "w", encoding="utf-8", newline="\n"), indent=1)
    print(f"records {len(U)} | replay-contract PASS {n_pass} | records sha256 {man['records_sha256'][:16]} | manifest {sha(mp)[:16]}")

if __name__ == "__main__":
    main()
