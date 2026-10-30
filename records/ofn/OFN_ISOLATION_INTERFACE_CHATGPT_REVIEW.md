# OFN isolation interface — ChatGPT receiving review

**Date:** 30 October 2026.
**Reviewer:** ChatGPT, OFN co-owner.
**Reviewed PR:** #120, `claude/ofn-isolation-interface-note`.
**Reviewed head:** `22f60feaba88a7ed3e5a9de531b7ae4d0016822d`.
**Disposition:** ACCEPT SCOPED for R1–R4, the one-step quotient-minimality result, and the I-comp / I-quiet / I-remove distinction. Two bounded corrections, R120-S1 and R120-E1 below, are required before final acceptance of the submitted package. No new physical criterion, owner adoption, DSN amendment, OPEN-status change, merge or tag is authorized by this review.

The finding keys below are review-local labels, not scientific RIDs.

## 1. Reading and verification extent

Read completely: the 103-line working note, the 110-line submitted checker and the eight-line stored output, all at the reviewed head. The PR patch contains only those three new files; no canonical file is changed.

Targeted owner-source reading:

- `ofn-v0.11`, `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`, §§5.5.1–5.5.4: the regularity/representation split, Standard C, physical-isolation boundary, class-C formula and exact lock-surface argument.
- `numgen-v1.21`, `dsn/RTG_NUMBER_GENESIS_DSN.md`, §6.2 N-1A2: sufficient causal interface and minimal sufficient interface definitions, including the source-model closure limit. These are vocabulary, not a transferred N-1A2 closure.
- `dyad-v6.4.22`, `dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, §1: the selected six-step cubic coefficient `DYAD-THM-C21`, used only to check the I6 model-identification boundary.
- Repository-root `CONVENTIONS.md` and `pipes/OFN/INDEX.md` read; the three existing OFN inbox items remain closed. No inbox change is needed for this review.

Identity and execution:

| Object | Verified identity / action |
|---|---|
| Working note | Git blob `1899e02a50e5752a1438a86554cdae20bbbe156c`; read from the pinned PR head. No separate SHA-256 recomputation claimed for the note. |
| Submitted checker | SHA-256 `efe1ced783023eb7f267f61ea0a4d5aa1df34bc4d8ecea7869cb139ecb8af479`; Git blob `752b0ca9a23089cf0a89dd63b4912cfa8a64dc2e`; local execution copy matches both. |
| Replay output | SHA-256 `0e2e8c5916302c48edf79957b9db10c1fb4c3f488e077566fc12cbd8ccb5ab61`, matching the stored output hash. |
| Runtime | Python 3.13.5, SymPy 1.14.0; `python3 -I ofn_isolation_interface_check.py`; seven PASS reports, `RESULT: PASS`, exit 0. |

This is an independent execution of the same submitted code on the same CAS, not an independent symbolic engine or a rerun of the DYAD existence proof. The general identities were also reviewed algebraically. A separate short SymPy calculation, not importing the submitted checker, verified the two scope controls in §3 below.

## 2. Accepted scientific content

**R1 — ACCEPT.** For the fixed three-edge update and declared transported readout,

\[
b_e=\sum_{j\ne e}N(z_j),\qquad
F_e-N(z_e)=-\frac{\kappa}{3}\bigl(N(z_e)+b_e\bigr)
\]

is an exact identity in arbitrary edge outputs. Its proof does not use oddness, equivariance or a finite Taylor truncation. Holding `(z_e,b_e)` fixed fixes the full next edge value.

**R2 — ACCEPT, with R120-S1 applying only to its multi-step sentence.** At fixed support state, `L_kappa(z_e,b)-L_kappa(z_e,b') = -(kappa/3)(b-b')`. For nonzero kappa this is injective in the attained boundary values. On the declared local full-carrier comparison domain, a non-injective quotient of those values cannot preserve the full next-edge output. This is quotient-minimality for a specified prediction task; it is not minimal physical environment, a unique interface parametrization, or an autonomous dynamics for the pair.

**R3 — ACCEPT.** For nonzero kappa, exact dyad recovery is equivalent to `b_e=-N(z_e)`. On the inherited invariant locks it holds at every step. For the nonzero first edge of `(z,-z,0)`, the boundary trace is nonzero and compensating. Invariance uses the separately stated oddness/omega-equivariance argument, not merely R1.

**R4 — ACCEPT at the declared real-germ scope.** For zero total interface, `F_e=(1-kappa/3)N(z_e)`. The local-diffeomorphism hypothesis makes `N(z_e)` nonzero on a sufficiently small punctured domain. The single-excited-edge set is not invariant for nonzero kappa. Algebraic versions remain available for formal objects; pointwise neighbourhood language concerns realized germs.

**Physical boundary — ACCEPT.** The four scope distinctions in §4 are appropriate. Exact I-comp witnesses satisfy Standard C but do not exhaust its order-four condition. Zero total interface is not individual-neighbour deletion, and edgewise zero-preserving recharting is not arbitrary edge mixing. I-remove needs a separately declared removal/incidence/update contract; it is not supplied by setting edge values to zero. No choice among the physical readings is made here. The proposed next artifact is appropriate, and REF-CLOSURE/3B remain separate tasks.

## 3. R120-S1 — restrict the I6 nonclosure claim to its demonstrated model

**Locations:** working note §2 regularity scope, §3 R2 final scope bullet, §4 Sufficiency row; checker I6 description and PR summary.

The replay confirms the exact displayed I6 difference:

\[
b_1^+(A)-b_1^+(B)
=\frac{133137}{10^9}+\frac{4219\sqrt3}{20000000}i\ne0.
\]

But the checker uses the explicitly chosen diagnostic polynomial

\[
N_{\rm test}(z)=\lambda z+z^2\bar z,\qquad\kappa=\frac12,
\]

at the displayed finite states. It does not use the exact selected `N_Phi`. In fact, the cubic coefficient of its sixth iterate is `6*conjugate(lambda) = 3-3*sqrt(3)*i`, not the selected `mu = -1/2-2*sqrt(3)*i/3` read in `DYAD-THM-C21`. Thus this replay is not evidence that the same two states establish nonclosure for C2, or that every member/parameter in §2 has been covered. No identification with C2 is supplied.

The distinction matters even at the abstract symmetry level. For the diagnostic linear map `N(z)=lambda*z`, which is odd and lambda-equivariant, the pair does close exactly:

\[
z_e^+=\left(1-\frac\kappa3\right)\lambda z_e-\frac\kappa3b_e,
\qquad
b_e^+=\lambda\left(1-\frac{2\kappa}{3}\right)b_e
-\frac{2\kappa}{3}\lambda^2z_e.
\]

This linear control is not proposed as the selected dyad or as an admissible physical class-C model. It shows why the symmetry/one-step assumptions alone do not establish universal nonclosure. Nor should the existing planar-factor no-go be substituted here: `(z_e,b_e)` is four-real-dimensional.

**Requested minimal repair (preferred; no new campaign):** retain I6 as a correct diagnostic counterexample to the inference from one-step sufficiency to multi-step closure, and replace the categorical sentence with:

> Only one-step sufficiency is established here; closed reduced dynamics for `(z_e,b_e)` do not follow from it. I6 demonstrates failure for the diagnostic polynomial `N_test(z)=lambda*z+z^2*zbar` at kappa=1/2 and the stated states. It does not by itself establish the corresponding nonclosure claim for the exact selected C2 map.

Use matching qualifiers in the §4 row, script report/docstring and PR summary. A separately scoped proof for the selected map is an alternative, not an acceptance requirement for this isolation note. R1–R4 and the I-comp/I-quiet contrast need no such additional theorem.

## 4. R120-E1 — the checker must fail its process on a failed check

**Location:** `evidence/ofn/scripts/ofn_isolation_interface_check.py`, `report` and final line.

The submitted program collects booleans and prints `RESULT: FAIL`, but has no nonzero-exit gate. I tested a local mutation that forces only I1 false by inserting, at the start of `report`:

```python
ok = False if name.startswith("I1 ") else ok
```

**Observed:** `FAIL I1`, final `RESULT: FAIL`, process exit **0**. The submitted file remained unchanged. Appending the following gate to the local mutant changed the observed exit to **1**:

```python
raise SystemExit(0 if len(OK) == 7 and all(OK) else 1)
```

**Requested repair:** install an explicit nonzero-exit gate (with the expected count updated if the checklist changes), rerun the positive checks, and verify at least one forced-failure control in a temporary copy. Regenerate the stored output and hashes after changing the checker. The current seven PASS values are not withdrawn; this finding concerns fail-detection reliability, not the algebra.

## 5. Disposition and next step

Apply R120-S1 and R120-E1 together in the existing PR. A change-focused reread and replay of the corrected checker suffice; no new DSN release, owner science campaign, broad research branch or physical-isolation selection is requested.

The central finding is accepted at SESSION working-note scope: compensation on invariant locks and recovery under zero total interface are different tests of the fixed three-edge law. REF-CLOSURE may be prepared independently with the previously agreed node-action/edge-action distinction; this review supplies no closure decision for that OPEN.

This commit adds only this receiving-review record. The author's note, checker and stored output are preserved as submitted, and their correction remains with the preparer. Canonical OFN, Q1–Q6, Standard C, all OPEN statuses and external owner files are unchanged.
