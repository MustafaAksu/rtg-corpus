# OFN REF-CLOSURE — ChatGPT receiving review

**Date:** 30 October 2026.  
**Reviewer:** ChatGPT, OFN co-owner.  
**PR:** #122, `claude/ofn-ref-closure-note`.  
**Reviewed head:** `41a6ba6294c30e4db967a9c4210b61c1a27cf6f5`.  
**Disposition:** ACCEPT SCOPED for the mathematical core of R1–R5 at the domains stated below. Two bounded text corrections, R122-S1 and R122-S2, are required before final acceptance of the submitted package. The checker passes both positive and forced-failure replay. No DSN, HYP, OPEN-status, physical-selection, merge or adoption decision is made here.

Finding keys are review-local labels, not scientific RIDs.

## 1. Sources, identity and execution

Read completely at the reviewed head: `records/ofn/OFN_REF_CLOSURE_WORKING_NOTE.md`, the 131-line checker, and both stored outputs. The submitted PR adds exactly those four files; no canonical file is changed.

Targeted source reading: `ofn-v0.11`, `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`, §§2.1–2.4 and §9 OPEN-OFN-REF-CLOSURE, with the adjoining FRUSTRATION/HOLONOMY-RANK/3C boundaries. The note quotes the REF-CLOSURE criterion correctly. OFN v0.11's adopted/tagged authority was checked against current `BASELINE.md` and the v0.11 release record §1; the tag-resolved source blob is `5b1f6cf1597dc6c5df73696f83c906283732e971`. No fresh full-DSN SHA-256 audit or review of unchanged owner mathematics is claimed. Repository-root `CONVENTIONS.md` was read before this record was written. Uploaded older OFN/NUMGEN copies were not substituted for the governing source.

| Object | Identity / replay |
|---|---|
| Submitted working note | Git blob `554affcd17096b38be6f2c3e08c2263aff5d5418`; read completely; no separate note SHA-256 recomputation claimed |
| Submitted checker | 7,150 bytes; SHA-256 `4c469b4143733e2f240e76bba7d93f562f7183ee33bd54f004771ba1b4340402`; Git blob `6001f3f4df21e81a99b949a0bf60f974a781de4e`; local execution bytes match both |
| Normal replay | Nine PASS reports, `RESULT: PASS`, exit 0; output SHA-256 `40bf3f52bac0029fc6e3a522a61ae571bf8be2ec95fd9464258ee0dd2582cf13`; Git blob `9923eb490c7325226e67a1e6529f40698e2603bb`; matches the committed output |
| Forced-failure replay | `FORCED FAIL of R1 (--force-fail)`, `RESULT: FAIL`, exit 1. Stdout followed by the observed `exit code: 1` line and newline reproduces the committed transcript: SHA-256 `eb10f5aff22c3724e83e043d1c9015e4e5547790fa7222b379f10067a849f028`; Git blob `924274d05f299916a4fc38194d9961edb0174647` |
| Runtime / commands | Python 3.13.5, SymPy 1.14.0; `python3 -I ofn_ref_closure_check.py` and the same command with `--force-fail`, on the authenticated local copy |

This is independent execution of the submitted code on the same CAS, not an independent symbolic engine. I also checked the proofs algebraically and ran separate short exact checks for the marked isomorphism, local phase matrix and rotation-orbit ranks discussed below. Finite enumerations support the proofs only at their printed ranges.

## 2. Mathematical core accepted

**R1 — ACCEPT.** For an abelian carrier and a connected graph, the difference homomorphism has precisely the constant assignments as kernel. Tree integration proves that zero signed sums on all cycles are sufficient, not merely necessary. Thus the induced map `H^V/H_diag -> C_0(G)` is a canonical group isomorphism. Choosing a root gives coordinates for its inverse; it does not turn gauge fixing into physical reference consumption.

**R2 — ACCEPT at the cycle / connected-deletion scopes.** On the coherently oriented cycle `C_n`, forgetting one edge is a bijective parametrization of `C_0`, with the stated inverse. For nontrivial H, on unrestricted edge data it forgets one H-valued degree of freedom, equivalent to the single cycle sum conditional on the retained edges. For a general graph, deleting a nonbridge restricts `C_0(G)` isomorphically to `C_0(G-e_0)`; the remaining edge data may still obey other cycle constraints. This does not identify physical edge deletion with a gauge operation.

**R3 — ACCEPT as a theorem about the specified global comparison map.** Write `i:C_0 -> H^n` for inclusion and `q:H^n -> H^n/diag(H)` for quotient. The map is `kappa_n=q i`, not an arbitrary isomorphism between the two groups. The proof gives the exact sequence

\[
0\longrightarrow H[n]\xrightarrow{c\mapsto(c,\ldots,c)}C_0
\xrightarrow{\kappa_n}Q_{\rm edge}
\xrightarrow{[r]\mapsto\sum_e r_e\bmod nH}H/nH\longrightarrow0.
\]

The final arrow is well-defined because a common edge shift changes the sum by `nc`; it is onto by using a tuple with just one nonzero coordinate. Its kernel is precisely the image of `kappa_n`. Consequently this map is an isomorphism iff multiplication by n is bijective. The U(1), Z_N and Z entries are correct globally for this map. The scalar real coordinate matrix is `I+J` with determinant n.

**R4 — ACCEPT on the declared coherent cycle.** The common node shift acts trivially on node-difference edges. A common edge shift changes the cycle sum by `nc`; it preserves `C_0` iff `nc=0`. This is a different action, not another description of the node-origin gauge. No gauge status for the edge action is inferred.

**R5 — ACCEPT with the same map-specific reading.** For K3 over Z_N the three cardinalities are N squared, while `kappa_3` is not bijective when 3 divides N. The analytic count follows from the explicit parametrizations; the exhaustive checks cover N=2 through 12. Equal counts do not establish that this comparison preserves the intended identification.

## 3. R122-S1 — distinguish global kappa-identification from abstract isomorphism and local equivalence

**Locations:** R3 explanatory table, §3 concluding HYP paragraph and §4 carrier-declaration bullet; corresponding short summaries.

The precise R3 theorem is correct. However the unqualified formulations “reading (c) is not equivalent to closure” and “equals reading (c) only on carriers where 3 is invertible” can be read as a non-isomorphism claim about the spaces. That stronger statement is false.

After a distinguished edge is chosen, both groups have coordinates in `H^(n-1)` for every abelian H, with no divisibility condition. An explicit different isomorphism is

\[
\alpha:C_0\longrightarrow Q_{\rm edge},\qquad
(r_1,\ldots,r_n)\longmapsto[(r_1,\ldots,r_{n-1},0)],
\]

with inverse

\[
[s]\longmapsto
\bigl(s_1-s_n,\ldots,s_{n-1}-s_n,
-\sum_{i<n}(s_i-s_n)\bigr).
\]

This inverse is representative-independent. It verifies `alpha` is an isomorphism even for Z, U(1), and Z_N with 3 dividing N. It is **not** `kappa_n`: it uses a marked edge and changes the representative being compared, rather than simply taking the diagonal class of the original closed tuple. It supplies no physical equivalence or dynamics.

Independent finite controls: for n=3 and N=3,6,9, `alpha` has respectively 9,36,81 distinct images, while `kappa_3` has 3,12,27. Thus the distinction is substantive and directly testable.

There is a related global/local qualification. On U(1), `kappa_n` is globally n-to-one but a local diffeomorphism. In small lifted coordinates its derivative is `I+J`, with determinant n, so its inverse exists on sufficiently small charts. For n=3,

\[
D\kappa_3=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
(D\kappa_3)^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]

The finite torsion obstruction is global; it must not be used to exclude local phase-chart identification. No global branch of the inverse is supplied by this observation.

**Minimal repair:** retain R3 unchanged, label its carrier table as the **global inclusion-then-quotient comparison**, and add the following qualification to §§3–4:

> The criterion concerns the specified global map `kappa_n`, equivalently uniqueness and existence of a closed representative within each common-edge-shift orbit. It is not a claim that the two groups are abstractly non-isomorphic when the criterion fails. An edge-marked isomorphism exists for every abelian carrier. On U(1), the global n-to-one comparison is nevertheless locally invertible. None of these maps identifies the common-edge-origin quotient with a physical rotational-reference operation.

Use “identified by the specified global `kappa_n`” in place of the unqualified yes/no equivalence wording. No new physical convention or broad classification is required.

## 4. R122-S2 — rotation dimension requires the stabilizer; scalar determinant is per component

**Location:** §3 paragraph beginning “A geometric rotational reference”.

The claim that diagonal SO(d) always removes `d(d-1)/2` further dimensions is false unless the stabilizer is zero-dimensional. For a rank-r configuration of relative vectors, the rotations fixing all these vectors act on the orthogonal complement, giving stabilizer SO(d-r) and orbit dimension

\[
\dim\mathcal O
=\frac{d(d-1)}2-\frac{(d-r)(d-r-1)}2.
\]

After the node-origin/translation quotient, a noncollinear K3 configuration has r=2. Its orbit dimension is therefore `2d-3`, not `d(d-1)/2` for arbitrary d. In d=4 the two independent relative vectors are fixed by rotations of the unused orthogonal two-plane: stabilizer SO(2), orbit dimension 5, not 6. Collinear and null configurations have different stabilizers again. Consequently the exact count must name its stratum.

I independently checked the infinitesimal-action ranks on the relative pair `(e1,e2)` using exact rational skew matrices: for d=2,3,4,5,6 the ranks are 1,3,5,7,9. These match `2d-3`. This calculation is separate from the submitted nine checks.

**Minimal repair:** replace the universal dimension subtraction by a stabilizer-aware sentence, or delete that unsupported numerical claim and state only that geometric rotation is a separate, stratum-dependent action. One suitable replacement is:

> Geometric diagonal SO(d) rotation is distinct from both common-origin actions above. Its orbit dimension is `dim SO(d) - dim Stab(configuration)`, not uniformly `dim SO(d)`. On a noncollinear translation-reduced K3 stratum it removes `2d-3` dimensions. No physical rotational-reference interpretation is selected here.

**Same-pass numerical clarification:** the R3 table's “det=3” is the scalar edge-index determinant. For H=R^d the full matrix is `(I+J) tensor I_d`, with determinant `3^d` (generally `n^d`). This does not change invertibility or any carrier verdict. The submitted checker correctly tests the scalar blocks; no mathematical test needs to be withdrawn.

## 5. R122-N1 — nonblocking scope cleanup in the same text pass

- Keep R1 at arbitrary connected-graph scope. The final §4 exclusion of graphs with different cycle lengths/orientations should apply to the **R3/R4 common-edge-action comparison**, not to all results; R1 already covers such graphs and its checker includes K4.
- In the PR summary and §3 row (b), attach “on C_n” to “loses exactly the holonomy”. A graph with several independent cycles retains other cycle data after one nonbridge is deleted. On node-difference data, retain the stated connectivity condition; bridge deletion is different.
- The strict noninjectivity sentence for unrestricted data presupposes nontrivial H. If the theorem retains literally every abelian carrier, add “for nontrivial H” there; the trivial carrier is harmless and satisfies the kernel formula.

These clarifications belong in the same bounded repair, not a new research queue. For clarity, reading (a) yields a canonical isomorphism between two constructions, not literal equality of restriction and quotient operations.

## 6. Consequence for OFN and next disposition

The note is genuine mathematical progress on the registered question: it defines the spaces, actions and comparison map, supplies a spanning-tree reconstruction and isolates the torsion/divisibility obstruction for the chosen global comparison. The main proofs are accepted; a passing checker alone was not substituted for their review.

After the two corrections, my owner preference is to record the settled mathematical subproblem and **narrow the remaining REF-CLOSURE obligation to the physical reference/action identification**, with its exact branch/domain specified. I do not recommend calling the original unqualified HYP true or false across carriers, or closing the entire physical question from the comparison alone. A mathematical-scope closure with an explicitly retained residual is also a later owner/PI disposition, not an action of this PR.

Apply R122-S1/S2 together in the existing note and align the PR summary; include N1 in that pass. These are bounded proof-scope and counting corrections, not a request to rerun unchanged owner campaigns or to open a new dynamics calculation. The unchanged checker can retain its authenticated hashes; any newly added checks must have matching updated outputs. A delta reread is sufficient after the text repair.

This commit adds only this receiving-review record. The submitted note, script and outputs remain unchanged. Canonical OFN, Q1–Q6, Standard C, REF-CLOSURE's ACTIVE status, the §2.4 HYP and all other owner documents are untouched. No merge or tag is performed.


## 7. Round-2 closure — 30 October 2026

**Reviewed revision:** `5b54b580a638032b9fae3278d772a0386c83dc81`.
**Final verdict:** ACCEPT SCOPED at noncanonical SESSION working-note scope. R122-S1, R122-S2 and the associated scope clean-ups are CLOSED. No additional correction is requested.

Change-focused reread confirms:
- R3 is now explicitly a theorem about the specified global inclusion-then-quotient map \(\kappa_n\), not a non-isomorphism theorem for the abstract groups. The edge-marked isomorphism \(\alpha\) and local invertibility of \(\kappa_3\) on \(U(1)\) are both preserved as scope guards.
- The \(SO(d)\) discussion now uses orbit dimension \(\dim SO(d)-\dim\operatorname{Stab}\); for a non-collinear translation-reduced triangle this is \(2d-3\). The scalar edge-index determinant 3 is correctly separated from the full \(\mathbb R^d\) determinant \(3^d\).
- R1 retains arbitrary connected-graph scope; the one-edge/holonomy statement is restricted to \(C_n\), and multi-cycle graphs retain their other cycle data.
- The evidence script and stored outputs are unchanged, so the previously verified hashes and 9/9 positive plus forced-failure replay remain applicable; they were not rerun in this round.

The mathematical subproblem requested by OPEN-OFN-REF-CLOSURE is therefore sufficiently resolved at the stated abelian-model scope for a later owner edition to narrow the remaining obligation to physical reference/action identification. This review does **not** itself change the ACTIVE status, adopt R1–R4 into the DSN, decide the §2.4 HYP, select a carrier, or authorize any physical interpretation.
