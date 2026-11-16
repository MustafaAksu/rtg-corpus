# DYAD OPEN 20 — independent C++ inclusion logic

**Date:** 16 November 2026. **Author/implementer:** ChatGPT, DYAD co-owner.
**Requested auditor:** Claude, DYAD owner and mathematical auditor.
**Status:** SESSION / PROPOSED DESIGN + DEVELOPMENT KERNEL. No owner acceptance,
scientific adoption, production authorization, jump certificate, or new RID.

The PI requested that ChatGPT construct new C++ logic and Claude audit it.
This package supplies the mathematical contract and a compiled first kernel,
not an additional request for permission to begin. A complete pilot execution,
stage 3c-b production/replay, and multi-height experiments are not performed.

## 1. Source cut and reading extent

- Repository base: `MustafaAksu/rtg-corpus`, `2d898fdafedee7f5b3d4628fe0c08ef2871a8b0c`.
- Governing owner: `dyad-v6.4.24`, the newest DYAD tag returned by the repository.
  Release/adoption record inspected at that tag: ADOPTED by PI on 11 November
  2026; source-reported DSN SHA-256
  `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16`.
  The full DSN bytes were not rehashed in this session.
- `CONVENTIONS.md`: full reading, especially evidence and branch rules; it names
  Methodology v1.4 as governing. No methodology or canonical science is edited.
- `DYAD_OPEN20_AN_STAGE3C_A_PROOF_RECORD.md`, blob
  `a8f5ab9cc29c5b1c2a35145aa994e69c487491ef`: targeted §§1–3 and §§9–11, plus the
  start of §12. §§4–8 were reviewed in preceding sessions, not fully reread here.
- `DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md`: targeted D1–D9, especially branch,
  lifted coordinates, normalization, inverse chart, and observable convention.
- MPFR public manual, version 4.2.2: directed rounding and interval endpoint
  semantics. Official reference: `https://www.mpfr.org/mpfr-current/mpfr.html`.
  The public C declarations were checked against `src/mpfr.h` in the upstream
  `P-p-H-d/mpfr` source mirror. FLINT/Arb documentation was consulted when choosing
  the backend; no FLINT code or API is used by this implementation.

**Independence disclosure.** ChatGPT has previously read parts of the Python
implementation and its results. This is not a blind clean-room study. The new
logic and source are derived below from the mathematical definitions rather
than translated from Python. No owner script, coefficient cache, remainder
constant, or enclosure output is read by the C++ kernel. MPFR replaces Arb for
interval arithmetic; GMP and the mathematical model remain shared dependencies.
Claude's review is requested, not received.

## 2. Scope and implemented boundary

**K0 (implemented):** directed real intervals; rectangular complex intervals;
full elementary T^6; holomorphic first-order automatic differentiation; generic
forward/inverse relation contraction; finite-chain sweeps in either orientation;
uniform local inverse-box inclusion; strict separation of enclosing discs.

**K1 (not yet implemented):** independent construction of all coefficients of
phi_40, exact binding of the pilot constants and decimal tau, tube/guard upper
bounds, and whole-fibre bootstrap of both actual selected orbits.

**K2 (not run):** the complete pilot legs from xi_star, then comparison against
the Python enclosure at the same definitions. No current output is an enclosure
of either selected sectorial value at xi_star. K0 tests use phi_3 and short local
orbits, not the invariant sectorial curves.

Region-I/II coverage, curve existence/identification, and L1/L3 are not being
independently reproved by this package. The eventual result will name these
imports explicitly. An arithmetic PASS does not discharge any of them.

## 3. Defining map — no lifted-series remainder engine

[OWNER: proof record §1; SESSION implementation]

T(rho,eta) = (rho-sin eta, eta+exp rho-1-sin eta), F=T^6.
Let omega=-1/2+i sqrt(3)/2 and omegabar=-1/2-i sqrt(3)/2. In the complexification
z and w are independent variables, not numerical conjugates:

eta=(z-w)/(omega-omegabar), rho=(omega*w-omegabar*z)/(omega-omegabar).

For a fixed polynomial P(x), define

H(x,d) = (Z, (W-P(Z))/Z^2),
(Z,W)=F(x,P(x)+x^2 d).

The evaluator executes the six elementary T steps directly. Differentiating this
expression by the product/chain rules gives DH on a rectangular box. No d-jet
truncation, M3/MZ constant, degree-360 series, Cauchy-circle cover, or empirical
safety multiplier enters this evaluator. A box whose x or resulting denominator
cannot be separated from zero is rejected, not rescued by a nominal value.

This strategy exchanges Taylor-tail bookkeeping for potentially wider interval
bounds. Raising precision reduces rounding error, not interval dependency or
wrapping. Practical usefulness at the full pilot fibre is an open engineering
question, to be decided by bounds rather than a speed claim.

## 4. New inclusion-preserving leg contractor

[SESSION / conditional mathematical argument]
Let B=B_x x B_d be a convex complex rectangular box. Assume H is holomorphic on
a neighbourhood of B. Let c be an exact dyadic centre in B; h encloses H(c), and
J encloses DH(u) for every u in B. For each fixed u in B,

H(u)=H(c)+A(u-c), A=integral_0^1 DH(c+t(u-c)) dt, A_ik in J_ik.

Thus a relation H(u)=v, u in B, v in V permits the forward update

V_i <- V_i intersect [h_i + sum_k J_ik (B_k-c_k)].

Choose an exactly represented, nonzero scalar pivot a_i, e.g. the midpoint of
an enclosure of partial_i H_i(c). The same relation gives

B_i <- B_i intersect {c_i + a_i^(-1)[V_i-h_i
              - sum_(k!=i) J_ik(B_k-c_k) -(J_ii-a_i)(B_i-c_i)]}.

**Proof of inclusion.** Substitute the exact relation into the bracket. It
reduces to a_i(u_i-c_i). Every remaining quantity is replaced by a containing
interval, so the exact u_i belongs to the candidate set and to the intersection.
The intervals for h and J may be correlated; discarding that correlation only
widens them. A later narrowing is valid while the old J still encloses its domain.

For the F leg the edges are H(p_k)=p_(k+1). For the G leg use
H(p_(k+1))=p_k. The same forward/backward sweep handles both orientations; no
separate translated G-update formula is required. Any finite order or number of
such updates preserves all initially enclosed solutions. An empty intersection
signals inconsistent hypotheses or failure; it is never interpreted as a
certificate that the selected sectorial curve does not exist.

**Essential limitation:** this theorem contracts a set already known to contain
the selected orbit. It does not establish existence, global initial coverage,
or selected-branch identity. A Newton centre is not an initial enclosure.

## 5. Uniform inverse-box witness

[SESSION / conditional mathematical argument]
For a proposed source box B, exact centre c and a target box Y, select an exactly
represented nonsingular complex 2x2 matrix C. The code checks nonsingularity of C
separately after midpoint selection. Enclose

K(B,Y)=c+C(Y-H(c))+(I-CJ(B))(B-c).

If K(B,Y) is strictly inside B, and

q=max_i sum_j (sup|Re E_ij|+sup|Im E_ij|) r_j/r_i < 1,
E=I-CJ(B), r_i>0,

then for each y in Y the map u -> u+C(y-H(u)) is a contraction of the compact
rectangle B into itself, using the weighted real infinity norm on its four real
coordinates. Banach gives one fixed point in B; C is nonsingular, so it solves
H(u)=y. The derivative bound proves uniqueness in B.

The positive weights r_i need not equal rounded stored halfwidths: they define
the norm. K uses the actual stored B and J is evaluated on that same B.

**What this does not prove:** it does not exclude another preimage outside B and
does not identify this inverse with the sectorial branch used by the owner. K1
must connect the inverse boxes to the germ at 0 or invoke the explicitly scoped
owner uniqueness/continuation contract, with source-region checks.

## 6. Polynomial and tube initialization contract

[SESSION proposal; not implemented except a2 and the a3 test polynomial]
Independently construct P=phi_40 from the formal graph equation
F_w(x,P(x))-P(F_z(x,P(x)))=0, not from the owner's coefficient output.
The leading constants read from proof record §2 give

A=mubar-2mu, B=d31-2c40, C0=cc,
a2=(-B-sqrt(B^2-4A C0))/(2A), Im(a2)>0,
ell=c40+mu*a2.

For n>=3 the proposed triangular solve uses the coefficient of x^(n+3):

Lambda_n*a_n + R_n=0,
Lambda_n=2(mubar-mu)*a2+d31-n*ell.

The displayed slope follows by varying a_n*x^n in the leading weighted terms:
the contributions are (2*mubar*a2+d31)*a_n from F_w, n*ell*a_n from P(F_z),
and 2*mu*a2*a_n from the variation of F_z inside P. Before use, the auditor
should check that higher weighted terms cannot contribute at this order and
that Lambda_n excludes zero for every required n. Residual intervals containing
zero are consistency checks, not a proof that structural coefficients vanish.

Bootstrap the F leg from the *entire* initial tube fibre, not a neighbourhood of
the expected answer. Bootstrap the G leg with inverse witnesses for the *entire*
target sets and the selected-branch contract. The declared decimal tau and tube
constants must be the ones defining the owner's sets, including the nonzero e3
correction; silently replacing tau by exact formal coefficients changes the task.

At every node, a tube restriction needs a justified domain-membership statement.
If direct interval evaluation is too wide, subdivide with a coverage ledger.
Discarding an unsolved subbox is forbidden. Failure of coverage is INCONCLUSIVE.

## 7. Two-disc test and comparison protocol

[SESSION / conditional mathematical argument]
For a final rectangle D, let m be its exact midpoint and r an upward bound of
sup_(z in D)|z-m|. Then D is contained in the disc (m,r). The strict test is

lower(|m_1-m_0|^2) > upper((r_0+r_1)^2).

Equality, overlap, nonfinite endpoints, or a negative radius cannot pass. This
only separates the enclosed sets. To conclude d_0(xi_star)!=d_1(xi_star), K1 must
first show that those exact selected values belong to the two sets.

Freeze the C++ code and its mathematical inputs before comparing resulting
boxes with the Python run. Require the same branch, x_star, d unit, polynomial,
clock/domain convention and conditional imports. Compare mathematical enclosures
and their intersection/containment, not printed decimal equality. A discrepancy
is investigated; Python output is not an oracle used to retune C++ bounds.

A positive independent leg result still does not decide B-an/B-6. Multi-height
raw jump magnitudes do not by themselves identify a first Fourier coefficient:
the observable, normalizer, prefactor, overlap and finite-height error need their
own design and the INF-016 implication audit. That optional work is deferred.

## 8. Development evidence and requested audit

Local implementation: C++17, MPFR 4.2.2 runtime, GCC; no Arb and no owner Python
code. The container lacked the full development header. A checked local public
ABI declaration subset was used only to compile these bounded tests; it is in
`evidence/local_build/`, outside the normal CMake include path. **Build with the
real distribution header remains the auditor's first acceptance check.**

Executed here:
- 20/20 kernel tests at each of 128, 256, 512 bits (60/60).
- 8 point/derivative comparisons at each precision against a fresh 220-decimal
  mpmath evaluation of T^6 (24/24); numerical evidence, not interval proof.
- AddressSanitizer + UndefinedBehaviorSanitizer, 256-bit test suite: exit 0;
  error stream empty.
- Unsupported `--production`: exit 2. No production pathway exists.

The test polynomial is phi_3 with the selected a2 and the stated a3 formula.
Short three-edge tests verify preservation of a known local orbit; they do not
stand in for whole-fibre coverage of the actual 334-step pilot legs.

Claude's requested review is a **source/math review**, not an adoption decision:
1. Endpoint rounding, trig bounds, complex division, precision lifetime and
   standard-header build; sanitizers and negative cases.
2. Mean-value contractor and inverse-box proof, including same-domain use,
   fixed polynomial parameters, pivot/matrix nonsingularity and strict tests.
3. K1 input/coverage/branch obligations and the independence boundary. Decide
   whether this direct-derivative architecture is worth completing at xi_star.
4. Preserve any negative feasibility finding; do not require performance or
   separation before the enclosure logic itself is accepted.

No new long computation, stage-3c-b authorization, DSN amendment, tag, merge,
claim of a jump, or physical interpretation follows from this package.
