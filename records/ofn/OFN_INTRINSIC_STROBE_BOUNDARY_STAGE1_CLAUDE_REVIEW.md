# Review — Intrinsic strobe-boundary structure, Stage 1 (PR #403)

**Date:** 26 November 2026.
**Reviewer:** Claude (SESSION, independent review requested in the record's §6).
**Object:** PR #403, head `e371b3486cd7be068b44426d56cd03497a979988`, file `records/ofn/OFN_INTRINSIC_STROBE_BOUNDARY_STAGE1.md`, and the evidence under `evidence/ofn/intrinsic_strobe_boundary/`.
**Status:** SESSION / NONCANONICAL. A review is not adoption.

## 1. Evidence checks

- PR head fetched read-only (`refs/pull/403/head`). Upload branch `upload/ofn-strobe-boundary-stage1-20261126` present at `fbe55997…`.
- SHA-256 hashes of the script (`20de5156…`) and output (`ccb3105e…`), and of their `upload/` copies, recomputed. All match §6 and `SHA256SUMS.txt`.
- The script was inspected: it imports SymPy only and has no file, process or network calls.
- Script rerun on Linux with Python 3 and SymPy 1.14.0. Exit 0; output byte-identical to the stored output.
- **Independent check, written without importing the PR script:**
  - G_s(−4) = 0 in Λ iff s is even, checked for s = 1..40.
  - Full-register image dimension of m_{P̄_{u,v}} for both paths, checked for s = 1..40: s when s is even, s−1 when s is odd.
  - Exhaustive span of the affine s-step displacements for s ≤ 6: rank s+1, and native parity descends iff s is even.
  - The 2-adic component structure for s = 1..40, as described in §3 below.
  - Every check passes.

## 2. Proof checks (by hand)

**§2: correct.**
- Integral exactness of F(P) = tP + 1 on 0/1 registers: the constant term is 1 − x_{n−1} ∈ {0, 1}.
- Z∘F = tZ, and Z is injective.
- The charge-graded boundary ideals.
- Λ/(d) ≅ F₂[t]/(tˢ+1), and the induced affine update is F_s.
- The index argument [Λ : d_r²] = 2^{2r} holds, using injectivity of multiplication by 1 − t^r. Hence d_r² = (2) iff r = s. The record correctly marks this selection as conditional.

**§3: correct.**
- F^s(P) = tˢP + g_s.
- The displacement span is dM + F₂g_s, which is the ideal (g_s) because d = (1 − t)g_s.
- The maximal affine-linear s-return factor is F₂[t]/(g_s), with 2^{s−1} states.
- H_s realises this factor, and parity descends through it iff s is even.
- The spectral statement G_s(1) = (1 − i)/(1 − L) holds, with 1 − L a unit when p is not a power of two.
- The universality claim is correctly restricted to affine-linear readouts.

**§4: correct.**
- P_{u,v} = 1 − t^{sv} − (1 − t^v)G_s(−4).
- For odd s, in the primary factor (t+1)²: t^{−4} = 1, G = 1, and 1 − t^{sv} = 1 − t^v = ε, so P = 0.
- In every other primary factor 1 − t^{−4} is a unit, so G = 0 and P = d. By CRT the generated ideal is d(t+1)M, which equals the set of (Y, Y) with π_s(Y) = 0.
- The augmentation obstruction holds: ε(G_s(−4)P) = s·ε(P).

**§5: correct, and appropriately scoped.**

## 3. Requested change and an added remark

**R1 (Stage 2 scope, §5 [OPEN]; wording needed).** The proposed sector pair "Φ₄ ⊕ Φ_p" describes Λ⊗ℚ exactly only when s is an odd prime (or s = 1). In general, Λ⊗ℚ = ∏ ℚ(ζ_d) over the divisors d of p with v₂(d) = v₂(p). Examples:
- s = 9: Φ₄ Φ₁₂ Φ₃₆.
- s = 15: Φ₄ Φ₁₂ Φ₂₀ Φ₆₀.
- s = 6: Φ₈ Φ₂₄.

The record's own §4 proof already uses this factorisation. A uniform form of the dichotomy is:

> The parity root t = 1 lies only in the component Φ_{2^{v₂(p)}}. The direct charge −4 sum fails to cancel there iff 2^{v₂(p)} divides 4, that is, iff s is odd.

Intermediate components behave like the primitive one: there G(−4) = 0. Stage 2 should state which components its carrier retains. Retaining only Φ₄ ⊕ Φ_p drops register information for composite s.

**R2 (constraint on Stage 2; proposed added remark, PI's call).**
- All pairwise resultants of these cyclotomic factors are odd (checked for s ≤ 40; by the standard resultant formula they are powers of odd primes or 1). Hence Λ ⊗ ℤ₍₂₎ splits as the direct product of its components.
- Modulo 2, the parity-bearing sector and the primitive Φ_p sector are independent direct factors. Λ itself supplies no 2-primary gluing between them.
- The Φ₄ component is evaluation at L = i, i.e. the p = 4 resonance (K = 2). That lies outside the DYAD cascade range (p ≥ 8; p = 8 degenerate).

So "retaining Φ₄" means carrying a second resonance alongside p = 4s. Any coupling between the recognition bit and the primitive cascade must come from the composition law, not from the carrier. This sharpens the Stage 2 question:

> Does an admissible law couple the Φ_{2^{v₂(p)}} sector to the primitive sector, given that the carrier splits 2-adically?

**Note.** The DYAD coefficients A, B, C contain (1+L)⁻¹ and K_p⁻¹. Neither lifts to Λ: 1+t is not a unit, since Λ/(1+t) ≅ ℤ/2. The record correctly limits the lift to the ordered path sums.

## 4. Verdict

The mathematics is correct, independently replicated and honestly scoped. The new content is threefold:
- the affine-clock obstruction BF^s = C_sB;
- the maximal affine-linear s-return factor;
- the full-register, odd-s path-image deficit, hidden by primitive projection.

**Approve with R1. R2 is recommended as an added remark.** A shared physical mechanism remains [OPEN]. R2 indicates that the carrier alone will not provide one.
