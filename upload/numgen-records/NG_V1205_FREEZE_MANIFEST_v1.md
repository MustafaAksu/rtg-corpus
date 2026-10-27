# Number Genesis v1.20.5 — Freeze Manifest

**Manifest ID:** `NG_V1205_FREEZE_MANIFEST_v1` · **Date:** 2026-09-29
**Ruling:** PI — **v1.20.5 FROZEN.** Class: consumer-sync patch; no scientific change.

## Canonical freeze pin
```
351384dc99001f476f1da8a9ce781fee6d1faffd14ba953e280d393795f3d34c  RTG_NUMBER_GENESIS_DSN_v1_20_5.md                  FROZEN OWNER (3263 lines, LF)
73e331aac7e4d5c2dd82779a065b983145d8992804ccf7dc71d78bd70c2d8ec3  RTG_NUMBER_GENESIS_DSN_v1_20_5_fingerprint_v2.json  generator v2.3 (1fbeb19d…3ff6); 495 blocks, dup 0/0
46a741cceca2c36d011f6702f55ecc16f0da2cea093cdbeaf59bda01325c7100  RTG_NUMBER_GENESIS_v1_20_4_to_v1_20_5.diff          5 hunks
```

## Verified delta v1.20.4 → v1.20.5
495 → 495 claim blocks: 3 replacements (status summary; §6.2 explicit-domain block, Dyadic-sync wording; §9 P3 registry row, whose block body carries the edited RECOG and RRF rows), **0 new blocks**. Identifier sets unchanged. 23 combined `[from: …/…]` lines (19 grade-decision rows + 4 §9.2 mirrors) and 29 status lines identical and in order. INV-LIVE 0 hits. Queue, §8, and v1.20.4-and-earlier changelog byte-identical.

## Consumer state recorded
- **RECOG v0.3.5** repinned to Number Genesis v1.20.4 and imports `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`; heuristic-grade cross-reference to GAP-LOCK Lemma 3. Residual v1.15 pins inside RECOG are RECOG's own records.
- **Dyadic v6.4.10** consumer rows ("acceptance pending") — left to the Dyadic stream's own owner pass; not edited from Number Genesis.
- **RRF** working-methodology reference → v0.6 (noncanonical, candidate for PI adoption).
- Stale Number Genesis pins in other owners (Programme Overview v1.2 → v1.18; OFN v0.8 → v1.19; RRF v0.6 → v1.18) are for those owners' next passes.

## Superseded, with content preservation
`RTG_NUMBER_GENESIS_DSN_v1_20_4.md` carries a SUPERSEDED banner (file hash `0c04da16145c9cf5a47e477b75de66deb842319db63763a6495cababc0eeb380`); **content without the banner hashes to the frozen `5559169a10e0b04ddfaa7d8d9e4a5b886809dcaabee648f0a4c5a6a1d27eed8b`**.

## Chain
v1.20 → v1.20.1 (STOP-01) → v1.20.2 (STOP-02/03) → v1.20.3 (structural migration) → v1.20.4 (STOP-04 + editorial) → **v1.20.5 FROZEN** (consumer sync).

## Next
1. **v1.20.6 grade normalization** — row-by-row ruling on the draft table (file still named `NG_V1205_GRADE_NORMALIZATION_TABLE_DRAFT_v1.md` from before the renumbering; a review queue, not a decision table). DISC-1/DISC-2 grade by separate ruling.
2. **C7C-M2** — interface-typed WD-DOM preregistration.
