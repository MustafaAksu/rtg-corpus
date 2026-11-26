# Note to the Number Genesis co-owners — current state and entry route

**Date:** 25 November 2026. Earlier version: 26 October 2026, in git history.
**From:** NUMGEN co-owner sessions (Claude; post-tag update by ChatGPT).
**Status:** [SESSION] working note. It is operational context only: not scientific authority, not an approval, and not recovered memory of earlier chats.

**Entry route** (Programme project instructions):
1. Read `CONVENTIONS.md` and this note.
2. Check yourself: the adopted tag and its release record, the open PRs, and `pipes/NUMGEN/`.

## 1. How we work

The full rules are in `CONVENTIONS.md` and Methodology v1.4 (`dsn/DSN_METHODOLOGY.md`, tag `methodology-v1.4`).

**Source.** The source is `dsn/RTG_NUMBER_GENESIS_DSN.md`. The governing edition is the latest `numgen-v…` tag together with its release record. The live file holds the current state only. Appendix A has one compact entry per edition; older history is at the tags.

**Release route.**
1. Work on a branch (`claude/*` for this session) and open a PR.
2. The other co-owner and the atlas owner review the change.
3. Write the release record.
4. The PI adopts.
5. The PI makes a merge commit (never squash) and the annotated tag.

**Stages.** One content stage suffices when the layout does not change. Layout compaction is a separate stage 2, checked by `tools/check_compaction.py`.

**Evidence and identifiers.**
- Evidence goes in `evidence/numgen/`.
- Held records are on the branch `upload/numgen-records`, now merged; see `records/numgen/NUMGEN_UPLOAD_HASH_CHECK_20261026.md`.
- Never invent hashes, RIDs or approvals.

**Cross-stream items** (`pipes/README.md`):
- Inbox `pipes/NUMGEN/`.
- The receiver sets `state` and `disposition`.
- A notice never creates adopted use.
- Validator: `python3 -I tools/pipes_index.py --check`.

## 2. Current state

| Item | Value |
|---|---|
| Governing edition | v1.22, tag `numgen-v1.22`, SHA-256 `36b31755c1bd73f1d5f69117c63b1556afacc18c2505e1b865b7a3adf512d40b`; release record `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md`; publication addendum `records/numgen/NUMGEN_v1_22_POST_TAG_20261124.md` |
| Release completion | PRs #374, #375, #377 and #380 merged; PI annotated tag verified. No later NUMGEN edition in progress in this checkpoint. |
| Work list for v1.22 | `records/numgen/ATLAS_ADVISORY_NUMGEN_SYNC_20261123.md` (rev. 2); owner disposition `records/numgen/NUMGEN_OWNER_DISPOSITION_SYNC_20261123_CLAUDE_20261124.md` (PR #374) |
| S1 evidence | `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md` (PR #375): P2 re-annotation of 158 witnesses under TDRG-DEF-ORIENT |
| Inbox | Eleven v1.22 dispositions recorded in `records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md`; their closure is merged via #380. Recheck live `pipes/NUMGEN/INDEX.md` at entry. |
| Outbound | Four items of 26 Oct closed by their receivers; seven v1.22 notices filed via merged #380. Filing does not imply receiver acceptance or adopted use. |

## 3. Open scientific frontier (unchanged by v1.22)

- **C7C-M.** The target is a non-degenerate composable three-stream witness and full-interface typed WD-DOM (OPEN).
  - M-4 stays on HOLD pending approval of a design/preregistration for the missing non-degenerate composable-chain witness (middle-interface and outer-pair admissibility). The P2 policy is answered. All 158 Census-1 TDR-G records are `(SWAP, P3)`; the two dyad records are separate. Finding the witness is the target, not a prerequisite to launching a properly authorized search.
  - Census-1 stays INCONCLUSIVE / INCONCLUSIVE.
  - A new evidence universe needs its own preregistration (Census-2).
- **C7B global breadth** is OPEN. DISC-3 is deferred.
- **N-4, N-6 and full NG-8** are OPEN.
- **φ* vs `C_D^ext`** stays OPEN as a comparison. No identification is claimed.

## 4. Next checkpoint

The v1.22 adoption, tag and post-tag closeout (#380, `3164c3d90dffa00c5052219c4c55b782968a0d6c`) are complete. Native exact-head and main trial-merge checks passed in Actions run `45561901189`; publication evidence is unchanged. Sync the Claude project and recheck the live queue at entry.

### ChatGPT co-owner — 25 November 2026

[SESSION] C7C-M design trail: PRs #383 (abstract design), #384 (Claude review), #386 (three-channel carrier), #388 (Claude review). A1/P1–P3 and #386 §§2–4 accepted as conditional mathematics. A2 (C_r) and A* (M_±/H_±) physical-admission proposals withdrawn after #388: same-source phase-offset/readout structure; no independent event admission. #386 §9 (commit `636e415426a4e07164783af038fa49597f28e4ef`) retains a mechanism control only; typed saturation follows from the stipulated key/carrier, not independent physical evidence. Its analytic mismatch bounds O_x(√N), and O_x(log(N+2)) for k=1,5, are independently ACCEPTED (conditional SESSION) in #388 §6 at `b7c69325d25886a30a2db702e84d3fde41f3afdc`, comment `7173714790`; the earlier P4 fixture was also engine-reproduced by Claude. #383 §8 (commit `381eeb7b697c2a8e1921854a6f0489506587331a`) records withdrawal without retracting A1/A3 conditional results. Next: owner-native event/support distinctions in TDR-G. #386 comment `7174411169` supplies a new analytic candidate invariant birth-free sector (N=24,k=1, four consecutive phase residues mod 6, distinct tokens 0/6/12/18) and three one-step feasibility controls; no triple-stream recurrence or physical event admission follows. PR #390 (`68bdd74a0ae2decb1bf54e4e0d2ac33fa8d9061e`) now contains the separate support-typing request and birth-free-sector offer, and Claude's exhaustive one-step check of 6,144 states (0 failures); NUMGEN readback ACCEPT SCOPED for filing, comment `7184558581`. Await PI-authorized merge; neither item is on main yet. Await TDR-G owner dispositions before any cycle search. Obtain TDR-G scope confirmation, triple co-realization and independent outer-pair provenance before new preregistration. No search. PI_PENDING: no adoption inferred; later design/campaign separately authorized. M4 HOLD; Census-1 INCONCLUSIVE / INCONCLUSIVE; DISC-3 DEFER.

## 5. Not asked

- No rerun of the N-5, C7A or DISC campaigns.
- No change to the C7C algebra or Census-1.
- No ALG→THM promotion by header edit.
- No new compaction or general regrading.
- No receiver-side changes to other streams' inboxes; only the seven declared outbound notices.

*END OF NOTE.*
