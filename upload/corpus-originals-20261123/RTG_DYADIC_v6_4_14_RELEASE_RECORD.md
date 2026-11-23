# DYAD v6.4.14 — Release Record

**Date:** 19 October 2026
**Owner decision:** owner/PI adoption, 19 October 2026, after external review of DRAFT r1 (`SCIENTIFIC REVIEW ACCEPTED`; `REVIEW ACCEPTED — OWNER ADOPTION READY`).
**Status:** v6.4.14 is the adopted Dyadic owner file from this release. v6.4.13 is superseded and preserved unchanged. Release verification by the reviewer is pending.

## Identities

| Object | SHA-256 |
|---|---|
| Prior adopted v6.4.13 (unchanged) | `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542` |
| Reviewed DRAFT r1 | `7f7ea7f3d7262b1297da5b5dc65f73f8e55ab03370189a6302ab44967aef6ebf` |
| **Adopted `RTG_DYADIC_OSCILLATOR_DSN_v6_4_14.md`** (1363 lines) | **`7fb8510563af17701dce7815c0a0f10771f0ff69490d22d1ea3d1af120b56bdd`** |
| r1 → final diff | `d36cddc6dc00be8b30dbf750254bf04cc166d90ef81ca11db1bfed88fbeb526d` |
| v6.4.13 → final diff | `0c6bfb0a5268c143e3d50246916f5737d937cdba7665e81eb36c64825b02cf6c` |
| `release_v6_4_14.py` / `check_release_v6_4_14.py` | `f156486c…4dd8` / `6097999a…e430` |
| Release checker output / negative-control output | `7921e87d…1acc3` / `c607cf9f…0e62` |
| Install manifest `RTG_DYADIC_v6_4_14_INSTALL_MANIFEST.json` | `a1534f7c07ff0fd1cae3a8f4d47ca3da0b10a69536e8c320e1784f057dd15815` |
| r1 manifest / r1 build / r1 checker | `88bfa0b2…a573` / `c815bd3e…eebd` / `9b08cf03…3b16` |

## Chain

1. **v6.4.13 → DRAFT r1.** 18 anchor-based edits (`build_v6_4_14_r1.py`). The r1 checker passed 12/12 gates, and its 5 negative controls failed as required. The reviewer independently rebuilt r1 and got identical bytes.
2. **DRAFT r1 → final.** 32 anchor-based label and metadata edits (`release_v6_4_14.py`). The release checker passed 12/12 gates (R0–R11), and its 5 negative controls failed as required.
3. **What the release checker verified:**
   - the transform is deterministic;
   - the RID set is identical to r1;
   - no draft or proposed label remains before Appendix A;
   - only label and metadata lines changed;
   - the scientific invariants are verbatim (the two constant rows, (I-5), the theorem inequality, c₃ and the L_Θ ceiling);
   - the Appendix A DRAFT r1 record is byte-identical;
   - the adopted grades appear on the two RID lines;
   - the OPEN 3 lifecycle (3a, 3b, 3c) is in place;
   - the three recorded distinctions are retained.
4. **RID difference, v6.4.13 → v6.4.14:**
   - added: `DYAD-ALG-OPEN3-LEADING`, `DYAD-THM-OPEN3-SPIRAL-REM`, `DYAD-ART-OPEN3-P2`, `DYAD-ART-OPEN3-P3`, `DYAD-ART-OPEN3-RECORDS`;
   - removed: none.

## In force from this release

- **`DYAD-ALG-OPEN3-LEADING`** `[ALG]`: the exact leading terms D₃, D_{Θ,1}, [S_Q]₅ and L_Θ, and the identity P₅(𝓛⁻¹z) = DD₃[μqz] + 2qD₃.
- **`DYAD-THM-OPEN3-SPIRAL-REM`** `[THM]`: |S_Θ − L_Θ| ≤ K_Θq² and |S_Q − [S_Q]₅| ≤ K_Qq³, with the rows kept separate:

  | Row | K_Θ | K_Q |
  |---|---|---|
  | \|z\| ≤ 1/20 | 123/125 | 2353/1000 |
  | \|z\| ≤ 1/40 | 909/1000 | 258/125 |

  These constants are majorant suprema, not true-error suprema.
- **OPEN 3: PARTIAL.**
  - 3a (per-block chart residual): CLOSED;
  - 3b (P4, asymptotic-phase transfer): OPEN;
  - 3c (P0, historical fit): BLOCKED.
- **Notices.** N8 is RECEIVED (Genesis v2.8.8). N9 is RECEIVED by RRF (v0.8.3); OFN has it only at session level. N10 is issued to RECOG and NUMGEN with status PENDING.
- **Unchanged.** All v6.4.13 RIDs and grades are unchanged. OPEN 20 stays PARTIAL (B-an, B-6 and B-∞ existence OPEN).

## Carried open

- **P4 (OPEN 3b).** Two results are to be proved separately: (i) the primitive and normalized asymptotic-phase limits are equal; (ii) the finite-q₀ O(√q₀) static offset.
- **P0 (OPEN 3c).** BLOCKED: `spiral_phase_fit.py` is unavailable.
- **Provenance.** h and J have not been compared byte for byte with the adopted P2B v2 `certificate.json`. h matches the 19 Sep audit reconstruction exactly (23/23 coefficients), but that comparison does not replace this one.
- **Other items.**
  - N3;
  - the Triadic part of N2;
  - the OFN owner-level receipt of N7 and N9;
  - the two v6.4.10 hashes carried forward.

## Outbound (after release verification, citing the adopted hash)

- **→ RECOG, NUMGEN (N10).** The OPEN 3 chart-level results are available for import at their grades. No statement is made about C_W^{(h)}, and R9 is not transferred to the raw track (SG-R14). No NUMGEN L1 coefficient is transferred (SG-19).
- **→ Genesis, RRF, OFN.** Informational only. v6.4.14 does not change any RID they import.
