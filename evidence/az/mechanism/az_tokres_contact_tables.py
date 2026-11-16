#!/usr/bin/env python3
"""AZ token resonance, mechanism study - exploratory first-contact tables on existing records.
[SESSION] NONCANONICAL. Implements the table contract of records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md §5
(review of PR #281 r2, readback 5921285881) and nothing else. Exploratory: the outcomes are known.

    python3 -I az_tokres_contact_tables.py --selftest
    python3 -I az_tokres_contact_tables.py --manifest M.json --dir DIR --plan test          (test records, tag SMOKE)
    python3 -I az_tokres_contact_tables.py --manifest M.json --dir DIR --plan registered    (refused until frozen)

FREEZE GATE. With --plan registered the script refuses to open any record unless the manifest's field
frozen_script_sha256 equals this file's SHA-256 and every listed input hash matches. The manifest is
frozen only after review (a commit that sets the field); until then no table on registered records exists.

What it computes, per record, without stepping the engine (only from th0, d0 and the slot):
  tau_contact    first processed tick whose post-advance, pre-interaction defect graph has an edge, by the closed
                 form of design §4 (infinity if none in 1..N, hence never);
  E_contact      the whole first-contact graph, classified with the pinned engine's own classifier;
  slot           degree and component type of the replaced node in E_contact; period P(d_s) = N/gcd(N, d_s) and the
                 three relative periods N/gcd(N, d_s - d_j);
  tau_common, tau_slot   the same minimum over the three pairs without / with the slot (design §4.2).
and reads the runner clocks fe, fb, t100 and the endpoint Y = 1{M >= 100 at tick 800} (cap before 800: positive).
Tables T1-T4 and the four prelisted joint tables J1-J4 are printed; nothing else. No test, no p-value, no verdict.
"""
from __future__ import annotations

import argparse, glob, hashlib, importlib.util, json, math, os, random, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
S1_LIB = os.path.join(ROOT, "evidence", "az", "scripts", "az_tokres_analyse.py")
RUNNER = os.path.join(ROOT, "evidence", "az", "scripts", "az_tokres_run.py")
ENGINE = os.path.join(ROOT, "upload", "tdrg-records", "genesis_mode_b_mc.py")
ORIENT = os.path.join(ROOT, "evidence", "tdrg", "scripts", "tdrg_orient_v2_12_14.py")
S1_LIB_SHA256 = "490b3d4f06ef52d6d39b217d0821bd8361d0a8ed37941f32f9c154113c91dc80"
INF = float("inf")
Y_THRESHOLD, Y_TICK = 100, 800
PAIRS = (("O1R", "O1D", "order 1 (2x = 0)"), ("O2R", "O2D", "order 2 (2x = N/2)"))


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def load(path, name):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ------------------------------------------------------------------ first-contact instrument (design §4)
def in_band(x, N, k):
    y = x % N
    y = y - N if y > N // 2 else y
    return abs(y) <= k


def pair_first(a, b, N, k):
    b %= N
    if b == 0:
        return 1 if in_band(a, N, k) else INF
    g = math.gcd(N, b)
    L = N // g
    inv = pow((b // g) % L, -1, L) if L > 1 else 0
    best = INF
    for e in range(-k, k + 1):
        r = (e - a) % N
        if r % g:
            continue
        t = ((r // g) * inv) % L if L > 1 else 0
        best = min(best, t if t else L)
    return best


def check_input(th, de, N, k):
    if N % 2 or N < 4:
        raise ValueError("N must be even and >= 4")
    if not (0 <= k < N / 6):
        raise ValueError("k must satisfy 0 <= k < N/6")
    if len(th) != 4 or len(de) != 4 or not all(isinstance(x, int) for x in list(th) + list(de)):
        raise ValueError("four integer phases and four integer tokens are required")


def contact_times(th, de, N, k, slot):
    """(tau_contact, tau_common, tau_slot): minima over all, non-slot and slot pairs."""
    check_input(th, de, N, k)
    common = slotm = INF
    for i in range(4):
        for j in range(i + 1, 4):
            t = pair_first(th[i] - th[j] - N // 2, de[i] - de[j], N, k)
            if slot in (i, j):
                slotm = min(slotm, t)
            else:
                common = min(common, t)
    return min(common, slotm), common, slotm


def first_contact(eng, th, de, N, k, slot):
    """Descriptor of the first-contact graph, classified by the pinned engine. Pure function of (th, de, slot)."""
    tau, common, slotm = contact_times(th, de, N, k, slot)
    d = {"tau": tau, "tau_common": common, "tau_slot": slotm}
    ps = N // math.gcd(N, de[slot] % N) if de[slot] % N else 1
    d["P_slot"] = ps
    d["P_rel"] = tuple(sorted((N // math.gcd(N, (de[slot] - de[j]) % N) if (de[slot] - de[j]) % N else 1) for j in range(4) if j != slot))
    if tau == INF:
        d.update(edges=(), types=(), slot_deg=None, slot_type=None, star=False)
        return d
    ph = {i: (th[i] + tau * de[i]) % N for i in range(4)}
    nodes = list(range(4))
    edges = sorted(tuple(sorted(e)) for e in eng.graph_edges_for(nodes, ph, N, k))
    adj = eng.build_adj(nodes, edges)
    comps = eng.connected_components(nodes, adj)
    typ = {}
    for c in comps:
        t = eng.classify_component(c, adj)[0]
        for v in c:
            typ[v] = t
    d["edges"] = tuple(edges)
    d["types"] = tuple(sorted(eng.classify_component(c, adj)[0] for c in comps))
    d["slot_deg"] = len(adj[slot])
    d["slot_type"] = typ[slot]
    d["star"] = any(t.startswith("star_k1c_") for t in d["types"])
    return d


def endpoint(r):
    at = r["M_at"]
    return int((at[str(Y_TICK)] if str(Y_TICK) in at else r["M"]) >= Y_THRESHOLD)


# ------------------------------------------------------------------ tables
def fmt_t(t):
    return "inf" if t == INF else ("none" if t is None else str(t))


def tables(eng, s1, cells, data, man, out=sys.stdout):
    w = lambda s="": print(s, file=out)
    grid = man["time_grid"]
    tb = man["birth_time_for_J4"]
    for c in cells:
        cfg = s1.REGISTRY[c]
        N, k, T = cfg["N"], cfg["k"], cfg["T"]
        rows = data[c]
        bases = sorted(rows)
        arms = [a for a in man["arms"] if a in s1.arms_for(N)]
        pairs = [p for p in PAIRS if p[0] in arms and p[1] in arms]
        w("=" * 100)
        w("cell %s  N=%d k=%d T=%d profile %s  base draws %d  arms %s" % (c, N, k, T, cfg["profile"], len(bases), ",".join(arms)))
        D = {a: {} for a in arms}
        for b in bases:
            for a in arms:
                r = rows[b][a]
                D[a][b] = first_contact(eng, r["th0"], r["d0"], N, k, r["slot"])
        # ---- T1 population
        w("\nT1 population: every base draw has every listed arm (checked); slot from the record; permuted copies not used")
        for a in arms:
            w("   %-5s n=%d  endpoint Y=1: %d" % (a, len(bases), sum(endpoint(rows[b][a]) for b in bases)))
        # ---- T2 contact descriptors
        w("\nT2 first-contact descriptors per arm (computed from th0, d0, slot; no engine stepping)")
        for a in arms:
            taus = [D[a][b]["tau"] for b in bases]
            fin = sorted(t for t in taus if t != INF)
            w("   %-5s tau_contact: never %d; attained by t<=g for g in %s: %s" % (a, len(taus) - len(fin), grid, [sum(1 for t in fin if t <= g) for g in grid]))
            if fin:
                q = lambda f: fin[min(len(fin) - 1, int(f * len(fin)))]
                w("          quantiles of finite tau (10/50/90 %%): %d / %d / %d; max %d" % (q(.1), q(.5), q(.9), fin[-1]))
            w("          slot degree in E_contact: %s" % dict(sorted(Counter("never" if D[a][b]["slot_deg"] is None else D[a][b]["slot_deg"] for b in bases).items(), key=str)))
            w("          slot component type: %s" % dict(Counter(str(D[a][b]["slot_type"]) for b in bases).most_common()))
            w("          first-contact component types (multiset, 8 most common): %s" % Counter(D[a][b]["types"] for b in bases).most_common(8))
            w("          unique-centre star in E_contact: %d" % sum(D[a][b]["star"] for b in bases))
            w("          slot period P(d_s): %s" % dict(sorted(Counter(D[a][b]["P_slot"] for b in bases).items())))
            w("          smallest relative period min_j N/gcd(N, d_s - d_j): %s" % dict(sorted(Counter(min(D[a][b]["P_rel"]) for b in bases).items())))
        # ---- T3 clocks
        w("\nT3 runner clocks per arm (fe, fb, t100 from the records; never relabelled); attainment by t<=g for g in %s" % grid)
        for a in arms:
            rr = [rows[b][a] for b in bases]
            cap_early = sum(1 for r in rr if r["hit_cap"] and r["steps"] < T)
            for name in ("fe", "fb", "t100"):
                v = [r[name] for r in rr]
                w("   %-5s %-4s none by the horizon %d; attained: %s" % (a, name, sum(1 for x in v if x is None), [sum(1 for x in v if x is not None and x <= g) for g in grid]))
            nc = sum(1 for b in bases if D[a][b]["tau"] == INF)
            nofe = sum(1 for b in bases if D[a][b]["tau"] != INF and rows[b][a]["fe"] is None)
            w("   %-5s categories: analytically no contact ever %d; contact but no fe by the horizon %d; cap reached before tick %d: %d"
              % (a, nc, nofe, T, cap_early))
            lag = Counter()
            for b in bases:
                t, fe = D[a][b]["tau"], rows[b][a]["fe"]
                if t != INF and fe is not None:
                    lag["fe<tau" if fe < t else "fe=tau" if fe == t else "fe>tau"] += 1
            w("   %-5s fe against tau_contact (both finite): %s" % (a, dict(lag)))
        # ---- T4 paired
        for r_, d_, lab in pairs:
            w("\nT4 paired %s vs %s, %s (same base draw: same th0, same three non-slot tokens - checked)" % (r_, d_, lab))
            mem = Counter()
            same = inv = 0
            cmpt = Counter()
            for b in bases:
                A, B = D[r_][b], D[d_][b]
                if A["tau_common"] != B["tau_common"]:
                    raise SystemExit("pairing error: tau_common differs within a pair (base %d)" % b)
                mem[membership(A, B)] += 1
                same += (A["tau"] == B["tau"] and A["edges"] == B["edges"])
                inv += (A["tau_common"] != INF and A["tau_slot"] > A["tau_common"] and B["tau_slot"] > B["tau_common"])
                cmpt["R<D" if A["tau"] < B["tau"] else "R=D" if A["tau"] == B["tau"] else "R>D"] += 1
            w("   slot in E_contact (R, D): %s" % dict(sorted(mem.items())))
            w("   identical first-contact time and graph: %d of %d" % (same, len(bases)))
            w("   strict common-contact condition (design §4.2: tau_common finite, both tau_slot > tau_common): %d of %d" % (inv, len(bases)))
            w("   tau_contact R vs D (infinity allowed): %s" % dict(cmpt))
        # ---- joint tables
        w("\nJoint tables (prelisted in the manifest; descriptive; post-intervention descriptors, not mediation estimates)")
        for r_, d_, lab in pairs:
            j1 = defaultdict(Counter)
            j2 = defaultdict(Counter)
            for b in bases:
                key = "(%d,%d)" % (endpoint(rows[b][r_]), endpoint(rows[b][d_]))
                A, B = D[r_][b], D[d_][b]
                j1[membership(A, B)][key] += 1
                flag = A["tau_common"] != INF and A["tau_slot"] > A["tau_common"] and B["tau_slot"] > B["tau_common"]
                j2["strict" if flag else "not strict"][key] += 1
            w("   J1 %s vs %s: rows slot membership (R, D), columns endpoint (Y_R, Y_D)" % (r_, d_))
            for m in sorted(j1):
                w("      %-14s %s" % (m, " ".join("%s:%d" % (kk, j1[m][kk]) for kk in ("(1,1)", "(1,0)", "(0,1)", "(0,0)"))))
            w("   J2 %s vs %s: rows strict common-contact condition, columns (Y_R, Y_D)" % (r_, d_))
            for m in ("strict", "not strict"):
                w("      %-14s %s" % (m, " ".join("%s:%d" % (kk, j2[m][kk]) for kk in ("(1,1)", "(1,0)", "(0,1)", "(0,0)"))))
        for a in arms:
            j3 = Counter((int(D[a][b]["star"]), endpoint(rows[b][a])) for b in bases)
            fbx = lambda r: r["fb"] is not None and r["fb"] <= tb
            j4 = Counter((int(fbx(rows[b][a])), endpoint(rows[b][a])) for b in bases)
            w("   J3 %-5s star in E_contact x Y: star&Y %d, star&noY %d, nostar&Y %d, nostar&noY %d" % (a, j3[(1, 1)], j3[(1, 0)], j3[(0, 1)], j3[(0, 0)]))
            w("   J4 %-5s fb<=%d x Y: born&Y %d, born&noY %d, notborn&Y %d, notborn&noY %d" % (a, tb, j4[(1, 1)], j4[(1, 0)], j4[(0, 1)], j4[(0, 0)]))


def membership(A, B):
    f = lambda X: "never" if X["slot_deg"] is None else ("in" if X["slot_deg"] > 0 else "out")
    return "R-%s/D-%s" % (f(A), f(B))


# ------------------------------------------------------------------ self-test (synthetic only)
def selftest():
    ok = True

    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond)
        print(("PASS " if cond else "FAIL ") + name)

    chk("Stage 1 library hashes to its pin", sha256_file(S1_LIB) == S1_LIB_SHA256)
    R = load(RUNNER, "az_tokres_run")
    eng, _ = R.load_engine(ENGINE, ORIENT, "P1")
    rng = random.Random(20261116)

    def engine_snapshot(th, de, N, k, Tmax):
        u = eng.Universe(N=N, k=k, theta={i: t % N for i, t in enumerate(th)}, delta={i: d % N for i, d in enumerate(de)})
        for _ in range(Tmax):
            ph = {x: (u.theta[x] + u.delta[x]) % N for x in u.theta}
            nodes = list(ph)
            E = sorted(tuple(sorted(e)) for e in eng.graph_edges_for(nodes, ph, N, k))
            if E:
                adj = eng.build_adj(nodes, E)
                return u.steps + 1, tuple(E), tuple(sorted(eng.classify_component(c, adj)[0] for c in eng.connected_components(nodes, adj)))
            eng.step_universe(u, multistar_policy="bound_symmetric")
            if len(u.theta) != 4 or u.edge_history[-1]:
                return "engine changed before a predicted contact", None, None
        return INF, (), ()

    # 1. graph, classifier and time against the engine's own pre-interaction snapshot
    n = agree = 0
    for N, k in ((120, 8), (122, 8), (240, 16), (242, 16), (480, 32), (12, 0), (30, 4)):
        for _ in range(300 if N > 12 else 60):
            th = [rng.randrange(N) for _ in range(4)]
            de = [rng.randrange(N) for _ in range(4)]
            s = rng.randrange(4)
            d = first_contact(eng, th, de, N, k, s)
            e = engine_snapshot(th, de, N, k, N + 1)
            n += 1
            agree += (d["tau"], d["edges"], d["types"]) == e
    chk("first-contact time, whole edge set and component types = engine pre-interaction snapshot (%d of %d)" % (agree, n), agree == n)
    # 2. fixtures of design §4
    d = first_contact(eng, [0, 6, 0, 0], [1, 0, 1, 1], 12, 0, 0)
    chk("t = N boundary: (N, k) = (12, 0), theta (0,6,0,0), delta (1,0,1,1) -> tau 12", d["tau"] == 12)
    dr = first_contact(eng, [109, 97, 80, 2], [0, 41, 21, 96], 120, 8, 0)
    dd = first_contact(eng, [109, 97, 80, 2], [1, 41, 21, 96], 120, 8, 0)
    chk("paired counterexample: tau 2 in both, E_R = {(1,2)}, E_D = {(0,1),(1,2)}, slot out in R and in in D",
        dr["tau"] == dd["tau"] == 2 and dr["edges"] == ((1, 2),) and dd["edges"] == ((0, 1), (1, 2)) and membership(dr, dd) == "R-out/D-in")
    chk("paired counterexample is not strict (tau_slot^D = tau_common)", not (dd["tau_slot"] > dd["tau_common"]))
    st = first_contact(eng, [0, 0, 60, 60], [0, 0, 0, 0], 120, 8, 0)
    chk("stationary K2,2: tau 1, one bound 4-cycle, no star", st["tau"] == 1 and st["types"] == ("cycle_c4_bound",) and not st["star"])
    nv = first_contact(eng, [0, 0, 0, 0], [0, 0, 0, 0], 120, 8, 2)
    chk("no contact ever: tau = inf, no graph, slot degree None", nv["tau"] == INF and nv["edges"] == () and nv["slot_deg"] is None)
    chk("periods: P(0) = 1, P(N/2) = 2, P(N/4) = 4 at N = 120",
        [first_contact(eng, [0, 1, 2, 3], [x, 7, 11, 13], 120, 8, 0)["P_slot"] for x in (0, 60, 30)] == [1, 2, 4])
    # 3. covariance
    good = True
    for _ in range(200):
        N, k = 120, 8
        th = [rng.randrange(N) for _ in range(4)]
        de = [rng.randrange(N) for _ in range(4)]
        s = rng.randrange(4)
        base = first_contact(eng, th, de, N, k, s)
        c = rng.randrange(N)
        sh_t = first_contact(eng, [(x + c) % N for x in th], de, N, k, s)
        sh_d = first_contact(eng, th, [(x + c) % N for x in de], N, k, s)   # common advance shift: graph unchanged
        p = [1, 2, 3, 0]
        rp = first_contact(eng, [th[p[i]] for i in range(4)], [de[p[i]] for i in range(4)], N, k, p.index(s))
        relabel = tuple(sorted(tuple(sorted((p.index(a), p.index(b)))) for a, b in base["edges"]))
        good &= (sh_t["tau"], sh_t["edges"]) == (base["tau"], base["edges"])
        good &= (sh_d["tau"], sh_d["edges"], sh_d["types"]) == (base["tau"], base["edges"], base["types"])
        good &= (rp["tau"], rp["types"], rp["slot_deg"], rp["slot_type"]) == (base["tau"], base["types"], base["slot_deg"], base["slot_type"])
        good &= rp["edges"] == relabel
    chk("covariance: common phase shift; common advance shift; node relabelling (time, types, slot role, relabelled edges)", good)
    # 4. invalid input refused
    refused = 0
    for args in (([0, 1, 2, 3], [0, 0, 0, 0], 121, 8), ([0, 1, 2, 3], [0, 0, 0, 0], 120, 20), ([0, 1, 2], [0, 0, 0], 120, 8), ([0, 1, 2, 3.5], [0, 0, 0, 0], 120, 8)):
        try:
            contact_times(*args, 0)
        except ValueError:
            refused += 1
    chk("invalid input refused (odd N, k >= N/6, three nodes, non-integer phase)", refused == 4)
    # 5. clock conversion: runner fb = engine tick of the first birth (birth_steps_list is written before steps += 1)
    good = True
    cnt = 0
    for _ in range(60):
        N, k = 120, 8
        th = [rng.randrange(N) for _ in range(4)]
        de = [rng.randrange(N) for _ in range(4)]
        r = R.run_state(eng, N, k, th, de, 300, 60, "bound_symmetric", tdr26=False)
        u = eng.Universe(N=N, k=k, theta={i: t for i, t in enumerate(th)}, delta={i: d for i, d in enumerate(de)})
        while u.steps < 300 and len(u.theta) < 60:
            eng.step_universe(u, multistar_policy="bound_symmetric")
        first = (u.birth_steps_list[0] + 1) if u.birth_steps_list else None
        good &= r["fb"] == first
        cnt += first is not None
    chk("clock conversion: runner fb = engine birth_steps_list[0] + 1 (%d of 60 synthetic runs with a birth; growth values not printed)" % cnt, good)
    # 6. freeze gate
    gate = freeze_errors({"frozen_script_sha256": None, "inputs": []}, registered=True)
    chk("freeze gate refuses an unfrozen manifest in registered mode", gate != [])
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def freeze_errors(man, registered):
    e = []
    if registered:
        if man.get("frozen_script_sha256") != sha256_file(os.path.abspath(__file__)):
            e.append("manifest is not frozen for this script (frozen_script_sha256 must equal this file's SHA-256)")
        for item in man.get("inputs", []):
            p = os.path.join(ROOT, item["hashes_file"])
            if not os.path.exists(p) or sha256_file(p) != item["sha256"]:
                e.append("input %s does not have the manifest's hash" % item["hashes_file"])
    return e


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--manifest")
    ap.add_argument("--dir")
    ap.add_argument("--plan", choices=("test", "registered"))
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.manifest and a.dir and a.plan):
        ap.error("--manifest, --dir and --plan are required")
    man = json.load(open(a.manifest))
    registered = a.plan == "registered"
    err = freeze_errors(man, registered)
    if err:
        print("REFUSED: " + "; ".join(err))
        return 2
    if sha256_file(S1_LIB) != S1_LIB_SHA256:
        print("REFUSED: Stage 1 library does not hash to its pin")
        return 2
    s1 = load(S1_LIB, "az_tokres_analyse")
    R = load(RUNNER, "az_tokres_run")
    eng, _ = R.load_engine(ENGINE, ORIENT, "P1")
    cells = man["cells_registered"] if registered else man["cells_test"]
    pins = {"engine": sha256_file(ENGINE), "orient": sha256_file(ORIENT), "runner": sha256_file(RUNNER),
            "fixtures": s1.FIXTURES_SHA256, "golden": s1.GOLDEN_SHA256}
    print("contact tables script SHA-256 %s; manifest %s; plan %s" % (sha256_file(os.path.abspath(__file__)), sha256_file(a.manifest), a.plan))
    if not registered:
        print("*** TEST RECORDS: instrument validation only; no evidential value ***")
    data, errors = {}, []
    for c in cells:
        cfg = s1.REGISTRY[c]
        if cfg["profile"] != "P1":
            errors.append("%s: profile %s is not covered by this script (P1 only)" % (c, cfg["profile"]))
            continue
        files = sorted(glob.glob(os.path.join(glob.escape(a.dir), c + "_*.jsonl")))
        rows, errs = s1.validate(files, cfg, pins)
        errors += ["%s: %s" % (c, x) for x in errs]
        if not files:
            errors.append("%s: no record file" % c)
        for b in rows:
            base = rows[b].get("BASE")
            for arm, r in rows[b].items():
                if arm.endswith("_P"):          # node-label permuted copies: relabelled by design, not used here
                    continue
                if base and (r["th0"] != base["th0"] or [x for i, x in enumerate(r["d0"]) if i != r["slot"]] != [x for i, x in enumerate(base["d0"]) if i != r["slot"]]):
                    errors.append("%s: base %d arm %s: pairing keys (th0, non-slot tokens) differ from BASE" % (c, b, arm))
        data[c] = rows
    if errors:
        print("INTEGRITY: FAIL (%d). No table is produced." % len(errors))
        for x in errors[:30]:
            print("  - " + x)
        return 2
    print("INTEGRITY: PASS (Stage 1 validator: identity, custody, states, records, set; pairing keys)")
    tables(eng, s1, cells, data, man)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
