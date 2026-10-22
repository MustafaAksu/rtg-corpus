---
title: "RTG — RRF Representation Registry"
version: "v0.8.4"
date: "20 October 2026"
class: "working artefact / representation discipline"
status: "ADOPTED — RRF v0.8.4 working representation standard; 20 October 2026"
supersedes: "RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3.md — ADOPTED 19 October 2026; SHA-256 b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187"
review scope: "DYAD v6.4.18 N14 C-infinity existence; RECOG v0.3.21 RF-1 W3 owner alignment; OFN v0.10 N-O10-3 (O10-P3) class-C model contract and psi readout; Genesis v2.8.9 conditional Q6 owner pin; no profile or physical choice"
revision base: "RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3.md (ADOPTED; SHA-256 b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187); historical publication text preserved"
predecessor source draft: "RTG_RRF_REPRESENTATION_REGISTRY_v0_7_DRAFT.md; preserved unchanged"
predecessor adoption record: "RTG_RRF_REPRESENTATION_REGISTRY_v0_7_ADOPTION_RECORD.md"
predecessor revision editor: "ChatGPT; 5 October 2026 scoped v0.7 finalization, unchanged history"
revision editor: "ChatGPT; 20 October 2026 v0.8.4 working-standard adoption"
adoption: "ADOPTED at RRF working-representation scope; separate RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_ADOPTION_RECORD.md"
parent: "RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0_2 §20, §26"
governing methodology: "DSN_METHODOLOGY_v1.3"
---

# 0. Purpose, scope, status grammar, lock

**v0.8.4 review-stage overlay (20 October 2026; subsequently adopted).** This overlay synchronizes adopted DYAD v6.4.18 smooth existence (N14), adopted RECOG v0.3.21 RF-1 owner W3, adopted OFN v0.10 model-contract request N-O10-3 (O10-P3) and its modulus-readout limitations, and conditional Genesis v2.8.9 Q6. The original v0.8.3 publication text and earlier §9/§10 histories below remain archival facts and are not retrospectively revised. This reviewed update adopts no new scientific theorem, physics, carrier, clock, native profile or OPEN-A/B/E closure.

**v0.8.3 publication boundary (19 October 2026).** This adopted RRF working-standard successor to v0.8.2 uses adopted DYAD v6.4.13 §§6.16–6.17 as scientific owner for Lemma F / F1–F3 and the formal ℤ₆ generator. The independent review requested a single §2.4c scope correction: B-6 ⇔ B-an ∧ B-3, so B-6 ⇒ B-an; no strictness claim. Earlier v0.8.2/v0.8.1 histories and source receipts remain historical text. The preceding v0.8.3 review overlay records the *prepublication* state, not the current adoption status. Adoption covers RRF working representation discipline only, and not new physics, mathematical theorem ownership, analytic/smooth existence or G2 realization. See the separate v0.8.3 adoption record and §10.3.

**v0.8.3 review overlay (19 October 2026; NOT ADOPTED).** Adopted DYAD v6.4.13 §§6.16–6.17 is the scientific owner for Lemma F, smooth clock bridge/uniqueness/root commutation (F1–F3), and the formal ℤ₆ generator. Its OPEN 20 differentiates **B-an**, **B-6**, and **B-∞ existence** (all OPEN) from **B-∞ flat uniqueness** (CLOSED at the stated C∞ scope). The original v0.8.2 publication boundary immediately below remains historical, not overwritten. No new physics or G2 realization is selected. `[import: DYAD v6.4.13 §§2, 6.16–6.17; RID: DYAD-CAND-FLAT-CENTRALIZER] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]`

**v0.8.2 publication boundary (17 October 2026).** This is an **adopted RRF working-standard successor** to v0.8.1, based on the independently reviewed candidate. The adopted owner's v6.4.12 formal results are now directly inspected; previous historical source receipts/changelog remain dated records. Acceptance of imported DYAD proof changes only its owner source status, not RRF OPEN-A/B/E, G2 physical admissibility or existence under OPEN 20. See §10.2 for exact file identities and rerun scope.

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

### 0.2 Current source receipts and inheritance/representation boundary — v0.8.1 adopted, with preserved v0.8 source receipt

These rows supplement rather than rewrite the preserved dated v0.7 receipts in §0.1 and §10. In **adopted v0.8.1**, the additional statements remain scoped proposal/provenance guards; adoption of this RRF working standard does not adopt their pending owner science. The separate v0.8.1 adoption record governs this publication. The source of the baseline is the **exact authenticated 57,524-byte adopted v0.7**, not its preceding draft. Scientific-owner proof grade, work-local adoption and certificate replay remain separate.

| Current source | Verified source location / status | RRF import boundary |
|---|---|---|
| **DYAD v6.4.18 (ADOPTED; N14)** | §6.17 `DYAD-THM-SMOOTH-EMBEDDING` E1–E4; OPEN 20 B-∞ existence CLOSED; B-an/B-6 OPEN | Local C∞ flow embedding, roots, J and involution R exist. E2 uniqueness applies **only** to generators with zero linear part. Construction uses `G_∞^{-n}F^n`, not the old unproved `F^{-n}R_∞F^n` route. No physical G2 or analyticity. |
| **RECOG v0.3.21 (ADOPTED; G3 / RF-1)** | §6.6a orientation RID; §§6.13a–6.16g prior scientific results retained; §7.2 RF-1 | Owner W3 requires `a^-` and `a^+` in one and the same cohomology space. Inter-space transport is a distinct, presently unspecified RRF extension (§6.3). |
| **OFN v0.10 (ADOPTED; N-O10-3 / O10-P3; reference RID RF-O10-01)** | §5.5.1–5.5.7 class-C and modulus/readout contract; `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT` | Class C is a distinct conditional model, **not** a native profile or chosen physical network state; see §6.2a. |
| **Genesis Geometry v2.8.9 (ADOPTED)** | §6.3c `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` | Conditional real C³ planar-product obstruction for class-C Q6 under owner hypotheses; not unconditional physical model selection. |
| OFN v0.9 (ADOPTED) | Complete-state/presentation covariance; RF-O09-03/04; §4.5 and OPEN-OPA; OPEN-PRIMACY-3B/3C | No universal node-coincidence axiom, carrier selection or physical clock derived |
| **DYAD v6.4.13 (ADOPTED; N8/N9, §6.17)** | §6.16 `DYAD-THM-FORMAL-Z6-GENERATOR`; §6.17 `DYAD-CAND-FLAT-CENTRALIZER` **[THM]**, `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` **[THM — conditional]**; OPEN 20 B-∞ flat uniqueness CLOSED | Existing C∞ involutions commuting with six-step `F=T^6` commute **exactly** with primitive `T` and are unique (F1–F2); existing C∞ tangent-identity roots commute with `T` and are unique (F3). B-an, B-6, B-∞ **existence**, physical exchange and distinct network-factor clock contracts remain OPEN. RID prefix `CAND` is a historical identifier, not current grade. |
| **DYAD v6.4.12 (ADOPTED; N7 source synchronization)** | §6.16 `DYAD-ALG-CENT-KERNEL`, `DYAD-THM-FORMAL-CENTRALIZER`, `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`; §6.15 `DYAD-THM-LOCAL-INVOLUTION-GERM`, `DYAD-THM-ANALYTIC-CLOCK-BRIDGE`; OPEN 19 formally CLOSED, OPEN 20 B-an/B-∞ OPEN | Formal uniqueness and analytic *conditional* clock bridge adopted by scientific owner; no analytic/C∞ involution existence, full G2/physical exchange, or convergence of the formal `R_0` / tangent-to-identity `F^{1/2}` asserted |
| RECOG v0.3.20 (freeze candidate, not auto-adopted) | §6.6a `RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY`; §6.16b `RECOG-ALG-BTOKEN-TRANSPORT`; §6.16g `RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS` | Family conjugacy ≠ physical relabeling; section transport ≠ new event rule; CELL-F4 W1–W5 are prerequisites, not a birth law |
| Genesis Geometry v2.8.5 (ADOPTED) / Triadic v1.6 (ADOPTED) | Genesis's child direction/amplitude, apex/UV and source lowering corrections; Triadic §6.15/SG-15 | No physical source/child functional/transverse dimension is selected by these notices |
| ER-2B consolidated v0.2 (noncanonical) and RRF coincidence v0.2 (noncanonical) | Specified projected three-edge map; analytic conditional noninvariance at primitive and six-step clocks | A physical exclusion requires complete-state exchange, actual fixed-state realization, encoding and clock intertwining (§6.2) |
| Communicated RER v0.2 **update plan only** | Proposed closure taxonomy, factor and N=7/8 Stage-2 status; moved into separate noncanonical proposal | Original RER v0.2 and newest Stage-2 certificate unavailable; no theorem/profile/standard adopted (§6.4) |

**v0.8.4 RECOG owner-pin convention.** RECOG v0.3.21 is a synchronization-only release with no scientific RID/grade change; for current consumption, it replaces unchanged live v0.3.14/v0.3.20 scientific imports at §§0.2, 4.1, 4.1a, 4.2, 4.3 and 6.3 (R11/R9/R1/token/F4 as applicable), always preserving their respective RIDs and claim scopes. Historic release statements, §0.1 and dated provenance receipts retain their original source versions. OFN v0.10 is the current consumer/ontology source; OFN v0.9 remains historical.

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
| Formal involution — **owner-adopted, formal only** | `R_0=T^3F^{-1/2}=\widehat h(-I)\widehat h^{-1}` is the **unique formal** `−I`-linear involution commuting with `F=T^6` and it also commutes formally with primitive `T` `[THM] [scope: formal only] [import: DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]`. The delivered **finite** $S_h=h_6(-I)h_6^{-1}$ is exactly involutive and equals `R_0` only through jet degree six under the shared normalizer convention; exact dynamical commutation is **not** established for $S_h$. Analytic existence/convergence remains **OPEN 20 (B-an/B-6)**. **C∞ existence CLOSED** by DYAD v6.4.18 E1–E4 (see current-state §2.4b override); adopted v6.4.13 F1–F3 classify existing smooth germs and roots, while v6.4.18 additionally supplies their local existence. Physical G2 and OPEN-A remain OPEN. |
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

**Unchanged by VF-1:** the formal all-order normal form (odd by $p-q\equiv1\bmod6$); the odd jet $J$; DYAD-THM-NF-REM ($C_7$, $C_D$) and DYAD-THM-PRIM-CTR; the one-return bound, now known to be non-vacuous: $\lvert\chi_1(-z)-\chi_1(z)\rvert\le200\lvert z\rvert^6$ on $0<\lvert z\rvert\le\tfrac1{20}$, $\le60\lvert z\rvert^6$ on $0<\lvert z\rvert\le\tfrac1{40}$ (profiles unmixed; VF-1 does not sharpen these constants or radii); $S_h^2=I$; RRF OPEN-A. R11 is now closed by its separate owner record; VF-1 neither supplies nor withdraws that closure. The covered degree-six provenance is upgraded by RECOG check 9, not by VF-1. Artifact-level identity against `PRR_RRF_REVIEW_v1.zip` and `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` / `outputs/certificate.json` was not re-done here (archives not mounted); recording the written confirmation does not require it.

**RECOG dependency note (v0.7 synchronization).** RECOG v0.3.14 §7 explicitly excludes the degree-ten result from its scientific inputs; its RRF import is convention-only. Section 6.16f nevertheless mentions VF-1 descriptively when warning that chart-symmetry germs do not justify an all-orders analytic gauge. Therefore the precise receipt is **not a load-bearing theorem/certificate premise**, not “absent everywhere.” Check 9 is not a new degree-ten verification. VF-1 retains its existing written-verification provenance unchanged.

### 2.4b Adopted DYAD formal involution receipt (new v0.8.2 candidate; not a new profile)

`[THM] [scope: formal germs for F=T^6; owner-adopted] [import: DYAD v6.4.12 §6.16 #sec-6-16-centralizer; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]` The formal object

\[
R_0=T^3\circ F^{-1/2}=\widehat h(-I)\widehat h^{-1},\qquad F=T^6,
\]

is the **unique formal involution** with derivative `−I` commuting with `F`; it commutes formally with primitive `T`. The tangent-to-identity formal centralizer is the one-parameter family `exp(s log F)` `[import: DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-CENTRALIZER]`. The kernel lemma over **all homogeneous degrees** is `[import: DYAD v6.4.12 §6.16; RID: DYAD-ALG-CENT-KERNEL]`. The lifecycle `DYAD-OPEN-FORMAL-CENTRALIZER` is **CLOSED (formal)** by this owner release; this is not RRF OPEN-A closure.

`[DEF] [scope: finite-versus-formal refusal]` The delivered `S_h=h_6(-I)h_6^{-1}` is an **exact involution of the finite polynomial chart** with only degree-six **dynamical commutation** established. In the shared normalization convention `J_{≤6}R_0=J_{≤6}S_h=S_6`; no exact equality `R_0=S_h`, analytic convergence or physical pole exchange follows. VF-1 (`DYAD-ALG-NF6-DEG10`) concerns the fixed finite `h_6` chart only; it does not obstruct a different analytic or smooth odd chart. The owner §6.15 specifies `DYAD-THM-LOCAL-INVOLUTION-GERM` for primitive `C¹` and six-step `C³` involutions, with appropriate invariant/tube domains.

`[THM] [scope: conditional real-analytic local germs] [import: DYAD v6.4.12 §6.15 #sec-6-15-involution; RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE]` A nonidentity **analytic** local involution commuting with `F=T^6` under the §6.15(b) hypotheses has derivative `−I` and commutes **exactly** with primitive `T`. A `C^∞` six-step involution has the same formal jet as `R_0`; **adopted DYAD v6.4.13 §6.17 F1 now upgrades this to exact primitive commutation** on its stated domain. The §6.15 analytical result remains a distinct earlier owner theorem. Network factor hypotheses `EF=TE` and `EF=T^6E` are still **different contracts**. `[import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]`

`[OPEN] [import: DYAD v6.4.13 §§2, 6.16–6.17; RID: DYAD-OPEN-INVOLUTION-REALIZATION]` **OPEN 20 (B-an):** analytic convergence of `R_0`/`F^{1/2}`; **(B-6):** analytic convergence of `F^{1/6}` / `J`; **(B-∞ existence): CLOSED** for local C∞ germs by DYAD v6.4.18 E1–E4; earlier DYAD v6.4.13 OPEN declaration is historical. `[THM] [scope: DYAD v6.4.13 §6.17 existing C∞ germs; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]` **B-∞ flat uniqueness CLOSED** for existing germs by Lemma F and F1–F3. These are distinct from the unknown existence outcomes. Owner RIDs `DYAD-CAND-FLAT-CENTRALIZER` and `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` retain their historical spelling despite [THM] grade.

`[ALG] [scope: class-wise local existence equivalence, conditional on the owner clock/root results; not a physical realization] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES] [import: DYAD v6.4.13 §§2, 6.16; RID: DYAD-OPEN-INVOLUTION-REALIZATION]` In each of C∞ and analytic categories, a nonidentity primitive-commuting involution (equivalently an odd chart for primitive `T`) exists **iff** a tangent-to-identity square root `Q²=F` exists in that category. The easy direction is `Q=T³R`; the reverse uses F3 for C∞, and the analytic special case of F3 (or formal-root uniqueness plus analytic identity) for Cω, with `R=T³Q^{-1}`. The existence equivalence is an algebraic *consequence* of owner theorems plus the explicitly defined averaging chart (G2 v0.3 §4); it does **not** make the open root/involution exist. No G2 physical factor/encoding is claimed.

**v0.8.4 current-state override (DYAD N14; owner v6.4.18).** `[THM] [import: DYAD v6.4.18 §6.17; RID: DYAD-THM-SMOOTH-EMBEDDING] [scope: C∞ germs at P₁; §6.15 local domain]` E1 supplies a smooth field `X` with `F=T⁶=φ_X¹`, `j∞X=log F`; E3 gives existing smooth tangent-to-identity roots `K_m=φ_X^{1/m}` commuting with `T`; E4 gives an existing smooth `J=T K_6^{-1}` and `R=T³ K_2^{-1}`. Hence **OPEN 20 B-∞ EXISTENCE CLOSED**; B-an/B-6 analytic existence remains OPEN, as does physical G2/OPEN-A. E2 uniqueness is restricted to smooth time-one generators with `DX'(0)=0`—not all generators. The owner construction passes by `G_∞^{-n}F^n`; convergence of the prior `F^{-n}R_∞ F^n` scheme remains unproved. L-SHADOW-POLY is not used. This override governs the live §2.4 NF profile row, the preceding §2.4b owner OPEN record and the following historical §2.4c receipt for **current scientific status only**; earlier version histories and past receipts are not retroactively rewritten.

### 2.4c DYAD N9 receipt: formal ℤ₆ and smooth centralizer (v0.8.3 source sync)

`[THM] [scope: formal only] [import: DYAD v6.4.13 §6.16; RID: DYAD-THM-FORMAL-Z6-GENERATOR]` The canonical formal generator `J=T∘F^{-1/6}` has order six and linear part `A`; `R_0=J³`, `G=J²`. **OPEN 20 B-6** concerns its analytic realization. **B-6 ⇒ B-an** and **B-6 ⇔ B-an ∧ B-3** `[ALG] [import: DYAD v6.4.13 §6.16; RID: DYAD-OPEN-INVOLUTION-REALIZATION]`; whether B-an alone entails B-3 is not established. A finite or formal generator is not a chosen physical pole/triad action.

`[THM] [scope: DYAD §6.17 forward-invariant ball and flat contact; existence not asserted] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-FLAT-CENTRALIZER]` Owner Lemma F states that an `F`-commuting map flat-close to identity is identity on its stated local ball; the RID spelling `CAND` does not indicate its adopted `[THM]` grade.

`[THM] [scope: conditional on an *existing* C∞ germ/root, owner §6.15 domain and §6.17 hypotheses] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]` F1: existing nonidentity six-step involution commutes exactly with primitive `T`; F2: it is unique; F3: existing tangent-identity roots of `F` commute with `T` and are unique. Analytic results are included as a regularity subclass; no convergence or realization is inferred. These theorems do **not** identify physical `σ`, edge encoding `E`, or `EF=TE` with `EF=T⁶E`. At the date of this v0.8.3 receipt, B-an, B-6 and B-∞ existence were open; **current status supersedes this historical receipt**: B-∞ existence CLOSED by DYAD v6.4.18 E1–E4, B-an/B-6 OPEN. The finite-C^r analogue remains unresolved.

`[DEF] [scope: representation and owner boundary]` The physical-clock field remains required even when a C∞ involution commutes with both local clocks: a dynamical factor from network update to `T` is different from a factor to `T⁶`. The separate noncanonical G2 v0.4 review will maintain the full gate contract.

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

**Adopted DYAD owner formal-involution receipt (N7).** `[THM] [scope: formal] [import: DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]` The unique formal `−I`-linear involution commuting with six-step `F=T^6` is `R_0=T^3F^{-1/2}=h_form(-I)h_form^{-1}`; its equality with the finite-chart `S_h` is **only through degree-six jet** under the stated shared normalization convention. Owner formal uniqueness **is now adopted**, not `source-pending`. `[THM] [scope: conditional analytic] [import: DYAD v6.4.12 §6.15; RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE]` A nonidentity analytic six-step commuting involution also commutes with primitive `T` under §6.15(b); neither existence nor physical pole relabeling is established (DYAD OPEN 20; RRF OPEN-A). See §2.4b.

**N9 update (current owner receipt).** In the formal category DYAD v6.4.13 §6.16 registers `J=T∘F^{-1/6}`, `R_0=J³`; for existing C∞ local six-step involutions §6.17 F1/F2 gives exact primitive commutation and uniqueness, not analytic/C∞ existence. See §2.4c; do **not** read this as physical OPEN-A closure. `[import: DYAD v6.4.13 §6.16; RID: DYAD-THM-FORMAL-Z6-GENERATOR] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]`

Typed-covariance criterion for gauge status (Wrap-up §10.2): $O(Sx)=\tau_O(O(x))$ for every admissible $O$, with $\tau_O$ the type's relabeling law — not universal invariance.

**Generator-family limit on OPEN-A.** `[import: RECOG v0.3.14 §6.7 and §6.15; RID: RECOG-THM-TWIN-RADIAL-ACCESS]` The global radial-access theorem concerns the particular symmetric twin $T_s=(\rho-\sin\eta,\eta+\sinh\rho-\sin\eta)$: every initial state with $0<Q<7/200$ eventually reaches $|\rho|\ge\operatorname{arccosh}2$. It contrasts with the selected $T$'s certified local contraction. It is **not** a theorem that exact swap symmetry precludes healing for every admissible shear. RECOG §6.7 explicitly retains $g(\rho)=\tanh\rho$ as an odd, healing-at-cubic-order counterexample. The family law $\Re\mu_6=3b-4a^2$ for $g=\rho+a\rho^2+b\rho^3+\cdots$ has two routes to negative radial drift; removing the quadratic term does not force $b>0$. The diagnostic twins are not new registered RRF physical profiles. OPEN-A is not resolved in favor of a nonlinear physical swap by the $\sinh$ result; R1 remains PARTIAL in RECOG.

### 4.2a Cross-model orientation conjugacy is not physical pole exchange

**Current owner-source pin (v0.8.4).** RECOG **v0.3.21 ADOPTED**, §6.6a, RID `RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY`, is the primary source of the unchanged family-conjugacy result below. OFN **v0.10** is a **consumer cross-reference**, not the theorem owner. The former RECOG v0.3.20 / OFN v0.9 pins appearing below are preserved as dated v0.8.1 text and are not the current-source state.

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

**v0.8.4 current regularity/clock notice.** `[THM] [import: DYAD v6.4.18 §6.17; RID: DYAD-THM-SMOOTH-EMBEDDING]` At the adopted local C∞ germ scope, a smooth involution and smooth roots actually **exist** and commute with primitive `T` (E3–E4); the following v0.8.3 text asserting lack of such existence is an archived statement, not current owner status. **Analytic B-an/B-6 existence and finite-Cʳ classification remain open.** The physical contract still must declare `clock:` because `EF_phys=TE` and `EF_phys=T⁶E` are different factor hypotheses even though the existing C∞ involution commutes with both local clocks. No physical node exchange, network submersion or carrier has been selected.

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

### 6.2a OFN class-C model contract — reference-only, not a native profile (v0.8.4 proposal)

`[DEF] [scope: RRF model-contract entry, not a physics selection] [import: OFN v0.10 §5.5.4; RID: RTG-OFN-DEF-TRIAD-MODEL-CONTRACT] [request: OFN N-O10-3 / O10-P3; reference RID: RF-O10-01]` **Class C** reimposes additive mean-feedback *in the transported carrier*, `F^N_κ(z)_e=N(z_e)-(κ/3)Σ_j N(z_j)`, and is a **different conditional model**, not passive recharting of the raw family and not a `RRF-NET-W-RAW` native-profile equation.

| Contract field | Declared RRF reading / obligation |
|---|---|
| Carrier / operation | Transformed or Bochner-chart modal variables; newly imposed mean-feedback. Passive coordinate transport alone does not define this class. |
| `regularity:` | **Formal**; real `C³` polynomial representatives. **`C∞`**: DYAD v6.4.18 E4 supplies a smooth `J`, and DYAD v6.4.13 F3 plus the E4 existence give an exactly λ-equivariant smooth chart for the local isolated DYAD (`DYAD-THM-SMOOTH-EMBEDDING`; owner-level mathematical realization). Transporting OFN class-C into that chart is a **conditional RRF reading**; OFN/Genesis have **not** separately adopted the resulting class-C family, lock surfaces or physical model realization. **Analytic**: conditional on DYAD OPEN 20 **B-6**; still OPEN. Earlier OFN v0.10 §5.5.4 labels both real branches conditional; that wording predates DYAD v6.4.18 and is not reproduced here as current DYAD status. |
| `clock:` | Primitive `T` / declared primitive class-C update; `T⁶` is derived sampling, not an interchangeable network factor condition. |
| Domain / chart | Local neighborhood of 0; state and readouts in transported `z` or specified `Φ` chart. Raw-W readouts require offset transport/subtraction; no off-surface transfer inferred. |
| `κ:` | Formal contract for `κ∉{0,1,2}`; scoped stability for `0<κ<2, κ≠1`. `κ=2` is excluded from the applicable center reduction, not simply a failed physical Q6 model. |
| Q6 factor exclusion | `[THM] [import: Genesis v2.8.9 §6.3c; RID: GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO]` Applies only under **`(H_spec)`, `μ≠0`, `γ∉{0,2}`** (`γ≡κ` in the OFN class-C parameter convention), real `C³` and the owner's appropriate transported-jet hypotheses. See adopted OFN v0.10 §5.5.3 narrow-Q6 corollary `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT`. No factor prohibition outside this scoped family. |
| Native-profile impact | **None**: four dyad profiles and one provisional `RRF-NET-W-RAW` profile remain unchanged; OPEN-B/E1 not resolved. |

`[DEF] [scope: ψ-modulus readout and representation non-transfer] [import: OFN v0.10 §5.5.7; reference: RF-O10-02]` Within the stipulated fifth-order reduced family, `m(a)=Im(a\bar\mu)` is the scoped modulus. `|c|` determines `m` **only up to** the reflection `m↦2m_*−m`; phase of `c` is representation-dependent. `Im c=0` is neither a canonical chart gauge nor a physical selection principle. A phase readout must state the **primitive clock** and the **transported chart**, and cannot be promoted to a physical chirality observable by this entry alone.

### 6.3 Token, history and network inheritance — interface prerequisites only

`[ALG] [scope: pointer to the preserved §4.3; no duplicate theorem import]` The full B-token transport rule is already registered in **§4.3**; RECOG v0.3.20 §6.16b retains its content. The B-section/count phase lift remains distinct from the primitive-`\eta` N-3A deck state. No duplicate transport claim or competing live version pin is introduced here.

`[OPEN] [import: RECOG v0.3.20 §6.16g; RID: RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS] [scope: missing network-inheritance interface; source classification not regraded]` For the currently registered source/carrier package, `token\to\Delta[a]` is **not yet well-posed**, rather than disproved. RRF records CELL-F4's necessary interface conditions without inventing physical attachments:

| Gate | Missing declaration |
|---|---|
| **W1** | graph, coefficient module, edge cochain and network realization |
| **W2** | dyad→edge/subgraph attachment preserving the relevant token predicate |
| **W3** | event-indexed cochains $a^-$, $a^+$ in the **same** cohomology space, so that $\Delta[a]=[a^+]-[a^-]$ is defined `[import: RECOG v0.3.21 §6.16g; RID: RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS]` |
| **W4** | independence from the event log, count or Track-A clock alone |
| **W5** | conditioning/common-driver quotient distinguishing token-specific writing from shared-driver correlation |

`[OPEN] [scope: RRF extension, **not** RECOG W3; no map registered]` If pre- and post-birth classes naturally belong to different spaces `H⁻`, `H⁺`, an extension must explicitly supply an appropriate typed comparison into **one common cohomology space** `H`, for example maps `j⁻:H⁻→H`, `j⁺:H⁺→H`, with justified algebraic and event-domain semantics, and then define `Δ_H[a]=j⁺[a⁺]-j⁻[a⁻]`. This is a **new missing-interface obligation**, not a currently registered transport, not an automatic birth law and not a restatement of RECOG W3. RER G9/1 should cite owner W3 separately from this extension.

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
12. That the **formal uniqueness theorem by itself** supplies analytic convergence, a physical pole exchange or exact equality with the finite `S_h` beyond the shared degree-six jet. **Current v0.8.4 status:** local **C∞ existence is now CLOSED** by DYAD v6.4.18 `DYAD-THM-SMOOTH-EMBEDDING` E1–E4, while B-an/B-6 analytic existence remain OPEN; v6.4.13 Lemma F/F1–F3 separately close smooth uniqueness/commutation. Physical G2/OPEN-A and network-factor realization remain OPEN (§§2.4b–c, 6.2).

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

- **v0.8.4 — ADOPTED (20 Oct 2026; RRF working representation standard):** DYAD v6.4.18 E1–E4 / N14 B-∞ C∞ existence CLOSED with E2 scope and proof-route guards; RECOG v0.3.21 owner W3 RF-1 same-space wording and explicitly OPEN interspace extension; OFN v0.10 N-O10-3 (O10-P3) class-C conditional model-contract row and ψ-modulus readout guards, with Genesis v2.8.9 Q6 conditional RID; owner-first RECOG/OFN source receipts. Older v0.8.3 and preceding histories unchanged. RER Phase A G9 request answered in separate editor response; 4 dyad + 1 provisional profiles and OPEN-A/B/E preserved. No owner mathematics, executable certification or physics adoption.

- **v0.8.3 — ADOPTED as RRF working representation standard (19 Oct 2026):** DYAD v6.4.13 N8/N9 source receipts for formal ℤ₆ generator (`DYAD-THM-FORMAL-Z6-GENERATOR`), owner-adopted Lemma F (`DYAD-CAND-FLAT-CENTRALIZER` [THM]) and F1–F3 (`DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` [THM conditional]); OPEN 20 B-∞ flat uniqueness CLOSED while B-an, B-6 and B-∞ existence OPEN. The C∞/analytic odd-chart–square-root *existence equivalence* is registered as an algebraic consequence of those owner results and the G2 averaging chart, not as an existence proof. C∞ six-step involution exact primitive commutation adopted at §6.17 domains; network factor clocks remain distinct. The reviewer-requested §2.4c qualifier limits B-6 to `B-6 ⇔ B-an ∧ B-3` (hence `B-6 ⇒ B-an`), without claiming strictness. Four dyad profiles, OPEN-A/B/E and predecessor publication history unchanged; source and certificate boundaries in §10.3 and separate adoption record.

- **v0.8.2 — ADOPTED as RRF working representation standard (17 Oct 2026):** DYAD v6.4.12 N7 owner-RID import: OPEN 19 formally CLOSED, `DYAD-THM-FORMAL-CENTRALIZER`, `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`, `DYAD-THM-ANALYTIC-CLOCK-BRIDGE`, separate OPEN 20 B-an/B-∞. G1 source-pending language corrected; analytic six-step versus primitive clock bridge imported conditionally without identifying network-factor clocks. VF-1 **mathematical scope unchanged; primary owner provenance now pinned** to `DYAD-ALG-NF6-DEG10` (§2.4a), retaining earlier written verification as supplementary evidence. §2.4b distinguishes the owner OPEN 20 status from the RRF/SESSION analytic odd-chart/square-root existence equivalence. §6.2 pins all three relevant owner RIDs; §0.2 corrects the convergence object (`R_0`/`F^{1/2}`, not polynomial `h_6`). §8.12 updated to owner-adopted *formal* theorem with unchanged realization/physical nonclaims. The distinct G2 v0.3 noncanonical review remains a separate interface record. Older v0.8.1 and v0.8 histories preserved verbatim. Separate v0.8.2 adoption record governs this **working-standard only** release; physical G2, OPEN-A/B/E and OPEN 20 remain open.


- **v0.8.1 — ADOPTED as RRF working representation standard (16 Oct 2026):** owner-RID-first orientation pin restored to RECOG v0.3.20 §6.6a with OFN v0.9 IMP-O09-03 consumer cross-reference; §2.3 rank-typing guard repinned to adopted OFN v0.9 §4.4 `RTG-OFN-DEF-RANK-TYPING`; prior optional §6.4 RER plan moved to `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md` with one registry pointer; reported formal-G1 identity/uniqueness pointer added strictly as **unverified cross-stream report** with finite-vs-formal distinction; §6.2 separates node exchange from edge-slot exchange and records regularity/clock as **OPEN decisions**. Review refinements: both import tags use the §0 `; RID:` grammar (including the §2.3 table cell); the adopted v0.8 §10 publication paragraph is retained verbatim, with candidate updates in a separate paragraph; §3.1 registers Triadic v1.6 §7.4/CN-05 as a **convention-only proposal** and explicitly records the conditional $Q_c^T=\tfrac{\kappa^2}{4}(Q_s^T)^3$ conversion obligation without applying it. No owner theorem or physical model is adopted, no certificate rerun, no native profile/OPEN closure, and the predecessor v0.8 file and adoption record remain unchanged. The separate v0.8.1 adoption record governs this scoped working-standard successor; §8.12 states the already-declared G1 nonclaim explicitly.

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

**v0.8.1 review-stage record (16 October 2026; subsequently adopted):** the §6.4 extraction into a separate RER proposal and the owner-RID/typing/identity source corrections were reviewed **after** the adopted v0.8 release. This paragraph preserves the order of review and does not retroactively edit v0.8 publication history or adoption scope.

**v0.8.1 publication boundary (16 October 2026):** the independently checked revised candidate is finalized as an **RRF working representation standard only**. Finalization resolves the duplicate candidate/supersession header, registers release status and a separate adoption record, and adds §8.12 as a restatement of an existing G1 guard. The earlier v0.8 record and §10 dated publication paragraph are unchanged. No imported source is upgraded, no scientific owner is changed, and no open physical selection is closed.

**Byte provenance:** the **mounted adopted v0.7 file** was validated against the independently recorded full SHA-256 and 57,524-byte length; its historical twelve finalization sites remain documented in the separate v0.7 adoption record. This is a byte-identity check, not a new scientific-source review or certificate rerun.


### 10.2 v0.8.2 candidate source receipt — DYAD N7 (16 October 2026)

- **Inspected directly:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_12.md`, 170,323 bytes, SHA-256 `c2f00eb0832e6aabcbcfd1a3c583d6f1e7b0950a2f8db97d89045ed0bcb438e8`; **ADOPTED**, 16 October 2026. The owner file's §§2, 6.15 and 6.16, §7 outbound notice N7 and Appendix A publication entry were checked; owner theorem RIDs and OPEN 19→CLOSED (formal), OPEN 20→OPEN statuses are present.
- **Installer manifest:** `RTG_DYADIC_v6_4_12_INSTALL_MANIFEST.json`, SHA-256 `55854504897fc55c9523830d1fd7ea04325edacd9daa5dafeed2f2b66489f4cf`. Its `v6_4_11_to_v6_4_12_final.diff` and `v6_4_12_r1_to_final.diff` SHA-256 values match the mounted files. Manifest includes **source-reported** kernel and `R_0` script runs from prior review rounds; those scripts were **not rerun in this RRF preparation**.
- **Predecessor:** `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_1.md`, 80,889 bytes, SHA-256 `1ba4713855a59b51cad8d79f88007380dfe2364f1b638478a927eea68f642c4c`; remains adopted and unchanged until reviewed successor publication. Historical §9 and §10 v0.8/v0.8.1 paragraphs remain unchanged.
- **Non-transfer boundary:** N7 is an **owner-science import** rather than physical G2 realization, analytic square-root convergence, network-factor existence or OPEN-A/B/E closure. New text is a candidate RRF working-standard source synchronization; not an adoption.

**v0.8.2 adoption boundary (17 October 2026):** Reviewed candidate file identity and predecessor hashes are retained in the separate adoption record. Publication changes review-only metadata, installs the owner-primary VF-1 RID, distinguishes the RRF/SESSION analytic existence equivalence from DYAD OPEN 20, corrects the polynomial-versus-formal convergence wording and completes the owner RID list in §6.2. The §10.2 dated candidate receipt remains a historical record; no new source proof execution occurred. All v0.8/v0.8.1 and older historical material is unchanged.


### 10.3 v0.8.3 review receipt — DYAD N8/N9 (19 October 2026)

- **Inspected directly:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_13.md` (ADOPTED, 18 Oct 2026), SHA-256 `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542`; §§2, 6.15–6.17, §7/N9 and Appendix release/adoption records. The source contains both adopted scientific claims and historical DRAFT records; only current adopted §6.17 status is imported. Original standalone Lemma F v0.3 script and archive were **not** separately mounted/rerun in this RRF pass.
- **Adopted predecessor:** `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_2.md` SHA-256 `f09dbb12f4b65b13c3f08ec049dcd701b04ca24c4b55876b565868f288555461`; no v0.8.2 body/history modified. Distinct `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW_v0_4_REVIEW_CANDIDATE.md` is a separate noncanonical consumer note.
- **Non-transfer:** Exact smooth commutation and root uniqueness are conditional on the *existence* and the domain of the candidate germ/root. No analytical B-an/B-6 existence, physical pole relabeling, G2 submersion/factor, or new RRF profile is claimed. The finite `h_6` involution is not identified with formal `R_0` beyond degree six by an owner theorem.
- **RRF-only mathematics kept outside the owner ledger:** a separate SESSION review evaluates VF-1 and the involution parity to locate the first nonmatching homogeneous jet of `S_h` and `R_0`. That inference is **not** promoted here to owner-grade nor used to select a physical representation.
- **Publication gate:** This is a review candidate. A separate reviewer decision, real final diff, and adoption record are required before v0.8.3 can supersede v0.8.2.

**v0.8.3 adoption boundary (19 October 2026).** The preceding §10.3 receipt and candidate publication gate above remain archived as the state at review. The independently reviewed candidate was accepted subject to one bounded source-scope correction in §2.4c, and released with publication metadata and this separate adoption boundary. The adoption record identifies exact final bytes/hash, predecessor/candidate identities, and distinct G2 v0.4 acceptance. This release did **not** rerun owner certificates or amend the historical §10.2/v0.8.2 release boundary. OPEN-A/B/E, OPEN 20 B-an/B-6/B-∞ existence, and physical G2/network realization remain unresolved.

### 10.4 v0.8.4 candidate receipt — 20 October 2026

The successor candidate is based on the exact adopted v0.8.3 bytes (SHA-256 `b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187`). Sources directly inspected in this editorial update: DYAD v6.4.18 §6.17 / N14, RECOG v0.3.21 §6.16g / RF-1, OFN v0.10 §5.5.3–§5.5.7 / RF-O10-01–02, Genesis v2.8.9 §6.3c and RER's 20 Oct request. No scientific scripts were executed. The candidate is NOT ADOPTED; v0.8.3 governs until independent review and a separate adoption record. The old source-receipt tables and dated publication boundaries above are retained as historical text; new current-state overlays supersede only their live status claims.


**v0.8.4 adoption boundary (20 October 2026).** The immediately preceding §10.4 candidate receipt remains an unchanged historical review-state record. The independently reviewed revised candidate (107,629 bytes; SHA-256 `fc53acff20c17e152884bc1835d4de2d4354a406f4d63262cdb04c200e2cab9e`) was accepted without further scientific text revision. Publication changes release metadata, marks this version adopted at RRF working-standard scope, and adds this separate adoption boundary and adoption record. The two input diffs from the review are identified in the adoption record. Adopted predecessor v0.8.3 and all earlier publication paragraphs remain unchanged. DYAD owner certificates were not rerun; no OPEN-A/B/E, analytic B-an/B-6, physical G2, RER receiver gate or external consumer adoption status is changed. The optional §6.2a F3 owner-RID restatement and §2.4b wording refinement are deferred editorial suggestions, not adoption conditions.
