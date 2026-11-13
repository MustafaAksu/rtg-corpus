# Discrete Genesis (TDR-G) v2.13 — Release Record

**Status:** DRAFT. The candidate is built in two stages and checked. Before adoption it needs:
- the ChatGPT co-owner's review of stage 1 (change-focused) and of stage 2 (mechanical);
- the atlas owner's row check;
- the PI's adoption.

**Date:** 13 November 2026.

**Prepared by:** Claude, TDR-G co-owner session `claude01SKePJ`, on branch `claude/tdrg-v2-13`.

**Edition:** v2.13, a maintenance edition. It migrates the document to Methodology v1.4 and pins AZ at v0.8. No scientific result changes, and nothing is rerun.

**Predecessor:** `RTG_DISCRETE_GENESIS_DSN` v2.12.15, tag `tdrg-v2.12.15`, SHA-256 `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64`.

Fields marked *(to be filled)* depend on steps that have not happened yet. Every hash below was computed on the branch files by `evidence/tdrg/v2.13/fill_release_record.py`; none was typed by hand.

## 1. Mandate, plan and decisions

| Step | Source | State |
|---|---|---|
| Cycle started | PI, 13 Nov 2026, 12:07 +03:00 ("onaylıyorum"), approving one candidate (v1.4 migration plus AZ v0.8 pin) with separate decision notes on XFER-O08-01 and `largest_center` / TDR-19 | given |
| Plan | `records/tdrg/TDRG_v2_13_EDIT_PLAN.md` (PR #263): rows S1–S8 and C1–C6, decisions D1–D3 | written |
| Co-owner evaluation of the plan | ChatGPT co-owner, relayed in the session at 12:06 +03:00. Agrees with the order. Stage 1 carries pins, structural fit and scope corrections; stage 2 is compaction only, with a movement map; results, RIDs, grades and OPEN states are preserved; the TDR-6 relational question is not a closing condition | not a repository record |
| PI decisions | "1- a 2-a 3-a" (13 Nov 2026, 12:23 +03:00): D1 (a), §1 as readouts; D2 (a), §2 history only; D3 (a), §A.sim to §8. Recorded in plan §7 | given |
| Stage 1 review | ChatGPT co-owner (change-focused) | *(to be filled)* |
| Stage 2 review | ChatGPT co-owner (mechanical) | *(to be filled)* |
| Row check | atlas owner | *(to be filled)* |
| Adoption, merge commit, tag `tdrg-v2.13` | PI | *(to be filled)* |

## 2. Identities and build

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v2.12.15) | `git show tdrg-v2.12.15:dsn/RTG_DISCRETE_GENESIS_DSN.md` | `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64` |
| Stage-1 intermediate (a build stage, not an edition) | `git show 1a8e02a29ed4589291b752e0a0a0901cf7e7d8b6:dsn/RTG_DISCRETE_GENESIS_DSN.md` | `b24c17ccbc93150449842a603c2c18fd47e66bc6f27ee77152802b36d450cdcc` |
| **Candidate v2.13** | `dsn/RTG_DISCRETE_GENESIS_DSN.md` | `1691a136d01ce3f68a241c72d13d9f17c1a184986f6869fe9b9d507a324dee18` |
| Stage-1 builder | `evidence/tdrg/v2.13/stage1/build_tdrg_v2_13_stage1.py` | `cde3d5e6c47eeaf87b8ce0cf476b82c4bea2c789a1b2cd76e8bb315a05d7aa7b` |
| Stage-1 checker | `evidence/tdrg/v2.13/stage1/check_tdrg_v2_13_stage1.py` | `f54d36be5c1635971df992612c777dadbf5cc78d4e5bf6b123b303c4730065f1` |
| Stage-1 edit log (29 edits) | `evidence/tdrg/v2.13/stage1/edit_log.json` | `6945f982725bdca286c24418b634f63a8a82847b68a9f7531de474411ac68cb5` |
| Stage-1 gates / controls output | `evidence/tdrg/v2.13/stage1/check_output.txt`, `controls_output.txt` | `93f070ec3054276656e464d4c21e55e4505e2728e9ea14876a791e1fb09558f2`, `4093f1ec91f8f1f492bae8fa54e53c7e99128993534e20a9c516468e562a5998` |
| Stage-2 builder | `evidence/tdrg/v2.13/stage2/build_tdrg_v2_13_stage2.py` | `4a724d53966af488b2f9c1a314c6731ed6d3fdf7a4d17b959a79e42e5ac55781` |
| Movement map (43 operations) | `evidence/tdrg/v2.13/stage2/movement_map.json` | `024a730e0482404c8c77299036d37cc7f6cd97c8b24547bc8ccb7cc31866a75b` |
| Compaction check output / report | `evidence/tdrg/v2.13/stage2/check_compaction_output.txt`, `check_compaction_report.json` | `12cdafea7ec921db4774aeb854416ade3701f8d089041a1d65e547bc3d74e6ce`, `f72cabff82bea8c0a2f3515a6f5c437eeaf447c9324eb84fa9df39cc1c02b5ef` |
| Stage-2 negative controls and output | `evidence/tdrg/v2.13/stage2/stage2_negative_controls.py`, `stage2_negative_controls_output.txt` | `474fcaca0d65bb244488ece9ddcf2b7d332b5df150c4ec042bb717e9c782340f`, `2e1ae162d81d9a8cfbe1837e468791964e0241ab7e93bc3b2e6839af7a00a801` |
| Compaction checker (repository tool, unchanged) | `tools/check_compaction.py` | `d2977b3e24fd54a1d85fe53ea88f65dd51a9e26890b56b17ab5855716b57d87c` |

**Reproduce** (from the repository root, with the tags present):
```
T=$(mktemp -d)
git show 1a8e02a29ed4589291b752e0a0a0901cf7e7d8b6:dsn/RTG_DISCRETE_GENESIS_DSN.md > $T/inter.md
python3 -I evidence/tdrg/v2.13/stage1/build_tdrg_v2_13_stage1.py --out $T/rebuilt.md --log $T/log.json   # = inter.md, = edit_log.json
python3 -I evidence/tdrg/v2.13/stage1/check_tdrg_v2_13_stage1.py --intermediate $T/inter.md [--controls]
python3 -I evidence/tdrg/v2.13/stage2/build_tdrg_v2_13_stage2.py --emit-base $T/base.md   # writes the candidate and the map
python3 tools/check_compaction.py $T/base.md dsn/RTG_DISCRETE_GENESIS_DSN.md evidence/tdrg/v2.13/stage2/movement_map.json
python3 -I evidence/tdrg/v2.13/stage2/stage2_negative_controls.py
```
The stage-1 builder reads its base from the tag. The stage-2 builder, the map and the controls read the intermediate from commit `1a8e02a` and assert its hash, so no second copy of a DSN state is kept (Methodology v1.4 §13.7).

## 3. Stage 1 — what changes, by decision (29 edits; `edit_log.json`)

| Plan row | Edits | What changed |
|---|---|---|
| S1 — AZ pin | E13, E25, E26 | §6.2 cites `AZ-ALG-ANTIPODAL-LOWORDER` at `az-v0.8`. Checker C6 shows the entry is byte-identical at `az-v0.6`, `az-v0.7` and `az-v0.8`. The AZ consumer row is restated from AZ's own v0.8 text: AZ §8, IMP-B, cites TDR-G at `tdrg-v2.12.14`; the two AZ identifiers with a `TDRG-` prefix are AZ's, not TDR-G RIDs, and are not named, so that no tool reads them as TDR-G identifiers. Pins are current. |
| S2 — Methodology | E01, E02 | The header declares v1.4. The alias sentence names v1.4 §8.1; its v2.12.14 history (the legacy rows, which carry tags) stays in the tagged predecessor. |
| S3 — historical pins | E06, E07, E15, E19, E26 | The OPEN-OFN-2 connection of TDR-1 and TDR-19 points to `ofn-v0.12`, where OPEN-OFN-2 is open as `RTG-OFN-OPEN-DISC-INTERACTION`. CONV-TICK and LEM-NOANNIHIL name their current consumer rows, OFN v0.12 IMP-O08-14 and IMP-O08-06; OFN imports LEM-NOANNIHIL as `[ALG]`, so the old "`[RESULT]` `[from: ALG]`" description of OFN v0.7 leaves. No claim-specific historical pin remains in the live text. |
| S4 — owner-review tasks | E05 | Stated as TDR-G's own current items (Programme v1.4 does not carry them; checker C6), with the same four statuses. |
| S5 / D3 (a) — §A.sim | E28 | The table and its `[RESULT]` are copied verbatim into §8 as "Simulation artifact evolution" (checker C8). Stage 2 removes the Appendix A copy. |
| S6, S7 / D1 (a) — §1 and summary | E03, E04 | §1 has 407 words of readouts with RIDs and pointers. Checker C7 requires that 24 statements dropped or shortened (formulas, fit values, rates, the factorization precision, the slot-volume fits, the $q_{\rm proj}$ correction and others) still occur at their home outside §1. The status summary has three present-state sentences. |
| Typing of the summary (part of D1 (a)) | E04 | The old §1 graded some summaries more strongly or more loosely than their owner records. The readouts now carry the owner grades: the band form of reachability is `[ALG]` as LEM-REACH in §6.5 (old §1: under `[THM]`); the policy branches are `[NUM]`, `[NUM]` and `[HEUR strong]` as in §6.6 (old §1: one `[NUM strong]` for all three); BIND3 is `[ALG]` for the exact enumeration and `[NUM strong]` for parity and the spectral gate, as in §6.12 (old §1: `[NUM strong]` throughout). No grade in §§2–9 changes (checker C4). The old §1 sentence "No plateau through $N=1080$" is not carried: the §6.8 table extends to $N=1440$, and the statement is stale. |
| S8 — superseded hypothesis | E10, E11, E29 | The v2.8 failed-relock hypothesis leaves TDR-25. Appendix B records it as `[SUPERSEDED]`, quoting its original statement verbatim (checker C9), with its reason and replacement. The bullet that revised it now points to Appendix B. |
| D2 (a) | E09 | The TDR-24B record stays in §2. The sentence announcing its move to Appendix A "in v2.13" is replaced by "The paragraphs below are the supporting record." |
| XFER-O08-01 | E24 | Stated as **open**, a separate decision of both owners (PI, 13 Nov 2026); previously "deferred to v2.13". |
| Correction labels with a tag | E08, E12, E14, E16–E18, E20–E23, E27 | Eleven "*(v2.12.x `[COR]` …)*" labels are removed. Each correction is recorded in Appendix A and in its release record. Where a label carried a qualification (CONV-TICK step 4, the gcd converse, the mirror-inventory scope), the qualification stays. |

**Checks, stage 1** (`check_output.txt`, `controls_output.txt`): RESULT: 11/11 gates pass — C0 base; C1 build; C2 confined; C3 RIDs; C4 tags; C5 OPEN; C6 pins; C7 §1; C8 §A.sim; C9 App. B; C10 header.

Negative controls:
```
K1 AZ pin back to az-v0.7: CAUGHT (target C6 FAIL; C1 FAIL)
K2 tag changed in an untouched paragraph: CAUGHT (target C4 FAIL; C1 FAIL)
K3 RID declaration dropped: CAUGHT (target C3 FAIL; C1 FAIL)
K4 OPEN Status line changed: CAUGHT (target C5 FAIL; C1 FAIL)
K5 §1 home lost: CAUGHT (target C7 FAIL; C1 FAIL)
K6 §A.sim copy altered: CAUGHT (target C8 FAIL; C1 FAIL)
K7 Appendix B paraphrased: CAUGHT (target C9 FAIL; C1 FAIL)
K8 fifth summary sentence: CAUGHT (target C10 FAIL; C1 FAIL)
K9 stale v2.13 promise reintroduced: CAUGHT (target C6 FAIL; C1 FAIL)
CONTROLS: 9/9 caught
```

## 4. Stage 2 — compaction (43 operations; `movement_map.json`)

The base is the stage-1 intermediate. The operations are:
- the header, in v1.4 field order, with the stage-1 status summary unchanged;
- 40 history-removal edits of version labels without content. Each removed span carries the profile history word `v2.12` and no tag, RID, mathematics or qualifying word, and each is found byte-identical in the intermediate;
- Appendix A: compact entries for v2.13, v2.12.15 and v2.12.14, and one line for each earlier edition, whose full text stays at `tdrg-v2.12.15`; §A.sim leaves;
- one footer line.

**Compaction check** (`tools/check_compaction.py`, `check_compaction_output.txt`): RESULT: PASS, exit 0 — 55 checks, every operation and every global check PASS; 268 claim blocks in base live text: 244 byte-identical, 24 changed by declared operations, 0 unexplained

**Negative controls** (`stage2_negative_controls_output.txt`):
```
base: git show 1a8e02a29ed4589291b752e0a0a0901cf7e7d8b6:dsn/RTG_DISCRETE_GENESIS_DSN.md  sha256 b24c17ccbc93150449842a603c2c18fd47e66bc6f27ee77152802b36d450cdcc
OK    P0 unmutated map                                               exit 0 (want 0)  RESULT: PASS
OK    N1 undeclared change in the live text                          exit 1 (want 1)  FAIL  mechanical scope (re-derivation)  — first difference at line 92: derived 'ACTIVE — PARTIAL  \nQuestion: Identify a purely relational invariant p
OK    N2 status summary with a sentence not in the base              exit 1 (want 1)  FAIL  operation S2-H (presentation)  — status summary adds text not in the base summary (header): ['TDR-6 is closed.']
OK    N3 history-removal of a tagged, identified span                exit 1 (want 1)  FAIL  operation X3 (history-removal)  — removed span carries a claim tag, qualifier, RID or math: '`[DEF]` [RID: TDRG-DEF-CANONICAL-BRANCH] '
OK    N4 Appendix A names an identifier absent from the live text    exit 1 (want 1)  FAIL  operation S2-A (history-appendix)  — history entry names identifiers absent from the live text: ['TDRG-ALG-NEW-INVARIANT']
OK    N5 history-removal of a span not marked as history             exit 1 (want 1)  FAIL  operation X5 (history-removal)  — removed span is not marked as history: ' | Theoretically loaded'
OK    N6 two footer lines                                            exit 1 (want 1)  FAIL  presentation (header, footer)  — 2 footer lines (exactly one required); text after the footer line
OK    N7 base differs from the stage-1 intermediate                  exit 1 (want 1)  FAIL  base identity  — map base_sha256 vs file
OK    N8 a claim tag changed under the label of a reference substitution exit 1 (want 1)  FAIL  operation X8 (ref-subst)  — changed text is not reference text: 'ALG' (offending: ['ALG'])
RESULT: PASS
```

## 5. What the change does not touch

- **Results.** No scientific result, RID declaration, grade in §§2–9, OPEN record (heading, RID, Status line), scope guard or evidence state changes (stage-1 checker C3–C5; compaction check). No engine is run and no number is recomputed.
- **Pins.** The pinned engine, the claim pins of the import (Finding A at `ofn-v0.12`) and the §6.13 AZ source stay as in v2.12.15.

## 6. Found and not changed (reported, not resolved here)

- **Crystallization grade.** In §2 TDR-24B, the `[ADMIN]` note calls the thermodynamic-crystallization claim `[HEUR strong]`, while TDR-22b and §1 grade it `[HEUR]`. This is a grade question for the owners, not a maintenance edit. The readouts keep `[HEUR]`, the owner OPEN record's grade.
- **`[RESULT]` without `[from: …]`.** The §A.sim `[RESULT]`, now in §8, lacks the `[from: TAG]` pairing of Methodology §3.4. It was moved verbatim (D3 (a)). Choosing the source tag is a typing decision.
- **History phrases left in live sections.** Phrases such as "superseded", "historical" and "former", and version references such as "consistent with the v2.12.5–.7 rank-1 finding", "executed in v2.12" and "**(v2.12 note:**" in §6.5 remain. They are part of statements or correction records; removing them would reword claim text. The lint report counts them.
- **§2 shape.** Under D2 (a) the TDR-24A/B/F, TDR-25/26 and OPEN-POLICY-GEOMETRY result bodies stay in §2. The OPEN-registry restructuring is a separately planned later edition.
- **Deviations from the plan.**
  - Plan row C3, the struck-through closed items of the §2 priority list: these lines carry tags and are accurate one-line references, so they stay.
  - Plan row S8: limited to the one hypothesis whose replacement is in the text. The other inline `[COR]` records with content are kept, as Methodology §3.6 allows.

## 7. Pipe items

`pipes/TDRG/` holds no open item; it was read at `main` `93f1986`. Notices after the tag, each `kind: notice`:

| Consumer | Contents |
|---|---|
| `pipes/AZ/` | §6.2 citation at `az-v0.8`; the consumer row restated from AZ's v0.8 §8; nothing asked |
| `pipes/OFN/` | OPEN-OFN-2, CONV-TICK and LEM-NOANNIHIL pins at `ofn-v0.12`; XFER-O08-01 stated as open (decision note to follow) |
| `pipes/PROG/` | Methodology v1.4 migration done; no export or gate changes |
| `pipes/NUMGEN/` | none needed (no NUMGEN-facing content changes); listed for completeness |

## 8. Size (Methodology v1.4 §13.8; `tools/dsn_lint.py --prev`)

```
file: dsn/RTG_DISCRETE_GENESIS_DSN.md
bytes: 157260
lines: 1201
header_chars: 1996
live_body_chars: 144881
appendix_a_chars: 9097
section1_words: 407
orientation_core: {"chars": 63130, "lines": 459, "words": 8022, "core_end_marker_present": true}
header_fields: {"Title": 67, "Date": 26, "Scope": 187, "Document class": 163, "Document status": 136, "Supersedes": 149, "Companion documents": 157, "DSN Methodology": 62, "Status summary": 930, "Programme tier": 75}
appendix_a_words_per_edition: 37 editions, max 251 words
footer_lines: 1
history_phrases_live: {"historical": 7, "superseded": 11, "former": 4, "no longer": 1}
near_duplicate_paragraphs: 0
rids_total: 91
previous: {"file": "tdrg-v2.12.15", "bytes": 196268}
growth_bytes: -39008
growth_percent: -19.9
new_rids: 1
growth_per_new_rid: -39008.0
(informational report; no gate)
```

Counting method: the lint script's own (whitespace tokens; §1 between its heading and the next `## `). Stage-1 intermediate: 191,737 bytes.

## 9. Steps after adoption

| # | Step | Who | State |
|---|---|---|---|
| 1 | Stage-1 and stage-2 reviews | ChatGPT co-owner | *(to be filled)* |
| 2 | Row check | atlas owner | *(to be filled)* |
| 3 | Adoption decision (§10) | PI | *(to be filled)* |
| 4 | Publication commit: header *Document status* ADOPTED with this record; `BASELINE.md` row | TDR-G co-owner | *(to be filled)* |
| 5 | Merge commit (not squash) and annotated tag `tdrg-v2.13` with the published SHA-256 | PI | *(to be filled)* |
| 6 | Notices (§7) | TDR-G co-owner, after the tag | *(to be filled)* |

## 10. Adoption decision

*(to be filled by the PI)*

## 11. Open items carried forward

- **TDR-6:** whether the signed-class set $\mathcal I(X)$ meets the purely relational condition.
- **XFER-O08-01:** custody of Finding A; a decision note follows separately.
- **`largest_center` / TDR-19:** the label-dependent centre choice; a decision note follows separately.
- **§2 OPEN-registry restructuring** (D2 (b)): a later, separately planned edition.
- **§6 items:** the crystallization grade and the `[RESULT]` pairing.
- **N4 follow-up:** the log reading.
