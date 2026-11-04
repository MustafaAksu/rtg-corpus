#!/usr/bin/env python3
"""check_recog_v0_3_27_stage1.py -- deterministic checker for the RECOG v0.3.27 stage-1 intermediate (inbox round after v0.3.26).

usage (from the repository root, after the owner rerun is in the working tree):
  python -I evidence/recog/scripts/check_recog_v0_3_27_stage1.py BASE INTERMEDIATE EDITLOG_JSON [--controls]
  BASE = `git show recog-v0.3.26:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`; EDITLOG_JSON written by the builder (any group variant).
exit 0 = every gate PASS (and, with --controls, every negative control caught by its target gate).

Gates (C0-C24 as v0.3.26 stage 1, adapted; C10 admits the declared qualifier replacements of R2/R3; C25-C28 new):
  C0  BASE       base SHA-256 is the adopted v0.3.26 identity (tag recog-v0.3.26)
  C1  BUILD      intermediate == exact-once application of the logged edits (Appendix A masked for "live")
  C2  REVERSE    undoing every edit recovers the base byte-exactly
  C3  APPENDIX A Appendix A minus the new v0.3.27 entry is byte-identical to the base Appendix A
  C4  SPAN TAGS  edits whose backticked tag multiset changes are exactly the declared TAG_CHANGE edits
  C5  SPAN RIDS  no edit removes a [RID: X]; added declarations are the declared new RECOG RIDs or the three Dyadic §7 rows
  C6  STATUS     OPEN-registry "Status:" lines byte-identical to the base
  C7  RID SET    RECOG RID set == base set + declared new RIDs of the built groups
  C8  RID ATTACH pre-existing RECOG RID after-texts unchanged; new RIDs attach to their declared statements
  C9  RESULT     every line-leading [RESULT] in §§1-6 carries one canonical [from: TAG]
  C10 QUALIFIERS qualifiers are removed only by the declared replacement edits (R2 sites, R3 C7 row), each of which adds an
                 [import:]; global change == sum of per-edit changes
  C11 VOCAB      no READ / WRITE / DECODE vocabulary introduced
  C12 IMPORTS    v0.3.26 import state kept; with D5B/D5A the bridge and spiral-remainder theorems are imported at all six A1c sites
                 and have §7 rows; with C7 the C7-SHARP theorem is imported at RECOG-THM-R9-SHARPENED-ROWS-C7 and has a §7 row
  C13 UNCHANGED  R9 statement and rows, the (c) rows, RECOG-THM-A1B-SLIP-SCHEDULE-U, the schedule display, the untouched
                 TAIL-HARMONICS items, the A1c-Q1′ line, the B1 theorem formula $q_0<|G|/C_2$ and every certificate script except part-1b L55
  C14 HEADER     title, date, supersedes, status summary and footer unchanged
  C15 HEADINGS   heading lines equal the base
  C16 §8 FILES   every backticked file in §8 exists; every hash quoted in rows marked `[v0.3.27]` is that file's hash in the working tree
  C17 LIVE       must-stay-live items present; R4, R6 ACTIVE; A1c-Q1′ [OPEN]
  C18 DECOUPLE   variants R1+D5B, R1+D5A, C7, DISP, PIN each carry exactly their own new RIDs; R1 alone, D5B alone, D5A alone and
                 D5B+D5A are refused
  C19 VALUES     (R1) the part-1b literal is 0.36916 and every rerun A1c certificate and the corrected grid pass; (D5B) the jet
                 certificate passes with c_J < 0.500819 < 0.50220 and c_7 < 100.231 < 157.58 and these ceilings are the ones printed
  C20 NOTICES    the §7.2 outbound-notices paragraph is unchanged
  C21 TAG CENSUS global backticked-tag delta == sum of per-edit deltas
  C22 ASSUMING   no group: the (D5) qualifier stands at all six sites; D5B: no [assuming:] and no (D5) wording remains at the six sites,
                 §1 or the decoder line; D5A: each of the six sites carries the narrowed [assuming:] naming c_J = 0.50220 and c_7 = 157.58
  C23 RECORDS    every records/recog path named in the new text exists
  C24 R83-1      the known-a centre is never called "record-only"; the decoder line stays scoped (its [assuming:] only without D5B)
  C25 APPENDIX B byte-identical to the base (no claim withdrawn in this edition)
  C26 DIRECTION  every displayed ceiling >= its certified value, every displayed window <= its certified window (certificate JSONs in the
                 working tree; 24 displays); with DISP the eight corrected displays carry `[COR]` and the old forms are gone
  C27 PINS       (PIN) live current-use Dyadic and NUMGEN citations at dyad-v6.4.23 / numgen-v1.21; remaining old pins only on the
                 listed provenance / historical lines; the GAP-LOCK row cites NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO
  C28 C7 ROWS    (C7) no [assuming:] ceiling on C_7 remains; the stale "published certificate values" wording is gone
"""
import hashlib, importlib.util, json, os, re, sys, tempfile, zipfile
from collections import Counter
from decimal import Decimal, getcontext

BASE_SHA = "45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34"
PREV_TAG = "recog-v0.3.26"
APPA_START, APPA_END = "## Appendix A — Version History", "## Appendix B —"
NEW_RIDS = {"R1": set(), "D5B": {"RECOG-ALG-A1C-JET-REMAINDER-BOUNDS", "RECOG-ART-A1C-JET-REMAINDER-BOUNDS"}, "D5A": set(), "C7": set(), "DISP": set(), "PIN": set()}
ATTACH = {"RECOG-ALG-A1C-JET-REMAINDER-BOUNDS": " [scope: chart of DYAD-ALG-NF6 and DYAD-THM-NF-REM, $0<q=|z|^2\\le q^*",
          "RECOG-ART-A1C-JET-REMAINDER-BOUNDS": " `[v0.3.27]` :: `recog_a1c_jet_remainder_bounds_cert.py`"}
# RIDs whose qualifier directly after the RID / scope is replaced by a declared edit (C8 compares their [scope:] prefix only)
REQUAL = {"R1": set(), "D5B": {"RECOG-ALG-A1C-TAIL-HARMONICS", "RECOG-THM-A1C-SHARPENED-SCHEDULE", "RECOG-ALG-A1C-LOGFREE-ENVELOPE", "RECOG-ALG-A1C-ADMISSIBLE-REGION", "RECOG-ALG-A1C-JOINT-CONTRACTOR"},
          "C7": {"RECOG-THM-R9-SHARPENED-ROWS-C7"}, "DISP": set(), "PIN": set()}
REQUAL["D5A"] = REQUAL["D5B"]
IMPORT_RIDS_ALLOWED = {"DYAD-THM-LPHASE-ROWA-BRIDGE", "DYAD-THM-OPEN3-SPIRAL-REM", "DYAD-THM-NF-REM-C7-SHARP"}
SITES = ("TAIL", "SCHED", "ENV", "SO", "ADM", "JC")
TAG_CHANGE = {f"{g}-{s}" for g in ("D5B", "D5A") for s in SITES if s not in ("ADM", "JC")} | {"D5B-S7-LPH", "D5A-S7-LPH", "D5B-JET", "D5B-S8-JET", "A-1", "PIN-GAP"} | {
    "DISP-KEPS", "DISP-C7R", "DISP-G0", "DISP-BETA", "DISP-KPHI", "DISP-WIN"}
QUAL_CHANGE = {f"{g}-{s}" for g in ("D5B", "D5A") for s in SITES} | {"C7-Q"}
# §1 summary qualifiers: removed (D5B, the (D5) qualifier discharged) or narrowed (D5A) without an [import:] in the same span
QUAL_DISCHARGE = {"D5B-S1-SCHED", "D5B-S1-ENV", "D5A-S1-SCHED", "D5A-S1-ENV"}
FILE_EXCEPT = {"dyad_referee_p2b_v2.py"}
CANON = {"DEF", "THM", "ALG", "ALG via IA", "THM-ALG via IA", "ENG", "NUM", "NUM strong", "OBS", "HEUR", "HEUR strong", "HYP", "ALG candidate", "ALG structure"}
TAGBT = re.compile(r"`\[[A-Z][^`\]]*\]`")
RID_RECOG = re.compile(r"\[RID: (RECOG-[A-Z0-9-]*[A-Z0-9])")
ANYRID = re.compile(r"\[RID: ([A-Z][A-Z0-9-]*[A-Z0-9])")
VOCAB = re.compile(r"\b(READ|WRITE|DECODE)\b")
RESULT_LEAD = re.compile(r"^(?:`\[RESULT\]`|\[RESULT\])")
FROM = re.compile(r"^(?:`\[RESULT\]`|\[RESULT\])\s*(?:`\[from: ([^`\]]+)\]`|\[from: ([^\]]+)\])")
QUAL = re.compile(r"\[(?:scope|assumes|assuming): [^\]]*\]")
HASHREF = re.compile(r"`((?:evidence|records)/[^`]+/|(?:[A-Za-z0-9_.\-/]*/)?[A-Za-z0-9_.\-]+\.(?:py|json|md|txt))`(?: v0\.[0-9.]+)?(?: \((?:sha256 )?`([0-9a-f]{8}…[0-9a-f]{4}|[0-9a-f]{64})`(?:, `([0-9a-f]{8}…[0-9a-f]{4}|[0-9a-f]{64})`)?\))?")
RECPATH = re.compile(r"`(records/recog/[A-Za-z0-9_./-]+\.md)`")
OLD_Q = "`[assuming: Dyadic row-A bridge constants $c_Q=0.79246$, $c'_Q=0.36915$"
OLD_QS = "`[assuming: the Dyadic (D5) row-A bridge proof constants, as RECOG-THM-A1C-SHARPENED-SCHEDULE]`"
SITE_ANCHOR = {"TAIL": "[RID: RECOG-ALG-A1C-TAIL-HARMONICS] [scope:", "SCHED": "[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE] [scope:",
               "ENV": "[RID: RECOG-ALG-A1C-LOGFREE-ENVELOPE] [scope:", "SO": "(ii) *Signed start offset* ",
               "ADM": "[RID: RECOG-ALG-A1C-ADMISSIBLE-REGION] [scope:", "JC": "[RID: RECOG-ALG-A1C-JOINT-CONTRACTOR] [scope:"}
# lines that keep an earlier Dyadic / NUMGEN / companion pin after PIN (provenance, historical audits, receipts, consumer inventory)
PIN_KEEP = ("  - v0.3.21 (receipt, no import)", "- [RID: (none — Genesis §6.1);",
            "- [RID: GEN-", "- [RID: NUMGEN-THM-N", "- [RID: OFN §6.2a, §", "- [RID: NUMGEN-DEF-N", "Historical audit", "- G2 (v0.3.21",
            "- [RID: DYAD-THM-OPEN3-ASYMPTOTIC-PHASE", "- RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION", "Owner editions that consume RECOG RIDs",
            "| RECOG-", "| RECOG §§", "- [RID: RECOG-ART-", "- **",
            "- [RID: (none — Genesis §6.6 $J_Q$)]", "| N11 (v6.4.15)", "| N13 (v6.4.17)")
OLD_PINS = ("6.4.22", "1.20.8", "v2.8.9", "Genesis v2.8", "OFN v0.10", "ofn-v0.10", "FOUNDATIONS v0.10", "2.12.13")

def split_appa(s):
    i, j = s.index(APPA_START), s.index(APPA_END); return s[:i], s[i:j], s[j:]
def live(s):
    a, _, c = split_appa(s); return a + c
def section(s, start, end):
    i = s.find(start); j = s.find(end, i + 1); return s[i:j] if i >= 0 and j > i else ""
def line_at(s, anchor, start=0):
    i = s.find(anchor, start)
    if i < 0: return ""
    a = s.rfind("\n", 0, i) + 1; b = s.find("\n", i); return s[a:len(s) if b < 0 else b]
def apply_log(base, edits, reverse=False):
    a, appa, c = split_appa(base); lv = a + "\x00APPA\x00" + c
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
    p = os.path.join(root, "evidence/recog/scripts/build_recog_v0_3_27_stage1.py")
    spec = importlib.util.spec_from_file_location("b27", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def hmatch(h, full): return full == h if len(h) == 64 else (full.startswith(h[:8]) and full.endswith(h[-4:]))

def direction_rows(root):
    """(name, kind, display in v0.3.26, display after DISP or None if unchanged, printed value after DISP, certified value)"""
    J = lambda p: json.load(open(os.path.join(root, p)))
    dd = J("evidence/recog/a1c_drift/a1c_drift_centering_cert.json"); pt = J("evidence/recog/a1c_drift/a1c_drift_proof_table_cert.json")
    ct = J("evidence/recog/a1c_comb/a1c_combined_tail_cert.json")["G2_constants"]; ib = J("evidence/recog/a1c_inblock/a1c_inblock_angular_cert.json")["G2_constants"]
    p1 = J("evidence/recog/a1c_1b/a1c_tail_averaging_cert.json")["G2_constants"]; so = J("evidence/recog/a1c_so/a1c_start_offset_cert.json")["G1"]
    q1 = J("evidence/recog/a1c_3/a1c_q1prime_fiber_cert.json")["G2_constants"]; b1 = J("evidence/recog/b1_l1l2/b1_l1l2_sharpened_rows_cert.json")
    rw = {r["row"]: r for r in b1["G3_rows"]}; K = dd["G2_constants"]["K_eps"]
    g0 = p1["gamma0"][1] if isinstance(p1["gamma0"], list) else p1["gamma0"]
    return [
     ("gamma_2", "ceiling", "$\\gamma_2=212.6$", None, 212.6, dd["G2_constants"]["gamma2"]),
     ("K_eps(625)", "ceiling", "$K_\\epsilon=0.7203$, $0.4513$, $0.1860$ at", "$K_\\epsilon\\le0.7204$, $0.4514$, $0.1861$ at", 0.7204, K["625"]["K"]),
     ("K_eps(1000)", "ceiling", "$K_\\epsilon=0.7203$, $0.4513$, $0.1860$ at", "$K_\\epsilon\\le0.7204$, $0.4514$, $0.1861$ at", 0.4514, K["1000"]["K"]),
     ("K_eps(2500)", "ceiling", "$K_\\epsilon=0.7203$, $0.4513$, $0.1860$ at", "$K_\\epsilon\\le0.7204$, $0.4514$, $0.1861$ at", 0.1861, K["2500"]["K"]),
     ("c_J^R", "ceiling", "$c_J^R=0.5008$, $c_7^R=100.23$", "$c_J^R\\le0.5008$, $c_7^R\\le100.231$", 0.5008, ct["c_J^R"]),
     ("c_7^R", "ceiling", "$c_J^R=0.5008$, $c_7^R=100.23$", "$c_J^R\\le0.5008$, $c_7^R\\le100.231$", 100.231, ct["c_7^R"]),
     ("sup|d|", "ceiling", "0.2955", None, 0.2955, ct["sup|d|"]),
     ("gamma_0", "ceiling", "$\\gamma_0=0.17715$, $\\gamma_1=205.15$", "$\\gamma_0\\le0.17716$, $\\gamma_1\\le205.15$", 0.17716, g0),
     ("gamma_1", "ceiling", "$\\gamma_0=0.17715$, $\\gamma_1=205.15$", "$\\gamma_0\\le0.17716$, $\\gamma_1\\le205.15$", 205.15, p1["gamma1"]),
     ("c_delta", "ceiling", "c_\\delta=0.793", None, 0.793, ib["c_delta_on_U_T"]),
     ("beta(625)", "ceiling", "($\\beta(625)=0.799$, $\\beta\\to0.792$)", "($\\beta(625)\\le0.800$, $\\beta\\to0.792$;", 0.800, so["beta(625)"]),
     ("c_Psi", "ceiling", "c_\\Psi=11.13", None, 11.13, q1["cPsi(=bound/q*)"]),
     ("Xi", "ceiling", "\\Xi=0.027", None, 0.027, q1["Xi"]),
     ("K_Phi L1+L2 large", "ceiling", "($K_\\Phi\\le220.8471$ / $75.6392$)", "($K_\\Phi\\le220.8471$ / $75.6393$;", 220.8471, rw["L1+L2 large"]["K_Phi_upper"]),
     ("K_Phi L1+L2 small", "ceiling", "($K_\\Phi\\le220.8471$ / $75.6392$)", "($K_\\Phi\\le220.8471$ / $75.6393$;", 75.6393, rw["L1+L2 small"]["K_Phi_upper"]),
     ("window L1 large", "window", "2.952\\times10^{-5}", None, 2.952e-5, rw["L1 large"]["window_new"]),
     ("window L1 small", "window", "9.390\\times10^{-5}", None, 9.390e-5, rw["L1 small"]["window_new"]),
     ("window L1+L2 large", "window", "3.456\\times10^{-5}", None, 3.456e-5, rw["L1+L2 large"]["window_new"]),
     ("window L1+L2 small", "window", "resp. $q_0<1.011\\times10^{-4}$", "resp. $q_0<1.010\\times10^{-4}$", 1.010e-4, rw["L1+L2 small"]["window_new"]),
    ] + [(f"C({a},5)", "ceiling", s, None, float(s), pt["PT3"][f"a={a},r=5"]["C_total"]) for a, s in (("625", "58.0"), ("1000", "61.0"), ("2500", "75.1"))]

def check(base, inter, log, root, verbose=True, files=None):
    res = {}
    def gate(n, ok, msg=""):
        res[n] = bool(ok)
        if verbose: print(f"  {n:<4} {'PASS' if ok else 'FAIL'} {msg}")
    edits = log["edits"]; groups = set(log.get("groups", []))
    new_rids = set().union(*(NEW_RIDS[g] for g in groups))
    D5 = "D5B" if "D5B" in groups else ("D5A" if "D5A" in groups else None)
    gate("C0", hashlib.sha256(base.encode()).hexdigest() == BASE_SHA, "BASE")
    gate("C1", apply_log(base, edits) == inter and hashlib.sha256(inter.encode()).hexdigest() == log["intermediate_sha256"], "BUILD")
    gate("C2", apply_log(inter, edits, reverse=True) == base, "REVERSE")
    _, ab, _ = split_appa(base); _, ai, _ = split_appa(inter)
    i = ai.find("### v0.3.27"); j = ai.find("### v0.3.26", i)
    gate("C3", i > 0 and j > i and ai[:i] + ai[j:] == ab, "APPENDIX A")
    changed = {e["key"] for e in edits if Counter(TAGBT.findall(e["old"])) != Counter(TAGBT.findall(e["new"]))}
    declared = {k for k in TAG_CHANGE if any(e["key"] == k for e in edits)}
    gate("C4", changed == declared, f"SPAN TAGS {sorted(changed ^ declared) if changed != declared else ''}")
    bad = []; L = live(inter); Lb = live(base)
    for e in edits:
        ro, rn = ANYRID.findall(e["old"]), ANYRID.findall(e["new"])
        if [x for x in ro if x not in rn]: bad.append(e["key"])
        if any(x not in ro and x not in new_rids | IMPORT_RIDS_ALLOWED for x in rn): bad.append(e["key"])
    gate("C5", not bad, f"SPAN RIDS {bad}")
    st = lambda s: [l for l in live(s).splitlines() if l.startswith("Status:")]
    gate("C6", st(base) == st(inter), "STATUS (byte-identical)")
    gate("C7", set(RID_RECOG.findall(inter)) == set(RID_RECOG.findall(base)) | new_rids, "RID SET")
    atb, ati = after_texts(Lb), after_texts(L)
    sp = lambda c: Counter(x[:x.index("]") + 1] if x.startswith(" [scope:") and "]" in x else "*" for x in c.elements())   # unscoped occurrences (§1 summary): count only
    requal = set().union(*(REQUAL[g] for g in groups))
    ok = all((sp(atb[k]) == sp(ati.get(k, Counter()))) if k in requal else (atb[k] == ati.get(k)) for k in atb)
    for k in new_rids:
        sig = ATTACH[k]; v = ati.get(k, Counter()); n = min(60, len(sig))
        ok &= sum(1 for x in v.elements() if x[:n] == sig[:n]) == 1
    gate("C8", ok, "RID ATTACH")
    head = L[:L.index("## §7. Import Ledger")]
    viol = [l[:60] for l in head.splitlines() if RESULT_LEAD.match(l) and ((FROM.match(l).group(1) or FROM.match(l).group(2)) if FROM.match(l) else None) not in CANON]
    gate("C9", not viol, f"RESULT {len(viol)} unpaired/combined" if viol else "RESULT")
    keys = lambda t: Counter(QUAL.findall(t)) + Counter({w: t.count(w) for w in ("Depends on:", "[cert:", "[proof:", "[import:")})
    glob = keys(inter); glob.subtract(keys(base)); loc, removed = Counter(), []
    for e in edits:
        d = keys(e["new"]); d.subtract(keys(e["old"])); loc.update(d)
        lost = [q for q in (-d) if not q.startswith("[assuming: ")]
        okrem = (e["key"] in QUAL_CHANGE and e["new"].count("[import:") > e["old"].count("[import:")) or (e["key"] in QUAL_DISCHARGE and not lost)
        if -d and not okrem: removed.append(e["key"])
    gate("C10", not removed and +glob == +loc and -glob == -loc, "QUALIFIERS" + (f" removed in {removed}" if removed else ""))
    gate("C11", len(VOCAB.findall(inter)) == len(VOCAB.findall(base)), "VOCAB")
    cell = section(inter, "#### §6.13b A1a", "### §6.14 The $h$-Chart Ledger"); s7 = section(inter, "## §7. Import Ledger", "### §7.1")
    s616 = section(inter, "#### §6.16e", "#### §6.16f")
    ok = ("RID unavailable" not in cell and "RID unavailable" not in s7 and all(x in cell and x in s7 for x in ("NUMGEN-DEF-N5AS1-DEFECT", "NUMGEN-RESULT-N5AS1-INF1")))
    if D5:
        for s in SITES:
            ln = line_at(L, SITE_ANCHOR[s], L.index("## §6."))
            ok &= "DYAD-THM-LPHASE-ROWA-BRIDGE" in ln and "DYAD-THM-OPEN3-SPIRAL-REM" in ln and "[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 §6.14 | DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM]" in ln
        ok &= "- [RID: DYAD-THM-LPHASE-ROWA-BRIDGE] ::" in s7 and "- [RID: DYAD-THM-OPEN3-SPIRAL-REM] ::" in s7 and "$c'_Q=0.36916$" in s7
    else:
        ok &= "DYAD-THM-LPHASE-ROWA-BRIDGE" not in L
    if "C7" in groups:
        ln = line_at(L, "[RID: RECOG-THM-R9-SHARPENED-ROWS-C7]", L.index("## §6."))
        ok &= "[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 §6.14 | DYAD-THM-NF-REM-C7-SHARP]" in ln and "- [RID: DYAD-THM-NF-REM-C7-SHARP] ::" in s7
    gate("C12", ok, "IMPORTS")
    r9 = lambda s: [l for l in s.splitlines() if l.startswith("`[THM]` [RID: RECOG-THM-R9-MEMORY]")]
    rows = lambda s: [l for l in s.splitlines() if l.startswith(("| A | $0<\\lvert W_0", "| B | $0<\\lvert W_0", "| large | $|z|\\le\\tfrac1{20}$, $C_7=100$", "| small | $|z|\\le\\tfrac1{40}$, $C_7=30$"))]
    a1b = lambda s: section(s, "`[THM]` [RID: RECOG-THM-A1B-SLIP-SCHEDULE-U] [scope:", "\n**Not supplied:**")
    pn = (lambda t: t.replace("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", "RTG_DYADIC_OSCILLATOR_DSN_v6.4.23")) if "PIN" in groups else (lambda t: t)   # pin maintenance only
    ok = len(r9(base)) == 1 and pn(r9(base)[0]) == r9(inter)[0] and len(rows(base)) == 4 and rows(base) == rows(inter) and len(a1b(base)) > 1000 and pn(a1b(base)) == a1b(inter)
    disp = lambda s_: [l for l in s_.splitlines() if l.startswith("$$c" + "'" * 3 + "_k(a):=")]
    ok &= len(disp(base)) == 1 and disp(base) == disp(inter)
    th = section(inter, "`[ALG]` [RID: RECOG-ALG-A1C-TAIL-HARMONICS]", "\n`[ALG]` [RID: RECOG-ALG-A1C-INBLOCK-ANGLE]")
    ok &= all(x in th for x in ("(ii) $Q_M\\le\\bar Q_M$ with $\\bar Q_M\\approx1/(a+M)$", "`[ALG via IA]` $E'(a,M)\\le0.31$ for every $a\\ge625$, $M\\ge1$"))
    q1 = lambda s: [l for l in s.splitlines() if l.startswith("- A1c-Q1′:")]
    ok &= len(q1(base)) == 1 and q1(base) == q1(inter)
    ok &= base.count("q_0<|G|/C_2") >= 3 and base.count("q_0<|G|/C_2") == inter.count("q_0<|G|/C_2")
    gate("C13", ok, "UNCHANGED (R9, A1B, schedule display, TAIL-HARMONICS items, Q1′, B1 formula)")
    hd = lambda s: ([l for l in s.splitlines()[:60] if l.startswith(("# ", "**Date:**", "**Supersedes:**", "**Title:**", "**Scope:**", "**Status summary", "**Document status"))] + s.splitlines()[-3:])
    gate("C14", hd(base) == hd(inter), "HEADER")
    hs = lambda s: [l for l in s.splitlines() if l.startswith("#")]
    gate("C15", hs(live(base)) == hs(L), "HEADINGS")
    s8 = section(inter, "## §8. Artifact", "## §9.")
    names = set(re.findall(r"`([A-Za-z0-9_.\-]+\.(?:py|json|jsonl|md|txt|zip))`", s8)) | {os.path.basename(x) for x in re.findall(r"`((?:evidence|records)/[^`]+\.(?:py|json|jsonl|md|txt))`", s8)}
    fl, paths = files if files is not None else repo_files(root)
    miss = sorted(n for n in names if n not in fl and n not in FILE_EXCEPT)
    hashok = True; nh = 0; nrows = 0
    for row in [l for l in s8.splitlines() if "`[v0.3.27]`" in l]:
        nrows += 1
        for ref, h1, h2 in HASHREF.findall(row):
            for h in (h1, h2):
                if not h: continue
                nh += 1
                if ref.endswith("/"):
                    d = os.path.join(root, ref); cands = [os.path.join(d, f) for f in os.listdir(d)] if os.path.isdir(d) else []
                else:
                    cands = paths.get(os.path.basename(ref), [])
                hashok &= any(hmatch(h, sha(p)) for p in cands)
    want_rows = (4 if "R1" in groups else 0) + (1 if "D5B" in groups else 0)
    gate("C16", not miss and hashok and nrows == want_rows and (nh >= 3 * want_rows), f"§8 FILES missing: {miss}" if miss else (f"§8 FILES ({nrows} rows, {nh} hashes checked)" if hashok else "§8 FILES: quoted hash mismatch"))
    ok = all(x in L for x in ("F2(a3)", "W1–W5", "registry-relative", "no identifiable token-specific write-through"))
    r6 = section(inter, "**OPEN R6 — Physical recognition-event rule**", "**OPEN R"); r4 = section(inter, "**OPEN R4 — Intrinsic type-change locus**", "**OPEN R")
    ok &= any(l.startswith("Status: ACTIVE") for l in r6.splitlines()) and "R6 therefore remains **ACTIVE**" in L and any(l.startswith("Status: ACTIVE") for l in r4.splitlines())
    qq = [l for l in r6.splitlines() if l.startswith("- A1c-Q1′:")]
    ok &= len(qq) == 1 and qq[0].rstrip().endswith(":: `[OPEN]`")
    gate("C17", ok, "LIVE")
    ok = True
    try:
        m = load_builder(root)
        for gs in (("R1", "D5B"), ("R1", "D5A"), ("C7",), ("DISP",), ("PIN",)):
            eds = [e for e in m.EDITS if e[1] in gs]
            if "R1" in gs: eds += [(k, "R1", "s8", "s8", "live", pre, reps, note) for k, pre, reps, note in m.s8_subs()]
            t, _ = m.apply(base, eds + [m.appa_edit(set(gs))])
            ok &= set(RID_RECOG.findall(t)) == set(RID_RECOG.findall(base)) | set().union(*(NEW_RIDS[g] for g in gs))
        with tempfile.TemporaryDirectory() as td:
            bp = os.path.join(td, "base.md"); open(bp, "w", encoding="utf-8").write(base)
            for bad_gs in ("R1", "D5B", "D5A", "R1,D5B,D5A"):
                refused = False
                try: m.main(["b", bp, os.path.join(td, "o.md"), os.path.join(td, "o.json"), "--only", bad_gs])
                except AssertionError: refused = True
                ok &= refused
    except (AssertionError, KeyError) as ex:
        ok = False
        if verbose: print("    C18 exception:", repr(ex))
    gate("C18", ok, "DECOUPLE")
    ok = True
    try:
        J = lambda p: json.load(open(os.path.join(root, p)))
        if "R1" in groups:
            src = open(os.path.join(root, "evidence/recog/scripts/recog_a1c_tail_averaging_cert.py"), encoding="utf-8").read().splitlines()
            ok &= sum(1 for l in src if l.startswith('cQ, cQp, cJ, c7, K_Theta = I("0.79246"), I("0.36916"), I("0.50220"), I("157.58"), I(123)/125')) == 1
            ok &= not any("0.36915" in l for l in src if not l.lstrip().startswith(("#", '"""')) and "I(" in l)
            for p, k in (("a1c_1b/a1c_tail_averaging_cert.json", "ALL_PASS"), ("a1c_so/a1c_start_offset_cert.json", "ALL_PASS"), ("a1c_2/a1c_unknown_a_interval_cert.json", "ALL_PASS"),
                         ("a1c_inblock/a1c_inblock_angular_cert.json", "ALL_PASS"), ("a1c_comb/a1c_combined_tail_cert.json", "ALL_PASS"), ("a1c_joint/a1c_joint_transfer_cert.json", "ALL_PASS"),
                         ("a1c_drift/a1c_drift_centering_cert.json", "ALL_PASS"), ("a1c_drift/a1c_drift_proof_table_cert.json", "ALL_PASS")):
                ok &= J("evidence/recog/" + p).get(k) is True
            ok &= J("evidence/recog/v0.3.26/corrected_grid.json")["all_below"] is True
            ok &= 0.7993 < J("evidence/recog/a1c_so/a1c_start_offset_cert.json")["G1"]["beta(625)"] < 0.800
        if "D5B" in groups:
            jt = J("evidence/recog/a1c_jet/a1c_jet_remainder_bounds_cert.json"); g = jt["G1_exact_rational"]
            ok &= jt["ALL_PASS"] is True and g["cJ_upper_float"] < 0.500819 < 0.50220 and g["c7_upper_float"] < 100.231 < 157.58
            blk = line_at(L, "[RID: RECOG-ALG-A1C-JET-REMAINDER-BOUNDS]", L.index("## §6."))
            ok &= "$c_J\\le0.500819$ and $c_7\\le100.231$" in blk and "$c_J=0.50220$ and $c_7=157.58$" in blk
    except Exception as ex:
        ok = False
        if verbose: print("    C19 exception:", repr(ex))
    gate("C19", ok, "VALUES")
    par = lambda s: [l for l in live(s).splitlines() if l.startswith("**Outbound notices; current state.**")]
    gate("C20", len(par(base)) == 1 and par(base) == par(inter), "NOTICES")
    glob = Counter(TAGBT.findall(inter)); glob.subtract(Counter(TAGBT.findall(base))); loc = Counter()
    for e in edits: loc.update(Counter(TAGBT.findall(e["new"]))); loc.subtract(Counter(TAGBT.findall(e["old"])))
    gate("C21", +glob == +loc and -glob == -loc, "TAG CENSUS")
    ok = True; six = L.index("## §6.")
    for s in SITES:
        ln = line_at(L, SITE_ANCHOR[s], six)
        if D5 is None: ok &= (OLD_Q in ln) or (OLD_QS in ln)
        elif D5 == "D5B": ok &= "`[assuming:" not in ln and "(D5)" not in ln.replace("the former (D5) qualifier is discharged", "")
        else: ok &= OLD_Q not in ln and OLD_QS not in ln and re.search(r"`\[assuming: [^`]*c_J[^`]*\]`", ln) is not None and ("157.58" in ln)
    if D5 == "D5B":
        s1 = section(inter, "## §1. Current Canonical State", "## §2. Active Frontier")
        ok &= "`[assuming: (D5)]`" not in L and "row-A bridge proof constants (D5)]" not in L and "under the (D5) `[assuming:]`" not in L and "(D5)]`" not in s1
    gate("C22", ok, "ASSUMING")
    s1 = section(inter, "## §1. Current Canonical State", "## §2. Active Frontier")
    i = s1.find("[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE]"); sent = s1[i:s1.find("$C_D$ depends", i)]
    j = L.find("[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE]", six); blk = L[j:L.find("\n`[NUM]`", j)]
    ok = i >= 0 and j >= 0 and "record-only centre" not in sent and "record-only centre" not in blk and "known-$a$ / declared-data centre" in sent and "nothing in this theorem is record-only" in blk
    dec = [l for l in L.splitlines() if l.startswith("- A1c-decoder")]
    ok &= len(dec) == 1 and "not record-only" in dec[0] and "at least two usable slips" in dec[0] and "no Q1′ conclusion" in dec[0]
    ok &= ("`[assuming:]`" in dec[0]) == (D5 != "D5B")
    gate("C24", ok, "R83-1 (known-a centre never called record-only; decoder closure scoped)")
    ok = all(os.path.exists(os.path.join(root, p)) for p in set(RECPATH.findall("\n".join(e["new"] for e in edits))))
    gate("C23", ok, "RECORDS")
    gate("C25", base[base.index(APPA_END):] == inter[inter.index(APPA_END):], "APPENDIX B (byte-identical)")
    ok = True; nd = 0
    try:
        for name, kind, old, new, val, cert in direction_rows(root):
            shown = new if ("DISP" in groups and new) else old
            ok &= shown in L; nd += 1
            if "DISP" in groups or new is None:
                ok &= (val >= cert) if kind == "ceiling" else (val <= cert)
            if "DISP" in groups and new:
                ok &= old not in L
                ln = line_at(L, new, six); ok &= "`[COR]` v0.3.27" in ln
    except Exception as ex:
        ok = False
        if verbose: print("    C26 exception:", repr(ex))
    gate("C26", ok, f"DIRECTION ({nd} displays)")
    if "PIN" in groups:
        bad = [l[:50] for l in L.splitlines() if any(p in l for p in OLD_PINS) and not l.startswith(PIN_KEEP)]
        hdr = [l for l in L.splitlines()[:20] if l.startswith("**Companion document")]
        gap = [l for l in L.splitlines() if l.startswith("- `[import: RTG_NUMBER_GENESIS_DSN_v1.21 §6.6 | NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO]`")]
        ok = not bad and len(hdr) == 1 and "`dyad-v6.4.23`" in hdr[0] and "`numgen-v1.21`" in hdr[0] and len(gap) == 1 and "no RID is inferred here for GAP-LOCK Lemma 3" not in L
        ok &= "`835a56f8…7e2f`" not in L.replace("the earlier abbreviation `835a56f8…7e2f`", "")
        gate("C27", ok, "PINS" + (f" stale: {bad}" if bad else ""))
    if "C7" in groups:
        ok = "`[assuming: $C_7\\le85.1$" not in L and "beyond Dyadic's published values" not in L and "used only as `[assuming:]` ceilings" not in L and "certificate values 85.07/27.60" not in L
        gate("C28", ok, "C7 ROWS")
    return res

def controls(base, inter, log, root):
    print("\nNEGATIVE CONTROLS (each must be caught by its target gate):")
    files = repo_files(root); L = inter; groups = set(log["groups"])
    def once(s, a, b):
        assert s.count(a) >= 1, a
        return s.replace(a, b, 1)
    def outside(s, a, b, anchor="### §6.7 Shear-Jet Law"):
        i = s.find(anchor); j = s.find(a, i); assert j > 0
        return s[:j] + b + s[j + len(a):]
    C = [
     ("NC01 new RID removed", "C7", once(L, "[RID: RECOG-ALG-A1C-JET-REMAINDER-BOUNDS] ", "")),
     ("NC02 OPEN status altered (R4 closed)", "C6", once(L, "**OPEN R4 — Intrinsic type-change locus** [RID: RECOG-OPEN-TYPE-CHANGE]\n\nStatus: ACTIVE", "**OPEN R4 — Intrinsic type-change locus** [RID: RECOG-OPEN-TYPE-CHANGE]\n\nStatus: CLOSED")),
     ("NC03 header identity altered", "C14", once(L, "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.26", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.27")),
     ("NC04 Appendix A history edited", "C3", once(L, "### v0.3.26 — 28 October 2026 — Adopted", "### v0.3.26 — 29 October 2026 — Adopted")),
     ("NC05 grade changed outside the spans", "C21", outside(L, "`[ALG]`", "`[THM]`")),
     ("NC06 scope qualifier deleted", "C10", once(L, "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL] [scope: diagnostic twin $T_s$, SG-R4]", "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL]")),
     ("NC07 (D5) qualifier restored at one site", "C22", once(L, "[RID: RECOG-ALG-A1C-ADMISSIBLE-REGION] [scope: as RECOG-THM-A1C-SHARPENED-SCHEDULE, $a$ unknown] ", "[RID: RECOG-ALG-A1C-ADMISSIBLE-REGION] [scope: as RECOG-THM-A1C-SHARPENED-SCHEDULE, $a$ unknown] `[assuming: (D5)]` ")),
     ("NC08 bridge import dropped at one site", "C12", L.replace(line_at(L, "[RID: RECOG-ALG-A1C-JOINT-CONTRACTOR] [scope:", L.index("## §6.")), line_at(L, "[RID: RECOG-ALG-A1C-JOINT-CONTRACTOR] [scope:", L.index("## §6.")).replace("[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 §6.14 | DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM]", "[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 §6.14 | DYAD-THM-LPHASE-ROWA-REMAINDER]"), 1)),
     ("NC09 jet ceiling printed below the certificate", "C19", once(L, "$c_J\\le0.500819$ and $c_7\\le100.231$", "$c_J\\le0.500819$ and $c_7\\le100.23$")),
     ("NC10 §8 regenerated hash altered", "C16", L.replace(line_at(L, "- [RID: RECOG-ART-A1C-DECODER] "), re.sub(r"`([0-9a-f]{8})…([0-9a-f]{3})([0-9a-f])`", lambda m: f"`{m.group(1)}…{m.group(2)}{'0' if m.group(3) != '0' else '1'}`", line_at(L, "- [RID: RECOG-ART-A1C-DECODER] "), count=1), 1)),
     ("NC11 §8 jet artifact hash altered", "C16", L.replace(line_at(L, "- [RID: RECOG-ART-A1C-JET-REMAINDER-BOUNDS] "), re.sub(r"\(sha256 `([0-9a-f]{63})([0-9a-f])`\)", lambda m: f"(sha256 `{m.group(1)}{'0' if m.group(2) != '0' else '1'}`)", line_at(L, "- [RID: RECOG-ART-A1C-JET-REMAINDER-BOUNDS] ")), 1)),
     ("NC12 notice state changed", "C20", once(L, "G3 to OFN and G3 to RRF: prepared", "G3 to OFN and G3 to RRF: sent")),
     ("NC13 Appendix B edited", "C25", once(L, "**[FAIL | RID: RECOG-FAIL-K-FROM-SADDLE]**", "**[FAIL | RID: RECOG-FAIL-K-FROM-SADDLE]** ")),
     ("NC14 Dyadic current-use pin left at v6.4.22", "C27", once(L, "Dyadic v6.4.23 §6.4", "Dyadic v6.4.22 §6.4")),
     ("NC15 NUMGEN current-use pin left at v1.20.8", "C27", once(L, "[import: RTG_NUMBER_GENESIS_DSN_v1.21 §6.6 | NUMGEN-RESULT-N5AS1-INF1]", "[import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 | NUMGEN-RESULT-N5AS1-INF1]")),
     ("NC16 miscopied NUMGEN hash abbreviation reintroduced", "C27", once(L, "NUMGEN `numgen-v1.21` (`4805760d…5701`)", "NUMGEN `numgen-v1.21` (`835a56f8…7e2f`)")),
     ("NC17 C_7 [assuming:] ceiling restored", "C28", once(L, "[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 §6.14 | DYAD-THM-NF-REM-C7-SHARP] ($C_7\\le85.1$", "`[assuming: $C_7\\le85.1$ ...]` ($C_7\\le85.1$")),
     ("NC18 heading changed", "C15", once(L, "### §6.12 Leading-Return Equivariance and Comparator Closure", "### §6.12 Leading-Return Equivariance")),
     ("NC19 R1 rerun JSON reported failing", "C19", None),
     ("NC21 OPEN R5 export line left at OFN v0.10", "C27", once(L, "Exports to: RTG_ONTOLOGICAL_FOUNDATIONS v0.12 §6.2a (`ofn-v0.12`;", "Exports to: RTG_ONTOLOGICAL_FOUNDATIONS v0.10 §6.2a (`ofn-v0.12`;")),
     ("NC20 decoder line regains [assuming:] under D5B", "C24", once(L, "with the row-A remainder constants of the envelope (", "under the `[assuming:]` row-A remainder constants of the envelope (")),
    ]
    # item 7: one control per old display (restoring the v0.3.26 display must be caught by C26)
    for nm, old, new in (("K_eps 0.7203", "$K_\\epsilon\\le0.7204$, $0.4514$, $0.1861$ at", "$K_\\epsilon\\le0.7203$, $0.4514$, $0.1861$ at"),
                         ("K_eps 0.4513", "$K_\\epsilon\\le0.7204$, $0.4514$, $0.1861$ at", "$K_\\epsilon\\le0.7204$, $0.4513$, $0.1861$ at"),
                         ("K_eps 0.1860", "$K_\\epsilon\\le0.7204$, $0.4514$, $0.1861$ at", "$K_\\epsilon\\le0.7204$, $0.4514$, $0.1860$ at"),
                         ("c_7^R 100.23", "$c_J^R\\le0.5008$, $c_7^R\\le100.231$", "$c_J^R\\le0.5008$, $c_7^R\\le100.23$"),
                         ("gamma_0 0.17715", "$\\gamma_0\\le0.17716$, $\\gamma_1\\le205.15$", "$\\gamma_0\\le0.17715$, $\\gamma_1\\le205.15$"),
                         ("beta(625) 0.799", "($\\beta(625)\\le0.800$, $\\beta\\to0.792$;", "($\\beta(625)\\le0.799$, $\\beta\\to0.792$;"),
                         ("beta(625) 0.7993", "($\\beta(625)\\le0.800$, $\\beta\\to0.792$;", "($\\beta(625)\\le0.7993$, $\\beta\\to0.792$;"),
                         ("K_Phi 75.6392", "($K_\\Phi\\le220.8471$ / $75.6393$;", "($K_\\Phi\\le220.8471$ / $75.6392$;"),
                         ("window 1.011e-4", "resp. $q_0<1.010\\times10^{-4}$", "resp. $q_0<1.011\\times10^{-4}$")):
        C.append((f"NC-DIR {nm} restored", "C26", once(L, old, new)))
    allok = True
    for name, target, mtxt in C:
        if name.startswith("NC19"):
            p = os.path.join(root, "evidence/recog/a1c_joint/a1c_joint_transfer_cert.json"); keep = open(p, "rb").read()
            try:
                d = json.loads(keep); d["ALL_PASS"] = False; open(p, "w").write(json.dumps(d))
                r = check(base, inter, log, root, verbose=False, files=files)
            finally:
                open(p, "wb").write(keep)
            assert sha(p) == hashlib.sha256(keep).hexdigest()
        else:
            if mtxt == inter: print(f"  {name:<52} NOT CONSTRUCTED"); allok = False; continue
            r = check(base, mtxt, log, root, verbose=False, files=files)
        failed = sorted(k for k, v in r.items() if not v); hit = target in failed; allok &= hit
        print(f"  {name:<52} target {target}: {'caught' if hit else 'NOT CAUGHT'}  (failing: {', '.join(failed)})")
    return allok

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) != 3: print(__doc__); sys.exit(2)
    base = open(a[0], encoding="utf-8").read(); inter = open(a[1], encoding="utf-8").read()
    log = json.load(open(a[2], encoding="utf-8")); root = os.getcwd()
    print(f"base {hashlib.sha256(base.encode()).hexdigest()}\nintermediate {hashlib.sha256(inter.encode()).hexdigest()} (groups {','.join(log.get('groups', []))}, {len(log['edits'])} edits)")
    print("GATES:"); r = check(base, inter, log, root); ok = all(r.values())
    if "--controls" in sys.argv: ok &= controls(base, inter, log, root)
    print("\nRESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
