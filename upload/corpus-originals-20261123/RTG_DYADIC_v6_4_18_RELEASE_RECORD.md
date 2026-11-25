# DYAD v6.4.18 — Release Record

**Date:** 20 October 2026
**Owner decision:** owner/PI adoption, 20 October 2026, after external review of DRAFT r1 (`v6.4.18 DRAFT r1 — SCIENTIFIC REVIEW ACCEPTED`).
**Status:** v6.4.18 is the adopted Dyadic owner file from this release. v6.4.17 is superseded and kept unchanged. **Release verification by the reviewer is pending.**
**Installation:** the final file, install manifest, this record and N14 were written to the project under `claude/` from the verified local bytes. The project copy was not re-read and hashed in this session.

## Identities

| Object | SHA-256 |
|---|---|
| Prior adopted v6.4.17 (unchanged) | `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` |
| Reviewed DRAFT r1 | `6abed0b86332728d41eeea265eb97e8fac6bc1a036e538fa671493112ea3d1b3` |
| **Adopted `RTG_DYADIC_OSCILLATOR_DSN_v6_4_18.md`** (1539 lines) | **`f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d`** |
| r1 → final diff | `571e2230…7e97` |
| v6.4.17 → final diff | `d3502631…a153` |
| `release_v6_4_18.py` / `check_release_v6_4_18.py` | `31d585e7…e8e1` / `9291eeca…6c40` |
| Install manifest | `RTG_DYADIC_v6_4_18_INSTALL_MANIFEST.json`; it lists this record, so its own hash is given in the release package listing, not here |
| N14 notice | `792b252e…d190` |

## Chain

1. **v6.4.17 → DRAFT r1.** 16 anchor-based edits. Draft checker 13/13; 8 negative controls fail as required. Reviewer: manifest 20/20, checker 13/13, payload scripts re-executed (integration 6/6, P3-a 8/8, P3-b/c 3/3) with their internal negative controls.
2. **DRAFT r1 → final.** 19 label and metadata edits (20 lines). Release checker 12/12 (R0–R11); 7 negative controls fail as required.
3. **RIDs:** 129 → 132. Added `DYAD-THM-SMOOTH-EMBEDDING`, `DYAD-ART-OPEN20-BINF-RECORDS`, `DYAD-ART-OPEN20-BINF-CHECKS`; none removed. Graded RID lines = v6.4.17 plus the one new theorem.
4. **Package.** Self-contained for v6.4.17 → r1 → final, including all O20-∞ proof records and the three check scripts with their pinned JSON outputs.

## In force from this release

- **`DYAD-THM-SMOOTH-EMBEDDING`** `[THM]`, C^∞ germ scope:
  - E1: F = T⁶ = φ¹_X, X ∈ C^∞, j^∞X = log F.
  - E2: X unique among C^∞ generators with DX′(0) = 0 (only this class).
  - E3: unique C^∞ tangent-to-identity roots K_m, commuting with T.
  - E4: C^∞ J = T∘K₆⁻¹ and involution R = T³∘K₂⁻¹.
- **OPEN 20:** B-∞ existence CLOSED; overall PARTIAL; B-an and B-6 OPEN.
- **Unchanged:** Lemma F `[THM]`, F1–F3 `[THM — conditional]` (existence condition discharged for K_m, J, R), DYAD-THM-FORMAL-Z6-GENERATOR, OPEN 3 and OPEN 21 closures, and every other adopted RID and grade.

## Recorded distinctions

- G_∞ (Borel time-one map) is unrelated to G = J² of §6.16.
- The proof route is G_∞⁻ⁿFⁿ; the §6.17 route F⁻ⁿR_∞Fⁿ remains unproved.
- The radius is qualitative; no finite-C^k constants are claimed.
- C^∞ existence says nothing about analyticity; SG-14/15 hold.
- The eight draft-checker negative controls are owner reruns recorded in the package.

## Carried open

- OPEN 20: B-an, B-6.
- N3; the Triadic part of N2; the OFN owner level of N7 and N9.
- N10–N13 receipts.

## Outbound (after release verification only)

- **N14 → FMS, RRF, OFN**, citing the adopted hash. Sent by the PI. No import required.
