# Dyadic Oscillator DSN — owner-adoption draft for the return-enclosure package
**Editor:** Claude (Dyadic DSN editor) · **Date:** 22 Sep 2026
**Purpose:** answer the "DYAD owner actions" row of `REVIEW_INTEGRATION_AND_OWNER_ACTIONS_v1.md` with concrete, ready-to-install text for the next Dyadic revision (v6.4.9 → v6.4.10). This is a **draft for the PI's adoption decision**, not an installed edit. Status axes kept separate per Methodology v1.3: evidence/review (done) ≠ owner adoption (this draft, pending) ≠ downstream closure (untouched).
**Reviewer harness:** `dyad_referee_p2b_v2.py` (48 asserting checks, exit-coded, independent reconstruction) closes the "no reviewer-specific driver" gap noted in the handoff. Two harness-side assumptions were caught by its own asserts on first run and corrected (the $h$-count convention; and the false generalization $a_{32}=6\bar\lambda n_{32}$ — see item 5).

## 1. Corrections `[COR]`
- **COR-RE-1 (artifact registry).** `jet1_deg5.json` is the **raw one-step $W$-jet, degree ≤ 5** (input to normalization). Replace the description "one-step normalized coefficient dictionary." Coefficients unchanged; label was wrong. *(P0–P1 audit, independently verified.)*
- **COR-RE-2 (script registry).** `gauge_bridge_p6.py`: "prints diagnostics; **no exit-code acceptance gate**." Any status that rested on its exit 0 is re-read as "ran," not "verified." `normalize_p6_liegauge_exact.py`: "mp.dps=120 numerical with tolerance pruning; builds $\Phi=\mathrm{id}+h_4+h_{5,\rm nr}$; does **not** zero non-resonant channels; preserves all raw coefficients through degree 5."
- **COR-RE-3 (withdrawn record).** The $(C_6,q_{\rm ctr},q_{\rm in})=(64,\tfrac1{256},\tfrac1{1024})$ delivery is **withdrawn as unsupported, not falsified.** Do not import.

## 2. New scope guard `[DEF]`
- **SG-19 — normalization-object guard.** *Archival coordinate change* ($\Phi_{\rm archive}$), *log-channel projection* ($G_{\rm proj}=\exp(P\log F_W)$), and *polynomial conjugacy* ($f\circ h=h\circ n$, additive $h$, resonant $h_n=0$) are three distinct operations. A "normalized coefficient" claim must name which. $G_{\rm proj}$ is never called "the normalized return." Coefficients under one operation are not transferred to another (the obstruction $c^{\rm raw}_{05}-a_{05}=\tfrac{-13+3i\sqrt3}{576}\ne0$ is the standing example).

## 3. Results to register `[ALG]` (owner IDs proposed; PI to confirm numbering)
| Proposed RID | Statement | Evidence |
|---|---|---|
| **DYAD-ALG-NF6** | One-step polynomial normalizer $h=\mathrm{id}+h_2+\dots+h_6$ (23 coefficients incl. linear, exact in $\mathbb{Q}(i\sqrt3)$), resonant $h_n=0$; $h_2=-\tfrac{1+i\sqrt3}{12}z^2-\tfrac13z\bar z+\tfrac{1-i\sqrt3}{24}\bar z^2$; unique $h_2$ removing $F_4$ (rank 6). Six-step normal-form jet $J=z+\mu z^2\bar z+a_{32}z^3\bar z^2+a_{05}\bar z^5$ with $a_{32}=-\tfrac{97}{432}+\tfrac{197i\sqrt3}{324}$, $a_{05}=-\tfrac{49}{8640}-\tfrac{307i\sqrt3}{25920}$. | P0–P1 package; recovered solver; two Claude reconstructions; harness |
| **DYAD-ALG-NF6-OBS** | Obstruction: no identity-linear polynomial change through degree 5 conjugates the raw-$c_{05}$ three-channel model to the primitive return ($a_{05}$ independent of all cubic corrections). | same |
| **DYAD-ALG-PRIM-CTR** | Primitive contraction: $\|R^{\rm prim}_{\ge6,\rm rad}\|\le108\,Q^3$ on $Q\le\tfrac1{400}$; $0<Q-\tfrac32Q^2\le Q(T^6x)\le Q-\tfrac12Q^2$; six-phase invariant tube from $Q\le\tfrac1{625}$; exact seed $(\tfrac1{100},\tfrac1{250})$, $Q_0=\tfrac{19}{250000}$, admitted. (v1 profile $(1560,\tfrac1{3600},\tfrac1{10000})$ recorded as weaker baseline.) | P2-A v2; reviewed |
| **DYAD-ALG-NF-INV** | $h$ injective on $\|z\|\le\tfrac1{10}$; inverse on $\|W\|\le\tfrac9{100}$; $\|Dh^{-1}\|_2<\tfrac87$; $\tfrac{225}{256}\|z\|^2\le Q_{\rm prim}\le\tfrac{289}{256}\|z\|^2$ (comparison, **not** identity). | P2-B v1/v2; reviewed |
| **DYAD-ALG-NF-REM** | Radius-indexed remainders for $\widehat F=h^{-1}F_Wh$: $(\tfrac1{20}:\,C_7{=}100,\ C_D{=}1000)$, $(\tfrac1{40}:\,30,\ 250)$; constants travel with radius and chart. Full P2-A tube maps inside $\|z\|<\tfrac1{20}$. Normalized one-orbit contraction $0<q-\tfrac32q^2\le\|\widehat F\|^2\le q-\tfrac12q^2$, $q\le\tfrac1{400}$. | P2-B v2; reviewed |

## 4. Ledger consistency notes (no change to existing RIDs)
- The one-step ledger value $c^{(1,6)}_{05}=\tfrac{43}{17280}-\tfrac{227i\sqrt3}{155520}$ **equals** the solver's $n_{05}$ and satisfies $a_{05}=6\bar\lambda\,n_{05}$; the existing DYAD-ALG-BRIDGE-LEMMA ($\mu_p=p\bar\lambda\nu_3^{(1,p)}$) is confirmed exactly at $p=6$. **No renaming.**
- $[W^3\bar W^3]\Delta Q_6=\tfrac{47}{54}$ reproduces the §6.5 backbone *number* as a raw radial coefficient / fixed-radius angle average. Wording to install: "coefficient-level agreement; not an independent derivation of the long-orbit backbone recursion, and not an identification of $Q_{\rm prim}$ with normalized amplitude."
- SG-10 (Im $\nu_5$ not gauge-invariant) is untouched and consistent: the (3,2) slot is the one where conventions differ.

## 5. A note for the ledger, from the harness
$a_{32}\ne6\bar\lambda\,n_{32}$: the $(3,2)$ slot of $n^{\circ6}$ carries second-order $n_{21}$ cross terms, so the bridge lemma transports the cubic slot and the $\bar z^5$ lattice slot but **not** the $(3,2)$ slot. Worth one sentence under DYAD-ALG-BRIDGE-LEMMA so no one repeats my mistake.

## 6. Explicitly *not* adopted / not closed
R8 (manifold entry), R9 (two-history memory), R10/R11 (await RECOG reconciliation on the fixed chart), quantitative GAP-LOCK angular conditions, historical $\Phi_1$ byte identity, optimality. NUMGEN's L1 ownership is not transferred. No geometry/source-amplitude/cascade/physical-selection consequence is claimed.

## 7. Immutable evidence to register
`DYAD_RETURN_ENCLOSURE_P0_P1_evidence.zip`, `…_P2B_v2_evidence.zip` (contains P2-A v2 / P2-B v1 baseline), the three review notes, and `dyad_referee_p2b_v2.py` + `dyad_return_qchi_exact.py` (reviewer backend). Register by hash; the handoff's `archive_integrity.json` already carries the 56 member hashes.

*Agreement with the handoff's [HEUR]: stop sharpening; next unit is R11 final-chart reconciliation, then R9 with R8 as a separate computation.*
