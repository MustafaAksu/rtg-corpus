# DYAD v6.4.24 — backlog (preparation record)

**Date:** 3 November 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record. It changes no DSN text, grade or RID, and it decides nothing. It lists what a later maintenance edition may carry. Scope boundary, agreed with the co-owner (3 Nov 2026):
- v6.4.24 carries the accepted interface changes and the S1 result, if S1 is accepted;
- the §1 compaction is deferred to v6.4.25 or later, as an independent editorial edition;
- S2 (L-PHASE row B) and S3 (OPEN 20 stage 3) are separate scientific work. S3 stays not authorized.

Governing edition: `dyad-v6.4.23` (`9f874ccc…25cb`). Line numbers refer to it.

## A. Consumer register (§7.0, §7) — stale rows

| Row | Now | Current state | Source |
|---|---|---|---|
| Triadic Birth-Lift (§7.0 L≈1081; §7 export line) | v1.6.1, "§7.1 repins to Dyadic v6.4.13 (N2 answered)" | Triadic v1.7 (`triad-v1.7`) repins its five Dyadic imports to v6.4.23 (`DYAD-THM-C21`, `DYAD-ALG-BRIDGE-LEMMA`, `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` item 1, `DYAD-ALG-PROTECTION-MATRIX`, `DYAD-DEF-PRIMITIVE-MAP`); Triadic filed no notice to DYAD | `triad-v1.7` §7 (import records) |
| RECOG, NUMGEN, OFN, ATLAS | as in v6.4.23 | update only when the receivers answer the v6.4.23 notices (RECOG re-check with $c'_Q=0.36916$; NUMGEN disambiguation of $q_*$) | `pipes/*/20261030-DYAD-v6-4-23-adopted.md` |
| GEN, DZT, AZ, RRF, RER, ER-2B, OPEN-M | as in v6.4.23 | update when the receivers record the 3 Nov notices | `pipes/*/20261103-DYAD-notices-n16-n21.md` |

## B. RID candidates (Atlas DYAD.X4: results used downstream without an owner RID)

| Statement | Location (v6.4.23) | Grade | Note |
|---|---|---|---|
| The map is not globally area-preserving ($\det DT=1+(e^\rho-1)\cos\eta$) | §1 L63, §6.1 L447 | `[THM]` | cited by OFN (non-symplecticity) |
| $p=6$ linear order ($\lambda=e^{i\pi/3}$ has order exactly six) | §6.6 L543 | `[ALG]` | regraded from THM at v6.4.20 |
| Homological resonance condition ($a-b-1\equiv0\pmod6$) | §6.6 L545 | `[ALG]` | |
| Cubic radial rate across $p$ ($\Re\mu^Z_p=-p\sin^2(\pi/p)$) | §6.6 L549 | `[ALG]` `[import: RECOG-ALG-NU3-CLOSED-FORM]` | custody question: a Dyadic RID for an evaluation of a RECOG result, or a pointer to RECOG's RID only |

Owner decision needed per row: register (name, scope) or record "no RID; cite the section". A new RID is a registration only; it changes no statement.

## C. Science feeding v6.4.24

- **S1 — OPEN 21 with the unconditional sharpened R9 rows** (selected; work item).
  - The co-owner's rational pre-check (3 Nov) uses the existing $K'_j$, $w_j$ and RECOG-THM-R9-SHARPENED-ROWS $(259.2,\tfrac1{400})$, $(81.49,\tfrac1{1600})$. It gives $K_A\approx19.679640\to19.68$ and $K_B\approx6.356467\to6.36$, against $35.32$ and $8.83$ now.
  - Form: a **new, separate result** (new RID). `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` keeps its rows and its `[assuming: RECOG-THM-R9-MEMORY]`.
  - The new result keeps the R9 dependency on the sharpened rows, the chart/primitive separation and every hypothesis. It never uses the -C7 rows.
  - Plan: design note → exact-rational certificate with negative controls → co-owner review → candidate for v6.4.24.

## D. Not in v6.4.24

- §1 compaction (two-stage editorial edition, v6.4.25 or later).
- S2 L-PHASE row B; S3 OPEN 20 stage 3 (not authorized); N=432.
- OPEN 18 footprint `[DEF]`; RAW-CUBIC historical identity (DYAD.X11); source recovery (`DYAD_SOURCE_RECOVERY_LIST.md`).
