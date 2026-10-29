#!/usr/bin/env python3
r"""OFN v0.11 — stage-1 checker (gates + negative controls).

usage: check_ofn_v0_11_stage1.py BASE CANDIDATE EDITLOG_JSON [--controls]
  BASE = `git show ofn-v0.10:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`; run from the repository root (owner tags are read
  with `git show`). Gates:
  K1 base identity; K2 deterministic rebuild (builder output == candidate) and edit-log hash chain;
  K3 every v0.10 OFN RID and anchor kept; K4 the 21 OPEN status lines unchanged in order;
  K5 new OFN RIDs are exactly the six registered DEF RIDs, each declared once;
  K6 every owner RID the candidate cites for DYAD/GEN/TDRG/RECOG/NUMGEN is declared at the governing tag;
  K7 stale phrases absent from the live text (before Appendix A); K8 required statements present (round 2 adds the
  R112-C1/C2/N1 phrases to K7 and K8, with controls C15-C17);
  K9 Appendix A, Appendix B (B.1, B.2, v0.9 and v0.10 records) and the inherited Appendix C entries unchanged.
--controls applies negative-control mutations to the candidate; each must fail at least one gate.
A passing run authorizes nothing.
"""
import hashlib, json, re, subprocess, sys, os, importlib.util

BASE_SHA = "acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa"
TAGS = {"DYAD": ("dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md"), "GEN": ("gen-v2.9", "dsn/RTG_GENESIS_GEOMETRY_DSN.md"),
        "TDRG": ("tdrg-v2.12.14", "dsn/RTG_DISCRETE_GENESIS_DSN.md"), "RECOG": ("recog-v0.3.26", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md"),
        "NUMGEN": ("numgen-v1.21", "dsn/RTG_NUMBER_GENESIS_DSN.md")}
NEW_RIDS = {"RTG-OFN-DEF-ZERO-ORIGIN", "RTG-OFN-DEF-DISCRETE-REDUCTION-BOUNDARY", "RTG-OFN-DEF-CONTINUOUS-REPRESENTATION",
            "RTG-OFN-DEF-FINITE-DESCRIPTION", "RTG-OFN-DEF-DIST-ZN", "RTG-OFN-DEF-REDUCTION-TARGET"}
STALE = ["conditional on DYAD OPEN 20", "existence is not asserted", "real only once $J$", "conditional on the real surfaces",
         "freeze-candidate", "live header says freeze candidate", "nonempty $F$-invariant", "[ALG —", "[from: THM + ALG]",
         "request IMP-O08", "XFER-O08-01 remains proposed", "transfer proposed]", "B-an, B-6 and B-∞ existence open",
         "analytic realization exists", "XFER-O08-01 is accepted", "custody transfer accepted", "Loopholes: non-manifold", "Real-analytic laws form the admitted continuous FMS test class",
         "separate map-definition custody remains unresolved", "Single input for §5.5", "Governing input: `OFN_REPLY_TO_FMS_MODEL_SELECTION",
         "interaction vanishes algebraically satisfies the mathematical contract"]
REQUIRED = [
    "Standard C at cubic order requires a positive-dimensional embedded $C^3$ manifold germ $M$ through the null state",
    "A singleton, a finite null-state record, or an isolated trajectory is not this local smooth isolation regime.",
    "consists of real $C^\\infty$ update germs. Real-analytic laws form a distinguished subclass.",
    "[RID: DYAD-THM-SMOOTH-EMBEDDING]" if False else "`DYAD-THM-SMOOTH-EMBEDDING` (v6.4.18). Source status: `THM`",
    "`DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (v6.4.20). Source status: `THM`",
    "inherits none of the §6.14 finite-chart bounds (SG-19)",
    "**Exactly transported analytic realization** — OPEN (DYAD OPEN 20, B-an/B-6).",
    "**Primary realized smooth mathematical candidate family; analytic exact realization and physical selection open.**",
    "(H-JET) third jet equal to the mean-feedback form over $N_3(z)=\\lambda z+nz^2\\bar z$; (H-μ) $\\mu=6\\bar\\lambda n\\ne0$; κ ∈ ℝ∖{0,2}; (H_spec)",
    "`[RESULT]` `[from: ALG]` [RID: RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT]",
    "custody transfer XFER-O08-01 is deferred by TDR-G to v2.13",
    "**OFN11-C01 — `RTG-OFN-DEF-STANDARD-C` quantifier `[COR]`.**", "**OFN11-C02 — test-class regularity amendment.**",
    "| **REQ-O09-02 — FULFILLED** |", "| **REQ-O09-03 — FULFILLED** |", "| **REQ-O09-04 — FULFILLED** |",
    "The single κ table of §5.5", "Status: PARTIAL | Layer: O1/O4→geometry",
    "Primitive-map custody is resolved separately: `DYAD-DEF-PRIMITIVE-MAP` (Dyadic custody)",
    "Historical integration input for v0.10: `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md`",
    "Historical single integration input for v0.10 §5.5",
    "Algebraic cancellation alone establishes neither those regime requirements nor physical removal of the surroundings.",
]

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()
def show(tag, path): return subprocess.run(["git", "show", f"{tag}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")
def live(t): return t[:t.index('<a id="ofn-historical-scenarios">')]
def ofn_rids(t): return set(re.findall(r"RTG-OFN-[A-Z0-9]+(?:-[A-Z0-9]+)*", t))
def anchors(t): return set(re.findall(r'<a id="([^"]+)"', t))
def statuses(t): return re.findall(r"^Status: (ACTIVE|PARTIAL)\b.*$", t, re.M)
def hist(t):
    a = t.index('<a id="ofn-historical-scenarios">'); b = t.index("### Adopted v0.10 records — 19 October 2026")
    b2 = t.index("<a id=\"ofn-version-history\">")
    c = t.index("### v0.10 — 19 October 2026 — ADOPTED / FMS model-selection interface release")
    d = t.index("*END OF DOCUMENT")
    blkB = t[b:b2]; blkB = blkB[:blkB.index("### Adopted v0.11 records") if "### Adopted v0.11 records" in blkB else len(blkB)]
    return t[a:b] + blkB.rstrip().removesuffix("---").rstrip() + "\n" + t[c:d]

def gates(base, cand, log, builder_out=None, out=print):
    res = []
    def g(k, ok, msg=""): res.append(ok); out(f"{k} {'PASS' if ok else 'FAIL'} {msg}")
    g("K1", sha(base) == BASE_SHA, "base is ofn-v0.10")
    if builder_out is not None:
        chain = log["edits"]; okc = chain[0]["doc_sha256_before"] == BASE_SHA and all(chain[i]["doc_sha256_after"] == chain[i+1]["doc_sha256_before"] for i in range(len(chain)-1)) and chain[-1]["doc_sha256_after"] == sha(cand)
        g("K2", builder_out == cand and okc and log["candidate_sha256"] == sha(cand), f"rebuild identical; {len(chain)} logged edits; chain intact")
    rb, rc = ofn_rids(base), ofn_rids(cand)
    g("K3", rb <= rc and anchors(base) <= anchors(cand), f"v0.10 RIDs {len(rb)} and anchors {len(anchors(base))} kept")
    g("K4", statuses(base) == statuses(cand) and len(statuses(cand)) == 21, f"OPEN status lines {len(statuses(cand))}: {statuses(cand).count('ACTIVE')} ACTIVE / {statuses(cand).count('PARTIAL')} PARTIAL")
    new = rc - rb; decl = {r: cand.count(f"[RID: {r}]") for r in NEW_RIDS}
    g("K5", new == NEW_RIDS and all(v == 1 for v in decl.values()), f"new OFN RIDs: {sorted(new)}")
    bad = []
    for key, (tag, path) in TAGS.items():
        src = show(tag, path)
        cited = set(m.group(0) for m in re.finditer(rf"\b{key}-(?:THM|ALG|DEF|CAND|RESULT|NUM|OPEN)-[A-Z0-9]+(?:-[A-Z0-9]+)*", cand) if cand[m.end():m.end()+2] != "-*")
        for r in cited:
            if not (f"[RID: {r}]" in src or f"`[RID: {r}]`" in src or f"RID: {r}]" in src or f"**RID:** `{r}`" in src):
                if key == "TDRG" and r.startswith("TDRG-OPEN-"): continue   # TDR-G OPEN module labels are cited as names
                if key == "RECOG" and r.startswith("RECOG-OPEN-"): continue
                if key == "GEN" and r.startswith("GEN-OPEN-"): continue
                if key == "NUMGEN" and r.startswith("NUMGEN-OPEN-"): continue
                bad.append(f"{r}@{tag}")
    g("K6", not bad, f"owner RIDs resolve at governing tags; unresolved: {bad}")
    L = live(cand); hits = [p for p in STALE if p in L]
    g("K7", not hits, f"stale phrases in live text: {hits}")
    miss = [p for p in REQUIRED if p not in cand]
    g("K8", not miss, f"required statements missing: {[m[:60] for m in miss]}")
    try: same = hist(base) == hist(cand)
    except ValueError as e: same = False
    g("K9", same, "Appendix A, Appendix B (to v0.10 records) and inherited Appendix C entries byte-identical")
    return all(res)

CONTROLS = [
    ("C1 stale OPEN-20 conditional", lambda t: t.replace("| Clock | Primitive $T$; $T^6$ derived sampling. |", "| Clock | Primitive $T$; realization conditional on DYAD OPEN 20. |", 1)),
    ("C2 freeze candidate reintroduced", lambda t: t.replace("no certificate rerun. The v0.3.20 edition's", "no certificate rerun. The live source declares freeze-candidate status. The v0.3.20 edition's", 1)),
    ("C3 Standard C singleton wording", lambda t: t.replace("Standard C at cubic order requires a positive-dimensional embedded $C^3$ manifold germ $M$ through the null state", "Standard C holds if there is a nonempty $F$-invariant regime $\\mathcal R$", 1)),
    ("C4 false custody transfer", lambda t: t.replace("custody transfer XFER-O08-01 is deferred by TDR-G to v2.13", "custody transfer XFER-O08-01 is accepted by TDR-G", 1)),
    ("C5 smooth-to-analytic promotion", lambda t: t.replace("**Exactly transported analytic realization** — OPEN (DYAD OPEN 20, B-an/B-6).", "**Exactly transported analytic realization** — analytic realization exists.", 1)),
    ("C6 missing H_spec", lambda t: t.replace("κ ∈ ℝ∖{0,2}; (H_spec); factor dimension", "κ ∈ ℝ∖{0,2}; factor dimension", 1)),
    ("C7 finite-chart bounds transported", lambda t: t.replace("inherits none of the §6.14 finite-chart bounds (SG-19)", "inherits the §6.14 finite-chart bounds", )),
    ("C8 narrow-Q6 compound status", lambda t: t.replace("`[RESULT]` `[from: ALG]` [RID: RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT]", "`[RESULT]` `[from: THM + ALG]` [RID: RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT]", 1)),
    ("C9 OPEN status changed", lambda t: t.replace("Status: PARTIAL | Layer: O1/O4→geometry", "Status: ACTIVE | Layer: O1/O4→geometry", 1)),
    ("C10 v0.10 RID dropped", lambda t: t.replace("[RID: RTG-OFN-OPEN-SECTOR]", "[RID: (removed)]", 1)),
    ("C11 extra OFN RID", lambda t: t.replace("`[DEF]` [RID: RTG-OFN-DEF-ZERO-ORIGIN]", "`[DEF]` [RID: RTG-OFN-DEF-ZERO-ORIGIN] [RID: RTG-OFN-DEF-INVENTED]", 1)),
    ("C12 unresolved owner RID", lambda t: t.replace("`DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (v6.4.20)", "`DYAD-THM-SMOOTH-EQUIVARIANT-CHART-X` (v6.4.20)", 1)),
    ("C13 history edited", lambda t: t.replace("**OFN08-C02 — scope/typing", "**OFN08-C02 — scope / typing", 1)),
    ("C15 stale map-custody sentence (R112-C1)", lambda t: t.replace("Dedicated result ID located. Primitive-map custody is resolved separately:", "Dedicated result ID located; separate map-definition custody remains unresolved. Primitive-map custody:", 1)),
    ("C16 handoff as sole current input (R112-C2)", lambda t: t.replace("| Historical single integration input for v0.10 §5.5;", "| Single input for §5.5;", 1)),
    ("C17 unqualified algebraic sufficiency (R112-N1)", lambda t: t.replace("on a regime that meets the manifold, nontriviality, domain and clock requirements above, $I_e\\equiv0$ for every edge satisfies the order-four bound. Algebraic cancellation alone establishes neither those regime requirements nor physical removal of the surroundings.", "an invariant regime on which the interaction vanishes algebraically satisfies the mathematical contract.", 1)),
    ("C14 compound tag", lambda t: t.replace("- `[ALG]` [scope: leading order] [provenance: SESSION]", "- `[ALG — leading order; SESSION]`", 1)),
]

def main(argv):
    if len(argv) < 4: raise SystemExit(__doc__)
    base = open(argv[1], encoding="utf-8").read(); cand = open(argv[2], encoding="utf-8").read(); log = json.load(open(argv[3], encoding="utf-8"))
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("b1", os.path.join(here, "build_ofn_v0_11_stage1.py")); b1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b1)
    rebuilt, _ = b1.apply(base)
    ok = gates(base, cand, log, builder_out=rebuilt)
    print("GATES", "PASS" if ok else "FAIL")
    if "--controls" in argv:
        allc = True
        for name, f in CONTROLS:
            m = f(cand)
            if m == cand: print(f"{name}: mutation did not apply — CONTROL INVALID"); allc = False; continue
            r = gates(base, m, log, builder_out=None, out=lambda s: None)
            print(f"{name}: {'caught' if not r else 'NOT CAUGHT'}"); allc &= (not r)
        print("CONTROLS", "PASS" if allc else "FAIL"); ok &= allc
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main(sys.argv)
