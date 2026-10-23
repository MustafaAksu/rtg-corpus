# RECOG G2 — Genesis, OFN and RRF Claim-Level Audit Record v0.1

**Date:** 20 October 2026
**Status:** `[SESSION]` audit record for review; it precedes any v0.3.21 edit specification.
- No DSN is edited, and RECOG v0.3.20 (FROZEN) remains authoritative.
- Nothing is imported into RECOG by this record.
- The verdicts are proposed. They become final on the reviewer's acceptance.

**Method.** Same verdict vocabulary as the Dyadic audit (U / S / CS / CST / N / ID).
- The comparison runs on the exact pinned and current files.
- Tool: `recog_g2_section_diff.py` v0.1.1, sha256 `aade4354…04d9`. It compares **whole sections** or whole OPEN entries where the import is a section or entry, and anchored blocks where the import is a single statement.
- Comparison is exact on the selected lines.
- Line ranges are printed for both files.
- Controls run in session: a self-comparison returns exit 0; a missing file returns exit 2.
- CLAIM_EQUIVALENT is the reviewer's verdict, field by field.

## 0. Inputs (hashes recomputed in session)

| File | Lines | SHA-256 | Reference identity | Match |
|---|---|---|---|---|
| Genesis v2.8.4 (pinned) | 1,237 | `c145f5d2a3e30fafcd9603132761cc1039f7f33e2a9da56ce1e7cafe2032cebd` | **none recorded in RECOG**; identity rests on the PI's provenance | — (recorded here) |
| Genesis v2.8.9 (current) | 1,649 | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` | Genesis v2.8.9 release record | **yes** |
| OFN v0.8 (pinned) | 1,205 | `56bc991d28c4a6f3e841eec5ac8c4550528fbaac91bcfc23ab0dc2540bd2a514` | RECOG §7.1 pin | **yes** |
| OFN v0.10 (current) | 1,660 | `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa` | OFN v0.10 release record | **yes** |
| RRF v0.6 (pinned, §7 Registry row) | 270 | `7a31357729e1561c600673cf673c785b645666ae65d8280ebbaf9b57722d6b89` | RECOG §7 pin | **yes** |
| RRF v0.8.3 (current) | 563 | `b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187` | the file Dyadic v6.4.14–17 records as inspected | **yes** |

**RRF v0.4 (convention-only row) was not supplied.**
- The row's conventions (profile names, observable typing, S_h, common-realisation condition, network guard) are all present in v0.6, which supersedes v0.4/v0.5 with a recorded change log. They are audited v0.6 → v0.8.3 here.
- The v0.4 → v0.6 step is not byte-verified. It is a convention-only citation with no scientific import, so nothing load-bearing depends on it.

Reports (attached):

| Report | SHA-256 |
|---|---|
| `g2_genesis_v2_8_4_vs_v2_8_9.txt` | `a6009802…8da6` |
| `g2_ofn_v0_8_vs_v0_10.txt` | `8ba10469…b1cb` |
| `g2_rrf_v0_6_vs_v0_8_3.txt` | `3af3fffd…6742` |

---

## A. Genesis (pinned v2.8.4 → current v2.8.9)

RECOG §7 Genesis rows: §6.1 (O₀ = 0, first dyad, B, Q = rᵀBr, AᵀBA = B `[THM]`); §6.6 (I_ab, ω_ab, J_Q, aᵀBJ_Qb = (√3/2)ω_ab, plateau phase memory).

| # | Import | RECOG points of use | Comparison (pinned → current lines) | Field-by-field | Verdict | RECOG consequence |
|---|---|---|---|---|---|---|
| GA1 | O₀ = 0; first dyad 0 → (A,B), A + B = 0 `[DEF]` | §5 (distinction anchoring), §6.5 | IDENTICAL (L549/551 → L636/638) | — | **U** | none |
| GA2 | B, Q(r) = rᵀBr `[DEF]` | §1 comparator construction, §6.1 | DIFFERS only by the inserted RID tag `GEN-DEF-PRIMITIVE-METRIC` (L562 → L649) | statement, matrix, formula, grade identical | **ID** | the §7 row may cite the RID |
| GA3 | AᵀBA = B `[THM]` | §1 RECOG-ALG-INVARIANT-FORM, §6.1 | DIFFERS only by the inserted RID tag `GEN-THM-PRIMITIVE-METRIC-INVARIANCE` (L564 → L651) | identical, `[THM]` | **ID** | the §7 row may cite the RID |
| GA4 | I_ab = √(Q_aQ_b) cos θ_ab; (√3/2)ω_ab = √(Q_aQ_b) sin θ_ab `[DEF]` | §1, §6.1 | IDENTICAL (L676 → L958) | — | **U** | none |
| GA5 | plateau shear bridge Φ_ab(∞) = Φ_ab(0) − τ log(q_a/q_b) `[ALG structure]` | §1, §6.8, §6.12 (leading plateau surrogate) | IDENTICAL (L686–688 → L968–970) | — | **U** | none |
| GA6 | J_Q = (1/√3)[[1,−2],[2,−1]], aᵀBJ_Qb = (√3/2)ω_ab, J_Q² = −I | §1, §6.1, SG-R9 | IDENTICAL (L692–694 → L974–976) | — | **U** | none |
| GA7 | J_Q convention (index order; ±J_Q branch) | §7 J_Q row ("sign branch fixed by convention; load-bearing properties branch-independent") | **DIFFERS** (L696 → L978) | old: "no downstream result depends on this sign … load-bearing properties branch-independent"; new: branch-independence only "for calculations in which the orientation convention is transported consistently"; it "does **not** erase sign-sensitive fixed-policy statements" (GCL-01) | **CS** (owner scope narrowed) | **Wording only.** RECOG's comparator orientation is sign-carrying and already declared (SG-R9: C→ carries the conjugate orientation; sign-carrying quantities state the orientation). The §7 row phrase "load-bearing properties branch-independent" should be restated with the owner's narrowed scope: metric identities are branch-independent under consistent orientation transport; RECOG's sign-carrying comparator statements carry their declared orientation. No RECOG claim changes. |

The whole-section runs (§6.1: L547–565 → L634–652; §6.6: L674–706 → L956–988) differ only at:
- **GA2, GA3, GA7** above;
- **the dyad generator line**, which gains the alias note "(same formula as GEN-DEF-PRIMITIVE-MAP = alias of DYAD-DEF-PRIMITIVE-MAP)" (ID);
- **two §6.6 paragraphs RECOG does not import**:
  - the birth-symmetry channel wording (D_birth versus Q(V_s));
  - the saturation-ceiling window.

  Both are recorded as not used.

**New upstream (N), not imported:** §6.3a–§6.3c (K3 factor no-gos, mean-feedback family, GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO). These bear on OFN/RER, not on any RECOG claim.

---

## B. OFN (pinned v0.8 → current v0.10)

RECOG uses OFN in two directions.
- **Exports:** §6.2a rows as export targets for R5/§6.4; §7.3 as SG-R5 context.
- **Responses received:** R1 / OPEN-OFN-OPA.

| # | Item | Comparison | Field-by-field | Verdict | RECOG consequence |
|---|---|---|---|---|---|
| OB1 | §6.2a radial row (export target of §6.4 / R1) | DIFFERS (section L428–441 → L542–570) | "symmetry/minimality premises not selected" → "its radial-row premises do not select full-map covariance" | **CS** (clarified; consistent with RECOG §6.4 conditional sine lemma) | export-target wording update |
| OB2 | §6.2a phase-shear row (export target of R5) | DIFFERS | one row split into three rows, **P1 composition / P2 weight magnitude / P3 orientation**, and OFN now imports RECOG-ALG-SHEAR-COCYCLE-CLASSIFICATION, -WEIGHT-IDENTIFICATION and -ORIENTATION-CONJUGACY at their scopes | restructured upstream, **consistent with R5 P1–P3** | **Fulfils RECOG's v0.3.17–v0.3.20 notices.** The R5 export target now points to the three rows. No RECOG claim changes. |
| OB3 | §6.2a "pole exchange" row (v0.8) | removed as a separate row; its question now sits in P3 and OPEN-OPA | — | restructured | R1's dependency line points to P3 / OPEN-OPA |
| OB4 | §6.2a "birth and memory" row | rewritten to cite RF-O09-02 (RECOG token/retention inventory) | the "independent retention not mandatory" wording is OFN's own | restructured | none; RF-O09-02 is a consumer citation of RECOG |
| OB5 | §7.3 Antipodal Band and Width Parameter (SG-R5 context) | **IDENTICAL** (whole section, L495–512 → L633–650) | — | **U** | none |
| OB6 | OPEN-OFN-OPA (R1's home for physical orientation) | DIFFERS (whole entry, L749–760 → L908–928): four paragraphs **added**; status line **unchanged** | additions:<br>(i) the orientation conjugacy is family conjugacy, not a symmetry of fixed T₁;<br>(ii) RRF OPEN-A's nonlinear S_h is a different candidate action;<br>(iii) the passive/distinct-role dichotomy is exhaustive only for the isolated-dyad question; G1-P1 composition stays open;<br>(iv) class-C reconciliation (Lemma F / F3) and a Finding A cross-reference | **CS** (owner question sharpened; status unchanged) | Consistent with RECOG v0.3.20 R1/R5-P3. Point (ii) is relevant to the later A2 cell (typed involution ledger). Nothing is imported in v0.3.21. |

**Consumer direction (OFN v0.10 imports RECOG v0.3.20).** For §7.2:
- **IMP rows:** IMP-O08-17/18/19 (as restated in v0.10) and IMP-O09-01/02/03.
- **RF rows:** RF-O09-01/02.
- **Source citations in §6.3–6.4** of: RECOG-ALG-SHEAR-COCYCLE-CLASSIFICATION, -WEIGHT-IDENTIFICATION, -ORIENTATION-CONJUGACY, -SWAP-SPLIT, -SELECTION-SIN, and RECOG-DEF-POLE/STATE-COMPARATOR.
- **REQ-O09-02** is fulfilled by the G1 freeze record.

**New upstream (N), not imported:** §5.5 (Q1–Q6, Standard C, class C, OPEN-OFN-TRIAD-CLASS). This bears on the later A4 cell.

---

## C. RRF (pinned v0.6 → current v0.8.3)

RECOG §7 RRF v0.6 row: the OPEN-B → E1 → E2 lock; RRF-NET-W-RAW; the open `T-net` bridge; multiplicative realization unregistered. The v0.4 convention row covers the S_h typing, the common-realisation condition, comparator typing and the network guard.

| # | Item | Comparison | Field-by-field | Verdict | RECOG consequence |
|---|---|---|---|---|---|
| RC1 | RRF-NET-W-RAW profile, incl. "multiplicative edges not registered" | **IDENTICAL** (whole §2.5, L139–155 → L225–241) | — | **U** | none |
| RC2 | `T-net` bridge `[OPEN] [scope: bridge]` | T-net row **identical**; the transport table differs only in the `T-h` row | T-h constraint cell: "single-dyad only; closure not transported" → "single-dyad only; **network** closure not **silently** transported; predicates/sections require full pullback on admissible transitions (§4.3)" | **U** for T-net; **CS** (clarification) for T-h, consistent with RECOG F2(a) | none |
| RC3 | dependency lock OPEN-B → E1 → E2 | the lock text is identical; §6 gains subsections §6.1–§6.4 (L227–234 → L375–431) | new: §6.1 (alignment ≠ composition domain), §6.2 RRF-CND-01 (proposed interface), §6.3 token/history/network inheritance (RECOG CELL-F4 W1–W5 recorded), §6.4 RER proposal (non-normative) | **U** (lock); **N** (subsections) | see finding RF-1 |
| RC4 | not-registered list (multiplicative realization) | **IDENTICAL** (whole §7) | — | **U** | none |
| RC5 | S_h (exact involution; J_≤6 commutation; covariance defect (3/2)t³) | §2.3 differs | covariance row restated as "general two-input identities are algebraic consequences of s₂" with the same O(3) statements and the same real-ray witness; guard re-pinned OFN v0.8 → OFN v0.9 RTG-OFN-DEF-RANK-TYPING | **U** (content); ID (re-pin) | none |
| RC6 | common-realisation condition | §2.4 differs | status "proposed RRF convention" → "RRF working convention"; text identical. §2.4 also adds the R9 observable row (consumer citation) and the formal-involution receipt (R₀; DYAD v6.4.12) | **CS** (convention status firmer); **N** (rows) | none; RECOG uses the convention as written |
| RC7 | comparator typing (C_z versus C_W^{(h)}; covariance belongs to the (observable, action) pair) | §4.1 differs | the citation moves from RECOG v0.3.1 OPEN R11 to RECOG v0.3.14 §6.14 (R11 CLOSED); the "covariance belongs to the pair" sentence is upgraded from `[HEUR → OPEN R11]` to the closed-ledger statement; §4.1a imports R9 (RECOG v0.3.14) | **U** (content); consumer citations of RECOG | notice: repin to RECOG v0.3.20 (content unchanged) |
| RC8 | pole-relabeling actions | §4.2 differs | additions: the DYAD formal-involution receipt (R₀ equals S_h only through the degree-6 jet), the N9 note (J, F1/F2), and a "generator-family limit on OPEN-A" paragraph citing RECOG-THM-TWIN-RADIAL-ACCESS (v0.3.14); §4.2a records orientation conjugacy ≠ physical pole exchange | **U** (table); **N** (additions) | the R₀ / S_h statement is the owner-cited form the later A2 cell must use |

**Finding RF-1 (paraphrase drift, notice to RRF).** RRF v0.8.3 §6.3 restates RECOG's W3 as "comparison/transport between *pre- and post-birth* cohomology spaces before forming Δ[a]".
- RECOG §6.16g W3 requires event-indexed cochains a⁻, a⁺ **in the same cohomology space**, so that Δ[a] is defined.
- The two coincide only if the transport is itself registered. RRF's wording admits a transport that RECOG's W3 does not supply.
- Proposed notice: RRF should either quote RECOG's W3 verbatim or mark its version as an RRF extension that requires a registered transport.
- No RECOG change.

**Stale consumer pins (notice to RRF).**
- §0.2 receipt table, §4.1, §4.1a, §4.2 and §4.3 cite RECOG **v0.3.14** for R9, R11, B-token transport and twin radial access.
- §4.2a and §6.3 cite **v0.3.20**.
- The cited content is unchanged since the respective RECOG releases. Repin to the frozen v0.3.20 (G1) or to v0.3.21 when issued.

---

## D. Consolidated results

| Owner | Rows | U | ID | CS | CST | Notes |
|---|---|---|---|---|---|---|
| Genesis | 7 | 4 | 2 | 1 (GA7 J_Q convention) | 0 | GA7 needs a §7 wording change, no claim change |
| OFN | 6 | 1 | 0 | 2 (OB1, OB6) | 0 | OB2–OB4 restructured upstream, consistent with RECOG and fulfilling its notices |
| RRF | 8 | 7 (content) | 1 | 2 (RC2 T-h, RC6) | 0 | RF-1 paraphrase drift; stale v0.3.14 pins |

**Proposed conclusion.** No Genesis, OFN or RRF item that RECOG relies on changed its statement, hypotheses, domain, constants or grade. One owner scope was narrowed (Genesis J_Q branch independence, GA7), and RECOG already satisfies the narrower scope through SG-R9.

## E. Wording items for the v0.3.21 edit specification

1. **§7 Genesis rows:** pin v2.8.9; cite GEN-DEF-PRIMITIVE-METRIC and GEN-THM-PRIMITIVE-METRIC-INVARIANCE; restate the J_Q row with the narrowed branch-independence scope (GA7).
2. **§7 OFN row and R1/R5:** pin v0.10; export targets become the radial row and the P1/P2/P3 rows; R1 records the v0.10 OPEN-OFN-OPA additions as received, with no import.
3. **§7 RRF row:** pin v0.8.3 (convention / registry reference only); add RF-1 and the stale-pin notice to G3.
4. **§7.2 dependents:** add the OFN v0.10 IMP/RF rows and the RRF v0.8.3 RECOG citations (§0.2, §4.1, §4.1a, §4.2, §4.2a, §4.3, §6.3).
5. **No READ/WRITE/DECODE vocabulary; no status changes.**
