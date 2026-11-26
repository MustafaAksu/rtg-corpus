# RRF S0 — reviewer verdict on PR #397

**Date:** 26 November 2026.
**Status:** [SESSION] / NONCANONICAL. Reviewer lane (Claude, independent reviewer / second co-owner). This is a source-custody verdict only: no scientific review, adoption, merge, tag, BASELINE edit or pipe disposition. The PI decides merge and any source-status question.
**Reviewed:** PR #397 `chatgpt/rrf-s0-source-custody`, exact head `44fac173b46489c90b3af6c17153c8c75632ab3c`, one commit, base `main` `43dabc5818b2dccba31030116e4ecd80570e7e35`. Criteria: `RRF_S0_REVIEWER_SOURCE_CHECK_20261126.md` §4 A1–A8 (this branch, `fcaaeac1`), plus CONVENTIONS §9 for the orientation note.

## Verdict

**ACCEPT SCOPED** — S0 source custody at head `44fac173`. A1–A8 are met. No head change is required. The notes in §3 are non-blocking.

Scope: this verdict accepts byte custody, identity mapping, authorization quotation and missing-source accounting. It does not accept or grade any scientific statement in the placed files, does not decide PRR v0.3 or GIIL status, and does not dispose of the two new pipe items.

## 1. Native checks (run in a full checkout of the exact head)

| Check | Result |
|---|---|
| `python -I evidence/rrf/scripts/check_s0_custody.py .` | exit 0; governing ×3, review diff A control, negative control, 17/17 placements (bytes, SHA-256, Git blob); `S0_CUSTODY_PASS 17` |
| `python tools/pipes_index.py --check` | `pipes OK: 185 items in 20 inboxes` |
| Reviewer route `python -I evidence/rrf/scripts/rrf_s0_regenerate_v084_diffs.py .` (#396) | exit 0; same two target digests |
| Cross-check against the #396 object scan (13,013 objects, independent of the PR's manifest) | all 15 original placements occur in upload custody at the same SHA-256; the 2 regenerated diffs occur nowhere as originals, as stated |
| Authorization excerpts (record §2) | 9/9 quoted strings found verbatim in the placed originals (whitespace and markdown emphasis normalised) |
| Protected paths `upload/ dsn/ noncanonical/ BASELINE.md` | unchanged against `43dabc5` |
| Merge simulation with #396 (`fcaaeac1`) and #394 (`39c42a33`), both orders | only conflict is the generated `pipes/GEN/INDEX.md`. Regenerating it with `tools/pipes_index.py` resolves it: `pipes OK: 197 items`, 18 GEN rows including both new items. Custody check and reviewer script still pass. |

## 2. A1–A8

1. **A1 — met.** Tag object, commit, blob, size and SHA-256 match §1 of my check. The v0.8.4 record is placed under its original name, and BASELINE is left to the PI.
2. **A2 — met.** All six adoption records are byte-identical. v0.8.2 is extracted from the *adopted* release package. Authorization wording is quoted as written, and no PI signature is inferred.
3. **A3 — met.** 37/37 is stated as digest-to-object links, not approval authentications. The two diffs are labelled "regenerated, digest-verified; not recovered original custody".
4. **A4 — met.** `build_r4_7_draft.py` is placed as `RRF_EDITOR_RESPONSE_TO_RER_PHASEA_v0_2_20261019.md`. `…v0_8_4_CANDIDATE.md` is placed as `…v0_8_4_REVISED_REVIEW_CANDIDATE.md`. The DYAD degree-ten check is left under DYAD custody in `upload/`; that is acceptable. All uploads are unchanged.
5. **A5 — met.** PRR v0.2 is recorded as the historical NONCANONICAL parent, with the digest cross-reference and the locator check. PRR v0.3 has its own row, is not a drop-in parent, and is left to the PI.
6. **A6 — met.** GIIL is identified by full digest, with the owner-side pin and the GEN v2.8.4 baseline stated. A GEN question and an RER finding are filed as proposed pipe items. Their wording leaves both dispositions to the receivers ("plausible, not established by RRF").
7. **A7 — met.** The QA JSON manifest, `PRR_RRF_REVIEW_v1.zip` and the original diff files are listed with the claims each one limits. The RRF §10 rerun gaps are explicitly not reassessed.
8. **A8 — met.** A native verifier is included and passes, as shown above.

## 3. Non-blocking notes

- **N1 — the verifier is pinned to this point in time.** `check_s0_custody.py` diffs protected paths from the checkpoint to `HEAD` and requires the `main` file to equal the tag. It will fail after any later release that touches `dsn/`, `noncanonical/` or `BASELINE.md`, or after an RRF successor. That is correct for S0. A successor edition should re-pin the verifier or scope it to the S0 commit, not read a later failure as a custody break.
- **N2 — orientation note.** The structure is accepted: one entry, a shared ENTRY block, two lanes, `PI_PENDING`, and links to the S0 record and manifest. At its next owner edit the shared part should add the §9 fields that are not yet explicit: tried-and-rejected approaches with reopening conditions (none yet is an acceptable entry), and the next one to three actions with acceptance criteria. Claude's lane is filled by a separate `claude/*` commit, not on the preparer branch.
- **N3 — README wording.** "(proposed under CONVENTIONS §9)" becomes stale on merge. It can be dropped at the next README touch.
- **N4 — merge order.** Whichever of #394 and #397 merges second needs `pipes/GEN/INDEX.md` regenerated by `tools/pipes_index.py`, not hand-merged. #396 has no conflict with either.

## 4. Gate state after this verdict

On the PI's merge of #397, S0 is **ACCEPTED SCOPED** at `44fac173`. S1 (source/consumer synchronization) and the scientific sequence the PI set may then open: BR-Q2 first, then OPEN-A, then OPEN-B → E1 → E2. This record opens none of them.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
