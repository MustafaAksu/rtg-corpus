# RER Phase A r4 — independent receiving review

**Date:** 19 October 2026  
**Status:** SESSION receiving review; no owner adoption, freeze or publication.  
**Receiving decision:** **ACCEPT SCOPED — Phase A r4 mechanical/currency-metadata delta**. A3-CUR-01 and A3-STATUS-02 are resolved *at their declared register scope*. The RER r4.6 source draft stays DRAFT; 20/20 record science remains to be dispositioned in Phase B. Original legacy-source byte authentication, individual scientific acceptance, and relevant source evidence remain separate gates.

## 1. Exact inspected identities and execution

- Input ZIP `RER_PHASEA_R4_PACKAGE_20261019.zip`: SHA-256 **`f6b9e3d08d61fc3034af7295c2066bebf02cdf02d60d0fb69fe9d90fa90da738`**.
- Its `SHA256SUMS.txt`: **44/44 PASS**, independently calculated over the extracted archived files *before* builder execution. The subsequent builder execution did not change any listed hash.
- Embedded source `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2_DRAFT_r4_6.md`: SHA-256 **`2fa878ffa32c0d4d725f53f17b86b9a43d5161f16a7adce9686cb374063a4772`**.
- `build_phaseA.py` and `check_phaseA.py --tamper` executed after a fresh ZIP extraction: **20/20 PASS; 16/16 negative controls rejected as required**. Post-build SHA-256 hashes agree with original archive manifest. These are locally re-executed developer gates, not independent proofs of the 20 scientific records.
- Embedded and separately supplied `RER_PHASE_A_R4_CHANGE_RECORD_20261019.md`: identical bytes.
- Compared directly with independently retained Phase A r3 ZIP (`c433c0e7e17ed683c51d23ec85d1ecb3e9dc11d8a7921b7aa90da347876f13f8`). The **r4.6 Markdown, `catalog_records.json`, parser and all 20 record objects are byte-/structurally unchanged**; generated registry JSON differs at the top-level *schema version* only (PHASEA/3 → PHASEA/4). Currency matrix rows changed in exactly 14 places: 1 Dyadic record row and 13 gap rows. Other expected changes: current-owner catalog, watch text, source manifests, builder/checker and blocked register.
- Independent reference text/link-target extraction: **13/13 gap reference paths non-null and matching**.

## 2. Current-owner update and independently verified Dyadic scope

- Owner file DYAD v6.4.16 (`/mnt/data/RTG_DYADIC_OSCILLATOR_DSN_v6_4_16.md`) SHA-256 independently calculated: **`33c14c5cc27625c17a2b78be74e070ae61b5c7399ded49a1538098735ab559e0`**. Owner status in that file: ADOPTED (19 October).
- The cited v6.4.13 bytes available in the prior receiving corpus have SHA-256 **`5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542`**. **DYAD §§6.15, 6.16, 6.17 are each independently byte-identical from v6.4.13 to v6.4.16** (direct section extraction; no reliance solely on the preparer's assertions). Pin retention on v6.4.13 is justified for the examined involution/centralizer content.
- DYAD v6.4.16 closes OPEN 3 within its defined scope, introduces OPEN 21, and does **not** close OPEN 20 (per owner §§1–2 and history). These lifecycle changes are not automatically imported as new RER scientific content.
- Genesis v2.8.9 file SHA independently calculated: **`d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc`**. Its new `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` is a separately scoped §6.3c result; its effect on GEN-K3-MODAL/G6 remains an explicit Phase B evaluation task.
- The A19 owner currency gate checks against a **frozen, versioned source catalog** (`inputs/owner_versions_known.json`), not a live global release service. RECOG v0.3.20 is a **freeze candidate** in its own header, not proof of adopted/frozen status. The catalog is a known-versions ledger, not owner-adoption certification.

## 3. The 13 gap references: independent current-use triage

RER r4.6 gap references explicitly point to historical RRF v0.8 source paths (ten cases), one historical ER-2B v0.1 path, and two current RECOG v0.3.20 paths. Directly read adopted RRF v0.8.3 (SHA-256 `b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187`) and RECOG v0.3.20 (SHA-256 `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df`). **RRF v0.8 and ER-2B v0.1 exact bytes are not included in this package or presently independently inspected.** Reported SAME-SCOPE/binary section comparisons from the RRF editor are attributed to the editor, not presented as local reproduction.

| Gap/reference | Independent finding | Remaining evidence/decision boundary |
|---|---|---|
| G7 / 0 — RRF v0.8 §6.2 | **Changed current scope.** r4.6 G7 overlay correctly requires full-state node exchange, full update, intertwining, witness and regularity/clock/domain. RRF v0.8.3 §6.2 and editor Q1/Q6 agree. | Historical v0.8 exact source bytes not independently replayed; physical realization remains OPEN. |
| G7 / 1 — RRF v0.8 §0.2 | History/source-receipt pointer; retained as historical and not silently repinned as a current scientific theorem. | v0.8 original bytes unavailable; §0.2 is not certified SAME-SCOPE. |
| G8 / 0 — ER-2B v0.1 C15 | Historical noncanonical mathematical context, passively transported model distinguished from newly re-imposed closure. | Exact v0.1 file missing; source verification **BLOCKED**. ER-2B adopted grade not inferred. |
| G8 / 1 — RRF v0.8 §0.3 | Same current representation scope; r4.6 G8 correctly distinguishes passive change from a new conditional model. Editor Q1 reports byte-identity of the v0.8/v0.8.3 section. | Exact old-byte equality is **editor-reported**, not locally replayed. |
| G8 / 2 — RRF v0.8 §6.2 | Changed current scope; G8 refers physical coincidence applications to G7's contract. | As G7/0. |
| G9 / 0 — RECOG v0.3.20 §6.6a | **DIRECT FULL-FILE SHA PASS; lines 517–542 checked**; `RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY` present. RER correctly names RECOG scientific owner. | RECOG owner header says freeze candidate; no additional adoption asserted. |
| G9 / 1 — RECOG v0.3.20 §6.16g | **DIRECT FULL-FILE SHA PASS; lines 1002–1042 checked**; `RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS` present. Network W1–W5 requirements scoped. | No resulting physical network realization asserted. |
| G9 / 2 — RRF v0.8 §4.2a | Current RRF v0.8.3 §4.2a confirms cross-model conjugacy ≠ physical exchange; owner first remains RECOG, OFN only downstream. | Historical pin bytes remain unavailable; editor Q2 says SAME-SCOPE. |
| G9 / 3 — RRF v0.8 §6.3 | Current RRF v0.8.3 §6.3 is an inheritance/interface prerequisite, not a new history carrier. | Editor Q2 reports SAME-SCOPE, local old-byte identity not replayed. |
| G10 / 0 — RRF v0.8 header | Historical adoption/working-standard boundary; current adopted working standard is v0.8.3. | v0.8 original bytes unavailable. |
| G10 / 1 — RRF v0.8 §6.4 | **Changed source location.** Current RRF v0.8.3 §6.4 is a nonnormative pointer; r4.6 points to separate closure proposal with reported hash `65186f393985ed502512c875601891cec999830abc2cc7db2fe01dd94f554e86`. | Separate proposal original bytes and historical v0.8 bytes not independently inspected; no normative promotion. |
| G10 / 2 — RRF v0.8 §8.1 | Historical nonclaim/adoption guard consistent with current v0.8.3 §8.1; owner does not adopt RER results. | Historical v0.8 exact bytes unavailable. |
| G10 / 3 — RRF v0.8 §10.1 | Historical source-inventory/authentication pointer; not treated as a current 2026-10-19 evidence receipt. | Historical v0.8 exact bytes unavailable. |

**Per-reference conclusion:** 13/13 references received a **current-use triage**, not 13/13 original-source byte certification. **2 direct primary-reference owner-file validations (RECOG)**, **10 RRF legacy pointers reconciled by the RRF editor's scoped disposition and current RRF v0.8.3**, and **1 ER-2B primary pointer still blocked**. Editorial Q1–Q8 response is complete; source/evidence authentication and Phase B per-record proof acceptance are distinct. The generated Phase A r4 `PENDING_PER_REFERENCE_AUDIT` field is left unchanged; this SESSION triage is not silently installed as a status promotion.

## 4. Disposition and next gate

- **A3-CUR-01 CLOSED at the declared machine-ledger/current-source level.** Owner v6.4.16 registered, v6.4.15 negative control rejects, §6.15–§6.17 verified unchanged from v6.4.13.
- **A3-STATUS-02 CLOSED at the declared schema level.** `interface_questions=EDITOR_DISPOSITION_RECEIVED` and `gap_reference_review=PENDING_PER_REFERENCE_AUDIT` separate completed editor answer from remaining per-reference evidence; the old `phaseC_disposition` rejected.
- **Phase A r4 ACCEPT SCOPED** as a mechanically verified candidate. Phase B can proceed with 13 deep, 5 receipt/claim-scope and 2 ER-2B blocked entries. The two Triadic author-conflict records require an independent recipient disposition. No PI authorization for RER adoption or release follows.
- Remaining scientific/source dependencies: ER-2B original primary archive and coincident audit ZIP, byte verification for absent historical v0.8/ER-2B v0.1 if literal source-pin closure is required, targeted GEN v2.8.9 §6.3c relevance, and Phase B record-level reviews. A1 installation, G6/degree-seven graph and regional/global Stage-2 certificates remain separate OPEN work.

**No scientific grade, contract, owner status, source Markdown, installed machine registry, or canonical DSN was modified by this receiver review.**
