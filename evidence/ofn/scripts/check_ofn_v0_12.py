#!/usr/bin/env python3
r"""OFN v0.12 — checker (gates + negative controls).

usage: check_ofn_v0_12.py BASE CANDIDATE EDITLOG_JSON [--controls]
  BASE = `git show ofn-v0.11:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`; run from the repository root (owner tags read with git show).
Gates:
  K1 base identity; K2 deterministic rebuild and edit-log hash chain;
  K3 every v0.11 RTG-OFN RID and anchor kept; K4 the 21 OPEN status lines unchanged in order;
  K5 the only new OFN RID is RTG-OFN-ALG-REF-CLOSURE-COMPARISON, declared once, with a single conclusion status [from: ALG];
  K6 every DYAD/GEN/TDRG/RECOG/NUMGEN RID cited resolves at the governing tag;
  K7 stale v0.11 edition phrases and the superseded REF-CLOSURE question absent from the live text;
  K8 required statements present (result parts, frames, "none selected" / "no standard selected" boundaries);
  K9 Appendix A, Appendix B and the Appendix C entries for v0.11 and earlier byte-identical;
  K10 every `[DEF]` line, the Q1-Q6 contract rows and the Standard C declaration of v0.11 unchanged;
  K11 no selection language: no isolation contract, independence standard or physical reading is declared selected.
--controls applies negative-control mutations to the candidate; each must fail at least one gate. A passing run authorizes nothing.
"""
import hashlib, importlib.util, json, os, re, subprocess, sys

BASE_SHA = "38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4"
NEW_RID = "RTG-OFN-ALG-REF-CLOSURE-COMPARISON"
TAGS = {"DYAD": ("dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md"), "GEN": ("gen-v2.9", "dsn/RTG_GENESIS_GEOMETRY_DSN.md"),
        "TDRG": ("tdrg-v2.12.14", "dsn/RTG_DISCRETE_GENESIS_DSN.md"), "RECOG": ("recog-v0.3.26", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md"),
        "NUMGEN": ("numgen-v1.21", "dsn/RTG_NUMBER_GENESIS_DSN.md")}
STALE = ["**v0.11 revision boundary:**", "*v0.11:* registers", "four OFN local results",
         "Question: Are edge-closure reduction and removal of one relational reference the same construction?",
         "Next required artifact or decision: An explicit comparison construction.",
         "The equality of those constructions is not assumed;"]
REQUIRED = [
    "`[RESULT]` `[from: ALG]` [RID: RTG-OFN-ALG-REF-CLOSURE-COMPARISON]",
    "(i) $d$ induces an isomorphism $Q_{\\rm node}\\cong C_0$",
    "has $\\ker\\kappa_n\\cong H[n]$ and $\\operatorname{coker}\\kappa_n\\cong H/nH$",
    "Edge-dependent isomorphisms $C_0\\cong Q_{\\rm edge}$ exist for every abelian $H$ and are a different comparison.",
    "Equal cardinalities of $Q_{\\rm node}$, $C_0$ and $Q_{\\rm edge}$ do not decide (iii).",
    "any physical reading of reference consumption, which stays with the `[HYP]` above and OPEN-OFN-REF-CLOSURE.",
    "exactly $F_e-N(z_e)=-\\tfrac{\\kappa}{3}\\bigl(N(z_e)+b_e\\bigr)$",
    "its closure is not imported.",
    "Isolation frame (recorded; none selected).",
    "Evaluation frame (recorded; no standard selected).",
    "Which combination of axes the phrase \"independently motivated model class\" of §8 requires is not selected",
    "No primacy conclusion follows.",
    "Question: Which reference operation, if any, is the physical (rotational) reference consumption of the §2.4 `[HYP]`?",
    "| `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` | v0.12 (adoption pending), OFN RESULT from ALG |",
    "the hypothesis FSP-U, five OFN local results and twenty-one foundational OPENs",
]
SELECTED = [r"\bI-comp is (?:selected|adopted|the physical)", r"\bI-quiet is (?:selected|adopted|required)", r"\bI-remove is (?:selected|adopted)",
            r"standard \((?:a|b|c)\) is (?:selected|adopted)", r"physical reading is (?:selected|adopted|established)",
            r"isolation contract is (?:selected|adopted)"]


def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()
def show(tag, path): return subprocess.run(["git", "show", f"{tag}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")
def live(t): return t[:t.index('<a id="ofn-historical-scenarios">')]
def ofn_rids(t): return set(re.findall(r"RTG-OFN-[A-Z0-9]+(?:-[A-Z0-9]+)*", t))
def anchors(t): return set(re.findall(r'<a id="([^"]+)"', t)) | set(re.findall(r"\{#([A-Za-z0-9_-]+)\}", t))
def statuses(t): return re.findall(r"^Status: (ACTIVE|PARTIAL)\b.*$", t, re.M)
def apps(t):
    a = t.index('<a id="ofn-historical-scenarios">'); c = t.index("### v0.11 — 30 October 2026")
    b = t.index('<a id="ofn-version-history">'); d = t.index("*END OF DOCUMENT")
    return t[a:b] + t[c:d]
def protected(t):
    L = t.split("\n")
    return [l for l in L if l.startswith("`[DEF]`") or l.startswith("| **Q") or "[RID: RTG-OFN-DEF-STANDARD-C]" in l]


def gates(base, cand, log, builder_out=None, out=print):
    res = []
    def g(k, ok, msg=""): res.append(bool(ok)); out(f"{k} {'PASS' if ok else 'FAIL'} {msg}".rstrip())
    g("K1", sha(base) == BASE_SHA, "base is ofn-v0.11")
    if builder_out is not None:
        ch = log["edits"]
        okc = ch[0]["doc_sha256_before"] == BASE_SHA and all(ch[i]["doc_sha256_after"] == ch[i + 1]["doc_sha256_before"] for i in range(len(ch) - 1)) \
            and ch[-1]["doc_sha256_after"] == sha(cand) and log["candidate_sha256"] == sha(cand)
        g("K2", builder_out == cand and okc, f"rebuild identical; {len(ch)} logged edits; chain intact")
    rb, rc = ofn_rids(base), ofn_rids(cand)
    g("K3", rb <= rc and anchors(base) <= anchors(cand), f"v0.11 RIDs {len(rb)} and anchors {len(anchors(base))} kept")
    g("K4", statuses(base) == statuses(cand) and len(statuses(cand)) == 21,
      f"OPEN status lines {len(statuses(cand))}: {statuses(cand).count('ACTIVE')} ACTIVE / {statuses(cand).count('PARTIAL')} PARTIAL")
    decl = [l for l in cand.split("\n") if f"[RID: {NEW_RID}]" in l]
    g("K5", rc - rb == {NEW_RID} and len(decl) == 1 and decl[0].startswith("`[RESULT]` `[from: ALG]` [RID:"),
      f"new OFN RIDs: {sorted(rc - rb)}")
    bad = []
    for key, (tag, path) in TAGS.items():
        src = show(tag, path)
        cited = set(m.group(0) for m in re.finditer(rf"\b{key}-(?:THM|ALG|DEF|CAND|RESULT|NUM|OPEN)-[A-Z0-9]+(?:-[A-Z0-9]+)*", cand)
                    if cand[m.end():m.end() + 2] != "-*")
        for r in cited:
            if not (f"RID: {r}]" in src or f"**RID:** `{r}`" in src):
                if r.startswith(f"{key}-OPEN-"): continue
                bad.append(f"{r}@{tag}")
    g("K6", not bad, f"owner RIDs resolve at governing tags; unresolved: {bad}")
    L = live(cand)
    hits = [p for p in STALE if p in L]
    g("K7", not hits, f"stale phrases in live text: {hits}")
    miss = [p for p in REQUIRED if p not in cand]
    g("K8", not miss, f"required statements missing: {[m[:60] for m in miss]}")
    try: same = apps(base) == apps(cand)
    except ValueError: same = False
    g("K9", same, "Appendix A, Appendix B and Appendix C entries for v0.11 and earlier byte-identical")
    pb, pc = protected(base), protected(cand)
    g("K10", pb == pc, f"{len(pb)} [DEF] lines, Q1–Q6 rows and the Standard C declaration unchanged")
    sel = [p for p in SELECTED if re.search(p, L)]
    g("K11", not sel, f"selection language: {sel}")
    return all(res)


CONTROLS = [
    ("C1 stale v0.11 boundary", lambda t: t.replace("**v0.12 revision boundary:**", "**v0.11 revision boundary:**", 1)),
    ("C2 old REF-CLOSURE question restored", lambda t: t.replace("Question: Which reference operation, if any, is the physical (rotational) reference consumption of the §2.4 `[HYP]`?", "Question: Are edge-closure reduction and removal of one relational reference the same construction?", 1)),
    ("C3 isolation contract selected", lambda t: t.replace("Isolation frame (recorded; none selected).", "Isolation frame. I-comp is selected as the physical-isolation criterion.", 1)),
    ("C4 independence standard selected", lambda t: t.replace("Evaluation frame (recorded; no standard selected).", "Evaluation frame. Standard (b) is adopted.", 1)),
    ("C5 OPEN status changed", lambda t: t.replace("Status: ACTIVE | Layer: O1  \nQuestion: Which reference operation", "Status: PARTIAL | Layer: O1  \nQuestion: Which reference operation", 1)),
    ("C6 v0.11 RID dropped", lambda t: t.replace("[RID: RTG-OFN-OPEN-SECTOR]", "[RID: (removed)]", 1)),
    ("C7 extra OFN RID", lambda t: t.replace("[RID: RTG-OFN-ALG-REF-CLOSURE-COMPARISON]", "[RID: RTG-OFN-ALG-REF-CLOSURE-COMPARISON] [RID: RTG-OFN-ALG-ISOLATION-INTERFACE]", 1)),
    ("C8 compound status on the new result", lambda t: t.replace("`[RESULT]` `[from: ALG]` [RID: RTG-OFN-ALG-REF-CLOSURE-COMPARISON]", "`[RESULT]` `[from: THM + ALG]` [RID: RTG-OFN-ALG-REF-CLOSURE-COMPARISON]", 1)),
    ("C9 definition line edited", lambda t: t.replace("`[DEF]` [RID: RTG-OFN-DEF-FEEDBACK] **Feedback rule.**", "`[DEF]` [RID: RTG-OFN-DEF-FEEDBACK] **Feedback rule (revised).**", 1)),
    ("C10 Appendix B edited", lambda t: t.replace("**OFN11-C03 — status and notation.**", "**OFN11-C03 — status / notation.**", 1)),
    ("C11 unresolved owner RID", lambda t: t.replace("`DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (v6.4.20)", "`DYAD-THM-SMOOTH-EQUIVARIANT-CHART-X` (v6.4.20)", 1)),
    ("C12 stale local-result count", lambda t: t.replace("five OFN local results and twenty-one", "four OFN local results and twenty-one", 1)),
    ("C13 edge-dependent isomorphism caveat dropped", lambda t: t.replace(" Edge-dependent isomorphisms $C_0\\cong Q_{\\rm edge}$ exist for every abelian $H$ and are a different comparison.", "", 1)),
    ("C14 N-1A2 closure imported", lambda t: t.replace("its closure is not imported.", "its closure is imported.", 1)),
]


def main(argv):
    if len(argv) < 4: raise SystemExit(__doc__)
    base = open(argv[1], encoding="utf-8").read(); cand = open(argv[2], encoding="utf-8").read()
    log = json.load(open(argv[3], encoding="utf-8"))
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("b12", os.path.join(here, "build_ofn_v0_12.py"))
    b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
    rebuilt, _ = b.apply(base)
    ok = gates(base, cand, log, builder_out=rebuilt)
    print("GATES", "PASS" if ok else "FAIL")
    if "--controls" in argv:
        allc = True
        for name, f in CONTROLS:
            m = f(cand)
            if m == cand: print(f"{name}: mutation did not apply — CONTROL INVALID"); allc = False; continue
            r = gates(base, m, log, builder_out=None, out=lambda s: None)
            print(f"{name}: {'caught' if not r else 'NOT CAUGHT'}"); allc &= not r
        print("CONTROLS", "PASS" if allc else "FAIL"); ok &= allc
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main(sys.argv)
