# RER R2 — independent reviewer verdict (PR #421)

**Date:** 27 November 2026. **Reviewer:** Claude (RER independent scientific reviewer; PI assignment, PR #402 comment 7191897848). **Status:** [SESSION] / NONCANONICAL review receipt. Not a registry edit, adoption, scope change or campaign authorization.

## 1. Object

PR #421, branch `chatgpt/rer-r2-flat-sector-relevance-20261127`, exact head `da62695a44f8b5532a8770c8e070889d8662d34a`, base `c167f807` (R1 merged). Files: `records/rer/RER_R2_FLAT_SECTOR_RELEVANCE_20261127.md`, `evidence/rer/r2/` (one script, output, SHA256SUMS), orientation (shared line and ChatGPT lane). No RER body, owner DSN, pipe, upload, BASELINE or Atlas change (verified).

## 2. Verdict

**ACCEPT WITH CHANGES.**
- **What holds:** the impact matrix and the §3 mathematics are correct. All six independently checkable §3 claims reproduce (§3 below). No scientific error was found.
- **What must change:** one scope statement (C-1) must be made explicit before integration, because the PI-facing reading "class C" is broader than what §3 tests.
- **Recommendations:** the R3 hold and the S2 sequencing in §4 are agreed.

## 3. Own checks

### 3.1 Sources

- **Model definitions:**
  - The GEN v2.10 §6.3c model class gives C1 as $N_3=\lambda z+n z^2\bar z$, with $n_T=\tfrac18-\tfrac{7i\sqrt3}{72}$ and $\mu=6\bar\lambda n_T$ (L865, L894).
  - C2 is conditional on an $A$-commuting chart (L895).
  - DYAD v6.4.24 L1056 supplies that chart: $N_\Phi$ commutes with $A$, it is $C^\infty$, and $D\Phi(0)=I$.
  - OFN v0.13 L486 gives the κ-independent centre-manifold cubic $f_e=\mu(w_e|w_e|^2-\tfrac13\sum_j w_j|w_j|^2)$.
- **Hypotheses:**
  - GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO is stated for γ ∉ {0,2}, μ ≠ 0, real C³ and d = 1–3 under $H_{\rm spec}$ (L59, L867), as the K3-MODAL row says.
  - The RER formal-age bound $\deg_\tau C_d\le\lfloor(d-3)/2\rfloor$ and the formal-involution uniqueness statement "unique formal involution commuting with N with linear part −I₄" (proof dimension-free) are as cited.
- **Coverage:** all 20 supplementary records have rows, and the 16 legacy keys (T01–T05, D01–D03, C01–C02, N01–N03, G01, P01, E01) are covered.

### 3.2 Structural claims (reasoning checked)

- **Oddness (§3.1).** $A^3=-I$, so $N_\Phi$ is odd. $P_{\mathcal C}$ and slot permutation commute with common λ, so $G$ and $F_{\mathcal C}$ are odd and λ-equivariant. Quadratic readouts are invariant under common λ. Consequences:
  - Opposite-point readout differences vanish exactly, not only at leading order (C03).
  - Readouts along the common-angle circle are π/3-periodic (C04).
  - Delay Jacobians of even readouts have odd entries, so 4×4 and 2×2 determinants are even in t (C05 degree-17 and C06 degree-5 terms vanish).
- **Six-step cubic.** Derived independently: $G=\lambda w+P(m\,w|w|^2)+\dots$ gives $G^6$ cubic $=\sum_{j=0}^5\lambda^{5-j}\lambda^j m\,P(w|w|^2)=6\lambda^5 m\,P(w|w|^2)$. This is consistent with OFN L486 and $\mu=6\bar\lambda n$. λ-equivariance leaves only the $z^2\bar z$ cubic.
- **§3.6.** −I₄ commutes exactly with G, is an involution, has linear part $DG(0)^3=\lambda^3=-I$, and $F_{\mathcal C}$ is tangent to identity. By the dimension-free uniqueness proof, the unique formal involution is −I₄ itself; equivalently $G^3F_{\mathcal C}^{-1/2}=-I_4$ formally. The claim and its scope limits (no six-step-only G6, no full κ-family) are correct.
- **§3.5.** The structural formal-age argument needs $F=\mathrm{id}+O(3)$, $F_c(s,0)=0$ and an $O(3)$ trial. All three hold on the native flat slice (slot invariance). Reuse at formal level is correct.

### 3.3 Computations (independent direct iteration of the full C1 map; `evidence/rer/r2/reviewer/`)

The map is $G(w)_e=N_3(w_e)-\tfrac13\sum_jN_3(w_j)$ with $n=n_T$, iterated six times. mpmath, 60 digits, Richardson extrapolation in ε². None of the preparer's modal formulas is used inside the map.

| Claim | Result |
|---|---|
| $\mu=6\bar\lambda n_T=-\tfrac12-\tfrac{2i\sqrt3}{3}$ | PASS |
| Six-step cubic $=\mu P(w\lvert w\rvert^2)$, all three edges | residual $1\times10^{-20}$ |
| §3.2 $\Delta_4 I/Q^2$ at $d=\pm iz$ equals $\pm\sqrt3/9$ | exact to printed digits |
| §3.3 $Q^+=Q\lvert\lambda+\tfrac34nQ\rvert^2$ on $d=0$, child stays 0 | exact (residual 0) |
| §3.4 defect $D_5=b(-\tfrac{\sqrt3}{3}+i)Q^2z$ for $C_b=ibQz$, full map (includes all $O(5)$ terms of $F$) | PASS; confirms the $O(\lvert z\rvert^7)$ remainder ordering |
| §3.4 finite-age separation $(C_n-C_m)\approx(n-m)D_5$ for (1,0), (2,0), (3,1) | PASS |
| C1 common-U(1) equivariance at finite amplitude | error $4\times10^{-62}$ |

The preparer's script `evidence/rer/r2/scripts/r2_flat_cubic_check.py` was re-run here (SymPy 1.14.0, `python3 -I -B`): SHA256SUMS 2/2 OK, and the output is byte-identical. The reviewer's computation is a separate method on the full map, not on the supplied cubic. These are reviewer checks, not certificates. C2 claims were checked by reasoning only, because no explicit $\Phi$ was computed.

## 4. Required change

**C-1 (scope; evidence-boundary, not a scientific error).** Every class-C comparison in §3 is made on the **κ = 1 member**. OFN v0.13 §5.5.4 states that at κ = 1 "class C is flat" and that Q4 cycle-defect capacity exists only for κ ≠ 1 — the same flatness for which raw A1 is excluded. The record says this in §1, but the §2 header ("class-C relevance") and the PI-facing summary read as statements about class C generally. Required:
1. Head §2's class-C column "flat κ = 1 class-C slice".
2. State in §2 and §4 that the class-C regime carrying Q4 capacity (κ ≠ 1, with mean mode or centre-manifold reduction) is not tested by §3.
3. In the C05/C06/C02 rows, attribute the exact-quotient and scalar-closure findings to C1 at κ = 1 only.

This keeps the comparisons from reading as evidence about the genuine-triad class-C regime.

## 5. Notes (non-blocking)

- **N-1.** OFN L486 gives the same six-step cubic on the centre manifold for every κ ≠ 0, 2. So the purely cubic-order statements (§3.2 opposite-orientation coefficient; §3.4 leading graph defect) may extend to κ ≠ 1 on the centre manifold at cubic order. The exact statements (oddness on $\mathcal C$, $Q^+$ closure, −I₄) do not follow without the centre-manifold chart. This is a candidate check for a PI-approved class-C problem, not a claim.
- **N-2.** In the PI summary, "C03–C04: raw witnesses not valid" should read "raw witnesses do not transfer to the native class-C chart". They remain valid in raw scope, as the record's §2 says.
- **N-3.** The R3 hold (raw G6 higher-order, Stage-2; K = 8 stopped; no new campaign without separate PI authority) is agreed.

18 + 2 is unchanged. The R1 custodian and scope decisions and the GIIL019 GEN disposition remain pending with their owners.
