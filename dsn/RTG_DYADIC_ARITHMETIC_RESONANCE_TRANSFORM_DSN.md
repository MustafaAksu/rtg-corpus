# RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.18

**Title:** RTG Dyadic Arithmetic-Resonance Transform Study — Founding Charter and Diagnostic Ledger
**Date:** 18 November 2026
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok
**Scope:** Arithmetic transforms (cyclotomic resultants and real-subfield norms) over Dyadic-owned OPEN 9 $p$-resonance observables, and the diagnostics they produce; no Dyadic result is re-owned, no AZ graph-zeta result transfers, and nothing is claimed about the Riemann Hypothesis or prime distribution.
**Document class:** Technical scientific ledger (Methodology v1.4 §0.5), standard layout. Short name: *Dyadic Zeta/Arithmetic Transform (DZT)*.
**Programme tier:** Tier 3 — Continuous Programme, downstream diagnostic of Dyadic. Maturity **Level A** (defined model; exploration begun). All results inherit the OPEN-P0 ceiling (SG-PROG-2 / SG-DZT-6).
**Document status:** ADOPTED — PI, 19 November 2026 (corrections and synchronization after the reactivation triage, list (i); Methodology v1.4 layout; no new claim, no grade raised). Adoption record: `records/dzt/DZT_v0_18_RELEASE_RECORD.md`.
**Supersedes:** `RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN` v0.8 (tag `dzt-v0.8`, SHA-256 `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2`)
**Companion documents:** Programme Overview v1.4 (`programme-v1.4`) · Dyadic Oscillator v6.4.24 (`dyad-v6.4.24`; source of truth for all OPEN 9 arithmetic) · Arithmetic Resonance and Zeta v0.10 (`az-v0.10`; discrete branch, quarantined, see SG-DZT-1) · Ontological Foundations v0.12 (`ofn-v0.12`)
**DSN Methodology:** v1.4 (`methodology-v1.4`)
**§1 length:** above the 500-word target of Methodology §1, because §1 states the three founding `[DEF]` records of the study (transform, channel state, ambient field) in full.

**Status summary:** This study defines a transform on Dyadic-owned OPEN 9 arithmetic. DZT-OPEN-0A is closed at finite-horizon scope (all three rows: $b=5$ survival, $b\le4$ structural absence, cascade $(4,(0,3))$). The active frontier is DZT-OPEN-0B-R: prove or reject the anomaly rule for all $p$ from a resultant identity (§2). No Dyadic result is re-owned here; no AZ Thread-C graph-zeta result transfers; no OPEN-M amplitude or RH/prime claim is made.

## Local Tag Aliases

Status tags follow DSN Methodology v1.4 §8.1 and §8.3; qualifiers follow its §3.2. The entries below are local to this document.

| Local alias | Canonical expansion | Use |
|---|---|---|
| `[NUM diagnostic]` | `[NUM]` `[scope: named diagnostic campaign]` | Finite numerical evidence (Methodology §8.4) |

Labels that are not status tags:

- `[import-ref]` marks a reference to a result owned by another DSN (Methodology §4.3). A status tag printed next to it is the owner's tag at the pinned edition (§7); ownership is not transferred.

**Standard clause** (Methodology §1.1, rule 5):

- **[RECOVERED]** — the bytes were received unchanged with the DZT recovery (PR #289; plain files PR #308) and are in `upload/dzt-recovery-20261116/received/originals/downloads/`; their SHA-256 equals the recovery manifest `upload/dzt-recovery-20261116/received/MANIFEST.json` (`EV-BYTES`, `EV-HASH`). The run recorded in this document is source-reported (`EV-SRC-REPORTED`) and was not repeated for this edition (`EV-NOT-RERUN`); the bytes are not shown to be those of the recorded run.

---

## §1. Current Canonical State {#sec-1-canonical-state}

`[DEF]` **Study object.** This study constructs *arithmetic transforms* over Dyadic-owned $p$-resonance observables and asks whether transform-level structure (zero locus, resultant factorization, field norm, valuation pattern, special value, functional relation) maps onto — or predicts — certified Dyadic OPEN 9 facts. It does not study the Riemann zeta function and does not assert any result about classical prime distribution (SG-DZT-4).

`[DEF]` **Primary object — Track A (cyclotomic channel transform).** For a *fixed* Dyadic channel $C$ (either $C=b$ in the raw anti-holomorphic family $(0,b)$, or $C=(q,D)$ in the cascade family) with Dyadic-owned channel polynomial or algebraic channel value $P_C(x)$, define
$$R_C(p) \;=\; \mathrm{Res}\big(\Phi_p(x),\,P_C(x)\big) \;=\; \prod_{\zeta:\ \Phi_p(\zeta)=0} P_C(\zeta),$$
the product taken over primitive $p$-th roots of unity ($\Phi_p$ monic, so the resultant equals the bare product). `[ALG]` $R_C(p)=0 \iff \Phi_p \mid P_C \iff P_C(\zeta_p)=0$ for $P_C\in\mathbb{Q}[x]$. The transform is **channel-fixed**: the science lives in how the family $\{R^{(b)}\}$ / $\{R^{(q,D)}\}$ varies with the channel, not in a mixed $p$-table. `[RID: DZT-DEF-CHANNEL-TRANSFORM]`

`[HEUR]` **Secondary object — Dirichlet diagnostic (demoted).** A series $\sum_p A_C(p)\,p^{-s}$ is admissible only after $A_C(p)$ is *defined from* the native cyclotomic object (e.g. $A_C(p)=\mathrm{sgn}\,R_C(p)$, $v_\ell(R_C(p))$, $\log|R_C(p)|/\varphi(p)$, or a vanishing indicator). It is not the primary transform and carries no classical-zeta implication (SG-DZT-4).

`[DEF]` **Two-layer channel state.** A resultant zero and a structural (secular-absence) zero are different events and must not be conflated. For a fixed channel $C$ and horizon $p$:
$$E_C(p)\in\{0,1\}\ \text{(secular-content indicator)},\qquad P_C(x)\ \text{and}\ R_C(p)=\mathrm{Res}(\Phi_p,P_C)\ \text{defined only when}\ E_C(p)=1.$$
Three classes:
- $E_C(p)=0$ — **structural/secular absence** (no source $\beta$-set contains the secular mode; the channel output vanishes identically). This is the $b\le4$ case for $p\ge b+2$ (Dyadic DYAD-ALG-VANISH-B2, DYAD-ALG-VANISH-B3, DYAD-ALG-VANISH-B4).
- $E_C(p)=1,\ R_C(p)=0$ — **cyclotomic cancellation** ($\Phi_p\mid P_C$).
- $E_C(p)=1,\ R_C(p)\ne0$ — **cyclotomic survival**. This is the $b=5$ case (§6.2).

The transform never encodes structural vanishing as a resultant zero. `[RID: DZT-DEF-CHANNEL-STATE]`

`[DEF]` **Ambient field.** For channel $C$ at horizon $p$ the honest default setting is the compositum
$$K_{C,p}=F_C\cdot\mathbb{Q}(\zeta_p),$$
where $F_C$ is the Dyadic coefficient field fixed by the source convention and $\mathbb{Q}(\zeta_p)$ is the $p$-step cyclotomic field. **Cascade correction:** for the $q=4,(0,3)$ cascade family the channel value is generically complex and lives in the full $\mathbb{Q}(\zeta_p)$; the natural real invariant is taken in the **maximal real subfield $\mathbb{Q}(\zeta_p)^+$** (degree $\varphi(p)/2$ over $\mathbb{Q}$), via $M_p=Q_p/(i\zeta_p^3)\in\mathbb{Q}(\zeta_p)^+$ and the norm $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)$. The earlier "coefficients in $\mathbb{Q}(\sqrt3)$" reading is a **$p=12$-only** artifact: $\mathbb{Q}(\zeta_{12})^+=\mathbb{Q}(\sqrt3)$, whereas $p=8$ is the zero degeneracy ($Q_8=0$, and $\mathbb{Q}(\zeta_8)^+=\mathbb{Q}(\sqrt2)\ne\mathbb{Q}(\sqrt3)$). It is not the family law. `[RID: DZT-DEF-AMBIENT-FIELD]`

`[ALG]` **$p=12$ reduced norm.** The certified cascade value $v=-13+\tfrac{15\sqrt3}{2}$ (Dyadic, channel $(4,(0,3))$, $p=12$) has $N_{\mathbb{Q}(\sqrt3)/\mathbb{Q}}(v)=\tfrac14$; it is the $\varphi(12)/2=2$ case of the amplitude norm below. Statement: §6.3, DZT-ALG-P12-NORM.

`[ALG]` `[scope: validation table p=12–64, 14 points]` **Amplitude norm.** With $M_p=Q_p/(i\zeta_p^3)\in\mathbb{Q}(\zeta_p)^+$ (Dyadic all-$p$ factorization, DYAD-THM-Q403-PHASELAW), $\lvert N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)\rvert$ is rational at every audited point. The tabulated values are absolute values; their sign is not determined here. The canonical computation is the closed-form audit for $p\le1000$. Statement and values: §6.3, DZT-ALG-CASCADE-NORM.

`[ALG]` `[scope: finite horizon p≤1000, 249 points]` **Odd-prime anomalies.** On the audited range the values with an odd prime in their numerator are exactly those at $p=8\ell^a$ ($\ell$ an odd prime, $\ell^a\equiv1\!\pmod4$; 20 points), with numerator $\ell^2$; on the 14-point table the only such point is $p=40$. Statement: §6.3, DZT-ALG-CASCADE-ANOMALY-SET.

`[FAIL]` **Support-on-2 hypothesis.** The hypothesis that the amplitude norm is a pure power of 2 for all $4\mid p$ is false ($p=40$ gives $\tfrac{25}{16}$). Record: §6.3 and Appendix B, DZT-HYP-MAHLER-NEARMISS.

`[OPEN]` **Frontier.** DZT-OPEN-0A is closed at finite-horizon scope (all three rows: $b=5$ survival, $b\le4$ structural absence, cascade $(4,(0,3))$). The active frontier is DZT-OPEN-0B-R: prove or reject the anomaly rule for all $p$ from a resultant identity (§2). Then the Track B objects.

---

## §2. Active Frontier / OPEN Registry {#sec-2-open-registry}

### Priority ordering
1. **DZT-OPEN-0A** — cyclotomic reproduction audit. CLOSED at finite-horizon scope: $b=5$ survival, $b\le4$ structural absence, and cascade $(4,(0,3))$ Case-V norm row all done.
2. **DZT-OPEN-0B-R** — prove or reject the corrected resultant pattern: $\lvert N_+(M_{8q})\rvert$ has odd-prime support iff $q=\ell^a$ is a prime power with $q\equiv1\!\pmod4$, with numerator $\ell^2$. Verified `[ALG]` `[scope: finite horizon p≤1000, 249 points]`; candidate mechanism `[HYP]` (below and §6.3).
3. **DZT-OPEN-B1** — formal local NF/dynamical zeta near $P_1$ (algebraic, near-term).
4. **DZT-OPEN-B2** — analytic transfer/Ruelle zeta of the global map (deferred analytic frontier).

---

**DZT-OPEN-0A — Cyclotomic reproduction audit** [RID: DZT-OPEN-REPRODUCTION-AUDIT]

Status: CLOSED at finite-horizon scope (all three rows: $b=5$ survival, $b\le4$ structural absence, cascade $(4,(0,3))$) | Owner branch: this DSN

Question: For each fixed channel $C$ with Dyadic-owned certification, construct $P_C$ and compute $R_C(p)=\mathrm{Res}(\Phi_p,P_C)$ over the certified horizon set $p=5,6,7,8,10,12$ (plus the finite $\varphi(p)\le6$ exception set where relevant). Does the transform reproduce certified zero/nonzero statuses *and* expose mechanism (SG-DZT-8)?

Closed sub-items:
- $b=5$ channel ($P_C=N=2x^6+x^5-5x^4-3x^3-4x^2+2x+1$): $R_{(0,5)}(p)\ne0$ for all $p\in\{6,7,8,10,12,13,14,30\}$, reproducing imported all-$p$ survival on the tested horizon; carries arithmetic size. `[RESULT]` `[from: ALG]` `[scope: finite horizon sweep]` ✓ [RID: DZT-ALG-B5-RESULTANT]
- $b\le4$ structural-absence encoding: for $b\in\{2,3,4\}$ at $p\ge b+2$, the transform reports $E_{(0,b)}(p)=0$ (structural/secular absence) with no $P_C$ and no resultant defined — distinct from a cyclotomic cancellation $R_C=0$. Certified against the $b=5$ $E_C=1$ contrast class by `dzt_channel_audit.py` (exit 0). `[ALG]` `[scope: DZT channel-state encoding test]` ✓ [RID: DZT-ALG-B234-STRUCTURAL]
- Cascade $(q,D)=(4,(0,3))$ (finite horizon): using the Dyadic-emitted Case-V values (Dyadic extractor DYAD-ART-Q403-EXTRACT; §7), DZT reproduces $p=8$ cancellation and the $p=12$ value $-13+\tfrac{15\sqrt3}{2}$, and registers the transform as the real-subfield norm in $\mathbb{Q}(\zeta_p)^+$ (not a $\Phi_p$-resultant: the channel is Case V, a per-$p$ algebraic value, not a single polynomial). The amplitude norm $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)$ is rational at all points; its absolute value is a 2-power on $p=12$–$36$ and $p=44,48,52$ but $5^2\cdot2^{-4}$ at $p=40$ (DZT-ALG-CASCADE-NORM, §6.3). `[ALG]` `[scope: finite horizon]` ✓ [RID: DZT-ALG-CASCADE-ROW]

Active sub-items: none — the reproduction audit is complete. The norm-mechanism question (post-falsification) is tracked under DZT-OPEN-0B.

Pass: reproduces certified zero/nonzero exactly; separates $E_C=0$ structural vanishing ($b\le4$) from $E_C=1$ cyclotomic survival ($b=5$); registers $p=12,(4,(0,3))$ as algebraically nonzero with its reduced-norm diagnostic.
Fail: collapses to prime/composite classification; mixes channels; encodes structural vanishing as a resultant zero; depends on a $\lambda_6=\zeta_p$ substitution outside $p=6$ (SG-DZT-7); cannot reproduce a certified status.

Next required artifact: none (audit complete). With the Dyadic (R)-link now closed, the factorization is all-$p$; the remaining all-$p$ work (DZT-OPEN-0B-R) is the **DZT-native** resultant-identity proof and no longer depends on any upstream gate.

Dependencies: Dyadic OPEN 9 channel polynomials/values (Import Ledger §7).

---

**DZT-OPEN-0B-R — Corrected odd-prime anomaly law (resultant pattern)** [RID: DZT-OPEN-NORM-LAW]

Status: ACTIVE (corrected pattern verified finite-horizon; all-$p$ proof open)
Verified `[ALG]` `[scope: finite horizon p≤1000, 249 points]`: computing $\lvert N_+(M_p)\rvert$ from the Dyadic closed form via $N_{\rm full}=\mathrm{Res}(\Phi_p,A_s)/[2^{\varphi(p)}\mathrm{Res}(\Phi_p,L{+}1)^4\mathrm{Res}(\Phi_p,L^2{+}L{+}1)]$ with $A_s=L^{s+2}+L^s-L^2+1$, the odd-prime anomalies are **exactly** $p=8\ell^a$ with $\ell^a\equiv1\!\pmod4$ (the 20 points $40,72,\dots,1000$), and the numerator is exactly $\ell^2$. Machine-verified `dzt_anomaly_rule_check.py` (exit 0, 0 mismatches over 249 rows).
Correction of import: the note's "every odd prime power $q$" is **false** — $q\equiv3\!\pmod4$ prime powers ($p=24,56,88,152,184,216$) are clean 2-powers; the $\equiv1\!\pmod4$ condition is required. The note's $N_+=2^{-\varphi(q)}$ denominator claim is also not general (fails off prime-powers); **no denominator formula is asserted**.
Open target: prove or reject the corrected rule from a resultant identity for $\mathrm{Res}(\Phi_{8q},A_s)$. With the Dyadic phase law proved for all $p$ (DYAD-THM-Q403-PHASELAW), the factorization and hence the norm object $M_p\in\mathbb{Q}(\zeta_p)^+$ are defined for all $p=4s\ge12$, so this is a fully **DZT-native** problem (a cyclotomic resultant identity) with no outstanding upstream gate: the resultant proof is DZT-owned, conditional on the imported Dyadic factorization at `dyad-v6.4.24`. The anomaly law itself stays `[ALG]` `[scope: finite horizon p≤1000]` until the identity is proved. Candidate mechanism (`[HYP]`): the $\equiv1\!\pmod4$ gate is the reality of $\mathbb{Q}(\sqrt q)\subset\mathbb{Q}(\zeta_q)^+$ — for $q\equiv1$, $\sqrt q$ is real and $\ell$ enters $N_+$; for $q\equiv3$, only $\sqrt{-q}$ (imaginary) lies in $\mathbb{Q}(\zeta_q)$, excluded from the real-subfield norm.
Standing falsifier: any $p\le1000$ violating the rule (none found); any larger $p$ with odd-prime support off the predicted set.

---

**DZT-OPEN-B1 — Formal local NF/dynamical zeta near $P_1$** [RID: DZT-OPEN-LOCAL-FORMAL-ZETA]

Status: OPEN (algebraic, near-term)
Question: Define a formal zeta/NF determinant built on the finite-order linear part ($A^6=I$, $\lambda_6=e^{i\pi/3}$), the six-step strobe, $Q_{\rm true}$, $c_{21}$, and certified NF coefficients — a *local* object near the order-6 elliptic point, never the global map. The periodic/formal-orbit structure of a finite-order-plus-NF germ is rigid and needs no function space.
Candidate form: $\zeta_{\rm loc}(z)=\exp\!\big(\sum_m W_m z^m/m\big)$ with $W_m$ a locally-defined weight from $Q_{\rm true}$ contraction or certified $p$-step channel data. Status `[OPEN]` until weights are specified.

---

**DZT-OPEN-B2 — Analytic transfer/Ruelle zeta (deferred)** [RID: DZT-OPEN-ANALYTIC-ZETA]

Status: OPEN (analytic frontier; not a launch object)
Requires a fixed operator type (Perron–Frobenius / Koopman / weighted Ruelle), domain (global map / wrapped cylinder / Birkhoff sector / $p$-step strobe), function space, weight, and a periodic-point-finiteness statement. The global map has an elliptic point $P_1$, a hyperbolic saddle $P_2$, and nonconstant $\det J$; singular/near-singular $\det(I-DT^m)$ on elliptic resonant orbits needs branch accounting. Deferred until B1 and 0A are settled.

---

## §3. Scope Guards {#sec-3-scope-guards}

**[SG-DZT-1]** No graph-zeta carryover. AZ Thread-C Hashimoto/Ihara/graph-zeta results do not transfer to DZT. Shared "zeta"/"transfer" vocabulary is not a bridge theorem (SG-PROG-1, SG-AZ-7).
Violation: citing the AZ `4|q` rule or any TDR-G graph-zeta spectrum as evidence for a DZT claim.

**[SG-DZT-2]** Continuous-only object. DZT acts on Dyadic continuous-branch observables. No TDR-G graph, $\mathbb{Z}_N$ memory observable, or discrete defect spectrum enters without a named bridge theorem.
Violation: importing a discrete-branch observable into a DZT transform.

**[SG-DZT-3]** Dyadic ownership. OPEN 9 coefficients, cancellations, channel polynomials, and channel-boundary results remain owned by `RTG_DYADIC_OSCILLATOR_DSN`. DZT owns only transform definitions, transform identities, diagnostics, and new consequences derived from them.
Violation: re-deriving or re-stating a Dyadic OPEN 9 result as DZT-owned.

**[SG-DZT-4]** No RH / prime mysticism. No statement may be read as bearing on the Riemann Hypothesis or classical prime distribution. Prime/composite status enters only through explicit RTG mechanisms: divisor structure, cyclic closure, subgroup charge, cyclotomic sum/divisibility, missing-slot structure, or secular-mode inclusion (mirrors SG-AZ-1/SG-AZ-2).
Violation: citing a prime as significant without naming the RTG mechanism through which it enters.

**[SG-DZT-5]** No OPEN-M amplitude import. No DZT pattern closes OPEN M or supplies a UV amplitude unless it computes a named OPEN-M source object or proves a named bridge theorem.
Violation: asserting a DZT arithmetic pattern resolves the $\sigma_f$ cascade source.

**[SG-DZT-6]** OPEN-P0 ceiling. All DZT results are conditional on the postulated/canonical continuous dyadic generator $T$ until OPEN-P0 closes (SG-PROG-2). No DZT object is "physically primitive."
Violation: presenting a DZT result as model-independent.

**[SG-DZT-7]** Two-root discipline. The fixed Dyadic resonance eigenvalue $\lambda_6=e^{i\pi/3}$ (linearization at $P_1$, a property of $T$) and the cyclotomic root $\zeta_p$ in $p$-step accumulation sums are distinct for all $p\ne6$ and coincide only when explicitly specialized to $p=6$. No proof may silently substitute $\lambda_6$ for $\zeta_p$, or let the fixed resonance eigenvalue acquire $p$-dependence, without a derived embedding or specialization.
Violation: any unannounced $\lambda_6=\zeta_p$ identification outside $p=6$.

**[SG-DZT-8]** No lookup-table transform. A DZT transform earns `[NUM diagnostic]` only if a transform-level structure — zero locus, resultant factorization, field norm, valuation pattern, special value, or functional relation — maps onto a certified Dyadic fact. A transform that merely re-encodes known channel labels is `[FAIL]`, even if it separates classes visually or statistically.
Violation: tagging a relabeling of the $A_p$ table as a diagnostic result.

---

## §4. Layer Routing {#sec-4-layer-routing}

$$\text{Dyadic OPEN 9 (owned)} \xrightarrow{\text{import-ref}} \text{Channel polynomial } P_C \xrightarrow{\text{Res}(\Phi_p,\cdot)} \text{Transform } R_C(p) \xrightarrow{\text{diagnostic}} \text{Arithmetic structure}$$

**Case V cascade channel:** when the channel is a per-$p$ algebraic value rather than a single polynomial (the $q=4,(0,3)$ cascade), the route is instead
$$\text{Dyadic Case-V values } Q_p \xrightarrow{\text{phase removal}} M_p=Q_p/(i\zeta_p^3)\in\mathbb{Q}(\zeta_p)^+ \xrightarrow{N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}} \text{amplitude-norm diagnostic}.$$
The resultant $\mathrm{Res}(\Phi_p,\cdot)$ path applies to Case P (polynomial-in-$\zeta_p$) channels like $b=5$; the field-norm path applies to Case V channels.

| Question | Layer | Canonical tool |
|---|---|---|
| What is the certified channel fact? | Dyadic (owned) | OPEN 9 ledger; cited by `[import-ref]`, never re-owned |
| What is the channel polynomial/value? | Channel | $P_C(x)$ extracted from Dyadic; raw vs normalized vs cascade distinguished |
| What does the transform compute? | Transform | $R_C(p)$, field norm, valuation, $\log|R_C|/\varphi(p)$, special value |
| What does the transform mean? | Diagnostic | mechanism mapping under SG-DZT-8; Mahler/norm reading is `[HYP]` until earned |

Routing rules:
- Diagnostic-layer structure does not certify a Dyadic-layer claim; it reproduces or predicts one, and prediction is confirmed only by Dyadic enumeration.
- $\lambda_6$ and $\zeta_p$ are distinct objects across the channel→transform boundary (SG-DZT-7).
- No transform object imports from the discrete branch or AZ Thread C without a named bridge theorem (SG-DZT-1/2).

<!-- AI_CONTEXT_CORE_END -->

---

## §5. High-Risk Claims Ledger {#sec-5-high-risk}

| Claim | Valid form | Forbidden overclaim | Section |
|---|---|---|---|
| $b=5$ survival reproduction | $R_{(0,5)}(p)\ne0$ on finite horizon, reproduces certified all-$p$ survival `[RESULT]` `[from: ALG]` | DZT *proves* all-$p$ survival (it is Dyadic-owned, imported) | §6.2 |
| Amplitude norm | rational $\lvert N_+(M_p)\rvert$ per point, `[ALG]` `[scope: validation table p=12–64; audit p≤1000]`; on the audited range the odd-prime anomalies are exactly $p=8\ell^a$, $\ell^a\equiv1\!\pmod4$ | the 2-power/support-on-2 *law* — **falsified** at $p=40$; any $k_p$ formula; a sign of $N_+(M_p)$ read off the tables | §6.3 |
| Phase-law import | $Q_p=i\zeta_p^3M_p$, $M_p\in\mathbb{Q}(\zeta_p)^+$ as Dyadic **all-$p$ `[THM]`** (DYAD-THM-Q403-PHASELAW) | zeta-continuation / RH / prime-distribution reading without a named DZT bridge (SG-DZT-4) | §6.3, §7 |
| Cyclotomic transform | vanishing $\iff \Phi_p\mid P_C$ `[ALG]` | a $p^{-s}$/RH/Euler-product reading | §1 |
| $\lambda_6$ vs $\zeta_p$ | distinct except $p=6$ (SG-DZT-7) | identifying them at general $p$ | §3 |
| AZ graph-zeta relation | none without bridge (SG-DZT-1) | DZT continues/validates AZ Thread C | §3 |

---

## §6. Main Scientific Ledger {#sec-6-ledger}

### §6.1 The channel transform `[DEF]` {#sec-6-1-transform}

`[DEF]` For $P_C\in\mathbb{Q}[x]$ (or a number-field channel value), $R_C(p)=\mathrm{Res}(\Phi_p,P_C)=\prod_{\zeta_p}P_C(\zeta_p)\in\mathbb{Q}$ (integer when $P_C\in\mathbb{Z}[x]$). `[ALG]` Standard resultant theory: $\Phi_p$ monic and irreducible over $\mathbb{Q}$ is the minimal polynomial of $\zeta_p$, so $R_C(p)=0\iff\Phi_p\mid P_C\iff P_C(\zeta_p)=0$. The transform is channel-indexed; cross-channel comparison is the intended observable.

### §6.2 DZT-OPEN-0A, $b=5$ row `[RESULT]` `[from: ALG]` {#sec-6-2-b5-row}

`[import-ref]` `[ALG]` `[import: RTG_DYADIC_OSCILLATOR_DSN v6.4.24 §6.11 | DYAD-ALG-B5-ALLP-NONVANISHING]` Channel polynomial $N(x)=2x^6+x^5-5x^4-3x^3-4x^2+2x+1$, with the certified statement $\Phi_p\nmid N$ for all $p$ (cyclotomic non-division; $\deg N=6\Rightarrow$ exception set $\varphi(p)\le6$, all checked). It closes the Dyadic OPEN module DYAD-OPEN-B5-ALLP.

`[RESULT]` `[from: ALG]` `[scope: finite horizon sweep]` Computing $R_{(0,5)}(p)=\mathrm{Res}(\Phi_p,N)$:

| $p$ | $\varphi(p)$ | $R_{(0,5)}(p)$ | zero? |
|---:|---:|---:|:--:|
| 6 | 2 | 147 | no |
| 7 | 6 | 30808 | no |
| 8 | 4 | 4132 | no |
| 10 | 4 | 101 | no |
| 12 | 4 | 3589 | no |
| 13 | 12 | 1004078323 | no |
| 14 | 6 | 155968 | no |
| 30 | 8 | 3232051 | no |

The transform is nonzero throughout, reproducing the imported $b=5$ survival on the tested horizon, and carries arithmetic magnitude beyond the zero/nonzero bit (satisfying SG-DZT-8: nonvanishing resultant $=$ cyclotomic non-division, mapped onto a certified fact). Certified by `dzt_open_0a_verify.py` (exit 0; output attributes the all-$p$ statement to DYAD-OPEN-B5-ALLP and only the finite sweep to DZT). The all-$p$ statement remains Dyadic-owned (`[import-ref]`); DZT reproduces it on the horizon and supplies the size diagnostic.

### §6.3 Cascade amplitude norm `[ALG]` — mixed content {#sec-6-3-nearmiss-norm}

`[import-ref]` `[THM]` `[import: RTG_DYADIC_OSCILLATOR_DSN v6.4.24 §6.11 | DYAD-THM-Q403-PHASELAW]` Each $q=4,(0,3)$ cascade value (Dyadic extraction DYAD-ART-Q403-EXTRACT; closed form in §7) factors as $Q_p=i\zeta_p^3 M_p$ with $M_p=Q_p/(i\zeta_p^3)\in\mathbb{Q}(\zeta_p)^+$ for all $p=4s\ge12$ ($p=8$ the zero degeneracy); the direction $i\zeta_p^3$ is universal ($\lambda^{-s}=-i$). $M_p$ is a real algebraic number whose sign is not asserted here. DZT's pointwise re-verification at the audited $p$ (incl. $p=40$) corroborates the Dyadic theorem; the all-$p$ proof is Dyadic-owned. `[ALG]` `[scope: object-level, all p=4s≥12]` Hence the norm $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)\in\mathbb{Q}$ is a well-defined invariant for all $p=4s\ge12$; its *values and anomaly pattern* are finite-horizon (below).

`[ALG]` `[RID: DZT-ALG-CASCADE-NORM]` `[scope: validation table, p=12–64; canonical computation is the p≤1000 closed-form audit below]` The absolute value of the real-subfield norm, $\lvert N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)\rvert$, is rational at every point:
$$\big(\tfrac14,\tfrac18,\tfrac14,\tfrac18,\tfrac18,\tfrac1{32},\tfrac18,\tfrac{25}{16},\tfrac1{32},\tfrac1{32},\tfrac1{64},\tfrac1{64},\tfrac1{16},\tfrac1{512}\big),\quad p=(12,16,20,24,28,32,36,40,44,48,52,56,60,64).$$
Pure 2-power at all 14 points except $p=40$: $\lvert N_+(M_{40})\rvert=\tfrac{25}{16}=5^2\cdot2^{-4}$ (numerator $5^2$; the only value above 1 on the table). The values are absolute values: the closed-form audit computes $\sqrt{\lvert N_{\rm full}\rvert}$ (§8, DZT-ART-CF-AUDIT), and the sign of $N_+(M_p)$ is not determined by DZT. Machine-verified `dzt_casev_norm_audit.py` (14-point, exit 1, falsifier flags $p=40$); $p=40$ and $p=60$ cross-checked against fresh Dyadic-engine extractions (runs source-reported; §8).

`[FAIL]` `[RID: DZT-HYP-MAHLER-NEARMISS]` The v0.4 hypothesis — $N_+(M_p)$ a pure 2-power / amplitude supported only on the prime above 2 for all $4\mid p$ — is **falsified** by $p=40$. The 2-power pattern held on the original $p=12$–$36$ window and at $p=44,48,52$, but is not a family law. Permanent record: Appendix B.

`[ALG]` `[RID: DZT-ALG-P12-NORM]` The certified cascade-boundary survivor $v=-13+\tfrac{15\sqrt3}{2}\in\mathbb{Q}(\sqrt3)$ (Dyadic, channel $(q,D)=(4,(0,3))$, $p=12$; $|v|\approx0.0096$) has $\mathbb{Q}(\sqrt3)/\mathbb{Q}$ **reduced** field norm $N_{\mathbb{Q}(\sqrt3)/\mathbb{Q}}(v)=v\,\bar v=(-13)^2-3\big(\tfrac{15}{2}\big)^2=169-\tfrac{675}{4}=\tfrac14$. The smallness of $|v|$ coincides with a large conjugate ($\bar v\approx-25.99$) and a small rational norm $\tfrac14$. The norm value is exact and machine-verified (`dzt_open_0a_verify.py`, §8; run source-reported). It is the $\varphi/2=2$ point ($\mathbb{Q}(\zeta_{12})^+=\mathbb{Q}(\sqrt3)$); $p=8$ is the $Q_8=0$ degeneracy ($\mathbb{Q}(\zeta_8)^+=\mathbb{Q}(\sqrt2)$). A fact about one value; survives the family falsification.

`[OPEN]` What survives the falsification: the norm is rational; the Dyadic factorization holds; the certified boundaries are reproduced. The odd-prime support question is DZT-OPEN-0B-R (§2); the anomaly set found so far is DZT-ALG-CASCADE-ANOMALY-SET below — not support-on-2.

`[ALG]` `[scope: finite horizon p≤1000, 249 points]` `[RID: DZT-ALG-CASCADE-ANOMALY-SET]` The odd-prime anomalies are exactly $p=8\ell^a$ with $\ell^a\equiv1\!\pmod4$: the 20 points $\{40,72,104,136,200,232,296,328,392,424,488,584,648,712,776,808,872,904,968,1000\}$, each with $\lvert N_+\rvert$ numerator exactly $\ell^2$ (e.g. $p=72=8\cdot3^2\!\to9/64$; $p=200=8\cdot5^2\!\to25/2^{20}$; $p=392=8\cdot7^2\!\to49/2^{42}$). Machine-verified `dzt_anomaly_rule_check.py` (exit 0, 0 mismatches / 249; run source-reported, §8).

`[ALG]` `[scope: finite horizon p≤1000]` **Correction of the imported note.** The note's pattern "anomaly for every odd prime power $q$" is **false**: prime powers $q\equiv3\!\pmod4$ ($p=24,56,88,152,184,216,\dots$) are pure 2-powers on the audited range. The required condition is $q\equiv1\!\pmod4$. The note's $N_+=2^{-\varphi(q)}$ denominator formula also fails in general (only the anomaly *locations* and the $\ell^2$ *numerators* are clean); **no denominator law is asserted**.

`[HYP]` Candidate mechanism for the mod-4 gate: $q\equiv1\!\pmod4\Rightarrow\mathbb{Q}(\sqrt q)\subset\mathbb{Q}(\zeta_q)^+$ real (so $\ell$ enters the real-subfield norm); $q\equiv3\Rightarrow$ only $\mathbb{Q}(\sqrt{-q})$, imaginary, excluded. To be settled by the DZT-OPEN-0B-R resultant identity.

---

## §7. Import Ledger {#sec-7-imports}

All imports are from `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 (`dyad-v6.4.24`), checked against that edition for v0.18; identifiers as classified by its Appendix F (`dyad-v6.4.24`), which creates no alias. Ownership remains Dyadic. No AZ, TDR-G, OPEN-M or Genesis import (SG-DZT-1/2/5).

- [RID: DYAD-ALG-B5-ALLP-NONVANISHING] :: $b=5$ channel: $F_{\rm raw}^p(0,5)\ne0$ for every $p\ge6$; channel polynomial $N=2x^6+x^5-5x^4-3x^3-4x^2+2x+1$ with $\Phi_p\nmid N$ :: Dyadic v6.4.24 §6.11 :: source for §6.2 :: dyadic map, $b=5$, all $p\ge6$
  Source status: `[ALG]` (all $p$, complete); it closes the lifecycle identifier DYAD-OPEN-B5-ALLP.
  Verification: owner entry inspected (`EV-SRC-READ`); owner artifacts not rerun by DZT.
- [RID: DYAD-ALG-VANISH-B2] :: $F_{\rm raw}^p(0,2)=0$ for $p\ge4$; no secular mode :: Dyadic v6.4.24 §6.11 :: $b\le4$ row of DZT-OPEN-0A (DZT-ALG-B234-STRUCTURAL) :: dyadic map, $p\ge b+2$ only
  Source status: `[ALG]`.
- [RID: DYAD-ALG-VANISH-B3] :: $F_{\rm raw}^p(0,3)=0$ for $p\ge5$; no secular mode :: Dyadic v6.4.24 §6.11 :: as above :: dyadic map, $p\ge b+2$ only
  Source status: `[ALG]`.
- [RID: DYAD-ALG-VANISH-B4] :: $F_{\rm raw}^p(0,4)=0$ for $p\ge6$; no secular mode :: Dyadic v6.4.24 §6.11 :: as above :: dyadic map, $p\ge b+2$ only
  Source status: `[ALG]`.
- Cascade values at $p=8$ and $p=12$ (no owner RID) :: channel $(4,(0,3))$: $p=8$ cancels; $p=12$ value $-13+\tfrac{15\sqrt3}{2}$ :: Dyadic v6.4.24 §6.11 and §2 OPEN 9 :: §6.3, DZT-ALG-P12-NORM :: dyadic map
  Source status: owner statement without a RID (owner Appendix F, `dyad-v6.4.24`, lists the string DZT used as unmatched); cited as text. Sign as stated by the owner.
- [RID: DYAD-ALG-P6-FACEFLUX] :: $\lambda_6=e^{iF_f/2}=e^{i\pi/3}$ resonance eigenvalue :: Dyadic v6.4.24 §6.2 :: SG-DZT-7 two-root discipline :: $p=6$ only
  Source status: `[ALG]`.
- [RID: DYAD-THM-Q403-PHASELAW] :: for $p=4s$, $s\ge2$: $\sigma_{-1}(Q)=-L^{-6}Q$ for the closed form $Q=L^5(IL^2+I-L^2+1)/[2(L+1)^4(L^2+L+1)]$, $L=\zeta_p$, $I=L^{p/4}=i$; hence $Q_p=i\zeta_p^3M_p$ with $M_p=Q_p/(i\zeta_p^3)\in\mathbb{Q}(\zeta_p)^+$ ($p=8$ the zero degeneracy; nonzero phase law from $p=12$) :: Dyadic v6.4.24 §6.11 :: §6.3 norm object; closed-form audit of DZT-OPEN-0B-R :: dyadic map, $4\mid p$
  Source status: `[THM]` `[proof: exact algebraic identity]`. Its parts at the owner carry no separate RIDs (owner Appendix F, `dyad-v6.4.24`): the universal direction $\lambda^{-s}=\zeta_p^{-p/4}=-i$ for all $4\mid p$; the reality relation $f^{\bar W}_{(b,a)}=\overline{f^W_{(a,b)}}$, lifting through composition ($J(f^s)=(Jf)^s$), with $J$ realized by the Galois automorphism $\sigma_{-1}$; the leading $(0,3)$ accumulation $\sum_{k=0}^{s-1}\zeta_p^{-4k}=0$ for $s\ge2$, so that $Q_p$ is the subleading remainder (total cancellation at $s=2$, i.e. $Q_8=0$); the remainder relation in its $A_p$-form, $\sigma_{-1}(A_p)=\zeta_p^{-6}A_p$; and the closed form above.
  Verification: owner entry inspected (`EV-SRC-READ`). DZT checked the closed form against the Dyadic extractor at $p=12,16,20,24,40,44,60$ (source-reported). The owner certificate is DYAD-ART-Q403-CERT; not rerun by DZT.
- [RID: DYAD-ART-Q403-EXTRACT] :: exact in-field extractor `q4_03_cascade_extract.py` for the Case-V values $Q_p\in\mathbb{Q}(\zeta_p)$ ($p=8$–$64$, $4\mid p$): raw $R^{\rm raw}_{p,4}=\lambda^{-s}f_p^s-\mathrm{Id}$, $s=p/4$, charge-projected on $K^{\rm extra}_{p,4}$, $\chi(a,b)=(a-b-1)\bmod p$; calibration gates $p=8\to0$, $p=12\to-13+\tfrac{15\sqrt3}{2}$ :: Dyadic v6.4.24 §8 :: source of the Case-V values used for §6.3 and DZT-ALG-CASCADE-ROW :: dyadic map, $4\mid p$, $p=8$–$64$
  Source status: owner artifact `[ALG]`. Correspondence by content only: DZT cited the extractor with SHA-256 `ecdb805f…05eac2` and its horizon file with `14526cf1…7bec16`; the owner records no hash and neither file is in this repository, so no byte identity is claimed.
- [RID: DYAD-ART-Q403-CERT] :: certificate `q4_03_R_identity_certificate.py`, exits `CERTIFICATE PASS` :: Dyadic v6.4.24 §8 :: proof artifact of DYAD-THM-Q403-PHASELAW :: —
  Availability: not in this repository; not rerun by DZT.

---

## §8. Artifact and Script Registry {#sec-8-artifacts}

Paths in this section are relative to `upload/dzt-recovery-20261116/received/originals/downloads/`.

- [RID: DZT-ART-VERIFY-0A] :: `dzt_open_0a_verify.py` :: computes $R_{(0,5)}(p)$ over the horizon sweep and the $p=12$ reduced field norm; reproduces imported $b=5$ survival on the tested horizon (ownership-safe wording) and norm $=\tfrac14$ :: `[ENG]` exit 0
  Files: [RECOVERED] two contents — `dzt_open_0a_verify (1).py` (= `dzt_open_0a_verify (2).py`), SHA-256 `3791b110b94fb7e6988c05109d963522f1fbc9e2907034945152d74ff7ba5c7e`, whose output wording matches this entry; and `dzt_open_0a_verify.py`, SHA-256 `989f6c2d858747bac66a97a7fe6eb6a7e135ddde040c57a936f881a7a9e62b52`, without the ownership-safe wording.
- [RID: DZT-ART-CHANNEL-AUDIT] :: `dzt_channel_audit.py` :: two-layer channel-state audit; certifies $b\le4$ $E_C=0$ structural-absence encoding (no resultant), distinct from $b=5$ $E_C=1$ cyclotomic survival; cascade row intentionally not computed :: `[ENG]` exit 0
  Files: [RECOVERED] `dzt_channel_audit.py`, SHA-256 `afcbed4f6ba7d6d00aef40d181789626fa44a6a9dd3b283ca5e171fa384c563c`.
- [RID: DZT-ART-CASCADE-AUDIT] :: `dzt_0b_audit.py` :: re-extracts $Q_p$ from the Dyadic engine, verifies the phase law and $M_p\in\mathbb{Q}(\zeta_p)^+$, computes field norms $p=12$–$28$ :: `[ENG]` exit 0
  Files: [RECOVERED] `dzt_0b_audit.py`, SHA-256 `b586c7c273469dd075164b245b485486ca08a33f514f11585c00ac940f8586f9`. It calls the Dyadic engine, which is not in this repository.
- [RID: DZT-ART-NORMLAW] :: `dzt_0b_normlaw.py` :: 7-point amplitude-norm computation ($p=12$–$36$); superseded as evidence by the 14-point transcription harness and, canonically, by the closed-form audit DZT-ART-CF-AUDIT :: `[ENG]` exit 0
  Files: [RECOVERED] `dzt_0b_normlaw.py`, SHA-256 `1b03da50a3bc02c7efd368d644970ec84f1c8255990ea6e31814a888c57f0fb4`.
- [RID: DZT-ART-CASEV-AUDIT] :: `dzt_casev_norm_audit.py` :: reusable 14-point transcription-based Case-V audit ($p=12$–$64$); **falsifies** support-on-2 at $p=40$ :: `[ENG]` exit 1 (falsifier fired, as designed)
  Files: [RECOVERED] two contents — `dzt_casev_norm_audit (1).py`, SHA-256 `22783fcd701dce5f4a8cf073f84db058e13604b55b1f5867e5653a32f54f0f16`, the 14-point audit this entry describes; and `dzt_casev_norm_audit.py`, SHA-256 `d48716c892d9c04804cdebd1bde79fb4cc6efff95d24f213634c932fc8279d9b`, an earlier, shorter horizon.
- [RID: DZT-ART-CF-AUDIT] :: `dzt_casev_norm_from_closed_form.py` :: transcription-free closed-form norm audit to $p=1000$ (249 points) from the Dyadic closed form (DYAD-THM-Q403-PHASELAW, §7); it reports $\sqrt{\lvert N_{\rm full}\rvert}$, so the sign of $N_+(M_p)$ is not part of its output; CSV `dzt_casev_norm_closed_form_p8_1000.csv` :: `[ENG]` (Dyadic-imported script, DZT-rerun)
  Files: [RECOVERED] two contents — `dzt_casev_norm_from_closed_form (2).py` (= `(3)`), SHA-256 `e38b5f7e0d809bc9333df91968ee741c89fecad5ea8fcd10fbfd3eecd65aa6ed`, which prints the required $q\equiv1\!\pmod4$ condition; and `dzt_casev_norm_from_closed_form.py` (= `(1)`), SHA-256 `4d3d3ca374d884377cf1ad5faa83fa218897c10dd69d9e119e076a73f7edb10e`, the uncorrected printed heuristic. CSV `dzt_casev_norm_closed_form_p8_1000.csv`, SHA-256 `d9dd7bd90bb9fd2340f6e5259129437db4850d5c057be0d5f527bbc78183555a`.
- [RID: DZT-ART-ANOMALY-RULE] :: `dzt_anomaly_rule_check.py` :: verifies the **corrected** anomaly rule ($p=8\ell^a$, $\ell^a\equiv1\!\pmod4$, numerator $\ell^2$) against the 249-row CSV :: `[ENG]` exit 0 (0 mismatches)
  Files: [RECOVERED] `dzt_anomaly_rule_check.py`, SHA-256 `cec06de0650a43f91f4c242403c6eb18af5a40915add5cdc2ff51611a4145b44`.

Every exit code in this section is source-reported; none was rerun for v0.18.

---

## §9. Collaboration and Provenance {#sec-9-provenance}

**Contributors:** Mustafa (PI — founding ruling: cyclotomic/resultant primary, $p^{-s}$ demoted, Mahler reading held at `[HYP]`, title/prefix). Claude (math auditor / DZT editor / coder — two-field discipline, SG-DZT-7, field-norm computation, DZT-OPEN-0A first row). ChatGPT · Gemini · Grok (critique rounds: founding-object scoping, lookup-table guard SG-DZT-8, two-track split).
**Archive:** rtgtheory.org · Zenodo DOI 10.5281/zenodo.17568897 · repository rtg-resonance-2025.

| Insight | Provenance | Tag |
|---|---|---|
| Cyclotomic/resultant transform as native object (not $p^{-s}$) | Claude finding 1; PI ruling | `[DEF]` |
| $\mathbb{Q}(\sqrt3)\times\mathbb{Q}(\zeta_p)$ two-field discipline; SG-DZT-7 | Claude finding 2; critique reword | `[DEF]` |
| Field norm $=\tfrac14$ for the $p=12$ near-miss | Claude (verified) | `[ALG]` |
| Mahler interpretation held at `[HYP]` | PI correction | `[HYP]` |
| Lookup-table falsifiability guard | critique contribution | `[DEF]` |
| Two-track split (A primary, B1 formal, B2 deferred) | critique + Claude | `[DEF]` |
| Two-layer channel state $E_C(p)$ (structural vs cyclotomic zero) | critique ruling (v0.2) | `[DEF]` |
| Compositum ambient field $K_{C,p}=F_C\cdot\mathbb{Q}(\zeta_p)$ | critique ruling (v0.2) | `[DEF]` |
| Cascade polynomial extracted Dyadic-side first | critique ruling (v0.2) | `[DEF]` |
| Script ownership-wording patch (all-$p$ → Dyadic) | critique ruling (v0.2) | `[ENG]` |
| Cascade is Case V; transform is real-subfield norm in $\mathbb{Q}(\zeta_p)^+$ | Claude (v0.4, on Dyadic delivery) | `[DEF]` |
| Amplitude norm 2-power on $p=12$–$36$ (later seen as finite-horizon coincidence) | Claude (v0.4) | `[ALG]` `[scope: finite horizon]` |
| Support-on-2 / 2-power hypothesis **falsified** at $p=40$ ($5^2\cdot2^{-4}$) | Claude (v0.5, `dzt_casev_norm_audit.py`) | `[FAIL]` |
| Reusable 14-point Case-V audit harness | activity-note item; Claude (v0.5–0.6) | `[ENG]` |
| $p=40$ is the sole 2-power anomaly across 14 points (isolated outlier; superseded, Appendix B) | Claude (v0.6) | `[OBS]` |
| Dyadic closed form for the cascade; DZT-verified faithful | Dyadic stream (v0.7) | `[import-ref]` |
| Anomalies recur; $p=40$ not globally isolated (next $p=72$) | Claude (v0.7) | `[COR]` |
| Corrected anomaly rule: $p=8\ell^a$, $\ell^a\equiv1\!\pmod4$, numerator $\ell^2$ (249 pts) | Claude (v0.7) | `[ALG]` `[scope: finite horizon p≤1000]`; mechanism `[HYP]` |
| Correction of imported note ($\equiv1\!\pmod4$ required; no denominator law) | Claude (v0.7) | `[COR]` |
| (R)-link closed upstream → factorization $Q_p=i\zeta_p^3M_p$ now all-$p$; norm object all-$p$ | Dyadic stream (v0.8) | factorization `[THM]` (Dyadic, DYAD-THM-Q403-PHASELAW); norm object all-$p$ `[ALG]` `[scope: object-level, all p=4s≥12]` (DZT, §6.3) |
| Object-vs-pattern discipline: anomaly law stays finite-horizon despite (R)-closure | Claude (v0.8) | `[DEF]` (scope rule) |
| $p=8$ real-subfield correction ($\mathbb{Q}(\zeta_8)^+=\mathbb{Q}(\sqrt2)$, $Q_8=0$) | Dyadic catch + Claude verify (v0.4) | `[ALG]` |
| Imported Dyadic phase law (DYAD-THM-Q403-PHASELAW); P1, reality and LEAD are its components, historical note labels without owner RIDs (owner Appendix F, `dyad-v6.4.24`) | Dyadic stream (v0.4) | `[THM]` (Dyadic, at `dyad-v6.4.24`) |

---

## Appendix A — Version History

### v0.18 — 18 November 2026 — adopted 19 November 2026
Corrections and synchronization edition after the reactivation triage (`records/dzt/DZT_REACTIVATION_TRIAGE.md`), with the Methodology v1.4 migration as a second build stage; no new scientific claim and no grade raised. The tabulated amplitude norms are stated as $\lvert N_+(M_p)\rvert$, and $M_p$ is defined as $Q_p/(i\zeta_p^3)$ with its sign not asserted; the validation table and the anomaly set are scoped together; the Import Ledger is repinned to `dyad-v6.4.24` per its Appendix F; compound grade tokens are unpacked; §8 cites the recovered script files by path and hash with their evidence states; §1 keeps readouts and pointers. Companion pins: `programme-v1.4`, `dyad-v6.4.24`, `az-v0.10`, `ofn-v0.12`, `methodology-v1.4`. Corrections: Appendix B. Record: `records/dzt/DZT_v0_18_RELEASE_RECORD.md`.

### v0.9–v0.17 — not part of this lineage
DZT editions v0.9–v0.17 (June 2026) have no adoption record. Their files were received on 16 November 2026 and are listed with hashes in the v0.18 release record; their content enters v0.18 only through the corrections above.

### v0.1–v0.8 — June 2026
From the founding charter (v0.1) to the integration of the Dyadic all-$p$ phase law (v0.8). Full entries: Appendix A of `dzt-v0.8`.

## Appendix B — Retired and Rejected Claims

`[RETRACTED | RID: DZT-RETRACT-MAHLER-RESULT]` Earlier draft phrasing called the $p=12$ near-miss a "small-Mahler-measure signature" in `[RESULT]` voice. Reason: the norm computation is exact `[ALG]` but the *mechanism* identification is not earned at v0.1. Replaced by: DZT-HYP-MAHLER-NEARMISS `[HYP]` (§6.3). Version: v0.1.

---

`[FAIL | RID: DZT-HYP-MAHLER-NEARMISS]` **Support-on-2 / pure-2-power amplitude-norm hypothesis — falsified (v0.5).** Stated (v0.4): for all $4\mid p$, $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)$ is a pure power of 2 / the cascade amplitude is supported only on the prime above 2. Held over $p=12$–$36$ (7 points) and $p=44,48,52$. **Counterexample $p=40$:** $N_+(M_{40})=\tfrac{25}{16}=5^2\cdot2^{-4}$ (odd prime 5, squared; also the unique point with $N_+>1$), confirmed against a fresh Dyadic-engine extraction. Cause of the earlier impression: the initial horizon happened to be all-2-power. What survives: the norm is rational; the Dyadic factorization $Q_p=i\zeta_p^3M_p$ holds (incl. $p=40$); the cascade reproduction is intact. The per-point computation is retained as DZT-ALG-CASCADE-NORM with the exception flagged. No structure inferred from the single anomaly. Version: v0.5.

---

`[SUPERSEDED]` Original (DZT-ALG-CASCADE-NORM and the §1 readout, `dzt-v0.8` §1 and §6.3): the tabulated values were headed $N_+(M_p)$, and $M_p$ was written as $\lvert Q_p\rvert$. Reason: the values are absolute values — the closed-form audit computes $\sqrt{\lvert N_{\rm full}\rvert}$ and the sign of $N_+(M_p)$ is not determined by DZT — and $M_p$ is defined as $Q_p/(i\zeta_p^3)$, a real number whose sign is not asserted. Replacement: §6.3, DZT-ALG-CASCADE-NORM, stated for $\lvert N_+(M_p)\rvert$; the values are unchanged. The same holds for the values in the `[FAIL]` record of DZT-HYP-MAHLER-NEARMISS above, which is kept as worded at `dzt-v0.8`: they are $\lvert N_+\rvert$ values, and its "unique point with $N_+>1$" refers to the points that record names ($p=12$–$52$, 11 points). Recorded in: v0.18.

---

`[SUPERSEDED]` Original (`dzt-v0.8` §6.3, an `[OBS]` of v0.6): "$p=40$ is the sole anomaly across 14 points", an isolated exception. Reason: true only for $p\le64$; the closed-form audit to $p\le1000$ finds 20 anomaly points (the next after $p=40$ is $p=72$), as the v0.7 `[COR]` recorded. Replacement: §6.3, DZT-ALG-CASCADE-ANOMALY-SET. Recorded in: v0.7 (as a `[COR]` in §6.3); moved here in v0.18.

*END OF DOCUMENT — RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.18*
