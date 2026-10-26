# External Reviewer Briefing — N-5A-S1-INF

**Briefing ID:** `NG_N5AS1_INF_EXTERNAL_BRIEF_v1` · **Date:** 2026-08-28
**Prepared by:** Claude (RTG mathematical auditor) · **For:** external reviewer relay
**Canonical base:** `RTG_NUMBER_GENESIS_DSN_v1.10`

---

## §0. Scope — read this first

This briefing is deliberately **filtered**. It contains one self-contained mathematical problem and the literature that bears on it. It omits the surrounding research programme on purpose; that context is not needed and would dilute focus.

**In scope:** the three lemmas in §3, the structural observation in §4, the literature routes in §5.

**Out of scope — please do not address:**
- Any connection to the Riemann Hypothesis or zeta functions. A separate stream owns that material under an explicit forbidden-interpretation guard, and its current status is that the one observable tested was substrate geometry rather than dynamics. Zeta-flavoured suggestions will be discarded.
- Physical, ontological, or foundational interpretation. This is a dynamical-systems question here.
- Whether the constants below "are" real numbers in any foundational sense. They are chart-derived diagnostics and are guarded as such.

**Epistemic rules for the reply:** numerical agreement is not proof; please mark clearly which of your statements are theorems, which are standard-but-needs-citation, and which are conjecture. Citations should be checkable — we verify before importing. Negative results ("this route fails because…") are as valuable as positive ones.

---

## §1. The map

Fix the planar map

```
T(ρ, η) = ( ρ − sin η ,  η + (e^ρ − 1) − sin η ).
```

The origin is a fixed point. Its linearization is

```
J = [[1, −1], [1, 0]],     eigenvalues  λ± = exp(±iπ/3),     J⁶ = I.
```

The map is **not** area-preserving: `det DT = 1 + (e^ρ − 1) cos η`, which is `> 1` for `ρ > 0` near the origin. There is a critical curve at `ρ ≥ ln 2` (far from the region of interest).

**Established (verified symbolically):** `F := T⁶` is **tangent to the identity** at the origin, with `F − id` of leading total degree **3**.

Primary observable:

```
Q(ρ, η) = ρ² − ρη + η²
```

with `η` taken wrapped to `(−π, π]`.

## §2. What is already established

**(E1) Radial law.** `Q(Fx) − Q(x) = −Q(x)² + O(Q^{5/2})`, uniformly in phase, on a sufficiently small punctured neighbourhood; the degree-5 correction is known exactly with an explicit uniform bound. Consequently `Q_m ≈ 1/(m + κ)` along `F`-orbits.

**(E2) Angular law (in the increasing-lift convention).** With `Θ = atan2(√3 η_wrap, 2ρ − η_wrap)` and `φ` its continuous lift along an orbit, the six-step block satisfies

```
φ_{m+1} − φ_m = 2π − τ Q_m + r_m,     τ = 2√3/3.
```

The defect is a **lag**. Note this law is currently available only as a *cubic-vector truncation*; establishing it for the exact six-step iterate is Lemma L-PHASE below.

**(E3) Remainder exponent — corrected.** We initially proposed `|r_m| ≤ C Q_m²`. **That is false.** Measured over a 256-fold range of initial `Q`, `sup|r|/Q²` doubles for every fourfold decrease of `Q`, i.e. diverges. The stable bound is

```
|r_m| ≤ C Q_m^{3/2},     C ≈ 1.35,
```

with `sup|r|/Q^{3/2} ∈ [1.3449, 1.3565]` across that range. Half-powers of `Q` are odd powers of `|z|`, which is what one expects for a **real** (non-holomorphic) germ with anti-holomorphic resonant terms.

**(E4) Section events.** With `Σ = {Θ = 0}`, one has exactly `Θ = 0 ⟺ η_wrap = 0 and ρ > 0`. Section returns take `6` or `7` primitive steps. Over 4×10⁶ steps the 7-returns occur at steps 33 229, 198 242, 606 981, 1 619 416 — geometrically spaced, with successive ratios of `(M_k + κ)` equal to 2.4710, 2.4746, 2.4760.

**(E5) Two combination theorems (proved, conditional on §3).** With `D_M := 2πM − (φ_{6M} − φ_0) = τ Σ Q_m − Σ r_m`:
- *INF-1:* if `Σ Q_m = ∞` and `Σ|r_m| < ∞`, then `D_M → ∞`.
- *INF-2:* if the per-step lifted increment lies in `(0, 2π)`, then `N(M) = M − D_M/(2π) + O(1)` where `N(M)` counts section crossings in `6M` steps. An eventually-constant return gap `m₀` forces `m₀ = 6` and `D_M = O(1)`, contradicting INF-1. Hence infinitely many non-6 returns.

So the entire remaining question is the three lemmas.

## §3. The ask — three lemmas

**L-BACKBONE.** From (E1), prove `Q_m ≥ c/(m + κ)` for suitable `c, κ` on a declared neighbourhood; hence `Σ Q_m = ∞` and `Σ Q_m² < ∞`. Sketch we have: `|ΔQ + Q²| ≤ K Q^{5/2}` gives `1/Q_{m+1} − 1/Q_m = 1 + O(Q_m^{1/2})`, so `1/Q_M = 1/Q_0 + M + O(Σ Q^{1/2}) = M(1 + o(1))` since `Σ m^{-1/2} = o(M)`. *We believe this is essentially complete; we want it checked and made uniform.*

**L-MONO.** Prove the per-primitive-step lifted angular increment lies strictly in `(0, 2π)` on a declared neighbourhood (observed range `[1.0371, 1.0571]` about `π/3`). Expected route: fixed rotation sense from the `exp(±iπ/3)` linearization plus smallness.

**L-PHASE.** Prove (E2) with `|r_m| ≤ C Q_m^{3/2}` for the **exact** six-step iterate, not the cubic truncation. *This is the substantive one.*

## §4. A structural observation that may help

Asking what `Q` is invariant under gives an exact answer, verified symbolically:

- `Q` is **exactly** `J`-invariant, and is the **unique** invariant quadratic form up to scale (the invariant family is one-parameter). The Euclidean form is not invariant; its defect is `ρ(ρ − 2η)`. So `Q` is the Eisenstein/hexagonal norm form belonging to `λ = exp(±iπ/3)`.
- With Gram matrix `g = [[1, −½], [−½, 1]]`, `det g = 3/4`, and then **`τ = 2√3/3 = 1/√(det g)`** exactly. The shear constant is the volume normalisation of the invariant form.
- Hence the observed slip ratio has the closed form `exp(π/(3τ)) = exp(√3 π/6) = 2.476632271…`, against measured 2.4710 → 2.4746 → 2.4760.

**Question this raises:** is `√3π/6` (equivalently `π/√12`) the *iterative residue* / Fatou-coordinate logarithmic coefficient of `F`? See §5.1 — if so, L-PHASE and the geometric slip law may both come from one computation.

## §5. Literature map — where to look, and where not to

### §5.1 Primary route: parabolic germs and Fatou coordinates

Because `F = T⁶` is tangent to the identity with cubic leading term, it belongs to the classical **parabolic** class. For `z ↦ z + a z^{k+1} + …` the orbits satisfy `|z_n| ~ n^{-1/k}`; our `Q_m ~ 1/m` means `|z| ~ m^{-1/2}`, i.e. `k = 2`, the cubic case — consistent with the verified degree-3 leading term.

The decisive fact: **the Fatou coordinate of a parabolic germ contains a logarithmic term**, whose coefficient is the *iterative residue* (résidu itératif). Our logarithmic phase drift is, we suspect, exactly that term. Relevant: the Leau–Fatou flower theorem; Fatou-coordinate normalisation; Écalle–Voronin classification of parabolic germs; and for the **real, non-holomorphic** setting, Takens' normal-form theorem approximating a map near a resonant fixed point by the time-one flow of a vector field with controlled remainder. Takens is likely the right vehicle for L-PHASE, since it directly supplies the vector-field approximation whose remainder bound we need — and the half-power structure in (E3) is the signature of the real/anti-holomorphic resonant terms that a purely holomorphic treatment would miss.

**Specific question:** does the Takens/Fatou machinery give a remainder bound of exactly order `Q^{3/2}` (odd order in `|z|`) for a real germ with `Z₆` resonant symmetry, or does it give `Q²` with our measured `3/2` coming from something else?

### §5.2 Secondary: strong vs weak resonance

Eigenvalues at a primitive 6th root of unity sit at the boundary of Arnold's classification of resonances (orders `q ≤ 4` strong, `q ≥ 5` weak). The `q = 6` case is the marginal one and is treated specially in the bifurcation literature. Worth checking whether the `Z₆` resonant monomial structure explains the `3/2` exponent.

### §5.3 Discrepancy, not Sturmian coding

Our statement `N(M) = M − D_M/(2π) + O(1)` with `D_M → ∞` is a **discrepancy** statement: unbounded deviation from the mean count. Related classical material: Weyl equidistribution, Ostrowski representation, the three-distance theorem, and Kesten's bounded-remainder theorem.

**But note the disanalogy, which we consider important.** All of that theory assumes a *fixed* rotation number. Ours drifts logarithmically toward `1/6` and is never equal to it. Sturmian coding and three-distance results therefore do **not** apply off the shelf, and we have already made one error of exactly this type (inferring asymptotic structure from a finite horizon). What we would value is a pointer to work on **rotations with slowly varying / drifting frequency**, or non-autonomous circle maps, if such a literature exists in usable form. If it does not, say so.

### §5.4 Beyond Riemann on the conceptual side (lower priority, but genuinely relevant)

Riemann's 1854 *Habilitationsvortrag* distinguishes discrete from continuous manifolds and argues that in the discrete case measure comes from **counting**, whereas in the continuous case the ground of the metric relations must be sought outside the manifold. Two lines went beyond this in directions that match our structure:

- **Weyl (1918), purely infinitesimal geometry.** Weyl replaced Riemann's primitive metric with *relative* length comparison and a length connection; the holonomy of length transport around a loop is `exp(∮A)`, and the "Weyl-integrable" case is exactly `A = dφ`. This is formally identical to a multiplicative recurrence-ratio holonomy with a node-potential null case — which is a structure we already have in certified form. Einstein's second-clock objection is part of the record and should be read alongside it.
- **Causal set theory** (Bombelli–Lee–Meyer–Sorkin 1987; Malament 1977 on causal order determining conformal structure). The programmatic slogan "order plus number equals geometry" is close to our architecture, where counting and order are separately certified before any metric statement. The disanalogy: causal sets presuppose a discrete substrate and Lorentzian signature; we do neither.

For the "reals classify relations rather than being constructed from rationals" direction, the Eudoxus/Schanuel–Arthan construction of `ℝ` from almost-homomorphisms of `ℤ` is the relevant technical object.

## §6. What we most want, ranked

1. **L-PHASE via Takens or Fatou coordinates** — a remainder bound for the exact six-step map, with the correct exponent. This is the bottleneck.
2. **Confirmation or refutation** that `√3π/6` is the iterative residue / log-coefficient of `F`. A positive answer would likely yield the geometric slip law as a theorem rather than a numerical pattern.
3. **L-BACKBONE checked** and made uniform (we think it is nearly done).
4. **L-MONO** (small; expected routine).
5. Pointers on **drifting-rotation-number discrepancy**, or a clear statement that no usable theory exists.

## §7. Reference-verification note

All citations in §5 are given from standard knowledge and have **not** been re-verified against sources in preparing this brief. Please supply precise references (author, year, statement number) for anything you rely on; we verify independently before importing anything into our record.
