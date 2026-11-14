# DYAD OPEN 20 (analytic branch) — stage 3c-b: preparation record

**Date:** 14–15 November 2026 (finished 15 November, 00:55 +03:00). **By:** Claude, Dyadic DSN owner. **Status:** working record (SESSION). **It is not a run of stage 3c-b and certifies nothing.**
**Authority:** PI decision of 14 November 2026, given in session on the owner's question: preparation of stage 3c-b is authorized — the t_M correction, freezing the code, a run package fixed by SHA-256, and one command block for the PI's Ubuntu server. **The production run and the independent replay are not part of that authorization; each needs a separate decision of the PI.**
**Governing edition:** `dyad-v6.4.24` (`10fbdacc…bc16`), unchanged. B-an and B-6 are ACTIVE. No statement about the jump or about divergence is drawn from anything here.
**Basis:** hand-over record of stage 3c-a (§4 commands, §6 scope, §8 prerequisite); proof record §§2–13.

## 1. What was done

| # | Item | Where |
|---|---|---|
| 1 | The t_M prerequisite: the tail threshold of the arc uses the upper bound of \|A₃\| | library, `arc_tail`, one line |
| 2 | A status line that tells a stage-3c-b run from a development run | library (`run_status`, `run_tail`), two lines in each of nine scripts |
| 3 | One driver for the whole run, with one acceptance rule and one ledger | `evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py` |
| 4 | The manifest of the frozen code and input | `evidence/dyad/open20-an/stage3c-b/MANIFEST_SHA256.txt` |
| 5 | A complete test of the package in development mode (selftest) | `evidence/dyad/open20-an/stage3c-b/selftest/` |

Nothing else in the mathematical code was changed.

## 2. The code changes

- **t_M** (co-owner's read-back of W8 r2, review `5877317450`, item 2; hand-over record §8). The tail of the arc holds for \|x₀\| ≤ X_M, that is for \|w\| ≥ \|A₃\|/X_M³. The sufficient threshold takes the upper bound of \|A₃\|; the code took the lower bound and relied on the slack of the float bound. Now `wmin = up(A3) / XM ** 3`. A₃ is a 15-digit decimal, so the two bounds differ by the rounding of one ball; the output of the arc script is byte-identical.
- **Status line.** The scripts were written for development runs and print "development run; not a certificate". When the driver starts them for a production run or a replay it sets the environment variable `DYAD_OPEN20_3CB=1`; the status then reads "stage 3c-b run; one output of the run; the verdict is the ledger of the run with its replay, not this file". The text does not contain the run's name, so a production run and its replay give byte-identical files. Without the variable every output is as before.
- **The driver** is new and contains no mathematics.

## 3. The package

**Identifier:** `DYAD-OPEN20-AN-3CB-1`. **Manifest:** `evidence/dyad/open20-an/stage3c-b/MANIFEST_SHA256.txt`, 17 files, SHA-256 `6014347580008e7ebcbcc422bf8a87e5a5e54ceb9db509fe4bb62db4808a9455`.
The manifest lists the driver, the ten scripts of the job table, every `dyad_*` module they import (the library, the stage-2 and stage-2b modules, the stage-3b tube sampling), and the stage-2 input `scout_N216_dps840.json`. The driver refuses to run if a listed file differs, or if the list is not exactly this set.

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

## 4. The acceptance rule

A run is **ACCEPTED** iff every job of the table occurs exactly once in the ledger with its expected outcome:
- positive process: exit code 0, and its output has `all_pass` true and every gate true;
- control: exit code 1, and its output has `all_pass` false;
- selftest only: in addition the JSON and the printed output are byte-identical to the committed reference.

Before any job starts the driver applies the rule to seven synthetic ledgers and stops if an answer is wrong: one complete ledger (accepted) and six defective ones (rejected) — a positive process with the right output and exit code 1; a missing process; a process recorded twice; a control that passes; a positive process with exit code 0 and a false gate; an output that differs from its reference.

The driver writes `LEDGER.json` (mode, the PI's authorization as quoted on the command line, times, manifest, environment, git commit, the result of the rule test, and for every job its command, exit code, time, hashes and gates) and `SHA256SUMS.txt` over every file of the run.

**Modes.** `selftest` (development mode, compared with the committed outputs); `production` and `replay` (need `--pi-authorization`, a clean git checkout and the manifest); `compare` (two run directories: same manifest, both accepted, every output byte-identical).

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

**Not executed:** the modes `production` and `replay` as a whole. Their parts are the ones tested above; the only difference to the selftest inside the scripts is the status line, which was checked on the arc script.

## 6. How a production run would go (not authorized)

1. **PI decision** to run stage 3c-b, and who replays it.
2. **Environment on the server,** once:
   ```bash
   python3 -m venv /root/venv-dyad-3cb \
   && /root/venv-dyad-3cb/bin/pip install --no-cache-dir python-flint==0.9.0 mpmath==1.3.0 sympy==1.14.0
   ```
3. **Selftest on the server** (development mode; recommended before the production run, see §8 item 2):
   ```bash
   cd /root/rtg-corpus && git fetch origin --tags && git checkout main && git pull --ff-only origin main \
   && /root/venv-dyad-3cb/bin/python -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py selftest \
        --out /root/dyad-3cb-selftest --jobs 2
   ```
4. **Production run,** at the commit the PI names:
   ```bash
   cd /root/rtg-corpus \
   && /root/venv-dyad-3cb/bin/python -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py production \
        --out /root/dyad-3cb-production --jobs 2 --pi-authorization "<the PI's decision, date and words>"
   ```
5. **The output directory arrives unchanged** on an `upload/…` branch and is hash-checked against its `SHA256SUMS.txt` (CONVENTIONS).
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
2. **Byte-identity across machines is not yet shown.** The selftest of §5 ran on the machine of the development runs. The outputs print rounded decimals of ball-arithmetic results; with the same wheel of python-flint they should be identical elsewhere, but that is an expectation. The selftest on the server (§6 step 3) settles it before a production run.
3. **The Python version is recorded, not fixed.** If the server's Python differs from 3.13 and the selftest there is not byte-identical, the difference has to be understood before anything else.
4. **Messages on the error stream are recorded, not judged.** The ledger gives their size per job; the rule does not use it. In the selftest of §5 no job wrote any.
5. **The two controls of the legs run in the default form of the leg,** as in W6, not with `--full-fibre`. They test the two-disc test and the length of the leg.
6. **The quality thresholds of the engine checks** (tails below 10⁻⁶, radii of the vanishing coefficients below 10⁻¹⁵⁰) are part of the gates; no bound of the argument depends on them (proof record §10).
7. **`seed` checks the explicit inequalities of the seed.** It does not prove the seed, which rests on L1 (proof record §12).
8. **No REVIEWER-REPLAYED run exists,** of this package or of any earlier one.

## 9. Open decisions (the PI's)

- Whether the selftest is run on the server now (it is a development-mode run and produces no certification output).
- Whether and when stage 3c-b is run; who replays it and where.
- Independently of both: the LIT request on Proposition 5.3 is filed (`pipes/LIT/20261114-DYAD-lh2012-prop53-scope.md`, PR #269).
