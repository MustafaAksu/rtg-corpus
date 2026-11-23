# N-5A-S1-INF Closure — Exact Local Phase Law, Radial Backbone, and Infinite Second Stream

**Certificate ID:** `NG_N5AS1_INF_CLOSURE_v1`  
**RID:** `NUMGEN-OPEN-N5AS1-INF`  
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.10`  
**Date:** 2026-08-28  
**Artifacts:** `ng_n5as1_inf_closure_cert_v1.py` / `.log`  
**Verdict:** **L-BACKBONE, L-MONO, L-PHASE CLOSED; INF-1 and INF-2 discharge Gate 2 and theorem-level Gate 5; N-5A-S1 CLOSED on a sufficiently small certified local primitive-dyad tube.**

## 1. Inputs and scope

Let `F=T^6`, let
\[
q_m:=Q_{\rm true}(F^m x),
\]
and work on a sufficiently small one-chart forward-invariant local tube, shrunk whenever necessary. Existing L1 gives
\[
q_{m+1}=q_m-q_m^2+\varepsilon_m,\qquad
|\varepsilon_m|\le Kq_m^{5/2}.
\]
In the primitive analytic coordinate
\[
W=u+iv,\qquad
u=\rho-\eta/2,\quad v=\sqrt3\,\eta/2,\quad |W|^2=Q_{\rm true}
\]
on the one-chart sector, the exact primitive one-step linearization is rotation by `+pi/3`.

No explicit numerical radius is claimed. The long seed-orbit runs remain `[NUM]` witnesses.

## 2. L-BACKBONE — CLOSED directly from L1

Shrink the L1 sector so that `K sqrt(q_m) <= 1/2` and `q_m <= 1/3`. Then
\[
q_m-\frac32q_m^2
\le q_{m+1}
\le q_m-\frac12q_m^2,
\]
and `q_{m+1} >= q_m/2`. Therefore
\[
\frac12
\le
\frac1{q_{m+1}}-\frac1{q_m}
\le 3.
\]
Hence `q_m = Theta(1/m)`, which already gives
\[
\sum q_m=\infty,\qquad \sum q_m^2<\infty.
\]

A refinement uses
\[
q_{m+1}=q_m(1-q_m+O(q_m^{3/2}))
\]
to obtain
\[
\frac1{q_{m+1}}-\frac1{q_m}
=1+O(q_m^{1/2}).
\]
The first comparison gives `q_m=O(1/m)`, so summing the error gives
\[
\frac1{q_M}=M+O(\sqrt M),
\]
and therefore
\[
\boxed{q_M=\frac1M+O(M^{-3/2}).}
\]
Consequently
\[
\sum_{m<M}q_m=\log M+C_Q+o(1),\qquad
\sum q_m^{3/2}<\infty.
\]

This repairs the v1.10 one-sided statement: a lower bound alone does not imply square-summability; the certified result is the two-sided/asymptotic estimate above.

## 3. L-MONO — CLOSED by exact one-step linearization plus local uniformity

The exact primitive map is analytic and, in `W`,
\[
W(Tx)=\lambda W(x)+O(|W|^2),\qquad
\lambda=e^{i\pi/3}.
\]
For nonzero sufficiently small `W`,
\[
\frac{W(Tx)}{W(x)}=\lambda+O(|W|),
\]
uniformly in direction. Shrink the punctured tube so the continuous argument branch satisfies
\[
\boxed{\pi/6<\delta_T(x)<\pi/2.}
\]
Thus the primitive lifted angle is strictly increasing and advances by less than `pi/2` each step. This is stronger than the v1.10 target `(0,2pi)` and is what the counting bridge actually needs.

### Canonical-section correspondence

A positive lap crossing of the `Theta=0` ray then has
\[
\eta^-<0\le\eta^+.
\]
The primitive update gives, writing `eta^-=-a` with `a>0`,
\[
\eta^+=-a+e^{\rho^-}-1+\sin a.
\]
If `eta^+>=0`, then
\[
e^{\rho^-}-1\ge a-\sin a>0,
\]
hence `rho^->0`; and
\[
\rho^+=\rho^-+\sin a>0.
\]
Therefore the lap crossing is exactly a canonical lift-free `B` transition of the v1.9.1 type. This also retires the prior orientation caveat.

## 4. L-PHASE — CLOSED from the exact primitive six-step iterate

The exact symbolic Taylor expansion of `F=T^6` in primitive `(rho,eta)` coordinates has no quadratic term and has cubic part
\[
\Delta\rho_3=\frac{(8\eta-7\rho)Q}{6},\qquad
\Delta\eta_3=\frac{(\eta-8\rho)Q}{6},
\]
where `Q=rho^2-rho eta+eta^2`.

Transforming this **exact primitive finite-iterate jet** to `W` gives
\[
\boxed{
W(Fx)
=
W+\left(-\frac12-i\tau\right)W|W|^2+O(|W|^4),
\qquad
\tau=\frac{2\sqrt3}{3}.
}
\]
This is independently consistent with owner RID `DYAD-THM-C21`, but the present proof uses the exact primitive finite iterate, not the cubic-vector surrogate.

For `W!=0`,
\[
\frac{W(Fx)}{W}
=
1+\left(-\frac12-i\tau\right)Q+O(Q^{3/2}).
\]
Taking the continuous local argument,
\[
\arg\!\frac{W(Fx)}W
=
-\tau Q+O(Q^{3/2}).
\]
Combining with L-MONO's increasing primitive lift, the six-step lifted law is
\[
\boxed{
\widehat\phi_{6(m+1)}-\widehat\phi_{6m}
=
2\pi-\tau q_m+r_m,\qquad
|r_m|\le Cq_m^{3/2}.
}
\]

### Exact correction of the rejected `O(Q^2)` hypothesis

The primitive quartic jet gives on the positive-`u` ray
\[
\frac{\Im(\Delta W_4/W)}{Q^{3/2}}
\longrightarrow
-\frac{25\sqrt3}{48}\neq0.
\]
Hence a uniform remainder `O(Q^2)` after subtracting `-\tau Q` is not merely unsupported; it is **false by exact Taylor algebra**. The corrected `O(Q^{3/2})` scale is theorem-grade.

## 5. INF-1 — accumulated lag is unbounded

Define
\[
D_M
:=
2\pi M-(\widehat\phi_{6M}-\widehat\phi_0)
=
\tau\sum_{m<M}q_m-\sum_{m<M}r_m.
\]
L-BACKBONE gives
\[
\sum_{m<M}q_m=\log M+C_Q+o(1),
\]
while L-PHASE and `sum q_m^{3/2}<infinity` give absolute convergence of `sum r_m`. Therefore
\[
\boxed{
D_M=\tau\log M+C_D+o(1)\to\infty.
}
\]
In particular `D_M=o(M)`.

## 6. INF-2 — primitive crossing count and non-fixed return structure

By L-MONO and the canonical-section correspondence, the canonical `B` count in the first `6M` primitive transitions equals the lap count. Therefore
\[
\boxed{
N_B(M)
=
M-\frac{D_M}{2\pi}+O(1)
=
M-\frac{\tau}{2\pi}\log M+O(1).
}
\]
Hence `N_B(M)->infinity`: Gate 2 (indefinite repeatability) closes.

If only finitely many non-6 return gaps occurred, all sufficiently late gaps would equal 6 and therefore `M-N_B(M)=O(1)`, contradicting the logarithmically divergent deficit. Thus there are infinitely many non-6 gaps.

More generally, if the `B` stream were eventually a fixed blocking `T^{m_0}`, then
\[
N_B(M)=\frac{6M}{m_0}+O(1).
\]
Since `N_B(M)/M->1`, necessarily `m_0=6`; the logarithmic deficit then gives the same contradiction. Therefore the `B` stream is not any fixed re-blocking `T^{m_0}`. The ALG form of Gate 5 closes.

## 7. N-5A-S1 verdict

Together with gates 1, 3, and 4 already closed at v1.9.1:

| Gate | Status after this certificate |
|---|---|
| 1 — relational/gauge-admissible `B` event | CLOSED `[ALG]` |
| 2 — indefinite repeatability | **CLOSED `[ALG]`** |
| 3 — co-realization with primitive `T` stream | CLOSED `[ALG]` |
| 4 — common N-2-ORD reachability order | CLOSED `[ALG]` |
| 5 — non-fixed re-blocking | **CLOSED `[ALG]`** |

Therefore:
\[
\boxed{\text{N-5A-S1 CLOSED}}
\]
on a sufficiently small certified local primitive-dyad tube, conditional on the selected continuous generator `T` under OPEN-P0.

## 8. Guards

1. This closes a **second certified recurrence/event stream**, not a nontrivial rational commensurability class. SG-NG-23 remains fully active.
2. The average primitive steps per `B` event still tends to 6. The nontrivial content is the unbounded subleading discrepancy.
3. The stronger geometric individual-slip spacing law involving `rho=exp(pi/(3 tau))` is **not** proved here; it remains a continuous-dyad diagnostic/candidate.
4. The long numerical seed need not be proved inside the existential tube for this theorem; all closure arguments are local/existential and exact.
5. N-5 may now open. It must decide what physical equivalence notion of commensurability preserves enough of the subleading return structure to avoid a vacuous label `6`.
