# Discrete Genesis (TDR-G) v2.13 — Release Record

**Status:** DRAFT, round 2. The candidate is built in two stages and checked. The ChatGPT co-owner reviewed round 1: stage 1 CONDITIONAL PASS, stage 2 PASS. Its two corrections are applied in round 2 (§3a), and the co-owner's readback of round 2 is PASS (review closed). Before adoption it needs:
- the atlas owner's row check;
- the PI's adoption.

**Date:** 13 November 2026.

**Prepared by:** Claude, TDR-G co-owner session `claude01SKePJ`, on branch `claude/tdrg-v2-13`.

**Edition:** v2.13, a maintenance edition. It migrates the document to Methodology v1.4 and pins AZ at v0.10 (v0.8 in the plan, v0.9 after F1; PI option 1; atlas row check F1). No scientific result changes, and nothing is rerun.

**Predecessor:** `RTG_DISCRETE_GENESIS_DSN` v2.12.15, tag `tdrg-v2.12.15`, SHA-256 `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64`.

Fields marked *(to be filled)* depend on steps that have not happened yet. Every hash below was computed on the branch files by `evidence/tdrg/v2.13/fill_release_record.py`; none was typed by hand.

## 1. Mandate, plan and decisions

| Step | Source | State |
|---|---|---|
| Cycle started | PI, 13 Nov 2026, 12:07 +03:00 ("onaylıyorum"), approving one candidate (v1.4 migration plus AZ v0.8 pin) with separate decision notes on XFER-O08-01 and `largest_center` / TDR-19 | given |
| Plan | `records/tdrg/TDRG_v2_13_EDIT_PLAN.md` (PR #263): rows S1–S8 and C1–C6, decisions D1–D3 | written |
| Co-owner evaluation of the plan | ChatGPT co-owner, relayed in the session at 12:06 +03:00. Agrees with the order. Stage 1 carries pins, structural fit and scope corrections; stage 2 is compaction only, with a movement map; results, RIDs, grades and OPEN states are preserved; the TDR-6 relational question is not a closing condition | not a repository record |
| PI decisions | "1- a 2-a 3-a" (13 Nov 2026, 12:23 +03:00): D1 (a), §1 as readouts; D2 (a), §2 history only; D3 (a), §A.sim to §8. Recorded in plan §7 | given |
| Stage 1 review | ChatGPT co-owner (change-focused): `records/tdrg/` review record on PR #268 (head `da61a6c8`, open at round 2); GitHub review `5906863206` on PR #265. Round 1 (intermediate `b24c17cc…cdcc`): CONDITIONAL PASS — R1 (methodological): the unpaired `[RESULT]` moved into live §8; R2 (record): the RID-growth metric | R1 and R2 applied in round 2 (§3a). Readback on head `f38c538` (PR #268 head `c9925513`; GitHub review `5906970313`): PASS — R1 and R2 closed; no objection to the narrowing of D3 (a) to the table; review closed |
| Stage 2 review | ChatGPT co-owner (mechanical), same record: round-1 candidate `1691a136…ee18` reproduced byte for byte by an independent implementation of the 43 operations | PASS on round 1; stage 2 rebuilt from the round-2 intermediate (§3a). Readback: candidate `c89eb81b…0a14` reproduced byte for byte by the independent implementation (43/43 operations; 81 RID declarations and 21 OPEN records kept) — PASS |
| Row check | atlas owner: `records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_13.md` (PR #277, merged to `main`). First check at head `fba3ea1`: build sound and reproducible; F1 recommended. Follow-up at head `40d8235`: F1 and F2 closed; ACCEPT FOR ADOPTION (atlas side) of candidate `c79898f9…36f4` | superseded by §3c; re-check of the current candidate *(to be filled)* |
| Adoption, merge commit, tag `tdrg-v2.13` | PI | *(to be filled)* |

## 2. Identities and build

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v2.12.15) | `git show tdrg-v2.12.15:dsn/RTG_DISCRETE_GENESIS_DSN.md` | `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64` |
| Stage-1 intermediate (a build stage, not an edition) | `git show b7687f11c38f8adc5af2e4d42ff5c74a4e7f2dce:dsn/RTG_DISCRETE_GENESIS_DSN.md` | `a27c3c525a4500ee4f62974ae5d508dbc5fdb450a4e2fe06ae8f6f46716775eb` |
| **Candidate v2.13** | `dsn/RTG_DISCRETE_GENESIS_DSN.md` | `6a4b94d5ec6946cad177889d453044a69eb4aa451763a2e81148b2e11739de88` |
| Stage-1 builder | `evidence/tdrg/v2.13/stage1/build_tdrg_v2_13_stage1.py` | `ea44547fae350e90c4872a6f33f7660d5854b84669ff1cbdbe86bc5a0352f332` |
| Stage-1 checker | `evidence/tdrg/v2.13/stage1/check_tdrg_v2_13_stage1.py` | `c98efd8df26ef89c9cb27332abbe2200aa4313692201ffb30402c3b95fec768c` |
| Stage-1 edit log (29 edits) | `evidence/tdrg/v2.13/stage1/edit_log.json` | `29844c3f1044ec1d5ef03d018685685065ce97f96f71241bf2a04ecc34744422` |
| Stage-1 gates / controls output | `evidence/tdrg/v2.13/stage1/check_output.txt`, `controls_output.txt` | `94486ec86e8ba61445937536e595257f387c3fa88c67cdc95628274008ed9019`, `befa181965d3cc11a8653971deb17ba8c67121c591e761d29aa26008bda252a4` |
| Stage-2 builder | `evidence/tdrg/v2.13/stage2/build_tdrg_v2_13_stage2.py` | `1d8304b1e1f3dc364bd38b353978de3dc17cf32422b4f0c58a2c0ee4e29eb9da` |
| Movement map (43 operations) | `evidence/tdrg/v2.13/stage2/movement_map.json` | `72408186ed90ed7fa993816668471aabe9abfd583cb974f8ff9f40b306d0fde5` |
| Compaction check output / report | `evidence/tdrg/v2.13/stage2/check_compaction_output.txt`, `check_compaction_report.json` | `20fec15a43c304841b7582bd8c6d241024e0c4b68840e004d9ee75f8bdd45f70`, `95d43ba730a07772e595d284a25d9a4f72b0abe9dc8cf464bb9fbc8f3281e3b9` |
| Stage-2 negative controls and output | `evidence/tdrg/v2.13/stage2/stage2_negative_controls.py`, `stage2_negative_controls_output.txt` | `474fcaca0d65bb244488ece9ddcf2b7d332b5df150c4ec042bb717e9c782340f`, `11db6b0971019586b13139ee56e0da48490ad0763447dfe7f568419d515a3bbb` |
| Compaction checker (repository tool, unchanged) | `tools/check_compaction.py` | `d2977b3e24fd54a1d85fe53ea88f65dd51a9e26890b56b17ab5855716b57d87c` |

**Reproduce** (from the repository root, with the tags present):
```
T=$(mktemp -d)
git show b7687f11c38f8adc5af2e4d42ff5c74a4e7f2dce:dsn/RTG_DISCRETE_GENESIS_DSN.md > $T/inter.md
python3 -I evidence/tdrg/v2.13/stage1/build_tdrg_v2_13_stage1.py --out $T/rebuilt.md --log $T/log.json   # = inter.md, = edit_log.json
python3 -I evidence/tdrg/v2.13/stage1/check_tdrg_v2_13_stage1.py --intermediate $T/inter.md [--controls]
python3 -I evidence/tdrg/v2.13/stage2/build_tdrg_v2_13_stage2.py --emit-base $T/base.md   # writes the candidate and the map
python3 tools/check_compaction.py $T/base.md dsn/RTG_DISCRETE_GENESIS_DSN.md evidence/tdrg/v2.13/stage2/movement_map.json
python3 -I evidence/tdrg/v2.13/stage2/stage2_negative_controls.py
```
The stage-1 builder reads its base from the tag. The stage-2 builder, the map and the controls read the intermediate from commit `b7687f1` and assert its hash, so no second copy of a DSN state is kept (Methodology v1.4 §13.7).

## 3. Stage 1 — what changes, by decision (29 edits; `edit_log.json`)

| Plan row | Edits | What changed |
|---|---|---|
| S1 — AZ pin (with F1 and option 1, §3b–§3c) | E13, E25, E26 | §6.2 cites `AZ-ALG-ANTIPODAL-LOWORDER` at `az-v0.10`. Checker C6 shows the entry is byte-identical at `az-v0.6` to `az-v0.10`. The AZ consumer row is restated from AZ's own v0.10 text: AZ §8, IMP-B, cites TDR-G at `tdrg-v2.12.15`, follows the LEM-SPECCONS generalization and adds the TDRG-ALG-EVENT-INVENTORY / TDRG-ALG-TOKEN-CENSUS-LAW and TDRG-ALG-PARENT-CHILD-PHASE rows; AZ-NUM-TOKRES-S1 and AZ-NUM-TOKRES-S2 are named as AZ's numerical diagnostics, not TDR-G results (their grades in words, not as TDR-G tags); the two AZ identifiers with a `TDRG-` prefix are AZ's, not TDR-G RIDs, and are not named, so that no tool reads them as TDR-G identifiers. The pin line names the verified source editions used by this release, not "governing" editions. |
| S2 — Methodology | E01, E02 | The header declares v1.4. The alias sentence names v1.4 §8.1; its v2.12.14 history (the legacy rows, which carry tags) stays in the tagged predecessor. |
| S3 — historical pins | E06, E07, E15, E19, E26 | The OPEN-OFN-2 connection of TDR-1 and TDR-19 points to `ofn-v0.12`, where OPEN-OFN-2 is open as `RTG-OFN-OPEN-DISC-INTERACTION`. CONV-TICK and LEM-NOANNIHIL name their current consumer rows, OFN v0.12 IMP-O08-14 and IMP-O08-06; OFN imports LEM-NOANNIHIL as `[ALG]`, so the old "`[RESULT]` `[from: ALG]`" description of OFN v0.7 leaves. No claim-specific historical pin remains in the live text. |
| S4 — owner-review tasks | E05 | Stated as TDR-G's own current items (Programme v1.4 does not carry them; checker C6), with the same four statuses. |
| S5 / D3 (a) — §A.sim | E28 | The table is copied verbatim into §8 as "Simulation artifact evolution" (checker C8). Its closing interpretive `[RESULT]` is not promoted (round 2, §3a). Stage 2 removes the Appendix A copy. |
| S6, S7 / D1 (a) — §1 and summary | E03, E04 | §1 has 407 words of readouts with RIDs and pointers. Checker C7 requires that 24 statements dropped or shortened (formulas, fit values, rates, the factorization precision, the slot-volume fits, the $q_{\rm proj}$ correction and others) still occur at their home outside §1. The status summary has three present-state sentences. |
| Typing of the summary (part of D1 (a)) | E04 | The old §1 graded some summaries more strongly or more loosely than their owner records. The readouts now carry the owner grades: the band form of reachability is `[ALG]` as LEM-REACH in §6.5 (old §1: under `[THM]`); the policy branches are `[NUM]`, `[NUM]` and `[HEUR strong]` as in §6.6 (old §1: one `[NUM strong]` for all three); BIND3 is `[ALG]` for the exact enumeration and `[NUM strong]` for parity and the spectral gate, as in §6.12 (old §1: `[NUM strong]` throughout). No grade in §§2–9 changes (checker C4). The old §1 sentence "No plateau through $N=1080$" is not carried: the §6.8 table extends to $N=1440$, and the statement is stale. |
| S8 — superseded hypothesis | E10, E11, E29 | The v2.8 failed-relock hypothesis leaves TDR-25. Appendix B records it as `[SUPERSEDED]`, quoting its original statement verbatim (checker C9), with its reason and replacement. The bullet that revised it now points to Appendix B. |
| D2 (a) | E09 | The TDR-24B record stays in §2. The sentence announcing its move to Appendix A "in v2.13" is replaced by "The paragraphs below are the supporting record." |
| XFER-O08-01 | E24 | Stated as **open**, a separate decision of both owners (PI, 13 Nov 2026); previously "deferred to v2.13". |
| Correction labels with a tag | E08, E12, E14, E16–E18, E20–E23, E27 | Eleven "*(v2.12.x `[COR]` …)*" labels are removed. Each correction is recorded in Appendix A and in its release record. Where a label carried a qualification (CONV-TICK step 4, the gcd converse, the mirror-inventory scope), the qualification stays. |

**Checks, stage 1** (`check_output.txt`, `controls_output.txt`): RESULT: 11/11 gates pass — C0 base; C1 build; C2 confined; C3 RIDs; C4 tags; C5 OPEN; C6 pins; C7 §1; C8 §A.sim; C9 App. B; C10 header.

Negative controls:
```
K1 AZ pin back to az-v0.9: CAUGHT (target C6 FAIL; C1 FAIL)
K2 tag changed in an untouched paragraph: CAUGHT (target C4 FAIL; C1 FAIL)
K3 RID declaration dropped: CAUGHT (target C3 FAIL; C1 FAIL)
K4 OPEN Status line changed: CAUGHT (target C5 FAIL; C1 FAIL)
K5 §1 home lost: CAUGHT (target C7 FAIL; C1 FAIL)
K6 §A.sim copy altered: CAUGHT (target C8 FAIL; C1 FAIL)
K7 Appendix B paraphrased: CAUGHT (target C9 FAIL; C1 FAIL)
K8 fifth summary sentence: CAUGHT (target C10 FAIL; C1 FAIL)
K9 stale v2.13 promise reintroduced: CAUGHT (target C6 FAIL; C1 FAIL)
K10 unpaired [RESULT] promoted to §8 (review R1): CAUGHT (target C8 FAIL; C1 FAIL)
CONTROLS: 10/10 caught
```

## 3a. Round 2 — corrections from the review of 14 November 2026

| Review item | Change |
|---|---|
| **R1** (methodological): the closing sentence of §A.sim, "`[RESULT]` Policy and bookkeeping bugs can invert the cosmological interpretation.", reached live §8 without the `[from: …]` pairing Methodology §3.4 requires. Moving the old bytes verbatim proved the move, not the typing in a live section. | The reviewer offered two remedies: a reasoned owner typing decision, or moving only the evidence table. The second is applied. E28 copies only the table into §8; its rows keep their own tags, and none of them is a `[RESULT]`. The interpretive sentence is not promoted; it stays in Appendix A of `tdrg-v2.12.15`, and the compact v2.13 entry of Appendix A says so. No `[from: …]` tag is invented. Checker C8 now also requires that the sentence is absent from the live text; C4 counts one `[RESULT]` fewer; the new control K10 restores the sentence in §8 and is caught. |
| **R2** (record): the size report showed `new_rids: 1` and `growth_per_new_rid: -39008.0` although TDR-G declares no new RID. | §8 below explains that the one new identifier is a citation of OFN's existing `RTG-OFN-OPEN-DISC-INTERACTION` (S3), not a TDR-G RID, so growth per new RID is N/A. The raw lint output is kept. |

Stage 2 is rebuilt from the round-2 intermediate. Its 43 operations are the same; only the Appendix A entry for v2.13 changes, to record R1. The review's stage-2 PASS concerned the round-1 bytes, and the readback covers the rebuilt candidate.

## 3b. F1 — AZ v0.9 (atlas row check, PR #277)

The atlas row check (`records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_13.md`, PR #277) found the build sound and reproducible. It recommended one correction before adoption, F1: `az-v0.9` was adopted on 14 Nov, after the cycle started, so the AZ pin and the AZ consumer row were one edition old. The PI instructed "F1 hemen uygulansın" (relayed in the session, 16 Nov 2026).

**Source changes** were made by the ChatGPT co-owner (`records/tdrg/TDRG_v2_13_F1_IMPLEMENTATION.md`; commits `e4e54ec`–`ddadd8a`):
- `consumers.md` and `pins.md`;
- E13 and E25;
- C6 (four AZ editions, the v0.9 §8 rows, AZ's ownership of AZ-NUM-TOKRES-S1);
- K1 (v0.9 → v0.8 must fail).

The TDR-G co-owner (Claude) completed the propagation:
- In the consumer row, AZ's grade of AZ-NUM-TOKRES-S1 is named in words rather than as a backticked tag, so the TDR-G live text gains no truth tag for an AZ claim; the C4 tag accounting is unchanged.
- The v2.13 Appendix A entry and the stage-2 `known_tags` are updated.
- This record and the AZ v0.9 pipe item are updated (F2).
- Both stages are rebuilt (identities in §2).

No TDR-G result, grade or RID changes. AZ's numerical result is not adopted.

## 3c. AZ v0.10 (PI option 1, 16 Nov 2026)

`az-v0.10` was adopted (PR #276) after the F1 rebuild, so the F1 candidate `c79898f9…36f4` named a superseded AZ edition. Its pin line also called AZ v0.9 a "governing" edition. The co-owner (Claude) compared the two editions:
- `AZ-ALG-ANTIPODAL-LOWORDER` is byte-identical at `az-v0.9` and `az-v0.10`;
- AZ §8 still uses TDR-G v2.12.15 with the same rows. Only AZ's local-use sentences change, to cover its new diagnostic AZ-NUM-TOKRES-S2 and its §4.2.2.

The PI chose option 1, repin to `az-v0.10`, in the session on 16 Nov 2026. The ChatGPT co-owner's relayed note confirms it and adds two points: the sync authorizes no adoption of AZ numbers, and the pin line should name "verified source editions used by this release", so that a later AZ edition does not make it false.

**Changes (stage 1, round 4, commit `b7687f1`):**
- E13 cites `az-v0.10`.
- The E25 consumer row is restated from AZ v0.10 §8, with AZ-NUM-TOKRES-S1 and AZ-NUM-TOKRES-S2 named as AZ-owned diagnostics.
- The E26 pin line is written as verified source editions.
- C6 checks the cited entry at `az-v0.6` to `az-v0.10` and AZ v0.10's §8 rows and diagnostics, and treats "AZ v0.9", `az-v0.9` and "Governing editions" as stale.
- K1 now fails a repin from `az-v0.10` back to `az-v0.9`.
- In stage 2, the Appendix A entry and `known_tags` are updated.

**Policy for later editions:** a newer AZ edition alone does not trigger a rebuild. What decides is whether the cited statement or AZ's use of TDR-G changes.

**Reviews:** the ChatGPT F1 readback, PASS (review `5918564536`, PR #268 `6603997a`), concerned `c79898f9…36f4`. The candidate of this round needs its own bounded readback and the atlas re-check.

## 4. Stage 2 — compaction (43 operations; `movement_map.json`)

The base is the stage-1 intermediate. The operations are:
- the header, in v1.4 field order, with the stage-1 status summary unchanged;
- 40 history-removal edits of version labels without content. Each removed span carries the profile history word `v2.12` and no tag, RID, mathematics or qualifying word, and each is found byte-identical in the intermediate;
- Appendix A: compact entries for v2.13, v2.12.15 and v2.12.14, and one line for each earlier edition, whose full text stays at `tdrg-v2.12.15`; §A.sim leaves;
- one footer line.

**Compaction check** (`tools/check_compaction.py`, `check_compaction_output.txt`): RESULT: PASS, exit 0 — 55 checks, every operation and every global check PASS; 268 claim blocks in base live text: 244 byte-identical, 24 changed by declared operations, 0 unexplained

**Negative controls** (`stage2_negative_controls_output.txt`):
```
base: git show b7687f11c38f8adc5af2e4d42ff5c74a4e7f2dce:dsn/RTG_DISCRETE_GENESIS_DSN.md  sha256 a27c3c525a4500ee4f62974ae5d508dbc5fdb450a4e2fe06ae8f6f46716775eb
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
- **History phrases left in live sections.** Phrases such as "superseded", "historical" and "former", and version references such as "consistent with the v2.12.5–.7 rank-1 finding", "executed in v2.12" and "**(v2.12 note:**" in §6.5 remain. They are part of statements or correction records; removing them would reword claim text. The lint report counts them.
- **§2 shape.** Under D2 (a) the TDR-24A/B/F, TDR-25/26 and OPEN-POLICY-GEOMETRY result bodies stay in §2. The OPEN-registry restructuring is a separately planned later edition.
- **Deviations from the plan.**
  - Plan row C3, the struck-through closed items of the §2 priority list: these lines carry tags and are accurate one-line references, so they stay.
  - Plan row S8: limited to the one hypothesis whose replacement is in the text. The other inline `[COR]` records with content are kept, as Methodology §3.6 allows.

## 7. Pipe items

`pipes/TDRG/` was read at `main` `93f1986` (no open item) and again at `main` `c9e313f`: it holds `20261114-AZ-v0-9-adopted.md` (notice, open on `main`). Its subject — the §6.2 citation and AZ §8 — is what F1 changes; on this branch it is **dispositioned** `2026-11-16 · accept · records/tdrg/TDRG_v2_13_RELEASE_RECORD.md` and is closed after the tag (atlas row check F2). Read again at `main` `2d898fd` (16 Nov): it also holds `20261116-AZ-v0-10-adopted.md` (notice; nothing asked). On this branch it is **dispositioned** `2026-11-16 · accept · records/tdrg/TDRG_v2_13_RELEASE_RECORD.md`, since v2.13 cites `az-v0.10` (§3c), and it is closed after the tag. Notices after the tag, each `kind: notice`:

| Consumer | Contents |
|---|---|
| `pipes/AZ/` | §6.2 citation at `az-v0.10`; the consumer row restated from AZ's v0.10 §8, with AZ-NUM-TOKRES-S1/S2 named as AZ-owned; reply to the v0.9 notice; nothing asked |
| `pipes/OFN/` | OPEN-OFN-2, CONV-TICK and LEM-NOANNIHIL pins at `ofn-v0.12`; XFER-O08-01 stated as open (decision note to follow) |
| `pipes/PROG/` | Methodology v1.4 migration done; no export or gate changes |
| `pipes/NUMGEN/` | none needed (no NUMGEN-facing content changes); listed for completeness |

## 8. Size (Methodology v1.4 §13.8; `tools/dsn_lint.py --prev`)

```
file: dsn/RTG_DISCRETE_GENESIS_DSN.md
bytes: 157864
lines: 1199
header_chars: 1996
live_body_chars: 145191
appendix_a_chars: 9389
section1_words: 407
orientation_core: {"chars": 63130, "lines": 459, "words": 8022, "core_end_marker_present": true}
header_fields: {"Title": 67, "Date": 26, "Scope": 187, "Document class": 163, "Document status": 136, "Supersedes": 149, "Companion documents": 157, "DSN Methodology": 62, "Status summary": 930, "Programme tier": 75}
appendix_a_words_per_edition: 37 editions, max 297 words
footer_lines: 1
history_phrases_live: {"historical": 7, "superseded": 11, "former": 4, "no longer": 1}
near_duplicate_paragraphs: 0
rids_total: 93
previous: {"file": "tdrg-v2.12.15", "bytes": 196268}
growth_bytes: -38404
growth_percent: -19.6
new_rids: 3
growth_per_new_rid: -12801.3
(informational report; no gate)
```

Counting method: the lint script's own (whitespace tokens; §1 between its heading and the next `## `). Stage-1 intermediate: 192,047 bytes.

**RID growth (review R2).** TDR-G declares no new RID in v2.13 (stage-1 checker C3: every declaration is kept and none is added). The lint's `new_rids` counts identifiers new to the text, which are citations of other owners' existing RIDs: OFN's `RTG-OFN-OPEN-DISC-INTERACTION` (S3) and AZ's `AZ-NUM-TOKRES-S1` (F1). Growth per new TDR-G RID is therefore N/A; the raw lint output above is kept as produced.

## 9. Steps after adoption

| # | Step | Who | State |
|---|---|---|---|
| 1 | Stage-1 and stage-2 reviews | ChatGPT co-owner | PASS after round 2 (PR #268, reviews `5906863206`, `5906970313`) |
| 2 | Row check | atlas owner | ACCEPT of `c79898f9…36f4` (PR #277); re-check of the current candidate *(to be filled)* |
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
- **§6 item:** the crystallization grade.
- **N4 follow-up:** the log reading.
