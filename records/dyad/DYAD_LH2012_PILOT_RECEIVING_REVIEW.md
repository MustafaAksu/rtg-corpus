# DYAD LH2012 — receiving review of corrected inputs and written pilot

**Date:** 23 October 2026. **Reviewer:** ChatGPT. **Status:** SESSION working review; no DSN amendment, adoption, release, notice or Stokes computation.
**Reviewed commit:** `220cc75d39e1796e3409e3bcc81fd275b154483f`, PR #21, branch `claude/dyad-open20-lh2012`; includes the R1/R2 correction commit `7355702`.
**Governing edition checked:** DYAD v6.4.22, tag `dyad-v6.4.22`; Methodology v1.4. B-an and B-6 remain ACTIVE.

## 1. Disposition and source coverage

**R1 and R2: CLOSED at receiving-review scope.** The summability application remains accepted at SESSION scope, with its P1-c SESSION dependencies. The alpha identity is now correctly conditional on `B*mu = 2*A*c40`.

**Pilot: ACCEPT WITH REQUIRED DESIGN REPAIRS; EXACT PREPARATION MAY PROCEED.** The sector inclusion and the two symmetry orbits are useful. E3 currently asks for an invariance that is false even for the model map; E1 does not yet provide a validated inverse branch. Correct those specifications in place before scouting/certification. There is no need for a versioned draft or DSN release. This is receiving-review clearance for stage 1, not PI adoption or authorization of a Stokes campaign.

Read in full: `DYAD_OPEN20_AN_LH2012_OWNER_ASSESSMENT.md`, `DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md`, and the corrected `dyad_lh2012_transfer_check.py` at the reviewed commit. Inspected the helper and replayed the corrected code. Re-read the supplied LH2012 transcription §§3–5, specifically the domains, Theorem 4.2 and its proof, and Theorem 5.1/Corollary 5.2. Transcription SHA-256 remains `9aa1ffa88ab87a92c5d77e0a672f409eaca17ee696dbb0f17cb605629d622978`; no comparison with publisher PDF bytes was made. Neither the paper nor its transcription is committed here.

## 2. Corrected-script replay (EV-HASH, EV-CODE, EV-RUN)

The connector-fetched script text was copied into the execution environment and checked before execution:
- `dyad_lh2012_transfer_check.py`: SHA-256 `adbe4c47b563c75c2ccf71e4846548aacd0a4406ffcee2cd3560d89b5935dbbc`.
- `dyad_h4_real_route_check.py`: SHA-256 `dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6d`.

Commands were `python -I -B dyad_lh2012_transfer_check.py` and separate `--control C`, `--control S`, `--control Z` runs.

| Run | Exit | Failed gates |
|---|---:|---|
| Positive | 0 | none; L1–L9 PASS |
| C | 1 | L3, L5 |
| S | 1 | L8, L9 |
| Z | 1 | L3, L5, L6 |

Positive stdout SHA-256: `01d01083c7ffe9fce45dcf2de102eebcade61d22288860e7a7765a56137f7352`. Its Git blob is `f489b6ce19ea34bd8ca3e01bc9150fc79b310258`, exactly the blob of the committed positive output. These are same-code receiving replays, not independent proofs of summability or of all-order branch uniqueness. The owner's newly reported replay of the original reviewer implementation is read as owner evidence; that original implementation was not rerun again in this turn.

The Z construction gives a double root because `B*mu = 2*A*c40`; the corrected code handles zero ell without division by zero and rejects it through the intended gates. Numeric root displays no longer determine L5.

## 3. D7: sector inclusion accepted; do not promote it to invariance

[ALG — SESSION, receiving derivation] Set eta = pi/4 and kappa = 2*cos(3*pi/8). Write q = xi^3 = s*exp(i*psi). For |psi| <= 5*pi/8 choose theta = clamp(psi, -pi/4, pi/4). Then |psi-theta| <= 3*pi/8, and

`|q - delta*exp(i*theta)|^2 < delta^2` iff `s < 2*delta*cos(psi-theta)`.

Consequently `s < kappa*delta` proves the claimed containment in the actual Hakim component. The adjacent overlap width is exactly `2*(5*pi/24)-pi/3 = pi/12`. Angular interiors are the holomorphic sectors; their angular closures can be used for enclosures inside a slightly larger open domain. No explicit value of the admissible delta_0 follows from this geometric inclusion.

### P-R3 — E3 must use the curved Hakim domains

The requested `f_u(S_j) subset S_j` is not a valid obligation for the wide straight sectors with a circular radial cutoff. Already for `f_0(xi)=xi-xi^4` and `xi=r*exp(i*theta)`,

`|f_0(xi)|^2/r^2 = 1 - 2*r^3*cos(3*theta) + r^6`.

For `pi/6 < theta < 5*pi/24`, cos(3*theta) is negative. Points sufficiently close to the outer radial boundary move outside the radial cutoff. Shrinking that cutoff does not fix the sign. The same leading obstruction persists for the normalized analytic map with an O(xi^5) remainder, for sufficiently small radii.

A fully rational model counterexample was evaluated in this review: choose unit direction `4/5+3*i/5`, so cos(3*theta) = -44/125; choose `R=1/100`, `r=R*(1-R^3/10)=9999999/1000000000`. Then `0<r<R`, the angle is strictly below 5*pi/24, and

`r^2*(1+(88/125)*r^3+r^6) > R^2`

exactly in rational arithmetic. Angular inclusion follows, for example, from cos(2*theta)=7/25 > cos(5*pi/12).

**Required replacement across D8 and E3–E6:** define the function space and Hakim fixed-point operator on the actual curved components Delta_j (with the rotated inverse normalization for odd j), prove uniform `f_u(Delta_j) subset Delta_j` for u in H_{Delta_j}, and restrict the selected fixed points to the S_j only for comparison. Orbits started in a comparison sector may leave that straight sector while remaining in Delta_j. This is exactly the domain distinction in LH2012 §4; Theorem 4.2(2) concerns nested curved Hakim domains, not arbitrary straight-sector truncations.

Use the weighted norm `sup_{Delta_j} |u(xi)|/|xi|^(m-1)`. An approximation in E6 must belong to the certified class or to an explicitly validated contraction neighborhood. E5 must bound the actual weighted tail, including the xi_0^alpha / xi_n^alpha factor and the chosen logarithm branches, not only an unweighted orbit sum. A common consistent Log shift cancels and is not a valid negative control; an inconsistent branch assignment is.

## 4. P-R4 — full analytic quotients and inverse validation

D2's phrase "quotients of the exact jets" must not define the map used in the fixed-point problem. Define the full analytic functions by

`G(x,u) = (F_z(x,x^2*u)-x)/x^4`,
`H(x,u) = (F_w(x,x^2*u)-x^2*u)/x^5`,

with the removable values at x=0. The finite jet proves the required divisibility and supplies normalization coefficients; it does not replace F by a truncation. The quoted lifted formulas then hold for the full germ. Remainder enclosures must include every omitted term.

E1's justification "T is entire" validates forward compositions, but does not construct or bound a single-valued F^{-1} on the chosen complex domain. DF(0)=I gives qualitative local inverse existence only. A later certificate must establish an inverse domain, branch, image containment and residual/tail bounds. One possible route is F(v)=v+R(v): for each target w in a specified domain, prove `v -> w-R(v)` maps a fixed domain into itself and has derivative norm <1 there. This yields the needed local inverse branch; no quantitative radius is supplied by this review. Formal inverse jets in stage 1 do not discharge this analytic obligation.

## 5. D10: two T^2 orbits accepted at sectorial-germ scope

[THM — SESSION consequence of the already accepted summability and formal-branch statements] The precise conclusion is

`Delta_{+,j} identically 0 <=> Delta_{+,j+2} identically 0`, with indices modulo six.

Thus the overlap indices have the two action orbits `{0,2,4}` and `{1,3,5}`. This is about identical vanishing of analytic germs, not pointwise nonvanishing everywhere, equality of jump magnitudes, or equality of Stokes constants.

**Receiving proof detail.** Let H=T^2=(P,Q), and let Gamma_j be the graph of the selected raw sum phi_j. The prior formal result gives H(Gamma_hat_+)=Gamma_hat_+, and H commutes with F. On a proper sector, define

`p_j(z)=P(z,phi_j(z)) = lambda^2*z+O(z^2)`.

After shrinking the radius and angular domain, this has an analytic inverse. The image graph is represented by

`v_j(zeta)=Q(p_j^{-1}(zeta), phi_j(p_j^{-1}(zeta)))`.

Analytic substitution and invertible reparametrization preserve the Gevrey asymptotic expansion on proper subsectors. Its formal graph is again Gamma_hat_+. Choose the sectors with enough angular margin that the common sector of v_j and phi_{j+2} still has opening strictly greater than pi/3; this is possible because the design uses opening 5*pi/12. Watson uniqueness identifies v_j with phi_{j+2}. Applying the same argument to H^{-1} proves the converse.

Equality of the two neighboring graph germs is preserved by this bijective graph transport, giving the stated equivalence. The horizontal parameters p_j and p_{j+1} generally differ: this is not the formula `Delta_{j+2}(lambda^2*z)=Delta_j(z)`. In particular, a zero at one numerically chosen point is not an identically zero jump. No explicit numerical transport radius or direct relation between the two parity orbits is obtained.

## 6. Stage-1 bookkeeping guards

1. **Branch labels:** choosing the root by Im(a)>0 is appropriate once an isolating enclosure is supplied. In the older P1-c record this numerical root was called a_-; the pilot calls it a_+. Add a short crosswalk or use a dedicated symbol a_pil. No existing historical result should be relabelled silently.
2. **Coefficient field:** a_+ and the unscaled b_n belong to E=Q(i*sqrt(3),a_+). The horizontal scale c_+ satisfies c_+^3=-ell_+. Normalized coefficients must be carried in E(c_+) (or an equivalent exact quotient/selected algebraic embedding), unless membership c_+ in E is separately proved. The inverse rotation exp(i*pi/3) already lies in the quadratic base field.
3. **Odd sectors:** make the transport explicit: if tilde u is computed in tilde xi = exp(i*pi/3)*xi, use its pullback to xi before the common raw-z formula D9. Do not mix the inverse-map coordinate with the forward coordinate in a point evaluation.
4. **m and jets:** compute b_1 and enough subsequent coefficients to determine the first nonzero term after subtracting b_1*x, then verify the normalized forward and inverse jets and their composition identities. These are exact preparation, not inverse-domain or remainder certificates.

## 7. Scope of the next work

Receiving-review support is limited to **stage 1: exact preparation**, with P-R3/P-R4 corrected in the same working design. No new review round is required merely to begin that algebra; the design repair can accompany its output. Scouting (stage 2) and interval/Stokes certification (stage 3) remain separate decisions. Any scouting result is to be recorded as NUM/non-certified, not as theorem evidence and not omitted from provenance. Stage 4 is the result classification, not an independently authorized computation.

Before certification, the full-domain operator, validated inverse, norms, tails and residual enclosures must be stated with actual constants. A certified enclosure of one actual same-branch jump excluding zero would prove branch divergence and, through the prior SESSION lemma, divergence of the tangent-to-identity formal log. It would still not decide B-an or B-6. An enclosure containing zero is inconclusive. No convergence assertion follows from a finite numerical test.

## 8. Repository and external-file custody

This review and its replay receipt are new records on the reviewed branch. They do not alter the owner assessment, pilot design, original evidence, canonical DSN, RID set, OPEN status, release tag or notices. PR #21 remains a draft; no merge is performed.

The original cover `48cc0de7-attachment.txt` with SHA-256 prefix/suffix `ef7fbc12...915b` was not found among this session's accessible files. The owner's possession is acknowledged, but the cover was not reconstructed or uploaded from prose. Its original bytes must be attached or supplied through the PI for unchanged upload. This absence is not a scientific blocker for stage 1. Tracked Python-cache cleanup is separate repository hygiene and is not included in this scientific PR.
