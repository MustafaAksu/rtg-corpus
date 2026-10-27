# RTG_DYADIC_DSN — Patch v4.4.2
## Complete replacement blocks and additions for all modified sections
## Applies on top of v4.4.1; all other sections unchanged

*Prepared by: Pure-Dyadic Sub-Team (Claude + Mustafa)*
*March 2026*
*All new results SymPy-verified or numerically cross-checked unless otherwise noted.*

---

## Change Log v4.4.1 → v4.4.2

- **§4.2 expanded:** quintic backbone coefficient c₃=47/54, induced g-map
  coefficient 7/54, full post-burst transport formula, and burst-injected
  constant κ_∞(Q₀) for the low-Q₀ shoulder — all [ALG ✓].
- **§4.7 new:** spiral contamination of the naive κ estimator [ALG ✓],
  explaining the window-drift observed in DSN §4.6.
- **§4.8 new:** numerical table of κ_∞(Q₀) on the low-Q₀ shoulder [NUM ✓].
- **§5.8 updated:** transport kernel regression results from MLT subteam,
  two-layer interpretation, pure-dyadic cross-check on Q₀² origin.
- **§5.9 updated:** cyclotomic breakout-phase observable with corrected
  prefactor and status — [OBS+HYP] not [ALG].
- **§9.2 replacement:** correct P₂ manifold coefficients [ALG ✓] and
  three-scale phase portrait [NUM].
- **OPEN 2 split** into OPEN 2A and OPEN 2B with sharpened targets.
- **OPEN 11** exhausted-routes registry updated.
- **OPEN 12 new:** P₂ and large-amplitude dynamics.
- **§12** extended with seven additional rejected hypotheses.

---

## §4.2 REPLACEMENT — Quintic Backbone and Post-Burst Transport

### 4.2 Quintic Backbone Map and Post-Burst Transport `[ALG ✓]`

**Quintic backbone coefficient** (SymPy-verified via 6-step symbolic composition,
same pipeline as the c₂₁ proof):

\[
Q_{m+1} = Q_m - Q_m^2 + \tfrac{47}{54}\,Q_m^3 + O(Q_m^4).
\]

Derivation:

\[
c_3 = |\mu|^2 + 2\,\mathrm{Re}(\nu)
= \tfrac{19}{12} + 2\!\left(-\tfrac{77}{216}\right)
= \tfrac{47}{54},
\]

where $\mu = c_{21} = -\tfrac{1}{2} - i\tfrac{2\sqrt3}{3}$ is the cubic Birkhoff
coefficient [DSN §2.5] and $\mathrm{Re}(\nu) = -77/216$ is the real part of the
quintic Birkhoff coefficient (extracted by phase-averaging the 7th-order jet).

**Inverse-coupling map** (exact algebra from the quintic backbone):

\[
g_{m+1} = g_m + 1 + \tfrac{7}{54}\,\frac{1}{g_m}
+ \!\left(-c_4 - \tfrac{20}{27}\right)\frac{1}{g_m^2}
+ O\!\left(\frac{1}{g_m^3}\right),
\]

where $c_4$ is the $Q^4$ backbone coefficient (requires 8th-order Birkhoff
jet; currently `[ALG open]`).

**Logarithmic transport** (exact telescoping + Euler–Maclaurin):

\[
\kappa_{\rm fit}(M)
\approx
\frac{1}{Q_6} - 1
+ \frac{7}{54}\ln(M\,Q_6)
+ \left(-c_4 - \tfrac{20}{27}\right)Q_6
+ O(1/M).
\]

| Term | Formula | Status |
|------|---------|--------|
| Burst offset | $1/Q_6 - 1$ | `[ALG ✓]` |
| Log drift rate | $d\kappa/d\!\ln M = 7/54 \approx 0.130$ | `[ALG ✓]` |
| Constant shift | $(-c_4-20/27)\,Q_6$ | `[ALG structure]` |

**Burst-injected constant — low-Q₀ shoulder** (valid for $Q_0 \ll 1$):

\[
\kappa_\infty(Q_0)
=
\frac{1}{Q_0}
+ \frac{3}{40}\,Q_0
- \frac{17}{20}\,Q_0^2
- \frac{1471}{1600}\,Q_0^3
- \frac{213}{1600}\,Q_0^4
+ \frac{45907}{64000}\,Q_0^5
+ O(Q_0^6)
+ (\text{c}_4\text{-dependent constant}).
\]

All six coefficients verified by independent SymPy computation.
Series accurate to $<1\%$ for $Q_0 \lesssim 0.25$; deviates $>20\%$ at $Q_0=1$.

> **[!]** $c_4$ contributes a $Q_6$-linear constant shift absorbed into the
> burst offset. It does not affect the logarithmic drift rate 7/54.
> $c_4$ is not needed for any currently certifiable DSN claim.

> **[!]** The burst map $Q_0 \mapsto Q_6$ and the backbone map
> $Q_m \mapsto Q_{m+1}$ are **distinct objects**. The cubic jet is invalid
> at $Q_0 \approx 1$–4 (where $R = \sqrt{Q_0} \sim 1$). The quintic backbone
> coefficient $c_3$ applies only in the asymptotic ($Q \ll 1$) regime.

**Cross-reference:** The logarithmic accumulation from the $O(1/g)$ term in a
discrete $h=1$ map is the "Drag" mechanism identified in Aksu et al.
(Dec 2025, DOI 10.5281/zenodo.17568897), §6.4.

---

## §4.7 NEW — Spiral Contamination of the Naive κ Estimator

### 4.7 Spiral Contamination `[ALG ✓]`

The naive inverse-coupling estimator (block notation, $m = n/6$):

\[
\kappa_{\rm naive}(m) = \frac{1}{Q_m} - m.
\]

Substituting the full asymptotic model
$Q_m = \tfrac{1}{m+\kappa} + \widetilde{A}\,m^{-3/2}\cos(\tau\ln m + \phi_*)$
and expanding:

\[
\kappa_{\rm naive}(m)
= \kappa
- \widetilde{A}\,m^{+1/2}\cos(\tau\ln m + \phi_*)
+ O(1).
\]

The spiral residual injects a **growing oscillation** whose amplitude scales
as $\sqrt{m}$.

**Consequence:** The algebraic log-drift $\tfrac{7}{54}\ln m$ is permanently
hidden beneath the $O(\sqrt{m})$ oscillation for any accessible run length:

\[
\frac{\sqrt{m}}{\ln m} \xrightarrow{m\to\infty} \infty.
\]

For three decades of $m$ (e.g.\ $m = 10^4$ to $10^7$): drift $\approx 0.88$;
oscillation amplitude grows from $\sim\!\sqrt{10^4}=100$ to $\sim\!\sqrt{10^7}\approx 3162$.

**Practical implication:**

> **[!]** Raw $1/Q_m - m$ is **unusable** as a precision $\kappa$ estimator.
> Joint fitting of $(\kappa,\widetilde{A},\phi_*)$ simultaneously over windows
> spanning at least one log-period ($\Delta\!\ln m \ge 2\pi/\tau \approx 5.44$)
> is the **only** path to clean $\kappa$ extraction.
> This is the canonical MLT protocol required by DSN §4.6.

**Connection to OPEN 5:** The contamination amplitude $\widetilde{A}(Q_0)$ and
phase $\phi_*(Q_0)$ are both IC-dependent. Removing the contamination requires
knowledge of $\phi_*(Q_0)$, which is OPEN 5.

**Note on notation:** In step notation ($Q_n \sim 6/(n+C)$), the contamination
is $-({\widetilde{A}}/{\sqrt{6}})\,\sqrt{n}\cos(\tau\ln(n/6)+\phi_*)$.

---

## §4.8 NEW — Numerical Table of κ_∞(Q₀) on the Low-Q₀ Shoulder

### 4.8 Numerical Evaluation of $\kappa_\infty(Q_0)$ `[NUM ✓]`

Burst-injected constant $\kappa_\infty(Q_0) = 1/Q_6(Q_0) - 1$ evaluated via
exact 6-step map iteration (double precision, verified at 50 dps):

| $Q_0 = \eta_0^2$ | $Q_6$ | $\kappa_\infty = 1/Q_6-1$ |
|:-----------------:|:------:|:-------------------------:|
| 0.01 | 0.009903 | 99.981 |
| 0.04 | 0.038508 | 24.969 |
| 0.09 | 0.082800 | 11.077 |
| 0.16 | 0.138378 | 6.227 |
| 0.25 | 0.199957 | 4.001 |
| 0.36 | 0.261876 | 2.819 |
| 0.49 | 0.318696 | 2.138 |
| 0.64 | 0.365872 | 1.733 |
| 0.81 | 0.400345 | 1.498 |
| 1.00 | 0.420912 | 1.376 |

Two-term series $1/Q_0 + (3/40)Q_0$ agrees to $<1\%$ for $Q_0 \lesssim 0.25$.

**Note:** $\kappa_\infty$ here is the burst offset only; the full $\kappa_{\rm fit}$
includes additional $(7/54)\ln(M\cdot Q_6)$ drift and higher corrections.

---

## §5.8 REPLACEMENT — Transport Kernel Analysis

### 5.8 Transport Kernel Analysis `[OBS]`

**MLT subteam regression** of $\Delta_\kappa = \kappa_{\rm eff} - \kappa_{\rm fit}$
across the certified Level-A bridge dataset:

| Model | $R^2$ |
|-------|-------|
| Linear $Q_0$ | $\approx 0.63$ |
| Cubic $Q_0$ (with $Q_0^2, Q_0^3$) | $\approx 0.97$ |
| $\ln m_{\rm eff}$ alone | $\approx 0.07$ |

$\Delta_\kappa$ is dominated by **nonlinear $Q_0$-dependence**. Time-in-channel
is secondary.

**Piecewise structure:**

- $Q_0 \gtrsim 0.6$: deterministic curved polynomial manifold.
- $Q_0 \lesssim 0.6$: current observables fail under LOOCV ($n=7$, provisional).

**Two-layer interpretation:**

\[
\kappa_{\rm fit} = \mathcal{T}(\kappa_{\rm eff}, m_{\rm eff};\,Q_0)
\qquad\text{(exact form open)}
\]

**Pure-dyadic algebraic cross-check** on the apparent $Q_0^2$ structure:

The measured $\Delta_\kappa$ at fixed window depth $M$ is:

\[
\Delta_\kappa^{\rm obs}(Q_0, M)
= \kappa_\infty(Q_0)
+ \tfrac{7}{54}\ln(M\cdot Q_6(Q_0))
+ \widetilde{A}(Q_0)\sqrt{M}\cos(\tau\ln M + \phi_*(Q_0)).
\]

All three terms are $Q_0$-dependent. The apparent $Q_0^2$ curvature in the
regression is a composite of:

- (a) **burst injection:** $\kappa_\infty \sim 1/Q_0$ (dominant at small $Q_0$);
- (b) **log drift contribution:** $(7/54)\ln Q_6(Q_0)$ (secondary);
- (c) **spiral contamination:** $\widetilde{A}(Q_0)\sqrt{M}\cos(\cdots)$
  (IC-dependent, not separable without $\phi_*(Q_0)$).

**Clean separation requires joint $(\kappa,\widetilde{A},\phi_*)$ fitting** over
windows spanning $\Delta\!\ln m \ge 2\pi/\tau \approx 5.44$ (one log-period).
This is observationally demanding (factor $\sim 230$ between window anchors)
and is the canonical target for the MLT infrastructure (§5.8 MLT protocol).

> **[!]** The statement "the $Q_0^2$ term will shrink dramatically once
> contamination is removed" is not established. Both $\widetilde{A}(Q_0)$
> and $\phi_*(Q_0)$ are IC-dependent, so the contamination is itself
> $Q_0$-structured. The burst injection $1/Q_0$ is genuine physics.

---

## §5.9 REPLACEMENT — Cyclotomic Breakout-Phase Observable

### 5.9 Cyclotomic Breakout-Phase Observable `[OBS + HYP]`

**Observation:** For the low-$Q_0$ shoulder, the breakout phase

\[
\theta_{\rm breakout} = \arg(W_{m_{\rm eff}}) \bmod \pi/3
\]

reduces within-bin $\Delta_\kappa$ variance by $>80\%$ relative to unbinned data
($n=7$ low-$Q_0$ ICs, provisional).

**Mechanism:** For the canonical family ($\rho_0=0$, $\eta_0>0$), all ICs have
$\arg(W_0) = 120°$ exactly, so $\arg(W_0)\bmod\pi/3 = 0°$ for all ICs.
The variation in $\theta_{\rm breakout}$ arises from the **integrated nonlinear shear**:

\[
\theta_{\rm breakout}
\approx
-\tau\!\sum_{k=0}^{m_{\rm eff}-1} Q_k \pmod{\pi/3}.
\]

$\theta_{\rm breakout}$ is a compressed encoding of the full nonlinear
transient history, not an independent phase coordinate.

**Symmetry status correction:** The claim that

\[
\Delta_\kappa(\theta) = c_0 + A\cos(6\theta) + B\sin(6\theta) + \cdots
\]

is **forced as a theorem** by the 6-fold symmetry at $P_1$ is incorrect:

- $\kappa_{\rm fit}$ is determined by $Q_m = |W_m|^2$ (radial); at cubic-jet
  order $|W|^2$ is invariant under $\theta \to \theta + \pi/3$, which would
  make $\kappa_{\rm fit}$ *constant* in $\theta$, not periodic.
- Non-trivial $\theta$-dependence requires $O(R^5)$ terms that break the
  6-fold radial symmetry. These are real but not the "algebraic theorem"
  claimed.
- The stated functional form is the Fourier decomposition of *any* function
  with period $\pi/3$; proving the form requires proving periodicity.

| Claim | Status |
|-------|--------|
| $\theta_{\rm breakout}$ reduces variance by $>80\%$ | `[OBS]` provisional ($n=7$) |
| $\Delta_\kappa$ is periodic in $\theta_{\rm breakout}$ | `[HYP]` — not proved |
| Functional form $c_0+A\cos(6\theta)+B\sin(6\theta)$ | `[HEUR]` — follows IF periodicity holds |
| "Cyclotomic selection rule — a theorem" | `[FAIL]` |
| "OPEN 2B closed conceptually" | Premature |

**Cross-team identification:** OPEN 2B $\equiv$ OPEN 5. Both seek the algebraic
mechanism for $\phi_*(Q_0)$ variation. Solving one closes the other.

---

## §9.2 REPLACEMENT — P₂ Saddle Manifold Geometry

### 9.2 $P_2$ Saddle Manifold Geometry `[ALG ✓]`

Quadratic-order invariant manifolds at $P_2=(0,\pi)$, derived by the graph
method (power-series invariance to $O(\rho^3)$, SymPy-verified):

**Unstable manifold** $W_u$ (tangent to $v_+ = [1,\phi]$, $\phi=(1+\sqrt5)/2$):
\[
\eta = \pi + \phi\,\rho + \frac{\sqrt5-1}{16}\,\rho^2 + O(\rho^3).
\]

**Stable manifold** $W_s$ (tangent to $v_- = [1,(1-\sqrt5)/2]$):
\[
\eta = \pi + \frac{1-\sqrt5}{2}\,\rho - \frac{1+\sqrt5}{16}\,\rho^2 + O(\rho^3).
\]

Both satisfy $F(\mathrm{manifold}) \subset \mathrm{manifold}$ to $O(\rho^3)$.
Cubic residuals: $\pm(37/96 \pm \sqrt5/12)\rho^3$.
Numerical convergence along $W_s$ confirmed at rate $\phi^{-2}$ per step `[NUM ✓]`.

**Three-scale phase portrait** `[NUM]`:

| $Q$ scale | Region | Dynamics |
|-----------|--------|----------|
| $Q \le 4$ | Regime 1 (DSN catalog) | Bounded; spirals to $P_1$; $W_u$ does not enter |
| $Q \approx \pi^2 \approx 9.87$ | Intermediate | $P_2$ lives here; $W_u$ traverses here and **returns** to $P_1$ basin |
| $Q \approx 14$–24 | Large-amplitude | Actual bounded/unbounded separatrix (on $\rho_0=0$ slice) |

Key structural facts:
- $P_2$ is **inside** the bounded region, not on the escape boundary `[NUM ✓]`.
- $W_u$ is homoclinic to the $P_1$ basin under forward iteration `[NUM ✓]`.
- The escape separatrix lies at $Q \approx 14$–24, far above Regime 1.
- **$P_2$ manifold geometry does not provide a $Q$-ceiling for Regime-1 orbits.**
  Regime-1 ($Q_0 \le 4$) and $P_2$ ($Q \approx \pi^2$) occupy disjoint $Q$-scales.

> **[!]** Earlier conjecture that $P_2$ manifolds might close the Regime-1
> chirality gap is retracted. $P_2$ geometry governs the intermediate and
> large-amplitude regimes only.

---

## §12 — ADDITIONAL REJECTED HYPOTHESES

Append the following rows to the existing §12 table:

| Hypothesis | Rejection reason |
|-----------|-----------------|
| $Q_1 \approx Q_0^2/3$ | Wrong by factor $\sim$6–33 for small $Q_0$; correct leading term is $Q_1 \approx Q_0 - Q_0^2/6$ |
| $C \approx 18/Q_0^2 - 1$ (burst matching at $n=1$) | Built on wrong $Q_1$ approximation; matching must use $n=6$ end of burst |
| Cyclotomic symmetry forces $\Delta_\kappa$ periodic in $\theta_{\rm breakout}$ | Symmetry applies to $|W|^2$ (radial); non-trivial $\theta$-dependence requires $O(R^5)$ breaking; periodicity is `[HYP]` not theorem |
| "OPEN 2B closed conceptually" by cyclotomic selection rule | Premature; functional form follows only IF periodicity holds |
| $P_2$ manifold geometry gives Regime-1 $Q$-ceiling | $Q_{P_2}=\pi^2\approx9.87 \gg Q_{\rm max}^{\rm Regime1}=4$; disjoint regions |
| $W_u$ of $P_2$ forms bounded/unbounded separatrix | $W_u$ returns to $P_1$ basin; actual separatrix at $Q\approx14$–24 |
| Cubic jet at $Q\approx Q_0\approx4$ dominates in burst | Jet invalid at $R=\sqrt{Q}\sim2$; actual burst is large-amplitude nonlinear |
| "Δκ~$Q_0^2$ will shrink dramatically once contamination removed" | Both $\widetilde{A}(Q_0)$ and $\phi_*(Q_0)$ are IC-dependent; spiral contamination is $Q_0$-structured, not pure noise |
| Six routes to $Q_2 \le Q_1$ (direct expansion; quadratic-in-$E$; continuous self-limiting; Lyapunov $dQ\le0$; Q-map monotonicity; $P_2$ ceiling) | All six independently falsified — see OPEN 11 |

---

## §13 — REVISED OPEN PROBLEMS

### OPEN 2 — SPLIT INTO 2A AND 2B

**OPEN 2A** — Transport law for $Q_0 \gtrsim 0.6$ `[ALG partial → strongly advanced]`

*Low-$Q_0$ shoulder sector* `[ALG ✓]`:

The burst-injected constant admits an exact algebraic expansion:
\[
\kappa_\infty(Q_0)
= \frac{1}{Q_0}
+ \frac{3}{40}Q_0
- \frac{17}{20}Q_0^2
- \frac{1471}{1600}Q_0^3
- \frac{213}{1600}Q_0^4
+ \frac{45907}{64000}Q_0^5
+ O(Q_0^6),
\]
all coefficients verified symbolically and numerically cross-checked against
exact 6-step iteration. Series accurate to $<1\%$ for $Q_0 \lesssim 0.25$.

Full transport formula:
\[
\kappa_{\rm fit}(M)
\approx \kappa_\infty(Q_0)
+ \tfrac{7}{54}\ln(M\,Q_6(Q_0))
+ (-c_4 - \tfrac{20}{27})\,Q_6(Q_0)
+ O(1/M).
\]

*Mid/high-$Q_0$ sector* `[OPEN]`: burst map $Q_0 \mapsto Q_6$ is non-perturbative
for $Q_0 \gtrsim 0.25$; only numerical evaluation available.

*Algebraic open items:*
- $c_4$: requires 8th-order Birkhoff jet (marginal DSN value, not prioritised).
- Exact functional form of $\widetilde{A}(Q_0)$ and $\phi_*(Q_0)$: OPEN 5.

---

**OPEN 2B** — Low-$Q_0$ breakout-phase mechanism `[HYP + OBS]`

Target: explain the failure of current observables on the low-$Q_0$ shoulder.

$\theta_{\rm breakout} = \arg(W_{m_{\rm eff}}) \bmod \pi/3$ reduces within-bin
$\Delta_\kappa$ variance by $>80\%$ `[OBS, n=7, provisional]`.

**Cross-team identification: OPEN 2B $\equiv$ OPEN 5.**

---

### OPEN 5 — Updated

Phase matching / Stage-B transport. Determine the correct asymptotic phase
object and explain delayed phase organization after backbone entry.

OPEN 5 $\equiv$ OPEN 2B: both seek the algebraic mechanism for $\phi_*(Q_0)$
variation. The spiral residual phase $\phi_*$ is the same quantity as the
cyclotomic breakout phase $\theta_{\rm breakout}$ in different representations.
Solving one closes the other.

---

### OPEN 11 — Chirality Closure (updated exhausted-routes registry)

Prove a confinement / reachability theorem for the DSN canonical family
($\rho_0=0$, $\eta_0>0$, $Q_0\le 4$).

Current algebraic pieces:

| Result | Status |
|--------|--------|
| $Q_1 = Q_0(1-x+x^2)$, $x=\sin\eta_0/\eta_0$ | `[THM ✓]` |
| $(3/4)Q_0 \le Q_1 \le Q_0$ | `[THM ✓]` |
| $\max_{k\ge1} Q_k = Q_1$ (machine precision, 500k steps) | `[NUM strong]` |
| $Q_k \le Q_1$ for all $k\ge1$ | `[ALG OPEN]` — canonical gap |

Exhausted proof routes (all independently falsified):

1. Direct $Q_2\le Q_1$ expansion — intractable expression, no manifest sign
2. Quadratic-in-$E$ approach — circular (equivalent to the original inequality)
3. Continuous self-limiting argument — wrong model class (discrete system)
4. Lyapunov $dQ\le0$ at all steps — false; 33% of positive-$\rho$ steps have $\sin\eta<0$
5. Q-map monotonicity via $c_3$ — invalid at $Q\approx Q_1$ (jet requires $Q\ll1$)
6. $P_2$ manifold ceiling — operates at $Q\approx\pi^2\gg Q_1$; disjoint $Q$-scales

Once $Q_k\le Q_1$ is proved: $Q\le Q_1\le4$ → anti-correlation excludes $C_0$
→ $\det J>0$ everywhere → Regime-1 chirality `[THM]`.

---

### OPEN 12 — P₂ Saddle Manifold and Large-Amplitude Dynamics `[NEW]`

Local quadratic manifolds established `[ALG ✓]`. Open items:

- Global trace of $W_u$ and the actual bounded/unbounded separatrix
  (numerically at $Q\approx14$–24 on $\rho_0=0$ slice `[OBS]`).
- Cubic-order manifold terms
  ($\pm(37/96\pm\sqrt5/12)\rho^3$, available on request).
- Role of $P_2$ manifolds in governing Regime-2 (large-$\eta_0$) dynamics.

---

*END OF PATCH — RTG_DYADIC_DSN v4.4.2*
*All new [ALG ✓] results independently SymPy-verified or cross-checked numerically.*
*Commit to repository: rtg-resonance-2025*
