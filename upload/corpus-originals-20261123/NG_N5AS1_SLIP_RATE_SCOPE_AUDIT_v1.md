# N-5A-S1 Slip-Rate Scope Audit v1

**Memo ID:** `NG_N5AS1_SLIP_RATE_SCOPE_AUDIT_v1`  
**Audits:** `RTG_NUMBER_GENESIS_DSN_v1.12`, `NG_N5AS1_CLOSURE_VERIFICATION_v1.md`  
**Date:** 2026-08-28  
**Verdict:** v1.11 N-5A closure confirmed; v1.12 physical 7-gap-rate promotion requires one additional locking theorem.

## 1. What is accepted unchanged

The independent verifier reproduces the exact six-step jet, the `dQ=-Q^2` cross-check, `c21`, the nonzero quartic angular term, and the one-step `+pi/3` linearization. The N-5A-S1 closure remains theorem-grade.

The preferred L-MONO statement is
\[
\Delta\phi_T=\pi/3+O(Q^{1/2}),
\]
with the older `(pi/6,pi/2)` bracket as a corollary.

## 2. The hidden premise in the v1.12 slip count

The v1.12 line
\[
6M=6N_B(M)+s(M)
\]
is valid as a literal count of 7-gaps only after proving that all relevant complete return gaps are `6` or `7` (plus bounded horizon/end effects). The certified theorem currently gives:
- infinitely many B-events;
- infinitely many non-6 gaps;
- no eventual fixed blocking `T^m`;
- numerical return alphabet `{6,7}` on the audited orbit/sweeps.

It does **not** yet give an all-domain ALG theorem excluding 5, 8, or other rare gaps.

## 3. The theorem-grade discrepancy

Define
\[
E_B(M):=6(M-N_B(M)).
\]
Since
\[
N_B(M)=M-\frac{D_M}{2\pi}+O(1),
\qquad
D_M=\tau\log M+C_D+o(1),
\]
we have
\[
\boxed{
E_B(M)=\frac{3\tau}{\pi}\log M+O(1).
}
\]
This is a valid subleading discrepancy invariant whether or not the physical gap alphabet is `{6,7}`.

## 4. The theorem-grade exponential rate that *is* available

The defect increment satisfies
\[
D_{M+1}-D_M=\tau q_M+O(q_M^{3/2})>0
\]
for sufficiently large/local `M`, and tends to zero.

Fix `alpha` and define `M_k^(def)` as the first `M` with
\[
D_M\ge \alpha+k\pi/3.
\]
The overshoot tends to zero. Using
\[
D_M=\tau\log M+C_D+o(1)
\]
gives
\[
\log M_k^{(def)}
=\frac{\pi}{3\tau}k+\frac{\alpha-C_D}{\tau}+o(1).
\]
Therefore
\[
\boxed{
\frac{M_{k+1}^{(def)}}{M_k^{(def)}}
\to
\exp\!\left(\frac{\pi}{3\tau}\right)
=
\exp\!\left(\frac{\sqrt3\pi}{6}\right).
}
\]

This is a theorem about **phase-defect thresholds**.

## 5. What remains open

`N-5A-S1-GAP-LOCK` should prove:
1. eventual local return alphabet `{6,7}`;
2. bounded endpoint bookkeeping between cumulative excess primitive steps and `E_B(M)`;
3. one-to-one or asymptotically one-to-one correspondence between `pi/3` defect-threshold crossings and 7-gap events.

Only then may the threshold rate be renamed the physical 7-gap rate.

## 6. Fatou-coordinate wording

v1.11 already proves
\[
D_M-\tau\log M\to C_D.
\]
Thus convergence/existence of the phase-defect constant is not open. The meaningful literature bridge is whether this already-defined `C_D` matches a canonically normalized Fatou-coordinate/iterative-residue constant for `F=T^6`, and whether that normalization controls the within-cell locking offset relevant to physical slip times.

This audit does not modify SG-NG-23 and does not affect the N-5A closure.
