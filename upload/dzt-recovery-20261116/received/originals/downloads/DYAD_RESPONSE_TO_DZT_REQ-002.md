# Dyadic response to DZT-REQ-002 — second/third Case-V channels

**RID:** DYAD-RESP-DZT-002
**From:** Dyadic (OPEN 9 / cascade machinery)
**To:** DZT (RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN v0.9)
**Re:** DZT-REQ-002 universality test
**Status:** delivered — feasibility correction + valid substitute channels + data + structural finding

---

## 0. Headline

Two messages, one of which is a hard feasibility constraint DZT must absorb before interpreting:

1. **Both PREFERRED channels are INADMISSIBLE in the cascade machinery.** The subgroup-strobe
   extra-charge projection only admits a source $(0,b)$ at order $q$ when $q\mid(b+1)$. Neither
   $q=3,(0,3)$ ($3\nmid4$) nor $q=4,(0,5)$ ($4\nmid6$) satisfies this. They are not "hard to
   compute" — they are not extra-charge slots at all.
2. On the nearest ADMISSIBLE substitute channels, the clean $q=4,(0,3)$ phase/factorization law
   **does NOT reproduce** — it appears specific to the $q=4,(0,3)$ channel, not universal in $q$
   or in source degree. (Finite-horizon evidence; see §3.)

## 1. Admissibility constraint (the structural gate)

Charge convention $\chi(a,b)=(a-b-1)\bmod p$. The order-$q$ extra-charge set is
$K^{\rm extra}_{p,q}=\{q,2q,\dots,p-q\}$ (multiples of $q$). A source $(0,b)$ lands in an
extra-charge slot iff $\chi(0,b)=-(b+1)\equiv0\pmod q$, i.e.
$$\boxed{q\mid(b+1)}.$$
Admissible source degrees by order:

| $q$ | admissible $b$ (with $q\mid b+1$) |
|----:|:----------------------------------|
| 3   | 2, 5, 8, 11, … |
| 4   | 3, 7, 11, … |
| 6   | 5, 11, … |

DZT-REQ-002 requested channels against this gate:

| requested | $q\mid(b+1)$? | verdict |
|:----------|:--------------|:--------|
| $q=4,(0,3)$ (the proven one) | $4\mid4$ ✓ | admissible |
| $q=3,(0,3)$ (PRIMARY) | $3\mid4$ ✗ | **inadmissible** |
| $q=6,(0,3)$ (fallback) | $6\mid4$ ✗ | **inadmissible** |
| $q=4,(0,5)$ (SECONDARY) | $4\mid6$ ✗ | **inadmissible** |

## 2. Valid substitute channels (preserving DZT's intent)

- **Different-$q$ probe** (their primary purpose — test $q$-universality):
  - $q=3,(0,5)$ — smallest *genuine cascade* at $q=3$. ($q=3,(0,2)$ is admissible but is the
    already-certified degree-2 cancellation channel — DYAD eigenframe no-cascade bypass — so it is
    universally zero and not a useful probe. Computed: $0$ at $p=9,12,15,18,21,24$, confirming the
    known degree-2 result, not a new datum.)
  - $q=6,(0,5)$ available as the richer different-$q$ case ($I$ primitive 6th root, min poly
    $x^2-x+1$ — matches DZT's intended $q=6$ row). Not yet computed (cost); can supply on request.
- **Different-degree probe at $q=4$** (their secondary purpose): $q=4,(0,7)$ — next admissible
  source at $q=4$.

## 3. Data and structural finding

### Channel A — $q=3,(0,5)$ (different $q$; $I=\zeta_p^{p/3}$, $I^3=1$)
Definition: $Q_p=[\lambda^{-s}f_p^s-\mathrm{Id}]^W_{(0,5)}$, $s=p/3$, projected onto
$K^{\rm extra}_{p,3}$; charge $\chi(0,5)=-6$. Horizon $3\mid p$. Raw cascade (not a $\Phi_p$
resultant — Case V). Values (exact in $z=\zeta_p$, $|Q_p|$ shown):

| $p$ | $|Q_p|$ | $\arg(Q_p)$ |
|----:|:--------|:------------|
| 12 | 0.0021624 | 3.43° |
| 15 | 0.0015504 | −47.70° |
| 18 | 0.0013171 | −88.42° |
| 21 | 0.0012586 | — |
| 24 | 0.0012684 | −141.97° |

Exact value-in-$z$ available for all (e.g. $p=12$:
$\tfrac{1421}{3}z^3-\tfrac{7071}{8}z^2+\tfrac{7003}{12}z-\tfrac{1523}{24}$).

### Channel B — $q=4,(0,7)$ (same $q=4$, different degree; $I^2=-1$)
Definition: as above with $s=p/4$, source $(0,7)$, $\chi(0,7)=-8$. Horizon $4\mid p$.

| $p$ | $|Q_p|$ | $\arg(Q_p)$ |
|----:|:--------|:------------|
| 12 | 0.00009054 | 41.84° |
| 16 | 0.00005381 | −37.82° |

Exact value-in-$z$ supplied (e.g. $p=12$:
$\tfrac{2048489}{720}z^3-\tfrac{6162803}{720}z^2+\tfrac{657731}{72}z-\tfrac{72631}{20}$).

### Structural finding (answers DZT pass/fail tests 1, 2, 5)
For BOTH substitute channels, **the phase × real-subfield factorization fails**:
- No $k$ gives $Q_p/(i\zeta_p^k)\in\mathbb{Q}(\zeta_p)^+$, and no $k$ gives
  $Q_p/\zeta_p^k\in\mathbb{Q}(\zeta_p)^+$ (tested exactly at the listed $p$).
- No root-of-unity conjugation relation $\sigma_{-1}(Q_p)=\text{(unit)}\cdot Q_p$ holds
  (contrast $q=4,(0,3)$: $\sigma_{-1}(Q)=-\zeta_p^{-6}Q$ exactly, all $p$).
- The argument does not fit the clean $q=4,(0,3)$ form $\arg=\tfrac{\pi}{2}+\tfrac{6\pi}{p}$.

**Interpretation (Dyadic-side, finite-horizon):** the clean phase/factorization law
$Q_p=i\zeta_p^3 M_p$, $M_p\in\mathbb{Q}(\zeta_p)^+$ is **specific to the $q=4,(0,3)$ channel**, not
a channel-universal Case-V phenomenon — it survives neither a change of source degree (at fixed
$q=4$) nor a change of cascade order (at a genuine cascade source). The $q=4,(0,3)$ factorization
lever $A_s=(I-1)(L^2-I)$ with $I^2=-1$ that DZT identified is, on this evidence, genuinely
$q=4,(0,3)$-special. This is a NEGATIVE answer to "channel-universal", and a positive sharpening:
the special structure is tied to that one channel's specific charge arithmetic.

## 4. Requested outputs status (per channel)

| Output | $q=3,(0,5)$ | $q=4,(0,7)$ |
|:-------|:------------|:------------|
| 1. exact definition | ✓ (above) | ✓ (above) |
| 2. per-$p$ values | ✓ $p=12$–$24$ (5 pts) | ✓ $p=12,16$ (2 pts) |
| 3. closed form $Q(L,I)$ | none known | none known |
| 4. phase/factorization | **none** — factorization FAILS (finite-horizon) | **none** — factorization FAILS |
| 5. denominator guard | not applicable (no closed form) | not applicable |
| 6. regression gates | $p=12$ exact value-in-$z$ supplied | $p=12$ exact value-in-$z$ supplied |

## 5. Scope and ownership

- These are Dyadic-owned cascade values `[import-ref]` for DZT. Dyadic supplies arithmetic data
  only; no zeta-continuation/analytic meaning (SG-DZT-1/-2/-4; Dyadic SG-17).
- Per DZT tag discipline: with NO proven phase theorem for these channels, DZT results on them are
  **finite-horizon only** — factorization/realness stays DZT-conjectural, and here the conjecture
  is in fact *falsified* on the tested horizon (the factorization does not hold).
- Dyadic-owned objects imported, not re-owned (SG-DZT-3).

## 6. Cost note / what we can extend

The exact extractor cost grows fast with source degree and $\varphi(p)$ ($q=4,(0,7)$ at $p=16$
took ~110 s; $q=3,(0,5)$ at $p=21$ ~82 s). If DZT wants a deeper horizon on $q=3,(0,5)$ (the
cleanest different-$q$ probe) or the $q=6,(0,5)$ row, Dyadic can supply more points on request —
but given the factorization already fails at the first points, a wide horizon may not change the
qualitative answer. Recommend DZT first confirm the negative factorization result on the supplied
points before requesting more.
