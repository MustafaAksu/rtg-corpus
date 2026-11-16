# First-contact tables — script, manifest and validation (for review; not frozen)

**[SESSION] NONCANONICAL.** Implementation of the table contract of `records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md` §5 by the Claude AZ lane, 16 November 2026, at the request recorded in PR #281 comment `6919043197`. Exploratory: the outcomes of the registered records are known.

**No registered record has been read by this script.** With `--plan registered` it refuses unless the manifest's `frozen_script_sha256` equals its own SHA-256 and the input hashes match (`contact_tables_negcontrols_output.txt`, NC6, NC7). The manifest is committed with `frozen_script_sha256: null`. Freezing is a later, reviewed commit that sets the field; only then may the tables be produced, once, and the output stored.

| File | Role |
|---|---|
| `az_tokres_contact_tables.py` | descriptors and tables T1–T4, J1–J4; Stage 1 validator reused unchanged (identity, custody, states re-derivation, records, set); pairing keys checked (`th0` and the three non-slot tokens equal to `BASE`) |
| `contact_tables_manifest.json` | **proposal**: cell `S1-C1` only (`(120, 8)`, profile P1); arms; pairs `O1R/O1D`, `O2R/O2D`; endpoint `M ≥ 100` at tick 800 (cap before 800 positive); time grid; `t_b = 100` for J4; input `upload/az-token-resonance-stage1/HASHES.txt` by hash |
| `contact_tables_selftest_output.txt` | synthetic checks, `SELFTEST PASS` |
| `contact_tables_test_output.txt` | the tables on Stage 1 **test-configuration** records (tag `SMOKE`, cells `TEST-C1`, `TEST-C2`; no evidential value) |
| `contact_tables_negcontrols.py`, `..._output.txt` | eight controls on copies of those records, `NEGCONTROLS PASS` |

**Self-test** (synthetic, own seed): first-contact time, whole edge set and component-type multiset equal the pinned engine's own pre-interaction snapshot on 1,860 states over seven `(N, k)` incl. `(12, 0)`; the `t = N` fixture; the paired counterexample of design §4.2 (and that it is not strict); the stationary `K2,2`; no-contact-ever; slot periods 1, 2, 4; covariance under a common phase shift, a common advance shift and node relabelling; refusal of invalid input; runner `fb` = engine `birth_steps_list[0] + 1` on 60 synthetic runs (growth values not printed); the freeze gate.

**Negative controls**: a dropped record; a duplicated record file; pairing keys swapped between two base draws; a wrong engine pin; a record file edited after the run; registered plan unfrozen; registered plan with a wrong input hash — each refused, no table printed.

**Reproduce the test output:** `python3 -I evidence/az/scripts/az_tokres_campaign.py --plan test --out DIR --jobs 2`, then `python3 -I evidence/az/mechanism/az_tokres_contact_tables.py --manifest evidence/az/mechanism/contact_tables_manifest.json --dir DIR --plan test` (the records differ only in `secs`; the tables do not use it).

**Choices for review and the PI** (each listed in the manifest; none taken by looking at a table): the cell (`S1-C1` alone, or also `S1-C2`; Stage 2 cells would need a Stage 2 validator path, not written); `t_b` of J4; the time grid; whether `SHAM` and `Q2R` stay as descriptor-only arms.
