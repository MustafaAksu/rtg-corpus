# Triadic — Stage 2 driver / coverage / pilot receiving review

**13 October 2026 · NONCANONICAL · NOT A REGION CERTIFICATE.** Source artifacts were read directly from the delivered paths; no Triadic, Genesis, RER, or producer source was modified.

## Source manifest

- `triad_tm_engine_v3.py`: SHA-256 `78a5e434073165b37e9e5457766b6d21edb63e51d076172f4ac92052c63bfd18`.
- `triad_stage2_driver.py`: SHA-256 `5268d037ba15ec7f7787e8cb2b67e6918479283ee12cae8635b33290e1f78e63`.
- `triad_stage2_coverage.py`: SHA-256 `2b5a9ff81f97af068d29f0293f459b58ba3defbc78bd2533a055caacd122555b`.
- `stage2_config.json`: SHA-256 `73389a2b83bac9fd2c55db779c9509c4865edada2d830568f97782a5ec455549` (K=8).
- `stage2_pilot_K6.jsonl`: SHA-256 `f103d1da35e9cc3401cc22f3049280546ea95c8eab877c763fd79fdfdc1490ed` (K=6, separate config hash `ca2619cc…`).
- Handoff note: SHA-256 `b975c5df70e8a53a92ff7adfc7e348be814e74efc7b9e9982362790965b139b1`.

## Confirmed

1. **Exact arithmetic geometry of tiling.** The plan has 272 inner and 180 outer spatial boxes per tau layer, times two tau layers: 904 boxes per N, 1808 (box,N) jobs. The structural covering proof is valid given the input region and the square-selection inequality. A 20,000-point sampled check found zero misses; that check is supplemental, not the proof.
2. **v2 → v3 scope.** The core six-step Taylor-model recurrence, multiplication and analytic remainder formulas are unchanged in source diff. V3 adds configuration, step logs, lower annulus radius, and B-transverse defect calculations. Consequently “no arithmetic change” means *no change to the old core recurrence*, not literal identity of all calculations or all outputs.
3. **K6 pilot.** Eight PASS rows (four boxes × N=7,8), all six step records present. Published `K_up` exceeds each recorded `K_raw`. The file is not a whole-domain certificate. No completed K8 pilot JSONL was attached in this delivery.
4. **Actual incomplete state.** Running the supplied coverage script against the attached K8 config exits 1 with 904 missing boxes for each N, as expected before the sweep.

## Blocking current-use/governance issues before whole-region acceptance

**G1 — [BLOCK] The coverage aggregator trusts unvalidated PASS records.** It checks only `(box_id,N)`, `status=PASS`, and the three hashes. It does not check recorded endpoints, degree K, precision, kt, R_floor, six-step records, or numerical consistency. In an isolated negative test with all 1808 planned IDs, matching hashes, wrong endpoints (`999..1000`), empty step lists, and zero fictitious bounds, the original verifier exited 0 and printed `CERTIFIED ... K_7=K_8=0`. This does not imply the real pilot values are wrong; it means the coverage program must not confer certification. Add strict per-record schema/plan reconciliation, reject conflicting duplicates, enforce finite nonnegative upper values and K_up>=K_raw, and retain engine-proof review as an independent gate.

**G2 — [BLOCK] Parallel output instructions conflict with config hashing.** The proposed process is to alter `results` in two config copies (one per ring), concatenate results and run one verifier. But `results` is part of the SHA-256 of the full config: the inner and outer copies acquire distinct hashes. Neither can be accepted under the other config. Add a CLI `--results` override that selects only the output path *without changing the hashed mathematical config*, or define a canonical semantic config hash excluding output path. Use separate files per worker and merge only records with the same canonical contract.

**G3 — [BLOCK for future extension] Engine ignores the configured poly file and kt selector.** The driver hashes `CFG['poly']` and logs `KT`, but the engine imports the fixed `age_family_polynomials_kt1.json` and contains fixed kappa-tilde=1 mathematics. A config edit could therefore attest to the wrong coefficient set. For now require `KT='1'` and `poly='age_family_polynomials_kt1.json'` with fatal assertions; or make engine load the given file explicitly before evaluating boxes.

**G4 — [SCOPE] Upper-bound ratio is not an actual transverse fraction.** The pilot has independent upper enclosures `K_up` for total defect and `K_perp_up` for transverse defect. Their quotient, even if 0.98–1.19, does not prove the actual defect is predominantly transverse. In fact `K_perp_up > K_up` is possible because the bounds have different slack. Claim only that the independently calculated transverse *upper bounds* are numerically comparable. A positive transverse lower bound would require additional sign/enclosure information.

**G5 — [GUARD] Formatting an interval upper endpoint through `mp.mpf` is not a proven outward decimal conversion.** `upq` first converts an interval endpoint to ordinary floating precision with `mp.nstr`, then rounds that result up. It happened to leave positive headroom in all eight delivered pilot rows, but a rigorous aggregation should round directly from the exact binary endpoint, using directed conversion or a conservative epsilon with proof. The same applies to logs of R_eff and intermediary bounds: preserve outward endpoint semantics when serializing.

**G6 — [SCOPE] Pilot cannot establish K8 optimum.** Only the first pilot box's K=8 comparison is printed in the note, with other K8 jobs marked “running”; a complete K8 pilot file was not supplied. Thus K=6 is a reasonable computational candidate, not yet a domain-optimality theorem.

## Proposed acceptance order

1. Patch G1–G3 before any long sweep; rerun negative controls that wrong endpoints, wrong K, and altered config hashes must be rejected.
2. Record G4–G6 as scope/serialization safeguards; obtain complete K8 short pilot and independent review of Taylor-model remainder lemmas.
3. Retain mathematical config identity across inner/outer worker outputs and generate a separate, exact-rational coverage manifest for all 904 boxes per N.
4. Run only a small fail-fast resume/merge experiment first. Full RTG-machine sweep follows review of that experiment; only then propose K_7,2 / K_8,2 for RER, with the known normal/component distinction.

## Disposition

`MODEL/TM CORE: no new mathematical rejection`; `TILING PLAN: ACCEPT`; `K6 PILOT: source-reported / internally checked`; `COVERAGE/RESUME AS CERTIFIER: REVISE`; `K8 PILOT: INCOMPLETE IN ATTACHED MATERIAL`; `FULL REGION CERTIFICATE: OPEN`.

No physical closure, long-time observable control, physical birth threshold, new owner theorem or memory mechanism is adopted.
