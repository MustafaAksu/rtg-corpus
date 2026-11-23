# RRF — OPEN 19 / G2 / K3 source reconciliation and post-adoption sync plan

**Date:** 16 October 2026  
**Status:** `[SESSION] NONCANONICAL — CORRECTED REVIEW AND REGULARITY/FLAT-CENTRALIZER HANDOFF; DYAD OPEN 19 OWNER ADOPTION PENDING`  
**Revision base:** `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_2.md`  
**Custody:** DYAD owns the formal centralizer theorem; Genesis owns the K3 result; RRF owns the representation/realization interface. **No adopted owner DSN, RRF standard, or G2 interface record is changed by this note.**

## 1. Source and inspection manifest

**Directly inspected in this revision (full relevant sections):**

- `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_1.md` (entire original review; SHA-256 `20f68a44ace3b7cfdb4a7ff5b506e101e7d4acbb9fb8e251c74c0a2feb98f4c3`).
- `RTG_DYADIC_OSCILLATOR_DSN_v6_4_11.md` (adopted; §2 OPEN 19, §6.15, §7; SHA-256 `6fccd429758adb729032a68c2a99e24a7bab6f5226aae5df1453b09b189ccb2e`). This *released* version still lists `DYAD-OPEN-FORMAL-CENTRALIZER` as OPEN.
- `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_1.md` (§§2.3–2.4, 4.2, 6.2, 8.12; adopted RRF working standard), and `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW_v0_2_1.md` (§§2–6; noncanonical).
- `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1.md` (entire SESSION proof and scope; SHA-256 `017295911120951d75d03e8a2ffafa6352f8b8cda0a7c0aaa96396710165838d`).
- `DSN_METHODOLOGY_v1_3.md` §4.3 (owner RID and import rules).
- The participant's 16 October 2026 detailed corrections, including the reported all-degree proof steps, the v0.1.2 dimension classification, and the 16 October Corollary U / smooth-flat-centralizer / Corollary A source refinements.

**Reported by participant but NOT directly available in this runtime:** `claude/DYAD_OPEN19_FORMAL_CENTRALIZER_PROOF_SESSION.md`; `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1_2.md`; `cent.py` and its outputs; `dyad_open19_kernel_check.py`; `k3_obstruction_exact_check.py`/`fac.py` executables. The user reports inspecting the first two documents and validating the proof; this review therefore no longer treats the *absence of an all-degree proof* as a scientific blocker, but **does not claim direct source inspection, byte/hash verification, or script execution for those missing files**. Owner adoption remains a separate act.

## 2. OPEN 19 — correction to the prior proof assessment

### 2.1 All-degree argument: existence reported, owner adoption pending

**[COR to v0.1 §2]** The earlier statement that the all-degree kernel proof still needed to be produced is **superseded as a project-status assessment**. The participant identifies a complete Lemma K proof in `claude/DYAD_OPEN19_FORMAL_CENTRALIZER_PROOF_SESSION.md`, and reports checking its Steps 4–5 for every homogeneous degree. Finite-degree rank checks ($k=2\ldots9$ or $k=2\ldots13$) are corroboration, **not** the claimed basis of the proof.

**[ALG — independently checked numerical identities, not proof-source re-execution]** For the RTG parameter

\[
\mu=-\frac12-\frac{2\sqrt3}{3}i,
\qquad \operatorname{Re}(\mu^2)=-\frac{13}{12},
\qquad |\mu|^2=\frac{19}{12}.
\]

The user's all-degree proof audit reports:

- **Paired monomial orbits:** the imaginary-part condition yields \(b=a-1\) or \(b=2-a\), the latter forcing \(k=2\); the remaining real-part term at \(k=2\) is nonzero (reported \(-m\), \(m=19/12\)).
- **Fixed monomial orbits:** the identity \(|\alpha|^2-m=4(a-1)(a-2)(\operatorname{Re}\mu)^2\) leaves the \(a=2\) branch, giving \(Y\in\mathbb R X_3\).
- **Boundary correction to proof Step 2:** at \(a=0\), there is no monomial with partner index \((b+1,-1)\). The isolated output coefficient forces \(c_{0,b}=0\) directly when \(\mu\ne0\); it should **not** be dismissed as imposing no further condition or be made dependent on \(\mu\notin\mathbb R\). The exceptional \((0,2)\) case belongs with this boundary analysis rather than the generic paired-orbit step.

**[SESSION, source-reported formal theorem]** The all-degree Lemma K plus the formal degree filtration is reported to establish \(\ker\operatorname{ad}_{X_3}=\mathbb R X_3\) (in the designated real homogeneous class) and the tangent-to-identity centralizer of \(F=T^6\). The algebraic passage from vanishing higher kernels to centralizer uniqueness is sound under the stated formal filtration/logarithm conventions: if \(e^{\operatorname{ad}Y}X=X\), then \(\frac{e^{\operatorname{ad}Y}-1}{\operatorname{ad}Y}\) has invertible constant term \(1\), so \([Y,X]=0\). The source document itself must be pinned in the successor DYAD proof/receipt.

**Owner status and RID custody:** released DYAD v6.4.11 retains `DYAD-OPEN-FORMAL-CENTRALIZER` OPEN. Candidate owner registration is `PROPOSED CLOSURE [THM — formal]`; **only an adopted DYAD successor** may relabel it `CLOSED (formal) [THM — formal]`. Suggested RIDs (not adopted/assigned here): `DYAD-ALG-CENT-KERNEL`, `DYAD-THM-FORMAL-CENTRALIZER`, `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`. The theorem is about the formal **six-step** return \(F=T^6\); do not silently replace its centralizer with that of \(T\) or an independently chosen one-step normal form.

### 2.2 Formal involution and analytic corollary — corrected owner chain

**[ALG — conditional on proposed Corollary U, not an adopted DYAD theorem yet]** In the declared formal normal-form convention, the formal normalizer `ĥ` takes the primitive map to a `λ`-equivariant normal form. Since `−I=λ³`,

\[
\widehat S_{\rm NF}=\widehat h\,(-I)\,\widehat h^{-1}
\]

commutes **formally with primitive \(T\)**. This source link belongs to the **Corollary U proof, step 1**, not to an unadopted G1 result. The alternative formal expression

\[
\widehat S_{\rm G1}=T^3F^{-1/2},\qquad F=T^6,
\]

also has the designated involution, derivative `−I`, and primitive-commutation properties under the specified formal inverse-square-root convention. **Proposed Corollary U**, through uniqueness of the formal nontrivial involution in `Cent(F)`, identifies the two descriptions. The G1 square-root construction is an **alternative representation/proof route**, not a separate owner dependency. This is a proposal awaiting DYAD owner adoption/RID.

**Proposed Corollary A (analytic clock bridge; exact hypothesis).** Let \(R\) be a **real-analytic, nonidentity involution germ** at the origin, defined on the DYAD §6.15(b) six-phase-tube domain, and suppose \(RF=FR\) for \(F=T^6\). Section 6.15(b) (adopted, `DYAD-THM-LOCAL-INVOLUTION-GERM`) first gives \(R(0)=0\) and \(DR(0)=-I\); neither must be postulated separately. Conditional on adopting Corollary U, \(j^\infty R=\widehat S\). Since \(R\) is analytic, this formal series converges to \(R\), and since \(\widehat S\) commutes formally with \(T\), analyticity implies **\(RT=TR\) as an exact germ identity**. Conversely, failure of analytic realizability of the nontrivial odd involution (analytic Problem B) excludes any such analytic six-step involution on the stated domain. This does **not** supply a physical full-network G2 factor.

For \(C^\infty\) \(R\), the same proposed formal theorem yields **\(j^\infty(RT-TR)=0\)** but does **not**, without an additional flat-centralizer statement, imply \(RT=TR\). Finite \(C^r\) conclusions are limited to justified finite jets; the separate L-SHADOW-POLY programme concerns such finite-regularity uniqueness transfers, **not the smooth flat-centralizer issue**.

**Finite-chart guard:** \(S_h=h_6(-I)h_6^{-1}\) remains an exact involution built from the *fixed finite* normalizer, with only the established degree-six jet equality \(\mathcal J_{\le6}S_h=\mathcal J_{\le6}\widehat S\). Owner formal uniqueness does not upgrade full finite \(S_h\) to the infinite formal or analytic map.


### 2.3 [OPEN] Smooth flat centralizer of the six-step return

**[ALG — conditional reduction; not an existence or rigidity theorem]** Suppose a nonidentity \(C^\infty\) involution germ \(R\) satisfies \(RF=FR\), with the domain/nontriviality hypotheses of adopted DYAD §6.15(b), and suppose **proposed Corollary U** has been established. The local primitive map \(T\) is invertible near \(0\). Define

\[
R' := T\circ R\circ T^{-1},\qquad
K := R'\circ R.
\]

Because \(T\) commutes with \(F=T^6\), both \(R'\) and \(R\) are nontrivial smooth involutions commuting with \(F\). Both have derivative \(-I\) by DYAD §6.15(b), and the proposed formal uniqueness theorem gives

\[
j^\infty R'=j^\infty R=\widehat S,
\qquad
KF=FK,
\qquad
j^\infty K=\mathrm{id}.
\]

Therefore \(K\) is a **smooth germ in the centralizer of \(F\), flat to the identity**. The missing implication is precisely:

> **[OPEN — proposed label: `DYAD-OPEN-SMOOTH-FLAT-CENTRALIZER`]** Is every \(C^\infty\) germ \(K\) commuting with \(F=T^6\), satisfying \(K(0)=0\), \(DK(0)=I\), and \(j^\infty K=\mathrm{id}\), necessarily the identity germ, in the declared local domain/regularity class?

If this smooth flat-centralizer is trivial, then \(K=\mathrm{id}\), hence \(R'=R\) and **\(RT=TR\) exactly**. Triviality is a **sufficient condition** for the primitive-clock implication; this reasoning does **not** show it is necessary, because nontrivial flat centralizer elements might exist without arising as \(R'R\) for an involution \(R\). No literature theorem is imported or presumed to resolve this two-real-dimensional parabolic/spiral problem. The one-dimensional analogy is motivation, not a certificate.

**Regularity distinction:** In the analytic category, a flat analytic germ is automatically the identity; thus proposed Corollary A follows directly and the two clocks agree for the specified **nontrivial analytic involutions**. In the smooth category, equality of infinite jets does not imply equality of germs. For finite \(C^r\), even all-order flatness is not a meaningful assumption without additional smoothness. This OPEN is **different from L-SHADOW-POLY** (finite \(C^r\) uniqueness-transfer route) and from **Problem B** (existence of an involution/odd chart in a selected regularity class).

**Owner request to DYAD:** place the smooth flat-centralizer question under OPEN 19's successor/Problem B dependency register as a separate OPEN or sub-OPEN, with no answer assumed. The analytical Corollary A should be cited to **Corollary U**, not to the not-yet-adopted G1 record. RRF remains an interface consumer and does not assign a scientific owner RID.

## 3. K3 — dimension refinement

**[COR to v0.1 §4.6]** The initial SESSION v0.1 directly inspected here proves only the \(C^3\) rank-two planar no-go; the participant reports that the successor `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1_2.md` §4 *also records* the dimension-one and dimension-three obstruction at \(C^1\). Its detailed algebra can be verified independently of that unavailable file:

Let \(L=DF_1(0)=A\oplus A\), where \(A\) has nonreal eigenvalues \(e^{\pm i\pi/3}\). For a \(C^1\) submersive factor \(E\) onto a real \(d\)-dimensional target, \(DE(0)L=DT'(p)DE(0)\); therefore \(\ker DE(0)\) is \(L\)-invariant. Since \(A\) generates a complex structure, any invariant *real* subspace has even dimension. The kernel has dimension \(4-d\); for \(d=1,3\) this is odd — contradiction.

**[ALG — independent linear-algebra consequence; source v0.1.2 participant-reported]** Thus \(d=1,3\) rank-\(d\) \(C^1\) factors are excluded for the **named projected \(K_3\)** primitive model, under the same fixed-point/local-factor hypotheses. For \(d=2\), \(\dim\ker DE=2\) is compatible with the linear action and the additional **cubic** obstruction in SESSION v0.1 applies to \(C^3\) factors. No blanket \(C^1/C^2\) no-go for \(d=2\) follows. No claim is made about general targets \(d\ge4\), other network models, physical admissibility or source-owner adoption.

The version identity, full text and declared RID/status of `...v0_1_2.md` must be verified upon receipt; the independently derived odd-dimension obstruction can be retained as a `[SESSION]` consequence in the meantime.

## 4. Corrected reading of adopted RRF §6.2

**[COR to v0.1 §4.2]** The *actual* adopted RRF v0.8.1 §6.2 guard is: “Formal G1 uniqueness for \(T\)-commuting actions must not be transferred to a hypothesis requiring commutation with \(T^6\) alone.” The prior review paraphrased this as an unqualified assertion that six-step-only commutation **can never** imply primitive commutation; that paraphrase overstated the source. The existing RRF statement was an evidence/logic boundary, not a universal no-go theorem.

After **owner adoption** of Corollary U, update this guard with the analytic/smooth distinctions in §§2.2–2.3 rather than declaring the old source text mathematically refuted. Also preserve the separate factor-contract distinction \(EF=TE\) versus \(EF=T^6E\); an analytic equivalence of *involution germs* does not make these two network factor contracts equivalent.

## 5. Consumer synchronization queue — no premature adoption

| Consumer location | Correct action and boundary | Release trigger |
|---|---|---|
| DYAD successor §2 / §6.15 / import ledger | Integrate full-degree Lemma K, Step-2 boundary correction, explicit \(F=T^6\), formal centralizer and **Corollary U** for both clocks; add analytic **Corollary A** with nonidentity-germ hypothesis; register smooth flat-centralizer triviality as a **separate OPEN**, not L-SHADOW-POLY; assign owner RIDs. | **DYAD owner review and adoption** |
| RRF v0.8.1 §§2.4, 4.2 | Change G1 “source pending” to adopted DYAD owner RID and section; maintain formal vs finite \(h_6\) distinction. | After DYAD release |
| RRF §6.2 | Add Corollary U-sourced analytic six-step→primitive implication; distinguish smooth *flat commutator* from the OPEN flat-centralizer triviality question; preserve distinct factor clocks. | After DYAD release |
| RRF §8.12 | Replace only the owner-adoption caveat; retain lack of automatic convergence and nonidentification with finite \(S_h\) beyond degree six. | After DYAD release |
| G2 v0.2.1 §3 | Supersede the first-derivative-only \(DT^6(0)=I\) argument with **already adopted** `DYAD-THM-LOCAL-INVOLUTION-GERM` (six-step \(C^3\) dichotomy); qualify primitive-commutation statement using future analytic Corollary A and the separate smooth flat-centralizer OPEN. | Lemma correction can be drafted now; analytic import after DYAD release |
| K3/G2 factor interface | Recognize \(C^1\) odd-dimensional no-go at \(d=1,3\); recognize \(C^3\) \(d=2\) no-go under named model; do not extrapolate to \(C^1/C^2\) rank-two or physical selection. | SESSION note now; Genesis owner import later |

## 6. Disposition

**[COR to v0.2 §§2.2, 5]** Smooth exact primitive commutation is tied to the triviality of a *flat smooth centralizer of \(F=T^6\)*, **not** to finite-regularity L-SHADOW-POLY. The source of formal primitive commutation/uniqueness is proposed **Corollary U**, not unadopted G1. The analytic bridge uses nontrivial-germ and DYAD §6.15(b) to deduce \(DR(0)=-I\). These refinements are mathematical interface recommendations only; the proof-session owner source has not been locally mounted in this revision.

**`ACCEPT SCOPED [SESSION] — PRIOR RRF REVIEW CORRECTED; OWNER ADOPTION PENDING`.**

- The earlier “all-degree proof still needs to be provided” **as a claim about the project's research status** is withdrawn: a complete proof file has been identified and independently reviewed by the participant. **Its full file contents were not mounted/read here**; that source-integrity gap remains for artifact-based release checks, not a claim that no proof exists.
- The K3 odd-dimension classification is independently transparent at the linear level and reported in v0.1.2; this revision corrects the previous “uninspected classification” characterization without pretending to inspect the absent successor file.
- Adopted DYAD v6.4.11 still says OPEN 19 is OPEN. A proof-session closeout is **not** an adopted scientific-owner closeout.
- Adopted RRF v0.8.1 and G2 v0.2.1 remain unchanged. No adopted theorem, physical exchange, carrier regularity, birth law or network factor is selected by this synchronization note.
