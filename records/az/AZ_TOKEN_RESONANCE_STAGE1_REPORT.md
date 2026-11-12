# AZ Action 1 — Token Resonance and Basin Selection: Stage 1 report

**[SESSION] NONCANONICAL. Nothing here is adopted.** Prepared by the AZ co-owner (Claude) on 12 November 2026 from the campaign directory the PI uploaded; reviewed by the second co-owner (review `5869662603`, accepted, scoped) and merged as a session record the same day (PR #228). §§1–10 are the reviewed text except for the title of §9; what happened after the review is in §11. It edits no DSN and claims no TDR-G result. Registration: `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` (draft r2, PR #211 head `47dee46`; reviews `5855522171`, `5857601141`). Governing sources: AZ `az-v0.7`, TDR-G `tdrg-v2.12.14`.

## 1. Result in one paragraph

The registered campaign is complete (19,900 runs), passes every integrity check and both gates, and its registered analysis reproduces byte for byte from the uploaded files. **Both confirmatory contrasts are supported, unqualified.** At `N = 120`, `k = 8`, `bound_symmetric`, adopted orientation rule, replacing one initial token by a value with `2x ≡ 0` rather than by its `±1` neighbour raises the risk of `max_{t≤800} M_t ≥ 100` from 1.5 % to 25.8 % (risk difference +0.243, 97.5 % interval +0.217 to +0.268); a value with `2x ≡ N/2` raises it from 2.4 % to 18.5 % (+0.161, +0.138 to +0.184). The supportive family at `N = 122` agrees: the order-1 effect is replicated (+0.219, +0.194 to +0.244), and the four values nearest `N/4`, `3N/4`, none of which has order 2 there, are equivalent to the native ensemble within the registered margin. This is the causal effect of a token replacement at this engine, profile, cell, horizon and threshold. It is not a mechanism, not a statement about the TDR-26 defective basin, and not a bridge observable.

## 2. Run record

| Item | Fact | Source |
|---|---|---|
| Registered bytes | PR #211 head `47dee46` (pushed 11 Nov 2026, 11:16:48Z); SHA-256 of `evidence/az/token_resonance/SHA256SUMS` = `81c87dcfc8d326e3c29861b9124c9654535f1c64cc6e5f9c7a9c9cafa6abd6eb`; the scripts are unchanged since `f7fdfac`, the head the readback `5857601141` (10:52:37Z) accepted | GitHub push and review timestamps; `verify_output.txt` |
| Authorisation | The PI ran the registered block himself on his Ubuntu server on 11 Nov 2026. There is no separate written authorisation naming the bytes; the block checks out the registered branch and verifies `SHA256SUMS` before anything runs, and its output shows `47dee46` and "package bytes OK" | PI's terminal output in the project conversation (14:32, 16:37 +03:00; 12 Nov 08:09 +03:00) |
| First attempt | 14:14 +03:00: a block that used the working tree of `~/rtg-corpus` stopped at its clean-tree check; nothing ran | conversation; preregistration §8 |
| Run | started between 14:17 and 14:32 +03:00 in a separate worktree; 5,781 records of cell C1 written when the console session timed out and the processes ended (seen at 16:23–16:37 +03:00) | conversation; manifests (`runs_present_before` 1435 + 1501 + 1504 + 1341) |
| Resume | 16:35:58 +03:00, detached from the terminal, `--resume`, same `--jobs 4`; fixtures rerun (pass, Python 3.12.3); finished 21:11:11 +03:00 | `CAMPAIGN_COMPLETE.json` (`resumed: true`, `started_utc`, `finished_utc`) |
| Machine | one core (`nproc` = 1), Linux 6.8.0, Python 3.12.3; about 5 s per run at C1 against 0.38 s in the test campaign | marker; record field `secs` |
| Upload | branch `upload/az-token-resonance-stage1`, commit `95db7af` by the PI (18:11:12Z), 41 files, 25.5 MB, directory `upload/az-token-resonance-stage1/` | GitHub |

## 3. Custody and verification (`EV-BYTES`, `EV-HASH`, `EV-RUN`)

`bash evidence/az/token_resonance/stage1/verify.sh` (output `verify_output.txt`), run from this branch on 12 Nov 2026 with Python 3.13.18:

- registered package: `SHA256SUMS` passes (50 files);
- campaign directory: `HASHES.txt` passes (39 files; SHA-256 of `HASHES.txt` `5ddbc605…500a`, equal to the value in the completion marker);
- marker: plan `stage1`, confirmatory, 4 workers, fixtures not skipped; the eight SHA-256 values it records (engine, orientation reference, runner, fixtures script, analysis script, driver, golden file, `HASHES.txt`) equal the bytes in the repository;
- 19,900 records in 12 files (C1 9,400; C2 7,500; C3 3,000);
- the registered analysis, rerun from the uploaded files, exits with code 0 for C1 (with the sensitivity set C3) and C2, and its two outputs are **byte-identical** to the outputs produced on the campaign machine (`analysis_S1-C1.rerun.txt`, `analysis_S1-C2.rerun.txt`).

The campaign therefore reproduces across two machines and two Python versions (3.12.3 and 3.13.18) at the level of the analysis output; the per-record determinism across platforms is covered by fixture T10, which passed on the server.

## 4. Integrity, gates and controls (verbatim)

Cell C1:
```
INTEGRITY: PASS (9400 records in 4 file(s); identity, custody, states, records and set checked)
G1 fixtures on the campaign machine: PASS
G2 token law (alphabet, exact class update, centre witness), summed violation counter: 0 -> PASS
G3 node-label permutation: PASS
    0 of 400 permuted runs differ in (M, births, steps, fb, M_at)
G4 sham perturbation vs BASE (native and perturbed slot token non-resonant): EQUIVALENT
    n=1392  p1=0.0287  p0=0.0223  RD=+0.0065 [-0.0039, +0.0168]  discordant 31/22  McNemar p=2.717e-01
G5 detuned arm O1D vs BASE (native slot token non-resonant): EQUIVALENT
    n=1436  p1=0.0160  p0=0.0223  RD=-0.0063 [-0.0151, +0.0026]  discordant 16/25  McNemar p=2.110e-01
G5 detuned arm O2D vs BASE (native slot token non-resonant): EQUIVALENT
    n=1436  p1=0.0230  p0=0.0223  RD=+0.0007 [-0.0091, +0.0105]  discordant 26/25  McNemar p=1.000e+00
```
Cell C2:
```
INTEGRITY: PASS (7500 records in 4 file(s); identity, custody, states, records and set checked)
G1 fixtures on the campaign machine: PASS
G2 token law (alphabet, exact class update, centre witness), summed violation counter: 0 -> PASS
G4 sham perturbation vs BASE (native and perturbed slot token non-resonant): EQUIVALENT
    n=1449  p1=0.0117  p0=0.0124  RD=-0.0007 [-0.0076, +0.0062]  discordant 12/13  McNemar p=1.000e+00
G5 detuned arm O1D vs BASE (native slot token non-resonant): EQUIVALENT
    n=1475  p1=0.0115  p0=0.0122  RD=-0.0007 [-0.0077, +0.0063]  discordant 13/14  McNemar p=1.000e+00
```
Proposition 1 of the preregistration (signed token alphabet, exact class update) had no violation in any of the 19,900 runs.

## 5. Registered readings (verbatim)

**Family 1 — the only confirmatory family (cell C1, `N = 120`):**
```
PC1  O1R vs O1D  (2x = 0)
    n=1500  p1=0.2580  p0=0.0153  RD=+0.2427 [+0.2166, +0.2681]  discordant 374/10  McNemar p=8.901e-97  Holm p=1.780e-96
    registered reading (family 1): SUPPORTED (Holm p < 0.05 and lower limit > 0.05)
    qualifiers: UNQUALIFIED (every control of this cell reads PASS or EQUIVALENT)
PC2  O2R vs O2D  (2x = N/2)
    n=1500  p1=0.1853  p0=0.0240  RD=+0.1613 [+0.1381, +0.1841]  discordant 259/17  McNemar p=9.375e-57  Holm p=9.375e-57
    registered reading (family 1): SUPPORTED (Holm p < 0.05 and lower limit > 0.05)
    qualifiers: UNQUALIFIED (every control of this cell reads PASS or EQUIVALENT)
```
**Family 2 — supportive replication, separate (cell C2, `N = 122`):**
```
PC3  O1R vs O1D  (2x = 0)
    n=1500  p1=0.2307  p0=0.0113  RD=+0.2193 [+0.1944, +0.2436]  discordant 336/7  McNemar p=1.188e-89  Bonferroni p=2.375e-89
    registered reading (family 2): SUPPORTED (Holm p < 0.05 and lower limit > 0.05)
    qualifiers: UNQUALIFIED (every control of this cell reads PASS or EQUIVALENT)
PC4  Q2R vs BASE (no order-2 token exists)
    n=1500  p1=0.0087  p0=0.0160  RD=-0.0073 [-0.0158, +0.0011]  discordant 10/21  McNemar p=7.076e-02
    registered reading (family 2): EQUIVALENT TO BASE within +-0.05
    qualifiers: UNQUALIFIED (every control of this cell reads PASS or EQUIVALENT)
```
**Erratum N1, declared before the data (preregistration §12):** in the PC3 reading the words "Holm p < 0.05" are to be read "Bonferroni-adjusted p < 0.05"; the adjusted value is the one printed on the line above (`2.375e-89`). Number and decision are unaffected.

## 6. Descriptive outputs (no reading)

Full text in the two analysis files. Selected:

- **Pooled `4x ≡ 0` (S1):** risk difference +0.202 (bootstrap 95 % +0.186 to +0.218).
- **Native association (S2), the pilot's quantity.** `N = 120`, 1,500 native draws: tails `30/188` with a `4x ≡ 0` seed against `12/1312` without; risk ratio 17.5 (Katz 95 % 9.1–33.5). The exploratory pilot gave 40.1 (21.4–75.2) on `61/258` against `11/1865`: the association is confirmed and the pilot's size was an overestimate. `N = 122`: `24/97` with an order-1 seed against `0/1403` without.
- **Resonant arms by value (S4):** `0` and `N/2`: 24.9 % and 26.7 % (`N = 120`), 23.4 % and 22.8 % (`N = 122`); `N/4` and `3N/4`: 18.5 % and 18.6 % — as the exact invariance under `δ ↦ δ + N/2` requires. The four near-quarter values at `N = 122`: 0.5 % to 1.7 %.
- **Other tokens non-resonant (S5):** PC1 +0.226 on `310/1` discordant pairs; PC2 +0.148 on `206/4`; PC3 +0.214 on `306/1`. In these pairs the detuned arm has a tail in 0.4 % (`N = 120`) and 0.07 % (`N = 122`) of the runs.
- **Thresholds (S6):** the contrast is present at every threshold from `M ≥ 60` to `M ≥ 300`. The two orders differ at the top: 13.4 % of order-1 runs reach the 300-node stop, 1.4 % of order-2 runs.
- **Token classes (S7):** runs with `Y = 1` end with one signed token class holding about 0.9 of the nodes in every arm; runs with `Y = 0` with about 0.53.
- **First birth (S10), descriptive, not a mediation analysis:** median first-birth tick 64 (order 1), 61 (order 2), 63–69 in the other arms.
- **TDR-26 birth-anchored rule (S8), outside its source scope:** in the order-1 arm at `N = 120` the rule is positive in 331 runs (318 of them tails) and negative in 1,156 (68 of them tails); in the order-2 arm 158 positive (153 tails) and 1,327 negative (125 tails). It validates nothing at this `N`.
- **Sensitivity, superseded orientation rule (profile `P2`, 500 base draws, no reading):** 2,748 of 3,000 runs have the same `(M, births)` as under `P1`; `Y` differs in 42; contrasts +0.240 (+0.195 to +0.283) and +0.124 (+0.088 to +0.159).

## 7. What this establishes and what it does not

Within the registration (§6.6): a `[NUM]` statement, for the pinned engine with `TDRG-DEF-ORIENT`, `bound_symmetric`, `N ∈ {120, 122}`, `k = 8`, four initial nodes, 800 ticks and the threshold `M ≥ 100`, that setting one initial token to a value with `4x ≡ 0 (mod N)` causes a large increase of the tail risk, that the `±1` neighbours of such values behave like native non-resonant tokens within `±0.025`, that perturbing a non-resonant token by `±1` is neutral within `±0.025`, that the outcome does not depend on node labels, and that at `N ≡ 2 (mod 4)`, where `2x ≡ N/2` has no solution, the values nearest `N/4` show no effect.

Not established: why. The first-contact mechanism remains OPEN; Proposition 3's parent–child law is a candidate only. Nothing is shown about `N`-scaling, other `k/N`, other policies, longer horizons, the TDR-26 defective basin at `N ≈ 720`, or any continuous-branch quantity; OPEN-P1 is untouched, and there is no relation to AZ's Hashimoto `4 | q` rule or to Dyadic/DZT `q = 4` beyond the numeral (SG-AZ-7, SG-DZT-1). `TDRG-OPEN-SPECCONS-STAR` and `TDRG-OPEN-LOCKING-FAIL` stay open and stay TDR-G's.

## 8. Deviations and process notes

1. **Interruption and resume.** Allowed by the registration (§8) and visible in the manifests. The 5,781 records written before the interruption were kept; the runner's resume checks passed; `--jobs` was 4 in both invocations. The first invocation left no manifest line (it was killed); every shard's single manifest line is that of the resumed invocation and records how many records were present before it.
2. **Location of the data.** The preregistration (§8) said the directory would be placed under `evidence/az/token_resonance/stage1/`. It stays where it arrived, `upload/az-token-resonance-stage1/` (25.5 MB), as other custody uploads do; `evidence/az/token_resonance/stage1/` holds the verification script and the rerun outputs. Bytes and analysis are unaffected.
3. **Two PI decisions of 11 Nov 2026, 18:15 +03:00, could not be met as worded** (`records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` §5, rows 1 and 3: an outcome rule recorded before Stage 1 runs; PR #211 merged before the run and an authorisation naming the bytes). The run had been started by the PI at about 14:17 +03:00 and resumed at 16:36 +03:00, before that decision; the AZ co-owner session learned of the decision on 12 Nov, after it had rerun the analysis. What exists instead: the registration and both reviews are timestamped on GitHub before the run (§2); the run verified the registered bytes itself; the outcome rule is taken up in §9.
4. **Not yet done:** the independent rerun by the second co-owner (`verify.sh`).

## 9. Outcome rule — proposal, worded after the run had started and before any Stage 1 result was analysed; replaced by the PI's rule in §11

The PI decided that an outcome rule (home and grade path of an Action 1 result) be recorded before Stage 1. That is no longer possible: the data exist and this session has seen them. To keep the rule independent of the result, this report does not draft one. It proposes the wording the Atlas owner wrote in its advisory at 14:56 +03:00 on 11 Nov (commit `410bee1`), when the campaign had started but no analysis had been run and no result was known to anyone:

> a supported contrast enters AZ as a `[NUM]` diagnostic inside Level A and is offered to TDR-G; it does not by itself answer AZ-OPEN-PROMO; it becomes a TDR-G statement only by a TDR-G edition.

If the PI confirms it, the consequences for this result are: it may enter the AZ DSN, at the next AZ edition and by the PI's decision, as a `[NUM]` diagnostic with its scope line; AZ stays Level A; whether AZ-2 is met is a separate decision the rule does not make; the result is offered to TDR-G through `pipes/TDRG/`, and nothing about TDR-26 or the token laws is a TDR-G statement until a TDR-G edition says so.

## 10. Decisions for the PI

1. Confirmation of the outcome rule (§9), or other wording.
2. Merge order, if the PI accepts the package as [SESSION] material (a merge adopts nothing): PR #211 (registration), the upload PR (custody), then this report with the verification files.
3. Whether to record, after the fact, the authorisation of Stage 1 naming the bytes of §2.
4. Stage 2 (`N = 240, 242, 480`) and Stage 3 (TDR-26 in its own scope, with TDR-G): both are proposals in the preregistration §10 and need design decisions before any run; large runs go to the server.

## 11. After the report — review, PI decision, merges (added 12 November 2026)

This section records what happened after §§1–10 were written. It changes no number and no reading. The title of §9 was changed in the same edit, on the reviewer's recommendation (item 2).

1. **Independent review.** Second co-owner (ChatGPT), GitHub review `5869662603` on PR #228 at head `f568787`, 12 Nov 2026, 08:39 +03:00: *accepted (scoped), with provenance qualifications; no new blocking finding*. Done by the reviewer, on the stored blobs: SHA-256 of all 50 package files and all 39 campaign files, equal to `SHA256SUMS` and `HASHES.txt`; the `HASHES.txt` digest; the 12 record files against their manifests; all 19,900 records parsed and their identity, parameter, law-counter and birth-count fields checked; the four registered pairs re-aggregated from the raw records, with Agresti–Min intervals and exact McNemar `p` computed by the reviewer's own code — equal to §5; G4/G5 discordance counts and the label-permutation control; the two rerun outputs compared with the campaign machine's outputs, byte-identical. **Not done by the reviewer, by its own statement:** `verify.sh` was not executed (no checked-out repository in its runtime), and no engine run was repeated. Item 4 of §8 therefore stands in this form: the registered analysis has been executed on the campaign machine (Python 3.12.3) and in the author's session (Python 3.13.18; again on `main` `ffaf5e7` after the merges, `VERIFY PASS`); the reviewer's check is an independent recomputation from the raw records, not an execution of the registered script.
2. **Reviewer's provenance qualifier, applied.** The Atlas wording quoted in §9 was committed on 11 Nov at 14:56 +03:00 (`410bee1`), after data collection had begun (about 14:17 +03:00), though before any Stage 1 aggregate was analysed; the exploratory pilot analyses existed earlier. §9 is not a pre-data rule and its title no longer reads as one.
3. **Outcome rule — the PI's decision.** Source: GitHub comment `6817166013` on PR #228 (12 Nov 2026, 10:06 +03:00, from the PI's account), relayed by the PI to this session at 11:16 +03:00. The conversation in which the decision was given is not available to this session. The comment records the PI's reply "Metni onaylıyorum" to this wording:

   > A validated, supported Action 1 contrast is eligible for a PI-approved `[NUM diagnostic]` entry within AZ Level A, with its exact simulation scope and provenance. It is offered to TDR-G for owner disposition. It does not by itself close AZ-OPEN-PROMO, promote AZ maturity, or become an adopted TDR-G claim.

   This is the rule; the proposal of §9 is replaced by it. It was written and confirmed **after** Stage 1 was complete, analysed and reviewed, and it is not the pre-analysis wording §9 proposed. The differences from that wording: "is eligible for a PI-approved entry" instead of "enters"; "validated" and "with its exact simulation scope and provenance" added; "promote AZ maturity" added to what the contrast does not do; "becomes a TDR-G statement only by a TDR-G edition" replaced by "offered to TDR-G for owner disposition" and "does not … become an adopted TDR-G claim". None of them widens what the result may claim. As the comment itself says, the PI approved a rule for the disposition of results, not the adoption of the Stage 1 result into any DSN and not a change of AZ's maturity level.
4. **Consequences under the rule.** PC1 and PC2 are eligible for a `[NUM diagnostic]` entry in the AZ DSN at a later AZ edition, by a separate PI decision, with the scope of §7. AZ stays Level A; AZ-OPEN-PROMO is not answered. The offer of the numerical result to TDR-G has not been filed: `pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md` (open) covers Propositions 1–3 only and says so.
5. **Merges, by the PI, merge commits:** PR #211 `07a20c1`, PR #227 `a36404c`, PR #230 `16d28fa` (12 Nov, 09:55–09:56 +03:00), PR #228 `082f702` (10:04 +03:00). PR #228 was merged at head `720b0bd`, which is the reviewed head `f568787` plus a merge of `main`; this report had the same bytes at both (SHA-256 `7896f9ec66cf9cdcb6cdceb0cea7192d72d7576c3ec99d026a76369725ba96ea`), and the package and campaign hash lists verify on `main`. No tag was created; the AZ row of `BASELINE.md` is `az-v0.7`, unchanged.
6. **PI decisions of 12 Nov 2026, 11:30 +03:00** (project conversation with this session; the PI's replies to the four open points, verbatim):
   - *Start of the AZ v0.8 cycle:* "başlatalım" — the cycle is started. Whether the Action 1 diagnostic enters v0.8 was asked in the same point and was not answered separately; it stays a separate PI decision, as the outcome rule requires.
   - *Offer of the Stage 1 numerical result to TDR-G as a separate pipe item:* "gerek yok" — not filed. TDR-G has the offer of Propositions 1–3, which names the campaign and this report.
   - *After-the-fact authorisation of Stage 1:* "yetki kaydı verilebilir" — recorded in item 7.
   - *Stage 2 and Stage 3:* no decision; the PI asked for an explanation of what the choices would entail first.
7. **Retrospective authorisation record for Stage 1.** By the PI's decision of 12 Nov 2026, 11:30 +03:00 (item 6), this is the record of authorisation of the Stage 1 campaign, given **after** the run and to be read as such; it is not a pre-run authorisation and changes nothing in §8 item 3. The bytes it names: the preregistration package at commit `47dee4632096e441933ae28868a85f82e3355aaa` (PR #211 head), `evidence/az/token_resonance/SHA256SUMS` with SHA-256 `81c87dcfc8d326e3c29861b9124c9654535f1c64cc6e5f9c7a9c9cafa6abd6eb` (50 files, among them the runner `75c5f139…8992`, the analysis `490b3d4f…dc80` and the driver; engine `4c94d874…a608` and orientation reference `ca59e9b9…d59c` pinned by the runner); plan `stage1`, tag `AZ-TOKRES-S1`, cells C1–C3, 19,900 runs; run by the PI on the PI's Ubuntu server with the block of the preregistration §8, started 11 Nov 2026 about 14:17 +03:00, resumed 16:36 +03:00, finished 21:11 +03:00; output `upload/az-token-resonance-stage1/` at commit `95db7af`, `HASHES.txt` SHA-256 `5ddbc60516acbeb75f2fc09fabdcaa017a320a68d88ee4904767c1c59b88500a`. What existed before the run: the registration and both reviews (`5855522171`, `5857601141`), timestamped on GitHub; the campaign verified the package hashes itself before its first run.
8. **Still open:** Stage 2 and Stage 3 (with the PI, after the explanation asked for); TDR-G's disposition of the offer; an execution of `verify.sh` by someone other than the author.
