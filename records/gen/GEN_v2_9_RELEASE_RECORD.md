# Genesis Geometry v2.9 — Release Record (DRAFT)

**Status:** DRAFT. **Not adopted.** Stage 1 is built; stage 2 is not started. The adopted Genesis edition remains v2.8.9 (`gen-v2.8.9`, `d143673e…c6fc`).

**Owner session:** Genesis co-owner (Claude), 24 October 2026.

**Location note.** The file name follows CONVENTIONS §4.5 (`records/<study>/<STUDY>_v<version>_RELEASE_RECORD.md`). The entry note named `RTG_GENESIS_GEOMETRY_v<version>_RELEASE_RECORD.md`; CONVENTIONS governs.

## 1. Authorization

| Item | Source |
|---|---|
| Q1, edition: v2.9 in two stages; v2.8.10 as fallback | PI, 24 Oct 2026, 23:38, recorded in reconciliation §5 (PR #37, commit `b0e974e`) |
| Stage-1 scope (the 21 reconciled dispositions) and F-1 (κ → κ_f) | PI, 24 Oct 2026, 23:45, verbatim: "her ikisini de onaylıyorum" |
| Dispositions | `records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_claude-genowner_20261024.md` (PR #39, including §9); `records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_chatgpt_20261024.md` (PR #41); reconciliation §3 (PR #37) |
| Edit plan | `records/gen/GEN_STAGE1_IMPLEMENTATION_MATRIX.md` (E01–E28, F-1 conditions F1-a–F1-e) |

## 2. Stage 1 — identities

| Object | SHA-256 |
|---|---|
| Base: adopted v2.8.9 (`gen-v2.8.9`) | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` |
| **Stage-1 intermediate** `dsn/RTG_GENESIS_GEOMETRY_DSN.md` on `claude/gen-stage1-prep` (1,688 lines; a build stage, not an edition) | **`21480757eb5b47035efa973e847263d4a50728f8fb13410e323685d37d162087`** |
| `evidence/gen/scripts/build_gen_v2_9_stage1.py` | `672362794bb75aae701e2c45d04a5b984aba040892dcd9c839da8234113a35ec` |
| `evidence/gen/scripts/check_gen_v2_9_stage1.py` | `cfd94b5ab9d9ee5a6a477975d2df3bee40c86a5634ad925660f34141a6e7a9c3` |
| `evidence/gen/v2.9/stage1_edit_log.json` (62 logged edits) | `af26110acfe5422732881b69b4c536ef92f749ca8b6a45643abbf6dc9479e984` |
| `evidence/gen/v2.9/stage1_check_output.txt` (15/15 PASS) | `39b796d3113b9a45d9f845482807dfd6efa9aff6f3e8f6da062306f4cac8812c` |
| `evidence/gen/v2.9/stage1_negative_controls_output.txt` (9/9 caught) | `4b7c9e80fa70393c4f855266d785817ce7d392ea306ca6c5ed7322ca93df3020` |
| `evidence/gen/v2.9/dsn_lint_stage1.txt` (informational) | `776a76ded781f1197a333ca161559af1240a5e83967185bd8f912fb84ec5153e` |
| `evidence/gen/scripts/gen_owner_advisory_checks.py` (cited evidence; 8/8 PASS, rerun 24 Oct) | `0ba256be3999606e936a0b14f92311600fd5bd3ff041dd3a828d7688dab6bf99` |

**Commands** (from the repository root; Python 3.13, sympy 1.14.0):

```
git show gen-v2.8.9:dsn/RTG_GENESIS_GEOMETRY_DSN.md > base_v2_8_9.md
python -I evidence/gen/scripts/build_gen_v2_9_stage1.py base_v2_8_9.md dsn/RTG_GENESIS_GEOMETRY_DSN.md evidence/gen/v2.9/stage1_edit_log.json
python -I evidence/gen/scripts/check_gen_v2_9_stage1.py base_v2_8_9.md dsn/RTG_GENESIS_GEOMETRY_DSN.md evidence/gen/v2.9/stage1_edit_log.json --root .
python -I evidence/gen/scripts/check_gen_v2_9_stage1.py base_v2_8_9.md dsn/RTG_GENESIS_GEOMETRY_DSN.md evidence/gen/v2.9/stage1_edit_log.json --root . --controls
```

The base file is not stored in `evidence/`; it is reproduced from the tag.

## 3. Stage 1 — edits by disposition row

Every edit is applied exactly once, at a unique anchor, and is recorded in the edit log with its old and new text and their hashes.

| Row | Edit keys | Change |
|---|---|---|
| F-1 | KF-81 … KF-1083 (17 lines) | Face-lift `\kappa` → `\kappa_f` at the listed lines only. Triadic-birth κ, κ_phys, κ_RTG and history are untouched (gate C6). |
| GA-01 | E01, E02, E03, E04 | Sourced-junction theorem: Δ₃ > 0 added. At w = 0, K± = τI, and there are exactly two antipodal solutions. "has a valid minimizer" is withdrawn; the physical branch is OPEN (GCL-02). The scope is carried to the §7 export and to OPEN M-foam. |
| GA-02, GA-03, GC-20 | E05, E06a–c, E07a–b, E08 | §6.8 defines κ_f = \|m\|\|w\|, N̂ and ΔM_f = sgn(m)κ_f N̂, and states that B_* is undefined with unknown sign. 9A: λ± = (τ−g) ∓ sgn(m)κ_f, Π± = ½(I ± N̂), with an explicit pole–projector map and the soft-branch limiting path OPEN. The residues are independent of sgn m. The notation guard covers γ, κ_f and birth κ. |
| GA-04 | E11, E12a–b | Projection nontriviality is `[ALG]` under the scalar-M ansatz, with "generically" defined; beyond scalar-M it is `[OPEN]`. |
| GA-05 | E13 | Qualifier for the raw-array premise. |
| GB-10 | E14a–e | RIDs `GEN-THM-QH-NOGO`, `GEN-THM-SINGLE-FACE-METRIC`, `GEN-THM-SOURCED-JUNCTION`, each attached at its §6 statement, with §1 pointers and §8 rows. No collision in `dsn/` (C5). |
| GB-11 | E15-× (9) | Custody state (a) missing, `EV-NOT-RERUN`, for all nine artifacts. Independent re-derivations are cited as such for FACE-LIFT and SOURCED-JUNCTION. |
| GB-12 | E16 | c_θ⁽⁶⁾ is archival reference only; pointer to the Dyadic chart value +89√3/324. |
| GC-17 | E17a, E17b | G-20 note: the only change in §6.3c (C4). New §7 block importing two Dyadic v6.4.22 RIDs, with a frame note. |
| GA-06 | E18 | One record per `GEN-OPEN-WPHASE`. |
| GA-07 | E19a–c | OPEN 1T moves to "Recently closed". The completed OPEN 2 item moves to "Closed sub-item". |
| GA-08 | E20 | Scoped non-identity between the 6-member set and the 13 moments. |
| GA-09 | E22a, E22b | Sign-split wording, in §1 and §6.5. |
| GB-13 | E23 | Inserted because gate GB13 passed (exact): Q_sQ_c − I_sc² = ¾ω_sc² under the J_Q-invariant B, with off-diagonal −1/2. Standalone ΔQ_c⁽⁴⁾ at I_sc = 0 equals ⅓Q_c² + ¾Q_sQ_c; the K4-shadow form gives 5/12 instead. The identity is re-verified by an independent code path (C13). |
| GB-14 | E24 | √21/64 labelled as shear policy / vector-seed reading. Four-case maximum √14/16 (Triadic §6.17 at `triad-v1.6.1`, checked in C14). |
| GB-16 | E25 | Tier wording: "Tier 3 — integrating study" (Programme v1.3 §6.1). |
| GC-18, GC-19 | E21a, E21b | Companion references refreshed to Programme v1.3 and OFN v0.10. New §7 Consumers and Pins blocks; consumer pins are not repinned. |
| GC-21 | APPA | The new Appendix A entry cites the OFN Q6 erratum as a `[SESSION]` record accepted by the owner on 19 Oct 2026; it is not an adopted theorem. |

## 4. Stage 1 — checks

**Checker gates C0–C14: 15/15 PASS.**
- base hash; rebuild; reverse transform to base;
- appendix region; §6.3a–§6.3c and the protected §8 rows;
- RID set and placement; κ census; tag census;
- sign-explicit 9A; GA-01 wording; header and footer;
- headings; evidence paths and hash; GB-13 identity;
- source facts at `dyad-v6.4.22`, `triad-v1.6.1` and `programme-v1.3`.

**Negative controls NC1–NC9: 9/9 caught.** NC6 first ran against a C5 that did not check where each RID is attached, and was missed; C5 was strengthened before the recorded run.

**`dsn_lint` (informational).**
- 1,688 lines, +6.2 % bytes.
- Six new namespace identifiers: the three GEN RIDs, the two imported DYAD RIDs, and the RECOG cross-reference in the GB-11 G2-CHRONO note, which is not an import.
- §1 has 1,006 words against the 200–400 target. That is stage-2 work.

## 5. Not done in stage 1 (deliberately)

- **Header identity lines, Appendix A heading and footer** (status, date, supersedes, companion list, methodology line). These belong to stage 2 and the publication transform. The companion list in the header still names Programme v1.2 and OFN v0.9 until then.
- **Stage-2 layout work.** Grouping §7 into the four parts Imports / Exports / Consumers / Pins; §1 reduced to the v1.4 size with pointers; moving superseded history; the Methodology v1.4 profile. Inputs: movement map and `tools/check_compaction.py` against the stage-1 hash.
- **Further RIDs not assigned.** Pure chiral protection and tetrahedral chronological protection come second under GB-10. "Tetrahedral quartic drift" waits for owner confirmation of its relation to P4-PRIMITIVE.
- **No rerun** of the K₃ certificates or the Dyadic campaigns. No change to `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`. No physical selection of κ, γ or branch.

## 6. Reviews (pending)

- Change-focused review of stage 1 by the other Genesis co-owner (ChatGPT).
- Row check by the atlas owner.
- Results go to `records/gen/`.

## 7. What would be notified (no notices sent; PI decision)

- **UVM / OPEN M (IF08, pin v2.8.5).**
  - κ_f = |m||w| is the same quantity as UVM's |mw|.
  - B_* is recorded as undefined with unknown sign; UVM R2 cites m = 2Q_sB_*.
  - The sourced-junction minimizer clause is withdrawn; physical branch selection is OPEN.
- **RRF (IF30, pin v2.8.9).** The §7 export list now names three new RIDs. The sourced-junction export is rescoped. §6.3c exports are unchanged.
- **OFN (IF32).** §6.3a–§6.3c are unchanged apart from the G-20 note: (C2) is non-vacuous at C^∞ via Dyadic v6.4.22, and the analytic case stays OPEN.
- **Dyadic.** Informational: two v6.4.22 RIDs are imported for the §6.3c note. The v6.4.13 pins are unchanged.
- **Triadic.** Informational: the §6.17 four-case maximum is cited at v1.6.1 as a companion reading.

## 8. Adoption

Not adopted. Order per CONVENTIONS §4: reviews → stage 2 (or the PI's v2.8.10 fallback) → release record final → PI decision → publication commit → merge commit and tag by the PI.
