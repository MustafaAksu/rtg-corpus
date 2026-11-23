# Independent Re-Derivation Report — Scalar-M 9-Series (against v2.7.2)

**Method:** clean-room SymPy. No import or reuse of `source_pairing.py`,
`index_placement_trace.py`, `tau_coupling_trace.py`, `secular_numerator_trace.py`.
Where possible, objects were rebuilt from defining properties (B from a 120°
Gram matrix; J_Q SOLVED from {J^T B J = B, J^2 = -I}; Delta M_f from
{traceless, Euclidean-symmetric, square = kappa^2 I}) rather than copied.
Artifact: `independent_rederivation.py`.

## Results

| # | Claim (v2.7.2) | Clean-room verdict |
|---|---|---|
| C1 | J_Q = (1/√3)[[1,-2],[2,-1]] is a B-isometry, J²=-I | **CONFIRMED** — J_Q is one of exactly two solutions of {J^T B J=B, J²=-I}; J²+I=0 exact |
| C1' | a^T B J_Q b = (√3/2) ω_ab | **CONFIRMED up to convention** — magnitude (√3/2)|ω| exact; the +sign holds for ω=a₂b₁-a₁b₂ (or equivalently the −J_Q branch with ω=a₁b₂-a₂b₁). Index-order convention, not an error. |
| C2 | Delta M_f Euclidean-sym, NOT B-self-adjoint; (Delta M_f)²=κ²I | **CONFIRMED** — DM_f²-κ²I=0; B-defect = m·μ₂·[[0,1],[-1,0]]≠0 exactly as documented |
| C3 | det(Delta M_f+τI)=τ²-κ²; τB form differs | **CONFIRMED** — det(τI form)=τ²-κ² exact; det(τB form)=¾τ²-mμ₁τ-κ² ≠ |
| C4 | Full secular Δ₃(τ²-κ²)²=σ_f²(τ²+2aτ+κ²) from K=τI-Delta M_f, Euclidean constraint, Euclidean unit source | **CONFIRMED** — r^T adj(K)^T adj(K) r - (τ²+2aτ+κ²)=0; σ_f²·num - Δ₃(τ²-κ²)² matches secular RHS-LHS exactly (residual 0) |
| C5 | Soft residue c_f^T B Π_+ B c_f = |Π_+ B c_f|² ≥ 0; Π_+ Euclidean-orthogonal | **CONFIRMED** — residue equals |Π_+ B c_f|² exactly; Π_+²=Π_+=Π_+^T verified |
| C6 | 9C: B-self-adjoint iff (M_spin2)₁₁-(M_spin2)₂₂=-2m·Im w | **CONFIRMED** — defect off-diagonal = (A-C)/2 + mμ₂; vanishes iff A-C=-2mμ₂ exact |

## Discrepancies found

1. **C1' ω-sign convention (cosmetic).** The identity a^T B J_Q b = +(√3/2)ω_ab
   holds only under a specific ω index-order / branch pairing. Both B-isometry
   branches (±J_Q) are mathematically valid; the documented "+" fixes a
   convention. Recommend a one-line convention note in §6.6/§6.9 stating the
   ω index order (ω_ab = a₂b₁ - a₁b₂ for the stated J_Q). No downstream result
   depends on this sign — the load-bearing properties (J^T B J=B, J²=-I) are
   branch-independent, and the residue/secular results use J_Q only through
   c_f = β J_Q s_* whose B-amplitude Q_c = c_f^T B c_f is branch-invariant.

2. **No substantive discrepancies.** C2–C6 reproduce exactly, including the
   v2.7.1 full-secular reconstruction and the v2.4-retraction-corrected PSD
   residue. The soft-branch sign (K=τI-Delta M_f giving +2aτ) is reproduced
   independently.

## Confidence assessment

The scalar-M frame (9A excitation, 9B forced lowered-covector source + PSD
residue, 9B-tau full secular reconstruction, 9C criterion) is now
**independently confirmed** by a derivation that did not reuse the original
scripts' objects or intermediate results. The one flag is a cosmetic ω-sign
convention with no downstream effect.

Given the series' prior correction history (v2.4 retract, v2.7 overpromote),
this clean-room pass is the due-diligence gate that was outstanding. With it
passed, the scalar-M frame is safe to treat as load-bearing for OPEN M.

## Recommended DSN action

- Add a one-line ω-index-order convention note (resolves C1').
- Record this independent re-derivation as a certification artifact (RID
  GEN-ART-REDERIV) in §8.
- No claim requires correction or retraction.
