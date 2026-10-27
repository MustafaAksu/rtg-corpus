# Number Genesis v1.20.1 — Freeze Manifest

**Manifest ID:** `NG_V1201_FREEZE_MANIFEST_v1` · **Date:** 2026-09-25
**Ruling:** co-owner, 2026-09-25 — **v1.20.1 DSN freeze GO.** v1.20.1 is the FROZEN owner baseline. No further scientific edit to this file. v1.20.2 (methodology-only migration) is HOLD.

## Canonical bundle
```
00174c3a51edea6c2a76d4b8d8e6f1d25da8723faba5df91ba7bda662f9c927b  RTG_NUMBER_GENESIS_DSN_v1_20_1.md                    FROZEN OWNER BASELINE (3198 lines, LF)
668ff285a397d9b143ca4386f7c1c42834f8e906f90e8a6078613a17ea92c232  RTG_NUMBER_GENESIS_v1_20_to_v1_20_1.diff             (+8 / -3)
c4b51f454abac32f708019c704b5aa26be8ba3446c4f42e6ba46083fa809fdd3  RTG_NUMBER_GENESIS_DSN_v1_20_1_fingerprint_v2.json   migration baseline fingerprint
574d331998775fe58e6a318d312878eb609916a4c42668f6c8124fd146c2f2e0  ng_state_fingerprint_v2_1.py                          GENERATOR of the fingerprint above (v2.1)
036c36de6be340b6fdc9375cdc8f66f366cc5d0bb75bbc124567b79995cf51d1  NG_V1201_RECONCILIATION_REVIEW_v1_1.md                (companion pointer corrected)
9666c89c2b6136733a645168cfcb63a9d061d999300017a46d9262d6f987bc7b  NG_V1201_RECONCILIATION_REVIEW_v1_1.json
```

## Generator binding
The fingerprint file is named `…_fingerprint_v2.json` because the output filename convention was fixed in the v2 script; it was **produced by v2.1** (`574d3319…f2e0`), which differs from v2 only in excluding the literal `RID` placeholder from the explicit set. Any future comparison must use this exact generator hash.

## Superseded, with content preservation
- `RTG_NUMBER_GENESIS_DSN_v1_20.md` — superseded scientifically **only** by the v1.20.1 sync patch. The mounted file carries a supersession banner, so its file hash is now `07dc5d88697a5feb1518b0b952fc9bc5b5b13ca993c0b49556d7a2550d9d8a38`; **with the banner removed, its content hashes to the original frozen `f5ed40f5adcf2835c6aceee7025a1daa299d97c679e895efb4fc84f54773b636`** — the base freeze is intact.
- `NG_V1201_RECONCILIATION_REVIEW_v1.md` / `.json` — superseded by v1.1.

## Verified delta v1.20 → v1.20.1
Fingerprint v2.1: 493 → 494 claim blocks; exactly **1** baseline block lost (stale D15 sentence) and **2** added (its correction; the v1.20.1 changelog `[COR]`). Explicit RIDs 38 = 38. Broad identifiers: one addition, `STOP-01`. §2↔§6 duplicates: 0. Independently reproduced by the co-owner.

## State
v1.20 FROZEN (superseded by sync patch only) · **v1.20.1 FROZEN owner baseline** · v1.20.2 methodology migration HOLD pending: 119-block reverse relocation inventory, INV-S, INV-P.
