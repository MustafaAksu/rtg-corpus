# DZT-REQ-004 — Subleading resonant tower / radial recurrence for the B1 $W^{(B)}$ audit

**RID:** DZT-REQ-004
**Requesting branch:** DZT (RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN, v0.11)
**Target branch:** Dyadic (local NF / germ machinery near $P_1$)
**Mirrors:** DZT-REQ-001/002/003 (all fulfilled)
**Status:** OPEN

## Purpose — a falsification gate for the dilogarithm lead

DYAD-RESP-DZT-003 gave the stamped germ near $P_1$. DZT's $W^{(B)}$ audit (v0.11) found a
**leading-order** local zeta
$$\zeta_{\rm loc}(z)\sim\exp\!\big(\Im(c_{21})\,\mathrm{Li}_2(z)\big),$$
built on the gauge-safe contraction $Q_{m+1}/Q_m=1-Q_m+O(Q^2)$ ($\Re\mu=-\tfrac12$) and the invariant
$c_{21}$. This is `[HEUR]` — it uses only $c_{21}$. This request is the cheap falsification gate:
supply the data that either confirms the $\mathrm{Li}_2$ structure survives the subleading tower or
breaks it.

## The decisive datum (DZT-identified)

The $\mathrm{Li}_2$ form follows from $Q_m\sim1/m$, which holds iff the radial recurrence is
parabolic with no log-correction. For
$$Q_{m+1}=Q_m-Q_m^2+A\,Q_m^3+B\,Q_m^4+\dots,$$
standard parabolic-iteration asymptotics make the **cubic coefficient $A$** control the $\ln m/m^2$
correction to $Q_m$: if it vanishes, $Q_m\sim1/m$ and $\mathrm{Li}_2$ holds; if not, $\zeta_{\rm loc}$
bends into a log-corrected polylog. So $A$ (then $B$) is the primary discriminator — more decisive
than any single high-degree monomial coefficient in isolation.

## Requested data (in the DYAD-RESP-DZT-003 stamped convention: $W_{\rm DSN}$ Birkhoff, normalized_pstep, Lie strict-kernel)

**Primary (the discriminator):**
1. **Radial recurrence for $Q_{\rm true}$ to cubic and quartic order:**
   $Q_{m+1}=Q_m-Q_m^2+A\,Q_m^3+B\,Q_m^4+\dots$ — exact $A$, $B$ if available.
2. **Phase recurrence to matching order:**
   $\theta_{m+1}-\theta_m=\Im(c_{21})\,Q_m+\alpha\,Q_m^2+\beta\,Q_m^3+\dots$ — exact $\alpha,\beta$.

**Supporting (the inputs that determine $A$, $B$):**
3. Resonant monomial coefficients through degree 7 (degree 9 if feasible): $c_{32}$, $c_{05}$,
   $c_{43}$, $c_{16}$, and any other $a-b\equiv1\bmod6$ terms, in the declared gauge.
4. For each: exact algebraic value; layer (normalized_pstep / raw_pstep / F1^p / bridge); gauge
   status (invariant / strict-kernel-stable / gauge-fixed); and whether it feeds radial contraction,
   phase shear, or transverse resonant mixing.

**Structural (if known):**
5. Any identity fixing the radial recurrence — e.g. exactly logistic-like, formally conjugate to a
   known parabolic normal form, or coefficient-defined only.

## DZT-side test and verdicts

DZT will substitute $A$ (and $B$) into the radial asymptotics and check whether
$W_m^{(B)}=\Im(c_{21})\,Q_m$ stays $\sim\Im(c_{21})/m$ (→ $\mathrm{Li}_2$ survives) or acquires a
log-correction (→ deviation).

- **PASS → toward `[ALG]`:** the resonant tower yields a controlled recurrence whose $\zeta_{\rm loc}$
  expansion is *derivable from the germ*, not coefficient-tabulated.
- **FAIL / downgrade:** coefficients don't stabilize into a recurrence, or the $\mathrm{Li}_2$ form is
  destroyed by subleading terms.
- **RETAIN `[HEUR]`:** finite coefficients remain suggestive but insufficient for a recurrence
  theorem.

## Scope guard

Formal local germ near $P_1$ only, using the one-step multiplier $\lambda_6$ — **never** the
cyclotomic $\zeta_p$ of the arithmetic-resonance branch (SG-DZT-7; per DYAD-RESP-DZT-003's explicit
two-root warning). No global Ruelle/transfer-operator/periodic-orbit zeta, RH/prime, OPEN-M, AZ, or
discrete-branch claim follows (SG-DZT-1/-2/-4). Dyadic objects imported, never re-owned (SG-DZT-3).
