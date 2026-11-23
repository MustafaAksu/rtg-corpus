# RER r4 Triadic addendum — answers to the 17 Oct record review (21:32)

**Status:** NONCANONICAL. This note amends `RER_v0_2_r4_TRIAD_RECORD_CANDIDATES_20261017.md` (`80b4e20e…238b`) in two places.

## 1. Kernel result: independent fast replay

**New script:** `triad_cubic_kernel_chiral_replay.py`. It runs in about 1 s and needs only numpy.

**Independence from the first check:**
- The original check `TRIAD_CK_PY` uses the triadic jet engine and exact rationals.
- The replay does not use that engine. It builds X₃ from the K3 SESSION record v0.1.2 chiral identities, as printed in Genesis v2.8.6 §6.3a(d):
  - u̇ = c₀u|u|² − iβ*Nu
  - v̇ = c₀v|v|² − iβ*Nv
  - N = |u|² + |v|²
  - c₀ = 1/6 + i√3/9
  - β* = 2√3/9
- Kernel dimension does not change under the real-linear coordinate change (s,c) ↔ (u,v).

**Method:**
- The operator is complexified, with u, ū, v, v̄ treated as independent variables. For a real operator, the real dimension of its kernel equals the complex dimension of the kernel of its complexification.
- Rank is computed by SVD in float64.
- Every rank decision has to clear a singular-value gap larger than 10⁶ before it is accepted.

**Result:**

| | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 |
|---|---|---|---|---|---|---|
| dim ker(ad_{X₃}) | 0 | **2** | 0 | 0 | 0 | 0 |

- Smallest kept singular value: at least 0.13.
- Next singular value: at most 1.4·10⁻¹⁶.
- Exit 0.

**Negative control (`--control-real`):** c₀ real and β* = 0. This gives dimension 6 at k=3, because the rotations survive, and the script exits 1.

**What is not a control:** β* = 0 on its own (two decoupled dyads) also gives dimension 2 at k=3. So that case is not used as a control, and the dimension-2 kernel is not tied to the chiral coupling.

**Evidence status for r4:**
- `TRIAD_CK_PY` (exact): source-executed.
- `TRIAD_KR_PY` ([NUM], independent source data and implementation): source-executed.
- Receiving replay: pending until the reviewer runs one of the two scripts. The new script runs in about 1 s.

**Scope:** This agrees with the review's note. A dimension-2 cubic kernel bounds the lowest-order term of any element of the formal centralizer. It does **not** show that the formal centralizer is two-dimensional. Whether the second direction extends to all orders is still open (G6).

## 2. Birth-graph record (d): contract made explicit

Replace (d) in RER-TRIAD-BIRTH-GRAPH-INVOLUTION with:

> [ALG] **(d) Remainder-order bookkeeping under a stated child contract.**
>
> **Child contract used here:** the child functional is the **graph value itself**. A birth places the state on a graph c = 𝒞(s) over the current parent, inside the conditional modal model (reprojection after each primitive step, F = 𝒩⁶). Its remainder order p is the leading degree of 𝒞(s) − κQ_sJ_Qs.
>
> Under this contract:
> - the Ŝ_triad-invariant completion has p = 4 (C₄ = G₄/2 ≠ 0 for κ̃ ≠ 0);
> - every formal age sheet has p ≥ 5 (𝒞₄ ≡ 0).
>
> So under this contract, Ŝ-compatibility of the birth graph and the Genesis fifth-order branch (OPEN 5/2B, GCL-06) are mutually exclusive.
>
> [OPEN] The following are not established by this record:
> - which child functional, if any, is physical;
> - whether the birth is a graph initialization at all;
> - whether either graph is the post-birth law;
> - selection of the p = 4 or p = 5 branch.
>
> An Ŝ-compatible graph existing does not select p = 4, and the age family does not select p = 5.

## Pins

| file | SHA-256 |
|---|---|
| triad_cubic_kernel_chiral_replay.py | 5447338c3fd30064b51e0360c0724aa9350ed8a34b3d78a5570ffaf2185f5584 |
| triad_cubic_kernel_chiral_replay.log | 641d3c34b35d0c7d0cb43d3817c4ef50d976c8b938758ae7d61671f4de01363b |
