#!/usr/bin/env python3
"""Checker for Genesis v2.9 stage 1 (corrected intermediate; not an edition). Round 2 (25 Oct 2026): B1–B3 of the
atlas row check; C3 covers the Appendix B insertion; C15 added; controls NC10–NC11 added.

usage: check_gen_v2_9_stage1.py BASE INTERMEDIATE EDITLOG_JSON [--root REPO] [--controls]
  BASE = `git show gen-v2.8.9:dsn/RTG_GENESIS_GEOMETRY_DSN.md`; INTERMEDIATE = dsn/RTG_GENESIS_GEOMETRY_DSN.md on the
  stage-1 branch; EDITLOG_JSON = evidence/gen/v2.9/stage1_edit_log.json. --root defaults to the current directory
  (must be the repository; C12/C14 read files and tags from it). --controls runs the negative controls instead.

Gates (exit 0 iff all PASS):
 C0  BASE         base bytes are adopted v2.8.9 (d143673e...c6fc)
 C1  BUILD        the builder reproduces the intermediate byte-exactly and the log hash matches
 C2  REVERSE      undoing the logged edits in reverse order recovers the base byte-exactly
 C3  APPENDIX     Appendix A/B and footer region = base with only the declared Appendix A and Appendix B entries inserted
 C4  PROTECTED    §6.3a–§6.3c identical to base except the one declared G-20 note line; §8 rows of the protected RIDs identical
 C5  RID SET      GEN RID set = base set + the three declared RIDs, each attached once at its [THM] statement;
                  the new RIDs occur in no other dsn/ file
 C6  KAPPA        no bare face-lift κ remains in §6.8–§6.9 except the declared definition line; the bare-κ lines outside
                  the face-lift list are the base ones (triadic birth κ untouched), plus the definition line if it names κ
 C7  TAGS         per-tag census: base + Σ(new−old over edits) = intermediate, and no edit removes a claim tag
 C8  SIGN         9A eigenvalues/inverse/projectors are sgn(m)-explicit; no signed κ (κ=m|w|) and no Π = ΔM_f/κ form remains
 C9  GA-01        "has a valid minimizer" absent from live text (it is recorded in Appendix B); both statements carry Δ₃>0; §7 export carries the scope
 C10 HEADER       header lines other than the tier line and the Status-summary label (E29, '.' -> ':'), and the footer, are unchanged
 C11 HEADINGS     base headings all survive; new headings are exactly the declared ones
 C12 EVIDENCE     every evidence/ path cited in the live text exists; the advisory-check script hash matches
 C13 GB13         the GSPLIT/DELTA-QC identity re-verified here (independent code path)
 C14 SOURCES      cited source facts are present at their tags (dyad-v6.4.22, triad-v1.6.1, programme-v1.3), incl. the
                  Triadic `[conv: RTG canonical B-metric]` normalization cited at the GB-13 line (B3)
 C15 LIVE         B1/B2: no dated "v2.9" marker in the live text; the standard clauses [custody-A] and [indep-AC] are
                  defined exactly once (head of §8) and cited by key; the nine GEN-ART custody rows cite [custody-A];
                  the withdrawn clause appears only in Appendix B
"""
import hashlib, importlib.util, json, os, re, subprocess, sys

BASE_SHA = "d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc"
APPA = "## Appendix A — Version History {#appendix-a}\n\n"
NEW_RIDS = {"GEN-THM-QH-NOGO", "GEN-THM-SINGLE-FACE-METRIC", "GEN-THM-SOURCED-JUNCTION"}
PROTECTED_RIDS = ["GEN-THM-K3-PLANAR-FACTOR-NOGO", "GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA", "GEN-THM-K3-SIXSTEP-FACTOR-NOGO",
                  "GEN-DEF-MEANFEEDBACK-FAMILY", "GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO", "GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO"]
G20_NOTE_PREFIX = "- **G-20, existence note (GC-17).**"
KF_DEF_PREFIX = "`[DEF]` **Face-lift magnitude, sign and $B_*$.**"
NEW_HEADINGS = {"### From `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22`", "### Consumers (Programme v1.3 §7.2)", "### Pins",
                "### v2.9 — stage 1 intermediate (build stage, not adopted)",
                "### Corrected claims (stage-1 corrections of the v2.8.9 advisory)"}
APPB = "## Appendix B — Retired and Rejected Claims {#appendix-b}\n\n"
TAGS = ["[THM]", "[ALG]", "[OPEN]", "[DEF]", "[RESULT]", "[COR]", "[HYP]", "[FAIL]", "[CAND]", "[RETRACTED]",
        "[ALG structure]", "[ALG diagnostic]", "[CONVENTION]"]
BARE_K = re.compile(r"\\kappa(?![A-Za-z_])")
EVID = ("evidence/gen/scripts/gen_owner_advisory_checks.py", "0ba256be3999606e936a0b14f92311600fd5bd3ff041dd3a828d7688dab6bf99")

def sha(s): return hashlib.sha256(s.encode() if isinstance(s, str) else s).hexdigest()
def live(s): return s[:s.index(APPA)]
def span(s, a, b):
    i = s.index(a); return s[i:s.index(b, i)]
def heads(s): return [l for l in s.split("\n") if l.startswith("#")]

def load_builder(root):
    p = os.path.join(root, "evidence/gen/scripts/build_gen_v2_9_stage1.py")
    spec = importlib.util.spec_from_file_location("b", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def git_show(root, ref):
    return subprocess.run(["git", "-C", root, "show", ref], capture_output=True, text=True).stdout

def reverse_full(inter, log):
    """Undo the logged edits in reverse order: substitutions first, then the one pure deletion (E19a, re-inserted
    before its recorded right neighbour), then the KF lines by base line number. The final byte comparison with
    the base is the test; a step that cannot be located returns None."""
    t = inter
    for e in reversed(log["edits"]):
        if e["mode"] == "kf-line" or e["new"] == "":
            continue
        if e["mode"] == "line" and "\n" not in e["new"]:
            ls = t.split("\n"); idx = [i for i, l in enumerate(ls) if l == e["new"]]
            if len(idx) != 1:
                return None
            ls[idx[0]] = e["old"]; t = "\n".join(ls)
        else:
            if t.count(e["new"]) != 1:
                return None
            t = t.replace(e["new"], e["old"])
    for e in log["edits"]:
        if e["new"] == "" and e["mode"] == "str":
            anchor = "\n2. **OPEN-GEN-II-7B"
            if t.count(anchor) != 1:
                return None
            t = t.replace(anchor, e["old"] + anchor)
    ls = t.split("\n")
    for e in log["edits"]:
        if e["mode"] == "kf-line":
            if ls[e["line"] - 1] != e["new"]:
                return None
            ls[e["line"] - 1] = e["old"]
    return "\n".join(ls)

def gb13_independent():
    import sympy as sp
    x, y = sp.symbols("x y", real=True)
    # B from the 120° Gram condition: unit vectors at 120°, inner product -1/2; check it is J_Q-invariant
    B = sp.Matrix([[1, -sp.Rational(1, 2)], [-sp.Rational(1, 2), 1]])
    J = sp.Matrix([[1, -2], [2, -1]]) / sp.sqrt(3)
    if sp.simplify(J.T*B*J - B) != sp.zeros(2) or sp.simplify(J*J + sp.eye(2)) != sp.zeros(2):
        return False
    a = sp.Matrix(sp.symbols("a1 a2", real=True)); b = sp.Matrix(sp.symbols("b1 b2", real=True))
    lag = sp.expand((a.T*B*a)[0]*(b.T*B*b)[0] - ((a.T*B*b)[0])**2 - B.det()*(a[1]*b[0] - a[0]*b[1])**2)
    if lag != 0 or B.det() != sp.Rational(3, 4):
        return False
    Qs, Qc = sp.symbols("Qs Qc", positive=True)
    om2 = Qs*Qc / B.det()                                      # I_sc = 0
    stand = sp.Rational(1, 3)*Qc**2 + sp.Rational(1, 4)*om2 + sp.Rational(5, 16)*om2
    return sp.simplify(stand - sp.Rational(1, 3)*Qc**2 - sp.Rational(3, 4)*Qs*Qc) == 0

def check(base, inter, log, root, verbose=True):
    R = {}
    def gate(k, ok, msg=""):
        R[k] = bool(ok)
        if verbose: print(f"[{'PASS' if ok else 'FAIL'}] {k} {msg}")
    gate("C0", sha(base) == BASE_SHA, "BASE")
    try:
        b = load_builder(root); rebuilt, _, _ = b.build(base)
        ok1 = rebuilt == inter and sha(inter) == log["intermediate_sha256"]
    except AssertionError as e:
        ok1 = False
    gate("C1", ok1, "BUILD")
    rev = reverse_full(inter, log)
    gate("C2", rev == base, "REVERSE")
    ea = next(e for e in log["edits"] if e["key"] == "APPA"); eb = next(e for e in log["edits"] if e["key"] == "APPB")
    tail_b, tail_i = base[base.index(APPA):], inter[inter.index(APPA):] if APPA in inter else ""
    gate("C3", tail_i == tail_b.replace(APPA, ea["new"], 1).replace(APPB, eb["new"], 1), "APPENDIX")
    a0, a1 = "### §6.3a ", "### §6.4 "
    pb, pi = span(base, a0, a1), span(inter, a0, a1)
    pi_lines = [l for l in pi.split("\n") if not l.startswith(G20_NOTE_PREFIX)]
    nnote = sum(1 for l in pi.split("\n") if l.startswith(G20_NOTE_PREFIX))
    rows_ok = all([l for l in base.split("\n") if l.startswith(f"- [RID: {r}]")] ==
                  [l for l in inter.split("\n") if l.startswith(f"- [RID: {r}]")] for r in PROTECTED_RIDS)
    gate("C4", "\n".join(pi_lines) == pb and nnote == 1 and rows_ok, "PROTECTED")
    rid = re.compile(r"\[RID: (GEN-[A-Z0-9-]+)\]")
    rb, ri = set(rid.findall(base)), set(rid.findall(inter))
    others = "".join(open(os.path.join(root, "dsn", f), encoding="utf-8").read()
                     for f in os.listdir(os.path.join(root, "dsn")) if f.endswith(".md") and "GENESIS_GEOMETRY" not in f)
    coll = [r for r in NEW_RIDS if r in others or r in base]
    homes = all(inter.count(f"`[THM]` `[RID: {r}]`") == 1 for r in NEW_RIDS)
    gate("C5", ri == rb | NEW_RIDS and not coll and homes, f"RID SET {sorted(ri ^ (rb | NEW_RIDS))} collisions={coll}")
    kf = set(log["kf_lines"])
    bl = base.split("\n"); il = inter.split("\n")
    base_bare = sorted(l.replace("**Status summary.**", "**Status summary:**", 1) for n, l in enumerate(bl, 1) if BARE_K.search(l) and n not in kf and not l.startswith("### v2.") and n < bl.index(APPA.strip()) + 1)
    lv = live(inter).split("\n")
    inter_bare = sorted(l for l in lv if BARE_K.search(l))
    defl = [l for l in lv if l.startswith(KF_DEF_PREFIX)]
    fl = span(inter, "### §6.8 ", "### §6.10 ")
    fl_bare = [l for l in fl.split("\n") if BARE_K.search(l) and not l.startswith(KF_DEF_PREFIX)]
    gate("C6", len(defl) == 1 and inter_bare == sorted(base_bare + [l for l in defl if BARE_K.search(l)]) and not fl_bare, f"KAPPA (face-lift bare κ left: {len(fl_bare)})")
    okt = True; bad = []
    for t in TAGS:
        d = sum(e["new"].count(t) - e["old"].count(t) for e in log["edits"])
        if base.count(t) + d != inter.count(t): okt = False; bad.append(t)
    rem = [(e["key"], t) for e in log["edits"] for t in TAGS if e["new"].count(t) < e["old"].count(t)]
    gate("C7", okt and not rem, f"TAGS {bad} removed={rem}")
    nine = span(inter, "**(OPEN-GEN-II-9A) Scalar-M eigendecomposition.**", "`[RID: GEN-THM-SCALARM-EIGEN]`")
    ok8 = (r"\mp\operatorname{sgn}(m)\kappa_f" in nine and r"\frac{\Pi_+}{\tau-g-\operatorname{sgn}(m)\kappa_f}" in nine
           and r"\Pi_\pm=\tfrac{1}{2}\!\left(I\pm\hat N\right)" in nine
           and r"\kappa_f=m|w|" not in inter and r"\kappa=m|w|" not in live(inter) and r"\frac{\Delta M_f}{\kappa" not in inter
           and r"\mp\operatorname{sgn}(m)\kappa_f" in span(inter, "Closed under scalar-M (OPEN-GEN-II-9A", "4. Scalar susceptibility"))
    gate("C8", ok8, "SIGN")
    L = live(inter)
    sj = [l for l in L.split("\n") if "**Local sourced-junction theorem" in l]
    exp = [l for l in L.split("\n") if l.startswith("`[DEF]` Genesis may export theorem-grade primitive algebra")]
    gate("C9", "has a valid minimizer" not in L and len(sj) == 2 and all(r"\Delta_3>0" in l for l in sj)
         and len(exp) == 1 and "physical branch selection OPEN" in exp[0], "GA-01")
    hb, hi = bl[:12], il[:12]
    hdr = (all(x == y for k, (x, y) in enumerate(zip(hb, hi)) if k not in (9, 10)) and hb[9] != hi[9]
           and hi[9].startswith("**Programme tier:** Tier 3 ")
           and hi[10] == hb[10].replace("**Status summary.**", "**Status summary:**", 1) and hb[10] != hi[10])
    foot = base[base.index("*END OF DOCUMENT"):] == inter[inter.index("*END OF DOCUMENT"):]
    gate("C10", hdr and foot, "HEADER")
    hset_b, hset_i = heads(base), heads(inter)
    gate("C11", all(h in hset_i for h in hset_b) and set(hset_i) - set(hset_b) == NEW_HEADINGS, "HEADINGS")
    paths = set(re.findall(r"`(evidence/[^`]+)`", L))
    miss = [p for p in paths if not os.path.exists(os.path.join(root, p.rstrip("/")))]
    hok = sha(open(os.path.join(root, EVID[0]), "rb").read()) == EVID[1]
    gate("C12", not miss and hok, f"EVIDENCE missing={miss}")
    gate("C13", gb13_independent() and ("Specialization of `GEN-THM-DELTA-QC`" in L) == log["gate_GB13"]["pass"], "GB13")
    d = git_show(root, "dyad-v6.4.22:dsn/RTG_DYADIC_OSCILLATOR_DSN.md")
    t6 = git_show(root, "triad-v1.6.1:dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md")
    pg = git_show(root, "programme-v1.3:dsn/RTG_PROGRAMME_OVERVIEW.md")
    ok14 = ("[RID: DYAD-THM-SMOOTH-EQUIVARIANT-CHART]" in d and "DYAD-THM-SMOOTH-EMBEDDING" in d
            and r"$\Phi(0)=0$, $D\Phi(0)=I$, $\Phi\circ J=A\circ\Phi$, and $N_\Phi:=\Phi T\Phi^{-1}$ commutes with $A$" in d
            and "+89\\sqrt3/324" in d and "-119\\sqrt{3}/648" in d
            and re.search(r"\| Shear, \$-2\\sqrt3/3\$ \| Vector seed[^|]*\| \$\\sqrt\{21\}/64\$", t6) is not None
            and "the largest diagnostic ratio is $\\sqrt{14}/16$" in t6
            and "| IF06 | GEN → TRIAD |" in pg and "| v2.8.7 |" in pg and "| IF08 | GEN → UVM |" in pg and "| v2.8.5 |" in pg
            and "Tier 3" in pg
            and "`[conv: RTG canonical B-metric]` The canonical normalization uses" in t6
            and r"I_{sc}^2+\frac34(\omega_{sc}^{(\mathrm{RTG})})^2=Q_sQ_c" in t6
            and "Cross-convention warning for T-6m" in t6)
    gate("C14", ok14, "SOURCES")
    defs = {k: len(re.findall(r"^- `\[" + k + r"\]` ::", L, re.M)) for k in ("custody-A", "indep-AC")}
    art = [l for l in L.split("\n") if re.match(r"- \[RID: GEN-ART-(PURE-CHIRAL|PHI-2TO3|G2-CHRONO|P4-PRIMITIVE|PHASE-AVG|PHASE-CLOSURE|QH-NOGO|FACE-LIFT|SOURCED-JUNCTION)\]", l)]
    ok15 = ("v2.9" not in L and all(v == 1 for v in defs.values()) and len(art) == 9
            and all("`[custody-A]`" in l and "held by neither" not in l for l in art)
            and L.count("held by neither Genesis co-owner session") == 1
            and L.count("not a rerun of missing original code") == 1
            and "has a valid" not in L and "has a valid minimizer" in inter[inter.index(APPB):])
    gate("C15", ok15, f"LIVE (standard-clause definitions {defs}; custody rows {len(art)})")
    return R

CONTROLS = [
 # (name, target, mutation, gates that must fail)
 ("NC1 9A sign dropped", "inter", (r"\frac{\Pi_+}{\tau-g-\operatorname{sgn}(m)\kappa_f}", r"\frac{\Pi_+}{\tau-g-\kappa_f}"), {"C1", "C8"}),
 ("NC2 edit inside §6.3c", "inter", ("**G-SEL.** No physical model", "**G-SEL.** No physical models"), {"C1", "C4"}),
 ("NC3 minimizer clause back", "inter", ("no minimizer is selected here.", "it has a valid minimizer."), {"C1", "C9", "C15"}),
 ("NC4 birth κ renamed", "inter", (r"Both retained reference policies have \(\kappa<0\)", r"Both retained reference policies have \(\kappa_f<0\)"), {"C1", "C6"}),
 ("NC5 base not v2.8.9", "base", ("**Date:** 19 October 2026", "**Date:** 18 October 2026"), {"C0", "C1"}),
 ("NC6 RID dropped", "inter", ("`[THM]` `[RID: GEN-THM-QH-NOGO]` ", "`[THM]` "), {"C1", "C5"}),
 ("NC7 Appendix A history edited", "inter", ("### v2.8.9 — 19 October 2026 — Adopted scientific release", "### v2.8.9 — 19 October 2026 — Adopted release"), {"C1", "C3"}),
 ("NC8 header status edited", "inter", ("**Date:** 19 October 2026", "**Date:** 24 October 2026"), {"C1", "C10"}),
 ("NC9 bare face-lift κ reintroduced", "inter", (r"$|a(\phi)| \leq \kappa_f$", r"$|a(\phi)| \leq \kappa$"), {"C1", "C6"}),
 ("NC10 dated marker in live text", "inter", ("Cascade condition: $\\langle\\mathcal{P}_4\\rangle > 0$. This six-member", "Cascade condition: $\\langle\\mathcal{P}_4\\rangle > 0$. (v2.9) This six-member"), {"C1", "C15"}),
 ("NC11 custody clause inlined", "inter", ("closure and plateau shear bridge derivation :: `[ALG structure]` — `[custody-A]`", "closure and plateau shear bridge derivation :: `[ALG structure]` — proof source not in the repository; custody (a) missing — held by neither Genesis co-owner session"), {"C1", "C15"}),
]

def controls(base, inter, log, root):
    allok = True
    for name, tgt, (a, b), must in CONTROLS:
        bb, ii = base, inter
        if tgt == "inter":
            assert ii.count(a) == 1, f"{name}: anchor count {ii.count(a)}"; ii = ii.replace(a, b)
        else:
            assert bb.count(a) == 1, f"{name}: anchor count {bb.count(a)}"; bb = bb.replace(a, b)
        R = check(bb, ii, log, root, verbose=False)
        failed = {k for k, v in R.items() if not v}
        ok = must <= failed
        allok &= ok
        print(f"[{'CAUGHT' if ok else 'MISSED'}] {name}: must fail {sorted(must)}; failed {sorted(failed)}")
    print(f"\n{'all controls caught' if allok else 'CONTROL MISSED'}")
    return allok

def main(argv):
    base_p, inter_p, log_p = argv[1:4]
    root = argv[argv.index("--root") + 1] if "--root" in argv else "."
    base = open(base_p, encoding="utf-8").read(); inter = open(inter_p, encoding="utf-8").read()
    log = json.load(open(log_p, encoding="utf-8"))
    if "--controls" in argv:
        sys.exit(0 if controls(base, inter, log, root) else 1)
    R = check(base, inter, log, root)
    n = sum(R.values())
    print(f"\n{n}/{len(R)} gates PASS; base {sha(base)[:8]}…, intermediate {sha(inter)}")
    sys.exit(0 if n == len(R) else 1)

if __name__ == "__main__":
    main(sys.argv)
