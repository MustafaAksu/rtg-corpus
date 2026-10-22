# DYAD v6.4.20 — Release Record

**Date:** 21 October 2026
**Owner decision:** the PI's explicit owner adoption of 21 October 2026 ("Ben onaylıyorum", 18:14 +03:00), recorded as `DYAD v6.4.20 — OWNER ADOPTION AUTHORIZED`. This decision is separate from the scientific review, which returned `DYAD v6.4.20 DRAFT r2 — REVIEW ACCEPTED`.
**Status:** v6.4.20 is the adopted Dyadic owner file from this release. v6.4.19 is superseded and kept unchanged as the historical adopted release. **External verification of the final SHA-256 is pending.** N16–N20 are not prepared or sent until it is done.
**Installation:** this record, the install manifest and the release scripts (`claude/atlas/release/`) were written to the project. **The final file is not yet installed in the project:** the project write was refused because the project is at its size limit (§5). The final file is delivered in the release package.

## 1. Identities

| Object | SHA-256 |
|---|---|
| Prior adopted v6.4.19 (unchanged) | `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9` |
| ATLAS P1 working file | `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905` |
| DRAFT r1 | `a5c70f5b1468ab01ba1cdf932fb9205c4bf00976a2b6523e8b90210e5e457c4a` |
| Reviewed DRAFT r2 | `f2030f853b94a7caa1d1d7c4afd8bdf9b6059582d331100bb0033226fd68465e` |
| **Adopted `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md`** (2793 lines) | **`0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`** |
| r2 → final diff (`r2_to_final.diff`, GNU diff normal format) | `4961ee46599e784e13025bc50ba8541f55dbc6bf6bc0df63609d6df7b07c0499` |
| `release_v6_4_20.py` / `release_v6_4_20_log.json` | `14384eaaa4e0208072c40d876b73cc79343ac672a0e4455753ebc8e3c4e0091d` / `7ac86364ac0c4559219804c60bb13ad1659096a53b5ccd2374e9c950053e3c68` |
| `check_release_v6_4_20.py` / `check_release_v6_4_20.json` | `5350a72168a7c7002ff26be24f87a39d17025855cd3c27c832140c7a9207badb` / `e08340e9be0abc3162b9f05b1d11ccebedd97b4e631fc3d40aac3ea6f33e3a96` |
| `p2_release_controls.py` / `release_controls_v6_4_20.json` | `79c20746b195c15ef26800982f389bfd3e919b0ce0b41c599876c4365809a59d` / `d06fc098585455709913ec0ce022ce0307fef827b11c871819a8b1e3984b78b6` |
| Install manifest | `RTG_DYADIC_v6_4_20_INSTALL_MANIFEST.json`. It lists this record, so its own hash is given in the package `SHA256SUMS.txt` |

## 2. Chain

1. **v6.4.19 → ATLAS P1 working file.** Scientific corrections. Review: `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED`.
2. **P1 → DRAFT r1.** Editorial and interface pass: 36 anchored edits and 12 relocations. Review: `v6.4.20 r1 — REVIEW ACCEPTED WITH MINOR CORRECTIONS`.
3. **r1 → DRAFT r2.** 39 single-line record corrections. Review: `DYAD v6.4.20 DRAFT r2 — REVIEW ACCEPTED`.
4. **r2 → final.** `release_v6_4_20.py`, labels and metadata only:
   - 55 lines are replaced in place, and each is quoted verbatim in the new Appendix A record "v6.4.20 — adopted 21 October 2026";
   - the "proposed / registered only at adoption" markers of the 13 new RIDs become "registered at adoption";
   - the header, footer, the §7.0 Dyadic row and the wording of the notice table, Appendix E, F and G are put in adopted form.
5. **Release checker R0–R11:** 12/12 PASS. Two clean transforms are byte-identical.
   - R2 confines the changes. Outside the record, the final file has r2's line count. Every changed line is quoted. In every changed non-header line, the removed words come only from a fixed label vocabulary.
   - R3: RID tag set and live tag sequence equal r2.
   - R4: every math span is unchanged.
   - R5: the grade-tag sequence is unchanged.
   - R9: OPEN status lines are unchanged.
6. **Release negative controls:** P0 passes, and all 11 others behave as expected: N0 one byte → R0; X1 constant → R4; X2 grade → R5; X3 RID tag → R3; X4 label residue → R6; X5 header decision → R7; X6 second footer → R8; X7 OPEN 20 sentence → R9; X8 evidence item → R10; X9 E.1 label → R11; X10 removed "not" → R2.
7. **RIDs:** tagged identifiers 135 (v6.4.19) → 148. None removed or renamed. The 13 RIDs registered by this adoption are:
   - `DYAD-ALG-KP-FRAME-SCALE`;
   - `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`;
   - `DYAD-ALG-B5-ALLP-NONVANISHING`;
   - `DYAD-ALG-RAW-ANGULAR-MEAN`;
   - `DYAD-ALG-ONE-BLOCK-BURST`;
   - `DYAD-ALG-P5-RADIAL`;
   - `DYAD-ALG-SIXSTEP-CUBIC-JET`;
   - `DYAD-ALG-Q3-DEG2-CANCEL`;
   - `DYAD-DEF-CRITICAL-CURVE`;
   - `DYAD-ALG-QC-CRITICAL-AMPLITUDE`;
   - `DYAD-ALG-ISP-MAPS`;
   - `DYAD-ART-ATLAS-P1`;
   - `DYAD-ART-ATLAS-P2`.

## 3. In force from this release

- **ATLAS P1 scientific corrections and P2 interface work**, at the reviewed r2 scope, with the 13 RIDs above.
- **Unchanged:** every earlier statement, grade, scope and OPEN status. OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-an and B-6 are OPEN. OPEN 9 is PARTIAL.
- **Kept distinctions:**
  - FA-08: the formula is verified; its match with the historical OPEN 9 source is not complete.
  - FA-04: `degree_b_vanishing_cert_v2.py` is not available.
  - FC-32 (H-NG) stays SESSION only.
  - Editions without a recorded hash stay "not recorded".

## 4. Evidence levels (kept separate)

| Level | Content |
|---|---|
| `REVIEWER-REPLAYED` | **r2 review:** r2 hash and package (26/26); r1→r2 build; r2 checker G0–G21; r2 negative controls; M1–M11; S1–S4 with C1–C2 on the packaged RECOG v0.3.20/v0.3.21/v0.3.22 files; records R1–R4 with D1–D2. **r1 review:** r1 hashes and package (16/16); r1 builder; G0–G18; N0–N16; K1–K3. **P1 review:** P1 working file and the FA-07/FB-13 checks |
| `OWNER-RUN` | Release transform; release checker R0–R11; release negative controls; installation read-back (§5) |
| `REVIEWER FULL REPLAY NOT COMPLETED` | The combined G14–G15 run carried from v6.4.19, a separate historical item that the v6.4.20 reviews do not close. The release checker of this edition, until it is replayed |
| `REVIEWER-MEASURED` | The v6.4.17 and v6.4.18 release-record hashes in addenda v0.1.1 (r1 review). Not owner-measured, and not re-measured in the r2 review |

Same-script replays are not second methods. The scientific results keep their own rows in Appendix E.

## 5. Installation check

The write of the final file to `claude/RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md` was refused on 21 Oct 2026 because the project is at its maximum size; nothing in the project was changed by that attempt. Installation and read-back are **pending** until room is made (the PI decides which docs to remove; the owner removes none). After installation the project copy is read back and compared with the SHA-256 in §1. The package copy was verified against `SHA256SUMS.txt` in a clean directory (12/12 OK) and the release transform, checker and controls were replayed there byte-identically.

## 6. Carried open

- External verification of the final SHA-256.
- Installation of the final file in the project (refused: project size limit) and its read-back.
- N16–N20 (ATLAS disposition §6). These are prepared after external verification, each citing the verified hash, and sent by the PI.
- Row B.
- The combined G14–G15 reviewer replay (v6.4.19).
- FC-31.
- O20-an (López-Hernanz source).
- The missing `degree_b_vanishing_cert_v2.py`.
- The FA-08 historical source match.
- Owner re-measurement of the v6.4.17 and v6.4.18 release-record hashes.
- OPEN 20: B-an and B-6.

## 7. Outbound (after external hash verification only)

| Notice | Recipients | Content |
|---|---|---|
| N16 | Genesis; OFN | FB-13 chart corollary, FB-25, FA-05 |
| N17 | DZT; AZ | crosswalk, sign, VANISH-B2, FA-08 outcome |
| N18 | NUMGEN | export table, φ*, FC-33, FC-32 for information |
| N19 | RECOG; RRF | R9 import row, S_h routing, FC-32 offered, FA-07 |
| N20 | Triadic | FA-07 frame qualifier, informational |

These follow the disposition §6 plan. Import is each owner's decision.
