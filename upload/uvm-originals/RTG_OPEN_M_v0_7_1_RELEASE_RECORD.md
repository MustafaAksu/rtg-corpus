# RTG OPEN-M v0.7.1 — Owner Release Record

**Date:** 7 October 2026  
**Decision:** ADOPTED — designated OPEN-M owner errata release.  
**Supersedes:** `RTG_OPEN_M_DSN_v0.7`  
**Accepted candidate:** `RTG_OPEN_M_DSN_v0_7_1_DRAFT2.md`  
**Accepted candidate SHA-256:** `ebbf23ea99fb281624accafb573a4e4b127a577da92956e778a37329fb41db95`  
**Released owner file:** `RTG_OPEN_M_DSN_v0_7_1.md`  
**Released owner SHA-256:** `0a51644de0a15035797ab03945207cf319fd6d7514a04b8cae441d9d6e93f53e`  

## Adoption basis

The owner/reviewer verification found no remaining scientific or documentation findings after the Draft-2 provenance repair. Adoption accepts the reviewed v0.7.1 scientific body and changes release-state metadata/history only.

## Scientific disposition retained

- R15 is a calibration-conditional proxy diagnostic, not a certified physical source-deficit measurement.
- Under `m=C_m h`, `h` cancels and the constructed quantity is `rho r^4 = ell Q_s^2/(g C_m)`.
- `Q_s=0.1` is the upper primitive-window edge, not a derived physical state.
- RESULT-M-3A leaves the `K_vac <-> g` identification open.
- RESULT-M-3B leaves the finite-`g` restoring norm/target calibration open; the familiar `0.024` target is not universal.
- Therefore no certified numerical OPEN-M deficit factor is currently established; magnitude and direction remain undetermined pending the named bridges.

## Preservation boundary

R12-R14 remain byte-identical to adopted v0.7. R15 is intentionally outside that boundary; the complete adopted-v0.7 R15 current-use block is archived verbatim in Appendix B and validated against v0.7. No growth run, Hodge recomputation, BCH certificate, or Genesis certificate was rerun for adoption.

## Next scientific priority

`OPEN-M-6` — full-map/observable source-coupling audit. Subsequent priorities remain the R16 constitutive/source bridge, OPEN-M-3C exact-target re-derivation, OPEN-M-5, OPEN-M-2E-a, and only then the pure-topology growth run.
