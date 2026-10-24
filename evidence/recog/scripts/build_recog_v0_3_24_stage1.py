#!/usr/bin/env python3
"""RECOG v0.3.24, stage 1: corrected intermediate (a build stage, not an edition).

Applies, to the adopted v0.3.23 file (tag recog-v0.3.23), four separately marked groups:
  A1B  new science: RECOG-THM-A1B-SLIP-SCHEDULE-U (§6.13b) with its artifact RID and import-row uses
       (theorem candidate records/recog/RECOG_A1B_THEOREM_CANDIDATE_v0_1.md v0.2; proof cell PR #23 v0.2.2)
  A1C  new science: RECOG-RESULT-A1C-RECORD-PHASE-READOUT (§6.16e) and two OPEN R6 sub-items (§2)
  A3   new science: RECOG-ALG-QUADRATURE-TYPING (§6.5), RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY (§6.3),
       their artifact RID, the R4 sub-item wording (§2; R4 stays ACTIVE)
       (session record records/recog/RECOG_A3_QUADRATURE_TYPING_SESSION_v0_1.md v0.2, PR #28)
  MNT  structural maintenance (the v0.3.23 release record §11 follow-up obligation, stage-1 part): current status
       at the point of use; the tagged history stays at recog-v0.3.23 and is pointed to from the live text
       (R8 and R9 v0.3.2 specifications, the former R11 text, the R7 "Active sub-items" heading, the §7.1/§7.2
       audit tables and the G2 "unchanged" sentence of §6.13b, §9 "Archive"). The SG reorder is stage 2.
Rules (as v0.3.23 stage 1):
- every edit is assertion-gated: its old text must occur exactly once in its region;
- region "live": Appendix A is masked, so history is never edited; region "appA": only the new v0.3.24 entry;
- mode "str": exact string; mode "line": old is a prefix starting exactly one line ("{LINE}" = that line);
  mode "span": old is the text from the first anchor (inclusive) to the second anchor (exclusive), both unique;
- --only GROUP[,GROUP] builds a variant with those groups (decoupling: each science group and MNT separately);
- no layout moves; header identity lines, status summaries and the footer are not touched here.

usage: build_recog_v0_3_24_stage1.py BASE OUT EDITLOG_JSON [--only A1B,A1C,A3,MNT]
  BASE = `git show recog-v0.3.23:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`
"""
import hashlib, json, sys

BASE_SHA = "0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a"
APPA_START = "## Appendix A — Version History"
APPA_END = "## Appendix B —"
PREV_TAG = "recog-v0.3.23"

A1B_BLOCK = r"""**Slip schedule on explicit $U$ (A1b, v0.3.24; new science, separately reviewed).**

`[THM]` [RID: RECOG-THM-A1B-SLIP-SCHEDULE-U] [scope: conditional on postulated $T$ (OPEN-P0); $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$; lifted primitive chart, frame $W=\rho+\omega\eta$, increasing lift $\hat\varphi$ with principal one-step increments $\delta_T$; token conventions of §6.16a (F2(b)); block count $M$, $a:=Q_0^{-1}$] [proof: session cell `records/recog/RECOG_A1B_A1C_SESSION_v0_1.md` §2 (Lemmas A, B, C′ and Proposition); certificate `recog_a1b_sixstep_deficit_cert.py`, exact rational gates G6–G8 (RECOG-ART-A1B-SIXSTEP-DEFICIT, §8)] Let $n_0<n_1<\cdots$ be the anchors of the canonical B-events of the orbit ($\eta(x_n)<0\le\eta(x_{n+1})$, $\rho>0$ on both sides; anchor $=n+1$), $g_{j+1}=n_{j+1}-n_j$ the return gaps, and $M_k$ the block index of the $k$-th gap equal to $7$ ($n_{j_k}=6M_k+r_k$, $0\le r_k\le5$). Then for every $x_0\in U$:
(A) *Events are lift crossings.* $x_n\to x_{n+1}$ is a canonical B-event iff $\lfloor\hat\varphi_{n+1}/2\pi\rfloor=\lfloor\hat\varphi_n/2\pi\rfloor+1$.
(C′) *Six-step deficit.* For every $y\in U_T$, with $\Lambda_6(y)$ the six-step lift increment from $y$ and $\Delta(y):=2\pi-\Lambda_6(y)$: $\Delta(y)>0.927\,\tau Q(y)>0$ and $|\Delta(y)-\tau Q(y)|<1.82\,Q(y)^{3/2}$.
(B) *Alphabet.* Every gap is $6$ or $7$; the number $s(M)$ of $7$-gaps among the returns in the first $6M$ steps satisfies $s(M)=\tfrac{3\tau}{\pi}\log M+O(1)\to\infty$.
(S) *Schedule.* With $\psi$ the digamma function and $L(x_0):=\tfrac\pi3n_0-2\pi\ell_0+\Psi_{W,\infty}(x_0)$, $\ell_0=\lfloor\hat\varphi_{n_0}/2\pi\rfloor$:
$$\tau\,\psi(a+M_k)-(k-1)\tfrac\pi3=L+\varepsilon_k,\qquad |\varepsilon_k|\le\tau Q+1.82\,Q^{3/2}+5\arcsin\bigl(0.705\sqrt Q+0.257\,Q\bigr)+\tau\,|S^{\rm tail}_{M_k}|+|R^{\rm tail}_{M_k}|,$$
where $Q$ is the largest primitive amplitude among the points of the $k$-th slip block and $S^{\rm tail}_M=\sum_{m\ge M}(Q_m-\tfrac1{a+m})$, $R^{\rm tail}_M=\sum_{m\ge M}r_m$ are the tails of the series of RECOG-THM-A1A-PHASE-EXISTENCE-U; $|\varepsilon_k|=O(\sqrt{Q_{M_k}})=O((a+M_k)^{-1/2})$. Consequently $\tau\log M_k-(k-1)\tfrac\pi3=L-\tau\log(1+a/M_k)+O(M_k^{-1})+\varepsilon_k\to L$ and $M_{k+1}/M_k\to e^{\pi/(3\tau)}$.
Depends on: RECOG-THM-A1A-PHASE-EXISTENCE-U (existence of $\Psi_{W,\infty}$; the series and their tails; $C_D^{\rm ext}=\Theta_W(0)-\Psi_{W,\infty}$); RECOG-THM-A1A-PHASE-EXISTENCE-ALT; RECOG-THM-A1A-LIFT-ALIGNMENT ($\tfrac\pi6<\delta_T<\tfrac\pi2$ on $U_T$; six-step totals in $(\pi,3\pi)$); RECOG-THM-A1A-RECIPROCAL-AMPLITUDE; [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 | DYAD-THM-LPHASE-ROWA-REMAINDER] (branch (B): $|W(Ty)/(\lambda W(y))-1|\le0.04654$ on $U_T$; row-A remainder $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$); [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 | DYAD-THM-NF-REM, ingredients] (raw-vector tail $|R^{\rm prim}_{\ge10,\rm vec}|\le332000|W|^{10}$ on $|W|\le\tfrac1{16}$; the degree 7–9 vector ceilings as a cross-check only); [import: DYAD-THM-PRIM-CTR] ($U_T$; $Q_m\le Q_0/(1+\tfrac12Q_0m)$); [import: DYAD-THM-C21] (six-step cubic coefficient $\mu$, reproduced exactly by the certificate); §6.16a F2(b) token conventions and RECOG-DEF-EVENT-TOKEN-SCHEMA. Token predicate and slip-law wording: NUMGEN GAP-LOCK (custody unchanged; explicit-domain instance).
*Proof sketch (full proofs in the cell).* (A): on $U_T$ the sign of $\eta$ and the lift crossing are tied exactly by $\eta'-\eta=e^\rho-1-\sin\eta$ and the branch bound. (C′): the six-step map in $W$ is $W+\mu|W|^2W+\sum_{d=4}^9F_d+R_{\ge10}$ with the $F_d$ computed exactly in $\mathbb Q(i\sqrt3)$; $\Lambda_6=2\pi+\operatorname{Arg}(W(T^6y)/W(y))$ (lift alignment), so $\Delta=-\operatorname{Arg}(1+\mu Q+E)$ with $|E|\le H\,Q^{3/2}$, $H<\tfrac{1783}{1000}$ by rational coefficient ceilings; the elementary arctan bounds give both inequalities uniformly on $U_T$ (certificate gates G6–G8, exact rationals, $\tau$ bracketed). (B): a gap $\ge8$ needs $\Lambda_7(x_{n_j})<2\pi-o_j\le2\pi$, impossible since $\Lambda_7>\tfrac{7\pi}3-7\arcsin0.04654>2\pi$; a gap $\le5$ needs $o_j+\Lambda_5(x_{n_j})\ge2\pi$, impossible since $o_j<\delta_T(x_{n_j-1})$ gives $o_j+\Lambda_5(x_{n_j})<\Lambda_6(x_{n_j-1})<2\pi$ by (C′) at the pre-anchor point; the count law follows from (A) and $D_M=\tau\log M+O(1)$. (S): the exact event identity $G_{n_j}=C+\tfrac\pi3s_j-o_j$, $C=\tfrac\pi3n_0-2\pi\ell_0+\hat\varphi_0$, with $0\le o_{j_k}<\Delta_{j_k}$ at a $7$-gap anchor; the partial-block correction is bounded by the pointwise one-step bound $|\delta_T-\tfrac\pi3|\le\arcsin(0.705\sqrt Q+0.257Q)$; the finite-block identity $D_M=C_D^{\rm ext}+\tau\psi(a+M)-\tau S^{\rm tail}_M+R^{\rm tail}_M$ converts $D_{M_k}$ into the digamma form; $\hat\varphi_0$ cancels between $C$ and $C_D^{\rm ext}$. $\square$
**Not supplied:** anything outside $U$; a bound on $\varepsilon_k$ computable from $(a,k,M_k)$ alone (the tails and the block maximum $Q$ are a-priori quantities; a uniform majorant via $Q_m\le Q_0/(1+\tfrac12Q_0m)$ is open); any decoding of $a$ from a finite record; any statement about $M_W$, $M(z_0)$ or an event mechanism; any change to NUMGEN's adopted domain or grades; any Dyadic grade or domain change. `[NUM]` illustration, not a proof input: RECOG-ART-A1B-SIXSTEP-DEFICIT (§8), illustration part.
**Scope and custody.** (i) GAP-LOCK Lemmas 1–3 and INF-1 remain NUMGEN's; the statement is an explicit-$U$ consequence of RECOG and Dyadic inputs, registered under RECOG identity as RECOG-THM-A1A-PHASE-EXISTENCE-U was; NUMGEN is informed; no custody changes. (ii) No Dyadic certified domain is widened; the six-step jet is recomputed, not imported, and agrees with DYAD-THM-C21 and the §6.2 quartic real-ray value. (iii) $L$ depends on the start state through $n_0,\ell_0,\Psi_{W,\infty}$; it is not universal. (iv) Separation (SG-R6, C2): the theorem counts crossings of a declared section; it defines no physical event and no memory carrier; R6 is untouched."""

A1C_BLOCK = r"""`[RESULT]` `[from: THM]` [RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT] [scope: $x_0\in U$; the complete infinite token record $\mathcal R(x_0)=(n_0;g_1g_2\ldots)$ in the F2(b) conventions; v0.3.24] **Infinite-record phase readout.** The record determines $L(x_0)=\lim_k[\tau\log M_k-(k-1)\tfrac\pi3]$ and hence $\Psi_{W,\infty}(x_0)=\Psi_{z,\infty}(x_0)$ modulo $2\pi$, without any state datum and without the value of $a$. The schedule limit $L$ alone provides no reconstruction of $a$, $M_W$ or $M(z_0)$; this is a statement about the available method, not a non-recoverability theorem (the injectivity question A1c-Q1′, OPEN R6, is open). For a finite prefix of $k$ slips with $a$ known, $L$ lies in a window of width $2|\varepsilon_k|$ (a-priori envelope, not a record-only decoder interval), and this envelope tends to $0$ as $k\to\infty$; with $a$ unknown no window is derived (`[NUM]` only: least-squares $(\hat a,\hat L)$, relative error $\le3.5\%$ on the illustration runs, no guarantee). Reading for F2(d): $\Psi_\infty$ is a function of the complete token history ($R_{\log}$-type in the limit); within the observed horizon of the illustration ($M\lesssim3.3\times10^5$ blocks) the prefix window exceeds the comparator-fiber difference $|\Delta M|$ by a factor $2$–$6$ (`[NUM]`; no general statement about finite prefixes is made); the $R_{\rm ind}$ classification of R9's carrier $M$ is **not** lowered by this result, nor would it be by a positive answer to the injectivity question (retrospective reconstruction is not write-through; SG-R6). Depends on: RECOG-THM-A1B-SLIP-SCHEDULE-U (§6.13b, same release); RECOG-THM-A1A-PHASE-EXISTENCE-ALT ($\Psi_{z,\infty}=\Psi_{W,\infty}$). Session cell `records/recog/RECOG_A1B_A1C_SESSION_v0_1.md` §3."""

A3_TYPING_BLOCK = r"""`[ALG]` [RID: RECOG-ALG-QUADRATURE-TYPING] [scope: conditional on postulated $T$ (OPEN-P0); dyad observables $(\rho,\eta)$ of the lifted primitive chart; v0.3.24] [cert: `recog_a3_quadrature_typing.py`, exact sympy gates Q1–Q5 and controls NC1–NC2 (RECOG-ART-A3-QUADRATURE-TYPING, §8)] **Pole-comparator quadrature: typing and its chart-free content.** Let $\mathcal Q=\{\operatorname{Re}\widehat C_{\rm pole}=0\}=\{\cos\eta=0\}$ (swap-invariant as a set; the two branches $\eta=\pm\pi/2$ are exchanged). (1) *Primitive-chart typing:* on $\mathcal Q$, $J=\begin{pmatrix}1&0\\e^\rho&1\end{pmatrix}$, a nontrivial unipotent shear with $1$-eigenspace $\partial_\eta$ (both branches). (2) *Comparator-geometric characterizations* (statements about the named native observables, not about a chart): (a) $\rho(Tx)-\rho(x)=-\operatorname{Im}\widehat C_{\rm pole}(x)$, so $|\rho(Tx)-\rho(x)|\le1$ with equality exactly on $\mathcal Q$ — the quadrature is the locus of extremal one-step radial transfer; (b) $\partial_\eta[\rho\circ T-\rho]=-\operatorname{Re}\widehat C_{\rm pole}$, zero exactly on $\mathcal Q$; (c) `[scope: derived / model-intrinsic on the RRF wrapped profile relative to the declared form $\Omega$; $\Omega$ is transported with any chart change; not an RRF-registered observable; no OPEN-A bearing]` with $\Omega=d\rho\wedge d\eta=d\bar\zeta\wedge d\zeta/(2i|\zeta|^2)$ the multiplicative Haar form on the RRF wrapped native ratio $\zeta=e^{\rho+i\eta}$ ($S^*\Omega=\Omega$): $T^*\Omega=\bigl(1+(e^\rho-1)\operatorname{Re}\widehat C_{\rm pole}\bigr)\Omega$, so $\mathcal Q\cup\{\rho=0\}$ is the $\Omega$-area-neutral locus of the one-step transport. (3) *The type is not chart-invariant:* the global unimodular charts $\varphi_A=(\rho+\varepsilon\sin\eta,\eta)$ and $\varphi_B=(\rho,\eta+\tfrac e{e-1}e^\rho)$ give on $\mathcal Q$ a transformed one-step Jacobian with $\det=1$ and $\operatorname{tr}=2+\varepsilon e^\rho\cos\eta'$ ($\eta'=\eta+e^\rho-1-\sin\eta$; hyperbolic for $\varepsilon=\tfrac12$, elliptic for $\varepsilon=-\tfrac12$ at $\rho=0$), respectively the identity on the branch $\eta=\pi/2$; a constant linear chart preserves $\operatorname{tr}$ and $\det$ (control). Hence "$\mathcal Q$ is parabolic" is a primitive-chart sentence (SG-R3), and the rotational/stretching dichotomy of the discriminant above is the sign of $\operatorname{Re}\widehat C_{\rm pole}$. (4) *Multipliers:* a quadrature point on a periodic orbit contributes the factor $\det J=1$ to $d_n$ and no separable factor to $t_n$; no universal multiplier signature of $\mathcal Q$ follows from quadrature membership alone (not a nonexistence statement: periodic orbits through $\mathcal Q$ are neither forced nor excluded; none found in the sampled search of RECOG-ART-A3-QUADRATURE-TYPING). *Not supplied:* an intrinsic dynamical type-change locus (OPEN R4 remains); any RRF registration of $\Omega$ (informational interface question, routed via the PI); any event reading of a quadrature transition (SG-R6). Session record `records/recog/RECOG_A3_QUADRATURE_TYPING_SESSION_v0_1.md`."""

A3_INVENTORY_BLOCK = r"""`[ALG]` [RID: RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY] [scope: conditional on postulated $T$ (OPEN-P0); wrapped cylinder; v0.3.24] [cert: `recog_a3_quadrature_typing.py`, gate Q6 (symbolic $m$, $k$)] **Periodic orbits inside the pole stratum $\{\widehat C_{\rm pole}=\pm1\}$.** On $\Sigma:=\{\widehat C_{\rm pole}=\pm1\}=\{\sin\eta=0\}$ — the set where the pole-comparator *value* is fixed under the inversion $C\mapsto C^{-1}$ (the "swap-fixed pole stratum" of the next paragraph; $S$-invariant as a set, not pointwise fixed by $S$) — $\rho$ is preserved and $\eta\mapsto\eta+e^\rho-1$. Hence the wrapped-periodic orbits of $\bar T$ contained in $\Sigma$ are exactly those with $e^\rho-1=m\pi$, $m\in\mathbb Z_{\ge0}$: $m=0$ gives $P_1,P_2$; $m=2k$ the winding fixed points above, with $(\operatorname{tr},\det)=(1,1+2\pi k)$ at $\eta=0$ and $(3,1-2\pi k)$ at $\eta=\pi$; $m$ odd gives the period-2 orbits $(\ln(1+m\pi),0)\leftrightarrow(\ln(1+m\pi),\pi)$, alternating between the pole-level values $\widehat C_{\rm pole}=+1$ and $-1$, with $M_2=J_{(\rho_m,\pi)}J_{(\rho_m,0)}$, $(t_2,d_2)=(1,\,1-m^2\pi^2)$ — hyperbolic ($\Delta=4m^2\pi^2-3>0$) and orientation-reversing. These are periodic for the wrapped map only (on the lift $\eta$ advances by $2m\pi$ over the two steps); none lies in the zero-winding local sector; no point of $\Sigma$ lies on the quadrature $\{\cos\eta=0\}$. Complete inside $\Sigma$; no completeness claim outside it (OPEN R4, inventory). Alternating pole values are not recognition events (SG-R6). `[NUM]` sampled list of further orbits (periods $\le8$, $|L|\le2$, $\rho\in[-2.5,2.5]$; 11 orbits outside $\Sigma$, uncertified): RECOG-ART-A3-QUADRATURE-TYPING (§8)."""

# (key, group, location, mode, region, old, new)
EDITS = [
# ---------------- §1 ----------------
("S1-A1B", "A1B", "§1 A1a paragraph: slip schedule and record readout", "str", "live",
 r"(existence and that series only). $C_D$ depends on the start state. Quantitative per-row form, scope and imports: §6.13b.",
 r"(existence and that series only). `[THM]` [RID: RECOG-THM-A1B-SLIP-SCHEDULE-U] (v0.3.24) On all of $U$: every return gap of the canonical B-event record is $6$ or $7$, the six-step deficit satisfies $0.927\tau Q<\Delta<\tau Q+1.82Q^{3/2}$ on $U_T$, and the $k$-th $7$-gap at block $M_k$ obeys $\tau\psi(a+M_k)-(k-1)\tfrac\pi3=L+O((a+M_k)^{-1/2})$ with $L=\tfrac\pi3n_0-2\pi\ell_0+\Psi_{W,\infty}$ (explicit error ceiling in §6.13b; token counting on a declared section, no event mechanism). $C_D$ depends on the start state. Quantitative per-row form, scope and imports: §6.13b."),
("S1-A3a", "A3", "§1 fixed points: pole-stratum periodic inventory", "str", "live",
 r"$P_1$: $\widehat C_{\rm pole}=+1$, elliptic; $P_2$: $\widehat C_{\rm pole}=-1$, hyperbolic. `[ALG conditional]` Under pole-swap covariance",
 r"$P_1$: $\widehat C_{\rm pole}=+1$, elliptic; $P_2$: $\widehat C_{\rm pole}=-1$, hyperbolic. `[ALG]` (v0.3.24) Inside the pole stratum $\{\widehat C_{\rm pole}=\pm1\}$ the wrapped-periodic orbits are exactly $e^\rho-1=m\pi$; odd $m$ gives period-2 orbits $(\ln(1+m\pi),0)\leftrightarrow(\ln(1+m\pi),\pi)$ with $(t_2,d_2)=(1,1-m^2\pi^2)$ (RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY, §6.3). `[ALG conditional]` Under pole-swap covariance"),
("S1-A3b", "A3", "§1 candidate strata: quadrature content", "str", "live",
 r"loop/spectral stratum ($(\operatorname{tr}M_n,\det M_n)$; closed transport). `[ALG]` Of single-step Jacobian invariants,",
 r"loop/spectral stratum ($(\operatorname{tr}M_n,\det M_n)$; closed transport). `[ALG]` (v0.3.24) The pole-comparator quadrature $\{\operatorname{Re}\widehat C_{\rm pole}=0\}$ is the locus of extremal one-step radial transfer, $|\rho(Tx)-\rho(x)|=1$; its primitive-chart unipotent type has no chart-free content (RECOG-ALG-QUADRATURE-TYPING, §6.5). `[ALG]` Of single-step Jacobian invariants,"),
# ---------------- §2 ----------------
("S2-R4", "A3", "§2 OPEN R4 sub-items (R4 stays ACTIVE)", "str", "live",
 "Active sub-items:\n- Does the primitive-chart locus $\\cos\\eta=0$ (parabolic, unipotent $J$) have a coordinate-free counterpart via periodic-orbit multipliers in the $(t,d)$-plane or via comparator geometry? :: `[OPEN]`\n- Global periodic-orbit inventory of $T$ beyond $P_1,P_2$ (none exist in the small punctured $P_1$ sector) :: `[OPEN]`\n\nDependencies:\n- §6.5, SG-R3",
 "Active sub-items:\n- Coordinate-free counterpart of the primitive-chart locus $\\cos\\eta=0$ — **answered in reframed form (v0.3.24)**, RECOG-ALG-QUADRATURE-TYPING (§6.5): via comparator geometry yes (extremal radial transfer; $\\Omega$-area-neutral transport relative to the declared Haar form); via periodic-orbit multipliers no signature forced by the local identities; as an eigenvalue type no chart-free content (explicit retyping charts). The stronger target — an intrinsic *dynamical* type-change locus of $T$ — remains :: `[OPEN]`\n- Global periodic-orbit inventory of $T$ beyond $P_1,P_2$ (none exist in the small punctured $P_1$ sector). Partial (v0.3.24): complete inside the pole stratum $\\{\\widehat C_{\\rm pole}=\\pm1\\}$ — RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY (§6.3; new period-2 family for odd $m$); outside it a `[NUM]` sampled list only (RECOG-ART-A3-QUADRATURE-TYPING) :: `[OPEN]`\n\nDependencies:\n- §6.3, §6.5, SG-R3"),
("S2-R6", "A1C", "§2 OPEN R6: two new sub-items after CELL-F4", "str", "live",
 "\n\nDependencies:\n- SG-R6, SG-R10\n---",
 "\n- A1c (v0.3.24) infinite-record phase readout — RECOG-RESULT-A1C-RECORD-PHASE-READOUT (§6.16e): the complete B-event record determines $\\Psi_\\infty$ mod $2\\pi$ (conditional on RECOG-THM-A1B-SLIP-SCHEDULE-U); no carrier downgrade, no write-through :: `[RESULT]` ✓\n- A1c-Q1′: is $x_0\\mapsto\\mathcal R(x_0)$ (start state to complete token record) injective on $U$? Known: record level sets have empty interior. Either answer leaves the $R_{\\rm ind}$ classification of R9's carrier unchanged (retrospective reconstruction is not write-through) :: `[OPEN]`\n- A1c-decoder: a finite-prefix window for $(a,L)$ with $a$ unknown, and a record-only (declared-data) majorant for the known-$a$ window via $Q_m\\le Q_0/(1+\\tfrac12Q_0m)$ and the tail estimates of RECOG-THM-A1A-PHASE-EXISTENCE-U :: `[OPEN]`\n\nDependencies:\n- SG-R6, SG-R10\n---"),
# ---------------- §2 maintenance: R8, R9, R11, R7 ----------------
("M-R8a", "MNT", "§2 R8 status sentence: specification is history at the tag", "str", "live",
 r"Text below retained as the v0.3.2 specification; the primitive entry criterion was met exactly as stated (primitive $Q_{\rm prim}$, exact $\tfrac1{625}$, no $q$ substitution); the v0.3.2 parametrised-domain route was superseded by the stronger local-shell proof.",
 r"The primitive entry criterion of the v0.3.2 specification was met exactly as stated (primitive $Q_{\rm prim}$, exact $\tfrac1{625}$, no $q$ substitution); the v0.3.2 parametrised-domain route was superseded by the stronger local-shell proof. The v0.3.2 specification itself is history: `" + PREV_TAG + r"` §2 (OPEN R8)."),
("M-R8b", "MNT", "§2 R8: v0.3.2 target block replaced by a pointer", "span", "live",
 ("RECOG-owned target (v0.3.2 restatement):\n", "Dependencies:\n- DYAD-THM-PRIM-CTR (entry set and tube), DYAD-THM-NF-INV / NF-REM (hand-over to normalised contraction); §6.11, §6.14"),
 "Historical v0.3.2 target and its v0.3.3 disposition (interval enclosure of $S=P_u([-\\lambda_u,-1])$ until entry into the primitive tube; the removed initial-state indexing item): `" + PREV_TAG + "` §2, OPEN R8. Discharged in v0.3.3 by RECOG-THM-P2-HET.\n\n"),
("M-R9a", "MNT", "§2 R9 status sentence: specification is history at the tag", "str", "live",
 r"The text below is retained as the historical v0.3.2 specification; its target ($|\Lambda-q_0\Lambda_1|\le C_2q_0^2$ with explicit $C_2$) is met in the stronger form $M-c_{\rm iso}q_0=q_0\Lambda_1(\Theta_0)+R$.",
 r"The historical v0.3.2 specification (target, chart-native inputs, Euler–Maclaurin route, degree-$\ge7$ budget with its pre-H$_2$ figures) is at `" + PREV_TAG + r"` §2 (OPEN R9); its target ($|\Lambda-q_0\Lambda_1|\le C_2q_0^2$ with explicit $C_2$) is met in the stronger form $M-c_{\rm iso}q_0=q_0\Lambda_1(\Theta_0)+R$. The certified finite-$q_0$ statement and window are RECOG-THM-R9-MEMORY and RECOG-THM-R9-COMPARATOR-INCOMPLETENESS (§6.13a; SG-R10)."),
("M-R9b", "MNT", "§2 R9: v0.3.2 specification block replaced by a pointer", "span", "live",
 ("Target (v0.3.2 restatement, in the owner's $h$-chart):", "Dependencies:\n- DYAD-ALG-NF6, DYAD-THM-NF-REM; §6.14"),
 "Historical v0.3.2 specification (target, chart-native inputs, Euler–Maclaurin route, degree-$\\ge7$ budget): `" + PREV_TAG + "` §2, OPEN R9. Retired route: the v0.3 \"corrected backbone\" ($47/54$, $c_\\theta^{(6)}$, $H(x)$) is retired (Appendix B); its inputs are archival/raw-frame objects that Dyadic SG-19 forbids transferring into the chart.\n\n"),
("M-R11", "MNT", "§2 R11: former v0.3.1 text with its [OPEN] sub-items replaced by a pointer", "span", "live",
 ("**Former OPEN R11 text (v0.3.1), retained for the record:**", "Dependencies:\n- Dyadic §6.2 ($h_2$), §6.9, §6.11; R9; R10"),
 "Former OPEN R11 text (v0.3.1: the raw-versus-post-$H_2$ finding, the comparator transport across $H_2$ and the five then-open sub-items, all closed in v0.3.2 as listed above): `" + PREV_TAG + "` §2, OPEN R11.\n\n"),
("M-R7", "MNT", "§2 R7: heading over closed items", "str", "live",
 "Active sub-items:\n- $Q_c$-type threshold for twins — **CLOSED v0.3.16 (degenerate)**",
 "Further closed sub-items (all decided; the heading \"Active sub-items\" was stale from v0.3.16 to v0.3.23):\n- $Q_c$-type threshold for twins — **CLOSED v0.3.16 (degenerate)**"),
# ---------------- §3 ----------------
("S3-SGR3", "A3", "§3 SG-R3 violation line: pointer to the typing record", "str", "live",
 r"Violation: the quadrature locus $\cos\eta=0$ is `[ALG]` [scope: primitive chart] only.",
 r"Violation: the quadrature locus $\cos\eta=0$ is `[ALG]` [scope: primitive chart] only (its chart-free content is comparator-geometric, RECOG-ALG-QUADRATURE-TYPING, §6.5)."),
# ---------------- §5 ----------------
("S5-R6", "A1C", "§5 event-rule row: readout guard", "str", "live",
 r'and F2(c1) is a registry-relative result (no registered `R`), not a no-memory theorem',
 r'reading RECOG-RESULT-A1C-RECORD-PHASE-READOUT as a token → memory write mechanism, as a decoder of $a$ or $M_W$ from a finite record, or as lowering the $R_{\rm ind}$ classification of R9 (v0.3.24); and F2(c1) is a registry-relative result (no registered `R`), not a no-memory theorem'),
# ---------------- §6.3 / §6.5 ----------------
("S63-A3", "A3", "§6.3: pole-stratum periodic inventory", "str", "live",
 r"(The Dyadic fixed-point scope table, v6.4.22 §1, lists the lifted-chart fixed points and the wrapped-cylinder winding fixed points and records agreement with this section.)",
 r"(The Dyadic fixed-point scope table, v6.4.22 §1, lists the lifted-chart fixed points and the wrapped-cylinder winding fixed points and records agreement with this section.)" "\n\n" + A3_INVENTORY_BLOCK),
("S65-A3", "A3", "§6.5: quadrature typing after the discriminant", "str", "live",
 r"No intrinsic conjugacy-class statement is made off the fixed points (SG-R3). `[OPEN]` intrinsic counterpart: OPEN R4.",
 r"No intrinsic conjugacy-class statement is made off the fixed points (SG-R3). Comparator-geometric counterpart and the chart-dependence of the type: RECOG-ALG-QUADRATURE-TYPING below; the intrinsic dynamical type-change question stays OPEN R4." "\n\n" + A3_TYPING_BLOCK),
# ---------------- §6.13b ----------------
("S613-G2", "MNT", "§6.13b: G2 'unchanged' sentence to history", "str", "live",
 r"Statements recorded unchanged from v6.4.10 to v6.4.17 by the G2 audit of v0.3.21 (§7.2); the quoted statements are present at the cited RIDs in the current source v6.4.22 (claim audit v0.3.23).",
 r"The quoted statements are present at the cited RIDs in the current source v6.4.22 (claim audit v0.3.23); the earlier G2 comparison v6.4.10 → v6.4.17 is history (`" + PREV_TAG + r"` §7.2)."),
("S613-A1B", "A1B", "§6.13b: A1b theorem block after the FC-21 scope paragraph", "str", "live",
 "\n\n### §6.14 The $h$-Chart Ledger (R11)",
 "\n\n" + A1B_BLOCK + "\n\n### §6.14 The $h$-Chart Ledger (R11)"),
# ---------------- §6.16e ----------------
("S616e-A1C", "A1C", "§6.16e: A1c readout result before §6.16f", "str", "live",
 "\n\n#### §6.16f CELL-F3 — Comparator-Quotient Token/Memory Coupling Audit",
 "\n\n" + A1C_BLOCK + "\n\n#### §6.16f CELL-F3 — Comparator-Quotient Token/Memory Coupling Audit"),
# ---------------- §7 import rows ----------------
("S7-note", "MNT", "§7 synchronization note: §7.1–§7.2 are summaries", "str", "live",
 r"the earlier comparisons are those of §7.1–§7.2.",
 r"the earlier comparisons are those of §7.1–§7.2 (summaries; the audit tables are at `" + PREV_TAG + r"`)."),
("S7-C21", "A1B", "§7 C21 row: A1b use", "str", "live",
 r"- [RID: DYAD-THM-C21] :: $\mu_6=c_{21}=-\tfrac12-i\tfrac{2\sqrt3}{3}$ :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.2, §6.7 :: return defect, jet-law anchor :: p=6, K=1, conditional on postulated $T$",
 r"- [RID: DYAD-THM-C21] :: $\mu_6=c_{21}=-\tfrac12-i\tfrac{2\sqrt3}{3}$ :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.2, §6.7 :: return defect, jet-law anchor; §6.13b RECOG-THM-A1B-SLIP-SCHEDULE-U (cubic coefficient of the six-step deficit; reproduced exactly by the A1b certificate, v0.3.24) :: p=6, K=1, conditional on postulated $T$"),
("S7-PRIMCTR", "A1B", "§7 PRIM-CTR row: A1b use", "str", "live",
 r":: Dyadic v6.4.10 §6.14 :: R8 entry target; contraction half of former R10 :: accepted; radius sufficient not optimal",
 r":: Dyadic v6.4.10 §6.14 :: R8 entry target; contraction half of former R10; §6.13b RECOG-THM-A1B-SLIP-SCHEDULE-U ($U_T$, $Q_m\le Q_0/(1+\tfrac12Q_0m)$; v0.3.24) :: accepted; radius sufficient not optimal"),
("S7-NFREM", "A1B", "§7 NF-REM row: A1b use of the ingredients", "str", "live",
 r":: Dyadic v6.4.10 §6.14 :: R9 budget, R8 hand-over :: accepted; rows not mixed; certificate values 85.07/27.60",
 r":: Dyadic v6.4.10 §6.14 :: R9 budget, R8 hand-over; §6.13b RECOG-THM-A1B-SLIP-SCHEDULE-U uses the ingredients only — raw-vector tail $|R^{\rm prim}_{\ge10,\rm vec}|\le332000|W|^{10}$ on $|W|\le\tfrac1{16}$ and the degree 7–9 vector ceilings $\tfrac{2079}{1000},\tfrac{577}{500},\tfrac{1763}{1000}$ (present at `dyad-v6.4.22` §6.14; v0.3.24) :: accepted; rows not mixed; certificate values 85.07/27.60"),
("S7-LPHASE", "A1B", "§7 LPHASE row A: A1b use", "str", "live",
 r":: §6.13b RECOG-THM-A1A-PHASE-EXISTENCE-U :: row A only; block base points in $U$, intermediate steps in $U_T$; primitive $Q_m$, not the chart $q$",
 r":: §6.13b RECOG-THM-A1A-PHASE-EXISTENCE-U; §6.13b RECOG-THM-A1B-SLIP-SCHEDULE-U (branch (B) for the $8$-gap exclusion; row A through the series tails; v0.3.24) :: row A only; block base points in $U$, intermediate steps in $U_T$; primitive $Q_m$, not the chart $q$"),
# ---------------- §7.1 / §7.2 maintenance ----------------
("M-71", "MNT", "§7.1: v0.3.18 audit table and OFN notices to history", "span", "live",
 ("Claim-level consumer audit of RECOG's dependencies on Number Genesis v1.20.6 → v1.20.7", "### §7.2 Owner Synchronization Audit (v0.3.21)"),
 "Historical audit (v0.3.18): claim-level consumer audit of RECOG's dependencies on Number Genesis v1.20.6 → v1.20.7 and OFN v0.7 → v0.8 (nine rows: NUMGEN L1, N1C, defect-threshold ratio and GAP-LOCK Lemma 3 identical; OFN §6.2a and §7.3 restructured; the R1 definition request answered conditionally by OFN v0.8 with OPEN-OFN-OPA; OFN comparator-typing definitions aligned), the consumer-direction note (IMP-O08-17 fulfilled by RECOG-DEF-COMPARATOR-POLE / -STATE) and the notices to the OFN owner of that date. Table and notes: `" + PREV_TAG + "` §7.1. Current owner editions and the current-source claim audit: the synchronization note above; current consumer state: §7.3.\n\n"),
("M-72", "MNT", "§7.2: v0.3.21 audit table and scope notes to history", "span", "live",
 ("Claim-level consumer audit of every load-bearing import, run on the exact owner files (G2).", "**Receipts of Dyadic notices**"),
 "Historical audit (v0.3.21, G2): claim-level consumer audit of every load-bearing import on the exact owner files — Dyadic v6.4.10 → v6.4.17 (18 rows), Genesis v2.8.4 → v2.8.9 (7), OFN v0.8 → v0.10 (6), RRF v0.6 → v0.8.3 (8); no changed statement (CST 0) in any row; identifier registrations and one narrowed Genesis branch-independence scope recorded. Table, classes and scope notes: `" + PREV_TAG + "` §7.2. The current-source claim audit (v0.3.23) is described in the synchronization note above.\n\n"),
# ---------------- §8 ----------------
("S8-A1B", "A1B", "§8 new artifact row: A1b certificate", "line", "live",
 r"- [RID: RECOG-ART-A1A-EXISTENCE-U] `[v0.3.23]`",
 "{LINE}\n" r"- [RID: RECOG-ART-A1B-SIXSTEP-DEFICIT] `[v0.3.24]` :: `recog_a1b_sixstep_deficit_cert.py` (sha256 `b418af086dfb7515faff5d266a7ea1d2e7f76efb74421021268c14495a1b35b0`) + output `evidence/recog/a1b_a1c/a1b_sixstep_deficit_cert.json` (`cc1f7e30def4defd8d8cb7af89aafe75b4207d3d6d0ab571e0ca20d78ce7c8f1`) :: exact six-step jet in $\mathbb Q(i\sqrt3)$ to degree 9; gates G1–G5 (cubic jet $=\mu$, quartic real ray $=$ Dyadic §6.2, Dyadic ceilings), G6–G8 (rational coefficient ceilings $H<\tfrac{1783}{1000}$, $\tau$ bracket, the three uniform inequalities: upper $1.8170<1.818$, lower $1.7876<1.788$, positivity $0.92725>0.927$), controls NC1–NC2; proof input of (C′) in RECOG-THM-A1B-SLIP-SCHEDULE-U. Illustration (`[NUM]`, not a proof input): `recog_a1b_a1c_explicit_u.py` (`cc964a51ee746f2cb6d8be6f85765fab8dd5766f212f097075e547d56b7be2c2`) + `a1b_a1c_explicit_u_2e6.json` (`0ea54e81cfbe7a9b528eb121aba054023ad0726fdcd85b4aec3f68f2fc988dcb`): 12 orbits, $2\times10^6$ steps, predicate–crossing mismatches $0$, alphabet $\{6,7\}$, $|\varepsilon_k|/\sqrt{Q_{M_k}}\le0.75$. Session cell `records/recog/RECOG_A1B_A1C_SESSION_v0_1.md` v0.2.2 (`205c68ef56e432bd98267efccaab3975b2daca7e94ca3bd545277b268c9feb23`); theorem candidate `records/recog/RECOG_A1B_THEOREM_CANDIDATE_v0_1.md` :: `[THM]` proof input (certificate) and `[NUM]` illustration"),
("S8-A3", "A3", "§8 new artifact row: A3 certificate", "str", "live",
 r"theorem candidate `records/recog/RECOG_A1B_THEOREM_CANDIDATE_v0_1.md` :: `[THM]` proof input (certificate) and `[NUM]` illustration",
 r"theorem candidate `records/recog/RECOG_A1B_THEOREM_CANDIDATE_v0_1.md` :: `[THM]` proof input (certificate) and `[NUM]` illustration" "\n"
 r"- [RID: RECOG-ART-A3-QUADRATURE-TYPING] `[v0.3.24]` :: `recog_a3_quadrature_typing.py` (sha256 `936d4c97950b53085b019411616324450a79b3c762b19a5688c06e53acb93e6b`) + output `evidence/recog/a3_quadrature/a3_quadrature_typing.json` (`65475ba57b48e17055b810dace404aaf964e194d79c2a63626fccd5965291e70`) :: exact sympy gates Q1–Q6 (Jacobian identities; unipotent shear on the quadrature; the three comparator-geometric identities and $S^*\Omega=\Omega$; the retyping charts $\varphi_A$, $\varphi_B$; the two-step trace on the quadrature; the pole-stratum inventory with symbolic $m,k$) and controls NC1 (constant linear chart preserves tr, det), NC2 ($\varepsilon=0$ reproduces the primitive unipotent); `[NUM]` Newton probe for periodic orbits ($n\le8$, $|L|\le2$, $\rho\in[-2.5,2.5]$): 18 orbits, of which $P_1$, $P_2$, the winding fixed points $k=1,2$ and the $m=1$ period-2 orbit are the exact ones, 11 further orbits uncertified; no sampled orbit has a point on the quadrature (no nonexistence claim). Session record `records/recog/RECOG_A3_QUADRATURE_TYPING_SESSION_v0_1.md` v0.2 (`262e2529a9288ddf56e1842f074a12bcaf66f43e96cc53f3cd12b939c1cd1d17`) :: `[ALG]` certificate (exact) and `[NUM]` sampled list"),
# ---------------- §9 ----------------
("S9-arch", "MNT", "§9 archive line", "str", "live",
 r"**Archive.** none yet; to be registered with the ontology note.",
 r"**Archive.** Records, notices and reviews: `records/recog/`; evidence: `evidence/recog/` (§8, repository locations). Earlier editions and their full history: the tags `recog-v<version>` (Appendix A)."),
# ---------------- Appendix A (new entry only) ----------------
("A-1", "MNT", "Appendix A: v0.3.24 draft entry", "str", "appA",
 "## Appendix A — Version History\n\nOne compact entry per edition",
 "## Appendix A — Version History\n\nOne compact entry per edition"),
]
# A-1 is a placeholder replaced below so that the Appendix A entry is assembled per variant.

APPA_ENTRY_HEAD = "### v0.3.24 — DRAFT, stage 1 (corrected intermediate; not adopted)\n"
APPA_LINES = {
 "A1B": r"- **New science, group A1b (separately reviewed):** RECOG-THM-A1B-SLIP-SCHEDULE-U (§6.13b) — on explicit $U$: B-events are lift crossings; six-step deficit $0.927\tau Q<\Delta<\tau Q+1.82Q^{3/2}$ on $U_T$ (exact rational certificate); return alphabet $\{6,7\}$ with logarithmic $7$-gap count; digamma slip schedule $\tau\psi(a+M_k)-(k-1)\tfrac\pi3=L+\varepsilon_k$ with explicit error ceiling; RECOG-ART-A1B-SIXSTEP-DEFICIT (§8); §7 import rows record the new uses (LPHASE row A and branch (B), NF-REM ingredients, PRIM-CTR, C21).",
 "A1C": r"- **New science, group A1c (separately reviewed):** RECOG-RESULT-A1C-RECORD-PHASE-READOUT (§6.16e) — the complete B-event record determines $\Psi_\infty$ mod $2\pi$, conditional on A1b; no carrier downgrade; OPEN R6 gains the sub-items A1c-Q1′ (injectivity of the record map) and A1c-decoder (unknown-$a$ / declared-data windows); §5 readout guard.",
 "A3": r"- **New science, group A3 (separately reviewed):** RECOG-ALG-QUADRATURE-TYPING (§6.5) — the pole-comparator quadrature is the extremal-radial-transfer locus and, relative to the declared Haar form $\Omega$, the area-neutral locus; its parabolic one-step type has no chart-free content (explicit retyping charts); RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY (§6.3) — complete wrapped-periodic inventory inside $\{\widehat C_{\rm pole}=\pm1\}$ with the new odd-$m$ period-2 family; RECOG-ART-A3-QUADRATURE-TYPING (§8). OPEN R4 sub-item 1 answered in reframed form; R4 stays ACTIVE.",
 "MNT": r"- **Structural maintenance (follow-up obligation of the v0.3.23 release record §11; separate acceptance):** current status at the point of use, history pointed to `recog-v0.3.23` — R8 and R9 v0.3.2 specifications (§2), the former R11 text with its `[OPEN]` sub-items (§2), the R7 heading over closed items (§2), the §7.1/§7.2 audit tables and the G2 \"unchanged\" sentence of §6.13b, §9 archive line. Layout reorder (SG order): stage 2.",
}
APPA_TAIL = (r"- **Unchanged:** every existing RID's statement and grade; every OPEN status (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED)." "\n"
             r"- **Records:** release record `records/recog/RECOG_v0_3_24_RELEASE_RECORD.md`; predecessor tag `recog-v0.3.23` (SHA-256 `0d583400…a31a`)." "\n\n")

NEW_RIDS = {
 "A1B": {"RECOG-THM-A1B-SLIP-SCHEDULE-U", "RECOG-ART-A1B-SIXSTEP-DEFICIT"},
 "A1C": {"RECOG-RESULT-A1C-RECORD-PHASE-READOUT"},
 "A3": {"RECOG-ALG-QUADRATURE-TYPING", "RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY", "RECOG-ART-A3-QUADRATURE-TYPING"},
 "MNT": set(),
}
GROUPS = ["A1B", "A1C", "A3", "MNT"]

def appa_edit(groups):
    new = "## Appendix A — Version History\n\nOne compact entry per edition (Methodology v1.4 §1). Full records of earlier editions — adoption metadata, draft-round records, review verdicts, the stacked status summaries and the freeze history — are in Appendix A and the header of v0.3.22 (tag `recog-v0.3.22`, SHA-256 `0dcce9e4…bcd9`). Scientific corrections and retired claims: Appendix B.\n\n" + APPA_ENTRY_HEAD
    new += "- **Basis:** PI decisions of 23–24 Oct 2026 (`START A1b/A1c`, `A3 AUTHORIZED`, `PREPARE A1B THEOREM CANDIDATE — APPROVED`, stage-1 preparation recommended by the receiving review #5638910665); co-owner reviews of PRs #23, #28, #30; the v0.3.23 release record §11 follow-up obligation. Each group below carries its own acceptance decision; three are scientific (A1b, A1c, A3) and one is structural maintenance.\n"
    for g in GROUPS:
        if g in groups: new += APPA_LINES[g] + "\n"
    new += APPA_TAIL + "### v0.3.23 — 23 October 2026 — Adopted"
    old = "## Appendix A — Version History\n\nOne compact entry per edition (Methodology v1.4 §1). Full records of earlier editions — adoption metadata, draft-round records, review verdicts, the stacked status summaries and the freeze history — are in Appendix A and the header of v0.3.22 (tag `recog-v0.3.22`, SHA-256 `0dcce9e4…bcd9`). Scientific corrections and retired claims: Appendix B.\n\n### v0.3.23 — 23 October 2026 — Adopted"
    return ("A-1", "ALL", "Appendix A: v0.3.24 draft entry (per variant)", "str", "appA", old, new)

def resolve(txt, mode, old, new):
    if mode == "line":
        lines = txt.split("\n")
        hits = [l for l in lines if l.startswith(old)]
        assert len(hits) == 1, f"expected 1 line starting with prefix, found {len(hits)}"
        return hits[0], new.replace("{LINE}", hits[0])
    if mode == "span":
        a, b = old
        assert txt.count(a) == 1 and txt.count(b) == 1, f"span anchors not unique ({txt.count(a)}, {txt.count(b)})"
        i, j = txt.index(a), txt.index(b)
        assert i < j, "span anchors out of order"
        return txt[i:j], new
    return old, new

def apply(s, edits):
    i = s.index(APPA_START); j = s.index(APPA_END)
    live = s[:i] + "\x00APPA\x00" + s[j:]
    appa = s[i:j]
    record = []
    for k, grp, loc, mode, region, old, new in edits:
        txt = live if region == "live" else appa
        old_full, new_full = resolve(txt, mode, old, new)
        n = txt.count(old_full)
        assert n == 1, f"{k}: expected 1 match, found {n}"
        assert old_full != new_full, f"{k}: no-op edit"
        txt = txt.replace(old_full, new_full)
        if region == "live": live = txt
        else: appa = txt
        record.append({"key": k, "group": grp, "location": loc, "mode": mode, "region": region,
                       "old_sha256": hashlib.sha256(old_full.encode()).hexdigest(),
                       "new_sha256": hashlib.sha256(new_full.encode()).hexdigest(),
                       "old": old_full, "new": new_full})
    assert live.count("\x00APPA\x00") == 1
    return live.replace("\x00APPA\x00", appa), record

def main(argv):
    base, out, log = argv[1:4]
    groups = set(GROUPS)
    if "--only" in argv:
        groups = set(argv[argv.index("--only") + 1].split(","))
        assert groups <= set(GROUPS), groups
    raw = open(base, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, "base is not adopted v0.3.23 (tag recog-v0.3.23)"
    s = raw.decode("utf-8")
    edits = [e for e in EDITS if e[0] != "A-1" and e[1] in groups]
    keys = [e[0] for e in EDITS]
    assert len(keys) == len(set(keys)), "duplicate edit keys"
    # the S8-A3 row is appended to the S8-A1B row; without A1B it attaches to the FC-21 row instead
    if "A3" in groups and "A1B" not in groups:
        edits = [e for e in edits if e[0] != "S8-A3"]
        a3row = [e for e in EDITS if e[0] == "S8-A3"][0][6].split("\n", 1)[1]
        edits.append(("S8-A3", "A3", "§8 new artifact row: A3 certificate (variant without A1B)", "line", "live",
                      r"- [RID: RECOG-ART-A1A-EXISTENCE-U] `[v0.3.23]`", "{LINE}\n" + a3row))
    edits.append(appa_edit(groups))
    t, record = apply(s, edits)
    data = t.encode("utf-8")
    open(out, "wb").write(data)
    new_rids = sorted(set().union(*(NEW_RIDS[g] for g in groups)))
    json.dump({"base_sha256": BASE_SHA, "base_tag": PREV_TAG, "groups": sorted(groups),
               "intermediate_sha256": hashlib.sha256(data).hexdigest(),
               "declared_new_recog_rids": new_rids, "edit_count": len(record), "edits": record},
              open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits", "groups:", ",".join(sorted(groups)))

if __name__ == "__main__":
    main(sys.argv)
