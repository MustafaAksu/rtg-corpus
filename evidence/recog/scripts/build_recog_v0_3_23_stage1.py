#!/usr/bin/env python3
"""RECOG v0.3.23, stage 1: corrected intermediate (a build stage, not an edition).

Applies the accepted rows of the two owner dispositions of the atlas advisory
(records/recog/ATLAS_ADVISORY_RECOG_v0_3_22.md; reconciliation and PI decisions of 23 Oct 2026 in
records/recog/ATLAS_ADVISORY_RECOG_v0_3_22_DISPOSITION_RECONCILIATION.md §5), the extra stage-1 items
(R10 wording, Dyadic v6.4.21+ tag forms, line pins -> RID + section, erratum E-0322-1, RF-1, VF-1) and,
as a separately marked group, the FC-21 science block, to the adopted v0.3.22 file.

Rules:
- every edit is assertion-gated: its old text must occur exactly once in its region;
- region "live": Appendix A (version history) is masked, so history is never edited;
  region "appA": the edit applies inside Appendix A (only the new v0.3.23 entry);
- mode "line": old is a prefix that must start exactly one line; the whole line is replaced
  ("{LINE}" in new stands for the original line);
- group "FC21" edits are the new-science block; --without-fc21 builds the maintenance-only
  intermediate (decoupling rule of the PI decision);
- no layout moves (FA-01 compaction is stage 2); header identity lines, status summaries and the
  footer are not touched here.

usage: build_recog_v0_3_23_stage1.py BASE OUT EDITLOG_JSON [--without-fc21]
  BASE = `git show recog-v0.3.22:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`
"""
import hashlib, json, sys

BASE_SHA = "0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9"
APPA_START = "## Appendix A — Version History"
APPA_END = "## Appendix B —"

FC21_BLOCK = r"""**R9-free existence on all of $U$ (v0.3.23; new science, separately reviewed).**

`[THM]` [RID: RECOG-THM-A1A-PHASE-EXISTENCE-U] [scope: conditional on postulated $T$; $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$; block base points $x_m=T^{6m}x_0$, $Q_m=Q(x_m)$, $a:=Q_0^{-1}$; $N$ is the block count] [proof: written below; proof cell `records/recog/RECOG_v0_3_23_FC21_PROOF_CELL.md`] For every $x_0\in U$, H-NG holds, and
$$C_D^{\rm ext}(x_0)=\lim_N\bigl(D_N^U-\tau\log N\bigr)=\tau H(a)+\tau\sum_{m\ge0}\Bigl(Q_m-\frac1{a+m}\Bigr)-\sum_{m\ge0}r_m,\qquad H(a)=-\log a+\sum_{m\ge0}\Bigl[\frac1{a+m}-\log\Bigl(1+\frac1{a+m}\Bigr)\Bigr]=-\psi(a),$$
with all three series absolutely convergent, $\psi$ the digamma function and $r_m$ the row-A block remainders below. Consequently (RECOG-THM-A1A-PHASE-EXISTENCE-ALT) $\Psi_{W,\infty}$ and $\Psi_{z,\infty}$ exist, $\Psi_{z,\infty}=\Psi_{W,\infty}=\Theta_W(0)-C_D^{\rm ext}$ and $C_D^{\rm ext}=\tau\log Q_0-M_W$. RECOG-THM-R9-MEMORY and NUMGEN INF-1 are not used. Depends on: [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.19) | DYAD-THM-LPHASE-ROWA-REMAINDER] (row A; block base points in $U$, intermediate steps in $U_T$; not conditional on R9): $\hat\varphi_{6(m+1)}-\hat\varphi_{6m}=2\pi-\tau Q_m+r_m$, $\lvert r_m\rvert\le\tfrac{403}{250}Q_m^{3/2}$, where $\hat\varphi$ is the increasing lift with principal one-step increments $\delta_T$ and $Q_m$ is the primitive amplitude (Dyadic interface I1–I5); RECOG-THM-A1A-LIFT-ALIGNMENT; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE; DYAD-THM-PRIM-CTR; RECOG-THM-A1A-PHASE-EXISTENCE-ALT.
*Proof.* (1) *Same lift and clock.* On $U_T$, $\tfrac\pi6<\delta_T<\tfrac\pi2$ (RECOG-THM-A1A-LIFT-ALIGNMENT), so the increasing lift of $\arg W$ in $D_N^U$ is Dyadic's $\hat\varphi$, sampled at the same block base points $x_m\in U$ ($F(U)\subset U$). Telescoping, $D_N^U=\sum_{m<N}\bigl[2\pi-(\hat\varphi_{6(m+1)}-\hat\varphi_{6m})\bigr]=\sum_{m<N}(\tau Q_m-r_m)$. (2) *Remainders.* $Q_m\le Q_0/(1+\tfrac12Q_0m)\le\min(Q_0,\tfrac2m)$ (DYAD-THM-PRIM-CTR), so $\sum_m\lvert r_m\rvert\le\tfrac{403}{250}\sum_mQ_m^{3/2}<\infty$. (3) *Amplitudes.* By RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, $Q_m^{-1}=a+m+e_m$ with $\lvert e_m\rvert<\tfrac{15}2\sum_{k<m}\sqrt{Q_k}=O(\sqrt m)$; hence $Q_m-\tfrac1{a+m}=-\tfrac{e_mQ_m}{a+m}=O(m^{-3/2})$. (4) *Harmonic part.* Since $\sum_{m<N}\log(1+\tfrac1{a+m})=\log\tfrac{a+N}a$, $\sum_{m<N}\tfrac1{a+m}-\log N=\sum_{m<N}\bigl[\tfrac1{a+m}-\log(1+\tfrac1{a+m})\bigr]-\log a+\log\tfrac{a+N}N\to H(a)$, the bracket being $O((a+m)^{-2})$; the limit equals $-\psi(a)$. Writing $\tau\sum_{m<N}Q_m-\tau\log N=\tau\sum_{m<N}(Q_m-\tfrac1{a+m})+\tau(\sum_{m<N}\tfrac1{a+m}-\log N)$ and adding (2)–(4) gives the limit (H-NG) and the series. RECOG-THM-A1A-PHASE-EXISTENCE-ALT, whose proof uses neither R9 nor INF-1, gives the rest. $\square$
**Not supplied:** $c_{\rm iso}$, $\Lambda_1$, $C_2$, memory coefficients or remainders without R9; an R9-free OPEN 21 or form of (c); the chart-variable form $\tau\log q_0+D_\Theta(z_0)-M(z_0)$ of (b) without R9; RECOG-THM-R9-COMPARATOR-INCOMPLETENESS; starts in $U_T\setminus U$; any extension of NUMGEN's adopted domain or grade; any physical memory, token or event mechanism. RECOG-RESULT-A1A-PHASE-EXISTENCE-NG and RECOG-RESULT-A1A-CD-AGREEMENT are unchanged as the NUMGEN-route records; RECOG-THM-A1A-CD-IDENTIFICATION keeps its R9 route. `[NUM]` illustration, not a proof input: RECOG-ART-A1A-EXISTENCE-U (§8)."""

# (key, group, advisory row, location, mode, region, old, new)
EDITS = [
# ---------------- header: pins and erratum (identity lines untouched) ----------------
("H-1", "M", "FB-11", "header companions: Dyadic pin and current counterpart", "str", "live",
 r"`RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` (adopted 24 Sep 2026; source pin of all Dyadic imports below;",
 r"`RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` (adopted 24 Sep 2026; source pin of the Dyadic imports below unless a row names another edition; current tagged counterpart `dyad-v6.4.22` (`2363ca40…8c29`), quoted statements present at the cited RIDs in the current source (claim audit v0.3.23, §7);"),
("H-2", "M", "FB-11", "header companions: A1a Dyadic pins", "str", "live",
 r"the A1a cell §6.13b pins its Dyadic imports to v6.4.16 and, for OPEN 21 and the primitive-variable form, to adopted v6.4.18 `f70308f1…458d`, source-checked for that use)",
 r"the A1a cell §6.13b cites its Dyadic imports by RID and section at `dyad-v6.4.22`, with producer editions named at the rows; the A1a-E2 source check of v6.4.18 `f70308f1…458d` is kept as historical evidence)"),
("H-3", "M", "FA-02", "header companions: NUMGEN repin", "str", "live",
 r"`RTG_NUMBER_GENESIS_DSN_v1.20.7` (sha256 `c4637e7a…ab28`; claim-level synchronized v0.3.18, §7.1; the $D_M$ definition and INF-1 are imported by §6.13b as `RID unavailable`; dedicated RID decided by the NUMGEN owner (reply v0.1 `184a74fc…5227`; co-owner ruling of 20 Oct 2026 approving the allocation); string to be fixed in NUMGEN v1.20.8; responsible owner NUMGEN; A1a-G1 allocation resolved, canonical repin pending NUMGEN v1.20.8)",
 r"`RTG_NUMBER_GENESIS_DSN_v1.20.8` (tag `numgen-v1.20.8`, sha256 `835a56f8…7e2f`; quoted statements present at the cited RIDs in the current source (claim audit v0.3.23, §7); §6.13b imports the $D_M$ definition and INF-1 by their owner RIDs `NUMGEN-DEF-N5AS1-DEFECT` and `NUMGEN-RESULT-N5AS1-INF1`; A1a-G1 closed; earlier pin v1.20.7 `c4637e7a…ab28`, claim-level synchronized v0.3.18, §7.1)"),
("H-4", "M", "FA-05", "header companions: RRF current edition", "str", "live",
 r"`RTG_RRF_REPRESENTATION_REGISTRY_v0.8.3` (`b393657e…a187`; convention/registry reference only, synchronized v0.3.21, §7.2)",
 r"`RTG_RRF_REPRESENTATION_REGISTRY_v0.8.3` (`b393657e…a187`; convention/registry reference only, synchronized v0.3.21, §7.2; current v0.8.4 `2fb0a0fe…afce`, a consumer of RECOG, §7.3)"),
("H-5", "M", "FA-06", "header companions: methodology", "str", "live",
 r"(reference only, no import) · `DSN_METHODOLOGY_v1.3`",
 r"(reference only, no import) · `DSN_METHODOLOGY_v1.4`"),
("H-6", "M", "FA-06", "header methodology field", "str", "live",
 r"**DSN Methodology:** DSN_METHODOLOGY_v1.3 (current adopted edition; `RECOG | RTG Relational Recognition` confirmed in its namespace registry)",
 r"**DSN Methodology:** DSN_METHODOLOGY_v1.4 (tag `methodology-v1.4`, sha256 `cdacab5f…f2df`; `RECOG | RTG Relational Recognition` in its namespace registry; v0.3.22 was adopted under v1.3)"),
("H-7", "M", "FA-06", "header programme tier: registry edition", "str", "live",
 r"DSN_METHODOLOGY_v1.3 namespace registry",
 r"DSN_METHODOLOGY_v1.4 namespace registry"),
("H-8", "M", "E-0322-1", "header freeze status: stale qualifier of the v0.3.21 clause", "str", "live",
 r"release record `RECOG_v0_3_21_RELEASE_RECORD.md`); current authoritative edition, not frozen (a freeze is a separate decision).",
 r'release record `RECOG_v0_3_21_RELEASE_RECORD.md`); prior adopted edition, historical, not frozen (erratum E-0322-1: v0.3.22 carried the stale qualifier "current authoritative edition" here).'),
# ---------------- §1 ----------------
("S1-1", "M", "FB-12", "§1 candidate strata: INTERSECTION tag", "str", "live",
 r"`[OPEN]` [RID: RECOG-OPEN-INTERSECTION] Recognition event",
 r"`[HYP]` [RID: RECOG-OPEN-INTERSECTION] (registered under OPEN R6; the word OPEN in the RID is identity text, not status) Recognition event"),
("S1-2", "M", "FB-12", "§1 resonant-return: authoritative statement pointer", "str", "live",
 r"then $LG_k=G_k\circ L$ (from $F\circ F^p=F^p\circ F$).",
 r"then $LG_k=G_k\circ L$ (from $F\circ F^p=F^p\circ F$; authoritative statement and proof §6.12)."),
("S1-3", "M", "FB-15", "§1 resonant-return: frame scale", "str", "live",
 r"for $p=5\ldots12$, and $6\bar\lambda\nu_3(\zeta_6)=3\mu_6^{W}$.",
 r"for $p=5\ldots12$, and $6\bar\lambda\nu_3(\zeta_6)=3\mu_6^{W}$ (the $p=6$ case of the frame scale DYAD-ALG-KP-FRAME-SCALE; $\nu_3$ and $\mu_p$ here are $Z$-frame quantities)."),
("S1-4", "M", "FB-13", "§1 resonant-return: radial identity as named sub-statement", "str", "live",
 r"`[ALG]` $\Re(\bar\lambda\nu_3(e^{i\theta}))=-\sin^2(\theta/2)$ exactly",
 r"`[ALG]` (named sub-statement of RECOG-ALG-NU3-CLOSED-FORM, $Z$-frame) $\Re(\bar\lambda\nu_3(e^{i\theta}))=-\sin^2(\theta/2)$ exactly"),
("S1-5", "M", "FB-13", "§1 lattice: corollary RID", "str", "live",
 r"identical comparator data can retain different asymptotic pair phases for $q_0<|G|/C_2$ (§6.13a).",
 r"identical comparator data can retain different asymptotic pair phases for $q_0<|G|/C_2$ (RECOG-THM-R9-COMPARATOR-INCOMPLETENESS, §6.13a)."),
("S1-6", "FC21", "FC-21", "§1 A1a paragraph: R9-free existence on U", "str", "live",
 r"and the asymptotic phase exists without R9 (existence only). $C_D$ depends on the start state.",
 r"and the asymptotic phase exists without R9 (existence only). `[THM]` [RID: RECOG-THM-A1A-PHASE-EXISTENCE-U] (v0.3.23) On all of $U$, without R9 and without NUMGEN INF-1, $C_D^{\rm ext}$ exists and equals an explicit absolutely convergent series in the block amplitudes and the Dyadic row-A block remainders (existence and that series only). $C_D$ depends on the start state."),
# ---------------- §2 ----------------
("S2-1", "M", "FB-18", "R2 owner branch (bridge-lemma custody)", "str", "live",
 r"Owner branch: this document → general theorem recommended for Dyadic ownership",
 r"Owner branch: this document supplies the general-$p$ proof (RECOG-ALG-LEADING-RETURN-EQUIVARIANCE, §6.12); the statement RID DYAD-ALG-BRIDGE-LEMMA is Dyadic's (§7 mutual-citation guard)"),
("S2-2", "M", "FB-15", "R2 residual: frame scale", "str", "live",
 r"Residual: none. Cross-$p$ comparison is by $\arg\mu_p$ only (magnitudes are frame-dependent).",
 r"Residual: none. Cross-$p$ comparison is by $\arg\mu_p$ only (magnitudes are frame-dependent; frame scale $W_p=i\cot(\pi/p)Z$, DYAD-ALG-KP-FRAME-SCALE)."),
("S2-3", "M", "FB-11", "R6 GAP-LOCK Lemma 3 cross-reference pin", "str", "live",
 r"`[import: RTG_NUMBER_GENESIS_DSN_v1.20.7 N-5A-S1-INF / GAP-LOCK Lemma 3]`",
 r"`[import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 N-5A-S1-INF / GAP-LOCK Lemma 3]` (pinned at v1.20.7 since v0.3.18; the owner records no theorem-level change in v1.20.8; the Lemma 3 text is present in the current source, claim audit v0.3.23)"),
("S2-4", "M", "R10 wording", "R10 status line", "str", "live",
 r"Status: **DELIVERED and ACCEPTED (v0.3.2)** — owner adoption",
 r"Status: **CLOSED (v0.3.2) — delivered and accepted** — owner adoption"),
# ---------------- §3 ----------------
("S3-1", "M", "FA-03", "SG-R10: keep guard, replace stale routing", "str", "live",
 r"the quoted leading amplitude (currently $0.007652\,Q_0$, post-$H_2$) is not a finite-$Q_0$ bound (R9/R10/R11).",
 r"the quoted leading amplitude (currently $0.007652\,Q_0$, post-$H_2$) is not a finite-$Q_0$ bound for the full exact memory. The certified finite-$q_0$ statement is RECOG-THM-R9-MEMORY (§6.13a): per row, on the $C_z$ track, in the normalized $q$, $|M-c_{\rm iso}q_0|\le|G|q_0+C_2q_0^2$, hence $|M|\le(|c_{\rm iso}|+|G|)q_0+C_2q_0^2$; comparator incompleteness is certified only for $q_0<|G|/C_2$ (RECOG-THM-R9-COMPARATOR-INCOMPLETENESS)."),
("S3-2", "M", "FA-03/FB-11", "SG-R14 quantified note: owner tag forms", "str", "live",
 r"*Quantified (v0.3.21, reference import).* [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.15 §6.14 | DYAD-THM-OPEN3-ASYMPTOTIC-PHASE, T2 `[THM — conditional on T1]`; T1 conditional on RECOG-THM-R9-MEMORY]",
 r"*Quantified.* [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.15) | DYAD-THM-OPEN3-ASYMPTOTIC-PHASE, T2 `[THM]` `[assuming: T1]`; T1 `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`]"),
("S3-3", "M", "FA-03", "SG-R14 quantified note: adopted use", "str", "live",
 r"this is not a theorem about the comparator $C_W^{(h)}$, no R9 coefficient is transferred to that track, and no RECOG claim changes.",
 r"this is not a theorem about the comparator $C_W^{(h)}$, and no R9 coefficient is transferred to that track. T1 and T2 are in adopted use in §6.13b (RECOG-THM-A1A-CD-IDENTIFICATION, R9 premise discharged by RECOG's own R9); this note adds no claim."),
# ---------------- §4, §5 ----------------
("S4-1", "M", "FA-03/FB-15", "§4 p-family row: frames and non-chart objects", "str", "live",
 r"| $p$-family / normal form | $\nu_3(\lambda)$, $\mu_p$, $c_{32},c_{05},c_\theta^{(6)}$, backbone |",
 r"| $p$-family / normal form | $\nu_3(\lambda)$, $\mu_p$ ($Z$-frame; frame scale DYAD-ALG-KP-FRAME-SCALE), $c_{32},c_{05}$ (frame named, SG-R10); $c_\theta^{(6)}$ and fitted backbones are archival, not chart objects (SG-R13; §6.14 refusal line) |"),
("S5-1", "FC21", "FC-21", "§5 C_D row: R9-free existence on U", "str", "live",
 r"R9-free existence (RECOG-RESULT-A1A-PHASE-EXISTENCE-NG) and agreement with NUMGEN's $C_D$ (RECOG-RESULT-A1A-CD-AGREEMENT) only on $U\cap U_{\rm NUMGEN}$; per-row quantitative form with the Dyadic OPEN 21 constants, rows not mixed | a universal, start-independent $C_D$; an explicit radius for the R9-free route; R9-free memory coefficients, $C_2$ or remainders;",
 r"R9-free existence on all of $U$ (RECOG-THM-A1A-PHASE-EXISTENCE-U) and on $U\cap U_{\rm NUMGEN}$ (RECOG-RESULT-A1A-PHASE-EXISTENCE-NG); agreement with NUMGEN's $C_D$ (RECOG-RESULT-A1A-CD-AGREEMENT) only on $U\cap U_{\rm NUMGEN}$; per-row quantitative form with the Dyadic OPEN 21 constants, rows not mixed | a universal, start-independent $C_D$; R9-free memory coefficients, $c_{\rm iso}$, $\Lambda_1$, $C_2$, remainders or an R9-free OPEN 21; starts in $U_T\setminus U$; any extension of NUMGEN's adopted domain;"),
("S5-2", "M", "FA-09", "§5 radial-neutrality row: remainder", "str", "live",
 r"gives $Q(T^6(t,0))-t^2=6\gamma t^6$ of either sign `[ALG]`",
 r"gives $Q(T^6(t,0))-t^2=6\gamma t^6+O(t^8)$ of either sign `[ALG]`"),
# ---------------- §6.2–§6.5 ----------------
("S62-1", "M", "FB-15", "§6.2 frame-independence sentence", "str", "live",
 r"Leading coefficient, return order and local strict contraction are frame-independent.",
 r"Within the tangent-to-identity frame changes compared here, the leading coefficient, return order and local strict contraction are frame-independent; under a complex linear rescaling the return order, local strict contraction, the sign of $\Re\mu$ and $\arg\mu$ are kept and $|\mu|$ scales (frame rule, DYAD-ALG-KP-FRAME-SCALE)."),
("S63-1", "M", "FA-04", "§6.3 fixed-point flag answered", "str", "live",
 r"(Dyadic §6.1 lists only $P_1,P_2$; flagged to Dyadic in the memo.)",
 r"(The Dyadic fixed-point scope table, v6.4.22 §1, lists the lifted-chart fixed points and the wrapped-cylinder winding fixed points and records agreement with this section.)"),
("S64-1", "M", "FB-13", "§6.4 swap-odd rho lemma RID", "str", "live",
 r"`[ALG conditional]` [assumes: pole-swap covariance; certified $A=DT(P_1)$] Write",
 r"`[ALG conditional]` [RID: RECOG-ALG-SWAP-ODD-RHO] [assumes: pole-swap covariance; certified $A=DT(P_1)$] **Swap-odd $\rho$ lemma.** Write"),
("S64-2", "M", "FA-08", "§6.4 RESULT pairing (L487)", "str", "live",
 r"`[RESULT]` `[from: ALG conditional]` The stationarity",
 r"`[RESULT]` `[from: ALG]` [assuming: pole-swap covariance of the radial row; certified $A=DT(P_1)$] The stationarity"),
("S66-1", "M", "FA-08", "§6.6a RESULT pairing (L548)", "str", "live",
 r"`[RESULT]` **R5 restated.**",
 r"`[RESULT]` `[from: ALG]` [assuming: the twisted-cocycle premise] **R5 restated.**"),
# ---------------- §6.9–§6.11 ----------------
("S69-1", "M", "FB-13", "§6.9 export: corollary RID", "str", "live",
 r"with the exact-map comparator-incompleteness corollary — exported only",
 r"with the exact-map comparator-incompleteness corollary RECOG-THM-R9-COMPARATOR-INCOMPLETENESS — exported only"),
("S610-1", "M", "FB-15", "§6.10 family: frame scale", "str", "live",
 r"relates to the $W$-frame by the exact scale $6\bar\lambda\nu_3(\zeta_6)=3\mu_6^{W}$.",
 r"relates to the $W$-frame by the exact scale $6\bar\lambda\nu_3(\zeta_6)=3\mu_6^{W}$, the $p=6$ case of $W_p=i\cot(\pi/p)Z$, $\nu_3^Z=\cot^2(\pi/p)\nu_3^{W_p}$ (DYAD-ALG-KP-FRAME-SCALE, Dyadic v6.4.22 §6.9). $\nu_3$, $\mu_p$ and the $\Re\mu_p$ law of this section are exported as $Z$-frame quantities; their arguments are frame-independent."),
("S610-2", "M", "FB-18", "§6.10 bridge-lemma custody", "str", "live",
 r"Ownership of this general theorem is recommended for Dyadic (stream memo §1).",
 r"Custody: the statement RID DYAD-ALG-BRIDGE-LEMMA is Dyadic's; RECOG-ALG-LEADING-RETURN-EQUIVARIANCE (§6.12) supplies the general-$p$ proof; no ownership transfer (§7 mutual-citation guard)."),
("S610-3", "M", "FB-13", "§6.10 radial identity as named sub-statement", "str", "live",
 r"`[ALG]` **Exact radial identity** (external audit; verified symbolically here):",
 r"`[ALG]` **Exact radial identity** (named sub-statement of RECOG-ALG-NU3-CLOSED-FORM, $Z$-frame; external audit; verified symbolically here):"),
("S611-1", "M", "FB-13", "§6.11 C0-avoidance corollary named", "str", "live",
 "Corollary `[THM]`: $W^u_-(P_2)\\cap C_0=\\varnothing$.\n",
 "Corollary `[THM]` ($C_0$-avoidance; named sub-statement of RECOG-THM-P2-HET): $W^u_-(P_2)\\cap C_0=\\varnothing$.\n"),
# ---------------- §6.13, §6.13a ----------------
("S613-1", "M", "FB-14", "§6.13 leading-crossing value: frame label", "str", "live",
 r'the "leading-crossing" value $|\mu|/|c_{05}|\approx41.3$ is outside the local regime.',
 r'the "leading-crossing" value $|\mu|/|c_{05}^{\rm raw}|\approx41.27$ (raw six-step frame; post-$H_2$ $|\mu|/|a_{05}|\approx59.12$) is outside the local regime in either frame.'),
("S613-2", "M", "FA-03", "§6.13 leading amplitude guard: pointer to R9", "str", "live",
 r"Leading amplitude $|\Lambda|\le0.007652\,Q_0$ — leading order only, for the truncated model (R9, R10, R11).",
 r"Leading amplitude $|\Lambda|\le0.007652\,Q_0$ — leading order only, for the truncated model; not a finite-$q_0$ bound for the full exact memory, whose certified statement is RECOG-THM-R9-MEMORY (§6.13a; SG-R10)."),
("S613a-1", "M", "FB-14", "§6.13a |G| exact with display", "str", "live",
 r"i.e. $G=-\tfrac{43+5611\sqrt3\,i}{1270080}$, $|G|=0.0076520$.",
 r"i.e. $G=-\tfrac{43+5611\sqrt3\,i}{1270080}$, $|G|=\tfrac{\sqrt{481897}}{90720}\approx0.0076520$."),
("S613a-2", "M", "FB-13", "§6.13a corollary RID", "str", "live",
 r"`[THM]` **Corollary (exact-map $C_z$ comparator incompleteness).**",
 r"`[THM]` [RID: RECOG-THM-R9-COMPARATOR-INCOMPLETENESS] [scope: as RECOG-THM-R9-MEMORY, per row; witness window $q_0<|G|/C_2$] **Corollary (exact-map $C_z$ comparator incompleteness).**"),
("S613a-3", "M", "FB-13", "§6.13a corollary dependency", "str", "live",
 r"the lattice memory is therefore certified nonzero whenever $q_0<|G|/C_2$.",
 r"the lattice memory is therefore certified nonzero whenever $q_0<|G|/C_2$. Depends on: RECOG-THM-R9-MEMORY."),
("S613a-4", "M", "FB-14", "§6.13a window row A", "str", "live",
 r"$q_0<|G|/517=1.48\times10^{-5}$",
 r"$q_0<|G|/517\approx1.4800743\times10^{-5}$"),
("S613a-5", "M", "FB-14", "§6.13a window row B", "str", "live",
 r"$q_0<|G|/163=4.69\times10^{-5}$",
 r"$q_0<|G|/163\approx4.6944689\times10^{-5}$"),
# ---------------- §6.13b ----------------
("S613b-1", "M", "FB-19", "§6.13b notation line", "line", "live",
 r"> **[SG-R13, SG-R14 apply]** Primitive frame $W=\rho-\eta/2",
 "{LINE}\n\n*Notation.* As a subscript or limit index ($D_M$, $D_M^U$, $\\lim_M$, $MQ_M$), $M$ is the block count; $M(z_0)$ and $M_W$ are retained memories (§6.13a). The two are distinct. Where both occur in one formula, the block count is written $N$."),
("S613b-2", "M", "FA-06", "§6.13b grade principle: methodology edition", "str", "live",
 r"**Grade principle.** Methodology v1.3 §3.4 (M13-C04):",
 r"**Grade principle.** Methodology v1.4 §3.4 (M13-C04):"),
("S613b-3", "M", "FA-02", "§6.13b D_M import: NUMGEN RID", "line", "live",
 r"`[DEF]` [import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6 N-5A-S1-INF, $D_M$ definition | RID unavailable]",
 r"`[DEF]` [import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 N-5A-S1-INF | NUMGEN-DEF-N5AS1-DEFECT] $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$, quoted verbatim; $\hat\phi_n$ is the increasing lift of $\arg W$ with principal one-step increments (NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT) from an arbitrary start $x_0$ on NUMGEN's tube $U_{\rm NUMGEN}$, the block counter taken from the start. Same formula as the v1.20.7 text imported by v0.3.22; the owner records that the RID allocation changes no statement, proof, domain or grade. The module RID `NUMGEN-OPEN-N5AS1-INF` is not a theorem RID and is not used as one."),
("S613b-4", "M", "FA-02", "§6.13b INF-1 import: NUMGEN RID", "line", "live",
 r"`[RESULT]` `[from: ALG]` [import: RTG_NUMBER_GENESIS_DSN_v1.20.7 §6.6, INF-1 | RID unavailable]",
 r"`[RESULT]` `[from: ALG]` [import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 | NUMGEN-RESULT-N5AS1-INF1] [scope: $U_{\rm NUMGEN}$, which exists but has no stated radius] $D_M=\tau\log M+C_D+o(1)$, with $C_D$ depending on $x_0$. Depends on: L-BACKBONE (from L1) and L-PHASE (owner text; NUMGEN-RESULT-N5AS1-L-BACKBONE, NUMGEN-RESULT-N5AS1-L-PHASE), with the lift made increasing by L-MONO (NUMGEN-RESULT-N5AS1-L-MONO); not on RECOG R9 (NUMGEN C4 reply `8a887ef3…bc4d`). `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` is the RID of the ratio theorem that uses INF-1, not of INF-1 (§7 scope note)."),
("S613b-5", "M", "FB-11", "§6.13b PRIM-CTR / NF-INV import", "str", "live",
 r"[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 | DYAD-THM-PRIM-CTR, DYAD-THM-NF-INV]",
 r"[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 | DYAD-THM-PRIM-CTR, DYAD-THM-NF-INV]"),
("S613b-6", "M", "FB-11", "§6.13b PRIM-CTR statement note", "str", "live",
 r"Statements unchanged since v6.4.10 (§7 rows).",
 r"Statements recorded unchanged from v6.4.10 to v6.4.17 by the G2 audit of v0.3.21 (§7.2); the quoted statements are present at the cited RIDs in the current source v6.4.22 (claim audit v0.3.23)."),
("S613b-7", "M", "FB-11", "§6.13b P4-0 import", "str", "live",
 r"[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14, v6.4.15 entries | DYAD-ALG-OPEN3-PHASE-OFFSET]",
 r"[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.15) | DYAD-ALG-OPEN3-PHASE-OFFSET]"),
("S613b-8", "M", "FB-11 (tag form; line pin)", "§6.13b primitive-variable form import", "str", "live",
 r"`[ALG — formal second order; remainder not certified]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 806–809 | DYAD-ALG-OPEN3-PHASE-OFFSET, primitive-variable form] $M_W(W_0)=\mathcal P_2(W_0)+O(Q_0^{3/2})$ with $P_{W2}=-\Delta_2+D\Delta_1[h_2]$; the owner qualifier is carried verbatim.",
 r"`[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14, primitive-variable form (pinned at v6.4.18 in v0.3.22) | DYAD-ALG-OPEN3-PHASE-OFFSET] $M_W(W_0)=\mathcal P_2(W_0)+O(Q_0^{3/2})$ with $P_{W2}=-\Delta_2+D\Delta_1[h_2]$; the owner tag and scope are carried verbatim (owner form since v6.4.21; at v6.4.18 the same expansion was tagged `[ALG — formal second order; remainder not certified]`; the remainder is certified separately by OPEN 21)."),
("S613b-9", "M", "FB-11", "§6.13b offset-bounds import", "str", "live",
 r"[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 | DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS]",
 r"[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.15) | DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS]"),
("S613b-10", "M", "FB-11 (tag form)", "§6.13b T1/T2 import", "str", "live",
 r"`[THM — conditional on RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.16 §6.14 | DYAD-THM-OPEN3-ASYMPTOTIC-PHASE] T1 (limit equality) and T2 ($M_W-M=-\Delta_0(z_0)$), orbits starting in a row disk.",
 r"`[THM]` `[assuming: RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.15) | DYAD-THM-OPEN3-ASYMPTOTIC-PHASE] T1 (limit equality; `[assuming: RECOG-THM-R9-MEMORY]`) and T2 ($M_W-M=-\Delta_0(z_0)$; `[assuming: T1]`), orbits starting in a row disk."),
("S613b-11", "M", "FB-11 (tag form; line pin)", "§6.13b OPEN 21 import", "line", "live",
 r"`[THM — conditional on RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 lines 843–850",
 r"`[THM]` `[assuming: RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14, OPEN 21 (first published v6.4.17; pinned at v6.4.18 `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d` in v0.3.22) | DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER] $\lvert M_W-\mathcal P_2(W_0)\rvert\le K'_jQ_0^{3/2}+C_{2,j}(\tfrac{256}{225})^2Q_0^2$, rows A, B not mixed. The quoted statement, owner tag, rows and constants are present at the cited RID in the current source `dyad-v6.4.22` (claim audit v0.3.23). The v6.4.18 source-statement check (A1a-E2, `941f42d6…126e`) is kept as historical evidence; the Dyadic P5 certificate and RECOG's R9 Arb certificate were not rerun."),
("S613b-12", "M", "FB-11 (line pin)", "§6.13b (c) P_W2 source", "str", "live",
 r"(Dyadic v6.4.18 §6.14 lines 806–809), and $c_{\rm iso}$",
 r"(Dyadic §6.14, DYAD-ALG-OPEN3-PHASE-OFFSET, primitive-variable form; present at the cited RID in the current source v6.4.22), and $c_{\rm iso}$"),
("S613b-13", "M", "FB-11", "§6.13b (c) source fidelity", "str", "live",
 r"Source fidelity of the OPEN 21 statement, constants and rows: A1a-E2 PASS on v6.4.18; this is not a recertification.",
 r"Source fidelity of the OPEN 21 statement, constants and rows: A1a-E2 PASS on v6.4.18, quoted statement, constants and rows present at the cited RID in the current source v6.4.22 (claim audit v0.3.23); this is not a recertification."),
("S613b-14", "FC21", "FC-21", "§6.13b new block and scope item (i)", "str", "live",
 "\n**Scope and custody.** (i) Statement (a) is the only R9-free claim and holds only on the existential intersection.",
 "\n" + FC21_BLOCK + "\n\n**Scope and custody.** (i) The R9-free claims are (a), on the existential intersection, and RECOG-THM-A1A-PHASE-EXISTENCE-U, on all of $U$ (existence and its series only)."),
# ---------------- §6.14 ----------------
("S614-1", "M", "FB-11", "§6.14 owner package: current counterpart", "str", "live",
 r"`[import: Dyadic v6.4.10 §6.14]` **Owner package (accepted).**",
 r"`[import: Dyadic v6.4.10 §6.14; current counterpart v6.4.22 §6.14, quoted statements present at the cited RIDs in the current source (claim audit v0.3.23)]` **Owner package (accepted).**"),
("S614-2", "M", "FB-16", "§6.14 S_h, R_0 and the smooth involution", "str", "live",
 r"Whether $S_h$ is the physical pole relabeling is RRF OPEN-A, outside RECOG.",
 r"$j^6S_h=j^6R_0$, with $R_0=T^3\circ F^{-1/2}$ the unique formal involution with linear part $-I$ commuting with $F=T^6$ (Dyadic v6.4.22 §6.15–§6.16: $S_h$ equals $R_0$ through degree 6 and is not upgraded by the closure of OPEN 19); $S_h$ is an exact involution; its commutation with $F$ is certified only through degree 6. At germ scope, DYAD-THM-SMOOTH-EMBEDDING (Dyadic v6.4.22 §6.17, E4) gives a $C^\infty$ involution $R=T^3\circ K_2^{-1}$, $DR(0)=-I$, commuting exactly with $T$. $R$ is **not** identified with the delivered finite-chart action $S_h$; no finite-chart radius transfers to it; it is not read as physical pole or node exchange; it does not discharge the §6.4 linear-swap covariance premise. Whether $S_h$ (or $R$) is the physical pole relabeling is RRF OPEN-A, outside RECOG; R1 and OPEN-OFN-OPA stay open."),
("S614-3", "M", "FA-03/FB-14", "§6.14 R9 partial budget", "str", "live",
 r"`[ALG]` [cert: check 8] **R9 budget.** Degree-$\ge7$ contribution to the retained memory $\le2C_7q_0^2$; leading coefficient $|\Lambda_1|\le0.0076520$; dominance threshold $q_0<|\Lambda_1|/(2C_7)=3.83\times10^{-5}$ ($C_7=100$), $1.28\times10^{-4}$ ($C_7=30$).",
 r"`[ALG]` [cert: check 8] **R9 partial budget (degree $\ge7$).** The degree-$\ge7$ contribution to the retained memory is $\le2C_7q_0^2$; this is a partial budget, distinct from the full R9 remainder $C_2q_0^2$ of RECOG-THM-R9-MEMORY. Leading-coefficient amplitude $\max_\Theta|\Lambda_1(\Theta)|=|G|\approx0.0076520$; partial-budget dominance threshold $q_0<|G|/(2C_7)\approx3.83\times10^{-5}$ ($C_7=100$), $\approx1.28\times10^{-4}$ ($C_7=30$), distinct from the incompleteness windows $q_0<|G|/C_2$ (§6.13a)."),
# ---------------- §6.15–§6.16 ----------------
("S615-1", "M", "FB-12", "§6.15 E2C identifier: custody note", "str", "live",
 r"`[ENG]` [RID: E2C-ENG-SPLIT-REFINEMENT] The inherited",
 r"`[ENG]` [RID: E2C-ENG-SPLIT-REFINEMENT] (custody: a RECOG artifact; the identifier keeps its historical prefix and is not renamed) The inherited"),
("S615c-1", "M", "FB-10", "§6.15c Q_c citation", "str", "live",
 r"(Dyadic v6.4.10 §4; canonical pre-crossing predicate",
 r"(DYAD-ALG-QC-CRITICAL-AMPLITUDE, Dyadic v6.4.22 §6.4; pinned at v6.4.10 §4 before the RID existed; canonical pre-crossing predicate"),
("S615-R1", "M", "FA-08", "§6.15a RESULT pairing (L837)", "str", "live",
 r"`[RESULT]` **Universal radial access does not imply universal rank-side entry.**",
 r"`[RESULT]` `[from: THM]` [scope: diagnostic twin $T_s$, SG-R4] **Universal radial access does not imply universal rank-side entry.**"),
("S615-R2", "M", "FA-08", "§6.15b RESULT pairing (L853)", "str", "live",
 r"`[RESULT]` **The three R7 statements are logically independent and now all decided.**",
 r"`[RESULT]` `[from: THM]` [scope: diagnostic twin $T_s$, SG-R4] **The three R7 statements are logically independent and now all decided.**"),
("S615-R3", "M", "FA-08", "§6.15c RESULT pairing (L865)", "str", "live",
 r"`[RESULT]` [RID: RECOG-RESULT-TWIN-QC-DEGENERACY]",
 r"`[RESULT]` `[from: ALG]` [RID: RECOG-RESULT-TWIN-QC-DEGENERACY]"),
("S616-R1", "M", "FA-08", "§6.16 RESULT pairing (L873)", "str", "live",
 r"`[RESULT]` [RID: RECOG-RESULT-EVENT-UNDERDETERMINATION]",
 r"`[RESULT]` `[from: THM]` [scope: registry-relative; the currently registered candidate structures] [RID: RECOG-RESULT-EVENT-UNDERDETERMINATION]"),
("S616-1", "M", "FA-01 (status part)", "§6.16 ledger row: F2(b) pointer", "str", "live",
 r"is not settled here and is the subject of F2(b).",
 r"is not settled by this row; F2(b) answered it: no termwise coincidence, the chart crossings are displaced shadows of the token (§6.16a)."),
("S616-R2", "M", "FA-08", "§6.16 RESULT pairing (L905)", "str", "live",
 r"`[RESULT]` **F1 conclusion.**",
 r"`[RESULT]` `[from: THM]` [scope: registry-relative] **F1 conclusion.**"),
("S616-2", "M", "FA-01 (status part)", "§6.16 CELL-F2 targets: executed", "str", "live",
 r"**CELL-F2 targets.**",
 r"**CELL-F2 targets** (as posed; all executed: F2(b) §6.16a, F2(a) §6.16b, F2(c0) §6.16c, F2(c1) §6.16d; the refinement F2(d) §6.16e)."),
("S616-3", "M", "FA-01 (status part)", "§6.16 CELL-F2 order line", "str", "live",
 r"Order: F2(b) before F2(c0).",
 r"Order used: F2(b) before F2(c0)."),
("S616a-R1", "M", "FA-08 (split) / FA-01 (status part)", "§6.16b RESULT split (L927)", "line", "live",
 r"`[RESULT]` `[from: NUM strong, ALG]` **Tokenisation consequence (R6).**",
 r"`[RESULT]` `[from: NUM strong]` [scope: F2(b) campaign, 12 orbits, 87 slips; leading-order law RECOG-ALG-CHART-SHADOW] **Tokenisation consequence (R6), token side.** The owner's *physical* return-section token (Number Genesis naming: physical 7-gap as opposed to defect threshold — not a physical-event verdict) is the primitive B-event, and the 7-gap is decided by the raw-track window $0\le o_j<\Delta_j=O(Q)$. RECOG $h$-chart lag crossings — lattice thresholds included — are displaced shadows of that token: same asymptotic clock, no termwise identity, displacement $\pm\tfrac3{16\sqrt Q}$ blocks, unbounded in return count and $O(\sqrt Q)$ relative to block time." "\n\n"
 r"`[RESULT]` `[from: ALG]` **Tokenisation consequence (R6), schema side.** Against the RECOG-DEF-EVENT-TOKEN-SCHEMA criteria: lattice thresholds fail criterion 1 (representation safety: the chart shadow is $O(\sqrt Q)$ while the deciding window is $O(Q)$) and criterion 4 (no change of return word at a threshold); the NG 7-gap passes criterion 4 (return word $6\to7$); its criterion-1 status (behaviour under registered representation changes of the section) was settled by F2(a) (§6.16b). This does **not** adopt the 7-gap as *the* recognition event (SG-R6); it removes the chart thresholds as candidates."),
("S616b-R1", "M", "FA-08", "§6.16b RESULT pairing (L956)", "str", "live",
 r"`[RESULT]` **F2(a) conclusion.**",
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative] **F2(a) conclusion.**"),
("S616b-1", "M", "FA-01 (status part)", "§6.16b stale next-step pointer", "str", "live",
 r" Next: F2(c0).",
 r" F2(c0) followed (§6.16c)."),
("S616c-1", "M", "FA-01 (status part)", "§6.16c F2(c1) pointer", "str", "live",
 r"that `R` question is F2(c1):",
 r"that `R` question was posed as F2(c1) and is answered in §6.16d:"),
("S616d-R1", "M", "FA-08", "§6.16d RESULT pairing (L995)", "str", "live",
 r"`[RESULT]` [RID: RECOG-RESULT-P2-FOLD-NO-REGISTERED-RETENTION]",
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative; current registered carrier inventory] [RID: RECOG-RESULT-P2-FOLD-NO-REGISTERED-RETENTION]"),
("S616d-R2", "M", "FA-08", "§6.16d RESULT pairing (L999)", "str", "live",
 r"`[RESULT]` **Criterion-5 classification.**",
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative] **Criterion-5 classification.**"),
("S616d-R3", "M", "FA-08 (split)", "§6.16d RESULT split (L1003)", "line", "live",
 r"`[RESULT]` `[from: THM, ALG, RESULT]` **Separation of the R and E axes.**",
 r"`[RESULT]` `[from: THM]` **Separation of the R and E axes — retention side.** The registered package contains retention without transition: RECOG-THM-R9-MEMORY (non-comparator memory in the rank-safe tube)." "\n\n"
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative] **Separation of the R and E axes — transition and token side.** It also contains transition/noninjectivity without registered retention (§6.16c–d) and a representation-safe, dynamically distinguished token (the B/7-gap, §6.16a–b). None of these facts selects *the* recognition event; what R6 still lacks is a selection principle, not a local calculation."),
("S616e-R1", "M", "FA-08", "§6.16e RESULT pairing (L1019)", "str", "live",
 r"`[RESULT]` Under the anti-tautology guard,",
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative; anti-tautology guard] Under the anti-tautology guard,"),
("S616e-R2", "M", "FA-08", "§6.16e RESULT pairing (L1021)", "str", "live",
 r"`[RESULT]` **Completed criterion table.**",
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative] **Completed criterion table.**"),
("S616e-R3", "M", "FA-08", "§6.16e RESULT pairing (L1030)", "str", "live",
 r"`[RESULT]` **The coupling gap.**",
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative] **The coupling gap.**"),
("S616f-1", "M", "VF-1", "§6.16f VF-1 identifier", "str", "live",
 r"(the delivered map need not have all-orders $\mathbb Z_6$ symmetry; VF-1)",
 r"(the delivered map need not have all-orders $\mathbb Z_6$ symmetry; DYAD-ALG-NF6-DEG10, registered in RRF v0.8 as finding VF-1)"),
("S616f-R1", "M", "FA-08", "§6.16f RESULT pairing (L1052)", "str", "live",
 r"`[RESULT]` [RID: RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH]",
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative] [RID: RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH]"),
("S616f-R2", "M", "FA-08", "§6.16f RESULT pairing (L1054)", "str", "live",
 r"`[RESULT]` **Ladder outcome and R6 endpoint.**",
 r"`[RESULT]` `[from: ALG]` [scope: registry-relative] **Ladder outcome and R6 endpoint.**"),
("S616g-R1", "M", "FA-08", "§6.16g RESULT pairing (L1108)", "str", "live",
 r"`[RESULT]` [RID: RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS]",
 r"`[RESULT]` `[from: DEF]` [scope: registry-relative] [RID: RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS]"),
("S616g-R2", "M", "FA-08", "§6.16g RESULT pairing (L1110)", "str", "live",
 r"`[RESULT]` **Cross-owner alignment (no import).**",
 r"`[RESULT]` `[from: DEF]` [scope: registry-relative; no import] **Cross-owner alignment (no import).**"),
# ---------------- §7 ----------------
("S7-1", "M", "FB-11/FA-05", "§7 synchronization note", "str", "live",
 r"*Synchronization note (v0.3.21).* Source pins below are retained for provenance (v0.3.18 practice). Each load-bearing row was compared claim by claim with the current owner edition (Dyadic v6.4.17, Genesis v2.8.9, OFN v0.10, RRF v0.8.3); dispositions are in §7.2. Where a row below adds a v0.3.21 remark, it records an identifier, a scope note or a mutual-citation guard only.",
 r"*Synchronization note.* Source pins below are producer or historical pins, kept where they are valid for the cited claim. Current owner editions: Dyadic `dyad-v6.4.22` (`2363ca40…8c29`), NUMGEN `numgen-v1.20.8` (`835a56f8…7e2f`), Genesis v2.8.9, OFN v0.10, RRF v0.8.4. For v0.3.23, for every load-bearing Dyadic and NUMGEN row, the statement strings RECOG quotes (scopes, rows and constants included) were checked to be present in the owner text at its tag. The audit establishes that the quoted statement is present at the cited RID in the current source; it is not a comparison with the earlier pinned editions, most of which are not in the repository; the earlier comparisons are those of §7.1–§7.2. The current owner tag forms are quoted at the point of use (claim audit `evidence/recog/v0.3.23/claim_audit.json`; table in the v0.3.23 release record). Genesis, OFN and RRF rows are as audited v0.3.21 (§7.2); RECOG's RRF rows are convention or registry references. Where a row below adds a remark, it records an identifier, a scope note or a mutual-citation guard only."),
("S7-2", "M", "FB-10", "§7 row §6.1 block: Dyadic RIDs", "str", "live",
 r"- [RID: (none — §6.1 block); map definition registered since Dyadic v6.4.11 as DYAD-DEF-PRIMITIVE-MAP (provisional custody; identifier only, content unchanged)] :: dyad map, $J$, $\det J$, $C_0$, $P_1,P_2$, escape law, non-symplecticity :: Dyadic §6.1 ::",
 r"- [RID: DYAD-DEF-PRIMITIVE-MAP (map; custody note Dyadic §1), DYAD-DEF-CRITICAL-CURVE ($C_0$, kernel field $k$); $J$, $\det J$, $P_1,P_2$, the escape law and non-symplecticity have no Dyadic RID] :: dyad map, $J$, $\det J$, $C_0$, $P_1,P_2$, escape law, non-symplecticity :: Dyadic §6.1 (v6.4.22; RIDs registered v6.4.11 and v6.4.20; quoted content present) ::"),
("S7-3", "M", "FB-10", "§7 row §6.4 block: Dyadic RIDs", "str", "live",
 r"- [RID: (none — §6.4 block)] :: $Q_c=(\arcsin\ln2)^2$, winding-index invisibility, ISP $\Theta$ :: Dyadic §6.4 ::",
 r"- [RID: DYAD-ALG-QC-CRITICAL-AMPLITUDE ($Q_c$), DYAD-ALG-ISP-MAPS (ISP maps, $\Theta$); winding-index invisibility has no Dyadic RID] :: $Q_c=(\arcsin\ln2)^2$, winding-index invisibility, ISP $\Theta$ :: Dyadic §6.4 (v6.4.22; RIDs registered v6.4.20; quoted content present) ::"),
("S7-4", "M", "FB-10", "§7 row §6.7/§6.8 block: Dyadic RID", "str", "live",
 r"- [RID: (none — §6.7/§6.8 block)] :: $M+M^\top=-I$, $Q_{m+1}=Q_m-Q_m^2+\cdots$, $\Theta_{m+1}=\Theta_m-\tau Q_m$ :: Dyadic §6.7–6.8 ::",
 r"- [RID: DYAD-ALG-SIXSTEP-CUBIC-JET (jet and $M+M^\top=-I$); the block recurrences have no separate Dyadic RID] :: $M+M^\top=-I$, $Q_{m+1}=Q_m-Q_m^2+\cdots$, $\Theta_{m+1}=\Theta_m-\tau Q_m$ :: Dyadic §6.7–6.8 (v6.4.22; RID registered v6.4.20; quoted content present) ::"),
("S7-5", "M", "FB-10", "§7 row 47/54: Dyadic RID", "str", "live",
 r"- [RID: (none — Dyadic §6.5)] :: $\tfrac{47}{54}=",
 r"- [RID: DYAD-ALG-RAW-ANGULAR-MEAN (registered v6.4.20)] :: $\tfrac{47}{54}="),
("S7-6", "M", "FB-18", "§7 bridge-lemma general-form row: custody", "str", "live",
 r"general proof supplied in §6.12 (ownership offered to Dyadic)",
 r"general proof supplied in §6.12 (custody: the statement RID is Dyadic's, the general-$p$ proof is RECOG's)"),
("S7-7", "M", "FB-11", "§7 NUMGEN L1 row: current owner", "str", "live",
 r"- [RID: NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION] (source pin v1.15 retained; RID resolves in v1.20.4; current owner v1.20.7;",
 r"- [RID: NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION] (source pin v1.15 retained; RID resolves in v1.20.4; current owner v1.20.8, `numgen-v1.20.8` §6.2, quoted statement present at the cited RID in the current source (claim audit v0.3.23);"),
("S7-8", "M", "FB-11", "§7 NUMGEN N1C row: current owner", "str", "live",
 r"- [RID: NUMGEN-OPEN-N1C] (source pin v1.15 retained; RID resolves in v1.20.4; current owner v1.20.7;",
 r"- [RID: NUMGEN-OPEN-N1C] (source pin v1.15 retained; RID resolves in v1.20.4; current owner v1.20.8, `numgen-v1.20.8` §6.2, quoted statement present at the cited RID in the current source (claim audit v0.3.23);"),
("S7-9", "M", "FB-11", "§7 defect-threshold row: current counterpart", "str", "live",
 r"RID present, statement unchanged, owner tag normalised to `[RESULT] [from: ALG]` under K5)",
 r"RID present, statement unchanged, owner tag normalised to `[RESULT] [from: ALG]` under K5; current counterpart `numgen-v1.20.8` §6.6, quoted statement and tag present at the cited RID in the current source, claim audit v0.3.23)"),
("S7-10", "M", "FA-02", "§7 defect-threshold row: scope note", "str", "live",
 r"*Scope note (v0.3.22):* the RID is registered for the defect-threshold ratio theorem; the INF-1 formula $D_M=\tau\log M+C_D+o(1)$ quoted in this row is context and has no RID of its own in v1.20.7. The A1a cell imports INF-1 separately as `RID unavailable` (§6.13b, A1a-G1). No statement or use of this row changes",
 r"*Scope note:* the RID is registered for the defect-threshold ratio theorem; the INF-1 formula $D_M=\tau\log M+C_D+o(1)$ quoted in this row is context. INF-1's own RID is `NUMGEN-RESULT-N5AS1-INF1` (v1.20.8), imported separately in §6.13b. No statement or use of this row changes"),
("S7-11", "M", "FA-02", "§7 A1a row: NUMGEN D_M", "line", "live",
 r"- [RID: (none — NUMGEN $D_M$ definition, `RID unavailable`;",
 r"- [RID: NUMGEN-DEF-N5AS1-DEFECT] :: $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$, increasing primitive lift (NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT), block counter from the start :: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 (`numgen-v1.20.8`, `835a56f8…7e2f`) :: §6.13b interface (local extension $D_M^U$ on $U$) :: definition quoted verbatim; same formula as the v1.20.7 text used by v0.3.22 (owner: the RID allocation changes no statement)"),
("S7-12", "M", "FA-02", "§7 A1a row: NUMGEN INF-1", "line", "live",
 r"- [RID: (none — NUMGEN INF-1, `RID unavailable`;",
 r"- [RID: NUMGEN-RESULT-N5AS1-INF1] :: $D_M=\tau\log M+C_D+o(1)$ `[RESULT] [from: ALG]`, independent of RECOG R9 (owner C4 reply) :: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 :: §6.13b (a), (b′) :: $U_{\rm NUMGEN}$, no explicit radius; not `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`"),
("S7-13", "M", "FB-11 (tag form)", "§7 A1a row: Dyadic offset / T1 / T2", "line", "live",
 r"- [RID: DYAD-ALG-OPEN3-PHASE-OFFSET; DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS; DYAD-THM-OPEN3-ASYMPTOTIC-PHASE]",
 r"- [RID: DYAD-ALG-OPEN3-PHASE-OFFSET; DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS; DYAD-THM-OPEN3-ASYMPTOTIC-PHASE] :: P4-0 offset identity, $\Delta_1$, $K_0$ per row; T1 `[THM]` `[assuming: RECOG-THM-R9-MEMORY]` and T2 `[THM]` `[assuming: T1]` (owner tag forms) :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.15; pinned at v6.4.16 `33c14c5c…59e0` in v0.3.22) :: §6.13b (a)–(c) :: rows not mixed; R9 premise discharged by RECOG's own R9 for (b), (c) only; no $C_W^{(h)}$ statement"),
("S7-14", "M", "FB-11 (tag form; line pin)", "§7 A1a row: primitive-variable form", "line", "live",
 r"- [RID: DYAD-ALG-OPEN3-PHASE-OFFSET, primitive-variable form]",
 r"- [RID: DYAD-ALG-OPEN3-PHASE-OFFSET, primitive-variable form] :: $\mathcal P_2$, $P_{W2}=-\Delta_2+D\Delta_1[h_2]$; owner form `[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]` (since v6.4.21; at v6.4.18 the same expansion was tagged `[ALG — formal second order; remainder not certified]`) :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (pinned at v6.4.18 `f70308f1…458d` in v0.3.22) :: §6.13b (c) expression only :: the formal expansion is not itself certified; the certified bound is OPEN 21"),
("S7-15", "M", "FB-11 (tag form; line pin)", "§7 A1a row: OPEN 21", "line", "live",
 r"- [RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER]",
 r"- [RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER] :: $\lvert M_W-\mathcal P_2(W_0)\rvert\le K'_jQ_0^{3/2}+C_{2,j}(\tfrac{256}{225})^2Q_0^2$, $K'_A=\tfrac{3951}{1000}$, $K'_B=\tfrac{971}{250}$, $C_{2,A}=517$, $C_{2,B}=163$; owner form `[THM]` `[assuming: RECOG-THM-R9-MEMORY]` :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14, OPEN 21 (first published v6.4.17; pinned at v6.4.18 `f70308f1…458d` in v0.3.22) :: §6.13b (c) :: source-statement check PASS on v6.4.18 (A1a-E2, `941f42d6…126e`), statement, rows and constants present at v6.4.22; P5 certificate not rerun; rows not mixed"),
("S7-16", "M", "FB-10", "§7 closing process sentence", "str", "live",
 r'RIDs marked "(none)" have no stable identifier in the source; requesting assignment there is part of the critique round.',
 r'RIDs marked "(none)" have no stable identifier in the owner source (Dyadic rows checked at `dyad-v6.4.22`; other rows as audited v0.3.21, §7.2).'),
("S7-17", "FC21", "FC-21", "§7 new import row: L-PHASE row A", "str", "live",
 r"- [RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER] :: $\lvert M_W-\mathcal P_2(W_0)\rvert\le K'_jQ_0^{3/2}",
 r"- [RID: DYAD-THM-LPHASE-ROWA-REMAINDER] :: block law $\hat\varphi_{6(m+1)}-\hat\varphi_{6m}=2\pi-\tau Q_m+r_m$, $\lvert r_m\rvert\le\tfrac{403}{250}Q_m^{3/2}$; branch $\varepsilon\le0.04654$ on $U_T$; owner form `[THM]`, not conditional on R9 :: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (first published v6.4.19) :: §6.13b RECOG-THM-A1A-PHASE-EXISTENCE-U :: row A only; block base points in $U$, intermediate steps in $U_T$; primitive $Q_m$, not the chart $q$" "\n"
 r"- [RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER] :: $\lvert M_W-\mathcal P_2(W_0)\rvert\le K'_jQ_0^{3/2}"),
# §7.2 / §7.3 current state (FA-05, FB-17)
("S72-1", "M", "FA-05", "§7.2 N11 RECOG use: adopted use", "str", "live",
 r"| reference import for the SG-R14 quantitative note only (rows not mixed; no $C_W^{(h)}$ statement); RECOG claims unchanged |",
 r"| adopted use since v0.3.22: RECOG-THM-A1A-CD-IDENTIFICATION (§6.13b) depends on T1/T2, R9 premise discharged by RECOG's own R9 (recorded by Dyadic v6.4.22 §7 as ADOPTED USE); also the SG-R14 quantitative note (rows not mixed; no $C_W^{(h)}$ statement) |"),
("S72-2", "M", "FB-11", "§7.2 N13 RECOG use: current pin", "str", "live",
 r"used in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (§6.13b) at the v6.4.18 pin,",
 r"used in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (§6.13b), pinned at v6.4.18 in v0.3.22 and cited at `dyad-v6.4.22` from v0.3.23 (quoted statement present at that tag),"),
("S72-3", "M", "FB-17/RF-1", "§7.2 outbound notices: current state, RF-1 fulfilled", "line", "live",
 r"**Outbound notices (G3).** To RRF:",
 r"**Outbound notices; current state.** Notice states are kept in the records (`records/recog/g3/`; `records/recog/RECOG_v0_3_22_OUTBOUND_NOTICES.md`) with four separate states per recipient (sent, received, statement accepted, adopted use); this release changes none of them. G3 to RER: as recorded by RER v0.2 §G9 (r4.11: received by the RER preparer via the PI, 21 Oct 2026); RECOG records no further state. G3 to OFN and G3 to RRF: prepared. v0.3.22 notices N-D, N-NG and N-O/R/E: prepared. Dyadic notices N19 and N21 to RECOG: prepared by Dyadic and not sent; their content is used here as input only, not as a receipt. **RF-1 fidelity task: fulfilled** (a content state, separate from notice state): RRF v0.8.4 §6.3 quotes W3 verbatim with RID RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS (both cochains in the same cohomology space) and labels inter-space transport a separate `[OPEN]` RRF extension."),
("S73-1", "M", "FA-05", "§7.3 heading edition", "str", "live",
 r"### §7.3 Downstream Dependents Register (v0.3.21) {#sec-7-3-dependents}",
 r"### §7.3 Downstream Dependents Register (v0.3.23) {#sec-7-3-dependents}"),
("S73-2", "M", "FA-05", "§7.3 inspected editions", "str", "live",
 r"Owner editions that consume RECOG RIDs (as inspected v0.3.21).",
 r"Owner editions that consume RECOG RIDs (as inspected v0.3.23 at the tags `dyad-v6.4.22`, `numgen-v1.20.8`, `ofn-v0.10`, `rrf-v0.8.4`, `rer-v0.2`)."),
("S73-3", "M", "FA-05", "§7.3 R9 consumers", "str", "live",
 r"| Dyadic v6.4.15–v6.4.17 §6.14: T1 and memory law (conditional on R9), T2 (conditional on T1), DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (conditional on R9; reported edition); Dyadic §6.14 consumer cross-reference; OFN v0.10 RF-O09-01/02; RRF v0.8.3 §2.4, §4.1a |",
 r"| Dyadic v6.4.22 §6.14: T1 and the memory law `[assuming: RECOG-THM-R9-MEMORY]`, T2 `[assuming: T1]`, DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER `[assuming: RECOG-THM-R9-MEMORY]`; Dyadic v6.4.22 §6.14 consumer cross-reference and §7 import list (pin RECOG v0.3.22 §6.13a); OFN v0.10 RF-O09-01/02; RRF v0.8.4 §2.4, §4.1a |"),
("S73-4", "M", "FA-05", "§7.3 orientation consumers: RRF edition", "str", "live",
 r"OPEN-OFN-OPA; RRF v0.8.3 §4.2a;",
 r"OPEN-OFN-OPA; RRF v0.8.4 §4.2a;"),
("S73-5", "M", "FA-05", "§7.3 token consumers: RRF edition", "str", "live",
 r"| RRF v0.8.3 §4.3, §6.3 | reference |",
 r"| RRF v0.8.4 §4.3, §6.3 | reference |"),
("S73-6", "M", "FA-05/RF-1", "§7.3 F4 consumers: RRF edition, RF-1", "str", "live",
 r"| RRF v0.8.3 §6.3 (see RF-1); RER v0.2 r4.6 G9 |",
 r"| RRF v0.8.4 §6.3 (W3 quoted verbatim with RID; RF-1 fulfilled); RER v0.2 r4.6 G9 |"),
("S73-7", "M", "FA-05", "§7.3 twin consumers: RRF edition", "str", "live",
 r"| RRF v0.8.3 §4.2 (generator-family limit on OPEN-A) |",
 r"| RRF v0.8.4 §4.2 (generator-family limit on OPEN-A) |"),
("S73-8", "M", "FA-05", "§7.3 new consumer rows (Dyadic v6.4.22)", "str", "live",
 r"| RECOG §§6.13a, 6.16–6.16f (token / transition / retention inventory) | OFN v0.10 RF-O09-02 | reference |",
 r"| RECOG §§6.13a, 6.16–6.16f (token / transition / retention inventory) | OFN v0.10 RF-O09-02 | reference |" "\n"
 r"| RECOG-THM-A1A-RECIPROCAL-AMPLITUDE | Dyadic v6.4.22 §6.5 leading-decay statement and §7 import list (pin RECOG v0.3.22 §6.13b) | import at owner grade |" "\n"
 r"| RECOG-ALG-P2-C0-WHITNEY-FOLD | Dyadic v6.4.22 §6.1 DYAD-DEF-CRITICAL-CURVE (kernel field $k$) | reference; no dependency loop |"),
# ---------------- §8 ----------------
("S8-1", "M", "FA-07/FB-20", "§8 repository locations", "str", "live",
 "## §8. Artifact and Script Registry {#sec-8-artifacts}\n\n",
 "## §8. Artifact and Script Registry {#sec-8-artifacts}\n\n"
 r"*Repository locations.* Scripts: `evidence/recog/scripts/`. Outputs and certificates: `evidence/recog/outputs/`, and `evidence/recog/<version>/` for small per-release outputs. Frozen packages, kept as received: `evidence/recog/packages/`. Records, notices and reviews: `records/recog/` (A1a in `records/recog/a1a/`, G3 in `records/recog/g3/`). Every file named in this section is in the repository, loose or as a member of a package in `evidence/recog/packages/`, except the Dyadic referee harness `dyad_referee_p2b_v2.py` (Dyadic-side). Items cited here by hash only that are not in the repository: superseded revisions (F2(b) rev. 1, CELL-D rev. 2 and rev. 3), the NUMGEN C4 reply and its receiving review, the A1a cell-draft v0.1–v0.3 reviews and the A1a session v0.3 review; elsewhere in this file, the v0.3.21 receiving review, the Dyadic v6.4.17 release-verification report and the frozen v0.3.5 bytes `3ba74002…abd6`. No certificate on which a current RECOG theorem rests is among them. Per-hash state: `records/recog/RECOG_SOURCE_RECOVERY_LIST.md` and `evidence/recog/inventory/recog_recovery_inventory_v0_3_22.json`." "\n\n"),
("S8-2", "M", "FA-07", "§8 A1a records locator", "str", "live",
 r"*archive locator:* the NUMGEN C4 reply, its receiving review and the cell-draft reviews are cited by identity and are not included in the draft review package (PI-held project evidence); the package manifest lists its own payload file",
 r"*archive locator:* session records, cell drafts and C4 records are in `records/recog/a1a/`; the NUMGEN C4 reply, its receiving review and the cell-draft and session reviews are cited by identity only and are not in the repository (recovery list §2)"),
("S8-3", "FC21", "FC-21", "§8 new artifact row for the FC-21 block", "line", "live",
 r"- [RID: RECOG-ART-A1A-NUM] `[v0.3.22]`",
 "{LINE}\n" r"- [RID: RECOG-ART-A1A-EXISTENCE-U] `[v0.3.23]` :: proof cell `records/recog/RECOG_v0_3_23_FC21_PROOF_CELL.md`; illustration `evidence/recog/scripts/recog_v0_3_23_value_checks.py` Part B with output `evidence/recog/v0.3.23/value_checks.json` :: written proof of RECOG-THM-A1A-PHASE-EXISTENCE-U checked against `dyad-v6.4.22` (lift, domain, indexing, amplitude inversion); float64 illustration on 12 starts in $U$ over 20000 blocks (sampled $\max\lvert r_m\rvert/Q_m^{3/2}\approx1.42\le\tfrac{403}{250}$; the $\psi$-corrected partial series varies by $<5\times10^{-3}$ from $N=10^4$ to $2\times10^4$) :: `[SESSION]` record; the illustration is `[NUM]` and not a proof input"),
# ---------------- Appendix A (new entry only) ----------------
("A-1", "M", "release entry", "Appendix A: v0.3.23 draft entry", "str", "appA",
 "## Appendix A — Version History\n\n### v0.3.22 — 20 October 2026",
 "## Appendix A — Version History\n\n"
 "### v0.3.23 — DRAFT, stage 1 (corrected intermediate; not adopted)\n"
 r"- **Basis:** the atlas advisory `records/recog/ATLAS_ADVISORY_RECOG_v0_3_22.md` as disposed by the PI on 23 Oct 2026 (`records/recog/ATLAS_ADVISORY_RECOG_v0_3_22_DISPOSITION_RECONCILIATION.md` §5), erratum E-0322-1, Methodology v1.4. Full change list, per-block RESULT ledger, claim audit and checks: `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md`." "\n"
 r"- **New RIDs (statements unchanged):** RECOG-THM-R9-COMPARATOR-INCOMPLETENESS (§6.13a corollary), RECOG-ALG-SWAP-ODD-RHO (§6.4 lemma). Named sub-statements: the radial identity under RECOG-ALG-NU3-CLOSED-FORM; the $C_0$-avoidance corollary under RECOG-THM-P2-HET." "\n"
 r"- **Imports:** NUMGEN $D_M$ and INF-1 by RID (`NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1`, v1.20.8; A1a-G1 closed); Dyadic A1a imports by RID and section at v6.4.22 with the current owner tag forms (line pins removed); §7 rows gain the Dyadic RIDs registered in v6.4.20; claim audit at `dyad-v6.4.22` and `numgen-v1.20.8`: quoted statements present at the cited RIDs in the current source." "\n"
 r'- **Status and wording:** R10 status "CLOSED (v0.3.2) — delivered and accepted"; §1 RECOG-OPEN-INTERSECTION carries the `[HYP]` tag of its §6.5 entry; frame labels and rounded equalities ($|\mu|/|c_{05}^{\rm raw}|\approx41.27$, post-$H_2$ $\approx59.12$; $|G|$ and windows with $\approx$; the original sentence is kept in the release record); R9 finite-$q_0$ pointer and partial budget; $j^6S_h=j^6R_0$; bare and combined `[RESULT]` blocks paired or split per block; stale F2 pointers; §7.2/§7.3 current state (RF-1 fulfilled; no notice state changed); §8 repository locations.' "\n"
 r"- **Unchanged:** every existing RID's statement and grade; every OPEN status (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED)." "\n\n"
 "### v0.3.22 — 20 October 2026"),
("A-2", "FC21", "FC-21", "Appendix A: v0.3.23 entry, new science line", "str", "appA",
 r"- **Unchanged:** every existing RID's statement and grade; every OPEN status (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED)." "\n\n### v0.3.22",
 r"- **New science (separately reviewed):** RECOG-THM-A1A-PHASE-EXISTENCE-U (§6.13b) — R9-free existence of $C_D^{\rm ext}$ on all of $U$ with an explicit series, from DYAD-THM-LPHASE-ROWA-REMAINDER; RECOG-ART-A1A-EXISTENCE-U (§8)." "\n"
 r"- **Unchanged:** every existing RID's statement and grade; every OPEN status (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED)." "\n\n### v0.3.22"),
]

NEW_RIDS_M = {"RECOG-THM-R9-COMPARATOR-INCOMPLETENESS", "RECOG-ALG-SWAP-ODD-RHO"}
NEW_RIDS_FC21 = {"RECOG-THM-A1A-PHASE-EXISTENCE-U", "RECOG-ART-A1A-EXISTENCE-U"}

def apply(s, edits):
    i = s.index(APPA_START); j = s.index(APPA_END)
    live = s[:i] + "\x00APPA\x00" + s[j:]
    appa = s[i:j]
    record = []
    for k, grp, row, loc, mode, region, old, new in edits:
        txt = live if region == "live" else appa
        if mode == "line":
            lines = txt.split("\n")
            hits = [l for l in lines if l.startswith(old)]
            assert len(hits) == 1, f"{k}: expected 1 line starting with prefix, found {len(hits)}"
            old_full = hits[0]
            new_full = new.replace("{LINE}", old_full)
        else:
            old_full, new_full = old, new
        n = txt.count(old_full)
        assert n == 1, f"{k}: expected 1 match, found {n}"
        assert old_full != new_full, f"{k}: no-op edit"
        txt = txt.replace(old_full, new_full)
        if region == "live":
            live = txt
        else:
            appa = txt
        record.append({"key": k, "group": grp, "row": row, "location": loc, "mode": mode, "region": region,
                       "old_sha256": hashlib.sha256(old_full.encode()).hexdigest(),
                       "new_sha256": hashlib.sha256(new_full.encode()).hexdigest(),
                       "old": old_full, "new": new_full})
    assert live.count("\x00APPA\x00") == 1
    return live.replace("\x00APPA\x00", appa), record

def main(argv):
    base, out, log = argv[1:4]
    with_fc21 = "--without-fc21" not in argv[4:]
    raw = open(base, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, "base is not adopted v0.3.22 (tag recog-v0.3.22)"
    s = raw.decode("utf-8")
    keys = [e[0] for e in EDITS]
    assert len(keys) == len(set(keys)), "duplicate edit keys"
    edits = [e for e in EDITS if with_fc21 or e[1] != "FC21"]
    t, record = apply(s, edits)
    data = t.encode("utf-8")
    open(out, "wb").write(data)
    new_rids = sorted(NEW_RIDS_M | (NEW_RIDS_FC21 if with_fc21 else set()))
    json.dump({"base_sha256": BASE_SHA, "variant": "with-fc21" if with_fc21 else "without-fc21",
               "intermediate_sha256": hashlib.sha256(data).hexdigest(),
               "declared_new_recog_rids": new_rids,
               "edit_count": len(record), "edits": record},
              open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits", "with-fc21" if with_fc21 else "without-fc21")

if __name__ == "__main__":
    main(sys.argv)
