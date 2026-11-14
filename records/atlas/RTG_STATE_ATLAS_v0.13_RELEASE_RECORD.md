# RTG State Atlas v0.13 — acceptance record (draft)

**Status:** DRAFT — candidate for change-focused review. Not accepted. `atlas-v0.12` is the tagged Atlas until the PI accepts this candidate, PR for branch `claude/atlas-v0.13` is merged and the annotated tag `atlas-v0.13` exists and is verified.
**Object:** a derived, NONCANONICAL Atlas. Acceptance adopts no owner science.
**Recorded by:** Claude, Atlas owner, 14 November 2026, on branch `claude/atlas-v0.13`.
**Method:** Atlas Method v0.3 (`atlas-method-v0.3`). This is the first edition built under it.

## 1. Object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md`, v0.13 candidate | `47384c0c6959392e786829e4435a62b52d76aa38c19d655fe9f7890ac86160a1` (536,466 bytes, 1,545 lines) |
| base `atlas-v0.12` | `cf9d8647b4c33206537e46ca37c7879d4fc33b1a936e0a50330a469f054def55` (523,005 bytes, 1,537 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.3) | `a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f` |
| `evidence/atlas/v0.13/source_manifest.json` | `c2b14b420df463552e43d1b3bf631cc799981493602a59b6fcb70884973d0a4e` |

Source snapshot: `main` `2676e6ff3e111aaa7d030cc1efcff45128b1abf3` (merge of PR #253). Two sources moved against the v0.12 manifest; the other sixteen are byte-identical and were not re-extracted.

| Source | v0.12 | v0.13 | File SHA-256 | Authority |
|---|---|---|---|---|
| TDRG | `tdrg-v2.12.14` | `tdrg-v2.12.15` | `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64` | `records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md` (PI adopted 12 Nov 2026) |
| AZ | `az-v0.7` | `az-v0.9` (contains v0.8) | `c198a8bbddb23ce0d546c3ed03bddcdcf02dd83b974da7651a89a3fec5ac7598` | `records/az/AZ_v0_9_RELEASE_RECORD.md` (PI adopted 14 Nov 2026); `records/az/AZ_v0_8_RELEASE_RECORD.md` |

Sequence: one refresh for both sources, after `az-v0.9`, by the PI's [SESSION] decision relayed 13 Nov 2026 (`records/atlas/ATLAS_V0_13_IMPACT_PREPARATION_20261113.md` §1). Both tags are annotated; the builder asserts tag bytes = manifest hash = snapshot bytes and that no newer tag of any source exists.

Build: `python3 -I evidence/atlas/build/refresh_v0_13.py` — from the bytes of `atlas-v0.12`, 74 anchored operations (`evidence/atlas/v0.13/edit_log.json`), replayed inside the run with an identical result. Evidence: `evidence/atlas/v0.13/`.

## 2. What changed (74 logged operations; net +8 lines, +13,461 bytes)

Operations by kind: identity 7 · TDR-G 16 · AZ 14 · reviewed items 6 · Method §4.1 span deletions 30 · pipes 1.

### 2.1 TDR-G v2.12.15

- **Star event domain** (`TDRG-DEF-STAR`, `TDRG-DEF-MULTISTAR`, `TDRG-DEF-CONV-TICK`): a valid centre has at least three pairwise non-adjacent defect neighbours; a single-star component has exactly one valid centre, of any shape; step 4 of the tick carries the classification precedence. The K₁,₃-only wording is recorded as superseded, with the owner's statement that no result changes (`EV-CODE`) and that the share of non-pure events in the canonical scans is not measured.
- **Eight new nodes** under the owner's RIDs, locator `@TDRG§6.13`: `TDRG-ALG-EVENT-INVENTORY`, `-NARROW-BAND-CLASSES`, `-TOKEN-CENSUS-LAW`, `-BIRTH-SPECTRUM-INJECTION`, `-SPECCONS-N`, `-BIRTH-SPECTRUM-NOT-CLOSED`, `-PARENT-CHILD-PHASE`, `TDRG-NUM-TOKEN-LAW-CHECK`; `TDRG-ART-TOKEN-LAW-CHECKS` as its `cert`. Each law carries "proposed by AZ, owned by TDR-G". No Stage 1 number of AZ is on any of them.
- **Spectrum conservation:** the n-node birth-free form is proved (`TDRG-ALG-SPECCONS-N`); the lemma node drops "CAND"; across births the update is exact but not closed on the spectrum.
- **Frontier:** TDR-6 is ACTIVE — PARTIAL with its sub-items as the owner prints them; `TDRG-OPEN-SPECCONS-STAR` stays ACTIVE for the spectrum-level question. The signed-class invariant is recorded as not closing TDR-6.
- **P:** FAIL as a birth invariant with ΔP ≡ −x; "gauge artifact" is withdrawn as the reason (frontier line, SG-3, retired list, and the OFN rejection row in D1, whose referral the owner has answered).
- **Gate and export:** the export row names 24A → 24B → 24C and TDR-T0. Two Atlas lines are corrected with it (§3, points 5 and 6).
- **L5:** TDRG.G9 retired (§2.3); TDRG.G8 reworded to the v2.12.15 layout; TDRG.G11 gains the placed artifact; TDRG.G10 unchanged in content.

### 2.2 AZ v0.9 (with v0.8)

- **New node `AZ-NUM-TOKRES-S1`**, `NUM·dx`, locator `@AZ§4.2.1`, `cert AZ-ART-TOKRES-S1`: full scope and convention, the four contrasts with their families, the owner's negatives, and edges to `TDRG-ALG-PARENT-CHILD-PHASE`, `TDRG-ALG-TOKEN-CENSUS-LAW`, `TDRG-DEF-ORIENT`. The phase law is not restated in the AZ node. One home.
- **Thread C evidence qualifier** rewritten from AZ §9 per artifact (what is deposited and replayed, what is source-reported). The v0.12 clause about a [SESSION] custody record is gone: the owner text now states the availability itself.
- **Ledgers:** `*AZ:A-ledger`, `*AZ:B-ledger`, `*AZ:A-heur` point to AZ §8 (each owner result cited once); pins `dyad-v6.4.24` and `tdrg-v2.12.15`; the B ledger gains the two token-law rows with their local use.
- **Frontier and guards:** `AZ-OPEN-SCOPE-ZETA` PARTIAL, `-SCOPE-ARITH` and `-PROMO` ACTIVE (not closed by the diagnostic); the two definitions of `G_birth(w)`; SG-AZ-7's worked example at the scope of its evidence; AZ.A5 kept in both rows with the AZ clause at v0.9.
- **PROG.G6:** AZ's state after the Programme record (Methodology v1.4 declared, §6.7 reduction carried out, no merger).

### 2.3 Reviewed items (Method §7: grade, qualifier, identifier or diagnostic change — six operations)

| # | Item | Change | Owner evidence |
|---|---|---|---|
| R1 | `PROP-AZ-CORE-EQUIV` | grade **THM-ALG → THM**; the 2,141,014-graph enumeration becomes source-reported corroboration; `cert AZ-ART-CORE-EQUIV-CHECK` added | AZ §4.3.2 (`[THM]` … `[proof: written derivation, below]`; "Corroboration; not the basis of the grade"), Appendix B, corrections at v0.8 |
| R2 | `TDRG-AZ-STATIC-ZN-4Q` | head **NUM·dx / HEUR strong → NUM·dx**, with the link to the low-order obstruction HEUR; the verdict stated for the tested null protocol only | AZ §4.3.3, §4.3.5, SG-AZ-7; Appendix B (two `[COR]` entries) |
| R3 | `AZ-1A/1B/1C` | evidence qualifier replaced (per artifact) | AZ §9, Appendix B |
| R4 | `AZ-ART-ZETA-V3` | grade token **ENG-historical removed**; the line carries no grade | AZ Local Tag Aliases ("described by its registry status in §9, not by a tag"), Appendix B |
| R5 | TDRG.G9 | **retired** — the owner separated the TDR-6 sub-item (resolved as a predictable-change law) from `TDRG-OPEN-SPECCONS-STAR` (still ACTIVE, a different question) | TDR-G §2 TDR-6 and OPEN-SPECCONS-STAR current status |
| R6 | METH.M1 | AZ leaves the list of sources with compound grades | AZ: the old spellings occur only in the retraction block, the corrections list and the edition history (asserted by the builder) |

No L5 key is new. Retired keys: the cumulative list has 154 entries (152 at v0.12, plus TDRG.G9 in its two spellings; `evidence/atlas/v0.13/retired_l5_keys.json`). Dispositions of all D5 L5 rows and of every other touched row: `evidence/atlas/v0.13/dispositions.json` (9 reworded, 1 retired, 7 retained).

### 2.4 Method §4.1 span deletions (30 operations, 336 bytes)

Edition labels that only date a result, removed without rewording: on TDR-G nodes of D5 (`(v2.12.14)` heads, "since v2.12.14" clauses), and AZ edition labels made stale by the source movement (`since az-v0.7`, `AZ v0.7 §6`) — the latter also on three Dyadic nodes' AZ consumer clauses and on H2, the OPEN-M audit node and OPENM.U11, outside D5. Kept, under the third sentence of rule 4.1: labels in H4, H9, D5.X1 and `TDRG-DEF-ORIENT` that say what two editions state differently, and consumer pins (OFN's `tdrg-v2.12.14`, TDR-G's `az-v0.7`). Rule 4.7 was not applied: no certificate-run span in D5 was found that could be cut without rewording.

### 2.5 Pipes

NUMGEN.N-I1 restated at the snapshot: 123 items in 20 inboxes — 66 closed, 2 dispositioned, 55 open. The open ATLAS item (`pipes/ATLAS/20261112-AZ-v0-8-adopted.md`) is dispositioned on this branch (accept) and is closed after the tag.

## 3. Checks, limits, and points for the reviewer

**Shared checker** (`tools/atlas_check.py`, run with this edition's manifest, coverage map and cumulative retired list): 0 FAIL — sources 72 PASS; coverage 137 PASS; qualifiers 4 PASS; links 525 PASS, 10 documented-unresolved, 2 UNVERIFIED; artifacts 120 PASS, 2 UNVERIFIED; keys 154 PASS; wording 13 WARN. Against v0.12: four UNVERIFIED rows are gone (the three `AZ-OPEN-*` RIDs now have declarations; `prove_core_equiv.py` is no longer cited as a bare file); one WARN is new ("resolved" in the TDR-6 line, the owner's word). 18 shared controls behave as expected.

**Builder assertions the shared tool lacks:** no RID of `tdrg-v2.12.14` or `az-v0.7` is missing at the new tags; the 16 identifiers new at the tags (nine at TDR-G; at AZ six of its own and three TDR-G RIDs it newly declares as cited, two of them among the nine and the third `TDRG-OPEN-TOPO-FILTER`, whose home is TDR-G's own node) each have exactly one declared home (`verification_summary.json`, `moved_source_homes`); 26 owner-text facts; 26 focused negative controls, all detected (`negative_controls.json`) — among them every control planned in the preparation record §5.

**Limits.** Structural checks only; no owner certificate was rerun. TDR-G was read in its full diff and §6.13; AZ v0.9 in full at statement level; AZ's Dyadic rows were not re-compared word by word with the unchanged Dyadic text. The homes check is the builder's, not the shared tool's.

**Points for the change-focused review:**
1. R1–R6 of §2.3, each against its owner evidence.
2. `AZ-NUM-TOKRES-S1`: is the node's statement the owner's (families, intervals, negatives), and is the `NUM·dx` head the right reading of `[NUM diagnostic]`?
3. The eight TDR-G nodes: statement fidelity, and the wording "proposed by AZ, owned by TDR-G" as attribution rather than chronology (rule 4.1).
4. Single ownership: no token law inside the AZ node, no AZ number on a TDR-G node, the B ledger as edges only.
5. **`*PROG:TDRG-launch-gate` (D1).** Programme v1.4 §6.4 still says that the owner's export row names the earlier D/A/B gate. The owner corrected the row in v2.12.15. The node now states both facts. No new L5 key was created for it; whether it deserves one (D-STALE, for the Programme's next edition) is a question for the reviewer and the PI.
6. **D5.L3 launch-chain line: an Atlas error corrected.** v0.12 carried "! owner Appendix C still carries older D/A/B gate". The owner had aligned Appendix C in v2.12.14 (TDRG.G8 in v0.12 said so itself); the note did not describe the owner text. It is replaced. The builder asserts that "D/A/B" occurs once in the owner file, in the correction note of the export row.
7. The §4.1 deletions outside D5 (H2, OPEN-M audit node, OPENM.U11, three Dyadic nodes): accepted as consequences of the source movement, or to be held for a D2/D4b opening?
8. METH.M2 keeps AZ: the Thread C items without RIDs (engineering records, retractions, the three open items) remain.

## 4. Decision

Pending. To be completed with the reviewer's result and the PI's decision.

## 5. Publication (pending; the PI executes)

After acceptance: BASELINE row for ATLAS; merge (merge commit) and annotated tag `atlas-v0.13` in one CLI block; tag verification record; closure of the ATLAS inbox item.

## 6. Carried forward

- Coverage check of the shared tool for non-Dyadic sources (now done by builder assertions).
- Seven other multi-line identifiers; comparator mode for heading renames; an AZ profile for `tools/orient.py`; F4.
- Size: 536,466 bytes. Reported, not targeted (Method §4.6); reconsidered by the PI after the sources consolidate.
