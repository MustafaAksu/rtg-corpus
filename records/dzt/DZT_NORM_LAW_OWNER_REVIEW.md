# DZT — owner review of the norm law (DZT-OPEN-NORM-LAW)

**Status:** [SESSION] owner review record, for the second co-owner's review. **Not an adoption, not a grade.** Nothing in this record changes `dzt-v0.18`. `DZT-OPEN-NORM-LAW` stays open until the PI decides on the grade and on a new edition (§8).
**Date:** 19–20 November 2026. **Prepared by:** the DZT co-owner (Claude). **Independent review:** the second DZT co-owner (ChatGPT), triage row 2 (d).
**Governing edition:** `dzt-v0.18` (SHA-256 `04581d1e8d8a187ec231d670d9639591e2b8d3aefb9834d5dd9f5cdf792a8dee`).
- **Objects:**
  - §2 DZT-OPEN-0B-R `[RID: DZT-OPEN-NORM-LAW]`;
  - §6.3 `DZT-ALG-CASCADE-NORM` and `DZT-ALG-CASCADE-ANOMALY-SET`;
  - the §6.3 `[HYP]` mechanism of the mod-4 gate.
- **Authority:**
  - PI decision D3, 18 Nov 2026 ("LIT reviewed this cycle"; owner proof review of row 2; `records/dzt/DZT_REACTIVATION_TRIAGE.md` §7);
  - triage rows 2–5 and 19.
  - On 19 Nov 2026 the PI forwarded the second co-owner's execution plan for this review (23:46 +03:00). That plan fixes the order: this review first, then the B1 object.
- **Acceptance (triage row 2):**
  - (a) every proof step checked, including $p=2^k$, $p=3\cdot2^k$, the range $p\ge12$ with $p=8$ the zero degeneracy, rationality and the $\lvert N_+\rvert$ scope;
  - (b) the definition as in row 1;
  - (c) the evidence states;
  - (d) independent review;
  - (e) the PI's grade decision.

  This record answers (a)–(c) and prepares (e).

## 1. Sources

| # | Text | Bytes | Provenance |
|---|---|---|---|
| S1 | Odd-support proof note, `upload/dzt-recovery-20261116/received/originals/downloads/DZT_OPEN_0B_R_odd_support_proof_note.md` (= `… (1).md`), 197 lines | SHA-256 `9ce5e99f012319d5cd5d095ed32261857e009d905ed8cf9cf3274f7b6355a30f` | Recovered. Cited in the unadopted DZT v0.9–v0.17 texts as `DZT-ART-ODD-PROOF` for `DZT-THM-CASCADE-ODD-SUPPORT` (v0.17 lines 248, 302) |
| S2 | Denominator proof, `…/DZT_THM_CASCADE_DENOMINATOR_proof.md`, 40 lines | `2a8354ca43d9c33b443a4f8f5d8fdf03548304b39e22badf46aedd598c1b5e39` | Recovered. Cited as `DZT-PROOF-CASCADE-DEN` for `DZT-THM-CASCADE-DENOMINATOR` (v0.17 lines 108, 280) |
| S3 | LIT note `records/lit/dzt2026/DZT_NORM_LAW_PROOF_NOTE.md`, rtg-lit `8e2fb5cb7e39c5c4ab05b3008c4a51d03faed0f3` (the commit pinned by the 13 Nov offer) | `f3f7b1cc8d54e751bc39ad6914dc7a2ec02a67aaccb775cb392186ba17a589ce` | Offered to DZT (`pipes/DZT/20261113-LIT-norm-law-proof-candidate.md`). At rtg-lit `main` `89f952c` the file is `4458e82a…1db`: one lifecycle paragraph is added and the body is unchanged (checked with `git diff`) |
| S4 | LIT note `records/lit/dzt2026/DZT_NORM_SIGN_NOTE.md`, rtg-lit `da9d5bcb34e8a89bbe2ec1b409b178fe9a6a6873` | `43aed1ff1f1e1ad33181919cfde57dfeb4739f20bb6783cbe90b19d4ac817267` (unchanged at `89f952c`) | Filed as `pipes/DZT/20261118-LIT-norm-sign-supplement.md` |

**Statements under review.** v0.17 line numbers below are those of `…_v0_17.md`.
- **S1 (= v0.17 `DZT-THM-CASCADE-ODD-SUPPORT`).** For $p=4s\ge12$, the odd part of the numerator of $N_+(M_p)$ is $\ell^2$ if $p=8\ell^a$ with $\ell$ an odd prime and $\ell^a\equiv1\pmod4$. Otherwise it is 1.
- **S2 (= v0.17 `DZT-THM-CASCADE-DENOMINATOR`).** The denominator of $N_+(M_p)$ is $2^{d_p}$, where $d_p=\varphi(p)/4+[p=2^k]+[p=3\cdot2^k]$.
- **S3 (Proposition).** $N_+(M_p)^2=N_{\rm full}(p)=2^{-\varphi(p)/2}D(p)/(B(p)^4C(p))$, where:
  - $B=2$ iff $p=2^k$;
  - $C=4$ iff $p=3\cdot2^k$;
  - $D=\ell^4$ iff $p=8\ell^a$ with $\ell^a\equiv1\pmod4$, and $D=4$ iff $p=2^k$;
  - otherwise $B$, $C$ and $D$ equal 1.
- **S4.**
  - A real form of every conjugate of $M_p$.
  - $\operatorname{sign}N_+(M_p)=(-1)^{c_1+c_2}$.
  - A classification of the negative points, stated as a pattern for $p\le20000$.

## 2. Definitions and the imported input (row 1)

Let $p=4s$, $K=\mathbb Q(\zeta_p)$, $K^+=\mathbb Q(\zeta_p)^+$, $L=\zeta_p$ and $I=L^s$. Both $L$ and $I$ are **field elements**: a Galois automorphism $\sigma_a$ sends $I$ to $I^a$. Under the base embedding, $I=i$. The four sources compute norms over $K$ with $I$ moving under Galois, so all four use this reading. S4 states it explicitly (S4 §1).

- **Imported, Dyadic-owned:** the closed form $Q_p=L^5A_s/\big(2(L+1)^4(L^2+L+1)\big)$, where $A_s=IL^2+I-L^2+1$, for every $p=4s$ with $s\ge2$. Source: `[import: RTG_DYADIC_OSCILLATOR_DSN v6.4.24 §6.11 | DYAD-THM-Q403-PHASELAW]`, `[THM]`; DZT §7. This is the only non-elementary input. Every statement below is conditional on it.
- **Defined by DZT:** $M_p:=Q_p/(IL^3)$. DZT writes this as $Q_p/(i\zeta_p^3)$, which is the same element under the base embedding. Norms are defined as $N_{\rm full}:=N_{K/\mathbb Q}(M_p)$ and $N_+:=N_{K^+/\mathbb Q}(M_p)$.
- **Reality of $M_p$ — verified here, elementary given the closed form.** Complex conjugation $\sigma_{-1}$ sends $L\mapsto L^{-1}$ and $I\mapsto-I$. It gives:
  - $\sigma_{-1}(A_s)=-L^{-2}A_s$;
  - $\sigma_{-1}\big((L+1)^4\big)=L^{-4}(L+1)^4$;
  - $\sigma_{-1}(L^2+L+1)=L^{-2}(L^2+L+1)$.

  Hence $\sigma_{-1}(M_p)=\dfrac{L^{-2}\cdot(-L^{-2}A_s)}{2(-I)L^{-4}(L+1)^4L^{-2}(L^2+L+1)}=M_p$. So $M_p\in K^+$. The DSN states this at §6.3 as `[ALG]` `[scope: object-level, all p=4s≥12]`; this record confirms that it needs nothing beyond the closed form.

## 3. Step-by-step audit (criterion (a))

**Verdicts.**
- *Verified*: the step is correct as written and was checked line by line here.
- *Verified, with correction*: the conclusion used later is correct, but a sentence in the source is wrong; the correction is given.
- *Gap*: the step is correct but incompletely argued in that source; another source or this record supplies the argument.
- *Wrong*: the step is incorrect.
- *Not used*: the step does not enter the result.

| Step | Statement | S1 | S2 | S3 | Verdict and note |
|---|---|---|---|---|---|
| P1 | Roots of unity in $K$ have norm 1 ($p\ge3$), so $N_{K/\mathbb Q}(Q_p)=N_{K/\mathbb Q}(M_p)$ | l. 63 ("absolute norm 1") | l. 12 ("±1") | §1 | **Verified.** $N(\zeta)=\pm1$ in general; here every root of unity is a power of $L$, and $N(L)=\Phi_p(0)=1$ ($\varphi(p)$ even) |
| P2 | $M_p\in K^+$ gives $N_{K/\mathbb Q}(M_p)=N_+(M_p)^2$, since $[K:K^+]=2$ | l. 147–151 | l. 9–11 | (1) | **Verified.** Consequences: $N_{\rm full}\ge0$; $N_+$ is rational; $N_{\rm full}$ determines only $\lvert N_+\rvert$ |
| P3 | $A_s=(I-1)(L^2-I)$ (S1, S2), equivalently $A_s=(1+I)(1+IL^2)$ (S3 Lemma 2, from $1+L^s=1-L^{3s}$ and $1+L^{s+2}=1-L^{3s+2}$) | l. 51–61 | l. 15 | §2 | **Verified** by expansion with $I^2=-1$. The two factorizations differ by the unit $-I\cdot I=1$: $(1+I)=-I(I-1)$ and $(1+IL^2)=I(L^2-I)$. Exact check: A1 |
| P4 | $N(I-1)=N_{\mathbb Q(i)/\mathbb Q}(i-1)^{\varphi(p)/2}=2^{\varphi(p)/2}$ | l. 67–71 | l. 25–26 | table, row $1+L^s$ | **Verified.** Check A2. *Correction (triage row 5):* v0.17 (line 248 of `…_v0_17.md`, line 250 of `…_v0_17 (1).md`) calls $I-1$ "a unit factor … of 2-power norm"; S1 line 63 speaks of "the unit factor". $I-1$ is **not a unit**: its norm is $2^{\varphi(p)/2}$. S1 line 63 means the roots-of-unity factors $L^5$ and $IL^3$; the v0.17 wording is wrong |
| P5 | For $\eta$ of exact order $n>1$ with $n\mid p$: $N_{K/\mathbb Q}(1-\eta)=\Phi_n(1)^{\varphi(p)/\varphi(n)}$, where $\Phi_n(1)=\ell$ if $n=\ell^a$ and $1$ otherwise | l. 89–103 (stated as standard) | l. 27–29 (stated) | Lemma 1 (proved) | **Verified.** S3 proves it in full (the positivity and integrality argument, then transitivity of the norm). It is classical (`[MATH]`) |
| P6 | $L^2-I=L^2(1-L^{s-2})$ (S1); $L^2-I=I(L^{2-s}-1)$ (S2); $1+L^{s+2}=1-L^{3s+2}$ (S3). The relevant order is $n=p/\gcd(p,s-2)$. Note $3s+2\equiv-(s-2)\pmod{4s}$, so all three give the same order | l. 75–85 | l. 27 | §3 | **Verified.** S1 writes "$\cdot(\text{unit})$", which is harmless: the identity is exact without it. $1-L^{s-2}\ne0$ because $0<s-2<p$ for $s\ge3$ |
| P7 | The value of $D(p)=N(L^2-I)$ | l. 105–145 (odd part only) | l. 27–31 (2-part only) | §3 (complete) | **Verified, with a gap in S1.** Write $p=2^\alpha m$ with $m$ odd. <br>• $\alpha=2$: $n=4m=p$, which is not a prime power ($m\ge3$), so $D=1$. <br>• $\alpha\ge4$: $v_2(s-2)=1$ and $\gcd(m,s-2)=1$, so $n=2^{\alpha-1}m$. Then $D=4$ iff $m=1$ (with $\varphi(p)/\varphi(n)=2$), else $D=1$. <br>• $\alpha=3$, $p=8q$: $\gcd(8q,2(q-1))=2\gcd(4,q-1)$, so $n=q$ if $q\equiv1\pmod4$ and $n=2q$ if $q\equiv3$. Then $D=\ell^4$ iff $q=\ell^a\equiv1\pmod4$ (with $\varphi(8q)/\varphi(q)=4$); $q=1$ ($p=8$) gives $n=1$ and the zero. <br>S1 shows only "$n$ even" for $\alpha\ne3$. That suffices for the odd part, but not for the value 4 at $p=2^k$, which S2 and S3 supply. S2's "forces $m=1$" is correct ($m\mid 2$). Its range $k\ge4$ is implicit ($p\ge12$). Check A3 compares all three forms |
| P8 | $N(1+L)=\Phi_p(-1)=B(p)$ | l. 173: "$=1$ for $4\mid p$" | l. 19–20 | table | **S1 wrong at $p=2^k$ (triage row 4); S2 and S3 verified.** $1+L=1-L^{1+2s}$ and $\gcd(1+2s,4s)=1$, so the order is $p$ and $N=\Phi_p(1)$: 2 iff $p=2^k$, else 1. $\Phi_{2^k}(-1)=2$. The error leaves S1's odd-part conclusion intact (the value is a power of 2). Correction: "$N(L+1)=\Phi_p(-1)=2$ if $p=2^k$, and $1$ otherwise ($4\mid p$, $p\ge12$)". Check A4 |
| P9 | $N(L^2+L+1)=C(p)$ | l. 174: "1 or a power of 2" (unproved) | l. 22–24 (Apostol, cited) | §3 (via P5) | **Verified; S1 has a gap, which S2 or S3 closes.** S3 is self-contained, using $L^2+L+1=(1-L^3)/(1-L)$: <br>• if $3\nmid p$, both orders are $p$ and $C=1$; <br>• if $p=2^k$, both norms are 2 and $C=1$; <br>• if $p=3\cdot2^k$, $C=2^{\varphi(p)/\varphi(p/3)}/1=4$; <br>• otherwise $C=1$. <br>S2 cites Apostol's theorem: for $m>n>1$, $\mathrm{Res}(\Phi_m,\Phi_n)=r^{\varphi(n)}$ if $m/n$ is a power of a prime $r$, else 1. Apostol (1970) was not opened for this review; S3's derivation makes it unnecessary. Check A5 |
| P10 | Assembly: $N_{\rm full}=N(A_s)/\big(N(2)N(L+1)^4N(L^2+L+1)\big)=2^{\varphi/2}D/(2^{\varphi}B^4C)$ | odd part l. 141–157 | l. 33–36 | Proposition | **Verified.** $N_{\rm full}$ is the square of a rational, because $4\mid\varphi(p)$ for $4\mid p$, $p\ge12$, and $D,B^4,C$ are squares. Hence: <br>• the odd part of the numerator of $\lvert N_+\rvert$ is $\ell^2$ or 1 (S1); <br>• the denominator is $2^{d_p}$ (S2), and $d_p\ge1$, so the 2-adic valuation sits wholly in the denominator; <br>• S3 holds in full. <br>The cases $p=2^k$, $p=3\cdot2^k$ and $p=8\ell^a$ are pairwise disjoint: $8\ell^a=3\cdot2^k$ would need $\ell^a=3$, which is $\equiv3\pmod4$. Checks A6–A8 |
| P11 | Range | l. 9 | l. 3 | §1, §3 | **Verified.** <br>• $p=8$: $n=1$, $A_2(\zeta_8)=0$, $Q_8=0$, the zero degeneracy (check A10). <br>• $p\ge12$: all factors are nonzero. $L+1\ne0$; $L^2+L+1\ne0$ because $p\ne3$; $1-L^{s-2}\ne0$. <br>• v0.17 line 108 writes "$(k\ge2)$" for both brackets. Within $p\ge12$, $[p=2^k]$ fires only for $k\ge4$; the statement is right but the qualifier is loose |
| P12 | Sign | — | — | §1: "not determined" | **Not determined by S1–S3.** Their statements are about $\lvert N_+\rvert$. For a rational number, "odd part of the numerator" and "denominator" do not depend on the sign, so S1 and S2 hold for the signed $N_+$ in that sense. S3's formula is for $N_+^2$ |

**Combined statement** (S1, S2 and S3 together, conditional on the imported closed form). For every $p=4s\ge12$:
$$\lvert N_+(M_p)\rvert=\frac{\ell(p)^2}{2^{d_p}},\qquad d_p=\frac{\varphi(p)}4+[p=2^k]+[p=3\cdot2^k],$$
where $\ell(p)=\ell$ if $p=8\ell^a$ with $\ell$ an odd prime and $\ell^a\equiv1\pmod4$, and $\ell(p)=1$ otherwise.

This single formula contains both recovered statements and the LIT Proposition. On the anomaly set it gives $\lvert N_+(M_{8\ell^a})\rvert=\ell^2/2^{\varphi(\ell^a)}$.

**Rationality.** $N_+\in\mathbb Q$ (P2). Every value is exact (check A6). The 14 values of DZT §6.3 and the 248 rows $p=12$–$1000$ of the recovered CSV agree with the formula (check A9).

**Verdict on criterion (a).** The proof of the combined statement is **complete and correct, conditional on the imported closed form**. Every step is verified in at least one source, and S3 alone is complete. S1 has one wrong sentence (P8, triage row 4) and two gaps (P7, P9). The gaps are closed by S2 and S3 and do not affect S1's conclusion. v0.17 has one wrong word (P4, triage row 5). S2 has no error.

## 4. The sign (S4)

- **Real form `[ALG]` — verified.** Here $\theta=2\pi a/p$, $\varepsilon_a=i^{a-1}$, and $\sigma_a(I)=i^a$. From the closed form:
  - $I(L^2+1)-(L^2-1)=2iL(\varepsilon\cos\theta-\sin\theta)$;
  - $(L+1)^4=16L^2\cos^4(\theta/2)$;
  - $L^2+L+1=L(1+2\cos\theta)$.

  So $\sigma_a(M_p)=(\cos\theta-\varepsilon_a\sin\theta)/\big(16\cos^4(\theta/2)(1+2\cos\theta)\big)$, as stated. This also proves $M_p\in K^+$ once more, because the value is real.
- **Sign as a count `[ALG]` — verified.** On the half-system $0<a<p/2$ with $\gcd(a,p)=1$:
  - $\cos^4(\theta/2)>0$;
  - $1+2\cos\theta<0$ iff $a>p/3$;
  - $\cos(\theta+\varepsilon\pi/4)<0$ iff $a>p/8$ (for $\varepsilon=+1$) or $a>3p/8$ (for $\varepsilon=-1$).

  The zeros fall on non-units, except at $p=8$. Hence $\operatorname{sign}N_+(M_p)=(-1)^{c_1+c_2}$ for every $p=4s\ge12$.
- **Checks B and C.**
  - The sign at the 14 table points: negative at $p=16,20,24,32,36,44,48,52,64$; positive at $12,28,40,56,60$. This agrees with S4 §4 and with the reading record §9.3.
- **The classification of S4 §5 is `[NUM]`, not proved.** The negative points are:
  - $p=2^k$ ($k\ge4$);
  - $p=3\cdot2^k$ ($k\ge3$);
  - $p=4\ell^a$ with $\ell\equiv\pm3\pmod8$ and $p\ne12$.

  S4 checked it for $p\le20000$ (378 negative points). This record checks it independently for $p\le100000$: 24,998 points, 1,456 negative, no exception (check C). A proof needs the parity of the interval counts $c_1, c_2$. Neither S4 nor this record supplies one.

## 5. The `[HYP]` mechanism (triage row 3)

DZT §6.3 states the `[HYP]` (also in §2): "the $\equiv1\pmod4$ gate is the reality of $\mathbb Q(\sqrt q)\subset\mathbb Q(\zeta_q)^+$".

The proved mechanism is different: it is the order of the root of unity in the factor $L^2-I$ (P7). For $p=8q$, that order is $q$ when $8\mid s-2$, that is when $q\equiv1\pmod4$, and $2q$ otherwise. $1-\eta$ is a non-unit only when the order of $\eta$ is a prime power. No quadratic subfield enters.

The `[HYP]` also fails at $p=72$ ($q=9$): it is an anomaly ($\lvert N_+\rvert=9/64$), but $\sqrt9$ is rational and $\mathbb Q(\zeta_9)^+$ is cubic. The same holds for every $q=\ell^{2b}$.

**Recommendation to the owner/PI:** retire the `[HYP]` at the next edition, into Appendix B with this reason (order condition; $q=9$).

## 6. Evidence states (criterion (c))

| Artifact | Bytes (recovered) | State | What it shows, from its text |
|---|---|---|---|
| `dzt_odd_support_proof_check.py` (`DZT-ART-ODD-PROOF-CHECK`) | `8cf67b9a62381e7f6423a98fe77ba5b6846461e4955e7c642fcd881fb8128bae` | `EV-BYTES`; `EV-NOT-RERUN` | It compares the odd numerator predicted by the order formula with the CSV (248 rows) and the multiplicity 4. The exit 0 is source-reported |
| `dzt_0b_den_law_check.py` (= `(1)`; `DZT-ART-0B-DEN-CERT`) | `54c02ce01d9559348782d62e4f98708c69fcb2832c01f0db9d42fa19f5fd64f1` | `EV-BYTES`; `EV-NOT-RERUN` | It compares $d_p$ with the CSV and checks the 2-adic valuations of $\Phi_p(-1)$ and $\mathrm{Res}(\Phi_p,\Phi_3)$. It does **not** check $N(I-1)$ or $N(L^2-I)$. Its docstring attributes $+[p=2^k]$ to $N(1+L)$ alone; in S2 that term is $4-2$ (from $(1+L)^4$ and $L^2-I$), halved. The input path is the session path `/mnt/user-data/outputs/…`. v0.17 line 280 says "every norm-valuation lemma certified" and S2 line 39 says "each intermediate valuation also verified". **No received script does that; UNVERIFIED** (a missing artifact, not a refutation) |
| `dzt_casev_norm_closed_form_p8_1000.csv` | `d9dd7bd90bb9fd2340f6e5259129437db4850d5c057be0d5f527bbc78183555a` | `EV-BYTES`, read as data | It records $\sqrt{\lvert N_{\rm full}\rvert}$ (reading record §9.2). It equals the exact values of check A9 on all 248 rows |
| `dzt_anomaly_rule_check.py`, `dzt_casev_norm_from_closed_form.py` | as cited in DZT §8 | `EV-BYTES`; `EV-NOT-RERUN` | Finite-horizon evidence of `DZT-ALG-CASCADE-ANOMALY-SET`; unchanged by this review |
| LIT `dzt_norm_law_check.py`, `dzt_norm_sign_check.py` and their outputs (rtg-lit) | in rtg-lit | `EV-SRC-REPORTED` | Not run here |

No recovered script and no LIT script was executed for this review.

**This review's own check.** `evidence/dzt/norm_law_review/dzt_norm_law_review_check.py` (SHA-256 `566867bb541cd3f5cb4fb1aa11c43ddd4f9b9c0a1e5149697c35a805ac4cebb7`) was written for this review from the definitions in §2. It ran on Python 3.13.18 with python-flint 0.9.0, mpmath 1.4.1 and numpy 2.5.3.
- **Part A, exact.** Integer resultants $N_{K/\mathbb Q}(f(L))=\mathrm{Res}(\Phi_p,f)$ for $12\le p\le4000$ (998 points), plus $p=8$. It checks A1–A8:
  - the factorization;
  - $N(I-1)$;
  - $D$ in three forms;
  - $B=\Phi_p(-1)$;
  - $C$;
  - the LIT Proposition;
  - the odd numerator;
  - the denominator.

  A9 compares with the CSV and the §6.3 table, and A10 checks $p=8$. The run finds 53 anomaly points up to 4000, of which 20 are $\le1000$.
- **Part B, numeric.** For $12\le p\le1000$ (248 points), the product of the conjugates from the complex closed form at 50 digits. It is checked against Part A (maximum relative error $2.7\cdot10^{-47}$), against S4's real form ($2.1\cdot10^{-46}$), and its sign against $(-1)^{c_1+c_2}$.
- **Part C.** The S4 pattern for $p\le100000$.
- **Result.** `python3 -I evidence/dzt/norm_law_review/dzt_norm_law_review_check.py 4000 1000 100000` gives **PASS**, 0 failures, in about 100 s. Output: `check_output_4000_1000_100000.txt` (`2cc86b9e…188f`).
- **Negative controls** (`negative_controls.py`, output `negative_controls_output.txt`): **PASS**. Each of six mutated laws fails on the expected check:
  - the gate $3\bmod4$;
  - $d_p$ without $[p=2^k]$;
  - S1's $N(L+1)=1$;
  - $I-1$ as a unit;
  - the sign from $c_1$ alone;
  - the pattern with $\ell\equiv3,7\pmod8$.

  The unmutated check passes.

A finite check supports only its range. The all-$p$ claim rests on the written proof (§3).

## 7. Corrections and discrepancies found

1. **S1 line 173:** "$N(L+1)=\lvert\Phi_p(-1)\rvert=1$ for $4\mid p$" → "$=2$ if $p=2^k$, $1$ otherwise" (row 4; P8).
2. **v0.17 (line 248 of `…_v0_17.md`; line 250 of `… (1).md`):** "unit factor $I-1$" → "$I-1$, of norm $2^{\varphi(p)/2}$ (not a unit)" (row 5; P4).
3. **v0.17 lines 280 and S2 line 39:** the claimed certification of every norm valuation is not backed by a received script (§6).
4. **v0.17 line 108:** "$(k\ge2)$" should read $k\ge4$ for $[p=2^k]$ within $p\ge12$; it stays $k\ge2$ for $[p=3\cdot2^k]$ (P11).
5. **LIT headers (row 19).**
   - S3 line 5 still says "Not reviewed … Not offered". The lifecycle paragraph at line 3, added on 18 Nov, records the review and the offer, but the status line itself is unchanged.
   - S4 line 3 says "Not yet reviewed by the second co-owner. Not offered to DZT". The pipe item records review `5953634022` (rtg-lit PR #121) and the filing.

   These are LIT actions. DZT does not edit rtg-lit; they are named in DZT's reply to LIT after the PI's decision.

## 8. For the PI (criterion (e)) — options, not a decision

The review supports, for the PI to decide:

- **Grade of the combined statement (§3).** The proposal is `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` `[proof: written derivation]`, with the classical inputs (P5) as `[MATH]`.
  - Methodology §8.1 defines `[THM]` as "a complete mathematical proof of the stated proposition under explicit assumptions"; the assumption is the imported closed form.
  - The alternative is `[ALG]` `[assuming: …]`. It is equally admissible, but understates a general proof.
- **Identifiers — two options.**
  - (A) One DZT record for the combined formula. This needs a new RID, chosen by the PI or owner.
  - (B) The two recovered RIDs `DZT-THM-CASCADE-ODD-SUPPORT` and `DZT-THM-CASCADE-DENOMINATOR`, with the corrected wording. Under D1 recovered content enters only by decision, so (B) is a decision, not a default.
- **Effect on the edition.** If adopted, a later edition would:
  - close `DZT-OPEN-NORM-LAW` with the chosen RID(s);
  - keep `DZT-ALG-CASCADE-ANOMALY-SET` as the finite-horizon record or mark it subsumed;
  - retire the `[HYP]` (§5);
  - record corrections 1–2 of §7 as correction records.

  The sign stays out of the theorem. If the owner wants it, the real form and count of §4 could enter as `[ALG]` (with LIT credit), and the classification stays `[NUM]` `[scope: p≤100000]` or out.
- **LIT disposition.** The 13 Nov offer stays `acknowledged` until the PI decides. Then DZT's reply goes to `pipes/LIT/`: what is verified, the corrections, the header discrepancies (§7.5) and the disposition.

Not decided here: no grade, no closure, no RID, no edition.
