# DYAD return-enclosure owner-adoption review v1

**Date:** 22 September 2026  
**Reviewer:** ChatGPT  
**Status:** Working review and proposed editorial amendments; not an owner DSN, not PI approval.  
**Inputs:** `DYAD_OWNER_ADOPTION_DRAFT_return_enclosure.md`, `dyad_referee_p2b_v2.py`, the reviewer's arithmetic backend, the reviewed P0–P1/P2-A/P2-B records, and Dyadic v6.4.9 / Methodology v1.3.  
**Disposition:** Recommend adoption of the reviewed mathematical package with the amendments below. No coefficient, enclosure constant, domain, existing RID, or downstream OPEN is changed by this review.

## 1. New reviewer artifact: execution and scope

The supplied `dyad_referee_p2b_v2.py` was run unmodified, with a byte-identical copy of `dyad_return_qchi_exact.py` as its backend. It prints **47 PASS checks**, no FAIL, and exits 0. The statement “48 checks” is not true of these supplied bytes. A separately marked fault-injected copy changes only the expected cubic coefficient; it records that failure and exits **1**. The original uses a failure accumulator and explicit final `sys.exit`, rather than literal Python `assert` statements. This is a valid acceptance gate and is not disabled by Python's `-O` flag.

The arithmetic is mixed:

- primitive/normalizer jets and many finite identities: exact `Fraction` arithmetic in Q(i sqrt(3));
- 11 coefficient-modulus acceptance checks: binary floating-point square roots with 1e-12 slack;
- 6 tail/domain acceptance checks: ordinary 60-decimal-digit mpmath values, without directed rounding;
- the remaining 30 checks: exact algebraic/rational, integer, or combinatorial checks.

Some profile calculations are exact rational expressions once their coefficient ceilings and tail constants are supplied. Their end-to-end validity still depends on those inputs. In particular, the original harness supplies the P^+ and J^+ coefficient ceilings without directly checking all of them against its reconstructed coefficients.

Thus the absent-reviewer-driver gap is closed. The original harness should be registered as **independent exact reconstruction plus numerical majorant/domain reproduction**, not as a fully outward-rounded exact certificate of every inequality. The already-reviewed exact-rational source certificates remain the principal enclosure evidence. This qualification does not refute or reopen the enclosure theorems.

### Supplement produced in this review

`check_owner_adoption.py` executes the supplied referee and adds **45 checks**, including exact rational square-root enclosures, exact P^+/J^+ ceiling checks, directed-rational Psi evaluations, finite-order homological residuals, and the quintic-iteration identity below. All pass. This supplement shares the referee's reconstruction/backend; it is **not a new independent reconstruction** and is not attributed to Claude.

The directed Psi bound expands through degree 40 and bounds the remaining terms by

\[
2\frac{x^{41}}{41!}\frac1{1-x/42},\qquad 0\le x<42,
\]

then rounds upwards to a rational grid after every scalar composition. Perfect-square rational moduli are retained exactly; other square roots have verified rational upper endpoints. No floating-point decision is used in the additional enclosure tests.

## 2. Amendment A — artifact wording and provenance

Replace the draft's header sentence with:

> `dyad_referee_p2b_v2.py`: 47 executed checks, all passing, exit 0; exact Q(i sqrt(3)) reconstruction of the finite jets and normalizer, with binary-float modulus and 60-dps non-directed tail/domain checks. Independent of producer/validator source code; uses the supplied reviewer backend. Its executable-reviewer role is distinct from the exact-rational enclosure producer/validator certificates. A negative-control copy confirms failure exit 1.

Record hashes of this exact harness, its actual imported backend, the supplied adoption draft, execution logs, and any adopted supplement. Do not retrospectively attribute a modified/strengthened harness to the reviewer or call a newly produced supplement independently reviewed.

The old handoff's 56-entry archive manifest authenticates the previous P2-B package only. The new harness and adoption draft require a new manifest. Preserve the original manifests unchanged.

## 3. Amendment B — complete finite-order and domain statements

The map and chart must be fixed explicitly:

\[
T(\rho,\eta)=(\rho-\sin\eta,\eta+e^\rho-1-\sin\eta),\qquad
\mathcal L(\rho,\eta)=\rho-\eta/2+i\sqrt3\eta/2,
\]
\[
f=\mathcal L T\mathcal L^{-1},\quad F_W=f^{\circ6},\quad
W=h(z,\bar z),\quad Q_{\rm prim}=|W|^2,\quad q=|z|^2.
\]

The phase is the local lifted phase; no wrapping seam is crossed. Here h is the fixed degree-six additive polynomial with resonant nonlinear correction coefficients zero.

For the degree-six one-step normal-form polynomial n, use

\[
\mathcal J_{\le6}(f\circ h-h\circ n)=0,
\qquad
\mathcal J_{\le6}(F_W\circ h-h\circ J)=0,
\]

not an unqualified all-orders polynomial identity `f o h = h o n`. The actual local maps

\[
\widehat f=h^{-1}fh,\qquad \widehat F=h^{-1}F_Wh
\]

are exact definitions on their proved domains; n and J are their stated finite jets.

For the primitive radial record, define

\[
P_5=\frac Q{24}(5\eta^3-43\eta^2\rho+4\eta\rho^2-5\rho^3),
\qquad
R^{\rm prim}_{\ge6,\rm rad}=Q(T^6x)-Q+Q^2-P_5.
\]

Then retain exactly

\[
|R^{\rm prim}_{\ge6,\rm rad}|\le108Q^3\quad(0\le Q\le1/400),
\]
\[
0<Q-\tfrac32Q^2\le Q(T^6x)\le Q-\tfrac12Q^2\quad(0<Q\le1/400).
\]

At Q=0 the map is fixed and strict positivity does not apply. The same punctured-domain qualification belongs to the normalized contraction statement. The tube base is `0<Q<=1/625` with six images j=0,...,5.

For NF-INV, write the compared observable as `Q_prim(L^{-1}h(z))`, and state the `|z|<=1/10` comparison domain; the inverse domain is `|W|<=9/100`.

For NF-REM, keep the full formulas rather than the constant tuple alone:

\[
|\widehat F(z)-J(z)|\le C_7|z|^7,\qquad
\|D\widehat F(z)-DJ(z)\|_2\le C_D|z|^6,
\]

where D is the first real derivative. Profiles remain `(1/20,100,1000)` and `(1/40,30,250)` in this same chart. No new radius or higher-derivative claim is made.

Methodology v1.3 distinguishes exact coefficient identities from complete analytic theorems. When writing the full entries, describe the domain proofs as analytic-majorant proofs with exact-rational certificates; do not imply that the new mixed-arithmetic referee is an interval certificate. `[THM]` is a natural proposed tag for the full contraction/inverse/remainder theorems, while `[ALG]` applies to the finite coefficient identities. Proposed RID spellings need not change with that tag choice; existing RIDs are not renamed or automatically retagged.

## 4. Amendment C — reconcile current statements at the point of use

Appending SG-19 and the new table is insufficient if contradictory live formulas remain. At installation review the following affected locations in Dyadic v6.4.9:

| Current location | Required scoped replacement / disposition |
|---|---|
| §6.7 primitive complex return `...+O(|W|^5)` | Raw linear W has a nonzero quartic jet: use `...+O(|W|^4)` and point to the separate normalized statement. |
| §1 and §6.5 primitive positive-real-ray burst | Include the nonzero half-power term; see formula below. An averaged/symmetrized observable, if intended instead, needs its own definition. |
| §1, §6.2, §6.9 and §8 archival `h3=0` / normalization labels | Preserve the historical calculation under its actual return-log/archive meaning; do not identify it with the nonzero h3 of the adopted one-step coordinate map. |
| §6.9 projected/raw coefficient descriptions | Preserve raw values, but do not identify the three-channel log-projected model with the actual normalized return. |
| §6.5 `47/54` discussion and downstream phase/projection quantities | Preserve the restricted raw coefficient / fixed-radius angle-average agreement. It does not certify a long-orbit backbone, a final-chart phase coefficient, or inherited a1/a2 calculations. Queue R11 rather than silently transferring them. |

The positive real primitive ray `(rho,eta)=(t,0)`, t>0, gives

\[
Q(T^6(t,0))
=t^2-t^4-\frac5{24}t^5+\frac{37}{40}t^6+O(t^7),
\]

or

\[
Q_6=Q_0-Q_0^2-\frac5{24}Q_0^{5/2}
+\frac{37}{40}Q_0^3+O(Q_0^{7/2}).
\]

The supplement reproduces these coefficients from the referee's reconstructed full primitive jet. These are already identified audit corrections, not new calibration or physical claims.

## 5. The (3,2) bridge note — explicit algebra

The proposed warning is correct. The existing cubic bridge RID need not be renamed or broadened.

For the stated p=6 normal form set

\[
A=\bar\lambda n_{21},\quad B=\bar\lambda n_{32},\quad C=\bar\lambda n_{05}.
\]

The nonlinear resonant map g=bar(lambda)n commutes with z->lambda z at this jet order. Since lambda^6=1, n^{circ6}=g^{circ6} at the relevant orders. With

\[
g(z)=z+Az^2\bar z+Bz^3\bar z^2+C\bar z^5,
\]

composition gives

\[
[g^{\circ m}]_{32}=mB+\binom m2(2A^2+A\bar A).
\]

The cross term follows from `D(A z^2 zb)[A z^2 zb]= (2A^2+A conj(A)) z^3 zb^2`. Degree-five input terms do not interact with nonlinear terms again until degree seven. Thus

\[
\boxed{a_{32}=6\bar\lambda n_{32}
+15\left(2(\bar\lambda n_{21})^2+|n_{21}|^2\right).}
\]

Numerically unspecified quantities are not needed:

\[
A=-\frac1{12}-\frac{i\sqrt3}{9},\quad
B=\frac1{324}+\frac{17i\sqrt3}{1944},
\]
\[
15(2A^2+|A|^2)=-\frac{35}{144}+\frac{5i\sqrt3}{9},
\]
\[
6B+15(2A^2+|A|^2)=-\frac{97}{432}+\frac{197i\sqrt3}{324}.
\]

Meanwhile `mu=6 bar(lambda) n21` and `a05=6 bar(lambda) n05` remain exact. This is a p=6 finite-jet iteration identity in the stated convention, not a universal quintic bridge for arbitrary p. The supplement checks the general m coefficient against direct composition for m=1,...,6.

## 6. Draft identifiers and evidence placement

The five proposed RIDs do not collide with any RID in the supplied Dyadic v6.4.9. SG-19 is unused there. Retain existing IDs; the proposed IDs remain proposals until the owner's/PI's adoption record is made. No need to change an identifier simply because its mnemonic contains ALG or OBS; give the obstruction row an unambiguous title.

The P2-B v2 archive really does carry the P2-A v2 / P2-B v1 baseline files. Preserve the wrapper paths in its hash manifest; do not describe an absent nested ZIP as present. The older 56-member manifest was checked again in this review and all hashes match. Fresh input hashes and execution records are included in this package.

Recommended pending decision: install the mathematical package plus these precise scope/provenance corrections in the next owner revision, then perform RECOG R11 final-chart reconciliation. R10 acceptance is chart-dependent; R9's two-history comparison and R8's manifold entry remain separate. No geometry, source amplitude, generator selection, or quantitative GAP-LOCK closure is obtained here.

## 7. Limits of this review

This is a focused new-artifact and adoption-draft audit, not a new rerun of the full producer/validator archive or a new independent proof campaign. The supplied referee was executed unmodified, its failure gate was tested by a marked copy, and the shared-backend exact supplement was executed. The original owner DSN, supplied draft, reviewer files and earlier archives are unchanged. The unrelated prior ontology-finalization request remains ignored.
