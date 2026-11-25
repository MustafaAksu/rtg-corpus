# Discrete Genesis (TDR-G) v2.12.15 — Release Record

**Status:** ADOPTED by the PI on 12 November 2026 (§11), on the bytes `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64`. The merge commits and the annotated tag `tdrg-v2.12.15` are still to be made; until the tag exists, the governing edition stays `tdrg-v2.12.14`.
**Date:** 12 November 2026
**Prepared by:** Claude, TDR-G co-owner session `claude01SKePJ` (branch `claude/tdrg-v2-12-15-stage1`).
**Edition:** v2.12.15, a scientific scope edition built in one stage. Methodology v1.2 stays as declared; there is no layout compaction and nothing is rerun. The Methodology v1.4 migration remains v2.13.
**Predecessor:** `RTG_DISCRETE_GENESIS_DSN_v2.12.14`, tag `tdrg-v2.12.14`, SHA-256 `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`.

Fields marked *(to be filled)* depend on steps that have not happened yet. Every hash below was computed on the branch files by `evidence/tdrg/scripts/fill_tdrg_v2_12_15_record.py`; none is typed by hand.

## 1. Authorization and reviews

| Step | Source | State |
|---|---|---|
| Inbox items | `pipes/TDRG/` items of 29 Oct, 30 Oct, 4 Nov, 11 Nov and 12 Nov 2026 | read at `main` `65491fa` |
| Owner records | `records/tdrg/TDRG_OWNER_INBOX_DISPOSITION_20261112_claude01SKePJ.md` (§§1–4; round 2, §7, after the ChatGPT review) | merged (PR #243, `e8d317d`) |
| ChatGPT co-owner | triage and review of 12 Nov 2026, relayed in the session; its agreement and its requested limits (N4 as a scope correction, TDR-6 PARTIAL, evidence scope) are recorded in §7 of the owner record | not a repository record |
| PI decision | "v2.12.15 bilimsel sürümü başlatılabilir"; "OFN v0.11 ve AZ v0.7 bildirimlerini `no action` ile kapatılabilir"; "PR 243 merge edildi" (12 Nov 2026, 16:37 +03:00, in the session) | given |
| Change-focused review | ChatGPT co-owner: `records/tdrg/TDRG_v2_12_15_CHATGPT_CHANGE_FOCUSED_REVIEW_20261112.md` on PR #250 (head `91d510a2`, open at the time of round 2); GitHub review `5875732026` on PR #248. Verdict CONDITIONAL PASS on the round-1 candidate `429a57f2…4f19`: R1 required, R2 nonblocking in the same round | conditions applied in round 2 (§3a) |
| Round-2 readback | ChatGPT co-owner, on head `9b82993` (DSN `1e35be54…2e64`): GitHub reviews `5876282524` and `5876326403` on PR #248; addendum §6 of the review record on PR #250 (head `70ed8e9b`) | PASS: R1 closed, including the owner's extension (E10, E13, E18); R2 closed. The addendum also gives the one-line reason the row check asked for: the $N=24$ pair has equal $D$ but different signed-class sets, so $\mathcal I(X)$ is not a function of $D$. The DSN bytes are unchanged. |
| Row check and rerun | atlas owner: `records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_12_15.md` and `evidence/atlas/rowcheck/tdrg_v2_12_15/` on PR #252 (head `8d47b1e7`, with a follow-up noting the condition and the recommendation met). The rebuild, the gates and the controls are byte-identical; the 32 edits are read against the decisions; the §6.13 proofs are checked by hand | ACCEPT FOR ADOPTION (atlas side), with one publication condition (PR not mergeable, `pipes/TDRG/INDEX.md`) and one recommendation (round-2 readback). The condition is met: `main` was merged into #247 and #247 into this branch, and the indexes were regenerated (§10) |
| Adoption | PI: "benimsiyorum" (12 Nov 2026, 18:39 +03:00, in the session), given on the candidate `1e35be54…2e64` after the row check and with the round-2 readback | given (§11) |
| Merge commits, tag `tdrg-v2.12.15` | PI | *(to be filled after the tag)* |

## 2. Identities

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v2.12.14) | `git show tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md` | `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392` |
| **Candidate v2.12.15** | `dsn/RTG_DISCRETE_GENESIS_DSN.md` | `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64` |
| Builder | `evidence/tdrg/scripts/build_tdrg_v2_12_15.py` | `e1332fece5f1ad2c14f647220d782cb1a59bfbd90801fb0c30638258935d3234` |
| Checker | `evidence/tdrg/scripts/check_tdrg_v2_12_15.py` | `df9b0195afdbf9d0f57639e8dc5fd0b42e3e85ba4140ebc103fb48ef4326d414` |
| Edit log (32 edits) | `evidence/tdrg/v2.12.15/edit_log.json` | `a3c79ba63e854e84172e411b584be9c2c32d188d5108730b3aca46d83f213cf1` |
| Checker output (gates) | `evidence/tdrg/v2.12.15/check_output.txt` | `ba1ffdb5d5ced586de65c72124b2cc6b30e846c0b9fcf63c946e327584b115b1` |
| Checker output (negative controls) | `evidence/tdrg/v2.12.15/controls_output.txt` | `6636140f139cc581e602baf1340de80ffbd340399b40e121874302f42957a6d0` |
| Owner token-law check v2 and output | `evidence/tdrg/inbox_20261112/owner_token_law_check_v2.py`, `…_v2_output.json` | `491cee3b30d9020899d1028b89ff5a67fb79fded6eead292005d2d7ac9b91151`, `acbc55dbcb17b769e7ec7db822e2a7b08521ec4850cbf90ab8ad5a8e9329dd84` |
| AZ source of §6.13 | `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` | `198d2f4af9ae338fec007874d003c755674ac90da087411c57c51d63714fb829` |
| Pinned engine | `upload/tdrg-records/genesis_mode_b_mc_v18.py` | `9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e` |

**Reproduce.**
1. `git show tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md > base.md`
2. `python3 -I evidence/tdrg/scripts/build_tdrg_v2_12_15.py base.md OUT.md LOG.json` writes the candidate (`1e35be54…2e64`) and the edit log.
3. `python3 -I evidence/tdrg/scripts/check_tdrg_v2_12_15.py base.md dsn/RTG_DISCRETE_GENESIS_DSN.md evidence/tdrg/v2.12.15/edit_log.json` runs the gates; add `--controls` for the negative controls. The checker needs the tags and commit `e8d317d` to be present; no branch name is consulted.

No publication transform is planned: the candidate carries no DRAFT marker.

## 3. Edits by decision

| Item / finding | Disposition | Edits | What changed |
|---|---|---|---|
| N4: star event domain (owner finding; ChatGPT review: a scope correction, not wording) | accept | E15, E16, E17 | TDRG-DEF-STAR states the domain the engines always used: a valid centre (≥3 pairwise non-adjacent defect neighbours); a single-star component has exactly one valid centre, any shape; only the centre and the newborn change. TDRG-DEF-MULTISTAR is stated with the same precision; CONV-TICK step 4 gives the precedence. The declared event domain is widened; no dynamics or result changes. |
| AZ token-alphabet offer (`pipes/TDRG/20261112-…`) | accept with change | E18, E19, E28 | New §6.13. Seven `[ALG]` results are registered as TDR-G results credited to AZ: event inventory (E), narrow-band classes, census law, birth injection, $n$-node birth-free conservation, not-closed counterexample, parent–child phase law. Also the owner check `[NUM]` and the artifact RID. The LEM-SPECCONS $n$-node conjecture is resolved. The Stage 1 campaign numbers are not included. |
| TDR-6 and OPEN-SPECCONS-STAR (owner record §7.2) | partial | E07, E09, E10, E13 | TDR-6 becomes ACTIVE — PARTIAL: its pairwise-multiset sub-item is resolved as a predictable-change law, conditional on the centre token and the census. OPEN-SPECCONS-STAR gets a current-status paragraph. SG-12 is updated. |
| OFN token-sum finding (`pipes/TDRG/20261029-…`) | accept with change | E08, E11, E12, E30 | SG-3, the TDR-6 row and Appendix B now say: $P$ is not conserved at births ($\Delta P\equiv-x$), is invariant under the declared gauge and under relabelling, and is not a gauge quantity. The SG-3 Violation clause is extended. |
| Programme v1.4 notice (`pipes/TDRG/20261104-…`) | accept | E27, E04, E22, E24 | The §7 export row `TDRG-EXPORT-DISCRETE-TRIAD` now names TDR-24A → 24B → 24C. Companion, context and pins move to Programme v1.4. |
| OFN v0.11 / AZ v0.7 notices | no action (closed, PR #247) | E14, E20, E21, E23 | The pins move to the current editions after checking that the imported statements are byte-identical: Finding A at `ofn-v0.10`/`ofn-v0.12`; `AZ-ALG-ANTIPODAL-LOWORDER` at `az-v0.6`/`az-v0.7`. The consumers table is updated. |
| Registry | — | E01–E03, E05, E06, E25, E26, E29, E31, E32 | Header, status summary, RID map rows, Appendix A entry, footer. |

## 3a. Round 2 — corrections from the change-focused review

The review verified the round-1 candidate (`429a57f2…4f19`, commit `e2db210`) and supported §6.13, the N4 scope and TDR-6 PARTIAL. It asked for two corrections. Both are applied by changing the texts of existing builder edits; the edit count (32) and the new RIDs (9) are unchanged.

| Review item | Edits | Change |
|---|---|---|
| **R1** (required): the candidate stated an unproven universal negative, "no purely relational quantity is preserved across births" | E09 (TDR-6 sub-items), E19 (§6.13 intro) | The sentence is replaced by what is proved: the full pairwise-advance spectrum is not preserved at births, and $D_{t+1}$ is not a function of $D_t$, so no closed update law computable from $D_t$ exists. The §6.13 intro now says that none of its statements closes TDR-6 or OPEN-SPECCONS-STAR. TDR-6 stays ACTIVE — PARTIAL. |
| **R1** (the reviewer's observation): the signed-class set $\mathcal I(X_t)=\{[\delta_i]_\pm\}$ is exactly invariant | E19 (TDRG-ALG-TOKEN-CENSUS-LAW (iii)), E09 (new TDR-6 sub-item) | Registered as item (iii) of the census law with its proof: no token count decreases, so no class disappears; a birth adds only $-x$, whose class is already present at the centre. It is a token-state quantity, unchanged by the declared phase gauge and by relabelling. Whether it meets the purely relational condition of TDR-6 is left undecided, so it does not close TDR-6. Credited to the review. |
| Consequence of R1 (owner) | E10 (OPEN-SPECCONS-STAR status), E13 (SG-12), E18 (LEM-SPECCONS generalization) | Three phrasings said that "an invariant of the full dynamics" is open; (iii) is such an invariant at token level. They now name the open question at spectrum level: a spectrum quantity preserved across births, or a law closed on the spectrum. |
| **R2** (nonblocking): the parent–child order statement needs its time quantifier | E19 (TDRG-ALG-PARENT-CHILD-PHASE) | Stated along the free orbit (hypothesis for every $j\ge0$): the separation stays in $\{N/2,0\}$ for all $j$ iff $4x\equiv0$. Already $j=1$ forces $2x\in\{0,N/2\}$, so the same holds on any window with at least one advance; a window with no advance imposes no condition. |

**Checker, round 2.** C6 also asserts that the R1 phrasings are gone, that the new statements are present and that the R2 quantifier is in place. C10 also checks the signed-class set on every tick of the sample; it is implied by the census law, so this is an independent recomputation, not a new test. A new negative control, K8, restores the universal negative and must be caught. No campaign is rerun; the owner token-law check and its numbers are unchanged.

## 4. Checks

**Gates** (`check_output.txt`): RESULT: PASS (11/11 gates) — C0 BASE; C1 BUILD; C2 REVERSE; C3 HISTORY; C4 RIDS; C5 TAGS; C6 CONTENT; C7 NUMBERS; C8 EVIDENCE; C9 SOURCES; C10 DYNAMICS.

**Negative controls** (`controls_output.txt`):

```
[CAUGHT] K1 K_{1,3}-only star text restored: failing ['C1 BUILD', 'C2 REVERSE', 'C6 CONTENT', 'C7 NUMBERS']
[CAUGHT] K2 'gauge artifact' restored in TDR-6: failing ['C1 BUILD', 'C2 REVERSE', 'C6 CONTENT']
[CAUGHT] K3 unlogged change: failing ['C1 BUILD', 'C2 REVERSE']
[CAUGHT] K5 one new RID declaration dropped: failing ['C1 BUILD', 'C2 REVERSE', 'C4 RIDS']
[CAUGHT] K6 Appendix A history edited: failing ['C1 BUILD', 'C2 REVERSE', 'C3 HISTORY']
[CAUGHT] K8 TDR-6 universal negative restored (R1): failing ['C1 BUILD', 'C2 REVERSE', 'C6 CONTENT']
[CAUGHT] K4 wrong number, consistent log: failing ['C7 NUMBERS']
[CAUGHT] K7 star map without centre flip: C10 FAIL
CONTROLS: PASS (all caught)
```

## 5. What the change touches

- **No result is recomputed or changed.** N4 states the domain under which every number was produced. §6.13 adds statements, and its numbers come from the owner check placed with PR #243.
- **Narrowed readings.** Two older phrasings are superseded, and both are recorded in the DSN:
  - any reading of "star" as $K_{1,3}$ only;
  - "$P$ is a gauge artifact".

## 6. Live-file exceptions kept on purpose

- The engine is not patched. Under SG-14, `largest_center` remains outside covariance (N1); it is unaffected by the token laws.
- Layout is untouched: the §2 TDR-24B overlays, the Appendix A order and the footer chain stay as they are (v2.13).
- The claim-specific historical pins (OFN v0.6/v0.7, Programme v1.1) stay.
- XFER-O08-01 custody stays deferred to v2.13.

## 7. Pipe items (`pipes/TDRG/`)

| Item | State on this branch | Disposition |
|---|---|---|
| `20261029-OFN-token-sum-gauge-label.md` (finding) | dispositioned | `2026-11-12 · accept with change · records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md` |
| `20261104-PROG-v1-4-adopted.md` (notice) | dispositioned | `2026-11-12 · accept · records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md` |
| `20261112-AZ-token-alphabet-law-offer.md` (offer) | dispositioned | `2026-11-12 · accept with change · records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md` |
| `20261030-OFN-v0-11-adopted.md`, `20261111-AZ-v0-7-adopted.md` (notices) | closed (PR #247) | `no action` |
| `20261112-AZ-v0-8-adopted.md` (notice; arrived on `main` after this branch was cut) | open | not part of this edition. The candidate pins `az-v0.7` on purpose; the cited `AZ-ALG-ANTIPODAL-LOWORDER` entry is byte-identical at `az-v0.8`. The notice also concerns the §7 AZ consumer row and the AZ identifiers `TDRG-AZ-STATIC-ZN-4Q` and `TDRG-AZ-EXPORT-BASELINE`; it is dispositioned after the tag or with v2.13 (PI decision) |

The three dispositioned items are closed after the tag.

## 8. Notices after the tag

Each notice is `kind: notice`, and filing one is a queue event, not adoption.

| Consumer | Notice contents |
|---|---|
| `pipes/OFN/` | SG-3 wording; Finding A repinned; TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED cites Finding A. |
| `pipes/AZ/` | §6.13 registered, credited; TDR-6 PARTIAL; the §6.2 citation at `az-v0.7`; no Stage 1 numbers adopted. |
| `pipes/PROG/` | The export row repaired; pin `programme-v1.4`. |
| `pipes/NUMGEN/` | TDRG-DEF-STAR scope statement (no effect on its panels); new RIDs. |

## 9. Size

| File | Bytes | Lines |
|---|---|---|
| v2.12.14 (adopted) | 178,909 | 1,387 |
| v2.12.15 candidate | 196,268 | 1,432 |

Net change: +17,359 bytes (+9.7 %), almost all of it the new §6.13 and the TDRG-DEF-STAR statement.

## 10. Steps after adoption

| # | Step | Who | State |
|---|---|---|---|
| 1 | Change-focused review | ChatGPT co-owner | CONDITIONAL PASS (PR #250); R1 and R2 applied, §3a |
| 2 | Row check and rerun | atlas owner | ACCEPT FOR ADOPTION (atlas side), PR #252; publication condition met |
| 2a | Round-2 readback | ChatGPT co-owner | PASS (reviews `5876282524`, `5876326403`; PR #250 §6) |
| 3 | Adoption decision (§11) | PI | given, 12 Nov 2026 |
| 4 | Merge commits (not squash): #247, #250, #252 (the records cited in §1), then this PR | PI | *(to be filled)* |
| 5 | Annotated tag `tdrg-v2.12.15` on the merge commit of this PR, with the candidate SHA-256 in the message | PI | *(to be filled)* |
| 6 | `BASELINE.md` TDRG row | this branch: row entered | entered |
| 7 | Notices (§8); close the three dispositioned items | TDR-G co-owner, after the tag | *(to be filled)* |

## 11. Adoption decision

The PI adopts Discrete Genesis v2.12.15 on 12 November 2026: "benimsiyorum" (18:39 +03:00, in the session).

- **Bytes adopted:** `dsn/RTG_DISCRETE_GENESIS_DSN.md`, SHA-256 `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64`, 196,268 bytes. These are the bytes of the candidate as built and checked; no publication transform.
- **Basis:**
  - the PI's decision to start the edition (16:37);
  - the ChatGPT co-owner's change-focused review, CONDITIONAL PASS, with R1 and R2 applied in round 2 (§3a);
  - the atlas owner's row check, ACCEPT FOR ADOPTION, with its condition met;
  - the ChatGPT co-owner's round-2 readback, PASS.
- **Status after adoption:** TDR-6 stays ACTIVE — PARTIAL. Whether the signed-class set is a purely relational observable stays open.
- **Governing edition:** this edition governs from the annotated tag `tdrg-v2.12.15` on the merge commit of PR #248. Until then `tdrg-v2.12.14` governs.

## 12. Open items carried forward

- **TDR-6:** whether the signed-class set $\mathcal I(X)$ (TDRG-ALG-TOKEN-CENSUS-LAW (iii)) meets the purely relational condition, and whether any further purely relational invariant exists across births.
- **OPEN-SPECCONS-STAR:** a spectrum-level invariant, or a law closed on the spectrum, across births; and which centre tokens fire.
- **N4 follow-up:** the share of non-pure single-star events in the canonical scans is not measured. It needs only a log reading, no rerun, and can be done in a later campaign.
- **Mechanism of the AZ Stage 1 effect:** design only (PI decision); not carried to TDR-26.
- **v2.13:** Methodology v1.4 migration and compaction; XFER-O08-01 custody; `largest_center` with TDR-19.
