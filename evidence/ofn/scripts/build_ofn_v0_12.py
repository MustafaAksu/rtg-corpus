#!/usr/bin/env python3
r"""OFN v0.12 — content build (one stage; no layout compaction).

Input: the adopted v0.11 file (tag ofn-v0.11, SHA-256 38a2f444...e9e4).
Round 2 (30 Oct 2026): A01, A02, A03, B06, B07 and H12 revised for review findings R126-S1, R126-S2 and R126-N1
(records/ofn/OFN_v0_12_CHATGPT_REVIEW.md, PR #126 review 5711097535); the round-1 candidate 8230b169...3bae stays in Git history.
Fixed by: the three OFN co-owner working notes merged on main — records/ofn/OFN_ISOLATION_INTERFACE_WORKING_NOTE.md (PR #120),
OFN_REF_CLOSURE_WORKING_NOTE.md (PR #122), OFN_3B_INDEPENDENCE_WORKING_NOTE.md (PR #124), each ACCEPT SCOPED by the second
co-owner — and the PI start of 30 Oct 2026: "Başla, RID yarat, henüz seçim yapılmasın" (start; create the RID; no selection yet).

Groups:  A  record mathematical results (new RID RTG-OFN-ALG-REF-CLOSURE-COMPARISON in §2.4; class-C interface identity in
            the §5.5.4 formal-properties list; 3B evaluation frame with class C's position)
         B  OPEN scope revisions without status change (REF-CLOSURE narrowed to its physical reading; TRIAD-CLASS isolation
            frame I-comp / I-quiet / I-remove, none selected; 3A pointer; 3B frame, no standard selected)
         H  header, §0.1 boundary, §0.3 edition line, §12 registers, Appendix C entry, footer
Not done: no definition, Q1-Q6 or Standard C change; no OPEN status change; no physical selection; no 3B standard; no primacy.

Edit modes: str (old occurs exactly once) and after (insert text after the unique full line that starts with `old`).
Every edit is logged with old/new text, SHA-256 and the document hash chain.

usage: build_ofn_v0_12.py BASE OUT EDITLOG_JSON      BASE = `git show ofn-v0.11:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`
"""
import hashlib, json, sys

BASE_SHA = "38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4"
BR = "  "
E = []


def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def ed(i, grp, old, new, mode="str"): E.append((i, grp, mode, old, new))


# ------------------------------------------------------------------------------------------------- H header
ed("H01", "H", "# RTG_ONTOLOGICAL_FOUNDATIONS_v0.11\n", "# RTG_ONTOLOGICAL_FOUNDATIONS_v0.12\n")
ed("H02", "H", "**Document status:** ADOPTED — PI, 30 October 2026 (owner synchronization, smooth class-C realization and two §5.5 contract corrections; stage 1 and stage 2 reviewed). Release record: `records/ofn/OFN_v0_11_RELEASE_RECORD.md`." + BR,
   "**Document status:** DRAFT — v0.12 candidate (one content stage; no layout stage); adoption pending (`records/ofn/OFN_v0_12_RELEASE_RECORD.md`). `ofn-v0.11` remains the governing edition until adoption and tag." + BR)
ed("H03", "H", "**Supersedes:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10` (tag `ofn-v0.10`, SHA-256 `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`)." + BR,
   "**Supersedes:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.11` (tag `ofn-v0.11`, SHA-256 `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4`), on adoption." + BR)
ed("H04", "H", "the hypothesis FSP-U, four OFN local results and twenty-one foundational OPENs",
   "the hypothesis FSP-U, five OFN local results and twenty-one foundational OPENs")
ed("H05", "H", "and the admitted FMS mathematical test class is real $C^\\infty$ with analytic laws as a distinguished subclass." + BR,
   "and the admitted FMS mathematical test class is real $C^\\infty$ with analytic laws as a distinguished subclass. The closure-versus-reference comparison is recorded as the OFN local result `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`; its physical reading, the physical-isolation contract and the standard of triadic independence remain open." + BR)
ed("H06", "H", "**Governing inputs:** owner disposition records `records/ofn/OFN_OWNER_DISPOSITION_ADVISORY_v0_10_claude012ZC8x_20261029.md`, `…_chatgpt_20261029.md` and their joint reconciliation `records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md` (both co-owners confirmed, 29 October 2026); PI start, 29 October 2026." + BR,
   "**Governing inputs:** the OFN co-owner working notes `records/ofn/OFN_ISOLATION_INTERFACE_WORKING_NOTE.md`, `records/ofn/OFN_REF_CLOSURE_WORKING_NOTE.md` and `records/ofn/OFN_3B_INDEPENDENCE_WORKING_NOTE.md` with their receiving reviews (PRs #120, #122, #124; ACCEPT SCOPED); PI start, 30 October 2026 (one new local-result RID authorized; no isolation contract or independence standard selected)." + BR)
ed("H07", "H", "Evidence states follow Methodology v1.4 §12." + BR,
   "Evidence states follow Methodology v1.4 §12. OFN SESSION scripts for §2.4, §5.5.4 and §9 are under `evidence/ofn/scripts/` (§12.1)." + BR)

# ------------------------------------------------------------------------------------------------- H §0.1 / §0.3
ed("H08", "H", "**v0.11 revision boundary:** owner synchronization with the editions released after v0.10 (Dyadic smooth realization, RRF class-C row, TDR-G Finding A acceptance and RID map, NUMGEN L-BACKBONE, the RECOG v0.3.20 freeze record, Triadic v1.6.1), two recorded definition corrections in the §5.5 contract (Standard C, Appendix B OFN11-C01; test-class regularity, OFN11-C02), six RID registrations for existing definition bodies (§§1.3, 4.1, 4.6, 8), and Methodology v1.4 tag spellings. No OPEN status changes and no physical selection is made.",
   "**v0.12 revision boundary:** the three OFN co-owner working notes of 30 October 2026 enter the live text. The closure/reference comparison is registered as the OFN local result `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` (§2.4) and OPEN-OFN-REF-CLOSURE is narrowed to its physical reading. The class-C causal-interface identity is recorded (§5.5.4), and the physical-isolation obligation of OPEN-OFN-TRIAD-CLASS is split into the contracts I-comp, I-quiet and I-remove, none selected. OPEN-OFN-3B receives an evaluation frame (U-form, U-class, C0, C1, J) with the position of class C; no standard of independence is selected. No definition or OPEN status changes and no physical selection is made.")
ed("H09", "H", "*v0.11:* registers six further definition RIDs for unchanged bodies, corrects two §5.5 definitions by recorded `[COR]` (Appendix B) and adds no OPEN record.",
   "*v0.12:* registers one OFN local result (`RTG-OFN-ALG-REF-CLOSURE-COMPARISON`), changes no definition and adds no OPEN record.")

# ------------------------------------------------------------------------------------------------- A §2.4 REF-CLOSURE result
ed("A01", "A", "The equality of those constructions is not assumed; `RTG-OFN-OPEN-REF-CLOSURE` preserves the original question.",
   "The mathematical comparison is the local result below: the closure sector is canonically isomorphic to node assignments modulo the common origin ($Q_{\\rm node}\\cong C_0$), and the global comparison map with the use of one relation as reference is an isomorphism only on carriers where multiplication by 3 is bijective. Whether either is the physical reference consumption meant here is not decided; `RTG-OFN-OPEN-REF-CLOSURE` keeps that question.")
ed("A02", "A", "`[HYP]` **Reference-consumption reading.**",
   "\n\n`[RESULT]` `[from: ALG]` [RID: RTG-OFN-ALG-REF-CLOSURE-COMPARISON] [scope: abelian carrier group $H$; connected graph $G$ for (i); cycle graph $C_n$ with coherent orientation for (ii)–(iv); the maps as stated; OFN custody] **Closure versus reference removal.** "
   "Let $d:H^V\\to H^E$, $(ds)_{ij}=s_i-s_j$; $Q_{\\rm node}=H^V/H_{\\rm diag}$; $C_0\\subseteq H^E$ the closure sector (zero oriented sum around every cycle); $Q_{\\rm edge}=H^E/H^E_{\\rm diag}$ (edges measured relative to one another). "
   "(i) $d$ induces a canonical isomorphism $Q_{\\rm node}\\cong C_0$: the closure sector is canonically identified with node assignments modulo the common origin (the two constructions are isomorphic, not literally the same operation). "
   "(ii) Forgetting one edge is a bijection $C_0\\to H^{E\\setminus\\{e_0\\}}$, a lossless parametrization rather than a reduction; on all of $H^E$ it loses exactly the holonomy. "
   "(iii) The composite $\\kappa_n:C_0\\hookrightarrow H^E\\twoheadrightarrow Q_{\\rm edge}$ has $\\ker\\kappa_n\\cong H[n]$ and $\\operatorname{coker}\\kappa_n\\cong H/nH$, so it is an isomorphism iff multiplication by $n$ is bijective on $H$. For $K_3$: yes over $\\mathbb R^d$; no over $U(1)$ (globally 3-to-1, locally a diffeomorphism), over $\\mathbb Z_N$ with $3\\mid N$, or over $\\mathbb Z$. Edge-dependent isomorphisms $C_0\\cong Q_{\\rm edge}$ exist for every abelian $H$ and are a different comparison. "
   "(iv) The diagonal node action fixes every edge; the diagonal edge action by $c$ preserves $C_0$ iff $nc=0$. "
   "Equal cardinalities of $Q_{\\rm node}$, $C_0$ and $Q_{\\rm edge}$ do not decide (iii).\n"
   "Depends on: abelian-group algebra; (i)–(ii) are standard, (iii)–(iv) elementary and exact. Evidence: `evidence/ofn/scripts/ofn_ref_closure_check.py` (`4c469b41…0402`, checks R1–R5; EV-RUN by both co-owners, same CAS); working note `records/ofn/OFN_REF_CLOSURE_WORKING_NOTE.md`. Not covered: non-abelian carriers; graphs with cycles of different lengths or orientations for (iii)–(iv); a geometric $SO(d)$ reference, whose orbit dimension depends on the configuration; any physical reading of reference consumption, which stays with the `[HYP]` above and OPEN-OFN-REF-CLOSURE.",
   "after")

# ------------------------------------------------------------------------------------------------- A §5.5.4 interface identity
ed("A03", "A", "- **Six-step cubic.**",
   "\n- **Causal interface.** With $b_e=\\sum_{j\\ne e}N(z_j)$, exactly $F_e-N(z_e)=-\\tfrac{\\kappa}{3}\\bigl(N(z_e)+b_e\\bigr)$; no symmetry or truncation is used. For $\\kappa\\ne0$, $b_e$ is a one-step sufficient interface for edge $e$, minimal in the quotient sense, and the dyad law holds on edge $e$ iff $b_e=-N(z_e)$: on the lock surfaces the interface of every nonzero edge is active and compensating ($b_1=-N(z)$ on $\\mathcal S_0$, whose zero edge has $b_3=0$), while under zero total interface $b_e=0$ the edge obeys $(1-\\tfrac{\\kappa}{3})N$, not the dyad law. One-step sufficiency does not by itself give closed reduced dynamics (shown to fail for a diagnostic polynomial, not shown for C2). The interface vocabulary is that of `numgen-v1.21` §6.2 N-1A2; its closure is not imported. Evidence: `ofn_isolation_interface_check.py` (`17e91906…b8ef`); working note `records/ofn/OFN_ISOLATION_INTERFACE_WORKING_NOTE.md`.",
   "after")

# ------------------------------------------------------------------------------------------------- B §9 OPEN scopes
ed("B01", "B", "Question: Are edge-closure reduction and removal of one relational reference the same construction?" + BR,
   "Question: Which reference operation, if any, is the physical (rotational) reference consumption of the §2.4 `[HYP]`?" + BR)
ed("B02", "B", "Closure criterion: Define both spaces, equivalence relations and maps, then prove or disprove the claimed identification in a stated model; matching counts alone are insufficient." + BR,
   "Closure criterion: A stated physical reading of the reference, with its action (on nodes, on edges, or geometric) in a declared carrier and encoding, shown to coincide with one of the constructions compared in `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`, or with none. The mathematical comparison is settled at the scope of that result; matching counts alone remain insufficient." + BR)
ed("B03", "B", "Dependencies: §2.4; branch-local edge/mode conventions." + BR,
   "Dependencies: §2.4; `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`; branch-local carrier and edge/mode conventions." + BR)
ed("B04", "B", "Next required artifact or decision: An explicit comparison construction.",
   "Next required artifact or decision: A physical reading of the reference operation, and the carrier declaration of each branch that uses the counting argument.")
ed("B05", "B", "Next required artifact or decision: An explicit completeness/observability criterion.",
   "Next required artifact or decision: An explicit completeness/observability criterion. One operational ingredient is available: a sufficient causal interface (vocabulary of `numgen-v1.21` §6.2), which for class C separates recovery under a compensating interface from recovery under a quiet or removed environment (§5.5.4; OPEN-OFN-TRIAD-CLASS). Completeness is not thereby defined, and full edge autonomy everywhere would be a stronger demand than Q3a.")
ed("B06", "B", "Reconciliation input: class C (§5.5.4) has exact invariant lock surfaces on which every edge evolves by the transported isolated-dyad map.",
   "\n\nEvaluation frame (recorded; no standard selected). An independently specified $T_3$ is assessed on five axes: **U-form** (the recipe $G\\mapsto T_3[G]$ is fixed on a declared class of single-edge laws), **U-class** (that class uses no nonlinear $T$-data), **C0** (an embedding exists in the declared carrier without a $T$-derived rechart), **C1** (an embedding exists with $T$-derived structure) and **J** (the coupling form is justified without presupposing recovery of $T$). "
   "Class C: U-form passes — $T_3[G]=P_\\kappa\\circ G^{\\times3}$ intertwines $\\iota_0$ for every odd $G$ and $\\iota_\\pm$ for every $G$ with $G(0)=0$, $G(A^2x)=A^2G(x)$; U-class is $T$-free for $\\iota_0$ and relative to the linear data $\\omega=A^2$, $A=DT(0)$, for the chiral pair; C0 fails for the named raw mean-feedback family under Standard C by the owner no-go `RTG-OFN-ALG-RAW-STANDARD-C-NOGO` (smooth $C^3$ invariant manifold germs through 0, every $\\kappa\\ne0$; within its scope only, so other carriers and laws are not excluded); separately, the raw map is not odd, $T(-x)+T(x)=\\bigl(0,2(\\cosh\\rho-1)\\bigr)$, which by itself excludes only the named embedding $\\iota_0$ for the raw recipe; C1 passes, $T$-relative ($\\Phi$ is built from $J=T\\circ K_6^{-1}$); J is open. "
   "Which combination of axes the phrase \"independently motivated model class\" of §8 requires is not selected; candidate standards are (a) U-form, C1 and the reduction witness; (b) in addition U-class without nonlinear $T$-data and C0; (c) in addition J. Class C meets (a), meets (b) only in part, and (c) is not shown. Working note `records/ofn/OFN_3B_INDEPENDENCE_WORKING_NOTE.md`; evidence `ofn_3b_independence_check.py` (`139f7934…cc70`). No primacy conclusion follows.",
   "after")
ed("B07", "B", "Next required artifact or decision: the physical selection, isolation and chirality obligations above.",
   "\n\nIsolation frame (recorded; none selected). The class-C interface identity (§5.5.4) separates three contracts: **I-comp**, the dyad law on a balanced invariant regime with a compensating interface (active for every nonzero edge), which class C meets exactly; **I-quiet**, the dyad law under zero total interface, which class C fails for $\\kappa\\ne0$; and **I-remove**, the dyad law after the environment is removed from the model, which needs a declared size-indexed family of laws that class C does not supply (its normalization $\\kappa/3$ presupposes three edges). The exact I-comp witness satisfies Standard C, which is not equivalent to $I_e\\equiv0$. The next isolation artifact is a contract declaring the intervention class, the preserved observables, the retained boundary data and, for I-remove, the size-indexed law (working note `records/ofn/OFN_ISOLATION_INTERFACE_WORKING_NOTE.md`).",
   "after")

# ------------------------------------------------------------------------------------------------- H §12 registers
ed("H10", "H", "| Genesis v2.8.9; DYAD v6.4.13–v6.4.16; RRF v0.8.3 |",
   "\n| OFN co-owner working notes and scripts (30 Oct 2026) | `ofn_isolation_interface_check.py` (`17e91906…b8ef`), `ofn_ref_closure_check.py` (`4c469b41…0402`) and `ofn_3b_independence_check.py` (`139f7934…cc70`) under `evidence/ofn/scripts/`, each with positive and forced-failure outputs; notes and receiving reviews under `records/ofn/` | Evidence for §2.4, §5.5.4 and §9 (OPEN-OFN-3A, -3B, -TRIAD-CLASS, -REF-CLOSURE); EV-CODE, EV-RUN (rerun by the second co-owner, same CAS) |",
   "after")
ed("H11", "H", "| `RTG-OFN-DEF-ZERO-ORIGIN`, `RTG-OFN-DEF-DISCRETE-REDUCTION-BOUNDARY`,",
   "\n| `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` | v0.12 (adoption pending), OFN RESULT from ALG | Registered on adoption of v0.12 (five OFN local results in total) |",
   "after")

# ------------------------------------------------------------------------------------------------- H Appendix C and footer
ed("H12", "H", "### v0.11 — 30 October 2026 — ADOPTED / smooth class-C realization and owner synchronization release\n",
   "### v0.12 — 30 October 2026 — DRAFT (adoption pending)\n"
   "- **§2.4 / §9 [result/scope]:** `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` registered (closure sector canonically isomorphic to node data modulo the common origin, $Q_{\\rm node}\\cong C_0$; the global comparison with one relation as reference is an isomorphism iff multiplication by $n$ is bijective; node and edge actions differ); OPEN-OFN-REF-CLOSURE narrowed to the physical reading.\n"
   "- **§5.5.4 / §9 [isolation]:** class-C causal-interface identity recorded; OPEN-OFN-TRIAD-CLASS isolation obligation split into I-comp, I-quiet and I-remove (none selected); OPEN-OFN-3A pointer.\n"
   "- **§9 [3B]:** evaluation frame U-form, U-class, C0, C1, J with the position of class C; no standard of independence selected.\n"
   "- **Unchanged:** definitions, Q1–Q6, Standard C and OPEN statuses (twenty ACTIVE, one PARTIAL); no physical selection; no primacy conclusion.\n"
   "- **Record:** `records/ofn/OFN_v0_12_RELEASE_RECORD.md`; predecessor tag `ofn-v0.11`.\n\n"
   "### v0.11 — 30 October 2026 — ADOPTED / smooth class-C realization and owner synchronization release\n")
ed("H13", "H", "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.11*",
   "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.12 — DRAFT, adoption pending; `ofn-v0.11` governs until adoption and tag.*")


def apply(base):
    s, log = base, []
    for (i, grp, mode, old, new) in E:
        before = s
        if mode == "str":
            n = s.count(old)
            if n != 1: raise SystemExit(f"{i}: expected 1 occurrence, found {n}: {old[:90]!r}")
            s = s.replace(old, new)
            o, nw = old, new
        elif mode == "after":
            lines = s.split("\n")
            idx = [k for k, l in enumerate(lines) if l.startswith(old)]
            if len(idx) != 1: raise SystemExit(f"{i}: expected 1 line starting with {old[:60]!r}, found {len(idx)}")
            line = lines[idx[0]]
            o = line; nw = line + new
            lines[idx[0]] = nw
            s = "\n".join(lines)
        log.append({"id": i, "group": grp, "mode": mode, "old": o, "new": nw, "old_sha256": sha(o), "new_sha256": sha(nw),
                    "doc_sha256_before": sha(before), "doc_sha256_after": sha(s)})
    return s, log


def main(argv):
    if len(argv) != 4: raise SystemExit(__doc__)
    base = open(argv[1], "rb").read()
    if hashlib.sha256(base).hexdigest() != BASE_SHA: raise SystemExit("input is not the adopted ofn-v0.11 file")
    out, log = apply(base.decode("utf-8"))
    open(argv[2], "w", encoding="utf-8", newline="\n").write(out)
    json.dump({"base_sha256": BASE_SHA, "candidate_sha256": sha(out), "edits": log}, open(argv[3], "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"edits: {len(log)}; candidate sha256: {sha(out)}; lines: {out.count(chr(10))}")


if __name__ == "__main__":
    main(sys.argv)
