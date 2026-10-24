# Atlas v0.4 — reconciliation of the two internal-consistency audits

**Date:** 24 October 2026. **Prepared by:** Claude, Atlas owner. **Status:** record (noncanonical); decides the v0.4 edit scope, adopts no owner science.

**Inputs.**
- Round 1, atlas owner: `records/atlas/ATLAS_V0_4_AUDIT_CLAUDE.md` (findings C04-01…C04-09; branch `claude/atlas-v0.4-audit`, PR #32; file SHA-256 `1b47746a142b1e4351fb0e56fbdeb15126a93a233907b2d9eadc7e8eb2f01b9d`).
- Independent round, ChatGPT: `records/atlas/ATLAS_V0_4_INDEPENDENT_CHATGPT_AUDIT.md` (findings A04-01…A04-06; branch `chatgpt/atlas-v0.4-independent-audit`, PR #31; file SHA-256 `882eac50c3d34439658132ca24f8ac7520a2417f5a0c764044b8097083b04c10`).
- Base: `atlas-v0.3` (`71310e8c…dc5b`); sources at `origin/main` `21edfb8d019f6f3130217035f387855cde87ce87`, where the only moved source is Programme v1.3 (`programme-v1.3`, file `1b8358b3…aea06`).

Rule applied throughout: owner text decides; the atlas records what owners state, marks its own identifications with `~`, and cites L5 rows by row id.

## 1. Agreement table

| Claude | ChatGPT | Subject | Outcome for v0.4 |
|---|---|---|---|
| C04-01 | A04-01 | SOURCES row and manifest still PROG v1.2; checker `sources` FAIL | PROG row → v1.3 / `programme-v1.3`; manifest PROG entry → tag, commit `02848538…`, sha `1b8358b3…`; `v0_3_input_equality` CHANGED for PROG only. |
| C04-02 | A04-01, A04-02 | H10 and PROG.G1/G2/G4/G7 describe v1.2 defects that v1.3 removed; G5/G6 partly stale | Retire G1, G2, G4, G7 (reasons in `evidence/atlas/v0.4/dispositions.json`); reword G5 (Programme side consistent with the P2B-CRITERION node; PREL side stays) and G6 (owner-recorded maintenance state, Programme v1.3 §9.2); H10 rebuilt from OPENM.U1 + PREL.P1/PROG.G6 and states that the corpus map is current at the snapshot; AZ.A3 mentions v1.3. |
| C04-03 | A04-02 | D1 nodes PROG-TIERS, PROG-INTERFACE-TYPES, `*PROG:IF-register`, D1 κ line reproduce v1.2 navigation | Rebuilt from Programme v1.3 §6.1, §7.1, §7.2 (IF01–IF36 with the settled IF17 custody split, pins per row) and §8.2 (κ table, 11 rows, cited as the owner-side navigation table). |
| C04-04 | A04-05 | H ↔ L5 referencing inconsistent (owner keys such as RER.E1, RER.E5, PREL.P2/P3 cited as if rows; high rows F1/F2/F3/F5/OFN.O1 not cited by any H) | Convention: every H cites L5 row ids only, many-to-one allowed; machine-readable map `evidence/atlas/v0.4/h_l5_map.json` with a dangling-key guard and a "high row without H" listing (empty at v0.4: H1 cites OFN.O1, F5, DYAD.X1; H7 cites F2, F3; H8 cites F1, OFN.O8 + RRF.F6, NUMGEN.N-S1; H11 cites LEGACY.Y2/Y3, OPENM.U9, PREL.P4). No new H lines were forced; H numbering stays display order. |
| C04-06…09 | — | consumer pins, recurring numbers, retired keys, carried checker limitations: no finding | Unchanged; carried limitations listed in the packet. |
| — | A04-06 | GEN K±/κ sign tensions, H9, F3 in unchanged domains | Deferred to the Genesis advisory (next stream); no GEN re-extraction in v0.4. |

## 2. Disagreement and its resolution

**A04-03 vs C04-05 — is "class-C κ ≡ GEN γ" an owner statement or an atlas reading?** ChatGPT read the v0.3 mixture (H8 and the D1 κ line without `~`, RRF.F5 with `~`) as atlas-derived equivalence promoted to identity, and cited Programme v1.3 §8.2, whose first row says the identification is "an atlas reading, not an owner statement". The owner texts were checked at their governing tags: OFN v0.10 §11.4 writes "γ ≡ κ ∈ ℝ∖{0,2}, under (H_spec)" and RRF v0.8.4 §6.2a writes "γ≡κ in the OFN class-C parameter convention". Genesis itself writes γ and states no identification. So the identification **is owner-stated** (OFN and RRF, as a parameter convention with its scope), and the v0.3 inconsistency is resolved in the other direction from A04-03's proposal: RRF.F5 loses its `~` and cites both passages; H8, the D1 κ line and the cross-domain index carry the convention scope ("by the OFN §11.4 / RRF §6.2a parameter convention, κ∈ℝ∖{0,2} under (H_spec); GEN itself writes γ"). The Programme v1.3 §8.2 sentence that A04-03 relied on is itself the error, recorded by the Programme owner as E-P13-1 (`records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_POST_RELEASE_NOTE.md`) for the next Programme edition; the atlas does not reproduce it. A04-03's principle — do not promote an atlas reading to identity syntax — is kept and applied below (A04-04).

**A04-04 — "every RER Triadic record sits in the flat A1 sector".** Accepted as a narrowing. The map-level identification RER 𝒩 ≡ GEN F₁ ≡ OFN raw κ=1 (RER-E-CONJ, F2) stays; the universal quantifier over RER records is replaced, at H7, the cross-domain index (K₃ model identity) and F2, by "the RER Triadic records built on 𝒩 (the F2 list) read as flat-sector reference results — a per-record scope reading, not verified against each record's hypotheses", marked `~`. No per-record transfer matrix is built in v0.4; RER's owner can supply the scope sentence F2 already asks for.

## 3. New finding taken into v0.4

**C04-10 — "κ_f" is an atlas label.** Genesis writes κ in both §6.8 (face-lift, κ=|m||w|) and §6.9 (scalar-M, κ=m|w|); the subscript f exists nowhere in GEN. The v0.3 atlas used κ_f as if it were an owner symbol (H6, H8, D1 κ line, RRF.F5, D4a κ line — where it listed "κ_f" separately from "face-lift κ", F1, FACE-LIFT node, D4b κ line, `*GEN:secular-K−`, SCALARM node, GEN.D5). v0.4 keeps the label where it disambiguates the two GEN κ's but says on every line that uses it that κ_f is an atlas label for the face-lift κ (guard in the build: a line containing κ_f must contain "atlas label"; κ_fit is excluded). The FACE-LIFT node now writes κ as GEN does.

## 4. Scope of the v0.4 edit (closed list)

Title, SOURCES header and PROG row, footer; H1 (keys), H6, H7, H8, H10, H11; cross-domain index lines for class C and K₃ model identity; D1 nodes PROG-TIERS, PROG-INTERFACE-TYPES, `*PROG:IF-register`, κ line; D1.L5 RRF.F5, PROG.G1/G2/G4/G7 (retired), PROG.G5/G6 (reworded); D4a κ line, F1, F2; D4b FACE-LIFT node, κ line, `*GEN:secular-K−`, GEN-THM-SCALARM-EIGEN flag, GEN.D5; D5.L5 AZ.A3. 35 exact-once operations (`evidence/atlas/v0.4/edit_log.json`). Nothing else in the atlas is touched; no owner DSN, source tag, Method edition or shared checker is changed.

## 5. Left for later

- Genesis advisory: A04-06 (K± sign conventions, GCL-02, κ family), H6/H9 owner checks, GEN.D1–D16.
- Programme next edition: E-P13-1 (κ≡γ provenance sentence in §8.2).
- RER owner: scope sentence citing OFN v0.10 (F2) and per-record applicability of the flat-sector reading.
- Pre-Legacy, TDR-G, DZT, AZ owner passes (Programme v1.3 §9.2); AZ.A3.
- Cross-stream notice structure (PI decision: none sent for now).
