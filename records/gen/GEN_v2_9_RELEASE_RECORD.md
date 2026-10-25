# Genesis Geometry v2.9 — Release Record

**Status:** **ADOPTED — PI, 25 October 2026** ("çalışmayı bu haliyle benimsiyorum").
- Adopted payload: stage-2 candidate `89cef1713292e889f8c6923e7d391e36668c7909d66e2504fe553037a967561a` (PR #44 at `4438250`).
- Published file after the status-only publication transform (§10): **`9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac`**.
- Reviews of round 3 are complete (§8): ChatGPT co-owner ACCEPT; atlas owner ACCEPT FOR ADOPTION.
- Merge commit and the annotated tag `gen-v2.9` are the PI's (§10). Until the tag exists, `gen-v2.8.9` (`d143673e…c6fc`) is the latest tagged edition.

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
| Stage-2 review (round 2 + stage 2 at `5acc2c9`) | Atlas row check `records/gen/ATLAS_ROW_CHECK_GEN_v2_9_STAGE2.md` (PR #50): reruns identical; ACCEPT with V1 (methodology sentence / bounded migration) and V2 (records home); §6 addendum G29-FINAL-01 (existence scope at G-20, §6.3c OPEN list, §5), bundled as stage-1 round 3. ChatGPT co-owner follow-up review on PR #44 (`5640109252`). |
| PI decision V2 | PI, 25 Oct 2026, 01:13: the permanent home of the recovered Genesis records is `upload/gen-records/`; no move to `records/gen/`; names, bytes and SHA-256 kept; the `upload/gen-records/…` citations in Appendix A stay; the PR #43 placement plan is updated accordingly; `BASELINE.md` may carry a pointer; `records/gen/` remains the home of current review, disposition and release records. |
| Instruction for round 3 | PI and ChatGPT co-owner, 25 Oct 2026, 01:13: V1 and G29-FINAL-01 in one stage-1 round 3 — E30 records the limits of the Methodology v1.4 migration honestly; E31 separates mathematical \(C^\infty\) existence, analytic existence and physical network realization; the theorem's proof and hypotheses are kept; then a deterministic stage-2 rerun and all new hashes here. |
| Instruction for round 2 and stage 2 | PI, 25 Oct 2026, 00:18. Apply B1–B3 as one stage-1 correction package; rerun; record the hash; list B4; then stage 2 (layout-only, `tools/check_compaction.py`, movement map, negative fixtures), preserving §6.3a–c, the GA-01/02 text and the nine custody states. No new scientific review round for stage 1; the atlas owner re-reads the B1–B3 diff only. |

## 2. Stage 1 — identities (round 3, frozen)

| Object | SHA-256 |
|---|---|
| Base: adopted v2.8.9 (`gen-v2.8.9`) | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` |
| Round-1 intermediate (reviewed in PR #47; superseded by round 2) | `21480757eb5b47035efa973e847263d4a50728f8fb13410e323685d37d162087` |
| Round-2 intermediate (reviewed in PR #50; superseded by round 3) | `ca431ce90669cfb8bebdf104b52833d05c1147a36ab696fbb4a6160874867845` |
| **Stage-1 intermediate, round 3 (frozen)** at `evidence/gen/v2.9/stage1_intermediate.md` (1,697 lines; a build stage, not an edition) | **`5677d706d5ccca0e3b822f484e1de7641e771e8ec3e83c51b50daf336833cd98`** |
| `evidence/gen/scripts/build_gen_v2_9_stage1.py` | `1172585b090d718a634a0180102da053e5b63ea64b40c7a878fb12d2ceea88cd` |
| `evidence/gen/scripts/check_gen_v2_9_stage1.py` | `25af1cf04ac3a74c52437c388d0fd5a250aa28ce954d8edd5a24bb1df3b91fd3` |
| `evidence/gen/v2.9/stage1_edit_log.json` (69 logged edits; includes the bounded-migration census) | `73fff7b511fc357db6aecff27ba602942599d1cb916c4e64a656d27ee144e4e8` |
| `evidence/gen/v2.9/stage1_check_output.txt` (17/17 PASS) | `c35fb2d3f1aeef46f85dbc9253d63d53ddd12a1c4c547900a54a20ed0d917645` |
| `evidence/gen/v2.9/stage1_negative_controls_output.txt` (13/13 caught) | `f7d39c91c0bc2d780002fb3633cc77e57928768735da74f1ea8657fd1407b47f` |
| `evidence/gen/v2.9/dsn_lint_stage1.txt` (informational) | `ad311b526f25c0990071e17f6a87c65a28d67952e9b9e840e00409ac1c0b1dcc` |
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
| **E30** (round 3; V1) | E30 | The Local Tag Aliases methodology sentence is restated for v1.4. The live-file rule, header and Appendix A follow v1.4; blocks written or edited from v2.8.5 use the canonical tags; inherited blocks keep their mixed-tag form; inherited `[RESULT]` occurrences without a `[from: TAG]` companion stay under a **bounded migration**. Census in the edit log: **29 of 32** `[RESULT]` occurrences in the live text are unpaired, 3 paired. This counts occurrences on a line, prose mentions included, and excludes the methodology sentence itself; the atlas count of 30 of 33 used a slightly different span. The 29 lines are listed under `bounded_migration_result_census` in `stage1_edit_log.json` and are recorded, not asserted zero (gate C16). Pairing them is retagging work for a later edition. |
| **E31a–c** (round 3; G29-FINAL-01) | E31a, E31b, E31c | Existence scope separated at the three sites the atlas verified. G-20 (§6.3c): "(C2) would be vacuous without such a Φ"; a real C^∞ Φ is imported (next item); analytic existence is open (Dyadic OPEN 20, B-an/B-6); no physical or network-level realization is asserted. The §6.3c OPEN list and the §5 high-risk row now read "existence of an analytic exactly transported realization … any physical or network-level realization (the C^∞ mathematical existence is imported, G-20 note)". The theorem statement, hypotheses and proof are byte-checked unchanged: gate C4 allows exactly E31a/E31b inside §6.3c. The §7 export sentence ("Genesis does not select … the existence of an exactly transported realization") states what Genesis does not select; it is not an existence claim and was left unchanged. |
| **E29** (round 2; B4 prerequisite) | E29 | Header field label `**Status summary.**` → `**Status summary:**`, punctuation only. Without it `tools/check_compaction.py` cannot read the base status summary, and the stage-2 header replacement (B4) cannot be checked. **This is the one edit beyond B1–B3, for the atlas owner's B1–B3 re-read.** |

## 4. Stage 1 — checks (round 3)

- **Checker gates C0–C16: 17/17 PASS.**
  - Base hash, rebuild, reverse to base.
  - Appendix A/B region; protected §6.3a–c and §8 rows.
  - RID set and placement, κ census, tag census.
  - Sign-explicit 9A; GA-01 wording; header and footer.
  - Headings; evidence paths and hash; GB-13; source facts at tags.
  - **C15:** no live "v2.9"; standard clauses defined once and cited; withdrawn clause only in Appendix B. Round 3 adds: no "vacuous if no such" wording; the old unqualified existence items are gone; the methodology sentence names `methodology-v1.4` and the bounded migration.
  - **C4, widened in round 3:** exactly E31a/E31b inside §6.3c.
  - **C16 (new):** the bounded-migration census is recomputed and equals the log.
- **Negative controls NC1–NC13: 13/13 caught.**
  - NC10 (dated marker) and NC11 (inlined custody clause) were added in round 2.
  - NC12 (old G-20 "vacuous if no such Φ exists" reintroduced; must fail C4 and C15) and NC13 (methodology sentence reverted to v1.3) are new in round 3.
- **Round-1 note.** NC6 was first missed because C5 did not check where a RID is attached; C5 was strengthened before the recorded round-1 run.

## 5. Stage 2 — layout-only compaction

| Object | SHA-256 |
|---|---|
| Base: frozen stage-1 intermediate (round 3) | `5677d706d5ccca0e3b822f484e1de7641e771e8ec3e83c51b50daf336833cd98` |
| Previous stage-2 candidate (reviewed in PR #50; superseded) | `3d1c0ba54b25fc3cf5c7539d612c52e8426f7a1c6f2b1dc70acfb3df0632389e` |
| **Stage-2 candidate** `dsn/RTG_GENESIS_GEOMETRY_DSN.md` (1,388 lines) | **`89cef1713292e889f8c6923e7d391e36668c7909d66e2504fe553037a967561a`** |
| `evidence/gen/scripts/build_gen_v2_9_stage2.py` | `c7fb50f13bd5a2003e5c28d37249598ffd37adf9f6bbbf199c7c63e8ec95ebfe` |
| `evidence/gen/scripts/check_gen_v2_9_stage2.py` (owner guards and negative fixtures) | `a8e572d51b9f63217d4cc445def1146e661cf5e7d79482c6e3e428d6ddf7c3af` |
| `evidence/gen/v2.9/movement_map.json` (3 operations) | `9e0233486ac4852ab367abadd560e2b966fcc811ee14a04bd52cd3001d5a1dd9` |
| `evidence/gen/v2.9/check_compaction_output.txt` (RESULT: PASS) | `a521693e4dde450151474f95a7aebd9b84cf90870105421ae9ed9abcae28aebe` |
| `evidence/gen/v2.9/check_compaction_report.json` | `1c3739a9d60fe54b7dc5ccdbbd20357ae73edcb4117435b368aae18937ec594a` |
| `evidence/gen/v2.9/stage2_guards_output.txt` (7/7 PASS) | `8bfaea17c0c3660f9144aa68d1e94895d455387f53cdd173d74de43a5ee5e45d` |
| `evidence/gen/v2.9/stage2_negative_fixtures_output.txt` (9/9 caught) | `5d60ac0e28e370add74e777350e607569e476951f01ab3184629d5995bd78a2f` |
| `evidence/gen/v2.9/dsn_lint_stage2.txt` (informational; −22.9 % bytes against stage 1) | `83529a53518d43cb8298bf027e03ce4c05394f34afc2b6592f8c936b1fb48fc3` |

**Determinism (round 3).** A fresh build of stage 1 from the base, then of stage 2 from that output, reproduces `stage1_intermediate.md`, the candidate and the movement map byte-identically. The negative-fixture output is unchanged from round 2.

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
  - Round 3: the base sentence ending "existence of an exactly transported realization is not asserted" is no longer reused (G29-FINAL-01).
- **S2-A `replace-section`, class history-appendix.** Appendix A becomes one compact entry per edition: v2.9; v2.8.9–v2.8.5 with their release records on `upload/gen-records/`; earlier editions pointed to Appendix A of `gen-v2.8.9`. Removed: 47,529 characters, all in the archive.
- **S2-F `replace-footer`.** One footer line; the inherited footer chain is in the archive.

**`tools/check_compaction.py`: RESULT PASS.**
- Identities and re-derivation.
- Each operation's class rules.
- Claim blocks: 360 in the base live text; 359 byte-identical; 1 changed by a declared operation, namely the inherited footer chain removed by S2-F.
- RID set, heading anchors, source hashes and qualifier tags preserved.
- References resolve; presentation passes (fields present, one predecessor, one footer).

**Owner guards G1–G7: 7/7 PASS** (on the round-3 base).
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

- **Bounded methodology migration (V1).** 29 inherited `[RESULT]` occurrences carry no `[from:]` companion. They are recorded (E30, C16), not repaired; pairing them is retagging work for a later edition. No metadata-only claim of v1.4 compliance is made.
- **Records home (V2, PI decision).** The recovered Genesis records stay at `upload/gen-records/` (names, bytes, SHA-256 unchanged). The Appendix A citations `upload/gen-records/GENESIS_V2_8_x_RELEASE_RECORD.md` are therefore final. The PR #43 placement plan and the `BASELINE.md` pointer are updated in a separate repository-maintenance PR (`claude/gen-records-home`).

- **§1 size.** About 1,000 words against 200–400. It is kept under the declared §1 profile exception, because the compaction checker cannot shorten claim prose and a pointer-only list would drop the hypotheses. The §1 sourced-junction statement beside its §6.9 home stays for the same reason.
- **§7 headings.** No grouping headings are added; the checker has no insert operation. The stage-1 order already runs Imports (producer blocks and companion references) → Export protocol → Consumers → Pins.
- **Live history pointers carrying RIDs or tags** (e.g. "(v2.8.6 repin …)"). Not removable by a history-removal edit, which rejects RIDs, and not touched.
- **Further RIDs.** Pure chiral protection and tetrahedral chronological protection come second under GB-10; "tetrahedral quartic drift" waits for owner confirmation of its relation to P4-PRIMITIVE.
- **Scope.** No rerun of the K₃ certificates or the Dyadic campaigns. No change to `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`. No physical selection of κ, γ or branch.

## 8. Reviews

- Stage 1 rounds 1–2 and stage 2: done (§1; PR #47, PR #50, PR #44 reviews).
- Round 3, targeted readback (scope: E30, E31a–c, the C4/C15/C16 gate changes, NC12–NC13 and the stage-2 rerun):
  - **ChatGPT co-owner — done.** PR #44 review `5643144174` at commit `4438250`, 25 Oct 2026.
    - Verdict: **ACCEPT FOR FINAL ATLAS / RELEASE PREPARATION**, not adoption. E30 and E31 accepted.
    - Recorded results confirmed from the repository records: stage 1 17/17 and 13/13; stage 2 compaction PASS, guards 7/7, fixtures 9/9; hashes `5677d706…cd98` and `89cef171…561a`.
    - The scripts were not rerun independently in that review.
    - Limitation stated by the reviewer: the 29 inherited `[RESULT]` occurrences without `[from:]` remain unpaired. This is declared (E30, C16) and does not block release preparation. Full v1.4 grammar compliance is **not** claimed.
  - **Atlas owner — done.** `records/gen/ATLAS_ROW_CHECK_GEN_v2_9_STAGE2.md` §7, 25 Oct 2026, 15:25 (PR #50, merged).
    - Reruns of stage 1 (`5677d706…cd98`, 17/17, controls all caught) and stage 2 (`89cef171…561a`; guards 7/7; fixtures 9/9; compaction PASS) were byte-identical.
    - The round 2 → round 3 diff is exactly E30 + E31 (+ the Appendix A entry sentence). V2 is settled (PR #52).
    - Census note: a plain line count over the whole file gives 30, not 29. The extra occurrence is the Appendix B retraction entry ("downgraded from `[RESULT]` to `[OPEN]`"), which lies outside the live region that C16 counts.
    - Verdict: **ACCEPT FOR ADOPTION.**
- Results go to `records/gen/`.

## 9. What would be notified (no notices sent; PI decision)

- **UVM / OPEN M (IF08, pin v2.8.5).**
  - κ_f = |m||w| is the same quantity as UVM's |mw|.
  - B_* is recorded as undefined with unknown sign; UVM R2 cites m = 2Q_sB_*.
  - The sourced-junction minimizer clause is withdrawn (Appendix B); physical branch selection is OPEN.
- **RRF (IF30, pin v2.8.9).** The §7 export names three new RIDs. The sourced-junction export is rescoped. §6.3c exports are unchanged.
- **OFN (IF32).** The statement, hypotheses and proof in §6.3a–§6.3c are unchanged. The G-20 note and the existence-scope wording are new: (C2) is non-vacuous at C^∞ via Dyadic v6.4.22; analytic existence and any physical or network-level realization stay OPEN.
- **Dyadic.** Informational: two v6.4.22 RIDs are imported for the §6.3c note. The v6.4.13 pins are unchanged.
- **Triadic.** Informational: §6.17 four-case maximum, and the §7.1 ω_sc convention, cited at v1.6.1 as companion readings.

## 10. Adoption and publication

**Decision.** PI, 25 October 2026, verbatim: "çalışmayı bu haliyle benimsiyorum". Adopted object: the stage-2 candidate `89cef1713292e889f8c6923e7d391e36668c7909d66e2504fe553037a967561a` on PR #44 at commit `4438250`.
- Basis: the reviews of §1 and §8, i.e. atlas row checks PR #47 and PR #50 §7 (ACCEPT FOR ADOPTION), and ChatGPT co-owner reviews `5640003252`, `5640109252` and `5643144174`.
- The bounded methodology migration of §7 (29 unpaired `[RESULT]` occurrences) is adopted as declared. Full v1.4 grammar compliance is not claimed.

**Publication transform.** `evidence/gen/scripts/release_gen_v2_9.py`, assertion-gated: it accepts only the `89cef171…561a` input and changes status lines only.
- Changed lines (3):
  - Document status → "ADOPTED — PI, 25 October 2026 (…; stage 1 and stage 2 reviewed). Adoption record: `records/gen/GEN_v2_9_RELEASE_RECORD.md`";
  - Appendix A heading → "### v2.9 — 25 October 2026 — Adopted";
  - footer → "*END OF DOCUMENT — RTG_GENESIS_GEOMETRY_DSN_v2.9 (ADOPTED, 25 October 2026).*".
- The Date line already reads "25 October 2026" in the candidate. The script asserts it and leaves it byte-unchanged.
- Nothing else changes: live body, Appendix B, every other header field and the claim-tag census are byte-identical (gate P6).

| Object | SHA-256 |
|---|---|
| Adopted stage-2 candidate (input) | `89cef1713292e889f8c6923e7d391e36668c7909d66e2504fe553037a967561a` |
| **Published `dsn/RTG_GENESIS_GEOMETRY_DSN.md` (v2.9, 1,388 lines)** | **`9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac`** |
| `evidence/gen/scripts/release_gen_v2_9.py` | `6e1e62187d480573aa4e6330242802eb33e84f36bf643a81ade98bf3ac0e9416` |
| `evidence/gen/v2.9/release_check_output.txt` (P1–P6: 6/6 PASS) | `5287135ebbbccb908124e73e9b59478cc76709c8cbcbaf693f110d7702bbf255` |
| `evidence/gen/v2.9/release_negative_controls_output.txt` (RC1–RC4: 4/4 caught) | `6c4b25a37ff3e7802902d6088e40e1425473f981233b0ed5ec3f9c2dade6347e` |
| Predecessor `gen-v2.8.9` | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` |

**Gates P1–P6, 6/6 PASS:**
- P1 candidate hash;
- P2 output = transform;
- P3 exactly the three declared lines differ, and the Date line equals the decision date;
- P4 the reverse transform recovers the candidate;
- P5 no "candidate"/"not adopted" marker in the header status lines, the v2.9 Appendix A heading or the footer;
- P6 every other line and the claim-tag census are byte-identical.

**Controls RC1–RC4, 4/4 caught:**
- RC1 wrong input refused;
- RC2 tampered footer date;
- RC3 undeclared header edit;
- RC4 Appendix A heading left as candidate.

**Commands:**

```
git show 4438250:dsn/RTG_GENESIS_GEOMETRY_DSN.md > cand.md      # 89cef171…561a
python -I evidence/gen/scripts/release_gen_v2_9.py cand.md dsn/RTG_GENESIS_GEOMETRY_DSN.md "25 October 2026"
python -I evidence/gen/scripts/release_gen_v2_9.py cand.md dsn/RTG_GENESIS_GEOMETRY_DSN.md "25 October 2026" --check
```

**For the PI (publication, CONVENTIONS §4.6):**
1. Merge PR #44 with a **merge commit** (not squash, not rebase).
2. Create the annotated tag `gen-v2.9` **on that merge commit**, with a message naming the published hash, e.g. "Genesis Geometry v2.9 — adopted by the PI 25 October 2026; dsn/RTG_GENESIS_GEOMETRY_DSN.md SHA-256 9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac".
3. `BASELINE.md`, GEN row: v2.9, `9178ca2c…00ac`, OWNER: this release record, tag `gen-v2.9` (predecessor `d143673e…c6fc`, `gen-v2.8.9`). Done after the tag, by the PI or the atlas owner.

**After the tag.** The atlas owner verifies tag → merge commit → file hash, then starts the atlas refresh (row check §4 notes). No notices are sent (PI decision); §9 lists what would be notified.
