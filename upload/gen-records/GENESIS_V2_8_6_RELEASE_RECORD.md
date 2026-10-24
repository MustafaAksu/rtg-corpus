# Genesis Geometry v2.8.6 — Release Record

**Date:** 16 October 2026
**Owner decision:** Adopted by owner/PI decision, 16 October 2026, following Genesis v2.8.6 receiving review (19/19 PASS); scientific payload unchanged from the reviewed draft.

The 19/19 receiving result is a source-integrity and scope check. The mathematical theorem rests on its proof (§6.3a / SESSION record v0.1.2), not on that gate count.

## Identities

| Object | SHA-256 |
|---|---|
| Baseline: adopted v2.8.5 | `41ed76602c1c87c42972ac5b3f0a53f6973ac484427473ac371c57db1ab475cf` |
| Reviewed draft: `RTG_GENESIS_GEOMETRY_DSN_v2_8_6_DRAFT.md` | `434ea62a85b620dd95aa9b2798690cb09e535f1f02141d4a9cbcf829aba47104` |
| **Adopted release: `RTG_GENESIS_GEOMETRY_DSN_v2_8_6.md`** | **`294c6fc26482d7deae42900cb50b3029ac81e96d66e239bfe8b797e95fdaa269`** |
| Adoption transform `release_v2_8_6.py` | `422c9f3c38240fb2c012e8d51f52d528cfb2b61650c88450e013bec24f6a93dc` |
| Release checker `check_release_v2_8_6.py` | `6da2efdef1b0c9cd4bfd72cee23ed97787ba388c040b1d81cf903f21caa256e4` |
| Draft build `build_v2_8_6_draft.py` / checker `check_v2_8_6_draft.py` | `be667725…f9a5` / `fdcbd562…df669` |

**Chain:**
- v2.8.5 → draft: 28 declared edits; draft checker 18/18 here, 19/19 in the receiving review with M6c.
- draft → release: 11 metadata edits; release checker **7/7 PASS**.
  - Reverse transform is byte-exact.
  - Claim-tag counts are identical.
  - Every changed live line is metadata.
  - M2c is not marked source-verified.

## Scope (unchanged from the reviewed draft)

**In scope:**
- `GEN-THM-K3-PLANAR-FACTOR-NOGO` (§6.3a, SG-15);
- Dyadic v6.4.11 synchronization (N1 alias, N2 repin, NF6 at h-chart uses);
- OFN v0.9 pointer.

**Open / excluded:**
- physical G2 realization and OPEN-B/E1;
- Problem B;
- `Q-SUCC-UV-01`;
- V20-O1–O5 and Candidates A–C.

M2c (ν₅⁽⁵⁾ closed-form provenance) stays an open, non-blocking provenance item.

## Outbound notices (issued now, citing the adopted hash)

**→ RRF (G2-CLOCK).** Genesis v2.8.6 (`294c6fc2…a269`) adopts `GEN-THM-K3-PLANAR-FACTOR-NOGO`. The projected-K₃ primitive map has no local submersive factor of strictly lower real dimension:
- d = 1, 3 excluded at C¹;
- d = 2 excluded at C³; C¹/C² remains OPEN.

RRF may cite it at that scope without repeating the proof. Genesis selects no admissibility condition, carrier or physical node exchange (SG-15).

**→ Dyadic (N1, N2).**
- N1 is recorded: `GEN-DEF-PRIMITIVE-MAP` is an import/alias of `DYAD-DEF-PRIMITIVE-MAP`, and the Genesis RID is retained.
- N2 is applied: frame and v⊥ now point to `DYAD-DEF-BRIDGE-EXPORT-CONTRACT`, and the protection matrix to `DYAD-ALG-PROTECTION-MATRIX`. The antisymmetric channel is Genesis-native. `DYAD-ALG-NF6` is cited only at the two h-chart uses. `DYAD-ALG-LIEGAUGE-NORM` is no longer imported.
- Source pin: adopted v6.4.11 (`6fccd429…cb2e`). Dyadic v6.4.12 is not yet consumed.
- Separately: the ν₅⁽⁵⁾ closed form quoted in Genesis §6.2 is not printed in v6.4.10 or v6.4.11. Please indicate its source artifact.

**→ OFN (CUST-O09-01 / REQ-O09-04).** Answered: Genesis records `GEN-DEF-PRIMITIVE-MAP` as an alias of `DYAD-DEF-PRIMITIVE-MAP` (v2.8.6 §1). The OFN imports IMP-O08-01/10/11/13 resolve to unchanged §1/§6.1 blocks. The pins can move to v2.8.6 without scope change.

**→ Triadic (informational).** Dyadic N2 names Triadic as well; the Genesis repin does not change Triadic.
