# RTG State Atlas v0.4 — change-focused review packet

**Date:** 24 October 2026. **Prepared by:** Claude, Atlas owner.
**Status:** DRAFT / NONCANONICAL — receiving review requested (ChatGPT, Atlas co-owner); no PI acceptance or owner-science adoption. `atlas-v0.3` governs until acceptance.

## 1. Inputs and identities

Base `atlas-v0.3`, SHA-256 `71310e8c5e1b29979a854ee2ee932efa4765f038bbe0c10299e14f424ad1dc5b`. Source snapshot `origin/main` `21edfb8d019f6f3130217035f387855cde87ce87` (after PR #26/#27). The only moved source is Programme v1.3: tag `programme-v1.3`, commit `02848538b81637828826eeef8e3b73b09c7cc221`, file SHA-256 `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06`; the other 17 sources are byte-equal to their v0.3 inputs (manifest `v0_3_input_equality`). Method edition v0.2 (`atlas-v0.2`), unchanged.

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate) | `988d0fa93e4962240ecbe8dc296acf7626e7b47e05c302c749d9fe82d1c6b3c4` (469,440 bytes, 1,557 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.4/source_manifest.json` | `dc8a840694f6da4cb42b5829efac02c4021c36a7ba52ac801b4e1d29409ca037` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_4.py` | `0fb9f466cade2172959f967639d8f73b7009b7b9517f44cfface05f7aa0f5c56` |

Decision basis: `records/atlas/ATLAS_V0_4_RECONCILIATION.md` (the two audits C04-01…10 and A04-01…06 and their reconciliation).

## 2. Review scope

This is an internal-consistency refresh plus the Programme v1.3 source move — not a re-extraction of any scientific domain. 35 exact-once operations in a closed list (reconciliation §4):

- **Programme move (C04-01/02/03, A04-01/02).** SOURCES row and manifest to v1.3. H10 rebuilt: the "corpus map out of date" claim is withdrawn (Programme v1.3 inventories every home, RRF, the noncanonical records and the atlas at their governing tags); what remains are the OPEN-M chart audit (OPENM.U1) and the Pre-Legacy owner pass, now cited from Programme v1.3 §9.2 (PREL.P1, PROG.G6). PROG.G1, G2, G4, G7 retired; G5 and G6 reworded; AZ.A3 mentions v1.3. D1 nodes PROG-TIERS, PROG-INTERFACE-TYPES and `*PROG:IF-register` rebuilt from §6.1, §7.1, §7.2 (IF01–IF36; IF17 settled custody split); the D1 κ line cites §8.2 as the owner-side navigation table.
- **κ ≡ γ provenance (C04-05 vs A04-03; owner text decides).** RRF.F5 becomes an owner-stated convention row citing OFN v0.10 §11.4 (claim-level import of `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`: γ ≡ κ ∈ ℝ∖{0,2}, under (H_spec)) and RRF v0.8.4 §6.2a; H8, the D1 κ line and the cross-domain class-C line carry the convention and its scope; "GEN itself writes γ" is stated. The Programme v1.3 §8.2 sentence calling this an atlas reading is the Programme's error (E-P13-1), not reproduced.
- **RER flat-sector reading narrowed (A04-04).** H7, the K₃-identity index line and F2 now say that the RER records built on 𝒩 (F2 list) *read as* flat-sector reference results, `~`, per record, not verified against each record's hypotheses; the map-level identity RER-E-CONJ stays as stated.
- **κ_f is an atlas label (C04-10).** GEN writes κ in §6.8 and §6.9; every atlas line that uses κ_f now says it is the atlas label for the face-lift κ (H6, H8, D1 κ line, RRF.F5, D4a κ line, F1, FACE-LIFT node — which now writes κ as GEN does —, D4b κ line, `*GEN:secular-K−`, SCALARM node flag, GEN.D5).
- **H ↔ L5 convention (C04-04, A04-05).** Every H line cites L5 row ids only (owner keys inside D4a rows such as RER.E1 are not row ids). Map and guard: `evidence/atlas/v0.4/h_l5_map.json` (12 H lines, 137 L5 rows, 0 dangling keys, 0 high rows without an H). H1 now cites OFN.O1; H7 → F2, F3; H8 → F1, OFN.O8 + RRF.F6, NUMGEN.N-S1 (RER.E5 and the retired PROG.G7 dropped); H11 → LEGACY.Y2, LEGACY.Y3, OPENM.U9, PREL.P4.
- **Deferred (A04-06).** GEN K±/κ sign tensions, H9, F3: Genesis advisory, not v0.4.

## 3. Dispositions and mechanical checks

11 touched L5 rows: 4 retired (PROG.G1, G2, G4, G7; keys added to `evidence/atlas/v0.4/retired_l5_keys.json`, not reused), 7 reworded (RRF.F5, PROG.G5, PROG.G6, AZ.A3, F1, F2, GEN.D5); hashes in `evidence/atlas/v0.4/dispositions.json`. Edit locators and hashes in `edit_log.json`; two builds give identical bytes; reproduce with `python3 -I evidence/atlas/build/refresh_v0_4.py` at the snapshot (the script asserts the base hash, every source tag's file hash and commit, and tag/snapshot byte equality).

Shared checker `tools/atlas_check.py`: **zero FAIL** (the v0.3-era `sources · PROG` FAIL is cleared); PASS counts sources 72, coverage 128, qualifiers 3, links 410, artifacts 96, keys 59. Carried, unchanged from v0.3 by text: 4 link UNVERIFIED + 3 artifact UNVERIFIED (= the 7 UNVERIFIED of the v0.3 record), 11 DOCUMENTED-UNRESOLVED, 16 wording WARN (three new time-relative words introduced by the first build were removed before this candidate). Shared negative controls 18/18 as expected; focused controls 6/6 detected (dangling H key; owner key cited as a row; retired key reused; SOURCES row older than the manifest; unlabelled κ_f; high row losing its H citation) — `evidence/atlas/v0.4/negative_controls.json`, `shared_controls.json`, `verification_summary.json`.

## 4. Questions for receiving review

1. Programme v1.3 extraction: are PROG-TIERS, PROG-INTERFACE-TYPES, the IF01–IF36 register line and the κ-line pointer faithful to §6.1, §7.1, §7.2, §8.2 (pins per row, IF17 wording, class/tier separation)?
2. κ ≡ γ: do you accept the owner-text ruling (OFN §11.4 / RRF §6.2a) over A04-03's reading, and the wording "by the … parameter convention … GEN itself writes γ" at H8, D1 κ line, class-C index line and RRF.F5?
3. RER narrowing: is the `~` per-record wording at H7, the K₃ index line and F2 what A04-04 asked for, or do you want the universal statement removed entirely?
4. κ_f: is "atlas label" stated at every use (guard says yes), and is keeping the label at all preferable to writing GEN's κ with section references?
5. H ↔ L5: any H key you read differently from `h_l5_map.json`; any high L5 row you think needs its own H line rather than coverage by H1/H7/H8?
6. Anything in the diff outside the closed list of reconciliation §4.

## 5. Publication boundary

The candidate is not accepted by this build. Acceptance needs the receiving review, then PI acceptance identifying the bytes `988d0fa9…6b3c4`, a merge commit (not squash) of `claude/atlas-v0.4` into `main`, and an annotated `atlas-v0.4` tag on that merge naming the hash. No owner DSN, grade, source tag, notice state, Method edition or consumer adoption is changed. `atlas-v0.3` remains the accepted Atlas until that decision.
