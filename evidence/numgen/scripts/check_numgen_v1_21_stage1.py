#!/usr/bin/env python3
"""Checker for Number Genesis v1.21 stage 1 (corrected intermediate; not an edition).

usage: check_numgen_v1_21_stage1.py BASE INTERMEDIATE EDITLOG_JSON [--root REPO] [--controls]
  BASE = `git show numgen-v1.20.8:dsn/RTG_NUMBER_GENESIS_DSN.md`; INTERMEDIATE = dsn/RTG_NUMBER_GENESIS_DSN.md on the
  stage-1 branch; EDITLOG_JSON = evidence/numgen/v1.21/stage1_edit_log.json. --root defaults to the current directory
  (must be the repository: C10–C12 read tags and files from it). --controls runs the negative controls instead.

Gates (exit 0 iff all PASS):
 C0  BASE        base bytes are adopted v1.20.8 (835a56f8...817e)
 C1  BUILD       the builder reproduces the intermediate byte-exactly and the log hash matches
 C2  REVERSE     undoing the logged edits in reverse order recovers the base byte-exactly (no unlogged change)
 C3  CHANGELOG   the changelog region equals the base one with only the declared stage-1 entry inserted
 C4  HEADER      the header block (before "## §0.") is unchanged (header work is stage 2)
 C5  RIDS        every NUMGEN-* string of the base survives; the new [RID: ...] declarations are exactly the five
                 tier-1 RIDs, each declared once, at its statement; none occurs in another dsn/ or noncanonical/ file
 C6  TAGS        status-tag census: intermediate = base + {[OPEN] -1, [THM] +1, [DEF] +1, [RESULT] +1, [from: NUM] +1,
                 [PROVENANCE] -1 (E42 merges two consumer rows into one)}; every other tag count unchanged
 C7  GRADES      outside E01 (OPEN -> imported THM + NUM range) and E04 (DEF alias table) no edit adds, removes or
                 changes a [THM]/[ALG]/[from: X] tag
 C8  OPEN        the only removed [OPEN] is the L-PHASE explicit-constant sub-item; NUMGEN-OPEN-NG0R-COV and every
                 other OPEN record survive; Census-1 stays INCONCLUSIVE / INCONCLUSIVE
 C9  IMPORTS     every import tag introduced by an edit carries one RID; "403/250" occurs only in the imported block
                 and the acceptance-matrix row; no identification of phi* with C_D^ext is asserted
 C10 SOURCES     every DYAD-/RECOG-/GEN-/RTG- identifier introduced by an edit exists in the owner file at its tag
                 (dyad-v6.4.22, recog-v0.3.24, gen-v2.9, programme-v1.3, ofn-v0.10); the cited facts are present there
                 (403/250 and 0.04654 at the row-A theorem; P_5 at DYAD-ALG-P5-RADIAL; 15/2; U_NUMGEN; 1.13 at
                 GEN-ART-SATURATION; SG-PROG-1/2); the cited RECOG hash prefix matches the file at the tag
 C11 EVIDENCE    every repository path introduced by an edit exists (on this tree, or until merged on the record
                 branches of PR #69 / PR #73); the four cited held-record hashes match the held-records SHA256SUMS
 C12 LABELS      the alias table defines the five labels once; every labelled domain used in edited text is defined there
 C13 REVIEW-R1R2 (round 2) no arrow between domains in the acceptance matrix, each row says "comparison only" or "no
                 inclusion claimed"; the availability clause names the branch upload/numgen-records and the release-commit
                 condition; the log records the round-1 hash 702e3917...3880 as superseded
"""
import hashlib, importlib.util, json, os, re, subprocess, sys

BASE_SHA = "835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e"
CHG = "## Changelog\n"
HEADER_END = "## §0. Epistemic Conventions"
NEW_RIDS = {"NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET": "**GAP-LOCK Lemma 1 CLOSED",
            "NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT": "**GAP-LOCK Lemma 2 CLOSED",
            "NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO": "**GAP-LOCK Lemma 3 CLOSED",
            "NUMGEN-RESULT-N5AS1-INF2": "**INF-2 / crossing count.**",
            "NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE": "**First-nonlinear cyclic-average theorem.**"}
TAG_DELTA = {"[OPEN]": -1, "[THM]": 1, "[DEF]": 1, "[RESULT]": 1, "[from: NUM]": 1, "[PROVENANCE]": -1}
TAGS = ["[THM]", "[ALG]", "[OPEN]", "[DEF]", "[RESULT]", "[COR]", "[HYP]", "[FAIL]", "[CAND]", "[GUARD]", "[NUM]",
        "[INTERP]", "[PROVENANCE]", "[from: ALG]", "[from: THM]", "[from: NUM]", "[from: DEF]", "[from: HEUR]"]
TAGGED = {"dyad-v6.4.22": "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "recog-v0.3.24": "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md",
          "gen-v2.9": "dsn/RTG_GENESIS_GEOMETRY_DSN.md", "programme-v1.3": "dsn/RTG_PROGRAMME_OVERVIEW.md",
          "ofn-v0.10": "dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md"}
PREFIX_TAG = {"DYAD-": "dyad-v6.4.22", "RECOG-": "recog-v0.3.24", "GEN-": "gen-v2.9", "RTG-OPEN-": "programme-v1.3",
              "RTG-OFN-": "ofn-v0.10"}
HELD = {"NG_N5AS1_INF_REDUCTION_v1.md": "90eb6658", "ng_n5as1_inf_reduction_cert_v1.py": "41917710",
        "ng_n5as1_inf_reduction_cert_v1.log": "4100e3a5", "NG_C7C_M2_PREREG_FREEZE_MANIFEST_v1.md": "cefb7180"}
# records cited by the stage-1 text that are on open record PRs (#69 held records, #73 reconciliation) until merged
PENDING_REFS = ["origin/upload/numgen-records", "origin/claude/numgen-disposition-reconciliation"]
LABELS = ["U_NG", "U_NG,tube", "U_D,base", "U_D,tube", "U_R,base"]

def sha(s): return hashlib.sha256(s.encode() if isinstance(s, str) else s).hexdigest()
def live(s): return s[:s.index(CHG)]
def git(root, *a): return subprocess.run(["git", "-C", root, *a], capture_output=True, text=True)
def show(root, ref, path):
    r = git(root, "show", f"{ref}:{path}")
    return r.stdout if r.returncode == 0 else None

def load_builder(root):
    p = os.path.join(root, "evidence/numgen/scripts/build_numgen_v1_21_stage1.py")
    spec = importlib.util.spec_from_file_location("b", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def census(text):
    t = live(text)
    return {k: t.count(k) for k in TAGS}

def reverse(inter, log):
    t = inter
    for e in reversed(log["edits"]):
        if t.count(e["new"]) != 1:
            return None
        t = t.replace(e["new"], e["old"])
    return t

def check(base, inter, log, root, verbose=True):
    res = {}
    def gate(k, ok, msg=""):
        res[k] = bool(ok)
        if verbose: print(f"{k}: {'PASS' if ok else 'FAIL'} {msg}")
    gate("C0 BASE", sha(base) == BASE_SHA)
    try:
        b = load_builder(root)
        built, _ = b.build(base)
        gate("C1 BUILD", built == inter and log["intermediate_sha256"] == sha(inter) and log["base_sha256"] == BASE_SHA)
    except Exception as ex:
        gate("C1 BUILD", False, repr(ex))
    gate("C2 REVERSE", reverse(inter, log) == base)
    bc, ic = base[base.index(CHG):], inter[inter.index(CHG):]
    chg_e = [e for e in log["edits"] if e["key"] == "CHG"]
    gate("C3 CHANGELOG", len(chg_e) == 1 and ic == bc.replace(CHG, chg_e[0]["new"], 1))
    gate("C4 HEADER", base[:base.index(HEADER_END)] == inter[:inter.index(HEADER_END)])
    # C5
    base_ids = set(re.findall(r"NUMGEN-[A-Z0-9-]*[A-Z0-9]", base))
    inter_ids = set(re.findall(r"NUMGEN-[A-Z0-9-]*[A-Z0-9]", inter))
    base_decl = set(re.findall(r"\[RID: (NUMGEN-[A-Z0-9-]*[A-Z0-9])\]", base))
    inter_decl = re.findall(r"\[RID: (NUMGEN-[A-Z0-9-]*[A-Z0-9])\]", inter)
    new_decl = set(inter_decl) - base_decl
    attached = all(sum(1 for l in inter.split("\n") if f"[RID: {r}]" in l and NEW_RIDS[r] in l) == 1
                   and inter_decl.count(r) == 1 for r in NEW_RIDS)
    others = []
    for d in ("dsn", "noncanonical"):
        for fn in os.listdir(os.path.join(root, d)):
            if fn.endswith(".md") and fn != "RTG_NUMBER_GENESIS_DSN.md":
                txt = open(os.path.join(root, d, fn), encoding="utf-8").read()
                others += [r for r in NEW_RIDS if r in txt]
    gate("C5 RIDS", base_ids <= inter_ids and new_decl == set(NEW_RIDS) and attached and not others,
         f"new={sorted(new_decl)} collisions={others}")
    # C6
    cb, ci = census(base), census(inter)
    delta = {k: ci[k] - cb[k] for k in TAGS if ci[k] != cb[k]}
    gate("C6 TAGS", delta == TAG_DELTA, f"delta={delta}")
    # C7
    q = re.compile(r"\[from: [^\]]+\]|\[(?:THM|ALG)\]")
    bad = [e["key"] for e in log["edits"] if e["key"] not in ("E01", "E04", "CHG")
           and sorted(q.findall(e["old"])) != sorted(q.findall(e["new"]))]
    gate("C7 GRADES", not bad, f"{bad}")
    # C8
    open_lines = lambda t: [l for l in live(t).split("\n") if "`[OPEN]`" in l or l.startswith("[OPEN]")]
    removed = [l for l in open_lines(base) if l not in open_lines(inter)]
    gate("C8 OPEN", len(removed) == 1 and "L-PHASE explicit constant" in removed[0]
         and "NUMGEN-OPEN-NG0R-COV" in inter and live(inter).count("INCONCLUSIVE / INCONCLUSIVE") == live(base).count("INCONCLUSIVE / INCONCLUSIVE"),
         f"removed={len(removed)}")
    # C9
    new_texts = "\n".join(e["new"] for e in log["edits"])
    new_imports = [m for m in re.findall(r"\[import: [^\]]*\]", new_texts) if m not in re.findall(r"\[import: [^\]]*\]", base)]
    one_rid = all(";" not in m.split("|", 1)[1] for m in new_imports if "|" in m)
    l403 = [l for l in live(inter).split("\n") if "403/250" in l]
    phi = re.search(r"phi\*?\s*(=|equals|is)\s*C_D\^ext", live(inter)) is not None
    e01 = next(e["new"] for e in log["edits"] if e["key"] == "E01")
    ok403 = all(l in e01 or (l.startswith("| L-PHASE `NUMGEN-RESULT-N5AS1-L-PHASE`") and "DYAD-THM-LPHASE-ROWA-REMAINDER" in l) for l in l403)
    gate("C9 IMPORTS", one_rid and l403 and ok403 and not phi,
         f"imports={len(new_imports)} lines403={len(l403)}")
    # C10
    ids = set(re.findall(r"\b(?:DYAD|RECOG|GEN|RTG-OPEN|RTG-OFN)-[A-Z0-9-]*[A-Z0-9]\b", new_texts))
    srcs = {t: show(root, t, p) for t, p in TAGGED.items()}
    missing = []
    for i in sorted(ids):
        tag = next(v for k, v in PREFIX_TAG.items() if i.startswith(k))
        if srcs[tag] is None or i not in srcs[tag]:
            missing.append(i)
    dy, rc, gn, pg = srcs["dyad-v6.4.22"], srcs["recog-v0.3.24"], srcs["gen-v2.9"], srcs["programme-v1.3"]
    facts = (dy and rc and gn and pg
             and any("DYAD-THM-LPHASE-ROWA-REMAINDER]" in l and "U=\\{0<Q\\le\\tfrac1{625}\\}" in l for l in dy.split("\n"))
             and "\\tfrac{403}{250}" in dy and "0.04654" in dy
             and any("[RID: DYAD-ALG-P5-RADIAL]" in l and "5\\eta^3-43\\eta^2\\rho+4\\eta\\rho^2-5\\rho^3" in l for l in dy.split("\n"))
             and "\\tfrac{15}2\\sqrt{Q_m}" in rc and "U_{\\rm NUMGEN}" in rc and "0.927" in rc
             and any("GEN-ART-SATURATION" in l and "1.13" in l for l in gn.split("\n"))
             and "[SG-PROG-1]" in pg and "[SG-PROG-2]" in pg
             and sha(rc).startswith("8c64bea2") and sha(rc).endswith("69e7c1"))
    gate("C10 SOURCES", not missing and facts, f"missing={missing}")
    # C11
    paths = set(re.findall(r"`((?:evidence|records|pipes|upload)/[^`\s]+)`", new_texts))
    def exists(p):
        if os.path.exists(os.path.join(root, p)): return True
        return any(git(root, "cat-file", "-e", f"{ref}:{p.rstrip('/')}").returncode == 0 for ref in PENDING_REFS)
    nopath = [p for p in sorted(paths) if "<" not in p and not exists(p)]   # "<file>" is a path pattern, not a path
    sums = None
    for ref in ("HEAD", "origin/upload/numgen-records"):
        sums = show(root, ref, "upload/numgen-records/SHA256SUMS.txt")
        if sums: break
    held_ok = bool(sums) and all(any(l.startswith(h) and l.rstrip().endswith("  " + f) for l in sums.split("\n")) for f, h in HELD.items())
    gate("C11 EVIDENCE", not nopath and held_ok, f"missing_paths={nopath}")
    # C12
    tbl = [l for l in inter.split("\n") if l.startswith("| `U_")]
    defined = [re.match(r"\| `([^`]+)`", l).group(1) for l in tbl]
    used = set(re.findall(r"U_(?:NG|D|R)(?:,(?:tube|base))?", new_texts))
    gate("C12 LABELS", sorted(defined) == sorted(LABELS) and used <= set(LABELS), f"used={sorted(used)}")
    # C13 (round 2)
    mrows = [l for l in inter.split("\n") if l.startswith("| ") and "`NUMGEN-RESULT-N5AS1-" in l and "statement accepted" in l or l.startswith("| L-PHASE `NUMGEN-RESULT-N5AS1-L-PHASE`")]
    r1 = len(mrows) == 8 and all(" → " not in l and "no inclusion claimed" in l for l in mrows)
    r2 = ("on the branch `upload/numgen-records`" in inter and "reachable at the release commit only if that branch is merged" in inter
          and "are in the repository at `upload/numgen-records/`" not in inter)
    gate("C13 REVIEW-R1R2", r1 and r2 and log.get("round1_intermediate_sha256") == "702e3917126edfeeda41e43b6a8ad820695b5feec19a61e724b12849dfb83880",
         f"matrix_rows={len(mrows)}")
    return res

def controls(base, inter, log, root):
    def mutate(desc, f, edits_fn=None):
        t = f(inter)
        lg = json.loads(json.dumps(log))
        if edits_fn: edits_fn(lg)
        lg["intermediate_sha256"] = sha(t)
        r = check(base, t, lg, root, verbose=False)
        failed = [k for k, v in r.items() if not v]
        print(f"{desc}: {'caught by ' + ', '.join(failed) if failed else 'NOT CAUGHT'}")
        return bool(failed)
    def both(a, b):
        def f(t): assert t.count(a) == 1, a; return t.replace(a, b)
        def g(lg):
            for e in lg["edits"]:
                if a in e["new"]: e["new"] = e["new"].replace(a, b)
        return f, g
    ok = []
    ok.append(mutate("NC1 unlogged body edit", lambda t: t.replace("only through the entry-phase shift", "only through the entry phase shift", 1)))
    f, g = both("[RID: NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT] ", ""); ok.append(mutate("NC2 tier-1 RID dropped", f, g))
    f, g = both("`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET]", "`[RESULT] [from: THM]` [RID: NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET]"); ok.append(mutate("NC3 regrade GAP-LOCK 1", f, g))
    ok.append(mutate("NC4 constant entered into NUMGEN's own L-PHASE", lambda t: t.replace(" = 2 pi - tau q_m + r_m,\n|r_m| <= C q_m^(3/2).", " = 2 pi - tau q_m + r_m,\n|r_m| <= (403/250) q_m^(3/2).", 1)))
    f, g = both("| `U_R,base` | the set `U_D,base`", "| `U_X,base` | the set `U_D,base`"); ok.append(mutate("NC5 undefined domain label", f, g))
    f, g = both("`RECOG-THM-A1A-LIFT-ALIGNMENT` (`recog-v0.3.24` §6.13b; consumer", "`RECOG-THM-A1A-LIFT-ALIGNMENT-U` (`recog-v0.3.24` §6.13b; consumer"); ok.append(mutate("NC6 nonexistent RECOG RID cited", f, g))
    f, g = both("[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.19) | DYAD-THM-LPHASE-ROWA-REMAINDER] `[scope:", "[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.19) | DYAD-THM-LPHASE-ROWA-REMAINDER; DYAD-THM-PRIM-CTR] `[scope:"); ok.append(mutate("NC7 merged import", f, g))
    ok.append(mutate("NC8 header edited", lambda t: t.replace("**Title:** RTG Number Genesis", "**Title:** RTG  Number Genesis", 1)))
    ok.append(mutate("NC9 another OPEN removed", lambda t: t.replace("`[OPEN]` **NG-7B.**", "**NG-7B.**", 1)))
    ok.append(mutate("NC10 changelog history edited", lambda t: t.replace("### v1.20.7 — October 1, 2026", "### v1.20.7 — October 2, 2026", 1)))
    f, g = both("`ng_n5as1_inf_reduction_cert_v1.py` / `.log`, `41917710…ee36`", "`ng_n5as1_inf_reduction_cert_v1.py` / `.log`, `41917710…ee36` (`evidence/numgen/missing_file.py`)"); ok.append(mutate("NC11 nonexistent evidence path", f, g))
    f, g = both("| NUMGEN: `U_NG,tube`; RECOG: `U_D,tube` (comparison only; no inclusion claimed) |", "| `U_NG,tube` → `U_D,tube` |"); ok.append(mutate("NC12 domain arrow reintroduced (R1)", f, g))
    print("RESULT:", "PASS (all controls caught)" if all(ok) else "FAIL")
    return 0 if all(ok) else 1

def main(argv):
    root = argv[argv.index("--root") + 1] if "--root" in argv else "."
    pos = [a for a in argv[1:] if not a.startswith("--") and a != root]
    base = open(pos[0], "rb").read().decode("utf-8"); inter = open(pos[1], "rb").read().decode("utf-8")
    log = json.load(open(pos[2], encoding="utf-8"))
    if "--controls" in argv:
        return controls(base, inter, log, root)
    r = check(base, inter, log, root)
    ok = all(r.values())
    print(f"intermediate sha256 {sha(inter)}")
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
