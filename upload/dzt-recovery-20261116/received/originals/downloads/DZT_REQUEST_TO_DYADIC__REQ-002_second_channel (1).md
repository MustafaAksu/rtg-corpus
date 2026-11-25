# DZT-REQ-002 — Second Case-V channel for the universality test

**RID:** DZT-REQ-002
**Requesting branch:** DZT (RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN, v0.9)
**Target branch:** Dyadic (OPEN 9 / cascade machinery)
**Mirrors:** DZT-REQ-001 (fulfilled → DYAD-ART-CASCADE-Q4-03, DYAD-CF-Q403, DYAD-THM-Q403-PHASE-ALLP)
**Status:** OPEN (awaiting Dyadic feasibility response)

## Purpose

DZT has closed one all-$p$ theorem on a single channel — the $q=4,(0,3)$ Case-V cascade
(DZT-THM-CASCADE-ODD-SUPPORT, v0.9): $Q_p=i\zeta_p^3 M_p$ with $M_p\in\mathbb{Q}(\zeta_p)^+$, and
odd-prime norm support exactly at $p=8\ell^a$, $\ell^a\equiv1\pmod4$, numerator $\ell^2$. The next
scientific question is whether this arithmetic is **$q=4$-specific, $(0,3)$-specific, or a
channel-universal Case-V transform phenomenon.** This request asks for a second channel (and a
third, cheaper, confirmation channel) so DZT can test that.

## Why the different-$q$ probe is the deep test (structural motivation)

Every $(0,3)$ result rests on the factorization lever
$$A_s=(I-1)(L^2-I),\qquad I=\zeta_p^{p/4},\quad I^2=-1,$$
which is special to $q=4$: $I=\zeta_4$ has minimal polynomial $x^2+1$, and that "$-1$" is what
threads the **mod-4** anomaly condition $\ell^a\equiv1\pmod4$ through the whole proof (via
$n=\mathrm{ord}(L^{s-2})$ and $\Phi_n(1)$). Changing the cascade order changes the minimal
polynomial of $I$ entirely:

| $q$ | $I=\zeta_p^{p/q}$ | min. poly of $I$ | candidate gate |
|----:|:------------------|:-----------------|:---------------|
| 4   | primitive 4th root | $x^2+1$ ($I^2=-1$) | $\ell^a\equiv1\pmod4$ (proved) |
| 3   | primitive cube root | $x^2+x+1$ ($I^3=1$) | mod 3? (unknown) |
| 6   | primitive 6th root | $x^2-x+1$           | mod 6? (unknown) |

So a different-$q$ channel is the only way to learn whether the $\mathbb{Q}(\zeta_p)^+$ reality and
the mod-4 gate are consequences of $q=4$ specifically or of a deeper, $q$-parametrised structure.
(Verified: for $3\mid p$, $I=\zeta_p^{p/3}$ is indeed a primitive cube root, $I^3=1$.)

## Primary request — different cascade order, same source $(0,3)$

Preferred: **$q=3$** on source $(0,3)$. Horizon $3\mid p$, $s=p/3$, $I=\zeta_p^{p/3}$, $I^3=1$.
Fallback if $q=3$ is unsupported/not meaningful in the cascade machinery: **$q=6$**.

## Secondary request — same order $q=4$, different source degree

Preferred: **$q=4,(0,5)$** (or another supported $(0,b)$). Same $4\mid p$ horizon and same
$I^2=-1$ structure, but a different monomial/source degree — tests whether the direction factor
$i\zeta_p^3$ generalises to a predictable degree-dependent phase (e.g. $i\zeta_p^{b}$).

## Requested Dyadic outputs (each channel, if supported)

1. **Exact channel definition:** $q$, source/projection label, charge convention, raw/normalised
   convention, and the valid $p$-horizon.
2. **Per-$p$ values $Q_p$:** an initial horizon covering the first 10–20 nonzero admissible $p$,
   plus any cancellation / zero-degeneracy points (the analogue of $p=8$).
3. **Closed form** $Q(L,I)$ if available, $L=\zeta_p$, $I=L^{p/q}$.
4. **Phase/factorization status:** an analogue of $\sigma_{-1}(Q)=\text{phase}\cdot Q$ if a
   certificate exists, OR an explicit statement that none is yet known.
5. **Denominator guard:** all factors that must be nonzero on primitive $p$-th roots.
6. **Regression gates:** at least one exact small-$p$ and one medium-$p$ value, so DZT can verify
   transcription before computing.

## DZT-side pass/fail tests (what DZT will do with the data)

1. Does $Q_p$ factor as (root-of-unity phase) $\times$ (fixed-field amplitude)?
2. Is the amplitude in $\mathbb{Q}(\zeta_p)^+$, or another natural fixed field (e.g. tied to
   $\mathbb{Q}(\zeta_q)$)?
3. Is the norm governed by a root-of-unity difference such as $1-\zeta_n$ (the $q=4$ mechanism)?
4. Does an odd-prime anomaly law appear, and on what arithmetic-progression gate?
5. Is the result $q$-dependent, degree-dependent, or channel-universal?

## Tag discipline (DZT side)

- `[import-ref]` for any Dyadic-owned channel values supplied.
- `[ALG finite horizon]` for finite value tables / DZT norm computations on them.
- `[THM]` only if Dyadic supplies a proof/certificate of the phase law (analogue of
  DYAD-THM-Q403-PHASE-ALLP); otherwise factorization/realness stays DZT-conjectural `[HYP]`.
- A new channel without a proven phase theorem yields **finite-horizon** DZT results only.

## Scope guard

DZT will not treat finite tables as theorem-grade. No zeta-continuation, RH, prime-distribution,
OPEN-M, AZ, or discrete-branch claim follows from these data (SG-DZT-1, -2, -4). Dyadic-owned
objects are imported, never re-owned (SG-DZT-3). Two-root discipline $\lambda_6$ vs $\zeta_p$ is
maintained per SG-DZT-7 (relevant now that $q=6$ enters).
