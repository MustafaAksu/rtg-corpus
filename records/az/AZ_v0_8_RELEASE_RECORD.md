# AZ v0.8 — release record (DRAFT; stage 1 of 2)

**[SESSION] Not adopted.** No edition exists until the PI adopts one, this record is completed, and the PI merges and tags. This draft covers **stage 1**, the corrected intermediate: a build stage, not an edition (Methodology v1.4 §13.6). Prepared by the AZ co-owner (Claude), 12 November 2026.

**Authority.** v0.8 cycle started by the PI on 12 Nov 2026, 11:30 +03:00 ("başlatalım"). Content: PI decision of 11 Nov 2026, 18:15 +03:00, row 5 (`records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` §5). Choices D1–D4: PI decision of 12 Nov 2026, 12:52 +03:00, "Ortak önerilerinizin tamamını kabul ediyorum" — D1 (a) declared section map, D2 (a) ledger rows only, D3 (a) `[THM]` on a written proof, D4 the Action 1 diagnostic is not in v0.8 (`records/az/AZ_v0_8_EDIT_PLAN.md` §4, §7).

## 1. Bytes and how to rebuild

| Stage | File | SHA-256 | Bytes |
|---|---|---|---|
| base | `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` at tag `az-v0.7` | `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94` | 83,281 |
| 1 — as first submitted (commit `aeb6108`, reviewed in `5874174108`) | same path | `8ebcfb9a6c4065278ff6120b28237d7d6752d05a6c48655a42542478528eba67` | 92,719 |
| **1 — corrected intermediate after review** (this branch) | same path | `19a1faf01e44a74d2bffc8dbf14fddae798f21e75f3c5e166f290d6f11fd0426` | 94,673 |
| 2 — compacted candidate | not built | — | — |

```bash
python3 -I evidence/az/v0.8/stage1/build_az_v0_8_stage1.py --out /tmp/inter.md --log /tmp/edit_log.txt
sha256sum /tmp/inter.md dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md      # equal
diff /tmp/edit_log.txt evidence/az/v0.8/stage1/edit_log.txt               # empty
git diff az-v0.7 -- dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md          # the stage-1 delta
```

The builder reads the base from the tag, asserts its hash, and applies 51 edits, each located by an anchor that must occur exactly once (`evidence/az/v0.8/stage1/edit_log.txt`; new text in `evidence/az/v0.8/stage1/blocks/`). It stops on a missing or repeated anchor, on a lost identifier, on a stale string, and when a protected region differs from the base.

## 2. What stage 1 changes

| Group | Edits (log keys) | What |
|---|---|---|
| Tags and identifiers (plan A5, A6) | A5-A6, A5-heur-1/2/3, A5-result, S3-PROG-1/2/4, S6-uvm, S5-4q | Aliases under Methodology v1.4 §8.4; `[ENG-planned]` and `[ENG-historical]` dropped; `[import-ref]`, `[ENG-blocker]`, `[ENG-open]` declared as labels; `[bridge-disqualified]` and the AZ-2 result paired with `[from: NUM]`; `[HEUR/NUM strong]` unpacked; four `[source:]` records turned into `[import:]`; identifier owner map |
| PROP-AZ-CORE-EQUIV (D3) | D3, S0.1-facts, S0.1-sg04, S5-prop, S5-prop2 | `[THM-ALG]` → `[THM]` with the complete proof in §4.3.2; the reading of "closed non-backtracking walk" the statement depends on; the reported enumeration and the new finite check as corroboration |
| Declared section map (D1 a) | S0-intro, S0.1-head, S0.2-S0.3, A7-marker, S2, S7-head | §0.2 current state, §0.3 section map, routing function assigned to §0.1, context-core marker after §3, OPEN entries in the §5.1 form; numbering unchanged |
| Reduction (D2 a) | B1-B3, B2, B4, B5, S8 | Restated owner results removed from §1.2, §4.1.1, §4.1.2, §4.2 and §6; each owner result cited once, in §8 |
| Pins (C5) | S0.1-dyad, and inside B1-B3, B5, S8 | Dyadic `dyad-v6.4.23` → `dyad-v6.4.24` in the live body |
| Availability (C1–C4) | C1-C4, C3-gbirth, S0.1-engine, S4.3-status, S5-eng | §9 per-artifact availability and evidence state; conventions file as found; two definitions of `G_birth(w)`; exporter registered under its own identifier; new check registered |
| Version-scoped wording | S1.1-done, S1.1-crit, S1.3-AZ0/AZ1/AZ2, S3-SG5-head, S3-SG5-hist, S3-SG6, S3-SG7, B4-note, S4.3.6-head, S5-eng2, S5-gz, S6-bd, S7-hist, S7-67 | "v0.6 note", "(REVISED v0.6)", "Was:" and similar labels removed or reworded as current status |
| Scope of the static-geometry conclusion (review R1) | R1-SG7, R1-AZ2 | The worked example of SG-AZ-7 and §4.3.5 no longer say that the `4\|q` rule appears for *any* antipodal-band graph on *any* $\mathbb{Z}_N$, nor that this is "proven"; they state that the rule is reproduced without TDR-G dynamics in the tested null protocol and is therefore not specific to the dynamics. The `[NUM diagnostic]` result and the `[bridge-disqualified]` verdict are unchanged |
| Appendix B | APPB | "Corrections registered at v0.8": six `[COR]` records for the status, scope and tag changes above |

**How the Import Ledger rows were made.** Each row is the readout of the v0.7 §8 row (its bytes) followed by limitation sentences taken byte for byte from the v0.7 thread text (builder functions `readout` and `frag`), with the owner's location and tag. The only new words are the labels that join them and, in one row, "remains a conditional candidate in the owner documents" for the non-canonical `[CAND/conditional]`. Mixed tags are unpacked to the owner's tags as printed at `tdrg-v2.12.14` (`[THM]` for `TDRG-THM-REACHABILITY-K0`, `[ALG]` for the three lemmas and the BIND3 cycle enumeration, `[NUM strong]` for the BIND3 `NUM` identifiers). Formulas and numerical values that were printed only in the threads are no longer in this document, except where a row keeps them (the `p = 12` boundary value, the N-scaling fit and its window dependence, the TDR-26 counts).

**Pin check for C5.** `git diff dyad-v6.4.23 dyad-v6.4.24 -- dsn/RTG_DYADIC_OSCILLATOR_DSN.md` was read at word level. Eleven changed lines carry an identifier AZ cites; all eleven are the owner's records about its consumers (the classification table of consumer strings, which names "AZ v0.7", and one consumer note on Genesis). No statement of a cited result changed. The owner's table cites AZ sections "§1.2, §4.1, §8"; after this edition the Dyadic strings are in §8 only — a notice to DYAD is due at release.

## 3. Protected regions (byte-identical to `az-v0.7`, asserted by the builder)

Header (stage 2 replaces it); §4.1.3; the non-claims of §4.2; §4.3.1 engineering closure; the statement of the antipodal-band low-order obstruction; the two evidence chains of §4.3.3; the retraction block of §4.3.4; §10; Appendix A; Appendix B through v0.7; the footer. 24,483 bytes in eleven regions; hashes in the edit log. No AZ identifier is lost; new identifiers: `AZ-ART-CORE-EQUIV-CHECK`, and `TDRG-AZ-EXPORT-BASELINE` as the exporter's printed self-identifier.

## 4. Points for the change-focused review

Each is a place where stage 1 words something that the adopted file did not say in that form.

1. **§4.3.2, the proof.** Read as a proof (the two standard facts; Case 2 and its junction checks). Proposed by the second co-owner, written out and checked by this lane; plan §8.
2. **`[HEUR/NUM strong]` → `[HEUR]`** for the link from the low-order obstruction to the `4|q` rule, with the `[NUM diagnostic]` chains named as its numerical support. The weaker of the two possible readings of the mixed tag was taken, because the same paragraph records a falsified prediction of that link. If the PI reads the tag as `[HEUR strong]`, it is a one-word change in two places.
3. **§2, closure criteria.** The adopted entries had no closure criterion. None was invented: OPEN 1 and OPEN 2 point to conditions already stated in §1.1, §4.3.6 and §4.2; OPEN 3 says that the conditions are to be registered. "Required before any Level B promotion" is kept on all three.
4. **§0.2 current state** is new navigation text; each bullet names the section that governs.
5. **§9**: the statements "not shown to be the frozen state this DSN cites" (conventions file), "the part of AZ-1B that concerns real TDR-G exports is source-reported", and the `G_birth(w)` paragraph are taken from `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md` (§3, §5 there). No grade is changed by them.
6. **AZ-OPEN-SCOPE-ARITH**: "it is proven to be substrate geometry" → "it is shown to be substrate geometry", since the reclassification is a `[NUM diagnostic]` (§4.3.3).
7. **Ledger rows**: each against the owner text at `dyad-v6.4.24` / `tdrg-v2.12.14`, in particular that no limitation printed in the v0.7 threads is missing from its row.
8. **§7**: the sentence on the Programme's §6.7 proposal now says that the reduction is carried out in this edition by the PI's decision.

## 5. Differences from the edit plan

- **The reduction is in stage 1, not stage 2.** The operation classes of `tools/check_compaction.py` (reference substitution, history removal, history sections, header, footer, reorder) do not include "remove a restated owner statement whose readout survives elsewhere". Removing it is therefore a content change and is reviewed as one. Stage 2 keeps only what the checker can verify.
- **Size.** The plan estimated 60–65 KB after both stages. The intermediate is 92.7 KB: the thread sections fell from 20.8 KB to 6.3 KB (§1.2, §4.1, §4.2 together), but the ledger grew from 5.0 KB to 13.9 KB because every limitation sentence was kept, so the text about owner results fell by 5.5 KB in all; and the edition adds the proof (+4.5 KB), the per-artifact availability (+4.6 KB), the state and section map (+2.8 KB), the OPEN entries in full form (+0.9 KB) and the correction records (+2.8 KB; +2.0 KB more with the review corrections, 94.7 KB in all). Stage 2 (header, §10, Appendix A) is expected to remove about 8 KB. The estimate in the plan was wrong; nothing was cut to meet it.
- **Row wording.** The plan foresaw newly worded short readouts. The rows reuse the v0.7 readouts and v0.7 sentences instead (§2 above), so that no owner statement is paraphrased anew.

## 6. Checks run for stage 1

| Check | Result |
|---|---|
| Build from the tag, base hash asserted, 51 exact-once edits | intermediate `19a1faf0…0426`; edit log stored |
| Protected regions | 11 regions byte-identical |
| Identifiers | none lost |
| Stale strings in the live body (`v6.4.23` pin, `[THM-ALG]`, `[source:`, mixed tags, version labels, the universal wording of R1) | none; `[HEUR/NUM strong]` twice, both inside or about the retraction block |
| `tools/dsn_lint.py --prev` (informational) | 94,673 bytes; context-core marker present; context core 37.1 k characters (v0.7: 46.4 k); history phrases in live text 16 (v0.7: 25) |
| `evidence/az/core_equiv_check/az_core_equiv_check.py --nmax 7` | exit 0; 2,131,019 graphs, 0 mismatches (plan §8.3) |
| `tools/pipes_index.py --check` | OK; `pipes/AZ/` holds two items, both closed |

Not run: `tools/check_compaction.py` (stage 2); no owner artifact; no Thread C computation other than the finite check.

## 6a. Review record

**Review `5874174108`** (second co-owner, ChatGPT; 12 Nov 2026, 15:06 +03:00; on commit `aeb6108`, intermediate `8ebcfb9a…ba67`): *accept with corrections; R1 required before stage 2; no adoption or merge authorisation.* By its own statement the reviewer recomputed the two file hashes and the edit count, read the proof, the ledger rows, the availability block, this record, the edit log and the finite check's source and stored output, and ran an independent comparison of the 2-core with the recurrent core on all 1,099 labelled simple graphs with at most 5 vertices (0 mismatches); it did not execute the builder, the full finite check or the compaction checker. Accepted: the proof and `[THM]` at the stated domain; `[HEUR]` for the mechanism link; D1, D2 in stage 1, D4; the §2 closure pointers; the §9 separation of recovered and missing files and the open `G_birth(w)` discrepancy.

| # | Finding | Disposition |
|---|---|---|
| R1 | SG-AZ-7 (worked example) and §4.3.5 assert that the `4\|q` rule would appear for any antipodal-band graph on any $\mathbb{Z}_N$ and call this proven. It follows neither from §4.3.2 nor from Chain 2, and is false as stated (full antipodal graph at $k=0$: a perfect matching, empty 2-core). An overstatement inherited from v0.7 | Accepted. Edits R1-SG7 and R1-AZ2; `[COR]` record in Appendix B; the old wording added to the builder's stale-string list. The other places that state the conclusion (§0.2, §1.1, §4.2, §4.3.3, §5, §6) carry no universal quantifier and are unchanged; Chain 2 itself is a protected region |
| R2a | `AZ-ART-AZV5-REGISTRY` lists `phase2_harness` in the set covered by the registry, while the received registry has ten files and no harness | Accepted. The entry now describes the received ten-file AZ-1A/AZ-1B registry; the harness is stated separately as not covered and source-reported; noted in the §9 `[COR]` record |
| R2b | `AZ-ART-CORE-EQUIV-CHECK` says three negative controls; the stored output has four lines | Accepted: "four negative-control checks of three kinds", named |

Delta for the readback: `git diff aeb6108 HEAD -- dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` — five hunks (SG-AZ-7; §4.3.5; two in §9; Appendix B).

## 7. Left for stage 2 and for the release

Stage 2 (layout only, against the reviewed intermediate): header in the v1.4 field order with the declared section map, Methodology v1.4, companions with `dyad-v6.4.24`, a 2–4 sentence status summary, no "Major update" list; the dated list of §10 to one provenance paragraph; Appendix A with a v0.8 entry and compact earlier entries; footer. Then: second co-owner review of each stage, PI decision, completion of this record, status-lines commit, merge and tag by the PI; notices through `pipes/` to PROG (its §6.7 and §9.2 rows), DYAD (its table of consumer strings), TDRG, DZT and ATLAS.

## 8. Not in v0.8

The Action 1 `[NUM diagnostic]` (D4); AZ-2; the still missing Thread C files; any change of Level A.
