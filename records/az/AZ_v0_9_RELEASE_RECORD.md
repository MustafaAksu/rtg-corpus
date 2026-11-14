# AZ v0.9 — release record (DRAFT; candidate built, not adopted)

**[SESSION] Not adopted.** `az-v0.8` governs until the PI adopts this edition, the record is completed, and the PI merges and tags. Prepared by the AZ co-owner (Claude), 12 November 2026; owner synchronization to `tdrg-v2.12.15` added on 14 November 2026 (§2a).

**Authority.** PI, 12 November 2026, 16:54 +03:00, project conversation, verbatim: "Stage 1 sonucunun `[NUM diagnostic]` olarak bir sonraki sürüme girmesini ve Stage2 çalışmasının başlamasını kabul ediyorum." — the Stage 1 result of Action 1 enters the next AZ edition as a `[NUM diagnostic]`. This is the separate PI decision that the outcome rule requires (rule confirmed by the PI on 12 Nov 2026; `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md` §11 item 3): *a validated, supported Action 1 contrast is eligible for a PI-approved `[NUM diagnostic]` entry within AZ Level A, with its exact simulation scope and provenance; it is offered to TDR-G for owner disposition; it does not by itself close AZ-OPEN-PROMO, promote AZ maturity, or become an adopted TDR-G claim.* The decision to enter the result is not yet the adoption of this edition.

## 1. Bytes and how to rebuild

| | File | SHA-256 | Bytes |
|---|---|---|---|
| base | `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` at tag `az-v0.8` | `146fcc2837f69e3d6a4fd626d29b5b038c7948c239eaedf7e55b57e74dd0ee76` | 89,039 |
| candidate as first submitted (commit `4ea9d2f`; reviews `5876303497`, `5877247214`) | same path | `24f25f70361d8159f629f555bc8207cc8cc285b34e74a775e2a6a4dfc2e05ec7` | 96,598 |
| candidate after the first two reviews (commit `e51fa3e`; readback `5890500279`) | same path | `4fac5f517712f93543e4c09a05c8c28cdc3a7c57cb5e8992ff5c97d5fdd9c0a2` | 97,620 |
| **candidate after the owner synchronization (DRAFT)** | same path on this branch | `8fc940797089c9627a9e75f0108cc0fce9af4d28d282d1afdef4b483c0ea6c29` | 100,945 |

```bash
python3 -I evidence/az/v0.9/build_az_v0_9.py --out /tmp/c.md --log /tmp/l.txt
sha256sum /tmp/c.md dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md        # equal
git diff az-v0.8 -- dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md        # the whole delta
```

One content stage, no compaction (Methodology v1.4 §13.6 asks for two stages only when a release also compacts). The builder reads the base from the tag, asserts its hash and the hashes of the registration package and of the campaign output, applies 35 exact-once edits (`evidence/az/v0.9/edit_log.txt`; the block is `evidence/az/v0.9/block_4_2_1.md`) — 14 for the diagnostic, 21 for the owner synchronization of §2a — and asserts that every base line not named in an edit is unchanged and in order: 577 of 602; seven lines replaced (title, *Document status*, *Supersedes*, the §4.2 heading, the §4.2 *Ownership* line, the §8 TDR-G heading, footer), eighteen edited in place.

## 2. What changes

| Edit | Where | What |
|---|---|---|
| S4.2.1 | new §4.2.1, at the end of Thread B | **The diagnostic block.** `[NUM diagnostic]` `AZ-NUM-TOKRES-S1`, with scope and convention qualifiers; the statement; the four registered contrasts with their intervals, discordant pairs and readings, copied from the report §5 (erratum N1 applied: PC3 "Bonferroni-adjusted"); the controls; what the statement is and is not; evidence |
| S4.2-status | §4.2 status line | one sentence: one item of the thread is owned by this DSN |
| S4.2-head | §4.2 heading | "(bridge-candidate only)" → "(bridge-candidate family; one AZ-owned diagnostic)" (review correction); the section number is unchanged |
| S0.1-row | §0.1 routing table | one row: owner, grade, not a TDR-G result, not a bridge-candidate |
| S0.2-B | §0.2, Thread B bullet | current-state readout of the diagnostic |
| S1.1-crit | §1.1 success criterion | the status stays "not met"; one sentence names the diagnostic and the outcome rule that limits it |
| S5-row | §5 high-risk ledger | one row with the forbidden overclaims |
| S9 | §9 | artifact entry `AZ-ART-TOKRES-S1` with hashes and evidence states |
| AppA | Appendix A | v0.9 entry |
| H-title, H-status, H-supersedes, H-summary, F | header, footer | edition identity (DRAFT), predecessor `az-v0.8` with its hash, one sentence in the status summary |

New identifiers: `AZ-NUM-TOKRES-S1`, `AZ-ART-TOKRES-S1`. None removed. One pin changes: TDR-G `tdrg-v2.12.14` → `tdrg-v2.12.15` (§2a); `dyad-v6.4.24` is unchanged and governs per `BASELINE.md`.

## 2a. Owner synchronization to `tdrg-v2.12.15` (14 November 2026)

**Why.** TDR-G v2.12.15 was adopted and tagged on 12 Nov 2026, after this candidate was first built (owner notice `pipes/AZ/20261112-TDRG-v2-12-15-adopted.md`): it accepted the AZ offer with change and registered seven `[ALG]` results in its §6.13, credited to AZ; it did not adopt the Stage 1 campaign or its numbers. The candidate's phrases "offered to TDR-G" and its TDR-G pin were stale for current use. Review `5890500279` asks for one content-stage synchronization before adoption.

**Comparison of the owner statements** (`evidence/az/v0.9/owner_sync_check.py`, output stored; both editions read from their tags with asserted hashes; `EV-SRC-READ`, no owner artifact run): of the 20 owner identifiers cited in the §8 IMP-B rows, the defining block of 19 is byte-identical in the two editions and stands under the same section heading; `TDRG-ALG-LEM-SPECCONS` carries an owner `[COR]` to its generalization sentence; `TDRG-DEF-ORIENT` (cited in §4.2.1) is byte-identical. The whole owner file differs in 29 removed / 74 added lines between the two tags; the statements AZ quotes about TDR-24 and the bulk scaling fit are not among the changed statements (the one changed row that names TDR-24D/F restates that they are closed at the mechanism level).

| Edit | Where | What |
|---|---|---|
| Y-companion, Y-0.1, Y-0.2, Y-4.2-own, Y-5, Y-8-head | header, §0.1, §0.2, §4.2, §5, §8 heading | live owner pin `tdrg-v2.12.14` → `tdrg-v2.12.15`; the §0.1 row also names the token laws |
| Y-IMPB | §8 clause IMP-B | verification state (read at v2.12.14 for v0.7; compared with v2.12.15 for v0.9: 19 of 20 identical, one `[COR]` followed, two rows new) and synchronization state |
| Y-r1 … Y-r10b | §8 rows | edition in the source field (and in two row texts that name the edition) → v2.12.15; statements unchanged |
| Y-r6-cor | §8 row `TDRG-ALG-LEM-SPECCONS` | follows the owner's `[COR]`: the `n`-node birth-free statement is proved (`TDRG-ALG-SPECCONS-N`); across star blow-up the update is exact but not determined by the spectrum; a spectrum-level invariant of the full dynamics is open (`TDRG-OPEN-SPECCONS-STAR`) |
| Y-rows | §8, two new rows | `TDRG-ALG-EVENT-INVENTORY` / `-TOKEN-CENSUS-LAW` and `TDRG-ALG-PARENT-CHILD-PHASE`, with the owner's scope tags and hypotheses and the local use in §4.2.1 |
| block (four phrases) | §4.2.1 | `[conv:]` keeps the edition pinned when the runs were made and adds that `TDRG-DEF-ORIENT` is unchanged at v2.12.15; the token law and the phase law are named as owner results at their point of use; "offered to TDR-G" replaced by the owner's disposition; one sentence that TDR-G did not adopt the diagnostic |
| AppA | Appendix A, v0.9 entry | two sentences on the synchronization |

**Kept deliberately.** The file name `tdrg_orient_v2_12_14.py` and the engine and orientation hashes in §9 (the bytes the runs used); the `[conv:]` edition of the runs; the history entries of v0.7 in §10 and Appendix A; the registration, the report and the Stage 1 evidence (not rewritten). **Not changed:** `AZ-NUM-TOKRES-S1` — owner, numbers, intervals, readings, grade, scope; the maturity level; the OPEN registry. The token laws are cited, not graded here, and are not said to explain the tail.

## 3. What the edition does not do

- No change of the maturity level, of the OPEN registry or of the milestones; AZ-2 stays "attempted, negative-clarifying" — it concerns a graph/transfer-zeta observable, and the new diagnostic is not one.
- No mechanism, no `N`-scaling, no statement about TDR-26; no relation to the Hashimoto `4|q` rule or to Dyadic/DZT `q = 4` (SG-AZ-3, SG-AZ-7, SG-DZT-1).
- The algebraic statements of the registration (token-alphabet law, parent–child phase law) are **not** entered as AZ results: TDR-G accepted the offer with change and registered them as its own at `tdrg-v2.12.15` §6.13 (`pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md`, closed 12 Nov 2026); v0.9 cites them in §8 as owner results (§2a).
- Nothing from Stage 2: its pilot is exploratory and running separately (`records/az/AZ_TOKEN_RESONANCE_STAGE2_PILOT_PLAN.md`).
- §10 is unchanged (as in v0.8).

## 4. Points for the change-focused review

1. **The numbers.** Every figure of the table in §4.2.1 against the report §5 and the stored analysis outputs `upload/az-token-resonance-stage1/analysis_S1-C1.txt` and `analysis_S1-C2.txt`.
2. **The scope qualifier** against the report §7 and the registration: engine and profile, policy, cells, four initial nodes, horizon, cap, endpoint.
3. **The controls sentence**: the label permutation is a control of the `N = 120` cell only (400 permuted runs); sham and detuned comparisons are restricted to draws whose native slot token is non-resonant, margin ±0.025; in both cells.
4. **"Causes" is not used**; the block says "raises the probability … against replacing it by a neighbour" and names the estimand as the total causal effect of the replacement, as the registration §6.6 does. Is that the right strength for a `[NUM diagnostic]`?
5. **§1.1**: the sentence does not say that the criterion is met or unmet by the diagnostic; it says that the rule forbids reading the diagnostic as meeting it by itself, and leaves the question open. The PI may prefer it removed.
6. **Placement**: Thread B is owned by TDR-G as to its facts; the subsection states its own ownership. An alternative would be a fourth thread; that changes the document's structure and was not done.
7. **Evidence states**: the engine runs were made once, on the campaign machine; `EV-RUN` is claimed for the analysis only; `EV-INDEP` for the reviewer's aggregation only.

## 5. Checks run

| Check | Result |
|---|---|
| Build from the tag, base and evidence hashes asserted, 35 exact-once edits | candidate `8fc94079…6c29` (rebuilt twice, equal) |
| Base lines unchanged and in order | 577 of 602; the other 25 are the declared edits |
| `evidence/az/v0.9/owner_sync_check.py` | exit code 0, `RESULT: AS RECORDED` |
| `tools/dsn_lint.py` (informational) | 100,945 bytes; one footer line; 78 identifiers; no new history phrase in live text |
| `tools/pipes_index.py --check` | OK (122 items, 20 inboxes); `pipes/AZ/` three items: two closed, the TDR-G v2.12.15 notice dispositioned (accept), to be closed after the tag |
| `bash evidence/az/token_resonance/stage1/verify.sh` | `VERIFY PASS` on 12 Nov 2026 (the evidence the block cites); not rerun for the synchronization, which changes no evidence |

## 5a. Review record

Two reviews by the second co-owner (ChatGPT) on commit `4ea9d2f`, candidate `24f25f70…5ec7`; neither is an adoption. Both checked the four contrasts (risks, intervals, discordant pairs, adjusted `p`, readings) against the report §5 and the stored analysis outputs and found them equal; the first also recomputed the base and candidate hashes and confirmed 594 of 602 predecessor lines unchanged in order with its own comparison. Neither executed the builder or reran the engine. Both accept the §1.1 sentence (it stays) and the placement in Thread B (no fourth thread).

| Review | Finding | Disposition |
|---|---|---|
| `5876303497` R1 | "the parent–child phase law … is a candidate only" conflates a conditional kinematic identity (derived in the registration under token persistence) with its untested role in basin selection | Accepted: the block says that the law is a conditional identity under a token-persistence hypothesis, a `[SESSION]` statement offered to TDR-G and not a result of this DSN, and that its role in the selection of the tail basin is untested. No grade is given to it here |
| `5876303497` R1 | "There is no relation to the Hashimoto `4\|q` rule …" states an absence of evidence as a fact | Accepted: "No relation is established or claimed …; the shared numeral is not evidence of one" |
| `5877247214` (1) | The §4.2 heading ends "(bridge-candidate only)" although §4.2.1 is not a bridge-candidate | Accepted: heading "(bridge-candidate family; one AZ-owned diagnostic)"; the family's bridge-candidate status stays in its own paragraph |
| `5877247214` (2) | "a continuous distribution of `M`" is false: `M` is an integer | Accepted: "the node count `M`, an integer-valued outcome whose distribution is not separated into two groups at the threshold" |
| `5877247214` (3) | The statement and the §0.2 readout should separate the resonant-against-neighbour effects (PC1–PC3) from the PC4 equivalence control, and keep PC3 supportive only | Accepted in the statement, the family sentence and the §0.2 readout |
| `5877247214` (4) | Name the interval; "unqualified" is a control qualifier, not a further validation | Accepted: "97.5 % Agresti–Min paired-proportion interval" (the level printed by the registered analysis for both families); the controls' intervals named as 95 % Agresti–Min; the qualifier explained |

All in one content pass: `block_4_2_1.md` and two builder edits; the old phrases are on the builder's stale-string list. Delta for the readback: `git diff 4ea9d2f HEAD -- dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` — six hunks (§0.2 readout; §4.2 heading; four within §4.2.1).

**Readback and new dependency.** Review `5890500279` (second co-owner, 13 Nov 2026, on `e51fa3e`): the corrections above pass; the four numerical contrasts are unchanged; a new owner-source synchronization is required before adoption, as one content stage — update the live owner pins (keeping deliberately historical pins and the Stage 1 engine and orientation hashes), reference the adopted §6.13 owner identifiers with their hypotheses at the point of use, keep `AZ-NUM-TOKRES-S1` distinct from the owner's `[ALG]` laws, update this record and the import references, incorporate the inbox notice with statement-accepted and adopted-use states separate; no rewriting of earlier evidence, no promotion of the numerical result, no claim that the token law explains the tail. **Done in §2a** (candidate `8fc94079…6c29`); the notice is dispositioned with the adopted use stated as pending the tag. Delta for the readback: `git diff e51fa3e HEAD -- dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md evidence/az/v0.9/block_4_2_1.md`. The PI relayed the review on 14 Nov 2026 without a decision text; the synchronization is this lane's response to the review and is a candidate change only.

## 6. Steps

Review by the second co-owner → the PI's adoption decision → publication commit (status lines, adopted hash, `BASELINE.md` row, this record completed) → the PI merges with a merge commit and creates the annotated tag `az-v0.9` → notices through `pipes/` (TDRG: an AZ-owned diagnostic on its engine now exists in a DSN, and AZ §8 is at `tdrg-v2.12.15`; ATLAS; PROG if its AZ entry is affected), closing `pipes/AZ/20261112-TDRG-v2-12-15-adopted.md`, and the entry note.
