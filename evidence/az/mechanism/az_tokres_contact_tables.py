#!/usr/bin/env python3
"""AZ token resonance, mechanism study - exploratory first-contact tables on existing records.
[SESSION] NONCANONICAL. Implements the table contract of records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md §5
(review of PR #281 r2, readback 5921285881) and nothing else. Exploratory: the outcomes are known.

    python3 -I az_tokres_contact_tables.py --selftest
    python3 -I az_tokres_contact_tables.py --manifest M.json --dir DIR --plan test [--json OUT.jsonl]
    python3 -I az_tokres_contact_tables.py --manifest M.json --dir DIR --plan registered [--json OUT.jsonl]  (refused until frozen)

GATES, all before any record file is looked up or opened (review 5922692022, R1-R2):
  plan and cells   --plan test accepts only Stage 1 test cells (TEST-*, tag SMOKE, confirmatory False);
                   --plan registered accepts only registered cells (tag AZ-TOKRES-S1, confirmatory True);
                   a mixed or unknown cell list is refused;
  freeze           --plan registered: the manifest's frozen_script_sha256 equals this file's SHA-256;
  pins             the manifest's pins equal the bytes of engine, orientation reference, runner and the Stage 1
                   library, checked before any of them is imported;
  input binding    exactly one trusted hash list: for registered, the repository file named in the manifest with its
                   SHA-256; for test, the test directory's own HASHES.txt. Every selected record file and its side
                   manifest must be listed there with an equal hash; a listed piece of a selected cell that is not
                   selected, an unlisted file, or a duplicate is refused.
Then: the Stage 1 validator (unchanged), the pairing keys, and a clock and endpoint layer (R3) - any failure: no table.

What it computes, per record, without stepping the engine (only from th0, d0 and the slot):
  tau_contact    first processed tick whose post-advance, pre-interaction defect graph has an edge, by the closed
                 form of design §4 (infinity if none in 1..N, hence never);
  E_contact      the whole first-contact graph, classified with the pinned engine's own classifier;
  slot           degree and component type of the replaced node in E_contact; period P(d_s) = N/gcd(N, d_s) and the
                 three relative periods N/gcd(N, d_s - d_j);
  tau_common, tau_slot   the same minimum over the three pairs without / with the slot (design §4.2).
and reads the runner clocks fe, fb, t100 and the endpoint Y = 1{M >= 100 at tick 800} (cap before 800: positive).
Tables T1-T4 and the four prelisted joint tables J1-J4 are printed; with --json, every per-record descriptor (full
edge set, component types, all three relative periods, clocks, endpoint) is written as deterministic JSON lines.
No test, no p-value, no verdict.
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
PINS = {"engine": (ENGINE, "4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608"),
        "orient": (ORIENT, "ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c"),
        "runner": (RUNNER, "75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992"),
        "stage1_analysis_library": (S1_LIB, S1_LIB_SHA256)}
SUPPORTED_PAIRS = [["O1R", "O1D"], ["O2R", "O2D"]]
SUPPORTED_JOINT = ["J1", "J2", "J3", "J4"]
TEST_CELLS = {"TEST-C1": (120, 8, 800), "TEST-C2": (122, 8, 800)}
ARMS_BY_RESIDUE = {True: {"BASE", "O1R", "O1D", "O2R", "O2D", "SHAM"}, False: {"BASE", "O1R", "O1D", "Q2R", "SHAM"}}   # 4 | N, else
REG_CELLS = {"S1-C1": (120, 8, 800), "S1-C2": (122, 8, 800)}
CHECKPOINTS = (100, 200, 300, 400, 500, 600, 700, 800)
INF = float("inf")
Y_THRESHOLD, Y_TICK = 100, 800
PAIR_LABEL = {"O1R": "order 1 (2x = 0)", "O2R": "order 2 (2x = N/2)"}


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



class Refused(Exception):
    pass


# ------------------------------------------------------------------ gates (no record is looked up before they pass)
def check_manifest(man, plan):
    """Schema, supported values, plan/cell consistency. Pure: reads nothing from disk."""
    e = []
    if man.get("schema") != "az_tokres_contact_tables_manifest_v2":
        e.append("manifest schema must be az_tokres_contact_tables_manifest_v2")
    cells = man.get("cells_registered" if plan == "registered" else "cells_test")
    allowed = REG_CELLS if plan == "registered" else TEST_CELLS
    if not isinstance(cells, list) or not cells or len(set(cells)) != len(cells) or any(c not in allowed for c in cells):
        e.append("cells for plan %s must be a non-empty list of distinct values from %s" % (plan, sorted(allowed)))
    other = man.get("cells_test" if plan == "registered" else "cells_registered", [])
    forbidden = TEST_CELLS if plan == "registered" else REG_CELLS
    if not isinstance(other, list) or any(c not in forbidden for c in other):
        e.append("the other plan's cell list may contain only that plan's cells")
    if man.get("pairs") is None or not isinstance(man["pairs"], list) or not man["pairs"] or any(p not in SUPPORTED_PAIRS for p in man["pairs"]) \
            or len({tuple(p) for p in man["pairs"]}) != len(man["pairs"]):
        e.append("pairs must be a non-empty list of distinct values from %s" % SUPPORTED_PAIRS)
    if sorted(man.get("joint_tables", {})) != SUPPORTED_JOINT:
        e.append("joint_tables must name exactly %s" % SUPPORTED_JOINT)
    g = man.get("time_grid")
    if not (isinstance(g, list) and g and all(isinstance(x, int) and not isinstance(x, bool) for x in g)
            and all(1 <= x <= 800 for x in g) and all(a < b for a, b in zip(g, g[1:]))):
        e.append("time_grid must be strictly increasing integers in 1..800")
    tb = man.get("birth_time_for_J4")
    if not (isinstance(tb, int) and not isinstance(tb, bool) and 1 <= tb <= 800):
        e.append("birth_time_for_J4 must be an integer in 1..800")
    arms = man.get("arms")
    if not (isinstance(arms, list) and arms and len(set(arms)) == len(arms) and "BASE" in arms
            and all(a in ("BASE", "O1R", "O1D", "O2R", "O2D", "Q2R", "SHAM") for a in arms)):
        e.append("arms must be distinct Stage 1 arm names including BASE")
    elif isinstance(man.get("pairs"), list):
        for p in man["pairs"]:
            if isinstance(p, list) and not set(p) <= set(arms):
                e.append("pair %s uses an arm not listed in arms" % p)
        if isinstance(cells, list):
            for c in cells:
                if c in allowed:
                    avail = ARMS_BY_RESIDUE[allowed[c][0] % 4 == 0]
                    if not set(arms) <= avail:
                        e.append("arms %s do not exist in cell %s" % (sorted(set(arms) - avail), c))
    if plan == "registered":
        ins = man.get("inputs")
        if not (isinstance(ins, list) and len(ins) == 1 and isinstance(ins[0], dict)
                and {"hashes_file", "sha256", "commit"} <= set(ins[0])):
            e.append("registered plan needs exactly one input with hashes_file, sha256 and commit")
    if e:
        raise Refused("; ".join(e))
    return cells


def check_pins(man):
    """Pins of the manifest = this script's pins = the bytes on disk, before anything is imported."""
    e = []
    for name, (path, want) in PINS.items():
        if man.get("pins", {}).get(name) != want:
            e.append("manifest pin %s differs from the script's" % name)
        elif sha256_file(path) != want:
            e.append("%s does not hash to its pin" % name)
    if e:
        raise Refused("; ".join(e))


def check_freeze(man, plan):
    if plan == "registered" and man.get("frozen_script_sha256") != sha256_file(os.path.abspath(__file__)):
        raise Refused("manifest is not frozen for this script (frozen_script_sha256 must equal this file's SHA-256)")


def trusted_list(man, plan, d):
    """(path, {name: sha256}) of the one trusted hash list."""
    if plan == "registered":
        item = man["inputs"][0]
        p = os.path.join(ROOT, item["hashes_file"])
        if not os.path.isfile(p) or sha256_file(p) != item["sha256"]:
            raise Refused("input %s does not have the manifest's hash" % item["hashes_file"])
    else:
        p = os.path.join(d, "HASHES.txt")
        if not os.path.isfile(p):
            raise Refused("test directory has no HASHES.txt")
    listed = {}
    for ln in open(p):
        parts = ln.split()
        if len(parts) != 2:
            raise Refused("malformed line in %s" % os.path.basename(p))
        h, name = parts[0], parts[1].lstrip("*")
        if name in listed:
            raise Refused("%s lists %s twice" % (os.path.basename(p), name))
        listed[name] = h
    return p, listed


def bind_inputs(cells, listed, d):
    """Every selected piece is listed with an equal hash; nothing listed for a selected cell is missing; no extra file."""
    e = []
    files = {}
    for c in cells:
        want = sorted(n for n in listed if n.startswith(c + "_") and n.endswith(".jsonl"))
        have = sorted(os.path.basename(x) for x in glob.glob(os.path.join(glob.escape(d), c + "_*")))
        need = sorted(want + [n + ".manifest.json" for n in want])
        if not want:
            e.append("%s: the trusted list names no record file" % c)
        for n in sorted(set(need) - set(have)):
            e.append("%s: listed piece %s is missing" % (c, n))
        for n in sorted(set(have) - set(need)):
            e.append("%s: %s is not in the trusted list" % (c, n))
        for n in sorted(set(need) & set(have)):
            if listed.get(n) is None or sha256_file(os.path.join(d, n)) != listed[n]:
                e.append("%s: %s does not have the listed hash" % (c, n))
        files[c] = [os.path.join(d, n) for n in want]
    if e:
        raise Refused("; ".join(e[:20]))
    return files


# ------------------------------------------------------------------ clock and endpoint layer (R3)
def clock_errors(r, d, T, cap):
    """Integrity of fe, fb, t100, M_at and the endpoint for one record, given its first-contact descriptor d."""
    e = []
    isint = lambda x: isinstance(x, int) and not isinstance(x, bool)
    steps, M, at = r.get("steps"), r.get("M"), r.get("M_at")
    if not (isint(steps) and 0 <= steps <= T and isint(M) and M >= 4 and isinstance(at, dict) and isinstance(r.get("hit_cap"), bool)
            and isint(r.get("births"))):
        return ["steps, M, births, hit_cap or M_at malformed"]
    for key, v in at.items():
        if not (key.isdigit() and int(key) in CHECKPOINTS and isint(v) and 4 <= v <= M):
            e.append("checkpoint %r malformed" % key)
    if set(int(x) for x in at if x.isdigit()) != {c for c in CHECKPOINTS if c <= steps}:
        e.append("checkpoints are not exactly the ticks <= steps")
    vals = [at[str(c)] for c in CHECKPOINTS if str(c) in at]
    if any(a > b for a, b in zip(vals, vals[1:])):
        e.append("checkpoints decrease")
    if str(steps) in at and at[str(steps)] != M:
        e.append("checkpoint at the last tick differs from M")
    if r["hit_cap"] != (M >= cap) or (steps < T and not r["hit_cap"]):
        e.append("stop reason inconsistent (hit_cap, M, steps)")
    if r["births"] != M - 4:
        e.append("M != 4 + births")
    for name in ("fe", "fb", "t100"):
        v = r.get(name, "absent")
        if v == "absent":
            e.append("%s absent" % name)
        elif v is not None and not (isint(v) and 1 <= v <= steps):
            e.append("%s = %r is not None or an integer in 1..steps" % (name, v))
    if e:
        return e
    fe, fb, t100, tau = r["fe"], r["fb"], r["t100"], d["tau"]
    if (fb is None) != (r["births"] == 0):
        e.append("fb present iff births > 0 violated")
    if (t100 is None) != (M < Y_THRESHOLD):
        e.append("t100 present iff M >= 100 violated")
    if tau == INF and (fe is not None or fb is not None or M != 4):
        e.append("an event or a birth although no contact ever occurs")
    if fe is not None and tau != INF and fe < tau:
        e.append("fe < tau_contact")
    if fb is not None and tau != INF and fb < tau:
        e.append("fb < tau_contact")
    if fb is not None and (fe is None or fe > fb):
        e.append("a birth without an earlier or simultaneous counted event (fe <= fb violated)")
    if t100 is not None and fb is not None and t100 < fb:
        e.append("t100 < fb")
    for c in CHECKPOINTS:
        if str(c) in at and (at[str(c)] >= Y_THRESHOLD) != (t100 is not None and c >= t100):
            e.append("checkpoint %d inconsistent with t100" % c)
            break
    for c in CHECKPOINTS:                       # M starts at 4 and never decreases: M(c) > 4 iff the first birth is at or before c
        if str(c) in at and (at[str(c)] > 4) != (fb is not None and fb <= c):
            e.append("checkpoint %d inconsistent with fb" % c)
            break
    return e


def endpoint(r, cap, T=800):
    """Y = 1{M >= 100 at tick 800}. Without a tick-800 checkpoint only a valid cap stop before 800 counts (positive)."""
    at = r["M_at"]
    if str(Y_TICK) in at:
        return int(at[str(Y_TICK)] >= Y_THRESHOLD)
    if r["hit_cap"] and r["steps"] < Y_TICK and r["M"] >= cap:
        return 1
    raise Refused("record without a tick-800 checkpoint that did not stop at the cap before tick 800")


# ------------------------------------------------------------------ tables
def fmt_t(t):
    return "inf" if t == INF else ("none" if t is None else str(t))


def paired_clock(xa, xb):
    """Paired order of two event times; None = not attained by the horizon."""
    c = Counter()
    for a, b in zip(xa, xb):
        if a is None and b is None:
            c["neither"] += 1
        elif a is None:
            c["D only"] += 1
        elif b is None:
            c["R only"] += 1
        else:
            c["R<D" if a < b else "R=D" if a == b else "R>D"] += 1
    return dict(sorted(c.items()))


def tables(cells, data, D, Y, cfgs, man, out=sys.stdout):
    w = lambda s="": print(s, file=out)
    grid = man["time_grid"]
    tb = man["birth_time_for_J4"]
    for c in cells:
        N, k, T = cfgs[c]
        rows = data[c]
        bases = sorted(rows)
        arms = [a for a in man["arms"] if a in rows[bases[0]]]
        pairs = [p for p in man["pairs"] if p[0] in arms and p[1] in arms]
        w("=" * 100)
        w("cell %s  N=%d k=%d T=%d  base draws %d  arms %s  pairs %s" % (c, N, k, T, len(bases), ",".join(arms), pairs))
        w("\nT1 population: every base draw has every listed arm (checked); slot from the record; permuted copies not used")
        for a in arms:
            w("   %-5s n=%d  endpoint Y=1: %d" % (a, len(bases), sum(Y[c][a][b] for b in bases)))
        w("\nT2 first-contact descriptors per arm (from th0, d0, slot; no engine stepping; full descriptors in the JSON output)")
        for a in arms:
            dd = [D[c][a][b] for b in bases]
            fin = sorted(x["tau"] for x in dd if x["tau"] != INF)
            w("   %-5s tau_contact: never %d; attained by t<=g for g in %s: %s" % (a, len(dd) - len(fin), grid, [sum(1 for t in fin if t <= g) for g in grid]))
            if fin:
                q = lambda f: fin[min(len(fin) - 1, int(f * len(fin)))]
                w("          quantiles of finite tau (10/50/90 %%): %d / %d / %d; max %d" % (q(.1), q(.5), q(.9), fin[-1]))
            w("          slot degree in E_contact: %s" % dict(sorted(Counter("never" if x["slot_deg"] is None else x["slot_deg"] for x in dd).items(), key=str)))
            w("          slot component type: %s" % dict(sorted(Counter(str(x["slot_type"]) for x in dd).items())))
            w("          first-contact component-type multisets: %s" % sorted(Counter(x["types"] for x in dd).items()))
            w("          first-contact edge sets (as sets of node pairs; 12 most common): %s" % Counter(x["edges"] for x in dd).most_common(12))
            w("          unique-centre star in E_contact: %d" % sum(x["star"] for x in dd))
            w("          slot period P(d_s): %s" % dict(sorted(Counter(x["P_slot"] for x in dd).items())))
            w("          sorted triple of relative periods N/gcd(N, d_s - d_j) (12 most common): %s" % Counter(x["P_rel"] for x in dd).most_common(12))
        w("\nT3 runner clocks per arm (fe, fb, t100 as recorded; checked against tau_contact and each other); attainment by t<=g, g in %s" % grid)
        for a in arms:
            rr = [rows[b][a] for b in bases]
            for name in ("fe", "fb", "t100"):
                v = [r[name] for r in rr]
                w("   %-5s %-4s not attained by the end of the run %d; attained: %s" % (a, name, sum(1 for x in v if x is None), [sum(1 for x in v if x is not None and x <= g) for g in grid]))
            nc = sum(1 for b in bases if D[c][a][b]["tau"] == INF)
            nofe = sum(1 for b in bases if D[c][a][b]["tau"] != INF and rows[b][a]["fe"] is None)
            cap_early = sum(1 for r in rr if r["hit_cap"] and r["steps"] < T)
            w("   %-5s categories: no contact ever (proved by the closed form) %d; contact but no counted event by the end %d; stopped at the cap before tick %d: %d"
              % (a, nc, nofe, T, cap_early))
            lag = Counter(("fe=tau" if rows[b][a]["fe"] == D[c][a][b]["tau"] else "fe>tau") for b in bases
                          if rows[b][a]["fe"] is not None)
            w("   %-5s fe against tau_contact (fe < tau is an integrity failure and cannot occur here): %s" % (a, dict(sorted(lag.items()))))
        for r_, d_ in pairs:
            lab = PAIR_LABEL[r_]
            w("\nT4 paired %s vs %s, %s (same base draw: same th0 and three non-slot tokens - checked)" % (r_, d_, lab))
            A = [D[c][r_][b] for b in bases]
            B = [D[c][d_][b] for b in bases]
            for x, y in zip(A, B):
                if x["tau_common"] != y["tau_common"]:
                    raise Refused("pairing error: tau_common differs within a pair")
            w("   slot in E_contact (R, D): %s" % dict(sorted(Counter(membership(x, y) for x, y in zip(A, B)).items())))
            w("   identical first-contact time and edge set: %d of %d" % (sum(x["tau"] == y["tau"] and x["edges"] == y["edges"] for x, y in zip(A, B)), len(bases)))
            w("   strict common-contact condition (design §4.2): %d of %d" % (sum(strict(x, y) for x, y in zip(A, B)), len(bases)))
            ta = [None if x["tau"] == INF else x["tau"] for x in A]
            tbb = [None if y["tau"] == INF else y["tau"] for y in B]
            w("   tau_contact, paired (None = no contact ever): %s" % paired_clock(ta, tbb))
            for name in ("fe", "fb", "t100"):
                xa = [rows[b][r_][name] for b in bases]
                xb = [rows[b][d_][name] for b in bases]
                w("   %-4s paired (not attained kept as its own category): %s" % (name, paired_clock(xa, xb)))
                w("        both attained by t<=g, R only, D only, for g in %s: %s" % (grid, [
                    (sum(1 for u, v in zip(xa, xb) if u is not None and v is not None and u <= g and v <= g),
                     sum(1 for u, v in zip(xa, xb) if u is not None and u <= g and not (v is not None and v <= g)),
                     sum(1 for u, v in zip(xa, xb) if v is not None and v <= g and not (u is not None and u <= g))) for g in grid]))
        w("\nJoint tables (manifest: %s; descriptive; post-intervention descriptors, not mediation estimates)" % ", ".join(SUPPORTED_JOINT))
        cols = ("(1,1)", "(1,0)", "(0,1)", "(0,0)")
        for r_, d_ in pairs:
            j1, j2 = defaultdict(Counter), defaultdict(Counter)
            for b in bases:
                key = "(%d,%d)" % (Y[c][r_][b], Y[c][d_][b])
                x, y = D[c][r_][b], D[c][d_][b]
                j1[membership(x, y)][key] += 1
                j2["strict" if strict(x, y) else "not strict"][key] += 1
            w("   J1 %s vs %s: rows slot membership (R, D), columns endpoint (Y_R, Y_D)" % (r_, d_))
            for m in sorted(j1):
                w("      %-14s %s" % (m, " ".join("%s:%d" % (kk, j1[m][kk]) for kk in cols)))
            w("   J2 %s vs %s: rows strict common-contact condition, columns (Y_R, Y_D)" % (r_, d_))
            for m in ("strict", "not strict"):
                w("      %-14s %s" % (m, " ".join("%s:%d" % (kk, j2[m][kk]) for kk in cols)))
        for a in arms:
            j3 = Counter((int(D[c][a][b]["star"]), Y[c][a][b]) for b in bases)
            j4 = Counter((int(rows[b][a]["fb"] is not None and rows[b][a]["fb"] <= tb), Y[c][a][b]) for b in bases)
            w("   J3 %-5s star in E_contact x Y: star&Y %d, star&noY %d, nostar&Y %d, nostar&noY %d" % (a, j3[(1, 1)], j3[(1, 0)], j3[(0, 1)], j3[(0, 0)]))
            w("   J4 %-5s fb<=%d x Y: born&Y %d, born&noY %d, notborn&Y %d, notborn&noY %d" % (a, tb, j4[(1, 1)], j4[(1, 0)], j4[(0, 1)], j4[(0, 0)]))


def strict(x, y):
    return x["tau_common"] != INF and x["tau_slot"] > x["tau_common"] and y["tau_slot"] > y["tau_common"]


def membership(A, B):
    f = lambda X: "never" if X["slot_deg"] is None else ("in" if X["slot_deg"] > 0 else "out")
    return "R-%s/D-%s" % (f(A), f(B))


def descriptor_json(cell, b, arm, r, d, y):
    j = lambda t: None if t == INF else t
    return json.dumps({"cell": cell, "base": b, "arm": arm, "slot": r["slot"], "tau_contact": j(d["tau"]), "tau_common": j(d["tau_common"]),
                       "tau_slot": j(d["tau_slot"]), "edges": [list(e) for e in d["edges"]], "types": list(d["types"]),
                       "slot_deg": d["slot_deg"], "slot_type": d["slot_type"], "star": d["star"], "P_slot": d["P_slot"],
                       "P_rel": list(d["P_rel"]), "fe": r["fe"], "fb": r["fb"], "t100": r["t100"], "Y": y}, sort_keys=True)


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
    # 6. gates (R1, R2): refused before any record is looked up
    man = json.load(open(os.path.join(HERE, "contact_tables_manifest.json")))

    import tempfile
    tmpd = tempfile.mkdtemp(prefix="az_ct_selftest_")

    def refused_before_binding(m, plan, d="/nonexistent-directory", want="", js=None):
        probe = []
        try:
            run(m, plan, d, json_out=js, _probe=probe)
        except Refused as ex:
            return probe == [] and want in str(ex)
        return False
    newjs = lambda: os.path.join(tmpd, "out_%d.jsonl" % len(os.listdir(tmpd)))
    m1 = dict(man, cells_test=["S1-C1"])
    chk("R1: test plan naming a registered cell is refused before any lookup", refused_before_binding(m1, "test"))
    m2 = dict(man, cells_test=["TEST-C1", "S1-C1"])
    chk("R1: mixed cell list refused before any lookup", refused_before_binding(m2, "test"))
    m3 = dict(man, cells_registered=["TEST-C1"])
    chk("R1: registered plan naming a test cell refused", refused_before_binding(dict(m3, frozen_script_sha256=sha256_file(os.path.abspath(__file__))), "registered"))
    chk("freeze: unfrozen manifest refused in registered mode before any lookup", refused_before_binding(man, "registered"))
    fz0 = dict(man, frozen_script_sha256=sha256_file(os.path.abspath(__file__)))
    chk("R4: registered plan without --json refused before any lookup", refused_before_binding(fz0, "registered", want="--json is required"))
    fz = dict(man, frozen_script_sha256=sha256_file(os.path.abspath(__file__)))
    chk("R2: frozen manifest with no input refused", refused_before_binding(dict(fz, inputs=[]), "registered", want="exactly one input", js=newjs()))
    chk("R2: frozen manifest with a wrong pin refused",
        refused_before_binding(dict(fz, pins=dict(fz["pins"], runner="0" * 64)), "registered", want="manifest pin runner", js=newjs()))
    chk("R2: frozen manifest with a wrong input hash refused",
        refused_before_binding(dict(fz, inputs=[dict(fz["inputs"][0], sha256="0" * 64)]), "registered", want="does not have the manifest's hash", js=newjs()))
    ex = os.path.join(tmpd, "exists.jsonl"); open(ex, "w").close()
    chk("R5: existing --json target refused before any lookup", refused_before_binding(man, "test", d=tmpd, want="exists", js=ex))
    chk("R5: --json target inside the record directory refused", refused_before_binding(man, "test", d=tmpd, want="protected", js=os.path.join(tmpd, "new.jsonl")))
    chk("R5: --json target in a missing directory refused", refused_before_binding(man, "test", want="directory does not exist", js=os.path.join(tmpd, "no", "x.jsonl")))
    for bad, why in ((dict(man, arms=man["arms"] + ["Q2R"]), "Q2R in a cell with 4 | N"),
                     (dict(man, cells_test=["TEST-C2"]), "O2R/O2D in a cell with N = 2 mod 4"),
                     (dict(man, pairs=[["O1R", "O2D"]]), "unsupported pair"), (dict(man, joint_tables={"J1": ""}), "joint tables"),
                     (dict(man, time_grid=[1, 5, 5]), "grid not increasing"), (dict(man, birth_time_for_J4=0), "J4 time 0"),
                     (dict(man, schema="v1"), "schema")):
        chk("R4: manifest field enforced (%s)" % why, refused_before_binding(bad, "test"))
    # 7. clock and endpoint layer (R3): the reviewer's counterexamples and others
    d1 = {"tau": 3}
    ok_rec = {"steps": 800, "M": 120, "births": 116, "hit_cap": False, "fe": 3, "fb": 550, "t100": 650,
              "M_at": {str(c): (4 if c < 700 else 120) for c in CHECKPOINTS}}
    ok_rec["M_at"]["600"] = 90
    chk("R3: a consistent record passes", clock_errors(ok_rec, d1, 800, 300) == [])
    cases = [("fe = -1", {"fe": -1}), ("fe = 801", {"fe": 801}), ("fe = 'invalid'", {"fe": "invalid"}), ("fb = 801", {"fb": 801}),
             ("negative t100", {"t100": -5}), ("t100 missing although M >= 100", {"t100": None}), ("fe < tau_contact", {"fe": 2}),
             ("fb before fe", {"fe": 551, "fb": 550}), ("t100 < fb", {"t100": 540, "M_at": dict(ok_rec["M_at"], **{"600": 120})}),
             ("steps 800, M 100, M_at[800] = 4", {"M": 100, "births": 96, "M_at": dict(ok_rec["M_at"], **{"700": 4, "800": 4})}),
             ("M != 4 + births", {"births": 7}), ("checkpoint missing", {"M_at": {k: v for k, v in ok_rec["M_at"].items() if k != "300"}}),
             ("fb without births", {"births": 0, "M": 4, "t100": None, "M_at": {str(c): 4 for c in CHECKPOINTS}})]
    chk("R3: every listed inconsistency is an integrity error (%d cases)" % len(cases),
        all(clock_errors(dict(ok_rec, **ch), d1, 800, 300) for _, ch in cases))
    capped = {"steps": 512, "M": 300, "births": 296, "hit_cap": True, "fe": 3, "fb": 150, "t100": 400,
              "M_at": {"100": 4, "200": 10, "300": 40, "400": 100, "500": 290}}
    rv = {"steps": 300, "M": 5, "births": 1, "hit_cap": False, "fe": 3, "t100": None, "M_at": {"100": 4, "200": 5, "300": 5}}
    chk("R3 (r3): M(100) = 4, M(200) = 5 accepts fb = 150 and refuses fb = 50 and fb = 250",
        clock_errors(dict(rv, fb=150), d1, 300, 300) == [] and clock_errors(dict(rv, fb=50), d1, 300, 300) != []
        and clock_errors(dict(rv, fb=250), d1, 300, 300) != [])
    chk("R3: a valid cap stop before tick 800 passes and is positive", clock_errors(capped, d1, 800, 300) == [] and endpoint(capped, 300) == 1)
    try:
        endpoint(dict(capped, hit_cap=False), 300)
        no_cp = False
    except Refused:
        no_cp = True
    chk("R3: a missing tick-800 checkpoint without a cap stop is refused, not counted", no_cp)
    chk("R3: events without any contact are an integrity error", clock_errors(dict(ok_rec), {"tau": INF}, 800, 300) != [])
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1



def check_output_target(json_out, plan, d, protected):
    """The descriptor file must be new: not existing (as a file, link or anything else), not inside the record directory,
    not inside upload/ or evidence/az/scripts/, and its directory must exist. Checked before any record is processed;
    the file is then created with O_EXCL, so a target that appears in the meantime is refused too."""
    if json_out is None:
        if plan == "registered":
            raise Refused("--json is required for the registered plan (the full descriptors must be stored)")
        return None
    t = os.path.abspath(json_out)
    if os.path.lexists(t):
        raise Refused("--json target exists; it must be a new file")
    parent = os.path.dirname(t)
    if not os.path.isdir(parent):
        raise Refused("--json target directory does not exist")
    rp = os.path.realpath(parent)
    for q in [d, os.path.join(ROOT, "upload"), os.path.join(ROOT, "evidence", "az", "scripts")] + list(protected):
        q = os.path.realpath(q)
        if rp == q or rp.startswith(q.rstrip(os.sep) + os.sep) or os.path.realpath(t) == q:
            raise Refused("--json target lies in a protected location (record directory, upload/, scripts, or an input)")
    return t


def run(man, plan, d, json_out=None, out=sys.stdout, _probe=None):
    """All gates first; records are looked up only after check_manifest, check_freeze, check_pins, output target, trusted_list."""
    cells = check_manifest(man, plan)
    check_freeze(man, plan)
    check_pins(man)
    tl_path = os.path.join(ROOT, man["inputs"][0]["hashes_file"]) if plan == "registered" else os.path.join(d, "HASHES.txt")
    json_out = check_output_target(json_out, plan, d, [tl_path] + [x for x, _ in PINS.values()])
    _, listed = trusted_list(man, plan, d)
    files = bind_inputs(cells, listed, d)
    if _probe is not None:
        _probe.append("bound")
    s1 = load(S1_LIB, "az_tokres_analyse")
    R = load(RUNNER, "az_tokres_run")
    eng, _ = R.load_engine(ENGINE, ORIENT, "P1")
    want_tag = "AZ-TOKRES-S1" if plan == "registered" else "SMOKE"
    pins = {"engine": PINS["engine"][1], "orient": PINS["orient"][1], "runner": PINS["runner"][1],
            "fixtures": s1.FIXTURES_SHA256, "golden": s1.GOLDEN_SHA256}
    data, D, Y, cfgs, errors = {}, {}, {}, {}, []
    for c in cells:
        cfg = s1.REGISTRY[c]
        if cfg["tag"] != want_tag or cfg["confirmatory"] != (plan == "registered") or cfg["profile"] != "P1" \
                or (cfg["N"], cfg["k"], cfg["T"]) != (REG_CELLS if plan == "registered" else TEST_CELLS)[c]:
            raise Refused("%s: the Stage 1 registry entry does not match plan %s" % (c, plan))
        cfgs[c] = (cfg["N"], cfg["k"], cfg["T"])
        rows, errs = s1.validate(files[c], cfg, pins)
        errors += ["%s: %s" % (c, x) for x in errs]
        D[c], Y[c] = defaultdict(dict), defaultdict(dict)
        for b in sorted(rows):
            base = rows[b].get("BASE")
            for arm in man["arms"]:
                r = rows[b].get(arm)
                if r is None:
                    if arm in s1.arms_for(cfg["N"]):
                        errors.append("%s: base %d: arm %s missing" % (c, b, arm))
                    continue
                if base is None or r["th0"] != base["th0"] or [x for i, x in enumerate(r["d0"]) if i != r["slot"]] != \
                        [x for i, x in enumerate(base["d0"]) if i != r["slot"]]:
                    errors.append("%s: base %d arm %s: pairing keys (th0, non-slot tokens) differ from BASE" % (c, b, arm))
                    continue
                dd = first_contact(eng, r["th0"], r["d0"], cfg["N"], cfg["k"], r["slot"])
                ce = clock_errors(r, dd, cfg["T"], cfg["cap"])
                if ce:
                    errors += ["%s: base %d arm %s: %s" % (c, b, arm, x) for x in ce[:3]]
                    continue
                try:
                    Y[c][arm][b] = endpoint(r, cfg["cap"])
                except Refused as ex:
                    errors.append("%s: base %d arm %s: %s" % (c, b, arm, ex))
                    continue
                D[c][arm][b] = dd
        data[c] = rows
    if errors:
        print("INTEGRITY: FAIL (%d). No table is produced." % len(errors), file=out)
        for x in errors[:30]:
            print("  - " + x, file=out)
        return 2
    print("INTEGRITY: PASS (trusted hash list binding; Stage 1 validator: identity, custody, states, records, set; pairing keys; clocks and endpoint)", file=out)
    tables(cells, data, D, Y, cfgs, man, out=out)
    if json_out:
        try:
            fd = os.open(json_out, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        except FileExistsError:
            raise Refused("--json target appeared during the run; nothing written")
        with os.fdopen(fd, "w", newline="\n") as f:
            for c in cells:
                for b in sorted(data[c]):
                    for arm in man["arms"]:
                        if b in D[c].get(arm, {}):
                            f.write(descriptor_json(c, b, arm, data[c][b][arm], D[c][arm][b], Y[c][arm][b]) + "\n")
        print("descriptors written: %s  SHA-256 %s" % (os.path.basename(json_out), sha256_file(json_out)), file=out)
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--manifest")
    ap.add_argument("--dir")
    ap.add_argument("--plan", choices=("test", "registered"))
    ap.add_argument("--json")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.manifest and a.dir and a.plan):
        ap.error("--manifest, --dir and --plan are required")
    with open(a.manifest) as f:
        man = json.load(f)
    print("contact tables script SHA-256 %s; manifest %s; plan %s" % (sha256_file(os.path.abspath(__file__)), sha256_file(a.manifest), a.plan))
    if a.plan == "test":
        print("*** TEST RECORDS: instrument validation only; no evidential value ***")
    try:
        return run(man, a.plan, os.path.abspath(a.dir), a.json)
    except Refused as ex:
        print("REFUSED: %s" % ex)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
