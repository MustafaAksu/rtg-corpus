# Genesis Geometry v2.9 — Release Record (DRAFT)

**Status:** DRAFT. **Not adopted.**
- Stage 1 is frozen and accepted for stage 2 by both reviewers.
- Stage 2 (layout-only compaction) is built and awaits the atlas owner's review.
- The adopted Genesis edition remains v2.8.9 (`gen-v2.8.9`, `d143673e…c6fc`).

**Owner session:** Genesis co-owner (Claude), 24–25 October 2026.

**Location note.** The file name follows CONVENTIONS §4.5 (`records/<study>/<STUDY>_v<version>_RELEASE_RECORD.md`). The entry note named `RTG_GENESIS_GEOMETRY_v<version>_RELEASE_RECORD.md`; CONVENTIONS governs.

## 1. Authorization and reviews

| Item | Source |
|---|---|
| Q1, edition: v2.9 in two stages; v2.8.10 as fallback | PI, 24 Oct 2026, 23:38; reconciliation §5 (PR #37, commit `b0e974e`) |
| Stage-1 scope (the 21 reconciled dispositions) and F-1 (κ → κ_f) | PI, 24 Oct 2026, 23:45, verbatim: "her ikisini de onaylıyorum" |
| Dispositions | `records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_claude-genowner_20261024.md` (PR #39, incl. §9); `records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_chatgpt_20261024.md` (PR #41); reconciliation §3 |
| Edit plan | `records/gen/GEN_STAGE1_IMPLEMENTATION_MATRIX.md` (E01–E28; F-1 conditions F1-a–F1-e) |
| Stage-1 review, round 1 (`21480757…2087`) | Atlas row check `records/gen/ATLAS_ROW_CHECK_GEN_v2_9_STAGE1.md` (PR #47): build, checker and controls rerun; 21 rows and F-1 verified at owner tags; ACCEPT for stage 2 with B1–B3 fixed in stage 1 and B4 recorded. The ChatGPT co-owner concurs (row check §6; PR #44 review `5640003252`). |
| Instruction for round 2 and stage 2 | PI, 25 Oct 2026, 00:18. Apply B1–B3 as one stage-1 correction package; rerun; record the hash; list B4; then stage 2 (layout-only, `tools/check_compaction.py`, movement map, negative fixtures), preserving §6.3a–c, the GA-01/02 text and the nine custody states. No new scientific review round for stage 1; the atlas owner re-reads the B1–B3 diff only. |

## 2. Stage 1 — identities (round 2, frozen)

| Object | SHA-256 |
|---|---|
| Base: adopted v2.8.9 (`gen-v2.8.9`) | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` |
| Round-1 intermediate (reviewed in PR #47; superseded by round 2) | `21480757eb5b47035efa973e847263d4a50728f8fb13410e323685d37d162087` |
| **Stage-1 intermediate, round 2 (frozen)**; copy at `evidence/gen/v2.9/stage1_intermediate.md` (1,697 lines; a build stage, not an edition) | **`ca431ce90669cfb8bebdf104b52833d05c1147a36ab696fbb4a6160874867845`** |
| `evidence/gen/scripts/build_gen_v2_9_stage1.py` | `53e5f7e684c0b646216c1f96ae43e6be47edf5723f42fa3a8aa25a3b5faf99d2` |
| `evidence/gen/scripts/check_gen_v2_9_stage1.py` | `cdbed5f2710009439f123aea288badbeab93e0bc4067096a05f3315811be91f9` |
| `evidence/gen/v2.9/stage1_edit_log.json` (65 logged edits) | `6eb77f7834779a4b1b0ad219825af029163908c7ae017bd4e75199e292877b5b` |
| `evidence/gen/v2.9/stage1_check_output.txt` (16/16 PASS) | `0531c1ba53faca2b118667cdbd997fc2b43366797683113a029d9b84cff84430` |
| `evidence/gen/v2.9/stage1_negative_controls_output.txt` (11/11 caught) | `948fa86fcae2615219c2cd1c963a37f93113e3aeafb1d3d7a6e9f6caabe3bccf` |
| `evidence/gen/v2.9/dsn_lint_stage1.txt` (informational) | `67605a17b3ddac1da09c7d7f7db8a4936637cf7d3caa15f89b6be837f55c4fc7` |
| `evidence/gen/scripts/gen_owner_advisory_checks.py` (cited as `[indep-AC]`; 8/8 PASS, rerun 24 Oct) | `0ba256be3999606e936a0b14f92311600fd5bd3ff041dd3a828d7688dab6bf99` |

**Commands** (from the repository root; Python 3.13, sympy 1.14.0). The DSN file on the branch is now the stage-2 candidate, so the stage-1 commands use the archived intermediate:

```
git show gen-v2.8.9:dsn/RTG_GENESIS_GEOMETRY_DSN.md > base_v2_8_9.md
python -I evidence/gen/scripts/build_gen_v2_9_stage1.py base_v2_8_9.md s1.md s1_log.json      # s1.md == evidence/gen/v2.9/stage1_intermediate.md
python -I evidence/gen/scripts/check_gen_v2_9_stage1.py base_v2_8_9.md evidence/gen/v2.9/stage1_intermediate.md evidence/gen/v2.9/stage1_edit_log.json --root .
python -I evidence/gen/scripts/check_gen_v2_9_stage1.py base_v2_8_9.md evidence/gen/v2.9/stage1_intermediate.md evidence/gen/v2.9/stage1_edit_log.json --root . --controls
```

## 3. Stage 1 — edits by disposition row

Every edit is applied exactly once, at a unique anchor, and is logged with its old and new text and their hashes.

| Row | Edit keys | Change |
|---|---|---|
| F-1 | KF-81 … KF-1083 (17 lines) | Face-lift `\kappa` → `\kappa_f` at the listed lines only. Triadic-birth κ, κ_phys, κ_RTG and history are untouched (gate C6). |
| GA-01 | E01–E04 | Sourced-junction theorem: Δ₃>0 added. At w=0, K±=τI, and there are exactly two antipodal solutions. The minimizer clause is withdrawn and the physical branch is OPEN (GCL-02). The scope is carried to the §7 export and to OPEN M-foam. |
| GA-02, GA-03, GC-20 | E05, E06a–c, E07a–b, E08 | §6.8 defines κ_f=\|m\|\|w\|, N̂ and ΔM_f=sgn(m)κ_f N̂, and states that B_* is undefined with unknown sign. 9A: λ±=(τ−g)∓sgn(m)κ_f, Π±=½(I±N̂), with an explicit pole–projector map and the soft-branch limiting path OPEN. The residues are independent of sgn m. The notation guard covers γ, κ_f and birth κ. |
| GA-04 | E11, E12a–b | Projection nontriviality is `[ALG]` under the scalar-M ansatz, with "generically" defined; beyond scalar-M it is `[OPEN]`. |
| GA-05 | E13 | Qualifier for the raw-array premise. |
| GB-10 | E14a–e | `GEN-THM-QH-NOGO`, `GEN-THM-SINGLE-FACE-METRIC`, `GEN-THM-SOURCED-JUNCTION`, each attached at its §6 statement, with §1 pointers and §8 rows. |
| GB-11 | E15-× (9), E15-STD | Custody state of the nine artifacts by key `[custody-A]`. The independent-contribution clause is `[indep-AC]`. Both are defined once at the head of §8 (B2). |
| GB-12 | E16 | c_θ⁽⁶⁾ is archival reference only; pointer to the Dyadic chart value +89√3/324. |
| GC-17 | E17a, E17b | G-20 existence note, the only change in §6.3c (C4). §7 import block for two Dyadic v6.4.22 RIDs, with a frame note. |
| GA-06 | E18 | One record per `GEN-OPEN-WPHASE`. |
| GA-07 | E19a–c | OPEN 1T moves to "Recently closed". The completed OPEN 2 item moves to "Closed sub-item". |
| GA-08 | E20 | Scoped non-identity between the 6-member set and the 13 moments. |
| GA-09 | E22a–b | Sign-split wording, in §1 and §6.5. |
| GB-13 | E23 | Inserted because gate GB13 passed (exact): Q_sQ_c−I_sc² = ¾ω_sc², with ω_sc in the RTG canonical B-metric convention (B3). Standalone ⅓Q_c²+¾Q_sQ_c; K4 shadow 5/12. Independently re-verified (C13). |
| GB-14 | E24 | √21/64 is the shear-policy / vector-seed case; the four-case maximum is √14/16 (Triadic §6.17 at `triad-v1.6.1`). |
| GB-16 | E25 | Tier wording "Tier 3 — integrating study". |
| GC-18, GC-19 | E21a, E21b | Companion references at Programme v1.3 and OFN v0.10. §7 Consumers and Pins blocks; consumer pins are not repinned. |
| GC-21 | APPA | The Appendix A entry cites the OFN Q6 erratum as a `[SESSION]` record accepted by the owner on 19 Oct 2026; it is not an adopted theorem. |
| **B1** (round 2) | E02, E05, E06c, E14e, E17a–b, E18, E20, E21b, E23; APPB | No dated "v2.9" marker in the live text (gate C15). The withdrawn clause "has a valid minimizer" is recorded in Appendix B ("Corrected claims", `[RETRACTED | RID: GEN-THM-SOURCED-JUNCTION]`, pointing to GCL-02 and the v2.9 Appendix A entry), not in the theorem block. |
| **B2** (round 2) | E15-STD, E15-× | `[custody-A]` and `[indep-AC]` are defined once and cited by key. The nine custody rows carry `[custody-A]` (gate C15). |
| **B3** (round 2) | E23 | ω_sc convention cited at the GB-13 line: `[conv: RTG canonical B-metric]`, I_sc²+¾ω_sc²=Q_sQ_c, as read at `triad-v1.6.1` (checked in C14). That convention text sits in Triadic **§7.1** (cross-convention note for T-6m, the §6.12 audit), line 791, not in §6.12 itself; the citation names §7.1. |
| **E29** (round 2; B4 prerequisite) | E29 | Header field label `**Status summary.**` → `**Status summary:**`, punctuation only. Without it `tools/check_compaction.py` cannot read the base status summary, and the stage-2 header replacement (B4) cannot be checked. **This is the one edit beyond B1–B3, for the atlas owner's B1–B3 re-read.** |

## 4. Stage 1 — checks (round 2)

- **Checker gates C0–C15: 16/16 PASS.**
  - Base hash, rebuild, reverse to base.
  - Appendix A/B region; protected §6.3a–c and §8 rows.
  - RID set and placement, κ census, tag census.
  - Sign-explicit 9A; GA-01 wording; header and footer.
  - Headings; evidence paths and hash; GB-13; source facts at tags.
  - **C15 (new):** no live "v2.9"; standard clauses defined once and cited; withdrawn clause only in Appendix B.
- **Negative controls NC1–NC11: 11/11 caught.** NC10 (dated marker) and NC11 (inlined custody clause) are new.
- **Round-1 note.** NC6 was first missed because C5 did not check where a RID is attached; C5 was strengthened before the recorded round-1 run.

## 5. Stage 2 — layout-only compaction

| Object | SHA-256 |
|---|---|
| Base: frozen stage-1 intermediate (round 2) | `ca431ce90669cfb8bebdf104b52833d05c1147a36ab696fbb4a6160874867845` |
| **Stage-2 candidate** `dsn/RTG_GENESIS_GEOMETRY_DSN.md` (1,387 lines) | **`3d1c0ba54b25fc3cf5c7539d612c52e8426f7a1c6f2b1dc70acfb3df0632389e`** |
| `evidence/gen/scripts/build_gen_v2_9_stage2.py` | `94bae3c96dc9a6b3b0dcf3a28ebfe75d18a7495fd16b1d8020531163b3145920` |
| `evidence/gen/scripts/check_gen_v2_9_stage2.py` (owner guards and negative fixtures) | `a8e572d51b9f63217d4cc445def1146e661cf5e7d79482c6e3e428d6ddf7c3af` |
| `evidence/gen/v2.9/movement_map.json` (3 operations) | `a759a3bc254492e0f5bc30bde923d20fd0950fe15dab8b7f1d0d45a270da1c3a` |
| `evidence/gen/v2.9/check_compaction_output.txt` (RESULT: PASS) | `73e89431021b43e45652c7d50bb4309a169c53bfd0ea267f83d2b698e5581a3d` |
| `evidence/gen/v2.9/check_compaction_report.json` | `2d74aea38892514dff0cfeba1f35094058f62c6a4ad4613dbe5e90793ee13150` |
| `evidence/gen/v2.9/stage2_guards_output.txt` (7/7 PASS) | `28eb12b431124dbaec4b553b2d85bb6b762e32c3e2f146aa6557c0775fa0aa9c` |
| `evidence/gen/v2.9/stage2_negative_fixtures_output.txt` (9/9 caught) | `5d60ac0e28e370add74e777350e607569e476951f01ab3184629d5995bd78a2f` |
| `evidence/gen/v2.9/dsn_lint_stage2.txt` (informational; −23.0 % bytes against stage 1) | `785faf1a7c192e973aa6f4eb43a8e852e80ff17a48e03f27eced6e0537b0792f` |

**Commands:**

```
python -I evidence/gen/scripts/build_gen_v2_9_stage2.py evidence/gen/v2.9/stage1_intermediate.md dsn/RTG_GENESIS_GEOMETRY_DSN.md evidence/gen/v2.9/movement_map.json
python -I tools/check_compaction.py evidence/gen/v2.9/stage1_intermediate.md dsn/RTG_GENESIS_GEOMETRY_DSN.md evidence/gen/v2.9/movement_map.json --report evidence/gen/v2.9/check_compaction_report.json
python -I evidence/gen/scripts/check_gen_v2_9_stage2.py evidence/gen/v2.9/stage1_intermediate.md dsn/RTG_GENESIS_GEOMETRY_DSN.md evidence/gen/v2.9/movement_map.json [--fixtures]
```

**Operations.** The archive for all three is the stage-1 intermediate. `gen-v2.8.9` is a known tag but is not named as an archive, for the reason given in the map's `archives_note`.

- **S2-H `replace-header` (B4).** The header becomes current-only:
  - title v2.9; date; Document status "STAGE-2 CANDIDATE — not adopted";
  - Document class, with the §1 profile exception (§1 ≈ 1,000 words of statement-level readouts with their qualifications);
  - Supersedes: v2.8.9 only, with full hash and tag;
  - Companion documents point to §7; DSN Methodology v1.4 (tag `methodology-v1.4`);
  - tier line as in stage 1;
  - Status summary built only from sentences of the base summary and base §1 (profile `summary_from` = header + section1).
- **S2-A `replace-section`, class history-appendix.** Appendix A becomes one compact entry per edition: v2.9; v2.8.9–v2.8.5 with their release records on `upload/gen-records/`; earlier editions pointed to Appendix A of `gen-v2.8.9`. Removed: 47,529 characters, all in the archive.
- **S2-F `replace-footer`.** One footer line; the inherited footer chain is in the archive.

**`tools/check_compaction.py`: RESULT PASS.**
- Identities and re-derivation.
- Each operation's class rules.
- Claim blocks: 360 in the base live text; 359 byte-identical; 1 changed by a declared operation, namely the inherited footer chain removed by S2-F.
- RID set, heading anchors, source hashes and qualifier tags preserved.
- References resolve; presentation passes (fields present, one predecessor, one footer).

**Owner guards G1–G7: 7/7 PASS.**
- The live body from "## Local Tag Aliases" to Appendix A is byte-identical to stage 1. This covers §1–§9, so no live text changed in stage 2.
- §6.3a–c byte-identical.
- GA-01: both statements, the §7 export and the Appendix B entry.
- GA-02/F-1: the κ_f definition, the 9A block and OPEN-GEN-II-9 items 1–3.
- Nine custody rows plus the two standard clauses.
- Appendix B byte-identical.
- The tool PASS.

**Negative fixtures F1–F9: 9/9 caught.**
- F1 undeclared edit inside §6.3c (mechanical scope).
- F2 a history entry naming a RID absent from the live text.
- F3 a status-summary sentence not in base summary or §1.
- F4 archive hash mismatch.
- F5 §6.3c relocated as a history section.
- F6 two predecessors in Supersedes.
- F7 two footer lines.
- F8 a block moved across sections.
- F9 a GA-01 wording change declared as `ref-subst` (guards G1 and G3).

A compaction PASS shows mechanical preservation only, not scientific equivalence (Methodology v1.4 §12.4). The scientific content was reviewed in stage 1.

## 6. B4 — header scope, and what remains for publication

**B4 is done in stage 2 as the declared `replace-header` operation S2-H, which the compaction checker sees.** Old → new:

| Field | Stage 1 (old) | Stage-2 candidate (new) |
|---|---|---|
| Title line | `RTG_GENESIS_GEOMETRY_DSN_v2.8.9` | `RTG_GENESIS_GEOMETRY_DSN_v2.9` |
| Date | 19 October 2026 | 25 October 2026 |
| Document status | ADOPTED owner ledger — scientific release (D-4 …) | STAGE-2 CANDIDATE — not adopted (…); release record named |
| Document class | (absent) | Technical scientific ledger; §1 profile exception |
| Supersedes | 30 editions, no hash | v2.8.9 only, full hash, tag `gen-v2.8.9` |
| Companion documents | Programme v1.2 · OFN v0.9 · Methodology v1.3 · Dyadic v6.4.13 · Triadic v1.6 · Discrete v2.12.13 | pointer to §7 (Pins; Programme-context references: Programme v1.3, OFN v0.10; Dyadic v6.4.13/v6.4.22; Triadic v1.6/v1.6.1; Discrete v2.12.13) |
| DSN Methodology | DSN_METHODOLOGY_v1.3 | v1.4 (tag `methodology-v1.4`) |
| Status summary | stacked v2.8.5–v2.8.9 summary | current state, from base summary and §1 sentences only |
| Release record | (absent) | `records/gen/GEN_v2_9_RELEASE_RECORD.md` |

**Left to the publication transform** (status lines only, after the PI decision; as for RECOG and Dyadic):
- the Document status line: "STAGE-2 CANDIDATE — not adopted …" → "ADOPTED — PI, <date> …";
- the Date line;
- the Appendix A v2.9 entry heading: "stage-2 candidate (not adopted)" → "Adopted";
- the footer line: "(stage-2 candidate; not adopted)" → "(ADOPTED, <date>)".

## 7. Not done (deliberately)

- **§1 size.** About 1,000 words against 200–400. It is kept under the declared §1 profile exception, because the compaction checker cannot shorten claim prose and a pointer-only list would drop the hypotheses. The §1 sourced-junction statement beside its §6.9 home stays for the same reason.
- **§7 headings.** No grouping headings are added; the checker has no insert operation. The stage-1 order already runs Imports (producer blocks and companion references) → Export protocol → Consumers → Pins.
- **Live history pointers carrying RIDs or tags** (e.g. "(v2.8.6 repin …)"). Not removable by a history-removal edit, which rejects RIDs, and not touched.
- **Further RIDs.** Pure chiral protection and tetrahedral chronological protection come second under GB-10; "tetrahedral quartic drift" waits for owner confirmation of its relation to P4-PRIMITIVE.
- **Scope.** No rerun of the K₃ certificates or the Dyadic campaigns. No change to `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`. No physical selection of κ, γ or branch.

## 8. Reviews

- Stage 1: done (§1).
- Next, atlas owner:
  - re-read of the round-2 diff: B1–B3 and E29;
  - review of stage 2: movement map, tool report, guards, fixtures.
- Results go to `records/gen/`.

## 9. What would be notified (no notices sent; PI decision)

- **UVM / OPEN M (IF08, pin v2.8.5).**
  - κ_f = |m||w| is the same quantity as UVM's |mw|.
  - B_* is recorded as undefined with unknown sign; UVM R2 cites m = 2Q_sB_*.
  - The sourced-junction minimizer clause is withdrawn (Appendix B); physical branch selection is OPEN.
- **RRF (IF30, pin v2.8.9).** The §7 export names three new RIDs. The sourced-junction export is rescoped. §6.3c exports are unchanged.
- **OFN (IF32).** §6.3a–§6.3c are unchanged apart from the G-20 note: (C2) is non-vacuous at C^∞ via Dyadic v6.4.22, and the analytic case stays OPEN.
- **Dyadic.** Informational: two v6.4.22 RIDs are imported for the §6.3c note. The v6.4.13 pins are unchanged.
- **Triadic.** Informational: §6.17 four-case maximum, and the §7.1 ω_sc convention, cited at v1.6.1 as companion readings.

## 10. Adoption

Not adopted. Order (CONVENTIONS §4): atlas review of round 2 and stage 2 → release record final → PI decision → publication commit (status lines, §6) → merge commit and tag `gen-v2.9` by the PI.
