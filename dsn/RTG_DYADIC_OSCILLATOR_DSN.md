# RTG_DYADIC_OSCILLATOR_DSN_v6.4.20

**Title:** RTG Dyadic Oscillator Study — Canonical Scientific Ledger  
**Edition:** v6.4.20 — adopted 21 October 2026  
**Status:** ADOPTED — owner/PI adoption recorded 21 October 2026 (`DYAD v6.4.20 — OWNER ADOPTION AUTHORIZED`) after external review of DRAFT r2 (`DYAD v6.4.20 DRAFT r2 — REVIEW ACCEPTED`; r2 SHA-256 `f2030f853b94a7caa1d1d7c4afd8bdf9b6059582d331100bb0033226fd68465e`). Earlier reviews: `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED` (P1 working file `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905`) and `v6.4.20 r1 — REVIEW ACCEPTED WITH MINOR CORRECTIONS` (r1 `a5c70f5b1468ab01ba1cdf932fb9205c4bf00976a2b6523e8b90210e5e457c4a`). Built by `build_dyad_v6_4_20_r1.py` (P1 → r1), `build_dyad_v6_4_20_r2.py` (r1 → r2) and `release_v6_4_20.py` (r2 → this file, labels and metadata only). Release record: `RTG_DYADIC_v6_4_20_RELEASE_RECORD.md`; external verification of this file's SHA-256 is recorded separately.  
**Scope:** The primitive 2D non-symplectic dyad map, its six-step resonant dynamics, ISP crossing geometry, normalized $p$-step structure, and $p$-resonance generalization program.  
**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19` (adopted 20 Oct 2026, `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`; kept unchanged as the historical adopted release). Lineage and all release records: Appendix A.  
**Companion and consumer editions:** one current-edition table, §7.0.  
**DSN Methodology:** `DSN_METHODOLOGY_v1.3`. Legacy compound tags are rendered in canonical form (normalization map after the Local Tag Aliases); no grade changes.  
**Programme tier:** Tier 3 — Continuous Programme, upstream source (Programme Overview §6).  
**Status summary:** The dyad map has theorem-grade and exact-algebraic certification for the six-step resonant module ($c_{21}$, the local quintic normalization pipeline, OPEN 11, OPEN 18); the local return enclosure of §6.14 (exact degree-6 normalizer and jet, primitive contraction with invariant tube, inverse coordinates, normalized remainders); the OPEN 3 spiral-residual results and the primitive-variable remainder (OPEN 21; conditional on `RECOG-THM-R9-MEMORY`); the L-PHASE angular remainder on row A (`[THM]`; the constant $\tfrac{403}{250}$ is an upper bound); the formal centralizer and ℤ₆ generator (§6.16); Lemma F with F1–F3 and the smooth flow embedding (§6.17). OPEN 9 is PARTIAL: low-degree anti-holomorphic vanishing is `[ALG]` for $b\in\{2,3,4\}$ ($p\ge b+2$), it fails at $b=5$ for every $p\ge6$, all-$b\ge5$ persistence is `[OPEN]`, and the $q=4,(0,3)$ phase law is closed for all $p$. OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-an and B-6 are OPEN. v6.4.20 adds the ATLAS P1 scientific corrections and the P2 interface work (Appendix A). Its 13 new RIDs are registered by this adoption; no earlier RID is renamed or regraded.  
**Adoption and draft records:** Appendix A, "v6.4.20 — adopted 21 October 2026", "v6.4.20 DRAFT r2" and "v6.4.20 DRAFT r1"; session records `DYAD_ATLAS_P2_R2_CORRECTION_SESSION_v0_1.md` and `DYAD_ATLAS_P2_EDITORIAL_INTERFACE_SESSION_v0_1.md`. The v6.4.19 header, adoption metadata, release summaries and footers are preserved verbatim there.

## Local Tag Aliases

| Local alias | Expands to | Used for |
|---|---|---|
| `[ALG by convention]` | `[ALG]` `[conv: NAME]` | exact result conditional on named normalization convention |
| `[ALG within implemented family]` | `[ALG]` `[family: DESC]` | exact result within explicitly stated parameter class |
| `[ENG/NUM strong]` | `[ENG]` co-certified with `[NUM strong]` | engineering result cross-verified numerically |
| `[ALG/NUM]` | `[ALG]` co-certified with `[NUM]` | exact identity cross-verified numerically |

`[DEF]` Ledger entries use canonical claim statuses from `DSN_METHODOLOGY_v1.3`. `[v6.4.20]` Legacy compound spellings in live text are rendered by the normalization map below; every rendering keeps the grade token. The four aliases above remain declared.  
`[DEF]` Canonical tags such as `[ALG via IA]` and `[THM-ALG via IA]` are used directly and do not require local aliasing.

**Tag normalization map (v6.4.20).** Left: legacy spelling in v6.4.19 / P1 live text. Right: canonical rendering. The grade token is unchanged in every row; qualifiers move into `[scope:]`, `[assuming:]`, `[proof:]` or a version marker.

| Legacy spelling | Canonical rendering |
|---|---|
| `[ALG, exact under OPEN-P0 representation-phase convention]` | `[ALG]` `[assuming: OPEN-P0 representation-phase convention]` |
| `[ALG, exact]` | `[ALG]` |
| `[ALG structure / NUM strong]` | `[ALG]` `[scope: structure]` `[NUM]` `[scope: strong numerical evidence]` |
| `[ALG structure]` | `[ALG]` `[scope: structure]` |
| `[ALG candidate]` | `[CAND]` `[target: ALG]` |
| `[ALG finite sweep]` | `[ALG]` `[scope: finite sweep]` |
| `[ALG validation]` | `[ALG]` `[scope: validation]` |
| `[ALG — formal second order; remainder not certified]` | `[ALG]` `[scope: formal second order; remainder not certified]` |
| `[ALG — formal]` | `[ALG]` `[scope: formal]` |
| `[ALG / ENG]` | `[ENG]` `[ALG]` |
| `[ENG / NUM strong]` | `[ENG]` `[NUM]` `[scope: strong numerical evidence]` |
| `[NUM strong]` | `[NUM]` `[scope: strong numerical evidence]` |
| `[CAND/conditional]` | `[CAND]` `[scope: conditional]` |
| `[HYP inherited]` | `[HYP]` `[scope: inherited]` |
| `[THM — analytic]` | `[THM]` `[scope: analytic]` |
| `[THM — conditional on RECOG-THM-R9-MEMORY]` | `[THM]` `[assuming: RECOG-THM-R9-MEMORY]` |
| `[THM — conditional on R9]` | `[THM]` `[assuming: RECOG-THM-R9-MEMORY]` |
| `[THM — conditional on T1]` | `[THM]` `[assuming: T1]` |
| `[THM — conditional]` | `[THM]` `[assuming: hypotheses stated in the entry]` |
| `[THM/ALG, all-$p$]` | `[THM]` `[proof: exact algebraic identity]` `[scope: all $p=4s$, $s\ge2$]` |
| `[THM/ALG]` | `[THM]` `[proof: exact algebraic identity]` |
| **`[CLOSED v6.4.9, THM/ALG]`** | **CLOSED (v6.4.9)** `[THM]` `[proof: exact algebraic identity]` |
| `[COR v6.4.11: "iff $b\le4$" shorthand withdrawn]` | `[COR]` `[v6.4.11: "iff $b\le4$" shorthand withdrawn]` |
| `[COR v6.4.10]` | `[COR]` `[v6.4.10]` |
| `[COR v6.4.11]` | `[COR]` `[v6.4.11]` |
| `[P1 COR]` | `[COR]` `[v6.4.20]` |
| `[P1]`, `[P1: …]` | `[v6.4.20]`, `[v6.4.20: …]` |

**Section headings.** A §6 heading lists the grades of the entries in that subsection ("entry grades: …"), computed from the entry tags. It is an index, not a grade of the section. A subsection without tagged entries (§6.13, a specification table) keeps its former heading tag.

**Version markers.** `[v6.4.20]` marks text introduced by the ATLAS P1 and P2 passes (the P1 working file wrote these as P1 markers). `[v6.4.20 entry]` marks a whole new entry; a RID new in v6.4.20 carries `[v6.4.20; RID registered at adoption, 21 Oct 2026]`.

**RID tag convention.** Each identifier has exactly one RID tag in live text (Appendix A, a historical record, is excluded): for an OPEN identifier, the §2 registry header; for an artifact identifier, the §8 registry line; otherwise the first §6 entry, else the first §2 entry. Every other live mention is a code span.

**Current-grade lookup for CAND-prefixed identifiers.** The prefix is part of the identifier, not a grade (Methodology v1.3).

| Identifier | Current status | Where |
|---|---|---|
| `DYAD-CAND-FLAT-CENTRALIZER` | `[THM]` (Lemma F) | §6.17 |
| `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` | `[THM]` `[assuming: hypotheses stated in the entry]` (F1–F3; existence of the $C^\infty$ object is a hypothesis) | §6.17 |
| `DYAD-CAND-P0-DYADIC` | `[CAND]` `[scope: conditional]` | §6.11, §6.12 |
| `DYAD-CAND-VANISH-B3`, `DYAD-CAND-VANISH-B4` | retired identifiers; promoted in v6.2 to `DYAD-ALG-VANISH-B3`, `DYAD-ALG-VANISH-B4` `[ALG]` | Appendix A, v6.2 |
| `DYAD-CAND-PHISTAR-ENTRY-PHASE` | never a Dyadic identifier (former NUMGEN pin; removed by NUMGEN v1.20.8, notice N3) | §7 notices |

---

## §1. Current Canonical State {#sec-1-canonical-state}

`[DEF]` `DYAD-DEF-PRIMITIVE-MAP` `[v6.4.11, provisional]` **Dyad map.** The primitive continuous dyadic generator is the 2D non-symplectic map
$$\rho' = \rho - \sin\eta, \qquad \eta' = \eta + (e^\rho - 1) - \sin\eta.$$
*Custody (OFN v0.9 CUST-O09-01 / REQ-O09-04):* Dyadic is the source lineage and owns this definition. Genesis uses `GEN-DEF-PRIMITIVE-MAP` for the same formula; that RID is **not** retired by this document. `[v6.4.13]` Genesis v2.8.6 (G-B02, retained in v2.8.7 §1) records it as an import/alias of DYAD-DEF-PRIMITIVE-MAP (notice N1 answered); both identifiers resolve to the identical formula and neither owner's theorem RIDs change.

`[ALG]` Fixed points: $P_1=(0,0)$ elliptic order-6; $P_2=(0,\pi)$ hyperbolic saddle.

`[ALG]` `[v6.4.20]` **Fixed-point scope.**

| Chart | Fixed points of $T$ | Note |
|---|---|---|
| Lifted chart $(\rho,\eta)\in\mathbb R^2$ | $\{(0,m\pi):m\in\mathbb Z\}$ | lifts of $P_1$ ($m$ even) and $P_2$ ($m$ odd) |
| Wrapped cylinder ($\eta$ mod $2\pi$), zero winding | $P_1=(0,0)$, $P_2=(0,\pi)$ | the fixed points used in §6 |
| Wrapped cylinder, winding $k\ge1$ | $(\log(1+2\pi k),0)$ and $(\log(1+2\pi k),\pi)$ | on the lift $T$ adds $2\pi k$ to $\eta$, so these are not fixed in the lifted chart |

Local results concern germs at $P_1$ under the §6.15 domain convention unless stated otherwise. The winding inventory agrees with RECOG §6.3 (v0.3.22). Owner check: `dyad_p2_math_checks.py` M9.

`[THM]` The map is not globally area-preserving:
$$\det J = 1+(e^\rho-1)\cos\eta.$$
The equality $\det J=1$ holds on $\rho=0$ and on $\cos\eta=0$, not globally. Non-symplectic structure is the local mechanism allowing $Q_{\rm true}$ to decay.

`[ALG]` **Primary observable.** $Q_{\rm true} = \rho^2 - \rho\eta_{\rm wrap} + \eta_{\rm wrap}^2 = |W_{\rm DSN}|^2$ where $W_{\rm DSN} = u + iv$, $u = \rho - \eta_{\rm wrap}/2$, $v = (\sqrt{3}/2)\eta_{\rm wrap}$. This is the $p=6$, $K=1$ Birkhoff frame. $Q_{\rm euclid} = \rho^2 + \eta_{\rm wrap}^2$ is comparison-only.

`[THM]` **Cubic coefficient.** $c_{21} = -\frac{1}{2} - i\frac{2\sqrt{3}}{3}$. `DYAD-THM-C21`

`[ALG]` **Canonical constants.** $\tau = 2\sqrt{3}/3$, $|\sigma|^2 = 19/12$, $\lambda_{\rm DSI} = e^{\pi\sqrt{3}} \approx 230.76$. Definition-ledger identities (v6.4.11, §6.3): $Q_{\rm true}$ is the unique $A$-invariant quadratic form up to scale; $\tau=(\det B)^{-1/2}$; $F=T^6$ is a cubic parabolic germ.

`[ALG]` `[scope: fixed-radius uniform-angle mean in the raw $W$-frame]` **Backbone coefficient $47/54$.** $\mathcal A_{\rm raw}(Q):=\tfrac1{2\pi}\int_0^{2\pi}|F_W(\sqrt Q\,e^{i\theta})|^2d\theta=Q-Q^2+\tfrac{47}{54}Q^3+O(Q^4)$ (§6.5). `[COR]` `[v6.4.10]` The former unqualified scalar backbone map did not identify its averaging/projection operator; the long-orbit backbone law $Q_m\sim1/(m+\kappa_{\rm bb})$ (`[v6.4.20]` $\kappa\to\kappa_{\rm bb}$; certified leading decay: §6.5) is retained as a historical fitted surrogate under its own definition, and its identification with $\mathcal A_{\rm raw}$ or with any final-chart quantity remains `[OPEN]` as a fitted-backbone identification problem. RECOG R11 is CLOSED at its final-chart ledger scope; the SG-19 non-transfer guard remains.

`[ALG]` **One-block burst** (on the positive real primitive ray $(\rho,\eta)=(t,0)$, $Q_0=t^2$): $Q_6 = Q_0 - Q_0^2 - \frac{5}{24}Q_0^{5/2} + \frac{37}{40}Q_0^3 + O(Q_0^{7/2})$. `[COR]` `[v6.4.10]` The half-power term $-\frac5{24}Q_0^{5/2}$ is nonzero on this ray (it is $P_5$ restricted to the ray, §6.14); earlier statements omitting it are superseded. Coefficient $37/40$ is distinct from the raw fixed-radius angular-mean coefficient $47/54$; a different symmetrized observable, if intended, needs its own definition (the fixed-radius mean $\mathcal A_{\rm raw}$ is already defined in §6.5).

`[THM-ALG via IA]` **OPEN 11 closed.** Chirality closure on canonical family $(\rho_0,\eta_0)=(0,q)$, $q\in(0,2]$: T1/F1 refinement residual-free throughout. `DYAD-THM-OPEN11`

`[THM-ALG via IA]` **OPEN 18 closed.** First-footprint branch monotonicity: $dQ/dq>0$ and $d\Theta/dq<0$ on both branches; $q=q_*$ is the branch split. `DYAD-THM-OPEN18`

`[ALG]` `[conv: Lie strict-kernel gauge]` **OPEN 13 archived.** Archival Lie-gauge 6-step object: $h_4$ exact with coefficients in $\mathbb{Q}(i\sqrt3)$ (real parts in $\mathbb Q$, imaginary parts in $\mathbb Q\sqrt3$; exact recomputation `dyad_h4_archival_exact_check.py`, v6.4.21), $c_\theta^{(6)} = -119\sqrt{3}/648$. `[COR]` `[v6.4.10]` The historical statement "$h_3=0$" refers to the **non-resonant cubic part of the return logarithm** in the archival coordinate change $\Phi_{\rm archive}=\mathrm{id}+h_4+h_{5,\rm nr}$ (which preserves every raw coefficient through degree 5); it is **not** a statement about the one-step polynomial conjugacy, whose $h_3\ne0$ (three channels, §6.14, DYAD-ALG-NF6). $c_\theta^{(6)}$ is retained under its own convention and is not transferred to the conjugacy chart (SG-19; permanent non-transfer guard). The chart quintic phase coefficient is $+\tfrac{89\sqrt3}{324}$ (RECOG-ALG-CHART-LAWS); RECOG R11 is CLOSED (RECOG v0.3.2). Gauge-universal formulations remain `[OPEN]`. `DYAD-ALG-LIEGAUGE-NORM`

`[ALG]` `[conv: Lie strict-kernel gauge]` **OPEN 17 closed through $a_2$.** Intrinsic projection coefficients: $a_1 = 559\sqrt{15}/4860$, $a_2 = 86775991\sqrt{15}/755827200$. Gauge-universal projection remains `[OPEN]`. `DYAD-ALG-A1A2-LIEGAUGE`

`[ALG]` **OPEN 16 partial.** Alias phase at $U=\pi/\tau$: $G_-(\pi/\tau) = 1/(1-i\tau) = 3/7 + (2\sqrt{3}/7)i$, $\arg G_- = \arctan(2\sqrt{3}/3)$. Full $\Pi(Q_0,U,\mathcal{O})$ remains `[OPEN]`. `DYAD-ALG-ALIAS-PHASE`

`[ALG]` `[family: p=5,6,7]` **OPEN 9 finite ledger sealed.** Raw cubic theorem `[THM]`; one-step ledger exact for $p=5,6,7$; $G_{\rm lattice}(5)=0$ `[ALG]` — unique non-trivial degree-4 lattice bridge cancellation. Sub-horizon inheritance conjecture `[RETRACTED]` `[scope: reframed]`: $G_{04}(10)=0$ is an instance of the observed degree-4 raw-vanishing pattern, not divisor inheritance. Universal $q=4,(0,3)$ cancellation `[FAIL]` (channel survives for $p\ge12$); cascade boundary $p=12,q=4,(0,3)$: exact value $-13+15\sqrt{3}/2\ne0$, modulus $\approx 0.0096$. The surviving value is now characterized all-$p$: $Q_p=i\zeta_p^3 M_p$, $M_p\in\mathbb{Q}(\zeta_p)^+$ `[THM]` `[proof: exact algebraic identity]` (DYAD-THM-Q403-PHASELAW, §6.11).

**Local return enclosure (v6.4.10).** `[THM]` In the fixed chart $W=h(z,\bar z)$ (exact degree-6 additive polynomial, the resonant monomial coefficients of each $h_n$ zero): primitive contraction $0<Q-\tfrac32Q^2\le Q(T^6x)\le Q-\tfrac12Q^2$ on $0<Q\le1/400$ with invariant six-phase tube from $0<Q\le1/625$ `[THM]`; $h$ injective on $|z|\le1/10$ with inverse on $|W|\le9/100$ `[THM]`; $|\widehat F-J|\le100|z|^7$, $\|D\widehat F-DJ\|_2\le1000|z|^6$ on $|z|\le1/20$ (and $30$, $250$ on $|z|\le1/40$) `[THM]`. `[ALG]` The exact NUMGEN seed $(1/100,1/250)$, $Q_0=19/250000$, is admitted to the tube. Details, RIDs, scope limits: §6.14.

`[ALG]` `[import: RECOG v0.3.20 §6.10 | RECOG-ALG-NU3-CLOSED-FORM, RECOG-ALG-NU3-NONVANISHING]` `[scope: declared $K_p$ family, $Z$-frame, local cubic order]` **All-$p$ cubic radial contraction (v6.4.11 import).** $\Re\mu_p^{Z}=-p\sin^2(\pi/p)<0$ and $k_{\rm ret}(p)=3$ for every $p\ge5$. Owner: RECOG. Not a statement about arbitrary generators, finite amplitudes or birth mechanisms (§6.11).

`[THM]` `[scope: formal category]` **OPEN 19 closed (v6.4.12).** The formal tangent-to-identity centralizer of the six-step return $F=T^6$ is $\{\exp(sX)\}$, $X=\log F$; the unique formal involution with linear part $-I$ commuting with $F$ is $R_0=T^3\circ F^{-1/2}$ ($=\widehat S$). Analytic involutions commuting with $T^6$ (nontrivial branch) commute exactly with $T$. Convergence/realization is OPEN 20. `DYAD-THM-FORMAL-CENTRALIZER` `DYAD-THM-FORMAL-INVOLUTION-UNIQUE` `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` (§6.15–§6.16)

`[THM]` `[scope: formal]` `[v6.4.13]` **Canonical ℤ₆ generator.** $J=T\circ F^{-1/6}$ is the unique formal map with $J^6=\mathrm{id}$, $DJ(0)=A$ commuting with $F$; $R_0=J^3$. `DYAD-THM-FORMAL-Z6-GENERATOR` (§6.16). `[THM]` `[v6.4.13; scope: local, forward-invariant ball, flat contact]` **Flat centralizer triviality** (Lemma F, §6.17): a map commuting with $F$ and flat-close to the identity is the identity. `[THM]` `[assuming: hypotheses stated in the entry]` Consequences for *existing* $C^\infty$ objects: $C^\infty$ clock bridge, $C^\infty$ uniqueness, smooth roots commute with $T$ (F1–F3). F1–F3 assert no existence; existence is DYAD-THM-SMOOTH-EMBEDDING (§6.17). `DYAD-CAND-FLAT-CENTRALIZER` `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES`

`[THM]` `[v6.4.14]` **Spiral residual, per block (OPEN 3).** In the chart of DYAD-ALG-NF6 the per-block primitive–normalized differences $S_Q=\Delta Q_{\rm prim}-\Delta q$ and $S_\Theta=\Delta\Theta_W-\Delta\Theta_z$ have exact leading terms $[S_Q]_5=DD_3[\mu qz]$, $L_\Theta=[S_\Theta]_3$ (`DYAD-ALG-OPEN3-LEADING`) and certified remainders $|S_\Theta-L_\Theta|\le K_\Theta q^2$, $|S_Q-[S_Q]_5|\le K_Qq^3$ on $|z|\le\tfrac1{20}$ and $|z|\le\tfrac1{40}$ (`DYAD-THM-OPEN3-SPIRAL-REM`, §6.14). OPEN 3 is CLOSED within its defined scope (v6.4.16); P4 is `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` (`[assuming: RECOG-THM-R9-MEMORY]`); the primitive-variable remainder is OPEN 21 (CLOSED, v6.4.17).

`[THM]` `[assuming: RECOG-THM-R9-MEMORY]` `[v6.4.15]` **Asymptotic-phase transfer (OPEN 3b).** The primitive asymptotic phase $\Psi_W=\Theta_W-\tau\log Q_{\rm prim}$ and the normalized $\Psi_z$ differ by the exact static offset $\Delta_0(z_m)$, certified $O(\sqrt{q_m})$; their limits coincide (conditional on RECOG-THM-R9-MEMORY), and the retained memories differ by $-\Delta_0(z_0)=O(\sqrt{q_0})$ (`DYAD-ALG-OPEN3-PHASE-OFFSET`, `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS`, `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`, §6.14).

`[THM]` `[assuming: RECOG-THM-R9-MEMORY]` `[v6.4.17]` **Primitive-variable phase remainder (OPEN 21).** The primitive asymptotic-phase memory satisfies $|M_W-\mathcal P_2(W_0)|\le K'_jQ_0^{3/2}+C_{2,j}(256/225)^2Q_0^2$ on the primitive disks $|W_0|\le3/64$ (row A) and $|W_0|\le3/128$ (row B), with $\mathcal P_2$ the adopted second-order form of DYAD-ALG-OPEN3-PHASE-OFFSET (`DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER`, §6.14).

`[THM]` `[v6.4.18]` `[scope: $C^\infty$ local germs at $P_1$]` **Smooth flow embedding (OPEN 20 B-∞ existence).** $F=T^6$ is the time-one map of a $C^\infty$ vector field $X$ with $j^\infty X=\log F$, unique among $C^\infty$ generators with zero linear part; hence $C^\infty$ realizations of $F^{1/m}$, $J$ and $R_0$ exist and commute with $T$ (`DYAD-THM-SMOOTH-EMBEDDING`, §6.17). Analytic realization (B-an, B-6) remains OPEN.

`[THM]` `[v6.4.19]` `[scope: block base points in $U$ of DYAD-THM-PRIM-CTR; chart row A of DYAD-THM-NF-REM; primitive observable]` **L-PHASE angular remainder, row A (NUMGEN interface).** Along every orbit started in $U=\{0<Q\le\tfrac1{625}\}$, the six-step increment of the increasing primitive phase lift is $2\pi-\tau Q_m+r_m$ with $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$; the one-step increments stay within $\arcsin(0.04654)$ of $\pi/3$ on the tube (`DYAD-THM-LPHASE-ROWA-REMAINDER`, §6.14). L-PHASE itself is NUMGEN-owned; no coefficient is transferred (SG-19).

`[OPEN]` **Immediate frontier:** universal missing-slot rules $Z^{\rm miss}_{p,q,D}$; all-$b\ge5$ persistence; general-coefficient (non-dyadic) cascade. The cubic cascade formula for $q=4,(0,3)$ is **CLOSED all-$p$** (DYAD-THM-Q403-PHASELAW, §6.11). See §2 and §6.11.

`[ALG]` **OPEN-P0-DYADIC structural connection.** The p=6 eigenvalue is the SU(2) half-angle representative of the K₄ ESM face flux: $\lambda=e^{i\pi/3}=e^{iF_f/2}$, $F_f=2\pi/3$ (Pre-Legacy §1.8). The SU(2) half/full-angle energy ratio is $E_{\rm full}/E_{\rm half}=F_f^2/(F_f/2)^2=4$ `[ALG]`. The R11 cascade-gate arithmetic conversion is `[ALG]`; the gate's physical threshold inherits OPEN-GEN-II-7B `[HYP]` status. Whether the SU(2) factor transfers to the OPEN-M source amplitude (giving $\times2$ or $\times4$) is `[CAND]` `[scope: conditional]`: R11 treats $h$ as an external amplitude (Audit-1 = OPEN-M v0.7.1 R16, `UVM-RESULT-AUDIT1`; Genesis SG-5). `[v6.4.11]` OPEN-M v0.7.1 records **no certified numerical deficit** (R15 corrected). `[v6.4.20]` The $0.024$/$4/125$ target inherits five conditions: the reduced birth-race wrapper, the 9C raw-array premise, the large-$g$ limit $\|M\|_B\to2g$, state/window matching, and the source normalization ($m=C_mh$, $Q_s$) (OPEN-M v0.7.1 §§2, 6; Genesis `GEN-OPEN-UVJET-SCOPE`). So this route is an OPEN-M calibration branch, not a deficit correction. See §6.2, §6.6, §6.12, SG-15.

---

## §2. Active Frontier / OPEN Registry {#sec-2-open-registry}

### Priority ordering

There are two queues:

**Handoff queue** — used when a downstream Genesis/Triadic document is being updated:
1. **Dyad-to-triad bridge handoff** — see `dyad_triad_antisymmetric_bridge_v1_1.md`. Dyad exports $\mu$, $\tau$, protection matrix, shear/healing ratio $4\sqrt{3}/3$; does not export Genesis lift scale $\beta$ or UV parameters.

**Internal dyadic frontier** — used when no downstream handoff is specified. `[v6.4.20]` Rebuilt from live items only; the former list (items 0–5, including the closed items 1, 4 and 4b) is relocated verbatim to Appendix A (H-4).
1. **OPEN 20 (B-an, B-6)** — analytic convergence of $F^{1/2}$ and $F^{1/6}$ ($J$).
2. **L-PHASE row B** — a constant for the row $|z|\le\tfrac1{40}$, and the optimal constant (DYAD-THM-LPHASE-ROWA-REMAINDER covers row A only).
3. **OPEN 9 remainder** — universal missing-slot rules $Z^{\rm miss}_{p,q,D}$; bridge-gap smooth baseline ($G_{32}$, $K_p$); general $\nu_5^{(p)}$; all-$b\ge5$ persistence; general-coefficient version.
4. **Large-amplitude and transport items** — OPEN 2A, 4, 4b, 5 (with its alias OPEN 2B), 6, 12, 16.
5. **OPEN-P0-DYADIC h-transfer** — `[CAND]` `[scope: conditional]`; depends on the OPEN-M h-source bridge, not a Dyadic-internal task.

---

**OPEN 2A — Transport law for $Q_0 \gtrsim 0.6$** [RID: DYAD-OPEN-TRANSPORT-HIGH-Q]

Status: ACTIVE  
Current state: Low-$Q_0$ sector advanced; mid/high-$Q_0$ transport remains `[OPEN]`.

---

**OPEN 2B — Low-$Q_0$ breakout-phase mechanism** [RID: DYAD-OPEN-BREAKOUT-PHASE]

Status: ALIAS of OPEN 5 `[v6.4.20]`. The identifier `DYAD-OPEN-BREAKOUT-PHASE` is kept (no rename) and resolves to OPEN 5 (`DYAD-OPEN-PHASE-MATCH`); it is not counted as a separate open item.  
Current state: tracked under OPEN 5.

---

**OPEN 3 — Spiral residual theorem-grade closure** [RID: DYAD-OPEN-SPIRAL-RESIDUAL]

Status: **CLOSED (v6.4.16) — within its defined scope** (3a per-block chart residual, 3b asymptotic-phase transfer, 3c historical-fit comparison). Not part of this closure: the certified primitive-variable remainder, carried as OPEN 21 (DYAD-OPEN-PRIMITIVE-PHASE-REMAINDER).  
`[v6.4.14]` Sub-items:  
(OPEN 3a — per-block chart residual) **CLOSED.** Fit-free definitions $S_Q=D_Q\circ\widehat F-D_Q$, $S_\Theta=D_\Theta\circ\widehat F-D_\Theta$ (§6.14); exact leading terms `DYAD-ALG-OPEN3-LEADING` (the $2\operatorname{Re}(\bar Wh_2)$ origin made exact: $D_3=2\operatorname{Re}(\bar zh_2)$, $D_{\Theta,1}=\Im(h_2/z)$); certified remainders `DYAD-THM-OPEN3-SPIRAL-REM` on both NF-REM rows.  
(OPEN 3b — P4, asymptotic-phase transfer) **CLOSED (v6.4.15).** (i) Limit equality $\Psi_{W,\infty}=\Psi_\infty$ (T1, conditional on RECOG-THM-R9-MEMORY) and (ii) the finite-start offset $M_W-M=-\Delta_0(z_0)$, $|M_W-M|\le K_0\sqrt{q_0}$ (T2, conditional on T1), proved as separate results (`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`, §6.14). The primitive-variable remainder beyond formal second order is certified by `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (OPEN 21; R9 premise; rows A/B unchanged).  
(OPEN 3c — P0, historical fit) **CLOSED (v6.4.16) — historical fit reconciled as a documented model discrepancy.** `spiral_phase_fit.py` (DYAD-ART-SPIRAL-FIT) recovered and compared with the adopted leading terms (§6.14, v6.4.16 entries). This does not validate the historical fit or promote any of its outputs; it records why the tool is not a source of scientific results.

---

**OPEN 4 — Morphology boundary / branch selection** [RID: DYAD-OPEN-MORPHOLOGY]

Status: ACTIVE  
Current state: First-block split at $Q_0=4$ is `[ALG]`. Branch-selection mechanism `[OPEN]`.

---

**OPEN 4b — Low-$Q_0$ asymptotic-side transition** [RID: DYAD-OPEN-LOW-Q-TRANSITION]

Status: ACTIVE  
Current state: `[OBS]` `[ALG]` `[scope: structure]`. Reclassified as window-dependent $C_{\rm est}$/spiral-phase alignment problem, not a primitive itinerary shift. Current object is $Q_0^*(w)$ for a specified observation window. Itinerary-shift mechanism: `[FAIL]` `[scope: not confirmed]`. Historical label: OPEN 13 (pre-reconciliation). `[v6.4.20: this historical label is not the current OPEN 13, which is the archived Lie-gauge normalization (§2 closed list)]`

---

**OPEN 5 — Phase matching / Stage-B transport** [RID: DYAD-OPEN-PHASE-MATCH]

Status: ACTIVE  
Current state: Leading-order $\Pi_0$ and $a_1,a_2$ intrinsic pieces closed under OPEN 16/17. Full $\Pi(Q_0,\text{window};\text{history})$ remains `[OPEN]`.

---

**OPEN 6 — Intermediate regime near $Q_0\approx2$** [RID: DYAD-OPEN-INTERMEDIATE]

Status: ACTIVE  
Current state: `[OBS]` — phase-rich region; not yet systematically characterized.

---

**OPEN 9 — $p$-Resonance generalization** [RID: DYAD-OPEN-P-RESONANCE]

Status: PARTIAL  
Owner branch: RTG_DYADIC_OSCILLATOR_DSN  
Imports to: RTG_TRIADIC_BIRTH_LIFT_DSN, RTG_GENESIS_GEOMETRY_DSN

Closed sub-items:
- Raw cubic theorem: `[THM]` ✓ [RID: DYAD-THM-RAW-CUBIC] `[v6.4.21: formula recovered and algebraically verified; identity with the historical proposition not yet established (Appendix E)]` For the declared $K_p$ family in the raw $Z_p$ eigenframe ($\eta=Z+\bar Z$, $\rho=uZ+\bar u\bar Z$, $u=1/(1-\lambda)$, $\lambda=e^{2\pi i/p}$), the $z^2\bar z$ coefficient of the **raw one-step map** (before any normalizer $h_d$) is $\nu_{3,\rm raw}^{(p)}=\tfrac{K_p}{4}+i\,\tfrac{2\cos^2(2\pi/p)-2\cos(2\pi/p)+1}{4\sin(2\pi/p)}$. Source: `OPEN9_full_onestep_normalization_table_v2.md` §4 (companion to DSN v5.4.x; SHA-256 `af90dc13…700e`). Proof: a one-step coefficient involves no composition, so it is read off the cubic Taylor terms $\rho'\ni\eta^3/6$, $\eta'\ni K_p(\rho^3+\eta^3)/6$; owner re-derivation in P1 (`dyad_p1_math_checks.py` P1-2). Scope: one-step, raw frame; $p\ge3$ (the raw $Z_p$ eigenframe needs $\lambda\ne\bar\lambda$; the denominator $4\sin(2\pi/p)$ vanishes at $p=2$). It is not the normalized $\nu_3$ of RECOG-ALG-NU3-CLOSED-FORM, not the six-step $\mu$, and not a statement about the raw $p$-step map.
- First pure lattice harmonic $(0,p-1)$ at degree $p-1$: `[ALG]` ✓
- Finite one-step ledger $p=5,6,7$: `[ALG]` ✓ [RID: DYAD-ALG-P567-LEDGER]
- $G_{\rm lattice}(5)=0$ (both sides nonzero and equal): `[ALG]` ✓ `DYAD-ALG-GLATTICE5`
- Exact $G_{04}(10)=0$ reinterpretation as non-inheritance result: `[ALG]` ✓
- $|K^{\rm extra}_{p,q}|=s-1$ cardinality lemma: `[ALG]` ✓
- Eigenframe linear-part lemma (degree-2 no-cascade bypass): `[ALG]` ✓
- Degree-2 $q=3,(0,2)$ cancellation for all $p>3$, $3\mid p$: `[ALG]` ✓
- $p=8,q=4,(0,3)$ cancellation ($Q_8=0$ zero degeneracy): `[ALG]` ✓
- $p=12,q=4,(0,3)$ cascade boundary: exact value $-13+15\sqrt{3}/2\ne0$, $|{-13+15\sqrt{3}/2}|\approx0.0096$: `[ALG]` ✓
- Universal $q=4,(0,3)$ cancellation: `[FAIL]` ✓ (channel survives $p\ge12$)
- $q=4,(0,3)$ all-$p$ phase/factorization law $Q_p=i\zeta_p^3 M_p$, $M_p\in\mathbb{Q}(\zeta_p)^+$ (family $p=4s$, $s\ge2$): `[THM]` `[proof: exact algebraic identity]` ✓ `DYAD-THM-Q403-PHASELAW`
- Prime-horizon first-lattice transparency: `[FAIL]` ✓ (exact $p=7$ counterexample)
- p=6 eigenvalue / K₄ face-flux identity $\lambda=e^{iF_f/2}$: `[ALG]` ✓ `DYAD-ALG-P6-FACEFLUX`
- Direct-accumulation weight $\lambda^{-(b+1)k}$ for channel $(0,b)$, vanishing for $p\nmid(b+1)$: `[ALG]` ✓ [RID: DYAD-ALG-DIRECT-WEIGHT]
- Cyclotomic cross-term identity $\tfrac12[(\sum_j\lambda^{2j})^2-\sum_j\lambda^{4j}]=0$ for $p\ge5$: `[ALG]` ✓ [RID: DYAD-ALG-CROSS-IDENTITY]
- Degree-2 raw-vanishing $F_{\rm raw}^p(0,2)=0$ for $p\ge4$ (no cross-path at degree 2): `[ALG]` ✓ `DYAD-ALG-VANISH-B2`
- Degree-3 raw-vanishing $F_{\rm raw}^p(0,3)=0$ for $p\ge5$ ($\beta$-set $\{-3,-2,0\}$, no secular): `[ALG]` ✓ `DYAD-ALG-VANISH-B3`
- Degree-4 raw-vanishing $F_{\rm raw}^p(0,4)=0$ for $p\ge6$ ($\beta$-set $\{-4,-3,-2,-1,0,2\}$, no secular): `[ALG]` ✓ `DYAD-ALG-VANISH-B4`
- All-$p$ cubic radial contraction $\Re\mu_p^Z=-p\sin^2(\pi/p)<0$, $k_{\rm ret}(p)=3$, $p\ge5$ (declared $K_p$ family): `[ALG]` ✓ imported, owner RECOG [RID: RECOG-ALG-NU3-CLOSED-FORM, RECOG-ALG-NU3-NONVANISHING] (v6.4.11)
- Exact cubic cascade formula for $q=4,(0,3)$: **CLOSED (v6.4.9)** `[THM]` `[proof: exact algebraic identity]` — all-$p$ closed form, $Q_p=i\zeta_p^3 M_p$, $M_p\in\mathbb{Q}(\zeta_p)^+$ (DYAD-THM-Q403-PHASELAW)
- Channel boundary all-$p$ (DYAD-OPEN-B5-ALLP): **CLOSED `[ALG]`**. `[v6.4.20: result RID registered at adoption, DYAD-ALG-B5-ALLP-NONVANISHING (§6.11); the lifecycle identifier is unchanged]` For $p\ge13$, $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{\rm eff}$ with $S_{\rm eff}/S=N/D$, $N=2\lambda^6+\lambda^5-5\lambda^4-3\lambda^3-4\lambda^2+2\lambda+1$. Cyclotomic non-division: $\deg N=6$ so $\Phi_p\mid N$ requires $\varphi(p)\le6$ (finite set); exact check shows $\Phi_p\nmid N$ for all, so $N(\lambda_p)\ne0$ for all $p$, hence $S_{\rm eff}\ne0$ for all $p\ge13$. With the exact sweep $p=6..12$: $F_{\rm raw}^p(0,5)\ne0$ for ALL $p\ge6$. Remaining (separate): all-$b\ge5$ persistence and the general-coefficient version: `[OPEN]`

Retracted sub-items:
- Sub-horizon inheritance conjecture: `[RETRACTED]` `[scope: reframed]` — $G_{04}(10)=0$ is not divisor inheritance; $(0,4)$ is dynamically active in $J^{extra,raw}_{10,5,D}$.
- Rectangular $M(D)$ support counting heuristic: `[FAIL]` `[scope: obsolete heuristic]` — superseded by reachable-basis projector formalism.

Active sub-items:
- Universal full $\nu_5^{(p)}$ generator: `[OPEN]`
- General Lie-gauge retained-channel theorem: `[OPEN]`
- Higher lattice harmonics beyond the first: `[OPEN]`
- Universal missing-slot rules $Z^{\rm miss}_{p,q,D}$: `[OPEN]`
- Near-cancellation structure of $-13+15\sqrt{3}/2\approx-0.0096$ (modulus $0.0096$; `[v6.4.20]` sign restored; DZT-ALG-P12-NORM records its norm $\tfrac14$, finite DZT scope): `[OPEN]` — the exact large-$p$ behaviour of $|Q_p|$ is the Tier-C target FC-DYAD-31
- Exact asymptotic structure of $G_{32}(p)$: `[OPEN]`
- Channel boundary all-$b\ge5$: prove the secular $\beta=1$ mode persists (nonzero coefficient) for every $b\ge5$ (scan-confirmed $b=6$); and the general-coefficient (non-dyadic) version: `[OPEN]`
- OPEN-P0-DYADIC h-source bridge: whether the SU(2) factor transfers to OPEN-M $h$ as $\times2$ (amplitude) or $\times4$ (energy) or neither; requires OPEN M proper (Genesis SG-5/SG-6 block the dyadic route): `[OPEN]`
- Exact smooth baseline for $G_{32}/K_p$: `[OPEN]`

Evidence / candidate patterns:
- Low-degree anti-holomorphic vanishing $F_{\rm raw}^p(0,b)=0$ for $p\ge b+2$, all $b\in\{2,3,4\}$: `[ALG]` (β-mode path enumeration; source β-sets carry no secular mode; doubly certified symbolic + iteration)
- Channel boundary at $b=4$: universal vanishing `[ALG]` for $b\in\{2,3,4\}$; fails at $b=5$ for EVERY $p\ge6$ `[ALG]` (all-$p$ theorem closed, DYAD-OPEN-B5-ALLP). SOURCE $\beta=1$ coefficient exactly nonzero (five-term $\propto c_{02}^2$); $F_{\rm raw}^p(0,5)\ne0$ exactly for $p=6..12$ `[ALG]` `[scope: finite sweep]`; for $p\ge13$, $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{\rm eff}$ with $S_{\rm eff}/S=N/D$, $\deg N=6$, and $\Phi_p\nmid N$ for all $p$ (cyclotomic non-division), so $S_{\rm eff}\ne0$ for all $p\ge13$. Dyadic boundary `[ALG]`: universal vanishing for $b\in\{2,3,4\}$, first failure at $b=5$ for every $p\ge6$ `[COR]` `[v6.4.11: "iff $b\le4$" shorthand withdrawn]`. Remaining (separate): all-$b\ge5$ persistence and the general-coefficient version: `[OPEN]`

Next required artifacts:
- Universal $Z^{\rm miss}_{p,q,D}$ proof using reachable-basis projector formalism

Dependencies:
- Eigenframe linear-part lemma `[ALG]` ✓ (anchors degree-2 no-cascade bypass)
- $p=5,6,7$ finite ledger `[ALG]` ✓ (data for general $\nu_5^{(p)}$ conjecture)

---

**OPEN 12 — $P_2$ saddle manifold and large-amplitude dynamics** [RID: DYAD-OPEN-P2-SADDLE]

Status: PARTIAL (v6.4.11, by consumer theorems)  
Current state: `[THM]` `[import: RECOG v0.3.20 §2 R8, §6.11 | RECOG-THM-P2-HET]` $W^u_-(P_2)\setminus\{P_2\}\subset\mathcal B(P_1)$, with entry into the DYAD-THM-PRIM-CTR tube. `[THM]` `[import: RECOG-THM-P2-C0-FIRST]` the first outward encounter of $W^u_+(P_2)$ with $C_0$ is unique and transverse, $2.03334<\rho_*<2.03342$. Owner: RECOG; Dyadic has not rerun these certificates. Remaining `[OPEN]`: global geometry of $W^s(P_2)$, later re-intersections with $C_0$, large-amplitude dynamics.

---

**OPEN 19 — Formal centralizer of the normal-form return** [RID: DYAD-OPEN-FORMAL-CENTRALIZER] `[v6.4.11 r2; closed v6.4.12 r1]`

Status: CLOSED — formal scope (v6.4.12, adopted 16 Oct 2026)  
Question (as registered in v6.4.11): Is the formal tangent-to-identity centralizer of the formal one-step normal form $\widehat f_{\rm form}$ (equivalently, of its six-step return) equal to the one-parameter family $\{\exp(s\widehat X)\}$ of its formal infinitesimal generator, with all members $\lambda$-equivariant?  
Answer: **yes**, `[THM]` `[scope: formal category, real coefficients]` (§6.16). The proof is posed in the raw frame for $F=T^6$ and uses only the cubic term $X_3$ of $X=\log F$; conjugation by any formal normalizer $\widehat h$ transports it to the normal-form return. RIDs: `DYAD-ALG-CENT-KERNEL`, `DYAD-THM-FORMAL-CENTRALIZER`, `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`; consequence `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` (§6.15).  
Registered hypotheses, now fixed: formal real-coefficient category; only $\Re\mu\ne0$ and $\Im\mu\ne0$ enter; the lattice term $a_{05}\bar z^5$ plays no role (the kernel argument stops at cubic order).  
Not closed by this item: convergence or realization of the formal involution — moved to OPEN 20.

---

**OPEN 20 — Realization of the formal involution (Problem B)** [RID: DYAD-OPEN-INVOLUTION-REALIZATION] `[v6.4.12 r1; restructured v6.4.13]`

Status: PARTIAL — B-∞ existence **CLOSED (v6.4.18)** by `DYAD-THM-SMOOTH-EMBEDDING` (§6.17; `[THM]`, $C^\infty$ germ scope); B-∞ flat uniqueness CLOSED (v6.4.13, $C^\infty$ scope); B-an and B-6 ACTIVE.  
(B-an) `[OPEN]` Does $R_0=T^3\circ F^{-1/2}$ converge? `[ALG]` (§6.16) Equivalently: does the tangent-to-identity formal square root $F^{1/2}=\exp(\tfrac12\log F)$ of the six-step return converge? A positive answer gives an analytic non-identity involution commuting with $T$. A negative answer excludes analytic non-identity involutions commuting with $T$ (by §6.15(a)) and, under the §6.15(b) hypotheses, with $T^6$ (Corollary A).  
(B-6) `[OPEN]` `[v6.4.13]` Does the tangent-to-identity formal sixth root $F^{1/6}=\exp(\tfrac16\log F)$ converge? `[ALG]` (§6.16) Equivalent: the canonical generator $J=T\circ F^{-1/6}$ converges; equivalent: an analytic local chart exists in which $T$ commutes exactly with $A$ (Bochner averaging). B-6 ⟺ (B-an and B-3), B-3: $F^{1/3}$ (equivalently $G=J^2$) converges. Hence B-6 ⇒ B-an, and a negative B-an answers B-6 negatively; B-an alone does not give B-6.  
(B-∞) Two sub-questions, separated in v6.4.13:  
(B-∞ existence — v6.4.18) `[THM]` `[v6.4.18]` **CLOSED (v6.4.18).** Yes: by `DYAD-THM-SMOOTH-EMBEDDING` (§6.17), $R=T^3\circ K_2^{-1}$ is a $C^\infty$ local involution with $DR(0)=-I$ commuting with $T$, and $K_6=F^{1/6}$, $J=T\circ K_6^{-1}$ exist in $C^\infty$. The route used is $\Phi_\infty=\lim G_\infty^{-n}F^n$, not the §6.17 sequence $F^{-n}R_\infty F^n$ (which stays unproved).  
(B-∞ flat uniqueness) `[THM]` **CLOSED (v6.4.13, $C^\infty$ scope).** For an *existing* $C^\infty$ local involution $R$ with $R(0)=0$, $RF=FR$ (§6.15 domain convention) and $DR(0)=-I$: $RT=TR$ exactly near $0$ (F1, §6.17); such an involution is unique (F2); an existing $C^\infty$ tangent-to-identity root of $F$ commutes with $T$ and is unique (F3). Closed only in this sense: nothing is asserted about existence, finite $C^k$, or analytic convergence. RRF L-SHADOW-POLY is not imported and is not used.  
No conjecture on the analytic or existence outcomes is recorded. Not claimed: any physical exchange or G2 realization (SG-14/15).

---

**OPEN 21 — Certified primitive-variable phase remainder** [RID: DYAD-OPEN-PRIMITIVE-PHASE-REMAINDER] `[v6.4.16]`

Status: **CLOSED (v6.4.17)** by `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (§6.14; `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`), per row, R9 term kept separate.  
Target: a certified bound for the $O(Q_0^{3/2})$ remainder of the primitive-variable second-order form of DYAD-ALG-OPEN3-PHASE-OFFSET (§6.14, `[ALG]` `[scope: formal]` part), i.e. $M_W(W_0)$ expressed in the primitive start $W_0$ rather than in $z_0=h^{-1}(W_0)$. Route: a second-order bound for $h^{-1}-(\mathrm{id}-h_2)$ on the row disks, composed with the certified $K_1,K_2$ of DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS. Separated from OPEN 3 at the v6.4.16 lifecycle decision. Does not affect T1/T2 or the chart-variable memory law of DYAD-THM-OPEN3-ASYMPTOTIC-PHASE (conditional grades unchanged).

---

**OPEN 16 — Full projection operator $\Pi(Q_0,U,\mathcal{O})$** [RID: DYAD-OPEN-PROJECTION]

Status: PARTIAL  
Closed sub-items:
- Decomposition $\Pi = \Pi_0 + a_1Q_0 + \Pi_{\rm alias}(U,\mathcal{O}) + a_2Q_0^2 + \cdots$: `[ALG]` `[scope: structure]` ✓
- Alias phase $G_-(\pi/\tau) = 1/(1-i\tau)$, $\arg G_- = \arctan(2\sqrt{3}/3)$: `[ALG]` ✓ [RID: DYAD-ALG-ALIAS-PHASE]

Active sub-items:
- Full observable-convention and history dependence: `[OPEN]`

---

**OPEN 14 — Historical branchwise wedge IA program** [RID: DYAD-OPEN-WEDGE-IA]

Status: ACTIVE | Optional — no longer blocking OPEN 11.

---

**OPEN 15 — Historical micro-regime IA remainder program** [RID: DYAD-OPEN-MICROREGIME-IA]

Status: ACTIVE | Optional — no longer needed for scoped OPEN 11 theorem.

---

Closed OPENs (one-line):

- **OPEN 1** `DYAD-THM-C21` :: `[THM]` ✓ CLOSED — archival proof of $c_{21}$.
- **OPEN 11** `DYAD-THM-OPEN11` :: `[THM-ALG via IA]` ✓ CLOSED — chirality closure, T1/F1 residual-free on $(0,2]$.
- **OPEN 13** [RID: DYAD-ALG-LIEGAUGE-NORM] :: `[ALG]` `[conv: Lie strict-kernel gauge]` ✓ ARCHIVED — Lie-gauge normalization; gauge-universal forms remain open.
- **OPEN 17** `DYAD-ALG-A1A2-LIEGAUGE` :: `[ALG]` `[conv: Lie strict-kernel gauge]` ✓ CLOSED through $a_2$ — $a_1=559\sqrt{15}/4860$, $a_2=86775991\sqrt{15}/755827200$.
- **OPEN 18** `DYAD-THM-OPEN18` :: `[THM-ALG via IA]` ✓ CLOSED — first-footprint branch monotonicity.
- **OPEN 3** `DYAD-OPEN-SPIRAL-RESIDUAL` :: `[ALG]`/`[THM]` (3a, 3b at their adopted grades; 3c documented discrepancy) ✓ CLOSED (v6.4.16) within its defined scope — the primitive-variable remainder continues as OPEN 21.
- **OPEN 21** `DYAD-OPEN-PRIMITIVE-PHASE-REMAINDER` → closed by `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` :: `[THM]` `[assuming: RECOG-THM-R9-MEMORY]` ✓ CLOSED (v6.4.17) — certified primitive-variable phase remainder, rows A/B not mixed.
- **OPEN 19** `DYAD-OPEN-FORMAL-CENTRALIZER` → closed by `DYAD-THM-FORMAL-CENTRALIZER` :: `[THM]` `[scope: formal]` ✓ CLOSED (v6.4.12) — formal tangent-to-identity centralizer ($DG(0)=I$) of $T^6$ is $\{\exp(sX)\}$; unique formal involution $R_0$ (§6.16). Realization: OPEN 20.

---

## §3. Scope Guards {#sec-3-scope-guards}

**[SG-1]** $Q_{\rm true}$ is the sole primary radial observable. $Q_{\rm euclid}$ is comparison-only and must never appear in certification claims.  
Violation: Using $Q_{\rm euclid}$ as a primary observable.

**[SG-2]** All canonical asymptotic dyad claims use six-step sampled data: $n=6,12,\ldots$, block index $m=n/6$.  
Violation: Mixing step-level and block-level claims without explicit conversion.

**[SG-3]** $W_{\rm DSN}=u+iv$ is the $p=6$ primitive master analytic coordinate, derived from $(\rho,\eta)$. It does not replace the primitive ontology. For general $p$-resonance work use $Z_{\rm eng}/W_{\rm new}$ (§6.11).  
Violation: Treating $W_{\rm DSN}$ as a generic $p$-resonance coordinate.

**[SG-4]** The exact six-step finite iterate of the primitive map is the canonical nonlinear object. Continuous Birkhoff vector fields are permitted as structural surrogates or cross-checks, not as primary extraction vehicles for new certification claims.  
Violation: Deriving a certification claim from a continuous vector field without primitive-map verification.

**[SG-5]** Raw $p$-step coefficients, $F_1^p$ coefficients, and normalized $p$-step coefficients are distinct objects unless a specific bridge theorem or normalization convention identifies them.  
Violation: Equating any two of these without citing the identifying theorem.

**[SG-6]** In tangent-to-identity $p$-step problems, vanishing linear homological denominators do not prove $\Phi_p = \text{Id}$. Gauge freedom remains until a convention or theorem is fixed.  
Violation: Concluding $\Phi_p=\text{Id}$ from denominator vanishing alone.

**[SG-7]** $C_{\rm est}/\kappa_{\rm est}$ magnitude is strongly window-dependent. Fixed-parameter late-window fitting is mandatory for certification attempts.  
Violation: Reporting $C_{\rm est}$ without specifying the observation window.

**[SG-8]** ISP pre-crossing tables built from sector membership alone are diagnostic overlays. Canonical pre-crossing requires: $\rho<0$, $\sin\eta<0$, $\rho-\sin\eta\ge0$.  
Violation: Treating sector-based ISP tables as theorem-grade pre-crossing certification.

**[SG-9]** Single-block ISP tests isolate $c_{21}$ but do not isolate $c_\theta$ without spiral subtraction. The per-block phase residual carries an $O(\sqrt{Q})$ spiral contribution dominating the $O(Q)$ quintic phase signal.  
Violation: Extracting $c_\theta$ from single-block data without spiral subtraction.  
`[v6.4.14]` Certified chart-level form (normalized $z$, F-block counter; not a subtraction recipe for primitive ISP data): $|S_\Theta|\le0.705\,q^{3/2}$ on $|z|\le\tfrac1{20}$ and $\le0.678\,q^{3/2}$ on $|z|\le\tfrac1{40}$, i.e. $\le0.611\sqrt q$ resp. $0.587\sqrt q$ relative to $\tau q$ (§6.14, DYAD-THM-OPEN3-SPIRAL-REM). The guard text is unchanged.  
`[v6.4.15]` Asymptotic form: along an orbit the primitive phase $\Psi_W$ approaches the common limit with the exact offset $\Delta_0(z_m)=\Delta_1(z_m)+O(q_m)$, i.e. an $O(m^{-1/2})$ spiral whose angle winds logarithmically, versus $O(1/m)$ on the $C_z$ track (§6.14, DYAD-THM-OPEN3-ASYMPTOTIC-PHASE). This is an exact-orbit statement, not a fit statement (SG-7).

**[SG-10]** $\Im(\nu_5)$ is not invariant under general real-analytic residual gauge transforms `[FAIL]`. Gauge derivative $d\Im(u_{32})/d\lambda = -4\sqrt{3}/3 \ne 0$ computed exactly in the implemented diagnostic family. All $c_\theta$ and $\Pi(Q_0)$ results carry the Lie strict-kernel gauge convention scope.  
Violation: Treating $\Im(\nu_5)$ as gauge-invariant.

**[SG-11]** OPEN 9 has a sealed finite one-step ledger for $p=5,6,7$ but not a universal $\nu_5^{(p)}$ theorem. Arithmetic-horizon claims about $C_{\rm sub}$ and bridge gaps must distinguish exact divisor definitions from thresholded broad-scan numerics.  
Violation: Extending finite-ledger results to general $p$ without proof.

**[SG-12]** Bridge-gap diagnostics compare $F_1^p = (\Phi_1^{-1}\circ f_p\circ\Phi_1)^p$ with $F_{\rm raw}^p = f_p^p$ in a one-step homological frame. They are not Lie-gauge $p$-step gaps unless a bridge theorem identifies them.  
Violation: Treating bridge-gap diagnostics as Lie-gauge $p$-step gaps.

**[SG-13]** The dyad-to-triad bridge exports a local $p=6$, $K=1$ module only: $\mu$, $\tau$, $4\sqrt{3}/3$, and the protection matrix. It does not export Genesis lift scale $\beta$, phase convention, or UV parameters.  
The separately defined odd-projected residual $E_{\rm odd}$ of §6.12 is a mathematical diagnostic export, not a DYAD-selected physical birth rule; its identification with a consumer's fracture variable is pending. The established local cubic module remains unchanged.  
Violation: Importing $\beta$ or UV parameters from the dyadic study without an explicit external lift; treating $E_{\rm odd}$ as an accepted consumer birth residual. `[v6.4.11]` Genesis v2.8.5 (GCL-06) now uses the typed residuals $E_{\rm raw}^W$, $E_{\rm odd}^W$, $E_{\rm NF}$ as definitions; physical residual selection remains OPEN there.

**[SG-14]** Programme guards SG-PROG-1 (cross-branch firewall) and SG-PROG-2 (`RTG_PROGRAMME_OVERVIEW_v1.2`) apply. `[v6.4.20]` Every dyadic result is conditional on the selected generator $T$: it is not physically primitive, inevitable or universal beyond the support of an explicit selection/universality result (`RTG-OPEN-GENERATOR-SELECTION`). Exact local mathematics stays established while physical selection is open.  
Violation: describing a dyadic result as physically primitive, inevitable or universal without such a result.

**[SG-15]** OPEN-P0-DYADIC scope guard. The p=6 eigenvalue satisfies $\lambda=e^{i\pi/3}=e^{iF_f/2}$ with $F_f=2\pi/3$ `[ALG]`, and the SU(2) half/full-angle energy ratio is $E_{\rm full}/E_{\rm half}=4$ `[ALG]`. However R11 treats $h$ as an external amplitude parameter and does not derive whether $h\sim F_f$, $h\sim F_f^2$, or neither. Therefore neither $h\mapsto2h$ nor $h\mapsto4h$ is DSN-certified, and any OPEN-M gate correction from this route is `[CAND]` `[scope: conditional]` pending the h-source bridge. `[v6.4.11]` OPEN-M v0.7.1 certifies no numerical deficit in either direction; the route is a conditional calibration branch only. Genesis SG-5 prohibits deriving $\alpha_f$ or UV data from dyadic coefficients alone.  
Violation: Claiming the p=6 NF closes OPEN-M, asserting a definite $\times2$ or $\times4$ OPEN-M gate factor from the dyadic alone, or describing this route as correcting a certified OPEN-M deficit.

**[SG-16]** Low-degree vanishing path-enumeration guard. Manual path enumeration is unsafe for pure anti-holomorphic vanishing claims (the $p=3,b=3$ nonzero case, where the direct term already vanishes, exhibits a cross-path that naive listing misses). For $b\le4$, automatic $\beta$-mode path enumeration certifies `[ALG]` (source $\beta$-sets carry no secular mode). `[v6.4.20]` Available certificates, owner-rerun 21 Oct 2026: `rtg_betagraded_vanishing.py` (DYAD-ART-VANISH-BGRADED) and `degree_b_vanishing_cert.py`; the registry name `degree_b_vanishing_cert_v2.py` is not available in the project (audit note, §6.11). For $b\ge5$, no promotion without the same source $\beta$-set certificate.  
Violation: `[v6.4.20]` (i) tagging a vanishing statement `[ALG]` without a registered enumeration proof; (ii) using DYAD-ALG-VANISH-B2/B3/B4 outside $p\ge b+2$, or asserting "$(c_{02})^2$ is the only cross-term". The certified statements for $b=2,3,4$ at $p\ge b+2$ are not violations. (v6.4.19 text: Appendix A H-6.)

**[SG-19]** Normalization-object guard (v6.4.10). Three distinct operations have historically all been called "normalization": (i) the **archival coordinate change** $\Phi_{\rm archive}=\mathrm{id}+h_4+h_{5,\rm nr}$ (`normalize_p6_liegauge_exact.py`; preserves every raw coefficient through degree 5, $F_4\ne0$ survives); (ii) the **log-channel projection** $G_{\rm proj}=\exp(\mathscr P_{\rm keep}\log F_W)$, $\mathscr P_{\rm keep}$ the channel projector onto the retained channels (`normalize_pstep_lie.py`; a defined reduced model, not a solved conjugacy); (iii) the **polynomial conjugacy** $\mathcal J_{\le6}(f\circ h-h\circ n)=0$ with additive $h$ and the resonant monomial coefficients of each $h_n$ zero (§6.14). A "normalized coefficient" claim must name which operation it refers to. $G_{\rm proj}$ is never called the normalized return. Coefficients are not transferred between operations: the standing example is the obstruction $c^{({\rm raw},6)}_{05}-a_{05}=\tfrac{-13+3i\sqrt3}{576}\ne0$ (DYAD-ALG-NF6-OBS). Finite jets ($n$, $J$) are stated as finite-order identities, never as all-orders polynomial identities; the actual maps $\widehat f=h^{-1}fh$, $\widehat F=h^{-1}F_Wh$ are exact only on their proved domains.  
Violation: Calling $G_{\rm proj}$ "the normalized return"; inserting raw $c_{05}$ (or $c_\theta$, $a_1$, $a_2$, or a long-orbit backbone) into the conjugacy chart without the R11 reconciliation; writing $f\circ h=h\circ n$ without the $\mathcal J_{\le6}$ qualifier.

`[DEF]` `[v6.4.20]` SG-17 and SG-18 do not occur in this ledger or in its Appendix A history; the numbers are unassigned.

---

## §4. Layer Routing {#sec-4-layer-routing}

$$\text{Primitive} \;\xrightarrow{\text{defines}}\; \text{ISP} \;\xrightarrow{\text{informs}}\; \text{Normalized }p\text{-step} \;\xrightarrow{\text{describes}}\; \text{Observables}$$

| Question | Layer | Canonical tool |
|---|---|---|
| What is the system exactly? | Primitive | Exact primitive map, raw finite-step iteration, scoped predicates |
| How does crossing geometry work? | ISP | $(Q,\Theta,\ell)$, overshoot $R$, safe funnel, canonical footprint |
| What are the asymptotic coefficients? | Normalized $p$-step | $c_{21}$, $\nu_5$, $c_\theta$, bridge theorems |
| What does a long run measure? | Observable / fit | Backbone fits, spiral phase, $\kappa_{\rm fit}$ `[v6.4.20: phi_* removed; it is not defined in this ledger (notice N3)]` |

Routing rules:
- Observable-layer results do not certify primitive-layer or normalized-layer claims without a named bridge.
- ISP results require the strict primitive pre-cross predicate before carrying theorem-grade weight.
- Distinct normalization conventions are related by explicit bridge theorems, not assumed identical.
- Raw $p$-step, $F_1^p$, and normalized $p$-step objects are distinct unless a specific theorem identifies them.
- No layer object imports from the discrete RTG programme (TDR-G) without a named bridge theorem (SG-14).

<!-- AI_CONTEXT_CORE_END -->

---

## §5. High-Risk Claims Ledger {#sec-5-high-risk}

| Claim | Valid form | Forbidden overclaim | Section |
|---|---|---|---|
| $c_{21}$ | $-\frac{1}{2}-i\frac{2\sqrt{3}}{3}$ `[THM]` | any other value or convention-dependence claim | §6.2 |
| $c_\theta^{(6)}$ | $-119\sqrt{3}/648$ `[ALG]` `[conv: Lie strict-kernel gauge]`; `[v6.4.20]` the chart quintic phase coefficient is $+89\sqrt3/324$ (RECOG-ALG-CHART-LAWS), opposite in sign | gauge-universal; use as a phase-moment or chart input | §6.9, §6.14 |
| $G_{04}(10)=0$ | Exact $p=10$ reinterpretation `[ALG]`; instance of degree-4 raw-vanishing for $p\ge6$ | Divisor-inheritance, sub-horizon-strobe cancellation, or universal theorem claim before proof | §6.11 |
| OPEN 9 finite ledger | Exact for $p=5,6,7$ `[ALG]` | Extended to general $p$ without proof | §6.11 |
| $G_{\rm lattice}(5)=0$ | Unique non-trivial degree-4 bridge cancellation `[ALG]` | Pattern for other $p$ | §6.11 |
| Low-degree anti-holomorphic vanishing | $F_{\rm raw}^p(0,b)=0$, $p\ge b+2$, all $b\in\{2,3,4\}$ `[ALG]` (β-mode enumeration, no secular) | Extending to $b\ge5$ without a β-set certificate; range "$p\ne b+1$" | §6.11, SG-16 |
| $\Im(\nu_5)$ invariance | `[FAIL]` — not gauge-invariant | Gauge-invariant under general real-analytic gauge | §6.9, SG-10 |
| OPEN 11 closure | Scoped canonical family $(\rho_0,\eta_0)=(0,q)$, $q\in(0,2]$ `[THM-ALG via IA]` | Full-phase-space chirality theorem | §2 |
| Dyad bridge exports | $\mu$, $\tau$, protection matrix, $4\sqrt{3}/3$ only | Genesis lift scale $\beta$ or UV parameters | §6.12, SG-13 |
| $\lambda=e^{iF_f/2}$ | Exact structural connection `[ALG]`; $F_f=2\pi/3$ (K₄ face flux) | Claiming this closes OPEN-M or fixes h-normalization | §6.2, §6.12 |
| OPEN-P0-DYADIC h-transfer | SU(2) energy ratio 4 `[ALG]`; transfer to $\rho$ `[CAND]` `[scope: conditional]` | Asserting definite $\times2$/$\times4$ OPEN-M correction | §6.12, SG-15 |
| Cross-operation coefficient transfer (raw / archival / projected / conjugated) | Distinct objects; transfer only via an explicit bridge (SG-19, §6.14) | Reading the archival $h_3=0$, projected-model coefficients, or raw $c_{05}$ as properties of the conjugacy chart | §6.9, §6.14 |
| Raw angular-mean coefficient $47/54$ | `[ALG]` for the explicitly defined fixed-radius operator $\mathcal A_{\rm raw}$ (§6.5); long-orbit/autonomous-backbone identification and final-chart transfer `[OPEN]` | Pointwise primitive-$Q$ update; an established subleading long-orbit coefficient; equating with the one-block burst $37/40$; unbridged normalized coefficient | §6.5, §6.14 |
| R11 cascade gate $4/125$ | Arithmetic conversion `[ALG]`; physical threshold `[HYP]` `[scope: inherited]` from OPEN-GEN-II-7B; `[v6.4.20]` inherited conditions: reduced birth-race wrapper, 9C raw-array premise, large-$g$ limit, state/window matching, source normalization (OPEN-M v0.7.1; `GEN-OPEN-UVJET-SCOPE`); OPEN-M records no certified numerical deficit | Treating the gate as a first-principles `[ALG]` threshold or as evidence of a certified deficit | §6.11 |
| All-$p$ cubic return (RECOG import) | $\Re\mu_p^Z=-p\sin^2(\pi/p)<0$: local cubic radial contraction in the declared $K_p$ family | Universal healing across generators, finite amplitudes or birth mechanisms | §6.11 |
| R9 lattice memory | Exact-map theorem on the $C_z$ track and stated small-$q_0$ windows (RECOG) | Physical event-to-memory inheritance; transfer to the $C_W^{(h)}$ track | §6.14 |
| Local involution germ (§6.15) | Conditional germ dichotomy $R=\mathrm{id}$ or $DR(0)=-I$; (a) $C^1$+$T$, (b) $C^3$+$T^6$+tube | Physical exchange existence; equivalence of $EF=TE$ and $EF=T^6E$; exact $RT=TR$ for a $C^\infty$ six-step $R$ from §6.15 alone (`[v6.4.20]` not implied by §6.15 alone; established by F1, §6.17) | §6.15 |
| Formal centralizer / $R_0$ (§6.16) and analytic clock bridge (§6.15) | Formal category, tangent to the identity: $\operatorname{Cent}_{{\rm formal},\,DG(0)=I}(T^6)=\{\exp(sX):s\in\mathbb R\}$ (`[v6.4.20]` restriction restored; without $DG(0)=I$ the centralizer also contains $T$ and $R_0$); unique formal involution $R_0=T^3F^{-1/2}=\widehat S$; analytic $R$ with $RT^6=T^6R$, $DR(0)=-I$ ⇒ $RT=TR$ exactly | Analytic convergence of $R_0$ (OPEN 20 B-an); exact commutation of the finite chart $S_h$; physical exchange / G2. `[v6.4.20]` Not implied by these formal results alone, but established elsewhere: $C^\infty$ existence (DYAD-THM-SMOOTH-EMBEDDING) and $C^\infty$ exact commutation (F1, §6.17) | §6.15, §6.16 |
| Canonical ℤ₆ generator $J$ (§6.16, v6.4.13) | Formal: unique $J=TF^{-1/6}$ with $J^6=\mathrm{id}$, $DJ(0)=A$; $R_0=J^3$, $G=J^2$; analytic realization ⟺ B-6 | Convergence of $J$; B-6 equated with B-an; a physical chirality or ℤ₆ action | §2 OPEN 20, §6.16 |
| Lemma F and F1–F3 (§6.17, v6.4.13) | `[THM]`: flat-close $F$-commuting maps are trivial on the stated forward-invariant ball; `[THM]` `[assuming: hypotheses stated in the entry]` for existing $C^\infty$ objects: clock bridge, uniqueness, root commutation | Existence of a $C^\infty$ root or involution from Lemma F / F1–F3 alone (`[v6.4.20]` existence: DYAD-THM-SMOOTH-EMBEDDING, §6.17); finite-$C^k$ versions; analytic convergence; reading the RID word `CAND` as a status | §6.17 |
| Smooth flow embedding (§6.17, v6.4.18) | `[THM]`, $C^\infty$ germ scope: $F=\varphi_X^1$, $X\in C^\infty$, $j^\infty X=\log F$; uniqueness of $X$ among generators with $DX(0)=0$; $C^\infty$ roots $K_m$, $J$, $R$ commuting with $T$ | Analyticity (B-an, B-6); uniqueness among all $C^\infty$ generators (no $DX(0)=0$); a quantitative radius or finite-$C^k$ constants; convergence of the §6.17 route $F^{-n}R_\infty F^n$; physical exchange, G2 realization, $EF=TE$ vs $EF=T^6E$ (SG-14/15) | §2 OPEN 20, §6.17 |
| Spiral residual (§6.14, v6.4.14) | Exact leading terms of $S_Q,S_\Theta$ `[ALG]`; per-block remainder bounds with majorant constants on $\vert z\vert \le\tfrac1{20}$, $\tfrac1{40}$ `[THM]` | Reading $K_\Theta,K_Q$ as true-error maxima; identifying $S_Q$ with $P_5$ (cross term $-2qD_3$); the primitive asymptotic-phase transfer (P4) as implied by the per-block result alone (P4 is DYAD-THM-OPEN3-ASYMPTOTIC-PHASE); equivalence with the historical fit; $C_{\rm est}$/$\kappa_{\rm est}$; transfer to NUMGEN L1 or ISP-angle coefficients (SG-7, SG-19) | §2 OPEN 3, §6.14 |
| Asymptotic-phase transfer (§6.14, v6.4.15) | Exact offset $\Psi_W-\Psi_z=\Delta_0$ `[ALG]`; certified $K_0,K_1,K_2$ `[THM]`; limit equality conditional on R9; memory offset $-\Delta_0(z_0)$ conditional on T1; chart-variable memory law conditional on R9 | An independent existence theorem for $\Psi_\infty$; R9 read directly on the raw track; transfer to the $C_W^{(h)}$ comparator; a certified primitive-variable ($W_0$) remainder from these results alone (`[v6.4.20]` see DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER); physical reading of $-\sqrt3/3$; C_est/κ_est or historical-fit statements (SG-7) | §2 OPEN 3, §6.14 |
| Historical-fit reconciliation (§6.14, v6.4.16) | Documented model differences D1–D4 of `spiral_phase_fit.py` against the adopted leading terms; `[NUM]` two-harmonic amplitudes agree with the predictions within about 1% | Validation of the historical fit; reading its $\kappa$, $A$, $B$, $c_\theta$ outputs as coefficients; C_est/κ_est (SG-7); transfer to NUMGEN L1 or ISP-angle coefficients (SG-19); a certified primitive-variable remainder from the fit (`[v6.4.20]` the remainder is DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER) | §2 OPEN 3, §6.14 |
| Primitive-variable phase remainder (§6.14, v6.4.17) | `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`: $\vert M_W-\mathcal P_2(W_0)\vert \le K'_jQ_0^{3/2}+C_{2,j}(256/225)^2Q_0^2$ per row ($K'_A=3951/1000$, $K'_B=971/250$); single-constant $K_A=8831/250$, $K_B=883/100$; majorant suprema | An unconditional result (R9 enters through T1 and the memory law); re-certification of R9 or of its $C_2$; reading the `[NUM]` ratio $\approx0.35$ as a proved constant or as absence of higher-order terms; mixing rows; transfer to $C_W^{(h)}$, NUMGEN L1 or ISP-angle coefficients (SG-19); C_est/κ_est (SG-7) | §2 OPEN 21, §6.14 |
| L-PHASE angular remainder, row A (§6.14, v6.4.19) | `[THM]`: $\vert r_m\vert \le\tfrac{403}{250}Q_m^{3/2}$ for block base points in $U$, $Q_m$ primitive; branch certificate $\varepsilon\le0.04654$ on $U_T$; the constant is the ceiling of a majorant (certificate value $1.61112$; angular supremum of the true error $\to\Lambda^*\approx1.4003$ as $Q\to0$, `[NUM]`) | Optimality of $403/250$; row B ($\vert z\vert \le\tfrac1{40}$) or larger domains; a statement beyond the first-order block law; reading $403/250$ or $\Lambda^*$ as a NUMGEN L1/ISP-angle coefficient or as a correction of NUMGEN's measured values (SG-19); discharge of GAP-LOCK angular hypotheses; any $\phi^*$ statement; byte identity with the P2B v2 `certificate.json` (provenance is exact-coefficient and transitive) | §6.14, §7 |
| $\widehat F$ degree-ten even term | Finite fixed-$h_6$ statement (DYAD-ALG-NF6-DEG10) | Asymmetry of the primitive dynamics; statement about all-order or other normalizers | §6.14 |
| $K_p$ frame scale (§6.9, `[v6.4.20]`) | `[ALG]`: $W_p=i\cot(\pi/p)\,Z$; $\mu_p^{Z}=\cot^2(\pi/p)\,\mu_p^{W_p}$; one-step cubic coefficients scale the same way | Comparing $\mu_p$ across frames or across $p$ without the frame scale; use outside the declared $K_p$ family | §6.6, §6.9, §6.11 |
| Smooth equivariant chart (§6.17, `[v6.4.20]`) | `[THM]` corollary of E4: $C^\infty$ $\Phi$ with $D\Phi(0)=I$, $\Phi J=A\Phi$, $[\Phi T\Phi^{-1},A]=0$ | Analyticity; a quantitative radius; finite-chart bounds for $\Phi$; a physical network model, carrier or $\gamma$; a choice for Genesis C2 or OFN class C | §6.17 |

---

## §6. Main Scientific Ledger {#sec-6-ledger}

### §6.1 Core Map and Fixed Points — entry grades: ALG, THM, DEF, FAIL {#sec-6-1-map}

`[DEF]` [RID: DYAD-DEF-PRIMITIVE-MAP] **Dyad map** (custody note §1):
$$\rho' = \rho - \sin\eta, \qquad \eta' = \eta + (e^\rho - 1) - \sin\eta.$$
$\eta$ treated as a lifted angle; $\eta_{\rm wrap} = \text{wrap}_{(-\pi,\pi]}(\eta)$.

`[ALG]` Fixed points: $P_1=(0,0)$ elliptic order-6; $P_2=(0,\pi)$ hyperbolic saddle.

`[DEF]` `[v6.4.20 entry]` Fixed-point scope (lifted chart; zero-winding $P_1,P_2$; winding fixed points of the wrapped cylinder): §1 table. Germs at $P_1$ follow the §6.15 domain convention.

`[ALG]` **Jacobian:**
$$J(\rho,\eta)=\begin{pmatrix}1&-\cos\eta\\e^\rho&1-\cos\eta\end{pmatrix},\qquad\det J=1+(e^\rho-1)\cos\eta.$$

`[THM]` Map is not globally area-preserving. The equality $\det J=1$ holds when $(e^\rho-1)\cos\eta=0$, i.e. on $\rho=0$ or $\cos\eta=0$, not globally.

`[DEF]` `[v6.4.20 entry; RID registered at adoption, 21 Oct 2026]` [RID: DYAD-DEF-CRITICAL-CURVE] **Critical curve (rank-one locus).** $C_0:=\{\det DT=0\}=\{1+(e^\rho-1)\cos\eta=0\}$. Because $|\cos\eta|\le1$, this is the set described in the next entry ($\rho\ge\ln2$). On $C_0$ the kernel of $DT$ is spanned by $k=(\cos\eta,1)$, since $DT\,k=(0,\det DT)$ identically; RECOG-ALG-P2-C0-WHITNEY-FOLD uses this direction. Owner check M2.

`[ALG]` **Critical curve:** $C_0=\{\rho\ge\ln2,\;\cos\eta=-1/(e^\rho-1)\}$. Map not globally invertible beyond $C_0$. $Q_{\min}(C_0)\approx2.9159$.

`[ALG]` **$P_2$ saddle:** $\lambda_+=\phi^2\approx2.618$, $\lambda_-=\phi^{-2}\approx0.382$; escape law $T_{\rm escape}\approx\ln(1/\varepsilon)/\ln(\phi^2)$.

`[FAIL]` $6\phi^2$ as crossing target is rejected.

### §6.2 Linear Structure and Cubic Coefficient — entry grades: ALG, THM {#sec-6-2-cubic}

`[ALG]`
$$J(P_1)=\begin{pmatrix}1&-1\\1&0\end{pmatrix},\qquad \lambda_\pm=e^{\pm i\pi/3}.$$
Order-6 elliptic resonance: one step $=60°$ rotation; six steps $=$ one full rotation at linear order.

`[ALG]` `[RID: DYAD-ALG-P6-FACEFLUX]` **K₄ face-flux connection.** The p=6 eigenvalue equals the SU(2) half-angle representative of the K₄ ESM face flux $F_f=2\pi/3$:
$$\lambda=e^{i\pi/3}=e^{iF_f/2}.$$
The OPEN-M cascade angular optimum $\theta_f=2\pi/3$ (R11 `[ALG]`) equals the face flux $F_f$ exactly; the ISP safe-funnel boundary angle $2\pi/3$ coincides. This is an exact arithmetic identity of the p=6 eigenvalue; its physical transfer to OPEN-M source normalization is a separate question (§6.12, SG-15).

`[THM]` `[RID: DYAD-THM-C21]` **Cubic coefficient:**
$$c_{21}=-\tfrac12-i\tfrac{2\sqrt3}{3}.$$
$\Re(c_{21})=-\frac{1}{2}$ (radial contraction); $\Im(c_{21})=-\frac{2\sqrt{3}}{3}$ (nonlinear phase shear).

`[ALG]` **Quadratic near-identity correction:**
$$h_2(W,\bar W)=c_{20}W^2+c_{11}W\bar W+c_{02}\bar W^2, \quad c_{20}=-\tfrac{1}{12}-i\tfrac{\sqrt3}{12},\; c_{11}=-\tfrac13,\; c_{02}=\tfrac{1}{24}-i\tfrac{\sqrt3}{24}.$$
All coefficients in $\mathbb{Q}(i\sqrt3)$ (`[v6.4.20]` field label corrected; values unchanged).

`[ALG]` **Post-$H_2$ quartic structure:** After conjugating $F_W$ by $H_2=\mathrm{id}+h_2$, the degree-4 residual vanishes identically. No additional quartic-cleanup correction required.

`[ALG]` **Post-$H_2$ quintic structure, $W$-component.** The specified quadratic conjugacy removes the raw quartic return term. Its $W$-component quintic part has six nonzero channels. At $p=6$ the resonance rule $a-b-1\equiv0\pmod 6$ selects only $(3,2)$ and $(0,5)$; $(5,0),(4,1),(2,3),(1,4)$ are nonresonant and absent from the final jet $J$ of DYAD-ALG-NF6. The conjugate output has the reflected channel list and is not merged into the $W$-component list. The adopted additive one-step normalizer has nonzero $h_3$ channels $(3,0),(1,2),(0,3)$ (§6.14); this $h_3$ is not the archival return-log quantity historically called zero (SG-19). Any separately defined sequential return-coordinate correction $H_3$ requires its own definition.

### §6.3 Canonical Constants — entry grades: ALG {#sec-6-3-constants}

$$\tau=\tfrac{2\sqrt3}{3}\approx1.154700538,\quad|\sigma|^2=\tfrac{19}{12},\quad\alpha_{\rm block}=\tfrac{\sqrt3}{3\pi},\quad\alpha_{\rm step}=\tfrac{\sqrt3}{18\pi}$$
$$R^*=\exp(\pi/\tau)\approx15.1909377,\quad\lambda_{\rm DSI}=e^{\pi\sqrt3}\approx230.7645883$$

`[ALG]` `[v6.4.20 entry]` **Constant identities.** $R^*=e^{\pi/\tau}=e^{\pi\sqrt3/2}=\lambda_{\rm DSI}^{1/2}$ and $e^{\pi/(3\tau)}=e^{\sqrt3\pi/6}=\lambda_{\rm DSI}^{1/6}$. The second number is the limit in `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` (NUMGEN v1.20.8 §6.6). NUMGEN SG-NG-23 types constants of this kind as chart/normal-form diagnostics, not a commensurability class; RECOG SG-R10 records that the lattice clock ratio is invariant under linear frame changes and $U(1)$-equivariant residual gauge. No physical identification is made. Owner check M1.

**Definition-ledger identities (v6.4.11).** Registration of known identities relayed by NUMGEN (`NG_TO_DYAD_RELAY_RIEMANN_LENS_v1.md`); not new results.

`[ALG]` [RID: DYAD-ALG-Q-INVARIANT-FORM] With $A=DT(P_1)$ elliptic of order 6, the real symmetric bilinear forms $G$ with $A^\top GA=G$ form a one-dimensional space spanned by $B=\begin{psmallmatrix}1&-\frac12\\-\frac12&1\end{psmallmatrix}$; hence $Q_{\rm true}=x^\top Bx$ is the unique $A$-invariant quadratic form up to scale. (Proof: $A$ is conjugate to a rotation by $\pi/3\notin\pi\mathbb Z$, whose invariant forms are multiples of the identity.) This fixes SG-1 up to normalization; the normalization itself is the §1 convention.

`[ALG]` [RID: DYAD-ALG-TAU-DETB] $\det B=\tfrac34$, hence $\tau=\tfrac{2\sqrt3}{3}=(\det B)^{-1/2}$. `[HEUR]` Any structural explanation of this equality (e.g. as the area normalization of the Birkhoff frame entering $\Im\mu$) is not established here.

`[ALG]` [RID: DYAD-ALG-CUBIC-PARABOLIC] $F=T^6$ is tangent to the identity at $P_1$ with vanishing quadratic return and nonzero cubic term ($\mu\ne0$, DYAD-THM-C21): a cubic parabolic germ in the raw frame (its raw quartic part is nonzero, §6.7).

### §6.4 ISP Coordinate System — entry grades: ALG, DEF {#sec-6-4-isp}

> **[Local guard SG-4 applies]**

`[ALG]` `[scope: structure]` ISP is a coordinate/proof layer overlying the primitive DSN structure, not a replacement. Primitive map, $Q_{\rm true}$, six-step block formulation, and certificate program remain the reference mathematical model. In case of conflict, the primitive record wins.

`[ALG]` [RID: DYAD-ALG-ISP-MAPS] `[v6.4.20; RID registered at adoption, 21 Oct 2026; covers the forward map and the reconstruction below; owner check M4]` **Forward map:**
$$Q=\rho^2-\rho\eta_{\rm wrap}+\eta_{\rm wrap}^2,\quad \Theta=\text{atan2}(\sqrt3\eta_{\rm wrap},2\rho-\eta_{\rm wrap})\in(-\pi,\pi].$$

`[ALG]` **Reconstruction:**
$$\eta_{\rm wrap}=\tfrac{2}{\sqrt3}\sqrt{Q}\sin\Theta,\quad\rho=\tfrac{2}{\sqrt3}\sqrt{Q}\cos(\Theta-\tfrac{\pi}{6}).$$
The $\pi/6$ offset is the exact geometric imprint of the Birkhoff shear.

`[ALG]` **Anti-correlation frame:** $U=\frac{\sqrt3}{2}\rho$, $V=\eta_{\rm wrap}-\frac{\rho}{2}$, $U+iV=We^{-i\pi/6}$.

`[DEF]` The symbol $\ell$ denotes the winding index throughout this document, to avoid collision with normal-form coefficients such as $\nu_5$.

`[ALG]` **Winding-index invisibility.** Winding index $\ell\in\mathbb{Z}$ is invisible to all quantities entering through $\sin\eta$ or $\cos\eta$.

`[ALG]` [RID: DYAD-ALG-QC-CRITICAL-AMPLITUDE] `[v6.4.20; RID registered at adoption, 21 Oct 2026; owner check M3]` **Critical ISP amplitude:** $Q_c := (\arcsin(\ln 2))^2 \approx 0.5865$. If $Q < Q_c$ at pre-crossing, critical curve is unreachable at the crossing step.

### §6.5 Backbone and Asymptotic Structure — entry grades: ALG, THM, DEF, OPEN {#sec-6-5-backbone}

`[THM]` `[v6.4.20]` `[import: RECOG v0.3.22 §6.13b | RECOG-THM-A1A-RECIPROCAL-AMPLITUDE]` `[scope: $x_0\in U=\{0<Q\le\tfrac1{625}\}$; primitive $Q_m=Q(T^{6m}x_0)$]` **Leading decay.** $\lvert Q_{m+1}^{-1}-Q_m^{-1}-1\rvert<\tfrac{15}2\sqrt{Q_m}$ (RECOG proves it from DYAD-THM-PRIM-CTR alone), hence $Q_m^{-1}=Q_0^{-1}+m+O(\sqrt m)$, $Q_m=\dfrac1{m+Q_0^{-1}}+O(m^{-3/2})$ and $mQ_m\to1$; in primitive steps $n=6m$, $nQ\to6$.

`[DEF]` `[v6.4.20: replaces the v6.4.19 [ALG] "backbone law"]` **Historical backbone ansatz.** $Q_m\approx1/(m+\kappa_{\rm bb})$, $Q_n\approx6/(n+C_{\rm bb})$, $C_{\rm bb}=6\kappa_{\rm bb}$, with $\kappa_{\rm bb}$, $C_{\rm bb}$ fit parameters (SG-7). By the leading-decay statement an offset $\kappa_{\rm bb}$ is subleading and start-dependent, not a canonical constant. $47/54$, $37/40$ and $245/216$ remain distinct objects.

`[ALG]` `[scope: fixed-radius uniform-angle mean in the raw $W$-frame]` [RID: DYAD-ALG-RAW-ANGULAR-MEAN] `[v6.4.20; RID registered at adoption, 21 Oct 2026; owner check M8]` **Raw angular-mean recurrence coefficient.** Define
$$\mathcal A_{\rm raw}(Q):=\frac1{2\pi}\int_0^{2\pi}\bigl|F_W(\sqrt Q\,e^{i\theta})\bigr|^2d\theta .$$
The exact radial jet gives
$$\mathcal A_{\rm raw}(Q)=Q-Q^2+\tfrac{47}{54}Q^3+O(Q^4),\qquad \tfrac{47}{54}=\tfrac{19}{12}+2\Re c^{({\rm raw},6)}_{32}=[W^3\bar W^3]\,\Delta Q_6 ,$$
since odd total degrees average to zero and the degree-six $(3,3)$ coefficient is $47/54$. This is an averaging operator, not a pointwise recurrence for $Q$ along arbitrary primitive orbits (the pointwise update carries the nonzero $Q^{5/2}$ term below), and not by itself a long-orbit backbone theorem.

`[COR]` `[v6.4.10]` The former unqualified wording $Q_{m+1}=Q_m-Q_m^2+\tfrac{47}{54}Q_m^3+O(Q_m^4)$ did not identify its averaging or projection operator; it is superseded by the scoped statement above. Its historical occurrence and evidence are preserved (Appendix A). The $37/40$ positive-ray coefficient and the $47/54$ raw angular-mean coefficient are different scoped coefficients.

`[OPEN]` Any autonomous backbone recursion, the fitted logarithmic correction below, or a final-chart transfer requires its explicit observable/projection definition and proof or stated numerical scope. This ledger does not transfer those claims through $h$. RECOG R11 is CLOSED at its final-chart ledger scope; that closure does not identify the historical fitted backbone with the exact dynamics or transfer it through $h$.

`[ALG]` [RID: DYAD-ALG-ONE-BLOCK-BURST] `[v6.4.20; RID registered at adoption, 21 Oct 2026; owner check M7]` **One-block burst on the positive real primitive ray** $(\rho,\eta)=(t,0)$, $t>0$, $Q_0=t^2$:
$$Q(T^6(t,0))=t^2-t^4-\tfrac{5}{24}t^5+\tfrac{37}{40}t^6+O(t^7),\qquad\text{i.e.}\qquad Q_6=Q_0-Q_0^2-\tfrac{5}{24}Q_0^{5/2}+\tfrac{37}{40}Q_0^3+O(Q_0^{7/2}).$$
`[COR]` `[v6.4.10]` The half-power term is the ray restriction of $P_5=\tfrac{Q}{24}(5\eta^3-43\eta^2\rho+4\eta\rho^2-5\rho^3)$ (§6.14); the earlier form without it is superseded. The $Q_0^3$ coefficient $37/40$ is unchanged.

`[DEF]` $37/40$ (one-block burst, positive real ray) and $47/54$ (raw fixed-radius angular mean) are distinct objects; they must not be conflated.

`[DEF]` **Historical fitting ansatz — DSI logarithmic transport (retained, not identified with the exact primitive orbit law).** The recorded fitting form is
$$\kappa_{\rm fit}(M)\approx\tfrac{1}{Q_6}-1+\tfrac{7}{54}\ln(MQ_6)+O(1/M).$$
`[COR]` `[v6.4.10]` This records the earlier fit expression; it does not certify the displayed error or the logarithmic coefficient for the exact primitive dynamics of $T$. Its fitting protocol/surrogate, observation window, and the identification of its amplitude must accompany any use; the primitive/final-chart interpretation remains `[OPEN]` under the §6.5 and SG-19 non-transfer qualifications. `[v6.4.20]` The certified leading decay is the statement at the top of this section; the offset form $1/(m+\kappa_{\rm bb})$ is the historical ansatz. No new fit validation is claimed.

### §6.6 Resonant Structure and Homological Algebra — entry grades: ALG, DEF, OPEN {#sec-6-6-resonance}

`[ALG]` `[v6.4.20: retagged from [THM]; content stated exactly]` **$p=6$ linear order.** $\lambda=e^{i\pi/3}$ has order exactly six: $\lambda^j\ne1$ for $1\le j\le5$ and $\lambda^6=1$. This concerns the linear part only; it holds for every primitive root of unity and is not a uniqueness property of $p=6$.

`[ALG]` `[v6.4.20]` **Homological resonance is a separate condition.** In the one-step normal form a monomial $z^a\bar z^b$ ($a+b\ge2$) is resonant iff $\lambda^a\bar\lambda^b=\lambda$, i.e. $a-b-1\equiv0\pmod 6$. Resonant monomials occur at every odd degree and at no even degree: $z^2\bar z$ at degree 3 ($\lambda^2\bar\lambda=\lambda$; coefficient $n_{21}$), $z^3\bar z^2$ and $\bar z^5$ at degree 5 ($n_{32}$, $n_{05}$; DYAD-ALG-NF6). They stay in the normal form and cannot be removed by the normalizer. For non-resonant monomials the homological divisors $\lambda-\lambda^a\bar\lambda^b=\lambda(1-\lambda^{a-b-1})$ have modulus $1$, $\sqrt3$ or $2$, so no small divisors occur at any degree (`dyad_p1_math_checks.py` P1-3). `[COR]` `[v6.4.20]` The v6.4.19 sentence "No intermediate resonance obstruction occurs" conflated the order of $\lambda$ with homological resonance; it is withdrawn (Appendix A H-7).

`[DEF]` `[v6.4.20: replaces the v6.4.19 [THM] "three-tier hierarchy"]` **Classification by $p$** (declared $K_p$ family): sub-resonant $p<6$, resonant $p=6$, super-resonant $p>6$. A naming convention, not a theorem.

`[ALG]` `[v6.4.20]` `[import: RECOG v0.3.22 §6.10 | RECOG-ALG-NU3-CLOSED-FORM]` `[scope: $p\ge5$; declared $K_p$ family; $Z$ frame; local cubic order]` **Cubic radial rate across $p$.** $\Re\mu_p^Z=-p\sin^2(\pi/p)$: $-1.7275$, $-1.5$, $-1.3178$, $-1.1716$ for $p=5,6,7,8$, tending to $-\pi^2/p$. In the $W_p$ frame these values are multiplied by $\tan^2(\pi/p)$ (DYAD-ALG-KP-FRAME-SCALE, §6.9), so any comparison of decay across $p$ names its frame. The RECOG closed form has a pole at $p=3$ ($\lambda^2+\lambda+1=0$); $p=3,4$ are outside this import.

`[OPEN]` `[v6.4.20]` A harmonic-count comparison across $p$ needs a fixed degree cutoff; none is registered. The first pure lattice harmonic $(0,p-1)$ lies at degree $p-1$ (§2 OPEN 9).

`[ALG]` `[assuming: OPEN-P0 representation-phase convention]` **p=6 SU(2) period selection.** Under the OPEN-P0 convention assigning the SU(2) representation phase $e^{i\theta m}$ ($\theta=\pi/3$) to spin-$j$ states, the p=6 resonance condition selects integer-spin representations:
$$(\lambda_{j=1/2})^6=e^{i2\pi(1/2)}=-1\ne1\ \text{(period 12)},\quad (\lambda_{j=1})^6=e^{i2\pi}=1\ \text{(period 6)}.$$
Half-integer representations ($j=1/2,3/2,\ldots$) close at $p=12$, not $p=6$. The exact dyadic fact underlying this is solely $\lambda=e^{i\pi/3}=e^{iF_f/2}$ (§6.2); the representation-period statement is conditional on the OPEN-P0 phase-assignment convention, not an unconditional dyadic theorem. See SG-15.

`[ALG]` `[scope: structure]` **1-step resonance condition** for monomial $Z^a\bar Z^b$ under $e^{i\pi/3}$: resonant iff $a-b\equiv1\pmod{6}$.

> **[Local guard SG-5 applies]**

For general $p$: replace $6$ by $p$. First pure anti-holomorphic lattice harmonic is $(0,p-1)$ at degree $p-1$. Exception: $p=5$ has a degree-4 lattice channel $(0,4)$, so degree 4 is not globally nonresonant for all $p\ge5$.

**1-step resonance table** ($p=6$ case):

| Degree | 1-step resonant | 1-step non-resonant |
|---|---|---|
| 3 | $(2,1)$ | $(3,0),(1,2),(0,3)$ |
| 4 | none | all |
| 5 | $(3,2),(0,5)$ | $(5,0),(4,1),(2,3),(1,4)$ |

`[ALG]` `[scope: structure]` The 6-step tangent-to-identity normalization is different: all linear denominators vanish; retained channels are determined by the Lie operator $[\mu|Z|^2Z,\cdot]$ and the normalization convention.

### §6.7 Six-Step Cubic Jet and Complex Form — entry grades: ALG {#sec-6-7-jet}

`[ALG]` [RID: DYAD-ALG-SIXSTEP-CUBIC-JET] `[v6.4.20; RID registered at adoption, 21 Oct 2026; covers the jet and M+M^T=-I; owner check M5]` **6-step cubic jet** in primitive $(\rho,\eta)$ coordinates:
$$\rho_{n+6}=\rho+\tfrac43\eta^3-\tfrac52\rho\eta^2+\tfrac52\rho^2\eta-\tfrac76\rho^3+O(4),$$
$$\eta_{n+6}=\eta+\tfrac16\eta^3-\tfrac32\rho\eta^2+\tfrac32\rho^2\eta-\tfrac43\rho^3+O(4).$$

In the linear primitive eigenframe $X=(\Re W,\Im W)^\top$, $Q=\|X\|_2^2$: $X_{m+1}=X_m+MX_mQ_m+O(\|X_m\|^4)$,
$$M=\begin{pmatrix}-\tfrac12&\tfrac{2}{\sqrt3}\\-\tfrac{2}{\sqrt3}&-\tfrac12\end{pmatrix},\quad M+M^T=-I.$$
The identity $M+M^T=-I$ forces isotropic leading radial contraction.

`[ALG]` **Complex form (raw linear $W$-frame):**
$$W_{m+1}=W_m+\mu|W_m|^2W_m+O(|W_m|^4),\quad\mu=-\tfrac12-i\tau,\quad\tau=\tfrac{2\sqrt3}{3}.$$
`[COR]` `[v6.4.10]` The raw six-step jet has a nonzero quartic part (channels $(4,0),(3,1),(2,2),(1,3)$), so the remainder is $O(|W|^4)$, not $O(|W|^5)$; on the positive real ray $F_4(t)=-\tfrac{5+25i\sqrt3}{48}t^4$. The degree-4 term is removed only in the conjugacy chart $W=h(z,\bar z)$, where $\widehat F(z)=z+\mu z^2\bar z+O(|z|^5)$ in $z$, $q=|z|^2$ (§6.14).
$$\sigma=\tfrac12+i\tfrac{2\sqrt3}{3},\quad c_{21}=-\sigma.$$

### §6.8 ISP Transport and Footprint — entry grades: THM-ALG via IA, ALG {#sec-6-8-transport}

> **[Local guard SG-8 applies]**
> **[Local guard SG-9 applies]**

`[ALG]` `[scope: structure]` **Cubic-vector truncation only.** At cubic vector order:
$$Q_{m+1}=Q_m-Q_m^2+\tfrac{19}{12}Q_m^3+O(Q_m^4),\quad\Theta_{m+1}=\Theta_m-\tau Q_m+O(Q_m^2).$$

> The $19/12$ coefficient is the cubic-vector truncation contribution — it is not the raw fixed-radius angular-mean coefficient $47/54$ (§6.5). These are distinct objects; do not substitute one for the other.

`[ALG]` **Overshoot $R$ monotonicity.** $R$ is monotone non-decreasing in $\Theta$; strict monotonicity can fail only at isolated $Q=(2k-1)^2\pi^2$.

`[THM-ALG via IA]` `[RID: DYAD-THM-OPEN18]` **OPEN 18 closed.** First-footprint branch monotonicity: $dQ/dq>0$ and $d\Theta/dq<0$ on both branches $\Gamma_3$, $\Gamma_4$; $q=q_*$ is the branch split. Certificate: `open18_arb_cert_final.cpp`.

`[ALG]` `[scope: structure]` **ISP-safe funnel:** $\mathcal{S}_{\rm ISP}:=\{(Q,\Theta):Q<Q_c,\Theta\in[-2\pi/3,-\pi/3]\}$.

### §6.9 Normalization Hierarchy and Gauge — entry grades: ALG, DEF, FAIL {#sec-6-9-normalization}

> **[Local guard SG-5 applies]**
> **[Local guard SG-10 applies]**

`[ALG]` `[scope: structure]` **Four-object ontology for $p$-step normalization:**

| Label | Object |
|---|---|
| (a) | $\nu_5^{(1\text{-step,norm})}$ — quintic coefficient of normalized 1-step map |
| (b) | $c_{32}^{({\rm raw},p\text{-step})}$ — raw $(3,2)$ coefficient of exact discrete $p$-step jet $f^p$ |
| (c) | $\nu_5^{(p\text{-step,norm})}$ — $(3,2)$ coefficient of canonically normalized $p$-step map |
| (d) | $F_1^p=(\Phi_1^{-1}\circ f\circ\Phi_1)^p$ — exact conjugation identity; bridge gap $\Delta_p$ measures failure of $\Phi_1$ to commute with $f^p$ |

Objects (a)–(d) are distinct unless an explicit bridge theorem or normalization convention identifies them.

`[FAIL]` $\Im(\nu_5)$ is not invariant under general real-analytic residual gauge transforms. Gauge derivative $d\Im(u_{32})/d\lambda = -4\sqrt{3}/3 \ne 0$ computed exactly.

`[ALG]` `[conv: Lie strict-kernel gauge]` Canonical 6-step jet coefficients in $\mathbb{Q}(i\sqrt3)$ (`[v6.4.20]` field label corrected; values unchanged):
$$c_{21}^{({\rm raw},6\text{-step})}=-\tfrac12-i\tfrac{2\sqrt3}{3},\quad c_{32}^{({\rm raw},6\text{-step})}=-\tfrac{77}{216}+i\tfrac{97\sqrt3}{648},\quad c_{05}^{({\rm raw},6\text{-step})}=-\tfrac{61}{2160}-i\tfrac{43\sqrt3}{6480}.$$

`[ALG]` `[conv: Lie strict-kernel gauge]` $c_\theta^{(6)}=-119\sqrt{3}/648$.

`[ALG]` `[conv: Lie strict-kernel gauge]` **OPEN 17 closed:** $a_1=559\sqrt{15}/4860$, $a_2=86775991\sqrt{15}/755827200$. `[RID: DYAD-ALG-A1A2-LIEGAUGE]`

`[ALG]` **One-step to $p$-step bridge lemma:** $\mu_p = p\bar\lambda\nu_3^{(1,p)}$. `[RID: DYAD-ALG-BRIDGE-LEMMA]`  
`[v6.4.11]` General-$p$ proof (all $p\ge5$, via leading-defect equivariance $LG_k=G_k\circ L$): RECOG v0.3.20 §6.12 (RECOG-ALG-LEADING-RETURN-EQUIVARIANCE), cross-referenced as provenance. The Dyadic RID and statement are retained; ownership of RECOG's proof is not transferred by this cross-reference.  
`[ALG]` [RID: DYAD-ALG-KP-FRAME-SCALE] `[v6.4.20; RID registered at adoption, 21 Oct 2026]` `[proof: exact algebra; `dyad_p1_math_checks.py` P1-1]` **Frame qualifier for the bridge lemma.** The lemma holds in each linear eigenframe for that frame's one-step coefficient. For the declared $K_p$ family the two frames in use are $Z$ ($\eta=Z+\bar Z$, $\rho=uZ+\bar u\bar Z$, $u=1/(1-\lambda)$; RECOG) and $W_p=\rho+\tfrac{\lambda-1}{K_p}\eta$ (Dyadic; the §1 frame at $p=6$). Since $\bar u+\tfrac{\lambda-1}{K_p}=0$ and $u=\tfrac12+\tfrac i2\cot(\pi/p)$,
$$W_p=i\cot(\pi/p)\,Z .$$
Under $w=sz$ the coefficient of $z^a\bar z^b$ scales by $s^{1-a}\bar s^{-b}$, for $(a,b)=(2,1)$ by $|s|^{-2}$, and the convention "resonant normalizer coefficients zero" is preserved. Hence $\nu_3^{Z}=\cot^2(\pi/p)\,\nu_3^{W_p}$ and $\mu_p^{Z}=\cot^2(\pi/p)\,\mu_p^{W_p}$; arguments are frame-independent. At $p=6$: $W=i\sqrt3\,Z$, $\mu_6^Z=3\mu_6^W$, $\nu_3^Z(\zeta_6)=3n_{21}$. `[NUM]` One-step normal form computed in $W_p$, $p=5,\dots,50$: deviation from the rule $\le5\cdot10^{-13}$ (disposition check E5). **Interface rule:** an exported $\mu_p$ or $\nu_3$ names its frame.  
`[ALG]` `[v6.4.10]` Confirmed exactly at $p=6$ in the conjugacy chart: $\mu=6\bar\lambda n_{21}$ with $n_{21}=\tfrac18-\tfrac{7i\sqrt3}{72}$; the lattice slot transports the same way, $a_{05}=6\bar\lambda n_{05}$ with $n_{05}=\tfrac{43}{17280}-\tfrac{227i\sqrt3}{155520}$ (this $n_{05}$ equals the existing one-step ledger value $c^{(1,6)}_{05}$). **The $(3,2)$ slot does not transport linearly:** with $A=\bar\lambda n_{21}$, $B=\bar\lambda n_{32}$, iteration of the tangent-to-identity jet gives $[g^{\circ m}]_{32}=mB+\binom m2\,(2A^2+A\bar A)$, hence
$$a_{32}=6\bar\lambda n_{32}+15\bigl(2(\bar\lambda n_{21})^2+|n_{21}|^2\bigr)=-\tfrac{97}{432}+\tfrac{197i\sqrt3}{324},\qquad 15(2A^2+|A|^2)=-\tfrac{35}{144}+\tfrac{5i\sqrt3}{9}.$$
This is a $p=6$ finite-jet identity in the stated convention, not a universal quintic bridge for arbitrary $p$. It is consistent with SG-10 ($\Im\nu_5$ convention-dependent).

`[DEF]` `[v6.4.10]` **Operation-labelled objects (SG-19).** The raw values above are six-step raw coefficients (operation-independent). $c_\theta^{(6)}$, $a_1$, $a_2$ are `[conv: Lie strict-kernel gauge]` quantities of the archival object and are **not** identified with quantities in the conjugacy chart $W=h(z,\bar z)$ (§6.14). `[v6.4.20]` Permanent transfer guard (SG-19): RECOG R11 is CLOSED and its final-chart ledger confirms the non-transfer (chart quintic phase coefficient $+89\sqrt3/324$ against the archival $-119\sqrt3/648$; $245/216\ne47/54$). The three-channel log-projected model is a reduced model, not the normalized return. The four-object ontology (a)–(d) above is retained. `[ALG]` `[conv: additive degree-six polynomial normalizer of DYAD-ALG-NF6]` The chart resolves the finite-order conjugacy relation $\mathcal J_{\le6}(F_W\circ h-h\circ J)=0$. This is **not** a zero raw-to-normalized coefficient gap: $[J-F_W]_{(0,5)}=\tfrac{13-3i\sqrt3}{576}\ne0$, $[J-F_W]_{(3,2)}=\tfrac{19}{144}+\tfrac{11i\sqrt3}{24}\ne0$, and the quartic difference is $-F_4$. With $P=\mathcal J_{\le6}F_W$, the polynomial defect $D_{\rm poly}=P\circ h-h\circ J$ starts at degree seven; its bound is part of DYAD-THM-NF-REM (§6.14). The raw coefficient difference, the finite conjugacy residual, and the analytic remainder are distinct objects.

### §6.10 OPEN 11 / Chirality Closure — entry grades: THM-ALG via IA, ENG {#sec-6-10-open11}

`[THM-ALG via IA]` `[RID: DYAD-THM-OPEN11]` **OPEN 11 closed.** Chirality closure on scoped canonical family $(\rho_0,\eta_0)=(0,q)$, $q\in(0,2]$. T1: sign of $F'(I)$ at $q_{10/11}$ certified `[ALG via IA]` via IFT transversality (certificate: `certify_transition_strip2.cpp`, 256-bit Arb). T2: four-lemma proof scaffold complete. Both T1 and T2 are residual-free.

`[ENG]` **Arb/FLINT engine scope:** local certificate engine for short horizons ($\lesssim20$ steps). Long-horizon trajectory enclosure beyond the step-174 Lyapunov wall requires reachable-set methods, not higher precision.

### §6.11 OPEN 9 — $p$-Resonance Arithmetic Horizon — entry grades: ALG, THM, OPEN, FAIL {#sec-6-11-open9}

> **[Local guard SG-11 applies]**
> **[Local guard SG-12 applies]**

`[ALG]` `[family: p=5,6,7]` **Finite one-step ledger.** Exact coefficients:
- $p=6$: $c_{05}^{(1,6)} = \frac{43}{17280} - i\frac{227\sqrt{3}}{155520}$ in the one-step engine/DSN bridge convention; distinct from the raw six-step Lie-gauge coefficient $c_{05}^{({\rm raw},6\text{-step})}=-61/2160-i\,43\sqrt{3}/6480$ recorded in §6.9
- $p=5$: $\nu_5^{(5)}$ exact in $\mathbb{Q}(\zeta_5)$, $\zeta_5=e^{2\pi i/5}$ (real and imaginary parts in $\mathbb{Q}(\sqrt5,\sqrt{10+2\sqrt5})$; `[v6.4.20]` field label corrected; value unchanged). `[v6.4.13]` `[ALG]` [RID: DYAD-ALG-NU5-P5] Closed form $\nu_5^{(5)}=\tfrac{355-159\sqrt5}{48}+i\,\tfrac{(1106\sqrt5-2473)\sqrt{10+2\sqrt5}}{48}$, the $(3,2)$ coefficient of the one-step normal form of the declared $K_5$ family ($\rho'=\rho-\sin\eta$, $\eta'=\eta+K_5(e^\rho-1)-K_5\sin\eta$) in the frame $W_p=\rho+\tfrac{\lambda-1}{K_p}\eta$ (equal to the §1 frame at $p=6$) with resonant normalizer coefficients set to zero (the DYAD-ALG-NF6 convention). Certificate `dyad_m2c_nu5_p5_exact.py`: exact arithmetic in $\mathbb{Q}(\zeta_5)$; calibrated by reproducing $n_{21},n_{32},n_{05}$ of DYAD-ALG-NF6 exactly at $p=6$; negative control exits 1. This answers the Genesis provenance item M2c: the value printed in Genesis v2.8.7 §6.2 is confirmed in this convention.
- $p=7$: $c_{06}^{(7)}$ exact over $\mathbb{Q}(\zeta_7)$

`[ALG]` `[RID: DYAD-ALG-GLATTICE5]` **$p=5$ lattice cancellation.** $G_{\rm lattice}(5)=0$: both $F_1^5(0,4)$ and $F_{\rm raw}^5(0,4)$ are nonzero and equal:
$$F_1^5(0,4)=F_{\rm raw}^5(0,4)=-\tfrac{83}{24}\lambda^3-\tfrac{13}{24}\lambda^2-\tfrac53\lambda-\tfrac94.$$
Unique non-trivial degree-4 lattice bridge cancellation.

`[ALG]` **Exact $G_{04}(10)=0$ reinterpretation.** The $p=10$ result is not divisor inheritance: $(0,4)$ is dynamically active in $J^{extra,raw}_{10,5,D}$.

`[ALG]` `[RID: DYAD-ALG-VANISH-B2]` **Degree-2 raw-vanishing.** $F_{\rm raw}^p(0,2)=0$ for all $p\ge4$. The direct accumulated contribution carries weight $\lambda^{-3k}$ with orbit sum $\sum_{k=0}^{p-1}\lambda^{-3k}=0$ for $p\nmid3$. No pure anti-holomorphic cross-term exists at degree 2: under composition a term built from nonlinear parts of degrees $a,b\ge2$ has degree $a+b-1\ge3>2$ (`[COR]` `[v6.4.20]` v6.4.19 said "degree $\ge4$"; quadratic–quadratic composition already contributes at degree 3, e.g. $(x+x^2)\circ(x+x^2)=x+2x^2+2x^3+x^4$; the conclusion is unchanged). The direct mechanism is therefore the complete account, and the result is `[ALG]`. Resonant exception $p=3$ (nonzero). Verified numerically through $p=35$ as regression.

`[ALG]` `[RID: DYAD-ALG-VANISH-B3]` **Degree-3 raw-vanishing.** $F_{\rm raw}^p(0,3)=0$ for all $p\ge5$. Proof by automatic $\beta$-mode path enumeration (β-graded jet composition, which enumerates ALL cascade paths — resolving the earlier gap exposed by the $p=3$ nonzero case where the direct term already vanishes). The complete source $\beta$-set of the $(0,3)$ channel is $\{-3,-2,0\}$; it contains no secular mode ($\beta=1$). At a primitive $p$-th root, each term carries $\sum_{k=0}^{p-1}\lambda^{(\beta-1)k}=0$ unless $p\mid(\beta-1)$; the exceptional orders are $\{2,3,4\}$, so for $p\ge5$ every term vanishes. Boundary cases $p=3,4$ nonzero. Doubly certified: exact symbolic evaluation at $\lambda=e^{2\pi i/p}$ ($p=5..13$) and direct 50–60 dps iteration. Promoted from `[CAND]` `[target: ALG]` in v6.2. [cert: degree_b_vanishing_cert_v2.py] `[v6.4.20: registry name only; this file is not available in the project and has not been recreated; available evidence: rtg_betagraded_vanishing.py and degree_b_vanishing_cert.py (FA-DYAD-04)]`

`[ALG]` `[RID: DYAD-ALG-VANISH-B4]` **Degree-4 raw-vanishing.** $F_{\rm raw}^p(0,4)=0$ for all $p\ge6$. Proof by automatic $\beta$-mode path enumeration. The complete source $\beta$-set of the $(0,4)$ channel is $\{-4,-3,-2,-1,0,2\}$; it contains no secular mode ($\beta=1$). The exceptional orders are $\{2,3,4,5\}$, so for $p\ge6$ every geometric sum $\sum_{k=0}^{p-1}\lambda^{(\beta-1)k}$ vanishes, hence $F_{\rm raw}^p(0,4)=0$. The $(c_{02})^2$ quadratic-quadratic path (orbit sum $\tfrac12[(\sum_j\lambda^{2j})^2-\sum_j\lambda^{4j}]=0$ for $p\ge5$) is one contributing path among those the enumeration captures, not the whole story. Boundary cases $p=4,5$ nonzero ($p=5$ is the unique lattice anomaly $G_{\rm lattice}(5)=0$). Doubly certified: $\beta$-graded engine (exact) and direct high-precision iteration. Promoted from `[CAND]` `[target: ALG]` in v6.2. [cert: degree_b_vanishing_cert_v2.py] `[v6.4.20: registry name only; this file is not available in the project and has not been recreated; available evidence: rtg_betagraded_vanishing.py and degree_b_vanishing_cert.py (FA-DYAD-04)]`

`[ALG]` `[v6.4.20]` **Certificate audit (FA-DYAD-04).** Both available engines compose the full jet ($g_{n+1}=F\circ g_n$ with all lower-degree parts), so every degree-$(a+b-1)$ cross term is enumerated; neither uses the withdrawn "degree $\ge4$" argument. Owner reruns, 21 Oct 2026: `rtg_betagraded_vanishing.py` (SHA-256 `dec08174…d774`, DYAD-ART-VANISH-BGRADED) exits 0 with source $\beta$-sets $\{-2\}$, $\{-3,-2,0\}$, $\{-4,-3,-2,-1,0,2\}$ for $b=2,3,4$, matching the text; the source coefficients have denominators only in $\Phi_1\Phi_2\Phi_3\Phi_4$, nonzero at primitive $p$-th roots for $p\ge5$. `degree_b_vanishing_cert.py` (`c9a369e6…0dc6`) exits 0; its symbolic Route A treats the one-step coefficients as self-conjugate and reports the $(0,3)$ source set $\{-3,0\}$ (the $\beta=-2$ coefficient cancels under that simplification); the vanishing range is the same. The registry name `degree_b_vanishing_cert_v2.py` (DYAD-ART-VANISH-CERT) is not available in the project; the two files above are the available evidence. Grades unchanged.

`[ALG]` (all $p$, complete) [RID: DYAD-ALG-B5-ALLP-NONVANISHING] `[v6.4.20; RID for the b=5 statement (F_raw^p(0,5) != 0 for every p >= 6), registered at adoption, 21 Oct 2026; the lifecycle identifier DYAD-OPEN-B5-ALLP is unchanged]` **Channel classification boundary at $b=4$ (dyadic map).** Universal pure anti-holomorphic vanishing (for $p\ge b+2$) holds for $b\in\{2,3,4\}$ `[ALG]` (source $\beta$-sets carry no secular mode; exceptional orders bounded by $b+1$), and FAILS at $b=5$ for EVERY $p\ge6$ `[ALG]`. Proof of the $b=5$ failure: the $(0,5)$ source carries the secular mode $\beta=1$ with five-term coefficient $S\propto c_{02}^2$ (nonzero `[ALG]`). For $p=6..12$, exact cyclotomic certificates give $F_{\rm raw}^p(0,5)\ne0$ in $\mathbb{Q}(\zeta_p)$ `[ALG]` `[scope: finite sweep]` (e.g. $F_{\rm raw}^7(0,5)=\tfrac{15}{2}\lambda^5+\tfrac{23}{8}\lambda^4+\tfrac{21}{8}\lambda^3+\tfrac{15}{2}\lambda^2-\tfrac18\lambda+\tfrac{17}{2}$). For $p\ge13$, all nonsecular $m=0$ modes vanish (geometric sums, $p\nmid(\beta-1)$ for $\beta-1\in\{-6,\dots,-1,1\}$) and the polynomial mode $(-2,1)$ has exact sum $-p/(1-\lambda^{-3})$, giving the exact identity $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{\rm eff}$, $S_{\rm eff}=S-c_{(-2,1)}/(1-\lambda^{-3})$. The effective ratio is the explicit rational $S_{\rm eff}/S=N/D$ with $N=2\lambda^6+\lambda^5-5\lambda^4-3\lambda^3-4\lambda^2+2\lambda+1$ ($\lim_{\lambda\to1}=3$, `[ALG]`). Since $\deg N=6$, a primitive $p$-th root can be a zero of $N$ only if $\varphi(p)\le6$ (finitely many $p$: $\{1..10,12,14,18\}$); exact division shows $\Phi_p\nmid N$ for every one, so $N(\lambda_p)\ne0$ for all $p$, hence $S_{\rm eff}\ne0$ for all $p\ge13$. Therefore $F_{\rm raw}^p(0,5)\ne0$ for ALL $p\ge6$ `[ALG]` (complete proof, not a finite scan). Net `[ALG]` for the dyadic map: **universal pure anti-holomorphic raw vanishing holds for $b\in\{2,3,4\}$ and first fails at $b=5$, for every $p\ge6$.** Whether it fails for every $b\ge6$ is `[OPEN]` (all-$b\ge5$ persistence; scan-confirmed $b=6$ only), as is the general-coefficient version. `[COR]` `[v6.4.11]` The former wording "holds iff $b\le4$" asserted the open $b\ge6$ direction and is withdrawn. [cert: rtg_b5_Seff_limit_cert.py (all-$p$ closure); exact_Fraw_b5_sweep.py ($p=6..12$); rtg_b5_step3_reduction.py; rtg_extract_b5_secular_coeff.py (source)]

`[ALG]` `DYAD-ALG-P6-FACEFLUX` **p=6 / K₄ face-flux identity (OPEN-P0-DYADIC).** $\lambda=e^{i\pi/3}=e^{iF_f/2}$, $F_f=2\pi/3$; $E_{\rm full}/E_{\rm half}=4$ `[ALG]` (Pre-Legacy §1.8). The R11 cascade-gate conversion is `[ALG]`: at $\theta_f=2\pi/3$, the factor is $3/4$, so the cascade threshold $0.024$ maps to $\rho r^4\gtrsim0.032=4/125$. The threshold $0.024$ itself inherits OPEN-GEN-II-7B `[HYP]` status, so the gate's physical scope is `[HYP]` `[scope: inherited]` while the conversion is exact. `[CAND]` `[scope: conditional]` **h-transfer:** R11 treats $h$ as an external amplitude (Audit-1: $|H|_B=hr^2$ at the optimum). `[v6.4.20: Audit-1 = OPEN-M v0.7.1 R16, UVM-RESULT-AUDIT1, a conditional calibration branch. The 0.024 threshold and its image 4/125 inherit the reduced birth-race wrapper, the 9C raw-array premise, the large-g limit, state/window matching and the source normalization (OPEN-M v0.7.1; GEN-OPEN-UVJET-SCOPE); OPEN-M records no certified numerical deficit]` Whether the SU(2) factor enters $\rho=h\ell/(gm)$ as $\times2$, $\times4$, or not at all is undetermined by R11 and blocked from the dyadic side by Genesis SG-5. Any OPEN-M gate correction is `[CAND]` `[scope: conditional]` pending the h-source bridge (OPEN M proper). See §6.12, SG-15. [RID: DYAD-CAND-P0-DYADIC]

`[ALG]` **Subgroup-charge projector formalism.** Current OPEN 9 canonical objects: $\mathcal{Q}(p)$, $s=p/q$, $\chi_p(a,b)=a-b-1\pmod p$, $K^{\rm extra}_{p,q}$ with $|K^{\rm extra}_{p,q}|=s-1$, $\Pi^{\rm extra}_{p,q}$, $J^{extra,raw}_{p,q,D}$, $\mathcal{B}^{extra}_{p,q,D}$, $Z^{\rm miss}_{p,q,D}$, $C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, $\Delta_{\rm overlap}$. Eight of these objects ($\mathcal Q(p)$, $\Pi^{\rm extra}_{p,q}$, $J^{extra,raw}_{p,q,D}$, $\mathcal B^{extra}_{p,q,D}$, $Z^{\rm miss}_{p,q,D}$, $C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, $\Delta_{\rm overlap}$) have no recovered definition (Appendix D). Named source: the OPEN 9 owner working files of the v5.4.x series beyond `OPEN9_arithmetic_horizon_definitions.md`; next step: the owner locates them and records the definitions, or records them as unrecoverable.

`[ALG]` **Eigenframe linear-part lemma.** Anchors the degree-2 no-cascade bypass. Its statement is not recovered (Appendix D); named source: the OPEN 9 owner working files of the v5.4.x series; next step: the owner recovers and records the statement.

`[ALG]` **Exact micro-certifications:**
- [RID: DYAD-ALG-Q3-DEG2-CANCEL] `[v6.4.20; RID registered at adoption, 21 Oct 2026; evidence rtg_p_certs.py (DYAD-ART-P-CERTS), not rerun in P2]` Degree-2 $q=3,(0,2)$ cancellation for all $p>3$ with $3\mid p$.
- $p=8,q=4,(0,3)$: cancellation exact ($Q_8=0$ zero degeneracy).
- $p=12,q=4,(0,3)$: cascade boundary, exact value $-13+15\sqrt{3}/2\ne0$, modulus $\approx0.0096$.

`[FAIL]` Universal $q=4,(0,3)$ cancellation (the channel does NOT cancel for $p\ge12$; superseded in scope by the all-$p$ phase-law theorem below, which characterizes the surviving value).

`[THM]` `[proof: exact algebraic identity]` `[scope: all $p=4s$, $s\ge2$]` `[RID: DYAD-THM-Q403-PHASELAW]` **Cubic cascade $q=4,(0,3)$ all-$p$ phase/factorization law — CLOSED (v6.4.9).** For the subgroup-strobe cascade coefficient $Q_p=[\lambda^{-s}f_p^s-\mathrm{Id}]^W_{(0,3)}$ with $s=p/4$, $\lambda=\zeta_p$, on the family $p=4s$, $s\ge2$:
$$Q_p=i\,\zeta_p^3\,M_p,\qquad M_p=\frac{Q_p}{i\zeta_p^3}\in\mathbb{Q}(\zeta_p)^+,$$
i.e. the value factors as a universal phase direction $i\zeta_p^3$ times a real amplitude in the maximal real subfield. Equivalently $\arg(Q_p)=\tfrac{\pi}{2}+\tfrac{6\pi}{p}$ for the nonzero cases ($p\ge12$); $p=8$ is the zero degeneracy ($Q_8=0$, phase undefined). **Closed form** (with $L=\zeta_p$, $I=L^{p/4}=i$ forced on the family):
$$Q(L,I)=\frac{L^5\,(IL^2+I-L^2+1)}{2(L+1)^4(L^2+L+1)}.$$
**Proof** by the degree-3 near-identity recursion $(\mathcal H_s)_3=\sum_j H_{j,3}+\sum_{j<k}DH_{k,2}\cdot H_{j,2}$ ($\mathcal H_s=L^{-s}f^s$, $H_j=L^{-j}hL^j$, $h=L^{-1}f$): degree counting bounds the insertion depth to $\le2$ for the degree-3 channel, so exactly three paths feed $W_{(0,3)}$ — one cubic ($h^W_{(0,3)}$, charge $-4$, which cancels by the leading-cancellation sum $S_{-4}=0$, i.e. LEAD) and two ordered quadratic–quadratic paths (charges $(-1,-3)$ and $(-3,-1)$). The collapsed single/ordered-double sums use $L^{cs}=I^c$ at $s=p/4$. The remainder relation
$$\sigma_{-1}(Q)=-L^{-6}Q,\qquad \sigma_{-1}:L\mapsto L^{-1},\ I\mapsto -I$$
is an exact symbolic identity over $\mathbb{Q}(I)(L)$ (holds with $I$ a free symbol), giving $\sigma_{-1}(A_p)=\zeta_p^{-6}A_p$ for $A_p=[f^s]^W_{(0,3)}=iQ_p$, hence $M_p$ is $\sigma_{-1}$-fixed (real subfield). Denominator $2(L+1)^4(L^2+L+1)$ is nonzero for primitive $p$-th roots with $4\mid p$. **Verification:** closed form reproduces the certified in-field extractor values exactly at $p=8,12,\dots,52$ (independent method); three-path derivation, $h$-coefficient cross-check, and $\sigma_{-1}$ identity all symbolic. **Scope:** family statement for $p=4s$ via the forced collapse $I=\zeta_p^{p/4}=i$; NOT a generic-$s$ formula. The four supporting links are all-$p$: $\lambda^{-s}=-i$ `[THM]`, reality `[THM]`, leading cancellation $S_{-4}=0$ `[THM]`, remainder relation (R) `[THM]` `[proof: exact algebraic identity]`. [cert: q4_03_R_identity_certificate.py → CERTIFICATE PASS; q4_03_cascade_extract.py]

`[OPEN]` Bridge-gap smooth baseline: $G_{32}/K_p$ is not constant in tested ranges; exact smooth baseline form open.

`[ALG]` `[import: RECOG v0.3.20 §6.10 | RECOG-ALG-NU3-CLOSED-FORM, RECOG-ALG-NU3-NONVANISHING]` `[scope: declared family $\eta'=\eta+K_p(e^\rho-1)-K_p\sin\eta$, $K_p=2-\lambda-\bar\lambda$, $\lambda=e^{2\pi i/p}$; eigenframe $Z$; local cubic order]` **All-$p$ cubic radial contraction (v6.4.11 import).**
$$\nu_3(\lambda)=-\frac{\lambda^5-\lambda^4-\lambda^3-2\lambda^2+1}{2(\lambda-1)(\lambda+1)(\lambda^2+\lambda+1)},\qquad \Re\bigl(\bar\lambda\nu_3(e^{i\theta})\bigr)=-\sin^2\tfrac\theta2,$$
hence $\Re\mu_p^{Z}=-p\sin^2(\pi/p)<0$ and $k_{\rm ret}(p)=3$ for every $p\ge5$ (numerator has no root on $|\lambda|=1$ and is coprime to $\Phi_p$ for $\varphi(p)\le5$). Frame scale at $p=6$: $6\bar\lambda\nu_3(\zeta_6)=3\mu^{W}$; general $p$: DYAD-ALG-KP-FRAME-SCALE (§6.9, `[v6.4.20]`). `[NUM]` Dyadic-side spot check (16 Oct 2026, double precision): $\Re\mu_p^{Z}$ matches $-p\sin^2(\pi/p)$ (`[v6.4.20]` typo corrected; v6.4.19 read "$p\mu_p$ real parts") at $p=5,6,7,12,50$; $\arg\mu_p=-120.96^\circ,-113.41^\circ,-108.33^\circ,-96.74^\circ,-90.16^\circ$. Owner and certificate: RECOG (`recog_cell_a2_nu3_closed_form_cert.py`); not rerun here. **Scope:** local cubic radial contraction in the declared family only — not universal healing across generators, finite amplitudes, or physical birth mechanisms. Consequence for OPEN 9: the cubic layer is closed for all $p$; remaining OPEN 9 questions (missing slots, $b\ge5$ persistence, general coefficients) are higher-degree.

`[ALG]` [RID: DYAD-ALG-PROTECTION-MATRIX] `[v6.4.11 RID assignment; content unchanged]` **$p$-step protection matrix** ($p=6$, $K=1$; linear eigenframe $X=(\Re W,\Im W)$, cubic order; $=I+R^2M$ with $M$ of §6.7):
$$\mathcal{P}_{\rm dyad}(R^2)=\begin{pmatrix}1-R^2/2&\tau R^2\\-\tau R^2&1-R^2/2\end{pmatrix}.$$

### §6.12 Dyad-to-Triad Bridge Export — entry grades: ALG, DEF, CAND, OPEN {#sec-6-12-bridge}

> **[Local guard SG-13 applies]**

`[ALG]` The dyad-to-triad bridge exports a local $p=6$, $K=1$ module: antisymmetric primitive channels cancel even powers.

Certified exports: $\mu=-\frac{1}{2}-i\tau$; $\tau=2\sqrt{3}/3$; shear/healing ratio $4\sqrt{3}/3$; protection matrix $\mathcal{P}_{\rm dyad}(R^2)$.

`[DEF]` [RID: DYAD-DEF-BRIDGE-EXPORT-CONTRACT] `[v6.4.11]` **Bridge export contract.** This RID owns the *list and typing* of the dyad-to-triad exports, not a single theorem; each item keeps its own source, grade, frame and scope:

| Item | Source RID / location | Grade | Frame / scope |
|---|---|---|---|
| primitive linear frame $W=\mathcal L(\rho,\eta)=\rho+\omega\eta$, $v_\perp$ | §1, §6.14 definition of $\mathcal L$ | `[DEF]` | lifted local; no gauge choice |
| $\mu=-\tfrac12-i\tau$ | DYAD-THM-C21 | `[THM]` | raw six-step, $p=6$, $K=1$ |
| $\tau=2\sqrt3/3$ | §6.3 | `[ALG]` | constant |
| shear/healing ratio $4\sqrt3/3=\vert \Im\mu\vert /\vert \Re\mu\vert $ | derived from DYAD-THM-C21 | `[ALG]` | ratio of cubic coefficients; bookkeeping cross-reference (FC-DYAD-34): $(4\sqrt3/3)^2=16/3$ equals Genesis v2.8.9 §6.3's leading homogeneous-graph ratio $Q(c_{0,\rm shear}^{[3]})/Q(c_{0,\rm recoil}^{[3]})$ ($\kappa_{\rm shear}=-2\sqrt3/3$, $\kappa_{\rm recoil}=-\tfrac12$); arithmetic identity only, selects no birth policy |
| $\mathcal P_{\rm dyad}(R^2)$ | DYAD-ALG-PROTECTION-MATRIX | `[ALG]` | linear eigenframe, cubic order |
| $\mu_p=p\bar\lambda\nu_3^{(1,p)}$ | DYAD-ALG-BRIDGE-LEMMA | `[ALG]` | normalized one-step frame |

None of these items depends on the Lie strict-kernel gauge. Consumers currently routing them through `DYAD-ALG-LIEGAUGE-NORM` (Genesis v2.8.5 §7; Triadic v1.6 §7.1) are notified to repin (§7 notices); `DYAD-ALG-LIEGAUGE-NORM` remains the RID of the archival Lie-gauge normalization only.

`[DEF]` `[scope: bridge export boundary]` Not exported: Genesis lift scale $\beta$, phase convention, UV parameters, or OPEN-M source amplitude $h$. The dyadic alone does not fix $h$, $\alpha_f$, or $g$ (Genesis SG-5). Absolute Genesis parameters require external lift $W=\beta e^{i\chi}w$ or explicit projection matrix.

`[DEF]` `[scope: DYAD diagnostic export convention; mathematical diagnostic only; local raw $W$-frame]` **Odd-projected six-step residual.** Let
$$E_{\rm odd}(w):=\frac{F_W(w)-F_W(-w)}{2}-w .$$
This projects the already-iterated six-step primitive map about the origin. It is not a definition of the physical birth law.

`[ALG]` Analytic parity and the certified cubic return give
$$E_{\rm odd}(w)=\mu|w|^2w+O(|w|^5),\qquad E_{\rm raw}(w)-E_{\rm odd}(w)=\frac{F_W(w)+F_W(-w)}{2}=F_4(w)+O(|w|^6),$$
with $F_4(t)=-\tfrac{5+25i\sqrt3}{48}t^4\ne0$ on the positive real ray (§6.7); selecting $E_{\rm odd}$ therefore changes the exported object at fourth order relative to $E_{\rm raw}(w)=F_W(w)-w$. The normalized residual is a third object, $E_{\rm NF}(z)=\widehat F(z)-z=\mu|z|^2z+O(|z|^5)$, in the explicitly different chart of §6.14. Equality of leading coefficients does not identify these full residuals. Projection order matters: $[\operatorname{Odd}(f^{\circ6})]_{21}=\mu$ whereas $[(\operatorname{Odd}f)^{\circ6}]_{21}=\tfrac12-\tfrac{i\sqrt3}{6}$, so "antisymmetric" alone does not fix the object.

`[ALG]` **Birth kinematics connection (cubic parts).** For a real parent vector $s_*$ write $w_*=\mathcal L s_*$, $Q_s=|w_*|^2$, $J_Q=\mathcal L^{-1}i\mathcal L$, and $e_{\rm odd}(s_*)=\mathcal L^{-1}E_{\rm odd}(\mathcal L s_*)$. Its **cubic parts** are
$$e^{[3]}_{\parallel,*}=-\tfrac12Q_s s_*,\qquad e^{[3]}_{\perp,*}=-\tau Q_s J_Q s_* ,$$
with $\mu_6=\mu=-\tfrac12-i\tau$. A complete component expression retains its $O(\|s_*\|^5)$ remainder; the cubic parts are not the complete residual components. `[COR]` `[v6.4.10]` The former line "$E_*=\mu_6Q_ss_*+O(|s_*|^5)$" left $E_*$ untyped; the $O(|s_*|^5)$ form holds for $E_{\rm odd}$ and $E_{\rm NF}$, not for $E_{\rm raw}$.

`[OPEN]` **Physical bridge / consumer acceptance.** DYAD defines $E_{\rm odd}$ as an explicitly scoped diagnostic export. `[v6.4.11]` Genesis v2.8.5 (GCL-06; §§6.2–6.3) now records the representation-typed residuals $E_{\rm raw}^W$, $E_{\rm odd}^W$ and $E_{\rm NF}$ with the same cubic jet and remainder typing as this section (raw quartic witness $F_4(t)=-\tfrac{5+25i\sqrt3}{48}t^4$), replacing its former untyped $E_*=F_6(s_*)-s_*$. The **definition** is therefore consumer-recorded. Selecting any of these residuals as the physical birth mechanism, or identifying it with the realized fracture residual, remains `[OPEN]` in Genesis and is not established here. The established local cubic module ($\mu$, $\tau$, protection matrix) and its scope are unchanged.

`[ALG]` **OPEN-P0-DYADIC structural result.** $\lambda=e^{i\pi/3}=e^{iF_f/2}$, the SU(2) half-angle representative of the K₄ face flux $F_f=2\pi/3$ — an exact structural connection between the dyadic arithmetic-horizon program and the ESM geometry, independent of OPEN-M's determination of $h$.

`[CAND]` `[scope: conditional]` **OPEN-M calibration route (RESULT-P0-DYADIC).** `[v6.4.11]` OPEN-M v0.7.1 records no certified numerical deficit (R15: $h$ cancels; target conditional on 9C, large $g$ and state matching); the text below describes a conditional calibration branch, not the correction of an established deficit. The OPEN-M gate $\rho r^4\ge4/125$ has an `[ALG]` arithmetic conversion from the cascade threshold $0.024$ via the R11 factor $3/4$ at $\theta_f=2\pi/3$; the threshold inherits OPEN-GEN-II-7B `[HYP]` status. R11's source formula $|H|_B=hr^2$ treats $h$ as external (Audit-1). `[v6.4.20: Audit-1 = OPEN-M v0.7.1 R16, UVM-RESULT-AUDIT1. The 4/125 gate inherits the reduced birth-race wrapper, the 9C raw-array premise, the large-g limit, state/window matching and the source normalization (OPEN-M v0.7.1; GEN-OPEN-UVJET-SCOPE)]` The SU(2) energy ratio is 4 `[ALG]`, but whether this transfers to $\rho$ as $\times2$, $\times4$, or not at all depends on $h$'s source scaling, which R11 does not fix and Genesis SG-5 blocks from the dyadic side. The OPEN-M deficit characterization is therefore `[CAND]` `[scope: conditional]`. Resolution requires OPEN M proper. See SG-15. `DYAD-CAND-P0-DYADIC`

### §6.13 Simulation Invariants and Audit Discipline `[ENG]` {#sec-6-13-audit}

| Element | Specification |
|---|---|
| Map | $\rho'=\rho-\sin\eta$, $\eta'=\eta+(e^\rho-1)-\sin\eta$ |
| Wrap | $\eta_{\rm wrap}\in(-\pi,\pi]$ |
| Observable | $Q_{\rm true}=\rho^2-\rho\eta_{\rm wrap}+\eta_{\rm wrap}^2$ |
| Analytic coordinate | $W_{\rm DSN}=u+iv$, $Q=\vert W_{\rm DSN}\vert ^2$ — $p=6$ primitive frame |
| ISP variables | $(Q,\Theta,\ell)$ — diagnostic/structural layer |
| Sampling | Six-step / resonant-block |
| Precision | dps $\ge120$ |
| Canonical audit | `rtg_dyad_audit.py` |
| Pre-crossing predicate | $\rho<0$, $\sin\eta<0$, $\rho-\sin\eta\ge0$ |
| Safety columns | separate `ceiling_ok`, `Q<Q_c`, `rho'<ln2` |
| Late-window fitting | Fixed-parameter / fixed-$\alpha$ only |
| Repository | `rtg-resonance-2025` |

Audit discipline: stamp all exported quantities with their layer (`primitive`, `ISP`, `raw_pstep`, `F1^p`, `normalized_pstep`, `observable_fit`).

---

### §6.14 Local Return Enclosure — Normalizer, Contraction, Inverse, Remainders — entry grades: ALG, THM, DEF, OPEN, NUM, ENG {#sec-6-14-enclosure}

> **[Local guard SG-19 applies]** · **[Local guard SG-10 applies]** · **[SG-14: all statements conditional on the postulated generator $T$]**

**Provenance (v6.4.10).** Multi-round audit and certificate campaign, Sep 2026: P0–P1 normalization audit; P2-A v1/v2 primitive contraction; P2-B v1/v2 coordinate and normalized remainders. Producer/validator: exact-rational certificates (ChatGPT). Independent verification: three reviewer records with independent exact reconstruction (Claude) and an exit-coded referee harness (§8, DYAD-ART-RE-REFEREE). Status axes per Methodology v1.3: evidence/review complete; owner adoption recorded (v6.4.10, 24 Sep 2026); downstream (RECOG/NUMGEN) closure **not** obtained.

`[DEF]` **Objects.** $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta)$, $F=T^6$; $\mathcal L(\rho,\eta)=\rho-\tfrac\eta2+i\tfrac{\sqrt3}{2}\eta$ (the §1 Birkhoff frame, lifted local phase, no wrapping seam); $f=\mathcal L T\mathcal L^{-1}$, $F_W=f^{\circ6}$, $Q_{\rm prim}=|W|^2$. $\lambda=\tfrac{1+i\sqrt3}{2}$ (branch fixed). Chart: $W=h(z,\bar z)$ with $h=\mathrm{id}+h_2+\cdots+h_6$ the exact additive polynomial (23 nonzero coefficients incl. linear, all in $\mathbb{Q}(i\sqrt3)$) determined by the one-step homological equation with the **resonant monomial coefficients of each $h_n$ set to zero** (resonance $a-b-1\equiv0\bmod6$); complete table: `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` → `DYAD_RETURN_ENCLOSURE_P2B_v2/outputs/certificate.json`, keys `jets.h_degree6`, `jets.J_through6` (hash in the installation manifest). $q=|z|^2$. Notation used below: $P:=\mathcal J_{\le6}F_W$; $D_{\rm poly}:=P\circ h-h\circ J$; $M(s)$ the coefficient-modulus majorant of $h-\mathrm{id}$ (DYAD-THM-NF-INV), $H(s):=s+M(s)$; $\Psi(s):=s+(e^{as}-1-as)+(\sinh as-as)$ with $a=\tfrac76$, $S_0(s):=s$, $S_{j+1}(s):=\Psi(S_j(s))$; primitive iterates $Q_m:=Q_{\rm prim}(F^mx)$, normalized iterates $q_m:=|\widehat F^m z|^2$ — these two sequences are **not** identified by the coordinate-comparison inequalities. Decimal values quoted in parentheses are approximations of exact rational certificate quantities. $\widehat f=h^{-1}fh$, $\widehat F=h^{-1}F_Wh$ are exact maps on their proved domains; $n$, $J$ are their **finite jets**.

`[ALG]` `[RID: DYAD-ALG-NF6]` **One-step polynomial normalizer and six-step normal-form jet (finite-order identities).**
$$\mathcal J_{\le6}(f\circ h-h\circ n)=0,\qquad \mathcal J_{\le6}(F_W\circ h-h\circ J)=0,$$
$$h_2=-\tfrac{1+i\sqrt3}{12}z^2-\tfrac13z\bar z+\tfrac{1-i\sqrt3}{24}\bar z^2\ \ (\text{unique quadratic change removing }F_4\text{; cancellation system rank 6}),\qquad h_3\ne0\ (\text{channels }(3,0),(1,2),(0,3)),$$
$$n=\lambda z+n_{21}z^2\bar z+n_{32}z^3\bar z^2+n_{05}\bar z^5,\quad n_{21}=\tfrac18-\tfrac{7i\sqrt3}{72},\ n_{32}=-\tfrac5{432}+\tfrac{23i\sqrt3}{3888},\ n_{05}=\tfrac{43}{17280}-\tfrac{227i\sqrt3}{155520},$$
$$J(z)=z+\mu z^2\bar z+a_{32}z^3\bar z^2+a_{05}\bar z^5,\quad \mu=-\tfrac12-\tfrac{2i\sqrt3}{3},\ a_{32}=-\tfrac{97}{432}+\tfrac{197i\sqrt3}{324},\ a_{05}=-\tfrac{49}{8640}-\tfrac{307i\sqrt3}{25920}.$$
$J=\mathcal J_{\le5}\,n^{\circ6}$; $\mu=6\bar\lambda n_{21}$, $a_{05}=6\bar\lambda n_{05}$, and the $(3,2)$ relation with its second-order term is recorded at DYAD-ALG-BRIDGE-LEMMA (§6.9). Transport constraint $3\Re n_{32}+3\sqrt3\,\Im n_{32}=\tfrac1{54}$ holds exactly. The regenerated `phi1_p6_deg5.json` from the recovered solver agrees with the independent solve on all 18 nonzero exported coefficients (to $\sim5\times10^{-81}$); historical byte identity of the original output file is `[OPEN]` (convention identity is established by the ledger identities above, not by the file).

`[ALG]` `[RID: DYAD-ALG-NF6-OBS]` **Normalization obstruction (raw $c_{05}$ is not a conjugacy-chart coefficient).** After the unique $h_2$, no cubic correction $h_3$ can change the $(0,5)$ coefficient of $h^{-1}F_Wh$ (all eight real directions verified), and
$$c^{({\rm raw},6)}_{05}-a_{05}=\tfrac{-13+3i\sqrt3}{576}\ne0.$$
Hence the three-channel model that deletes $F_4$ but keeps raw $c_{05}$ is **not** conjugate through degree 5 to the primitive return by any identity-linear polynomial change. This does not affect the raw coefficients, $\mu$, local contraction, or the existence of a nonzero lattice harmonic; it excludes *transferring* raw $c_{05}$ into that model (SG-19).

`[ALG]` `[v6.4.20 entry; RID registered at adoption, 21 Oct 2026]` [RID: DYAD-ALG-P5-RADIAL] **Degree-five radial part of the six-step return.** In primitive coordinates $Q(T^6x)-Q=-Q^2+P_5+O(\|x\|^6)$ with $P_5=\tfrac{Q}{24}(5\eta^3-43\eta^2\rho+4\eta\rho^2-5\rho^3)$, $Q=\rho^2-\rho\eta+\eta^2$; the quadratic and cubic parts vanish. This registers as a result the identity used inside `DYAD-THM-PRIM-CTR` below; no statement changes. Owner check M6.

`[THM]` `[proof: analytic majorant + exact-rational certificate]` `[RID: DYAD-THM-PRIM-CTR]` **Primitive contraction and six-phase invariant tube.** With $P_5=\tfrac{Q}{24}(5\eta^3-43\eta^2\rho+4\eta\rho^2-5\rho^3)$ and $R^{\rm prim}_{\ge6,\rm rad}=Q(T^6x)-Q+Q^2-P_5$:
$$|R^{\rm prim}_{\ge6,\rm rad}(x)|\le108\,Q(x)^3\quad(0\le Q\le\tfrac1{400}),\qquad 0<Q-\tfrac32Q^2\le Q(T^6x)\le Q-\tfrac12Q^2<Q\quad(0<Q\le\tfrac1{400}).$$
Method: exact signed radial degrees $-Q^2$, $P_5$, $P_6$, $P_7$ (phase-uniform rational ceilings $|P_5|\le\tfrac{16931}{10000}Q^{5/2}$, $|P_6|\le\tfrac{6671}{5000}Q^3$, $|P_7|\le\tfrac{3567}{1000}Q^{7/2}$; $[W^3\bar W^3]P_6=\tfrac{47}{54}$, cf. §6.5), scalar majorant $\Psi$ ($a=\tfrac76>\tfrac2{\sqrt3}$), applied only from radial degree 8 ($|R^{\rm prim}_{\ge8}|\le42355\,Q^4$ on $Q\le\tfrac1{400}$). Tube: $U=\{0<Q\le\tfrac1{625}\}$, $U_T=\bigcup_{j=0}^{5}T^j(U)$; $\max_j|W(T^jx)|<\tfrac{47}{1000}$ on $U$, so $T(U_T)\subseteq U_T\subset\{0<Q<\tfrac{2209}{10^6}\}$; every trajectory in $U_T$ tends to $0$, no nonzero periodic orbit in $U_T$; $Q_m\le Q_0/(1+\tfrac12Q_0m)$, $\sum_mQ_m^2\le2Q_0$, $\sum_mQ_m^3\le2Q_0^2$. At $Q=0$ the map is fixed (strictness excluded). Weaker baseline $(1560,\tfrac1{3600},\tfrac1{10000})$ (P2-A v1) retained as valid. The radius is sufficient, not optimal. **NUMGEN interface** `[ALG]`: the exact seed $(\rho,\eta)=(\tfrac1{100},\tfrac1{250})$ has $Q_0=\tfrac{19}{250000}<\tfrac1{625}$ and is admitted to $U$ (ratio $\tfrac{400}{19}$); this discharges its radial/tube-membership premise only, **not** the additional angular inequalities of GAP-LOCK. NUMGEN's L1 ownership is unchanged.

`[THM]` `[proof: majorant + contraction mapping]` `[RID: DYAD-THM-NF-INV]` **Quantitative inverse chart.** With $M(s)=\tfrac7{12}s^2+\tfrac{39}{500}s^3+\tfrac{14}{125}s^4+\tfrac{11}{250}s^5+\tfrac1{20}s^6$ (coefficient-modulus ceilings of $h-\mathrm{id}$; degree 2 exact), $R=\tfrac1{10}$: $\kappa=M'(R)=\tfrac{358439}{3000000}<\tfrac18$, $R-M(R)>\tfrac9{100}$, $M(R)/R<\tfrac1{16}$, $M''(R)=\tfrac{368381}{300000}$. Hence $h$ is injective on $|z|\le\tfrac1{10}$ (segment integration, $h$ treated as a real $\mathbb R^2$ map), $h^{-1}$ exists on $|W|\le\tfrac9{100}$ by the contraction $z\mapsto W-(h(z)-z)$, $\|Dh^{-1}\|_2<\tfrac87$, $\|Dh^{-1}-I\|_2<\tfrac17$, and on $|z|\le\tfrac1{10}$
$$\tfrac{15}{16}|z|\le|h(z)|\le\tfrac{17}{16}|z|,\qquad \tfrac{225}{256}|z|^2\le Q_{\rm prim}\bigl(\mathcal L^{-1}h(z)\bigr)\le\tfrac{289}{256}|z|^2 .$$
These are comparison inequalities; $Q_{\rm prim}$ is **not** identified with $q=|z|^2$, and the primitive comparator transports as $\overline{h(z_a)}\,h(z_b)$, not $\bar z_az_b$.

`[THM]` `[proof: exact vector jet to degree 9 + majorant tail from degree 10 + finite defect + differentiated conjugacy identity]` `[RID: DYAD-THM-NF-REM]` **Radius-indexed normalized remainders (first real derivative, Euclidean norm).** In the chart of DYAD-THM-NF-INV, for the exact map $\widehat F=h^{-1}F_Wh$ and the jet $J$ of DYAD-ALG-NF6:

| $\vert z\vert \le$ | $\vert \widehat F(z)-J(z)\vert \le C_7\vert z\vert ^7$ | $\Vert D\widehat F(z)-DJ(z)\Vert _2\le C_D\vert z\vert ^6$ |
|---|---|---|
| $\tfrac1{20}$ | $C_7=100$ (certificate value $85.07$) | $C_D=1000$ (certificate value $812.89$) |
| $\tfrac1{40}$ | $C_7=30$ (certificate value $27.60$) | $C_D=250$ (certificate value $216.77$) |

Constants travel with their radius and this chart; profiles are not to be mixed. Ingredients: vector ceilings $|F_7|\le\tfrac{2079}{1000}|W|^7$, $|F_8|\le\tfrac{577}{500}|W|^8$, $|F_9|\le\tfrac{1763}{1000}|W|^9$; tail $|R^{\rm prim}_{\ge10,\rm vec}|\le332000|W|^{10}$ on $|W|\le\tfrac1{16}$; the **finite conjugacy defect** $D_{\rm poly}$, which vanishes through degree 6 but not identically ($[D_{\rm poly}]_{(0,7)}=\tfrac{31}{9720}-\tfrac{77i\sqrt3}{19440}$), bounded by $|D_{\rm poly}(z)|\le C_{\rm poly}(r)|z|^7$ for $|z|\le r$ with $C_{\rm poly}(\tfrac1{20})<17$, $C_{\rm poly}(\tfrac1{40})<16$; all compositions enclosed in the inverse domain ($H(\tfrac1{20})<\tfrac1{16}$, $S_6(H(\tfrac1{20}))<0.0653<\tfrac9{100}$). The full tube of DYAD-THM-PRIM-CTR maps into the normalized disk: $\tfrac{16}{15}\max_{j\le5}S_j(\tfrac1{25})<\tfrac1{20}$, so $\widehat U_T=h^{-1}(\mathcal L(U_T))\subset\{|z|<\tfrac1{20}\}$ is invariant under $\widehat F$. **Normalized one-orbit contraction** `[THM]`: $0<q-\tfrac32q^2\le|\widehat F(z)|^2\le q-\tfrac12q^2$ for $0<q\le\tfrac1{400}$ (rational certificate margin $\approx0.011$ vs $\tfrac12$), giving $q_m\le q_0/(1+\tfrac12q_0m)$ and $\sum_mq_m^3\le2q_0^2$ directly in the normalized sequence $q_m$. Weaker baseline P2-B v1 $(\tfrac1{40};\,8000,\,60000)$ retained as valid. The withdrawn $(64,\tfrac1{256},\tfrac1{1024})$ record is listed in Appendix B (withdrawn, not falsified).

`[ALG]` [RID: DYAD-ALG-NF6-DEG10] `[v6.4.11]` `[scope: fixed adopted $h_6$ of DYAD-ALG-NF6; exact Taylor computation through total degree 10]` `[provenance: Claude-checked written verification record `DYAD_CHECK_degree10_even_term_hatF.md` (25 Sep 2026, SHA-256 `dcfd808c…f4d4`), exact $\mathbb Q(i\sqrt3)$ engine `dyad_return_qchi_exact.py` (`e45286fa…50f6`) shared with DYAD-ART-RE-REFEREE, independent of producer/validator code; confirms the third-party PRR_RRF_REVIEW_v1 report; registered in RRF v0.8 as finding VF-1]` **Degree-ten even term of the delivered map.** For $\widehat F=h_6^{-1}\circ F_W\circ h_6$ with $h_6^{-1}$ taken as the degree-ten Taylor jet of the certified local inverse ($h_6\circ h_6^{-1}=\mathrm{id}$ verified through degree 10): $\mathcal J_{\le6}\widehat F=J$; the even homogeneous parts of degrees 2, 4, 6, 8 vanish identically; the degree-10 even part does not, with
$$[\widehat F]_{(5,5)}=-\tfrac{6113}{839808}-\tfrac{3152683}{403107840}\,i\sqrt3\ne0.$$
Consequences, at this scope only: $\widehat F(-z)+\widehat F(z)\not\equiv0$ and $\chi_1(-z)-\chi_1(z)\not\equiv0$ (identity failure, not a pointwise lower bound); $\chi_m$, $m\ge2$, not computed. Not affected: the formal all-order normal form (odd), the jet $J$, DYAD-THM-NF-REM, DYAD-THM-PRIM-CTR. Reading: a degree-6 truncated normalizer is not expected to preserve normal-form parity beyond its order; this is a property of the delivered chart/action pair, not of the primitive dynamics.

**OPEN 3 — spiral residual in the chart (v6.4.14).** Sources: scope note v0.1.1, P1/P2 record v0.1, P3 record v0.1 and review disposition v0.1 (§8 DYAD-ART-OPEN3-RECORDS); all reviewed 19 Oct 2026 as SESSION records.

`[DEF]` `[v6.4.14]` **Fit-free spiral residual.** Frame $W=\mathcal L(\rho,\eta)=\rho-\tfrac\eta2+i\tfrac{\sqrt3}2\eta$, $Q_{\rm prim}=|W|^2$; chart $W=h(z,\bar z)$ (DYAD-ALG-NF6), $q=|z|^2$; block counter $m$ for $F=T^6$, $W_m=h(z_m)$ exactly. Per-block angle increments are principal values, $\Delta\Theta_W=\operatorname{Arg}(W_{m+1}/W_m)$, $\Delta\Theta_z=\operatorname{Arg}(z_{m+1}/z_m)$ (the $\approx2\pi$ winding of the six intermediate steps is excluded). Static offsets $D_Q:=|h(z)|^2-|z|^2$ and $D_\Theta:=\operatorname{Arg}(h(z)/z)$ (principal; $|h(z)/z-1|<\tfrac1{16}$ on $|z|\le\tfrac1{10}$ by DYAD-THM-NF-INV). Spiral residuals: $S_Q:=\Delta Q_{\rm prim}-\Delta q=D_Q\circ\widehat F-D_Q$ (difference of **absolute** radial increments) and $S_\Theta:=\Delta\Theta_W-\Delta\Theta_z=D_\Theta\circ\widehat F-D_\Theta$ (as real numbers on the certified domains). These are not fit residuals; no window or backbone enters.

`[ALG]` [RID: DYAD-ALG-OPEN3-LEADING] `[v6.4.14]` `[scope: chart of DYAD-ALG-NF6; one F-block; leading homogeneous terms; normalized $z=re^{i\Theta}$]` **Exact leading terms.** Only $h_2$ and $\mu=-\tfrac12-i\tfrac{2\sqrt3}3$ enter:
$$D_3:=[D_Q]_3=2\operatorname{Re}(\bar zh_2)=r^3\bigl[-\tfrac56\cos\Theta+\tfrac{\sqrt3}6\sin\Theta+\tfrac1{12}\cos3\Theta-\tfrac{\sqrt3}{12}\sin3\Theta\bigr],$$
$$D_{\Theta,1}:=[D_\Theta]_1=\Im(h_2/z)=r\bigl[-\tfrac{\sqrt3}{12}\cos\Theta+\tfrac14\sin\Theta-\tfrac{\sqrt3}{24}\cos3\Theta-\tfrac1{24}\sin3\Theta\bigr],$$
$$[S_Q]_5=DD_3(z)[\mu qz]=r^5\bigl[\tfrac{11}{12}\cos\Theta-\tfrac{29\sqrt3}{36}\sin\Theta+\tfrac38\cos3\Theta+\tfrac{7\sqrt3}{24}\sin3\Theta\bigr],$$
$$L_\Theta:=[S_\Theta]_3=DD_{\Theta,1}(z)[\mu qz]=r^3\bigl[-\tfrac{\sqrt3}8\cos\Theta-\tfrac7{24}\sin\Theta+\tfrac{5\sqrt3}{48}\cos3\Theta-\tfrac{11}{48}\sin3\Theta\bigr]=-\tfrac{\sqrt3}{48}X^3-\tfrac{47}{48}X^2Y-\tfrac{7\sqrt3}{16}XY^2-\tfrac1{16}Y^3,$$
($D$ the real derivative, $z=X+iY$), and the radial transport identity
$$P_5(\mathcal L^{-1}z)=DD_3(z)[\mu qz]+2q\,D_3(z),$$
with $P_5$ of DYAD-THM-PRIM-CTR. Only harmonics $k=\pm1,\pm3$ occur. Exact ceiling $|L_\Theta|\le\tfrac{7+2\sqrt{19}}{24}q^{3/2}$. **$S_Q$ is not $P_5$:** $P_5$ is the quintic term of the primitive radial increment, $S_Q$ the primitive–normalized difference; the cross term $-2qD_3$ from $-Q^2$ versus $-q^2$ is essential (the v0.1 scope-note form without it was wrong and is withdrawn). *Certificate:* DYAD-ART-OPEN3-P2 (exit-gated; negative controls: wrong $\omega$ branch, missing $2qD_3$, flipped cross-term sign, flipped and conjugated angular direction — all fail). Reviewer re-derivation by an independent polynomial method: PASS.

`[THM]` [RID: DYAD-THM-OPEN3-SPIRAL-REM] `[v6.4.14]` `[proof: analytic majorant + exact-rational certificate]` `[scope: chart of DYAD-ALG-NF6; NF-REM rows, not mixed]` **Certified per-block remainders.** For each row and every $0<|z|\le r$:
$$|S_\Theta(z)-L_\Theta(z)|\le K_\Theta q^2,\qquad |S_Q(z)-[S_Q]_5(z)|\le K_Q q^3,$$

| $\lvert z\rvert\le$ | $C_7$ used (NF-REM) | $K_\Theta$ | $K_Q$ | $c_1$ | $c_2$ |
|---|---|---|---|---|---|
| $\tfrac1{20}$ | 100 | $\tfrac{123}{125}$ | $\tfrac{2353}{1000}$ | $\tfrac{261}{1000}$ | $\tfrac{393}{500}$ |
| $\tfrac1{40}$ | 30 | $\tfrac{909}{1000}$ | $\tfrac{258}{125}$ | $\tfrac{51}{200}$ | $\tfrac{96}{125}$ |

with static constants $|D_\Theta-D_{\Theta,1}|\le c_1q$, $\|DD_\Theta\|\le c_2$ on the row, and $\|D^2D_{\Theta,1}(w)\|\le c_3/|w|$, $c_3=\tfrac23$. The disks are forward-invariant ($|\widehat Fz|^2\le q-\tfrac12q^2$ for $q\le\tfrac1{400}$, NF-REM), so the bounds hold at every block of every orbit started in the row's disk. Primitive-amplitude form via $q\le\tfrac{256}{225}Q_{\rm prim}$ (NF-INV): $|S_\Theta-L_\Theta|\le\tfrac{637}{500}Q^2$ resp. $\tfrac{1177}{1000}Q^2$; $|S_Q-[S_Q]_5|\le\tfrac{1733}{500}Q^3$ resp. $\tfrac{3041}{1000}Q^3$ ($L_\Theta$, $[S_Q]_5$ evaluated at $z=h^{-1}(W)$; $Q$ and $q$ are not identified).

*Proof outline* (full text in the P3 record). Block displacement $\widehat Fz-z=\mu qz+\rho$, $|\rho|\le A_5|z|^5+C_7|z|^7$ ($A_5=|a_{32}|+|a_{05}|$; NF-REM). Angular: with $g=(h-z)/z$, $g_1=h_2/z$, $S_\Theta-L_\Theta=A_1+A_2+B+C$ (second-order Taylor term of $g_1$, using $\|D^2(\bar w^2/w)\|\le8/|w|$; $Dg_1[\rho]$; increment of $g-g_1$; increment of $\Im[\operatorname{Log}(1+g)-g]$ on the principal branch). Radial: $D_Q$ is an exact polynomial of degrees 3–12 (the explicit $Q\leftrightarrow q$ bridge); its degree-3 part is expanded to second order, degrees $\ge4$ by the mean-value inequality. DYAD-THM-PRIM-CTR is not an input. Each majorant divided by $s^4$ (resp. $s^6$), $s=|z|$, is nondecreasing, so it is evaluated at $s=r$ in exact rational arithmetic; stated constants are three-decimal ceilings. *Certificate:* DYAD-ART-OPEN3-P3 (exit 0; negative controls `neg_K`, `neg_h2`, `neg_mu` exit 1; reviewer replay byte-identical).

`[DEF]` `[v6.4.14]` **Recorded distinctions.** (i) The constants are suprema of **majorants**, attained at $s=r$; they are not the suprema of the true errors ([NUM] sampled maxima: $|S_\Theta-L_\Theta|/q^2\approx0.196$, $0.189$; $|S_Q-[S_Q]_5|/q^3\approx0.949$, $0.909$; $|\widehat F-J|/|z|^7\approx0.971$ against the adopted $C_7=100$, $30$, which are used unchanged). (ii) The per-block theorem does **not** by itself prove the primitive asymptotic-phase transfer (OPEN 3b / P4); along an orbit $\sum_{m<M}S_\Theta(z_m)=D_\Theta(z_M)-D_\Theta(z_0)$ telescopes. (iii) $h$ and $J$ were regenerated exactly from $T$ and checked against the adopted data ($h_2$; 23 coefficients; resonant coefficients zero; $M(s)$ ceilings; $\mu$; RECOG-ALG-CHART-LAWS identities $\tfrac{245}{216}$, $\tfrac{89\sqrt3}{324}$) and coefficient-by-coefficient (23/23) against the independent 19 Sep 2026 audit reconstruction `coordinate_h_deg6_reconstructed.json` (`bb09bace…99f6`; marked "not historical owner artifact"). Coefficient verification against the adopted P2B v2 `certificate.json` (`jets.h_degree6`, `jets.J_through6`) is complete: the v6.4.16 record shows the reproduced $h$, $J$ coefficients equal the certificate coefficients in exact arithmetic. This is coefficient equality, not byte identity of files; no byte-identity check is claimed.

`[OPEN]` `[v6.4.20]` **Not established (current; consolidates the v6.4.14–v6.4.16 lists relocated to Appendix A H-2):** any statement on $C_{\rm est}$, $\kappa_{\rm est}$ (SG-7); transfer of the chart coefficients to NUMGEN L1 primitive phase coefficients, ISP-angle coefficients, $47/54$, $c_\theta^{(6)}$, $a_1$, $a_2$ (SG-19); a certified bound on $\Delta\Theta_z$ beyond RECOG-ALG-CHART-LAWS; the combined $\pm6$ coefficient of $\Lambda_1$ and $P_{W2}$; byte identity with the P2B v2 `certificate.json` (provenance is exact-coefficient and transitive, DYAD-ART-LPHASE-P2B-PROV); any effect on OPEN 20, G2 or physical readings. Resolved since those lists: OPEN 3b (v6.4.15), OPEN 3c (v6.4.16), the primitive-variable remainder (OPEN 21, v6.4.17).

**OPEN 3b — asymptotic-phase transfer (v6.4.15).** Source: P4 proof record v0.1 (§8 DYAD-ART-OPEN3-P4-RECORD), reviewed 19 Oct 2026 as a SESSION record (`P4 SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING`).

`[DEF]` `[v6.4.15]` **Lifted asymptotic phases.** For an orbit $z_m=\widehat F^m(z_0)$ in a row disk, $W_m=h(z_m)$: $\Theta_z(m)=\Theta_z(0)+\sum_{j<m}\operatorname{Arg}(z_{j+1}/z_j)$, $\Theta_W(m)=\Theta_W(0)+\sum_{j<m}\operatorname{Arg}(W_{j+1}/W_j)$ with the tie $\Theta_W(0):=\Theta_z(0)+D_\Theta(z_0)$; $\Psi_z(m)=\Theta_z(m)-\tau\log q_m$ (the $C_z$-track phase of RECOG-THM-R9-MEMORY), $\Psi_W(m)=\Theta_W(m)-\tau\log Q_m$; memories $M=\Psi_\infty-\Psi_z(0)$, $M_W=\Psi_{W,\infty}-\Psi_W(0)$ (independent of the initial lift). Static offset $\Delta_0(z):=D_\Theta(z)-\tau\log(1+D_Q(z)/q)$.

`[ALG]` [RID: DYAD-ALG-OPEN3-PHASE-OFFSET] `[v6.4.15]` `[scope: chart of DYAD-ALG-NF6; row disks; $z=re^{i\Theta}$]` **Exact offset and leading terms.** (P4-0) $\Psi_W(m)-\Psi_z(m)=\Delta_0(z_m)$ for every $m$ (telescoping of $S_\Theta$ as real numbers, and $Q=q+D_Q$). Leading terms:
$$\Delta_1=[\Delta_0]_1=D_{\Theta,1}-\tau D_3/q=r\bigl[\tfrac{17\sqrt3}{36}\cos\Theta-\tfrac1{12}\sin\Theta-\tfrac{7\sqrt3}{72}\cos3\Theta+\tfrac18\sin3\Theta\bigr],$$
$$\Delta_2=[\Delta_0]_2=r^2\bigl[\tfrac{\sqrt3}{108}+\tfrac{\sqrt3}{1296}\cos2\Theta+\tfrac7{432}\sin2\Theta-\tfrac{\sqrt3}{324}\cos4\Theta-\tfrac5{108}\sin4\Theta-\tfrac{\sqrt3}{1728}\cos6\Theta-\tfrac5{576}\sin6\Theta\bigr].$$
$\Delta_1$ has harmonics $\pm1,\pm3$, zero angular mean, and is nonzero (on $\Theta=0$: $\tfrac{3\sqrt3}8r$); $\Delta_2$ has harmonics $0,\pm2,\pm4,\pm6$. *Certificate:* DYAD-ART-OPEN3-P4 (`dyad_open3_p4_exact.py`; two routes — unit-circle Laurent arithmetic and real ray series compared at 60 digits, the latter internal to the same script; six negative controls fail). `[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]` **Primitive-variable form.** With $h^{-1}(W)=W-h_2(W)+O(|W|^3)$: $M_W(W_0)=-\Delta_1(W_0)+Q_0[c_{\rm iso}+\Lambda_1(\Theta_{W_0})]+P_{W2}(W_0)+O(Q_0^{3/2})$ with $P_{W2}=-\Delta_2+D\Delta_1[h_2]=|W|^2\bigl[-\tfrac{5\sqrt3}{27}+\tfrac{47\sqrt3}{1296}\cos2\Theta-\tfrac{19}{432}\sin2\Theta-\tfrac{11\sqrt3}{324}\cos4\Theta+\tfrac1{54}\sin4\Theta-\tfrac{\sqrt3}{1728}\cos6\Theta-\tfrac5{576}\sin6\Theta\bigr]$; hence the $Q_0$-order isotropic coefficient on the raw track is $c_{\rm iso}+\langle P_{W2}\rangle=-\tfrac{\sqrt3}3$ (arithmetic identity; no interpretation claimed). This expansion is formal at second order and is not itself a `[THM]`; its $O(Q_0^{3/2})$ remainder in primitive variables is certified separately by `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (OPEN 21, `[assuming: RECOG-THM-R9-MEMORY]`).

`[THM]` [RID: DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS] `[v6.4.15]` `[proof: analytic majorant + exact-rational certificate]` `[scope: NF-REM rows, not mixed]` **Certified offset bounds.** For $0<|z|\le r$: $|\Delta_0|\le K_0\sqrt q$, $|\Delta_0-\Delta_1|\le K_1q$, $|\Delta_0-\Delta_1-\Delta_2|\le K_2q^{3/2}$,

| $\lvert z\rvert\le$ | $K_0$ | $K_1$ | $K_2$ |
|---|---|---|---|
| $\tfrac1{20}$ | $\tfrac{1101}{1000}$ | $\tfrac{691}{500}$ | $\tfrac{1323}{1000}$ |
| $\tfrac1{40}$ | $\tfrac{533}{500}$ | $\tfrac{1341}{1000}$ | $\tfrac{641}{500}$ |

Majorants of $\operatorname{Im}\operatorname{Log}(1+g)$ and $\log(1+u)$, $g=(h-z)/z$, $u=D_Q/q$, built from the P3 coefficient-modulus data (DYAD-ART-OPEN3-P3) on the principal branch ($|g|<\tfrac1{16}$, $|u|<\tfrac12$ certified); $\tau$ by a rational ceiling; nondecreasing after division by $s^k$, evaluated at $s=r$; $K_0=A_1+K_1r$, $A_1=\tfrac{\sqrt{57}+2\sqrt{219}}{36}$. Constants are majorant suprema. *Certificate:* DYAD-ART-OPEN3-P4 (`dyad_open3_p4_offset_cert.py`; negative controls `neg_tau`, `neg_A1`, `neg_dom` exit 1; reviewer re-execution byte-identical).

`[THM]` `[assuming: hypotheses stated in the entry]` [RID: DYAD-THM-OPEN3-ASYMPTOTIC-PHASE] `[v6.4.15]` `[scope: orbits starting in a row disk; disks forward-invariant by NF-REM]` **Asymptotic-phase transfer.**
- **T1 (limit equality)** `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`: $|\Psi_W(m)-\Psi_z(m)|\le K_0\sqrt{q_m}\le K_0\sqrt{q_0/(1+\tfrac12q_0m)}\to0$; hence, where $\Psi_z(m)\to\Psi_\infty$ (R9, $C_z$ track, its certified rows), $\Psi_{W,\infty}=\Psi_\infty$. Not an independent existence theorem for $\Psi_\infty$. Leading-order rate `[ALG]`: $\Psi_W(m)-\Psi_\infty=\Delta_1(z_m)+O(q_m)$, an $O(m^{-1/2})$ spiral with logarithmically winding angle.
- **T2 (finite-start offset)** `[THM]` `[assuming: T1]`: $M_W-M=-\Delta_0(z_0)$, $|M_W-M+\Delta_1(z_0)|\le K_1q_0$, $|M_W-M|\le K_0\sqrt{q_0}$; the leading $-\Delta_1(z_0)$ is $O(\sqrt{q_0})$, nonzero, and larger than R9's $O(q_0)$ memory — the quantitative reason R9 is not read on the raw track (SG-R14).
- **Chart-variable memory law** `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`: $M_W(z_0)=-\Delta_1(z_0)-\Delta_2(z_0)+q_0[c_{\rm iso}+\Lambda_1(\Theta_0)]+E$, $|E|\le C_2q_0^2+K_2q_0^{3/2}$, with R9's own $C_2$ and $q_0$ windows ($517$, $\tfrac1{400}$; $163$, $\tfrac1{1600}$) on the matching NF-REM row; $z_0=h^{-1}(W_0)$.

`[DEF]` `[v6.4.15]` **Recorded distinctions.** (i) T1 depends on R9's limit and is not a new existence theorem. (ii) The primitive-variable expansion of DYAD-ALG-OPEN3-PHASE-OFFSET is formal at second order; its remainder is certified by DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (OPEN 21), and the chart-variable law by DYAD-THM-OPEN3-ASYMPTOTIC-PHASE. (iii) $M_W$ is the primitive asymptotic-phase memory defined above; no statement is made about the comparator $C_W^{(h)}$. (iv) [NUM] illustration (not a proof input): the P4-0 identity holds along 6 primitive orbits × 4000 blocks to $\le1.5\cdot10^{-40}$; sampled $|\Psi_W-\Psi_z|/\sqrt{q_m}\le0.792$, $|\Delta_0-\Delta_1|/q\le0.075$, $|\Delta_0-\Delta_1-\Delta_2|/q^{3/2}\le0.139$; primitive expansion matches $-P_{W2}$ to $1.4\cdot10^{-13}$.

*`[v6.4.20]` v6.4.15 "Not established" list relocated to Appendix A H-2; the current list is under OPEN 3a above.*

**OPEN 3c, provenance and carried hashes (v6.4.16).** Source: recovered-artifacts SESSION record v0.1.1 (§8 DYAD-ART-OPEN3-P0), reviewed 19 Oct 2026 as a SESSION record.

`[DEF]` `[v6.4.16]` **Provenance of $h$, $J$.** The exact $h$ (DYAD-ALG-NF6, 23 coefficients) and $J$ regenerated in the OPEN 3 certificates (input block of `dyad_open3_p3_remainder_cert.py`) equal, coefficient by coefficient in exact arithmetic, `jets.h_degree6` and `jets.J_through6` of the P2B v2 enclosure `certificate.json` (SHA-256 `d59b0ff68b4341debf5e8a7542bf3865b63dd63e36546952db95298c2bd5c6ce`, inside DYAD-ART-RE-P2B2). Exact coefficient equality only; no file is claimed to be a byte copy of another. Gate: `compare_h_J_with_p2b_v2.py` (exit 0; one-coefficient negative control exits 1); referee DYAD-ART-RE-REFEREE re-executed, ALL PASS; replayed by the reviewer. The v6.4.14 recorded distinction (regeneration does not replace verification against the certificate) is hereby discharged.

`[ENG]` `[v6.4.16]` **Historical fit (P0).** `spiral_phase_fit.py` fits $Q_m\approx C/(m+\kappa)+Am^{-3/2}\cos(\tau\log m+\varphi)$ and $\Delta\Theta\approx-\tau Q+c_\theta Q^2+Bm^{-3/2}\cos(\tau\log m+\varphi_\theta)$ ($C=6$ default; reference $c_\theta^{(6)}=-119\sqrt3/648$). Documented differences from the adopted terms: (D1) one log-harmonic, whereas $D_3$, $[S_Q]_5$ and $L_\Theta$ carry $\cos\Theta,\sin\Theta$ and $\cos3\Theta,\sin3\Theta$, hence $k=1$ and $k=3$ along the orbit; (D2) $C=6$ is a step-index normalization, block-index data have $C=1$ (SG-2); (D3) the $c_\theta$ reference is the archival Lie-gauge object and does not transfer (SG-19); (D4) single-window regression; the $q^2$ lattice harmonic $\pm6$ and the $k=1$ log-period $e^{2\pi/\tau}=e^{\pi\sqrt3}$ make window amplitudes window-dependent (SG-7). The fit is not a definition of $S_Q$, $S_\Theta$; none of its outputs is imported.

`[NUM]` `[v6.4.16]` **Amplitude comparison** (illustration, not a proof input). Leading-order predictions in block index: $Q$ spiral $|A_{k=1}|=\sqrt7/3$, $|A_{k=3}|=1/6$ (the harmonics of $D_3$); phase right-hand side $L_\Theta+\tau D_3$: $\sqrt{7212}/72$, $\sqrt{4836}/144$. On a float64 primitive orbit ($Q_0=2\cdot10^{-3}$, blocks $m\in[40000,52000]$), a two-harmonic least-squares fit gives $0.8714,\ 0.1682$ (predicted $0.8819,\ 0.1667$) and $1.1753,\ 0.4869$ (predicted $1.1795,\ 0.4829$). The historical one-harmonic model gives $c_\theta\approx-395$ with $C=1$ and is meaningless with $C=6$ (`p0_fit_comparison.json`).

`[DEF]` `[v6.4.16]` **Carried v6.4.10 hashes.** Owner-measured SHA-256: `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4`; `check_owner_adoption.py` (inside `DYAD_OWNER_ADOPTION_REVIEW_v1.zip`) `c04096e1cd9ab559d5997c92ad8a442fbf79d350e801e9ed01e6e6a9e19800fe`. Agreement with the reviewer-measured identities of 22 Sep 2026 as reported by the owner; not independently re-measured in the v6.4.16 review.

*`[v6.4.20]` v6.4.16 "Not established" list relocated to Appendix A H-2; the current list is under OPEN 3a above.*

**OPEN 21 — primitive-variable phase remainder (v6.4.17).** Sources: P5 scope note v0.1 and P5 proof record v0.1.2 (§8 DYAD-ART-OPEN21-P5-RECORDS), reviewed 19 Oct 2026 as SESSION records (three rounds; final `P5 v0.1.2 — SCIENTIFIC REVIEW ACCEPTED`).

`[THM]` `[assuming: RECOG-THM-R9-MEMORY]` [RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER] `[v6.4.17]` `[proof: function-level decomposition + analytic majorants + exact-rational certificate]` `[scope: rows A, B of NF-REM, not mixed; primitive start $W_0$]` **Certified primitive-variable phase remainder.** Let $\mathcal P_2(W_0)=-\Delta_1(W_0)+Q_0[c_{\rm iso}+\Lambda_1(\Theta_{W_0})]+P_{W2}(W_0)$, $P_{W2}=-\Delta_2+D\Delta_1[h_2]$, be the adopted second-order form of DYAD-ALG-OPEN3-PHASE-OFFSET, and $M_W$ the primitive asymptotic-phase memory of DYAD-THM-OPEN3-ASYMPTOTIC-PHASE. For $0<|W_0|\le w_j$:
$$|M_W-\mathcal P_2(W_0)|\le K'_jQ_0^{3/2}+C_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2\qquad\text{(primary)},\qquad |M_W-\mathcal P_2(W_0)|\le K_jQ_0^{3/2}\qquad\text{(secondary)},$$

| Row | Chart disk | Primitive domain $w_j$ | $K'_j$ | $C_{2,j}$ (R9) | $C_{2,j}(256/225)^2$ | $K_j$ |
|---|---|---|---|---|---|---|
| A | $\lvert z\rvert\le\tfrac1{20}$ | $\tfrac3{64}$ | $\tfrac{3951}{1000}$ | $517$ | $\tfrac{33882112}{50625}$ | $\tfrac{8831}{250}$ |
| B | $\lvert z\rvert\le\tfrac1{40}$ | $\tfrac3{128}$ | $\tfrac{971}{250}$ | $163$ | $\tfrac{10682368}{50625}$ | $\tfrac{883}{100}$ |

$K'_j$ is the published ceiling of the exact rational majorant ($3.95020\ldots$, $3.88362\ldots$); $K_j$ is the published ceiling of $K'_j+C_{2,j}(256/225)^2w_j$ built from the published $K'_j$. Constants are majorant suprema. *Proof outline* (full text in the record): with $z_0=h^{-1}(W_0)$, the adopted chart-variable memory law defines $E$, $|E|\le C_2q_0^2+K_2q_0^{3/2}$, and the exact identity $M_W-\mathcal P_2=E+T_{\Delta1a}+T_{\Delta1b}+T_{\Delta2}+T_{\rm iso}+T_{\Lambda a}+T_{\Lambda b}$ holds at function level. Domains: $|W_0|\le\tfrac{15}{16}r_j$ gives $|z_0|\le r_j$ (and R9's window), $|z_0-W_0|<|W_0|/15$, segment points $|\xi|\ge\tfrac{14}{15}|W_0|$ (DYAD-THM-NF-INV). Inverse remainder $|z_0-W_0+h_2(W_0)|\le c_{\rm inv}|W_0|^3$ ($c_{\rm inv}^A\le\tfrac{467}{500}$, $c_{\rm inv}^B\le\tfrac{927}{1000}$) from $M(s)$, with $M(s)-\tfrac7{12}s^2$ checked as a majorant of degrees $\ge3$ by certified upper bounds. $\Lambda_1(\Theta)=\tfrac{43\sin6\Theta-5611\sqrt3\cos6\Theta}{1270080}$ and $c_{\rm iso}=-\tfrac{4\sqrt3}{27}$ reproduced exactly from the adopted $\mu,a_{32},a_{05}$; $\|\Lambda_1\|_\infty=\tfrac{\sqrt{481897}}{90720}$, $\|\Lambda_1'\|_\infty=\tfrac{\sqrt{481897}}{15120}$. Each part is nondecreasing in $|W_0|$ by its algebraic structure, so it is evaluated at $w_j$ in exact rational arithmetic. *Certificate:* DYAD-ART-OPEN21-P5 (28 gates; negative controls `neg_dropDh2`, `neg_noTL`, `neg_noC2`, `neg_mix`, `neg_Mdeg3`, `neg_raw`, `neg_Kround` exit 1; reviewer replay byte-identical). On adoption this certifies the $O(Q_0^{3/2})$ remainder that the v6.4.15 entry of DYAD-ALG-OPEN3-PHASE-OFFSET records as `[ALG]` `[scope: formal]`; that entry is kept unchanged as the v6.4.15 record.

`[DEF]` `[v6.4.17]` **Recorded distinctions.** (i) Conditional on RECOG-THM-R9-MEMORY: $M_W$ exists through T1, and the starting chart-variable memory law is conditional on R9. R9 is used at **statement level only** (RECOG v0.3.20 §6.13a–6.14: $\Lambda_1$, $c_{\rm iso}$, $C_2$, rows, $C_z$ observable); RECOG's internal Arb certificate and proof record were not available and are not re-certified. (ii) The R9 term $C_{2,j}(256/225)^2Q_0^2$ is kept separate from the new P5 error $K'_j$; it dominates the single constant $K_j$, especially on row A. (iii) [NUM] illustration (not a proof input): on 64 primitive orbits ($10^6$ blocks each; 4 radii × 8 angles per row) the estimator $\widehat M_W(m)=\Psi_W(m)-\Delta_0(z_m)+q_m[c_{\rm iso}+\Lambda_1(\Theta_z(m))]-\Psi_W(0)$, $|\widehat M_W-M_W|\le C_2q_m^2$, gives $|\widehat M_W-\mathcal P_2|/Q_0^{3/2}\le0.346$, nearly constant over an $8\times$ range of $|W_0|$; all samples within the finite-time bound. This does not prove the absence of higher-order terms. (iv) T1, T2 and the chart-variable memory law keep their adopted grades; no statement on $C_W^{(h)}$.

`[OPEN]` `[v6.4.17]` **Not established:** an unconditional version (independent of R9); sharper $C_2$ (RECOG-owned); optimal $K'_j$ (the `[NUM]` ratio suggests a factor $\approx11$ of slack); the combined $\pm6$ coefficient of $\Lambda_1$ and $P_{W2}$; C_est/κ_est (SG-7); NUMGEN L1/ISP-angle transfer (SG-19); any effect on OPEN 20, G2 or physical readings.

**NUMGEN interface — L-PHASE angular remainder, row A (v6.4.19).** Sources: scope note v0.1, row-A certificate record v0.1, P2B provenance gate records v0.1 and v0.1.1, DYAD reply to NUMGEN, NUMGEN interface confirmation and receipt replay (§8 DYAD-ART-LPHASE-ROWA-RECORDS). Requested by NUMGEN (Requests v0.1 §3, 20 Oct 2026: an explicit certified constant for L-PHASE).

`[DEF]` `[v6.4.19]` **Interface objects** (confirmed by NUMGEN as I1–I5). Frame $W=\mathcal L(\rho,\eta)$ (§1, lifted local $\eta$), $W(Tx)=\lambda W+O(|W|^2)$. One-step angle $\delta_T(y)=\operatorname{Arg}(W(Ty)/W(y))$ (principal value); $\hat\varphi$ is the increasing lift whose one-step increments are $\delta_T$ (NUMGEN's L-MONO lift), $\hat\varphi_{6m}$ taken at the block base point $x_m=F^mx$. Observable $Q_m=Q_{\rm prim}(x_m)=|W(x_m)|^2$ — the primitive quantity, not the chart variable $q=|z|^2$. Block law written $2\pi-\tau Q_m+r_m$ (defect read as a lag). Domain: block base points in $U$, intermediate steps in $U_T$ (DYAD-THM-PRIM-CTR).

`[THM]` [RID: DYAD-THM-LPHASE-ROWA-REMAINDER] `[v6.4.19]` `[proof: exact identity + analytic majorants + exact-rational certificate]` `[scope: block base points in $U$ of DYAD-THM-PRIM-CTR; chart row A ($|z|\le\tfrac1{20}$) of DYAD-THM-NF-REM; primitive observable]` **L-PHASE angular remainder on row A.** Let $x\in U=\{0<Q\le\tfrac1{625}\}$.
- **(B) Branch.** For every $y\in U_T$: $|W(Ty)/(\lambda W(y))-1|\le\varepsilon$ with $\varepsilon\le0.04654$. Hence $W$ does not vanish on $U_T$, $|\delta_T-\pi/3|\le\arcsin\varepsilon<\pi/6$, and the six-step lifted increment equals $2\pi+\operatorname{Arg}(F_W(W)/W)$ (margin $2.86$ rad to the edges of the window $(\pi,3\pi)$).
- **(R) Remainder.** For every $m\ge0$,
$$\hat\varphi_{6(m+1)}-\hat\varphi_{6m}=2\pi-\tau Q_m+r_m,\qquad |r_m|\le\tfrac{403}{250}\,Q_m^{3/2}.$$

*Proof outline* (full text in the certificate record). Block base points stay in $U$ ($F(U)\subset U$) and their chart images $z_m=h^{-1}(W_m)$ lie in $|z|<\tfrac1{20}$ (DYAD-THM-NF-REM tube statement). With $q=|z|^2$ and the OPEN 3 objects of this section, under (B):
$$r=\Lambda_3(z)+[S_\Theta-L_\Theta]+\tau[D_Q-D_3]+[\operatorname{Arg}(J/z)+\tau q]+\operatorname{Arg}(\widehat F/J),\qquad \Lambda_3=L_\Theta+\tau D_3,$$
$$\Lambda_3/r^3=-\tfrac{49\sqrt3}{72}\cos\Theta+\tfrac1{24}\sin\Theta+\tfrac{23\sqrt3}{144}\cos3\Theta-\tfrac{19}{48}\sin3\Theta\qquad(z=re^{i\Theta}).$$
The leading order is checked exactly against the primitive map: $\Im(F_4(W)\bar W)=\Lambda_3(W)|W|^2$ with $F_4$ the raw quartic part and $F_3=\mu|W|^2W$. Row-A bounds: $|\Lambda_3|\le\tfrac{1401}{1000}q^{3/2}$ (certified cell bound $1.400397$); $|S_\Theta-L_\Theta|\le\tfrac{123}{125}q^2$ (DYAD-THM-OPEN3-SPIRAL-REM); $\tau|D_Q-D_3|\le\bar\tau c'_Qq^2$, $c'_Q=0.36915$, from the exact polynomial $D_Q$ of degrees 3–12; $|\operatorname{Arg}(J/z)+\tau q|\le c_Jq^2$, $c_J=0.50220$; $|\operatorname{Arg}(\widehat F/J)|\le c_7q^3$, $c_7=157.58$, from $C_7=100$ (DYAD-THM-NF-REM). With $q^2\le q^{3/2}/20$, $q^3\le q^{3/2}/8000$: $|r|\le1.51632\,q^{3/2}$. Bridge: $|D_Q|\le c_Qq^{3/2}$, $c_Q=0.79246$, so $Q=q+D_Q\ge q(1-c_Q/20)$ and $q^{3/2}\le(1-c_Q/20)^{-3/2}Q^{3/2}$, factor $\le1.06252$. Hence $|r_m|\le1.61112\,Q_m^{3/2}$, published as the ceiling $\tfrac{403}{250}$. Every irrational factor ($\tau$, the bridge factor, $\pi/2$) enters through a proved rational ceiling. *Certificate:* DYAD-ART-LPHASE-ROWA (10 gates G-H, G-L, G-D, P-c, P-L, P-a, P-b, P-7, S-T, FIN; negative controls N1–N6 fail as required; byte-identical JSON on rerun and in NUMGEN's receipt replay).

`[DEF]` `[v6.4.19]` **Recorded distinctions.**
- (i) **Majorant, not optimum.** $403/250$ is a majorant ceiling. `[NUM]` illustration, not a proof input: $\sup_\Theta|r|/Q^{3/2}$ is $1.42849$ on $Q=\tfrac1{625}$ and tends to $\Lambda^*\approx1.4003$ as $Q\to0$. The NUMGEN seed orbit gives $1.35035$, inside NUMGEN's measured range $[1.3449,1.3565]$; this is orbit sampling, not a NUMGEN coefficient correction. NUMGEN's own sampling (receipt record) gives $1.4285$ at $Q=\tfrac1{625}$ and a one-step ratio $0.0319$ at $|W|=0.047$, both below the certified bounds.
- (ii) **SG-19.** The target is the primitive $Q_m$; the chart variable $q$ enters only inside the proof, through the explicit bridge P-a1. No chart coefficient is transferred to NUMGEN L1, to the ISP angle, or to $47/54$, $c_\theta^{(6)}$, $a_1$, $a_2$.
- (iii) **Ownership.** L-PHASE and L1 remain NUMGEN-owned. DYAD supplies a constant and a branch certificate as a separate import. NUMGEN v1.20.8 keeps an `[OPEN]` sub-item without a value; a later NUMGEN edition may import this RID after DYAD adoption.
- (iv) **Chart provenance** (exact coefficient equality, transitive). The certificate regenerates $h$ (23 coefficients), $n$ and $J$ from $T$ (gate G-H). The P2B provenance gate (DYAD-ART-LPHASE-P2B-PROV) shows exact equality with the adopted referee DYAD-ART-RE-REFEREE on its pinned backend and with the archived P0/P1 tables `coordinate_h_deg6_reconstructed.json`, `normalized_onestep_deg6.json` and `normalized_sixstep_deg6.json` (DYAD-ART-RE-P0P1). The convention fixes $h$ and $n$ uniquely through degree 6 (PV1). The link to `jets.h_degree6`/`jets.J_through6` of the P2B v2 `certificate.json` is the v6.4.16 exact-coefficient gate; that file is not compared directly, and no byte identity is claimed. The three sources are not claimed to be fully independent implementations. Gate v0.1.1: owner clean-directory replay ALL PASS, gate JSON byte-identical to v0.1, negative-control exit codes recorded separately; **reviewer full replay pending**.
- (v) **Receipt replay.** NUMGEN's replay reproduced the certificate JSON byte-identically with the same algorithm; it is a receipt, not an independent engine.
- (vi) **Not claimed:** optimality; row B ($|z|\le\tfrac1{40}$; separate); any statement beyond the first-order block law; any change to NUMGEN grades or measured values; the GAP-LOCK angular hypotheses (relation not asserted here); any $\phi^*$ statement (N3 unchanged `[v6.4.20: N3 is now ANSWERED by NUMGEN v1.20.8 §9.1, pin removed, no Dyadic RID; see the §7 notice table]`); any effect on OPEN 20.

`[OPEN]` `[v6.4.19]` **Not established:** row-B constant; optimal constant (the `[NUM]` gap is about 13% at the top of $U$); higher-order block law; reviewer full replay of the P2B provenance gate v0.1.1; direct comparison with the P2B v2 `certificate.json`.

**Consumer results built on this section (v6.4.11 cross-references; owner grades; not rerun by Dyadic).**
- `[ALG]` RECOG-ALG-CHART-LAWS (RECOG v0.3.20 §6.14): $|J|^2=q-q^2+[\tfrac{245}{216}+2\Re(a_{05}e^{-6i\Theta})]q^3+O(q^4)$, $\arg(J/z)=-\tau q+[\tfrac{89\sqrt3}{324}+\Im(a_{05}e^{-6i\Theta})]q^2+O(q^3)$; identities $\tfrac{245}{216}=|\mu|^2+2\Re a_{32}$, $\tfrac{89\sqrt3}{324}=\Im(a_{32}-\mu^2/2)$ rechecked by Dyadic. The chart phase coefficient is opposite in sign to the archival $c_\theta^{(6)}=-\tfrac{119\sqrt3}{648}$ and $\tfrac{245}{216}\ne\tfrac{47}{54}$ — the concrete instances of the SG-19 non-transfer rule.
- `[THM]` RECOG-THM-R9-MEMORY: on the $C_z$ track of this chart, $M(z_0)=q_0[c_{\rm iso}+\Lambda_1(\Theta_0)]+R$, $|R|\le C_2q_0^2$, rows $(517,\tfrac1{400})$ on $|z|\le\tfrac1{20}$ and $(163,\tfrac1{1600})$ on $|z|\le\tfrac1{40}$; $c_{\rm iso}=-\tfrac{4\sqrt3}{27}$; lattice coefficient $G=(1-2i\tau)a_{05}/(1-6i\tau)=-\tfrac{43+5611\sqrt3\,i}{1270080}$, $|G|\approx0.0076520$ (both rechecked by Dyadic). The resonant $(0,5)$ slot whose raw value is obstructed (DYAD-ALG-NF6-OBS) is the carrier of this comparator-invisible asymptotic phase. **Scope:** the $C_z$ observable and its certified small-$q_0$ windows; no physical event-to-memory inheritance and no transfer to the $C_W^{(h)}$ track.
- RECOG v0.3.20 §6.14 / RRF v0.8 §2.3: the transported involution $S_h=h_6\circ(-I)\circ h_6^{-1}$ (exact involution; $\mathcal J_{\le6}$ commutation only) is owned and registered there; Dyadic does not re-register it.

`[OPEN]` **Not established by this section (owner-recorded boundaries):** RECOG R8 validated saddle-manifold entry into a certified attracting region (the sampled 12-step entry into $Q<0.3$ is not an entry certificate for $Q\le\tfrac1{400}$); RECOG R9 two-history retained-memory comparison (one-orbit summability is an input, not the theorem); R10 acceptance and R11 final-chart ledger (amplitude, angle, comparator, backbone, phase coefficient all in *this* chart; per SG-19 none of $c_\theta$, $a_1$, $a_2$, or a long-orbit backbone is transferred by this section). `[v6.4.11 status note]` These four were **not** obtained by this section, and remain outside Dyadic custody; they have since been closed **in the consumer** at RECOG's grades — R8 (RECOG-THM-P2-HET), R9 (RECOG-THM-R9-MEMORY), R10 delivered/accepted, R11 chart ledger (RECOG v0.3.20; see the cross-references above and §7). Dyadic has not rerun those certificates. Still not established anywhere: historical $\Phi_1$ output byte identity; optimal radii/constants; higher-derivative bounds. `[v6.4.20: GAP-LOCK pointer. GAP-LOCK Lemmas 1-3 are CLOSED [ALG] in NUMGEN v1.20.8 §6.6 at NUMGEN grades; this ledger neither restates nor regrades them. DYAD supplies only the explicit row-A constant of DYAD-THM-LPHASE-ROWA-REMAINDER, whose import NUMGEN defers (§7 L-PHASE interface)]` No geometry, source-amplitude, cascade, or generator-selection consequence follows from this section alone (SG-13, SG-14, SG-15). `[HEUR]` Further constant sharpening is deferred until a specific downstream error budget shows it is needed.

### §6.15 Local Involutions Commuting with the Return — entry grades: THM, DEF {#sec-6-15-involution}

> **[SG-14 applies]** **[SG-15 applies]** Pure mathematics about the selected $T$. Nothing here establishes a physical pole or node exchange, the meaning of an edge exchange $\sigma$, or any factor contract $EF=TE$ / $EF=T^6E$ (RRF G2: CONTRACT READY / PHYSICAL REALIZATION OPEN; RRF OPEN-A; OFN OPEN-OPA).

**Provenance.** Part (a): G2-FIX argument from the RRF/OFN review stream, audited here. Part (b): Dyadic-owner strengthening (16 Oct 2026), accepted by the external mathematical review of the same date (`ACCEPT SCOPED`). No numerical work.

`[DEF]` **Domain convention (G2-DOM form).** Let $V$ be an open neighbourhood of $0$ in the **lifted** $(\rho,\eta)$-plane and $R:V\to V$ a $C^k$ map with $R\circ R=\mathrm{id}_V$. Let $\Phi\in\{T,\,F=T^6\}$ and $V_\Phi:=V\cap\Phi^{-1}(V)$ (an open neighbourhood of $0$, since $\Phi(0)=0$). "$R$ commutes with $\Phi$" means $R\circ\Phi=\Phi\circ R$ on $D_\Phi:=V_\Phi\cap R^{-1}(V_\Phi)$, and it is **required** that
$$0\in\operatorname{int}D_\Phi .$$
This does not presuppose $R(0)=0$; it only guarantees that both compositions are defined, and equal, on a neighbourhood of $0$, so that the identity may be evaluated and differentiated at $0$. `[COR r3, R2-01]` r2 omitted this requirement. All statements are about germs at $0$.

`[THM]` [RID: DYAD-THM-LOCAL-INVOLUTION-GERM] `[proof: elementary; conditional on the stated domain/regularity hypotheses; scope: selected $T$]`

**(a) Primitive clock.** If $k\ge1$, $R$ commutes with $T$, and $V\subset\{|\eta|<\pi\}$, then $R(0)=0$ and $DR(0)\in\{I,-I\}$.

**(b) Six-step clock.** If $k\ge3$, $R$ commutes with $F=T^6$, and $V\subset U_T\cup\{0\}$ with $U_T$ the six-phase tube of DYAD-THM-PRIM-CTR, then $R(0)=0$ and $DR(0)\in\{I,-I\}$.

**(c) Dichotomy.** In either case, $DR(0)=I$ implies $R=\mathrm{id}$ on a neighbourhood of $0$. Hence $R$ is not the identity germ $\iff DR(0)=-I$; and then $\Psi:=\tfrac12(\mathrm{id}-R)$ is a local $C^k$ diffeomorphism with $\Psi\circ R=-\Psi$, i.e. $R$ is locally $C^k$-conjugate to $-I$ (Bochner).

*Proof.* Fixed point: since $0\in D_\Phi$, $\Phi(R(0))=R(\Phi(0))=R(0)$. (a) Fixed points of the lifted $T$ are $\sin\eta=0$, $e^\rho=1$, i.e. $(0,k\pi)$; only $0$ lies in $\{|\eta|<\pi\}$. (On the wrapped cylinder there are further fixed points $(\log(1+2\pi k),0)$, $(\log(1+2\pi k),\pi)$; the lifted-chart hypothesis excludes them.) (b) Fixed points of $F$ are $T$-periodic points of period dividing 6; by DYAD-THM-PRIM-CTR there is no nonzero periodic orbit in $U_T$. In both cases $R(0)=0$. Let $L=DR(0)$, so $L^2=I$.
(a) Differentiating $RT=TR$ at $0$: $LA=AL$, $A=DT(0)$. The eigenvalues $e^{\pm i\pi/3}$ are non-real, so the real commutant of $A$ is $\mathrm{span}\{I,A\}\cong\mathbb C$; its only square roots of $1$ are $\pm I$.
(b) In the raw linear frame $W=\mathcal L(\rho,\eta)$, $F(W)=W+G_3(W)+O(|W|^4)$ with $G_3(W)=\mu|W|^2W$ and no quadratic term (§6.7, DYAD-THM-C21). Write $R(W)=LW+R_2(W)+R_3(W)+o(|W|^3)$, the third-order Taylor expansion of a $C^3$ map (`[COR r3, R2-02]`: r2 wrote $O(4)$, which a general $C^3$ map does not guarantee). Since $F=\mathrm{id}+G_3+O(|W|^4)$ with $F$ analytic, $R\circ F=LW+R_2(W)+R_3(W)+LG_3(W)+o(|W|^3)$ and $F\circ R=LW+R_2(W)+R_3(W)+G_3(LW)+o(|W|^3)$ ($R_2$ evaluated at $W+G_3+\dots$ differs from $R_2(W)$ by $O(|W|^4)$, and $G_3(R(W))-G_3(LW)=O(|W|^4)$). Comparing the homogeneous cubic parts, which are determined uniquely modulo $o(|W|^3)$, gives $L\,G_3(W)=G_3(LW)$. If $L\ne\pm I$, $L$ is a (possibly oblique) reflection, so $LW_0=W_0$ for some $W_0\ne0$; then $L(\mu W_0)=\mu W_0$, so $\mu W_0$ lies in the $+1$ eigenline $\mathbb RW_0$. But $\Im\mu=-\tfrac{2\sqrt3}{3}\ne0$, so multiplication by $\mu$ has no real invariant line — contradiction. Thus $L=\pm I$. (The $O(|W|^4)$ remainder comes from the analyticity of $F$ and needs no fourth derivative of $R$.)
(c) For $L=I$: $\Theta:=\tfrac12(\mathrm{id}+R)$ has $D\Theta(0)=I$ and $\Theta\circ R=\Theta$; $\Theta$ is injective near $0$ (inverse function theorem) and $R(x)\to0$ as $x\to0$, so $R(x)=x$ near $0$. For $L=-I$: $D\Psi(0)=I$ and $\Psi\circ R=-\Psi$ directly. $\square$

`[DEF]` **Reading.** The selectivity lost by the six-step linearization ($DT^6(0)=I$) is restored at cubic order by the chiral (phase-shear) part $\Im\mu$ of the return. If the return were radially symmetric to cubic order with real $\mu$, reflections would survive the cubic test. Both clocks give the same germ dichotomy, but $EF=TE$ and $EF=T^6E$ remain different factor contracts; this lemma does not make them equivalent.

`[DEF]` **Relation to $S_h$.** RECOG/RRF's $S_h=h_6\circ(-I)\circ h_6^{-1}$ has $DS_h(0)=-I$ but commutes with $f$ only through degree 6; it is **not** an exact commuting involution and the lemma does not apply to it as such. The formal $\widehat S=\widehat h(-I)\widehat h^{-1}$ commutes formally. `[v6.4.12]` The identity $\widehat S=R_0$ (§6.16) holds in the formal category only; $S_h$ remains a finite chart object (equal to $R_0$ through degree 6) and is not upgraded by the closure of OPEN 19.

`[v6.4.12]` **Formal uniqueness (now proved, separate RID).** DYAD-THM-LOCAL-INVOLUTION-GERM is unchanged. The jet identification is proved in §6.16 (DYAD-THM-FORMAL-INVOLUTION-UNIQUE): for $C^\infty$ or analytic $R$ in the nontrivial branch of (a) or (b), $j^\infty R=R_0=\widehat S$. Both clocks select the same formal involution. (v6.4.11 recorded this as a conditional reduction under OPEN 19.) Any $C^r$ ($4\le r<\infty$) transfer conditional on RRF/G1 lemmas (L-SHADOW-POLY) is not registered here.

`[THM]` `[scope: analytic]` [RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE] `[v6.4.12 r1]` `[depends: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]` `[scope: selected $T$, local germs]` **Analytic versus smooth commutation (Corollary A).** Let $R$ be a real-analytic local involution with $R(0)=0$ that commutes with $F=T^6$ in the sense of the domain convention above, and let $DR(0)=-I$. (Under the hypotheses of (b), $R(0)=0$ is automatic and every non-identity germ has $DR(0)=-I$.) Then $RT=TR$ exactly on a neighbourhood of $0$.

*Proof.* $j^\infty R$ is a formal involution commuting with $F$ with linear part $-I$, so $j^\infty R=R_0$ (§6.16). $R_0$ commutes with $T$ formally, so the Taylor series of $RT-TR$ is $R_0T-TR_0=0$. Since $T(0)=R(0)=0$, both compositions are defined and real-analytic on a connected neighbourhood of $0$; an analytic map with vanishing Taylor series vanishes there. $\square$

- If $R_0$ diverges (negative answer to OPEN 20 (B-an)), no analytic non-identity involution commutes with $T^6$ under the hypotheses of (b).
- For $C^\infty$ $R$, the argument of this section gives only $j^\infty(RT-TR)=0$; exact primitive-clock commutation is F1 (§6.17) and existence is DYAD-THM-SMOOTH-EMBEDDING (§6.17). `[v6.4.20]` (v6.4.12/v6.4.13 wording: Appendix A H-9.)
- This does not identify the distinct factor contracts $EF=TE$ and $EF=T^6E$, and it does not establish the existence of an analytic or $C^\infty$ involution.

*Provenance.* Proposed by the RRF sync review v0.2 ("analytic clock bridge"); endorsed by the external reviewer (16 Oct 2026); proof written and checked by the Dyadic owner.

`[DEF]` **Failure-mode bookkeeping (for RRF/OFN, not a Dyadic claim).** Failure of $EF=TE$, of fibre compatibility, local triviality $R=\mathrm{id}$, or regularity/jet compatibility each diagnoses a different contract defect; none alone proves physical node exchange impossible.

### §6.16 Formal Centralizer of the Six-Step Return — entry grades: ALG, THM, DEF, OPEN {#sec-6-16-centralizer}

> **[SG-14 applies]** **[SG-15 applies]** Formal mathematics about the selected $T$. Nothing here establishes convergence, an analytic or smooth involution, a physical exchange, or any factor contract.

**Provenance.** Dyadic-owner proof (16 Oct 2026), recorded in `DYAD_OPEN19_FORMAL_CENTRALIZER_PROOF_SESSION.md` v1.2. External review of v1.0 and v1.1: ACCEPT. RRF sync review v0.2: `ACCEPT SCOPED`, with the $a=0$ boundary correction applied below (Steps 2–3).

`[DEF]` **Setting.** $F=T^6$ in the raw linear frame $W=\mathcal L(\rho,\eta)$; $F=\mathrm{id}+G_3+O(|W|^4)$ with $G_3=\mu|W|^2W$, $\mu=-\tfrac12-\tfrac{2i\sqrt3}{3}$, no quadratic term (DYAD-THM-C21, §6.7). Real formal vector fields with vanishing 1-jet are written by their complex component $V(z,\bar z)$; $\mathfrak X_k$ denotes the homogeneous fields of degree $k$. $X:=\log F=X_3+X_4+\cdots$ (formal), with $X_3$ of component $V_3=\mu z^2\bar z$.

`[ALG]` [RID: DYAD-ALG-CENT-KERNEL] `[v6.4.12 r1]` **Lemma K (homogeneous kernel).** For every $k\ge2$,
$$\ker(\operatorname{ad}_{X_3})\cap\mathfrak X_k=\mathbb R\,X_3\ (k=3),\qquad =0\ (k\ne3).$$
Only $\Re\mu\ne0$ and $\Im\mu\ne0$ are used.

*Proof.*
1. *Bracket on a monomial.* For $B=c\,z^a\bar z^b$, $a+b=k$: $[X_3,B]=c\,\alpha_{a,b}\,z^{a+1}\bar z^{b+1}-\mu\,\bar c\,z^{b+2}\bar z^{a}$, with $\alpha_{a,b}=(a-2)\mu+b\bar\mu$.
2. *Coefficient equations.* The output $z^{a+1}\bar z^{b+1}$ receives the first term from $(a,b)$ and the second from $\phi(a,b)=(b+1,a-1)$ when $a\ge1$. For $a=0$ the partner $(b+1,-1)$ does not exist. The second term of the input $(0,b)$ lands on the $\bar z$-free monomial $(b+2,0)$, which receives nothing else. Hence $[X_3,Y]=0$ for $Y=\sum c_{a,b}z^a\bar z^b$ iff
$$c_{a,b}\alpha_{a,b}=\mu\,\bar c_{\phi(a,b)}\ (a\ge1),\qquad c_{0,b}\alpha_{0,b}=0,\qquad \mu\,\bar c_{0,b}=0 .$$
Outputs $(0,q)$ receive nothing. $\phi$ is an involution on $\{a\ge1\}$ with fixed points $a=b+1$.
3. *Boundary $a=0$.* $\mu\ne0$ gives $c_{0,b}=0$; this removes $(0,2)$ at $k=2$. `[COR r1]` The proof record v1.1 stated that $(p,0)$ outputs give no further condition and used the factor $b\bar\mu-2\mu$ instead. The conclusion was right; the bookkeeping is corrected here (RRF sync review v0.2).
4. *Two-element orbits* ($a\ge1$, $\phi(a,b)\ne(a,b)$). With $c_1=c_{a,b}$, $c_2=c_{\phi(a,b)}$, $\alpha_2=(b-1)\mu+(a-1)\bar\mu$: $c_1\alpha_1=\mu\bar c_2$, $c_2\alpha_2=\mu\bar c_1$. If $\alpha_2=0$ then $c_1=c_2=0$. Otherwise $c_1(\alpha_1\bar\alpha_2-|\mu|^2)=0$. The imaginary part of the factor is $\Im(\mu^2)[(a-2)(a-1)-b(b-1)]$ with $\Im(\mu^2)=2\Re\mu\Im\mu\ne0$. It vanishes only for $b=a-1$ (a fixed point, excluded) or $b=2-a$ ($k=2$); the only two-element orbit left at $k=2$ is $(1,1)\leftrightarrow(2,0)$, where the real part equals $-|\mu|^2\ne0$. So $c_1=c_2=0$.
5. *Fixed points* $(a,a-1)$, $k=2a-1$. The equation is $c\alpha=\mu\bar c$ with $\alpha=(a-2)\mu+(a-1)\bar\mu$, and $|\alpha|^2-|\mu|^2=(a-1)(a-2)\cdot4(\Re\mu)^2$. A nonzero $c$ forces $a\in\{1,2\}$. $a=1$ is linear (excluded); $a=2$ gives $k=3$, $\alpha=\bar\mu$, and $c\bar\mu=\mu\bar c$ means $c\in\mathbb R\mu$, i.e. $Y\in\mathbb RX_3$. $\square$

`[THM]` [RID: DYAD-THM-FORMAL-CENTRALIZER] `[v6.4.12 r1]` `[scope: formal category, real coefficients]` **Theorem C.** $\operatorname{Cent}_{{\rm formal},\,DG(0)=I}(F)=\{\exp(sX):s\in\mathbb R\}$.

*Proof.* Tangent-to-identity formal maps form a pro-unipotent group, so $G=\exp Y$. If $G$ commutes with $F=\exp X$ then $e^{\operatorname{ad}X}Y=Y$; since $(e^{\operatorname{ad}X}-1)=\operatorname{ad}X\cdot\psi(\operatorname{ad}X)$ with $\psi$ invertible, $[X,Y]=0$. The lowest term $Y_k$ satisfies $[X_3,Y_k]=0$, so by Lemma K $k=3$ and $Y_3=sX_3$. Then $Y-sX$ commutes with $X$ and starts above degree 3, so it vanishes by Lemma K. $\square$

`[THM]` [RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE] `[v6.4.12 r1]` `[scope: formal category]` **Corollary U.** Let $R_0:=T^3\circ F^{-1/2}=T^3\circ\exp(-\tfrac12X)$.
- (i) $R_0$ is a formal involution with $DR_0(0)=-I$ that commutes with $T$, hence with $F$.
- (ii) Every formal involution $\widehat R$ commuting with $F$ with $D\widehat R(0)=-I$ equals $R_0$.

*Proof.* (i) $T$ commutes with $F$, so $\mathrm{Ad}_TX=X$ and $T^3$ commutes with every $\exp(sX)$. Then $R_0^2=T^6\exp(-X)=\mathrm{id}$ and $DR_0(0)=A^3=-I$. (ii) $C=\widehat RR_0$ is tangent to the identity and commutes with $F$, so $C=\exp(sX)$ by Theorem C. Since $R_0$ commutes with $X$, $\widehat R^2=C^2R_0^2=\exp(2sX)=\mathrm{id}$, so $s=0$. $\square$

No normalizer is used. `[ALG]` **Identification.** For any formal Poincaré–Dulac normalizer $\widehat h$ with $\lambda$-equivariant normal form, $\widehat S=\widehat h(-I)\widehat h^{-1}$ satisfies (ii) because $-I=\lambda^3$; hence $\widehat S=R_0$. In normal-form coordinates the centralizer $\{\exp(s\widehat X)\}$ consists of $\lambda$-equivariant maps, which answers OPEN 19 as registered. $\widehat S=R_0$ is a formal identity only; see §6.15 on $S_h$.

`[ALG]` **Problem B reduction** (OPEN 20). $T^3$ is analytic and invertible near $0$ and $F^{1/2}=R_0T^3$. So $R_0$ converges iff the tangent-to-identity formal square root $F^{1/2}$ of the six-step return converges. ($T^3=R_0\circ F^{1/2}$ factors the analytic square root of $F$ with linear part $-I$.) Existence of a formal root does not imply convergence; the question is not answered here.

`[THM]` [RID: DYAD-THM-FORMAL-Z6-GENERATOR] `[v6.4.13]` `[scope: formal category]` **Canonical ℤ₆ generator.** Let $J:=T\circ\exp(-\tfrac16X)=T\circ F^{-1/6}$. Then $J^6=\mathrm{id}$, $JT=TJ$, $DJ(0)=A$, $R_0=J^3$ and $G:=J^2=T^2F^{-1/3}$. $J$ is the unique formal map commuting with $F$ with linear part $A$ and $J^6=\mathrm{id}$; likewise $G$ (order 3, linear part $A^2$).

*Proof.* $T$ commutes with $X$, so $J^6=T^6\exp(-X)=\mathrm{id}$ and $J$ commutes with $T$. If $J'$ has the stated properties, $J'J^{-1}$ is tangent to the identity and commutes with $F$, so $J'=\exp(sX)J$ (Theorem C); $J$ commutes with $X$, so $\mathrm{id}=J'^6=\exp(6sX)$ and $s=0$. The same argument applies to $G$. $\square$ (No use of the full centralizer of $T$ is needed; cf. FMS v0.5.1 R3, SESSION.)

`[ALG]` `[v6.4.13]` **Analytic realization hierarchy** (OPEN 20). Let $K:=F^{1/6}=\exp(\tfrac16X)$. (a) $K$ converges ⟺ $J=TK^{-1}$ converges ⟺ an analytic chart exists in which $T$ commutes exactly with $A$: given analytic $J$, $\Phi=\tfrac16\sum_{k=0}^5A^{-k}J^k$ satisfies $D\Phi(0)=I$, $\Phi J=A\Phi$, so $\Phi T\Phi^{-1}$ commutes with $A$; conversely, in such a chart $A^{-1}T'$ is an analytic tangent-to-identity sixth root. (b) $K$ converges ⟺ $F^{1/2}$ and $F^{1/3}$ converge: $F^{1/2}=K^3$, $F^{1/3}=K^2$, and $K=F^{1/2}\circ F^{-1/3}$, with exact commutation by the identity theorem. Hence B-6 ⇒ B-an. The admissible exactly-equivariant charts are $\{\psi\circ\Phi:\psi A=A\psi\}$.

**Finite reproductions** `[ALG]` `[scope: finite checks; not certificates of the all-order statements]`:
- `dyad_open19_kernel_check.py` (DYAD-ART-OPEN19-KERNEL): real Jacobian brackets, exact sympy, $k=2,\dots,13$; kernel dimensions $0,1,0,\dots,0$, the $k=3$ field parallel to $X_3$; exit-gated.
- `dyad_open19_a0_boundary_check.py` (DYAD-ART-OPEN19-KERNEL): the Step 2–3 boundary structure for $b=0,\dots,7$; exit-gated, negative control exits 1.
- `dyad_open19_R0_identity_cert.py` (DYAD-ART-OPEN19-R0CERT): 3 truncations ($N=6,8,12$) × 7 assertions — $R_0^2=\mathrm{id}$, $R_0f=fR_0$, $R_0F=FR_0$, $DR_0(0)=-I$, $f\circ h=h\circ n$, $\mathcal J_{\le N}(h(-I)h^{-1})=\mathcal J_{\le N}R_0$, $[R_0]_2=2h_2$; all PASS; negative control (root factor $\tfrac13$) exits 1. At $N=6$ it reproduces RECOG/RRF's $S_6$. It shares the engine of DYAD-ART-RE-REFEREE and is not an independent third implementation.
- Cross-check reference `[reviewer-reported; not owner-inspected]`: `cent.py` (SHA-256 prefix `c6189068`, suffix `4624`; complex-component method) reports kernel dimensions $0,1,0,\dots,0$ for $k=2,\dots,13$. Computational support only.

`[OPEN]` **Not established by this section:** convergence of $R_0$ and analytic or $C^\infty$ existence of a non-identity commuting involution (OPEN 20); exact commutation of a $C^\infty$ six-step involution with $T$; physical exchange or G2 realization (SG-14/15, RRF OPEN-A, OFN OPEN-OPA); equivalence of $EF=TE$ and $EF=T^6E$.

### §6.17 Flat Centralizer Triviality — entry grades: THM, DEF, OPEN, NUM {#sec-6-17-flat}

> **[SG-14 applies]** **[SG-15 applies]** Local mathematics about the selected $T$ near $P_1$. Status: **adopted 18 Oct 2026** after two external review rounds (r1: ACCEPT with R1–R2; r2: ACCEPT — ADOPTION READY). Proof record: `DYAD_LEMMA_F_FLAT_CENTRALIZER_PROOF_RECORD_v0_3.md` (SHA-256 `2e6c5c59a1fdfe6baa1702df8873b0d89664796d4f317313f239969b406a8ece`; reviewed predecessor v0.2 `0a2ae5e2…4dfb`; v0.3 changes only the construction-route sentence, review R1). The RIDs below retain the word `CAND` from the draft stage; per DSN v1.3 a RID is a fixed identifier and carries no status.

`[THM]` [RID: DYAD-CAND-FLAT-CENTRALIZER] `[v6.4.13]` `[proof: elementary; uses DYAD-THM-PRIM-CTR only; scope: stated ball and flat-contact hypothesis]` **Lemma F.** Raw frame $W$, $Q=|W|^2$, $B_s=\{Q\le s\}$. Fix $s_0\in(0,\tfrac1{400}]$ and $K$ with $\|DF(W)-I\|\le KQ(W)$ on $B_{s_0}$; choose $r$ with $4r\le s_0$, $4rK\le\tfrac12$, $B:=B_{4r}$. If $C:B_r\to B$ is any map with $C\circ F=F\circ C$ on $B_r$ and $|C(W)-W|\le c_N|W|^N$ for every $N$, then $C=\mathrm{id}$ on $B_r$.

*Proof sketch* (full text in the proof record). By DYAD-THM-PRIM-CTR, $B_r$ and $B$ are forward-invariant and orbits obey $Q(F^kz)\le\min(4r,2/k)$. For $a=C(x)$, $b=x$, convexity of $Q$ and the mean-value inequality give $|F^na-F^nb|\ge c_0n^{-4K}|a-b|$, while commutation and flatness give $|F^na-F^nb|=|C(F^nx)-F^nx|\le c_N(2/n)^{N/2}$. Take $N>8K$, $n\to\infty$. $\square$ Only the radial contraction ($\Re\mu<0$) is used; no regularity of $C$ is assumed.

`[THM]` `[assuming: hypotheses stated in the entry]` [RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES] `[v6.4.13]` `[conditional on: Lemma F; and on the existence of the $C^\infty$ involution or root concerned — no existence is asserted]` For $C^\infty$ maps, flatness follows from jets (Taylor's theorem and the chain rule); this is the only use of $C^\infty$.
- **F1 ($C^\infty$ clock bridge).** A $C^\infty$ local involution $R$ with $R(0)=0$, $RF=FR$ (§6.15 domain convention), $DR(0)=-I$ satisfies $RT=TR$ near $0$. ($C=TRT^{-1}R$ has jet $TR_0T^{-1}R_0=\mathrm{id}$.)
- **F2 ($C^\infty$ uniqueness).** Two such involutions coincide near $0$.
- **F3 (smooth roots).** A $C^\infty$ tangent-to-identity $K$ with $K^m=F$ commutes with $T$ and is unique. Hence in $C^\infty$: $F^{1/6}$ exists ⟺ $J$ exists ⟺ an exactly $\lambda$-equivariant $C^\infty$ chart exists, without a separate commutation hypothesis; likewise $F^{1/2}$ ⟺ $R_0$.

*`[v6.4.20]` v6.4.17 "Not established" list relocated to Appendix A H-3; the current list is the v6.4.18 one below. The proposed route $F^{-n}R_\infty F^n$ remains unproved (Recorded distinctions (ii)).*

**OPEN 20 B-∞ existence — smooth flow embedding (v6.4.18).** Sources: the O20-∞ SESSION records (§8 DYAD-ART-OPEN20-BINF-RECORDS), reviewed 19–20 Oct 2026 (P2-b v0.2.1, P3-a v0.1 and P3-b/c v0.1 accepted; integration audit v0.1 accepted with the E2 scope correction applied in v0.1.1). Requested by FMS (OPEN 20 priority, `DYAD_REPLY_TO_FMS_OPEN20_PRIORITY_v0_1.md`).

`[THM]` [RID: DYAD-THM-SMOOTH-EMBEDDING] `[v6.4.18]` `[proof: Borel realization + flat conjugacy by inverse iteration + polynomial derivative bounds + Lemma F/F2/F3; scope: $C^\infty$ local germs at $P_1$, raw frame $W$, lifted chart]` **Smooth flow embedding of the six-step return.** Let $\widehat X=\log F$ be the formal generator of §6.16. (E1) There are a ball $U^*=B(0,r'')$ and a $C^\infty$ vector field $X$ near $0$ with $j^\infty_0X=\widehat X$ and $F=\varphi^1_X$ on $U^*$. (E2) If $X'$ is a $C^\infty$ field with $\varphi^1_{X'}=F$ near $0$ and $DX'(0)=0$, then $X'=X$ as germs; in particular $X$ does not depend on the Borel realization used. (E3) For every $m\ge1$, $K_m:=\varphi_X^{1/m}$ is a $C^\infty$ tangent-to-identity germ with $K_m^m=F$; it commutes with $T$ and is the unique such root (F3). (E4) $J:=T\circ K_6^{-1}$ satisfies $J^6=\mathrm{id}$, $DJ(0)=A$, $JT=TJ$; $R:=T^3\circ K_2^{-1}$ is a $C^\infty$ local involution with $DR(0)=-I$, $RT=TR$, unique by F2, and satisfies the §6.15 domain convention with $V=B\cap R^{-1}(B)$.

*Proof outline* (full text in the records). (i) $X_\infty$: a $C^\infty$ Borel realization of $\widehat X$; $G_\infty:=\varphi^1_{X_\infty}$ has $j^\infty G_\infty=j^\infty F$ (jet ODE on finite-dimensional jet spaces). (ii) On $\bar B(0,3\rho)$, $F$ and $G_\infty$ are local diffeomorphisms with $\|DH-I\|\le c_1|w|^2$ and $Q(Hw)\le Q-\tfrac12Q^2$ (common cubic term $\mu|W|^2W$, $\operatorname{Re}\mu=-\tfrac12$; DYAD-THM-PRIM-CTR for $F$), and $F-G_\infty$ is flat. (iii) P2-b: for $N_0>2\gamma+4$, $\gamma=2c_1/a$, the inverse-branch iterates $p_n=\Gamma_n\circ F^n$, $\Gamma_n=(G_\infty^n|_{B(0,3\rho)})^{-1}$, are defined on a fixed ball $B(0,\rho_1)$ and converge uniformly to $\Phi_\infty$ with $\Phi_\infty F=G_\infty\Phi_\infty$; by the symmetric construction and Lemma F (re-proved for $G_\infty$ from its own hypotheses) $\Phi_\infty$ is a local homeomorphism. (iv) P3-a: $\|D^\ell H^n\|\le C_\ell(1+n)^{A_\ell}$, $\|D^\ell\Gamma_m\|\le\bar C_\ell(1+m)^{B_\ell}$, $\|D^\ell p_n\|\le\hat C_\ell(1+n)^{P_\ell}$, uniform in the base point, with $A_\ell=(2\alpha+1)(\ell-1)+\alpha$, $B_\ell=(7\alpha+1)(\ell-1)+2\alpha$, $P_\ell=(7\alpha+1)(\ell-1)+(\ell+2)\alpha$, $\alpha=c_1/a$. A uniform form $(1+nQ)^{A}$ is impossible for $\ell=3$: $j^3F^n=\mathrm{id}+nP_3$. (v) P3-b/c: $\|D^j(F-G_\infty)(w)\|\le C_{N,j}|w|^N$ for all $N,j$; $d_n=p_{n+1}-p_n=\int_0^1D\Gamma_{n+1}(z_t)[(F-G_\infty)(F^nx)]\,dt$ with one flat factor per Leibniz term gives $\|D^\ell d_n\|\le M_{N,\ell}(1+n)^{E_\ell}|F^nx|^N$, $E_\ell=(8\alpha+1)\ell+2\alpha$; with the integer $N_k=\lceil2E_k+3\rceil$, $\sum_n\|d_n\|_{C^k(B(0,\rho_1))}<\infty$ for every $k$ on the same ball. So $\Phi_\infty\in C^\infty$, $\Phi_\infty-\mathrm{id}$ flat. (vi) Inverse function theorem, a Grönwall flow ball for $X_\infty$ and a forward-invariant common ball $U^*$ give $F=\varphi^1_X$, $X=\Phi_\infty^*X_\infty$. (vii) E2: the jet of $X'$ equals $\widehat X$ (needs $DX'(0)=0$); $C_t=\varphi_X^{-t}\varphi_{X'}^t$ commutes with $F$, is flat-close to the identity and maps $B_r\to B_{4r}$ for all $t\in[0,1]$, so Lemma F gives $C_t=\mathrm{id}$. (viii) E3–E4: F3, with its existence condition discharged by E1; F2; §6.15 convention checked in the audit. *Checks* (DYAD-ART-OPEN20-BINF-CHECKS): exact 3-jet of $T^6$ ($j^3F^n=\mathrm{id}+nP_3$, $DQ\cdot P_3=-Q^2$, cubic part $=\mu|W|^2W$), $A^6=I$, $A^3=-I$, exponent recursions, input pins; negative controls fail as required. The checks do not replace the all-orders arguments.

`[DEF]` `[v6.4.18]` **Recorded distinctions.** (i) **Notation:** $G_\infty$ denotes the Borel time-one map; it is unrelated to $G=J^2$ of §6.16. (ii) **Route:** the proof uses $G_\infty^{-n}F^n$; the §6.17 route $F^{-n}R_\infty F^n$ is a different sequence and remains unproved. (iii) **E2 scope:** uniqueness is claimed only among generators with $DX'(0)=0$; $\exp(DX'(0))=I$ does not force $DX'(0)=0$ in general. (iv) **F1–F3:** grades unchanged (`[THM]` `[assuming: hypotheses stated in the entry]`); their existence condition is discharged for the roots $K_m$, $J$ and $R$ by E1. (v) **Radius:** $r''$ is qualitative; no numerical radius and no finite-$C^k$ constant is claimed. (vi) $C^\infty$ existence says nothing about analyticity: B-an and B-6 are untouched. (vii) SG-14/15: no physical exchange, G2 realization or $EF=TE$/$EF=T^6E$ identification follows.

`[THM]` [RID: DYAD-THM-SMOOTH-EQUIVARIANT-CHART] `[v6.4.20; RID registered at adoption, 21 Oct 2026]` `[corollary of DYAD-THM-SMOOTH-EMBEDDING E3–E4; proof: finite-group averaging]` **Smooth equivariant chart.** Let $J$ be the $C^\infty$ germ of E4 ($J^6=\mathrm{id}$, $DJ(0)=A$, $JT=TJ$) and $\Phi:=\tfrac16\sum_{k=0}^{5}A^{-k}J^k$. Then $\Phi$ is a $C^\infty$ local diffeomorphism with $\Phi(0)=0$, $D\Phi(0)=I$, $\Phi\circ J=A\circ\Phi$, and $N_\Phi:=\Phi T\Phi^{-1}$ commutes with $A$.  
*Proof.* $D\Phi(0)=\tfrac16\sum_kA^{-k}A^k=I$, so $\Phi$ is a local diffeomorphism. With $J^6=\mathrm{id}$ and $A^6=I$, $\Phi\circ J=\tfrac16\sum_kA^{-k}J^{k+1}=A\cdot\tfrac16\sum_kA^{-(k+1)}J^{k+1}=A\circ\Phi$. Then $AN_\Phi A^{-1}=\Phi JTJ^{-1}\Phi^{-1}=\Phi T\Phi^{-1}=N_\Phi$ since $JT=TJ$. $\square$ (Formal sanity example of the averaging identity: `dyad_p1_math_checks.py` P1-4.)  
**Scope.** Radius qualitative, as in E1; $\Phi$ is a further normalization object and inherits none of the finite-chart bounds of §6.14 (SG-19); no analyticity (B-an, B-6 OPEN). **Interface.** $\Phi$ is a real $C^\infty$, hence $C^3$, chart meeting the hypothesis of Genesis v2.8.9 §6.3c instance C2 ($\Phi(0)=0$, $D\Phi(0)=I$, $\Phi T\Phi^{-1}$ commuting with $A$). Whether Genesis C2 or OFN class C uses it is their owners' decision. No physical model, carrier, closure condition or $\gamma$ is selected (SG-14/15).

`[OPEN]` `[v6.4.18]` **Not established:** convergence of $\log F$, $F^{1/2}$, $F^{1/6}$ (B-an, B-6); uniqueness among all $C^\infty$ generators of $F$; quantitative radii and finite-$C^k$ versions; convergence of $F^{-n}R_\infty F^n$; physical exchange or G2 realization.

`[NUM]` `[scope: illustration only]` Sampled $\max\|DF-I\|/Q\approx3.80$–$4.07$ for $|W|\in[0.005,0.05]$, consistent with $3|\mu|\approx3.77$; not a proof input.

---

## §7. Import Ledger {#sec-7-imports}

`[COR]` `[v6.4.20]` **Dependency structure.** The self-contained foundation of this study is derived from the postulated primitive map $T(\rho,\eta)$ with no upstream scientific DSN import: DYAD-ALG-NF6, DYAD-ALG-NF6-OBS, DYAD-THM-NF-INV, DYAD-THM-NF-REM, DYAD-THM-PRIM-CTR, the OPEN 3 per-block and offset results (DYAD-ALG-OPEN3-LEADING, DYAD-THM-OPEN3-SPIRAL-REM, DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS, and of DYAD-ALG-OPEN3-PHASE-OFFSET the static-offset identity and $\Delta_1,\Delta_2$; its primitive-memory expansion uses the R9 memory law, $c_{\rm iso}$ and $\Lambda_1$), DYAD-THM-LPHASE-ROWA-REMAINDER, the six-step module and the native OPEN 9 derivations, excluding the named RECOG imports. **R9-dependent layer:** T1, T2 and the chart-variable memory law (DYAD-THM-OPEN3-ASYMPTOTIC-PHASE) and DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER are `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`; R9 is load-bearing for them (claim-level row below). Chain: Dyadic NF6, PRIM-CTR, NF-REM → RECOG-THM-R9-MEMORY → Dyadic T1/T2/OPEN 21 → RECOG-THM-A1A-CD-IDENTIFICATION and RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (RECOG v0.3.22). RECOG records that no A1a result is used to establish R9; the chain is acyclic. A change to R9 (statement, rows or $C_2$) reaches this document through RECOG v0.3.22 §7.3 (downstream dependents register). Custody does not move. Cross-study interpretations elsewhere (face-flux identity, OPEN-M gate conversion) use external inputs whose provenance is recorded at their entries (§6.2, §6.11, §6.12, SG-15). (v6.4.19 paragraph: Appendix A H-5.)

**Claim-level scientific imports** `[v6.4.20]`:
- `[THM]` [import: RECOG v0.3.22 §6.13a | RECOG-THM-R9-MEMORY] track $C_z$ in the chart of DYAD-ALG-NF6; rows $(C_2,q_0)=(517,\tfrac1{400})$ on $|z|\le\tfrac1{20}$ and $(163,\tfrac1{1600})$ on $|z|\le\tfrac1{40}$, not mixed. Used by DYAD-THM-OPEN3-ASYMPTOTIC-PHASE (T1, memory law) and DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER. Custody: RECOG.
- `[THM]` [import: RECOG v0.3.22 §6.13b | RECOG-THM-A1A-RECIPROCAL-AMPLITUDE] start set $U$; used by the leading-decay statement of §6.5. Its proof uses DYAD-THM-PRIM-CTR only (no cycle). Custody: RECOG.
- `[ALG]` RECOG-ALG-NU3-CLOSED-FORM, RECOG-ALG-NU3-NONVANISHING (§6.6, §6.11) and RECOG-ALG-CHART-LAWS (§6.14): statement-level imports at owner grade, as recorded at their entries.

### §7.0 Current editions and source pins {#sec-7-0-editions}

`[DEF]` `[v6.4.20]` One table of the editions this ledger uses. A hash marked "project copy hashed by DYAD" was computed from the project file during the v6.4.20 draft work; "not recorded" means this ledger carries no hash for that edition.

| Document | Edition | Status | SHA-256 | Identity source | Role for this ledger |
|---|---|---|---|---|---|
| Dyadic (this ledger) | v6.4.19 | ADOPTED 20 Oct 2026; superseded by v6.4.20 (this edition, adopted 21 Oct 2026; its SHA-256 is in `RTG_DYADIC_v6_4_20_RELEASE_RECORD.md`) | `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9` | release record; verification record | base of P1/P2 |
| Dyadic ATLAS P1 working file | v6.4.20 P1 | noncanonical; reviewed (`ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED`) | `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905` | P1 record; reviewer hash check | base of the v6.4.20 drafts |
| RECOG | v0.3.22 | ADOPTED 20 Oct 2026 (current) | `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` | project copy hashed by DYAD; RECOG release record | claim-level imports (§7); consumer of §6.14 |
| RECOG | v0.3.21 | ADOPTED 20 Oct 2026; superseded by v0.3.22 | `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` | project copy hashed by DYAD | history |
| RECOG | v0.3.20 | FROZEN (external freeze recorded by RECOG v0.3.21 G1) | `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df` | project copy hashed by DYAD; G1 record `5c00f66d…9b55` | historical source pins in §1, §2, §6 (content identical to v0.3.22, check S2) |
| Number Genesis (NUMGEN) | v1.20.8 | ADOPTED 21 Oct 2026 | `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e` | project copy hashed by DYAD | L-PHASE interface (I1–I5); notice receipts N3, N10–N15 |
| Ontological Foundations (OFN) | v0.10 | ADOPTED 19 Oct 2026 | `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa` | OFN release record | imports IMP-O10-03/04/05; N9 answered (N-O10-1) |
| Genesis Geometry | v2.8.9 | ADOPTED 19 Oct 2026 | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` | Genesis release record; OFN-computed | consumer; live Dyadic pins remain v6.4.13 (repin to v6.4.14+ deferred, R-1); no new Dyadic RID imported |
| RRF Representation Registry | v0.8.4 | ADOPTED 20 Oct 2026 (working standard) | `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce` | RRF adoption record | consumer; records N14 (§0.2, §2.4b) |
| Triadic Birth-Lift | v1.6.1 | ADOPTED 19 Oct 2026 | not recorded in this ledger | Triadic release record (not in the project) | consumer; §7.1 repins to Dyadic v6.4.13 (N2 answered) |
| OPEN-M | v0.7.1 | ADOPTED 7 Oct 2026 | not recorded in this ledger | — | R16 `UVM-RESULT-AUDIT1`; target conditions of the 4/125 gate |
| Programme Overview | v1.2 | ADOPTED | not recorded in this ledger | — | SG-PROG-1–4; `RTG-OPEN-GENERATOR-SELECTION` |
| DSN Methodology | v1.3 | ADOPTED | not recorded in this ledger | — | tag grammar, lifecycle |
| DZT | v0.8 | June 2026 (project copy) | not recorded in this ledger | — | string crosswalk (Appendix F) |
| AZ | v0.6 | June 2026 (project copy) | not recorded in this ledger | — | string crosswalk (Appendix F) |

`[DEF]` `[v6.4.20]` **Historical RECOG pins.** Claim imports in §1, §2 (OPEN 9, OPEN 12), §6.11 and §6.14 keep their RECOG v0.3.20 pins on purpose. Every v0.3.20 paragraph carrying RECOG-ALG-NU3-CLOSED-FORM, RECOG-ALG-NU3-NONVANISHING, RECOG-THM-P2-HET, RECOG-THM-P2-C0-FIRST, RECOG-ALG-CHART-LAWS, RECOG-ALG-LEADING-RETURN-EQUIVARIANCE or RECOG-THM-R9-MEMORY occurs byte-identically in v0.3.22 (`p2_source_checks.py` S2), so the pinned statements are current. The claim-level rows above cite v0.3.22.

The following are programme context, except where a claim-level row above applies:
- `RTG_PROGRAMME_OVERVIEW_v1.2` — SG-PROG-1 through SG-PROG-4; `RTG-OPEN-GENERATOR-SELECTION`.
- `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10` — motivational layer for the generator choice; does not derive $T$. OFN imports `DYAD-THM-PRIM-CTR` (IMP-O08-20), `DYAD-THM-FORMAL-Z6-GENERATOR` (IMP-O10-03), Lemma F / F3 (IMP-O10-04) and the OPEN 3 records (IMP-O10-05); CUST-O09-01 is answered by `DYAD-DEF-PRIMITIVE-MAP`.
- `RTG_RELATIONAL_RECOGNITION_DSN` — v0.3.22 (adopted) for claim-level imports; v0.3.20 (frozen) for the historical pins above. RECOG-THM-R9-MEMORY is load-bearing for the R9-dependent layer; the others feed OPEN 9 / OPEN 12 status and cross-references.

Exports to (via Import Ledger entries in those documents):
- `RTG_TRIADIC_BIRTH_LIFT_DSN` (v1.6.1, adopted 19 Oct 2026) — §7.1 imports `DYAD-THM-C21`, `DYAD-ALG-BRIDGE-LEMMA`, `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` item 1, `DYAD-ALG-PROTECTION-MATRIX` and `DYAD-DEF-PRIMITIVE-MAP`, pinned to Dyadic v6.4.13 (N2 answered). The odd-projected residual $E_{\rm odd}$ (§6.12) is offered as a diagnostic export only.
- `RTG_GENESIS_GEOMETRY_DSN` (v2.8.9, adopted 19 Oct 2026) — imports $\mu_6$, $\tau$, the bridge frame and protection matrix, `DYAD-ALG-NF6`, the OPEN 9 finite ledger, `DYAD-ALG-NU5-P5`, `DYAD-ALG-GLATTICE5`, `DYAD-ALG-ALIAS-PHASE`, `DYAD-ALG-A1A2-LIEGAUGE` and the conditional `DYAD-CAND-P0-DYADIC`. Genesis pins Dyadic v6.4.13; its repin to a later edition is deferred (R-1). v2.8.9 imports no new Dyadic RID.
- **Consumer (acceptance recorded): `RTG_RELATIONAL_RECOGNITION_DSN`** — `DYAD-ALG-NF6`, `DYAD-ALG-NF6-OBS`, `DYAD-THM-PRIM-CTR`, `DYAD-THM-NF-INV`, `DYAD-THM-NF-REM`; acceptance recorded from v0.3.2 and retained through v0.3.22. Consumer outcomes at RECOG grades: R11 CLOSED, R10 DELIVERED/ACCEPTED, R9 CLOSED, R8 CLOSED; A1a (v0.3.22) uses the OPEN 21 remainder at the v6.4.18 pin.
- **Consumer (acceptance recorded): `RTG_NUMBER_GENESIS_DSN`** — `DYAD-THM-PRIM-CTR` (seed admitted to the tube) and `DYAD-THM-Q403-PHASELAW`; v1.20.8 (adopted 21 Oct 2026). Tube membership does not certify GAP-LOCK; GAP-LOCK is NUMGEN-owned (pointer below).
- **Offered import: `RTG_NUMBER_GENESIS_DSN`** — `DYAD-THM-LPHASE-ROWA-REMAINDER` (`[THM]`): constant and branch certificate for NUMGEN L-PHASE on row A. NUMGEN v1.20.8 records N15 RECEIVED and defers the import to a later edition (OPEN sub-item "L-PHASE explicit constant"). No coefficient transfer (SG-19).
- **Reference consumers:** OPEN-M v0.7.1 (`DYAD-CAND-P0-DYADIC` conditional only; R16 `UVM-RESULT-AUDIT1`); RRF v0.8.4 (profiles RRF-DYAD-W, RRF-DYAD-NF; N7, N9, N14 recorded; `DYAD-ALG-NF6-DEG10` as VF-1).

### §7.0a L-PHASE row-A export interface (I1–I5) {#sec-7-0a-lphase}

`[DEF]` `[v6.4.20]` Interface between `DYAD-THM-LPHASE-ROWA-REMAINDER` and the NUMGEN v1.20.8 records, as confirmed by NUMGEN on 20 Oct 2026.

| Item | DYAD object | NUMGEN v1.20.8 record | Agreement |
|---|---|---|---|
| I1 lift | sum of principal increments $\delta_T=\operatorname{Arg}(W(Ty)/W(y))$ (increasing lift); $\hat\varphi_{6m}$ evaluated at $T^{6m}x$ | `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`; monotonicity `NUMGEN-RESULT-N5AS1-L-MONO` | same lift; NUMGEN states it explicitly from v1.20.8 |
| I2 frame | $W=\rho-\eta/2+i(\sqrt3/2)\eta$ with lifted $\eta$ | $W=\rho+\omega\eta_{\rm wrap}$ (`NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`) | on $U_T$, $\vert W\vert <0.047$ gives $\vert \eta\vert <0.0543<\pi$, so $\eta=\eta_{\rm wrap}$ and the two frames coincide (owner check M10) |
| I3 observable | $Q_m=\vert W(T^{6m}x)\vert ^2$, the primitive observable | block-sampled primitive amplitude $q_m:=Q_{\rm true}(T^{6m}x)$ (DEF, no RID) | not the chart variable $q=\vert z\vert ^2$ (SG-19; NUMGEN SG-NG-18) |
| I4 sign | increment $2\pi-\tau Q_m+r_m$; the defect is read as a lag | `NUMGEN-RESULT-N5AS1-L-PHASE` ($C$ existential); defect $D_M$: `NUMGEN-DEF-N5AS1-DEFECT`; `NUMGEN-RESULT-N5AS1-INF1` | same orientation; NUMGEN imports no constant (OPEN sub-item "L-PHASE explicit constant") |
| I5 domain | block base points in $U=\{0<Q\le\tfrac1{625}\}$; intermediate steps in $U_T=\bigcup_{j=0}^5T^j(U)$ | NUMGEN tube is existential; amplitude law `NUMGEN-RESULT-N5AS1-L-BACKBONE` | remainder bound at base points in $U$ only; branch certificate on $U_T$ (asymmetry below) |

- **Upper bound.** $\tfrac{403}{250}$ is a certified upper bound (the ceiling of a majorant, certificate value $1.61112$), not an optimal constant; the sampled angular supremum tends to $\Lambda^*\approx1.4003$ (`[NUM]`).
- **Domain asymmetry.** The remainder bound (R) holds at block base points in $U$. The branch certificate (B) holds at every point of $U_T\supset U$. A start in $U_T\setminus U$ is covered by (R) only from the first block base point that lies in $U$; no bound is claimed at base points in $U_T\setminus U$. NUMGEN's tube is existential and is not identified with $U$.
- **GAP-LOCK.** GAP-LOCK Lemmas 1–3 are CLOSED `[ALG]` in NUMGEN v1.20.8 §6.6 at NUMGEN grades. This ledger neither restates nor regrades them; its only input is the explicit row-A constant above, whose import NUMGEN has deferred.
- **Defect-threshold constant.** The limit $e^{\pi/(3\tau)}=\lambda_{\rm DSI}^{1/6}$ of `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` is related to the §6.3 constants by exact identities only (§6.3).

### Outbound notices — state table (v6.4.20) {#sec-7-notices}

`[DEF]` `[v6.4.20]` One recipient per row. "Where recorded" names the consumer record read for this edition; "NOT RECORDED" means no receipt was found there, not that the notice was refused. Notices N16–N20 (ATLAS disposition §6) are prepared only after external verification of this edition's SHA-256; none is prepared in this edition.

| Notice | Issued in | Recipient | Subject | State | Where recorded |
|---|---|---|---|---|---|
| N1 | v6.4.11 | Genesis | recognize GEN-DEF-PRIMITIVE-MAP as alias of DYAD-DEF-PRIMITIVE-MAP | ANSWERED | Genesis v2.8.6 G-B02; retained v2.8.9 §1 |
| N2 | v6.4.11 | Genesis | repin frame/protection-matrix imports to DYAD-DEF-BRIDGE-EXPORT-CONTRACT / DYAD-ALG-PROTECTION-MATRIX | ANSWERED | Genesis v2.8.6 G-B03; retained v2.8.9 §7 |
| N2 | v6.4.11 | Triadic | same repin | ANSWERED | Triadic v1.6.1 §7.1 (repinned to Dyadic v6.4.13) |
| N3 | v6.4.11 | NUMGEN | DYAD-CAND-PHISTAR-ENTRY-PHASE does not exist in Dyadic; identify the historical source | ANSWERED | NUMGEN v1.20.8 §9.1: pin removed, `[CAND]` cap kept, historical source not identified; $\phi_*$ removed from §4 here |
| N4 | v6.4.11 | OFN | CUST-O09-01 answered by DYAD-DEF-PRIMITIVE-MAP | INFORMATIONAL — no OFN receipt recorded | OFN v0.10 §12.3 retains the inherited v0.9 CUST-O09-01 paragraph |
| N5 | v6.4.11 | RECOG | bridge-lemma general proof cross-referenced; Dyadic RID retained | INFORMATIONAL — no RECOG receipt recorded | RECOG v0.3.22 §7.2 lists N10–N13 only |
| N6 | v6.4.12 | RRF | G2-FIX content registered as DYAD-THM-LOCAL-INVOLUTION-GERM | RECEIVED (by citation) | RRF v0.8.4 §2.4b, §6.2 |
| N6 | v6.4.12 | OFN | same | INFORMATIONAL — no OFN receipt recorded | — |
| N7 | v6.4.12 r1 | RRF | OPEN 19 closed (formal); clock bridge | RECEIVED | RRF v0.8.2 (17 Oct 2026); retained v0.8.4 §0.2 |
| N7 | v6.4.12 r1 | Genesis | same | ACKNOWLEDGED — no import | Genesis consumer-impact note (17 Oct); v2.8.7 release record |
| N7 | v6.4.12 r1 | OFN | same | NO SEPARATE RECEIPT — used by import | OFN v0.10 IMP-O10-03 cites DYAD-THM-FORMAL-Z6-GENERATOR resting on DYAD-THM-FORMAL-CENTRALIZER |
| N8 | v6.4.13 | Genesis | M2c: $\nu_5^{(5)}$ closed form DYAD-ALG-NU5-P5 | RECEIVED | Genesis v2.8.8 (M2c CLOSED at the point of use); retained v2.8.9 |
| N9 | v6.4.13 | RRF | formal ℤ₆ generator; Lemma F / F1–F3 | RECEIVED | RRF v0.8.3 §2.4b–c; retained v0.8.4 |
| N9 | v6.4.13 | OFN | same | ANSWERED at owner level | OFN v0.10 O10-P7, RF-O10-04; release record N-O10-1 |
| N10 | v6.4.14 | RECOG | OPEN 3 chart-level spiral residual | RECEIVED — no use | RECOG v0.3.22 §7.2 |
| N10 | v6.4.14 | NUMGEN | same | RECEIVED — no use | NUMGEN v1.20.8 §9.1 |
| N11 | v6.4.15 | RECOG | OPEN 3b offset and memory | ADOPTED USE — `RECOG-THM-A1A-CD-IDENTIFICATION` depends on T1/T2 (`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`) at RECOG's pin; the earlier v0.3.21 reference import (SG-R14) is in the v6.4.20 notice table | RECOG v0.3.22 §6.13b; §7.2 mirror to be reconciled by RECOG |
| N11 | v6.4.15 | NUMGEN | same | RECEIVED — no use | NUMGEN v1.20.8 §9.1 |
| N12 | v6.4.16 | RECOG | OPEN 3 closed in scope; OPEN 21 opened | RECEIVED — no use | RECOG v0.3.22 §7.2 |
| N12 | v6.4.16 | NUMGEN | same | RECEIVED — no use | NUMGEN v1.20.8 §9.1 |
| N12 | v6.4.16 | RRF | same | NOT RECORDED | no entry in RRF v0.8.4 |
| N13 | v6.4.17 | RECOG | OPEN 21 primitive-variable remainder | RECEIVED — used | RECOG v0.3.22 §7.2: in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION at the v6.4.18 pin |
| N13 | v6.4.17 | NUMGEN | same | RECEIVED — no use | NUMGEN v1.20.8 §9.1 (no R9-conditional input) |
| N14 | v6.4.18 | FMS | OPEN 20 B-∞ existence: DYAD-THM-SMOOTH-EMBEDDING | NOT RECORDED | no FMS record after 19 Oct 2026 in the project |
| N14 | v6.4.18 | RRF | same | RECEIVED | RRF v0.8.4 §0.2, §2.4b |
| N14 | v6.4.18 | OFN | same | NOT RECORDED | OFN v0.10 (19 Oct) predates v6.4.18 |
| N15 | v6.4.19 | NUMGEN | L-PHASE row A: DYAD-THM-LPHASE-ROWA-REMAINDER | RECEIVED — import deferred | NUMGEN v1.20.8 §6.6 OPEN sub-item, §9.1 |

### Export protocol

`[DEF]` `[v6.4.20]` All exported dyadic claims are conditional on the selected generator $T$ (SG-PROG-2): they are not physically primitive, inevitable or universal beyond the support of an explicit selection/universality result (`RTG-OPEN-GENERATOR-SELECTION`). Importers carry `[scope: conditional on the selected generator T]`.

`[DEF]` Convention-dependent exports, including Lie-gauge normalization and projection coefficients, must carry their convention tag in the importing document.

`[DEF]` Dyadic exports are local continuous $p=6$, $K=1$ module data unless explicitly stated otherwise. They do not export Genesis lift scale, UV data, or discrete TDR-G policy information.

---

## §8. Artifact and Script Registry {#sec-8-artifacts}

**OPEN 11 / F1 artifacts:**
- [RID: DYAD-ART-IA-CERT-FIXED] :: `rtg_ia_cert_fixed.cpp` :: Arb ball certification on `(4,10)` branch :: `[ENG]`
- [RID: DYAD-ART-IA-BULK] :: `rtg_ia_bulk_cert.cpp` :: Arb certification on `(4,11)`, `(5,11)`, `(5,12)` :: `[ENG]`
- [RID: DYAD-ART-STRIP1] :: `certify_transition_strip.cpp` :: 15M-slice Arb audit of `(4,10)`/`(4,11)` transition strip :: `[ENG]`
- [RID: DYAD-ART-STRIP2] :: `certify_transition_strip2.cpp` :: Arb IFT/transversality cert of $q_{10/11}$ strip :: `[ALG via IA]` ✓
- [RID: DYAD-ART-QMAX] :: `certify_q_max.cpp` :: Arb endpoint enclosure for $Q^{(2)}(2)$ :: `[ENG]`
- [RID: DYAD-ART-T1-TAYLOR] :: `t1_near_zero_taylor.py` :: Near-zero Taylor proof for T1 :: `[ENG]`
- [RID: DYAD-ART-T1-SIGN] :: `f1_T1_sign_proof.py` :: Algebraic sign chain for T1 derivative :: `[ENG]`
- [RID: DYAD-ART-T2-BOUND] :: `f1_T2_theta_bound.py` :: Four-lemma proof scaffold for T2 :: `[ENG]`
- [RID: DYAD-ART-OPEN18] :: `open18_arb_cert_final.cpp` :: FLINT/Arb certificate for OPEN 18 footprint monotonicity :: `[THM-ALG via IA]` ✓

**Normalization pipeline artifacts:**
- [RID: DYAD-ART-NORM-P6] :: `normalize_p6_liegauge_exact.py` (SHA-256 `cec918f808cbc02c53beba5f88faf1edbed830a87dac7283e6ac2511d2ec5835`, `evidence/dyad/scripts/`; its $h_4$ closed forms are confirmed exactly by `dyad_h4_archival_exact_check.py`) :: Archival coordinate change $\Phi_{\rm archive}=\mathrm{id}+h_4+h_{5,\rm nr}$ (SG-19 operation (i)); `mp.dps=120` numerical with tolerance pruning, not exact; "$h_3=0$" refers to the non-resonant cubic of the return logarithm; does not zero non-resonant channels; preserves all raw coefficients through degree 5 :: role: archival coordinate change (numerical, 120-dps, tolerance-pruned); availability: repository; `[ENG]` validated behavior: reproduces the recorded raw coefficients through degree 5 on its inputs. Numerical residual tests recorded under `[NUM]` scope. `[COR]` v6.4.10: previously graded `[ALG]`; that grade described a proof the script does not perform.
- [RID: DYAD-ART-HOM-P6] :: `homological_solver_p6_numeric.py` :: 1-step discrete homological solver (80-digit numeric); recovered copy regenerates `phi1_p6_deg5.json`, all 18 nonzero coefficients agreeing with the exact solve (DYAD-ALG-NF6) to $\sim5\times10^{-81}$; original output byte identity `[OPEN]` :: `[ENG]`
- [RID: DYAD-ART-ACCUM-P56] :: `step_accumulation_p5_p6_cli.py` :: $p$-step accumulation of normalized 1-step models; computes $F_1^p$ :: `[ENG]`
- [RID: DYAD-ART-NORM-PSTEP] :: `normalize_pstep_lie.py` :: Log-channel projection $G_{\rm proj}=\exp(\mathscr P_{\rm keep}\log F_W)$ (SG-19 operation (ii)); a reduced model, not a solved conjugacy :: `[ENG]`
- [RID: DYAD-ART-GAUGE-BRIDGE] :: `gauge_bridge_p6.py` :: Bridge audit $\Psi^{-1}\circ F_1^6\circ\Psi=F^6_{\rm raw}$ through degree 5 (an identity on its inputs; does not prove conjugacy of $G_{\rm proj}$). **Prints diagnostics only; no exit-code acceptance gate** (negative control: a $10^{-3}$ perturbation still exits 0). Any status that rested on its exit code is re-read as "ran" :: `[ENG]` diagnostic; its valid input identities are not falsified by the missing gate. `[COR]` v6.4.10: previously graded `[ALG]`.
- [RID: DYAD-ART-BLOCK-CSV] :: `generate_block_csv.py` :: Branch-local $(m,Q,\Theta)$ CSV extraction :: `[ENG]`
- [RID: DYAD-ART-SPIRAL-FIT] :: `spiral_phase_fit.py` :: Branch-local OPEN 3/OPEN 5 residual-and-phase fitting :: `[ENG]` `[v6.4.16]` recovered, SHA-256 `c431c851ba81f37ffc3a37ad28d5ead216fdcd3beed5b6c29907a37f423e6b90`; documented model discrepancy (§6.14); not a definition of the OPEN 3 residual.
- [RID: DYAD-ART-JET6] :: `jet6_deg5.json` :: Canonical raw 6-step jet coefficient dictionary :: `[ALG]`
- [RID: DYAD-ART-JET1] :: `jet1_deg5.json` :: **Raw** one-step $W$-jet, degree $\le5$ (17 coefficients; $[f]_{(2,0)}=\tfrac{1+i\sqrt3}{12}\ne0$) — the *input* to normalization, not a normalized dictionary :: `[ALG]` `[COR]` v6.4.10: label corrected; coefficients unchanged.

**Return-enclosure artifacts (v6.4.10). Installation manifest: `RTG_DYADIC_v6_4_10_INSTALL_MANIFEST.json` (owner-measured SHA-256 where the file is held by the owner; producer-manifest references otherwise); the original 56-member P2-B v2 manifest and the P0–P1 manifest are preserved unchanged:**
- [RID: DYAD-ART-RE-P0P1] :: `DYAD_RETURN_ENCLOSURE_P0_P1_evidence.zip` :: P0 convention contract, P1 exact normalizer and obstruction, two arithmetic implementations, negative bridge control :: `[ALG]`
- [RID: DYAD-ART-RE-P2B2] :: `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` :: P2-B v2 exact-rational producer (67 checks) + independent validator (73 checks), negative controls; contains the extracted P2-A v2/P2-B v1 baseline tree at `inputs/baseline/DYAD_RETURN_ENCLOSURE_P2A_v2_P2B_v1/`, including the preserved P2-A v1 proof (`P2A_v1_PROOF_PRESERVED.md`) and certificate JSON (`P2A_v1_certificate_preserved.json`); no original P2-A v1 ZIP is embedded. Exact $h$/$J$: `outputs/certificate.json` :: evidence for `[THM]` entries of §6.14 :: `[v6.4.16]` owner-measured SHA-256 `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4` (matches the 22 Sep reviewer identity as reported); `outputs/certificate.json` `d59b0ff68b4341debf5e8a7542bf3865b63dd63e36546952db95298c2bd5c6ce`
- [RID: DYAD-ART-RE-REVIEWS] :: `DYAD_RETURN_ENCLOSURE_P0_P1_REVIEW.md`, `DYAD_P2A_V2_P2B_V1_REVIEW.md`, `DYAD_P2B_V2_REVIEW.md`, `OWNER_ADOPTION_REVIEW_v1.md` :: independent reviewer records (Claude), adoption review and draft review (ChatGPT); role: review/availability metadata, not a truth grade
- [RID: DYAD-ART-RE-REFEREE] :: `dyad_referee_p2b_v2.py` + backend `dyad_return_qchi_exact.py` :: 47 executed exit-coded checks, all passing; exact $\mathbb{Q}(i\sqrt3)$ reconstruction of the finite jets and normalizer (independent of producer/validator code), with binary-float modulus and 60-dps non-directed tail/domain checks. Executable-reviewer role, distinct from the exact-rational enclosure certificates; negative-control copy exits 1 :: `[ENG]`
- [RID: DYAD-ART-RE-SUPPL] :: `DYAD_OWNER_ADOPTION_REVIEW_v1.zip` → `DYAD_OWNER_ADOPTION_REVIEW_v1/scripts/check_owner_adoption.py` (backend/referee under that archive's `sources/`) :: 45 shared-backend supplementary checks (rational square-root enclosures, exact $P^+/J^+$ ceilings, directed-rational $\Psi$, finite-order residuals, $(3,2)$ iteration identity); not an independent reconstruction :: `[ENG]` :: `[v6.4.16]` owner-measured SHA-256 of `check_owner_adoption.py` `c04096e1cd9ab559d5997c92ad8a442fbf79d350e801e9ed01e6e6a9e19800fe` (matches the 22 Sep reviewer identity as reported)
- [RID: DYAD-ART-NF6-DEG10] `[v6.4.11]` :: `DYAD_CHECK_degree10_even_term_hatF.md` (SHA-256 `dcfd808c0270202768b4422acb474cda08f693a1cf69e8ec368e7faac414f4d4`) + engine `dyad_return_qchi_exact.py` (`e45286fa100b2b31c4d547e8513e23f926b2bda36d31938577fa9f312ca350f6`) :: written verification record for DYAD-ALG-NF6-DEG10; the full degree-10 even-part table is not attached (re-executable with the engine) :: evidence for `[ALG]` finite statement
- [RID: DYAD-ART-OPEN19-SESSION] `[v6.4.12 r1]` :: `DYAD_OPEN19_FORMAL_CENTRALIZER_PROOF_SESSION.md` v1.2 (SHA-256 `6749df1126b36453f1f860dd797a872f291fcc7926412225f839acfb2e60e1c6`) :: proof record for §6.16 and Corollary A; reviewer records: SESSION v1.1 review (ACCEPT), RRF sync review `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_2.md` (`ACCEPT SCOPED`) :: `[SESSION]` record; role: provenance, not a truth grade
- [RID: DYAD-ART-OPEN19-KERNEL] `[v6.4.12 r1]` :: `dyad_open19_kernel_check.py` v1.1 (SHA-256 `1cb40446c0289424fcb8539c77aec6d43f4e6a0873434645b8cc3dc4397a291e`) + `dyad_open19_a0_boundary_check.py` (`a2aedc51acef70738e5b6006c601c036d5ee182a5d2eb899beb92c5dc4303a45`) :: exit-gated sympy reproductions of Lemma K for $k\le13$ and of the $a=0$ boundary structure for $b\le7$ :: `[ALG]` `[scope: finite]`
- [RID: DYAD-ART-OPEN19-R0CERT] `[v6.4.12 r1]` :: `dyad_open19_R0_identity_cert.py` (SHA-256 `c8c144426b2c9e795df19a997b181209fce6ab7edeaa1b9c04e731ad0d059cf8`) + engine `dyad_return_qchi_exact.py` (`e45286fa100b2b31c4d547e8513e23f926b2bda36d31938577fa9f312ca350f6`) :: 3 truncations × 7 exit-gated assertions for $R_0$ (§6.16); owner rerun 16 Oct 2026 PASS at $N=6,8,12$; independent reviewer rerun PASS in the SESSION v1.1 review round (kernel check and $R_0$ certificate). The r1 review reran only `dyad_open19_a0_boundary_check.py` and relies on those earlier records for the other two :: `[ALG]` `[scope: finite jets]`
- [RID: DYAD-ART-NU5-P5] `[v6.4.13]` :: `dyad_m2c_nu5_p5_exact.py` (SHA-256 `5fcccb9d38a7dcafe317044ca341cbead38047e24041da92e6fe891faa5cd464`) :: exact $\mathbb{Q}(\zeta_5)$ one-step normal form of the $K_5$ family through degree 5; $p=6$ calibration against DYAD-ALG-NF6 ($n_{21},n_{32},n_{05}$); exit-gated, negative control exits 1; owner run 18 Oct 2026 PASS :: `[ALG]`
- [RID: DYAD-ART-LEMMA-F-RECORD] `[v6.4.13]` :: `DYAD_LEMMA_F_FLAT_CENTRALIZER_PROOF_RECORD_v0_3.md` (SHA-256 `2e6c5c59a1fdfe6baa1702df8873b0d89664796d4f317313f239969b406a8ece`; current) — predecessor v0.2 (`0a2ae5e266a9d9dd175503df4ea9629c10978637bdaadadc38e75a94fb104dfb`, the text reviewed in the r1 round; superseded on the §3.4 construction-route sentence only) :: proof record for §6.17; reviewed r1 and r2 rounds (18 Oct 2026) :: `[SESSION]` record, provenance for the adopted `[THM]`
- [RID: DYAD-ART-OPEN3-P2] `[v6.4.14]` :: `dyad_open3_p2_exact_gate.py` (SHA-256 `89939581d553483de0793b17c6e4b65748291e158e6db218bf1a0c2883b10c50`) + output `p2_coefficients.json` (`c24389c94f5d77a674374aabc8cef75f7f5781e821a81d65700e1c2f8151f3dc`); predecessor sanity check `dyad_open3_p5_sq_identity_sanity.py` (`9ded29aa0484d695abc1d09e0e57312924a456bb52d3381214300b9fda5614d7`) :: exact sympy gate for DYAD-ALG-OPEN3-LEADING; exit-gated; five negative controls :: `[ALG]`
- [RID: DYAD-ART-OPEN3-P3] `[v6.4.14]` :: `dyad_open3_p3_remainder_cert.py` (SHA-256 `b7df79b0f820f8431e6c2af54a03ef8fd93f869fb06470ed037cdca1126d258d`) + engine `dyad_return_qchi_exact.py` (`e45286fa100b2b31c4d547e8513e23f926b2bda36d31938577fa9f312ca350f6`) + output `p3_certificate.json` (`bd533725b8c562fae708becdfa6b58ab3601ac5698b1ab00da6afd6493ddfcde`); illustration `dyad_open3_p3_numeric_check.py` (`7e91c6b5648b9756cd83de7f4a1222890537c33b273203f4bb679e4b8d8737e3`) + `p3_numeric.json` (`2e7ee33640c894e3371e26aabc833b2ffd01df2be5072e494a41faead9f414cd`, `[NUM]` only) :: exact-rational certificate for DYAD-THM-OPEN3-SPIRAL-REM; exit-gated; negative controls `neg_K`, `neg_h2`, `neg_mu`; reviewer replay 19 Oct 2026 byte-identical :: `[THM]` certificate
- [RID: DYAD-ART-OPEN3-RECORDS] `[v6.4.14]` :: `DYAD_OPEN3_OBSERVABLE_TRANSPORT_SCOPE_SESSION_v0_1_1.md` (`4526546ad6a99835a9fe2cddd8a6b63d2134ce89d0e9a405e2b601ccf8e6c1ab`), `DYAD_OPEN3_P1_P2_SESSION_RECORD_v0_1.md` (`83248235367c0b38eac670121d209da7bef9d22fd6d5daba8af288a017d91b53`), `DYAD_OPEN3_P3_REMAINDER_PROOF_RECORD_v0_1.md` (`af4a61237a56152101026c70ce461b0ec7bc9fd33e681c215133209e273c2a54`), `DYAD_OPEN3_P3_REVIEW_DISPOSITION_v0_1.md` (`6ab21ca55da0127ccd25fc49ae629b21bcb3f1d4a91e0941d80578db5b69db0b`) :: scope, definitions, proof records and review disposition for OPEN 3 :: `[SESSION]` records
- [RID: DYAD-ART-OPEN3-P4] `[v6.4.15]` :: `dyad_open3_p4_exact.py` (SHA-256 `199a15bae67db1f30cfce66221822315f44d40f27cbfd74249dceebf96f0b703`) + `p4_exact.json` (`945db486fa87e61b9412b47c5b591d88c7e01e607c4aec4998c898882d6b38d8`); `dyad_open3_p4_offset_cert.py` (`4058dfc92d587db75e2a7d68d3c15cddb9d62c6aaaa72b124ab5795f7a8f6b7a`) + `p4_offset_certificate.json` (`9b0e0c80f3a7f5f9ddf052ca8bc203e30f79e7d1ad8619555875f3df3e8557b4`), reusing DYAD-ART-OPEN3-P3 inputs; illustration `dyad_open3_p4_numeric_check.py` (`df8badbf128c97930776666e4646c271d55482d6af959288051a8c6204081005`) + `p4_numeric.json` (`3c19292da85eefa181924f6c26aec0e04b9d7b8a42278013b5832097ee893a34`, `[NUM]` only) :: exact leading terms and exact-rational offset certificate for OPEN 3b; exit-gated; negative controls 6 + 3; reviewer re-execution byte-identical :: `[ALG]` / `[THM]` certificate
- [RID: DYAD-ART-OPEN3-P4-RECORD] `[v6.4.15]` :: `DYAD_OPEN3_P4_ASYMPTOTIC_PHASE_PROOF_RECORD_v0_1.md` (`9d781afcc395683379929a93496bcb069f9b1aa14a1de03ff1147bc21fc8cd16`); notice record `DYAD_v6_4_14_OUTBOUND_NOTICES_N10.md` (`ea120a2658dc28dd85661c71740efb8696457c77827417ec6ee6ae683f91b4c0`) :: P4 proof record and N10 notice text :: `[SESSION]` records
- [RID: DYAD-ART-OPEN3-P0] `[v6.4.16]` :: `DYAD_RECOVERED_ARTIFACTS_PROVENANCE_AND_P0_SESSION_v0_1_1.md` (`233947368e7b865eb401f2aa9f5f9e37b059a7c9df3b8fb315615f5fb85801fe`); `compare_h_J_with_p2b_v2.py` (`6e8c7fa75094fe5bd8caa6218c524efb29aa564ea95026392f885829a2f80579`), exit-gated, negative control exits 1; `p0_fit_comparison.py` (`2d5bedaa84a2a98af90f4657e57a45b527b5b5933842e437ca00172e7c422d48`) + `p0_fit_comparison.json` (`60687aceba1dee73259c055a79412168eb0f809c2bffd9d53af752a42fa3c73f`, `[NUM]` only); uses DYAD-ART-OPEN3-P3 inputs, engine `dyad_return_qchi_exact.py` and DYAD-ART-SPIRAL-FIT :: provenance gate for $h,J$ and P0 comparison :: `[SESSION]` record; `[ENG]`/`[NUM]` scripts
- [RID: DYAD-ART-OPEN21-P5] `[v6.4.17]` :: `dyad_open21_p5_remainder_cert.py` v0.1.2 (SHA-256 `80452d8af9c58bd32f1ffeb587e2b5102cf2c651b05770fc002b58a81837787c`) + `p5_certificate.json` (`2902ba44f443fbd911f3c6457e769170795384436140cec0bb5709778942bc10`); $\Lambda_1$ gate `dyad_open21_p5_lambda1_check.py` (`aca13bf62a6034a11e30190178e3e7a7fad932f26b4114cceb941e530e06e8ae`); reuses DYAD-ART-OPEN3-P3 and DYAD-ART-OPEN3-P4 inputs (pinned by hash); illustration `dyad_open21_p5_orbit_num.py` (`e9af1ee1a66287044484aeffe90fb1b2bed1ddf614cefc9dda0c8f049cecc7f5`) + `p5_orbit_num.json` (`94c0933cfb57e16e96d6b10cdb2ab80e8fe4d2fce3c51aadf3fe40993d5f8297`, `[NUM]` only, not byte-reproducible) :: exact-rational certificate for OPEN 21; exit-gated; 7 negative controls; reviewer replay byte-identical :: `[THM]` certificate
- [RID: DYAD-ART-OPEN21-P5-RECORDS] `[v6.4.17]` :: `DYAD_OPEN21_P5_PRIMITIVE_PHASE_SCOPE_SESSION_v0_1.md` (`a75994fdbc51ff662b9db3937a74d3e0c34773182a61b9431942f6a6ba35cf07`), `DYAD_OPEN21_P5_PRIMITIVE_PHASE_PROOF_RECORD_v0_1_2.md` (`ed7b5f25cc927193351245b05f6175a8511ab3f2da53e5d3cd7a1d98ee10463a`; supersedes v0.1 `4410ad54…fd64` and v0.1.1 `5f82ef6c…a5fe4`) :: scope note and proof record for OPEN 21 :: `[SESSION]` records
- [RID: DYAD-ART-OPEN20-BINF-RECORDS] `[v6.4.18]` :: `DYAD_REPLY_TO_FMS_OPEN20_PRIORITY_v0_1.md` (`208ec09a4c57eee69463e0ea6e8867b8868aa019643f075e8b9bfb73db91dda3`), `DYAD_OPEN20_SMOOTH_EMBEDDING_LITERATURE_SCOPE_SESSION_v0_1.md` (`3a06222a67d7b895cbcd911db7928a94fc8dc1599d1aa69da1e83e0a2a78c0be`), `DYAD_OPEN20_P1B_P2_DOMAIN_SESSION_v0_1.md` (`0ab4fab0e30c02a8874e6d08d91dff00abe389e528b492435dc0e3409a55820c`; §1–§2 current, §3 superseded), `DYAD_OPEN20_P2B_DOMAIN_PROOF_SESSION_v0_2_1.md` (`6f275e735897a3f29308de132a416d184b01c2e420fafb83cc012d360033fcf4`; supersedes v0.2 `b8a1434f…19f9`), `DYAD_OPEN20_P3A_ITERATE_DERIVATIVE_BOUNDS_SESSION_v0_1.md` (`b044a41d88c57bfc258469e741d01bd458e9256e2fe4e4ebda92e32b07e9a846`), `DYAD_OPEN20_P3BC_FLAT_DERIVATIVES_AND_CK_CONVERGENCE_SESSION_v0_1_1.md` (`3ceca25ee64d0b0263da10972ab8e64231545e74e8ad8fc977cd25caeb9e487f`; supersedes v0.1 `f299f50f…a136`), `DYAD_OPEN20_BINF_EXISTENCE_INTEGRATION_AUDIT_SESSION_v0_1_1.md` (`57327922a56aabc409023a780618d9ff46070daa785e4c6355a086cabbe66f4e`; supersedes v0.1 `4e598848…7b57`) :: reply, scope and proof records for OPEN 20 B-∞ existence :: `[SESSION]` records
- [RID: DYAD-ART-OPEN20-BINF-CHECKS] `[v6.4.18]` :: `dyad_open20_p3a_check.py` (`56d8178109b34a8858dca6d3d5470524916ae850390bf2a81b86d9ddf2e67140`) + `p3a_check.json` (`1665994e5460a377192a29d3ef7b6efd55491856b7aa5bcd291be7d8fa12ebd1`); `dyad_open20_p3bc_check_v0_1_1.py` (`6cde7ca66cb86101a4ae7b8a41877d49a31ec449563c41bb0d6fc136b6c76d48`) + `p3bc_check_v0_1_1.json` (`4204cd4f05d889df153744b161709d38db261a9ed14ff112c5bf026f7dfe14e9`); `dyad_open20_binf_integration_check.py` (`0d5a1dfdc13a7bfe7d3ebbe63d5dc1d8f88baff44f663fddaff4b765c2fb0264`) + `binf_integration_check.json` (`26ef2748045cb0ceac138beb2f211f4dc5ff2aa17d7d47c81e2e387bca078f5f`) :: exact jet, linear-algebra, exponent and pin checks (8+3+6 gates; 4+3+3 negative controls; reviewer re-executed) :: `[ALG]` checks supporting the proof (not a substitute for it)
- [RID: DYAD-ART-LPHASE-ROWA] `[v6.4.19]` :: `dyad_numgen_lphase_rowA_cert.py` (SHA-256 `117484ae1a2509b6f6065d395840bfdfe2b0c977af0505f9fe6de68c13959cdb`) + helpers `qw.py` (`3a913062c1cdc6d151a2fb5b2f76d5354a367d1fa55df43f1f31d06e1b94cce8`), `tzw.py` (`f007d42cde36d2a70115b9db25f47b107c446735fa31c66664f620c3247a5609`) + output `lphase_rowA_certificate.json` (`8697c6970bd908327c66ef2ce3b2d38386947899033ef7f720bc096c4c3ad4fa`); illustration `lphase_rowA_numeric.py` (`95b891f8f62b42342c0307e77b0f8c13e68cc7f5a3b9d368b18a1a3e4c3a4647`) + `lphase_rowA_numeric.json` (`2291db4e1404654427b567bdba338ea1ce0ddd0b7f4e8bad1bd8b03b16d1b9c4`, `[NUM]` only); scope checks `lphase_scope_checks.py` (`570078dbfc2c8a881c47c4a468370452e0a5d76e8c73055857196e99e49cd8b6`) + `lphase_scope_checks.json` (`9b31c7107a9d1e44cb19b213e1060f5aead30dddc7b79a49b6ca42372d1c3f25`) :: exact-rational certificate for DYAD-THM-LPHASE-ROWA-REMAINDER; exit-gated; 10 gates; negative controls N1–N6; NUMGEN receipt replay byte-identical :: `[THM]` certificate
- [RID: DYAD-ART-LPHASE-P2B-PROV] `[v6.4.19]` :: `dyad_lphase_p2b_provenance_gate_v0_1_1.py` (`343a3631f41e41741f3c0b6e99b6431fe2e0635b7821f9f71674b5f1878a27a5`; current) + `lphase_p2b_provenance_gate.json` (`58cfafd359da64ef8b20f12b656fe3e8ab8b69e559cd46574767c8629692fc89`) + `lphase_p2b_provenance_control_exits.json` (`e2ffa46bced46fff76044a1a651281557b93a70fa7ab96dc13cb1e8f859c1a1e`); predecessor `dyad_lphase_p2b_provenance_gate.py` v0.1 (`5cff2b46eee14d157678320d173c2ca6fe8fa4dcb248018d5ab3d8646e0bf59f`; same gate JSON); inputs pinned in the script: certificate engine, DYAD-ART-RE-REFEREE with backend `dyad_return_qchi_exact.py` (`e45286fa…50f6`), P0/P1 tables (`bb09bace…99f6`, `b42bafb3…6e52`, `8d072962…20cc`, control `60d10315…62bf`) :: transitive exact-coefficient provenance gate for $h$, $n$, $J$; 9 gates, 4 negative controls (exit 1 each; crash exits 3); owner replay; reviewer full replay pending :: `[ALG]` gate
- [RID: DYAD-ART-LPHASE-ROWA-RECORDS] `[v6.4.19]` :: `DYAD_NUMGEN_LPHASE_ANGULAR_ENCLOSURE_SCOPE_v0_1.md` (`1eae1d1a204673969ea0a69f0ecd32624a734e9e96a7f855985c360882c01f74`), `DYAD_NUMGEN_LPHASE_ROWA_CERTIFICATE_SESSION_v0_1.md` (`775c6715e1a5ba3c020927c1990c1843120cecd3e3b2855be17c959947cf233d`), `DYAD_LPHASE_ROWA_P2B_PROVENANCE_GATE_SESSION_v0_1_1.md` (`5e9f324e444a8c48bc226cd159af0195c84f4f10c3a103d49035c971480a8a7f`; supersedes v0.1 `ea22727c…29ec4a82`), `DYAD_REPLY_TO_NUMGEN_LPHASE_ROWA_v0_1.md` (`45cdd7043ee69f0b0dccf23ce47d3c165216d6c8eb381680f8dff581d27851cf`); NUMGEN-side (not DYAD-owned): `NUMGEN_INTERFACE_CONFIRMATION_LPHASE_ROWA_20261020_v0_1.md` (`7a91c223691b3705c2560fca452e671442939452e11cf98820512b182f46f78f`), `NUMGEN_RECEIPT_REPLAY_LPHASE_ROWA_20261020_v0_1.md` (`71bfc4c597b4be502129a6d0da0b1c987723979eec1701b9c1b4187140c4b66f`) :: scope, proof, provenance and interface records for the L-PHASE row-A result :: `[SESSION]` records
- [RID: DYAD-ART-OPEN16] :: `open16_alias_phase.py` :: Exact alias phase $G_-(\pi/\tau)$ and $\arg G_-$ :: `[ALG]`
- [RID: DYAD-ART-OPEN17] :: `open17_a2.py` :: Exact $a_2=86775991\sqrt{15}/755827200$ :: `[ALG]` `[conv: Lie gauge]`
- [RID: DYAD-ART-CYCLOTOMIC-P567] :: `normalize_p_full_onestep_cyclotomic.py` :: Unified exact cyclotomic full one-step Birkhoff engine for $p=5,6,7$ :: `[ENG]`
- [RID: DYAD-ART-P7-C06] :: `normalize_p7_c06_full_cyclotomic_optimized.py` :: Exact $c_{06}^{(7)}$ over $\mathbb{Q}(\zeta_7)$ :: `[ALG]`
- [RID: DYAD-ART-P5-LATTICE] :: `prove_p5_lattice_anomaly_exact.py` :: Exact cyclotomic proof $F_1^5(0,4)=F_{\rm raw}^5(0,4)$ :: `[ALG]`
- [RID: DYAD-ART-HOM-GEN] :: `homological_solver_p_general_numeric.py` :: Generalized $K_p$ homological solver and broad $p$-horizon diagnostic engine :: `[ENG]`
- [RID: DYAD-ART-ACCUM-GEN] :: `step_accumulation_p_general_cli.py` :: $F_1^p$ vs raw $p$-step accumulation / bridge-gap CLI for general $p$ :: `[ENG]`
- [RID: DYAD-ART-P-AUDIT] :: `rtg_p_horizon_audit.py` :: OPEN 9 master CLI: `subgroup`, `normalform`, `certify` modes :: `[ENG]`
- [RID: DYAD-ART-P-CORE] :: `rtg_p_core.py` :: Shared polynomial/map utilities for general $p$ :: `[ENG]`
- [RID: DYAD-ART-P-SUBGROUP] :: `rtg_p_subgroup.py` :: Raw Birkhoff-strobe subgroup-extra projector diagnostics :: `[ENG]`
- [RID: DYAD-ART-Q403-CERT] :: `q4_03_R_identity_certificate.py` :: All-$p$ phase-law remainder-relation certificate (3-path derivation, $\sigma_{-1}(Q)=-L^{-6}Q$ exact, denominator guard, horizon $p=8$–$52$); exits `CERTIFICATE PASS` :: `[ALG]`
- [RID: DYAD-ART-Q403-EXTRACT] :: `q4_03_cascade_extract.py` :: Calibration-gated exact in-field extractor for $Q_p$ (gates on $p=8\to0$, $p=12\to-13+15\sqrt3/2$) :: `[ALG]`
- [RID: DYAD-ART-P-NORMALFORM] :: `rtg_p_normalform.py` :: Numerical one-step normal-form / bridge-gap diagnostics; native-float results `[NUM]` `[scope: diagnostic]` :: `[ENG]`
- [RID: DYAD-ART-P-CERTS] :: `rtg_p_certs.py` :: Exact SymPy/cyclotomic micro-certification authority for OPEN 9 :: `[ENG]`
- [RID: DYAD-ART-SURGICAL] :: `rtg_invariant_algebraic_engine_surgical.py` :: Surgical diagnostic for invariant subgroup-strobe audits; established $(0,4)$ is dynamically active in $J^{extra,raw}_{10,5,D}$, enabling retraction of false sub-horizon inheritance for $G_{04}(10)$ :: `[ENG]`
- [RID: DYAD-ART-B5-STEP3] :: `rtg_b5_step3_reduction.py` :: Step-3 reduction: for $p\ge13$ the nonsecular $m=0$ modes vanish, leaving $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{\rm eff}$; polynomial-mode sum $-p/(1-\lambda^{-3})$ exact :: `[ALG]`
- [RID: DYAD-ART-B5-SEFF] :: `rtg_b5_step3_Seff.py` :: $S_{\rm eff}$ structure; numeric scan $\mathrm{Re}(S_{\rm eff}/S)>0$ to $p=200$ (monotone $\to3$) :: `[NUM]` `[scope: strong numerical evidence]`
- [RID: DYAD-ART-B5-ALLP-CERT] :: `rtg_b5_Seff_limit_cert.py` :: Fast all-$p$ closure certificate: closed form $S_{\rm eff}/S=N/D$, exact limit $3$, and cyclotomic non-division ($\Phi_p\nmid N$ for all $p$ with $\varphi(p)\le6$) proving $F_{\rm raw}^p(0,5)\ne0\ \forall p\ge6$ :: `[ALG]`
- [RID: DYAD-ART-B5-DECOMP] :: `rtg_b5_secular_decomposition.py` :: Exact secular decomposition $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{05}^{(\beta=1)}+R_p$ `[ALG]` `[scope: structure]`; validates against the $p=6..12$ sweep `[ALG]` `[scope: validation]`; ratio-to-3 trend `[NUM]` `[scope: strong numerical evidence]` :: `[ALG]` `[scope: structure]` `[NUM]` `[scope: strong numerical evidence]`
- [RID: DYAD-ART-FRAW-B5-SWEEP] :: `exact_Fraw_b5_sweep.py` :: Exact cyclotomic certificates $F_{\rm raw}^p(0,5)\ne0$ in $\mathbb{Q}(\zeta_p)$ for $p=6..12$ (degree-5 raw $p$-fold iteration, field reduction mod $\Phi_p$) :: `[ALG]` `[scope: finite sweep]`
- [RID: DYAD-ART-FRAW7-B5] :: `exact_Fraw7_certificate.py` :: Exact degree-5 raw 7-fold iteration in $\mathbb{Q}(\zeta_7)$ (field reduction mod $\Phi_7$), proving $F_{\rm raw}^7(0,5)=\tfrac{15}{2}\lambda^5+\tfrac{23}{8}\lambda^4+\tfrac{21}{8}\lambda^3+\tfrac{15}{2}\lambda^2-\tfrac18\lambda+\tfrac{17}{2}\ne0$ :: `[ALG]`
- [RID: DYAD-ART-B5-SECULAR] :: `rtg_extract_b5_secular_coeff.py` :: Targeted extraction + nonvanishing certificate for the $(1,0)$ secular coefficient of the $(0,5)$ source (symbolic not-identically-zero + dyadic-value nonzero); establishes the first failure at $b=5$ of the dyadic channel boundary `[ALG]` (vanishing for $b\le4$ is DYAD-ART-VANISH-CERT; failure for all $b\ge6$ not established) :: `[ALG]`
- [RID: DYAD-ART-VANISH-CERT] :: `degree_b_vanishing_cert_v2.py` `[v6.4.20: custody OPEN; the file is not available in the project and has not been recreated; available evidence DYAD-ART-VANISH-BGRADED and degree_b_vanishing_cert.py (FA-DYAD-04, §6.11)]` :: Exit-code-gated certificate: Route A (β-mode path enumeration, exact source β-sets) + Route B (direct high-precision dyadic-map iteration); certifies $F_{\rm raw}^p(0,b)=0$ for $p\ge b+2$, $b\in\{2,3,4\}$ :: `[ALG]`
- [RID: DYAD-ART-VANISH-BGRADED] :: `rtg_betagraded_vanishing.py` :: β-graded jet-composition engine; computes exact source β-sets and vanishing ranges; scales to $b\ge5$ for the channel-boundary scan :: `[ENG]` `[ALG]`
- [RID: DYAD-ART-VANISH-B234] :: `degree_b_vanishing_scan.py` :: Direct-weight $\lambda^{-(b+1)k}$ vanishing (exact symbolic) + $(c_{02})^2$ cyclotomic identity (exact symbolic) + finite verification of $F_{\rm raw}^p(0,b)=0$ through $p=35$ at 80 dps. $b=2$ proof complete (no cross-path); $b=3,4$ finite scan is `[NUM]` `[scope: strong numerical evidence]`, general-$p$ path-enumeration NOT included (open) :: `[ENG]` `[NUM]` `[scope: strong numerical evidence]`
- [RID: DYAD-ART-CHANNEL-CLASS] :: `channel_classification_scan.py` :: Scan $(0,b)$ for $b=2..8$ across $p=3..35$; $b\le4$ zero / $b\ge5$ nonzero tested boundary :: `[ENG]` `[NUM]` `[scope: strong numerical evidence]`
- [RID: DYAD-ART-BRIDGE-NOTE] :: `dyad_triad_antisymmetric_bridge_v1_1.md` :: Bridge note v1.1: antisymmetric odd-channel identity, $\mu_p=p\bar\lambda\nu_3^{(1,p)}$, protection matrix, Genesis lift obstruction :: `[ALG]`

**ATLAS revision artifacts (v6.4.20):**
- [RID: DYAD-ART-ATLAS-P1] `[v6.4.20; RID registered at adoption, 21 Oct 2026]` :: `build_dyad_p1.py`, `check_dyad_p1.py`, `dyad_p1_math_checks.py`; records `DYAD_ATLAS_P1_SCIENTIFIC_CORRECTION_SESSION_v0_1.md`, `DYAD_FC32_HNG_R9FREE_SESSION_v0_1.md` (project `claude/atlas/p1/`) :: P1 working-file builder, gates G0–G13, checks P1-1–P1-5; reviewer replay recorded in the P1 review :: `[ENG]`
- [RID: DYAD-ART-ATLAS-P2] `[v6.4.20; RID registered at adoption, 21 Oct 2026]` :: `build_dyad_v6_4_20_r1.py` with `p2_content.py`, `check_dyad_v6_4_20_r1.py`; r2: `build_dyad_v6_4_20_r2.py`, `check_dyad_v6_4_20_r2.py`; `dyad_p2_math_checks.py` (M1–M11), `p2_source_checks.py` (S1–S4); record `DYAD_ATLAS_P2_EDITORIAL_INTERFACE_SESSION_v0_1.md` (project `claude/atlas/p2/`) :: the v6.4.20 drafts: builders, gates, owner math and source checks; r1 and r2 packages replayed by the external reviewer (21 Oct 2026; r2: G0–G21, the r2 negative controls, M1–M11, S1–S4 with C1–C2, R1–R4 with D1–D2), as recorded at adoption :: `[ENG]`

---

## §9. Collaboration and Provenance {#sec-9-provenance}

**Principal investigator:** Mustafa  
**AI / collaborator roles:** Claude · ChatGPT · Gemini · Grok  
**Archive:** Zenodo DOI 10.5281/zenodo.17568897  
**Repository:** `rtg-resonance-2025`

**v6.4.10 review-completion record (24 Sep 2026):** draft r1 → r2 (C01–C08 applied) → r3 (final text patch) → external r3 disposition "scientifically review-complete for this scoped revision; no remaining release blocker"; adopted by the PI. Reviewer-held identities: r3 SHA-256 `4ef13741cb1212d0…`, v6.4.9→r3 diff `aed6a27193cc74fa…` (246 lines; r2→r3 72 lines). The adopted text differs from r3 only by the adoption metadata, the removal of "proposed" from the $E_{\rm odd}$ diagnostic definition, one editorial micro-edit in §1, and the manifest reference.

**v6.4.10 adoption note:** the local return-enclosure package (§6.14) was produced by an explicit audit→certificate→independent-review cycle: a P0–P1 normalization audit (ChatGPT) corrected the owner registry label of `jet1_deg5.json` and separated three operations previously conflated as "normalization"; exact-rational contraction/inverse/remainder certificates (ChatGPT, producer + validator) were sharpened twice by inserting exact signed jet degrees before majorization (a reviewer proposal), and each version was independently reconstructed and verified (Claude, three review records + exit-coded referee). Errors were caught on both sides and recorded (reviewer: vector-vs-radial tail degree, seed margin, omitted finite defect $D_{\rm poly}$, tail-share accounting, check count; producer: an undocumented constant set, withdrawn). Method note: **retain exact signed jet degrees, majorize only the tail** (P2-A v1→v2: $9\times$ domain; P2-B v1→v2: $80\times$ constant) and **always bound the finite conjugacy defect separately from the raw tail**.

**v6.4.9 closure note:** the $q=4,(0,3)$ all-$p$ theorem (DYAD-THM-Q403-PHASELAW) was closed collaboratively — degree-counting diagnosis (insertion depth $\le2$) and the three-path enumeration narrowed a stalled symbolic fit to a closed form; independent cross-checks against the certified in-field extractor confirm it reproduces the actual cascade object. Method note: the closure technique (degree-bound → finite charge-path enumeration → cyclotomic/collapse identity) is the same shape as the $b=5$ all-$p$ closure (cyclotomic non-division, DYAD-OPEN-B5-ALLP) — a twice-validated reusable strategy for all-$p$ frontiers.

---

## Appendix A — Version History {#appendix-a}

### v6.4.20 — adopted 21 October 2026

- **Owner decision:** explicit PI adoption, 21 Oct 2026 ("Ben onaylıyorum", 18:14 +03:00), recorded as `DYAD v6.4.20 — OWNER ADOPTION AUTHORIZED`. It follows the external review `DYAD v6.4.20 DRAFT r2 — REVIEW ACCEPTED` of DRAFT r2 (`f2030f853b94a7caa1d1d7c4afd8bdf9b6059582d331100bb0033226fd68465e`). Review acceptance and owner adoption are separate decisions.
- **Chain:** v6.4.19 (`40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`) → ATLAS P1 working file (`6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905`; `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED`) → DRAFT r1 (`a5c70f5b1468ab01ba1cdf932fb9205c4bf00976a2b6523e8b90210e5e457c4a`; `v6.4.20 r1 — REVIEW ACCEPTED WITH MINOR CORRECTIONS`) → DRAFT r2 (`f2030f853b94a7caa1d1d7c4afd8bdf9b6059582d331100bb0033226fd68465e`; `DYAD v6.4.20 DRAFT r2 — REVIEW ACCEPTED`) → this file by `release_v6_4_20.py` (labels and metadata only; 55 lines replaced in place, quoted below).
- **Registered by this adoption (13 RIDs):** `DYAD-ALG-KP-FRAME-SCALE`, `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`, `DYAD-ALG-B5-ALLP-NONVANISHING`, `DYAD-ALG-RAW-ANGULAR-MEAN`, `DYAD-ALG-ONE-BLOCK-BURST`, `DYAD-ALG-P5-RADIAL`, `DYAD-ALG-SIXSTEP-CUBIC-JET`, `DYAD-ALG-Q3-DEG2-CANCEL`, `DYAD-DEF-CRITICAL-CURVE`, `DYAD-ALG-QC-CRITICAL-AMPLITUDE`, `DYAD-ALG-ISP-MAPS`, `DYAD-ART-ATLAS-P1`, `DYAD-ART-ATLAS-P2`. Census A (tagged identifiers): v6.4.19 135 → v6.4.20 148; every v6.4.19 identifier is kept.
- **Unchanged:** every earlier statement, grade, scope and OPEN status. OPEN 20 PARTIAL (B-∞ existence and flat uniqueness CLOSED; B-an and B-6 OPEN); OPEN 9 PARTIAL.
- **Kept distinctions:** FA-08 — the `DYAD-THM-RAW-CUBIC` formula is verified, its direct match with the historical OPEN 9 source is not complete. FA-04 — `degree_b_vanishing_cert_v2.py` is not available and is not presented as recreated. FC-32 (H-NG) stays a SESSION result and is not imported. Editions without a recorded hash (Triadic, OPEN-M, Programme, Methodology, DZT, AZ) stay "not recorded".
- **Evidence levels:** `REVIEWER-REPLAYED` — r2 review: r2 G0–G21, the r2 negative controls, M1–M11, S1–S4 with C1–C2 (with the RECOG v0.3.20/v0.3.21/v0.3.22 files), R1–R4 with D1–D2; r1 review: r1 hashes, builder, G0–G18, N0–N16, K1–K3. `OWNER-RUN` — this release transform and its release checker with negative controls. `REVIEWER FULL REPLAY NOT COMPLETED` — the combined G14–G15 run carried from v6.4.19 (a separate historical item, not closed by the v6.4.20 reviews); the release checker of this edition until it is replayed. The release-record hashes in the v6.4.17/v6.4.18 addenda v0.1.1 are `REVIEWER-MEASURED` (r1 review), not owner-measured.
- **Outbound:** N16–N20 (ATLAS disposition §6) are prepared only after external verification of this file's SHA-256 and are sent by the PI. No notice is sent by this release.

#### v6.4.20 adoption — replaced DRAFT r2 lines (verbatim)

**r2 line 4**

> **Edition:** v6.4.20 DRAFT r2 — 21 October 2026  

**r2 line 5**

> **Status:** DRAFT r2 — not adopted, not released. Adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19` (SHA-256 `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`) remains the canonical Dyadic ledger until a separate external review and an explicit PI adoption decision. r1 built by `build_dyad_v6_4_20_r1.py` from the verified ATLAS P1 working file (SHA-256 `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905`) under `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED` (P2 authorized, 21 Oct 2026); r2 = r1 with the record corrections of the r1 review (`TECHNICAL REVIEW PASSED — MINOR RECORD CORRECTIONS REQUIRED`), built by `build_dyad_v6_4_20_r2.py`.  

**r2 line 7**

> **Supersedes (on adoption only):** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19`. Lineage and all release records: Appendix A.  

**r2 line 11**

> **Status summary:** The dyad map has theorem-grade and exact-algebraic certification for the six-step resonant module ($c_{21}$, the local quintic normalization pipeline, OPEN 11, OPEN 18); the local return enclosure of §6.14 (exact degree-6 normalizer and jet, primitive contraction with invariant tube, inverse coordinates, normalized remainders); the OPEN 3 spiral-residual results and the primitive-variable remainder (OPEN 21; conditional on `RECOG-THM-R9-MEMORY`); the L-PHASE angular remainder on row A (`[THM]`; the constant $\tfrac{403}{250}$ is an upper bound); the formal centralizer and ℤ₆ generator (§6.16); Lemma F with F1–F3 and the smooth flow embedding (§6.17). OPEN 9 is PARTIAL: low-degree anti-holomorphic vanishing is `[ALG]` for $b\in\{2,3,4\}$ ($p\ge b+2$), it fails at $b=5$ for every $p\ge6$, all-$b\ge5$ persistence is `[OPEN]`, and the $q=4,(0,3)$ phase law is closed for all $p$. OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-an and B-6 are OPEN. This draft adds the ATLAS P1 scientific corrections and the P2 interface work (Appendix A). Proposed RIDs are registered only on adoption; no adopted RID is renamed or regraded.  

**r2 line 12**

> **Draft record:** Appendix A, "v6.4.20 DRAFT r2" and "v6.4.20 DRAFT r1"; session records `DYAD_ATLAS_P2_R2_CORRECTION_SESSION_v0_1.md` and `DYAD_ATLAS_P2_EDITORIAL_INTERFACE_SESSION_v0_1.md`. The v6.4.19 header, adoption metadata, release summaries and footers are preserved verbatim there.

**r2 line 60**

> **Version markers.** `[v6.4.20]` marks text introduced by the ATLAS P1 and P2 passes (the P1 working file wrote these as P1 markers). `[v6.4.20 entry]` marks a whole new entry; a proposed RID carries `[v6.4.20; proposed RID, registered only at adoption]`.

**r2 line 254**

> - Channel boundary all-$p$ (DYAD-OPEN-B5-ALLP): **CLOSED `[ALG]`**. `[v6.4.20: result RID proposed, DYAD-ALG-B5-ALLP-NONVANISHING (§6.11); the lifecycle identifier is unchanged]` For $p\ge13$, $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{\rm eff}$ with $S_{\rm eff}/S=N/D$, $N=2\lambda^6+\lambda^5-5\lambda^4-3\lambda^3-4\lambda^2+2\lambda+1$. Cyclotomic non-division: $\deg N=6$ so $\Phi_p\mid N$ requires $\varphi(p)\le6$ (finite set); exact check shows $\Phi_p\nmid N$ for all, so $N(\lambda_p)\ne0$ for all $p$, hence $S_{\rm eff}\ne0$ for all $p\ge13$. With the exact sweep $p=6..12$: $F_{\rm raw}^p(0,5)\ne0$ for ALL $p\ge6$. Remaining (separate): all-$b\ge5$ persistence and the general-coefficient version: `[OPEN]`

**r2 line 481**

> `[DEF]` `[v6.4.20 entry; proposed RID, registered only at adoption]` [RID: DYAD-DEF-CRITICAL-CURVE] **Critical curve (rank-one locus).** $C_0:=\{\det DT=0\}=\{1+(e^\rho-1)\cos\eta=0\}$. Because $|\cos\eta|\le1$, this is the set described in the next entry ($\rho\ge\ln2$). On $C_0$ the kernel of $DT$ is spanned by $k=(\cos\eta,1)$, since $DT\,k=(0,\det DT)$ identically; RECOG-ALG-P2-C0-WHITNEY-FOLD uses this direction. Owner check M2.

**r2 line 532**

> `[ALG]` [RID: DYAD-ALG-ISP-MAPS] `[v6.4.20; proposed RID, registered only at adoption; covers the forward map and the reconstruction below; owner check M4]` **Forward map:**

**r2 line 545**

> `[ALG]` [RID: DYAD-ALG-QC-CRITICAL-AMPLITUDE] `[v6.4.20; proposed RID, registered only at adoption; owner check M3]` **Critical ISP amplitude:** $Q_c := (\arcsin(\ln 2))^2 \approx 0.5865$. If $Q < Q_c$ at pre-crossing, critical curve is unreachable at the crossing step.

**r2 line 553**

> `[ALG]` `[scope: fixed-radius uniform-angle mean in the raw $W$-frame]` [RID: DYAD-ALG-RAW-ANGULAR-MEAN] `[v6.4.20; proposed RID, registered only at adoption; owner check M8]` **Raw angular-mean recurrence coefficient.** Define

**r2 line 563**

> `[ALG]` [RID: DYAD-ALG-ONE-BLOCK-BURST] `[v6.4.20; proposed RID, registered only at adoption; owner check M7]` **One-block burst on the positive real primitive ray** $(\rho,\eta)=(t,0)$, $t>0$, $Q_0=t^2$:

**r2 line 607**

> `[ALG]` [RID: DYAD-ALG-SIXSTEP-CUBIC-JET] `[v6.4.20; proposed RID, registered only at adoption; covers the jet and M+M^T=-I; owner check M5]` **6-step cubic jet** in primitive $(\rho,\eta)$ coordinates:

**r2 line 663**

> `[ALG]` [RID: DYAD-ALG-KP-FRAME-SCALE] `[v6.4.20; proposed RID, registered only at adoption]` `[proof: exact algebra; `dyad_p1_math_checks.py` P1-1]` **Frame qualifier for the bridge lemma.** The lemma holds in each linear eigenframe for that frame's one-step coefficient. For the declared $K_p$ family the two frames in use are $Z$ ($\eta=Z+\bar Z$, $\rho=uZ+\bar u\bar Z$, $u=1/(1-\lambda)$; RECOG) and $W_p=\rho+\tfrac{\lambda-1}{K_p}\eta$ (Dyadic; the §1 frame at $p=6$). Since $\bar u+\tfrac{\lambda-1}{K_p}=0$ and $u=\tfrac12+\tfrac i2\cot(\pi/p)$,

**r2 line 702**

> `[ALG]` (all $p$, complete) [RID: DYAD-ALG-B5-ALLP-NONVANISHING] `[v6.4.20; proposed RID for the b=5 statement (F_raw^p(0,5) != 0 for every p >= 6), registered only at adoption; the lifecycle identifier DYAD-OPEN-B5-ALLP is unchanged]` **Channel classification boundary at $b=4$ (dyadic map).** Universal pure anti-holomorphic vanishing (for $p\ge b+2$) holds for $b\in\{2,3,4\}$ `[ALG]` (source $\beta$-sets carry no secular mode; exceptional orders bounded by $b+1$), and FAILS at $b=5$ for EVERY $p\ge6$ `[ALG]`. Proof of the $b=5$ failure: the $(0,5)$ source carries the secular mode $\beta=1$ with five-term coefficient $S\propto c_{02}^2$ (nonzero `[ALG]`). For $p=6..12$, exact cyclotomic certificates give $F_{\rm raw}^p(0,5)\ne0$ in $\mathbb{Q}(\zeta_p)$ `[ALG]` `[scope: finite sweep]` (e.g. $F_{\rm raw}^7(0,5)=\tfrac{15}{2}\lambda^5+\tfrac{23}{8}\lambda^4+\tfrac{21}{8}\lambda^3+\tfrac{15}{2}\lambda^2-\tfrac18\lambda+\tfrac{17}{2}$). For $p\ge13$, all nonsecular $m=0$ modes vanish (geometric sums, $p\nmid(\beta-1)$ for $\beta-1\in\{-6,\dots,-1,1\}$) and the polynomial mode $(-2,1)$ has exact sum $-p/(1-\lambda^{-3})$, giving the exact identity $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{\rm eff}$, $S_{\rm eff}=S-c_{(-2,1)}/(1-\lambda^{-3})$. The effective ratio is the explicit rational $S_{\rm eff}/S=N/D$ with $N=2\lambda^6+\lambda^5-5\lambda^4-3\lambda^3-4\lambda^2+2\lambda+1$ ($\lim_{\lambda\to1}=3$, `[ALG]`). Since $\deg N=6$, a primitive $p$-th root can be a zero of $N$ only if $\varphi(p)\le6$ (finitely many $p$: $\{1..10,12,14,18\}$); exact division shows $\Phi_p\nmid N$ for every one, so $N(\lambda_p)\ne0$ for all $p$, hence $S_{\rm eff}\ne0$ for all $p\ge13$. Therefore $F_{\rm raw}^p(0,5)\ne0$ for ALL $p\ge6$ `[ALG]` (complete proof, not a finite scan). Net `[ALG]` for the dyadic map: **universal pure anti-holomorphic raw vanishing holds for $b\in\{2,3,4\}$ and first fails at $b=5$, for every $p\ge6$.** Whether it fails for every $b\ge6$ is `[OPEN]` (all-$b\ge5$ persistence; scan-confirmed $b=6$ only), as is the general-coefficient version. `[COR]` `[v6.4.11]` The former wording "holds iff $b\le4$" asserted the open $b\ge6$ direction and is withdrawn. [cert: rtg_b5_Seff_limit_cert.py (all-$p$ closure); exact_Fraw_b5_sweep.py ($p=6..12$); rtg_b5_step3_reduction.py; rtg_extract_b5_secular_coeff.py (source)]

**r2 line 711**

> - [RID: DYAD-ALG-Q3-DEG2-CANCEL] `[v6.4.20; proposed RID, registered only at adoption; evidence rtg_p_certs.py (DYAD-ART-P-CERTS), not rerun in P2]` Degree-2 $q=3,(0,2)$ cancellation for all $p>3$ with $3\mid p$.

**r2 line 815**

> `[ALG]` `[v6.4.20 entry; proposed RID, registered only at adoption]` [RID: DYAD-ALG-P5-RADIAL] **Degree-five radial part of the six-step return.** In primitive coordinates $Q(T^6x)-Q=-Q^2+P_5+O(\|x\|^6)$ with $P_5=\tfrac{Q}{24}(5\eta^3-43\eta^2\rho+4\eta\rho^2-5\rho^3)$, $Q=\rho^2-\rho\eta+\eta^2$; the quadratic and cubic parts vanish. This registers as a result the identity used inside `DYAD-THM-PRIM-CTR` below; no statement changes. Owner check M6.

**r2 line 1066**

> `[THM]` [RID: DYAD-THM-SMOOTH-EQUIVARIANT-CHART] `[v6.4.20; proposed RID, registered only at adoption]` `[corollary of DYAD-THM-SMOOTH-EMBEDDING E3–E4; proof: finite-group averaging]` **Smooth equivariant chart.** Let $J$ be the $C^\infty$ germ of E4 ($J^6=\mathrm{id}$, $DJ(0)=A$, $JT=TJ$) and $\Phi:=\tfrac16\sum_{k=0}^{5}A^{-k}J^k$. Then $\Phi$ is a $C^\infty$ local diffeomorphism with $\Phi(0)=0$, $D\Phi(0)=I$, $\Phi\circ J=A\circ\Phi$, and $N_\Phi:=\Phi T\Phi^{-1}$ commutes with $A$.  

**r2 line 1087**

> `[DEF]` `[v6.4.20]` One table of the editions this ledger uses. A hash marked "project copy hashed by DYAD" was computed from the project file for this draft; "not recorded" means this ledger carries no hash for that edition.

**r2 line 1091**

> | Dyadic (this ledger) | v6.4.19 | ADOPTED 20 Oct 2026; canonical until a v6.4.20 adoption decision | `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9` | release record; verification record | base of P1/P2 |

**r2 line 1092**

> | Dyadic ATLAS P1 working file | v6.4.20 P1 | noncanonical; reviewed (`ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED`) | `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905` | P1 record; reviewer hash check | base of this draft |

**r2 line 1141**

> `[DEF]` `[v6.4.20]` One recipient per row. "Where recorded" names the consumer record read for this draft; "NOT RECORDED" means no receipt was found there, not that the notice was refused. Notices N16–N20 (ATLAS disposition §6) are issued only after adoption; none is prepared in this draft.

**r2 line 1261**

> - [RID: DYAD-ART-ATLAS-P1] `[v6.4.20; proposed RID, registered only at adoption]` :: `build_dyad_p1.py`, `check_dyad_p1.py`, `dyad_p1_math_checks.py`; records `DYAD_ATLAS_P1_SCIENTIFIC_CORRECTION_SESSION_v0_1.md`, `DYAD_FC32_HNG_R9FREE_SESSION_v0_1.md` (project `claude/atlas/p1/`) :: P1 working-file builder, gates G0–G13, checks P1-1–P1-5; reviewer replay recorded in the P1 review :: `[ENG]`

**r2 line 1262**

> - [RID: DYAD-ART-ATLAS-P2] `[v6.4.20; proposed RID, registered only at adoption]` :: `build_dyad_v6_4_20_r1.py` with `p2_content.py`, `check_dyad_v6_4_20_r1.py`; r2: `build_dyad_v6_4_20_r2.py`, `check_dyad_v6_4_20_r2.py`; `dyad_p2_math_checks.py` (M1–M11), `p2_source_checks.py` (S1–S4); record `DYAD_ATLAS_P2_EDITORIAL_INTERFACE_SESSION_v0_1.md` (project `claude/atlas/p2/`) :: this draft: builders, gates, owner math and source checks; r1 package replayed by the external reviewer (21 Oct 2026), r2 OWNER-RUN :: `[ENG]`

**r2 line 2351**

> `[DEF]` `[v6.4.20]` One row per result or definition identifier carried by this ledger (adopted and proposed). Evidence levels are kept apart: **OWNER-RUN** (run by the Dyadic owner), **REVIEWER-REPLAYED** (rerun by an external reviewer), **REVIEWER FULL REPLAY NOT COMPLETED** (named runs a reviewer did not finish). "not recorded" means this ledger carries no record; an absent attachment is recorded as absent, not inferred. "Written proof" is the section of the entry. P2 checks M1–M11 are in `dyad_p2_math_checks.py` (OWNER-RUN, 21 Oct 2026; REVIEWER-REPLAYED from the r1 package, 21 Oct 2026 — the same script rerun, not a second method). `[v6.4.20]` (r2) **Grade rule:** the grade is the grade tag governing the identifier's canonical RID tag (the nearest grade tag before it on that line, otherwise the first after it; for a list item without a grade tag, the grade of the list's lead-in line); proposed identifiers read "— proposed, not adopted". `DYAD-CAND-FLAT-CENTRALIZER` and `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` carry `[THM]` since the v6.4.13 adoption decision; their identifiers were kept. **Scope rule:** the scope span of the entry, or a stated split where the entry has parts of different coverage.

**r2 line 2359**

> | `DYAD-ALG-B5-ALLP-NONVANISHING` | ALG — proposed, not adopted | all $p\ge6$: $6\le p\le12$ by exact cyclotomic certificates (finite part); $p\ge13$ by algebraic proof ($\Phi_p\nmid N$) | §6.11 | `rtg_b5_Seff_limit_cert.py`, `exact_Fraw_b5_sweep.py`, `rtg_b5_step3_reduction.py` | not recorded | exact cyclotomic | all $p\ge6$ |

**r2 line 2366**

> | `DYAD-ALG-ISP-MAPS` | ALG — proposed, not adopted | as stated at the entry | §6.4 | P2 M4 | `dyad_p2_math_checks.py` | SymPy exact | forward map and reconstruction |

**r2 line 2367**

> | `DYAD-ALG-KP-FRAME-SCALE` | ALG — proposed, not adopted | as stated at the entry | §6.9 | P1 math checks | `dyad_p1_math_checks.py` | SymPy | declared $K_p$ family |

**r2 line 2373**

> | `DYAD-ALG-ONE-BLOCK-BURST` | ALG — proposed, not adopted | as stated at the entry | §6.5 | P2 M7 | `dyad_p2_math_checks.py` | exact rational jets | positive real ray |

**r2 line 2376**

> | `DYAD-ALG-P5-RADIAL` | ALG — proposed, not adopted | as stated at the entry | §6.14 | P2 M6 | `dyad_p2_math_checks.py` | exact rational jets | degrees 2–5 |

**r2 line 2381**

> | `DYAD-ALG-Q3-DEG2-CANCEL` | ALG — proposed, not adopted | as stated at the entry | §6.11 | `rtg_p_certs.py` (DYAD-ART-P-CERTS) | not recorded | SymPy/cyclotomic | all $p>3$, $3\mid p$ |

**r2 line 2382**

> | `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | ALG — proposed, not adopted | as stated at the entry | §6.4 | P2 M3 | `dyad_p2_math_checks.py` | SymPy | value to 4 d.p. |

**r2 line 2383**

> | `DYAD-ALG-RAW-ANGULAR-MEAN` | ALG — proposed, not adopted | scope: fixed-radius uniform-angle mean in the raw $W$-frame | §6.5 | P2 M8 | `dyad_p2_math_checks.py` | exact rational jets | raw fixed-radius mean |

**r2 line 2384**

> | `DYAD-ALG-SIXSTEP-CUBIC-JET` | ALG — proposed, not adopted | as stated at the entry | §6.7 | P2 M5 | `dyad_p2_math_checks.py` | exact rational jets | cubic order |

**r2 line 2393**

> | `DYAD-DEF-CRITICAL-CURVE` | DEF — proposed, not adopted | as stated at the entry | §6.1 | P2 M2 | `dyad_p2_math_checks.py` | SymPy exact | full statement |

**r2 line 2414**

> | `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | THM — proposed, not adopted | as stated at the entry | §6.17 | P1 SESSION derivation | `dyad_p1_math_checks.py` (linear part) | SymPy | $C^\infty$ germs |

**r2 line 2422**

> | `DYAD-ALG-B5-ALLP-NONVANISHING` | historical (v6.4.7) | not recorded | not recorded | not recorded | proposed RID; all-$b\ge5$ OPEN |

**r2 line 2429**

> | `DYAD-ALG-ISP-MAPS` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M4 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | proposed RID |

**r2 line 2430**

> | `DYAD-ALG-KP-FRAME-SCALE` | P1 | reviewer general-angle algebraic check | — | yes (reviewer) | proposed RID |

**r2 line 2436**

> | `DYAD-ALG-ONE-BLOCK-BURST` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M7 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | proposed RID |

**r2 line 2439**

> | `DYAD-ALG-P5-RADIAL` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M6 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | proposed RID |

**r2 line 2444**

> | `DYAD-ALG-Q3-DEG2-CANCEL` | historical | not recorded | not recorded | not recorded | proposed RID; not rerun in P2 |

**r2 line 2445**

> | `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M3 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | proposed RID |

**r2 line 2446**

> | `DYAD-ALG-RAW-ANGULAR-MEAN` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M8 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | proposed RID; long-orbit identification OPEN |

**r2 line 2447**

> | `DYAD-ALG-SIXSTEP-CUBIC-JET` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M5 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | proposed RID |

**r2 line 2456**

> | `DYAD-DEF-CRITICAL-CURVE` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M2 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | proposed RID |

**r2 line 2477**

> | `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | P1 | reviewer ACCEPT `[THM — SESSION]` (FB-13) | — | reviewer check of the averaging argument | proposed RID; analyticity OPEN |

**r2 line 2483**

> `[DEF]` `[v6.4.20]` Every Dyadic-pattern string printed in DZT v0.8 (§7) and AZ v0.6 (§§4.1, 8), classified. Classes: exact match; component of `DYAD-THM-Q403-PHASELAW`; historical note label; artifact; unmatched. No alias is created by this table; consumer repins are requested after adoption (planned notice N17).

**r2 line 2487**

> | DZT v0.8 §7 | DYAD-OPEN-B5-ALLP | exact match | `DYAD-OPEN-B5-ALLP` (closed lifecycle item, untagged in this ledger) | result RID proposed: `DYAD-ALG-B5-ALLP-NONVANISHING` |

**r2 line 2509**

> | AZ v0.6 §8 | DYAD-ALG-Q3-CANCEL | unmatched | statement = the degree-2 $q=3,(0,2)$ cancellation (§6.11 micro-certification, no RID in v6.4.19) | proposed `DYAD-ALG-Q3-DEG2-CANCEL` covers the statement; no alias is created; AZ may repin after adoption |

**r2 line 2515**

> `[DEF]` `[v6.4.20]` Every v6.4.19 heading and its place in this draft. Anchors are kept. Relocated text is listed in Appendix A (H-P2-*).

**r2 line 2517**

> | v6.4.19 | v6.4.20 DRAFT r2 (headings as in r1) | Change |

**r2 line 2547**

> | `## Appendix A — Version History {#appendix-a}` | `## Appendix A — Version History {#appendix-a}` | v6.4.20 DRAFT r2 and r1 records added; P1 record and older history retained |

**r2 line 2560**

> *END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.20 DRAFT r2*  

**r2 line 2561**

> *DRAFT r2, 21 October 2026 — not adopted, not released. Adopted v6.4.19 (`40c9e63f…6ec9`) remains canonical. The r1 footer and every other replaced r1 line are quoted verbatim in Appendix A (v6.4.20 DRAFT r2 record); the v6.4.19 and inherited footers remain in the r1 record (H-P2-12).*

### v6.4.20 DRAFT r2 — 21 October 2026 (draft record; not adopted)

- **Base:** v6.4.20 DRAFT r1, SHA-256 `a5c70f5b1468ab01ba1cdf932fb9205c4bf00976a2b6523e8b90210e5e457c4a` (unchanged; reviewed).
- **Authority:** external r1 review of 21 Oct 2026, `TECHNICAL REVIEW PASSED — MINOR RECORD CORRECTIONS REQUIRED`; final line `v6.4.20 r1 — REVIEW ACCEPTED WITH MINOR CORRECTIONS`. P2 technical replay PASS; scientific scope transfer ACCEPT; Appendix E consistency MINOR CORRECTION REQUIRED. This is not an adoption decision.
- **Scope of r2 (limited to the review items):** C1 three Appendix E.1 rows and the grade/scope rule (new checker gate G19); C2 `|` inside math in live table rows (G21); C3 reviewer replays recorded as REVIEWER-REPLAYED; C4 edition markers; C5 this record. No theorem, statement, grade in §1–§9, OPEN status or RID is changed. The full release-record hashes measured by the reviewer go to the addenda v0.1.1, not to this ledger.
- **Official state unchanged:** v6.4.19 adopted; OPEN 20 PARTIAL (B-an, B-6 OPEN). No notice is sent; N16–N20 follow a release.

**E.1 corrections (C1).** The three rows named by the review are `DYAD-ALG-B5-ALLP-NONVANISHING` (scope split: finite certificate range and all-$p$ algebraic proof), `DYAD-CAND-P0-DYADIC` (grade `[CAND]`, conditional; its exact arithmetic sub-results stay under `DYAD-ALG-P6-FACEFLUX`) and `DYAD-ALG-Q3-DEG2-CANCEL` (grade `[ALG]`, proposed, not adopted; source script not rerun in P2). The other rows below change only by the "proposed, not adopted" suffix.

| RID | r1 Grade | r2 Grade | r1 Scope | r2 Scope |
|---|---|---|---|---|
| `DYAD-ALG-B5-ALLP-NONVANISHING` | ALG | ALG — proposed, not adopted | scope: finite sweep | all $p\ge6$: $6\le p\le12$ by exact cyclotomic certificates (finite part); $p\ge13$ by algebraic proof ($\Phi_p\nmid N$) |
| `DYAD-ALG-ISP-MAPS` | ALG | ALG — proposed, not adopted | as stated at the entry | as stated at the entry |
| `DYAD-ALG-KP-FRAME-SCALE` | ALG | ALG — proposed, not adopted | as stated at the entry | as stated at the entry |
| `DYAD-ALG-ONE-BLOCK-BURST` | ALG | ALG — proposed, not adopted | as stated at the entry | as stated at the entry |
| `DYAD-ALG-P5-RADIAL` | ALG | ALG — proposed, not adopted | as stated at the entry | as stated at the entry |
| `DYAD-ALG-Q3-DEG2-CANCEL` | — | ALG — proposed, not adopted | as stated at the entry | as stated at the entry |
| `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | ALG | ALG — proposed, not adopted | as stated at the entry | as stated at the entry |
| `DYAD-ALG-RAW-ANGULAR-MEAN` | ALG | ALG — proposed, not adopted | scope: fixed-radius uniform-angle mean in the raw $W$-frame | scope: fixed-radius uniform-angle mean in the raw $W$-frame |
| `DYAD-ALG-SIXSTEP-CUBIC-JET` | ALG | ALG — proposed, not adopted | as stated at the entry | as stated at the entry |
| `DYAD-CAND-P0-DYADIC` | ALG | CAND | scope: inherited | conditional h-transfer (h-source bridge OPEN in OPEN-M); exact sub-results are not part of this row: face-flux identity and R11 factor $3/4$ under `DYAD-ALG-P6-FACEFLUX` `[ALG]`; threshold $0.024$ `[HYP]` inherited |
| `DYAD-DEF-CRITICAL-CURVE` | DEF | DEF — proposed, not adopted | as stated at the entry | as stated at the entry |
| `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | THM | THM — proposed, not adopted | as stated at the entry | as stated at the entry |

**Table repairs (C2).** 6 live table rows; inside `$…$` the bar `|` is written `\vert` and `\|` is written `\Vert`. The mathematics is unchanged. Appendix A quotations are not touched (history stays verbatim).

**Evidence levels after the r1 review.** REVIEWER-REPLAYED (r1 package, clean folder): hashes of v6.4.19, the P1 working file, r1 and the ZIP; ZIP inventory 16/16; deterministic builder byte-for-byte; checker G0–G18 19/19; negative controls N0–N16 17/17; M1–M11 11/11; K1–K3 exit 1; RECOG v0.3.22 and NUMGEN v1.20.8 hashes with content checks S4 and S3; RECOG §7.2 receipt rows N10–N13. OWNER-RUN only: S1 for RECOG v0.3.20/v0.3.21, S2 (v0.3.20 → v0.3.22 paragraph identity), C1–C2, the records check R1–R4 with D1–D2, and everything new in r2. The r2 package carries the source files so that S1/S2 can be replayed. A same-script replay is not a second method; the scientific results keep their own evidence rows.

#### v6.4.20 DRAFT r2 — replaced r1 lines (verbatim)

**r1 line 4** (C4)

> **Edition:** v6.4.20 DRAFT r1 — 21 October 2026  

**r1 line 5** (C4)

> **Status:** DRAFT r1 — not adopted, not released. Adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19` (SHA-256 `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`) remains the canonical Dyadic ledger until a separate external review and an explicit PI adoption decision. Built by `build_dyad_v6_4_20_r1.py` from the verified ATLAS P1 working file (SHA-256 `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905`) under `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED` (P2 authorized, 21 Oct 2026).  

**r1 line 12** (C4)

> **Draft record:** Appendix A, "v6.4.20 DRAFT r1"; session record `DYAD_ATLAS_P2_EDITORIAL_INTERFACE_SESSION_v0_1.md`. The v6.4.19 header, adoption metadata, release summaries and footers are preserved verbatim there.

**r1 line 453** (C2)

> | Spiral residual (§6.14, v6.4.14) | Exact leading terms of $S_Q,S_\Theta$ `[ALG]`; per-block remainder bounds with majorant constants on $|z|\le\tfrac1{20}$, $\tfrac1{40}$ `[THM]` | Reading $K_\Theta,K_Q$ as true-error maxima; identifying $S_Q$ with $P_5$ (cross term $-2qD_3$); primitive asymptotic-phase transfer (P4); equivalence with the historical fit; $C_{\rm est}$/$\kappa_{\rm est}$; transfer to NUMGEN L1 or ISP-angle coefficients (SG-7, SG-19) | §2 OPEN 3, §6.14 |

**r1 line 456** (C2)

> | Primitive-variable phase remainder (§6.14, v6.4.17) | `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`: $|M_W-\mathcal P_2(W_0)|\le K'_jQ_0^{3/2}+C_{2,j}(256/225)^2Q_0^2$ per row ($K'_A=3951/1000$, $K'_B=971/250$); single-constant $K_A=8831/250$, $K_B=883/100$; majorant suprema | An unconditional result (R9 enters through T1 and the memory law); re-certification of R9 or of its $C_2$; reading the `[NUM]` ratio $\approx0.35$ as a proved constant or as absence of higher-order terms; mixing rows; transfer to $C_W^{(h)}$, NUMGEN L1 or ISP-angle coefficients (SG-19); C_est/κ_est (SG-7) | §2 OPEN 21, §6.14 |

**r1 line 457** (C2)

> | L-PHASE angular remainder, row A (§6.14, v6.4.19) | `[THM]`: $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$ for block base points in $U$, $Q_m$ primitive; branch certificate $\varepsilon\le0.04654$ on $U_T$; the constant is the ceiling of a majorant (certificate value $1.61112$; angular supremum of the true error $\to\Lambda^*\approx1.4003$ as $Q\to0$, `[NUM]`) | Optimality of $403/250$; row B ($|z|\le\tfrac1{40}$) or larger domains; a statement beyond the first-order block law; reading $403/250$ or $\Lambda^*$ as a NUMGEN L1/ISP-angle coefficient or as a correction of NUMGEN's measured values (SG-19); discharge of GAP-LOCK angular hypotheses; any $\phi^*$ statement; byte identity with the P2B v2 `certificate.json` (provenance is exact-coefficient and transitive) | §6.14, §7 |

**r1 line 749** (C2)

> | shear/healing ratio $4\sqrt3/3=|\Im\mu|/|\Re\mu|$ | derived from DYAD-THM-C21 | `[ALG]` | ratio of cubic coefficients |

**r1 line 782** (C2)

> | Analytic coordinate | $W_{\rm DSN}=u+iv$, $Q=|W_{\rm DSN}|^2$ — $p=6$ primitive frame |

**r1 line 827** (C2)

> | $|z|\le$ | $|\widehat F(z)-J(z)|\le C_7|z|^7$ | $\|D\widehat F(z)-DJ(z)\|_2\le C_D|z|^6$ |

**r1 line 1262** (C4)

> - [RID: DYAD-ART-ATLAS-P2] `[v6.4.20; proposed RID, registered only at adoption]` :: `build_dyad_v6_4_20_r1.py` with `p2_content.py`, `check_dyad_v6_4_20_r1.py`, `dyad_p2_math_checks.py` (M1–M11), `p2_source_checks.py` (S1–S4); record `DYAD_ATLAS_P2_EDITORIAL_INTERFACE_SESSION_v0_1.md` (project `claude/atlas/p2/`) :: this draft: builder, gates, owner math and source checks; OWNER-RUN only :: `[ENG]`

**r1 line 2165** (C3)

> `[DEF]` `[v6.4.20]` One row per result or definition identifier carried by this ledger (adopted and proposed). Evidence levels are kept apart: **OWNER-RUN** (run by the Dyadic owner), **REVIEWER-REPLAYED** (rerun by an external reviewer), **REVIEWER FULL REPLAY NOT COMPLETED** (named runs a reviewer did not finish). "not recorded" means this ledger carries no record; an absent attachment is recorded as absent, not inferred. "Written proof" is the section of the entry. P2 checks M1–M11 are in `dyad_p2_math_checks.py` (OWNER-RUN, 21 Oct 2026).

**r1 line 2173** (C1)

> | `DYAD-ALG-B5-ALLP-NONVANISHING` | ALG | scope: finite sweep | §6.11 | `rtg_b5_Seff_limit_cert.py`, `exact_Fraw_b5_sweep.py`, `rtg_b5_step3_reduction.py` | not recorded | exact cyclotomic | all $p\ge6$ |

**r1 line 2180** (C1)

> | `DYAD-ALG-ISP-MAPS` | ALG | as stated at the entry | §6.4 | P2 M4 | `dyad_p2_math_checks.py` | SymPy exact | forward map and reconstruction |

**r1 line 2181** (C1)

> | `DYAD-ALG-KP-FRAME-SCALE` | ALG | as stated at the entry | §6.9 | P1 math checks | `dyad_p1_math_checks.py` | SymPy | declared $K_p$ family |

**r1 line 2187** (C1)

> | `DYAD-ALG-ONE-BLOCK-BURST` | ALG | as stated at the entry | §6.5 | P2 M7 | `dyad_p2_math_checks.py` | exact rational jets | positive real ray |

**r1 line 2190** (C1)

> | `DYAD-ALG-P5-RADIAL` | ALG | as stated at the entry | §6.14 | P2 M6 | `dyad_p2_math_checks.py` | exact rational jets | degrees 2–5 |

**r1 line 2195** (C1)

> | `DYAD-ALG-Q3-DEG2-CANCEL` | — | as stated at the entry | §6.11 | `rtg_p_certs.py` (DYAD-ART-P-CERTS) | not recorded | SymPy/cyclotomic | all $p>3$, $3\mid p$ |

**r1 line 2196** (C1)

> | `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | ALG | as stated at the entry | §6.4 | P2 M3 | `dyad_p2_math_checks.py` | SymPy | value to 4 d.p. |

**r1 line 2197** (C1)

> | `DYAD-ALG-RAW-ANGULAR-MEAN` | ALG | scope: fixed-radius uniform-angle mean in the raw $W$-frame | §6.5 | P2 M8 | `dyad_p2_math_checks.py` | exact rational jets | raw fixed-radius mean |

**r1 line 2198** (C1)

> | `DYAD-ALG-SIXSTEP-CUBIC-JET` | ALG | as stated at the entry | §6.7 | P2 M5 | `dyad_p2_math_checks.py` | exact rational jets | cubic order |

**r1 line 2204** (C1)

> | `DYAD-CAND-P0-DYADIC` | ALG | scope: inherited | §6.11 | none | — | — | conditional calibration branch |

**r1 line 2207** (C1)

> | `DYAD-DEF-CRITICAL-CURVE` | DEF | as stated at the entry | §6.1 | P2 M2 | `dyad_p2_math_checks.py` | SymPy exact | full statement |

**r1 line 2228** (C1)

> | `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | THM | as stated at the entry | §6.17 | P1 SESSION derivation | `dyad_p1_math_checks.py` (linear part) | SymPy | $C^\infty$ germs |

**r1 line 2243** (C3)

> | `DYAD-ALG-ISP-MAPS` | P2, 21 Oct 2026 | none | not replayed | no | proposed RID |

**r1 line 2250** (C3)

> | `DYAD-ALG-ONE-BLOCK-BURST` | P2, 21 Oct 2026 | none | not replayed | no | proposed RID |

**r1 line 2253** (C3)

> | `DYAD-ALG-P5-RADIAL` | P2, 21 Oct 2026 | none | not replayed | no | proposed RID |

**r1 line 2259** (C3)

> | `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | P2, 21 Oct 2026 | none | not replayed | no | proposed RID |

**r1 line 2260** (C3)

> | `DYAD-ALG-RAW-ANGULAR-MEAN` | P2, 21 Oct 2026 | none | not replayed | no | proposed RID; long-orbit identification OPEN |

**r1 line 2261** (C3)

> | `DYAD-ALG-SIXSTEP-CUBIC-JET` | P2, 21 Oct 2026 | none | not replayed | no | proposed RID |

**r1 line 2270** (C3)

> | `DYAD-DEF-CRITICAL-CURVE` | P2, 21 Oct 2026 | none | not replayed | no | proposed RID |

**r1 line 2331** (C4)

> | v6.4.19 | v6.4.20 DRAFT r1 | Change |

**r1 line 2339** (C4)

> | `## §5. High-Risk Claims Ledger {#sec-5-high-risk}` | `## §5. High-Risk Claims Ledger {#sec-5-high-risk}` | R11 row conditions (H-P2-7) |

**r1 line 2352** (C4)

> | `### §6.12 Dyad-to-Triad Bridge Export '[ALG]' {#sec-6-12-bridge}` | `### §6.12 Dyad-to-Triad Bridge Export — entry grades: ALG, DEF, CAND, OPEN {#sec-6-12-bridge}` | heading grade tag replaced by the computed entry-grade list |

**r1 line 2353** (C4)

> | `### §6.13 Simulation Invariants and Audit Discipline '[ENG]' {#sec-6-13-audit}` | `### §6.13 Simulation Invariants and Audit Discipline '[ENG]' {#sec-6-13-audit}` | heading grade tag replaced by the computed entry-grade list |

**r1 line 2354** (C4)

> | `### §6.14 Local Return Enclosure — Normalizer, Contraction, Inverse, Remainders '[ALG / THM]' {#sec-6-14-enclosure}` | `### §6.14 Local Return Enclosure — Normalizer, Contraction, Inverse, Remainders — entry grades: ALG, THM, DEF, OPEN, NUM, ENG {#sec-6-14-enclosure}` | heading grade tag replaced by the computed entry-grade list |

**r1 line 2361** (C4)

> | `## Appendix A — Version History {#appendix-a}` | `## Appendix A — Version History {#appendix-a}` | v6.4.20 DRAFT r1 record added; P1 record and older history retained |

**r1 line 2367** (C4)

> | — | `## Appendix E — Claim-to-evidence matrix {#appendix-e}` | new in v6.4.20 |

**r1 line 2374** (C4)

> *END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.20 DRAFT r1*  

**r1 line 2375** (C4)

> *DRAFT r1, 21 October 2026 — not adopted, not released. Adopted v6.4.19 (`40c9e63f…6ec9`) remains canonical. The v6.4.19 footer and the inherited footers are preserved verbatim in Appendix A (v6.4.20 DRAFT r1 record, H-P2-12).*

### v6.4.20 DRAFT r1 — 21 October 2026 (draft record; not adopted)

- **Base:** verified ATLAS P1 working file, SHA-256 `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905` (itself built from adopted v6.4.19 `40c9e63f…6ec9`, unchanged).
- **Authority:** `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED` (reviewer, 21 Oct 2026): P2 authorized; FA-07 and FB-13 candidates kept; no v6.4.19 identifier lost; source pins, receipts, claim-to-evidence matrix and section map completed in this round. External review of this draft and the PI adoption decision are separate.
- **Scope:** disposition items FB-DYAD-09, 10, 11, 14, 16, 17, 18, 20, 22, 23, 24, 26, 27, 28, 29, 30 and the section map. Tier-C items (FC-31, FC-32) are outside this draft.
- **Kept distinctions:** FA-08 — the formula of `DYAD-THM-RAW-CUBIC` is independently verified, its historical-source match is not (source file outside the review package). FA-04 — `degree_b_vanishing_cert_v2.py` is not available and is not presented as recreated. FB-13 is a proposed `[THM]` RID; FC-32 is a SESSION record only.
- **Official state unchanged:** v6.4.19 adopted; OPEN 20 PARTIAL (B-an, B-6 OPEN). No notice is sent.

**Proposed identifiers (registered only at adoption).**

| RID | Grade | Where | Statement | Evidence |
|---|---|---|---|---|
| `DYAD-ALG-KP-FRAME-SCALE` | ALG | §6.9 | $W_p=i\cot(\pi/p)Z$; $\mu_p^Z=\cot^2(\pi/p)\mu_p^{W_p}$ | P1 math checks; reviewer general-angle check (P1 review FA-07) |
| `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | THM | §6.17 | smooth $\Phi$ with $D\Phi(0)=I$, $\Phi J=A\Phi$ | P1 SESSION; reviewer ACCEPT (P1 review FB-13) |
| `DYAD-ALG-B5-ALLP-NONVANISHING` | ALG | §6.11 | $F_{\rm raw}^p(0,5)\ne0$ for every $p\ge6$ (result of the closed lifecycle item DYAD-OPEN-B5-ALLP) | rtg_b5_Seff_limit_cert.py, exact_Fraw_b5_sweep.py (§8); not rerun in P2 |
| `DYAD-ALG-RAW-ANGULAR-MEAN` | ALG | §6.5 | $\mathcal A_{\rm raw}(Q)=Q-Q^2+\tfrac{47}{54}Q^3+O(Q^4)$, $\tfrac{47}{54}=[W^3\bar W^3]\Delta Q_6$ | P2 M8 (exact) |
| `DYAD-ALG-ONE-BLOCK-BURST` | ALG | §6.5 | positive-ray burst $Q_6=Q_0-Q_0^2-\tfrac5{24}Q_0^{5/2}+\tfrac{37}{40}Q_0^3+O(Q_0^{7/2})$ | P2 M7 (exact) |
| `DYAD-ALG-P5-RADIAL` | ALG | §6.14 | $Q(T^6x)-Q=-Q^2+P_5+O(\vert x\vert ^6)$, $P_5=\tfrac{Q}{24}(5\eta^3-43\eta^2\rho+4\eta\rho^2-5\rho^3)$ | P2 M6 (exact) |
| `DYAD-ALG-SIXSTEP-CUBIC-JET` | ALG | §6.7 | six-step cubic jet in $(\rho,\eta)$; $M+M^T=-I$ | P2 M5 (exact) |
| `DYAD-ALG-Q3-DEG2-CANCEL` | ALG | §6.11 | degree-2 $q=3,(0,2)$ cancellation for all $p>3$, $3\mid p$ | rtg_p_certs.py (DYAD-ART-P-CERTS); not rerun in P2 |
| `DYAD-DEF-CRITICAL-CURVE` | DEF | §6.1 | $C_0=\{\det DT=0\}$; kernel direction $(\cos\eta,1)$ | P2 M2 (exact) |
| `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | ALG | §6.4 | $Q_c=(\arcsin\ln2)^2\approx0.5865$ | P2 M3 |
| `DYAD-ALG-ISP-MAPS` | ALG | §6.4 | ISP forward map and reconstruction | P2 M4 (exact) |
| `DYAD-ART-ATLAS-P1` | ENG | §8 | ATLAS P1 builder, checker and math checks | project claude/atlas/p1/ |
| `DYAD-ART-ATLAS-P2` | ENG | §8 | ATLAS P2 builder, checker, math and source checks | project claude/atlas/p2/ |

**RID census.** Census A counts distinct identifiers carried by a RID tag anywhere in the file, multi-identifier tags split. Census B counts distinct RID-shaped Dyadic strings (prefix DYAD- followed by ALG, THM, DEF, OPEN, ART, CAND, NUM or CF) anywhere. v6.4.19: A = 135, B = 136; the B-only strings are `DYAD-ART-B5-LIMIT-CERT`, `DYAD-CAND-PHISTAR-ENTRY-PHASE`, `DYAD-OPEN-B5-ALLP` (a lifecycle identifier that is never tagged, an artifact named only in history, and a string quoted in notice N3 that never existed). The "136 RIDs" of the P1 record is Census B; the P1 gate G1 regex counted first tokens of tags (131). P1: A = 137 (+2 proposed). This draft: A = 148, adding `DYAD-ALG-B5-ALLP-NONVANISHING`, `DYAD-ALG-ISP-MAPS`, `DYAD-ALG-ONE-BLOCK-BURST`, `DYAD-ALG-P5-RADIAL`, `DYAD-ALG-Q3-DEG2-CANCEL`, `DYAD-ALG-QC-CRITICAL-AMPLITUDE`, `DYAD-ALG-RAW-ANGULAR-MEAN`, `DYAD-ALG-SIXSTEP-CUBIC-JET`, `DYAD-ART-ATLAS-P1`, `DYAD-ART-ATLAS-P2`, `DYAD-DEF-CRITICAL-CURVE`. Every P1 identifier remains tagged; every v6.4.19 Census-B string remains present (checker gate G2).

**Anchored edits (stage 1).**

| Edit | Row | Old (SHA-256, 16 hex) | New |
|---|---|---|---|
| P01 | FB-22 | `02bf59ad9ad0b46f` | `ae3eb04da919fb43` |
| P02 | FB-24 | `4d9dcc04f4f46737` | `7af0691c85c42a5b` |
| P03 | FB-24 | `a358c95312cf9a5b` | `58dee5842ebb96d3` |
| P04 | FB-28 | `912ec1ace7e17883` | `840cefae1cfdd2f9` |
| P05 | FB-20 | `7f296e9157bf3a0e` | `0799b9ab20efa806` |
| P06 | FB-27 | `b2d3896d18711239` | `826f668c82c1fdf5` |
| P07 | FB-27 | `0a5478c023b43a8a` | `c3618ee6b0579f24` |
| P08 | FB-27 | `9f43db6b81fb033d` | `e7d0ee5b0d506c75` |
| P09 | FB-10 | `45d85b5b8b6c99d1` | `95617f2699fc633a` |
| P10 | FB-26 | `eaf1011d3e0659ea` | `923d9df3d5991861` |
| P11 | FB-27 | `a32059cb2514d872` | `dbd514805a32f91d` |
| P12 | FB-18 | `d74c29c4fc3dd4c8` | `e4ea22de360536c9` |
| P13 | FB-20 | `8bba2f49e7a5a79f` | `685beca13fb96b78` |
| P14 | FB-28 | `460f2ce8e60cc79e` | `43eca1d6ba860a76` |
| P15 | FB-10 | `9f7f65191150c4c1` | `c69e93a43514133b` |
| P16 | FB-30 | `3cba64fb37fbb36c` | `2264a3852d512917` |
| P17 | FB-22 | `4a4ce34af8905994` | `ecab0c71e5de43c4` |
| P18 | FB-10 | `83c7172bb792ca72` | `ca337611366bb978` |
| P19 | FB-10 | `8a8e8372d2084d8e` | `9015f0614c3a4889` |
| P20 | FB-10 | `af1c0201e18b1a54` | `e77b7470b7dbd7ba` |
| P21 | FB-10 | `c655c73a5897fc06` | `84835b73fd3372e1` |
| P22 | FB-10 | `e79bddb325679c78` | `a8dc696dd52914cb` |
| P23 | FA-04 | `373b10cf7e3a9c44` | `8128c9283dacfac2` |
| P24 | FB-10 | `929da23952ee1b11` | `c67a8a86d4b45328` |
| P25 | FB-20 | `bf328144bc3be633` | `03c7a50536ef81a3` |
| P26 | FB-10 | `de44692f9f3f5728` | `0e36b9d8d30c00b2` |
| P27 | FB-20 | `7d08ec51207d8dde` | `04ecd47633821f82` |
| P28 | FB-10 | `d89ecb12bd053658` | `b9c3592db3f0f665` |
| P29 | FB-18 | `6476d1bd9787264f` | `2d695ed8f6cd2bb7` |
| P30 | FB-14 | `1aaf4d0e233189c3` | `dcdcc656cabed576` |
| P31 | FB-14 | `f40e0098e8d67546` | `6adbcb31c7fa52b6` |
| P32 | FB-16 | `e5745316e3bb90ef` | `a89076167a6c3a21` |
| P33 | FB-26 | `77528ca9f9d4f8b9` | `480f82fc252885cc` |
| P34 | FA-04 | `b3ce8d5871e83056` | `9fd2a1044c9a9514` |
| P35 | FB-10 | `4436c80129e4473d` | `9b2a554b48c5c0f1` |
| P36 | FB-22 | `0a70851dc538d9b4` | `5a0e839d45dba836` |

**Global transforms (stages 2–3).**

| Global transform | Count |
|---|---|
| P1 marker | 39 |
| RID tags converted to code spans | 30 |
| RIDs with a canonical tag | 146 |
| breaker primes | 3 |
| double-escape lines Appendix A | 38 |
| double-escape lines live | 2 |
| tag **`[CLOSED v6.4.9, THM/ALG]`** | 1 |
| tag `[ALG / ENG]` | 1 |
| tag `[ALG candidate]` | 2 |
| tag `[ALG finite sweep]` | 3 |
| tag `[ALG structure / NUM strong]` | 1 |
| tag `[ALG structure]` | 10 |
| tag `[ALG validation]` | 1 |
| tag `[ALG — formal second order; remainder not certified]` | 1 |
| tag `[ALG — formal]` | 2 |
| tag `[ALG, exact under OPEN-P0 representation-phase convention]` | 1 |
| tag `[ALG, exact]` | 16 |
| tag `[CAND/conditional]` | 8 |
| tag `[COR v6.4.10]` | 8 |
| tag `[COR v6.4.11: "iff $b\le4$" shorthand withdrawn]` | 1 |
| tag `[COR v6.4.11]` | 1 |
| tag `[ENG / NUM strong]` | 1 |
| tag `[HYP inherited]` | 1 |
| tag `[NUM strong]` | 4 |
| tag `[P1 COR]` | 3 |
| tag `[THM — analytic]` | 1 |
| tag `[THM — conditional on R9]` | 1 |
| tag `[THM — conditional on RECOG-THM-R9-MEMORY]` | 8 |
| tag `[THM — conditional on T1]` | 1 |
| tag `[THM — conditional]` | 5 |
| tag `[THM/ALG, all-$p$]` | 1 |
| tag `[THM/ALG]` | 3 |
| §6 headings | 17 |
| §6 headings kept (no tagged entries) | 1 |

**Evidence levels for this draft.** OWNER-RUN: builder rebuild, checker gates, `dyad_p2_math_checks.py` M1–M11 with controls K1–K3, `p2_source_checks.py` S1–S4 with controls C1–C2 (all 21 Oct 2026). REVIEWER-REPLAYED: none yet. REVIEWER FULL REPLAY NOT COMPLETED: not applicable before review.

#### v6.4.20 DRAFT r1 relocated text (verbatim from the P1 working file)

**H-P2-1** — origin: title, P1 banner, v6.4.19 header fields, status summary and release summaries v6.4.11–v6.4.19 (lines 1–31 of the P1 working file). Verbatim P1-working-file text:

> # RTG_DYADIC_OSCILLATOR_DSN_v6.4.19
> 
> > **P1 WORKING FILE — noncanonical.** Built from adopted v6.4.19 (SHA-256 `40c9e63f…6ec9`) by `build_dyad_p1.py` under the reviewer decision `P1 — SCIENTIFIC CORRECTION PASS AUTHORIZED` (21 Oct 2026; disposition `ATLAS_DISPOSITION_DYAD_v6_4_19_SESSION_v0_1.md`). Not a draft for adoption and not a release; adopted v6.4.19 remains in force. The header, adoption metadata and footer below are those of v6.4.19 and are not updated in P1 (P2 and the v6.4.20 draft do that). Every P1 change carries `[P1]`; the edit list and the verbatim relocated text are in Appendix A (P1 working record).
> 
> **Title:** RTG Dyadic Oscillator Study — Canonical Scientific Ledger  
> **Date:** 20 October 2026  
> **Status:** ADOPTED — owner/PI adoption recorded 20 October 2026 (`DYAD v6.4.19 — OWNER ADOPTION AUTHORIZED`) after external review of DRAFT r1 (`v6.4.19 r1 — SCIENTIFIC REVIEW ACCEPTED` (`SCIENTIFIC CONTENT ACCEPTED — OWNER ADOPTION READY, WITH REPLAY QUALIFICATION`); r1 SHA-256 `f6211201b95c5a7a5c8d992cdd943e56d3655b9a757cb1b427d72a8fd85d6e47`; no correction to the mathematics or the RID structure; RIDs 132 → 136, none lost; prior grades unchanged; evidence levels kept separate — `REVIEWER-REPLAYED`: draft, draft-package and provenance-package hashes, draft manifest 32/32, deterministic builder, the 11 draft-checker negative controls, provenance gate v0.1.1 main run 9/9 with its 4 internal negative controls; `OWNER-RUN`: combined draft checker 16/16 (including G14 certificate replay and G15 provenance replay), separate negative-control processes M1–M4 (exit 1 each; `lphase_p2b_provenance_control_exits.json` `e2ffa46b…1a1e`), gate JSON `58cfafd3…fc89`, certificate JSON `8697c697…ad4fa`, and the split release replays `replay_g14_certificate.py`, `replay_g15_provenance.py`; `REVIEWER FULL REPLAY NOT COMPLETED`: the combined G14–G15 run and the independent `--record-exit-codes` run (reviewer time limit). NUMGEN receipt replay: certificate JSON byte-identical, same algorithm (not an independent engine)). **Adoption decision (scientific):** `DYAD-THM-LPHASE-ROWA-REMAINDER` `[THM]` at the reviewed DRAFT r1 scope — $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$ for $0<Q_0\le\tfrac1{625}$, $m\ge0$, $Q_m$ the primitive observable, with the branch certificate on $U_T$; NUMGEN interface objects I1–I5 kept; $\tfrac{403}{250}$ is a certified upper bound, not an optimal coefficient. All other scientific results, RID grades and OPEN statuses unchanged; OPEN 20 PARTIAL (B-an, B-6 OPEN). Release edits: draft/proposed labels replaced by adopted labels, release metadata, N15 → PENDING (to be sent only after external verification of the final SHA-256), Appendix A release record, footer. Installation manifest: `RTG_DYADIC_v6_4_19_INSTALL_MANIFEST.json`. Revision base: adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.18` (SHA-256 `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d`), preserved unchanged as the prior adopted release. Session source: `DYAD_NUMGEN_LPHASE_ROWA_CERTIFICATE_SESSION_v0_1.md` (`775c6715…f233d`).  
> **Scope:** The primitive 2D non-symplectic dyad map, its six-step resonant dynamics, ISP crossing geometry, normalized $p$-step structure, and $p$-resonance generalization program.  
> **Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.18`. Scientific lineage: v6.4.18 (adopted 20 Oct 2026) ← v6.4.17 (adopted 19 Oct 2026) ← v6.4.16 (adopted 19 Oct 2026) ← v6.4.15 (adopted 19 Oct 2026) ← v6.4.14 (adopted 19 Oct 2026) ← v6.4.13 (adopted 18 Oct 2026) ← v6.4.12.1 (metadata release of v6.4.12, 17 Oct 2026) ← v6.4.12 (adopted 16 Oct 2026) ← v6.4.11 ← v6.4.10.  
> **Companion documents:** `RTG_PROGRAMME_OVERVIEW_v1.2` · `RTG_ONTOLOGICAL_FOUNDATIONS_v0.9` · `DSN_METHODOLOGY_v1.3` · `dyad_triad_antisymmetric_bridge_v1_1.md` · return-enclosure evidence packages (§8, §6.14). **Consumer editions inspected for v6.4.14 (19 Oct 2026):** `RTG_GENESIS_GEOMETRY_DSN_v2.8.8` (adopted 19 Oct 2026, `9abd3616…0f37`; live pins name DYAD v6.4.13; N8 RECEIVED) · `RTG_RRF_REPRESENTATION_REGISTRY_v0.8.3` (adopted working standard 19 Oct 2026; inspected file `b393657e…a187`; N9 RECEIVED). **Consumer editions inspected for v6.4.13 (18 Oct 2026):** `RTG_GENESIS_GEOMETRY_DSN_v2.8.7` (adopted; pins DYAD v6.4.11, repin deferred) · `RTG_RRF_REPRESENTATION_REGISTRY_v0.8.2` (adopted working standard; N7 receipt) · noncanonical: `GENESIS_DYAD_v6_4_12_1_CONSUMER_IMPACT_NOTE.md`, `FMS_MODEL_SELECTION_LEDGER_v0_5_1_SESSION.md`, `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_7.md`. **Editions inspected in the v6.4.11 synchronization pass and not re-inspected since:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20` (live header: freeze candidate) · `RTG_NUMBER_GENESIS_DSN_v1.20.7` · `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6` · `RTG_OPEN_M_DSN_v0.7.1` · `RTG_RRF_REPRESENTATION_REGISTRY_v0.8` (working standard; reference only)  
> **DSN Methodology:** DSN_METHODOLOGY_v1.3 governs this revision. Scientific-result grades are not changed by methodology migration. Scoped unfinished migration: pre-existing entries retain their v1.2-era spellings except where touched by this revision; full v1.3 conformity of untouched sections is not claimed. **Result-review state:** `[v6.4.19]` payload reviewed as SESSION records on 20 Oct 2026: scope note v0.1 (`L-PHASE SCOPE ACCEPTED — ROW A CERTIFICATION AUTHORIZED`), row-A certificate record v0.1 (`L-PHASE ROW A SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING`), P2B provenance gate v0.1 (`PROVENANCE CHAIN ACCEPTED IN PRINCIPLE — FULL REPLAY NOT VERIFIED`) and v0.1.1 (replay tooling; main gate re-run by the reviewer in the r1 review); NUMGEN interface confirmation (I1–I5 CONFIRMED) and receipt replay; DRAFT r1 reviewed 20 Oct 2026 (`v6.4.19 r1 — SCIENTIFIC REVIEW ACCEPTED` (`SCIENTIFIC CONTENT ACCEPTED — OWNER ADOPTION READY, WITH REPLAY QUALIFICATION`); evidence levels kept separate — `REVIEWER-REPLAYED`: draft, draft-package and provenance-package hashes, draft manifest 32/32, deterministic builder, the 11 draft-checker negative controls, provenance gate v0.1.1 main run 9/9 with its 4 internal negative controls; `OWNER-RUN`: combined draft checker 16/16 (including G14 certificate replay and G15 provenance replay), separate negative-control processes M1–M4 (exit 1 each; `lphase_p2b_provenance_control_exits.json` `e2ffa46b…1a1e`), gate JSON `58cfafd3…fc89`, certificate JSON `8697c697…ad4fa`, and the split release replays `replay_g14_certificate.py`, `replay_g15_provenance.py`; `REVIEWER FULL REPLAY NOT COMPLETED`: the combined G14–G15 run and the independent `--record-exit-codes` run (reviewer time limit). NUMGEN receipt replay: certificate JSON byte-identical, same algorithm (not an independent engine)); owner/PI adoption 20 Oct 2026 with the grade listed in Status. *v6.4.18 record:* `[v6.4.18]` payload reviewed as SESSION records on 19–20 Oct 2026: P1 scope (`SCOPE REVIEW ACCEPTED`), P2-a (`ACCEPT`), P2-b v0.2.1 (`PROOF REVIEW ACCEPTED — P3-a AUTHORIZED`), P3-a v0.1 (`SCIENTIFIC REVIEW ACCEPTED — P3-b AUTHORIZED`), P3-b/c v0.1 (`SCIENTIFIC REVIEW ACCEPTED — FINAL OWNER INTEGRATION AUDIT REQUIRED`; P3C-01/02 applied in v0.1.1), integration audit v0.1 (`SMOOTH EMBEDDING CHAIN ACCEPTED — E2 SCOPE CORRECTION REQUIRED`) and v0.1.1 (E2/L7 correction accepted in the r1 review); DRAFT r1 reviewed 20 Oct 2026 (`v6.4.18 DRAFT r1 — SCIENTIFIC REVIEW ACCEPTED`; manifest 20/20; package draft byte-identical to the uploaded draft; draft checker 13/13; payload check scripts re-executed with their internal negative controls (integration 6/6, P3-a 8/8, P3-b/c v0.1.1 3/3); E2/L7 scope correction of integration audit v0.1.1 accepted; RIDs 129 → 132, none lost; prior grades unchanged; the eight draft-checker negative controls (`--neg`) are owner reruns recorded in the package); owner/PI adoption 20 Oct 2026 with the grade listed in Status. *v6.4.17 record:* `[v6.4.17]` P5 payload reviewed as a SESSION record through three rounds on 19 Oct 2026 (final `P5 v0.1.2 — SCIENTIFIC REVIEW ACCEPTED`; certificate 28/28 replayed with byte-identical JSON; $P_{W2}=-\Delta_2+D\Delta_1[h_2]$ re-derived independently by Laurent polynomials); DRAFT r1 reviewed 19 Oct 2026 (`SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION READY`; draft checker and negative controls re-executed; the P5 negative controls verified from the package records); owner/PI adoption 19 Oct 2026 with the grade listed in Status. *v6.4.16 record:* `[v6.4.16]` payload reviewed as a SESSION record on 19 Oct 2026; DRAFT r1 reviewed 19 Oct 2026 (`SCIENTIFIC AND LIFECYCLE REVIEW ACCEPTED — OWNER ADOPTION READY`). Reviewer-executed: package manifest, rebuild, checker and negative controls, the P2B v2 $h,J$ coefficient comparison with its negative control, the P2B v2 referee, and the P0 numerical comparison. Owner-measured only: the two carried v6.4.10 hashes. Owner/PI adoption 19 Oct 2026. *v6.4.15 record:* `[v6.4.15]` P4 payload reviewed as a SESSION record on 19 Oct 2026 (`P4 SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING`; exact script and rational certificate re-executed, byte-identical JSON); DRAFT r1 reviewed 19 Oct 2026 (`REVIEW ACCEPTED — OWNER ADOPTION READY`); owner/PI adoption 19 Oct 2026 with the grades listed in Status. *v6.4.14 record:* `[v6.4.14]` OPEN 3 payload reviewed as SESSION records on 19 Oct 2026 (scope note v0.1.1 `SESSION REVIEW PASSED`; P1/P2 `SCIENTIFIC REVIEW ACCEPTED — P3 READY`; P3 `SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING`, certificate replayed byte-identically); DRAFT r1 reviewed 19 Oct 2026 (`REVIEW ACCEPTED — OWNER ADOPTION READY`); owner/PI adoption 19 Oct 2026 with the grades listed in Status. *v6.4.13 record:* DRAFT r1 reviewed 18 Oct 2026 (ACCEPTED, corrections R1–R2 → r2); DRAFT r2 reviewed 18 Oct 2026 (ACCEPTED — ADOPTION READY); owner/PI adoption 18 Oct 2026 with the grade promotions listed in Status. Lemma F and F1–F3 (§6.17) are adopted `[THM]` at their stated scopes; `DYAD-THM-FORMAL-Z6-GENERATOR` and `DYAD-ALG-NU5-P5` are adopted owner results; adopted v6.4.12 content (§6.15–§6.16) keeps its review record (Appendix A v6.4.12). Consumer acceptance: §6.14 exports recorded by RECOG and NUMGEN; v6.4.12 results received by RRF v0.8.2 and acknowledged by Genesis (N7); OFN pending.  
> **Programme tier:** Tier 3 — Continuous Programme, upstream source (see Programme Overview §6)  
> **Status summary:** The dyad map has theorem-grade and exact-algebraic certification for the core six-step resonant module, including $c_{21}$, the local quintic normalization pipeline, the raw fixed-radius angular-mean coefficient $47/54$, OPEN 11 (chirality closure), and OPEN 18 (footprint monotonicity). OPEN 17 ($a_2$ projection coefficient) is closed under Lie-gauge convention. The finite OPEN 9 one-step ledger is exact for $p=5,6,7$. The low-degree anti-holomorphic vanishing theorem is now `[ALG]` for all $b\in\{2,3,4\}$ with exact ranges $p\ge b+2$, proved by automatic $\beta$-mode path enumeration (no source $\beta$-set contains the secular mode). OPEN-P0-DYADIC (SU(2) analysis of the p=6 resonance) is partially absorbed: the exact structural result is $\lambda=e^{i\pi/3}=e^{iF_f/2}$ `[ALG, exact]`; its transfer to the OPEN-M source amplitude remains `[CAND/conditional]`. The cubic cascade formula for $q=4,(0,3)$ is now **CLOSED all-$p$** (v6.4.9): the subgroup-strobe coefficient factors as $Q_p=i\zeta_p^3 M_p$ with $M_p\in\mathbb{Q}(\zeta_p)^+$ on the family $p=4s$, $s\ge2$ ($p=8$ zero degeneracy), via a three-path degree-3 derivation with the remainder relation $\sigma_{-1}(Q)=-\zeta_p^{-6}Q$ proved as an exact symbolic identity (DYAD-THM-Q403-PHASELAW). The active frontier is the remaining OPEN 9 arithmetic-horizon program: universal missing-slot rules and the all-$b\ge5$ persistence extension. The $b=4$ channel boundary is `[ALG]` for the dyadic map in the following two-part sense: universal vanishing holds for $b\in\{2,3,4\}$ (range $p\ge b+2$), and it first fails at $b=5$, for EVERY $p\ge6$ (all-$p$ theorem closed via cyclotomic non-division). Failure for every $b\ge6$ is **not** established (scan-confirmed at $b=6$ only); all-$b\ge5$ persistence and the general-coefficient version remain `[OPEN]`. `[COR v6.4.11]` The former shorthand "universal vanishing iff $b\le4$" overstated the $b\ge6$ direction. **v6.4.10 adopts** the independently reviewed local return-enclosure package (§6.14): the exact one-step polynomial normalizer $h$ through degree 6 with its six-step normal-form jet $J$ `[ALG]`, the normalization obstruction `[ALG]`, explicit primitive contraction with a six-phase invariant tube `[THM]`, the quantitative inverse-coordinate theorem `[THM]`, and radius-indexed normalized value/first-derivative remainders `[THM]`; installs SG-19 (normalization-object guard); corrects the `jet1_deg5.json` registry label and the archival $h_3=0$ wording (COR-RE-1..3); and reconciles the raw complex-form order symbol and the real-ray burst at their points of use. No pre-existing **scientific-result** RID is renamed or regraded; artifact-role corrections in §8 are explicitly recorded. RECOG R8/R9/R10/R11 and NUMGEN GAP-LOCK closures are **not** obtained here.
> 
> **v6.4.11 — synchronization (adopted 16 Oct 2026).** Consumer acceptance of the §6.14 package is now recorded by RECOG (v0.3.2 onward; R8–R11 closed in the consumer) and NUMGEN (v1.20; seed admission), and OFN v0.9 imports DYAD-THM-PRIM-CTR; §7 rows are synchronized. New registrations: `DYAD-DEF-PRIMITIVE-MAP` (provisional, Genesis alias pending), `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` + `DYAD-ALG-PROTECTION-MATRIX` (per-item grades retained), definition-ledger identities (`DYAD-ALG-Q-INVARIANT-FORM`, `DYAD-ALG-TAU-DETB`, `DYAD-ALG-CUBIC-PARABOLIC`), and `DYAD-ALG-NF6-DEG10` (finite fixed-$h_6$ statement). r2 adds `DYAD-THM-LOCAL-INVOLUTION-GERM` (§6.15: a local $C^1$ involution commuting with $T$, or a local $C^3$ involution commuting with $T^6$, is either the identity germ or has $DR(0)=-I$; conditional mathematics, no physical exchange claim) and the separate `[OPEN]` `DYAD-OPEN-FORMAL-CENTRALIZER`. Imported at owner grade: RECOG all-$p$ cubic radial contraction for the declared $K_p$ family, the general bridge-lemma proof (cross-reference; Dyadic RID retained), chart-native laws, the R9 lattice-memory theorem (scoped), and the P₂ manifold theorems (OPEN 12 → PARTIAL by consumer). §6.12/SG-15 wording updated to Genesis v2.8.5 typing and OPEN-M v0.7.1 (no certified numerical deficit). No certified v6.4.10 result is changed.
> 
> **v6.4.19 — adopted 20 Oct 2026.** NUMGEN interface: L-PHASE angular remainder on row A (`DYAD-THM-LPHASE-ROWA-REMAINDER`, `[THM]`). For every orbit started in $U=\{0<Q\le\tfrac1{625}\}$ and every block $m\ge0$: $\hat\varphi_{6(m+1)}-\hat\varphi_{6m}=2\pi-\tau Q_m+r_m$, $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$ ($Q_m$ primitive); on the six-phase tube every one-step increment satisfies $|\delta_T-\pi/3|\le\arcsin(0.04654)$, which fixes the six-step branch. Route: exact identity $r=\Lambda_3+[S_\Theta-L_\Theta]+\tau[D_Q-D_3]+[\operatorname{Arg}(J/z)+\tau q]+\operatorname{Arg}(\widehat F/J)$ in the chart of DYAD-ALG-NF6, adopted row-A bounds, exact-rational certificate, explicit $q\to Q$ bridge. No OPEN item changes; new notice N15. No adopted RID is renamed or regraded.
> 
> **v6.4.18 — adopted 20 Oct 2026.** OPEN 20 B-∞ existence: smooth flow embedding of the six-step return (`DYAD-THM-SMOOTH-EMBEDDING`, `[THM]`, $C^\infty$ germ scope). $F=\varphi_X^1$ with $X\in C^\infty$, $j^\infty X=\log F$; $X$ unique among generators with $DX(0)=0$; $C^\infty$ roots $K_m$, $J=T\circ K_6^{-1}$ ($J^6=\mathrm{id}$, $DJ(0)=A$, $JT=TJ$) and $R=T^3\circ K_2^{-1}$ ($R^2=\mathrm{id}$, $DR(0)=-I$, $RT=TR$). Route: Borel realization $X_\infty$ of $\log F$, $G_\infty=\varphi^1_{X_\infty}$, $\Phi_\infty=\lim G_\infty^{-n}F^n$ (flat, $C^\infty$), $X=\Phi_\infty^*X_\infty$. OPEN 20 B-∞ existence → CLOSED; OPEN 20 stays PARTIAL (B-an, B-6 OPEN). New notice N14. No adopted RID is renamed or regraded.
> 
> **v6.4.17 — adopted 19 Oct 2026.** OPEN 21 (P5): certified primitive-variable phase remainder (`[THM — conditional on RECOG-THM-R9-MEMORY]`): $|M_W-\mathcal P_2(W_0)|\le K'_jQ_0^{3/2}+C_{2,j}(256/225)^2Q_0^2$ with $K'_A=3951/1000$ ($|W_0|\le3/64$), $K'_B=971/250$ ($|W_0|\le3/128$); single-constant form $K_A=8831/250$, $K_B=883/100$; $\mathcal P_2$ is the adopted primitive-variable second-order form (§6.14). OPEN 21 → CLOSED. New notice N13. No adopted RID is renamed or regraded; OPEN 3 and OPEN 20 unchanged.
> 
> **v6.4.16 — adopted 19 Oct 2026.** Lifecycle only. OPEN 3c (P0): the recovered `spiral_phase_fit.py` is compared with the adopted OPEN 3 leading terms; four model differences are documented (one log-harmonic instead of $k=1,3$; $C=6$ step normalization on block-index data; archival Lie-gauge $c_\theta$ reference; single-window regression) and a `[NUM]` two-harmonic fit recovers the predicted amplitudes; OPEN 3c → CLOSED as a documented discrepancy, OPEN 3 → CLOSED within its defined scope; new OPEN 21 for the certified primitive-variable remainder. P2B v2 provenance: exact coefficient equality of $h$, $J$ with the enclosure certificate. Carried v6.4.10 hashes recorded (owner-measured). No RID is renamed or regraded; OPEN 20 unchanged.
> 
> **v6.4.15 — adopted 19 Oct 2026.** OPEN 3b (P4): with consistently lifted block phases, $\Psi_W-\Psi_z=\Delta_0(z_m)$, $\Delta_0=D_\Theta-\tau\log(1+D_Q/q)$ exactly; certified $|\Delta_0|\le K_0\sqrt q$, $|\Delta_0-\Delta_1|\le K_1q$, $|\Delta_0-\Delta_1-\Delta_2|\le K_2q^{3/2}$ per row; T1 limit equality $\Psi_{W,\infty}=\Psi_\infty$ (conditional on R9); T2 finite-start offset $M_W-M=-\Delta_0(z_0)=O(\sqrt{q_0})$ (conditional on T1); chart-variable raw-track memory law (conditional on R9); primitive-variable second order `[ALG — formal]` only (§6.14). OPEN 3b → CLOSED; OPEN 3 PARTIAL. New notice N11. No adopted RID is renamed or regraded; OPEN 20 unchanged.
> 
> **v6.4.14 — adopted 19 Oct 2026.** (1) OPEN 3 spiral residual, defined fit-free in the normalized chart ($S_Q=D_Q\circ\widehat F-D_Q$, $S_\Theta=D_\Theta\circ\widehat F-D_\Theta$): exact leading terms `DYAD-ALG-OPEN3-LEADING` `[ALG]`, including the corrected radial identity $P_5(\mathcal L^{-1}z)=DD_3[\mu qz]+2qD_3$, and certified per-block remainders `DYAD-THM-OPEN3-SPIRAL-REM` `[THM]` ( rows $|z|\le\tfrac1{20}$, $\tfrac1{40}$ unmixed) (§6.14). (2) OPEN 3 → PARTIAL: per-block chart sub-problem CLOSED; P4 asymptotic-phase transfer OPEN; P0 historical fit comparison BLOCKED. (3) N8/N9 receipts (Genesis v2.8.8, RRF v0.8.3); N10 to RECOG/NUMGEN. No adopted RID is renamed or regraded; OPEN 20 unchanged (PARTIAL).
> 
> **v6.4.13 — adopted 18 Oct 2026.** (1) `DYAD-THM-FORMAL-Z6-GENERATOR` `[THM — formal]`: $J=T\circ F^{-1/6}$ is the unique formal map with $J^6=\mathrm{id}$, $DJ(0)=A$, commuting with $F$; $R_0=J^3$, $G=J^2$ (§6.16). (2) OPEN 20 restructured: B-an ($F^{1/2}$), new **B-6** ($F^{1/6}$ ⟺ $J$ ⟺ exactly $\lambda$-equivariant chart; B-6 ⇒ B-an), B-∞ split into existence (OPEN) and flat uniqueness (closure **proposed**, §6.17). (3) §6.17 Lemma F (flat centralizer triviality) `[THM]` and F1–F3 `[THM — conditional]`, adopted after two review rounds; OPEN 20 B-∞ flat uniqueness CLOSED at the $C^\infty$ scope (existence stays OPEN). (4) M2c: $\nu_5^{(5)}$ closed form registered with an exact certificate (`DYAD-ALG-NU5-P5`). (5) N1/N2 (Genesis) answered, N7 status, custody text and consumer pins synchronized. No adopted RID is renamed or regraded.
> 
> **v6.4.12 — formal centralizer (adopted 16 Oct 2026).** OPEN 19 is closed in the formal category (§6.16): `DYAD-ALG-CENT-KERNEL` (homogeneous kernel of $\operatorname{ad}_{X_3}$ for every degree $k\ge2$), `DYAD-THM-FORMAL-CENTRALIZER` ($\operatorname{Cent}_{\rm formal,\,DG=I}(T^6)=\{\exp(sX)\}$), `DYAD-THM-FORMAL-INVOLUTION-UNIQUE` ($R_0=T^3\circ F^{-1/2}$ is the unique formal involution with linear part $-I$ commuting with $F=T^6$; it commutes with $T$ and equals $\widehat S$). §6.15 gains `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` (Corollary A: an analytic involution commuting with $T^6$ with $DR(0)=-I$ commutes exactly with $T$). New OPEN 20 (`DYAD-OPEN-INVOLUTION-REALIZATION`): convergence of $R_0$ / of $F^{1/2}$, and $C^\infty$ realization and flat uniqueness. Not claimed: existence of any analytic or $C^\infty$ involution, any factor-contract equivalence, any physical exchange (SG-14/15).

**H-P2-2** — origin: Local Tag Aliases, migration sentence. Verbatim P1-working-file text:

> `[DEF]` New ledger entries use canonical claim statuses from `DSN_METHODOLOGY_v1.3`. Pre-existing entries may retain legacy compound spellings; those are not claimed to be fully normalized, and where this revision unpacks a mixed alias into separate evidence/claim statements the scientific grade is preserved.

**H-P2-3** — origin: §1 OPEN-P0-DYADIC paragraph, Audit-1 clause. Verbatim P1-working-file text:

> (Audit-1; Genesis SG-5). `[v6.4.11]` OPEN-M v0.7.1 records **no certified numerical deficit** (R15 corrected; the $0.024$/$4/125$ target additionally conditional on the 9C premise, the large-$g$ limit and state matching), so this route

**H-P2-4** — origin: §2 OPEN 2B status lines. Verbatim P1-working-file text:

> Status: ACTIVE  
> Current state: Equivalent to OPEN 5.

**H-P2-5** — origin: §3 SG-14. Verbatim P1-working-file text:

> **[SG-14]** Programme-level cross-branch firewall (SG-PROG-1 in `RTG_PROGRAMME_OVERVIEW_v1.2`) applies. All dyadic results carry `[scope: conditional on postulated continuous generator T]` at the programme level until OPEN-P0 (generator selection) is resolved.

**H-P2-6** — origin: §4 layer-routing table, observable row. Verbatim P1-working-file text:

> | What does a long run measure? | Observable / fit | Backbone fits, spiral phase, $\kappa_{\rm fit}$, $\phi_*$ |

**H-P2-7** — origin: §5 R11 cascade-gate row. Verbatim P1-working-file text:

> | R11 cascade gate $4/125$ | Arithmetic conversion `[ALG, exact]`; physical threshold `[HYP inherited]` from OPEN-GEN-II-7B; OPEN-M v0.7.1 adds 9C/large-$g$/state-matching conditions |

**H-P2-8** — origin: §6.4, ISP layer sentence (wording). Verbatim P1-working-file text:

> remain ontological ground truth.

**H-P2-9** — origin: §6.14 boundary sentence, GAP-LOCK item. Verbatim P1-working-file text:

> Still not established anywhere: quantitative GAP-LOCK angular inequalities; historical

**H-P2-10** — origin: §7 programme-context list, export rows and outbound-notice table (v6.4.11–v6.4.19 states). Verbatim P1-working-file text:

> The following are programme context, except where a claim-level row above applies:
> - `RTG_PROGRAMME_OVERVIEW_v1.2` — SG-PROG-1 through SG-PROG-4.
> - `RTG_ONTOLOGICAL_FOUNDATIONS_v0.9` — Motivational layer for the generator choice; does not derive $T$. OFN v0.9 imports DYAD-THM-PRIM-CTR (IMP-O08-20) and records CUST-O09-01 (answered provisionally by DYAD-DEF-PRIMITIVE-MAP).
> - `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20` (freeze candidate) — source of the v6.4.11 imports: RECOG-ALG-NU3-CLOSED-FORM, RECOG-ALG-NU3-NONVANISHING, RECOG-ALG-LEADING-RETURN-EQUIVARIANCE (bridge-lemma proof provenance), RECOG-ALG-CHART-LAWS, RECOG-THM-R9-MEMORY, RECOG-THM-P2-HET, RECOG-THM-P2-C0-FIRST. `[P1 COR]` RECOG-THM-R9-MEMORY is load-bearing for the R9-dependent layer (claim-level row above); the others feed OPEN 9/OPEN 12 status and cross-references. Edition pins in this list are updated in P2 (FB-DYAD-16).
> 
> Exports to (via Import Ledger entries in those documents):
> - `RTG_TRIADIC_BIRTH_LIFT_DSN` (v1.6 inspected; its §7.1 pins are historical v6.4.8.1 via bridge note v1.1) — imports: $\mu_6$, $\tau$, Birkhoff frame, protection matrix, fracture-state kinematics [RID: DYAD-ALG-BRIDGE-LEMMA, DYAD-THM-C21, DYAD-ALG-LIEGAUGE-NORM]. `[v6.4.11]` Repin requested: frame and protection matrix → DYAD-DEF-BRIDGE-EXPORT-CONTRACT / DYAD-ALG-PROTECTION-MATRIX (not Lie-gauge dependent). NOTE (v6.4.10): the odd-projected residual $E_{\rm odd}$ (§6.12) is offered as a mathematical diagnostic export only; its identification with the Triadic/Genesis fracture residual is pending consumer acceptance.
> - `RTG_GENESIS_GEOMETRY_DSN` (v2.8.7 inspected `[v6.4.13]`; requests (i)–(ii) below answered in v2.8.6, Genesis pins DYAD v6.4.11 pending its own repin) — imports: $\mu_6$, $\tau$, $4\sqrt{3}/3$, OPEN 9 finite ledger, alias phase, $\lambda=e^{iF_f/2}$ face-flux identity `[ALG, exact]` [RID: DYAD-ALG-A1A2-LIEGAUGE, DYAD-ALG-ALIAS-PHASE, DYAD-ALG-P567-LEDGER, DYAD-ALG-P6-FACEFLUX]. `[v6.4.11]` Genesis v2.8.5 records the typed residuals of §6.12 (definition only; physical selection OPEN) and the archival-$h_3$ correction (GCL-07). Requests: (i) recognize GEN-DEF-PRIMITIVE-MAP as import/alias of DYAD-DEF-PRIMITIVE-MAP; (ii) repin "Birkhoff frame, $v_\perp$, protection matrix" from DYAD-ALG-LIEGAUGE-NORM to DYAD-DEF-BRIDGE-EXPORT-CONTRACT; (iii) optionally cite DYAD-ALG-NF6 where §6.2/§6.3 use "the adopted isolated-dyad normalizing chart $h$". NOTE: the OPEN-M gate-correction route (DYAD-CAND-P0-DYADIC) is `[CAND/conditional]` and must NOT be imported as a certified gate factor.
> - **Consumer (acceptance recorded): `RTG_RELATIONAL_RECOGNITION_DSN`** — DYAD-ALG-NF6, DYAD-ALG-NF6-OBS, DYAD-THM-PRIM-CTR, DYAD-THM-NF-INV, DYAD-THM-NF-REM. `[v6.4.11]` Acceptance recorded in RECOG v0.3.2 §7 and retained through v0.3.20 (live header: freeze candidate; final freeze record not inspected). Consumer outcomes, at RECOG's grades: R11 CLOSED (chart ledger), R10 DELIVERED/ACCEPTED, R9 CLOSED (RECOG-THM-R9-MEMORY), R8 CLOSED (RECOG-THM-P2-HET; PRIM-CTR as entry target). Scope unchanged: fixed $T$, exact $h$, stated domains, first real derivative; rows of NF-REM not mixed.
> - **Consumer (acceptance recorded): `RTG_NUMBER_GENESIS_DSN`** — DYAD-THM-PRIM-CTR. `[v6.4.11]` Acceptance recorded in NUMGEN v1.20 (retained in v1.20.7 §§6.2/9.1): seed $(\tfrac1{100},\tfrac1{250})\in U$ `[ALG]`; whole explicit tube inside the NUMGEN P3 injectivity box ($|\rho|,|\eta|<0.0665$, rechecked). NUMGEN left this upstream row to the Dyadic owner pass; synchronized here. Lineage: NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION retains its ownership. Tube membership does **not** certify GAP-LOCK's angular hypotheses. NUMGEN also imports DYAD-THM-Q403-PHASELAW (ownership Dyadic) and cites the typed-object distinctions of §6.5 (SG-NG-18).
> - **Offered import (v6.4.19): `RTG_NUMBER_GENESIS_DSN`** — DYAD-THM-LPHASE-ROWA-REMAINDER (`[THM]`), the explicit constant $\tfrac{403}{250}$ and branch certificate for NUMGEN's L-PHASE on row A. Interface objects I1–I5 confirmed by NUMGEN (20 Oct 2026); NUMGEN receipt replay byte-identical. Import by RID only after DYAD adoption; NUMGEN v1.20.8 records an `[OPEN]` sub-item without a value. No coefficient transfer (SG-19).
> - **Reference consumers (v6.4.11):** OFN v0.9 (IMP-O08-20 → DYAD-THM-PRIM-CTR; replaces its ambiguous backbone import); OPEN-M v0.7.1 (DYAD-CAND-P0-DYADIC as conditional only; archival/adopted $h_3$ distinction; OPEN-M-6 reopened); RRF v0.8 (profiles `RRF-DYAD-W`, `RRF-DYAD-NF`; VF-1 now registered here as DYAD-ALG-NF6-DEG10).
> 
> ### Outbound notices (v6.4.11) — pending owner action
> 
> | Notice | To | Request | Status |
> |---|---|---|---|
> | N1 | Genesis | Recognize GEN-DEF-PRIMITIVE-MAP as import/alias of DYAD-DEF-PRIMITIVE-MAP (OFN CUST-O09-01) | ANSWERED `[v6.4.13]` — Genesis v2.8.6 G-B02 (retained v2.8.7) |
> | N2 | Genesis, Triadic | Repin frame/protection-matrix imports from DYAD-ALG-LIEGAUGE-NORM to DYAD-DEF-BRIDGE-EXPORT-CONTRACT / DYAD-ALG-PROTECTION-MATRIX | Genesis ANSWERED `[v6.4.13]` (v2.8.6 G-B03); Triadic PENDING |
> | N3 | NUMGEN | `DYAD-CAND-PHISTAR-ENTRY-PHASE` (NUMGEN pre-registration pin) does not exist in Dyadic v6.4.10/v6.4.11. Identify the historical source of the $\phi^*$ entry-phase law before any Dyadic RID is assigned or the citation replaced. **No Dyadic RID is created.** | PENDING |
> | N4 | OFN | CUST-O09-01 answered (DYAD-DEF-PRIMITIVE-MAP; Genesis alias recorded in v2.8.6 `[v6.4.13]`) | INFORMATIONAL |
> | N5 | RECOG | Bridge-lemma general proof cross-referenced; Dyadic RID retained; ownership offer acknowledged, not executed | INFORMATIONAL |
> | N7 `[v6.4.12 r1]` | RRF, OFN, Genesis | OPEN 19 closed (formal; DYAD-ALG-CENT-KERNEL, DYAD-THM-FORMAL-CENTRALIZER, DYAD-THM-FORMAL-INVOLUTION-UNIQUE) and DYAD-THM-ANALYTIC-CLOCK-BRIDGE available for import (RRF v0.8.2 sync; G2 v0.2.1 §3 qualification). Realization stays OPEN 20; the K3 dimension split remains Genesis-owned. | RRF RECEIVED (v0.8.2, 17 Oct 2026); Genesis ACKNOWLEDGED, no import (consumer-impact note, 17 Oct; release record v2.8.7); OFN PENDING `[v6.4.13]` |
> | N8 `[v6.4.13]` | Genesis | M2c answered: $\nu_5^{(5)}$ closed form registered as DYAD-ALG-NU5-P5 (§6.11) with exact certificate; the Genesis v2.8.7 §6.2 value is confirmed | RECEIVED `[v6.4.14]` — Genesis v2.8.8 adopted 19 Oct 2026 (`9abd3616…0f37`): M2c CLOSED at the point of use with convention tag; live pins repinned to v6.4.13; replay [NUM] 4/4 |
> | N9 `[v6.4.13]` | OFN, RRF | Canonical ℤ₆ generator $J$ (DYAD-THM-FORMAL-Z6-GENERATOR, formal), the B-6 realization target, and the adopted Lemma F / F1–F3 (`[THM]` at the stated $C^\infty$ scope; existence OPEN). Bears on OFN reply v0.7 §3.5(b),(e): the C^∞ branch no longer needs an added commutation hypothesis or L-SHADOW-POLY | RRF RECEIVED `[v6.4.14]` — RRF v0.8.3 adopted 19 Oct 2026 (inspected `b393657e…a187`; §2.4b–c, all requested lines); OFN RECEIVED at session level (reply v0.7.1), owner level pending OFN v0.10 |
> | N10 `[v6.4.14]` | RECOG, NUMGEN | OPEN 3 chart-level spiral residual: DYAD-ALG-OPEN3-LEADING and DYAD-THM-OPEN3-SPIRAL-REM (adopted v6.4.14: `[ALG]`, `[THM]`). For RECOG: the per-block primitive-minus-normalized amplitude and phase increments ($S_Q$, $S_\Theta$) are bounded in the chart; no statement on the comparator $C_W^{(h)}$ and no R9 transfer to the raw track (SG-R14) is made (OPEN 3b). For NUMGEN: no L1 coefficient is transferred (SG-19) | PENDING |
> | N11 `[v6.4.15]` | RECOG, NUMGEN | OPEN 3b: exact offset $\Psi_W-\Psi_z=\Delta_0$ and certified bounds; R9 limit transfers to the primitive phase (T1, conditional on R9); raw-track memory $M_W=M-\Delta_0(z_0)$ (T2) and chart-variable memory law (conditional on R9). For RECOG: this quantifies SG-R14; no $C_W^{(h)}$ statement. For NUMGEN: no L1 transfer (SG-19) | PENDING |
> | N12 `[v6.4.16]` | RECOG, NUMGEN, RRF | OPEN 3 closed within its defined scope (lifecycle only; no RID or grade change); the historical fit `spiral_phase_fit.py` is a documented discrepancy and none of its outputs is a coefficient (SG-7, SG-19); new OPEN 21 for the primitive-variable remainder | PENDING (informational) |
> | N13 `[v6.4.17]` | RECOG, NUMGEN | OPEN 21: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (`[THM — conditional on RECOG-THM-R9-MEMORY]`), the certified primitive-variable remainder of the P4 memory expansion, per row, R9 term separate. For RECOG: uses R9 at statement level only; please flag any change of R9 statement, rows or $C_2$; a sharper $C_2$ would tighten the single constant directly. For NUMGEN: no L1/ISP-angle transfer (SG-19) | PENDING |
> | N14 `[v6.4.18]` | FMS, RRF, OFN | OPEN 20 B-∞ existence: DYAD-THM-SMOOTH-EMBEDDING (`[THM]`, $C^\infty$ germ scope) — $F=\varphi^1_X$, $X\in C^\infty$, $j^\infty X=\log F$; $C^\infty$ $F^{1/m}$, $J$, $R$ commuting with $T$. For FMS: answers the OPEN 20 priority request at the $C^\infty$ scope; B-an/B-6 (analytic) stay OPEN. For RRF: L-SHADOW-POLY not imported or used; G2 physical realization untouched. For OFN: bears on reply v0.7 §3.5(b),(e) (the $C^\infty$ branch now has an existing object); no physical reading | PENDING |
> | N15 `[v6.4.19]` | NUMGEN | L-PHASE angular remainder, row A: DYAD-THM-LPHASE-ROWA-REMAINDER (`[THM]`) — $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$ for block base points in $U$, $Q_m$ primitive; branch certificate on $U_T$. Interface I1–I5 as confirmed by NUMGEN. Majorant ceiling, not an optimum; no correction of NUMGEN's measured values; no L1/ISP-angle transfer (SG-19); row B not covered | PENDING |
> | N6 | RRF, OFN | G2-FIX mathematical content registered as DYAD-THM-LOCAL-INVOLUTION-GERM (a)+(b); RRF may narrow the G2 contract by reference; OFN retains the physical question of when $EF=TE$ holds and whether edge exchange is nontrivial | INFORMATIONAL |

**H-P2-11** — origin: §7 export protocol, first rule. Verbatim P1-working-file text:

> `[DEF]` All exported dyadic claims carry `[scope: conditional on postulated continuous generator T]` until programme-level OPEN-P0 is resolved.

**H-P2-12** — origin: v6.4.19 footer and the inherited footers v6.4.18–v6.4.12. Verbatim P1-working-file text:

> ---
> 
> *END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.19*  
> *Adopted 20 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 (adopted 20 October 2026). v6.4.19 adds the L-PHASE angular remainder on row A for NUMGEN, `DYAD-THM-LPHASE-ROWA-REMAINDER` `[THM]` ($|r_m|\le\tfrac{403}{250}Q_m^{3/2}$, $0<Q_0\le\tfrac1{625}$); no other RID, grade or OPEN status changed. v6.4.18 footer follows.*  
> *Adopted 20 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.17 (adopted 19 October 2026). v6.4.18 adds the smooth flow embedding of the six-step return `DYAD-THM-SMOOTH-EMBEDDING` `[THM]` ($C^\infty$ germ scope); OPEN 20 B-∞ existence CLOSED; OPEN 20 PARTIAL (B-an, B-6 OPEN). v6.4.17 footer follows.*  
> *Adopted 19 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 (adopted 19 October 2026). v6.4.17 adds the certified primitive-variable phase remainder `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` `[THM — conditional on RECOG-THM-R9-MEMORY]`, rows A/B not mixed; OPEN 21 CLOSED. v6.4.16 footer follows.*  
> *Adopted 19 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.15 (adopted 19 October 2026). Lifecycle only: OPEN 3c closed as a documented model discrepancy, OPEN 3 CLOSED within its defined scope, new OPEN 21 (primitive-variable remainder), P2B v2 provenance closed (exact coefficient equality), carried v6.4.10 hashes closed (owner-measured); no RID or grade changed. v6.4.15 footer follows.*  
> *Adopted 19 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.14 (adopted 19 October 2026). v6.4.15 adds the OPEN 3b asymptotic-phase transfer: exact offset `[ALG]`, certified bounds `[THM]`, limit equality and memory law conditional on R9, memory offset conditional on T1; OPEN 3b CLOSED, OPEN 3 PARTIAL (P0 BLOCKED). v6.4.14 footer follows.*  
> *Adopted 19 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.13 (adopted 18 October 2026). v6.4.14 adds the fit-free OPEN 3 spiral residual with exact leading terms (`[ALG]`) and certified per-block remainders (`[THM]`); OPEN 3 is PARTIAL (P4 OPEN, P0 BLOCKED). v6.4.13 footer follows.*  
> *Adopted 18 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.12.1 (metadata release of v6.4.12, adopted 16 October 2026). v6.4.13 adds the canonical ℤ₆ generator, the OPEN 20 realization hierarchy, Lemma F with F1–F3, and the $p=5$ quintic closed form; closes OPEN 20 B-∞ flat uniqueness at the $C^\infty$ scope; existence, analytic convergence and physical realization remain OPEN.*  
> *v6.4.12.1 is a metadata-only revision of v6.4.12. v6.4.12 (adopted 16 October 2026) supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.11 (adopted 16 October 2026): formal centralizer (OPEN 19 CLOSED, formal), Corollary A, OPEN 20 opened; outbound notices N1–N3 and N7 pending. Governing methodology: DSN_METHODOLOGY_v1.3 for edits since v6.4.10; untouched sections retain their prior status and are not claimed revalidated. Consumer acceptance of the §6.14 exports is recorded by RECOG and NUMGEN (§7); the §6.12 diagnostic definition is consumer-recorded by Genesis v2.8.5, its physical identification remains OPEN.*

### P1 working record — 21 October 2026 (noncanonical; not adopted)

- **Base:** adopted v6.4.19, SHA-256 `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`, unchanged.
- **Authority:** `P1 — SCIENTIFIC CORRECTION PASS AUTHORIZED` (reviewer, 21 Oct 2026), on disposition v0.1 (`7b2d1573…465c`). Preparation only: no adoption, no release, no notice.
- **Scope:** Tier A (FA-DYAD-01–08) and the scientific Tier B items FB-DYAD-12, 13, 15, 25. RID registration (FB-DYAD-10), edition pins, notice states and editorial items are P2.
- **Proposed RIDs (registered only at adoption):** DYAD-ALG-KP-FRAME-SCALE (`[ALG]`), DYAD-THM-SMOOTH-EQUIVARIANT-CHART (`[THM]`, corollary). No existing RID is renamed, removed or regraded, except that the two §6.6 statements without RIDs are retagged ([THM] → [ALG] and [DEF]).
- **FC-DYAD-32** is a separate SESSION record (`DYAD_FC32_HNG_R9FREE_SESSION_v0_1.md`); no text here.

| Edit | Row | Old (SHA-256, 16 hex) | New |
|---|---|---|---|
| E01 | all | `14dfd51e1e443176` | `4a3c1449b903f1c4` |
| E02 | FA-08 | `942c30baa762b98f` | `7d9c3cca0cf016c1` |
| E03 | FB-15 | `a9752cb7111bd3ed` | `6ae7ffc6fcebbbce` |
| E04a | FA-02 | `70ad0d6b0b898c71` | `e3b0c44298fc1c14` |
| E04b | FA-02 | `77fa2ef86bd605f9` | `e3b0c44298fc1c14` |
| E04c | FA-02 | `e296837f110b3abb` | `e3b0c44298fc1c14` |
| E04d | FA-02 | `f7a0375369e338cf` | `e3b0c44298fc1c14` |
| E05a | FA-02 | `c43c57096734593c` | `e3b0c44298fc1c14` |
| E05b | FA-02 | `fc02b4d3fc059409` | `e3b0c44298fc1c14` |
| E05c | FA-02 | `80f8879a0e243e45` | `e3b0c44298fc1c14` |
| E05d | FA-02/FB-24 | `34c64ca1fea4d986` | `7e14b5491121bc81` |
| E06 | FA-02 | `8a10b5694d268e55` | `e3b0c44298fc1c14` |
| E07 | FA-02 | `eebaa0f0d2029593` | `db2f3823a6d4f135` |
| E08 | FA-03/FA-04 | `003d063760b715f5` | `97617fa5984c3ab1` |
| E09a | FB-25 | `8a75abfb5387556c` | `685b46b49f438641` |
| E09b | FA-03 | `9c226cda1e401d9d` | `06e50ff2ab17c2da` |
| E09c | FA-03 | `0445c2412ba1c28c` | `1687be86c73a9104` |
| E09d | FA-03 | `8d58a376b039fa25` | `b6e83bf6d43df367` |
| E09e | FA-03 | `49a8769a960d0d77` | `5c2f448ef25f1279` |
| E09f | FA-03 | `0fa809bc2ea1c2a3` | `06a1178101801e72` |
| E09g | FA-03 | `147b63d0db4ac1cc` | `97b5bc7b51fa7570` |
| E09h | FA-07/FB-13 | `af53dc2fb5729ac1` | `15b18a3c5fc49b2d` |
| E10a | FA-05 | `24cc43f6be3320c9` | `a71d4ee1149945ca` |
| E10b | FA-05 | `eaefe1b4a3a62357` | `9d515dedc979f83b` |
| E10c | FA-05 | `b8878e2ff62f17ae` | `8f5055db1962f386` |
| E11a | FA-06 | `a0e7b4bff765befc` | `13981a4d43d501da` |
| E11b | FA-06 | `cbdd3fe5c1c78825` | `555ea85fa3011cd7` |
| E12a | FA-07 | `6f2436b34be65887` | `7b81117bdf7b196a` |
| E12b | FA-07 | `63995bec332bae29` | `08e5d469f91118b9` |
| E12c | FA-07 | `9d17b2d056b7ed42` | `7c0e9ad64fa22422` |
| E13 | FA-02 | `863e62c23ef48420` | `b85c3bb1adb4c4d1` |
| E14a | FA-04 | `0547909e4aa80fb3` | `82c688f4f0ac7f45` |
| E14b | FA-04 | `ddb4996f8f8afac5` | `378896af55d42c72` |
| E15a | FB-12 | `777b3ed68b8b9683` | `e336675cdfe47b16` |
| E15b | FB-12 | `2132246d02883252` | `55d39e80f9aad143` |
| E15c | FB-12 | `7626463ed3f6f5f1` | `3bca65337a9d9981` |
| E16 | FB-13 | `11acc1fbbc129259` | `37a2edf7ba22fa20` |
| E17 | FA-02 | `35fed544594a0128` | `a779b75db023d98d` |
| E18a | FA-02 | `85452523c237615c` | `6005bfef5d02fd3a` |
| E18b | FA-02 | `0b8019492cc3bd01` | `0d5d5579cdbeeee9` |
| E18c | FA-02 | `5cf60ea2a2d551c4` | `7fdc5436e0b8c13c` |
| E19 | FA-02 | `2fc6fa20f331deca` | `294f400269c2955c` |
| E19b | FA-02 | `e73f5c40a7448d8f` | `e3b0c44298fc1c14` |
| E20a | FA-01 | `ad9b20c403cc3580` | `7773f9210125d8fa` |
| E20b | FA-01 | `e4f4243c1a7028f3` | `84bf54d5139f10b3` |
| E20c | FA-01 | `7e2de987a250bc75` | `8c0afdb9e47766bd` |
| E21 | FA-02 | `094d0f8161f92b9e` | `88034132eb37f78f` |

#### P1 relocated history (verbatim from v6.4.19)

**H-1a** — origin: §2 OPEN 3, status line. Verbatim v6.4.19 text:

>  *v6.4.14–v6.4.15 status line, retained as history:* PARTIAL `[v6.4.14]` (v6.4.13: ACTIVE)

**H-1b** — origin: §2 OPEN 3, current-state line. Verbatim v6.4.19 text:

> Current state (v6.4.13, retained as history): Mechanistic origin identified: geometric projection from $2\operatorname{Re}(\bar{W}h_2)$ `[ALG structure]`. Theorem-grade Taylor remainder bounds remain `[OPEN]`.  

**H-1c** — origin: §2 OPEN 3b. Verbatim v6.4.19 text:

>  *v6.4.14 state, retained as history:* `[OPEN]`. From $\Psi_W-\Psi_z=D_\Theta-\tau\log(1+D_Q/q)$: (i) equality of the primitive and normalized asymptotic-phase limits and (ii) the finite-$q_0$ $O(\sqrt{q_0})$ static offset in the initial memory are to be proved as separate results. The per-block theorem does not by itself prove either.

**H-1d** — origin: §2 OPEN 3c. Verbatim v6.4.19 text:

>  *v6.4.14–v6.4.15 state, retained as history:* `BLOCKED` — `spiral_phase_fit.py` (DYAD-ART-SPIRAL-FIT) is unavailable; the fit is not a definition of the residual and is not a premise of OPEN 3a.

**H-1e** — origin: §2 OPEN 20, status line. Verbatim v6.4.19 text:

>  *v6.4.17 status, retained as history:* PARTIAL (v6.4.13) — B-∞ flat uniqueness CLOSED at the $C^\infty$ scope; B-an, B-6 and B-∞ existence ACTIVE

**H-1f** — origin: §2 OPEN 20, B-∞ existence pointer. Verbatim v6.4.19 text:

>  The next line is the v6.4.17 text, retained as history.

**H-1g** — origin: §2 OPEN 20, v6.4.17 B-∞ existence line. Verbatim v6.4.19 text:

> (B-∞ existence) `[OPEN]` Does a $C^\infty$ local involution with $DR(0)=-I$ commuting with $T$ exist (equivalently, by F3, a $C^\infty$ tangent-to-identity square root of $F$)? Same question for $F^{1/6}$ / $J$. A proposed construction route is recorded in §6.17; neither convergence nor the limit's properties are claimed.  

**H-1h** — origin: §2 OPEN 21, status line. Verbatim v6.4.19 text:

>  *v6.4.16 status, retained as history:* OPEN

**H-4** — origin: §2 priority ordering, internal frontier. Verbatim v6.4.19 text:

> **Internal dyadic frontier** — used when no downstream handoff is specified:
> 0. **OPEN-P0-DYADIC absorption** — `[PARTIAL v6.1]`: $\lambda=e^{iF_f/2}$ and SU(2) energy ratio registered `[ALG, exact]`; h-transfer to OPEN-M remains `[CAND/conditional]`. See §6.2, §6.6, §6.12.
> 1. **OPEN 9 cubic cascade formula — `[CLOSED v6.4.9]`.** Exact all-$p$ closed form $Q(L,I)=L^5(IL^2+I-L^2+1)/(2(L+1)^4(L^2+L+1))$; $p=8$ cancels ($Q_8=0$ zero degeneracy) while $p\ge12$ survives as $Q_p=i\zeta_p^3 M_p$, $M_p\in\mathbb{Q}(\zeta_p)^+$. Three-path degree-3 derivation; remainder relation $\sigma_{-1}(Q)=-\zeta_p^{-6}Q$ exact-symbolic. See §6.11 (DYAD-THM-Q403-PHASELAW).
> 2. **Universal missing-slot rules** — prove $Z^{\rm miss}_{p,q,D}$ using reachable-basis projector formalism.
> 3. **Bridge-gap smooth baseline** — compare $G_{32}$, $K_p$, $G_{32}/K_p$, $p^2G_{32}$, subgroup diagnostics over dense $p$ windows.
> 4. **Low-degree anti-holomorphic vanishing — `[COMPLETED v6.2]`.** $F_{\rm raw}^p(0,b)=0$ for $p\ge b+2$ is now `[ALG]` for all $b\in\{2,3,4\}$ via automatic $\beta$-mode path enumeration (source $\beta$-sets contain no secular mode). See §6.11.
> 4b. **Channel boundary $b=4$ — `[COMPLETED v6.4]` for the dyadic map.** The $b=5$ secular coefficient is proved nonzero (symbolic, not identically zero, $\propto c_{02}^2$; and nonzero at dyadic values). Proved `[ALG]`: vanishing for $b\in\{2,3,4\}$ and first failure at $b=5$ for all $p\ge6$. `[COR v6.4.11]` Not proved: failure for all $b\ge6$ (the former "$b\le4$ iff" shorthand). Remaining: all-$b\ge5$ persistence and general-coefficient version (§6.11).
> 5. **General $\nu_5^{(p)}$ theorem** — only after subgroup-strobe definitions and cancellation rules are stabilized.

**H-6** — origin: §3 SG-16 (full v6.4.19 text). Verbatim v6.4.19 text:

> **[SG-16]** Low-degree vanishing path-enumeration guard. Manual path enumeration is unsafe for pure anti-holomorphic vanishing claims (the $p=3,b=3$ nonzero case, where the direct term already vanishes, exhibits a cross-path that naive listing misses). For $b\le4$, automatic $\beta$-mode path enumeration has now been completed and certifies `[ALG]` (source $\beta$-sets carry no secular mode; cert: degree_b_vanishing_cert_v2.py). For $b\ge5$, NO promotion is allowed without the same source $\beta$-set certificate.  
> Violation: Tagging the $b=3,4$ vanishing as `[ALG]`, or asserting "$(c_{02})^2$ is the only cross-term" without the path-enumeration proof.

**H-7** — origin: §6.6, "p=6 uniqueness" and "three-tier hierarchy". Verbatim v6.4.19 text:

> `[THM]` **$p=6$ uniqueness.** For the resonant case $p=6$ ($\lambda = e^{i\pi/3}$), the eigenvalues $\lambda^j$ for $j=1,\ldots,5$ satisfy $\lambda^j \neq 1$. No intermediate resonance obstruction occurs: the 6-step tangent-to-identity normalization proceeds without spurious small-denominator cancellations at intermediate steps.
> 
> `[THM]` **Three-tier resonance hierarchy.** The $p$-resonance family decomposes into:
> - **Sub-resonant** ($p < 6$): rotation angle is not a rational multiple of $2\pi$ for which a six-step return is exact; faster decay.
> - **Resonant** ($p = 6$): unique six-step order-6 elliptic resonance; canonical study case.
> - **Super-resonant** ($p > 6$): more lattice harmonics activate; richer arithmetic-horizon structure.

**H-8** — origin: §6.9 operation-labelled objects. Verbatim v6.4.19 text:

>  until RECOG R11 completes the final-chart ledger.

**H-10** — origin: §6.5 backbone law. Verbatim v6.4.19 text:

> `[ALG]` **Backbone law:**
> $$Q_m\sim\tfrac{1}{m+\kappa},\quad Q_n\sim\tfrac{6}{n+C},\quad C=6\kappa.$$

**H-9** — origin: §6.15 bullet. Verbatim v6.4.19 text:

> - For $C^\infty$ $R$, only $j^\infty(RT-TR)=0$ follows. Exact primitive-clock commutation then needs a flat-uniqueness argument, currently OPEN (OPEN 20 (B-∞); RRF L-SHADOW-POLY, not imported). `[v6.4.13]` Superseded for existing $C^\infty$ involutions by §6.17 F1 (`[THM — conditional]`): exact primitive-clock commutation holds. The sentence is kept as the v6.4.12 record; existence remains OPEN 20.

**H-2a** — origin: §6.14 OPEN 3a, v6.4.14 list. Verbatim v6.4.19 text:

> `[OPEN]` `[v6.4.14]` **Not established** *(v6.4.14 state; OPEN 3b is addressed by the v6.4.15 entries below)*: OPEN 3b (P4) — equality of the primitive and normalized asymptotic-phase limits and the finite-$q_0$ $O(\sqrt{q_0})$ memory offset, as separate results; OPEN 3c (P0) — comparison with the historical fit (BLOCKED); any statement on $C_{\rm est}$, $\kappa_{\rm est}$ (SG-7); transfer of the chart coefficients to NUMGEN L1 primitive phase coefficients, ISP-angle coefficients, $47/54$, $c_\theta^{(6)}$, $a_1$, $a_2$ (SG-19); a certified bound on $\Delta\Theta_z$ beyond RECOG-ALG-CHART-LAWS; any effect on OPEN 20, G2 or physical readings.

**H-2b** — origin: §6.14 OPEN 3b, v6.4.15 list. Verbatim v6.4.19 text:

> `[OPEN]` `[v6.4.15]` **Not established** *(v6.4.15 state; OPEN 3c, the provenance comparison and the primitive-variable remainder are addressed by the v6.4.16 entries below)*: a certified primitive-variable remainder; the combined $\pm6$ coefficient of $\Lambda_1$ and $P_{W2}$ (exact $\Lambda_1$ not inspected); OPEN 3c (P0, BLOCKED); C_est/κ_est (SG-7); NUMGEN L1/ISP-angle transfer (SG-19); the P2B v2 `certificate.json` provenance comparison (carried); any effect on OPEN 20, G2 or physical readings.

**H-2c** — origin: §6.14 OPEN 3c, v6.4.16 list. Verbatim v6.4.19 text:

> `[OPEN]` `[v6.4.16]` **Not established** *(v6.4.16 state; the primitive-variable remainder (OPEN 21) is addressed by the v6.4.17 entries below)*: a certified primitive-variable remainder (OPEN 21); the combined $\pm6$ coefficient of $\Lambda_1$ and $P_{W2}$; C_est/κ_est (SG-7); NUMGEN L1/ISP-angle transfer (SG-19); any effect on OPEN 20, G2 or physical readings.

**H-3** — origin: §6.17, v6.4.17 list. Verbatim v6.4.19 text:

> `[OPEN]` `[v6.4.17]` **Not established** *(v6.4.17 state; existence of $C^\infty$ roots, $J$ and $R$ is addressed by the v6.4.18 entries below)*: existence of any $C^\infty$ root, involution or $J$ (OPEN 20 B-∞ existence; proposed construction route: the conjugation sequence $F^{-n}R_\infty F^n$ with $R_\infty$ a Borel realization of $R_0$. `[COR r2, review R1]` Its $C^0$ convergence, higher-derivative convergence, and the commutation properties of a limit are **not proved**; Lemma F gives uniqueness of an existing flat-close commuting map, not convergence of approximately commuting conjugates. r1's statement that $C^0$ convergence follows from Lemma-F-type estimates is withdrawn); finite-$C^k$ analogues; analytic B-an/B-6; physical exchange or G2 realization; identification of $EF=TE$ with $EF=T^6E$.

**H-1i** — origin: §8 DYAD-ART-SPIRAL-FIT entry. Verbatim v6.4.19 text:

>  *v6.4.14 note, retained:* `[v6.4.14]` file unavailable (OPEN 3c BLOCKED)

**H-5** — origin: §7 first paragraph. Verbatim v6.4.19 text:

> The self-contained local core of this study (the six-step module, the OPEN 9 arithmetic ledger, and the return-enclosure package of §6.14) has no upstream scientific DSN imports; it is derived from the postulated primitive map $T(\rho,\eta)$. Cross-study interpretations elsewhere (face-flux identity, OPEN-M gate conversion) use external inputs whose provenance is recorded at their entries (§6.2, §6.11, §6.12, SG-15).

### v6.4.19 — adopted 20 October 2026

- **Adoption:** owner/PI decision of 20 Oct 2026 (`DYAD v6.4.19 — OWNER ADOPTION AUTHORIZED`) after external review of DRAFT r1 (`v6.4.19 r1 — SCIENTIFIC REVIEW ACCEPTED` (`SCIENTIFIC CONTENT ACCEPTED — OWNER ADOPTION READY, WITH REPLAY QUALIFICATION`); r1 `f6211201b95c5a7a5c8d992cdd943e56d3655b9a757cb1b427d72a8fd85d6e47`). r1 scientific text unchanged.
- **Grade taken at adoption:** `DYAD-THM-LPHASE-ROWA-REMAINDER` `[THM]` — (B) branch certificate on $U_T$, $\varepsilon\le0.04654$; (R) $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$, $0<Q_0\le\tfrac1{625}$, $m\ge0$, $Q_m$ primitive; NUMGEN interface I1–I5 kept; $\tfrac{403}{250}$ a certified upper bound, not an optimum. No other RID, grade or OPEN status changed.
- **Release edits:** body status labels ("v6.4.19 draft", "proposed grade, not in force", "proposed `[THM]`", "ON ADOPTION" → adopted labels; N15 PENDING), header metadata, this record, footer. Release transform `release_v6_4_19.py`; checker `check_release_v6_4_19.py`.
- **Evidence levels (PI decision):** `OWNER-RUN` — combined draft checker 16/16 with G14/G15, the 11 draft-checker negative controls, provenance controls M1–M4 as separate processes (exit 1 each), certificate JSON `8697c697…ad4fa`, gate JSON `58cfafd3…fc89`, control exit codes `e2ffa46b…1a1e`, split replays `replay_g14_certificate.py` / `replay_g15_provenance.py`. `REVIEWER-REPLAYED` — hashes of the draft and both packages, manifest 32/32, deterministic builder, the 11 draft negative controls, provenance gate main run 9/9 with 4 internal controls. `REVIEWER FULL REPLAY NOT COMPLETED` — combined G14–G15 run and the independent `--record-exit-codes` run; this line changes only after new independent runs.
- **Release tools (no scientific text):** G14 and G15 of the draft checker are separately runnable (`replay_g14_certificate.py`; `replay_g15_provenance.py` with `--control Mk` and `--all-controls`), each with deterministic JSON output and crash exit code 3.
- **Carried open:** row B; reviewer full replay of G14–G15; N15 (to be sent only after external verification of the final SHA-256); N3 (pending NUMGEN v1.20.8); Triadic part of N2; N7/N9 OFN owner level; N10–N14 receipts; OPEN 20 B-an, B-6.
- Draft history follows.

### v6.4.19 — DRAFT r1, 20 October 2026 (draft record; not adopted)

- **Basis:** PI/reviewer decision `v6.4.19 DRAFT r1 — PREPARATION AUTHORIZED` (20 Oct 2026), given with the review of the P2B provenance gate v0.1 (`PROVENANCE CHAIN ACCEPTED IN PRINCIPLE — FULL REPLAY NOT VERIFIED`); earlier reviews: scope note (`ROW A CERTIFICATION AUTHORIZED`), certificate (`L-PHASE ROW A SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING`); NUMGEN interface confirmation I1–I5 and receipt replay. Not a final adoption decision.
- **Scientific payload (proposed grade):** `DYAD-THM-LPHASE-ROWA-REMAINDER` `[THM]` — (B) branch certificate on $U_T$, $\varepsilon\le0.04654$; (R) $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$ for block base points in $U$, $Q_m$ primitive. Sign convention and six-step phase lift as confirmed by NUMGEN.
- **Registrations:** §1 line; §5 scope row; §6.14 block (interface objects, theorem, recorded distinctions, not-established list); §7 offered-import row and notice N15 (ON ADOPTION); §8 artifacts DYAD-ART-LPHASE-ROWA, DYAD-ART-LPHASE-P2B-PROV, DYAD-ART-LPHASE-ROWA-RECORDS.
- **Provenance (reviewer table):** P2B coefficient chain recorded as a transitive exact-coefficient comparison; gate v0.1.1 owner replay ALL PASS with separate control exit codes; reviewer full replay pending, to be done before adoption.
- **Unchanged:** all adopted RIDs and grades of v6.4.18 (including DYAD-THM-SMOOTH-EMBEDDING, OPEN 21, the §6.14 enclosure theorems used as inputs); OPEN 20 PARTIAL (B-an, B-6 OPEN); N3 (pending NUMGEN v1.20.8); Triadic part of N2; N7/N9 OFN owner level; N10–N14 (PENDING).

### v6.4.18 — adopted 20 October 2026

- **Adoption:** owner/PI decision of 20 Oct 2026 after external review of DRAFT r1 (`v6.4.18 DRAFT r1 — SCIENTIFIC REVIEW ACCEPTED`; r1 `6abed0b86332728d41eeea265eb97e8fac6bc1a036e538fa671493112ea3d1b3`; manifest 20/20; package draft byte-identical to the uploaded draft; draft checker 13/13; payload check scripts re-executed with their internal negative controls (integration 6/6, P3-a 8/8, P3-b/c v0.1.1 3/3); E2/L7 scope correction of integration audit v0.1.1 accepted; RIDs 129 → 132, none lost; prior grades unchanged). r1 scientific text unchanged.
- **Grade taken at adoption:** `DYAD-THM-SMOOTH-EMBEDDING` `[THM]`, $C^\infty$ germ scope (E1–E4; E2 only for generators with $DX'(0)=0$). OPEN 20 B-∞ existence CLOSED; OPEN 20 PARTIAL (B-an, B-6 OPEN).
- **Release edits:** body status labels ("v6.4.18 draft", "proposed grade, not in force", "CLOSED (proposed …)", "ON ADOPTION" → adopted labels; N14 PENDING), header metadata, this record, footer. Release transform `release_v6_4_18.py`; checker `check_release_v6_4_18.py`.
- **Evidence distinction:** the r1 review re-executed the draft checker (13/13) and the three payload check scripts with their internal negative controls; the eight draft-checker negative controls (`--neg`) are owner reruns recorded in the package.
- **Carried open:** OPEN 20 B-an, B-6; N3; Triadic part of N2; N7/N9 OFN owner level; N10–N13 receipts; N14 (to be sent only after release verification, citing the verified final hash).
- Draft history follows.

### v6.4.18 — DRAFT r1, 20 October 2026 (draft record; not adopted)

- **Basis:** external review of the integration audit v0.1 (`SMOOTH EMBEDDING CHAIN ACCEPTED — E2 SCOPE CORRECTION REQUIRED`, 20 Oct 2026), which supports a v6.4.18 DRAFT r1 after the E2 narrowing (applied in audit v0.1.1), with no new numerical campaign and no new physical claim.
- **Scientific payload (proposed grade):** `DYAD-THM-SMOOTH-EMBEDDING` `[THM]` ($C^\infty$ germ scope) — E1 smooth flow embedding, E2 uniqueness among generators with zero linear part, E3 smooth roots (F3), E4 smooth $J$ and $R$ (F3, F2, §6.15 convention).
- **Lifecycle:** OPEN 20 B-∞ existence OPEN → CLOSED (proposed); OPEN 20 stays PARTIAL; the v6.4.17 status and B-∞ existence text are kept as history; the v6.4.17 §6.17 "Not established" paragraph is annotated, not removed; §1 line; §5 scope row; §8 artifacts (DYAD-ART-OPEN20-BINF-RECORDS, DYAD-ART-OPEN20-BINF-CHECKS); notice N14.
- **Recorded distinctions:** $G_\infty$ vs $G=J^2$; route $G_\infty^{-n}F^n$ vs the unproved §6.17 route; E2 scope; F1–F3 grades unchanged, existence condition discharged; qualitative radius; analyticity untouched; SG-14/15.
- **Unchanged:** all adopted RIDs and grades of v6.4.17 (including Lemma F, F1–F3, DYAD-THM-FORMAL-Z6-GENERATOR, OPEN 21); B-an, B-6; N3; Triadic part of N2; N7/N9 OFN owner level; N10–N13 (PENDING).

### v6.4.17 — adopted 19 October 2026

- **Adoption:** owner/PI decision of 19 Oct 2026 after external review of DRAFT r1 (`SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION READY`; r1 `191110e3432d69df3a3d9c7e41162f7756ad508783bbed0858fd50f6839c74e1`; manifest 20/20; v6.4.16→r1 diff applied byte-exactly; checker 13/13; negative controls 7/7; P5 certificate 28/28, JSON byte-identical; RIDs 126 → 129, none lost). r1 scientific text unchanged.
- **Grade taken at adoption:** `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` `[THM — conditional on RECOG-THM-R9-MEMORY]`; constants per row as reviewed ($K'_A=3951/1000$, $K'_B=971/250$; $K_A=8831/250$, $K_B=883/100$; $C_{2,j}(256/225)^2$ kept separate). OPEN 21 CLOSED.
- **Release edits:** body status labels ("v6.4.17 draft", "proposed grade, not in force", "CLOSED (proposed, …)", "ON ADOPTION" → adopted labels; N13 PENDING), header metadata, this record, footer. Release transform `release_v6_4_17.py`; checker `check_release_v6_4_17.py`.
- **Evidence distinction (reviewer note):** the r1 review re-executed the draft checker and its negative controls; the seven P5 negative controls were verified from the package records (owner reruns), not re-executed in that round.
- **Carried open:** OPEN 20 B-an, B-6, B-∞ existence; N3; Triadic part of N2; N7/N9 OFN owner level; N10, N11, N12, N13 receipts (N13 to be sent only after release verification).
- Draft history follows.

### v6.4.17 — DRAFT r1, 19 October 2026 (draft record; not adopted)

- **Basis:** external review `P5 v0.1.2 — SCIENTIFIC REVIEW ACCEPTED` (19 Oct 2026), which approves a v6.4.17 DRAFT r1 carrying the reviewed P5 result into the owner DSN, with no new physical or representational claim and no new certificate campaign.
- **Scientific payload (proposed grade):** `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` `[THM — conditional on RECOG-THM-R9-MEMORY]` — primary decomposed inequality with $K'_A=3951/1000$, $K'_B=971/250$ and the separate R9 term $C_{2,j}(256/225)^2Q_0^2$; secondary single constants $K_A=8831/250$, $K_B=883/100$; rows not mixed.
- **Lifecycle:** OPEN 21 OPEN → CLOSED (proposed); the v6.4.16 status is kept as history; the v6.4.16 §6.14 "Not established" paragraph is annotated, not removed; closed-list entry; §1 line; §5 scope row; §8 artifacts (DYAD-ART-OPEN21-P5, DYAD-ART-OPEN21-P5-RECORDS); notice N13.
- **Recorded distinctions:** R9 at statement level only, not re-certified; R9 term kept separate; `[NUM]` sampling supporting only; the v6.4.15 `[ALG — formal]` entry is unchanged.
- **Unchanged:** all adopted RIDs and grades of v6.4.16 (including T1, T2 and the chart-variable memory law); OPEN 3 (CLOSED, defined scope); OPEN 20 (PARTIAL); N3; Triadic part of N2; N7/N9 OFN owner level; N10, N11, N12 (PENDING).

### v6.4.16 — adopted 19 October 2026

- **Adoption:** owner/PI decision of 19 Oct 2026 after external review of DRAFT r1 (`SCIENTIFIC AND LIFECYCLE REVIEW ACCEPTED — OWNER ADOPTION READY`; r1 `a24bf77d9c0b6721717346155a9910e644204689fbcb6757a47db20d43b1982f`; manifest 16/16; rebuild PASS; checker 13/13; negative controls 7/7). r1 text unchanged except labels and metadata.
- **Statuses taken at adoption:** OPEN 3c CLOSED — documented model discrepancy; OPEN 3 CLOSED within its defined scope; OPEN 21 `DYAD-OPEN-PRIMITIVE-PHASE-REMAINDER` OPEN; P2B v2 provenance CLOSED (exact coefficient equality); carried v6.4.10 hashes CLOSED — owner-measured. No scientific RID added, no grade changed.
- **Evidence distinction (reviewer condition):** reviewer-executed — P2B coefficient comparison and its negative control, P2B v2 referee, P0 numerical comparison, build/check chain; owner-measured only — `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` `e4e2bab0…fdbe4` and `check_owner_adoption.py` `c04096e1…00fe` (historical reviewer match as reported, not re-measured).
- **Release edits:** draft/proposed labels → adopted labels (header, OPEN 3 status, OPEN 3c, closed list, OPEN 21 tag, §5 row, §6.14 v6.4.16 entries, §8 tags), N12 PENDING (informational), header metadata, this record, footer. Release transform `release_v6_4_16.py`; checker `check_release_v6_4_16.py`.
- **Carried open:** OPEN 21 (certified primitive-variable remainder); OPEN 20 B-an, B-6, B-∞ existence; N3; Triadic part of N2; N7/N9 OFN owner level; N10, N11, N12.
- Draft history follows.

### v6.4.16 — DRAFT r1, 19 October 2026 (draft record; not adopted)

- **Basis:** external review of the recovered-artifacts SESSION record (19 Oct 2026), supporting a v6.4.16 DRAFT r1 with option (a): OPEN 3 closed within its defined scope, the primitive-variable remainder separated as a new OPEN, provenance and carried hashes closed. Session record v0.1.1 applies the review notes (exact coefficient equality, not byte identity; hashes owner-measured; engine added to the package).
- **Lifecycle (proposed):** OPEN 3c BLOCKED → CLOSED (documented model discrepancy); OPEN 3 PARTIAL → CLOSED within its defined scope (history lines retained; closed-list entry added); new OPEN 21 `DYAD-OPEN-PRIMITIVE-PHASE-REMAINDER`; P2B v2 provenance comparison CLOSED; the two carried v6.4.10 hashes CLOSED (owner-measured). §5 scope row, §6.14 v6.4.16 entries (the v6.4.15 "Not established" paragraph is annotated, not removed), §8 (DYAD-ART-SPIRAL-FIT updated; DYAD-ART-RE-P2B2 and DYAD-ART-RE-SUPPL annotated with hashes; new DYAD-ART-OPEN3-P0), notice N12 (informational).
- **New RIDs:** `DYAD-OPEN-PRIMITIVE-PHASE-REMAINDER` (OPEN item), `DYAD-ART-OPEN3-P0` (artifact). No scientific RID added; no grade changed.
- **Unchanged:** all adopted RIDs and grades of v6.4.15 (including the conditional T1/T2 and memory-law grades of DYAD-THM-OPEN3-ASYMPTOTIC-PHASE); OPEN 20 (PARTIAL); N3; Triadic part of N2; N7/N9 OFN owner level; N10, N11 (PENDING).

### v6.4.15 — adopted 19 October 2026

- **Adoption:** owner/PI decision of 19 Oct 2026 after external review of DRAFT r1 (`SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION READY`; r1 `d2be05c54680715a8567370a334be1812ca509c07fe00bd7f9217627a0f79f64`; v6.4.14→r1 diff applied byte-exactly; checker 13/13; negative controls 6/6 re-run by the reviewer). r1 scientific text unchanged.
- **Grades taken at adoption:** `DYAD-ALG-OPEN3-PHASE-OFFSET` `[ALG]` (primitive-variable part `[ALG — formal]`); `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS` `[THM]`; `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`: T1 `[THM — conditional on R9]`, T2 `[THM — conditional on T1]`, chart-variable memory law `[THM — conditional on R9]`. OPEN 3b CLOSED; OPEN 3 PARTIAL (3c BLOCKED).
- **Release edits:** body status labels ("v6.4.15 draft", "proposed grade, not in force", "CLOSED (proposed, …)", "ON ADOPTION" → adopted labels; N11 PENDING; §1 line tagged with its R9 condition), header metadata, this record, footer. Release transform `release_v6_4_15.py`; checker `check_release_v6_4_15.py`.
- **Installation note:** the project installation is recorded separately from adoption (reviewer guidance): "adopted and installed" only once the file and manifest are written to the project; otherwise "adoption authorized, installation pending".
- **Carried open:** certified primitive-variable remainder; OPEN 3c (P0); P2B v2 `certificate.json` comparison; OPEN 20 B-an, B-6, B-∞ existence; N3; Triadic part of N2; N7/N9 OFN owner level; N10, N11; the two carried v6.4.10 hashes.
- Draft history follows.

### v6.4.15 — DRAFT r1, 19 October 2026 (draft record; not adopted)

- **Basis:** external P4 review of 19 Oct 2026 (`P4 SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING`), recommending a v6.4.15 DRAFT r1 with the P4 results, their R9 dependencies and the primitive-variable proof gap stated explicitly; OPEN 3b to be closed only by an owner adoption decision.
- **Scientific payload (proposed grades, as recommended by the review):** `DYAD-ALG-OPEN3-PHASE-OFFSET` `[ALG]` (P4-0, $\Delta_1$, $\Delta_2$; primitive-variable second order `[ALG — formal]`); `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS` `[THM]` ($K_0,K_1,K_2$ per row: $\tfrac1{20}$: $\tfrac{1101}{1000},\tfrac{691}{500},\tfrac{1323}{1000}$; $\tfrac1{40}$: $\tfrac{533}{500},\tfrac{1341}{1000},\tfrac{641}{500}$); `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` — T1 `[THM — conditional on R9]`, T2 `[THM — conditional on T1]`, chart-variable memory law `[THM — conditional on R9]`.
- **Lifecycle:** OPEN 3b `[OPEN]` → CLOSED (proposed); OPEN 3 remains PARTIAL (3a CLOSED, 3c BLOCKED); the v6.4.14 OPEN 3b line is kept as history; the v6.4.14 §6.14 "Not established" paragraph is annotated, not removed. §1 line, SG-9 asymptotic note, §5 scope row, §8 artifacts (DYAD-ART-OPEN3-P4, DYAD-ART-OPEN3-P4-RECORD), notice N11.
- **Recorded distinctions:** T1 is conditional on R9 and not an independent existence theorem; the primitive-variable $O(Q_0^{3/2})$ remainder is not certified; no $C_W^{(h)}$ statement.
- **Unchanged:** all adopted RIDs and grades of v6.4.14 (including DYAD-ALG-OPEN3-LEADING, DYAD-THM-OPEN3-SPIRAL-REM and the §6.14 consumer imports); OPEN 20 (PARTIAL); N3; Triadic part of N2; N7/N9 OFN owner level; N10 (issued, PENDING); P2B v2 provenance comparison; the two carried v6.4.10 hashes.

### v6.4.14 — adopted 19 October 2026

- **Adoption:** owner/PI decision of 19 Oct 2026 after external review of DRAFT r1 (`SCIENTIFIC REVIEW ACCEPTED`, `REVIEW ACCEPTED — OWNER ADOPTION READY`; r1 `7f7ea7f3d7262b1297da5b5dc65f73f8e55ab03370189a6302ab44967aef6ebf`; package integrity, deterministic rebuild and 12/12 gates confirmed by the reviewer). r1 scientific text unchanged.
- **Grades taken at adoption:** `DYAD-ALG-OPEN3-LEADING` `[ALG]`; `DYAD-THM-OPEN3-SPIRAL-REM` `[THM]` (constants per row as reviewed; majorant suprema, not true-error suprema). OPEN 3 PARTIAL: 3a CLOSED, 3b (P4) OPEN, 3c (P0) BLOCKED.
- **Release edits:** status labels in the body ("v6.4.14 draft", "proposed grade, not in force", "CLOSED (proposed)", "ON ADOPTION" → adopted labels; N10 PENDING), header metadata, this record, footer. Release transform `release_v6_4_14.py`; checker `check_release_v6_4_14.py`.
- **Carried open:** P4 (OPEN 3b); P0 (OPEN 3c, artifact unavailable); comparison of $h$, $J$ with the adopted P2B v2 `certificate.json`; OPEN 20 B-an, B-6, B-∞ existence; N3; Triadic part of N2; N7/N9 OFN owner level; N10; the two carried v6.4.10 hashes.
- Draft history follows.

### v6.4.14 — DRAFT r1, 19 October 2026 (draft record; not adopted)

- **Authorization:** PI work decision of 19 Oct 2026 — v6.4.14 DRAFT r1 approved, containing only the reviewed P2/P3 results and the required lifecycle updates; formal adoption of the `[ALG]`/`[THM]` promotions only after review of the final draft and a separate adoption record; v6.4.13 unchanged; P4 to follow as a separate task.
- **Scientific payload (proposed grades):** §6.14 `[DEF]` fit-free spiral residual; `DYAD-ALG-OPEN3-LEADING` (proposed `[ALG]`); `DYAD-THM-OPEN3-SPIRAL-REM` (proposed `[THM]`), constants per row exactly as reviewed ($\tfrac1{20}$: $K_\Theta=\tfrac{123}{125}$, $K_Q=\tfrac{2353}{1000}$; $\tfrac1{40}$: $K_\Theta=\tfrac{909}{1000}$, $K_Q=\tfrac{258}{125}$).
- **Lifecycle:** OPEN 3 ACTIVE → PARTIAL (proposed): OPEN 3a per-block chart residual CLOSED, OPEN 3b (P4) OPEN, OPEN 3c (P0) BLOCKED; the v6.4.13 state line is kept as history. SG-9 gains a certified chart-level note (guard text unchanged). §1 summary line, §5 scope row, §8 artifacts (DYAD-ART-OPEN3-P2/-P3/-RECORDS; DYAD-ART-SPIRAL-FIT annotated).
- **Recorded distinctions (PI condition):** majorant supremum ≠ true-error supremum; the per-block theorem does not prove the asymptotic-phase transfer; the independent regeneration of $h$ (23/23 against the 19 Sep audit reconstruction) does not replace verification against the adopted P2B v2 `certificate.json`.
- **Synchronization:** N8 RECEIVED (Genesis v2.8.8); N9 RRF RECEIVED (RRF v0.8.3), OFN session level; new N10 (RECOG, NUMGEN; on adoption); consumer-edition pins.
- **Unchanged:** all adopted RIDs and grades (DYAD-THM-PRIM-CTR, NF-INV, NF-REM, NF6 and the §6.14 consumer imports); OPEN 20 (PARTIAL; B-an, B-6, B-∞ existence OPEN); G2 status; SG-14/15; N3; Triadic part of N2; the two carried v6.4.10 hashes.

### v6.4.13 — adopted 18 October 2026

- **Adoption:** owner/PI decision of 18 Oct 2026 after external review of DRAFT r2 (`SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION READY`, r2 `d6bebcc9022637469d93c46c88e1249e4c06adbda1be838ea56af8cc393dee41`; review manifest `DYAD_v6_4_13_r2_REVIEW_MANIFEST.json`: v6.4.12.1→r1 and r1→r2 diffs byte-exact, 0 RID loss, 6 new RIDs, M2c replay PASS with negative control exit 1).
- **Scientific status decisions taken at adoption (recorded here, in OPEN 20 and in the change record):** `DYAD-CAND-FLAT-CENTRALIZER` (Lemma F) `[CAND]` → `[THM]` with explicit domain (D1–D3) and flat-contact hypotheses; `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` (F1–F3) `[CAND]` → `[THM — conditional]` on Lemma F and on the existence of the smooth object; OPEN 20 B-∞ flat uniqueness `[OPEN]` → CLOSED at the proved $C^\infty$ scope, OPEN 20 status ACTIVE → PARTIAL; `DYAD-THM-FORMAL-Z6-GENERATOR` and `DYAD-ALG-NU5-P5` adopted at their draft grades. RIDs unchanged (DSN v1.3 §4.2). Not adopted: any existence statement; B-an/B-6; the construction route of §6.17.
- **Reviewer record items (release edits):** §8 DYAD-ART-LEMMA-F-RECORD repinned to proof record v0.3 (v0.2 kept as reviewed predecessor); §1 and §6.15 review wording updated; live summary relabelled; OPEN 20 closure wording limited to existing smooth objects; notices N8/N9 set PENDING.
- **Carried open:** OPEN 20 B-an, B-6, B-∞ existence; G2 physical realization; N3, N7 (OFN), N8, N9; Triadic part of N2; the two carried v6.4.10 hashes.
- Draft history follows (r2 → r1).

### v6.4.13 — DRAFT r2, 18 October 2026 (draft record; not adopted)

- **Review of r1** (`eea9b68e4b238d5c521bc2f1730f9406092fd5ebeb396ee8a740356166a06352`): `SCIENTIFIC REVIEW ACCEPTED`. Lemma F with D1–D3 ACCEPT; F1–F3 ACCEPT conditional on Lemma F; formal $J$ ACCEPT; M2c exact certificate PASS (with the note that the $p=6$ calibration fixes the declared convention and does not prove equivalence of alternative normalization conventions); diff and RID preservation PASS; owner adoption not yet done.
- **R1 (applied):** §6.17 and OPEN 20 (B-∞ existence) no longer state that $C^0$ convergence of $F^{-n}R_\infty F^n$ follows from Lemma-F-type estimates; the sequence is a proposed construction route only. Proof record bumped to v0.3 (same correction; `2e6c5c59…8ece`).
- **R2 (applied):** review/adoption metadata current — header Status and Result-review line, §6.17 heading and status, OPEN 20 flat-uniqueness line. B-∞ flat uniqueness stays `[OPEN]` (closure proposed); Lemma F, F1–F3 stay `[CAND]`; `DYAD-THM-FORMAL-Z6-GENERATOR` and `DYAD-ALG-NU5-P5` are reviewed draft entries, not adopted results.
- No mathematical change, no new RID, no numerical work.

### v6.4.13 — DRAFT r1, 18 October 2026 (draft record; not adopted)

- **Authorization:** PI work decision of 18 Oct 2026 — v6.4.13 drafting approved; Lemma F to independent review; scientific adoption a separate decision; B-∞ flat uniqueness not to be declared CLOSED before review.
- **Owner-grade additions (resting on adopted theorems):** DYAD-THM-FORMAL-Z6-GENERATOR (§6.16; uniqueness from Theorem C alone); analytic realization hierarchy and new OPEN 20 sub-item B-6 (B-6 ⟺ B-an ∧ B-3; B-6 ⇒ B-an); DYAD-ALG-NU5-P5 (M2c; exact certificate with $p=6$ calibration).
- **Candidate layer:** §6.17 DYAD-CAND-FLAT-CENTRALIZER (Lemma F) and DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES (F1–F3), `[CAND]` (review ACCEPTED in r1 review; adoption pending); OPEN 20 B-∞ split into existence (OPEN) and flat uniqueness (closure proposed, status OPEN).
- **Synchronization:** N1 answered; N2 answered for Genesis (Triadic pending); N7 receipts (RRF received, Genesis acknowledged, OFN pending); new notices N8 (M2c), N9 (J/B-6; candidate guard); §1 custody text; consumer-edition pins; Result-review line.
- **Unchanged:** all adopted RIDs and grades; §6.15 adopted statements (a pointer to §6.17 is added); G2 status; SG-14/15; the two carried v6.4.10 hashes still pending; N3 pending.

### v6.4.12 — adopted 16 October 2026

- **Adoption:** owner/PI decision of 16 Oct 2026 after external review of DRAFT r1 (`REVIEW ACCEPTED — OWNER ADOPTION PENDING`; Lemma K boundary correction, Theorem C, Corollary U and Corollary A accepted; OPEN 20 split accepted). r1 scientific text unchanged.
- **Release edits:** metadata (title, status, supersedes, labels, footer, N7 status); two reviewer record notes — (i) the closed-OPEN line now names both the lifecycle RID `DYAD-OPEN-FORMAL-CENTRALIZER` and the closing theorem RID; (ii) DYAD-ART-OPEN19-R0CERT records which review round reran which script.
- **Interface note (no DYAD claim):** `DYAD_RRF_OFN_G2_CONSOLIDATED_NOTE_v0_4.md` is noncanonical. Its polar-coordinate proof of Lemma K (ChatGPT) is an independent second derivation using only $\Re\mu\Im\mu\ne0$; it is a candidate for citation in a later revision, not imported here. Its §5b $h$-transported network construction is not a DYAD isolated-map theorem and is not owned here (RRF/OFN evaluation).
- **Carried open:** OPEN 20 (B-an, B-∞); N1–N3 and N7 PENDING; the two carried v6.4.10 hashes; G2 physical realization; K3 dimension split (Genesis-owned).

### v6.4.12 — DRAFT r1, 16 October 2026 (draft record; not adopted)

- **Trigger:** RRF owner decision `ACCEPT SCOPED` on `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_2.md`, order item 1 ("DYAD takes the all-degree proof and the proposed Corollary A into the owner version"); external review of SESSION v1.1 (ACCEPT).
- **OPEN 19 → CLOSED (formal):** new §6.16 with DYAD-ALG-CENT-KERNEL (Lemma K, all $k\ge2$), DYAD-THM-FORMAL-CENTRALIZER (Theorem C), DYAD-THM-FORMAL-INVOLUTION-UNIQUE (Corollary U, explicit $R_0=T^3F^{-1/2}$; no normalizer used); OPEN 19 block, closed list and §1 updated. The question as registered (normal-form return, $\lambda$-equivariance) is answered through the identification $\widehat S=R_0$.
- **RRF boundary correction applied:** Lemma K Step 2 now records the isolated output equation $\mu\bar c_{0,b}=0$ at $(b+2,0)$; Step 3 uses only $\mu\ne0$; the inaccurate statement that $(p,0)$ outputs give no condition is withdrawn (`[COR r1]`).
- **Corollary A:** DYAD-THM-ANALYTIC-CLOCK-BRIDGE in §6.15 — analytic $R$, $RT^6=T^6R$, $DR(0)=-I$ ⇒ $RT=TR$ exactly near $0$; $C^\infty$ gives only a flat commutator. The §6.15 `[OPEN]` paragraph on formal uniqueness is replaced by a pointer; DYAD-THM-LOCAL-INVOLUTION-GERM itself is unchanged.
- **New OPEN 20:** DYAD-OPEN-INVOLUTION-REALIZATION — (B-an) convergence of $R_0$ ⇔ of $F^{1/2}$; (B-∞) $C^\infty$ realization and flat uniqueness.
- **Registry:** protection-matrix rows (§5); notice N7 (§7); artifacts DYAD-ART-OPEN19-SESSION, -KERNEL, -R0CERT (§8); `cent.py` recorded as reviewer-reported cross-check only.
- **Owner checks for this draft:** kernel check PASS ($k=2..13$); $R_0$ certificate 7/7 PASS at $N=6,8,12$; new $a=0$ boundary check PASS ($b=0..7$) with failing negative control.
- **Unchanged:** all v6.4.11 RIDs and grades; G2 status (CONTRACT READY / PHYSICAL REALIZATION OPEN); SG-14/15; RRF OPEN-A; N1–N3 still PENDING; the two carried v6.4.10 hashes still pending.

### v6.4.11 — adopted 16 October 2026

- **Adoption:** owner/PI decision of 16 Oct 2026 after external final review of DRAFT r3 (scientific review PASS; no r4). Release edits are metadata only (title, date, status, supersedes, status-summary label, this entry, footer); r3 scientific text unchanged.
- **Carried open, not closed by adoption:** outbound notices N1–N3 (PENDING); two owner-measured hashes carried from the v6.4.10 manifest (P2-B v2 evidence zip, `check_owner_adoption.py`); OPEN 19; G2 physical realization; RECOG/NUMGEN certificates not rerun by Dyadic.
- Draft history follows (r3 → r1).

### v6.4.11 — DRAFT r3, 16 October 2026 (draft record)

- **R2-01 (release blocker, fixed):** §6.15 domain convention now requires $0\in\operatorname{int}(V_\Phi\cap R^{-1}(V_\Phi))$, so the fixed-point step and the differentiation at $0$ are justified without presupposing $R(0)=0$.
- **R2-02 (fixed):** §6.15(b) Taylor expansion of $R$ written with $o(|W|^3)$ (correct for $C^3$); cubic comparison unchanged.
- **D01 (carried from r1 review, fixed):** live "universal vanishing iff $b\le4$" statements (status summary, §2 item 4b, §2 evidence line, §6.11 boundary block, DYAD-ART-B5-SECULAR) restated as vanishing for $b\in\{2,3,4\}$ plus first failure at $b=5$; failure for all $b\ge6$ marked `[OPEN]`. Historical changelog lines quoting the old wording are left as history and are superseded by this entry. No result regraded; no computation.
- **D02 (carried from r1 review, fixed):** §6.14 "not established by this section" list now states at the same point that RECOG R8–R11 have since been closed in the consumer, at RECOG's grades, outside Dyadic custody.
- Unchanged: all §6.15 mathematics, OPEN 19, G2 status, SG-14/15, RRF OPEN-A.

### v6.4.11 — DRAFT r2, 16 October 2026 (draft record)

- **New §6.15:** DYAD-THM-LOCAL-INVOLUTION-GERM `[THM conditional]` — (a) primitive clock, $C^1$, lifted chart $|\eta|<\pi$; (b) six-step clock, $C^3$, six-phase tube, cubic chirality $\Im\mu\ne0$; (c) germ dichotomy and Bochner conjugacy. Part (b) is a Dyadic-owner strengthening of the G2-FIX argument (which had noted the loss of linear selectivity at $DT^6(0)=I$), accepted by external review (`ACCEPT SCOPED`). Domain stated in G2-DOM form.
- **New OPEN 19:** DYAD-OPEN-FORMAL-CENTRALIZER — formal tangent-to-identity centralizer; conditional reduction of $j^\infty R=\widehat S$ recorded, not proved.
- §5 high-risk row; §7 notice N6. Unchanged: G2 status (CONTRACT READY / PHYSICAL REALIZATION OPEN), SG-14/15, RRF OPEN-A. No numerical work.

### v6.4.11 — DRAFT r1, 16 October 2026 (draft record)

**Owner synchronization against the October 2026 corpus** (OFN v0.9, RRF v0.8, RECOG v0.3.20, NUMGEN v1.20.7, Genesis v2.8.5, Triadic v1.6, OPEN-M v0.7.1). Drafting authorized by the PI/reviewer decision of 16 Oct 2026 with these boundaries: preserve all v6.4.10 certificates and scientific RIDs; register the primitive-map definition provisionally; give the bridge exports a contract RID with per-item grades; import consumer results at owner grade/domain/version; register the degree-ten finite-chart result with provenance; correct OPEN-M deficit language, the Genesis residual reference and OPEN 12; do not broaden the physical meaning of cubic contraction, lattice memory or network symmetry; keep unresolved RID/provenance decisions visibly pending.
- **New registrations:** DYAD-DEF-PRIMITIVE-MAP (provisional; N1); DYAD-DEF-BRIDGE-EXPORT-CONTRACT (`[DEF]` list/typing) and DYAD-ALG-PROTECTION-MATRIX (RID for an existing `[ALG]` block); DYAD-ALG-Q-INVARIANT-FORM, DYAD-ALG-TAU-DETB, DYAD-ALG-CUBIC-PARABOLIC (known identities registered in the definition ledger, relayed by NUMGEN; not new results); DYAD-ALG-NF6-DEG10 + DYAD-ART-NF6-DEG10.
- **Imports / cross-references (owner grades, not rerun):** RECOG all-$p$ cubic radial contraction ($K_p$ family, $Z$-frame; OPEN 9 closed sub-item); general bridge-lemma proof (RECOG §6.12; Dyadic RID retained); RECOG chart laws and R9 lattice memory ($C_z$ track, stated windows); RECOG P₂ theorems (OPEN 12 → PARTIAL by consumer).
- **Corrections of currency:** §6.12 $E_{\rm odd}$ text updated to Genesis v2.8.5 typing; §1/§6.12/SG-15/§5 OPEN-M language updated to v0.7.1 (no certified numerical deficit); §7 consumer rows converted from "proposed, pending" to recorded acceptance with versions; companion pointer OFN v0.8 → v0.9.
- **Not done (deliberate):** no Dyadic RID for $\phi^*$ (N3); no re-registration of $S_h$ or the $\mathbb C^*$ rewrite (owned/registered in RECOG/RRF); no change to Programme Overview pointers; no new numerical campaign; install-manifest pending hashes from v6.4.10 still pending.
- **Dyadic-side checks performed for this draft (16 Oct 2026):** ν₃ closed form and $\Re\mu_p^Z$ at $p=5,6,7,12,50$; $6\bar\lambda\nu_3(\zeta_6)=3\mu^W$; $245/216$, $89\sqrt3/324$, $c_{\rm iso}$ and $G$; $\det B$, $\tau$; NUMGEN box bound $0.0665$; $\mathcal L J_Q\mathcal L^{-1}=i$ for the Genesis $J_Q$.

### v6.4.10 — September 2026 (adopted 24 Sep 2026)

**Local return-enclosure adoption (new §6.14) and normalization-object reconciliation:**
- New results: DYAD-ALG-NF6 (exact one-step normalizer $h$ through degree 6, six-step jet $J$, ledger identities $\mu=6\bar\lambda n_{21}$, $a_{05}=6\bar\lambda n_{05}$, $(3,2)$ iteration formula), DYAD-ALG-NF6-OBS (raw $c_{05}$ obstruction), DYAD-THM-PRIM-CTR $(108,\tfrac1{400},\tfrac1{625},\tfrac12)$ with six-phase tube and NUMGEN seed admission, DYAD-THM-NF-INV (injective on $|z|\le\tfrac1{10}$, inverse on $|W|\le\tfrac9{100}$), DYAD-THM-NF-REM (radius-indexed $C_7/C_D$: $\tfrac1{20}$: $100/1000$; $\tfrac1{40}$: $30/250$; full tube inside the normalized disk; normalized one-orbit contraction). `[THM]` entries carry the proof qualifier *analytic majorant + exact-rational certificate*; finite identities are `[ALG]`.
- New scope guard SG-19 (normalization-object guard): archival coordinate change / log-channel projection / polynomial conjugacy are distinct; finite jets stated with $\mathcal J_{\le6}$; no cross-operation coefficient transfer.
- Corrections at point of use `[COR]`: §1/§6.5 real-ray burst gains the nonzero half-power term $-\tfrac5{24}Q_0^{5/2}$; §6.7 raw complex-form remainder $O(|W|^5)\to O(|W|^4)$; §1 OPEN 13 "$h_3=0$" scoped to the archival return-log object (the conjugacy $h_3\ne0$); §6.9 operation labels added, $c_\theta$, $a_1$, $a_2$ explicitly not transferred pending R11.
- Registry `[COR]`: `jet1_deg5.json` relabelled raw one-step jet; `normalize_p6_liegauge_exact.py` regraded `[ALG]`→`[ENG]` with role/arithmetic metadata and its numerical tests under `[NUM]` scope; `gauge_bridge_p6.py` retagged `[ENG]`, no exit gate; `normalize_pstep_lie.py` labelled as projection; `homological_solver_p6_numeric.py` provenance note. New artifacts DYAD-ART-RE-P0P1 / -P2B2 / -REVIEWS / -REFEREE / -SUPPL.
- High-risk ledger: cross-operation coefficient transfer row. Appendix B: withdrawn $(64,\tfrac1{256},\tfrac1{1024})$ record (withdrawn, not falsified).
- Companion/methodology declarations updated to Programme Overview v1.2, Ontological Foundations v0.8, Methodology v1.3 (SG-14, §7, local grammar rule, footer reconciled; pre-existing entries not regraded; scoped migration limits stated). §7 gains proposed consumer rows (RECOG, NUMGEN; acceptance pending) and its blanket no-import statement is narrowed to the self-contained local core.
- Final (adoption): metadata set to adopted; "proposed" removed from the $E_{\rm odd}$ diagnostic definition only (physical/consumer bridge stays `[OPEN]`); §1 micro-edit ("a different symmetrized observable"); installation manifest referenced.
- r3 (final text patch, r2 review): C04 propagated to all live uses (status summary, §1, §6.5 DEF, §6.8 note; duplicate high-risk row merged; DSI logarithmic transport retained as a historical fitting ansatz `[DEF]`, not `[ALG]`); C05 narrowed to a typed diagnostic export $E_{\rm odd}$ with cubic parts in $(s_*,w_*)$ variables and the physical/consumer bridge `[OPEN]` (SG-13/§7 notes); notation: resonant *monomial coefficients*, $F_W$ conjugated by $H_2=\mathrm{id}+h_2$, channel projector $\mathscr P_{\rm keep}$ vs polynomial $P$.
- Draft-review corrections applied (D6410-C01–C08): §6.9 conjugacy residual vs coefficient gap; §6.2 $W$-component quintic resonance list; §6.7 real-vector remainder $O(\|X\|^4)$ and ray quartic; §1/§6.5 $47/54$ scoped as the raw fixed-radius angular mean $\mathcal A_{\rm raw}$ with the pointwise/long-orbit identification `[OPEN]`; §6.12 birth-residual typing ($E_{\rm raw}/E_{\rm odd}/E_{\rm NF}$); §6.14 definitions ($\lambda$, $H$, $S_j$, $P$, $D_{\rm poly}$, $Q_m$ vs $q_m$, $h$-table path); §8 artifact roles split from numerical evidence and archive contents named exactly.
- Unchanged: all pre-existing scientific-result RIDs and grades, $c_{21}$, the number $47/54$ (now scoped as the raw angular-mean coefficient $=[W^3\bar W^3]\Delta Q_6$), OPEN 9 program, all-$b\ge5$ persistence `[OPEN]`. Not closed: RECOG R8/R9/R10/R11, quantitative GAP-LOCK, historical $\Phi_1$ byte identity, optimality.

### v6.4.9 — June 2026

**Cubic cascade $q=4,(0,3)$ all-$p$ closure (new theorem):**
- Closed the OPEN 9 cubic cascade formula for $q=4,(0,3)$ all-$p$ on the family $p=4s$, $s\ge2$: $Q_p=i\zeta_p^3 M_p$ with $M_p\in\mathbb{Q}(\zeta_p)^+$, closed form $Q(L,I)=L^5(IL^2+I-L^2+1)/(2(L+1)^4(L^2+L+1))$ (DYAD-THM-Q403-PHASELAW, §6.11). $p=8$ is the zero degeneracy ($Q_8=0$).
- Proof: degree-3 near-identity recursion $(\mathcal H_s)_3=\sum_j H_{j,3}+\sum_{j<k}DH_{k,2}\cdot H_{j,2}$; degree counting bounds insertion depth to $\le2$, giving exactly three contributing paths (one cubic cancelling by $S_{-4}=0$ = LEAD; two ordered quadratic–quadratic). Remainder relation $\sigma_{-1}(Q)=-L^{-6}Q$ proved as an exact symbolic identity over $\mathbb{Q}(I)(L)$; supporting links $\lambda^{-s}=-i$, reality, leading cancellation all all-$p$ `[THM]`.
- Verification: closed form matches the certified in-field extractor at $p=8,12,\dots,52$ (independent method); three-path derivation, $h$-coefficient cross-check, and the $\sigma_{-1}$ identity all symbolic. Artifacts DYAD-ART-Q403-CERT (`q4_03_R_identity_certificate.py` → CERTIFICATE PASS) and DYAD-ART-Q403-EXTRACT registered.
- Scope discipline: family statement for $p=4s$ via the forced collapse $I=\zeta_p^{p/4}=i$; NOT a generic-$s$ formula (the generic-$s$ cascade differs). The earlier `[FAIL]` "universal cancellation" line is retained with a scope note (channel survives $p\ge12$); the surviving value is now characterized by the theorem.
- Updated: status summary, §2 frontier (lines for OPEN 9 cubic cascade → CLOSED), high-risk ledger, artifact registry. Single core-end marker preserved. all-$b\ge5$ persistence, universal missing-slot rules, and general-coefficient version remain `[OPEN]`.

### v6.4.8.1 — June 2026

**Stale-line hygiene patch (no scientific change):**
- §2 evidence/candidate line still listed the all-$p$ ($p\ge6$) monotone failure among `[OPEN]` items and tagged the $p=6..15$ scan `[NUM strong]`, both superseded by the v6.4.8 closure. Corrected to state the all-$p$ theorem is `[ALG]` (closed via cyclotomic non-division). The §status-summary and §6.11 block were already correct.
- Residual "broader $p=6..15$ scan `[NUM strong]`" wording now appears only in historical changelog entries (v6.4.2/v6.4.3), which is correct.
- all-$b\ge5$ persistence and general-coefficient version remain `[OPEN]`. Single core-end marker preserved.

### v6.4.8 — June 2026

**DYAD-OPEN-B5-ALLP CLOSED — all-$p$ theorem proved `[ALG]`:**
- The open all-$p$ statement $F_{\rm raw}^p(0,5)\ne0\ \forall p\ge6$ is now a theorem. Closing step: the effective ratio $S_{\rm eff}/S$ is the explicit rational $N/D$ with $N=2\lambda^6+\lambda^5-5\lambda^4-3\lambda^3-4\lambda^2+2\lambda+1$ (re-derived from the $\beta$-graded engine, confirmed identical to the reviewer's closed form). Since $\deg N=6$, a primitive $p$-th root is a zero of $N$ only if $\Phi_p\mid N$, possible only for $\varphi(p)\le6$ (finite set $\{1..10,12,14,18\}$); exact division shows $\Phi_p\nmid N$ for all of them. Hence $N(\lambda_p)\ne0$ for all $p$, so $S_{\rm eff}\ne0$ for all $p\ge13$. With the exact sweep $p=6..12$, $F_{\rm raw}^p(0,5)\ne0$ for ALL $p\ge6$. This is a complete proof (degree bound $\Rightarrow$ finitely many candidate $p$), not a scan.
- §6.11 boundary block rewritten: "universal pure anti-holomorphic raw vanishing holds iff $b\le4$, and fails at $b=5$ for every $p\ge6$" `[ALG]` (dyadic map). Previously `[NUM strong / ALG candidate]` for the all-$p$ extension.
- The $\mathrm{Re}(S_{\rm eff}/S)>0$ numeric scan (DYAD-ART-B5-SEFF, `[NUM strong]`) is now superseded by the exact cyclotomic argument; retained as cross-check.
- §8: artifact DYAD-ART-B5-ALLP-CERT registered (the fast certificate proving the all-$p$ closure).
- Remaining `[OPEN]` (separate problems): all-$b\ge5$ persistence; general-coefficient (non-dyadic) version.
- No change to any prior `[ALG]` result.

### v6.4.7 — June 2026

**Artifact-trail correction (no scientific change):**
- The v6.4.6 `[ALG]` claim $\lim_{\lambda\to1}S_{\rm eff}/S=3$ was reported from local work but the registered artifact `rtg_b5_step3_Seff.py` only performed the numerical $\mathrm{Re}(S_{\rm eff}/S)>0$ scan, not the symbolic limit. Added a dedicated executable certificate `rtg_b5_Seff_limit_cert.py` that builds the $(0,5)$ source, extracts $S$ and $c_{(-2,1)}$, substitutes the exact dyadic $c_{ab}(\lambda)$, forms $S_{\rm eff}/S$, and computes $\lim_{\lambda\to1}=3$ symbolically (passes, exit 0). The `[ALG]` tag on the limit is now backed by an executable certificate.
- DYAD-ART-B5-SEFF re-tagged `[NUM strong]` (numeric scan only); new artifact DYAD-ART-B5-LIMIT-CERT `[ALG]` carries the exact limit.
- No change to any result; this is artifact-discipline hygiene.

### v6.4.6 — June 2026

**Step 3 reduction of the all-$p$ boundary theorem (DYAD-OPEN-B5-ALLP):**
- New `[ALG]` results. For $p\ge13$: every $m=0$ nonsecular source mode of $(0,5)$ vanishes exactly (geometric sum $\sum_k\lambda^{(\beta-1)k}=0$ since $p\nmid(\beta-1)$ for $\beta-1\in\{-6,\dots,-1,1\}$), and the sole polynomial mode $(-2,1)$ has exact sum $\sum_{k=0}^{p-1}k\lambda^{-3k}=-p/(1-\lambda^{-3})$. Hence the exact identity $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{\rm eff}$ with $S_{\rm eff}=S-c_{(-2,1)}/(1-\lambda^{-3})$.
- New `[ALG]`: $\lim_{\lambda\to1}S_{\rm eff}/S=3$ (exact symbolic), the asymptotic anchor. Validated: $p|S_{\rm eff}|$ matches direct iteration for $p=13..23$.
- The open all-$p$ theorem is thereby reduced to a single scalar nonvanishing: $S_{\rm eff}\ne0$ for all $p\ge13$ (equivalently $\mathrm{Re}(S_{\rm eff}/S)>0$), `[NUM strong]` to $p=200$ (monotone $\to3$). With $p=6..12$ closed by exact sweep, only an explicit error bound for finite $p\ge13$ remains for full `[ALG]`.
- §8: artifacts DYAD-ART-B5-STEP3 (reduction) and DYAD-ART-B5-SEFF (S_eff analysis) registered.
- No change to established `[ALG]` results.

### v6.4.5 — June 2026

**Hygiene patch (no scientific change):**
- Adopted the fixed Step-2 evaluator `rtg_b5_secular_decomposition.py` (the prior upload left unevaluated symbolic summations after substituting $p$, raising a float-conversion error; the fix evaluates the nonsecular Duhamel contribution at fixed $p$ as the finite sum $\lambda^{p-1}\sum_{k=0}^{p-1}k^m\lambda^{(\beta-1)k}$). Reconstructs swept values $p=6..12$ (match) and the ratio-to-3 trend $p=7..15$.
- Artifact DYAD-ART-B5-DECOMP tag split: `[ALG structure]` (decomposition) / `[ALG validation]` ($p=6..12$ reconstruction) / `[NUM strong]` (ratio-to-3 trend), rather than a single `[ALG structure]` umbrella.
- Softened the non-cancellation wording: the ratio staying far from the cancellation point is `[NUM strong]`, not a proof; proving $R_p/(p\lambda^{p-1}S)\ne-1$ for all $p$ is Step 3 and remains `[OPEN]`.
- Step 3 scope sharpened: $p=6..12$ closed by exact sweep, so only $p\ge13$ needs the ratio bound.
- No change to any `[ALG]` result.

### v6.4.4 — June 2026

**Secular decomposition of the first failing channel (DYAD-OPEN-B5-ALLP Step 2):**
- §6.11 / new result note: exact decomposition $F_{\rm raw}^p(0,5)=p\lambda^{p-1}S_{05}^{(\beta=1)}+R_p$ `[ALG structure]`, where $S_{05}^{(\beta=1)}$ is the five-term secular source coefficient ($\propto c_{02}^2$, nonzero) and $R_p$ is the nonsecular + polynomial-mode residual. The $(0,5)$ source has nine modes with a single secular mode $(1,0)$ and a single polynomial mode $(-2,1)$.
- Validated: the decomposition reconstructs all swept exact values $p=6..12$ to full precision.
- Structural discovery: the complex ratio $F_{\rm raw}^p(0,5)/(p\lambda^{p-1}S)\to3$ as $p\to\infty$ (real part $\to3$, imaginary $\to0$); equivalently $R_p\sim2p\lambda^{p-1}S$. This reduces the open all-$p$ theorem to a single ratio-bound (Step 3): prove $R_p/(p\lambda^{p-1}S)\ne-1$ for all $p\ge6$.
- §8: artifact DYAD-ART-B5-DECOMP registered.
- No change to established `[ALG]` results (b∈{2,3,4} vanishing, source coeff, $p=7$ witness, $p=6..12$ sweep).

### v6.4.3 — June 2026

**Exact finite sweep of the first failing channel (DYAD-OPEN-B5-ALLP Step 1):**
- §6.11 channel boundary: $F_{\rm raw}^p(0,5)\ne0$ promoted from `[NUM strong]` to `[ALG finite sweep]` for ALL of $p=6,7,8,9,10,11,12$ — exact cyclotomic certificates in $\mathbb{Q}(\zeta_p)$, each a canonical reduced nonzero element (e.g. $p=6$: $\tfrac{43}{360}\lambda+\tfrac{7}{36}$; $p=8$: $-8\lambda^3+\tfrac{27}{2}\lambda^2-\tfrac{23}{2}\lambda+\tfrac52$; $p=10$: $-\tfrac54\lambda^3+\tfrac94\lambda^2-\tfrac94\lambda+\tfrac12$). Magnitudes match the prior direct-iteration scan exactly.
- $p=13,14,15$ remain `[NUM strong]` (not yet exactly swept). The all-$p$ ($p\ge6$) theorem remains `[OPEN]` (Steps 2–3: general secular decomposition + non-cancellation proof).
- §8: artifact DYAD-ART-FRAW-B5-SWEEP registered.
- No change to the $b\in\{2,3,4\}$ `[ALG]` results, the source-level `[ALG]` coefficient, or the $p=7$ exact witness.

### v6.4.2 — June 2026

**Exact final-coefficient witness closes the micro-gap at p=7:**
- §6.11 channel boundary: the residual `[NUM strong]` final-coefficient gap is closed for the witness prime $p=7$. Exact cyclotomic 7-fold iteration (degree-5 truncation, field reduction mod $\Phi_7$) gives $F_{\rm raw}^7(0,5)=\tfrac{15}{2}\lambda^5+\tfrac{23}{8}\lambda^4+\tfrac{21}{8}\lambda^3+\tfrac{15}{2}\lambda^2-\tfrac18\lambda+\tfrac{17}{2}\ne0$ in $\mathbb{Q}(\zeta_7)$ `[ALG]` (canonical reduced degree-5 form; numeric $0.1289-0.2062i$, $|{\cdot}|=0.2432$, matching the 60-dps iteration to 12 digits).
- Dyadic boundary statement promoted to `[ALG]`: **universal pure anti-holomorphic raw vanishing holds through $b=4$ and fails at $b=5$**, with the $b=5$ failure certified by the exact $p=7$ witness. (Was `[ALG]` source-level / `[NUM strong]` final-coefficient in v6.4.1.)
- Scope guard retained: the exact witness is for $p=7$; it does NOT assert $F_{\rm raw}^p(0,5)\ne0$ for every $p\ge6$. The all-$p$ monotone failure remains `[OPEN]` (broader $p=6..15$ scan is `[NUM strong]`).
- Script fix: `exact_Fraw7_certificate.py` corrected — the cyclotomic inverse used `gcdex` with the wrong return-value order; replaced with `sp.invert(den_p, Phi)`. (External reviewer caught the bug and supplied the corrected engine; reproduced and verified here: exact polynomial confirmed in canonical reduced form, numeric value matches independent direct iteration.)
- §8: artifact DYAD-ART-FRAW7-B5 registered.
- No change to $b\in\{2,3,4\}$ `[ALG]` vanishing results or the source-level `[ALG]` coefficient.

### v6.4.1 — June 2026

**Wording correction (separate source-level `[ALG]` from final-coefficient `[NUM strong]`):**
- §6.11 channel boundary: v6.4 stated "$b=5$ breaks universal vanishing `[ALG]`", conflating two distinct objects. Corrected: the $(0,5)$ SOURCE secular coefficient ($\beta=1$ slot) is exactly nonzero `[ALG]` (five-term $\propto c_{02}^2$, not identically zero; dyadic $p=7$ reduces to $\tfrac{11}{56}\lambda^5-\tfrac{13}{56}\lambda^4+\tfrac14\lambda^3-\tfrac{11}{56}\lambda^2+\tfrac{3}{14}\lambda-\tfrac{3}{28}\ne0$ in $\mathbb{Q}(\zeta_7)$, exact). The FINAL raw coefficient $F_{\rm raw}^p(0,5)$ nonvanishing is `[NUM strong]` (60 dps; $|F_{\rm raw}^7(0,5)|=0.243$; secular growth $0.27\to1.28$), pending an exact $\mathbb{Q}(\zeta_p)$ certificate of the final coefficient.
- Net boundary statement unchanged in substance ("vanishing through $b=4$; first secular obstruction at $b=5$") but now correctly tagged `[ALG]` source-level / `[NUM strong]` final-coefficient.
- §2: residual micro-gap (exact $F_{\rm raw}^p(0,5)$ certificate) added as a distinct `[OPEN]` item.
- Credit: exact $p=7$ source-coefficient reduction supplied by external reviewer; reproduced.
- No change to $b\in\{2,3,4\}$ `[ALG]` vanishing results.

### v6.4 — June 2026

**Channel boundary "$b\le4$ iff" promoted to `[ALG]` for the dyadic map:**
- §6.11 channel-classification block rewritten: the $b=5$ failure is now `[ALG]`, not numerical. The $(0,5)$ source secular coefficient (slot $(1,0)$, $\beta=1$) was extracted by one $F$-application on the degree-$\le4$ jet (no secular recursion solved) and is the five-term expression $\propto c_{02}^2$: $\{c_{02}^3\bar c_{02},\ c_{02}^2c_{11}c_{20}(\times2),\ c_{02}^2c_{11}\bar c_{11},\ c_{02}^2c_{21}\}$. It is NOT identically zero (symbolic) and NONZERO at the actual dyadic coefficients ($|{\cdot}|\approx1.2$–$1.3\times10^{-2}$, $p=6,7,8$).
- Consistency: nonzero $\beta=1$ source $\Rightarrow$ resonant accumulation $A^p\sim C p\lambda^{p-1}$; direct iteration confirms $|F_{\rm raw}^p(0,5)|$ grows $0.27\to1.28$ for $p=6..15$.
- Result: for the dyadic map, **universal pure anti-holomorphic raw vanishing holds iff $b\le4$** `[ALG]`. (Was `[NUM strong / ALG candidate]` in v6.3.)
- §2 priority item 4b marked `[COMPLETED v6.4]` for the dyadic boundary; active frontier refocused on the all-$b\ge5$ monotone-failure extension and the general-coefficient (non-dyadic) version, both `[OPEN]` (the secular coefficient is nonzero on a Zariski-open set containing the dyadic values; scan confirms $b=6$ also secular).
- §8: certificate rtg_extract_b5_secular_coeff.py registered.
- No change to the $b\in\{2,3,4\}$ `[ALG]` results.

### v6.3 — June 2026

**Channel boundary at b=4 sharpened (b=5 secular entry confirmed):**
- §6.11 channel-classification block: recorded that the secular mode $\beta=1$ ENTERS the $(0,5)$ source $\beta$-set $\{-5,-4,-3,-2,-1,0,1,2\}$ (plus a polynomial mode $(-2,1)$), breaking universal vanishing at $b=5$. Direct iteration of the actual dyadic map confirms $F_{\rm raw}^p(0,5)\ne0$ for all tested $p=6..13$ (vs $b=4$ machine-zero for $p\ge6$).
- Boundary statement "universal vanishing iff $b\le4$" upgraded from conjecture to `[NUM strong / ALG candidate]` (was `[NUM strong / CAND]`): the $b=5$ failure is now directly evidenced, not merely "tested generically nonzero." Full `[ALG]` boundary awaits a symbolic nonzero-coefficient certificate for the $b=5$ secular source.
- §2: active sub-item refocused on symbolically certifying the $b=5$ secular coefficient; evidence-line updated.
- Adopted patched engine rtg_betagraded_vanishing.py v1.1 (records each source $\beta$-set at generation time, avoiding the reporting hang at MAXDEG$\ge5$ once secular modes appear). README updated to v1.1.
- No change to the $b\in\{2,3,4\}$ `[ALG]` results (v6.2); they remain certified.

### v6.2 — June 2026

**Degree-b vanishing promoted `[NUM strong / ALG candidate]` → `[ALG]` for b=3,4:**
- §6.11: $F_{\rm raw}^p(0,3)=0$ for $p\ge5$ and $F_{\rm raw}^p(0,4)=0$ for $p\ge6$ promoted to `[ALG]` (RIDs DYAD-CAND-VANISH-B3/B4 → DYAD-ALG-VANISH-B3/B4). Proof: automatic $\beta$-mode path enumeration via $\beta$-graded jet composition (enumerates ALL cascade paths, resolving the gap the $p=3,b=3$ counter-instance exposed). Source $\beta$-sets: $(0,3)=\{-3,-2,0\}$, $(0,4)=\{-4,-3,-2,-1,0,2\}$; neither contains the secular mode $\beta=1$, and breaker primes are bounded by $b+1$, so vanishing holds for $p\ge b+2$.
- Doubly certified: exact symbolic evaluation at primitive $p$-th roots + direct 50–60 dps iteration. Certificate degree_b_vanishing_cert_v2.py passes (two independent representations).
- §3 SG-16 RELAXED (not deleted): $b\le4$ now certified `[ALG]`; $b\ge5$ still requires a source $\beta$-set certificate before any promotion.
- §2 priority item 4 marked `[COMPLETED v6.2]`; two proof-task sub-items closed; active frontier refocused on the $b\ge5$ channel-boundary classification.
- §6.11 channel-classification boundary: $b\in\{2,3,4\}$ all `[ALG]`; the "$b\le4$ iff" boundary remains `[NUM strong / CAND]` pending the $b\ge5$ $\beta$-set scan.
- §8: certificate and engine artifacts registered.

### v6.1 — June 2026

**Low-degree anti-holomorphic vanishing (`[ALG candidate]` → split tags, ranges corrected):**
- §6.11: $F_{\rm raw}^p(0,2)=0$ for $p\ge4$ promoted to `[ALG]` (degree 2 admits no cross-path: any cross-term has degree $\ge4$). [RID: DYAD-ALG-VANISH-B2]
- §6.11: $F_{\rm raw}^p(0,3)=0$ for $p\ge5$ and $F_{\rm raw}^p(0,4)=0$ for $p\ge6$ are `[NUM strong / ALG candidate]` — direct-term mechanism exact, cross-path enumeration open. [RID: DYAD-CAND-VANISH-B3, DYAD-CAND-VANISH-B4]
- Direct-accumulation weight corrected to $\lambda^{-(b+1)k}$ (resonant exception $p=b+1$); ranges corrected to $p\ge b+2$. The first-draft weight $\lambda^{-bk}$ and "also $p=3$" claims were errors, removed.
- §6.11: exact lemmas registered separately: direct-weight vanishing `[ALG, exact]` (DYAD-ALG-DIRECT-WEIGHT); cross-term cyclotomic identity `[ALG, exact]` (DYAD-ALG-CROSS-IDENTITY).
- §6.11: channel boundary $b=4$ `[NUM strong / CAND]`.
- §3 SG-16 `[NEW]`: path-enumeration guard.

**OPEN-P0-DYADIC partial absorption (structural leg only):**
- §6.2 `[NEW ALG, exact]` (DYAD-ALG-P6-FACEFLUX): $\lambda=e^{i\pi/3}=e^{iF_f/2}$.
- §6.6 `[NEW]`: p=6 SU(2) period selection, scoped to OPEN-P0 representation-phase convention.
- §6.11/§6.12 `[NEW]`: R11 gate conversion `[ALG, exact]`, physical threshold `[HYP inherited]`; h-transfer `[CAND/conditional]` (DYAD-CAND-P0-DYADIC).
- §3 SG-15 `[NEW]`: OPEN-P0-DYADIC scope guard.
- §5 High-Risk: six rows added. §7 exports updated. §8: two artifacts registered.

**Two review rounds applied before freeze:**
- R1: phase factor $\lambda^{-bk}\to\lambda^{-(b+1)k}$; ranges $p\ge b+2$; false "also $p=3$" removed; h-transfer downgraded to `[CAND/conditional]`.
- R2: vanishing tag downgraded `[ALG]`→`[NUM strong / ALG candidate]` for $b=3,4$ (path enumeration not closed, per $p=3,b=3$ counter-instance); R11 gate threshold scoped `[HYP inherited]`; artifact tag corrected to `[NUM strong]` for finite scan.
- R3: $b=2$ split out as genuine `[ALG]` (degree-2 admits no cross-path — complete proof).

**v6.1 freeze note:** Final review applied. §6.11 p=6 one-step lattice coefficient $c_{05}^{(1,6)}$ corrected to $\frac{43}{17280}-i\frac{227\sqrt3}{155520}$ (one-step engine/DSN bridge convention), avoiding conflation with the §6.9 raw six-step Lie-gauge coefficient $-61/2160-i\,43\sqrt3/6480$. The two values belong to distinct ontology layers (raw six-step Lie-gauge ≠ one-step p=6 lattice).

### v6.0 — June 2026

Full refactor to DSN_METHODOLOGY_v1.2 architecture. All active scientific ledger content preserved; structure changed throughout.

Errata applied before canonical freeze:
- **§1 [COR]:** split fixed-point `[ALG]` claim from `[DEF]` dyad-map claim-block; compressed OPEN 9 §1 entry; removed `[ALG candidate]` low-degree vanishing from §1 (detail belongs in §6.11).
- **§3 [COR]:** corrected SG-3 cross-reference from §6.10 to §6.11.
- **§5 [COR]:** softened $G_{04}(10)=0$ high-risk row to distinguish exact `[ALG]` reinterpretation from still-open `[ALG candidate]` universal pattern.
- **§2 [COR]:** normalized OPEN 9 retracted sub-item tags to `[RETRACTED]` `[scope: reframed]` and `[FAIL]` `[scope: obsolete heuristic]`.
- **§6.1/§6.2/§6.10 [COR]:** marked mixed-status section headings explicitly with `/ mixed`.
- **§8 [COR]:** replaced noncanonical `[NUM diagnostic]` with `[NUM]` `[scope: diagnostic]`.

Final errata applied before freeze:
- **Local Tag Aliases [COR]:** Removed unused `[REJ]` and `[FAIL to confirm]` migration rows; DEF note updated to reflect normalization is complete.
- **§2 OPEN 9 [COR]:** `[ALG candidate]` degree-4 raw-vanishing pattern moved from closed sub-items to new "Evidence / candidate patterns" block; corresponding `[OPEN]` for universal proof added to active sub-items.
- **§2 OPEN 4b [COR]:** Compound tag `[OBS / ALG structure]` split to `[OBS]` `[ALG structure]`.
- **§3 SG-4 [COR]:** "exact six-step discrete map" → "exact six-step finite iterate of the primitive map" (avoids confusion with TDR-G discrete programme).
- **§4 layer routing table [COR]:** "Exact discrete map" → "Exact primitive map".
- **§6.1 heading [COR]:** `[DEF / ALG / mixed]` → `[ALG / mixed]` (internal `[DEF]` on map entry is sufficient).
- **§6.6 [NEW]:** $p=6$ uniqueness `[THM]` and three-tier resonance hierarchy `[THM]` added.
- **§6.12 [COR]:** Bridge export boundary tagged `[DEF]` `[scope: bridge export boundary]`.
- **§7 [NEW]:** Export protocol block added (three `[DEF]` entries: generator-T scope, convention tagging, export scope limits).
- **Appendix A marker string [COR]:** Literal HTML marker string → plain text.
- **Appendix B [COR]:** Sub-horizon conjecture `[FAIL]` `[scope: retracted / reframed]` → `[RETRACTED]` `[scope: reframed]`.

- **Header:** Updated title to `RTG_DYADIC_OSCILLATOR_DSN`; added programme tier, companion documents, DSN methodology reference.
- **Changelogs v5.4.5–v5.4.16 [MOVED]:** Entire blockquote changelog preamble (~120 lines) moved to Appendix A subsections below.
- **Status tag table [REMOVED]:** Replaced by pointer to `DSN_METHODOLOGY_v1.2` + Local Tag Aliases.
- **§17 Ground Truth Compression [PROMOTED]:** Becomes §1 Current Canonical State with explicit DSN tags on each claim-block.
- **§14 OPEN Registry [RESTRUCTURED]:** Prose OPEN entries → structured ledger format with RIDs, Closed/Active/Retracted sub-items. OPEN 9 paragraph → structured sub-item ledger.
- **§15 Simulation Invariants [MOVED]:** → §6.13 with anchor.
- **§16 Priority Defaults [MOVED]:** → §2 priority ordering subsection.
- **§15.2 / §15.3 Artifact tables [CONVERTED]:** → §8 structured list format with RIDs.
- **Scope Guards [RENUMBERED]:** SG-1 through SG-14; `[!]` blockquote format → `**[SG-N]**` format. Added SG-14 (programme-level cross-branch firewall).
- **Collaboration Identity [MOVED]:** → §9.
- **All §6 subsections:** Added `{#sec-N-M-slug}` persistent anchors.
- **AI Context Core marker:** Inserted at end of §4.

### v5.4.16 — June 2026

- §10.7: cardinality lemma $|K^{\rm extra}_{p,q}|=s-1$ `[ALG]`.
- §10.7b: eigenframe linear-part lemma anchoring degree-2 no-cascade bypass `[ALG]`.
- §10.7/§10.13/§14: unified $G_{04}(10)=0$ retraction wording.
- §10.13: replaced `[REPLACED AS CANONICAL]` with `[REJ / obsolete heuristic]`; near-cancellation modulus $|{-13+15\sqrt3/2}|\approx0.010$ archived.
- §15.3: expanded `rtg_invariant_algebraic_engine_surgical.py` role.
- §17: updated ground-truth compression.

### v5.4.15 — June 2026 (carried forward patch)

- §10.7: replaced rectangular-support heuristic with subgroup-charge projector formalism.
- §10.7b: exact subgroup-strobe micro-certifications and degree-2 $q=3,(0,2)$ cancellation theorem.
- §10.13: universal $q=4,(0,3)$ cancellation `[FAIL]`; $p=12,q=4,(0,3)$ cascade boundary exact.

### v5.4.14 — May 2026

- $F_{\rm raw}^p(0,4)=0$ universally for tested $p\ne5$ `[ALG candidate]`.
- Sub-horizon channel conjecture `[RETRACTED / REFRAMED]`.

### v5.4.13 — May 2026

- $G_{04}(15)\approx0$ `[NUM strong / ALG candidate]`.
- $G_{06}(21)\ne0$ `[NUM strong]`.

### v5.4.12 — May 2026

- §10.12.3: interpretation refined; sub-horizon-resonant channel phrasing.

### v5.4.11 — May 2026

- $G_{06}(7)\ne0$: prime-horizon transparency `[FAIL]`.
- $G_{04}(10)=0$ `[ALG]` confirmed.

### v5.4.10 — May 2026

- $p=5$ primary lattice bridge cancellation promoted to `[ALG]` via exact cyclotomic arithmetic over $\mathbb{Q}(\zeta_5)$.

### v5.4.9 — May 2026

- $W=u+iv$ labeled as $p=6$ primitive frame, not generic.
- One-step to $p$-step bridge lemma $\mu_p=p\bar\lambda\nu_3^{(1,p)}$ `[ALG]`.

### v5.4.5 — May 2026

- OPEN 11 sharpened closure: T1/F1 residual-free `[ALG via IA]` via IFT transversality certificate.

---

## Appendix B — Retired and Rejected Claims {#appendix-b}

`[RETRACTED]` `[scope: withdrawn as unsupported delivery, not falsified]` **(v6.4.10)** Primitive contraction constants $(C_6,q_{\rm ctr},q_{\rm in})=(64,\tfrac1{256},\tfrac1{1024})$ with a displayed remainder bound $53.3157$: advertised in a working message without a delivered proof; the same-named archive documented $(1560,\tfrac1{3600},\tfrac1{10000})$ instead. Withdrawn as an unsupported delivery record. A looser proved bound does not falsify it; do not import on the authority of that message. Operative profile: DYAD-THM-PRIM-CTR (§6.14).

`[RETIRED wording]` **(v6.4.10)** "$jet1\_deg5.json$ = one-step normalized coefficient dictionary" (it is the raw one-step jet); "$O(|W|^5)$" for the raw complex form; the real-ray burst without the $Q_0^{5/2}$ term; and any reading of the archival "$h_3=0$" as a property of the one-step polynomial conjugacy. See COR items in Appendix A v6.4.10.

- `[FAIL]` $6\phi^2$ as crossing target.
- `[FAIL]` $\Im(\nu_5)$ invariant under general real-analytic residual gauge — gauge derivative $d\Im(u_{32})/d\lambda=-4\sqrt{3}/3\ne0$ computed exactly.
- `[FAIL]` Universal $q=4,(0,3)$ cancellation — $p=12$ provides exact counterexample.
- `[RETRACTED]` `[scope: reframed]` Sub-horizon inheritance conjecture — replaced by the degree-4 raw-vanishing pattern, `[v6.4.20]` since proved: DYAD-ALG-VANISH-B4 `[ALG]` (v6.2) for $p\ge6$. (v6.4.19 wording: "universal proof remains open".)
- `[FAIL]` `[scope: obsolete heuristic]` Rectangular $M(D)$ support counting — superseded by reachable-basis projector formalism.
- `[FAIL]` `[scope: not confirmed]` OPEN 4b itinerary-shift mechanism — reclassified as window-dependent problem.
- `[BOUNDARY NOTE]` Degree-$b$ vanishing edge cases: $F_{\rm raw}^p(0,b)$ is NONZERO at $p=b+1$ (direct-resonant, weight $\lambda^{-(b+1)}=1$) and, for $b\ge3$, at one additional small $p$ below the clean range ($p=3$ for $b=3$; $p=4$ for $b=4$) from cross-contributions. Clean vanishing holds only for $p\ge b+2$. State the results with range "$p\ge b+2$", never "$p\ne b+1$".

---

## Appendix C — Notation {#appendix-c}

`[DEF]` `[v6.4.20]` Symbols with more than one meaning in this ledger, and symbols that consumers read differently. Read an overloaded symbol by its section.

| Symbol | Meaning(s) | Where | Guard |
|---|---|---|---|
| $T$ | primitive dyad map (DYAD-DEF-PRIMITIVE-MAP); in §6.11 also the map family with $K_p$ | §1, §6.1, §6.11 | family parameter stated when $p\ne6$ |
| $F$, $F_W$, $\widehat F$ | $F=T^6$; $F_W=\mathcal L T^6\mathcal L^{-1}$ (raw $W$-frame); $\widehat F=h^{-1}F_Wh$ (chart) | §6.7, §6.14, §6.16 | raw, archival, projected and conjugated returns are distinct (SG-19) |
| $J$ | (i) Jacobian $DT$ in §1/§6.1; (ii) six-step normal-form jet in §6.14; (iii) ℤ₆ generator $T\circ F^{-1/6}$ in §6.16–§6.17 | see column | read by section; $J_Q=\mathcal L^{-1}i\mathcal L$ is the rotation defined and used in §6.12 (birth kinematics; Genesis/Triadic notation) |
| $h$, $h_6$, $n$ | degree-6 additive normalizer; one-step normal-form jet | §6.14 | archival $\Phi_{\rm archive}$ is a different operation |
| $\mu$, $\mu_p$ | six-step cubic coefficient $-\tfrac12-i\tau$; frame-dependent $\mu_p^Z$, $\mu_p^{W_p}$ | §6.2, §6.7, §6.9, §6.11 | compare across frames only with DYAD-ALG-KP-FRAME-SCALE |
| $\tau$ | $2\sqrt3/3$ | §6.3 | — |
| $\lambda$ | (i) $e^{i\pi/3}$; (ii) $e^{2\pi i/p}$ in the $K_p$ family; (iii) $\lambda_{\rm DSI}=e^{\pi\sqrt3}$; (iv) $\lambda_\pm$ saddle eigenvalues | §6.1–§6.3, §6.11 | context fixes $p$ |
| $Q_{\rm true}$, $Q_{\rm prim}$, $Q_m$ | primitive quadratic observable $\vert W\vert ^2$; block samples $Q_m=Q(T^{6m}x)$ | §1, §6.5, §6.14 | not the chart variable $q=\vert z\vert ^2$ (SG-19) |
| $q$, $q_m$ | chart amplitude $\vert z\vert ^2$ and its block samples | §6.14 | NUMGEN writes $q_m$ for the primitive $Q_m$ (I3, §7) |
| $W$, $W_{\rm DSN}$, $Z$, $z$ | primitive linear frame; same with wrapped $\eta$; $K_p$ eigenframe; chart coordinate | §1, §6.9, §6.11, §6.14 | $W=W_{\rm DSN}$ only on the principal lift |
| $\eta$, $\eta_{\rm wrap}$, $\ell$ | lifted angle; wrapped representative; winding index | §6.1, §6.4 | — |
| $\Theta$, $\hat\varphi$, $\delta_T$ | ISP angle; increasing primitive phase lift; one-step increment | §6.4, §6.14, §7 | lift convention I1 |
| $U$, $U_T$ | $\{0<Q\le\tfrac1{625}\}$; $\bigcup_{j=0}^5T^j(U)$ | §6.14, §7 | base points vs intermediate steps (I5) |
| $C_0$, $Q_c$ | critical curve $\{\det DT=0\}$; critical ISP amplitude $(\arcsin\ln2)^2$ | §6.1, §6.4 | $C_0$ is not a constant $C$ |
| $R^*$ | $e^{\pi/\tau}=\lambda_{\rm DSI}^{1/2}$ | §6.3 | — |
| $P_1$, $P_2$, $P_5$ | fixed points; degree-5 radial polynomial | §1, §6.1, §6.14 | $P_5$ is not a fixed point |
| $M$ | (i) cubic-jet matrix of §6.7; (ii) memory $M$, $M_W$ of §6.14; (iii) real amplitude $M_p$ of §6.11; (iv) count $M(D)$ of Appendix D | see column | read by section |
| $G$ | (i) lattice coefficient of RECOG R9; (ii) $G_{\rm lattice}(5)$, $G_{04}$, $G_{32}$ bridge gaps; (iii) $G=J^2$ | §6.11, §6.14, §6.16 | read by section |
| $\kappa_{\rm bb}$, $C_{\rm bb}$, $\kappa_{\rm fit}$ | historical fit parameters | §6.5 | not canonical constants (SG-7) |
| $\mathcal A_{\rm raw}$ | fixed-radius angular mean in the raw $W$-frame | §6.5 | not a pointwise recurrence |
| $r_m$, $D_Q$, $D_\Theta$, $S_Q$, $S_\Theta$, $\Lambda_3$ | L-PHASE remainder; OPEN 3 differences and leading term | §6.14 | rows A/B not mixed |
| $R_0$, $K_m$, $X$, $\Phi$ | formal involution; smooth roots; generator; equivariant chart (§6.17); $\Phi_1$, $\Phi_{\rm archive}$ are other maps | §6.9, §6.16–§6.17 | formal vs $C^\infty$ vs analytic |
| $\nu_3$, $\nu_5$, $c_{21}$, $c_\theta$, $a_1$, $a_2$, $a_{05}$ | normal-form coefficients (raw, one-step, Lie-gauge, chart) | §6.2, §6.9, §6.11, §6.14 | always name the frame/convention |
| $K_p$, $u$ | $2-2\cos(2\pi/p)$; $1/(1-\lambda)$ in the $K_p$ eigenframe | §2 OPEN 9, §6.11, Appendix D | — |
| $U$ (other uses) | (i) ISP anti-correlation coordinate $U=\tfrac{\sqrt3}2\rho$ (§6.4); (ii) the start/base-point set $U=\{0<Q\le\tfrac1{625}\}$ (§6.14), whose invariant six-phase tube is $U_T$ (see the $U$, $U_T$ row); (iii) the projection window $U$ of OPEN 16, $\Pi(Q_0,U,\mathcal O)$ | §6.4, §6.14, §2 OPEN 16 | read by section |
| $\widehat h$, $h_6$, $h$ (OPEN-M) | formal Poincaré–Dulac normalizer; finite adopted degree-6 normalizer; OPEN-M source amplitude $h$ | §6.16, §6.14, SG-15 | the OPEN-M $h$ is not a normalizer (SG-15) |
| $M(s)$ | majorant of $h-\mathrm{id}$ in DYAD-THM-NF-INV; distinct from the $M$ entries above | §6.14 | — |
| $\kappa$ | $\kappa=M'(R)$, contraction constant of DYAD-THM-NF-INV; not the historical fit parameter $\kappa_{\rm bb}$ | §6.14, §6.5 | — |
| $r$, $r_m$ | polar radius $z=re^{i\Theta}$; L-PHASE remainder $r_m$ | §6.14 | — |

---

## Appendix D — OPEN 9 definitions (recovered) {#appendix-d}

`[DEF]` `[v6.4.20]` Definitions recovered from two owner-side sources outside this ledger (FB-DYAD-11, deferred in the disposition, completed here as far as the sources go). They are recorded as definitions only; no new result is stated.

| Source file | SHA-256 |
|---|---|
| `OPEN9_arithmetic_horizon_definitions.md` | `d944ad8ccdbdaaeb79344cf312f6bcff9694159f60c7c8b483f3decd23867c29` |
| `DYAD_RESPONSE_TO_DZT_REQ-002.md` | `0f8c4b1566e62f0cb97513bc9b9e2b57d9fd712a314f24f66ba8ad7b0a7f7dd3` |

| Object | Recovered definition | Source |
|---|---|---|
| $K_p$ family | $\rho'=\rho-\sin\eta$, $\eta'=\eta+K_p(e^\rho-1)-K_p\sin\eta$, $K_p=2-2\cos(2\pi/p)$, $\lambda=e^{2\pi i/p}$ | OPEN9 definitions §1 |
| $W_{\rm new}$, $\gamma$ | $W_{\rm new}=\rho+\gamma\eta$, $\gamma=(\lambda-1)/K_p$ | OPEN9 definitions §1 |
| Frame theorem | $W_{\rm new}=D\,Z_{\rm eng}$, $D=(1+\lambda)/(1-\lambda)=i\cot(\pi/p)$ `[ALG]` (same scale as DYAD-ALG-KP-FRAME-SCALE) | OPEN9 definitions §1 |
| $N_p$, $F_1^p$, $F_{\rm raw}^p$ | $N_p=\Phi_1^{-1}f_p\Phi_1$; $F_1^p=N_p^p$; $F_{\rm raw}^p=f_p^p$ | OPEN9 definitions §2 |
| $S(p)$ | $\{d: d\mid p,\ 1<d<p\}$ | OPEN9 definitions §3 |
| $G^Z_{p,d}$, $\Delta^Z_{p,d}$ | $G^Z_{p,d}=\lambda^{-d}(f_p^d)^Z$; $\Delta^Z_{p,d}=G^Z_{p,d}-Z$ | OPEN9 definitions §3 |
| $C^Z_{\rm sub}(p;D)$ | $\sum_{d\in S(p)}\#\operatorname{supp}(\Delta^Z_{p,d})_{\le D}$ | OPEN9 definitions §3 |
| $M(D)$ | $(D+1)(D+2)/2-3$ | OPEN9 definitions §3 |
| Dense-lattice formula | $C_{\rm sub}=(\tau(p)-2)M(D)-\sum_dZ_{p,d}(D)$, $Z_{p,d}(D)=M(D)-\#\operatorname{supp}$; the cancellation rules $Z_{p,d}$ are `[OPEN]` | OPEN9 definitions §3 |
| Resonance, ladder, first harmonic | resonant monomials $a-b\equiv1\pmod p$; ladder $(j+1,j)$; first lattice harmonic $(0,p-1)$ | OPEN9 definitions §4 |
| $\Delta_p$, $G_{ab}(p)$, $G_{32}$, $G_{\rm lattice}(5)$ | $\Delta_p=F_1^p-F_{\rm raw}^p$; $G_{ab}(p)=\vert \Delta_p(a,b)\vert $; $G_{32}=G_{(3,2)}$; $G_{\rm lattice}(5)=G_{(0,4)}(5)$ | OPEN9 definitions §5 |
| Bridge norms $G^{(1)}$, $G^{(2)}$ | norms of $\Delta_p$ over the resonant set $a-b\equiv1\pmod p$ | OPEN9 definitions §6 |
| $\chi_p(a,b)$ | $(a-b-1)\bmod p$ | DYAD response to DZT REQ-002 |
| $K^{\rm extra}_{p,q}$ | $\{q,2q,\dots,p-q\}$, $s=p/q$, $\vert K^{\rm extra}_{p,q}\vert =s-1$ | DYAD response to DZT REQ-002 |
| Source admissibility | source $(0,b)$ is admissible iff $q\mid(b+1)$ (for $b+1<p$; in general $\chi_p(0,b)\in K^{\rm extra}_{p,q}$ iff $q\mid(b+1)$ and $p\nmid(b+1)$, owner check M11) | DYAD response to DZT REQ-002 |
| $R^{\rm raw}_{p,q}$ | raw subgroup strobe $\lambda^{-s}f_p^s-\mathrm{Id}$, $s=p/q$ | DYAD response to DZT REQ-002 |

**Symbols without recovered definitions.** $\mathcal Q(p)$, $\Pi^{\rm extra}_{p,q}$, $J^{extra,raw}_{p,q,D}$, $\mathcal B^{extra}_{p,q,D}$, $Z^{\rm miss}_{p,q,D}$, $C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, $\Delta_{\rm overlap}$, the statement of the eigenframe linear-part lemma. They keep their names in §6.11; no definition is reconstructed for them here.

---

## Appendix E — Claim-to-evidence matrix {#appendix-e}

`[DEF]` `[v6.4.20]` One row per result or definition identifier carried by this ledger (including those new in v6.4.20). Evidence levels are kept apart: **OWNER-RUN** (run by the Dyadic owner), **REVIEWER-REPLAYED** (rerun by an external reviewer), **REVIEWER FULL REPLAY NOT COMPLETED** (named runs a reviewer did not finish). "not recorded" means this ledger carries no record; an absent attachment is recorded as absent, not inferred. "Written proof" is the section of the entry. P2 checks M1–M11 are in `dyad_p2_math_checks.py` (OWNER-RUN, 21 Oct 2026; REVIEWER-REPLAYED from the r1 package, 21 Oct 2026 — the same script rerun, not a second method). `[v6.4.20]` (r2) **Grade rule:** the grade is the grade tag governing the identifier's canonical RID tag (the nearest grade tag before it on that line, otherwise the first after it; for a list item without a grade tag, the grade of the list's lead-in line); identifiers registered at the v6.4.20 adoption read "— new in v6.4.20" (in r2: "— proposed, not adopted"). `DYAD-CAND-FLAT-CENTRALIZER` and `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` carry `[THM]` since the v6.4.13 adoption decision; their identifiers were kept. **Scope rule:** the scope span of the entry, or a stated split where the entry has parts of different coverage.

**E.1 Statement, proof and certificate**

| RID | Grade | Scope | Written proof | Certificate / script | Input identity | Backend | Coverage |
|---|---|---|---|---|---|---|---|
| `DYAD-ALG-A1A2-LIEGAUGE` | ALG | conv: Lie strict-kernel gauge | §6.9 | `open17_a2.py` (DYAD-ART-OPEN17) | not recorded | not recorded | Lie gauge |
| `DYAD-ALG-ALIAS-PHASE` | ALG | as stated at the entry | §2 | `open16_alias_phase.py` (DYAD-ART-OPEN16) | not recorded | not recorded | alias phase at $U=\pi/\tau$ |
| `DYAD-ALG-B5-ALLP-NONVANISHING` | ALG — new in v6.4.20 | all $p\ge6$: $6\le p\le12$ by exact cyclotomic certificates (finite part); $p\ge13$ by algebraic proof ($\Phi_p\nmid N$) | §6.11 | `rtg_b5_Seff_limit_cert.py`, `exact_Fraw_b5_sweep.py`, `rtg_b5_step3_reduction.py` | not recorded | exact cyclotomic | all $p\ge6$ |
| `DYAD-ALG-BRIDGE-LEMMA` | ALG | as stated at the entry | §6.9 | §6.9; general proof cross-referenced to `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` | — | — | stated in §6.9 |
| `DYAD-ALG-CENT-KERNEL` | ALG | as stated at the entry | §6.16 | `dyad_open19_kernel_check.py` (DYAD-ART-OPEN19-KERNEL) | `1cb40446…291e` | SymPy | proof all $k$; checks $k\le13$ |
| `DYAD-ALG-CROSS-IDENTITY` | ALG | as stated at the entry | §2 | `degree_b_vanishing_scan.py` (DYAD-ART-VANISH-B234) | not recorded | SymPy exact | $p\ge5$ |
| `DYAD-ALG-CUBIC-PARABOLIC` | ALG | as stated at the entry | §6.3 | proof in the entry; §6.7 jet | — | — | full statement |
| `DYAD-ALG-DIRECT-WEIGHT` | ALG | as stated at the entry | §2 | `degree_b_vanishing_scan.py` (DYAD-ART-VANISH-B234) | not recorded | SymPy exact | all $p$ with $p\nmid(b+1)$ |
| `DYAD-ALG-GLATTICE5` | ALG | as stated at the entry | §6.11 | `prove_p5_lattice_anomaly_exact.py` (DYAD-ART-P5-LATTICE) | not recorded | exact cyclotomic | $p=5$ |
| `DYAD-ALG-ISP-MAPS` | ALG — new in v6.4.20 | as stated at the entry | §6.4 | P2 M4 | `dyad_p2_math_checks.py` | SymPy exact | forward map and reconstruction |
| `DYAD-ALG-KP-FRAME-SCALE` | ALG — new in v6.4.20 | as stated at the entry | §6.9 | P1 math checks | `dyad_p1_math_checks.py` | SymPy | declared $K_p$ family |
| `DYAD-ALG-LIEGAUGE-NORM` | ALG | conv: Lie strict-kernel gauge | §2 | `normalize_p6_liegauge_exact.py` (DYAD-ART-NORM-P6, `[ENG]`, 120 dps) | not recorded | mpmath, tolerance-pruned | Lie strict-kernel gauge only |
| `DYAD-ALG-NF6` | ALG | as stated at the entry | §6.14 | DYAD-ART-RE-P0P1, DYAD-ART-RE-P2B2, DYAD-ART-RE-REFEREE | manifest `RTG_DYADIC_v6_4_10_INSTALL_MANIFEST.json` | exact $\mathbb Q(i\sqrt3)$ | through degree 6 |
| `DYAD-ALG-NF6-DEG10` | ALG | scope: fixed adopted $h_6$ of DYAD-ALG-NF6; exact Taylor computation through total degree 10 | §6.14 | `DYAD_CHECK_degree10_even_term_hatF.md` (DYAD-ART-NF6-DEG10) | `dcfd808c…f4d4`; engine `e45286fa…50f6` | exact $\mathbb Q(i\sqrt3)$ | fixed $h_6$, degree 10 |
| `DYAD-ALG-NF6-OBS` | ALG | as stated at the entry | §6.14 | as DYAD-ALG-NF6 | as NF6 | as NF6 | degree 5–6 obstruction |
| `DYAD-ALG-NU5-P5` | ALG | as stated at the entry | §6.11 | `dyad_m2c_nu5_p5_exact.py` (DYAD-ART-NU5-P5) | `5fcccb9d…d464` | exact $\mathbb Q(\zeta_5)$ | $p=5$ |
| `DYAD-ALG-ONE-BLOCK-BURST` | ALG — new in v6.4.20 | as stated at the entry | §6.5 | P2 M7 | `dyad_p2_math_checks.py` | exact rational jets | positive real ray |
| `DYAD-ALG-OPEN3-LEADING` | ALG | scope: chart of DYAD-ALG-NF6; one F-block; leading homogeneous terms; normalized $z=re^{i\Theta}$ | §6.14 | `dyad_open3_p2_exact_gate.py` (DYAD-ART-OPEN3-P2) | `89939581…0c50` | exact | leading terms |
| `DYAD-ALG-OPEN3-PHASE-OFFSET` | ALG | scope: chart of DYAD-ALG-NF6; row disks; $z=re^{i\Theta}$ | §6.14 | `dyad_open3_p4_exact.py` (DYAD-ART-OPEN3-P4) | `199a15ba…0703` | exact | exact identity; primitive-variable form `[ALG]` formal |
| `DYAD-ALG-P5-RADIAL` | ALG — new in v6.4.20 | as stated at the entry | §6.14 | P2 M6 | `dyad_p2_math_checks.py` | exact rational jets | degrees 2–5 |
| `DYAD-ALG-P567-LEDGER` | ALG | as stated at the entry | §2 | `normalize_p_full_onestep_cyclotomic.py`, `normalize_p7_c06_full_cyclotomic_optimized.py` | not recorded | exact cyclotomic | $p=5,6,7$ |
| `DYAD-ALG-P6-FACEFLUX` | ALG | as stated at the entry | §6.2 | arithmetic identity in the entry | — | — | exact identity; external input Pre-Legacy §1.8 |
| `DYAD-ALG-PROTECTION-MATRIX` | ALG | as stated at the entry | §6.11 | follows from the §6.7 jet | — | — | cubic order, $p=6$, $K=1$ |
| `DYAD-ALG-Q-INVARIANT-FORM` | ALG | as stated at the entry | §6.3 | proof in the entry | — | — | full statement |
| `DYAD-ALG-Q3-DEG2-CANCEL` | ALG — new in v6.4.20 | as stated at the entry | §6.11 | `rtg_p_certs.py` (DYAD-ART-P-CERTS) | not recorded | SymPy/cyclotomic | all $p>3$, $3\mid p$ |
| `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | ALG — new in v6.4.20 | as stated at the entry | §6.4 | P2 M3 | `dyad_p2_math_checks.py` | SymPy | value to 4 d.p. |
| `DYAD-ALG-RAW-ANGULAR-MEAN` | ALG — new in v6.4.20 | scope: fixed-radius uniform-angle mean in the raw $W$-frame | §6.5 | P2 M8 | `dyad_p2_math_checks.py` | exact rational jets | raw fixed-radius mean |
| `DYAD-ALG-SIXSTEP-CUBIC-JET` | ALG — new in v6.4.20 | as stated at the entry | §6.7 | P2 M5 | `dyad_p2_math_checks.py` | exact rational jets | cubic order |
| `DYAD-ALG-TAU-DETB` | ALG | as stated at the entry | §6.3 | proof in the entry | — | — | full statement |
| `DYAD-ALG-VANISH-B2` | ALG | as stated at the entry | §6.11 | `rtg_betagraded_vanishing.py` (DYAD-ART-VANISH-BGRADED); `degree_b_vanishing_cert.py` | `dec08174…d774`; `c9a369e6…0dc6` | β-graded exact engine; SymPy Route A/B | $p\ge4$ |
| `DYAD-ALG-VANISH-B3` | ALG | as stated at the entry | §6.11 | as DYAD-ALG-VANISH-B2 | as B2 | as B2 | $p\ge5$ |
| `DYAD-ALG-VANISH-B4` | ALG | as stated at the entry | §6.11 | as DYAD-ALG-VANISH-B2 | as B2 | as B2 | $p\ge6$ |
| `DYAD-CAND-FLAT-CENTRALIZER` | THM | as stated at the entry | §6.17 | `DYAD_LEMMA_F_FLAT_CENTRALIZER_PROOF_RECORD_v0_3.md` (DYAD-ART-LEMMA-F-RECORD) | `2e6c5c59…8ece` | — | stated ball, flat contact |
| `DYAD-CAND-P0-DYADIC` | CAND | conditional h-transfer (h-source bridge OPEN in OPEN-M); exact sub-results are not part of this row: face-flux identity and R11 factor $3/4$ under `DYAD-ALG-P6-FACEFLUX` `[ALG]`; threshold $0.024$ `[HYP]` inherited | §6.11 | none | — | — | conditional calibration branch |
| `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` | THM | assuming: hypotheses stated in the entry | §6.17 | as DYAD-CAND-FLAT-CENTRALIZER | `2e6c5c59…8ece` | — | existing $C^\infty$ objects |
| `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` | DEF | as stated at the entry | §6.12 | definition; items carry their own RIDs | — | — | six items |
| `DYAD-DEF-CRITICAL-CURVE` | DEF — new in v6.4.20 | as stated at the entry | §6.1 | P2 M2 | `dyad_p2_math_checks.py` | SymPy exact | full statement |
| `DYAD-DEF-PRIMITIVE-MAP` | DEF | as stated at the entry | §6.1 | definition | — | — | — |
| `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` | THM | scope: analytic | §6.15 | proof in §6.15 (Corollary A); DYAD-ART-OPEN19-SESSION | `6749df11…60e1c6` | — | analytic germs |
| `DYAD-THM-C21` | THM | as stated at the entry | §6.2 | archival proof (OPEN 1) | not recorded | not recorded | full statement |
| `DYAD-THM-FORMAL-CENTRALIZER` | THM | scope: formal category, real coefficients | §6.16 | DYAD-ART-OPEN19-SESSION; DYAD-ART-OPEN19-R0CERT | `c8c14442…9cf8` | exact $\mathbb Q(i\sqrt3)$ | formal category |
| `DYAD-THM-FORMAL-INVOLUTION-UNIQUE` | THM | scope: formal category | §6.16 | DYAD-ART-OPEN19-SESSION; DYAD-ART-OPEN19-R0CERT (3 truncations × 7 assertions) | `c8c14442…9cf8` | exact $\mathbb Q(i\sqrt3)$ | formal category |
| `DYAD-THM-FORMAL-Z6-GENERATOR` | THM | scope: formal category | §6.16 | proof in §6.16 | — | — | formal |
| `DYAD-THM-LOCAL-INVOLUTION-GERM` | THM | as stated at the entry | §6.15 | proof in §6.15 | — | — | (a) $C^1$ + $T$; (b) $C^3$ + $T^6$ + tube |
| `DYAD-THM-LPHASE-ROWA-REMAINDER` | THM | scope: block base points in $U$ of DYAD-THM-PRIM-CTR; chart row A ($\vert z\vert \le\tfrac1{20}$) of DYAD-THM-NF-REM; primitive observable | §6.14 | `dyad_numgen_lphase_rowA_cert.py` (DYAD-ART-LPHASE-ROWA); provenance gate v0.1.1 (DYAD-ART-LPHASE-P2B-PROV) | `117484ae…9cdb`; gate `343a3631…a27a5` | exact rational | row A, block base points in $U$ |
| `DYAD-THM-NF-INV` | THM | as stated at the entry | §6.14 | as DYAD-THM-PRIM-CTR | v6.4.10 manifest | exact rational | $\vert z\vert \le1/10$, $\vert W\vert \le9/100$ |
| `DYAD-THM-NF-REM` | THM | as stated at the entry | §6.14 | as DYAD-THM-PRIM-CTR | v6.4.10 manifest | exact rational | rows $1/20$, $1/40$ (not mixed) |
| `DYAD-THM-OPEN11` | THM-ALG via IA | as stated at the entry | §6.10 | `certify_transition_strip2.cpp` (DYAD-ART-STRIP2) and the F1 artifacts | not recorded | Arb (C++) | canonical family $(0,q)$, $q\in(0,2]$ |
| `DYAD-THM-OPEN18` | THM-ALG via IA | as stated at the entry | §6.8 | `open18_arb_cert_final.cpp` (DYAD-ART-OPEN18) | not recorded | FLINT/Arb (C++) | first footprint, both branches |
| `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` | THM | assuming: RECOG-THM-R9-MEMORY | §6.14 | `dyad_open21_p5_remainder_cert.py` v0.1.2 (DYAD-ART-OPEN21-P5) | `80452d8a…787c` | exact rational | rows A, B |
| `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` | THM | assuming: hypotheses stated in the entry | §6.14 | DYAD-ART-OPEN3-P4 and record | — | exact rational | row disks; conditional on R9 |
| `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS` | THM | scope: NF-REM rows, not mixed | §6.14 | `dyad_open3_p4_offset_cert.py` (DYAD-ART-OPEN3-P4) | `4058dfc9…7a8f` | exact rational | rows $1/20$, $1/40$ |
| `DYAD-THM-OPEN3-SPIRAL-REM` | THM | scope: chart of DYAD-ALG-NF6; NF-REM rows, not mixed | §6.14 | `dyad_open3_p3_remainder_cert.py` (DYAD-ART-OPEN3-P3) | `b7df79b0…258d` | exact rational | rows $1/20$, $1/40$ |
| `DYAD-THM-PRIM-CTR` | THM | as stated at the entry | §6.14 | DYAD-ART-RE-P2B2 (67+73 checks), DYAD-ART-RE-REFEREE (47), DYAD-ART-RE-SUPPL (45) | v6.4.10 manifest | exact rational + 60-dps tail | $0<Q\le1/400$; tube from $1/625$ |
| `DYAD-THM-Q403-PHASELAW` | THM | scope: all $p=4s$, $s\ge2$ | §6.11 | `q4_03_R_identity_certificate.py` (DYAD-ART-Q403-CERT); `q4_03_cascade_extract.py` | not recorded | exact symbolic over $\mathbb Q(I)(L)$ | all $p=4s$, $s\ge2$; extractor $p=8$–$52$ |
| `DYAD-THM-RAW-CUBIC` | THM | as stated at the entry | §2 | source `OPEN9_full_onestep_normalization_table_v2.md` §4 (`af90dc13…700e`); P1-2 re-derivation | source not in the P1 review package | SymPy | one-step raw frame, declared $K_p$ family |
| `DYAD-THM-SMOOTH-EMBEDDING` | THM | as stated at the entry | §6.17 | DYAD-ART-OPEN20-BINF-RECORDS and -CHECKS | `56d81781…7140` (P3-a) | SymPy / exact | $C^\infty$ germs at $P_1$ |
| `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | THM — new in v6.4.20 | as stated at the entry | §6.17 | P1 SESSION derivation | `dyad_p1_math_checks.py` (linear part) | SymPy | $C^\infty$ germs |

**E.2 Evidence levels and gaps**

| RID | OWNER-RUN | REVIEWER-REPLAYED | REVIEWER FULL REPLAY NOT COMPLETED | Independent engine | Remaining gaps |
|---|---|---|---|---|---|
| `DYAD-ALG-A1A2-LIEGAUGE` | historical | not recorded | not recorded | not recorded | gauge-universal projection OPEN |
| `DYAD-ALG-ALIAS-PHASE` | historical | not recorded | not recorded | not recorded | full $\Pi$ OPEN |
| `DYAD-ALG-B5-ALLP-NONVANISHING` | historical (v6.4.7) | not recorded | not recorded | not recorded | new RID (v6.4.20); all-$b\ge5$ OPEN |
| `DYAD-ALG-BRIDGE-LEMMA` | — | not recorded | not recorded | RECOG proof (separate owner) | — |
| `DYAD-ALG-CENT-KERNEL` | v6.4.12 | source-reported runs | not recorded | not recorded | finite checks are not certificates of the all-order statement |
| `DYAD-ALG-CROSS-IDENTITY` | historical | not recorded | not recorded | not recorded | — |
| `DYAD-ALG-CUBIC-PARABOLIC` | P2 M5 (jet) | not recorded | not recorded | — | — |
| `DYAD-ALG-DIRECT-WEIGHT` | historical | not recorded | not recorded | not recorded | — |
| `DYAD-ALG-GLATTICE5` | historical | not recorded | not recorded | not recorded | — |
| `DYAD-ALG-ISP-MAPS` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M4 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | new RID (v6.4.20) |
| `DYAD-ALG-KP-FRAME-SCALE` | P1 | reviewer general-angle algebraic check | — | yes (reviewer) | new RID (v6.4.20) |
| `DYAD-ALG-LIEGAUGE-NORM` | historical | not recorded | not recorded | not recorded | gauge-universal form OPEN |
| `DYAD-ALG-NF6` | v6.4.10 producer/validator | v6.4.10 independent reconstruction (Claude review records) | not recorded | yes: referee independent of producer/validator code | — |
| `DYAD-ALG-NF6-DEG10` | v6.4.11 | third-party report confirmed (RRF VF-1) | not recorded | yes (third reviewer) | — |
| `DYAD-ALG-NF6-OBS` | v6.4.10 | v6.4.10 review | not recorded | yes (referee) | — |
| `DYAD-ALG-NU5-P5` | v6.4.13 | not recorded | not recorded | Genesis replay `[NUM]` 4/4 | — |
| `DYAD-ALG-ONE-BLOCK-BURST` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M7 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | new RID (v6.4.20) |
| `DYAD-ALG-OPEN3-LEADING` | v6.4.14 | v6.4.14 review | not recorded | not recorded | — |
| `DYAD-ALG-OPEN3-PHASE-OFFSET` | v6.4.15 | exact script re-executed, byte-identical JSON (v6.4.15 review) | not recorded | no | formal second-order remainder not certified (see OPEN 21 result) |
| `DYAD-ALG-P5-RADIAL` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M6 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | new RID (v6.4.20) |
| `DYAD-ALG-P567-LEDGER` | historical | not recorded | not recorded | not recorded | general $\nu_5^{(p)}$ OPEN |
| `DYAD-ALG-P6-FACEFLUX` | — | — | — | — | h-transfer `[CAND]` (DYAD-CAND-P0-DYADIC) |
| `DYAD-ALG-PROTECTION-MATRIX` | P2 M5 rechecks $M$ | — | — | no | — |
| `DYAD-ALG-Q-INVARIANT-FORM` | — | not recorded | not recorded | — | — |
| `DYAD-ALG-Q3-DEG2-CANCEL` | historical | not recorded | not recorded | not recorded | new RID (v6.4.20); not rerun in P2 |
| `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M3 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | new RID (v6.4.20) |
| `DYAD-ALG-RAW-ANGULAR-MEAN` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M8 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | new RID (v6.4.20); long-orbit identification OPEN |
| `DYAD-ALG-SIXSTEP-CUBIC-JET` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M5 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | new RID (v6.4.20) |
| `DYAD-ALG-TAU-DETB` | — | not recorded | not recorded | — | structural explanation `[HEUR]` only |
| `DYAD-ALG-VANISH-B2` | P1, 21 Oct 2026 (both exit 0) | P1 review: both scripts PASS | — | two owner engines; no third-party engine | `degree_b_vanishing_cert_v2.py` (registry name) not available; not recreated |
| `DYAD-ALG-VANISH-B3` | P1, 21 Oct 2026 | P1 review: PASS | — | two owner engines | v2 certificate custody OPEN |
| `DYAD-ALG-VANISH-B4` | P1, 21 Oct 2026 | P1 review: PASS | — | two owner engines | v2 certificate custody OPEN |
| `DYAD-CAND-FLAT-CENTRALIZER` | — | two review rounds (v6.4.13) | not recorded | — | finite-$C^k$ versions OPEN |
| `DYAD-CAND-P0-DYADIC` | — | — | — | — | h-source bridge OPEN (OPEN-M) |
| `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` | — | two review rounds (v6.4.13) | not recorded | — | existence supplied by `DYAD-THM-SMOOTH-EMBEDDING` |
| `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` | — | — | — | — | consumer acceptance per item |
| `DYAD-DEF-CRITICAL-CURVE` | P2, 21 Oct 2026 | r1 review, 21 Oct 2026: `dyad_p2_math_checks.py` M2 rerun from the r1 package (same script) | — | no (same-script replay, not a second method) | new RID (v6.4.20) |
| `DYAD-DEF-PRIMITIVE-MAP` | — | — | — | — | Genesis alias recorded (N1) |
| `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` | — | SESSION v1.1 review ACCEPT | not recorded | — | existence (B-an) OPEN |
| `DYAD-THM-C21` | historical; P2 M5 re-derives $\mu$ from the exact six-step jet | not recorded | not recorded | P2 M5 is an owner recheck, not independent | — |
| `DYAD-THM-FORMAL-CENTRALIZER` | v6.4.12 | SESSION v1.1 review ACCEPT | not recorded | not recorded | — |
| `DYAD-THM-FORMAL-INVOLUTION-UNIQUE` | v6.4.12 | SESSION review ACCEPT | not recorded | not recorded | convergence OPEN 20 |
| `DYAD-THM-FORMAL-Z6-GENERATOR` | — | v6.4.13 review rounds | not recorded | — | B-6 OPEN |
| `DYAD-THM-LOCAL-INVOLUTION-GERM` | — | review rounds r1–r3 (v6.4.11–v6.4.12) | not recorded | — | existence not asserted |
| `DYAD-THM-LPHASE-ROWA-REMAINDER` | combined checker 16/16 (G14 certificate, G15 provenance); controls M1–M4 | gate v0.1.1 main 9/9 + 4 internal controls; draft and package hashes; 11 draft-checker controls | combined G14–G15 run; independent `--record-exit-codes` run | no: NUMGEN receipt replay used the same algorithm | row B; optimal constant |
| `DYAD-THM-NF-INV` | v6.4.10 | v6.4.10 independent reconstruction | not recorded | yes (referee) | — |
| `DYAD-THM-NF-REM` | v6.4.10 | v6.4.10 independent reconstruction | not recorded | yes (referee) | higher derivatives not bounded |
| `DYAD-THM-OPEN11` | historical | not recorded | not recorded | not recorded | full phase space not covered |
| `DYAD-THM-OPEN18` | historical | not recorded | not recorded | not recorded | — |
| `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` | v6.4.17 | certificate 28/28 replayed byte-identically; $P_{W2}$ re-derived by Laurent polynomials | not recorded | partial ($P_{W2}$ only) | conditional on `RECOG-THM-R9-MEMORY` |
| `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` | v6.4.15 | v6.4.15 review | not recorded | no | conditional on `RECOG-THM-R9-MEMORY` |
| `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS` | v6.4.15 | rational certificate re-executed (v6.4.15 review) | not recorded | no | — |
| `DYAD-THM-OPEN3-SPIRAL-REM` | v6.4.14 | P3 certificate replayed byte-identically (v6.4.14 review) | not recorded | no (same algorithm) | majorant constants, not maxima |
| `DYAD-THM-PRIM-CTR` | v6.4.10 | v6.4.10 independent reconstruction | not recorded | yes (referee) | optimal radii not claimed |
| `DYAD-THM-Q403-PHASELAW` | historical (v6.4.9) | not recorded | not recorded | extractor is an independent method (owner) | — |
| `DYAD-THM-RAW-CUBIC` | P1 (formula) | reviewer independent derivation via $\tan(\theta/2)$ | — | yes (formula) | historical provenance comparison not done |
| `DYAD-THM-SMOOTH-EMBEDDING` | v6.4.18 | payload checks re-executed with controls (integration 6/6, P3-a 8/8, P3-b/c 3/3) | not recorded | no | B-an, B-6 OPEN; no radius |
| `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | P1 | reviewer ACCEPT `[THM — SESSION]` (FB-13) | — | reviewer check of the averaging argument | new RID (v6.4.20); analyticity OPEN |

---

## Appendix F — DZT / AZ string crosswalk {#appendix-f}

`[DEF]` `[v6.4.20]` Every Dyadic-pattern string printed in DZT v0.8 (§7) and AZ v0.6 (§§4.1, 8), classified. Classes: exact match; component of `DYAD-THM-Q403-PHASELAW`; historical note label; artifact; unmatched. No alias is created by this table; consumer repins are requested by planned notice N17, after external verification of this edition's SHA-256.

| Consumer (pin v6.4.8.1) | String as printed | Class | Dyadic reading | Note |
|---|---|---|---|---|
| DZT v0.8 §7 | DYAD-OPEN-B5-ALLP | exact match | `DYAD-OPEN-B5-ALLP` (closed lifecycle item, untagged in this ledger) | result RID registered at v6.4.20 adoption: `DYAD-ALG-B5-ALLP-NONVANISHING` |
| DZT v0.8 §7 | DYAD-ALG-VANISH-B2/B3/B4 | exact match (combined spelling) | `DYAD-ALG-VANISH-B2`, `DYAD-ALG-VANISH-B3`, `DYAD-ALG-VANISH-B4` | cite the three RIDs separately |
| DZT v0.8 §7 | DYAD-ALG-P6-FACEFLUX | exact match | `DYAD-ALG-P6-FACEFLUX` | — |
| DZT v0.8 §7 | DYAD-THM-Q403-PHASE-ALLP | historical note label | the theorem `DYAD-THM-Q403-PHASELAW` (§6.11); label from a non-DSN Dyadic phase-law note | no alias created; consumer repin to `DYAD-THM-Q403-PHASELAW` |
| DZT v0.8 §7 | DYAD-THM-P1 | component of PHASELAW | universal direction factor $\lambda^{-s}=\zeta_p^{-p/4}=-i$ ($I=L^{p/4}=i$ in §6.11) | no separate RID |
| DZT v0.8 §7 | DYAD-THM-REALITY | component of PHASELAW | conjugation/Galois $\sigma_{-1}$ step of the §6.11 proof | no separate RID |
| DZT v0.8 §7 | DYAD-THM-LEAD | component of PHASELAW | leading cancellation $S_{-4}=0$ (LEAD) in the §6.11 proof | no separate RID |
| DZT v0.8 §7 | DYAD-THM-R | component of PHASELAW | remainder relation $\sigma_{-1}(Q)=-L^{-6}Q$ (equivalently for $A_p$) | no separate RID |
| DZT v0.8 §7 | DYAD-CF-Q403 | component of PHASELAW | closed form $Q(L,I)$ displayed in §6.11 | no separate RID |
| DZT v0.8 §7 | DYAD-ALG-PHASELAW | historical note label | superseded finite-horizon phase law $\arg Q_p=\tfrac\pi2+\tfrac{6\pi}p$ (now part of `DYAD-THM-Q403-PHASELAW`) | no alias created |
| DZT v0.8 §7 | DYAD-ALG-CASCADE-P12 | unmatched | the §6.11 micro-certification $p=12,q=4,(0,3)$ value $-13+15\sqrt3/2$ (no RID) | DZT marks it subsumed by its artifact string |
| DZT v0.8 §7 | DYAD-ART-CASCADE-Q4-03 | artifact (correspondence not hash-verified) | content matches `DYAD-ART-Q403-EXTRACT` (`q4_03_cascade_extract.py`, gates $p=8\to0$, $p=12\to-13+15\sqrt3/2$) | DZT prints extractor SHA-256 `ecdb805f…05eac2`; §8 prints no hash, so no byte identity is claimed |
| AZ v0.6 §8 | DYAD-THM-RAW-CUBIC | exact match | `DYAD-THM-RAW-CUBIC` | formula recovered and algebraically verified (P1, FA-08); identity with the historical proposition not yet established (Appendix E) |
| AZ v0.6 §8 | DYAD-ALG-P567-LEDGER | exact match | `DYAD-ALG-P567-LEDGER` | — |
| AZ v0.6 §8 | DYAD-ALG-GLATTICE5 | exact match | `DYAD-ALG-GLATTICE5` | — |
| AZ v0.6 §8 | DYAD-OPEN-P-RESONANCE (sub-item labels) | exact match (lifecycle RID with free-text sub-labels) | `DYAD-OPEN-P-RESONANCE` | sub-labels are not identifiers |
| AZ v0.6 §8 | DYAD-ALG-VANISH-B2, -B3, -B4 | exact match | the three vanishing RIDs | — |
| AZ v0.6 §8 | DYAD-ALG-DIRECT-WEIGHT | exact match | `DYAD-ALG-DIRECT-WEIGHT` | — |
| AZ v0.6 §8 | DYAD-ALG-CROSS-IDENTITY | exact match | `DYAD-ALG-CROSS-IDENTITY` | — |
| AZ v0.6 §8 | DYAD-ALG-P6-FACEFLUX | exact match | `DYAD-ALG-P6-FACEFLUX` | — |
| AZ v0.6 §4.1 | DYAD-OPEN-B5-ALLP | exact match | `DYAD-OPEN-B5-ALLP` | — |
| AZ v0.6 §4.1 | DYAD-ART-B5-SECULAR | exact match | `DYAD-ART-B5-SECULAR` | — |
| AZ v0.6 §8 | DYAD-ALG-Q3-CANCEL | unmatched | statement = the degree-2 $q=3,(0,2)$ cancellation (§6.11 micro-certification, no RID in v6.4.19) | `DYAD-ALG-Q3-DEG2-CANCEL` (registered at v6.4.20 adoption) covers the statement; no alias is created; AZ may repin |

---

## Appendix G — Old→new section map {#appendix-g}

`[DEF]` `[v6.4.20]` Every v6.4.19 heading and its place in this edition. Anchors are kept. Relocated text is listed in Appendix A (H-P2-*).

| v6.4.19 | v6.4.20 (headings as in r1) | Change |
|---|---|---|
| header (title, metadata, status summary, release summaries) | compact header | v6.4.19 header relocated verbatim to Appendix A (H-P2-1) |
| `## Local Tag Aliases` | `## Local Tag Aliases` | tag normalization map, version markers, RID tag convention and CAND lookup added |
| `## §1. Current Canonical State {#sec-1-canonical-state}` | `## §1. Current Canonical State {#sec-1-canonical-state}` | fixed-point scope table added; Audit-1 clause rewritten (H-P2-3) |
| `## §2. Active Frontier / OPEN Registry {#sec-2-open-registry}` | `## §2. Active Frontier / OPEN Registry {#sec-2-open-registry}` | OPEN 2B alias; OPEN 4b label note; B5 result pointer |
| `## §3. Scope Guards {#sec-3-scope-guards}` | `## §3. Scope Guards {#sec-3-scope-guards}` | SG-14 restated (H-P2-5); SG-17/18 note |
| `## §4. Layer Routing {#sec-4-layer-routing}` | `## §4. Layer Routing {#sec-4-layer-routing}` | $\phi_*$ removed (H-P2-6) |
| `## §5. High-Risk Claims Ledger {#sec-5-high-risk}` | `## §5. High-Risk Claims Ledger {#sec-5-high-risk}` | R11 row conditions (H-P2-7); r2: absolute-value bars inside math in table rows written as `\vert` (3 rows) |
| `## §6. Main Scientific Ledger {#sec-6-ledger}` | `## §6. Main Scientific Ledger {#sec-6-ledger}` | unchanged |
| `### §6.1 Core Map and Fixed Points '[ALG / mixed]' {#sec-6-1-map}` | `### §6.1 Core Map and Fixed Points — entry grades: ALG, THM, DEF, FAIL {#sec-6-1-map}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.2 Linear Structure and Cubic Coefficient '[THM / mixed]' {#sec-6-2-cubic}` | `### §6.2 Linear Structure and Cubic Coefficient — entry grades: ALG, THM {#sec-6-2-cubic}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.3 Canonical Constants '[ALG]' {#sec-6-3-constants}` | `### §6.3 Canonical Constants — entry grades: ALG {#sec-6-3-constants}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.4 ISP Coordinate System '[ALG structure]' {#sec-6-4-isp}` | `### §6.4 ISP Coordinate System — entry grades: ALG, DEF {#sec-6-4-isp}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.5 Backbone and Asymptotic Structure '[ALG]' {#sec-6-5-backbone}` | `### §6.5 Backbone and Asymptotic Structure — entry grades: ALG, THM, DEF, OPEN {#sec-6-5-backbone}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.6 Resonant Structure and Homological Algebra '[ALG structure / THM]' {#sec-6-6-resonance}` | `### §6.6 Resonant Structure and Homological Algebra — entry grades: ALG, DEF, OPEN {#sec-6-6-resonance}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.7 Six-Step Cubic Jet and Complex Form '[ALG]' {#sec-6-7-jet}` | `### §6.7 Six-Step Cubic Jet and Complex Form — entry grades: ALG {#sec-6-7-jet}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.8 ISP Transport and Footprint '[ALG structure / THM-ALG via IA]' {#sec-6-8-transport}` | `### §6.8 ISP Transport and Footprint — entry grades: THM-ALG via IA, ALG {#sec-6-8-transport}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.9 Normalization Hierarchy and Gauge '[ALG / mixed]' {#sec-6-9-normalization}` | `### §6.9 Normalization Hierarchy and Gauge — entry grades: ALG, DEF, FAIL {#sec-6-9-normalization}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.10 OPEN 11 / Chirality Closure '[THM-ALG via IA / mixed]' {#sec-6-10-open11}` | `### §6.10 OPEN 11 / Chirality Closure — entry grades: THM-ALG via IA, ENG {#sec-6-10-open11}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.11 OPEN 9 — $p$-Resonance Arithmetic Horizon '[ALG / mixed]' {#sec-6-11-open9}` | `### §6.11 OPEN 9 — $p$-Resonance Arithmetic Horizon — entry grades: ALG, THM, OPEN, FAIL {#sec-6-11-open9}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.12 Dyad-to-Triad Bridge Export '[ALG]' {#sec-6-12-bridge}` | `### §6.12 Dyad-to-Triad Bridge Export — entry grades: ALG, DEF, CAND, OPEN {#sec-6-12-bridge}` | heading grade tag replaced by the computed entry-grade list; r2: absolute-value bars inside math in table rows written as `\vert` (1 row) |
| `### §6.13 Simulation Invariants and Audit Discipline '[ENG]' {#sec-6-13-audit}` | `### §6.13 Simulation Invariants and Audit Discipline '[ENG]' {#sec-6-13-audit}` | heading grade tag replaced by the computed entry-grade list; r2: absolute-value bars inside math in table rows written as `\vert` (1 row) |
| `### §6.14 Local Return Enclosure — Normalizer, Contraction, Inverse, Remainders '[ALG / THM]' {#sec-6-14-enclosure}` | `### §6.14 Local Return Enclosure — Normalizer, Contraction, Inverse, Remainders — entry grades: ALG, THM, DEF, OPEN, NUM, ENG {#sec-6-14-enclosure}` | heading grade tag replaced by the computed entry-grade list; r2: absolute-value bars inside math in table rows written as `\vert` (1 row) |
| `### §6.15 Local Involutions Commuting with the Return '[THM conditional / OPEN]' {#sec-6-15-involution}` | `### §6.15 Local Involutions Commuting with the Return — entry grades: THM, DEF {#sec-6-15-involution}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.16 Formal Centralizer of the Six-Step Return '[ALG / THM — formal]' {#sec-6-16-centralizer}` | `### §6.16 Formal Centralizer of the Six-Step Return — entry grades: ALG, THM, DEF, OPEN {#sec-6-16-centralizer}` | heading grade tag replaced by the computed entry-grade list |
| `### §6.17 Flat Centralizer Triviality '[THM / THM — conditional]' {#sec-6-17-flat}` | `### §6.17 Flat Centralizer Triviality — entry grades: THM, DEF, OPEN, NUM {#sec-6-17-flat}` | heading grade tag replaced by the computed entry-grade list |
| `## §7. Import Ledger {#sec-7-imports}` | `## §7. Import Ledger {#sec-7-imports}` | §7.0 editions, §7.0a L-PHASE interface and the notice-state table replace the old context list, rows and notice table (H-P2-10) |
| `## §8. Artifact and Script Registry {#sec-8-artifacts}` | `## §8. Artifact and Script Registry {#sec-8-artifacts}` | ATLAS artifacts; FA-04 custody note; double escapes repaired |
| `## §9. Collaboration and Provenance {#sec-9-provenance}` | `## §9. Collaboration and Provenance {#sec-9-provenance}` | unchanged |
| `## Appendix A — Version History {#appendix-a}` | `## Appendix A — Version History {#appendix-a}` | v6.4.20 adoption record, DRAFT r2 and r1 records added; P1 record and older history retained |
| `## Appendix B — Retired and Rejected Claims {#appendix-b}` | `## Appendix B — Retired and Rejected Claims {#appendix-b}` | unchanged |
| — | `### §7.0 Current editions and source pins {#sec-7-0-editions}` | new in v6.4.20 |
| — | `### §7.0a L-PHASE row-A export interface (I1–I5) {#sec-7-0a-lphase}` | new in v6.4.20 |
| — | `## Appendix C — Notation {#appendix-c}` | new in v6.4.20 |
| — | `## Appendix D — OPEN 9 definitions (recovered) {#appendix-d}` | new in v6.4.20 |
| — | `## Appendix E — Claim-to-evidence matrix {#appendix-e}` | new in v6.4.20; r2: grade/scope rule, three rows corrected, reviewer replays recorded |
| — | `## Appendix F — DZT / AZ string crosswalk {#appendix-f}` | new in v6.4.20 |
| — | `## Appendix G — Old→new section map {#appendix-g}` | new in v6.4.20 |
| footer (v6.4.19 and inherited footers) | single footer | relocated verbatim to Appendix A (H-P2-12) |

---

*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.20*  
*Adopted 21 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.19 (adopted 20 October 2026). v6.4.20 carries the ATLAS P1 scientific corrections and the P2 interface work; it registers 13 new RIDs and changes no earlier grade or OPEN status (OPEN 20 PARTIAL; B-an, B-6 OPEN). The replaced DRAFT r2 lines, including its footer, are quoted in Appendix A (v6.4.20 adoption record); the r1 footer is in the DRAFT r2 record, the v6.4.19 and inherited footers in the r1 record (H-P2-12).*
