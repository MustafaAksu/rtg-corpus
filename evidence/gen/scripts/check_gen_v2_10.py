#!/usr/bin/env python3
"""Checker for the Genesis v2.10 content stage (candidate; not an edition).

usage: check_gen_v2_10.py BASE CANDIDATE EDITLOG_JSON [--root REPO] [--controls]
  BASE = `git show gen-v2.9:dsn/RTG_GENESIS_GEOMETRY_DSN.md`; run from the repository root (tags and evidence are read from it).

Gates (exit 0 iff all PASS):
 C0  BASE        base bytes are adopted v2.9 (9178ca2c…00ac)
 C1  BUILD       the builder reproduces the candidate byte-exactly; the log hash matches
 C2  REVERSE     undoing the logged edits in reverse order recovers the base byte-exactly
 C3  PROTECTED   §6.3a–§6.3c byte-identical; §8 rows of the K3/6S/D-4 RIDs identical
 C4  RID SET     GEN RIDs = base + {GEN-ALG-P4-DRIFT-IDENTITY, GEN-ALG-BIRTH-SYMMETRY-SEED}; each attached once at an `[ALG]`
                 statement; no collision in other dsn/ files; GEN-CAND-APEX-T6U kept
 C5  TAGS        per-tag census: base + Σ(new−old) = candidate; the only decreases are [THM] −1 (G8) and [CAND] −1 (G6: T-6s/T-6t
                 lose their line tags; R1 adds an inline `[CAND]` for the proposed OPEN-M use of T-6s)
 C6  G7          the identity line shows the cubic term 2dᵀB G₂,d, names L⁶=I (GEN-THM-LIN-ORDER6) and G₂=0 (§6.4), states the
                 boxed identity, the custody of the 𝒫₄ census, and is not filed under GEN-THM-DELTA-QC
 C7  G8          no `[THM]` birth-symmetry statement remains; the RID is cited at §6.6, §1 and §2; the §8 artifact row keeps its
                 typing and points to the RID; the Appendix B correction entry exists
 C8  G6          T-6s/T-6t lines are `[ALG]` imports at v1.7 (R1: the T-6s interface use is stated separately as `[CAND]`); T-6u has an `[ALG]` import line at v1.7 and the Genesis `[CAND]`
                 GEN-CAND-APEX-T6U reading; no v1.6 §6.15–§6.17 import remains
 C9  PINS        every tag named in the live text exists in the repository; no `ofn-v0.10` and no Discrete Genesis v2.12.13 remains live
 C10 G5          the DYAD-ALG-NU5-P5 row carries the ℚ(ζ₅) label and the dyad-v6.4.23 pin in the same row; the value line in §6.2 is unchanged
 C11 G1          GEN-ART-G2-CHRONO keeps [custody-A]; the route is "a new proof, not a recovery"; the NUMGEN row carries [RESULT][from: ALG]
 C12 SOURCES     the cited producer facts are present at numgen-v1.21, dyad-v6.4.23, triad-v1.7, ofn-v0.12, tdrg-v2.12.14
 C13 EVIDENCE    [indep-INB] defined exactly once; its script exists with the quoted hash prefix; the script passes on the candidate
 C14 HEADER      title v2.10; Supersedes = v2.9 with full hash; candidate status; one footer, candidate form
 C15 APPENDICES  Appendix A = base with exactly the v2.10 entry inserted above v2.9; Appendix B = base with exactly the new entry inserted
"""
import hashlib, importlib.util, json, os, re, subprocess, sys

BASE_SHA = "9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac"
NEW = {"GEN-ALG-P4-DRIFT-IDENTITY", "GEN-ALG-BIRTH-SYMMETRY-SEED"}
PROT = ["GEN-THM-K3-PLANAR-FACTOR-NOGO", "GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA", "GEN-THM-K3-SIXSTEP-FACTOR-NOGO",
        "GEN-DEF-MEANFEEDBACK-FAMILY", "GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO", "GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO"]
TAGS = ["[THM]", "[ALG]", "[OPEN]", "[DEF]", "[RESULT]", "[COR]", "[HYP]", "[FAIL]", "[CAND]", "[RETRACTED]", "[ALG structure]", "[CONVENTION]"]
ALLOWED_DROP = {"[THM]": -1, "[CAND]": -1}
APPA = "## Appendix A — Version History {#appendix-a}"
APPB = "## Appendix B — Retired and Rejected Claims {#appendix-b}"
SCRIPT = ("evidence/gen/scripts/gen_inbox_checks.py", "4b9f0a3c", "5415")

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()
def span(s, a, b): i = s.index(a); return s[i:s.index(b, i)]
def live(s): return s[:s.index(APPA)]

def builder(root):
    p = os.path.join(root, "evidence/gen/scripts/build_gen_v2_10.py")
    sp_ = importlib.util.spec_from_file_location("b", p); m = importlib.util.module_from_spec(sp_); sp_.loader.exec_module(m); return m

def show(root, ref):
    return subprocess.run(["git", "-C", root, "show", ref], capture_output=True, text=True).stdout

def reverse(c, log):
    t = c
    for e in reversed(log["edits"]):
        if e["mode"] == "line":
            ls = t.split("\n"); idx = [i for i, l in enumerate(ls) if l == e["new"]]
            if len(idx) != 1:
                if t.count(e["new"]) != 1: return None
                t = t.replace(e["new"], e["old"]); continue
            ls[idx[0]] = e["old"]; t = "\n".join(ls)
        else:
            if t.count(e["new"]) != 1: return None
            t = t.replace(e["new"], e["old"])
    return t

def check(base, cand, log, root, verbose=True):
    R = {}
    def g(k, ok, m=""):
        R[k] = bool(ok)
        if verbose: print(f"[{'PASS' if ok else 'FAIL'}] {k} {m}")
    g("C0", sha(base) == BASE_SHA, "BASE")
    try:
        t, _ = builder(root).build(base); ok = t == cand and sha(cand) == log["candidate_sha256"]
    except AssertionError:
        ok = False
    g("C1", ok, "BUILD")
    g("C2", reverse(cand, log) == base, "REVERSE")
    a0, a1 = "### §6.3a ", "### §6.4 "
    rows = all([l for l in base.split("\n") if l.startswith(f"- [RID: {r}]")] == [l for l in cand.split("\n") if l.startswith(f"- [RID: {r}]")] for r in PROT)
    g("C3", span(base, a0, a1) == span(cand, a0, a1) and rows, "PROTECTED")
    rid = re.compile(r"\[RID: (GEN-[A-Z0-9-]+)\]")
    rb, rc = set(rid.findall(base)), set(rid.findall(cand))
    others = "".join(open(os.path.join(root, "dsn", f), encoding="utf-8").read() for f in os.listdir(os.path.join(root, "dsn"))
                     if f.endswith(".md") and "GENESIS_GEOMETRY" not in f)
    homes = all(cand.count(f"`[ALG]` [RID: {r}]") == 1 for r in NEW)
    g("C4", rc == rb | NEW and not any(r in others or r in base for r in NEW) and homes and "[RID: GEN-CAND-APEX-T6U]" in cand,
      f"RID SET {sorted(rc ^ (rb | NEW))}")
    bad = []
    for tg in TAGS:
        d = sum(e["new"].count(tg) - e["old"].count(tg) for e in log["edits"])
        if base.count(tg) + d != cand.count(tg): bad.append(tg)
    deltas = {tg: live(cand).count(tg) - live(base).count(tg) for tg in TAGS}
    drops = {tg: v for tg, v in deltas.items() if v < 0}
    g("C5", not bad and drops == ALLOWED_DROP, f"TAGS census_bad={bad} live drops={drops}")
    L = live(cand)
    g7 = [l for l in L.split("\n") if l.startswith("`[ALG]` [RID: GEN-ALG-P4-DRIFT-IDENTITY]")]
    ok7 = (len(g7) == 1 and r"2d^\top B\,G_{2,d}(Z)" in g7[0] and "GEN-THM-LIN-ORDER6" in g7[0] and r"$G_2=0$ (§6.4)" in g7[0]
           and "cubic term first" in g7[0] and "GEN-ART-P4-PRIMITIVE" in L and "distinct from it" in L
           and r"\mathcal P_4(s,c,d)=\Delta Q_d^{(4)}=2d^\top B\,G_{3,d}(s,c,d)" in L)
    g("C6", ok7, "G7")
    ok8 = ("`[THM]` **Birth-symmetry" not in cand and cand.count("`[ALG]` [RID: GEN-ALG-BIRTH-SYMMETRY-SEED] **Birth-symmetry") == 1
           and "birth-symmetry sign (`GEN-ALG-BIRTH-SYMMETRY-SEED`, §6.6)" in L and "birth-symmetry sign (`GEN-ALG-BIRTH-SYMMETRY-SEED`), phase-drift law" in L
           and "(artifact typing; supports `GEN-ALG-BIRTH-SYMMETRY-SEED`, §6.6)" in L
           and "**[RETRACTED | RID: GEN-ALG-BIRTH-SYMMETRY-SEED]**" in cand[cand.index(APPB):])
    g("C7", ok8, "G8")
    ok6 = (L.count("`[ALG]` `[import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 §6.15 | TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY]`") == 1
           and L.count("`[ALG]` `[import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 §6.16 | TRIAD-ALG-T6T-JACOBI-MODE-SIGNS]`") == 1
           and L.count("`[ALG]` `[import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 §6.17 | TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC]`") == 1
           and L.count("**[CAND]** `[scope: primitive seed diagnostic]` [RID: GEN-CAND-APEX-T6U]") == 1
           and not re.search(r"RTG_TRIADIC_BIRTH_LIFT_DSN_v1\.6 §6\.1[5-7]", L)
           and "This remains a candidate interface statement" not in L
           and L.count("The imported coherent-family identity is `[ALG]`; its proposed use as an OPEN-M interface remains `[CAND]` and is not a source realization.") == 1)
    g("C8", ok6, "G6")
    named = set(re.findall(r"`((?:gen|dyad|triad|numgen|ofn|tdrg|programme|methodology|rrf|recog)-v[0-9.]+)`", L))
    missing = sorted(t for t in named if subprocess.run(["git", "-C", root, "rev-parse", "-q", "--verify", f"{t}^{{commit}}"],
                                                        capture_output=True).returncode != 0)
    g("C9", not missing and "ofn-v0.10" not in L and "OFN v0.10" not in L and "v2.12.13" not in L, f"PINS missing tags={missing}")
    nu = [l for l in L.split("\n") if l.startswith("- [RID: DYAD-ALG-NU5-P5]")]
    val_b = [l for l in base.split("\n") if l.startswith("- $p=5$: $\\nu_5^{(5)}")]
    val_c = [l for l in cand.split("\n") if l.startswith("- $p=5$: $\\nu_5^{(5)}")]
    g("C10", len(nu) == 1 and r"exact in $\mathbb{Q}(\zeta_5)$" in nu[0] and "claim-level pin `dyad-v6.4.23` §6.11" in nu[0] and val_b == val_c and len(val_c) == 1, "G5")
    ch = [l for l in L.split("\n") if l.startswith("- [RID: GEN-ART-G2-CHRONO]")]
    ng = [l for l in L.split("\n") if l.startswith("- [RID: NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE]")]
    g("C11", len(ch) == 1 and "`[custody-A]`" in ch[0] and "(a new proof, not a recovery)" in ch[0] and len(ng) == 1
      and "`[RESULT][from: ALG]`" in ng[0] and "not a recovery of its original source" in L and "recovered" not in " ".join(ch + ng), "G1")
    n = show(root, "numgen-v1.21:dsn/RTG_NUMBER_GENESIS_DSN.md"); d = show(root, "dyad-v6.4.23:dsn/RTG_DYADIC_OSCILLATOR_DSN.md")
    tr = show(root, "triad-v1.7:dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md"); o = show(root, "ofn-v0.12:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md")
    td = show(root, "tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md")
    ok12 = ("`[RESULT][from: ALG]` [RID: NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE]" in n and "[f^p-id]_d=pR^{-1}\\Pi_0h_d" in n
            and r"exact in $\mathbb{Q}(\zeta_5)$, $\zeta_5=e^{2\pi i/5}$ (real and imaginary parts in $\mathbb{Q}(\sqrt5,\sqrt{10+2\sqrt5})$; `[v6.4.20]` field label corrected" in d)
    ok12 = ok12 and all(re.search(r"^### §6\.%s .*\n(?:.*\n)*?`\[ALG\]` \[RID: %s\]" % (s, r), tr, re.M) is not None
                        for s, r in (("15", "TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY"), ("16", "TRIAD-ALG-T6T-JACOBI-MODE-SIGNS"), ("17", "TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC")))
    ok12 = ok12 and o.startswith("# RTG_ONTOLOGICAL_FOUNDATIONS_v0.12") and td.startswith("# RTG_DISCRETE_GENESIS_DSN_v2.12.14") and "TDR-19" in td
    i655 = d.split("\n").index(next(l for l in d.split("\n") if "[RID: DYAD-ALG-NU5-P5]" in l and "Closed form" in l))
    head = [l for l in d.split("\n")[:i655] if l.startswith("### ")][-1]
    ok12 = ok12 and head.startswith("### §6.11")
    g("C12", ok12, "SOURCES")
    dfn = len(re.findall(r"^- `\[indep-INB\]` ::", L, re.M))
    p = os.path.join(root, SCRIPT[0]); h = sha(open(p, "rb").read()) if os.path.exists(p) else ""
    run_ok = False
    if h:
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(cand); tmp = f.name
        run_ok = subprocess.run([sys.executable, "-I", p, tmp], capture_output=True).returncode == 0; os.unlink(tmp)
    g("C13", dfn == 1 and h.startswith(SCRIPT[1]) and h.endswith(SCRIPT[2]) and f"`{SCRIPT[1]}…{SCRIPT[2]}`" in L and run_ok,
      f"EVIDENCE (definitions={dfn}; script run on candidate={'PASS' if run_ok else 'FAIL'})")
    hd = cand[:cand.index("\n## ")]
    foot = [l for l in cand.split("\n") if l.startswith("*END OF DOCUMENT")]
    g("C14", hd.startswith("# RTG_GENESIS_GEOMETRY_DSN_v2.10\n") and f"(SHA-256 `{BASE_SHA}`; tag `gen-v2.9`)" in hd
      and "**Document status:** CANDIDATE — not adopted" in hd and foot == ["*END OF DOCUMENT — RTG_GENESIS_GEOMETRY_DSN_v2.10 (candidate; not adopted).*"], "HEADER")
    ea = next(e for e in log["edits"] if e["key"] == "APPA"); eb = next(e for e in log["edits"] if e["key"] == "APPB")
    tb = base[base.index(APPA):base.index("*END OF DOCUMENT")]; tc = cand[cand.index(APPA):cand.index("*END OF DOCUMENT")]
    g("C15", tc == tb.replace(ea["old"], ea["new"], 1).replace(eb["old"], eb["new"], 1), "APPENDICES")
    return R

CONTROLS = [
 ("NC1 G7 without the G2=0 premise", (r"With $L^6=I$ (`GEN-THM-LIN-ORDER6`) and $G_2=0$ (§6.4) the cubic term", r"With $L^6=I$ (`GEN-THM-LIN-ORDER6`) the cubic term"), {"C1", "C6"}),
 ("NC2 independent clause rewritten as an original rerun", ("- `[indep-INB]` :: independent contribution, not a rerun of missing original code and not a recovery of the original source",
                                                            "- `[indep-INB]` :: rerun of the original census code (`EV-RUN`)"), {"C1"}),
 ("NC3 NUMGEN application relabelled as the original proof", ("(a new proof, not a recovery)", "(the original proof, recovered)"), {"C1", "C11"}),
 ("NC4 T-6u CAND/ALG collapse", ("**[CAND]** `[scope: primitive seed diagnostic]` [RID: GEN-CAND-APEX-T6U] Genesis interface reading of the import above:", "Genesis interface reading of the import above:"), {"C1", "C8"}),
 ("NC5 ν5 label changed without the matching pin", ("claim-level pin `dyad-v6.4.23` §6.11, where the field label is corrected", "v2.8.8"), {"C1", "C10"}),
 ("NC6 wrong Triadic tag", ("- Triadic: v1.7 (`triad-v1.7`)", "- Triadic: v1.7 (`triad-v1.9`)"), {"C1", "C9"}),
 ("NC7 birth-symmetry grade left [THM]", ("`[ALG]` [RID: GEN-ALG-BIRTH-SYMMETRY-SEED] **Birth-symmetry", "`[THM]` [RID: GEN-ALG-BIRTH-SYMMETRY-SEED] **Birth-symmetry"), {"C1", "C4", "C7"}),
 ("NC8 byte change in §6.3c", ("**G-SEL.** No physical model", "**G-SEL.** No physical models"), {"C1", "C3"}),
 ("NC9 identity filed under GEN-THM-DELTA-QC", ("It is the $d$-mode analogue of `GEN-THM-DELTA-QC` and distinct from it.", "It is part of `GEN-THM-DELTA-QC`."), {"C1", "C6"}),
 ("NC11 R1 reverted", ("The imported coherent-family identity is `[ALG]`; its proposed use as an OPEN-M interface remains `[CAND]` and is not a source realization.",
                       "This remains a candidate interface statement, not an OPEN-M source realization."), {"C1", "C8"}),
 ("NC10 printed 𝒫₄ coefficient altered", (r"&-\tfrac{1}{8}Q_sI_{ds} - \tfrac{3}{32}Q_s\omega_{ds} \\", r"&-\tfrac{1}{8}Q_sI_{ds} - \tfrac{3}{16}Q_s\omega_{ds} \\"), {"C1", "C13"}),
]

def controls(base, cand, log, root):
    allok = True
    for name, (a, b), must in CONTROLS:
        assert cand.count(a) == 1, f"{name}: anchor count {cand.count(a)}"
        R = check(base, cand.replace(a, b), log, root, verbose=False)
        failed = {k for k, v in R.items() if not v}
        ok = must <= failed; allok &= ok
        print(f"[{'CAUGHT' if ok else 'MISSED'}] {name}: must fail {sorted(must)}; failed {sorted(failed)}")
    print("\nall controls caught" if allok else "\nCONTROL MISSED")
    return allok

def main(argv):
    bp, cp, lp = argv[1:4]; root = argv[argv.index("--root") + 1] if "--root" in argv else "."
    base = open(bp, encoding="utf-8").read(); cand = open(cp, encoding="utf-8").read(); log = json.load(open(lp, encoding="utf-8"))
    if "--controls" in argv:
        sys.exit(0 if controls(base, cand, log, root) else 1)
    R = check(base, cand, log, root); n = sum(R.values())
    print(f"\n{n}/{len(R)} gates PASS; base {sha(base)[:8]}…, candidate {sha(cand)}")
    sys.exit(0 if n == len(R) else 1)

if __name__ == "__main__":
    main(sys.argv)
