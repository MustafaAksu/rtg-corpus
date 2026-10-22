# RTG — ER-2B Consolidated Study v0.3

**Title:** Finite-Clock Separability, Triadic Chirality, Cubic Return and Additive-Carrier Selection  
**Date:** 19 October 2026 (v0.3 synchronization). Scientific body dated 10 October 2026 (v0.2).  
**Document class:** Consolidated noncanonical research source and provenance record  
**Status:** **WORKING / NONCANONICAL — NOT OWNER-ADOPTED.** Kept in project files as a reference record. It is not a handoff request.  
**Supersedes:** `RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md` (noncanonical, SHA-256 `ea26d3d1a4853ac88d1938dcb66c76eda4d55980ebf6f4d61091b97d67b2bb5e`), as the project copy only. The v0.2 package (`RTG_ER2B_CONSOLIDATED_v0_2.zip`, SHA-256 `8c6352906143653a1736848e289da9765876927e3d2f089389c3a29326a048ee`) is retained unchanged as the evidence archive.  
**What v0.3 changes:** Part A is new. It records where each ER-2B claim lives in the October 2026 corpus, withdraws the stale v0.2 handoff requests, repins source versions, and records one new cross-check (§A.4). Part B is the complete v0.2 scientific body, **verbatim**. No v0.2 formula, grade or scope is changed.  
**Governance:** `ER2B-Cxx` are local IDs, not owner RIDs. Every `[ALG]`/`[THM]` holds only inside its declared conditional model. Where Part A and Part B disagree about routing or source versions, Part A governs. On mathematics, Part B stands as written.

---

# PART A — v0.3 synchronization (19 Oct 2026)

## A.1 Current-state summary

1. **Two pieces have entered owner DSNs.**
   - The (ν, χ) six-step cubic of the projected K3 model (C10) is now the source cubic of `GEN-THM-K3-PLANAR-FACTOR-NOGO` (Genesis v2.8.6 §6.3a(d)) and `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` (Genesis v2.8.7 §6.3a.1). Genesis re-derived it independently (`k3_obstruction_exact_check.py`, `384aaa5f…01ee`). It does not rest on this document.
   - The RER–Genesis G5 modal application of that theorem is owner-closed in the RER/Genesis line.
2. **Several owners cite ER-2B as noncanonical context.** Genesis §8 pins the archive `ER2B_OBSERVABLE_RESPONSE_v1.zip` (`06d5e0c9…82b1`) as the historical coefficient source. That archive is inside the v0.2 package, and its hash was re-checked on 19 Oct 2026: it matches. The v0.2 package must therefore be kept.
3. **The central open question C16 has been addressed in substance outside ER-2B.** The question was: which carrier makes K3 closure additive? The FMS/OFN model-selection chain (SESSION grade) gives the current answer:
   - the raw carrier fails cubic-order Standard C for every coupling κ ≠ 0;
   - the h-transported carrier is the primary candidate;
   - it becomes a real carrier once DYAD OPEN 20 B-6 / B-∞ (existence of J = T∘F^{−1/6}) is answered.

   See `claude/OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_7_1.md`. This is not adopted OFN text.
4. **The v0.2 handoff requests (§8 and `HANDOFF_TO_STREAMS.md`) are withdrawn.** They were addressed to superseded owner versions (A.3). Any remaining item should be sent as a new, short request against current versions (A.5).

## A.2 Claim disposition against the October 2026 corpus

Legend:
- **CANONICAL-REDERIVED**: an owner DSN contains the content, proved independently.
- **CITED-NONCANONICAL**: an owner names ER-2B as context only.
- **SUPERSEDED-ROUTING**: the question was answered elsewhere.
- **NOT TAKEN UP**: no current owner record.

All Part B mathematics stays valid at its declared scope whatever its disposition.

| ID | Capsule | Disposition (19 Oct 2026) | Current location / note |
|---|---|---|---|
| C01 | Mixed-derivative separability test | NOT TAKEN UP | — |
| C02 | Projected-unary nonclosure | NOT TAKEN UP | — |
| C03 | n = 1…6 obstruction ladder | NOT TAKEN UP | — |
| C04 | First six-step cubic G₃, covariance | Content used by Genesis without citing C04 | Genesis §6.3a(b): leading-term lemma, F₁⁶ = id + f₃ + O(4) |
| C05 | Direct cubic source is separable | NOT TAKEN UP | — |
| C06–C08 | Eight-component obstruction; χ; cyclic reduction to (ν, χ) | Basis consistent with Genesis; no import | Genesis §6.3a(d) writes f₃ in exactly the (ν, χ) form |
| C09 | Chirality/area bridge | NOT TAKEN UP | Triadic v1.6 orientation typing (Ω_T = −√3 ω_raw) is a separate convention; do not mix with Ω_G |
| **C10** | Genesis ν = 1/6 − i√3/3, χ = 1/3 | **CANONICAL-REDERIVED** | Genesis v2.8.6 §6.3a(d), v2.8.7 §6.3a.1; source archive pinned in Genesis §8 |
| C11 | ΔN, ΔS response | NOT TAKEN UP | — |
| C12 | Signed-Gram quartic updates | NOT TAKEN UP | RECOG v0.3.20 has no ER-2B import |
| C13 | Conditional local outflow Δ₄N = N²/6 + 2S² | CITED-NONCANONICAL | Genesis §6.3a `[INTERP]` ("ER-2B OBS-1, noncanonical"); Genesis SG-16 blocks transport of ER-2B shape-sphere results to γ ≠ 1 |
| C14 | ν = μ₃ + μ₂₂/3 source split | NOT TAKEN UP | — |
| C15A/B | Passive transport versus new normalized-addition model | CITED-NONCANONICAL | RRF v0.8.2 §0.3 states the same rule as its own representation discipline; §8.1 nonclaim |
| **C16** | Four model selections, carrier first | **SUPERSEDED-ROUTING** | FMS/OFN chain (A.1 item 3); OFN v0.9 RF-O09-03 records that primary ER-2B evidence was not supplied there |
| C17A/B, C18 | Node/edge algebra; Pre-Legacy scope; resonance agenda | NOT TAKEN UP | Pre-Legacy v0.8 predates ER-2B |
| C19 | Six-parameter quadratic carrier freedom | CITED-NONCANONICAL | RRF v0.8.2 §0.2, §6.2 source pointer, §8.1 ("conditional mathematics, not a passive-gauge family of one triad") |
| C20 | σ-continuum and the 13.4 % / 29.3 % thresholds | CITED-NONCANONICAL, plus the new cross-check in A.4 | RRF v0.8.2 §8.1; the σ = 1 endpoint coincides with the FMS transported cubic |

## A.3 Superseded source pins in Part B

Part B is pinned to the owner versions current on 10 Oct 2026. Current versions on 19 Oct 2026:

| Part B pin | Current owner version | What matters for ER-2B |
|---|---|---|
| DYAD v6.4.10 | **v6.4.13** (adopted 18 Oct) | Adds the formal centralizer, the canonical ℤ₆ generator J, Lemma F / F1–F3 and OPEN 20 B-an / B-6 / B-∞. None of this changes C04/C14/C19, but it fixes the realization target of the transported carrier |
| Genesis v2.8.5 | **v2.8.7** (adopted 18 Oct) | §6.3a / §6.3a.1 (K3 factor no-gos built on the C10 cubic); §6.3b mean-feedback family; SG-15, SG-16 |
| Triadic v1.6 | v1.6 (unchanged) | CN-05 orientation normalization; the historical wedge, basin and steering chain is withdrawn from current use |
| OFN v0.8 | **v0.9** (adopted 13 Oct) | RF-O09-03; FMS handoff disposition. The v0.10 candidate content is in the SESSION OFN reply |
| RRF v0.7 | **v0.8.2** (adopted 17 Oct) | §0.3 passive-versus-model rule; RRF-CND-01; ER-2B nonclaims in §8.1 |
| Pre-Legacy v0.8 | v0.8 (unchanged) | — |

Part B §0 item 5 states Ω_T = −2Ω_G. Triadic v1.6 CN-05 now types its planar convention as B_T = 2B_G and Ω_T = −√3 ω_raw for identified planar vectors. Before using either relation, convert explicitly. Neither is a birth or mode bridge.

## A.4 New cross-check: the C20 endpoint equals the FMS transported cubic `[ALG]`

In C20, set σ = 1 (k = 0): the full quadratic normalizer chart with linear closure re-imposed. Then
- ν(1) = μ = −½ − 2i√3/3 and χ(1) = 0;
- Δ₄N = −½N² + 2S²;
- Δ₄S = −⅓NS.

The FMS/OFN transported κ-family has, independently, the κ-independent six-step cubic f_e = μ(w_e|w_e|² − ⅓Σ_j w_j|w_j|²). This is the raw-K3 cubic with ν → μ and χ → 0 (OFN reply v0.7.1 §3.4).

Re-check, 19 Oct 2026, exact sympy on the closure plane Σw_e = 0, with N = Σ|w_e|² and S = Im(w₁w̄₂):
- the cubic f gives ΔN = 2Re Σ w̄_e f_e = −Σ|w_e|⁴ = −½N² + 2S²;
- it gives ΔS = −⅓NS;
- both residuals vanish identically.

**Reading.** Two derivations agree at cubic order:
- ER-2B's σ-continuum (quadratic chart only);
- FMS's transported carrier (full λ-equivariant chart).

The C20 interpolation is therefore a one-parameter path from the raw K3 model (σ = 0, outward) to the transported class (σ = 1, inward). Its two thresholds mark where the uniform outward drift is lost (13.4 %) and where uniform inward drift begins (29.3 %).

**Limits.**
- This is a cubic-order identity only. Beyond cubic order the two models differ in general (OFN v0.7.1 §3.5(a)).
- It selects no carrier.
- At its σ = 1 end the transported class is still formal until J is realized.

## A.5 What remains open, and where it would go

| Item | Proposed current destination | Form |
|---|---|---|
| Physical carrier and in-class chart selection (former C16) | OFN / RRF, via the FMS reply | Already in progress; ER-2B is background only |
| C11–C12 signed-Gram observable updates | RER / RECOG | New short request against RECOG v0.3.20 / current RER, if wanted |
| C17A–C18 node-flow versus edge-map comparator | Pre-Legacy / OFN | New request, if wanted; no source-defined comparator exists yet |
| C13 certified finite radius | Genesis (optional) | Not a prerequisite for anything current |

## A.6 Evidence identities (re-hashed 19 Oct 2026, from the v0.2 package)

| File | SHA-256 |
|---|---|
| `RTG_ER2B_CONSOLIDATED_v0_2.zip` (whole package) | `8c6352906143653a1736848e289da9765876927e3d2f089389c3a29326a048ee` |
| `RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md` | `ea26d3d1a4853ac88d1938dcb66c76eda4d55980ebf6f4d61091b97d67b2bb5e` |
| `CLAIM_REGISTER.json` | `e6c874219a8612a51b9ffa6f49c8059f86b63d3487a84c31c6ef8a55c93c3345` |
| `MANIFEST.json` | `92c884eb0fa174e4e499ad25ed1f12ff939f9674090b140164f0fb6f40f8cf05` |
| `HANDOFF_TO_STREAMS.md` (withdrawn, history only) | `b464a9a61582cca1ef776e4407e812287699795a6b834d42cf289b7819158d9c` |
| `repro/check_carrier_continuum.py` | `48cf58ede5e0d54bb0e71897467dffc25c86c278a13d92b0a6e7fdd52f5c76e5` |
| `repro/check_iterate_family.py` | `1b56c343d4c9d2462d7adeaac599be0ba454003b23da3ffc1f8fce50308891c1` |
| `evidence/original_review_archives/ER2B_OBSERVABLE_RESPONSE_v1.zip` (**Genesis-pinned**) | `06d5e0c90d864ee8f5ab5ecfa7cadac5e76272a0b4754955bf43ecdcbc4b82b1` |
| `…/ER2B_GENERAL_QUADRATIC_REVIEW_v1.zip` | `2422cb28a919241a863ee9ebfd5ae8a1ec495f3f23251619ee8d66ec4b9bc398` |
| `…/ER2B_CHIRALITY_BRIDGE_v1.zip` | `541d2b9e8bc6d5292376506147a35869808ca843500a0ecfe326bde8d633a640` |
| `…/ER2B_SOURCE_SPLIT_OCT10_v1.zip` | `d7a5c5e5a535d4758902ddf9cea396ed26926bbd142788cac10e0a4ce050a2bb` |
| `…/ER2B_OBS1_SCOPE_AMENDMENT_v1_1.zip` | `1fa9ca0c23de5c3f1ebfa2b533d66ab1afc1086db42081ac4c19d5ca1f0b4601` |

**Package erratum.** The v0.2 `README.md` points readers first to `RTG_ER2B_CONSOLIDATED_STUDY_v0_1.md`. The main file is `…_v0_2.md`; v0.1 is under `evidence/previous_consolidation_v0_1/`.

**Not rerun in v0.3.** None of the v0.2 package scripts was rerun. The only new computation is the sympy identity check of A.4.

## A.7 Change log

- **v0.3 (19 Oct 2026):** Part A added: disposition, withdrawn routing, repins, the A.4 cross-check, re-hashed evidence and the README erratum. Part B kept verbatim. Status unchanged: noncanonical.
- **v0.2 (10 Oct 2026):** review-response working update (see Part B header text in the archived file).
- **v0.1:** initial consolidation (archived in the v0.2 package).

---

# PART B — Scientific body of v0.2 (verbatim, 10 Oct 2026)

> **Reading note.** Everything below is unchanged v0.2 text. Owner-version pins, "handoff" and "receiving stream" language, and "next blocking choice" statements are historical; Part A governs them. The mathematics and its scope guards are unchanged.

---

## 0. Decision abstract: what may, and may not, be handed off

**First resolve the additive carrier:** fixing the same isolated dyad map does not fix a projected K3 model until the affine/closure chart is specified. The following is mathematically settled **only** for the stated conditional carrier and map:
1. **First receiving-stream decision — additive carrier:** the source split, the exact factor \(1/3\), and the outward-versus-inward comparison depend on which edge carrier makes closure additive. Nonlinear **passive** coordinate transport retains the original outward result; imposing **new linear closure** in normalized coordinates defines a *different* inward-return model.  At quadratic order this is a **six-real-parameter local chart selection**, not merely a binary A/B option; a one-parameter slice changes the radial sign after a 13.4% chart interpolation. See C19–C20.
2. The common-unary projected class \(P_{\mathcal C}h^{\times3}\) is **not generally composition closed**. Its first separation obstruction in the named Genesis example appears at the fourth-degree map jet for two steps, and at the cubic map jet from the third step onwards. Thus this obstruction is **clock/iterate-relative**, not an independent-resonance detector.
3. With the fixed \(A\), six primitive steps return to identity at the linear level and cancel the full quadratic jet: \(\mathcal N^6=\mathrm{id}+G_3+O(4)\). The first cubic \(G_3\) transports covariantly under every origin-fixing local diffeomorphism, by its linear derivative at the origin; the three-edge *separable/nonseparable split* uses extra incidence structure.
4. All eight mixed-derivative components of the six-step cubic obstruction are controlled by **one complex coefficient \(\chi\)** (equivalently two real quadrics \(U,V\) in the six quadratic coefficients of \(q=T_2\)). For the Genesis primitive \(\chi=1/3\).
5. The nonseparable cubic difference is exactly \(-2i\chi w_3\Omega_G\) in the registered eigenframe, with \(\Omega_G=\operatorname{Im}(w_1\bar w_2)\). The same chirality has a different numeric normalization in Triadic v1.6: \(\Omega_T=-2\Omega_G\) for identified planar components only.
6. The \(\chi\) obstruction comes entirely from repeated **quadratic** primitive terms. The cubic **radial amplitude response** also depends on the directly cubic source \(T_3\); these are **different** claims.
7. For the conditional Genesis model, \(\nu=1/6-i\sqrt3/3\), \(\chi=1/3\), and \(\Delta_4N=N^2/6+2\Omega_G^2>0\) off the origin. The origin is locally Lyapunov-unstable in this *model*. In the same complex chart isolated DYAD has \(\mu=-1/2-2i\sqrt3/3\); the source relation is \(\nu=\mu_3+\mu_{22}/3\).
8. The historical Pre-Legacy frequency/phase/spin resonance kernel presupposes a richer effective state than a primitive dyad supplies. No independent primitive K3 map has been selected from it. Node-node resonant flows must not be equated with edge-edge resonant maps without clock and carrier transport.



**[OPEN] Four physical/model selections precede broader use:** (a) incidence and primitive coupled update, (b) clock/strobe, (c) admitted norm/readouts and their transport, (d) **additive carrier / which coordinates support linear closure**. This report identifies mathematical alternatives; it **does not choose** between them.
## 1. Fixed mathematical contract and notation

### 1.1 Primitive map and closed three-edge state

Let \(V=\mathbb R^2\), \(x=(\rho,\eta)\), and let the adopted isolated DYAD primitive analytic map be

\[
T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta).
\]

Its jet at zero is

\[
\begin{aligned}
T(x)&=Ax+q_G(x)+r_G(x)+O(\|x\|^4),\\
A&=\begin{pmatrix}1&-1\\1&0\end{pmatrix},\quad A^6=I,\\
q_G(\rho,\eta)&=(0,\rho^2/2),\\
r_G(\rho,\eta)&=(\eta^3/6,(\rho^3+\eta^3)/6).
\end{aligned}
\]

The **conditional** triad state space is

\[
\mathcal C=\{(r_1,r_2,r_3)\in V^3:r_1+r_2+r_3=0\},\quad
P_{\mathcal C}=I_3-\tfrac13\mathbf1\mathbf1^\top.
\]

Write \(r_1=a\), \(r_2=b\), \(r_3=-a-b\), or \(r_1=s\), \(r_2=-s/2+c\), \(r_3=-s/2-c\). The *simultaneous primitive coupled update* is defined as

\[
\boxed{\mathcal N=P_{\mathcal C}\circ T^{\times3}|_{\mathcal C},\qquad F_6=\mathcal N^6.}
\]

The projection belongs to this **map definition** after *every* primitive step. It is **not** a physical healing action, discontinuous reset, constraint force, or an auxiliary clock stage. This map is a model-defined construction, **not** the experimentally/ontologically selected physical K3 generator. \(\mathcal N\) is never replaced silently by \(P_{\mathcal C}\circ(T^6)^{\times3}\).

### 1.2 Eigenframe, orientation and observables

Set

\[
W(\rho,\eta)=\rho-\frac12\eta+i\frac{\sqrt3}{2}\eta,
\qquad W(Ax)=\lambda W(x),\quad\lambda=e^{i\pi/3}.
\]

Let \(w_e=W(r_e)\), \(z=W(s)\), \(d=W(c)\). Then

\[
w_1=z,\quad w_2=-z/2+d,\quad w_3=-z/2-d,\quad\sum w_e=0.
\]

Use the Genesis/RER (not the Triadic producer) signed Gram convention

\[
\begin{aligned}
Q_s&=|z|^2,\quad Q_c=|d|^2,\quad I_{sc}=\operatorname{Re}(z\bar d),\\
S:=\Omega_G&=\operatorname{Im}(z\bar d)
=\frac{\sqrt3}{2}(s_\eta c_\rho-s_\rho c_\eta),\\
Q_sQ_c&=I_{sc}^2+S^2,\\
N&:=\sum_{e=1}^3|w_e|^2=\frac32Q_s+2Q_c.
\end{aligned}
\]

Further **exact closure identities**:

\[
\sum_e|w_e|^4=\frac12N^2-2S^2,
\quad0\le S^2\le\frac{N^2}{12},
\quad N^2-12S^2=(\tfrac32Q_s-2Q_c)^2+12I_{sc}^2.
\]

\(S=\operatorname{Im}(w_1\bar w_2)=\operatorname{Im}(w_2\bar w_3)=\operatorname{Im}(w_3\bar w_1)\). For the standard counterclockwise-positive polygon from vertices \((0,w_1,w_1+w_2)\), \(S=-2A_{\rm CCW}\), i.e. **minus** twice the oriented area. For identical planar component inputs only, Triadic v1.6 uses \(B_T=2B_G\), \(Q_T=2Q_G\), \(I_T=2I_G\) and \(\Omega_T=-2\Omega_G\). This is a *normalization bridge*, not identity of producer/birth/physical dynamics.

### 1.3 Status and scope guard

**[DEF]** \(\Omega_{\rm sep}\) below is an **operator on a selected finite-time map**, entirely distinct from the signed-area observable \(\Omega_G\). Mathematical edge-slot \(S_3\) is distinct from physical oriented-node \(S_3\): changing node orientation reverses edge coordinates and can break node-\(S_3\) equivariance even when identical edge slots are permutable. The primitive DYAD even part \((0,\cosh\rho-1)\) is nonconstant. A pure edge-slot permutation does **not** establish node relabelling symmetry or physical triadic chirality selection.

### 1.4 Earlier K3 baselines retained from the discussion (not independent resonance discoveries)

**`[ALG]` [scope: selected model] Projection-reference decomposition.** Relative to the **same** isolated primitive map \(T\), the coupled-edge difference is

\[
K_e:=\mathcal N_e-T(r_e)=-\frac13\sum_{j=1}^3T(r_j).
\]

This term is **common to the three edge slots** (the slot-perpendicular component is zero) and is determined by the current triple. It is not a new force or a post-six-step repair. If one instead compares the *same coupled map* to a changed isolated reference \(h=T+A_{\rm ref}\), then \(K'_e=K_e-A_{\rm ref}(r_e)\), and its slot-perpendicular decomposition need not vanish. Thus the reference-independent object is the **fully specified coupled law**, not a "force" inferred from an arbitrarily chosen isolated baseline.

**`[ALG]` [scope: selected model] Primitive modal quadratic mixing.** From \(q_G=(0,\rho^2/2)\) and \(r_1=s\), \(r_2=-s/2+c\), \(r_3=-s/2-c\), the projected quadratic pieces are

\[
\boxed{\begin{aligned}
s^{+[2]}&=(0,\ s_\rho^2/4-c_\rho^2/3),\\
c^{+[2]}&=(0,\ -s_\rho c_\rho/2).
\end{aligned}}
\]

These are exact model algebra. They demonstrate nonlinear modal coupling in the projected rule, **not** that a separately postulated resonance field has been discovered.

**`[ALG]` [scope: oriented edge-slot symmetry] Node versus edge-slot permutations.** The one-step primitive DYAD's even part is \(T_{\mathrm{even}}(\rho,\eta)=(0,\cosh\rho-1)\), not constant. Although \(P_{\mathcal C}T^{\times3}\) is covariant under pure permutations of its **oriented edge slots**, a physical **node transposition** also reverses one or more oriented edges. The corresponding full node-\(S_3\) equivariance does not hold for this \(T\); cyclic orientation-preserving node relabelling survives in the stated convention. This is an orientation/symmetry guard, not a derivation of physical chirality.

**[DEF] Closure typing.** If \(r_{AB}=u_B-u_A\), \(r_{BC}=u_C-u_B\), \(r_{CA}=u_A-u_C\) in an admitted additive node carrier, their sum is an identity. If the three edge states are specified independently, the same equality is an additional **modelling constraint**, not automatically node ontology. Allowing independent holonomy is another model class. The identity/constraint distinction predates, and is not resolved by, the ER-2B return-jet calculations.

## 2. Separability, node–edge distinction, and finite clocks

### ER2B-C01 — `[ALG]` A common-unary separability test, not a resonance meter

For a fixed edge chart \(a,b,-a-b\) and a map \(G:\mathcal C\to\mathcal C\), define all four mixed derivatives, with 2-component outputs:

\[
\boxed{\mathfrak O_{ij}[G]=\partial_{a_i}\partial_{b_j}(G_1-G_2),\qquad i,j\in\{1,2\}.}
\]

An earlier scalar component was called \(\Omega_{\rm sep}\); \(\mathfrak O\) is used here to prevent collision with \(\Omega_G\). If \(G=P_{\mathcal C}h^{\times3}\), every \(\mathfrak O_{ij}[G]\) is identically zero. The converse for a homogeneous cubic **requires** common edge-slot equivariance, exchange antisymmetry, cyclic consistency, and a specified domain; no general converse across unrestricted maps/coordinate changes is asserted.

\(\mathfrak O\ne0\) says only that a particular finite-clock representation fails the common-unary form. It is **not** a detector of an additional force, independent resonance, curvature, extra physical degree of freedom, or node memory.

### ER2B-C02 — `[ALG]` The fixed projected class is not composition closed

\(\mathcal N=P_{\mathcal C}T^{\times3}\) has \(\mathfrak O[\mathcal N]\equiv0\) by definition. Yet \(\mathfrak O[\mathcal N^2]\not\equiv0\), even without a separately added resonant kernel. Thus the class \(\{P_{\mathcal C}h^{\times3}\}\) is **not generally closed under composition**. An affine/common-linear special case does close; neither "every nonlinear \(T\)" nor "physical resonance generated" follows.

A separate simple **continuous-flow comparator**: for scalar node phases and odd node-node coupling \(g(u)=u^3\), the node-induced edge vector field is \(\dot r_i=-3P_{\mathcal C}(r_i^3)=-3Qr_i\), where \(Q=a^2+ab+b^2\). It has

\[
r_i(t)=\frac{r_i(0)}{\sqrt{1+6tQ_0}},\qquad
\partial_a\partial_b(F_{t,1}-F_{t,2})=
\frac{27t^2(a-b)(a+2b)(2a+b)}{(1+6tQ_0)^{5/2}}.
\]

Its infinitesimal generator is common-unary projected but its finite-time map generally is not. This is an **illustrative independent model**, not a derivation of Genesis or the original Pre-Legacy effective dynamics.

### ER2B-C03 — `[ALG]` Genesis's exact leading clock ladder \(n=1,\ldots,6\)

For \(\mathfrak O_n:=\partial_{a_1}\partial_{b_1}(\mathcal N_1^n-\mathcal N_2^n)\), in real outputs \((\rho,\eta)\):

| Primitive steps \(n\) | Leading \(\mathfrak O_n\) | Map degree giving this term |
|---|---|---|
| 1 | \(0\) identically | None |
| 2 | \(-\tfrac12(a_1^2-b_1^2)(1,1)+O(3)\) | 4 |
| 3 | \((a_2-b_2)(0,-\tfrac13)+O(2)\) | 3 |
| 4 | \((a_2-b_2)(\tfrac13,-\tfrac13)+O(2)\) | 3 |
| 5 | \((a_2-b_2)(\tfrac23,\tfrac13)+O(2)\) | 3 |
| 6 | \((a_2-b_2)(\tfrac13,\tfrac23)+O(2)\) | 3 |

\(O(k)\) here refers to degree \(k\) or higher **after two derivatives**, in local edge coordinates. The **four** mixed-derivative blocks of \(n=2\)'s cubic map jet vanish. Cubic nonseparability **first appears at step three** and remains cubic through step six; only its coefficient vector changes for \(n=3\ldots6\). The two-step fourth-degree witness was independently recomputed from the full primitive 4-jet. The family was reproduced again in this package by a separate exact rational sparse-polynomial check (`repro/check_iterate_family.py`).

The generation chain is \(q_G\) in the first projection \(\to\) transport through the \(\sin\eta\) coupling in the next step \(\to\) multiplication by edge-specific linear components in the third step. This is **iterative coupling induced by the selected projection**, not a separate resonance input.

## 3. Six-step cubic return and general quadratic classification

### ER2B-C04 — `[THM]` [family: conditional projected K3] First nonlinear jet and coordinate covariance

Since the eigenvalues of \(A\) are \(e^{\pm i\pi/3}\), \(A^6=I\) and quadratic resonances are absent, the full six-step **quadratic jet vanishes for any homogeneous \(q\)** in the declared three-edge class:

\[
\boxed{\mathcal N^6(X)=X+G_3(X)+O(\|X\|^4).}
\]

**Do not generalize this to arbitrary \(A\) merely satisfying \(A^6=I\)**: \(A=I\) with nonzero \(q\) is a counterexample.

If \(H(X)=LX+O(\|X\|^2)\) is any origin-preserving local diffeomorphism, then

\[
\boxed{G_3^{H}(X)=L^{-1}G_3(LX).}
\]

This is coordinate covariance of the **first nonzero homogeneous cubic vector-valued tensor**. It does **not** make \(\mathfrak O\), which depends on an additional edge-slot split, invariant under arbitrary slot-mixing linear transformations. Both \(G_3(A_4X)=A_4G_3(X)\), \(A_4=\operatorname{diag}(A,A)\), and cyclic edge-slot covariance were checked. The quadratic normalizer and the physical incidence law must still be transported explicitly.

### ER2B-C05 — `[THM]` Direct primitive cubic \(T_3\) never contributes to the cubic separation obstruction

For arbitrary \(q:T_2\) and arbitrary homogeneous cubic \(r:T_3\), write \(N_2=P_{\mathcal C}q^{\times3}\), \(N_3=P_{\mathcal C}r^{\times3}\). The direct cubic contribution is

\[
G_3^{(3)}=\sum_{j=0}^{5}A_4^{5-j}N_3(A_4^jX)
=P_{\mathcal C}h^{\times3}(X),
\quad h(x)=\sum_{j=0}^{5}A^{5-j}r(A^jx).
\]

Therefore \(\boxed{\mathfrak O[G_3^{(3)}]\equiv0}\), **for every \(r\)**. This does *not* mean \(r\) is absent from the full \(G_3\) or from amplitude dynamics. It means the *separability obstruction* first arises exclusively from the \(q\times q\) composition sector.

Set \(m_i=\frac13\sum_kq(A^ir_k)\). Modulo separable edge terms and the common mean, the nonseparable representative for edge \(e\) is

\[
\boxed{\Theta^{(2\times2)}_e(X)=-\sum_{0\le i<j\le5}A^{5-j}Dq(A^jr_e)\big[A^{j-1-i}m_i\big].}
\]

Its complete mixed-derivative obstruction agrees with that of \(G_3\). It is **not** asserted that \(\Theta\) by itself equals the full cubic return field. The direct \(r\) and the edge-local \(q\times q\) pieces require reassembly to reconstruct \(G_3\).

The recursion documenting this split (on \(X\in\mathbb R^4\)) is

\[
\begin{aligned}
B_{j+1}&=A_4B_j+N_2(A_4^jX),\\
C_{j+1}&=A_4C_j+DN_2(A_4^jX)B_j+N_3(A_4^jX),\quad B_0=C_0=0.
\end{aligned}
\]

### ER2B-C06 — `[ALG]` Exact six-coefficient classification by two real quadrics

Let

\[
q(\rho,\eta)=(\alpha\rho^2+\beta\rho\eta+\gamma\eta^2,\ \delta\rho^2+\varepsilon\rho\eta+\zeta\eta^2).
\]

In the fixed complex eigenframe write \(q_w=u w^2+v w\bar w+t\bar w^2\), with \(u,v,t\in\mathbb C\). This is an invertible real-linear repackaging of the six coefficients. **Here** \(U,V\) denote two *obstruction coefficient functions*, not DYAD frame variables:

\[
\boxed{\begin{aligned}
U&=-12\Re(uv)+4\sqrt3\Im(uv)-2|v|^2-4|t|^2,\\
V&=-12\Re(uv)-4\sqrt3\Im(uv)+2|v|^2-8|t|^2.
\end{aligned}}
\]

The **full eight-component linear leading obstruction** \(\mathfrak O[G_3]\) is:

| Mixed derivative | Output \(\rho\) | Output \(\eta\) |
|---|---|---|
| \(\partial_{a_1}\partial_{b_1}\) | \(U(a_2-b_2)\) | \(V(a_2-b_2)\) |
| \(\partial_{a_1}\partial_{b_2}\) | \(-U(2a_1+b_1)+V(a_2+2b_2)\) | \(-U(a_2+2b_2)+V(-2a_1+a_2-b_1+2b_2)\) |
| \(\partial_{a_2}\partial_{b_1}\) | \(U(a_1+2b_1)-V(2a_2+b_2)\) | \(U(2a_2+b_2)+V(a_1-2a_2+2b_1-b_2)\) |
| \(\partial_{a_2}\partial_{b_2}\) | \(V(a_1-b_1)\) | \((V-U)(a_1-b_1)\) |

\[
\boxed{\mathfrak O[G_3]\equiv0\iff U=V=0
\iff\begin{cases}
2\Re(uv)+|t|^2=0,\\
2\sqrt3\Im(uv)-|v|^2+|t|^2=0.
\end{cases}}
\]

The criterion is **only for the cubic leading jet**, not exact higher-order separability. Examples: Genesis \(q_G=(0,\rho^2/2)\) has \((U,V)=(1/3,2/3)\); \(q=(\eta^2,\rho^2)\ne0\) has \((U,V)=(0,0)\). The nonzero locus is Zariski-open dense in the real six-coefficient space. The zero set is locally a smooth **real codimension-two / dimension-four** variety away from the origin (Jacobian rank two), singular at the origin; no *physical* moduli-space dimension is claimed.

### ER2B-C07 — `[ALG]` One complex obstruction \(\chi\) and its covariance

The two real numbers are the components of **one complex** coefficient:

\[
\boxed{\chi=\frac V2+\frac{i}{\sqrt3}(\frac V2-U)
=(-6+2i\sqrt3)uv+(1+i\sqrt3)|v|^2-4|t|^2.}
\]

Conversely \(V=2\Re\chi\), \(U=\Re\chi-\sqrt3\Im\chi\). The quadratic combinations \(uv,|v|^2,|t|^2\) are the ones appearing in \(\chi\) for this **composition**. They are **not** the complete list of all second-degree invariants of the underlying symmetry: \(|u|^2\) is also invariant, and for the discrete \(C_6\) action further invariants may exist. The absence of \(|u|^2\) is a dynamical cancellation.

For a common complex-linear frame change \(w_{\rm old}=\ell w_{\rm new}\), \(\ell\ne0\), and correctly transported edge structure,

\[
\boxed{\chi_{\rm new}=|\ell|^2\chi_{\rm old}.}
\]

Consequently \(\chi=0\) is preserved under this *restricted* chart group, and \(\arg\chi\) is stable under such positive amplitude rescaling. No coordinate-free physical coupling constant follows from this restricted covariance.

### ER2B-C08 — `[THM]` [scope: oriented edge-slot S3 only] Why only \(\nu,\chi\) remain

The antisymmetric resonant homogeneous cubic difference \(D_{12}=G_{3,1}-G_{3,2}\), with \(x=w_1\), \(y=w_2\), has basis

\[
\begin{aligned}
B_1&=x^2\bar x-y^2\bar y,\\
B_2&=x^2\bar y-y^2\bar x,\\
B_3&=xy(\bar x-\bar y).
\end{aligned}
\]

But \(x+y+z=0\) and coherent edge-output differences enforce \(D_{12}+D_{23}+D_{31}=0\). Exactly \(\sum_{cyc}B_1=0\), \(\sum_{cyc}B_2=\sum_{cyc}B_3\not\equiv0\), so \(\beta+\gamma=0\) for \(D_{12}=\nu B_1+\beta B_2+\gamma B_3\). Thus

\[
\boxed{D_{12}=\nu B_1+\chi(B_2-B_3),\quad
B_2-B_3=(w_1+w_2)(w_1\bar w_2-w_2\bar w_1).}
\]

This argument uses *identical edge-slot dynamics* and *cyclic consistency*, **not physical node-permutation equivalence**. If the admissible action does not retain these assumptions, the basis reduction need not survive.

### ER2B-C09 — `[ALG]` Exact area/chirality factor of nonseparable cubic content

Since \(w_1+w_2=-w_3\), \(w_1\bar w_2-w_2\bar w_1=2iS\),

\[
\boxed{D_{12}^{\rm nonsep}=-2i\chi w_3\Omega_G,\qquad
G_{3,e}^{\rm nonsep}=\frac{2i\chi}{3}(w_{e+1}-w_{e-1})\Omega_G.}
\]

The representative \(G^{\rm nonsep}\) is zero-sum; the full \(G_3\) additionally includes the projected separable \(\nu\) term. **Pointwise** \(\Omega_G=0\) kills this cubic nonseparable contribution, even if \(\chi\ne0\). This does **not** make the collinear locus invariant under the primitive analytic map.

Exact counterexample in the Genesis primitive model: \(s=(t,0)\), \(c=(t,0)\) gives \(S=0\) initially, but one projected primitive step produces

\[
\boxed{\Omega_G^+=\frac{\sqrt3\,t}{12}
(4e^t-5e^{t/2}+e^{-3t/2})
=\frac{5\sqrt3}{24}t^3+O(t^5).}
\]

Thus the \(\chi\Omega_G\) cubic factor is not a claim that the whole dynamical system preserves zero chirality. The area is determined by existing closed edges; it is not an independent additional state variable.

## 4. Observable response, source split and local stability

### ER2B-C10 — `[ALG]` The \(\nu,\chi\) decomposition of the complete Genesis cubic return

A compatible zero-sum representative of the full six-step cubic return is

\[
\boxed{\begin{aligned}
\delta_\nu w_e&=\nu\big(w_e|w_e|^2-\tfrac13\sum_j w_j|w_j|^2\big),\\
\delta_\chi w_e&=\tfrac{2i\chi}{3}(w_{e+1}-w_{e-1})S,
\end{aligned}}
\]

with \(G_3=\delta_\nu+\delta_\chi\). In the **named Genesis model**

\[
\boxed{\nu=\frac16-\frac{i\sqrt3}{3},\qquad \chi=\frac13.}
\]

The earlier exact four-coordinate \(G_3\) polynomials, each of their projected edge components and the full eight-entry mixed-derivative table agree with this representation. **The full four polynomials are preserved byte-for-byte as a machine-readable source snapshot** at `evidence/genesis_sixjet_obstruction_audit.json` (keys `full/G3`). Do not treat a zero obstruction as a proof of all-order common-unary representability.

### ER2B-C11 — `[ALG]` General leading \(N,S\) response

To first order in \(G_3\), the changes of the quadratic observables are **quartic** in the state. The two sources yield

\[
\boxed{\begin{aligned}
\delta_\chi S&=\frac23\Re\chi\,NS,&\delta_\chi N&=8\Re\chi\,S^2,\\
\delta_\nu S&=\frac23\Re\nu\,NS,&\delta_\nu N&=2\Re\nu\sum_e|w_e|^4.
\end{aligned}}
\]

Thus, for any \((\nu,\chi)\) of the declared homogeneous cubic class,

\[
\boxed{\Delta_4N=aN^2+(8b-4a)S^2,\quad a=\Re\nu,\ b=\Re\chi,\qquad
\Delta_4S=\tfrac23(a+b)NS.}
\]

Since \(0\le S^2/N^2\le1/12\) and both endpoints occur, \(\Delta_4N\) is **strictly positive at every nonzero closed-edge state** if and only if

\[\boxed{\Re\nu>0\quad\text{and}\quad\Re(\nu+\chi)>0.}\]

For nonzero signed area \(S\), the leading \(\Delta_4S=\tfrac23(a+b)NS\) increases \(|S|\) exactly when \(a+b>0\). Thus the second strict radial-positivity condition also governs leading chirality amplification; chirality amplification alone does not imply positive radial drift in every direction.

\(\Im\nu\), \(\Im\chi\) do not enter **these two** total observables at quartic order; they can affect individual signed-Gram components. They are not thereby declared physical rotation/frequency variables. For the isolated DYAD amplitude or return coefficient a different readout and carrier may apply.

### ER2B-C12 — `[ALG]` Complete signed-Gram observable increments in Genesis

For \(F_6=\mathcal N^6\), write \(\Delta Y=Y(F_6X)-Y(X)\). With \(N=3Q_s/2+2Q_c\) and \(S=\Omega_G\):

\[
\boxed{\begin{aligned}
\Delta Q_s&=\tfrac14Q_s^2+\tfrac13Q_sQ_c+\tfrac23S^2
-\tfrac{4\sqrt3}{9}I_{sc}S+O(\|X\|^5),\\
\Delta Q_c&=\tfrac14Q_sQ_c+\tfrac13Q_c^2+\tfrac12S^2
+\tfrac{\sqrt3}{3}I_{sc}S+O(\|X\|^5),\\
\Delta I_{sc}&=\tfrac16NI_{sc}
+\sqrt3(\tfrac16Q_s-\tfrac29Q_c)S+O(\|X\|^5),\\
\Delta S&=\tfrac13NS+O(\|X\|^5),\\
\Delta N&=\tfrac16N^2+2S^2+O(\|X\|^5).
\end{aligned}}
\]

The quartic Gram-constraint variation cancels identically. This is an **order-limited jet**, **not** closure of the full analytic signed-Gram dynamics. The separate RER C03 witness that signed Gram fails full analytic autonomous closure remains valid.

For arbitrary complex \(\chi\), the nonseparable source alone has additionally

\[
\boxed{\begin{aligned}
\delta_\chi Q_s&=\tfrac83(\Re\chi\,S^2-\Im\chi\,I_{sc}S),\\
\delta_\chi Q_c&=2\Re\chi\,S^2+2\Im\chi\,I_{sc}S,\\
\delta_\chi I_{sc}&=\Im\chi\,(Q_s-\tfrac43Q_c)S.
\end{aligned}}
\]

This makes the \(\Im\chi\) distinction precise without assuming physical spin/frequency emergence.

### ER2B-C13 — `[THM]` [family: analytic projected K3; qualitative radius only] Outward quartic return and instability

In Genesis,

\[
\boxed{\Delta_4N=\frac16N^2+2S^2,\quad\frac16N^2\le\Delta_4N\le\frac13N^2.}
\]

The analytic remainder is \(O(\|X\|^5)=O(N^{5/2})\) locally. Therefore there exists a sufficiently small, currently **uncertified numerical radius**, such that for every nonzero state inside it

\[
\boxed{N(F_6X)\ge N(X)+\frac1{12}N(X)^2.}
\]

This proves local Lyapunov instability of the origin for **this projected triad model**, in the transported positive-definite edge norm. **Evidence-strength asymmetry:** adopted DYAD v6.4.10 §6.12 [RID: DYAD-THM-PRIM-CTR] has an *explicit* certified contraction domain \(Q\le1/400\), bounds and a six-phase invariant tube (initial tube seed \(Q\le1/625\)); ER2B-C13 has only an *existence* neighborhood and no certified numerical instability radius. Neither result transfers to the other model. It does **not** prove the full inequality with \(1/6\), global runaway, physical energy production, actual triad birth, or an independently selected physical instability. For chirality, the leading \(\Delta_4S=NS/3\) tracks the sign of nonzero \(S\), but exact sign preservation close to \(S=0\) does not follow: higher-order terms may dominate there.

### ER2B-C14 — `[THM]` [conv: original additive real-edge chart] Exact isolated–triad source relationship

For the isolated six-step edge return, in the **same** complex eigenframe,

\[
T^6(w)=w+\mu w|w|^2+O(|w|^4),\quad \mu=\mu_3+\mu_{22},
\]

where the fixed-chart source split is into direct primitive \(T_3\) and quadratic composition \(T_2\times T_2\). In the projected triad, the separable coefficient satisfies

\[
\boxed{\nu=\mu_3+\frac13\mu_{22}}
\]

for **any homogeneous quadratic \(q\) and cubic \(r\)** with this \(A\), incidence, additive carrier and six-step clock. Proof: on \((x,0,-x)\), homogeneity makes \(q(-x)=q(x)\) and \(Dq(0)=0\). Every quadratic correction is \((b_j/3,-2b_j/3,b_j/3)\), with \(b_{j+1}=Ab_j+q(A^jx)\); the first-minus-second cubic correction has \(T_3(A^jx)+(1/3)Dq(A^jx)b_j\), compared with \(T_3(A^jx)+Dq(A^jx)b_j\) in the isolated edge. On this ray \(S=0\), so \(\chi\) does not contaminate the \(\nu\) extraction.

Genesis source coefficients:

| Source sector | Isolated \(\mu\) | Triad separable \(\nu\) |
|---|---|---|
| Direct \(T_3\) | \(\frac12-\frac{i\sqrt3}{6}\) | \(\frac12-\frac{i\sqrt3}{6}\) |
| Iterated \(T_2\times T_2\) | \(-1-\frac{i\sqrt3}{2}\) | \(-\frac13-\frac{i\sqrt3}{6}\) |
| Total | \(-\frac12-\frac{2i\sqrt3}{3}\) | \(\frac16-\frac{i\sqrt3}{3}\) |

In the chosen chart, the direct cubic source pushes outward and the quadratic-composition source pulls inward. The latter dominates isolated DYAD but is attenuated in the triad's separable coefficient. The precise **quartic norm responses** are

\[
\boxed{\begin{aligned}
\Delta_4N\big|_{T_3}&=\tfrac12N^2-2S^2>0\quad(N>0),\\
\Delta_4N\big|_{T_2\times T_2}&=-\tfrac13N^2+4S^2
=-\tfrac13[(\tfrac32Q_s-2Q_c)^2+12I_{sc}^2]\le0.
\end{aligned}}
\]

**Crucial distinction:** \(\chi\), which controls the nonseparable cubic term, comes solely from \(T_2\times T_2\); the outward norm drift **requires the direct \(T_3\)** to win over the negative quadratic-composition contribution. These are different model-derived phenomena and must never be called simply "the same triad effect".

## 5. The additive-carrier / representation boundary

### ER2B-C15A — `[THM]` [scope: transported conditional coupled map] Passive coordinate change preserves model dynamics

The fixed \(A\) has no quadratic resonances, so an origin-tangent-to-identity local normalizer \(H(z)=z+h_2(z)+O(|z|^3)\) eliminates the **isolated** primitive quadratic term in \(\widetilde T=H^{-1}TH\): \(\widetilde T_2=0\). The six-step isolated first nonzero coefficient \(\mu\) is preserved, but \(\widetilde\mu_{22}=0\), \(\widetilde\mu_3=\mu\). Thus the \(T_2\times T_2\) versus \(T_3\) source split is **not invariant** under nonlinear recharting.

Two distinct coupled models must be separated:

**A — passive transport of the original Genesis model.** The closure set becomes \(\mathcal C_H=\{z:\sum_eH(z_e)=0\}\), and the correctly conjugated coupled map is \(\mathcal N_H=H^{-\times3}\circ\mathcal N\circ H^{\times3}\) on \(\mathcal C_H\). The transported norm is \(N_H(z)=\sum_e|H(z_e)|^2\). This model has the **same local outward quartic return**. No extra correction/reset is inserted.

### ER2B-C15B — `[ALG]` [family: new normalized-addition projected K3] Re-imposed linear closure defines a different model

**B — new normalized-addition model.** Impose \(\sum_ez_e=0\) instead and define \(\widetilde{\mathcal N}=P_{\mathcal C}\widetilde T^{\times3}\). Here \(\widetilde T_2=0\), so the six-step return has \(\widetilde\nu=\mu\), \(\widetilde\chi=0\), and **for its newly defined** \(\widetilde N=\sum|z_e|^2\),

\[
\boxed{\Delta_4\widetilde N=-\frac12\widetilde N^2+2\widetilde S^2
\le-\frac13\widetilde N^2<0.}
\]

Thus **A and B have opposite local radial signs because they use different additive laws**, not because passive coordinate transformations reverse physical stability.

In the adopted normalizer chart,

\[
h_2(z,\bar z)=-\frac{1+i\sqrt3}{12}z^2-\frac13z\bar z+\frac{1-i\sqrt3}{24}\bar z^2.
\]

The *new linearly closed* triple \((t,t,-2t)\) has **nonzero original closure sum**

\[
\boxed{\sum_eH(z_e)=-\frac{9+3i\sqrt3}{4}t^2+O(t^3)\ne0.}
\]

The correctly transported binary addition is instead \(x\oplus_Hy=H^{-1}(H(x)+H(y))\), which is generally nonlinear but preserves the original local associative law. An additive node carrier can ground \(r_{ij}=u_j-u_i\) **only after that carrier is specified**; dyad-first modelling does not derive the affine carrier automatically.

### ER2B-C19 — `[THM]` [family: fixed DYAD local conjugacy class; arbitrary quadratic additive-carrier jet] Six-real-parameter carrier freedom

Fix the same **isolated** analytic germ \(T\) with linear part \(A\), and let \(H(z)=z+h_2(z)+O(|z|^3)\) be an origin-tangent-to-identity local coordinate change in the \(W\)-frame. For \(\widetilde T=H^{-1}TH\), the primitive quadratic term transforms exactly as

\[
\widetilde q(z)=q(z)+Ah_2(z)-h_2(Az).
\]

The quadratic homological operator \(\mathcal L_A:h_2\mapsto Ah_2-h_2\circ A\) is invertible on all real quadratic vector-valued forms because \(\lambda=e^{i\pi/3}\), \(\bar\lambda\) have **no order-2 resonances**. Consequently \(\widetilde q\) can be **any** desired six-real-coefficient quadratic map. A selected linear closure \(\sum z_e=0\) in each new chart yields a *new projected triad model* \(P_{\mathcal C}\widetilde T^{\times3}\). This is a **formal local family at quadratic order**, not a claim that all such charts are admissible physical carriers. Higher-jet terms of \(\widetilde T\) change with \(H\); the isolated six-step resonant coefficient \(\mu\) remains fixed under these tangent-to-identity conjugacies.

This explains how C06 may **also** be read as an algebraic classification over candidate additive-carrier charts for a *fixed isolated dyad conjugacy class*. It does **not** identify C06 and C15 as the same claim: C06 computes the projected obstruction for arbitrary \(q\), whereas C15 determines which model and closure are being changed. Correct passive transport of the original closure **does not** create this family of physically different signs.

### ER2B-C20 — `[ALG]` [family: Genesis normalizer interpolation \(0\le\sigma\le1\); fixed six-step strobe] Exact continuum and two different sign thresholds

To avoid conflating the interpolation \(\sigma\) with the modal coordinate \(s\), denote the chart parameter by \(\sigma\). Take \(H_\sigma(z)=z+\sigma h_2(z)+O(|z|^3)\) (e.g. the *explicit local chart* \(z+\sigma h_2(z)\)), use the **conjugated isolated** map \(\widetilde T_\sigma=H_\sigma^{-1}TH_\sigma\), and **re-impose linear closure in that chart**. Let \(k=1-\sigma\). Since \(\mathcal L_Ah_2=-q_G\),

\[
q_\sigma=kq_G,
\qquad \mu_{22}(\sigma)=k^2\mu_{22,G},
\qquad \chi(\sigma)=k^2\chi_G,
\qquad \nu(\sigma)=\mu-\tfrac23k^2\mu_{22,G}.
\]

For Genesis \(\mu=-\tfrac12-\tfrac{2i\sqrt3}{3}\), \(\mu_{22,G}=-1-\tfrac{i\sqrt3}{2}\), \(\chi_G=1/3\), hence

\[
\boxed{\Re\nu(\sigma)=-\frac12+\frac23 k^2,\quad \Re\chi(\sigma)=\frac13 k^2,\quad
\Re(\nu+\chi)=-\frac12+k^2.}
\]

For the **new chart's** \(N_\sigma=\sum_e|z_e|^2\), \(S_\sigma=\Im(z_1\bar z_2)\):

\[
\boxed{\Delta_4N_\sigma=\left(-\frac12+\frac23k^2\right)N_\sigma^2+2S_\sigma^2,\qquad
\Delta_4S_\sigma=\frac23\left(-\frac12+k^2\right)N_\sigma S_\sigma.}
\]

The exact local **quartic response** regimes along \(\sigma\in[0,1]\) are:

| Chart interpolation | Quartic norm response | Leading chirality magnitude |
|---|---|---|
| \(0\le\sigma<\sigma_{\rm out}=1-\sqrt3/2\approx0.133975\) | Strictly positive for **every** nonzero state | Amplifying when \(S\ne0\) |
| \(\sigma_{\rm out}<\sigma<\sigma_{\rm in}=1-1/\sqrt2\approx0.292893\) | **Mixed**: negative on collinear states, positive on maximum-area states | Amplifying when \(S\ne0\) |
| \(\sigma_{\rm in}<\sigma\le1\) | Strictly negative for **every** nonzero state | Attenuating when \(S\ne0\) |

At \(\sigma=\sigma_{\rm out}\) the quartic response is \(2S^2\), vanishing on collinear states; at \(\sigma=\sigma_{\rm in}\) it is nonpositive and vanishes on maximum-area states. Thus **the 13.4% threshold destroys uniform outward drift but does not yet establish uniform inward drift**. The full analytic behavior along quartic-zero directions at the threshold values requires higher terms. Uniform strict signs away from these values imply local analytic outward or inward drift in a sufficiently small but **uncertified numerical** neighborhood for each fixed \(\sigma\). The result concerns a *new family of model definitions*, not instability under a passive rechart.

For general \(q_w=uw^2+vw\bar w+t\bar w^2\), the isolated six-step quadratic-composition coefficient has the **closed form**

\[
\boxed{\mu_{22}(q)=(9+3i\sqrt3)uv-(3+3i\sqrt3)|v|^2-6|t|^2.}
\]

This formula and the existing \(\chi(q)=(-6+2i\sqrt3)uv+(1+i\sqrt3)|v|^2-4|t|^2\), together with C14, give \(\nu(q)=\mu-\tfrac23\mu_{22}(q)\) for any chart-induced \(q\) with the *same isolated* \(\mu\), provided the transformed cubic jet accompanies it. A truly arbitrary unrelated primitive \(T\) does **not** share that fixed \(\mu\).

**Scope boundary:** The only isolated *cubic return coefficient* held fixed by this tangent-to-identity quadratic-chart experiment is \(\mu\). This does **not** say that the original transported triad has no other invariants, that all physical carrier choices are admissible, or that all RTG observables are functions of \(\mu\).

### ER2B-C16 — `[OPEN]` Four-input physical/model-selection interface

| Independent selection | Question to the owning stream | Why it matters |
|---|---|---|
| Incidence | Are edges node differences, primitive relations, or another registered object? What *simultaneous* coupled map is allowed? | Defines whether/how projection and cycle-closure arise |
| Clock | Is primitive \(T\), a six-step return, a continuous flow map, or some event the comparison unit? | \(\mathfrak O_n\) and effective coefficients depend on the strobe |
| Observable | Which quadratic norm/phase/orientation readouts are admitted, and how are they transported? | Outward/inward numerical statements are readout-relative |
| **Additive carrier** | **Which affine/edge chart makes closure additive, and which changes preserve that carrier?** | Six free real quadratic-jet parameters before admissibility constraints; the Genesis \(\sigma\) slice loses uniform expansion already at \(1-\sqrt3/2\), while uniform contraction begins only after \(1-1/\sqrt2\) |

Mathematical primitive-step status in the adopted DYAD/Genesis construction does **not** establish an ontologically fundamental physical clock. No consumer may promote the projected K3 model to a selected physical process on the strength of the jet results alone.

## 6. Pre-Legacy / emergence-conditioned resonance interface (related, not solved by ER-2B)

### ER2B-C17A — `[ALG]` [family: uniform odd three-node phase field and separately postulated edge-edge field] Node/edge/clock algebra

For **uniform odd node-node** phase coupling \(\dot\phi_i=\sum_{j\ne i}g(\phi_j-\phi_i)\) and node-induced oriented edges, an exact identity is

\[
\boxed{\dot r=-3P_{\mathcal C}g^{\times3}(r).}
\]

This is a vector-field identity; it does **not** provide a primitive finite-step Genesis-type map or physical clock identification. Conversely, for a separately defined **edge-edge** field \(R_i=\sum_{j\ne i}g(r_j-r_i)\), with smooth odd \(g\), and independent edge coordinates \(p=2a+b\), \(q=b-a\),

\[
\boxed{\partial_a\partial_b(R_1-R_2)=2[D^2g(p+q)-D^2g(p)-D^2g(q)].}
\]

The derivative is a bilinear \(V\times V\to V\) object. Under suitable smoothness/connected-domain assumptions, vanishing throughout implies \(g\) is linear plus homogeneous cubic; a quintic odd term produces a nonzero obstruction. This **cannot** be transferred from edge-edge to node-node without a new modelling choice. The Pre-Legacy historical phase factor \(g(\theta)=(1+\cos\theta)\sin\theta=2\theta-\frac56\theta^3+\frac{17}{120}\theta^5+\cdots\) may be used as an illustrative scalar kernel, **not** a presently selected primitive edge law.

### ER2B-C17B — `[HEUR]` [scope: historical Pre-Legacy interpretation] Emergent variables and effective resonance are not primitive givens

Pre-Legacy v0.8 §1.1 retains the *historically constructed effective kernel*

\[
\mathcal R_{ij}=\frac34[1+\cos(\phi_i-\phi_j)](1+s_is_j)
\exp[-((\omega_i-\omega_j)/\Delta\omega^*)^2].
\]

Its own `[HEUR]` record describes three motivations, **not a unique primitive derivation**, and OFN notes that \(N_i=(\omega_i,\phi_i,s_i)\) is a relational bookkeeping device, not isolated physical node ontology. The QS variant uses **opposite** gate \((1-\sigma_i\sigma_j)/2\), not the same spin convention. These quantities must not be silently inserted as primitive DYAD or triad state variables. An effective-frequency candidate \(\nu_{\rm rel}=\eta^+-\eta=e^\rho-1-\sin\eta\) is a per-update phase increment; whether a long-run average exists, or whether it corresponds to physical frequency, is not settled. Likewise a triad orientation sign is **not** automatically a node spin.

### ER2B-C18 — `[OPEN]` Emergence-conditioned resonance is a model-selection research agenda

A generic placeholder \(\mathscr R(\mathcal S,\mathcal O,\mathcal F)\) imposes no excluded cases and is **not** a theorem. A useful scientific challenge is narrower: supply an **independently source-defined** node/edge resonance model; specify exactly which phase, frequency, polarity/spin and collective observables are *available at that level*; transport to a common carrier, primitive clock and admissible state; then test whether it contains anything not explained by the same projected single-edge evolution and its iterates. Missing observable \(\ne\) a present observable with value zero. Until that source exists, no comparison of its physical resonance to the present \(\chi\) is certified.

## 7. Local result ledger / ownership and destination

**Evidence classes:** `A` = independently implemented check also *reported by peer* in this conversation (peer scripts not included); `B` = one packaged implementation, possibly with internal tests or dependent scripts; `P` = analytic proof/definition or programme guard. Status and evidence class are separate axes. The earlier PASS counts cannot be added to claim a number of independent proofs.

| ID | Grade | Result capsule | Evidence class | Intended consumers |
|---|---|---|---|---|
| ER2B-C01 | `[ALG]` | Mixed-derivative test | P | Genesis, Pre-Legacy, RRF |
| ER2B-C02 | `[ALG]` | Composition nonclosure and flow comparator | P | Genesis, DYAD |
| ER2B-C03 | `[ALG]` | n=1…6 obstruction ladder | A | Genesis, DYAD |
| ER2B-C04 | `[THM]` | First cubic G3, covariance, quadratic cancellation | A/P | DYAD, RRF |
| ER2B-C05 | `[THM]` | Direct cubic source separable; quadratic double sum | B/P; Θ not independently peer-checked | Genesis, DYAD |
| ER2B-C06 | `[ALG]` | Eight mixed derivatives; U,V and null variety | A for sample table; B for whole symbolic identity | Genesis, Triadic |
| ER2B-C07 | `[ALG]` | Complex χ and restricted scaling | B/P | RRF, Genesis |
| ER2B-C08 | `[THM]` | Cyclic consistency reduces basis | P; spot-check reported | Genesis, Triadic |
| ER2B-C09 | `[ALG]` | Chirality bridge and collinear example | B; source example independently reported | Triadic, RER |
| ER2B-C10 | `[ALG]` | Full Genesis cubic G3 coefficients | A | Genesis, DYAD |
| ER2B-C11 | `[ALG]` | ΔN, ΔS and two positivity inequalities | A for Genesis; B for general symbolic | Genesis, Triadic |
| ER2B-C12 | `[ALG]` | Signed-Gram quartic increments | B; not peer rechecked | RER, RECOG, Triadic |
| ER2B-C13 | `[THM]` | Conditional local Lyapunov instability | A for leading jet; P for analytic existence step | Genesis, OFN |
| ER2B-C14 | `[THM]` | ν=μ3+μ22/3 and source split | A for Genesis values; P/packaged script for general identity | DYAD, Genesis |
| ER2B-C15A | `[THM]` | Passive chart conjugacy preserves dynamics | P | RRF, OFN, Genesis |
| ER2B-C15B | `[ALG]` | New normalized-addition model and sign | A for chart values; packaged script | RRF, OFN, Genesis |
| ER2B-C16 | `[OPEN]` | Four model selections incl. carrier | P | OFN, RRF, Genesis |
| ER2B-C17A | `[ALG]` | Node-node vs edge-edge identities | P / independent hand derivation | Pre-Legacy, DYAD |
| ER2B-C17B | `[HEUR]` | Emergent-feature Pre-Legacy scope | owner historical source; interpretation | Pre-Legacy, OFN |
| ER2B-C18 | `[OPEN]` | Need genuine source-defined resonance comparator | P | Pre-Legacy, OFN |
| ER2B-C19 | `[THM]` | Quadratic chart freedom over six real parameters | P; direct homological proof | OFN, DYAD, RRF, Genesis |
| ER2B-C20 | `[ALG]` | σ-family, two thresholds, closed μ22(q) | new independent symbolic recurrence + exact formulas | Genesis, OFN, DYAD |

**Provenance:** Original exact jet and archived symbolic reviewers remain preserved in the evidence subdirectories; C20's new verifier is `repro/check_carrier_continuum.py`. Reviewer-reported independent checks are labeled as such, not falsely represented as two packaged implementations. Owner decisions remain pending.

## 8. Cross-stream import contract and required non-claims

**One scope guard for all C01–C20:** this is mathematics of named projected K3 models, not physically selected coupling, physical energy, curvature, time, a post-step healing mechanism, nor an adopted stream result. Later sections inherit this guard; local negative assertions narrow only a specific risk.

| Destination stream | Proposed source import | Required guard / owner's decision |
|---|---|---|
| **DYAD** | C02–C05, C10, C14–C15B, C19–C20; isolated \(\mu\) vs triad \(\nu\) | No modification to DYAD normalizer/return theorem; compare identical eigenframe and chart; separate source split from invariant \(\mu\) |
| **Genesis Geometry** | C01–C16; conditional \(\mathcal N\) plus local instability | Keep projected K3 as selected mathematical diagnostic, **not physical birth**; no 'healing' step; additive carrier explicit |
| **Triadic** | C06–C13; \(S=\Omega_G\), \(\Omega_T=-2\Omega_G\) | Normalize before transporting; no adoption of physical chirality pumping or birth-lift dynamics; do not restore withdrawn wedge premises |
| **RRF** | C04, C07, C09, C15A–C16, C19–C20 | Register additive-carrier and edge-slot maps; passive transport vs new model; no universal tensor claim for \(\mathfrak O\) |
| **Ontology / OFN** | C15A–C20, four-choice interface | Mathematical primitive clock \(\ne\) ontological time; no unregistered physical node; affine/torsor law open |
| **Pre-Legacy** | C01–C03, C17A–C18 | Historical \((\phi,\omega,s)\) effective not primordial; specify flow-to-map strobe, node/edge distinction and selected observables |
| **RER / RECOG** | C09, C11–C12, C15A | Signed-Gram quartic closure is **not** full exact analytic closure (C03 counterexample remains); avoid quotienting common angle as automatic physical gauge |

**Recommended receiver response:** (i) confirm source hashes/model version/clock, (ii) mark each proposed item `ACCEPT SCOPED / NEED RECHECK / REJECT`, (iii) identify the precise source RID if an owner import is later adopted, (iv) make owner adoption a separate authorization. No importing stream is declared to have accepted this handoff by the existence of this document.

## 9. Evidence map and reproducibility boundary

This package contains:

- `evidence/carrier_continuum_checks.json`: newly certified two-threshold carrier family and general \(\mu_{22}(q)\), with `repro/check_carrier_continuum.py`.
- `evidence/genesis_sixjet_obstruction_audit.json`: full four cubic coordinate polynomials for \(G_3\), quadratic-only and cubic-only controls, and mixed derivatives.
- `evidence/iterate_family_checks.json`: independently regenerated exact \(n=1..6\) selected mixed-derivative family and the \(n=2\) fourth-degree witness.
- `repro/check_iterate_family.py`: original exact rational checker for the above (standalone Python standard library).
- `evidence/source_notes/`: snapshots of the five source math notes including the v1.1 scope amendment, each traceable to an original path and hash in `MANIFEST.json`.
- `evidence/original_review_archives/`: prior evidence zips; their existing scripts, logs and snapshots are not renamed or modified.
- `HANDOFF_TO_STREAMS.md`: concise stream-by-stream copyable message and adoption request.
- `CLAIM_REGISTER.json`: agent-readable summary of the local result IDs, recipient streams, status and restrictions.
- `MANIFEST.json`: SHA-256 inventory, source provenance and actually rerun checks.

**Current scoped script execution in this consolidation:** `check_genesis_sixjet_scope.py` (PASS; entire 6-step rational cubic plus internal assertions); `check_closed_form.py` (23/23); `check_orientation_and_cyclic_basis.py` (27/27); `check_observable_response.py` (24/24; imported \(G_3\)); `check_source_split.py` (17/17; special-orbit arbitrary \(q\)); `check_chart_closure_scope.py` (9/9; partial chart checks), `repro/check_iterate_family.py` (PASS; six-step-family check), and new `repro/check_carrier_continuum.py` (PASS; exact \(q_\sigma\), universal \(\mu_{22}(q)\), two thresholds and observable response). These are **separate scoped tests**, not an end-to-end physical certification. No numerical uniform radius certificate, independent primitive physical mechanism, newly rerun owner release certification, or full analytic higher-order factor theorem is included.

## 10. Exact outstanding questions and freeze recommendation

**`[OPEN]` [scope: awaiting model selection, not new jet calculations]** Which edge carrier has additive closure, what incidence/coupled map is physical, what primitive clock is admitted, and which observable/norm belongs to that model? Which emergent frequency, phase or polarity observables exist in each chosen effective layer? A genuine Pre-Legacy node-flow or edge-map comparator needs a separately named generator and time identification.

**`[OPEN]` [scope: optional mathematical refinements]** Certified finite positive neighborhood/radius of the analytic outward inequality; admissible representation-group or higher-arity transport beyond the present fixed edge class; higher-order exact separability or autonomous observable closure (not claimed by this report). These are **not prerequisites for sharing** the present scoped results.

**Freeze recommendation [HEUR]:** Accept this document as a **noncanonical, self-contained handoff candidate**, not as a new adopted Genesis/Triadic/DYAD result. Invite each owner stream to review only its named imports. The **next blocking choice is additive-carrier selection**, not another polynomial sweep. C19–C20 show that the choice is a six-real-parameter local quadratic family before admissibility restrictions, with distinct 13.4% / 29.3% radial thresholds along the Genesis normalizer interpolation.

---

### Source documents, interpreted as evidence rather than owner replacements

- `GENESIS_ER2B_SIXSTEP_AUDIT.md` and `genesis_sixjet_obstruction_audit.json` — initial full rational finite-jet reconstruction.
- `ER2B_GENERAL_QUADRATIC_REVIEW_v1/ER2B_GENERAL_Q_THEOREM.md` — six-parameter \(q\), \(U,V\), double sum and two-quadratic classification.
- `ER2B_CHIRALITY_BRIDGE_v1/ER2B_GENERAL_Q_THEOREM_v1_1_WORKING.md` — \(S\)-chirality bridge, cyclic reduction, complex \(\chi\) and codimension.
- `ER2B_OBSERVABLE_RESPONSE_v1/notes/ER2B_GENESIS_OBSERVABLE_RESPONSE.md` — \((\nu,\chi)\) observable response and exact jet-import boundary.
- `ER2B_SOURCE_SPLIT_OCT10_v1/ER2B_OBS1_SOURCE_SPLIT_ADDENDUM_v1_1_SCOPE_WORKING.md` — source-split proof, local sign, normalizer and additive-carrier scope amendment.
- `RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md`, `RTG_GENESIS_GEOMETRY_DSN_v2_8_5.md`, `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6.md`, `RTG_PRE_LEGACY_DSN_v0_8.md`, `RTG_ONTOLOGICAL_FOUNDATIONS_v0_8.md`, `RTG_RRF_REPRESENTATION_REGISTRY_v0_7.md` — existing owner/representation sources; **none amended** here.
- `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_1_DRAFT.md`, `TRIAD_COMMON_ANGLE_UPDATE_AND_ORBIT_SEPARATION.md` — **draft/research** signed-Gram and observable-closure context, not adopted physical selection.

*End of consolidated noncanonical source note.*
