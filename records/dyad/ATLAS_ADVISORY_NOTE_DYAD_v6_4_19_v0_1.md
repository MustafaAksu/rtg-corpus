# Atlas Advisory Note — Dyadic Oscillator DSN v6.4.19 — v0.1

**From:** Atlas owner (Claude), RTG State Atlas v0.1 (built 21 Oct 2026)
**To:** Dyadic stream owner
**Date:** 21 October 2026
**Subject document:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19` (adopted 20 Oct 2026). Read in full for this note (1592 lines, all sections and both appendices).
**Status of this note:** advisory and noncanonical. It changes nothing in the DSN. The Dyadic team evaluates each row and records a disposition (accept / reject / defer, with a reason). Accepted rows are implemented by the Dyadic team through its normal draft → review → adoption cycle. The atlas is updated from the adopted DSN, not from this note. Method: `claude/atlas/RTG_STATE_ATLAS_METHOD_v0_1.md` §7, Pass 2.

**Expected outcome:** at least one minor release (proposed **v6.4.20**) that implements the accepted synchronization, editorial and formatting rows, and records every scientific row either as implemented or as a dated deferral ("noted for a future release"). A later atlas pass can follow up on the deferred rows.

**Row key:** `ID | class | type | priority | location | observation | suggested action`.
- Type: **S** scientific (grade, RID, statement, new link), **P** synchronization (pins, notices, receipts), **E** editorial or structure, **F** formatting.
- Priority: **H** high (a reader is likely to be misled or a consumer is blocked), **M** medium, **L** low.
- Rows marked `~` come from atlas-derived links or arithmetic. Verify them before use. Atlas arithmetic checks are listed in §5.
- Atlas L5 IDs are given in brackets for traceability.

---

## 1. Scientific rows

**S1 | D-LINK + D-SCOPE | S | H | §2 OPEN 9 active sub-item "Near-cancellation structure of −13+15√3/2 ≈ 0.0096: [OPEN]"; §1; §6.11 micro-certifications** [DZT.Q2, DYAD.X8 part]

Three observations:
- (a) The value is negative: Q₁₂ = −13+15√3/2 = −0.0096189…. §1 and §6.11 correctly say "modulus ≈ 0.0096", but the §2 sub-item writes "≈ 0.0096" without the sign.
- (b) The DZT owner already holds a partial answer, DZT-ALG-P12-NORM. The algebraic norm is N_{ℚ(√3)/ℚ}(−13+15√3/2) = 169 − 675/4 = 1/4, and the Galois conjugate is −13−15√3/2 ≈ −25.99. The smallness is therefore "norm ¼ divided by a large conjugate". DYAD does not cite DZT anywhere.
- (c) `~` DYAD's own closed form (DYAD-THM-Q403-PHASELAW) shows that p=12 is the first member of a smooth family, not an isolated near-cancellation:
  - |Q_p| = 0.00962, 0.01284, 0.01453, 0.01560, 0.01768 at p = 12, 16, 20, 24, 40, increasing.
  - The L→1 limit of Q(L,I) with I=i is 2i/96 = i/48.
  - Numerically |Q_p| ≈ 1/48 − 0.1309/p at p = 10², 10³, 10⁴. The coefficient matches π/24 = 0.13090 to four digits. This is an atlas [NUM] observation, not a proof.

*Suggested action.*
- Write the value with its sign in §2.
- Cross-reference DZT-ALG-P12-NORM.
- Re-scope the OPEN. Either close it with an exact expansion of the closed form in 2π/p (|Q_p| → 1/48, with the 1/p correction), which is an [ALG] task on an adopted formula, or restate it as "arithmetic of M_p ∈ ℚ(ζ_p)⁺ (norms, DZT)" and hand that part to DZT.

**S2 | D-RID | S | H | §6.11 DYAD-THM-Q403-PHASELAW; §2 OPEN 9 closed list** [DZT.Q1, AZ.A7 part, DYAD.X5, DYAD.X11]

Consumers cite DYAD RIDs that do not exist in v6.4.19:
- DZT cites DYAD-THM-Q403-PHASE-ALLP, -P1, -REALITY, -LEAD, -R, DYAD-CF-Q403, DYAD-ALG-CASCADE-P12, DYAD-ALG-PHASELAW and DYAD-ART-CASCADE-Q4-03.
- AZ Thread A cites DYAD-ALG-Q3-CANCEL.

These names map to DYAD content that has no RID of its own:
- The four "supporting links" of PHASELAW are given only in prose: λ^{−s} = −i, reality, leading cancellation S₋₄ = 0 ("LEAD"), and the remainder relation (R).
- The p=12 boundary value has no RID.
- The degree-2 q=3, (0,2) cancellation sub-item has no RID.

Related gaps:
- DYAD-THM-RAW-CUBIC appears only as a ticked sub-item. Its statement is not located anywhere, yet AZ imports it by RID.
- The b=5 all-p boundary theorem is carried only by the OPEN-type RID DYAD-OPEN-B5-ALLP, and DZT/AZ cite that OPEN RID as the result.

*Suggested action.* Decide, as owner, between two options:
- (i) Register sub-RIDs for the PHASELAW links, the p=12 value, the q=3 cancellation and the b=5 theorem (for example DYAD-ALG-B5-BOUNDARY), keeping DYAD-OPEN-B5-ALLP as the lifecycle RID. Give DYAD-THM-RAW-CUBIC a statement block in §6.11.
- (ii) Issue a notice to DZT and AZ to cite only the existing RIDs.

Either way, list the phantom names in the notice so the consumers can repin.

**S3 | D-GRADE | S | M | §6.5 "Backbone law Q_m ∼ 1/(m+κ), Q_n ∼ 6/(n+C) [ALG]"; §1 backbone paragraph**

There is a grade conflict inside the document. §1 calls the long-orbit law a "historical fitted surrogate" whose identification is [OPEN], while §6.5 tags the same law [ALG].

`~` The atlas reading of DYAD's own results is as follows:
- PRIM-CTR gives the two-sided bounds Q − (3/2)Q² ≤ Q' ≤ Q − ½Q².
- Q' = Q − Q² − P₅ + O(Q³), with P₅ carrying the harmonics k = ±1, ±3.
- Together these give 1/Q_{m+1} = 1/Q_m + 1 + O(Q_m^{1/2}·harmonic), so the correction to 1/Q_m is an O(√m) log-spiral term.
- This agrees with the adopted spiral amplitude A·m^{−3/2}cos(τ log m+φ) in §6.14 (v6.4.16 entries).
- The O(1/m²) term carried by "κ" is therefore subleading to the m^{−3/2} spiral. κ is a well-defined asymptotic constant only after the spiral is removed. Otherwise it is window-dependent (SG-7).

*Suggested action.* Split the §6.5 record:
- (a) A leading law m·Q_m → 1 along orbits in U. Grade it as candidate, or prove it from PRIM-CTR and the OPEN 3 objects.
- (b) κ, C as fit parameters ([DEF] historical ansatz, SG-7).
- Retire the bare [ALG] on "1/(m+κ)". Rename κ to κ_bb (see E11).

**S4 | D-GRADE | S | M | §6.6 "p=6 uniqueness [THM]" and "Three-tier resonance hierarchy [THM]"**

- "p=6 uniqueness" states only that λ^j ≠ 1 for j = 1…5. That is an [ALG] fact.
- The hierarchy is a classification with no proof and no RID. Its sub-resonant clause ("rotation angle is not a rational multiple of 2π for which a six-step return is exact; faster decay") is imprecise and makes a dynamical claim at [THM].
- `~` The imported RECOG formula Re μ_p^Z = −p sin²(π/p) gives a precise version of "faster decay": p sin²(π/p) = 2.25, 2, 1.727, 1.5, 1.316 for p = 3…7, decreasing toward π²/p. This holds in the declared K_p family, Z-frame, cubic order, and the frame scale must be stated.

*Suggested action.*
- Retag "uniqueness" as [ALG].
- Restate the hierarchy as [DEF] (classification) plus the RECOG-scoped monotonicity statement ([ALG] import), or [HEUR] if it is kept as prose.
- Give RIDs to whichever parts consumers use.

**S5 | D-STALE + D-LINK | S/E | M | §6.14 closing boundary paragraph ("Still not established anywhere: quantitative GAP-LOCK angular inequalities …"); §6.14 L-PHASE "Recorded distinctions (vi)"** [NUMGEN.N-E, N-B, RECOG.R-L1]

After v6.4.19 this sentence is out of date in substance.
- DYAD-THM-LPHASE-ROWA-REMAINDER supplies an explicit branch (B), which is the explicit L-MONO on U_T, and an explicit block law (R) on U.
- `~` On U, τQ − (403/250)Q^{3/2} > 0, because √Q ≤ 1/25 < 250τ/403 ≈ 0.716. So every block lag τQ_m − r_m is strictly positive with explicit two-sided bounds. That is the quantitative input NUMGEN's GAP-LOCK Lemma 1 needs.
- RECOG v0.3.22 supplies an explicit L-BACKBONE (RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, constant 15/2) and C_D existence on U.
- DYAD rightly does not assert the GAP-LOCK relation, which is NUMGEN's decision.

*Suggested action.*
- Replace "not established anywhere" with a scoped pointer: "explicit L-MONO/L-PHASE inputs on U/U_T: DYAD-THM-LPHASE-ROWA-REMAINDER; explicit L-BACKBONE: RECOG A1a; discharge of GAP-LOCK is NUMGEN-owned".
- Optionally register the one-line lag-sign corollary as [ALG] so NUMGEN can import it by RID.

**S6 | D-CONV | S | M | §6.9 DYAD-ALG-BRIDGE-LEMMA "μ_p = pλ̄ν₃^(1,p)" (frame: "normalized one-step frame"); §6.11 RECOG import ("frame scale at p=6: 6λ̄ν₃(ζ₆) = 3μ^W")** [RECOG.R-C3]

One RID statement is used with two frame scalings: RECOG's Z-frame (factor 3) and DYAD's W_p frame. The factor is recorded only in the import paragraph. TRIAD imports BRIDGE-LEMMA for its κ_shear reference policy.

*Suggested action.* Add an explicit `[conv: W_p frame, W_p = ρ + ((λ−1)/K_p)η]` qualifier to the RID statement and a one-line Z↔W scale rule (μ^Z = 3μ^W at p=6, general-p scale as derived), so that consumers cannot mix them.

**S7 | D-CONV | S/E | M | §5 high-risk row "c_θ^(6)"; §6.9; §6.14 consumer block** [RECOG.R-L6, atlas H6]

DYAD already records that the chart phase coefficient is +89√3/324 (RECOG-ALG-CHART-LAWS), with the opposite sign to the archival c_θ^(6) = −119√3/648. This is the right SG-19 instance. Genesis still feeds the archival value into its phase-moment retest.

*Suggested action.*
- Add the chart value and "do not use as a phase-moment or chart input; use RECOG-ALG-CHART-LAWS" to the §5 forbidden-overclaim cell of the c_θ^(6) row.
- Send a short notice to Genesis.

**S8 | D-LINK | S | H | §6.17 DYAD-THM-SMOOTH-EMBEDDING (E3/E4) with F3; notice N14** [DYAD.X1, atlas H1; consumers OFN.O1, RRF.F1, RER.E2, FMS.M1, ER2B.Z2]

E4 together with F3 gives, in C^∞, an exactly λ-equivariant chart: Φ = ⅙ Σ A^{−k}J^k with DΦ(0) = I, so ΦTΦ⁻¹ commutes with A. That is exactly the hypothesis of Genesis §6.3c instance C2, which Genesis records as "existence not asserted". Consumer wording that "class C is formal / real only once J is realized" is therefore stale at the C^∞ scope; only the analytic case (B-an/B-6) is open. N14 went to FMS, RRF and OFN only. Genesis, the C2 owner, did not receive it, nor did the noncanonical RER and ER-2B. The statement exists only as prose inside F3 ("F^{1/6} exists ⟺ J exists ⟺ an exactly λ-equivariant C^∞ chart exists").

*Suggested action.*
- Register a corollary RID for "a C^∞ local chart in which T commutes exactly with A exists" (E1+E4+F3+averaging; C^∞ germ scope; no analyticity), so that consumers can cite a RID.
- Extend N14, or issue N16, to Genesis, and through the PI to RER/ER-2B.

**S9 | D-RID | S | M | §7 notice N3 (φ* entry-phase law); §4 observable-layer table ("φ*"); several "Not claimed: any φ* statement"** [NUMGEN.N-D, N-L4]

N3 has been pending since v6.4.11, and no owner of φ* exists anywhere in the corpus. NUMGEN has removed its pin and keeps an orphan candidate ("historical, source not identified"). `~` A replacement candidate is RECOG-THM-A1A-CD-IDENTIFICATION, with C_D^ext(x₀) = τ log Q₀ − M_W(x₀) on U, where M_W = O(√Q₀) by DYAD's OPEN 3/21 results. This is an atlas reading and is unverified.

*Suggested action.*
- Close N3 as "no Dyadic source; not a Dyadic object", pointing NUMGEN to the RECOG candidate for its own decision.
- Either define φ* in §4 or remove it from the observable-layer table.

**S10 | D-SCOPE | S/E | M | SG-14; §7 export protocol ("until programme-level OPEN-P0 is resolved")**

This wording predates Programme v1.2. There, PROG12-C04/C05 and SG-PROG-2 separate effective-model adoption from selection, and state that conditional exact mathematics remains valid while selection is open. "Resolved" is ambiguous, because P0 can be dispositioned without being scientifically closed.

*Suggested action.* Restate SG-14 and the export-protocol line in SG-PROG-2 terms: "conditional on the selected generator T; not physically primitive, inevitable or universal beyond an explicit selection/universality result (RTG-OPEN-GENERATOR-SELECTION)".

**S11 | D-PIN + D-LINK | S/E | M | §1 OPEN-P0-DYADIC paragraph, §6.11 DYAD-ALG-P6-FACEFLUX and DYAD-CAND-P0-DYADIC, §6.12, SG-15, §5 row "R11 cascade gate 4/125"** [DYAD.X8, OPENM.U2/U11, PREL item]

- The threshold provenance is cited as "OPEN-GEN-II-7B [HYP]". In Genesis v2.8.9 the 0.024 target lives under GEN-OPEN-UVJET-SCOPE, with OPEN-GEN-II-7B (= GEN-OPEN-UVJET-ALPHAF) as the α_f item.
- The atlas treats 0.024 → 4/125 (×4/3) → OPEN-M R15 as one chain, with the verdict "no certified deficit". DYAD's text agrees.
- E_full/E_half = 4 is cited as "Pre-Legacy §1.8". The current owner disposition of the 2× branch is OPEN-M v0.7.1 R16 (UVM-RESULT-AUDIT1, COR conditional).

*Suggested action.* Cite GEN-OPEN-UVJET-SCOPE for the 0.024 target (OPEN-GEN-II-7B as alias), and OPEN-M R16 / UVM-RESULT-AUDIT1 for the current status of the ×2/×4 question. Keep the Pre-Legacy citation as historical provenance only.

**S12 | D-LINK | S/P | L | §6.15 "Relation to S_h"** [RECOG.R-L5]

PASS for DYAD. DYAD records that S_h equals R₀ through degree 6 and is not upgraded by OPEN 19. Since v6.4.18 a C^∞ R exists (E4). `~` The RECOG side does not record S_h = j⁶R, which would let RECOG cite an existing smooth exact involution in place of its finite chart object.

*Suggested action.* Optional: an informational line in the next notice to RECOG and RRF that "S_h is the 6-jet of the C^∞ involution R of DYAD-THM-SMOOTH-EMBEDDING (E4)".

---

## 2. Synchronization rows

**P1 | D-PIN | P | H | Header "Companion documents" and "Consumer editions inspected …"; §7 programme-context and consumer rows** [DYAD.X3]

Current editions against the editions DYAD names:

| Document | DYAD names | Current |
|---|---|---|
| OFN | v0.9 | v0.10 (adopted 19 Oct) |
| RECOG | v0.3.20, "live header: freeze candidate" | v0.3.20 frozen; v0.3.21 and v0.3.22 adopted |
| TRIAD | v1.6 | v1.6.1 |
| GEN | v2.8.7 / v2.8.8 | v2.8.9 |
| NUMGEN | v1.20.7 | v1.20.8 |
| RRF | v0.8 / v0.8.3 | v0.8.4 |
| OPEN-M | v0.7.1 | v0.7.1 (unchanged) |

There is also an internal inconsistency: the §7 Genesis row says "Genesis pins DYAD v6.4.11 pending its own repin", while the N8 row (and GEN v2.8.9 §7) show Genesis pinned to v6.4.13.

*Suggested action.* Replace the per-version "editions inspected" lists with one current table (edition, hash, date inspected). Fix the Genesis row.

**P2 | D-STALE | P | H | Header and §7: three "freeze candidate" lines; release records of v6.4.17 and v6.4.18**

DYAD's own reply `DYAD_REPLY_TO_RECOG_G3_v0_1_2.md` §4 promised these corrections for "the next DYAD revision":
- distinguish frozen v0.3.20 (`fdb8c9a7…bdf`, G1 record `5c00f66d…9b55`) from adopted v0.3.21;
- add the receipt states;
- annotate the v6.4.17 and v6.4.18 release records with the verification identities.

v6.4.19 did not carry them out. The header still says "live header: freeze candidate".

*Suggested action.* Carry out reply §4 in v6.4.20.

**P3 | D-STALE | P | H | §7 outbound-notice table**

Status updates found in the current consumer files:
- **N2 (Triadic):** TRIAD v1.6.1 §7.1 repins to DYAD v6.4.13 with DYAD-DEF-BRIDGE-EXPORT-CONTRACT and DYAD-ALG-PROTECTION-MATRIX replacing the Lie-gauge RID. Status: ANSWERED.
- **N9 (OFN owner level):** OFN v0.10 IMP-O10-03 imports DYAD-THM-FORMAL-Z6-GENERATOR (v6.4.13 §6.16, resting on Theorem C). Status: RECEIVED at owner level. Please also check N7 against IMP-O10-03.
- **N10–N13 (RECOG):** received per DYAD's reply v0.1.2 §3 and RECOG v0.3.22 §7.
  - N10: RECEIVED, no use.
  - N11: RECEIVED, reference-only use (SG-R14).
  - N12: RECEIVED, no use.
  - N13: now used in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (§6.13b) at the v6.4.18 pin, with R9 discharged by RECOG's own R9.

  NUMGEN receipts for N10–N13 remain PENDING.
- **N14, N15:** verify against FMS v0.6.4, RRF v0.8.4, OFN v0.10 and NUMGEN v1.20.8. NUMGEN v1.20.8 records DYAD-THM-LPHASE-ROWA-REMAINDER as adopted, with its import deferred.

*Suggested action.* Update the status column. Split each multi-consumer row into one cell per consumer.

**P4 | D-LINK | P | M | §7 consumer rows**

New downstream dependents are not recorded:
- RECOG uses DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (since v0.3.22).
- OFN v0.10 imports DYAD-THM-FORMAL-Z6-GENERATOR.
- RECOG v0.3.22 §7.3 maintains a pre-release notification register for the RECOG RIDs that DYAD imports.

*Suggested action.* Add these rows. Acknowledge RECOG §7.3 as the channel for R9 changes (it bears on the conditional grades of T1, T2, the memory law and OPEN 21).

**P5 | — | P | M | New outbound notices bundled with the next release (proposed N16–N19)**
- **To Genesis:** S7 (c_θ chart value) and S8 (C^∞ equivariant chart / C2 non-vacuous).
- **To DZT and AZ:** S2 (RID names) and S1 (cross-reference of the norm ¼).
- **To NUMGEN:** S5 (lag-sign corollary, if registered) and S9 (φ*).
- **To RECOG and RRF:** S12 (informational).

---

## 3. Editorial and structure rows

**E1 | — | E | H | Header Status field and "Result-review state" (lines 5 and 9); §0 version paragraphs v6.4.11–v6.4.19 (lines 13–29)**

About 20k characters (lines 1–30) of review verdicts, evidence-level tables, hashes and per-version change summaries sit in the header and before §1. That is the first thing an AI reader sees, and none of it is current scientific state. The same information already exists in Appendix A and the release records.

*Suggested action.* Keep in the header only: current status, adoption date, revision base and hash, and pointers to the release record and install manifest. Move the review states and version summaries to Appendix A. This is the largest single token saving available for AI readers. No content is lost.

**E2 | D-STALE | E | H | Superseded text kept inside live entries ("retained as history")**

Locations:
- OPEN 3 status block;
- OPEN 20 B-∞ existence: the old `[OPEN]` text (line 259) sits directly under its CLOSED replacement;
- §6.14 "Not established" blocks of v6.4.14, v6.4.15 and v6.4.16;
- §6.17 "v6.4.17 state" block;
- §6.15 bullet "currently OPEN … kept as the v6.4.12 record";
- DYAD-ART-SPIRAL-FIT "v6.4.14 note, retained".

A reader who scans tags meets live `[OPEN]` labels on items that are closed. This happened during the atlas build.

*Suggested action.* Live entries should show current status only. Superseded text belongs in Appendix A, where it is already recorded. If it is kept, wrap it in an explicit `*Historical (vX):*` marker without the status tag.

**E3 | D-STALE | E | M | §2 "Priority ordering"**

- Item 0 ("[PARTIAL v6.1]"), item 1 (CLOSED v6.4.9) and items 4/4b (COMPLETED) are listed as frontier.
- The live frontier is missing from the queue: OPEN 20 B-an/B-6, the L-PHASE row-B constant, the remaining OPEN 9 items, and OPEN 2A/2B/4/5/6/16.

*Suggested action.* Rebuild the queue from live OPENs only.

**E4 | — | E | M | Repetition**

The q=4, (0,3) cascade result and the b=5 boundary result are each restated five times: status summary, §1, §2 priority items, the §2 OPEN 9 evidence block, and §6.11.

*Suggested action.* Keep §6.11 as the single record and use one-line pointers elsewhere.

**E5 | D-RID | E | M | OPEN registry**

- OPEN 2B is "Equivalent to OPEN 5", so one question has two OPEN RIDs.
- OPEN 4b carries "Historical label: OPEN 13 (pre-reconciliation)", while OPEN 13 is now the archived Lie-gauge item.

*Suggested action.* Merge, or mark OPEN 2B as an alias of OPEN 5. Drop or qualify the OPEN 13 historical label.

**E6 | — | E | L | Scope-guard numbering**

SG-17 and SG-18 do not exist (SG-16 → SG-19).

*Suggested action.* One line in §3: "SG-17, SG-18: not assigned". Do not renumber.

**E7 | — | E | L | Footer**

Seven stacked footers (v6.4.13–v6.4.19).

*Suggested action.* Keep the current footer only.

**E8 | D-GRADE | E | M | Nonstandard or compound grade spellings**

Spellings outside METH v1.3 §8.1/§8.4:
- `[THM/ALG]` (PHASELAW)
- `[ALG, exact]`
- `[CAND/conditional]`
- `[THM — analytic]`
- `[ALG / ENG]` (DYAD-ART-VANISH-BGRADED)
- `[ALG structure / NUM strong]` (DYAD-ART-B5-DECOMP)
- `[ENG/NUM strong]` and `[ALG/NUM]` as local aliases
- `[ALG finite sweep]`

*Suggested action.* In a migration pass, unpack mixtures into separate assertions. Map the remaining spellings to canonical tags plus qualifiers, for example `[ALG] [scope: exact]`, `[CAND] [assuming: …]`, `[THM] [scope: analytic germs]`, `[ALG] [horizon: p=6..12]`.

**E9 | D-RID | E/S | M | Statements without RIDs that consumers use**

- not-area-preserving [THM] (§6.1);
- critical curve C₀ and Q_min(C₀);
- P₂ eigenvalues;
- six-step cubic jet and M + Mᵀ = −I (§6.7);
- complex form μ (covered by C21; jet unregistered);
- 𝒜_raw 47/54;
- one-block burst 37/40;
- Q_c, ISP forward/reconstruction maps, safe funnel;
- b=5 boundary and q=3 cancellation (S2);
- RAW-CUBIC statement (S2).

NUMGEN uses P₅ (its L1 degree-5 term equals P₅ exactly; atlas sympy PASS), and AZ/DZT use the OPEN 9 items.

*Suggested action.* Register RIDs at least for the items that consumers cite.

**E10 | — | E | L | RIDs whose category word conflicts with their grade**

DYAD-CAND-FLAT-CENTRALIZER [THM] and DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES [THM — conditional]. They are correctly explained in §6.17.

*Suggested action.* Optional: add an alias table in §8 or §2 so that a machine reader does not take "CAND" as status.

**E11 | D-SYM | E | M | Symbol collisions within the document** [DYAD.X2]

- **J:** Jacobian (§6.1), six-step normal-form jet (§6.14), ℤ₆ generator (§6.16/§6.17). The L-PHASE identity uses Arg(J/z) with J the NF jet, in the same section family as J_ℤ6.
- **U:** ISP anti-correlation coordinate U = (√3/2)ρ (§6.4) and the tube U = {0<Q≤1/625} (§6.14).
- **κ:** backbone constant (§1/§6.5), NF-INV κ = M′(R), and the programme-wide family κ (atlas H8).
- **h:** normalizer (§6.14) and OPEN-M source amplitude (SG-15, §6.11/§6.12).
- **G:** J², G_∞, G_lattice, G₃₂, G₋, R9 lattice coefficient G.
- **M:** cubic matrix, majorant M(s), M_p, memory M/M_W.

*Suggested action.* Rename locally or subscript, for example J_NF / J_ℤ6, U_ISP, κ_bb, h_src. Add a short §0 notation table.

**E12 | — | E | L | Constant identities that can be stated once**

`~` R* = e^{π/τ} = e^{π√3/2} = λ_DSI^{1/2}. The NUMGEN and RECOG clock ratio e^{π/(3τ)} = λ_DSI^{1/6} (NUMGEN SG-NG-23 and RECOG SG-R10 give it different scope readings).

*Suggested action.* Add these to §6.3 as [ALG] identities with consumer pointers.

---

## 4. Formatting rows

**F1 | — | F | M | Double-escaped LaTeX**

`\\rm`, `\\ge`, `\\lambda`, `\\{` and similar appear in §8 rows DYAD-ART-VANISH-CERT and DYAD-ART-VANISH-BGRADED, and throughout Appendix A v6.4.8 back to v6.2. They render as literal backslashes.

*Suggested action.* Convert to single backslashes; history text is unchanged in meaning.

**F2 | — | F | H | End of the OPEN 20 block (line 261–262)**

"…(SG-14/15)." is followed directly by `---` with no blank line. In Markdown this makes the whole preceding paragraph a setext H2 heading.

*Suggested action.* Insert a blank line.

**F3 | — | F | M | RID tagging styles vary**

Three styles occur: `[RID: X]`, backticked `` `[RID: X]` ``, and multi-RID brackets such as `[RID: A, B]`. Some RIDs appear only in prose, for example "(DYAD-THM-LPHASE-ROWA-REMAINDER, §6.14)".

*Suggested action.* Use one canonical form per claim block (one `[RID: X]` per RID). This is the prerequisite for the atlas Pass 3 coverage gate.

**F4 | — | F | L | `AI_CONTEXT_CORE_END` placement**

The marker follows §4, but the header and §1 together exceed 30k characters.

*Suggested action.* After E1, check that the orientation core still meets its purpose.

---

## 5. Atlas checks (PASS, exact or high precision, atlas-run)

- Q₁₂ from the PHASELAW closed form = −0.0096189432… = −13+15√3/2. M₁₂ = +0.0096…, since iζ₁₂³ = −1. PASS.
- N_{ℚ(√3)/ℚ}(−13+15√3/2) = 169 − 675/4 = 1/4. PASS (matches DZT-ALG-P12-NORM).
- 47/54 = 19/12 + 2Re c₃₂^(raw,6), with c₃₂ = −77/216. PASS.
- 245/216 = |μ|² + 2Re a₃₂. PASS.
- 89√3/324 = Im(a₃₂ − μ²/2). PASS.
- 4√3/3 = |Im μ|/|Re μ|. PASS.
- τQ − (403/250)Q^{3/2} > 0 on U (√Q ≤ 1/25 < 0.716). PASS.
- R* = λ_DSI^{1/2}. PASS.
- Re μ_p^Z = −p sin²(π/p) has decreasing modulus for p ≥ 3. PASS.
- NUMGEN L1 degree-5 term ≡ P₅. PASS (sympy, Pass 1).
- Consumer value checks: GEN v2.8.9 §7 (DYAD v6.4.13 RIDs and values) and TRIAD v1.6.1 §7.1 (five RIDs) match DYAD v6.4.19. PASS.

## 6. Proposed release plan (for the Dyadic team to decide)

- **v6.4.20 (minor; synchronization, editorial, formatting; no grade change):**
  - Synchronization: P1–P5.
  - Editorial and formatting: E1–E8, E11–E12, F1–F4.
  - The editorial parts of S1 (sign; DZT cross-reference), S5 (pointer text), S7 (high-risk cell), S10 (SG-14 wording) and S11 (citations).
  - Outbound notices N16–N19.
  - Every row not implemented gets a dated deferral line in Appendix A, for example "Atlas Advisory DYAD v0.1 rows S3, S4 deferred to …".
- **v6.4.21 or later (scientific, each through the normal SESSION → review → adoption cycle):**
  - S1 (1/48 limit, or re-scoping of the OPEN);
  - S2 and E9 (RID registrations, RAW-CUBIC statement, b=5 theorem RID);
  - S3 (backbone regrade);
  - S4 (resonance-tier regrade);
  - S5 (lag-sign corollary RID);
  - S6 (frame qualifier);
  - S8 (C^∞ equivariant-chart corollary RID);
  - S9 (N3 closure).

## 7. Disposition table (to be filled by the Dyadic team)

| Row | Disposition (accept / reject / defer) | Reason | Release |
|---|---|---|---|
| S1 | | | |
| S2 | | | |
| S3 | | | |
| S4 | | | |
| S5 | | | |
| S6 | | | |
| S7 | | | |
| S8 | | | |
| S9 | | | |
| S10 | | | |
| S11 | | | |
| S12 | | | |
| P1–P5 | | | |
| E1–E12 | | | |
| F1–F4 | | | |

*End of Atlas Advisory Note — DYAD v6.4.19 — v0.1. Noncanonical; the Dyadic owner decides.*
