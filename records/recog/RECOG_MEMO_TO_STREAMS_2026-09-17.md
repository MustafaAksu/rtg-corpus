# RECOG → Other Streams — Memo 2026-09-17 (amended 2026-09-18)

**From:** RTG Relational Recognition study (`RTG_RELATIONAL_RECOGNITION_DSN_v0.2.1`, prefix `RECOG`, Tier 3)
**To:** Dyadic (`DYAD`), Genesis (`GEN`), Number Genesis (`NUMGEN`), Ontological Foundations (OFN), Discrete Genesis / TDR-G (`TDRG`), Methodology & Programme Overview
**Purpose:** (a) hand over results that belong upstream or that other streams can use now; (b) state what RECOG needs from each stream, distinguishing *blocking* from *housekeeping*; (c) record what RECOG has already solved on another stream's behalf so it can be adopted rather than redone.
**Discipline:** every item carries its DSN tag and scope. Nothing here is an ontological theorem (RECOG SG-R1). All results are conditional on the postulated continuous generator $T$ and, where stated, on the $p$-resonant family $K_p=2-\lambda-\bar\lambda$.

---

## 0. One-page summary — **status as of 19 Sep; superseded by §6d (25 Sep): R11 closed, five Dyadic RIDs accepted, NUMGEN radius request withdrawn, no upstream blocker remains**

| Stream | We hand over | We need | Blocking? |
|---|---|---|---|
| DYAD | general resonant-return theorem for all $p\ge5$; closed form $\nu_3(\lambda)$ and its empty unit-circle zero set; $\Re\mu_p=-p\sin^2(\pi/p)$; CELL-B data on $P_2$ manifolds (OPEN 12); post-$H_2$ six-step quintics | **R11 (§6c): declare the frame of the §6.9 quintic ledger and §6.5 backbone; supply the coordinate ledger $W_{\rm raw}\leftrightarrow W_{H_2}\leftrightarrow W_{\rm final}$**; RID assignment for §6.1/§6.4/§6.7 blocks; ownership of the general theorem; OPEN 9 update | **yes (R11), precedes the enclosure** |
| GEN | comparator identity $\overline W_aW_b=I_{ab}-i\tfrac{\sqrt3}{2}\omega_{ab}$; invariant-form uniqueness $H=cB$ | RIDs for §6.1 ($B$, $A^\top BA=B$) and §6.6 ($I_{ab},\omega_{ab},J_Q$); confirmation that $\theta_{ab}$ is the eigenframe angle; explicit $J_Q$ sign-branch statement | no |
| NUMGEN | strong numerical evidence for the heteroclinic connection $W^u_-(P_2)\to P_1$ with concrete entry numbers; lattice reading of the defect-threshold rate | **explicit-radius healing-tube theorem** (contraction half of `RETURN-ENCLOSURE`, posed after R11); dedicated RID for the defect-threshold rate theorem | **yes** (blocks CELL-B2), after R11 |
| OFN | conditional derivation of the $-\sin\eta$ radial row; conditional $\rho$ swap-odd; three-way split of §6.2a rows; CELL-0 functional consequences; pole/state comparator distinction | adopt two `[DEF]` lines; receive the interpretive `[HYP]` lines moved out of RECOG; reword §6.2a status; sharpen §7.3 band question | no |
| TDRG | the continuous $P_2\to C_0$ excursion is a lifted $278.66^\circ$ traversal, not a symmetric band | say whether $\mathcal D_k$ is a wrapped half-width or a discretised oriented excursion; keep SG-R5 | no |
| Methodology / Programme | — | register `RECOG` prefix; list study in Tier 3 at Maturity A; note `[ALG conditional]` / `[ALG diagnostic]` as document-local aliases | housekeeping, same release |

---

## 1. To Dyadic (`DYAD`)

### 1.1 Results we believe belong in the Dyadic $p$-resonance layer (adopt, do not redo)

**General resonant-return theorem** `[ALG]` [scope: $p$-resonant family, eigenframe $\rho=uZ+\bar u\bar Z$, $\eta=Z+\bar Z$, $u=1/(1-\lambda)$]. For $p\ge5$:
$$[F_p^p-\mathrm{id}]_2=0,\qquad [F_p^p-\mathrm{id}]_3=p\bar\lambda\,\nu_3^{(1,p)}\,Z^2\bar Z .$$
Proof: after $h_2$ (exists for $p\ge4$), the linear part of $F^p$ acts on $Z^a\bar Z^b$ by $\lambda^{p-1}\sum_{k=0}^{p-1}\lambda^{k(a-b-1)}$, nonzero only for $a-b\equiv1\pmod p$; degree 2 never, degree 3 only $(2,1)$ for $p\ge5$. Since $F^p$ is tangent to identity with vanishing quadratic part, its cubic term is invariant under the near-identity conjugacy relating raw and normalised maps, so raw $p$-fold composition sees the same coefficient. This generalises the master parity lemma (which used $A^3=-I$) and *is* the bridge lemma `DYAD-ALG-BRIDGE-LEMMA` in its general form. **Consequence:** $k_{\rm ret}(p)\ge3$ always; $=3$ iff $\nu_3^{(1,p)}\ne0$.

**Closed form of the one-step resonant cubic coefficient** `[ALG]` [cert: `recog_cell_a2_nu3_closed_form_cert.py`, two independent routes]:
$$\nu_3(\lambda)=-\frac{\lambda^5-\lambda^4-\lambda^3-2\lambda^2+1}{2(\lambda-1)(\lambda+1)(\lambda^2+\lambda+1)} .$$
Depends on $\lambda$ only (the family, frame and $h_2$ are all $\lambda$-expressions). Verified exactly mod $\Phi_5,\Phi_7$ against the archived $p=7$ normaliser output and the new $p=5$ certificate, and against raw composition for $p=5\ldots12$. At $p=6$, $6\bar\lambda\nu_3(\zeta_6)=3\mu_6^{W}$ exactly (frame scale $|c|^2=\tfrac13$ between the $Z$- and $W$-frames).

**Empty zero set** `[ALG]`: the numerator $N(\lambda)$ satisfies $\gcd(N,\lambda^5N(1/\lambda))=1$ (no root on $|\lambda|=1$) and $\gcd(N,\Phi_p)=1$ for all $p$ with $\varphi(p)\le5$. Hence $\nu_3^{(1,p)}\ne0$ and $k_{\rm ret}(p)=3$ **for every $p\ge5$**. There is no cubic-silent horizon. (OPEN 9's "$p=8$ zero" is the $q=4,(0,3)$ strobe channel and is untouched by this.)

**Frame-invariant radial sign** `[ALG]` (leading order) / `[NUM]` (interval): with $\lambda=e^{i\theta}$,
$$\bar\lambda\nu_3=-\tfrac{i}{6\theta}-\tfrac{i\theta}{2}-\tfrac{\theta^2}{4}+\tfrac{11i\theta^3}{120}+\tfrac{\theta^4}{48}+O(\theta^5),$$
so $\Re\mu_p=p\Re(\bar\lambda\nu_3)\to-\pi^2/p$, and $\Re(\bar\lambda\nu_3)<0$ on a fine mesh of $(0,2\pi/5]$. Since $\operatorname{sign}\Re\mu$ is invariant under $Z\to cZ$: the six-step-type return is healing for every sampled $p$, with $\arg\mu_p$ increasing monotonically toward $-90^\circ$ ($-120.96^\circ,\,-113.41^\circ,\,-108.33^\circ$ at $p=5,6,7$).

**Scope guard to carry with these:** the RECOG shear-jet rigidity $|\mu_6(a,b)|\ge\tfrac12$ is a $K=1$, $p=6$ theorem over shear jets; the family result above is a $K_p$, all-$p$ theorem at fixed shear. They agree at $p=6$ and are otherwise different statements.

### 1.2 Data for OPEN 12 ($P_2$ saddle manifolds) `[NUM strong]`

- $W^u_+(P_2)$ first transverse encounter with $C_0$ at $x_*=(\rho_*,\eta_*^{\rm lift})=(2.03336443891\ldots,\ 8.00516505150\ldots)$; $Q_*=3.5984$. Pole-comparator itinerary along the lift: $-1\to-i\ (\rho{=}0.9110)\to+1\ (\rho{=}1.6327)\to+i\ (\rho{=}2.0204)\to C_0$; lifted excursion $278.66^\circ$ in the $\ell=1$ sector; wrapped $\operatorname{dist}_{S^1}(\eta_*,\pi)=81.34^\circ$ is derived from the $C_0$ equation, not an independent scale.
- $W^u_-(P_2)=\bigcup_{k\ge0}T^k(S)$ with $S=P_u([-\lambda_u,-1])$ (exact, from $P_u(\lambda_ut)=T(P_u(t))$). Every sampled point of $S$ reaches $Q<0.3$ within 12 primitive steps; max $Q$ en route $3.95$; min $\det J$ en route $0.1367$; six-step $Q$ then decays monotonically to $n=1200$. Strong evidence for $W^u_-(P_2)\to P_1$.
- Exact companion `[ALG]`: $\rho<0\Rightarrow0<\det J<2$ (no rank loss in the negative-$\rho$ half-plane). Note $W^u_-$ is *not* confined there (reaches $\rho\approx0.62$ near $\eta\approx-0.07$).
- Artifacts: `recog_cell_b_p2_manifolds.py` (contributor, sha256 `7ea5e161…b216e`).

### 1.3 Requests (housekeeping, not blocking)

1. Assign stable RIDs to the Dyadic §6.1 block (map, $J$, $\det J$, $C_0$, $P_1,P_2$, escape law, non-symplecticity), §6.4 block ($Q_c$, winding invisibility, ISP $\Theta$) and §6.7–6.8 block ($M+M^\top=-I$, $Q$- and $\Theta$-laws). RECOG imports all three and currently cites by section.
2. Decide ownership of the general resonant-return theorem (§1.1). RECOG's recommendation: Dyadic owns it; RECOG imports and records only the $k_{\rm ret}$ consequence.
3. Update the OPEN 9 finite ledger with $\nu_3^{(1,5)}=(12-\lambda+\lambda^2+8\lambda^3)/10$ and $\nu_3^{(1,7)}=(12-4\lambda+\lambda^2+6\lambda^3-3\lambda^4+9\lambda^5)/14$, and note that the closed form makes the finite ledger a special case.
4. Rename the archived `nu3_full^(7)` to $\nu_3^{(1,7)}$ on import ("full" = full sequential one-step normalisation, not $p$-step).

---

## 2. To Genesis (`GEN`)

### 2.1 Results (exact consequences of Genesis definitions; adopt or cross-reference)

- **Comparator identity** `[RESULT] [from: ALG]`: with $W=\rho+\omega\eta$, $\omega=\tfrac12(-1+i\sqrt3)$, $B=\begin{psmallmatrix}1&-\frac12\\-\frac12&1\end{psmallmatrix}$, $J_Q=\tfrac1{\sqrt3}\begin{psmallmatrix}1&-2\\2&-1\end{psmallmatrix}$ and the Genesis $+$ convention $a^\top BJ_Qb=+\tfrac{\sqrt3}{2}\omega_{ab}$:
  $$\overline W_aW_b=a^\top Bb-i\,a^\top BJ_Qb=I_{ab}-i\tfrac{\sqrt3}{2}\omega_{ab},\qquad W_a\overline W_b=I_{ab}+i\tfrac{\sqrt3}{2}\omega_{ab}.$$
  RECOG's state comparator $C_\to=\overline W_aW_b$ is therefore the *conjugate orientation* of the Genesis pairing (RECOG SG-R9). We flag this because a $+i$ pairing with $\overline W_aW_b$ was an actual sign error in RECOG v0.1; anyone else combining these objects will hit the same trap.
- **Invariant-form uniqueness** `[ALG]` [`RECOG-ALG-INVARIANT-FORM`]: every symmetric $H$ with $A^\top HA=H$ is $H=cB$. This upgrades "$B$ is the invariant form" to "$B$ is the *only* one up to scale"; Genesis may want it beside $A^\top BA=B$.

### 2.2 Requests (housekeeping)

1. RIDs for §6.1 ($\mathcal O_0=0$, first dyad $A+B=0$, $B$, $Q=r^\top Br$, $A^\top BA=B$) and §6.6 ($I_{ab}$, $\omega_{ab}$, $J_Q$, plateau phase memory $\Phi_{ab}(\infty)=\Phi_{ab}(0)-\tau\log(q_a/q_b)$).
2. Confirm that $\theta_{ab}$ in §6.6 is the eigenframe angle difference $\arg W_b-\arg W_a$; the comparator identity assumes it.
3. State the $J_Q$ sign branch explicitly as a convention line (`[DEF]`), since it fixes the complex orientation of every downstream comparator.
4. Note for the plateau memory: RECOG certifies that three-quarters of the *local cubic angular return coefficient* is swap-breaking-mediated ($\Im\mu_6^{(s)}=\tfrac14\Im\mu_6$); no additive decomposition of the asymptotic plateau law is claimed, because that law also uses the healing backbone. Please do not import a "three-quarters of $\tau$" statement.

---

## 3. To Number Genesis (`NUMGEN`) — **blocking request**

### 3.1 What we have

Strong numerical evidence (§1.2) that the negative unstable branch of the antipodal saddle enters the $P_1$ healing regime: from the fundamental domain $S$, entry to $Q<0.3$ within $\le12$ steps, $\det J>0$ throughout, monotone six-step decay thereafter. If certified, $W^u_-(P_2)\subset\mathcal B(P_1)$ and the antipodal saddle globally separates a rank-loss-directed branch from a healing-captured branch.

### 3.2 What blocks certification — and it is upstream

`NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION` gives $Q(T^6x)-Q(x)=-Q^2+O(Q^{5/2})$ with contraction on a *sufficiently small, unspecified* punctured sector, and the corpus explicitly marks numerical membership in $U_T$ as uncertified. RECOG cannot close this from its imports.

**Amendment 18 Sep — one deliverable, two RECOG theorems.** A second RECOG result (CELL-D, retained lattice phase memory $\Lambda$) needs an explicit degree-$\ge7$ remainder bound on the same six-step return germ, because $\sum_mQ_m^3=O(q^2)$ enters at the order being bounded. The heteroclinic certification (B2) needs the explicit contraction domain. These are the same object. RECOG therefore replaces its two separate requests with one (RECOG OPEN R10, proposed upstream RID `DYAD/NUMGEN-OPEN-RETURN-ENCLOSURE`): explicit $r_0>0$, $C_7$, $c>0$ such that on $|W|^2\le r_0$ in the Lie strict-kernel chart
$$\bigl|T^6(W)-W-\mu|W|^2W-c_{32}|W|^4W-c_{05}\overline W^5\bigr|\le C_7|W|^7,\qquad Q(T^6x)\le Q(x)-cQ(x)^2,$$
with a scalar sufficient membership criterion — **in the R11-resolved normal-form chart** (the 18 Sep wording "Lie strict-kernel chart" is withdrawn; the chart must be fixed by R11 first). The original formulation below is retained as the contraction half of that deliverable.

**Requested theorem** (proposed RID `NUMGEN-OPEN-L1-EXPLICIT-RADIUS`, now the contraction half of `RETURN-ENCLOSURE`): an explicit $r_0>0$ and, ideally, explicit $c>0$ such that
$$0<Q(x)\le r_0\ \Longrightarrow\ Q(T^6x)\le Q(x)-c\,Q(x)^2\quad\text{and}\quad Q(T^6x)\le r_0,$$
plus a **scalar sufficient criterion** if the invariant domain is currently defined by a six-image phase-tube condition rather than a $Q$-threshold. The route is a rigorous remainder bound on $Q(T^6x)-Q(x)+Q(x)^2$ in terms of $Q^{5/2}$.

**Design numbers from our side:** an $r_0\ge0.3$ closes CELL-B2 with the existing 12-step enclosure; a smaller $r_0$ only lengthens the enclosure by a few six-step blocks. Either way the RECOG-owned part (`RECOG-OPEN-P2-HET-ENTRY`: interval-enclose $S$, iterate, verify entry and $\det J>0$) is finite.

**Why this is not a one-off favour:** the same explicit radius removes the "membership in $U_T$ not certified" guard on Number Genesis' own long-orbit results, and would let the RECOG local statements ($k_{\rm ret}$, $Q_c$ protection) be stated on an explicit neighbourhood instead of "small punctured sector".

---

## 4. To Ontological Foundations (OFN)

### 4.1 Findings that touch OFN §6.2a (generator motivation)

- **Row 1 "why does phase opposition change radial separation"** — candidate conditional derivation `[ALG conditional]` [`RECOG-ALG-SELECTION-SIN`]: pole-swap covariance + $2\pi$-periodicity + stationarity on the swap-fixed pole strata $f(0)=f(\pi)=0$ + lowest nonzero harmonic $\Rightarrow f(\eta)\propto\sin\eta$. The lemma selects the functional form only, not the coefficient. Under swap-even $\rho$ the same assumptions give $\propto\sin^2\eta$ (sign-definite drift, no elliptic $P_1$); so the certified linearisation forces $\rho$ swap-odd (`[ALG conditional]`).
- **Row 2 "why exponential shear"** splits in three: $e^\rho-1=\sinh\rho+(\cosh\rho-1)$. The odd part is admissible but *not selected* by the lemma ($\rho$, $\sinh\rho$, $\tanh\rho$ all pass). The even part $\cosh\rho-1$ is the entire swap-non-equivariant content of $T$ and its only quadratic term. **Certified functional consequence** (`[ALG]`, shear-jet law $\mu_6(a,b)=3b-4a^2-i\sqrt3(\tfrac13+2a^2-b)$): radial fate is healing iff $4a^2>3b$; $\log r$ drive is neutral, $\sinh\rho$ drive expands, $\tanh\rho$ and $e^{\kappa\rho}-1$ drives heal. Healing does **not** require swap breaking. The one-sided rank stratum $C_0$ (only $\rho\ge\ln2$) is also sourced by the even part. The open question is now precise: *why one-sided ratio shear* $r-1$ rather than $\log r$ or $\tfrac12(r-r^{-1})$ (`RECOG-OPEN-ONESIDED-SHEAR`).
- The stationarity of $P_1,P_2$ on the swap-fixed pole comparisons $\widehat C_{\rm pole}=\pm1$ is a *consequence* of the $-\sin\eta$ row, not an independent coincidence; OFN should not cite it as evidence for anything beyond the lemma above.

### 4.2 Definitions we ask OFN to adopt

1. `[DEF]` **Pole comparator vs state comparator.** $C_{\rm pole}(A,B)=e^{i\eta}$ (within one dyad; swap $\Rightarrow$ inverse; swap-fixed set $\pm1$) is distinct from the state comparator $C_\to(a,b)=\overline W_aW_b$ between two dyad states. Antipode statements must name their comparator.
2. `[DEF]` (conditional on pole-swap covariance `[HYP]`) $\rho$ is an oriented relational coordinate, swap-odd. If OFN prefers not to adopt covariance as a primitive, please record the parity as `[OPEN]` with the RECOG argument attached.

### 4.3 Interpretive lines moved out of RECOG (to be housed here as `[HYP]`)

"Existence $=$ recognisability" (substrate witness: $0<Q<\epsilon\Rightarrow T^6x\ne x$ with nontrivial return defect); "a physical event is a jump of the mathematical equivalence class, not an imposed threshold"; "closure is arithmetic, closure defect geometric, recognition comparison"; "$-1$ is the unique nonidentity swap-fixed comparison" as the algebraic content of "maximal distinction". RECOG's §6.9 export interface lists exactly which substrate objects may be cited for these.

### 4.4 §7.3 (TDR-G antipodal band) — see §5.

---

## 5. To Discrete Genesis / TDR-G (`TDRG`)

**Finding** `[NUM strong]`, continuous side only: the dynamically selected escape from the antipodal saddle traverses $278.66^\circ$ of lifted pole angle in the $\ell=1$ sector, crossing $\widehat C_{\rm pole}=\pm i$, $+1$, $\pm i$ before rank loss; the wrapped $81.34^\circ$ is a shadow. The continuous dyad therefore supplies an **oriented excursion**, not a symmetric band around $\pi$. The saddle spectrum $\phi^{\pm2}$ fixes width–lifetime scaling but no width (`RECOG-FAIL-K-FROM-SADDLE`).

**Request** (not blocking; SG-R5 stays in force — no identification without a bridge):
1. Is $\mathcal D_k=\{\operatorname{dist}(\Delta,N/2)\le k\}$ meant as a wrapped half-width or as the discretisation of an oriented encounter scale? These lead to different candidate derivations of $k$.
2. A falsifiable comparison would put three rules side by side under identical relational criteria: antipode-centred ($N/2$), quadrature-centred ($N/4,3N/4$), and oriented-excursion-centred. OFN §7.3 currently motivates $N/2$ by "maximal distinction"; RECOG offers the purely algebraic version of that motivation ($-1$ is the unique nonidentity swap-fixed value), which is neutral between the three rules.
3. STAR-NOERASE-1 and the continuous $Q_c$ protection are two witnesses for no-erasure in two substrates; please keep them unlinked until a bridge theorem exists.

---

## 6. To Methodology and Programme Overview

1. Register `RECOG | RTG Relational Recognition` in the DSN_METHODOLOGY RID-prefix table (RECOG already emits stable RIDs).
2. List the study in Programme Overview Tier 3, Maturity Level A, "downstream diagnostic of Dyadic/Genesis".
3. Document-local aliases in use (no registration needed per v1.2, listed for transparency): `[ALG consequence]` $=$ `[RESULT] [from: ALG]` [scope: exact consequence of imported definitions]; `[ALG conditional]`; `[ALG diagnostic]`.
4. Suggested new upstream OPEN RIDs: `NUMGEN-OPEN-L1-EXPLICIT-RADIUS` (§3), and Dyadic-side ownership entry for the general resonant-return theorem (§1.1).

---

## 6b. Addendum 18 Sep — results since the memo (for Dyadic, Genesis, NUMGEN, TDR-G)

- `[ALG]` Leading-return equivariance $LG_k=G_k\circ L$ and comparator closure through degree $p-2$; first non-comparator channel $\bar W^{p-1}$. Genesis' $Q,I,\omega$-form of $\Delta Q_d^{(4)}$ is an instance.
- `[ALG]` For $p=6$: $\chi_6=1+\mu Q+(c_{32}+c_{05}e^{-6i\Theta})Q^2$; $\beta=c_{32}-\mu^2/2$ has $\Im\beta=c_\theta^{(6)}$ exactly (consistency check for Dyadic §6.9).
- `[ALG consequence]` Lattice clock: $\pi/3$ phase-defect thresholds (NUMGEN rate $e^{\pi/(3\tau)}$) are lattice-readable because $c_{05}\ne0$; ratio $=\lambda_{\rm DSI}^{1/6}=(R^*)^{1/3}$. Request to NUMGEN: **assign a dedicated RID** to the defect-threshold rate theorem (currently nested under `NUMGEN-OPEN-N5AS1-INF`; suggested `NUMGEN-ALG-N5AS1-DEFECT-RATE`, naming left to owner).
- `[ALG consequence, leading order]` Retained lattice memory $\Lambda=\tfrac{Q_0}{1270080}[43\sin6\Theta_0-5611\sqrt3\cos6\Theta_0]+O(Q_0^2)$ (post-$H_2$ frame; the 17 Sep raw-frame value is withdrawn); no $\log Q$ memory; identical comparator data can yield different retained memory. For Genesis: the plateau law acquires a non-comparator correction at $O(Q_0)$. For TDR-G: two bridge statistics — spacing $n_{k+1}/n_k\stackrel?\to\lambda_{\rm DSI}^{1/6}$ and comparator-completeness of retained discrete state (SG-R5 unchanged).
- Additional artifacts: `recog_cell_c_lattice_readability_cert.py` (`73a919e2…6083`), `recog_cell_d_lattice_memory_cert.py` rev. 2 (`5c678051…d3ad`).

## 6c. Addendum 18 Sep (evening) — after external audit: a Dyadic request that now precedes R10

**To Dyadic (blocking for RECOG R9/R10).** External audit, confirmed by independent $H_2$ conjugation in RECOG: the §6.9 quintic coefficients $c_{32}=-\tfrac{77}{216}+i\tfrac{97\sqrt3}{648}$, $c_{05}=-\tfrac{61}{2160}-i\tfrac{43\sqrt3}{6480}$ are coefficients of the **raw** six-step map in the linear eigenframe (nonzero quartic jet), although the ledger attaches a Lie-gauge qualifier. Post-$H_2$: quartic jet zero, $c_{32}^{\rm NF}=-\tfrac{97}{432}+i\tfrac{197\sqrt3}{324}$, $c_{05}^{\rm NF}=-\tfrac{49}{8640}-i\tfrac{307\sqrt3}{25920}=6\bar\lambda\nu_5^{(1,6)}$ exactly (your §6.11 one-step value). Consequently $47/54=|\mu|^2+2\Re c_{32}^{\rm raw}$ and $\Im\beta^{\rm raw}=c_\theta^{(6)}$ are raw-frame identities, and $|\mu|^2+2\Re c_{32}^{\rm NF}=245/216$. Request: state the frame of the §6.9 ledger and of the §6.5 asymptotic backbone explicitly, and record both frames with the $H_2$ relation. Until then RECOG carries this as OPEN R11 and has restated its lattice numbers post-$H_2$ ($\mathcal I_{\rm lat}\approx0.01344$).

**To Dyadic (housekeeping).** §6.1 lists fixed points $P_1,P_2$ only; on the wrapped cylinder $\eta'\equiv\eta\pmod{2\pi}$ also admits $(\log(1+2\pi k),0)$ and $(\log(1+2\pi k),\pi)$, $k\ge1$ ($\det J=1\pm2\pi k$). Worth a line, even if only to exclude them by sector. Also: `DYAD-ALG-BRIDGE-LEMMA` lives in §6.9, not §6.2 as RECOG had cited.

**Exact identity handed over (from the audit):** $\Re(\bar\lambda\nu_3(e^{i\theta}))=-\sin^2(\theta/2)$, hence $\Re\mu_p=-p\sin^2(\pi/p)$ in the $Z$-frame for every $p$.

**Updated artifact:** `recog_cell_d_lattice_memory_cert.py` rev. 3 (`b92b9936…59cd`, 25 checks) derives both frames from the primitive map.

## 6d. Addendum 25 Sep — consumer acceptance of Dyadic v6.4.10 §6.14; R11 filled

**To Dyadic.** RECOG v0.3.2 accepts `DYAD-ALG-NF6`, `DYAD-ALG-NF6-OBS`, `DYAD-THM-PRIM-CTR`, `DYAD-THM-NF-INV`, `DYAD-THM-NF-REM` as imports (your §7 proposed-consumer row can be marked accepted). Per SG-19 the final-chart ledger is RECOG-owned; it is filled in RECOG §6.14 from $J$ alone: $|J|^2=q-q^2+[\tfrac{245}{216}+2\Re(a_{05}e^{-6i\Theta})]q^3+\ldots$, $\arg(J/z)=-\tau q+[\tfrac{89\sqrt3}{324}+\Im(a_{05}e^{-6i\Theta})]q^2+\ldots$; two comparator tracks; $S_h$ covariance defect $\tfrac32t^3$ reproduced. Nothing archival ($\tfrac{47}{54}$, $c_\theta^{(6)}$, $a_1$, $a_2$) is used. Note for your own ledger: the chart quintic phase coefficient is $+\tfrac{89\sqrt3}{324}$, opposite in sign to $c_\theta^{(6)}$. **Request (optional, now justified by a downstream budget):** the deferred $C_7$ sharpening — RECOG R9's leading lattice-memory term dominates the degree-7 remainder only for $q_0<3.8\times10^{-5}$ at $C_7=100$; an $O(10)$ constant would raise this by an order of magnitude. Still outstanding from the 17–18 Sep items: winding fixed points in §6.1.

**To NUMGEN.** The contraction half of the enclosure exists (`DYAD-THM-PRIM-CTR`, seed admitted to the tube); RECOG withdraws its separate `L1-EXPLICIT-RADIUS` request. The dedicated RID for the defect-threshold rate theorem is still requested.

**To OFN / ontology note.** R6's `[HYP]` is reworded as readability emergence (retained information made readable, not created) per the PRR Wrap-up; the physical pole-relabeling question is RRF OPEN-A, not closed by R11.

**To TDR-G.** Unchanged (SG-R5); the network guard $h(z_{AB})+h(z_{BC})+h(z_{CA})=0\ne\sum z_e$ is now explicit.

**Artifact:** `recog_r11_chart_ledger_cert.py` (`a4950ed5…e5e5`, 11 checks).

## 7. Artifact registry (all run to PASS in the RECOG session)

| Artifact | sha256 | Content |
|---|---|---|
| `recog_shear_jet_cert.py` | `e1d2444f9d8d8c940270d73df4ca20d0323504d93f89dbb2fe6da1a9a3fe48a4` | 18 checks: $T=T_s+T_b$, shear-jet law, rigidity, comparator orientation, $J_Q$ properties, $H=cB$, fate-boundary corollary |
| `recog_cell_b_p2_manifolds.py` (contributor) | `7ea5e161b9ffa244b279681a067047e66a0a477a29477d0946637694f10b216e` | $W^u_+(P_2)\cap C_0$, transversality, opposite-branch scan |
| `normalize_p7_full_onestep_cyclotomic.py` (archived Dyadic) | `7cea7b43954c534c7f79113de85164614bb38ec3e7aa0f76360bf1930f1716a9` | exact $\nu_3^{(1,7)}$, $\nu_5^{(7)}$ |
| `recog_cell_a_p7_rawcomp_cert.py` | `0414f3a031a4bf9bfe2d1a7d508128114f78d2ca5a28f7b3e99823a62f1979ab` | raw seven-fold composition, independent $\mu_7$ |
| `recog_cell_a_p5_rawcomp_cert.py` (contributor) | `0a87d59d600a11414fb1b26dd90ef770d3e2ae282a2e5da7b61c8ab648f84383` | exact $\mathbb Q(\zeta_5)$ raw composition, $\mu_5$, $\nu_3^{(1,5)}$ |
| `recog_cell_a2_nu3_closed_form_cert.py` | `222c964532a48e04dd37baeb86017620060b8dece250a135552b83d3e3cab2cd` | closed form $\nu_3(\lambda)$, empty zero set, series, sign scan |

---

## 7b. Artifact registry addendum (19 Sep)

| Artifact | sha256 | Content |
|---|---|---|
| `recog_cell_c_lattice_readability_cert.py` (contributor) | `73a919e24fe5349e7a0944e4c1dc4aeb9fc7d1bd43f8d89f3e25e29ee1476083` | raw-frame quintic identities (6 checks); numbers superseded pending R11 |
| `recog_cell_d_lattice_memory_cert.py` rev. 4 | `242b13e33357b7e41c5575a4a39d6eff24b26773fa38360a4effcf85592a8b7f` | raw and post-$H_2$ six-step jets from the primitive map, $c_{05}^{\rm NF}=6\bar\lambda\nu_5^{(1,6)}$, retained lattice memory, identical-comparator counterexamples (post-$H_2$ and canonical raw); 26 checks |

## 8. State of RECOG after this memo — **status as of 19 Sep (historical); current state in §6d**

Closed: OPEN R2 (finite and general — $k_{\rm ret}(p)=3$ for all $p\ge5$); the positive-branch part of OPEN R3 as `[NUM strong]`.
Open, RECOG-owned: `RECOG-OPEN-P2-HET-ENTRY` (finite enclosure), R4 (intrinsic type-change locus), R5 (one-sided ratio shear), R6 (event rule), R7 (twin accessibility).
Open, blocked upstream (19 Sep): **R11 quintic-frame reconciliation with Dyadic is the current blocker**; it precedes the single `RETURN-ENCLOSURE` deliverable (R10, contraction half formerly `NUMGEN-OPEN-L1-EXPLICIT-RADIUS`), which in turn unblocks R8 (heteroclinic) and R9 (finite-$Q_0$ memory bound).
Next RECOG action after the Dyadic reply: restate R9's backbone and CELL-C's fractions in the declared frame, then interval enclosure of $S$; until then, no further global-manifold numerics.

**Current (25 Sep, §6d):** Dyadic v6.4.10 delivered and RECOG v0.3.2 accepted; R11 CLOSED; R10 delivered; next actions R8 interval enclosure → R9 finite-$q_0$ memory bound, both RECOG-internal. Outstanding upstream items are non-blocking: NUMGEN defect-rate RID; Dyadic winding fixed points; optional $C_7$ sharpening; RECOG prefix / Tier 3 registration.

*END OF MEMO*
