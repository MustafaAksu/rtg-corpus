# RECOG v0.3.27 — Release record (DRAFT; stage 1 round 2 after review; not adopted)

**Study:** RECOG · **Base (governing edition):** `recog-v0.3.26`, DSN SHA-256 `45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34` (349,982 bytes; tag object `1ad76914…`, merge commit `2c076a75…`).
**Stage-1 intermediate:** `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` on `claude/recog-v0.3.27-stage1`, SHA-256 `c8e30dafce1b535ebe3b258b243920401fe99a1d8ce785b0402de7576b7cf0bb` (363,572 bytes), groups R1, D5B, C7, DISP, PIN (76 logged edits; round 2, §2a). Round 1 (commit `e451877`): `63acd5fff83cb116115f6eab0688372f9ebf6792bc43191b50274d8319a21df3` (363,073 bytes), reviewed in #5764962040. A build stage, not an edition: header identity lines, status summary and footer are untouched; the Appendix A entry is a DRAFT line.
**Date:** 4 November 2026 · **Builder:** RECOG co-owner (Claude). **Method:** DSN Methodology v1.4 (§3.6 `[COR]` inline; §13.1, §13.6, §13.7); CONVENTIONS.md §4, §7, §8.
**Decision basis:** the RECOG inbox round after v0.3.26 — `pipes/RECOG/20261030-DYAD-v6-4-23-adopted.md`, `pipes/RECOG/20261030-OFN-v0-11-adopted.md`, the two NUMGEN items of 26 Oct (dispositioned 29 Oct); Atlas advisory and owner entry note (PR #168); independent co-owner dispositions (ChatGPT PR #169, Claude PR #170); two-co-owner reconciliation of 3 Nov 2026 (ChatGPT proposal PR #172, Claude reply PR #173, ChatGPT acceptance record `records/recog/RECOG_OWNER_RECONCILIATION_INBOX_20261103_CHATGPT_ACCEPTANCE.md`, commit `efdf2304d903a843ab666d5393386b0bade7d20b`). The reconciliation is complete at the two-co-owner level for R1–R6 and item 7; **it is not a canonical adoption**: each group below needs the PI's separate scientific decision.

## 1. Groups and their acceptance decisions

| Group | Content | Reconciled disposition | Requires | Decision |
|---|---|---|---|---|
| R1 | $c'_Q=0.36916$ (DYAD-THM-LPHASE-ROWA-BRIDGE): part-1b literal changed (L55 only), the eight A1c certificates and the corrected grid rerun by the owner, four §8 rows re-registered | accept (owner rerun required) | exactly one of D5B / D5A (the five text sites carry the value through them) | **pending (PI)** |
| D5B | R2 option (b): new RECOG-ALG-A1C-JET-REMAINDER-BOUNDS `[ALG]` + RECOG-ART-A1C-JET-REMAINDER-BOUNDS; DYAD-THM-LPHASE-ROWA-BRIDGE and DYAD-THM-OPEN3-SPIRAL-REM imported; the (D5) `[assuming:]` removed at the six A1c sites, §1, §2 R6 decoder line; §7 rows | accept, conditionally (independent lemma; depends only on DYAD-ALG-NF6, DYAD-THM-NF-REM and $q\le q^*$; no cycle; outward ceilings); claim-specific review #5764962040: ACCEPT (§2a) | R1 | **pending (PI)** — D5A remains the fallback only if the PI does not accept the lemma |
| D5A | R2 fallback (a): the same imports, the `[assuming:]` narrowed to $c_J=0.50220$, $c_7=157.58$ | fallback | R1; exclusive with D5B | built as variant only |
| C7 | R3: RECOG-THM-R9-SHARPENED-ROWS-C7 imports DYAD-THM-NF-REM-C7-SHARP (same ceilings $85.1/27.7$); stale wording; §7 rows | accept with change (C7-SHARP only; $C_D$ untouched); review: ACCEPT | — | **pending (PI)** |
| DISP | item 7: eight displays printed in the safe direction with `[COR]` at the point of use | accept with change; review: ACCEPT | — | **pending (PI)** |
| PIN | R4–R6 (+R5 receipt): current-use pins to `dyad-v6.4.23` / `numgen-v1.21`, delimiter-anchored claim audit, GAP-LOCK Lemma 3 by RID with two consumption grades, companion pins, historical pins kept | accept / accept with change; review: ACCEPT WITH CHANGE (OPEN R5 export line, applied in round 2) | — | **pending (PI)** |

No existing result is strengthened and no grade changes. The source conditions change only where stated: under D5B the (D5) `[assuming:]` of the six A1c sites is discharged by imported owner theorem rows (DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM) and the new RECOG-ALG-A1C-JET-REMAINDER-BOUNDS; under C7 the $C_7$ `[assuming:]` of RECOG-THM-R9-SHARPENED-ROWS-C7 is replaced by the imported DYAD-THM-NF-REM-C7-SHARP (same ceilings). No OPEN status word changes (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED); A1c-Q1′ stays `[OPEN]`; Appendix B is byte-identical (no claim is withdrawn: every changed display was a display, never a script input).

## 2. Build

- Builder `evidence/recog/scripts/build_recog_v0_3_27_stage1.py` (sha256 `3cb42e81591f50069ec6a7a44ce1a8d53c33531a8d805fcc4b151e4cd0c46791`), base = `git show recog-v0.3.26:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`, run from the repository root (R1 reads the regenerated hashes from the working tree). Edit log `evidence/recog/v0.3.27/stage1_edit_log.json` (old / new text and hashes of every edit). Modes `str` / `line` / `sub` (exact-count substitutions in one line found by a unique prefix) / `s8` (quoted hashes of changed files replaced in the named §8 row, the row marked `[v0.3.27]`); every edit exact-once; Appendix A masked for live edits.
- Variants (`evidence/recog/v0.3.27/variants/`): `only_R1_D5B.md` R1+D5B `eb3dce01…b968`; `only_R1_D5A.md` R1+D5A (fallback for R2) `f0f029c5…38e9`; `only_C7.md` C7 `fd43c112…87a6`; `only_DISP.md` DISP `3763980c…b463`; `only_PIN.md` PIN `6198662d…fb13`; each passes the checker (`only_*_check.txt`).
- Refused by the builder: R1 alone, D5B alone, D5A alone, D5B+D5A.

### 2.1 R1 — owner rerun (4 Nov 2026, RECOG co-owner, this workspace)

`evidence/recog/scripts/recog_a1c_tail_averaging_cert.py` line 55 only: `I("0.36915")` → `I("0.36916")` (sha256 `c731cf1b7105bf70d4e5ce4f1d993f5009bbeb0cdcc9c82144dde7ddc93dff24`; equals the patched script of the Atlas RA1 recheck and of the co-owner's reconciliation rerun). The docstring (lines 10–17) still says $c'_Q=0.36915$, cites Dyadic v6.4.22 and describes (D5) as proof constants; it is a now-inaccurate description, not executed code. **Deferred to the next bulk maintenance** (review #5764962040): changing it would change the script's hash and its §8 row without any change of output, so it is aligned together with the other docstring pins in one later package. Commands (from `evidence/recog/<dir>`, `python -I ../scripts/<script>.py <json> [args]`, stdout to `<json-stem>_output.txt`), all rc = 0:

| directory | script | args | time | JSON sha256 (new) | JSON at `recog-v0.3.26` | output.txt |
|---|---|---|---|---|---|---|
| `a1c_1b` | `recog_a1c_tail_averaging_cert.py` | 6000000 | 62 s | `d7bbe537…5995` | `deb1d039…b32e` | `9afec446…d1bf` (was `a8e3a5b4…b9ef`) |
| `a1c_so` | `recog_a1c_start_offset_cert.py` | — | 134 s | `deaf180d…bf50` | `6a16f295…eff4` | `35c37c22…4762` (was `d0db0bcc…9c1e`) |
| `a1c_2` | `recog_a1c_unknown_a_interval_cert.py` | — | 162 s | `dfbd8619…c244` | `73720b80…2bfe` | unchanged |
| `a1c_inblock` | `recog_a1c_inblock_angular_cert.py` | — | 96 s | `89d9beff…b3d4` | `c0b7e7df…4724` | `88c37eb0…140a` (was `efe95017…2951`) |
| `a1c_comb` | `recog_a1c_combined_tail_cert.py` | — | 134 s | `0d0b4e5c…a894` | `1948acab…57a0` | unchanged |
| `a1c_joint` | `recog_a1c_joint_transfer_cert.py` | — | 1594 s | `efa66a4a…412b` | `b5f28e5f…e8eb` | unchanged |
| `a1c_drift` | `recog_a1c_drift_centering_cert.py` | — | 209 s | `bbd3caa7…6b7a` | `cbf0e806…fc80` | unchanged |
| `a1c_drift` | `recog_a1c_drift_proof_table_cert.py` | — | 568 s | `64f7cb69…8635` | `e7c4731e…063f` | unchanged |
| `v0.3.26` | `recog_v0_3_26_corrected_grid.py` | — | 88 s | `7e464519…af06` | `569b018e…e141` | (stdout to the session scratch log) |

Every certificate reports ALL_PASS; the corrected grid reports `all_below: true`. The five JSONs common with the Atlas RA1 recheck / the co-owner's reconciliation rerun are byte-identical to them (part 1b `d7bbe537…`, start offset `deaf180d…`, unknown-$a$ `dfbd8619…`, in-block `89d9beff…`, combined tail `0d0b4e5c…`; the joint transfer `efa66a4a…`, drift `bbd3caa7…`, proof table `64f7cb69…` and corrected grid `7e464519…` equal the co-owner's own patched session runs). No printed decimal of the DSN changes from R1 except $\beta(625)$: $0.7992976\ldots\to0.7993089\ldots$ ($+(0.36916-0.36915)\cdot\tfrac{256}{225}=1.1378\times10^{-5}$), printed $\le0.800$ under DISP (the alternative $0.7993$ is rejected: it lies below the R1 value).

### 2.2 D5B — the jet-remainder lemma

`evidence/recog/scripts/recog_a1c_jet_remainder_bounds_cert.py` (sha256 `0fa7bb4d4179774b2a1a6b9d8472cf3c7e93f45727c6174c3914657f63f1c0f1`) → `evidence/recog/a1c_jet/` (`62854819…b7ae`, `875dea82…68dc`): G1 exact rationals (sufficient enclosures of $\sqrt3$, $|\mu|$, $|a_{32}|$, $|a_{05}|$ by squared comparisons, from `evidence/recog/inbox_reconciliation_20261103/recog_r2_rational_bounds.py`, PR #172): $c_J(q^*)<0.5008182254<0.500819<0.50220$, $100.2300186<c_7(q^*)<100.2301467<100.231<157.58$; G2 interval enclosure inside the rational bounds; G3 monotonicity in $q$ on a grid; G4 the identity $\operatorname{Im}a_{32}-\tfrac12\operatorname{Im}\mu^2=\tfrac{89\sqrt3}{324}$ (sympy); NC1 the display $100.23$ refused; NC2 the wrong-sign identity exceeds $0.50220$; ALL PASS.
**Dependency (for the claim-specific review):** the lemma uses only DYAD-ALG-NF6 ($\mu$, $a_{32}$, $a_{05}$; the jet $J$) and DYAD-THM-NF-REM ($C_7=100$ on $|z|\le\tfrac1{20}$) and $q\le q^*=\tfrac{256}{140625}<\tfrac1{400}$. It uses no RECOG A1c result and no Dyadic LPHASE statement; its majorants are the ones computed for RECOG-ALG-A1C-COMBINED-TAIL in v0.3.25, now stated source-independently, and COMBINED-TAIL cites the lemma (one direction; no cycle). The proof outline of DYAD-THM-LPHASE-ROWA-REMAINDER's constants $c_J=0.50220$, $c_7=157.58$ stay what part-1b uses; the lemma shows they are valid ceilings on RECOG's domain.

## 2a. Round 2 — review #5764962040 on `e451877` (ChatGPT co-owner, change-focused: `COMMENTED — ACCEPT WITH TWO SCOPED DOCUMENTATION EDITS`, no scientific blocker)

Review result (reviewer verdict, not PI adoption): D5B ACCEPT (proof and dependency separation valid: the lemma rests only on DYAD-ALG-NF6 and DYAD-THM-NF-REM, not on TAIL-HARMONICS or COMBINED-TAIL; exact comparisons $c_J(q^*)<0.500818226<0.500819<0.50220$, $c_7(q^*)<100.230147<100.231<157.58$); R1 identity confirmed (9/9 JSON hashes recomputed independently, 57/57 gates pass in the eight A1c certificates, no boolean changed between the old and new JSONs, corrected grid `all_below = true`, intermediate hash matches; the heavy orbit runs not repeated by the reviewer — output identity and the owner run's scientific validity kept apart); C7 ACCEPT; DISP ACCEPT; PIN ACCEPT WITH CHANGE; no Appendix B entry needed; no further computation requested. Applied in round 2:
- **OPEN R5 `Exports to:`** now cites `RTG_ONTOLOGICAL_FOUNDATIONS v0.12 §6.2a` (`ofn-v0.12`; the same constraint rows; OFN imports RECOG-ALG-SHEAR-COCYCLE-CLASSIFICATION and RECOG-ALG-SHEAR-WEIGHT-IDENTIFICATION at v0.3.26 §6.6a; checked against `ofn-v0.12` §6.2a), keeping the previous citation v0.10 (PIN edit PIN-EXP; checker C27 now counts the line, control NC21).
- **Scope sentence narrowed** (§1 above and the Appendix A DRAFT entry): results and grades unchanged; the source conditions of D5B and C7 are replaced by owner theorem rows or the new RECOG lemma.
- **Part-1b docstring:** deferred to the next bulk maintenance, recorded in §2.1.
No certificate rerun; no other text changed.

## 3. Checks

### 3.1 Checker `evidence/recog/scripts/check_recog_v0_3_27_stage1.py` (sha256 `59008abf1e84065b6f809501eccf05d48fee69d1a2811509624452bec2149c0d`)

Gates C0–C28 (C0–C24 as v0.3.26, adapted; C25 Appendix B byte-identical; C26 DIRECTION; C27 PINS; C28 C7 ROWS): all PASS on the full intermediate (C27 and C28 apply to the PIN and C7 builds). Negative controls (`--controls`): 30 controls, each caught by its target gate (NC01–NC21 structural, value and pin controls, including a failing rerun JSON for C19, a lowered jet ceiling, a dropped bridge import, restored (D5) and $C_7$ qualifiers, altered regenerated and new §8 hashes, stale Dyadic and NUMGEN pins, the OPEN R5 export line left at OFN v0.10 and the miscopied hash abbreviation); one control for each old display of item 7 (eight, plus the rejected $0.7993$), each caught by C26. Output: `evidence/recog/v0.3.27/stage1_check_output.txt`.
C26 is direction-aware: each displayed ceiling $\ge$ its certified value, each displayed window $\le$ its certified window, over 22 displays with a JSON counterpart (the v0.3.26 C19 used a symmetric tolerance and could not see direction). The B1 window: $q_0<|G|/75.69$ with $|G|=\sqrt{481897}/90720$, certified $1.0109637\ldots\times10^{-4}$; printed $1.010\times10^{-4}$; the theorem's formula and its $C_2$ row are unchanged.

### 3.2 Claim audit `evidence/recog/scripts/recog_v0_3_27_claim_audit.py` (sha256 `9f0a4d663f123b1ff989eda8afc12a46d6f4ccad5d1173cca53dcef3e7652d73`) → `evidence/recog/v0.3.27/claim_audit.json`

At `dyad-v6.4.23` (`9f874ccc…25cb`) and `numgen-v1.21` (`4805760d…5701`): the 31 rows of the v0.3.23 audit (read from the frozen script, not modified) with NF-REM and GAP-LOCK Lemma 3 rewritten for the owner's current text, plus LPHASE-BRIDGE, LPHASE-OUTLINE ($c_J$, $c_7$), SPIRAL-REM, C7-SHARP, NF6-JET — 39 rows. **Delimiter-anchored** (R4): a quoted string counts only inside the cited entry (anchor line to the next RID entry or heading; five rows whose v0.3.23 context strings sit elsewhere use the enclosing section or the file, as recorded per row) and only where not continued by a digit, so `85.07` is not found inside `85.0732`. Direction checks: $c_Q=0.79246\ge0.7924576152$, $c'_Q=0.36916\ge0.3691523046$, $C_7=85.1\ge85.0731933471$, $27.7\ge27.6022209836$. Negative controls: NC1 the v0.3.23 NF-REM needle (`certificate value $85.07$`) not found; NC2 `0.36915` found as a plain substring of the bridge entry but not delimiter-anchored; NC3 direction refuses $0.36915$; NC4 direction refuses the window display $1.011\times10^{-4}$. ALL PASS. EV-SRC-READ only: no comparison with earlier pinned editions, no owner certificate rerun.
**Claim-specific review for D5B** (reconciliation condition): done in review #5764962040 (§2a) — ACCEPT; the removal of (D5) still takes effect only with the PI's adoption of D5B.

### 3.3 Further checks

- Companion pins (PIN): Genesis `gen-v2.10` — the two RID declaration lines GEN-DEF-PRIMITIVE-METRIC and GEN-THM-PRIMITIVE-METRIC-INVARIANCE are byte-identical to `gen-v2.8.9`; OFN `ofn-v0.12` — the imported statements of §6.2a and §7.3 unchanged, OFN's own import pins and TDR-G RIDs updated and one owner note added in §7.3 (OFN08-C12 fulfilled at `tdrg-v2.12.14`).
- Finding (PIN): the abbreviation `835a56f8…7e2f` used for the NUMGEN v1.20.8 hash at two places of v0.3.26 (§7 sync paragraph and the NUMGEN-DEF-N5AS1-DEFECT row) was miscopied — the hash `835a56f82b26…f4817e` ends `…817e`. The sync paragraph now gives v1.21's hash; the row records the miscopy. A display defect only; the v0.3.23 audit asserted the full hash.
- OPEN R5 `Exports to:` line: repinned to OFN v0.12 §6.2a in round 2 (§2a). The consumer inventory ("Owner editions that consume RECOG RIDs", as inspected v0.3.23) is a historical audit line and is kept. A consumer re-inspection would be a separate maintenance item.

## 4. Notices

None prepared in this stage. After a PI adoption: notices to DYAD (registrations consumed: LPHASE-ROWA-BRIDGE, OPEN3-SPIRAL-REM, NF-REM-C7-SHARP; RECOG-side bounds for $c_J$, $c_7$ if D5B), NUMGEN (GAP-LOCK Lemma 3 cited by RID with two grades; v1.21 repin), OFN (v0.11 notice received; receipt), ATLAS; the four inbox items closed with their disposition lines. Filing is a queue event; no notice state is asserted.

## 5. Stage 2

None (no compaction).

## 6. Reviews and adoption

Review: #5764962040 on `e451877` (ChatGPT co-owner) — ACCEPT WITH TWO SCOPED DOCUMENTATION EDITS; both applied in round 2 (§2a). Receiving read-back: #5765657572 on `2f896d4` (ChatGPT co-owner, 4 Nov 2026) — **ACCEPT; no remaining blocking request**: the OPEN R5 repin, the narrowed scope sentence and the docstring deferral confirmed; NC21 rejects the old OFN v0.10 use-citation; no certificate or JSON output changed in round 2; candidate SHA-256 `c8e30daf…f0bb` recomputed independently and matching (DSN and intermediate copy), edit log 76/76, builder and checker hashes matching. Co-owner recommendation to the PI, per group: R1 ACCEPT, D5B ACCEPT (discharge (D5) by the new lemma; no return to D5A), C7 ACCEPT, DISP ACCEPT, PIN ACCEPT. The deferred part-1b docstring is recorded non-blocking maintenance debt. These are reviewer verdicts, not adoption. **Next: the PI's separate decisions per group (§1).** After adoption: `release_recog_v0_3_27.py` with the decision date, a review number and the PI's scope clause (eight metadata edits), `BASELINE.md` row, the adoption section of this record, then the PI's merge commit and annotated tag `recog-v0.3.27`. Publication: `evidence/recog/scripts/release_recog_v0_3_27.py` (eight metadata edits; candidate hash `c8e30daf…f0bb` set in the script; `--preview` only until the decision).

## 7. Records and evidence of this release

`evidence/recog/v0.3.27/` (edit log, intermediate copy `stage1_intermediate.md`, check output, claim audit, variants); `evidence/recog/a1c_jet/`; the regenerated A1c outputs in `evidence/recog/a1c_1b|a1c_so|a1c_2|a1c_inblock|a1c_comb|a1c_joint|a1c_drift/` and `evidence/recog/v0.3.26/corrected_grid.json`.
