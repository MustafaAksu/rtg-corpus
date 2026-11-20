# AZ token-resonance fork design — BASE-only pilot protocol (for review; not authorised)

r2 (20 Nov 2026) closes R1, R2 and F1 of review `5993141443`; see §3 and §5.

**[SESSION] NONCANONICAL operational protocol.** It belongs to the §6.3 fork design (`records/az/AZ_TOKEN_RESONANCE_FORK_DESIGN.md` r2; Gate D PASS `5960841961`) and follows Gate I.1 (PR #328) and Gate I.2 (PR #331), both merged.

- **Drafting.** Written by the Claude AZ lane, with independent review by ChatGPT. This task split was proposed by Claude and supported by ChatGPT in the exchange of 20 Nov 2026; the PI relayed it, but it is not yet recorded in the PI's own words.
- **Scope.** This record fixes what the pilot measures and how L is chosen. **It does not authorise the run.** The pilot needs a review PASS, the PI's decisions listed in §6, a frozen manifest and a separate compute authorisation.
- **No outcome data.** No R or D arm is built. No registered record (Stage 1 or Stage 2) is read.

## 1. Purpose

The only purpose is to fix the observation bound L of the fork design, using the BASE contact distribution of **new** seeds, and to report the eligibility structure of the C⁻ and C⁺ boundaries. The pilot is not a test of any effect, it is not mechanism evidence, and its seeds are not reused in any later confirmatory campaign.

## 2. Population and seed law

| Item | Value |
|---|---|
| Cell | N = 120, k = 8; P1 (`tdrg_orient_v2_12_14`), `bound_symmetric`; pinned engine `4c94d874…a608` |
| Seeds | b = 0 … n − 1, with n = 500 fixed in advance |
| Tag | `AZ-FORK-BASEPILOT-P1`. New; the driver refuses registered `AZ-TOKRES-*` tags and every synthetic test tag. |
| Initial state | `az_tokres_run.base_draw(engine, tag, N, k, b)`: the engine's native four-node draw |
| Slot | `j = az_tokres_run.arm_choices(tag, N, k, b)["slot"]`, uniform on the four initial nodes, from a stream independent of the native draw |
| Node cap / threshold | C = 300, q = 100 (C ≥ q) |
| Candidate grid | 𝓛 = {100, 200, 400, 800}; L_max = 800 |

No seed is replaced, dropped or added. The denominator is always all n seeds.

## 3. Measurement (driver `evidence/az/mechanism/az_fork_base_pilot.py`)

- **One BASE prefix per seed.** It uses the merged contact clock (`az_tokres_contact_clock.py`, `4cdd9a7d`) with `T_ref = L_max + 1 = 801` and cap C. Every candidate L is evaluated from this single run, for two reasons:
  - τ_C does not depend on `T_ref` or L;
  - C⁺ eligibility at τ_C ≤ L is the same for `T_ref = L + 1` and `L_max + 1`.
  
  Self-test C3 tests this.
- **Verification.** τ_C is taken **only** from the clock output. It is accepted only if an **independent replay** of the same seed reproduces it. The replay has its own loop, not the clock. It must reproduce the status, the first slot-contact tick, the C⁻/C⁺ annotations (`landmark_tick = τ_C − 1` and `τ_C`) and both boundary states as full fingerprints. Otherwise the run stops with `REFUSED`. The two fingerprints are stored as checkpoint ids (SHA-256). A forged τ_C, swapped boundaries, a boundary from another seed, a wrong annotation and a wrong status are all refused (self-test C2).
- **Per seed** (`seeds.jsonl`):
  - the draw (θ₀, δ₀, j), the status and τ_C, and the counterfactual `τ_free` (information only, never a clock);
  - for contacts:
    - the number of incident edges, and the pre-tick and C⁺ carriers;
    - eligibility at C⁻ and C⁺, and M at each boundary;
    - already-positive flags (M ≥ q) at C⁻ and C⁺;
    - whether the slot copy is a birth centre at the contact tick (the "centre case" of the C⁺ target rule);
    - both checkpoint ids.
- **Summary** (`summary.json`, `summary.txt`; deterministic): the status counts; for each L, the count k(L), F(L), its Wilson interval, C⁻, C⁺ and joint eligibility, centre cases and already-positive counts; the rule result; τ_C quantiles; and how often `τ_free ≠ τ_C`. Run times go to a separate `timing.txt`, which is not deterministic.
- **Approved-manifest identity (r2, R2).** The run is bound to the manifest the PI approves, named by its SHA-256 `H`.
  - `--run --manifest M --manifest-sha256 H --out DIR` refuses unless all of the following hold: M is a file of this repository; M is byte-identical to its committed version at HEAD; `sha256(M) = H`; M passes the protocol checks (frozen script SHA-256, decided `wilson_in_rule`, a new tag).
  - Freezing the script hash alone would not freeze n, the tag or the grid. Binding the manifest bytes does.
  - The output stores M byte for byte as `manifest.json`. `summary.json` and `summary.txt` carry both `manifest_sha256` and `script_sha256`.
- **Outputs.** A new directory, created atomically. Its location is checked on the **resolved** parent path (r2, F1), so a symbolic link cannot redirect it into `upload/`, `records/`, `dsn/` or `evidence/az/scripts/`. The directory holds exactly `manifest.json`, `seeds.jsonl`, `summary.json`, `summary.txt`, `timing.txt` and `SHA256SUMS`. All are written with `O_EXCL`, and `SHA256SUMS` lists exactly the five data files.
- **Complete audit (r2, R1).** `--audit DIR --manifest M --manifest-sha256 H` checks, in order:
  - the approved identity: H, and the stored `manifest.json` equal to M;
  - the exact file set and every `SHA256SUMS` entry;
  - **exactly** the n seeds 0 … n − 1, in order;
  - every record **field**, recomputed by the clock path and compared in full;
  - every seed independently replayed (draw, status, τ_C, checkpoint ids);
  - both summaries recomputed from the records, byte for byte;
  - the seed list in `timing.txt`.
  
  An empty or incomplete `seeds.jsonl` therefore fails. So does any forgery made consistent by rewriting `SHA256SUMS` (self-tests D4–D6).

## 4. L rule (fixed before the run)

F(L) = #{b : status contact and τ_C,b ≤ L} / n, with **all n pilot seeds** in the denominator. Seeds with no contact by L_max, or terminated before contact, count in the denominator and never in the numerator.

L\* = min{L ∈ 𝓛 : F(L) ≥ 0.95}. If no candidate qualifies, the result is **"no qualifying L"**: there is no automatic L = 800, and the decision returns to the PI.

The manifest field `wilson_in_rule` must be set to `true` or `false` before the run; the driver refuses `null`. With `true`, the comparison uses the lower 95% Wilson bound instead of F(L). The Wilson interval is reported in both cases.

C⁻/C⁺ eligibility, centre cases and already-positive counts are reported. **They never change the rule after the fact.**

## 5. Validation of the driver (synthetic test tag only)

- `base_pilot_selftest_output.txt`: `SELFTEST PASS`, 24 checks (r1: 20).
  - A1–A5: the L rule on hand-made records, including τ_C = L counted, the denominator including no-contact and terminated seeds, "no qualifying L", the Wilson bound against its closed form, and refusal of a record set that is not exactly seeds 0 … n − 1.
  - B1–B6: manifest and output gates. The test plan accepts only the test tag, so the pilot seeds are never touched by tests. The pilot plan refuses a manifest that is not frozen for the script, `wilson_in_rule = null`, registered and synthetic tags, an unsorted grid, cap < q, unknown keys, and output directories that exist or lie inside `upload/` or `records/`.
  - C1–C3: verification and the L-invariance of the single run.
  - D1–D3: two end-to-end test-plan runs with 16 seeds are byte-identical, including `manifest.json`. Every contact carries verified ids, the summary binds the manifest and script SHA-256, and only pinned files are opened.
  - D4: the complete audit of a genuine output reports no problem.
  - D5: the audit fails on every **consistent** forgery, that is, with `SHA256SUMS` rewritten to match. The forgeries tested: an empty `seeds.jsonl`, a missing seed, reordered seeds, a changed `eligible_plus`, `centre_case`, `M_minus` or `tau_free`, a changed `summary.json` or `summary.txt`, a changed stored manifest, and an extra file. It also fails on a `SHA256SUMS` mismatch.
  - D6: the audit fails against a different approved SHA-256 and against changed manifest parameters.
  - D7: a run is refused when the manifest bytes do not match the approved SHA-256.
  - D8: a manifest outside the repository is refused, while a committed, unmodified file is accepted.
  - D9: an output path through a symbolic link into `upload/` is refused, and nothing is created there.
- `base_pilot_negcontrols.py` and its output: eighteen injected faults (r1: eleven), all detected. They are:
  - verification disabled;
  - denominator over contacts only;
  - automatic L_max;
  - τ_C < L used instead of ≤;
  - one-sided z in the Wilson interval;
  - run time in the deterministic summary;
  - freeze gate off;
  - tag guard off;
  - an existing output directory accepted;
  - `τ_free` substituted for τ_C;
  - audit disabled;
  - (r2) the audit without its field comparison, without summary recomputation, without the file-set and `SHA256SUMS` check, and without the manifest identity;
  - (r2) a run without the manifest identity check;
  - (r2) no git binding;
  - (r2) an output check that ignores links.

**Synthetic orientation, not pilot data.** On the 16 test-tag seeds of the end-to-end self-test, every seed made contact by tick 8, so L\* = 100. In the 400 synthetic trajectories of Gate I.1, 196 of 381 contacts were at τ_C = 1. The pilot is therefore likely to give L\* = 100, the smallest candidate. Its main value would then lie in the eligibility, centre-case and already-positive rates, and in the run-time estimate for the later campaign. This expectation comes from synthetic test seeds only. It is stated here **before** the pilot so that it cannot be read into the result afterwards.

## 6. Decisions needed before the run (PI)

| # | Decision | Proposal |
|---|---|---|
| 1 | Task split: Claude writes the protocol and driver, ChatGPT reviews | as relayed on 20 Nov; to be confirmed in the PI's words |
| 2 | n, tag, grid 𝓛, threshold | n = 500, `AZ-FORK-BASEPILOT-P1`, {100, 200, 400, 800}, 0.95 |
| 3 | `wilson_in_rule` | **false**: F(L) in the rule, Wilson reported. With n = 500, the lower bound for F = 0.95 is about 0.927, so `true` amounts to a stricter threshold; the PI may prefer that. |
| 4 | Freeze | after review PASS: set `frozen_script_sha256` and `wilson_in_rule` in `base_pilot_manifest.json` in one freeze commit; readback. The PI then approves the manifest by its SHA-256 `H` (the committed file's bytes) in the authorisation record. |
| 5 | Compute authorisation | run once on the PI's server, in a separate worktree at the freeze commit: `python3 -I evidence/az/mechanism/az_fork_base_pilot.py --run --manifest evidence/az/mechanism/base_pilot_manifest.json --manifest-sha256 H --out <new dir>`; then `--audit <dir> --manifest … --manifest-sha256 H`; then the outputs are uploaded unchanged on an `upload/...` branch and hash-checked |

## 7. What follows the pilot (each a separate PI decision)

A pilot report with L\* and the eligibility structure comes first. After it:

- the seed law and sample size of the R/D campaign;
- the power calculation;
- the analysis code;
- the preregistration;
- the compute authorisation.

The O1 contrasts at C⁻ and C⁺ are paired R−D differences. Their analysis family (two contrasts, Holm) and the descriptive Γ (difference of differences on jointly eligible seeds) are fixed only in the preregistration.
