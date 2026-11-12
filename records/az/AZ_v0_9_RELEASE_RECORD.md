# AZ v0.9 — release record (DRAFT; candidate built, not adopted)

**[SESSION] Not adopted.** `az-v0.8` governs until the PI adopts this edition, the record is completed, and the PI merges and tags. Prepared by the AZ co-owner (Claude), 12 November 2026.

**Authority.** PI, 12 November 2026, 16:54 +03:00, project conversation, verbatim: "Stage 1 sonucunun `[NUM diagnostic]` olarak bir sonraki sürüme girmesini ve Stage2 çalışmasının başlamasını kabul ediyorum." — the Stage 1 result of Action 1 enters the next AZ edition as a `[NUM diagnostic]`. This is the separate PI decision that the outcome rule requires (rule confirmed by the PI on 12 Nov 2026; `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md` §11 item 3): *a validated, supported Action 1 contrast is eligible for a PI-approved `[NUM diagnostic]` entry within AZ Level A, with its exact simulation scope and provenance; it is offered to TDR-G for owner disposition; it does not by itself close AZ-OPEN-PROMO, promote AZ maturity, or become an adopted TDR-G claim.* The decision to enter the result is not yet the adoption of this edition.

## 1. Bytes and how to rebuild

| | File | SHA-256 | Bytes |
|---|---|---|---|
| base | `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` at tag `az-v0.8` | `146fcc2837f69e3d6a4fd626d29b5b038c7948c239eaedf7e55b57e74dd0ee76` | 89,039 |
| **candidate (DRAFT)** | same path on this branch | `24f25f70361d8159f629f555bc8207cc8cc285b34e74a775e2a6a4dfc2e05ec7` | 96,598 |

```bash
python3 -I evidence/az/v0.9/build_az_v0_9.py --out /tmp/c.md --log /tmp/l.txt
sha256sum /tmp/c.md dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md        # equal
git diff az-v0.8 -- dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md        # the whole delta: twelve hunks
```

One content stage, no compaction (Methodology v1.4 §13.6 asks for two stages only when a release also compacts). The builder reads the base from the tag, asserts its hash and the hashes of the registration package and of the campaign output, applies 13 exact-once edits (`evidence/az/v0.9/edit_log.txt`; the block is `evidence/az/v0.9/block_4_2_1.md`), and asserts that every base line not named in an edit is unchanged and in order: 594 of 602; four lines replaced (title, *Document status*, *Supersedes*, footer), four edited in place.

## 2. What changes

| Edit | Where | What |
|---|---|---|
| S4.2.1 | new §4.2.1, at the end of Thread B | **The diagnostic block.** `[NUM diagnostic]` `AZ-NUM-TOKRES-S1`, with scope and convention qualifiers; the statement; the four registered contrasts with their intervals, discordant pairs and readings, copied from the report §5 (erratum N1 applied: PC3 "Bonferroni-adjusted"); the controls; what the statement is and is not; evidence |
| S4.2-status | §4.2 status line | one sentence: one item of the thread is owned by this DSN |
| S0.1-row | §0.1 routing table | one row: owner, grade, not a TDR-G result, not a bridge-candidate |
| S0.2-B | §0.2, Thread B bullet | current-state readout of the diagnostic |
| S1.1-crit | §1.1 success criterion | the status stays "not met"; one sentence names the diagnostic and the outcome rule that limits it |
| S5-row | §5 high-risk ledger | one row with the forbidden overclaims |
| S9 | §9 | artifact entry `AZ-ART-TOKRES-S1` with hashes and evidence states |
| AppA | Appendix A | v0.9 entry |
| H-title, H-status, H-supersedes, H-summary, F | header, footer | edition identity (DRAFT), predecessor `az-v0.8` with its hash, one sentence in the status summary |

New identifiers: `AZ-NUM-TOKRES-S1`, `AZ-ART-TOKRES-S1`. None removed. No pin changes (`dyad-v6.4.24`, `tdrg-v2.12.14` are the governing editions per `BASELINE.md`).

## 3. What the edition does not do

- No change of the maturity level, of the OPEN registry or of the milestones; AZ-2 stays "attempted, negative-clarifying" — it concerns a graph/transfer-zeta observable, and the new diagnostic is not one.
- No mechanism, no `N`-scaling, no statement about TDR-26; no relation to the Hashimoto `4|q` rule or to Dyadic/DZT `q = 4` (SG-AZ-3, SG-AZ-7, SG-DZT-1).
- The algebraic statements of the registration (token-alphabet law, parent–child phase law) are **not** entered: they are offered to TDR-G (`pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md`, acknowledged, no disposition yet) and are TDR-G's to adopt or not.
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
| Build from the tag, base and evidence hashes asserted, 13 exact-once edits | candidate `24f25f70…5ec7` |
| Base lines unchanged and in order | 594 of 602; the other eight are the declared edits |
| `tools/dsn_lint.py` (informational) | 96,598 bytes; one footer line; 72 identifiers |
| `tools/pipes_index.py --check` | OK; `pipes/AZ/` two items, both closed |
| `bash evidence/az/token_resonance/stage1/verify.sh` | `VERIFY PASS` (the evidence the block cites) |

## 6. Steps

Review by the second co-owner → the PI's adoption decision → publication commit (status lines, adopted hash, `BASELINE.md` row, this record completed) → the PI merges with a merge commit and creates the annotated tag `az-v0.9` → notices through `pipes/` (TDRG: an AZ-owned diagnostic on its engine now exists in a DSN; ATLAS; PROG if its AZ entry is affected) and the entry note.
