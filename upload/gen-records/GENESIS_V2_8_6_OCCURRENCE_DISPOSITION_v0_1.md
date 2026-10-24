# Genesis v2.8.6 DRAFT — Occurrence Disposition v0.1

**Date:** 16 October 2026 · **State:** draft companion; no adoption.
**Baseline:** adopted v2.8.5 `41ed76602c1c87c42972ac5b3f0a53f6973ac484427473ac371c57db1ab475cf` (line numbers below are baseline lines).
**Control:** manifest v0.1 `5cdc4ee6…259e` + owner decisions D1–D4 (16 Oct 2026).
**Build:** `build_v2_8_6_draft.py` applies 28 exact-once edits; `check_v2_8_6_draft.py` proves that reversing them recovers v2.8.5 byte-exactly (M1d). Every change is therefore listed below; there is no other change.

## 1. Edit-by-edit disposition

| ID | v2.8.5 line | Package | Change | Claim effect |
|---|---|---|---|---|
| H1 | 1 | mech | title → v2.8.6_DRAFT | none |
| H2 | 4–5 | mech | date; status DRAFT, not adopted, adopted owner stays v2.8.5 | none |
| H3 | 7 | mech | supersedes (on adoption) adds v2.8.5 | none |
| H4 | 8 | mech/D2 | companions: OFN v0.8→v0.9, Dyadic v6.4.10→v6.4.11 | none |
| H5 | 11 | G-B01 | status-summary sentence: K3 no-go + sync, with explicit non-selection | summary of §6.3a |
| N1a | 29 | G-B02 | `GEN-DEF-PRIMITIVE-MAP` recorded as alias of `DYAD-DEF-PRIMITIVE-MAP`; GEN RID kept | none (custody note) |
| N1b | 624 | G-B02 | §6.1 boxed T cross-referenced to the alias; no third RID | none |
| K1 | 51 | G-B01 | §1 one-paragraph `[THM]` summary | new claim (authorized) |
| SG15 | 559 | G-B01 | new SG-15 planar-factor scope guard (document-internal ID, D4) | guard |
| HR | 610 | G-B01 | §5 high-risk row (valid form / forbidden overclaims) | guard |
| K63a | 718 | G-B01 | new §6.3a: `[DEF]` model; `[THM]` statement and proof (a)–(e); `[ALG]` reading; `[DEF]` evidence; `[OPEN]` scope; `[INTERP]` contrast | new claim (authorized) |
| N2a | 570 | G-B03 | §4 routing: μ₆, τ → C21; frame, v⊥ → bridge contract; antisymmetric channel → Genesis-native (D3) | none |
| N2b | 640 | G-B03 | §6.2 eigenframe: source pointer to contract item 1 | none |
| NF6a | 653 | G-B03 | `DYAD-ALG-NF6` cited at the h-chart use | none |
| NF6b | 685 | G-B03 | `DYAD-ALG-NF6` cited at the h-chart use | none |
| N2c | 956 | G-B02/03 | §7 line split: `DYAD-DEF-PRIMITIVE-MAP`; `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` (frame, v⊥); `DYAD-ALG-PROTECTION-MATRIX`; `DYAD-ALG-NF6`; repin note; `DYAD-ALG-LIEGAUGE-NORM` no longer imported | none (source attribution) |
| P211 | 211 | mech | P0-DYADIC repin note → v6.4.11 | none |
| P276 | 276 | mech | OPEN 9 primary-ledger pointer → v6.4.11 | none |
| P662 | 662 | mech | OPEN 9 imports pointer → v6.4.11 (Lie-gauge tag on c_θ⁽⁶⁾ kept) | none |
| P951 | 951 | mech | §7 Dyadic header → v6.4.11 | none |
| P993/P994 | 993–994 | mech | OPEN 16/17 continuity pointers → v6.4.11 | none |
| P1024 | 1024 | mech | §8 P0-DYADIC import → v6.4.11 (`DYAD-CAND-P0-DYADIC`, conditional) | none |
| P989 | 989 | D2 | OFN context pointer → v0.9 (context-only, no import) | none |
| EXP | 1004 | G-B04 | §7 export line for RRF G2-CLOCK, exact §6.3a scope, no physical selection | export statement |
| ART | 1040 | G-B05 | §8 RID entry with full provenance hashes | registry |
| APPA | 1055 | log | Appendix A v2.8.6 draft entry | history |
| FOOT | 1383 | mech | footer: draft identity prepended; inherited footer kept | none |

**Not edited, by design:** lines 1066 and 1331 (version history keeps v6.4.10 and historical wording); line 148 OPEN 1A candidate #2 (archival-chart scope already correct); 9B/9C, GCL-01–11 dispositions, and all Triadic import rows.

## 2. Gate results (executed here)

`check_v2_8_6_draft.py`: **18/18 executed gates PASS; 1 SKIP (M6c needs the OFN file locally).**
- **M1a–d:** baseline/Dyadic hashes; deterministic rebuild; reverse-edit recovery.
- **S3a–c:** no tag removed; tags added only in authorized edits; whole-document deltas +6 THM, +3 DEF, +2 NUM, +1 ALG/OPEN/INTERP, no COR/RETRACTED.
- **M2a–b:** 12 DYAD RIDs; 8 cited values verbatim in v6.4.11.
- **M3–M6b, S1a–b, S2, S4.**

Two negative controls:
- A tampered draft with one undeclared word deletion exits 1 at M1c/M1d.
- A build that turns SG-15 into "excludes a physical node exchange" exits 1 at S2.

**M2c — owner item, not changed here.** The ν₅⁽⁵⁾ closed form in §6.2 is attributed to the Dyadic primary ledger. Dyadic v6.4.11 (and v6.4.10) prints only "exact over ℚ(√5, √(10+2√5))". This provenance gap predates the draft and is recorded in queue v0.4 §12.

**M6 — OFN scope preservation.**
- Genesis cites OFN only as context. There is no OFN scientific import, before or after.
- OFN v0.9 (adopted 13 Oct 2026) imports from Genesis v2.8.5 §6.1/§1:
  - IMP-O08-01 zero-origin/first-dyad;
  - IMP-O08-10 `GEN-DEF-PRIMITIVE-METRIC`;
  - IMP-O08-11 `GEN-THM-PRIMITIVE-METRIC-INVARIANCE`;
  - IMP-O08-13 `GEN-THM-LIN-ORDER6`.
- None of these blocks is altered by the draft. §6.1 receives only an alias annotation on the T definition. The OFN consumer pins therefore remain valid on adoption.
- OFN CUST-O09-01 / REQ-O09-04 is answered by edit N1a.

## 3. Outbound notices on adoption (not sent by the draft)

| To | Notice |
|---|---|
| Dyadic | N1 recognized (alias recorded); N2 repin applied; NF6 cited at the two h-chart uses. Draft pinned to adopted v6.4.11; the project's v6.4.12 DRAFT r1 is not used. |
| OFN | CUST-O09-01 / REQ-O09-04 answered by the Genesis alias record; v0.9 Genesis imports unaffected. |
| RRF | G2-CLOCK may cite `GEN-THM-K3-PLANAR-FACTOR-NOGO` at §6.3a scope; no admissibility condition selected by Genesis. |
| Triadic | Same N2 repin is pending on the Triadic side (Dyadic notice N2 names both); Genesis does not edit Triadic. |

## 4. Remaining before adoption

1. Independent receiving review of the draft bytes and this disposition.
2. Local run with `--ofn` (closes M6c) and `--k3`.
3. Owner adoption decision. New RIDs become citable only then.
