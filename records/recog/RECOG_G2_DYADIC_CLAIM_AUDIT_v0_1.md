# RECOG G2 — Dyadic Claim-Level Audit Record v0.1

**Date:** 19 October 2026
**Status:** `[SESSION]` audit record for review. It precedes any v0.3.21 edit specification. No DSN is edited. RECOG v0.3.20 (`fdb8c9a7…b8df`, FROZEN) remains authoritative. No claim from Dyadic v6.4.17 is accepted by RECOG through this record.
**Consumer:** RECOG v0.3.20, §7 import ledger (Dyadic rows), with every point of use in §§1–6.
**Owner editions:**

| Role | Edition | Identity | Availability in this audit |
|---|---|---|---|
| Pinned | Dyadic v6.4.10 | `7455811928606076b3bc3075632275dc2a24e37fdbf0ae20036db5529a1b56b7` (RECOG §8) | **Bytes not available.** The pinned content is taken from RECOG §7's recorded statements and from v6.4.17's own version-tagged history of v6.4.10 text. |
| Last verified | Dyadic v6.4.16 | `33c14c5c…59e0` (project root; adopted and verified) | Not re-read in full here. The v6.4.16 → v6.4.17 delta is reported as OPEN 21 additions and labels only. |
| Reported current | Dyadic v6.4.17 | `e07cf2b9…4bfc` (adopted; **release verification pending** for this receiving review) | Read in full (project `claude/` copy). |

**Source-fidelity gap and how it closes.** Both gaps are mechanical, not scientific. Running `recog_g2_dyad_passage_diff.py` (sha256 `5e228704…86f9`) on v6.4.10 / v6.4.16 / v6.4.17 closes them:

```powershell
python recog_g2_dyad_passage_diff.py RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md RTG_DYADIC_OSCILLATOR_DSN_v6_4_16.md RTG_DYADIC_OSCILLATOR_DSN_v6_4_17.md > g2_dyad_passage_diff.txt
```

- Every verdict below is **provisional** until that report confirms that the passages are byte-identical across the editions, or shows exactly where they are not.
- If the PI does not hold v6.4.10, the verdicts stay qualified as "against RECOG's recorded pinned statement".

**Verdict vocabulary** (per claim, comparing statement, hypotheses, domain/rows, normalization/chart, remainder/constants, grade and evidence status separately):
- **U** — unchanged;
- **S** — strengthened upstream (the RECOG claim is *not* thereby strengthened);
- **CS** — changed scope;
- **CST** — changed statement;
- **N** — new upstream, recorded and not imported.

---

## A. Load-bearing imports

| # | Import (RECOG §7) | RECOG points of use | Statement | Hyp. | Domain / rows | Norm. / chart | Remainder / constants | Grade | Evidence | Verdict | RECOG consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | DYAD-THM-C21: μ₆ = c₂₁ = −½ − i·2√3/3 | §1, §6.2, §6.7 (jet-law anchor), §6.10, R2 | same value (v6.4.17 §1, §6.2) | p = 6, K = 1, postulated T | local germ | raw six-step | — | `[THM]` | archival proof | **U** | none |
| A2 | DYAD-ALG-NF6: chart h (deg 6, resonant coefficients zero), J, μ = 6λ̄n₂₁, a₀₅ = 6λ̄n₀₅, (3,2) iteration formula | §6.13, §6.13a (R9: a₃₂, a₀₅, G, c_iso), §6.14, F2(a)/(b) | same coefficients: a₃₂ = −97/432 + 197i√3/324, a₀₅ = −49/8640 − 307i√3/25920, n₂₁, n₃₂, n₀₅ | J_≤6 conjugacy only | — | additive degree-6 normalizer, resonant coefficients zero | finite jets | `[ALG]` | **strengthened (v6.4.16):** exact coefficient equality of h, J with the P2B v2 `certificate.json` | **S** (evidence only) | none; the R9 inputs are the identical numbers |
| A3 | DYAD-ALG-NF6-OBS: c₀₅^raw − a₀₅ = (−13+3i√3)/576 | §6.13, §6.14, SG-R13 refusal line | same | — | — | the chart of A2 | — | `[ALG]` | — | **U** | none |
| A4 | DYAD-THM-PRIM-CTR: (108, 1/400, 1/625, ½), tube U_T, ΣQ³ ≤ 2Q₀² | R8 / RECOG-THM-P2-HET (entry target and tail), §6.14 | same (current text also lists ΣQ² ≤ 2Q₀ and the NUMGEN seed admission) | postulated T | Q ≤ 1/400; tube from Q ≤ 1/625 | primitive Q_prim | 108Q³ | `[THM]` | exact-rational certificate | **U** (ΣQ² ≤ 2Q₀ presence in v6.4.10 to be confirmed by the diff report) | none |
| A5 | DYAD-THM-NF-INV: inverse chart, ‖Dh⁻¹‖ < 8/7, 225/256 ≤ Q_prim/q ≤ 289/256 | §6.14 (q ≠ Q_prim); R8 hand-over | same | — | \|z\| ≤ 1/10, \|W\| ≤ 9/100 | the chart of A2 | constants as stated | `[THM]` | certificate | **U** | none |
| A6 | DYAD-THM-NF-REM: C₇/C_D = (100, 1000) on \|z\| ≤ 1/20, (30, 250) on \|z\| ≤ 1/40; Û_T ⊂ {\|z\| < 1/20}; normalized contraction; ΣQ³ ≤ 2q₀² | **R9 (C₇ enters K_Φ, hence C₂)**, R8 hand-over, §6.14 budget | same; certificate values 85.07 / 27.60 and 812.89 / 216.77 | — | two rows, not mixed | the chart of A2 | as stated | `[THM]` | certificate; **v6.4.14 adds `[NUM]` sampled \|F̂−J\|/\|z\|⁷ ≈ 0.971** against C₇ = 100 / 30 | **U** (the `[NUM]` observation is new information, not a change) | none now; relevant to B1 (C₂ budget) |
| A7 | DYAD-ALG-BRIDGE-LEMMA: μ_p = p λ̄ ν₃^(1,p) (general form) | §1, §6.10, R2 | same; **v6.4.11 cites RECOG §6.12 as the general-p proof provenance** | p ≥ 5, K_p family | — | normalized one-step frame | — | `[ALG]` | — | **U**, with a **mutual-citation guard** (see C2) | wording only: RECOG cites its own §6.12 as the proof of the general form and the Dyadic RID for the statement. No evidence is created by mutual citation. |
| A8 | DYAD-ALG-P6-FACEFLUX: λ = e^{iπ/3} = e^{iF_f/2} | §7 only ("not used for derivation") | same | — | p = 6 | — | — | `[ALG, exact]` | — | **U** | none |
| A9 | DYAD-ALG-ALIAS-PHASE: G₋(π/τ) = 1/(1−iτ) | §6.13 `[HEUR]` cross-reference only | same | — | — | — | — | `[ALG]` | — | **U** | none |
| A10 | DYAD-ALG-LIEGAUGE-NORM; §6.9 raw six-step c₃₂, c₀₅, c_θ^(6) | §6.13 frame correction, R11 history, refusal line | same values and the same archival labelling (SG-19) | — | — | Lie strict-kernel / raw six-step | — | `[ALG]` [conv] | — | **U** | none |
| A11 | §6.1 block: map, J, det J, C₀, P₁, P₂, escape law, non-symplecticity | §1, §6.3, §6.5, §6.11, §6.16c, R7 | same content; **new RID `DYAD-DEF-PRIMITIVE-MAP` (v6.4.11, "provisional"; Genesis alias)** | — | lifted chart | primitive | — | `[DEF]` / `[ALG]` / `[THM]` | — | **S** (identifier only) | §7 row may cite the RID with its provisional custody note; the content is unchanged |
| A12 | §6.4 block: Q_c = (arcsin ln 2)², winding invisibility, ISP Θ | SG-R8, §6.15c (twin Q_c semantics) | same | crossing step | — | primitive / ISP | — | `[ALG]` / `[ALG structure]` | — | **U** | none |
| A13 | §6.7–6.8 block: M + Mᵀ = −I, Q_{m+1} = Q_m − Q_m² + ⋯, Θ_{m+1} = Θ_m − τQ_m | §6.2 χ₆ reconstruction | same; the v6.4.10 COR (raw remainder O(\|W\|⁴)) is already reflected in RECOG §1 | — | — | raw linear eigenframe | O(\|W\|⁴) raw | `[ALG]` / `[ALG structure]` | — | **U** | none |
| A14 | §6.3 constants τ, R*, λ_DSI | §6.13 lattice clock | same; **new definition-ledger RIDs (v6.4.11): DYAD-ALG-Q-INVARIANT-FORM, DYAD-ALG-TAU-DETB, DYAD-ALG-CUBIC-PARABOLIC** | — | — | — | — | `[ALG]` | — | **U** (+ N for the RIDs) | see C1 (dual registration) |
| A15 | §6.2 h₂ = −(1+i√3)/12 z² − ⅓ zz̄ + (1−i√3)/24 z̄² | §6.13 frame correction, F2(b) chart shadow, F2(a) S_h | same (§6.2 c₂₀, c₁₁, c₀₂; §6.14) | — | — | — | — | `[ALG]` | — | **U** | none |
| A16 | §6.11 ν₅^(1,6) = 43/17280 − i·227√3/155520 | §6.13 (c₀₅^NF confirmation) | same | — | — | one-step engine/DSN bridge convention | — | `[ALG]` | — | **U** | none |
| A17 | §6.5 47/54 as the raw fixed-radius angular mean 𝒜_raw | §6.13, §6.14, §7 (non-transfer record) | same (v6.4.10 rescoping retained) | — | — | raw W, averaging operator | — | `[ALG]` [scope] | — | **U** | none |
| A18 | Dyadic OPEN 12 (R3 dependency) | R3 dependencies | **status changed: OPEN → PARTIAL (v6.4.11) "by consumer theorems"**, importing RECOG-THM-P2-HET and -C0-FIRST; remaining: global W^s(P₂), later C₀ re-intersections, large amplitude | — | — | — | — | — | — | **CS** (owner status), consistent with RECOG R3 | R3's dependency line may record that Dyadic OPEN 12 remains open exactly for W^s(P₂). No RECOG status change. |

**No row is CST.** No load-bearing import changed its statement, hypotheses, domain, rows, chart, constants or grade between the pinned content and v6.4.17. This is subject to the diff report.

---

## B. New upstream results (N) — recorded, not imported

| Item | Edition | Grade | Relation to RECOG | Disposition in v0.3.21 |
|---|---|---|---|---|
| N10: DYAD-ALG-OPEN3-LEADING; DYAD-THM-OPEN3-SPIRAL-REM | v6.4.14 | `[ALG]`; `[THM]` | per-block chart spiral residual; no C_W^{(h)} statement; no R9 raw-track transfer | receipt (fields below) |
| N11: DYAD-ALG-OPEN3-PHASE-OFFSET; DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS; DYAD-THM-OPEN3-ASYMPTOTIC-PHASE (T1, T2, memory law) | v6.4.15 | `[ALG]` (primitive part `[ALG — formal]`); `[THM]`; T1 `[THM — cond. R9]`, T2 `[THM — cond. T1]`, law `[THM — cond. R9]` | quantifies SG-R14; all three conditional results depend on RECOG-THM-R9-MEMORY | receipt; SG-R14 note (G2 item 4); §7.2 dependents |
| N12: OPEN 3 CLOSED (defined scope); OPEN 21 opened | v6.4.16 | lifecycle | none | receipt (informational) |
| N13: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER | v6.4.17 | `[THM — cond. R9]` | uses R9 at statement level (Λ₁, c_iso, C₂ = 517/163, q_max, C_z) | **conditional receipt only** (below); §7.2 dependent, marked "reported edition, verification pending" |
| DYAD-THM-LOCAL-INVOLUTION-GERM; DYAD-THM-FORMAL-CENTRALIZER; DYAD-THM-FORMAL-INVOLUTION-UNIQUE; DYAD-THM-ANALYTIC-CLOCK-BRIDGE; DYAD-THM-FORMAL-Z6-GENERATOR; Lemma F / F1–F3; OPEN 20 | v6.4.11–13 | `[THM]` (formal / conditional) | bears on R1 and S_h typing; it is the substrate of the later A2 cell | recorded only; **no import in v0.3.21** (A2 is a separate scientific cell) |
| DYAD-ALG-NF6-DEG10 (degree-10 even term of F̂ for the fixed h₆) | v6.4.11 | `[ALG]` finite | already respected by RECOG (SG-R13: −z is not an exact symmetry of F̂; F3(b) VF-1 remark) | recorded; RECOG's RRF-v0.4 row note ("reported even degree-ten term … not used") can point to the owner RID |
| DYAD-DEF-BRIDGE-EXPORT-CONTRACT; DYAD-ALG-PROTECTION-MATRIX; DYAD-ALG-NU5-P5 | v6.4.11, v6.4.13 | `[DEF]`; `[ALG]` | not used by RECOG | none |

---

## C. Findings requiring wording in v0.3.21 (no scientific change)

1. **Dual registration (A14).**
   - RECOG-ALG-INVARIANT-FORM ("every symmetric H with AᵀHA = H is H = cB") and DYAD-ALG-Q-INVARIANT-FORM state the same algebraic fact.
   - Proposed: RECOG keeps its RID and proof, and adds a cross-reference line ("same statement registered by Dyadic v6.4.11 §6.3; independent proofs; no transfer of authority in either direction").
   - This is not an import.
2. **Mutual citation (A7).**
   - Dyadic now cites RECOG §6.12 as the proof provenance of the general-p bridge lemma, while RECOG §6.10/§7 imports the general form from Dyadic.
   - Proposed wording: the *statement* is Dyadic's RID; the *general-p proof* is RECOG's §6.12 (RECOG-ALG-LEADING-RETURN-EQUIVARIANCE); neither citation adds evidence to the other.
3. **Reverse-direction dependents (for §7.2).** Dyadic imports these RECOG RIDs at owner grade:
   - RECOG-ALG-NU3-CLOSED-FORM and RECOG-ALG-NU3-NONVANISHING (OPEN 9 sub-item);
   - RECOG-ALG-LEADING-RETURN-EQUIVARIANCE (provenance);
   - RECOG-ALG-CHART-LAWS;
   - RECOG-THM-R9-MEMORY;
   - RECOG-THM-P2-HET and RECOG-THM-P2-C0-FIRST (OPEN 12).

   The register should list all of these, not only the R9-conditional theorems. A change to any of them is noticeable.
4. **Dyadic's view of RECOG's lifecycle.** Dyadic §7 records RECOG v0.3.20 as "freeze candidate; final freeze record not inspected". The G3 notice to Dyadic should cite the G1 record.

---

## D. Receipts — draft field contents (three separate states)

| Notice | (a) Received | (b) Source verification | (c) RECOG use / acceptance |
|---|---|---|---|
| N10 | DYAD v6.4.14, notice `ea120a26…b4c0`; RIDs DYAD-ALG-OPEN3-LEADING `[ALG]`, DYAD-THM-OPEN3-SPIRAL-REM `[THM]` | v6.4.14 adopted and superseded; the passages are carried unchanged in v6.4.16 (verified) | **No import.** Per-block chart statements; RECOG makes no claim from them. Consequence: none. |
| N11 | DYAD v6.4.15 (`be270dde…47c4`); RIDs per B | carried in v6.4.16 (verified) | **Reference import for SG-R14 only:** M_W − M = −Δ₀(z₀), \|M_W − M\| ≤ K₀√q₀, rows K₀ = 1101/1000 (\|z\| ≤ 1/20), 533/500 (\|z\| ≤ 1/40), not mixed. M_W is the primitive-phase memory built through Dyadic's transported asymptotic-phase observable; it is **not** a theorem for C_W^{(h)}. Assumptions: T1 conditional on RECOG-THM-R9-MEMORY, T2 conditional on T1. RECOG's own claims are unchanged. |
| N12 | DYAD v6.4.16 (`33c14c5c…59e0`) | verified adopted edition | No import; lifecycle only. |
| N13 | DYAD v6.4.17 as **reported** (`e07cf2b9…4bfc`); RID DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER | **pending:** release verification of v6.4.17 is not available to this review | **None decided.** Recorded as a conditional downstream dependent in §7.2. RECOG's standing obligation (notify before any change to R9's statement, rows, C₂ or track) applies regardless. |

---

## E. Completeness check

- **Every Dyadic row of RECOG §7 is covered:**
  - C21, NF6, NF6-OBS, PRIM-CTR, NF-INV, NF-REM, BRIDGE-LEMMA (both rows), P6-FACEFLUX, ALIAS-PHASE, LIEGAUGE-NORM;
  - the §6.1, §6.2 h₂, §6.3, §6.4, §6.5, §6.7–6.8 and §6.11 blocks;
  - the §6.13 / R11 historical rows (A10, A17).
- **Dyadic objects used in RECOG prose but not in §7** (OPEN 12, the R10 template) are covered by A18 and by R10's existing "DELIVERED and ACCEPTED" record, which is unchanged.
- **Historical pins** (e.g. the v6.4.9 → v6.4.10 note in the header; R11 v0.3.1 history text) are recorded as historical and not re-evaluated, per the v0.3.18 practice. Their identities stay as written.

---

## F. Open items before an edit specification

1. Run the passage-diff report (PI machine): it closes source fidelity for A1–A18.
2. Release verification of Dyadic v6.4.17 decides N13's field (b). It does not block v0.3.21, because N13 stays conditional.
3. The Genesis, OFN and RRF claim-level audits follow in the same format, as separate records.
