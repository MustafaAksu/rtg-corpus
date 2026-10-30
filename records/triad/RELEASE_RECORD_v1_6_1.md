# Triadic Birth-Lift DSN v1.6.1: release record

**Date:** 19 October 2026.
**Decision:** owner release (ADOPTED), on the PI's explicit authorization of 19 Oct 2026 ("Triadic v1.6.1 yayınını yetkilendiriyorum").
**Status:** v1.6.1 is the Triadic owner file from this release. v1.6 is superseded and preserved unchanged. Release verification by the receiving co-owner is pending.

## Identities

| Object | SHA-256 |
|---|---|
| Superseded v1.6 | `c768687cec6d52ffd358dc362cee4348f076160943564adaa461e6c7c4595b36` |
| DRAFT r1 | `31b87c3edc90a2ec54f97d5b63ac043ab0d2b3bcd495ddb35b05f3a9cb4630ea` |
| Reviewed DRAFT r2 (scientific review ACCEPTED, 19 Oct) | `dd67907fc21e457e413c3d6ee924617bc7818c1c200a9bde04fb67649d79b3e7` |
| **Adopted `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6_1.md`** (1202 lines) | **`95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`** |
| `v1_6_1_release_edits.json` (12 edits) / `make_release_edits.py` | `d64adc3f…8e17` / `d47d9000…2b1b` |
| `release_v1_6_1.py` / `check_release_v1_6_1.py` | `8dfde4ef…eaff` / `8d0a58ef…a707` |
| Checker output / r2→release diff (66 lines) | `edc2f089…1866` / `a3116572…00e5` |

## Chain

1. **v1.6 → DRAFT r1.** 28 edits: D3 and hygiene D1–D10.
2. **DRAFT r1 → DRAFT r2.** 22 edits: D3-R1, H-R1, H-R2 and E1. The co-owner receiving review returned SCIENTIFIC REVIEW ACCEPTED.
3. **DRAFT r2 → release.** 12 metadata-only edits. The release checker passed 10/10 gates:
   - R0–R2: base hash, deterministic rebuild, byte-exact reversal to r2;
   - R3: every changed line is a declared metadata line;
   - R4: §§1–8, the rest of §9, the draft history from the r2 entry onward and Appendix B are byte-identical to r2;
   - R5: title, status and footer are released;
   - R6: RID set (46 tokens) and claim-tag counts are identical to r2;
   - R7: the release note names the three newer owner hashes;
   - R8: the v1.6 approval is not reused;
   - R9: the v1.6 metadata is kept as labelled history.

   The negative controls for R3/R4, R5, R6 and R8 each fail, as required.

## In force from this release

**D3.** The cubic birth term c₀^{[3]} = κQ_sJ_Qs keeps its owner theorem grade. The following hold only under the selected child functional (Genesis GCL-06), for p > 3:
- the fifth-order child remainder;
- the full-child ratio iκQ_s + O(Q_s^{(p−1)/2});
- the phase −π/2 + O(Q_s^{(p−3)/2}).

These bounds are stated at §6.1, §6.15, §6.17.2, §7.2 and CN-02. T-6u leading ratios and the reference-policy coefficients are unchanged.

**Pins.**
- Dyadic v6.4.13. Notice N2 (frame and protection matrix routed through `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` / `DYAD-ALG-PROTECTION-MATRIX`) is answered for Triadic.
- Genesis v2.8.7, including the four point-of-use imports in §6.15 and §6.17.1.
- RRF v0.8.2 §3.1.

**Release note.** Genesis v2.8.8, Dyadic v6.4.14 and RRF v0.8.3 were adopted on 19 Oct. Their owner records report that the items cited here are unchanged (OWNER-REPORTED). Repinning is deferred to the next maintenance pass.

**Unchanged.** No value, grade, RID or certificate changes. No result is retracted.

**Open.**
- physical child-functional selection;
- T-6r, T-6q, T-6m2, T-6n and T-6o;
- the physical questions of CN-01 and CN-04;
- Programme v1.2 pass two.

## Outbound (after release verification, citing `95340abe…451f`)

- **→ Dyadic.** Notice N2, Triadic part, is ANSWERED: v1.6.1 §7.1 pins v6.4.13 with `DYAD-DEF-BRIDGE-EXPORT-CONTRACT`, `DYAD-ALG-PROTECTION-MATRIX` and `DYAD-DEF-PRIMITIVE-MAP`. v6.4.14 is OWNER-REPORTED as unchanged for these RIDs.
- **→ Genesis, OPEN-M, RRF, OFN.** Informational. D3 is now the owner text: the full-child remainder, ratio and phase orders are conditional on GCL-06. The CN-01–CN-05 content is unchanged.
- **→ RER.** v1.6.1 replaces the "v1.6 adopted + v1.6.1 draft" pair as the Triadic source object at the next RER synchronization.
