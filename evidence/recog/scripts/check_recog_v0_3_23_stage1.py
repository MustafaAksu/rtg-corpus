#!/usr/bin/env python3
"""check_recog_v0_3_23_stage1.py -- deterministic checker for the RECOG v0.3.23 stage-1 intermediate.

usage (from the repository root):
  python -I evidence/recog/scripts/check_recog_v0_3_23_stage1.py BASE INTERMEDIATE EDITLOG_JSON [--controls]
  BASE = `git show recog-v0.3.22:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`; EDITLOG_JSON written by the builder.
exit 0 = every gate PASS (and, with --controls, every negative control caught by its target gate).

Gates. C1-C5 use the edit log; all other gates read only the two texts, so a negative control can show which
semantic gate catches it (C1 BUILD catches every byte change by construction).
  C0  BASE       base SHA-256 is the adopted v0.3.22 identity (tag recog-v0.3.22)
  C1  BUILD      intermediate == exact-once application of the logged edits to the base (Appendix A masked
                 for region "live"); hash == the logged intermediate hash
  C2  REVERSE    undoing every edit (reverse order, exact-once) recovers the base byte-exactly
  C3  APPENDIX A Appendix A minus the new v0.3.23 entry is byte-identical to the base Appendix A
  C4  SPAN TAGS  the edits whose backticked tag multiset changes are exactly the declared TAG_CHANGE edits
  C5  SPAN RIDS  per edit every [RID: X] of the old text survives; added RIDs are declared (new RECOG RIDs or
                 owner RIDs now cited in §7/§6.13b rows)
  C6  STATUS     OPEN-registry "Status:" lines equal the base except the declared R10 wording
  C7  RID SET    RECOG RID set == base set + declared new RIDs (variant-aware); none removed
  C8  RID ATTACH for every RECOG RID declaration, the multiset of the text after "[RID: X]" (to the end of the
                 line, at most 60 characters) is unchanged
                 (exception: RECOG-OPEN-INTERSECTION, declared); new RIDs attach to their declared statements
  C9  RESULT     in §§1-6 every line-leading [RESULT] is followed by [from: TAG] with one canonical tag
  C10 QUALIFIERS no edit removes a [scope: ...], [assumes: ...], [assuming: ...], "Depends on:", "[cert:",
                 "[proof:" or "[import:"; the global change of these equals the sum of the per-edit changes
  C11 VOCAB      no READ / WRITE / DECODE vocabulary introduced
  C12 IMPORTS    no "RID unavailable" in §6.13b or §7 (§7 before §7.1); both NUMGEN RIDs in §6.13b and §7;
                 no Dyadic line pins ("lines 806", "lines 843"); the old Dyadic tag forms occur only as quoted
                 v6.4.18 text; no "`[THM — conditional on RECOG-THM-R9-MEMORY]`" in live text
  C13 R9/OPEN21  the RECOG-THM-R9-MEMORY statement line and the (c) row table are unchanged; OPEN 21 constants
                 present in §6.13b and §7
  C14 HEADER     title, date, supersedes, every status-summary line and the footer are unchanged
  C15 HEADINGS   heading lines equal the base except the declared §7.3 heading
  C16 §8 FILES   every backticked file name in §8 exists in the repository (loose or as a package member),
                 except the declared Dyadic-side harness
  C17 LIVE       must-stay-live items present: F2(a3) selection question, W1-W5, R6 ACTIVE, registry-relative
                 limits, the absence of independent write-through
  C18 DECOUPLE   (with-fc21 variant) the builder's without-fc21 variant builds and carries no FC-21 RID
  C19 VALUES     the edited displays carry the checked values (see recog_v0_3_23_value_checks.py)
  C20 NOTICES    the §7.2 notice paragraph changes no notice state (G3-OFN/RRF prepared; nothing sent)
  C21 TAG CENSUS global backticked-tag multiset delta == sum of the per-edit deltas (no grade change outside
                 the declared spans)
"""
import hashlib, importlib.util, json, os, re, sys, zipfile
from collections import Counter

BASE_SHA = "0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9"
APPA_START, APPA_END = "## Appendix A — Version History", "## Appendix B —"
NEW_M = {"RECOG-THM-R9-COMPARATOR-INCOMPLETENESS", "RECOG-ALG-SWAP-ODD-RHO"}
NEW_FC21 = {"RECOG-THM-A1A-PHASE-EXISTENCE-U", "RECOG-ART-A1A-EXISTENCE-U"}
ATTACH = {  # new RID -> text that must follow its declaration
    "RECOG-THM-R9-COMPARATOR-INCOMPLETENESS": " [scope: as RECOG-THM-R9-MEMORY, per row; witness window $q_0<|G|/C_2$] **Corollary (exact-map $C_z$ comparator incompleteness).**",
    "RECOG-ALG-SWAP-ODD-RHO": " [assumes: pole-swap covariance; certified $A=DT(P_1)$] **Swap-odd $\\rho$ lemma.**",
    "RECOG-THM-A1A-PHASE-EXISTENCE-U": " [scope: conditional on postulated $T$; $x_0\\in U=",
    "RECOG-ART-A1A-EXISTENCE-U": " `[v0.3.23]` :: proof cell",
}
ATTACH_CHANGED = {"RECOG-OPEN-INTERSECTION"}
TAG_CHANGE = {
    "S1-1": "§1 INTERSECTION [OPEN] -> [HYP] (its §6.5 tag)",
    "S1-6": "FC-21 summary line (new [THM])",
    "S3-2": "owner tag form quoted (T1/T2)",
    "S613b-8": "owner tag form (primitive-variable form)",
    "S613b-10": "owner tag form (T1/T2)",
    "S613b-11": "owner tag form (OPEN 21)",
    "S613b-14": "FC-21 block (new [THM], [NUM] pointer)",
    "S616a-R1": "RESULT split into two paired blocks",
    "S616d-R3": "RESULT split into two paired blocks",
    "S7-13": "owner tag forms quoted in a §7 row",
    "S7-14": "owner tag form quoted in a §7 row",
    "S7-15": "owner tag form quoted in a §7 row",
    "S7-17": "owner tag form quoted in the new FC-21 §7 row",
    "S72-3": "RRF [OPEN] label quoted",
    "S8-3": "FC-21 artifact row ([SESSION], [NUM])",
    "A-1": "Appendix A entry quotes [HYP], [RESULT]",
}
IMPORT_RIDS_ADDED = {"DYAD-DEF-PRIMITIVE-MAP", "DYAD-DEF-CRITICAL-CURVE", "DYAD-ALG-QC-CRITICAL-AMPLITUDE",
                     "DYAD-ALG-ISP-MAPS", "DYAD-ALG-SIXSTEP-CUBIC-JET", "DYAD-ALG-RAW-ANGULAR-MEAN",
                     "NUMGEN-DEF-N5AS1-DEFECT", "NUMGEN-RESULT-N5AS1-INF1", "DYAD-THM-LPHASE-ROWA-REMAINDER"}
R10_OLD = "Status: **DELIVERED and ACCEPTED (v0.3.2)** — owner adoption"
R10_NEW = "Status: **CLOSED (v0.3.2) — delivered and accepted** — owner adoption"
HEAD_73 = ("### §7.3 Downstream Dependents Register (v0.3.21) {#sec-7-3-dependents}",
           "### §7.3 Downstream Dependents Register (v0.3.23) {#sec-7-3-dependents}")
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

def split_appa(s):
    i, j = s.index(APPA_START), s.index(APPA_END)
    return s[:i], s[i:j], s[j:]

def live(s):
    a, _, c = split_appa(s)
    return a + c

def section(s, start, end):
    i = s.find(start); j = s.find(end, i + 1)
    return s[i:j] if i >= 0 and j > i else ""

def apply_log(base, edits, reverse=False):
    a, appa, c = split_appa(base)
    lv = a + "\x00APPA\x00" + c
    seq = reversed(edits) if reverse else edits
    for e in seq:
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
    names = set()
    for top in ("evidence/recog", "records/recog"):
        for d, _, fs in os.walk(os.path.join(root, top)):
            for f in fs:
                names.add(f)
                if f.endswith(".zip"):
                    try:
                        for m in zipfile.ZipFile(os.path.join(d, f)).namelist():
                            names.add(os.path.basename(m))
                    except zipfile.BadZipFile:
                        pass
    return names

def load_builder(root):
    p = os.path.join(root, "evidence/recog/scripts/build_recog_v0_3_23_stage1.py")
    spec = importlib.util.spec_from_file_location("b", p); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m

def check(base, inter, log, root, verbose=True, files=None):
    res = {}
    def gate(n, ok, msg=""):
        res[n] = bool(ok)
        if verbose: print(f"  {n:<4} {'PASS' if ok else 'FAIL'} {msg}")
    edits = log["edits"]
    fc21 = log.get("variant") == "with-fc21"
    gate("C0", hashlib.sha256(base.encode()).hexdigest() == BASE_SHA, "BASE")
    b = apply_log(base, edits)
    gate("C1", b == inter and hashlib.sha256(inter.encode()).hexdigest() == log["intermediate_sha256"], "BUILD")
    r = apply_log(inter, edits, reverse=True)
    gate("C2", r == base, "REVERSE")
    _, ab, _ = split_appa(base); _, ai, _ = split_appa(inter)
    i = ai.find("### v0.3.23"); j = ai.find("### v0.3.22", i)
    gate("C3", i > 0 and j > i and ai[:i] + ai[j:] == ab, "APPENDIX A")
    changed = {e["key"] for e in edits if Counter(TAGBT.findall(e["old"])) != Counter(TAGBT.findall(e["new"]))}
    declared = {k for k in TAG_CHANGE if any(e["key"] == k for e in edits)}
    gate("C4", changed == declared, f"SPAN TAGS {sorted(changed ^ declared) if changed != declared else ''}")
    bad = []
    allowed = NEW_M | (NEW_FC21 if fc21 else set()) | IMPORT_RIDS_ADDED
    for e in edits:
        ro, rn = ANYRID.findall(e["old"]), ANYRID.findall(e["new"])
        if any(x not in rn for x in ro) or any(x not in ro and x not in allowed for x in rn): bad.append(e["key"])
    gate("C5", not bad, f"SPAN RIDS {bad}")
    st = lambda s: [l for l in live(s).splitlines() if l.startswith("Status:")]
    sb, si = st(base), st(inter)
    gate("C6", len(sb) == len(si) and [l.replace(R10_OLD, R10_NEW) for l in sb] == si and sum(R10_OLD in l for l in sb) == 1, "STATUS")
    want = set(RID_RECOG.findall(base)) | NEW_M | (NEW_FC21 if fc21 else set())
    gate("C7", set(RID_RECOG.findall(inter)) == want, "RID SET")
    atb, ati = after_texts(live(base)), after_texts(live(inter))
    ok = all(atb[k] == ati.get(k) for k in atb if k not in ATTACH_CHANGED)
    for k, sig in ATTACH.items():
        if k in want - set(RID_RECOG.findall(base)):
            v = ati.get(k, Counter())
            n = min(60, len(sig))
            ok &= sum(1 for x in v.elements() if x[:n] == sig[:n]) == 1
    gate("C8", ok, "RID ATTACH")
    head = live(inter)[:live(inter).index("## §7. Import Ledger")]
    viol = []
    for l in head.splitlines():
        if RESULT_LEAD.match(l):
            m = FROM.match(l)
            t = (m.group(1) or m.group(2)) if m else None
            if t not in CANON: viol.append(l[:60])
    gate("C9", not viol, f"RESULT {len(viol)} unpaired/combined" if viol else "RESULT")
    # qualifier accounting: no edit removes a qualifier, and the global change equals the sum of the edits'
    # changes (so a deletion outside the spans cannot be masked by an identical qualifier added in a span)
    keys = lambda t: Counter(QUAL.findall(t)) + Counter({w: t.count(w) for w in ("Depends on:", "[cert:", "[proof:", "[import:")})
    glob = keys(inter); glob.subtract(keys(base))
    loc, removed = Counter(), []
    for e in edits:
        d = keys(e["new"]); d.subtract(keys(e["old"]))
        loc.update(d)
        if -d: removed.append(e["key"])
    gate("C10", not removed and +glob == +loc and -glob == -loc, "QUALIFIERS" + (f" removed in {removed}" if removed else ""))
    gate("C11", len(VOCAB.findall(inter)) == len(VOCAB.findall(base)), "VOCAB")
    cell = section(inter, "#### §6.13b A1a", "### §6.14 The $h$-Chart Ledger")
    s7 = section(inter, "## §7. Import Ledger", "### §7.1")
    L = live(inter)
    old_alg = "`[ALG — formal second order; remainder not certified]`"
    ok = ("RID unavailable" not in cell and "RID unavailable" not in s7
          and all(x in cell and x in s7 for x in ("NUMGEN-DEF-N5AS1-DEFECT", "NUMGEN-RESULT-N5AS1-INF1"))
          and "lines 806" not in L and "lines 843" not in L
          and L.count(old_alg) == L.count("at v6.4.18 the same expansion was tagged " + old_alg) == 2
          and "`[THM — conditional on RECOG-THM-R9-MEMORY]`" not in L)
    gate("C12", ok, "IMPORTS")
    r9 = lambda s: [l for l in s.splitlines() if l.startswith("`[THM]` [RID: RECOG-THM-R9-MEMORY]")]
    rows = lambda s: [l for l in s.splitlines() if l.startswith("| A | $0<\\lvert W_0") or l.startswith("| B | $0<\\lvert W_0")]
    ok = len(r9(base)) == 1 and r9(base) == r9(inter) and len(rows(base)) == 2 and rows(base) == rows(inter)
    ok &= all(x in cell and x in s7 for x in ("\\tfrac{3951}{1000}", "\\tfrac{971}{250}", "\\tfrac{256}{225}"))
    gate("C13", ok, "R9/OPEN21")
    hd = lambda s: ([l for l in s.splitlines()[:60] if l.startswith(("# ", "**Date:**", "**Supersedes:**", "**Title:**", "**Scope:**", "**Status summary"))]
                    + [l for l in s.splitlines()[-3:]])
    gate("C14", hd(base) == hd(inter), "HEADER")
    hs = lambda s: [l for l in s.splitlines() if l.startswith("#")]
    gate("C15", [l.replace(*HEAD_73) for l in hs(live(base))] == hs(live(inter)) and HEAD_73[0] in hs(base), "HEADINGS")
    s8 = section(inter, "## §8. Artifact", "## §9.")
    names = set(re.findall(r"`([A-Za-z0-9_.\-]+\.(?:py|json|jsonl|md|txt|zip))`", s8))
    files = files if files is not None else repo_files(root)
    miss = sorted(n for n in names if n not in files and n not in FILE_EXCEPT)
    gate("C16", not miss, f"§8 FILES missing: {miss}" if miss else "§8 FILES")
    ok = all(x in L for x in ("F2(a3)", "W1–W5", "registry-relative", "no identifiable token-specific write-through"))
    r6 = section(inter, "**OPEN R6 — Physical recognition-event rule**", "**OPEN R")
    ok &= any(l.startswith("Status: ACTIVE") for l in r6.splitlines()) and "R6 therefore remains **ACTIVE**" in L
    gate("C17", ok, "LIVE")
    if fc21:
        try:
            m = load_builder(root)
            t, rec = m.apply(base, [e for e in m.EDITS if e[1] != "FC21"])
            ok = not any(x in t for x in NEW_FC21) and set(RID_RECOG.findall(t)) == set(RID_RECOG.findall(base)) | NEW_M
        except AssertionError:
            ok = False
        gate("C18", ok, "DECOUPLE")
    vals = [r"|G|=\tfrac{\sqrt{481897}}{90720}\approx0.0076520", r"|G|/517\approx1.4800743\times10^{-5}",
            r"|G|/163\approx4.6944689\times10^{-5}", r"|\mu|/|c_{05}^{\rm raw}|\approx41.27", r"|\mu|/|a_{05}|\approx59.12",
            r"q_0<|G|/(2C_7)\approx3.83\times10^{-5}", r"$\approx1.28\times10^{-4}$ ($C_7=30$)", r"$Q(T^6(t,0))-t^2=6\gamma t^6+O(t^8)$ of either sign `[ALG]`"]
    gate("C19", all(L.count(v) == 1 for v in vals), "VALUES")
    par = [l for l in L.splitlines() if l.startswith("**Outbound notices; current state.**")]
    ok = (len(par) == 1 and "G3 to OFN and G3 to RRF: prepared" in par[0] and "this release changes none of them" in par[0]
          and "N19 and N21 to RECOG: prepared by Dyadic and not sent" in par[0]
          and not re.search(r"G3 to (OFN|RRF)[^.;]*\b(sent|received|accepted)\b", par[0]))
    gate("C20", ok, "NOTICES")
    glob = Counter(TAGBT.findall(inter)); glob.subtract(Counter(TAGBT.findall(base)))
    loc = Counter()
    for e in edits:
        loc.update(Counter(TAGBT.findall(e["new"]))); loc.subtract(Counter(TAGBT.findall(e["old"])))
    gate("C21", +glob == +loc and -glob == -loc, "TAG CENSUS")
    return res

def controls(base, inter, log, root):
    print("\nNEGATIVE CONTROLS (each must be caught by its target gate):")
    files = repo_files(root)
    L = inter
    def once(s, a, b):
        assert s.count(a) >= 1, a
        return s.replace(a, b, 1)
    def swap(s, a, b):
        i, j = s.find(a), s.find(b)
        assert i >= 0 and j >= 0
        if i > j: a, b, i, j = b, a, j, i
        return s[:i] + b + s[i + len(a):j] + a + s[j + len(b):]
    def outside(s, a, b, anchor="### §6.7 Shear-Jet Law"):
        i = s.find(anchor); j = s.find(a, i)
        return s[:j] + b + s[j + len(a):]
    C = [
     ("NC01 new RID removed", "C7", once(L, "[RID: RECOG-ALG-SWAP-ODD-RHO] ", "")),
     ("NC02 RID attached to another statement", "C8", swap(L, "[RID: RECOG-THM-R9-COMPARATOR-INCOMPLETENESS]", "[RID: RECOG-ALG-LATTICE-MEMORY]")),
     ("NC03 bare [RESULT] reintroduced", "C9", once(L, "`[RESULT]` `[from: THM]` [scope: registry-relative] **F1 conclusion.**", "`[RESULT]` **F1 conclusion.**")),
     ("NC04 combined from-tag reintroduced", "C9", once(L, "`[RESULT]` `[from: THM]` **Separation", "`[RESULT]` `[from: THM, ALG]` **Separation")),
     ("NC05 scope qualifier deleted", "C10", once(L, "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL] [scope: diagnostic twin $T_s$, SG-R4]", "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL]")),
     ("NC06 evidence pointer deleted", "C10", once(L, "`[ALG]` [cert: check 8] **R9 partial budget", "`[ALG]` **R9 partial budget")),
     ("NC07 OPEN status altered (R6)", "C6", once(L, "Status: ACTIVE", "Status: CLOSED")),
     ("NC08 stale state kept (RID unavailable)", "C12", once(L, "[import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 | NUMGEN-RESULT-N5AS1-INF1]", "[import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6, INF-1 | RID unavailable]")),
     ("NC09 Dyadic line pin reinserted", "C12", once(L, "[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14, OPEN 21 (", "[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 843–850 (")),
     ("NC10 R9 statement altered", "C13", outside(L, "$(C_2,q_{\\max})=(517,\\tfrac1{400})$", "$(C_2,q_{\\max})=(163,\\tfrac1{400})$", anchor="#### §6.13a")),
     ("NC11 OPEN 21 rows mixed", "C13", once(L, r"$\tfrac{3951}{1000}$ | $517$ |", r"$\tfrac{3951}{1000}$ | $163$ |")),
     ("NC12 header identity altered", "C14", once(L, "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23")),
     ("NC13 READ/DECODE vocabulary inserted", "C11", once(L, "Owner editions that consume RECOG RIDs", "Owner editions that DECODE RECOG RIDs")),
     ("NC14 Appendix A history edited", "C3", once(L, "G3 notices to OFN, RRF and RER remain unsent.", "G3 notices to OFN, RRF and RER were sent.")),
     ("NC15 §8 evidence file renamed", "C16", outside(L, "`recog_cell_r9_memory_cert.py`", "`recog_cell_r9_memory_cert_v2.py`", anchor="## §8. Artifact")),
     ("NC16 must-stay-live item deleted", "C17", L.replace("F2(a3)", "F2(a)")),
     ("NC17 notice state changed", "C20", once(L, "G3 to OFN and G3 to RRF: prepared", "G3 to OFN and G3 to RRF: sent")),
     ("NC18 wrong value display", "C19", once(L, r"|\mu|/|c_{05}^{\rm raw}|\approx41.27", r"|\mu|/|c_{05}^{\rm raw}|\approx41.3")),
     ("NC19 heading changed", "C15", once(L, "### §6.12 Leading-Return Equivariance and Comparator Closure", "### §6.12 Leading-Return Equivariance")),
     ("NC20 grade changed outside the spans", "C21", outside(L, "`[ALG]`", "`[THM]`")),
     ("NC21 extra undeclared RECOG RID", "C7", once(L, "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE]", "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE-X]")),
     ("NC22 old Dyadic tag form restored", "C12", once(L, "`[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14, primitive-variable form", "`[ALG — formal second order; remainder not certified]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14, primitive-variable form")),
    ]
    allok = True
    for name, target, mtxt in C:
        if mtxt == inter:
            print(f"  {name:<44} NOT CONSTRUCTED"); allok = False; continue
        r = check(base, mtxt, log, root, verbose=False, files=files)
        failed = sorted(k for k, v in r.items() if not v)
        hit = target in failed
        allok &= hit
        print(f"  {name:<44} target {target}: {'caught' if hit else 'NOT CAUGHT'}  (failing: {', '.join(failed)})")
    return allok

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) != 3: print(__doc__); sys.exit(2)
    base = open(a[0], encoding="utf-8").read(); inter = open(a[1], encoding="utf-8").read()
    log = json.load(open(a[2], encoding="utf-8"))
    root = os.getcwd()
    print(f"base {hashlib.sha256(base.encode()).hexdigest()}\nintermediate {hashlib.sha256(inter.encode()).hexdigest()} ({log.get('variant')}, {len(log['edits'])} edits)")
    hb = [l for l in live(base)[:live(base).index('## §7. Import Ledger')].splitlines() if RESULT_LEAD.match(l)]
    nb = sum(1 for l in hb if not (FROM.match(l) and (FROM.match(l).group(1) or FROM.match(l).group(2)) in CANON))
    print(f"calibration: base §§1-6 has {nb} unpaired or combined [RESULT] blocks (advisory count: 19)")
    print("GATES:")
    r = check(base, inter, log, root)
    ok = all(r.values())
    if "--controls" in sys.argv:
        ok &= controls(base, inter, log, root)
    print("\nRESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
