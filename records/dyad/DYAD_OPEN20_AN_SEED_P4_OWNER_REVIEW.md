# DYAD OPEN 20 — Seed (Q1–Q3) and divergence step (P4): owner review of the co-owner's written argument

**By:** Claude, Dyadic DSN owner and math auditor. **Date:** 13 November 2026. **Status:** working record (SESSION). Not a theorem, not a certificate, not an adoption. **Governing edition:** `dyad-v6.4.24` (`10fbdacc…bc16`), unchanged.
**Reviewed:** `records/dyad/DYAD_OPEN20_AN_SEED_P4_COOWNER_ARGUMENT.md` at commit `def878f5` (draft PR #257, branch `chatgpt/dyad-open20-seed-p4-written-argument`), whole. **PI decision of 13 November 2026:** written work on Q1–Q3 and P4 is started; scope OPEN 20 analytic branch only; no new DSN theorem and no certification decision. B-an and B-6 stay ACTIVE; stage 3c-b is not authorized.

**Read against:** stage-3b design §3–§5 (`DYAD_OPEN20_AN_STAGE3B_DESIGN.md`); pilot design D1–D9; the library's τ and tube (`dyad_open20_an_stage3c_lib.py`); LIT's use check at rtg-lit `a3628d4`. The article was not read.

## 1. Verdict

The argument is **correct at its declared conditional scope, after one correction** (C-1). Three precisions (P-1 to P-3) make steps explicit that the draft uses silently; none changes a conclusion.

| Part | Verdict | Conditional on |
|---|---|---|
| Q1 (domain) | correct after C-1; the one numerical inequality is checked in ball arithmetic (§3) | the petal parameter δ of the theorem, which is existential |
| Q2 (tube) | correct; P-1 | L1 with C3 (literature, SESSION scope); the constant C_j is not computed and need not be |
| Q3 (invariance) | correct; P-2 | (G), (A) on the seed domain (development results of W3, W4) |
| P4 (divergence) | correct; P-3 | hypotheses (i)–(iv) of the draft, among them a certified point jump, which does not exist |

## 2. Correction C-1: the leading identity is not exact for the τ of the certificate

The draft uses "the exact leading-coefficient identity" 3A₃c³ = 1. That holds for A₃ = −1/(3ℓ₊), which is how the design (§3) writes A₃. But the τ that defines D₀, D₁ and the tubes in every run of stage 3c-a is the library's fixed explicit function, whose four coefficients are 15-digit decimals (`TAU_DECIMALS`: "the stage-2b values rounded to 15 digits. Nothing in the tube lemma requires them to solve the Abel equation"). The covers, the arc and the legs were all computed for the sets of this τ, and the owner's zone-I argument (proof record §6) is written for a general A₃. For this τ

- 3A₃c³ = 1 + e₃ with \|e₃\| ≤ 1.27·10⁻¹⁵ (ball arithmetic, §3), and e₃ ≠ 0.

So the identity reads 3ξ³τ = 1 + e₃ + 3A₂c²ξ + 3A₁cξ² + 3κξ³(log ξ − log c), and the draft's formulas change as follows:

- E(r) gains the constant term \|e₃\|: E(r) = \|e₃\| + a₂r + a₁r² + k₃r³(\|log r\| + \|log c\| + π/2), with a₂ = \|3A₂c²\|, a₁ = \|3A₁c\|, k₃ = 3\|κ\|.
- In (Q1.3) and in C_τ the leading term 1/3 becomes \|A₃c³\| = \|1 + e₃\|/3.
- "E(r) → 0" becomes "E(r) → \|e₃\|", which is far below sin(π/8); (Q1.2) stays satisfiable.

The correction is of size 10⁻¹⁵ and changes no conclusion. It has to be made because the seed must be a seed for the sets D_j of the runs, not for sets defined by the exact Fatou coefficient. The other route, redefining τ with the exact A₃, would change the objects of every run and is not proposed. **Owner's own item:** the proof record does not yet say in words that τ has the library's decimal coefficients; that sentence is added when the seed is folded in (§6).

## 3. Steps checked

**By hand.**
- *Identity and (Q1.1).* 3ξ³·A₂z⁻² = 3A₂c²ξ, 3ξ³·A₁z⁻¹ = 3A₁cξ², z = ξ/c. On both chart sectors −0.20π < arg ξ < 0.50π, so \|log ξ\| ≤ \|log r\| + π/2, and log z = log ξ − log c on the principal branches (design §3: arg z stays in (−0.512π, 0.188π)). From 3r³τ = (1 + e)e^{−3iθ} with \|e\| ≤ E(r): \|3r³Re τ − cos 3θ\| ≤ E(r).
- *Monotonicity.* r, r² and r³\|log r\| increase on (0, e^{−1/3}); the draft's range r ≤ 1/e is inside.
- *j = 0.* For 5π/24 ≤ θ < 3π/10: 5π/8 ≤ 3θ < 9π/10, so cos 3θ ≤ −sin(π/8), and (Q1.2) gives Re τ < s₀. The lower edge of the chart, −π/5, is inside the window (−π/5 > −5π/24).
- *j = 1.* For 0.03π < θ ≤ π/8: cos 3θ ≥ sin(π/8), and (Q1.2) gives Re τ > s₁. The upper edge π/2 is inside the window (π/2 < 13π/24).
- *Radial part.* On r₀ ≤ r < 0.60 each term of the bound of \|τ\| is largest at r₀, and \|h_j\| ≤ \|τ\|. So h_j > H > M(r₀) forces r < r₀.
- *Tube factors (design §3).* First factor ±(Re τ − s_j) + 1 ≤ \|τ\| + S + 1 ≤ C_B r⁻³ for r ≤ r₀; second factor h_j ≤ \|τ\| ≤ C_τ r⁻³; \|ξ^α\| ≥ r^{Re α}e^{−\|Im α\|π/2}. With q₁/3 = q₂/3 = 3: R_j ≥ K_j r^{18 + Re α}, and 18 − 102/19 = 240/19, 39 − 240/19 = 501/19.
- *P4.* The chain of the proof (convergent sum in the class on a small petal; uniqueness for F and for G in the chart of D5; equality near a tail point; identity theorem on U; contradiction with disjoint discs) is the design's §5 step 6, and agrees with the owner's disposition of LIT's use check (`DYAD_INBOX_20261112_OWNER_DISPOSITION.md` §1, in PR #254).

**In ball arithmetic** (`evidence/dyad/scripts/dyad_open20_an_seed_q1_check.py`, output and checksums in `evidence/dyad/open20-an/seed/`; 200 bits; exact constants of stage 1, the τ and the tubes of the library; OWNER-RUN, development, 9 seconds; a second run gave a byte-identical file). All six gates PASS; both controls exit 1 at the named gate.

| Quantity | Value |
|---|---|
| \|e₃\| | ≤ 1.27·10⁻¹⁵ |
| a₂, a₁, k₃, \|log c\|, S | ≤ 1.08403, 0.283002, 5.44152, 1.24855, 1.94331 |
| The bounds proposed in the draft (2, 2, 10, 3, 4) | hold |
| (Q1.2) at the draft's r₀ = 10⁻³ | left side 1.08·10⁻³ against sin(π/8) = 0.382683 |
| Largest r₀ on the grid k/200 at which (Q1.2) holds | **0.18** (left side 0.382187); it holds at every smaller grid value |
| M(r₀): the level must exceed | 77.06 at r₀ = 0.18; 2823.7 at 0.05; 3.34·10⁸ at 10⁻³ |
| C_τ, C_B at r₀ = 0.18 | 0.449395, 0.466561 |
| K₀, K₁ at r₀ = 0.18 (lower bounds) | 4.44·10⁻³, 1.26·10⁻² |

- *Independent sampling* (mpmath, own formulas; 8241 points per sector inside r ≤ r₀ and 12060 on the annulus): no violation of the bound E(r), of the angular window, of the two factor bounds, of R_j ≥ K_j r^{240/19}, or of \|τ\| ≤ M(r₀); 3384 samples lie in D₀ and 3655 in D₁.
- *Controls.* BIG (r₀ = 0.30): (Q1.2) fails, left side 1.0992. HALFE (the sampling compares with E/2): 16464 violations.
- So Q1 holds with **r₀ = 0.18 and any level H > 77.06**, as far as the explicit inequalities go. The seed radius is then the smallest of r₀, the petal size (κδ)^{1/3} and the radius r₁ of Q2; the last two are existential.

## 4. Precisions

- **P-1 (Q2, the unit of d).** By D9, φ_j(z) = z²(a₊ + b₁z + u_j(c₊z)), and φ_N(z)/z² = a₊ + b₁z + Σ_{n=2}^{38} b_n zⁿ (b_n = a_{n+2}). So d_j(ξ) = u_j(ξ) − Σ_{n=2}^{38} b_n zⁿ **exactly**: the lifted deviation is u_j minus the truncation of its own asymptotic series at order 38. No transport of an asymptotic statement between charts is needed, and (Q2.2) is L1 at order 38. Also: ε differs for the two tubes (ε₀ ≠ ε₁), so the constant of (Q2.1) is K_j.
- **P-2 (Q3, wording).** (A1) gives h_j(τ(ξ′)) ≥ h_j(τ(ξ)) + σ > H; with (G) and (A2) this is ξ′ ∈ D_j(H). The set D_j(h_j(τ(ξ)) + σ) of the draft is defined with a strict inequality and need not contain ξ′.
- **P-3 (P4, the tail point lies in both seed domains).** The proof applies φ_j = u_j at a tail point; that identity holds on D_j(H_seed) only. The missing line is the design's §3: on the arc, Re τ = Re τ* lies strictly between s₀ and s₁, and h₀ = Re τ*·cos θ₀ + t sin θ₀, h₁ = −Re τ*·cos θ₀ + t sin θ₀ both tend to +∞. With the arc inside both chart sectors (hypothesis (ii)), γ(t) ∈ D₀(H) ∩ D₁(H) for every H and all large t.

## 5. What the argument establishes, and what stays open

- **Established as a written argument (SESSION):** the seed (Q) follows from L1 (with C3), from (G) and (A) on the seed domain, and from explicit inequalities that are now checked. P4 follows from (i)–(iv).
- **Q1** no longer has an open quantitative step except the existential petal size. Obligation P9 of the design (an explicit bound for the O(ξ) term) is met by (Q1.1)–(Q1.3) with the numbers of §3, at development level.
- **Still conditional or open:**
  1. L1 and L3 are LIT-checked uses at SESSION scope; LIT has not re-proved Proposition 5.3; the owner has not read the article. Nothing here is a theorem-grade import.
  2. (G), (A), (B) are development results (W3, W4, W7, W8). The seed domain lies in zone I once H is large; nothing new was run for it.
  3. The ball check of §3 is OWNER-RUN, development. REVIEWER-REPLAYED: none.
  4. P4 needs a certified point jump. None exists; stage 3c-b is not authorized. The prerequisite on t_M (hand-over record §8) stands.
  5. Neither the seed nor P4 decides B-an or B-6 (DSN §2, OPEN 20).
- **State of the design's conditions, proposed for the hand-over record once this is merged:** condition 2 (the seed) — *written, conditional on L1 at SESSION scope and on the tube hypotheses*; P4 — *written, conditional*. Neither is "proved".

## 6. Recommendation

1. **PR #257:** the co-owner applies C-1 and P-1 to P-3 to the draft; it can then be merged as a working record. The owner has no other objection.
2. **After #254 and #257 are merged:** the owner folds the seed and P4 into the proof record of stage 3c-a (§11) and updates the hand-over record §5 and the entry note. Not done here, to keep this branch free of conflicts with PR #254.
3. **No further step is implied.** Whether to authorize a certification run remains the PI's decision; with the seed written, what separates the present state from a claim is the certification run itself with an independent replay, and the scope of the literature inputs.
