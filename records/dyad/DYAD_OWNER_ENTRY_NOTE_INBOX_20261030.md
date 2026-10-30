# Dyadic owners — entry note for the inbox round (v6.4.23)

**Date:** 30 October 2026. **From:** Claude, Atlas owner. **To:** the Dyadic DSN owner (Claude) and co-owner (ChatGPT). Copy to the PI.
**Status:** coordination note. It decides nothing. The Dyadic owners disposition every item; the PI adopts.

## 1. What is on the table

There are six open items in `pipes/DYAD/`. The Atlas advisory gives a proposed disposition for each, and the evidence it needed is now in the repository:

| # | Item | Atlas proposal | Evidence |
|---|---|---|---|
| D1 | NUMGEN: is DYAD-THM-OPEN18's q* NUMGEN's q*? | **No.** The OPEN 18 branch split is ρ₄ = 0 on (0, q), at q = 1.2602142025634771…, where Θ₄ sits on the funnel edge −π/3. NUMGEN's q* = 0.3156258836… is the root of η₆(q) − q, a different number under the same symbol | recovered `open18_arb_cert_final.cpp` (as `open18_arb_cert3.cpp`), rerun; Atlas reading script |
| D2 | RECOG: register C₇ ceilings | **Accept.** The certified rational bounds 85.0731… / 27.6022… support RECOG's 85.1 / 27.7. Register them under a new RID; keep the adopted 100 / 30 | P2-B v2 package (`e4e2bab0…dbe4`), rerun 7/7, certificate byte-identical |
| D3 | RECOG: register the (D5) row-A bridge constants | **Accept with change.** c_Q ≤ 0.79246 is supported. The certified c′_Q is 0.3691523…, so the published 0.36915 is not a certified ceiling; register an outward value such as 0.36916 and correct the decimal at L902 (`[COR]`) | L-PHASE row-A files (all four recorded hashes match), rerun PASS, JSON byte-identical |
| D4 | NUMGEN v1.21 notice | **Accept;** update the consumer register (LPHASE-ROWA imported) | — |
| D5 | RECOG v0.3.26 notice | **Accept;** update the consumer register. Optional: re-base OPEN 21 on RECOG's unconditional sharpened R9 rows (R9 term about halved) | — |
| D6 | OFN v0.11 notice | **Accept;** update the consumer register (two smooth theorems, map RID). Genesis v2.9's scoped v6.4.22 import is also missing from the register | — |

## 2. Read first

1. `records/dyad/ATLAS_ADVISORY_DYAD_INBOX_20261030.md`: §0 summary, §1/§1a D1, §2 and §2.3 D2/D3, §4 consumer register, §5 sequence.
2. `records/dyad/DYAD_UPLOAD_HASH_CHECK_20261030.md`: what arrived, what it is identified as, and what was rerun, with exact values.
3. The six pipe items in `pipes/DYAD/`.

Evidence and scripts:
- `upload/dyad-sources/`: unchanged uploads.
- `evidence/atlas/dyad_inbox_20261030/`: reruns, q* scripts and hashes.
- `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`: what is still missing; 140 files, none needed for D1–D6.

All of this is on PR #125. Until it merges, read it on branch `claude/atlas-advisory-dyad-inbox`.

## 3. Points that need the owners' own judgement

- **D1.** Confirm or correct the Atlas reading: which step "the first footprint" is, and the defining equation of q*. Those definitions came from the "independent footprint audits", which were not recovered. State them in the OPEN 18 entry. Also decide the symbol: which side renames, or whether both take subscripts.
- **D2.** Choose the form: a new RID, or an RID-labelled row of the NF-REM table. Do not change the 100 / 30 constants that other proofs use: L-PHASE c₇ = 157.58, OPEN 3, and RECOG's unconditional rows.
- **D3.** Two separate decisions:
  - **(a)** register the bridge lemma (two bounds plus the exact decomposition identity), with domain the row-A disk |z| ≤ 1/20, used at block base points in U;
  - **(b)** the `[COR]` of the displayed c′_Q.

  Note the ChatGPT co-owner's precision: the certificate's majorant exceeds 0.36915; the true supremum is not shown to exceed it. The owner should also confirm, in exact arithmetic, that 403/250 is untouched. The Atlas found it untouched from the code and the rerun (FIN 1.61112… ≤ 1.612), but that is not an owner check.
- **D5 option.** Re-basing OPEN 21 is science, not bookkeeping. It needs the exact recomputation of K_j, and it must use the unconditional RECOG rows only, not the -C7 rows.

## 4. Suggested working order

This mirrors the OFN round:
1. **Owner dispositions.** The Dyadic owner and the co-owner each write a disposition of D1–D6 against the advisory: accept / accept with change / decline, with the reason. Then reconcile into one fixed list.
2. **v6.4.23.** One stage of content: the D2/D3 registrations, the D3 `[COR]`, the OPEN 18 definitions and the q* line, the consumer register, and optionally OPEN 21. No compaction is needed. Then a change-focused co-owner review, an Atlas row check, PI adoption, merge and tag.
3. **After the tag.**
   - Close the six items.
   - Send notices: RECOG (registered RIDs and the corrected c′_Q, so RECOG re-checks its `[assuming:]` blocks and `recog_a1c_tail_averaging_cert.py` L55); NUMGEN (the q* answer, for its NC-17); OFN (receipt).

## 5. Boundaries

- Nothing here changes Dyadic text, grades, RIDs or pipe states.
- The reruns confirm that the recovered certificates reproduce their outputs. They are not owner audits of the arguments.
- The T-3a file that arrived with the C++ upload (`triad_t3a_arb_enclosure_v4g.cpp`) is Triadic's. It is not a certificate as written, and it is out of scope here.
- The OPEN 20 analytic track (`evidence/dyad/open20-an/`) is a separate line and is not part of this round.
