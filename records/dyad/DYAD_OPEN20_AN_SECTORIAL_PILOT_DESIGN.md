# DYAD OPEN 20 (analytic branch) — written design of a sectorial pilot for one formal branch

**Date:** 23 October 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION). It is a written design only. It is not a computation, certificate, amendment, release or notice, and no numerical Stokes campaign is started by it.

**Authority:** receiving review `records/dyad/DYAD_LH2012_RECEIVING_REVIEW.md` §6 ("WRITTEN PILOT DESIGN SUPPORTED"), on `records/dyad/DYAD_OPEN20_AN_LH2012_OWNER_ASSESSMENT.md`.

**Governing edition:** DYAD v6.4.22. OPEN 20 B-an and B-6 are ACTIVE.

**Notation:**
- $F=T^6$ in the complexified raw frame $z=\rho+\omega\eta$, $w=\rho+\bar\omega\eta$ ($z=W$). This $z$ is not the normalized NF coordinate.
- $\mu,c_{40},d_{31},C,A,B,\ell,\alpha$ are as in the owner assessment.
- [L12] = López-Hernanz, ETDS 32 (2012) 211–221.

**Goal of the pilot.** Produce, for one formal branch, a certified enclosure of one sectorial jump $\Delta_{\sigma,j}(z_*)$ at one nonzero point, or report that the enclosure contains 0.
- An enclosure that excludes 0 proves that the branch diverges. By Lemma 5b-1 (P1-c-5) it then also proves that $\log F$ diverges.
- An enclosure that contains 0 decides nothing.
- Neither outcome decides B-an or B-6.

## 1. Branch, coordinates and normalization

**D1. Branch.** The leading coefficients are the two roots of $P(a)=Aa^2+Ba+C$, whose discriminant is $B^2-4AC=\tfrac{1277}{4320}+\tfrac{281\sqrt3}{12960}i$. The pilot uses the root with $\operatorname{Im}a>0$:
- $a_+\approx0.0256752224+0.1484934467\,i$;
- the other root is $a_-\approx0.0576581110-0.0041558794\,i$.

The sign of $\operatorname{Im}a$ isolates the branch. The pilot certifies it from the exact radical by an interval evaluation, which needs only a crude enclosure.

One branch suffices for a convergence/divergence decision, because $T(\Gamma_+)=\Gamma_-$ (owner assessment §1). It does not make the jumps of the two branches identical.

**D2. Lifted chart.** Use $(z,w)=(x,\,x^2(a_++y))$. The lifted map is analytic:

$$x'=x+x^4G(x,a_++y),\qquad y'=\frac{a_++y+x^3H(x,a_++y)}{(1+x^3G(x,a_++y))^2}-a_+.$$

Here $G,H$ are the quotients of the exact jets by $x^4$ and $x^5$. Since $T$ is entire, $F$ and the lifted map are analytic on any bounded polydisc where $1+x^3G\neq0$. The pilot certifies a lower bound for $|1+x^3G|$ on its domain.

**D3. Strict-transform jet and $m$.** The strict transform of $\Gamma_+$ is $y=\sum_{n\ge1}b_nx^n$ with $b_1=a_{3,+}$, the $z^3$ coefficient of $\hat\phi_+$; numerically $a_{3,+}\approx-0.0378863102-0.0333746170\,i$.
- Put $Y=y-b_1x$. Then $m(F;\xi,Y)\ge2$, and $m>1+\operatorname{Re}\alpha$ holds because $\operatorname{Re}\alpha=-102/19$.
- The pilot computes $b_1$ exactly in $E=\mathbb Q(i\sqrt3)[a_+]$ from the order-$z^6$ graph equation $\ell(k^*-3)a_3=R_3$ (P1-c).
- It also records the first nonzero $b_n$, $n\ge2$, which fixes $m$.

**D4. Horizontal normalization.** $\ell_+=c_{40}+\mu a_+\approx0.0961278516-0.0196970021\,i$, so $\arg(-\ell_+)\approx0.935667\pi$.
- Choose $c_+$ as the principal cube root of $-\ell_+$: $c_+\approx0.2569865579+0.3830143552\,i$, with $\arg c_+\approx0.311889\pi$.
- Put $\xi=c_+x$.
- Then $F_1=\xi-\xi^4+O(\xi^4Y,\xi^5)$ and $F_2=Y-\alpha\xi^3Y+O(\xi^3Y^2,\xi^4Y)+\xi^{3+m}\psi(\xi)$, which is [L12] Definition 4.1 with $k=3$.

**D5. Inverse map.** $F^{-1}$ has $\xi\mapsto\xi+\xi^4+\dots$. With $\tilde\xi=\rho\xi$, $\rho^3=-1$ ($\rho=e^{i\pi/3}$), we get $\tilde\xi\mapsto\tilde\xi-\tilde\xi^4+\dots$ and the same $\alpha$ and $m$. This is the normalized form for the repelling petals. The pilot writes it out and checks it exactly.

## 2. Cover, overlaps and inclusion in the Hakim domains

**D6. Petals.** Take $\eta=\pi/4$.
- $F$ has petals bisected by $\arg\xi=0,\,2\pi/3,\,4\pi/3$, i.e. by $\xi^3\in\mathbb R^+$.
- $F^{-1}$ has petals bisected by $\arg\xi=\pi/3,\,\pi,\,5\pi/3$.
- Each petal has asymptotic half-opening $(\pi-\eta)/3=\pi/4$.
- The six candidate singular directions are $\arg\xi=\pi/6+j\pi/3$. In raw $z$ they are $\arg z\approx(-0.145222+j/3)\pi$, $j=0,\dots,5$.

**D7. Straight sectors inside the petals.** Let $S_j=\{0<|\xi|^3<\kappa\delta,\ |\arg\xi-j\pi/3|\le5\pi/24\}$ with $\kappa=2\cos(3\pi/8)\approx0.7654$.

*Inclusion.* With $\theta$ ranging over $[-(\pi/2-\eta),\pi/2-\eta]$, the union of the discs $D(\delta e^{i\theta},\delta)$ contains every point $re^{i\psi}$ with $|\psi|\le\pi-\eta$ and $r<2\delta\cos(|\psi|-(\pi/2-\eta))$. Apply this to $\xi^3$ with $|\psi|\le5\pi/8$, so $|\psi|-(\pi/2-\eta)\le3\pi/8$; this gives $S_0\subset\Delta^3_{\pi/4,\delta}$. The other $S_j$ follow by rotation, using the $\tilde\xi$ coordinate of D5 for odd $j$.

So the template of the receiving review is contained in the true Hakim domains for every $\delta\le\delta_0$, without replacing their dynamics. $\delta_0$ itself is fixed in §4.

Adjacent $S_j,S_{j+1}$ overlap in an angular window of width $\pi/12$ centered on the singular direction $\pi/6+j\pi/3$; this includes $S_5\cap S_0$. The comparison point $z_*$ lies in such an overlap, and the jump is evaluated after both sums are pushed back to the same raw $z$ (D9).

## 3. Selected functions and branches

**D8. Selected sums.** On $S_j$ the selected function is the fixed point of Hakim's operator ([L12] §4) for $F$ ($j$ even) or $F^{-1}$ ($j$ odd), in the class
$$\mathcal H=\{u:\ |u(\xi)|\le|\xi|^{m-1},\ |u'(\xi)|\le|\xi|^{m-2}\}.$$
By [L12] Theorem 4.2(3) it is unique in this class, and by Corollary 5.2 it is the 3-sum of $\hat Y$ in that direction.

The factor $\xi^\alpha$ and the ratio $x_0^\alpha/x_n^\alpha$ in the operator use the branch of $\log\xi$ continuous on the petal, with its cut outside the petal. Its value is fixed by $\log(e^{ij\pi/3}r)=\ln r+ij\pi/3$ on the bisector. The operator depends only on ratios along an orbit inside one petal, so the choice cancels; it is fixed only to make the computation reproducible.

**D9. Comparison in raw $z$.** For each sum $u_j$, form $\phi_j(z)=z^2\bigl(a_++b_1z+u_j(c_+z)\bigr)$ in the raw chart, on the common raw sector $c_+^{-1}(S_j\cap S_{j+1})$. Then
$$\Delta_{+,j}(z_*)=\phi_{j+1}(z_*)-\phi_j(z_*).$$
Never compare $\phi_+$ with $\phi_-$: they differ at order $z^2$.

**D10. Symmetry reduction (SESSION derivation; to be checked in the receiving review of this design).**
- $T^2$ maps $\Gamma_+$ to itself, because $T$ exchanges the two branches.
- Its linear part rotates $z$ by $\lambda^2=e^{2\pi i/3}$.
- The image of the 3-sum in direction $d$ is analytic on a sector around $d+2\pi/3$ of opening $>\pi/3$, deformed only at $O(z^2)$, and is Gevrey-1/3 asymptotic to the same formal series. By uniqueness of 3-sums (Watson's lemma) it is the 3-sum in direction $d+2\pi/3$.

So the jump on overlap $j$ vanishes if and only if the jump on overlap $j+2$ does. The six overlaps of one branch fall into two $T^2$-classes, even and odd $j$. This does not identify the two classes and does not reduce them to one scalar.

The pilot needs one overlap for a divergence certificate. A convergence statement would need analytic gluing on all six overlaps; numerically that is unreachable.

## 4. Certifiable error budget

All quantities are enclosed with interval arithmetic: `python-flint` `arb`/`acb` at stated precision, or `mpmath.iv` as fallback. Floating-point values serve only for scouting.

| Item | What is bounded | How |
|---|---|---|
| E1 map | $F$ and $F^{-1}$ on a polydisc of radius $r_0$; Cauchy bounds for the remainders after the normalized leading terms | $T$ is entire: interval evaluation of the six-fold composition on the polydisc, with Cauchy estimates |
| E2 blow-up | $\inf|1+x^3G|>0$ and bounds for $G,H$ on $|x|\le x_0$, $|y|\le y_0$ | interval evaluation of the exact quotients |
| E3 orbit control | uniform invariance $f_u(S_j)\subset S_j$ for all $u\in\mathcal H$, and $|f_u^n(\xi)|^3\le C|\xi|^3/(1+n|\xi|^3)$ with explicit $C$, $\delta_0$ | explicit Leau–Fatou estimates for $\xi-\xi^4+$ (bounded perturbation), following [L12] §4 and Lemma 4.4 with every constant written out |
| E4 contraction | $\|Tu-Tv\|\le L\|u-v\|$ on $\mathcal H$ with $L<1$, and $T(\mathcal H)\subset\mathcal H$ | constants $B,B'$ of [L12] §4 made explicit from E1–E3 |
| E5 tail | the orbit sum truncated at $N$ terms | $\sum_{n\ge N}|x_n|^{s}\le C_s(N)$ from E3 |
| E6 approximation | a numerical approximation $\tilde u$, e.g. a polynomial in $\xi$ or a Chebyshev model on the sector | a posteriori fixed-point bound $\|u-\tilde u\|\le\|T\tilde u-\tilde u\|/(1-L)$ in the weighted norm |
| E7 transport | the map back to raw $z$ (D9), and the coordinate change of D3–D5 | exact coefficients; interval evaluation |

Only the article's qualitative existence of these constants is available; every constant must be produced by the pilot. If E3 or E4 cannot be closed with $L<1$ for some $\delta_0>0$, the pilot reports that and stops.

## 5. Stages and decision rule

1. **Exact preparation (small).** $b_1$, $m$ and the normalized jets of D3–D5, exact in $E$, with a checker and negative controls. This stage can run in the owner session.
2. **Scouting (non-rigorous).**
   - Estimate the jump scale $e^{-A/|z|^3}$ from the growth of the coefficients of $\hat\phi_+$; P1-c computed many of them. Use a Borel-plane singularity estimate.
   - From it, choose $|z_*|$ so that the expected jump exceeds the achievable error budget while $z_*$ stays inside $\bigcup S_j$.
   - The result of this stage is an estimate only; it is not recorded as evidence.
3. **Certification (heavier; on the PI's machine if needed).** E1–E7 for two adjacent sectors around one singular direction, then an enclosure of $\Delta_{+,j}(z_*)$.
   - It is delivered as a script with a fixed command, its JSON output with hashes, and negative controls (wrong branch, wrong log branch, perturbed $\alpha$).
4. **Decision.**
   - An enclosure excluding 0 proves the branch diverges and $\log F$ diverges. It is recorded as a SESSION result for review. It does not settle B-an or B-6.
   - An enclosure containing 0 is inconclusive and recorded as such.
   - No convergence claim can come from this pilot.

## 6. Guards

- **Real slice.** The complex sectorial curves have no nonzero real-slice points near 0. Real PRIM-CTR or L-PHASE constants are not reused.
- **Truncations.** The formal object is the full series. No finite truncation is identified with a sum.
- **Prior results.** Prior SESSION results keep their custody.
- **No change** to the DSN, RIDs, OPEN statuses or notices.
- **Next:** stage 1 can start after the receiving review of this design and the PI's go-ahead.
