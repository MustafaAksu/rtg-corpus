# RTG State Atlas v0.12 — acceptance record (draft)

**Status:** CANDIDATE, 12 November 2026. Not accepted. Open before acceptance: the change-focused receiving review (§3). `atlas-v0.11` stays the governing tagged Atlas until the PI accepts, the PR is merged and the tag `atlas-v0.12` exists and is verified.
**Object:** a derived, NONCANONICAL Atlas. Acceptance adopts no owner science.
**Recorded by:** Claude, Atlas owner, on branch `claude/atlas-v0.12`. Under CONVENTIONS §4 this record comes before the merge and the tag.

## 1. Object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md`, v0.12 candidate | `cf9d8647b4c33206537e46ca37c7879d4fc33b1a936e0a50330a469f054def55` (523,005 bytes, 1,537 lines) |
| base `atlas-v0.11` | `8d7a43f05a42c6a69b50eb97b98dd96ddda7eea327333ae5cc73e03dee46f358` (520,271 bytes, 1,542 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.12/source_manifest.json` | `c798d2727f35233043fe75e6df0054245a394eaae93f8c214f757de7e8e08e6d` |
| `evidence/atlas/build/refresh_v0_12.py` (builder and checks) | `e01435b95a2cce802202cf1a5191c7205c1c2216569e7ab06c44ed828b41f389` |
| `evidence/atlas/v0.12/edit_log.json` (39 operations, old and new text with hashes) | `45a068fa0669317ae5dd3915641bbe308814e884d3ce9a6d5eb1fe617cf9f7e4` |
| `evidence/atlas/v0.12/dispositions.json` | `177582bd06bf4e4c8be1cb41f5466cec41699749bff5dace7f9286dcbfe8ca75` |
| `evidence/atlas/v0.12/retired_l5_keys.json` | `4c56f0822e89d45f94595bbb608732312413d3e2619fd72dcfeb840275269e81` |
| `evidence/atlas/v0.12/coverage_map.json` | `e90a3c0b12386bf2d6d1ab5da82fc21910658fbf10dc9bd6c21547a1e811bf27` |
| `tools/atlas_check.py` (unchanged since v0.9) | `2141e0b991f21acfa2c4f2e0575e88d3ae5d1f43bffd00dafc4ef80d66f66373` |

**Source snapshot:** `main` `c8e71980d053545edcc2f4d1fc5ccf92460de48f` (after PR #219). **Moved sources (2 of 18):**

| Key | v0.11 | v0.12 | Tag target | SHA-256 | Authority |
|---|---|---|---|---|---|
| AZ | `az-v0.6` | `az-v0.7` | `b1c30b7a2d425bd6d7400c49ede0a491b1b2a453` | `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94` | `records/az/AZ_v0_7_RELEASE_RECORD.md` |
| DYAD | `dyad-v6.4.23` | `dyad-v6.4.24` | `f0af6392ed560b55aedc640bc166f0b87f612f7c` | `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16` | `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md` |

The builder asserts for all 18 sources: tagged bytes equal the manifest hash, the tag resolves to the manifest commit, the bytes at the snapshot equal the tagged bytes, and no newer tag of that study exists. Sixteen inputs are byte-equal to their v0.11 inputs.

**Reproduce.** `python3 -I evidence/atlas/build/refresh_v0_12.py` from the repository root rebuilds the candidate from the `atlas-v0.11` bytes, writes `evidence/atlas/v0.12/` and stops on any failed assertion.

## 2. What changed (39 logged operations; net −5 lines, +2,734 bytes)

**AZ v0.7** (corrections edition; no new AZ science; Thread C byte-identical at the owner):

| Atlas item | Change | Owner basis |
|---|---|---|
| **AZ.A1** (D-WRONG, high) | **retired.** The D-WRONG list is empty ("none at this edition"). H2 loses its AZ conflict and is typed D-LINK; the OPEN-M audit node and OPENM.U11 point to AZ §6 as now consistent | AZ v0.7 §6, Appendix B; OPEN-M v0.7.1 R15/R16 |
| **AZ.A2** (two rows) | **retired.** `DYAD-THM-Q403-PHASELAW` lists AZ as an import-ref consumer | AZ v0.7 §4.1.1, §4.1.2, §6, §8 |
| **AZ.A3** | **retired.** The closed Programme request leaves the D5 frontier line; PROG.G6 notes that AZ v0.7 is not the §9.2 pass | AZ v0.7 §7; release record §9 |
| **AZ.A7** | **retired.** H3 and DZT.Q1 keep the DZT half; the Q3 and ℤ_N-state nodes and the two AZ ledgers cite owner RIDs | AZ v0.7 §4.1, §4.2, §8; Dyadic v6.4.24 Appendix F |
| **DYAD.X11** | **retired** (owner's addition to the reviewer's map, see §3). AZ imports the raw-cubic theorem as the raw one-step statement for p≥3 with the owner caveat; the caveat stays on the `DYAD-THM-RAW-CUBIC` node | AZ v0.7 §4.1.1, §8; Dyadic Appendix E |
| AZ.A5, D5.X3 | kept unchanged | SG-AZ-7, SG-DZT-1 |
| Thread C block | statements, grades and the static-geometry verdict unchanged; one evidence qualifier added on the engine node, stated to hold for the whole block: none of the Thread C files is in the repository at the edition (`EV-SRC-REPORTED`, `EV-NOT-RERUN`); the later [SESSION] custody record is named and declared not owner text | AZ v0.7 §9 |
| SOURCES, D2 and D5 headers, pins | `az-v0.7`; Thread A pin `dyad-v6.4.23` as AZ now pins it | AZ v0.7 header, §8 |

**Dyadic v6.4.24:**

| Atlas item | Change | Owner basis |
|---|---|---|
| three pseudo-ID records | become `DYAD-ALG-NOT-AREA-PRESERVING` (grade ALG as the owner retagged it; THM before), `DYAD-ALG-P6-LINEAR-ORDER`, `DYAD-ALG-HOMOLOGICAL-RESONANCE`; statements unchanged | §1, §6.1, §6.6 |
| **DYAD.X4** | **narrowed**, not closed: the cubic radial rate across p stays without a Dyadic RID by owner decision | Appendix A v6.4.24 |
| new node | `DYAD-THM-OPEN21-SHARP-ROWS`, THM·c, conditional on `RECOG-THM-R9-SHARPENED-ROWS` (consumer pin `recog-v0.3.26` §6.13a, as the owner pins it), rows A and B with their own constants, not mixed; the adopted OPEN 21 node is unchanged | §6.14, §7 |
| OPEN 20 frontier line | carries the owner's [SESSION] state-of-work paragraph on the analytic branch; no result claimed, B-an and B-6 stay open | §2 OPEN 20 |
| SOURCES, D2 header | `dyad-v6.4.24` | header |
| not changed | `DYAD-DEF-PRIMITIVE-MAP` (the Atlas never carried "provisional"; its scope is already "PROG P0 reference map"); `DYAD-ART-BRIDGE-NOTE` (not an Atlas item; its replay appears as `cert` on two nodes) | §1, §8 |

**Pipes:** NUMGEN.N-I1 restated at the new snapshot (107 items: 52 closed, 4 dispositioned, 51 open).

Full old and new text of every operation: `edit_log.json`. Disposition of sixteen L5 keys touched or checked: `dispositions.json` (5 retired, 5 reworded, 6 retained).

## 3. Checks, limits, and points for the reviewer

**Checks (all in the builder; a failed one stops the build).**
- `tools/atlas_check.py` with the v0.12 manifest, the coverage map and the cumulative retired-key list: **0 FAIL** — sources 72, coverage 137, qualifiers 4, links 507 PASS / 5 UNVERIFIED / 10 documented-unresolved (one fewer: `DYAD-ALG-Q3-CANCEL` is no longer cited), artifacts 115 / 3 UNVERIFIED, keys 152, wording 12 WARN (none new). The checker's own 18 controls pass.
- 18 focused negative controls, each detected (`negative_controls.json`): a retired key cited or reused; stale source rows; a misspelled new RID; the new theorem shown unconditional, with mixed rows, or with its consumer pin moved to the newest RECOG edition; THM kept against the owner's ALG; a registered RID shown as a pseudo-ID; DYAD.X4 shown as closed; the OPEN 20 pilot read as a result; the [SESSION] recovery read as owner evidence; the `4|q` rule read as dynamics; AZ.A5 dropped; the withdrawn sentence listed as a current D-WRONG; the DZT half of the identifier finding dropped; the raw-cubic import without its caveat.
- Owner facts asserted on the tagged files (`verification_summary.json`, `owner_facts`): thirteen statements, among them that the "legal ×2" sentence occurs in AZ v0.7 only as the withdrawn quotation, that every AZ-owned identifier of v0.6 is still present in v0.7, and that the Dyadic entries carry the tags stated above.
- HEADLINE → L5: no dangling key; no high L5 row without a headline (109 L5 rows).

**Correction to the v0.11 record.** The v0.11 check was run with the tool's default retired-key list (31 keys), not with the cumulative list of v0.10 (142 keys); the record's sentence "the same counts as v0.10" was wrong in the `keys` column. The v0.12 builder reruns the checker on the adopted v0.11 bytes with the cumulative list: **0 FAIL**, coverage 132, links 499/5/11, artifacts 110/3, keys 142. The v0.11 object is unaffected; the v0.11 record is frozen and is corrected here.

**Limits.**
- Structural checks only. No owner certificate was rerun. New RIDs are checked for presence in the tagged sources, not re-proved.
- Two sources were re-read; sixteen were not. AZ v0.7 was read at statement level (header, §§2, 4.1, 4.2, 6–9, Appendix B) and through its release record; its 59 edits were not re-compared one by one with their owner texts. Dyadic was read in the diff against v6.4.23.
- `tools/atlas_preservation.py` was not used: a refresh changes the title line, which changes the recorded heading context of every region (limit recorded at v0.11). The edit log is the reproducible change map; it shows exactly 39 anchored operations and the builder asserts that replaying them reproduces the candidate.
- One coverage-map entry is new: Dyadic v6.4.24 §7 declares an import row for `RECOG-THM-R9-SHARPENED-ROWS`, which the Atlas states inside RECOG's R9 node (D3) rather than as a node of its own; the entry names that node as the reviewed shared home.

**Points on which the owner asks the reviewer's reading.**
1. Retiring DYAD.X11 (not in the reviewer's impact map, PR #225).
2. The Thread C evidence qualifier: its wording, its placement on one node for the block, and the mention of the [SESSION] custody record.
3. H2 retyped from D-WRONG/D-LINK to D-LINK, and the empty D-WRONG list kept as a section.
4. The OPEN 20 paragraph: length and whether a [SESSION] owner paragraph belongs on an L3 line.
5. The new theorem's node against Dyadic §6.14 (constants, premise, pin).

## 4. Decision

**Receiving review:** requested from ChatGPT, Atlas co-owner; the reviewer's impact map (PR #225, `records/atlas/ATLAS_V0_12_CHATGPT_SOURCE_IMPACT_PREPARATION_20261111.md`) was read before the build and its §5 criteria are the ones answered above. Open.

**PI acceptance:** not yet given. Recorded here verbatim when given, with the object hash it refers to.

## 5. Publication (after acceptance; the PI executes)

1. `BASELINE.md`: the owner sets the ATLAS row to v0.12 with the hash of §1 and this record, on the branch before the merge.
2. Merge the PR into `main` with a merge commit, not squash.
3. Annotated tag `atlas-v0.12` on that merge commit, after checking the file hash on `main`.
4. The Atlas owner closes the two dispositioned `pipes/ATLAS/` items and writes the tag verification.

A merge, a tag or a passing check is not an adoption.

## 6. Carried forward

- Everything in §5 of `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md` and §5 of the v0.11 record that this edition does not change.
- Advisory rows of 10 November: rows 1 and 3 (AZ) are resolved and their L5 keys retired here; row 2 (DZT), row 4 (OPEN-M) and row 5 (Legacy, Pre-Legacy) stand.
- AZ: Action 1 (token resonance) and the Thread C recovery are [SESSION] work and are not Atlas content until an AZ or TDR-G edition adopts them.
- Method v0.3 delta (size aim; K1/K2 at refreshes; satellite repositories out of scope): separate.
