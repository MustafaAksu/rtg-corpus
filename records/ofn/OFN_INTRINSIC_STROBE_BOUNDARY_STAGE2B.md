# Intrinsic strobe-boundary structure — Stage 2B: alternating cubic compensation and first parity resonance

**Date:** 26 November 2026.
**Status:** SESSION / NONCANONICAL; independently reviewed at the original head (review PR #415); N1–N3 scope and provenance notes incorporated. PI archival merge decision pending. No owner RID, canonical adoption, physical selection, or closure of the common-mechanism question.
**Decision:** In the parity-only skew-product model, all alternating terms through cubic order can be removed by finite-jet fibre charts. The first possible alternating homological resonance is degree q=p/2-1. An explicit recognition-gated shear at that degree preserves every lower owner jet, has a nonzero raw quarter-strobe contrast, and is not reducible to an autonomous product by origin-preserving parity-only fibre diffeomorphisms. This is an existence result in a deliberately enlarged model class, not a derivation of a physical coupling.

## 1. Source, dependency and scope

- Stage 1, PR #403 merged at 14b46849791087cb264685bd5d70edd383c6cc41, record SHA-256 3a7b6e59bec9028f518d7fd9b17e5c146e189a859d59ecb07caa18744baa310f; review #407. Inspected §§2–5 and the R1–R2 full component inventory and 2-local CRT. The signed-history algebra alone gives no interaction between distinct parity and primitive factors.
- Stage 2A, PR #411, originally read while unmerged at `496aafbe0113e422b7f538b71efa6be8f127e6f3`, record SHA-256 `ef9020071a7ca3a9b1687d5fb55a5e4d9a7113d4aed6d6e6155fb19206a5c5f9`. Full record read, especially §§2–6. The original scientific pin is retained. Claude's independent APPROVE is recorded in #415; the R1 wording/provenance revision at `6a332020a029d0a5988039846fb4cbc693fc05f2` has SHA-256 `7d6f54dc3515f264bf74ed5dd0a3c24e0193e9b8f42601a16ca58d3bfa1fd6c2` and changes no formula or proof hypothesis. Both are SESSION records, not an owner result. The extension below is also derived from direct finite path sums. Stage 2B is a separate branch from main. Merge #411 before #413 to retain the reviewed dependency in main history; no merge of #411 is claimed by this note.
- DYAD v6.4.24, tag dyad-v6.4.24, DSN SHA-256 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16, §§6.9, 6.11, DYAD-THM-Q403-PHASELAW: owner raw W_p frame and rotation-removed cubic channel at s=p/4.
- DZT v0.19, tag dzt-v0.19, DSN SHA-256 2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce, §6.3, DZT-THM-CASCADE-NORM-LAW with inherited DYAD premise.
- OFN v0.13, tag ofn-v0.13, DSN SHA-256 4a2d266bf89cd2130e901b7543bacbaf7fa3e844c60e355a2e3c23ef4f075a49, SG-OFN-STATE, PRESENTATION, SELECTION, TIME, INFORMATION and state-completeness contract.
- Binary Recognition and Gaussian boundary models are used at the fixed definitions and proof scopes in Stage 1 and Stage 2A. No claim to re-own their results.

EV-SRC-READ / EV-HASH: governing tagged editions and adoption records checked against retrieved owner bytes; targeted source reading, not a full owner-proof audit. CONVENTIONS.md read. No original owner extractor/certificate replay. No mathematical novelty claim.

## 2. Carrier, actual parity factor and the diagnostic model class

[DEF] [SESSION] Let p=4s>=12, n=2s, L=zeta_p, I=L^s=i, K_p=2-L-L^{-1}. Let X_n=F_2^n carry the fixed twisted register F_n. Write sigma(X)=(-1)^{pi_n(X)}. Then sigma(F_n X)=-sigma(X). Keep the **full register**, including every intermediate cyclotomic factor, and the independent continuous fibre z=(rho,eta) in R^2. The clock is one simultaneous formal update. The common raw coordinate is W=rho+(L-1)eta/K_p with V=conjugate(W); rotation R(W,V)=(LW,L^{-1}V). The class of models is
$$\mathcal T(X,z)=(F_nX,T_{\sigma(X)}z),\quad
T_\sigma(\rho,\eta)=(\rho-S_\sigma(\eta),\ \eta+K_p(G_\sigma(\rho)-S_\sigma(\eta))).$$
This one-way observation law is imposed explicitly; no feedback or physical recognition event is asserted. The continuous fibre is not identified with the cyclotomic readout of X. The autonomous owner null uses G=e^rho-1 and S=sin(eta). Each map fixes the fibre origin, with common invertible linear part R.

[THM] [SESSION] Put s=2^a m, m odd, alpha=a+2. By Stage 1, the mod-2 history carrier M has factors indexed by d|m, namely F_2[t]/(overline Phi_d^{2^{alpha-1}}). Native parity is evaluation at t=1 on the d=1 factor. No factors are discarded in the present model. For m>1 the primitive factor d=m is distinct: the binary vectors with polynomials 0 and overline Phi_p have the same primitive mod-2 residue, opposite native parity, and degree <n because phi(p)<n. Thus a nonzero sigma-dependent coefficient accesses information not determined by that primitive residue. This proves a distinction of inputs, not a map from the primitive residue to z. For m=1 the factors coincide; the parity-gate calculation still applies but cannot be interpreted as an interaction between distinct CRT factors. Mod-2 collision is not asserted to be a characteristic-zero collision of the complex phase readout.

## 3. Alternating cubic source: exact recovery/compensation classification

[THM] [SESSION] In the Stage 2A shear model allow the cubic coefficients to alternate as well:
$$G_\sigma(\rho)=\rho+(a+\sigma d)\rho^2+(b+\sigma\beta)\rho^3+O(\rho^4),$$
$$S_\sigma(\eta)=\eta+(\gamma+\sigma\delta)\eta^3+O(\eta^4).$$
The six scalar parameters are real; the sine-like source still has no quadratic term. Here d denotes the scalar gate contrast rather than a cyclotomic divisor. Write Q0 for the nonzero owner cubic (0,3) coefficient and r_p,c_p for the Stage 2A path-weight ratios. Then the cubic channel of the s-step fibre return with L^s removed is
$$Q^\sigma=4Q0(a^2+r_p d^2)+\sigma(4Q0c_p ad+J_s\chi),$$
$$J_s=\sum_{j=0}^{s-1}(-1)^j L^{-4j}=\frac{1-(-1)^s}{1+L^{-4}},\qquad
\chi=\frac{(L-1)L^2}{(1+L)^3}\left(\beta+\frac{K_p}{L}\delta\right).$$

Proof: the pure V^3 term of the rotation-removed one-step W map has a contribution (L-1)b rho^3/L-gamma eta^3. Substituting rho=L V/(1+L), eta=(L-1)V/(1+L) at W=0 gives the coefficient of the alternating source as displayed, using K_p=-(L-1)^2/L. Its ordinary charge is -4, the extra alternating sign contributes (-1)^j, and the common direct cubic term cancels since L^{-4} has exact order s. The degree-three two-insertion contributions are unchanged by the new cubic terms. Explicitly put x=L^{-1},
$$w_{jk}=x^{3j+k}-L^2x^{j+3k},\quad
A=\sum_{j<k}w_{jk},\quad B=\sum_{j<k}(-1)^{j+k}w_{jk},\quad
C=\sum_{j<k}(({-1})^j+({-1})^k)w_{jk}.$$
The quadratic sources enter as (a+sigma d(-1)^j)(a+sigma d(-1)^k). Their unit-source prefactor B_1 C_1 is the #398/Stage 2A raw-frame path prefactor, where A_1=(L-1)/(L(1+L)^2), B_1=2LA_1, C_1=L^2 A_1; the second path coefficient is -L^2 B_1 C_1. Thus r_p=B/A and c_p=C/A, and B_1 C_1 A/4=Q0. This proves the extension directly. The geometric collapse in pinned Stage 2A §3 gives c_p nonzero for all p>=12; in particular, its odd-s numerator has the nonvanishing factors (x+i)^2(x^2-i x-1), and its even-s numerator has (1+i)(x^2+1)(x^2+i). The same ratios are evaluated by direct finite summation in the present test, not imported executable code.

Since p>=12, 1+L^{-4}!=0. Therefore J_s=0 iff s even. Also K_p/L has nonzero imaginary part, and (L-1)L^2/(1+L)^3!=0. The real-linear map (beta,delta)->chi is bijective onto C.

Both-parity recovery Q^+=Q^-=Q0 is **equivalent** to
$$a^2+r_p d^2=1/4,\qquad 4Q0c_p ad+J_s\chi=0.$$
For even s, the alternating direct term cancels independently of (beta,delta); the quadratic recovery conditions are those of Stage 2A (ad=0 and, since r_p<0, only the constant a=+/-1/2,d=0). For odd s the second equality uniquely specifies the two real cubic contrasts for each a,d satisfying the first. In particular mixed quadratic gates can match Q0 by nonzero compensating direct cubic sources, not by the original cancellation mechanism. The odd-s mixed branch exists over the reals: r_p>0 by the ratio formula in Stage 2A §4, and for any sufficiently small nonzero real t the conic parametrization a=(1-r_p t^2)/(2(1+r_p t^2)), d=t/(1+r_p t^2) has a d!=0. If these parameters are in K^+=Q(L)^+, the compensator can be computed in K^+ by complex conjugation: with y=-4Q0c_p ad/(J_s chi_b), chi_b=(L-1)L^2/(1+L)^3 and kappa=K_p/L, set delta=(y-conjugate(y))/(kappa-conjugate(kappa)), beta=y-kappa delta.

If direct alternating cubic cancellation is required separately, J_s chi=0 and the mixed branch is excluded by c_p!=0. For odd s this also forces beta=delta=0. Matching a single coefficient for both initial signs necessarily erases contrast in that channel; the proposed compensation is not an intrinsic selection rule and does not establish full nonlinear equivalence. No general rational-parameter classification for compensators is asserted.

## 4. First parity homological resonance (fixed parity-dependent chart class)

[THM] [SESSION] Consider any real C^k fibre family f_sigma fixing the origin with common linear rotation R, above the fixed alternating sign. A parity-dependent origin-preserving fibre chart is a map H(X,z)=(X,H_{sigma(X)}(z)), with H_+,H_- local real diffeomorphisms fixing zero. For finite-jet normalization first take them tangent to identity. At a homogeneous degree k a change H_sigma=id+sigma h_k changes the alternating part P_k of the W-component, at that degree, by
$$P_k(W,V)\longmapsto P_k(W,V)-h_k(LW,L^{-1}V)-L h_k(W,V).$$
The other component is the real conjugate. Indeed the new fibre map is H_{-sigma} f_sigma H_sigma^{-1}; lower-degree terms are unchanged. The corresponding alternating homological multiplier on W^u V^v, u+v=k, is L^{u-v}+L. Its kernel is characterized by
$$u-v-1\equiv p/2\pmod p.$$
As the charge lies in [-k-1,k-1], no alternating resonance occurs for 2<=k<p/2-1. At
$$q=p/2-1=2s-1$$
the only alternating W-channel resonance of that degree is u=0,v=q (charge -p/2). The conjugate V channel follows by reality. An equivalent joint-clock statement is that sigma V^q transforms under (sigma,W,V)->(-sigma,LW,L^{-1}V) with eigenvalue L, exactly the W output character. At every even degree the alternating homological multiplier is nonzero since the charge is odd and p/2 is even.

Consequently all alternating terms through any order k<q can be removed successively by tangent-to-identity parity-dependent charts, leaving a common autonomous k-jet. This allows the common jet to change. In particular all quadratic and cubic gates in §§2–3 are reducible through cubic order in this sense, not necessarily to the **owner** cubic jet or to an autonomous full map. At degree q a general candidate must be checked after lower-order normalization; a nonzero raw alternating coefficient in an arbitrary unnormalized model is not automatically a conjugacy obstruction.

**N1 (standard resonance framing).** This is the period-two (Floquet-type) homological resonance condition: the alternating character is -1=L^{p/2}. The threshold follows by multiplying that character with the input monomial character and comparing with the W output character. No new general resonance theory is claimed.

## 5. Untuned higher-order comparator with an actual obstruction in this chart class

[THM] [SESSION] Choose the explicit analytic fibre maps
$$G_\sigma(\rho)=e^\rho-1+\epsilon\sigma\rho^q,\qquad
S_\sigma(\eta)=\sin\eta,\qquad q=2s-1,\quad \epsilon\in\mathbb R\setminus\{0\}.$$
All one-step and finite-return jets through degree q-1 agree with the owner in the fixed raw coordinate, since the first modification is at degree q>=5. In particular the actual cubic coefficient Q0, not merely its norm, is unchanged for both signs. There is no adjustment of lower Taylor coefficients; any fixed nonzero epsilon (including a rational value independent of p) is allowed, although the chosen monomial degree depends on p.

The normalized one-step alternating V^q coefficient is epsilon times
$$\kappa_{p,q}=\frac{(L-1)L^{q-1}}{(1+L)^q}\ne0.$$
To verify it, the W raw map receives sigma epsilon (L-1) rho^q; divide by L and set W=0. Under iteration, a first difference at degree q can only compose with the linear terms at that degree: insertion into any lower nonlinear term of degree >=2, or the effect of a lower nonlinear term inside the new degree-q source, has degree >=q+1. For ell formal steps the difference in the rotation-removed V^q coefficient is therefore
$$\sigma\epsilon\kappa_{p,q}\sum_{j=0}^{\ell-1}(-1)^j L^{-(q+1)j}
=\ell\sigma\epsilon\kappa_{p,q}.$$
For ell=s the initial-parity contrast is 2s epsilon kappa_{p,q}!=0. The quantity here is a new degree-q raw channel, not a replacement of the owner cubic Q0 or an adopted DYAD higher-order invariant.

**No parity-only product reduction, including a changed autonomous linear rotation.** Suppose origin-preserving C^q charts H_+,H_- conjugate the above skew product to (F_n X,g(w)) with one common local C^q map g fixing zero. Let A_sigma=DH_sigma(0), S=Dg(0). The linear equations are A_- R=S A_+, A_+ R=S A_-. Conjugate the target by the common real matrix A_+^{-1}. Then A_+=Id and S^2=R^2. Since R^2 is a nonreal planar rotation for p>=12, its real matrix centralizer consists of complex scalar multiplications. S commutes with R^2, so S=+R or -R; correspondingly A_-=+Id or -Id.

Case S=R: both charts are tangent to identity. The source jets below q are independent of sigma. Comparing the parity-odd parts of H_{-sigma} f_sigma=g H_sigma degree by degree shows that all parity-odd chart coefficients below q vanish (induction using the invertible homological multipliers from §4; lower chart terms are common). At q the same equation demands P_q=h_q R+R h_q, with P_q the alternating source and h_q the odd chart part. The pure V^q coefficient of P_q is L epsilon kappa_{p,q}!=0, whereas that multiplier on h_q is zero. Contradiction.

Case S=-R: replace the target coordinate by w'=sigma w (and compose H_sigma with the same sign). Both charts are then tangent to identity; the target pair is g'_sigma(w')=-sigma g(sigma w'), with common linear R. This pair has reflection symmetry g'_-=-g'_+(-w'); its odd-degree terms are common and its even-degree terms alternating. Through degree q it can be made common by successively eliminating its alternating even-degree terms with parity charts id+sigma h_k at even degrees. Such charts preserve reflection symmetry (H_-=-H_+(-)), the homological multipliers are invertible at every even degree, and later eliminations do not affect lower degrees. The odd degrees are already common by the preserved symmetry. Composing these finite-jet charts with the proposed conjugacy would reduce the source to a common jet through q, with common linear R and tangent-to-identity parity charts. Case S=R has already ruled this out. Contradiction.

Thus no product reduction in the stated parity-only, origin-preserving C^q chart class exists. It is enough to test q-jets; the argument is not a claim of non-conjugacy under arbitrary state-dependent charts using the entire X, changes that move the fibre origin, base reassignments, extra carriers, clocks, or physical gauge transformations. In particular the threshold is a threshold for this parity harmonic and chart class, not for all non-componentwise laws in the full history carrier. For p a power of two there are no distinct CRT factors to couple. For m>1 the exact contrast uses the parity-bearing factor as an additional readout, but the analytic fibre itself remains separately postulated.

## 6. Research disposition and next test

- [THM] Within this enlarged model and parity-only observation class, cubic compensation is possible in odd s with tuned direct cubic sources; cubic-order alternation alone is not a non-reducibility certificate.
- [THM] The first alternating homological obstruction occurs at q=p/2-1. The explicit higher-order shear provides an exact positive control with owner-cubic recovery, nonzero parity contrast in another channel, and proved nonreducibility under the named parity charts. All finite-return lower jets (hence the DZT norm of the fixed owner cubic) are unchanged. It does not prove that the full owner map is a factor or identify the existing strobe/fold operations physically.
- [ALG] [SESSION] **N2 — diagnostic non-identifiability.** The autonomous owner product (F_n X,T_own) and the explicit degree-q comparator of §5 have exactly the same raw cubic coefficient and therefore the same real-subfield norm in the fixed frame and clock, although the latter has no product reduction in the stated parity-only origin-preserving C^q chart class. The reflection-completed sign comparator of Stage 2A §§5–6 is itself decouplable in that chart class: it can change the raw cubic while leaving the norm equal. That example alone does not demonstrate blindness to an irreducible coupling. Conversely, a constant (hence uncoupled) shear with a=1,d=0 in Stage 2A gives Q=4Q0 and multiplies the absolute norm by 4^{phi(p)/2}, so a changed norm alone cannot certify coupling either. Together these explicit model comparisons show that the cubic norm by itself neither establishes nor excludes such coupling in the enlarged class. They do not establish non-reducibility under full-register-dependent charts or physical gauge changes, nor a failure of the owner arithmetic law.
- [OPEN] **Intrinsic origin and full-carrier admissibility.** The term sigma rho^q is chosen, not generated by the signed-history algebra, by folding, or by the OFN commitments. Derive or rule out that resonant term using a specified relational composition rule that retains the actual parity factor and primitive readout without independently postulating a continuous fibre. Test admissibility and irreducibility under the full proposed presentation group (including X-dependent charts if allowed). An exact full-map recovery under the original fixed continuous readout would exclude any nonzero added shear and must not be confused with the established finite-jet recovery. The family-dependent order q and the free epsilon are remaining selection obligations. No physical mechanism, timing rule, recognition event, or canonical closure follows.

## 7. Evidence and requested independent review

EV-CODE / EV-RUN / EV-COVER: native Python 3 and SymPy 1.14.0, exact rational/cyclotomic arithmetic. Initial development run hit an unsupported int/ANP division; the numerator was explicitly converted to the field before freezing and rerunning. Final script exits 0. No previous campaign or owner extractor rerun.

- p=(12,16,20,24,28,36,40,60), 96/96 raw cubic checks: three (a,d) gates, two (beta,delta) choices, both signs, common owner b,gamma. Path weights evaluated by explicit finite sums, independent of closed-form evaluation. 16/16 additional recovery checks (both signs; conic and exact compensation for odd s, arbitrary nonzero cubic contrast at constant quadratic source for even s).
- p=12,16,...,256: 62/62 integer charge-inventory checks, first alternating kernel at q and reflection even-degree nonresonance. 57/57 non-power-of-two primitive-collision opposite-parity polynomial witnesses.
- p=(12,16,20): 12/12 raw high-jet checks using exact polynomial convolution in the real coordinates through q=5,7,9, respectively. Both signs, steps=s and s+1, epsilon=1/7, against the original exponential/sine Taylor jets. All extracted pure V lower coefficients through q-1 agree and degree-q contrast matches the formula. The written argument establishes the full lower-jet equality and the conjugacy obstruction; these are not claims of exhaustively checking every mixed monomial or chart.
- No normal form used in coefficient extraction. Raw recurrence adapted from the earlier SESSION computation, not an independent replay of the full owner engine. All-p conclusions rest on written proofs; finite regressions do not provide universal quantifiers.

Received unchanged via upload/ofn-strobe-boundary-stage2b-20261126, commit 55fee53b33ea5f46dbf20ae45eb20d8ec10167ad; SHA-256 readback matched before exact-blob placement.

| File under evidence/ofn/intrinsic_strobe_boundary/ | SHA-256 |
|---|---|
| scripts/strobe_boundary_stage2b_check.py | a64602fca97e1be04d113a954d4cc380fcec31aa89daaae144396e166c11ec5b |
| runs/strobe_boundary_stage2b_output.txt | b2bf2247ee3bef94a3adf90927150f347c26a26a700a2258977405439fb18f45 |

Reproduce: python3 evidence/ofn/intrinsic_strobe_boundary/scripts/strobe_boundary_stage2b_check.py

Independent review receipt: `records/ofn/OFN_INTRINSIC_STROBE_BOUNDARY_STAGE2B_CLAUDE_REVIEW.md` (PR #415, head `484143486e342dcd188a515c69c220866b080a9a`, SHA-256 `629e0c99dbac0a4cd52e716297f1c2c296b0a4cc357a9ba0e756d0ae3aa9979a`), reviewing #413 at `37e4f006b22b98582394903cd9183b3f02c3b70b`; discussion comment 7197389967. Verdict: APPROVE; N1–N3 optional. The reviewer reports Linux/Python 3/SymPy 1.14.0 native replay, exit 0 and byte-identical output (`b2bf2247ee3bef94a3adf90927150f347c26a26a700a2258977405439fb18f45`), with matching intake/placement hashes. A separate mpmath calculation at 50 digits, not importing the producer script, tests raw Taylor coefficients to degree q for p=12,16,20,24 (p=24 extends the producer's high-jet sample); the reported lower pure-V coefficients agree and the degree-q contrast agrees to within 1e-52. This is reviewer-reported high-precision evidence, not an exact certificate or new producer run; no separate executable/log was supplied. Both branches S=+R and S=-R of the written product-obstruction proof were checked by hand. N1 frames the standard period-two resonance; N2 narrows the joint diagnostic conclusion to the stated chart/model class; N3 retains the original Stage 2A pin and requires #411 first. These notes change no model, proof hypothesis or frozen evidence. No new computational campaign was run. The review is preserved unchanged in separate PR #415. PI archival merge decision remains pending. No canonical DSN, existing evidence, pipe or tag change.

*END OF STAGE 2B SESSION RECORD.*
