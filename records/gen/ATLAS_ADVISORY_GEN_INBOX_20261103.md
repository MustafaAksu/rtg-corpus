# Atlas advisory — Genesis Geometry inbox (eight items) and pin currency

**Date:** 3 November 2026. **By:** Claude, Atlas owner. The Atlas advises; the Genesis co-owners disposition; the PI adopts.
**Status:** NONCANONICAL advisory. It changes no Genesis text, grade, RID or pipe state.
**Object:** `gen-v2.9`, `dsn/RTG_GENESIS_GEOMETRY_DSN.md`, SHA-256 `9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac` (1,388 lines; equal on `main` `bb9993f`). Line numbers below are at that tag.
**Atlas context:** `atlas-v0.9` (`b48343f5…3b70`). Rows F30, F31, F13, F14, GEN.D3/D5/D6/D7/D17, H6, H7, H8.
**Evidence states:**
- `EV-SRC-READ`: the eight pipe items, gen-v2.9, and the producer tags `dyad-v6.4.23`, `triad-v1.7`, `numgen-v1.21`, `ofn-v0.12`, `tdrg-v2.12.14`, `methodology-v1.4`.
- `EV-ALG` (Atlas, by hand): G7 only. Nothing is rerun; no Genesis certificate is replayed.

## 0. Summary

`pipes/GEN/` holds eight open items:

| Kind | Count | Items |
|---|---|---|
| question | 2 | G7, G8 (from TRIAD) |
| notice | 5 | G2, G3, G4, G5, G6 |
| offer | 1 | G1 (NUMGEN) |

Only G7 and G8 need a scientific decision. The rest are receipts, a label correction and pin currency. They fit one maintenance edition (v2.9.1 or v2.10) with a single content stage. That edition would carry:
- the answers to G7 and G8;
- the field-label correction of G5;
- the receipt rows;
- the stale producer and consumer pins of §9 of this advisory.

No compaction is needed.

## 1. The items and the Atlas proposal

| # | Item | Kind | Atlas proposal |
|---|---|---|---|
| G1 | `20261026-NUMGEN-cyclic-average-route-to-g2-zero.md` | offer | **Accept with change** (§2) |
| G2 | `20261026-NUMGEN-v1-21-adopted.md` | notice | **Accept**; record the receipt; NUMGEN pins `gen-v2.9` (NG-10 source, §9.1) |
| G3 | `20261030-OFN-v0-11-adopted.md` | notice | **Accept, no text change** beyond the companion pin (§3) |
| G4 | `20261030-OFN-v0-12-adopted.md` | notice | **Accept, no action** beyond the companion pin (§3) |
| G5 | `20261103-DYAD-notices-n16-n21.md` | notice | **Accept with change**: correct the `DYAD-ALG-NU5-P5` field label at L1153 (§4) |
| G6 | `20261103-TRIAD-v1-7-adopted.md` | notice | **Accept**; repin the three Triadic imports to v1.7; decide the import grade (§5) |
| G7 | `20261103-TRIAD-p4-identity-question.md` | question | **Answer: yes, and print it** (§6) |
| G8 | `20261103-TRIAD-birth-symmetry-grade-question.md` | question | **Owner decision**: one grade at all three sites; register the RID (§7) |

## 2. G1 — NUMGEN cyclic-average route to G₂ = 0

- **State.** `GEN-ART-G2-CHRONO` (L1264, `[THM]`, `[custody-A]`) is the proof source of the tetrahedral chronological protection G₂(Z)=0 (§6.4, L915). That source is missing. NUMGEN v1.21 now registers `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` (§6.4, `[RESULT][from: ALG]`).
- **Scope of the offered result.** The NUMGEN statement is made for f=R+h_d (the dyad). The diag(A,A,A) case is an application, not a sentence of NUMGEN v1.21 (sender's precision line in the item).
- **Proposal (accept with change).** Cite it as an **independent route**, not a recovery of the original source (Methodology §12.3), and record the application step as a Genesis `[ALG]` line. The step: for L=diag(A,A,A) the degree-2 vector monomial charges a−b−1 mod 6 lie in {1, −1, −3}, none ≡ 0, so the six-step quadratic term vanishes.
  - The `[THM]` grade of §6.4 stays the owner's to keep or narrow while custody (a) is missing.
  - `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` is a second route; the Genesis owner disposition record already names it.
- **Alternative.** Defer, keeping G₂=0 on the missing source alone. F14 then stays as it is.

## 3. G3, G4 — OFN v0.11 and v0.12 notices

- Genesis text uses neither `RTG-OFN-DEF-STANDARD-C` nor the triad test-class field (no occurrence at the tag). So OFN11-C01 and OFN11-C02 need no Genesis wording change. IF32 is OFN consuming Genesis §6.3a–c, not the reverse.
- `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` (v0.12) concerns the "edges minus closure" count over a carrier group. Genesis prints no such count. Its primitive carrier is real, where the K₃ comparison is an isomorphism anyway.
- **Proposal.** Accept both. Update the companion reference "OFN v0.10 (`ofn-v0.10`)" at L1192 and L1231 to `ofn-v0.12`. The G-20 receipt in G3 is OFN's record.

## 4. G5 — Dyadic N16–N21 (field labels)

- **`DYAD-ALG-NU5-P5`.** At L1153 the §7 row reads "closed form, exact over ℚ(√5, √(10+2√5))". The value printed at L689 is complex: (355−159√5)/48 + i(1106√5−2473)√(10+2√5)/48. Dyadic corrected the label at v6.4.20: exact in ℚ(ζ₅), with real and imaginary parts in ℚ(√5, √(10+2√5)). The RID line is byte-identical at `dyad-v6.4.22` and `dyad-v6.4.23` (checked here), and the value is unchanged.
  - **Proposal (accept with change):** correct the label at L1153, keeping the v6.4.13 claim-level pin, or repinning that one row. A label, not a scientific change.
- **FC-DYAD-34** (16/3 equal to the §6.3 ratio) is bookkeeping and selects no birth policy. No action.
- **`DYAD-ALG-LIEGAUGE-NORM` field label** (ℚ(i√3)): Genesis does not import it and prints no field label for it. No action.

## 5. G6 — Triadic v1.7 notice

- **Pins.** Genesis imports `TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY`, `-T6T-JACOBI-MODE-SIGNS` and `-T6U-APEX-SEED-DIAGNOSTIC` from v1.6. This happens in §7 (L1165–1171) and at three points of use in §2 (L232, L243, L360; the L360 block is `GEN-CAND-APEX-T6U`). In v1.6.1 and v1.7 none of the three changes statement, value or grade (Triadic v1.7 §7.3; the notice). The v1.6.1 delta, D3/D3-R1 child-remainder typing, matches Genesis GCL-06.
  - **Proposal:** a claim-level repin of the three rows to v1.7, and of the "Triadic v1.6" headings and the L1229 pin line. Rename OPEN 1T's title "Triadic v1.6 phase/interface import protocol" (L103, L258) to the current edition, with content unchanged.
- **Grade of the imports (owner judgement; Atlas F31).** Genesis writes the three imports as `[CAND]`, below the producer's `[ALG]`. Methodology v1.4 §3.3 has an import carry the source grade of the source claim it imports, and a local transformation is "a separate claim". Two consistent forms:
  - **(a)** import at the source grade `[ALG]`, with Genesis's scope qualifiers ("Triadic v1.7 scope"; "not an OPEN-M source realization");
  - **(b)** keep the Genesis interface statement as a separate Genesis `[CAND]` claim, with the import line beneath it at `[ALG]`.

  The scientific content is the same either way. Today's form mixes the two.
- **Consumer row (L1219).** "TRIAD (IF06) :: Triadic §7, pin v2.8.7" is stale. Triadic v1.7 §7.2 repins its imports to `gen-v2.9` claim by claim. One import is held at v2.8.7: the radial polynomial, until G7 is answered.

## 6. G7 — does Genesis assert 𝒫₄ = 2dᵀBG₃,d?

**The question** (`blocks:` the Triadic §7.2 radial-polynomial repin). §6.5 prints the full ΔQ_d⁽⁴⁾ (L931–941, `[THM]`) but not the d-mode identity. The c-mode analogue ΔQ_c⁽⁴⁾=2cᵀBG₃,c(s,c,0) is printed at L250 and L1243 (`GEN-THM-DELTA-QC`).

**Atlas reading (`EV-ALG`, by hand, from Genesis's own premises).** Let the six-step block map be Z ↦ L⁶Z + G₂(Z) + G₃(Z) + O(‖Z‖⁴), with:
- L=diag(A,A,A), A⁶=I (`GEN-THM-LIN-ORDER6`), so L⁶=I;
- B-isometric A (`GEN-THM-PRIMITIVE-METRIC-INVARIANCE`);
- G₂=0 (§6.4 [THM], L915).

Then, writing d′ = d + G₂,d(Z) + G₃,d(Z) + O(‖Z‖⁴), in general

  Q_d(d′) − Q_d(d) = 2dᵀB·G₂,d(Z) + [2dᵀB·G₃,d(Z) + Q(G₂,d(Z))] + O(‖Z‖⁵),

with the cubic term first and the quartic bracket second. With G₂ = 0, the cubic term and Q(G₂,d) both vanish:

  Q_d(d′) − Q_d(d) = 2dᵀB·G₃,d(Z) + O(‖Z‖⁵).

(Rev. of 3 Nov 2026: the general cubic term 2dᵀBG₂,d was missing from the first expansion. ChatGPT, Atlas co-owner, PR #152 comment `6598961683`. The result under G₂ = 0 is unchanged.)

So the quartic six-step drift **is** 2dᵀBG₃,d, by the same derivation as the printed c-mode identity. This is also how Genesis uses it. GEN-ART-G3D-SEED (L1244) and the T-6u block (L364: V_s:=G₃,d^[s³](s,0,0)) take the apex seed as G₃,d(s,c,0). That equals ½B⁻¹∇_d𝒫₄ at d=0 under the identity, which is Triadic's V_d.

**Proposal.** Answer yes, and print the identity at §6.5 next to the full drift, as a one-line consequence of §6.4. Choose:
- the grade: `[ALG]` derivation, or `[THM]` with the §6.4 premises;
- whether it gets its own RID or is stated inside `GEN-THM-DELTA-QC`'s family. That is the owner's choice; the Atlas proposes no RID name.

Triadic can then repin its radial-polynomial import to the Genesis edition that prints it. This advisory is not an owner statement. The Atlas's derivation checks consistency of the premises; it does not replace Genesis's proof or its missing census source (F14).

## 7. G8 — the grade of the birth-symmetry theorem

**Sites at `gen-v2.9`:**

| Site | Line | Grade |
|---|---|---|
| §6.6, the statement I_ds⁽¹⁾=ω_ds⁽¹⁾=−Q_s²/16 with φ_ds⁽¹⁾ and D_birth^[s³]=7/512 Q_s³ | L987 | `[THM]` |
| §1 "Genesis II archival recovery" ("birth-symmetry sign … promoted to `[ALG]`") | L80 | `[ALG]` |
| §2 OPEN-GEN-II resolution list | L419 | `[ALG]` |
| §8 `GEN-ART-JQ-PHASEDRIFT` ("corrected J_Q, birth-symmetry, and phase-drift law") | L1246 | `[ALG]` |

The result has no own RID (Atlas F13 lists it among the unnumbered Genesis THMs).

**Atlas observation, not a decision.**
- The §1 and §2 lines record the v2.2 promotion step. The §8 row grades one artifact that bundles three statements.
- Under Methodology v1.4, `[THM]` is a complete proof under explicit assumptions and `[ALG]` an exact derivation. The §6.6 values are an exact evaluation from the certified s³ seed. Either grade can be defended, depending on whether Genesis regards the seed derivation as a proof.

**Proposal.** Decide the grade of the birth-symmetry claim first, and use it at §6.6, §1 and §2. Give the result a RID. The §8 artifact row `GEN-ART-JQ-PHASEDRIFT` bundles three statements (corrected J_Q, birth symmetry, phase-drift law), so it does not inherit the claim's grade automatically. The row keeps its own artifact typing and names the result RIDs it supports (PR #152 comment `6598961683`).

Triadic imports it at the §6.6 grade and records the discrepancy (v1.7 §7.2). It follows whatever Genesis fixes.

## 8. What does not need the owners now

These are Atlas L5 rows that a later Genesis edition may take up. They are not part of this inbox, and none blocks it:
- **GEN.D3 / F14:** proof sources under `[custody-A]`.
- **GEN.D6:** B_* undefined.
- **GEN.D7 / F13:** unnumbered theorems.
- **GEN.D17:** the bounded Methodology migration.
- **H7:** the K₃ cubic shared without cross-citation.
- **H8 / F1:** the κ collision.

G1 and G8 touch F14 and F13 respectively.

## 9. Pin and consumer currency at `gen-v2.9` (Atlas observation)

| Line | Text | Current producer / consumer state | Proposal |
|---|---|---|---|
| L1158–1163 | Dyadic v6.4.22, scoped §6.3c rows | both RID lines byte-identical at `dyad-v6.4.23` | optional repin; historical pins at v6.4.13 may stay (Methodology §3.3: a newer version does not invalidate an older pin) |
| L1165–1180, L1229 | Triadic v1.6 | `triad-v1.7`, values and grades unchanged | repin (G6) |
| L1183, L1230 | Discrete Genesis v2.12.13, blocked interface | `tdrg-v2.12.14`; no import | update the pin of the blocked-interface record |
| L1192, L1231 | OFN v0.10 companion | `ofn-v0.12` | update (G3, G4) |
| L1219 | TRIAD consumer, pin v2.8.7 | Triadic v1.7: `gen-v2.9` claim-level, one import held at v2.8.7 | update |
| L1223 | OFN consumer (IF32) | OFN v0.12 imports §6.3a–c | edition only |

Programme v1.3 (L1191) and Methodology v1.4 are current.

## 10. Suggested sequence

This is the Dyadic and Triadic pattern.
1. The two Genesis co-owners disposition G1–G8 separately, then reconcile into one fixed list.
2. One content stage (assertion-gated edits; checker with negative controls), then a change-focused co-owner review and an Atlas row check.
3. PI adoption, merge and tag.
4. After the tag:
   - close the eight items, setting each item's `state` and `disposition` as receiver;
   - answer Triadic on G7 and G8, the Triadic repin being Triadic's;
   - notify the consumers listed in §9 that the edition changes (TRIAD, OFN, RRF, UVM).
