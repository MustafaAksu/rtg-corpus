---
from: UVM
to: GEN
date: 2026-11-23
kind: request
object: UVM-PROP-JPERP-01 (records/uvm/UVM_OPEN_M6_STAGE1_RESULTS.md §6, PR #366 at 0c2292a, not merged); GEN §6.7 minimal UV completion; GEN-OPEN-SOURCE-PAIRING; GEN-DEF-PRIMITIVE-METRIC
tags: [uvm-v0.7.1, gen-v2.10, dyad-v6.4.24, rrf-v0.8.4]
state: open
blocks: OPEN-M-6 stage 2 (contract C3, physical discrimination of the source models)
---
UVM asks Genesis to review a proposal, under the PI's decision of 23 Nov 2026 ("OPEN-M(UVM) önerir Genesis inceler"; preparer-reported in the record's §1). It is a [SESSION] proposal, accepted only as such by the second UVM co-owner (review `6020412456`). Nothing in it is adopted and no Genesis text is asserted.
**Proposal (JP1–JP7):** UV space `q = z + jy`, `ja = āj`, with `Π_∥ = {y = 0}`; ℤ₆ lifted as left multiplication by `λ` in an equivariant dyad chart named per claim (NF through degree 6, or `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`); constant vector-fibre action `P = λ̄` with `P⁶ = I`; covariance in update form (`s(Jx) = P_{fx}s(x)`, `M(Jx)P_x = P_{fx}M(x)`); clock: primitive `T`.
**Why it matters (stage-1 finite-jet results, independently reproduced):** with complex-linear re-trivializations only, the NF-native source `jΛz̄` is ℤ₆-covariant and the W-native `jΛW̄` is not. With real-linear state-dependent gauges the two sources are section-equivalent at all orders locally, and only `M`, the action and the observable can distinguish them.
**Questions for the Genesis owners:**
1. Is `q = z + jy` with this `Π_∥ / Π_⊥` split the embedding the harness `T_ℍ^UV` of §6.7 uses? If not, which?
2. Which lift of ℤ₆ does the harness commute with, and does it act on the source by the vector action on `Π_⊥` or by the contragredient `(P⁻¹)ᵀ` on `Π_⊥*`?
3. Which `B` lowers the source on `Π_⊥` (`S_f = Bc_f`), in which basis, and does `PᵀBP = B` hold there? (In the primitive frame `GEN-DEF-PRIMITIVE-METRIC` with `P = A⁻¹` it holds exactly, but that metric is not automatically the fibre metric.)
4. Is the admissible structure group of the transverse bundle `GL₁(ℂ)` (JP5) or wider, and on what physical ground? UVM treats it as an open hypothesis.
**Sought:** a Genesis owner view on 1–4, or "not decidable from Genesis text". No adoption, repin or RID is requested.
**2026-11-25 — sender update:** PR #366 is merged (`bfe0c474b6354ec8cd32cfe5e3f6138f93be1b64`, reviewed head `0c2292a763b5a07b8c903fd3bcbdc49f1d6eb22f`). The original “not merged” wording records the filing checkpoint. Adopted `uvm-v0.7.2` §2/§8 records the proposal as SESSION only. The request, its four questions, source tags, receiver state and C3 block are unchanged; no GEN answer or physical adoption is inferred.
