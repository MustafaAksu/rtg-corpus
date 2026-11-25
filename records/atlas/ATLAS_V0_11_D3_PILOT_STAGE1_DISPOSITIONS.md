# Atlas v0.11 — D3 pilot, stage 1: dispositions for the six scientific identifiers with two record lines

**Date:** 10 November 2026. **By:** Claude, Atlas owner. **Status:** [SESSION] proposal for review. No Atlas byte changes in this record; nothing adopted. `atlas-v0.10` governs.
**Frozen base:** `atlas/RTG_STATE_ATLAS.md` at `atlas-v0.10`, SHA-256 `443b5990e6082599d1f43fca7d4d24e512e7a632ec395aa56f05bed16f53dbf7` (equal on `main` `7d6eb4c`). All 18 source tags of the v0.10 manifest are still the newest tags of their studies and resolve to the manifest commits (checked 10 Nov 2026), so no impact refresh is due before the pilot.
**Tool:** `tools/atlas_preservation.py` rev. 3 (`6a4047b0…1d62`); occurrence keys and hashes below are from its extract of the frozen base.

## 1. Why stage 1 exists

Method v0.2 §4(4) asks for one node per claim; an imported or consumed claim gets an edge to the owner's node, not a second record. Six scientific RIDs have two record lines in v0.10. Resolving them changes record text and removes record occurrences, so it is not a compaction: it is a separate, reviewed delta whose hashed output becomes the base of the D3 compaction (stage 2). Grade and scope questions are decided here and are not carried into stage 2.

## 2. Classification

In every pair both lines state the same owner claim at the same grade. None is a distinct claim and none is an edge only. The short line sits in the consumer's domain and restates part of the full node.

| RID | Short line (key, line, heading, bytes, hash) | Full node (key, line, bytes, hash) | Role |
|---|---|---|---|
| `RECOG-THM-R9-MEMORY` | `#1`, L392, D2 "return phase: OPEN 3, OPEN 21, L-PHASE, L-MONO, defect growth", 345, `7b9ec0236849` | `#2`, L718 (D3), 1,370, `d17dcd6ae7a7` | second home in D2 |
| `RECOG-THM-P2-HET` | `#1`, L419, D2 "ISP, footprint, chirality (IA)", 110, `b2ca3a7bfa0c` | `#2`, L752 (D3), 831, `e57c3d0b12e7` | second home in D2 |
| `RECOG-THM-P2-C0-FIRST` | `#1`, L420, same heading, 142, `ea000995ffe1` | `#2`, L753 (D3), 829, `26f654854448` | second home in D2 |
| `RECOG-ALG-NU3-CLOSED-FORM` | `#1`, L462, D2 "p-resonance arithmetic (OPEN 9) and its transforms", 341, `33985171274b` | `#2`, L702 (D3), 550, `f5d1b8c9d53a` | second home in D2 |
| `RECOG-ALG-CHART-LAWS` | `#1`, L373, D2 "normal form and chart (finite jets only)", 323, `07357b826616` | `#2`, L744 (D3), 562, `6425cea13bf6` | second home in D2 |
| `NUMGEN-N3D-FINITE-CHAR` | `#2`, L1351, D5 "Discrete realization of ratio classes", 196, `fc0cc8b3e3c6` | `#1`, L511 (D2), 286, `889c4765cc63` | second home in D5 |

## 3. Does the short line carry anything the full node lacks?

A second home may only become a cross-reference if nothing is lost. Each short line was compared with its full node and with the rest of the Atlas.

| RID | Content of the short line not in the full node | Where else it is in v0.10 | Consequence |
|---|---|---|---|
| R9-MEMORY | (a) G=(1−2iτ)a₀₅/(1−6iτ)=−(43+5611√3i)/1270080, \|G\|≈0.0076520; (b) "resonant (0,5) slot carries the comparator-invisible phase"; (c) "¬ physical inheritance" | (a) at L625 (R9 observable) and L714 (`RECOG-ALG-LATTICE-MEMORY`); owner RECOG §6.13 states the value. (b) nowhere else: Atlas wording, not owner text ("comparator-invisible" does not occur in the RECOG DSN). (c) the full node has "¬ physical event" and "¬ direct use in C_W^(h) track". | (b) is kept verbatim on the reference line, marked as the D2 reading. (a) is not repeated; the reference names L714's node. (c) kept verbatim. |
| P2-HET | none ("entering the PRIM-CTR tube" ↔ "entry into U … tail <DYAD-THM-PRIM-CTR") | — | plain reference |
| P2-C0-FIRST | none | — | plain reference |
| NU3-CLOSED-FORM | Re(λ̄ν₃(e^{iθ}))=−sin²(θ/2) ⇒ Re μ_p^Z=−p sin²(π/p)<0, k_ret(p)=3 ∀p≥5 | L705 `*RECOG:radial-identity` and L703 `RECOG-ALG-NU3-NONVANISHING` (D3); owner: RECOG §6.10 names the radial identity a sub-statement of this RID | not repeated; the reference names the D3 radial-identity record |
| CHART-LAWS | notation `J_NF` (full node writes `J(z)`); the tag "(SG-19)" on 245/216≠47/54 | `J_NF` is the D2 notation (L358–L366); SG-19 is Dyadic's guard, cited on many D2 lines | the reference keeps "245/216≠47/54 (SG-19)" verbatim as the D2 guard; notation question below |
| N3D-FINITE-CHAR | "(SG-NG-3/4)" | the guards themselves are at L1382 ff. | kept verbatim on the reference line |

**One open point for the reviewer.** CHART-LAWS: D2 writes `J_NF`, D3 writes `J(z)` for the same jet. This is a notation difference between two homes of one claim, not a scope difference; the reference line will say "J_NF (D2 notation) = J(z) of the node". If the reviewer reads it as a possible object difference, the pair is left as it is and recorded as deferred.

## 4. Proposed stage-1 action

For each pair: the full node stays byte-identical. The short record line is replaced by a typed cross-reference line that is not a record (it starts with `→`, as the birth-symmetry reference of v0.10 does), in the same place under the same heading, carrying only (i) the pointer to the node and its domain, (ii) any text from §3 that exists nowhere else, verbatim, and (iii) the consumer-domain reason for the pointer where the short line gave one.

*(Prediction written before the build; superseded by the measured result in §7: 12 pending, 7 mapped, 2 context reviews.)* Expected mechanical result against the frozen base, with a map that declares each replacement: six declared deletions of record occurrences and six declared insertions of reference lines (12 `DECLARED_PENDING_REVIEW`), everything else `EXACT`, 0 `FAIL`, no context review. The grade invariant holds: each RID keeps its grade on its remaining occurrence. The twelve pending items are exactly what the reviewer is asked to read; none is claimed preserved by the tool.

The seven other multi-occurrence identifiers (five `*GEN:`/`*NUMGEN:` pseudo records and two `GEN-ART-` artifact rows) are outside D3 and are not touched by the pilot; they stay a recorded, deferred debt (design note §7).

## 5. After stage 1

Stage 2 is the D3 compaction proper, against the hashed stage-1 output: movement map, comparator report with 0 FAIL, every pending item and every context review listed for review, two byte-identical builds, `tools/atlas_check.py` 0 FAIL. Size is reported, not gated. Acceptance of the pilot is not an Atlas edition; v0.11 as a whole is decided after the pilot's result.

## 6. Requested

Review of §§2–4: the classification, the no-loss table, the `J_NF` point, and the form of the reference line. On acceptance the owner builds stage 1 (builder, map, comparator report) and submits the twelve pending items.

## 7. Stage 1 built (10 November 2026, after the review of §§2–4)

The review (PR #204 review 5839419629) is ACCEPT WITH CHANGE: classification and no-loss table accepted; `J_NF` and `J(z)` are the same defined finite normal-form jet (not F̂, not the raw jet, not the archival Lie-gauge object), so the sixth pair is not deferred; the reference line needs an explicit `<RID` edge and `@OWNER§`; the movement map must remap the five full RECOG nodes from occurrence `#2` to `#1`. All applied.

**Files** (`evidence/atlas/v0.11_pilot/`): `build_stage1.py` (asserts the base hash and each replaced line's hash), `RTG_STATE_ATLAS_stage1.md`, `stage1_movement_map.json`, `stage1_compare_report.json`, `stage1_pending_items.md` (the six before/after pairs, verbatim). The live `atlas/RTG_STATE_ATLAS.md` is not changed.

| Item | Result |
|---|---|
| Stage-1 output | SHA-256 `0f8ba5c0e34dcbbaaa11858e2d568a9f5d5ced63aeca8ee69a44c973d7a1a6c2`, 521,832 bytes (base 521,243; +589: the reference lines carry explicit edges and locators) |
| Comparator (`atlas_preservation.py` rev. 3) | **MECHANICAL PASS**: 1,414 EXACT, 12 DECLARED_PENDING_REVIEW, 7 MAPPED_EXACT, 0 FAIL |
| Context reviews | 2 (see below) |
| Two builds | byte-identical |
| `tools/atlas_check.py` on the stage-1 text | 0 FAIL; counts equal to v0.10 (links 499/5/11, keys 142, wording 12 WARN) |

**Difference from the predicted result.** The prediction was 12 pending, 5 mapped, no context review. The run gave 7 mapped and 2 context reviews. Cause: lines 754 and 755 (`RECOG-NUM-P2-C0-FIRST`, `RECOG-NUM-P2-HET-NEG`, records with a `NUM+` grade form the tool keeps as raw lines) follow the full `RECOG-THM-P2-C0-FIRST` node and are anchored to it. Renumbering that node `#2 → #1` changes their anchor key, so the tool refused them until the map declared them, and then listed both as context reviews. Their bytes, position, heading context and the record they follow are unchanged; only the occurrence number in the anchor key differs. This is the tool behaving conservatively, not a scope change, and it is left visible rather than tuned away.

**Reference-line contents, by pair** (full texts in `stage1_pending_items.md`):
- R9-MEMORY: the Atlas wording "resonant (0,5) slot carries the comparator-invisible phase" is kept verbatim and labelled "Atlas reading, not owner text"; G is not repeated, the line names `RECOG-ALG-LATTICE-MEMORY` (D3); "¬ physical inheritance; ¬ C_W^(h)" kept verbatim.
- P2-HET, P2-C0-FIRST: the D2 statement kept verbatim as "D2 use".
- NU3-CLOSED-FORM: names `*RECOG:radial-identity` and `RECOG-ALG-NU3-NONVANISHING` (D3) for the radial identity and k_ret; negative kept verbatim.
- CHART-LAWS: `J_NF` identified with `J(z)` as the defined polynomial jet only; "245/216≠47/54 (SG-19)" and the sign remark kept verbatim.
- N3D-FINITE-CHAR: "pure representation theory" stated; the negatives with "(SG-NG-3/4)" kept verbatim.

**Requested:** review of the twelve pending items and the two context reviews. On acceptance, the stage-1 output with this hash is the frozen base of the D3 compaction (stage 2).

**Accepted** as the intermediate base for stage 2: PR #204 review 5840025491 (ACCEPT SCOPED, 10 November 2026; reviewer recomputed both file hashes and the six changed lines). Stage 2 result: `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md`.
