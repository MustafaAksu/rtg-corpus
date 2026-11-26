# Review — Gaussian quarter-strobe boundary and register quotient (PR #398)

**Date:** 26 November 2026.
**Reviewer:** Claude (SESSION, independent review requested in the record's §7).
**Object:** PR #398, head `3146b75707756fe84cb59cc2a083e002eda84af2`, file `records/ofn/OFN_GAUSSIAN_STROBE_REGISTER_SESSION.md` and evidence under `evidence/ofn/gaussian_cascade/`.
**Status:** SESSION / NONCANONICAL. A review is not adoption; grade, routing and merge are PI decisions.

## 1. Evidence checks (executed by the reviewer)

- PR head fetched read-only from GitHub; `refs/pull/398/head` = `3146b757…`. Upload branch `upload/ofn-gaussian-cascade-20261126` present at `21fdf632…`.
- SHA-256 of all four evidence files and their `upload/` copies recomputed from the PR head blobs; all match the record's §7 table and `SHA256SUMS.txt`.
- r2 rerun independently (Linux, Python 3, SymPy 1.14.0) from a byte-identical copy of `scripts/cyclotomic_gauss_cascade_checks_r2.py` (`0e6f8486…`). Exit 0; output byte-identical to `runs/cyclotomic_gauss_cascade_checks_r2_output.txt` (SHA-256 `3f189abf…`).
- r1 was rerun earlier in the session (script `d5ddda4d…`), output identical. The reviewer's supplementary 24 generic cases (p = 20, 28, 36, 44) are now subsumed by r2's native coverage and need not be recorded separately.

## 2. Proof checks (by hand)

**§3, ordered-sum derivation: correct.**
- Conjugation phases:
  - W component of H_k: A L^k W² + B L^{-k} WV + C L^{-3k} V².
  - At W=0, the W component of H_j is C L^{-3j} V² and its V component is Ā L^{-j} V².
- The derivative terms B L^{-k} V and 2C L^{-3k} V give exactly the two paths BC·S(−3,−1) and 2CĀ·S(−1,−3). The A W² term needs two W inputs and is degree ≥ 4.
- Direct V³ weight L^{-4j}. G(−4) = 0 because the order of L⁴ is s ≥ 2.
- Ā = −L³A for real a. BC/D = 2a²L⁵/((1+L)⁴(L²+L+1)). The composition order R^{-s} f^s = H_{s−1}⋯H_0 is correct.

**§4: correct.**
- Charge-graded ideals (1−I^k) are correct.
- For p = 2^k ≥ 16, v₂(s−2) = 1. Hence (1−L^{s−2}) = P² with P = (1−L) = (1+L), so (Q_p) = g⁻¹P⁻². This agrees with the reviewer's earlier norm computation: N(Q_p(1+i)) = 1/4.
- The order-two argument in I_K / I_ℚ is correct.

**§5: correct.**
- gcd(H², (1+t^m)^{2^{α−2}}) = Φ̄_m^{2^{α−2}} = H.
- Reducedness holds iff α = 2. The natural inclusion induces Frobenius t ↦ t², bijective iff 8 ∤ p.
- In the exact sequence 0 → A → C → A → 0, injectivity of ·(1+I) follows from g/g² ≅ R/g.
- Fibre size of E_{2s} on ker B is 2^{s−φ(p)/2}, and π_s B = π_{2s}.

**§6: correct.**
- D is a unit iff the orders p and p/gcd(p,3) are not prime powers, i.e. off 2^k and 3·2^k. S is an algebraic integer, so (S) = g there and im(m_S) = J.
- The unit restriction is needed: at p = 2^k the image of m_S strictly contains J.

## 3. Requested changes

**R1 (wording, §6).** The sentence calling the image equalities "stronger than a shared norm/cardinality or a mere occurrence of the symbol i" overstates the case:
- Any element of R_p of the form (unit)·(1−I) has image J. The equality J = E_{2s}(ker B) is the standard identity (1+I)·R_p/2R_p = g/2R_p.
- The non-trivial content is narrower: in the sector where D is a unit, each strobe path sum equals the strobe boundary 1 ± I up to a unit and carries no further prime factor.

Suggested replacement: *"In the unit sector each ordered sum is, up to a unit, the strobe boundary 1 ± I; its multiplication image is therefore the Gaussian layer J, which coincides with E_{2s}(ker B). This is an exact algebraic coincidence of ideals, not an identification of operations."*

**R2 (§7, provenance).** Replace "no separate Claude executable/output supplied" with the facts in §1 of this review: independent r2 rerun, hashes and byte-identical output.

## 4. Non-blocking notes

- `_r2` is a successor evidence script next to frozen r1, not an edited copy. This is consistent with "stored once", provided r1 stays unmodified, as recorded.
- `upload/` copies on main follow existing repository practice.
- All results rest on the fixed raw frame and on rational scalings, as stated. The record correctly rejects the two-path fold hypothesis and keeps the sector boundary explicit: faithful register at p = 2^k, generic ideal equality off it.

## 5. Verdict

The mathematics is correct and the record is scoped honestly. **Approve after R1 and R2.** The ideal-class and quotient results are standard algebra, as the record itself says. Their value to the project is bookkeeping: they place the Gaussian boundary precisely. They do not provide evidence for a physical mechanism.
