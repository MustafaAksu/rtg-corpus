#!/usr/bin/env python3
"""Checker for the Programme Overview v1.4 candidate (and, with --controls, its negative controls).

usage (repository root; needs the git tags):
  python -I evidence/programme/scripts/check_programme_v1_4.py BASE CANDIDATE EDITLOG_JSON [--controls]
exit 0 = every gate PASS (and every control caught by its target gate).

Gates
  C0  BASE        base SHA-256 is programme-v1.3
  C1  BUILD       candidate == exact-once application of the logged edits to the base; hash == logged hash
  C2  REVERSE     undoing the edits (reverse order, exact-once) recovers the base byte-exactly
  C3  OPEN RIDS   the five programme OPEN RIDs present exactly once; five "**Status:** ACTIVE" lines, as in the base
  C4  GUARDS      SG-PROG-1..4 blocks byte-identical to the base
  C5  ANCHORS     every <a id="..."> of the base is present
  C6  TAGS        no [THM]/[ALG]/[NUM]/[ENG]/[RESULT] introduced; the [DEF]/[HYP]/[COR] multiset unchanged
  C7  INVENTORY   every §6.1 row (except PROG) names an existing tag whose version is the row's edition, the tag is the
                  latest tag of its prefix, and the file at the tag has the SHA-256 that BASELINE.md lists for it
  C8  IF PINS     every version in a §7.2 pin cell occurs in the named consumer file read at its governing tag
  C9  SECTIONS    heading set = base heading set, except the title and the one new Appendix A entry
  C10 NO SCIENCE  §6.2-6.5 carry no number with 3+ decimals and no "⇒" / "$$"
  C11 FILENAMES   no versioned DSN filename in live text (before Appendix A) except the Programme's own titles/records
  C12 METHODOLOGY no "Methodology v1.3" as a current pointer in live text
  C13 APPENDIX B  Appendix B byte-identical to the base
  C14 STALE       §6.1-6.5 name no superseded tag of a study whose row moved (e.g. `dyad-v6.4.22`), and every
                  "(vX, `prefix-vX`)" entry heading in §6.2-6.5 names the latest tag of its prefix
  C15 RECEIVERS   the four pipes/PROG items are answered in the text: OFN v0.12 at the two §5 criterion pointers;
                  κ_f row; class-C row without "atlas reading"; CN-05 receipt line; IF07 at v1.7
  C16 IF IDS      §7.2 rows are IF01..IF38, each once, in order
  C17 SOURCE TYPE OFN's claim-level import sources are read from OFN §11.2 and §11.4 at its governing tag (the
                  owner files named in its IMP entries). Every owner the Programme calls an import into OFN (the
                  §6.2 OFN entry, the §7.1 "OFN <--" line, the declared-import part of each "→ OFN" row of §7.2) is in
                  that set; every owner it calls reference-only is not (review PR #179, R1)
"""
import hashlib, json, re, subprocess, sys, io, contextlib
from collections import Counter

BASE_SHA = "1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06"
OPEN_RIDS = ["RTG-OPEN-GENERATOR-SELECTION", "RTG-OPEN-DISCRETE-BRIDGE", "RTG-OPEN-TRIAD-PRIMACY-ONTO",
             "RTG-OPEN-TRIAD-REDUCTION", "RTG-OPEN-REGGE-BRIDGE"]
CONSUMERS = {"DYAD": "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "TRIAD": "dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md",
             "GEN": "dsn/RTG_GENESIS_GEOMETRY_DSN.md", "UVM": "dsn/RTG_OPEN_M_DSN.md", "NUMGEN": "dsn/RTG_NUMBER_GENESIS_DSN.md",
             "RECOG": "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", "DZT": "dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md",
             "AZ": "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md", "TDRG": "dsn/RTG_DISCRETE_GENESIS_DSN.md",
             "OFN": "dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md", "RRF": "dsn/RTG_RRF_REPRESENTATION_REGISTRY.md",
             "PREL": "dsn/RTG_PRE_LEGACY_DSN.md", "RER": "noncanonical/RTG_RELATIONAL_EMERGENCE_REGISTRY.md",
             "FMS": "noncanonical/FMS_MODEL_SELECTION_LEDGER.md", "ER2B": "noncanonical/RTG_ER2B_CONSOLIDATED_STUDY.md"}
PREFIX = {"DYAD": "dyad", "TRIAD": "triad", "GEN": "gen", "UVM": "uvm", "NUMGEN": "numgen", "RECOG": "recog", "DZT": "dzt",
          "AZ": "az", "TDRG": "tdrg", "OFN": "ofn", "RRF": "rrf", "PREL": "prelegacy", "RER": "rer", "FMS": "fms", "ER2B": "er2b"}
MOVED_OLD_TAGS = ["ofn-v0.10", "numgen-v1.20.8", "dyad-v6.4.22", "triad-v1.6.1", "gen-v2.8.9", "recog-v0.3.23",
                  "tdrg-v2.12.13", "atlas-v0.3"]

def sha(b): return hashlib.sha256(b.encode("utf-8") if isinstance(b, str) else b).hexdigest()
def git(*a): return subprocess.run(["git", *a], check=True, capture_output=True).stdout
def vkey(t): return [int(x) for x in t.split("-v", 1)[1].split(".")]

TAGS = git("tag").decode().split()
def latest(prefix):
    c = [t for t in TAGS if t.startswith(prefix + "-v") and re.fullmatch(r"[a-z0-9]+-v\d+(\.\d+)*", t)]
    return max(c, key=vkey) if c else None
_cache = {}
def at_tag(tag, path):
    if (tag, path) not in _cache: _cache[(tag, path)] = git("show", f"{tag}:{path}")
    return _cache[(tag, path)]

class C:
    def __init__(self): self.rows = []; self.failed = False
    def add(self, g, ok, why):
        self.rows.append((g, ok, why)); self.failed |= not ok
        print(f"{'PASS' if ok else 'FAIL'}  {g:14s} — {why}")

def headings(t): return [l for l in t.split("\n") if l.startswith("#")]
def live(t):
    i = t.find("\n## Appendix A"); return t if i < 0 else t[:i]
def section(t, a, b):
    i = t.find(a); j = t.find(b, i + 1); return t[i:j]

def run(base, cand, log):
    c = C()
    c.add("C0 BASE", sha(base) == BASE_SHA, sha(base)[:12])
    t = base; ok = True; why = ""
    for e in log["edits"]:
        if t.count(e["old"]) != 1: ok = False; why = f"{e['key']}: old occurs {t.count(e['old'])}x"; break
        t = t.replace(e["old"], e["new"])
    ok = ok and t == cand and sha(cand) == log["candidate_sha256"]
    c.add("C1 BUILD", ok, why or f"{len(log['edits'])} edits; candidate {sha(cand)[:12]}")
    t = cand; ok = True; why = ""
    for e in reversed(log["edits"]):
        if t.count(e["new"]) != 1: ok = False; why = f"{e['key']}: new occurs {t.count(e['new'])}x"; break
        t = t.replace(e["new"], e["old"])
    c.add("C2 REVERSE", ok and t == base, why or "base recovered")
    ok = all(cand.count(f"**RID:** `{r}`") == 1 for r in OPEN_RIDS) and cand.count("**Status:** ACTIVE") == 5 == base.count("**Status:** ACTIVE")
    c.add("C3 OPEN RIDS", ok, "5 RIDs, 5 ACTIVE")
    def guard(t, n):
        i = t.find(f"**[SG-PROG-{n}]"); j = t.find("\n\n", i); return t[i:j]
    c.add("C4 GUARDS", all(guard(base, n) == guard(cand, n) and guard(base, n) for n in (1, 2, 3, 4)), "SG-PROG-1..4 byte-identical")
    anchors = re.findall(r'<a id="[^"]+"></a>', base); missing = [a for a in anchors if a not in cand]
    c.add("C5 ANCHORS", not missing, f"{len(anchors)} anchors; missing {missing}")
    tg = lambda t: Counter(re.findall(r"`\[(DEF|HYP|COR|THM|ALG|NUM|ENG|RESULT|HEUR)[^\]]*\]`", t))
    tb, tc = tg(base), tg(cand)
    bad = [k for k in ("THM", "ALG", "NUM", "ENG", "RESULT") if tc.get(k, 0) > tb.get(k, 0)]
    same = all(tb.get(k, 0) == tc.get(k, 0) for k in ("DEF", "HYP", "COR"))
    c.add("C6 TAGS", not bad and same, f"base {dict(tb)} cand {dict(tc)}")
    # C7
    baseline = open("BASELINE.md", encoding="utf-8").read()
    bl = {m.group(1): m.group(2) for m in re.finditer(r"^\| [^|]+ \| `([^`]+)` \| [^|]+ \| `([0-9a-f]{64})` \|", baseline, re.M)}
    inv = section(cand, "### 6.1", "### 6.2")
    rows = re.findall(r"^\| (\w+) \| `([^`]+)` \| ([^|]+) \| `([^`]+)`", inv, re.M)
    probs = []
    for key, path, edition, tag in rows:
        if key == "PROG": continue
        if tag not in TAGS: probs.append(f"{key}: tag {tag} missing"); continue
        ver = tag.split("-v", 1)[1]
        if not re.match(rf"v{re.escape(ver)}\b", edition.strip()): probs.append(f"{key}: edition '{edition.strip()}' vs {tag}")
        if latest(tag.split("-v")[0]) != tag: probs.append(f"{key}: {tag} is not the latest tag ({latest(tag.split('-v')[0])})")
        if path.startswith(("dsn/", "noncanonical/")):
            h = sha(at_tag(tag, path)); b = bl.get(path.split("/", 1)[1])
            if b != h: probs.append(f"{key}: hash at {tag} {h[:8]} != BASELINE {str(b)[:8]}")
    prog = re.search(r"^\| PROG \| `dsn/RTG_PROGRAMME_OVERVIEW.md` \| v1\.4 ", inv, re.M) is not None
    c.add("C7 INVENTORY", not probs and len(rows) == 19 and prog, f"{len(rows)} rows; {probs or 'all at latest tag; hashes = BASELINE'}")
    # C8
    reg = section(cand, "### 7.2", "### 7.3"); probs = []; n = 0
    for line in reg.split("\n"):
        if not line.startswith("| IF"): continue
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells) != 6: probs.append(f"{cells[0]}: {len(cells)} cells"); continue
        cons = re.findall(r"\b(" + "|".join(CONSUMERS) + r")\b", cells[4])
        for v in re.findall(r"v\d+(?:\.\d+)+", cells[5]):
            n += 1
            if cons and not any(v in at_tag(latest(PREFIX[k]), CONSUMERS[k]).decode("utf-8") for k in cons):
                probs.append(f"{cells[0]}: pin {v} not in {cons} at governing tag")
    c.add("C8 IF PINS", not probs, probs or f"{n} pins; each occurs in the named consumer at its governing tag")
    # C9
    hb, hc = set(headings(base)), set(headings(cand))
    ok = hc - hb == {"# RTG_PROGRAMME_OVERVIEW_v1.4", "### v1.4 — 4 November 2026 — DRAFT (candidate; not adopted)"} and hb - hc == {"# RTG_PROGRAMME_OVERVIEW_v1.3"}
    c.add("C9 SECTIONS", ok, f"new {sorted(hc - hb)} gone {sorted(hb - hc)}")
    s6 = section(cand, "### 6.2", "### 6.6")
    nums = re.findall(r"(?<![\w.`v])\d+\.\d{3,}", s6)
    c.add("C10 NO SCIENCE", not nums and "⇒" not in s6 and "$$" not in s6, f"numbers {nums[:3]}")
    lt = live(cand)
    fn = [m for m in re.findall(r"RTG_[A-Z_0-9]+_v\d[\d._]*(?:_RELEASE_RECORD)?|DSN_METHODOLOGY_v\d[\d._]*", lt)
          if not m.startswith("RTG_PROGRAMME_OVERVIEW_v1") and not m.endswith("_RELEASE_RECORD")]
    c.add("C11 FILENAMES", not fn, f"versioned filenames in live text: {sorted(set(fn))}")
    hits = [l[:90] for l in lt.split("\n") if re.search(r"Methodology v1\.3|DSN_METHODOLOGY_v1\.3", l)]
    c.add("C12 METHODOLOGY", not hits, hits or "no stale methodology pointer")
    ab = lambda t: t[t.find("## Appendix B"):t.find("*END OF DOCUMENT")]
    c.add("C13 APPENDIX B", ab(base) == ab(cand) and len(ab(base)) > 1000, "byte-identical")
    s61_65 = section(cand, "### 6.1", "### 6.6"); probs = [t for t in MOVED_OLD_TAGS if t in s61_65]
    for m in re.finditer(r"^\*\*(\w+) — [^*]+\*\* \((v[\d.]+)[^,)]*, `([a-z0-9]+-v[\d.]+)`", s6, re.M):
        if latest(m.group(3).split("-v")[0]) != m.group(3): probs.append(f"{m.group(1)}: {m.group(3)} not latest")
    c.add("C14 STALE", not probs, probs or "no superseded tag in §6.1-6.5; entry headings at latest tags")
    p0 = re.search(r"^\*\*Owner study:\*\* Programme Overview for coordination; OFN \(admissibility and model-selection criteria, OFN v0\.12 ", cand, re.M)
    p2b = "**Next required decision:** the criterion home is OFN v0.12, OPEN-OFN-3B" in cand
    kf = re.search(r"^\| κ_f \| GEN \| GEN §6\.8", cand, re.M)
    classc = [l for l in cand.split("\n") if l.startswith("| κ (class-C coupling)")]
    cn05 = "**Consumer notices received.** Triadic CN-05" in cand
    if07 = re.search(r"^\| IF07 \| TRIAD → GEN \|.*\| v1\.7 ", cand, re.M)
    ok = bool(p0 and p2b and kf and len(classc) == 1 and "atlas reading" not in classc[0] and "parameter convention" in classc[0] and cn05 and if07)
    c.add("C15 RECEIVERS", ok, f"P0 {bool(p0)} P2B {p2b} κ_f {bool(kf)} class-C {bool(classc) and 'atlas reading' not in classc[0]} CN-05 {cn05} IF07 {bool(if07)}")
    ids = re.findall(r"^\| (IF\d\d) \|", reg, re.M)
    c.add("C16 IF IDS", ids == [f"IF{i:02d}" for i in range(1, 39)], f"{len(ids)} rows")
    imp, probs = source_types(cand)
    c.add("C17 SOURCE TYPE", not probs, probs or f"OFN imports from {sorted(imp)}; Programme typing agrees")
    return c

FILE_KEY = {"RTG_GENESIS_GEOMETRY_DSN": "GEN", "RTG_DISCRETE_GENESIS_DSN": "TDRG", "RTG_DYADIC_OSCILLATOR_DSN": "DYAD",
            "RTG_RELATIONAL_RECOGNITION_DSN": "RECOG", "RTG_TRIADIC_BIRTH_LIFT_DSN": "TRIAD", "RTG_NUMBER_GENESIS_DSN": "NUMGEN",
            "RTG_OPEN_M_DSN": "UVM"}
NAME_KEY = {"DYAD": "DYAD", "RECOG": "RECOG", "GEN": "GEN", "TDR-G": "TDRG", "TDRG": "TDRG", "TRIAD": "TRIAD",
            "OPEN M": "UVM", "UVM": "UVM", "NUMGEN": "NUMGEN"}
def ofn_import_sources():
    t = at_tag(latest("ofn"), CONSUMERS["OFN"]).decode("utf-8")
    a = t.find("### 11.2"); b = t.find("### 11.3"); c2 = t.find("### 11.4"); d = t.find("### 11.5")
    seg = t[a:b] + t[c2:d]
    keys = set()
    for line in seg.split("\n"):
        if re.match(r"^- \*\*IMP-", line):
            for f, k in FILE_KEY.items():
                if f"`{f}_v" in line: keys.add(k)
    return keys
def names(s): return {NAME_KEY[n] for n in re.findall(r"TDR-G|OPEN M|DYAD|RECOG|GEN|TDRG|TRIAD|UVM|NUMGEN", s)}
def source_types(cand):
    imp = ofn_import_sources(); probs = []
    e = [l for l in cand.split("\n") if l.startswith("**OFN — Ontological Foundations**")]
    m = re.search(r"Imports claim-level statements from ([^(]+)\(", e[0]) if len(e) == 1 else None
    r = re.search(r"records ([^.;]+?) feedback as reference-only", e[0]) if len(e) == 1 else None
    if not (m and r): probs.append("§6.2 OFN entry: import/reference-only sentence missing")
    else:
        if not names(m.group(1)) <= imp: probs.append(f"§6.2 OFN: imports {sorted(names(m.group(1)) - imp)} not in OFN §11.2/11.4")
        if names(r.group(1)) & imp: probs.append(f"§6.2 OFN: reference-only {sorted(names(r.group(1)) & imp)} are imports")
    g = [l for l in cand.split("\n") if l.startswith("  OFN <-- ")]
    for l in g:
        if not names(l.split("(")[0]) <= imp: probs.append(f"§7.1: {sorted(names(l.split('(')[0]) - imp)} drawn as imports into OFN")
    reg = section(cand, "### 7.2", "### 7.3")
    for line in reg.split("\n"):
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if not line.startswith("| IF") or len(cells) != 6 or not cells[1].endswith("→ OFN"): continue
        src, typ = names(cells[1].split("→")[0]), cells[2]
        if "reference-only (" in typ or "declared-import (" in typ:
            dec = names(re.search(r"declared-import \(([^)]*)\)", typ).group(1)) if "declared-import (" in typ else set()
            ref = names(re.search(r"reference-only \(([^)]*)\)", typ).group(1)) if "reference-only (" in typ else set()
        elif "import" in typ: dec, ref = src, set()
        else: dec, ref = set(), src
        if not dec <= imp: probs.append(f"{cells[0]}: {sorted(dec - imp)} typed as imports into OFN")
        if ref & imp: probs.append(f"{cells[0]}: {sorted(ref & imp)} typed reference-only but imported by OFN")
        if dec | ref != src: probs.append(f"{cells[0]}: type split does not cover {sorted(src - dec - ref)}")
    return imp, probs

def addlog(L, old, new):
    L2 = json.loads(json.dumps(L)); L2["edits"].append(dict(key="X", old=old, new=new)); return L2
def mut(old, new, logged=True):
    def f(i, L):
        assert i.count(old) == 1, f"control precondition: {old[:40]!r} occurs {i.count(old)}x"
        return i.replace(old, new), (addlog(L, old, new) if logged else L)
    return f

CONTROLS = [
 ("K1 undeclared edit", mut("| IF27 | NUMGEN ← RECOG |", "| IF27 | NUMGEN <- RECOG |", logged=False), "C1 BUILD"),
 ("K2 OPEN status changed (logged)", mut("**RID:** `RTG-OPEN-REGGE-BRIDGE`  \n**Status:** ACTIVE", "**RID:** `RTG-OPEN-REGGE-BRIDGE`  \n**Status:** CLOSED"), "C3 OPEN RIDS"),
 ("K3 guard text edited (logged)", mut("No physical dynamical law, coefficient,", "No physical law, coefficient,"), "C4 GUARDS"),
 ("K4 anchor removed (logged)", mut('<a id="prog-guards"></a>\n', ""), "C5 ANCHORS"),
 ("K5 THM tag introduced (logged)", mut("`[DEF]` Tier numbers", "`[THM]` Tier numbers"), "C6 TAGS"),
 ("K6 inventory edition wrong (logged)", mut("| v6.4.23 | `dyad-v6.4.23` |", "| v6.4.22 | `dyad-v6.4.23` |"), "C7 INVENTORY"),
 ("K7 inventory at superseded tag (logged)", mut("| v1.21 | `numgen-v1.21` |", "| v1.20.8 | `numgen-v1.20.8` |"), "C7 INVENTORY"),
 ("K8 invented consumer pin (logged)", mut("| NUMGEN §9.1 | v2.9 |", "| NUMGEN §9.1 | v2.9.9 |"), "C8 IF PINS"),
 ("K9 pin read from the wrong consumer (logged)", mut("| GEN §7 | v1.21 |", "| UVM §7 | v1.21 |"), "C8 IF PINS"),
 ("K10 science restated in §6 (logged)", mut("Owns the selected primitive map,", "Owns the selected primitive map, c'_Q=0.36916 ⇒"), "C10 NO SCIENCE"),
 ("K11 versioned filename in live text (logged)", mut("(v0.8, `dzt-v0.8`)", "(`RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0_8.md`)"), "C11 FILENAMES"),
 ("K12 stale methodology pointer (logged)", mut("The namespace registry is **Methodology v1.4 §4.2**", "The namespace registry is **Methodology v1.3 §4.2**"), "C12 METHODOLOGY"),
 ("K13 Appendix B edited (logged)", mut("These administrative keys are not fabricated", "These administrative keys are not invented"), "C13 APPENDIX B"),
 ("K14 stale tag in a §6 entry (logged)", mut("**RECOG — Relational Recognition** (v0.3.27, `recog-v0.3.27`)", "**RECOG — Relational Recognition** (v0.3.26, `recog-v0.3.26`)"), "C14 STALE"),
 ("K15 E-P13-1 wording restored (logged)", mut("OFN §11.4 and RRF §6.2a record γ ≡ κ as the class-C parameter convention (Genesis writes γ)", "its relation to Genesis's γ is an atlas reading, not an owner statement"), "C15 RECEIVERS"),
 ("K16 CN-05 receipt dropped (logged)", mut("**Consumer notices received.** Triadic CN-05", "Triadic CN-05"), "C15 RECEIVERS"),
 ("K17 IF row duplicated (logged)", mut("| IF38 | NUMGEN → GEN |", "| IF37 | NUMGEN → GEN |"), "C16 IF IDS"),
 ("K19 IF24 typed as import again (logged)", mut("| IF24 | NUMGEN → OFN | reference-only feedback |", "| IF24 | NUMGEN → OFN | feedback (recorded import) |"), "C17 SOURCE TYPE"),
 ("K20 TRIAD drawn as import into OFN (logged)", mut("  OFN <-- DYAD, RECOG, GEN  ", "  OFN <-- DYAD, RECOG, GEN, TRIAD"), "C17 SOURCE TYPE"),
 ("K21 OFN entry lists NUMGEN as import (logged)", mut("Imports claim-level statements from DYAD, RECOG, GEN and TDR-G (", "Imports claim-level statements from DYAD, RECOG, GEN, NUMGEN and TDR-G ("), "C17 SOURCE TYPE"),
 ("K22 IF32 split drops TDRG (logged)", mut("declared-import (DYAD, GEN, TDRG); reference-only (TRIAD, UVM)", "declared-import (DYAD, GEN); reference-only (TRIAD, UVM)"), "C17 SOURCE TYPE"),
 ("K18 heading renamed (logged)", mut("### 8.2 Cross-stream symbol table — κ\n", "### 8.2 Symbol table\n"), "C9 SECTIONS"),
]

def main():
    base = open(sys.argv[1], encoding="utf-8").read()
    cand = open(sys.argv[2], encoding="utf-8").read()
    log = json.load(open(sys.argv[3], encoding="utf-8"))
    c = run(base, cand, log)
    print("RESULT:", "FAIL" if c.failed else "PASS")
    rc = 1 if c.failed else 0
    if "--controls" in sys.argv:
        print("\n== negative controls ==")
        caught = 0
        for name, f, gate in CONTROLS:
            i2, L2 = f(cand, log); L2 = dict(L2); L2["candidate_sha256"] = sha(i2)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf): cc = run(base, i2, L2)
            failed = {g for g, ok, _ in cc.rows if not ok}
            ok = gate in failed; caught += ok
            print(f"{'ok  ' if ok else 'MISS'} {name:46s} expect FAIL at {gate}; failed: {sorted(failed)}")
        print(f"CONTROLS: {caught}/{len(CONTROLS)} caught")
        rc |= 0 if caught == len(CONTROLS) else 2
    sys.exit(rc)

if __name__ == "__main__":
    main()
