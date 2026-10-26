# Number Genesis v1.20.4 — Freeze Manifest

**Manifest ID:** `NG_V1204_FREEZE_MANIFEST_v1` · **Date:** 2026-09-28
**Ruling:** co-owner — v1.20.4 scientific/sync patch APPROVED; preservation of the 19 grade-decision rows APPROVED; STOP-04 CLOSED; count-definition precision fix (23 = 19 + 4) verified. **v1.20.4 FROZEN.**
**Class:** scientific-sync + editorial/governance correction patch.

## Canonical freeze pin
```
5559169a10e0b04ddfaa7d8d9e4a5b886809dcaabee648f0a4c5a6a1d27eed8b  RTG_NUMBER_GENESIS_DSN_v1_20_4.md                  FROZEN OWNER (3254 lines, LF)
c19f11968b976cbedc0eadd5384ed2ff28e3bf6acd50238635d95ccb72a7b4d8  RTG_NUMBER_GENESIS_DSN_v1_20_4_fingerprint_v2.json  generator v2.3 (1fbeb19d…3ff6); 495 blocks, dup 0/0
bfd654e204bb19a7821cd07a20a1f4e3cdca891ed00bc1e7fe953894b308329c  RTG_NUMBER_GENESIS_v1_20_3_to_v1_20_4.diff          4 hunks
```

## Verified delta v1.20.3 → v1.20.4
493 → 495 claim blocks: 2 replacements (status summary; the block carrying the §6.3a self-reference) + 2 new changelog `[COR]` blocks. Explicit RIDs unchanged; broad identifiers + `STOP-04` only. 29 status lines identical and in order; Priority queue, §8 and all earlier changelog byte-identical. The **23** live combined `[from: …/…]` occurrences (**19** independent scientific grade-decision rows + **4** §9.2 provenance mirrors) are untouched. Independently reproduced by the co-owner.

## Known coverage boundary (recorded, not a defect of this release)
STOP-04's sentence carried no status tag, so it lay outside every FP-v2 claim block: unanchored prose is invisible to the fingerprint and is checked only by INV-LIVE, which matches known patterns. Candidate INV-LIVE extension for a later tooling pass: future-conditional phrasing ("if closed", "may supply") inside closed modules.

## Superseded, with content preservation
`RTG_NUMBER_GENESIS_DSN_v1_20_3.md` now carries a SUPERSEDED banner (file hash `eeb6f8dfd1d15a4ae22b0f3454f6a1757614b1af0db77452bca131fa29561fdb`); **with the banner removed its content hashes to the frozen `c3265a3a12974e300789179298a732cec579ccfad98b587755e018bcc5cfd2df`**. The v1.20.3 freeze verifier was upgraded to **v1.2** (`34241347d48ef950bb1b2c99036c8df56cc263cee10dd2f102f6d50279106677`) *before* the banner was applied, so that it strips a banner from the owner as well as from the base and proves the remaining content hashes; it still returns FREEZE CONDITIONS MET.

## Chain
v1.20 → v1.20.1 (STOP-01) → v1.20.2 (STOP-02/03) → v1.20.3 (structural migration) → **v1.20.4 FROZEN** (STOP-04 + editorial/governance).

## Next
1. **Consumer sync** — RECOG v0.3.1 repin of `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` (pinned to v1.15); Dyadic v6.4.10 consumer row "acceptance pending". Neither depends on the 19 grade decisions.
2. **v1.20.5 grade normalization** — row-by-row ruling on `NG_V1205_GRADE_NORMALIZATION_TABLE_DRAFT_v1` (a review queue, not yet a decision table); DISC-1/DISC-2 grade by separate ruling.
3. **C7C-M2** — interface-typed WD-DOM preregistration.
