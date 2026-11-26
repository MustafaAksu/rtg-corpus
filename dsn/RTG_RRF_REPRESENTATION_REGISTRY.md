# RTG — RRF Representation Registry — v0.9

**Title:** RTG — RRF Representation Registry
**Version:** v0.9
**Date:** 26 November 2026
**Scope:** Isolated continuous dyad (four profiles) and one provisional network profile; working representation standard only.
**Document class:** Infrastructure / representation registry; declared nonstandard section map (§0). §1 is equation-annotation syntax rather than a 200–400 word state summary.
**Document status:** DRAFT — S2b review candidate; not adopted. `rrf-v0.8.4` governs until the PI adoption and release.
**Supersedes:** RTG_RRF_REPRESENTATION_REGISTRY.md at `rrf-v0.8.4` (SHA-256 `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce`), proposed successor only.
**Companion documents:** §0.2 current-source table and §7 import/use records; historical PRR Wrap-up v0.2 §§20, 26 (NONCANONICAL parent).
**DSN Methodology:** `methodology-v1.4`.
**Status summary:** The registry produces no new physics; it makes representation mistakes of the R11 type mechanically visible. All dyad statements are conditional on the postulated generator T. OPEN-A/B/E remain ACTIVE.

# 0. Purpose, scope, status grammar, lock

**Section map:** §0 scope, evidence discipline and current state; §1 equation syntax; §§2–5 profiles, transport, comparators and cycles; §6 interface contracts and OPEN register; §7 owner uses, consumers, evidence and unregistered objects; §8 standing scope guards; Appendices A/B change and correction routing.
**Purpose.** Fix, for every representation profile in current RTG dyad/network work, its native objects, transport arrows to the other profiles, observable status (native / transported / re-defined / projected), the pole-relabeling candidate action in that profile, and what each transport loses. The registry produces no new physics; it makes representation mistakes of the R11 type mechanically visible.

**Theorem-source policy.** The registry records track, domain, typing and transport conditions; it does not maintain an independent authoritative theorem ledger. Any formula excerpt, including §4.1a, is imported for orientation, not restated authoritatively: the cited scientific owner governs. Such an excerpt is not a precedent for transferring theorem ownership to RRF.

**Scope.** Isolated continuous dyad (four profiles) and one provisional network profile. Discrete (TDR-G) state representation is not registered (§7). All dyad statements are conditional on the postulated generator $T$ (DYAD SG-14).

**Status grammar (Methodology v1.4).** §§0.6, 3–5, 12.2 govern. Claim status, model assumptions, physical interpretation, evidence, OPEN lifecycle and document adoption are independent. Retain owner `[DEF]`, `[ALG]`, `[THM]`, `[NUM]`, `[HYP]`, `[OPEN]`, `[RESULT] [from: …]` and `[COR]` distinctions; an artifact identifier is not a theorem RID. `RID unavailable` identifies an unnumbered owner statement without inventing a RID or borrowing an OPEN ID as a theorem ID. Exact source versions, local use, inherited scope, depends-on and verification belong to the import record. Historical syntax is a migration input; reference-only use is distinct from scientific import.

**Provenance vocabulary.**
- `owner-adopted`: retained for adopted DYAD v6.4.10 results. This source-provenance label does not itself establish RRF adoption or certify later downstream interpretations; the registry adoption decision is recorded separately.
- `Claude-checked as recorded by RECOG`: a written owner-ledger record attributes an independent reconstruction to Claude. For the covered swap identities, the source is RECOG v0.3.14 §6.14, certificate check 9, `RECOG-ART-R11-LEDGER`. This update reads that source; it does **not** rerun its script or authenticate an absent executable against its printed hash.
- `algebraic consequence of imported definitions/results`: e.g. a general two-input cubic expansion derived from the registered $s_2=2h_2$. It is not silently described as an additional case independently executed by the source's check 9.
- `Claude-checked (written verification record); prior report confirmed`: the separate degree-ten record already carried in VF-1. Its evidence is not upgraded by importing RECOG's degree-six check.
- `Claude-checked`: retained for earlier discussion-local derivations expressly attributed that way; no new execution is asserted here.
- Historical labels `participant-rechecked; third-party reproduced; Claude-check pending`, `(ext.)`, and `third-party reported; unreviewed` describe the earlier evidence state. The covered swap-commutator and real-ray comparator records no longer await that review, because RECOG records it. Any other claim needs its own matching evidence; this is not a blanket removal of provenance obligations.

**Representation safety lock (provisional, until OPEN-E).**

> All triad/network equations are written in profile `RRF-NET-W-RAW` with profile-typed symbols $W_e^{\rm net}$. $z_{\rm NF}$ appears in network work only inside an explicitly transported single-dyad subexpression. No closure, incidence, comparator or holonomy law is transferred between profiles without a registered transport arrow. The identification `RRF-DYAD-W → RRF-NET-W-RAW` is `[OPEN] [scope: bridge]`; notational similarity does not establish object identity.

Rationale: single-dyad normalisation turns linear closure $\sum_e\epsilon_{\gamma e}W_e=0$ into $\sum_e\epsilon_{\gamma e}h(z_e)=0$, not $\sum_e\epsilon_{\gamma e}z_e=0$ (Wrap-up §19).

### 0.1 Retained proof-source receipts and dependency boundary

| Owner record inspected | State used by this registry | Boundary |
|---|---|---|
| RECOG v0.3.14 §6.14 / §2 R11 | R11 is CLOSED as the typed final-chart ledger; DYAD enclosure inputs accepted | Physical pole relabeling remains RRF OPEN-A. The standing non-transfer/refusal line is not removed by R11 closure. |
| RECOG v0.3.14 §6.13a | R9 exact-map retained memory and comparator-incompleteness corollary are theorem-grade on the declared $C_z$ track and amplitude windows | Not a theorem for every comparator track, every amplitude, event selection, or birth inheritance. |
| RECOG v0.3.14 §6.16a–f | Representation-safe token transport and separate classifications of transition, retention, and write-through | Definitions of tokens/carriers do not identify them with birth events. No new history carrier is created by registering them. |
| NUMGEN v1.20.7 §6.6 | M2-1 transported chain identity adopted at algebra grade; Census-1 INCONCLUSIVE / INCONCLUSIVE; interface-typed WD-DOM still OPEN | A context transport does not create co-realization, outer admissibility, or an admitted composable chain. |

**No circular scientific import.** RECOG imports the RRF's notation and convention only; its §6.14 finite algebra is independently reconstructed from the specified generator and adopted DYAD chart. This registry cites that algebraic evidence, not its own earlier convention as a proof. RECOG's internal RRF v0.4 pointers have not been edited here. NUMGEN's RRF v0.6 pointer is likewise explicitly noncanonical and imports no theorem. The source status of RECOG v0.3.14 is not promoted to an unrecorded owner/PI freeze decision by this receipt.

---

### 0.2 Current source receipts and inheritance/representation boundary

Accepted S1 matrix `records/rrf/RRF_S1_SOURCE_INTERFACE_MATRIX_20261126.md` at `2c087763e94ac23768c8b778aecc3bb8a57e508d`, reviewer readback `6074506269` (§5 verdict), governs the proposed synchronization. Current source checks are distinguished from retained load-bearing and historical proof pins; no owner certificate replay.

| Current source | Claim/interface check | RRF boundary |
|---|---|---|
| DYAD v6.4.24 | §§6.9, 6.14–17; NF-INV/REM, fixed-h6 VF-1, formal and smooth involution, smooth equivariant chart | OPEN20 B-∞ existence/flat uniqueness CLOSED, B-an/B-6 ACTIVE; no physical G2, no finite-chart bounds on smooth Φ. |
| RECOG v0.3.27 | §§6.6a, 6.13a–b, 6.14, 6.16; R11, R9, W1–5 | Baseline rows and historical evidence pins retained; additive sharper rows separate; no physical swap, raw-track extension or inheritance. |
| OFN v0.13 | §5.5; OFN11-C01/C02; RTG-OFN-DEF-STANDARD-C and RTG-OFN-DEF-TRIAD-MODEL-CONTRACT; RF-O10-01/02 | Corrected test/contract, realized smooth mathematical candidate family; SESSION properties not registered, physical selection OPEN. |
| GEN v2.10 | §6.3c G-20; gen-v2.8.9 theorem/proof pin retained | Conditional six-step real C³ factor theorem; separate primitive ALG; C2 nonvacuous in smooth chart, analytic and physical realization OPEN. |
| NUMGEN v1.22 / TDRG v2.13 | NUMGEN §§6.4,6.6,6.8; TDRG-DEF-ORIENT | Historical M2-1, deck/NG-7A pins retained; P2 answered, M-4 HOLD for missing-chain design. No discrete profile or physical composition. |
| GEN v2.10 / TRIAD v1.7 | GEN §1/2/6.3c/7, TRIAD §6.18/7.4 CN-05 | Same-vector metric convention and unit direction vs loaded child, no physical bridge or unique lowering. |
| ER-2B v0.2 / RRF coincidence reviews (noncanonical) | Named projected-map conditional examples | Physical exclusion requires complete-state action, fixed-state witness, encoding and clock (§6.2); no re-audit. |
| RER v0.2 ADOPTED (NONCANONICAL) | G7–10; 18 accepted scoped records, 2 excluded; Stage-2 source limits | Closure proposal nonnormative, global certificate pending, no owner theorem or native profile. |
| UVM v0.7.2 / Programme v1.5 | OPEN-M-6/SG-M-7/§7; IF29–33 | Typing reference only; no UV profile/transport or automatic consumer repin. |

Dated provenance and proof-source pins are distinct from the current-use table (see §§0.1, 7.3). The updated live RECOG uses in §§2–4, 6.3 are checked at v0.3.27; proof evidence at v0.3.14 and v0.3.20/21 is retained as such. DYAD v6.4.10/12/13/18, GEN v2.8.9 and NUMGEN v1.20.7 retained proof/source pins are not silently superseded. OFN's v0.9 covariance/rank-typing source and v0.10 readout history remain traceable; amended contracts use ofn-v0.13. See §7.2.

OFN v0.13 retains RF-O09-03/04; the old v0.9 locator remains a historical receipt (recovered `upload/corpus-originals-20261123/RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md`, blob fefb1549f80ff4637ed67a69aea354711f7234e1, targeted text read; no ofn-v0.9 tag asserted). TRIAD v1.7 §6.15, SG-15 remains operative: unit direction, policy-scaled child and source operator are distinct; no-gain bound requires the declared coherent source construction and real weight 0≤g2≤2. These references do not select physical source, carrier or node-coincidence axiom.

### 0.3 Model/carrier versus passive-chart safety rule

**Local candidate identity:** `RRF-DEF-PASSIVE-TRANSPORT` — passive transport / reimposed-model distinction; registration awaits adoption.
`[DEF] [scope: RRF representation discipline; conditional ER-2B illustration]` A **passive** diffeomorphic recharting transports the state, update, exchange action, incidence/closure operator, event predicate and comparison subset together. It retains the same model, so correctly transported fixed-set noninvariance cannot disappear. **Reimposing** linear addition, projection or incidence in the new coordinates creates a *different conditional model* unless an intertwining equivalence is proved. This distinction already exists in §§3/6; ER-2B v0.2 C15A–C20 supplies a bounded illustration, **not** a physical threshold or native RRF network profile.

`[OPEN] [scope: non-transfer guard; physical bridge not selected]` `RRF-DYAD-W` and `RRF-NET-W-RAW` remain distinct types; additive closure of the latter is not automatically transported from isolated dyads. Neither a coordinate change, a source identification, nor a finite-order factor is evidence of a chosen physical carrier, incidence law or birth mechanism. OPEN-B → OPEN-E1 → OPEN-E2 remains locked.

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
| Native dynamics | $T:\ \rho'=\rho-\sin\eta,\ \eta'=\eta+e^\rho-1-\sin\eta$ `[import: DYAD v6.4.24 §1; RID: DYAD-DEF-PRIMITIVE-MAP] (historical v6.4.10 source receipt)` |
| Native observables | lifted differences $(\Delta\rho,\Delta\eta)$ along a trajectory; lift fixed points $(0,m\pi)$, $m\in\mathbb Z$; zero-winding cylinder representatives $P_1=(0,0)$ elliptic order-6 and $P_2=(0,\pi)$ hyperbolic saddle. Additional wrapped-cylinder winding fixed points $(\log(1+2\pi k),0)$, $(\log(1+2\pi k),\pi)$ occur for $k\ge1$; on the lift these advance by $2\pi k$, not fixed. Source: DYAD v6.4.24 §1 fixed-point scope (unnumbered), RECOG v0.3.27 §6.3; historical receipts DYAD v6.4.10 and RECOG v0.3.14. $\det J=1+(e^\rho-1)\cos\eta$ (DYAD-ALG-NOT-AREA-PRESERVING, DYAD v6.4.24 §1). Guard: $\mathrm{Fix}_0(T)=\{P_1,P_2\}\subsetneq\{C_{\rm pole}=\pm1\}$ in the zero-winding representative sector — fixed comparator value is not a fixed state (e.g. $T(a,0)=(a,e^a-1)$ with $C_{\rm pole}=1$); RECOG v0.3.27 §6.3, unnumbered statement (RID unavailable). |
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
| Domain | inverse-coordinate domain of DYAD-THM-NF-INV: $h_6$ injective on $\lvert z\rvert\le\tfrac1{10}$ with $\tfrac{15}{16}\lvert z\rvert\le\lvert h_6(z)\rvert\le\tfrac{17}{16}\lvert z\rvert$, $h_6^{-1}$ exists on $\lvert W\rvert\le\tfrac9{100}$ (majorant $M(s)$, $H(s)=s+M(s)$); remainder domain of DYAD-THM-NF-REM with radius-indexed profiles $(r,C_7)=(\tfrac1{20},100)$ or $(\tfrac1{40},30)$, never mixed; **local only**. Baseline derivative ceilings C_D=1000,250 respectively. Current owner check DYAD v6.4.24 §6.14. Separate `DYAD-THM-NF-REM-C7-SHARP` ceilings C7=85.1,27.7 on the same respective chart/radii/norm, no C_D re-derivation or change to existing proof constants |
| One-step objects (two symbols) | **Delivered:** $\widehat f_6=h_6^{-1}fh_6$, exact analytic map on its proved domain, finite jet $n$ with $\mathcal J_{\le6}(f\circ h_6-h_6\circ n)=0$. **Formal:** $\widehat f_{\rm form}=h_{\rm form}^{-1}fh_{\rm form}$, the formal Poincaré–Dulac normal form; contains only resonant monomials $z^p\bar z^q$, $p-q\equiv1\ (\mathrm{mod}\ 6)$ — hence all of odd degree. $h_6=\mathcal J_{\le6}h_{\rm form}$ under the shared convention. |
| One-step symmetry | Formal: $\widehat f_{\rm form}(\lambda z)=\lambda\widehat f_{\rm form}(z)$, hence $\widehat f_{\rm form}(-z)=-\widehat f_{\rm form}(z)$, $-1=\lambda^3$ `[ALG] [scope: formal all-order] [provenance: Claude-checked (resonance argument)]`. Delivered: only $\mathcal J_{\le6}\big(\widehat f_6(\lambda z)-\lambda\widehat f_6(z)\big)=0$ `[ALG] [scope: degree ≤ 6]`; all-order equivariance of the exact analytic $\widehat f_6$ is **not** established by the certificate. |
| Six-step object | $\widehat F=h^{-1}F_Wh$, finite jet $J(z)=z+\mu z^2\bar z+a_{32}z^3\bar z^2+a_{05}\bar z^5$; linear part identity; certified remainder $\lvert\widehat F-J\rvert\le C_7\lvert z\rvert^7$ `[import: DYAD v6.4.10 §6.14; RID: DYAD-THM-NF-REM]`. $E_{\rm NF}(z)=\widehat F(z)-z=\mu\lvert z\rvert^2z+O(5)$; its jet $J$ is odd (finite order), the formal six-step normal form is odd; this exact map (fixed finite $h_6$) has **no all-order oddness under the naive $-I$ action**: the verified fixed-chart degree-ten parity obstruction is recorded separately as finding VF-1 (§2.4a); the jet and remainder certificates are unaffected and the profile remains valid. **$\widehat f$ and $\widehat F$ are different maps; $n$ and $J$ are different jets; neither is an all-orders identity (SG-19).** |
| Native observables | $q=\lvert z\rvert^2$; self-return multiplier $\chi_m(z)=\widehat F^{\circ m}(z)/z$, defined for $z\ne0$ and admissible iterates (extension at $0$ stated separately); NF comparator $C_z(a,b)=\bar z_az_b$ |
| Source-derived history/limit observable | $\Psi=\Theta-\tau\log q$, $\tau=2\sqrt3/3$, with the continuous along-orbit lift of $\arg z$; $\mathcal M(z_0):=\Psi_\infty-\Psi(z_0)$ denotes RECOG's $M$ (renamed typographically here to avoid collision with the coordinate majorant $M(s)$). Defined for the exact return $\widehat F$, not a lattice-free comparison model `[import: RECOG v0.3.14 §6.13a; RID: RECOG-THM-R9-MEMORY]`. This is an imported derived observable with its own source theorem, not a newly appended independent state coordinate; track/domain and token limitations are in §4.1a. |
| Observable status | $q$, $\chi_m$, $C_z$ **native / re-defined**; $Q_{\rm prim}=\lvert h(z,\bar z)\rvert^2$ and $C_W\!\mid_{\rm NF}=\overline{h(z_a)}\,h(z_b)$ **transported** |
| Relabeling candidate | $z\mapsto-z$: exact symmetry of $\widehat f_{\rm form}$; degree-6 certified for $\widehat f_6$. $h_6$ is the unique solution of the specified homological recursion through degree 6 under the zero-resonant-coefficient convention, so the exact map $S_h=h_6(-I)h_6^{-1}$ and its truncation $S_6=\mathcal J_{\le6}S_h$ carry no residual-gauge ambiguity at degree $\le6$ `[ALG] [scope: degree ≤ 6] [conv: DYAD-ALG-NF6]`. Canonicity under other normalizer conventions and at all formal orders is not supplied by this fixed-chart registry and remains `[OPEN] [scope: other normalization classes]`. This is not an unclosed R11 task: the completed R11 ledger pins the adopted chart and routes physical pole identification to RRF OPEN-A `[import: RECOG v0.3.14 §6.14; evidence RID: RECOG-ART-R11-LEDGER]`. |
| Formal involution — **owner-adopted, formal only** | `R_0=T^3F^{-1/2}=\widehat h(-I)\widehat h^{-1}` is the **unique formal** `−I`-linear involution commuting with `F=T^6` and it also commutes formally with primitive `T` `[THM] [scope: formal only] [import: DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]`. The delivered **finite** $S_h=h_6(-I)h_6^{-1}$ is exactly involutive and equals `R_0` only through jet degree six under the shared normalizer convention; exact dynamical commutation is **not** established for $S_h$. Analytic existence/convergence remains **OPEN 20 (B-an/B-6)**. **C∞ existence CLOSED** (DYAD v6.4.24 §6.17 `DYAD-THM-SMOOTH-EMBEDDING`, producer v6.4.18 E1–E4); v6.4.13 F1–F3 classify existing smooth germs/roots. The smooth commuting R is not the finite S_h and inherits none of its finite-chart radii or bounds (§2.4b–c). Physical G2 and OPEN-A remain OPEN. |
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

`[ALG] [scope: fixed adopted h_6; exact Taylor computation through total degree 10] [import: DYAD v6.4.12 §6.14; RID: DYAD-ALG-NF6-DEG10] [provenance: Claude-checked (written verification record `DYAD_CHECK_degree10_even_term_hatF`, Dyadic DSN editor session, 25 Sep 2026; same exact $\mathbb Q(i\sqrt3)$ engine as the v6.4.10 referee, independent of the third-party code); prior report (PRR_RRF_REVIEW_v1, third reviewer) confirmed including the "first even term is degree ten" part; integration record RTG_RRF_DEGREE10_REVIEW_INTEGRATION_v1 (ChatGPT, inspection only, no re-execution)]`.

**Consequences (verified scope only).** $\widehat F(-z)+\widehat F(z)\not\equiv0$ and $\chi_1(-z)-\chi_1(z)\not\equiv0$ for $z\ne0$: an identity failure, not a pointwise-nonzero defect, not a positive uniform lower bound, and not a statement about $\chi_m$ for $m\ge2$ (not computed). Reading: the parity in question is that of the dynamics **as represented with the fixed truncated $h_6$ under the naive $-I$ action**; a degree-6 truncated normalizer is not expected to preserve normal-form parity beyond its own order, the even content re-entering at the first order where the truncation error of $h$ feeds back into the return. This is a property of the delivered chart/action pair, not a statement that the primitive dynamics lacks symmetry under every local involution.

**Unchanged by VF-1:** the formal all-order normal form (odd by $p-q\equiv1\bmod6$); the odd jet $J$; DYAD-THM-NF-REM ($C_7$, $C_D$) and DYAD-THM-PRIM-CTR; the one-return bound, now known to be non-vacuous: $\lvert\chi_1(-z)-\chi_1(z)\rvert\le200\lvert z\rvert^6$ on $0<\lvert z\rvert\le\tfrac1{20}$, $\le60\lvert z\rvert^6$ on $0<\lvert z\rvert\le\tfrac1{40}$ (profiles unmixed; VF-1 does not sharpen these constants or radii); $S_h^2=I$; RRF OPEN-A. R11 is now closed by its separate owner record; VF-1 neither supplies nor withdraws that closure. The covered degree-six provenance is upgraded by RECOG check 9, not by VF-1. Current owner check DYAD v6.4.24 §6.14 `DYAD-ALG-NF6-DEG10` (historical v6.4.12 proof pin retained). S0 recovered the written degree-ten note at SHA-256 `dcfd808c0270202768b4422acb474cda08f693a1cf69e8ec368e7faac414f4d4`, in DYAD upload custody. `PRR_RRF_REVIEW_v1.zip` remains missing; `upload/dyad-sources/DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` (121,396 bytes; SHA-256 `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4`; EV-BYTES, EV-HASH at S2a correction) is present. Its internal `outputs/certificate.json` and the certificate adequacy were not re-audited or rerun in this correction. EV-NOT-RERUN; no new degree-ten computation.

**RECOG dependency note (v0.7 synchronization).** RECOG v0.3.14 §7 explicitly excludes the degree-ten result from its scientific inputs; its RRF import is convention-only. Section 6.16f nevertheless mentions VF-1 descriptively when warning that chart-symmetry germs do not justify an all-orders analytic gauge. Therefore the precise receipt is **not a load-bearing theorem/certificate premise**, not “absent everywhere.” Check 9 is not a new degree-ten verification. VF-1 retains its existing written-verification provenance unchanged.

### 2.4b Formal involution and local existence (not a new profile)

`[THM] [scope: formal germs for F=T^6; owner-adopted] [import: DYAD v6.4.12 §6.16 #sec-6-16-centralizer; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]` The formal object

\[
R_0=T^3\circ F^{-1/2}=\widehat h(-I)\widehat h^{-1},\qquad F=T^6,
\]

is the **unique formal involution** with derivative `−I` commuting with `F`; it commutes formally with primitive `T`. The tangent-to-identity formal centralizer is the one-parameter family `exp(s log F)` `[import: DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-CENTRALIZER]`. The kernel lemma over **all homogeneous degrees** is `[import: DYAD v6.4.12 §6.16; RID: DYAD-ALG-CENT-KERNEL]`. The lifecycle `DYAD-OPEN-FORMAL-CENTRALIZER` is **CLOSED (formal)** by this owner release; this is not RRF OPEN-A closure.

`[DEF] [scope: finite-versus-formal refusal]` The delivered `S_h=h_6(-I)h_6^{-1}` is an **exact involution of the finite polynomial chart** with only degree-six **dynamical commutation** established. In the shared normalization convention `J_{≤6}R_0=J_{≤6}S_h=S_6`; no exact equality `R_0=S_h`, analytic convergence or physical pole exchange follows. VF-1 (`DYAD-ALG-NF6-DEG10`) concerns the fixed finite `h_6` chart only; it does not obstruct a different analytic or smooth odd chart. The owner §6.15 specifies `DYAD-THM-LOCAL-INVOLUTION-GERM` for primitive `C¹` and six-step `C³` involutions, with appropriate invariant/tube domains. Current DYAD v6.4.24 §6.15 `DYAD-THM-LOCAL-INVOLUTION-GERM`: lifted open neighborhood V, involution R:V→V; commutation defined on common D_Φ with 0 in its interior. Primitive C^k, k≥1, V in strip abs(η)<π; six-step k≥3, V contained in U_T∪{0}. Nonidentity germ has derivative −I and is locally conjugate to −I. Identity branch distinct; no physical action.

`[THM] [scope: conditional real-analytic local germs] [import: DYAD v6.4.12 §6.15 #sec-6-15-involution; RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE]` A nonidentity **analytic** local involution commuting with `F=T^6` under the §6.15(b) hypotheses has derivative `−I` and commutes **exactly** with primitive `T`. A `C^∞` six-step involution has the same formal jet as `R_0`; **adopted DYAD v6.4.13 §6.17 F1 now upgrades this to exact primitive commutation** on its stated domain. The §6.15 analytical result remains a distinct earlier owner theorem. Network factor hypotheses `EF=TE` and `EF=T^6E` are still **different contracts**. `[import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]`

`[OPEN] [import: DYAD v6.4.13 §§2, 6.16–6.17; RID: DYAD-OPEN-INVOLUTION-REALIZATION]` **OPEN 20 (B-an):** analytic convergence of `R_0`/`F^{1/2}`; **(B-6):** analytic convergence of `F^{1/6}` / `J`; **(B-∞ existence): CLOSED** for local C∞ germs by DYAD v6.4.18 E1–E4; current DYAD v6.4.24 §2 OPEN20 PARTIAL, B-an/B-6 ACTIVE. `[THM] [scope: DYAD v6.4.13 §6.17 existing C∞ germs; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]` **B-∞ flat uniqueness CLOSED** for existing germs by Lemma F and F1–F3. These are distinct from the unknown existence outcomes. Owner RIDs `DYAD-CAND-FLAT-CENTRALIZER` and `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` retain their historical spelling despite [THM] grade.

**Local candidate identity:** `RRF-ALG-ODD-ROOT-EQUIVALENCE` — conditional class-wise local existence equivalence; registration awaits adoption.
`[ALG] [scope: class-wise local existence equivalence, conditional on the owner clock/root results; not a physical realization] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES] [import: DYAD v6.4.13 §§2, 6.16; RID: DYAD-OPEN-INVOLUTION-REALIZATION]` In each of C∞ and analytic categories, a nonidentity primitive-commuting involution (equivalently an odd chart for primitive `T`) exists **iff** a tangent-to-identity square root `Q²=F` exists in that category. The easy direction is `Q=T³R`; the reverse uses F3 for C∞, and the analytic special case of F3 (or formal-root uniqueness plus analytic identity) for Cω, with `R=T³Q^{-1}`. The existence equivalence is an algebraic *consequence* of owner theorems plus the explicitly defined averaging chart (G2 v0.3 §4); it does not establish existence by itself. E1–E4 supply smooth existence separately; analytic existence remains OPEN. No G2 physical factor/encoding is claimed.

**Current smooth existence (DYAD v6.4.24 §6.17; producer v6.4.18 N14).** `[THM] [import: DYAD v6.4.24 §6.17 | DYAD-THM-SMOOTH-EMBEDDING] [scope: C∞ germs at P₁; §6.15 local domain]` E1 supplies a smooth field `X` with `F=T⁶=φ_X¹`, `j∞X=log F`; E3 gives existing smooth tangent-to-identity roots `K_m=φ_X^{1/m}` commuting with `T`; E4 gives an existing smooth `J=T K_6^{-1}` and `R=T³ K_2^{-1}`. Hence **OPEN 20 B-∞ EXISTENCE CLOSED**; B-an/B-6 analytic existence remains OPEN, as does physical G2/OPEN-A. E2 uniqueness is restricted to smooth time-one generators with `DX'(0)=0`—not all generators. The owner construction passes by `G_∞^{-n}F^n`; convergence of the prior `F^{-n}R_∞ F^n` scheme remains unproved. L-SHADOW-POLY is not used. The radius is qualitative; finite-C^r exact commutation and physical exchange/G2 remain unestablished.

### 2.4c Formal ℤ₆ and smooth centralizer

`[THM] [scope: formal only] [import: DYAD v6.4.13 §6.16; RID: DYAD-THM-FORMAL-Z6-GENERATOR]` The canonical formal generator `J=T∘F^{-1/6}` has order six and linear part `A`; `R_0=J³`, `G=J²`. **OPEN 20 B-6** concerns its analytic realization. **B-6 ⇒ B-an** and **B-6 ⇔ B-an ∧ B-3** `[ALG] [import: DYAD v6.4.13 §6.16; RID: DYAD-OPEN-INVOLUTION-REALIZATION]`; whether B-an alone entails B-3 is not established. A finite or formal generator is not a chosen physical pole/triad action.

`[THM] [scope: DYAD §6.17 forward-invariant ball and flat contact; existence not asserted] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-FLAT-CENTRALIZER]` Owner Lemma F states that an `F`-commuting map flat-close to identity is identity on its stated local ball; the RID spelling `CAND` does not indicate its adopted `[THM]` grade.

`[THM] [scope: conditional on an *existing* C∞ germ/root, owner §6.15 domain and §6.17 hypotheses] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]` F1: existing nonidentity six-step involution commutes exactly with primitive `T`; F2: it is unique; F3: existing tangent-identity roots of `F` commute with `T` and are unique. Analytic results are included as a regularity subclass; no convergence or realization is inferred. These theorems do **not** identify physical `σ`, edge encoding `E`, or `EF=TE` with `EF=T⁶E`. Existence of the smooth germs is discharged by E1–E4; B-an/B-6 OPEN. The finite-C^r analogue remains unresolved.

`[DEF] [scope: representation and owner boundary]` The physical-clock field remains required even when a C∞ involution commutes with both local clocks: a dynamical factor from network update to `T` is different from a factor to `T⁶`. The separate noncanonical G2 v0.4 review will maintain the full gate contract.

`[THM]` [import: DYAD v6.4.24 §6.17 | DYAD-THM-SMOOTH-EQUIVARIANT-CHART] [scope: real C∞ local germs at P1] For the E4 germ J the average Φ=(1/6)Σ_(k=0)^5 A^(−k)J^k is a local C∞ diffeomorphism fixing 0 with DΦ(0)=I, ΦJ=AΦ; N_Φ=ΦTΦ^(−1) commutes with A. Depends on: E3–E4 of DYAD-THM-SMOOTH-EMBEDDING, finite cyclic averaging. Qualitative radius; Φ is neither h6 nor the formal normalizer nor the archival chart. No finite-chart bounds, analyticity, physical action or new native profile. B-6 iff B-an and B-3 remains the owner analytic condition; no strictness claim.

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

`[DEF] [scope: typed metric convention for **identical identified planar vectors only**; no new RRF native profile or physical transport arrow] [import: Triadic v1.6 §7.4 and CN-05; RID unavailable; owner notice CN-05] [provenance: historical CN-05 Triadic v1.6 source; current TRIAD v1.7 §6.18 metric-unit identification block is [OPEN], convention-only, birth/mode bridge unresolved; §7.4 records in-text convention receipt, not RID-keyed physical adopted use]` For the same planar vector pair in the respective producer conventions, the **metric and oriented-area units** obey

\[
B_T^{\rm plane}=2B_G,\qquad Q_T=2Q_G,\qquad I_T=2I_G,\qquad \Omega_T=-\sqrt3\,\omega_{\rm raw}.
\]

This is a **convention comparison**, not a generator, mode, birth-event, inherited-child, apex $z$-component or physical carrier identification. It does not assert that the actual Genesis and Triadic birth states are the same objects; that bridge remains `[OPEN]`. When **and only when** the same vectors are identified, translating the Genesis conditional cubic loading $Q_c^G=\kappa^2(Q_s^G)^3$ would require

\[
Q_c^T=\frac{\kappa^2}{4}(Q_s^T)^3.
\]

`[OPEN] [scope: consumer obligation; NOT APPLIED to any owner birth formula]` Any later use must first declare the same-vector identification, source metric, orientation convention, child/parent variables and owner-accepted birth law; its coefficients must be re-expressed rather than copied. The equality above is the **conditional units conversion**, not a modified physical child law or an adopted Genesis↔Triadic birth bridge. Triadic CN-05 requests this convention record while retaining its distinct consumer-reconciliation tasks.

**Frame comparison (owner `[ALG]`, reference-only).** DYAD v6.4.24 §6.9 `DYAD-ALG-KP-FRAME-SCALE` (producer v6.4.20, declared K_p family): W_p=i cot(π/p) Z; μ_p^Z=cot²(π/p) μ_p^(W_p), same scale for ν3. At p=6 factor 3; arguments and shear κ unchanged. Exported coefficients name their frame; no new profile or physical interpretation. RECOG R11 = final-chart ledger (CLOSED); OPEN-M R11 = UVM assembly formulas, not that ledger (DYAD v6.4.24 Appendix C).

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

**Local candidate identity:** `RRF-ALG-S-DECOMPOSITION` — local nonzero comparator decomposition; registration awaits adoption.
**$S$-decomposition** `[ALG] [scope: RRF discussion-local] [provenance: Claude-checked]`: on a simply connected local domain where $C\ne0$ and $C\circ S\ne0$, with a consistent square-root branch (branch near $1$ inside the certified tube),
$C=C_-\,C_+$, $C_-=(C/C\circ S)^{1/2}$, $C_+=(C\cdot C\circ S)^{1/2}$; $C_-(Sx)=C_-(x)^{-1}$, $C_+(Sx)=C_+(x)$.
For multiplicative comparators whose typed relabeling law is $C(Sx)=C(x)^{-1}$, $C_+\ne1$ measures the covariance defect. $C_+$ is $S$-even and cannot decide orientation. Not canonical globally without a branch choice.

**Symmetrisation-order guard** `[import: DYAD §6.12]`: symmetrising the generator and iterating is not symmetrising the return — $[\mathrm{Odd}(f^{\circ6})]_{21}=\mu$ but $[(\mathrm{Odd}\,f)^{\circ6}]_{21}=\tfrac12-\tfrac{i\sqrt3}{6}$. A $C_\pm$ decomposition or an odd twin ($T_s$) defined at one-step level is not transferred to the six-step return without recomputation.

### 4.1a Imported exact-map memory: track and amplitude limits

`[DEF]` [import: RECOG v0.3.27 §6.13a | RECOG-THM-R9-MEMORY] RECOG's intrinsic retained observable is $\mathcal M(z_0)=\Psi_\infty-\Psi(z_0)$ in §2.4's fixed chart. Its current theorem is on the **$C_z$ track only**. The transported raw track $C_W^{(h)}$ has different initial equality classes and is not granted the same exact-map incompleteness theorem by a change of label.

`[THM]` [scope: imported owner result; selected T; exact normalized return; not a new RRF theorem] [import: RECOG v0.3.27 §6.13a | RECOG-THM-R9-MEMORY]

$$\mathcal M(z_0)=q_0[c_{\rm iso}+\Lambda_1(\Theta_0)]+R,\qquad |R|\le C_2q_0^2,$$

where $c_{\rm iso}=-4\sqrt3/27$ and $\Lambda_1(\Theta)=(43\sin6\Theta-5611\sqrt3\cos6\Theta)/1270080$ in the owner's fixed chart.

| DYAD-NF row | Memory theorem domain | R9 remainder constant $C_2$ in $\lvert R\rvert\le C_2q_0^2$ | Constructive exact-map $C_z$ incompleteness window |
|---|---|---|---|
| $r=1/20$, $C_7=100$ | $0<q_0\le1/400$ | 517 | $0<q_0<\lvert G\rvert/517$ |
| $r=1/40$, $C_7=30$ | $0<q_0\le1/1600$ | 163 | $0<q_0<\lvert G\rvert/163$ |

Here $G=-(43+5611i\sqrt3)/1270080$ is the owner's averaging coefficient. The theorem has an isotropic as well as a lattice term; the table does not replace its full statement. The smaller windows are not the whole memory-theorem domains. This is retained information not determined by the specified initial pair-comparator data; it is not information created by a threshold, a birth law, or a token-written carrier. No exact sign-invariance of $\mathcal M$ is inferred from its leading sixfold harmonic.

**Additive owner references, not replacement rows.** RECOG v0.3.27 §6.13a `RECOG-THM-R9-COMPARATOR-INCOMPLETENESS` is the separate strict-window corollary q0<abs(G)/C2. `RECOG-THM-R9-SHARPENED-ROWS`: C2=259.2,81.49 respectively at radii 1/20,1/40 with baseline C7=100,30. `RECOG-THM-R9-SHARPENED-ROWS-C7`: C2=221.4,75.69 on the same respective radii using the separate DYAD C7 ceilings 85.1,27.7. RECOG's actual import pin dyad-v6.4.23 `DYAD-THM-NF-REM-C7-SHARP`; entry unchanged at dyad-v6.4.24 §6.14. Strict formula controls; safe displayed windows for last pair q0<3.456e-5 and q0<1.010e-4. Native C_z track, rows not mixed, no whole-domain or raw-track incompleteness. No certificate replacement; original R9 evidence and baseline rows remain valid.

**Conditional primitive-phase reference.** DYAD v6.4.24 §6.14 `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` (T1 assumes RECOG-THM-R9-MEMORY; T2 assumes T1) and `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` retain the R9 premise. In the declared exact h6 chart with matched initial phase lifts, M_W−M=−Δ0(z0), abs(M_W−M)≤K0 sqrt(q0), K0=1101/1000 at radius 1/20 and 533/500 at 1/40. OPEN21 retains its own row constants and R9 error term. No transfer to C_W^(h) incompleteness. RECOG v0.3.27 §6.13b `RECOG-THM-A1A-PHASE-EXISTENCE-U` concerns separate R9-free existence on its explicit U, not the quantitative R9 law or R9-free OPEN21. No A1b/A1c claim import.

## 4.2 Pole-relabeling candidate actions

| Profile | Action | Status |
|---|---|---|
| WRAPPED | $\zeta\mapsto\zeta^{-1}$ | exact as ordered-ratio relabeling candidate |
| LIFT | $\mathcal L^{-1}S_h\mathcal L$ | exact involution; dynamical commutation degree-6 certified; not $(-\rho,-\eta)$ |
| W | $S_h=h_6(-I)h_6^{-1}$ (exact map on $h_6(D)$); $S_6=\mathcal J_{\le6}S_h$ (truncation) | $S_h^2=I$ exact; $\mathcal J_{\le6}(fS_h-S_hf)=0$; $h_6$ unique under `[conv: DYAD-ALG-NF6]` |
| NF | $z\mapsto-z$ | exact symmetry of $\widehat f_{\rm form}$; degree-6 certified for $\widehat f_6$ |
| NET | $\mathscr O_e$ (bookkeeping reorientation) | exact bookkeeping; **not** a pole-relabel candidate |

**Local candidate identity:** `RRF-ALG-FINITE-SWAP-TRANSPORT` — exact representation-level involution transport, not exact dynamical commutation; registration awaits adoption.
> **Established by registered transports:** $-I_{\rm NF}$, $S_h$ and $S_{\rm lift}$ are the same representation-level involution carried along `T-h` and `T-L` (by definition of $S_h$ and by exactness of $\mathcal L$). Involutivity is exact; commutation with the dynamics is finite-order (degree 6) or formal (for $\widehat f_{\rm form}$) — no all-order dynamical symmetry of the delivered maps is registered. **OPEN-A proper** consists of two questions only: (1) whether this involution is the physical pole relabeling; (2) whether the WRAPPED action $\zeta\mapsto\zeta^{-1}$ is the same physical operation — the two agree at linear order only and no exact transport of the involution across `T-exp` is registered. Six-step evidence: the raw return $F_W$ is not $-I$-odd ($F_4\ne0$) while the six-step jet $J$ is (DYAD §6.12).

**Adopted DYAD owner formal-involution receipt (N7).** `[THM] [scope: formal] [import: DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]` The unique formal `−I`-linear involution commuting with six-step `F=T^6` is `R_0=T^3F^{-1/2}=h_form(-I)h_form^{-1}`; its equality with the finite-chart `S_h` is **only through degree-six jet** under the stated shared normalization convention. Owner formal uniqueness **is now adopted**, not `source-pending`. `[THM] [scope: conditional analytic] [import: DYAD v6.4.12 §6.15; RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE]` A nonidentity analytic six-step commuting involution also commutes with primitive `T` under §6.15(b); analytic existence and physical pole relabeling are not established (DYAD OPEN 20; RRF OPEN-A). See §2.4b.

**Smooth owner receipt.** DYAD v6.4.24 §§6.15–17 retains formal J/R0 and F1–F3; E3–E4 supply the distinct smooth R=T³K_2^(−1) commuting exactly with T (DYAD-THM-SMOOTH-EMBEDDING). Finite S_h remains an exact involution, with only degree-six dynamical commutation certified. RECOG v0.3.27 §6.14/SG-R14 distinguishes them (historical R11 evidence v0.3.14). No exact physical relabeling, finite-chart radius, section-shadow transfer to R or raw C_W covariance follows. B-an/B-6 OPEN; see §§2.4b–c.

**Local candidate identity:** `RRF-DEF-TYPED-COVARIANCE` — typed observable/action criterion, not physical gauge selection; registration awaits adoption.
Typed-covariance criterion for gauge status (Wrap-up §10.2): $O(Sx)=\tau_O(O(x))$ for every admissible $O$, with $\tau_O$ the type's relabeling law — not universal invariance.

**Generator-family limit on OPEN-A.** `[import: RECOG v0.3.27 §§6.7,6.15 | RECOG-THM-TWIN-RADIAL-ACCESS] (historical v0.3.14 receipt)` The global radial-access theorem concerns the particular symmetric twin $T_s=(\rho-\sin\eta,\eta+\sinh\rho-\sin\eta)$: every initial state with $0<Q<7/200$ eventually reaches $|\rho|\ge\operatorname{arccosh}2$. It contrasts with the selected $T$'s certified local contraction. It is **not** a theorem that exact swap symmetry precludes healing for every admissible shear. RECOG §6.7 explicitly retains $g(\rho)=\tanh\rho$ as an odd, healing-at-cubic-order counterexample. The family law $\Re\mu_6=3b-4a^2$ for $g=\rho+a\rho^2+b\rho^3+\cdots$ has two routes to negative radial drift; removing the quadratic term does not force $b>0$. The diagnostic twins are not new registered RRF physical profiles. OPEN-A is not resolved in favor of a nonlinear physical swap by the $\sinh$ result; R1 remains PARTIAL in RECOG.

### 4.2a Cross-model orientation conjugacy is not physical pole exchange

**Current owner-source pin.** RECOG v0.3.27 §6.6a `RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY` is the owner of the scoped family identity; historical proof/receipt pins v0.3.20/21 retained. OFN v0.13 IMP-O09-03 is a consumer cross-reference, not owner.

`[ALG]` [import: RECOG v0.3.27 §6.6a #sec-6-6a-composition | RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY] [scope: character/shear family only; owner-source checked, EV-NOT-RERUN] For the declared character/shear family and `S_o(ρ,η)=(-ρ,-η)`:

\[
 S_o\circ T_k\circ S_o=T_{-k}.
\]

This is **conjugacy between two parameter-labelled maps**, not an exact symmetry of the fixed primitive `T_1`, nor an identity with the nonlinear fixed-chart involution `S_h=h_6(-I)h_6^{-1}` or the edge-bookkeeping reversal `\mathscr O_e`. Thus an isolated-dyad conjugacy invariant cannot select the `k` sign *within this model family*, while physical oriented-role interpretation stays OFN `OPEN-OPA` / RRF OPEN-A. The specific `sinh` diagnostic twin's radial theorem cannot exclude all odd generators: RECOG's odd `tanh` example has local cubic healing. No additional RRF native profile or physical gauge law is created.

## 4.3 Event predicates and sections: transported is not reselected

**Local candidate identity:** `RRF-DEF-EVENT-TRANSPORT` — representation/admissibility convention only; RECOG-ALG-BTOKEN-TRANSPORT remains the owner result; registration awaits adoption.
`[ALG]` [scope: same registered exact map and complete event predicate, where its chart/transition domains are valid] [import: RECOG v0.3.27 §6.16b | RECOG-ALG-BTOKEN-TRANSPORT] (historical v0.3.14 receipt)

Let the primitive B section be $\Sigma_B^W=\{W=t>0\}$, with the owner's full crossing predicate (including side/coorientation and $\rho$ restrictions). Under `T-h`,

$$\Sigma_B^z=h_6^{-1}(\Sigma_B^W),\qquad E_B^z(z,z')=E_B^W(h_6(z),h_6(z')).$$

The same admissible trajectory has the same event indices and gap word after this pullback. Replacing $\Sigma_B^z$ by the native ray $\arg z=0$ is **re-definition/selection of another event rule**, not transport of the old rule. A six-step-only record also does not automatically recover intermediate primitive crossing predicates.

The section/action shadow is separately recorded under `RECOG-ALG-SH-SECTION-SHADOW` (representation-level $S_h$ only). It does not identify $S_h$ with physical pole exchange. Full predicate transport is a necessary representation check, but every state-defined predicate has a pullback; independence from auxiliary choices still left free by the model is a separate token-selection requirement. A normalizer-dependent native lattice threshold is not promoted to the B/7-gap token by this table. No new physical event or retained state field is registered.

The section-shadow result concerns finite S_h (RECOG v0.3.27 §6.16b); transfer of its asymptotics to smooth R is unestablished, not a consequence of exact smooth commutation. No physical action selected.


---

# 5. Cycle-invariant matrix

| Invariant | Value space | Arity | Required structure | Gauge law under which invariant | Isolated certified dyad tube | Network sectors |
|---|---|---|---|---|---|---|
| $H_\times(\gamma)=\prod_{e\in\gamma}R_e$ | $\mathbb C^*$ | cycle $\ge3$ | multiplicative edge relations $R_e$ — **not native to `RRF-NET-W-RAW`**; requires a future registered multiplicative network realization | coherent vertex gauge $R_{ij}\mapsto g_i^{-1}R_{ij}g_j$, $g_i\in\mathbb C^*$ | N/A (no cycle) | node-mediated multiplicative-ratio branch: $H_\times=1$; independent multiplicative-edge branch: $H_\times\ne1$ possible |
| $H_2(\gamma)=\prod_{e\in\gamma}\sigma_e$ | $\mathbb Z_2$ | cycle $\ge3$ | pole-identification connection $\sigma_e$ | $\sigma_{ij}\mapsto g_i\sigma_{ij}g_j$, $g_i\in\mathbb Z_2$ (incidence-dressed) | N/A (no cycle; no winding needed) | not independently represented in current node-mediated attachment |
| $k$ | $\mathbb Z$ | history / path-lift; cycle when spatially closed | coherent lifted history | $\tilde\theta_i\mapsto\tilde\theta_i+2\pi n_i$ (node-coherent lift gauge) | $k=0$ `[import: NUMGEN v1.20.7 §6.4 N-3A; RID: NUMGEN-N3A-DECK-TRIVIAL] [scope: certified local one-chart tube, not every network or global trajectory; checked NUMGEN v1.22 §6.4; historical v1.20.7 pin retained]` | `[OPEN]` until a discrete profile is registered |

Obstruction statements, one-way: $H_\times\ne1\Rightarrow$ no pure node-presentation reduction `[ALG] [scope: RRF discussion-local]`; $H_2=-1\Rightarrow$ present node-mediated identification scheme insufficient (pole-role identification or an added $\mathbb Z_2$ edge field required) `[ALG] [scope: RRF discussion-local]`; additive $Ca\ne0\Rightarrow$ node-potential representation insufficient `[import: NUMGEN v1.20.7 §6.8 NG-7A; RID: NUMGEN-OPEN-REC-HOL-OPERATOR]` (sub-RID of closed NG-7A; identifier spelling preserved). No coupling among the three is claimed.

Current NUMGEN v1.22 §6.8: finite directed multigraph, field coefficients, CD^T=0 and im D^T=ker C. `NUMGEN-OPEN-REC-HOL-OPERATOR` is the closed NG-7A sub-RID; historical v1.20.7 pin retained. No NG-7B physical source, face-complex curvature or multiplicative composition follows.

---

# 6. Dependency lock: OPEN-B → OPEN-E1 → OPEN-E2

- **OPEN-B** (genesis identification primitive: node identity vs pole-role identity) must be resolved before a **canonical** choice of network state variables (**OPEN-E1**).
- Provisional network work may proceed in `RRF-NET-W-RAW` with incidence data, provided any node-mediated Jacobi/mode reduction is explicitly marked as that branch.
- **OPEN-E2** (joint constrained normal form of the coupled triad) starts only after E1. The single-dyad $h$ is not the answer to E2.

### 6.1 Representation alignment does not supply a physical composition domain

`[ALG]` [scope: imported algebra only] [import: NUMGEN v1.20.7 §6.6 C7C-M, M2-1 transported chain identity; RID unavailable for this sub-result] A cofinal order-preserving map can align two comparison contexts and transport bounded count defects. M2-1 still requires a separately admitted outer pair for carrier closure; alignment does not create co-realization. Current owner M2-1 `[RESULT] [from: ALG]` statement/guard checked at NUMGEN v1.22 §6.6; original v1.20.7 source pin retained. Depends on the cofinal order-preserving context alignment, bounded input and bridge defects; Π, WD-DOM, outer admissibility and admitted-chain existence are not supplied.

**Separate source-status receipt, not an algebraic closure:** Census-1 is **INCONCLUSIVE / INCONCLUSIVE** because no admitted nondegenerate composable source chain is present in that evidence set. No PASS/FAIL verdict on full-interface WD-DOM follows. This outcome is recorded in the same owner §6.6, not inferred from M2-1.

For this registry, the consequence is a **boundary**, not a new physical composition theorem: same numerical labels, same $h_6$, or a registered coordinate/context map alone do not establish an admissible common birth history or comparison interface. The common-realisation condition in §2.4 is a representation requirement, not a construction of its physical prerequisites. No NUMGEN C7C instrument-only lemma is promoted here. OPEN-B/E and M-4 remain separate. NUMGEN v1.22 §6.6: P2 answered by TDRG-DEF-ORIENT; M-4 HOLD pending approved design/preregistration for missing composable-chain evidence. Census-1 remains INCONCLUSIVE / INCONCLUSIVE. Source-reported re-annotation (N=24, three nodes, k∈{0,1,2,3}, bound_symmetric): DISC-1 0/22 changed, DISC-2 20/136 change verdict/class, 124/136 remain PASS, ten labels unchanged. No retroactive admission or universal certification (EV-SRC-REPORTED; EV-NOT-RERUN).

---

### 6.2 `RRF-CND-01` — coincidence realization admissibility (PROPOSED INTERFACE ONLY)

**Current regularity/clock boundary.** `[THM] [import: DYAD v6.4.24 §6.17 | DYAD-THM-SMOOTH-EMBEDDING] (producer v6.4.18)` At the adopted local C∞ germ scope, a smooth involution and smooth roots actually **exist** and commute with primitive `T` (E3–E4); finite S_h does not thereby become an exactly commuting action. **Analytic B-an/B-6 existence and finite-Cʳ classification remain open.** The physical contract still must declare `clock:` because `EF_phys=TE` and `EF_phys=T⁶E` are different factor hypotheses even though the existing C∞ involution commutes with both local clocks. No physical node exchange, network submersion or carrier has been selected.

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

**Regularity/clock decision — OPEN-B/E1 and OFN:** The elementary fixed-set implication needs only a defined equivariant map, not analyticity. A $C^\infty$ carrier may be studied as a **candidate**; this does not choose it over an analytic carrier, supply a convergent odd normalizer or make it a physical realization. Explicitly declare `regularity: analytic / C^\infty / formal / other`, valid domain and `clock: primitive T / six-step T^6 / other physical update` in each submitted realization contract. Adopted DYAD v6.4.12 §6.16 now proves **formal** uniqueness for the `F=T^6`-commuting involution, and §6.15(b) constrains even six-step `C³` involution linear parts to `±I`; §6.15 Corollary A promotes a nonidentity **analytic** six-step involution to exact primitive commutation under its local domain hypotheses. For an **existing `C^∞`** involution on DYAD §6.15/§6.17 local domains, adopted F1 upgrades flat primitive commutation to **exact** `RT=TR`; F2 gives uniqueness, and F3 upgrades existing smooth roots. **DYAD v6.4.18 E1–E4 now separately supplies such smooth roots/involution on its local domain**; this is not physical network realization. [import: DYAD v6.4.18 §6.17; RID: DYAD-THM-SMOOTH-EMBEDDING] For finite `C^r` the exact clock bridge is not imported. **No clock implication identifies** `EF=TE` with `EF=T^6E`; these remain different network-factor hypotheses and physical clock must still be declared. `[import: DYAD v6.4.12 §6.15; RID: DYAD-THM-LOCAL-INVOLUTION-GERM] [import: DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE] [import: DYAD v6.4.12 §6.15; RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]

**Passive transport guard:** A true passive recharting transports the *same* model, action and test subset; it cannot change invariance/noninvariance. Reimposing linear closure, replacing the carrier, changing update or selecting another physical clock is a **different model contract** requiring its own admissibility audit. Do not identify `(P_\mathcal C T^{\times3})^6` with `P_\mathcal C (T^6)^{\times3}` without proof of equivalence.

OFN v0.13 §5.5.2 model-contract reference: Q3b designating a slaved edge as physical state data is necessary for that route but not sufficient for complete-state covariance; Q5 concerns full oriented state/model relabeling with its model data, not active dynamical reversal of a fixed raw model. RRF-CND-01 gates still apply; none of these supplies physical exchange.

### 6.2a OFN class-C model contract — reference-only, not a native profile

`[DEF] [scope: RRF model-contract entry, not a physics selection] [import: OFN v0.13 §§5.5.2,5.5.4 | RTG-OFN-DEF-TRIAD-MODEL-CONTRACT] [request: OFN N-O10-3 / O10-P3; reference key: RF-O10-01]` **Class C** reimposes additive mean-feedback *in the transported carrier*, `F^N_κ(z)_e=N(z_e)-(κ/3)Σ_j N(z_j)`, and is a **different conditional model**, not passive recharting of the raw family and not a `RRF-NET-W-RAW` native-profile equation.

`[DEF]` [import: OFN v0.13 §5.5.2 | RTG-OFN-DEF-STANDARD-C] **Standard C at cubic order (OFN11-C01).** Requires a positive-dimensional embedded C³ manifold germ M through the null state, invariant under the declared update as a germ, supporting nonzero dyadic edge states arbitrarily close to null. On one common punctured local domain in M, F_e(r)=T(r_e)+I_e(r) and norm(I_e(r))≤C norm(r)^4 for common C,ε, all edges and all r∈M with 0<norm(r)<ε. Declare carrier, edge readout, complete local network-state norm and primitive clock. Not all edges need be nonzero; coincidence embedding allowed. A singleton, finite null-state record or isolated trajectory is insufficient; linear-order recovery alone is insufficient. Depends on the declared model, isolation manifold, domain and clock. Algebraic cancellation alone supplies neither the regime nor physical isolation/removal. Historical v0.10 nonempty-regime wording is superseded at this use.

| Contract field | Declared RRF reading / obligation |
|---|---|
| Carrier / operation | Transformed or Bochner-chart modal variables; newly imposed mean-feedback. Passive coordinate transport alone does not define this class. |
| `regularity:` | OFN11-C02: admitted real C∞ update germs in the local continuous FMS mathematical test class; analytic distinguished subclass; formal not realized law. Q6-REG remains local C³ comparison/factor regularity and C³ is the minimum Standard C manifold regularity. Formal family; real polynomial C1 (instance label, not differentiability) exists independently of smooth J, not the exactly transported dyad. Real C∞ exactly transported C2 uses DYAD-THM-SMOOTH-EMBEDDING E3–E4 and DYAD-THM-SMOOTH-EQUIVARIANT-CHART, current DYAD v6.4.24 §6.17 (qualitative radius, chart-family freedom, no finite-chart bounds). OFN v0.13 §5.5.5: **primary realized smooth mathematical candidate family; analytic exact realization and physical selection open**. Lock surfaces, cycle-defect capacity, six-step cubic, causal interface retain `[ALG]` [provenance: OFN co-owner SESSION computation, recorded, not registered] in §5.5.4. No registration of those properties or Genesis adoption of class C inferred. Analytic exact realization conditional on OPEN20 B-6, still OPEN; physical realization not selected. |
| `clock:` | Primitive `T` / declared primitive class-C update; `T⁶` is derived sampling, not an interchangeable network factor condition. |
| Domain / chart | Local neighborhood of 0; state and readouts in transported `z` or specified `Φ` chart. Raw-W readouts require offset transport/subtraction; no off-surface transfer inferred. |
| `κ:` | Formal contract κ∉{0,1,2}; κ=0 decoupled reference excluded by Q6; κ=1 flat sector (Q4 fails, not a failed coupling theorem); κ=2 neutral closure/mean multiplier −λ, outside hyperbolic center reduction, not proved Q6 failure. For 0<κ<2, κ≠1 closure-mode linear attraction modulus abs(1−κ), not a basin theorem. γ≡κ is OFN's class-C convention also recorded by RRF, not GEN's declaration, identity of raw/transported models, or Genesis face-lift κ_f. |
| Q6 factor exclusion | `[THM]` [import: Genesis v2.8.9 §6.3c; RID: GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO] (theorem/proof byte-identical in gen-v2.10). Real C³ germ on R6 fixing 0 in C³ coordinates, linear blocks λ on C and (1−γ)λ on D, zero quadratic and cubic mean-feedback H-JET: component n w_e² conj(w_e) − (γ/3) Σ_j n w_j² conj(w_j), μ=6 conj(λ)n≠0, γ∉{0,2}. No local C³ submersion E onto real dimension d∈{1,2,3} and C³ target map T' satisfying E G^6=T' E under H_spec: (1−γ)^6 not in spec DT'(E(0)). Separate GEN primitive-clock `[ALG]`, unnumbered, excludes E G=T' E for the same local C³ submersion/target/dimension scope, under H-JET/H-μ and H_prim: (1−γ)λ not in spec B, B=DT'(E(0)) real; H_prim does not imply H_spec for B^6 in general. Do not interchange the hypotheses or promote the primitive statement to the six-step theorem. GEN v2.10 §6.3c G-20: smooth C2 chart premise nonvacuous, analytic/physical/network realization OPEN. OFN v0.13 §5.5.3 `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT` `[RESULT] [from: ALG]` at its real C³ narrow scope (no conjugacy to product of three planar maps); no sub-C³ or wider non-planar no-go. |
| Native-profile impact | **None**: four dyad profiles and one provisional `RRF-NET-W-RAW` profile remain unchanged; OPEN-B/E1 not resolved. |

`[DEF] [scope: ψ-modulus readout and representation non-transfer] [reference-only: OFN v0.13 §5.5.7 and RF-O10-02; historical v0.10 readout source]` Within the stipulated fifth-order reduced family, `m(a)=Im(a\bar\mu)` is the scoped modulus. `|c|` determines `m` **only up to** the reflection `m↦2m_*−m`; phase of `c` is representation-dependent. `Im c=0` is neither a canonical chart gauge nor a physical selection principle. A phase readout must state the **primitive clock** and the **transported chart**, and cannot be promoted to a physical chirality observable by this entry alone.

**Isolation frame, reference-only.** OFN v0.13 §5.5.4: F_e−N(z_e)=−(κ/3)(N(z_e)+b_e), b_e=Σ_(j≠e)N(z_j), `[ALG]` [scope: formal family; for the exactly transported family real C∞] [provenance: OFN co-owner SESSION computation, recorded, not registered]; no RID. One-step sufficiency for κ≠0 does not prove closed reduced dynamics. §9 frame **recorded; none selected**: I-comp exact dyad law on balanced invariant lock regimes (compensating interface active for each nonzero edge), I-quiet (b_e=0) fails as dyad-recovery contract for κ≠0, I-remove requires a declared size-indexed law absent from class C. None selects physical isolation.

**Modulus evidence:** RF-O10-02, fifth-order reduced-map classification by m(a), `[ALG]` [provenance: SESSION; FMS symbolic P4 source-reported; OFN sampled verification]. Universal κ statement rests on P4 whose proof text OFN has not audited; κ sampled in {1,1/2,3}. Only the "not conjugate" direction carries over to full transported models (κ∉{0,2}), not a full-model iff. Reflection ambiguity, primitive clock and transported-chart readout above retained; no sign scalar, general rigidity, physical selection or owner-registered import assigned.

### 6.3 Token, history and network inheritance — interface prerequisites only

`[ALG] [scope: pointer to the preserved §4.3; no duplicate theorem import]` The full B-token transport rule is already registered in **§4.3**; RECOG v0.3.27 §6.16b retains its content (historical v0.3.20 receipt). The B-section/count phase lift remains distinct from the primitive-`\eta` N-3A deck state. No duplicate transport claim or competing live version pin is introduced here.

`[RESULT]` `[from: DEF]` [import: RECOG v0.3.27 §6.16g | RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS] [scope: registry-relative; missing network-inheritance interface remains RRF `[OPEN]`; historical v0.3.20/21 receipt]` For the currently registered source/carrier package, `token\to\Delta[a]` is **not yet well-posed**, rather than disproved. RRF records CELL-F4's necessary interface conditions without inventing physical attachments:

| Gate | Missing declaration |
|---|---|
| **W1** | graph, coefficient module, edge cochain and network realization |
| **W2** | dyad→edge/subgraph attachment preserving the relevant token predicate |
| **W3** | event-indexed cochains $a^-$, $a^+$ in the **same** cohomology space, so that $\Delta[a]=[a^+]-[a^-]$ is defined `[import: RECOG v0.3.27 §6.16g; RID: RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS] (RF-1 historical v0.3.21 source)` |
| **W4** | independence from the event log, count or Track-A clock alone |
| **W5** | conditioning/common-driver quotient distinguishing token-specific writing from shared-driver correlation |

`[OPEN] [scope: RRF extension, **not** RECOG W3; no map registered]` If pre- and post-birth classes naturally belong to different spaces `H⁻`, `H⁺`, an extension must explicitly supply an appropriate typed comparison into **one common cohomology space** `H`, for example maps `j⁻:H⁻→H`, `j⁺:H⁺→H`, with justified algebraic and event-domain semantics, and then define `Δ_H[a]=j⁺[a⁺]-j⁻[a⁻]`. This is a **new missing-interface obligation**, not a currently registered transport, not an automatic birth law and not a restatement of RECOG W3. RER G9/1 should cite owner W3 separately from this extension.

The closed algebra of NUMGEN NG-7A, including its closed sub-RID, does not produce NG-7B source/curvature or a multiplicative G1 realization. M2-1's transported counting identity is not a co-realized physical composition or new birth law. Genesis v2.8.5 and Triadic v1.6 also distinguish unit rotation `W(J_Qs)/W(s)=i` from loaded child ratio `W(c_0^{[3]})/W(s_*)=i\kappa Q_s`; full remainder/physical source remain conditional. Independent Jacobi *mode labels* do not select an extra physical state dimension, and covariance typing does not uniquely fix physical lowering.

Current GEN v2.10 §§1–2,6.9,7 and TRIAD v1.7 §§6.18,7.4 preserve the unit-direction vs loaded-child distinction and conditional remainder: the admitted complete child functional must preserve the cubic term and inherit the fifth-order absolute remainder; a raw-residual quartic does not imply that remainder. 9B covector B-lowering not forced, sign selection OPEN; 9C extra raw-array premise. GEN sourced-junction theorem under w=0, σ_f≠0 and Δ3>0: constrained birth equation τ d_perp+S_f=0, norm(d_perp)²=Δ3 has two antipodal solutions, no selected minimizer (GEN-THM-SOURCED-JUNCTION, reference only). GEN-ALG-P4-DRIFT-IDENTITY and GEN-ALG-BIRTH-SYMMETRY-SEED are not imported. No physical transverse dimension, child or source law.

### 6.4 RER dynamical-closure interface — adopted noncanonical reference, nonnormative proposal

`[DEF] [scope: reference-only; NON-NORMATIVE]` `rer-v0.2` (SHA-256 58feee5ff1f16a37fc4ee029f24499928ea7439731de0a090d8794c1cbe57ad0; PI adoption record `upload/corpus-originals-20261123/RER_v0_2_ADOPTION_RECORD_20261021.md`) is adopted at NONCANONICAL working-registry scope: 18 scoped records accepted at declared grades/limits; RER-ER2B-T6D and RER-ER2B-CARRIER retained BLOCKED_SOURCE_UNVERIFIED and excluded from scientific acceptance. G7–G10 reference the RRF guards at §§0.3,4.2a,6.2–4. S0 recovered original RRF closure proposal `records/rrf/RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md`, SHA-256 65186f393985ed502512c875601891cec999830abc2cc7db2fe01dd94f554e86; this pointer is NOT a mandatory profile field, theorem, numerical certificate or physical realization. RER reports K=6 pilot 8/8 (4/904 boxes per N), K=8 stopped at 1/8; regional/global Stage-2 certificate, multi-step error control, G6, all-order graph completion, G2 §5b carrier identification and physical realization remain OPEN. CONTROLLED_APPROXIMATE_CLOSURE not accepted. No evidence re-audit or new RER record acceptance inferred from recovered bytes. Historical RER source-pending statements remain in predecessor provenance. For admissibility use §§0.3,3,4,6.2–6.3.

### 6.5 OPEN register (representation scope)
**OPEN register — proposed descriptive identities, existing obligations unchanged.** Status and owner fields below concern RRF representation work only; owner science stays with the respective scientific owners. All remain ACTIVE. The local names OPEN-A, OPEN-B, OPEN-E1 and OPEN-E2 are retained as aliases (Methodology §§4.2,5.1); proposed descriptive RIDs are not registered until PI adoption.

**Closure criteria (PI-approved for the v0.9 candidate, 26 November 2026).** The final column contains the accepted candidate wording, restricted to the questions already stated in rrf-v0.8.4 §§4.2 and 6. It is not an adopted closure rule and establishes neither new prerequisites nor additional sufficient closure routes. In particular a scoped refusal or obstruction does not automatically close a module. Current governing questions and the B→E1→E2 dependency lock remain unchanged.

| Local alias / proposed RID | Status | Owner study | Question (existing scope) | Dependencies (existing prerequisites) | Closure criterion (candidate); relevant interfaces |
|---|---|---|---|---|---|
| OPEN-A / RRF-OPEN-POLE-RELABELING | ACTIVE | RRF | §4.2: (1) whether the registered representation-level involution is physical pole relabeling; (2) whether WRAPPED inversion is the same physical operation. Distinct smooth/formal actions and bookkeeping; no selected action. | No other RRF OPEN prerequisite declared in §4.2. | Justified resolution of both existing questions at their declared scope. Smooth existence alone does not settle either. Relevant: OFN OPEN-OPA, RECOG R1 and G2 contract. |
| OPEN-B / RRF-OPEN-IDENTIFICATION-PRIMITIVE | ACTIVE | RRF | §6: Genesis identification primitive, node identity versus pole-role identity. | No RRF OPEN prerequisite declared for B in §6. | Resolve the stated identification question before canonical network-state selection. Relevant: GEN/OFN, RECOG F4. |
| OPEN-E1 / RRF-OPEN-NETWORK-VARIABLES | ACTIVE | RRF | §6: canonical choice of network state variables after B; W→NET identification bridge remains OPEN (§0.3/§3), provisional work only. | OPEN-B. | Justify the canonical choice of network variables in its declared domain; separately resolve the applicable carrier/transport obligations without inferring physical realization. Relevant: RER, RECOG, GEN/OFN. |
| OPEN-E2 / RRF-OPEN-JOINT-NF | ACTIVE | RRF | §6: joint constrained normal form of the coupled triad; the single-dyad h is not the answer. | OPEN-E1 (and its OPEN-B prerequisite). | Establish the stated joint constrained normal form for the declared coupled model, at its declared scope, after E1; no substitution by the isolated h. |

BR-Q2 is the separately authorized, not-yet-dispositioned OFN question `pipes/RRF/20261104-OFN-binary-recognition-sign-typing.md`. No new sign comparator, gauge choice, registration or BR-Q2 conclusion in this intermediate. OPEN-A then OPEN-B→E1→E2 remains the research sequence.

---

# 7. Owner uses, consumer references, evidence and unregistered objects

## 7.1 Reference-only consumer and boundary register

| Interface | Current source, actual use and refusal |
|---|---|
| Discrete boundary | TDRG v2.13 §6.3 TDRG-DEF-ORIENT: S=0 balanced tie when E=0 or N/2. SG14 and §7: common token shift star condition 2c≡0 (mod N), `RTG-OFN-ALG-STAR-TOKEN-SHIFT` at ofn-v0.12, statement accepted, custody transfer open; birth-free symmetry not unrestricted gauge, mirror not step symmetry. No discrete profile, physical bridge or continuous transfer. |
| UVM | `uvm-v0.7.2` OPEN-M-6, SG-M-7, §7: PI-approved reference-only use of rrf-v0.8.4 §§0.3,3,3.1,6.2. C3 requires physical J_perp, group, covector dual/lowering, domain, source normalization, observable and restoring block; Stage 1 SESSION only. Archive/finite NF/smooth chart distinct, no UV source-bundle profile or arrow. Same-vector metric convention not applied to UVM Q_s=0.1. C3 remains GEN-facing. |
| Programme | `programme-v1.5` IF29–33: actual RRF reference and owner-import pins are distinct from prospective synchronized pins. IF30/31 and IF33 change notices to PROG and scoped IF33 notice to RER are due only on authorized successor publication; consumer disposition separate. SG-PROG-1–4 apply; five programme OPENs ACTIVE; no new governing home or PRR status. |
| RER | `rer-v0.2` G7–10 and adoption record: reference/record only, see §6.4. Historical pins and source limits remain as adopted; no automatic receiving acceptance of v0.9. |
| Existing DYAD / RECOG / TRIAD / OFN / NUMGEN references | Actual owner-pinned RRF references remain distinct from RRF scientific imports. Programme IF29–32, accepted S1 matrix and each owner import ledger determine scope; no consumer repin by this candidate. |

## 7.2 Source-use and evidence routing

Claim-level source and scope entries remain at their technical homes in §§2–6; the accepted S1 matrix and S2a build record identify every checked owner version, decision record, point of use and inherited scope. Current checks are EV-SRC-READ; source hashes/identity EV-HASH from S1, not EV-RUN. Baseline proof pins and historically load-bearing evidence are retained. The following current references are separate from owner imports: sharper C7/R9 rows (§§2.4,4.1a); frame scale (§3.1); R9-dependent DYAD phase and independent A1a existence (§4.1a); OFN SESSION isolation/modulus (§6.2a); GEN current G-20 and export guard (§§6.2a,6.3); CN-05 owner OPEN convention (§3.1); NUMGEN P2 re-annotation (§6.1); RER and UVM (§§6.4,7.1). No new owner proof or certificate rerun. Historical evidence pointers, source access gaps, precise import entries and missing-owner-RID routing are retained below; no fabricated owner RID. The historical v0.8 QA JSON and PRR review ZIP remain missing. S0 check is pinned to S0, not a prospective verifier after DSN changes.

#### Import ledger — claim/use index

Each entry points to the complete local claim/use block at the identified section and line in this review candidate; the inherited scope, assumptions, chart, domain, clock and dependency conditions are the ones at that block and the actual owner pin, not a new inference. The frozen-source locator and corresponding candidate locator are also in the movement map. Line numbers are candidate navigation; section and exact source identity control. Source status is distinguished from RRF use. For historical receipts, S0 custody and S1's exact-source matrix govern verification; no certificate execution is asserted here. Unnumbered source blocks remain `RID unavailable`; owner-RID assignment follow-up is unresolved, and no sent governance request is inferred. Evidence RIDs do not stand in for scientific claim RIDs. Explicit current-owner grades below are targeted source readouts, not deductions from RID category or substitutions for historical proof pins. Where a grade is not separately verified, the source block controls.

| Use key | Actual source pin / RID or exact source locator | Source status / local use boundary | Local use, inherited scope and depends-on | Verification / synchronization |
|---|---|---|---|---|
| I-01 | DYAD v6.4.10 §1, definition Q_true; RID unavailable | RID unavailable; owner assignment follow-up | §2.1; use line 109; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-02 | DYAD v6.4.10 §6.4 ISP (#sec-6-4-isp), anti-correlation frame; RID unavailable | RID unavailable; owner assignment follow-up | §2.1; use line 109; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-03 | DYAD v6.4.24 §1; RID: DYAD-DEF-PRIMITIVE-MAP | Current DYAD v6.4.24 L47: [DEF] | §2.2; use line 123; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-04 | RECOG v0.3.14 §6.14, cert check 9; evidence RID: RECOG-ART-R11-LEDGER | Evidence pointer (not theorem RID) | §2.2; use line 126; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-05 | RECOG v0.3.14 §6.4 and §6.7; RID unavailable | RID unavailable; owner assignment follow-up | §2.2; use line 126; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-06 | DYAD v6.4.10 §6.14, definition 𝓛; RID unavailable | RID unavailable; owner assignment follow-up | §2.3; use line 136; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-07 | DYAD v6.4.10 §1; OFN v0.8 | Source block; no new grade asserted | §2.3; use line 139; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-08 | DYAD v6.4.10; RID: DYAD-THM-C21 (actual historical source pin) | Current DYAD v6.4.24 L469: [THM] | §2.3; use line 139; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-09 | RECOG v0.3.14 §6.14, cert check 9; evidence RID: RECOG-ART-R11-LEDGER | Evidence pointer (not theorem RID) | §2.3; use line 142; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-10 | RECOG v0.3.14 §6.14; evidence RID: RECOG-ART-R11-LEDGER | Evidence pointer (not theorem RID) | §2.3; use line 143; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-11 | DYAD v6.4.10 §6.12, definition E_odd; RID unavailable | RID unavailable; owner assignment follow-up | §2.3; use line 144; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-12 | OFN v0.9 §4.4 #ofn-rank-typing; RID: RTG-OFN-DEF-RANK-TYPING | Current OFN v0.13 L290: [DEF] | §2.3; use line 147; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-13 | DYAD v6.4.10 §6.14; RID: DYAD-ALG-NF6 | Current DYAD v6.4.24 L776: [ALG] | §2.4; use line 154; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-14 | RECOG v0.3.14 §6.14, refusal line; evidence RID: RECOG-ART-R11-LEDGER | Evidence pointer (not theorem RID) | §2.4; use line 155; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-15 | DYAD v6.4.10 §6.14; RID: DYAD-ALG-NF6-OBS | Current DYAD v6.4.24 L783: [ALG] | §2.4; use line 155; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-16 | DYAD v6.4.10 §6.14; RID: DYAD-THM-NF-REM | Current DYAD v6.4.24 L797: [THM] | §2.4; use line 159; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-17 | RECOG v0.3.14 §6.13a; RID: RECOG-THM-R9-MEMORY | Current RECOG v0.3.27 L643: [THM] | §2.4; use line 161; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-18 | RECOG v0.3.14 §6.14; evidence RID: RECOG-ART-R11-LEDGER | Evidence pointer (not theorem RID) | §2.4; use line 163; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-19 | DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE | Current DYAD v6.4.24 L1009: [THM] | §2.4; use line 164; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-20 | DYAD v6.4.12 §6.14; RID: DYAD-ALG-NF6-DEG10 | Current DYAD v6.4.24 L808: [ALG] | §2.4a; use line 180; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-21 | DYAD v6.4.12 §6.16 #sec-6-16-centralizer; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE | Current DYAD v6.4.24 L1009: [THM] | §2.4b; use line 190; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-22 | DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-CENTRALIZER | Current DYAD v6.4.24 L1005: [THM] | §2.4b; use line 196; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-23 | DYAD v6.4.12 §6.16; RID: DYAD-ALG-CENT-KERNEL | Current DYAD v6.4.24 L992: [ALG] | §2.4b; use line 196; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-24 | DYAD v6.4.12 §6.15 #sec-6-15-involution; RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE | Current DYAD v6.4.24 L972: [THM]; conditional | §2.4b; use line 200; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-25 | DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES | Current DYAD v6.4.24 L1041: [THM]; conditional; existing germ/root | §2.4b; use line 200; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-26 | DYAD v6.4.13 §§2, 6.16–6.17; RID: DYAD-OPEN-INVOLUTION-REALIZATION | Current DYAD v6.4.24 L258–260: OPEN module status; not theorem RID | §2.4b; use line 202; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-27 | DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES | Current DYAD v6.4.24 L1041: [THM]; conditional; existing germ/root | §2.4b; use line 205; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-28 | DYAD v6.4.13 §§2, 6.16; RID: DYAD-OPEN-INVOLUTION-REALIZATION | Current DYAD v6.4.24 L258–260: OPEN module reference; local algebraic consequence remains local | §2.4b; use line 205; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-29 | DYAD v6.4.24 §6.17 \| DYAD-THM-SMOOTH-EMBEDDING | Current DYAD v6.4.24 L1050: [THM] | §2.4b; use line 207; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-30 | DYAD v6.4.13 §6.16; RID: DYAD-THM-FORMAL-Z6-GENERATOR | Current DYAD v6.4.24 L1019: [THM] | §2.4c; use line 211; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-31 | DYAD v6.4.13 §6.16; RID: DYAD-OPEN-INVOLUTION-REALIZATION | Current DYAD v6.4.24 L258–260: OPEN module; equivalence scope at use | §2.4c; use line 211; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-32 | DYAD v6.4.13 §6.17; RID: DYAD-CAND-FLAT-CENTRALIZER | Current DYAD v6.4.24 L1037: [THM] | §2.4c; use line 213; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-33 | DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES | Current DYAD v6.4.24 L1041: [THM]; conditional; existing germ/root | §2.4c; use line 215; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-34 | DYAD v6.4.24 §6.17 \| DYAD-THM-SMOOTH-EQUIVARIANT-CHART | Current DYAD v6.4.24 L1056: [THM] | §2.4c; use line 219; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-35 | Triadic v1.6 §7.4 and CN-05; RID unavailable; owner notice CN-05 | Convention-only; current TRIAD v1.7 §6.18 [OPEN]; RID unavailable | §3.1; use line 258; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-36 | RECOG v0.3.14 §6.14, comparator tracks, cert checks 5–7; evidence RID: RECOG-ART-R11-LEDGER | Evidence pointer (not theorem RID) | §4.1; use line 289; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-37 | RECOG v0.3.14 §6.14, cert checks 5–7 and 9; evidence RID: RECOG-ART-R11-LEDGER | Evidence pointer (not theorem RID) | §4.1; use line 291; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-38 | DYAD v6.4.24 §6.12 (current exact-text locator; previous inline unversioned guard; RID unavailable) | Owner source guard; RID unavailable; assignment follow-up | §4.1; use line 298; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-39 | RECOG v0.3.27 §6.13a \| RECOG-THM-R9-MEMORY | Current RECOG v0.3.27 L643: [THM] | §4.1a; use line 302; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-40 | RECOG v0.3.27 §6.13a \| RECOG-THM-R9-MEMORY | Current RECOG v0.3.27 L643: [THM] | §4.1a; use line 304; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-41 | DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE | Current DYAD v6.4.24 L1009: [THM] | §4.2; use line 334; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-42 | DYAD v6.4.12 §6.15; RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE | Current DYAD v6.4.24 L972: [THM]; conditional | §4.2; use line 334; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-43 | RECOG v0.3.27 §§6.7,6.15 \| RECOG-THM-TWIN-RADIAL-ACCESS | Current RECOG v0.3.27 L817: [THM]; diagnostic twin scope | §4.2; use line 341; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-44 | RECOG v0.3.27 §6.6a #sec-6-6a-composition \| RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY | Current RECOG v0.3.27 L478: [ALG] | §4.2a; use line 347; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-45 | RECOG v0.3.27 §6.16b \| RECOG-ALG-BTOKEN-TRANSPORT | Current RECOG v0.3.27 L939: [ALG] | §4.3; use line 358; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-46 | NUMGEN v1.20.7 §6.4 N-3A; RID: NUMGEN-N3A-DECK-TRIVIAL | Source block; no new grade asserted | §5; use line 379; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-47 | NUMGEN v1.20.7 §6.8 NG-7A; RID: NUMGEN-OPEN-REC-HOL-OPERATOR | Source block; no new grade asserted | §5; use line 381; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-48 | NUMGEN v1.20.7 §6.6 C7C-M, M2-1 transported chain identity; RID unavailable for this sub-result | Current NUMGEN v1.22 §6.6 [RESULT] [from: ALG], as checked in S1; RID unavailable | §6.1; use line 395; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-49 | DYAD v6.4.24 §6.17 \| DYAD-THM-SMOOTH-EMBEDDING | Current DYAD v6.4.24 L1050: [THM] | §6.2; use line 405; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-50 | OFN v0.9, complete-state covariance / OPEN-PRIMACY-3B/3C; RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md; RTG_RRF_COINCIDENCE_ADMISSIBILITY_REVIEW_v0_1.md; RTG_RRF_RESPONSE_TO_OFN_COINCIDENCE_v0_2.md | Reference-only source bundle | §6.2; use line 418; complete block and referenced domain/guard at that site | Historical source bundle; S0 custody and S1 targeted interface checks; EV-NOT-RERUN; no new owner adoption. |
| I-51 | DYAD v6.4.18 §6.17; RID: DYAD-THM-SMOOTH-EMBEDDING | Current DYAD v6.4.24 L1050: [THM] | §6.2; use line 422; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-52 | DYAD v6.4.12 §6.15; RID: DYAD-THM-LOCAL-INVOLUTION-GERM | Current DYAD v6.4.24 L953: [THM]; conditional | §6.2; use line 422; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-53 | DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE | Current DYAD v6.4.24 L1009: [THM] | §6.2; use line 422; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-54 | DYAD v6.4.12 §6.15; RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE | Current DYAD v6.4.24 L972: [THM]; conditional | §6.2; use line 422; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-55 | DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES | Current DYAD v6.4.24 L1041: [THM]; conditional; existing germ/root | §6.2; use line 422; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-56 | OFN v0.13 §§5.5.2,5.5.4 \| RTG-OFN-DEF-TRIAD-MODEL-CONTRACT | Current OFN v0.13 L437: [DEF] | §6.2a; use line 430; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-57 | OFN v0.13 §5.5.2 \| RTG-OFN-DEF-STANDARD-C | Current OFN v0.13 L449: [DEF] | §6.2a; use line 432; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-58 | Genesis v2.8.9 §6.3c; RID: GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO | Current GEN v2.10 L867 [THM], conditional; unchanged pinned v2.8.9 statement (S1) | §6.2a; use line 441; complete block and referenced domain/guard at that site | Historical proof/receipt pin; current-source check as recorded at point of use; EV-NOT-RERUN |
| I-59 | RECOG v0.3.27 §6.16g \| RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS | Current RECOG v0.3.27 L1134: [RESULT] [from: DEF] | §6.3; use line 454; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |
| I-60 | RECOG v0.3.27 §6.16g; RID: RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS | Current RECOG v0.3.27 L1134: [RESULT] [from: DEF] | §6.3; use line 460; complete block and referenced domain/guard at that site | Current owner statement/contract inspected; EV-SRC-READ, EV-NOT-RERUN |

## 7.3 Proposed RRF-native identifier routing (candidate only)

The four dyad profiles and one provisional network profile keep their existing identifiers. Existing transport keys T-h, T-L, T-exp and T-net, and the local NF→WRAPPED composite keep direction, domain and loss as in §3; T-net remains OPEN. No profile or arrow added. `RRF-CND-01` remains the existing proposed coincidence admissibility interface. The following are proposed local identity labels for unchanged RRF-owned conventions/implications, not owner theorem RIDs and not registered until PI adoption. Identifier annotations point to the actual statement homes without changing their predicates.

| Candidate local ID | Existing home and grade/scope |
|---|---|
| RRF-DEF-PASSIVE-TRANSPORT | §0.3 passive versus new-model discipline `[DEF]`; ER-2B illustration external |
| RRF-ALG-S-DECOMPOSITION | §4.1 local nonzero multiplicative comparator with consistent square-root branch `[ALG]`, not global canonical decomposition |
| RRF-ALG-FINITE-SWAP-TRANSPORT | §4.2 representation-level transported involution only; finite-jet dynamical commutation distinct `[ALG]` |
| RRF-DEF-TYPED-COVARIANCE | §4.2 criterion for declared observables/actions; no physical gauge selection `[DEF]` |
| RRF-ALG-ODD-ROOT-EQUIVALENCE | §2.4b conditional class-wise consequence of owner clock/root results, not existence theorem `[ALG]` |
| RRF-DEF-EVENT-TRANSPORT | §4.3 representation/admissibility convention only `[DEF]`; RECOG-ALG-BTOKEN-TRANSPORT remains RECOG's result |

### 7.4 Not registered

- TDR-G discrete state profile (node phase/advance data; edges reconstructed from nodes) — to be registered once OPEN-B fixes whether $\sigma_e$ is added.
- A multiplicative network realization ($R_e\in\mathbb C^*$) and its bridge to $W_e^{\rm net}$ — prerequisite for $H_\times$ as a native network invariant.
- Any profile for effective geometry — no representation decision exists; deliberately last in the PRR ladder.
- Genesis inheritance fields for all profiles — pending the Genesis Identification & Inheritance Ledger (Wrap-up §14.1). Recovered GIIL v0.19 DRAFT (SHA-256 f6320914190b434332058b69fe0974ce584d1a8167ae40e2650091be5bdbe2f8) is a historical noncanonical source on GEN v2.8.4; GEN/RER source-status dispositions pending (§S0 custody record). No inheritance registration or PRR v0.3 substitution.
- The archival coordinate change $\Phi_{\rm archive}$ and the log-projected model $G_{\rm proj}$ (DYAD SG-19 operations (i), (ii)) — distinct objects, not representation profiles of this registry.

### 7.5 Retained evidence identities and reproduction boundaries

The following source identities are retained as printed in the dated receipts, not newly verified claims about current availability. Full source custody, recovered archives and remaining missing identities are in `records/rrf/RRF_S0_SOURCE_CUSTODY_20261126.md`, the S1 matrix and the adopted predecessor §10. The evidence scope at each technical use controls; no owner certificates were rerun in the v0.9 maintenance cycle.

| Historical proof source (as printed in v0.7 snapshot) | SHA-256 | Role recorded at that date |
|---|---|---|
| `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_14.md` | `d10c2a988bd1dcaf0c673ad6951efec3245275ee65a0d341f44335cfc7904b43` | Full owner-ledger reading; current result/status source |
| `RTG_NUMBER_GENESIS_DSN_v1_20_7.md` | `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` | Full owner-ledger reading; current partial-composition guard |
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md` | `7455811928606076b3bc3075632275dc2a24e37fdbf0ae20036db5529a1b56b7` | Unchanged owner; fixed chart, constants and scopes |

**R11 evidence pin, as printed by the owner:** `RECOG-ART-R11-LEDGER` → `recog_r11_chart_ledger_cert.py`; SHA-256 `a4950ed525f2e6ee4be0ddd7f9607b2c3c14d8e31052a88db6ae163fa5d6e5e5`; 11-check certificate, with check 9 as the swap/covariance evidence. The executable is not present in this update's mounted files, so this hash is **source-reported**, not locally authenticated against script bytes. The ledger's attribution to Claude is the basis for the covered reviewer-stage update.

**v0.7 evidence-availability receipt (5 October 2026; not current inventory):**

**Unavailable for a new artifact-level rerun:** the current R11, R9, R8/B3, symmetric-twin and F2 certificate packages, the original P2-B v2 evidence archive and full `certificate.json`, and the original independent degree-ten package. Some older algebra/referee files are mounted, but none was executed here. Written owner records and the existing VF-1 verification note are not replaced by inferred script results.

- **Inspected directly:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_12.md`, 170,323 bytes, SHA-256 `c2f00eb0832e6aabcbcfd1a3c583d6f1e7b0950a2f8db97d89045ed0bcb438e8`; **ADOPTED**, 16 October 2026. The owner file's §§2, 6.15 and 6.16, §7 outbound notice N7 and Appendix A publication entry were checked; owner theorem RIDs and OPEN 19→CLOSED (formal), OPEN 20→OPEN statuses are present.
- **Installer manifest:** `RTG_DYADIC_v6_4_12_INSTALL_MANIFEST.json`, SHA-256 `55854504897fc55c9523830d1fd7ea04325edacd9daa5dafeed2f2b66489f4cf`. Its `v6_4_11_to_v6_4_12_final.diff` and `v6_4_12_r1_to_final.diff` SHA-256 values match the mounted files. Manifest includes **source-reported** kernel and `R_0` script runs from prior review rounds; those scripts were **not rerun in this RRF preparation**.
- **Inspected directly:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_13.md` (ADOPTED, 18 Oct 2026), SHA-256 `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542`; §§2, 6.15–6.17, §7/N9 and Appendix release/adoption records. The source contains both adopted scientific claims and historical DRAFT records; only current adopted §6.17 status is imported. Original standalone Lemma F v0.3 script and archive were **not** separately mounted/rerun in this RRF pass.
- **Adopted predecessor:** `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_2.md` SHA-256 `f09dbb12f4b65b13c3f08ec049dcd701b04ca24c4b55876b565868f288555461`; no v0.8.2 body/history modified. Distinct `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW_v0_4_REVIEW_CANDIDATE.md` is a separate noncanonical consumer note.
- **RRF-only mathematics kept outside the owner ledger:** a separate SESSION review evaluates VF-1 and the involution parity to locate the first nonmatching homogeneous jet of `S_h` and `R_0`. That inference is **not** promoted here to owner-grade nor used to select a physical representation.

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
12. That the **formal uniqueness theorem by itself** supplies analytic convergence, a physical pole exchange or exact equality with the finite `S_h` beyond the shared degree-six jet. **Current owner status (DYAD v6.4.24 §§2,6.17):** local **C∞ existence is now CLOSED** by DYAD v6.4.18 `DYAD-THM-SMOOTH-EMBEDDING` E1–E4, while B-an/B-6 analytic existence remain OPEN; v6.4.13 Lemma F/F1–F3 separately close smooth uniqueness/commutation. Physical G2/OPEN-A and network-factor realization remain OPEN (§§2.4b–c, 6.2).

---

### 8.1 Source/adoption nonclaims

- `RRF-CND-01` does not establish a new primordial coincidence axiom, physical node identity or admissible node merge. No selected physical `K_3` law or universal prohibition of node-mediated RTG follows.
- The `T_k\leftrightarrow T_{-k}` family conjugacy does not make `S_o`, `S_h`, `-I_{NF}` and `\mathscr O_e` the same physical pole action; RRF OPEN-A stays open.
- The ER-2B additive-carrier continuum is conditional mathematics, not a passive-gauge family of *one* physical triad; quartic drift thresholds do not select a physical carrier.
- RECOG CELL-F4 W1–W5 are missing-interface criteria, not a registered token-to-cochain map, network memory field or birth inheritance law.
- A formally verified finite jet does not supply a global remainder or controlled approximate closure. N=7/8 Stage-2 **global certificate remains pending** in adopted noncanonical RER v0.2 (§6.4); no Stage-2 executable or certificate rerun in this review.
- RER F3, formal age families, child-free/ambient minima, `w_13`, or candidate factors are not imported as verified RRF scientific theorems or new native profiles.
- `RRF-NET-W-RAW` remains provisional, the `RRF-DYAD-W→RRF-NET-W-RAW` bridge is OPEN and OPEN-B→E1→E2 is unchanged. OFN 3B/3C, NG-7B and physical Genesis/Triadic/OPEN-M selections remain open.

## Appendix A — Change record

- **v0.9 — DRAFT (26 Nov 2026):** accepted S1 owner-source/interface synchronization and S2a corrections, followed by S2b structural migration. Standard C/class-C scope, smooth/analytic/finite separation, R9 additional rows, M4 HOLD reason, RER noncanonical and UVM reference scope; proposed local identifiers and OPEN aliases retained. Historical bytes and earlier release/evidence records remain retrievable from `rrf-v0.8.4` and the frozen S2a commit. No owner theorem, physical model, BR-Q2 result, OPEN closure or adoption.

## Appendix B — Correction routing

The scoped content delta is the independently accepted S2a (review 6076472389), not a compaction inference. The accepted S1 matrix and `records/rrf/RRF_V0_9_S2A_BUILD_REVIEW.md` map each correction to its source and point of use, including Standard C/class-C, current owner statuses, the fixed finite chart versus smooth/analytic distinction, and the distinct R9 rows. Historical rejected/limited claims and evidence remain in the adopted predecessor and owner correction records; operative refusals remain in §8. No new scientific correction in S2b.

*END OF DOCUMENT — RRF v0.9 DRAFT*
