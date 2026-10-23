# RECOG v0.3.22 atlas advisory — reconciliation of the two owner dispositions

**Date:** 23 October 2026. **Prepared by:** Claude (atlas owner), for the PI. **Status:** working record. The atlas owner advises and does not decide; the PI decides the open points in §3.

**Inputs** (placed unchanged in `records/recog/`):

| Disposition | File | SHA-256 |
|---|---|---|
| [C-O] RECOG co-owner (Claude) | `RECOG_OWNER_DISPOSITION_ATLAS_ADVISORY_v0_3_22_COOWNER_CLAUDE_20261023.md` | `49f1eb206573fc4ca0abf1bd55c85fba935d1684b8b70816c2f92521ecf8e8bd` |
| [G-O] RECOG co-owner (ChatGPT) | `RECOG_ATLAS_ADVISORY_OWNER_DISPOSITION_20261023.md` | `be286088157f38c306af37bb275c9a31e2a329bfe8beba31bbaa56ffe5858b91` |

Both answer `records/recog/ATLAS_ADVISORY_RECOG_v0_3_22.md` (FINAL PROPOSAL v1.0) §3 and the five questions of the PI's cover message.

## 1. Agreed by both

- **Release shape:** one successor, proposed **v0.3.23** (the PI fixes the number), under Methodology v1.4. Stage 1 holds all corrections, status edits and identifier work; it records an intermediate hash. Stage 2 is layout-only compaction against that hash, with a movement map, `tools/check_compaction.py` and negative controls. A release record follows, then PI adoption, merge and tag.
- **Rows:** 21 accepted, 3 deferred or routed.
  - Tier A: FA-01 … FA-09 accepted. FA-01 is stage 2, the rest stage 1. FA-07 is substantially met by the recovery.
  - Tier B: FB-10 … FB-20 accepted. FB-19 is a notation line only; FB-20 is met, with follow-up in §8.
  - Tier C: FC-21 accepted. FC-22 and FC-24 are deferred, each with its missing premises named. FC-23 goes to GEN.
- **FC-21** becomes a separately reviewed block of new science inside stage 1.
  - It gets a new RID; [C-O] proposes `RECOG-THM-A1A-PHASE-EXISTENCE-U`.
  - It gets its own proof cell, checked against `dyad-v6.4.22` for the lift branch, the domain (block base points in $U$), the indexing and the amplitude inversion.
  - It gets its own review verdict and is listed as new science in the release record.
  - RECOG-RESULT-A1A-PHASE-EXISTENCE-NG and RECOG-RESULT-A1A-CD-AGREEMENT stay unchanged.
  - Not supplied: R9-free $C_2$, R9-free OPEN 21, R9 incompleteness, physical memory, starts in $U_T\setminus U$.
  - **Decoupling:** if FC-21's review is not finished when the maintenance rows are ready, v0.3.23 is released without it and FC-21 follows in its own release.
- **FB-14:** both repairs.
  - In place: raw frame $\approx41.27$, post-$H_2$ $\approx59.12$.
  - Correction record: the original sentence.
  - $|G|$ given exactly or with $\approx$.
- **FA-08:** RESULT tags reviewed block by block, with a per-block ledger in the release record. No blanket relabel and no grade promotion.
- **FB-16:** reference $j^6S_h=j^6R_0$ and the smooth involution at germ scope, with the advisory's "must not" list. R1 stays PARTIAL; RRF OPEN-A and OPEN-OFN-OPA stay open.
- **Extra stage-1 items** (both): R10 wording "CLOSED (v0.3.2) — delivered and accepted"; Dyadic v6.4.21+ tag forms; the five Dyadic line-number pins replaced by RID plus section; erratum E-0322-1; RF-1 fidelity task fulfilled, kept separate from notice state; VF-1 cites `DYAD-ALG-NF6-DEG10`.
- **Notices:**
  - G3-OFN and G3-RRF stay "prepared" until the PI confirms otherwise.
  - The v0.3.22 notices (N-D, N-NG, N-O/R/E) are prepared and unsent.
  - Dyadic N19/N21 are prepared, not received, and are used as input only.
- **v0.3.5:** the bundled file is the pre-freeze candidate. The frozen bytes `3ba74002…abd6` are recorded as missing (recovery list §3).
- **Research order:** FC-21, then R6 F5 (RECOG-internal scoping), then R4 or R3, whichever upstream interface opens first. The W1–W5 network feasibility work waits on RRF OPEN-B/E1. The PI ranks.
- **Census unchanged:** R1 and R3 PARTIAL; R4, R5 and R6 ACTIVE; R2 and R7–R11 CLOSED.

## 2. Same decision, different wording (no PI decision needed)

| Point | [C-O] | [G-O] | Reading for the build |
|---|---|---|---|
| FB-12, `E2C-ENG-SPLIT-REFINEMENT` | keep the identifier text, add the custody note "RECOG artifact"; no rename | mapping only by explicit custody ruling, no silent rename | [C-O]'s note is that explicit ruling |
| FC-23 | route to GEN | defer / route to GEN | route to GEN |
| W1–W5 timing | after F5 | in parallel, dependent on RRF | both: it cannot start before RRF moves |

## 3. Open points for the PI

1. **FB-13, R9 comparator incompleteness and the swap-odd ρ lemma.**
   - [C-O] proposes two new RIDs: `RECOG-THM-R9-COMPARATOR-INCOMPLETENESS` (§6.13a corollary, exported in §6.9, used by R6) and `RECOG-ALG-SWAP-ODD-RHO` (§6.4 lemma, the OFN-facing R1 sub-item). The rest are deferred or named as sub-statements.
   - [G-O] binds R9 incompleteness and the P2 corollaries as named sub-claims of their owning theorems. It allows a distinct RID only for an independent statement that is used externally, with owner approval.
   - Both rule out bulk creation, and both treat the P2 corollaries and the radial identity as sub-statements. The difference is whether these two claims get RIDs of their own. Both are cited outside their sections, so [C-O]'s reading meets [G-O]'s condition if the PI approves.
2. **How to label the G3 notice to RER.**
   - [C-O]: received 21 Oct (RER record); sent via the PI on or before that date; statement accepted; no new adopted use.
   - [G-O]: "recipient-reported until the routing record is reconciled".
   - The PI routed the notice. A one-line PI confirmation of the send date settles it. Please also give the actual state of G3-OFN and G3-RRF.
3. **F5 claim scope** (research, not release). [G-O] limits F5: a non-smooth or event-gated boundary signature is a sufficient intrinsic witness of write-through, not a proved necessary condition for every carrier. [C-O]'s target, "write-through requires a non-smooth or event-gated update on a registered carrier", is the stronger form. Recommendation: pose F5 with [G-O]'s scope and the stronger statement as its test question.

## 4. Build route

The RECOG co-owner session ([C-O]) offers to build stage 1 on `claude/recog-v0.3.23-stage1` with an assertion-gated script against `recog-v0.3.22`. That session has read-only repository access. Two ways forward:
- (a) the PI gives that session push access; or
- (b) the session hands the built files to the PI. The PI uploads them unchanged to `upload/recog-v0.3.23-stage1`, and the atlas session hash-checks them and moves them to the `claude/` branch.

The change-focused review of stage 1 is done by the other co-owner, plus the atlas owner for the advisory rows.
