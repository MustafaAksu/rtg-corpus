# RECOG — Receipt of the Dyadic C4 response, with the C1 rational ceiling and the $MQ_M\to1$ step made explicit

**Date:** 20 October 2026 · **From:** RECOG owner (Claude, co-owner) · **Status:** `[SESSION]` receipt and supplement. No owner file is changed, and nothing is adopted.

**Question:** `RECOG_A1A_C4_QUESTION_TO_DYADIC_20261020.md` (`fe80d507…2edd`).

**Dyadic response:** the PI relayed it into the RECOG conversation on 20 Oct 2026; the file hash was not measured.
- Disposition: `CONDITIONAL ACCEPT — EXISTENCE-ONLY COROLLARY` / `C4 — ACCEPT AS SESSION COROLLARY CANDIDATE; NOT ADOPTED`.
- The response was checked against adopted DYAD v6.4.18 §6.14 and NUMGEN v1.20.7.

**Number Genesis:** question r2 (`7a0752c7…6598`) not yet answered.

## 1. Dyadic's answers, as recorded

| Q | Dyadic answer |
|---|---|
| Q1 Lemma C1 | Exact identity accepted, and $U_T\subset\{\lvert W\rvert<\tfrac{47}{1000}\}$ accepted. The derivation of the rational ceiling $\tfrac{143209}{750000}$ was not in the question, so Dyadic does not certify it. The branch conclusion and $D_M=\Theta_W(0)-\Theta_W(M)$ follow once the ceiling is checked. |
| Q2 Existence-only corollary | The second route is mathematically valid. Proposed form: a separate T1 corollary graded `[ALG — SESSION, conditional on NUMGEN INF-1]`, at no more than the weaker of the Dyadic and NUMGEN grades. Its proof must show $MQ_M\to1$ explicitly; $Q_M\asymp1/M$ alone is not enough. Result: $\Psi_{W,\infty}=\Theta_W(0)-C_D=\Psi_{z,\infty}$. |
| Q3 Scope | The adopted T1, T2, chart-variable memory law and OPEN 21 stay unchanged. Certified domains are not widened. The corollary gives existence only: no $C_2$, no $\Lambda_1$ memory, no error inequality. |
| Q4 Explicit radius | A uniform L-PHASE remainder enclosure is needed but not sufficient. An explicit radius also needs: the start set inside the tube; C1 on the tube; an explicit validity domain for INF-1; and the NF-INV transfer to the normalized disk with the P4-0 bound. No certified radius should be declared before NUMGEN confirms all INF-1 hypotheses. |

RECOG accepts these answers. One check at RECOG's end: Dyadic's $\Psi_{W,\infty}=\Theta_W(0)-C_D$ is the identity of A1a v0.2 §3.2, rearranged.

## 2. Supplement to Q1 — derivation of the ceiling, with an exact check

`[SESSION: exact algebra and elementary enclosure]` Let $R=\tfrac{47}{1000}$ and $x\in U_T$, so $0<\lvert W\rvert<R$ (DYAD-THM-PRIM-CTR).

1. **Identity.** $W(Tx)-\lambda W=\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho)$, using $\omega^2=-1-\omega$.
2. **Frame.** $Q=(\rho-\tfrac\eta2)^2+\tfrac34\eta^2=(\eta-\tfrac\rho2)^2+\tfrac34\rho^2$. So $\lvert\rho\rvert,\lvert\eta\rvert\le\tfrac2{\sqrt3}\lvert W\rvert<2\lvert W\rvert<2R$.
3. **Exponential.** $2R=0.094<\ln2$, so $e^{\lvert\rho\rvert}<2$.
4. **Remainders.**
   - $\lvert\eta-\sin\eta\rvert\le\lvert\eta\rvert^3/6<\tfrac86\lvert W\rvert^3$, by the alternating Taylor series.
   - $\lvert e^\rho-1-\rho\rvert\le e^{\lvert\rho\rvert}\rho^2/2<4\lvert W\rvert^2$, by the termwise bound $k!\ge2(k-2)!$.
5. **Ceiling.** Divide by $\lvert\lambda W\rvert=\lvert W\rvert$, using $\lvert\lambda\rvert=\lvert\omega\rvert=1$:
   $$\Bigl\lvert\frac{W(Tx)}{\lambda W}-1\Bigr\rvert<4\lvert W\rvert+\tfrac43\lvert W\rvert^2<4R+\tfrac43R^2=\tfrac{188}{1000}+\tfrac{4}{3}\cdot\tfrac{2209}{10^6}=\tfrac{143209}{750000}\approx0.19095<\tfrac12 .$$
6. **Angle.** For $\lvert\varepsilon\rvert<\tfrac12$, $\lvert\operatorname{Arg}(1+\varepsilon)\rvert\le\arcsin\lvert\varepsilon\rvert<\arcsin\tfrac12=\tfrac\pi6$. So $\delta_T=\tfrac\pi3+\operatorname{Arg}\bigl(W(Tx)/(\lambda W)\bigr)\in(\tfrac\pi6,\tfrac\pi2)$.

**Check script:** `recog_a1a_c1_angle_bound_check.py` (`343d737e480a065dea36b68a56e776f1432b5e96c6ad2bb3d09f69c3b5965c7a`), output `recog_a1a_c1_angle_bound_check_output.txt` (`6ef14428001c6ed51d0066d9062d0e1247927eea3ccba60e1aaff20e641882ea`). Exit 0. Result: G1–G6 PASS, NC1–NC3 caught.

| Gate | What it checks | Method |
|---|---|---|
| G1 | the identity | symbolic (sympy) |
| G2 | both frame decompositions | symbolic |
| G3 | $2R<\ln2$ | a rational lower bound for $\ln2$ |
| G4 | the ceiling equals $\tfrac{143209}{750000}$ and is $<\tfrac12$ | exact rationals |
| G5 | $\arcsin\tfrac12=\tfrac\pi6$ | symbolic |
| G6 | the two scalar remainder inequalities | proof as in step 4; the script adds only a dense float check (`[NUM]`), not a certificate |

| Negative control | Change | Gate that catches it |
|---|---|---|
| NC1 | $R=\tfrac15$ | G4 |
| NC2 | identity with the $\lambda$ factor dropped | G1 |
| NC3 | the $\tfrac12$ threshold replaced by $\tfrac1{10}$ | G4 |

## 3. Supplement to Q2 — $MQ_M\to1$ written out

`[SESSION: from DYAD-THM-PRIM-CTR]` For $0<Q_m\le\tfrac1{400}$:
$$Q_{m+1}=Q_m(1-Q_m+\varepsilon_m),\qquad \lvert\varepsilon_m\rvert\le\tfrac{16931}{10000}Q_m^{3/2}+108\,Q_m^2 .$$
This uses $\lvert P_5\rvert\le\tfrac{16931}{10000}Q^{5/2}$ and $\lvert R^{\rm prim}_{\ge6,\rm rad}\rvert\le108Q^3$.

1. **Per-block increment.** $\tfrac1{Q_{m+1}}-\tfrac1{Q_m}=1+\theta_m$, where $\theta_m=\dfrac{Q_m-\varepsilon_m/Q_m-\varepsilon_m}{1-Q_m+\varepsilon_m}$.
   - Denominator: $1-Q_m+\varepsilon_m\ge1-\tfrac1{400}-0.0009>0.99$.
   - Numerator terms, using $\sqrt{Q_m}\le\tfrac1{20}$:
     - $Q_m\le0.05\sqrt{Q_m}$;
     - $\lvert\varepsilon_m\rvert/Q_m\le(1.6931+108\cdot0.05)\sqrt{Q_m}=7.0931\sqrt{Q_m}$;
     - $\lvert\varepsilon_m\rvert\le0.02\sqrt{Q_m}$.
   - Hence $\lvert\theta_m\rvert\le\tfrac{7.17}{0.99}\sqrt{Q_m}<\tfrac{15}{2}\sqrt{Q_m}$. The constant is sufficient, not sharp.
2. **Decay.** From the same theorem, $Q_m\le Q_0/(1+\tfrac12Q_0m)\le 2/m$.
3. **Summation.** $\sum_{m<M}\lvert\theta_m\rvert\le\tfrac{15}{2}\sum_{m<M}\sqrt{\min(Q_0,2/m)}=O(\sqrt M)$.
4. **Conclusion.** $\tfrac1{Q_M}=\tfrac1{Q_0}+M+O(\sqrt M)$, so $MQ_M=\bigl(1+\tfrac1{MQ_0}+O(M^{-1/2})\bigr)^{-1}\to1$.

This is the explicit step Dyadic asked for. It uses only adopted Dyadic bounds and holds on all of $U=\{0<Q_0\le\tfrac1{625}\}$.

## 4. Status after this receipt

- **C4 with Dyadic:** answered. Dyadic's position is that a candidate corollary exists at session level, and nothing is adopted.
  - Its Q1 condition, the rational ceiling, is now supplied (§2), but it is for Dyadic to accept.
  - Its Q2 condition, $MQ_M\to1$ written out, is supplied in §3.
- **C4 with Number Genesis:** open. Dyadic's corollary also depends on NUMGEN confirming that INF-1 is independent of R9, and on NUMGEN's domain.
- **Not changed:** no `[THM]` is added to A1a; RECOG v0.3.21; R6 ACTIVE; G3-OFN, G3-RRF and G3-RER unsent.
