# DYAD OPEN 20 — analytic branch (O20-an): scope note for B-an and B-6 (SESSION v0.1)

**Version:** v0.1 · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Authorization.** PI decision of 20 Oct 2026. Approved:
- a SESSION scope study for the analytic branch of OPEN 20, priority B-an, then B-6;
- items [LIT], [ALG], [NUM] design and [OPEN] criteria;
- the explicit pre-check of whether B-an and B-6 are coupled.

The approval covers **only** this scope note and the computation design. Running the large coefficient campaign and adopting any new result are separate decisions.

**Status.**
- `[SESSION]` scope record. Nothing here is adopted.
- DYAD v6.4.18 is unchanged and its §6.17 C^∞ result (`DYAD-THM-SMOOTH-EMBEDDING`) is kept as is.
- No analytic convergence or divergence result is assumed or claimed.
- OPEN 20 stays PARTIAL; B-an and B-6 stay OPEN.
- N14 not yet sent; it stays PENDING.

**Pilot script.** `dyad_open20_an_formal_roots_pilot.py`, SHA-256 `ff3a970565406ff0e0b1e5b694b58fdc2bf8c8c7b510f1d277a91b268ae46376`.
- 7 gates and 3 negative controls; exact rationals; runs locally in seconds.
- Output for N = 15: `an_pilot_N15.json` (`7fb1c97d3a6036afd06239659cec97a2c249735a0cc71d6c046f7781e8076822`).
- The pilot validates the coefficient algorithm only. It makes no growth statement.

## 1. Objects and fixed conventions

**Coordinates.** The primitive coordinates are (ρ, η), lifted; T has rational Taylor coefficients in them. The raw frame W = ρ − η/2 + i(√3/2)η (§1, §6.14) is used only for statements that are naturally complex. The two coordinate systems differ by a fixed real linear map, so convergence questions are identical in both.

**Maps.**
- F = T⁶ is real-analytic. T is entire on ℂ², so F is too.
- F is tangent to the identity at P₁, with j²F = id and cubic part μ|W|²W, μ = −½ − (2√3/3)i (DYAD-THM-C21).

**Formal objects** (§6.16):
- X̂ = log F, the unique formal tangent-to-identity generator, with j²X̂ = 0;
- for s ∈ ℝ, F^s := exp(sX̂) as a formal series;
- F^{1/2}, F^{1/3} and F^{1/6} are tangent to the identity;
- R₀ = T³∘F^{−1/2} and J = T∘F^{−1/6}.

**Questions, as registered in v6.4.18:**
- B-an: does F^{1/2} converge (equivalently R₀)?
- B-6: does F^{1/6} converge (equivalently J, or an exactly λ-equivariant analytic chart)?
- B-3: does F^{1/3} converge? It is a sub-item of the B-6 equivalence.

**Category.** "Converges" means the formal power series has a positive radius of convergence at 0. A real series converges iff its complexification does, so the real and complex questions coincide.

## 2. Owner theorems and RID dependencies

| Used as | RID / location | Grade |
|---|---|---|
| Definition of T, F | DYAD-DEF-PRIMITIVE-MAP | `[DEF]` |
| Cubic term, μ | DYAD-THM-C21 | `[THM]` |
| X̂, formal centralizer {exp(sX̂)} | DYAD-THM-FORMAL-CENTRALIZER, DYAD-ALG-CENT-KERNEL | `[THM]`, `[ALG]` |
| R₀ unique formal involution | DYAD-THM-FORMAL-INVOLUTION-UNIQUE | `[THM]` |
| J, B-6 hierarchy (B-6 ⟺ B-an ∧ B-3) | DYAD-THM-FORMAL-Z6-GENERATOR; §6.16 hierarchy `[ALG]` | `[THM]`, `[ALG]` |
| Analytic involution ⇒ RT = TR | DYAD-THM-ANALYTIC-CLOCK-BRIDGE | `[THM — analytic]` |
| C^∞ embedding and C^∞ roots | DYAD-THM-SMOOTH-EMBEDDING (v6.4.18) | `[THM]`, C^∞ germ scope — **not** an input to any analytic statement |
| Raw six-step coefficients c₃₂, c₀₅ | §6.9 (raw values, operation-independent per SG-19) | `[ALG]` |

**Guards:**
- SG-19: no transfer between normalization operations.
- SG-14/15: no physical reading.
- The C^∞ existence result gives no information about convergence (v6.4.18 §6.17, distinction vi).

## 3. [LIT] Literature audit

Status: first pass, sources read through abstracts or summaries. Each item is classified as directly applicable or not.

**L1. One variable, Baker (1964).** I. N. Baker, "Fractional iteration near a fixpoint of multiplier 1", *J. Austral. Math. Soc.* 4 (1964) 143–148.
- For f(z) = z + … in one complex variable, the formal iterates f_s satisfy f_s∘f_t = f_{s+t} and have coefficients polynomial in s.
- The set 𝔅 of s for which f_s converges is the whole plane, a one-dimensional lattice {ns₁}, or a two-dimensional lattice.
- For meromorphic f, extending Szekeres's theorem for entire and rational f, 𝔅 is the whole plane only for a special form (Möbius-type).
- **Applicability:** one complex variable only. F is a real-analytic map of ℝ² whose complexification is a germ of ℂ², not of ℂ. The lattice structure of 𝔅 is the 1D template for §4.

**L2. One variable, Écalle–Voronin.** Classification of parabolic germs of (ℂ, 0) by sectorial normalizations. Embeddability in an analytic flow, and analytic roots, are governed by the moduli; generic germs do not embed.
- **Applicability:** one variable; holomorphic. Not assumed applicable to F, as the PI condition requires.
- The antiholomorphic parabolic germs of Godin–Rousseau (codimension k) are germs z ↦ z̄ + … of one complex variable. That is a different object from our real 2D germ.

**L3. Several variables, Ribón.** J. Ribón, "Non-embeddability of general unipotent diffeomorphisms up to formal conjugacy", *Ann. Inst. Fourier* 59 (2009).
- There are unipotent germs of (ℂ², 0) whose **formal class** is non-embeddable, i.e. log φ is not formally conjugate to any convergent vector field.
- Within the studied affine families this is "clearly the generic situation".
- The proof is constructive, through polynomial families and potential theory. It covers a specific family and does not address F.
- **Applicability:** confirms that divergence is the typical behaviour in ℂ². It gives no statement about our F and no criterion we can check.
- The notion used there (formal class embeddable) is **weaker** than ours: B-an asks for convergence of exp(½X̂) itself, not of a conjugate.

**L4. Parabolic germs of ℂ² with degenerate characteristic directions.** Hakim; Abate (2001, index theorem and parabolic curves); Abate–Tovena (Fuchsian, irregular and apparent degenerate directions); Molino; Vivas (arXiv:1106.1471, basins along degenerate directions).
- **Relevance:** §5.3 shows that every characteristic direction of the complexified F is degenerate. This literature describes parabolic curves and basins: geometric objects on which a divergence argument might be built.
- **Applicability:** dynamics of germs, not embeddability. The classification of our directions against the Abate–Tovena definitions is still to be checked (§5.3).

**L5. Not found** in accessible sources:
- a theorem deciding analytic embeddability, or convergence of a specific fractional iterate, for a real-analytic tangent-to-identity germ of ℝ² with cubic part μ|W|²W, μ ∉ ℝ;
- a Baker-type lattice theorem for the set S of §4 in dimension 2;
- an analogue of the Szekeres–Baker "entire map" argument for entire maps of ℂ².

"Not found" does not mean such results do not exist. A deeper search (Ilyashenko–Yakovenko, Martinet–Ramis, Rousseau, Ribón's later papers, Écalle's resurgence in several variables) is a P1-b item.

## 4. Pre-check: are B-an and B-6 coupled?

### 4.1 Lemma S

`[THM — SESSION, elementary; proposed]`

Let S := {s ∈ ℝ : exp(sX̂) converges}. Then:
- **(i)** S is an additive subgroup of ℝ containing ℤ.
- **(ii)** B-an ⟺ ½ ∈ S; B-3 ⟺ ⅓ ∈ S; B-6 ⟺ ⅙ ∈ S.
- **(iii)** Hence B-6 ⟺ (½ ∈ S and ⅓ ∈ S), because ⅙ = ½ − ⅓ while ½ = 3·⅙ and ⅓ = 2·⅙. This recovers the adopted hierarchy (B-6 ⟺ B-an ∧ B-3) by a one-line argument.
- **(iv)** If S is discrete, then S = (1/q)ℤ for a unique integer q ≥ 1. In that case B-an ⟺ 2 | q and B-6 ⟺ 6 | q.
- **(v)** If X̂ converges, then S = ℝ.

*Proof.*
- (i) n ∈ S for n ∈ ℤ, since Fⁿ is analytic and equals exp(nX̂) formally.
- If s, t ∈ S, then exp(sX̂)∘exp(tX̂) converges, as a composition of convergent tangent-to-identity series. It equals exp((s + t)X̂) formally.
- The inverse of a convergent tangent-to-identity series converges (inverse function theorem). It equals exp(−sX̂).
- (ii)–(iii) restate the definitions and the group property. (iv) is the structure of discrete subgroups of ℝ. (v) holds because the time-s map of an analytic field is analytic. ∎

### 4.2 What is not known

- Whether S is closed in ℝ, or whether S dense implies S = ℝ.
  - In one variable Baker obtains the trichotomy from the polynomial dependence of the coefficients on s together with one-variable complex analysis.
  - For dimension 2 a corresponding theorem was not found (L5).
- Whether S = ℝ implies that X̂ converges.

### 4.3 Coupling of B-an and B-6

- Lemma S couples B-an and B-6 only through the group S.
- It does **not** force B-an ⟹ B-6: S = (1/2)ℤ is consistent with B-an true and B-6 false.
- The 1D analogue shows this is a real possibility. For g(z) = e^z − 1 and f = g∘g, the half-iterate f^{1/2} = g converges, while the standard account (Baker 1958, *Math. Z.* 69, not read directly here) states that g has no convergent fractional iterates other than the integer ones. So f has 𝔅 ⊇ ½ℤ with log f divergent.
- Analytic T gives no element of S, because T is not tangent to the identity. The relation J = T∘F^{−1/6} only re-expresses B-6.

**Decision, as the PI requires:** B-an and B-6 keep separate records. The only coupling recorded is Lemma S (proposed), and it adds nothing beyond the adopted B-6 ⟺ B-an ∧ B-3. No further equivalence is claimed.

## 5. [ALG] Formal coefficients: definitions, algorithm, pilot

### 5.1 Algorithm (exact, primitive coordinates)

1. **Jets.** Degree-N jets of T from the rational Taylor series of sin and exp − 1. F = T⁶ by truncated composition.
2. **Formal logarithm.** Mercator series of the composition operator, X̂(u) = Σ_{k≥1} (−1)^{k+1}/k · (F* − I)^k u for u ∈ {ρ, η}.
   - F* − I raises the order by at least 2, so the series stops after about (N − 1)/2 terms at truncation N.
   - Alternative, for the campaign: degree-by-degree solution of the Julia equation DF·X̂ = X̂∘F. It is uniquely solvable from degree 4 on because ker ad_{X̂₃} ∩ 𝔛_k = 0 for k ≠ 3 (Lemma K).
3. **Fractional iterates.** F^s = exp(sX̂) by the Lie series Σ_k s^k/k! · L_{X̂}^k u. L_{X̂} raises the order by at least 2.
4. **Derived objects.** R₀ = T³∘F^{−1/2} and J = T∘F^{−1/6} by composition.

### 5.2 Pilot gates

All gates passed for N = 7, 9, 11, 13 and 15:

| Gate | Check | Result |
|---|---|---|
| A1 | exp(X̂) = F through degree N | PASS |
| A2 | (F^{1/6})⁶ = F, (F^{1/2})² = F | PASS |
| A3 | R₀² = id, DR₀(0) = −I, R₀T = TR₀ (Corollary U) | PASS |
| A4 | J⁶ = id, JT = TJ, DJ(0) = A (DYAD-THM-FORMAL-Z6-GENERATOR) | PASS |
| A5 | j²X̂ = 0; cubic part of X̂ in W equals μ\|W\|²W | PASS |
| A6 | raw [F]_{(3,2)} = −77/216 + 97i√3/648 and [F]_{(0,5)} = −61/2160 − 43i√3/6480 (adopted §6.9 values) | PASS |
| A7 | log(F^{1/6}) computed independently equals X̂/6 | PASS |

**Negative controls.** All fail as required:
- M1: Mercator series with the k = 2 sign flipped;
- M2: R₀ built with F^{−1/3};
- M3: conjugated c₀₅.

So the coefficient generation agrees with the adopted jets and the adopted formal identities.

**Cost of the pilot.**

| N | Total time (gates included) | Max denominator of X̂ |
|---|---|---|
| 11 | 3.1 s | 27 bits |
| 13 | 6.0 s | 36 bits |
| 15 | 13.4 s | 44 bits |

- The gate compositions dominate the run time. Generating F, X̂ and the roots alone took 2.4 s at N = 15.
- `[NUM — pilot]` The ℓ¹ norms per degree in (ρ, η) are recorded in the JSON for campaign design only.
- These norms include the geometric growth that every convergent series with finite radius shows; F itself grows that way. At N ≤ 15 they carry **no** information on convergence, and none is drawn.

### 5.3 Complexified cubic structure

`[ALG]`

**Characteristic directions.**
- In complex coordinates (z, w) with w = z̄ on the real plane, the cubic part of the complexified F is P₃ = (μz²w, μ̄zw²).
- A direction v is characteristic if P₃(v) = λv. Taking zw ≠ 0 would force μ = μ̄, contradicting Im μ ≠ 0.
- So the only characteristic directions are [1:0] and [0:1]. P₃ vanishes on both, so they are **degenerate** (λ = 0).

**Blow-up data at [1:0].** With u = w/z:
- p₃(1, u) = μu, of order 1;
- r(1, u) = (μ̄ − μ)u², of order 2.

The type of these directions (Fuchsian, irregular or apparent) under the Abate–Tovena definitions is to be checked from the original definitions in P1-b. The results of Hakim (non-degenerate case) therefore do not apply directly.

The orders above are a simple computation. Its consequences are `[HEUR]`.

## 6. [NUM] Campaign design

Running it is a separate decision. Compute-heavy work runs on the PI's Windows/PowerShell machine.

### 6.1 Arithmetic tiers

- **Exact core:** truncation N_ex ≈ 25–31 with exact rationals. The planned implementation is python-flint `fmpq_mpoly`, or the pilot code with dense arrays.
  - Purpose: exact X̂, F^{1/2}, F^{1/3}, F^{1/6}.
  - Records per degree: denominators and height growth.
- **Ball tier:** truncation N_b ≈ 60–120, floating-point balls (python-flint `arb`, precision adapted so that every coefficient carries a certified radius).
  - Each reported coefficient norm then has a rigorous enclosure, so the numbers are certified.
  - Their growth interpretation remains `[NUM]`.
- **Cost model:**
  - The pilot scales roughly ×2 per +2 degrees with the gates included, so the exact tier is expected to stay below hours for N_ex ≈ 25.
  - A measured cost table (seconds, memory, coefficient bit sizes per N) is a deliverable of the first campaign run.
  - The run uses exit-coded stops (PowerShell runner, as for P5).

### 6.2 Diagnostics

For each degree d and each object Y ∈ {X̂, F^{1/2}, F^{1/3}, F^{1/6}}:
- the norms ‖Y_d‖ (max-modulus in the W frame and ℓ¹ in (ρ, η));
- the root test ‖Y_d‖^{1/d}, which stays bounded for a convergent series;
- the factorial test: a fit of log‖Y_d‖ ≈ (d/κ)·log d + βd + c.
  - A stable κ would indicate Gevrey-type growth of order 1/κ.
  - For a germ with cubic tangency the 1D analogue suggests κ ≈ 2 (`[HEUR]`).
- the ratio ‖Y_d‖/‖F_d‖ against the convergent baseline F;
- parity splitting (even and odd d) and the harmonic channel (a − b mod 6 in W) per degree.
  - This guards against cancellations that hide growth in a single norm.

### 6.3 Independent controls

Each control must be run through the **same** code path.

| # | Control | Expected (basis) | Purpose |
|---|---|---|---|
| C1 | F, T themselves | convergent (analytic) | geometric baseline |
| C2 | z/(1 − z) = exp(z²∂_z) | log = z² exactly | algorithm recovers a finite log |
| C3 | 2D: time-one map of a polynomial field (e.g. μ\|W\|²W plus a chosen quartic) | log = that polynomial | exactness in 2D |
| C4 | g(z) = e^z − 1 | log divergent (Baker 1958 / Szekeres–Baker, citation to verify) | known divergent behaviour |
| C5 | f = g∘g | f^{1/2} = g convergent, log f divergent | the diagnostic must separate a convergent root from a divergent log, i.e. B-an from B-∞ |
| C6 | f = g^{∘6} | f^{1/6} convergent, f^{1/2} = g³ convergent | B-6-type positive control |

**Negative controls** (planted defects that must flip the verdict of a gate):
- a perturbed Mercator coefficient;
- truncation-order mismatch;
- a wrong frame map;
- a ball tier run at too low precision. Ball widths must exceed the reported digits, and the run must stop with an exit code.

### 6.4 Reading rules

Recorded now, before any data:
- No campaign outcome is a convergence or divergence proof.
- "Geometric-looking" growth up to N_b is reported as "no factorial growth detected up to N_b", never as convergence.
- "Factorial-looking" growth is reported as "growth consistent with Gevrey order 1/κ", never as divergence.
- Disagreement between the W and (ρ, η) norms, or between the parity channels, is reported as such.
- Results for X̂, F^{1/2} and F^{1/6} are reported separately, in line with §4.

## 7. [OPEN] Decision criteria and proof obligations

### 7.1 Positive closure

B-an positive (resp. B-6 positive) requires a **mathematical** construction of an analytic germ, either:
- (a) a convergence proof for exp(½X̂) (resp. exp(⅙X̂)), e.g. by majorants; or
- (b) an analytic involution R with DR(0) = −I commuting with F (resp. an analytic J with J⁶ = id, DJ(0) = A, JT = TJ).

By DYAD-THM-ANALYTIC-CLOCK-BRIDGE and the uniqueness of R₀, such an R equals R₀.

### 7.2 Negative closure

Negative closure requires a proof that the formal root diverges. Candidate routes, all `[HEUR]` and none established:
- **(N1) Invariant-curve reduction.** Find an F-invariant analytic curve (e.g. a parabolic curve of Abate type along a degenerate direction, §5.3) on which F restricts to a one-variable parabolic germ with checkable Écalle–Voronin data.
  - It must also be shown that an analytic F^{1/2} would restrict to that curve. This is **not** automatic and is itself an obligation.
- **(N2) Global, Szekeres–Baker type.** Use that F = T⁶ is entire on ℂ²: if F^{1/2} converged, analytic continuation would be constrained globally. No two-variable theorem of this kind was found (L5).
- **(N3) Sectorial obstruction.** Construct sectorial normalizations near the degenerate directions and exhibit a nontrivial modulus incompatible with ½ ∈ S. This is a research programme, not a short proof.

### 7.3 Other obligations

- **Lemma S** (§4) should be reviewed before it is used anywhere. It is elementary but new as a recorded statement.
- **Abate–Tovena type** of the degenerate directions (§5.3), from the original definitions.
- **Literature P1-b:** a deeper search on the items listed in L5.

## 8. Proposed next steps

Each step needs its own decision.

| Step | Content | Needs |
|---|---|---|
| P1-b | Deeper literature (L5 list); classification of the degenerate directions; review of Lemma S | PI go-ahead |
| P2 | Campaign code: exact tier and ball tier; controls C1–C6; negative controls; PowerShell runner with exit-coded stops | PI go-ahead for the code; separate decision to run it at scale |
| P3 | Run on the PI machine; `[NUM]` report under the §6.4 rules | separate decision |
| P4 | Proof attempt on the more promising side (positive (a)/(b) or negative N1–N3) | after P1-b–P3 |

**Status:** DYAD v6.4.18 adopted; OPEN 20 PARTIAL; B-an and B-6 OPEN; N14 PENDING.

## Sources

- I. N. Baker, Fractional iteration near a fixpoint of multiplier 1, J. Austral. Math. Soc. 4 (1964): https://core-cms.cambridgecore.org/core/services/aop-cambridge-core/content/view/B0EE7D3E5945913D19E95C8530106421/S144678870002334Xa.pdf/fractional-iteration-near-a-fixpoint-of-multiplier-1.pdf
- J. Ribón, Non-embeddability of general unipotent diffeomorphisms up to formal conjugacy, Ann. Inst. Fourier 59 (2009): https://arxiv.org/pdf/0902.2985
- Degenerate characteristic directions for maps tangent to the identity (Vivas): https://arxiv.org/pdf/1106.1471
- Parabolic curves for diffeomorphisms in (ℂ², 0): https://arxiv.org/pdf/math/0611019
- Godin–Rousseau, analytic classification of parabolic antiholomorphic germs (one variable; recorded as not applicable): https://arxiv.org/pdf/2001.06428
- Baker 1958 (Math. Z. 69) and Szekeres: cited through the account in Baker 1964; originals not read here.
