# RRF editor: question packet from RER Phase A (v0.2)

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner (preparer).
**Status:** NONCANONICAL. A request for written dispositions. It changes no RRF text and asks for no RRF adoption.
**Supersedes:** packet v0.1 of the same date. v0.1 understated the §6.2 change (Q1) and mislabelled the carrier profile (Q5).

**Objects:**
- RER v0.2 DRAFT r4.5 (`5691e20a…8c19`): the gap entries G7–G10 and the record RER-RRF-CND01. Their RRF text is the same as in r4.4.
- RRF v0.8 (`c4ec1f10…2b44a`): RER's current section pin.
- RRF v0.8.3 (`b393657e…a187`): the adopted working standard.
- Separate RER proposal `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md` (`65186f39…54e86`, 3,847 B).

**How the proposed answers were checked:**
- *RRF side.* Before sending, a check compared each question with the RRF v0.8, v0.8.3 and proposal texts (relayed by the PI, 19 Oct). The line numbers below are from that check. I confirmed the quoted passages against the v0.8.3 text, but did not recount the lines.
- *RER side.* I checked the r4.5 text myself (§D).

Each proposed answer is for the editor to confirm or correct. The editor's written answer is the RRF interface resolution required before release (decision record §IV).

## A. Section pins (v0.8 → v0.8.3)

**Q1. G7, G8 and CND01 cite v0.8 §6.2 (`RRF-CND-01`, lines 333–349). G8 also cites §0.3. Are the v0.8.3 sections acceptable successor pins?**

*Proposed answer:*
- **§0.3: SAME-SCOPE.** It is byte-identical in v0.8 and v0.8.3.
- **§6.2: CHANGED-SCOPE.** Besides the regularity/clock declaration and the DYAD F1 reference, v0.8.1 made three changes:
  1. The Identity/Action contract now requires **node-exchange** equivariance at the selected physical update. Its note reads: "an exchange of edge slots need not be the node permutation".
  2. A new **slot-versus-node guard** was added.
  3. Every submitted realization contract must declare `regularity:` and `clock:`.

  The four-predicate distinction RER relies on is unchanged.

*Consequence for RER, if confirmed:* a pointer repin is not enough.
- CND01's carrier currently reads "complete state X with a fixed-model involution sigma". It must state that σ is the **node exchange on the complete state**, not an edge-slot permutation.
- `Fσ = σF` must be stated for the same full update.
- G7 needs the same qualifier.
- These are scoped revisions, reviewed by the receiving co-owner.

**Q2. G9 cites v0.8 §4.2a and §6.3. Are the v0.8.3 sections acceptable successor pins?**

*Proposed answer:* **SAME-SCOPE, with a pin-order change.**
- §6.3 is byte-identical.
- §4.2a has the same mathematics. Since v0.8.1, its import tag puts the owner RID first: `RECOG v0.3.20 §6.6a; RID: RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY`. OFN v0.9 IMP-O09-03 is only a consumer cross-reference.
- G9 already cites RECOG §6.6a first. On repin it should cite RRF v0.8.3 §4.2a with the same owner-first order.

**Q3. G10 cites v0.8 §6.4 (lines 366–390). Should RER (a) keep the v0.8 pin as history and cite the proposal file, or (b) cite only v0.8.3 §6.4?**

*Proposed answer:* **(a).** v0.8.3 §6.4 itself says: "for candidate closure taxonomy, read the separate proposal, not this working standard".
- Keep the v0.8 pin as history.
- Cite the proposal file by its hash (`65186f39…`) for the closure taxonomy.
- The FORMAL_ONLY passage is preserved verbatim in that file. RER's "interface clarification" line should therefore refer to the proposal file, not to the working standard.

## B. Status of RER relative to RRF

**Q4. Does RER's closure proposal remain non-normative under v0.8.3?**

*Proposed answer:* **YES.**
- §6.4 (line 430): "not a mandatory profile field, owner theorem, numerical certificate or approved physical representation".
- §8.1 (lines 465–466) repeats the same limit.

**Q5. Which RRF carrier profile should RER cite for the formal involution? Is `RRF-NET-W-RAW` used correctly?**

*Proposed answer:* **PARTLY.**
- **Formal involution.** RRF registers the formal involution $R_0$ in the `RRF-DYAD-NF` row ("Formal involution — owner-adopted, formal only") and in §2.4b. The relabeling candidate of `RRF-DYAD-W` is the finite $S_h = h_6(-I)h_6^{-1}$, which equals $R_0$ only through degree six.
  - RER-DYAD-FORMAL-INVOLUTION currently names the carrier "profile RRF-DYAD-W (RRF v0.8.2 §2.3, §2.4b)".
  - Its transformation law already keeps $S_h$ and $R_0$ apart. The label could still blur the finite/formal distinction.
  - **Proposed carrier:** `RRF-DYAD-NF` + §2.4b. W is named only as the coordinate frame in which $R_0 = T^3F^{-1/2}$ is written. DYAD §6.16 states $R_0$ in the raw frame without a normalizer.
  - In r4.5 this label occurs only in RER-DYAD-FORMAL-INVOLUTION (line 856); the Triadic involution records do not cite an RRF-DYAD profile.
- **`RRF-NET-W-RAW`.** Used correctly: it appears only as the provisional network lock, and the `RRF-DYAD-W → RRF-NET-W-RAW` bridge is OPEN (line 49, §2.5, §8.4, §8.1 line 467).

## C. RER-RRF-CND01 ownership split

**Q6. RER attributes the `[THM]` `Fσ = σF ⇒ F(Fix σ) ⊆ Fix σ` to standard mathematics, and the contract structure to RRF v0.8.3 §6.2 as a [DEF] proposed interface. Does RRF agree?**

*Proposed answer:* **YES.** §6.2 (line 393) calls the general exchange-fixed lemma "mathematical source background … not owned here". One condition comes from Q1: σ is the node exchange on the complete state, and `Fσ = σF` holds for the same full update.

**Q7. Does RRF hold the primary bytes of the three coincidence sources?**

*Proposed answer:* **No bytes. Hashes for two of them, plus a related review.** `RTG_RRF_v0_8_CANDIDATE_REVIEW_MANIFEST.json` (14 Oct) records:

| File | SHA-256 | Size |
|---|---|---|
| `RTG_RRF_RESPONSE_TO_OFN_COINCIDENCE_v0_2.md` | `897bfad0…1126d` | 8,809 B |
| `RTG_RRF_COINCIDENCE_ADMISSIBILITY_REVIEW_v0_1.md` | `ef89db5c…72a53` | 5,975 B |
| `RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md` | `ea26d3d1…7b2bb5e` | 50,183 B |

- The ER-2B v0.2 hash agrees with the identity reported independently in ER-2B consolidated v0.3 Part A (`ea26d3d1…b2bb5e`).
- RRF records no hash for `ER2B_COINCIDENCE_SIXSTEP_AUDIT_v0_1.zip`.

*Consequence for RER:*
- With known identities, the bytes can be authenticated as soon as the files are supplied. Until then the witness stays an unauthenticated secondary report.
- The ER-2B records stay blocked (receiver D-2): a matching hash identifies a file; it does not authenticate the v0.2 evidence package.

## D. Q8: does RER understate or overstate RRF v0.8.3?

RRF lines to watch (from the pre-send check), and RER r4.5 as I checked it:

| RRF v0.8.3 | What it says | RER r4.5 |
|---|---|---|
| line 211 | B-∞: only existence is OPEN; flat uniqueness is CLOSED by Lemma F and F1–F3 | **Consistent.** Lines 883–884 separate B-∞ existence (OPEN) from flat uniqueness (CLOSED, existing objects). Gate C2 enforces this. |
| line 213 | The odd chart and the root $Q^2=F$ are equivalent existence questions ([ALG]) | **Consistent.** Line 883 states B-∞ existence once, "equivalently a C^∞ tangent-to-identity square root of F". It is not counted as two OPENs. |
| line 217 | B-6 ⇔ B-an ∧ B-3, hence B-6 ⇒ B-an; no claim that B-6 is strictly stronger | **Consistent.** Lines 27 and 882 state only B-6 ⇒ B-an. |
| line 408 | Exact C^∞ commutation does not identify EF=TE with EF=T⁶E; a physical clock must be declared | **Consistent.** Line 868 keeps the two factor contracts distinct. CND01 does not yet carry the `clock:` / `regularity:` declaration (Q1). |

*Question to the editor:* is any other v0.8.3 statement understated or overstated by RER? A list of line numbers is enough.

## What RER does with the answers

| Answer | RER action |
|---|---|
| Q1 (§0.3), Q2, Q4 confirmed | Pointer repin in the next draft; no grade change |
| Q1 (§6.2), Q5, Q6 confirmed | Scoped revision of CND01, G7 and the carrier label, reviewed by the receiving co-owner |
| Q3 confirmed | G10 cites the proposal file by hash |
| Q7 | RER records the hashes. The witness is authenticated only when the bytes are supplied. |

Nothing in this packet adopts, freezes or publishes RER or RRF.
