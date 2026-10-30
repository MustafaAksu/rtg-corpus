#!/usr/bin/env python3
r"""Triadic v1.7 — stage-1 checker (gates + negative controls).

usage: check_triad_v1_7_stage1.py BASE CANDIDATE EDITLOG_JSON [--controls]
  BASE = `git show triad-v1.6.1:dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md`; run from the repository root.
Gates:
  K1 base identity (triad-v1.6.1);
  K2 deterministic rebuild (builder output == candidate) and edit-log hash chain ending at the candidate;
  K3 the set of TRIAD-* identifiers is unchanged and the declared count is 46 (the RER record name excluded);
  K4 every {#anchor} kept, in order;
  K5 every `Status:` line of the OPEN/PARTIAL/CLOSED records unchanged, in order;
  K6 Appendix A byte-identical to the base;
  K7 stale phrases absent from the live text (before Appendix A);
  K8 required statements present (rows 1-5, 7-11, 13-15, 21, custody);
  S1 the two evidence scripts cited for rows 1-3 run with exit 0 and print RESULT: PASS;
  S5 the T-6q coordinate sign table, parsed from the candidate, equals the exact SymPy computation;
  S6 the producer Gram identity Q_sQ_c - I^2 = Omega^2 with B_T and omega_raw = -Omega/sqrt3 (premise of S5).
--controls applies negative-control mutations to the candidate; each must fail its named gate.
A passing run authorizes nothing.
"""
import hashlib, json, re, subprocess, sys, os, importlib.util
import sympy as sp

BASE_SHA = "95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f"
HERE = os.path.dirname(os.path.abspath(__file__))
LIVE_END = "## Appendix A — Version History"

STALE = [
    "Send CN-01–CN-05", "Programme/OFN pass two follows", "its pass-two synchronization is still pending",
    "consumer acceptance remains pending", "Consumer acceptance remains pending", "Consumer acceptance remains OPEN until",
    "Consumer status: OPEN", "consumer synchronization pending", "scientific reconciliation pending",
    "`[COR v1.6.1", "`[v1.6.1 r2 —", "`[ALG+NUM diagnostic]`", "OPEN-B-E1", "`[ALG/NUM synthesis]`",
    "is preserved under `evidence/accepted_r4_2/`", "**Two-pass handoff.**", "No new numerical sweep is required for this r4",
    "**Adoption record (v1.6.1):** `records/OWNER_ADOPTION_v1_6_1.json`", "**Document status:** ADOPTED",
]
REQUIRED = [
    # row 1
    "The off-root extension is not unique, and $f_s$, $f_c$ depend on it.",
    "In (b), $f_s=\\dot Q_s$ and $f_c=\\dot Q_c$; in (a), $f_s=\\dot Q_s+rQ_sq_1$ and $f_c=\\dot Q_c-rQ_cq_1$.",
    "In extension (a), $\\dot D=r\\,q_1D$",
    "special solutions such as $D\\equiv0$ ($K=1$)",
    "not a conserved physical mode, and not a statement about the exact six-step map. No RID is assigned.",
    "not the $H_1,H_2$ producer bytes, which are not in the repository",
    "time is the continuous coefficient-ODE time in units of one six-step block, not the exact discrete six-step map",
    # row 2
    "is the first-variation (degree-3) coefficient of the exact identity $\\Delta\\mathcal G\\equiv0$",
    "both of degree 4, which the retained six-step expansion discards",
    "not an exact discrete conservation law of the six-step map",
    # row 3
    "$$6(\\sqrt3-1)K\\le A_\\theta^{\\rm corr}\\le6(\\sqrt3+1)K.$$",
    "without a proved uniform remainder smaller than the lower margin",
    # row 4
    "- **C1 — carrier and metric.**", "- **C2 — encoding and reduction.**", "- **C3 — full evolution.**",
    "- **C4 — clock and phase convention.**", "- **C5 — events and regularity.**", "- **C6 — covariance.**",
    "including how each coefficient extends off the root; this fixes $f_s$, $f_c$ and the fate of $D$",
    "No corrected-field trajectory campaign is treated as scientifically decisive before the T-6r acceptance contract",
    # row 5
    "This is coordinate bookkeeping, not a physical action",
    "T-6n's naive-flip failure and its OPEN continuation are unchanged",
    # row 7
    "the same arithmetic would give 192 instead of 96",
    "This paragraph is the single statement of the 96:1 status",
    # row 8
    "**Companion documents (governing editions read for v1.7):**",
    "is repinned to Dyadic v6.4.23",
    "**v1.7 claim-level pins:**",
    "claim-level historical pin kept",
    # row 9, 10, 11
    "**Consumer state (current).**",
    "| CN-05 | Programme (`programme-v1.3`) |",
    "Programme v1.3 (`programme-v1.3`) is the pass-two synchronization edition",
    "**Consumer interface.** The per-recipient state of CN-01–CN-05 is in §7.4.",
    "A v1.6 receipt is not acceptance of a v1.6.1 or v1.7 delta.",
    # row 13
    "This ledger declares 46 `TRIAD-*` RIDs (13 ALG, 22 ART, 2 EXPORT, 2 NUM, 7 OPEN)",
    "close OPEN-A/OPEN-B/E1",
    # row 21
    "**Current reading of the negative records above (v1.7).**",
    "| `[FAIL]` $I_{sc}^*$ as full-system stable attractor | not a current failure",
    # custody, row 24, row 25
    "is held by the PI and is **not in the repository**",
    "`records/triad/OWNER_ADOPTION_v1_6_1.json` (SHA-256 `33bcd3cea83b467d0bc4d8cc4a37c10771cd81151831caec87c55873937cd5dd`)",
    "`records/triad/RELEASE_RECORD_v1_6_1.md` (SHA-256 `aa3d8d773a2083908f2e576bc59f9c6d3c110c1caadbc70782c72b07e95eb45d`)",
    "in the repository at `evidence/triad/scripts/` (recovered from commit `9df0319`; hash equal",
    # status
    "**Document status:** DRAFT — stage-1 intermediate of v1.7",
]

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()
def live(t): return t[:t.index(LIVE_END)]
def appA(t): return t[t.index(LIVE_END):t.index("## Appendix B — Retired and Rejected Claims")]
def rid_set(t): return set(re.findall(r"(?<!RER-)\bTRIAD-[A-Z0-9]+(?:-[A-Z0-9]+)*", t))
def all_triad_strings(t): return set(re.findall(r"TRIAD-[A-Z0-9]+(?:-[A-Z0-9]+)*", t))
def anchors(t): return re.findall(r"\{#([^}]+)\}", t)
def statuses(t): return re.findall(r"^Status: .*$", t, re.M)

def load_builder():
    spec = importlib.util.spec_from_file_location("b", os.path.join(HERE, "build_triad_v1_7_stage1.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def sign_table_ok(t):
    """S5: parse the T-6q table and compare with exact computation."""
    a = t.index("**Coordinate sign table.**"); b = t.index("$K$ is invariant under each operation.", a)
    rows = [r for r in t[a:b].split("\n") if r.startswith("| $(s,c)\\mapsto")]
    if len(rows) != 3: return False, "table rows != 3"
    s1, s2, c1, c2 = sp.symbols("s_rho s_eta c_rho c_eta", real=True)
    B = sp.Matrix([[2, -1], [-1, 2]])
    def inv(s, c):
        Qs = (s.T*B*s)[0]; Qc = (c.T*B*c)[0]; I = (s.T*B*c)[0]
        Om = -sp.sqrt(3)*(s[1]*c[0] - s[0]*c[1])          # Omega = -sqrt3 * omega_raw
        return sp.expand(Qs), sp.expand(Qc), sp.expand(I), sp.expand(Om)
    s = sp.Matrix([s1, s2]); c = sp.Matrix([c1, c2])
    Qs, Qc, I, Om = inv(s, c)
    ops = {"$(s,c)\\mapsto(c,s)$": (c, s), "$(s,c)\\mapsto(-s,c)$": (-s, c), "$(s,c)\\mapsto(-s,-c)$": (-s, -c)}
    def word(new, old, alt=None):
        if sp.expand(new - old) == 0: return "unchanged"
        if sp.expand(new + old) == 0: return "negated"
        return "?"
    for r in rows:
        cells = [x.strip() for x in r.strip("|").split("|")]
        op, qcol, icol, ocol, mncol, sgcol = cells
        Qs2, Qc2, I2, Om2 = inv(*ops[op])
        q = "exchanged" if (sp.expand(Qs2 - Qc) == 0 and sp.expand(Qc2 - Qs) == 0 and sp.expand(Qs - Qc) != 0) else \
            ("unchanged" if sp.expand(Qs2 - Qs) == 0 and sp.expand(Qc2 - Qc) == 0 else "?")
        iw, ow = word(I2, I), word(Om2, Om)
        sgw = "flips" if ow == "negated" else ("unchanged" if ow == "unchanged" else "?")
        mu = {"unchanged": "\\mu", "negated": "-\\mu"}[iw]; nu = {"unchanged": "\\nu", "negated": "-\\nu"}[ow]
        mn = "unchanged" if (iw, ow) == ("unchanged", "unchanged") else f"$({mu},{nu})$"
        K_inv = sp.simplify((I2**2 + Om2**2)/(Qs2*Qc2) - (I**2 + Om**2)/(Qs*Qc)) == 0
        got = (qcol, icol, ocol, mncol, sgcol); want = (q, iw, ow, mn, sgw)
        if got != want or not K_inv: return False, f"{op}: table {got} != computed {want}, K invariant {K_inv}"
    return True, "3 rows match"

def gram_ok():
    s1, s2, c1, c2 = sp.symbols("s_rho s_eta c_rho c_eta", real=True)
    B = sp.Matrix([[2, -1], [-1, 2]]); s = sp.Matrix([s1, s2]); c = sp.Matrix([c1, c2])
    Qs = (s.T*B*s)[0]; Qc = (c.T*B*c)[0]; I = (s.T*B*c)[0]; Om = -sp.sqrt(3)*(s2*c1 - s1*c2)
    return sp.expand(Qs*Qc - I**2 - Om**2) == 0

def gates(base, cand, log, run_scripts=True):
    R = {}
    R["K1"] = sha(base) == BASE_SHA
    try:
        out, _ = load_builder().apply(base)
        chain = all(log["edits"][k]["doc_sha256_after"] == log["edits"][k+1]["doc_sha256_before"] for k in range(len(log["edits"]) - 1))
        R["K2"] = out == cand and chain and log["edits"][0]["doc_sha256_before"] == BASE_SHA and log["edits"][-1]["doc_sha256_after"] == sha(cand) == log["candidate_sha256"]
    except SystemExit:
        R["K2"] = False
    R["K3"] = all_triad_strings(cand) == all_triad_strings(base) and len(rid_set(cand)) == 46
    R["K4"] = anchors(cand) == anchors(base)
    R["K5"] = statuses(cand) == statuses(base)
    R["K6"] = appA(cand) == appA(base)
    L = live(cand)
    R["K7"] = not [p for p in STALE if p in L]
    R["K8"] = not [p for p in REQUIRED if p not in cand]
    if run_scripts:
        ok = True
        for f in ("triad_reconciliation_row1_extension_check.py", "triad_coowner_row1_row3_check.py"):
            p = subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, f)], capture_output=True, text=True)
            ok &= p.returncode == 0 and "RESULT: PASS" in p.stdout
        R["S1"] = ok
    try:
        R["S5"] = sign_table_ok(cand)[0]
    except Exception:
        R["S5"] = False
    R["S6"] = gram_ok()
    return R

CONTROLS = [  # (name, gate that must fail, mutation)
    ("drop C3", "K8", lambda t: t.replace("- **C3 — full evolution.**", "- **C3 — evolution.**")),
    ("restore send queue", "K7", lambda t: t.replace("**Consumer interface.**", "1. Send CN-01–CN-05 to Genesis/OPEN M. **Consumer interface.**")),
    ("rename an RID", "K3", lambda t: t.replace("TRIAD-OPEN-T6Q]", "TRIAD-OPEN-T6Q2]")),
    ("edit Appendix A", "K6", lambda t: t.replace("### v1.6 owner release — 5 October 2026", "### v1.6 owner release — 6 October 2026")),
    ("claim D constant in (a)", "K8", lambda t: t.replace("In extension (a), $\\dot D=r\\,q_1D$", "In extension (a), $\\dot D=0$")),
    ("wrong sigma in single flip", "S5", lambda t: t.replace("| $(s,c)\\mapsto(-s,c)$ | unchanged | negated | negated | $(-\\mu,-\\nu)$ | flips |",
                                                          "| $(s,c)\\mapsto(-s,c)$ | unchanged | negated | negated | $(-\\mu,-\\nu)$ | unchanged |")),
    ("wrong I under exchange", "S5", lambda t: t.replace("| $(s,c)\\mapsto(c,s)$ | exchanged | unchanged |", "| $(s,c)\\mapsto(c,s)$ | exchanged | negated |")),
    ("change a Status line", "K5", lambda t: t.replace("Status: ACTIVE after r4 correction", "Status: CLOSED after r4 correction")),
    ("drop an anchor", "K4", lambda t: t.replace(" {#sec-6-18-orientation-correction}", "")),
    ("reintroduce release-label qualifier", "K7", lambda t: t.replace("`[COR]` If the selected complete child functional", "`[COR v1.6.1 — D3]` If the selected complete child functional", 1)),
    ("claim custody package present", "K7", lambda t: t.replace("is held by the PI and is **not in the repository**", "is preserved under `evidence/accepted_r4_2/`")),
]

def main(argv):
    if len(argv) < 4: raise SystemExit(__doc__)
    base = open(argv[1], encoding="utf-8").read(); cand = open(argv[2], encoding="utf-8").read()
    log = json.load(open(argv[3], encoding="utf-8"))
    R = gates(base, cand, log)
    for k, v in R.items(): print(f"{k}: {'PASS' if v else 'FAIL'}")
    if not R["K7"]: print("  stale:", [p for p in STALE if p in live(cand)])
    if not R["K8"]: print("  missing:", [p for p in REQUIRED if p not in cand])
    if not R["S5"]: print("  S5:", sign_table_ok(cand)[1])
    ok = all(R.values())
    print(f"edits: {len(log['edits'])}; candidate sha256: {sha(cand)}; GATES: {'ALL PASS' if ok else 'FAIL'}")
    if "--controls" in argv:
        cok = True
        for name, gate, mut in CONTROLS:
            m = mut(cand)
            if m == cand: print(f"control '{name}': mutation did not apply -> FAIL"); cok = False; continue
            Rm = gates(base, m, log, run_scripts=False)
            hit = not Rm[gate]
            print(f"control '{name}': gate {gate} {'fails as required' if hit else 'DID NOT FAIL'}")
            cok &= hit
        print(f"CONTROLS: {'ALL CAUGHT' if cok else 'FAIL'}"); ok &= cok
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main(sys.argv)
