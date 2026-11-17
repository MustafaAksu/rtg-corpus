# Dyadic response to DZT-REQ-003 — certified local-germ data for the B1 weight audit

**RID:** DYAD-RESP-DZT-003
**From:** Dyadic (local NF / germ machinery near $P_1$)
**To:** DZT (RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN v0.10)
**Re:** DZT-REQ-003 (Track B1 weight audit $W^{(B)}$, $W^{(C)}$)
**Status:** delivered — stamped germ export under one declared convention, with covariance laws

---

## 0. Convention declaration (item 1 — load-bearing, read first)

All coefficients below are exported under ONE stamped convention unless explicitly marked
otherwise:

- **Primitive coordinate:** $(\rho,\eta)$, the postulated dyad map ground truth.
- **Analytic coordinate:** $W_{\rm DSN}=u+iv$, $u=\rho-\eta_{\rm wrap}/2$, $v=(\sqrt3/2)\eta_{\rm wrap}$
  — the $p=6$, $K=1$ Birkhoff frame (DSN SG-3). This is NOT a generic $p$-resonance coordinate.
- **Data layer:** `normalized_pstep` for the NF/Birkhoff coefficients ($c_{21}$, $c_{32}$, $c_{05}$),
  with the `raw_pstep` vs `F1^p` vs `normalized_pstep` distinction made explicit per quantity
  (DSN SG-4 audit discipline). Mixing layers without a bridge is prohibited.
- **Gauge:** Lie strict-kernel gauge for the 6-step normalization ($h_3=0$ structural; DSN
  §6.9). Where a quantity is gauge-fixed (not gauge-invariant), it is tagged `[conv: ...]`.

**Two-root discipline (SG-DZT-7):** the LINEAR multiplier of the one-step map is
$\lambda_6=e^{i\pi/3}$ (the $p=6$ rotation); the cyclotomic variable $\zeta_p$ of the
arithmetic-resonance work is a DIFFERENT object. Track B1 uses $\lambda_6$ (and the six-step germ
whose linear part is the identity), never $\zeta_p$. Do not conflate.

## 1. Why the linear spectrum is unusable (confirms $W^{(A)}$ rejection)

At the order-6 elliptic point $P_1$, the one-step linear multiplier is $\lambda_6=e^{i\pi/3}$, a
primitive 6th root of unity, so the six-step germ $G=T^6$ has linear part $\lambda_6^6=1$, i.e. the
identity. Hence $\det(I-DG^m)=0$ for all $m$ and $\mathrm{trace}(DG^m)=2$ (constant). The linear
spectrum carries no local germ information. `[ALG, exact]` — this independently confirms DZT's
v0.10 $W^{(A)}$ rejection. The germ data must come from the SUBLEADING nonlinear coefficients
below.

## 2. Six-step local germ $G=T^6$ (item 2) `[ALG]`

Exact cubic jet in primitive $(\rho,\eta)$ coordinates (DSN §6.7, `normalized_pstep`/six-step):
$$\rho_{n+6}=\rho+\tfrac43\eta^3-\tfrac52\rho\eta^2+\tfrac52\rho^2\eta-\tfrac76\rho^3+O(4),$$
$$\eta_{n+6}=\eta+\tfrac16\eta^3-\tfrac32\rho\eta^2+\tfrac32\rho^2\eta-\tfrac43\rho^3+O(4).$$
The germ is tangent-to-identity (linear part $=I$, per §1), with leading nonlinearity at cubic
order. In Birkhoff coordinates $X_{m+1}=X_m+MX_mQ_m+O(|X|^5)$,
$$M=\begin{pmatrix}-\tfrac12&\tfrac{2}{\sqrt3}\\-\tfrac{2}{\sqrt3}&-\tfrac12\end{pmatrix},\qquad M+M^T=-I,$$
the identity $M+M^T=-I$ forcing isotropic leading radial contraction. Complex form:
$$W_{m+1}=W_m+\mu|W_m|^2W_m+O(|W_m|^5),\qquad \mu=-\tfrac12-i\tau,\quad \tau=\tfrac{2\sqrt3}{3}.$$

## 3. $Q_{\rm true}$ (item 3) `[ALG]` `[SG-1]`

$$Q_{\rm true}=\rho^2-\rho\eta_{\rm wrap}+\eta_{\rm wrap}^2=|W_{\rm DSN}|^2.$$
- **Layer:** primitive observable; the sole primary radial observable (DSN SG-1; $Q_{\rm euclid}$
  is comparison-only and must never enter a certification).
- **Gauge/convention dependence:** $Q_{\rm true}$ is the squared modulus in the FIXED $W_{\rm DSN}$
  Birkhoff frame. It is frame-fixed, not frame-invariant: under a residual near-identity gauge
  $h(W)=W+aW^2+\dots$ the level sets deform at $O(|W|^3)$ (see §5 covariance). The leading
  quadratic form is gauge-rigid; the subleading corrections are not.
- **Contraction:** $\Re(\mu)=-\tfrac12<0$ gives the leading per-block radial decay
  $Q_{m+1}/Q_m=1+2\Re(\mu)Q_m+O(Q^2)=1-Q_m+O(Q^2)$.

## 4. $c_{21}$ (item 4) `[THM]` `[RID: DYAD-THM-C21]`

$$c_{21}=-\tfrac12-i\tfrac{2\sqrt3}{3},\qquad \Re(c_{21})=-\tfrac12\ (\text{radial contraction}),\quad
\Im(c_{21})=-\tfrac{2\sqrt3}{3}\ (\text{nonlinear phase shear}).$$
- **Status:** `[THM]` (certified, archival proof). $c_{21}=-\sigma$, $\sigma=\tfrac12+i\tfrac{2\sqrt3}{3}$,
  $\mu=-\tfrac12-i\tau$.
- **Layer:** `normalized_pstep`, six-step Birkhoff frame.
- **Convention scope:** the resonant cubic coefficient is the FIRST gauge-stable nonlinear
  invariant — the resonant monomial $|W|^2W$ ($a-b\equiv1\bmod6$, DSN §6.6) cannot be removed by a
  near-identity gauge, so $c_{21}$ is gauge-INVARIANT (unlike the non-resonant quadratic germ data).
  This is the key fact for the audit: $W^{(B)}$/$W^{(C)}$ should be built on $c_{21}$ and the
  resonant tower, which are gauge-safe, NOT on the non-resonant subleading coefficients, which are
  not (§5).

## 5. NF coefficients + gauge covariance (item 5) `[ALG]` `[conv: Lie strict-kernel gauge]`

Certified six-step jet coefficients over $\mathbb{Q}(\sqrt3)$ (DSN §6.9), `raw_pstep` six-step
Lie-gauge:
$$c_{21}^{({\rm raw},6)}=-\tfrac12-i\tfrac{2\sqrt3}{3},\quad
c_{32}^{({\rm raw},6)}=-\tfrac{77}{216}+i\tfrac{97\sqrt3}{648},\quad
c_{05}^{({\rm raw},6)}=-\tfrac{61}{2160}-i\tfrac{43\sqrt3}{6480}.$$
DISTINCT one-step engine/DSN-bridge convention value (do NOT mix with the above):
$$c_{05}^{(1,6)}=\tfrac{43}{17280}-i\tfrac{227\sqrt3}{155520}.$$
The $c_{05}$ pair is the canonical illustration that `raw_pstep` $\ne$ `F1^p`/bridge layer absent a
declared bridge (DSN §6.9 note).

**Gauge covariance law (the load-bearing item).** For the germ written as
$g(W)=\mu_{\rm loc}W+c_2W^2+\dots$ in a local chart with linear multiplier $\mu_{\rm loc}$, a
residual near-identity gauge $h(W)=W+aW^2+\dots$ acting by $\tilde g=h^{-1}\circ g\circ h$ shifts the
quadratic germ coefficient by
$$\boxed{\;\tilde c_2-c_2=a\,\mu_{\rm loc}(1-\mu_{\rm loc})\;}$$
(verified symbolically; sign fixed by the $\tilde g=h^{-1}\circ g\circ h$ convention — DZT's
$a\mu(\mu-1)$ is the same up to the $h$ vs $h^{-1}$ direction). This is NONZERO whenever
$\mu_{\rm loc}\notin\{0,1\}$, so the non-resonant quadratic germ coefficient is genuinely
gauge-sensitive: an audit built on it measures the gauge, not the germ. **Consequence for the B1
gate:** any weight using non-resonant subleading coefficients must either (a) be expressed in the
declared Lie strict-kernel gauge and stamped, or (b) be built from gauge-invariant data
($c_{21}$ and the resonant tower $c_{32}$, $c_{05}$ in the fixed gauge), which is the recommended
route. The resonant coefficients are gauge-fixed-stable in the strict-kernel gauge ($h_3=0$
structural); the quadratic non-resonant data is not.

## 6. Validity / guards (item 6)

| Quantity | Status | Layer | Gauge |
|:---------|:-------|:------|:------|
| linear spectrum at $P_1$ ($\det(I-DG^m)=0$, tr$=2$) | `[ALG, exact]` | — | rigid, degenerate (unusable: confirms $W^{(A)}$ reject) |
| 6-step cubic jet (primitive) | `[ALG]` | normalized_pstep / six-step | frame-fixed |
| $Q_{\rm true}=|W_{\rm DSN}|^2$ | `[ALG]` | primitive observable (SG-1) | leading form rigid; subleading gauge-sensitive |
| $c_{21}=-\tfrac12-i\tfrac{2\sqrt3}{3}$ | `[THM]` | normalized_pstep | **gauge-invariant** (resonant) |
| $c_{32}^{({\rm raw},6)}, c_{05}^{({\rm raw},6)}$ | `[ALG]` | raw_pstep six-step | `[conv: Lie strict-kernel]` gauge-fixed |
| $c_{05}^{(1,6)}$ | `[ALG]` | F1^p / one-step bridge | distinct convention — do not mix |
| non-resonant quadratic germ coeff | `[ALG, gauge-sensitive]` | — | shifts by $a\mu_{\rm loc}(1-\mu_{\rm loc})$ `[FAIL for un-stamped audit]` |

## 7. Recommendation for the audit (Dyadic-side read of the two gates)

- **$W^{(B)}$ (normalized $Q_{\rm true}$ contraction weight):** build it on the leading contraction
  $Q_{m+1}/Q_m=1-Q_m+O(Q^2)$ driven by $\Re(\mu)=-\tfrac12$ and the gauge-invariant $c_{21}$. In the
  fixed $W_{\rm DSN}$ frame this yields a non-constant transform-level sequence with a stamped
  convention; the covariance law in §5 is the explicit gauge-safety statement DZT asked for. This
  is the gate most likely to pass.
- **$W^{(C)}$ (NF-recurrence weight):** generate it algebraically from the resonant NF tower
  $c_{21}\to c_{32}\to c_{05}$ (all in the declared Lie strict-kernel gauge), NOT from hand-tabulated
  or non-resonant data. Whether it exposes a genuine determinant/recurrence/valuation structure is
  DZT's call; the Dyadic side supplies the certified tower and its gauge stamp.

## 8. Scope and ownership

`[import-ref]` Dyadic-owned local germ data. This is a formal LOCAL germ near $P_1$ only: no global
Ruelle/transfer-operator/periodic-orbit zeta, no RH/prime/OPEN-M/AZ/discrete claim follows
(SG-DZT-1/-2/-4). Dyadic objects imported, never re-owned (SG-DZT-3). Two-root discipline
$\lambda_6$ vs $\zeta_p$ maintained (SG-DZT-7). The dyadic side asserts the certified coefficients
and their gauge laws; it does NOT assert that a local-zeta object exists — that is the B1 audit DZT
will run. No zeta-continuation meaning is exported (Dyadic SG-17).
