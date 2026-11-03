# Dyad-to-Triad Antisymmetric Bridge  v1.1

**Status:** DSN companion document, RTG dyadic program  
**Certifying instances:** Exact cyclotomic engine (OPEN 9 prerequisites) + mpmath numerical checks (60–100 dps)  
**Revision note v1.1:** Corrected area/Jacobian statement (§6), corrected Genesis lift formula (§10).  
**Prerequisite:** OPEN 9 finite ledger p=5,6,7 sealed [ALG]; see `OPEN9_full_onestep_normalization_table_v2.md`.

---

## §1. Primitive dyad — exact odd-channel identity

**Map:**

$$T(\rho,\eta) = \bigl(\rho - \sin\eta,\; \eta + K(e^\rho - 1) - K\sin\eta\bigr)$$

**Primitive case:** $K = 1$ (coincides with $K_6$, the $p=6$ parameter).

**Theorem [ALG]:** For any $x = (\rho,\eta)$ and displacement vector $v = (a,b)$:

$$\Delta_c T_\rho = 2ca - 2\cos\eta\cdot\sin(cb)$$

$$\Delta_c T_\eta = 2cb + 2e^\rho\sinh(ca) - 2\cos\eta\cdot\sin(cb)$$

**Corollary [ALG]:** Only odd powers of $c$ appear in $\Delta_c T = T(x+cv) - T(x-cv)$. **Quadratic fatigue cancels identically.**

*Proof:* $\sinh$ and $\sin$ are odd functions of their arguments. ∎

**Jacobian note [ALG]:** The primitive map is **not** globally area-preserving:

$$\det \nabla T = 1 + K\cos\eta\,(e^\rho - 1)$$

At the fixed point $(\rho, \eta) = (0, 0)$: $\det = 1$ ✓, enabling Birkhoff NF. Away from the origin: $\det \neq 1$ in general.

**Scope:** The odd-channel identity holds for any $v$, any $x$, for arbitrary $K$ (not just $K=1$).

---

## §2. Canonical p=6 eigenframe — W-coordinate

**Definition [ALG, p=6, K=1]:** The complex coordinate adapted to the $p=6$ eigenvalue $\lambda = e^{i\pi/3}$ is

$$W = \rho + \omega\eta, \qquad \omega = e^{2\pi i/3} = -\tfrac{1}{2} + i\tfrac{\sqrt{3}}{2}$$

so $W = s + ic$ with

$$s = \Re W = \rho - \tfrac{\eta}{2}, \qquad c = \Im W = \tfrac{\sqrt{3}}{2}\,\eta$$

**Inverse:**

$$\boxed{(\rho, \eta) = \left(s + \frac{c}{\sqrt{3}},\; \frac{2c}{\sqrt{3}}\right)}$$

**Frame bridge:** $W = W_\mathrm{DSN}^{(p=6)} = i\sqrt{3}\,Z_\mathrm{eng}$ where $Z_\mathrm{eng}$ is the engine eigenframe variable.

**Canonical transverse direction [ALG, p=6, K=1]:** At fixed $s$,

$$\boxed{v_\perp = \left(\frac{1}{\sqrt{3}},\, \frac{2}{\sqrt{3}}\right)} \qquad \left[\frac{\partial(\rho,\eta)}{\partial c}\bigg|_s\right]$$

---

## §3. Primitive one-step antisymmetric channel at $P_1 = (0,0)$

**Theorem [ALG, p=6, K=1]:** With $v = v_\perp$ around $P_1 = (0,0)$:

$$\Delta_c T_\rho = -\frac{2}{\sqrt{3}}c + \frac{8}{9\sqrt{3}}c^3 + O(c^5)$$

$$\Delta_c T_\eta = \frac{2}{\sqrt{3}}c + \frac{\sqrt{3}}{3}c^3 + O(c^5)$$

**In W-coordinates:**

$$\boxed{\Delta_c W' = 2\lambda\,ic + \left(\frac{7\sqrt{3}}{54} + \frac{i}{2}\right)c^3 + O(c^5), \qquad \lambda = e^{i\pi/3}}$$

*Derivation:* $\Delta_c W' = \Delta_c T_\rho + \omega\,\Delta_c T_\eta$.  
- Linear: $(2c/\sqrt{3})(-1+\omega) = c(-\sqrt{3}+i) = 2\lambda\,ic$ ✓  
- Cubic: $(8/(9\sqrt{3}) + \omega\sqrt{3}/3)c^3 = (7\sqrt{3}/54 + i/2)c^3$ ✓

**Interpretation:** The transverse mode $c$ rotates by $\lambda = e^{i\pi/3}$ per step at linearization. The cubic antisymmetric correction carries both chiral phase ($7\sqrt{3}/54$) and transverse modulation ($i/2$).

---

## §4. One-step to p-step bridge lemma

**Lemma [ALG]:** For the one-step Birkhoff normal form

$$W' = \lambda W + \nu_3 |W|^2 W + O(|W|^5), \qquad \lambda = e^{2\pi i/p}, \quad \lambda^p = 1$$

the $p$-step return map satisfies

$$\boxed{F^p(W) = W + p\,\bar\lambda\,\nu_3\,|W|^2 W + O(|W|^5)}$$

so the $p$-step healing cubic coefficient is

$$\boxed{\mu_p = p\,\bar\lambda\,\nu_3^{(1,p)}}$$

*Proof by induction:* If $W_{n+k} = \lambda^k W_n + k\lambda^{k-1}\nu_3|W_n|^2 W_n + O(5)$, then (using $|W_{n+k}|^2 \approx |W_n|^2$ at cubic level):

$$W_{n+k+1} = \lambda^{k+1}W_n + (k{+}1)\lambda^k\nu_3|W_n|^2W_n + O(5)$$

At $k=p$: $\lambda^p = 1$, $\lambda^{p-1} = \bar\lambda$ (since $|\lambda|=1$). ∎

**Scope:** Requires $\lambda^j \neq 1$ for $j = 1,\ldots,p-1$.

**Verification for $p=6$ [ALG]:**

$$\mu_6 = 6\bar\lambda\cdot\nu_3^{(1,6)} = 6\cdot\tfrac{1-i\sqrt{3}}{2}\cdot\left(\tfrac{1}{8} - i\tfrac{7\sqrt{3}}{72}\right) = -\tfrac{1}{2} - i\tfrac{2\sqrt{3}}{3} = \mu \checkmark$$

residual $< 6\times10^{-61}$.

**Consequence:** The one-step and $p$-step time scales carry no independent information — $\mu_p$ is fully determined by $\nu_3^{(1,p)}$ once $p$ is fixed.

---

## §5. Six-step slow-healing antisymmetric channel

**Map [ALG, p=6 slow module]:**

$$F(W) = W + \mu|W|^2W + O(|W|^5), \qquad \mu = -\tfrac{1}{2} - i\tau, \qquad \tau = \tfrac{2\sqrt{3}}{3}$$

**Antisymmetric channel [ALG, p=6]:** For $W_\pm = s \pm ic$, $R^2 = s^2+c^2$:

$$\boxed{F(s+ic) - F(s-ic) = 2ic\bigl[1 + \mu R^2\bigr] + O(R^5)}$$

*Proof:* $|W_+|^2 = |W_-|^2 = R^2$, so $F(W_\pm) = (1+\mu R^2)W_\pm + O(R^5)$. ∎

**Explicit real form:**

$$\Delta F = \underbrace{2ic\!\left(1-\tfrac{R^2}{2}\right)}_{\text{transverse + healing}} + \underbrace{2\tau c\,R^2}_{\text{longitudinal relay}} + O(R^5)$$

- $\mathrm{Re}(\mu) = -1/2$: isotropic transverse damping/healing  
- $\mathrm{Im}(\mu) = -\tau$: chiral relay converting transverse amplitude $c$ into longitudinal displacement $\tau R^2 c$

---

## §6. Dyadic local protection matrix

**Definition [ALG, p=6 slow normal form]:** The six-step map $F: W \mapsto W + \mu R^2 W$ acts on coordinates $(s,c)$ via real-linear representation of complex multiplication by $1+\mu R^2 = (1-R^2/2) - i\tau R^2$:

$$\boxed{\mathcal{P}_\mathrm{dyad}(R^2) = \begin{pmatrix}1-R^2/2 & \tau R^2 \\ -\tau R^2 & 1-R^2/2\end{pmatrix}}$$

so $F(s,c)^T = \mathcal{P}_\mathrm{dyad}(R^2)\cdot(s,c)^T + O(R^5)$.

**Structure:**

$$\mathcal{P}_\mathrm{dyad} = \left(1-\tfrac{R^2}{2}\right)I + \tau R^2 J, \qquad J = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$$

decomposing into isotropic healing and chiral shear.

**Eigenvalues:** $1+\bar\mu R^2$ and $1+\mu R^2$ (complex conjugate pair), with modulus

$$|\alpha|^2 = \left(1-\tfrac{R^2}{2}\right)^2 + \tau^2 R^4 = 1 - R^2 + \tfrac{19}{12}R^4 < 1 \quad (R > 0 \text{ small})$$

confirming local amplitude contraction.

**Determinant clarification [ALG]:** The matrix $\mathcal{P}_\mathrm{dyad}$ is the "frozen-amplitude" linear factor; it is **not** the full Jacobian of the nonlinear map. Their determinants differ:

| object | $\det$ |
|---|---|
| $\mathcal{P}_\mathrm{dyad}$ (frozen-amplitude multiplier) | $1 - R^2 + \tfrac{19}{12}R^4$ |
| $\nabla F$ (true Jacobian of $W \mapsto W+\mu R^2W$) | $1 - 2R^2 + \tfrac{19}{4}R^4$ |
| primitive map $\nabla T$ | $1 + K\cos\eta(e^\rho-1)$ |

The primitive dyad is **not** globally area-preserving ($\det\nabla T \neq 1$ in general). The Birkhoff NF applies locally because $\det\nabla T|_{(0,0)} = 1$.

$$\boxed{\text{Do not interpret }\det\mathcal{P}_\mathrm{dyad}\text{ as area preservation of the primitive map.}}$$

**Key dimensionless invariant [ALG]:**

$$\boxed{\frac{-\mathrm{Im}(\mu)}{-\mathrm{Re}(\mu)} = \frac{\tau}{1/2} = 2\tau = \frac{4\sqrt{3}}{3} \approx 2.309}$$

This chiral-shear-to-healing ratio is convention-free (frame rescalings cancel) and is a genuine dyadic export candidate for Genesis.

---

## §7. UV lift obstruction

**Obstruction [ALG structure]:** Suppose Genesis provides a face/triad variable $w$ with complex lift $W = \gamma w$ where $\gamma = \beta e^{i\chi}$. Then:

$$\gamma w' = \gamma w + \mu|\gamma w|^2\gamma w + O(5)$$

$$\boxed{w' = w + \mu\beta^2|w|^2 w + O(|w|^5)}$$

The phase $\chi$ cancels exactly (since $|γw|^2 = \beta^2|w|^2$ regardless of $\chi$). The Genesis-frame cubic coefficient is $\mu\beta^2$, where $\beta = |\gamma|$ is the only lift scale that appears.

**What the dyad supplies without Genesis input:**
- $\mu, \tau$ and the ratio $4\sqrt{3}/3$ (dimensionless)
- $\mathcal{P}_\mathrm{dyad}(R^2)$ parametrically in $R$
- Primitive cubic antisymmetric correction: $7\sqrt{3}/54 + i/2$

**What requires Genesis input:**
- Lift scale $\beta$ (absolute; not derivable locally)
- Genesis UV parameters $\alpha_f, \sigma_f$, face variable $|w|$

---

## §8. Status ledger

| Result | Status |
|---|---|
| Odd-channel identity: only odd powers of $c$ | `[ALG]` |
| Canonical $W = \rho+\omega\eta$ embedding | `[ALG, p=6, K=1]` |
| $v_\perp = (1/\sqrt{3}, 2/\sqrt{3})$ | `[ALG, p=6, K=1]` |
| $\Delta_c W' = 2\lambda ic + (7\sqrt{3}/54+i/2)c^3 + O(c^5)$ | `[ALG, p=6, K=1]` |
| $\mu_p = p\bar\lambda\nu_3^{(1,p)}$ bridge lemma | `[ALG]` (all $p$, no intermediate resonance) |
| $\Delta F = 2ic[1+\mu R^2]+O(5)$ | `[ALG, p=6]` |
| $\mathcal{P}_\mathrm{dyad}(R^2)$ protection matrix | `[ALG, p=6 slow module]` |
| $-\mathrm{Im}(\mu)/(-\mathrm{Re}(\mu)) = 4\sqrt{3}/3$ | `[ALG]` |
| Primitive dyad not globally area-preserving | `[ALG]` — $\det\nabla T = 1 + K\cos\eta(e^\rho-1)$ |
| Genesis phase $\chi$ cancels; only $\beta^2$ appears | `[ALG]` |
| UV lift obstruction ($\beta$ not determined locally) | `[ALG structure]` |
| Triad lift $(\beta, w)$ | `[OPEN — Genesis input required]` |

---

## §9. Critical scope warnings

1. **K=1 specificity.** Sections §2–§3 use the $p=6$ primitive dyad ($K=1$). For $p=7$ ($K_7 \approx 0.753$) the eigenframe, $v_\perp$, and channel coefficients all differ.
2. **$P_1=(0,0)$ expansion.** Series in §3 are expanded at the origin; other periodic orbits give different coefficients.
3. **Cubic truncation.** $\mathcal{P}_\mathrm{dyad}$ is the degree-3 approximation; valid for $R \ll 1$ only.
4. **No triad geometry assumed.** The bridge lemma §4 and protection matrix §6 are purely dyadic. No tetrahedral structure, face weights, or Genesis variables have been assumed.

---

## §10. Genesis lift transformation

Once the Genesis side supplies $W = \beta e^{i\chi} w$ (with $\beta = |\gamma|$ the lift scale), the dyadic protection matrix becomes:

$$\mathcal{P}_\mathrm{Genesis}(|w|^2) = \begin{pmatrix}1 - \tfrac{\beta^2}{2}|w|^2 & \tau\beta^2|w|^2 \\ -\tau\beta^2|w|^2 & 1 - \tfrac{\beta^2}{2}|w|^2\end{pmatrix}$$

The chiral-to-healing ratio $4\sqrt{3}/3$ is preserved under this scaling. The absolute healing rate requires knowing $\beta$.

---

*Version 1.1 — RTG dyadic program, 2026-05-05.*
