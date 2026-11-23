# Verification record — degree-ten even term of the delivered $\widehat F$ (fixed $h_6$)
**Checker:** Claude (Dyadic DSN editor) · **Date:** 25 Sep 2026 · **Scope:** exact $\mathbb Q(i\sqrt3)$ computation, independent of the third-party report and of the producer/validator code; same exact engine as the v6.4.10 referee.
**Object checked:** $\widehat F:=h_6^{-1}\circ F_W\circ h_6$ with $h_6$ the **fixed** adopted degree-6 polynomial normalizer (DYAD-ALG-NF6; 23 coefficients; resonant monomial coefficients of each $h_n$ zero), $F_W$ the exact six-step return built to total degree 10, $h_6^{-1}$ as a convergent series taken to degree 10 (verified $h_6\circ h_6^{-1}=\mathrm{id}$ through degree 10).

## Result `[ALG] [scope: fixed h_6; degree ≤ 10] [provenance: Claude-checked]`
- $\mathcal J_{\le6}\widehat F=J$ (the adopted jet) — reproduced.
- Even-degree parts of $\widehat F$: **degrees 2, 4, 6, 8 vanish identically; degree 10 does not.** Ten nonzero degree-10 monomials.
- $$[\widehat F]_{(5,5)}=-\frac{6113}{839808}-\frac{3152683}{403107840}\,i\sqrt3\;\ne0 .$$
- Consequently the **delivered** exact map $\widehat F$ (defined with the truncated $h_6$) is **not** odd under $z\mapsto-z$; its first even term is at degree ten; and $\chi_1(z)=\widehat F(z)/z$ is **not** exactly sign-invariant. The third-party report is **confirmed**, including its "first even term is degree ten" part (lower even degrees checked to be zero).

## What this does and does not change
- Does **not** touch: the formal all-order normal form (odd, by $p-q\equiv1\bmod6$); the finite jet $J$ (odd); DYAD-THM-NF-REM ($C_7$, $C_D$); DYAD-THM-PRIM-CTR; any physical relabeling claim (OPEN-A). The safe bound $|\chi_1(-z)-\chi_1(z)|\le2C_7|z|^6$ stands and is now known to be non-vacuous.
- Establishes only for $m=1$; $\chi_m$, $m\ge2$, not separately computed here (the same engine can do it on request).
- Interpretation: a degree-6 truncated normalizer cannot be expected to preserve the normal-form parity beyond its own order; the even content re-enters at the first order where the truncation error of $h$ feeds back into the return. This is a property of the delivered chart, not of the dynamics.

## Recommended registry wording (v0.4 → v0.5)
Main profile line (`RRF-DYAD-NF`): unchanged from the reviewer's proposal — all-order oddness of the delivered $\widehat F$ and exact sign-invariance of $\chi_1$ are **not asserted**.
Finding block: replace "third-party reported; unreviewed" by  
> $[\widehat F]_{(5,5)}=-\tfrac{6113}{839808}-\tfrac{3152683}{403107840}i\sqrt3\ne0$; even degrees 2–8 vanish. `[ALG] [scope: fixed $h_6$, degree ≤ 10] [provenance: Claude-checked 25 Sep 2026; third-party report confirmed]`. Delivered $\widehat F$ not odd; $\chi_1$ not exactly sign-invariant; $\chi_m$ ($m\ge2$) not examined.
