# RRF v0.8.4 — Separate Adoption and Release Record

- **Decision:** ADOPTED, 20 October 2026, only as the RRF working representation standard.
- **Published file:** `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4.md`; **108,615 bytes**; SHA-256 `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce`.
- **Adopted predecessor:** `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3.md`; **97,717 bytes**; SHA-256 `b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187`. Unmodified.
- **Reviewer-approved revised candidate:** `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_REVISED_REVIEW_CANDIDATE.md`; **107,629 bytes**; SHA-256 `fc53acff20c17e152884bc1835d4de2d4354a406f4d63262cdb04c200e2cab9e`.
- **Review diff A:** `RTG_RRF_v0_8_3_ADOPTED_to_v0_8_4_REVISED_REVIEW_CANDIDATE.diff`; 36,647 bytes; SHA-256 `e4b666fadd181551428b1407c6df2edd45f583887c8ae2d8be378a83ef433385`. Independently reviewed as adopted v0.8.3 → revised candidate.
- **Review diff B:** `RTG_RRF_v0_8_4_FIRST_to_REVISED.diff`; 32,839 bytes; SHA-256 `ada2a00b48c141e817cd2d26420c7f55a70fddc5e3ca84830d2047f79f620783`. First candidate → revised candidate.
- **Publication diff:** `RTG_RRF_v0_8_4_REVISED_CANDIDATE_to_ADOPTED.diff`; SHA-256 `e8eb5193a71fc573f4003cad1052c6b0b2cbe15290c584b06ac0a14c973403ce`.
- **Complete predecessor → adopted diff:** `RTG_RRF_v0_8_3_ADOPTED_to_v0_8_4_ADOPTED.diff`; SHA-256 `bcb8c9b5721ea4fbeb22f1be88d9578f193e1555f56ef8f7f7e414817321a967`.

## Approval and scope

The reviewer independently verified candidate byte identity, both review diffs, control-character absence, live B-∞ status correction, W3 owner scope, N-O10-3 label, source pins, the class-C non-profile character, and preservation of historical receipts. The reviewer explicitly authorized adoption as-is; two optional suggestions do not block adoption.

This release implements editorial/publication metadata and a separate new adoption boundary only. It does **not** modify the reviewed scientific assertions, update any scientific owner DSN, introduce a native representation, select physical node exchange/carrier/clock, or close RRF OPEN-A/B/E.

## Owner/source boundaries

DYAD v6.4.18 `DYAD-THM-SMOOTH-EMBEDDING` establishes local C∞ mathematical existence (OPEN 20 B-∞ CLOSED); B-an/B-6 analytic existence remains OPEN. RECOG v0.3.21 W3 requires the same cohomology space; different-space transport remains an explicitly OPEN additional RRF interface. OFN v0.10 class-C and Genesis v2.8.9 Q6 are conditional model contracts, not registered physical profiles. RER r4.10 receiver status is outside this release.

## Deferred non-blocking editorial suggestions

1. In §6.2a, cite DYAD v6.4.13 §6.17 / `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` alongside DYAD v6.4.18 E4 where F3's exactly λ-equivariant chart implication is used.
2. In §2.4b, replace the older generic 'unknown existence outcomes' wording with the specifically OPEN analytic B-an/B-6 outcomes at the next maintenance window. The current-state override already explicitly closes B-∞ smooth existence.

No scientific certificate or new simulation was run for publication. Byte/diff and structural checks are recorded in the separate release QA.
