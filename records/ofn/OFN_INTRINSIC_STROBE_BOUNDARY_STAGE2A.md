# Intrinsic strobe-boundary structure — Stage 2A: scalar recognition gate and cascade-norm non-identifiability

**Date:** 26 November 2026.
**Status:** SESSION / NONCANONICAL; independently reviewed at the original head (review PR #415); R1 wording incorporated. PI archival merge decision pending. No owner RID, canonical adoption, physical carrier, clock or generator selection.
**Decision:** A deliberately coupled diagnostic model supplies an explicit initial-parity contrast. Its scalar quadratic-gate class is completely classified for matching the owner cubic cascade at both initial parities. A pure sign gate can change that coefficient while preserving its real-subfield norm exactly. A reflection-completed sign gate is reducible to an autonomous product by a bit-dependent change of coordinates. These findings constrain, but do not resolve, the intrinsic common-mechanism question.

## 1. Sources and scope

- Stage 1, PR #403 merged at 14b46849791087cb264685bd5d70edd383c6cc41, record SHA-256 3a7b6e59bec9028f518d7fd9b17e5c146e189a859d59ecb07caa18744baa310f; independent review #407 merged at 12a5ae9b294505055479a63683b1a9bde0dac4d7. Full Stage 1 record and review inspected; especially §§2–5, the affine-clock obstruction, parity-sensitive lower component, and R1–R2 all-s 2-local CRT splitting. The latter rules out deriving a mixed-sector interaction from componentwise ring operations alone. Neither Stage 1 nor this study identifies the physical operations.
- Binary Recognition wrap-up, #183 at 1da597feb194837f56ad5d632c3ddd36c9f80abc, §2 (register law and parity). Fixed model, SESSION, not owner-adopted.
- Gaussian quarter-strobe record, #398 at 65a42d1ba4725caf42e9f8b2d3017bf3f714a15c, §3 (quadratic-source scaling and the two charge paths), §§4–6 (Gaussian ideal, quotient, nonclaims). Scoped accepted NONCANONICAL result.
- DYAD v6.4.24, tag dyad-v6.4.24, SHA-256 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16, §§6.9, 6.11, DYAD-THM-Q403-PHASELAW: raw W_p frame and owner cubic subgroup-strobe channel. Its owner family has a quadratic coefficient 1/2, cubic source 1/6 and sine cubic coefficient -1/6.
- DZT v0.19, tag dzt-v0.19, SHA-256 2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce, §6.3, DZT-THM-CASCADE-NORM-LAW, conditional on DYAD-THM-Q403-PHASELAW. The comparison below uses the actual real-subfield norm, not a transfer of the owner law to a physically identified model.
- OFN v0.13, tag ofn-v0.13, SHA-256 4a2d266bf89cd2130e901b7543bacbaf7fa3e844c60e355a2e3c23ef4f075a49, targeted §1 and SG-OFN-STATE/PRESENTATION/TIME/INFORMATION/SELECTION. State completeness and admissible transformations remain separate requirements.

EV-SRC-READ / EV-HASH: tagged DSNs and adoption/release records checked against actual retrieved bytes; targeted owner reading, not a full owner proof audit. No owner extractor replay. Standard mathematics is used without a novelty claim. Methodology v1.4 and CONVENTIONS.md govern the SESSION record.

## 2. Explicit candidate and its null

[DEF] [SESSION] Fix p=4s>=12, n=2s, L=zeta_p, I=L^s=i, K=Q(L), K^+ its maximal real subfield, K_p=2-L-L^{-1}. Let X_n be the complete binary register and F_n its existing twisted shift. The chosen recognition sign is sigma(X)=(-1)^{pi_n(X)}, so sigma(F_n X)=-sigma(X). The sign is complement-invariant for this even n; physical complement gauge is not selected.

Take the enlarged state (X,z) in X_n x R^2, with z=(rho,eta). Define a family of local analytic maps T_sigma by
$$G_\sigma(\rho)=\rho+(a+\sigma d)\rho^2+b\rho^3+O(\rho^4),\quad S(\eta)=\eta+\gamma\eta^3+O(\eta^4),$$
$$T_\sigma(\rho,\eta)=(\rho-S(\eta),\ \eta+K_p(G_\sigma(\rho)-S(\eta))),\qquad
\mathcal T(X,z)=(F_n X,T_{\sigma(X)}z).$$
All a,d,b,gamma are real; the linear and cubic jets are shared by both sign values and S has no quadratic term. Higher terms do not affect the degree-three result. The clock is one simultaneous formal update, observed after s updates, not calibrated time. The common raw eigenframe is W=rho+(L-1)eta/K_p, with V its formal conjugate.

This is a specified one-way scalar gate, not a construction from the history algebra alone. The register retains all its bits independently of z, and the continuous component is a separate enlarged-state coordinate, not identified with the primitive cyclotomic readout of X. At d=0 the gate is the autonomous-product null; a=1/2, b=1/6, gamma=-1/6 recovers the owner three-jet (the full owner map only for the owner analytic nonlinearities). At d!=0 it is a changed model, even if one particular return coefficient agrees. No physical event or pole-exchange law follows.

For initial sigma=+1 or -1, define Q_p^sigma(a,d) as the pure V^3 coefficient in the W component of the s-step continuous fibre map with linear rotation L^s removed, in this fixed raw frame. Subtracting identity does not change that coefficient. Let Q_p^0 be the nonzero owner coefficient at p>=12; superscript 0 denotes the owner baseline, not a third sign state. The recovery gate below requires both Q_p^+=Q_p^-=Q_p^0. It is coefficient-level recovery, not a full nonlinear factor or generator identification.

## 3. Exact all-p scalar-gate formula

[THM] [SESSION] Write x=L^{-1}, e=(-1)^s. Define
$$A=\frac{(1+I)(x^2+I)}{x^2(x-1)^2(x^2+x+1)},\quad
B=\frac{(1+eI)(x^2+eI)}{x^2(x+1)^2(x^2-x+1)},$$
$$C=\frac{C_{\rm num}}{x^2(x-1)(x+1)(x^2-x+1)(x^2+x+1)},$$
$$C_{\rm num}=\begin{cases}
-2(x+I)^2(x^2-Ix-1),&s\text{ odd},\\
-2(1+I)(x^2+1)(x^2+I),&s\text{ even}.
\end{cases}$$
Let r_p=B/A and c_p=C/A. Then
$$Q_p^\sigma(a,d)=4Q_p^0(a^2+r_p d^2+\sigma c_p ad),\qquad c_p\ne0.$$
The coefficient is independent of the common b and gamma. It is not asserted to be independent of a cubic jet that changes with the recognition sign.

**Derivation.** Put R(W,V)=(LW,L^{-1}V), and let the j-th continuous fibre map be f_j with quadratic shear a_j=a+sigma d(-1)^j. As in #398 §3, write h_j=R^{-1} f_j and H_j=R^{-j}h_j R^j. The rotation-removed composition is H_{s-1}...H_0. Its cubic jet consists of the sum of direct cubic jets and the ordered sum D H_{k,2} H_{j,2} for j<k. The direct V^3 coefficient of h_j is independent of j since the cubic jet is shared, and its charge -4 sum vanishes because L^{-4} has order s>=3.

At unit quadratic shear use coefficients A_1=(L-1)/(L(1+L)^2), B_1=2L A_1, C_1=L^2 A_1; the two path coefficients are B_1 C_1 and 2 C_1 conjugate(A_1)=-L^2 B_1 C_1. The factors from varying the two quadratic insertions are a_j a_k. Thus exactly
$$Q_p^\sigma=B_1 C_1\sum_{0\le j<k<s}a_j a_k(x^{3j+k}-L^2 x^{j+3k}).$$
For signed weights eta,zeta in {+1,-1}, put
$$S_s(u,v;\eta,\zeta)=\sum_{j<k}(\eta x^u)^j(\zeta x^v)^k,\quad
T_s(\eta,\zeta)=S_s(3,1;\eta,\zeta)-x^{-2} S_s(1,3;\eta,\zeta).$$
Expand a_j a_k to obtain coefficients of a^2,d^2,sigma ad respectively:
$$A=T_s(+,+),\quad B=T_s(-,-),\quad C=T_s(+,-)+T_s(-,+).$$
If U=eta x^u, V'=zeta x^v, finite geometric summation gives
$$S_s(u,v;\eta,\zeta)=
\frac{(1-(V')^s)/(1-V')-(1-U^s(V')^s)/(1-UV')}{1-U}.$$
Here U^s=eta^s(-I)^u, (V')^s=zeta^s(-I)^v. All denominators used for the two paths are nonzero for p>=12: the possible offending orders of x or its powers 1,3,4 with signs would require p<=8. Substitution and common-denominator simplification give the three displayed rational formulas. Equivalently, the following symbolic script derives them from the geometric identity rather than fitting field values. At a=1/2,d=0 this gives B_1 C_1 A/4=Q_p^0 by #398 and the owner closed form; hence the normalization above.

For theta=2pi/p in (0,pi/6], x=exp(-i theta). Every denominator and the numerators of A,B are nonzero; the odd-s C numerator has x^2-Ix-1=x(-2i sin(theta)-i), nonzero, and x+I!=0. The even-s C numerator is also nonzero in this angle interval. Therefore c_p!=0. This completes the all-p proof; numerical or finite symbolic checks do not supply the quantifier.

## 4. Classification of both-parity recovery

[THM] [SESSION] The ratio r_p is real and lies in K^+. In the principal embedding,
$$r_p=\tan^2(\theta/2)\frac{1+2\cos\theta}{2\cos\theta-1}
\begin{cases}
\tan(\pi/4+\theta),&s\text{ odd},\\
-1,&s\text{ even}.
\end{cases}$$
Proof: use (x-1)/(x+1)=-i tan(theta/2), and (x^2+x+1)/(x^2-x+1)=(1+2cos(theta))/(2cos(theta)-1). For odd s the extra multiplier in B/A is ((1-I)/(1+I))*((x^2-I)/(x^2+I))=-tan(pi/4+theta). The denominators are nonzero on the stated domain. For odd s the three positive factors increase strictly with theta; at theta=pi/6 their product is 1, so r_12=1 and 0<r_p<1 for p>12. For even s r_p<0.

Subtracting the two recovery equations using §3 and Q_p^0 c_p!=0 gives ad=0; the common equation is a^2+r_p d^2=1/4. Consequently:
- constant gate: d=0, a=+/-1/2;
- pure sign gate: a=0, d=+/-1/(2 sqrt(r_p)), available over R iff s is odd;
- mixed gate ad!=0: impossible;
- even-s nonconstant scalar gate: impossible.

[THM] [SESSION] Rational-coefficient refinement. The automorphism tau:L->-L exists for p divisible by 4, since gcd(1+p/2,p)=1, and is an involution. In the expressions of §3, x->-x and I->e I interchange A and B. Thus tau(r_p)=1/r_p. If r_p is rational, r_p=+/-1. For odd s>3 the strict bound 0<r_p<1 excludes rationality. Therefore the only nonconstant both-parity recovery with a,d rational is p=12, a=0,d=+/-1/2. In particular there is no nonconstant rational scalar gate preserving the coefficient for the entire family. With nonnegative shear coefficients a+d,a-d>=0 only the constant owner magnitude a=1/2 is admitted by the recovery gate.

These are exact scoped obstructions in the scalar quadratic-gate family, not no-go theorems for arbitrary cross-sector composition. For ad!=0 the initial sign is detectably coupled to the raw coefficient, with
$$Q_p^+-Q_p^-=8Q_p^0 c_p ad.$$
For example a=d=1/4 is a nonconstant on/off gate, with nonzero contrast, and fails simultaneous owner-coefficient recovery. This is a positive control for the discrimination test, not evidence for a physical recognition mechanism.

## 5. Exact norm blindness of the owner-magnitude pure sign gate

[THM] [SESSION] Set a=0,d=1/2 (or -1/2). For either initial sign,
$$Q_p^{\rm alt}=r_p Q_p^0,\qquad M_p^{\rm alt}=Q_p^{\rm alt}/(iL^3)=r_p M_p^0\in K^+.$$
The involution tau above restricts to a nontrivial involution of K^+ for p>=12: its multiplier 1+p/2 is not congruent to +/-1 modulo p. Pairing real-subfield embeddings by tau gives
$$N_{K^+/\mathbb Q}(r_p)=1,\qquad
N_{K^+/\mathbb Q}(M_p^{\rm alt})=N_{K^+/\mathbb Q}(M_p^0).$$
The proof uses tau(r_p)=r_p^{-1}; equivalently the relative norm to its fixed field is 1. This holds for both strobe parities, including the negative real r_p for even s; the real-subfield embeddings pair exactly. The absolute value agrees as well. For all p!=12 in p=4s>=12 the coefficient itself differs (odd s: 0<r_p<1; even s: r_p<0).

Thus the arithmetic norm appearing in the adopted DZT diagnostic is not identifying on this pair of models at the specified frame and clock, although the owner magnitude and both-parity coefficient gate normally distinguish them. The signed norm equality is a model calculation, not a physical import of the DZT law and not an assertion that every gate has a real amplitude. No norm criterion alone can distinguish this particular sign-alternation comparator. Norm one of a field element is not a claim that it is an algebraic-integer unit. The exact coefficient and initial-parity contrast should be retained as separate tests.

**R1 scope (review PR #415).** The owner-magnitude sign comparator of this section, with the full reflection completion in §6, has G_+(rho)=exp(rho)-1, G_-(rho)=1-exp(-rho), and S=sin(eta). The chart of §6 conjugates this completed system to the autonomous product (F_n X, -T_own(w)). It is therefore a decouplable comparator, not evidence for an interaction irreducible under those charts. The norm equality demonstrates non-identification of the raw coefficient in the fixed frame and clock, not blindness to a genuine coupling by this example alone. Without the full reflection completion, only the stated finite-jet conclusion is available. No physical admissibility of the chart is selected.

## 6. Sign gate reducibility and Stage 2 boundary

[THM] [SESSION] [assuming: full reflection completion] The pure sign branch also has a product-conjugacy control. For a=0 choose a full analytic positive-sign map T_+ with the specified quadratic coefficient d, and choose its negative-sign partner by T_-(z)=-T_+(-z). For the shear family this is effected by G_-(rho)=-G_+(-rho) and odd S, in particular by reflecting the owner exponential with d=1/2. This preserves the common linear and cubic jets. Then T_sigma(z)=sigma T_+(sigma z) and H(X,z)=(X,sigma(X) z) is an involutive coordinate change on the enlarged state. Direct calculation gives
$$H\mathcal T H^{-1}(X,w)=(F_n X,-T_+(w)).$$
Thus this explicitly completed sign gate is conjugate to a product with autonomous map -T_+, not to the asserted original owner product. Its displayed primitive eigenvalue changes from L to -L in the new fibre chart. This is an exact mathematical conjugacy conditional on the full reflection completion; for arbitrary higher jets with the same quadratic/cubic terms it gives only the corresponding finite-jet result, not a full conjugacy. Whether such a bit-dependent chart is physically admissible is not selected. The equality in §5 is calculated in the original common raw frame and clock; no passive recharting is silently used to compare coefficients.

[OPEN] The intrinsic mechanism remains unresolved. The split carrier does not generate the scalar gate; the above deliberately imposed model uses an additional observation law and a separate continuous fibre. The recovery test covers only one raw coefficient with the common cubic jet. In particular it does not require the continuous dynamics to be exactly the original DYAD factor (that stronger fixed-readout contract excludes nonconstant T_sigma immediately). No lower p=4 DYAD cascade, carrier/clock identification, physical gauge choice or new owner claim is admitted. A nonconstant contrast is not a recognition event or feedback into the register.

**Stage 2B proposed next test:** classify the first non-componentwise composition jet retaining the actual parity-bearing sector and primitive sector, with intermediate-factor inventory for composite s. Include parity-dependent cubic sources only as an explicitly different model class; test whether direct charge cancellation, coefficient recovery and initial-parity contrast can be satisfied simultaneously without tuning or bit-dependent separability. Require a declared observation/factor contract and distinguish exact nonlinear recovery, finite-jet recovery, passive transport and norm-only coincidence. Do not treat a fitted gate that reproduces one norm or one coefficient as intrinsic selection. An obstruction is an acceptable outcome.

## 7. Evidence and review request

EV-CODE / EV-RUN / EV-COVER: native Python 3 / SymPy 1.14.0, exact rational and cyclotomic arithmetic. The real-coordinate raw recurrence is adapted from the frozen #398 r2 script, with step-dependent quadratic source, and is independent of the ordered-sum evaluation in this checker. Not a fresh independent implementation of the whole owner engine, no replay of the unavailable owner extractor. The symbolic calculation derives all three ordered weights for both e values from the geometric identity and checks their automorphic exchange. The all-p proof is §3–5, not extrapolation.

Coverage p=(12,16,20,24,28,32,36,40,44,60,72): six pairs (a,d)=(0,0),(1/2,0),(-1/2,0),(0,1/2),(1/4,1/4),(3/5,-2/7); two shared cubic pairs (b,gamma)=(1/6,-1/6),(7/5,-3/7); both initial signs. 264/264 raw-jet cases; 33/33 direct ordered-sum coefficient checks; 11/11 exact real-subfield norm-one products including inverse conjugacy and realness; 11/11 nonconstant-amplitude contrast controls. All PASS. No all-p enumeration, no test of arbitrary higher-order gates or physical mechanisms. The reflection-conjugacy statement in §6 is a written algebraic proof.

Evidence received unchanged on upload/ofn-strobe-boundary-stage2a-20261126, commit 9ff0b54bb4a49c2091e3e6c61feb1bdf59c9588b, read back by exact hashes before placement.

| File under evidence/ofn/intrinsic_strobe_boundary/ | SHA-256 |
|---|---|
| scripts/strobe_boundary_stage2_scalar_gate_check.py | aac8861eb440ae325a6ab9549b8919ce0b76481431b220efdd0c532b00be71f9 |
| runs/strobe_boundary_stage2_scalar_gate_output.txt | df1bc84aa5a38c8b36e71d160ca10aa681731594c4354b09691c5972a80938ff |

Reproduce from repository root: python3 evidence/ofn/intrinsic_strobe_boundary/scripts/strobe_boundary_stage2_scalar_gate_check.py

Independent review receipt: `records/ofn/OFN_INTRINSIC_STROBE_BOUNDARY_STAGE2A_CLAUDE_REVIEW.md` (PR #415, head `484143486e342dcd188a515c69c220866b080a9a`, SHA-256 `3ba36b1089b2a3cfc47ceca801ab5e523bf3535eee7091ce0b3078f565c3d78a`), reviewing #411 at `496aafbe0113e422b7f538b71efa6be8f127e6f3`; discussion comment 7197389601. Verdict: APPROVE, R1 recommended. The reviewer reports Linux/Python 3/SymPy 1.14.0 native replay, exit 0, output byte-identical to the frozen output (`df1bc84aa5a38c8b36e71d160ca10aa681731594c4354b09691c5972a80938ff`), and matched intake/placement hashes. A separate mpmath calculation at 40 digits, not importing the producer script, checks p=12,16,...,200, including the ratio formula (reported agreement 2e-41), inverse conjugacy, reality, r_12=1 and nonzero c_p. This is reviewer-reported high-precision evidence, not an exact certificate or a new producer execution; no separate executable/log was supplied. The review also checks the written all-p proofs in §§3–6. R1 is incorporated in §5 without changing any formula, assumptions, grade scope or frozen evidence. No computational rerun is required for this wording change. The review record remains unchanged in its separate PR #415. Merge #411 before #413 (which pins this original reviewed scientific source); PI authorization remains pending. No mathematical novelty, physical selection, owner OPEN closure, canonical changes or consumer import asserted.

*END OF STAGE 2A SESSION RECORD.*
