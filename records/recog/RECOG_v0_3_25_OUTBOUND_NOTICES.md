# RECOG v0.3.25 — Outbound notices (prepared texts; routed through the PI)

**Date:** 27 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` notice record, v0.1. Release: `recog-v0.3.25`, merge commit `bdb3712397da146d75cef8f7d2999838a0620a0e`, DSN SHA-256 `86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db`; release record `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md`. Per CONVENTIONS.md §7 each notice carries four separate states per recipient (sent, received, statement accepted, adopted use); **no state is recorded here before a real dispatch**. Pending consumer decisions do not block the release (Methodology v1.4 §13.5).

| # | Recipient | Kind | State |
|---|---|---|---|
| N1 | Dyadic | request (registration) | prepared |
| N2 | Dyadic | request (registration) | prepared |
| N3 | Dyadic | informational | prepared |
| N4 | NUMGEN | informational | prepared |
| N5 | OFN, RRF, RER (consumers of RECOG RIDs) | informational | prepared |
| N6 | Atlas | row update | prepared |

## N1 — Dyadic: (D5) row-A bridge proof constants (request)

RECOG v0.3.25 (`86cae8ff…d7db`) uses, under `[assuming:]`, two constants and one decomposition that appear in the **proof** of DYAD-THM-LPHASE-ROWA-REMAINDER at `dyad-v6.4.22` (`2363ca40…8c29`) and are certified by DYAD-ART-LPHASE-ROWA, but are not owner theorem rows: $|D_Q|\le c_Qq^{3/2}$ with $c_Q=0.79246$; $|D_Q-D_3|\le c'_Qq^2$ with $c'_Q=0.36915$ ($D_3=2\operatorname{Re}(\bar zh_2)$); and the decomposition $r=\Lambda_3+{\rm rest}$ with its constants ($\tfrac{123}{125}$, $c_J=0.50220$, $c_7=157.58$). Consequential RECOG uses: RECOG-ALG-A1C-TAIL-HARMONICS, RECOG-THM-A1C-SHARPENED-SCHEDULE (§6.13b), RECOG-ALG-A1C-START-OFFSET (ii), RECOG-ALG-A1C-ADMISSIBLE-REGION, RECOG-ALG-A1C-JOINT-CONTRACTOR (§6.16e); §7 LPHASE row. **Request:** register these as owner statements (a theorem row or a named certified-constant row) so that the RECOG blocks can drop the `[assuming:]`; or state that they are to remain proof-level. No change to Dyadic's grades or domains is implied; RECOG does not widen any Dyadic certified domain.

## N2 — Dyadic: $C_7$ certificate values as ceilings (request)

RECOG-THM-R9-SHARPENED-ROWS-C7 (§6.13a) takes Dyadic's published DYAD-THM-NF-REM certificate values $85.07$ (row $|z|\le\tfrac1{20}$) and $27.60$ (row $|z|\le\tfrac1{40}$), rounded up to $85.1$ and $27.7$, as $C_7$ ceilings under `[assuming:]`, giving $(C_2,q_{\max})=(221.4,\tfrac1{400})$ and $(75.69,\tfrac1{1600})$ with incompleteness windows $3.456\times10^{-5}$ and $1.011\times10^{-4}$. The unconditional rows RECOG-THM-R9-SHARPENED-ROWS use the adopted $C_7=100/30$. **Request:** register $C_7\le85.1$ / $27.7$ (or the Arb upper bounds) as ceilings, or state that the theorem ceilings $100/30$ are to remain the only owner statement. The adopted RECOG rows $(517,\tfrac1{400})$, $(163,\tfrac1{1600})$ remain valid and in force; rows are not mixed.

## N3 — Dyadic: informational

(i) RECOG-ALG-R9-SUM-LEMMA: from the one-orbit bound $q_m\le q_0/(1+\tfrac12q_0m)$ alone, $\sum_{m\ge0}q_m^3\le(1+q_0)q_0^2$ (essentially sharp); it sharpens Dyadic's own $\sum_mq_m^3\le2q_0^2$ and Dyadic may adopt it; the R9 term $C_2(\tfrac{256}{225})^2Q_0^2$ in Dyadic's OPEN 21 constants would shrink accordingly if Dyadic imports the new rows. (ii) RECOG-ALG-A1C-COMBINED-TAIL uses the owner's decomposition of the block remainder $r_m$ as an exact identity under branch (B): the bridge terms $\tau D_Q$ cancel in $\tau(Q_m-\tfrac1{a+m})-r_m$ and the angular increments telescope, so the two RECOG tails are one boundary term $D_\Theta(z_M)$. (iii) New RECOG uses of adopted Dyadic rows are recorded in RECOG §7 (NF-REM, NF-INV, PRIM-CTR, LPHASE row A, NF6). No Dyadic RID is renamed, regraded or re-scoped by RECOG.

## N4 — NUMGEN: informational

The explicit-$U$ slip law (RECOG-THM-A1B-SLIP-SCHEDULE-U, v0.3.24) now carries a known-$a$ / declared-data error majorant $E'''(a,M_k,r_k)=O_a((1+\log(a+M_k))/(a+M_k))$ (RECOG-THM-A1C-SHARPENED-SCHEDULE, conditional on the Dyadic (D5) constants) and, with $a$ unknown, a record-only certified outer enclosure of the admissible $(a,L,a-b,\Theta_0)$ from a finite prefix (RECOG-ALG-A1C-JOINT-CONTRACTOR; windows, not identification; no uniqueness). Custody of GAP-LOCK Lemmas 1–3 and INF-1 is unchanged; NUMGEN's adopted domain and grades are untouched; nothing is imported from NUMGEN v1.21 yet (RECOG's §7 pin stays `numgen-v1.20.8` until a separate repin audit).

## N5 — OFN, RRF, RER: informational

New RECOG RIDs (16): RECOG-ALG-R9-SUM-LEMMA, RECOG-THM-R9-SHARPENED-ROWS, RECOG-THM-R9-SHARPENED-ROWS-C7, RECOG-ART-R9-SHARPENED-ROWS; RECOG-ALG-A1C-TAIL-HARMONICS, -INBLOCK-ANGLE, -COMBINED-TAIL, RECOG-THM-A1C-SHARPENED-SCHEDULE, RECOG-ART-A1C-SHARPENED-SCHEDULE; RECOG-ALG-A1C-ADMISSIBLE-REGION, -START-OFFSET, -JOINT-CONTRACTOR, RECOG-ART-A1C-DECODER; RECOG-ALG-A1C-THRESHOLD-CODING, RECOG-ALG-A1C-PHASE-C1-FIBER, RECOG-ART-A1C-Q1PRIME-FIBER. Where a consumer cites the R9 comparator-incompleteness window $q_0<|G|/C_2$: the adopted rows remain valid; additive sharpened rows give windows $2.952\times10^{-5}$ / $9.390\times10^{-5}$ unconditionally and $3.456\times10^{-5}$ / $1.011\times10^{-4}$ under the $C_7$ `[assuming:]`. No RECOG RID a consumer imports has been renamed, regraded or re-scoped. SG-R6 unchanged: nothing in v0.3.25 defines an event, a token-write mechanism or a carrier; the $R_{\rm ind}$ classification of R9's carrier is unchanged; A1c-Q1′ stays OPEN.

## N6 — Atlas: row update

New RIDs as in N5 with their sections (§6.13a; §6.13b; §6.16e); OPEN R6 sub-item A1c-decoder answered in bounded form (✓: outer windows on $U$, two usable slips, (D5) `[assuming:]`), sub-item A1c-Q1′ reworded and still `[OPEN]`; §5 event-rule row: the decoder guard; §7: new uses on the NF-REM, NF-INV, PRIM-CTR and LPHASE rows; §8: four new artifact rows. The B1 Stage-C targets, the logarithmic chart drift and the in-block $c_P(r)$ at $r\ge3$ are research levers, not open obligations of the DSN.
