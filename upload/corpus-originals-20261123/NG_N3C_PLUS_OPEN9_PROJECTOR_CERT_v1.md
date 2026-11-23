# NG N-3C+ / OPEN-9 Character-Projector Certificate v1

**Date:** 2026-08-27  
**Scope:** continuous dyadic p-resonance representation kinematics; no discrete-branch dynamics transfer.  
**Status:** `[RESULT][from: ALG/MATH]` for the projector/charge statements and the p=6 degree-2 no-cascade consequence; OPEN-9 nonlinear coefficient cancellations remain dynamical unless separately certified.

## 1. Correct vector-character action

Let
\[
R(Z)=\lambda Z,\qquad \lambda=e^{2\pi i/p},\qquad \lambda^p=1.
\]
For a complex vector-map component `h`, the relevant cyclic action is conjugation
\[
\mathcal C_R h:=R^{-1}\circ h\circ R,
\]
not the scalar phase pullback alone. For the monomial
\[
M_{ab}(Z,\bar Z)=Z^a\bar Z^b,
\]
we obtain exactly
\[
\mathcal C_R M_{ab}
=\lambda^{-1}(\lambda Z)^a(\bar\lambda\bar Z)^b
=\lambda^{a-b-1}M_{ab}.
\]
Thus the natural vector charge is
\[
\boxed{\chi_p(a,b)=a-b-1\pmod p.}
\]
The extra `-1` is the output-vector charge. This is why the resonance rule cannot be derived from a scalar term `rho^a chi_b`: radial powers are rotation-neutral and do not reproduce the `a-b` charge.

## 2. Roots-of-unity projectors

For residue `r in Z_p`, define
\[
\Pi_r:=\frac1p\sum_{j=0}^{p-1}\lambda^{-jr}\mathcal C_R^j.
\]
Then
\[
\Pi_r M_{ab}
=\frac1p\sum_{j=0}^{p-1}\lambda^{j(a-b-1-r)}M_{ab}.
\]
The roots-of-unity sum is `p` iff `a-b-1-r == 0 mod p`, and zero otherwise. Hence
\[
\boxed{\Pi_rM_{ab}=\delta_{\chi_p(a,b),r}\,M_{ab}.}
\]
The resonant projector is `Pi_0`, so
\[
\boxed{\Pi_0M_{ab}\neq0\iff a-b\equiv1\pmod p.}
\]
This recovers the one-step p-resonance condition as pure representation kinematics.

## 3. First-nonlinear p-step averaging theorem

Let a one-step map have linear part `R` and lowest nonlinear homogeneous degree `d>=2`:
\[
f=R+h_d+O(d+1).
\]
At homogeneous degree `d`, only one insertion of `h_d` is possible. Therefore
\[
[f^p-\mathrm{id}]_d
=\sum_{j=0}^{p-1}R^{p-1-j}h_dR^j
=pR^{-1}\Pi_0h_d.
\]
Thus every nonresonant degree-`d` slot vanishes in the p-step jet **without any nonlinear cascade calculation**.

### p=6 primitive-dyad consequence

The primitive dyad has quadratic nonlinear terms, so `d=2`. For `p=6`, the degree-2 monomials have no charge-zero slot. Therefore
\[
\boxed{[T^6-\mathrm{id}]_2=0.}
\]
This is the representation-theoretic content of the existing degree-2 no-cascade/eigenframe bypass: the quadratic p-step cancellation is kinematic.

## 4. p=6 resonant support through degree 5

Solving `a+b=D` and `a-b == 1 mod 6` gives:

| Degree D | Resonant slots |
|---:|---|
| 2 | none |
| 3 | `(2,1)` |
| 4 | none |
| 5 | `(3,2)`, `(0,5)` |

This reproduces the existing dyadic resonance table.

For a pure anti-holomorphic monomial `(0,b)`, resonance requires
\[
-b\equiv1\pmod p,
\]
so the first positive solution is
\[
\boxed{b=p-1.}
\]
This is a kinematic theorem about **allowed one-step resonant support**. It is not by itself a theorem that every raw p-step anti-holomorphic coefficient below `p-1` vanishes, because higher-degree p-step coefficients can receive nonlinear cascades from lower-degree terms.

## 5. Charge reachability versus coefficient cancellation

The conjugation action `C_R` is an automorphism of the polynomial/Lie operations used in normal-form algebra. If two homogeneous objects have charges `r` and `s`, their Lie bracket (and corresponding multilinear cascade term) has charge
\[
r+s\pmod p.
\]
Therefore representation theory provides a **necessary reachable-charge rule**:

> A nonlinear cascade can contribute to a target residue only if the source charges combine to that residue.

If no such charge combination exists, the slot is structurally forbidden. If it does exist, representation theory only permits the slot; it does not determine whether its coefficient survives or cancels.

This is the exact boundary between kinematic selection and nonlinear/cyclotomic cascade algebra.

## 6. q=4 subgroup test: p=8 versus p=12

For a divisor `q|p`, put `s=p/q` and use the subgroup rotation `R_q=R^s`, whose eigenvalue has order `q`. The subgroup resonant projector keeps
\[
a-b\equiv1\pmod q.
\]
For the OPEN-9 target `(a,b)=(0,3)`,
\[
0-3-1=-4\equiv0\pmod4.
\]
Hence `(0,3)` is **q=4 subgroup-allowed** for both `p=8` and `p=12`.

The active Dyadic ledger records:

- `p=8,q=4,(0,3)`: exact cancellation;
- `p=12,q=4,(0,3)`: exact nonzero value `-13+15 sqrt(3)/2`.

Since the same q=4 character selection permits the channel in both cases,
\[
\boxed{\text{the p=8 cancellation is not forced by subgroup representation theory alone.}}
\]
The p=8/p=12 split is genuinely nonlinear/cyclotomic cascade information. This is a direct N-3C+ contribution to OPEN-9.

## 7. Scalar Bessel-residue projector — separate object

For scalar phase characters `chi_m(eta)=exp(i m eta)`, define the scalar residue projector
\[
P_r^{\rm sc}=\frac1p\sum_{j=0}^{p-1}\omega^{-jr}(R^*)^j,
\qquad R^*\chi_k=\omega^k\chi_k.
\]
Using the exact primitive pullback
\[
T^*\chi_m
=e^{im(e^\rho-1)}\sum_{n\in\mathbb Z}J_n(-m)\chi_{m+n},
\]
one gets
\[
\boxed{
P_r^{\rm sc}(T^*\chi_m)
=e^{im(e^\rho-1)}
\sum_{\ell\in\mathbb Z}
J_{r-m+\ell p}(-m)\chi_{r+\ell p}.
}
\]
For `p=6`, `r=1`, `m=1`,
\[
P_1^{\rm sc}(T^*\chi_1)
=e^{i(e^\rho-1)}\sum_{\ell\in\mathbb Z}J_{6\ell}(-1)\chi_{1+6\ell}.
\]
The first noncentral sidebands have coefficient
\[
J_{\pm6}(-1)\approx2.09383380023893\times10^{-5}.
\]

**Guard:** these Bessel coefficients are exact primitive Fourier-mixing coefficients. They are **not** OPEN-9 Birkhoff/Lie cascade coefficients. An explicit coordinate/jet bridge would be required before identifying them.

## 8. Epistemic split achieved

### Forced by representation theory

- charge `chi_p(a,b)=a-b-1 mod p`;
- one-step resonant rule `a-b == 1 mod p`;
- direct cyclic-average annihilation of nonresonant first-nonlinear slots;
- p=6 quadratic p-step cancellation;
- p=6 resonant support table through degree 5;
- first pure anti-holomorphic resonant support `(0,p-1)`;
- necessary charge-reachability constraints on nonlinear cascades.

### Not fixed by representation theory

- the numerical value of an allowed coefficient;
- cancellations among multiple allowed cascade paths;
- the p=8 versus p=12 q=4 `(0,3)` split;
- the universal low-degree raw anti-holomorphic vanishing conjecture beyond cases where no cascade is possible;
- OPEN-9 missing-slot multiplicities inside reachable charge sectors.

## 9. Certificate artifact

`ng_n3c_plus_projector_cert_v1.py` verifies the residue tables and the q=4 permission statements by exact integer arithmetic. It deliberately does not compute nonlinear OPEN-9 coefficients.
