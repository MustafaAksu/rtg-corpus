# RECOG A1a scientific cell draft v0.4 — independent release-readiness review

**Date:** 20 October 2026  
**Disposition:** `[SESSION] SCIENTIFIC CELL REVIEW ACCEPTED — RELEASE-DRAFT INTEGRATION AUTHORIZED FOR PREPARATION; FINAL ADOPTION NOT AUTHORIZED BY THIS REVIEW.`  
**What was reviewed:** standalone A1a scientific cell, **not** an integrated RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22 release candidate. No RID is registered, no adopted DSN is edited, and no owner/adoption decision is exercised.

## 1. Source manifest and evidence coverage

| Source | SHA-256 | Scope actually read/checked |
|---|---|---|
| `RECOG_A1A_CELL_DRAFT_v0_4.md` | `117584032f85ed89b404931ccdba1d5abf9c66e0740833dfe2fdbe129f50f4f7` | All 238 lines; all claims, G1/G2/E2 changes |
| `RECOG_A1A_CELL_DRAFT_v0_3.md` | `febed7f985f6e19b35b572c0ac329777e342ebe3d15388cc7c04d6e934009562` | Exact unified diff v0.3 → v0.4 |
| `RECOG_A1A_CELL_DRAFT_v0_3_RECEIVING_REVIEW_20261020.md` | `d9b20aea8303833e1b7abe5b70f5776c135efab32b2ee9a601784b87698d27a5` | G1/G2 prior disposition |
| `RECOG_A1A_E2_OPEN21_SOURCE_CHECK_v6_4_18_20261020.md` | `941f42d6273f707bb161c24bd7e753c12acacda991dd29ff4050cbdcbfa6126e` | Full E2 source-check record |
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_18.md` | `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d` | §6.14, primitive P4 form and OPEN 21 statement/rows; not entire DSN or certificate replay |
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_16.md` | `33c14c5cc27625c17a2b78be74e070ae61b5c7399ded49a1538098735ab559e0` | Imported PRIM-CTR, NF-INV, P4-0, offset bounds, T1/T2 as previously reviewed; not whole new audit |
| `RTG_NUMBER_GENESIS_DSN_v1_20_7.md` | `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` | INF-1 / C4 owner statements and previous provenance, not a new certificate rerun |
| `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md` | `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` | Adopted R9 and §7.2 N13 state; proposed RID collision check |
| `DSN_METHODOLOGY_v1_3.md` | `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e` | §§3.3–3.4, 4.3–4.4, 8.1, 12, 13.1 |

The exact installed Dyadic v6.4.17 bytes were **not** inspected in this review. Dyadic v6.4.18 §6.14's equality to v6.4.17 remains owner-reported; it is not a premise of the current v6.4.18 E2 pin.

## 2. Change-boundary audit: v0.3 → v0.4

`[SESSION]` The unified diff contains publication/provenance changes only; no scientific formula, proof grade, model hypothesis, or claim domain was changed.

- **G1 — conditional pass for draft work.** Both NUMGEN imports retain `RID unavailable` and their two local tracking keys `A1A-NG-D-DEF`, `A1A-NG-INF1`. The owner source and statement are unambiguously identified; no foreign RID is invented. **Governance remains unresolved for release** (see §4).
- **G2 — PASS.** A separate v6.4.18 §6.14 P4 primitive-variable import includes the exact inherited qualifier `[ALG — formal second order; remainder not certified]`, states `P_{W2}=-Δ₂+DΔ₁[h₂]`, and does not claim that the formal remainder has been certified there. The independent certification is sourced exclusively to the OPEN 21 theorem.
- **E2 — PASS at source-statement fidelity.** OPEN 21 pinned to adopted v6.4.18, explicit full SHA-256, §6.14 lines 843–850; P4 primitive form lines 806–809. `K'_A=3951/1000`, `K'_B=971/250`, `C_{2,A}=517`, `C_{2,B}=163`, `(256/225)^2`, chart disks, primitive domains and R9 condition match the source. The provenance note distinguishes the unverified v6.4.17 byte comparison. The P5 28-gate certificate and R9 Arb certificate were *not* rerun; E2 is not a recertification.

## 3. Scientific claim/grade check

`[SESSION: reviewed against the named adopted source claims]`

| A1a claim | Proposed status | Disposition | Essential scope |
|---|---|---|---|
| C1 branch / lift alignment | `[THM]` | PASS | Postulated `T`, certified primitive invariant six-phase tube, starts in `U` |
| Reciprocal amplitude and `M Q_M → 1` | `[THM]` | PASS | `0<Q_0≤1/625`, Dyadic PRIM-CTR; no NUMGEN tube needed |
| Finite-block identity | `[ALG]` internal | PASS | `M≥1`, local extension `D_M^U` |
| H-NG ⇒ phase-limit existence | `[THM] [assuming: H-NG]` | PASS | Hypothesis is an assumed limit, not claimed as proved on all `U` |
| (a) independent-existence NUMGEN application | `[RESULT] [from: ALG]` | PASS | `U∩U_NUMGEN`, selected generator `T` under OPEN-P0; **no R9** |
| (b) `C_D^ext=τ log Q_0−M_W` | `[THM]` | PASS | Explicit `U`; R9 is discharged using RECOG's adopted R9 theorem and imported Dyadic T1/T2 |
| (b′) equality to NUMGEN `C_D` | `[RESULT] [from: ALG]` | PASS | Only `U∩U_NUMGEN`, using owner INF-1 |
| (c) two-row quantitative bound | `[THM]` | PASS for inherited source and logical combination | Dyadic v6.4.18 OPEN 21, R9, owner row A/B profiles not mixed; **no P5 certificate replay** |

The eight proposed RECOG A1a RIDs are distinct and none collides by exact text with adopted RECOG v0.3.21. This collision check is not a registration action. Nothing here transfers to comparator `C_W^(h)`, event recovery, or any A1b/A1c result. R6 remains ACTIVE.

## 4. One outstanding governance issue: exact Methodology §3.3 interpretation

`[OWNER: DSN Methodology v1.3 §3.3]` The canonical missing-owner-RID template explicitly says `Owner RID: none in the inspected source; dedicated RID requested`, then calls the `RID unavailable` use **"a declared exception with unresolved identifier governance"**. This is a *temporary, explicitly allowed form*, not a fully settled owner identifier.

`[SESSION]` The v0.4 sentence `a deferred governance decision; no method exception is claimed` reports the editor's intent but can be read as denying that Methodology itself calls the temporary form an exception. The further claim that the missing-RID import **"satisfies Methodology §3.3 through its RID unavailable form"** is only true subject to the template's *unresolved governance/request* provision; it must not be read as final closure.

**Publication-resolution alternatives** (no invented RID):
- Log a dedicated RID request to NUMGEN with the owner's decision to defer/decline, and retain the `RID unavailable` tracking keys pending a future exact repin; **or**
- Obtain a recorded Methodology-steward/PI interpretation explicitly allowing a deferred request at this release, and name the continuing temporary exception and responsible owner in the issue ledger.

A mere wording change to `no exception claimed` is not sufficient by itself for final conformity. This is **not a mathematical blocker**, and it need not prevent preparing an integrated draft. It is a **release-signoff governance gate**.

## 5. Release preparation versus adoption

**Review recommendation: authorize preparation of one integrated `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22_DRAFT_r1.md`, not its adoption.** Use adopted v0.3.21 as the immutable base and incorporate the v0.4 cell as new science with its eight *proposed* RIDs. Before any release approval:

1. Resolve or explicitly approve the temporary NUMGEN missing-RID exception as above; record the issue ID, owner and disposition.
2. Integrate the scientific cell into the **canonical** §6, with resulting table-of-contents and anchors checked; create fully versioned import rows in §7, the E2 and C1/A1a artifact records in §8, provenance in §9 and Appendix A entry. Add applicable §1 and §5 notices if these new claims are summarized or exported. Preserve exact existing R9 and R6 statements.
3. Update §7.2 N13's *three independent fields*: receipt; release verification (v6.4.17 reviewer-passed **owner-reported**, not report independently read); **new usage** of the v6.4.18-verified OPEN 21 statement in A1a only once that cell is adopted. Do not convert a receipt or a source check into a proof rerun.
4. Run a separate **integrated-release** review: manifest/base hash, exactly scoped scientific delta, import and RID consistency, old RIDs unaltered, cross-references, negative checks, and all source/certificate evidence limits. Record PI/authorized owner adoption separately if and only if approved.
5. Keep G3-OFN, G3-RRF and G3-RER dispatch records truthful: still unsent; do not mark delivery by editing an issue ledger. Their historical v0.3.21 notices and any new release-notification obligations remain separate.

**Final review verdict:** `SCIENTIFIC CELL ACCEPTED; E2 PASS; CANDIDATE INTEGRATION MAY START; RID GOVERNANCE AND INTEGRATED-RELEASE VERIFICATION OUTSTANDING; NOT ADOPTED.`
