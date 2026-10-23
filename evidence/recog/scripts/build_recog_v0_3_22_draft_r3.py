#!/usr/bin/env python3
"""build_recog_v0_3_22_draft_r3.py -- deterministic build of RECOG v0.3.22 DRAFT r3 (A1a scientific cell).

r3 = r2 plus the A1a-G1 disposition (NUMGEN reply v0.1 184a74fc...5227 choosing option 1; NUMGEN co-owner ruling of
20 Oct 2026 approving the six RID allocations; record RECOG_A1A_G1_DISPOSITION_RECORD_20261020.md 0e5f91c0...71a7)
and the two nonblocking notes of the r2 review (fee7e519...0efe): N1 revision-neutral N13 label; N2 checker help text.
Approved NUMGEN strings are NOT written into any [RID: ...] field before NUMGEN v1.20.8 adoption.

r2 = r1 plus the limited corrections of the integrated receiving review of DRAFT r1
(RECOG_v0_3_22_DRAFT_r1_INTEGRATED_RECEIVING_REVIEW_20261020.md, c1d49013...8d17): L1 (header typing: D_M^U),
L2 (RID request prepared, not yet dispatched), optional historical-header label and package-locator note.
Same adopted base; the r1 builder is retained unchanged.

Basis: A1a cell draft v0.4 (sha256 117584032f85ed89b404931ccdba1d5abf9c66e0740833dfe2fdbe129f50f4f7), accepted by the
independent release-readiness review RECOG_A1A_CELL_DRAFT_v0_4_RELEASE_READINESS_REVIEW_20261020.md
(d195af7aa5453d7392bfbb9f56fafb33cf8a391bf036935c7af56c15f8445274): integration authorized for preparation; not adopted.

Input : RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md (ADOPTED, sha256 a3459522...0ae3); refuses any other bytes.
Output: RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22_DRAFT_r3.md and recog_v0_3_22_edits_r3.json.
Every edit is an exact-once replacement (old -> new); a missing or repeated anchor aborts the build.
New science enters only in edit S1 (new §6.13b) and its summaries (A1, R1); no existing scientific statement, RID,
grade or OPEN status is edited -- see check_recog_v0_3_22_draft.py (reverse-application gate).
Usage: python build_recog_v0_3_22_draft_r3.py BASE.md [OUT_DIR]
"""
import sys, os, json, hashlib

BASE_SHA = "a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3"

SCI_RIDS = ["RECOG-DEF-A1A-PHASE-INTERFACE", "RECOG-THM-A1A-LIFT-ALIGNMENT", "RECOG-THM-A1A-RECIPROCAL-AMPLITUDE",
            "RECOG-THM-A1A-PHASE-EXISTENCE-ALT", "RECOG-RESULT-A1A-PHASE-EXISTENCE-NG", "RECOG-THM-A1A-CD-IDENTIFICATION",
            "RECOG-RESULT-A1A-CD-AGREEMENT", "RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION"]
ART_RIDS = ["RECOG-ART-A1A-C1-CHECK", "RECOG-ART-A1A-NUM", "RECOG-ART-A1A-RECORDS", "RECOG-ART-A1A-SOURCE-AND-GOVERNANCE"]

E = []
def edit(eid, purpose, old, new, allowed_new_tags=(), allowed_new_rids=()):
    E.append({"id": eid, "purpose": purpose, "old": old, "new": new,
              "allowed_new_tags": list(allowed_new_tags), "allowed_new_rids": list(allowed_new_rids)})

# ---------------------------------------------------------------- header
edit("H1", "title",
 "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21\n",
 "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22 (DRAFT r3)\n")
edit("H2", "date",
 "**Date:** 20 October 2026 (v0.3.21 — synchronization release, no new mathematics; adopted 20 Oct 2026)\n",
 "**Date:** 20 October 2026 (v0.3.22 DRAFT r3 — A1a scientific cell: asymptotic phase and the Number Genesis constant $C_D$; not adopted)\n")
edit("H3", "supersedes",
 "**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20` (frozen 19 Oct 2026, sha256 `fdb8c9a7…b8df`; external record `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`)",
 "**Supersedes (on adoption):** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21` (adopted 20 Oct 2026, sha256 `a3459522…0ae3`; release record `RECOG_v0_3_21_RELEASE_RECORD.md`) · v0.3.20 (frozen 19 Oct 2026, sha256 `fdb8c9a7…b8df`; external record `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`)")
edit("H4", "companion pins: Dyadic editions used by A1a; v6.4.17 pending note labelled as v0.3.21 historical state",
 "— Dyadic release verification of v6.4.17 pending — and v6.4.16 `33c14c5c…59e0` as last verified, §7.2)",
 "— v0.3.21 historical state: Dyadic release verification of v6.4.17 pending; current receipt state in §7.2 N13 — and v6.4.16 `33c14c5c…59e0` as last verified, §7.2; the A1a cell §6.13b pins its Dyadic imports to v6.4.16 and, for OPEN 21 and the primitive-variable form, to adopted v6.4.18 `f70308f1…458d`, source-checked for that use)")
edit("H5", "companion pins: NUMGEN items used by A1a",
 "`RTG_NUMBER_GENESIS_DSN_v1.20.7` (sha256 `c4637e7a…ab28`; claim-level synchronized v0.3.18, §7.1)",
 "`RTG_NUMBER_GENESIS_DSN_v1.20.7` (sha256 `c4637e7a…ab28`; claim-level synchronized v0.3.18, §7.1; the $D_M$ definition and INF-1 are imported by §6.13b as `RID unavailable`; dedicated RID decided by the NUMGEN owner (reply v0.1 `184a74fc…5227`; co-owner ruling of 20 Oct 2026 approving the allocation); string to be fixed in NUMGEN v1.20.8; responsible owner NUMGEN; A1a-G1 allocation resolved, canonical repin pending NUMGEN v1.20.8)")
edit("H6", "status summary v0.3.22 DRAFT r1 (new paragraph above the v0.3.21 summary)",
 "**Status summary (v0.3.21):**",
 r"**Status summary (v0.3.22 DRAFT r3):** One new scientific cell, §6.13b (A1a), with eight proposed RIDs (registered only on adoption) and four artifact IDs (§8). On the explicit start set $U=\{0<Q_0\le\tfrac1{625}\}$, A1a's local extension $D_M^U$ of the Number Genesis defect formula aligns exactly with Dyadic's block phase, and $MQ_M\to1$; on the intersection with NUMGEN's existential tube $U_{\rm NUMGEN}$, $D_M^U$ equals NUMGEN's $D_M$. Hence: the limit $C_D^{\rm ext}=\lim_M(D_M^U-\tau\log M)$ exists and equals $\tau\log Q_0-M_W$ (`[THM]`, using RECOG's own R9 through Dyadic T1/T2); on $U\cap U_{\rm NUMGEN}$ it equals NUMGEN's $C_D$, and the asymptotic phase exists **without R9** (existence only, `[RESULT] [from: ALG]`, no explicit radius); quantitatively $C_D^{\rm ext}=\tau\log Q_0-\mathcal P_2(W_0)+E$ per Dyadic OPEN 21 row (`[THM]`). No existing scientific RID, grade or OPEN status changes; R6 stays ACTIVE. §7 gains the A1a import rows and a scope note on the NUMGEN defect-threshold row; §7.2 N13 is updated in three separate fields. **Release state:** integrated review of DRAFT r2 accepted (L1/L2 closed); A1a-G1 allocation resolved by the NUMGEN owner (option 1; co-owner ruling of 20 Oct 2026), canonical repin of the two NUMGEN imports pending NUMGEN v1.20.8; PI adoption pending."
 "\n\n**Status summary (v0.3.21):**",
 allowed_new_tags=["[THM]", "[RESULT]"])
edit("H7", "freeze status",
 "**Freeze status:** v0.3.21 adopted 20 Oct 2026",
 "**Freeze status:** v0.3.22 DRAFT r3 (not adopted; v0.3.21 remains the authoritative edition until adoption). *Earlier:* v0.3.21 adopted 20 Oct 2026")

# ---------------------------------------------------------------- §1 summary line
edit("A1", "§1: A1a summary paragraph",
 "**$h$-chart ledger (R11, v0.3.2).**",
 r"**Asymptotic phase and the Number Genesis constant $C_D$ (A1a, v0.3.22).** `[THM]` [RID: RECOG-THM-A1A-CD-IDENTIFICATION] [scope: conditional on postulated $T$; starts $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$] $C_D^{\rm ext}(x_0)=\lim_M(D_M^U-\tau\log M)$ exists and $C_D^{\rm ext}=\tau\log Q_0-M_W=\tau\log q_0+D_\Theta(z_0)-M(z_0)$, via RECOG-THM-R9-MEMORY and Dyadic T1/T2. `[RESULT]` `[from: ALG]` On $U\cap U_{\rm NUMGEN}$ (no explicit radius) it equals NUMGEN's $C_D$, and the asymptotic phase exists without R9 (existence only). $C_D$ depends on the start state. Quantitative per-row form, scope and imports: §6.13b."
 "\n\n**$h$-chart ledger (R11, v0.3.2).**",
 allowed_new_tags=["[THM]", "[RESULT]"], allowed_new_rids=["RECOG-THM-A1A-CD-IDENTIFICATION"])

# ---------------------------------------------------------------- §5 row
edit("R1", "§5: high-risk row for A1a",
 r"applying the theorem directly in the raw $C_W^{(h)}$ track | §6.13a, SG-R14 |" "\n",
 r"applying the theorem directly in the raw $C_W^{(h)}$ track | §6.13a, SG-R14 |" "\n"
 r"| $C_D$ identification (A1a) | RECOG-THM-A1A-CD-IDENTIFICATION `[THM]` on the explicit $U$, using R9; R9-free existence (RECOG-RESULT-A1A-PHASE-EXISTENCE-NG) and agreement with NUMGEN's $C_D$ (RECOG-RESULT-A1A-CD-AGREEMENT) only on $U\cap U_{\rm NUMGEN}$; per-row quantitative form with the Dyadic OPEN 21 constants, rows not mixed | a universal, start-independent $C_D$; an explicit radius for the R9-free route; R9-free memory coefficients, $C_2$ or remainders; widening a Dyadic certified domain or regrading T1/T2/OPEN 21; transfer to $C_W^{(h)}$, the R9 incompleteness corollary, a token schedule or event recovery | §6.13b |" "\n",
 allowed_new_tags=["[THM]"],
 allowed_new_rids=[])

# ---------------------------------------------------------------- §6.13b (new science)
S613B = r"""#### §6.13b A1a — Asymptotic phase and the Number Genesis constant $C_D$ `[THM / RESULT]` {#sec-6-13b-a1a}

> **[SG-R13, SG-R14 apply]** Primitive frame $W=\rho-\eta/2+i\tfrac{\sqrt3}2\eta$ ($=\rho+\omega\eta$), $Q=\lvert W\rvert^2$; normalized chart $z=h^{-1}(W)$ of DYAD-ALG-NF6, $q=\lvert z\rvert^2$; R9 objects of §6.13a ($\Psi$, $M$, $\Lambda_1$, $c_{\rm iso}$, rows) on the $C_z$ track. All statements are conditional on the postulated $T$ (programme OPEN-P0). **RIDs in this subsection are proposed and are registered only on adoption of this release.**

**Grade principle.** Methodology v1.3 §3.4 (M13-C04): a fully proved implication keeps its own grade with its hypotheses explicit; the weakest-premise rule applies only to an unconditional conclusion that uses its premises as true. Dyadic T1/T2 and OPEN 21 remain conditional in their own owner record; their R9 premise is discharged here by RECOG's own adopted R9.

**Imports at point of use** (Methodology §3.3; also listed in §7).

`[DEF]` [import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6 N-5A-S1-INF, $D_M$ definition | RID unavailable] $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$, quoted verbatim; $\hat\phi_n$ is the increasing lift of $\arg W$ along primitive steps from an arbitrary start $x_0$ on NUMGEN's tube $U_{\rm NUMGEN}$. *Owner RID:* none in the inspected source (v1.20.7); dedicated RID decided by the NUMGEN owner (reply v0.1 `184a74fc…5227`; co-owner ruling of 20 Oct 2026 approving the allocation); string to be fixed in NUMGEN v1.20.8; responsible owner NUMGEN; A1a-G1 allocation resolved, canonical repin pending NUMGEN v1.20.8 (request `RECOG_TO_NUMGEN_A1A_RID_REQUEST_20261020.md`; disposition `RECOG_A1A_G1_DISPOSITION_RECORD_20261020.md`). Methodology §3.3 temporary `RID unavailable` until the NUMGEN v1.20.8 owner edition; governance disposition recorded. No allocated string is cited as an owner RID before that edition. The module RID `NUMGEN-OPEN-N5AS1-INF` is not a theorem RID and is not used as one. Tracking key `A1A-NG-D-DEF`.

`[RESULT]` `[from: ALG]` [import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6, INF-1 | RID unavailable] [scope: $U_{\rm NUMGEN}$, which exists but has no stated radius] $D_M=\tau\log M+C_D+o(1)$, with $C_D$ depending on $x_0$. Depends on: NUMGEN L1, L-BACKBONE, L-MONO, L-PHASE; not on RECOG R9 (NUMGEN C4 reply `8a887ef3…bc4d`). Owner RID and governance as above (A1a-G1). `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` is the RID of the ratio theorem that uses INF-1, not of INF-1 (§7 scope note). Tracking key `A1A-NG-INF1`.

`[THM]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 | DYAD-THM-PRIM-CTR, DYAD-THM-NF-INV] Primitive contraction on $0<Q\le\tfrac1{400}$ with $\lvert P_5\rvert\le\tfrac{16931}{10000}Q^{5/2}$, $\lvert R^{\rm prim}_{\ge6,\rm rad}\rvert\le108Q^3$; tube $U_T=\bigcup_{j<6}T^j(U)\subset\{\lvert W\rvert<\tfrac{47}{1000}\}$, $T(U_T)\subseteq U_T$; $Q_m\le Q_0/(1+\tfrac12Q_0m)$; $\tfrac{15}{16}\lvert z\rvert\le\lvert h(z)\rvert\le\tfrac{17}{16}\lvert z\rvert$ on $\lvert z\rvert\le\tfrac1{10}$. Statements unchanged since v6.4.10 (§7 rows).

`[ALG]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14, v6.4.15 entries | DYAD-ALG-OPEN3-PHASE-OFFSET] P4-0: $\Psi_W(m)-\Psi_z(m)=\Delta_0(z_m)$ for every $m$, under the lift tie $\Theta_W(0)=\Theta_z(0)+D_\Theta(z_0)$; leading term $\Delta_1$.

`[ALG — formal second order; remainder not certified]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 806–809 | DYAD-ALG-OPEN3-PHASE-OFFSET, primitive-variable form] $M_W(W_0)=\mathcal P_2(W_0)+O(Q_0^{3/2})$ with $P_{W2}=-\Delta_2+D\Delta_1[h_2]$; the owner qualifier is carried verbatim. The remainder is **not** certified in this entry; the certified bound comes only from OPEN 21 below.

`[THM]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 | DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS] $\lvert\Delta_0\rvert\le K_0\sqrt q$, $K_0=\tfrac{1101}{1000}$ ($\lvert z\rvert\le\tfrac1{20}$), $\tfrac{533}{500}$ ($\lvert z\rvert\le\tfrac1{40}$). Not conditional on R9.

`[THM — conditional on RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 | DYAD-THM-OPEN3-ASYMPTOTIC-PHASE] T1 (limit equality) and T2 ($M_W-M=-\Delta_0(z_0)$), orbits starting in a row disk.

`[THM — conditional on RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 843–850, sha256 `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d` | DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER] $\lvert M_W-\mathcal P_2(W_0)\rvert\le K'_jQ_0^{3/2}+C_{2,j}(\tfrac{256}{225})^2Q_0^2$, rows A, B not mixed. Source-statement check PASS against v6.4.18 (A1a-E2, `941f42d6…126e`); the Dyadic P5 certificate and RECOG's R9 Arb certificate were not rerun; first published in v6.4.17 (owner-reported §6.14 identity).

**Typed interface and lemmas.**

`[DEF]` [RID: RECOG-DEF-A1A-PHASE-INTERFACE] For $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$ and the orbit $x_m=T^{6m}x_0$, three objects are tied to the same orbit: (i) the **A1a extension** $D_M^U:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$ for every $x_0\in U$ — NUMGEN's formula, made unambiguous on $U$ by RECOG-THM-A1A-LIFT-ALIGNMENT; on $U\cap U_{\rm NUMGEN}$, $D_M^U=D_M$. This extends a definition, not a NUMGEN theorem, and changes no custody; (ii) Dyadic's block phase $\Theta_W(m)$ from principal per-block increments $\operatorname{Arg}(W_{m+1}/W_m)$ with the lift tie; (iii) $z_m=h^{-1}(W_m)$. $\Psi_W:=\Theta_W-\tau\log Q$, $M_W:=\Psi_{W,\infty}-\Psi_W(0)$ where the limit exists. RECOG owns the typed join, not the three objects.

`[THM]` [RID: RECOG-THM-A1A-LIFT-ALIGNMENT] [scope: $U_T$ of DYAD-THM-PRIM-CTR] [proof: exact algebra + elementary enclosure] For every $x\in U_T$, $\tfrac\pi6<\delta_T(x)<\tfrac\pi2$, where $\delta_T$ is the primitive one-step angle increment. Hence for $x_0\in U$ and every integer $M\ge1$: $D_M^U=\Theta_W(0)-\Theta_W(M)$.
*Proof.* $W(Tx)=\lambda W+\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho)$ exactly ($\omega^2=-1-\omega$). On $U_T$, $\lvert\rho\rvert,\lvert\eta\rvert\le\tfrac2{\sqrt3}\lvert W\rvert<2R$, $R=\tfrac{47}{1000}$, and $2R<\ln2$; so $\lvert\eta-\sin\eta\rvert<\tfrac86\lvert W\rvert^3$, $\lvert e^\rho-1-\rho\rvert<4\lvert W\rvert^2$, and $\lvert W(Tx)/(\lambda W)-1\rvert<4R+\tfrac43R^2=\tfrac{143209}{750000}<\tfrac12$. Then $\lvert\operatorname{Arg}(1+\varepsilon)\rvert<\arcsin\tfrac12=\tfrac\pi6$ gives $\delta_T\in(\tfrac\pi6,\tfrac\pi2)$; six-step totals lie in $(\pi,3\pi)$, so each block increment of $\hat\phi$ is $2\pi+\operatorname{Arg}(W_{m+1}/W_m)$, and telescoping gives the identity. $\square$ Check: RECOG-ART-A1A-C1-CHECK.

`[THM]` [RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE] [scope: $x_0\in U$] $\lvert Q_{m+1}^{-1}-Q_m^{-1}-1\rvert<\tfrac{15}2\sqrt{Q_m}$; hence $Q_M^{-1}=Q_0^{-1}+M+O(\sqrt M)$ and $MQ_M\to1$.
*Proof.* By DYAD-THM-PRIM-CTR, $Q_{m+1}=Q_m(1-Q_m+\varepsilon_m)$ with $\lvert\varepsilon_m\rvert\le\tfrac{16931}{10000}Q_m^{3/2}+108Q_m^2$, so $Q_{m+1}^{-1}-Q_m^{-1}=1+\theta_m$, $\theta_m=(Q_m-\varepsilon_m/Q_m-\varepsilon_m)/(1-Q_m+\varepsilon_m)$, and with $\sqrt{Q_m}\le\tfrac1{20}$: $\lvert\theta_m\rvert\le\tfrac{7.17}{0.99}\sqrt{Q_m}<\tfrac{15}2\sqrt{Q_m}$. With $Q_m\le\min(Q_0,2/m)$, $\sum_{m<M}\lvert\theta_m\rvert=O(\sqrt M)$. $\square$ (Sufficient, not sharp.)

`[ALG]` [internal lemma; no RID] [scope: $x_0\in U$, $M\ge1$] **Finite-block identity.** $D_M^U-\tau\log M=\tau\log Q_0-\bigl(\Psi_W(M)-\Psi_W(0)\bigr)-\tau\log(MQ_M)$. Depends on: RECOG-THM-A1A-LIFT-ALIGNMENT.

**Results.**

`[THM]` [RID: RECOG-THM-A1A-PHASE-EXISTENCE-ALT] [assuming: H-NG] [scope: $x_0\in U$] **H-NG:** $\lim_M(D_M^U-\tau\log M)$ exists for the orbit of $x_0$. If H-NG holds, then $\Psi_{W,\infty}$ and $\Psi_{z,\infty}$ exist and $\Psi_{z,\infty}=\Psi_{W,\infty}=\Theta_W(0)-\lim_M(D_M^U-\tau\log M)$; the limit equals $\tau\log Q_0-M_W$. Depends on: the finite-block identity; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE; P4-0 and the offset bounds (every $x_0\in U$ has $\lvert z_0\rvert\le\tfrac{16}{15}\cdot\tfrac1{25}=\tfrac{16}{375}<\tfrac1{20}$, and the row disks are forward-invariant); H-NG. R9 is not used. The proof establishes H-NG ⇒ conclusion only.

`[RESULT]` `[from: ALG]` [RID: RECOG-RESULT-A1A-PHASE-EXISTENCE-NG] [scope: $x_0\in U\cap U_{\rm NUMGEN}$; $U_{\rm NUMGEN}$ has no explicit certified radius] **(a)** $\Psi_{z,\infty}=\Psi_{W,\infty}=\Theta_W(0)-C_D$ and $C_D=\tau\log Q_0-M_W$. **RECOG-THM-R9-MEMORY is not used.** Existence only: no memory coefficients, no $C_2$, no remainder. Depends on: RECOG-THM-A1A-PHASE-EXISTENCE-ALT with H-NG discharged by INF-1 used as true ($D_M^U=D_M$ on this domain).

`[THM]` [RID: RECOG-THM-A1A-CD-IDENTIFICATION] [scope: $x_0\in U$] **(b)** $C_D^{\rm ext}(x_0):=\lim_M(D_M^U-\tau\log M)$ exists and $C_D^{\rm ext}=\tau\log Q_0-M_W=\tau\log q_0+D_\Theta(z_0)-M(z_0)$. Depends on: RECOG-THM-R9-MEMORY (row $\lvert z\rvert\le\tfrac1{20}$, $q_0\le\tfrac1{400}$ since $\lvert z_0\rvert\le\tfrac{16}{375}$); Dyadic T1 and T2, whose R9 premise is discharged here; the finite-block identity; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE. *Dependency guard.* Dyadic NF6, PRIM-CTR and NF-REM feed R9; R9 feeds Dyadic T1/T2/OPEN 21, which feed (b) and (c). No A1a claim is used to establish R9.

`[RESULT]` `[from: ALG]` [RID: RECOG-RESULT-A1A-CD-AGREEMENT] [scope: $x_0\in U\cap U_{\rm NUMGEN}$] **(b′)** $C_D^{\rm ext}(x_0)=C_D(x_0)$, NUMGEN's constant. Depends on: RECOG-THM-A1A-CD-IDENTIFICATION and INF-1 used as true; both are limits of the same sequence on the overlap.

`[THM]` [RID: RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION] [scope: rows not mixed] **(c)** With the owner's second-order form $\mathcal P_2(W_0):=-\Delta_1(W_0)+Q_0[c_{\rm iso}+\Lambda_1(\Theta_{W_0})]+P_{W2}(W_0)$, $W_0=\lvert W_0\rvert e^{i\Theta_{W_0}}$, where $\Delta_1(W)=\lvert W\rvert[\tfrac{17\sqrt3}{36}\cos\Theta-\tfrac1{12}\sin\Theta-\tfrac{7\sqrt3}{72}\cos3\Theta+\tfrac18\sin3\Theta]$, $P_{W2}(W)=-\Delta_2+D\Delta_1[h_2]=\lvert W\rvert^2[-\tfrac{5\sqrt3}{27}+\tfrac{47\sqrt3}{1296}\cos2\Theta-\tfrac{19}{432}\sin2\Theta-\tfrac{11\sqrt3}{324}\cos4\Theta+\tfrac1{54}\sin4\Theta-\tfrac{\sqrt3}{1728}\cos6\Theta-\tfrac5{576}\sin6\Theta]$ (Dyadic v6.4.18 §6.14 lines 806–809), and $c_{\rm iso}$, $\Lambda_1$ of §6.13a:
$$C_D^{\rm ext}=\tau\log Q_0-\mathcal P_2(W_0)+E,\qquad\lvert E\rvert\le K'_jQ_0^{3/2}+C_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2 .$$

| Row | start domain here | owner primitive domain | chart disk | $K'_j$ | $C_{2,j}$ |
|---|---|---|---|---|---|
| A | $0<\lvert W_0\rvert\le\tfrac1{25}$ | $\tfrac3{64}$ | $\lvert z\rvert\le\tfrac1{20}$ | $\tfrac{3951}{1000}$ | $517$ |
| B | $0<\lvert W_0\rvert\le\tfrac3{128}$ | $\tfrac3{128}$ | $\lvert z\rvert\le\tfrac1{40}$ | $\tfrac{971}{250}$ | $163$ |

Chart inclusions $\tfrac{16}{15}\cdot\tfrac1{25}=\tfrac{16}{375}<\tfrac1{20}$, $\tfrac{16}{15}\cdot\tfrac3{128}=\tfrac1{40}$; row A is cut to $U$ because (b) needs $x_0\in U$. Depends on: RECOG-THM-A1A-CD-IDENTIFICATION; DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (R9 premise discharged by RECOG R9; its $C_{2,j}$ are R9's row constants). Source fidelity of the OPEN 21 statement, constants and rows: A1a-E2 PASS on v6.4.18; this is not a recertification.

`[NUM]` [scope: illustration; not a proof input, not a domain certificate] Twelve float64 primitive orbits in row A, 16,000 blocks: the alignment identity holds to $2.4\times10^{-9}$ (float drift); $(\hat C-[\tau\log Q_0-\mathcal P_2])/Q_0^{3/2}\in[-0.28,0.35]$. Artifact RECOG-ART-A1A-NUM.

**Scope and custody.** (i) Statement (a) is the only R9-free claim and holds only on the existential intersection. (ii) No Dyadic certified domain is widened, no Dyadic conditional grade is changed, and INF-1 gains no explicit radius. (iii) Nothing transfers to the comparator $C_W^{(h)}$ or to the R9 $C_z$ incompleteness corollary. (iv) $C_D$ depends on the start state; it is not universal. (v) The Dyadic acceptance of the lift-alignment derivation (C4 session) is a review acceptance, not a Dyadic owner adoption; no Dyadic RID is created. (vi) Separation: this cell defines no physical event and no token schedule; it does not touch R6, which stays ACTIVE. (vii) Not made: on $U$, H-NG and the convergence of $\Psi_W$ are equivalent ($\log(MQ_M)\to0$); only the one-way statement is registered.

"""
edit("S1", "§6.13b: A1a scientific cell (new science; eight proposed RIDs)",
 "### §6.14 The $h$-Chart Ledger (R11) `[ALG / import]` {#sec-6-14-chart-ledger}",
 S613B + "### §6.14 The $h$-Chart Ledger (R11) `[ALG / import]` {#sec-6-14-chart-ledger}",
 allowed_new_tags=["[THM / RESULT]", "[DEF]", "[RESULT]", "[THM]", "[ALG]", "[ALG — formal second order; remainder not certified]",
                   "[THM — conditional on RECOG-THM-R9-MEMORY]", "[NUM]"],
 allowed_new_rids=SCI_RIDS)

# ---------------------------------------------------------------- §7 rows
edit("I1", "§7: scope note on the NUMGEN defect-threshold row (RID covers the ratio theorem, not INF-1)",
 "RECOG adds the $c_{05}$ readability interpretation\n",
 "RECOG adds the $c_{05}$ readability interpretation. *Scope note (v0.3.22):* the RID is registered for the defect-threshold ratio theorem; the INF-1 formula $D_M=\\tau\\log M+C_D+o(1)$ quoted in this row is context and has no RID of its own in v1.20.7. The A1a cell imports INF-1 separately as `RID unavailable` (§6.13b, A1a-G1). No statement or use of this row changes\n")
edit("I2", "§7: A1a import rows",
 'RIDs marked "(none)" have no stable identifier',
 "- [RID: (none — NUMGEN $D_M$ definition, `RID unavailable`; RID allocation decided by the NUMGEN owner, canonical repin pending NUMGEN v1.20.8)] :: $D_M:=2\\pi M-(\\hat\\phi_{6M}-\\hat\\phi_0)$, increasing primitive lift :: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6 N-5A-S1-INF (`c4637e7a…ab28`) :: §6.13b interface (local extension $D_M^U$ on $U$) :: definition quoted verbatim; tracking key `A1A-NG-D-DEF`; temporary `RID unavailable` with recorded governance disposition (Methodology §3.3; A1a-G1 allocation resolved, repin pending NUMGEN v1.20.8)\n"
 "- [RID: (none — NUMGEN INF-1, `RID unavailable`; RID allocation decided by the NUMGEN owner, canonical repin pending NUMGEN v1.20.8)] :: $D_M=\\tau\\log M+C_D+o(1)$ `[RESULT] [from: ALG]`, independent of RECOG R9 (owner C4 reply) :: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6 :: §6.13b (a), (b′) :: $U_{\\rm NUMGEN}$, no explicit radius; tracking key `A1A-NG-INF1`; not `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`\n"
 "- [RID: DYAD-ALG-OPEN3-PHASE-OFFSET; DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS; DYAD-THM-OPEN3-ASYMPTOTIC-PHASE] :: P4-0 offset identity, $\\Delta_1$, $K_0$ per row; T1 and T2 (conditional on RECOG-THM-R9-MEMORY in the owner record) :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 (`33c14c5c…59e0`, release-verified) :: §6.13b (a)–(c) :: rows not mixed; R9 premise discharged by RECOG's own R9 for (b), (c) only; no $C_W^{(h)}$ statement\n"
 "- [RID: DYAD-ALG-OPEN3-PHASE-OFFSET, primitive-variable form] :: $\\mathcal P_2$, $P_{W2}=-\\Delta_2+D\\Delta_1[h_2]$, owner grade `[ALG — formal second order; remainder not certified]` :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 806–809 (`f70308f1…458d`) :: §6.13b (c) expression only :: remainder not certified here; certified bound only via OPEN 21\n"
 "- [RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER] :: $\\lvert M_W-\\mathcal P_2(W_0)\\rvert\\le K'_jQ_0^{3/2}+C_{2,j}(\\tfrac{256}{225})^2Q_0^2$, $K'_A=\\tfrac{3951}{1000}$, $K'_B=\\tfrac{971}{250}$, $C_{2,A}=517$, $C_{2,B}=163$, conditional on RECOG-THM-R9-MEMORY :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 843–850 (`f70308f1…458d`; first published v6.4.17) :: §6.13b (c) :: source-statement check PASS (A1a-E2, `941f42d6…126e`); P5 certificate not rerun; rows not mixed\n\n"
 'RIDs marked "(none)" have no stable identifier',
 allowed_new_tags=["[RESULT]", "[ALG — formal second order; remainder not certified]"],
 allowed_new_rids=["DYAD-ALG-OPEN3-PHASE-OFFSET", "DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER"])

# ---------------------------------------------------------------- §7.2 N13 row (three fields)
edit("N1", "§7.2 N13: received / source verification / RECOG use, kept separate",
 "| N13 (v6.4.17) | DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, conditional on RECOG-THM-R9-MEMORY, as reported (`e07cf2b9…4bfc`) | pending: Dyadic release verification of v6.4.17 not available to this review | none decided; conditional receipt only; recorded as a downstream dependent (§7.3) |",
 "| N13 (v6.4.17) | DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, conditional on RECOG-THM-R9-MEMORY, as reported (`e07cf2b9…4bfc`); carried in adopted v6.4.18 (`f70308f1…458d`) | v6.4.17: release verification reported passed by the Dyadic owner (report `c0ef4446…1e39`; owner-reported, the report itself not independently read here); v6.4.18 §6.14: independent source check of statement, grade, constants and rows for A1a, PASS (`941f42d6…126e`); v6.4.17 ↔ v6.4.18 §6.14 identity owner-reported; P5 certificate not rerun | v0.3.22 draft: proposed use in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (§6.13b) at the v6.4.18 pin, R9 premise discharged by RECOG's own R9; takes effect only on adoption (v0.3.21 state: conditional receipt only) |",
 allowed_new_rids=["RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION"])

# ---------------------------------------------------------------- §8 artifacts
edit("F1", "§8: A1a artifacts",
 "\n---\n\n## §9. Collaboration and Provenance",
 "\n- [RID: RECOG-ART-A1A-C1-CHECK] `[v0.3.22]` :: `recog_a1a_c1_angle_bound_check.py` (sha256 `343d737e480a065dea36b68a56e776f1432b5e96c6ad2bb3d09f69c3b5965c7a`) + output `recog_a1a_c1_angle_bound_check_output.txt` (`6ef14428001c6ed51d0066d9062d0e1247927eea3ccba60e1aaff20e641882ea`) :: gates 1–6 for RECOG-THM-A1A-LIFT-ALIGNMENT (identity and frame symbolic; $2R<\\ln2$ by a rational bound; ceiling $\\tfrac{143209}{750000}<\\tfrac12$ exact; $\\arcsin\\tfrac12=\\tfrac\\pi6$; gate 6 a `[NUM]` dense check of two elementary inequalities whose proof is written out); 3 negative controls caught; exit 0 :: `[ENG]`; supports, does not replace, the written proof\n"
 "- [RID: RECOG-ART-A1A-NUM] `[v0.3.22]` :: `recog_a1a_cd_identity_num.py` (`efccd210007ac206aff8ed1804051dc29f1ed110a426aee66325778ce90c791b`) + `a1a_cd_identity_num.json` (`09136040e85dcece83c52e1f159129c76f279ee23446580ab06f9d70478c9740`) :: float64 orbits; alignment identity and the (c) scaled error; byte-reproduced by the reviewer :: `[NUM]` illustration only\n"
 "- [RID: RECOG-ART-A1A-RECORDS] `[v0.3.22]` :: session records `RECOG_A1A_CD_IDENTIFICATION_SESSION_v0_1/_v0_2/_v0_3.md` (`cf22e325…f218`, `b4906ddf…c428`, `e542d105…8de0`); C4 questions to Dyadic (`fe80d507…2edd`) and NUMGEN (`f2b92173…9fec`, r2 `7a0752c7…6598`); Dyadic C4 response receipt (`36e20687…ee91`); NUMGEN C4 reply `8a887ef3…bc4d` and its receiving review `e5a5fcec…fec1` (reviewer-measured); cell drafts v0.1–v0.4 (`511e3c1d…782d`, `7adace40…ad79`, `febed7f9…9562`, `11758403…f4f7`) and their reviews (`02762139…f0e8b`, `1b1c664e…7068a0`, `d9b20aea…7a5`; session v0.3 review `5ccf9098…f994`) :: provenance of §6.13b; *archive locator:* the NUMGEN C4 reply, its receiving review and the cell-draft reviews are cited by identity and are not included in the draft review package (PI-held project evidence); the package manifest lists its own payload files only :: `[SESSION]` records\n"
 "- [RID: RECOG-ART-A1A-SOURCE-AND-GOVERNANCE] `[v0.3.22]` :: `RECOG_A1A_E2_OPEN21_SOURCE_CHECK_v6_4_18_20261020.md` (`941f42d6273f707bb161c24bd7e753c12acacda991dd29ff4050cbdcbfa6126e`; independent source-statement check against Dyadic v6.4.18, A1a-E2); `RECOG_A1A_CELL_DRAFT_v0_4_RELEASE_READINESS_REVIEW_20261020.md` (`d195af7aa5453d7392bfbb9f56fafb33cf8a391bf036935c7af56c15f8445274`); `RECOG_TO_NUMGEN_A1A_RID_REQUEST_20261020.md` (`a89b69243f24d63f74fed29c9af809f8616017ecdbbd8ef07446ed646e0246a0`; delivered to the NUMGEN owner side through the PI); NUMGEN reply `NUMGEN_REPLY_TO_RECOG_A1A_RID_REQUEST_20261020_v0_1.md` (`184a74fcede666c9427d0f959ed94b15c4206435b371b7d69b438a7254265227`; option 1; draft pending the string ruling — the final dispatched copy, same body with updated header, to be recorded on receipt); `RECOG_A1A_G1_RECEIPT_OF_NUMGEN_REPLY_20261020.md` (`87a0d9ce72f717be4a1cd256a12ff98b399578047d1d6da7b81fd447ac40722b`); `RECOG_A1A_G1_DISPOSITION_RECORD_20261020.md` (`0e5f91c0dabbd34bb8261ddd6e0a34361be4dbaaa9b3545b0f98fc14e3e971a7`; NUMGEN co-owner ruling of 20 Oct 2026; allocation resolved, repin pending v1.20.8); integrated receiving review of DRAFT r2 `RECOG_v0_3_22_DRAFT_r2_INDEPENDENT_RECEIVING_REVIEW_20261020.md` (`fee7e519f3e6cd8bf32aa2be0402bef667178148ea43c9fa8521159a1d500efe`); integrated receiving review of DRAFT r1 `RECOG_v0_3_22_DRAFT_r1_INTEGRATED_RECEIVING_REVIEW_20261020.md` (`c1d4901381305a101d11b88a5f553619eceb562829c40580fcf6734b34d88d17`) :: source verification and release-readiness review of the cell; RID-governance request :: `[SESSION]` records\n"
 "\n---\n\n## §9. Collaboration and Provenance",
 allowed_new_tags=["[ENG]", "[NUM]", "[SESSION]"], allowed_new_rids=ART_RIDS + ["RECOG-THM-A1A-LIFT-ALIGNMENT"])

# ---------------------------------------------------------------- §9 provenance row
edit("P1", "§9: provenance row for A1a",
 "RRF Registry (convention) | `[ALG]` / `[DEF]` |\n",
 "RRF Registry (convention) | `[ALG]` / `[DEF]` |\n"
 "| A1a / §6.13b: $C_D$ identification, lift alignment, $MQ_M\\to1$, R9-free existence route, per-row quantitative form | contributor (preliminary $C_D=\\tau\\log q_0+D_\\Theta-M$ derivation, the $(\\tfrac\\pi6,\\tfrac\\pi2)$ lemma replacing a wrong $(0,\\pi)$ claim, grade principle M13-C04, (b)/(b′) split, interface typing, G1/G2/E2 notes, source check against v6.4.18, release-readiness review); Claude (lift-alignment identity, rational ceiling and check script, $MQ_M\\to1$ proof, finite-block identity, reverse-direction existence observation, numerical illustration, cell drafting); Dyadic owner (C4 conditional session acceptance; v6.4.17/v6.4.18 release-verification reports); NUMGEN owner (C4 reply: INF-1 independent of R9, arbitrary start) | `[THM]` / `[RESULT]` |\n",
 allowed_new_tags=["[THM]", "[RESULT]"])

# ---------------------------------------------------------------- Appendix A + footer
edit("V1", "Appendix A v0.3.22 DRAFT r1 entry",
 "## Appendix A — Version History\n\n",
 "## Appendix A — Version History\n\n"
 "### v0.3.22 — DRAFT r3, 20 October 2026 (A1a scientific cell; not adopted)\n"
 "- **Basis:** A1a cell draft v0.4 (`11758403…f4f7`), accepted by the independent release-readiness review (`d195af7a…8445274`: scientific cell accepted; source check PASS; integration may start; RID governance and integrated-release verification outstanding; not adopted). Base: adopted v0.3.21 (`a3459522…0ae3`), used unchanged.\n"
 "- **§6.13b [new]:** A1a cell — interface, lift alignment, reciprocal amplitude, finite-block identity, H-NG implication, (a) R9-free existence, (b) $C_D^{\\rm ext}$ identification, (b′) NUMGEN agreement, (c) per-row quantitative form. Eight proposed scientific RIDs (registered only on adoption). Labels of the review trail are prefixed `A1a-` (A1a-G1, A1a-E2) to avoid collision with the v0.3.21 G1/G2/G3 records and with RRF OPEN-E2.\n"
 "- **§1, §5:** summary paragraph and high-risk row for A1a. **§7:** five A1a import rows (two NUMGEN `RID unavailable`, three Dyadic); scope note on the `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` row (the RID covers the ratio theorem, not INF-1). **§7.2:** N13 row updated in its three separate fields. **§8:** four artifact IDs. **§9:** provenance row.\n"
 "- **Release state:** (1) A1a-G1 — allocation resolved: NUMGEN reply v0.1 (`184a74fc…5227`) takes option 1 (dedicated RIDs in NUMGEN v1.20.8, no statement change) and the NUMGEN co-owner ruling of 20 Oct 2026 approves the allocations (`RECOG_A1A_G1_DISPOSITION_RECORD_20261020.md`); the imports keep `RID unavailable` with the interim governance line, and the repin to canonical NUMGEN RIDs is a follow-up after NUMGEN v1.20.8 adoption, not a v0.3.22 release blocker. (2) Integrated review of DRAFT r2 accepted (`fee7e519…0efe`). (3) PI adoption decision, recorded separately.\n"
 "- **r2 → r3:** A1a-G1 interim governance line in the companion header, §6.13b and the two §7 NUMGEN rows; status-summary release state; §8 governance records (reply, receipt, disposition, r2 review); r2-review note N1 (N13 use cell revision-neutral) and N2 (checker help text). No mathematical statement, grade, domain or proposed RECOG RID changed; no NUMGEN string is cited as an owner RID.\n"

 "- **r1 → r2 (integrated receiving review `c1d49013…8d17`: scientific/engineering integration accepted; limited metadata patch required):** L1 — status summary states that A1a's local extension $D_M^U$ (not NUMGEN's $D_M$) aligns on $U$, with $D_M^U=D_M$ only on $U\\cap U_{\\rm NUMGEN}$; L2 — every \"dedicated RID requested\" replaced by \"dedicated RID request prepared, not yet dispatched; A1a-G1 OPEN\"; optional — the header's v6.4.17 \"verification pending\" phrase labelled as v0.3.21 historical state with a pointer to §7.2 N13; §8 archive-locator note for items cited by identity but not packaged; r1 integrated review registered in §8. No mathematical statement, grade, domain or RID changed. Same adopted base; r1 draft and builder retained as history.\n"
 "- **Unchanged:** every existing scientific statement, RID statement and grade; every OPEN status (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED); RECOG-THM-R9-MEMORY and its rows; §7.3 register. G3 notices to OFN, RRF and RER remain unsent. No token/memory read-out vocabulary introduced.\n\n")
edit("V2", "footer",
 "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21*",
 "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22 (DRAFT r3; not adopted; v0.3.21 `a3459522…0ae3` remains authoritative until adoption)*")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    base = open(sys.argv[1], "rb").read()
    h = hashlib.sha256(base).hexdigest()
    if h != BASE_SHA:
        print(f"REFUSED: base sha256 {h} != {BASE_SHA}"); sys.exit(2)
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    text = base.decode("utf-8")
    for e in E:
        n = text.count(e["old"])
        if n != 1:
            print(f"ABORT: edit {e['id']} anchor count {n}"); sys.exit(2)
        text = text.replace(e["old"], e["new"], 1)
    draft = os.path.join(out_dir, "RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22_DRAFT_r3.md")
    open(draft, "wb").write(text.encode("utf-8"))
    json.dump({"base_sha256": BASE_SHA, "proposed_scientific_rids": SCI_RIDS, "new_artifact_rids": ART_RIDS, "edits": E},
              open(os.path.join(out_dir, "recog_v0_3_22_edits_r3.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"BUILT {draft} sha256 {hashlib.sha256(text.encode('utf-8')).hexdigest()} ({len(E)} edits)")

if __name__ == "__main__":
    main()
