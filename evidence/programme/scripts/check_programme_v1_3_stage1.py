#!/usr/bin/env python3
"""Checker for Programme Overview v1.3 stage 1 (and, with --controls, its negative controls).

usage (repository root):
  python -I evidence/programme/scripts/check_programme_v1_3_stage1.py BASE INTERMEDIATE EDITLOG_JSON [--controls]
exit 0 = every gate PASS (and every control caught by its target gate).

Gates
  G0  BASE        base SHA-256 is programme-v1.2
  G1  BUILD       intermediate == exact-once application of the logged edits to the base; hash == logged hash
  G2  REVERSE     undoing the edits (reverse order, exact-once) recovers the base byte-exactly
  G3  OPEN RIDS   the five programme OPEN RIDs present exactly as in the base; each "**Status:** ACTIVE" line present (5)
  G4  GUARDS      SG-PROG-1..4 headings present; their body text byte-identical to the base
  G5  ANCHORS     every <a id="..."> of the base is present in the intermediate
  G6  TAGS        no [THM], [ALG], [NUM], [ENG], [RESULT] tag introduced; the multiset of [DEF]/[HYP]/[COR] tags unchanged
  G7  INVENTORY   every §6.1 row's tag is a git tag, and its edition equals the tag's version; BASELINE.md agrees
                  (hash of the file at the tag == BASELINE hash where BASELINE lists it)
  G8  IF PINS     every edition pin in §7.2 is either the governing edition or is a version that the named consumer
                  file at its governing tag actually mentions (so no pin is invented)
  G9  SECTIONS    the heading set equals the base heading set plus exactly the declared new/renamed headings
  G10 NO SCIENCE  §6.2-6.5 contain no numerical value with more than 3 significant digits and no theorem statement
                  markers ("⇒", "$$"), i.e. the Programme restates no owner mathematics
  G11 FILENAMES   no versioned DSN filename (RTG_*_v<digits>) in live text (before Appendix A) except the Programme's
                  own titles and release-record names
  G12 METHODOLOGY no "Methodology v1.3" / "DSN_METHODOLOGY_v1.3" as a current pointer in live text (history kept)
"""
import hashlib, json, re, subprocess, sys
from collections import Counter

BASE_SHA = "4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359"
OPEN_RIDS = ["RTG-OPEN-GENERATOR-SELECTION", "RTG-OPEN-DISCRETE-BRIDGE", "RTG-OPEN-TRIAD-PRIMACY-ONTO",
             "RTG-OPEN-TRIAD-REDUCTION", "RTG-OPEN-REGGE-BRIDGE"]
NEW_HEADINGS = {"### 6.2 Governance, foundations, standards and history",
                "### 6.5 Shared infrastructure, noncanonical documents and the derived map",
                "### 8.2 Cross-stream symbol table — κ",
                "### 9.2 Two-pass completion and maintenance record",
                "### v1.3 — 23 October 2026 — DRAFT, stage 1 (corrected intermediate; not adopted)"}
GONE_HEADINGS = {"### 6.2 Governance, foundations and history", "### 6.5 Shared infrastructure", "### 9.2 Two-pass completion"}
CONSUMER_FILES = {"DYAD": "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "TRIAD": "dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md",
                  "GEN": "dsn/RTG_GENESIS_GEOMETRY_DSN.md", "UVM": "dsn/RTG_OPEN_M_DSN.md", "NUMGEN": "dsn/RTG_NUMBER_GENESIS_DSN.md",
                  "RECOG": "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", "DZT": "dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md",
                  "AZ": "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md", "TDRG": "dsn/RTG_DISCRETE_GENESIS_DSN.md",
                  "OFN": "dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md", "RRF": "dsn/RTG_RRF_REPRESENTATION_REGISTRY.md",
                  "PREL": "dsn/RTG_PRE_LEGACY_DSN.md", "RER": "noncanonical/RTG_RELATIONAL_EMERGENCE_REGISTRY.md",
                  "FMS": "noncanonical/FMS_MODEL_SELECTION_LEDGER.md", "ER2B": "noncanonical/RTG_ER2B_CONSOLIDATED_STUDY.md"}

def sha(b): return hashlib.sha256(b.encode("utf-8") if isinstance(b, str) else b).hexdigest()
def git(*a): return subprocess.run(["git", *a], check=True, capture_output=True).stdout

class C:
    def __init__(self): self.rows = []; self.failed = False
    def add(self, g, ok, why):
        self.rows.append((g, ok, why)); self.failed |= not ok
        print(f"{'PASS' if ok else 'FAIL'}  {g:12s} — {why}")

def headings(t): return [l for l in t.split("\n") if l.startswith("#")]
def live(t):
    i = t.find("\n## Appendix A")
    return t if i < 0 else t[:i]

def run(base, inter, log, verbose=True):
    c = C()
    c.add("G0 BASE", sha(base) == BASE_SHA, sha(base)[:12])
    # G1
    t = base; ok = True; why = ""
    for e in log["edits"]:
        if t.count(e["old"]) != 1: ok = False; why = f"{e['key']}: old occurs {t.count(e['old'])}×"; break
        t = t.replace(e["old"], e["new"])
    ok = ok and t == inter and sha(inter) == log["intermediate_sha256"]
    c.add("G1 BUILD", ok, why or f"{len(log['edits'])} edits; hash {sha(inter)[:12]}")
    # G2
    t = inter; ok = True; why = ""
    for e in reversed(log["edits"]):
        if t.count(e["new"]) != 1: ok = False; why = f"{e['key']}: new occurs {t.count(e['new'])}×"; break
        t = t.replace(e["new"], e["old"])
    c.add("G2 REVERSE", ok and t == base, why or "base recovered")
    # G3
    ok = all(inter.count(f"**RID:** `{r}`") == 1 for r in OPEN_RIDS) and inter.count("**Status:** ACTIVE") == 5 == base.count("**Status:** ACTIVE")
    c.add("G3 OPEN RIDS", ok, "5 RIDs, 5 ACTIVE")
    # G4
    def guard_block(t, n):
        i = t.find(f"**[SG-PROG-{n}]"); j = t.find("\n\n", i); return t[i:j]
    ok = all(guard_block(base, n) == guard_block(inter, n) for n in (1, 2, 3, 4))
    c.add("G4 GUARDS", ok, "SG-PROG-1..4 byte-identical")
    # G5
    anchors = re.findall(r'<a id="[^"]+"></a>', base)
    missing = [a for a in anchors if a not in inter]
    c.add("G5 ANCHORS", not missing, f"{len(anchors)} anchors; missing {missing}")
    # G6
    tags = lambda t: Counter(re.findall(r"`\[(DEF|HYP|COR|THM|ALG|NUM|ENG|RESULT|HEUR)[^\]]*\]`", t))
    tb, ti = tags(base), tags(inter)
    bad = [k for k in ("THM", "ALG", "NUM", "ENG", "RESULT") if ti.get(k, 0) > tb.get(k, 0)]
    same = all(tb.get(k, 0) == ti.get(k, 0) for k in ("DEF", "HYP", "COR"))
    c.add("G6 TAGS", not bad and same, f"base {dict(tb)} inter {dict(ti)}")
    # G7
    tagset = set(git("tag").decode().split())
    baseline = open("BASELINE.md", encoding="utf-8").read()
    rows = re.findall(r"^\| (\w+) \| `([^`]+)` \| ([^|]+) \| `([^`]+)` \|", inter[inter.find("### 6.1"):inter.find("### 6.2")], re.M)
    probs = []
    for key, path, edition, tag in rows:
        if key == "PROG": continue
        if tag not in tagset: probs.append(f"{key}: tag {tag} missing"); continue
        ver = tag.split("-v", 1)[1]
        if ver not in edition: probs.append(f"{key}: edition '{edition}' vs tag {tag}")
        h = sha(git("show", f"{tag}:{path}"))
        if h[:8] not in baseline and path.startswith(("dsn/", "noncanonical/")):
            probs.append(f"{key}: hash at tag not in BASELINE")
    prog_row = "| PROG | `dsn/RTG_PROGRAMME_OVERVIEW.md` | v1.3" in inter
    c.add("G7 INVENTORY", not probs and len(rows) == 18 and prog_row, f"{len(rows)} tagged rows + PROG; {probs}")
    # G8
    reg = inter[inter.find("### 7.2"):inter.find("### 7.3")]
    probs = []
    cache = {}
    def mentions(key, ver):
        if key not in CONSUMER_FILES: return True
        if key not in cache: cache[key] = open(CONSUMER_FILES[key], encoding="utf-8").read()
        return ver in cache[key]
    for line in reg.split("\n"):
        if not line.startswith("| IF"): continue
        cells = [x.strip() for x in line.strip("|").split("|")]
        if len(cells) < 6: continue
        declared, pin = cells[4], cells[5]
        cons = re.findall(r"\b(DYAD|TRIAD|GEN|UVM|NUMGEN|RECOG|DZT|AZ|TDRG|OFN|RRF|PREL|RER|FMS|ER2B)\b", declared)
        for v in re.findall(r"v\d+(?:\.\d+)+", pin):
            if cons and not any(mentions(k, v) for k in cons):
                probs.append(f"{cells[0]}: pin {v} not found in {cons}")
    c.add("G8 IF PINS", not probs, probs or "every pin occurs in the named consumer file")
    # G9
    hb, hi = set(headings(base)), set(headings(inter))
    extra = hi - hb; gone = hb - hi
    ok = extra == NEW_HEADINGS | {"# RTG_PROGRAMME_OVERVIEW_v1.3"} and gone == GONE_HEADINGS | {"# RTG_PROGRAMME_OVERVIEW_v1.2"}
    c.add("G9 SECTIONS", ok, f"new {sorted(extra - NEW_HEADINGS)} gone {sorted(gone - GONE_HEADINGS)}")
    # G10
    s6 = inter[inter.find("### 6.2"):inter.find("### 6.6")]
    nums = [m for m in re.findall(r"(?<![\w.`v])\d+\.\d{3,}", s6)]
    ok = not nums and "⇒" not in s6 and "$$" not in s6
    c.add("G10 NO SCIENCE", ok, f"numbers {nums[:3]}")
    # G11
    lt = live(inter)
    fn = [m for m in re.findall(r"RTG_[A-Z_0-9]+_v\d[\d._]*(?:_RELEASE_RECORD)?|DSN_METHODOLOGY_v\d[\d._]*", lt)
          if m not in ("RTG_PROGRAMME_OVERVIEW_v1.2", "RTG_PROGRAMME_OVERVIEW_v1.3", "RTG_PROGRAMME_OVERVIEW_v1.1", "RTG_PROGRAMME_OVERVIEW_v1_1.md")
          and not m.endswith("_RELEASE_RECORD") and (m + "RELEASE_RECORD") not in lt]
    c.add("G11 FILENAMES", not fn, f"versioned filenames in live text: {sorted(set(fn))}")
    # G12
    hits = [l[:90] for l in lt.split("\n") if re.search(r"Methodology v1\.3|DSN_METHODOLOGY_v1\.3|DSN_METHODOLOGY_v1_3", l)
            and not re.search(r"was adopted under v1\.3|v1\.2 was|history|Appendix", l)]
    c.add("G12 METHODOLOGY", not hits, hits or "no stale methodology pointer")
    return c

CONTROLS = [
 ("N1 undeclared edit", lambda i, L: (i.replace("**Status:** ACTIVE", "**Status:** CLOSED", 1), L), "G1 BUILD"),
 ("N2 OPEN status changed and logged", lambda i, L: (i.replace("**Status:** ACTIVE", "**Status:** CLOSED", 1), addlog(L, "**Status:** ACTIVE", "**Status:** CLOSED")), "G3 OPEN RIDS"),
 ("N3 guard text edited and logged", lambda i, L: (i.replace("No physical dynamical law, coefficient,", "No physical law, coefficient,", 1), addlog(L, "No physical dynamical law, coefficient,", "No physical law, coefficient,")), "G4 GUARDS"),
 ("N4 anchor removed", lambda i, L: (i.replace('<a id="prog-guards"></a>\n', "", 1), addlog(L, '<a id="prog-guards"></a>\n', "")), "G5 ANCHORS"),
 ("N5 THM tag introduced", lambda i, L: (i.replace("`[DEF]` Tier numbers", "`[THM]` Tier numbers", 1), addlog(L, "`[DEF]` Tier numbers", "`[THM]` Tier numbers")), "G6 TAGS"),
 ("N6 inventory edition wrong", lambda i, L: (i.replace("| v6.4.22 | `dyad-v6.4.22` |", "| v6.4.21 | `dyad-v6.4.22` |", 1), addlog(L, "| v6.4.22 | `dyad-v6.4.22` |", "| v6.4.21 | `dyad-v6.4.22` |")), "G7 INVENTORY"),
 ("N7 inventory tag nonexistent", lambda i, L: (i.replace("`numgen-v1.20.8` | canonical common home", "`numgen-v1.20.9` | canonical common home", 1), addlog(L, "`numgen-v1.20.8` | canonical common home", "`numgen-v1.20.9` | canonical common home")), "G7 INVENTORY"),
 ("N8 invented consumer pin", lambda i, L: (i.replace("| GEN §7 | v6.4.13 |", "| GEN §7 | v6.4.99 |", 1), addlog(L, "| GEN §7 | v6.4.13 |", "| GEN §7 | v6.4.99 |")), "G8 IF PINS"),
 ("N9 science restated in §6", lambda i, L: (i.replace("Owns the selected primitive map,", "Owns the selected primitive map, |G|=0.0076520 ⇒", 1), addlog(L, "Owns the selected primitive map,", "Owns the selected primitive map, |G|=0.0076520 ⇒")), "G10 NO SCIENCE"),
 ("N10 versioned filename in live text", lambda i, L: (i.replace("(v0.8, `dzt-v0.8`)", "(`RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0_8.md`)", 1), addlog(L, "(v0.8, `dzt-v0.8`)", "(`RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0_8.md`)")), "G11 FILENAMES"),
 ("N11 stale methodology pointer", lambda i, L: (i.replace("The namespace registry is **Methodology v1.4 §4.2**", "The namespace registry is **Methodology v1.3 §4.2**", 1), addlog(L, "The namespace registry is **Methodology v1.4 §4.2**", "The namespace registry is **Methodology v1.3 §4.2**")), "G12 METHODOLOGY"),
 ("N12 heading removed", lambda i, L: (i.replace("### 8.2 Cross-stream symbol table — κ\n", "### 8.2 Symbol table\n", 1), addlog(L, "### 8.2 Cross-stream symbol table — κ\n", "### 8.2 Symbol table\n")), "G9 SECTIONS"),
]

def addlog(L, old, new):
    L2 = json.loads(json.dumps(L)); L2["edits"].append(dict(key="X", old=old, new=new)); return L2

def main():
    base = open(sys.argv[1], encoding="utf-8").read()
    inter = open(sys.argv[2], encoding="utf-8").read()
    log = json.load(open(sys.argv[3], encoding="utf-8"))
    c = run(base, inter, log)
    print("RESULT:", "FAIL" if c.failed else "PASS")
    rc = 1 if c.failed else 0
    if "--controls" in sys.argv:
        print("\n== negative controls ==")
        caught = 0
        for name, mut, gate in CONTROLS:
            i2, L2 = mut(inter, log)
            L2["intermediate_sha256"] = sha(i2)
            import io, contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                cc = run(base, i2, L2)
            failed = {g for g, ok, _ in cc.rows if not ok}
            ok = gate in failed
            caught += ok
            print(f"{'ok ' if ok else 'MISS'} {name:40s} expect FAIL at {gate}; failed gates: {sorted(failed)}")
        print(f"CONTROLS: {caught}/{len(CONTROLS)} caught")
        rc |= 0 if caught == len(CONTROLS) else 2
    sys.exit(rc)

if __name__ == "__main__":
    main()
