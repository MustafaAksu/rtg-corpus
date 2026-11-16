# First-contact tables — script, manifest and validation (for review; not frozen)

**[SESSION] NONCANONICAL.** Implementation of the table contract of `records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md` §5 by the Claude AZ lane, 16 November 2026, at the request recorded in PR #281 comment `6919043197`. Exploratory: the outcomes of the registered records are known.

**No registered record has been read by this script.** Revision r2 (16 November 2026) closes R1–R4 of review `5922692022` in one pass; the frozen Stage 1 library is unchanged.

**Gates, all before any record file is looked up** (R1, R2): `--plan test` accepts only `TEST-C1`, `TEST-C2` (tag `SMOKE`, not confirmatory), `--plan registered` only `S1-C1`, `S1-C2` (tag `AZ-TOKRES-S1`); a mixed or unknown list is refused; the Stage 1 registry entry must also match the plan. `--plan registered` needs `frozen_script_sha256` equal to the script's SHA-256 and exactly one input with `hashes_file`, `sha256` and `commit`. The manifest's `pins` must equal the script's pins and the bytes on disk before engine, orientation reference, runner or library is imported. Every selected record file and side manifest is bound to the one trusted list (registered: the repository `HASHES.txt` pinned by hash; test: the directory's own `HASHES.txt`) — a listed piece that is missing, an unlisted file, a duplicate or a hash mismatch is refused.

**Clock and endpoint layer** (R3), after the Stage 1 validator: `fe`, `fb`, `t100` are `None` or integers in `1..steps`; `fb` present iff births > 0; `t100` present iff `M ≥ 100`; checkpoints exactly the ticks `≤ steps`, non-decreasing, equal to `M` at the last tick; `M = 4 + births`; stop reason consistent; no event without a contact; `fe ≥ tau_contact`, `fb ≥ tau_contact`, `fe ≤ fb`, `t100 ≥ fb`. A missing tick-800 checkpoint is positive only for a valid cap stop before tick 800, otherwise refused. Any violation is an integrity failure, not a table entry.

**Outputs** (R4): T4 now pairs all four clocks (`tau_contact`, `fe`, `fb`, `t100`) with "not attained" kept as its own category and paired attainment on the grid; T2 prints full edge-set and relative-period-triple distributions; `--json` writes every per-record descriptor (full edge set, component types, all three relative periods, clocks, endpoint) as deterministic JSON lines. `pairs` drives the paired loops and is limited to the supported values; `joint_tables` must name exactly J1–J4; schema, grid and `t_b` are type- and range-checked.

| File | Role |
|---|---|
| `az_tokres_contact_tables.py` | descriptors and tables T1–T4, J1–J4; Stage 1 validator reused unchanged (identity, custody, states re-derivation, records, set); pairing keys checked (`th0` and the three non-slot tokens equal to `BASE`) |
| `contact_tables_manifest.json` | schema v2, **proposal**: cell `S1-C1` only (`(120, 8)`, profile P1); arms BASE, O1R, O1D, O2R, O2D, SHAM (Q2R exists only at `N = 122`); pairs `O1R/O1D`, `O2R/O2D`; endpoint `M ≥ 100` at tick 800 (valid cap stop before 800 positive); grid `1, 2, 5, 10, 20, 50, 100, 200, 400, 800`; `t_b = 100`; input `upload/az-token-resonance-stage1/HASHES.txt` with its SHA-256, commit `95db7af` and the S1-C1 inventory |
| `contact_tables_selftest_output.txt` | synthetic checks, `SELFTEST PASS` |
| `contact_tables_test_output.txt`, `contact_tables_test_descriptors.jsonl` | tables and per-record descriptors on Stage 1 **test-configuration** records (tag `SMOKE`, cell `TEST-C1`; no evidential value) |
| `contact_tables_negcontrols.py`, `..._output.txt` | one positive control and twelve refusal controls, `NEGCONTROLS PASS` (r1 had one positive and seven refusal controls, not \"eight\" — corrected) |

**Self-test** (synthetic, own seed): first-contact time, edge set and component types = the pinned engine's pre-interaction snapshot on 1,860 states; the design fixtures; periods; covariance; invalid input; `fb` clock; the gates of R1, R2 and the manifest fields of R4, each refused before any lookup; the clock layer on the reviewer's counterexamples (`fe = −1, 801, "invalid"`, `fb = 801`, negative `t100`, `steps = 800, M = 100, M_at[800] = 4`) and nine more; the cap rule.

**Negative controls**: NC00 positive; NC01–NC04 binding (dropped record with re-stamped side manifest; unlisted copy; missing side manifest; swapped keys re-stamped); NC05–NC08 deeper layers with every hash re-stamped (state re-derivation; `fe = 801`; `fe < tau_contact`; the `M_at[800] = 4` case); NC09–NC12 pointed at the registered Stage 1 records and refused before any is looked up (test plan naming `S1-C1`; unfrozen; wrong input hash; wrong pin).

**Reproduce the test output:** `python3 -I evidence/az/scripts/az_tokres_campaign.py --plan test --out DIR --jobs 2`, then `python3 -I evidence/az/mechanism/az_tokres_contact_tables.py --manifest evidence/az/mechanism/contact_tables_manifest.json --dir DIR --plan test` (the records differ only in `secs`; the tables do not use it).

**Choices for review and the PI** (each listed in the manifest; none taken by looking at a table): the cell (`S1-C1` alone, or also `S1-C2`; Stage 2 cells would need a Stage 2 validator path, not written); `t_b` of J4; the time grid; whether `SHAM` and `Q2R` stay as descriptor-only arms.
