# DYAD OPEN 20 (analytic branch) — stage 3c-b: preparation record

**Date:** 14–15 November 2026; r2 and r3 on 16 November 2026 after the co-owner's reviews `5915522711` and `5917787569` (both REVISE; §10, §11). **By:** Claude, Dyadic DSN owner. **Status:** working record (SESSION). **It is not a run of stage 3c-b and certifies nothing.**
**Authority:** PI decision of 14 November 2026, given in session on the owner's question: preparation of stage 3c-b is authorized — the t_M correction, freezing the code, a run package fixed by SHA-256, and one command block for the PI's Ubuntu server. **The production run and the independent replay are not part of that authorization; each needs a separate decision of the PI.**
**Governing edition:** `dyad-v6.4.24` (`10fbdacc…bc16`), unchanged. B-an and B-6 are ACTIVE. No statement about the jump or about divergence is drawn from anything here.
**Basis:** hand-over record of stage 3c-a (§4 commands, §6 scope, §8 prerequisite); proof record §§2–13.

## 1. What was done

| # | Item | Where |
|---|---|---|
| 1 | The t_M prerequisite: the tail threshold of the arc uses the upper bound of \|A₃\| | library, `arc_tail`, one line |
| 2 | A status line that tells a stage-3c-b run from a development run | library (`run_status`, `run_tail`), two lines in each of nine scripts |
| 3 | One driver for the whole run, with one acceptance rule and one ledger | `evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py` |
| 4 | The manifest of the frozen code and input, and the gate schema | `evidence/dyad/open20-an/stage3c-b/MANIFEST_SHA256.txt`, `GATE_SCHEMA.json` |
| 5 | A complete test of the package in development mode (selftest, r1 driver) | `evidence/dyad/open20-an/stage3c-b/selftest/` |
| 6 | Tests of the driver itself (r2) | `evidence/dyad/scripts/dyad_open20_an_stage3c_b_driver_tests.py`, output `driver_tests.json` |

Nothing else in the mathematical code was changed.

## 2. The code changes

- **t_M** (co-owner's read-back of W8 r2, review `5877317450`, item 2; hand-over record §8). The tail of the arc holds for \|x₀\| ≤ X_M, that is for \|w\| ≥ \|A₃\|/X_M³. The sufficient threshold takes the upper bound of \|A₃\|; the code took the lower bound and relied on the slack of the float bound. Now `wmin = up(A3) / XM ** 3`. A₃ is a 15-digit decimal, so the two bounds differ by the rounding of one ball; the output of the arc script is byte-identical.
- **Status line.** The scripts were written for development runs and print "development run; not a certificate". When the driver starts them for a production run or a replay it sets the environment variable `DYAD_OPEN20_3CB=1`; the status then reads "stage 3c-b run; one output of the run; the verdict is the ledger of the run with its replay, not this file". The text does not contain the run's name, so a production run and its replay give byte-identical files. Without the variable every output is as before.
- **The driver** is new and contains no mathematics.

## 3. The package

**Identifier:** `DYAD-OPEN20-AN-3CB-1`. **Manifest (r3):** `evidence/dyad/open20-an/stage3c-b/MANIFEST_SHA256.txt`, 18 files, SHA-256 `2553ea87400a09e225597c1b287b7cabadb3ec2838575ae0576e9dcb022d280f`. (r1: 17 files, `60143475…9455`; r2: `e57a1614…1163`.)
The manifest lists the driver, the ten scripts of the job table, every `dyad_*` module they import (the library, the stage-2 and stage-2b modules, the stage-3b tube sampling), the stage-2 input `scout_N216_dps840.json`, and the gate schema `GATE_SCHEMA.json`. The driver refuses to run if a listed file differs, or if the list is not exactly this set.

**Frozen environment:** python-flint 0.9.0 (FLINT 3.6.0 in the wheel used here), mpmath 1.3.0, sympy 1.14.0. The driver stops on any other version of these three. The development runs used Python 3.13.16; the Python version is recorded, not fixed.

**Jobs: 11 positive processes and 23 negative controls**, each run once, with the flags of the committed runs of stage 3c-a.

| Group | Positive process (expected exit 0, every gate true) | Controls (expected exit 1) |
|---|---|---|
| Structure (exact algebra) | `structure` | SCALE, SHIFT |
| Seed inequalities (proof record §12) | `seed` | BIG, HALFE |
| Common arc | `arc` | BIGSTEP, CORE, BRANCH, LOGBRANCH |
| Engine | `engine_w1`, `engine_w2a`, `engine_w2b` | SHIFTCOEF; TAMPER; SHRINKREM, SHIFTINV |
| Zone II, both sides | `zone2_F`, `zone2_G` | CORE, SIGMA, QZERO |
| Zone I and seam | `zone1` | BIGZONE, SIGMA, CORE, ALPHA, BRANCH |
| The one inverse branch | `branch` (`--strict-e`) | SMALLSECTOR |
| Legs and two-disc test | `legs` (`--full-fibre --strict-snd`) | SHORT, ZEROJUMP |

Parameters: hand-over record §3; none was changed.

## 4. The acceptance rule (r2)

**Gate schema.** `GATE_SCHEMA.json` fixes, for each of the 34 jobs, the exact set of gate names and the exact set of gates that are false: none for a positive process; for a control, its expected failure (for example `SEP_two_disc_test` for `legs_ZEROJUMP`, `Q12_inequality_at_r0` for `seed_BIG`). It was written from the committed reference outputs by the mode `schema` and is part of the manifest.

A run is **ACCEPTED** iff every job of the table occurs exactly once among the records, and its record shows:
- exit code 0 for a positive process, 1 for a control;
- exactly the gate names of the schema, each a boolean;
- `all_pass` a boolean equal to the conjunction of the gates;
- exactly the false gates of the schema;
- no error and not skipped;
- in selftest also: JSON and printed output byte-identical to the committed reference.

**Records.** Every job ends with exactly one record. An output that is missing, not JSON, not a JSON object or without a gates object gives an error record. A job whose dependency did not end as expected is not run and gets a skipped record. Dependencies point to earlier jobs, so the queue always empties.

**Rule test.** Before any job starts the driver applies the rule to 16 synthetic ledgers built from the schema (one accepted, fifteen rejected) and stops if an answer is wrong. The rejected cases: exit 1 with the right output; a missing process; a process recorded twice; a control that passes; a positive process with exit 0 and a false gate; an output that differs from its reference; the legs without the two-disc gate; `seed_BIG` failing at the wrong gate; a control with every gate true and `all_pass` false; a gate value that is not a boolean; an extra gate; exit code 7; an error record; a skipped job; a record of an unknown job.

The driver writes `LEDGER.json` (mode, the PI's authorization as quoted on the command line, times, manifest, environment, git state, the result of the rule test, and for every job its command, exit code, time, hashes and gates) and `SHA256SUMS.txt` over every file of the run.

**Git.** Production and replay need both git queries to succeed and a clean tree on the package paths. A failing query stops the run; it is never read as a clean tree.

**Modes.** `selftest` (development mode, compared with the committed outputs); `production` and `replay` (need `--pi-authorization`, a readable and clean git checkout and the manifest).

`validate DIR` checks one run directory on its own, from its files. It first checks the frozen package against its manifest, so the gate schema it uses is the frozen one, and the ledger must carry that manifest (r3). The stored verdict is not trusted:
- `SHA256SUMS.txt` must list exactly the files with their hashes;
- each record must name the files of its job and carry their actual hashes;
- its gates must be those of the actual output;
- the ledger must agree with its mode (r3): its scope text is the text of the mode; it shows a passed rule test and the frozen package versions; in `production` and `replay` it records a PI authorization and a clean, readable git state, and every output that has a status field says "stage 3c-b run"; a selftest records no authorization and no output with that status (the structure script writes no status and is the stated exception). This cannot show that a PI decision is real; it rejects a set of files that contradicts itself;
- the rule is then applied again, and the stored verdict must equal the result.

`compare A B` checks the package against its manifest, validates both directories, requires the manifest of this checkout in both and production against replay (or two selftests), and then compares every output byte for byte.

## 5. The selftest

**Run:** by the owner, on the machine of the development runs (two cores), at commit `5ead9de` with a clean working tree on the package paths; 14 November 2026, 21:03–21:54 UTC; 51 minutes. OWNER-RUN, development mode. **It is not a certification run** and its ledger says so.

| Item | Result |
|---|---|
| Verdict by the rule | **ACCEPTED** |
| Positive processes | 11 of 11 with exit code 0 and every gate true |
| Negative controls | 23 of 23 with exit code 1 |
| Outputs compared with the committed outputs of stage 3c-a and of the seed check | 68 files (JSON and printed output of each job): **all byte-identical** |
| Rule test | 7 of 7 cases as expected |
| Messages on the error stream | none |
| Environment recorded | Python 3.13.16, python-flint 0.9.0 (FLINT 3.6.0), mpmath 1.3.0 (backend `python`), sympy 1.14.0 |

- **What it shows.** The frozen package — with the t_M correction, the status line and the driver — reproduces every reviewed development output of W1–W8 and of the seed check. In particular the t_M correction changes no printed value.
- **What is stored.** `evidence/dyad/open20-an/stage3c-b/selftest/LEDGER.json` (SHA-256 `f3e43e95…80d7`) and the run's `SHA256SUMS.txt`. The 68 output files are not stored a second time: the ledger names for each job its committed reference file and the hash of what the run produced, and the owner checked that the two agree for all 34 jobs.
- **An earlier complete selftest** (same code, before the FLINT version was added to the ledger; 48 minutes) was also accepted with 68 identical files. It is not stored.

**Other tests of the driver** (none starts a job):
- it stops for `production` without `--pi-authorization`; for an output directory that is not empty; for a file that differs from the manifest; for an untracked file on a package path when the git state is checked strictly;
- `compare` reports AGREE for a run directory against an unchanged copy, DISAGREE when one byte of one output is changed, and DISAGREE for the two selftests above because their manifests differ;
- the environment block of §6 step 2 was executed in a fresh virtual environment here: the driver's environment and manifest checks pass in it.

**r2.** The selftest above ran with the r1 driver (manifest `60143475…9455`); it is kept as a record of that run, and its ledger is in the r1 format, so `validate` of r2 does not accept it. r2 changes only the driver and adds the gate schema; no script of the job table and no module they import changed (the 16 other files of the manifest have the same hashes as in r1). So the 68 outputs of that selftest are the outputs the r2 driver would see. The co-owner's review asked for no new campaign, and none was run. Instead:
- the six quick real jobs (structure and seed, with their controls) were run through the r2 runner in both modes, and both were accepted;
- the driver tests of §10 build a run directory from the 68 committed reference outputs and check that it is valid under the r2 rule and schema.

**Not executed:** the modes `production` and `replay` as a whole. Their parts are the ones tested above; the only difference to the selftest inside the scripts is the status line, which was checked on the arc script.

### 5.1 Selftest of the r3 package on the PI's server (16 November 2026)

**Run by the PI** on the Ubuntu server, at `main` `c9e313f` (the merge of PR #273), manifest `2553ea87…280f`, clean git state. Python 3.12.3, python-flint 0.9.0 (FLINT 3.6.0), mpmath 1.3.0, sympy 1.14.0; one CPU; two workers. 10:08–12:43 UTC (2 h 34 min). Development mode; **not a certification run.** The whole run directory came unchanged on `upload/dyad-3cb-selftest-r3-server` (commit `bc5ed24`), at `evidence/dyad/open20-an/stage3c-b/selftest-server-r3/`.

| Check | Result |
|---|---|
| Verdict of the run | **ACCEPTED**, exit code 0 |
| `validate` on the server (PI) and here (owner, from the uploaded files) | **VALID** both |
| `SHA256SUMS.txt` | 70 files: 68 outputs, `LEDGER.json`, the checksum file; all match |
| Byte-identity with the committed outputs of stage 3c-a and of the seed check | **68 of 68 files** |
| Rule test | 16 of 16; no message on the error stream |

**What it settles:**
- **§8 item 2 (byte-identity across machines):** shown for this server. A different machine, a different Python minor version (3.12.3 against 3.13.16) and a single CPU produced the same 68 files byte for byte. It is also the first complete selftest of the r3 driver.
- **§8 item 3 (Python version):** 3.12 and 3.13 gave the same outputs; the version stays recorded, not fixed.

**What it does not settle:** it runs the same frozen code as the owner's runs, so it is a reproducibility check by a second operator on a second machine, not an independent implementation (§8 item 1). It is not REVIEWER-REPLAYED, and it is not a run of stage 3c-b.

**Time:** with one CPU the two workers share it; the longest jobs were the inverse branch and its control (about 54 min each), zone II for G (44 min) and the legs (26 min). A production run on this server needs about 2.5 hours.

## 6. How a production run would go (not authorized)

1. **PI decision** to run stage 3c-b, and who replays it.
2. **Environment on the server,** once:
   ```bash
   python3 -m venv /root/venv-dyad-3cb \
   && /root/venv-dyad-3cb/bin/pip install --no-cache-dir python-flint==0.9.0 mpmath==1.3.0 sympy==1.14.0
   ```
3. **Selftest on the server** (development mode; recommended before the production run, see §8 item 2). The manifest pins the package: the block tests its hash before running, and keeps the driver's exit code as the block's status.
   ```bash
   cd /root/rtg-corpus && git fetch origin --tags && git checkout main && git pull --ff-only origin main \
   && test "$(sha256sum evidence/dyad/open20-an/stage3c-b/MANIFEST_SHA256.txt | cut -d' ' -f1)" = "<the manifest hash of the merged package>" \
   && /root/venv-dyad-3cb/bin/python -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py selftest \
        --out /root/dyad-3cb-selftest --jobs 2; rc=$?; echo "exit=$rc"; (exit $rc)
   ```
4. **Production run,** at the commit the PI names:
   ```bash
   cd /root/rtg-corpus \
   && /root/venv-dyad-3cb/bin/python -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py production \
        --out /root/dyad-3cb-production --jobs 2 --pi-authorization "<the PI's decision, date and words>"
   ```
5. **The whole output directory** (every JSON and printed output, `LEDGER.json`, `SHA256SUMS.txt`) **arrives unchanged** on an `upload/…` branch — `validate` needs the files, not only the ledger — and is hash-checked against its `SHA256SUMS.txt` (CONVENTIONS).
6. **Replay** by the second party with the mode `replay`, then `compare PRODUCTION_DIR REPLAY_DIR`.
7. **Release record** by the owner, stating the scope of §7; review; PI decision.

`--jobs` may be raised on a machine with more cores: the jobs are independent, each used about 45 MB of memory in the samples taken, and the outputs do not depend on the number of workers. With two workers the selftest took 51 minutes; the longest chain (zone II for G, then the inverse branch) is about 30 minutes and bounds the time from below.

## 7. What an accepted production run would and would not establish

As in the hand-over record §6 and the proof record §§11–13:
- *Would establish, after a replay that agrees:* under the remainder constants and the structural facts, the hypotheses (G), (A1), (A2), (B) of the tube lemma on D₀ for F and on D₁ for the inverse branch G; the arc in D₀ ∩ D₁; and two disjoint discs at ξ* for the values of the two graphs.
- *Together with proof record §12 and §13:* the divergence of the formal branch Γ̂₊ (and of Γ̂₋ and of log F), **conditionally on the literature inputs L1 and L3**, which are LIT-checked uses at SESSION scope.
- *Would not establish:* anything at theorem grade in the DSN while L1 and L3 have that scope; anything about B-an or B-6.

## 8. Limits of the package

1. **A replay is a reproducibility check, not an independent implementation.** Both runs execute the same frozen code. Agreement shows that the result does not depend on the machine or the operator. It does not test the code against a second implementation. What tests the code is inside the run: the independent sampling gates (SND) and the 23 negative controls.
2. **Byte-identity across machines — shown for the PI's server on 16 November 2026 (§5.1).** The outputs print rounded decimals of ball-arithmetic results; identity elsewhere was an expectation until that run. Another machine still needs its own selftest before it carries a production run or a replay.
3. **The Python version is recorded, not fixed.** If the server's Python differs from 3.13 and the selftest there is not byte-identical, the difference has to be understood before anything else.
4. **Messages on the error stream are recorded, not judged.** The ledger gives their size per job; the rule does not use it. In the selftest of §5 no job wrote any.
5. **The two controls of the legs run in the default form of the leg,** as in W6, not with `--full-fibre`. They test the two-disc test and the length of the leg.
6. **The quality thresholds of the engine checks** (tails below 10⁻⁶, radii of the vanishing coefficients below 10⁻¹⁵⁰) are part of the gates; no bound of the argument depends on them (proof record §10).
7. **`seed` checks the explicit inequalities of the seed.** It does not prove the seed, which rests on L1 (proof record §12).
8. **No REVIEWER-REPLAYED run exists,** of this package or of any earlier one.

## 9. Open decisions (the PI's)

- Whether and when stage 3c-b is run; who replays it and where.
- Independently of both: the LIT request on Proposition 5.3 is filed (`pipes/LIT/20261114-DYAD-lh2012-prop53-scope.md`, PR #269).

## 10. r2 — co-owner review `5915522711` (REVISE), 16 November 2026

The review found no fault in the mathematics or in the development outputs. It found three faults in how the driver accepts runs and handles errors. All three are corrected in the driver; the scripts of the job table are unchanged.

| Finding | Correction | Test (`dyad_open20_an_stage3c_b_driver_tests.py`) |
|---|---|---|
| **R1** The rule checked only the gates present, and for a control only exit 1 and `all_pass` false | Gate schema in the manifest: exact gate names and exact false gates per job; `all_pass` must equal the conjunction; booleans only (§4) | RULE: 16 synthetic ledgers, among them the three cases of the review; FIXTURE: the 68 committed outputs satisfy the schema |
| **R2** `compare` trusted the stored verdicts, lost duplicates, and checked hashes only against the first ledger | `validate` of each directory from its files, then the comparison (§4) | COMPARE: unchanged copy AGREE; seven changes DISAGREE: wrong JSON hash in the ledger, a job recorded twice, exit 7, a gate false in the ledger only, one changed byte with renewed SHA256SUMS, a deleted output, a false gate under a stored ACCEPTED |
| **R3** A defective output stopped the worker and left a dependent job waiting; a failing `git status` read as clean | Error and skipped records; every job ends with one record; dependencies point backwards; a failing git query stops a strict check (§4) | WORKER: outputs `[]` and non-JSON give error records, the dependent job is skipped and not run, the run ends; GIT: status exit 128 stops the strict check and is not clean |

- **Result:** all five tests PASS (`evidence/dyad/open20-an/stage3c-b/driver_tests.json`; checksums in `DRIVER_TESTS_SHA256SUMS.txt`). They take under a second and use only the standard library. OWNER-RUN.
- **Server command** (the review's last point): pinned by the manifest hash, and it keeps the driver's exit code (§6 step 3).
- **Not done:** no campaign run, no selftest with the r2 driver, no production run, no replay.

## 11. r3 — co-owner review `5917787569` (REVISE), 16 November 2026

R1 and R3 of the previous review were accepted, and the counter-examples of R2 were found closed. Two gaps were found in the new `validate`/`compare` path.

| Finding | Correction | Test |
|---|---|---|
| **R2-A** `validate` and `compare` did not check the package against the manifest, so a changed schema with an unchanged manifest could make a false two-disc gate acceptable | both call `check_manifest()` before using the schema; the ledger must carry the frozen manifest | PACKAGE: two directories with a false `SEP_two_disc_test` DISAGREE; they still DISAGREE with the schema changed to expect that failure and the manifest unchanged (the package check stops); the schema is restored and the package matches its manifest again |
| **R2-B** two selftests relabelled `production` and `replay` compared AGREE | the mode check of §4, on the statuses read from the output files | MODE: a consistent production/replay pair AGREE; the relabelled selftests DISAGREE; five inconsistent production ledgers (no authorization, unclean git, selftest scope, other package versions, one output in development status) INVALID; a selftest with an authorization INVALID; the library's status text equals the driver's |

- **Result:** seven driver tests, all PASS (`driver_tests.json`, `DRIVER_TESTS_SHA256SUMS.txt`). OWNER-RUN.
- **Manifest r3:** `2553ea87…280f`; only the driver changed since r2. No script of the job table changed; no campaign was run.
- **Kept output:** the stored selftest ledger of r1 is a ledger only. A selftest or a run that is to be checked by `validate` must be kept as a whole directory (§6 step 5).
