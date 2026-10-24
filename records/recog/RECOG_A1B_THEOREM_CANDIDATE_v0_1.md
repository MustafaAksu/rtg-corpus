# RECOG — Theorem candidate `RECOG-THM-A1B-SLIP-SCHEDULE-U` (registration draft)

**Date:** 24 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` **candidate record** for the next RECOG stage-1 item, **v0.2.1** (v0.1 at commit `79e6e6b`; v0.2 at `9777685`; v0.2.1: two A1c sentences aligned with the stage-1 review #5639519847 of PR #35; revised after review #5638820480: `THM ACCEPTED — A1C RESULT NEEDS LIMITED CORRECTIONS`; dispositions in §7). PI decision of 24 Oct 2026: `PREPARE A1B THEOREM CANDIDATE — APPROVED` (preparation only: no DSN change, no RID adoption, no release). Review basis: co-owner reviews of PR #23 — #5630982748 (round 1), #5631395296 (round 2), #5634312954 (A1b proof cell ACCEPTED; theorem candidate may be submitted for registration and adoption review).
**Governing edition:** `recog-v0.3.23` (DSN SHA-256 `0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a`). Producer: Dyadic `dyad-v6.4.22`. NUMGEN `numgen-v1.20.8` (custody only).
**Source cell:** `records/recog/RECOG_A1B_A1C_SESSION_v0_1.md` v0.2.2 at commit `1ef20de` on `claude/recog-a1b-a1c` (PR #23), SHA-256 `205c68ef56e432bd98267efccaab3975b2daca7e94ca3bd545277b268c9feb23` (v0.2.1 at `7acdaca`, `ae3ae4ed…98c5`, differs only in the §4 sentence corrected per §7 below; the proofs and certificates are unchanged). This record restates that cell's proved content in registration form; it adds no new mathematics. Where the two differ, the cell's proofs govern and this record is to be corrected.

---

## 1. Proposed DSN text (for §6.13b, after RECOG-THM-A1A-PHASE-EXISTENCE-U)

**Slip schedule on explicit $U$ (A1b).** `[THM]` [RID: RECOG-THM-A1B-SLIP-SCHEDULE-U] [scope: conditional on postulated $T$ (OPEN-P0); $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$; lifted primitive chart, frame $W=\rho+\omega\eta$, increasing lift $\hat\varphi$ with principal one-step increments $\delta_T$; token conventions of §6.16a (F2(b)); block count $M$, $a:=Q_0^{-1}$] [proof: session cell `records/recog/RECOG_A1B_A1C_SESSION_v0_1.md` §2, Lemmas A, B, C′ and Proposition; certificate `recog_a1b_sixstep_deficit_cert.py`, exact rational gates G6–G8] 

Let $n_0<n_1<\cdots$ be the anchors of the canonical B-events of the orbit ($\eta(x_n)<0\le\eta(x_{n+1})$, $\rho>0$ on both sides; anchor $=n+1$), $g_{j+1}=n_{j+1}-n_j$ the return gaps, and $M_k$ the block index of the $k$-th gap equal to $7$ ($n_{j_k}=6M_k+r_k$, $0\le r_k\le5$). Then for every $x_0\in U$:

(A) *Events are lift crossings.* $x_n\to x_{n+1}$ is a canonical B-event iff $\lfloor\hat\varphi_{n+1}/2\pi\rfloor=\lfloor\hat\varphi_n/2\pi\rfloor+1$.

(C′) *Six-step deficit.* For every $y\in U_T$, with $\Lambda_6(y)$ the six-step lift increment from $y$ and $\Delta(y):=2\pi-\Lambda_6(y)$:
$$\Delta(y)>0.927\,\tau Q(y)>0,\qquad|\Delta(y)-\tau Q(y)|<1.82\,Q(y)^{3/2}.$$

(B) *Alphabet.* Every gap is $6$ or $7$; the number $s(M)$ of $7$-gaps among the returns in the first $6M$ steps satisfies $s(M)=\tfrac{3\tau}{\pi}\log M+O(1)\to\infty$.

(S) *Schedule.* With $\psi$ the digamma function and
$$L(x_0):=\tfrac\pi3n_0-2\pi\ell_0+\Psi_{W,\infty}(x_0),\qquad \ell_0=\lfloor\hat\varphi_{n_0}/2\pi\rfloor,$$
$$\tau\,\psi(a+M_k)-(k-1)\tfrac\pi3=L+\varepsilon_k,\qquad |\varepsilon_k|\le\tau Q+1.82\,Q^{3/2}+5\arcsin\bigl(0.705\sqrt Q+0.257\,Q\bigr)+\tau\,|S^{\rm tail}_{M_k}|+|R^{\rm tail}_{M_k}|,$$
where $Q$ is the largest primitive amplitude among the points of the $k$-th slip block and $S^{\rm tail}_M=\sum_{m\ge M}(Q_m-\tfrac1{a+m})$, $R^{\rm tail}_M=\sum_{m\ge M}r_m$ are the tails of the FC-21 series; $|\varepsilon_k|=O(\sqrt{Q_{M_k}})=O((a+M_k)^{-1/2})$. Consequently $\tau\log M_k-(k-1)\tfrac\pi3=L-\tau\log(1+a/M_k)+O(M_k^{-1})+\varepsilon_k\to L$ and $M_{k+1}/M_k\to e^{\pi/(3\tau)}$.

Depends on: RECOG-THM-A1A-PHASE-EXISTENCE-U (existence of $\Psi_{W,\infty}$; the series and their tails; $C_D^{\rm ext}=\Theta_W(0)-\Psi_{W,\infty}$); RECOG-THM-A1A-PHASE-EXISTENCE-ALT; RECOG-THM-A1A-LIFT-ALIGNMENT ($\tfrac\pi6<\delta_T<\tfrac\pi2$ on $U_T$; six-step totals in $(\pi,3\pi)$); RECOG-THM-A1A-RECIPROCAL-AMPLITUDE; [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 | DYAD-THM-LPHASE-ROWA-REMAINDER] (branch (B): $|W(Ty)/(\lambda W(y))-1|\le0.04654$ on $U_T$; row A remainder $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$); [import: same §6.14 | DYAD-THM-NF-REM ingredients] (raw-vector tail $|R^{\rm prim}_{\ge10}|\le332000|W|^{10}$ on $|W|\le\tfrac1{16}$; vector ceilings for $F_7,F_8,F_9$ used as a cross-check only); [import: DYAD-THM-PRIM-CTR] ($U_T$, $Q_m\le Q_0/(1+\tfrac12Q_0m)$); [import: DYAD-THM-C21] (six-step cubic coefficient $\mu$, reproduced exactly by the certificate); RECOG-DEF-EVENT-TOKEN-SCHEMA / §6.16a F2(b) conventions. Token predicate and the slip-law wording: NUMGEN GAP-LOCK (custody unchanged; this is an explicit-domain instance, see §4).

*Proof sketch (full proofs in the cell).* (A): on $U_T$ the sign of $\eta$ and the lift crossing are tied by $\eta'-\eta=e^\rho-1-\sin\eta$ and the branch bound, exactly. (C′): the six-step map in $W$ is $W+\mu|W|^2W+\sum_{d=4}^9F_d+R_{\ge10}$ with $F_d$ computed exactly in $\mathbb Q(i\sqrt3)$; $\Lambda_6=2\pi+\operatorname{Arg}(W(T^6y)/W(y))$ (lift alignment), so $\Delta=-\operatorname{Arg}(1+\mu Q+E)$ with $|E|\le e(Q)\le H\,Q^{3/2}$, $H<\tfrac{1783}{1000}$ by rational coefficient ceilings; the elementary arctan bounds give the two displayed inequalities uniformly on $U_T$ (certificate gates G6–G8, exact rationals, $\tau$ bracketed). (B): a gap $\ge8$ needs $\Lambda_7(x_{n_j})<2\pi-o_j\le2\pi$, impossible since $\Lambda_7>\tfrac{7\pi}3-7\arcsin0.04654>2\pi$ by (B); a gap $\le5$ needs $o_j+\Lambda_5(x_{n_j})\ge2\pi$, impossible since $o_j<\delta_T(x_{n_j-1})$ gives $o_j+\Lambda_5(x_{n_j})<\Lambda_6(x_{n_j-1})<2\pi$ by (C′) at the pre-anchor point; the count law follows from (A) and FC-21 ($D_M=\tau\log M+O(1)$). (S): the exact event identity $G_{n_j}=C+\tfrac\pi3s_j-o_j$, $C=\tfrac\pi3n_0-2\pi\ell_0+\hat\varphi_0$, with $0\le o_{j_k}<\Delta_{j_k}$ at a $7$-gap anchor; the partial-block correction is bounded by the pointwise one-step bound $|\delta_T-\tfrac\pi3|\le\arcsin(0.705\sqrt Q+0.257Q)$; FC-21's finite-block identity $D_M=C_D^{\rm ext}+\tau\psi(a+M)-\tau S^{\rm tail}_M+R^{\rm tail}_M$ converts $D_{M_k}$ into the digamma form; $\hat\varphi_0$ cancels between $C$ and $C_D^{\rm ext}$. $\square$

**Not supplied:** anything outside $U$; a bound on $\varepsilon_k$ computable from $(a,k,M_k)$ alone (the tails and the block maximum $Q$ are a-priori quantities; a uniform majorant via $Q_m\le Q_0/(1+\tfrac12Q_0m)$ is listed as open); any decoding of $a$ from a finite record; any statement about $M_W$, $M(z_0)$ or an event/WRITE mechanism; any change to NUMGEN's adopted domain or grades; any Dyadic grade or domain change. `[NUM]` illustration, not a proof input: `recog_a1b_a1c_explicit_u.py` (12 orbits, $2\times10^6$ steps; predicate–crossing mismatches $0$, alphabet $\{6,7\}$, $|\varepsilon_k|/\sqrt{Q_{M_k}}\le0.75$; SHA-256 script `cc964a51ee746f2cb6d8be6f85765fab8dd5766f212f097075e547d56b7be2c2`, output `0ea54e81cfbe7a9b528eb121aba054023ad0726fdcd85b4aec3f68f2fc988dcb`).

**Scope and custody.** (i) GAP-LOCK Lemmas 1–3 and INF-1 remain NUMGEN's; the statement above is an explicit-$U$ consequence of RECOG and Dyadic inputs and is registered under RECOG identity, as FC-21 was; NUMGEN is informed, no custody changes. (ii) No Dyadic certified domain is widened; the six-step jet is recomputed, not imported, and agrees with DYAD-THM-C21 and the §6.2 quartic real-ray value. (iii) $L$ depends on the start state through $n_0,\ell_0,\Psi_{W,\infty}$; it is not universal. (iv) Separation (SG-R6, C2): the theorem counts crossings of a declared section; it defines no physical event, no token WRITE and no memory carrier; R6 is untouched.

---

## 2. Separate result (proposed, §6.16e after F2(d)) — infinite-record phase readout

`[RESULT]` `[from: THM]` [RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT] [scope: $x_0\in U$; the complete infinite token record $\mathcal R(x_0)=(n_0;g_1g_2\ldots)$ in the F2(b) conventions] The record determines $L(x_0)=\lim_k[\tau\log M_k-(k-1)\tfrac\pi3]$ and hence $\Psi_{W,\infty}(x_0)=\Psi_{z,\infty}(x_0)$ modulo $2\pi$, without any state datum and without the value of $a$. The schedule limit $L$ alone provides no reconstruction of $a$, $M_W$ or $M(z_0)$; this is a statement about the available method, not a non-recoverability theorem (the injectivity question A1c-Q1′ below is open). For a finite prefix of $k$ slips with $a$ known, $L$ lies in a window of width $2|\varepsilon_k|$ (a-priori envelope, not a record-only decoder interval), and this envelope tends to $0$ as $k\to\infty$; with $a$ unknown no window is derived (`[NUM]` only: least-squares $(\hat a,\hat L)$, relative error $\le3.5\%$ on the illustration runs, no guarantee). Reading for F2(d): $\Psi_\infty$ is a function of the complete token history ($R_{\log}$-type in the limit); no general statement about finite prefixes is made — the illustration's figure "$\approx2$–$6\times|\Delta M|$" (cell §5) is the absolute error of the fitted *record-only pair decoder* on four sampled comparator-fiber pairs at $N=2\times10^6$ steps, a `[NUM]` decoder-error measurement and not a bound on the finite-prefix window (stage-1 review #5639519847, A1C-1; v0.2.1); the $R_{\rm ind}$ classification of R9's carrier $M$ is **not** lowered by this result, nor would it be by a positive answer to the injectivity question below (retrospective reconstruction is not write-through; SG-R6). Depends on: RECOG-THM-A1B-SLIP-SCHEDULE-U (same release; hence `Depends on:` rather than `[assuming:]`, Methodology v1.4 §3.4); RECOG-THM-A1A-PHASE-EXISTENCE-ALT ($\Psi_{z,\infty}=\Psi_{W,\infty}$).

**Proposed OPEN sub-items (under OPEN R6, RECOG-OPEN-EVENT-RULE, in the §2 OPEN Registry):**
- `[OPEN]` A1c-Q1′ — injectivity of $x_0\mapsto\mathcal R(x_0)$ on $U$. Neither answer is established; the cell's empty-interior remark is a `[SESSION]` conjectural observation with an open local-nonconstancy proof obligation on all of $U$ (review #5639519847, A1C-2). Either answer has a stated consequence (cell §3); neither affects the carrier classification.
- `[OPEN]` A1c-decoder — a finite-prefix window for $(a,L)$ with $a$ unknown, and a record-only (declared-data) majorant for the known-$a$ window via $Q_m\le Q_0/(1+\tfrac12Q_0m)$ and the FC-21 tail estimates.

Not proposed for registration: the comparator-fiber $\Delta M$ numerics (cell §3, `[NUM]` outside the certified R9 window) and the long-orbit pair-cancellation experiment (deferred).

---

## 3. Certificates and hashes (cell at `1ef20de`; certificates unchanged since `7acdaca`)

| Item | Path | SHA-256 | Role |
|---|---|---|---|
| Session cell v0.2.2 | `records/recog/RECOG_A1B_A1C_SESSION_v0_1.md` | `205c68ef56e432bd98267efccaab3975b2daca7e94ca3bd545277b268c9feb23` | proofs; dispositions §7/§7b/§7c |
| Six-step deficit certificate | `evidence/recog/scripts/recog_a1b_sixstep_deficit_cert.py` | `b418af086dfb7515faff5d266a7ea1d2e7f76efb74421021268c14495a1b35b0` | (C′): exact jet, G1–G8, NC1–NC2 |
| Certificate output | `evidence/recog/a1b_a1c/a1b_sixstep_deficit_cert.json` | `cc1f7e30def4defd8d8cb7af89aafe75b4207d3d6d0ab571e0ca20d78ce7c8f1` | $H=1.78218$, bounds $1.8170/1.7876/0.92725$ |
| Illustration script | `evidence/recog/scripts/recog_a1b_a1c_explicit_u.py` | `cc964a51ee746f2cb6d8be6f85765fab8dd5766f212f097075e547d56b7be2c2` | `[NUM]` only |
| Illustration output | `evidence/recog/a1b_a1c/a1b_a1c_explicit_u_2e6.json` | `0ea54e81cfbe7a9b528eb121aba054023ad0726fdcd85b4aec3f68f2fc988dcb` | `[NUM]` only |

Certificate gates (all PASS): G1 cubic jet $=\mu$, degree 2 vanishes; G2 quartic real-ray $-(5+25i\sqrt3)/48$ = Dyadic §6.2; G3 $\sup e/(\tau Q)=0.0725$ (illustration); G4 grid value $K=1.8162$ (illustration only); G5 $c_7,c_8,c_9$ within Dyadic ceilings; **G6** rational coefficient ceilings, $H<\tfrac{1783}{1000}$; **G7** $\tau$ bracket; **G8** the three uniform inequalities ($<1.818$, $<1.788$, $>0.927$); NC1 conjugate $\mu$ caught; NC2 tail $\times10^8$ caught. Published constants: $K=1.82$, $\Delta>0.927\tau Q$. Proposed artifact RID: `RECOG-ART-A1B-SIXSTEP-DEFICIT` (§8 census).

Explicit constants used in the statement and where they come from: $0.04654$ (Dyadic (B)); $\tfrac{403}{250}$ (Dyadic row A); $332000$ (Dyadic tail); $0.705,\ 0.257$ (one-step pointwise bound, cell §2: $|\eta-\sin\eta|\le|\eta|^3/6$, $|e^\rho-1-\rho|\le\tfrac{\rho^2}2e^{|\rho|}$, $|\rho|,|\eta|\le\tfrac2{\sqrt3}|W|$); $0.927,\ 1.82$ (certificate G8); $\tau=2/\sqrt3$.

---

## 4. Notices and consumers (prepared for the PI; separate states)

| Recipient | Kind | Content | State |
|---|---|---|---|
| NUMGEN | informational | explicit-$U$ instance of the GAP-LOCK slip law with identified constant $L$ and error order; no custody change; NUMGEN's adopted domain/grade untouched | to prepare after adoption |
| Dyadic | use notice | new RECOG uses of DYAD-THM-LPHASE-ROWA-REMAINDER (branch (B)), DYAD-THM-NF-REM tail ceiling, DYAD-THM-PRIM-CTR, DYAD-THM-C21; the certificate reproduces C21/§6.2 values (a free cross-check for Dyadic, not a Dyadic RID) | to prepare after adoption |
| RRF | none | no profile or representation change (W-frame, lifted chart, as registered) | — |
| Atlas | row update | R6 open sub-items; new THM/RESULT rows; census | at release |

---

## 5. Placement and census (for the stage-1 build)

- §6.13b: insert the THM block of §1 after RECOG-THM-A1A-PHASE-EXISTENCE-U and its "Scope and custody" paragraph; add one line to the §6.13b status summary.
- §6.16e: insert the RESULT block of §2 after F2(d); the F2(d) finite-versus-limit qualifier as stated.
- §2 OPEN Registry, OPEN R6 (RECOG-OPEN-EVENT-RULE): add the two `[OPEN]` sub-items under "Active sub-items"; R6 stays ACTIVE; no other OPEN status changes. (§7 is the Import Ledger: it receives the consumer-use rows below, not the OPEN items.)
- §8 census: `RECOG-ART-A1B-SIXSTEP-DEFICIT` with the two hashes; the illustration listed as `[NUM]`.
- §7 Import Ledger / claim tables: consumer-use rows for the four Dyadic RIDs.
- Not in this item: A3's two `[ALG]` RIDs (separate scientific review item of the same release); the v0.3.23 live-file cleanup (maintenance item of the same release, per the PI's grouping).

---

## 6. Review checklist for the receiving reviewer

1. The THM text of §1 against the cell's Lemmas A, B, C′ and Proposition (no strengthening in transit; in particular the $\varepsilon_k$ bound names the block maximum $Q$ and the two tails).
2. The dependency list: every constant has an owner RID or a cell derivation; nothing imported from NUMGEN beyond conventions and custody.
3. "Not supplied" and "Scope and custody" against the round-2 refinements (a-priori envelope; no carrier downgrade; SG-R6).
4. The RESULT of §2: `[from: THM]` with `Depends on:` the same-release THM; the finite-prefix comparison scoped to the illustration horizon; the two OPEN sub-items worded as questions.
5. Hashes of §3 against `git show 1ef20de:<path> | sha256sum` (cell) and `git show 7acdaca:<path> | sha256sum` (certificates).

Nothing in this record is adopted. The PI decides registration at the stage-1 review of the next release.

---

## 7. Review round 1 — dispositions (review #5638820480 on `79e6e6b`: `THM ACCEPTED — A1C RESULT NEEDS LIMITED CORRECTIONS`)

| Review point | Disposition in v0.2 |
|---|---|
| (A), (C′), (B), (S) accepted; THM scope accepted | §1 unchanged |
| finite-prefix sentence "every finite prefix leaves a window $\gg|\Delta M|$" not true in general (envelope $\to0$) | replaced: envelope $\to0$ as $k\to\infty$ stated; the $|\Delta M|$ comparison scoped to the illustration's observed horizon as `[NUM]`; same sentence corrected in the source cell (v0.2.2, PR #23) |
| $L$ gives no reconstruction method, but this is not a non-recoverability theorem; Q1′ open | reworded accordingly |
| same-release A1b: `Depends on:` instead of `[assuming:]` | done (Methodology v1.4 §3.4) |
| R6's OPEN record is in §2, not §7 | placement corrected (§2 OPEN Registry for the sub-items; §7 Import Ledger for consumer-use rows) |
| no certificate rerun needed | none performed |

