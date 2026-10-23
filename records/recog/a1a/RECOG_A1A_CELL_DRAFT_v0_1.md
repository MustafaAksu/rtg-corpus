# RECOG A1a — Scientific Cell Draft v0.1: $C_D$ identification and an alternative existence route for the asymptotic phase

**Date:** 20 October 2026
**Status:** `[SESSION]` cell **draft** for a future, separately reviewed RECOG release (e.g. v0.3.22).
- Nothing here is adopted, and no RID is registered. RIDs below are *proposed* RECOG identifiers, which the owner may propose.
- RECOG v0.3.21 is unchanged, and R6 stays ACTIVE.

**Basis:**
- accepted session record A1a v0.3 (`e542d1051babcc0375a89fbe254b98e41a87b159dc8a6301bfbe824cd8828de0`);
- its review `RECOG_A1A_SESSION_v0_3_RECEIVING_REVIEW_20261020.md` (`5ccf9098ebfed06fd0bb0a98155d96ef4df217a8dc09ad5b348fef0db938f994`), which accepted it with notes E1 and E2.

**Grammar:** DSN Methodology v1.3 (§3.3 imports, §3.4 `[RESULT]` pairing and conditional proofs).

## 0. Correction to v0.3 on grades (review note E1)

`[COR]` **Old statement.** A1a v0.3 §6 said the DSN grade of the corollary "would be `[RESULT] [from: ALG]`-level" by a "weaker-input rule".

**Reason it is wrong.** Methodology v1.3 §3.4 applies the weakest-undischarged-premise rule only to an *unconditional* conclusion that uses its premises as true. A completely proved implication keeps its own grade, with its hypotheses explicit (M13-C04).

**New statement.** The result is split below into:
- a conditional theorem, graded `[THM] [assuming: H-NG]`;
- an unconditional application using NUMGEN INF-1 as true, graded `[RESULT] [from: …]` with that grade chosen for the actual assertion.

The accepted v0.3 record is not edited; this draft supersedes its grade note.

## 1. Imports used (to enter §7 of the release)

| Import | Source, version | Owner grade as registered | Used for |
|---|---|---|---|
| DYAD-THM-PRIM-CTR | Dyadic §6.14 (v6.4.16 release-verified; byte-identical through v6.4.18 per owner) | `[THM]` | tube $U_T\subset\{\lvert W\rvert<\tfrac{47}{1000}\}$; radial bounds |
| DYAD-THM-NF-INV | same | `[THM]` | $\lvert z\rvert\le\tfrac{16}{15}\lvert W\rvert$ |
| DYAD-ALG-OPEN3-PHASE-OFFSET (P4-0), DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS | same, v6.4.15 onward | `[ALG]`, `[THM]` | $\Psi_W-\Psi_z=\Delta_0(z_m)$, $\lvert\Delta_0\rvert\le K_0\sqrt q$ |
| DYAD-THM-OPEN3-ASYMPTOTIC-PHASE (T1, T2) | same | `[THM — conditional on RECOG-THM-R9-MEMORY]` | statement (b) |
| DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER | Dyadic v6.4.17 §6.14, line 837 | `[THM — conditional on RECOG-THM-R9-MEMORY]` | statement (c) |
| NUMGEN INF-1 (N-5A-S1-INF; RID unavailable for the INF-1 statement itself; module `NUMGEN-OPEN-N5AS1-INF`) | Number Genesis v1.20.7 §6.6 | `[RESULT] [from: ALG]` | statement (a), application |

## 2. Claim blocks (proposed)

`[DEF]` [RID: RECOG-DEF-A1A-PHASE-DEFECT (proposed)] For a start $x_0$:
- **Phase defect** (NUMGEN's definition, adopted verbatim): $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$, where $\hat\phi$ is the increasing lift of $\arg W$ along primitive steps and $W=\rho+\omega\eta$.
- **Block phase** (Dyadic P4): $\Theta_W(M)$, from principal per-block increments $\operatorname{Arg}(W_{m+1}/W_m)$.
- $\Psi_W:=\Theta_W-\tau\log Q$.

`[THM]` [RID: RECOG-THM-A1A-LIFT-ALIGNMENT (proposed)] [scope: conditional on postulated $T$; primitive tube $U_T$ of DYAD-THM-PRIM-CTR] [proof: exact algebra + elementary enclosure]
- For every $x\in U_T$: $\tfrac\pi6<\delta_T(x)<\tfrac\pi2$.
- Hence, for every $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$ and every integer $M\ge1$, $D_M=\Theta_W(0)-\Theta_W(M)$ exactly.

Depends on: DYAD-THM-PRIM-CTR (import). Proof: A1a v0.2 §3.1, and the C4 Dyadic receipt §2 (`36e20687…ee91`). Check: `recog_a1a_c1_angle_bound_check.py` (`343d737e…65c7a`), G1–G6 PASS, 3 negative controls caught; G6 is a `[NUM]` dense check of two elementary inequalities whose proof is written out.

`[THM]` [RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE (proposed)] [scope: as above]
- For $x_0\in U$: $Q_M^{-1}=Q_0^{-1}+M+O(\sqrt M)$, hence $MQ_M\to1$.
- Per block, $\lvert Q_{m+1}^{-1}-Q_m^{-1}-1\rvert<\tfrac{15}2\sqrt{Q_m}$.

Depends on: DYAD-THM-PRIM-CTR (import). Proof: C4 Dyadic receipt §3.

`[ALG]` [scope: $x_0\in U$, $M\ge1$] Finite-block identity:
$$D_M-\tau\log M=\tau\log Q_0-\bigl(\Psi_W(M)-\Psi_W(0)\bigr)-\tau\log(MQ_M).$$
Depends on: RECOG-THM-A1A-LIFT-ALIGNMENT.

`[THM]` [RID: RECOG-THM-A1A-PHASE-EXISTENCE-ALT (proposed)] [assuming: H-NG] [scope: conditional on postulated $T$; starts $x_0\in U$]

**H-NG** is the hypothesis that $D_M-\tau\log M$ converges as $M\to\infty$ for the orbit of $x_0$.

Statement: if H-NG holds for $x_0$, then $\Psi_{W,\infty}$ and $\Psi_{z,\infty}$ exist and
$$\Psi_{z,\infty}=\Psi_{W,\infty}=\Theta_W(0)-\lim_M(D_M-\tau\log M).$$
Writing $M_W:=\Psi_{W,\infty}-\Psi_W(0)$, the limit equals $\tau\log Q_0-M_W$.

Depends on: the identity above, RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, DYAD P4-0 and the offset bounds (imports), and H-NG. The proof establishes H-NG ⇒ conclusion, not H-NG.

`[RESULT]` `[from: ALG]` [RID: RECOG-RESULT-A1A-PHASE-EXISTENCE-NG (proposed)] [scope: $x_0\in U\cap U_{\rm NUMGEN}$, where $U_{\rm NUMGEN}$ is INF-1's tube, which exists but has no stated radius]

Statement (a): on this domain, $\Psi_{z,\infty}=\Psi_{W,\infty}=\Theta_W(0)-C_D$ and $C_D=\tau\log Q_0-M_W$. **RECOG-THM-R9-MEMORY is not used.**

Depends on: RECOG-THM-A1A-PHASE-EXISTENCE-ALT, plus NUMGEN INF-1 used as true (import; owner grade `[RESULT] [from: ALG]`; NUMGEN confirmed it is independent of R9 and works from an arbitrary start).

*Tag choice.* The assertion uses an imported `[RESULT] [from: ALG]` premise as true, so `[from: ALG]` is proposed. It is to be confirmed at release review. This is an existence statement only.

`[THM]` [RID: RECOG-THM-A1A-CD-IDENTIFICATION (proposed)] [scope: conditional on postulated $T$; starts $x_0\in U$; R9 chart and rows]

Statement (b): for $x_0\in U$, the limit $C_D^{\rm ext}(x_0):=\lim_M(D_M-\tau\log M)$ exists and
$$C_D^{\rm ext}=\tau\log Q_0-M_W=\tau\log q_0+D_\Theta(z_0)-M(z_0).$$
On $U\cap U_{\rm NUMGEN}$ it equals NUMGEN's $C_D$.

Depends on: RECOG-THM-R9-MEMORY (**RECOG's own adopted `[THM]`**, §6.13a); Dyadic T1 and T2 (imports, conditional on that same R9); the identity above; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE. Every start in $U$ satisfies $\lvert z_0\rvert\le\tfrac{16}{375}<\tfrac1{20}$, so it lies in row A.

*Custody note.* Dyadic's "conditional on R9" is discharged inside RECOG by RECOG's own R9. That is why this block is `[THM]` and not `[THM — conditional]`. The evidence runs one way only: RECOG R9 → Dyadic T1/T2 → this block. Nothing here strengthens R9; this is the mutual-citation guard.

`[THM]` [RID: RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (proposed)] [scope: conditional on postulated $T$; rows not mixed]

Statement (c): for $0<\lvert W_0\rvert\le\tfrac1{25}$ (row A) and for $0<\lvert W_0\rvert\le\tfrac3{128}$ (row B),
$$C_D^{\rm ext}=\tau\log Q_0-\mathcal P_2(W_0)+E,\qquad\lvert E\rvert\le K'_jQ_0^{3/2}+C_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2,$$
where
- row A: $K'_A=\tfrac{3951}{1000}$, $C_{2,A}=517$;
- row B: $K'_B=\tfrac{971}{250}$, $C_{2,B}=163$.

Depends on: RECOG-THM-A1A-CD-IDENTIFICATION; DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (import; conditional on R9, discharged by RECOG R9 as above; constants are $C_2$ of R9).

**Release precondition (E2):** an independent source check of v6.4.17 lines 837–843.

`[NUM]` [scope: illustration] Twelve float64 primitive orbits in row A, run for 16,000 blocks:
- the alignment identity holds to $2.4\times10^{-9}$;
- the scaled error $(\hat C-[\tau\log Q_0-\mathcal P_2])/Q_0^{3/2}$ lies in $[-0.28,0.35]$.

Artifact: `recog_a1a_cd_identity_num.py` (`efccd210…791b`) and its JSON (`09136040…740`); byte-reproduced by the reviewer.

## 3. Scope guards for the cell

- Statement (a) is the **only** statement without R9, and only on the existential intersection. It is existence only: no memory coefficients, no $C_2$, no remainder.
- Statements (b) and (c) rest on R9. Nothing in this cell widens Dyadic's certified domains or regrades its T1/T2/OPEN 21. Nothing transfers to the comparator $C_W^{(h)}$ or to the R9 $C_z$ incompleteness corollary.
- $C_D$ depends on the start state; it is not universal.
- Separation: A1a ⇏ A1b token schedule ⇏ A1c recoverability. No physical event is defined, and R6 stays ACTIVE.
- Owner custody:
  - NUMGEN's INF-1 is unchanged. NUMGEN prefers at most a later provenance pointer.
  - Dyadic's response was a conditional *session* acceptance of an existence-only corollary. That is not an owner decision on C1. Any later `C1 CERTIFIED` record must be registered with its identity, stating whether it is a review or an owner decision (E2).

## 4. Before this enters a release

1. A receiving review of this draft. It should cover the grade choices of §2, in particular `[THM]` for (b) and (c) given RECOG's own R9, and `[from: ALG]` for (a).
2. The E2 source check of the OPEN 21 constants (v6.4.17 lines 837–843).
3. Recording Dyadic's position on the C1 derivation, and saying whether it comes from a review or the owner.
4. A PI decision to include the cell in a RECOG release. That release would also update the §7.2 N13 row to "release verification reported passed (owner-reported)".
