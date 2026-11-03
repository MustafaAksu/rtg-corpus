# Triadic v1.7 — post-tag read-back, pipes and notices

**Date:** 3 November 2026. **By:** Claude, Triadic co-owner. **Status:** working record (owner-run read-back). The release record `records/triad/TRIAD_v1_7_RELEASE_RECORD.md` is frozen at adoption and is not edited. Its *(to be filled)* fields are answered here.

## 1. Merges and tag (PI, 3 November 2026)

| Item | Value |
|---|---|
| Merges, each a merge commit pinned with `--match-head-commit`, in the planned order | #137 → `95ed2801` (05:26:50 UTC), #138 → `a450b09e` (05:26:53), #139 → `dae419d8` (05:26:56), #140 → `7568941d3d30a9091af2b63a28be9abf5d916d8a` (05:27:00) |
| Tag | `triad-v1.7`, annotated; it points to `7568941d3d30a9091af2b63a28be9abf5d916d8a`, the PR #140 merge commit and the `main` head at tagging |
| Tag message | "Triadic v1.7 — dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md SHA-256 506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a" |
| File at the tag | `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` SHA-256 `506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a` = release record = `main` |
| Not yet merged | the Atlas row-check records #141 and #143 (release record §9 step 1 lists them after #140) |

Before tagging, the PI checked the file hash at the merge commit (`git show "$M":dsn/… | sha256sum` printed `506f3403…e64a`). An earlier attempt had run the tag command with the literal placeholder `<merge-commit-sha>`. The shell rejected it ("No such file or directory"), so no tag was created; the push then failed with "src refspec … does not match any". Nothing was written.

## 2. Read-back (owner-run on `main` at `7568941`)

- **Stage 1.** `build_triad_v1_7_stage1.py`, run on `git show triad-v1.6.1:…`, reproduces `evidence/triad/v1.7/stage1_intermediate.md` (`b47d294d…a66a`) and `stage1_edit_log.json` byte-for-byte. The stage-1 checker gives gates ALL PASS and 16 controls ALL CAUGHT.
- **Stage 2.** `build_triad_v1_7_stage2.py` reproduces the candidate `2573961a…5c0d` and `movement_map.json` byte-for-byte. `tools/check_compaction.py` returns PASS.
- **Publication.** `release_triad_v1_7.py "3 November 2026"`, applied to the reproduced candidate, gives exactly the file on `main` and at the tag.
- **Records on `main`.** The co-owner dispositions (`f35f52e6…`, `5fffb199…`), the reconciliation (`3c551769…`) and the release record (`29ebfd46…eb6a7`; ChatGPT's release-integrity review `5747517764` computed the same hash).

## 3. `BASELINE.md`

The TRIAD row now reads v1.7, `506f3403…e64a`, OWNER (release record), tag `triad-v1.7`, with predecessor v1.6.1 `95340abe…451f` (`triad-v1.6.1`).

## 4. Inbox `pipes/TRIAD/`

`20261030-OFN-v0-12-adopted.md` is dispositioned (2026-11-02 · no action · reconciliation §5). There are no other items.

## 5. Notices filed (release record §6; row 12)

| Item | Kind | Content |
|---|---|---|
| `pipes/GEN/20261103-TRIAD-v1-7-adopted.md` | notice | v1.6 pin; v1.6.1 and v1.7 deltas; `[CAND]` imports noted as Genesis's grading |
| `pipes/GEN/20261103-TRIAD-p4-identity-question.md` | question | 𝒫₄ = 2dᵀBG₃,d not printed at `gen-v2.9`; blocks the §7.2 radial-polynomial repin |
| `pipes/GEN/20261103-TRIAD-birth-symmetry-grade-question.md` | question | `[THM]` in §6.6 versus `[ALG]` in §1 and §8 |
| `pipes/UVM/20261103-TRIAD-v1-7-adopted.md` | notice | v1.6 pin; v1.6.1 and v1.7 deltas |
| `pipes/PROG/20261103-TRIAD-v1-7-adopted.md` | notice | IF07/IF11 pin v1.6; no CN-05 disposition in v1.3 |
| `pipes/OFN/20261103-TRIAD-v1-7-adopted.md` | notice | C1 cites the OFN result as an interface constraint |
| `pipes/RRF/20261103-TRIAD-v1-7-adopted.md` | notice | §3.1 convention-only typing unchanged |
| `pipes/ATLAS/20261103-TRIAD-v1-7-adopted.md` | notice | A-4 refresh; open notes F-1, F-2, A-1; row 29 |

`tools/pipes_index.py --check`: OK. Filing a notice is a queue event, not acceptance; adopted use is read only from the receivers' ledgers.

## 6. Carried forward

These are unchanged from release record §7: F-1 (qualifier syntax), F-2 (status-summary length), A-1 (v1.6-era wording in the §2 T-6u record), A-4 (atlas refresh) and row 29 (DEFER, PR #113). The two Genesis questions hold one claim-level repin. They do not hold any Triadic statement.
