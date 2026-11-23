# OPEN M (UVM) — S0 Source-Custody Audit

**Status:** [SESSION] / NONCANONICAL working record. It checks the originals the PI brought in on 23 November 2026 against the identities recorded in the corpus and proposes dispositions for the triage rows S0-1…S0-5, U8, P-DYAD, P-TRIAD, P-OFN, I-3 and I-4. It edits no DSN, moves no pin, adopts or re-grades no result and changes no pipe state. The PI decides.
**By:** Claude, UVM co-owner (preparer and triage owner).
**Date:** 23 November 2026. `main` `d4f74a967b76ea92ea0cf8104983d4cad25d01ac`. Governing edition: `uvm-v0.7.1`, `dsn/RTG_OPEN_M_DSN.md`, SHA-256 `0a51644de0a15035797ab03945207cf319fd6d7514a04b8cae441d9d6e93f53e`.
**Inputs:** `upload/uvm-originals/` (31 files with `SHA256SUMS.txt`) and `upload/corpus-originals-20261123/` (535 files with `SHA256SUMS.txt` and `_WANTED_LIST.txt`), both merged by the PI into `d4f74a9`.
**Second co-owner:** its session check (relayed by the PI, 23 November 2026) independently computed the SHA-256 of `main`, of `dsn/RTG_OPEN_M_DSN.md` at the tag `uvm-v0.7.1`, of the uploaded v0.7 edition and of v0.7.1 Draft 2; all four agree with §2. It recommended this audit and the scope limits of §5 and §8.

Two kinds of gap are kept apart throughout. A **historical record gap** is something the earlier campaigns did not record. A **delivery gap** is something that existed but has not yet been brought in. A delivery does not repair a historical record gap. The absence of a file is not evidence about the claim it supported.

---

## 1. PI statements of 23 November 2026 (project conversation with this session)

Verbatim: "PR 361 ve 366 yı onaylıyorum / U8 denetimimden geçti / Dosyalar push edildi".

| Statement | What it settles | What it does not settle |
|---|---|---|
| "PR 361 ve 366 yı onaylıyorum" | The decisions quoted in §1 of `UVM_REACTIVATION_TRIAGE.md` (22 November) and §1 of `UVM_OPEN_M6_STAGE1_RESULTS.md` (23 November) are confirmed by the PI. The merges of both branches are commits authored by the PI (`c0f9659`, `bfe0c47`, parents of `d4f74a9`). | A merge is not an adoption (CONVENTIONS). Both records stay [SESSION]. No edition, grade or campaign follows from the confirmation. |
| "U8 denetimimden geçti" | The June 2026 equivariance package R1–R6 passed the PI's audit. Triage question §10.3 is answered. | The date, form and artifact of that audit are not recorded. The June certificate bytes, `uvjet_equivariant_classification.py` and its output, are still absent (delivery gap, §7). The PI's attestation is the evidence for the audit fact: `EV-SRC-REPORTED` (PI). It is not a co-owner reproduction. |
| "Dosyalar push edildi" | The two upload folders are on `main`. | Which wanted files are absent; see §7. |

---

## 2. Identity checks

**2.1 Folder integrity.** `sha256sum -c upload/uvm-originals/SHA256SUMS.txt`: 31/31 OK. The PI's merge log reports the corpus folder's checks OK. The two adoption JSONs present in both folders are byte-identical.

**2.2 Against identities recorded before the upload.**

| File | Recorded where | Recorded SHA-256 | Result |
|---|---|---|---|
| `uvm-v0.7.1:dsn/RTG_OPEN_M_DSN.md` (from the tag) | v0.7.1 adoption JSON, release record, validation | `0a51644d…f53e` | equal (Claude; second co-owner) |
| `RTG_OPEN_M_DSN_v0_7.md` | v0.7.1 header; v0.7 adoption JSON | `fea80656…7540` | equal (Claude; second co-owner) |
| `RTG_OPEN_M_DSN_v0_7_1_DRAFT2.md` | v0.7.1 header; adoption JSON | `ebbf23ea…db95` | equal (Claude; second co-owner) |
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md` | RER v0.2 §7 | `74558119…56b7` | equal (Claude) |
| `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6.md` | RER v0.2 §7 | `c768687c…5b36` | equal (Claude) |
| `RTG_ONTOLOGICAL_FOUNDATIONS_v0_8.md` | RER v0.2 §7 | `56bc991d…a514` | equal (Claude) |
| `corpus-originals-20261123/RTG_GENESIS_GEOMETRY_DSN_v2_8_5.md` | target of the reverse-patch recipe, Claude entry report (PR #357) | `41ed7660…75cf` | equal (Claude) |

**2.3 Hashes cited inside the governance files.** Every 64-hex value in the v0.7 and v0.7.1 governance files was matched against the folder and the tag:

- `0a51644d…` (released v0.7.1) matches the tagged DSN.
- `fea80656…` (released v0.7) and `ebbf23ea…` (v0.7.1 candidate) match uploaded files.
- `4950d54d…` (v0.7 Draft 3.1, the accepted v0.7 candidate) and `81eef954…` (v0.7 Draft 3) are cited but their files are not in either folder. This is a delivery gap for intermediate drafts only. The released bytes they led to are present, so it is non-blocking.

**2.4 Governance content.**
- The v0.7.1 adoption JSON, release record and validation agree with each other: candidate Draft 2, released file `0a51644d…`, `scientific_change_at_release: false`, next priority OPEN-M-6.
- The validation file reports `ALL CHECKS: 30/30 PASS`. That result is recorded in the original file. It was not rerun in this session.
- Descriptive comparison, made by Claude and not one of the validation's checks: `diff` of Draft 2 against the tagged release gives 32 changed lines.
- The v0.7 adoption JSON records adoption delegated by the project owner to the maintaining co-owner (ChatGPT), with candidate Draft 3.1.

---

## 3. Proposed S0 dispositions

| Row | Proposed state | Basis | Remaining |
|---|---|---|---|
| S0-1 | **closed** | four v0.7.1 governance files present; identities as §2.2–2.4; adoption JSON names `0a51644d…` | — |
| S0-2 | **closed** | six v0.7 governance files and both editions present, hashes equal | Draft 3 / Draft 3.1 bytes (§2.3): delivery gap, non-blocking |
| S0-3 | **PARTIAL** | 15 of 18 named scripts and `open_m_3g_mini_protocol.py` present | 3 scripts, the wiring note, every campaign output, ESM packs and growth series: delivery gap (§7). The I-4 data arrived later the same day (§6). Statements whose certificates are present stay `EV-SRC-REPORTED` until a co-owner reruns them under a PI decision |
| S0-4 | **closed for custody** | the original Genesis v2.8.5 file is present with SHA-256 equal to the reconstruction target | the reconstruction recipe stays as the cross-check. The requirement that a separately recorded hash be checked is satisfied by §2.2. PI decision 2 (comparison source) is unchanged |
| S0-5 | **closed for identity**; statement-level comparison in §4 | three editions present, hashes equal | `B` in Dyadic v6.4.10 not located (§4.1) |

---

## 4. Old-side comparisons at statement scope (S0-5)

**4.1 Dyadic v6.4.10 (P-DYAD).** These are the items UVM's §2 and §5 import:

| Item | Location in v6.4.10 | Agreement with UVM's reading |
|---|---|---|
| `τ = 2√3/3` | line 42 | yes |
| `μ = μ_6 = −1/2 − iτ` | lines 468, 582, 596 | yes |
| `J_Q = L⁻¹ i L` | line 594 | yes |
| `λ = e^{iπ/3} = e^{iF_f/2}`, `[ALG, exact]` | lines 64, 78 | yes |
| h-transfer to OPEN-M `[CAND/conditional]` | line 78 | yes |
| "`h_3 = 0`" scoped to the archival return-log object, conjugacy `h_3 ≠ 0` (`[COR v6.4.10]`) | lines 52, 635, 771 | yes (UVM line 74) |
| `h_2 = −(1+i√3)/12 z² − (1/3) z z̄ + (1−i√3)/24 z̄²` | line 635 | yes: the formula used by the OPEN-M-6 stage-1 certificate is identical |
| `B` | not located by text search in v6.4.10 | UNVERIFIED on the old side; the current side was found consistent in the triage |

No changed claim was found. The proposed class for the old side moves from (iv) to (iii).

**4.2 Triadic v1.6 → v1.6.1 (P-TRIAD).**
- **Unchanged.** Line comparison of v1.6 with the `triad-v1.6.1` DSN shows that every line carrying T-6s, T-6t, T-6u, SG-16, SG-17 and CN-01…CN-05 is identical, apart from release metadata. The triage had already recorded T-6s/t/u and SG-17 as identical from v1.6.1 to v1.7. The chain v1.6 → v1.7 is therefore unchanged on the T-6 rows.
- **D3 changes the birth remainder.** Q_c(0)=κ²Q_s³ and u(0)=κ²Q_s² are now written without the earlier unconditional O(Q_s⁴)/O(Q_s³) remainders. The higher-order remainder holds only if the selected child functional preserves it (Genesis GCL-06). The leading child ratio `W(c_0)/W(s_*) = iκQ_s + O(Q_s²)` (v1.6 line 562) is replaced by scoped leading-term statements. The CN-02 summary now reads "subject to GCL-06 remainder typing". The Genesis import moved from v2.8.4 to v2.8.7.
- **Effect on UVM: none found.** UVM line 76 imports CN-02 as the leading ratio `W(c_0^{[3]})/W(s) = iκQ_s`, without a remainder. It already says that full face-phase remainder statements depend on GCL-06. A pin restatement is an editorial (ii) item for the successor edition. Class (iii) for content.

**4.3 OFN v0.8 (P-OFN).** OPA is `[OPEN]` (line 337). UVM appears only in notify, dependency and table lines (384, 389, 614–615, 627). That matches UVM's reference-only use. Class (iii).

---

## 5. I-3 — diagnostic reproduction of `open_m_3g_mini_protocol.py`

**Run.** The command was `python3 -I upload/uvm-originals/open_m_3g_mini_protocol.py`, using the script with SHA-256 `7c519cd6…ae6d` (`SHA256SUMS.txt` of the upload) and running from a scratch directory.
- Output: exit 0, `ALL CHECKS: PASS` (6 checks).
- A second run produced byte-identical output (fixed seed 7).
- Evidence: `evidence/uvm/open-m-3g-mini-repro/{stdout.txt, environment.txt, SHA256SUMS.txt}`.

**What ran.** Two synthetic random geometric graphs with `K_vac = 1`. The first has N_E = 116; the second has a different N and topology, with N_E = 124. On each, the script fits E(s) under uniform dilation without relaxation and with gradient relaxation at fixed scale:
- bare curvature 116.000000 against 116;
- relaxed curvature 115.998 and 123.999 against 116 and 124.

No ESM pack was loaded. The header's suggested sanity check on the real cluster npz was not available.

**Algebra behind it** `[SESSION: ALG]`. This is a co-owner reading, concurred in by the second co-owner. It is not an owner claim block.
- Take E(s,u) = (K_vac/2) Σ_e (z_e(u)+s)².
- On a fixed-scale slice Σ_e z_e(u) = c. Then E(s,u) = E(0,u) + K_vac c s + (N_E K_vac/2) s².
- The minimizer in u does not depend on s, so E_min''(s) = N_E K_vac.
- This holds for this energy on a scale-invariant configuration space with the slice constraint enforced.

**Scope boundary.**
1. The run is `EV-RUN` of the original script on synthetic inputs. It is a diagnostic reproduction. It is not a proof of the general statement, and it is not the prior campaign's output: that output is still a delivery gap.
2. It does not touch the identification `K_vac = g^{(spin2)}`. That identification stays open under RESULT-M-3A, and v0.7.1 §2 line 70 and line 317 already exclude it.
3. The script header claims the result "for ANY topology and frustration". The governing DSN scopes it to "the tested topology class" (lines 70, 285, 317). The DSN scope governs, and this record does not widen it.
4. I-3's registration gap is a historical record gap and stays open: there is no claim block, status, RID, hypotheses list or §8 row. THM-3G's grade and wording are unchanged. Any scoped §6 statement needs owner and PI authorization (triage I-3).

---

## 6. I-4 — `T100` (`nm=2` at line 110, `nm=0` at line 277)

**Status: the two lines are shown to describe different packs. Line 277 is reproduced; line 110 is reproduced by no single pack. Proposed class (i) for line 110. The PI decides.**

**The two lines name different scripts.**
- Line 110 (OPEN-M-2E status) gives `σ_{h,int}=0.252`, `L_{z_h}=0.527`, `nm=2`, graded by `open_m_2e_panel.py`. That script reads an audit pack with `internal_edges`.
- Line 277 (R14) gives `σ_{h,int}=0.252`, `nm=0`, corridor fraction `0.302`, from `open_m_2f_trajectory.py`. That script reads the microstate `…T80_to_T100_gentle`.
- Both scripts count `nm` the same way: edges in three or more faces.

**Data.** The PI supplied the data in two batches on 23 November 2026. Both are placed unchanged on `upload/uvm-i4-microstates` (`7be6e47`, `f358697`) with `SHA256SUMS.txt` (15 files) and `README_UPLOAD.md`.
- Batch 1: the microstates of T89, T90, T91, T92 and T94, plus `T93_to_T102_2e` and `T98_to_T100_2e_ultra`.
- Batch 2: the complete `T80_to_T100_gentle` set — microstate, audit pack (npz and json), grown manifest, growth log and cluster JSONs.

No earlier record gives hashes for these files, so their integrity is checked but their identity against a record is not. The pickled object arrays were disassembled before any `allow_pickle=True` load: they hold only numpy reconstruction calls and two convention strings.

**Runs.** All are in `evidence/uvm/i4-t100-packs/`; each was byte-identical on rerun.
1. The original `open_m_2e_panel.py` (`da9900af…`) on `…T80_to_T100_gentle_auditpack.npz`, output `panel_T80_to_T100_gentle_auditpack.txt`: `σ_{h,int}=0.2521`, `L_{z_h}=0.3425`, `nonmanifold=0`, `dimH=13`, density 1.488. Verdict "2E: not yet" (fails `L_zh>0.5`, the 0.28 floor, density, and `σ_int≥0.8`).
2. The diagnostic re-implementation of the trajectory row on all eight microstates, output `stdout.txt`:

| Pack | nint | corrFrac | `σ_{h,int}` | `L_{z_h}` | nm | dimH | Source of the numbers |
|---|---|---|---|---|---|---|---|
| `T80_to_T100_gentle` | 86 | **0.302** | **0.2521** | 0.343 | **0** | 13 | microstate, trajectory definitions; equal to the panel run on its audit pack (86 internal edges both ways) |
| `T98_to_T100_2e_ultra` | 105 | 0.267 | 0.2949 | **0.527** | **2** | 10 | microstate only; its audit pack is not supplied |

**Findings.**
1. **Line 277 is reproduced exactly** by the `gentle` pack: `σ_{h,int}=0.252`, `nm=0`, corridor fraction `0.302`. The original panel script on the same pack's audit pack gives the same `σ_{h,int}` and `nm`.
2. **Line 110 is not reproduced by any single supplied pack.**
   - The `gentle` pack, under the original panel, has line 110's `σ_{h,int}=0.252` but `L_{z_h}=0.343` (not 0.527) and `nm=0` (not 2).
   - The `ultra` T98→T100 pack has line 110's `L_{z_h}=0.527` and `nm=2` but `σ_{h,int}=0.295`. Its internal-edge set here is the trajectory rule (inc ≥ 2), not an audit pack's `internal_edges`.
   - **Reading [SESSION], not established:** line 110 combines `σ_{h,int}` of the `gentle` pack with `L_{z_h}` and `nm` of the `ultra` pack. Confirming it would need the `ultra` audit pack or the original panel printout.
3. **The triage acceptance criterion is met** in its second form: the two lines describe different packs. Line 277 is `gentle`; line 110 is not `gentle`, because two of its three values differ under the original panel.
4. **Not changed by this:**
   - The surrounding conclusions of line 110 ("near-pass … but no clean A-candidate"): the `gentle` pack fails three binding criteria, and the `ultra` pack has `nm=2`.
   - R14's statement that clean high-loading stages exist (`gentle`: `nm=0`, `σ_{h,int}=0.252`).
5. **Growth log.** `…_growth_log.csv` shows `nm` rising to 7 at growth step 100. The final cluster after `swap_polish` has `nonmanifold=0` (manifest, cluster JSON, audit pack). Line 277's `nm=0` refers to the final pack.
6. **R14 correlations** (+0.654, +0.326, +0.488) are still not rerun: 6 of the 9 `SERIES` stages are present (T80, T93 and T120 missing), and the script requires at least 7 rows.

**Proposed owner action** for the successor edition, PI decision:
- Line 110: class (i), numerical attribution. Restate the T100 near-pass values per pack, for example `T100 gentle: σ_{h,int}=0.252, L_{z_h}=0.343, nm=0`, and give the `ultra` values only with their source typed. Alternatively mark the triple `[UNVERIFIED: values not reproduced by a single pack]`.
- Line 277: unchanged. Its T100 entry can cite the reproduction.
- No value is changed by this record.

---

## 7. Still missing (delivery gaps)

Listed by the PI's `_WANTED_LIST.txt` with tag UVM and not found:
- `uvjet_equivariant_classification.py` (June R1–R6 certificate, see U8)
- `esm_harmonic_report.py`
- `t103_defect_carrier_test.py`
- `EDIT_A_wiring_instructions.txt`

Data, not found:
- the original printed OPEN-M-2E panel output and T80→T120 trajectory output (I-4; no longer needed for line 277);
- the microstates `…mid40_to_T80_minref`, `…T80_to_T93_2e_loadtest` and `…v13_loose_T80_to_T120` (R14 correlations), and the `T98_to_T100_2e_ultra` audit pack (line 110). The T100 `gentle` set and five other trajectory microstates were received on 23 November (§6);
- the prior output of `open_m_3g_mini_protocol.py` (I-3);
- the ESM packs for RUN05, RUN10, RUN11, T100, T103.

Intermediate drafts: the v0.7 Draft 3 and Draft 3.1 bytes (§2.3).

---

## 8. Non-claims

This record does not:
- adopt, re-grade or re-scope any UVM statement;
- treat a passing script as a theorem;
- treat the PI's confirmations or merges as an edition decision;
- rerun the v0.7.1 validation or any campaign. The I-3 diagnostic of §5 and the I-4 runs of §6 (the original panel script on one audit pack, and the diagnostic on eight microstates) are the only executions;
- change a pipe state.

The triage rows it touches are updated in `UVM_REACTIVATION_TRIAGE.md` revision 4, which cites this record.
