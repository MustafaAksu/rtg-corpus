# RTG_PRE_LEGACY_DSN_v0.8

**Title:** RTG Pre-Legacy Period — Node-Resonance Theory, Substrate Evolution, and Crystallized Knowledge  
**Date:** June 2026  
**Supersedes:** `RTG_PRE_LEGACY_DSN_v0.7`  
**Companion documents:** `RTG_L0_L1_L2_BRIDGE_LEGACY_DSN_v0.5` · `RTG_ONTOLOGICAL_FOUNDATIONS_v0.3` · `RTG_PROGRAMME_OVERVIEW_v1.1` · `DSN_METHODOLOGY_v1.2`  
**Primary sources:** 68 rtgtheory.org articles (67 pre-Legacy + 1 Legacy); `core_notes_v1.19.md`; `findings_v1_14.yaml` (Jan 14 2026 v12.2 freeze)  
**Document class:** Historical provenance / knowledge-distillation ledger. AI-targeted: dense, explicit, minimally redundant.

**Status summary:** The pre-Legacy period spans four substrate phases (pure node-resonance → cubic lattice → spherical lattice → tetrahedral ESM). It produced nine knowledge categories: resonance kernel; RG fixed point and dimensional ladder; spin gate as binary selector; frustration field and logarithmic force law; minimal-graph dimensional hierarchy; continuum limit (EH emergence and EFT geometry factor); thermodynamics; particle and cosmological predictions; spectroscopic photon validation. All substrate assumptions and early parameter errors are `[FAIL]`. v0.8 audits against current Legacy/Dyadic/OFN programme: demotes overclaimed tags; corrects internal consistency gaps; adds SG-PROG-2 cross-references throughout.

---

## AI Reader Orientation

**Why this document exists.** The RTG pre-Legacy corpus spans 68 articles. This document distills the pre-Legacy period into one structured ledger: what was built, what failed, what survived, and how it connects to current studies. An AI reading only this file has sufficient context to reason about pre-Legacy provenance without fetching original articles.

**What "pre-Legacy" means.** The Legacy period begins when `L0_MASTER_DSN_v2_2.txt` was frozen. Everything before that freeze is pre-Legacy. Chronologically: pure node-resonance → cubic lattice → spherical lattice → tetrahedral ESM → handoff to Legacy L0/L1/L2.

**How to read this document.** §1 gives canonical surviving knowledge (start here). §2 gives active open problems. §3 gives scope guards — boundaries for citing pre-Legacy results. §4 gives the routing map to current DSN targets. §5 is the high-risk ledger. §6 is the full scientific ledger. §7 is the import status. §8 is the article registry.

---

## Quick-Retrieval Table — Key Numbers and Their Locations

| Query | Value | Tag | Section |
|---|---|---|---|
| Critical bandwidth | $\Delta\omega^* = (1.45\pm0.08)\times10^{23}$ rad/s | `[ALG]` | §1.2 |
| RG fixed point | $g^* = 1.14\pm0.02$ | `[ALG]` | §1.2 |
| Energy scale | $E^* = \hbar\Delta\omega^* \approx 95.4$ MeV | `[ALG]` | §1.2 |
| Lattice spacing | $a = \ell_* = 2.07\pm0.11$ fm | `[ALG]` | §1.2 |
| Beat length | $r_* = 2\pi\ell_* = 13.0\pm0.7$ fm | `[ALG]` | §1.2 |
| Proton radius | $r_p = 0.84\pm0.01$ fm | `[NUM strong]` | §1.7 |
| Proton rest energy | 938.27 MeV | `[NUM strong]` | §1.7 |
| CHSH (zero noise) | $S\approx2.827$ | `[NUM strong]` | §1.6 |
| Decoherence onset | $\sigma\approx0.5\Delta\omega^*$ | `[NUM strong]` | §1.6 |
| Decoherence refined | $\sigma_{\rm crit}\approx0.589\Delta\omega^*$ | `[NUM]` | §1.6 |
| EFT geometry factor | $C_\kappa^\infty\approx0.00911$ (window-spread $\leq0.13\%$) | `[NUM strong]` | §1.7 |
| Ward residual | $a_0=(0.10\pm0.97)\times10^{-3}$ ≈ 0 | `[NUM strong]` | §1.7 |
| Effective charge | $e_{\rm eff}\approx16.49$ | `[NUM]` | §1.7 |
| Gravity $1/r$ fit | slope $-1.00\pm0.01$, $R^2>0.9999$ | `[NUM strong]` | §1.5 |
| Gravity elastic const | $K=1.9(2)\times10^{-12}$ J·s, $A=(3.6\pm0.3)\times10^{-3}$ J·m | `[NUM strong]` | §1.5 |
| ESM canonical $\kappa_{\rm grav}$ | $-0.175$ (quadratic law $E_{\rm int}=\kappa\phi^2$) | `[NUM]` | §1.9 |
| Holonomy deficit | $\Delta\approx0.5$ | `[NUM strong]` | §1.8 |
| Topological stiffness | $\kappa_{\rm top}=b_1(K_4)=3$ | `[ALG]` | §1.8 |
| ESM screening error | $7.7\times10^{-12}$ (machine precision) | `[NUM strong]` | §1.9 |
| ESM cooled vacuum | $\eta_{\rm irr}=0.403$ | `[NUM strong]` | §1.9 |
| ESM hot foam floor | $\eta_{\rm irr}=0.75$–$0.80$ | `[NUM strong]` | §1.9 |
| Topological matter | $\beta_1=8$, spectral gap $\lambda_9/\lambda_8\approx10^9$ | `[NUM strong]` | §1.9 |
| κ₃ dark state stiffness | $\Delta_{\rm RMS}=0.52$, flux corr $\approx-0.02$ | `[NUM]` | §1.9 |
| GPS time dilation | $38\,\mu$s day⁻¹ | `[NUM strong]` | §1.15 |
| Lensing surplus | $+0.01''\pm0.002''$ | `[HEUR strong]` | §1.15 |
| BH corridor activation | $E_{\rm th}=66.81\pm3.69$ MeV, $r_{\rm th}=18.56\pm1.02$ fm | `[HEUR]` | §1.15 |

---

## §0. Header

### §0.1 Period definition and chronology

```
Phase 0:  Pure node-resonance (no fixed graph, all-to-all)
          Output: R_ij kernel design, spin gate, beat-distance,
                  void-origin narrative
          [FAIL]: no spatial crystallization without locality

Phase 1:  Cubic lattice L^3
          Output: two-loop RG, CHSH validation, proton K3 model
          [FAIL]: artificial Cartesian symmetry; fixed coord.
          [FAIL]: early Delta_omega* = 2.18e23 s^-1 (superseded)

Phase 2:  Spherical lattice (Fibonacci shell grid)
          Output: frustration field z; natural spherical coords.
          [FAIL]: absolute center; shell discontinuities

Phase 3:  Tetrahedral ESM (K4 grown from 4-node dipole seed)
          Output: ESM quantum foam; kappa_3 curvature;
                  holonomy deficit Delta~0.5; kappa_top=b1(K4)=3
          Status: successful substrate; handed off to Legacy
```

### §0.2 What was being modelled

Nodes $N_i = (\omega_i, \phi_i, s_i)$ are sub-quark constituents, not quarks or electrons. Physical particles emerge as bound states: proton = three-node K₃; photon = zero-$\Delta\omega$ anti-spin pair; quarks = node clusters; vacuum = frustrated node field. **Current programme note:** OFN §1.1 establishes that isolated nodes have no physical state — $N_i=(\omega_i,\phi_i,s_i)$ is a bookkeeping notation for relational differences, not an ontological claim that nodes possess these attributes independently. `[SG-PL-1; SG-PROG-2]`

**Three design principles (pre-Legacy O0 commitments):**
1. **Energy First:** mass is energy; no mass without frequency.
2. **Minimal Assumptions:** no arbitrary constants; derive all from $\Delta\omega^*$, $g^*$. `[scope: within canonical effective model; OPEN-P0 applies]`
3. **Nature-Guided:** emergence from resonance, not imposed geometry.

### §0.3 What was NOT assumed

- No background spacetime. Distance $= 2\pi c/|\Delta\omega|$.
- No external time. Observable interval: $\Delta\tau \approx \Delta\phi/\Delta\omega$ (relational).
- No imposed gauge group. U(1)/SU(2)/SU(3)-analog emerge as kernel windows.
- No gravitational constant. Gravity = residual elasticity of frustration field.
- **No external observer; no privileged reference node.** `[FAIL]` The Observer Relativity article treated one node as "the observer node whose frame defines all measurements." Rejected per PI clarification: all nodes are ontologically equivalent. Any node may serve as computational reference (gauge-like convention, not ontology). The $\Delta\omega^*$-observer is a SI calibration convention only. `[SG-PL-15]`
- **Upstream authority:** Mathematical Foundations defines all symbols and $\Delta\omega^*$. Any inter-article conflict resolves in favor of Mathematical Foundations.
- **Four $\sigma$ identities:** $\sigma_{\rm exch}$ (UV regulator, $\approx\Delta\omega^*$), $\sigma_{\rm noise}$ (CHSH noise), $\sigma$ (RG cutoff), $\Delta\omega^*$ (bandwidth) are mutually independent. Never substitute one for another.

---

## §1. Current Canonical State — What Survived the Pre-Legacy Period

### §1.1 The Resonance Kernel

`[ALG]` `[scope: within canonical effective model; SG-PROG-2 applies]` **Kernel (standard form):**
$$\mathcal{R}_{ij} = \frac{3}{4}[1+\cos(\Delta\phi_{ij})](1+s_is_j)\exp\!\left[-\left(\frac{\Delta\omega_{ij}}{\Delta\omega^*}\right)^2\right]$$

`[HEUR]` **Three construction motivations** for this form: (1) U(1) phase symmetry → cosine term; (2) finite bandwidth from RG fixed point → Gaussian; (3) pair complementarity → spin gate $(1+s_is_j)$. These are motivations, not derivations — the kernel was constructed for consistency with relational commitments, not derived from them. Whether any generator in this form is uniquely selected is OPEN-P0. `[ALG]` Gate is binary: $s_is_j = +1 \Rightarrow (1+s_is_j)=2$ (open); $s_is_j = -1 \Rightarrow 0$ (closed). **The gate is not an SU(2) matrix element.** `[SG-PL-9]`

`[ALG]` **QS kernel (gate-explicit):** $\mathcal{R}_{ij}^{(\rm QS)} = \frac{3}{4}G_{ij}[1+\cos\Delta\phi_{ij}]e^{-(\Delta\omega_{ij}/\Delta\omega^*)^2}$ where $G_{ij}=(1-\sigma_i\sigma_j)/2\in\{0,1\}$. Preferred for superposition analysis.

`[ALG]` `[scope: continuous effective model; SG-PROG-2 applies]` **Bond energy (ungauged default):**
$$E_{ij} = J\mathcal{R}_{ij} + K'\frac{|\Delta\omega_{ij}|}{\Delta\omega^*} + J_{\rm ex}\sin(\Delta\phi_{ij})\exp\!\left[-\frac{\Delta\omega_{ij}^2}{\sigma_{\rm exch}^2}\right]$$

Gauged form (U(1) explicit only): exchange term $\to -J_{\rm ex}\cos(\Delta\phi_{ij}-2\pi aA_{ij})\exp[\ldots]$. **TDR-G import guard:** the $\sin(\Delta\phi)$ exchange term is a smooth continuous-branch construct. It is `[FAIL]` to import it into TDR-G without an explicit bridge theorem (OFN §1.4; SG-PROG-1).

`[ALG]` **Beat-distance metric:** $r_{ij} = 2\pi c/|\omega_i-\omega_j|$. **Speed guard:** use $c$ at nuclear scales; use $c_{\rm eff}\sim10^3$ m/s at molecular scales (water density). Pairwise symmetry: $r_{ij}=r_{ji}$; no privileged reference node.

**Kernel construction guards:**
- $A_{ij}$ (kernel amplitude) ≠ $B_{ij}$ (U(1) gauge phase). Never substitute. `[SG-PL-10]`
- Spin gate: binary 0 or 2, not SU(2) projector. `[SG-PL-9]`
- $\text{sgn}(0)\equiv0$ in force derivative to avoid jitter at $\Delta\omega\to0$.
- $K'$, $J$, $J_{\rm ex}$: calibrated effective parameters, not fundamental constants. `[SG-PL-3]`

### §1.2 The RG Fixed Point and Critical Bandwidth

`[ALG]` **Two-loop β-function:** $\beta(g)\approx0.72g-0.63g^2-0.011g^3$ where $g=\tilde{J}/\tilde{K}$. Fixed point: $g^*=1.14\pm0.02$. The linear $+0.72g$ term is essential — abstract $\beta=-b_1g^2-b_2g^3$ applies only to strictly marginal couplings.

`[ALG]` **Critical bandwidth:** $\Delta\omega^*=(1.45\pm0.08)\times10^{23}$ rad/s (angular). Uncertainty from RG scheme spread, not measurement. Derived consequence of $g^*$, not a free parameter.

`[ALG]` **Four derived scales:**
$$E^*=\hbar\Delta\omega^*\approx95.4\,\text{MeV},\quad \ell_*=c/\Delta\omega^*=2.07\pm0.11\,\text{fm}=a,\quad r_*=2\pi\ell_*=13.0\pm0.7\,\text{fm}$$
Lattice spacing $a=\ell_*=2.07\,\text{fm}$. `[COR]` Earlier table: $a=0.207\,\text{fm}$ — factor-10 error, corrected v0.3.

`[HEUR]` `[scope: conditional on canonical generator being correct; SG-PROG-2]` **Speed of light as derived ratio:** $c_{\rm spec}=a\cdot\Delta\omega^*=c$. Within the canonical model, speed of light is the product of lattice scale and bandwidth — both anchored to $g^*$. No-signalling is structurally enforced in this model: $\mathcal{R}_{ij}$ propagates at $c_{\rm spec}$. **Note:** $a=c/\Delta\omega^*$ is definitional (not derived independently), so this argument is circular unless the generator independently fixes $a$. Until OPEN-P0 closes, treat as a consistency check, not a derivation.

`[FAIL]` **Hypercubic mapping $\rho_s=\frac{3}{2}J$ applied to ESM.** ESM has ~7.36° angular deficit (geometric frustration); analytic hypercubic multipliers invalid. Use Test-Field Calibration for ESM. `[SG-PL-11]`

`[FAIL-corrected]` **Observer node.** Pairwise relational formulas survive with $j$ as computational reference: $r_{ij}=2\pi c/|\omega_i-\omega_j|$; $T_{ij}=\hbar(\langle\omega\rangle-\omega_j)/k_B$. No node is privileged. $\Delta\omega^*$-observer = SI calibration convention only. `[SG-PL-15]`

### §1.3 Dimensional Ladder

`[ALG]` `[scope: within canonical $\mathcal{R}_{ij}$ model; thresholds are properties of this kernel; generator selection OPEN-P0]` **Threshold table** ($x\equiv\delta\omega/\Delta\omega^*$; systematics $\pm0.02$ on all thresholds):

| $x$ range | $D_{\rm eff}$ | Physics | Gauge | Notes |
|---|---|---|---|---|
| $0<x<0.28$ | 2 | Quark-level planar sheets | U(1) | 2D→3D cert.: Cayley–Menger $V_4>0$ |
| $0.28\leq x\leq0.70$ | 3 | Stable 3D shells; proton window | Soft-SU(2) | SU(2) is effective; $\varepsilon_{\rm asym}\ll1$ required |
| $0.70\leq x<1.55$ | 4 | 4D corridors; BH regime | **Not gauged** | Loop density fails; see §1.4 |
| $1.55\leq x\leq1.70$ | 4, U(1)² | SU(3) analog; narrow window | $\theta_1+\theta_2+\theta_3=\rm const$ | Small $\varepsilon$ only; not QCD |
| $x>1.70$ | Unstable | High-D anomaly | Forbidden | Do not simulate |

**Dimensionality = number of stable resonance axes along which coherence can propagate without decohering.** Operational definition: $D_{\rm eff}=\text{rank}(\mathbf{S}_{\mu\nu})$ where $\mathbf{S}_{\mu\nu}=\sum_{\langle ij\rangle}w_{ij}\Delta x_\mu\Delta x_\nu/\sum w_{ij}$, $w_{ij}=\mathcal{R}_{ij}$.

### §1.4 Gauge Structure

`[HEUR]` `[scope: physical interpretation within ESM model; not proved from relational first principles]` **Chronological consistency — origin of gauge fields.** RTG requires $\oint d\tau=0$ (no net time delay around any closed path). When geometric frustration $z_{ij}$ creates a coexact residual on closed paths, the network generates gauge connection field $B$ to screen it. Gauge fields are not imposed — they are the mathematical consequence of chronological consistency on a frustrated network. This is the physical interpretation behind the Screening Theorem in the ESM model. A first-principles derivation from O0–O3 relational commitments does not yet exist.

**Three gauge windows** (authoritative location: §1.3 table):
- U(1) ($x<0.28$): phase coherence; local $\phi_i\to\phi_i+\Lambda_i$ invariance.
- Soft-SU(2) ($0.28\leq x\leq0.70$): spin doublet $(+i,-i)$ mixes; effective SU(2). **Not exact symmetry.** `[SG-PL-12]`
- U(1)² ($1.55\leq x\leq1.70$): triplet coherence $\theta_1+\theta_2+\theta_3=\text{const}$. **Does not reproduce QCD.** `[SG-PL-5,6]`

`[ALG]` **Why the 4D corridor ($0.70\leq x<1.55$) is not gauged.** Three conditions for local U(1) EFT all fail in the corridor: (1) loop abundance — closed loops become rare above the decoherence cliff; (2) phase regularity — distribution fails uniformity; (3) locality — long-range paths dominate. Corridor supports transport and looks 4D in diffusion tests but cannot carry a local gauge field. → OPEN-PL-12.

`[DEF]` **GVT diagnostic tests** (must pass before any corridor-regime gauge claim):
- GVT-1: closed-loop fraction vs $x$ — drops sharply at $x=0.70$
- GVT-2: holonomy variance on minimal loops — diverges above $x=0.70$
- GVT-3: spectral dimension $d_s$ from random walk — $d_s>3$ in corridor
- GVT-4: phase distribution fails uniformity above $x=0.70$

### §1.5 Forces and Fields

`[ALG]` **Four forces as $x$-window regimes of one kernel:**

| Force | Window | Mechanism |
|---|---|---|
| Electromagnetism | $x<0.28$ | Long-range phase coherence; charge = spin imbalance |
| Strong | $0.28\leq x\leq0.70$ | Exchange term confinement; asymptotically free at short $r_{ij}$ |
| Weak | Spin-flip events | `[ONTO pre-legacy]` $s_i:+i\to-i$ costs $\Delta E=2JA_{ij}$; discrete, energy-costing. In current programme, discrete transitions are studied as events/births, not force-like interactions. |
| Gravity | All $x$ | Frustration field $z$; logarithmic; no gate; always attractive |

`[DEF]` **Frustration field $z$ — canonical definition and sign guard:**
$$z_{ij}=\ln\!\left(\frac{r_{ij}^{\rm em}}{s\cdot r_{ij}^{\rm geo}}\right),\quad r_{ij}^{\rm em}=\frac{\kappa}{|\Delta\omega_{ij}|},\quad \kappa=2\pi c$$
$s$ = global scale from bootstrap; $\kappa=2\pi c$ makes $r_{ij}^{\rm em}$ identical to the beat-distance $r_{ij}=2\pi c/|\Delta\omega_{ij}|$ from §1.1 (same object, different notation). **Sign guard:** Emergent Gravity article uses $z=\ln(r_{\rm geo}/r_{\rm em})$ (opposite sign). Both give $E_{\rm vac}\propto z^2$; force law sign depends on convention — always declare which form is used.

`[ALG]` **Exact logarithmic force law:**
$$E_{\rm vac}=\tfrac{1}{2}K_{\rm vac}\sum z^2,\qquad F_{\rm Log}=-K_{\rm vac}\frac{z}{r_{\rm geo}}$$
Scale-invariant; self-limiting ($F\to0$ as $r\to\infty$). Hookean approximation valid only for $|z|<0.1$ and structurally unstable under expansion.

`[HEUR]` **Structural necessity of log forces.** During expansion $r_{\rm em}(t)=r_{\rm em}(0)\times a(t)$. Log forces satisfy bounded restoring and no parametric resonance; Hookean forces violate the second, producing runaway. Log forces are structurally necessary, not merely convenient.

`[HEUR]` **Vacuum viscosity.** Logarithmic frustration produces emergent resistance to expansion: growing $z$ increases the restoring force, damping expansion without dark energy. Single simulation, $N=175$, seed=42.

`[NUM strong]` **HMC residual gravity** (64³ lattice, $\delta\omega\in[0.70,2.0]\Delta\omega^*$, 20k steps):
$$A=(3.6\pm0.3)\times10^{-3}\,\text{J·m},\quad K=1.9(2)\times10^{-12}\,\text{J·s}$$
log-log slope $=-1.00\pm0.01$, $R^2>0.9999$. Perfect $1/r$ residual energy.

`[HEUR]` **Effective G:** $m_0=\hbar\Delta\omega^*/c^2=1.7\times10^{-28}$ kg. Matching $G=Kc/(2m_0^2)$ gives $G_{\rm RTG}\approx G_N$. Match depends on assumed $m_0$.

`[HEUR]` **Cornell confinement potential** (strong-force comparison): $V(r)=\sigma r-\kappa'/r$; $\sigma\approx0.03$ J/m, $\kappa'\approx2.43\times10^{-8}$ J·m. QCD targets: $\sigma\approx0.89$ GeV/fm, $\kappa'\approx0.2$ GeV·fm. Proposed; not simulated.

`[NUM strong]` **Maxwell's equations from coarse-graining.** In long-wavelength limit $a/\lambda\ll1$, node dynamics coarse-grain to $\mathbf{E}$, $\mathbf{B}$ expressed via $\Phi=\langle\phi_i\rangle$, $\mathbf{S}=\langle\vec{s}_i\rangle$; d'Alembert equation $\Box\Phi=0$ with $c=a\Delta\omega^*$ emerging from ratio of lattice scale to bandwidth — not input. Validated in 64³ simulation (energy drift $<10^{-3}$, 1 run).

`[ALG]` **Elastic bond energy reformulation** (decoherent-limit explicit):
$$E_{ij}=K|\omega_i-\omega_j|\,[1-\mathcal{R}_{ij}]+J\mathcal{R}_{ij}+J_{\rm ex}\sin(\Delta\phi_{ij})e^{-(\Delta\omega_{ij}/\sigma)^2}$$
In the decoherent limit ($\delta\omega>0.70\Delta\omega^*$): $\mathcal{R}_{ij}\to0$; elastic remainder $K|\Delta\omega|$ gives $E_{\rm res}(r)=A/r$, i.e., $1/r$ potential → $1/r^2$ force without assuming Newton's law.

### §1.6 Quantum Mechanics

`[NUM strong]` **CHSH.** Anti-aligned spin pair, $\omega_1=0.75\Delta\omega^*$, $\omega_2=0.76\Delta\omega^*$, zero noise: $S\approx2.827\pm0.002$ (near Tsirelson bound $2\sqrt{2}\approx2.828$). Two decoherence thresholds: onset $\sigma\approx0.5\Delta\omega^*$ (CHSH first drops below 2); refined complete decoherence $\sigma_{\rm crit}\approx0.589\Delta\omega^*$. Specify which when citing. CHSH drops to $0.725\pm0.04$ at $\sigma\approx0.345\Delta\omega^*$.

`[HEUR]` **Decoherence = memory fracture.** The bandwidth limit $\Delta\omega^*$ is the system's finite memory capacity. When noise exceeds $0.5\Delta\omega^*$, the gate closes; coherence across that pair is lost. Not wavefunction collapse — bandwidth enforcement of a relational system.

`[NUM]` **Spectroscopic simulation** (sub-0.05% agreement):
| Observable | Simulated | Experimental | Deviation |
|---|---|---|---|
| H-alpha frequency | $4.567\times10^{14}$ Hz | $4.568\times10^{14}$ Hz | 0.02% |
| Lyman-alpha wavelength | 121.502 nm | 121.567 nm | 0.05% |
| 1s→2s transition | 10.204 eV | 10.199 eV | 0.05% |

`[DEF]` **Photon.** Anti-spin pair with $\Delta\omega_{12}=0$ between its two constituent nodes (matched internal frequencies → $m_\gamma=0$ exactly from gate structure). The photon propagation frequency $\omega_\gamma=c|\mathbf{k}|$ is the wavelength/wavevector mode — distinct from the constituent node frequencies. Visible photons: $x=\omega_\gamma/\Delta\omega^*\approx10^{-9}$, deep in U(1) window. Cliff mass at $x=0.70$: $m_\gamma^{\rm cliff}\sim\hbar\Delta\omega^*/c^2\approx95.4$ MeV/c² — irrelevant for visible photons.

`[ONTO pre-legacy philosophical]` **Ghost Manifold / memory depth $M$.** The Geometry of Forgetting (Dec 2025) interprets wave-particle duality as memory-dependent stability. Pre-measurement state = "Ghost Manifold" supported by memory depth $M$; detector truncates $M$, fracturing the high-rank geometry; Born rule $|\psi|^2$ = "local thickness of projected geometry." **Scope:** explicitly philosophical — the document itself says "intentionally philosophical; predictions means proposals." Do not cite as a derivation. → OPEN-PL-5. `[SG-PL-8]`

### §1.7 Particles and Bound States

`[NUM strong]` **Proton** (K₃ three-node bound state, SU(2) window):

| Parameter | Value |
|---|---|
| $\omega_{\rm proton}$ | $3.058\times10^{23}$ rad/s |
| $K'$ (proton context) | $12.0$ MeV |
| $J$ (proton context) | $2.3$ MeV — **see dual-J guard below** |
| $J_{\rm ex}$ (proton context) | $0.5$ MeV — **see dual-J guard below** |
| $\sigma_{\rm exch}$ | $\Delta\omega^*$ |
| Radius | $0.84\pm0.01$ fm |
| Rest energy | 938.3 MeV |
| Binding energy | $48\pm3$ MeV (three-node) |
| Quark frequency | $\omega_q\approx2.51\times10^{23}$ rad/s |
| Buffer nodes | $\sim40$ |
| Trion geometry | $\Delta\phi=2\pi/3$ |

**Dual-J notation guard.** $J=2.3$ MeV above is the proton calibration (Particle & Nuclear v2.4 §4.1). $J=3.24\pm0.12$ MeV is the ESM/EFT context (core_notes v1.19 §1.2). $J_{\rm ex}=0.5$ MeV (proton) vs $2.20\pm0.08$ MeV (EFT). These are NOT interchangeable — always specify calibration context.

`[NUM]` **Proton triangle geometry (v0.7, Sep 2025).** Two short edges $\approx1.756$ fm, one long edge $\approx2.03$ fm (non-equilateral). $r_{\rm metric}\approx1.068$–$1.070$ fm. Binding plateau $E_{\rm bind}\approx-3J_{\rm bind}$. Hessian stable. `[scope: grid scan, not ensemble]`

`[NUM]` **Neutron companion (v0.7 draft).** Same SU(2) window; topological charge $\approx0$; size $\sim1$ fm. No ensemble validation.

`[HEUR]` **RTG Hydrogen (v0.1 draft).** Proton triad (fixed) + electron node in U(1) window ($x_e<0.28$). Stable plateaus $E\approx-2.7\ldots-3.3$; beat-distance radii $10^4$–$10^5$ fm (Bohr scale). Straddles two gauge sectors (U(1) electron + SU(2) proton). No Hessian, no ensemble.

`[HYP]` **K₃ as minimal closed relational loop.** Pre-Legacy reasoning: K₃ is the minimum closed resonance loop — a dyad has two free ends (not closed); gate-topology requires at least three anti-aligned nodes for closure. **Current programme status (OFN v0.3 §2.2):** this is OPEN-OFN-3A — a testable hypothesis, not a settled result. Dyad-first ordering (OPEN-OFN-3B: does $T_3(s,c)|_{c=0}=T(s)$?) is equally open. Do not export as derivation. `[SG-PL-6]`

`[NUM strong]` **EFT geometry factor** $C_\kappa^\infty$ (L=32/64/96 infinite-volume limit, `amp=none`):
| Window | $C_\kappa^\infty$ | Uncertainty |
|---|---|---|
| SU(2) (0.28–0.70) | 0.0091044741 | $\pm5.5\times10^{-7}$ |
| U(1) (0–0.28) | 0.0091160847 | $\pm1.1\times10^{-7}$ |
| U(1)² (1.55–1.70) | 0.0091147145 | $\pm4.9\times10^{-9}$ |
Window spread $\leq0.13\%$ — $C_\kappa$ is universal (not gauge-sector-specific). `[NUM strong]` Ward residual: $a_0=(0.10\pm0.97)\times10^{-3}\approx0$. $\kappa_B\approx3.675\times10^{-3}$ MeV; $e_{\rm eff}=\kappa_B^{-1/2}\approx16.49$.

`[DEF]` **Multilayer hierarchy** `[scope: bookkeeping description; SG-PL-1 applies]`. Level 0: relational difference carriers $N_i=(\omega_i,\phi_i,s_i)$ — bookkeeping notation, not ontological primitives (OFN §1.1). Level 1: quark clusters (U(1) window). Level 2: hadrons (K₃, SU(2) window). Level 3: nuclei (multi-K₃ graphs). Sub-nodes are clusters; hierarchy defined by RG block-spin flow.

`[NUM]` **Ca-40.** Binding $\approx8.5$ MeV/nucleon (exp: 8.55), rms radius $\approx3.47$ fm (exp: 3.48 fm). `[NEED CHECK → see §5]`

### §1.8 κ₃ Curvature and Topological Stiffness

`[NUM strong]` **Holonomy deficit.** K₄ with SU(2) connections, frustrated face flux $F_f=2\pi/3$: holonomy trivializes (${\rm tr}_f\approx1.0$), giving $\Delta={\rm tr}_f-\cos(F_f/2)=1.0-0.5=0.5$. Pinned under geometric tilts, axis permutations, and least-squares refinements.

`[ALG]` **Wilson loop + general gap formula:**
$$H_f=\prod_{e\in\partial f}e^{iA_e},\quad{\rm gap}_f=\left|{\rm tr}_f-\cos\!\left(\frac{F_f}{2}\right)\right|,\quad{\rm tr}_f=\frac{{\rm Re}({\rm Tr}(H_f))}{2}$$
The $\Delta\approx0.5$ result is the specific case $F_f=2\pi/3$, $\cos(\pi/3)=0.5$.

`[ALG]` **Topological stiffness:** $\kappa_{\rm top}=b_1(K_4)=|E|-|V|+1=6-4+1=3$. Topologically determined, not a free parameter.

`[HEUR]` **Dark state — BCH mechanism.** The linear solver screens Abelian target flux but commutators $[A_e,A_{e'}]$ (Baker–Campbell–Hausdorff quadratic terms) produce residual SU(2) rotation that cannot be eliminated. This "dark state" has linear constraints met but non-Abelian curvature screened. $\Delta\approx0.5$ is the visible signature. **Energy barrier:** the dark state is separated from the curvature-realized configuration by an energy barrier — the "cost of geometry."

`[ALG]` **SU(2) lift — Pauli matrix construction** (Legacy formalization of pre-Legacy holonomy operations; the binary spin gate of §1.1 is superseded by this continuous SU(2) algebra at the Legacy level — they are different objects at different levels `[SG-PL-9]`):
$$\hat{J}_i=\cos(\theta_i)\sigma_1+\sin(\theta_i)\sigma_2,\quad U_{ij}^{\rm base}=\exp\!\left(-i\tfrac{(\theta_j-\theta_i)-\alpha_{ij}}{2}\sigma_3\right)$$
Minimize: $L(A)=\sum_f\|\log(H_{t,f}^\dagger H_f(A))\|_F^2+\lambda\sum_e\|A_e\|^2$. **Energy normalization:** $E_{\rm full}=4E_{\rm half}$ (factor-4 between half/full-angle conventions).

`[NUM]` **κ₃ Stratified Active Matter (R2 ensemble, $N=10$ seeds):**
1. **Stratification:** stress on bottleneck hinges (faces with $n_{\rm active}=2$, k-core $\geq2$)
2. **Plasticity:** quartic constitutive law $E_{\rm def}\propto Q_{\rm opp}\theta^4$, $Q_{\rm opp}<0$ (Type-I yielding) — universally plastic, not rigid
3. **Protection:** Betti-1 $z$-score $\sim8$–$11$ above null; structural redundancy traps non-Abelian frustration

`[HEUR]` **ESM geometric frustration — 7.36° angular deficit.** Tetrahedral dihedral $\approx70.53°$ vs ideal $72°$; deficit creates the κ₃ obstruction, holonomy deficit $\Delta\approx0.5$, and 75.2% irreducible curvature floor.

### §1.9 Emergent Spacetime and ESM

`[HEUR]` **Four Pillars — unified ESM sequence** (core_notes v1.19 §10):
1. **Frustration (origin):** $z_{ij}=\ln(r_{\rm em}/s\cdot r_{\rm geo})$ mismatch between frequency-derived and embedding distances.
2. **Gauge field (response):** Vacuum generates $B$ to screen $z_{\rm co}$, enforcing $\oint d\tau=0$.
3. **Matter (residue):** Topology ($\beta_1$) prevents perfect screening. Unscreenable $z_h$ modes are matter.
4. **Gravity (interaction):** Matter defects attract to minimize harmonic stress $E_h$. Structure formation is entropic. **Central conclusion:** gravity is the entropic consequence of a cooling, frustrated vacuum organizing its topology. `[SCOPE]` Individual components validated (Tiers 1–2); full chain is programme-level `[HEUR]`. **Step 4 additional blocker:** the smooth metric lift (Genesis Geometry OPEN M) and the Regge bridge (OPEN-P3/OPEN 0) are required before this conclusion can be made rigorous; the current proto-gravity result ($\kappa=-0.175$) is a quadratic coupling in a toy model.

`[DEF]` **Hodge three-way decomposition (canonical ESM framework):**
$$z=z_{\rm ex}+z_{\rm co}+z_{\rm h}$$
| Component | Name | Physical role | Screened? |
|---|---|---|---|
| $z_{\rm ex}$ | Exact | Gauge-trivial; pure curl | Completely by $B$ |
| $z_{\rm co}$ | Coexact | Foam — irreducible curvature | By $B$ via $D_1B=D_1z_{\rm co}$ |
| $z_{\rm h}$ | Harmonic | Topological matter ($\beta_1$ modes) | Cannot be screened |

$\eta_{\rm irr}=(\text{Coexact+Harmonic variance})/\text{Total variance}$. $\beta_1$ invariant under gauge transformations.

`[NUM strong]` **Screening Theorem** (two equivalent forms):
- Compact: $D_1B=D_1z_{\rm co}$
- Additive: $z_{\rm total}-z_{\rm exact}-B=z_{\rm harmonic}$

Structure error: $7.7\times10^{-12}$ (machine precision). Gauge field is the mathematical inverse of screenable vacuum energy.

`[DEF]` **ESM growth — four phases:** Phase I: Hodge/geometric floor. Phase II: 4-node dipole seed. Phase III: flux-balanced growth minimizing signed boundary charge $Q=\sum_{e\in\partial\mathcal{K}}z_{ij}$; "breathing" avoids stalls. Phase IV: refinement via DRR ($\sum|z_{ij}|$ on boundary). $Q$ (signed, drives growth) and DRR (unsigned, drives refinement) are independent observables.

`[NUM strong]` **Cooled vacuum vs hot foam:**
| System | $\eta_{\rm irr}$ | $\beta_1$ | Spectral gap $\lambda_9/\lambda_8$ | State |
|---|---|---|---|---|
| FCC ($N=14$–$1400$) | 0.75–0.80 | varies (no gap) | $\sim1$ | Hot Foam |
| Grown ($N=175$) | **0.403** | **8** | **$\sim10^9$** | Cooled Vacuum |

46% reduction in irreducible curvature. The spectral gap $\sim10^9$ distinguishes genuine topological matter from FCC artifacts (no gap).

`[NUM]` **Proto-gravity — canonical coupling.** Topological defects attract to minimize harmonic stress. Gravity probe v5.1:
$$E_{\rm int,h}=\kappa_{\rm grav}\phi^2,\quad\kappa_{\rm grav}=-0.175\;\text{(canonical)}$$
**Normalization guard:** Earlier reports gave "−83% interaction energy" — that was a different baseline normalization, superseded by $\kappa=-0.175$. Vacuum and κ₃ channels remain at $\sim10^{-14}$–$10^{-15}$ across the sweep. Single cluster, parameter-sensitive.

`[HEUR]` **κ₃ as dark energy candidate.** Vacuum is Abelian-flat ($B$ screens $F$) but non-Abelian-stiff ($\Delta_{\rm RMS}=0.52$, flux correlation $\approx-0.02$). Residual non-Abelian curvature = geometric candidate for dark energy (distinct from $\Lambda_{\rm eff}$ from the irreducible curvature floor — two different mechanisms).

`[HEUR]` **Machian feature.** Coherent geometry nucleates around relational defects, not empty space. Random initialization without seed fails to produce coherent structure ("void fails" — informal; systematic tests deferred).

`[NUM]` **ESM cosmology drift phase diagram** (mass2 coupling $q=z_h^2$):
| $G$ | Phase | Notes |
|---|---|---|
| 5 | FREE (${\rm conc}\approx3.8\%$) | No clustering |
| ≈20 | BALANCED/MARGINAL | Threshold region |
| ≥50 | BOUND++ (${\rm conc}\approx21\%$) | Clustering confirmed |

Signed coupling ($q=z_h$) produces blow-up — documented failure mode.

`[SCOPE]` **ESM cosmology simulation hygiene.** Three required bug fixes: (1) self-force removal (diagonal distances $\to\infty$); (2) COM recentering each step; (3) Hodge recomputation each step with spatial concentration metric (not percentile).

`[DEF]` **ESM publication readiness** (v12.2 freeze, Jan 2026): ✓ Tier 1 ready: gauge screening, κ₃ dark state, topological matter. ⚠ Tier 2 needs work: proto-gravity (quadratic coupling), cosmology drift. ❌ Tier 3 not ready: Lorentz symmetry, particle masses.

### §1.10 Origin Narrative

`[ONTO pre-legacy]` **Void = absolute neutrality.** Initial state: net energy, phase, spin = 0. Spontaneous symmetry breaking into $(+i,-i)$ node pairs conserving global spin = 0. Not matter-antimatter annihilation — complementary populations coexist. **Current programme reframing (OFN §1.3):** the zero-origin condition ($O_0=0$) is adopted, but the "node pair creation" framing is pre-Legacy. The current programme understands the first physical event as a dyadic distinction — a relational asymmetry between two poles — not a node-creation event. Dyad-vs-triad primacy (OPEN-OFN-3) means the correct picture of the "first event" is open.

`[ONTO pre-legacy]` **Zero-sum initialization.** $\omega_i^+=+0.5\Delta\omega^*+\epsilon_i$, $\omega_j^-=-0.5\Delta\omega^*-\epsilon_j$, $\epsilon\sim\mathcal{N}(0,0.1\Delta\omega^*)$, phases $\mathcal{N}(\pi,0.1)$; ensures $E^{\rm raw}_{\rm initial}=0$.

`[ONTO pre-legacy]` **Geometry from frustration.** Nodes are distributed in frequency-phase-spin space (not physical space). Physical space crystallizes from local frequency frustration patterns. Geometry is what happens between matter seeds.

`[HEUR]` **Kuramoto-type dynamics.** $\dot\phi_i=\omega_i-\eta\sum_j\mathcal{R}_{ij}\sin(\phi_i-\phi_j)$; $\dot\omega_i=-\gamma\sum_j(\omega_i-\omega_j)\mathcal{R}_{ij}$. Resonance energy $E_{ij}\sim-J\mathcal{R}_{ij}$ minimized at maximum coherence — Kuramoto synchronization analog.

### §1.11 Stability and Simulation Hygiene

`[DEF]` **Equilibrium:** $\partial E/\partial q=0$; energy-minimization simulations (MC, MD) seek stationary points of $H_{\rm tot}=\sum_{\langle ij\rangle}E_{ij}$.

`[DEF]` **Phase-locking attractor.** $\mathcal{R}_{ij}$ maximized at $\Delta\phi=0$; phase locking is the dynamical attractor.

`[DEF]` **Hypercubic lattice-to-continuum** (hypercubic only; `[FAIL]` for ESM): $K'_{\rm TV}=K_{\rm lat}a^{1-d}$; $\rho_s=\frac{3}{2}Ja^{2-d}$.

`[SCOPE]` **Clipping caveat.** Clamping $\mathcal{R}_{ij}$ to $[0,3]$ can manufacture spurious bounded periodic behavior. Must: (1) report clamping explicitly; (2) check unclamped dynamics; (3) never treat bounded post-clamp behavior as evidence of stability without this check.

`[SCOPE]` **ESM cosmology hygiene.** Three required fixes: (1) self-force removal; (2) COM recentering; (3) Hodge recomputation each step. (Also in §1.9 for proximity to ESM content.)

### §1.12 Continuum Limit and Gravitational Emergence

`[ALG]` **Six-step metric pipeline** (Gravity I §3): (1) structure tensor $S_{\mu\nu}$ from $w_{ij}=\mathcal{R}_{ij}$; (2) diagonalize; (3) tetrads from eigenvectors; (4) timelike axis from phase flow; (5) conformal factor $\Omega$ from Laplace-Beltrami; (6) $g_{\mu\nu}=\Omega^2\eta_{ab}e^a{}_\mu e^b{}_\nu$.

`[ALG]` `[scope: tree-level; loop corrections not established; OPEN-P3 Regge bridge required]` **Tree-level EH action:** $S_{\rm EH}=\int d^4x\sqrt{-g}[\frac{M_{\rm Pl}^2}{2}R-\Lambda_{\rm eff}]+S_{\rm matter}+S_{\rm U(1)}$. $\Lambda_{\rm eff}$ from irreducible curvature floor. **Consistency note:** the Phase 0 seed ($N=14$) gives $\eta_{\rm irr}=75.2\%$; the mature cooled vacuum ($N=175$, §1.9) gives $\eta_{\rm irr}=40.3\%$. For a mature ESM, use $\Lambda_{\rm eff}\propto\eta_{\rm cool}=0.403$; the 75.2% figure belongs to the small-seed geometric floor. Loop corrections: $G(\mu_\ell)\approx G_0[1+c_G\mu_\ell^2/\mu_0^2]$; $\Lambda$ decreases with energy.

`[HEUR]` **RTG→GR 14-phase pipeline** (v2.2, Nov 2025 — Pre-Axiom):

| Phase | Content | Status |
|---|---|---|
| I | Resonant nodes; no spacetime | `[ALG]` solid |
| II | K₄ double-NS bifurcation → 4D torus | `[HEUR]` open (Roadmap 1A/1B) |
| III | Non-Abelian lift → SU(2)/quaternions | `[HEUR]` open |
| IV–VI | Structure tensor, tetrads, metric | `[HEUR]` sketch |
| VII | Torsion: micro nonzero, macro zero | `[HEUR]` |
| VIII | Holonomy/curvature (Wilson loops) | `[ALG]` (κ₃) |
| IX–X | Continuum manifold; EH dominant | `[HEUR]`/`[ALG]` tree-level |
| XI–XII | Quantum RTG; RTG Radion | Sketch/speculative |
| XIII | GR assumes vs RTG derives | See below |

**GR vs RTG (Phase XIII):**
| GR assumes | RTG derives |
|---|---|
| Background spacetime | Emergent from resonance |
| Lorentzian signature | NS stability — **Conjecture 1 unproved** → OPEN-PL-13 |
| 3+1 dimensions | 2D torus stabilization — **Conjecture 2 unproved** → OPEN-PL-13 |
| Spin-2 graviton | SU(2) holonomy structure `[HYP — requires OPEN M closure; block-diagonal no-go THM means non-trivial UV completion needed]` |
| Gauge freedom | Relational invariance |

**K₄ NS mechanism** `[HEUR open]`: K₄ double-NS (codimension-2) produces two complex mode pairs ($|\lambda_1|=|\lambda_2|=1$), 4D invariant torus. This is the proposed reason why K₄ → 4D, not K₃ (single-NS, 2D torus). **Current programme status:** the saddle-node mechanism has been downgraded from `[THM]` to `[HYP]` in Genesis Geometry DSN §6.9 (resonance-assisted saddle-node pending exact resolvent derivation). The NS mechanism itself (Phase 1A/1B) remains fully open in the Post-v2 Roadmap.

**Torsion:** micro nonzero (non-Abelian connections); macro vanishes (energy minimization provides restoring force). RTG has torsion-free continuum limit.

**RTG Radion:** bandwidth modulation $\delta(\Delta\omega^*)$ → scalar field analogous to Kaluza-Klein radion; lightest scalar mode.

### §1.13 Lattice-to-Continuum Parameter Map (hypercubic only)

| Lattice | Continuum | Value (hypercubic, $d=3$) |
|---|---|---|
| $K_{\rm lat}$ | $K'_{\rm TV}$ | $K_{\rm lat}a^{1-d}$ |
| $J_{\rm lat}$ | $\rho_s$ | $\frac{3}{2}J_{\rm lat}a^{2-d}$ |
| $\Delta\omega^*$ | $E^*$, $\ell_*$, $r_*$ | 95.4 MeV; 2.07 fm; 13.0 fm |
| $g^*=1.14$ | all ratios | scheme uncertainty $\pm0.08$ |

### §1.14 Thermodynamic Layer

`[DEF]` **Two temperature concepts — must not be conflated:**
| Concept | Formula | Properties |
|---|---|---|
| Relational $T_{\rm RTG}$ | $\hbar(\langle\omega\rangle-\omega_j)/k_B$ | Frame-dependent; can be negative |
| Spectral $T_{\rm spec}$ | $\hbar\sigma_\omega/k_B\geq0$ | Frame-invariant; thermodynamic |

Temperature-bandwidth calibration (SI): $T_{\rm SI}[\text{K}]=\hbar\delta\omega_{\rm RTG}/k_B$. At 4°C: $\delta\omega\approx3.62\times10^{13}$ rad/s $\ll\Delta\omega^*$.

`[ALG]` **Internal energy:** $U=\sum_i\hbar\omega_i+\frac{1}{2}\sum_{i\neq j}[K'|\Delta\omega|/\Delta\omega^*+J\mathcal{R}_{ij}+J_{\rm ex}\sin(\Delta\phi)e^{-\ldots}]$. Factor $\frac{1}{2}$: double-count of undirected bonds.

`[ALG]` **Heat flow:** $\dot{q}=\hbar(\langle\omega\rangle_1-\langle\omega\rangle_2)\mathcal{R}_{12}$. Closed gate stops heat flow.

`[DEF]` **Mass estimator convention guard.** Two conventions: (A) Thermodynamics: $E^{\rm bind}=J\mathcal{R}_{ij}$, $\frac{1}{2}$ factor. (B) Canonical Handbook M1: $E^{\rm res}_{ij}=\hbar|\Delta\omega_{ij}|\mathcal{R}_{ij}$, no $\frac{1}{2}$. State which convention in every computation.

### §1.15 Relativistic Effects, Experimental Validation, and Cosmology

`[DEF]` **Validated predictions:**
| Observable | RTG value | Tag | Note |
|---|---|---|---|
| GPS time dilation | $38\,\mu$s day⁻¹ | `[NUM strong]` ✓ | $\Delta\tau=\Delta\phi/\Delta\omega$ from phase equipartition |
| Proton radius | $0.84\pm0.01$ fm | `[NUM strong]` ✓ | — |
| CHSH (zero noise) | $\approx2.827$ | `[NUM strong]` ✓ | Near Tsirelson bound |
| H-alpha | 0.02% deviation | `[NUM]` ✓ | — |
| Lyman-alpha | 0.05% deviation | `[NUM]` ✓ | — |
| 1s→2s | 0.05% deviation | `[NUM]` ✓ | — |
| Gravity $1/r$ | slope $-1.00\pm0.01$, $R^2>0.9999$ | `[NUM strong]` ✓ | HMC 64³ |
| Ward residual | $\approx0$ | `[NUM strong]` ✓ | EFT v1.4.2 |
| Ca-40 binding | $\approx8.5$ MeV/A | `[NUM]` ✓ | `[NEED CHECK → §5]` for radius |
| CMB $\Delta T/T$ | $\sigma_\phi\approx10^{-5}$ | `[HEUR]` match | — |
| Lensing surplus | $+0.01''\pm0.002''$ | `[HEUR strong]` testable | Gaia DR4 resolution $0.008''$ |
| Hawking temperature | within 2× of GR | `[HEUR]` structural | — |

`[HEUR]` **Relational light cones.** Past/future partition determined by resonance reachability, not fixed background. Corridor threshold $x\approx0.70$ sets effective causal boundary for high-energy modes.

`[HEUR]` **Equivalence principle.** Inertial mass (resistance to $\Delta\omega$ changes) = gravitational mass (curvature from rerouting) because both arise from $\mathcal{R}_{ij}$. Structural equality, not postulate.

`[HEUR]` **Black hole corridor activation:**
$$E_{\rm th}=\hbar(0.70\Delta\omega^*)=66.81\pm3.69\,\text{MeV},\quad r_{\rm th}=18.56\pm1.02\,\text{fm}$$
Empirical knee $x\approx0.69\pm0.06$ from Isomap diagnostics. Singularity resolution via bandwidth ceiling: collapse freezes at corridor scale. Information preservation conjectured.

`[HEUR]` **Cosmic expansion.** $\dot\omega_i=-K\sum_j(\omega_i-\omega_j)\mathcal{R}_{ij}$; $\dot\phi_i=\omega_i-\eta\sum_j\mathcal{R}_{ij}\sin(\phi_i-\phi_j)$. $\epsilon=K\alpha\langle\mathcal{R}\rangle$; $\alpha\approx2/3$ (radiation), $\approx1/3$ (matter). No dark energy: $\Lambda_{\rm eff}$ from irreducible curvature floor. `[SCOPE]` $N=175$, single seed.

`[HEUR]` **RTG information principle.** Information stored in history of stable resonance patterns. Universe "remembers" through pattern stability.

`[HEUR]` **Higgs-like.** Tetrahedral cluster ($\Delta\phi=2\pi/3$), $\delta\omega_H\approx0.8\Delta\omega^*$, $c_{\rm eff}=0.3c$ (chosen to match 125 GeV — not derived). Early-era speculative content.

---

## §2. Active Frontier — Open Problems

**OPEN-PL-1 — Generator derivation (= current OPEN-P0).** Why does $\mathcal{R}_{ij}$ have its specific form? Constructed by symmetry + RG calibration; no derivation from relational first principles. → RTG_PROGRAMME_OVERVIEW OPEN-P0.

**OPEN-PL-2 — $\Delta\omega^*$ scheme independence.** Derived from two-loop RG under a specific scheme. Whether scheme-independent (truly universal) is unresolved. Uncertainty $\pm0.08$ captures scheme spread.

**OPEN-PL-3 — K₄ natural selection.** Arrived at K₄ by elimination; no positive derivation that K₄ is the unique minimal graph satisfying background-independence + closed 3D structure + non-trivial holonomy. → OFN OPEN-OFN-3C (minimal network size for geometric emergence); Genesis DSN OPEN-GEN-TETH-SELECT.

**OPEN-PL-4 — Continuum limit of logarithmic force law.** Validated at $N=175$, nuclear scale, single seed. Connection to EH action at tree level is partial; full quantum corrections and scheme independence not established. → OPEN-P3 (Regge bridge).

**OPEN-PL-5 — Physical meaning of decoherence threshold.** CHSH drops below 2 at $\sigma\approx0.5\Delta\omega^*$ — clean result. Connection to Born rule and measurement theory is `[HEUR]` only. Ghost Manifold interpretation is explicitly philosophical.

**OPEN-PL-6 — SU(3) analog robustness.** U(1)² triplet coherence at $x\in[1.55,1.70]$ does not reproduce QCD. Window is narrow and numerically fragile above $x=1.70$.

**OPEN-PL-7 — Coupling proxy exponent $\alpha$.** $C_{12}(\alpha)=r^{-\alpha}\mathcal{R}$; no first-principles derivation selects $\alpha=1$ or $\alpha=2$.

**OPEN-PL-8 — Regge/LQG connection (= OPEN-P3).** Tree-level EH is derived; discrete-to-continuum limit at path integral level not established.

**OPEN-PL-9 — Full SU(2) gauge extension.** Kernel has U(1) gauge invariance; whether it extends to full SU(2) without modifying kernel structure is unresolved.

**OPEN-PL-10 — RTG UV cutoff vs Planck scale.** $\ell_*\approx2.07$ fm is 19 orders above $\ell_{\rm Pl}$. Planck-scale physics not accessible to pre-Legacy node model.

**OPEN-PL-11 — CHSH multi-node and asymmetric noise.** Study limited to $N=2$, symmetric noise. Extensions not computed.

**OPEN-PL-12 — How to gauge the 4D corridors.** Three conditions for gauge emergence all fail in $x\in[0.70,1.55]$. Whether they can be restored is open. GVT-1–4 are the measurement targets.

**OPEN-PL-13 — Lorentzian signature and 3+1D from NS bifurcation.** Two unproved conjectures in RTG→GR Phase V. Resolving both completes the Pre-Axiom pipeline. → Post-v2 Roadmap Phase 1A/1B (highest priority).

---

## §3. Scope Guards

**[SG-PL-1]** Node $(\omega,\phi,s)$ is not the correct ontological primitive — it is a bookkeeping carrier for relational differences. Pre-Legacy results from node-internal structure must be re-examined under relational primacy before export. `[SG-PROG-2 applies: no coefficient derived from node structure may be called physically primitive until OPEN-P0 closes]`

**[SG-PL-2]** Cubic and spherical lattice results are substrate-contaminated. Only explicitly substrate-independent results (pairwise kernel, RG fixed point, CHSH, proton K₃) may be exported without revalidation.

**[SG-PL-3]** $K'$, $J$, $J_{\rm ex}$ are calibrated effective parameters, not fundamental constants. Pending derivation from generator (OPEN-P0).

**[SG-PL-4]** Logarithmic gravity is $N=175$, single seed, nuclear scale. Not evidence for cosmological stability or derivation of Newton's law.

**[SG-PL-5]** Gauge windows are kernel properties, not derivations of Standard Model groups. U(1)/SU(2)/U(1)² identification with forces is physical interpretation, not theorem.

**[SG-PL-6]** Proton, CHSH, photon results are K₂/K₃ calculations — not lattice validations. Do not cite as evidence for any substrate's correctness.

**[SG-PL-7]** Void origin narrative and pair-creation are `[ONTO pre-legacy]` design hypotheses. No simulation support, no algebraic proof.

**[SG-PL-8]** Ghost Manifold / Born rule as projected thickness: philosophical interpretation, not derivation of quantum probability.

**[SG-PL-9]** Spin gate $(1+s_is_j)$ is binary (values 0 or 2) — NOT an SU(2) matrix element, projector, or representation. Critical type-error if confused with Genesis/Triadic DSN SU(2).

**[SG-PL-10]** $A_{ij}$ (kernel amplitude) ≠ $B_{ij}$ (U(1) gauge phase). Never substitute. Link: $U_{ij}=e^{i(\phi_i-\phi_j-B_{ij})}$.

**[SG-PL-11]** Hypercubic lattice mappings ($\rho_s=\frac{3}{2}J$, $K'_{\rm TV}=K_{\rm lat}a^{1-d}$) do not apply to ESM. Use Test-Field Calibration for ESM.

**[SG-PL-12]** Soft-spin SU(2) is an effective approximation for $x\in[0.28,0.70]$ and $\varepsilon_{\rm asym}\ll1$. Not Standard Model SU(2)$_L$; not an exact symmetry.

**[SG-PL-13]** RTG UV cutoff $\ell_*\approx2.07$ fm is NOT near the Planck scale. Pre-Legacy nodes cannot address Planck-scale physics.

**[SG-PL-14]** All RTG cosmological claims rest on $N=175$, single seed, nuclear-scale simulation. Dark matter and dark energy replacement are design hypotheses.

**[SG-PL-15]** No external observer; no privileged reference node. Observer Relativity article framing is `[FAIL]`. All pairwise formulas use $j$ as computational reference only. $\Delta\omega^*$-observer = SI calibration convention.

---

## §4. Layer Routing — Where Pre-Legacy Items Connect to Current Studies

| Pre-Legacy item | Tag | Primary route | Secondary route |
|---|---|---|---|
| Resonance kernel $\mathcal{R}_{ij}$ | `[ALG]` `[scope: canonical effective model]` | OFN OPEN-OFN-1; OPEN-P0 derivation | Dyadic DSN — OPEN-P0 asks whether $T(\rho,\eta)$ and $\mathcal{R}_{ij}$ share a common foundation; they are NOT the same object |
| Gauge invariance of $\mathcal{R}_{ij}$ | `[ALG]` | OFN §1.1 relational primacy | Dyadic — relational-difference structure |
| $\Delta\omega^*=(1.45\pm0.08)\times10^{23}$ | `[ALG]` | All current DSN documents | SI Calibration anchor |
| $g^*=1.14\pm0.02$ | `[ALG]` | All current DSN documents | — |
| Proton $r_p=0.84$ fm | `[NUM strong]` | Genesis DSN §6.6 calibration | L0 master calibration |
| CHSH $S\approx2.827$ | `[NUM strong]` | Arithmetic Resonance DSN Thread B | TDR-G memory depth study |
| Frustration field $z=\ln(r_{\rm em}/r_{\rm geo})$ | `[ALG]` | TDR-G defect band; Genesis holonomy | Legacy L0L1 §3.2 Lyapunov plateau |
| Log force stability | `[NUM]` | OFN OPEN-OFN-6 (Q-healing prototype) | Legacy DSN Appendix B |
| Hookean gravity `[FAIL]` | `[FAIL]` | TDR-G scope guard (avoid linear laws) | Legacy DSN Appendix B |
| Holonomy deficit $\Delta\approx0.5$ | `[NUM strong]` | Genesis DSN §6.4 κ₃ entry | L2 DSN OPEN-L2-NONABELIAN |
| $\kappa_{\rm top}=b_1(K_4)=3$ | `[ALG]` | Genesis DSN §6.4 | L2 DSN OPEN-L2-NONABELIAN |
| ESM quantum foam 75.2% | `[NUM strong]` | Genesis DSN §6.7 block-diagonal no-go | Legacy L0L1 vacuum floor |
| Observer `[FAIL]` | `[FAIL]` | OFN §1.1 relational primacy (confirmed) | All DSN documents |
| κ₃ Stratified Active Matter | `[NUM]` | Legacy L2 DSN κ₃ programme | — |
| Screening Theorem $10^{-12}$ | `[NUM strong]` | ESM validation suite | Working Document v12.2 |
| $\beta_1=8$, gap $10^9$ | `[NUM strong]` | ESM matter identification | Working Document v12.2 |
| 4D corridors non-gauged | `[ALG]` | EFT §2; future gauge programme (OPEN-PL-12) | — |
| NS bifurcation → 4D torus | `[HEUR]` | Post-v2 Roadmap Phase 1A/1B | Genesis DSN NS programme |
| Dual-J values | `[SCOPE]` | Any study importing $J$ from corpus | Calibration convention |

---

## §5. High-Risk Claims Ledger

| Claim | What it actually is | What it is NOT | Guard |
|---|---|---|---|
| Proton radius agreement | K₂/K₃ calculation `[NUM strong]` | Validation of any lattice substrate | SG-PL-6 |
| CHSH value | $N=2$, K₂, symmetric noise | Multi-node or asymmetric test | SG-PL-6 |
| Log gravity stability | $N=175$, single seed, nuclear scale | Cosmological derivation of Newton's law | SG-PL-4 |
| $\kappa_{\rm grav}=-0.175$ | Canonical quadratic fit `[NUM]`; not −83% | Earlier −83% was different baseline normalization | §1.9 guard |
| **Ca-40 rms radius** | **`[NEED CHECK]`: article says $3.47$ fm; finding 094 says $4.80$ fm — discrepancy unresolved** | **Either value exported without resolution** | **§1.7** |
| Born rule / Ghost Manifold | Philosophical interpretation `[HEUR]` | Derivation of quantum probability | SG-PL-8 |
| Spin gate $(1+s_is_j)$ | Binary gate; values 0 or 2 | SU(2) projector or matrix element | SG-PL-9 |
| $\rho_s=\frac{3}{2}J$ mapping | Hypercubic only `[ALG]` | Valid for ESM | SG-PL-11 |
| Soft-spin SU(2) | Effective doublet; $\varepsilon\ll1$ required | SM SU(2)$_L$; exact symmetry | SG-PL-12 |
| SU(3)/U(1)² analog | Narrow window; doesn't reproduce QCD | SU(3) color | SG-PL-5,6 |
| Anomaly cancellation | Necessary lattice condition | Full QFT anomaly-free proof | §1.4 |
| Tree-level EH action | Tree-level only; loop corrections missing | Fully quantum-corrected GR | OPEN-PL-4,8 |
| Lensing surplus $+0.01''$ | `[HEUR strong]`; not yet confirmed | Confirmed GR deviation | §1.15 |
| Cosmic expansion | `[HEUR]`; $N=175$, single seed | Validated cosmological derivation | SG-PL-14 |
| Hawking temperature | Within 2× of GR; structural `[HEUR]` | Exact Hawking derivation from RTG | §1.15 |
| EFT $C_\kappa^\infty\approx0.00911$ | Universal geometric constant `[NUM strong]` | Scheme-dependent quantity | §1.7 |
| RTG→GR pipeline | Phases I,VIII solid; rest `[HEUR]` or open | Proven GR derivation | OPEN-PL-13 |
| Observer node | `[FAIL]` — all nodes equivalent | Any node having special measurement status | SG-PL-15 |
| 4D corridor no gauge | `[ALG]` three conditions fail | Gauge field applicable without GVT tests | OPEN-PL-12 |
| Clipping $\mathcal{R}_{ij}$ to $[0,3]$ | Modeling choice; disclose; can manufacture artifacts | Harmless numerical fix | §1.11 |
| Higgs-like $m_H\approx125$ GeV | $c_{\rm eff}=0.3c$ chosen, not derived | Derived Higgs mass prediction | §1.15 |
| Dual-J values | Two calibration contexts; not interchangeable | Substituting without specifying context | §1.7 guard |

---

## §6. Main Scientific Ledger

### §6.1 Substrate Evolution — Why Each Failed

`[FAIL]` **All-to-all (Phase 0).** No spatial crystallization without locality; $O(N^2)$ scaling. Resolution: $\mathcal{R}_{ij}$ naturally induces sparse graph via bandwidth cutoff — not imposed.

`[FAIL]` **Cubic lattice $L^3$ (Phase 1).** (1) Artificial Cartesian symmetry; (2) fixed coordination number; (3) periodic $\mathbb{Z}_L^3$ topology. K₂/K₃ results (proton, CHSH, photon) computed on subgraphs — not contaminated — remain valid.

`[FAIL]` **Spherical lattice (Phase 2).** (1) Pre-defined center = absolute position (OFN §1.1 violation); (2) shell discontinuities; (3) radial/angular asymmetry; (4) no natural K₄ minimal unit.

`[HEUR]` **Why K₄ survives** (selection-by-elimination). After removing Cartesian preference and hidden center, the requirement is a graph that is (1) background-independent, (2) $b_1\geq3$, (3) admits non-trivial SU(2) holonomy ($\geq4$ nodes), (4) fully symmetric. $K_4$ is the minimum satisfying all four by elimination. **This is not a uniqueness proof** — it is the argument that remained after the two substrate failures. A positive first-principles derivation that $K_4$ is the unique or canonical minimal graph is OPEN-OFN-3C. `[RID: PL-HEUR-K4-SELECTION-BY-ELIMINATION]`

### §6.2 Kernel Properties — Why Correct Physics on Wrong Substrates

`[ALG]` **Substrate independence.** $\mathcal{R}_{ij}$ depends only on $(\Delta\phi_{ij},\Delta\omega_{ij},s_is_j)$ — no absolute positions or lattice topology. Every pairwise observable from $\mathcal{R}_{ij}$ is substrate-independent. Wrong substrates → correct K₂/K₃ observables.

`[ALG]` **RG universality.** $\Delta\omega^*$ is an IR fixed point. Wrong UV substrates do not shift IR fixed points provided kernel symmetries are preserved. Reason the pre-Legacy period got correct CHSH and proton radius on cubic lattice.

`[ALG]` **Three-factor structure of $\mathcal{R}_{ij}$.** Each factor is independently derivable: phase cosine from U(1) symmetry; Gaussian from RG bandwidth; spin gate from pair complementarity. No factor is redundant; all three are necessary for correct physics.

### §6.3 Constants and Default Parameters

| Symbol | Value | Tag | Source |
|---|---|---|---|
| $\Delta\omega^*$ | $(1.45\pm0.08)\times10^{23}$ rad/s | `[ALG]` | Two-loop RG |
| $g^*$ | $1.14\pm0.02$ | `[ALG]` | Two-loop RG fixed point |
| $c$ | $2.998\times10^8$ m/s | — | SI |
| $\hbar$ | $1.055\times10^{-34}$ J·s | — | SI |
| $E^*$ | $\approx95.4$ MeV | `[ALG]` | $\hbar\Delta\omega^*$ |
| $\ell_*=a$ | $2.07\pm0.11$ fm | `[ALG]` | $c/\Delta\omega^*$ |
| $r_*$ | $13.0\pm0.7$ fm | `[ALG]` | $2\pi\ell_*$ |
| $K'$ | 12.0 MeV | `[NUM]` proton context | Particle & Nuclear §4 |
| $J$ | 2.3 MeV (proton); 3.24±0.12 MeV (ESM) | dual-value guard | §1.7 |
| $J_{\rm ex}$ | 0.5 MeV (proton); 2.20±0.08 MeV (ESM) | dual-value guard | §1.7 |
| $\sigma_{\rm exch}$ | $\approx\Delta\omega^*$ | `[DEF]` UV regulator | — |
| Proton $r_p$ | $0.84\pm0.01$ fm | `[NUM strong]` | Math Foundations §11 |
| CHSH $S$ | $\approx2.827$ | `[NUM strong]` | Math Foundations §11 |
| $\sigma_{\rm crit}$ | $\approx0.589\Delta\omega^*$ (complete decoherence) | `[NUM]` | core_notes §1.1 |
| $C_\kappa^\infty$ | $\approx0.00911$ (spread $\leq0.13\%$) | `[NUM strong]` | EFT v1.4.2 |
| $\kappa_B$ | $(3.675\pm0.002)\times10^{-3}$ MeV | `[NUM]` | EFT v1.4.2 |
| $e_{\rm eff}$ | $\approx16.49=\kappa_B^{-1/2}$ | `[NUM]` | EFT v1.4.2 |
| $f_P$ | $\approx2.31\times10^{22}$ Hz $=\Delta\omega^*/(2\pi)$ | `[DEF]` | RTG Planck freq (≠ standard) |
| $c_{\rm eff}$ | $\sim10^3$ m/s (molecular) | `[DEF]` | Replace $c$ at molecular scale |
| $m_0$ | $1.7\times10^{-28}$ kg | `[HEUR]` | $\hbar\Delta\omega^*/c^2$ |
| $K$ (elastic) | $1.9(2)\times10^{-12}$ J·s | `[NUM strong]` | HMC fit |
| $A$ | $(3.6\pm0.3)\times10^{-3}$ J·m | `[NUM strong]` | HMC fit |
| $\kappa_{\rm grav}$ | $-0.175$ | `[NUM]` canonical | Working Document v12.2 |
| $\Delta_{\rm RMS}$ (κ₃) | $0.52$; flux corr $\approx-0.02$ | `[NUM]` | Working Document V2 |
| $\eta_{\rm hot}$ | $0.75$–$0.80$ | `[NUM strong]` | FCC baseline |
| $\eta_{\rm cool}$ | $0.403$ | `[NUM strong]` | Grown cluster $N=175$ |
| $\beta_1$ (matter) | 8 | `[NUM strong]` | Grown cluster |
| Spectral gap | $\lambda_9/\lambda_8\approx10^9$ | `[NUM strong]` | L1 Laplacian |
| $G_{\rm cosmo}$ | $\approx50$ (mass2 threshold) | `[NUM]` | Drift engine |
| $\Delta\approx0.5$ | holonomy deficit K₄ | `[NUM strong]` | κ₃ Ricci article |
| $\kappa_{\rm top}$ | $3=b_1(K_4)$ | `[ALG]` | κ₃ Ricci article |

---

## §7. Import Ledger

### §7.1 Already imported from pre-Legacy (confirmed in Legacy DSN)

$\mathcal{R}_{ij}$ kernel and gate structure; $\Delta\omega^*$ and $g^*$; proton $r_p=0.84$ fm; CHSH $S\approx2.827$; frustration field $z$ and log force; holonomy deficit $\Delta\approx0.5$; $\kappa_{\rm top}=b_1(K_4)=3$; ESM quantum foam 75.2%; K₄ selection-by-elimination rationale; observer `[FAIL]`.

### §7.2 Active import candidates (not yet in Legacy DSN)

| Item | Tag | Route |
|---|---|---|
| Hodge three-way decomposition ($z=z_{\rm ex}+z_{\rm co}+z_{\rm h}$) | `[ALG]` | ESM validation suite |
| Screening Theorem ($D_1B=D_1z_{\rm co}$, error $10^{-12}$) | `[NUM strong]` | ESM validation suite |
| Cooled vacuum $\eta_{\rm irr}=0.403$ vs hot foam $0.75$–$0.80$ | `[NUM strong]` | ESM validation suite |
| Topological matter $\beta_1=8$, spectral gap $10^9$ | `[NUM strong]` | ESM matter identification |
| Canonical gravity coupling $\kappa_{\rm grav}=-0.175$ | `[NUM]` | ESM gravity programme |
| κ₃ Stratified Active Matter (stratification/plasticity/protection) | `[NUM]` | L2 κ₃ programme |
| BCH commutator as named origin of κ₃ stiffness | `[ALG]` | Genesis DSN holonomy |
| SU(2) lift Pauli matrix form ($\hat{J}_i=\cos\theta_i\sigma_1+\sin\theta_i\sigma_2$) | `[ALG]` | L0 Master Definition |
| 4D corridor non-gauged argument (three conditions) | `[ALG]` | EFT §2; future gauge programme |
| Cosmology drift phase diagram ($G=5,20,\geq50$) | `[NUM]` | Cosmology programme |
| Dual-J notation guard | `[SCOPE]` | Any study importing $J$ |
| NS bifurcation → 4D torus (K₄ double-NS) | `[HEUR]` | Genesis DSN Phase 1A/1B |

---

## §8. Article Registry

Articles read: 68 (67 pre-Legacy physics + 1 Legacy out-of-scope). Full corpus coverage.

| # | Title | Status | Key pre-Legacy content |
|---|---|---|---|
| 1 | Glossary of RTG Terms | Full | $\mathcal{R}_{ij}$, $r_{ij}$, $s_i$, observer corrected |
| 2 | Core Principles & Foundations | Full | Energy First; no-observer; void origin |
| 3 | Mathematical Foundations | Full | Kernel; CHSH $S=2.827$; proton K₃ |
| 4 | Enriched Geometric Concepts | Full | $S_{\mu\nu}$; $U_{\rm curv}$; resonance lattice |
| 5 | Two-Loop RG Derivation | Full | $\beta(g)$; $g^*=1.14$; $\Delta\omega^*$; ESM FAIL |
| 6 | Forces & Fields (v2.2) | Full | Four forces; bond energy forms; gate conventions |
| 7 | Gauge Symmetries (v1.4e) | Full | Three windows; soft-SU(2); anomaly conds |
| 8 | RTG Gravity I | Full | Six-step metric; tree-level EH |
| 9 | RTG Gravity II | Full | Running $G$, $\Lambda$; anomaly checks |
| 10 | κ₃-Sector as Emergent Ricci Curvature | Full | $\Delta\approx0.5$; $\kappa_{\rm top}=3$; Wilson loop |
| 11 | Quantum Behaviours (v1.4) | Full | CHSH; $\sigma_{\rm noise}$; decoherence cliff |
| 12 | Particle & Nuclear (v2.4) | Full | Proton params; Ca-40; lattice action |
| 13 | Cosmological Applications | Full | Expansion; Hawking; CMB; BH corridor |
| 14 | Relativistic Effects | Full | GPS; lensing surplus $+0.01''$; no-signalling |
| 15 | Advanced Topics (v1.3) | Full | Resonance cascade; historical $\Delta\omega^*$ `[FAIL]` |
| 16 | What Is a Photon (v1.4) | Full | Photon def; polarization; cliff mass |
| 17 | Photon Dynamics (v1.6) | Full | E,B fields; Maxwell derivation; lattice spacing corrected |
| 18 | RTG CHSH vs Decoherence | Full | CHSH sweep; $\sigma_{\rm crit}$ |
| 19 | Thermodynamics & Rotational | Full | Two temps; internal energy; heat flow |
| 20 | Lattice Hamiltonian Workbook (v1.4) | Full | Continuum action; ESM angular deficit |
| 21 | Enriched Geometric Concepts | Full | (see #4) |
| 22–26 | (v0.2 cross-check articles) | Full | See v0.2 release notes |
| 27 | Photon Mass Relation (v1.6) | Full | Whirling freq; spectroscopic table |
| 28 | Gravity as Residual Elasticity (v1.6) | Full | HMC $1/r$ fit; $A$, $K$; effective $G$ |
| 29 | Photon's Dimensional Journey (v1.3) | Full | 1D→2D; RTG Planck freq; $r_{\rm node}$ `[FAIL]` |
| 30 | From 2D Quarks to 3D Proton (v1.2) | Full | Design principles; $r_p=0.87$ `[FAIL]` |
| 31 | Spherical Lattice Rethinking | Full | Cornell potential; spherical `[FAIL]` |
| 32 | Cosmological Dynamics | Full | Energy partition; zero-sum init; Kuramoto |
| 33 | From RTG to EFT (v1.4.2) | Full | $C_\kappa^\infty$; Ward residual; $\kappa_B$; $e_{\rm eff}$ |
| 34 | Water Density 4°C (v1.0) | Full | $T=\hbar\delta\omega/k_B$; $c_{\rm eff}$ molecular |
| 35 | Higgs-like Particle (v2.0) | Full | Tetrahedral VEV; $m_H\approx125$ GeV (`[HEUR]` only) |
| 36 | Genesis of Resonance | Full | Kernel construction; Kuramoto; spin conservation |
| 37 | RTG–EFT Release 2025-09-03 | Full | Canonical data source for $C_\kappa^\infty$; acceptance gates |
| 38 | Running the RTG–EFT Suite | Full | Scripts; `amp=none` baseline; 5 acceptance gates |
| 39 | 4D Corridors — Why Not Gauged (v0.9) | Full | Three conditions; corridor non-gauged; GVT-1–4 |
| 40 | Enhancing Speculations on Dim. Emergence | Full | Dimensionality as resonance attractor; threshold diagnostics |
| 41 | Observer Relativity | Full | **`[FAIL]` framing** — observer node privileged reference |
| 42 | RTG — A New Lens | Full | "Node alone is meaningless"; information principle |
| 43 | RTG↔SI Calibration & Planck Observer (v3.1) | Full | Planck observer = calibration convention; two anchors |
| 44 | RTG Proton Model (v0.7) | Full | Triangle geometry; neutron companion |
| 45 | Black Hole Resolution (v1.8) | Full | $E_{\rm th}$; $r_{\rm th}$; empirical knee $x\approx0.69$ |
| 46 | RTG Hydrogen (v0.1) | Full | U(1)×SU(2) straddle; Bohr-scale radii |
| 47 | RTG→Geometry→GR (v2.2) | Full | 14-phase pipeline; NS mechanism; conjectures 1,2 |
| 48 | Post-v2 Roadmap | Full | Phase 1A/1B; scripts; beyond K₄ |
| 49 | κ₃-Sector as Emergent Ricci Curvature | Full (re-read) | Wilson loop; BCH; energy barrier |
| 50 | Power Rule as Chaos's Silent Architect (v7.3) | Full | Clipping caveat; κ₃ holonomy thermostat |
| 51 | Deterministic Ghost Scaling (v1.0) | Full | $\gamma=1/(2\alpha_t)$; clipping caveat |
| 52 | RTG — A New Lens (re-read) | Full | (see #42) |
| 53 | RTG↔SI Calibration (re-read) | Full | (see #43) |
| 54 | RTG Proton Model (re-read) | Full | (see #44) |
| 55 | Black Hole Resolution (re-read) | Full | (see #45) |
| 56 | RTG Hydrogen (re-read) | Full | (see #46) |
| 57 | Geometry of Forgetting | Full | Ghost Manifold; memory depth M; triple-slit prediction |
| 58 | Quantum Foam Vacuum (ESM, Jan 2026) | Full | Four-phase ESM; two boundary metrics; Machian feature |
| 59 | Working Document: Gauge & Gravity (v12.2) | Full | Screening $10^{-11}$; cooled vacuum; $\kappa=-0.175$; pub tiers |
| 60 | Working Document: Gauge & Gravity V2 (v11.0) | Full | Four Pillars; FCC vs grown; $\Delta_{\rm RMS}=0.52$ |
| 61 | Emergent Gravity and Structure Formation | Full | Log force derivation; necessity; vacuum viscosity |
| 62 | κ₃ Sector in RTG | Full | Stratified Active Matter; BCH; Pauli lift; Betti z-score |
| 63–67 | (see v0.6 registry #47–51) | — | — |
| 68 | **RTG L0 Master Definition (v1.2)** | Full | **LEGACY DOCUMENT — out-of-scope for pre-Legacy ledger.** Canonical SU(2) lift Pauli form; L0 node atom; layer-consistency rule. Pre-Legacy connection: formalizes operations used informally in κ₃ work. Cross-reference: Legacy DSN. |

---

## §9. Collaboration and Provenance

**Authors:** Mustafa (PI) · Claude  
**Date:** June 2026  
**Method:** 68 rtgtheory.org articles across seven reading sessions + cross-check against `core_notes_v1.19.md` and `findings_v1_14.yaml` (Jan 14 2026 v12.2 freeze). v0.7 restructured for conciseness: ~25% line reduction, duplication eliminated, quick-retrieval table added, Ca-40 flag moved to §5, Four Pillars moved to §1.9, dual-J guard placed adjacent to proton table.

**Epistemic tiers:**
- **Tier 1** `[NUM strong]`/`[ALG]`: kernel, RG, CHSH, proton, GPS, HMC $1/r$, EFT $C_\kappa$, spectroscopic, Ward, κ₃ holonomy, $\kappa_{\rm top}$, Screening Theorem, cooled vacuum, $\beta_1=8$ gap, log force necessity
- **Tier 2** `[HEUR]`/`[HEUR strong]`: Maxwell, Hawking, lensing surplus, temperature calibration, water density, Kuramoto, equivalence principle, torsion, relational light cones, proton triangle geometry, BH corridor, vacuum viscosity, Four Pillars, proto-gravity
- **Tier 3** `[ONTO pre-legacy]`/speculative: void origin, RTG→GR conjectures 1&2, Higgs-like, RTG Hydrogen, RTG Radion, cosmic structure
- **Tier 4** `[ONTO pre-legacy philosophical]`: Ghost Manifold, memory depth M, Born rule as projected thickness

---

## Appendix A — Version History

### v0.8 — June 2026

Audit pass against Legacy/Dyadic/OFN programme state. No physics removed; tags and framing corrected to reflect current understanding.

**Tag corrections (overclaims demoted):**
- §1.1: kernel "three structural reasons" `[ALG]` → `[HEUR]` (construction motivations, not derivations; OPEN-P0)
- §1.1: bond energy scope note added (`[scope: continuous effective model]`); TDR-G sine-term import guard added
- §1.2: $c_{m spec}=a\cdot\Delta\omega^*$ `[ALG]` → `[HEUR]` `[scope: conditional on canonical generator; circular unless OPEN-P0 closes]`
- §1.3: dimensional ladder `[ALG]` → `[ALG]` `[scope: conditional on $\mathcal{R}_{ij}$ model; OPEN-P0]`
- §1.4: chronological consistency `[ALG]` → `[HEUR]` (physical interpretation, not proved from relational axioms)
- §6.1: K₄ selection `[ALG]` → `[HEUR]` (selection-by-elimination; uniqueness proof = OPEN-OFN-3C)

**Internal consistency fixes:**
- §0.2: node description updated to "relational difference carriers, not ontological primitives" (OFN §1.1)
- §1.1: multilayer hierarchy Level 0 corrected from "fundamental nodes" to "relational difference carriers"
- §1.5: frustration field $\kappa=2\pi c$ identity made explicit (matches beat-distance in §1.1)
- §1.5: weak force spin-flip retagged `[ONTO pre-legacy]`; note added that discrete transitions are events in current programme
- §1.6: photon definition corrected — $\Delta\omega_{12}=0$ refers to constituent nodes; $\omega_\gamma=c|\mathbf{k}|$ is propagation frequency
- §1.8: SU(2) lift bridging note added (Pauli-matrix lift supersedes binary gate at Legacy level)
- §1.9: Four Pillars step 4 (gravity) notes OPEN M and OPEN-P3 as additional blockers
- §1.10: void origin narrative updated with OFN dyad-vs-triad primacy note (first event is relational distinction, not node-pair creation)
- §1.12: $\Lambda_{m eff}$ citation corrected — 75.2% is Phase-0 seed floor; mature ESM uses $\eta_{m cool}=0.403$
- §1.12: K₄ NS mechanism and spin-2 graviton status updated (HYP open; OPEN M required)
- §1.7: K₃ minimal-loop entry retagged `[HYP]` with OPEN-OFN-3A/3B pointers

**Pointer updates:**
- OPEN-PL-3: added OFN OPEN-OFN-3C pointer
- §3 SG-PL-1: SG-PROG-2 cross-reference added
- §4 routing table: kernel → Dyadic DSN corrected ($\mathcal{R}_{ij}$ ≠ $T(ho,\eta)$; OPEN-P0 is the bridge question)

### v0.7 — June 2026

Restructured for conciseness. ~25% reduction from 1,528 to ~1,150 lines. No physics removed — all content consolidated or cross-referenced from authoritative location.

**Structural changes:** Added quick-retrieval table. Collapsed three restatements of dimensional thresholds to §1.3 as single authoritative location. Consolidated four $\Delta\approx0.5$ restatements to two (opening + derivation). Merged gravity $z$-field standalone entry with `[DEF]` block. Removed orphan formulas ($Z_{\rm space}$, $C_{12}$, CHSH four-row table condensed). Compressed four trivial §1.11 `[DEF]` entries. Moved Four Pillars to head of §1.9. Moved dual-J guard to §1.7 adjacent to proton table. Moved ESM cosmology hygiene to §1.11. Moved Ca-40 `[NEED CHECK]` to §5 high-risk ledger. Removed body-text `[FAIL]` duplicates — Appendix B consolidated into §6.1. Trimmed §6.2 kernel properties. Updated article registry for conciseness.

### v0.6 — June 2026
Internal KB cross-check; ESM unified framework; spectral gap; canonical $\kappa=-0.175$; SU(2) lift algorithm; BCH commutator; Stratified Active Matter; articles 62–68.

### v0.5 — June 2026
Observer `[FAIL]`; 4D corridors; RTG→GR pipeline; proton triangle; neutron; BH corridor; hydrogen; NS mechanism; torsion; clipping caveat; articles 47–61.

### v0.4 — June 2026
Gravity HMC numbers; spectroscopic table; EFT geometry factor; temperature calibration; articles 37–46.

### v0.3 — June 2026
Lattice spacing correction; thermodynamics; cosmology; articles 27–36.

### v0.2 — June 2026
Cross-check corrections; articles 22–26.

### v0.1 — June 2026
Initial release; 21 articles.

---

## Appendix B — Retired and Rejected Claims

`[FAIL]` **Pure all-to-all interaction.** No spatial crystallization; $O(N^2)$.

`[FAIL]` **Cubic lattice $L^3$.** Artificial Cartesian symmetry; fixed coordination; periodic artifacts.

`[FAIL]` **Spherical lattice.** Absolute center; shell discontinuities; radial/angular asymmetry; no natural K₄ unit.

`[FAIL]` **Hookean gravity $V\propto(r-r_0)^2$.** Runaway expansion (+136%) at $G=50$; self-force bug and parametric instability. Replaced by logarithmic potential.

`[FAIL]` **Hypercubic $\rho_s=\frac{3}{2}J$ for ESM.** ESM has 7.36° geometric frustration; mapping invalid. Use Test-Field Calibration.

`[FAIL]` **Abstract β-function $\beta=-b_1g^2-b_2g^3$.** Correct form has $+0.72g$ linear term.

`[FAIL]` **Early bandwidth $\Delta\omega^*=2.18\times10^{23}$ s⁻¹.** Superseded by two-loop RG: $(1.45\pm0.08)\times10^{23}$.

`[FAIL]` **Lattice spacing $a=2.07\times10^{-16}$ m = 0.207 fm.** Factor-10 error. Correct: $a=2.07\times10^{-15}$ m = 2.07 fm.

`[FAIL]` **Resonance-modulated distance $r=(2\pi c/|\Delta\omega|)\cdot\mathcal{R}_{ij}^{-1}$.** Superseded by standard $r_{ij}=2\pi c/|\Delta\omega_{ij}|$.

`[FAIL]` **Node radius $r_{\rm node}=2.07\times10^{-16}$ m.** Same factor-10 error. Correct: 2.07 fm.

`[FAIL]` **Proton radius $r_p=0.87$ fm in early articles.** Correct: $0.84\pm0.01$ fm.

`[FAIL]` **Observer node as privileged reference.** All nodes equivalent; any node serves as computational reference. $\Delta\omega^*$-observer = calibration convention.

`[FAIL]` **ESM signed coupling ($q=z_h$) in cosmology drift engine.** Produces blow-up divergence due to mode mixing. Use mass2 ($q=z_h^2$).

`[FAIL]` **−83% gravity interaction energy.** Baseline-normalized figure from Working Document V2 §4. Superseded by canonical $\kappa_{\rm grav}=-0.175$.

---

*END OF DOCUMENT — RTG_PRE_LEGACY_DSN_v0.8*  
*Supersedes v0.7. Knowledge-distillation and provenance ledger; no new derivations. All scientific results extracted from rtgtheory.org articles and cross-checked against core_notes_v1.19 / findings_v1_14. Written for AI audience: dense, minimal redundancy, sequenced for retrieval. 68 articles read (67 pre-Legacy + 1 Legacy). 100% corpus coverage.*
