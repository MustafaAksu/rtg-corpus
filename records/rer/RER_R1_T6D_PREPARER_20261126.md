# RER R1b — T6D source and exact-algebra receiving assessment

**Date:** 26 November 2026. **Status:** [SESSION] / NONCANONICAL; ChatGPT preparer proposal, not a reviewer verdict or adoption. Checkpoint main cba0213e7ef04e6126ce87eac9c378c18f2ab30c. RER-ER2B-T6D remains BLOCKED_SOURCE_UNVERIFIED / EXCLUDED_BLOCKED until separate PI decision.

## 1. Source contract and limitations

RER v0.2 §6 L637–673. ER-2B v0.3 Part B C12 L498–528, C10/C11 and model §1.1–1.2; v0.2 and original archive checked in companion RER_R1_CARRIER_PREPARER_20261126.md. ER-2B v0.1 C12 L367–397 text agrees with v0.2 C12 apart from heading grade formatting; retain historical pin. Proposed current noncanonical pin er2b-v0.3 Part B, pending custodian disposition. ER-2B v0.3 SHA-256 80669c69ada042230c36883f5f1de7a0738e637793a4d1cf4b590990da57a134; v0.2 SHA-256 ea26d3d1a4853ac88d1938dcb66c76eda4d55980ebf6f4d61091b97d67b2bb5e. Source archive and C12 checker inspected at targeted scope (not run): ER2B_OBSERVABLE_RESPONSE_v1.zip SHA-256 06d5e0c90d864ee8f5ab5ecfa7cadac5e76272a0b4754955bf43ecdcbc4b82b1, member ER2B_OBSERVABLE_RESPONSE_v1/scripts/check_observable_response.py SHA-256 920347cb5c0ba07a97e0b198f1104c79cd79a5a58440c1e0bdedf8e1987ae6d9. Its source-tensor/observable and Gram-constraint assertions are distinct from our direct recurrence.

Historical TRIAD v1.6 actual recovered path upload/uvm-originals/RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6.md, blob 0e9a5104ef42d2f97aca6ba2436d2abc14847fd9, SHA-256 freshly recomputed c768687cec6d52ffd358dc362cee4348f076160943564adaa461e6c7c4595b36 = RER historical pin; §6.4 L367–402 fully read, r^0 formula L380. Governing TRIAD v1.7 tag triad-v1.7 (digest verified S1), §6.4 L385–419, orientation §6.18 L745–762 targeted; retains r^0 polynomial and the root model. The T-6e raw-determinant rate correction does not amend T-6d. Historical GENESIS_ER2B_REPLY_TO_TRIADIC_20261010.md (upload/corpus-originals-20261123/, blob 92258a0b8c12f5e7f411e807be00b0875011e3b0) read in full; §A/B explicitly separates reflection, normalized readout, clock and own-producer descent. TRIAD_RER_v0_2_r2_RECORD_REVIEW_20261014.md read in full; scoped historical receipt only. ERADD (RER_T03_PROPOSED_ADDENDUM.md) and t6d_generalized_ode.py not located in the inspected 23 Nov intake inventory or loose paths checked; no proof or execution attributed to them. The historical ledger and GEN receiving reply suffice for the stated polynomial comparison, not authentication of every historical producer or the independent graph-force descent. No archived code executed. No blanket evidence-gap closure.

## 2. Derivation and checks

[SESSION] [ALG] Use the exact CARRIER recurrence with k=1 (sigma=0), per-step projection, six primitive compositions, not one projection after six isolated steps. Let z=W(s), d=W(c), Qs=|z|^2,Qc=|d|^2,I=Re(z bar(d)), S=Im(z bar(d)). The derived first nonlinear state jet is cubic. With N=3Qs/2+2Qc the exact quartic coefficients recovered independently are
    Delta4 Qs=Qs^2/4+Qs Qc/3+2S^2/3-4 sqrt(3) I S/9,
    Delta4 Qc=Qs Qc/4+Qc^2/3+S^2/2+sqrt(3) I S/3,
    Delta4 I=N I/6+sqrt(3)(Qs/6-2Qc/9)S,
    Delta4 S=NS/3, Delta4 N=N^2/6+2S^2.
The Gram differential Qc Delta4 Qs+Qs Delta4 Qc-2 I Delta4 I-2S Delta4 S=0 is checked exactly. O(||X||^5) remainders are not controlled numerically here; signed-Gram full analytic closure is still refuted by the separate RER C03 witness.

[SESSION] [ALG] Slot permutation Pi=(23) commutes exactly with the identical unary update and P; on modal coordinates Pi(s,c)=(s,-c), hence all iterates including F6 commute with Pi on the corresponding full domain. Qs,Qc are even, I,S odd as readouts. This exact argument is not restricted to the cubic; cubic reflection separately tested. It is not a physical node/pole exchange or a proof of an autonomous signed-Gram factor.

[SESSION] [ALG] TRIAD v1.7 §6.18 uses B_T=2 B_G and Omega_T=-sqrt(3) omega_raw with omega_raw=s_eta c_rho-s_rho c_eta. Thus for identical planar component inputs, Q_T=2 Qs, Q_cT=2 Qc, I_T=2 I, Omega_T=-2S. This is a normalization bridge, not a state/model identification. Both satisfy Q_T Q_cT=I_T^2+Omega_T^2; on Q_T,Q_cT>0 both have K=1. C12 then gives (using that Gram identity)
    M=Delta4 Q_T=Q_T^2/8+I_T^2/6+Omega_T^2/2+2 sqrt(3) I_T Omega_T/9.
Historical T-6d §6.4 r^0 diagnostic coefficient is
    D=-24 Q_T^2+18 I_T Q_T-18 I_T^2-12 sqrt(3) I_T Omega_T+6 sqrt(3)Q_T Omega_T-6 Omega_T^2.
Under (I_T,Omega_T)->(-I_T,-Omega_T), M is even while D-D_reflected=36 I_T Q_T+12 sqrt(3) Q_T Omega_T. The root branch sign changes under this comparison; a single fixed root branch is not itself a reflection-invariant domain. This obstruction needs an identification respecting modes/readouts and reflection on the compared states, and a fixed or reflection-even positive clock factor (or a smooth clock with nonzero positive limit for a leading-jet comparison). Arbitrary state-dependent clock or non-equivariant change is outside scope. ODE coefficient-time in units of one six-step block is not the exact discrete map or a claim about its time-one map.

[SESSION] [ALG] Additional exact sign check at matched planar pairs Q_T=Q_cT=q>0, I_T=0, Omega_T=+/-q (positive radicand q^2):
    M=(5/8)q^2,
    D=(-30+/-6 sqrt(3))q^2<0.
Thus at these matched readouts even an arbitrary positive scalar multiplier at that state cannot match the r^0 radial coefficient. This is a coefficient-level witness, not a stronger theorem for unrestricted clocks/correspondences or a T-6d trajectory on r=0: r=0 is an event guard. No integration across root contact, no comparison of full T-6d ODE to F6 time-one, no proof of descent from its own lifted producer. The sign test does not require both branches to be jointly admitted, whereas the parity statement does require a reflection-compatible comparison.

## 3. Evidence and reconciliation proposal

The shared exact script evidence/rer/r1/preparer/scripts/r1_exact_check.py (Python 3.13.5, SymPy 1.14.0, executed with python -I -B) verifies the recurrence, C12, Gram differential, cubic reflection, normalization substitution and coefficient sign witnesses. Output and SHA256SUMS in evidence/rer/r1/preparer/. No finite-radius or trajectory certification. No Claude or ER-2B package script used; reviewer synopsis already supplied, so not blind. Full #416 review read after first exact calculation: matches its two model comparison and C12 numerical checks, with exact coefficient confirmation and additional fixed-readout sign witness. Its native PI rerun §6 remains reviewer evidence, not our run.

**Proposed disposition: ACCEPT SCOPED**, subject to independent reviewer reconciliation and custodian confirmation. Agree with T-1/T-2/T-3 in #416; explicitly write the mode/readout/reflection/clock hypotheses, root branch/domain, r^0 coefficient nature. Keep historical TRIAD16 pin and current TRIAD17 retained statement; propose ER-2B v0.3 Part B C12 current noncanonical reference and historical v0.1/v0.2 pins. Missing ancillary historical addendum and producer execution remain disclosed and do not prevent this independently established limited comparison. No widening to arbitrary conjugacy or any physical carrier, no new age or memory conclusion, no K mismatch, no owner theorem adoption.

[OPEN] Historical lifted graph-force -> own T6d diagnostic descent, physical model correspondence and event/carrier selection. The PI must decide scientific acceptance of this record separately from CARRIER. Until then the excluded scope and existing machine catalog remain unchanged.
