# AZ token-resonance fork design — BASE-only pilot: authorisation record

**[SESSION] NONCANONICAL operational record.** It records the PI's authorisation of the BASE-only pilot (`records/az/AZ_TOKEN_RESONANCE_FORK_BASE_PILOT_PROTOCOL.md`) and binds the run to one frozen manifest.

## 1. The PI's decision

PI, 20 Nov 2026, 22:43 +03:00, verbatim:

> "1- Chat GPT yazar Claude denetler / 2- Uygun / 3- False / 4 Uygun / 5 Sunucuda koşabiliriz"

Row 1, clarified at 22:52 +03:00: "Bu PR'ı Claude bitirsin". The rows refer to the decisions in §6 of the protocol, and their reading is recorded there.

## 2. What is authorised

The pilot is run **once** on the PI's server under the following conditions:

- It is run **only after** ChatGPT's readback PASS of both the R1b fix (`79ef9e6`) and the freeze commit that adds this record.
- It uses the manifest and script identified below, unchanged.
- It is run in a separate worktree at the freeze commit, by a fresh process.
- The output directory is new.
- After the run:
  1. the audit is run against the same manifest and H;
  2. the output directory is uploaded unchanged on an `upload/az-fork-base-pilot` branch, with its `SHA256SUMS`;
  3. the pilot report is written by ChatGPT and reviewed by Claude, following the task split of §6, row 1.

| Item | Identity |
|---|---|
| Manifest | `evidence/az/mechanism/base_pilot_manifest.json`, **H = `c218cad90e9bfd7d3911a630168aa356e8ff6aad1b448383b4ed27f8a7e44203`** |
| Driver | `evidence/az/mechanism/az_fork_base_pilot.py`, SHA-256 `a91ada53dd6f629cade2b8a2b6addc9b7ad2f5818ae06e023f084c6feb17d0a1`, equal to `frozen_script_sha256` in the manifest |
| Dependencies | contact clock `4cdd9a7d…8eee`, provenance library `5d5ca8ac…3f68`, runner `75c5f139…8992`, engine `4c94d874…a608`, orientation `ca59e9b9…d59c`. These are checked by the driver before anything is loaded. |
| Parameters | tag `AZ-FORK-BASEPILOT-P1`, N = 120, k = 8, P1 / `bound_symmetric`, cap 300, q = 100, n = 500, 𝓛 = {100, 200, 400, 800}, threshold 0.95, `wilson_in_rule = false` |

## 3. What is not authorised

The following are not authorised:

- any R/D fork on the pilot seeds, and any reuse of these seeds in a later campaign;
- a second run, or a run with any other manifest, script or H;
- any change to the L rule after the run.

The power calculation, the seed law and sample size of the R/D campaign, the analysis code, the preregistration and the campaign compute each need a separate PI decision.
