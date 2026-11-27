# Intrinsic strobe-boundary structure — Stage 2D: complement lifts, full formal centralizer and presentation contract

**Date:** 27 November 2026.
**Status:** SESSION / NONCANONICAL. ChatGPT prepares; Claude independent review requested; PI decides. No owner RID, canonical adoption, physical gauge selection or owner OPEN closure.
**Decision:** For the specific nonzero Stage 2B parity comparator, classify the full real formal centralizer of its full return, all complement lifts over the fixed register, and all normalized autonomous product roots. Every formal product reduction exchanges the two complement fibre-action types on each orbit; opposite types admit a constructive nonlinear formal reduction, with a parity-dependent nontrivial source lift or a fixed nontrivial target action. A nontrivial source action independent of the register is possible and unique through degree q, but impossible through degree q+1 in the original common fibre trivialization. These are mathematical classification results in a specified model and category, not a physical choice of complement, fibre, observation law or clock.

## 1. Source and evidence boundary

Main checkpoint 136d1c5954bdb3d031cdc19ddb9fac3096a67b58. CONVENTIONS.md read in full; no pending OFN PR at entry. Stage 2C #420 merged at 28df49fe29695b62152b5e3014eb8d03d9f1cb2b, final head 2d6bd1f7e1f4e63434c495647aeabca652b927ef; #422 review merged at 136d1c5954bdb3d031cdc19ddb9fac3096a67b58. Read Stage 2C §§2–7 and the full independent review, especially the centralizer lemma and N1–N3. Stage 2C record blob 0ccae599949696682893153582ac2e6db2d12ecb; independent review blob eda7a9ecd67c250a99a472644009cbaeb31fab0c at reviewer head 5a7200a0be1f37841471e6a9f2ad7d1d283ebcfc. The reviewer approved the original #420 head f256abc8952c635ec911596c8f833644e8a78ff9; the subsequent N2 clarification distinguishes source and target actions. PI authorized the two archival merges; no separate reviewer approval of the N2 clarification is inferred. This record rederives the covariance equations and proves the nonlinear result independently of the review's proposed N2 expression. Stage 2B #413 (blob 2b7277dcc9b0b223e7a02a7e058b0635787ce891), §§2, 4–6: fixed comparator, not a selected generator. Binary Recognition #183, wrap-up §2: fixed register and native readout identities. Earlier results remain SESSION.

Governing owner and discipline sources, targeted reading at the actual tags and release/adoption records; recorded SHA-256 values are from the tag/BASELINE/release identities, not fresh full-file byte hashing in this session:
- RECOG v0.3.27, tag recog-v0.3.27, target 7bad433b1cea32c34c4c24f24c26b895998e735d, SHA-256 19556f913f51b98599faa6ad88c363dda0a278345677f3bd69f3b892d810e1f1, §6.10 RECOG-ALG-NU3-CLOSED-FORM and RECOG-ALG-LEADING-RETURN-EQUIVARIANCE; release records/recog/RECOG_v0_3_27_RELEASE_RECORD.md.
- DYAD v6.4.24, tag dyad-v6.4.24, target f0af6392ed560b55aedc640bc166f0b87f612f7c, SHA-256 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16, §6.9 DYAD-ALG-KP-FRAME-SCALE and DYAD-ALG-BRIDGE-LEMMA; §6.16 DYAD-THM-FORMAL-CENTRALIZER, DYAD-THM-FORMAL-INVOLUTION-UNIQUE and DYAD-THM-FORMAL-Z6-GENERATOR (method precedent, six-step owner map, NOT the new parity comparator). Release records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md. The proof below uses the Stage 2C comparator's own cubic and centralizer bound, not a transfer of the owner six-step theorem, analytic status or smooth embedding.
- OFN v0.13, tag ofn-v0.13, target 3f266eb4337c10d6e88a0ea90527dbe732922319, SHA-256 4a2d266bf89cd2130e901b7543bacbaf7fa3e844c60e355a2e3c23ef4f075a49; §0.5 guards STATE/PRESENTATION/SELECTION/TIME, §1.2 RTG-OFN-DEF-PRESENTATION-COVARIANCE, §4.1 RTG-OFN-DEF-STATE-COMPLETENESS. Release records/ofn/OFN_v0_13_RELEASE_RECORD.md.
- RRF v0.8.4, tag rrf-v0.8.4, target d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d, SHA-256 2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce, §§4.1–4.2a typed action/observable and orientation non-transfer discipline. Separate adoption record at current main records/rrf/RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_ADOPTION_RECORD.md (not present at the tag): working representation standard only. The pending RRF successor is not taken as governing. No RRF profile is registered here.
- Methodology v1.4, tag methodology-v1.4, target 72d8a838db04f249bbb93a0930804e9ec8b9d289; §12.2 evidence states, repository CONVENTIONS §§5–6,9. Release records/methodology/DSN_METHODOLOGY_v1.4_RELEASE_RECORD.md.

EV-SRC-READ: the named passages and adoption identities, not full owner-proof audits. EV-NOT-RERUN: prior owner and Stage 2C campaigns. The new native checker is described in §7. No novelty claim; LIT dependencies: none. No use of DZT norm law as a centralizer premise.

## 2. Presentation contract for this calculation

[DEF] [SESSION] Retain the Stage 2B analytic comparator as given, not a newly chosen mechanism. Set p=4s>=12, n=p/2=hm, h=2^{v_2(n)}, m odd, q=n-1>=5, epsilon a nonzero real scalar, L=zeta_p, K=2-L-L^{-1}. The full state is (X,z) with X in the complete binary register X_n and z=(rho,eta) a separately specified continuous fibre. F_n is the twisted register shift, C_n=F_n^n is complement, sigma(X)=(-1)^{pi_n(X)}. Thus sigma(F_n X)=-sigma(X), sigma(C_n X)=sigma(X). The primitive simultaneous update is
$$\mathcal T(X,z)=(F_n X,f_{\sigma(X)}z),\qquad
f_\sigma(\rho,\eta)=(\rho-\sin\eta,\eta+K(e^\rho-1+\epsilon\sigma\rho^q-\sin\eta)).$$
Use the common raw W frame W=rho+(L-1)eta/K, V=conjugate(W), with linear rotation R. All compositions are right to left. A=f_- o f_+, P=A^n, B=A^h. These maps fix the origin and have invertible linear parts. The event/step index is formal; no physical duration is calibrated.

The chart class tested is base-preserving, origin-preserving, real formal invertible fibre maps H_X, preserving one primitive update, with no additional variables or base reassignment. A product target has one autonomous g and the same F_n. A formal complement lift is
$$\widehat C(X,z)=(C_n X,\kappa_X(z)),\quad \widehat C^2=id,\quad
\widehat C\mathcal T=\mathcal T\widehat C.$$
Equivalently kappa_{C_n X} o kappa_X=id and kappa_{F_n X} o f_{sigma(X)}=f_{sigma(X)} o kappa_X. Initially kappa_X is a map between the two origin-marked fibres, not assumed to be an involution in the common trivialization or independent of X. A covariant conjugacy to a target lift theta_X obeys H_{C_n X} o kappa_X=theta_X o H_X. Source and target lift actions are not silently identified. These are mathematical conditions for a candidate quotient; physical admissibility also needs observables (§6). Statements about finite jets are separately marked. Infinite formal series are not asserted convergent.

## 3. Complete formal centralizer of the comparator return

[THM] [SESSION] Write script X=log P for the real formal iterative logarithm, P^t=exp(t script X) for real t, and J=A o P^{-1/n}. Then J^n=id and DJ(0)=R^2 of exact order n. The full origin-preserving real formal centralizer is
$$\operatorname{Cent}_{\rm form}(P)=\{J^j\circ P^t:j\in\mathbb Z/n\mathbb Z,\ t\in\mathbb R\}
\simeq\mathbb Z_n\times(\mathbb R,+).$$
In particular this group is abelian. For every positive integer ell dividing n, the formal centralizer of A^ell is the same group.

Proof. Stage 2C §§3–4 establishes, in the common W frame and after a common tangent-to-identity normalizer where needed, P=id+X_3+... with no quadratic term, X_3(W)=mu W|W|^2, mu=a_0+i b_0, a_0<0, b_0<0. It also proves that every invertible real q-jet commuting with P has derivative a rotation omega with omega^n=1. The latter uses the nonzero degree-q charge -n term of this comparator and both cubic premises, not just the presence of a resonant linear rotation. The bound therefore applies to the truncation of any formal centralizer element.

For a tangent-identity centralizer G, if G!=id, let H_d be its first nonzero homogeneous correction (d>=2). At degree d+2 of G P=P G one gets [X_3,H_d]=0. In polar coordinates H_d has components r^d U(phi), r^{d-1} V(phi). The bracket's Fourier-mode equations are
$$((d-3)a_0+ik b_0)U_k=0,\qquad
((d-1)a_0+ik b_0)V_k-2b_0 U_k=0.$$
For k!=0 the two diagonal coefficients are nonzero because b_0!=0. For k=0 and d>=2, the second diagonal coefficient is nonzero because a_0!=0; the first can vanish only at d=3. At d=3, V_0=(b_0/a_0)U_0, so the real polynomial kernel is exactly the one-dimensional span of X_3. Thus any nonidentity tangent-identity centralizer first differs from id at degree 3, by t X_3 for some real t. P^t commutes with P and has that same leading term. G o P^{-t} commutes with P and is tangent to id with zero terms through degree 3; it must be id by the same lowest-degree argument. Conversely every P^t is a centralizer element, and t is unique because X_3!=0. This is an all-orders argument, not a classification of all centralizer elements of a finite q-jet (the latter can have extra terminal-degree freedoms).

A commutes with P and hence with every P^t (commutation with the formal substitution logarithm). Therefore J^n=A^n P^{-1}=id; its linear part has order n. Every centralizer derivative is a power of R^2 by the Stage 2C bound. Composing with the inverse of the corresponding J^j gives a tangent-identity centralizer, now proved to be P^t. Each J^j commutes with the flow. Distinct j have distinct linear parts and the flow parameter is unique. This proves the direct product. A=J P^{1/n} belongs to this abelian group. If ell|n, a map commuting with A^ell commutes with P=(A^ell)^{n/ell}; conversely every element of Cent(P) commutes with A and hence A^ell. QED.

[ALG] [SESSION] The only elements of Cent(P) whose square is id are id and
$$\mathcal K=J^{n/2}=A^{n/2}\circ P^{-1/2},\quad D\mathcal K(0)=-I.$$
Indeed the flow parameter must vanish, and 2j=0 mod n. This is a uniquely determined nonidentity formal involution of this return, not the raw linear half-turn or a physical pole-exchange operation. The notation K (real shear coefficient) and calligraphic K (involution) are distinct.

## 4. Classification of complement lifts and product targets

[THM] [SESSION] Stage 2C §2 gives orbit periods d=2h k=2ell, k|m odd, ell=h k even, with F_n^ell X=C_n X; a shortest orbit d=2h exists. At a positive-parity orbit start X let D=A^{ell/2} be the half-return fibre transport and M=A^ell=D^2 the monodromy. Every formal complement lift in §2 is determined on each orbit by one independent bit e in {0,1}:
$$\kappa_X=
\begin{cases}
\mathcal K^e,&\sigma(X)=+1,\\
f_+\mathcal K^e f_+^{-1},&\sigma(X)=-1.
\end{cases}$$
The bit is constant along that orbit. Conversely any assignment of these bits to the finite register orbits gives a formal lift. The subclass of parity-only lifts has exactly two members (all bits zero or all bits one).

Proof. Let U_j be the prefix fibre transport from the chosen start after j steps. Since sigma(C_n X)=sigma(X) and C_n commutes with F_n, the same prefix acts from C_n X. Covariance forces kappa_{F_n^j X}=U_j kappa_X U_j^{-1}. At j=d this gives kappa_X M=M kappa_X. By §3 this is the abelian Cent(P), so kappa_X also commutes with D. At j=ell, kappa_{C_n X}=D kappa_X D^{-1}=kappa_X; the involution condition now gives kappa_X^2=id. Hence the only choices at a positive start are id and calligraphic K. They propagate to the displayed formula, since every pair of steps on that orbit is A. Both choices commute with A and square to id; the negative-parity transport is conjugate to the positive action. Directly, f_- (f_+ calligraphic K f_+^{-1})=calligraphic K f_- because A commutes with calligraphic K, and the other covariance relation is by definition. The complement-invariance of parity and the constancy of the bit give the required square. This proves necessity and sufficiency. It does not count a formal lift as an exact smooth/analytic symmetry.

[THM] [SESSION] By the Stage 2C shortest-orbit root criterion, a product conjugacy normalized by H_X=id at one shortest positive-parity start has g^{2h}=B. Conversely every such root supplies a formal product conjugacy. All roots in this normalization are
$$g_j=J^j P^{1/p},\qquad 2j\equiv1\pmod m,\qquad j\in\mathbb Z/n\mathbb Z.$$
There are h such roots, including the case m=1 (every j). Proof: every root commutes with B, hence with P=B^m, so is J^j P^t by §3. Raising to 2h and comparing with B=J^h P^{h/n} gives 2h t=h/n and 2h j=h mod n. Since m is odd, 2 is invertible modulo m, giving exactly h j classes. This sharpens Stage 2C's existence construction; the count is of normalized g germs, not a count of all H_X. On other positive-parity orbit starts g^{2ell}=A^ell by the root condition, and any product chart there must commute with A^ell. One may choose H_X=id at every such start for construction. Propagate by H_{F_n X}=g H_X f_{sigma(X)}^{-1}; the monodromy identity closes each orbit.

[THM] [SESSION] For every such normalized root and each orbit half-length ell=h k,
$$g_j^\ell=\mathcal K\,D,\qquad D=A^{\ell/2}.$$
Indeed the flow powers match, and the ratio of finite rotations is J^{ell(2j-1)/2}. Since 2j-1 is an odd multiple of m and k is odd, this exponent is n/2 modulo n. Thus the ratio is calligraphic K, not id.

Every formal product conjugacy, after the common normalization above, transports the source lift bit e on each orbit to the opposite target bit 1-e:
$$\theta_X=\mathcal K^{1-e}\quad\hbox{for every X on that orbit in the normalized target.}$$
At a positive start, H_{C_n X}=g^ell H_X D^{-1}=calligraphic K H_X because H_X commutes with M and hence D, by §3. The source action there is calligraphic K^e and H_X commutes with it. Consequently theta_X=H_{C_n X} kappa_X H_X^{-1}=calligraphic K^{1+e}; exponents are modulo two. Target covariance propagates theta_X by conjugation with g, but calligraphic K commutes with g, so the target action is constant along the orbit. This applies to every formal reduction in the class, not just the constructed choice of H_X. Conversely choose a root and the orbit-wise charts just constructed. They give a covariant product reduction with exactly these opposite lifts.

Consequences for uniform lift types:
- Trivial source and trivial target: impossible.
- Nontrivial parity-dependent source and nontrivial target: impossible when both actions are to be preserved with their derivative type.
- Trivial source and fixed nontrivial target action calligraphic K: possible formally.
- Nontrivial parity-dependent source and trivial target: possible formally.

More generally the flip of e is necessary and sufficient orbit by orbit when base-dependent target actions are permitted. Same-type nonreduction also holds at q-jet order: at a positive start normalized to identity, the n-step covariance equation yields S^n=-K_t K_s^{-1}, whereas Stage 2C forces S^n=I for the target derivative S; K_s,K_t are the source and transported target scalar derivative signs. Equal signs contradict this. Opposite-type formal constructions give compatible finite-jet representatives at every order. A formal change of presentation may move an explicit parity dependence from the update into the complement action or an observable; it does not by itself remove physical relational content. Exact analytic/smooth realization of these roots or of the nontrivial lift is not proved.

## 5. Fixed nontrivial source involution: exact first failure at q+1

[THM] [SESSION] For the raw common fibre trivialization of the Stage 2B comparator, there is exactly one nonidentity q-jet involution common to f_+ and f_- (commuting with both through degree q). There is no nonidentity origin-preserving (q+1)-jet involution commuting with both. Consequently no nonidentity C^{q+1} exact local involution independent of X can define a complement lift for the complete comparator. The boundary is for a common action, not the parity-dependent lifts of §4.

Existence through q. In the common tangent-to-identity owner normalizing chart of Stage 2C §3 the owner map is rotation-equivariant through q<p-1, hence odd through q; the comparator perturbation starts at the odd degree q, and its homogeneous difference from the owner is unchanged by this common chart. Thus both comparator q-jets are odd, and the linear half-turn in this chart is a common involution. Pull it back to the raw common coordinates. Any common q-jet involution commutes with P, so its derivative is +/-I by Stage 2C and involutivity. An identity-derivative involution is the identity in the finite jet group (its first nonzero correction would double upon squaring). In the normalized chart, a -I-derivative involution differing from -I first at degree d must have d even: the square at that degree is ((-1)^d-1)H_d. Commutation with f_+ then requires H_d(Rz)=RH_d(z). Every degree-even monomial has odd charge u-v-1, which cannot be divisible by p (p even). Hence no such first difference through q. This proves uniqueness.

Failure at q+1, in raw (rho,eta). Let kappa=-id+H_2+... with H_2 a real homogeneous quadratic pair. The common primitive linear matrix and quadratic jet are
$$R_{\rm raw}=\begin{pmatrix}1&-1\\ K&1-K\end{pmatrix},\qquad
F_2=(0,K\rho^2/2).$$
Commutation with either f_sigma through degree 2 forces
$$H_2(R_{\rm raw} z)-R_{\rm raw} H_2(z)=(0,K\rho^2).$$
For H_{2,1}=a rho^2+b rho eta+c eta^2, H_{2,2}=d rho^2+e rho eta+f eta^2, order the six coefficient equations by (rho^2,rho eta,eta^2) in the first and then second component. Their determinant is K^3(K-3)^2. Since 0<K<=2-sqrt(3), it is nonzero. Solving gives in particular
$$H_{2,1}=\frac{-K^2+2K+1}{K-3}\rho^2+
\frac{2(K-2)}{K-3}\rho\eta-\frac{K-2}{K(K-3)}\eta^2,$$
and
$$K\partial_\eta H_{2,1}(R_{\rm raw} z)=-\frac{2(K-2)}{K-3}\eta.$$
Both the equation and these rational identities are checked symbolically in the new checker.

Subtract the commutators kappa f_+ - f_+ kappa and kappa f_- - f_- kappa. Since f_+-f_-=(0,2 epsilon K rho^q) exactly, their difference in the first component receives no contribution from (f_+-f_-) o kappa. The linear term of kappa gives zero first-component difference; at degree q+1 the only possible contribution is the derivative of H_{2,1} at R_raw z on (0,2 epsilon K rho^q). Higher terms of kappa or nonlinear terms of the common input in this derivative contribute at degree >=q+2. The forced first-component residual is therefore
$$-\frac{4\epsilon(K-2)}{K-3}\rho^q\eta\ne0.$$
No higher chart coefficient can compensate at this order. Contradiction to a common (q+1)-jet. Any common involution through q+1 with derivative +I is the identity jet, as above. If an exact origin-preserving C^{q+1} involution has derivative +I, the local chart z->(z+kappa(z))/2 has invertible derivative I and is invariant under kappa, so kappa is the identity germ. Thus the exact C^{q+1} common-action no-go follows as well; no general analytic nonexistence of base-dependent lifts follows.

[THM] [SESSION] The unique nontrivial formal positive and negative parity actions in §4 have identical jets through q and first differ at q+1. To see equality, use the same common normalizing chart as above: A is odd through q with derivative R^2 (order n even). The -I-derivative formal involution calligraphic K commutes with A. The same lowest-difference argument using R^2 excludes every even-degree correction through q in this chart (odd charge cannot vanish mod even n); it therefore equals -I through q. Its negative-parity conjugate by the odd f_+ q-jet has the same q-jet. If their (q+1)-jets agreed, covariance in §4 would make that one jet a common nontrivial involution of both f_+,f_-, contradicting the residual above. The split occurs at exactly q+1, also in the raw common chart since common diffeomorphic transport preserves the order of a first difference. This explains why a common half-turn looks sufficient at the very order detecting the Stage 2B resonance, yet fails at the next order. The result depends on nonzero epsilon and the specific quadratic/shear structure; it does not classify common actions of arbitrary parity-gated families.

## 6. Conditional observation/presentation contract and next research gate

[ALG] [SESSION] In the fixed register model the native sign is C-even at even n, while the character Z_n obeys Z_n C_n=-Z_n. Both are base-only observations. Either complement lift bit gives these same laws, so neither observation determines the derivative sign of the independently postulated continuous fibre action. There is no map identifying the fibre with the register character.

A possible discriminating contract is a fibre-only observation O(z) (real scalar/vector, C^1 at 0, D O(0)!=0) with specified scalar complement type tau in {+1,-1}, satisfying O(kappa_X z)=tau O(z) in its stated domain (or at first-jet level). Since the classified fibre derivatives are scalar signs, differentiation forces D kappa_X(0)=tau I. Requiring the same type for such an observation in both presentations, with observations fibre-only and nonzero linear response in both, therefore excludes a product reduction by §4. This is a conditional sufficient restriction on the presentation contract, not a derived physical observable. In particular a quadratic gauge-invariant norm with zero derivative at the origin need not fix the sign; and transporting an observation as O_t(X,w)=O_s(H_X^{-1}w) can make it depend on X even with autonomous update. Those possibilities are not ruled out by this contract. The full state and typed covariance must be specified, not replaced by a norm or parity scalar.

Research disposition:
- [THM] The mathematical formal complement-lift classification and opposite-action product construction are complete for this fixed comparator and the declared base-preserving category. The common-action boundary is proved at q+1. Neither result is a physical gauge selection or a claim about all finite-jet centralizer kernels.
- [OPEN] Independent relational justification of a presentation class and observable algebra: whether complement has a physical role, what its fibre action is, and whether independent information requires a fibre-only observation of the same type or an equivalent restriction. Neither select equal signs to force irreducibility nor opposite signs to force reducibility. RRF OPEN-A and OFN OPEN-OPA remain distinct from this result.
- [OPEN] Exact smooth/analytic realization of the nontrivial lift and product roots of the selected comparator; not required for the formal/finite-jet result.
- [OPEN] Intrinsic composition: derive a nonlinear rule from an admissible carrier and readout without postulating a continuous fibre and the term epsilon sigma rho^q. Under unrestricted full-register formal charts, a parity-only gate with common R^p=id cannot suffice; richer orbit-dependent monodromy, a nonperiodic base or an independently justified readout restriction are possible next routes. None has been selected or derived here. The chosen q(p), epsilon, event rule and physical clock are still open.

## 7. Evidence and independent review request

EV-CODE / EV-RUN / EV-COVER: Native Python/SymPy 1.14.0 in the ChatGPT execution container, isolated invocation from /tmp, exit 0. The checker is newly written for this stage and does not import earlier scripts. It uses symbolic rational identities, integer congruences, and full sparse bivariate Taylor arithmetic in the exact real algebraic field Q(2 cos(2pi/p)). The finite fractional iterate is evaluated via the nilpotent substitution difference Delta: on coordinate polynomials P^t = sum binom(t,k) Delta^k(id), Delta(f)=f o P-f; no convergence is inferred. This provides a second mathematical extraction method relative to the prior pure-V tests, not a new independent co-owner review or an owner certificate replay.

- Symbolic solve of the quadratic commutation equations and first-component residual identity.
- p=12,16,...,256: 62/62 root-count congruence horizons, 878 root/possible orbit-half-length pairs (all j satisfying the congruence and each divisor k of m). The arithmetic includes the half-return square-root congruence 2j=ell mod n; it does not prove the nonlinear centralizer.
- p=12 at order 6 and p=16 at order 8, epsilon=1/7: exact full bivariate raw jets, P quadratic jet vanishes; one representative g root per horizon, J^n=id, both parity-specific involutions, their covariance with both maps, negative derivative of the positive-parity action, first parity-action split at q+1, commutation of target action with g, full root and opposite-action half-return identities at every allowed orbit half-length in these two examples. These are finite exact regression tests of the explicit constructions and include a power-of-two p. The all-p centralizer, lift classification, root count and no-go are written proofs, not extrapolation from these tests.
- No separate physical model, certificate or prior owner engine run.

Intake: upload/ofn-strobe-boundary-stage2d-20261127 at 8ebbb99c5a39a2b8a754280cb6a0dfa03687912b. Native SHA-256 and Git blob hashes computed on the executed bytes before upload; readback matches the native blob identities and intake content, placed by reusing exactly those blobs.

| File under evidence/ofn/intrinsic_strobe_boundary/ | SHA-256 |
|---|---|
| scripts/strobe_boundary_stage2d_check.py | be0950006f46d943c720cad0541418ecaec480a9ce6b3696058db65244eb0606 |
| runs/strobe_boundary_stage2d_output.txt | 2495b5176b692a4da20f59e21c50923b6ba2d624183d9c27262184ce24e248f4 |

Reproduce from a repository checkout or from an isolated temporary directory using the absolute path: python3 -I evidence/ofn/intrinsic_strobe_boundary/scripts/strobe_boundary_stage2d_check.py

Requested independent review: (1) source and evidence identities, inspect and replay checker byte-identically; (2) prove/check the zero-mode centralizer kernel, all-orders tangent-identity argument and finite rotation bound (do not infer complete finite-jet centralizer from this); (3) review all-orbit lift classification, normalized root count, opposite-type necessity/sufficiency including m=1, and the source/target normalization; (4) independently verify the quadratic homological equation and the q+1 residual with no higher-order cancellation, the uniqueness through q and first parity split; (5) assess the finite-jet implementation, and if feasible perform independent bivariate or symbolic checks; (6) check the readout restriction is conditional, not a chosen physical gauge. No new scientific RID or DSN edition is requested. PI decides archival merge and subsequent scope.

*END OF STAGE 2D SESSION RECORD.*
