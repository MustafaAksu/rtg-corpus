# RECOG — A1a-G1 disposition addendum: final NUMGEN reply received

**Date:** 20 October 2026 · **Recorded by:** RECOG owner (Claude, co-owner; PI Mustafa)
**Status:** `[SESSION]` addendum to `RECOG_A1A_G1_DISPOSITION_RECORD_20261020.md` (`0e5f91c0dabbd34bb8261ddd6e0a34361be4dbaaa9b3545b0f98fc14e3e971a7`). That record is not edited, and no RID is registered here.

## 1. Received

| Record | SHA-256 | Note |
|---|---|---|
| `NUMGEN_REPLY_TO_RECOG_A1A_RID_REQUEST_20261020_v0_1_1.md` | `a2e7bf98fe08d2d64a883b8996c285ba4b67c94f73bb53548abe206f228b1902` | final for dispatch; handed into the RECOG conversation by the PI on 20 Oct 2026 |
| predecessor v0.1 (draft) | `184a74fcede666c9427d0f959ed94b15c4206435b371b7d69b438a7254265227` | already recorded |

## 2. Check against v0.1

A line diff shows that v0.1.1 differs from v0.1 only on line 1 (the title gains "— v0.1.1") and line 4 (the status line). Lines 8 to the end (§§1–5) are byte-identical. This satisfies the co-owner's condition that the header is updated and the body is not changed.

The new status line states:
- the reply is final for dispatch;
- the co-owner ruled on 20 Oct 2026 and approved all six strings as allocations, with no regrading;
- the strings are canonical only from NUMGEN v1.20.8 and must not be cited before then;
- the module RID and the threshold-ratio RID keep their identities;
- for A1a-G1, the allocation is resolved and the repin waits for v1.20.8.

This matches the disposition record exactly.

*Residual wording:* the §3 heading of the body still reads "(subject to the co-owner ruling)". The heading is historical, the ruling is recorded in the status line, and the body was deliberately left unchanged. No action is needed.

## 3. Effect

- **A1a-G1:** the disposition is unchanged ("allocation resolved; canonical repin pending NUMGEN v1.20.8"). The evidence chain is now complete with an owner-side final record, in addition to the co-owner ruling.
- **RECOG v0.3.22 DRAFT r3** (`8f496d3c…d959`): no text change is required.
  - Its §6.13b and §7 cite the reply as "v0.1 `184a74fc…5227`" together with the co-owner ruling. Both stay true.
  - Its §8 says the final copy is "to be recorded on receipt". This addendum is that record.
  - In the adoption pass, the §8 governance row adds this addendum and the v0.1.1 reply with their hashes. That is a metadata addition at adoption, inside the already reviewed scope.
