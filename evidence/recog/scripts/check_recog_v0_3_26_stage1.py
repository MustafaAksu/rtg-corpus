#!/usr/bin/env python3
"""check_recog_v0_3_26_stage1.py -- deterministic checker for the RECOG v0.3.26 stage-1 intermediate (asymptotic correction + drift centring).

usage (from the repository root):
  python -I evidence/recog/scripts/check_recog_v0_3_26_stage1.py BASE INTERMEDIATE EDITLOG_JSON [--controls]
  BASE = `git show recog-v0.3.25:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`; EDITLOG_JSON written by the builder
  (any group variant: the gates read the declared groups from the log).
exit 0 = every gate PASS (and, with --controls, every negative control caught by its target gate).

Gates (as v0.3.25 stage 1 with the v0.3.26 declarations; C13 extended to the untouched parts of the two corrected blocks; C25 added):
  C0  BASE       base SHA-256 is the adopted v0.3.25 identity (tag recog-v0.3.25)
  C1  BUILD      intermediate == exact-once application of the logged edits (Appendix A masked for "live")
  C2  REVERSE    undoing every edit recovers the base byte-exactly
  C3  APPENDIX A Appendix A minus the new v0.3.26 entry is byte-identical to the base Appendix A
  C4  SPAN TAGS  edits whose backticked tag multiset changes are exactly the declared TAG_CHANGE edits
  C5  SPAN RIDS  no edit removes a [RID: X] declaration; added declarations are the declared new RIDs
  C6  STATUS     OPEN-registry "Status:" lines are byte-identical to the base (no status word, no history sentence changes)
  C7  RID SET    RECOG RID set == base set + the declared new RIDs of the built groups; none removed
  C8  RID ATTACH for every pre-existing RECOG RID declaration the after-text is unchanged; new RIDs attach to their
                 declared statements
  C9  RESULT     in §§1-6 every line-leading [RESULT] is followed by [from: TAG] with one canonical tag
  C10 QUALIFIERS no edit removes a qualifier; global change == sum of per-edit changes
  C11 VOCAB      no READ / WRITE / DECODE vocabulary introduced
  C12 IMPORTS    v0.3.25 import state kept (no "RID unavailable"; both NUMGEN RIDs; owner tag forms)
  C13 R9/A1B     the RECOG-THM-R9-MEMORY statement line, its row table, the (c) row table and the RECOG-THM-A1B-SLIP-SCHEDULE-U
                 statement (tag line through the proof sketch) are unchanged; the adopted rows (517, 163) stay in force; the
                 sharpened-schedule display line and the untouched items of TAIL-HARMONICS ((ii), the universal ceiling) are unchanged
  C14 HEADER     title, date, supersedes, status summary and footer unchanged
  C15 HEADINGS   heading lines equal the base
  C16 §8 FILES   every backticked file name in §8 exists in the repository; every SHA-256 (full or abbreviated 8…4) quoted in the
                 new §8 rows is the hash of the named repository file (directory references: a file of that directory)
  C17 LIVE       must-stay-live items present (F2(a3), W1-W5, R6 ACTIVE, registry-relative, no write-through); R4 ACTIVE;
                 the R6 sub-item A1c-Q1′ stays [OPEN]
  C18 DECOUPLE   each buildable variant (CORR, DRIFT, DRIFT+ENV, CORR+DRIFT) carries exactly its own new RIDs; ENV alone is refused
  C19 VALUES     the constants displayed in the new blocks agree with the certificate outputs in the repository
  C20 NOTICES    the §7.2 outbound-notices paragraph is unchanged (no notice state changed)
  C21 TAG CENSUS global backticked-tag multiset delta == sum of the per-edit deltas
  C22 ASSUMING   the log-free envelope carries a backticked [assuming:] naming DYAD-THM-LPHASE-ROWA-REMAINDER; the reciprocal-drift
                 block (adopted rows only) carries none
  C23 RECORDS    every records/recog path named in the new text exists; the review-accepted record versions named in §8 match
                 the records' own status lines
  C24 R83-1      the v0.3.25 wording persists: the known-a centre is never called "record-only"; the decoder closure line stays scoped
  C25 APPENDIX B (CORR) the two RETRACTED entries exist only in the intermediate, each with Reason / Replaced by / Version: v0.3.26,
                 the retracted count rises by exactly two, and the two corrected blocks carry their [COR] notes and point to Appendix B
"""
import hashlib, importlib.util, json, os, re, subprocess, sys, zipfile
from collections import Counter

BASE_SHA = "86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db"
PREV_TAG = "recog-v0.3.25"
APPA_START, APPA_END = "## Appendix A — Version History", "## Appendix B —"
NEW_RIDS = {
 "CORR": {"RECOG-ART-A1C-CORRECTED-GRID"},
 "DRIFT": {"RECOG-ALG-A1C-RECIPROCAL-DRIFT", "RECOG-ART-A1C-DRIFT-CENTERING"},
 "ENV": {"RECOG-ALG-A1C-LOGFREE-ENVELOPE"},
}
APPB_RIDS = {"RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325", "RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325"}   # Appendix B "[RETRACTED | RID: ...]" entries (CORR)
ATTACH = {
 "RECOG-ART-A1C-CORRECTED-GRID": " `[v0.3.26]` :: `recog_v0_3_26_corrected_grid.py`",
 "RECOG-ALG-A1C-RECIPROCAL-DRIFT": " [scope: $x_0\\in U$, chart row A, block base points; adopted rows only",
 "RECOG-ART-A1C-DRIFT-CENTERING": " `[v0.3.26]` :: `recog_a1c_drift_centering_cert.py`",
 "RECOG-ALG-A1C-LOGFREE-ENVELOPE": " [scope: as RECOG-THM-A1C-SHARPENED-SCHEDULE with the start offset enclosed",
}
TAG_CHANGE = {
 "S1-CORR": "§1 sentence ([COR] mention)", "S1-DRIFT": "§1 drift sentence (new [ALG])",
 "S613b-COR-TAIL-I": "TAIL-HARMONICS (i): [COR]", "S613b-COR-TAIL-III": "TAIL-HARMONICS (iii): [COR]", "S613b-COR-SCHED": "SHARPENED-SCHEDULE: [COR]",
 "S613b-DRIFT": "drift block (new [ALG], [NUM])", "S613b-ENV": "envelope block (new [ALG], [assuming:], [NUM])",
 "S8-DRIFT": "drift artifact row ([ALG], [COR], [NUM])", "S8-CORR": "corrected-grid artifact row ([COR])",
 "B-CORR": "Appendix B entries ([COR] mentions)", "A-1": "Appendix A entry quotes tags",
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
    p = os.path.join(root, "evidence/recog/scripts/build_recog_v0_3_26_stage1.py")
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
    i = ai.find("### v0.3.26"); j = ai.find("### v0.3.25", i)
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
    disp = lambda s_: [l for l in s_.splitlines() if l.startswith("$$c" + "'" * 3 + "_k(a):=")]
    ok &= len(disp(base)) == 1 and disp(base) == disp(inter)
    th_b = section(base, "`[ALG]` [RID: RECOG-ALG-A1C-TAIL-HARMONICS]", "\n`[ALG]` [RID: RECOG-ALG-A1C-INBLOCK-ANGLE]")
    th_i = section(inter, "`[ALG]` [RID: RECOG-ALG-A1C-TAIL-HARMONICS]", "\n`[ALG]` [RID: RECOG-ALG-A1C-INBLOCK-ANGLE]")
    keep = ("(ii) $Q_M\\le\\bar Q_M$ with $\\bar Q_M\\approx1/(a+M)$", "`[ALG via IA]` $E'(a,M)\\le0.31$ for every $a\\ge625$, $M\\ge1$")
    ok &= len(th_b) > 1000 and all(x in th_b and x in th_i for x in keep)
    gate("C13", ok, "R9/A1B statements, the schedule display and the untouched TAIL-HARMONICS items unchanged")
    hd = lambda s: ([l for l in s.splitlines()[:60] if l.startswith(("# ", "**Date:**", "**Supersedes:**", "**Title:**", "**Scope:**", "**Status summary", "**Document status"))] + s.splitlines()[-3:])
    gate("C14", hd(base) == hd(inter), "HEADER")
    hs = lambda s: [l for l in s.splitlines() if l.startswith("#")]
    gate("C15", hs(live(base)) == hs(live(inter)), "HEADINGS")
    s8 = section(inter, "## §8. Artifact", "## §9.")
    names = set(re.findall(r"`([A-Za-z0-9_.\-]+\.(?:py|json|jsonl|md|txt|zip))`", s8)) | {os.path.basename(x) for x in re.findall(r"`((?:evidence|records)/[^`]+\.(?:py|json|jsonl|md|txt))`", s8)}
    fl, paths = files if files is not None else repo_files(root)
    miss = sorted(n for n in names if n not in fl and n not in FILE_EXCEPT)
    hashok = True; nh = 0
    for row in [l for l in s8.splitlines() if "`[v0.3.26]`" in l]:
        for ref, h1, h2 in HASHREF.findall(row):
            for h in (h1, h2):
                if not h: continue
                nh += 1
                if ref.endswith("/"):
                    d = os.path.join(root, ref); cands = [os.path.join(d, f) for f in os.listdir(d)] if os.path.isdir(d) else []
                else:
                    cands = paths.get(os.path.basename(ref), [])
                hashok &= any(hmatch(h, sha(p)) for p in cands)
    gate("C16", not miss and hashok and nh >= 2 * len(groups), f"§8 FILES missing: {miss}" if miss else (f"§8 FILES ({nh} hashes checked)" if hashok else "§8 FILES: quoted hash mismatch"))
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
        for gs in (("CORR",), ("DRIFT",), ("DRIFT", "ENV"), ("CORR", "DRIFT")):
            eds = [e for e in m.EDITS if e[1] in gs] + [m.appa_edit(set(gs))]
            t, _ = m.apply(base, eds)
            ok &= set(RID_RECOG.findall(t)) == set(RID_RECOG.findall(base)) | set().union(*(NEW_RIDS[g] for g in gs))
        refused = False
        try:
            m.main(["b", os.path.join(root, "evidence/recog/v0.3.26/base_v0_3_25.md"), os.devnull, os.devnull, "--only", "ENV"])
        except AssertionError:
            refused = True
        ok &= refused
    except AssertionError:
        ok = False
    gate("C18", ok, "DECOUPLE")
    ok = True
    try:
        J = lambda p: json.load(open(os.path.join(root, p)))
        dd = J("evidence/recog/a1c_drift/a1c_drift_centering_cert.json"); cg = J("evidence/recog/v0.3.26/corrected_grid.json")
        ok &= dd["ALL_PASS"] and cg["all_below"] is True and all(dd["gates"].values())
        if "CORR" in groups:
            g = cg["grid"]["625"]
            ok &= near(g["1000"]["E3_corr_worst_r"], 0.029, 2e-2) and near(g["10000"]["E3_corr_worst_r"], 4.3e-3, 2e-2) and near(g["100000"]["E3_corr_worst_r"], 4.5e-4, 2e-2)
            ok &= near(g["1000000"]["E3_corr_worst_r"], 4.6e-5, 2e-2) and near(g["10000000"]["E3_corr_worst_r"], 4.7e-6, 2e-2)
            ok &= near(g["1000000"]["E3_old_worst_r"], 4.7e-5, 2e-2) and near(g["10000000"]["E3_old_worst_r"], 5.8e-6, 2e-2)
            ok &= all(cg["grid"][a][M]["E3_corr_worst_r"] <= cg["grid"][a][M]["E3_old_worst_r"] for a in cg["grid"] for M in cg["grid"][a])
            ok &= near(cg["grid"]["625"]["100000"]["E3_corr_scaled"], 45, 3e-2) and near(cg["grid"]["1000"]["100000"]["E3_corr_scaled"], 52, 3e-2) and near(cg["grid"]["2500"]["100000"]["E3_corr_scaled"], 69, 3e-2)
            for a in ("625", "1000", "2500"):
                A = cg["asymptotic"][a]["10000000000000"]
                ok &= near(A["Sbar_corr_sqrt"], 0.74850, 2e-4) and near(A["Rbar_corr_sqrt"], 1.0753, 2e-4) and near(A["Eprime_corr_sqrt"], 5.4646, 2e-4) and A["E3_corr_sqrt"] < 1e-4 and A["E3_old_sqrt"] > 0.1
            ok &= near(cg["asymptotic"]["625"]["1000000000"]["E3_corr_scaled_over_log"], 2.2, 5e-2) and near(cg["asymptotic"]["625"]["10000000000000"]["E3_corr_scaled_over_log"], 1.7, 5e-2)
            ok &= near(dd["G3c_asymptotics"]["625"]["10000000000000"]["Sbar_old*sqrt"], 4.0, 2e-2) and near(dd["G3c_asymptotics"]["625"]["10000000000000"]["ref_d_old*sqrt"], 1.45e-4, 2e-2)
            ok &= all(v["ok"] and v["Lg_corr"][1] <= v["Lg_old"] and v["Lg_corr"][0] >= v["brute"] * (1 - 1e-12) for v in dd["G3b_Lg_corr"].values())
            ok &= all(x in L for x in ("$4.6\\times10^{-5}$ at $10^6$, $4.7\\times10^{-6}$ at $10^7$ (v0.3.25 forms: $4.7\\times10^{-5}$, $5.8\\times10^{-6}$)", "decreases from $2.2$ to $1.7$", "$\\bar S'\\sqrt{a+M}=4.0$ at $M=10^{13}$", "$1.45\\times10^{-4}(a+M)^{-1/2}$", "$1.1\\times10^{-6}$ at $a=625$"))
        if "DRIFT" in groups:
            c = dd["G2_constants"]; K = c["K_eps"]
            ok &= near(c["gamma2"], 212.6, 1e-3) and c["gamma2_C7_share"] == 200.0 and near(c["29/216"], 29 / 216, 1e-12)
            ok &= near(K["625"]["K"], 0.7203, 1e-3) and near(K["1000"]["K"], 0.4513, 1e-3) and near(K["2500"]["K"], 0.1860, 1e-3) and K["625"]["gamma2_part"] / K["625"]["K"] > 0.97
            ok &= all(dd["G1"].values()) and all(v["ok"] for v in dd["G3a_Lambda_log"].values())
            jet = dd["G4_jet_model"]; sd = [v["sup_drift"] for v in jet.values()]
            ok &= len(jet) == 12 and near(min(sd), 0.0066, 3e-2) and near(max(sd), 0.0113, 3e-2) and max(v["ratio"] for v in jet.values()) <= 0.061 and all(v["ok"] for v in jet.values())
            ok &= near(max(v["old_epsbar_at_N"] for v in jet.values()), 2.6, 5e-2)
            ok &= dd["NC1"]["uncentred_drift_exceeds_K"] is True and dd["NC2"]["wrong_sign_drift_exceeds_K"] is True
            ok &= all(x in L for x in ("$\\gamma_2=212.6$", "$K_\\epsilon=0.7203$, $0.4513$, $0.1860$", "\\tilde b_m|=0.0066$–$0.0113$", "-\\tfrac{29}{216}q_m-2\\operatorname{Re}(a_{05}e^{-6i\\Theta_m})q_m+R_m$", "every $m\\ge0$ and every admissible $b\\in[b'", "rows D1–D8"))
            pt = J("evidence/recog/a1c_drift/a1c_drift_proof_table_cert.json"); ok &= pt["ALL_PASS"] and all(pt["gates"].values()) and pt["imports"]["recog_a1c_drift_centering_cert.py"] == hashlib.sha256(open(os.path.join(root, "evidence/recog/scripts/recog_a1c_drift_centering_cert.py"), "rb").read()).hexdigest()
            ok &= all(abs(pt["PT1"][a]["K_from_rows"] - pt["PT1"][a]["K_cert"]) <= 1e-12 for a in ("625", "2500"))
        if "ENV" in groups:
            A = dd["G3c_asymptotics"]
            vals = [A["625"][M]["E5*n"] for M in ("10000", "100000", "1000000", "10000000", "1000000000", "100000000000", "10000000000000")]
            ok &= all(near(v, t, 5e-3) for v, t in zip(vals, (20.6, 19.6, 19.3, 19.2, 19.15, 19.15, 19.15))) and near(A["2500"]["10000000000000"]["E5*n"], 18.53, 2e-3)
            ok &= all(near(A["625"][M]["E4*n"], t, 3e-2) for M, t in (("10000", 21.9), ("100000", 21.9), ("1000000", 23.7), ("10000000", 34.9), ("1000000000", 1153), ("100000000000", 1.1e5), ("10000000000000", 1.1e7)))
            ok &= dd["G3c_E5n_rises_from_1e4"] == {"625": False, "2500": False}
            g5 = dd["G5"]; ok &= g5["n_slips"] == 73 and g5["slips_with_gain_gt_1"] == 73 and g5["N_steps"] == 1800000 and len(g5["orbits"]) == 12
            ok &= near(g5["min_gain"], 1.02, 1e-2) and near(g5["max_gain"], 1.87, 1e-2) and near(g5["max_ratio5_with_tol"], 0.79, 2e-2) and near(g5["max_ratio5"], 10.7, 2e-2)
            ok &= all(sl["ok"] for o in g5["orbits"] for sl in o["slips"])
            ok &= all(x in L for x in ("$E^{(5)}(a+M)=20.6,19.6,19.3,19.2,19.15,19.15,19.15$", "$18.53$ at $a=2500$", "$E^{(4)}(a+M)=21.9,21.9,23.7,34.9,1153,1.1\\times10^5,1.1\\times10^7$", "$73/73$", "ratio $10.7$ without it", "gains $E^{(4)}/E^{(5)}=1.02$–$1.87$ ($73/73>1$)", "$C(a,r)=\\sum_ic_i=58.0$, $61.0$, $75.1$ at $r=5$", "ten non-negative terms"))
            pt = J("evidence/recog/a1c_drift/a1c_drift_proof_table_cert.json"); ok &= pt["ALL_PASS"] and len(pt["PT3_M_sample"]) == 28 and pt["PT3_M_sample"][0] == 1 and pt["PT3_M_sample"][-1] == 10**13
            ok &= all(near(pt["PT3"][f"a={a},r=5"]["C_total"], t, 2e-3) for a, t in (("625", 58.0), ("1000", 61.0), ("2500", 75.1))) and all(v["worst_E5n_over_C"] <= 1 for v in pt["PT3"].values())
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
    for rid, need in (("RECOG-ALG-A1C-LOGFREE-ENVELOPE", "DYAD-THM-LPHASE-ROWA-REMAINDER"),):
        if rid in new_rids:
            i = L.find(f"[RID: {rid}]", L.index("## §6.")); blk = L[i:L.find("\n", i)]
            m = re.search(r"`\[assuming: [^`]*\]`", blk)
            ok &= m is not None and need in m.group(0)
    for rid in ("RECOG-ALG-A1C-RECIPROCAL-DRIFT",):
        if rid in new_rids:
            i = L.find(f"[RID: {rid}]", L.index("## §6.")); blk = L[i:L.find("\n", i)]
            ok &= "`[assuming:" not in blk and "no (D5)" not in blk
    gate("C22", ok, "ASSUMING (source-conditioned blocks carry the qualifier; unconditional ones do not)")
    if True:
        s1 = section(inter, "## §1. Current Canonical State", "## §2. Active Frontier")
        i = s1.find("[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE]"); sent = s1[i:s1.find("$C_D$ depends", i)]
        j = L.find("[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE]", L.index("## §6.")); blk = L[j:L.find("\n`[NUM]`", j)]
        ok = i >= 0 and j >= 0 and "record-only centre" not in sent and "record-only centre" not in blk and "known-$a$ / declared-data centre" in sent and "known-$a$ / declared-data centre" in blk
        ok &= "nothing in this theorem is record-only" in blk
        if True:
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
    if "CORR" in groups:
        appb_b, appb_i = base[base.index(APPA_END):], inter[inter.index(APPA_END):]
        ok = all(f"**[RETRACTED | RID: {r}]**" in appb_i for r in APPB_RIDS) and not any(r in appb_b for r in APPB_RIDS)
        for r in APPB_RIDS:
            if f"**[RETRACTED | RID: {r}]**" in appb_i:
                i = appb_i.index(f"**[RETRACTED | RID: {r}]**"); ent = appb_i[i:appb_i.find("\n", i)]
                ok &= all(x in ent for x in ("Reason", "Replaced by:", "Version: v0.3.26.")) and ("CORR-1" in ent)
        ok &= appb_i.count("**[RETRACTED | RID: RECOG-") == appb_b.count("**[RETRACTED | RID: RECOG-") + 2
        ok &= appb_i.count("**[") == appb_b.count("**[") + 2
        th = section(inter, "`[ALG]` [RID: RECOG-ALG-A1C-TAIL-HARMONICS]", "\n`[ALG]` [RID: RECOG-ALG-A1C-INBLOCK-ANGLE]")
        sc = section(inter[inter.index("#### §6.13b"):], "`[THM]` [RID: RECOG-THM-A1C-SHARPENED-SCHEDULE]", "\n`[NUM]`")
        ok &= th.count("`[COR]`") == 2 and sc.count("`[COR]`") == 1 and inter.count("`[COR]`") - base.count("`[COR]`") >= 3
        ok &= all(r in th or r in sc for r in APPB_RIDS) and "Appendix B" in th and "Appendix B" in sc
        gate("C25", ok, "APPENDIX B (two RETRACTED entries with reason / replacement / version; [COR] notes in the two corrected blocks)")
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
     ("NC01 new RID removed", "C7", once(L, "[RID: RECOG-ALG-A1C-RECIPROCAL-DRIFT] ", "")),
     ("NC02 RID attached to another statement", "C8", swap(L, "[RID: RECOG-THM-R9-COMPARATOR-INCOMPLETENESS]", "[RID: RECOG-ALG-LATTICE-MEMORY]")),
     ("NC03 bare [RESULT] reintroduced", "C9", once(L, "`[RESULT]` `[from: THM]` [RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT]", "`[RESULT]` [RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT]")),
     ("NC04 scope qualifier deleted", "C10", once(L, "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL] [scope: diagnostic twin $T_s$, SG-R4]", "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL]")),
     ("NC05 OPEN status altered (R4 closed)", "C6", once(L, "**OPEN R4 — Intrinsic type-change locus** [RID: RECOG-OPEN-TYPE-CHANGE]\n\nStatus: ACTIVE", "**OPEN R4 — Intrinsic type-change locus** [RID: RECOG-OPEN-TYPE-CHANGE]\n\nStatus: CLOSED")),
     ("NC06 header identity altered", "C14", once(L, "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.25", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.26")),
     ("NC07 READ/DECODE vocabulary inserted", "C11", once(L, "Owner editions that consume RECOG RIDs", "Owner editions that DECODE RECOG RIDs")),
     ("NC08 Appendix A history edited", "C3", once(L, "### v0.3.25 — 27 October 2026 — Adopted", "### v0.3.25 — 28 October 2026 — Adopted")),
     ("NC09 §8 quoted hash altered (full)", "C16", once(L, "`69edfebd9f4ca981ac012e4906de6ed677f9e2acf77927ee58e1ed87f49ca0b8`", "`69edfebd9f4ca981ac012e4906de6ed677f9e2acf77927ee58e1ed87f49ca0b9`")),
     ("NC10 §8 quoted hash altered (abbreviated)", "C16", once(L, "(`cbf0e806…fc80`, `c9e2b2f0…6058`)", "(`cbf0e806…fc81`, `c9e2b2f0…6058`)")),
     ("NC11 §8 evidence file renamed", "C16", once(L, "`recog_v0_3_26_corrected_grid.py` (sha256", "`recog_v0_3_26_corrected_grid_v2.py` (sha256")),
     ("NC12 must-stay-live item deleted", "C17", L.replace("F2(a3)", "F2(a)")),
     ("NC13 Q1′ sub-item closed", "C17", once(L, "(retrospective reconstruction is not write-through) :: `[OPEN]`\n- A1c-decoder", "(retrospective reconstruction is not write-through) :: `[ALG]` ✓\n- A1c-decoder")),
     ("NC14 notice state changed", "C20", once(L, "G3 to OFN and G3 to RRF: prepared", "G3 to OFN and G3 to RRF: sent")),
     ("NC15 wrong value display (corrected grid)", "C19", once(L, "$4.6\\times10^{-5}$ at $10^6$, $4.7\\times10^{-6}$ at $10^7$", "$4.6\\times10^{-5}$ at $10^6$, $5.8\\times10^{-6}$ at $10^7$")),
     ("NC16 wrong value display (K_eps)", "C19", once(L, "$K_\\epsilon=0.7203$, $0.4513$, $0.1860$", "$K_\\epsilon=0.7023$, $0.4513$, $0.1860$")),
     ("NC33 wrong value display (all-M constants)", "C19", once(L, "$C(a,r)=\\sum_ic_i=58.0$, $61.0$, $75.1$ at $r=5$", "$C(a,r)=\\sum_ic_i=58.0$, $61.0$, $57.1$ at $r=5$")),
     ("NC17 heading changed", "C15", once(L, "### §6.12 Leading-Return Equivariance and Comparator Closure", "### §6.12 Leading-Return Equivariance")),
     ("NC18 grade changed outside the spans", "C21", outside(L, "`[ALG]`", "`[THM]`")),
     ("NC19 extra undeclared RECOG RID", "C7", once(L, "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE]", "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE-X]")),
     ("NC20 adopted R9 row altered", "C13", outside(L, "$(C_2,q_{\\max})=(517,\\tfrac1{400})$", "$(C_2,q_{\\max})=(163,\\tfrac1{400})$", anchor="#### §6.13a")),
     ("NC21 schedule display altered", "C13", once(L, "$$c" + "'" * 3 + "_k(a):=\\tau\\,\\psi(a+M_k)-(k-1)\\tfrac\\pi3+\\tfrac{\\sqrt3}8(a+M_k)^{-1/2}", "$$c" + "'" * 3 + "_k(a):=\\tau\\,\\psi(a+M_k)-(k-1)\\tfrac\\pi3+\\tfrac{\\sqrt3}4(a+M_k)^{-1/2}")),
     ("NC22 universal ceiling altered in TAIL-HARMONICS", "C13", once(L, "`[ALG via IA]` $E'(a,M)\\le0.31$ for every $a\\ge625$, $M\\ge1$", "`[ALG via IA]` $E'(a,M)\\le0.30$ for every $a\\ge625$, $M\\ge1$")),
     ("NC23 [assuming:] dropped from the envelope", "C22", once(L, "$a$ known] `[assuming: Dyadic row-A bridge constants $c_Q=0.79246$, $c'_Q=0.36915$ ($|D_Q|\\le c_Qq^{3/2}$, $|D_Q-D_3|\\le c'_Qq^2$) and the remainder decomposition $r=\\Lambda_3+{\\rm rest}$ with its constants, as published in the proof of DYAD-THM-LPHASE-ROWA-REMAINDER (certified by DYAD-ART-LPHASE-ROWA); proof constants, not theorem rows; registration requested (§7)]` [proof: cell v0.3 §3 (Cor. 24)", "$a$ known] [proof: cell v0.3 §3 (Cor. 24)")),
     ("NC24 [assuming:] added to the unconditional drift block", "C22", once(L, "[RID: RECOG-ALG-A1C-RECIPROCAL-DRIFT] [scope:", "[RID: RECOG-ALG-A1C-RECIPROCAL-DRIFT] `[assuming: (D5)]` [scope:")),
     ("NC25 stale state restored (RID unavailable)", "C12", once(L, "[import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 | NUMGEN-RESULT-N5AS1-INF1]", "[import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6, INF-1 | RID unavailable]")),
     ("NC26 record version misstated in §8", "C23", once(L, "`RECOG_A1C_DRIFT_CENTERING_SESSION_v0_1.md` v0.3", "`RECOG_A1C_DRIFT_CENTERING_SESSION_v0_1.md` v0.4")),
     ("NC27 record-only centre reintroduced", "C24", once(L, "known-$a$ / declared-data centre $c" + "'" * 3 + "_k(a)=", "record-only centre $c" + "'" * 3 + "_k(a)=")),
     ("NC28 Appendix B entry without its reason", "C25", once(L, "Reason (CORR-1, CORR-2): the envelope's term", "Note: the envelope's term")),
     ("NC29 Appendix B entry without its version", "C25", once(L, "stated in §6.13b with `[COR]`. Version: v0.3.26.\n\n**[RETRACTED | RID: RECOG-THM", "stated in §6.13b with `[COR]`.\n\n**[RETRACTED | RID: RECOG-THM")),
     ("NC30 [COR] note removed from the corrected block", "C25", once(L, "— `[COR]` (v0.3.26) these limits hold for the **corrected** closed forms", "— (v0.3.26) these limits hold for the **corrected** closed forms")),
     ("NC31 Appendix B entry deleted", "C25", L[:L.index("\n\n**[RETRACTED | RID: RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325]**")] + L[L.index("\n", L.index("**[RETRACTED | RID: RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325]**")):]),
     ("NC32 wrong value display (E5 grid)", "C19", once(L, "$E^{(5)}(a+M)=20.6,19.6,19.3,19.2,19.15,19.15,19.15$", "$E^{(5)}(a+M)=20.6,19.6,19.3,19.2,19.15,19.15,19.10$")),
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
