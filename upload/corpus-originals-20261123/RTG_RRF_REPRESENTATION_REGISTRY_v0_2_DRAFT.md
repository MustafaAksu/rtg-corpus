---
title: "RTG — RRF Representation Registry"
version: "v0.2 DRAFT"
date: "24 September 2026"
class: "working artefact / representation discipline"
status: "noncanonical; does not amend OFN, DYAD, RECOG, NUMGEN, Triadic Birth-Lift or Discrete Genesis. Architecture ACCEPTED (external review, 24 Sep 2026); adoption of this text pending PI decision."
supersedes: "RTG_RRF_REPRESENTATION_REGISTRY_v0_1_DRAFT"
parent: "RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0_2 §20, §26"
governing methodology: "DSN_METHODOLOGY_v1.3"
---

# 0. Purpose, scope, status grammar, lock

**Purpose.** Fix, for every representation profile in current RTG dyad/network work, its native objects, transport arrows to the other profiles, observable status (native / transported / re-defined / projected), the pole-relabeling candidate action in that profile, and what each transport loses. The registry produces no new physics; it makes representation mistakes of the R11 type mechanically visible.

**Scope.** Isolated continuous dyad (four profiles) and one provisional network profile. Discrete (TDR-G) state representation is not registered (§7). All dyad statements are conditional on the postulated generator $T$ (DYAD SG-14).

**Status grammar (DSN v1.3 only).** Claim tags `[DEF]`, `[ALG]`, `[THM]`, `[NUM]`, `[HYP]`, `[OPEN]`, with `[scope: …]`, `[conv: …]`, `[import: DOC vX §… | RID]` and `[provenance: …]` as metadata. Provenance values used here:
- `owner-adopted` — from an adopted owner DSN;
- `participant-rechecked; Claude-check pending` — exact algebra performed by the external participant in the PRR discussion and independently re-derived by the participant on 24 Sep 2026; not yet re-derived by Claude from the manifest $h_6$ table;
- `Claude-checked` — re-derived by Claude in-session.
Historical attribution "(ext.)" appears in prose only, never as a tag.

**Representation safety lock (provisional, until OPEN-E).**

> All triad/network equations are written in profile `RRF-NET-W-RAW` with profile-typed symbols $W_e^{\rm net}$. $z_{\rm NF}$ appears in network work only inside an explicitly transported single-dyad subexpression. No closure, incidence, comparator or holonomy law is transferred between profiles without a registered transport arrow. The identification `RRF-DYAD-W → RRF-NET-W-RAW` is `[OPEN: bridge]`; notational similarity does not establish object identity.

Rationale: single-dyad normalisation turns linear closure $\sum_e\epsilon_{\gamma e}W_e=0$ into $\sum_e\epsilon_{\gamma e}h(z_e)=0$, not $\sum_e\epsilon_{\gamma e}z_e=0$ (Wrap-up §19).

---

# 1. Equation annotation syntax

```
<equation>        (rep: <PROFILE-ID>; <exactness>; <domain>)
<equation>        (transport: <SRC> → <DST>; <arrow-ID>; <domain>)
```

Examples:

```
Q_prim = |W|^2                          (rep: RRF-DYAD-W; exact; lifted local)
|F̂(z) − J(z)| ≤ C_7 |z|^7               (rep: RRF-DYAD-NF; six-step; certified remainder DYAD-THM-NF-REM)
f̂(λz) = λ f̂(z)                          (rep: RRF-DYAD-NF; one-step; formal all-order)
W = h(z, z̄)                             (transport: NF → W; T-h; DYAD-THM-NF-INV domain)
```

The suffix is a pointer. Definitions, domains and remainders live in the profile/arrow entries, never in the suffix. This extends the existing `[conv:]` / `[scope:]` discipline; it is an RTG documentation convention, not a claimed universal notation.

---

# 2. Representation profiles

## 2.1 `RRF-DYAD-WRAPPED`

| Field | Entry |
|---|---|
| Native state | $\zeta=e^{\rho+i\eta}\in\mathbb C^*$, equivalently $(m,\nu)\in\mathbb R_{>0}\times U(1)$, $m=e^\rho$, $\nu=e^{i\eta}$ |
| Domain | global on $\mathbb C^*$ |
| Native dynamics | $m'=m\,e^{-s(\nu)}$, $\nu'=\nu\,e^{i[m-1-s(\nu)]}$, $s(\nu)=\frac{\nu-\nu^{-1}}{2i}$ — exact rewrite of $T$ `[ALG] [scope: RRF discussion-local] [provenance: Claude-checked]` |
| Native observables | $\lvert\zeta\rvert=m$; $\zeta/\lvert\zeta\rvert=\nu$; multiplicative ratio $R^\times_{ab}=\zeta_a^{-1}\zeta_b$ |
| Projected observable | $Q_{\rm true}=\rho^2-\rho\eta_{\rm wrap}+\eta_{\rm wrap}^2=\lvert W_{\rm DSN}\rvert^2$, $\eta_{\rm wrap}=\mathrm{wrap}_{(-\pi,\pi]}(\eta)$ — **projected** from LIFT/W via the wrap seam `[import: DYAD v6.4.10 §1 | Q_true]`. $Q_{\rm euclid}$ comparison-only, not registered. |
| Observable status | $m,\nu,R^\times$ **native / re-defined**; $Q_{\rm true}$ **projected**; $R^\times$ is not the transport of $\bar W_aW_b$ |
| Relabeling candidate | $\zeta\mapsto\zeta^{-1}$ — exact as the action induced by $R_{AB}\mapsto R_{BA}=R_{AB}^{-1}$ under ordered-ratio semantics; identification with physical pole exchange is OPEN-A |
| Exactness | exact |
| Information loss | integer lift/winding of $\eta$; branch of $\rho$-none |
| Genesis inheritance | `[OPEN]` (Ledger, Wrap-up §14.1) |
| Status | `[DEF]` |

## 2.2 `RRF-DYAD-LIFT`

| Field | Entry |
|---|---|
| Native state | $(\rho,\eta)\in\mathbb R^2$, $\eta$ unwrapped |
| Domain | global as a chart on $\mathbb R^2$; on the cylinder only with a declared lift/history |
| Native dynamics | $T:\ \rho'=\rho-\sin\eta,\ \eta'=\eta+e^\rho-1-\sin\eta$ `[import: DYAD v6.4.10 §1]` |
| Native observables | lifted differences $(\Delta\rho,\Delta\eta)$ along a trajectory; fixed points $P_1=(0,0)$ elliptic order-6, $P_2=(0,\pi)$ hyperbolic saddle (`[import: DYAD §1]`; $\det J=1+(e^\rho-1)\cos\eta$, non-symplectic); winding fixed points $(\log(1+2\pi k),0)$, $(\log(1+2\pi k),\pi)$ on the global cylinder `[import: RECOG v0.3.1]` |
| Observable status | $(\Delta\rho,\Delta\eta)$ **lifted realisation** of $R^\times$; not $\log R^\times$ without branch data |
| Relabeling candidate | $S_{\rm lift}=\mathcal L^{-1}S_6\mathcal L$ `[ALG] [scope: degree ≤ 6] [provenance: participant-rechecked; Claude-check pending]`; **not** $(\rho,\eta)\mapsto(-\rho,-\eta)$: $T\circ S_o-S_o\circ T=(0,2(\cosh\rho-1))$, i.e. $T=T_s+T_b$, $T_b=(0,\cosh\rho-1)$ `[import: RECOG v0.3.1]` |
| Exactness | dynamics exact; swap action certified through degree 6 |
| Information loss | none relative to WRAPPED; adds branch data |
| Guard | $\eta\ne\arg\zeta$ globally without a chosen lift |
| Status | `[DEF]` |

## 2.3 `RRF-DYAD-W` (lifted $\mathcal L$-frame)

| Field | Entry |
|---|---|
| Native state | $W=\mathcal L(\rho,\eta)=\rho-\tfrac{\eta}{2}+i\tfrac{\sqrt3}{2}\eta=\rho+\omega\eta$, $\omega=\tfrac{-1+i\sqrt3}{2}$; **lifted local phase, no wrapping seam** `[import: DYAD v6.4.10 §6.14 | 𝓛]` |
| Distinguish from | $W_{\rm DSN}$ of DYAD §1, built on $\eta_{\rm wrap}$ — the same linear frame applied to the wrapped angle; registered as the projected observable $Q_{\rm true}$ in `RRF-DYAD-WRAPPED`, not here. The two symbols agree only away from the wrap seam. |
| Frame rotation | anti-correlation frame $U+iV=We^{-i\pi/6}$ `[import: DYAD §6.5]` — same profile, rotated basis |
| Domain | lifted local |
| Native dynamics | $f=\mathcal LT\mathcal L^{-1}$ (one-step); linear part $\lambda=e^{i\pi/3}$, $\lambda^6=1$ `[import: DYAD §1, OFN v0.8]`; six-step return $F_W=f^{\circ6}$ with cubic coefficient $c_{21}=\mu=-\tfrac12-i\tfrac{2\sqrt3}{3}$ `[import: DYAD-THM-C21]` |
| Native observables | $Q_{\rm prim}=\lvert W\rvert^2=\rho^2-\rho\eta+\eta^2$; Hermitian comparator $C_W(a,b)=\bar W_aW_b$; normalised $\widehat C=e^{i(\Theta_b-\Theta_a)}$ |
| Observable status | $Q_{\rm prim}$, $C_W$ **native** (raw bilinear forms) |
| Relabeling candidate | $S_6=h\circ(-I)\circ h^{-1}$; $\mathcal J_{\le6}(S_6^2-I)=0$, $\mathcal J_{\le6}(f\circ S_6-S_6\circ f)=0$ `[ALG] [scope: degree ≤ 6] [conv: DYAD-ALG-NF6 additive normalizer] [provenance: participant-rechecked; Claude-check pending]`; $S_6(W)=-W+s_2(W,\bar W)+O(3)$ |
| Covariance of native observables under $S_6$ | $C_W(SW_a,SW_b)-C_W(W_a,W_b)=O(3)$; $C_W(SW_a,W_b)=-C_W(W_a,W_b)+O(3)$ `[ALG] [scope: degree ≤ 6] [provenance: participant-rechecked; Claude-check pending]` |
| Six-step parity `[import: DYAD §6.12 | E_odd]` | $F_W$ is **not** odd under $w\mapsto-w$: $\tfrac12(F_W(w)+F_W(-w))=F_4(w)+O(6)$, $F_4\ne0$; $E_{\rm odd}(w)=\tfrac12(F_W(w)-F_W(-w))-w=\mu\lvert w\rvert^2w+O(5)$. $F_4$ is the six-step counterpart of the one-step $T_b$ obstruction. Physical bridge of $E_{\rm odd}$ `[OPEN]` (owner-recorded). |
| Exactness | $\mathcal L$ exact linear bijection; swap action degree-6 certified |
| Information loss | none relative to LIFT |
| Guard | $\Re W,\Im W$ are structure-adapted components, not spatial axes `[import: OFN v0.8]` |
| Status | `[DEF]`; $Q_{\rm prim}=\lvert W\rvert^2$ exact |

## 2.4 `RRF-DYAD-NF`

| Field | Entry |
|---|---|
| Normalisation object | **Polynomial conjugacy only** — DYAD SG-19 operation (iii): $W=h(z,\bar z)$, $h=\mathrm{id}+h_2+\dots+h_6$, exact additive polynomial over $\mathbb Q(i\sqrt3)$, **resonant monomial coefficients of each $h_n$ set to zero** (resonance $a-b-1\equiv0\bmod 6$); table in `DYAD_RETURN_ENCLOSURE_P2B_v2/outputs/certificate.json` (`jets.h_degree6`, `jets.J_through6`) `[import: DYAD v6.4.10 §6.14 | DYAD-ALG-NF6, owner-adopted]`. Operations (i) archival $\Phi_{\rm archive}$ and (ii) log-channel projection $G_{\rm proj}$ are **not** this profile. |
| Non-transferable quantities | $c_\theta^{(6)}$, $a_1$, $a_2$ `[conv: Lie strict-kernel gauge]`, projected-model coefficients, raw $c_{05}$: not properties of this chart until the R11 final-chart ledger (SG-19). Standing obstruction: $c^{({\rm raw},6)}_{05}-a_{05}=\tfrac{-13+3i\sqrt3}{576}\ne0$ `[import: DYAD-ALG-NF6-OBS]` |
| Domain | inverse-coordinate domain of DYAD-THM-NF-INV (majorant $M(s)$, $H(s)=s+M(s)$) and remainder domain of DYAD-THM-NF-REM; **local only** |
| One-step object | $\widehat f=h^{-1}fh$, finite jet $n$ with $\mathcal J_{\le6}(f\circ h-h\circ n)=0$; linear part $\lambda$; formal normal form contains only resonant monomials $z^p\bar z^q$, $p-q\equiv1\ (\mathrm{mod}\ 6)$ — hence all of odd degree |
| One-step symmetry | $\widehat f(\lambda z)=\lambda\widehat f(z)$ (formal all-order $\mathbb Z_6$ equivariance); therefore $\widehat f(-z)=-\widehat f(z)$, $-1=\lambda^3$ `[ALG] [scope: formal normal form; delivered chart certified to degree 6] [provenance: Claude-checked (resonance argument)]` |
| Six-step object | $\widehat F=h^{-1}F_Wh$, finite jet $J(z)=z+\mu z^2\bar z+a_{32}z^3\bar z^2+a_{05}\bar z^5$; linear part identity; certified remainder $\lvert\widehat F-J\rvert\le C_7\lvert z\rvert^7$ `[import: DYAD-THM-NF-REM]`. $E_{\rm NF}(z)=\widehat F(z)-z=\mu\lvert z\rvert^2z+O(5)$ is odd. **$\widehat f$ and $\widehat F$ are different maps; $n$ and $J$ are different jets; neither is an all-orders identity (SG-19).** |
| Native observables | $q=\lvert z\rvert^2$; self-return multiplier $\chi_m(z)=\widehat F^m(z)/z$; NF comparator $C_z(a,b)=\bar z_az_b$ |
| Observable status | $q$, $\chi_m$, $C_z$ **native / re-defined**; $Q_{\rm prim}=\lvert h(z,\bar z)\rvert^2$ and $C_W\!\mid_{\rm NF}=\overline{h(z_a)}\,h(z_b)$ **transported** |
| Relabeling candidate | $z\mapsto-z$: exact symmetry of the formal normal form; degree-6 certified in the delivered analytic chart; **unique under the adopted normalizer convention** (resonant coefficients of $h_n$ zero), so $S_6$ carries no residual-gauge ambiguity at certified order `[ALG] [conv: DYAD-ALG-NF6]`. Formal all-order canonicity under other normalizer conventions `[OPEN]` (RECOG quintic residual-gauge caveat). |
| Covariance under $-I$ | $q$, $\chi_m$ invariant (exact); $C_z(-z_a,-z_b)=C_z$, $C_z(-z_a,z_b)=-C_z$ (exact) |
| Common-realisation condition `[DEF, proposed]` | two $z$-states may be compared by $C_z$ only if they are images under the **same registered $h$** of states in the **same registered $W$-frame**, or an explicit certified frame transport between their charts is registered |
| Exactness | formal all-order / degree-6 certified / certified remainder |
| Information loss | none inside domain; no global content |
| Guards | $q\ne Q_{\rm prim}$ beyond leading order; primitive iterates $Q_m$ and normalized iterates $q_m$ are **not identified** (DYAD §6.14); $\bar z_az_b\ne\overline{h(z_a)}h(z_b)$ in general |
| Status | `[DEF]`; chart and certificates owner-adopted (DYAD v6.4.10) |

## 2.5 `RRF-NET-W-RAW` — provisional

| Field | Entry |
|---|---|
| Native state | oriented raw edge relations $W_e^{\rm net}$ plus declared incidence/attachment structure (edge → pole-identification sites) |
| Relation to `RRF-DYAD-W` | `[OPEN: bridge]` — $W_e^{\rm net}$ is **not** identified with the isolated-dyad $W$ by this registry; the identification is part of OPEN-B/E1 |
| Domain | lifted; per-edge local |
| Native operators | incidence $D$, cycle operator $C$ (linear, exact/native in this profile) |
| Closure status | $CW^{\rm net}=0$ holds **only in the exact / node-mediated branch**; the general raw-edge profile admits $CW^{\rm net}\ne0$ (holonomy, §5). Closure is a branch statement, not a profile property. |
| Permitted native equations | cycle sums $\sum_{e\in\gamma}\epsilon_{\gamma e}W_e^{\rm net}$; raw edge comparators $\overline{W_a^{\rm net}}W_b^{\rm net}$ for **incident** edges (relative orientation supplied by incidence) |
| Forbidden implicit substitution | $W_e^{\rm net}\mapsto z_e$ inside any of the above |
| Bookkeeping reorientation | $\mathscr O_e:\ W_e^{\rm net}\mapsto-W_e^{\rm net}$ **together with** $\epsilon_{\gamma e}\mapsto-\epsilon_{\gamma e}$; incidence-dressed quantities invariant. **This is edge-coordinate bookkeeping, not the dynamical pole-relabel candidate $S_6$; no bridge between $\mathscr O_e$ and $S_6$ is established until OPEN-B/E1.** Bare $\overline{W_a}W_b$ for non-incident edges has no gauge-invariant sign. |
| Status | `[DEF] [scope: provisional until OPEN-E; canonical network state variables (OPEN-E1) cannot be closed before OPEN-B]` |

---

# 3. Transport graph

```
RRF-DYAD-NF --T-h--> RRF-DYAD-W --T-L--> RRF-DYAD-LIFT --T-exp--> RRF-DYAD-WRAPPED
   (no native/global NF → WRAPPED arrow; local forward composite T-exp ∘ T-L ∘ T-h exists, no native global inverse)
RRF-DYAD-W  ~~[OPEN: bridge]~~  RRF-NET-W-RAW
```

| Arrow | Map | Type | Inverse | Domain | Observable transport | Constraint transport | Gauge transport | Loss |
|---|---|---|---|---|---|---|---|---|
| `T-h` | $W=h(z,\bar z)$ | certified local nonlinear diffeomorphism | local-certified $h^{-1}$ (DYAD-THM-NF-INV) | NF-INV / NF-REM domains | $q\to Q_{\rm prim}=\lvert h\rvert^2$; **$C_W$ in NF coordinates is $\overline{h(z_a)}h(z_b)$** (direction W → NF); $C_z$ is a separate re-defined comparator, not a transport | single-dyad only; closure not transported | $-I\mapsto S_6$ | none in domain |
| `T-L` | $(\rho,\eta)=\mathcal L^{-1}W$ | global linear bijection | global | $\mathbb R^2$ | $Q_{\rm prim}=\rho^2-\rho\eta+\eta^2$ | linear cycle sums transported exactly | $S_6\mapsto\mathcal L^{-1}S_6\mathcal L$ | none |
| `T-exp` | $\zeta=e^{\rho+i\eta}$ | covering / quotient wrap | **none without lift** | global | $(\Delta\rho,\Delta\eta)\mapsto R^\times=e^{\Delta\rho+i\Delta\eta}$ (loses $k$) | additive cycle sums $\mapsto$ multiplicative: $\sum_\gamma(\Delta\rho_e+i\Delta\eta_e)=2\pi ik\Rightarrow H_\times=1$ (both radial and angular parts must close) | **no registered exact transport of the swap**: $S_{\rm lift}$ and $\zeta\mapsto\zeta^{-1}$ agree at linear order only; identification OPEN-A | integer winding |
| `T-net` | — | `[OPEN: bridge]` | — | — | — | — | — | — |
| composite NF → WRAPPED | $\exp\circ\mathcal L^{-1}\circ h$ | local forward composite | no native global inverse | NF domain | as composed | as composed | as composed | winding |

Rule: an observable or constraint written in a destination profile without a row in this table is **untransported** and must be tagged `[OPEN: transport]`.

---

# 4. Comparator and swap matrices

## 4.1 Comparator typing

| Profile | Comparator | Type | Status |
|---|---|---|---|
| WRAPPED | $\zeta_a^{-1}\zeta_b$ | multiplicative ratio, $\mathbb C^*$-valued | native / re-defined |
| LIFT | $(\Delta\rho,\Delta\eta)$ | additive lifted difference | lifted realisation (branch-dependent) |
| W | $\bar W_aW_b$ | Hermitian bilinear form | native |
| NF | $\bar z_az_b$ | Hermitian bilinear form in NF chart | native / re-defined |
| NF coordinates of the W comparator | $\overline{h(z_a)}\,h(z_b)$ | transported observable | transported (W → NF) |

$\bar z_az_b\ne\overline{h(z_a)}h(z_b)$ in general `[import: RECOG raw/post-$H_2$ guard; Wrap-up §11]`.

**$S$-decomposition** `[ALG] [scope: RRF discussion-local]`: on a simply connected local domain where $C\ne0$ and $C\circ S\ne0$, with a consistent square-root branch (branch near $1$ inside the certified tube),
$C=C_-\,C_+$, $C_-=(C/C\circ S)^{1/2}$, $C_+=(C\cdot C\circ S)^{1/2}$; $C_-(Sx)=C_-(x)^{-1}$, $C_+(Sx)=C_+(x)$.
For multiplicative comparators whose typed relabeling law is $C(Sx)=C(x)^{-1}$, $C_+\ne1$ measures the covariance defect. $C_+$ is $S$-even and cannot decide orientation. Not canonical globally without a branch choice.

**Symmetrisation-order guard** `[import: DYAD §6.12]`: symmetrising the generator and iterating is not symmetrising the return — $[\mathrm{Odd}(f^{\circ6})]_{21}=\mu$ but $[(\mathrm{Odd}\,f)^{\circ6}]_{21}=\tfrac12-\tfrac{i\sqrt3}{6}$. A $C_\pm$ decomposition or an odd twin ($T_s$) defined at one-step level is not transferred to the six-step return without recomputation.

## 4.2 Pole-relabeling candidate actions

| Profile | Action | Status |
|---|---|---|
| WRAPPED | $\zeta\mapsto\zeta^{-1}$ | exact as ordered-ratio relabeling candidate |
| LIFT | $\mathcal L^{-1}S_6\mathcal L$ | degree-6 certified; not $(-\rho,-\eta)$ |
| W | $S_6=h(-I)h^{-1}$ | degree-6 certified; unique under `[conv: DYAD-ALG-NF6]` |
| NF | $z\mapsto-z$ | formal all-order symmetry of $\widehat f$; delivered chart certified to degree 6 |
| NET | $\mathscr O_e$ (bookkeeping reorientation) | exact bookkeeping; **not** a pole-relabel candidate |

> The first four actions are representation-level candidates for the same physical pole exchange. Their mutual identification, and identification with physical relabeling, is **OPEN-A**. $\zeta\mapsto\zeta^{-1}$ and $z\mapsto-z$ agree at linear order only. Six-step evidence: the raw return $F_W$ is not $-I$-odd ($F_4\ne0$), the NF return is (DYAD §6.12).

Typed-covariance criterion for gauge status (Wrap-up §10.2): $O(Sx)=\tau_O(O(x))$ for every admissible $O$, with $\tau_O$ the type's relabeling law — not universal invariance.

---

# 5. Cycle-invariant matrix

| Invariant | Value space | Arity | Required structure | Gauge law under which invariant | Isolated certified dyad tube | Network sectors |
|---|---|---|---|---|---|---|
| $H_\times(\gamma)=\prod_{e\in\gamma}R_e$ | $\mathbb C^*$ | cycle $\ge3$ | multiplicative edge relations | coherent vertex gauge $R_{ij}\mapsto g_i^{-1}R_{ij}g_j$, $g_i\in\mathbb C^*$ | N/A (no cycle) | node-mediated branch: $H_\times=1$ built in; general raw-edge branch: may be $\ne1$ |
| $H_2(\gamma)=\prod_{e\in\gamma}\sigma_e$ | $\mathbb Z_2$ | cycle $\ge3$ | pole-identification connection $\sigma_e$ | $\sigma_{ij}\mapsto g_i\sigma_{ij}g_j$, $g_i\in\mathbb Z_2$ (incidence-dressed) | N/A (no cycle; no winding needed) | not independently represented in current node-mediated attachment |
| $k$ | $\mathbb Z$ | history / path-lift; cycle when spatially closed | coherent lifted history | $\tilde\theta_i\mapsto\tilde\theta_i+2\pi n_i$ (node-coherent lift gauge) | $k=0$ `[import: NUMGEN v1.18; scope: certified local one-chart tube]` | `[OPEN]` until a discrete profile is registered |

Obstruction statements, one-way: $H_\times\ne1\Rightarrow$ no pure node-presentation reduction `[ALG, discussion-local]`; $H_2=-1\Rightarrow$ present node-mediated identification scheme insufficient (pole-role identification or an added $\mathbb Z_2$ edge field required) `[ALG, discussion-local]`; additive $Ca\ne0\Rightarrow$ node-potential representation insufficient `[import: NUMGEN NG-7A]`. No coupling among the three is claimed.

---

# 6. Dependency lock: OPEN-B → OPEN-E1 → OPEN-E2

- **OPEN-B** (genesis identification primitive: node identity vs pole-role identity) must be resolved before a **canonical** choice of network state variables (**OPEN-E1**).
- Provisional network work may proceed in `RRF-NET-W-RAW` with incidence data, provided any node-mediated Jacobi/mode reduction is explicitly marked as that branch.
- **OPEN-E2** (joint constrained normal form of the coupled triad) starts only after E1. The single-dyad $h$ is not the answer to E2.

---

# 7. Not registered in v0.2

- TDR-G discrete state profile (node phase/advance data; edges reconstructed from nodes) — to be registered once OPEN-B fixes whether $\sigma_e$ is added.
- Any profile for effective geometry — no representation decision exists; deliberately last in the PRR ladder.
- Genesis inheritance fields for all profiles — pending the Genesis Identification & Inheritance Ledger (Wrap-up §14.1).
- The archival coordinate change $\Phi_{\rm archive}$ and the log-projected model $G_{\rm proj}$ (DYAD SG-19 operations (i), (ii)) — distinct objects, not representation profiles of this registry.

---

# 8. Claims this registry does NOT make

1. That any profile is the physical/primordial carrier.
2. That the relabeling candidates in §4.2 are the same physical operation, or that $\mathscr O_e$ is one of them.
3. That $H_\times$, $H_2$, $k$ couple or share a carrier.
4. That the provisional network lock or the `T-net` bridge is a result; both are conventions revisable at OPEN-B/E.
5. That items marked `participant-rechecked; Claude-check pending` have been re-derived by Claude.
6. That $E_{\rm odd}$ has a physical or consumer-accepted meaning (owner `[OPEN]`).

---

# 9. Change log

- v0.2 DRAFT (24 Sep 2026): ten bounded corrections from external review — DSN v1.3 status grammar; source pin to ADOPTED DYAD v6.4.10; one-step $\widehat f$ / six-step $\widehat F$ separated; bookkeeping reorientation $\mathscr O_e$ separated from $S_6$; `T-net` set to `[OPEN: bridge]`, network symbols typed $W_e^{\rm net}$; closure made a branch statement; comparator transport direction fixed (W → NF); $T_{\exp}$ closure with radial part, coherent vertex gauge for $H_\times$; cycle-table scope; $C_\pm$ branch conditions. From DYAD v6.4.10 check: `RRF-DYAD-W` pinned to the lifted $\mathcal L$-frame with $Q_{\rm true}$ registered as a projected wrapped observable; SG-19 pin and non-transferable quantities; $S_6$ uniqueness under the adopted normalizer convention; $E_{\rm odd}/F_4$ six-step parity import; symmetrisation-order guard; domains pinned to DYAD-THM-NF-INV / NF-REM.
- v0.1 DRAFT (24 Sep 2026): initial registry.
