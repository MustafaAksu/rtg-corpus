# RECOG A1a — Scientific Cell Draft v0.4: $C_D$ identification and an alternative existence route for the asymptotic phase

**Date:** 20 October 2026
**Status:** `[SESSION]` cell **draft** for a future, separately reviewed RECOG release.
- Nothing here is adopted, and no RID is registered; "(proposed)" RIDs are RECOG-owned proposals only.
- RECOG v0.3.21 is unchanged, and R6 stays ACTIVE.

**Supersedes:** draft v0.3 (`febed7f9…9562`), which superseded v0.2 (`7adace40…ad79`) and v0.1 (`511e3c1d…782d`).
- v0.2 applied R1–R5 of the v0.1 review (`02762139…f0e8b`).
- v0.3 applied P1–P2 of the v0.2 review (`1b1c664e…7068a0`).
- v0.4 applies three maintenance items, all record or provenance changes. No statement and no grade changes.
  - G1 and G2 come from the v0.3 review (`ACCEPTED WITH ONE GOVERNANCE NOTE — E2 OPEN`, `d9b20aea8303833e1b7abe5b70f5776c135efab32b2ee9a601784b87698d27a5`).
  - The E2 repin comes from the receiving source check `RECOG_A1A_E2_OPEN21_SOURCE_CHECK_v6_4_18_20261020.md` (`941f42d6273f707bb161c24bd7e753c12acacda991dd29ff4050cbdcbfa6126e`).
- The change list is in §6.

**Basis:** A1a session record v0.3 (`e542d105…8de0`, accepted). Grammar: DSN Methodology v1.3 §§3.3, 3.4, 4.3, 8.1.

**E2 gate:** PASS against adopted Dyadic v6.4.18 (§4). This is a source-statement fidelity check, not a recertification.

## 0. Grade principle (carried from v0.1 §0)

`[COR]` A1a v0.3 §6's "weaker-input rule" wording is superseded. Under Methodology v1.3 §3.4 (M13-C04):
- a fully proved implication keeps its own grade, with its hypotheses explicit;
- the weakest-premise rule applies only to an unconditional conclusion that uses its premises as true.

Every `[THM]` below is a mathematical grade inside the postulated-$T$ model, not a physical-selection claim; the model remains OPEN-P0. Dyadic T1/T2 and OPEN 21 **remain conditional in their own owner record**.

## 1. Imports at point of use (Methodology §3.3)

**Source-pin convention.** Each Dyadic import is pinned to the edition whose text was actually inspected for this draft. The **Verification** line records who inspected which bytes:
- **v6.4.16** (`33c14c5c…59e0`): release-verified; inspected by the reviewer.
- **v6.4.17** (`e07cf2b9…4bfc`): read by the RECOG owner.
- **v6.4.18** (`f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d`, adopted, in force): the reviewer inspected and rehashed this source for E2. The checked passages are §6.14 lines 806–809 (primitive-variable form) and lines 843–850 (OPEN 21 theorem and rows).
- The Dyadic owner reports that §6.14 is byte-identical between v6.4.17 and v6.4.18. This is **owner-reported** and was not independently checked.

No edition is described as independently inspected where it was not.

`[DEF]` [import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6 N-5A-S1-INF, INF-1 statement | RID unavailable]
- Phase defect $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$, quoted verbatim. $\hat\phi_n$ is the increasing lift of $\arg W$ along primitive steps, $n=0,1,\dots$, from an arbitrary start $x_0$ on NUMGEN's tube $U_{\rm NUMGEN}$.
- **Owner RID:** none for this definition or for the INF-1 statement in the inspected source. The module RID `NUMGEN-OPEN-N5AS1-INF` is not a theorem RID and is not used as one.
- **Governance disposition (G1):** `RID unavailable` is a **deferred governance decision; no method exception is claimed**. The import satisfies Methodology §3.3 through its `RID unavailable` form. RECOG requests no new owner RID, and NUMGEN's reply recommends at most a later provenance pointer. If NUMGEN registers a RID later, the import is repinned to it. Local tracking key `A1A-NG-D-DEF`.
- **Depends on:** NUMGEN's primitive frame $W$ and L-MONO branch control.
- **Verification:** NUMGEN v1.20.7 (`c4637e7a…ab28`) read by the RECOG owner and by the reviewer.

`[RESULT]` `[from: ALG]` [import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6, INF-1 | RID unavailable] [scope: $U_{\rm NUMGEN}$, which exists but has no stated radius; conditional on the selected continuous $T$ under OPEN-P0]
- $D_M=\tau\log M+C_D+o(1)$, with $C_D$ depending on the start $x_0$.
- **Owner RID / governance (G1):** as above: a deferred governance decision, with no method exception claimed. Local tracking key `A1A-NG-INF1`.
- **Depends on:** L1, L-BACKBONE, L-MONO and L-PHASE (NUMGEN). RECOG R9 is not used; the NUMGEN owner confirmed this in its reply `8a887ef3…bc4d`.
- **Verification:** owner text read by RECOG and by the reviewer; NUMGEN's certificate was not rerun.

`[THM]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 #sec-6-14-enclosure | DYAD-THM-PRIM-CTR]
- Primitive contraction $0<Q-\tfrac32Q^2\le Q(T^6x)\le Q-\tfrac12Q^2$ for $0<Q\le\tfrac1{400}$.
- $\lvert P_5\rvert\le\tfrac{16931}{10000}Q^{5/2}$ and $\lvert R^{\rm prim}_{\ge6,\rm rad}\rvert\le108Q^3$.
- Tube $U=\{0<Q\le\tfrac1{625}\}$ and $U_T=\bigcup_{j<6}T^j(U)$ with $T(U_T)\subseteq U_T\subset\{\lvert W\rvert<\tfrac{47}{1000}\}$; $Q_m\le Q_0/(1+\tfrac12Q_0m)$.
- **Depends on:** the postulated $T$ (Dyadic SG-14); an analytic majorant and exact-rational certificate (DYAD-ART-RE-P2B2).
- **Verification:** v6.4.16 text read by the reviewer; the same text in v6.4.17 read by the RECOG owner; unchanged since v6.4.10.

`[THM]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 #sec-6-14-enclosure | DYAD-THM-NF-INV]
- $\tfrac{15}{16}\lvert z\rvert\le\lvert h(z)\rvert\le\tfrac{17}{16}\lvert z\rvert$ on $\lvert z\rvert\le\tfrac1{10}$; $h^{-1}$ exists on $\lvert W\rvert\le\tfrac9{100}$.
- **Depends on:** DYAD-ALG-NF6, i.e. the exact $h$ through degree 6 and its coefficient-modulus majorant $M(s)$.
- **Verification:** as for PRIM-CTR.

`[ALG]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14, v6.4.15 entries | DYAD-ALG-OPEN3-PHASE-OFFSET] [scope: NF-REM rows, not mixed]
- P4-0: $\Psi_W(m)-\Psi_z(m)=\Delta_0(z_m)$ for every $m$, under the P4 lift tie $\Theta_W(0)=\Theta_z(0)+D_\Theta(z_0)$.
- $\Delta_1$ (chart-variable leading term), as quoted in §3(c).
- **Depends on:** DYAD-ALG-NF6, and the telescoping of $S_\Theta$ (DYAD-ALG-OPEN3-LEADING setting).
- **Verification:** reviewer (v6.4.16) and RECOG owner (v6.4.17).

`[ALG — formal second order; remainder not certified]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 806–809, v6.4.15 entry | DYAD-ALG-OPEN3-PHASE-OFFSET, primitive-variable form] (G2: owner qualifier carried verbatim)
- $M_W(W_0)=-\Delta_1(W_0)+Q_0[c_{\rm iso}+\Lambda_1(\Theta_{W_0})]+P_{W2}(W_0)+O(Q_0^{3/2})$, with $P_{W2}=-\Delta_2+D\Delta_1[h_2]$. This defines the expression $\mathcal P_2$ used in §3(c).
- **Grade boundary:** in this entry the $O(Q_0^{3/2})$ remainder is **not certified** and the entry is not a `[THM]`. The certified error bound is used only through DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (next import).
- **Depends on:** DYAD-ALG-NF6 ($h_2$, $h^{-1}=\mathrm{id}-h_2+O(\lvert W\rvert^3)$); RECOG-THM-R9-MEMORY ($c_{\rm iso}$, $\Lambda_1$).
- **Verification:** the reviewer checked the source against v6.4.18 (E2). The reviewer also confirmed $P_{W2}+\Delta_2-D\Delta_1[h_2]=0$ identically, by independent exact Laurent arithmetic.

`[THM]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14, v6.4.15 entries | DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS] [scope: NF-REM rows, not mixed]
- $\lvert\Delta_0\rvert\le K_0\sqrt q$, with $K_0=\tfrac{1101}{1000}$ (row A) and $\tfrac{533}{500}$ (row B).
- Not conditional on R9.
- **Depends on:** the DYAD-ART-OPEN3-P3 coefficient data and the exact-rational certificate DYAD-ART-OPEN3-P4.
- **Verification:** reviewer (v6.4.16) and RECOG owner (v6.4.17).

`[THM — conditional on RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 | DYAD-THM-OPEN3-ASYMPTOTIC-PHASE]
- T1 (limit equality) and T2 ($M_W-M=-\Delta_0(z_0)$), on orbits starting in a row disk.
- **Depends on:** RECOG-THM-R9-MEMORY, plus the two entries above.
- **Verification:** reviewer (v6.4.16) and RECOG owner (v6.4.17).

`[THM — conditional on RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 843–850 (SHA-256 `f70308f1…458d`) | DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER]
- Statement: $\lvert M_W-\mathcal P_2(W_0)\rvert\le K'_jQ_0^{3/2}+C_{2,j}(256/225)^2Q_0^2$, rows A and B, not mixed.
- Used only in block (c).
- **Depends on:** RECOG-THM-R9-MEMORY; DYAD-THM-OPEN3-ASYMPTOTIC-PHASE; DYAD-ART-OPEN21-P5.
- **Verification:** E2 PASS. The reviewer checked this independently against the v6.4.18 source (`941f42d6…126e`): statement, grade, constants, rows, chart disks, R9 condition and the comparator separation.
- **Not done:** the Dyadic 28-gate P5 certificate and RECOG's R9 Arb certificate were not rerun.
- **Provenance note:** the theorem first appeared in v6.4.17 (RECOG owner read, line 837). Identity of §6.14 between v6.4.17 and v6.4.18 is owner-reported. Not present in v6.4.16.

## 2. Typed interface and lemmas

`[DEF]` [RID: RECOG-DEF-A1A-PHASE-INTERFACE (proposed)] **A1a interface.** For $x_0\in U$, three objects are tied to the same orbit $x_m=T^{6m}x_0$:
- the **A1a extension of NUMGEN's defect formula**, $D_M^U:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$ for every $x_0\in U$. It uses the same formula as NUMGEN; RECOG-THM-A1A-LIFT-ALIGNMENT makes the increasing lift unambiguous on $U$. On $U\cap U_{\rm NUMGEN}$, $D_M^U=D_M$ (NUMGEN). This is a local definition extension: it extends no NUMGEN theorem and changes no source custody. NUMGEN's own $D_M$ is imported above and not re-owned;
- Dyadic's block phase $\Theta_W(m)$, built from principal per-block increments $\operatorname{Arg}(W_{m+1}/W_m)$ with the P4 lift tie;
- the normalized chart $z_m=h^{-1}(W_m)$.

Write $\Psi_W:=\Theta_W-\tau\log Q$. RECOG owns this typed join, not the three objects.

`[THM]` [RID: RECOG-THM-A1A-LIFT-ALIGNMENT (proposed)] [scope: conditional on postulated $T$; $U_T$ of DYAD-THM-PRIM-CTR] [proof: exact algebra + elementary enclosure]
- For every $x\in U_T$: $\tfrac\pi6<\delta_T(x)<\tfrac\pi2$.
- Hence, for $x_0\in U$ and every integer $M\ge1$: $D_M^U=\Theta_W(0)-\Theta_W(M)$.
- Depends on: DYAD-THM-PRIM-CTR (above).
- Proof: $W(Tx)=\lambda W+\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho)$ exactly, and $\lvert W(Tx)/(\lambda W)-1\rvert<\tfrac{143209}{750000}<\tfrac12$. Written out in the C4 Dyadic receipt §2 (`36e20687…ee91`).
- Check: `recog_a1a_c1_angle_bound_check.py` (`343d737e…65c7a`).

`[THM]` [RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE (proposed)] [scope: as above]
- For $x_0\in U$: $\lvert Q_{m+1}^{-1}-Q_m^{-1}-1\rvert<\tfrac{15}2\sqrt{Q_m}$, hence $Q_M^{-1}=Q_0^{-1}+M+O(\sqrt M)$ and $MQ_M\to1$.
- Depends on: DYAD-THM-PRIM-CTR. Proof: C4 Dyadic receipt §3.

`[ALG]` [internal lemma of this cell; no RID, not exported] [scope: $x_0\in U$, integer $M\ge1$] **Finite-block identity.**
$$D_M^U-\tau\log M=\tau\log Q_0-\bigl(\Psi_W(M)-\Psi_W(0)\bigr)-\tau\log(MQ_M).$$
Depends on: RECOG-THM-A1A-LIFT-ALIGNMENT.

## 3. Results

`[THM]` [RID: RECOG-THM-A1A-PHASE-EXISTENCE-ALT (proposed)] [assuming: H-NG] [scope: conditional on postulated $T$; $x_0\in U$]

**H-NG**: $\lim_M(D_M^U-\tau\log M)$ exists for the orbit of $x_0$.

If H-NG holds, then $\Psi_{W,\infty}$ and $\Psi_{z,\infty}$ exist and
$$\Psi_{z,\infty}=\Psi_{W,\infty}=\Theta_W(0)-\lim_M(D_M^U-\tau\log M);$$
with $M_W:=\Psi_{W,\infty}-\Psi_W(0)$, that limit equals $\tau\log Q_0-M_W$.

Depends on: the finite-block identity; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE; P4-0 and the offset bounds (row A: every $x_0\in U$ has $\lvert z_0\rvert\le\tfrac{16}{15}\cdot\tfrac1{25}=\tfrac{16}{375}<\tfrac1{20}$, and the row disks are forward-invariant); H-NG. The proof establishes H-NG ⇒ conclusion. R9 is not used.

`[RESULT]` `[from: ALG]` [RID: RECOG-RESULT-A1A-PHASE-EXISTENCE-NG (proposed)] [scope: $x_0\in U\cap U_{\rm NUMGEN}$; conditional on the selected continuous $T$ under OPEN-P0; $U_{\rm NUMGEN}$ has **no** explicit certified radius]

**(a)** On this domain, $\Psi_{z,\infty}=\Psi_{W,\infty}=\Theta_W(0)-C_D$ and $C_D=\tau\log Q_0-M_W$. **RECOG-THM-R9-MEMORY is not used.** This is existence only: no memory coefficients, no $C_2$, no remainder.

Depends on: RECOG-THM-A1A-PHASE-EXISTENCE-ALT, with H-NG discharged by NUMGEN INF-1 used as true (import above). On this domain $D_M^U=D_M$, so INF-1 applies directly.

`[THM]` [RID: RECOG-THM-A1A-CD-IDENTIFICATION (proposed)] [scope: conditional on postulated $T$; $x_0\in U$]

**(b)** For $x_0\in U$, $C_D^{\rm ext}(x_0):=\lim_M(D_M^U-\tau\log M)$ exists and
$$C_D^{\rm ext}=\tau\log Q_0-M_W=\tau\log q_0+D_\Theta(z_0)-M(z_0).$$

Depends on:
- RECOG-THM-R9-MEMORY: RECOG's own adopted `[THM]`, §6.13a, row A, $q_0\le\tfrac1{400}$ since $\lvert z_0\rvert\le\tfrac{16}{375}$;
- Dyadic T1 and T2 (imports), whose R9 premise is discharged here by RECOG R9;
- the finite-block identity; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE.

*Dependency guard.* The older Dyadic results NF6, PRIM-CTR and NF-REM feed RECOG R9. RECOG R9 feeds the later Dyadic T1/T2/OPEN 21, which feed A1a (b)/(c). No A1a claim is used to establish R9.

`[RESULT]` `[from: ALG]` [RID: RECOG-RESULT-A1A-CD-AGREEMENT (proposed)] [scope: $x_0\in U\cap U_{\rm NUMGEN}$; conditional on the selected $T$ under OPEN-P0]

**(b′)** $C_D^{\rm ext}(x_0)=C_D(x_0)$, NUMGEN's constant.

Depends on: RECOG-THM-A1A-CD-IDENTIFICATION and NUMGEN INF-1 (import, used as true). On the overlap $D_M^U=D_M$, so both are limits of the same sequence.

`[THM]` [RID: RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (proposed)] [scope: conditional on postulated $T$; rows not mixed] (E2 source check PASS on v6.4.18, §4)

**(c)** Let
$$\mathcal P_2(W_0):=-\Delta_1(W_0)+Q_0\bigl[c_{\rm iso}+\Lambda_1(\Theta_{W_0})\bigr]+P_{W2}(W_0),$$
the owner's second-order form, where:
- the form is defined in DYAD-ALG-OPEN3-PHASE-OFFSET, v6.4.18 §6.14 lines 806–809, `[ALG — formal second order; remainder not certified]`;
- it is certified only through DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, v6.4.18 §6.14 lines 843–850;
- $W_0=\lvert W_0\rvert e^{i\Theta_{W_0}}$ in the primitive frame $W=\rho-\eta/2+i\tfrac{\sqrt3}2\eta$, and $Q_0=\lvert W_0\rvert^2$;
- $\Delta_1(W)=\lvert W\rvert\bigl[\tfrac{17\sqrt3}{36}\cos\Theta-\tfrac1{12}\sin\Theta-\tfrac{7\sqrt3}{72}\cos3\Theta+\tfrac18\sin3\Theta\bigr]$, evaluated at $W_0$ (DYAD-ALG-OPEN3-PHASE-OFFSET, v6.4.18 §6.14 lines 806–809);
- $P_{W2}(W)=-\Delta_2(W)+D\Delta_1(W)[h_2(W)]=\lvert W\rvert^2\bigl[-\tfrac{5\sqrt3}{27}+\tfrac{47\sqrt3}{1296}\cos2\Theta-\tfrac{19}{432}\sin2\Theta-\tfrac{11\sqrt3}{324}\cos4\Theta+\tfrac1{54}\sin4\Theta-\tfrac{\sqrt3}{1728}\cos6\Theta-\tfrac5{576}\sin6\Theta\bigr]$ (same entry; the identity was rechecked in E2);
- $c_{\rm iso}=-\tfrac{4\sqrt3}{27}$ and $\Lambda_1(\Theta)=\tfrac{43\sin6\Theta-5611\sqrt3\cos6\Theta}{1270080}$ (RECOG-THM-R9-MEMORY, RECOG v0.3.21 §6.13a).

Then
$$C_D^{\rm ext}=\tau\log Q_0-\mathcal P_2(W_0)+E,\qquad\lvert E\rvert\le K'_jQ_0^{3/2}+C_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2,$$
on two row domains, which are not to be mixed:

| Row | Start domain here | Owner primitive domain $w_j$ | Chart disk | $K'_j$ | $C_{2,j}$ |
|---|---|---|---|---|---|
| A | $0<\lvert W_0\rvert\le\tfrac1{25}$ | $\tfrac3{64}$ | $\lvert z\rvert\le\tfrac1{20}$ | $\tfrac{3951}{1000}$ | 517 |
| B | $0<\lvert W_0\rvert\le\tfrac3{128}$ | $\tfrac3{128}$ | $\lvert z\rvert\le\tfrac1{40}$ | $\tfrac{971}{250}$ | 163 |

- **Chart inclusions:** $\tfrac{16}{15}\cdot\tfrac1{25}=\tfrac{16}{375}<\tfrac1{20}$, and $\tfrac{16}{15}\cdot\tfrac3{128}=\tfrac1{40}$.
- **Row A** is cut to $U$ because (b) needs the starting point in $U$.
- **Depends on:** RECOG-THM-A1A-CD-IDENTIFICATION; DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (import), whose R9 premise is discharged by RECOG R9. Its $C_{2,j}$ are R9's row constants.

`[NUM]` [scope: illustration; not a proof input, not a domain certificate] Twelve float64 orbits in row A, run for 16,000 blocks:
- the alignment identity holds to $2.4\times10^{-9}$;
- $(\hat C-[\tau\log Q_0-\mathcal P_2])/Q_0^{3/2}\in[-0.28,0.35]$.

Artifact: `recog_a1a_cd_identity_num.py` (`efccd210…791b`) and its JSON (`09136040…740`).

## 4. E2 — source gate for block (c)

**PASS — source-statement fidelity, against adopted Dyadic v6.4.18.**

Record: `RECOG_A1A_E2_OPEN21_SOURCE_CHECK_v6_4_18_20261020.md`, `941f42d6273f707bb161c24bd7e753c12acacda991dd29ff4050cbdcbfa6126e`. Inspected source: `RTG_DYADIC_OSCILLATOR_DSN_v6_4_18.md`, SHA-256 `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d`, rehashed by the reviewer.

| Check | Owner location (v6.4.18 §6.14) | Result |
|---|---|---|
| Primitive-variable form, grade qualifier, $P_{W2}=-\Delta_2+D\Delta_1[h_2]$ | lines 806–809 | PASS; the identity was recomputed independently in exact Laurent arithmetic |
| OPEN 21 statement and grade `[THM — conditional on R9]` | lines 843–850 | PASS |
| $K'_A=\tfrac{3951}{1000}$, $K'_B=\tfrac{971}{250}$; $C_{2,A}=517$, $C_{2,B}=163$; factor $(\tfrac{256}{225})^2$ | lines 846–849 | PASS |
| Rows A and B, chart disks, not mixed; A1a's narrowed domains ($\tfrac{16}{375}<\tfrac1{20}$, $\tfrac{16}{15}\cdot\tfrac3{128}=\tfrac1{40}$) | lines 846–849 | PASS: no widening |
| R9 condition; no transfer to the comparator $C_W^{(h)}$ | lines 843–850 | PASS |

**Evidence limits:**
- Neither the Dyadic P5 28-gate certificate nor RECOG's R9 Arb certificate was rerun.
- v6.4.17 was not byte-compared, so the v6.4.17 line-837 pin is **not** described as independently verified. Its §6.14 identity to v6.4.18 is owner-reported.
- E2 does not decide release readiness and registers no RID.

Block (c) no longer carries the PROVISIONAL label. Blocks (a), (b) and (b′) did not depend on E2.

## 5. Governance and scope

- **C1 provenance.** Dyadic's reported "C1 CERTIFIED — C4 CONDITIONAL COROLLARY ACCEPTED" is a **review acceptance**. It is not a Dyadic owner adoption or release, and no Dyadic RID is created. Its archived record identity is to be added when the PI files the original Dyadic C4 reply.
- **No widening.** No Dyadic certified domain is widened, no Dyadic conditional grade is changed, and NUMGEN INF-1 gains no explicit radius.
- **Nothing transferred.** Nothing goes to the comparator $C_W^{(h)}$ or to the R9 $C_z$ incompleteness corollary. $C_D$ depends on the start state.
- **Separation.** A1a ⇏ A1b ⇏ A1c. No physical event is defined. R6 stays ACTIVE.
- **Optional strengthening (not made).** On $U$, H-NG and the convergence of $\Psi_W$ are *equivalent*, because $\log(MQ_M)\to0$. The one-way statement is kept.

## 6. Changes from v0.1

| Item | Change |
|---|---|
| R1 | $D_M$ is now an **import** of NUMGEN's definition (`RID unavailable`, quoted verbatim). The proposed RECOG RID is moved to the typed join `RECOG-DEF-A1A-PHASE-INTERFACE`, and RECOG-DEF-A1A-PHASE-DEFECT is dropped. |
| R2 | (b) is split: the existence and identification on $U$ (`[THM]`, R9) stay in (b); agreement with NUMGEN's $C_D$ on the overlap becomes (b′), `[RESULT] [from: ALG]`, with INF-1 provenance. |
| R3 | (c) now states $\mathcal P_2$, $\Delta_1$, $P_{W2}$, $c_{\rm iso}$ and $\Lambda_1$ explicitly, with source lines, the frame, both rows and the chart inclusions. |
| R4 | The imports now follow §3.3 at point of use (version, RID or `RID unavailable`, scope, Depends on). The module RID is not used as a theorem RID. The finite-block identity is marked an internal lemma with no RID. |
| R5 | (a) carries "conditional on the selected continuous $T$ under OPEN-P0" and "no explicit certified radius" in its claim line. |
| Other | C1 is marked as a review acceptance, not an owner adoption. E2 is given as its own section with exact source locations. The optional equivalence is noted but not made. |

**v0.2 → v0.3 (review of v0.2, P1–P2; record corrections only, no statement or grade change):**

| Item | Change |
|---|---|
| P1 | The A1a definition extension $D_M^U$ on $U$ is declared in §2, with $D_M^U=D_M$ on $U\cap U_{\rm NUMGEN}$ and no extension of any NUMGEN theorem. $D_M^U$ is used in the lift lemma, the finite-block identity, H-NG and (b). (a) and (b′) note that $D_M^U=D_M$ on the overlap. |
| P2 | Every `[import: same …]` is replaced by its full edition, section and RID. Each Dyadic import is pinned to v6.4.16, the reviewer-inspected and release-verified source; only OPEN 21 is pinned to v6.4.17. Each import has its own `Depends on:` and `Verification:` lines. The two NUMGEN imports carry `RID unavailable` with a governance disposition (no new owner RID requested) and local tracking keys. v6.4.17 is described as RECOG-owner read only. |

**v0.3 → v0.4 (maintenance; no statement or grade change):**

| Item | Change |
|---|---|
| G1 | Both NUMGEN `RID unavailable` imports are labelled a **deferred governance decision, with no method exception claimed**. The import satisfies §3.3 through its `RID unavailable` form, and it will be repinned if NUMGEN registers a RID later. Tracking keys are unchanged. |
| G2 | The primitive-variable second-order form ($\mathcal P_2$, $P_{W2}=-\Delta_2+D\Delta_1[h_2]$) gets its own import line. That line carries the owner qualifier `[ALG — formal second order; remainder not certified]` verbatim. The certified error bound is taken only from the OPEN 21 import. |
| E2 | The OPEN 21 import and the (c) source references are repinned to adopted v6.4.18 §6.14 (`f70308f1…458d`): lines 806–809 for the primitive form and lines 843–850 for the theorem and its rows. The E2 PASS record (`941f42d6…126e`) is cited. The PROVISIONAL label on (c) is removed. v6.4.17 stays a provenance note marked owner-reported. §4 is rewritten as a PASS record with its evidence limits. |
