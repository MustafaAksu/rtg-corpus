# RTG OPEN-M v0.7.1 — Calibration/Target-Typing Errata Change Record

**Date:** 7 October 2026  
**Revision editor:** ChatGPT  
**Base:** adopted `RTG_OPEN_M_DSN_v0.7`  
**Accepted candidate:** `RTG_OPEN_M_DSN_v0_7_1_DRAFT2.md` — SHA-256 `ebbf23ea99fb281624accafb573a4e4b127a577da92956e778a37329fb41db95`  
**Released owner file:** `RTG_OPEN_M_DSN_v0_7_1.md` — SHA-256 `0a51644de0a15035797ab03945207cf319fd6d7514a04b8cae441d9d6e93f53e`  
**Status:** ADOPTED owner errata release; change record finalized at release with no scientific disposition change.  
**Scope:** Errata only. No new ESM growth run, Hodge recomputation, BCH certificate, Genesis campaign, or physical closure.

## E071-01 — R15 cancellation / calibration status

**Finding.** `open_m_2f_rho_assembler.py` uses `m=C_m*h`; therefore `h` cancels exactly from the total:

\[
\rho r^4=\frac{h\ell}{gm}r^4=\frac{\ell Q_s^2}{gC_m}.
\]

The reported `0.007–0.008` uses the measured proxy statistic `ell := sigma(z_centered)` plus `C_m=1`, scalar `g=1`, and `Q_s=0.1`. The Hodge amplitude campaign does not determine the total value.

**Disposition.** R15 is retagged/reworded as `[NUM diagnostic] [scope: calibration-conditional]`. The old physical “~4× source deficit” interpretation is superseded. Band values are explicitly source-fraction attributions; because `f_band<=1`, their gate failures are not independent tests when the total is already below the same target.

**Preservation boundary.** R15 is intentionally removed from the byte-preservation boundary established at v0.7; its prior adopted-v0.7 current-use body is archived verbatim in Appendix B of the v0.7.1 candidate and is validated byte-for-byte against the adopted v0.7 source.

## E071-02 — `Q_s=0.1` and state/window matching

**Finding.** Genesis v2.8.5 declares the primitive window `Q_s in (0,0.1]`; the assembler uses its upper edge. The Genesis reduced-wrapper control-loss value varies across its initial-state window, and the `|alpha_f| >= 0.012` value is a model-dependent estimate rather than a universal state-independent threshold.

**Disposition.** `Q_s=0.1` is recorded as an evaluation convention / favorable window edge, not a selected physical state. R11 gains a state/window matching obligation before its target can be compared physically with R15.

## E071-03 — RESULT-M-3A: `K_vac` versus Genesis `g`

**Finding.** THM-3G is OPEN-M-native and protects the scalar log-conformal stiffness equal to bare `K_vac` against relaxation in the tested topology class. Genesis `g` is the isotropic coefficient of the transverse covariant restoring block `M_spin2: V -> V*`. No owner theorem identifies these coefficients.

**Disposition.** `g=K_vac` is reclassified as an OPEN calibration bridge. The import/routing ledger is corrected so Genesis is no longer listed as the source of THM-3G. Pre-Legacy supplies historical vacuum/log-frustration stiffness provenance; THM-3G remains branch-native.

## E071-04 — RESULT-M-3B: finite-`g` norm audit

**Finding.** Under the conditional 9C family, Genesis gives

\[
\lambda_\pm=\frac{2D+4g}{3}\pm\frac23\sqrt{4D^2+4Dg+g^2+3m^2\Im(w)^2},
\]

and `||M||_B -> 2g` only on the large-positive-`g` branch. The registered soft branch has `|D|/g=1/2`; for `Im(w)=0`, `||M||_B/g = 1,2,3` at `D/g=-1/2,0,+1/2`.

**Disposition.** `0.024` is no longer treated as certified at `g=1`. R11/R7/high-risk text now mark it as reduced-wrapper + conditional-9C + large-`g` scoped. No direction of correction is inferred.

## E071-05 — Target-side status

**Finding.** Genesis explicitly states that `0.024` uses both `||M||_B -> 2g` and the reduced-wrapper estimate `|alpha_f| >= 0.012`; it is not a first-principles OPEN-M threshold.

**Disposition.** The candidate does **not** replace R11 with a new exact-norm formula. It registers `OPEN-M-3C exact-target re-derivation` as a follow-on study: start from the underlying wrapper condition, use the exact admitted restoring norm, and match the physical state/window.

## E071-06 — Headline / deficit-factor correction

**Finding.** Both sides of the former `0.007–0.008 vs 0.032` comparison contain unresolved calibration/typing assumptions.

**Disposition.** Current headline becomes: **there is no certified numerical OPEN-M deficit factor; its magnitude is undetermined in either direction.** This does not imply a smaller or larger physical gap.

## E071-07 — Provenance correction

**Finding.** v0.7 incorrectly listed “THM-3G `g=K_vac` calibration input” as a Genesis → OPEN-M import.

**Disposition.** Corrected in §4 and §7. Genesis owns the reduced target, typed norm/spectrum, and 9C conditionality; THM-3G is OPEN-M-native. Historical `K_vac` provenance remains Pre-Legacy scoped.

## Preserved content

- R12, R13 and R14 numerical bodies are byte-identical to adopted v0.7.
- Existing v0.7 source-proxy and corridor-localization correction blocks remain intact.
- ERR-M-2F-CONV, ERR-M-2F-THRESH and SG-M-ESM-CAL remain in force.
- No numerical data point, Hodge decomposition, trajectory correlation, band fraction, or Triadic/Genesis reconciliation from v0.7 is altered.

## Follow-on ordering

1. OPEN-M-6 full-map/observable source-coupling audit.
2. R16 constitutive/source bridge.
3. OPEN-M-3C exact-target re-derivation.
4. OPEN-M-5 physical 9C selection.
5. OPEN-M-2E-a, then pure-topology growth only after source/target normalization is sufficiently fixed.
