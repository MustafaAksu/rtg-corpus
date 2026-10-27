#!/usr/bin/env python3
"""check_recog_v0_3_25_stage1.py -- deterministic checker for the RECOG v0.3.25 stage-1 intermediate.

usage (from the repository root):
  python -I evidence/recog/scripts/check_recog_v0_3_25_stage1.py BASE INTERMEDIATE EDITLOG_JSON [--controls]
  BASE = `git show recog-v0.3.24:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`; EDITLOG_JSON written by the builder
  (any group variant: the gates read the declared groups from the log).
exit 0 = every gate PASS (and, with --controls, every negative control caught by its target gate).

Gates (as v0.3.24 stage 1; no history moves in this release, so the MNT exceptions of C5/C10/C22 are gone; C24 added in round 2):
  C0  BASE       base SHA-256 is the adopted v0.3.24 identity (tag recog-v0.3.24)
  C1  BUILD      intermediate == exact-once application of the logged edits (Appendix A masked for "live")
  C2  REVERSE    undoing every edit recovers the base byte-exactly
  C3  APPENDIX A Appendix A minus the new v0.3.25 entry is byte-identical to the base Appendix A
  C4  SPAN TAGS  edits whose backticked tag multiset changes are exactly the declared TAG_CHANGE edits
  C5  SPAN RIDS  no edit removes a [RID: X] declaration; added declarations are the declared new RIDs
  C6  STATUS     OPEN-registry "Status:" lines are byte-identical to the base (no status word, no history sentence changes)
  C7  RID SET    RECOG RID set == base set + the declared new RIDs of the built groups; none removed
  C8  RID ATTACH for every pre-existing RECOG RID declaration the after-text is unchanged; new RIDs attach to their
                 declared statements
  C9  RESULT     in §§1-6 every line-leading [RESULT] is followed by [from: TAG] with one canonical tag
  C10 QUALIFIERS no edit removes a qualifier; global change == sum of per-edit changes
  C11 VOCAB      no READ / WRITE / DECODE vocabulary introduced
  C12 IMPORTS    v0.3.24 import state kept (no "RID unavailable"; both NUMGEN RIDs; owner tag forms)
  C13 R9/A1B     the RECOG-THM-R9-MEMORY statement line, its row table, the (c) row table and the RECOG-THM-A1B-SLIP-SCHEDULE-U
                 statement (tag line through the proof sketch) are unchanged; the adopted rows (517, 163) stay in force
  C14 HEADER     title, date, supersedes, status summary and footer unchanged
  C15 HEADINGS   heading lines equal the base
  C16 §8 FILES   every backticked file name in §8 exists in the repository; every SHA-256 (full or abbreviated 8…4) quoted in the
                 new §8 rows is the hash of the named repository file (directory references: a file of that directory)
  C17 LIVE       must-stay-live items present (F2(a3), W1-W5, R6 ACTIVE, registry-relative, no write-through); R4 ACTIVE;
                 the R6 sub-item A1c-Q1′ stays [OPEN]
  C18 DECOUPLE   each buildable variant (B1, A1CE, A1CQ, A1CE+A1CD) carries exactly its own new RIDs; A1CD alone is refused
  C19 VALUES     the constants displayed in the new blocks agree with the certificate outputs in the repository
  C20 NOTICES    the §7.2 outbound-notices paragraph is unchanged (no notice state changed)
  C21 TAG CENSUS global backticked-tag multiset delta == sum of the per-edit deltas
  C22 ASSUMING   every new block that depends on the (D5) proof constants or the C_7 ceilings carries a backticked [assuming:]
                 qualifier, and every such qualifier names the Dyadic source; the sharpened schedule and the contractor
                 are not tagged [THM] without it
  C23 RECORDS    every records/recog path named in the new text exists; the review-accepted record versions named in §8 match
                 the records' own status lines
  C24 R83-1      (round 2) the known-a sharpened-schedule centre is never called "record-only" (§1 and §6.13b); the R6 decoder
                 closure line says "not record-only" for the majorant and is scoped to U, two usable slips, outer windows,
                 the (D5) [assuming:], no Q1′ conclusion
"""
import hashlib, importlib.util, json, os, re, subprocess, sys, zipfile
from collections import Counter

BASE_SHA = "8c64bea231b3691b737f4143f6f4105030ee183fcc90d7f604ec83a4c869e7c1"
PREV_TAG = "recog-v0.3.24"
APPA_START, APPA_END = "## Appendix A — Version History", "## Appendix B —"
NEW_RIDS = {
 "B1": {"RECOG-ALG-R9-SUM-LEMMA", "RECOG-THM-R9-SHARPENED-ROWS", "RECOG-THM-R9-SHARPENED-ROWS-C7", "RECOG-ART-R9-SHARPENED-ROWS"},
 "A1CE": {"RECOG-ALG-A1C-TAIL-HARMONICS", "RECOG-ALG-A1C-INBLOCK-ANGLE", "RECOG-ALG-A1C-COMBINED-TAIL", "RECOG-THM-A1C-SHARPENED-SCHEDULE", "RECOG-ART-A1C-SHARPENED-SCHEDULE"},
 "A1CD": {"RECOG-ALG-A1C-ADMISSIBLE-REGION", "RECOG-ALG-A1C-START-OFFSET", "RECOG-ALG-A1C-JOINT-CONTRACTOR", "RECOG-ART-A1C-DECODER"},
 "A1CQ": {"RECOG-ALG-A1C-THRESHOLD-CODING", "RECOG-ALG-A1C-PHASE-C1-FIBER", "RECOG-ART-A1C-Q1PRIME-FIBER"},
}
ATTACH = {
 "RECOG-ALG-R9-SUM-LEMMA": " [scope: any sequence with $q_m\\le q_0/(1+\\tfrac12q_0m)$",
 "RECOG-THM-R9-SHARPENED-ROWS": " [scope: as RECOG-THM-R9-MEMORY and RECOG-THM-R9-COMPARATOR-INCOMPLETENESS, per row; adopted statements only]",
 "RECOG-THM-R9-SHARPENED-ROWS-C7": " [scope: as RECOG-THM-R9-SHARPENED-ROWS] `[assuming: $C_7\\le85.1$",
 "RECOG-ART-R9-SHARPENED-ROWS": " `[v0.3.25]` :: `recog_b1_l1l2_sharpened_rows_cert.py`",
 "RECOG-ALG-A1C-TAIL-HARMONICS": " [scope: $x_0\\in U$; every $M\\ge1$] `[assuming: Dyadic row-A bridge constants",
 "RECOG-ALG-A1C-INBLOCK-ANGLE": " [scope: $y\\in U_T$; primitive frame $W=\\sqrt Qe^{i\\theta}$; no Dyadic proof constant]",
 "RECOG-ALG-A1C-COMBINED-TAIL": " [scope: $x_0\\in U$, chart row A, branch (B)]",
 "RECOG-THM-A1C-SHARPENED-SCHEDULE": " [scope: as RECOG-THM-A1B-SLIP-SCHEDULE-U; $a$ known] `[assuming: Dyadic row-A bridge constants",
 "RECOG-ART-A1C-SHARPENED-SCHEDULE": " `[v0.3.25]` :: part 1b `recog_a1c_tail_averaging_cert.py`",
 "RECOG-ALG-A1C-ADMISSIBLE-REGION": " [scope: as RECOG-THM-A1C-SHARPENED-SCHEDULE, $a$ unknown] `[assuming: the Dyadic (D5)",
 "RECOG-ALG-A1C-START-OFFSET": " [scope: $x_0\\in U$; first anchor $1\\le n_0\\le7$",
 "RECOG-ALG-A1C-JOINT-CONTRACTOR": " [scope: as above; $a$ unknown; the true $a$ is never an input",
 "RECOG-ART-A1C-DECODER": " `[v0.3.25]` :: part 2 `recog_a1c_unknown_a_interval_cert.py`",
 "RECOG-ALG-A1C-THRESHOLD-CODING": " [scope: $x_0\\in U$; F2(b) conventions]",
 "RECOG-ALG-A1C-PHASE-C1-FIBER": " [scope: chart row A, $0<q_0\\le q^*=\\tfrac{256}{140625}$",
 "RECOG-ART-A1C-Q1PRIME-FIBER": " `[v0.3.25]` :: `recog_a1c_q1prime_fiber_cert.py`",
}
TAG_CHANGE = {
 "S1-A1CE": "§1 sharpened-schedule sentence (new [THM], [assuming:])",
 "S1-A1CD": "§1 decoder sentence (new [ALG])", "S1-A1CQ": "§1 fiber sentence (new [ALG])",
 "S2-R6-Q1P": "R6 sub-item A1c-Q1′ ([SESSION/HEUR] added; [OPEN] kept)", "S2-R6-DEC": "R6 sub-item A1c-decoder ([OPEN] → [ALG] ✓, [NUM])",
 "S613a-B1": "§6.13a block (new [ALG], [THM], [assuming:])", "S613b-A1CE": "§6.13b block (new [ALG], [ALG via IA], [THM], [assuming:], [NUM])",
 "S616e-A1CQ": "§6.16e fiber block (new [ALG], [SESSION/HEUR], [NUM])", "S616e-A1CD": "§6.16e decoder block (new [ALG], [assuming:], [NUM])",
 "S8-B1": "B1 artifact row ([v0.3.25], [THM])", "S8-A1CE": "A1c-E artifact row ([v0.3.25], [ALG], [THM], [NUM])",
 "S8-A1CD": "A1c-D artifact row ([v0.3.25], [ALG], [NUM])", "S8-A1CQ": "A1c-Q artifact row ([v0.3.25], [ALG], [NUM], [SESSION/HEUR])",
 "A-1": "Appendix A entry quotes tags",
}
IMPORT_RIDS_ALLOWED = set()
FILE_EXCEPT = {"dyad_referee_p2b_v2.py"}
CANON = {"DEF", "THM", "ALG", "ALG via IA", "THM-ALG via IA", "ENG", "NUM", "NUM strong", "OBS", "HEUR",
         "HEUR strong", "HYP", "ALG candidate", "ALG structure"}
TAGBT = re.compile(r"`\[[A-Z][^`\]]*\]`")
RID_RECOG = re.compile(r"\[RID: (RECOG-[A-Z0-9-]*[A-Z0-9])")
ANYRID = re.compile(r"\[RID: ([A-Z][A-Z0-9-]*[A-Z0-9])")
VOCAB = re.compile(r"\b(READ|WRITE|DECODE)\b")
RESULT_LEAD = re.compile(r"^(?:`\[RESULT\]`|\[RESULT\])")
FROM = re.compile(r"^(?:`\[RESULT\]`|\[RESULT\])\s*(?:`\[from: ([^`\]]+)\]`|\[from: ([^\]]+)\])")
QUAL = re.compile(r"\[(?:scope|assumes|assuming): [^\]]*\]")
HASHREF = re.compile(r"`((?:evidence|records)/[^`]+/|(?:[A-Za-z0-9_.\-/]*/)?[A-Za-z0-9_.\-]+\.(?:py|json|md|txt))`(?: v0\.[0-9.]+)?(?: \((?:sha256 )?`([0-9a-f]{8}…[0-9a-f]{4}|[0-9a-f]{64})`(?:, `([0-9a-f]{8}…[0-9a-f]{4}|[0-9a-f]{64})`)?\))?")
RECPATH = re.compile(r"`(records/recog/[A-Za-z0-9_./-]+\.md)`")
RECVER = re.compile(r"`(RECOG_[A-Z0-9_]+_v0_1\.md)` (v0\.[0-9.]+)")

def split_appa(s):
    i, j = s.index(APPA_START), s.index(APPA_END)
    return s[:i], s[i:j], s[j:]
def live(s):
    a, _, c = split_appa(s); return a + c
def section(s, start, end):
    i = s.find(start); j = s.find(end, i + 1)
    return s[i:j] if i >= 0 and j > i else ""
def apply_log(base, edits, reverse=False):
    a, appa, c = split_appa(base)
    lv = a + "\x00APPA\x00" + c
    for e in (reversed(edits) if reverse else edits):
        old, new = (e["new"], e["old"]) if reverse else (e["old"], e["new"])
        if e["region"] == "live":
            if lv.count(old) != 1: return None
            lv = lv.replace(old, new, 1)
        else:
            if appa.count(old) != 1: return None
            appa = appa.replace(old, new, 1)
    if lv.count("\x00APPA\x00") != 1: return None
    return lv.replace("\x00APPA\x00", appa)
def after_texts(s):
    out = {}
    for m in re.finditer(r"\[RID: (RECOG-[A-Z0-9-]*[A-Z0-9])\]", s):
        e = s.find("\n", m.end()); e = len(s) if e < 0 else e
        out.setdefault(m.group(1), []).append(s[m.end():min(m.end() + 60, e)])
    return {k: Counter(v) for k, v in out.items()}
def repo_files(root):
    names, paths = set(), {}
    for top in ("evidence/recog", "records/recog"):
        for d, _, fs in os.walk(os.path.join(root, top)):
            for f in fs:
                names.add(f); paths.setdefault(f, []).append(os.path.join(d, f))
                if f.endswith(".zip"):
                    try:
                        for m in zipfile.ZipFile(os.path.join(d, f)).namelist(): names.add(os.path.basename(m))
                    except zipfile.BadZipFile: pass
    return names, paths
def load_builder(root):
    p = os.path.join(root, "evidence/recog/scripts/build_recog_v0_3_25_stage1.py")
    spec = importlib.util.spec_from_file_location("b", p); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def hmatch(h, full): return full == h if len(h) == 64 else (full.startswith(h[:8]) and full.endswith(h[-4:]))
def near(x, y, rel=0.05): return abs(x - y) <= rel * max(abs(x), abs(y), 1e-300)

def check(base, inter, log, root, verbose=True, files=None):
    res = {}
    def gate(n, ok, msg=""):
        res[n] = bool(ok)
        if verbose: print(f"  {n:<4} {'PASS' if ok else 'FAIL'} {msg}")
    edits = log["edits"]; groups = set(log.get("groups", []))
    new_rids = set().union(*(NEW_RIDS[g] for g in groups))
    gate("C0", hashlib.sha256(base.encode()).hexdigest() == BASE_SHA, "BASE")
    gate("C1", apply_log(base, edits) == inter and hashlib.sha256(inter.encode()).hexdigest() == log["intermediate_sha256"], "BUILD")
    gate("C2", apply_log(inter, edits, reverse=True) == base, "REVERSE")
    _, ab, _ = split_appa(base); _, ai, _ = split_appa(inter)
    i = ai.find("### v0.3.25"); j = ai.find("### v0.3.24", i)
    gate("C3", i > 0 and j > i and ai[:i] + ai[j:] == ab, "APPENDIX A")
    changed = {e["key"] for e in edits if Counter(TAGBT.findall(e["old"])) != Counter(TAGBT.findall(e["new"]))}
    declared = {k for k in TAG_CHANGE if any(e["key"] == k for e in edits)}
    gate("C4", changed == declared, f"SPAN TAGS {sorted(changed ^ declared) if changed != declared else ''}")
    bad = []
    L = live(inter)
    for e in edits:
        ro, rn = ANYRID.findall(e["old"]), ANYRID.findall(e["new"])
        if [x for x in ro if x not in rn]: bad.append(e["key"])
        if any(x not in ro and x not in new_rids | IMPORT_RIDS_ALLOWED for x in rn): bad.append(e["key"])
    gate("C5", not bad, f"SPAN RIDS {bad}")
    st = lambda s: [l for l in live(s).splitlines() if l.startswith("Status:")]
    gate("C6", st(base) == st(inter), "STATUS (byte-identical)")
    want = set(RID_RECOG.findall(base)) | new_rids
    gate("C7", set(RID_RECOG.findall(inter)) == want, "RID SET")
    atb, ati = after_texts(live(base)), after_texts(live(inter))
    ok = all(atb[k] == ati.get(k) for k in atb)
    for k in new_rids:
        sig = ATTACH[k]; v = ati.get(k, Counter()); n = min(60, len(sig))
        ok &= sum(1 for x in v.elements() if x[:n] == sig[:n]) == 1
    gate("C8", ok, "RID ATTACH")
    head = L[:L.index("## §7. Import Ledger")]
    viol = [l[:60] for l in head.splitlines() if RESULT_LEAD.match(l) and ((FROM.match(l).group(1) or FROM.match(l).group(2)) if FROM.match(l) else None) not in CANON]
    gate("C9", not viol, f"RESULT {len(viol)} unpaired/combined" if viol else "RESULT")
    keys = lambda t: Counter(QUAL.findall(t)) + Counter({w: t.count(w) for w in ("Depends on:", "[cert:", "[proof:", "[import:")})
    glob = keys(inter); glob.subtract(keys(base))
    loc, removed = Counter(), []
    for e in edits:
        d = keys(e["new"]); d.subtract(keys(e["old"])); loc.update(d)
        if -d: removed.append(e["key"])
    gate("C10", not removed and +glob == +loc and -glob == -loc, "QUALIFIERS" + (f" removed in {removed}" if removed else ""))
    gate("C11", len(VOCAB.findall(inter)) == len(VOCAB.findall(base)), "VOCAB")
    cell = section(inter, "#### §6.13b A1a", "### §6.14 The $h$-Chart Ledger")
    s7 = section(inter, "## §7. Import Ledger", "### §7.1")
    ok = ("RID unavailable" not in cell and "RID unavailable" not in s7
          and all(x in cell and x in s7 for x in ("NUMGEN-DEF-N5AS1-DEFECT", "NUMGEN-RESULT-N5AS1-INF1"))
          and "`[THM — conditional on RECOG-THM-R9-MEMORY]`" not in L)
    gate("C12", ok, "IMPORTS")
    r9 = lambda s: [l for l in s.splitlines() if l.startswith("`[THM]` [RID: RECOG-THM-R9-MEMORY]")]
    rows = lambda s: [l for l in s.splitlines() if l.startswith("| A | $0<\\lvert W_0") or l.startswith("| B | $0<\\lvert W_0") or l.startswith("| large | $|z|\\le\\tfrac1{20}$, $C_7=100$") or l.startswith("| small | $|z|\\le\\tfrac1{40}$, $C_7=30$")]
    a1b = lambda s: section(s, "`[THM]` [RID: RECOG-THM-A1B-SLIP-SCHEDULE-U] [scope:", "\n**Not supplied:**")
    ok = len(r9(base)) == 1 and r9(base) == r9(inter) and len(rows(base)) == 4 and rows(base) == rows(inter)
    ok &= len(a1b(base)) > 1000 and a1b(base) == a1b(inter)
    ok &= all(x in cell and x in s7 for x in ("\\tfrac{3951}{1000}", "\\tfrac{971}{250}", "\\tfrac{256}{225}"))
    gate("C13", ok, "R9/A1B statements unchanged")
    hd = lambda s: ([l for l in s.splitlines()[:60] if l.startswith(("# ", "**Date:**", "**Supersedes:**", "**Title:**", "**Scope:**", "**Status summary", "**Document status"))] + s.splitlines()[-3:])
    gate("C14", hd(base) == hd(inter), "HEADER")
    hs = lambda s: [l for l in s.splitlines() if l.startswith("#")]
    gate("C15", hs(live(base)) == hs(live(inter)), "HEADINGS")
    s8 = section(inter, "## §8. Artifact", "## §9.")
    names = set(re.findall(r"`([A-Za-z0-9_.\-]+\.(?:py|json|jsonl|md|txt|zip))`", s8)) | {os.path.basename(x) for x in re.findall(r"`((?:evidence|records)/[^`]+\.(?:py|json|jsonl|md|txt))`", s8)}
    fl, paths = files if files is not None else repo_files(root)
    miss = sorted(n for n in names if n not in fl and n not in FILE_EXCEPT)
    hashok = True; nh = 0
    for row in [l for l in s8.splitlines() if "`[v0.3.25]`" in l]:
        for ref, h1, h2 in HASHREF.findall(row):
            for h in (h1, h2):
                if not h: continue
                nh += 1
                if ref.endswith("/"):
                    d = os.path.join(root, ref); cands = [os.path.join(d, f) for f in os.listdir(d)] if os.path.isdir(d) else []
                else:
                    cands = paths.get(os.path.basename(ref), [])
                hashok &= any(hmatch(h, sha(p)) for p in cands)
    gate("C16", not miss and hashok and nh >= 3 * len(groups), f"§8 FILES missing: {miss}" if miss else (f"§8 FILES ({nh} hashes checked)" if hashok else "§8 FILES: quoted hash mismatch"))
    ok = all(x in L for x in ("F2(a3)", "W1–W5", "registry-relative", "no identifiable token-specific write-through"))
    r6 = section(inter, "**OPEN R6 — Physical recognition-event rule**", "**OPEN R")
    r4 = section(inter, "**OPEN R4 — Intrinsic type-change locus**", "**OPEN R")
    ok &= any(l.startswith("Status: ACTIVE") for l in r6.splitlines()) and "R6 therefore remains **ACTIVE**" in L
    ok &= any(l.startswith("Status: ACTIVE") for l in r4.splitlines())
    q1 = [l for l in r6.splitlines() if l.startswith("- A1c-Q1′:")]
    ok &= len(q1) == 1 and q1[0].rstrip().endswith(":: `[OPEN]`") and "Neither answer is established" in q1[0]
    gate("C17", ok, "LIVE")
    ok = True
    try:
        m = load_builder(root)
        for gs in (("B1",), ("A1CE",), ("A1CQ",), ("A1CE", "A1CD")):
            eds = [e for e in m.EDITS if e[1] in gs] + [m.appa_edit(set(gs))]
            t, _ = m.apply(base, eds)
            ok &= set(RID_RECOG.findall(t)) == set(RID_RECOG.findall(base)) | set().union(*(NEW_RIDS[g] for g in gs))
        refused = False
        try:
            m.main(["b", os.path.join(root, "evidence/recog/v0.3.25/base_v0_3_24.md"), os.devnull, os.devnull, "--only", "A1CD"])
        except AssertionError:
            refused = True
        ok &= refused
    except AssertionError:
        ok = False
    gate("C18", ok, "DECOUPLE")
    ok = True
    try:
        J = lambda p: json.load(open(os.path.join(root, p)))
        if "B1" in groups:
            d = J("evidence/recog/b1_l1l2/b1_l1l2_sharpened_rows_cert.json"); rows_ = {r["row"]: r for r in d["G3_rows"]}
            ok &= d["ALL_PASS"] and rows_["L1 large"]["C2_new_ceiling_4sig"] == 259.2 and rows_["L1 small"]["C2_new_ceiling_4sig"] == 81.49
            ok &= rows_["L1+L2 large"]["C2_new_ceiling_4sig"] == 221.4 and rows_["L1+L2 small"]["C2_new_ceiling_4sig"] == 75.69
            ok &= near(rows_["L1 large"]["window_new"], 2.952e-5, 1e-3) and near(rows_["L1 small"]["window_new"], 9.390e-5, 1e-3)
            ok &= near(rows_["L1+L2 large"]["window_new"], 3.456e-5, 1e-3) and near(rows_["L1+L2 small"]["window_new"], 1.011e-4, 1e-3)
            ok &= near(d["G2_reproduction"]["K_Phi_100"][1], 258.4848, 1e-5) and near(d["G2_reproduction"]["K_Phi_30"][1], 81.4328, 1e-5)
            ok &= near(rows_["L1+L2 large"]["K_Phi_upper"], 220.8471, 1e-5) and near(rows_["L1+L2 small"]["K_Phi_upper"], 75.6392, 1e-5)
            ok &= min(v["lower/upper"] for v in d["G1_lemma_bracket"].values()) >= 0.9975
            ok &= all(x in L for x in ("(259.2,\\tfrac1{400})", "(81.49,\\tfrac1{1600})", "(221.4,\\tfrac1{400})", "(75.69,\\tfrac1{1600})", "2.952\\times10^{-5}", "9.390\\times10^{-5}", "3.456\\times10^{-5}", "1.011\\times10^{-4}", "258.4848", "81.4328", "220.8471", "75.6392"))
        if "A1CE" in groups:
            d = J("evidence/recog/a1c_1b/a1c_tail_averaging_cert.json"); c = d["G2_constants"]
            ok &= d["ALL_PASS"] and near(c["lead_S"], 0.74850, 1e-4) and near(c["lead_R"], 1.0753, 1e-4) and near(c["gamma0"][1], 0.17715, 1e-4) and near(c["gamma1"], 205.15, 1e-4)
            ok &= d["G6_universal"]["box_max"] < 0.31 and near(d["G6_universal"]["E(625,1)"], 0.3034, 1e-3)
            t = d["G4_table"]["625"]; ok &= near(t["1000"]["E"], 0.166, 1e-2) and near(t["10000"]["E"], 0.057, 2e-2) and near(d["G4_asymptotic_old"], 187.31, 1e-4)
            ok &= near(t["1000"]["E"] * (625 + 1000) ** 0.5 / (1000 + 625) ** 0.5 * (625 + 1000) ** 0.5, 0.166 * 40.31, 2e-2)
            d2 = J("evidence/recog/a1c_inblock/a1c_inblock_angular_cert.json"); c2 = d2["G2_constants"]
            ok &= d2["ALL_PASS"] and near(c2["c_delta_on_U_T"], 0.793, 1e-3) and near(d2["G3_asymptotic_constant"][1], 1.9396, 1e-4) and near(c2["e_sqrt"], 0.705, 2e-3) and near(c2["e_lin"], 0.257, 2e-3)
            ok &= d2["G1"]["kappa"] == ["0", "0", "0", "sqrt(3)/4", "sqrt(3)/4", "sqrt(3)/4"]
            d3 = J("evidence/recog/a1c_comb/a1c_combined_tail_cert.json"); c3 = d3["G2_constants"]
            ok &= d3["ALL_PASS"] and near(c3["c_J^R"], 0.5008, 1e-3) and near(c3["c_7^R"], 100.23, 1e-4) and near(c3["lead_combined"], 0.3720, 1e-3) and near(c3["sup|d|"], 0.2955, 1e-3) and c3["c_1"] == 0.261
            ok &= d3["G1"]["kappa_minus_d_eq_sqrt3_over_8"] and d3["G1"]["d_at_phases"] == ["-sqrt(3)/8"] * 3 + ["sqrt(3)/8"] * 3
            E3 = lambda a, M: max(d3["G3_table"][a][M][r]["E3"] for r in d3["G3_table"][a][M])
            ok &= near(E3("625", "1000"), 0.029, 2e-2) and near(E3("625", "10000"), 4.3e-3, 2e-2) and near(E3("625", "100000"), 4.5e-4, 2e-2) and near(E3("625", "1000000"), 4.7e-5, 2e-2) and near(E3("625", "10000000"), 5.8e-6, 5e-2)
            ok &= near(E3("625", "100000") * (625 + 100000), 45, 3e-2) and near(E3("1000", "100000") * (1000 + 100000), 52, 3e-2) and near(E3("2500", "100000") * (2500 + 100000), 69, 3e-2)
            ok &= max(s["ratio"] for o in d3["G4"]["orbits"] for s in o["slips"]) <= 0.855
            ok &= all(x in L for x in ("0.74850", "1.0753", "5.4646", "E'(a,M)\\le0.31", "c_\\delta=0.793", "1.9396", "c_J^R=0.5008", "c_7^R=100.23", "0.3720", "E'''=0.029"))
        if "A1CD" in groups:
            d = J("evidence/recog/a1c_so/a1c_start_offset_cert.json")
            ok &= d["ALL_PASS"] and near(d["G1"]["beta(625)"], 0.799, 1e-3) and near(d["G1"]["beta(1e6)"], 0.792, 1e-3) and near(d["G1"]["sup|Phi|"], 0.7734, 1e-3)
            dj = J("evidence/recog/a1c_joint/a1c_joint_transfer_cert.json"); H = [r["hulls"] for r in dj["records"]]
            ok &= dj["ALL_PASS"] and len(H) == 12 and all(dj["gates"].values())
            ok &= near(min(h["a_width"] for h in H), 4.8, 2e-2) and near(max(h["a_width"] for h in H), 21.4, 2e-2)
            ok &= near(min(h["omega_width"] for h in H), 1.63, 2e-2) and near(max(h["omega_width"] for h in H), 2.23, 2e-2)
            ok &= near(min(h["Theta0_width"] for h in H), 0.0044, 5e-2) and near(max(h["Theta0_width"] for h in H), 0.0226, 5e-2)
            ok &= near(min(h["L_width"] for h in H), 7.4e-5, 5e-2) and near(max(h["L_width"] for h in H), 2.8e-4, 5e-2)
            ok &= min(r["n_boxes_evaluated"] for r in dj["records"]) == 79 and max(r["n_boxes_evaluated"] for r in dj["records"]) == 353
            ok &= all(len(h["components"]) == 1 for h in H) and all(r["contains_a"] and r["contains_L"] and r["contains_theta"] for r in dj["records"])
            ok &= near(min(r["two_Delta_a"] for r in dj["records"]), 42.3, 1e-2) and near(max(r["two_Delta_a"] for r in dj["records"]), 84.5, 1e-2)
            d2 = J("evidence/recog/a1c_2/a1c_unknown_a_interval_cert.json"); W = [o["final"]["width"] for o in d2["orbits"]]
            ok &= d2["ALL_PASS"] and near(min(W), 173, 1e-2) and near(max(W), 965, 1e-2)
            ok &= all(x in L for x in ("$4.8$–$21.4$", "$173$–$965$", "$6$–$114$", "$1.6$–$2.2$", "$2\\Delta_a=42$–$85$", "$0.004$–$0.023$", "$79$–$353$", "\\beta(625)=0.799"))
        if "A1CQ" in groups:
            d = J("evidence/recog/a1c_3/a1c_q1prime_fiber_cert.json"); c = d["G2_constants"]
            ok &= d["ALL_PASS"] and c["cPsi(=bound/q*)"] <= 11.13 and near(c["cPsi(=bound/q*)"], 11.13, 1e-3) and near(c["Xi"], 0.027, 2e-2) and near(c["q*"], 256 / 140625, 1e-9)
            ok &= c["bound_|dTheta Psi_inf - 1|_at_q*"] <= 0.0203 and 0.975 <= min(d["G3_finite_difference_dPsi_dtheta"]["values"]) and max(d["G3_finite_difference_dPsi_dtheta"]["values"]) <= 1.045
            ok &= all(x in L for x in ("c_\\Psi=11.13", "\\Xi=0.027", "q^*=\\tfrac{256}{140625}", "\\le0.0203"))
    except Exception as ex:
        ok = False
        if verbose: print("    C19 exception:", repr(ex))
    gate("C19", ok, "VALUES")
    par = lambda s: [l for l in live(s).splitlines() if l.startswith("**Outbound notices; current state.**")]
    gate("C20", len(par(base)) == 1 and par(base) == par(inter), "NOTICES")
    glob = Counter(TAGBT.findall(inter)); glob.subtract(Counter(TAGBT.findall(base)))
    loc = Counter()
    for e in edits:
        loc.update(Counter(TAGBT.findall(e["new"]))); loc.subtract(Counter(TAGBT.findall(e["old"])))
    gate("C21", +glob == +loc and -glob == -loc, "TAG CENSUS")
    ok = True
    for rid, need in (("RECOG-THM-R9-SHARPENED-ROWS-C7", "C_7\\le85.1"), ("RECOG-ALG-A1C-TAIL-HARMONICS", "DYAD-THM-LPHASE-ROWA-REMAINDER"),
                      ("RECOG-THM-A1C-SHARPENED-SCHEDULE", "DYAD-THM-LPHASE-ROWA-REMAINDER"), ("RECOG-ALG-A1C-ADMISSIBLE-REGION", "(D5)"),
                      ("RECOG-ALG-A1C-JOINT-CONTRACTOR", "(D5)"), ("RECOG-ALG-A1C-START-OFFSET", "DYAD-THM-LPHASE-ROWA-REMAINDER")):
        if rid in new_rids:
            i = L.find(f"[RID: {rid}]", L.index("## §6.")); blk = L[i:L.find("\n", i)]
            m = re.search(r"`\[assuming: [^`]*\]`", blk)
            ok &= m is not None and need in m.group(0)
    for rid in ("RECOG-THM-R9-SHARPENED-ROWS", "RECOG-ALG-A1C-INBLOCK-ANGLE", "RECOG-ALG-A1C-COMBINED-TAIL", "RECOG-ALG-A1C-THRESHOLD-CODING", "RECOG-ALG-A1C-PHASE-C1-FIBER"):
        if rid in new_rids:
            i = L.find(f"[RID: {rid}]", L.index("## §6.")); blk = L[i:L.find("\n", i)]
            ok &= "`[assuming:" not in blk
    gate("C22", ok, "ASSUMING (source-conditioned blocks carry the qualifier; unconditional ones do not)")
    if "A1CE" in groups:
        s1 = section(inter, "## §1. Current Canonical State", "## §2. Active Frontier")
        i = s1.find("[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE]"); sent = s1[i:s1.find("$C_D$ depends", i)]
        j = L.find("[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE]", L.index("## §6.")); blk = L[j:L.find("\n`[NUM]`", j)]
        ok = i >= 0 and j >= 0 and "record-only centre" not in sent and "record-only centre" not in blk and "known-$a$ / declared-data centre" in sent and "known-$a$ / declared-data centre" in blk
        ok &= "nothing in this theorem is record-only" in blk
        if "A1CD" in groups:
            dec = [l for l in L.splitlines() if l.startswith("- A1c-decoder")]
            ok &= len(dec) == 1 and "not record-only" in dec[0] and "at least two usable slips" in dec[0] and "no Q1′ conclusion" in dec[0] and "`[assuming:]`" in dec[0]
        gate("C24", ok, "R83-1 (known-a centre never called record-only; decoder closure scoped)")
    ok = True
    newtext = "\n".join(e["new"] for e in edits)
    for p in set(RECPATH.findall(newtext)):
        ok &= os.path.exists(os.path.join(root, p))
    for fname, ver in set(RECVER.findall(s8)):
        ps = paths.get(fname, [])
        ok &= bool(ps) and any(re.search(r"\*\*Status:\*\*[^\n]*v" + re.escape(ver[1:]) + r"\b", open(p, encoding="utf-8").read()[:3000]) is not None for p in ps)
    gate("C23", ok, "RECORDS (paths exist; §8 record versions match the records' status lines)")
    return res

def controls(base, inter, log, root):
    print("\nNEGATIVE CONTROLS (each must be caught by its target gate):")
    files = repo_files(root)
    L = inter
    def once(s, a, b):
        assert s.count(a) >= 1, a
        return s.replace(a, b, 1)
    def swap(s, a, b):
        i, j = s.find(a), s.find(b); assert i >= 0 and j >= 0
        if i > j: a, b, i, j = b, a, j, i
        return s[:i] + b + s[i + len(a):j] + a + s[j + len(b):]
    def outside(s, a, b, anchor="### §6.7 Shear-Jet Law"):
        i = s.find(anchor); j = s.find(a, i); assert j > 0
        return s[:j] + b + s[j + len(a):]
    C = [
     ("NC01 new RID removed", "C7", once(L, "[RID: RECOG-ALG-A1C-COMBINED-TAIL] ", "")),
     ("NC02 RID attached to another statement", "C8", swap(L, "[RID: RECOG-THM-R9-COMPARATOR-INCOMPLETENESS]", "[RID: RECOG-ALG-LATTICE-MEMORY]")),
     ("NC03 bare [RESULT] reintroduced", "C9", once(L, "`[RESULT]` `[from: THM]` [RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT]", "`[RESULT]` [RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT]")),
     ("NC04 scope qualifier deleted", "C10", once(L, "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL] [scope: diagnostic twin $T_s$, SG-R4]", "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL]")),
     ("NC05 OPEN status altered (R4 closed)", "C6", once(L, "**OPEN R4 — Intrinsic type-change locus** [RID: RECOG-OPEN-TYPE-CHANGE]\n\nStatus: ACTIVE", "**OPEN R4 — Intrinsic type-change locus** [RID: RECOG-OPEN-TYPE-CHANGE]\n\nStatus: CLOSED")),
     ("NC06 header identity altered", "C14", once(L, "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.24", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.25")),
     ("NC07 READ/DECODE vocabulary inserted", "C11", once(L, "Owner editions that consume RECOG RIDs", "Owner editions that DECODE RECOG RIDs")),
     ("NC08 Appendix A history edited", "C3", once(L, "### v0.3.24 — 24 October 2026 — Adopted", "### v0.3.24 — 25 October 2026 — Adopted")),
     ("NC09 §8 quoted hash altered (full)", "C16", once(L, "`e964ec91cfed63a34a1f01b69bca97ba5d677a090d26d4b54f74432ae87eceff`", "`e964ec91cfed63a34a1f01b69bca97ba5d677a090d26d4b54f74432ae87ecefe`")),
     ("NC10 §8 quoted hash altered (abbreviated)", "C16", once(L, "(`1948acab…57a0`, `beabd7cc…6eb1`)", "(`1948acab…57a1`, `beabd7cc…6eb1`)")),
     ("NC11 §8 evidence file renamed", "C16", once(L, "`recog_a1c_q1prime_fiber_cert.py` (sha256", "`recog_a1c_q1prime_fiber_cert_v2.py` (sha256")),
     ("NC12 must-stay-live item deleted", "C17", L.replace("F2(a3)", "F2(a)")),
     ("NC13 Q1′ sub-item closed", "C17", once(L, "(retrospective reconstruction is not write-through) :: `[OPEN]`\n- A1c-decoder", "(retrospective reconstruction is not write-through) :: `[ALG]` ✓\n- A1c-decoder")),
     ("NC14 notice state changed", "C20", once(L, "G3 to OFN and G3 to RRF: prepared", "G3 to OFN and G3 to RRF: sent")),
     ("NC15 wrong value display (B1 row)", "C19", once(L, "$(C_2,q_{\\max})=(259.2,\\tfrac1{400})$", "$(C_2,q_{\\max})=(259.1,\\tfrac1{400})$")),
     ("NC16 wrong value display (A1c constant)", "C19", once(L, "c_J^R=0.5008", "c_J^R=0.5080")),
     ("NC17 heading changed", "C15", once(L, "### §6.12 Leading-Return Equivariance and Comparator Closure", "### §6.12 Leading-Return Equivariance")),
     ("NC18 grade changed outside the spans", "C21", outside(L, "`[ALG]`", "`[THM]`")),
     ("NC19 extra undeclared RECOG RID", "C7", once(L, "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE]", "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE-X]")),
     ("NC20 adopted R9 row altered", "C13", outside(L, "$(C_2,q_{\\max})=(517,\\tfrac1{400})$", "$(C_2,q_{\\max})=(163,\\tfrac1{400})$", anchor="#### §6.13a")),
     ("NC21 A1b theorem statement altered", "C13", once(L, "(B) *Alphabet.* Every gap is $6$ or $7$;", "(B) *Alphabet.* Every gap is $6$, $7$ or $8$;")),
     ("NC22 [assuming:] dropped from the C7 rows", "C22", once(L, "[scope: as RECOG-THM-R9-SHARPENED-ROWS] `[assuming: $C_7\\le85.1$ on $|z|\\le\\tfrac1{20}$ and $C_7\\le27.7$ on $|z|\\le\\tfrac1{40}$ — Dyadic's published DYAD-THM-NF-REM certificate values $85.07$ / $27.60$ rounded up; these are not Dyadic theorem statements; registration requested (§7)]`", "[scope: as RECOG-THM-R9-SHARPENED-ROWS]")),
     ("NC23 [assuming:] added to an unconditional block", "C22", once(L, "[RID: RECOG-ALG-A1C-INBLOCK-ANGLE] [scope:", "[RID: RECOG-ALG-A1C-INBLOCK-ANGLE] `[assuming: (D5)]` [scope:")),
     ("NC24 stale state restored (RID unavailable)", "C12", once(L, "[import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 | NUMGEN-RESULT-N5AS1-INF1]", "[import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6, INF-1 | RID unavailable]")),
     ("NC26 record-only centre reintroduced", "C24", once(L, "known-$a$ / declared-data centre $c" + "'" * 3 + "_k(a)=", "record-only centre $c" + "'" * 3 + "_k(a)=")),
     ("NC27 decoder closure scope dropped", "C24", once(L, "for records with at least two usable slips ($M_k\\ge1$), under the (D5) `[assuming:]` of the envelope;", "under the (D5) `[assuming:]` of the envelope;")),
     ("NC25 record version misstated in §8", "C23", once(L, "`RECOG_A1C_TAIL_AVERAGING_SESSION_v0_1.md` v0.2.1", "`RECOG_A1C_TAIL_AVERAGING_SESSION_v0_1.md` v0.3")),
    ]
    allok = True
    for name, target, mtxt in C:
        if mtxt == inter:
            print(f"  {name:<46} NOT CONSTRUCTED"); allok = False; continue
        r = check(base, mtxt, log, root, verbose=False, files=files)
        failed = sorted(k for k, v in r.items() if not v)
        hit = target in failed; allok &= hit
        print(f"  {name:<46} target {target}: {'caught' if hit else 'NOT CAUGHT'}  (failing: {', '.join(failed)})")
    return allok

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) != 3: print(__doc__); sys.exit(2)
    base = open(a[0], encoding="utf-8").read(); inter = open(a[1], encoding="utf-8").read()
    log = json.load(open(a[2], encoding="utf-8")); root = os.getcwd()
    print(f"base {hashlib.sha256(base.encode()).hexdigest()}\nintermediate {hashlib.sha256(inter.encode()).hexdigest()} (groups {','.join(log.get('groups', []))}, {len(log['edits'])} edits)")
    print("GATES:")
    r = check(base, inter, log, root)
    ok = all(r.values())
    if "--controls" in sys.argv: ok &= controls(base, inter, log, root)
    print("\nRESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
