#!/usr/bin/env python3
r"""Checker for Discrete Genesis (TDR-G) v2.12.14 (corrections-only candidate).

usage: check_tdrg_v2_12_14.py BASE CANDIDATE EDITLOG_JSON [--root REPO] [--controls] [--exhaustive]
  BASE = `git show tdrg-v2.12.13:dsn/RTG_DISCRETE_GENESIS_DSN.md`; CANDIDATE = dsn/RTG_DISCRETE_GENESIS_DSN.md on the
  build branch; EDITLOG_JSON = evidence/tdrg/v2.12.14/edit_log.json. --root defaults to the current directory and must
  be the repository (C8-C10 read tags, branches and files). --controls runs the negative controls instead of the gates
  (every control must be caught). --exhaustive adds the full three-node k=1 equivariance census to C10 (~2 min).

Gates (exit 0 iff all PASS):
 C0  BASE         base bytes are adopted v2.12.13 (aa232643...053f)
 C1  BUILD        the builder reproduces the candidate byte-exactly; log hashes, edit count and candidate hash agree
 C2  REVERSE      undoing the logged edits in reverse order recovers the base byte-exactly (no unlogged change)
 C3  HISTORY      Appendix A of the candidate equals that of the base with only the v2.12.14 entry inserted on top
 C4  RIDS         every TDRG-* identifier of the base survives; every base [RID:] declaration survives once; the new
                  declarations are exactly the 39 declared RIDs, once each, in PREFIX-CATEGORY-DESCRIPTION form; none
                  occurs in dsn/, noncanonical/ or atlas/ at the collision reference (main ed5f85b) — consumer names
                  (TDRG-ORIENT, TDRG-ZN-STATE, ...) are aliases in the owner map, not declarations; every RID-only edit
                  (group TB09) inserts exactly one "[RID: X] " and nothing else
 C5  TAGS         no compound grade (`[ALG/NUM]`, `[ALG / NUM ...]`, `[ENG/ALG]`, `[BRANCH/NUM...]`, `[NUM / ...]`,
                  `[HEUR/NUM]`, `[NUM strong / ALG exact]`) remains outside Appendix A except in the one sentence that
                  names the retired aliases; no bare `[RESULT]` without `[from: ...]` in live text; tag census reported
 C6  ORIENT       the orientation DEF states the extended tie (2E = 0 mod N, E in {0, N/2}) and the open-interval
                  forward/reverse clauses; the v2.12.13 clause "If $S = E = 0$" is gone; signed_centered is defined on
                  (-N/2, N/2]; SG-14 names Sym(V) x Z_N^phase and excludes the token shift and the mirror; the
                  largest_center exception, the Appendix B row and the G-alternative (recorded, not adopted) are present
 C7  NUMBERS      every number of the v2.12.14 orientation statements equals its evidence file: owner equivariance JSON
                  (72/72, 168/168, 112, zeros), atlas JSON (40 exposed; 10/20/12; census 9,800/77/16,322/331,776;
                  inert 9,789/66), mirror output (2,661 of 2,703), multistar output, antipodal fixture text
 C8  EVIDENCE     every hash prefix cited in edited text matches its file (on this tree, or for the session scripts on
                  origin/upload/tdrg-session-scripts at 386e9d4); every repository path cited in edited text exists
                  (on this tree, or until merged on the PR #91 / upload branches)
 C9  SOURCES      the cited tags exist (programme-v1.2/1.3, ofn-v0.10, methodology-v1.4, az-v0.6, triad-v1.6.1,
                  numgen-v1.21); the cited facts are at those tags (RTG-OFN-ALG-STAR-TOKEN-SHIFT and 2c=0 in OFN;
                  AZ-ALG-ANTIPODAL-LOWORDER and Lk<N/2 in AZ; CN-05, 96:1 and the x_* root in TRIAD; "the antipodal
                  path tie" in Programme v1.2)
 C10 DYNAMICS     on the pinned engine (hash-checked) with the reference implementation tdrg_orient_v2_12_14.py:
                  antipodal fixture — v18 NOT equivariant (negative control), v2.12.14 equivariant and a tie;
                  K_{2,3} fixture — largest_center NOT equivariant (negative control), bound_symmetric equivariant;
                  mirror probe (2,000 states) — failures > 0 (negative control); 3,000 random three-node states at
                  k in {1,2,3} — v2.12.14 equivariant under both S_3 generators; reference function equals the owner
                  check's tie_b rule on every sampled path; with --exhaustive the k=1 census reproduces 72/72 and 0/0
"""
import hashlib, importlib.util, json, os, random, re, subprocess, sys

sys.dont_write_bytecode = True
BASE_SHA = "aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f"
ENGINE_V18 = ("upload/tdrg-records/genesis_mode_b_mc_v18.py",
              "9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e")
COLLISION_REF = "ed5f85b367d8390b08aa8241abbc220548e52110"
SESSION_REF = "origin/upload/tdrg-session-scripts"
SESSION_COMMIT = "386e9d44f1f819d89b5b0e0ce4f6cb18c6e08c8b"
PENDING_REFS = ["origin/claude/tdrg-disposition-reconciliation", SESSION_REF]
APPA, APPB = "## Appendix A — Version History {#appendix-a}\n\n", "## Appendix B"
ALIAS_SENTENCE_START = "Canonical tags follow `DSN_METHODOLOGY`"
COMPOUND = ["[ALG/NUM", "[ALG / NUM", "[ENG/ALG]", "[BRANCH/NUM", "[NUM / ", "[HEUR/NUM]", "[NUM strong / ALG",
            "[NUM-strong]", "[HEUR-strong]"]
TAGS = ["[DEF]", "[THM]", "[ALG]", "[ALG structure]", "[ALG candidate]", "[ENG]", "[NUM]", "[NUM strong]", "[HEUR]",
        "[HEUR strong]", "[OPEN]", "[FAIL]", "[COR]", "[RESULT]", "[INTERP]"]
# hash prefixes cited in edited text -> (path, where): where = "tree" or a git ref
HASHES = {
    "aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f": ("dsn/RTG_DISCRETE_GENESIS_DSN.md", "tdrg-v2.12.13"),
    "aa232643": ("dsn/RTG_DISCRETE_GENESIS_DSN.md", "tdrg-v2.12.13"),
    "4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608": ("upload/tdrg-records/genesis_mode_b_mc.py", "tree"),
    "4c94d874": ("upload/tdrg-records/genesis_mode_b_mc.py", "tree"),
    "9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e": (ENGINE_V18[0], "tree"),
    "9d787b43": (ENGINE_V18[0], "tree"),
    "de0f3e42": ("upload/tdrg-records/motif_TEST_N120_k8_T1200_b3_v17.csv", "tree"),
    "7ef343b0": ("upload/tdrg-records/motif_N120_k08_T5000_b20_v17.csv", "tree"),
    "3ebf064d": ("upload/tdrg-records/tdr_motif_bootstrap_v6.py", "tree"),
    "86e77511": ("upload/tdrg-records/tdr_motif_bootstrap_v4.py", "tree"),
    "ba99e307": ("upload/tdrg-records/genesis_mode_b_mc_telemetry.py", "tree"),
    "fe3928a4": ("evidence/tdrg/disposition/multistar_fixture_output.txt", "tree"),
    "c47d78b9": ("evidence/tdrg/disposition/antipodal_fixture.txt", "tree"),
    "2f54e0fc": ("evidence/tdrg/disposition/owner_relabel_equivariance_check.py", "tree"),
    "a0b33690": ("evidence/tdrg/disposition/owner_relabel_equivariance_check_output.txt", "tree"),
    "9f8bdf59": ("evidence/tdrg/disposition/mirror_probe_output.txt", "tree"),
    "5684da96": ("evidence/atlas/tdrg/atlas_tdrg_orientation_covariance_check.py", "tree"),
    "2d15b12f": ("evidence/atlas/tdrg/atlas_tdrg_orientation_covariance_check.json", "tree"),
}
SHORT_ENDS = {"4c94d874…a608": "4c94d874", "9d787b43…675e": "9d787b43", "aa232643…053f": "aa232643"}


def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()
def git(root, *a): return subprocess.run(["git", "-C", root, *a], capture_output=True)
def show(root, ref, path):
    r = git(root, "show", f"{ref}:{path}")
    return r.stdout if r.returncode == 0 else None


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m)
    return m


def appa(t):
    i = t.index(APPA); j = t.index(APPB)
    return t[i:j]


def live(t):
    return t[:t.index(APPA)] + t[t.index(APPB):]


def edited_text(log):
    return "\n".join(e["new"] for e in log["edits"])


# ------------------------------------------------------------------------------------------------- gates
def gates(root, base, cand, log, exhaustive=False, builder=None, out=print):
    res = {}
    def g(k, ok, msg=""):
        res[k] = bool(ok); out(f"[{'PASS' if ok else 'FAIL'}] {k} {msg}")
    builder = builder or load(os.path.join(root, "evidence/tdrg/scripts/build_tdrg_v2_12_14.py"), "tdrg_builder")
    g("C0 BASE", sha(base) == BASE_SHA)
    try:
        text, rec = builder.build(base)
        ok = (text == cand and log["candidate_sha256"] == sha(cand) and log["edit_count"] == len(rec) == len(log["edits"])
              and all(a["old_sha256"] == b["old_sha256"] and a["new_sha256"] == b["new_sha256"] and a["key"] == b["key"]
                      for a, b in zip(rec, log["edits"]))
              and all(sha(e["old"]) == e["old_sha256"] and sha(e["new"]) == e["new_sha256"] for e in log["edits"]))
        g("C1 BUILD", ok, f"{len(rec)} edits, candidate {sha(cand)[:12]}")
    except AssertionError as ex:
        g("C1 BUILD", False, f"builder refused: {ex}")
    t = cand; ok = True
    for e in reversed(log["edits"]):
        if t.count(e["new"]) != 1: ok = False; break
        t = t.replace(e["new"], e["old"])
    g("C2 REVERSE", ok and t == base)
    entry_end = "### v2.12 — June 2026"
    ca, ba = appa(cand), appa(base)
    ok = ca.startswith(APPA + "### v2.12.14 — October 2026\n") and ca[ca.index(entry_end):] == ba[ba.index(entry_end):]
    g("C3 HISTORY", ok)
    # C4
    ids = lambda s: set(re.findall(r"\bTDRG-[A-Z0-9][A-Z0-9-]*[A-Z0-9]\b", s))
    decl = lambda s: re.findall(r"\[RID: (TDRG-[A-Z0-9-]+)\]", s)
    new_rids = builder.NEW_RIDS
    base_decl, cand_decl = decl(base), decl(cand)
    lost = ids(base) - ids(cand)
    added = [r for r in cand_decl if r not in base_decl]
    form = all(re.fullmatch(r"TDRG-(DEF|THM|ALG|NUM|ART)-[A-Z0-9]+(-[A-Z0-9]+)*", r) for r in new_rids)
    base_kept = all(cand_decl.count(r) == base_decl.count(r) == 1 for r in set(base_decl))
    coll = []
    files = git(root, "ls-tree", "-r", "--name-only", COLLISION_REF, "dsn", "noncanonical", "atlas").stdout.decode().split()
    for f in files:
        if f == "dsn/RTG_DISCRETE_GENESIS_DSN.md": continue
        body = (show(root, COLLISION_REF, f) or b"").decode("utf-8", "replace")
        coll += [(r, f) for r in new_rids if re.search(re.escape(r) + r"(?![A-Z0-9-])", body)]
    rid_only = True
    for e in log["edits"]:
        if e["group"] != "TB09" or e["key"] == "E82": continue   # E82 also re-tags BIND3-CYCLE (TB12), checked in C5
        m = re.findall(r"\[RID: [A-Z0-9-]+\] | \[RID: [A-Z0-9-]+\]$", e["new"])   # "[RID: X] " before, or " [RID: X]" after
        rid_only &= len(m) == 1 and e["new"].replace(m[0], "", 1) == e["old"]
    ok = (not lost and sorted(added) == sorted(new_rids) and len(added) == len(set(added)) and form and base_kept
          and not coll and rid_only)
    g("C4 RIDS", ok, f"base ids kept: {not lost}; new declarations {len(added)}/{len(new_rids)}; form {form}; "
                     f"collisions {coll[:3]}; RID-only edits clean {rid_only}")
    # C5
    L = live(cand)
    i = L.index(ALIAS_SENTENCE_START); L2 = L[:i] + L[L.index("\n", i):]
    left = {c: L2.count(c) for c in COMPOUND if L2.count(c)}
    bare = [m.start() for m in re.finditer(r"`\[RESULT\]`(?! `\[from:)", L)]
    census = {k: (live(base).count(k), L.count(k)) for k in TAGS}
    g("C5 TAGS", not left and not bare, f"compound left {left}; bare RESULT {len(bare)}; census (base→cand) "
      + ", ".join(f"{k} {a}→{b}" for k, (a, b) in census.items() if a != b))
    # C6
    i = cand.find("[RID: TDRG-DEF-ORIENT]")
    od = cand[i:cand.index("\n", i)] if i >= 0 else ""
    need =["2E\\equiv0 \\pmod N", "E\\in\\{0,\\,N/2\\}", "forward if $0<E<N/2$", "reversed if $-N/2<E<0$",
            "**balanced path-tie**", "tdrg_orient_v2_12_14.py"]
    sg = cand[cand.index("**[SG-14]**"):]; sg = sg[:sg.index("Violation:")]
    ok = (all(n in od for n in need) and "If $S = E = 0$" not in cand
          and "in the half-open interval $(-N/2,\\,N/2]$" in cand
          and "\\mathrm{Sym}(V)\\times\\mathbb{Z}_N^{\\rm phase}" in sg and "common token shift" in sg
          and "the mirror" in sg and "TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK" in sg
          and "Path-orientation completion by node-ID listing" in cand
          and "**Recorded alternative (not adopted):**" in cand)
    g("C6 ORIENT", ok)
    # C7
    oj = json.load(open(os.path.join(root, "evidence/tdrg/disposition/owner_relabel_equivariance_check.json")))
    aj = json.load(open(os.path.join(root, "evidence/atlas/tdrg/atlas_tdrg_orientation_covariance_check.json")))
    mo = open(os.path.join(root, "evidence/tdrg/disposition/mirror_probe_output.txt")).read()
    mf = open(os.path.join(root, "evidence/tdrg/disposition/multistar_fixture_output.txt")).read()
    af = open(os.path.join(root, "evidence/tdrg/disposition/antipodal_fixture.txt")).read()
    ev = (oj["n3_v18_k1"]["fail_gen01"] == oj["n3_v18_k1"]["fail_gen12"] == 72
          and oj["n3_v18_k3"]["fail_gen01"] == oj["n3_v18_k3"]["fail_gen12"] == 168
          and all(oj[f"n3_{v}_k{k}"][f] == 0 for v in ("tie_b", "G_a") for k in (1, 3) for f in ("fail_gen01", "fail_gen12"))
          and all(oj[k]["phase_shift_fail_sampled"] == 0 for k in oj if k.startswith("n3_"))
          and oj["n4_v18_bound_symmetric"]["fail"] == 112 and oj["n4_tie_b_bound_symmetric"]["fail"] == 0
          and oj["n4_G_a_bound_symmetric"]["fail"] == 0 and oj["n4_tie_b_largest_center"]["fail"] == 0
          and aj["exposed_witnesses"] == 40 and aj["ratified_witnesses"] == 136
          and (aj["changes_reverse"], aj["changes_inert"], aj["changes_covariant-G"]) == (10, 20, 12)
          and aj["labels_identical_inert"] and aj["labels_without_unexposed_witness"] == []
          and aj["census_k1_v18"]["cycles"] == 9800 and aj["census_k1_v18"]["cycles_with_degenerate_event"] == 77
          and aj["census_k1_v18"]["states_whose_cycle_has_degenerate_event"] == 16322
          and aj["census_k1_v18"]["states"] == 331776
          and aj["census_k1_inert"]["cycles"] == 9789 and aj["census_k1_inert"]["cycles_with_degenerate_event"] == 66
          and "step-equivariance failures 2661; states with a P3 event 2703" in mo
          and "largest_center births 1 centre tokens after 23 2 | swap centres (0 1) equivariant: False" in mf
          and "bound_symmetric births 0 centre tokens after 1 2 | swap centres (0 1) equivariant: True" in mf
          and "v18    delta after [1, 12, 0]  path ties 0  equivariant under (0 2): False" in af
          and "tie_b  delta after [0, 1, 12]  path ties 1  equivariant under (0 2): True" in af
          and "G_a    delta after [12, 0, 1]  path ties 0  equivariant under (0 2): True" in af)
    txt = ["72 / 72 at $k=1$ and 168 / 168 at $k=3$", "v18 112 failures", "77 of 9,800 eventual cycles",
           "16,322 of 331,776 states (4.9 %)", "9,789", "66 of which", "**20 of 136**", "reverse completion 10",
           "G-alternative 12", "2,661 failures among the 2,703 states", "$\\delta'=(1,12,0)$", "$\\delta'=(12,0,1)$",
           "DISC-2 effect 20 of 136 records"]
    missing = [x for x in txt if x not in cand]
    g("C7 NUMBERS", ev and not missing and abs(16322 / 331776 - 0.049) < 0.0005, f"text missing {missing}")
    # C8
    et = edited_text(log)
    bad = []
    unknown = [h for h in set(re.findall(r"`([0-9a-f]{8})(?:…|[0-9a-f]{56}`)", et)) if h not in HASHES]
    bad += [(h, "not in the checker's hash map") for h in unknown]
    for pre, (path, where) in HASHES.items():
        if pre not in et:
            continue
        data = open(os.path.join(root, path), "rb").read() if where == "tree" else show(root, where, path)
        if data is None or not sha(data).startswith(pre): bad.append((pre, path))
    for short, pre in SHORT_ENDS.items():
        if short in et:
            path, where = HASHES[pre]
            data = open(os.path.join(root, path), "rb").read() if where == "tree" else show(root, where, path)
            if not sha(data).endswith(short.split("…")[1]): bad.append((short, path))
    # session-scripts hashes on the upload branch
    sums = show(root, SESSION_REF, "upload/tdrg-session-scripts/SHA256SUMS.txt")
    sess_ok = sums is not None and git(root, "rev-parse", SESSION_REF).stdout.decode().strip() == SESSION_COMMIT
    if sess_ok:
        for line in sums.decode().splitlines():
            h, p = line.split(None, 1); p = p.strip().lstrip("./")
            d = show(root, SESSION_REF, "upload/tdrg-session-scripts/" + p)
            sess_ok &= d is not None and sha(d) == h
    paths = set(re.findall(r"`((?:evidence|records|upload|pipes|dsn)/[A-Za-z0-9_./-]+)`", et))
    nopath = []
    for p in sorted(paths):
        if os.path.exists(os.path.join(root, p)): continue
        if any(show(root, r, p) is not None for r in PENDING_REFS): continue
        nopath.append(p)
    g("C8 EVIDENCE", not bad and sess_ok and not nopath,
      f"hash mismatches {bad}; session-scripts branch ok {sess_ok}; missing paths {nopath}")
    # C9
    tags = git(root, "tag", "-l").stdout.decode().split()
    need_tags = ["programme-v1.2", "programme-v1.3", "ofn-v0.10", "methodology-v1.4", "az-v0.6", "triad-v1.6.1",
                 "numgen-v1.21", "tdrg-v2.12.13"]
    ofn = (show(root, "ofn-v0.10", "dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md") or b"").decode()
    az = (show(root, "az-v0.6", "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md") or b"").decode()
    tri = (show(root, "triad-v1.6.1", "dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md") or b"").decode()
    p12 = (show(root, "programme-v1.2", "dsn/RTG_PROGRAMME_OVERVIEW.md") or b"").decode()
    azline = [l for l in az.splitlines() if "AZ-ALG-ANTIPODAL-LOWORDER" in l]
    ok = (all(x in tags for x in need_tags) and "RTG-OFN-ALG-STAR-TOKEN-SHIFT" in ofn and "$2c=0$" in ofn
          and "XFER-O08-01" in ofn and "REQ-O09-05" in ofn and azline and "Lk<N/2" in azline[0]
          and "length 2 or 3" in azline[0] and "CN-05" in tri and "96:1" in tri and "x_*" in tri
          and "the antipodal path tie" in p12)
    g("C9 SOURCES", ok)
    # C10
    g("C10 DYNAMICS", dynamics(root, exhaustive, out))
    return res


def dynamics(root, exhaustive, out, orient_factory=None):
    ep = os.path.join(root, ENGINE_V18[0])
    if sha(open(ep, "rb").read()) != ENGINE_V18[1]:
        out("  engine hash mismatch"); return False
    eng = load(ep, "tdrg_engine_v18")
    ref = load(os.path.join(root, "evidence/tdrg/scripts/tdrg_orient_v2_12_14.py"), "tdrg_orient_ref")
    V18 = eng.orient_path
    NEW = (orient_factory or ref.make_orient)(eng)

    def run(th, dl, N, k, pol, fn):
        eng.orient_path = fn
        u = eng.Universe(N=N, k=k, theta=dict(th), delta=dict(dl)); eng.step_universe(u, multistar_policy=pol); return u

    def canon(u, perm, n0):
        return (tuple(sorted((perm[i], u.theta[i], u.delta[i]) for i in range(n0))),
                tuple(sorted((u.theta[i], u.delta[i]) for i in u.theta if i >= n0)))

    def equiv(th, dl, N, k, pol, perm, fn):
        n0 = len(th)
        a = canon(run(th, dl, N, k, pol, fn), perm, n0)
        b = canon(run({perm[i]: th[i] for i in range(n0)}, {perm[i]: dl[i] for i in range(n0)}, N, k, pol, fn),
                  list(range(n0)), n0)
        return a == b

    ok = True
    th, dl = {0: 0, 1: 11, 2: 12}, {0: 0, 1: 1, 2: 12}
    v18_fix = equiv(th, dl, 24, 1, "bound_symmetric", (2, 1, 0), V18)
    u = run(th, dl, 24, 1, "bound_symmetric", NEW)
    new_fix = equiv(th, dl, 24, 1, "bound_symmetric", (2, 1, 0), NEW) and u.path_ties_seen == 1 \
        and [u.delta[i] for i in range(3)] == [0, 1, 12]
    out(f"  antipodal fixture: v18 equivariant={v18_fix} (control expects False); v2.12.14 equivariant+tie={new_fix}")
    ok &= (not v18_fix) and new_fix
    post = {0: 0, 1: 0, 2: 12, 3: 12, 4: 12}; dl5 = {0: 1, 1: 2, 2: 0, 3: 0, 4: 0}
    pre = {i: (post[i] - dl5[i]) % 24 for i in post}
    lc = equiv(pre, dl5, 24, 1, "largest_center", (1, 0, 2, 3, 4), NEW)
    bs = equiv(pre, dl5, 24, 1, "bound_symmetric", (1, 0, 2, 3, 4), NEW)
    out(f"  K23 fixture: largest_center equivariant={lc} (control expects False); bound_symmetric equivariant={bs}")
    ok &= (not lc) and bs
    rng = random.Random(20261028); mf = 0
    for _ in range(2000):
        a = {i: rng.randrange(24) for i in range(3)}; d = {i: rng.randrange(24) for i in range(3)}
        u0 = run(a, d, 24, 1, "bound_symmetric", NEW)
        u1 = run({i: (-x) % 24 for i, x in a.items()}, {i: (-x) % 24 for i, x in d.items()}, 24, 1, "bound_symmetric", NEW)
        mf += any(u1.theta[i] != (-u0.theta[i]) % 24 or u1.delta[i] != (-u0.delta[i]) % 24 for i in range(3))
    out(f"  mirror probe: {mf} failures in 2000 states (control expects > 0)")
    ok &= mf > 0
    # reference rule == owner check's tie_b on sampled paths; equivariance on random states
    fails = 0; disagree = 0; paths = 0
    for _ in range(3000):
        k = rng.choice((1, 2, 3))
        a = {0: 0, 1: rng.randrange(24), 2: rng.randrange(24)}; d = {0: 0, 1: rng.randrange(24), 2: rng.randrange(24)}
        for gperm in ((1, 0, 2), (0, 2, 1)):
            fails += not equiv(a, d, 24, k, "bound_symmetric", gperm, NEW)
        for p in ([0, 1, 2], [1, 0, 2], [0, 2, 1]):
            class U: orientation_ties = 0; path_ties_seen = 0
            th2 = {i: rng.randrange(24) for i in range(3)}; dd = {i: rng.randrange(24) for i in range(3)}
            r1 = NEW(p, th2, dd, 24, U())
            s = sum(eng.signed_defect_error(th2[p[i]], th2[p[i + 1]], 24) for i in range(2))
            e = eng.signed_centered(dd[p[-1]] - dd[p[0]], 24)
            r2 = p if s > 0 else p[::-1] if s < 0 else p if 0 < e < 12 else p[::-1] if e < 0 else None
            disagree += r1 != r2; paths += 1
    out(f"  random three-node states: v2.12.14 equivariance failures {fails} (expect 0); rule disagreements "
        f"{disagree}/{paths} (expect 0)")
    ok &= fails == 0 and disagree == 0
    if exhaustive:
        import itertools
        f18 = [0, 0]; fnew = [0, 0]
        for t1, t2, d1, d2 in itertools.product(range(24), repeat=4):
            a = {0: 0, 1: t1, 2: t2}; d = {0: 0, 1: d1, 2: d2}
            for j, gp in enumerate(((1, 0, 2), (0, 2, 1))):
                f18[j] += not equiv(a, d, 24, 1, "bound_symmetric", gp, V18)
                fnew[j] += not equiv(a, d, 24, 1, "bound_symmetric", gp, NEW)
        out(f"  exhaustive k=1: v18 {f18} (expect [72, 72]); v2.12.14 {fnew} (expect [0, 0])")
        ok &= f18 == [72, 72] and fnew == [0, 0]
    eng.orient_path = V18
    return ok


# ---------------------------------------------------------------------------------------------- controls
def controls(root, base, cand, log, out=print):
    quiet = lambda *a, **k: None
    builder = load(os.path.join(root, "evidence/tdrg/scripts/build_tdrg_v2_12_14.py"), "tdrg_builder")
    caught = {}
    orient_line = [l for l in cand.split("\n") if l.startswith("`[DEF]` [RID: TDRG-DEF-ORIENT]")][0]
    old_rule = ("`[DEF]` **Path orientation rule.** For path $P_n$ ($n \\geq 3$): compute signed phase-gradient score "
                "... If $S = E = 0$: balanced path-tie.")
    muts = {
        "K1 old orientation text restored": cand.replace(orient_line, old_rule),
        "K2 one RID declaration dropped": cand.replace("[RID: TDRG-DEF-STAR] ", "", 1),
        "K3 unlogged change": cand.replace("**Thermodynamic crystallization.**", "**Thermodynamic crystallisation.**", 1),
        "K4 wrong engine hash in §8": cand.replace("4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608",
                                                    "4c94d8751dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608", 1),
        "K5 compound tag reintroduced": cand.replace("`[NUM]` In long-horizon", "`[NUM / mixed]` In long-horizon", 1),
        "K6 edited Appendix A history": cand.replace("### v2.12.13 — June 2026\n", "### v2.12.13 — July 2026\n", 1),
    }
    for name, mutated in muts.items():
        assert mutated != cand, name
        mlog = json.loads(json.dumps(log))
        if name.startswith("K4"):   # a consistent but wrong log: the hash change is propagated into the log
            for e in mlog["edits"]:
                e["new"] = e["new"].replace("4c94d8741dc4", "4c94d8751dc4"); e["new_sha256"] = sha(e["new"])
            mlog["candidate_sha256"] = sha(mutated)
            class B:   # builder stand-in that reproduces the mutated candidate, so only C8 can catch it
                NEW_RIDS = builder.NEW_RIDS
                @staticmethod
                def build(b): return mutated, mlog["edits"]
            r = gates(root, base, mutated, mlog, builder=B, out=quiet)
        else:
            r = gates(root, base, mutated, mlog, out=quiet)
        caught[name] = not all(r.values())
        out(f"[{'CAUGHT' if caught[name] else 'MISSED'}] {name}: failing gates "
            f"{[k for k, v in r.items() if not v]}")
    # K7 engine control: the "new" rule replaced by v18 must fail the dynamics gate
    r = dynamics(root, False, quiet, orient_factory=lambda eng: eng.orient_path)
    caught["K7 v18 rule substituted for the reference rule"] = not r
    out(f"[{'CAUGHT' if not r else 'MISSED'}] K7 v18 rule substituted for the reference rule: C10 "
        f"{'FAIL' if not r else 'PASS'}")
    return all(caught.values())


def main(argv):
    root = argv[argv.index("--root") + 1] if "--root" in argv else os.getcwd()
    args = [a for a in argv[1:] if not a.startswith("--") and a != root]
    base = open(args[0], "rb").read().decode("utf-8")
    cand = open(args[1], "rb").read().decode("utf-8")
    log = json.load(open(args[2], encoding="utf-8"))
    if "--controls" in argv:
        ok = controls(root, base, cand, log)
        print("CONTROLS:", "PASS (all caught)" if ok else "FAIL")
    else:
        res = gates(root, base, cand, log, exhaustive="--exhaustive" in argv)
        ok = all(res.values())
        print("RESULT:", "PASS" if ok else "FAIL", f"({sum(res.values())}/{len(res)} gates)")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main(sys.argv)
