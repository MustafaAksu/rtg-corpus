# DYAD OPEN 19: formal centralizer — closed-form proof of the homogeneous kernel lemma (SESSION v1.1)

**Date:** 16 October 2026 · **Author:** Claude (Dyadic DSN owner/editor) · **Status:** `[SESSION]` proof record v1.1, proposed for the next owner revision. The adopted v6.4.11 is **not** modified. v1.1 applies the review of 16 Oct 2026 (ACCEPT): §1 Step 4 tidied; Corollary U now proved without a normal-form dependency through the explicit involution $R_0=T^3\circ F^{-1/2}$; both scripts exit-gated; Problem B restated (§5).
**Purpose:** The reviewer asked for the general homogeneous-kernel lemma for **all** $k\ge2$, not only a finite table. This record gives a closed-form algebraic proof. It then derives the formal centralizer theorem and the uniqueness of the formal involution.

## 0. Setting

- $F=T^6$, written in the raw linear frame $W=\mathcal L(\rho,\eta)\in\mathbb C\cong\mathbb R^2$.
- $F=\mathrm{id}+G_3+O(|W|^4)$ with $G_3(W)=\mu|W|^2W$ and $\mu=-\tfrac12-\tfrac{2i\sqrt3}{3}$ (DYAD-THM-C21). $F$ has no quadratic term.
- Real formal vector fields with vanishing 1-jet are written by their complex component $V(z,\bar z)$; $\mathfrak X_k$ is the space of homogeneous fields of degree $k$.
- $X:=\log F$ (formal), so $X=X_3+X_4+\cdots$ with $X_3$ having component $V_3=\mu z^2\bar z$.

Only two properties of $\mu$ are used: $\Re\mu\ne0$ and $\Im\mu\ne0$.

## 1. Lemma K (homogeneous kernel) `[ALG]`

For every $k\ge2$:
$$\ker(\operatorname{ad}_{X_3})\cap\mathfrak X_k=\begin{cases}\mathbb R\,X_3,&k=3,\\0,&k\ne3.\end{cases}$$

### Proof

**Step 1 — the bracket on a monomial.** For real fields with complex components $A$ and $B$, the bracket component is $[A,B]=A\,\partial_zB+\bar A\,\partial_{\bar z}B-B\,\partial_zA-\bar B\,\partial_{\bar z}A$. Take $B=c\,z^a\bar z^b$ with $a+b=k$. Using $\partial_zV_3=2\mu z\bar z$ and $\partial_{\bar z}V_3=\mu z^2$:
$$[X_3,B]=c\,\alpha_{a,b}\,z^{a+1}\bar z^{b+1}-\mu\,\bar c\,z^{b+2}\bar z^{a},\qquad \alpha_{a,b}:=(a-2)\mu+b\bar\mu .$$

**Step 2 — the coefficient equations.** For $Y=\sum c_{a,b}z^a\bar z^b\in\mathfrak X_k$, collect the coefficient of the output monomial $z^{a+1}\bar z^{b+1}$. It receives two contributions: one from the input $(a,b)$ and one from the input $\phi(a,b):=(b+1,a-1)$. So $[X_3,Y]=0$ is equivalent to
$$c_{a,b}\,\alpha_{a,b}=\mu\,\bar c_{\phi(a,b)}\quad\text{for all }(a,b),\tag{E}$$
with the convention $c_{\phi(a,b)}:=0$ when $a=0$.

- $\phi$ is an involution on the index set. Its fixed points are exactly the monomials with $a=b+1$.
- Output monomials $(p,0)$ and $(0,q)$ give no further independent conditions.

**Step 3 — case $a=0$.** Here (E) reads $c_{0,b}(b\bar\mu-2\mu)=0$. The factor vanishes only if $\mu/\bar\mu=b/2$. Since $|\mu/\bar\mu|=1$, this forces $\mu/\bar\mu=\pm1$, i.e. $\mu$ real or purely imaginary. Neither holds, so $c_{0,b}=0$.

**Step 4 — two-element orbits** ($a\ge1$, $\phi(a,b)\ne(a,b)$). Write $c_1:=c_{a,b}$ and $c_2:=c_{\phi(a,b)}$. Equation (E) for $(a,b)$ and for $\phi(a,b)$ gives
$$c_1\alpha_1=\mu\bar c_2,\qquad c_2\alpha_2=\mu\bar c_1,$$
with $\alpha_2=(b-1)\mu+(a-1)\bar\mu$.

- If $\alpha_2=0$: then $\mu\bar c_1=0$, so $c_1=0$, and then $c_2=0$.
- Otherwise, eliminating $c_2$ gives $c_1(\alpha_1\bar\alpha_2-|\mu|^2)=0$.

Expand $\alpha_1\bar\alpha_2-|\mu|^2$ and set $m:=|\mu|^2$. Its imaginary part is
$$\Im(\mu^2)\,[(a-2)(a-1)-b(b-1)],\qquad \Im(\mu^2)=2\Re\mu\,\Im\mu\ne0 .$$
So a nonzero solution needs $(a-2)(a-1)=b(b-1)$. That gives two possibilities:

- $b=a-1$: this is the fixed-point case, which is excluded here.
- $b=2-a$, so $k=2$. Since $(0,2)$ is already removed by Step 3, the only two-element orbit here is $(1,1)\leftrightarrow(2,0)$. For it the real part $\Re(\mu^2)[(a-2)(a-1)+b(b-1)]+m[(a-2)(b-1)+b(a-1)-1]$ equals $-m\ne0$.

So every two-element orbit carries only $c=0$.

**Step 5 — fixed points** $(a,a-1)$, degree $k=2a-1$. Here (E) reads $c\,\alpha=\mu\bar c$ with $\alpha=(a-2)\mu+(a-1)\bar\mu$. A nonzero solution needs $|\alpha|=|\mu|$. Since
$$|\alpha|^2-m=(a-1)(a-2)\,\bigl[2m+2\Re\mu^2\bigr]=(a-1)(a-2)\cdot4(\Re\mu)^2,$$
and $\Re\mu\ne0$, this forces $a\in\{1,2\}$.

- $a=1$ is the linear degree, excluded.
- $a=2$ gives $k=3$ and $\alpha=\bar\mu$. The equation $c\bar\mu=\mu\bar c$ means $c\in\mathbb R\mu$, i.e. $Y\in\mathbb RX_3$. $\square$

### Independent check

`dyad_open19_kernel_check.py` (v1.1, exit-gated; SHA-256 `1cb40446…291e`; the v1.0 print-only version was `49ead041…d7f5`) computes real Jacobian brackets with exact sympy arithmetic. It does not use the complex shortcut of Steps 1–5. Result:

- kernel dimension 0 for $k=2$ and for $k=4,\dots,13$;
- kernel dimension 1 for $k=3$, with the kernel field parallel to $X_3$.

This agrees with the general proof. The proof itself covers all $k$; the check is not a substitute for it.

## 2. Theorem C (formal centralizer) `[THM]` `[scope: formal category, real coefficients]`

$$\operatorname{Cent}_{\rm formal,\,DG(0)=I}(F)=\{\exp(sX):s\in\mathbb R\}.$$

*Proof.*

1. Formal maps tangent to the identity form a pro-unipotent group, so $\exp$ and $\log$ are inverse bijections.
2. Let $G=\exp Y$ commute with $F=\exp X$. Then $e^{\operatorname{ad}X}Y=Y$. Write $e^{\operatorname{ad}X}-1=\operatorname{ad}X\cdot\psi(\operatorname{ad}X)$, where $\psi$ is invertible as a power series in the pro-nilpotent operator $\operatorname{ad}X$. Hence $[X,Y]=0$.
3. Let $Y_k$ be the lowest nonzero term of $Y$, with $k\ge2$. The lowest term of $[X,Y]$ is $[X_3,Y_k]\in\mathfrak X_{k+2}$. Since $[X,Y]=0$, $[X_3,Y_k]=0$.
4. By Lemma K, $k=3$ and $Y_3=sX_3$.
5. Then $Y-sX$ also commutes with $X$, and its lowest degree is greater than 3. By Lemma K again, $Y-sX=0$. $\square$

## 3. Corollary U (existence and uniqueness of the formal involution) `[THM]` `[scope: formal]`

Define the explicit formal map
$$R_0:=T^3\circ F^{-1/2}=T^3\circ\exp\!\bigl(-\tfrac12X\bigr).$$

**(i) Existence.** $R_0$ is a formal involution with $DR_0(0)=-I$ that commutes with $T$, hence with $F$.

**(ii) Uniqueness.** Every formal involution $\widehat R$ commuting with $F$ and having $D\widehat R(0)=-I$ equals $R_0$. In particular this applies to every $\widehat R$ commuting with $T$.

*Proof of (i).*
1. $T$ commutes with $F=T^6$, so $\mathrm{Ad}_T X=\log(TFT^{-1})=X$.
2. Hence $T$, and therefore $T^3$, commutes with every $\exp(sX)$.
3. Then $R_0^2=T^6\exp(-X)=F\,F^{-1}=\mathrm{id}$.
4. $DT^3(0)=A^3=-I$ and $D\exp(-X/2)(0)=I$, so $DR_0(0)=-I$.
5. Commutation with $T$ follows from step 2.

*Proof of (ii).*
1. Set $C=\widehat R R_0$. It is tangent to the identity and commutes with $F$. By Theorem C, $C=\exp(sX)$.
2. $R_0$ commutes with $X$, so $\widehat R^2=CR_0CR_0=C^2R_0^2=\exp(2sX)=\mathrm{id}$.
3. Since $X\ne0$, $s=0$. $\square$

No normal-form or normalizer existence is needed. **Identification with the normal-form involution:** for any formal Poincaré–Dulac normalizer $\widehat h$ whose normal form is $\lambda$-equivariant (the standard formal Poincaré–Dulac theorem; DYAD-ALG-NF6 is its degree-6 truncation), $\widehat S:=\widehat h(-I)\widehat h^{-1}$ is such an involution, because $-I=\lambda^3$. So by (ii), $\widehat S=R_0$.

**Certificate** `[ALG]` `[scope: finite jets]`: `dyad_open19_R0_identity_cert.py` (SHA-256 `c8c14442…cf8`; exit-gated, 7 checks; exact $\mathbb Q(i\sqrt3)$ engine `dyad_return_qchi_exact.py`). At truncation degrees $N=6,8,12$ it builds $R_0$ from the primitive one-step map, computing $F^{-1/2}$ as the unique tangent-to-identity square root of $F^{-1}$. It verifies:
- $R_0^2=\mathrm{id}$, $R_0f=fR_0$, $R_0F=FR_0$, $DR_0(0)=-I$;
- the recomputed normalizer satisfies $f\circ h=h\circ n$;
- $\mathcal J_{\le N}(h(-I)h^{-1})=\mathcal J_{\le N}R_0$;
- $[R_0]_2=2h_2$.

At $N=6$ this reproduces RECOG/RRF's $S_6$ (with $s_2=2h_2$). A negative control (square-root factor $\tfrac13$ in place of $\tfrac12$) exits 1. The all-order statement rests on the proof above, not on the certificate.

**Combined with DYAD-THM-LOCAL-INVOLUTION-GERM:** a $C^\infty$ or analytic local involution $R$ commuting with $T$ (or with $T^6$, under the §6.15 hypotheses) is either the identity germ, or satisfies $j^\infty R=R_0=\widehat S$. This holds for both clocks, and they select the **same** formal nontrivial involution.

## 4. Scope and what remains open

- **What closes.** The formal question of OPEN 19 closes. The answer is in the **raw** frame and uses only $X_3$, so no normal-form truncation is involved.
  - Only $\Re\mu\ne0$ and $\Im\mu\ne0$ enter.
  - The lattice term $a_{05}\bar z^5$ plays no role: the kernel argument stops at the cubic level.
- **Not established.**
  - Convergence of $R_0=\widehat S$; analytic or $C^\infty$ existence of a nontrivial commuting involution (Problem B: OPEN; see §5).
  - Any physical exchange or G2 realization: OPEN (SG-14/15, RRF OPEN-A, OFN OPA).
  - Equivalence of the factor contracts $EF=TE$ and $EF=T^6E$: they stay distinct.
- **Relation to the reviewed session result.** The SESSION argument the reviewer accepted, with its `cent.py` finite table, is consistent with this proof. Lemma K now supplies the all-$k$ statement the reviewer required. `cent.py` itself was not available to me and has not been compared.
- **Proposed owner action** (next revision, not v6.4.11):
  - OPEN 19 → CLOSED (formal), with RIDs `DYAD-ALG-CENT-KERNEL` (Lemma K), `DYAD-THM-FORMAL-CENTRALIZER` (Theorem C) and `DYAD-THM-FORMAL-INVOLUTION-UNIQUE` (Corollary U).
  - New OPEN for analytic/$C^\infty$ realization (Problem B).

## 5. Problem B restated `[ALG]` (reduction only)

$T^3$ is analytic and invertible near $0$. So by Corollary U, an **analytic** nontrivial involution commuting with $T$ (or with $F$) exists iff $R_0$ converges. That holds iff the formal tangent-to-identity square root $F^{1/2}=\exp(\tfrac12\log F)$ converges: indeed $F^{1/2}=R_0^{-1}T^3=R_0T^3$.

So Problem B in the analytic class is the question whether the six-step return $F$ has an analytic square root tangent to the identity. (Note $T^3=R_0\circ F^{1/2}$ factors the known analytic square root of $F$, with linear part $-I$, into the involution and the tangent-to-identity root.)

This is a classical embedding/root question for parabolic germs with a cubic leading term. It is not answered here, and no conjecture on its outcome is recorded.

The $C^\infty$ class is different. By a Borel-type realization, smooth maps with any prescribed jet exist, but a smooth involution must also **commute** with $T$. That commutation requirement is the actual content, and it remains OPEN.
