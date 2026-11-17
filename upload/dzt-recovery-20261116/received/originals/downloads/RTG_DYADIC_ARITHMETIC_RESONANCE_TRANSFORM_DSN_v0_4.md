# RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.4

**Title:** RTG Dyadic Arithmetic-Resonance Transform Study — Founding Charter and Diagnostic Ledger
**Date:** June 2026
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok
**DSN Methodology:** DSN_METHODOLOGY_v1.2
**Programme document:** RTG_PROGRAMME_OVERVIEW_v1.1
**Document class:** Technical scientific DSN ledger (continuous branch, Tier 3 downstream diagnostic). Short name: *Dyadic Zeta/Arithmetic Transform (DZT)*.
**Supersedes:** `RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.3`.
**Companion documents:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1` (source of truth for all OPEN 9 arithmetic) · `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6` (discrete-branch AZ; quarantined, see SG-DZT-1) · `RTG_ONTOLOGICAL_FOUNDATIONS_v0.7` · `DSN_METHODOLOGY_v1.2`
**Programme tier:** Tier 3 — Continuous Programme, downstream diagnostic of Dyadic. Maturity **Level A** (defined model; exploration begun). All results inherit the OPEN-P0 ceiling (SG-PROG-2 / SG-DZT-6).

**Status summary:** This study defines a transform on Dyadic-owned OPEN 9 arithmetic. The founding object (Track A) is the **channel-fixed cyclotomic/resultant transform** $R_C(p)=\mathrm{Res}(\Phi_p,P_C)=\prod_{\zeta}P_C(\zeta)$, not a Dirichlet $p^{-s}$ series (which is demoted to a derived secondary diagnostic). v0.2 adds the **two-layer channel state** (a secular-content indicator $E_C(p)$ distinguishing structural absence from cyclotomic cancellation), the **compositum ambient field** $K_{C,p}=F_C\cdot\mathbb{Q}(\zeta_p)$ as the honest default setting, and makes the cascade transform row **Dyadic-extraction-gated** (the cascade channel polynomial $P_{(4,(0,3))}$ must be emitted by the Dyadic DSN before DZT promotes it to canonical state; DZT may run only a quarantined shadow reconstruction). The `[ALG]` field-norm fact ($N_{\mathbb{Q}(\sqrt3)/\mathbb{Q}}(-13+\tfrac{15\sqrt3}{2})=\tfrac14$) is recorded as a *reduced* norm; its mechanism interpretation stays `[HYP]`. v0.4 closes the cascade $(4,(0,3))$ row of DZT-OPEN-0A on the finite horizon using the Dyadic-emitted Case-V values (DYAD-ART-CASCADE-Q4-03, hash-pinned), all three rows now done. The DZT-OPEN-0B amplitude-norm result is registered: across $p=12,16,20,24,28,32,36$ the real-subfield norm $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)$ is a **pure power of 2** (no odd prime divides the amplitude norm), `[ALG finite horizon]`. The ambient-field target is corrected to $\mathbb{Q}(\zeta_p)^+$ (the $\mathbb{Q}(\sqrt3)$ framing was a $p=8,12$ artifact). Three Dyadic all-$p$ theorems now import ($\lambda^{-s}=-i$; reality; leading $s$-th-root cancellation); the phase law / (R)-link is imported as `[ALG finite horizon]`. **No Dyadic result is re-owned here; no AZ Thread-C graph-zeta result transfers; no OPEN-M amplitude or RH/prime claim is made.**

## Local Tag Aliases

| Local alias | Expands to | Used for |
|---|---|---|
| `[import-ref]` | `[DEF]` `[scope: reference-only import]` | result owned by another DSN; cited here, ownership not transferred |
| `[NUM diagnostic]` | `[NUM]` `[scope: diagnostic]` | numerical/finite-sweep result used as a diagnostic, not a standalone theorem |

`[DEF]` All other tag usage follows `DSN_METHODOLOGY_v1.2` canonical syntax. `[COR]` and `[RESULT]` `[from: TAG]` are canonical and require no aliasing.

---

## §1. Current Canonical State {#sec-1-canonical-state}

`[DEF]` **Study object.** This study constructs *arithmetic transforms* over Dyadic-owned $p$-resonance observables and asks whether transform-level structure (zero locus, resultant factorization, field norm, valuation pattern, special value, functional relation) maps onto — or predicts — certified Dyadic OPEN 9 facts. It does not study the Riemann zeta function and does not assert any result about classical prime distribution (SG-DZT-4).

`[DEF]` **Primary object — Track A (cyclotomic channel transform).** For a *fixed* Dyadic channel $C$ (either $C=b$ in the raw anti-holomorphic family $(0,b)$, or $C=(q,D)$ in the cascade family) with Dyadic-owned channel polynomial or algebraic channel value $P_C(x)$, define
$$R_C(p) \;=\; \mathrm{Res}\big(\Phi_p(x),\,P_C(x)\big) \;=\; \prod_{\zeta:\ \Phi_p(\zeta)=0} P_C(\zeta),$$
the product taken over primitive $p$-th roots of unity ($\Phi_p$ monic, so the resultant equals the bare product). `[ALG]` $R_C(p)=0 \iff \Phi_p \mid P_C \iff P_C(\zeta_p)=0$ for $P_C\in\mathbb{Q}[x]$. The transform is **channel-fixed**: the science lives in how the family $\{R^{(b)}\}$ / $\{R^{(q,D)}\}$ varies with the channel, not in a mixed $p$-table. `[RID: DZT-DEF-CHANNEL-TRANSFORM]`

`[HEUR]` **Secondary object — Dirichlet diagnostic (demoted).** A series $\sum_p A_C(p)\,p^{-s}$ is admissible only after $A_C(p)$ is *defined from* the native cyclotomic object (e.g. $A_C(p)=\mathrm{sgn}\,R_C(p)$, $v_\ell(R_C(p))$, $\log|R_C(p)|/\varphi(p)$, or a vanishing indicator). It is not the primary transform and carries no classical-zeta implication (SG-DZT-4).

`[DEF]` **Two-layer channel state (v0.2).** A resultant zero and a structural (secular-absence) zero are different events and must not be conflated. For a fixed channel $C$ and horizon $p$:
$$E_C(p)\in\{0,1\}\ \text{(secular-content indicator)},\qquad P_C(x)\ \text{and}\ R_C(p)=\mathrm{Res}(\Phi_p,P_C)\ \text{defined only when}\ E_C(p)=1.$$
Three classes:
- $E_C(p)=0$ — **structural/secular absence** (no source $\beta$-set contains the secular mode; the channel output vanishes identically). This is the $b\le4$ case for $p\ge b+2$ (Dyadic DYAD-ALG-VANISH-B2/B3/B4).
- $E_C(p)=1,\ R_C(p)=0$ — **cyclotomic cancellation** ($\Phi_p\mid P_C$).
- $E_C(p)=1,\ R_C(p)\ne0$ — **cyclotomic survival**. This is the $b=5$ case (§6.2).

The transform never encodes structural vanishing as a resultant zero. `[RID: DZT-DEF-CHANNEL-STATE]`

`[DEF]` **Ambient field (v0.2).** For channel $C$ at horizon $p$ the honest default setting is the compositum
$$K_{C,p}=F_C\cdot\mathbb{Q}(\zeta_p),$$
where $F_C$ is the Dyadic coefficient field fixed by the source convention and $\mathbb{Q}(\zeta_p)$ is the $p$-step cyclotomic field. **Cascade correction (v0.4):** for the $q=4,(0,3)$ cascade family the channel value is generically complex and lives in the full $\mathbb{Q}(\zeta_p)$; the natural real invariant is taken in the **maximal real subfield $\mathbb{Q}(\zeta_p)^+$** (degree $\varphi(p)/2$ over $\mathbb{Q}$), via $M_p=Q_p/(i\zeta_p^3)\in\mathbb{Q}(\zeta_p)^+$ and the norm $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)$. The earlier "coefficients in $\mathbb{Q}(\sqrt3)$" reading is a $p=8,12$ artifact ($\mathbb{Q}(\zeta_8)^+=\mathbb{Q}(\zeta_{12})^+=\mathbb{Q}(\sqrt3)$ only there), not the family law. `[RID: DZT-DEF-AMBIENT-FIELD]`

`[ALG]` **First native arithmetic fact — $p=12$ near-miss reduced norm.** The certified cascade-boundary survivor $v=-13+\tfrac{15\sqrt3}{2}\in\mathbb{Q}(\sqrt3)$ (Dyadic, channel $(q,D)=(4,(0,3))$, $p=12$; $|v|\approx0.0096$) has $\mathbb{Q}(\sqrt3)/\mathbb{Q}$ **reduced** field norm
$$N_{\mathbb{Q}(\sqrt3)/\mathbb{Q}}(v)=v\,\bar v=(-13)^2-3\big(\tfrac{15}{2}\big)^2=169-\tfrac{675}{4}=\tfrac14.$$
The smallness of $|v|$ coincides with a large conjugate ($\bar v\approx-25.99$) and a small rational norm $\tfrac14$. The norm value is exact and machine-verified. In the v0.4 family framing this is the $\varphi/2=2$ member ($\mathbb{Q}(\zeta_{12})^+=\mathbb{Q}(\sqrt3)$) of the amplitude-norm law below. `[RID: DZT-ALG-P12-NORM]`

`[ALG]` `[scope: finite horizon p∈{12,16,20,24,28,32,36}]` **Amplitude-norm law — 2-power property.** Writing each cascade value as $Q_p=i\zeta_p^3 M_p$ with $M_p=|Q_p|\in\mathbb{Q}(\zeta_p)^+$ (Dyadic-owned factorization, imported), the real-subfield norm is a **pure negative power of 2** at every horizon point:
$$N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)=2^{-k_p},\quad (k_p)_{p=12,16,20,24,28,32,36}=(2,3,2,3,3,5,3).$$
Equivalently $N_{\mathbb{Q}(\zeta_p)/\mathbb{Q}}(M_p)=2^{-2k_p}=\mathrm{Res}(\Phi_p,M_p)$ (the resultant transform applied to $M_p$). **No odd prime divides the amplitude norm**: the cascade amplitude is supported only on the prime above 2 (ramified in $\mathbb{Q}(\zeta_p)^+$ since $4\mid p$). Machine-verified, `dzt_0b_normlaw.py` (extract-vs-md cross-checked $p=16$–$28$; modulus-gated $p=32,36$). `[RID: DZT-ALG-CASCADE-NORM-2POWER]`

`[HEUR]` The exponent sequence $k_p$ is **diagnostic-only**; seven points do not determine a closed form, and no $k_p$ law is asserted (primitive-vs-ratio discipline). The robust claim is the 2-power *property*, not the exponent.

`[HYP]` **Mechanism / all-$p$ (reframed v0.4).** The original "$p=12$ near-miss is a small-norm effect" is now seen as the $\varphi/2=2$ instance of the 2-power-norm family. Open: (i) prove the 2-power property for all $p\equiv0\bmod4$ (DZT-side, gated on the Dyadic all-$p$ factorization, i.e. their link (R)); (ii) explain *why* only the prime above 2 appears — plausibly from the all-$p$ leading-cancellation (LEAD), making $Q_p$ a subleading remainder divisible by powers of the ramified prime, but this is not yet derived. See DZT-OPEN-0B. `[RID: DZT-HYP-MAHLER-NEARMISS]`

`[OPEN]` **Immediate frontier.** DZT-OPEN-0A (cyclotomic reproduction audit) — two rows done ($b=5$ survival §6.2; $b\le4$ structural absence, `dzt_channel_audit.py`); only the cascade $(4,(0,3))$ row remains, Dyadic-extraction-gated. Then DZT-0B (near-miss norm mechanism) and the Track B objects.

---

## §2. Active Frontier / OPEN Registry {#sec-2-open-registry}

### Priority ordering
1. **DZT-OPEN-0A** — cyclotomic reproduction audit (founding falsifier). $b=5$ survival and $b\le4$ structural-absence rows done; cascade $(4,(0,3))$ row remains Dyadic-gated.
2. **DZT-OPEN-0B** — characterize the amplitude-norm law: prove the 2-power property of $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)$ for all $4\mid p$, and (secondary) seek a closed form for $k_p$ (DZT-ALG-CASCADE-NORM-2POWER).
3. **DZT-OPEN-B1** — formal local NF/dynamical zeta near $P_1$ (algebraic, near-term).
4. **DZT-OPEN-B2** — analytic transfer/Ruelle zeta of the global map (deferred analytic frontier).

---

**DZT-OPEN-0A — Cyclotomic reproduction audit** [RID: DZT-OPEN-REPRODUCTION-AUDIT]

Status: CLOSED at finite-horizon scope (all three rows: $b=5$ survival, $b\le4$ structural absence, cascade $(4,(0,3))$) | Owner branch: this DSN

Question: For each fixed channel $C$ with Dyadic-owned certification, construct $P_C$ and compute $R_C(p)=\mathrm{Res}(\Phi_p,P_C)$ over the certified horizon set $p=5,6,7,8,10,12$ (plus the finite $\varphi(p)\le6$ exception set where relevant). Does the transform reproduce certified zero/nonzero statuses *and* expose mechanism (SG-DZT-8)?

Closed sub-items:
- $b=5$ channel ($P_C=N=2x^6+x^5-5x^4-3x^3-4x^2+2x+1$): $R_{(0,5)}(p)\ne0$ for all $p\in\{6,7,8,10,12,13,14,30\}$, reproducing imported all-$p$ survival on the tested horizon; carries arithmetic size. `[RESULT]` `[from: ALG]` `[scope: finite horizon sweep]` ✓ [RID: DZT-ALG-B5-RESULTANT]
- $b\le4$ structural-absence encoding: for $b\in\{2,3,4\}$ at $p\ge b+2$, the transform reports $E_{(0,b)}(p)=0$ (structural/secular absence) with no $P_C$ and no resultant defined — distinct from a cyclotomic cancellation $R_C=0$. Certified against the $b=5$ $E_C=1$ contrast class by `dzt_channel_audit.py` (exit 0). `[ALG]` `[scope: DZT channel-state encoding test]` ✓ [RID: DZT-ALG-B234-STRUCTURAL]
- Cascade $(q,D)=(4,(0,3))$ (v0.4, finite horizon): using the Dyadic-emitted Case-V values (DYAD-ART-CASCADE-Q4-03, hash-pinned), DZT reproduces $p=8$ cancellation and the $p=12$ value $-13+\tfrac{15\sqrt3}{2}$, and registers the transform as the real-subfield norm in $\mathbb{Q}(\zeta_p)^+$ (not a $\Phi_p$-resultant: the channel is Case V, a per-$p$ algebraic value, not a single polynomial). The norm is a 2-power across $p=12$–$36$ (DZT-ALG-CASCADE-NORM-2POWER). `[ALG]` `[scope: finite horizon]` ✓ [RID: DZT-ALG-CASCADE-ROW]

Active sub-items: none at finite-horizon scope; all-$p$ promotion of the cascade norm law is tracked under DZT-OPEN-0B.

Pass: reproduces certified zero/nonzero exactly; separates $E_C=0$ structural vanishing ($b\le4$) from $E_C=1$ cyclotomic survival ($b=5$); registers $p=12,(4,(0,3))$ as algebraically nonzero with its reduced-norm diagnostic.
Fail: collapses to prime/composite classification; mixes channels; encodes structural vanishing as a resultant zero; depends on a $\lambda_6=\zeta_p$ substitution outside $p=6$ (SG-DZT-7); cannot reproduce a certified status.

Next required artifact: none for the finite-horizon audit (complete). All-$p$ work moves to DZT-OPEN-0B and depends on the Dyadic (R)-link closure.

Dependencies: Dyadic OPEN 9 channel polynomials/values (Import Ledger §7).

---

**DZT-OPEN-0B — Amplitude-norm law (2-power property)** [RID: DZT-OPEN-NORM-LAW]

Status: ACTIVE (finite-horizon result in hand; all-$p$ open)
Result so far: `[ALG finite horizon]` $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)=2^{-k_p}$ for $p=12,16,20,24,28,32,36$ — a pure 2-power, no odd prime in the amplitude norm (DZT-ALG-CASCADE-NORM-2POWER, §6.3).
Open: (i) prove the 2-power property for **all** $p\equiv0\bmod4$. This is DZT-owned (transform-level) but **gated on the Dyadic all-$p$ factorization** $Q_p=i\zeta_p^3 M_p$, i.e. their link (R): until (R) closes, $M_p\in\mathbb{Q}(\zeta_p)^+$ is itself only finite-horizon. (ii) explain the support-on-2 structurally — candidate route via the all-$p$ leading cancellation (LEAD), with $Q_p$ a subleading remainder divisible by powers of the prime above 2. (iii) secondary: a closed form for $k_p$ (not pursued from 7 points; would need either many more points or a structural handle). Negatively resolved if some $4\mid p$ gives an odd prime in $N_+(M_p)$.

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
| Amplitude norm | 2-power $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)=2^{-k_p}$ on finite horizon `[ALG fin-hor]` | all-$p$ 2-power claim (gated on Dyadic (R)); any closed $k_p$ law | §6.3 |
| Phase-law import | $Q_p=i\zeta_p^3M_p$ as Dyadic `[ALG fin-hor]` | reading it all-$p$ or as a zeta-continuation (needs (R); SG-DZT-4) | §6.3, §7 |
| Cyclotomic transform | vanishing $\iff \Phi_p\mid P_C$ `[ALG]` | a $p^{-s}$/RH/Euler-product reading | §1 |
| $\lambda_6$ vs $\zeta_p$ | distinct except $p=6$ (SG-DZT-7) | identifying them at general $p$ | §3 |
| AZ graph-zeta relation | none without bridge (SG-DZT-1) | DZT continues/validates AZ Thread C | §3 |

---

## §6. Main Scientific Ledger {#sec-6-ledger}

### §6.1 The channel transform `[DEF]` {#sec-6-1-transform}

`[DEF]` For $P_C\in\mathbb{Q}[x]$ (or a number-field channel value), $R_C(p)=\mathrm{Res}(\Phi_p,P_C)=\prod_{\zeta_p}P_C(\zeta_p)\in\mathbb{Q}$ (integer when $P_C\in\mathbb{Z}[x]$). `[ALG]` Standard resultant theory: $\Phi_p$ monic and irreducible over $\mathbb{Q}$ is the minimal polynomial of $\zeta_p$, so $R_C(p)=0\iff\Phi_p\mid P_C\iff P_C(\zeta_p)=0$. The transform is channel-indexed; cross-channel comparison is the intended observable.

### §6.2 DZT-OPEN-0A, $b=5$ row `[RESULT]` `[from: ALG]` {#sec-6-2-b5-row}

`[import-ref]` Channel polynomial (Dyadic DYAD-OPEN-B5-ALLP): $N(x)=2x^6+x^5-5x^4-3x^3-4x^2+2x+1$, with the certified statement $\Phi_p\nmid N$ for all $p$ (cyclotomic non-division; $\deg N=6\Rightarrow$ exception set $\varphi(p)\le6$, all checked).

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

### §6.3 Cascade amplitude-norm law `[ALG finite horizon]` {#sec-6-3-nearmiss-norm}

`[import-ref]` `[from: DYAD-ART-CASCADE-Q4-03, DYAD-THM-P1, DYAD-ALG-PHASELAW]` Each $q=4,(0,3)$ cascade value factors as $Q_p=i\zeta_p^3 M_p$ with $M_p=|Q_p|\in\mathbb{Q}(\zeta_p)^+$ (positive real); the direction $i\zeta_p^3$ is universal ($\lambda^{-s}=-i$ for all $4\mid p$, Dyadic all-$p$ THM). Reality of $M_p$ is Dyadic `[ALG finite horizon]` pending their (R)-link; DZT re-verified it pointwise at every horizon $p$.

`[ALG]` `[RID: DZT-ALG-CASCADE-NORM-2POWER]` `[scope: finite horizon p∈{12,16,20,24,28,32,36}]` The real-subfield norm is a pure 2-power:
$$N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)=2^{-k_p},\quad (k_p)=(2,3,2,3,3,5,3),$$
equivalently $\mathrm{Res}(\Phi_p,M_p)=N_{\mathbb{Q}(\zeta_p)/\mathbb{Q}}(M_p)=2^{-2k_p}$. No odd prime divides the amplitude norm; the amplitude is supported only on the prime above 2 (ramified in $\mathbb{Q}(\zeta_p)^+$, $4\mid p$). Machine-verified `dzt_0b_normlaw.py` (exit 0; $p=16$–$28$ extract-vs-md cross-checked, $p=32,36$ modulus-gated against the Dyadic table).

`[ALG]` `[RID: DZT-ALG-P12-NORM]` The $p=12$ value $v=-13+\tfrac{15\sqrt3}{2}$ has $N_{\mathbb{Q}(\sqrt3)/\mathbb{Q}}(v)=v\bar v=\tfrac14=2^{-2}$ — the $\varphi/2=2$ member ($k_{12}=2$), the unique horizon point where $\mathbb{Q}(\zeta_p)^+$ collapses to $\mathbb{Q}(\sqrt3)$.

`[HEUR]` Exponent $k_p$ is diagnostic-only; no closed form asserted (7 points, primitive-vs-ratio discipline). The robust result is the 2-power property; the all-$p$ statement and the support-on-2 mechanism are tracked under DZT-OPEN-0B / DZT-HYP-MAHLER-NEARMISS.

---

## §7. Import Ledger {#sec-7-imports}

- [RID: DYAD-OPEN-B5-ALLP] :: $b=5$ channel polynomial $N$ and all-$p$ survival via $\Phi_p\nmid N$ :: `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1` §2/§6.11 :: source for §6.2 :: dyadic map, $b=5$, all $p\ge6$
- [RID: DYAD-ALG-VANISH-B2/B3/B4] :: $F_{\rm raw}^p(0,b)=0$, $p\ge b+2$, no secular mode :: Dyadic §6.11 :: $b\le4$ row of DZT-OPEN-0A :: dyadic map
- [RID: DYAD-ALG-CASCADE-P12] :: $(4,(0,3))$ boundary value $v=-13+\tfrac{15\sqrt3}{2}$, $p=8$ cancels / $p=12$ survives :: Dyadic §2/§6.11 :: source for §6.3, DZT-OPEN-0B :: dyadic map
- [RID: DYAD-ALG-P6-FACEFLUX] :: $\lambda_6=e^{iF_f/2}=e^{i\pi/3}$ resonance eigenvalue :: Dyadic §6.2 :: SG-DZT-7 two-root discipline :: $p=6$ only

All imports `[import-ref]`; ownership remains Dyadic. No AZ, TDR-G, OPEN-M, or Genesis import (firewall SG-DZT-1/2/5).

---

## §8. Artifact and Script Registry {#sec-8-artifacts}

- [RID: DZT-ART-VERIFY-0A] :: `dzt_open_0a_verify.py` :: computes $R_{(0,5)}(p)$ over the horizon sweep and the $p=12$ reduced field norm; reproduces imported $b=5$ survival on the tested horizon (ownership-safe wording) and norm $=\tfrac14$ :: `[ENG]` exit-0
- [RID: DZT-ART-CHANNEL-AUDIT] :: `dzt_channel_audit.py` :: two-layer channel-state audit; certifies $b\le4$ $E_C=0$ structural-absence encoding (no resultant), distinct from $b=5$ $E_C=1$ cyclotomic survival; cascade row intentionally not computed (gated) :: `[ENG]` exit-0
- [RID: DZT-ART-CASCADE-AUDIT] :: `dzt_0b_audit.py` :: re-extracts $Q_p$ from the Dyadic engine, verifies phase law and $M_p\in\mathbb{Q}(\zeta_p)^+$, computes field norms $p=12$–$28$ :: `[ENG]` exit-0
- [RID: DZT-ART-NORMLAW] :: `dzt_0b_normlaw.py` :: full 7-point amplitude-norm computation; establishes the 2-power property (DZT-ALG-CASCADE-NORM-2POWER); extract-vs-md cross-check and modulus gates :: `[ENG]` exit-0
- [RID: DYAD-ART-CASCADE-Q4-03] :: **delivered** Dyadic-owned cascade channel object (Case V: per-$p$ algebraic values $Q_p\in\mathbb{Q}(\zeta_p)$, $p=8$–$36$, $4\mid p$); raw $R^{\rm raw}_{p,4}=\lambda^{-s}f_p^s-\mathrm{Id}$, $s=p/4$, charge-projected on $K^{\rm extra}_{p,4}$, $\chi(a,b)=(a-b-1)\bmod p$ :: extract script sha256 `ecdb805f…05eac2`, horizon md sha256 `14526cf1…7bec16` :: source for §6.3, DZT-OPEN-0B :: regression-gated $p=8\to0$, $p=12\to-13+\tfrac{15\sqrt3}{2}$
- [RID: DYAD-THM-P1] :: $\lambda^{-s}=\zeta_p^{-p/4}=-i$ for all $4\mid p$ (universal direction factor) :: Dyadic phase-law note :: all-$p$ `[THM]`
- [RID: DYAD-THM-REALITY] :: $f^{\bar W}_{(b,a)}=\overline{f^W_{(a,b)}}$, lifting through composition ($J(f^s)=(Jf)^s$); Galois $\sigma_{-1}$ realizes $J$ :: Dyadic phase-law note :: all-$p$ `[THM]`
- [RID: DYAD-THM-LEAD] :: leading $(0,3)$ accumulation $\sum_{k=0}^{s-1}\zeta_p^{-4k}=0$ for $s\ge2$; $Q_p$ is the subleading remainder; explains $p=8$ ($s=2$) total cancellation :: Dyadic phase-law note :: all-$p$ `[THM]`
- [RID: DYAD-ALG-PHASELAW] :: phase law $\arg Q_p=\tfrac\pi2+\tfrac{6\pi}p$, equiv. $Q_p=i\zeta_p^3 M_p$, $M_p\in\mathbb{Q}(\zeta_p)^+$; reduces to link (R) $\sigma_{-1}(A_p)=\zeta_p^{-6}A_p$ :: Dyadic phase-law note :: `[ALG finite horizon]`, all-$p$ open (R); gates DZT-OPEN-0B all-$p$

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

---

## Appendix A — Version History

### v0.4 — June 2026
Integrated the delivered Dyadic cascade artifact (DYAD-ART-CASCADE-Q4-03, hash-pinned) and the Dyadic phase-law findings. **Closed the cascade $(4,(0,3))$ row of DZT-OPEN-0A** at finite-horizon scope (DZT-ALG-CASCADE-ROW): the channel is Case V (per-$p$ algebraic value, complex for $p\ge16$), so the transform is the real-subfield norm in $\mathbb{Q}(\zeta_p)^+$, not a $\Phi_p$-resultant; reproduces $p=8$ cancellation and the $p=12$ value. **Registered DZT-ALG-CASCADE-NORM-2POWER** (`[ALG finite horizon]`, $p=12$–$36$): $N_{\mathbb{Q}(\zeta_p)^+/\mathbb{Q}}(M_p)=2^{-k_p}$ is a pure 2-power — no odd prime in the amplitude norm; exponent $k_p$ kept diagnostic-only (no overfit). **Corrected DZT-DEF-AMBIENT-FIELD**: the cascade norm target is $\mathbb{Q}(\zeta_p)^+$; the $\mathbb{Q}(\sqrt3)$ reading was a $p=8,12$ artifact. Recontextualized DZT-ALG-P12-NORM as the $\varphi/2=2$ family member; reframed DZT-HYP-MAHLER-NEARMISS to the all-$p$ 2-power question + support-on-2 mechanism. Rewrote DZT-OPEN-0B to the amplitude-norm-law target (all-$p$ gated on the Dyadic (R)-link). Imported three Dyadic all-$p$ theorems (DYAD-THM-P1 $\lambda^{-s}=-i$, DYAD-THM-REALITY, DYAD-THM-LEAD) and the phase law (DYAD-ALG-PHASELAW, `[ALG finite horizon]`). Added artifacts `dzt_0b_audit.py`, `dzt_0b_normlaw.py`. No change to the founding object or guards SG-DZT-1–8.

### v0.3 — June 2026
Closed the $b\le4$ structural-absence sub-item of DZT-OPEN-0A. Built `dzt_channel_audit.py` (`[ENG]`, exit 0) implementing the two-layer channel state: for $b\in\{2,3,4\}$ at $p\ge b+2$ the transform reports $E_C=0$ (structural/secular absence, no $P_C$, no resultant), certified distinct from the $b=5$ $E_C=1$ cyclotomic-survival contrast class. Registered DZT-ALG-B234-STRUCTURAL (`[ALG]` `[scope: channel-state encoding test]`). Cascade row left Dyadic-gated (no scope change). No change to the founding object, definitions, or guards.

### v0.2 — June 2026
Ruling-consolidation patch over v0.1 (four critique-round rulings). Added the **two-layer channel state** DZT-DEF-CHANNEL-STATE (`[DEF]`): secular-content indicator $E_C(p)$ separating structural/secular absence ($b\le4$) from cyclotomic cancellation/survival, so structural vanishing is never encoded as a resultant zero. Added the **compositum ambient field** DZT-DEF-AMBIENT-FIELD (`[DEF]`): $K_{C,p}=F_C\cdot\mathbb{Q}(\zeta_p)$ as the honest default, with subfield-reduced norms recorded but not claimed as native. Reframed DZT-ALG-P12-NORM as a *reduced* norm in $\mathbb{Q}(\sqrt3)\subseteq K_{C,12}$. Made the cascade $(4,(0,3))$ row of DZT-OPEN-0A and all of DZT-OPEN-0B **Dyadic-extraction-gated**: the channel polynomial $P_{(4,(0,3))}$ must be emitted Dyadic-side as DYAD-ART-CASCADE-Q4-03 before promotion; DZT runs only a quarantined shadow reconstruction (SG-DZT-3). Patched `dzt_open_0a_verify.py` output wording so the all-$p$ certification is attributed to Dyadic (DYAD-OPEN-B5-ALLP) and only the finite horizon sweep to DZT. No change to the founding object, guards SG-DZT-1–8, or import ownership.

### v0.1 — June 2026
Initial founding charter. Registered the channel-fixed cyclotomic/resultant transform `[DEF]` (DZT-DEF-CHANNEL-TRANSFORM) as Track A primary; demoted Dirichlet $p^{-s}$ to a derived secondary diagnostic `[HEUR]`; registered Track B1 (formal local NF zeta, `[OPEN]`) and Track B2 (analytic transfer zeta, deferred `[OPEN]`). Registered DZT-ALG-P12-NORM (`[ALG]`, norm $=\tfrac14$) and DZT-HYP-MAHLER-NEARMISS (`[HYP]`). Completed the $b=5$ row of DZT-OPEN-0A (`[RESULT]` `[from: ALG]`, reproduces certified survival). Installed scope guards SG-DZT-1 through SG-DZT-8 and the Dyadic Import Ledger. Maturity Level A; OPEN-P0 ceiling inherited.

## Appendix B — Retired and Rejected Claims

`[RETRACTED | RID: DZT-RETRACT-MAHLER-RESULT]` Earlier draft phrasing called the $p=12$ near-miss a "small-Mahler-measure signature" in `[RESULT]` voice. Reason: the norm computation is exact `[ALG]` but the *mechanism* identification is not earned at v0.1. Replaced by: DZT-HYP-MAHLER-NEARMISS `[HYP]` (§6.3). Version: v0.1.

---

*END OF DOCUMENT — RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.4*
*Founding charter for the continuous-branch arithmetic-resonance transform study (DZT). Imports Dyadic OPEN 9 by reference only; quarantines AZ Thread-C graph-zeta; inherits the OPEN-P0 ceiling. All transform definitions, identities, and diagnostics are DZT-owned; all underlying $p$-resonance facts remain Dyadic-owned.*
