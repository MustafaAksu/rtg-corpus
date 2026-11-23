---
title: "RTG — RRF Representation Registry"
version: "v0.4"
date: "25 September 2026"
class: "working artefact / representation discipline"
status: "noncanonical RRF working representation standard — candidate for PI adoption. Incorporates review v1 (ChatGPT, 25 Sep 2026: RRF03-C01/C02/C03 + editorial) and the PRR/RRF audit review v1 (third reviewer, 25 Sep 2026: degree-ten even return term, covariant comparator in raw coordinates, local single-sheet inverse). Does not replace or amend any scientific owner DSN (OFN, DYAD, RECOG, NUMGEN, Triadic Birth-Lift, Discrete Genesis); it governs which object lives in which representation, which transports are registered, and which identifications remain OPEN."
supersedes: "RTG_RRF_REPRESENTATION_REGISTRY_v0_3"
parent: "RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0_2 §20, §26"
governing methodology: "DSN_METHODOLOGY_v1.3"
---

# 0. Purpose, scope, status grammar, lock

**Purpose.** Fix, for every representation profile in current RTG dyad/network work, its native objects, transport arrows to the other profiles, observable status (native / transported / re-defined / projected), the pole-relabeling candidate action in that profile, and what each transport loses. The registry produces no new physics; it makes representation mistakes of the R11 type mechanically visible.

**Scope.** Isolated continuous dyad (four profiles) and one provisional network profile. Discrete (TDR-G) state representation is not registered (§7). All dyad statements are conditional on the postulated generator $T$ (DYAD SG-14).

**Status grammar (DSN v1.3 only).** Claim tags `[DEF]`, `[ALG]`, `[THM]`, `[NUM]`, `[HYP]`, `[OPEN]`, with `[scope: …]`, `[conv: …]`, `[import: DOC vX §…; RID: …]` (or `RID unavailable` for definition labels) and `[provenance: …]` as metadata. Provenance values used here:
- `owner-adopted` — from an adopted owner DSN;
- `participant-rechecked; third-party reproduced; Claude-check pending` — exact algebra performed by the external participant (ChatGPT) in the PRR discussion, re-derived by the same participant on 24 Sep 2026 (referee 47/47 PASS, exit 0; $S_2$ reproduced), and reproduced by a third reviewer on 25 Sep 2026 (`PRR_RRF_REVIEW_v1`, exact script, 28 checks, same $\mathbb Q(i\sqrt3)$ backend — not an independently implemented certificate); the in-session Claude re-derivation from the manifest $h_6$ table is the **review-routing stage agreed for this work**, not a Methodology v1.3 mandate (Methodology §§0.6, 12, 13 require truthful independent review and recorded adoption, and name no model). Artifact-level Claude check requires `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` / `outputs/certificate.json`, not currently mounted;
- `third-party reported; unreviewed` — a result stated in the audit review v1 with evidence archive, not yet reproduced by the participant or Claude;
- `Claude-checked` — re-derived by Claude in-session.
Historical attribution "(ext.)" appears in prose only, never as a tag.

**Representation safety lock (provisional, until OPEN-E).**

> All triad/network equations are written in profile `RRF-NET-W-RAW` with profile-typed symbols $W_e^{\rm net}$. $z_{\rm NF}$ appears in network work only inside an explicitly transported single-dyad subexpression. No closure, incidence, comparator or holonomy law is transferred between profiles without a registered transport arrow. The identification `RRF-DYAD-W → RRF-NET-W-RAW` is `[OPEN] [scope: bridge]`; notational similarity does not establish object identity.

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
f̂_form(λz) = λ f̂_form(z)                (rep: RRF-DYAD-NF; one-step formal object; formal all-order)
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
| Projected observables | $Q_{\rm true}=\rho^2-\rho\eta_{\rm wrap}+\eta_{\rm wrap}^2=\lvert W_{\rm DSN}\rvert^2$, $W_{\rm DSN}=\mathcal L(\rho,\eta_{\rm wrap})$, $\eta_{\rm wrap}=\mathrm{wrap}_{(-\pi,\pi]}(\eta)$ — **projected** from LIFT/W via the principal-angle seam `[import: DYAD v6.4.10 §1, definition Q_true; RID unavailable]` `[provenance: owner-adopted]`. Anti-correlation frame $U=\tfrac{\sqrt3}{2}\rho$, $V=\eta_{\rm wrap}-\tfrac{\rho}{2}$, $U+iV=W_{\rm DSN}e^{-i\pi/6}$ `[import: DYAD v6.4.10 §6.4 ISP (#sec-6-4-isp), anti-correlation frame; RID unavailable]` — lives on this wrapped side; it agrees with the rotated lifted frame only on a declared principal lift with $\eta=\eta_{\rm wrap}$. $Q_{\rm euclid}$ comparison-only, not registered. |
| Observable status | $m,\nu,R^\times$ **native / re-defined**; $Q_{\rm true}$, $(U,V)$ **projected**; $R^\times$ is not the transport of $\bar W_aW_b$ |
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
| Native observables | lifted differences $(\Delta\rho,\Delta\eta)$ along a trajectory; fixed points $P_1=(0,0)$ elliptic order-6, $P_2=(0,\pi)$ hyperbolic saddle (`[import: DYAD v6.4.10 §1; RID unavailable]`; $\det J=1+(e^\rho-1)\cos\eta$, non-symplectic); winding fixed points $(\log(1+2\pi k),0)$, $(\log(1+2\pi k),\pi)$ on the global cylinder `[import: RECOG v0.3.1 §6.3; RID unavailable]`. Guard: $\mathrm{Fix}_0(T)=\{P_1,P_2\}\subsetneq\{C_{\rm pole}=\pm1\}$ — a comparator value fixed under inversion is not a fixed state (e.g. $T(a,0)=(a,e^a-1)$ with $C_{\rm pole}=1$) `[import: RECOG v0.3.1 §6.3]`. |
| Observable status | $(\Delta\rho,\Delta\eta)$ **lifted realisation** of $R^\times$; not $\log R^\times$ without branch data |
| Relabeling candidate | $S_{\rm lift}=\mathcal L^{-1}S_6\mathcal L$ `[ALG] [scope: degree ≤ 6] [provenance: participant-rechecked; third-party reproduced; Claude-check pending]` — the exact `T-L` transport of $S_h$, hence the same representation-level involution as $S_6$ and $-I_{\rm NF}$ within stated scope (§4.2); **not** $(\rho,\eta)\mapsto(-\rho,-\eta)$: $T\circ S_o-S_o\circ T=(0,2(\cosh\rho-1))$, i.e. $T=T_s+T_b$, $T_b=(0,\cosh\rho-1)$ `[import: RECOG v0.3.1; RID unavailable]` |
| Exactness | dynamics exact; swap action certified through degree 6 |
| Information loss | none relative to WRAPPED; adds branch data |
| Guard | $\eta\ne\arg\zeta$ globally without a chosen lift |
| Status | `[DEF]` |

## 2.3 `RRF-DYAD-W` (lifted $\mathcal L$-frame)

| Field | Entry |
|---|---|
| Native state | $W=\mathcal L(\rho,\eta)=\rho-\tfrac{\eta}{2}+i\tfrac{\sqrt3}{2}\eta=\rho+\omega\eta$, $\omega=\tfrac{-1+i\sqrt3}{2}$; **lifted local phase, no wrapping seam** `[import: DYAD v6.4.10 §6.14, definition 𝓛; RID unavailable]` |
| Distinguish from | $W_{\rm DSN}=\mathcal L(\rho,\eta_{\rm wrap})$ of DYAD §1 — the same linear frame applied to the principal angle; registered on the wrapped side (`RRF-DYAD-WRAPPED`, projected observables), not here. $W_{\rm DSN}=W_{\rm lift}$ **iff** the chosen lift equals $\eta_{\rm wrap}$; on other deck sheets they differ even far from the seam. The anti-correlation frame $(U,V)$ is likewise a wrapped-side object. |
| Domain | lifted local |
| Native dynamics | $f=\mathcal LT\mathcal L^{-1}$ (one-step); linear part $\lambda=e^{i\pi/3}$, $\lambda^6=1$ `[import: DYAD v6.4.10 §1; OFN v0.8]`; six-step return $F_W=f^{\circ6}$ with cubic coefficient $c_{21}=\mu=-\tfrac12-i\tfrac{2\sqrt3}{3}$ `[import: DYAD v6.4.10; RID: DYAD-THM-C21]` |
| Native observables | $Q_{\rm prim}=\lvert W\rvert^2=\rho^2-\rho\eta+\eta^2$; Hermitian comparator $C_W(a,b)=\bar W_aW_b$; normalised $\widehat C=e^{i(\Theta_b-\Theta_a)}$ |
| Observable status | $Q_{\rm prim}$, $C_W$ **native** (raw bilinear forms) |
| Relabeling candidate (two symbols) | **Registered object:** the exact local map $S_h=h_6\circ(-I)\circ h_6^{-1}$ on $h_6(D)$, $D$ a sign-symmetric disk inside the certified inverse domain. **Involution exact by construction:** $S_h^2=I$ on $h_6(D)$. **Commutation finite-order only:** $\mathcal J_{\le6}(f\circ S_h-S_h\circ f)=0$ `[ALG] [scope: degree ≤ 6] [conv: DYAD-ALG-NF6 additive normalizer] [provenance: participant-rechecked; third-party reproduced; Claude-check pending]`. The truncation $S_6:=\mathcal J_{\le6}S_h$ satisfies both identities only to jet order. Leading terms: $S_h(W)=-W+s_2(W,\bar W)+O(3)$, $s_2=2h_2=-\tfrac{1+i\sqrt3}{6}W^2-\tfrac23W\bar W+\tfrac{1-i\sqrt3}{12}\bar W^2$. |
| Covariance of native observables under $S_h$ | $C_W(SW_a,SW_b)-C_W(W_a,W_b)=O(3)$, and the defect is nonzero: on real $t>0$, $C_W(S_ht,S_ht)-C_W(t,t)=\tfrac32t^3+O(t^4)$; $C_W(SW_a,W_b)=-C_W(W_a,W_b)+O(3)$ `[ALG] [scope: degree ≤ 6] [provenance: participant-rechecked; third-party reproduced; Claude-check pending]`. A comparator with exact $S_h$-covariance exists in $W$ coordinates: $C^W_{\rm cov}(a,b)=\overline{h_6^{-1}(W_a)}\,h_6^{-1}(W_b)$ — this is the NF-native $C_z$ written in raw coordinates, i.e. a **re-defined** observable, not a transport of $C_W$ (§4.1). |
| Six-step parity `[import: DYAD v6.4.10 §6.12, definition E_odd; RID unavailable]` | $F_W$ is **not** odd under $w\mapsto-w$: $\tfrac12(F_W(w)+F_W(-w))=F_4(w)+O(6)$, $F_4\ne0$; $E_{\rm odd}(w)=\tfrac12(F_W(w)-F_W(-w))-w=\mu\lvert w\rvert^2w+O(5)$. $F_4$ is the six-step counterpart of the one-step $T_b$ obstruction. Physical bridge of $E_{\rm odd}$ `[OPEN]` (owner-recorded). |
| Exactness | $\mathcal L$ exact linear bijection; $S_h$ exact involution, dynamical commutation degree-6 certified |
| Information loss | none relative to LIFT |
| Guard | $\Re W,\Im W$ are structure-adapted components, not spatial axes `[import: OFN v0.8; RID unavailable]` |
| Status | `[DEF]`; $Q_{\rm prim}=\lvert W\rvert^2$ exact |

## 2.4 `RRF-DYAD-NF`

| Field | Entry |
|---|---|
| Normalisation object | **Polynomial conjugacy only** — DYAD SG-19 operation (iii): $W=h(z,\bar z)$, $h=\mathrm{id}+h_2+\dots+h_6$, exact additive polynomial over $\mathbb Q(i\sqrt3)$, **resonant monomial coefficients of each $h_n$ set to zero** (resonance $a-b-1\equiv0\bmod 6$); table in `DYAD_RETURN_ENCLOSURE_P2B_v2/outputs/certificate.json` (`jets.h_degree6`, `jets.J_through6`) `[import: DYAD v6.4.10 §6.14; RID: DYAD-ALG-NF6] [provenance: owner-adopted]`. Operations (i) archival $\Phi_{\rm archive}$ and (ii) log-channel projection $G_{\rm proj}$ are **not** this profile. |
| Non-transferable quantities | $c_\theta^{(6)}$, $a_1$, $a_2$ `[conv: Lie strict-kernel gauge]`, projected-model coefficients, raw $c_{05}$: not properties of this chart until the R11 final-chart ledger (SG-19). Standing obstruction: $c^{({\rm raw},6)}_{05}-a_{05}=\tfrac{-13+3i\sqrt3}{576}\ne0$ `[import: DYAD v6.4.10 §6.14; RID: DYAD-ALG-NF6-OBS]` |
| Domain | inverse-coordinate domain of DYAD-THM-NF-INV: $h_6$ injective on $\lvert z\rvert\le\tfrac1{10}$ with $\lvert h_6(z)\rvert\le\tfrac{17}{16}\lvert z\rvert$, $h_6^{-1}$ exists on $\lvert W\rvert\le\tfrac9{100}$ (majorant $M(s)$, $H(s)=s+M(s)$); remainder domain of DYAD-THM-NF-REM with radius-indexed profiles $(r,C_7)=(\tfrac1{20},100)$ or $(\tfrac1{40},30)$, never mixed; **local only** |
| One-step objects (two symbols) | **Delivered:** $\widehat f_6=h_6^{-1}fh_6$, exact analytic map on its proved domain, finite jet $n$ with $\mathcal J_{\le6}(f\circ h_6-h_6\circ n)=0$. **Formal:** $\widehat f_{\rm form}=h_{\rm form}^{-1}fh_{\rm form}$, the formal Poincaré–Dulac normal form; contains only resonant monomials $z^p\bar z^q$, $p-q\equiv1\ (\mathrm{mod}\ 6)$ — hence all of odd degree. $h_6=\mathcal J_{\le6}h_{\rm form}$ under the shared convention. |
| One-step symmetry | Formal: $\widehat f_{\rm form}(\lambda z)=\lambda\widehat f_{\rm form}(z)$, hence $\widehat f_{\rm form}(-z)=-\widehat f_{\rm form}(z)$, $-1=\lambda^3$ `[ALG] [scope: formal all-order] [provenance: Claude-checked (resonance argument)]`. Delivered: only $\mathcal J_{\le6}\big(\widehat f_6(\lambda z)-\lambda\widehat f_6(z)\big)=0$ `[ALG] [scope: degree ≤ 6]`; all-order equivariance of the exact analytic $\widehat f_6$ is **not** established by the certificate. |
| Six-step object | $\widehat F=h^{-1}F_Wh$, finite jet $J(z)=z+\mu z^2\bar z+a_{32}z^3\bar z^2+a_{05}\bar z^5$; linear part identity; certified remainder $\lvert\widehat F-J\rvert\le C_7\lvert z\rvert^7$ `[import: DYAD v6.4.10 §6.14; RID: DYAD-THM-NF-REM]`. $E_{\rm NF}(z)=\widehat F(z)-z=\mu\lvert z\rvert^2z+O(5)$; its jet $J$ is odd (finite order), the formal six-step normal form is odd; **the exact $\widehat F$ (fixed finite $h_6$) is not odd**: reported first even-degree return term $[\widehat F]_{(5,5)}=-\tfrac{6113}{839808}-\tfrac{3152683\,i\sqrt3}{403107840}\ne0$ at degree ten, permitted inside the certified degree-$\ge7$ remainder `[ALG] [scope: fixed adopted h_6, Taylor through degree 10] [provenance: third-party reported; unreviewed (PRR_RRF_REVIEW_v1)]`. **$\widehat f$ and $\widehat F$ are different maps; $n$ and $J$ are different jets; neither is an all-orders identity (SG-19).** |
| Native observables | $q=\lvert z\rvert^2$; self-return multiplier $\chi_m(z)=\widehat F^{\circ m}(z)/z$, defined for $z\ne0$ and admissible iterates (extension at $0$ stated separately); NF comparator $C_z(a,b)=\bar z_az_b$ |
| Observable status | $q$, $\chi_m$, $C_z$ **native / re-defined**; $Q_{\rm prim}=\lvert h(z,\bar z)\rvert^2$ and $C_W\!\mid_{\rm NF}=\overline{h(z_a)}\,h(z_b)$ **transported** |
| Relabeling candidate | $z\mapsto-z$: exact symmetry of $\widehat f_{\rm form}$; degree-6 certified for $\widehat f_6$. $h_6$ is the unique solution of the specified homological recursion through degree 6 under the zero-resonant-coefficient convention, so $S_6=h_6(-I)h_6^{-1}$ carries no residual-gauge ambiguity at degree $\le6$ `[ALG] [scope: degree ≤ 6] [conv: DYAD-ALG-NF6]`. Canonicity under other normalizer conventions and at all formal orders `[OPEN]` `[import: RTG_RELATIONAL_RECOGNITION_DSN_v0_3_1 OPEN R11; RID: RECOG-OPEN-QUINTIC-FRAME]`. |
| Covariance under $-I$ | **Exact algebraic identities:** $q(-z)=q(z)$; $C_z(-z_a,-z_b)=C_z(z_a,z_b)$; $C_z(-z_a,z_b)=-C_z(z_a,z_b)$. **Self-return multiplier:** for the formal odd normal form the formal multiplier is sign-invariant; for the polynomial model $\chi^J_m=J^{\circ m}/z$ sign-invariance is exact but that model is a separate re-definition, not a transport of $\chi_m$; for the delivered exact $\widehat F$, exact sign-invariance of $\chi_m$ is **not established** and, per the reported degree-ten term, **fails**. Bounded statement for one return: with $R:=\widehat F-J$, $\lvert R(z)\rvert\le C_7\lvert z\rvert^7$ and $J(-z)=-J(z)$, $\chi_1(-z)-\chi_1(z)=-\tfrac{R(-z)+R(z)}{z}$, hence $\lvert\chi_1(-z)-\chi_1(z)\rvert\le2C_7\lvert z\rvert^6$ on $0<\lvert z\rvert\le r$ `[ALG] [scope: direct consequence of DYAD-THM-NF-REM, one six-step return, either (r,C_7) profile unmixed] [provenance: review v1 deduction; Claude-checked]`. No $m$-uniform iteration bound is claimed. |
| Common-realisation condition `[DEF] [scope: proposed RRF convention]` | two $z$-states may be compared by $C_z$ only if $z_a=h_6^{-1}(W_a)$, $z_b=h_6^{-1}(W_b)$ — **preimages under the same registered $h_6$** (images under $h_6^{-1}$) of states in the **same registered $W$-frame**, both inside the registered inverse domain — or an explicit certified frame transport between their charts is registered. Direction/typing only; decides nothing about physical co-realisation, birth inheritance or the network bridge. |
| Exactness | formal all-order / degree-6 certified / certified remainder |
| Information loss | none inside domain; no global content |
| Guards | $q\ne Q_{\rm prim}$ beyond leading order — they are different native observables, not two coordinate expressions of one; primitive iterates $Q_m$ and normalized iterates $q_m$ are **not identified** (DYAD §6.14); $\bar z_az_b\ne\overline{h(z_a)}h(z_b)$ in general |
| Status | `[DEF]`; chart and certificates owner-adopted (DYAD v6.4.10) |

## 2.5 `RRF-NET-W-RAW` — provisional

| Field | Entry |
|---|---|
| Native state | oriented raw edge relations $W_e^{\rm net}$ plus declared incidence/attachment structure (edge → pole-identification sites) |
| Relation to `RRF-DYAD-W` | `[OPEN] [scope: bridge]` — $W_e^{\rm net}$ is **not** identified with the isolated-dyad $W$ by this registry; the identification is part of OPEN-B/E1 |
| Domain | lifted; per-edge local |
| Native operators | incidence $D$, cycle operator $C$ (linear, exact/native in this profile) |
| Closure status | $CW^{\rm net}=0$ holds **only in the exact / node-mediated branch**; the general raw-edge profile admits $CW^{\rm net}\ne0$ (additive holonomy, §5). Closure is a branch statement, not a profile property. |
| Multiplicative edges | **not registered.** This profile carries additive complex edges $W_e^{\rm net}$; $R_e\in\mathbb C^*$ and hence $H_\times$ require a future registered multiplicative network realization and a $W_e^{\rm net}\leftrightarrow R_e$ bridge. |
| Permitted native equations | cycle sums $\sum_{e\in\gamma}\epsilon_{\gamma e}W_e^{\rm net}$; raw edge comparators $\overline{W_a^{\rm net}}W_b^{\rm net}$ for **incident** edges (relative orientation supplied by incidence) |
| Forbidden implicit substitution | $W_e^{\rm net}\mapsto z_e$ inside any of the above |
| Bookkeeping reorientation | $\mathscr O_e:\ W_e^{\rm net}\mapsto-W_e^{\rm net}$ **together with** $\epsilon_{\gamma e}\mapsto-\epsilon_{\gamma e}$; incidence-dressed quantities invariant. **This is edge-coordinate bookkeeping, not the dynamical pole-relabel candidate $S_6$; no bridge between $\mathscr O_e$ and $S_6$ is established until OPEN-B/E1.** Bare $\overline{W_a}W_b$ for non-incident edges has no gauge-invariant sign. |
| Status | `[DEF] [scope: provisional until OPEN-E; canonical network state variables (OPEN-E1) cannot be closed before OPEN-B]` |

---

# 3. Transport graph

```
RRF-DYAD-NF --T-h--> RRF-DYAD-W --T-L--> RRF-DYAD-LIFT --T-exp--> RRF-DYAD-WRAPPED
   (no native/global NF → WRAPPED arrow; local forward composite T-exp ∘ T-L ∘ T-h exists, no native global inverse)
RRF-DYAD-W  ~~[OPEN] [scope: bridge]~~  RRF-NET-W-RAW
```

| Arrow | Map | Type | Inverse | Domain | Observable transport | Constraint transport | Gauge transport | Loss |
|---|---|---|---|---|---|---|---|---|
| `T-h` | $W=h_6(z,\bar z)$ | certified local nonlinear diffeomorphism | local-certified $h_6^{-1}$ (DYAD-THM-NF-INV: $\lvert z\rvert\le\tfrac1{10}$, $\lvert W\rvert\le\tfrac9{100}$) | NF-INV / NF-REM domains | **Pullbacks, not identifications:** $h_6^*Q_{\rm prim}(z)=\lvert h_6(z)\rvert^2$ (primitive amplitude in NF coordinates); $(h_6^{-1})^*q(W)=\lvert h_6^{-1}(W)\rvert^2$ (NF amplitude in $W$ coordinates); $h_6^*C_W(a,b)=\overline{h_6(z_a)}h_6(z_b)$; $(h_6^{-1})^*C_z=C^W_{\rm cov}$. $q$, $C_z$ remain separately defined native NF observables. | single-dyad only; closure not transported | $-I\mapsto S_h$ | none in domain |
| `T-L` | $(\rho,\eta)=\mathcal L^{-1}W$ | global linear bijection | global | $\mathbb R^2$ | $Q_{\rm prim}=\rho^2-\rho\eta+\eta^2$ | linear cycle sums transported exactly | $S_h\mapsto\mathcal L^{-1}S_h\mathcal L$ | none |
| `T-exp` | $\zeta=e^{\rho+i\eta}$ | covering / quotient wrap | **none without lift** | global | $(\Delta\rho,\Delta\eta)\mapsto R^\times=e^{\Delta\rho+i\Delta\eta}$ (loses $k$) | additive cycle sums $\mapsto$ multiplicative: $\sum_\gamma(\Delta\rho_e+i\Delta\eta_e)=2\pi ik\Rightarrow H_\times=1$ (both radial and angular parts must close) | **no registered exact transport of the swap**: $S_{\rm lift}$ and $\zeta\mapsto\zeta^{-1}$ agree at linear order only; identification OPEN-A | integer winding |
| `T-net` | — | `[OPEN] [scope: bridge]` | — | — | — | — | — | — |
| composite NF → WRAPPED | $p=E\circ\mathcal L^{-1}\circ h_6$, $E(\rho,\eta)=e^{\rho+i\eta}$ | local forward composite | **local inverse on the registered image using the fixed principal lift:** $p^{-1}(\zeta)=h_6^{-1}\big(\mathcal L(\log\lvert\zeta\rvert,\operatorname{Arg}\zeta)\big)$, since on $\lvert z\rvert\le\tfrac1{10}$: $\lvert\eta\rvert\le\tfrac{2}{\sqrt3}\lvert h_6(z)\rvert<\tfrac{119}{960}<\pi$ (single principal sheet) `[ALG] [scope: consequence of DYAD-THM-NF-INV; no new radius] [provenance: review v1 deduction; Claude-checked]`; **no global inverse on arbitrary $\mathbb C^*$** | NF domain | as composed | as composed | as composed | **none on the registered single-sheet domain**; only the unrestricted global `T-exp` forgets deck-sheet data, and only when such data are part of its source |

Rule: an observable or constraint written in a destination profile without a row in this table is **untransported** and must be tagged `[OPEN] [scope: transport]`.

---

# 4. Comparator and swap matrices

## 4.1 Comparator typing

| Profile | Comparator | Type | Status |
|---|---|---|---|
| WRAPPED | $\zeta_a^{-1}\zeta_b$ | multiplicative ratio, $\mathbb C^*$-valued | native / re-defined |
| LIFT | $(\Delta\rho,\Delta\eta)$ | additive lifted difference | lifted realisation (branch-dependent) |
| W | $\bar W_aW_b$ | Hermitian bilinear form | native |
| NF | $\bar z_az_b$ | Hermitian bilinear form in NF chart | native / re-defined |
| NF coordinates of the W comparator | $h_6^*C_W=\overline{h_6(z_a)}\,h_6(z_b)$ | transported observable | transported (W → NF) |
| W coordinates of the NF comparator | $C^W_{\rm cov}=(h_6^{-1})^*C_z=\overline{h_6^{-1}(W_a)}\,h_6^{-1}(W_b)$ | transported observable; exactly $S_h$-covariant | transported (NF → W); a **re-definition** relative to $C_W$ |

$\bar z_az_b\ne\overline{h(z_a)}h(z_b)$ in general `[import: RTG_RELATIONAL_RECOGNITION_DSN_v0_3_1 OPEN R11; RID: RECOG-OPEN-QUINTIC-FRAME]`; discussion record in Wrap-up v0.2 §11.

**Covariance belongs to the pair (observable, action), not to a chart** `[HEUR → OPEN R11]`: transporting $C_W$ and $S_h$ together does not remove the covariance defect of $C_W$; $C^W_{\rm cov}$ has exact covariance in raw coordinates. R11 must decide which observables are being transported and which are being proposed as replacements; the covariant candidate algebra $(q,C_z)$ is simple, not shown to be the unique physically admissible one, and does not close OPEN-A.

**$S$-decomposition** `[ALG] [scope: RRF discussion-local] [provenance: Claude-checked]`: on a simply connected local domain where $C\ne0$ and $C\circ S\ne0$, with a consistent square-root branch (branch near $1$ inside the certified tube),
$C=C_-\,C_+$, $C_-=(C/C\circ S)^{1/2}$, $C_+=(C\cdot C\circ S)^{1/2}$; $C_-(Sx)=C_-(x)^{-1}$, $C_+(Sx)=C_+(x)$.
For multiplicative comparators whose typed relabeling law is $C(Sx)=C(x)^{-1}$, $C_+\ne1$ measures the covariance defect. $C_+$ is $S$-even and cannot decide orientation. Not canonical globally without a branch choice.

**Symmetrisation-order guard** `[import: DYAD §6.12]`: symmetrising the generator and iterating is not symmetrising the return — $[\mathrm{Odd}(f^{\circ6})]_{21}=\mu$ but $[(\mathrm{Odd}\,f)^{\circ6}]_{21}=\tfrac12-\tfrac{i\sqrt3}{6}$. A $C_\pm$ decomposition or an odd twin ($T_s$) defined at one-step level is not transferred to the six-step return without recomputation.

## 4.2 Pole-relabeling candidate actions

| Profile | Action | Status |
|---|---|---|
| WRAPPED | $\zeta\mapsto\zeta^{-1}$ | exact as ordered-ratio relabeling candidate |
| LIFT | $\mathcal L^{-1}S_h\mathcal L$ | exact involution; dynamical commutation degree-6 certified; not $(-\rho,-\eta)$ |
| W | $S_h=h_6(-I)h_6^{-1}$ (exact map on $h_6(D)$); $S_6=\mathcal J_{\le6}S_h$ (truncation) | $S_h^2=I$ exact; $\mathcal J_{\le6}(fS_h-S_hf)=0$; $h_6$ unique under `[conv: DYAD-ALG-NF6]` |
| NF | $z\mapsto-z$ | exact symmetry of $\widehat f_{\rm form}$; degree-6 certified for $\widehat f_6$ |
| NET | $\mathscr O_e$ (bookkeeping reorientation) | exact bookkeeping; **not** a pole-relabel candidate |

> **Established by registered transports:** $-I_{\rm NF}$, $S_h$ and $S_{\rm lift}$ are the same representation-level involution carried along `T-h` and `T-L` (by definition of $S_h$ and by exactness of $\mathcal L$). Involutivity is exact; commutation with the dynamics is finite-order (degree 6) or formal (for $\widehat f_{\rm form}$) — no all-order dynamical symmetry of the delivered maps is registered. **OPEN-A proper** consists of two questions only: (1) whether this involution is the physical pole relabeling; (2) whether the WRAPPED action $\zeta\mapsto\zeta^{-1}$ is the same physical operation — the two agree at linear order only and no exact transport of the involution across `T-exp` is registered. Six-step evidence: the raw return $F_W$ is not $-I$-odd ($F_4\ne0$) while the six-step jet $J$ is (DYAD §6.12).

Typed-covariance criterion for gauge status (Wrap-up §10.2): $O(Sx)=\tau_O(O(x))$ for every admissible $O$, with $\tau_O$ the type's relabeling law — not universal invariance.

---

# 5. Cycle-invariant matrix

| Invariant | Value space | Arity | Required structure | Gauge law under which invariant | Isolated certified dyad tube | Network sectors |
|---|---|---|---|---|---|---|
| $H_\times(\gamma)=\prod_{e\in\gamma}R_e$ | $\mathbb C^*$ | cycle $\ge3$ | multiplicative edge relations $R_e$ — **not native to `RRF-NET-W-RAW`**; requires a future registered multiplicative network realization | coherent vertex gauge $R_{ij}\mapsto g_i^{-1}R_{ij}g_j$, $g_i\in\mathbb C^*$ | N/A (no cycle) | node-mediated multiplicative-ratio branch: $H_\times=1$; independent multiplicative-edge branch: $H_\times\ne1$ possible |
| $H_2(\gamma)=\prod_{e\in\gamma}\sigma_e$ | $\mathbb Z_2$ | cycle $\ge3$ | pole-identification connection $\sigma_e$ | $\sigma_{ij}\mapsto g_i\sigma_{ij}g_j$, $g_i\in\mathbb Z_2$ (incidence-dressed) | N/A (no cycle; no winding needed) | not independently represented in current node-mediated attachment |
| $k$ | $\mathbb Z$ | history / path-lift; cycle when spatially closed | coherent lifted history | $\tilde\theta_i\mapsto\tilde\theta_i+2\pi n_i$ (node-coherent lift gauge) | $k=0$ `[import: NUMGEN v1.18; scope: certified local one-chart tube]` | `[OPEN]` until a discrete profile is registered |

Obstruction statements, one-way: $H_\times\ne1\Rightarrow$ no pure node-presentation reduction `[ALG] [scope: RRF discussion-local]`; $H_2=-1\Rightarrow$ present node-mediated identification scheme insufficient (pole-role identification or an added $\mathbb Z_2$ edge field required) `[ALG] [scope: RRF discussion-local]`; additive $Ca\ne0\Rightarrow$ node-potential representation insufficient `[import: NUMGEN NG-7A]`. No coupling among the three is claimed.

---

# 6. Dependency lock: OPEN-B → OPEN-E1 → OPEN-E2

- **OPEN-B** (genesis identification primitive: node identity vs pole-role identity) must be resolved before a **canonical** choice of network state variables (**OPEN-E1**).
- Provisional network work may proceed in `RRF-NET-W-RAW` with incidence data, provided any node-mediated Jacobi/mode reduction is explicitly marked as that branch.
- **OPEN-E2** (joint constrained normal form of the coupled triad) starts only after E1. The single-dyad $h$ is not the answer to E2.

---

# 7. Not registered in v0.3

- TDR-G discrete state profile (node phase/advance data; edges reconstructed from nodes) — to be registered once OPEN-B fixes whether $\sigma_e$ is added.
- A multiplicative network realization ($R_e\in\mathbb C^*$) and its bridge to $W_e^{\rm net}$ — prerequisite for $H_\times$ as a native network invariant.
- Any profile for effective geometry — no representation decision exists; deliberately last in the PRR ladder.
- Genesis inheritance fields for all profiles — pending the Genesis Identification & Inheritance Ledger (Wrap-up §14.1).
- The archival coordinate change $\Phi_{\rm archive}$ and the log-projected model $G_{\rm proj}$ (DYAD SG-19 operations (i), (ii)) — distinct objects, not representation profiles of this registry.

---

# 8. Claims this registry does NOT make

1. That any profile is the physical/primordial carrier.
2. That the representation-level involution of §4.2 is the physical pole relabeling, that it coincides with the WRAPPED action, or that $\mathscr O_e$ is a relabeling candidate at all.
3. That $H_\times$, $H_2$, $k$ couple or share a carrier.
4. That the provisional network lock or the `T-net` bridge is a result; both are conventions revisable at OPEN-B/E.
5. That items marked `participant-rechecked; Claude-check pending` have been re-derived by Claude.
6. That $E_{\rm odd}$ has a physical or consumer-accepted meaning (owner `[OPEN]`).
7. That the delivered exact maps $\widehat f_6$, $\widehat F$ possess all-order symmetries; only their finite jets and the formal normal form do — and for $\widehat F$ a nonzero even degree-ten term is reported.
8. That $\chi_m$ is exactly sign-invariant for the delivered map; only the $2C_7\lvert z\rvert^6$ one-return bound is registered.
9. That the local NF → WRAPPED composite reconstructs or discards deck-sheet data; the registered domain has none.

---

# 9. Change log

- v0.4 (25 Sep 2026): review v1 (RRF03-C01/C02/C03) and audit review v1 applied — $\chi_m$ exact-invariance claim removed and replaced by the exact/formal/polynomial-model/delivered split plus the one-return bound $2C_7\lvert z\rvert^6$; registered swap object fixed as the exact map $S_h$ (involution exact, commutation finite-order), truncation $S_6$ distinguished; `T-h` amplitude row rewritten as pullbacks $h_6^*Q_{\rm prim}$, $(h_6^{-1})^*q$; common-realisation stated as preimages under $h_6$; composite NF → WRAPPED given its local single-sheet inverse with no loss on the registered domain; $C^W_{\rm cov}$ added and "covariance belongs to (observable, action)" recorded for R11; reported degree-ten even term $[\widehat F]_{(5,5)}$ filed as third-party unreviewed; $\mathrm{Fix}_0(T)\subsetneq\{C_{\rm pole}=\pm1\}$ guard added; §1 example uses $\widehat f_{\rm form}$; live `[OPEN: transport]` respelled; anti-correlation source corrected to DYAD §6.4 ISP; definition labels moved out of RID slots with `RID unavailable`; interior import separators removed from table cells; provenance policy reworded (review-routing stage, not a Methodology mandate) and third-party reproduction recorded.

- v0.3 (24 Sep 2026): five bounded corrections from external review of v0.2 — anti-correlation frame and $W_{\rm DSN}$ moved to the wrapped side with the principal-lift condition; formal $\widehat f_{\rm form}$ / delivered $\widehat f_6$ symbols separated and all-order claims scoped to the formal object; $H_\times$ marked not native to `RRF-NET-W-RAW` pending a multiplicative realization; DSN v1.3 tag grammar normalised throughout with RID pins (RECOG-OPEN-QUINTIC-FRAME, DYAD-THM-NF-INV radii); swap table split into transport-established identity (NF ↔ W ↔ LIFT) versus OPEN-A proper (physical relabeling, WRAPPED). B3 wording fixed to degree-$\le6$ uniqueness of $h_6$. Status raised to candidate working standard.

- v0.2 DRAFT (24 Sep 2026): ten bounded corrections from external review — DSN v1.3 status grammar; source pin to ADOPTED DYAD v6.4.10; one-step $\widehat f$ / six-step $\widehat F$ separated; bookkeeping reorientation $\mathscr O_e$ separated from $S_6$; `T-net` set to `[OPEN: bridge]`, network symbols typed $W_e^{\rm net}$; closure made a branch statement; comparator transport direction fixed (W → NF); $T_{\exp}$ closure with radial part, coherent vertex gauge for $H_\times$; cycle-table scope; $C_\pm$ branch conditions. From DYAD v6.4.10 check: `RRF-DYAD-W` pinned to the lifted $\mathcal L$-frame with $Q_{\rm true}$ registered as a projected wrapped observable; SG-19 pin and non-transferable quantities; $S_6$ uniqueness under the adopted normalizer convention; $E_{\rm odd}/F_4$ six-step parity import; symmetrisation-order guard; domains pinned to DYAD-THM-NF-INV / NF-REM.
- v0.1 DRAFT (24 Sep 2026): initial registry.
