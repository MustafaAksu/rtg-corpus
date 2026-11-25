# Atlas v0.10 — review packet

**Date:** 4 November 2026. **By:** Claude, Atlas owner. The Atlas advises; it does not decide. The PI adopts.
**Status:** DRAFT candidate for review, revision 2 (after the ChatGPT receiving review, CONDITIONAL PASS; §8). `atlas-v0.9` governs until adoption.
**Object:** `atlas/RTG_STATE_ATLAS.md` on branch `claude/atlas-v0.10`, SHA-256 `443b5990e6082599d1f43fca7d4d24e512e7a632ec395aa56f05bed16f53dbf7` (521,243 bytes, 1,543 lines; revision 1 was `ea7faa79…d1bc`). Base: `atlas-v0.9`, `b48343f5a4d4c066eb37a325ff87d1dadf686fc6c616b67e7a0ad418dcec3b70` (1,546 lines).
**Builder:** `evidence/atlas/build/refresh_v0_10.py` (SHA-256 `9405436c738f9c3dd079975ce21d5a4a73d45181a2831634b43c6c7512f2e01c`), run from the repository root with `python3 -I evidence/atlas/build/refresh_v0_10.py`. Two runs gave byte-identical outputs (atlas and all of `evidence/atlas/v0.10/`).
**Shared checker:** `tools/atlas_check.py` (SHA-256 `2141e0b991f21acfa2c4f2e0575e88d3ae5d1f43bffd00dafc4ef80d66f66373`; unchanged since v0.9), with the coverage and identifier maps of `atlas-v0.2`.

## 1. Scope

An impact refresh for three moved sources and the three open items of `pipes/ATLAS/`. There is no compaction, no Methodology migration of the atlas, and no new certificate campaign. Following the ChatGPT scope note, the order is: freeze the source snapshot, then the node and L5 dispositions, then the pipe states. The pipe items are closed only after the tag.

| Key | v0.9 source | v0.10 source | Tag commit | DSN SHA-256 |
|---|---|---|---|---|
| PROG | `programme-v1.3` | `programme-v1.4` | `514e17f3` | `37d857d0…f28c0` |
| GEN | `gen-v2.9` | `gen-v2.10` | `12bb2b39` | `63c3b020…13d62` |
| RECOG | `recog-v0.3.26` | `recog-v0.3.27` | `7bad433b` | `19556f91…0e1f1` |

The source snapshot is `main` `fa3db80a935a20b1eff64b0e14c6d0436f861852` (after PR #181). The builder checks four things for all 18 sources:
- each tag's file equals the file at the snapshot;
- the other 15 sources are byte-equal to v0.9 (`v0_9_input_equality`: 15 EQUAL, 3 CHANGED);
- each tag resolves to the commit in the manifest;
- the three changed SHA-256 values match the release records.

## 2. What changed (83 exact-once edits, `edit_log.json`)

| Group | Edits | Content |
|---|---|---|
| GEN v2.10 | 44 | New node `GEN-ALG-P4-DRIFT-IDENTITY` (after `GEN-THM-DELTA-QC`): the general cubic term is stated first, then the premises L⁶=I and G₂=0. The coefficients have no independent certificate (`GEN-ART-P4-PRIMITIVE` [custody-A]). The D4a `*GEN:birth-symmetry THM` record becomes the one home node `GEN-ALG-BIRTH-SYMMETRY-SEED` `[ALG]`, values unchanged, with GEN's caution that D_birth^[s³]=2Q(V_s) is not by itself a complete next-block increment; the D4b record becomes a cross-reference to it. Chrono-protection gains the independent `[ALG]` route through `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`; it is "a new proof, not a recovery", and `GEN-ART-G2-CHRONO` stays [custody-A]. T-6s/t/u are imported at `[ALG]`; T-6u has the separate Genesis `[CAND]` reading. The NU5-P5 label is now pinned to `dyad-v6.4.23`. Section pointers are repinned. |
| PROG v1.4 | 15 | SOURCES row. Full IF register at v1.4: IF37 and IF38, plus the OFN import/reference typing of IF24, IF28 and IF32. TDR-G launch-gate record (App. C aligned in v2.12.14; one §7 export row still names the old gate). Maintenance state at v1.4 §9.2. H8, H10, D1 and F1 κ-table pointers (12 rows, κ_f included). PROG.G5, PROG.G6 and D5.X1 pointers. |
| RECOG v0.3.27 | 13 | SOURCES row and D3 header. New node `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS` (after `RECIPROCAL-DRIFT`). It uses adopted Dyadic rows only, with c_J≤0.500819 and c₇≤100.231 on q≤q\*, and it is not a Dyadic registration. The (D5) `[assuming:]` is removed at H5, at the log-free envelope (ALG·c → ALG, grade unchanged) and at the two Dyadic consumer edges. The R9 C₇ rows import `DYAD-THM-NF-REM-C7-SHARP`. K_ε is shown outward (0.7204/0.4514/0.1861). The drift "not supplied" note now names the registered C₇ ceiling as not applied. |
| TRIAD finding | 3 | LEGACY.Y6 is retyped D-STALE → D-SCOPE and carries the owner readings. Genesis states the leading one-dimensional transverse birth `[THM]` under the name Φ₂→₃ (§1; `GEN-ART-PHI-2TO3` [custody-A]; no RID); the fifth-order remainder is conditional on the child functional, which is OPEN (GCL-06). Triadic uses Φ₂→₃ as `[DEF]` family notation (§6.1). The Legacy phrase matches the leading theorem and overstates only if read as a certified complete birth or event law, which no owner states. The RER citation is typed reference-only and not load-bearing. |
| identity, currency, pipes | 8 | Title, manifest path, footer. Four "verify/recheck against GEN v2.10" and AZ.A2 pointers. NUMGEN.N-I1 pipe census. |

**GEN pointer rule.** A `GEN v2.9 §X` pointer is repinned to v2.10 only when one of these holds:
- the section is byte-identical between `gen-v2.9` and `gen-v2.10` (§6.2, §6.3b, §6.3c, §6.8);
- the quoted words are present at v2.10 (§2, §6.6, §7, §8).

The builder asserts each case; `gen_repin_evidence.json` lists nine entries. The atlas deliberately keeps "since GEN v2.9" where it dates the introduction of κ_f notation. Consumer-declared pins are left as written: TRIAD at gen-v2.8.7 and gen-v2.9; OFN's own pins.

## 3. L5 dispositions (`dispositions.json`; 26 keys touched)

**Retired (8; keys never reused; `retired_l5_keys.json`)**
- **RECOG.R-A1.** RECOG v0.3.27 discharged (D5) at six A1c sites: TAIL-HARMONICS, SHARPENED-SCHEDULE, LOGFREE-ENVELOPE, START-OFFSET (ii), ADMISSIBLE-REGION, JOINT-CONTRACTOR. It did so by importing BRIDGE and SPIRAL-REM and adding the jet-remainder lemma. The C₇ rows import C7-SHARP. Grades are unchanged. Closing this row means the cross-owner dependency is settled. It does **not** mean an unconditional physical validation.
- **PROG.G8.** v1.4 §8.2 adds the κ_f row and corrects the class-C row (E-P13-1).
- **PROG.G9.** v1.4 §7.2–7.3: IF07 at v1.7. IF11 stays at OPEN M's own pin v1.6. That is the consumer's pin, recorded and not set by the Programme, so it is not a stale pin. CN-05 is received and accepted.
- **F31 + TRIAD.T12.** GEN v2.10 imports T-6s/t/u at `[ALG]`. The T-6u `[CAND]` reading is Genesis's own. The OPEN-M interface use of T-6s stays `[CAND]`.
- **F18 + TRIAD.T10.** Owner reading of both Triadic co-owners: the RER citation is reference-only and not load-bearing. The p=4 remainder bounds are stated conditionally in Triadic. The RER node keeps the typed edge.
- **NUMGEN.N-L6.** GEN v2.10 §6.4 states the cyclic-average application as its own `[ALG]` line, imported at numgen-v1.21. The atlas-derived link has become owner text.

**Reworded, kept open (16).**
- **F30** stays open on the consumer side. Genesis answered both questions; the answers are filed in `pipes/TRIAD/` and are still open. TRIAD v1.7 still holds gen-v2.8.7 for the radial polynomial and imports birth symmetry as `[THM]`. The repin and the import grade are Triadic's decision. No Triadic grade changes.
- **F14** is kept. The new G₂=0 route is a new proof, not a recovery of the missing sources. G2-CHRONO and P4-PRIMITIVE stay [custody-A], and no independent ΔQ_d^(4) certificate exists.
- **F13**: two of the RID-less GEN theorems now have RIDs; the rest are unchanged.
- **GEN.D7**: birth symmetry has a RID.
- **GEN.D6, GEN.D17, F1, OFN.O14, DYAD.X1, PROG.G5, PROG.G6, AZ.A2, PREL.P1**: pointers only.
- **RECOG.R-L2**: the RECOG route is a second route, noted only.
- **LEGACY.Y6**: retyped D-SCOPE; carries the owner readings.
- **NUMGEN.N-I1**: census updated.

**Retained unchanged (2): GEN.D3, F11.**

**H→L5:** no dangling keys; no high L5 row without an H; 114 L5 rows. H5 still cites RECOG.R-L2 only.

## 4. Checks

| Check | Result |
|---|---|
| Shared checker (`atlas_check_report.md`) | sources 72 PASS · coverage 132 PASS · qualifiers 3 PASS · links 499 PASS / 5 UNVERIFIED / 11 DOCUMENTED-UNRESOLVED · artifacts 110 PASS / 3 UNVERIFIED · keys 142 PASS · wording 12 WARN · **0 FAIL** |
| v0.9 for comparison | links 495/5/11 · artifacts 109/3 · keys 128 · wording 13 WARN |
| Shared self-test controls | 18/18 as expected |
| Focused negative controls V1–V19 (`negative_controls.json`) | 19/19 detected |
| Stale-edition guard | 0 hits outside `*ATLAS:checked-*` lines (dated evidence records, left as recorded) |
| Scope guards | 14 statement-level checks hold (one home line for the birth-symmetry RID among them) |
| New RIDs | All four present in the tagged sources (three scientific RIDs with atlas nodes, one artifact RID cited in a `cert` field). RID set difference: GEN v2.9→v2.10 adds exactly the two GEN RIDs and RECOG v0.3.26→v0.3.27 adds exactly the two RECOG RIDs; none removed. |
| Retired keys | None of the 8 appears in the text |
| Pipes (`tools/pipes_index.py --check`) | 87 items, 20 inboxes. Snapshot: 38 closed / 1 dispositioned / 48 open. Branch: 38 / 4 / 45 (the three ATLAS items dispositioned). |
| Reproducibility | Two builds byte-identical |

The focused controls cover:
- a retired key cited from an H line;
- reuse of a retired key;
- a stale SOURCES row (all three sources);
- misspelled new RIDs (link FAIL);
- the P4 identity without its cubic term;
- the route shown as a recovery;
- the jet lemma shown as a Dyadic registration;
- the 0.36915 constant restored;
- a consumer repin implied by the producer answer;
- Triadic Φ₂→₃ notation read as a certified theorem;
- NUMGEN→OFN typed as an import;
- the unsafe K_ε display;
- birth symmetry back as an unnumbered THM;
- a second full node for the birth-symmetry RID (Method §4(4));
- D_birth read as a complete next-block increment;
- Y6 typed D-STALE again;
- Y6 without the full-birth-law restriction.

The 12 wording WARNs are the v0.9 set less the old TDR-G gate WARN, which is gone.

## 5. Evidence limits

- **Structural checks only.** No owner certificate was rerun for this edition, with two exceptions:
  - the RECOG jet-remainder certificate, rerun byte-identical on 4 Nov 2026;
  - the A1c chain rerun of the RA1 advisory (`evidence/recog/atlas_review/ra1/`).

  The new RIDs were checked for presence in the tagged sources, not re-proved.
- **The P4 identity** was checked by hand in `records/gen/ATLAS_ADVISORY_GEN_INBOX_20261103.md` §6 and in `records/gen/ATLAS_ROW_CHECK_GEN_v2_10.md`.
- **The other 15 domains** were not re-extracted.
- **Pipe items** are cited as filed. Receiver dispositions are not atlas sources.

## 6. Pipe states (this branch)

The three items in `pipes/ATLAS/` are set to `dispositioned · accept · this packet`:
- `20261103-TRIAD-atlas-readings-y6-f18.md`;
- `20261104-PROG-v1-4-adopted.md`;
- `20261104-RECOG-v0-3-27-adopted.md`.

The atlas owner closes them after the `atlas-v0.10` tag, in the post-release step.

## 7. Requested

1. A change-focused review of this candidate (ChatGPT), in particular:
   - the F30/F14 wording;
   - the jet-remainder node scope;
   - the IF register typing;
   - the Y6 owner reading.
2. Then the PI's adoption decision. After adoption, the atlas owner:
   - writes the release record (the atlas carries no status line, so the adopted file is this candidate byte for byte);
   - gives one CLI block for merge and tag.

## 8. Revision 2 (after the ChatGPT receiving review)

The review (PR #186, `records/atlas/ATLAS_V0_10_CHATGPT_RECEIVING_REVIEW_20261104.md`; PR #185 comment 6634539731) is a CONDITIONAL PASS. It replayed all 83 edits independently and recomputed the hashes. It asked for two corrections and noted two metadata items. All four are applied in one assertion-gated pass. Three atlas lines change: D4a L1051, D4b L1204 and LEGACY.Y6 L1537. The edit count stays 83, and no source, pipe state or other line changes.

| Item | Change | Gate |
|---|---|---|
| R1a — one home per owner claim | D4a L1051 is the one node `GEN-ALG-BIRTH-SYMMETRY-SEED ALG`. It carries GEN §6.6's caution that D_birth^[s³]=7/512Q_s³=2Q(V_s) is the selected seeded-vector radial channel, distinct from Q(V_s)=7/1024Q_s³ and not by itself a demonstrated complete next-block increment, and the FAIL branch `GEN-FAIL-OLD-BIRTH-SIGN-PHASEDRIFT`. D4b L1204 becomes a typed cross-reference (`→ … (cross-domain reference, not a node; the one node is in D4a) \| <GEN-ALG-BIRTH-SYMMETRY-SEED (D4a)`). The chronology wording ("v2.10; was [THM]") is replaced by the current-state record "the former §6.6 [THM] grade is a corrected claim (GEN App. B), values unchanged". | scope guard: exactly one line starts with the RID; controls V16, V17 |
| R1b — Y6 at scope | `LEGACY.Y6 D-STALE` → `LEGACY.Y6 D-SCOPE`. The line now says the certified part is the leading one: Genesis's `[THM]` c₀^[3]=κQ_sJ_Qs_* under the name Φ₂→₃. The fifth-order remainder holds only if the complete child functional preserves and inherits it (GCL-06, OPEN); Triadic §6.1 is `[DEF]` family notation. The Legacy phrase overstates only if read as a certified complete birth or event law. | scope guard; controls V11 (reworded), V18, V19 |
| Metadata: repin count | `verification_summary.json` reported 18 GEN repin records because the reproducibility rebuild appended a second copy. `refresh()` now clears the list, so file and summary both give 9. | — |
| Metadata: RID types | `new_node_rids` now lists the three scientific RIDs only. The artifact `RECOG-ART-A1C-JET-REMAINDER-BOUNDS` is under `new_artifact_rids`; the full set is under `new_rids_at_tag`. | — |

A delta-only re-review of these three lines and the metadata is requested.
