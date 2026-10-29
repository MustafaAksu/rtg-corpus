#!/usr/bin/env python3
r"""OFN v0.11 — stage-1 build (content and contract corrections; no layout change).

Input: the adopted v0.10 file (tag ofn-v0.10, SHA-256 acb70a8c...5dfa).
Fixed by: the two owner disposition records (PR #108 claude012ZC8x, PR #109 chatgpt), the joint reconciliation
records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md (PR #110, both co-owners confirmed) and the PI's
"başla" of 29 Oct 2026. Rows are the 29 rows of records/ofn/ATLAS_ADVISORY_OFN_v0_10_RECONCILIATION.md §3.

Stage 1 carries every semantic change: the class-C realization (row 1), the test-class amendment (row 2), the Standard C
[COR] (row 3), receipts and repins (rows 4-20, 23, 25, 27-28), six DEF RID registrations and two OPEN pointers (row 22),
the canonical tag spellings and the narrow-Q6 status (row 21, content part) and the Appendix B / C records. Stage 2 is
layout only (current-only removal of history, Appendix C compaction) and is built by a separate script against the
frozen stage-1 hash.

Round 2 (29 Oct 2026): R16i, R21l, R21m and R03e apply the bounded current-state corrections R112-C1, R112-C2 and the
clarification R112-N1 of the co-owner review records/ofn/OFN_v0_11_CHATGPT_REVIEW.md (PR #112). The round-1
intermediate (cf38b61b...7ce3, commit 762d273) stays in Git history.

Edit modes:
  str   : `old` occurs exactly once in the whole document; replaced by `new`;
  live  : `old` occurs exactly `count` times in the live region (before the §12 anchor); all are replaced;
  block : the text between two unique markers (start inclusive, end exclusive) is replaced by `new`.
Every edit is logged with old/new text and SHA-256. Token ⟨BR⟩ in an edit text stands for the two-space Markdown
line break at end of line.

usage: build_ofn_v0_11_stage1.py BASE OUT EDITLOG_JSON
  BASE = `git show ofn-v0.10:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`
"""
import hashlib, json, sys

BASE_SHA = "acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa"
LIVE_END = '<a id="ofn-artifacts-provenance"></a>'
BR = "⟨BR⟩"

def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def br(t): return None if t is None else t.replace(BR, "  ")

E = []  # (id, row, mode, old, new, count)
def ed(i, row, old, new, mode="str", count=1): E.append((i, row, mode, br(old), br(new), count))

# ----------------------------------------------------------------------------------------------- globals (live region)
ed("G01", "9/23", "RTG_DISCRETE_GENESIS_DSN_v2.12.13", "RTG_DISCRETE_GENESIS_DSN_v2.12.14", "live", 23)
ed("G02", "9/23", "TDR-G v2.12.13", "TDR-G v2.12.14", "live", 4)
ed("G03", "14/23", "RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20", "RTG_RELATIONAL_RECOGNITION_DSN_v0.3.26", "live", 13)
ed("G04", "14/23", "RECOG v0.3.20", "RECOG v0.3.26", "live", 7)
ed("G05", "23", "RTG_GENESIS_GEOMETRY_DSN_v2.8.5", "RTG_GENESIS_GEOMETRY_DSN_v2.9", "live", 7)
ed("G06", "16/23", "RTG_DYADIC_OSCILLATOR_DSN_v6.4.10", "RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", "live", 3)
ed("G07", "12/23", "NUMGEN v1.20.7", "NUMGEN v1.21", "live", 7)
ed("G08", "20", "Triadic v1.6 ", "Triadic v1.6.1 ", "live", 5)
ed("G09", "23", "RRF v0.7 ", "RRF v0.8.4 ", "live", 4)
ed("G10", "5/23", "RRF v0.8.3", "RRF v0.8.4", "live", 4)
ed("G11", "23", "Programme v1.2", "Programme v1.3", "live", 4)

# ----------------------------------------------------------------------------------------------- header (rows 21-content, 23)
HDR = r"""# RTG_ONTOLOGICAL_FOUNDATIONS_v0.11

**Title:** Relational Time Geometry — Ontological Foundations and Model-Selection Layer⟨BR⟩
**Date:** 29 October 2026⟨BR⟩
**Scope:** Foundational commitments, primitive-object hypotheses and model-selection criteria of RTG, including the genuine relational-triad model-selection contract for the FMS interface (§5.5); no physical generator, carrier or primitive object is selected.⟨BR⟩
**Document class:** Foundational ontology / model-selection ledger (Methodology v1.4 §0.5); nonstandard profile with the section map in §0.4.⟨BR⟩
**Document status:** DRAFT — stage-1 intermediate of v0.11; adoption pending (`records/ofn/OFN_v0_11_RELEASE_RECORD.md`). `ofn-v0.10` remains the governing edition until adoption and tag.⟨BR⟩
**Supersedes:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10` (tag `ofn-v0.10`, SHA-256 `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`), on adoption.⟨BR⟩
**Companion documents:** governing editions read for this edition — Programme Overview v1.3 (`programme-v1.3`), DSN Methodology v1.4 (`methodology-v1.4`), Dyadic Oscillator v6.4.22 (`dyad-v6.4.22`), Genesis Geometry v2.9 (`gen-v2.9`), RRF v0.8.4 (`rrf-v0.8.4`), Discrete Genesis v2.12.14 (`tdrg-v2.12.14`), Number Genesis v1.21 (`numgen-v1.21`), RECOG v0.3.26 (`recog-v0.3.26`), Triadic v1.6.1 (`triad-v1.6.1`); claim-level pins are stated at each use and in §11.⟨BR⟩
**DSN Methodology:** v1.4 (tag `methodology-v1.4`).⟨BR⟩
**Status summary:** OFN holds seventeen registered definitions, the hypothesis FSP-U, four OFN local results and twenty-one foundational OPENs (twenty ACTIVE, one PARTIAL); no physical generator, carrier, primitive object, chirality or isolation regime is selected. In the genuine relational-triad contract the transported class C is the primary realized smooth mathematical candidate family: a real $C^\infty$ realization exists through two imported Dyadic theorems, while analytic realization (DYAD B-an/B-6) and physical selection remain open. Standard C is a positive-dimensional local $C^3$ invariant-manifold test, and the admitted FMS mathematical test class is real $C^\infty$ with analytic laws as a distinguished subclass.⟨BR⟩
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok — inherited attribution; separate approval by every listed contributor is not inferred.⟨BR⟩
**Revision editor:** Claude (OFN co-owner session `claude012ZC8x`, builder); change-focused review by the second OFN co-owner (ChatGPT).⟨BR⟩
**Programme document / placement:** Programme Overview v1.3; Tier 2, namespace `RTG-OFN`; criteria home for OPEN-P0 and OPEN-P2B (Programme v1.3 §5).⟨BR⟩
**Governing inputs:** owner disposition records `records/ofn/OFN_OWNER_DISPOSITION_ADVISORY_v0_10_claude012ZC8x_20261029.md`, `…_chatgpt_20261029.md` and their joint reconciliation `records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md` (both co-owners confirmed, 29 October 2026); PI start, 29 October 2026.⟨BR⟩
**Evidence boundary:** owner statements were read at the governing tags named above; no owner certificate is rerun. FMS SESSION results are reference-only (RF-O10-02); the universal finite-$a$ statement keeps its FMS P4 qualification. Evidence states follow Methodology v1.4 §12.⟨BR⟩

"""
ed("H01", "21/23", None, HDR, "block")

ed("H02", "21", "Methodology v1.3 governs live tags. `[DEF-axiom]` is replaced by `[DEF]` with explicit adoption and scope; adopted does not mean underived forever.",
   "Methodology v1.4 (§8) governs live tags; qualifiers follow v1.4 §3.2 (`[scope:]`, `[assuming:]`, `[provenance:]`), and compound dash spellings are not used in live claims. `[DEF-axiom]` is replaced by `[DEF]` with explicit adoption and scope; adopted does not mean underived forever.")

# ----------------------------------------------------------------------------------------------- §0 (rows 7, 26, 21)
ed("S01", "21", "**v0.10 Draft 1 revision boundary:** this draft is the separate definition proposal anticipated above, limited to the FMS model-selection interface. It adds §5.5 and its imports, references and one proposed OPEN record. It does not change any v0.9 definition body, FSP-U, the two registered local consequences, any guard, or any of the twenty OPEN statuses. The new contract binds a *named model class* (the genuine interacting relational triad) and is not a universal axiom, a primacy verdict or a physical selection (SG-OFN-SELECTION, SG-OFN-PRIMACY).",
   "**v0.11 revision boundary:** owner synchronization with the editions released after v0.10 (Dyadic smooth realization, RRF class-C row, TDR-G Finding A acceptance and RID map, NUMGEN L-BACKBONE, the RECOG v0.3.20 freeze record, Triadic v1.6.1), two recorded definition corrections in the §5.5 contract (Standard C, Appendix B OFN11-C01; test-class regularity, OFN11-C02), six RID registrations for existing definition bodies (§§1.3, 4.1, 4.6, 8), and Methodology v1.4 tag spellings. No OPEN status changes and no physical selection is made. The §5.5 contract binds a *named model class* and is not a universal axiom, a primacy verdict or a physical selection (SG-OFN-SELECTION, SG-OFN-PRIMACY).")
ed("S02", "21", " Until then v0.9 governs, and the v0.8.2 handoff remains a co-owner-accepted working record.",
   "\n\n*v0.11 (adoption pending):* registers six further definition RIDs for unchanged bodies, corrects two §5.5 definitions by recorded `[COR]` (Appendix B) and adds no OPEN record.")
ed("S03", "7", "Finding A is offered for TDRG custody under XFER-O08-01, not silently registered in the TDRG namespace.",
   "Finding A's statement is accepted and used by TDR-G (`tdrg-v2.12.14` §7, SG-14); its custody transfer XFER-O08-01 is deferred by TDR-G to v2.13, so the RID remains OFN's and is not registered in the TDRG namespace.")
ed("S04", "26", "Orientation core: §1, §§0.5/4.5/4.6, §5.2 and §9. This nonstandard profile uses explicit anchors rather than the technical §1–§4 marker; inherited anchors are retained.",
   "Orientation core: §1, §§0.5/4.5/4.6, §5.2 and §9. This nonstandard profile uses explicit anchors rather than the technical §1–§4 marker; inherited anchors are retained. Appendix map to Methodology v1.4 §1: OFN Appendix C is the version history (v1.4 Appendix A), Appendix B the retired and rejected claims (v1.4 Appendix B), and Appendix A the preserved historical scenarios (profile-specific).")
ed("S05", "23", "Programme SG-PROG-1–4 apply in their adopted v1.2 form (§8), with Methodology v1.3 §§3.3–3.4.",
   "Programme SG-PROG-1–4 apply in their adopted v1.3 form (Programme v1.3 §8), with Methodology v1.4 §§3.3–3.4.")

# ----------------------------------------------------------------------------------------------- row 22: DEF RIDs (bodies unchanged)
ed("R22a", "22", "`[DEF]` **Zero-origin.** $\\mathcal O_0=0$", "`[DEF]` [RID: RTG-OFN-DEF-ZERO-ORIGIN] **Zero-origin.** $\\mathcal O_0=0$")
ed("R22b", "22", "`[DEF]` **Discrete reduction boundary.**", "`[DEF]` [RID: RTG-OFN-DEF-DISCRETE-REDUCTION-BOUNDARY] **Discrete reduction boundary.**")
ed("R22c", "22", "`[DEF]` **Continuous representation.**", "`[DEF]` [RID: RTG-OFN-DEF-CONTINUOUS-REPRESENTATION] **Continuous representation.**")
ed("R22d", "22", "`[DEF]` **Finite description and finite domain.**", "`[DEF]` [RID: RTG-OFN-DEF-FINITE-DESCRIPTION] **Finite description and finite domain.**")
ed("R22e", "22", "`[DEF]` **OFN-DIST-ZN.**", "`[DEF]` [RID: RTG-OFN-DEF-DIST-ZN] **OFN-DIST-ZN.**")
ed("R22f", "22", "`[DEF]` **Reduction target, not established construction.**", "`[DEF]` [RID: RTG-OFN-DEF-REDUCTION-TARGET] **Reduction target, not established construction.**")
ed("R22g", "22", "Whether a broader physical closure or nonintegrable connection is selected is still open; no discrete-to-continuous dynamical identification follows from the common telescoping form.",
   "Whether a broader physical closure or nonintegrable connection is selected is still open; no discrete-to-continuous dynamical identification follows from the common telescoping form. Registry home: OPEN-OFN-FRUSTRATION and OPEN-OFN-HOLONOMY-RANK (§9).")
ed("R22h", "22", "it does not by itself select exact conservation for the physical theory.",
   "it does not by itself select exact conservation for the physical theory. Registry home: OPEN-OFN-IQP (§9).")

# ----------------------------------------------------------------------------------------------- TDR-G inline imports (row 9)
ed("R09a", "9", "§6.2 #sec-6-2-holonomy | RID unavailable] For node-difference phases, $\\Delta_{AB}+\\Delta_{BC}+\\Delta_{CA}\\equiv0\\pmod N$. This is a flat closure identity, not a nonintegrable-curvature signal.\nOwner RID: unavailable; request IMP-O08-04.⟨BR⟩",
   "§6.2 #sec-6-2-holonomy | TDRG-THM-HOLONOMY] For node-difference phases, $\\Delta_{AB}+\\Delta_{BC}+\\Delta_{CA}\\equiv0\\pmod N$. This is a flat closure identity, not a nonintegrable-curvature signal.\nOwner RID: TDRG-THM-HOLONOMY (TDR-G §7 owner RID map); administrative entry IMP-O08-04.⟨BR⟩")
ed("R09b", "9", "§6.1 #sec-6-1-state | RID unavailable] TDR-G uses even $N$ and the defect band $\\mathcal D_k=\\{\\Delta:\\operatorname{dist}_{C_N}(\\Delta,N/2)\\le k\\}$.\nOwner RID: unavailable; request IMP-O08-03.⟨BR⟩",
   "§6.1 #sec-6-1-state | TDRG-DEF-BAND] TDR-G uses even $N$ and the defect band $\\mathcal D_k=\\{\\Delta:\\operatorname{dist}_{C_N}(\\Delta,N/2)\\le k\\}$.\nOwner RID: TDRG-DEF-BAND (TDR-G §7 owner RID map); administrative entry IMP-O08-03.⟨BR⟩")
ed("R09c", "9", "§6.5 #sec-6-5-twonode | LEM-NOANNIHIL] In the discrete free-dyad model,", "§6.5 #sec-6-5-twonode | TDRG-ALG-LEM-NOANNIHIL] In the discrete free-dyad model,")
ed("R09d", "9", "§6.3 #sec-6-3-interaction | RID unavailable] The star rule creates a node at the center's antipodal shadow with the stated copied token, and inverts the center token.\nOwner RID: unavailable; request IMP-O08-09.⟨BR⟩",
   "§6.3 #sec-6-3-interaction | TDRG-DEF-STAR] The star rule creates a node at the center's antipodal shadow with the stated copied token, and inverts the center token.\nOwner RID: TDRG-DEF-STAR (TDR-G §7 owner RID map); administrative entry IMP-O08-09.⟨BR⟩")
ed("R09e", "9", "§6.1 #sec-6-1-state | RID unavailable] TDR-G stores $X=(\\theta_1,\\ldots,\\theta_M,\\delta_1,\\ldots,\\delta_M)$, with phases and tokens in $\\mathbb Z_N$, and declares global phase shifts $\\theta_i\\mapsto\\theta_i+c$ as gauge; relative advances are $d_{ij}=\\delta_i-\\delta_j$.\nOwner RID: unavailable; request IMP-O08-02.⟨BR⟩",
   "§6.1 #sec-6-1-state | TDRG-DEF-ZN-STATE; TDRG-DEF-PHYSICAL-STATE; TDRG-DEF-REL-ADVANCE] TDR-G stores $X=(\\theta_1,\\ldots,\\theta_M,\\delta_1,\\ldots,\\delta_M)$, with phases and tokens in $\\mathbb Z_N$, and declares global phase shifts $\\theta_i\\mapsto\\theta_i+c$ as gauge; relative advances are $d_{ij}=\\delta_i-\\delta_j$.\nOwner RIDs: TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE, TDRG-DEF-REL-ADVANCE (TDR-G §7 owner RID map); administrative entry IMP-O08-02.⟨BR⟩")
ed("R09f", "9", "§6.2 #sec-6-2-holonomy | RID unavailable] A specified deterministic update on the fixed-cap finite state set is eventually periodic.\nOwner RID: unavailable; request IMP-O08-08.⟨BR⟩",
   "§6.2 #sec-6-2-holonomy | TDRG-THM-RECURRENCE] A specified deterministic update on the fixed-cap finite state set is eventually periodic.\nOwner RID: TDRG-THM-RECURRENCE (TDR-G §7 owner RID map); administrative entry IMP-O08-08.⟨BR⟩")
ed("R09g", "9", "§6.5 #sec-6-5-twonode | LEM-REACH] A free dyad orbit", "§6.5 #sec-6-5-twonode | TDRG-ALG-LEM-REACH] A free dyad orbit")
ed("R09h", "9", "§6.3 #sec-6-3-interaction | CONV-TICK] The update order", "§6.3 #sec-6-3-interaction | TDRG-DEF-CONV-TICK] The update order")
ed("R09i", "8/9", "§6.3 #sec-6-3-interaction | CONV-P3CYC] The oriented path uses successor-token shift.\nDepends on: a valid path orientation selected under the source rule. Naming the shift does not certify that the orientation selection is presentation-independent. See IMP-O08-15 and RF-O08-01.",
   "§6.3 #sec-6-3-interaction | TDRG-DEF-CONV-P3CYC] The oriented path uses successor-token shift.\nDepends on: a valid path orientation under `TDRG-DEF-ORIENT` (balanced path-tie on $S=0\\wedge2E\\equiv0$, `tdrg-v2.12.14` §6.3). On the canonical branch `bound_symmetric` the owner states relabelling covariance under SG-14 ($\\mathrm{Sym}(V)\\times\\mathbb Z_N^{\\rm phase}$, modulo newborn relabelling), supported by a finite equivariance check at $N=24$; other policy branches only once their covariance is separately established, and `largest_center`'s ID tie-break is a recorded exception (`TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK`). See IMP-O08-15 and RF-O08-01.")
ed("R09j", "9/10", "§6.5 #sec-6-5-twonode | LEM-RETRIG] Under the isolated-dyad snapshot semantics,", "§6.5 #sec-6-5-twonode | TDRG-ALG-LEM-RETRIG] Under the isolated-dyad snapshot semantics,")
ed("R09k", "10", "The resulting displayed alternation has period dividing two; $d=0$ is the fixed-state case. See IMP-O08-07 and OFN08-C12.",
   "The resulting displayed alternation has period dividing two; $d=0$ is the fixed-state case, as the owner now also states (OFN08-C12 fulfilled at `tdrg-v2.12.14`). See IMP-O08-07.")
ed("R09l", "9", "§6.2 #sec-6-2-holonomy | RID unavailable] For $k<N/6$, a triangle cannot have all three pairs defect-related.\nOwner RID: unavailable; request IMP-O08-04B.⟨BR⟩",
   "§6.2 #sec-6-2-holonomy | TDRG-THM-NARROW-BAND-EXCLUSION] For $k<N/6$, a triangle cannot have all three pairs defect-related.\nOwner RID: TDRG-THM-NARROW-BAND-EXCLUSION (TDR-G §7 owner RID map); administrative entry IMP-O08-04B.⟨BR⟩")

# ----------------------------------------------------------------------------------------------- Finding A (row 7)
ed("R07a", "7", "[scope: fixed local component maps; OFN custody; transfer proposed] **Finding A — common-token shifts.**",
   "[scope: fixed local component maps; OFN custody; statement accepted by TDR-G, custody transfer deferred] **Finding A — common-token shifts.**")
ed("R07b", "7", "Provenance and checks: `REVIEW_FINDINGS.md`. Proposed consumer/custody transfer: TDRG, XFER-O08-01; §12.3 and RF-O08-01. No TDRG custody acceptance is implied.",
   "Provenance and checks: `REVIEW_FINDINGS.md`. Receiver state: TDR-G accepts the statement and uses it in SG-14 (`tdrg-v2.12.14` §7: checked as one-line algebra on `TDRG-DEF-STAR` and against the engine, `EV-CODE`); the custody transfer XFER-O08-01 is deferred by TDR-G to v2.13 and the RID remains OFN's (§12.3, RF-O08-01).")
ed("R07c", "7", "OFN offers the identified local consequence to the TDR-G owner under XFER-O08-01 and asks it to resolve the affine token origin: retain it as explicit physical structure with relational meaning, or provide a covariant relational inversion. Covariance alone does not declare the residual symmetry to be gauge. No TDRG rule or custody transfer is enacted here; the transfer proposal is in `OFN_TDRG_FINDING_A_HANDOFF.md`.",
   "TDR-G now records that the common token shift lies outside its covariance group and is a symmetry of the birth-free sector only, not a gauge (SG-14). Covariance alone does not declare the residual symmetry to be gauge. No TDRG rule or custody transfer is enacted here; the transfer proposal is in `OFN_TDRG_FINDING_A_HANDOFF.md` and stays open until TDR-G v2.13 decides.")

# ----------------------------------------------------------------------------------------------- §4.2, §6.3 primitive map (row 16)
ed("R16a", "16", "as recorded in Programme v1.3 OPEN-P0 and Dyadic v6.4.10 §6.1. Its source definition and conventions are IMP-O08-12; adopting it is not deriving it. Primitive-map RID custody remains unresolved (CUST-O09-01).",
   "as recorded in Programme v1.3 OPEN-P0 and Dyadic v6.4.22 §6.1 (`DYAD-DEF-PRIMITIVE-MAP`; Genesis `GEN-DEF-PRIMITIVE-MAP` is its recognized alias). Its source definition and conventions are IMP-O08-12; adopting it is not deriving it. CUST-O09-01 is answered (§12.3).")
ed("R16b", "16", "See IMP-O08-13; the primitive-map RID custody issue is distinct (CUST-O09-01).", "See IMP-O08-13; the primitive-map identity is `DYAD-DEF-PRIMITIVE-MAP` (IMP-O08-12).")

# ----------------------------------------------------------------------------------------------- §6.2a RECOG scope (row 14)
ed("R14a", "14", "[scope: diagnostic power-character family; source statement inspected; release qualification in §12.1]",
   "[scope: diagnostic power-character family] [provenance: source-read at `recog-v0.3.26`]")

# ----------------------------------------------------------------------------------------------- §5.5.1-§5.5.2 (rows 2, 3, 18)
ed("R02a", "2", "| Regularity | Real-analytic laws form the admitted continuous FMS test class; this is not a universal requirement. |",
   "| Regularity | The admitted local continuous FMS mathematical test class consists of real $C^\\infty$ update germs. Real-analytic laws form a distinguished subclass. Every candidate states its realized regularity; formal series remain formal candidates, not realized laws. This is a scoped model-testing convention, not a universal physical regularity axiom. $C^3$ remains the comparison/factor regularity of Q6 (Q6-REG) and the minimum manifold regularity of the Standard C test. (Amended in v0.11; OFN11-C02.) |")
ed("R03a", "3", "Boundary-conditioned isolated-dyad recovery (Standard C) is the minimum target, with an explicitly defined, physically admissible, nonempty and dynamically consistent isolation regime.",
   "Boundary-conditioned isolated-dyad recovery (Standard C, in its corrected local form) is the minimum target, with an explicitly defined, physically admissible and dynamically consistent isolation regime.")
ed("R18a", "18", "i.e. a declared extra variable (route C-a). The two-factor-plus-slaved-edge construction is a mathematical witness only. | — |",
   "i.e. a declared extra variable (route C-a). Declaring the role is necessary to avoid hiding it, not sufficient for full-state covariance; its representation gate is RRF-CND-01 Identity/Action (`rrf-v0.8.4` §6.2), without identifying slot symmetry with node exchange. The two-factor-plus-slaved-edge construction is a mathematical witness only. | — |")
ed("R03b", "3", "**Standard C at cubic order.** Write the update as $F_e(X)=T(r_e)+I_e(X)$. Standard C holds if there is a nonempty $F$-invariant regime $\\mathcal R$ on which $I_e=O(|r|^4)$ for every edge $e$, i.e. the isolated dyad is recovered through the order carrying $\\mu$ and the six-step return. Recovery at linear order alone does not count.",
   "**Standard C at cubic order.** Write the update as $F_e(r)=T(r_e)+I_e(r)$. Standard C at cubic order requires a positive-dimensional embedded $C^3$ manifold germ $M$ through the null state, invariant under the declared update as a germ, and supporting nonzero dyadic edge states arbitrarily close to the null state. On one common punctured local domain in $M$, every edge obeys $F_e(r)=T(r_e)+I_e(r)$, with constants $C$ and $\\varepsilon$ such that $\\lVert I_e(r)\\rVert\\le C\\lVert r\\rVert^4$ for all edges and all $r\\in M$ with $0<\\lVert r\\rVert<\\varepsilon$. The carrier, edge readout, norm (the complete local network-state norm) and primitive clock are declared. A singleton, a finite null-state record, or an isolated trajectory is not this local smooth isolation regime. Not all edges need be nonzero, so the coincidence embedding is admitted. The isolated dyad is thereby recovered through the order carrying $\\mu$ and the six-step return; recovery at linear order alone does not count. (Corrected in v0.11; old wording and reason in Appendix B, OFN11-C01.)")

# ----------------------------------------------------------------------------------------------- §5.5.3 (rows 1, 21-content)
ed("R01a", "1", "`[RESULT]` `[from: THM + ALG]` [RID: RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT]",
   "`[RESULT]` `[from: ALG]` [RID: RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT]")
ed("R01b", "1", "instance C2, $\\mathcal F_{\\kappa,\\Phi}$ conditionally on a real $C^3$ chart $\\Phi$ with $\\Phi T\\Phi^{-1}$ commuting with $A$, whose existence is not asserted)",
   "instance C2, the exactly transported $\\mathcal F_{\\kappa,\\Phi}$ in the real $C^\\infty$, hence $C^3$, chart $\\Phi$ of `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`, IMP-O10-07)")
ed("R01c", "1", "Depends on: IMP-O10-01/02 at their stated scope. The six-step theorems are used;",
   "Depends on: IMP-O10-01/02 at their stated scope (the Genesis `[THM]` premises; the OFN step is exact spectral algebra, hence the single conclusion status `[from: ALG]`, Methodology v1.4 §3.4) and, for C2, IMP-O10-07. The six-step theorems are used;")
ed("R01d", "1", "it does not distinguish class C from its third-jet equivalents (G-SEL) and asserts no realization of $J$.",
   "it does not distinguish class C from its third-jet equivalents (G-SEL) and asserts no analytic or physical realization.")

# ----------------------------------------------------------------------------------------------- §5.5.4 (rows 1, 5, 6, 19, 21)
ed("R01e", "1/6", "| Regularity | Formal; real $C^3$ for the polynomial representatives. Analytic or $C^\\infty$ realization is conditional on DYAD OPEN 20 (B-6 / B-∞ existence). |",
   "| Regularity | One table, used at every site of §5.5: |\n|  | **All-order formal family** — formal algebra and lock geometry retained; a formal series is not a real germ or a basin theorem. |\n|  | **Real polynomial instance C1** — exists independently of smooth $J$; Q6 by narrow-Q6 (ii). \"C1\" is the Genesis instance label, not differentiability; a polynomial proxy is not the exact transported dyad. |\n|  | **Exactly transported $C^\\infty$ instance C2**, $\\mathcal F_{\\kappa,\\Phi}=(\\Phi^{-1})^{\\times3}\\circ P_\\kappa\\circ N_\\Phi^{\\times3}\\circ\\Phi^{\\times3}$ — exists and is used (IMP-O10-06/07): local $C^\\infty$, hence $C^3$; qualitative radius; no finite-chart bounds (SG-19); chart-family freedom remains. |\n|  | **Exactly transported analytic realization** — OPEN (DYAD OPEN 20, B-an/B-6). |\n|  | **Physical realization or selection** — OPEN: no carrier, exchange, isolation mechanism, chirality dictionary or modulus value (OPEN-OFN-TRIAD-CLASS). |")
ed("R06a", "6", "| κ range | Formal properties for $\\kappa\\notin\\{0,1,2\\}$; stability statements only for $0<\\kappa<2$, $\\kappa\\ne1$. At $\\kappa=2$ the closure multiplier lies on the unit circle and the centre-manifold reduction does not apply; this is not a Q6 failure. |",
   "| κ values | The single κ table of §5.5 (other sites point here): **κ = 0** — decoupled reference (raw B), excluded from the coupled class by Q6. **κ = 1** — flat: raw A1 fails Q4; class C is flat; narrow-Q6 (i) holds via `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`; this is not a failed coupling theorem. **κ = 2** — the closure multiplier $(1-\\kappa)\\lambda=-\\lambda$ lies on the unit circle; the hyperbolic centre-manifold reduction does not apply; not a proved Q6 failure (Genesis γ ∈ {0,2} OPEN). **0 < κ < 2, κ ≠ 1** — linear attraction of the closure (mean) mode with modulus $\\lvert1-\\kappa\\rvert$, the range of the stability statements; not a basin theorem. **κ ∉ {0, 1, 2}** — the formal class-C contract. The lock identities themselves do not \"fail\" at exceptional κ merely because a factor theorem excludes those values. γ ≡ κ is the declared parameter convention of Genesis §6.3c and RRF §6.2a, not a raw/transported model identity. |")
ed("R05a", "5", "| Registration | OFN requests RRF to register class C as a *model-contract row*, not a new native profile, while OPEN-B/E1 stays locked. The decision is RRF's. |",
   "| Registration | Registered by RRF as a reference-only *model-contract row*, not a native profile (`rrf-v0.8.4` §6.2a, importing `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT`), with a representation-level ψ-readout entry; OPEN-B/E1 stays locked (RF-O10-01). |")
ed("R01f", "1/21", "Formal properties `[ALG — formal; OFN co-owner SESSION, recorded, not registered]`:",
   "Formal properties `[ALG]` [scope: formal family; for $\\mathcal F_{\\kappa,\\Phi}$ real $C^\\infty$] [provenance: OFN co-owner SESSION computation, recorded, not registered]:")
ed("R01g", "1", "In raw coordinates they are generated by the canonical $J=T\\circ F^{-1/6}$ ($R_0=J^3$, $G=J^2$), whose formal uniqueness is owner-grade (IMP-O10-03).",
   "In raw coordinates they are generated by the canonical $J=T\\circ F^{-1/6}$ ($R_0=J^3$, $G=J^2$), whose formal uniqueness is owner-grade (IMP-O10-03) and which exists as a real $C^\\infty$ germ (IMP-O10-06). For the $C^\\infty$ member: $[N_\\Phi,A]=0$ with $A^3=-I$ and $A^2=\\omega$ makes $N_\\Phi$ odd and $\\omega$-equivariant, so the same two-line computation shows that its lock surfaces are real $C^\\infty$ invariant submanifolds with exact isolated-dyad evolution on them `[ALG]` (Depends on: IMP-O10-06/07; an application of the imported chart, not a new Dyadic existence proof).")
ed("R01h", "1", "- **Realization.** A real carrier for the whole class follows from one object, an identity-tangent sixth root of $F=T^6$ (equivalently a real $J$), via Bochner averaging $\\Phi=\\tfrac16\\sum_{k=0}^5A^{-k}J^k$; a convergent normalizer is not needed. Existence is DYAD OPEN 20 (IMP-O10-04).",
   "- **Realization.** A real carrier for the whole class follows from one object, an identity-tangent sixth root of $F=T^6$ (equivalently a real $J$), via Bochner averaging $\\Phi=\\tfrac16\\sum_{k=0}^5A^{-k}J^k$; a convergent normalizer is not needed. In $C^\\infty$ this object exists (`DYAD-THM-SMOOTH-EMBEDDING`, IMP-O10-06) and $\\Phi$ is the owner's chart (`DYAD-THM-SMOOTH-EQUIVARIANT-CHART`, IMP-O10-07); uniqueness of $J$, $K_m$ and $R$ holds in the DYAD F2/F3 sense, and E2 only among generators with $DX'(0)=0$. Analytic existence is DYAD OPEN 20 B-an/B-6 (IMP-O10-04).")
ed("R19a", "19", "Chiral convention for sign statements (Genesis §6.3a): $u=w_1+\\lambda w_2$, $v=w_1+\\bar\\lambda w_2$, $N=|u|^2+|v|^2$, $S=\\operatorname{Im}(w_1\\bar w_2)=(|u|^2-|v|^2)/\\sqrt{12}$, $\\rho=S/N$. A sign of chirality must name its convention.",
   "Chiral convention for sign statements (Genesis §6.3a): $u=w_1+\\lambda w_2$, $v=w_1+\\bar\\lambda w_2$, $N_{\\rm ch}=|u|^2+|v|^2$, $S=\\operatorname{Im}(w_1\\bar w_2)=(|u|^2-|v|^2)/\\sqrt{12}$, $\\chi=S/N_{\\rm ch}$. A sign of chirality must name its convention. Notation (v0.11): $\\chi$ and $N_{\\rm ch}$ replace the v0.10 symbols $\\rho$ and $N$ of this paragraph, which clashed with the dyad coordinate $\\rho$ and the normal-form map $N$; formulas and normalizations are unchanged.")

# ----------------------------------------------------------------------------------------------- §5.5.5 (rows 1, 3)
ed("R03c", "3", "Loopholes: non-manifold or finite-amplitude regimes; other carriers (OPEN-C19-L) |",
   "Non-manifold invariant sets and finite-amplitude regimes are outside this test and the no-go; a proposal using them must supply its own recovery contract. Other carriers: OPEN-C19-L |")
ed("R01i", "1", "| C, transported κ-family | **Primary formal candidate class; real only once $J$ is realized.** A family with an in-class modulus (§5.5.7), not a single model | Standard C exactly on $\\mathcal S_0,\\mathcal S_\\pm$; Q4 capacity; Q5 with active covariance; Q6 by IMP-O10-02 and narrow-Q6 case (ii) for real $C^3$ germs |",
   "| C, transported κ-family | **Primary realized smooth mathematical candidate family; analytic exact realization and physical selection open.** A family with an in-class modulus (§5.5.7), not a single model | Standard C exactly on $\\mathcal S_0,\\mathcal S_\\pm$ (real $C^\\infty$ for the $C^\\infty$ member); Q4 capacity; Q5 with active covariance; Q6 by IMP-O10-02 and narrow-Q6 case (ii) for real $C^3$ germs, C2 included; κ values per the §5.5.4 table |")

# ----------------------------------------------------------------------------------------------- §5.5.6 (rows 1, 4, 19, 21)
ed("R19b", "19/21", "- `[ALG — leading order; SESSION]` Per six-step block, $\\Delta\\log(|u|^2/|v|^2)=\\tfrac13(|u|^2-|v|^2)+O(|(u,v)|^4)$: the chiral axes $\\mathcal S_+=\\{u=0\\}$, $\\mathcal S_-=\\{v=0\\}$ are relatively attracting at cubic order. The attraction is **relative**: $\\Delta\\rho=S(\\tfrac16-2\\rho^2)+O(5)$, so $|\\rho|\\to1/\\sqrt{12}$ while $|S|$ decays with $N$.",
   "- `[ALG]` [scope: leading order] [provenance: SESSION] Per six-step block, $\\Delta\\log(|u|^2/|v|^2)=\\tfrac13(|u|^2-|v|^2)+O(|(u,v)|^4)$: the chiral axes $\\mathcal S_+=\\{u=0\\}$, $\\mathcal S_-=\\{v=0\\}$ are relatively attracting at cubic order. The attraction is **relative**: $\\Delta\\chi=S(\\tfrac16-2\\chi^2)+O(5)$, so $|\\chi|\\to1/\\sqrt{12}$ while $|S|$ decays with $N_{\\rm ch}$.")
ed("R04a", "1/4", "- **Single-dyad imports on the lock surfaces only.** On $\\mathcal S_0,\\mathcal S_\\pm$ each edge is an isolated dyad, so the IMP-O10-05 results apply edgewise there, conditional on the real surfaces ($J$). Nothing transfers off the surfaces, and nothing transfers as a separator or basin statement.",
   "- **Single-dyad imports on the lock surfaces only.** On $\\mathcal S_0,\\mathcal S_\\pm$ each edge is an isolated dyad, so the IMP-O10-05 results apply edgewise there; the surfaces exist as real $C^\\infty$ submanifolds for the $C^\\infty$ member (§5.5.4). Their constants hold edgewise in the dyad chart and domain where they are proved; in the $\\Phi$ chart they hold qualitatively unless an explicit estimate is supplied, since $\\Phi$ inherits none of the §6.14 finite-chart bounds (SG-19). R9-conditional statements keep their assumption. Nothing transfers off the surfaces, and nothing transfers as a separator or basin statement.")

# ----------------------------------------------------------------------------------------------- §5.5.7 (row 21)
ed("R21a", "21", "The fifth-order ψ-modulus `[ALG — SESSION; RF-O10-02]` establishes a nontrivial formal conjugacy obstruction within its stated scope. The universal finite-$a$ classification retains the FMS symbolic P4 evidence qualification (`[ALG — SESSION; FMS symbolic P4 reported, OFN sampled verification]`).",
   "The fifth-order ψ-modulus (`[ALG]` [provenance: SESSION], RF-O10-02) establishes a nontrivial formal conjugacy obstruction within its stated scope. The universal finite-$a$ classification retains the FMS symbolic P4 evidence qualification (`[ALG]` [provenance: SESSION; FMS symbolic P4 source-reported; OFN sampled verification at three κ]).")

# ----------------------------------------------------------------------------------------------- §5.5.8 (row 1)
ed("R01j", "1", "- No physical carrier, chirality, isolation regime or exchange operation is selected; class C is not claimed unique, and the ψ-modulus has no physical value.",
   "- No physical carrier, chirality, isolation regime or exchange operation is selected; class C is not claimed unique, analytic or physical, and the ψ-modulus has no physical value.")

# ----------------------------------------------------------------------------------------------- §8, §9 (rows 1, 5, 8, 12, 20, 21)
ed("R23a", "23", "Programme v1.3 distinguishes OPEN-P2A from P2B", "Programme v1.3 distinguishes OPEN-P2A from P2B")  # placeholder replaced below
E.pop()
ed("R20a", "20", "Reference-only source report (RF-O08-08): Triadic v1.6.1 and Genesis v2.8.5 retain scoped",
   "Reference-only source report (RF-O08-08): Triadic v1.6.1 and Genesis v2.8.5 (claim-level pin; statement not re-read at `gen-v2.9`) retain scoped")
ed("R21b", "21", "All twenty entries belong to OFN for the foundational question;", "All twenty-one entries belong to OFN for the foundational question;")
ed("R21c", "21", "This registry preserves all twenty existing OFN research identities.", "This registry holds twenty-one OFN research identities (twenty ACTIVE, one PARTIAL).")
ed("R08a", "8", "Next required artifact or decision: Owner state/rule/covariance record, including star common-token shifts and path ties; recover the six-constraint list.",
   "Next required artifact or decision: the owner state/rule/covariance record is delivered (`tdrg-v2.12.14`: `TDRG-DEF-ZN-STATE`, SG-14, `TDRG-DEF-ORIENT`; Finding A statement accepted); recover the six-constraint list. A fixed-star $2c=0$ is not a covariance theorem for all policies, and TDR-G's ruling is not an ontological derivation of the rule.")
ed("R01k", "1", "This is a formal, $J$-conditional invariant-subsystem witness for a specified coupled triad law.",
   "This is a real $C^\\infty$ invariant-subsystem witness for a specified coupled triad law (§5.5.4; DYAD IMP-O10-06/07), not closure.")
ed("R08b", "8/9", "Dependencies: LEM-REACH, LEM-RETRIG; OPEN-OFN-5/FSP/SECTOR; TDRG rule/policy owner.⟨BR⟩",
   "Dependencies: TDRG-ALG-LEM-REACH, TDRG-ALG-LEM-RETRIG; OPEN-OFN-5/FSP/SECTOR; TDRG rule/policy owner (`TDRG-DEF-ORIENT`, SG-14).⟨BR⟩")
ed("R12a", "12", "Dependencies: §1.2; IMP-O08-20 primitive contraction; NUMGEN local history/order/slip modules and its separately located L-BACKBONE reference; RECOG event rule.⟨BR⟩",
   "Dependencies: §1.2; IMP-O08-20 primitive contraction; NUMGEN local history/order/slip modules and `NUMGEN-RESULT-N5AS1-L-BACKBONE` (`numgen-v1.21` §6.6); RECOG event rule.⟨BR⟩")
ed("R12b", "12", "NUMGEN v1.21 §6.6 supplies the separate L-BACKBONE asymptotic at source grade ALG; it lacks a dedicated theorem RID and remains a precisely located reference. The primitive-orbit interpretation is OFN's reading of its source context, with observable/frame/index/domain confirmation requested from NUMGEN (RF-O08-09; REQ-O09-03).",
   "NUMGEN v1.21 §6.6 supplies the separate L-BACKBONE asymptotic as `NUMGEN-RESULT-N5AS1-L-BACKBONE` (`[RESULT]` `[from: ALG]`), with $q_m:=Q_{\\rm true}(T^{6m}x)$ typed by the owner as the block-sampled primitive observable on NUMGEN's declared tube (RF-O08-09; REQ-O09-03 fulfilled). No inclusion of NUMGEN's tube in an explicit DYAD or RECOG domain is inferred.")
ed("R01l", "1", "For class C, radial contraction removes flat ambiguity among admissible smooth commuting realizations (DYAD Lemma F / F3, IMP-O10-04); existence remains open, and identifying any realization with pole exchange needs a separate ontological and representation contract (this OPEN; RRF OPEN-A). Status unchanged.",
   "For class C, radial contraction removes flat ambiguity among admissible smooth commuting realizations (DYAD Lemma F / F3, IMP-O10-04); a real $C^\\infty$ realization exists (IMP-O10-06/07), analytic existence remains open, and identifying any realization with pole exchange needs a separate ontological and representation contract (this OPEN; RRF OPEN-A). Status unchanged.")
ed("R01m", "1/5", "Dependencies: §5.5; DYAD OPEN 20 (realization of $J$); RF-O10-02 (modulus and its reflection-limited readout); RRF model-contract row; FMS basin-boundary work;",
   "Dependencies: §5.5; DYAD OPEN 20 B-an/B-6, only if an analytic model is wanted; RF-O10-02 (modulus and its reflection-limited readout); RRF §6.2a model-contract row and its representation-level readout entry; FMS basin-boundary work;")
ed("R05b", "5", "Next required artifact or decision: an RRF readout contract. A torus-invariant scalar reading the sign of $m-m_*$ is needed only if RRF requires a full physical readout.",
   "Next required artifact or decision: the physical selection, isolation and chirality obligations above. RRF `rrf-v0.8.4` §6.2a supplies the representation-level readout contract (primitive clock and transported chart declared; $|c|$ reads $m$ only up to reflection; \"Im c = 0\" is no selection principle); no sign-reading scalar for $m-m_*$ is mandatory.")
ed("R05c", "5", "A stated principle or effective-limit argument fixing the modulus (or an explicit equivalence class) in a declared carrier and encoding, with the RRF readout contract;",
   "A stated principle or effective-limit argument fixing the modulus (or an explicit equivalence class) in a declared carrier and encoding, consistent with the RRF readout contract (`rrf-v0.8.4` §6.2a);")

# ----------------------------------------------------------------------------------------------- §10 (rows 8, 11)
ed("R08c", "8", "| Arbitrary path label / first listed star center | Passive labels cannot choose physical outcomes | A valid relational orientation/selection rule still requires owner verification |",
   "| Arbitrary path label / first listed star center | Passive labels cannot choose physical outcomes | The owner rule is `TDRG-DEF-ORIENT` with the balanced path-tie and SG-14 covariance on the canonical branch (`tdrg-v2.12.14`); `largest_center`'s node-ID tie-break is the recorded surviving label-dependent instance (`TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK`) |")
ed("R11a", "11", "| Total additive token sum as a physical conserved quantity | Owner rejection/gauge claim needs the actual rule, action and observable | Nonconservation and gauge dependence are not interchangeable; broad rejection withheld pending TDRG review |",
   "| Total additive token sum as a physical conserved quantity | Under `TDRG-DEF-STAR` the sum $\\Sigma\\delta$ changes by $-\\delta_A \\pmod N$ at a star event and is preserved by the token permutations (swap, path successor shift, ties); exact conservation therefore fails on the birth-capable model | The common token shift is not a gauge of the full model (TDR-G SG-14: outside $G_{\\rm cov}$, a symmetry of the birth-free sector only). Nonconservation and gauge dependence remain distinct: neither a physical-momentum reading nor a universal \"unphysical\" verdict follows without a named observable and physical contract. TDR-G's own \"gauge-like\" / \"gauge artifact\" labels are referred back to TDR-G (`pipes/TDRG/20261029-OFN-token-sum-gauge-label.md`) |")

# ----------------------------------------------------------------------------------------------- §11.1-§11.2 (rows 9, 10, 12, 14, 16, 21, 23)
ed("R23b", "21/23", "Normative references: `DSN_METHODOLOGY_v1.3` §§0.5–0.7, 3.3–3.4, 4–5, 7 and 12–13; `RTG_PROGRAMME_OVERVIEW_v1.2` §§3–5, §7 and SG-PROG-1–4. These governance texts are accessible through the project index, not as original mounted byte copies in this pass. They remain adopted references, not mathematical theorem imports; their earlier release evidence is not represented as newly supplied.",
   "Normative references: DSN Methodology v1.4 (`methodology-v1.4`) §§0.5–0.7, 1.1, 3.2–3.4, 4–5, 7, 8 and 12–13; Programme Overview v1.3 (`programme-v1.3`) §§3–5, §7 and §8 (SG-PROG-1–4). They are adopted references, not mathematical theorem imports.\n\n**Governing editions at this edition** (claim-level pins are at each use): Programme v1.3, Methodology v1.4, Dyadic v6.4.22, Genesis v2.9, RRF v0.8.4, TDR-G v2.12.14, NUMGEN v1.21, RECOG v0.3.26, Triadic v1.6.1. A pin left on an older edition is a claim-level pin whose statement was not re-read at the governing tag; it is labelled so where it occurs (Methodology v1.4 §1.1 rule 4).")
ed("R09m", "9", "The `IMP-O08-*` keys identify this consumer's administrative entries. They are not invented source RIDs. Unnumbered source blocks use `RID unavailable`; owner legacy labels such as `LEM-REACH` are preserved rather than silently renamed.",
   "The `IMP-O08-*` keys identify this consumer's administrative entries. They are not invented source RIDs. Owner RIDs are cited as the owner registers them; TDR-G's former labels (`LEM-*`, `CONV-*`) are aliases of the `TDRG-ALG-LEM-*` / `TDRG-DEF-CONV-*` RIDs of its §7 map, and `RID unavailable` remains only where the owner has registered none (IMP-O08-01).")
ed("R09n", "9", "Updated blocks state their exact source and scope; untouched TDR-G imports retain their existing version and limitations.",
   "Updated blocks state their exact source and scope; the TDR-G imports carry the owner RIDs of `tdrg-v2.12.14` §7 with unchanged statements.")
ed("R23c", "23", "- **IMP-O08-01** :: Zero-origin and first-dyad definitions :: `RTG_GENESIS_GEOMETRY_DSN_v2.9` §6.1 #sec-6-1-primitive :: §1.3 notation only\n  Source identity: `RID unavailable`. Source status: `DEF`. Depends on: The formal definitions O0=0 and 0→(A,B), A+B=0; no physical creation/conservation theorem.\n  Reconciliation: The source expressions are retained; dedicated zero-origin/first-dyad IDs remain requested. This does not resolve the separate primitive-map custody issue.",
   "- **IMP-O08-01** :: Zero-origin and first-dyad definitions :: `RTG_GENESIS_GEOMETRY_DSN_v2.9` §6.1 #sec-6-1-primitive :: §1.3 notation only\n  Source identity: `RID unavailable` (Genesis registers no RID for these two blocks at `gen-v2.9`). Source status: `DEF`. Depends on: The formal definitions O0=0 and 0→(A,B), A+B=0; no physical creation/conservation theorem.\n  Reconciliation: The source expressions are retained unchanged at `gen-v2.9`; a dedicated Genesis identifier is Genesis's decision. OFN's own convention block now carries `RTG-OFN-DEF-ZERO-ORIGIN`.")
TD = [
 ("IMP-O08-02", "[RID: RID unavailable] :: Full discrete phase/token state", "[RID: TDRG-DEF-ZN-STATE; TDRG-DEF-PHYSICAL-STATE; TDRG-DEF-REL-ADVANCE] :: Full discrete phase/token state",
  "  Synchronization: State RID remains requested; local token-origin consequence has registered OFN identity and transfer proposal XFER-O08-01; RF-O08-01.",
  "  Synchronization: owner RIDs registered (`tdrg-v2.12.14` §7). `TDRG-DEF-PHYSICAL-STATE` still says \"only $\\Delta_{ij}$ are physical\"; OFN does not use that phrase to delete tokens. Finding A: statement accepted by TDR-G, custody XFER-O08-01 deferred to v2.13; RF-O08-01."),
 ("IMP-O08-03", "[RID: RID unavailable] :: Even-N cyclic defect band", "[RID: TDRG-DEF-BAND] :: Even-N cyclic defect band",
  "  Synchronization: Dedicated definition RID requested; no continuous excursion identified.", "  Synchronization: owner RID registered; no continuous excursion identified."),
 ("IMP-O08-04", "[RID: RID unavailable] :: Node-difference triangle holonomy", "[RID: TDRG-THM-HOLONOMY] :: Node-difference triangle holonomy",
  "  Synchronization: Dedicated holonomy theorem RID requested; no re-ownership or curvature promotion.", "  Synchronization: owner RID registered; no re-ownership or curvature promotion."),
 ("IMP-O08-04B", "[RID: RID unavailable] :: Strict narrow-band exclusion", "[RID: TDRG-THM-NARROW-BAND-EXCLUSION] :: Strict narrow-band exclusion",
  "  Synchronization: Dedicated narrow-band theorem RID requested.", "  Synchronization: owner RID registered."),
 ("IMP-O08-05", "[RID: LEM-REACH] :: Free orbit", "[RID: TDRG-ALG-LEM-REACH] :: Free orbit",
  "  Synchronization: Preserve owner legacy lemma identifier; no invented TDRG-prefix replacement.", "  Synchronization: owner RID registered; `LEM-REACH` is its alias."),
 ("IMP-O08-06", "[RID: LEM-NOANNIHIL] :: No free return", "[RID: TDRG-ALG-LEM-NOANNIHIL] :: No free return",
  "  Synchronization: Preserve scoped import and original axiom retirement; no universal no-erasure or birth theorem.", "  Synchronization: owner RID registered (`LEM-NOANNIHIL` its alias); scoped import and original axiom retirement preserved; no universal no-erasure or birth theorem."),
 ("IMP-O08-07", "[RID: LEM-RETRIG] :: Impact-overlap", "[RID: TDRG-ALG-LEM-RETRIG] :: Impact-overlap",
  "  Synchronization: Owner summary says exact period two even at d=0. OFN retains the displayed map, explicitly separates the fixed case, and requests owner correction (OFN08-C12).",
  "  Synchronization: owner RID registered (`LEM-RETRIG` its alias). The owner now states \"a 2-cycle for $d\\neq0$, a fixed point for $d=0$\"; the OFN08-C12 request is fulfilled and the OFN statement is unchanged."),
 ("IMP-O08-08", "[RID: RID unavailable] :: Deterministic fixed-cap", "[RID: TDRG-THM-RECURRENCE] :: Deterministic fixed-cap",
  "  Synchronization: Dedicated result RID requested; no universal thermodynamic or chaos inference.", "  Synchronization: owner RID registered; no universal thermodynamic or chaos inference."),
 ("IMP-O08-09", "[RID: RID unavailable] :: Star creates", "[RID: TDRG-DEF-STAR] :: Star creates",
  "  Synchronization: Star-definition RID remains requested; finding A is offered under XFER-O08-01 with its OFN RID, not an invented TDRG ID; RF-O08-01.",
  "  Synchronization: owner RID registered. Finding A: statement accepted by TDR-G and used in SG-14; custody XFER-O08-01 deferred to TDR-G v2.13; the RID stays OFN's; RF-O08-01."),
 ("IMP-O08-14", "[RID: CONV-TICK] :: Advance", "[RID: TDRG-DEF-CONV-TICK] :: Advance",
  "  Synchronization: Retain owner convention name; source-reported v18 engineering audit is not rerun.", "  Synchronization: owner RID registered (`CONV-TICK` its alias); the source-reported v18 engineering audit is not rerun (`[conv: v18]`, `EV-NOT-RERUN`)."),
 ("IMP-O08-15", "[RID: CONV-P3CYC] :: Successor-token", "[RID: TDRG-DEF-CONV-P3CYC] :: Successor-token",
  "  Synchronization: Owner path-orientation audit queued; do not import reported convention-sensitivity numerics as a definition.",
  "  Synchronization: owner RID registered (`CONV-P3CYC` its alias). REQ-O09-05 endpoint component answered: `TDRG-DEF-ORIENT` (balanced path-tie on $S=0\\wedge2E\\equiv0$), SG-14 covariance on the canonical branch with a finite $N=24$ equivariance check, `largest_center` exception recorded. Reported convention-sensitivity numerics are not imported as a definition; motif and BIND3 numerics keep `[conv: v18]`."),
 ("IMP-O08-16", "[RID: LEM-SPECCONS] :: Pairwise", "[RID: TDRG-ALG-LEM-SPECCONS] :: Pairwise",
  "  Synchronization: Owner scope/wording reconciliation queued; BIND3 statistics remain separate RF-O08-04.", "  Synchronization: owner RID registered (`LEM-SPECCONS` its alias); BIND3 statistics remain separate, RF-O08-04."),
]
for k, (key, o1, n1, o2, n2) in enumerate(TD):
    ed(f"R09-{key}a", "9", f"- **{key}** {o1}", f"- **{key}** {n1}")
    ed(f"R09-{key}b", "9/10", o2, n2)
ed("R09o", "8/9", "Depends on: An oriented path must already be well-defined. The antipodal endpoint/presentation question is not discharged.",
   "Depends on: An oriented path under `TDRG-DEF-ORIENT`; the antipodal endpoint/presentation question is discharged on the canonical branch at SG-14 scope.")
ed("R16c", "16", "- **IMP-O08-12** :: Primitive continuous dyad map :: `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22` §6.1 #sec-6-1-map :: §4.2\n  Source identity: `RID unavailable`. Source status: `DEF`. Depends on: Selected K=1 model and local/lifted coordinate convention; no all-p or global fixed-point assertion.\n  Reconciliation: Dyadic remains the declared source lineage, with missing definition RID. Genesis v2.8.5 uses GEN-DEF-PRIMITIVE-MAP for the same formula. CUST-O09-01 requests a joint owner decision; OFN assigns no alias or competing owner.",
   "- **IMP-O08-12** :: Primitive continuous dyad map :: `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22` §6.1 #sec-6-1-map :: §4.2\n  Source identity: `DYAD-DEF-PRIMITIVE-MAP` (registered provisional, Dyadic custody). Source status: `DEF`. Depends on: Selected K=1 model and local/lifted coordinate convention; no all-p or global fixed-point assertion.\n  Reconciliation: Dyadic owns the definition; Genesis records `GEN-DEF-PRIMITIVE-MAP` as its alias (`gen-v2.9` §1). CUST-O09-01 / REQ-O09-04 answered (Dyadic notice N4 received).")
ed("R14b", "14", "  Verification: source block directly inspected; theorem/source custody remains RECOG. The live source declares freeze-candidate status; no final freeze record or certificate rerun is claimed.\n\n<a id=\"imp-o09-02\"></a>",
   "  Verification: source block read at `recog-v0.3.26` (statement unchanged); theorem/source custody remains RECOG; no certificate rerun.\n\n<a id=\"imp-o09-02\"></a>")
ed("R14c", "14", "  Verification: source block directly inspected; theorem/source custody remains RECOG. The live source declares freeze-candidate status; no final freeze record or certificate rerun is claimed.\n\n<a id=\"imp-o09-03\"></a>",
   "  Verification: source block read at `recog-v0.3.26` (statement unchanged); theorem/source custody remains RECOG; no certificate rerun.\n\n<a id=\"imp-o09-03\"></a>")
ed("R14d", "14", "  Verification: source block directly inspected; theorem/source custody remains RECOG. The live source declares freeze-candidate status; no final freeze record or certificate rerun is claimed.\n\n### 11.3",
   "  Verification: source block read at `recog-v0.3.26` (statement unchanged); theorem/source custody remains RECOG; no certificate rerun. The v0.3.20 edition's frozen status is documented by `records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (REQ-O09-02 fulfilled).\n\n### 11.3")
ed("R12c", "12", "Reconciliation: Replacement, not a re-pin of the old asymptotic. The original v0.8 input is preserved in OFN09-C01; NUMGEN L-BACKBONE stays a separate ALG reference with a dedicated-RID request.",
   "Reconciliation: Replacement, not a re-pin of the old asymptotic. The original v0.8 input is preserved in OFN09-C01; NUMGEN L-BACKBONE is the separate `NUMGEN-RESULT-N5AS1-L-BACKBONE` (RF-O08-09). Statement checked unchanged at `dyad-v6.4.22` §6.14.")

# ----------------------------------------------------------------------------------------------- §11.3 (rows 7, 8, 12, 14, 15, 16, 20, 23)
ed("R14e", "14", "No original owner certificate or campaign is rerun. The live RECOG release qualification and RRF work-local adoption limit apply throughout.",
   "No original owner certificate or campaign is rerun. RRF is cited at its adopted working-standard scope.")
ed("R07d", "7/8", "Neither campaign was rerun here, and these records do not settle the general endpoint-policy ruling.\nAction: TDR-G retains the endpoint-policy/full-selector ruling and prospective custody decision. XFER-O08-01 remains proposed; NUMGEN acknowledgment is not transfer acceptance. No new physics or v18 recertification is implied.",
   "Neither campaign was rerun here. TDR-G v2.12.14 has since ruled the endpoint policy (`TDRG-DEF-ORIENT`; SG-14; DISC-2 effect 20 of 136 records under the adopted rule, its §6.12).\nAction: TDR-G accepts the Finding A statement and defers the custody transfer XFER-O08-01 to v2.13; NUMGEN acknowledgment is not transfer acceptance. No new physics or v18 recertification is implied.")
ed("R20b", "20/23", "- **RF-O08-02 — Continuous closure and mode representations** :: Triadic v1.6.1 §§6.15–6.18, SG-18 and CN-01–CN-05; Genesis v2.8.5 §§6.3–6.6",
   "- **RF-O08-02 — Continuous closure and mode representations** :: Triadic v1.6.1 §§6.15–6.18, SG-18 and CN-01–CN-05; Genesis v2.8.5 §§6.3–6.6 (claim-level pin; not re-read at `gen-v2.9`)")
ed("R20c", "20", "Action: use current owner-scoped statements only. Neither a sign correction nor a shared symbol proves that diagnostic and primitive models are equivalent.",
   "Action: use current owner-scoped statements only. Neither a sign correction nor a shared symbol proves that diagnostic and primitive models are equivalent. Triadic v1.6.1 §7.4 \"Programme/OFN pass two\" — OFN half recorded: corrected local algebra, numerical outcomes of the former mis-scaled model and physical interpretation are kept distinct; no cascade verdict, source deficit or ontology selection follows; no Triadic release is a precondition.")
ed("R20d", "20/23", "- **RF-O08-03 — Rank capacity, birth direction and physical transverse carrier** :: Genesis v2.8.5 GCL-05/06 and OPEN 5/2B;",
   "- **RF-O08-03 — Rank capacity, birth direction and physical transverse carrier** :: Genesis v2.8.5 GCL-05/06 and OPEN 5/2B (claim-level pin; not re-read at `gen-v2.9`);")
ed("R20e", "20/23", "- **RF-O08-08 — Birth and UV/cascade interpretation** :: Triadic v1.6.1 CN-01–CN-05; Genesis v2.8.5 GCL-01–11;",
   "- **RF-O08-08 — Birth and UV/cascade interpretation** :: Triadic v1.6.1 CN-01–CN-05; Genesis v2.8.5 GCL-01–11 (claim-level pin; not re-read at `gen-v2.9`);")
ed("R14f", "14", "Action: record positive retained-memory evidence without defining a physical event, transporting the theorem to another comparator by renaming, or selecting a new carrier. RECOG's live v0.3.20 metadata still says freeze candidate; final release authentication remains REQ-O09-02.",
   "Action: record positive retained-memory evidence without defining a physical event, transporting the theorem to another comparator by renaming, or selecting a new carrier. REQ-O09-02 is fulfilled by `records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (SHA-256 `5c00f66d…9b55`), with that record's own evidence qualification (the verbatim exchange is not retained).")
ed("R12d", "12", "L-BACKBONE supplies q_M=1/M+O(M^(-3/2)) and sum_(m<M) q_m=log M+C_Q+o(1), at source grade RESULT from ALG, without a dedicated theorem RID. The primitive-orbit reading is OFN's reading of that block's L1/primitive context, not a separately confirmed owner definition of q_m; REQ-O09-03 requests the explicit observable, frame, sampling index and domain when NUMGEN assigns the RID. Shared notation does not identify it with RECOG's chart-native q=|z|^2.",
   "L-BACKBONE (`NUMGEN-RESULT-N5AS1-L-BACKBONE`) supplies q_M=1/M+O(M^(-3/2)) and sum_(m<M) q_m=log M+C_Q+o(1), at source grade RESULT from ALG. The owner types q_m := Q_true(T^(6m) x), the block-sampled primitive observable on the declared tube, not the normalized-chart q=|z|^2 (`numgen-v1.21` §6.6; REQ-O09-03 fulfilled). No inclusion of NUMGEN's tube in an explicit DYAD or RECOG domain is inferred.")
ed("R12e", "12", "Action: IMP-O08-20 uses the identified DYAD contraction bound. Request a dedicated L-BACKBONE RID and explicit owner confirmation of its observable/frame/index/domain (REQ-O09-03), without borrowing its OPEN-module identity or regrading its proof. No exact clock, calibrated duration or full physical arithmetic is inferred.",
   "Action: IMP-O08-20 uses the identified DYAD contraction bound; L-BACKBONE is cited by its owner RID without regrading its proof. No exact clock, calibrated duration or full physical arithmetic is inferred.")
ed("R15a", "15", "In CELL-F3, RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE / RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH concern the registered single-dyad mechanism and certified order.",
   "Recorded at `recog-v0.3.26` by exact claim, each with its own conditions, not as an event principle: `RECOG-RESULT-A1C-RECORD-PHASE-READOUT` (record-phase readout), the record-fiber constraint and the finite-prefix record-only outer decoder of the A1c chain (§6.13b; under (D5), chart/domain and at-least-two-usable-slip conditions where stated). No injectivity, connectedness, write-through, physical event or OPA closure is inferred; R9 and (D5) are not removed, and the two order sentences RECOG retracted in v0.3.26 Appendix B are not cited. The sharpened rows `RECOG-THM-R9-SHARPENED-ROWS` may be cited beside the unchanged RF-O09-01 table.\nIn CELL-F3, RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE / RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH concern the registered single-dyad mechanism and certified order.")
ed("R16d", "16/23", "Owner example for SG-OFN-PRESENTATION: Dyadic v6.4.10 SG-19 distinguishes", "Owner example for SG-OFN-PRESENTATION: Dyadic v6.4.22 SG-19 distinguishes")
ed("R16e", "16/23", "- **RF-O08-05 — All-p resonance and generator selection** :: Dyadic v6.4.10 p-family;", "- **RF-O08-05 — All-p resonance and generator selection** :: Dyadic v6.4.22 §6.11 p-family;")
ed("R16f", "16/23", "named N-1/N-2/N-2-ORD/N5AS1-INF/GAP-LOCK blocks; Dyadic v6.4.10 §6.14", "named N-1/N-2/N-2-ORD/N5AS1-INF/GAP-LOCK blocks; Dyadic v6.4.22 §6.14")

# ----------------------------------------------------------------------------------------------- §11.4 (rows 1, 4, 23, 28)
ed("R23d", "23", "These entries support §5.5 only. Inherited §11.2 entries keep their v0.9 pins: the Genesis v2.8.5 and Dyadic v6.4.10 imports there are **not** re-pinned to v2.8.9 / v6.4.16, because no inherited statement was re-inspected against the newer editions for this draft. Source statements below were read in the cited owner files; no owner certificate is rerun.",
   "These entries support §5.5. Source statements below were read in the cited owner files; no owner certificate is rerun. The Genesis and Dyadic pins are the claim-level sources; each cited statement was checked unchanged at `gen-v2.9` and `dyad-v6.4.22`.")
ed("R01n", "1", "Class C satisfies (H-JET) with $n=n_{21}$, $\\mu=\\mu_6\\ne0$ for instance C1, and for C2 conditionally on Φ.",
   "Class C satisfies (H-JET) with $n=n_{21}$, $\\mu=\\mu_6\\ne0$ for instance C1 and for instance C2 in the owner's $C^\\infty$ chart Φ (IMP-O10-07; Genesis v2.9 G-20 existence note: C2 non-vacuous at $C^\\infty$).")
ed("R01o", "1", "OPEN 20 is PARTIAL: B-∞ flat uniqueness CLOSED for existing $C^\\infty$ objects; B-an, B-6 and B-∞ existence open.\n  Depends on: an *existing* $C^\\infty$ identity-tangent root; existence is not imported. The Borel-and-iterate route is a proposal only, and RRF L-SHADOW-POLY is not imported.",
   "OPEN 20 (`dyad-v6.4.22`): PARTIAL — B-∞ existence CLOSED by `DYAD-THM-SMOOTH-EMBEDDING` (IMP-O10-06), B-∞ flat uniqueness CLOSED, B-an and B-6 ACTIVE. Lemma F and F3 statements checked unchanged at `dyad-v6.4.22` §6.17.\n  Depends on: an existing $C^\\infty$ identity-tangent root, now supplied by IMP-O10-06. The §6.17 sequence $F^{-n}R_\\infty F^n$ remains an unproved route, and RRF L-SHADOW-POLY is not imported.")
ed("R01p", "1/4", "  Depends on: an isolated dyad. Applied only on $\\mathcal S_0,\\mathcal S_\\pm$, edgewise, conditional on the real surfaces ($J$). Static leading offsets transfer edgewise and class-wide at leading order. Nothing transfers off the surfaces or as a separator or basin statement. v6.4.16 (lifecycle-only) records OPEN 3 CLOSED within its scope and opens OPEN 21; no graded RID changed (RF-O10-04).",
   "  Depends on: an isolated dyad. Applied only on $\\mathcal S_0,\\mathcal S_\\pm$, edgewise; the surfaces exist in $C^\\infty$ (§5.5.4). Constants hold in the dyad chart and domain where proved; in the Φ chart only qualitatively unless an explicit estimate is supplied (SG-19). R9-conditional statements keep their assumption. Static leading offsets transfer edgewise and class-wide at leading order. Nothing transfers off the surfaces or as a separator or basin statement. v6.4.16 (lifecycle-only) records OPEN 3 CLOSED within its scope and opens OPEN 21; no graded RID changed (RF-O10-04).")
NEWIMP = r"""

<a id="imp-o10-06"></a>
- **IMP-O10-06** :: Smooth flow embedding of the six-step return (OPEN 20 B-∞ existence) :: `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22` §6.17 :: §5.5.3–§5.5.6; OPEN-OFN-3B, OPEN-OFN-OPA and OPEN-OFN-TRIAD-CLASS inputs
  Source identity: `DYAD-THM-SMOOTH-EMBEDDING` (v6.4.18). Source status: `THM`, scope $C^\infty$ local germs at $P_1$, raw frame $W$, lifted chart.
  Depends on: (E1) a $C^\infty$ field $X$ with $j^\infty_0X=\log F$ and $F=\varphi^1_X$ on a ball of qualitative radius; (E2) uniqueness only among generators with $DX'(0)=0$; (E3) the roots $K_m=\varphi_X^{1/m}$ commute with $T$ and are unique (F3); (E4) $J=T\circ K_6^{-1}$ with $J^6=\mathrm{id}$, $DJ(0)=A$, $JT=TJ$, and $R=T^3\circ K_2^{-1}$. No numerical radius, finite-$C^k$ constant, analyticity (B-an, B-6) or physical exchange / G2 realization follows (owner §6.17 recorded distinctions).
  Verification: statement read at `dyad-v6.4.22`; no certificate rerun. Receipt of Dyadic notice N14 recorded (§12.3).

<a id="imp-o10-07"></a>
- **IMP-O10-07** :: Smooth equivariant chart :: `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22` §6.17 :: §5.5.3 (C2), §5.5.4
  Source identity: `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (v6.4.20). Source status: `THM` (corollary of E3–E4, finite-group averaging).
  Depends on: the $C^\infty$ germ $J$ of IMP-O10-06; $\Phi=\tfrac16\sum_{k=0}^5A^{-k}J^k$ is a $C^\infty$ local diffeomorphism with $\Phi(0)=0$, $D\Phi(0)=I$, $\Phi\circ J=A\circ\Phi$, and $N_\Phi=\Phi T\Phi^{-1}$ commutes with $A$. Radius qualitative; $\Phi$ inherits none of the §6.14 finite-chart bounds (SG-19); no analyticity. The owner leaves its use to Genesis C2 and OFN class C; OFN uses it for class C (§5.5.4).
  Verification: statement read at `dyad-v6.4.22`; no certificate rerun."""
ed("R01q", "1", "Nothing transfers off the surfaces or as a separator or basin statement. v6.4.16 (lifecycle-only) records OPEN 3 CLOSED within its scope and opens OPEN 21; no graded RID changed (RF-O10-04).\n\n### 11.5",
   "Nothing transfers off the surfaces or as a separator or basin statement. v6.4.16 (lifecycle-only) records OPEN 3 CLOSED within its scope and opens OPEN 21; no graded RID changed (RF-O10-04)." + NEWIMP + "\n\n### 11.5")

# ----------------------------------------------------------------------------------------------- §11.5 (rows 5, 21, 25, 28)
ed("R05d", "5", "Action: §5.5.4 declares class C under §0.3 and requests a model-contract row. RRF decides. RRF v0.8.4 is a working standard; this is a reference, not a theorem import.",
   "RRF v0.8.4 §6.2a registers class C as a reference-only model-contract row (not a native profile) importing `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT`, and adds a ψ-readout entry: $|c|$ determines $m$ only up to the reflection; the phase of $c$ is representation-dependent; a phase readout states the primitive clock and the transported chart and is not by itself a physical chirality observable. Its regularity field calls the $C^\\infty$ class-C transport a conditional RRF reading that OFN had not yet adopted; OFN adopts that reading at the scope of §5.5.4 (IMP-O10-06/07).\nAction: received; O10-P3 fulfilled. The §6.2a readout entry is the representation-level readout contract OPEN-OFN-TRIAD-CLASS asked for; physical selection remains open. RRF v0.8.4 is a working standard; this is a reference, not a theorem import.")
ed("R21d", "21", "| $a\\in\\mathbb R\\mu$: $N_a=N$ through degree 5 ($g_a$ agrees with an element of $\\mathrm{Cent}(N)$) | `[ALG — SESSION]` |",
   "| $a\\in\\mathbb R\\mu$: $N_a=N$ through degree 5 ($g_a$ agrees with an element of $\\mathrm{Cent}(N)$) | `[ALG]` [provenance: SESSION] |")
ed("R21e", "21", "| `[ALG — SESSION; two independent exact computations]` (FMS 9×9 minor;", "| `[ALG]` [provenance: SESSION; two independent exact computations] (FMS 9×9 minor;")
ed("R21f", "21", "| `[ALG — SESSION; FMS symbolic P4 reported, OFN sampled verification]`. The universal κ statement",
   "| `[ALG]` [provenance: SESSION; FMS symbolic P4 source-reported; OFN sampled verification]. The universal κ statement")
ed("R25a", "25", "- **RF-O10-03 — ER-2B and the C19 loophole** :: `RTG_ER2B_CONSOLIDATED_STUDY` v0.3.1 (noncanonical), A.4, C09, C11/C20, C19\n\nThe A.4 cubic identity was reproduced by OFN. ER-2B's \"chirality attenuating\" (C11/C20) refers to absolute $|S|$ and does not conflict with relative attraction (§5.5.6). The C19 subfamily $\\tilde v=0$ is not excluded (OPEN-C19-L, §5.5.3).\nAction: noncanonical context only.",
   "- **RF-O10-03 — ER-2B and the C19 loophole** :: `RTG_ER2B_CONSOLIDATED_STUDY` at `er2b-v0.3` (noncanonical; SHA-256 `80669c69…a134`), A.4 (L74–97), C11/C15B, C20, C19\n\nThree uses, each checked at `er2b-v0.3`: (i) A.4 and C11/C15B with C20 at $\\sigma=1$ — on the closure plane $\\sum_e|w_e|^4=\\tfrac12N_{\\rm ch}^2-2S^2$ is exact for closed triples and $\\Delta_4S=-\\tfrac13N_{\\rm ch}S$ is the degree-four part of the six-step observable increment, not an exact finite-step law (both re-checked exactly by the two OFN co-owners); (ii) the C20 \"attenuating\" regime row refers to absolute $|S|$ and does not conflict with relative attraction (§5.5.6); (iii) the C19 family statement, for OPEN-C19-L (§5.5.3; the hand derivation is OFN's own). The v0.3.1 edition named in v0.10 is not in the repository: its identity `711e427a…81b4` stays source-reported (FMS v0.6.4) and its authentication is deferred. No whole-file equivalence between v0.3 and v0.3.1 is claimed.\nAction: noncanonical context only; nothing stronger that depends on ER-2B is used.")
ed("R28a", "28", "Action: notice N9 is answered at owner level when v0.10 is adopted; until then the session-level answer stands. N12 was not read for this draft.",
   "Action: notice N9 answered at owner level by v0.10 (retained). Later DYAD editions to v6.4.22 (OPEN 20 B-∞ existence, smooth chart, `DYAD-DEF-PRIMITIVE-MAP`) are received in IMP-O08-12, IMP-O10-04, IMP-O10-06/07 and §12.3 (notices N4, N6, N14).")

# ----------------------------------------------------------------------------------------------- §12 (rows 14, 16, 24, 28)
ed("R14g", "14", "| RECOG v0.3.20 | Mathematical statement text supplied; live header says freeze candidate | External final freeze/adoption record not supplied; REQ-O09-02 remains a release-verification request |",
   "| RECOG v0.3.20 | Mathematical statement text supplied; the DSN header's \"freeze candidate\" defers the hash to an external record | That record is `records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (`5c00f66d…9b55`); REQ-O09-02 fulfilled. v0.11 cites the RECOG RIDs at `recog-v0.3.26` |")
ed("R24a", "24", "| Session evidence for §5.5 and RF-O10-02. The last six were executed by both co-owners; scripts are held by the PI and the co-owners, not attached to the project |",
   "| Session evidence for §5.5 and RF-O10-02. The last six were executed by both co-owners. *v0.11:* eleven of the twelve, with the v0.10 release record, both draft builders, `release_ofn_v0_10.py` and Drafts 1–2, are on `upload/ofn-records/` (commit `c6fd574`, `SHA256SUMS.txt`, hashes equal to those printed here); `transported_chiral_pq.py` is held by neither OFN session (custody table in the v0.11 release record) |")
ed("R28b", "28", "| NUMGEN v1.20.7 §1.1 RF-06 | `SG-OFN-STATE`; `RTG-OFN-ALG-STAR-TOKEN-SHIFT` | Actual named use; full-state/no-birth distinction retained. Separate overly broad opening §1.1 imports still need the precise OFN definition RIDs and scope. |",
   "| NUMGEN v1.21 §1.1 RF-06 and three §1.1 DEF imports | `SG-OFN-STATE`; `RTG-OFN-ALG-STAR-TOKEN-SHIFT`; `RTG-OFN-DEF-RELATIONAL-CONTENT`, `-PHASE-GAUGE`, `-BACKGROUND-TIME` | Actual named use at source grade; the opening imports are narrowed to one DEF import per OFN RID (NUMGEN notice received). |")
ed("R28c", "28", "| RECOG v0.3.20 §7.1 and §2 R1/R5 | OFN v0.8 comparator/orientation disposition and selection questions | Source acknowledges OFN's conditional disposition; no physical OPA closure. |",
   "| RECOG v0.3.26 §2 R1/R5 | OFN comparator/orientation disposition and selection questions (receipts of OFN v0.8 and v0.10) | Source acknowledges OFN's conditional disposition; no physical OPA closure. |")
ed("R28d", "28", "| RRF v0.7 §2.3 guard | OFN non-spatial interpretation of Re W / Im W, presently cited with `RID unavailable` | Actual reference consumer, not yet an exact named-rank-RID import; propose owner linkage to `RTG-OFN-DEF-RANK-TYPING`. |",
   "| RRF v0.8.4 §2.3 guard; §6.2a | `RTG-OFN-DEF-RANK-TYPING` (non-spatial reading of Re W / Im W); `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT` (class-C model-contract row) | Actual named imports by RID. |")
ed("R07e", "7/28", "| TDR-G v2.12.13 | Earlier OFN references; no inspected XFER-O08-01 acceptance | Proposed updated consumer/custodian only for finding A; preserve pending status. |",
   "| TDR-G v2.12.14 §7, SG-14 | `RTG-OFN-ALG-STAR-TOKEN-SHIFT` (import, statement accepted); O0–O3 as context | Custody transfer XFER-O08-01 deferred by TDR-G to v2.13; the RID stays OFN's. |\n| Genesis v2.9 §6.3c, §7 IF32 | OFN §5.5 / IMP-O10-01 interface | Reference consumer; no OFN claim imported into Genesis. |\n| Dyadic v6.4.22 §7 | OFN imports `DYAD-THM-PRIM-CTR`, `DYAD-DEF-PRIMITIVE-MAP`, `DYAD-THM-FORMAL-Z6-GENERATOR`, Lemma F / F3, OPEN 3 RIDs, `DYAD-THM-SMOOTH-EMBEDDING`, `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | Dyadic notices N4 (map custody), N6 (`DYAD-THM-LOCAL-INVOLUTION-GERM`; received, no OFN import) and N14 (B-∞ existence) received in v0.11. |\n| Triadic v1.6.1 | OFN v0.9 (pinned by Triadic) | Triadic's repin is its decision; OFN half of pass two recorded in RF-O08-02. |")
ed("R16g", "16", "**CUST-O09-01 — primitive-map identity.** IMP-O08-12 keeps its Dyadic source lineage and an exact version/section with `RID unavailable`. Genesis v2.8.5 assigns `GEN-DEF-PRIMITIVE-MAP` to the same formula; no resolving owner record is supplied. Request a Dyadic/Genesis custody or alias decision. OFN neither invents a DYAD identifier nor borrows the GEN identifier to imply settled custody. The metric/invariance/linear-order identifier refreshes are separate.",
   "**CUST-O09-01 — primitive-map identity: answered.** Dyadic owns `DYAD-DEF-PRIMITIVE-MAP` (`dyad-v6.4.22` §1, §6.1); Genesis records `GEN-DEF-PRIMITIVE-MAP` as its alias (`gen-v2.9` §1); both resolve to the same formula. IMP-O08-12 carries the Dyadic RID; REQ-O09-04 is fulfilled.")
ed("R23e", "23", "`OFN_v0_9_PROGRAMME_AND_OWNER_SYNC_REQUEST.md` records the next authorized Programme v1.3 inventory refresh, actual consumers, the NUMGEN opening-import scope correction and RRF citation request. Programme v1.2 remains unchanged.",
   "Programme v1.3 (adopted) lists OFN v0.10 and names OFN §§5, 9 as the criteria home for OPEN-P0 and OPEN-P2B; the NUMGEN opening-import scope correction and the RRF citation request of `OFN_v0_9_PROGRAMME_AND_OWNER_SYNC_REQUEST.md` are answered (NUMGEN v1.21 §1.1; RRF v0.8.4 §2.3).")
ed("R14h", "14", "| **REQ-O09-02** | RECOG v0.3.20 final freeze/adoption record, exact source hash | Needed to describe that source as finally frozen/adopted; nonblocking while candidate provenance remains explicit |",
   "| **REQ-O09-02 — FULFILLED** | RECOG v0.3.20 final freeze/adoption record, exact source hash | `records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (`5c00f66d…9b55`; \"Fulfils REQ-O09-02\"), with its evidence qualification |")
ed("R12f", "12", "| **REQ-O09-03** | NUMGEN owner assignment of a dedicated L-BACKBONE theorem/result RID, with explicit confirmation of q_m, its observable/frame, sampling index and domain | Identifier and source-typing clarification; no regrading or reopening of the inspected ALG proof. IMP-O08-20 continues to use the identified DYAD contraction bound. |",
   "| **REQ-O09-03 — FULFILLED** | NUMGEN owner assignment of a dedicated L-BACKBONE theorem/result RID, with explicit confirmation of q_m, its observable/frame, sampling index and domain | `NUMGEN-RESULT-N5AS1-L-BACKBONE`; q_m typed as the block-sampled primitive Q_true (`numgen-v1.21` §6.6). IMP-O08-20 continues to use the DYAD contraction bound. |")
ed("R16h", "16", "| **REQ-O09-04** | Dyadic/Genesis disposition of CUST-O09-01 | Needed to resolve map-RID ownership; section-pinned map reference remains usable under Methodology §3.3 |",
   "| **REQ-O09-04 — FULFILLED** | Dyadic/Genesis disposition of CUST-O09-01 | `DYAD-DEF-PRIMITIVE-MAP` (Dyadic custody), Genesis alias recorded |")
ed("R08d", "7/8", "| **REQ-O09-05** | TDR-G endpoint-policy and XFER-O08-01 disposition | Needed for the corresponding physical-rule/custody claims; neither is inferred from NUMGEN's receipt |",
   "| **REQ-O09-05 — endpoint component FULFILLED; custody component deferred by the owner** | TDR-G endpoint-policy and XFER-O08-01 disposition | `TDRG-DEF-ORIENT` and SG-14 (`tdrg-v2.12.14`); XFER-O08-01 deferred to TDR-G v2.13, RID stays OFN's; the six-constraint list is not recovered (OPEN-OFN-2) |")

# ----------------------------------------------------------------------------------------------- Appendix B / C records (rows 2, 3, 21)
APPB = r"""

### Adopted v0.11 records (adoption pending)

**OFN11-C01 — `RTG-OFN-DEF-STANDARD-C` quantifier `[COR]`.** Old (`ofn-v0.10` §5.5.2): "Standard C holds if there is a nonempty $F$-invariant regime $\mathcal R$ on which $I_e=O(|r|^4)$ for every edge $e$". Reason: the singleton $\{0\}$ ($T(0)=0$, $F_\kappa(0)=0$, $I_e(0)=0$) and any invariant set bounded away from 0 satisfied the wording vacuously; the intended content is local at 0 and is what `RTG-OFN-ALG-RAW-STANDARD-C-NOGO` excludes. New: the positive-dimensional local $C^3$ invariant-manifold-germ test of §5.5.2 (uniform punctured-domain bound; declared carrier, readout, norm and clock; singleton, finite records and isolated trajectories excluded; not all edges need be nonzero). RID kept. Effect: the raw no-go and the FMS disposition are unchanged; non-manifold and finite-amplitude regimes are outside the test and need their own contract. Sources: owner disposition records and reconciliation of 29 October 2026.

**OFN11-C02 — test-class regularity amendment.** Old (`ofn-v0.10` §5.5.1): "Real-analytic laws form the admitted continuous FMS test class; this is not a universal requirement." New: real $C^\infty$ update germs, with real-analytic laws a distinguished subclass; each candidate states its realized regularity; Q6-REG stays local $C^3$. Reason: nothing in Q1–Q6 or the imported theorems needs analyticity, and the exactly transported class-C member is now a real $C^\infty$ germ (IMP-O10-06/07). Contract change, recorded for PI adoption; no physical regularity axiom.

**OFN11-C03 — status and notation.** The narrow-Q6 corollary carries the single conclusion status `[from: ALG]` (Methodology v1.4 §3.4; Genesis `[THM]` premises in *Depends on*; no promotion). In §5.5.4–§5.5.6 the chiral ratio and norm are written $\chi$, $N_{\rm ch}$ (v0.10: $\rho$, $N$); formulas unchanged.
"""
ed("R21g", "2/3/21", "\n\n---\n\n<a id=\"ofn-version-history\"></a>", APPB + "\n---\n\n<a id=\"ofn-version-history\"></a>")
APPC = r"""## Appendix C — Version History

### v0.11 — 29 October 2026 — DRAFT (stage-1 intermediate; adoption pending)
- **§5.5 [scientific/contract]:** class C consumes `DYAD-THM-SMOOTH-EMBEDDING` and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (IMP-O10-06/07): one five-row regularity table; real $C^\infty$ lock surfaces; class C "primary realized smooth mathematical candidate family"; analytic and physical realization open. `RTG-OFN-DEF-STANDARD-C` corrected (OFN11-C01); test class real $C^\infty$ (OFN11-C02); one κ table; narrow-Q6 `[from: ALG]`.
- **§§9–12 [receipts/pins]:** TDR-G v2.12.14 (Finding A statement accepted, custody deferred; REQ-O09-05 endpoint answered; owner RID map), NUMGEN v1.21 (REQ-O09-03), RECOG freeze record (REQ-O09-02), Dyadic map custody (REQ-O09-04), RRF §6.2a (O10-P3), Triadic v1.6.1 pass two; governing-editions line; Methodology v1.4 tag spellings.
- **RIDs:** six DEF RIDs registered for unchanged bodies (`RTG-OFN-DEF-ZERO-ORIGIN`, `-DISCRETE-REDUCTION-BOUNDARY`, `-CONTINUOUS-REPRESENTATION`, `-FINITE-DESCRIPTION`, `-DIST-ZN`, `-REDUCTION-TARGET`). No OPEN status changes.
- **Record:** `records/ofn/OFN_v0_11_RELEASE_RECORD.md`; predecessor tag `ofn-v0.10`.
"""
ed("R21h", "21", "## Appendix C — Version History\n", APPC)

# ----------------------------------------------------------------------------------------------- residual sites (rows 7, 9, 12, 21, 22)
ed("R09p", "9", "Dependencies: LEM-REACH; LEM-SPECCONS at three-node no-birth scope; OPEN-SPECCONS-STAR remains with TDRG.⟨BR⟩",
   "Dependencies: TDRG-ALG-LEM-REACH; TDRG-ALG-LEM-SPECCONS at three-node no-birth scope; OPEN-SPECCONS-STAR remains with TDRG.⟨BR⟩")
ed("R09q", "9", "impact ε in B_k∩(B_k+d), CONV-TICK.", "impact ε in B_k∩(B_k+d), TDRG-DEF-CONV-TICK.")
ed("R21i", "21", "`CAND` in these strings is an identity, not a status (Methodology v1.3).", "`CAND` in these strings is an identity, not a status (Methodology v1.4 §4.2).")
ed("R07f", "7", "| `RTG-OFN-ALG-STAR-TOKEN-SHIFT` | Registered OFN RESULT from ALG | XFER-O08-01 remains proposed to TDR-G; acknowledgment by another consumer is not custody acceptance |",
   "| `RTG-OFN-ALG-STAR-TOKEN-SHIFT` | Registered OFN RESULT from ALG | Statement accepted by TDR-G and used in SG-14 (`tdrg-v2.12.14` §7); custody transfer XFER-O08-01 deferred by TDR-G to v2.13; the RID stays OFN's |")
ed("R21j", "21", "| `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT` | Registered v0.10, OFN RESULT from THM + ALG |",
   "| `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT` | Registered v0.10, OFN RESULT; single status `[from: ALG]` in v0.11 (OFN11-C03) |")
ed("R22i", "22", "| `RTG-OFN-OPEN-TRIAD-CLASS` | Registered v0.10, OFN OPEN | Registered 19 Oct 2026 (O10-P6) |",
   "| `RTG-OFN-OPEN-TRIAD-CLASS` | Registered v0.10, OFN OPEN | Registered 19 Oct 2026 (O10-P6) |\n| `RTG-OFN-DEF-ZERO-ORIGIN`, `RTG-OFN-DEF-DISCRETE-REDUCTION-BOUNDARY`, `RTG-OFN-DEF-CONTINUOUS-REPRESENTATION`, `RTG-OFN-DEF-FINITE-DESCRIPTION`, `RTG-OFN-DEF-DIST-ZN`, `RTG-OFN-DEF-REDUCTION-TARGET` | v0.11 (adoption pending), OFN definitions; bodies unchanged from v0.10 §§1.3, 4.1, 4.6, 8 | Registered on adoption of v0.11 (seventeen definition RIDs in total) |")
ed("R12g", "12", "| NUMGEN v1.20.7 §9.1, NG-7 reference |", "| NUMGEN v1.21 §6.8 (NG-7A Foundations export) and §9.1 |")

ed("R07g", "7", "XFER-O08-01 remains proposed; the twenty inherited research records", "XFER-O08-01 then remained proposed; the twenty inherited research records")
ed("R21k", "21", "C2-B (visible `[ALG — SESSION]` grade in §5.5.7)", "C2-B (visible SESSION grade in §5.5.7)")
# ----------------------------------------------------------------------------------------------- round 2 (PR #112 review)
ed("R16i", "16", "  Reconciliation: Dedicated result ID located; separate map-definition custody remains unresolved.",
   "  Reconciliation: Dedicated result ID located. Primitive-map custody is resolved separately: `DYAD-DEF-PRIMITIVE-MAP` (Dyadic custody), with `GEN-DEF-PRIMITIVE-MAP` as the Genesis alias (IMP-O08-12; CUST-O09-01 answered, REQ-O09-04 fulfilled). The linear order-six result is distinct from map custody and from generator selection.")
ed("R21l", "21", "**Source and status.** Governing input: `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md` (SHA-256 `6e4fc3c3…564b1d`), accepted by both OFN co-owners on 19 October 2026. The `[DEF]` and `[RESULT]` records in this section are registered by the v0.10 adoption (O10-P2–P5, 19 October 2026).",
   "**Source and status.** Historical integration input for v0.10: `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md` (SHA-256 `6e4fc3c3…564b1d`), accepted by both OFN co-owners on 19 October 2026. The `[DEF]` and `[RESULT]` records in this section were registered by the v0.10 adoption (O10-P2–P5, 19 October 2026). The v0.11 changes to this section are governed by the joint owner reconciliation (`records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md`) and the v0.11 release record: the Standard C and test-class amendments are OFN11-C01/C02 (Appendix B) and the smooth-realization imports are IMP-O10-06/07.")
ed("R21m", "21", "| Single input for §5.5; co-owner handoff acceptance, not adoption |",
   "| Historical single integration input for v0.10 §5.5; retained evidence baseline, amended in v0.11 by the joint owner reconciliation and current imports; co-owner handoff acceptance, not adoption |")
ed("R03e", "3", "Physical-isolation scope: an invariant regime on which the interaction vanishes algebraically satisfies the mathematical contract; it does not by itself show that the surroundings are physically removed.",
   "Physical-isolation scope: on a regime that meets the manifold, nontriviality, domain and clock requirements above, $I_e\\equiv0$ for every edge satisfies the order-four bound. Algebraic cancellation alone establishes neither those regime requirements nor physical removal of the surroundings.")
# ----------------------------------------------------------------------------------------------- footer
ed("F01", "21", None, None, "footer")

# =============================================================================================== engine
def apply(base):
    s = base; log = []
    for (i, row, mode, old, new, count) in E:
        before = s
        if mode == "str":
            n = s.count(old)
            if n != 1: raise SystemExit(f"{i}: expected 1 occurrence, found {n}: {old[:90]!r}")
            s = s.replace(old, new)
        elif mode == "live":
            a = s.index(LIVE_END); live, rest = s[:a], s[a:]
            n = live.count(old)
            if n != count: raise SystemExit(f"{i}: expected {count} live occurrences, found {n}: {old!r}")
            s = live.replace(old, new) + rest
        elif mode == "block":
            a = 0; b = s.index("## Local Tag Aliases")
            old = s[a:b]; s = new + s[b:]
        elif mode == "footer":
            a = s.index("*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.10*")
            old = s[a:]
            new = br("*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.11*⟨BR⟩\n*DRAFT — stage-1 intermediate of v0.11, adoption pending; `ofn-v0.10` governs until adoption and tag.*\n")
            s = s[:a] + new
        log.append({"id": i, "row": row, "mode": mode, "count": count if mode == "live" else 1,
                    "old": old, "new": new, "old_sha256": sha(old), "new_sha256": sha(new),
                    "doc_sha256_before": sha(before), "doc_sha256_after": sha(s)})
    return s, log

def main(argv):
    if len(argv) != 4: raise SystemExit(__doc__)
    base = open(argv[1], "rb").read()
    if hashlib.sha256(base).hexdigest() != BASE_SHA: raise SystemExit("input is not the adopted ofn-v0.10 file")
    out, log = apply(base.decode("utf-8"))
    for e in log:
        if e["mode"] == "str" and out.count(e["new"]) < 1 and e["new"]:
            raise SystemExit(f"{e['id']}: new text not present in candidate")
    open(argv[2], "w", encoding="utf-8", newline="\n").write(out)
    json.dump({"base_sha256": BASE_SHA, "candidate_sha256": sha(out), "edits": log}, open(argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"edits: {len(log)}; candidate sha256: {sha(out)}; lines: {out.count(chr(10))}")

if __name__ == "__main__":
    main(sys.argv)
