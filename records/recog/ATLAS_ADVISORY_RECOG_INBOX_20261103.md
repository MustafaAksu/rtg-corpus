# Atlas advisory — RECOG inbox (RECOG.R-A1 re-check) and pin currency

**Date:** 3 November 2026. **By:** Claude, Atlas owner. The Atlas advises; the RECOG co-owners disposition; the PI adopts.
**Status:** NONCANONICAL advisory. It changes no RECOG text, grade, RID, certificate or pipe state.
**Object:** `recog-v0.3.26`, `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`, SHA-256 `45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34` (1,463 lines; equal on `main` `d340282`). Line numbers below are at that tag.
**Atlas context:** `atlas-v0.9` (`b48343f5…3b70`). Rows RECOG.R-A1 (L857) and the RECOG and Dyadic node rows that cite it (L369, L388, L741).
**Evidence states:**
- `EV-SRC-READ`:
  - the two open items in `pipes/RECOG/`;
  - `recog-v0.3.26`;
  - the producer tags `dyad-v6.4.23`, `numgen-v1.21`, `gen-v2.10`, `ofn-v0.12`, `rrf-v0.8.4`, `tdrg-v2.12.14`.
- `EV-RERUN` (Atlas): the eight A1c certificates, run twice — once as committed, once with c′_Q = 0.36916.
  - Evidence: `evidence/recog/atlas_review/ra1/`, holding the driver `recog_ra1_cprime_recheck.py`, `ra1_recheck_summary.json` and `ra1_run_note.md`.
  - The rerun replays owner certificates with one changed input. It is not a re-proof.

## 0. Summary

`pipes/RECOG/` holds two open items:
- the Dyadic v6.4.23 notice, which asks for the c′_Q re-check;
- the OFN v0.11 notice, which asks nothing.

The two NUMGEN items are already dispositioned (co-owner state review, 29 October).

**The re-check result.** With c′_Q = 0.36916:
- all 57 gates of the eight A1c certificates pass;
- no boolean leaf of any certificate JSON changes;
- no decimal printed in the RECOG DSN changes.

The run as committed reproduces every committed JSON and output file **byte for byte**. The replacement 0.36915 → 0.36916 is therefore a maintenance edit with no effect on any statement.

**What the registration does not cover.** RECOG's `[assuming: (D5)]` names three things:
- c_Q;
- c′_Q;
- "the remainder decomposition r = Λ₃ + rest with its constants".

Dyadic registered the first two and the exact decomposition. Two of the "rest" constants that the certificates use are still constants of the proof sketch only, with no theorem row of their own:
- c_J = 0.50220;
- c₇ = 157.58.

So the registration alone does not support dropping the qualifier entirely. It supports narrowing it (§2).

**The C₇ rows.** The C₇ rows are a clean import. `DYAD-THM-NF-REM-C7-SHARP` registers exactly the ceilings that RECOG assumes, on the same chart and norm (§3).

| # | Item | Atlas proposal |
|---|---|---|
| R1 | c′_Q re-check (DYAD notice) | accept; replace 0.36915 by 0.36916 at the five text sites and the one script literal; rerun and re-register the affected certificate hashes |
| R2 | what `[assuming: (D5)]` becomes | owner decision; the Atlas reading is **narrow, not drop** (options a–c in §2) |
| R3 | `RECOG-THM-R9-SHARPENED-ROWS-C7` | accept with change; replace the `[assuming:]` by an import of `DYAD-THM-NF-REM-C7-SHARP` and update the stale wording |
| R4 | release tooling quoting Dyadic text | note for the next stage-1 package: re-quote at `dyad-v6.4.23` |
| R5 | OFN v0.11 notice | accept (receipt); no imported OFN statement changed |
| R6 | pins | repin Dyadic, NUMGEN, Genesis and OFN where a use changes (Methodology v1.4 §3.3); all cited RIDs resolve at the current tags |

All six fit one maintenance edition (v0.3.27) with one content stage. R2 needs a decision before the text is written.

## 1. R1 — the c′_Q re-check

**The notice** (`pipes/RECOG/20261030-DYAD-v6-4-23-adopted.md`):
- `DYAD-THM-LPHASE-ROWA-BRIDGE` (ii) registers |D_Q − D₃| ≤ c′_Q q² with **c′_Q = 0.36916**;
- the certified majorant is 0.3691523046…;
- RECOG's value 0.36915 lies below the majorant, so it is not a certified ceiling.

Dyadic corrected its own proof-sketch display in the same edition (`[COR]` at `dyad-v6.4.23` §6.14).

**Where 0.36915 occurs in RECOG.**

| Site | Claim |
|---|---|
| L753 | `RECOG-ALG-A1C-TAIL-HARMONICS` `[assuming:]` |
| L761 | `RECOG-THM-A1C-SHARPENED-SCHEDULE` `[assuming:]` |
| L773 | `RECOG-ALG-A1C-LOGFREE-ENVELOPE` `[assuming:]` |
| L1051 | `RECOG-ALG-A1C-START-OFFSET` (ii) `[assuming:]` |
| L1175 | §7 import row `DYAD-THM-LPHASE-ROWA-REMAINDER` |
| (by reference) L1049, L1053 | `RECOG-ALG-A1C-ADMISSIBLE-REGION` and `-JOINT-CONTRACTOR` ("as RECOG-THM-A1C-SHARPENED-SCHEDULE") |
| script | `evidence/recog/scripts/recog_a1c_tail_averaging_cert.py` L55, `I("0.36915")` — the only literal in the chain |

**How the value propagates.** The other A1c certificates import `cQp` from part 1b:
- directly: start offset, unknown-a interval, in-block angular, joint transfer;
- through start offset: drift centring and drift proof table;
- through in-block angular: combined tail.

**What the Atlas ran** (`evidence/recog/atlas_review/ra1/`):
1. It checked all eight scripts against the hashes registered in the RECOG DSN artifact rows: 8/8 match.
2. It ran the chain in the repository layout twice. The `patch` tree changes only L55 to `I("0.36916")` (patched script SHA-256 `c731cf1b…3dff24`).
3. Part 1b ran with its committed orbit length of 6,000,000 steps (`argv[2]`; JSON `G5.N_steps`).

**Results.**

| Certificate | As committed vs committed outputs | Gates with 0.36916 | Largest relative change |
|---|---|---|---|
| tail averaging (part 1b) | byte-equal | 8/8 | 2.71 × 10⁻⁵ (the C term, linear in c′_Q) |
| start offset | byte-equal | 7/7 | 1.44 × 10⁻⁵ (β(a)) |
| unknown-a interval | byte-equal | 7/7 | 1.6 × 10⁻⁹ |
| in-block angular | byte-equal | 7/7 | 2.7 × 10⁻⁷ |
| combined tail | byte-equal | 8/8 | 2.7 × 10⁻⁷ |
| joint transfer | byte-equal | 9/9 | 1.41 × 10⁻⁵ (ω widths) |
| drift centring | byte-equal | 7/7 | 9.8 × 10⁻⁶ (slip-test terms) |
| drift proof table | byte-equal | 4/4 | 0 (only the import-hash field changes) |

The run reached the certificates: the part-1b C term changes by exactly (0.36916 − 0.36915)/0.36915 = 2.709 × 10⁻⁵ at every table point, and β(a) rises by exactly 10⁻⁵ · 256/225.

Printed values are unchanged at their displayed precision:
- E′ ≤ 0.31: box maximum 0.3095493 in both runs;
- β(625) = 0.799 and β → 0.792 (L1051);
- the 73-slip containment results;
- C(a, r) = 58.0 / 61.0 / 75.1 (L775). The proof-table JSON is identical apart from its import-hash field.

The boolean leaves that are `False` in the JSONs are the same in both runs and in the committed files. They are reported observations, not gates: two `G3c_E5n_rises_from_1e4` entries and the twelve `Theta0_full` hull flags.

**Proposal.**
- In v0.3.27, write 0.36916 at the five text sites.
- Change L55 of the part-1b script.
- Rerun the chain as owner and re-register the changed script and output hashes (`RECOG-ART-A1C-SHARPENED-SCHEDULE` and the rows that list the downstream outputs).

The Atlas rerun shows what the owner rerun should find; it does not replace it.

**One observation for the owners.** The proof-table JSON does not move at all, because its all-M constants use the widest b-range (|ω| ≤ Δ_a, with Δ_a = (16/15) c_Q √a), not β(a). In the log-free envelope, c′_Q therefore enters only through the start-offset enclosure used on records (the drift-centring slip tests move), not through C(a, r).

Whether the L773 `[assuming:]` should then name c′_Q only for that step is a wording question for the owners. The Atlas does not propose a change.

## 2. R2 — what `[assuming: (D5)]` becomes

**The registered result** (`dyad-v6.4.23` §6.14, L910) covers:
- (i) the exact decomposition r = Λ₃ + [S_Θ − L_Θ] + τ[D_Q − D₃] + [Arg(J/z) + τq] + Arg(F̂/J) under (B);
- (ii) c_Q and c′_Q.

Its scope is the row-A disk |z| ≤ 1/20 of the `DYAD-THM-NF-INV` chart, at block base points in U, with branch (B) on U_T. This matches RECOG's use: chart row A, block base points, x₀ ∈ U.

**The constants of the "rest" that the certificates use** (part-1b L55–57: `c_r2 = K_Theta + taubar*cQp + cJ; c_r3 = c7`):

| Constant | Value | Dyadic source at `dyad-v6.4.23` | Theorem row? |
|---|---|---|---|
| K_Θ | 123/125 | `DYAD-THM-OPEN3-SPIRAL-REM` table, row \|z\| ≤ 1/20 | yes |
| c_Q, c′_Q | 0.79246, 0.36916 | `DYAD-THM-LPHASE-ROWA-BRIDGE` (ii) | yes (new) |
| c_J | 0.50220 | proof sketch of `DYAD-THM-LPHASE-ROWA-REMAINDER` (L906) | **no** |
| c₇ | 157.58 (from C₇ = 100) | same proof sketch (L906) | **no** |

**The Atlas reading.** After v6.4.23, RECOG can import (i) and (ii) by RID. The `[assuming:]` still has to name c_J and c₇, or RECOG has to supply them. Options for the owners:
- **(a) Narrow.** Import `DYAD-THM-LPHASE-ROWA-BRIDGE` and `DYAD-THM-OPEN3-SPIRAL-REM`. Keep `[assuming: c_J = 0.50220, c₇ = 157.58 as published in the proof of DYAD-THM-LPHASE-ROWA-REMAINDER]` at the five sites.
- **(b) Supply.** Derive both bounds RECOG-side from adopted rows:
  - c_J from the jet J of `DYAD-ALG-NF6`;
  - c₇ from C₇ = 100 of `DYAD-THM-NF-REM`, or from C₇ = 85.1 of `DYAD-THM-NF-REM-C7-SHARP`, which would give a smaller c₇.

  This needs a certified computation, so it is new science: a separate cell with review, not part of the maintenance edition.
- **(c) Ask.** File a request in `pipes/DYAD/` to register c_J and c₇. The (D5) qualifier then drops once Dyadic answers.

(a) is the maintenance-sized step. (b) and (c) can follow without blocking it. Under every option the grades stay as they are: the co-owner review of 29 October (§3) already records that the registration affects the source conditions, not the proof grade.

## 3. R3 — the C₇ rows

**RECOG's assumption** at L662: `RECOG-THM-R9-SHARPENED-ROWS-C7` assumes C₇ ≤ 85.1 on |z| ≤ 1/20 and C₇ ≤ 27.7 on |z| ≤ 1/40.

**What Dyadic registered** (`dyad-v6.4.23` L804): `DYAD-THM-NF-REM-C7-SHARP` gives exactly these values:
- the exact bounds are 85.0731933471… and 27.6022209836…;
- the scope is "chart and norm of DYAD-THM-NF-REM; rows not mixed";
- the `DYAD-THM-NF-REM` constants stay at C₇ = 100/30 and C_D = 1000/250, and the certificate's C_D bounds are not re-derived.

**Why the scope fits.** RECOG's rows use q_max = 1/400 and 1/1600, that is |z| ≤ 1/20 and 1/40, unmixed. Its certificate `recog_b1_l1l2_sharpened_rows_cert.py` uses C₇ and not C_D, so the C_D caveat does not reach it.

**Proposal.** Replace the `[assuming:]` by `[import: … | DYAD-THM-NF-REM-C7-SHARP]` and add the row to §7. Three wording points go stale with the import:
- **L662.** "Dyadic's published DYAD-THM-NF-REM certificate values 85.07 / 27.60 rounded up; these are not Dyadic theorem statements; registration requested (§7)". Dyadic now displays 85.0732 / 27.6023, "rounded up", and states that the earlier 85.07 / 27.60 were below the bounds.
- **L663.** "any claim about C₇ beyond Dyadic's published values".
- **L771.** "the B1-L2 ceiling C₇ ≤ 85.1, would lower it", in `K_ε`'s *Not supplied* list. The ceiling is now registered; using it is new science, not maintenance (co-owner review §6, row K_ε).

**The certificate's control NC2** refuses any ceiling below "published + 0.005", using `PUBLISHED = 85.07 / 27.60` (L98). It stays conservative, because 85.075 > 85.0732 and 27.605 > 27.6022. Repointing it at the registered exact bounds is the owners' choice.

## 4. R4 — release tooling that quotes Dyadic text

The stage-1 claim audits check Dyadic text by substring. At `dyad-v6.4.23` they behave as follows:
- `recog_v0_3_23_claim_audit.py` L38 quotes "$C_7=100$ (certificate value $85.07$)" and the 27.60 analogue. Neither string occurs any more, so this check would **fail**.
- `recog_v0_3_25_claim_audit.py` L17 quotes "85.07" and "27.60" separately, and `recog_v0_3_26_claim_audit.py` L23 quotes "0.36915". All three strings still occur at the tag, but only inside Dyadic's two `[COR]` sentences, which name the old displays. These checks would **pass for the wrong reason**.

These scripts belong to past releases and stay as they are. The v0.3.27 audit should quote the new rows:
- `DYAD-THM-LPHASE-ROWA-BRIDGE`: "c'_Q=0.36916";
- `DYAD-THM-NF-REM-C7-SHARP`: "C_7=85.1" and "C_7=27.7".

On the RECOG side, the negative controls that match RECOG's own `[assuming:]` text need updating together with that text. Two examples: `check_recog_v0_3_26_stage1.py` L376 (NC23, which quotes c′_Q = 0.36915) and `check_recog_v0_3_25_stage1.py` L378 (NC22, the C₇ rows).

`recog_b1_stageA_r9_budget.py` uses 85.07 / 27.60 as "certificate values" (L13, L62). These lie slightly below the exact bounds. Stage A is a budget analysis cited in records, not a proof input, so no change is needed; a wording note is optional.

## 5. R5 — OFN v0.11 notice

OFN v0.11 fulfils REQ-O09-02, reads the RECOG imports at `recog-v0.3.26`, and records the A1c witnesses as reference only. Nothing is asked.

RECOG imports OFN §6.2a ("Minimal Constraint List for T") and §7.3 ("Antipodal Band and Width Parameter") at v0.10. At `ofn-v0.12` both sections still exist. Their only changes are OFN's own import pins: RECOG v0.3.20 → v0.3.26 in §6.2a, and TDR-G v2.12.13 → v2.12.14 with RIDs filled in §7.3.

The rows RECOG cites are unchanged in content. **Proposal:** accept as receipt, and move the OFN companion pin if the edition repins.

## 6. R6 — pins and RID currency

| Source | RECOG pin | Current tag | Cited RIDs and content at the current tag | Atlas proposal |
|---|---|---|---|---|
| Dyadic | `dyad-v6.4.22` (8 ×), header L9, §7 note L1137 | `dyad-v6.4.23` | 27 of 27 cited RIDs resolve. For each, the RID line itself is unchanged; the only differences are new lines that mention the RID (consumer rows) and the corrected displays in the NF-REM table and the L-PHASE proof sketch. | repin where R1–R3 change a use; add the two v6.4.23 RIDs to §7 |
| NUMGEN | `numgen-v1.20.8` (7 ×) | `numgen-v1.21` | all 11 cited RIDs resolve; the claim-difference audit is already done (co-owner review §3) | the planned citation micro-edit, including Lemma 3 by `NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO` |
| Genesis | v2.8.9 | `gen-v2.10` | `GEN-DEF-PRIMITIVE-METRIC` and `GEN-THM-PRIMITIVE-METRIC-INVARIANCE` resolve; the §6.6 lines RECOG cites (I_ab, ω_ab, J_Q, the v2.7.3 index-order convention) are text-identical | companion pin only |
| OFN | v0.10 | `ofn-v0.12` | §5 above | companion pin only |
| RRF | `rrf-v0.8.4` | `rrf-v0.8.4` | — | none |
| TDR-G | v2.12.13 (reference only) | `tdrg-v2.12.14` | no import | optional |

"Resolve" means the RID occurs at the tag. In the RID count, the fragment `DYAD-RADIAL` is the tail of `NUMGEN-N1C-DYAD-RADIAL` and is not counted as a Dyadic RID.

The RECOG-side items in other inboxes are outside this round: RECOG's own notices of 29 October in `pipes/NUMGEN`, `pipes/RER` and `pipes/RRF` are still open with their receivers.

## 7. What this advisory does not do

- It does not edit RECOG text, scripts or outputs, and it changes no pipe state.
- It does not decide R2. Whether the qualifier drops, narrows or stays is RECOG's decision, after its own rerun.
- It does not re-prove any certificate. The rerun replays owner code at one changed input.
- It does not assess the RECOG research frontier (co-owner review §6). The C₇-SHARP lever for `K_ε` is mentioned only because its wording goes stale.
