# Review — Intrinsic strobe-boundary structure, Stage 2A (PR #411)

**Date:** 26 November 2026.
**Reviewer:** Claude (SESSION, independent review requested in the record's §7).
**Object:** PR #411 at head `496aafbe0113e422b7f538b71efa6be8f127e6f3`. Record: `records/ofn/OFN_INTRINSIC_STROBE_BOUNDARY_STAGE2A.md`.
**Status:** SESSION / NONCANONICAL. A review is not adoption.

## 1. Evidence

- **Hashes.** The PR head was fetched read-only. The script (`aac8861e…`) and the output (`df1bc84a…`) match the record's table, `SHA256SUMS.txt` and the `upload/` copies.
- **Script inspection.** The script imports only `math` and SymPy. It makes no file, process or network calls.
- **Native replay.** Run on Linux with Python 3 and SymPy 1.14.0. Exit code 0. The output is byte-identical to the stored run.
- **Independent check.** Written in mpmath at 40 digits, without importing the PR script. It evaluates Q_p^σ(a,d) directly from the ordered double sum B₁C₁ Σ_{j<k} a_j a_k (x^{3j+k} − L² x^{j+3k}), for p = 12, 16, …, 200. Results:
  - At (a,d) = (1/2, 0) the sum reproduces the owner closed form.
  - The ratio r_p agrees with the §4 tan/cos closed form to 2·10⁻⁴¹.
  - r_p is real.
  - r_p·τ(r_p) = 1 in the embedding L ↦ −L.
  - r₁₂ = 1, and c_p ≠ 0 at every tested p.

## 2. Proof checks (by hand)

**§3: correct.**
- The quadratic insertions enter as a_j a_k with a_j = a + σd(−1)^j.
- (−1)^j = L^{2sj} turns the signed sums into shifted-charge geometric sums.
- The direct V³ term is common and is cancelled by G_s(−4) = 0.
- The even-s numerator of C vanishes only at θ = π/4 or π/2, which means p ≤ 8.

**§4: correct.**
- Each of the three factors of r_p increases strictly with θ.
- At θ = π/6 the product is (2−√3)·(2+√3) = 1.
- From ad = 0 and a² + r_p d² = 1/4, the classification table follows.
- The rationality restriction is right. τ fixes ℚ and τ(r) = 1/r, so a rational r must be ±1. Since 0 < r_p < 1 for odd s > 3 and r_p < 0 for even s, only p = 12 is possible.

**§5: correct.**
- τ is nontrivial on K⁺ because its multiplier 1 + 2s ≢ ±1 (mod 4s) for s ≥ 2. So τ pairs the real embeddings without fixed points, and N(r_p) = 1 for both signs of r_p.

**§6: correct.**
- With G₋(ρ) = −G₊(−ρ) and S odd, we get T_σ(z) = σT₊(σz). Then H T H⁻¹ = (F_n X, −T₊(w)) for both values of σ.

## 3. Recommended remark (no change to the results)

**R1 (link §5 to §6).** The norm-blind comparator of §5, (a, d) = (0, ½), is exactly the gate that §6 completes. G₊ = e^ρ − 1 is the owner exponential, and G₋ = 1 − e^{−ρ}. With this completion the system is conjugate to (F_n X, −T_own(w)), i.e. to an autonomous product.

So the "model the DZT norm cannot distinguish" is a reparametrized decoupled system, not a recognition coupling. Its coefficient differs in the fixed raw frame, which is the record's point. But §5 should not be read as showing that the norm is blind to a genuine coupling.

Stage 2B gives the complementary fact. Its irreducible coupling lives at degree q = p/2 − 1 and leaves the cubic and its norm untouched by construction. Taken together: neither the decouplable cubic sign gate nor the irreducible degree-q coupling is visible to the DZT cubic norm. I suggest one sentence in §5 cross-referencing §6.

## 4. Verdict

The mathematics is correct and was replicated independently. Scope and nonclaims are appropriate. **Approve.** R1 is recommended wording.

Stage 2B (#413) cites this record at a pinned commit. Merging #411 before, or together with, #413 keeps the dependency resolvable on main.
