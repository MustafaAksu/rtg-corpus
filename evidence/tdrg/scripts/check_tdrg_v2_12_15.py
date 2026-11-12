#!/usr/bin/env python3
r"""Checker for Discrete Genesis (TDR-G) v2.12.15 (scientific scope edition).

usage: check_tdrg_v2_12_15.py BASE CANDIDATE EDITLOG_JSON [--root REPO] [--controls]
  BASE = `git show tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md`; CANDIDATE = dsn/RTG_DISCRETE_GENESIS_DSN.md;
  EDITLOG_JSON = evidence/tdrg/v2.12.15/edit_log.json. --root (default: cwd) must be the repository: C4 and C9 read
  tags and the collision reference commit. --controls runs the negative controls (each must be caught).

Gates (exit 0 iff all PASS):
 C0  BASE      base bytes are adopted v2.12.14 (3be72923...2392)
 C1  BUILD     the builder reproduces the candidate byte-exactly; log hashes and candidate hash agree
 C2  REVERSE   undoing the logged edits in reverse order recovers the base byte-exactly
 C3  HISTORY   Appendix A = base Appendix A with only the v2.12.15 entry inserted on top
 C4  RIDS      every TDRG-* identifier of the base survives; base declarations survive once; new declarations are
               exactly the builder's 9, once each, PREFIX-CATEGORY-DESCRIPTION form, absent from dsn/ noncanonical/
               atlas/ at the collision reference (main e8d317d) outside this DSN
 C5  TAGS      no compound grade reintroduced in live text (outside Appendix A and the alias sentence)
 C6  CONTENT   TDRG-DEF-STAR states "exactly one valid centre" and the inert rest, and the K_{1,3}-only wording is gone;
               SG-3, TDR-6 and Appendix B no longer give "gauge artifact"/"gauge-like" as the reason; TDR-6 is
               "ACTIVE — PARTIAL"; the LEM-SPECCONS conjecture sentence is replaced; the export row names
               TDR-24A → TDR-24B → TDR-24C; companion pins programme-v1.4 / ofn-v0.12 and no live Programme v1.3 /
               OFN v0.10 context pin
 C7  NUMBERS   every number of §6.13 and of the TDRG-DEF-STAR note equals the owner check output
               (evidence/tdrg/inbox_20261112/owner_token_law_check_v2_output.json), fixtures included
 C8  EVIDENCE  every hash prefix cited in edited text matches its file (tree or tag); every cited repository path
               exists
 C9  SOURCES   Finding A body identical at ofn-v0.10 and ofn-v0.12; AZ-ALG-ANTIPODAL-LOWORDER line identical at az-v0.6
               and az-v0.7; the AZ preregistration on this tree carries Propositions 1-3 and Corollaries 1.1-1.2; the
               five pipes items cited exist; programme-v1.4 tag exists
 C10 DYNAMICS  on the pinned engine (hash-checked) with the TDRG-DEF-ORIENT reference: census law, alphabet and
               birth injection on a random sample of all six policies (0 violations); fixture F1 (tailed tree is a
               single star); fixture F2 (equal spectra, different birth increments); no residual component class
               under the narrow band; negative control: an engine whose star map does not flip the centre must
               violate the census law
"""
import hashlib, importlib.util, json, os, random, re, subprocess, sys
from collections import Counter

sys.dont_write_bytecode = True
BASE_SHA = "3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392"
ENGINE = ("upload/tdrg-records/genesis_mode_b_mc_v18.py", "9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e")
ORIENT = "evidence/tdrg/scripts/tdrg_orient_v2_12_14.py"
OWNER_OUT = "evidence/tdrg/inbox_20261112/owner_token_law_check_v2_output.json"
COLLISION_REF = "e8d317d"
APPA, APPB = "## Appendix A — Version History {#appendix-a}\n\n", "## Appendix B"
ALIAS_SENTENCE = "Canonical tags follow `DSN_METHODOLOGY`"
COMPOUND = ["[ALG/NUM", "[ALG / NUM", "[ENG/ALG]", "[BRANCH/NUM", "[NUM / ", "[HEUR/NUM]", "[NUM strong / ALG",
            "[NUM-strong]", "[HEUR-strong]"]
HASHES = {   # prefix cited in edited text -> (path, where)
    "3be72923": ("dsn/RTG_DISCRETE_GENESIS_DSN.md", "tdrg-v2.12.14"),
    "3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392": ("dsn/RTG_DISCRETE_GENESIS_DSN.md", "tdrg-v2.12.14"),
    "198d2f4a": ("records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md", "tree"),
    "491cee3b": ("evidence/tdrg/inbox_20261112/owner_token_law_check_v2.py", "tree"),
    "acbc55db": (OWNER_OUT, "tree"),
}
ENDS = {"198d2f4a…fb829": "198d2f4a", "3be72923…2392": "3be72923"}
PIPES = ["pipes/TDRG/20261029-OFN-token-sum-gauge-label.md", "pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md"]


def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()
def git(root, *a): return subprocess.run(["git", "-C", root, *a], capture_output=True)
def show(root, ref, path):
    r = git(root, "show", f"{ref}:{path}"); return r.stdout if r.returncode == 0 else None
def load(path, name):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s)
    sys.modules[name] = m; s.loader.exec_module(m); return m
def live(t): return t[:t.index(APPA)] + t[t.index(APPB):]


def gates(root, base, cand, log, builder=None, engine_mutation=None, out=print):
    res = {}
    def g(k, ok, msg=""):
        res[k] = bool(ok); out(f"[{'PASS' if ok else 'FAIL'}] {k} {msg}")
    builder = builder or load(os.path.join(root, "evidence/tdrg/scripts/build_tdrg_v2_12_15.py"), "b1215")
    g("C0 BASE", sha(base) == BASE_SHA)
    try:
        text, rec = builder.build(base)
        ok = (text == cand and log["candidate_sha256"] == sha(cand) and log["edit_count"] == len(rec) == len(log["edits"])
              and all(a["key"] == b["key"] and a["old_sha256"] == b["old_sha256"] and a["new_sha256"] == b["new_sha256"]
                      for a, b in zip(rec, log["edits"]))
              and all(sha(e["old"]) == e["old_sha256"] and sha(e["new"]) == e["new_sha256"] for e in log["edits"]))
        g("C1 BUILD", ok, f"{len(rec)} edits, candidate {sha(cand)[:12]}")
    except AssertionError as ex:
        g("C1 BUILD", False, f"builder refused: {ex}")
    t, ok = cand, True
    for e in reversed(log["edits"]):
        if t.count(e["new"]) != 1: ok = False; break
        t = t.replace(e["new"], e["old"])
    g("C2 REVERSE", ok and t == base)
    ca = cand[cand.index(APPA):cand.index(APPB)]; ba = base[base.index(APPA):base.index(APPB)]
    tail = "### v2.12.14 — October 2026"
    j = ca.find(tail)
    g("C3 HISTORY", j >= 0 and ca.startswith(APPA + "### v2.12.15 — November 2026\n") and ca[j:] == ba[ba.index(tail):])
    ids = lambda s: set(re.findall(r"\bTDRG-[A-Z0-9][A-Z0-9-]*[A-Z0-9]\b", s))
    decl = lambda s: re.findall(r"\[RID: (TDRG-[A-Z0-9-]+)\]", s)
    bd, cd = decl(base), decl(cand)
    added = [r for r in cd if r not in bd]
    new = builder.NEW_RIDS
    form = all(re.fullmatch(r"TDRG-(DEF|THM|ALG|NUM|ART)-[A-Z0-9]+(-[A-Z0-9]+)*", r) for r in new)
    coll = []
    for f in git(root, "ls-tree", "-r", "--name-only", COLLISION_REF, "dsn", "noncanonical", "atlas").stdout.decode().split():
        if f == "dsn/RTG_DISCRETE_GENESIS_DSN.md": continue
        body = (show(root, COLLISION_REF, f) or b"").decode("utf-8", "replace")
        coll += [(r, f) for r in new if re.search(re.escape(r) + r"(?![A-Z0-9-])", body)]
    ok = (not (ids(base) - ids(cand)) and all(cd.count(r) == 1 for r in set(bd)) and sorted(added) == sorted(new)
          and len(added) == len(set(added)) and form and not coll)
    g("C4 RIDS", ok, f"new {len(added)}/{len(new)}; collisions {coll[:3]}")
    L = live(cand); i = L.index(ALIAS_SENTENCE); L2 = L[:i] + L[L.index("\n", i):]
    left = {c: L2.count(c) for c in COMPOUND if L2.count(c)}
    g("C5 TAGS", not left, f"compound left {left}")
    star = [l for l in cand.split("\n") if l.startswith("`[DEF]` [RID: TDRG-DEF-STAR]")]
    ok = (len(star) == 1 and "exactly one valid centre" in star[0] and "every other node of the component is inert" in star[0]
          and "($K_{1,3}$ with center $A$, leaves" not in cand
          and "— gauge artifact." not in L and "($P$ is gauge-like" not in L
          and "Status: ACTIVE — PARTIAL *(v2.12.15)*" in cand
          and "$n$-node signed-permutation invariance is conjectured" not in cand
          and "blocked by TDR-24A → TDR-24B → TDR-24C and TDR-T0" in cand and "blocked by TDR-24D/A/B" not in cand
          and "Programme Overview v1.4 (`programme-v1.4`)" in cand and "Ontological Foundations v0.12 (`ofn-v0.12`)" in cand
          and "Programme Overview v1.3 SG-PROG" not in L and "OFN v0.10 O0–O3" not in L)
    g("C6 CONTENT", ok)
    o = json.load(open(os.path.join(root, OWNER_OUT)))
    c, s, fx = o["counts"], o["star_shapes (campaign, fixtures excluded)"], o["fixtures"]
    nonpure = s["star with extra nodes, tree"] + s["star with extra nodes, contains a cycle"]
    single = nonpure + s["star pure K_1,3"] + s["star pure K_1,>=4"]
    fmt = lambda n: f"{n:,}"
    need = [f"{fmt(c['ticks'])} ticks", f"{fmt(c['birth_ticks'])} with births", f"{fmt(c['births'])} births",
            f"up to {c['max M_post on a checked birth tick']}", f"all {fmt(c['birth_free_ticks'])} birth-free ticks",
            f"{fmt(c['P2 phase checked (provenance-exact)'])} parent–child advances",
            f"{fmt(single)}, of which pure $K_{{1,3}}$ {fmt(s['star pure K_1,3'])}",
            f"$m\\ge4$ {fmt(s['star pure K_1,>=4'])}", f"not pure {fmt(nonpure)}",
            f"trees {fmt(s['star with extra nodes, tree'])}", f"containing a cycle {fmt(s['star with extra nodes, contains a cycle'])}",
            f"{fmt(nonpure)} of {fmt(single)} single-star events",
            "D(C')=\\{1,1,2,2,3,4\\}$", "adds $\\{2,4,5,6\\}$", "$\\{4,6,7,8\\}$"]
    ev = (not o["violations"] and fx["F1 tailed tree blown up as single star (centre 0)"] and fx["F2 D(C) == D(C')"]
          and fx["F2 increments differ"] and fx["F2 D(C)"] == [1, 1, 2, 2, 3, 4]
          and fx["F2 birth increment C"] == [2, 4, 5, 6] and fx["F2 birth increment C'"] == [4, 6, 7, 8]
          and c["P1 census checked"] == c["ticks"] == c["birth_ticks"] + c["birth_free_ticks"]
          and c["Cor1.1 injection checked (birth ticks)"] == c["birth_ticks"]
          and c["Cor1.2 conservation checked (birth-free ticks)"] == c["birth_free_ticks"])
    miss = [x for x in need if x not in cand]
    g("C7 NUMBERS", ev and not miss, f"missing {miss}")
    et = "\n".join(e["new"] for e in log["edits"])
    bad = [h for h in set(re.findall(r"`([0-9a-f]{8})(?:…|[0-9a-f]{56}`)", et)) if h not in HASHES]
    for pre, (path, where) in HASHES.items():
        if pre not in et: continue
        d = open(os.path.join(root, path), "rb").read() if where == "tree" else show(root, where, path)
        if d is None or not sha(d).startswith(pre): bad.append((pre, path))
    for short, pre in ENDS.items():
        if short in et:
            path, where = HASHES[pre]
            d = open(os.path.join(root, path), "rb").read() if where == "tree" else show(root, where, path)
            if not sha(d).endswith(short.split("…")[1]): bad.append((short, path))
    paths = set(re.findall(r"`((?:evidence|records|upload|pipes|dsn)/[A-Za-z0-9_./-]+)`", et))
    nopath = sorted(p for p in paths if not os.path.exists(os.path.join(root, p)) and not p.endswith("_RELEASE_RECORD.md"))
    rr = os.path.exists(os.path.join(root, "records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md"))
    g("C8 EVIDENCE", not bad and not nopath and rr, f"hash issues {bad}; missing paths {nopath}; release record {rr}")
    fa = lambda tag: sha(re.sub(r"^.*?\*\*Finding A", "**Finding A", [l for l in (show(root, tag, "dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md") or b"").decode().splitlines() if "RID: RTG-OFN-ALG-STAR-TOKEN-SHIFT]" in l][0]))
    az = lambda tag: [l for l in (show(root, tag, "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md") or b"").decode().splitlines() if "(1) There is no closed non-backtracking walk of length 2 or 3" in l]
    pr = open(os.path.join(root, "records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md"), encoding="utf-8").read()
    tags = git(root, "tag", "-l").stdout.decode().split()
    ok = (fa("ofn-v0.10") == fa("ofn-v0.12") and az("az-v0.6") == az("az-v0.7") and len(az("az-v0.7")) == 1
          and all(x in pr for x in ("**Proposition 1", "**Corollary 1.1", "**Corollary 1.2", "**Proposition 2", "**Proposition 3"))
          and all(os.path.exists(os.path.join(root, p)) for p in PIPES) and "programme-v1.4" in tags)
    g("C9 SOURCES", ok)
    g("C10 DYNAMICS", dynamics(root, out, engine_mutation))
    return res


def dynamics(root, out, mutation=None):
    ep = os.path.join(root, ENGINE[0])
    if sha(open(ep, "rb").read()) != ENGINE[1]: out("  engine hash mismatch"); return False
    eng = load(ep, "tdrg_eng_1215"); ref = load(os.path.join(root, ORIENT), "tdrg_orient_1215")
    eng.orient_path = ref.make_orient(eng)
    if mutation: mutation(eng)
    cls = Counter(); o = eng.classify_component
    def spy(comp, adj):
        t, c = o(comp, adj); cls[t.split("_")[0]] += 1; return t, c
    eng.classify_component = spy
    cd = lambda a, b, N: min((a - b) % N, (b - a) % N)
    D = lambda ts, N: Counter(cd(ts[i], ts[j], N) for i in range(len(ts)) for j in range(i + 1, len(ts)))
    rng = random.Random(15); viol = 0; ticks = 0
    for pol in ["trap", "bound_multistar", "bound_path_tie", "bound_symmetric", "largest_center", "all_centers"]:
        for N, k in ((24, 1), (60, 4), (120, 8)):
            for _ in range(4):
                u = eng.Universe(N=N, k=k, theta={i: rng.randrange(N) for i in range(4)}, delta={i: rng.randrange(N) for i in range(4)})
                S0 = set(u.delta.values()) | {(-x) % N for x in u.delta.values()}
                for _t in range(200):
                    if len(u.theta) >= 50: break
                    pre = set(u.theta); C = list(u.delta.values()); eng.step_universe(u, multistar_policy=pol); ticks += 1
                    xs = [u.delta[i] for i in u.theta if i not in pre]
                    viol += Counter(u.delta.values()) != Counter(C) + Counter((-x) % N for x in xs)
                    viol += not set(u.delta.values()) <= S0
                    De = D(C, N)
                    for a, x in enumerate(xs):
                        for y in C: De[cd((-x) % N, y, N)] += 1
                        for b in range(a + 1, len(xs)): De[cd(x, xs[b], N)] += 1
                    viol += D(list(u.delta.values()), N) != De
    residual = {k: v for k, v in cls.items() if k in ("ambiguous", "triangle")}
    u = eng.Universe(N=24, k=1, theta={0: 0, 1: 11, 2: 12, 3: 13, 4: 22}, delta={i: 0 for i in range(5)})
    eng.step_universe(u, multistar_policy="bound_symmetric"); f1 = len(u.theta) == 6
    def realise(C):
        post = {0: 0, 1: 11, 2: 12, 3: 13}
        u = eng.Universe(N=24, k=1, theta={i: (post[i] - C[i]) % 24 for i in range(4)}, delta={i: C[i] for i in range(4)})
        d0 = D(C, 24); eng.step_universe(u, multistar_policy="bound_symmetric")
        return d0, sorted((D(list(u.delta.values()), 24) - d0).elements())
    a, b = realise([1, 3, 4, 5]), realise([2, 4, 5, 6])
    f2 = a[0] == b[0] and a[1] == [2, 4, 5, 6] and b[1] == [4, 6, 7, 8]
    out(f"  sample: {ticks} ticks, violations {viol}; residual classes {residual}; F1 {f1}; F2 {f2}")
    return viol == 0 and not residual and f1 and f2


def controls(root, base, cand, log, out=print):
    quiet = lambda *a, **k: None
    builder = load(os.path.join(root, "evidence/tdrg/scripts/build_tdrg_v2_12_15.py"), "b1215")
    star = [l for l in cand.split("\n") if l.startswith("`[DEF]` [RID: TDRG-DEF-STAR]")][0]
    old_star = [l for l in base.split("\n") if l.startswith("`[DEF]` [RID: TDRG-DEF-STAR]")][0]
    muts = {
        "K1 K_{1,3}-only star text restored": cand.replace(star, old_star),
        "K2 'gauge artifact' restored in TDR-6": cand.replace(builder.TDR6_P_NEW, builder.TDR6_P_OLD),
        "K3 unlogged change": cand.replace("**Free parent–child phase law", "**Free parent-child phase law", 1),
        "K5 one new RID declaration dropped": cand.replace("[RID: TDRG-ALG-SPECCONS-N] ", "", 1),
        "K6 Appendix A history edited": cand.replace("### v2.12.14 — October 2026\n", "### v2.12.14 — Oct 2026\n", 1),
    }
    caught = {}
    for name, m in muts.items():
        assert m != cand, name
        r = gates(root, base, m, log, out=quiet)
        caught[name] = not all(r.values())
        out(f"[{'CAUGHT' if caught[name] else 'MISSED'}] {name}: failing {[k for k, v in r.items() if not v]}")
    # K4: a consistent but wrong number (log and builder agree with the mutated text): only C7 can catch it
    m = cand.replace("765,224 parent–child advances", "765,225 parent–child advances")
    mlog = json.loads(json.dumps(log))
    for e in mlog["edits"]:
        e["new"] = e["new"].replace("765,224 parent–child", "765,225 parent–child"); e["new_sha256"] = sha(e["new"])
    mlog["candidate_sha256"] = sha(m)
    class B:
        NEW_RIDS = builder.NEW_RIDS; TDR6_P_NEW = builder.TDR6_P_NEW
        @staticmethod
        def build(b): return m, mlog["edits"]
    r = gates(root, base, m, mlog, builder=B, out=quiet)
    caught["K4 wrong number, consistent log"] = not r["C7 NUMBERS"]
    out(f"[{'CAUGHT' if not r['C7 NUMBERS'] else 'MISSED'}] K4 wrong number, consistent log: failing {[k for k, v in r.items() if not v]}")
    # K7: engine whose star map leaves the centre unflipped must fail C10
    def no_flip(eng):
        orig = eng.blow_up_star_with_snapshot
        def f(u, center, tp, dp, nid):
            r = orig(u, center, tp, dp, nid); u.delta[center] = dp[center]; return r
        eng.blow_up_star_with_snapshot = f
    ok = dynamics(root, quiet, no_flip)
    caught["K7 star map without centre flip"] = not ok
    out(f"[{'CAUGHT' if not ok else 'MISSED'}] K7 star map without centre flip: C10 {'FAIL' if not ok else 'PASS'}")
    return all(caught.values())


def main(argv):
    root = argv[argv.index("--root") + 1] if "--root" in argv else os.getcwd()
    args = [a for a in argv[1:] if not a.startswith("--") and a != root]
    base = open(args[0], "rb").read().decode("utf-8"); cand = open(args[1], "rb").read().decode("utf-8")
    log = json.load(open(args[2], encoding="utf-8"))
    if "--controls" in argv:
        ok = controls(root, base, cand, log); print("CONTROLS:", "PASS (all caught)" if ok else "FAIL")
    else:
        res = gates(root, base, cand, log); ok = all(res.values())
        print("RESULT:", "PASS" if ok else "FAIL", f"({sum(res.values())}/{len(res)} gates)")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main(sys.argv)
