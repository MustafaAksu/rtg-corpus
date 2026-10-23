# RECOG atlas-advisory cycle, v0.3.22 → v0.3.23 — summary

**Date:** 23 October 2026. **Prepared by:** Claude (atlas owner), for the atlas co-owner and the PI. **Status:** summary record. The owner documents govern: `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` at tag `recog-v0.3.23` and `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md`.

## 1. Outcome

| Item | State |
|---|---|
| Governing edition | **RECOG v0.3.23**, annotated tag `recog-v0.3.23` (tag object `9aa29594…`, merge commit `4edaa88`); file SHA-256 `0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a`, 281,915 bytes. Predecessor `recog-v0.3.22` (`0dcce9e4…bcd9`). Verified after tagging: the tag points to the merge commit, the file hash matches, and the stage-1 archive commit `97b0425` is reachable from `main`. |
| Adoption | PI, 23 Oct 2026, 17:57 +03:00, verbatim in release record §11 |
| OPEN census | unchanged: R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED |
| Existing RIDs | none renamed or regraded |
| New RIDs | RECOG-THM-R9-COMPARATOR-INCOMPLETENESS, RECOG-ALG-SWAP-ODD-RHO (FB-13); RECOG-THM-A1A-PHASE-EXISTENCE-U and RECOG-ART-A1A-EXISTENCE-U (FC-21) |
| New science | **FC-21:** $C_D^{\rm ext}$ exists on all of $U=\{0<Q_0\le\tfrac1{625}\}$ without R9 and without NUMGEN INF-1, with $C_D^{\rm ext}=-\tau\psi(Q_0^{-1})+\tau\sum_m(Q_m-\tfrac1{Q_0^{-1}+m})-\sum_mr_m$, from DYAD-THM-LPHASE-ROWA-REMAINDER. Verified by the co-owner review. It does not give R9-free memory constants or an R9-free OPEN 21. |

## 2. Sequence

1. **Entry note** to the RECOG co-owners on current state and the new working method (`RECOG_COOWNER_ENTRY_NOTE.md`, PR #15). Both co-owners reviewed RECOG independently before seeing the advisory. Their reviews agreed with the atlas on the census and on the R9-free route, and found five atlas misreadings in D3 (A1–A5, §5 below).
2. **Advisory:** `ATLAS_ADVISORY_RECOG_v0_3_22.md`, FINAL PROPOSAL v1.0 (PR #13). Two independent passes (Claude, ChatGPT) reconciled into 24 rows: Tier A 9, Tier B 11, Tier C 4, plus 4 routed items.
3. **Record and evidence recovery** (PR #14, #16, #17). The co-owner hand-over bundle (174 files, SHA256SUMS 174/174 OK) and PI uploads were placed unchanged under `records/recog/` and `evidence/recog/`. The inventory of the 137 hashes cited in v0.3.22 found:
   - 92 in the tree;
   - 19 earlier editions, kept in history only;
   - 2 current owner DSNs;
   - 24 not found.

   The PI's E2C production run matches the v2 certificate 29/29. The bundled v0.3.5 is the pre-freeze candidate; the frozen bytes are recorded as missing. Details: `RECOG_SOURCE_RECOVERY_LIST.md`, `evidence/recog/inventory/`.
4. **Owner dispositions** (PR #18). Both co-owners filled the §3 table: 21 rows accepted, FC-22 and FC-24 deferred, FC-23 routed to GEN. The reconciliation record's §5 holds the PI decisions:
   - both FB-13 RIDs are created;
   - notice states are left as they stand until a separate cross-stream notice structure exists;
   - F5 is posed with the narrower scope (sufficient witness, not a necessary condition);
   - every session has repository write access; v0.3.23.
5. **Stage 1** (corrections; Claude co-owner; PR #19). 116 assertion-gated edits, 22 checker gates and 22 negative controls, plus a claim-level audit at `dyad-v6.4.22` / `numgen-v1.20.8`.
   - Round 1 reviews: the co-owner (ChatGPT) gave STAGE 1 ACCEPTED WITH ONE LIMITED CORRECTION, with FC-21 VERIFIED. The atlas row check gave rows implemented as disposed, with A1 and A2 to correct.
   - Round 2 applied A1 (`[assuming: …]`), A2 ($S_h$ is an exact involution; commutation certified through degree 6) and G (the claim audit verifies quoted-statement presence in the current source; it is not a historical comparison). Intermediate `0b2d5109…bc76`, commit `97b0425`.
6. **Stage 2** (layout-only compaction). Candidate `771f87f2…bf9c`, 18.7 % smaller.
   - Operations: current-only header, compact Appendix A, R10 template left at the tag, one footer.
   - `tools/check_compaction.py` gained a declared study profile. The atlas regression on the DYAD v6.4.21 triple gave the same verdicts, and the DYAD harness still rejects 16/16. The RECOG controls reject 17/17.
   - Co-owner review: STAGE 2 MECHANICAL REVIEW ACCEPTED — FA-RECOG-01 PARTIAL.
7. **Adoption and publication.** A publication transform changed three status lines only. PR #19 was merged with a merge commit, then the PI created the annotated tag.

Every build and check step above was reproduced byte-exactly by the atlas owner (`ATLAS_ROW_CHECK_RECOG_v0_3_23_STAGE1.md`, PR #22).

## 3. What changed in RECOG (by advisory row)

- **Imports and pins:**
  - NUMGEN $D_M$ and INF-1 cited by RID at v1.20.8; A1a-G1 closed (FA-02).
  - Dyadic A1a imports cited by RID and section at v6.4.22, with the owner's v6.4.21+ tag forms; the five line pins are removed (FB-11).
  - §7 rows gain the Dyadic RIDs registered in v6.4.20 (FB-10).
- **Methodology v1.4** for the successor (FA-06). All 19 bare or combined `[RESULT]` blocks are paired per block, two of them split (FA-08). The missing $O(t^8)$ remainder is restored (FA-09).
- **Status and wording:**
  - SG-R10 keeps its guard, now with the certified R9 row bound and a $2C_7$ partial budget (FA-03).
  - The fixed-point flag is answered (FA-04).
  - Consumer register and N11 adopted use are current (FA-05).
  - Frame labels: 41.27 raw, 59.12 post-$H_2$; $\lvert G\rvert$ is given exactly (FB-14).
  - Frame scale cites DYAD-ALG-KP-FRAME-SCALE (FB-15).
  - $j^6S_h=j^6R_0$ and the smooth involution are cited with the full "must not" list (FB-16).
  - Bridge-lemma custody (FB-18); notation line (FB-19); §8 repository locations (FA-07, FB-20).
  - Extras: R10 wording; erratum E-0322-1; RF-1 fulfilled as a content state; VF-1 cites `DYAD-ALG-NF6-DEG10`.
- **Notices:** no notice state changed. The two `[from: …]` pairings on consumed RESULT RIDs are a normalization, notified with the release hash (PI decision on §7.3).

## 4. Carried open

| Item | Owner | Note |
|---|---|---|
| Live-file exception (release record §11) | RECOG | Historical blocks still in the live file: the R8 and R9 v0.3.2 specifications, the former R11 text with its `[OPEN]` sub-items, R7's closed "Active sub-items", the §7.1/§7.2 audit tables and the G2 sentence, the SG order. The next release separates them: a stage-1 correction first, then compaction. The former R11 `[OPEN]` sub-items come first. |
| v0.3.23 notices | PI routing | Dyadic, OFN, RRF, RER, NUMGEN (FC-21); with the release hash |
| Prepared, unsent notices | PI | G3 to OFN and RRF; v0.3.22 N-D, N-NG, N-O/R/E; Dyadic N19 and N21 to RECOG. These wait for the cross-stream notice structure. |
| Programme Overview | Programme | selected RECOG edition → v0.3.23 |
| Missing evidence | PI | 24 hash-cited items (`RECOG_SOURCE_RECOVERY_LIST.md` §2–§4). None is a certificate that a current theorem rests on. |
| Research | RECOG, PI ranks | R6 F5 (admissible event-gated carriers; sufficient-witness scope), then R4 or R3. W1–W5 waits on RRF OPEN-B/E1. FC-22 and FC-24 deferred with named premises. FC-23 is with GEN. |
| Routed | NUMGEN, GEN | GAP-LOCK Lemma 3 grading and the explicit-domain inputs (NUMGEN); the phase-moment retest (GEN) |

## 5. For the atlas (next refresh, v0.3)

- **Rebase D3 on `recog-v0.3.23`:**
  - the new RIDs and FC-21 (R-L1 is now owner science, no longer an atlas diagnostic);
  - the updated imports and the R10 wording.
- **Correct the atlas misreadings the co-owners found:**
  - **A1:** R-L5(i) said R1's premise is "satisfied"; it is only consistent with the smooth involution.
  - **A2:** 15/2 is an ingredient of an explicit L-BACKBONE constant, not the constant itself.
  - **A3:** CD-IDENTIFICATION is a candidate source for $\phi^*$, not its owner node.
  - **A4:** mark the H-NG / INF-1 edge as an atlas identification.
  - **A5:** R-L7 is partly stale.
- **Retire or close the D3.L5 diagnostics resolved by v0.3.23:**
  - R-P2 (NUMGEN repin);
  - R-T1 and R-T2 (partly; the live-file exception stays open);
  - R-S2 (frame label);
  - R-L1 (FC-21);
  - R-L3 (now FC-22, deferred).
- **Record the R6 F5 scope as decided:** a non-smooth or event-gated signature is a sufficient witness, not a necessary condition.

## 6. Process lessons

- The independent owner pre-review before the advisory was shared worked well. Two co-owners confirmed the main scientific opportunity (FC-21) and caught atlas errors without being anchored on the advisory.
- Hash-checked recovery first made the evidence rows (FA-07, FB-20) concrete rather than aspirational.
- Separating stage 1 from stage 2 kept every scientific edit reviewable. The reproduce-everything check by a second party caught two wording issues and one evidence-scope overstatement (G); none was a mathematical error.
- The compaction tool cannot move tagged text. Studies with history inside tagged OPEN blocks need a stage-1 separation pass before compaction. Plan for this in the next advisory for any study.
- Merge with merge commits whenever a movement map archives an untagged intermediate.
