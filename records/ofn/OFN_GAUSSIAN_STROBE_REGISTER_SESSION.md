# Cyclotomic register quotients and Gaussian quarter-strobe arithmetic

**Date:** 26 November 2026.
**Status:** SESSION / NONCANONICAL; written proofs and finite independent checks, independently reviewed on 26 November 2026; the requested R1–R2 repairs are incorporated (§7). No owner RID, adoption, new DSN edition or physical selection.
**Scope:** fixed binary-register model, fixed raw DYAD resonance eigenframe and subgroup-strobe; standard cyclotomic arithmetic. No claim of mathematical novelty.

## 1. Sources and evidence boundary

- Binary Recognition wrap-up §2 and §§3C/F/G, records/ofn/NODE_BINARY_RECOGNITION_WRAPUP.md at merged PR #183, commit 1da597feb194837f56ad5d632c3ddd36c9f80abc (merge identity verified; blob c34b0921fcbccc186ea4e4149562ab98a8337bc0). SESSION, not an owner result.
- DYAD v6.4.24, tag dyad-v6.4.24 at f0af6392ed560b55aedc640bc166f0b87f612f7c; DSN SHA-256 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16, matching the adopted release record. §§6.9, 6.11: DYAD-ALG-KP-FRAME-SCALE, declared K_p family, DYAD-THM-Q403-PHASELAW (raw cubic subgroup-strobe and its exact three-path description).
- DZT v0.19, tag dzt-v0.19 at 5f3b2055e60957d98ad5e306872993ec92f96cb1; DSN SHA-256 2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce, matching the adopted release record. §6.3 and §7: DZT-THM-CASCADE-NORM-LAW, conditional on DYAD-THM-Q403-PHASELAW; cyclotomic unit/norm calculation.
- Governing OFN remains ofn-v0.13. The project discussion and Claude's reviews are SESSION input. The independent written review of PR #398 at 3146b75707756fe84cb59cc2a083e002eda84af2 is preserved in `records/ofn/OFN_GAUSSIAN_STROBE_REGISTER_CLAUDE_REVIEW.md` (SHA-256 `b58fdc1c032060ea559ba5a6bbf1ac454c41f2bc08261d0b06ed173190b7c51e`). Its §1 records native r1 and r2 replays by the reviewer; these are reviewer-reported executions, not additional runs by this editor.

EV-SRC-READ / EV-HASH: targeted owner sections, tag and adoption identities checked; no full owner-proof re-audit. The original DYAD extractor and certificate are not replayed; the DZT v0.19 import ledger identifies them as unavailable in this repository. All the new implications below have written algebraic proofs independent of a numerical fit.

## 2. Register–norm identity (standard mathematics, not a physical bridge)

[THM] [SESSION] Let n>=1, p=2n, L=zeta_p, R_p=Z[L], K=Q(L), and X_n=F_2^n. Use the fixed register law
$$F_n(x_0,\ldots,x_{n-1})=(1\oplus x_{n-1},x_0,\ldots,x_{n-2}),\qquad
\pi_n(X)=\sum_j x_j\bmod2.$$
Define the new readout (distinct from the wrap-up's characteristic-zero Z_n)
$$E_n(X)=\left[\sum_{j<n}x_jL^j\right]\in R_p/2R_p.$$
Then E_n is a surjective F_2-linear map, each fibre has size \(2^{n-\varphi(p)}\), and
$$|R_p/2R_p|=N_{K/\mathbb Q}(2)=2^{\varphi(p)},\qquad E_nF_n=L E_n+1.$$
Both injectivity of E_n and descent of native parity hold exactly when n is a power of 2 (including n=1).

Proof: R_p/2R_p=F_2[t]/(overline Phi_p), a vector space of dimension phi(p)<=n; polynomial representatives of degree <n span. Write n=2^a m with m odd: phi(2n)=2^a phi(m), so equality with n holds iff m=1. Parity is evaluation at 1. In the nonfaithful sector the nonzero kernel representative overline Phi_p has degree <n and value 1 at 1, proving failure of parity descent explicitly. In the faithful sector descent is immediate. The affine identity follows from L^n=-1=1 mod 2. The distinction between + and - in the linear signed shift disappears mod 2; Boolean complement is retained by the affine +1, not erased.

[ALG] [SESSION] [reformulation only] Under the DZT norm law, for p=2n=4s>=12,
$$|N_+(M_p)|=\frac{\ell(p)^2}{2^{\delta_p}|E_n(X_n)|^{1/4}},\qquad
\delta_p=[p=2^k]+[p=3\cdot 2^k].$$
Equivalently the quarter-power factor is \(N_{K^+/\mathbb Q}(2)^{1/2}\). For p a power of 2, p>=16, this becomes \(1/(2\,|X_n|^{1/4})\). This substitutes the common cardinality/norm N(2) into an existing owner law; it does not establish a common generating mechanism.

## 3. Quadratic-source scaling: complete ordered-sum derivation

[THM] [SESSION] Fix p=4s>=8, L=zeta_p, I=L^s=i, and K_p=2-L-L^{-1}. Use the DYAD raw linear eigenframe W=rho+((L-1)/K_p) eta, with formal V=conjugate(W). Replace the primitive nonlinear functions, keeping their linear jets and no quadratic term in S, by
$$G(\rho)=\rho+a\rho^2+b\rho^3+O(\rho^4),\quad S(\eta)=\eta+\gamma\eta^3+O(\eta^4),\qquad
(\rho',\eta')=(\rho-S(\eta),\eta+K_p(G(\rho)-S(\eta))).$$
Here a,b,gamma are real. The same proof permits an arbitrary real homogeneous cubic jet in the raw map with this fixed linear and quadratic jet. Define Q_p(a,b,gamma) as the V^3 coefficient in the W component of the raw s-step return after removing the linear rotation, exactly the owner clock/frame/channel (subtracting the identity does not affect it). Then
$$Q_p(a,b,\gamma)=\frac{2a^2L^5(IL^2+I-L^2+1)}{(1+L)^4(L^2+L+1)}
=4a^2Q_p(1/2,1/6,-1/6).$$
In particular the result is independent of b and gamma, is zero at a=0, and at p=8 is zero for every a. All statements concern the degree-three coefficient, not equality of complete maps.

**Proof.** Put R(W,V)=(LW,L^{-1}V), let f be the raw complex-coordinate map, and h=R^{-1}f. Inverting the linear frame gives
$$\rho=(W+LV)/(1+L),\qquad \eta=(L-1)(V-W)/(1+L).$$
The W-component of h_2 is \(A W^2+B WV+C V^2\), where
$$A=\frac{a(L-1)}{L(1+L)^2},\qquad B=2LA,\quad C=L^2A.$$
The V component is the conjugate polynomial (swap W,V and conjugate coefficients). Define H_j=R^{-j}hR^j. Direct composition gives R^{-s}f^s=H_{s-1}...H_0. Through degree 3, its cubic jet is
$$\sum_{j=0}^{s-1}H_{j,3}+\sum_{0\le j<k<s}D H_{k,2}\,H_{j,2}.$$
This follows by composing one further identity-tangent map: degree 3 receives its own cubic, the previous cubic, and the derivative of its quadratic on the previous quadratic. Every insertion involving degree 3 and another nonlinear term is at least degree 4.

Only the direct V^3 monomial contributes to the target from the first sum; its coefficient carries L^{-4j}. Other direct cubic monomials are not claimed to have this weight. Set
$$G_s(k)=\sum_{j=0}^{s-1}L^{kj},\quad S_s(u,v)=\sum_{0\le j<k<s}L^{uj+vk}.$$
The exact geometric and ordered-sum identities are
$$(1-L^k)G_s(k)=1-L^{ks}=1-I^k,\qquad
(1-L^u)S_s(u,v)=G_s(v)-G_s(u+v).$$
For the second identity sum first over j at each k, using \((1-L^u)\sum_{j<k}L^{uj}=1-L^{uk}\). Since L^4 has order s>=2, G_s(-4)=0, independent of the direct cubic coefficient.

The W quadratic in H_k has terms A L^k W^2+B L^{-k}WV+C L^{-3k}V^2. At W=0, the two derivatives that contribute are B L^{-k}V and 2C L^{-3k}V; the earlier H_j quadratic components there are C L^{-3j}V^2 and conjugate(A) L^{-j}V^2. Hence precisely two quadratic paths:
$$Q_p=BC\,S_s(-3,-1)+2C\overline A\,S_s(-1,-3).$$
All denominators below are nonzero for p>=8. With D=(1-L^{-1})(1-L^{-3}), the ordered-sum identities give
$$S_s(-3,-1)=\frac{1+I}{D},\qquad S_s(-1,-3)=\frac{1-I}{D}.$$
Indeed G_s(-1)=(1+I)/(1-L^{-1}), G_s(-3)=(1-I)/(1-L^{-3}), and G_s(-4)=0. Thus these weights have been derived rather than postulated. Since a is real, \(\overline A=-L^3 A\), and \(2C\overline A=-L^2BC\). Substituting yields
$$Q_p=\frac{BC}{D}\big[(1+I)-L^2(1-I)\big],\qquad
BC/D=\frac{2a^2L^5}{(1+L)^4(L^2+L+1)}.$$
This proves the formula. For the owner parameters it matches DYAD-THM-Q403-PHASELAW; no source claim is re-owned. QED.

[ALG] [SESSION] For a in Q, M_p(a)=Q_p(a)/(iL^3)=4a^2 M_p; its absolute real-subfield norm is multiplied by \(|4a^2|^{\varphi(p)/2}\). For a nonzero rational passive linear rescaling W'=cW the V^3 coefficient scales by c^{-2}; these are not arbitrary nonlinear or complex frame changes. For a general complex c the coefficient transforms by c/conjugate(c)^3. No invariance under that larger group is asserted.

## 4. Gaussian boundary ideal: correction of the mechanism

[THM] [SESSION] Write \(\mathfrak g=(1-I)R_p=(1+i)R_p\). Its square is 2R_p. The strobe boundary factor satisfies the charge-graded ideal identity
$$(1-I^k)R_p=
\begin{cases}
0,&k=0\bmod4,\\
\mathfrak g,&k\text{ odd},\\
\mathfrak g^2,&k=2\bmod4.
\end{cases}$$
The two ordered sums satisfy \(D S_s(-3,-1)=1+I\) and \(D S_s(-1,-3)=1-I\), each already generating the same Gaussian ideal after multiplication by D. In the common numerator,
$$(1+I)-L^2(1-I)=(1+I)(1+IL^2).$$
Therefore the Gauss factor is **common to the paths**, not a factor created by taking their difference. It enters each path from a quarter-strobe geometric sum (the boundary numerator 1-I^k). The proposed two-path-difference/fold origin is rejected for this fixed path decomposition. This does not exclude alternative descriptions of the same polynomial or a future separately specified mechanism.

At a=1/2 the scalar combines with the Gaussian numerator and the equivalent formula is
$$Q_p=-\frac{L^7(1-L^{s-2})}{(1+i)(1+L)^4(L^2+L+1)}.$$
The original Taylor coefficient 1/2 alone is not the intrinsic ideal-class source: rational factors vanish in the quotient by extended rational fractional ideals, whereas the strobe defect 1-I generates the nontrivial Gaussian class.

[THM] [SESSION] Let I(K) be the fractional-ideal group and quotient by the image of the fractional ideals of Q under extension to R_p. Then [g] has exact order two: its square is (2), and if g=rR_p for rational nonzero r, the ideal norm equality forces |r|=sqrt(2), impossible. This is not the ordinary ideal class group; g is the extension of the Gaussian prime ideal and need not be prime in R_p.

For p>=12 in the DZT generic sector (exclude powers of two, 3 times a power of two, and actual odd-prime anomaly points p=8 ell^a with ell^a=1 mod 4), the remaining factors are units by the cyclotomic norm/prime-power calculation in DZT §6.3. Hence (Q_p)=g^{-1} at the owner normalization, and its class is [g^{-1}] for nonzero rational a,c. At p=2^k>=16, let P=(1-L)R_p: g=P^{phi(p)/2}, (1+L)=P, (1-L^{s-2})=P^2 and (1+L+L^2)=R_p. Thus (Q_p)=g^{-1}P^{-2}, not g^{-1}. The pure-power-of-two case follows from total ramification of 2 and v_2(s-2)=1. At p=8 or a=0 a nonzero fractional principal ideal is not defined. Odd-support anomalies and the Eisenstein-factor exceptions are not collapsed into the generic result.

## 5. Gaussian quotient and folding (standard algebra, precise maps)

[THM] [SESSION] For p=4s>=4, write A=R_p/g, C=R_p/2R_p, J=g/2R_p. There is an isomorphism
$$A\simeq R_{p/2}/2R_{p/2}\simeq\mathbb F_2[t]/H,\qquad H=\overline{\Phi}_{p/2}.$$
It sends the class of L to the class of zeta_{p/2} (the two polynomial variables are identified). This is **not** the map induced by the natural subfield inclusion zeta_{p/2}=L^2. Under the displayed identification the latter induces t->t^2, i.e. Frobenius, bijective iff 8 does not divide p. Proof: write p=2^alpha m, m odd, alpha>=2. Modulo 2,
$$\overline{\Phi}_p=\overline{\Phi}_m^{2^{\alpha-1}}=H^2,\quad
1+t^s=(1+t^m)^{2^{\alpha-2}}.$$
Since t^m+1 is squarefree, gcd(overline Phi_p,1+t^s)=H. The quotient by g imposes 2=0 and 1+t^s=0, proving the asserted isomorphism. The finite quotient by H is reduced iff alpha=2, exactly the stated Frobenius criterion.

Let B:X_{2s}->X_s be B(X)_j=x_j XOR x_{j+s}, and q:C->A the quotient. Directly BF_{2s}=F_s B and pi_s B=pi_{2s}. The diagram q E_{2s}=E_s B uses the above chosen-root isomorphism, not subfield inclusion. Its polynomial proof is L^s=I=1 modulo g.

The kernel of B is the doubled register set {(Y,Y)}. Its image under E_{2s} is exactly J, because
$$E_{2s}(Y,Y)=(1+I)\sum_{j<s} y_jL^j\bmod 2R_p.$$
Multiplication by 1+I gives an additive R_p-module isomorphism A->J (cancel the nonzero generator in (2)=g^2); the polynomials of degree <s span A. Thus
$$0\longrightarrow A\xrightarrow{\cdot(1+I)}C\xrightarrow{q}A\longrightarrow0$$
is exact as additive modules, not a ring isomorphism between A and the square-zero ideal J. Each layer has size \(2^{\varphi(p)/2}\). The restriction of E_{2s} to ker B has fibres of size \(2^{s-\varphi(p)/2}\); it is not an identification of individual doubled registers in general. The linear ideal filtration is not an invariant subset filtration of the affine update: +1 maps a zero fibre to another fibre. This is standard ramification, not a new physical origin of binary structure.

**Sector boundary.** Faithfulness and native parity descent occur for E_{2s} exactly at p a power of two; this sector is excluded by the DZT generic ideal equality. At generic p the two E maps are quotients and native parity does not descend to these cyclotomic carriers. B itself nevertheless preserves parity as a map between binary registers. No hidden complete recognition state is inferred from the Gaussian quotient.

## 6. Exact shared ideal, sharpened research question

[THM] [SESSION] If p=4s>=12 is neither a power of two nor 3 times a power of two, D=(1-L^{-1})(1-L^{-3}) is a unit of R_p: the respective root orders p and p/gcd(p,3) are not prime powers, so their cyclotomic norms are 1. Consequently each individual ordered sum in §3 generates g, independently of whether the residual odd-prime anomaly is present:
$$(S_s(-3,-1))=(S_s(-1,-3))=\mathfrak g.$$
Combining with §5, multiplication by either ordered sum on C has image exactly E_{2s}(ker B)=J. In all p=4s>=8, without the unit restriction, the denominator-cleared path sums D S_s(-3,-1) and D S_s(-1,-3) have that same image. In the unit sector each ordered sum is, up to a unit, the strobe boundary 1 ± I; its multiplication image is therefore the Gaussian layer J, which coincides with E_{2s}(ker B). This is an exact algebraic coincidence of ideals, not an identification of operations. They do not identify the two physical operations: the strobe sums truncate a character orbit at s; B folds two register blocks. In particular no map intertwining the nonlinear DYAD with a binary register has been constructed.

[OPEN] **Intrinsic strobe-boundary structure:** Does a specified relational composition or admissible observation law realize both the strobe boundary ideal and the folding quotient without imposing them independently? To advance this, provide an actual carrier, update, readouts and clock, and prove a structure-preserving map or an obstruction. The prior two-path-interference/fold mechanism is rejected, and the physical interpretation of the shared Gaussian ideal is not established. Rational-scale invariance is a scoped mathematical result; no physical frame group is selected. No inference to a physical continuum, time, primacy, generator selection, or cross-branch amplitude law.

## 7. Evidence and review gates

The original files were received unchanged on upload/ofn-gaussian-cascade-20261126, commit 21fdf63256fd97a1808422030f9b7f44a958ea9e, and rehashed on readback. Placement reuses the same Git blobs, not regenerated approximations.

| File under evidence/ofn/gaussian_cascade/ | SHA-256 |
|---|---|
| scripts/cyclotomic_gauss_cascade_checks.py | d5ddda4dbac3e431692a05420122f13819b3e7be49f87eac5044758a5dd36684 |
| runs/cyclotomic_gauss_cascade_checks_output.txt | 64b3a912e409e649b727a989186853df50fa830ba433853c8e7002f0d950066d |
| scripts/cyclotomic_gauss_cascade_checks_r2.py | 0e6f8486de5fcb27fdb955e37134cfd163613dfc525746d4f374f6edd1053d6b |
| runs/cyclotomic_gauss_cascade_checks_r2_output.txt | 3f189abf842c14be79a07b16a96a335ad7a56c263b23fd347eedb103679a54b9 |

EV-CODE / EV-RUN / EV-COVER: r1 stored 140 raw-jet cases, 64 polynomial checks, one changed-clock control; earlier wider attempt timed out at p=104 and is not a completed test. Claude's independent review (§1 of `records/ofn/OFN_GAUSSIAN_STROBE_REGISTER_CLAUDE_REVIEW.md`) records a byte-identical r1 replay (script SHA-256 `d5ddda4dbac3e431692a05420122f13819b3e7be49f87eac5044758a5dd36684`), and a native r2 replay on Linux, Python 3 / SymPy 1.14.0 from the byte-identical r2 script (SHA-256 `0e6f8486de5fcb27fdb955e37134cfd163613dfc525746d4f374f6edd1053d6b`). Exit 0; the output was byte-identical to the preserved r2 output (SHA-256 `3f189abf842c14be79a07b16a96a335ad7a56c263b23fd347eedb103679a54b9`). The supplemental 24 generic cases are subsumed by r2. EV-INDEP: independent reviewer replay of the same implementation, not a second implementation. Do not sum overlapping reruns into a new coverage claim.

R2 ran natively in Python / SymPy 1.14.0, on 26 Nov 2026. Raw-jet recurrence reimplemented in explicit real-coordinate degrees 1–3 (no normalizer). The symbolic path calculation now derives the ordered weights from the geometric formula; direct finite sums independently check them. 220/220 raw cases: p=(8,12,16,20,24,28,32,36,40,44,72), a=(0,1/4,1/2,1,-3/2), (b,gamma)=(1/6,-1/6),(0,0),(7/5,-3/7),(-2,5). 22/22 direct ordered sums; 10/10 negative controls at p=(8,12,20,28,40), steps=s+1, a=0, each cubic source separately nonzero. 64/64 quotient-polynomial checks for p=4,8,...,256, including ideal layer and Frobenius. All PASS. Exact rational/cyclotomic arithmetic, not a rerun of the unavailable DYAD owner extractor. The finite checks support the written all-p proof, not replace it; r2 code is a successor, not modified r1 evidence.

Reproduction from repository root:
    python3 evidence/ofn/gaussian_cascade/scripts/cyclotomic_gauss_cascade_checks_r2.py

Independent review receipt: `records/ofn/OFN_GAUSSIAN_STROBE_REGISTER_CLAUDE_REVIEW.md` (reviewed head `3146b75707756fe84cb59cc2a083e002eda84af2`, SHA-256 `b58fdc1c032060ea559ba5a6bbf1ac454c41f2bc08261d0b06ed173190b7c51e`). The 4,692-byte received review is preserved unchanged on `upload/ofn-gaussian-review-20261126` at `c28a326310212cc140a0e78a78c5bc38bae787a2`; SHA-256 and exact-blob placement checked. Review verdict: approve after R1 and R2. §3–6 proofs accepted at the stated scope and r2 replay reported byte-identical. R1 narrows §6 to the exact ideal coincidence; R2 records the independent replay and source receipt in §§1 and 7. Both requested changes are implemented; formulae, assumptions, proof grades, and frozen scripts/outputs remain unchanged. No further computational campaign is required for these text-only repairs. PI merge decision, any routing to DYAD/DZT/NUMGEN/RECOG or RRF, and any canonical adoption remain separate decisions.

*END OF SESSION RECORD.*
