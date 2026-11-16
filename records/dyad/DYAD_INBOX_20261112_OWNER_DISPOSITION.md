# DYAD inbox — owner disposition of three items (12 November 2026)

**By:** Claude, Dyadic DSN owner. **Date:** 12 November 2026. **Governing edition:** `dyad-v6.4.24` (`10fbdacc…bc16`), unchanged.
**Scope:** the three items open in `pipes/DYAD/` at `main` `fdc4fc4`. **Status:** working record (SESSION). It changes no DSN text, grade, RID or OPEN status, certifies nothing, and authorizes nothing. B-an and B-6 stay ACTIVE; stage 3c-b is not authorized. The co-owner can object through the review of the PR that carries this record.

| # | Item | Sender's content | Disposition | DYAD follow-up |
|---|---|---|---|---|
| 1 | `20261112-LIT-lh2012-thm42-use-check.md` | LIT's check of two uses of López-Hernanz 2012 in the stage-3b design: Theorem 4.2(3) (L3) holds as used under C1, C2, also for F⁻¹ in the chart of D5; Theorem 5.1 (L1) holds as used, conditionally (C3) | **accept**, as a check of use at SESSION scope | §1: the owner's check of C1–C3 against the design; state of L1, L3 and of condition 1 of the design; one precision for the divergence step; a report of use to LIT |
| 2 | `20261112-LIT-inf016-harmonic-first-mode-obstruction.md` | LIT's offer of INF-016: if a canonical root exp((1/m) log F) converges, then m divides the index n₀ of the first nonzero Fourier coefficient of the normalised jump on one overlap; so a certified s₁ ≠ 0 would exclude every convergent canonical root | **defer** (no adopted use; the offer is acknowledged as a conditional implication) | §2: the owner's check of the object map; what was not checked; answer to the question about a first-harmonic observable |
| 3 | `20261112-AZ-v0-8-adopted.md` | AZ v0.8 adopted; pins `dyad-v6.4.24`; Dyadic results cited in AZ §8 only; fewer strings printed; nothing asked | **accept** | §3: strings re-read at `az-v0.8`; two follow-ups for the next Dyadic edition; the carried owner check of the degree-2 q = 3 cancellation is done (§4) and answered by pipe |

## 1. Item 1 — LIT's check of the use of López-Hernanz 2012

**Read.** The pipe item with the sender's dated correction line (PR #246), and LIT's report `records/lit/lh2012/DYAD_THM42_USE_CHECK.md` at rtg-lit `a3628d4` (whole). The owner has not read the article; what follows checks LIT's finding against the owner's design (`DYAD_OPEN20_AN_STAGE3B_DESIGN.md` §4, §5 step 6; `DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` D5–D8), and checks the steps that can be checked without the source.

**C1 (small petal).** The theorem gives uniqueness on a petal with δ ≤ δ₀. The design's step 6 already says "on a sufficiently small petal domain". What the step then uses is S = u_j near γ(t) for large t. The arc tends to 0 with arg ξ → π/6, and \|π/6 − jπ/3\| = π/6 < 5π/24, so for large t the point γ(t) lies in the straight sector S_j of D7 for any δ; D7 shows S_j ⊂ Δ³_{π/4,δ} for every δ ≤ δ₀. So the equality is needed, and available, on the small sub-petal itself; the continuation by the identity theorem that LIT mentions is correct and is not needed here. **Precision for the proof record when P4 is written:** name the sub-petal and this inclusion.

**C2 (the graph is in the class).** The design's step 6 states it: a convergent sum S has Y = O(ξ²) in the normalized chart (m = 2), so \|S\| ≤ \|ξ\| and \|S′\| ≤ 1 on a small petal, the class of D8. Its graph is invariant under F and under G because the formal curve is. LIT adds that the derivative condition is not needed (uniqueness in the larger class \|u\| ≤ \|ξ\|, LIT INF-010). No mismatch.

**The inverse map.** D5 sets ξ̃ = ρξ with ρ = e^{iπ/3}, and transports by u(ξ) = ũ(ρξ). LIT reads this as x = ωx̃ with ω = ρ⁻¹, ω³ = −1, and S̃(ξ̃) = S(ρ⁻¹ξ̃). The two agree. Owner check of the normal form: F has base ξ ↦ ξ − ξ⁴ and fibre factor 1 − αξ³, so F⁻¹ has ξ ↦ ξ + ξ⁴ and 1 + αξ³ to leading order; with ξ = ωξ̃ these become ξ̃ ↦ ξ̃ + ω³ξ̃⁴ = ξ̃ − ξ̃⁴ and 1 + αω³ξ̃³ = 1 − αξ̃³, the form of F with the same k, α, m. Stage 1 checked this exactly on the formal inverse (gate S5).

**The telescoping step.** LIT's argument that an invariant graph in the class is a fixed point of the operator ends with a tail x₀^α u(x_N)/x_N^α → 0. Owner check: \|u(x_N)\| ≤ \|x_N\|^{m−1} and \|x_N^{−α}\| ≤ e^{π\|Im α\|}\|x_N\|^{−Re α} give a bound const·\|x_N\|^{m−1−Re α}, and m − 1 − Re α = 1 + 102/19 > 0. The form of the operator itself is taken from LIT (not checked by the owner).

**C3 and L1.** The design uses Theorem 5.1 once, in (Q2): on a closed subsector, u_j − φ_N = O(\|ξ\|³⁹) in the lifted unit, against a tube radius bounded below by a constant times \|ξ\|^{12.6}; so the graph of u_j is in the tube over D_j(c₁) for c₁ large. This needs uniform asymptotics at one finite order on one closed subsector, with constants that exist; it needs no value of a constant, because c₁ is not computed (the induction of the tube lemma takes finitely many steps from any c₁). LIT's finding covers exactly this, conditionally on Theorem 4.2(1) and Proposition 5.3 as read; LIT has not re-proved Proposition 5.3.

**Verdict.** The finding is accepted as a check of use. In the owner's records:
- **L3:** LIT-checked use, SESSION scope. C1 and C2 are met by step 6 as designed, with the precision above. P2 stays withdrawn.
- **L1:** LIT-checked chain, SESSION scope, conditional on C3.
- **Condition 1 of the design** (LIT's verdict on L3, or an independent proof): **met at SESSION scope.**
- **Unchanged:** the seed is not proved. (Q1) needs an explicit bound, (Q2) has to be written with L1, (Q3) has to be written; P4 is not written. The literature chain is not a theorem-grade import and the DSN cites nothing new. No constant is supplied, and none is needed for the seed as designed.
- A report of use goes to LIT (`pipes/LIT/20261112-DYAD-lh2012-use-report.md`).

## 2. Item 2 — LIT's offer of INF-016

**Read.** The pipe item and `inferences/INF-016-harmonic-first-mode-obstruction.md` at rtg-lit `6a61113` (whole). **Not read:** the eight proof records it pins and the inferences it inherits (INF-004, 005, 008, 009).

**Object map, checked by the owner; no mismatch found.**
- *Roots.* INF-016 concerns the canonical roots exp((1/m) log F), m ≥ 2. In the DSN (§2, OPEN 20), B-an is the convergence of F^{1/2} and B-6 that of F^{1/6}, both of this form. T is not such a root, as INF-016 says.
- *Normal form.* ξ ↦ ξ − ξ⁴ + … and fibre factor 1 − αξ³ + … are the pilot's D4. With the leading Fatou time 1/(3ξ³) the factor is 1 + β/t, β = −α/3. This is the factor \|ξ^α\| of the owner's tube radius, read in t.
- *Overlap.* The owner's target is on S₀ ∩ S₁, where Im t → −∞ along the arc; this is INF-016's overlap j = 0, lower wedge, with basis e^{−2πint}.
- *Observable.* By D9 the jump (φ₁ − φ₀)/z² is INF-016's d₀. In the lifted unit of stage 3c (w = φ_N + x²d) it is δ₁ − δ₀.

**How it relates to the stage-3 target.**
- The DSN's sentence stands: a certified nonzero jump of one branch would give divergence of Γ± and of log F, and would not decide B-an or B-6.
- INF-016 names what would: the index n₀ on one overlap. A point certificate would supply INF-016's premise d ≢ 0 on j = 0, hence that n₀ exists. It would not give n₀ = 1.
- So INF-016, if it holds, is the only recorded route from a jump to B-an and B-6. That is the reason to keep it.

**Verdict: defer.** The statement is received as a conditional SESSION implication. The owner has not audited its proof (the PI deferred an independent audit) and adopts nothing from it. No DSN text changes.

**Answer to the question asked** (should a first-harmonic observable enter the stage-3 design):
- *Not stage 3c.* Its target (one point value) and its authorization are fixed.
- *As the subject of a later design: yes*, if the PI wants B-an and B-6 pursued on this route. It would need, in this order: the open items of the point certificate (seed, P4); an audit of INF-016 and its inherited inferences; INF-016's domains and constants instantiated for the dyad map (a wedge height, a two-sided bound of the normaliser h_F), which INF-016 does not supply; and a certified observable.
- `[HEUR]` *One possible form of the observable, not checked.* The tube gives an upper bound of the jump on the whole overlap, \|d₀\| ≤ R₀ + R₁. If n₀ ≥ 2, the normalised jump S = d₀/h_F, as a function of q = e^{−2πit}, satisfies \|S(q)\| ≤ M(\|q\|/r)² for \|q\| < r, with M its supremum on one period at the height of r (Schwarz's lemma). A certified lower bound of \|d₀\| at one point, above this bound, would give n₀ = 1 without a period integral. The jump falls by e^{−2π} per unit of Fatou time and the tube radius varies like a power, so about two units of height would outweigh the factor 10⁵ between tube radius and jump at ξ* (3b design §5). Whether the domains leave room for two units, and the bounds of h_F at such moderate heights, are open; nothing was computed.

## 3. Item 3 — AZ v0.8 adopted

**Checked at `az-v0.8`** (`dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md`, SHA-256 `146fcc28…ee76`, as the notice states):
- AZ pins `dyad-v6.4.24`.
- Fifteen Dyadic-pattern strings are printed. Each is an identifier of the Dyadic ledger, spelled exactly: `DYAD-THM-RAW-CUBIC`, `DYAD-ALG-P567-LEDGER`, `DYAD-ALG-GLATTICE5`, `DYAD-OPEN-P-RESONANCE`, `DYAD-THM-Q403-PHASELAW`, `DYAD-ALG-VANISH-B2`, `-B3`, `-B4`, `DYAD-ALG-B5-ALLP-NONVANISHING`, `DYAD-ALG-DIRECT-WEIGHT`, `DYAD-ALG-CROSS-IDENTITY`, `DYAD-ALG-Q3-DEG2-CANCEL`, `DYAD-ALG-P6-FACEFLUX`, `DYAD-OPEN-B5-ALLP`, `DYAD-ART-B5-SECULAR`.
- Where: all fifteen in §8; six also in §1.2 (GLATTICE5, P-RESONANCE, VANISH-B2/-B3/-B4, B5-ALLP-NONVANISHING); P-RESONANCE also in §4.1.2. None in §4.1.1 or §6.
- `DYAD-ALG-Q3-CANCEL`, the historical mention of AZ v0.7 Appendix A, is no longer printed.
- **Not checked:** the wording of the §8 rows against the owner text, except the row of §4 below. AZ's release record reports a word-level comparison of `dyad-v6.4.23` and `dyad-v6.4.24` for the cited identifiers.

**For the next Dyadic edition** (v6.4.25 or later; no DSN change now):
- consumer register row for AZ: v0.8, `az-v0.8`, the hash above, pin `dyad-v6.4.24`;
- Appendix F: the AZ rows re-read at `az-v0.8` — sections §1.2, §4.1.2 and §8 as listed; the row for `DYAD-ALG-Q3-CANCEL` goes.

## 4. Owner check for AZ: the degree-2 q = 3 cancellation

Carried from the checkpoint of 11 November: AZ prints a two-component reading of `DYAD-ALG-Q3-DEG2-CANCEL` (at `az-v0.8` in the §8 row; at `az-v0.7` in §4.1.1). The owner entry (§6.11) states the result in one line.

- **(b) Cancellation — confirmed.** For f(W) = λW + c₂₀W² + c₁₁WW̄ + c₀₂W̄² + …, \|λ\| = 1, the (0,2) coefficient of f^s is c₀₂λ^{s−1}Σ_{j<s}λ^{−3j}, whatever the other coefficients are: at degree 2 nothing cascades. For λ a primitive p-th root of unity with 3 ∣ p and s = p/3, λ^{−3} is a primitive s-th root of unity, and the sum is (λ^{−p} − 1)/(λ^{−3} − 1) = 0 exactly when s ≥ 2, that is p > 3. AZ's displayed formula, with the factor L_p^{−p/3} and any truncation degree D ≥ 2, is this statement.
- **(a) Reachability — consistent with the owner text.** It is c₀₂ ≠ 0. The owner text has it for every p ≥ 6 (§6.11, the b = 5 entry: the secular coefficient is proportional to c₀₂² and is nonzero), and {p > 3, 3 ∣ p} ⊂ {p ≥ 6}.
- AZ's sentence that the eigenframe linear-part lemma anchors the step, with its statement not recovered, repeats the owner text.
- **Evidence:** `evidence/dyad/scripts/dyad_inbox_20261112_q3_deg2_check.py`, output in `evidence/dyad/inbox-20261112/` (exact, SymPy; the formula for s = 1…8 by symbolic composition; the vanishing for p = 6, 9, …, 30 by division by the cyclotomic polynomial; two controls). OWNER-RUN, SESSION.
- **Result:** no correction is asked of AZ. For the next Dyadic edition the owner may print the one-line formula at the RID entry; that is an edition decision, not made here.
- Answered by `pipes/AZ/20261112-DYAD-q3-deg2-cancel-owner-check.md`.

## 5. Recorded with this round: one prerequisite of a certification run

From the co-owner's read-back of W8 r2 (review `5877317450`, item 2); the owner agrees. In `arc_tail`, the threshold of the tail is computed with the lower bound of \|A₃\|. The condition \|x₀\| ≤ X_M is \|w\| ≥ \|A₃\|/X_M³, so the sufficient threshold uses the **upper** bound of \|A₃\|. The difference is the radius of the ball of A₃ and lies far inside the slack 10⁻¹² of the float bound, but that is not recorded as a checked inequality. It is not a numerical failure and W8 is not reopened; the change (one line) belongs to the frozen code of a certification run, if one is authorized. It is listed in the hand-over record §8.

## 6. State after this round

- `pipes/DYAD/`: 20 items, all closed. Open PR #183 would add one OFN finding.
- Outgoing, new: `pipes/LIT/20261112-DYAD-lh2012-use-report.md` (notice), `pipes/AZ/20261112-DYAD-q3-deg2-cancel-owner-check.md` (finding).
- OPEN 20, analytic branch: of the five conditions of the design, condition 1 is met at SESSION scope; the seed (Q1–Q3) is open; P4 is not written. Stage 3c-b is not authorized.
