#!/usr/bin/env python3
"""Genesis v2.9, stage 1: corrected intermediate (a build stage, not an edition).
Round 2 (25 Oct 2026; atlas row check records/gen/ATLAS_ROW_CHECK_GEN_v2_9_STAGE1.md §3, ChatGPT concurrence §6):
B1 no dated "v2.9" markers in live text, and the withdrawn minimizer clause recorded in Appendix B, not in the theorem
block; B2 the custody clause and the independent-contribution clause defined once as standard clauses at the head of
§8 and cited by key; B3 the omega_sc convention cited at the GB-13 line. Applied in place to the round-1 edits.
Round 3 (25 Oct 2026; atlas stage-2 row check records/gen/ATLAS_ROW_CHECK_GEN_v2_9_STAGE2.md V1 and §6 G29-FINAL-01, PI
instruction of 25 Oct 2026): E30 restates the Local Tag Aliases methodology sentence for v1.4 with the bounded
migration of inherited [RESULT] blocks without a [from:] companion (counted and listed in the log, not asserted zero);
E31a–c separate C^∞ mathematical existence (imported, G-20 note), analytic existence (Dyadic OPEN 20) and physical or
network-level realization (OPEN) at G-20, in the §6.3c OPEN list and in the §5 high-risk row. The theorem statement,
its hypotheses and its proof are unchanged.
Also E29 (prerequisite for the B4 header replacement in stage 2): the header field label "**Status summary.**" becomes
"**Status summary:**", punctuation only, so that tools/check_compaction.py can read the base status summary.

Applies, to the adopted v2.8.9 file (tag gen-v2.8.9, sha256 d143673e...c6fc), the corrections authorized by the PI
on 24 Oct 2026 ("her ikisini de onaylıyorum": the 21 reconciled dispositions as stage-1 scope, and F-1 κ -> κ_f).
Sources: records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_{claude-genowner,chatgpt}_20261024.md,
records/gen/ATLAS_ADVISORY_GEN_v2_8_9_RECONCILIATION.md §3/§5, records/gen/GEN_STAGE1_IMPLEMENTATION_MATRIX.md.

Groups (labels only; every edit is applied): KF (F-1 rename), P0 (GA-01, GA-02, GA-03), P1 (GA-04, GA-05, GB-10,
GB-11, GB-12, GC-17), P2 (GA-06..09, GB-13, GB-14, GB-16, GC-18/19), APPA (new Appendix A entry, cites GC-21).

Rules:
- the input must be the adopted v2.8.9 bytes;
- KF is applied first, by line number on the base: every `\\kappa` not followed by a letter or `_` on the listed
  face-lift lines becomes `\\kappa_f`; each listed line must contain at least one; no other line is touched by KF;
- every other edit is assertion-gated: mode "str" = exact substring occurring exactly once in the live region;
  mode "line" = the old text is one entire line occurring exactly once in the live region;
- live region = everything before "## Appendix A — Version History"; Appendix A/B and the footer are not edited,
  except the APPA insertion of one new entry directly under the Appendix A heading;
- GB-13 is inserted only if its identity is verified symbolically here (gate GB13); otherwise it is skipped and
  the skip is logged;
- header identity lines (title, date, status, supersedes, companions, methodology) and the footer are left for
  the publication transform; the header lines changed are the tier line (GB-16) and the Status-summary field label (E29, punctuation only).

usage: build_gen_v2_9_stage1.py BASE OUT EDITLOG_JSON
  BASE = `git show gen-v2.8.9:dsn/RTG_GENESIS_GEOMETRY_DSN.md`
"""
import hashlib, json, re, sys

BASE_SHA = "d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc"
BASE_TAG = "gen-v2.8.9"
APPA_START = "## Appendix A — Version History {#appendix-a}\n\n"
EVID_SHA = "0ba256be3999606e936a0b14f92311600fd5bd3ff041dd3a828d7688dab6bf99"  # gen_owner_advisory_checks.py

# F-1: face-lift κ lines (1-based, in the base). Triadic-birth κ, κ_phys, κ_RTG and history are not on this list.
KF_LINES = [81, 82, 434, 437, 438, 1004, 1006, 1020, 1034, 1035, 1057, 1058, 1060, 1061, 1062, 1082, 1083]
KF_RE = re.compile(r"\\kappa(?![A-Za-z_])")
NEW_RIDS = ["GEN-THM-QH-NOGO", "GEN-THM-SINGLE-FACE-METRIC", "GEN-THM-SOURCED-JUNCTION"]

def ev(gates):
    return f"`[indep-AC]` gates {gates}"

CUSTODY = "`[custody-A]`"
STD_CLAUSES = (
 "**Standard clauses** (each defined once here and cited by key).\n\n"
 "- `[custody-A]` :: proof source not in the repository; custody (a) missing — held by neither Genesis co-owner session "
 "and not among the held records placed at `upload/gen-records/` (hash check `records/gen/GEN_UPLOAD_HASH_CHECK_20261024.md`; "
 "owner disposition records of 24 Oct 2026) — `EV-NOT-RERUN`.\n"
 "- `[indep-AC]` :: independent contribution, not a rerun of missing original code and not a recovery of the original "
 "source (Methodology §12.3): `evidence/gen/scripts/gen_owner_advisory_checks.py` (`0ba256be…bf99`), exact sympy gates "
 "K1–K4 and S1–S3 (S4 is numerical and supports no live text) — `EV-CODE`, `EV-RUN`, `EV-INDEP`.\n\n")

GB13_LINE = (r"`[ALG]` **Specialization of `GEN-THM-DELTA-QC`.** At \(I_{sc}=0\) the standalone surface "
             r"\(\Delta Q_c^{(4)}=\tfrac13Q_c^2+\tfrac14(I_{sc}+\omega_{sc})^2+\tfrac5{16}\omega_{sc}^2\) (§6.5) equals the gap "
             r"\(\tfrac13Q_c^2+\tfrac34Q_sQ_c\) above, by the identity \(Q_sQ_c-I_{sc}^2=\tfrac34\omega_{sc}^2\) for the declared "
             r"\(B\) (Gram determinant \(\tfrac34\)), with \(\omega_{sc}\) in the RTG canonical B-metric convention "
             r"`[conv: RTG canonical B-metric]`, \(I_{sc}^2+\tfrac34\omega_{sc}^2=Q_sQ_c\) (Triadic §7.1, cross-convention note for "
             r"T-6m §6.12, as read at `triad-v1.6.1`; the T-6d normalization \(\omega_{sc}^{(\mathrm{T6d})}\) differs and is not used "
             r"here); \(\omega_{sc}\) enters squared, so the index order of §6.5 does not matter. "
             r"The K4-shadow form of §6.5 gives \(\tfrac13Q_c^2+\tfrac5{12}Q_sQ_c\) at \(I_{sc}=0\) instead. This is a consistency "
             r"identity between the two certified expressions under the declared inner product, not a UV energy statement. "
             r"Check: `build_gen_v2_9_stage1.py` gate GB13 (exact).")

# (key, group, row, mode, old, new)
EDITS = [
# ---------------- P0: GA-01 sourced junction ----------------
("E01", "P0", "GA-01 §1 statement", "line",
 r"`[THM]` **Local sourced-junction theorem.** If $w=0$ and $\sigma_f\neq0$: vacuum gluing fails ($S_f = 0$ is impossible), but the constrained birth $(\Delta M_f + \tau I)d_\perp + S_f = 0$ has a valid minimizer. The foam branch is sourced-birth, not no-birth.",
 r"`[THM]` **Local sourced-junction theorem** (§6.9, `GEN-THM-SOURCED-JUNCTION`). If $w=0$, $\sigma_f\neq0$ and $\Delta_3>0$: vacuum gluing fails ($S_f = 0$ is impossible), and the constrained birth equation, which at $w=0$ reads $\tau d_\perp+S_f=0$ on $|d_\perp|^2=\Delta_3$, has exactly two antipodal solutions; selection of the physical branch is OPEN (GCL-02, §6.8). The foam branch is sourced-birth, not no-birth."),
("E02", "P0", "GA-01 §6.9 statement (single home; RID GB-10)", "line",
 r"`[THM]` **Local sourced-junction theorem.** If $w=0$, $\sigma_f\neq0$: vacuum gluing fails; constrained birth $(\Delta M_f + \tau I)d_\perp + S_f = 0$ has a valid minimizer.",
 r"`[THM]` `[RID: GEN-THM-SOURCED-JUNCTION]` **Local sourced-junction theorem.** If $w=0$, $\sigma_f\neq0$ and $\Delta_3>0$: vacuum gluing fails ($S_f=0$ is impossible). Since $\Delta M_f(0)=0$, the two branches of §6.8 coincide, $K_\pm=\tau I$, and the constrained birth equation $\tau d_\perp+S_f=0$, $|d_\perp|^2=\Delta_3$, has exactly the two antipodal solutions $d_\perp=\mp\sqrt{\Delta_3}\,S_f/|S_f|$, with $\tau=\pm|S_f|/\sqrt{\Delta_3}$; for $\Delta_3=0$ it has none. Which solution is the physical birth requires the birth energy and its constrained second variation, which are OPEN (GCL-02, §6.8); no minimizer is selected here. Proof of the algebraic statement: " + ev("S1–S2") + r" (§8); the original source GEN-ART-SOURCED-JUNCTION is not recovered. Corrected-claim record: Appendix B."),
("E03", "P0", "GA-01 §7 export (with GB-10 RIDs)", "line",
 r"`[DEF]` Genesis may export theorem-grade primitive algebra through tetrahedral quartic drift, the block-diagonal quaternionic no-go, the smooth single-face metric criterion, and the local sourced-junction theorem with their stated scopes.",
 r"`[DEF]` Genesis may export theorem-grade primitive algebra through tetrahedral quartic drift, the block-diagonal quaternionic no-go (`GEN-THM-QH-NOGO`), the smooth single-face metric criterion (`GEN-THM-SINGLE-FACE-METRIC`), and the local sourced-junction theorem (`GEN-THM-SOURCED-JUNCTION`: the algebraic statement at $w=0$, $\Delta_3>0$; physical branch selection OPEN) with their stated scopes."),
("E04", "P0", "GA-01 §2 OPEN M-foam", "line",
 r"7. **OPEN M-foam — Network phase compatibility.** Downstream of local sourced-junction structure.",
 r"7. **OPEN M-foam — Network phase compatibility.** Downstream of local sourced-junction structure (the algebraic statement only; physical branch selection OPEN, GCL-02)."),
# ---------------- P0: GA-02 / GA-03 / F-1 ----------------
("E05", "P0", "GA-02/GA-03/F-1/GC-20 §6.8 definition of κ_f, N̂ and B_* status", "line",
 r"$$\Delta M_f(w) = m\begin{pmatrix}\Im w & -\Re w \\ -\Re w & -\Im w\end{pmatrix}, \quad m = 2Q_s B_*, \quad (\Delta M_f)^2 = \kappa_f^2 I, \quad \kappa_f = |m||w|.$$",
 r"$$\Delta M_f(w) = m\begin{pmatrix}\Im w & -\Re w \\ -\Re w & -\Im w\end{pmatrix}, \quad m = 2Q_s B_*, \quad (\Delta M_f)^2 = \kappa_f^2 I, \quad \kappa_f = |m||w|.$$" "\n\n"
 r"`[DEF]` **Face-lift magnitude, sign and $B_*$.** $\kappa_f:=|m||w|\ge0$ is the face-lift magnitude. It is distinct from the triadic birth coefficient of §6.1, from $\kappa_{\rm phys}$ and $\kappa_{\rm RTG}$, and from the $\gamma$ of §6.3b–§6.3c; no parameter identification is made. For $w\neq0$ write $N(w)$ for the matrix above, so $\Delta M_f=m\,N(w)$, and $\hat N:=N(w)/|w|$, so $\Delta M_f=\operatorname{sgn}(m)\,\kappa_f\hat N$. $B_*$ is not defined in the current owner text and its sign is unknown; every statement below that depends on $\operatorname{sgn}(m)$ carries that dependence explicitly. $B_*$ is not identified with any quantity of another stream."),
("E06a", "P0", "GA-02 §6.9 9A eigenvalues", "str",
 r"eigenvalues are $\lambda_\pm=(\tau-g)\mp\kappa_f$, $\kappa_f=m|w|$, and",
 r"eigenvalues are $\lambda_\pm=(\tau-g)\mp\operatorname{sgn}(m)\kappa_f$ with $\kappa_f=|m||w|$ (§6.8; domain $m\neq0$, $w\neq0$), and"),
("E06b", "P0", "GA-02 §6.9 9A inverse and projectors", "line",
 r"$$L_{\rm sc}^{-1} = \frac{\Pi_+}{\tau-g-\kappa_f} + \frac{\Pi_-}{\tau-g+\kappa_f}, \qquad \Pi_\pm=\tfrac{1}{2}\!\left(I\pm\frac{\Delta M_f}{\kappa_f}\right).$$",
 r"$$L_{\rm sc}^{-1} = \frac{\Pi_+}{\tau-g-\operatorname{sgn}(m)\kappa_f} + \frac{\Pi_-}{\tau-g+\operatorname{sgn}(m)\kappa_f}, \qquad \Pi_\pm=\tfrac{1}{2}\!\left(I\pm\hat N\right).$$"),
("E06c", "P0", "GA-02 §6.9 9A soft-branch sentence", "str",
 r"The soft branch is $\tau-g-\kappa_f\to0$ with soft eigenvector $v_+=(\mu_1,\ \mu_2-|w|)$.",
 r"The vector $v_+=(\mu_1,\ \mu_2-|w|)$ spans the range of $\Pi_+$ for either sign of $m$. The pole at $\tau-g=+\kappa_f$ carries $\Pi_+$ if $m>0$ and $\Pi_-$ if $m<0$. The limiting-path definition of the physical soft branch is OPEN (OPEN-GEN-II-9). Both signs of $m$: " + ev("K2–K4") + " (§8)."),
("E07a", "P0", "GA-02 §2 OPEN-GEN-II-9 item 1", "str",
 r"1. Scalar-M eigendecomposition $\lambda_\pm=(\tau-g)\mp\kappa_f$, $\kappa_f=m|w|$:",
 r"1. Scalar-M eigendecomposition $\lambda_\pm=(\tau-g)\mp\operatorname{sgn}(m)\kappa_f$, $\kappa_f=|m||w|$:"),
("E07b", "P0", "GA-02 §2 OPEN-GEN-II-9 item 2", "line",
 r"2. Soft-mode identification (branch $\tau-g-\kappa_f\to0$, eigenvector $v_+=(\mu_1,\mu_2-|w|)$): `[ALG]` ✓",
 r"2. Pole–projector map with explicit $\operatorname{sgn}(m)$ (the pole at $\tau-g=+\kappa_f$ carries $\Pi_+$ for $m>0$ and $\Pi_-$ for $m<0$; $v_+=(\mu_1,\mu_2-|w|)$ spans the range of $\Pi_+$): `[ALG]` ✓; limiting-path definition of the physical soft branch: `[OPEN]`"),
("E08", "P0", "GA-02 §6.9 9A residues independent of sgn m", "str",
 r"$R^{(E)}_+$ is positive-semidefinite",
 r"With $\Pi_+=\tfrac12(I+\hat N)$ both numerators are independent of the sign of $m$ (gate K4). $R^{(E)}_+$ is positive-semidefinite"),
# ---------------- P1 ----------------
("E11", "P1", "GA-04 §2 OPEN-GEN-II-9 item 3", "line",
 r"3. Projection nontriviality — $R_{\rm soft}\neq0$ generically at $H_0=J_Qs_*$, both pairings: `[ALG]` ✓ (residue sign convention-dependent — Euclidean PSD, $B$ indefinite)",
 r"3. Projection nontriviality under the scalar-M ansatz — $R_{\rm soft}\neq0$ generically at $H_0=J_Qs_*$, both pairings (“generically”: off the residue zero set — one line for $R^{(E)}_+$, two lines for $R^{(B)}_+$ in $s_*$-space, §6.9): `[ALG]` ✓ `[scope: scalar-M ansatz]` (residue sign convention-dependent — Euclidean PSD, $B$ indefinite); beyond the scalar-M ansatz: `[OPEN]`"),
("E12a", "P1", "GA-04 SG-13", "str",
 r"Projection nontriviality is `[OPEN]`, not resolved.",
 r"Projection nontriviality beyond the scalar-M ansatz is `[OPEN]`, not resolved (under the scalar-M ansatz it holds generically, §6.9)."),
("E12b", "P1", "GA-04 §6.9 projection nontriviality", "str",
 r"**Projection nontriviality.** Prior `[RESULT]` downgraded to `[OPEN]`:",
 r"**Projection nontriviality (beyond the scalar-M ansatz).** Prior `[RESULT]` downgraded to `[OPEN]`; under the scalar-M ansatz it holds generically (OPEN-GEN-II-9A below):"),
("E13", "P1", "GA-05 raw-array premise", "line",
 r"- $M_{\rm spin2}$ anisotropy — `[OPEN-GEN-II-9C]`; diagonal splitting $-2m\,\Im w$ gives $B$-self-adjointness (generalization beyond scalar-M)",
 r"- $M_{\rm spin2}$ anisotropy — `[OPEN-GEN-II-9C]`; diagonal splitting $-2m\,\Im w$ gives $B$-self-adjointness under the additional raw-array premise $K^\top B=BK$ (`GEN-OPEN-MSPIN2-ANISO`; not required by the 9B type contract) (generalization beyond scalar-M)"),
("E14a", "P1", "GB-10 §6.7 RID", "line",
 r"`[THM]` **Universal no-go.** $T_{\mathbb{H}} = T \oplus T \Rightarrow w = 0$. No smooth local metric branch from block-diagonal extension.",
 r"`[THM]` `[RID: GEN-THM-QH-NOGO]` **Universal no-go.** $T_{\mathbb{H}} = T \oplus T \Rightarrow w = 0$. No smooth local metric branch from block-diagonal extension. Proof source: GEN-ART-QH-NOGO (§8; not in the repository)."),
("E14b", "P1", "GB-10 §1 pointer", "line",
 r"`[THM]` **Universal no-go.** $T_{\mathbb{H}} = T \oplus T \Rightarrow w=0$. Block-diagonal quaternionic extension cannot generate a smooth 3D metric branch.",
 r"`[THM]` **Universal no-go** (§6.7, `GEN-THM-QH-NOGO`). $T_{\mathbb{H}} = T \oplus T \Rightarrow w=0$. Block-diagonal quaternionic extension cannot generate a smooth 3D metric branch."),
("E14c", "P1", "GB-10 §6.9 RID", "str",
 r"`[THM]` **Smooth single-face metric criterion.** If $Q_s>0$",
 r"`[THM]` `[RID: GEN-THM-SINGLE-FACE-METRIC]` **Smooth single-face metric criterion.** If $Q_s>0$"),
("E14d", "P1", "GB-10 §1 pointer", "line",
 r"`[THM]` **Smooth single-face metric criterion.**",
 r"`[THM]` **Smooth single-face metric criterion** (§6.9, `GEN-THM-SINGLE-FACE-METRIC`)."),
("E14e", "P1", "GB-10 §8 rows for the new RIDs", "str",
 "\n\n---\n\n## §9. Collaboration and Provenance",
 "\n- [RID: GEN-THM-QH-NOGO] :: block-diagonal quaternionic no-go (statement as before; RID newly assigned) :: `[THM]` `[scope: §6.7]` — proof source GEN-ART-QH-NOGO, not in the repository"
 "\n- [RID: GEN-THM-SINGLE-FACE-METRIC] :: smooth single-face metric criterion (statement as before; RID newly assigned) :: `[THM]` `[scope: §6.9]` — proof source not identified in the owner text; not in the repository"
 "\n- [RID: GEN-THM-SOURCED-JUNCTION] :: local sourced-junction theorem, algebraic statement at $w=0$, $\\Delta_3>0$ (minimizer clause withdrawn, Appendix B) :: `[THM]` `[scope: §6.9]` — proof: " + ev("S1–S2") + "; original source GEN-ART-SOURCED-JUNCTION not in the repository"
 "\n\n---\n\n## §9. Collaboration and Provenance"),
] + [
("E15-" + k, "P1", f"GB-11 custody {k}", "str",
 f"- [RID: GEN-ART-{k}] :: {body} :: {tag} — proof-source reference required",
 f"- [RID: GEN-ART-{k}] :: {body} :: {tag} — {CUSTODY}{extra}")
 for k, body, tag, extra in [
  ("PURE-CHIRAL", r"pure chiral protection and mixed-longitudinal survival audit", "`[THM]`", ""),
  ("PHI-2TO3", r"$\Phi_{2\to3}$ one-dimensional transverse birth theorem and $Q_c \sim Q_s^3$ derivation", "`[THM]`", ""),
  ("G2-CHRONO", r"tetrahedral chronological protection $G_2(Z)=0$ over six-step block", "`[THM]`",
   "; a possible independent route via `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` is noted in the owner disposition record and is not used here"),
  ("P4-PRIMITIVE", r"primitive tetrahedral $\mathcal{P}_4(s,c,d)$ derivation / certificate", "`[THM]`",
   "; certifying script `genesis_k4_route_census.py` not in the repository"),
  ("PHASE-AVG", r"uniform independent phase-average reduction of $\mathcal{P}_4$", "`[ALG]`", ""),
  ("PHASE-CLOSURE", r"phase-moment closure and plateau shear bridge derivation", "`[ALG structure]`", ""),
  ("QH-NOGO", r"block-diagonal quaternionic no-go proof ($T_{\mathbb{H}}=T\oplus T \Rightarrow w=0$)", "`[THM]`", ""),
  ("FACE-LIFT", r"canonical face lift matrix $\Delta M_f(w)$ and constrained lift secular equation", "`[ALG]`",
   "; the algebra is re-derived: " + ev("K1, S3") + "; the UV derivation is not re-derived ($B_*$ undefined, §6.8)"),
  ("SOURCED-JUNCTION", r"local sourced-junction theorem proof", "`[THM]`",
   "; the corrected algebraic statement is proved independently: " + ev("S1–S2")),
 ]
] + [
("E16", "P1", "GB-12 c_θ⁽⁶⁾ archival status", "line",
 r"- $p=6$: $c_\theta^{(6)} = -119\sqrt{3}/648$ `[conv: Lie strict-kernel gauge]`",
 r"- $p=6$: $c_\theta^{(6)} = -119\sqrt{3}/648$ `[conv: Lie strict-kernel gauge]` — archival reference only (`DYAD-ALG-LIEGAUGE-NORM`, not imported; §7 note); not a chart or phase-moment input. The Dyadic chart quintic phase coefficient is $+89\sqrt3/324$ (Dyadic v6.4.22, $c_\theta^{(6)}$ row)."),
("E17a", "P1", "GC-17 note after G-20 (§6.3c; the only §6.3c change)", "str",
 r"Preservation under \(C^3\) conjugacy is a mathematical statement about an existing diffeomorphism, not a choice of physical network representation.",
 r"Preservation under \(C^3\) conjugacy is a mathematical statement about an existing diffeomorphism, not a choice of physical network representation." "\n"
 r"- **G-20, existence note (GC-17).** By `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (Dyadic v6.4.22; §7) a real \(C^\infty\) — hence \(C^3\) — \(\Phi\) with \(\Phi(0)=0\), \(D\Phi(0)=I\) and \(\Phi T\Phi^{-1}\) commuting with \(A\) exists, so (C2) is non-vacuous at \(C^\infty\). The analytic case remains Dyadic OPEN 20 (B-an/B-6); no network-level node exchange and no physical realization follows."),
("E17b", "P1", "GC-17 §7 import block", "str",
 "### From `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6`",
 "### From `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22`\n\n"
 "Scoped import for the §6.3c (C2) note only (`dyad-v6.4.22`). The rows above remain pinned to v6.4.13 (historical proof pins; no bulk repin).\n\n"
 r"- [RID: DYAD-THM-SMOOTH-EMBEDDING] :: $C^\infty$ flow embedding at $P_1$ (OPEN 20 B-∞ existence) supplying the $C^\infty$ germ $J$ ($J^6=\mathrm{id}$, $DJ(0)=A$, $JT=TJ$) `[scope: C^\infty local germs at P_1]` :: §6.3c G-20 note" "\n"
 r"- [RID: DYAD-THM-SMOOTH-EQUIVARIANT-CHART] :: $C^\infty$ local diffeomorphism $\Phi$ with $\Phi(0)=0$, $D\Phi(0)=I$, $\Phi\circ J=A\circ\Phi$ and $\Phi T\Phi^{-1}$ commuting with $A$ `[scope: C^\infty local germs at P_1]`. Frame note: Genesis uses it through the linear frame $W=\mathcal L(\rho,\eta)$ of `DYAD-DEF-BRIDGE-EXPORT-CONTRACT`; a linear conjugation preserves $\Phi(0)=0$, $D\Phi(0)=I$ and the commutation. The analytic case (Dyadic OPEN 20 B-an/B-6) is not imported :: §6.3c G-20 note" "\n\n"
 "### From `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6`"),
# ---------------- P2 ----------------
("E18", "P2", "GA-06 one record per RID", "line",
 r"**OPEN 5 / 2B — face-phase / healing-core insertion** [RID: GEN-OPEN-WPHASE]",
 r"**OPEN 5 / 2B — face-phase / healing-core insertion** (question carried by the `GEN-OPEN-WPHASE` record above; no second record for that RID)"),
("E19a", "P2", "GA-07 OPEN 1T out of the active frontier", "str",
 "\n1b. **OPEN 1T — Triadic v1.6 phase/interface import protocol.** Reconciled in this release: the historical $x_*$, $[0^\\circ,5.5^\\circ]$ safety wedge, no-safe-basin and phase-steering route-obstruction chain are withdrawn from current Genesis use under CN-05. Retained imports are limited to currently adopted, explicitly scoped Triadic v1.6 statements; no replacement global phase/basin theorem is imported.",
 ""),
("E19b", "P2", "GA-07 OPEN 1T into the closed list", "str",
 "**Recently closed:**\n",
 "**Recently closed:**\n- **OPEN 1T — Triadic v1.6 phase/interface import protocol.** CLOSED (v2.8.5): the historical $x_*$, $[0^\\circ,5.5^\\circ]$ safety wedge, no-safe-basin and phase-steering route-obstruction chain are withdrawn from current Genesis use under CN-05; retained imports are limited to adopted, explicitly scoped Triadic v1.6 statements; no replacement global phase/basin theorem is imported. Record: OPEN 1T below.\n"),
("E19c", "P2", "GA-07 OPEN 2 done item out of the active list", "str",
 "\n- Compute $\\Delta Q_s^{(4)}$, $\\Delta Q_c^{(4)}$ as needed:",
 "\n\nClosed sub-item:\n- Compute $\\Delta Q_s^{(4)}$, $\\Delta Q_c^{(4)}$ as needed:"),
("E20", "P2", "GA-08 6 vs 13 phase moments", "str",
 r"Cascade condition: $\langle\mathcal{P}_4\rangle > 0$.",
 r"Cascade condition: $\langle\mathcal{P}_4\rangle > 0$. This six-member set is a coarse closure ansatz; it is not a basis of the 13-moment space of OPEN 1A (§2), and no rank or linear map between the two is asserted."),
("E22a", "P2", "GA-09 §1 sign-split wording", "str",
 r"opposite signs in their declared constructions.",
 r"opposite signs for different objects in different declared constructions (not a verified passive conjugacy)."),
("E22b", "P2", "GA-09 §6.5 sign-split wording", "str",
 r"Opposite signs — NF healing is a coordinate statement, not a primitive-amplitude statement.",
 r"Opposite signs for different objects — NF healing is a coordinate statement, not a primitive-amplitude statement; no verified passive conjugacy relates them (§1)."),
("E24", "P2", "GB-14 T-6u case label", "str",
 r"reference seed ratio $R_{\rm apex}=\sqrt{21}/64$;",
 r"reference seed ratio $R_{\rm apex}=\sqrt{21}/64$ — the shear reference policy with the vector-seed reading; the four-case maximum over the two reference policies and two typed readings is $\sqrt{14}/16$ (Triadic §6.17 table, as read at `triad-v1.6.1`; companion reading, not an import);"),
("E25", "P2", "GB-16 tier wording (header line)", "str",
 r"**Programme tier:** Tier 3/4 — Integrating document;",
 r"**Programme tier:** Tier 3 — integrating study (placement recorded in Programme v1.3 §6.1);"),
("E21a", "P2", "GC-18 stale companion references", "str",
 "- `RTG_PROGRAMME_OVERVIEW_v1.2` — current programme inventory/guards; not a re-certification of Genesis claims.\n"
 "- `RTG_ONTOLOGICAL_FOUNDATIONS_v0.9` — current foundational context; not proof of Genesis birth laws or UV embeddings. *(v2.8.6 mechanical refresh from v0.8; OFN v0.9 imports Genesis identities IMP-O08-11/13 and records CUST-O09-01, answered here by the §1 alias; no OFN claim is imported into Genesis.)*",
 "- `RTG_PROGRAMME_OVERVIEW` v1.3 (`programme-v1.3`) — programme inventory, guards and interface register (§7.2); not a re-certification of Genesis claims.\n"
 "- `RTG_ONTOLOGICAL_FOUNDATIONS` v0.10 (`ofn-v0.10`) — foundational context; not proof of Genesis birth laws or UV embeddings. OFN §5.5 and IMP-O10-01 import §6.3a–§6.3c (Programme IF32); no OFN claim is imported into Genesis. *(The v2.8.6 note on OFN v0.9 and CUST-O09-01 is history at `gen-v2.8.9`; the §1 alias answering CUST-O09-01 is unchanged.)*"),
("E21b", "P2", "GC-18/19 §7 Consumers and Pins blocks", "str",
 "\n\n---\n\n## §8. Artifact Registry",
 "\n\n### Consumers (Programme v1.3 §7.2)\n\n"
 "Consumer-declared pins are the consumers' state and are not repinned here. Status of each row: declared use; no notice has been sent for the current corrections (PI decision); the release record lists what would be notified.\n\n"
 "- TRIAD (IF06) :: Triadic §7, pin v2.8.7 :: primitive tetrahedral seed and metric conventions\n"
 "- UVM / OPEN M (IF08) :: OPEN M §0.3, §7, pin v2.8.5 :: secular frame, norms, cascade test and geometry requirements; imports the 9B-tau secular numerator and uses $|mw|$ and $m=2Q_sB_*$ — affected by the renaming $\\kappa_f=|m||w|$ (same quantity), the $B_*$ status (§6.8) and the sourced-junction rescoping (to be notified)\n"
 "- RECOG (IF15) :: RECOG §7, as declared there :: $B$, $J_Q$, pairings and phase-memory context\n"
 "- RRF (IF30) :: RRF §2 table, pin v2.8.9 :: registry imports with RID; §6.2a cites §6.3c\n"
 "- OFN (IF32) :: OFN §11 rows IMP-O10-*, §5.5 :: §6.3a–§6.3c\n"
 "- RER, FMS, ER-2B (IF33–IF35) :: noncanonical records, as declared in each\n\n"
 "### Pins\n\n"
 "- Dyadic: v6.4.13 for the historical rows above (proof pins); v6.4.22 (`dyad-v6.4.22`) for the two §6.3c (C2) rows only.\n"
 "- Triadic: v1.6 for the imports above; the §6.17 table is read at `triad-v1.6.1` for the T-6u case label (§8), a companion reading.\n"
 "- Discrete Genesis: v2.12.13, blocked interface (Programme IF25); no import.\n"
 "- Programme v1.3 and OFN v0.10: companion references above, not scientific imports.\n\n"
 "---\n\n## §8. Artifact Registry"),
]

EDITS.append(("E29", "P2", "B4 prerequisite: header field label 'Status summary.' -> 'Status summary:' (punctuation only; makes the field parseable by tools/check_compaction.py for the stage-2 header replacement)", "str",
 "**Status summary.** *(v2.8.9 adopted", "**Status summary:** *(v2.8.9 adopted"))
EDITS.append(("E30", "P2", "V1: methodology sentence restated for v1.4 with the bounded migration (Local Tag Aliases)", "line",
 "`[DEF]` New and edited v2.8.5 blocks use canonical scientific status tags from `DSN_METHODOLOGY_v1.3`, with scope/assumption/provenance recorded separately. Local aliases above are permitted where explicitly declared. Untouched inherited mixed-tag text is retained under a **bounded migration** and is not claimed to have been globally retagged in this release.  ",
 "`[DEF]` This file follows Methodology v1.4 (`methodology-v1.4`) for the live-file rule (§1.1), the header and Appendix A. Blocks written or edited from v2.8.5 onward use the canonical scientific status tags, with scope/assumption/provenance recorded separately. Local aliases above are permitted where explicitly declared. Inherited blocks not re-edited since then keep their earlier mixed-tag form; in particular, inherited `[RESULT]` blocks without a `[from: TAG]` companion (Methodology §3.4) are retained under a **bounded migration**, counted and listed in the release record; pairing them is retagging work for a later edition and is not done here.  "))
EDITS.append(("E31a", "P1", "G29-FINAL-01: G-20 existence scope (§6.3c)", "str",
 r"The theorem neither requires nor supplies existence of an exactly transported realization; (C2) is vacuous if no such \(\Phi\) exists.",
 r"The theorem neither requires nor supplies existence of an exactly transported realization; (C2) would be vacuous without such a \(\Phi\). A real \(C^\infty\) \(\Phi\) is imported (next item); analytic existence is open (Dyadic OPEN 20, B-an/B-6), and no physical or network-level realization is asserted."))
EDITS.append(("E31b", "P1", "G29-FINAL-01: §6.3c OPEN list", "str",
 r"formal power-series maps as such; existence of an exactly transported realization; any physical selection (OFN/FMS).",
 r"formal power-series maps as such; existence of an analytic exactly transported realization (the \(C^\infty\) mathematical existence is imported, G-20 note); any physical or network-level realization; any physical selection (OFN/FMS)."))
EDITS.append(("E31c", "P1", "G29-FINAL-01: §5 high-risk row, not-covered column", "str",
 r"Selection of model C or of any physical model; existence of an exactly transported realization; sub-$C^3$",
 r"Selection of model C or of any physical model; existence of an analytic exactly transported realization, and any physical or network-level realization (the $C^\infty$ mathematical existence is imported, §6.3c G-20 note); sub-$C^3$"))
EDITS.append(("E15-STD", "P1", "GB-11/B2 standard clauses defined once at the head of §8", "str",
 "## §8. Artifact Registry {#sec-8-artifacts}\n\n", "## §8. Artifact Registry {#sec-8-artifacts}\n\n" + STD_CLAUSES))

APPB_START = "## Appendix B — Retired and Rejected Claims {#appendix-b}\n\n"
APPB_ENTRY = (
 "### Corrected claims (stage-1 corrections of the v2.8.9 advisory)\n\n"
 r"**[RETRACTED | RID: GEN-THM-SOURCED-JUNCTION]** Clause “the constrained birth $(\Delta M_f + \tau I)d_\perp + S_f = 0$ has a valid "
 r"minimizer” of the local sourced-junction theorem (v2.8.9 and earlier; §1 and §6.9). Reason: at $w=0$, $\Delta M_f=0$, so $K_\pm=\tau I$, "
 r"and on $|d_\perp|^2=\Delta_3$ the equation has exactly two antipodal solutions (none for $\Delta_3=0$); which one is the physical birth "
 r"requires the birth energy and its constrained second variation, which are OPEN (GCL-02, §6.8). Existence of some minimizer on the circle "
 r"is trivial by compactness and selects nothing. Corrected statement: §6.9 `GEN-THM-SOURCED-JUNCTION` (hypothesis $\Delta_3>0$ added). "
 "Record: Appendix A, v2.9 stage-1 entry; owner dispositions GA-01 (`records/gen/`).\n\n")

APPA_ENTRY = (
 "### v2.9 — stage 1 intermediate (build stage, not adopted)\n\n"
 "Corrections to v2.8.9 (`d143673e…c6fc`) from the reconciled v2.8.9 advisory; scope authorized by the PI on 24 October 2026 "
 "(21 dispositions; F-1). Changes: sourced-junction theorem rescoped to its algebraic content, the minimizer clause withdrawn (GA-01); "
 "face-lift magnitude renamed κ → κ_f, sign-explicit 9A pole–projector map, $B_*$ declared undefined (GA-02, GA-03, F-1); "
 "the withdrawn clause is recorded in Appendix B; scope words (GA-04, GA-05, GA-08, GA-09); one record per `GEN-OPEN-WPHASE` (GA-06); closed items out of active lists (GA-07); "
 "RIDs `GEN-THM-QH-NOGO`, `GEN-THM-SINGLE-FACE-METRIC`, `GEN-THM-SOURCED-JUNCTION` (GB-10); proof-source custody states (GB-11); "
 "$c_\\theta^{(6)}$ archival status (GB-12); custody and independent-contribution standard clauses defined once in §8 (GB-11); GSPLIT/DELTA-QC specialization with its $\\omega_{sc}$ convention (GB-13); T-6u case label (GB-14); tier wording (GB-16); "
 "Dyadic v6.4.22 import and G-20 note for §6.3c (C2) (GC-17); §7 Consumers and Pins, companion references refreshed (GC-18, GC-19). "
 "The OFN Q6 notice erratum (`records/gen/GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md`) is a `[SESSION]` record accepted by the owner on "
 "19 October 2026; it corrects notice wording only and is not an adopted theorem (GC-21). Methodology statement restated for v1.4, with the bounded "
 "migration of inherited `[RESULT]` blocks recorded (V1). Existence scope separated into $C^\\infty$ mathematical existence (imported), analytic existence "
 "(OPEN) and physical or network-level realization (OPEN) at G-20, in the §6.3c OPEN list and in §5 (G29-FINAL-01). §6.3a–§6.3c are unchanged except "
 "the G-20 note and these two existence-scope wordings; the theorem, its hypotheses and its proof are unchanged. "
 "Build, edit log and checker: `evidence/gen/scripts/build_gen_v2_9_stage1.py`, `evidence/gen/v2.9/`. Release record: `records/gen/GEN_v2_9_RELEASE_RECORD.md`.\n\n")

def gb13_identity():
    """Exact check: B is the unit-diagonal symmetric form fixed by J_Q^T B J_Q = B for the stated J_Q;
    then Q_s Q_c - I_sc^2 = (3/4) omega_sc^2, and the standalone ΔQ_c^(4) at I_sc=0 equals Q_c^2/3 + (3/4) Q_s Q_c,
    while the K4-shadow form gives Q_c^2/3 + (5/12) Q_s Q_c."""
    import sympy as sp
    b = sp.Symbol("b", real=True)
    JQ = sp.Matrix([[1, -2], [2, -1]]) / sp.sqrt(3)
    B = sp.Matrix([[1, b], [b, 1]])
    sol = sp.solve(list(JQ.T * B * JQ - B), b, dict=True)
    if len(sol) != 1:
        return False, f"B not unique: {sol}"
    B = B.subs(sol[0])
    if sp.simplify((JQ * JQ + sp.eye(2))) != sp.zeros(2):
        return False, "J_Q^2 != -I"
    s1, s2, c1, c2 = sp.symbols("s1 s2 c1 c2", real=True)
    s = sp.Matrix([s1, s2]); c = sp.Matrix([c1, c2])
    Qs, Qc, I = (s.T*B*s)[0], (c.T*B*c)[0], (s.T*B*c)[0]
    om = s2*c1 - s1*c2                                       # §6.5 index order; enters squared
    if sp.expand(Qs*Qc - I**2 - sp.Rational(3, 4)*om**2) != 0:
        return False, "Gram identity fails"
    q_s, q_c, w = sp.symbols("Qs Qc w", positive=True)
    stand = sp.Rational(1, 3)*q_c**2 + sp.Rational(1, 4)*w**2 + sp.Rational(5, 16)*w**2     # I_sc = 0
    shadow = sp.Rational(1, 3)*q_c**2 + sp.Rational(1, 4)*(sp.Rational(19, 24)*w)**2 + sp.Rational(359, 2304)*w**2
    sub = {w: sp.sqrt(sp.Rational(4, 3)*q_s*q_c)}
    ok1 = sp.simplify(stand.subs(sub) - (sp.Rational(1, 3)*q_c**2 + sp.Rational(3, 4)*q_s*q_c)) == 0
    ok2 = sp.simplify(shadow.subs(sub) - (sp.Rational(1, 3)*q_c**2 + sp.Rational(5, 12)*q_s*q_c)) == 0
    return ok1 and ok2, f"B offdiag={sol[0][b]}; standalone={ok1}; shadow 5/12={ok2}"

GB13_ANCHOR = r"This statement does not supply UV energy sufficiency, an apex embedding, or a physical source norm."

def apply_kf(text):
    lines = text.split("\n")
    log = []
    for n in KF_LINES:
        old = lines[n-1]
        k = len(KF_RE.findall(old))
        assert k >= 1, f"KF line {n}: no face-lift kappa"
        new = KF_RE.sub(r"\\kappa_f", old)
        lines[n-1] = new
        log.append({"key": f"KF-{n}", "group": "KF", "row": "F-1 kappa -> kappa_f", "mode": "kf-line", "line": n,
                    "count": k, "old": old, "new": new,
                    "old_sha256": hashlib.sha256(old.encode()).hexdigest(),
                    "new_sha256": hashlib.sha256(new.encode()).hexdigest()})
    return "\n".join(lines), log

def apply_edit(live, key, mode, old, new):
    if mode == "str":
        n = live.count(old)
        assert n == 1, f"{key}: expected 1 match, found {n}"
        return live.replace(old, new)
    if mode == "line":
        ls = live.split("\n")
        idx = [i for i, l in enumerate(ls) if l == old]
        assert len(idx) == 1, f"{key}: expected 1 whole-line match, found {len(idx)}"
        ls[idx[0]] = new
        return "\n".join(ls)
    raise ValueError(mode)

def build(base_text):
    assert hashlib.sha256(base_text.encode()).hexdigest() == BASE_SHA, f"base is not adopted v2.8.9 ({BASE_TAG})"
    keys = [e[0] for e in EDITS]
    assert len(keys) == len(set(keys)), "duplicate edit keys"
    t, record = apply_kf(base_text)
    i = t.index(APPA_START)
    live, appa = t[:i], t[i:]
    ok13, msg13 = gb13_identity()
    edits = list(EDITS)
    if ok13:
        edits.append(("E23", "P2", "GB-13 GSPLIT = DELTA-QC specialization (verified, gate GB13)", "str",
                      GB13_ANCHOR, GB13_ANCHOR + "\n\n" + GB13_LINE))
    for k, grp, row, mode, old, new in edits:
        assert old != new, f"{k}: no-op"
        live = apply_edit(live, k, mode, old, new)
        record.append({"key": k, "group": grp, "row": row, "mode": mode,
                       "old_sha256": hashlib.sha256(old.encode()).hexdigest(),
                       "new_sha256": hashlib.sha256(new.encode()).hexdigest(), "old": old, "new": new})
    assert appa.count(APPA_START) == 1 and appa.count(APPB_START) == 1
    appa = appa.replace(APPA_START, APPA_START + APPA_ENTRY)
    appa = appa.replace(APPB_START, APPB_START + APPB_ENTRY)
    record.append({"key": "APPA", "group": "APPA", "row": "new Appendix A entry (cites GC-21)", "mode": "appa-insert",
                   "old_sha256": hashlib.sha256(APPA_START.encode()).hexdigest(),
                   "new_sha256": hashlib.sha256((APPA_START + APPA_ENTRY).encode()).hexdigest(),
                   "old": APPA_START, "new": APPA_START + APPA_ENTRY})
    record.append({"key": "APPB", "group": "APPB", "row": "B1: corrected-claim record for the withdrawn minimizer clause", "mode": "appb-insert",
                   "old_sha256": hashlib.sha256(APPB_START.encode()).hexdigest(),
                   "new_sha256": hashlib.sha256((APPB_START + APPB_ENTRY).encode()).hexdigest(),
                   "old": APPB_START, "new": APPB_START + APPB_ENTRY})
    return live + appa, record, (ok13, msg13)

def unpaired_results(text):
    """Bounded-migration census (V1). Occurrences of the backticked tag `[RESULT]` in the live text (Local Tag Aliases ..
    Appendix A), excluding the methodology sentence that names the rule. An occurrence is paired if a `[from: ` tag
    follows it on the same line. Prose mentions of the tag are counted too (they are listed). Counted, not asserted zero."""
    import re as _re
    live = text[text.index("\n## Local Tag Aliases"):text.index("## Appendix A — Version History")]
    occ = []
    for line in live.split("\n"):
        if line.startswith("`[DEF]` This file follows Methodology v1.4"):
            continue
        for m in _re.finditer(r"`\[RESULT\]`", line):
            occ.append(("`[from: " in line[m.end():], line[:160]))
    return {"result_occurrences": len(occ), "paired": sum(1 for p, _ in occ if p),
            "unpaired": sum(1 for p, _ in occ if not p),
            "unpaired_lines": [l for p, l in occ if not p]}

def main(argv):
    base, out, log = argv[1:4]
    raw = open(base, "rb").read()
    text, record, (ok13, msg13) = build(raw.decode("utf-8"))
    data = text.encode("utf-8")
    open(out, "wb").write(data)
    json.dump({"base_sha256": BASE_SHA, "base_tag": BASE_TAG, "intermediate_sha256": hashlib.sha256(data).hexdigest(),
               "declared_new_gen_rids": NEW_RIDS, "kf_lines": KF_LINES, "gate_GB13": {"pass": ok13, "detail": msg13},
               "bounded_migration_result_census": unpaired_results(text),
               "edit_count": len(record), "edits": record},
              open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits;", "GB13", "PASS" if ok13 else "SKIPPED", msg13)

if __name__ == "__main__":
    main(sys.argv)
