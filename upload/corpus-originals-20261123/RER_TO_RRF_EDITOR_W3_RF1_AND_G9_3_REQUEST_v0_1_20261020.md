# RER → RRF editor: request on W3 (RF-1) and the G9/3 section pin

**Date:** 20 October 2026
**From:** Claude, RER co-owner and editor (preparer), for the RER registry
**To:** RRF editor
**Copy:** Mustafa (PI); RER receiving co-owner
**Status:** NONCANONICAL request memo. It asks two questions and makes no scientific decision. It amends no RRF, RECOG or RER text.

---

## 1. Why we are writing

RER-G9 is a gap entry of the RER v0.2 DRAFT (current draft r4.9, `9c0f43fc…cc84`). It cites the RECOG CELL-F4 interface conditions W1–W5 and the RRF §6.3 table that restates them. In the per-reference audit of G9, two rows stay open, and only the RRF editor can settle them:

- **G9/1** (RECOG v0.3.20 §6.16g, `RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS`). The receiving co-owner has marked it `SCOPE_CLARIFICATION_PENDING`, because RECOG's W3 and RRF's W3 are not worded with the same obligation.
- **G9/3** (RRF v0.8 §6.3, lines 350–365, SHA-256 `c4ec1f10da0cdf3b95a84b3013909e04db49212e0119b858c170e5fd8f42b44a`). It is still open, because neither RER side holds the v0.8 bytes. The byte identity of v0.8 §6.3 with v0.8.3 §6.3 is therefore not checked.

RECOG has already sent RRF the same W3 question as its outbound notice RF-1 (RECOG v0.3.21 §7.2). This memo does not duplicate RF-1. It asks that RER receive the answer too, because RER-G9 depends on it.

## 2. The texts, verbatim

All three quotations come from byte-verified files. The quotation packet `RER_G9_W3_QUOTE_PACKET_r1.zip` (`74d3a8ca502eae4f0c770cf7d973010dbc758f6af916022a6f8da4098ef879ba`) carries the files, the extraction script and span hashes. The receiver accepted it on 20 Oct 2026 for source identity and reproducibility.

**RECOG v0.3.21 §6.16g, W3** (byte-identical in v0.3.20; RECOG `a3459522…0ae3`):

> **(W3)** event-indexed cochains $a^-$, $a^+$ in the **same** cohomology space, so that $\Delta[a]=[a^+]-[a^-]$ is defined;

**RRF v0.8.3 §6.3, W3 row** (RRF v0.8.3 `b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187`, line 422):

> | **W3** | comparison/transport between *pre- and post-birth* cohomology spaces before forming `\Delta[a]` |

**RECOG v0.3.21 §7.2, notice RF-1:**

> RF-1 — RRF v0.8.3 §6.3 restates W3 as comparison or transport between pre- and post-birth cohomology spaces, whereas §6.16g W3 requires $a^-$, $a^+$ in the same space; RRF is asked to quote W3 verbatim or to label its version an extension carrying an explicit map between the spaces as an additional obligation.

For transparency, RER's own G9 wording (RER r4.9, line 130) is "W3 a shared pre/post comparison space". The receiver found that it points in the right direction but is not precise enough on its own. RER will revise it after your answer.

## 3. What we ask

### Q-W3 (RF-1): which reading does RRF §6.3 intend?

Please state one of the two options. Both are taken from RF-1.

| Option | What RRF would state | Consequence for RER-G9 |
|---|---|---|
| **(a) Verbatim** | §6.3 W3 is RECOG's condition: $a^-$ and $a^+$ lie in the **same** cohomology space, and $\Delta[a]=[a^+]-[a^-]$ is formed there. | RER aligns its G9 wording to the owner text and audits G9/1 against it. |
| **(b) Extension** | §6.3 W3 deliberately allows pre- and post-birth classes in **different** spaces. It is then an RRF extension of RECOG's W3, carrying an explicit comparison/transport map as an extra obligation. | RER records an RRF extension next to the owner condition and does not read it as RECOG's W3. |

If (b), please also state, so that the obligation is checkable:
1. the type of the map (e.g. a homomorphism of cohomology groups, a chain map, a transport along a specified path);
2. its domain and target, i.e. the pre-birth space and the post-birth space;
3. the common space in which $\Delta[a]$ is then formed;
4. whether the map is part of the missing interface (still to be supplied, like W1–W2) or is already registered somewhere in RRF.

RER cannot choose between (a) and (b) on RRF's behalf. Your answer is also the input the receiver named for G9/1.

### Q-v0.8: identity of the G9/3 section

RER-G9 reference n=3 is pinned to RRF v0.8 §6.3. An RER overlay line (r4.6, carried in r4.9) states that "RRF v0.8.3 §6.3 is byte-identical with v0.8 §6.3". It rests on your earlier Q2 disposition (SAME-SCOPE, owner-first; RRF editor response v0.2, `413a869b…3084`). We keep that disposition as separate evidence. A byte claim, however, needs bytes. Please provide **one** of:

1. the original file `RTG_RRF_REPRESENTATION_REGISTRY_v0_8.md` (expected SHA-256 `c4ec1f10da0cdf3b95a84b3013909e04db49212e0119b858c170e5fd8f42b44a`); or
2. a byte comparison you ran yourself: the SHA-256 of the v0.8 §6.3 block, cut by the rule below, against our value for v0.8.3.

**Cut rule:** from the line starting `### 6.3 ` up to, not including, the line starting `### 6.4 `, with lines joined by `\n`.

| File | Block lines | Block SHA-256 |
|---|---|---|
| RRF v0.8.3 (`b393657e…a187`) | 412–427 | `588f37a0adcacd1a3150846a98e067a12713c63f59c4657712ab34c3191105a3` (1 905 bytes) |
| RRF v0.8 (`c4ec1f10…2b44a`) | 350–365 (per the RER pin) | — please supply — |

If the blocks differ (for instance only in the RECOG version label in the import line), please say which lines differ. SAME-SCOPE can still hold without byte identity, but RER would then correct the overlay wording.

## 4. What does not change while we wait

- **RER r4.9:** stays a DRAFT. No RER grade, pin or OPEN status changes because of this memo.
- **Rows G9/1 and G9/3:** stay `PENDING_PER_REFERENCE_AUDIT` in the RER Phase A registry (r15, accepted).
- **RRF083 in Phase A:** now `BYTE_VERIFIED_HERE`. This verifies the RRF v0.8.3 file only, not the W3 interface.
- **No inference from this memo:** none about RRF's scientific content, and no adoption, freeze or publication.

## 5. Reply format (suggested)

A short note with:
- **Q-W3:** `(a)` or `(b)`, with the items 1–4 above if (b);
- **Q-v0.8:** the file, or the block hash, or "differs at lines …";
- whether RRF intends a text revision of §6.3, and in which version.

We will record your answer as RRF-editor input in the G9 per-reference audit. Each resulting RER change will be a separate, receiver-reviewed draft.

---

*Prepared by the RER preparer; the RER receiving co-owner decides on any resulting RER change.*
