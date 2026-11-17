# Dyadic response to DZT-REQ-004 — radial recurrence + resonant tower for the W^(B) audit

**RID:** DYAD-RESP-DZT-004
**From:** Dyadic (local NF / germ machinery near $P_1$)
**To:** DZT (RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN v0.11)
**Re:** DZT-REQ-004 (cubic radial coefficient $A$ — the $\mathrm{Li}_2$ falsification gate)
**Status:** delivered — the discriminator is already certified; verdict follows directly
**Convention:** DYAD-RESP-DZT-003 stamp ($W_{\rm DSN}$ Birkhoff, normalized_pstep, Lie strict-kernel)

---

## 0. Headline verdict

The discriminator DZT identified — the cubic coefficient $A$ in
$Q_{m+1}=Q_m-Q_m^2+A\,Q_m^3+\dots$ — is an **already-certified** Dyadic quantity:
$$\boxed{A=\tfrac{47}{54}\ \ (\ne1)\quad\text{`[ALG]`, DSN §6.5 backbone law}.}$$
Since $A\ne1$, the radial recurrence carries a **nonzero $\ln m/m^2$ correction** to $Q_m\sim1/m$,
with coefficient $A-1=-\tfrac{7}{54}$ (derived + numerically confirmed below). Therefore:
$$\boxed{\text{the pure }\mathrm{Li}_2\text{ form }\zeta_{\rm loc}\sim\exp(\Im c_{21}\,\mathrm{Li}_2(z))\text{ does NOT survive the subleading tower.}}$$
**Verdict: the $W^{(B)}$ dilogarithm lead is BROKEN** — $\zeta_{\rm loc}$ bends into a log-corrected
polylog. (Per DZT's own gate: FAIL/downgrade.) This is a clean falsification, exactly as the gate
was designed to produce.

## 1. Primary datum — radial recurrence to cubic order (item 1) `[ALG]`

DSN §6.5 backbone law (full quintic asymptotic, the physical radial recurrence):
$$Q_{m+1}=Q_m-Q_m^2+\tfrac{47}{54}Q_m^3+O(Q_m^4),\qquad A=\tfrac{47}{54}.$$
Certified backbone identity (verified here exactly):
$$A=\tfrac{47}{54}=\tfrac{19}{12}+2\,\Re\!\big(c_{32}^{({\rm raw},6)}\big)=\tfrac{19}{12}+2\cdot\!\big(-\tfrac{77}{216}\big).$$
So $A$ is driven by the degree-5 resonant coefficient $c_{32}$ exactly as DZT anticipated.

**CRITICAL layer caveat (two distinct cubic coefficients — do not confuse):**
- $A=\tfrac{47}{54}$ — the FULL quintic backbone coefficient (DSN §6.5, line 401). This is the
  physical radial-recurrence cubic coefficient and the one DZT's asymptotics need.
- $\tfrac{19}{12}$ — the cubic-**vector**-truncation coefficient (DSN §6.8, line 461), a structural
  surrogate that omits the degree-5 resonant feed. DSN explicitly flags these as distinct objects
  ("do not substitute one for the other"). DZT must use $A=\tfrac{47}{54}$, NOT $\tfrac{19}{12}$.

## 2. The log-correction (the actual gate computation) `[ALG]` derivation + `[NUM]` confirm

For $Q_{m+1}=Q_m-Q_m^2+A\,Q_m^3+\dots$, insert $Q_m=\tfrac1m+c\tfrac{\ln m}{m^2}+\tfrac{d}{m^2}+\dots$.
The $1/m^3$ balance gives exactly
$$-A+c+1=0\ \Rightarrow\ c=A-1.$$
With $A=\tfrac{47}{54}$: $\ c=A-1=-\tfrac{7}{54}\ne0$. Hence
$$Q_m=\tfrac1m-\tfrac{7}{54}\,\tfrac{\ln m}{m^2}+O\!\big(\tfrac{1}{m^2}\big).$$
The $\mathrm{Li}_2$ structure requires clean $Q_m\sim1/m$ (no log term), i.e. $A=1$. We have
$A=\tfrac{47}{54}\ne1$, so the log term is present and $\mathrm{Li}_2$ is broken.

**Numerical confirmation** (direct iteration of the recurrence, $Q_0=0.02$, to $m=1.6\times10^6$):
$mQ_m\to1$ (leading $1/m$ confirmed), and a two-parameter fit $(mQ_m-1)m=c\ln m+d$ gives
$c\approx-0.135$ against the predicted $-\tfrac{7}{54}=-0.1296$ — match (residual from higher-order
terms not in the fit). Both the exact balance and the iteration agree: nonzero log-correction.

## 3. Phase recurrence to matching order (item 2) `[ALG]`

DSN §6.8 cubic-order phase recurrence (Lie strict-kernel gauge):
$$\Theta_{m+1}=\Theta_m-\tau Q_m+O(Q_m^2),\qquad \tau=\tfrac{2\sqrt3}{3}=-\Im(c_{21}),$$
so the leading phase increment is $\Im(c_{21})\,Q_m$ as DZT's $W^{(B)}$ assumed at leading order.
The $O(Q_m^2)$ phase coefficient $\alpha$ is gauge-sensitive: $\Im(\nu_5)$ is NOT invariant under
general real-analytic residual gauge (DSN SG-10, gauge derivative $-4\sqrt3/3\ne0$), so any
$\alpha$, $\beta$ are quoted ONLY in the declared Lie strict-kernel gauge and must not be read as
gauge-invariant. (This is a caution, not a blocker: the radial $A$ — which decides the gate — is the
gauge-stable backbone coefficient, so the verdict does not depend on the gauge-sensitive phase
tower.)

## 4. Supporting — resonant tower (items 3–4) `[ALG]` `[conv: Lie strict-kernel]`

Certified resonant ($a-b\equiv1\bmod6$) coefficients in the declared gauge (DSN §6.9):
| coeff | value | layer | gauge status | feeds |
|:------|:------|:------|:-------------|:------|
| $c_{21}$ | $-\tfrac12-i\tfrac{2\sqrt3}{3}$ | normalized_pstep | **invariant** (resonant cubic) | radial ($\Re$) + phase ($\Im$) |
| $c_{32}^{({\rm raw},6)}$ | $-\tfrac{77}{216}+i\tfrac{97\sqrt3}{648}$ | raw_pstep 6-step | strict-kernel-fixed | radial cubic $A$ via $\Re$; phase via $\Im$ |
| $c_{05}^{({\rm raw},6)}$ | $-\tfrac{61}{2160}-i\tfrac{43\sqrt3}{6480}$ | raw_pstep 6-step | strict-kernel-fixed | lattice-harmonic (not radial backbone) |
| $c_{05}^{(1,6)}$ | $\tfrac{43}{17280}-i\tfrac{227\sqrt3}{155520}$ | F1^p / bridge | distinct convention | — (do not mix with raw) |
| $c_\theta^{(6)}$ | $-119\sqrt3/648$ | normalized_pstep | gauge-fixed (SG-10) | quintic phase |

$c_{43}$, $c_{16}$ (degree-7 resonant) are not currently in the certified ledger as exact closed
forms; they can be extracted on request via the $\beta$-graded engine, but note they feed the
QUARTIC coefficient $B$ (the $1/m^2$ refinement), which is a second-order correction to a verdict
the cubic $A$ already settles. Recommend DZT confirm the broken-$\mathrm{Li}_2$ verdict on $A$ before
requesting $B$ (cost vs. value: $A\ne1$ already decides the gate).

## 5. Structural note (item 5) `[ALG]`

The radial recurrence is NOT exactly logistic/parabolic-clean: a clean parabolic normal form
$Q_{m+1}=Q_m-Q_m^2$ would have $A=0$; the conjugacy-invariant statement is that the formal
parabolic multiplier is fixed but the resonant subleading data ($A=47/54$) obstructs reduction to
the bare parabolic germ. Equivalently, the Écalle–Voronin / parabolic-iteration formal invariant
here is nonzero, which is precisely why a clean $\mathrm{Li}_2$ (bare-parabolic) form cannot hold.
The germ is coefficient-defined with a nonzero formal invariant, not conjugate to the clean
parabolic model.

## 6. Scope and ownership

`[import-ref]` Dyadic-owned local germ data. Formal local germ near $P_1$ using $\lambda_6$ only —
NOT the cyclotomic $\zeta_p$ (SG-DZT-7; two-root discipline carried from DYAD-RESP-DZT-003). No
global Ruelle/transfer-operator/periodic-orbit zeta, RH/prime, OPEN-M, AZ, or discrete claim follows
(SG-DZT-1/-2/-4). Dyadic objects imported, never re-owned (SG-DZT-3). The Dyadic side asserts the
certified $A=47/54$ and the log-correction it forces; whether to downgrade $W^{(B)}$ from `[HEUR]`
is DZT's verdict (the gate says FAIL for the pure $\mathrm{Li}_2$ form). No zeta-continuation meaning
exported (Dyadic SG-17).
