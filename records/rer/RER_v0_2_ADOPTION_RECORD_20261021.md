# RTG — Relational Emergence Registry v0.2 — adoption record (21 October 2026)

**Decision authority.** PI (Mustafa Aksu) — explicit adoption-scope decision of 21 October 2026, taken on the exact bytes identified below after the receiving co-owner's L1 finalization acceptance. **Prepared by** the RER preparer (Claude, RER co-owner; PREPARER_ROLE) as the record of that decision; the preparer accepts nothing here.

**Status of the adopted object.** NONCANONICAL working registry (Methodology v1.3 §0.5 supplement class) — ADOPTED at registry scope. Not an owner DSN adoption, not a freeze, not a publication.

## 1. Adopted object

| Object | SHA-256 |
|---|---|
| **`RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2.md`** (ADOPTED; metadata-only release) | `58feee5ff1f16a37fc4ee029f24499928ea7439731de0a090d8794c1cbe57ad0` |
| Release basis: DRAFT r4.14-L1 (receiver L1 finalization ACCEPTED) | `032f2211229ab55d6f5f2477f19b75bb29c55a32d7574682be514b18ae0070d3` |
| Phase A r21-L1 (machine image of r4.14-L1; ACCEPT SCOPED) | package `076fd118820996513d4367de001a58b6a2bf7c4e4dace5db0b90cdff984ed274` |
| Phase A release pin (same catalog, adoption fields filled from this record) | `RER_phaseA_v0_2_RELEASE.zip` — identity in the release package README |

The release changes **four header lines** of r4.14-L1 (title, Date, Document status, Supersedes); every line from **Scope** on — all 20 records, 4 gap entries, 23 reference lines, §§1–9 — is byte-identical (release gate R2). The record-level phrase "Registry/owner adoption: pending" is the preserved pre-adoption text and is read through the header and this record.

## 2. Adoption scope (the PI's decision)

**Adopted as scoped, reviewed scientific payloads — 18 records**, each at its stated scope, grade and declared limits:

RER-GEN-C01, C02, C03 (B-02; HARM not received), C04 (B-03; HARM, ANGLE_DATA not received), C05 (B-03; RANKDATA not received), C06, C07 (receiver did not complete the twelve-basis replay), C08, C09 (B-03); RER-TRIAD-FORMAL-AGE (B-06 + r4.11 correction; `[ALG]` formal, source grade); RER-TRIAD-AGE-CURVATURE (B-08); RER-TRIAD-REGULAR-3FOLD (B-04); RER-F3-N7N8 (B-08 + r4.13 correction; `[ALG]` FINITE_ORDER; regional/global Stage-2 certificate **OPEN**, GLOBAL_CERTIFICATE_PENDING); RER-RRF-CND01 (B-06; general theorem accepted, physical application unproven); RER-GEN-K3-MODAL (owner imports; E-conjugacy transport step ACCEPT SCOPED `[ALG]`, batch review 21 Oct); RER-DYAD-FORMAL-INVOLUTION (B-05/B-06; owner import, owner proof packages not re-audited); RER-TRIAD-FORMAL-INVOLUTION (B-07; (ii)(b) on the prior receiver certificate, not fully replayed); RER-TRIAD-BIRTH-GRAPH-INVOLUTION (B-07; (d) conditional on the explicit child contract).

**Retained in the registry but excluded from scientific acceptance — 2 records:** RER-ER2B-T6D and RER-ER2B-CARRIER, status BLOCKED_SOURCE_UNVERIFIED (ER-2B v0.2 study and evidence ZIP not inspected; NOT_FOUND_IN_SEARCHED_SNAPSHOT, receiver search 21 Oct 2026). Their mathematical payload is neither accepted nor rejected by this adoption.

**Source and reference limits adopted as stated (not waived):** the 12 historical RRF v0.8 pins are HISTORICAL_PIN_SOURCE_UNVERIFIED (original bytes not recovered); the 12 current RRF v0.8.4 references are ACCEPT SCOPED (ER2B-CARRIER context-only; G10 §6.4 pointer-only — the closure-proposal file `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md` is not held); the three held pins G8/0, G9/0, G9/1 AUDITED_AT_PIN; G2 §5b CARRIER_IDENTIFICATION_PENDING; RECOG v0.3.20 pins frozen; Dyadic v6.4.13 / RRF v0.8.2 pins RECHECK_IN_PHASE_B (sections changed in later editions, as recorded). Source-currency matrix at adoption: 103 rows — 43 VERIFIED / 2 OWNER_REPORTED / 52 HISTORICAL / 6 BLOCKED; authentication 74 / 4 / 24 / 1.

## 3. What this adoption does not do

It does not re-adopt or re-certify any owner theorem (Genesis, Dyadic, Triadic, RECOG, RRF, OFN); it does not make RRF normative or adopt the RER closure taxonomy into RRF; it selects no physical carrier, node-exchange realization or clock; it certifies nothing globally (the Stage-2 regional/global certificate and multi-step error control remain OPEN); it does not close G6, all-order graph completion, G2 carrier identification or physical realization; it does not authenticate the missing archives. The registry may be revised later under the Fast-Track rule (L1 changes accumulate; L2 changes need receiving review).

## 4. Review chain (receipts, hashed in the release package)

Phase B receiving decisions B-01 … B-08 and the r4.7 follow-up (19–21 Oct); Phase A r14–r21 and r21-L1 receiving decisions; owner section checks r1/r2; Fast-Track decision (21 Oct); batch receiving review (`bd80f89d…`, scientific/source delta ACCEPT SCOPED, K3 ACCEPT SCOPED `[ALG]`, 18 + 2 coverage); L1 receiving review (`822615825fccf0e3…`, L1 FINALIZATION ACCEPTED — exact object ready for the separate PI adoption-scope decision). Reference dispositions sidecar `3536c207…b78d`.

## 5. Release integrity (gates, `check_release.py`)

R1 basis hash; R2 body identity (lines from Scope on byte-identical to r4.14-L1; exactly lines 1, 4, 7, 8 differ); R3 parser identity (all 20 records, gap entries, references, source table, legacy entries identical); R4 header content (ADOPTED, scope 18 + 2 named, basis hash, "does not" clauses, pre-adoption phrase note); R5 deterministic rebuild and reversibility; R6 line-initial tag counts unchanged; R7 adoption record pinned and consistent (hashes, 18 + 2 lists equal the registry's record set). Negative controls: a body line edited; a record dropped; scope list altered; status line without the exclusion clause.

**PI signature of the decision:** this record is written at the PI's instruction of 21 October 2026 ("Adopt: 18 + 2 scope"). Any later change of scope is a new PI decision.
