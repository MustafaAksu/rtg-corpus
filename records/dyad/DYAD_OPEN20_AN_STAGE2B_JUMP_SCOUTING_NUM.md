# DYAD OPEN 20 analytic branch — stage 2b: `[NUM]` scouting of the sectorial jump

**Date:** 11 November 2026. **By:** Claude, Dyadic DSN owner. **Run:** OWNER-RUN (Linux container, Python 3.13, mpmath 1.3.0).
**Authorization:** PI, 11 November 2026 (in session: "evet aşama 2b'yi yetkilendiriyorum"), for the scope of the pilot design record §9, item 1.
**Status of every number below:** `[NUM]` scouting. Not a certificate and not theorem evidence. No error bound is proved. Nothing here changes a DSN statement, a grade, a RID or an OPEN status. B-an and B-6 stay ACTIVE. Stage 3c is not authorized.

## 0. Outcome in one paragraph

On the pilot branch Γ₊ of F = T⁶, the two sectorial values of the curve at a common point of the overlap S₀ ∩ S₁ were computed directly from the full map, at ten points ξ* on arg ξ = π/6 with 0.24 ≤ \|ξ*\| ≤ 0.45. They differ. The jump ΔY = (φ₁ − φ₀)/z*² ranges from 1.6·10⁻⁵ at \|ξ*\| = 0.45 to 7.3·10⁻⁵⁰ at 0.24. It is reproduced across changes of truncation order, matching radius and precision to between 33 and 79 significant digits. A control map with an exactly zero jump returns 10⁻¹⁶⁰. Measured against the Fatou time of the restricted map, the jump decays like exp(−2πT): the local slope is −2π·(0.984 … 0.9988), rising monotonically toward −2π as \|ξ*\| decreases. Numerically, the formal branch does not look convergent. This is scouting, not a proof.

## 1. What was computed

Notation as in the pilot design (D1–D9): w = φ(z) on the branch a_pil (Im a > 0); ξ = c₊z; forward orbits tend to 0 along arg ξ = 0 (sector S₀), backward orbits along arg ξ = π/3 (sector S₁); ξ* = r·e^{iπ/6}, z* = ξ*/c₊.

- **φ₁(z*)**, the curve of S₁ at z*. Take a point z₀ of small \|ξ\| near arg ξ = π/3 on the truncated series, and iterate the full map forward n steps. z₀ is adjusted by a secant iteration until the z-coordinate after n steps is exactly z*. The w-coordinate there is φ₁(z*). Forward iteration contracts transversally along S₁, so the truncation error at the start shrinks.
- **φ₀(z*)**, the curve of S₀ at z*. It is the w for which the forward orbit of (z*, w), after n steps, lies on the truncated series at small \|ξ\| near arg ξ = 0. It is found by Newton iteration on w. Forward iteration expands transversally here (amplification 12 to 180 over the leg), so the condition fixes w sharply.
- **Δ(z*) = φ₁(z*) − φ₀(z*)** is the jump of design D9 on the overlap of S₀ and S₁, at one common point. ΔY = Δ/z*² is the same difference in the lifted coordinate.

Only forward iteration of the full map is used; no inverse map and no jet. The truncated series enters only at the start and at the matching point, at \|ξ\| ≈ r_m ≤ 0.12, where its terms are far below the accuracy of the stored coefficients (80 digits). If Γ̂₊ converged, φ₀ and φ₁ would be one analytic function and Δ would vanish.

**Inputs.** The stage-2 coefficients a₂…a₂₁₆ (`evidence/dyad/open20-an/stage2/scout_N216_dps840.json`, SHA-256 `6ca8c663…477e`) and the map T.

## 2. Package

| File | Role |
|---|---|
| `evidence/dyad/scripts/dyad_open20_an_stage2b_jump_scout.py` | the measurement, the stability matrix, the zero-jump control, gates |
| `evidence/dyad/scripts/dyad_open20_an_stage2b_law.py` | formal Fatou coordinate of the restricted map; decay law in Fatou time |
| `evidence/dyad/open20-an/stage2b/run.sh` | runs both and the two negative controls; enforces the exit codes |
| `evidence/dyad/open20-an/stage2b/` | outputs and `SHA256SUMS.txt` |

**Configurations.** Base: N = 216, r_m = 0.10, 160 digits. Variations, each hitting the same z*: r_m = 0.08; r_m = 0.12; N = 144; 230 digits.

**Gates (all PASS):**
- G0: input hash.
- G_ORBIT: no orbit leaves the neighbourhood of 0.
- G_ON: map and series agree on the first three steps (residual 3·10⁻⁸², the coefficient accuracy).
- G_SEC, G_NEWTON: both iterations converged.
- G_STAB: the jump agrees across the five configurations to 10⁻⁶ relative (observed: far better, §3).
- G_ZERO: the control with zero jump returns \|ΔY\| < 10⁻¹¹⁰ (observed 10⁻¹⁶⁰).

**Zero-jump control.** The time-one map of the vector field ξ′ = −ξ⁴, Y′ = −αξ³Y + ξ⁵, with the same k = 3 and the same α. Its invariant curve Y = ξ²/(α − 2) is a polynomial, so its jump is exactly zero. The same harness is applied to it.

**Negative controls (each exits 1 at the named gates):**
- SHIFTCOEF: a₅ changed by 10⁻²⁰ relative. Fails G_ON and G_STAB.
- WRONGMAP: sin η in the second component of T multiplied by 1 + 10⁻²⁰. Fails G_ON and G_STAB.

**Law script gates (all PASS):** L1 restricted map f = z + ℓz⁴ + … to 10⁻³⁰; L2 Abel defect 1.2·10⁻¹⁸ on an orbit point; L3 the times read from the S₀ side and from the S₁ side agree; L4 slopes within a wide sanity band.

Owner timing: about 19 minutes for the whole `run.sh` (matrix about 11, controls about 5, law about 2.5). `jump_scout.json` records its own run time, so its bytes differ between runs; the numbers do not.

## 3. Results

| \|ξ*\| | \|ΔY\| | relative spread across configurations | T_model = 1/(3\|ξ*\|³) | T_true (Fatou time) |
|---|---|---|---|---|
| 0.45 | 1.632225·10⁻⁵ | 7·10⁻⁸⁰ | 3.658 | 2.627 |
| 0.42 | 4.504299·10⁻⁷ | 4·10⁻⁷⁸ | 4.499 | 3.272 |
| 0.40 | 1.952756·10⁻⁸ | 1·10⁻⁷⁶ | 5.208 | 3.823 |
| 0.37 | 3.657823·10⁻¹¹ | 1·10⁻⁷³ | 6.581 | 4.902 |
| 0.35 | 1.315890·10⁻¹³ | 4·10⁻⁷¹ | 7.775 | 5.853 |
| 0.32 | 1.171320·10⁻¹⁸ | 8·10⁻⁶⁶ | 10.173 | 7.791 |
| 0.30 | 2.362353·10⁻²³ | 6·10⁻⁶¹ | 12.346 | 9.574 |
| 0.28 | 1.311023·10⁻²⁹ | 2·10⁻⁵⁴ | 15.185 | 11.932 |
| 0.26 | 4.256789·10⁻³⁸ | 8·10⁻⁴⁶ | 18.965 | 15.112 |
| 0.24 | 7.282474·10⁻⁵⁰ | 8·10⁻³⁴ | 24.113 | 19.498 |

- The spread column is the largest relative difference of Δ from the base value over the four variations. Its growth toward small radii is the fixed absolute floor of about 10⁻⁸², set by the 80-digit coefficients, divided by a shrinking jump.
- At \|ξ*\| = 0.50 the start-point search leaves the neighbourhood of 0. Radii above about 0.45 are outside this harness.
- The first-order value D/A (mismatch after the forward leg divided by the amplification) agrees with the Newton value to second order in the jump: 8 % at 0.45, 5·10⁻⁵ at 0.40, 10⁻²⁰ at 0.30.

**Decay law.**
- Against T_model the effective exponent is A_ξ ≈ 1.83–1.86 (fits with a free power of T), below the design model 2π/3 = 2.094. This is the same low value stage 2 read from the coefficients (1.77–1.95).
- T_model keeps only the leading term of the Fatou coordinate of the restricted map f(z) = F_z(z, φ(z)). The formal Fatou coordinate is t̂ = A₃z⁻³ + A₂z⁻² + A₁z⁻¹ + κ log z + ΣB_jz^j, with A₃ = −1/(3ℓ) (checked), A₂ ≈ 0.537 + 1.611i, A₁ ≈ −0.135 + 0.154i and κ ≈ 1.812 + 0.090i. The lower terms reduce the time by a fifth to a quarter at these radii (last column).
- Against T_true = −Im t(z*), after removing the power factor \|t\|^{−Re α/3}·e^{Im α·arg t/3} of the linear model, the local slope of ln\|ΔY\| between consecutive radii is:

| Between | slope / (−2π) |
|---|---|
| 0.45–0.42 | 0.98375 |
| 0.42–0.40 | 0.98671 |
| 0.40–0.37 | 0.98965 |
| 0.37–0.35 | 0.99220 |
| 0.35–0.32 | 0.99443 |
| 0.32–0.30 | 0.99616 |
| 0.30–0.28 | 0.99727 |
| 0.28–0.26 | 0.99812 |
| 0.26–0.24 | 0.99876 |

- Without the power factor the same slopes run from 0.886 to 0.983.
- The remaining prefactor drifts slowly, from about 14 to about 22 over the range. No Stokes constant is claimed.

## 4. Reading (`[NUM]`, owner; SESSION)

1. **The jump is numerically nonzero** on the overlap S₀ ∩ S₁ of the pilot branch, by a margin of 33 to 79 orders of magnitude over the reproducibility floor.
2. **The decay is exp(−2πT) in the Fatou time**, with slopes approaching −2π from below. This is what a first Fourier mode of a 1-periodic factor gives. It is consistent with the design model D6 (Borel singularity at 2πi in t), and it explains stage 2's INCONCLUSIVE scale: the apparent exponent 1.8–1.9 is the leading-time variable at radii where the lower terms of the Fatou coordinate still matter. It is not a different singularity.
3. **Consequence if the jump is real.** By the pilot's decision rule (§5): Γ̂₊ diverges; by T(Γ₊) = Γ₋ so does Γ̂₋; and under P1-c-5 Lemma 5b-1, log F diverges. **None of this is established here.** It would not close B-an or B-6 either: an analytic square or sixth root can exist without an analytic flow.
4. **What a certificate now has to resolve.** At \|ξ*\| = 0.40 to 0.45 the jump is 10⁻⁸ to 10⁻⁵. The design had assumed about 10⁻¹¹⁴ at \|ξ*\| = 0.2. Certified enclosures of φ₀(z*) and φ₁(z*) to about 10⁻¹⁰ would suffice, and ordinary interval precision covers that. The transport legs are short (about 330 map steps from \|ξ\| = 0.1). The open proof obligation is unchanged in kind and much smaller in size: a rigorous bound for the distance between each sectorial curve and a truncated series at \|ξ\| ≈ 0.1, to about 10⁻¹⁰.

## 5. Limits

- No error bound is proved for the distance between a sectorial curve and the truncated series at the matching radius. The stability under r_m and N is evidence, not a bound.
- The identification of the two computed curves with the 3-sums of Γ̂₊ on S₀ and S₁ rests on the qualitative theory (LH2012 Theorem 4.2; assessment §5 and §6). It is not re-proved here.
- One overlap of one branch was measured. The T²-class of the odd overlaps (design §3) was not.
- The linear model used for the power factor is `[HEUR]`. The formal Fatou coordinate is truncated at J = 12.
- Not replayed by the co-owner. Evidence level: OWNER-RUN.

## 6. Proposed next step (for the 3b design note; not authorized by this record)

Design the certificate around the measured numbers:
- **Common point:** \|ξ*\| between 0.40 and 0.45 on arg ξ = π/6.
- **Target:** Δ ≠ 0 only (non-vanishing), as in the decision rule.
- **Architecture:** local enclosure of each curve at \|ξ\| ≈ 0.1 around a low-order truncation, validated forward transport over about 330 steps, and one interval subtraction.
- **Open obligation to be designed:** the local enclosure. One candidate is an invariant tube around the truncated series, proved by a one-step inequality checked by interval arithmetic on a finite range of \|ξ\| and by an analytic estimate near 0. Its feasibility is not known.
- **Second overlap class:** the same scouting on the overlap S₁ ∩ S₂ is cheap and could be run first.
