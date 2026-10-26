# DISC-1 Canonical Freeze Manifest v1

**Manifest ID:** `NG_DISC1_FREEZE_MANIFEST_v1`
**Scientific freeze / ruling date:** 2026-08-31 · **Manifest generation date:** 2026-09-01
**Purpose:** record the canonical pre-data artifact bundle for the N-5 discrimination architecture. Provenance record only — no scientific content.
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.15` (sha256 `d56440c68ca047c7d76877043710a7e4251de439b948a69411506a9c605f3375`)

## Canonical bundle

| Role | Artifact | sha256 |
|---|---|---|
| Identity certificate (final) | `ng_n5_discrimination_identity_cert_v5.py` | see below |
| Criterion memo (final pre-data state) | `NG_N5_DISCRIMINATION_CRITERION_v6_2.md` | see below |
| Analysis harness (frozen before data) | `disc1_analysis_harness_v1.py` | see below |
| Regression guard | `disc1_labelneutral_regression_v2.py` | see below |
| Pre-registration | `NG_DISC1_FROZEN_PREREGISTRATION_v1.md` | see below |

Hashes are appended by the generating command below and were computed in the auditor's execution environment; they are recorded so any party can recompute and compare rather than take them on assertion.

## Superseded, retained for lineage

- `NG_N5_DISCRIMINATION_CRITERION_v1..v5`, `v6`, `v6_1` — superseded memos; `v1`'s A3/A6 and `v2`'s T3 carry `[COR]`/`[RETRACTED]` records that must not be silently dropped.
- `ng_n5_discrimination_criterion_cert_v1/v2`, `ng_n5_discrimination_identity_cert_v3/v4` — superseded certificates.
- `disc1_labelneutral_regression_v1` — superseded, **not retracted**; passed as written, rows carried forward as L1–L8 of v2.

## Frozen parameters (restated for checkability)

`𝒦_DISC = {0,1,2,3}`, `k₀ = 1`, `K_stab = {2}`, `K_cont = {0,3}`, positive-band adjacency `1~2, 2~3`, same-realization guard in force, comparison qualifies only if dual-active. DISC-1D is label-neutral per PI ruling.

## Artifact dating

The scientific content of every bundle member is frozen as of the ruling date **2026-08-31**. The two provenance artifacts were generated or repaired on **2026-09-01**. Bundle members other than those two were left byte-unchanged during the provenance repair, deliberately: editing the harness or the regression would alter hashes on which the "frozen before data" claim depends, so their generation dates are recorded here rather than inside them.

| Artifact | Content frozen | File generated / last written |
|---|---|---|
| `ng_n5_discrimination_identity_cert_v5.py` | 2026-08-31 | 2026-08-31 |
| `disc1_analysis_harness_v1.py` | 2026-08-31 | 2026-08-31 |
| `disc1_labelneutral_regression_v2.py` | 2026-08-31 | 2026-08-31 |
| `NG_DISC1_FROZEN_PREREGISTRATION_v1.md` | 2026-08-31 | 2026-08-31 |
| `NG_N5_DISCRIMINATION_CRITERION_v6_2.md` | 2026-08-31 (ruling) | **2026-09-01** (provenance patch) |
| `NG_DISC1_FREEZE_MANIFEST_v1.md` | — (provenance record) | **2026-09-01** |

Internal date lines carrying only `2026-08-31` in the four unchanged artifacts refer to the scientific freeze, not to file generation; this table is authoritative for the latter.

## Verification note

The auditor computed the listed hashes and observed exit 0 for the certificate, harness self-test, and regression in its own execution environment. An independent party should recompute rather than rely on that report. The reviewing party in this cycle reported that sandbox mounts were not visible to its runtimes and therefore did not independently recompute; that limitation is recorded here rather than left implicit.

## State

Pre-data architecture closed. Next operation: owner-compatible per-cycle BIND3 enumeration at `N = 24` for `k ∈ {0,1,2,3}` over the frozen raw seed panel → DISC-1B → frozen DISC-1D transport audit.

## Computed hashes

Computed 2026-09-01, after the date-metadata patch. The v6.2 hash below supersedes the value recorded in the previous manifest revision, which was taken before that patch.

```
f3fbc05318c46120f466eac0c22f442bcc3561853ce4f56573cb7a287afd8a86  ng_n5_discrimination_identity_cert_v5.py
e8e5b6a7063f36a21778257e09b872d44d94563dbe7cdf7f23d97f8e27fe8fca  NG_N5_DISCRIMINATION_CRITERION_v6_2.md
57a15421b352f8fbe58d7642d78a6ebb936b78aae90d91b9e39034b738510d9d  disc1_analysis_harness_v1.py
76f1b571b951b174eaeadf88ce9b39eb550e39fbf841274e0f48131d14fd7603  disc1_labelneutral_regression_v2.py
dee081f5cf04a20212ea6294030d891145a25d1e00ef00b5d1c7e8396ec00c38  NG_DISC1_FROZEN_PREREGISTRATION_v1.md
```
