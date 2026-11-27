# RER R1a — CARRIER source and exact-algebra receiving assessment

**Date:** 26 November 2026. **Status:** [SESSION] / NONCANONICAL; ChatGPT preparer proposal, not a reviewer verdict or adoption. Checkpoint main cba0213e7ef04e6126ce87eac9c378c18f2ab30c. S0 and S1 integrated (#405/#408 and #409/#412). RER v0.2 remains unchanged; RER-ER2B-CARRIER remains BLOCKED_SOURCE_UNVERIFIED / EXCLUDED_BLOCKED until separate PI decision.

## 1. Source identity and reading

RER v0.2, rer-v0.2, §6 L676–714 and G7/G8; S0 custody and original adoption record. ER-2B v0.3, er2b-v0.3 annotated tag object 82e133922f86a62f9593f4447489c63da4f8e1d0 -> d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d, blob afbb3b87145d40049347f26cfcc9b880545cbd9d. SHA-256 80669c69ada042230c36883f5f1de7a0738e637793a4d1cf4b590990da57a134 freshly computed from decoded bytes; matches BASELINE (PI). Header explicitly NOT OWNER-ADOPTED; proposed current noncanonical reference, not adopted owner theorem. Read Part A in full, Part B §§1,4 C10–C14,5 C15A/B,C19/C20,C16 and §§8–10 targeted; other claims not re-audited. The text from §0 decision abstract through end equals the recovered v0.2 text (connector string equality), not its old header. v0.2 SHA-256 ea26d3d1a4853ac88d1938dcb66c76eda4d55980ebf6f4d61091b97d67b2bb5e.

Original evidence: upload/corpus-originals-20261123/RTG_ER2B_CONSOLIDATED_v0_2.zip, 170556 B, SHA-256 8c6352906143653a1736848e289da9765876927e3d2f089389c3a29326a048ee, freshly computed. Targeted extraction from ZIP root RTG_ER2B_CONSOLIDATED_v0_2/ (not execution):
| Member | SHA-256 | Inspection |
|---|---|---|
| RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md | ea26d3d1a4853ac88d1938dcb66c76eda4d55980ebf6f4d61091b97d67b2bb5e | matches loose source |
| MANIFEST.json | 92c884eb0fa174e4e499ad25ed1f12ff939f9674090b140164f0fb6f40f8cf05 | provenance and archive pins; not full manifest re-scan |
| repro/check_carrier_continuum.py | 48cf58ede5e0d54bb0e71897467dffc25c86c278a13d92b0a6e7fdd52f5c76e5 | targeted code passages: symbolic quadratic recurrence, continuum, threshold and response assertions |
| repro/check_iterate_family.py | 1b56c343d4c9d2462d7adeaac599be0ba454003b23da3ffc1f8fce50308891c1 | targeted method/assertion passages |
| evidence/carrier_continuum_checks.json | 5a7b8bb6157be756819760b3defebad2643fe61902ac3bdcec3b3d43d60a086a | full JSON |
| evidence/genesis_sixjet_obstruction_audit.json | 99c11cbe9a9e920dfee2d0de0925724787ca5c73c5ff1ce901e9da83ab041885 | identity and key inventory |
| evidence/original_review_archives/ER2B_OBSERVABLE_RESPONSE_v1.zip | 06d5e0c90d864ee8f5ab5ecfa7cadac5e76272a0b4754955bf43ecdcbc4b82b1 | member inventory and targeted C12 checker; historical Genesis pin |

Use ER-2B local keys, not owner RIDs. OFN v0.13 (ofn-v0.13) §5.5.4–5.5.5 and GEN v2.10 (gen-v2.10) §6.3a(d) L767 and §8 historical pin read; identity previously checked in S1. RRF v0.8.4 §0.3 read in S1; reference only. DYAD primitive map and exact smooth chart source as already checked in S1; no new owner theorem review. No archived script was executed here. Targeted selected-member checks are not full recursive archive validation.

## 2. Independent derivation and results

[SESSION] [ALG] Set A(rho,eta)=(rho-eta,rho), q=(0,rho^2/2), r=(eta^3/6,(rho^3+eta^3)/6). Write W=rho-eta/2+i sqrt(3) eta/2. On the zero-sum three-edge plane apply P=I-11^T/3 **at every primitive update**. For homogeneous state-degree jets L_j,B_j,C_j, recurrence from the primitive expansion is L'=A L, B'=A B+P q(L), C'=A C+P(Dq(L)B+r(L)); here A acts per edge, P is omitted for the isolated map. Initially B=C=0. No use of the source/reviewer checker code. The real polynomial-ring check uses exact QQ coefficients and symbolic k=1-sigma.

[SESSION] [ALG] C15A: H^{x3} maps C_H={sum H(z_e)=0} to the raw plane. Correct conjugacy preserves every iterate, and transported O_H=O o H^{x3} gives identical responses, including outward radial drift for N_H. C15B re-imposes sum z_e=0; it is not this conjugacy. In real coordinates the source h2 is (-rho^2/2+rho eta/2-eta^2/4,(-rho^2+eta^2)/4). Its homological cancellation is checked exactly. For the linearly closed real W triple (t,t,-2t) the raw closure sum after H is -(9+3i sqrt(3))t^2/4+O(t^3). Thus the domains already differ. The local chart exists by DH(0)=I; not a physical carrier.

[SESSION] [ALG] C19: the quadratic homological operator on complex monomials has eigenvalue lambda-lambda^a bar(lambda)^b or its conjugate, a+b=2. The monomial eigenvalues are lambda^2,1,bar(lambda)^2; neither output eigenvalue lambda=e^{i pi/3} or bar(lambda) coincides. Hence the real six-dimensional operator is invertible; arbitrary quadratic q in a tangent-identity chart is possible at this order. This does not classify physical carriers. The first isolated return cubic is invariant under such conjugacies (F=id+G3+O(4)); higher chart jets are not irrelevant to the full analytic coupled law.

[SESSION] [ALG] C20: H_sigma=id+sigma h2 gives q_sigma=k q_G. Its cubic is r_sigma=r+Dq*(sigma h2)-D(sigma h2)(A x)q_sigma, from T H_sigma=H_sigma Ttilde. The real exact check compares all six projected cubic components at arbitrary symbolic k and the isolated return. It recovers
    mu=-1/2-2i sqrt(3)/3,
    nu=-1/2+(2/3)k^2+i sqrt(3)(-2/3+k^2/3), chi=k^2/3.
The separate general-q script uses exact Q(i sqrt(3))[a,abar,b,bbar,u,ubar,v,vbar,t,tbar] and independently iterates the quadratic-composition sector on isolated and projected edges. It establishes all component identities
    mu22(q)=(9+3i sqrt(3))uv-(3+3i sqrt(3))v vbar-6 t tbar,
    chi(q)=(-6+2i sqrt(3))uv+(1+i sqrt(3))v vbar-4 t tbar,
    nu22=mu22/3.
For a direct cubic primitive term, the six-step sum is P times the isolated resonant cubic because A commutes with P. Thus nu=mu-2mu22/3, and higher h3 chart coboundaries telescope over six steps (A^6=I); the fixed isolated mu and quadratic jet suffice for this cubic comparison, not all orders. The generic chi formula was not checked in #416; this is an additional exact source check, not a new claimed RER import.

[SESSION] [ALG] Write N=3Qs/2+2Qc, S=Im(z bar(d)); the exact sharp bound is N^2-12S^2=(3Qs/2-2Qc)^2+12 I_sc^2. The independently iterated quartic response is
    Delta4 N=(-1/2+2k^2/3)N^2+2S^2,
    Delta4 S=(2/3)(-1/2+k^2)NS.
Uniform positive iff k^2>3/4, uniform negative iff k^2<1/2; mixed for 1/2<k^2<3/4. Along sigma in [0,1] the two thresholds are 1-sqrt(3)/2 and 1-1/sqrt(2), respectively. At the first threshold collinear directions are zero, at the second maximum-area directions zero. Strict quartic sign gives a sufficiently small neighbourhood for each fixed sigma by compactness of the unit sphere and analytic remainder; no quantitative radius or result along threshold-zero directions. No global basin claim.

## 3. C-2 naming and scope

ER-2B v0.3 A.4 explicitly compares the sigma=1 cubic with the FMS/OFN transported kappa-family, not C15A passive transport. OFN v0.13 §5.5.4 defines new mean-feedback in the transported chart and states its centre-manifold cubic. At kappa=1 on the flat closure plane the cubic agrees with the sigma=1 endpoint. The full coupled maps need not agree; no transfer of all-order, finite-radius or physical claims. A.4's historical formal-realization statement must be read through current DYAD smooth existence and OFN class-C C2 (real C-infinity, qualitative radius); analytic realization and physical selection OPEN. OFN §5.5.5 retains raw kappa=1 as a flat-sector reference. No transfer of RER raw results to class C.

## 4. Evidence and reconciliation proposal

Evidence: evidence/rer/r1/preparer/scripts/r1_exact_check.py and r1_general_q_check.py, exact output files under runs/, SHA256SUMS.txt. Executed here with Python 3.13.5 and SymPy 1.14.0 using python -I -B <script>; PASS. Scripts/results copied by identical Git blob from the executed local files. These are finite-degree exact algebra checks, not analytic certificates or native source-producer replay. The reviewer report synopsis was supplied before the preparer calculation; independent implementation, not blind review. Full #416 record at 90e45fcc3e7f7fc230e2a0b3e71278a105143d79 read after the first exact computation; independent numerical results agree. Native PI rerun in its §6 is reviewer-side execution, not mine.

**Proposed disposition: ACCEPT SCOPED**, subject to Claude's corrected-source reconciliation and separate ER-2B custodian decision. Agree with #416 C-1/C-2/C-3. If separately authorized for acceptance, cite current noncanonical ER-2B v0.3 Part B C15A/B,C19/C20, exact historical v0.2 source/archive and this evidence; replace only obsolete missing-source language, preserve the earlier receipt as history. Preserve C16 physical carrier selection, qualitative-radius/threshold-zero limitations, no native RRF profile, no physical clock or ontology. Do not infer adoption of the entire ER-2B study, owner science or broader C19/C20 imports merely from a receiving check.

Custodian question (PI): confirm v0.3 Part B as the current noncanonical reference for this claim set; confirm A.4 reading above. PI separately decides whether CARRIER enters a successor's accepted scientific scope. No change to 18+2, registry body or machine image now.
