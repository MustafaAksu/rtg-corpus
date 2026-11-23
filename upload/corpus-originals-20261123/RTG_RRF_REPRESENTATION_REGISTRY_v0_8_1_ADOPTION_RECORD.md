# RRF v0.8.1 — scoped working-standard adoption and release record

**Date:** 16 October 2026  
**Record type:** Administrative RRF working-standard adoption; **not** a scientific owner theorem, certificate, Programme/PI adoption or physical-model selection  
**Decision:** **ADOPT** `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_1.md` as successor RRF working representation standard  
**Supersedes:** adopted `RTG_RRF_REPRESENTATION_REGISTRY_v0_8.md` only at RRF working-reference scope  
**Review authorization:** User's 16 October 2026 adopted-v0.8 diff and provenance review: revised v0.8.1 candidate **fit for adoption**, subject to release-header correction; optional §8 G1 disclaimer accepted as non-substantive  
**Publication editor:** ChatGPT (RRF working thread)  
**Scientific owner statuses:** Unchanged

## 1. Artifact identities

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Predecessor adopted v0.8 | 75580 | `c4ec1f10da0cdf3b95a84b3013909e04db49212e0119b858c170e5fd8f42b44a` |
| Reviewed revised candidate | 79859 | `c658fe540c6c5aa3f8125a8c623e2962093297ecd8a59b091557cb02f0d1f65f` |
| **Adopted v0.8.1** | **80889** | **`1ba4713855a59b51cad8d79f88007380dfe2364f1b638478a927eea68f642c4c`** |
| Separate noncanonical RER proposal | 3847 | `65186f393985ed502512c875601891cec999830abc2cc7db2fe01dd94f554e86` |

The predecessor, candidate and proposal bytes were confirmed before release and **were not modified**. The full candidate→adopted and adopted v0.8→adopted v0.8.1 diffs are separate reproducible files.

## 2. Reviewer-accepted v0.8.1 content

- **Methodology §4.3 provenance:** §4.2a imports `RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY` from RECOG v0.3.20 §6.6a as its primary scientific owner source. OFN v0.9 IMP-O09-03 remains a consumer cross-reference, not the owner of the result. RECOG's freeze-candidate source status is not promoted.
- **§2.3 rank typing:** source pin is adopted OFN v0.9 §4.4 `RTG-OFN-DEF-RANK-TYPING`; import grammar is `[import: DOC vX §…; RID: …]`, without an unescaped pipe in a Markdown table cell.
- **§6.4 RER plan:** former optional RER-taxonomy text lives verbatim in `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md`; the registry retains a single non-normative, `SOURCE PENDING` pointer. Original RER v0.2 and Stage-2 validation are not claimed to have been inspected.
- **Formal G1 pointer:** reported formal `\widehat S_{\rm form}` is distinguished from exact finite-normalizer `S_h`; only the degree-six jet coincidence under a shared normalizer convention is recorded. The source-pending formal uniqueness report is **not** an adopted owner theorem and implies neither convergence nor physical pole relabeling.
- **§6.2 identity/action:** node exchange and edge-slot exchange are distinguished; analytic versus smooth carrier and physical-clock selection remain OPEN.
- **§3.1 Triadic CN-05:** convention-only same-vector relations are recorded; the conditional birth-amplitude conversion is a future consumer obligation, **not** an applied physical birth law.

## 3. Release-only editorial operations

1. Retain **one** `supersedes:` field naming adopted v0.8; remove the redundant `review candidate supersedes if adopted` field. Update the header's status, scope, editor and adoption-record pointer to the final release.
2. Rewrite the **current** v0.8.1 review-candidate status paragraphs in §0.2, §9 and the separate §10.1 review-stage overlay as an adopted working-standard release. The adopted **v0.8** §9 historical line and §10 **14 October 2026** publication paragraph are unchanged, as are the v0.7 history and older baseline receipts.
3. Add §8.12, at the reviewer's suggestion, repeating the **already-existing** formal-G1 nonclaim in one place. No new scientific result or proof status is introduced.

## 4. Explicit non-adoptions and unresolved interfaces

- RRF's four dyad profiles and provisional `RRF-NET-W-RAW` remain as specified; no new physical carrier, incidence, network field, coefficient, birth law or event mechanism is chosen.
- **OPEN-A/B/E1/E2, RECOG R1, OFN 3B/3C, G2, G2-PRE, analytical Problem B, physical clock and carrier regularity** remain OPEN at their owner-defined scopes. The separately accepted noncanonical `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW_v0_2_1.md` is **not** imported as newly adopted science by this release.
- RER closure taxonomy, age-family and N=7/8 Stage-2 claims stay non-normative/source-pending; no global numerical certification is asserted.
- RECOG/DYAD/OFN/Triadic/NUMGEN owner texts, Programme and Methodology are **not edited**; consumer repinning is deferred to their editors.

## 5. Evidence and QA scope

All SHA-256 and byte identities were calculated on the mounted files. Release validation checks the version/supersession metadata, targeted import grammar, the G1 disclaimer, §9/§10 predecessor historical retention, RER proposal identity and unchanged input hashes. This is an **editorial and structural validation**, not an independent symbolic/numerical rerun or scientific referee report. Details: `RTG_RRF_v0_8_1_ADOPTION_QA.json`.
