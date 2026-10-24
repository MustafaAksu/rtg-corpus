#!/usr/bin/env python3
"""check_recog_v0_3_24_stage1.py -- deterministic checker for the RECOG v0.3.24 stage-1 intermediate.

usage (from the repository root):
  python -I evidence/recog/scripts/check_recog_v0_3_24_stage1.py BASE INTERMEDIATE EDITLOG_JSON [--controls]
  BASE = `git show recog-v0.3.23:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`; EDITLOG_JSON written by the builder
  (any group variant: the gates read the declared groups from the log).
exit 0 = every gate PASS (and, with --controls, every negative control caught by its target gate).

Gates (as v0.3.23 stage 1, with the v0.3.24 declarations):
  C0  BASE       base SHA-256 is the adopted v0.3.23 identity (tag recog-v0.3.23)
  C1  BUILD      intermediate == exact-once application of the logged edits (Appendix A masked for "live")
  C2  REVERSE    undoing every edit recovers the base byte-exactly
  C3  APPENDIX A Appendix A minus the new v0.3.24 entry is byte-identical to the base Appendix A
  C4  SPAN TAGS  edits whose backticked tag multiset changes are exactly the declared TAG_CHANGE edits
  C5  SPAN RIDS  per edit every [RID: X] of the old text survives unless the edit is a declared history move
                 (MNT spans whose removed RIDs are owner RIDs cited elsewhere in the live text); added RIDs are declared
  C6  STATUS     OPEN-registry "Status:" lines: the status word of every line is unchanged; only the declared R8/R9
                 history sentences change
  C7  RID SET    RECOG RID set == base set + the declared new RIDs of the built groups; none removed
  C8  RID ATTACH for every pre-existing RECOG RID declaration the after-text is unchanged; new RIDs attach to their
                 declared statements
  C9  RESULT     in §§1-6 every line-leading [RESULT] is followed by [from: TAG] with one canonical tag
  C10 QUALIFIERS no edit outside the declared MNT history moves removes a qualifier; global change == sum of per-edit
                 changes; the MNT moves remove only qualifiers that sit in the moved history
  C11 VOCAB      no READ / WRITE / DECODE vocabulary introduced
  C12 IMPORTS    v0.3.23 import state kept (no "RID unavailable"; both NUMGEN RIDs; no Dyadic line pins; owner tag forms)
  C13 R9/OPEN21  the RECOG-THM-R9-MEMORY statement line and the (c) row table are unchanged; OPEN 21 constants present
  C14 HEADER     title, date, supersedes, status summary and footer unchanged
  C15 HEADINGS   heading lines equal the base
  C16 §8 FILES   every backticked file name in §8 exists in the repository; every SHA-256 quoted in the new §8 rows is the
                 hash of the named repository file
  C17 LIVE       must-stay-live items present (F2(a3), W1-W5, R6 ACTIVE, registry-relative, no write-through); R4 ACTIVE
  C18 DECOUPLE   each single-group variant builds and carries exactly its own new RIDs
  C19 VALUES     the constants displayed in the new blocks agree with the certificate outputs in the repository
  C20 NOTICES    the §7.2 outbound-notices paragraph is unchanged (no notice state changed)
  C21 TAG CENSUS global backticked-tag multiset delta == sum of the per-edit deltas
  C22 HISTORY    every MNT pointer names the predecessor tag, and the pointed-to passages exist at that tag
"""
import hashlib, importlib.util, json, os, re, subprocess, sys, zipfile
from collections import Counter

BASE_SHA = "0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a"
PREV_TAG = "recog-v0.3.23"
APPA_START, APPA_END = "## Appendix A — Version History", "## Appendix B —"
NEW_RIDS = {
 "A1B": {"RECOG-THM-A1B-SLIP-SCHEDULE-U", "RECOG-ART-A1B-SIXSTEP-DEFICIT"},
 "A1C": {"RECOG-RESULT-A1C-RECORD-PHASE-READOUT"},
 "A3": {"RECOG-ALG-QUADRATURE-TYPING", "RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY", "RECOG-ART-A3-QUADRATURE-TYPING"},
 "MNT": set(),
}
ATTACH = {
 "RECOG-THM-A1B-SLIP-SCHEDULE-U": " [scope: conditional on postulated $T$ (OPEN-P0); $x_0\\in U=\\{0<Q_0\\le\\tfrac1{625}\\}$; lifted primitive chart",
 "RECOG-ART-A1B-SIXSTEP-DEFICIT": " `[v0.3.24]` :: `recog_a1b_sixstep_deficit_cert.py`",
 "RECOG-RESULT-A1C-RECORD-PHASE-READOUT": " [scope: $x_0\\in U$; the complete infinite token record",
 "RECOG-ALG-QUADRATURE-TYPING": " [scope: conditional on postulated $T$ (OPEN-P0); dyad observables",
 "RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY": " [scope: conditional on postulated $T$ (OPEN-P0); wrapped cylinder",
 "RECOG-ART-A3-QUADRATURE-TYPING": " `[v0.3.24]` :: `recog_a3_quadrature_typing.py`",
}
TAG_CHANGE = {
 "S1-A1B": "§1 A1b summary (new [THM])", "S1-A3a": "§1 inventory line (new [ALG])", "S1-A3b": "§1 quadrature line (new [ALG])",
 "S2-R4": "R4 sub-items re-worded ([OPEN] count unchanged, [NUM] pointer added)", "S2-R6": "R6 sub-items (new [RESULT], two [OPEN])",
 "S63-A3": "inventory block (new [ALG], [NUM])", "S65-A3": "typing block (new [ALG], [scope], [NUM])",
 "S613-A1B": "A1b block (new [THM], [NUM])", "S616e-A1C": "A1c block (new [RESULT], [from: THM], [NUM])",
 "S8-A1B": "A1b artifact row ([v0.3.24], [NUM], [THM])", "S8-A3": "A3 artifact row ([v0.3.24], [NUM], [ALG])",
 "M-R8b": "R8 history moved ([NUM strong] in the moved text)", "M-R9b": "R9 history moved ([ALG] budget paragraph)",
 "M-R11": "R11 history moved (five [OPEN] sub-items)", "M-71": "§7.1 table moved (grade tags in cells)",
 "A-1": "Appendix A entry quotes tags",
}
MNT_MOVES = {"M-R8b", "M-R9b", "M-R11", "M-71", "M-72"}
IMPORT_RIDS_ALLOWED = {"DYAD-THM-LPHASE-ROWA-REMAINDER", "DYAD-THM-NF-REM", "DYAD-THM-PRIM-CTR", "DYAD-THM-C21"}
STATUS_HISTORY = {"R8": ("Text below retained as the v0.3.2 specification;", "The primitive entry criterion of the v0.3.2 specification"),
                  "R9": ("The text below is retained as the historical v0.3.2 specification;", "The historical v0.3.2 specification (target, chart-native inputs")}
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
SHA = re.compile(r"`([0-9a-f]{64})`")

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
    p = os.path.join(root, "evidence/recog/scripts/build_recog_v0_3_24_stage1.py")
    spec = importlib.util.spec_from_file_location("b", p); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m
def git_show(root, tag, path):
    try: return subprocess.run(["git", "-C", root, "show", f"{tag}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")
    except Exception: return None

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
    i = ai.find("### v0.3.24"); j = ai.find("### v0.3.23", i)
    gate("C3", i > 0 and j > i and ai[:i] + ai[j:] == ab, "APPENDIX A")
    changed = {e["key"] for e in edits if Counter(TAGBT.findall(e["old"])) != Counter(TAGBT.findall(e["new"]))}
    declared = {k for k in TAG_CHANGE if any(e["key"] == k for e in edits)}
    gate("C4", changed == declared, f"SPAN TAGS {sorted(changed ^ declared) if changed != declared else ''}")
    bad = []
    L = live(inter)
    for e in edits:
        ro, rn = ANYRID.findall(e["old"]), ANYRID.findall(e["new"])
        lost = [x for x in ro if x not in rn]
        if e["key"] in MNT_MOVES:
            if any(x.startswith("RECOG-") or f"[RID: {x}" not in L for x in lost): bad.append(e["key"])
        elif lost: bad.append(e["key"])
        if any(x not in ro and x not in new_rids | IMPORT_RIDS_ALLOWED for x in rn): bad.append(e["key"])
    gate("C5", not bad, f"SPAN RIDS {bad}")
    st = lambda s: [l for l in live(s).splitlines() if l.startswith("Status:")]
    sb, si = st(base), st(inter)
    word = lambda l: re.match(r"Status: \**([A-Z]+)", l).group(1) if re.match(r"Status: \**([A-Z]+)", l) else l
    diff = [(a, b) for a, b in zip(sb, si) if a != b]
    ok = len(sb) == len(si) and [word(l) for l in sb] == [word(l) for l in si]
    ok &= all(any(a.find(o) >= 0 and b.find(n) >= 0 for o, n in STATUS_HISTORY.values()) for a, b in diff)
    gate("C6", ok, f"STATUS ({len(diff)} declared history sentences)")
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
        if -d and e["key"] not in MNT_MOVES: removed.append(e["key"])
    gate("C10", not removed and +glob == +loc and -glob == -loc, "QUALIFIERS" + (f" removed in {removed}" if removed else ""))
    gate("C11", len(VOCAB.findall(inter)) == len(VOCAB.findall(base)), "VOCAB")
    cell = section(inter, "#### §6.13b A1a", "### §6.14 The $h$-Chart Ledger")
    s7 = section(inter, "## §7. Import Ledger", "### §7.1")
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
    hd = lambda s: ([l for l in s.splitlines()[:60] if l.startswith(("# ", "**Date:**", "**Supersedes:**", "**Title:**", "**Scope:**", "**Status summary"))] + s.splitlines()[-3:])
    gate("C14", hd(base) == hd(inter), "HEADER")
    hs = lambda s: [l for l in s.splitlines() if l.startswith("#")]
    gate("C15", hs(live(base)) == hs(live(inter)), "HEADINGS")
    s8 = section(inter, "## §8. Artifact", "## §9.")
    names = set(re.findall(r"`([A-Za-z0-9_.\-]+\.(?:py|json|jsonl|md|txt|zip))`", s8)) | {os.path.basename(x) for x in re.findall(r"`((?:evidence|records)/[^`]+\.(?:py|json|jsonl|md|txt))`", s8)}
    fl, paths = files if files is not None else repo_files(root)
    miss = sorted(n for n in names if n not in fl and n not in FILE_EXCEPT)
    hashok = True
    for row in [l for l in s8.splitlines() if "`[v0.3.24]`" in l]:
        for fname, h in re.findall(r"`(?:(?:evidence|records)/[^`]+/)?([A-Za-z0-9_.\-]+\.(?:py|json|md))`(?: v0\.2(?:\.2)?)? \(?(?:sha256 )?`([0-9a-f]{64})`", row):
            ps = paths.get(fname, [])
            hashok &= any(hashlib.sha256(open(p, "rb").read()).hexdigest() == h for p in ps)
    gate("C16", not miss and hashok, f"§8 FILES missing: {miss}" if miss else ("§8 FILES" if hashok else "§8 FILES: quoted hash mismatch"))
    ok = all(x in L for x in ("F2(a3)", "W1–W5", "registry-relative", "no identifiable token-specific write-through"))
    r6 = section(inter, "**OPEN R6 — Physical recognition-event rule**", "**OPEN R")
    r4 = section(inter, "**OPEN R4 — Intrinsic type-change locus**", "**OPEN R")
    ok &= any(l.startswith("Status: ACTIVE") for l in r6.splitlines()) and "R6 therefore remains **ACTIVE**" in L
    ok &= any(l.startswith("Status: ACTIVE") for l in r4.splitlines())
    gate("C17", ok, "LIVE")
    ok = True
    try:
        m = load_builder(root)
        for g in ("A1B", "A1C", "A3", "MNT"):
            eds = [e for e in m.EDITS if e[0] != "A-1" and e[1] == g]
            if g == "A3":
                eds = [e for e in eds if e[0] != "S8-A3"]
                a3row = [e for e in m.EDITS if e[0] == "S8-A3"][0][6].split("\n", 1)[1]
                eds.append(("S8-A3", "A3", "", "line", "live", r"- [RID: RECOG-ART-A1A-EXISTENCE-U] `[v0.3.23]`", "{LINE}\n" + a3row))
            eds.append(m.appa_edit({g}))
            t, _ = m.apply(base, eds)
            ok &= set(RID_RECOG.findall(t)) == set(RID_RECOG.findall(base)) | NEW_RIDS[g]
    except AssertionError:
        ok = False
    gate("C18", ok, "DECOUPLE")
    ok = True
    try:
        if "A1B" in groups:
            d = json.load(open(os.path.join(root, "evidence/recog/a1b_a1c/a1b_sixstep_deficit_cert.json")))
            ok &= d["ALL_PASS"] and d["G6_H_lt_1783_over_1000"] and d["G8_upper_branch_bound"] < 1.818 and d["G8_lower_branch_bound"] < 1.788 and d["G8_positivity_ratio_bound"] > 0.927
            ok &= all(x in L for x in ("0.927\\,\\tau Q(y)>0", "1.82\\,Q(y)^{3/2}", "H<\\tfrac{1783}{1000}", "upper $1.8170<1.818$, lower $1.7876<1.788$, positivity $0.92725>0.927$"))
            ok &= abs(d["G8_upper_branch_bound"] - 1.8170) < 5e-4 and abs(d["G8_lower_branch_bound"] - 1.7876) < 5e-4 and abs(d["G8_positivity_ratio_bound"] - 0.92725) < 5e-5
        if "A3" in groups:
            d = json.load(open(os.path.join(root, "evidence/recog/a3_quadrature/a3_quadrature_typing.json")))
            ok &= d["ALL_PASS"] and d["Q4_chartA"]["hyperbolic_instance"] and d["Q4_chartA"]["elliptic_instance"] and d["Q4_chartB"]["identity_on_branch_pi_over_2"]
            orbs = d["NUM_periodic_orbit_probe"]["orbits"]
            ok &= len(orbs) == 18 and "18 orbits" in L and "11 further orbits uncertified" in L
            ok &= min(o["min_abs_cos_eta"] for o in orbs) > 0
    except Exception:
        ok = False
    gate("C19", ok, "VALUES")
    par = lambda s: [l for l in live(s).splitlines() if l.startswith("**Outbound notices; current state.**")]
    gate("C20", len(par(base)) == 1 and par(base) == par(inter), "NOTICES")
    glob = Counter(TAGBT.findall(inter)); glob.subtract(Counter(TAGBT.findall(base)))
    loc = Counter()
    for e in edits:
        loc.update(Counter(TAGBT.findall(e["new"]))); loc.subtract(Counter(TAGBT.findall(e["old"])))
    gate("C21", +glob == +loc and -glob == -loc, "TAG CENSUS")
    ok = True
    prev = git_show(root, PREV_TAG, "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md")
    if prev is None: ok = False
    else:
        for e in edits:
            if e["key"] in MNT_MOVES:
                ok &= f"`{PREV_TAG}`" in e["new"] and e["old"] in prev and e["new"] in L
    gate("C22", ok, "HISTORY")
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
     ("NC01 new RID removed", "C7", once(L, "[RID: RECOG-ALG-QUADRATURE-TYPING] ", "")),
     ("NC02 RID attached to another statement", "C8", swap(L, "[RID: RECOG-THM-R9-COMPARATOR-INCOMPLETENESS]", "[RID: RECOG-ALG-LATTICE-MEMORY]")),
     ("NC03 bare [RESULT] reintroduced", "C9", once(L, "`[RESULT]` `[from: THM]` [RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT]", "`[RESULT]` [RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT]")),
     ("NC04 scope qualifier deleted", "C10", once(L, "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL] [scope: diagnostic twin $T_s$, SG-R4]", "[RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL]")),
     ("NC05 OPEN status altered (R4 closed)", "C6", once(L, "**OPEN R4 — Intrinsic type-change locus** [RID: RECOG-OPEN-TYPE-CHANGE]\n\nStatus: ACTIVE", "**OPEN R4 — Intrinsic type-change locus** [RID: RECOG-OPEN-TYPE-CHANGE]\n\nStatus: CLOSED")),
     ("NC06 header identity altered", "C14", once(L, "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.24")),
     ("NC07 READ/DECODE vocabulary inserted", "C11", once(L, "Owner editions that consume RECOG RIDs", "Owner editions that DECODE RECOG RIDs")),
     ("NC08 Appendix A history edited", "C3", once(L, "### v0.3.23 — 23 October 2026 — Adopted", "### v0.3.23 — 24 October 2026 — Adopted")),
     ("NC09 §8 quoted hash altered", "C16", once(L, "`b418af086dfb7515faff5d266a7ea1d2e7f76efb74421021268c14495a1b35b0`", "`b418af086dfb7515faff5d266a7ea1d2e7f76efb74421021268c14495a1b35b1`")),
     ("NC10 §8 evidence file renamed", "C16", once(L, "`recog_a3_quadrature_typing.py` (sha256", "`recog_a3_quadrature_typing_v2.py` (sha256")),
     ("NC11 must-stay-live item deleted", "C17", L.replace("F2(a3)", "F2(a)")),
     ("NC12 notice state changed", "C20", once(L, "G3 to OFN and G3 to RRF: prepared", "G3 to OFN and G3 to RRF: sent")),
     ("NC13 wrong value display (A1b constant)", "C19", once(L, "upper $1.8170<1.818$, lower $1.7876<1.788$, positivity $0.92725>0.927$", "upper $1.8160<1.818$, lower $1.7876<1.788$, positivity $0.92725>0.927$")),
     ("NC14 heading changed", "C15", once(L, "### §6.12 Leading-Return Equivariance and Comparator Closure", "### §6.12 Leading-Return Equivariance")),
     ("NC15 grade changed outside the spans", "C21", outside(L, "`[ALG]`", "`[THM]`")),
     ("NC16 extra undeclared RECOG RID", "C7", once(L, "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE]", "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE-X]")),
     ("NC17 R9 statement altered", "C13", outside(L, "$(C_2,q_{\\max})=(517,\\tfrac1{400})$", "$(C_2,q_{\\max})=(163,\\tfrac1{400})$", anchor="#### §6.13a")),
     ("NC18 history pointer without the tag", "C22", L.replace("`recog-v0.3.23` §2, OPEN R11", "an earlier edition §2, OPEN R11")),
     ("NC19 R6 sub-item status altered", "C17", once(L, "Status: ACTIVE (sharpened v0.3; identifiability audited v0.3.7)", "Status: PARTIAL (sharpened v0.3; identifiability audited v0.3.7)")),
     ("NC20 stale state restored (RID unavailable)", "C12", once(L, "[import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 | NUMGEN-RESULT-N5AS1-INF1]", "[import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6, INF-1 | RID unavailable]")),
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
