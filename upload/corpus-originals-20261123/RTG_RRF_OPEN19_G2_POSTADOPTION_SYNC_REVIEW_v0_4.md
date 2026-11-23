# RRF — OPEN 19 / G2 / K3 source reconciliation and post-adoption sync plan

**Date:** 16 October 2026  
**Status:** `[SESSION] NONCANONICAL — DRAFT-SUCCESSOR AWARENESS / COROLLARY U SQUARE-ROOT ROUTE / OPEN 20 (B-∞) REFINEMENT; OWNER ADOPTION PENDING`  
**Revision base:** `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_3.md`  
**Custody:** DYAD owns the formal centralizer theorem, Corollaries U/A and OPEN 20; Genesis owns the K3 result; RRF owns the representation/realization interface. **No adopted owner DSN, RRF standard, or G2 interface record is changed by this note.**

## 1. Source and inspection manifest

**Directly inspected in this revision (full relevant sections):**

- `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_1.md` (entire original review; SHA-256 `20f68a44ace3b7cfdb4a7ff5b506e101e7d4acbb9fb8e251c74c0a2feb98f4c3`).
- `RTG_DYADIC_OSCILLATOR_DSN_v6_4_11.md` (adopted; §2 OPEN 19, §6.15, §7; SHA-256 `6fccd429758adb729032a68c2a99e24a7bab6f5226aae5df1453b09b189ccb2e`). This *released* version still lists `DYAD-OPEN-FORMAL-CENTRALIZER` as OPEN.
- `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_1.md` (§§2.3–2.4, 4.2, 6.2, 8.12; adopted RRF working standard), and `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW_v0_2_1.md` (§§2–6; noncanonical).
- `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1.md` (entire SESSION proof and scope; SHA-256 `017295911120951d75d03e8a2ffafa6352f8b8cda0a7c0aaa96396710165838d`).
- `DSN_METHODOLOGY_v1_3.md` §4.3 (owner RID and import rules).
- The participant's 16 October 2026 detailed corrections, including the reported all-degree proof steps, the v0.1.2 dimension classification, and the 16 October Corollary U / smooth-flat-centralizer / Corollary A source refinements.
- The participant's subsequent 16 October 2026 source-specific audit of **`RTG_DYADIC_OSCILLATOR_DSN_v6_4_12_DRAFT_r1`** (draft §6.16 and §6.15), plus the reported SESSION v1.1/v1.2 square-root construction and the OPEN 20 (B-an)/(B-∞) split. These are **participant-reported draft contents**, not direct file inspection or owner adoption.

**Reported by participant but NOT directly available in this runtime:** `claude/DYAD_OPEN19_FORMAL_CENTRALIZER_PROOF_SESSION.md`; `RTG_DYADIC_OSCILLATOR_DSN_v6_4_12_DRAFT_r1` (exact filename/bytes not verified); SESSION v1.1/v1.2 OPEN 19 studies; `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1_2.md`; `cent.py` and its outputs; `dyad_open19_kernel_check.py`; `k3_obstruction_exact_check.py`/`fac.py` executables. The user reports inspecting the first two documents and validating the proof; this review therefore no longer treats the *absence of an all-degree proof* as a scientific blocker, but **does not claim direct source inspection, byte/hash verification, or script execution for those missing files**. Owner adoption remains a separate act. **Status split:** adopted v6.4.11 still has OPEN 19 OPEN; participant-reviewed v6.4.12 DRAFT r1 reportedly has `OPEN 19 → CLOSED (formal)` in proposed §6.16, with `DYAD-ALG-CENT-KERNEL`, `DYAD-THM-FORMAL-CENTRALIZER`, and `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`; an analytic `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` proposed in §6.15; and successor OPEN 20 (`DYAD-OPEN-INVOLUTION-REALIZATION`, branches B-an/B-∞). **These are not adopted owner facts at this time.**

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

**Owner status and RID custody:** released DYAD v6.4.11 retains `DYAD-OPEN-FORMAL-CENTRALIZER` OPEN. Candidate owner registration is `PROPOSED CLOSURE [THM — formal]`; **only an adopted DYAD successor** may relabel it `CLOSED (formal) [THM — formal]`. Suggested RIDs (not adopted/assigned here): `DYAD-ALG-CENT-KERNEL`, `DYAD-THM-FORMAL-CENTRALIZER`, `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`. The theorem is about the formal **six-step** return \(F=T^6\); do not silently replace its centralizer with that of \(T\) or an independently chosen one-step normal form. **Draft update:** the reported v6.4.12 DRAFT r1 already performs the Lemma K, Theorem C, Corollary U, corrected `a=0` boundary and analytic Corollary A integration requested here. This changes the owner work item from *draft it* to *review/adopt the existing draft*.

### 2.2 Formal involution and analytic corollary — square-root-first draft owner chain

**[ALG — reconstruction from participant-reported DYAD v6.4.12 DRAFT r1 / Corollary U; original draft not mounted]** Put `F=T^6` and let `F^{1/2}=exp((1/2)log F)` denote the **unique formal tangent-to-identity square root**, whose inverse is `F^{-1/2}`. The proposed owner construction is

\[
\boxed{R_0=T^3F^{-1/2}.}
\]

Because `T` commutes with `F`, it commutes with their formal logarithmic powers. Hence `R_0` formally commutes with primitive `T`, and

\[
R_0^2=T^6F^{-1}=I,\qquad DR_0(0)=DT^3(0)=-I.
\]

**Proposed Corollary U** establishes uniqueness of the formal nonidentity involution commuting with the *six-step* `F` via the proposed all-degree centralizer classification; it then identifies the normal-form presentation

\[
\widehat S_{\rm NF}=\widehat h(-I)\widehat h^{-1}=R_0.
\]

The normal-form expression is a **secondary identification**, not the primary existence construction. The `T^3F^{-1/2}` route is a DYAD draft owner proof in its own right; it is not an import from an unadopted G1 SESSION theorem. For the *fixed finite* `h_6` chart, the previously registered equality remains **only** `\mathcal J_{\le6}S_h=\mathcal J_{\le6}R_0` under the declared normalization convention.

**Proposed Corollary A, reported in DYAD draft §6.15 (`DYAD-THM-ANALYTIC-CLOCK-BRIDGE`).** Let `R` be a nonidentity real-analytic involution germ commuting with `F` on the §6.15(b) domain. Adopted DYAD v6.4.11 §6.15(b) supplies `R(0)=0`, `DR(0)=-I` (the draft may display `DR=-I` as a redundant hypothesis with an explanatory parenthesis). Conditional on adopted formal Corollary U, `j^∞R=R_0`; thus `R_0` converges, `R=R_0` as an analytic germ and **`RT=TR` exactly**. This does not identify a physical node action or full G2 realization. For `C^∞` one only obtains infinite-jet equality and flat primitive-commutation defect; for finite `C^r` neither all-order formal uniqueness nor convergence may be inferred.

**[ALG — independently derived local analytic existence equivalence; candidate DYAD owner B-an import pending]** The square-root construction yields the precise *mathematical* G2-PRE / Problem B bridge:

\[
\boxed{\begin{aligned}
&\text{analytic nonidentity involution germ commuting with primitive }T\\
&\quad\Longleftrightarrow\quad\text{analytic odd chart for }T\\
&\quad\Longleftrightarrow\quad\text{analytic tangent-to-identity square root }Q\text{ of }F=T^6.
\end{aligned}}
\]

**Proof and qualification (does not require Corollary U).** If analytic `Q` satisfies `Q^2=F` and `DQ(0)=I`, its formal germ is the unique tangent-to-identity square root `F^{1/2}=exp((1/2)log F)`. Since `T` commutes with `F`, `TQT^{-1}` is another analytic tangent-to-identity square root of `F`; its formal series therefore equals that of `Q`, and **analyticity gives `TQ=QT` exactly**. Thus `R_0=T^3Q^{-1}` is an analytic nonidentity involution commuting with primitive `T`, and `\Phi=(id-R_0)/2` is an analytic odd chart. Conversely, an analytic odd chart yields an analytic nonidentity involution `R` commuting with `T`; now simply set `Q=T^3R`. Then `Q` is analytic, tangent to the identity (`DQ(0)=A^3(-I)=I`) and `Q^2=T^6=F`. The equivalence requires only the stated local invertibility, fixed-point and analytic-germ/domain conventions, **not** proposed formal Corollary U. Corollary U is needed for the additional classification of *all* nonidentity six-step commuting involutions and the analytic six-step-to-primitive bridge; it remains unadopted here. This is an existence result for the isolated dyad germ only; it supplies none of the physical `E,F_{\rm net},\sigma` G2 gates. The separate `C^∞` square-root/odd-chart problem and the `C^∞` exact primitive-versus-six-step commutation problem remain distinct.

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

> **[OPEN — refinement of existing draft `DYAD-OPEN-INVOLUTION-REALIZATION` / OPEN 20 (B-∞), *not a new RID*]** Is every \(C^\infty\) germ \(K\) commuting with \(F=T^6\), satisfying \(K(0)=0\), \(DK(0)=I\), and \(j^\infty K=\mathrm{id}\), necessarily the identity germ, in the declared local domain/regularity class?

If this smooth flat-centralizer is trivial, then \(K=\mathrm{id}\), hence \(R'=R\) and **\(RT=TR\) exactly**. Triviality is a **sufficient condition** for the primitive-clock implication; this reasoning does **not** show it is necessary, because nontrivial flat centralizer elements might exist without arising as \(R'R\) for an involution \(R\). No literature theorem is imported or presumed to resolve this two-real-dimensional parabolic/spiral problem. The one-dimensional analogy is motivation, not a certificate.

**Regularity distinction:** In the analytic category, a flat analytic germ is automatically the identity; thus proposed Corollary A follows directly and the two clocks agree for the specified **nontrivial analytic involutions**. In the smooth category, equality of infinite jets does not imply equality of germs. For finite \(C^r\), even all-order flatness is not a meaningful assumption without additional smoothness. This question is a **refinement of draft OPEN 20 (B-∞) within the broader Problem B programme**, distinct from L-SHADOW-POLY (finite \(C^r\) uniqueness transfer); it does not settle smooth odd-chart existence.

**Owner request to DYAD:** refine the **already existing draft OPEN 20 (B-∞)** text to record `K=(TRT^{-1})R`, `KF=FK`, `j^∞K=id` and the **sufficient, not proved necessary** flat-centralizer triviality criterion. **Do not create `DYAD-OPEN-SMOOTH-FLAT-CENTRALIZER` as a duplicate RID.** Analytic Corollary A and both-clock uniqueness should cite proposed **Corollary U via `R_0=T^3F^{-1/2}`**; this is already reportedly drafted. RRF remains an interface consumer and does not assign scientific owner RIDs.

### 2.4 Adopted-versus-draft DYAD status and exact recipient actions

| Item | Adopted DYAD v6.4.11 | Participant-reported DYAD v6.4.12 DRAFT r1 | RRF action |
|---|---|---|---|
| OPEN 19 / formal centralizer | `DYAD-OPEN-FORMAL-CENTRALIZER` OPEN | CLOSED (formal) **in draft only**; proposed Lemma K / Theorem C / Corollary U §6.16, owner RIDs as reported | Retain adopted-vs-draft distinction; await DYAD adoption |
| Boundary `a=0` | Formal proof not in adopted owner | `[COR r1]`: boundary coefficient follows from `μ≠0` | Do not reopen; verify adopted final on receipt |
| Analytic clock bridge | §6.15(b) local germ dichotomy adopted | `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` proposed in §6.15 | Pin after adoption; keep analytic vs smooth separate |
| OPEN 20 / Problem B | Not registered as successor here | `DYAD-OPEN-INVOLUTION-REALIZATION`, B-an/B-∞, OPEN | Register as **draft-reported dependency**, not new RID |
| B-an square root | Not owner-established here | analytic `F^{1/2}` convergence claimed as the equivalent analytic existence test | G2-PRE candidate dependency; draft status retained |
| B-∞ flat commutation | Not owner-established here | question already present; mechanism can be sharpened by `K` reduction | **Refine** existing OPEN 20 (B-∞), no extra OPEN |

## 3. K3 — dimension refinement

**[COR to v0.1 §4.6]** The initial SESSION v0.1 directly inspected here proves only the \(C^3\) rank-two planar no-go; the participant reports that the successor `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1_2.md` §4 *also records* the dimension-one and dimension-three obstruction at \(C^1\). Its detailed algebra can be verified independently of that unavailable file:

Let \(L=DF_1(0)=A\oplus A\), where \(A\) has nonreal eigenvalues \(e^{\pm i\pi/3}\). For a \(C^1\) submersive factor \(E\) onto a real \(d\)-dimensional target, \(DE(0)L=DT'(p)DE(0)\); therefore \(\ker DE(0)\) is \(L\)-invariant. Since \(A\) generates a complex structure, any invariant *real* subspace has even dimension. The kernel has dimension \(4-d\); for \(d=1,3\) this is odd — contradiction.

**[ALG — independent linear-algebra consequence; source v0.1.2 participant-reported]** Thus \(d=1,3\) rank-\(d\) \(C^1\) factors are excluded for the **named projected \(K_3\)** primitive model, under the same fixed-point/local-factor hypotheses. For \(d=2\), \(\dim\ker DE=2\) is compatible with the linear action and the additional **cubic** obstruction in SESSION v0.1 applies to \(C^3\) factors. No blanket \(C^1/C^2\) no-go for \(d=2\) follows. No claim is made about general targets \(d\ge4\), other network models, physical admissibility or source-owner adoption.

The version identity, full text and declared RID/status of `...v0_1_2.md` must be verified upon receipt; the independently derived odd-dimension obstruction can be retained as a `[SESSION]` consequence in the meantime.

## 4. Corrected reading of adopted RRF §6.2

**[COR to v0.1 §4.2]** The *actual* adopted RRF v0.8.1 §6.2 guard is: “Formal G1 uniqueness for \(T\)-commuting actions must not be transferred to a hypothesis requiring commutation with \(T^6\) alone.” The prior review paraphrased this as an unqualified assertion that six-step-only commutation **can never** imply primitive commutation; that paraphrase overstated the source. The existing RRF statement was an evidence/logic boundary, not a universal no-go theorem.

After **owner adoption** of Corollary U, update this guard with the analytic/smooth distinctions in §§2.2–2.3 rather than declaring the old source text mathematically refuted. Also preserve the separate factor-contract distinction \(EF=TE\) versus \(EF=T^6E\); an analytic equivalence of *involution germs* does not make these two network factor contracts equivalent.

## 5. Consumer synchronization queue — draft prepared, adoption not presumed

| Consumer location | Correct action and boundary | Release trigger |
|---|---|---|
| DYAD v6.4.12 DRAFT r1 §6.16 / §6.15 | **Already drafted per participant:** Lemma K / Theorem C / Corollary U via `R_0=T^3F^{-1/2}`, boundary `a=0` correction, analytic Corollary A and OPEN 20 (B-an/B-∞). **Review and adopt existing draft, not open duplicate implementation work.** | DYAD scientific-owner review/adoption |
| DYAD draft OPEN 20 (B-∞) | Refine existing smooth question with `K=(TRT^{-1})R∈Cent_{C^∞}(F)`, `j^∞K=id`; flat-centralizer triviality **sufficient, not necessary as far as shown**. No new RID. | DYAD draft editorial/scientific review |
| RRF v0.8.1 §§2.4, 4.2 | On adoption repin G1 `source-pending` language to DYAD §6.16 / Corollary U owner RID; preserve finite `h_6` jet guard. | After DYAD release |
| RRF §6.2 | After adoption register analytic six-step-to-primitive involution bridge, distinct primitive/six-step **factor** contracts, and B-∞ flat-centralizer OPEN. | After DYAD release |
| RRF §8.12 | Replace only former owner-adoption nonclaim; retain lack of automatic analytic convergence and no finite `S_h` identification beyond degree six. | After DYAD release |
| G2 v0.2.1 §3 | Already adopted v6.4.11 §6.15(b) supersedes “`DT^6=I`, no `±I` restriction” at `C^3`; this lemma correction may be drafted **now**. | Adopted DYAD v6.4.11 |
| G2-PRE / DYAD owner handoff | Add conditional **analytic odd chart ⇔ analytic tangent-to-identity square root of `F=T^6`**; classify as B-an / proposed §6.16 Corollary U until DYAD adoption. Separate B-∞ exact six-step commutation and primitive G2 factor. | Draft pointer now; owner theorem import after adoption |
| K3/G2 factor interface | Retain `C^1` odd-dimensional no-go for `d=1,3` and `C^3` `d=2` no-go in named model; do not extrapolate rank-2 `C^1/C^2` or physical-selection conclusions. | SESSION now; Genesis owner review later |

## 6. Disposition

**[COR to v0.3 §§2.2–2.3, 5]** The formal construction is **square-root first** (`R_0=T^3F^{-1/2}`), with normal-form agreement following proposed Corollary U; this proof is reportedly already integrated into DYAD v6.4.12 DRAFT r1, not a missing owner drafting task. The smooth exact primitive-commutation question is **OPEN 20 (B-∞) refinement**, not a new `DYAD-OPEN-SMOOTH-FLAT-CENTRALIZER` RID and not finite-regularity L-SHADOW-POLY. Analytic G2-PRE is equivalent, by direct analytic-germ reasoning **without Corollary U**, to existence of an analytic tangent-to-identity square root of `F=T^6` (participant-reported draft OPEN 20 B-an). These remain draft/SESSION-status interfaces; the owner draft proof file was not locally mounted in this revision.

**`ACCEPT SCOPED [SESSION] — DRAFT-SUCCESSOR COORDINATED; DYAD v6.4.12 OWNER ADOPTION PENDING`.**

- The earlier “all-degree proof still needs to be provided” **as a claim about the project's research status** is withdrawn: a complete proof file has been identified and independently reviewed by the participant. **Its full file contents were not mounted/read here**; that source-integrity gap remains for artifact-based release checks, not a claim that no proof exists.
- The K3 odd-dimension classification is independently transparent at the linear level and reported in v0.1.2; this revision corrects the previous “uninspected classification” characterization without pretending to inspect the absent successor file.
- Adopted DYAD v6.4.11 still says OPEN 19 is OPEN. **The participant-reported v6.4.12 DRAFT r1 already registers proposed formal closure and OPEN 20 (B-an/B-∞)**; the corresponding adoption has not been verified. A draft closeout is **not** an adopted scientific-owner closeout.
- Adopted RRF v0.8.1 and G2 v0.2.1 remain unchanged. No adopted theorem, physical exchange, carrier regularity, birth law or network factor is selected by this synchronization note.
