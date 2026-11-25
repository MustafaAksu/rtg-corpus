# RRF v0.8 full-content review candidate — merge provenance and QA

**Date:** 14 October 2026  
**Disposition:** COMPLETE-CONTENT CANDIDATE / **NOT ADOPTED**  
**Compared with:** Mounted `RTG_RRF_REPRESENTATION_REGISTRY_v0_7_DRAFT.md`, **not** the adopted final v0.7 file.

## 1. What the user supplied

The current handoff supplied the reviewed v0.7 **DRAFT**, the separate v0.7 **adoption record**, the earlier October source-sync review and two RRF coincidence reviews. The adoption record reports a distinct final file named `RTG_RRF_REPRESENTATION_REGISTRY_v0_7.md`, size **57,524 bytes** and SHA-256 `2a2b4102ba12e53bc56c746ffe30c553d24ecffa90afddeb4027cd72307717a5`. That final file is **not mounted**.

- Mounted v0.7 DRAFT: 54734 bytes; SHA-256 `b7135dc9859fd17282b6fb70eee4dea04869d9bc2a405ad7fcbbb9cbb070bab9`.
- New complete-content v0.8 review candidate: 72615 bytes; SHA-256 `09fd4e010df6848ad52930a4af4ab64cf68642d8ebbed0afdc0c3fb58ba94abb`.

**Therefore this is NOT a proven lossless successor to the adopted 57,524-byte file.** It is an integral, reviewable merge based on the only mounted full registry baseline, annotated with known finalization policy but without fabricating the final artifact.

## 2. Applied scope

| Area | Disposition |
|---|---|
| Existing profiles and transport graph | Retained from mounted v0.7 DRAFT; four dyad profiles plus one provisional network profile |
| §0 source-state receipts / theorem-owner boundary | Added current OFN/RECOG/Genesis/Triadic/ER-2B/RER-plan boundary; imported the adoption record’s theorem policy |
| §4.2a | Scoped cross-model `T_k↔T_{-k}` family conjugacy; fixed `T_1` symmetry and physical swap not identified |
| §6.2 | Proposed `RRF-CND-01` full-state coincidence, encoding, witness and clock/merge contract; physical selection still OPEN |
| §6.3 | CELL-F4 W1–W5 prerequisite inventory; token-to-cochain not yet well-posed |
| §6.4 | Optional dynamical-closure taxonomy with remainder/time-horizon and RER Stage-2 global-certification guard |
| §8.1 | Explicit no-transfer and nonclaims for conditional models and pending RER evidence |
| §9/§10.1 | New **candidate** history and missing-final source/verification disclosure |

## 3. Mechanical checks

| Check | Status |
|---|---|
| owner OFN v0.9 | PASS |
| owner RECOG family RID | PASS |
| owner RECOG CELL-F4 RID | PASS |
| owner RECOG B-token RID | PASS |
| v0.7 adoption hash declared | PASS |
| draft matches adoption base hash | PASS |
| exact native profile headings unchanged | PASS |
| v0.7 draft histories all preserved | PASS |
| old NF numerical coefficient preserved | PASS |
| v0.7 OPEN lock retained | PASS |
| only one proposed coincidence interface | PASS |
| both files code fence counts equal | PASS |
| no v0.8 adoption stated | PASS |
| RER plan only guard | PASS |
| §§2.1-2.3 verbatim | PASS |
| §2.4 only convention edit | PASS |
| §2.5 network profile verbatim | PASS |
| §3 transport table verbatim | PASS |
| OFN source fixed state cited | PASS |

**Scientific checks NOT performed in this merge:** independent complete symbolic jet expansion, rerun of the RER Stage-2 verifier, proof of physical node realization, original RECOG certificate replay, fresh owner mathematical theorem proof. Textual RID presence is a source-location check, not a rerun.

## 4. Blocking before final v0.8 adoption

1. Supply the **exact** adopted final `RTG_RRF_REPRESENTATION_REGISTRY_v0_7.md` and authenticate its full SHA/byte count against the separate adoption record.
2. Diff adopted final **against this review candidate**, carry forward every editorial release boundary/source snapshot statement that differs; require no unexplained deletion or formula/profile mutation.
3. Review optional clause `K_closure` with RER after actual RER v0.2 text/evidence is received; no upgraded Stage-2 global certification without audited verifier.
4. Record explicit RRF working-standard adoption separately if authorized; do not infer adoption from this file.

## 5. Deliverables

- `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_REVIEW_CANDIDATE.md` — full-content draft, not adopted.
- `RTG_RRF_v0_7_DRAFT_to_v0_8_CANDIDATE.diff` — reproducible unified diff **from the draft**, not an adopted-final diff.
- `RTG_RRF_v0_8_CANDIDATE_REVIEW_MANIFEST.json` — source/candidate identities and availability boundary.
- This QA note.
