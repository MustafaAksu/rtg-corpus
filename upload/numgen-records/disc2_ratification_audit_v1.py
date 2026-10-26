#!/usr/bin/env python3
# =============================================================================
# DISC-2 RATIFICATION AUDIT  v1   (A1-A5, frozen before execution)
# =============================================================================
# Governed by NG_C7B_DISC2_PREREG_v1.md. Inert on import.
#
# A1  exhaustive owner recount of ALL 136 admitted witnesses at all four k
#     (544 owner runs) via pinned genesis_mode_b_mc_v18.py. Compares
#     (n_swap, n_P3, preperiod, period) against the enumeration artifact.
#     Because the one-step gateway already certified
#     (next reduced state, dn_swap, dn_P3) for EVERY reduced state at every k,
#     deterministic induction gives identical trajectories globally; A1 is
#     therefore an independent audit of CYCLE DETECTION, CYCLE SLICING, SEED
#     RECONSTRUCTION and ARTIFACT EMISSION, not of the transition rule.
#     Any mismatch => [STOP] ratification.
# A2  exact integer T4 certificate per witness: with base class p:q,
#     C_k = q*n_swap(k) - p*n_P3(k). Require C_1 = 0, C_2 = 0, and C_kc != 0
#     at the qualifying contingency point, per subtype.
# A3  supplementary-family membership/reconstruction for all 136 witnesses.
# A4  the six PASS_BDY_ONLY witnesses, published individually in full.
# A5  DESCRIPTIVE concentration tables. No threshold, no retroactive criterion.
#     Concentration bears on robustness/generalization, NOT on existential
#     label membership: Q^dyn is existential through certified realizations.
# =============================================================================
import sys, os, json, hashlib, importlib.util
from math import gcd
from collections import Counter

N = 24
V18_SHA = "9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e"
OWNER = "genesis_mode_b_mc_v18.py"
REGISTERED_D = {-5, -4, -3, 3, 4, 5}
REGISTERED_DAB = {11, 12, 13}          # N/2 + eps, eps in {-1,0,1}
ESTABLISHED = {(2, 1), (3, 1)}
FAIL = []


def sc(x, n=N):
    y = x % n
    return y - n if y > n // 2 else y


def load_owner(path):
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    if h != V18_SHA:
        raise SystemExit(f"[STOP] owner hash {h} != pinned {V18_SHA}")
    spec = importlib.util.spec_from_file_location("pinned_v18", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def owner_cycle(v18, r, k, cap=200000):
    """Independent recount straight through the owner module."""
    DAB, DAC, dAB, dAC = r
    u = v18.Universe(N=N, k=k, theta={0: 0, 1: (0 - DAB) % N, 2: (0 - DAC) % N},
                     delta={0: 0, 1: (0 - dAB) % N, 2: (0 - dAC) % N})
    seen = {}; hist = []; t = 0
    while t < cap:
        key = ((u.theta[0] - u.theta[1]) % N, (u.theta[0] - u.theta[2]) % N,
               (u.delta[0] - u.delta[1]) % N, (u.delta[0] - u.delta[2]) % N)
        if key in seen:
            pre = seen[key]
            c = hist[pre:t]
            return (sum(a for a, _ in c), sum(b for _, b in c), pre, t - pre)
        seen[key] = t
        s0, p0 = u.single_edge_swaps, u.path_interactions
        v18.step_universe(u, multistar_policy="bound_symmetric")
        hist.append((u.single_edge_swaps - s0, u.path_interactions - p0)); t += 1
    raise SystemExit(f"[STOP] owner recount hit cap for {r} k={k}")


def reduced(a, b):
    if a <= 0 or b <= 0:
        return None
    g = gcd(a, b); return (a // g, b // g)


def main():
    v18 = load_owner(OWNER)
    enum = json.load(open("disc2_enumeration_sup_d345.json"))
    rep = json.load(open("disc2_witness_report.json"))
    E = {(x["seed_id"], x["k"]): x for x in enum}
    W = {s: v for s, v in rep["per_seed"].items() if v["verdict"].startswith("PASS")}
    print(f"admitted witnesses: {len(W)}  ({Counter(v['verdict'] for v in W.values())})")

    # ---------------- A1 exhaustive owner recount --------------------------
    bad1 = []
    for sid in sorted(W):
        r = tuple(int(z) for z in sid.split("_")[1:])
        for k in (0, 1, 2, 3):
            a, b, pre, per = owner_cycle(v18, r, k)
            e = E[(sid, k)]
            if (a, b, pre, per) != (e["n_swap"], e["n_p3"], e["preperiod"], e["cycle_len"]):
                bad1.append((sid, k, (a, b, pre, per),
                             (e["n_swap"], e["n_p3"], e["preperiod"], e["cycle_len"])))
    print(f"[{'PASS' if not bad1 else 'FAIL'}] A1 owner recount of all {len(W)} witnesses "
          f"x 4 k = {4*len(W)} runs: {len(bad1)} mismatches")
    if bad1: FAIL.append("A1"); print("   e.g.", bad1[:3])

    # ---------------- A2 exact integer T4 certificates ----------------------
    bad2 = []; certs = {}
    for sid, v in sorted(W.items()):
        p, q = tuple(v["base_class"])
        C = {k: q * E[(sid, k)]["n_swap"] - p * E[(sid, k)]["n_p3"] for k in (0, 1, 2, 3)}
        qual = {k: E[(sid, k)]["dual_active"] for k in (0, 1, 2, 3)}
        certs[sid] = {"class": (p, q), "C": C, "qualifying": qual, "subtype": v["verdict"]}
        ok = (C[1] == 0 and C[2] == 0 and qual[2])
        if v["verdict"] == "PASS_INT":
            ok &= (qual[3] and C[3] != 0)
        else:                                    # PASS_BDY_ONLY
            ok &= (qual[0] and C[0] != 0)
            ok &= not (qual[3] and C[3] != 0)    # no interior contingency
        if not ok: bad2.append((sid, v["verdict"], C, qual))
    print(f"[{'PASS' if not bad2 else 'FAIL'}] A2 exact T4 certificates "
          f"(C_1 = C_2 = 0, C_kc != 0 by subtype): {len(bad2)} violations")
    if bad2: FAIL.append("A2"); print("   e.g.", bad2[:3])

    # ---------------- A3 membership / reconstruction ------------------------
    bad3 = []
    for sid in sorted(W):
        r = tuple(int(z) for z in sid.split("_")[1:])
        d = sc((-r[2]) % N)
        if sid != "sup_" + "_".join(map(str, r)): bad3.append((sid, "id-reconstruct"))
        if d not in REGISTERED_D:                bad3.append((sid, f"d={d} not registered"))
        if r[0] not in REGISTERED_DAB:           bad3.append((sid, f"D_AB={r[0]} not a k=1 offset"))
        if abs(d) > 5:                           bad3.append((sid, "unregistered extrapolation"))
        for k in (0, 1, 2, 3):
            if (sid, k) not in E: bad3.append((sid, f"missing k={k}"))
    print(f"[{'PASS' if not bad3 else 'FAIL'}] A3 supplementary membership + same-x "
          f"at all four k: {len(bad3)} violations")
    if bad3: FAIL.append("A3"); print("   e.g.", bad3[:5])

    # ---------------- A4 boundary-only block, published in full -------------
    print("\n[A4] PASS_BDY_ONLY witnesses, complete:")
    for sid, v in sorted(W.items()):
        if v["verdict"] != "PASS_BDY_ONLY": continue
        cls = [reduced(E[(sid, k)]["n_swap"], E[(sid, k)]["n_p3"]) for k in (0, 1, 2, 3)]
        cnt = [(E[(sid, k)]["n_swap"], E[(sid, k)]["n_p3"]) for k in (0, 1, 2, 3)]
        print(f"   {sid:20s} base {tuple(v['base_class'])}  classes(k=0..3) {cls}")
        print(f"   {'':20s} counts {cnt}  C {certs[sid]['C']}")

    # ---------------- A5 descriptive concentration --------------------------
    print("\n[A5] concentration (descriptive only; bears on robustness, not membership)")
    print("  by signed d:", dict(sorted(Counter(sc((-int(s.split('_')[3])) % N)
                                                for s in W).items())))
    print("  by D_AB    :", dict(sorted(Counter(int(s.split('_')[1]) for s in W).items())))
    print("  by class   :", dict(sorted(Counter(tuple(v["base_class"]) for v in W.values()).items())))
    print("  by subtype :", dict(Counter(v["verdict"] for v in W.values())))
    print("  class x d  :")
    cx = Counter((tuple(v["base_class"]), sc((-int(s.split('_')[3])) % N)) for s, v in W.items())
    for (c, d), n in sorted(cx.items()):
        print(f"     {c[0]}:{c[1]:<3} d={d:+d}  n={n}")

    json.dump({"certs": {k: {kk: (vv if kk != "class" else list(vv))
                             for kk, vv in v.items()} for k, v in certs.items()}},
              open("disc2_ratification_certs.json", "w"), indent=1, default=str)
    print("-" * 70)
    if FAIL:
        print("[STOP] RATIFICATION BLOCKED:", FAIL); sys.exit(1)
    print("A1-A3 PASS; A4/A5 published. Ratification audit complete.")


if __name__ == "__main__":
    main()
