# RER R1 — independent scientific review of RER-ER2B-CARRIER and RER-ER2B-T6D

**Date:** 26 November 2026. **Reviewer:** Claude (RER independent scientific reviewer; PI assignment, PR #402 comment 7191897848). **Status:** [SESSION] / NONCANONICAL review receipt. Not a registry edit, adoption, scope change, Import Ledger row or owner decision. The 18 + 2 scope changes only by PI decision.

**Independence:** written from owner and source bytes only. No preparer (ChatGPT) R1 derivation existed when this review was made, so none was read. When the preparer files its R1 work, this review is the reviewer's independent first disposition to reconcile against; it does not pre-accept that work.

## 1. Sources (bytes re-hashed at `main` `cb4994c`)

| Ref | File | SHA-256 |
|---|---|---|
| RER | `noncanonical/RTG_RELATIONAL_EMERGENCE_REGISTRY.md` at `rer-v0.2`, L637–725 | `58feee5f…7ad0` (blob `5c0897a0`) |
| ER02 | `upload/corpus-originals-20261123/RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md` | `ea26d3d1…bb5e` |
| ER03 | `noncanonical/RTG_ER2B_CONSOLIDATED_STUDY.md` at `er2b-v0.3` (governing per BASELINE; custodian PI) | `80669c69…a134` |
| ER01 | `upload/corpus-originals-20261123/RTG_ER2B_CONSOLIDATED_STUDY_v0_1.md` (RER pin) | `267c6f37…b44` |
| TRIAD16 | `upload/uvm-originals/RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6.md` §6.4 L367–402 (RER pin) | `c768687c…5b36` |
| TRIAD17 | `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` at `triad-v1.7` | `506f3403…` |

Source identities:
- ER03 Part B (L137 onward) is the v0.2 scientific body unchanged. The C12, C15A, C15B, C19 and C20 blocks are line-identical in ER02 and ER03.
- ER01 C12 (L367–397) equals ER02 C12 apart from backticks in the heading.
- 25 of the 27 non-blank lines of TRIAD16 §6.4 are verbatim in TRIAD17 (§6.4, L385–417; the heading grade wording is one of the two changed lines); the T-6d ledger is retained.
- No newer edition changes these claims, so the older pins are not defective.

## 2. Method

The checks are independent direct iteration of the model, not a check of the source's formulas against each other:
- **Model:** the DYAD primitive $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta)$ in the W-frame, with the projected update $\mathcal N=P_{\mathcal C}T^{\times3}$ and $F_6=\mathcal N^6$ (ER02 §1.1–1.2).
- **Charts:** charts $H$ are given explicitly; $H^{-1}$ is computed by fixed-point iteration.
- **Precision and extraction:** mpmath, 80 digits. Quartic increments are extracted at two scales ($\varepsilon=10^{-6},2\cdot10^{-6}$) with a Richardson step. The residuals are of order $10^{-12}$–$10^{-10}$, the expected $O(\varepsilon^2)$ remainder.
- **Evidence:** `evidence/rer/r1/scripts/` and `runs/`, hashed in `evidence/rer/r1/SHA256SUMS.txt`. Run with `python3 <script>.py` (mpmath required). These are reviewer checks (`EV-RUN`), not certificates. No ER-2B package script was executed.

## 3. RER-ER2B-CARRIER

### 3.1 Checks

| Claim (ER02/ER03) | Independent check | Result |
|---|---|---|
| C19 transformation law $\widetilde q=q+Ah_2-h_2\circ A$ for $\widetilde T=H^{-1}TH$ | First-order expansion; confirmed numerically through the σ-family below | PASS |
| C19 $\mathcal L_A$ invertible on quadratic forms | Eigenvalues $\lambda-\lambda^a\bar\lambda^b$ ($a+b=2$) and conjugates are nonzero for $\lambda=e^{i\pi/3}$ | PASS |
| C15B $h_2$ solves $\mathcal L_Ah_2=-q_G$ | Residual $1\times10^{-82}$ | PASS |
| C15B $\sum_eH(z_e)=-\tfrac{9+3i\sqrt3}{4}t^2$ for $(t,t,-2t)$, real $t$ | Exact to 80 digits | PASS |
| C20 $\Delta_4N_\sigma=(-\tfrac12+\tfrac23k^2)N_\sigma^2+2S_\sigma^2$ and $\Delta_4S_\sigma=\tfrac23(-\tfrac12+k^2)N_\sigma S_\sigma$ | Direct six-step iteration of $P_{\mathcal C}\widetilde T_\sigma^{\times3}$ for σ ∈ {0, 0.1, σ_out, 0.2, σ_in, 0.5, 1} on 4 states (collinear, maximum-area, generic); max error $1.2\times10^{-11}$ | PASS |
| C15B endpoint σ = 1: $\Delta_4\widetilde N=-\tfrac12\widetilde N^2+2\widetilde S^2$ | Included above | PASS |
| C19 independence from higher chart jets | Adding $c_3z^2\bar z+c_4\bar z^3$ to $H$ leaves both formulas unchanged (σ = 0.2, 0.7; error $2\times10^{-10}$) | PASS |
| C20 thresholds $\sigma_{\rm out}=1-\sqrt3/2$, $\sigma_{\rm in}=1-1/\sqrt2$ | Exact consequence of the verified formulas with $0\le S^2\le N^2/12$ (ER02 §1.2): uniformly positive iff $k^2>3/4$, uniformly negative iff $k^2<1/2$, mixed between; chirality leading growth iff $k^2>1/2$ | PASS |
| C20 $\mu=-\tfrac12-\tfrac{2i\sqrt3}{3}$, $\mu_{22,G}=-1-\tfrac{i\sqrt3}{2}$ | $w^2\bar w$ coefficient of $T^6-\mathrm{id}$ by circle sampling | PASS |
| C20 closed form $\mu_{22}(q)=(9+3i\sqrt3)uv-(3+3i\sqrt3)\lvert v\rvert^2-6\lvert t\rvert^2$ | Four random $q$; max error $2\times10^{-12}$ | PASS |
| C15A passive transport preserves dynamics | $\mathcal N_H=H^{-\times3}\mathcal NH^{\times3}$ on $\mathcal C_H$ is a conjugacy; the claim follows from that identity | PASS (definitional) |

Not checked: the general χ(q) closed form for arbitrary q. It was tested only at $\chi_G$ and along the σ-path through $\Delta_4S$.

### 3.2 Verdict: ACCEPT SCOPED

The record's distinction ("passive transport is not reimposed additive closure") and the v0.2 C19–C20 content are mathematically correct at the scope ER02 declares:
- formal local statements at the stated jet order for a family of distinct model definitions;
- the uniform-sign neighbourhood for fixed σ is uncertified;
- the quartic-zero directions at σ_out and σ_in are OPEN;
- σ, the chart and the carrier are not selected.

No scientific error or counterexample was found. The source bytes now exist and this review has verified the content, so the earlier blocker "not authenticated by this RER revision" is met for C19–C20.

### 3.3 Required, if the PI moves this record into scope

- **C-1 (record text).** Replace the "not authenticated" clauses and the "Missing primary input" paragraph with:
  - the pin `er2b-v0.3`, Part B, C15A–C20 (equal to v0.2);
  - this receipt;
  - the stated limits.
  Keep "No C19/C20 coefficients … imported from recollection" true by quoting only from the pinned bytes.
- **C-2 (naming guard).** ER03 §A.4 calls the C20 endpoint σ = 1 "the transported class". That class is the FMS/OFN transported κ-family, cubic-order coincident only. It is **not** C15A passive transport of the raw model, which keeps the **outward** return. The record must keep the two senses of "transported" apart and must not carry raw (σ = 0 or C15A) results to class C, or the reverse (R2 boundary).
- **C-3.** Keep the "no physical carrier selection" and "no RRF profile" non-transfers.

## 4. RER-ER2B-T6D

### 4.1 Checks

| Claim | Independent check | Result |
|---|---|---|
| Exact edge-slot identity $F(s,-c)=(F_s,-F_c)$ | Swapping slots 2 and 3 commutes with $T^{\times3}$ and $P_{\mathcal C}$; numerically exact at finite ε = 0.01 (error $10^{-83}$); under it $(Q_s,Q_c,I_{sc},S)\mapsto(Q_s,Q_c,-I_{sc},-S)$ | PASS |
| C12 quartic increments $\Delta Q_s,\Delta Q_c,\Delta I_{sc},\Delta S,\Delta N$ | Direct iteration, 3 generic states; max error $4\times10^{-12}$ | PASS |
| Modal $\Delta Q_T^{[4]}=Q_T^2/8+I_T^2/6+\Omega_T^2/2+2\sqrt3I_T\Omega_T/9$ | C12 $\Delta Q_s$ under $Q_T=2Q_s$, $I_T=2I_{sc}$, $\Omega_T=-2S$, plus the Gram identity $Q_sQ_c=I_{sc}^2+S^2$ | PASS |
| Modal $\Delta Q_s$ reflection-even | Follows from the identity; C12 contains only $Q^2$, $S^2$ and $I_{sc}S$ | PASS |
| Historical T6d $\Delta Q_s$ has reflection-odd terms | TRIAD16 L380 $\Delta Q_s^{(0)}$ contains $18I_{sc}Q_s$ and $6\sqrt3Q_s\Omega$, odd under $(I_{sc},\Omega)\mapsto(-I_{sc},-\Omega)$ (the T6d branch sign flips) | PASS |

### 4.2 Verdict: ACCEPT SCOPED

The negative comparison holds as stated. Under any correspondence that preserves the modes and the child reflection, with a fixed or reflection-compatible positive clock, a reflection-equivariant modal increment cannot equal a vector field with reflection-odd $Q_s$ terms. Equality of a discrete map with an ODE time-one map is not assumed. This independent reasoning adds two points:
- **Convention-independent.** The argument does not depend on the orientation convention. Replacing $\Omega_T=-2\Omega_G$ with $+2\Omega_G$ preserves parity classes, so the result needs only reflection-compatibility.
- **No K mismatch.** Both models satisfy the Gram identity ($K\equiv1$). The rejection is a parity obstruction; no mismatch of the independent-K kind is involved.

### 4.3 Required, if the PI moves this record into scope

- **T-1 (scope sharpening).** State the correspondence class explicitly: reflection-equivariant identifications of $(Q_s,Q_c,I_{sc},\Omega)$ and reflection-even clocks. A state-dependent clock odd in Ω, or an identification that breaks reflection, is outside the result. The record's "not arbitrary conjugacy" already implies this; it should be written as a hypothesis.
- **T-2 (pins).** C12 may be pinned to `er2b-v0.3` Part B, equal to the v0.1 pin. The T6d pin to TRIAD16 §6.4 stays valid; TRIAD17 §6.4 retains the ledger.
- **T-3.** [OPEN] Descent of T6d from its own producer and physical model correspondence stay open, unchanged.

## 5. Classification and custodian disposition

- **Classification:** No scientific error and no counterexample in either record. Evidence gaps: none remaining in the declared scope. The χ(q) general formula was not independently tested; neither record imports it. Editorial items: C-1, C-2, T-1, T-2.
- **ER-2B custodian disposition required (PI, per BASELINE):**
  1. Confirm that `er2b-v0.3` Part B is the governing pin for C12, C15A, C15B, C19 and C20 in RER.
  2. Confirm the C-2 reading of ER03 §A.4: the σ = 1 "transported class" is the FMS/OFN κ-family coincidence at cubic order, not C15A passive transport.
- **Scope:** Moving either record from EXCLUDED_BLOCKED into accepted scope (changing 18 + 2) is a PI decision. These verdicts are inputs to it, not the decision.

## 6. Addendum — PI native rerun (26 November 2026)

- **Rerun:** The PI re-executed the three scripts on the Ubuntu server, at branch head `7adf8e21`, after a fresh `pip install mpmath`.
- **Result:** Every printed value matches `evidence/rer/r1/runs/` to the printed digits. That covers the residuals, the σ-family errors, the cubic-jet errors, μ, μ22,G, μ22(q), C12 and the reflection identity.
- **Duplicate output:** `carrier_check2.py` and `t6d_check.py` import `carrier_check.py`, which runs its checks again on import, so its lines appear more than once. This is cosmetic and changes no value. The stored outputs show the same duplication.
- **Status:** The run is now reproduced on a second machine. It remains a reviewer check, not a certificate.
