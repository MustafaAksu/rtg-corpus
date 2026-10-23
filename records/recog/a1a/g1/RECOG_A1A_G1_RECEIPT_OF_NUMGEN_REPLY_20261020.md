# RECOG — receipt of the Number Genesis reply to the A1a RID request (gate A1a-G1)

**Date:** 20 October 2026 · **From:** RECOG owner (Claude, co-owner; PI Mustafa)
**Status:** `[SESSION]` receipt. Nothing is adopted, no RECOG or NUMGEN file is edited, and no RID is registered.

**Request:** `RECOG_TO_NUMGEN_A1A_RID_REQUEST_20261020.md` (`a89b69243f24d63f74fed29c9af809f8616017ecdbbd8ef07446ed646e0246a0`), delivered to the NUMGEN owner side through the PI. The NUMGEN reply's §0 says the hash is recorded in NUMGEN's dispatch log.

**Reply:** `NUMGEN_REPLY_TO_RECOG_A1A_RID_REQUEST_20261020_v0_1.md` (`184a74fcede666c9427d0f959ed94b15c4206435b371b7d69b438a7254265227`). The PI handed it into the RECOG conversation on 20 Oct 2026. Its own status line says:
> "DRAFT pending the co-owner ruling on the RID strings (§3). It becomes final once the strings are ruled; the PI then dispatches it."

## 1. What the reply says

| Item | Content | RECOG reading |
|---|---|---|
| Decision | Option 1: dedicated RIDs will be assigned, in NUMGEN maintenance release v1.20.8, with no statement changes | resolves the governance question in principle |
| Ratio-theorem RID | `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` is not INF-1 and must not be reused | agrees with the v0.3.22 §7 scope note |
| Module RID | `NUMGEN-OPEN-N5AS1-INF` is a lifecycle RID; RECOG must not repin to it | agrees with §6.13b |
| Proposed strings | `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`, `NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-L-BACKBONE`, `-L-MONO`, `-L-PHASE`, `NUMGEN-RESULT-N5AS1-INF1` | proposed only; fixed when v1.20.8 is adopted |
| Interim line for RECOG | "Owner RID: dedicated RID decided by the NUMGEN owner (reply of 20 Oct 2026); string to be fixed in NUMGEN v1.20.8; responsible owner NUMGEN." | a governance disposition (option 1, pending edition), not a deferral |

## 2. Disposition of A1a-G1

**State: decision received in draft; not yet final.** Two facts set this state:
- The reply has `DRAFT` status: the RID strings await the NUMGEN co-owner ruling, and after that the PI dispatches the reply.
- The decision itself (option 1) is stated without condition. Only the strings are pending.

Under the request's own terms, a recorded NUMGEN owner decision closes A1a-G1. RECOG will treat the gate as closed when **one** of the following exists:
1. **The final reply**, with its status line no longer `DRAFT`, recorded with its SHA-256. RECOG then records the interim line of §4 of the reply. The strings may still be pending v1.20.8; that is allowed, because the disposition is recorded.
2. **An explicit PI statement**, as NUMGEN co-owner, that the option 1 decision in v0.1 is final even though the strings are not yet ruled.

Until then, RECOG does not mark A1a-G1 closed and does not use any proposed NUMGEN string as an identifier.

## 3. Compatibility check (RECOG side)

- NUMGEN's v1.20.8 will define φ̂ explicitly as the sum of the principal one-step angles under L-MONO. RECOG's $D_M^U$ uses the increasing primitive lift. On $U$, RECOG-THM-A1A-LIFT-ALIGNMENT gives $\tfrac\pi6<\delta_T<\tfrac\pi2$, so each one-step principal angle equals the lift increment. The two definitions therefore agree on $U$, and on $U\cap U_{\rm NUMGEN}$ in particular. No RECOG statement changes.
- RECOG imports only $D_M$ and INF-1. The four further NUMGEN RIDs (lift, L-BACKBONE, L-MONO, L-PHASE) appear in the INF-1 import's `Depends on:` line. Once assigned, they can be cited there at the repin; they are not new RECOG imports.

## 4. Prepared change for the release text (to apply once §2 holds)

This is a metadata change to the v0.3.22 candidate. No mathematics, grade, domain or proposed RECOG RID changes. Replace "dedicated RID request prepared, not yet dispatched; A1a-G1 OPEN" in four places:
- the companion header;
- §6.13b, `D_M` import;
- §7, two NUMGEN rows.

The replacement is:

> "dedicated RID decided by the NUMGEN owner (reply of 20 Oct 2026, `<final SHA-256>`); string to be fixed in NUMGEN v1.20.8; responsible owner NUMGEN; A1a-G1 CLOSED"

Also:
- the §6.13b note "declared exception with unresolved identifier governance … not final closure" becomes "temporary `RID unavailable` until NUMGEN v1.20.8; governance disposition recorded";
- §8 registers the reply and this receipt;
- the repin to the actual strings follows in a later RECOG revision after NUMGEN v1.20.8 is adopted, with tracking keys `A1A-NG-D-DEF` and `A1A-NG-INF1` kept until then.

Whether this goes in as a DRAFT r3 or in the adoption pass is the PI's choice. Either way it needs an exact-delta check.
