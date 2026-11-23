# T-6 producer recovery — receiving review and r4 disposition

**Date:** 1 October 2026  
**Status:** Noncanonical source review and proposed r4 text. No owner DSN, frozen GCL, RID, source code, historical record, physical birth rule or ODE campaign is changed.  
**Requested outcome:** Evidence-bound normalization correction and expanded CN-05, for the existing Triadic co-owner/editor to integrate once into r4.

## 1. Disposition

The recovered source resolves the orientation-normalization question at the actual extraction-model level. It is no longer merely a comparison of two substitutions into unidentified coefficient strings.

The root closure in T-6d is consistent with the **input variable Omega** in T-6c2. T-6e instead extracts the raw component determinant increment and expresses it as a function of that same Omega. Subsequent direct-orientation and dimensionless producers insert this determinant increment as though it were the increment of Omega. The required conversion is **Delta Omega = -sqrt(3) Delta omega_det**. This is a sign and scale error in the consumer chain, not an error in the T-6e measured determinant.

The scientific subtask identifying this mismatch can be marked CLOSED on adoption of the source-pinned correction. That does not revalidate the prior numerical sector/basin interpretations or complete a physical five-variable state contract. Triadic v1.5 remains adopted and v1.6 r3 remains a draft awaiting the wider r4 integration.

## 2. Recovered bytes and provenance

The archive contains 25 Python files and `SHA256_MANIFEST.csv`. Every Python file matches the CSV hash. Their exact byte sizes, CSV LastWriteTime strings, ZIP timestamps and verified hashes are in `data/verified_producer_manifest.json` and CSV.

For the principal pair:

| File | Recorded Windows LastWriteTime | SHA-256 |
|---|---|---|
| `tetrahedral_six_step_cross_phase_t6c2_patched.py` | 2026-05-28T19:15:45 | `afb4525ccc2f459964fc3e9acade004f2aa61c03be2366f125cef63fc466d80e` |
| `tetrahedral_six_step_omega_t6e.py` | 2026-05-28T21:59:20 | `98e4b0b033c2592b6a084006ab51283092238f291f5b455f1aa2e23b7af82d59` |
| `triad_generalized_k4_ode_t6d.py` | 2026-05-28T21:49:25 | `3674b7a2ea6bc2b1918a15e3c60dc5d38cf6fecfc8029716f2f5677944c8934c` |

The CSV times have no timezone/offset. ZIP timestamps have two-second resolution, explaining the observed one-second differences. These are preserved filesystem provenance fields, not authenticated historical execution times. Matching current bytes does not prove no earlier edits, that these were every DSN run's exact bytes, or a git revision. The outputs' `script_git_hash` fields contain descriptive labels rather than commit hashes.

The received output hashes match the user's report in full:

- `t6c2_out.json`: `82451781d45e2af2bff311656b2046b02fad767ed1c2e2f5901766bd507aa414`;
- `t6e_out.json`: `288cd77da617a12022350f7902c01a1f4d02565298b84e101becb108f6e241db`.

Both files are **UTF-16LE with a BOM, and contain progress output followed by JSON**. They are not directly JSON-parseable before isolating that JSON object. Raw bytes are preserved; decoded and parsed files are separately named derivatives with no substitution of their hashes for the originals. The output environments report Python 3.13.2 and SymPy 1.14.0. These received runs are not represented as reruns performed here.

The specifically named 15-check `triad_orientation_normalization_audit.py` is not among these attachments or archive members. Its reported execution remains peer-reported. The receiving implementation below supplies its own independent, exit-gated checks; no extra upload is required for the conclusions established here. No T-6j2 producer or event log was recovered. The author's declaration that that session code was never committed is retained as an author report.

## 3. Which model was actually recovered?

T-6a1, T-6c2 and T-6e use the same lifted graph-force model: vertices 0,S,C,D, cubic forces from the quadratic metric, order-six planar linear core, planar S/C components reset to z=0 at each step, and a diagonal initial D whose components then evolve. Coordinate terms are retained to degree three; invariant increments to degree four.

This is not the primitive dyadic sine/exponential map by mere filename or coordinate notation. The recovered `triad_symbolic_core.py` separately uses that primitive map and an edge-to-Jacobi projection. The 96:1 cross-model correspondence question is therefore not settled by recovering the orientation convention. The diagonal initial gauge and planar component restriction are model operations, not proof of an unrestricted K4 flow or a passive chart transformation.

The source metric is

\[
\mathsf B_T=\begin{pmatrix}2&-1&0\\-1&2&0\\0&0&1\end{pmatrix},
\qquad B_T^{\rm plane}=2B_G.
\]
(rep: recovered T-6 lifted graph-force producer; B_G is the earlier primitive two-dimensional comparison form)

On the source planar representative,

\[
s_\rho=\sqrt{Q_s^T/2},\quad s_\eta=0,\quad
c_\eta=\frac{\Omega_T}{\sqrt3s_\rho},\quad
c_\rho=\frac12\left(c_\eta+\frac{I_T}{s_\rho}\right),
\]
(rep: recovered T-6c/T-6c2 reduction, Q_s^T>0)

one has exactly

\[
Q_s^TQ_c^T-I_T^2=\Omega_T^2,
\qquad \omega_{\det}=s_\eta c_\rho-s_\rho c_\eta=-\frac{\Omega_T}{\sqrt3}.
\]
(rep: recovered T-6 metric/orientation convention, not a registered physical Genesis bridge)

Consequently the source's root variable is `Omega_T`, and the T-6e reported output is `Delta omega_det`. If H_j are the returned r^j polynomials, then

\[
\Delta\Omega_T^{[4]}=-\sqrt3\sum_{j=0}^{2}r^jH_j(Q_s^T,I_T,\Omega_T).
\]
(rep: correctly typed invariant-degree-four output conversion; arguments remain in the producer's Omega_T convention)

A fully raw-determinant presentation would ALSO substitute Omega_T=-sqrt(3) omega_det into the arguments of all invariant coefficient functions. Multiplying only one equation is the correction when retaining the existing normalized input/state convention.

## 4. Fresh independent finite-jet reconstruction closes the supplied radial-algebra gap

The received T-6c2/e runs were read, not executed again. Independently, `reconstruct_recovered_jet.py` constructs the same diagnostic generator's cubic iterate without importing any producer. For a map T(x)=Lx+H3(x), it uses

\[
x_j^{[1]}=L^jx_0,\qquad
G_{j+1}=LG_j+H_3(x_j^{[1]}),\quad G_0=0.
\]
(rep: exact coordinate-degree-three recursion for the recovered cubic-force generator)

This is mathematically equivalent at degree three to the supplied full-expression composition followed by truncation; discarded terms cannot feed back into lower degrees. It reproduces all r^0,r^1,r^2 terms of both supplied outputs. It ALSO derives Delta Qs, Delta Qc and Delta Qd from the recovered vector generator, and matches every corresponding coordinate coefficient copied into T-6a2 and T-6c.

Thus the minor gap about radial coefficient consistency is closed **for the supplied generator and copies, at the retained jet order**. This is not a claim that the original T-6a1 executable or its old campaign was rerun, nor proof of byte identity with an undocumented historical run. The new result is separately logged and source-pinned.

`check_normalization_chain.py` executes **63 checks**, including per-order extraction matches, both copied-radial source tables, root-model coefficient matches, Gram identities, consumer formula reuse and angular-polynomial tests. Counts are checks, not independent scientific theorems. Static AST arithmetic is evaluated exactly; it does not pretend that all downstream Python numeric literals or lambdified ODE evaluations use exact rational arithmetic at runtime.

## 5. Corrected diagnostic consequences

### Gram tangency

Let f_s,f_c,f_I be the recovered invariant increments used as the declared ODE's RHS, H the raw determinant rate, and f_Omega=-sqrt(3)H. For each radius order separately,

\[
\frac{I_T^2+\Omega_T^2}{Q_s^T}f_s+Q_s^Tf_c-2I_Tf_I-2\Omega_Tf_\Omega=0.
\]
(rep: recovered finite-jet coefficient identity; source planar constraint)

In the **same formal five-variable algebraic extension used by the downstream code**, with Qc allowed independent but the reduced coefficient formulas retained, define

\[
\mathcal G=Q_s^TQ_c^T-I_T^2-\Omega_T^2,\quad
K=\frac{I_T^2+\Omega_T^2}{Q_s^TQ_c^T}.
\]
(rep: diagnostic off-surface extension; not a derived physical interior carrier)

The corrected field obeys

\[
\dot{\mathcal G}=\frac{f_s}{Q_s^T}\mathcal G,
\qquad
\boxed{\dot K=(1-K)\frac{f_c}{Q_c^T}.}
\]
(rep: exact identities of that specified rational ODE on positive-amplitude regular domains)

Therefore its ambient normal derivative is zero at K=1; it has no old outward/inward K=1 sectors. Interior/exterior crossing cannot occur at finite time while the indicated smooth-domain conditions hold. This does not rule out collapse, blow-up or termination at a domain boundary. It also does not make an arbitrary K<1 state a pair of actual planar vectors.

The numerical sector and fatal-contact classifications generated with f_Omega=H cannot be transferred to this corrected field. The old outputs remain records of the executed model; they are not evidence for the corrected model.

### Large-u torsion

For r=0 and I_T=mu sqrt(u) Q_s^T, Omega_T=nu sqrt(u) Q_s^T, the incorrect update reproduces exactly the old leading ratio polynomial

\[
9\sqrt3x^2+(21+5\sqrt3)x-3,
\qquad x=\nu/\mu.
\]
(rep: historical mis-scaled diagnostic; polynomial root remains historical algebra)

With the correct -sqrt(3) conversion, the leading coefficient of u in dot(theta)/Q_s^T is

\[
\boxed{3\sqrt3\mu^2+6\mu\nu+9\sqrt3\nu^2}
=3\sqrt3(\mu+\nu/\sqrt3)^2+8\sqrt3\nu^2>0
\]
(rep: corrected r=0 leading-large-u diagnostic, K=mu^2+nu^2>0)

and its ratio polynomial is

\[
9\sqrt3x^2+6x+3\sqrt3,
\qquad \mathrm{disc}=-288.
\]
(rep: same corrected leading diagnostic)

There is no real replacement x_* in this leading equation. This does not prove full finite-u steering, an escape basin or a physical obstruction; subleading and r-dependent terms remain, and no new ODE sweep is performed.

### T-6m turn and the doubled metric

The recovered T-6c2 polynomial still gives

\[
\Delta I_T|_{I_T=0,\,\Omega_T=-2(Q_s^T)^2/\sqrt3}
=2(Q_s^T)^3(12(Q_s^T)^2+4Q_s^T-9).
\]
(rep: recorded producer-frame reference ansatz Qc^T=4(Qs^T)^3/3, not a physically selected Genesis birth)

Its positive root remains `(2sqrt(7)-1)/6`. The earlier 0.6194 sensitivity reading is not the normalization selected by these recovered bytes. This restores the provenance of the recorded forcing formula, not T-6m's withdrawn wedge comparison.

The requested relation Q_T=2Q_G is valid for the **same planar vectors**. Under that extra identification, I_T=2I_G and Omega_T=-sqrt(3) omega_raw. A Genesis law `Qc^G=kappa^2(Qs^G)^3` would become

\[
\boxed{Q_c^T=\frac{\kappa^2}{4}(Q_s^T)^3,}
\]
(rep: conditional same-vector metric transport, not an established generator/event bridge)

so the shear coefficient would be 1/3, not the copied 4/3. Do not silently change either reference law: record the unresolved birth/mode identification. This is why the RRF entry must describe source/target metrics, vectors and operations, not globally assert that every Triadic Q is twice every Genesis Q. The apex z-component has no such automatic identification with the primitive two-dimensional d-mode.

## 6. Correction footprint and custody

Keep the extraction correction distinct from result/module disposition:

- **T-6c2:** polynomial and input convention verified; attach actual recovered producer under the existing artifact identity.
- **T-6e:** correct raw-output extraction retained; withdraw the automatic identification of its output with a normalized orientation rate and any unsupported five-dimensional physical interpretation.
- **T-6d/d2:** root convention is consistent. Its derivative formulas are retained; no historical numerical campaign was rerun, and this does not certify its reduced generator as a physical event law.
- **T-6f/h/i/i2/k/k2/l and T-6j:** recovered producers demonstrably reuse H as dot Omega. Preserve historical outputs/bytes, but remove downstream interpretations as results of the correctly normalized system. New corrected claims require their own statement/evidence, not rescaling plotted endpoints.
- **T-6j2:** original code/log still lost. Root-closed excursion and stopping descriptions remain author-reported; no-safe-basin/fatal classifications are withdrawn, module PARTIAL. Producer recovery elsewhere does not restore this experiment.
- **T-6m:** fixed quarter-turn and conditional recorded forcing polynomial remain; full wedge-based obstruction remains PARTIAL/OPEN. A narrower exact-angle successor needs its own identity if used as a result replacing the obstruction proposition.
- **T-6r:** the missing normalization/extraction dependency can close, but the full corrected state/carrier/proxy/test contract and its numerical evidence remain unresolved. Replace the obsolete missing-source blocker rather than pretending the sweep is complete.
- **T-6p:** the protocol may remain a definition, with obsolete dependency-discharge and no-basin/wedge exports removed.
- **T-6g radial square identities:** its recovered producer uses the radial equations, not the erroneous orientation rate. Those fixed-expression algebraic identities are not withdrawn by this factor correction; any global phase/stability interpretation remains a separate claim.
- **T-6s/t/u, raw GSPLIT and OPEN 1C:** unaffected by this source-convention correction within their existing scopes. Do not rerun or rederive their primary certificate merely for this change.
- **96:1:** retains only its exact arithmetic until the generator/mode/time/observable correspondence is provided. Recovered graph forcing does not supply that bridge.

The proposed COR/CN-05 texts accompany this review. Their result/RID fields are not registrations. Under Methodology §4.4, retain IDs for corrected readings of the same extraction; use successor identities when a numerical no-basin result or dynamical obstruction is replaced by a materially different restricted proposition. The new normalized tangency/torsion algebra, if installed as load-bearing owner science, needs its own adopted statement, evidence and owner-assigned RID rather than being hidden in a guard.

## 7. Source and availability limits

The exact producer directory and two supplied outputs are preserved unchanged. Key source locations and consumer reuse sites are recorded in `data/source_trace.json`. No current attachment needed reupload. Some much older attachment references have expired; the absent session-only T-6j2 log and the named prior 15-check audit are not claimed as inspected or reconstructed.

The ZIP and LastWriteTime inventory establish recovered current bytes, not an authenticated historical run. The new 63-check audit and independent cubic recursion are separate receiving evidence. No numerical trajectory, C0 encounter, basin coverage, physical relabel, gauge, source law, or event predicate was selected or validated here.
