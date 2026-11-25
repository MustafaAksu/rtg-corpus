#!/usr/bin/env python3
"""NUMGEN v1.22 S1 — witness-level P2 re-annotation of the Census-1 TDR-G witness universe (DISC-1 22 + DISC-2 136)
under TDRG-DEF-ORIENT (tdrg-v2.13 §6.3), with the frozen v18 engine. [NUM]; frozen verdict files are read, never written.

Single intervention: the pinned owner engine `genesis_mode_b_mc_v18.py` (9d787b43…675e) is loaded twice from the same
bytes. In the second copy `orient_path` is replaced by the TDR-G reference `make_orient` (`tdrg_orient_v2_12_14.py`,
ca59e9b9…d77c). Nothing else changes: N=24, three nodes, `step_universe(..., multistar_policy="bound_symmetric")` (the
policy of the Census-1 lockstep), event semantics of the engine, and the frozen enumerators' `lift`/`canon` as cycle key.

Gates (acceptance criteria of the co-owner GO, 24 Nov 2026):
  G1 IDENTITY     every input matches its SHA-256 pin
  G2 POSITIVE     unmodified v18 reproduces the frozen record of every witness: DISC-1 transport tuple (k=0..3) and
                  PASS_INT class; DISC-2 verdict and base class; plus tick-by-tick lockstep with the record's own frozen
                  enumerator `step` at every k
  G3 SINGLE       the two engine copies differ in `orient_path` only (bytecode of every other function identical)
  G4 DISC-2       136 witnesses, new policy vs the held audit's `inert` column, witness by witness (verdict and class)
  G5 DISC-1       22 witnesses evaluated directly; exposure counted, not assumed (the reported 0/22 is the expected value)
  G6 NEGATIVE     (a) the antipodal fixture: v18 and the new policy give different successors, and only the new policy is
                  relabelling-equivariant on it; (b) a deliberately wrong orient (always reversed) fails G2
  G7 SUMMARY      counts reported against the expected table (difference reported, not forced)

usage: numgen_v1_22_s1_p2_reannotation.py --root REPO --out DIR
"""
import argparse, hashlib, importlib.util, json, os, platform, sys, types
from collections import Counter
from math import gcd

PINS = {
    "engine":   ("upload/tdrg-records/genesis_mode_b_mc_v18.py", "9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e"),
    "orient":   ("evidence/tdrg/scripts/tdrg_orient_v2_12_14.py", "ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c"),
    "universe": ("upload/numgen-records/NG_C7C_M2_CENSUS1_UTDRG_UNIVERSE_v1.json", "80b0c3b17349e8746b939c241007b7a0a67c2e69160badc4ebbfa3f1973513e9"),
    "d1_code":  ("upload/numgen-records/bind3_enumerate_k0123_v1.py", "41a86011c6ad7ccb378097aa62106bf2dfbf5acf9a4b56792a690379a6eae929"),
    "d1_result":("upload/numgen-records/disc1_result.json", "92593b8cfdc7b9d37af49af32952652b7d4555dec4e13c4a1571c81388cb6f70"),
    "d2_code":  ("upload/numgen-records/disc2_supplementary_enumerator_v3_1.py", "b7cee9220f73252af3b7322b50a67ecff4227424b6b1309f241d5e24babb35df"),
    "d2_report":("upload/numgen-records/disc2_witness_report.json", "ccc8457086b01193bdec598a7db44508be8486659ae07feb4df15a66401faa7d"),
    "audit":    ("upload/numgen-records/disc2_p2_antipodal_exposure_audit_v1.py", "89a1466ff8922fb17ed21b0fbff9f719b752abb5ad3fe9cf76545259ebe5fe1c"),
}
N, POLICY, KS = 24, "bound_symmetric", (0, 1, 2, 3)
SYM = {"swap": "S", "p3": "P", "tie": "T", "k3": "K", None: ".", "S": "S", "P": "P", "T": "T", "K": "K", ".": "."}  # as census1_tdrg_replay_v1.py
EXPECTED = {"witnesses_DISC2": 136, "exposed_DISC2": 40, "changed_DISC2": 20, "pass_kept_class_changed": 8,
            "pass_lost_base_dual_kept": 6, "base_dual_lost": 6, "labels_kept": 10, "exposed_DISC1_reported": 0}

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m); return m

def ratio(a, b):
    return None if (a == 0 or b == 0) else (a // gcd(a, b), b // gcd(a, b))

def verdict(out):  # the DISC verdict rule, as in the frozen harness / held audit
    r1 = out[1]
    if r1 is None: return "NO_BASE_DUAL"
    if out[2] is None: return "STABILITY_UNAVAILABLE"
    if out[2] != r1: return "UNSTABLE"
    if out[3] is not None and out[3] != r1: return "PASS_INT"
    if out[0] is not None and out[0] != r1: return "PASS_BDY_ONLY"
    return "STABLE_NO_CONTINGENCY"

class Run:
    """Drive one engine copy from a lifted seed until the frozen canonical key repeats."""
    def __init__(self, eng, enum, lock=False):
        self.eng, self.enum, self.lock = eng, enum, lock
        real = eng.orient_path
        def watched(path, theta, delta, n, u):      # exposure probe: reads, never alters the decision
            if len(path) == 3:
                s = sum(eng.signed_defect_error(theta[path[i]], theta[path[i + 1]], n) for i in range(2))
                e = eng.signed_centered(delta[path[-1]] - delta[path[0]], n)
                if s == 0 and 2 * e % n == 0 and e != 0: u._antipodal_hits = getattr(u, "_antipodal_hits", 0) + 1
            return real(path, theta, delta, n, u)
        self.watched = watched
    def cycle(self, r, k):
        eng, enum = self.eng, self.enum
        th, dl = enum.lift(r)
        u = eng.Universe(N=N, k=k, theta={i: th[i] for i in range(3)}, delta={i: dl[i] for i in range(3)})
        saved = eng.orient_path; eng.orient_path = self.watched
        try:
            seen, ev, t, lock_ok, s = {}, [], 0, True, (th, dl)
            while t < 200000:
                c = enum.canon(s)
                if c in seen: break
                seen[c] = t
                before = (u.single_edge_swaps, u.path_interactions, u.path_ties_bound)
                eng.step_universe(u, multistar_policy=POLICY)
                after = (u.single_edge_swaps, u.path_interactions, u.path_ties_bound)
                e = "S" if after[0] > before[0] else "P" if after[1] > before[1] else "T" if after[2] > before[2] else "."
                s_new = (tuple(u.theta[i] for i in range(3)), tuple(u.delta[i] for i in range(3)))
                if self.lock:
                    s_ref, e_ref = enum.step(s, k); e_ref = SYM[e_ref]
                    if s_ref != s_new or u.births or len(u.theta) != 3 or (e_ref in "SP" or e in "SP") and e_ref != e:
                        lock_ok = False
                s = s_new; ev.append(e); t += 1
            pre = seen[enum.canon(s)]; cyc = ev[pre:t]
            return ratio(cyc.count("S"), cyc.count("P")), getattr(u, "_antipodal_hits", 0), lock_ok
        finally:
            eng.orient_path = saved

def evaluate(run, r):
    outs, hits, lock = {}, 0, True
    for k in KS:
        o, h, l = run.cycle(r, k); outs[k] = o; hits += h; lock &= l
    return outs, hits, lock

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default="."); ap.add_argument("--out", required=True)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    P = {k: os.path.join(a.root, p) for k, (p, _) in PINS.items()}
    gates, log = {}, []
    def gate(k, ok, msg=""):
        gates[k] = bool(ok); line = f"[{'PASS' if ok else 'FAIL'}] {k} {msg}"; log.append(line); print(line)

    got = {k: sha(P[k]) for k in PINS}
    gate("G1 IDENTITY", all(got[k] == PINS[k][1] for k in PINS), f"{len(PINS)} inputs")
    if not gates["G1 IDENTITY"]:
        for k in PINS: print(k, got[k]); sys.exit(1)

    v18 = load("eng_v18", P["engine"]); new = load("eng_orient", P["engine"])
    ref = load("tdrg_orient_ref", P["orient"]); new.orient_path = ref.make_orient(new)
    E1, E2 = load("enum_d1", P["d1_code"]), load("enum_d2", P["d2_code"])
    U = json.load(open(P["universe"]))["records"]
    D1 = json.load(open(P["d1_result"]))["transport_tuples"]
    D2 = json.load(open(P["d2_report"]))["per_seed"]

    # G3: every module-level function except orient_path has identical bytecode in the two copies
    def fn_codes(m):
        return {n: f.__code__.co_code for n, f in vars(m).items() if isinstance(f, types.FunctionType) and f.__module__ == m.__name__}
    c18, cnew = fn_codes(v18), fn_codes(new)
    diff = sorted(n for n in set(c18) | set(cnew) if n != "orient_path" and c18.get(n) != cnew.get(n))
    gate("G3 SINGLE", new.orient_path is not v18.orient_path and new.orient_path.__module__ == "tdrg_orient_ref" and diff == [],
         f"functions differing other than orient_path: {diff}")

    recs, pos_fail = [], []
    for rec in U:
        camp, sid = rec["campaign"], rec["seed_id"]; r = tuple(int(x) for x in sid.split("_")[1:])
        enum = E1 if camp == "C7B-DISC-1" else E2
        o18, h18, lock = evaluate(Run(v18, enum, lock=True), r)
        onew, hnew, _ = evaluate(Run(new, enum), r)
        v_18, v_new = verdict(o18), verdict(onew)
        if camp == "C7B-DISC-1":
            fr = D1[sid]; frozen_t = [tuple(x) if x else None for x in fr]
            ok = lock and [o18[k] for k in KS] == frozen_t and v_18 == "PASS_INT"
            frozen = {"transport_tuple": fr, "verdict": "PASS_INT (DISC-1D interior k3)", "class": list(o18[1]) if o18[1] else None}
        else:
            fr = D2[sid]; bc = tuple(fr["base_class"]) if fr["base_class"] else None
            ok = lock and v_18 == fr["verdict"] and o18[1] == bc
            frozen = {"verdict": fr["verdict"], "base_class": fr["base_class"]}
        if not ok: pos_fail.append(sid)
        recs.append({"record_id": rec["record_id"], "campaign": camp, "seed_id": sid, "frozen": frozen,
                     "v18": {"tuple": [list(o18[k]) if o18[k] else None for k in KS], "verdict": v_18,
                             "class": list(o18[1]) if o18[1] else None, "antipodal_hits": h18},
                     "tdrg_def_orient": {"tuple": [list(onew[k]) if onew[k] else None for k in KS], "verdict": v_new,
                                         "class": list(onew[1]) if onew[1] else None, "antipodal_hits": hnew},
                     "exposed": h18 > 0, "changed": (v_new, onew[1]) != (v_18, o18[1]), "positive_control": ok})
    gate("G2 POSITIVE", not pos_fail, f"{len(U) - len(pos_fail)}/{len(U)} witnesses reproduce the frozen record with v18 "
         f"(DISC-1 tuple k=0..3 + PASS_INT; DISC-2 verdict + base class; lockstep with own enumerator){'; fail ' + str(pos_fail[:5]) if pos_fail else ''}")

    # G4: DISC-2 vs the held audit's inert column
    g = {"__name__": "audit"}; argv = sys.argv; sys.argv = ["audit", P["d2_report"]]
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        try: exec(compile(open(P["audit"]).read(), P["audit"], "exec"), g)
        except SystemExit: pass
    sys.argv = argv
    mism = []
    for x in recs:
        if x["campaign"] != "C7B-DISC-2": continue
        r = tuple(int(z) for z in x["seed_id"].split("_")[1:])
        av, ac, at = g["verdict"](g["ine"], r)
        _, _, a18 = g["verdict"](g["v18"], r)
        x["audit_inert"] = {"verdict": av, "class": list(ac) if ac else None, "audit_exposed": a18}
        if (av, list(ac) if ac else None) != (x["tdrg_def_orient"]["verdict"], x["tdrg_def_orient"]["class"]) or a18 != x["exposed"]:
            mism.append(x["seed_id"])
    d2 = [x for x in recs if x["campaign"] == "C7B-DISC-2"]
    gate("G4 DISC-2", len(d2) == 136 and not mism, f"{len(d2) - len(mism)}/{len(d2)} witnesses: verdict, class and exposure equal to "
         f"the held audit's inert column{'; mismatch ' + str(mism[:5]) if mism else ''}")

    d1 = [x for x in recs if x["campaign"] == "C7B-DISC-1"]
    e1, c1 = sum(x["exposed"] for x in d1), sum(x["changed"] for x in d1)
    gate("G5 DISC-1", len(d1) == 22, f"{len(d1)} witnesses evaluated directly: exposed {e1}/22 (reported value 0/22), "
         f"verdict/class changed {c1}/22")

    # G6a: antipodal fixture (TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE): theta_pre=(0,11,12), delta=(0,1,12), k=1
    def one(eng, th, dl):
        u = eng.Universe(N=N, k=1, theta=dict(enumerate(th)), delta=dict(enumerate(dl)))
        eng.step_universe(u, multistar_policy=POLICY); return tuple(u.delta[i] for i in range(3))
    perm = (2, 1, 0)                                  # exchange the endpoint labels 0 <-> 2
    th, dl = (0, 11, 12), (0, 1, 12)
    thp, dlp = tuple(th[perm[i]] for i in range(3)), tuple(dl[perm[i]] for i in range(3))
    res = {}
    for name, eng in (("v18", v18), ("tdrg_def_orient", new)):
        d0, dp = one(eng, th, dl), one(eng, thp, dlp)
        res[name] = {"successor_delta": d0, "relabelled_run": dp,
                     "equivariant": dp == tuple(d0[perm[i]] for i in range(3))}
    fixture_ok = res["v18"]["successor_delta"] != res["tdrg_def_orient"]["successor_delta"] \
        and not res["v18"]["equivariant"] and res["tdrg_def_orient"]["equivariant"]
    # G6b: a deliberately wrong orient (always reversed) must break the positive control on some witness
    bad = load("eng_bad", P["engine"]); bad.orient_path = lambda path, th_, dl_, n, u: (path if len(path) == 2 else list(reversed(path)))
    broken = 0
    for rec in U:
        r = tuple(int(x) for x in rec["seed_id"].split("_")[1:]); enum = E1 if rec["campaign"] == "C7B-DISC-1" else E2
        ob, _, _ = evaluate(Run(bad, enum), r)
        x = next(y for y in recs if y["seed_id"] == rec["seed_id"])
        broken += [list(ob[k]) if ob[k] else None for k in KS] != x["v18"]["tuple"]
    gate("G6 NEGATIVE", fixture_ok and broken > 0, f"fixture {json.dumps(res)}; always-reversed orient breaks the v18 "
         f"reproduction on {broken}/{len(U)} witnesses")

    # G7: summary
    ch = [x for x in d2 if x["changed"]]
    tr = Counter((x["v18"]["verdict"], str(tuple(x["v18"]["class"]) if x["v18"]["class"] else None),
                  x["tdrg_def_orient"]["verdict"], str(tuple(x["tdrg_def_orient"]["class"]) if x["tdrg_def_orient"]["class"] else None)) for x in ch)
    isp = lambda v: v.startswith("PASS")
    summ = {"witnesses_DISC2": len(d2), "exposed_DISC2": sum(x["exposed"] for x in d2), "changed_DISC2": len(ch),
            "pass_kept_class_changed": sum(isp(x["tdrg_def_orient"]["verdict"]) for x in ch),
            "pass_lost_base_dual_kept": sum(not isp(x["tdrg_def_orient"]["verdict"]) and x["tdrg_def_orient"]["class"] is not None for x in ch),
            "base_dual_lost": sum(x["tdrg_def_orient"]["class"] is None for x in ch),
            "labels_kept": len({tuple(x["v18"]["class"]) for x in d2} & {tuple(x["tdrg_def_orient"]["class"]) for x in d2 if isp(x["tdrg_def_orient"]["verdict"])}),
            "labels_v18": len({tuple(x["v18"]["class"]) for x in d2}),
            "labels_new_pass": len({tuple(x["tdrg_def_orient"]["class"]) for x in d2 if isp(x["tdrg_def_orient"]["verdict"])}),
            "exposed_DISC1_reported": e1, "changed_DISC1": c1}
    diffs = {k: (summ[k], v) for k, v in EXPECTED.items() if summ[k] != v}
    gate("G7 SUMMARY", True, f"{json.dumps(summ)}; differences from the expected table: {diffs or 'none'}")
    for k, v in sorted(tr.items()): log.append(f"   transition {k[0]} {k[1]} -> {k[2]} {k[3]}: {v}"); print(log[-1])

    rp = os.path.join(a.out, "numgen_v1_22_s1_witness_annotation.jsonl")
    with open(rp, "w", encoding="utf-8", newline="\n") as f:
        for x in recs: f.write(json.dumps(x, sort_keys=True) + "\n")
    man = {"script": os.path.basename(__file__), "script_sha256": sha(__file__), "inputs": {k: {"path": PINS[k][0], "sha256": got[k]} for k in PINS},
           "engine_policy": POLICY, "N": N, "k": list(KS), "python": sys.version.split()[0], "platform": platform.platform(),
           "gates": gates, "summary": summ, "expected": EXPECTED, "differences": {k: list(v) for k, v in diffs.items()},
           "annotation_file": os.path.basename(rp), "annotation_sha256": sha(rp)}
    json.dump(man, open(os.path.join(a.out, "numgen_v1_22_s1_manifest.json"), "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)
    ok = all(gates.values()); print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
