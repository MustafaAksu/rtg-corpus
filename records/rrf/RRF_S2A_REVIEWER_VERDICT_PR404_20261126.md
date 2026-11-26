# RRF v0.9 S2a — reviewer verdict on PR #404

**Date:** 26 November 2026.
**Status:** [SESSION] / NONCANONICAL. Reviewer lane (Claude, independent reviewer / second co-owner). Content/scope review of a DRAFT intermediate. It authorizes no freeze, S2b, merge, adoption or release; the PI decides.
**Reviewed:** PR #404 `chatgpt/rrf-v0-9-s2a`, exact head `6a7b27de16d60d5824aaebef8af8de82ee5c577d`, merge base `02ed0ba9`. Intermediate `dsn/RTG_RRF_REPRESENTATION_REGISTRY.md`: 124,197 bytes, SHA-256 `9f162a7fb4c5f32e899a147edea43dbed0410a1db1c80aa629ac6ddcde8f89f9`. Base: `rrf-v0.8.4` (`2fb0a0fe…`).
**Criteria:** the build record's A1–A3, against the accepted S1 matrix (#400 at `2c087763`). Changed statements were compared with owner text at the S1 governing tags. The Atlas was not used and no owner certificate was rerun.

## Verdict

**ACCEPT WITH CHANGES.**
- **A1 (replay):** met.
- **A2 (row-by-row content):** met for every S1 row. No owner statement, grade, domain, chart, clock or numerical value is misrepresented.
- **A3 (preservation and identifiers):** two changes are required before the intermediate is frozen for S2b — C1 (three dropped pointers) and C2 (OPEN identifier format).

## 1. Checks performed

| Check | Result |
|---|---|
| Native builder `python -I evidence/rrf/scripts/build_rrf_s2a.py` | exit 0. Three negative controls pass. `S2A_BUILD_PASS 38 operations 124197 9f162a7f…`, equal to the working-tree file. |
| Changed paths against the merge base | The DSN, the builder, the build plan, the build record and the orientation. The Claude lane is untouched. Pipes: 197/20. |
| `tools/dsn_lint.py --prev` (informational) | +15,582 bytes (+14.3 %). 29 new identifier strings, which are the owner RIDs newly cited plus 10 proposed RRF IDs. |
| Owner RIDs removed | none |
| Owner RIDs newly cited | 17. Each exists in its owner DSN at the governing tag. |
| Profiles | the five profile headings are unchanged |
| Preservation of identifiers, guards and evidence filenames: `evidence/rrf/scripts/rrf_s2a_preservation_check.py` (new; has a negative control) | **3 tokens lost** (see C1). The header predecessor filename change is allowed. Output: `evidence/rrf/v0.9/s2a_preservation_pr404_6a7b27de.txt`. |

**Point-of-use owner comparisons — all agree:**
- **D1:** winding k≥1; DYAD-ALG-NOT-AREA-PRESERVING.
- **D2/D3:** 15/16–17/16 bounds; C_D = 1000/250; C7-SHARP kept separate.
- **D5/D6:** E2 restricted to `DX'(0)=0`; `G_∞^{-n}F^n` construction, with `F^{-n}R_∞F^n` retained as unproved; smooth chart with qualitative radius.
- **D7:** K₀ rows; T1/T2 conditionality.
- **R2/R3:** baseline and sharpened rows not mixed.
- **R5:** the F4 tag changes from `[OPEN]` to `[RESULT] [from: DEF]`, which matches RECOG L1134, while the missing interface stays RRF `[OPEN]`.
- **O1:** Standard C matches OFN §5.5.2 L449–451, including "algebraic cancellation …".
- **O3:** Q3b matches L444; the κ table matches L480.
- **O2/O4:** SESSION grades are kept as required by S1 C2/C3.
- **G1:** H-JET, H_spec, H_prim and the non-implication match GEN L855/L891.
- **G2:** GEN-THM-SOURCED-JUNCTION with σ_f≠0.
- **T1:** `[OPEN]`.
- **N1–N3:** values and HOLD reason.
- **E1:** RER L23 K6/K8.
- **U1/P1:** reference-only.
- **BQ:** no BR-Q2 content.

## 2. Required changes

**C1 — restore dropped pointers.**

*Basis:* CONVENTIONS §3 ("never remove … an evidence pointer") and the build record's own statement that frozen history is kept for S2b. Rewriting the v0.8.4 §0.2 "current source receipts" table and the §2.4a evidence sentence dropped three tokens that occur nowhere else in the file:
- **`RF-O09-03`** (with `/04`, §4.5, OPEN-OPA): the OFN v0.9 reference keys behind the guard "no universal node-coincidence axiom, carrier selection or physical clock derived".
- **`SG-15`**: the "Triadic §6.15/SG-15" receipt in the Genesis v2.8.5 / Triadic v1.6 row. TRIAD v1.7 still carries SG-15 (L257, L576), and the old v0.7 Wrap-up sync obligation refers to it.
- **`DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip`**: the evidence archive name in §2.4a. This archive is no longer missing. It is in `upload/dyad-sources/DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip`, 121,396 bytes, SHA-256 `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4`. Cite it by path and full hash with EV-NOT-RERUN, rather than as an unnamed "P2-B v2 evidence".

*Fix:* keep the replaced v0.8.4 §0.2 rows verbatim under a labelled "historical receipts (S2b relocation)" block, or move them into §0.1 or §10, and restore the archive pointer.

*Acceptance:*
- `python -I evidence/rrf/scripts/rrf_s2a_preservation_check.py` exits 0 on the corrected head.
- The builder gains the same preservation assertion, so that "assertion-gated" covers content preservation and not only byte anchors.

**C2 — OPEN identifier format.**

*Basis:* Methodology v1.4 §4.2 gives `[PREFIX]-[CATEGORY]-[SHORT_DESCRIPTION]`, and §5.1 gives `STUDY-OPEN-TARGET`. The proposed `RRF-OPEN-A`, `-B`, `-E1` and `-E2` carry no description.

*Fix:* use descriptive targets, keeping OPEN-A/B/E1/E2 as local aliases under §8.4. For example:
- `RRF-OPEN-POLE-RELABELING` (A)
- `RRF-OPEN-IDENTIFICATION-PRIMITIVE` (B)
- `RRF-OPEN-NETWORK-VARIABLES` (E1)
- `RRF-OPEN-JOINT-NF` (E2)

*PI decision item:* the closure criteria in §7.3 are new normative text with no v0.8.4 equivalent. They are representation-level obligations, not new physics, but their wording is a PI decision, not reviewer acceptance.

*Acceptance:* descriptive IDs plus the alias line, or an explicit PI decision to keep the letter IDs.

The six local candidates (`RRF-DEF-PASSIVE-TRANSPORT`, `RRF-ALG-S-DECOMPOSITION`, `RRF-ALG-FINITE-SWAP-TRANSPORT`, `RRF-DEF-TYPED-COVARIANCE`, `RRF-ALG-ODD-ROOT-EQUIVALENCE`, `RRF-DEF-EVENT-TRANSPORT`) are accepted as proposals. Each matches the grade and scope its home already carries in v0.8.4. Registration remains with PI adoption (§4.4).

## 3. Non-blocking notes (for S2b or the release)

- **N1:** §§7.1–7.3 sit under "# 7. Not registered". In S2b, the OPEN register belongs with the OPEN registry and the consumer register with the import/interface ledger. No content change is involved.
- **N2:** the OPEN entries lack the §5.1 fields `Status`, `Owner study` and `Dependencies` (B precedes E1, which precedes E2). Add these in S2b or at the release, without changing the questions.
- **N3:** the builder's plan replay proves byte reconstruction only. Content assurance comes from this review and the C1 preservation assertion. The build record should say so.

## 4. Gate

The S2a freeze for S2b becomes possible after C1 and C2 are applied (or C2 is decided by the PI) and a readback is done at the corrected head. PR #404 stays unmerged as an intermediate. S2b may start only from the frozen hash. BR-Q2 continues separately; no result of it enters S2a.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## 5. C1/C2 readback — corrected head `98da97c311a917d1539b9c31afaba779bc75a73f`

**Verdict: ACCEPT SCOPED.** The S2a intermediate at this head is acceptable for freeze as S2b input. The proposed OPEN closure wording and the registration of identifiers remain PI_PENDING.

| Check (native, full checkout) | Result |
|---|---|
| `python -I evidence/rrf/scripts/build_rrf_s2a.py` | exit 0. Four negative controls pass (changed base, changed anchor, changed target, removed protected pointer). `PRESERVATION_PASS 89 tokens; lost 0`. `P2B_ARCHIVE_IDENTITY_PASS 121396 e4e2bab0…fdbe4`, an identity check only, not a certificate replay. `S2A_BUILD_PASS 38 operations 131089 390f75e4…9d72`, equal to the working tree. |
| `python -I evidence/rrf/scripts/rrf_s2a_preservation_check.py` | exit 0: 89 tokens, 0 lost. The only allowed change is the header predecessor filename. Script blob `53754974…` is identical to #406. |
| Historical block | rrf-v0.8.4 L69–86 (4,728 characters) occurs verbatim in the candidate, between labelled start and end markers. It is marked as dated evidence and not as a current pin. |
| C1 pointers | `RF-O09-03/04` is restored; OFN v0.13 still carries it (5 occurrences). The OFN v0.9 copy is cited by blob `fefb1549…`, and no `ofn-v0.9` tag exists or is asserted. `SG-15` is restored, and its operative TRIAD v1.7 statement matches L257/L576. The P2-B v2 archive is cited by path and full hash. |
| C2 identifiers | The descriptive targets follow `RRF-OPEN-<TARGET>`, with OPEN-A/B/E1/E2 kept as aliases. The §5.1 fields Status, Owner study and Dependencies are present. Dependencies reproduce the v0.8.4 §6 lock B → E1 → E2 and add no prerequisite. The closure criteria are narrowed to the existing §4.2/§6 questions, marked PI_PENDING, and say that a refusal or obstruction does not close a module by itself. |
| Scope of change since `6a7b27de` | The DSN (historical block plus OPEN register), the builder, the plan, the preservation script, the build record and the orientation shared part. The Claude lane is untouched. Pipes 197/20. `main` `14b46849` + #404 + #406 merge cleanly. |

Remark, non-blocking: the "Owner study: RRF" column covers representation work only, as the register's preamble states. OPEN-B's identification question still also concerns GEN/OFN at the owner-science level.

**Gate:**
- The S2a freeze hash is `390f75e447b7d5a9dcb01810d7eb513e9feef3c157f0de2f2f79afb259b39d72`, pending the PI decision on the closure wording.
- S2b may then start from this hash only: structural migration, history separation and compaction, with no content change.
- #404 stays unmerged as an intermediate.
