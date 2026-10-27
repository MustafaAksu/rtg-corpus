#!/usr/bin/env python3
# =============================================================================
# C7B-DISC-2 WITNESS REPORTER  v2
# =============================================================================
# Governed by NG_C7B_DISC2_PREREG_v1.md
#   (sha256 db87b45565f6c5e59ef4797abde8514d89586c1b56bfe303d29ec6fb33919da9)
#
# THIS FILE IS INERT ON IMPORT. All execution is under __main__.
#
# PURPOSE. The sealed harness disc1_analysis_harness_v1.py decides admission and
# is NOT modified. It does not, however, emit the DISC-2 reporting contract:
# six mutually exclusive per-seed gate verdicts, orthogonal blindness/label
# annotations, and panel-level diagnoses. This reporter supplies exactly that.
#
# IT IS NOT A SECOND ADMISSION ENGINE. It recomputes the verdict layer only for
# reporting, then ABORTS unless its PASS-INT count, PASS-BDY-only count and
# admitted-class multiset agree EXACTLY with the sealed harness output. If the
# two ever disagree, the harness is right and this reporter is wrong.
#
# Frozen reporting layers (NG_C7B_DISC2_PREREG_v1 section 5):
#   (a) per-seed gate verdict, mutually exclusive and exhaustive:
#         NO_BASE_DUAL / STABILITY_UNAVAILABLE / UNSTABLE /
#         STABLE_NO_CONTINGENCY / PASS_INT / PASS_BDY_ONLY
#       PASS_INT takes precedence whenever k=3 supplies contingency, even if
#       k=0 does too. PASS_BDY_ONLY means no interior pass but k=0 supplies one.
#   (b) orthogonal per-seed annotations: blind_k0 / blind_k2 / blind_k3,
#       axis_blind, base class, new-label vs already-established-label,
#       qualifying status at each k.
#   (c) panel-level diagnoses.
#
# Blindness is REPORTED, never a fence. No prevalence threshold is applied:
# one valid witness suffices, per the standing definition of Q^dyn.
#
# v1 -> v2 [COR]. v1's anti-second-engine cross-check protected only the
# ADMISSION calculation, which depends solely on the enumeration artifact.
# Supplying an EMPTY transport artifact therefore passed with exit 0 and all
# blindness counts silently zero -- satisfying the reporter while violating the
# frozen witness-provenance contract. v2 adds validate_inputs(), an integrity
# gate run BEFORE any reporting, certifying that the two frozen artifacts are
# the same complete witness panel. None of its checks is an admission rule.
# =============================================================================

import os, json, hashlib, importlib.util
from math import gcd
from collections import Counter

K_BASE, K_STAB, K_CONT = 1, (2,), (0, 3)
K_SET = {0, 1, 2, 3}
EXPECTED_SEEDS = 10368
EXPECTED_RECORDS = 41472
DOMAIN_ID = "SUP_d345"
ESTABLISHED = {(2, 1), (3, 1)}          # from the ratified DISC-1 campaign
HARNESS_SHA = "57a15421b352f8fbe58d7642d78a6ebb936b78aae90d91b9e39034b738510d9d"


def reduced(a, b):
    if a <= 0 or b <= 0:
        return None
    g = gcd(a, b)
    return (a // g, b // g)


def validate_inputs(enum, trans):
    """Certify that the two frozen artifacts are the same complete witness
    panel. NOT an admission rule: no check here can change any verdict."""
    if len(enum) != EXPECTED_RECORDS:
        raise SystemExit(f"ABORT: enumeration has {len(enum)} rows != {EXPECTED_RECORDS}")
    if len(trans) != EXPECTED_RECORDS:
        raise SystemExit(f"ABORT: transport has {len(trans)} rows != {EXPECTED_RECORDS}")
    E = {(x["seed_id"], x["k"]): x for x in enum}
    T = {(x["seed_id"], x["k"]): x for x in trans}
    if len(E) != EXPECTED_RECORDS or len(T) != EXPECTED_RECORDS:
        raise SystemExit("ABORT: duplicate (seed_id, k) records")
    if set(E) != set(T):
        raise SystemExit("ABORT: enumeration/transport key sets differ")
    kmap = {}
    for sid, k in E:
        kmap.setdefault(sid, set()).add(k)
    if len(kmap) != EXPECTED_SEEDS:
        raise SystemExit(f"ABORT: {len(kmap)} seeds != {EXPECTED_SEEDS}")
    for sid, ks in kmap.items():
        if ks != K_SET:
            raise SystemExit(f"ABORT: seed {sid} has k-set {sorted(ks)} != {sorted(K_SET)}")
    for key, e in E.items():
        t = T[key]; sid, k = key
        if t.get("domain_id") != DOMAIN_ID:
            raise SystemExit(f"ABORT: {sid} k={k} domain_id {t.get('domain_id')} != {DOMAIN_ID}")
        for f in ("n_swap", "n_p3", "dual_active", "preperiod"):
            if e[f] != t.get(f):
                raise SystemExit(f"ABORT: {sid} k={k} field {f} disagrees between artifacts")
        if e["cycle_len"] != t.get("period"):
            raise SystemExit(f"ABORT: {sid} k={k} cycle_len != transport period")
        if e["dual_active"] is not (e["n_swap"] > 0 and e["n_p3"] > 0):
            raise SystemExit(f"ABORT: {sid} k={k} dual_active inconsistent with counts")
        r = t.get("raw_reduced_state")
        if (not isinstance(r, list) or len(r) != 4
                or any(not isinstance(z, int) or not 0 <= z < 24 for z in r)):
            raise SystemExit(f"ABORT: {sid} k={k} malformed raw_reduced_state {r}")
        if sid != "sup_" + "_".join(map(str, r)):
            raise SystemExit(f"ABORT: {sid} does not reconstruct from its raw state {r}")
        b = t.get("blind_vs_base")
        if k == K_BASE:
            if b is not None:
                raise SystemExit(f"ABORT: {sid} k={k} blind_vs_base must be null at base")
        elif type(b) is not bool:
            raise SystemExit(f"ABORT: {sid} k={k} blind_vs_base is {type(b).__name__}, not bool")
    print(f"input integrity OK: {EXPECTED_SEEDS} seeds x {sorted(K_SET)}, "
          f"{EXPECTED_RECORDS} matched records in both artifacts")


def verdict(rows_by_k):
    """Mutually exclusive per-seed gate verdict. Mirrors the sealed harness."""
    base = rows_by_k.get(K_BASE)
    r = reduced(base["n_swap"], base["n_p3"]) if base and base["dual_active"] else None
    if r is None:
        return "NO_BASE_DUAL", None
    s = rows_by_k.get(K_STAB[0])
    if not (s and s["dual_active"]):
        return "STABILITY_UNAVAILABLE", r
    if reduced(s["n_swap"], s["n_p3"]) != r:
        return "UNSTABLE", r
    interior = boundary = False
    for kc in K_CONT:
        c = rows_by_k.get(kc)
        if c and c["dual_active"] and reduced(c["n_swap"], c["n_p3"]) != r:
            if kc == 3:
                interior = True
            else:
                boundary = True
    if interior:
        return "PASS_INT", r
    if boundary:
        return "PASS_BDY_ONLY", r
    return "STABLE_NO_CONTINGENCY", r


def main(enum_path, transport_path, harness_path):
    enum = json.load(open(enum_path))
    trans = json.load(open(transport_path))
    validate_inputs(enum, trans)
    by_seed = {}
    for x in enum:
        by_seed.setdefault(x["seed_id"], {})[x["k"]] = x
    blind = {}
    for t in trans:
        blind.setdefault(t["seed_id"], {})[t["k"]] = t.get("blind_vs_base")

    # ---- layer (a) + (b) -------------------------------------------------
    per_seed = {}
    for sid, rows in by_seed.items():
        v, r = verdict(rows)
        b = blind.get(sid, {})
        per_seed[sid] = {
            "verdict": v,
            "base_class": r,
            "blind_k0": b.get(0), "blind_k2": b.get(2), "blind_k3": b.get(3),
            "axis_blind": bool(b.get(0)) and bool(b.get(2)) and bool(b.get(3)),
            "qualifying": {k: bool(rows.get(k, {}).get("dual_active")) for k in (0, 1, 2, 3)},
            "label_status": (None if v not in ("PASS_INT", "PASS_BDY_ONLY")
                             else ("already-established" if r in ESTABLISHED else "new-label")),
        }

    vc = Counter(v["verdict"] for v in per_seed.values())
    passes = {s: v for s, v in per_seed.items() if v["verdict"].startswith("PASS")}
    admitted = Counter(v["base_class"] for v in passes.values())

    # ---- CROSS-CHECK against the sealed harness --------------------------
    h = hashlib.sha256(open(harness_path, "rb").read()).hexdigest()
    if h != HARNESS_SHA:
        raise SystemExit(f"ABORT: harness hash {h} != sealed {HARNESS_SHA}")
    spec = importlib.util.spec_from_file_location("sealed_harness", harness_path)
    H = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(H)
    hres = H.analyse(enum)
    hi = hres["disc1d"]["n_pass_interior_k3"]
    hb = hres["disc1d"]["n_pass_boundary_only_k0"]
    hm = dict(hres["disc1d"]["admitted_class_multiset"])
    mine_i = vc["PASS_INT"]; mine_b = vc["PASS_BDY_ONLY"]
    mine_m = {str(k): n for k, n in admitted.items()}
    if (mine_i, mine_b) != (hi, hb) or mine_m != hm:
        raise SystemExit(
            "ABORT: reporter disagrees with the sealed harness. The harness is "
            f"authoritative.\n  harness  INT={hi} BDY={hb} classes={hm}\n"
            f"  reporter INT={mine_i} BDY={mine_b} classes={mine_m}")
    print(f"cross-check OK against sealed harness ({h[:12]}...): "
          f"PASS_INT={hi}, PASS_BDY_ONLY={hb}, classes={hm}")

    # ---- layer (c) panel diagnoses ---------------------------------------
    any_stab = any(v["verdict"] in ("STABLE_NO_CONTINGENCY", "PASS_INT", "PASS_BDY_ONLY")
                   for v in per_seed.values())
    any_cont = any(
        rows.get(kc) and rows[kc]["dual_active"] and by_seed[s].get(K_BASE)
        and by_seed[s][K_BASE]["dual_active"]
        and reduced(rows[kc]["n_swap"], rows[kc]["n_p3"])
            != reduced(by_seed[s][K_BASE]["n_swap"], by_seed[s][K_BASE]["n_p3"])
        for s, rows in by_seed.items() for kc in K_CONT)
    new_labels = {v["base_class"] for v in passes.values()} - ESTABLISHED
    panel = {
        "stability_somewhere_contingency_nowhere": any_stab and not any_cont,
        "contingency_somewhere_stability_nowhere": any_cont and not any_stab,
        "both_present_never_same_realization": bool(any_stab and any_cont and not passes),
        "new_label_breadth": sorted(map(str, new_labels)) if new_labels else False,
        "no_new_label_breadth": not new_labels,
    }
    all_labels = ESTABLISHED | set(admitted)
    out = {"per_seed_verdict_counts": dict(vc),
           "Qdyn_established_after_DISC2": sorted(map(str, all_labels)),
           "admitted_class_multiset": mine_m,
           "panel_diagnoses": panel,
           "blindness": {
               "axis_blind": sum(1 for v in per_seed.values() if v["axis_blind"]),
               "blind_k2": sum(1 for v in per_seed.values() if v["blind_k2"]),
               "blind_k3": sum(1 for v in per_seed.values() if v["blind_k3"]),
               "blind_k0": sum(1 for v in per_seed.values() if v["blind_k0"])},
           "label_projection_note":
               "Q^dyn_new = pi_r(W_existing U W_DISC2). No prevalence threshold; "
               "one valid witness suffices. Witnesses only for 2 and 3 constitute a "
               "successful dynamic campaign with no new label breadth, not a failure.",
           "per_seed": per_seed}
    json.dump(out, open("disc2_witness_report.json", "w"), indent=1, default=str)
    print(json.dumps({k: out[k] for k in
                      ("per_seed_verdict_counts", "admitted_class_multiset",
                       "panel_diagnoses", "blindness")}, indent=1, default=str))
    print(f"\nwritten: disc2_witness_report.json  sha256 "
          f"{hashlib.sha256(open('disc2_witness_report.json','rb').read()).hexdigest()}")


if __name__ == "__main__":
    import sys
    a = sys.argv[1:]
    main(a[0] if a else "disc2_enumeration_sup_d345.json",
         a[1] if len(a) > 1 else "disc2_transport_sup_d345.json",
         a[2] if len(a) > 2 else "disc1_analysis_harness_v1.py")
