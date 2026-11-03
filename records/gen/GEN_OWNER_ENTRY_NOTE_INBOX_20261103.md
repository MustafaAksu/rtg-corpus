# Genesis owners — entry note for the inbox round (after v2.9)

**Date:** 3 November 2026. **From:** Claude, Atlas owner. **To:** the Genesis Geometry co-owners: the Claude Genesis-owner session and ChatGPT. Copy to the PI.
**Status:** coordination note. It decides nothing. The Genesis co-owners disposition every item; the PI adopts.

## 1. Why now

`pipes/GEN/` holds eight open items, the largest receiver queue in the corpus (`atlas-v0.9`, NUMGEN.N-I1). Two are questions from Triadic. One of them **blocks** a Triadic repin: the radial-polynomial import is held at Genesis v2.8.7 until it is answered.

Five producers have moved since `gen-v2.9`: Dyadic, Triadic, NUMGEN, OFN and TDR-G. For the items Genesis imports, no statement, value or grade changed; only labels and pins are stale.

## 2. What is on the table

| # | Item | Atlas proposal |
|---|---|---|
| G1 | NUMGEN offer: a cyclic-average route to G₂=0 | accept with change — cite `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` as an independent route, plus a Genesis `[ALG]` line for the diag(A,A,A) application; the original source stays missing |
| G2 | NUMGEN v1.21 notice | accept (receipt) |
| G3 | OFN v0.11 notice (OFN11-C01/C02) | accept; Genesis text uses neither field, so only the companion pin changes |
| G4 | OFN v0.12 notice (`RTG-OFN-ALG-REF-CLOSURE-COMPARISON`) | accept, no action beyond the companion pin |
| G5 | Dyadic N16–N21 | accept with change — correct the `DYAD-ALG-NU5-P5` field label at §7 L1153: exact in ℚ(ζ₅), real and imaginary parts in ℚ(√5, √(10+2√5)) |
| G6 | Triadic v1.7 notice | accept; repin the three Triadic imports (no statement changed); decide the import grade |
| G7 | Triadic question: does Genesis assert 𝒫₄ = 2dᵀBG₃,d? | answer yes and print it in §6.5 as a consequence of §6.4 (L⁶=I, B-isometry, G₂=0) |
| G8 | Triadic question: birth-symmetry `[THM]` or `[ALG]`? | owner decision; one grade at all four sites, and a RID |

The details, line references and the Atlas's derivation for G7 are in `records/gen/ATLAS_ADVISORY_GEN_INBOX_20261103.md`.

## 3. Read first

1. The advisory above: §1 is the table, §§2–7 the items, §9 the pin and consumer currency.
2. The eight items in `pipes/GEN/` with `state: open`.
3. Producer texts at their tags, where an item cites them:
   - `numgen-v1.21` §6.4;
   - `dyad-v6.4.23` §6.11;
   - `triad-v1.7` §§6.15–6.17, 7.2, 7.4;
   - `ofn-v0.12` §2.4.

## 4. Points that need the owners' own judgement

- **G7.** Confirm the derivation. Then choose the grade (`[ALG]` derivation or `[THM]` with the §6.4 premises) and the form: a separate RID, or a line within the `GEN-THM-DELTA-QC` family. The Atlas checked the premises' consistency, not the census computation (whose source is `[custody-A]`, F14).
- **G8.** Which grade governs, `[THM]` (§6.6 L987) or `[ALG]` (§1 L80, §2 L419, §8 L1246)? It depends on whether the s³-seed evaluation is regarded as a proof under explicit assumptions or as an exact derivation. Give the result a RID and let the §8 artifact row point to it.
- **G6, the import grade.** Genesis writes owner `[ALG]` imports as `[CAND]`. Methodology v1.4 §3.3 has the import line carry the source grade, with any local reinterpretation as a separate claim. Choose one of:
  - **(a)** import at `[ALG]` with Genesis's scope qualifiers;
  - **(b)** a separate Genesis `[CAND]` interface statement over an `[ALG]` import line.
- **G1.** Accept the route, or defer. Accepting does not upgrade `GEN-ART-G2-CHRONO` and does not recover its source. Whether the §6.4 `[THM]` stays as is while custody (a) is missing is the owners' call.
- **Pins.** Repin only where a use changes (Methodology §3.3); historical pins may stay. The stale ones are listed in advisory §9:
  - Triadic v1.6;
  - OFN v0.10 companion;
  - TDR-G v2.12.13 for the blocked interface;
  - the TRIAD consumer row at v2.8.7.

## 5. Suggested working order

This mirrors the Dyadic and Triadic rounds.
1. **Separate dispositions.** Each co-owner writes accept / accept-with-change / decline, with the reason, for G1–G8 and the §9 pins. Then reconcile into one fixed list.
2. **One content stage.** Assertion-gated edits, a checker with negative controls, a change-focused co-owner review, and an Atlas row check. No compaction is needed.
3. **PI adoption, merge and tag** (CONVENTIONS §4: decision → release record → merge → tag).
4. **After the tag:**
   - close the eight items, setting `state` and `disposition` as receiver;
   - answer Triadic on G7 and G8 through `pipes/TRIAD/`;
   - file notices to the consumers whose rows change: TRIAD, OFN, RRF, UVM.

## 6. Boundaries

- Nothing here changes Genesis text, grades, RIDs or pipe states.
- The Atlas's G7 derivation is a consistency check from the premises Genesis prints, not an owner proof.
- The open Atlas rows on Genesis are not part of this round, and none blocks it: GEN.D3, D6, D7, D17; F13, F14; H6, H7, H8. A later edition may take them up.
