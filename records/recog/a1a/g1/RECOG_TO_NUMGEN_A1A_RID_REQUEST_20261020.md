# RECOG → Number Genesis: request for dedicated RIDs for the INF-1 statement and the $D_M$ definition

**Date:** 20 October 2026
**From:** RECOG owner (Claude, co-owner; PI Mustafa)
**To:** Number Genesis owner
**Status:** `[SESSION]` request, **prepared and not yet sent**. The PI dispatches it, and the A1a-G1 record is updated only with real send and reply events. Nothing in NUMGEN is edited, and no RID is assigned or invented here.

**Reason:** DSN Methodology v1.3 §3.3. When an imported claim has no owner RID, the import is written `RID unavailable`. The template records "Owner RID: none in the inspected source; dedicated RID requested". The use is a *declared exception with unresolved identifier governance*. The independent release-readiness review of RECOG A1a cell draft v0.4 (`d195af7a…8445274`, §4) requires this request, or an equivalent recorded governance decision, before a RECOG v0.3.22 release sign-off.

## 1. What RECOG imports without a RID

Source: `RTG_NUMBER_GENESIS_DSN_v1.20.7` (`c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28`), §6.6, N-5A-S1-INF.

| RECOG tracking key | NUMGEN item (quoted) | NUMGEN grade | Owner RID in the inspected source |
|---|---|---|---|
| `A1A-NG-D-DEF` | $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$, with $\hat\phi$ the increasing primitive lift of $\arg W$ | definition | none |
| `A1A-NG-INF1` | INF-1: $D_M=\tau\log M+C_D+o(1)$ (from L-BACKBONE and L-PHASE, on the small punctured tube) | `[RESULT] [from: ALG]` | none |

**Not the same item.** `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` is registered for the defect-threshold consecutive-ratio theorem $M^{(\rm def)}_{k+1}/M^{(\rm def)}_k\to e^{\sqrt3\pi/6}$, which *uses* INF-1. RECOG does not reuse that RID for INF-1. The adopted RECOG v0.3.21 §7 row quotes the INF-1 formula as context under that RID. The v0.3.22 draft adds a scope note there and does not reassign the RID.

**RECOG's use:**
- RECOG v0.3.22 DRAFT r1 §6.13b uses INF-1 as true in two results, both graded `[RESULT] [from: ALG]` and both on $U\cap U_{\rm NUMGEN}$:
  - (a) existence of the asymptotic phase without R9;
  - (b′) agreement of RECOG's $C_D^{\rm ext}$ with NUMGEN's $C_D$.
- Neither changes INF-1 or its domain. In your C4 reply (`8a887ef3…bc4d`) you confirmed that INF-1 is independent of RECOG R9 and is indexed from an arbitrary start.

## 2. Request

Please choose one of the following and record it in a NUMGEN owner record:

1. **Assign dedicated RIDs** to the INF-1 statement and, if you wish, to the $D_M$ definition. RECOG will then repin both imports to them at its next revision. The statements stay unchanged.
2. **Defer or decline**, with a short reason, for example that the identification is an optional refinement and needs no RID now. RECOG will then keep `RID unavailable` with the tracking keys and record your decision as the governance disposition of the exception.

Either answer closes RECOG's release gate A1a-G1. RECOG asks for no other NUMGEN change and makes no import into NUMGEN.

**Alternative open to the PI:** the PI, acting as Methodology steward, may instead record an explicit decision that this deferred request is acceptable for the v0.3.22 release. That decision must name the continuing temporary exception and its responsible owner (NUMGEN). If this alternative is used, this request may still be sent, for information.
