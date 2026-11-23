---
title: "RTG — RRF Representation Registry"
version: "v0.8.1"
date: "16 October 2026"
class: "working artefact / representation discipline"
status: "REVIEW CANDIDATE — v0.8.1 editorial/provenance correction only; NOT ADOPTED. Adopted v0.8 remains governing working standard pending explicit approval."
supersedes: "RTG_RRF_REPRESENTATION_REGISTRY_v0_8.md — ADOPTED 14 October 2026; SHA-256 c4ec1f10da0cdf3b95a84b3013909e04db49212e0119b858c170e5fd8f42b44a"
review candidate supersedes if adopted: "RTG_RRF_REPRESENTATION_REGISTRY_v0_8.md — adopted 14 October 2026; SHA-256 c4ec1f10da0cdf3b95a84b3013909e04db49212e0119b858c170e5fd8f42b44a"
review candidate scope: "RID-first owner provenance, RER proposal extraction, OFN rank typing, reported formal-G1 pointer, node-vs-slot exchange and regularity/clock open decisions; no physics adoption"
revision base: "RTG_RRF_REPRESENTATION_REGISTRY_v0_8.md (adopted); the authenticated v0.7 predecessor and its v0.6 history remain unchanged"
predecessor source draft: "RTG_RRF_REPRESENTATION_REGISTRY_v0_7_DRAFT.md; preserved unchanged"
predecessor adoption record: "RTG_RRF_REPRESENTATION_REGISTRY_v0_7_ADOPTION_RECORD.md"
predecessor revision editor: "ChatGPT; 5 October 2026 scoped v0.7 finalization, unchanged history"
revision editor: "ChatGPT; candidate v0.8.1 provenance/representation corrections (16 October 2026); v0.8 release editor remains in historical log"
adoption: "PENDING for v0.8.1; v0.8 adoption remains recorded in RTG_RRF_REPRESENTATION_REGISTRY_v0_8_ADOPTION_RECORD.md"
parent: "RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0_2 §20, §26"
governing methodology: "DSN_METHODOLOGY_v1.3"
---

# 0. Purpose, scope, status grammar, lock

**Purpose.** Fix, for every representation profile in current RTG dyad/network work, its native objects, transport arrows to the other profiles, observable status (native / transported / re-defined / projected), the pole-relabeling candidate action in that profile, and what each transport loses. The registry produces no new physics; it makes representation mistakes of the R11 type mechanically visible.

**Theorem-source policy.** The registry records track, domain, typing and transport conditions; it does not maintain an independent authoritative theorem ledger. Any formula excerpt, including §4.1a, is imported for orientation, not restated authoritatively: the cited scientific owner governs. Such an excerpt is not a precedent for transferring theorem ownership to RRF.

**Scope.** Isolated continuous dyad (four profiles) and one provisional network profile. Discrete (TDR-G) state representation is not registered (§7). All dyad statements are conditional on the postulated generator $T$ (DYAD SG-14).

**Status grammar (DSN v1.3).** Claim tags `[DEF]`, `[ALG]`, `[THM]`, `[NUM]`, `[HYP]`, `[OPEN]`; `[scope: …]`, `[conv: …]`, `[import: DOC vX §…; RID: …]` and `[provenance: …]` are qualifiers. `RID unavailable` identifies a source block without inventing a result identifier. An artifact RID identifies evidence, not a replacement theorem RID. Imported owner claim status, the extent of source inspection/reproduction, and RRF adoption are separate axes.

**Provenance vocabulary and this update.**
- `owner-adopted`: retained for adopted DYAD v6.4.10 results. This source-provenance label does not itself establish RRF adoption or certify later downstream interpretations; the registry adoption decision is recorded separately.
- `Claude-checked as recorded by RECOG`: a written owner-ledger record attributes an independent reconstruction to Claude. For the covered swap identities, the source is RECOG v0.3.14 §6.14, certificate check 9, `RECOG-ART-R11-LEDGER`. This update reads that source; it does **not** rerun its script or authenticate an absent executable against its printed hash.
- `algebraic consequence of imported definitions/results`: e.g. a general two-input cubic expansion derived from the registered $s_2=2h_2$. It is not silently described as an additional case independently executed by the source's check 9.
- `Claude-checked (written verification record); prior report confirmed`: the separate degree-ten record already carried in VF-1. Its evidence is not upgraded by importing RECOG's degree-six check.
- `Claude-checked`: retained for earlier discussion-local derivations expressly attributed that way; no new execution is asserted here.
- Historical labels `participant-rechecked; third-party reproduced; Claude-check pending`, `(ext.)`, and `third-party reported; unreviewed` describe the earlier evidence state. The covered swap-commutator and real-ray comparator records no longer await that review, because RECOG records it. Any other claim needs its own matching evidence; this is not a blanket removal of provenance obligations.

**Source-synchronization reading/reproduction boundary (preserved draft-stage record).** The supplied RECOG v0.3.14 and NUMGEN v1.20.7 were read in full; the entire registry v0.6 was reviewed. Existing scientific owner files were checked at the affected interfaces and against recorded hashes. No numerical or symbolic certificate, simulator, or archived gate was executed in this synchronization. Source-reported PASS counts remain source reports. Exact source identities and missing artifacts are recorded in §10. Historical attribution is prose, not a truth grade.

**Finalization boundary (5 October 2026).** The reviewer-supported candidate is adopted here only as the RRF working representation standard. Finalization implements the three accepted editorial notes and consistent release-state metadata; no scientific statement, formula, domain or imported proof status is changed. This step performs source/status spot-checks and mechanical identity/diff checks, not another full scientific-source review or certificate rerun. The separate adoption record lists the reviewer correction, unchanged OPENs and deferred consumer synchronization.

**Representation safety lock (provisional, until OPEN-E).**

> All triad/network equations are written in profile `RRF-NET-W-RAW` with profile-typed symbols $W_e^{\rm net}$. $z_{\rm NF}$ appears in network work only inside an explicitly transported single-dyad subexpression. No closure, incidence, comparator or holonomy law is transferred between profiles without a registered transport arrow. The identification `RRF-DYAD-W → RRF-NET-W-RAW` is `[OPEN] [scope: bridge]`; notational similarity does not establish object identity.

Rationale: single-dyad normalisation turns linear closure $\sum_e\epsilon_{\gamma e}W_e=0$ into $\sum_e\epsilon_{\gamma e}h(z_e)=0$, not $\sum_e\epsilon_{\gamma e}z_e=0$ (Wrap-up §19).

### 0.1 Source-state receipt and dependency boundary

| Owner record inspected | State used by this registry | Boundary |
|---|---|---|
| RECOG v0.3.14 §6.14 / §2 R11 | R11 is CLOSED as the typed final-chart ledger; DYAD enclosure inputs accepted | Physical pole relabeling remains RRF OPEN-A. The standing non-transfer/refusal line is not removed by R11 closure. |
| RECOG v0.3.14 §6.13a | R9 exact-map retained memory and comparator-incompleteness corollary are theorem-grade on the declared $C_z$ track and amplitude windows | Not a theorem for every comparator track, every amplitude, event selection, or birth inheritance. |
| RECOG v0.3.14 §6.16a–f | Representation-safe token transport and separate classifications of transition, retention, and write-through | Definitions of tokens/carriers do not identify them with birth events. No new history carrier is created by registering them. |
| NUMGEN v1.20.7 §6.6 | M2-1 transported chain identity adopted at algebra grade; Census-1 INCONCLUSIVE / INCONCLUSIVE; interface-typed WD-DOM still OPEN | A context transport does not create co-realization, outer admissibility, or an admitted composable chain. |

**No circular scientific import.** RECOG imports the RRF's notation and convention only; its §6.14 finite algebra is independently reconstructed from the specified generator and adopted DYAD chart. This registry cites that algebraic evidence, not its own earlier convention as a proof. RECOG's internal RRF v0.4 pointers have not been edited here. NUMGEN's RRF v0.6 pointer is likewise explicitly noncanonical and imports no theorem. The source status of RECOG v0.3.14 is not promoted to an unrecorded owner/PI freeze decision by this receipt.

---

### 0.2 Current source receipts and inheritance/representation boundary — adopted v0.8, with v0.8.1 review overlay

These rows supplement rather than rewrite the preserved dated v0.7 receipts in §0.1 and §10. In this **v0.8.1 REVIEW CANDIDATE**, additions are proposal/provenance guards only; adopted v0.8 remains governing until a separate adoption record is authorized. The source of the baseline is the **exact authenticated 57,524-byte adopted v0.7**, not its preceding draft. Scientific-owner proof grade, work-local adoption and certificate replay remain separate.

| Current source | Verified source location / status | RRF import boundary |
|---|---|---|
| OFN v0.9 (ADOPTED) | Complete-state/presentation covariance; RF-O09-03/04; §4.5 and OPEN-OPA; OPEN-PRIMACY-3B/3C | No universal node-coincidence axiom, carrier selection or physical clock derived |
| RECOG v0.3.20 (freeze candidate, not auto-adopted) | §6.6a `RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY`; §6.16b `RECOG-ALG-BTOKEN-TRANSPORT`; §6.16g `RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS` | Family conjugacy ≠ physical relabeling; section transport ≠ new event rule; CELL-F4 W1–W5 are prerequisites, not a birth law |
| Genesis Geometry v2.8.5 (ADOPTED) / Triadic v1.6 (ADOPTED) | Genesis's child direction/amplitude, apex/UV and source lowering corrections; Triadic §6.15/SG-15 | No physical source/child functional/transverse dimension is selected by these notices |
| ER-2B consolidated v0.2 (noncanonical) and RRF coincidence v0.2 (noncanonical) | Specified projected three-edge map; analytic conditional noninvariance at primitive and six-step clocks | A physical exclusion requires complete-state exchange, actual fixed-state realization, encoding and clock intertwining (§6.2) |
| Communicated RER v0.2 **update plan only** | Proposed closure taxonomy, factor and N=7/8 Stage-2 status; moved into separate noncanonical proposal | Original RER v0.2 and newest Stage-2 certificate unavailable; no theorem/profile/standard adopted (§6.4) |

### 0.3 Model/carrier versus passive-chart safety rule

`[DEF] [scope: RRF representation discipline; conditional ER-2B illustration]` A **passive** diffeomorphic recharting transports the state, update, exchange action, incidence/closure operator, event predicate and comparison subset together. It retains the same model, so correctly transported fixed-set noninvariance cannot disappear. **Reimposing** linear addition, projection or incidence in the new coordinates creates a *different conditional model* unless an intertwining equivalence is proved. This distinction already exists in §§3/6; ER-2B v0.2 C15A–C20 supplies a bounded illustration, **not** a physical threshold or native RRF network profile.

`[OPEN] [scope: non-transfer guard; physical bridge not selected]` `RRF-DYAD-W` and `RRF-NET-W-RAW` remain distinct types; additive closure of the latter is not automatically transported from isolated dyads. Neither a coordinate change, a source identification, nor a finite-order factor is evidence of a chosen physical carrier, incidence law or birth mechanism. OPEN-B → OPEN-E1 → OPEN-E2 remains locked.

**v0.8 evaluation boundary.** The preceding §0 paragraphs labelled source-synchronization and finalization record the **adopted v0.7 history (5 October 2026)**; they are preserved as issued, not claims that v0.8 is adopted or that v0.8 reran the old owner certificates. The v0.8 work rechecked current interface passages and performed text/identity comparison only. The previous release’s `supersedes: v0.6`, draft, adoption-record and finalization-editor metadata remain attributable to v0.7, as copied into the history and predecessor fields above.

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
| Native observables | lifted differences $(\Delta\rho,\Delta\eta)$ along a trajectory; fixed points $P_1=(0,0)$ elliptic order-6, $P_2=(0,\pi)$ hyperbolic saddle (`[import: DYAD v6.4.10 §1; RID unavailable]`; $\det J=1+(e^\rho-1)\cos\eta$, non-symplectic); winding fixed points $(\log(1+2\pi k),0)$, $(\log(1+2\pi k),\pi)$ on the global cylinder `[import: RECOG v0.3.14 §6.3; RID unavailable]`. Guard: $\mathrm{Fix}_0(T)=\{P_1,P_2\}\subsetneq\{C_{\rm pole}=\pm1\}$ — a comparator value fixed under inversion is not a fixed state (e.g. $T(a,0)=(a,e^a-1)$ with $C_{\rm pole}=1$) `[import: RECOG v0.3.14 §6.3; RID unavailable]`. |
| Observable status | $(\Delta\rho,\Delta\eta)$ **lifted realisation** of $R^\times$; not $\log R^\times$ without branch data |
| Relabeling candidate | $S_{{\rm lift},h}=\mathcal L^{-1}S_h\mathcal L$ — the exact `T-L` transport of the registered exact involution $S_h$ (involutivity exact); its truncation $S_{{\rm lift},6}=\mathcal J_{\le6}S_{{\rm lift},h}=\mathcal L^{-1}S_6\mathcal L$; dynamical commutation `[ALG] [scope: degree ≤ 6] [import: RECOG v0.3.14 §6.14, cert check 9; evidence RID: RECOG-ART-R11-LEDGER] [provenance: Claude-checked as recorded by RECOG; owner-source inspection, no rerun here]`, hence the same exact representation-level involution as $S_h$ and $-I_{\rm NF}$; $S_6$ is only its degree-six truncation (§4.2); **not** $(\rho,\eta)\mapsto(-\rho,-\eta)$: $T\circ S_o-S_o\circ T=(0,2(\cosh\rho-1))$, i.e. $T=T_s+T_b$, $T_b=(0,\cosh\rho-1)$ `[import: RECOG v0.3.14 §6.4 and §6.7; RID unavailable]` |
| Exactness | dynamics exact; $S_{{\rm lift},h}$ exact local involution; commutation with the dynamics verified through degree six only |
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
| Relabeling candidate (two symbols) | **Registered object:** the exact local map $S_h=h_6\circ(-I)\circ h_6^{-1}$ on $h_6(D)$, $D$ a sign-symmetric disk inside the certified inverse domain. **Involution exact by construction:** $S_h^2=I$ on $h_6(D)$. **Commutation finite-order only:** $\mathcal J_{\le6}(f\circ S_h-S_h\circ f)=0$ `[ALG] [scope: degree ≤ 6] [conv: DYAD-ALG-NF6 additive normalizer] [import: RECOG v0.3.14 §6.14, cert check 9; evidence RID: RECOG-ART-R11-LEDGER] [provenance: Claude-checked as recorded by RECOG; owner-source inspection, no rerun here]`. The truncation $S_6:=\mathcal J_{\le6}S_h$ satisfies both identities only to jet order. Leading terms: $S_h(W)=-W+s_2(W,\bar W)+O(3)$, $s_2=2h_2=-\tfrac{1+i\sqrt3}{6}W^2-\tfrac23W\bar W+\tfrac{1-i\sqrt3}{12}\bar W^2$. |
| Covariance of native observables under $S_h$ | General two-input identities are algebraic consequences of the displayed $s_2$: $C_W(S_hW_a,S_hW_b)-C_W(W_a,W_b)=O(3)$, and $C_W(S_hW_a,W_b)=-C_W(W_a,W_b)+O(3)$ (joint total degree in the two states). The nonzero real-ray witness $C_W(S_ht,S_ht)-C_W(t,t)=\tfrac32t^3+O(t^4)$ is independently reconstructed in RECOG §6.14 check 9 `[ALG] [scope: fixed adopted h_6; finite-jet consequence, not exact invariance] [import: RECOG v0.3.14 §6.14; evidence RID: RECOG-ART-R11-LEDGER] [provenance: Claude-checked as recorded by RECOG for the stated check; no rerun here]`. A comparator with exact $S_h$-covariance is $C^W_{\rm cov}(a,b)=\overline{h_6^{-1}(W_a)}h_6^{-1}(W_b)$: the transported NF-native $C_z$, separately **re-defined** relative to $C_W$ (§4.1). |
| Six-step parity `[import: DYAD v6.4.10 §6.12, definition E_odd; RID unavailable]` | $F_W$ is **not** odd under $w\mapsto-w$: $\tfrac12(F_W(w)+F_W(-w))=F_4(w)+O(6)$, $F_4\ne0$; $E_{\rm odd}(w)=\tfrac12(F_W(w)-F_W(-w))-w=\mu\lvert w\rvert^2w+O(5)$. $F_4$ is the six-step counterpart of the one-step $T_b$ obstruction. Physical bridge of $E_{\rm odd}$ `[OPEN]` (owner-recorded). |
| Exactness | $\mathcal L$ exact linear bijection; $S_h$ exact involution, dynamical commutation degree-6 certified |
| Information loss | none relative to LIFT |
| Guard | $\Re W,\Im W$ are structure-adapted components, not spatial axes `[import: OFN v0.9 §4.4 #ofn-rank-typing; RID: RTG-OFN-DEF-RANK-TYPING]` |
| Status | `[DEF]`; $Q_{\rm prim}=\lvert W\rvert^2$ exact |

## 2.4 `RRF-DYAD-NF`

| Field | Entry |
|---|---|
| Normalisation object | **Polynomial conjugacy only** — DYAD SG-19 operation (iii): $W=h(z,\bar z)$, $h=\mathrm{id}+h_2+\dots+h_6$, exact additive polynomial over $\mathbb Q(i\sqrt3)$, **resonant monomial coefficients of each $h_n$ set to zero** (resonance $a-b-1\equiv0\bmod 6$); table in `DYAD_RETURN_ENCLOSURE_P2B_v2/outputs/certificate.json` (`jets.h_degree6`, `jets.J_through6`) `[import: DYAD v6.4.10 §6.14; RID: DYAD-ALG-NF6] [provenance: owner-adopted]`. Operations (i) archival $\Phi_{\rm archive}$ and (ii) log-channel projection $G_{\rm proj}$ are **not** this profile. |
| Non-transferable quantities | **Standing refusal after R11 closure:** raw $\tfrac{47}{54}$ ($\mathcal A_{\rm raw}$), archival $c_\theta^{(6)},a_1,a_2$ in the Lie strict-kernel convention, fitted long-orbit backbones, projected-model coefficients, and raw $c_{05}$ are not inputs to the current NF chart merely by sharing names. RECOG R11 is CLOSED and explicitly retains this refusal; it does not authorize these transfers `[import: RECOG v0.3.14 §6.14, refusal line; evidence RID: RECOG-ART-R11-LEDGER]`. Standing lattice obstruction: $c^{({\rm raw},6)}_{05}-a_{05}=\tfrac{-13+3i\sqrt3}{576}\ne0$ `[import: DYAD v6.4.10 §6.14; RID: DYAD-ALG-NF6-OBS]`. |
| Domain | inverse-coordinate domain of DYAD-THM-NF-INV: $h_6$ injective on $\lvert z\rvert\le\tfrac1{10}$ with $\lvert h_6(z)\rvert\le\tfrac{17}{16}\lvert z\rvert$, $h_6^{-1}$ exists on $\lvert W\rvert\le\tfrac9{100}$ (majorant $M(s)$, $H(s)=s+M(s)$); remainder domain of DYAD-THM-NF-REM with radius-indexed profiles $(r,C_7)=(\tfrac1{20},100)$ or $(\tfrac1{40},30)$, never mixed; **local only** |
| One-step objects (two symbols) | **Delivered:** $\widehat f_6=h_6^{-1}fh_6$, exact analytic map on its proved domain, finite jet $n$ with $\mathcal J_{\le6}(f\circ h_6-h_6\circ n)=0$. **Formal:** $\widehat f_{\rm form}=h_{\rm form}^{-1}fh_{\rm form}$, the formal Poincaré–Dulac normal form; contains only resonant monomials $z^p\bar z^q$, $p-q\equiv1\ (\mathrm{mod}\ 6)$ — hence all of odd degree. $h_6=\mathcal J_{\le6}h_{\rm form}$ under the shared convention. |
| One-step symmetry | Formal: $\widehat f_{\rm form}(\lambda z)=\lambda\widehat f_{\rm form}(z)$, hence $\widehat f_{\rm form}(-z)=-\widehat f_{\rm form}(z)$, $-1=\lambda^3$ `[ALG] [scope: formal all-order] [provenance: Claude-checked (resonance argument)]`. Delivered: only $\mathcal J_{\le6}\big(\widehat f_6(\lambda z)-\lambda\widehat f_6(z)\big)=0$ `[ALG] [scope: degree ≤ 6]`; all-order equivariance of the exact analytic $\widehat f_6$ is **not** established by the certificate. |
| Six-step object | $\widehat F=h^{-1}F_Wh$, finite jet $J(z)=z+\mu z^2\bar z+a_{32}z^3\bar z^2+a_{05}\bar z^5$; linear part identity; certified remainder $\lvert\widehat F-J\rvert\le C_7\lvert z\rvert^7$ `[import: DYAD v6.4.10 §6.14; RID: DYAD-THM-NF-REM]`. $E_{\rm NF}(z)=\widehat F(z)-z=\mu\lvert z\rvert^2z+O(5)$; its jet $J$ is odd (finite order), the formal six-step normal form is odd; this exact map (fixed finite $h_6$) has **no all-order oddness under the naive $-I$ action**: the verified fixed-chart degree-ten parity obstruction is recorded separately as finding VF-1 (§2.4a); the jet and remainder certificates are unaffected and the profile remains valid. **$\widehat f$ and $\widehat F$ are different maps; $n$ and $J$ are different jets; neither is an all-orders identity (SG-19).** |
| Native observables | $q=\lvert z\rvert^2$; self-return multiplier $\chi_m(z)=\widehat F^{\circ m}(z)/z$, defined for $z\ne0$ and admissible iterates (extension at $0$ stated separately); NF comparator $C_z(a,b)=\bar z_az_b$ |
| Source-derived history/limit observable | $\Psi=\Theta-\tau\log q$, $\tau=2\sqrt3/3$, with the continuous along-orbit lift of $\arg z$; $\mathcal M(z_0):=\Psi_\infty-\Psi(z_0)$ denotes RECOG's $M$ (renamed typographically here to avoid collision with the coordinate majorant $M(s)$). Defined for the exact return $\widehat F$, not a lattice-free comparison model `[import: RECOG v0.3.14 §6.13a; RID: RECOG-THM-R9-MEMORY]`. This is an imported derived observable with its own source theorem, not a newly appended independent state coordinate; track/domain and token limitations are in §4.1a. |
| Observable status | $q$, $\chi_m$, $C_z$ **native / re-defined**; $Q_{\rm prim}=\lvert h(z,\bar z)\rvert^2$ and $C_W\!\mid_{\rm NF}=\overline{h(z_a)}\,h(z_b)$ **transported** |
| Relabeling candidate | $z\mapsto-z$: exact symmetry of $\widehat f_{\rm form}$; degree-6 certified for $\widehat f_6$. $h_6$ is the unique solution of the specified homological recursion through degree 6 under the zero-resonant-coefficient convention, so the exact map $S_h=h_6(-I)h_6^{-1}$ and its truncation $S_6=\mathcal J_{\le6}S_h$ carry no residual-gauge ambiguity at degree $\le6$ `[ALG] [scope: degree ≤ 6] [conv: DYAD-ALG-NF6]`. Canonicity under other normalizer conventions and at all formal orders is not supplied by this fixed-chart registry and remains `[OPEN] [scope: other normalization classes]`. This is not an unclosed R11 task: the completed R11 ledger pins the adopted chart and routes physical pole identification to RRF OPEN-A `[import: RECOG v0.3.14 §6.14; evidence RID: RECOG-ART-R11-LEDGER]`. |
| Formal G1 report — **source-pending pointer, not adopted here** | A 15–16 October cross-stream report proposes `\widehat S_{\rm form}=T^3(T^6)^{-1/2}=h_{\rm form}(-I)h_{\rm form}^{-1}` with formal tangent-to-identity inverse-square-root branch, and reports a formal uniqueness argument. The fixed **finite** chart map $S_h=h_6(-I)h_6^{-1}$ is exactly involutive but is only a **degree-6 jet realization** of that formal object: $\mathcal J_{\le6}\widehat S_{\rm form}=\mathcal J_{\le6}S_h=S_6$ under the shared normalizer convention. Do **not** identify the full formal map with finite $S_h$, infer analytic convergence or upgrade its dynamical commutation past the certified scope. `[OPEN] [scope: original G1 owner source / proof, formal uniqueness review and convergence absent from inspected corpus]` |
| Covariance under $-I$ | **Exact algebraic identities:** $q(-z)=q(z)$; $C_z(-z_a,-z_b)=C_z(z_a,z_b)$; $C_z(-z_a,z_b)=-C_z(z_a,z_b)$. **Self-return multiplier:** for the formal odd normal form the formal multiplier is sign-invariant; for the polynomial model $\chi^J_m=J^{\circ m}/z$ sign-invariance is exact but that model is a separate re-definition, not a transport of $\chi_m$; for the delivered exact $\widehat F$, $\chi_1$ is **not exactly sign-invariant** — a consequence of the verified fixed-$h_6$ degree-ten finding VF-1 (§2.4a); $\chi_m$ for $m\ge2$ is not classified in this registry. Bounded statement for one return: with $R:=\widehat F-J$, $\lvert R(z)\rvert\le C_7\lvert z\rvert^7$ and $J(-z)=-J(z)$, $\chi_1(-z)-\chi_1(z)=-\tfrac{R(-z)+R(z)}{z}$, hence $\lvert\chi_1(-z)-\chi_1(z)\rvert\le2C_7\lvert z\rvert^6$ on $0<\lvert z\rvert\le r$ `[ALG] [scope: direct consequence of DYAD-THM-NF-REM, one six-step return, either (r,C_7) profile unmixed] [provenance: review v1 deduction; Claude-checked]`. No $m$-uniform iteration bound is claimed. |
| Common-realisation condition `[DEF] [scope: RRF working convention]` | two $z$-states may be compared by $C_z$ only if $z_a=h_6^{-1}(W_a)$, $z_b=h_6^{-1}(W_b)$ — **preimages under the same registered $h_6$** (images under $h_6^{-1}$) of states in the **same registered $W$-frame**, both inside the registered inverse domain — or an explicit certified frame transport between their charts is registered. Direction/typing only; decides nothing about physical co-realisation, birth inheritance or the network bridge. A registered frame/context transport is necessary for comparing differently represented data, but does not itself supply an admissible shared physical history; NUMGEN M2-1 makes this separation explicit (§6.1). |
| Exactness | formal all-order / degree-6 certified / certified remainder |
| Information loss | none inside domain; no global content |
| Guards | $q\ne Q_{\rm prim}$ beyond leading order — they are different native observables, not two coordinate expressions of one; primitive iterates $Q_m$ and normalized iterates $q_m$ are **not identified** (DYAD §6.14); $\bar z_az_b\ne\overline{h(z_a)}h(z_b)$ in general |
| Status | `[DEF]`; chart and certificates owner-adopted (DYAD v6.4.10) |

## 2.4a Verified findings attached to `RRF-DYAD-NF`

Findings kept in their own block, with provenance, so that the profile rows state what holds and this block states what was computed, by whom, and within what scope (Methodology distinction: reported / reviewed / executed / independently checked).

**VF-1 — even degree-ten return term (formerly PRF-1).** Object: $\widehat F=h_6^{-1}\circ F_W\circ h_6$ with $h_6$ the fixed adopted degree-6 polynomial normalizer (DYAD-ALG-NF6, 23 coefficients, resonant coefficients zero), $F_W$ the exact six-step return built to total degree 10, and $h_6^{-1}$ taken as the degree-ten Taylor jet of the certified local analytic inverse (DYAD-THM-NF-INV; $h_6\circ h_6^{-1}=\mathrm{id}$ verified through degree 10 — a finite identity, not a convergence proof for any all-order normalizer). Result: $\mathcal J_{\le6}\widehat F=J$ reproduced; even-degree homogeneous parts of degrees 2, 4, 6, 8 vanish identically; the degree-10 even part does not (ten nonzero monomials; the full table is not attached), with

$$[\widehat F]_{(5,5)}=-\tfrac{6113}{839808}-\tfrac{3152683\,i\sqrt3}{403107840}\ne0 .$$

`[ALG] [scope: fixed adopted h_6; exact Taylor computation through total degree 10] [provenance: Claude-checked (written verification record `DYAD_CHECK_degree10_even_term_hatF`, Dyadic DSN editor session, 25 Sep 2026; same exact $\mathbb Q(i\sqrt3)$ engine as the v6.4.10 referee, independent of the third-party code); prior report (PRR_RRF_REVIEW_v1, third reviewer) confirmed including the "first even term is degree ten" part; integration record RTG_RRF_DEGREE10_REVIEW_INTEGRATION_v1 (ChatGPT, inspection only, no re-execution)]`.

**Consequences (verified scope only).** $\widehat F(-z)+\widehat F(z)\not\equiv0$ and $\chi_1(-z)-\chi_1(z)\not\equiv0$ for $z\ne0$: an identity failure, not a pointwise-nonzero defect, not a positive uniform lower bound, and not a statement about $\chi_m$ for $m\ge2$ (not computed). Reading: the parity in question is that of the dynamics **as represented with the fixed truncated $h_6$ under the naive $-I$ action**; a degree-6 truncated normalizer is not expected to preserve normal-form parity beyond its own order, the even content re-entering at the first order where the truncation error of $h$ feeds back into the return. This is a property of the delivered chart/action pair, not a statement that the primitive dynamics lacks symmetry under every local involution.

**Unchanged by VF-1:** the formal all-order normal form (odd by $p-q\equiv1\bmod6$); the odd jet $J$; DYAD-THM-NF-REM ($C_7$, $C_D$) and DYAD-THM-PRIM-CTR; the one-return bound, now known to be non-vacuous: $\lvert\chi_1(-z)-\chi_1(z)\rvert\le200\lvert z\rvert^6$ on $0<\lvert z\rvert\le\tfrac1{20}$, $\le60\lvert z\rvert^6$ on $0<\lvert z\rvert\le\tfrac1{40}$ (profiles unmixed; VF-1 does not sharpen these constants or radii); $S_h^2=I$; RRF OPEN-A. R11 is now closed by its separate owner record; VF-1 neither supplies nor withdraws that closure. The covered degree-six provenance is upgraded by RECOG check 9, not by VF-1. Artifact-level identity against `PRR_RRF_REVIEW_v1.zip` and `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` / `outputs/certificate.json` was not re-done here (archives not mounted); recording the written confirmation does not require it.

**RECOG dependency note (v0.7 synchronization).** RECOG v0.3.14 §7 explicitly excludes the degree-ten result from its scientific inputs; its RRF import is convention-only. Section 6.16f nevertheless mentions VF-1 descriptively when warning that chart-symmetry germs do not justify an all-orders analytic gauge. Therefore the precise receipt is **not a load-bearing theorem/certificate premise**, not “absent everywhere.” Check 9 is not a new degree-ten verification. VF-1 retains its existing written-verification provenance unchanged.

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
| Bookkeeping reorientation | $\mathscr O_e:\ W_e^{\rm net}\mapsto-W_e^{\rm net}$ **together with** $\epsilon_{\gamma e}\mapsto-\epsilon_{\gamma e}$; incidence-dressed quantities invariant. **This is edge-coordinate bookkeeping, not the dynamical pole-relabel candidate $S_h$; no bridge between $\mathscr O_e$ and $S_h$ is established until OPEN-B/E1.** Bare $\overline{W_a}W_b$ for non-incident edges has no gauge-invariant sign. |
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
| `T-h` | $W=h_6(z,\bar z)$ | certified local nonlinear diffeomorphism | local-certified $h_6^{-1}$ (DYAD-THM-NF-INV: $\lvert z\rvert\le\tfrac1{10}$, $\lvert W\rvert\le\tfrac9{100}$) | NF-INV / NF-REM domains | **Pullbacks, not identifications:** $h_6^*Q_{\rm prim}(z)=\lvert h_6(z)\rvert^2$ (primitive amplitude in NF coordinates); $(h_6^{-1})^*q(W)=\lvert h_6^{-1}(W)\rvert^2$ (NF amplitude in $W$ coordinates); $h_6^*C_W(a,b)=\overline{h_6(z_a)}h_6(z_b)$; $(h_6^{-1})^*C_z=C^W_{\rm cov}$. $q$, $C_z$ remain separately defined native NF observables. | single-dyad only; network closure not silently transported; predicates/sections require full pullback on admissible transitions (§4.3) | $-I\mapsto S_h$ | none in domain |
| `T-L` | $(\rho,\eta)=\mathcal L^{-1}W$ | global linear bijection | global | $\mathbb R^2$ | $Q_{\rm prim}=\rho^2-\rho\eta+\eta^2$ | linear cycle sums transported exactly | $S_h\mapsto\mathcal L^{-1}S_h\mathcal L$ | none |
| `T-exp` | $\zeta=e^{\rho+i\eta}$ | covering / quotient wrap | **none without lift** | global | $(\Delta\rho,\Delta\eta)\mapsto R^\times=e^{\Delta\rho+i\Delta\eta}$ (loses $k$) | additive cycle sums $\mapsto$ multiplicative: $\sum_\gamma(\Delta\rho_e+i\Delta\eta_e)=2\pi ik\Rightarrow H_\times=1$ (both radial and angular parts must close) | **no registered exact transport of the swap**: $S_{\rm lift}$ and $\zeta\mapsto\zeta^{-1}$ agree at linear order only; identification OPEN-A | integer winding |
| `T-net` | — | `[OPEN] [scope: bridge]` | — | — | — | — | — | — |
| composite NF → WRAPPED | $p=E\circ\mathcal L^{-1}\circ h_6$, $E(\rho,\eta)=e^{\rho+i\eta}$ | local forward composite | **local inverse on the registered image using the fixed principal lift:** $p^{-1}(\zeta)=h_6^{-1}\big(\mathcal L(\log\lvert\zeta\rvert,\operatorname{Arg}\zeta)\big)$, since on $\lvert z\rvert\le\tfrac1{10}$: $\lvert\eta\rvert\le\tfrac{2}{\sqrt3}\lvert h_6(z)\rvert<\tfrac{119}{960}<\pi$ (single principal sheet) `[ALG] [scope: consequence of DYAD-THM-NF-INV; no new radius] [provenance: review v1 deduction; Claude-checked]`; **no global inverse on arbitrary $\mathbb C^*$** | NF domain | as composed | as composed | as composed | **none on the registered single-sheet domain**; only the unrestricted global `T-exp` forgets deck-sheet data, and only when such data are part of its source |

Rule: an observable or constraint written in a destination profile without a row in this table is **untransported** and must be tagged `[OPEN] [scope: transport]`.

### 3.1 Triadic / Genesis planar metric convention — CN-05 (convention-only; proposed consumer receipt)

`[DEF] [scope: typed metric convention for **identical identified planar vectors only**; no new RRF native profile or physical transport arrow] [import: Triadic v1.6 §7.4 and CN-05; RID unavailable; owner notice CN-05] [provenance: adopted Triadic owner source; consumer interpretation restricted]` For the same planar vector pair in the respective producer conventions, the **metric and oriented-area units** obey

\[
B_T^{\rm plane}=2B_G,\qquad Q_T=2Q_G,\qquad I_T=2I_G,\qquad \Omega_T=-\sqrt3\,\omega_{\rm raw}.
\]

This is a **convention comparison**, not a generator, mode, birth-event, inherited-child, apex $z$-component or physical carrier identification. It does not assert that the actual Genesis and Triadic birth states are the same objects; that bridge remains `[OPEN]`. When **and only when** the same vectors are identified, translating the Genesis conditional cubic loading $Q_c^G=\kappa^2(Q_s^G)^3$ would require

\[
Q_c^T=\frac{\kappa^2}{4}(Q_s^T)^3.
\]

`[OPEN] [scope: consumer obligation; NOT APPLIED to any owner birth formula]` Any later use must first declare the same-vector identification, source metric, orientation convention, child/parent variables and owner-accepted birth law; its coefficients must be re-expressed rather than copied. The equality above is the **conditional units conversion**, not a modified physical child law or an adopted Genesis↔Triadic birth bridge. Triadic CN-05 requests this convention record while retaining its distinct consumer-reconciliation tasks.

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

$\bar z_az_b\ne\overline{h(z_a)}h(z_b)$ in general `[import: RECOG v0.3.14 §6.14, comparator tracks, cert checks 5–7; evidence RID: RECOG-ART-R11-LEDGER]`; discussion record in Wrap-up v0.2 §11.

**Covariance belongs to the pair (observable, action), not to a chart.** The two tracks are now explicitly defined and checked in the CLOSED R11 ledger: transporting $C_W$ and $S_h$ together does not remove the covariance defect of $C_W$, while $C^W_{\rm cov}$ has exact covariance in raw coordinates `[ALG] [scope: fixed chart and specified involution] [import: RECOG v0.3.14 §6.14, cert checks 5–7 and 9; evidence RID: RECOG-ART-R11-LEDGER]`. This resolves the representation ledger, not uniqueness of the physically admissible observable algebra or physical pole-relabeling status. OPEN-A remains outside RECOG.

**$S$-decomposition** `[ALG] [scope: RRF discussion-local] [provenance: Claude-checked]`: on a simply connected local domain where $C\ne0$ and $C\circ S\ne0$, with a consistent square-root branch (branch near $1$ inside the certified tube),
$C=C_-\,C_+$, $C_-=(C/C\circ S)^{1/2}$, $C_+=(C\cdot C\circ S)^{1/2}$; $C_-(Sx)=C_-(x)^{-1}$, $C_+(Sx)=C_+(x)$.
For multiplicative comparators whose typed relabeling law is $C(Sx)=C(x)^{-1}$, $C_+\ne1$ measures the covariance defect. $C_+$ is $S$-even and cannot decide orientation. Not canonical globally without a branch choice.

**Symmetrisation-order guard** `[import: DYAD §6.12]`: symmetrising the generator and iterating is not symmetrising the return — $[\mathrm{Odd}(f^{\circ6})]_{21}=\mu$ but $[(\mathrm{Odd}\,f)^{\circ6}]_{21}=\tfrac12-\tfrac{i\sqrt3}{6}$. A $C_\pm$ decomposition or an odd twin ($T_s$) defined at one-step level is not transferred to the six-step return without recomputation.

### 4.1a Imported exact-map memory: track and amplitude limits

`[DEF]` [import: RECOG v0.3.14 §6.13a; RID: RECOG-THM-R9-MEMORY] RECOG's intrinsic retained observable is $\mathcal M(z_0)=\Psi_\infty-\Psi(z_0)$ in §2.4's fixed chart. Its current theorem is on the **$C_z$ track only**. The transported raw track $C_W^{(h)}$ has different initial equality classes and is not granted the same exact-map incompleteness theorem by a change of label.

`[THM]` [scope: imported owner result; selected T; exact normalized return; not a new RRF theorem] [import: RECOG v0.3.14 §6.13a; RID: RECOG-THM-R9-MEMORY]

$$\mathcal M(z_0)=q_0[c_{\rm iso}+\Lambda_1(\Theta_0)]+R,\qquad |R|\le C_2q_0^2,$$

where $c_{\rm iso}=-4\sqrt3/27$ and $\Lambda_1(\Theta)=(43\sin6\Theta-5611\sqrt3\cos6\Theta)/1270080$ in the owner's fixed chart.

| DYAD-NF row | Memory theorem domain | R9 remainder constant $C_2$ in $\lvert R\rvert\le C_2q_0^2$ | Constructive exact-map $C_z$ incompleteness window |
|---|---|---|---|
| $r=1/20$, $C_7=100$ | $0<q_0\le1/400$ | 517 | $0<q_0<\lvert G\rvert/517$ |
| $r=1/40$, $C_7=30$ | $0<q_0\le1/1600$ | 163 | $0<q_0<\lvert G\rvert/163$ |

Here $G=-(43+5611i\sqrt3)/1270080$ is the owner's averaging coefficient. The theorem has an isotropic as well as a lattice term; the table does not replace its full statement. The smaller windows are not the whole memory-theorem domains. This is retained information not determined by the specified initial pair-comparator data; it is not information created by a threshold, a birth law, or a token-written carrier. No exact sign-invariance of $\mathcal M$ is inferred from its leading sixfold harmonic.

## 4.2 Pole-relabeling candidate actions

| Profile | Action | Status |
|---|---|---|
| WRAPPED | $\zeta\mapsto\zeta^{-1}$ | exact as ordered-ratio relabeling candidate |
| LIFT | $\mathcal L^{-1}S_h\mathcal L$ | exact involution; dynamical commutation degree-6 certified; not $(-\rho,-\eta)$ |
| W | $S_h=h_6(-I)h_6^{-1}$ (exact map on $h_6(D)$); $S_6=\mathcal J_{\le6}S_h$ (truncation) | $S_h^2=I$ exact; $\mathcal J_{\le6}(fS_h-S_hf)=0$; $h_6$ unique under `[conv: DYAD-ALG-NF6]` |
| NF | $z\mapsto-z$ | exact symmetry of $\widehat f_{\rm form}$; degree-6 certified for $\widehat f_6$ |
| NET | $\mathscr O_e$ (bookkeeping reorientation) | exact bookkeeping; **not** a pole-relabel candidate |

> **Established by registered transports:** $-I_{\rm NF}$, $S_h$ and $S_{\rm lift}$ are the same representation-level involution carried along `T-h` and `T-L` (by definition of $S_h$ and by exactness of $\mathcal L$). Involutivity is exact; commutation with the dynamics is finite-order (degree 6) or formal (for $\widehat f_{\rm form}$) — no all-order dynamical symmetry of the delivered maps is registered. **OPEN-A proper** consists of two questions only: (1) whether this involution is the physical pole relabeling; (2) whether the WRAPPED action $\zeta\mapsto\zeta^{-1}$ is the same physical operation — the two agree at linear order only and no exact transport of the involution across `T-exp` is registered. Six-step evidence: the raw return $F_W$ is not $-I$-odd ($F_4\ne0$) while the six-step jet $J$ is (DYAD §6.12).

**Cross-stream G1 pointer (reported 15–16 October, not a new RRF theorem).** The proposed formal involution $\widehat S_{\rm form}=T^3(T^6)^{-1/2}$ and the canonical formal normalizer involution $h_{\rm form}(-I)h_{\rm form}^{-1}$ are reported equal, with degree-6 jet agreeing with the registered $S_6$; the full finite-map $S_h$ remains only exactly involutive and finite-order commuting as recorded above. Proof of **formal uniqueness**, convergence of the formal normalizer, and physical identification await the named owner source/decision. This pointer does **not** close OPEN-A, G2 or analytic Problem B.

Typed-covariance criterion for gauge status (Wrap-up §10.2): $O(Sx)=\tau_O(O(x))$ for every admissible $O$, with $\tau_O$ the type's relabeling law — not universal invariance.

**Generator-family limit on OPEN-A.** `[import: RECOG v0.3.14 §6.7 and §6.15; RID: RECOG-THM-TWIN-RADIAL-ACCESS]` The global radial-access theorem concerns the particular symmetric twin $T_s=(\rho-\sin\eta,\eta+\sinh\rho-\sin\eta)$: every initial state with $0<Q<7/200$ eventually reaches $|\rho|\ge\operatorname{arccosh}2$. It contrasts with the selected $T$'s certified local contraction. It is **not** a theorem that exact swap symmetry precludes healing for every admissible shear. RECOG §6.7 explicitly retains $g(\rho)=\tanh\rho$ as an odd, healing-at-cubic-order counterexample. The family law $\Re\mu_6=3b-4a^2$ for $g=\rho+a\rho^2+b\rho^3+\cdots$ has two routes to negative radial drift; removing the quadratic term does not force $b>0$. The diagnostic twins are not new registered RRF physical profiles. OPEN-A is not resolved in favor of a nonlinear physical swap by the $\sinh$ result; R1 remains PARTIAL in RECOG.

### 4.2a Cross-model orientation conjugacy is not physical pole exchange

`[ALG] [import: RECOG v0.3.20 §6.6a #sec-6-6a-composition; RID: RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY] [provenance: RECOG freeze candidate; owner source inspected, no independent certificate rerun; adopted OFN v0.9 §6.4 / IMP-O09-03 is a consumer cross-reference, not the theorem owner] [scope: character/shear family only]` For the declared character/shear family and `S_o(ρ,η)=(-ρ,-η)`:

\[
 S_o\circ T_k\circ S_o=T_{-k}.
\]

This is **conjugacy between two parameter-labelled maps**, not an exact symmetry of the fixed primitive `T_1`, nor an identity with the nonlinear fixed-chart involution `S_h=h_6(-I)h_6^{-1}` or the edge-bookkeeping reversal `\mathscr O_e`. Thus an isolated-dyad conjugacy invariant cannot select the `k` sign *within this model family*, while physical oriented-role interpretation stays OFN `OPEN-OPA` / RRF OPEN-A. The specific `sinh` diagnostic twin's radial theorem cannot exclude all odd generators: RECOG's odd `tanh` example has local cubic healing. No additional RRF native profile or physical gauge law is created.

## 4.3 Event predicates and sections: transported is not reselected

`[ALG]` [scope: same registered exact map and complete event predicate, where its chart/transition domains are valid] [import: RECOG v0.3.14 §6.16b; RID: RECOG-ALG-BTOKEN-TRANSPORT]

Let the primitive B section be $\Sigma_B^W=\{W=t>0\}$, with the owner's full crossing predicate (including side/coorientation and $\rho$ restrictions). Under `T-h`,

$$\Sigma_B^z=h_6^{-1}(\Sigma_B^W),\qquad E_B^z(z,z')=E_B^W(h_6(z),h_6(z')).$$

The same admissible trajectory has the same event indices and gap word after this pullback. Replacing $\Sigma_B^z$ by the native ray $\arg z=0$ is **re-definition/selection of another event rule**, not transport of the old rule. A six-step-only record also does not automatically recover intermediate primitive crossing predicates.

The section/action shadow is separately recorded under `RECOG-ALG-SH-SECTION-SHADOW` (representation-level $S_h$ only). It does not identify $S_h$ with physical pole exchange. Full predicate transport is a necessary representation check, but every state-defined predicate has a pullback; independence from auxiliary choices still left free by the model is a separate token-selection requirement. A normalizer-dependent native lattice threshold is not promoted to the B/7-gap token by this table. No new physical event or retained state field is registered.


---

# 5. Cycle-invariant matrix

| Invariant | Value space | Arity | Required structure | Gauge law under which invariant | Isolated certified dyad tube | Network sectors |
|---|---|---|---|---|---|---|
| $H_\times(\gamma)=\prod_{e\in\gamma}R_e$ | $\mathbb C^*$ | cycle $\ge3$ | multiplicative edge relations $R_e$ — **not native to `RRF-NET-W-RAW`**; requires a future registered multiplicative network realization | coherent vertex gauge $R_{ij}\mapsto g_i^{-1}R_{ij}g_j$, $g_i\in\mathbb C^*$ | N/A (no cycle) | node-mediated multiplicative-ratio branch: $H_\times=1$; independent multiplicative-edge branch: $H_\times\ne1$ possible |
| $H_2(\gamma)=\prod_{e\in\gamma}\sigma_e$ | $\mathbb Z_2$ | cycle $\ge3$ | pole-identification connection $\sigma_e$ | $\sigma_{ij}\mapsto g_i\sigma_{ij}g_j$, $g_i\in\mathbb Z_2$ (incidence-dressed) | N/A (no cycle; no winding needed) | not independently represented in current node-mediated attachment |
| $k$ | $\mathbb Z$ | history / path-lift; cycle when spatially closed | coherent lifted history | $\tilde\theta_i\mapsto\tilde\theta_i+2\pi n_i$ (node-coherent lift gauge) | $k=0$ `[import: NUMGEN v1.20.7 §6.4 N-3A; RID: NUMGEN-N3A-DECK-TRIVIAL] [scope: certified local one-chart tube, not every network or global trajectory]` | `[OPEN]` until a discrete profile is registered |

Obstruction statements, one-way: $H_\times\ne1\Rightarrow$ no pure node-presentation reduction `[ALG] [scope: RRF discussion-local]`; $H_2=-1\Rightarrow$ present node-mediated identification scheme insufficient (pole-role identification or an added $\mathbb Z_2$ edge field required) `[ALG] [scope: RRF discussion-local]`; additive $Ca\ne0\Rightarrow$ node-potential representation insufficient `[import: NUMGEN v1.20.7 §6.8 NG-7A; RID: NUMGEN-OPEN-REC-HOL-OPERATOR]` (sub-RID of closed NG-7A; identifier spelling preserved). No coupling among the three is claimed.

---

# 6. Dependency lock: OPEN-B → OPEN-E1 → OPEN-E2

- **OPEN-B** (genesis identification primitive: node identity vs pole-role identity) must be resolved before a **canonical** choice of network state variables (**OPEN-E1**).
- Provisional network work may proceed in `RRF-NET-W-RAW` with incidence data, provided any node-mediated Jacobi/mode reduction is explicitly marked as that branch.
- **OPEN-E2** (joint constrained normal form of the coupled triad) starts only after E1. The single-dyad $h$ is not the answer to E2.

### 6.1 Representation alignment does not supply a physical composition domain

`[ALG]` [scope: imported algebra only] [import: NUMGEN v1.20.7 §6.6 C7C-M, M2-1 transported chain identity; RID unavailable for this sub-result] A cofinal order-preserving map can align two comparison contexts and transport bounded count defects. M2-1 still requires a separately admitted outer pair for carrier closure; alignment does not create co-realization.

**Separate source-status receipt, not an algebraic closure:** Census-1 is **INCONCLUSIVE / INCONCLUSIVE** because no admitted nondegenerate composable source chain is present in that evidence set. No PASS/FAIL verdict on full-interface WD-DOM follows. This outcome is recorded in the same owner §6.6, not inferred from M2-1.

For this registry, the consequence is a **boundary**, not a new physical composition theorem: same numerical labels, same $h_6$, or a registered coordinate/context map alone do not establish an admissible common birth history or comparison interface. The common-realisation condition in §2.4 is a representation requirement, not a construction of its physical prerequisites. No NUMGEN C7C instrument-only lemma is promoted here. OPEN-B/E and the source M-4 HOLD on the Discrete-owner P2 policy remain separate.

---

### 6.2 `RRF-CND-01` — coincidence realization admissibility (PROPOSED INTERFACE ONLY)

**Status:** `[DEF] [scope: noncanonical interface proposal; RRF/OFN ACCEPT SCOPED; not an adopted physics choice]`. This registry records **representation and admissibility contracts, not proofs or polynomial-jet tables**. The general exchange-fixed lemma remains mathematical source background and the primitive/six-step coincidence counterexample belongs to ER-2B and the two RRF/OFN coincidence reviews; their proofs, exact coefficients and execution provenance are **not reproduced or owned here**.

Four notions must remain distinct: **equal node coordinates**, **zero edge relation**, **exchange-fixed complete configuration**, and **node merge / lower-cardinality reduction**. Only a specified complete-state exchange-fixed set is governed by the usual equivariant fixed-set reasoning; merge needs a separate reduction.

| Owner contract | Required object | RRF admissibility gate |
|---|---|---|
| **Identity / Action** | Full physical state `\mathscr X` including transition-relevant incidence, roles, parameters and necessary history; fixed-model exchange action `\sigma_{BC}` and its physically realizable fixed states | State-completeness and **node-exchange** equivariance at the **selected** physical update; an exchange of edge slots need not be the node permutation. Identify the correct complete-state action and its fixed set; do not infer node-fixed semantics from slot symmetry or `r_{BC}=0` |
| **Carrier / Encoding** | Defined encoding `E:\mathscr X\to\mathcal C`, carrier exchange action `R`, candidate coincidence subset `\mathcal D` | `E\sigma=RE`; a **witnessed** mathematical counterexample initial point must lie in `E(Fix\sigma)` (not only in `\mathcal D`) |
| **Clock / Model** | Full physical update `F_{phys}`, conditional projected model `K`, physical strobe and projection cadence | `EF_{phys}=KE` on the applicable domain and relevant states, with compatible exchange/role action; primitive and six-step cadence are not interchangeable |
| **Merge** *(separate)* | If claimed, a specified lower-cardinality carrier, merge map and post-merge evolution | Independently justified commuting reduction; no merge conclusion from coincidence or symmetry alone |

**Source pointers and conditional outcome:** `[import/source: OFN v0.9, complete-state covariance / OPEN-PRIMACY-3B/3C; RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md; RTG_RRF_COINCIDENCE_ADMISSIBILITY_REVIEW_v0_1.md; RTG_RRF_RESPONSE_TO_OFN_COINCIDENCE_v0_2.md]`. For the named *raw projected* three-edge map with reprojection **after each primitive step**, the standard additive coincidence embedding has an exact noninvariance witness at primitive (degree 2) and six-step (degree 4) clocks. This is **conditional mathematics**, not automatic physical node-mediated exclusion. The full-state realization/encoding/clock bridge remains `[OPEN]` (OFN 3B/3C and RRF OPEN-B/E1).

**Slot-versus-node guard (cross-stream report; numerical evidence not replayed):** The projected triad may be edge-slot permutation-equivariant and preserve a child-free *slot-fixed* stratum while failing to preserve a *node-coincidence* stratum. Reported odd-twin comparison is diagnostic, not an owner-adopted physical selection; the detailed calculation remains with the external OFN/ER-2B study. A fixed-set or quotient inference requires the action to intertwine the **actual full update** and the proposed coincidence embedding.

**Regularity/clock decision — OPEN-B/E1 and OFN:** The elementary fixed-set implication needs only a defined equivariant map, not analyticity. A $C^\infty$ carrier may be studied as a **candidate**; this does not choose it over an analytic carrier, supply a convergent odd normalizer or make it a physical realization. Explicitly declare `regularity: analytic / C^\infty / formal / other`, valid domain and `clock: primitive T / six-step T^6 / other physical update` in each submitted realization contract. Formal G1 uniqueness for $T$-commuting actions must not be transferred to a hypothesis requiring commutation with $T^6$ alone.

**Passive transport guard:** A true passive recharting transports the *same* model, action and test subset; it cannot change invariance/noninvariance. Reimposing linear closure, replacing the carrier, changing update or selecting another physical clock is a **different model contract** requiring its own admissibility audit. Do not identify `(P_\mathcal C T^{\times3})^6` with `P_\mathcal C (T^6)^{\times3}` without proof of equivalence.

### 6.3 Token, history and network inheritance — interface prerequisites only

`[ALG] [scope: pointer to the preserved §4.3; no duplicate theorem import]` The full B-token transport rule is already registered in **§4.3**; RECOG v0.3.20 §6.16b retains its content. The B-section/count phase lift remains distinct from the primitive-`\eta` N-3A deck state. No duplicate transport claim or competing live version pin is introduced here.

`[OPEN] [import: RECOG v0.3.20 §6.16g; RID: RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS] [scope: missing network-inheritance interface; source classification not regraded]` For the currently registered source/carrier package, `token\to\Delta[a]` is **not yet well-posed**, rather than disproved. RRF records CELL-F4's necessary interface conditions without inventing physical attachments:

| Gate | Missing declaration |
|---|---|
| **W1** | graph, coefficient module, edge cochain and network realization |
| **W2** | dyad→edge/subgraph attachment preserving the relevant token predicate |
| **W3** | comparison/transport between *pre- and post-birth* cohomology spaces before forming `\Delta[a]` |
| **W4** | independence from the event log, count or Track-A clock alone |
| **W5** | conditioning/common-driver quotient distinguishing token-specific writing from shared-driver correlation |

The closed algebra of NUMGEN NG-7A, including its closed sub-RID, does not produce NG-7B source/curvature or a multiplicative G1 realization. M2-1's transported counting identity is not a co-realized physical composition or new birth law. Genesis v2.8.5 and Triadic v1.6 also distinguish unit rotation `W(J_Qs)/W(s)=i` from loaded child ratio `W(c_0^{[3]})/W(s_*)=i\kappa Q_s`; full remainder/physical source remain conditional. Independent Jacobi *mode labels* do not select an extra physical state dimension, and covariance typing does not uniquely fix physical lowering.

### 6.4 RER dynamical-closure proposal — external, source pending

`[DEF] [scope: reference-only; NON-NORMATIVE; RER v0.2 original source pending]` The optional RER closure-taxonomy and factor-evaluation plan formerly quoted in adopted v0.8 §6.4 is retained verbatim as a **separate noncanonical proposal**: `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md`. It is **not** a mandatory profile field, owner theorem, numerical certificate or approved physical representation. The original RER v0.2 and N=7/8 Stage-2 global verification remain uninspected; the communicated Stage-2 global certificate status is PENDING. For current representation admissibility use §§0.3, 3, 4 and 6.2–6.3; for candidate closure taxonomy, read the separate proposal, not this working standard.

# 7. Not registered (current version)

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
5. That source-ledger inspection is a local rerun of its scripts, or that RECOG check 9 verifies the full degree-ten table, every pairwise formula separately, or any physical gauge identification. Its specifically covered degree-six and real-ray claims now have recorded Claude verification.
6. That $E_{\rm odd}$ has a physical or consumer-accepted meaning (owner `[OPEN]`).
7. That the delivered exact maps $\widehat f_6$, $\widehat F$ possess all-order symmetries under the naive $-I$ action; only their finite jets and the formal normal form do, and for $\widehat F$ the verified finding VF-1 shows the contrary at degree ten. No universal negative about symmetry under other local involutions or actions is asserted.
8. That $\chi_1$ is exactly sign-invariant for the delivered map (it is not, VF-1); nothing is asserted about $\chi_m$, $m\ge2$; the only quantitative self-return defect statement registered is the one-return bound.
9. That the local NF → WRAPPED composite reconstructs or discards deck-sheet data; the registered domain has none.
10. That R9 memory writes an event token or a child variable, or that fold inverse non-uniqueness proves ontological erasure. RECOG §6.16c–f distinguishes a fold with type `E` and no registered branch-retaining carrier, B/7-gap with `R_log`, and R9 with `R_ind` but no registered token-specific write-through channel. These are scoped single-dyad results, not birth-law inheritances or TDR-G imports.
11. That the specific symmetric-twin theorem excludes all odd healing generators or resolves OPEN-A. The source retains the odd `tanh` counterexample (§4.2).

---

### 8.1 v0.8 integration guard — source/adoption nonclaims

- `RRF-CND-01` does not establish a new primordial coincidence axiom, physical node identity or admissible node merge. No selected physical `K_3` law or universal prohibition of node-mediated RTG follows.
- The `T_k\leftrightarrow T_{-k}` family conjugacy does not make `S_o`, `S_h`, `-I_{NF}` and `\mathscr O_e` the same physical pole action; RRF OPEN-A stays open.
- The ER-2B additive-carrier continuum is conditional mathematics, not a passive-gauge family of *one* physical triad; quartic drift thresholds do not select a physical carrier.
- RECOG CELL-F4 W1–W5 are missing-interface criteria, not a registered token-to-cochain map, network memory field or birth inheritance law.
- A formally verified finite jet does not supply a global remainder or controlled approximate closure. N=7/8 Stage-2 **global certificate remains pending** on the communicated RER status; no latest executable was inspected.
- RER F3, formal age families, child-free/ambient minima, `w_13`, or candidate factors are not imported as verified RRF scientific theorems or new native profiles.
- `RRF-NET-W-RAW` remains provisional, the `RRF-DYAD-W→RRF-NET-W-RAW` bridge is OPEN and OPEN-B→E1→E2 is unchanged. OFN 3B/3C, NG-7B and physical Genesis/Triadic/OPEN-M selections remain open.

# 9. Change log

- **v0.8.1 — REVIEW CANDIDATE (16 Oct 2026; NOT ADOPTED):** owner-RID-first orientation pin restored to RECOG v0.3.20 §6.6a with OFN v0.9 IMP-O09-03 consumer cross-reference; §2.3 rank-typing guard repinned to adopted OFN v0.9 §4.4 `RTG-OFN-DEF-RANK-TYPING`; prior optional §6.4 RER plan moved to `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md` with one registry pointer; reported formal-G1 identity/uniqueness pointer added strictly as **unverified cross-stream report** with finite-vs-formal distinction; §6.2 separates node exchange from edge-slot exchange and records regularity/clock as **OPEN decisions**. Review refinements: both import tags use the §0 `; RID:` grammar (including the §2.3 table cell); the adopted v0.8 §10 publication paragraph is retained verbatim, with candidate updates in a separate paragraph; §3.1 registers Triadic v1.6 §7.4/CN-05 as a **convention-only proposal** and explicitly records the conditional $Q_c^T=\tfrac{\kappa^2}{4}(Q_s^T)^3$ conversion obligation without applying it. No owner theorem or physical model is adopted, no certificate rerun, no native profile/OPEN closure, and the adopted v0.8 standard and record remain unchanged.

- **v0.8 — ADOPTED as RRF working representation standard (14 Oct 2026):** re-based on the **exact adopted v0.7 file** (57,524 bytes, SHA-256 `2a2b4102ba12e53bc56c746ffe30c553d24ecffa90afddeb4027cd72307717a5`), whose previously finalized header, §0 theorem-source policy and finalization boundary, §2.4 convention label, §5 NG-7A out-of-tag explanation, §9 full release history, and §10 dated source/adoption statements are retained. New receipt blocks cover OFN v0.9, RECOG v0.3.20 orientation/CELL-F4, adopted Genesis v2.8.5 and Triadic v1.6 limits, noncanonical ER-2B and conditional `RRF-CND-01` **contract only**. §6.4 carries RER closure taxonomy as optional `RER-PLAN-ONLY / SOURCE PENDING`, not an imported theorem or physical profile. No proof, mathematical model, native profile, OPEN status, scientific owner or earlier adoption record has been changed. The three reviewer-requested editorial refinements were applied: normalized new-section tags, adopted OFN v0.9 IMP-O09-03 as the immediate orientation-conjugacy pin while retaining RECOG origin, and §6.3 B-token de-duplication by pointer to §4.3. The separate v0.8 adoption record governs this bounded working-standard release; physical realization and RER source adoption remain OPEN.

- v0.7 — ADOPTED as RRF working representation standard (5 Oct 2026): finalized from the reviewer-supported v0.7 draft after three editorial notes. Section 0 makes theorem-source authority explicit; §5 labels `NUMGEN-OPEN-REC-HOL-OPERATOR` as a sub-RID of closed NG-7A without renaming it; the header records working-reference supersession of v0.6 and points to the separate adoption record. Release-state metadata and the existing working-convention label are currentized. No formula, profile, transport law, certificate constant, scientific claim grade, owner RID or OPEN status changes. The reviewed draft, its source-synchronization history, v0.6 and all scientific owners remain unchanged as files. Reviewer correction and the Triadic v1.6 requirement for the pending Wrap-up sync are recorded separately; no Wrap-up/GIIL or consumer file is edited.

- v0.7 DRAFT (5 Oct 2026): source synchronization against RECOG v0.3.14 and NUMGEN v1.20.7. Covered degree-six swap and real-ray comparator provenance now cites the owner's independently reconstructed R11 check 9; no script rerun in this update. R11 CLOSED / R10 accepted receipts, current pins, and the standing refusal of incompatible archival quantities are explicit. R9 retained-memory observable is imported on its exact chart/track and two separate domain/window profiles. VF-1 retains independent written evidence; RECOG's degree-ten non-dependency is recorded without claiming no textual mention. Section/predicate transport is distinguished from event-rule replacement; NUMGEN M2-1 alignment is separated from physical co-realization and WD-DOM closure. The `sinh` twin result is not generalized to all odd shears; `tanh` counterexample retained. No new physical profile, generator, carrier, geometry, birth inheritance, or RRF adoption. Historical v0.6–v0.1 records below are unchanged. Source snapshot and evidence boundaries added in §10.


- v0.6 (25 Sep 2026): independent confirmation of the degree-ten finding received (written verification record `DYAD_CHECK_degree10_even_term_hatF`, Claude / Dyadic DSN editor session; even degrees 2–8 vanish, $[\widehat F]_{(5,5)}\ne0$; integration record by ChatGPT) — PRF-1 renamed VF-1 with `Claude-checked (written verification record); prior report confirmed` provenance; §2.4 six-step and covariance rows now state that the delivered $\widehat F$ has no all-order oddness under naive $-I$ and that $\chi_1$ is not exactly sign-invariant, with $m\ge2$ unclassified; §8.7–8.8 restated accordingly; §0 provenance vocabulary extended; v0.4/v0.5 historical changelog lines unchanged. No adoption decision, no owner DSN change, no closure of OPEN-A or R11.

- v0.5 (25 Sep 2026): v0.4 review applied — reported degree-ten term moved out of the §2.4 profile rows into pending-review finding PRF-1 (§2.4a); "is not odd" / "fails" verdict language withdrawn from profile and §8; $S_h/S_6$ distinction completed at the two remaining use points (§2.2 $S_{{\rm lift},h}$ vs $S_{{\rm lift},6}$; §2.4 uniqueness sentence); §7 heading made versionless. Wrap-up v0.3 synchronisation delegated to the Wrap-up editor (scope A–D in the v0.4 review); not produced here.

- v0.4 (25 Sep 2026): review v1 (RRF03-C01/C02/C03) and audit review v1 applied — $\chi_m$ exact-invariance claim removed and replaced by the exact/formal/polynomial-model/delivered split plus the one-return bound $2C_7\lvert z\rvert^6$; registered swap object fixed as the exact map $S_h$ (involution exact, commutation finite-order), truncation $S_6$ distinguished; `T-h` amplitude row rewritten as pullbacks $h_6^*Q_{\rm prim}$, $(h_6^{-1})^*q$; common-realisation stated as preimages under $h_6$; composite NF → WRAPPED given its local single-sheet inverse with no loss on the registered domain; $C^W_{\rm cov}$ added and "covariance belongs to (observable, action)" recorded for R11; reported degree-ten even term $[\widehat F]_{(5,5)}$ filed as third-party unreviewed; $\mathrm{Fix}_0(T)\subsetneq\{C_{\rm pole}=\pm1\}$ guard added; §1 example uses $\widehat f_{\rm form}$; live `[OPEN: transport]` respelled; anti-correlation source corrected to DYAD §6.4 ISP; definition labels moved out of RID slots with `RID unavailable`; interior import separators removed from table cells; provenance policy reworded (review-routing stage, not a Methodology mandate) and third-party reproduction recorded.

- v0.3 (24 Sep 2026): five bounded corrections from external review of v0.2 — anti-correlation frame and $W_{\rm DSN}$ moved to the wrapped side with the principal-lift condition; formal $\widehat f_{\rm form}$ / delivered $\widehat f_6$ symbols separated and all-order claims scoped to the formal object; $H_\times$ marked not native to `RRF-NET-W-RAW` pending a multiplicative realization; DSN v1.3 tag grammar normalised throughout with RID pins (RECOG-OPEN-QUINTIC-FRAME, DYAD-THM-NF-INV radii); swap table split into transport-established identity (NF ↔ W ↔ LIFT) versus OPEN-A proper (physical relabeling, WRAPPED). B3 wording fixed to degree-$\le6$ uniqueness of $h_6$. Status raised to candidate working standard.

- v0.2 DRAFT (24 Sep 2026): ten bounded corrections from external review — DSN v1.3 status grammar; source pin to ADOPTED DYAD v6.4.10; one-step $\widehat f$ / six-step $\widehat F$ separated; bookkeeping reorientation $\mathscr O_e$ separated from $S_6$; `T-net` set to `[OPEN: bridge]`, network symbols typed $W_e^{\rm net}$; closure made a branch statement; comparator transport direction fixed (W → NF); $T_{\exp}$ closure with radial part, coherent vertex gauge for $H_\times$; cycle-table scope; $C_\pm$ branch conditions. From DYAD v6.4.10 check: `RRF-DYAD-W` pinned to the lifted $\mathcal L$-frame with $Q_{\rm true}$ registered as a projected wrapped observable; SG-19 pin and non-transferable quantities; $S_6$ uniqueness under the adopted normalizer convention; $E_{\rm odd}/F_4$ six-step parity import; symmetrisation-order guard; domains pinned to DYAD-THM-NF-INV / NF-REM.
- v0.1 DRAFT (24 Sep 2026): initial registry.

---

# 10. Source identity and reproduction boundary (5 October 2026)

This is the preserved source-synchronization snapshot, not the adoption manifest. Source versions and historical dates inside them are unchanged. The finalized registry, reviewed draft and separate record are identified in `RTG_RRF_REPRESENTATION_REGISTRY_v0_7_ADOPTION_RECORD.md`; the source hashes below are retained verbatim.

| Supplied source | SHA-256 | Role in this update |
|---|---|---|
| `RTG_RRF_REPRESENTATION_REGISTRY_v0_6.md` | `7a31357729e1561c600673cf673c785b645666ae65d8280ebbaf9b57722d6b89` | Preserved revision base, no overwrite |
| `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_14.md` | `d10c2a988bd1dcaf0c673ad6951efec3245275ee65a0d341f44335cfc7904b43` | Full owner-ledger reading; current result/status source |
| `RTG_NUMBER_GENESIS_DSN_v1_20_7.md` | `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` | Full owner-ledger reading; current partial-composition guard |
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md` | `7455811928606076b3bc3075632275dc2a24e37fdbf0ae20036db5529a1b56b7` | Unchanged owner; fixed chart, constants and scopes |
| `DSN_METHODOLOGY_v1_3.md` | `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e` | Governing status/import/owner rules |
| `RTG_ONTOLOGICAL_FOUNDATIONS_v0_8.md` | `56bc991d28c4a6f3e841eec5ac8c4550528fbaac91bcfc23ab0dc2540bd2a514` | Unchanged ontology; no new physical identification |
| `RTG_PROGRAMME_OVERVIEW_v1_2.md` | `4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359` | Unchanged programme routing; current inventory still requires owner sync |

**R11 evidence pin, as printed by the owner:** `RECOG-ART-R11-LEDGER` → `recog_r11_chart_ledger_cert.py`; SHA-256 `a4950ed525f2e6ee4be0ddd7f9607b2c3c14d8e31052a88db6ae163fa5d6e5e5`; 11-check certificate, with check 9 as the swap/covariance evidence. The executable is not present in this update's mounted files, so this hash is **source-reported**, not locally authenticated against script bytes. The ledger's attribution to Claude is the basis for the covered reviewer-stage update.

**Unavailable for a new artifact-level rerun:** the current R11, R9, R8/B3, symmetric-twin and F2 certificate packages, the original P2-B v2 evidence archive and full `certificate.json`, and the original independent degree-ten package. Some older algebra/referee files are mounted, but none was executed here. Written owner records and the existing VF-1 verification note are not replaced by inferred script results.

**Separate files not edited:** RECOG retains RRF v0.4 convention pins in §6.14/§7, and its companion/source table contains other older pointers. Any owner update must distinguish a historical pin from a current dependency; this registry cannot rewrite the upstream record. NUMGEN already references RRF v0.6 as noncanonical, no theorem import. Its pointer change occurred at v1.20.5; v1.20.7 additionally adopts M2-1 and records Census-1. The Wrap-up and Genesis Identification & Inheritance Ledger need their own source synchronization; no version of either is created by this registry release. Their recent Markdown copies are not mounted in this update, so this document does not claim to have edited or reread those absent files.

**History and adoption:** original v0.6, the reviewed v0.7 draft, the source-synchronization review and all scientific owners are left byte-for-byte unchanged. This release records RRF working-standard adoption only. Imported source closures do not administratively close RRF OPEN-A/B/E, create an independent pole-identification field, imply consumer acceptance, or constitute a separate PI/owner adoption of an imported scientific ledger. The actual decision scope, provenance and pending work are in the separate adoption record.

### 10.1 Additional v0.8 source inventory and adopted-baseline authentication

The §10 table is the **unchanged dated v0.7 source-synchronization snapshot**, not a claim that historical source versions were reread as current. The following are additional inspected or communicated sources for v0.8. SHA-256 values are recorded in the separate v0.8 adoption record and QA manifest where inspected; source reports are not execution attestations.

| Source | Record type / evidence boundary |
|---|---|
| `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md` | Adopted OFN owner; current covariance / complete-state / RF-O09 guards; no rerun |
| `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_20.md` | Freeze candidate; §§6.6a/6.16b/6.16g source-checked; no local replay of its certificates |
| `RTG_GENESIS_GEOMETRY_DSN_v2_8_5.md` | Adopted Genesis corrections; scoped interpretations |
| `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6.md` | Adopted Triadic consumer; existing source unchanged |
| `RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md` | Conditional noncanonical mathematical study; not selected physics |
| `RTG_RRF_RESPONSE_TO_OFN_COINCIDENCE_v0_2.md`, `RTG_RRF_COINCIDENCE_ADMISSIBILITY_REVIEW_v0_1.md` | Earlier noncanonical scoped RRF audits |
| `RTG_RRF_REPRESENTATION_REGISTRY_v0_7_ADOPTION_RECORD.md` | Records adopted hash/size and separate working-standard scope; the **mounted adopted v0.7 file** matches 57,524 bytes and the full SHA-256 |
| `RTG_RRF_REPRESENTATION_REGISTRY_v0_7_DRAFT.md` | Historical draft retained unchanged; adopted final authenticated separately before the adopted-v0.8 merge |
| RER proposed v0.2 / F3 / formal age / N=7/8 Stage 2 | **NOT READ / NOT MOUNTED**; user plan only, no owner-RID or numerical certificate upgraded |

**Publication and adoption boundary (14 October 2026):** the adopted-final v0.7 base authentication, complete v0.7 → v0.8 unified diff, reviewer acceptance of the scoped interface text and the three requested editorial refinements are recorded. The **separate v0.8 adoption record** authorizes the replacement working standard at RRF scope only. §6.4 remains non-normative `RER-PLAN-ONLY`, source pending; no scientific-owner file, physical profile or scientific OPEN status is changed.

**v0.8.1 review overlay (16 October 2026; not adopted):** the §6.4 extraction into a separate RER proposal and the owner-RID/typing/identity source corrections are changes proposed **after** the adopted v0.8 release. This paragraph records the candidate delta only; it does not retroactively edit v0.8 publication history or adoption scope.

**Byte provenance:** the **mounted adopted v0.7 file** was validated against the independently recorded full SHA-256 and 57,524-byte length; its historical twelve finalization sites remain documented in the separate v0.7 adoption record. This is a byte-identity check, not a new scientific-source review or certificate rerun.
