# DZT — Reading record of the recovered v0.1–v0.17 chain (evidence only)

**Status:** [SESSION] / NONCANONICAL. Evidence-only reading record; **not** the triage record (`DZT_REACTIVATION_TRIAGE.md`, BOOTSTRAP 2 of the orientation note), not a disposition, not a review verdict.
**Prepared by:** Claude, DZT co-owner session, 17 November 2026 (BOOTSTRAP 1, reading only). PI decision of 17 Nov 2026: prepare this record and the plain-file placement (PR #308) as two separate PRs.
**For:** the second DZT co-owner (ChatGPT), to check every observation against the bytes, and the PI.
**Nothing here selects a variant, raises or lowers a grade, adopts an edition, or disposes of an inbox item.** The governing DZT edition remains `dzt-v0.8`.

**Inputs (as read):**
- `rtg-corpus` `main` at `a7ccaa6` (merge of PR #306); `CONVENTIONS.md`; `records/dzt/DZT_COOWNER_SESSION_ORIENTATION.md`; `pipes/DZT/`; `BASELINE.md`.
- Tags: `dzt-v0.8`, `methodology-v1.4`, `programme-v1.4`, `dyad-v6.4.24`, `az-v0.10`, `ofn-v0.12`, `numgen-v1.21`, `atlas-v0.14` (each file equal to `main`; each with its release record in `BASELINE.md`).
- Recovery: `upload/dzt-recovery-20261116/` (PR #289). Extracted with its reviewed helper on a copy outside the repository (`--extract`: PASS, `ORIGINAL_FILES_EXECUTED=0`). **Paths below are relative to `upload/dzt-recovery-20261116/received/originals/downloads/`** and become readable on GitHub when PR #308 (commit `abac408c476221e4f5a03d08d667b90d0b8fb37d`) is merged.
- NUMGEN audit memo `upload/numgen-records/RTG_NG_PROGRAMME_REVIEW_AUDIT_v1.md` (SHA-256 `45d418b7…c91`).
- LIT record `records/lit/dzt2026/DZT_NORM_LAW_PROOF_NOTE.md` in the private repository `MustafaAksu/rtg-lit` at commit `8e2fb5cb7e39c5c4ab05b3008c4a51d03faed0f3` (unchanged at LIT `main` `6526c4cd` when read); its review on LIT PR #100 (review `5888136234`).

**Companion diffs (generated on demand; Methodology v1.4 §13.7).** The complete `diff -U0` output of every same-numbered variant pair was stored as `records/dzt/DZT_RECOVERY_VARIANT_DIFFS.md` and is no longer on `main`.
- **Identity of the removed file:** SHA-256 `385299fd0d120b22a99f0b77aa30617c866cc72a22c2222b6e73332bbb870494`, 87,609 bytes, git blob `a9b91777f9b7d927463a23274ae81d89f8cfffa9`. It was added by commit `2c22802778d62445eea32fe08a3c463d0bf7afa3` and merged in PR #309 (`b4ebe61c565ec8dcc048e1b5d3e7c62b8d258e5c`). It was removed from `main` by the commit that adds this paragraph, at the PI's authorization of 18 Nov 2026.
- **Exact bytes:** `git show 2c22802778d62445eea32fe08a3c463d0bf7afa3:records/dzt/DZT_RECOVERY_VARIANT_DIFFS.md`.
- **Regeneration:** run the command below on the nine pairs of §4. Each pair exits 1 (files differ). Its hunks equal the stored block byte for byte; this was checked for all nine pairs before removal. Only the two header lines differ, since they carry the file times of the checkout.

```bash
cd upload/dzt-recovery-20261116/received/originals/downloads
R=RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_
for p in "v0_4.md|v0_4 (1).md" "v0_8.md|v0_8 (1).md" "v0_9.md|v0_9 (1).md" "v0_9 (1).md|v0_9 (2).md" \
         "v0_10.md|v0_10 (1).md" "v0_10 (1).md|v0_10 (2).md" "v0_11.md|v0_11 (1).md" "v0_16.md|v0_16 (1).md" "v0_17.md|v0_17 (1).md"; do
  a="$R${p%%|*}"; b="$R${p#*|}"; sha256sum "$a" "$b"; diff -U0 "$a" "$b"
done
```

**No recovered script was executed.** One new session check was run (§9.3); its script and output are reproduced in full below.

---

## 1. Live state at reading (observations)

- `dzt-v0.8` = `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md` on `main`, SHA-256 `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2`. `BASELINE.md` verifies it against the PI's value; there is no DZT release record and no `dzt-v*` tag other than `dzt-v0.8`.
- `pipes/DZT/`: four items, all `open` (DYAD 3 Nov; AZ 11 Nov; AZ 12 Nov; LIT 13 Nov). `tools/pipes_index.py --check`: OK.
- Open PRs touching DZT paths: none (other than #308 and this record). The branches `claude/dzt-entry-note`, `claude/pipes-dzt-lit-norm-law` and `upload/dzt-recovery-20261116` point at commits already merged into `main`.
- AZ v0.9 and v0.10 were adopted after the two AZ items; neither filed a DZT item (their notices went to ATLAS and PROG).

## 2. Inventory of the recovered DZT DSN files

Times are the collection manifest's `observed_last_write_time_utc` (an observation of the collecting machine, not provenance or chronology).

| edition | file | SHA-256 | bytes | observed write (UTC) |
|---|---|---|---|---|
| v0.1 | `…_v0_1.md` | `c7656a7a9e9c5d43d14b6fe41d332f1f8afdb8fe72ece761983e051e0ff6ad99` | 21078 | 2026-06-22 13:18 |
| v0.2 | `…_v0_2.md` | `838f49ea3ec6a60b1c94922e48e2a587b7919ce449849b7957ce2218630090ea` | 26282 | 2026-06-22 13:30 |
| v0.3 | `…_v0_3.md` | `6af8db841f75e86630397c70b2942b4b4b0489ee2f2fc08800707a08422ebe3d` | 27678 | 2026-06-22 13:39 |
| v0.4 | `…_v0_4.md` | `ad797e5d28ac5a4d316b3da618ef44d2760260982d236850713f12d5a2f632c7` | 33151 | 2026-06-23 05:18 |
| v0.4 | `…_v0_4 (1).md` | `806ff90041365404513b34767d9f9ef0d2ea47519ae71089ee43af9bb8ac83e8` | 34605 | 2026-06-23 05:28 |
| v0.5 | `…_v0_5.md` | `d59146da69443cb1901b2e97ad6244582fc5938d5f4f0d30853f11122a0d8fba` | 38055 | 2026-06-23 06:11 |
| v0.6 | — | **absent** | — | — |
| v0.7 | `…_v0_7.md` | `33b3030ce1e3fec5e3c0139788e6ac61461bd2a193671ec3902e41d86ebd3af0` | 45807 | 2026-06-23 09:27 |
| v0.8 | `…_v0_8.md` | `57cbb30e8405ab961fcf2d3ceea1e6275aacd460948f42c6109622189d3cdceb` | 49224 | 2026-06-23 09:35 |
| v0.8 | `…_v0_8 (1).md` (= tag; also `legacy-src/…/DSN/…_v0_8.md`) | `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2` | 50547 | 2026-06-23 09:40 |
| v0.9 | `…_v0_9.md` | `5e2e4462243d2e27934b277d305fb4d5bb218a36729371060ff0651fd5e6224e` | 55539 | 2026-06-23 10:14 |
| v0.9 | `…_v0_9 (1).md` | `bf12113fb050ef3600d21d6e4a5141e8a75c8f574eff8e584104eaa3250448bf` | 54817 | 2026-06-23 10:18 |
| v0.9 | `…_v0_9 (2).md` | `3990c411d4b89c54e1d4556fb361cd8f9d65bff6f393f1fb7548c367e571666e` | 56353 | 2026-06-23 10:34 |
| v0.10 | `…_v0_10.md` | `6942d7cd5e224b7a016ca72fca9bf01a8b1000ab2363122ddd9b2522df9e285a` | 60338 | 2026-06-23 12:47 |
| v0.10 | `…_v0_10 (1).md` | `a70c6522145bbb714a240db020b8b048b2fa275f615540ffcf0254a58174b400` | 61869 | 2026-06-23 13:44 |
| v0.10 | `…_v0_10 (2).md` | `70a529d9eb38d00f76575634ef88ce56f579e23309597731849ff2fcc2331a75` | 62520 | 2026-06-24 05:46 |
| v0.11 | `…_v0_11.md` | `ec75d6c9095adb38c29bc6f68fd97247d29bd5259cdbcf97c2625bf675b0b366` | 67128 | 2026-06-24 05:59 |
| v0.11 | `…_v0_11 (1).md` | `0c5addf779bd5c1503e89a39007672281d2a56a23e18aef483ec0877a41767e6` | 67759 | 2026-06-24 06:27 |
| v0.12 | `…_v0_12.md` | `032bf581fd424f03dffc9fc9c2825ba7ed0b4af441c47fc88b37e09d8080d2b2` | 71924 | 2026-06-24 07:21 |
| v0.13 | `…_v0_13.md` | `1392acb37d75f34137ffcbfcd5b05898f353ab4f693aeacce7deb66e0b1cbe02` | 75267 | 2026-06-24 07:29 |
| v0.14 | `…_v0_14.md` | `b3b56875868be5f2ee3c6b1d266587dd868a8401aa9904b9f2eec56cd9dde739` | 79768 | 2026-06-24 08:53 |
| v0.15 | `…_v0_15.md` | `916ecab0861ff781e55d24197afe41a9c79415660522c426d1b4902735c87d5c` | 83938 | 2026-06-24 09:46 |
| v0.16 | `…_v0_16.md` | `2b68463e6ef536c815d3e50744141ea1a4925247480e0a0c1714586aac317e5b` | 86638 | 2026-06-24 10:32 |
| v0.16 | `…_v0_16 (1).md` | `975c7b98a3b316307df51a57cc2b0e3be2dc4357631ad8c39ccfd976becccf11` | 88425 | 2026-06-24 14:49 |
| v0.17 | `…_v0_17.md` | `10ca26328ded751269081b3d85e5aa78c30ae97a85e899f017eee24ea07e2df8` | 92269 | 2026-06-24 14:56 |
| v0.17 | `…_v0_17 (1).md` | `e24acfc150e3f4e9753ff06e6bd6edb89bf913e11382818743b9bce057bf1bcd` | 93107 | 2026-06-25 07:23 |

`…` = `RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN`. All hashes recomputed from the extracted bytes and equal to the collection `MANIFEST.json`.

## 3. Relation of the chain to `dzt-v0.8` (observations)

- **O-3.1** `…_v0_8.md` (`57cbb30e…`) differs from the tagged text (`cad20982…`) in 7 hunks (lines 53, 178, 212, 214, 244–245, 257, 300). The untagged copy scopes the §1 amplitude-norm computation and `DZT-ALG-CASCADE-NORM` to "finite horizon p∈{12,16,…,52}" and lists `DYAD-ALG-PHASELAW` and `DYAD-THM-R` as the all-$p$ import rows. The tagged text makes the p ≤ 1000 closed-form audit the canonical computation with the p = 12–52 table as validation only, registers `DYAD-THM-Q403-PHASE-ALLP` as the canonical all-$p$ phase theorem (PHASELAW superseded, THM-R folded in), and carries the "Ledger-hygiene patches (pre-freeze)" text.
- **O-3.2** Every v0.9–v0.17 file contains the "Ledger-hygiene patches" paragraph and `DYAD-THM-Q403-PHASE-ALLP`; each v0.9 variant shares more lines with the tagged v0.8 than with `57cbb30e…`. The recovered chain after v0.8 is built on the tagged text.
- **O-3.3** v0.6 is absent. v0.7's header reads "Supersedes … v0.6"; the tagged v0.8 Appendix A carries a v0.6 entry.
- **O-3.4** Every v0.9–v0.17 file keeps the v0.8 header pins (Methodology v1.2, Programme v1.1, Dyadic v6.4.8.1, AZ v0.6, OFN v0.7).
- **O-3.5** No release record, adoption record or tag exists for any recovered edition. The NUMGEN memo (line 6) cites a "DZT v0.17 session record"; no such file is in the recovery.

## 4. Same-numbered variants — what differs (observations; complete diffs: regeneration command in the header)

| edition | pair | hunks | difference |
|---|---|---|---|
| v0.4 | `v0_4` → `v0_4 (1)` | 10 | `(1)` replaces the claim $\mathbb Q(\zeta_8)^+=\mathbb Q(\sqrt3)$ by a p = 12-only statement with the p = 8 degeneracy ($\mathbb Q(\zeta_8)^+=\mathbb Q(\sqrt2)$); rewrites the §1 frontier (0A closed on all three rows; OPEN-0B active); adds the Case-V route in §4; reorders and extends the import ledger (`DYAD-ART-CASCADE-Q4-03`, P1, REALITY, LEAD, PHASELAW rows; `DYAD-ALG-CASCADE-P12` marked subsumed); adds provenance rows. The tagged v0.8 carries the p = 12-only wording. |
| v0.8 | `v0_8` → `v0_8 (1)` | 7 | see O-3.1 |
| v0.9 | `v0_9` → `v0_9 (1)` | 5 | `v0_9`: the theorem and status paragraph are present, but §2 still lists OPEN-0B-R as "prove or reject", its block keeps the v0.8 target and the `[HYP]` text with a bracketed "odd-support part now proven", §6.3 keeps an `[OPEN]` line. `(1)`: §2 moves to OPEN-0B-DEN; the 0B-R block is rewritten as "Closed result"; §6.3 line marked superseded; `DZT-ALG-CASCADE-NORM` scope "validation table, p=12–64"; status summary adds that the phase-law import was promoted to all-$p$ `[THM]` in v0.8 as `DYAD-THM-Q403-PHASE-ALLP`. |
| v0.9 | `v0_9 (1)` → `v0_9 (2)` | 5 | `(2)` adds DZT-OPEN-CHANNEL-UNIV as the active direction, issues DZT-REQ-002 (registry row), rewrites the §1 frontier, and replaces the candidate-mechanism `[HEUR]` paragraph by "the proved mechanism is the order condition". |
| v0.10 | `v0_10` → `v0_10 (1)` | 4 | `(1)` extends the §1 validation table to 14 values (p = 12–64), adds the DZT-B1-0 gate and the $W^{(A)}$ rejection, adds the §5 universality row, rewords the §1 frontier. |
| v0.10 | `v0_10 (1)` → `v0_10 (2)` | 2 | `(2)` adds a gauge caveat and issues DZT-REQ-003 (registry row). |
| v0.11 | `v0_11` → `v0_11 (1)` | 2 | `(1)` adds the discriminator paragraph (cubic coefficient $A$ as the decisive datum) and registers DZT-REQ-004 as issued. |
| v0.16 | `v0_16` → `v0_16 (1)` | 1 | `(1)` extends the B1 paragraph (line 125) with "DZT-B1-WC OPENED (v0.16+)", first-pass scoping and the leading hypothesis that $W^{(C)}$ fails. Header and Appendix A are identical. |
| v0.17 | `v0_17` → `v0_17 (1)` | 2 | Header, status summary (line 13), §2–§9 and Appendix A are identical. Hunk 1: line 59 of `v0_17` ("`[OPEN]` **Immediate frontier.** … remaining native open piece is the denominator … next new direction is Track B1") is replaced in `(1)` by lines 59–61: "`[OPEN / parked]` … (closure freeze v0.17)" and "`[COR hygiene]` … No v0.18 unless new science". Hunk 2: `(1)` removes from the B1 block the sentence that $W^{(C)}$ "remains un-audited". |

- **O-4.1** `v0_17` line 59 states the denominator law as open while its own line 13 and the DEN block (line 108 → the "CLOSED at THEOREM grade (v0.16)" paragraph) state it closed.
- **O-4.2** In both v0.17 files, §2 item 2 (line 69 in `(1)`, 67 in `v0_17`) still lists DZT-OPEN-0B-DEN as an open priority, and the DEN block keeps "Status: OPEN (the one remaining piece …)" (line 108 in `(1)`) directly above the "CLOSED at THEOREM grade (v0.16)" paragraph (line 110).
- **O-4.3** Only `(1)` states the closure freeze. No record outside the file says whether the freeze was a PI decision; the NUMGEN memo (line 56) reports it as the stream's state.

## 5. Other recovered files

### 5.1 Proof notes and cross-stream exchanges

| file | SHA-256 | copies |
|---|---|---|
| `DZT_OPEN_0B_R_odd_support_proof_note.md` | `9ce5e99f012319d5cd5d095ed32261857e009d905ed8cf9cf3274f7b6355a30f` | 2 identical |
| `DZT_THM_CASCADE_DENOMINATOR_proof.md` | `2a8354ca43d9c33b443a4f8f5d8fdf03548304b39e22badf46aedd598c1b5e39` | 1 |
| `DZT_v0_7_closed_form_iteration_note.md` | `e6887488f354d468efd8e99e98c597fc05c55dcb44e8f8e72ede8255e3ee42f0` | 1 |
| `DZT_REQUEST_TO_DYADIC__REQ-002_second_channel.md` | `ed6bf3630e65a0873f692277c3e36dab1c18d6a7083b35756c388bcabc7f97f9` | 2 identical |
| `DZT_REQUEST_TO_DYADIC__REQ-003_local_germ_data.md` | `b69439ec3afc8d72cb13e56ad07afcfab5864392eda9178f6549e70c7785f51e` | 1 |
| `DZT_REQUEST_TO_DYADIC__REQ-004_resonant_tower.md` | `ca746c0839b67e5fb09f76e47cdd65ca68ed80471974399ef400b28da2a57254` | 1 |
| `DYAD_RESPONSE_TO_DZT_REQ-002.md` | `0f8c4b1566e62f0cb97513bc9b9e2b57d9fd712a314f24f66ba8ad7b0a7f7dd3` | 2 identical |
| `DYAD_RESPONSE_TO_DZT_REQ-003.md` | `c8b5ee22297c9db7d51581ff3272b06281187e98c7985909e042635ca14f8e09` | 2 identical |
| `DYAD_RESPONSE_TO_DZT_REQ-004.md` | `94f3f458d1d491ea231803520636bd00d558854832669c80731fde84d4c12f55` | 2 identical |

DZT-REQ-001 is cited by v0.17 (twice) but no file of it is in the recovery. No DZT-REQ-005 file is present either (cited twice in `(1)`).

### 5.2 Scripts named in v0.17 (both variants name the same set)

v0.17 names 15 distinct `.py` files. Thirteen are DZT scripts and all thirteen are present; the two absent ones are Dyadic-origin.

| script | present | distinct contents (copies) |
|---|---|---|
| `dzt_0b_audit.py` | yes | 1 |
| `dzt_0b_den_law_check.py` | yes | 1 (2 copies) |
| `dzt_0b_normlaw.py` | yes | 1 |
| `dzt_anomaly_rule_check.py` | yes | 1 |
| `dzt_b1_leadinglog_tower.py` | yes | 1 |
| `dzt_b1_polylog_hierarchy.py` | yes | 1 |
| `dzt_b1_wB_audit.py` | yes | 1 |
| `dzt_casev_norm_audit.py` | yes | **2**: `d48716c8…` (plain), `22783fcd…` (`(1)`) |
| `dzt_casev_norm_from_closed_form.py` | yes | **2**: `4d3d3ca3…` (plain, `(1)`), `e38b5f7e…` (`(2)`, `(3)`) |
| `dzt_channel_audit.py` | yes | 1 |
| `dzt_channel_universality_check.py` | yes | 1 |
| `dzt_odd_support_proof_check.py` | yes | 1 |
| `dzt_open_0a_verify.py` | yes | **2**: `989f6c2d…` (plain), `3791b110…` (`(1)`, `(2)`) |
| `qb_extract.py` (Dyadic extractor, cited with DYAD-RESP-DZT-002) | **no** | — |
| `q4_03_R_identity_certificate.py` (Dyadic certificate) | **no** | — |

Also present, not named in v0.17: `dzt_q4_03_numeric_probe.py`, `dzt_q4_03_profile_exact.py` (also in `legacy-src/`), `dzt_casev_norm_closed_form_p8_1000.csv` (named in v0.8 §8; 2 identical copies), `ng_review_dzt_independent_audit_v1.py`.

- **O-5.1** The PR #289 intake comment counts "13 scripts named in v0.17, 12 present". The count above differs: 15 names, 13 DZT scripts present, 2 Dyadic-origin absent.
- **O-5.2** DZT DSNs cite scripts without hashes. For the three scripts with two contents, the text of the later content matches what the DSNs say was changed: `(1)` of `dzt_casev_norm_audit.py` is the 14-point version (v0.6+), `(2)`/`(3)` of `dzt_casev_norm_from_closed_form.py` print the corrected `q ≡ 1 (mod 4)` heuristic (the v0.8 hygiene patch), `(1)`/`(2)` of `dzt_open_0a_verify.py` carry the patched ownership wording (v0.2+). This is a reading of the text, not an identification of the cited bytes.
- **O-5.3** The Dyadic files `q4_03_cascade_extract.py` and `q4_03_cascade_coeffs_p8_200.csv` (cited by DZT v0.8 with `ecdb805f…`/`14526cf1…`) are neither in the recovery nor in the repository; Dyadic v6.4.24 names the extraction `DYAD-ART-Q403-EXTRACT` without a hash.

## 6. Hash cross-references to independent sources

Searched: every recovered SHA-256 (full, 12-character and `8…4`/`8…6` short forms) against all files on `main` outside the upload.

| recovered file | SHA-256 | independent record |
|---|---|---|
| `…_v0_8 (1).md`, `legacy-src/…/…_v0_8.md` | `cad20982…92ff2` | tag `dzt-v0.8`; `BASELINE.md` |
| `DYAD_RESPONSE_TO_DZT_REQ-002.md` (both copies) | `0f8c4b15…7dd3` | `dyad-v6.4.24` Appendix D, line 1426 |
| `ng_review_dzt_independent_audit_v1.py` | `17f8415b…cad8` | `upload/numgen-records/` (`SHA256SUMS`) |

No other recovered file matches a hash recorded elsewhere in the repository.

## 7. Pins, imports and identifiers against the current tags (observations)

Classification (claim / identifier-pin / none) is left to the triage record.

### 7.1 Header pins (v0.8 lines 6, 7, 10; identical in v0.9–v0.17)

| cited | current | observation |
|---|---|---|
| `DSN_METHODOLOGY_v1.2` | `methodology-v1.4` | v0.8 uses compound grade tokens `[THM/ALG]`, `[ALG finite horizon]/[HEUR]`, `[HEUR/ALG finite horizon]`, `[ALG fin-hor]` and the undeclared alias `[HEUR diagnostic]`; v0.17 adds `[CERT]`, `[NOTE — method]`, `[COR hygiene]`, `[OPEN / parked]`, `[FAIL at certification level]`, `[DEF/HYP]`, `[RESULT, RID: …]` without `[from: …]`, undeclared `[INTERP]`. Both carry history in §1 (Methodology v1.4 live-file rule). New v0.17 identifiers `DZT-PROOF-*`, `DZT-REQ-*`, `DZT-B1-0`, `DZT-B1-1`, `DZT-B1-WC` use words outside the RID category list. Atlas finding DZT.Q4 (at `atlas-v0.14`) covers the v0.8 part. |
| `RTG_PROGRAMME_OVERVIEW_v1.1` | `programme-v1.4` | SG-PROG-2 rewritten as a physical-selection restriction; SG-DZT-6's wording reads consistently with it. IF18 still pins Dyadic v6.4.8.1; IF19 (DZT→Dyadic feedback) open; §9.2 records the DZT pass as not executed. |
| `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1` | `dyad-v6.4.24` | see 7.2 |
| `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6` | `az-v0.10` | SG-AZ-7 unchanged; AZ v0.10 mentions DZT only to exclude a relation. |
| `RTG_ONTOLOGICAL_FOUNDATIONS_v0.7` | `ofn-v0.12` | RF-O08-13 keeps DZT v0.8 as the supplied version. |

### 7.2 Dyadic imports in v0.8 §7 (lines 236–247) and the v0.17 additions (v0.17 `(1)` lines 266–292)

| as printed in DZT | at `dyad-v6.4.24` | observation |
|---|---|---|
| `DYAD-OPEN-B5-ALLP` | closed lifecycle RID; result `DYAD-ALG-B5-ALLP-NONVANISHING` `[ALG]` | Appendix F row |
| `DYAD-ALG-VANISH-B2/B3/B4` | three RIDs | Appendix F row; VANISH-B2 holds for all $p\ge4$ (DYAD notice N16–N21) |
| `DYAD-ALG-CASCADE-P12` | no RID; value in §6.11 | DZT writes $-13+\tfrac{15\sqrt3}{2}$, the sign Dyadic restored |
| `DYAD-ALG-P6-FACEFLUX` | same RID | — |
| `DYAD-ART-CASCADE-Q4-03` (`ecdb805f…`, `14526cf1…`) | content of `DYAD-ART-Q403-EXTRACT`, no hash recorded | files absent (O-5.3) |
| `DYAD-THM-P1`, `-REALITY`, `-LEAD`, `-R`, `DYAD-CF-Q403` | components of `DYAD-THM-Q403-PHASELAW`, no RIDs | Appendix F; Atlas DZT.Q1 |
| `DYAD-THM-Q403-PHASE-ALLP` | `DYAD-THM-Q403-PHASELAW` `[THM]`, line 689, closed v6.4.9 | same content; DZT grade token `[THM/ALG]` |
| `DYAD-ALG-PHASELAW` | historical label | — |
| `q4_03_R_identity_certificate.py` | `DYAD-ART-Q403-CERT` | file not in the repository |
| *v0.17:* `DYAD-THM-C21` | same RID `[THM]` (lines 69, 469); $c_{21}=-\tfrac12-i\tfrac{2\sqrt3}{3}$ | value equal |
| *v0.17:* `DYAD-RESP-DZT-002`, `-003`, `-004` registered as RIDs in DZT §8 | no such Dyadic RIDs; Appendix D cites the REQ-002 response file as a definition source | DYAD-namespace strings registered by DZT |
| *v0.17:* $A=\tfrac{47}{54}$ "radial recurrence $Q_{m+1}=Q_m-Q_m^2+AQ_m^3$" (line 287; source: REQ-004 response lines 26–27, "DSN §6.5 … line 401") | `DYAD-ALG-RAW-ANGULAR-MEAN` `[ALG]` `[scope: fixed-radius uniform-angle mean in the raw W-frame]` (lines 73, 523–527); `[COR] [v6.4.10]` (line 529) supersedes the unqualified recurrence wording | see O-8.1 |
| *v0.17:* admissibility "$(0,b)$ is an order-$q$ extra-charge slot iff $q\mid(b+1)$" (`DZT-ALG-ADMISSIBILITY`, line 116) | Appendix D line 1444: "iff $q\mid(b+1)$ (for $b+1<p$; in general … iff $q\mid(b+1)$ and $p\nmid(b+1)$, owner check M11)" | see O-8.2 |
| *v0.17:* "SG-10" for the transformation status of $\Im c_{32}$, $c_{05}$ | Dyadic `[SG-10]` (line 347): $\Im(\nu_5)$ not invariant under real-analytic residual gauge | the correspondence $\Im c_{32}\leftrightarrow\Im\nu_5$ is not checked here |

## 8. Scope mismatches and text errors observed

- **O-8.1 (B1 premise).** v0.17 builds the B1 results on a pointwise radial recurrence: line 127 (discriminator, verdict, DZT-B1-1 "first correction", "extended (v0.14)") uses $Q_{m+1}=Q_m-Q_m^2+AQ_m^3$ with $A=\tfrac{47}{54}$ and the balance $c=A-1$, $Q_m=\tfrac1m-\tfrac7{54}\tfrac{\ln m}{m^2}+\dots$. The source, the REQ-004 response (lines 26–27), calls this "the physical radial recurrence". At `dyad-v6.4.24`, $\tfrac{47}{54}$ is the coefficient of an averaging operator, "not a pointwise recurrence for $Q$ along arbitrary primitive orbits (the pointwise update carries the nonzero $Q^{5/2}$ term below)" (line 527), and the unqualified recurrence wording is superseded by `[COR] [v6.4.10]` (line 529). On the positive real ray, Dyadic records $Q_6=Q_0-Q_0^2-\tfrac5{24}Q_0^{5/2}+\tfrac{37}{40}Q_0^3+O(Q_0^{7/2})$ (lines 75, 534), so $Q_6-(Q_0-Q_0^2+\tfrac{47}{54}Q_0^3)=-\tfrac5{24}Q_0^{5/2}+O(Q_0^3)$ there. Both co-owners reached this independently (17 Nov 2026).
- **O-8.2 (admissibility).** DZT states the gate without the qualifier "$b+1<p$" or the condition $p\nmid(b+1)$ that Dyadic Appendix D records.
- **O-8.3 (odd-support proof note).** `DZT_OPEN_0B_R_odd_support_proof_note.md` line 173: "$N(L+1)=|\Phi_p(-1)|=1$ for $4\mid p$". For $p=2^k$ ($k\ge2$), $\Phi_p(-1)=2$. The denominator proof uses $\Phi_p(-1)\to[p=2^k]$ (v0.17 line 110). The odd part of the norm is unaffected; the two texts disagree.
- **O-8.4 ("unit factor").** v0.17 line 250 (both variants): "$A_s=(I-1)(L^2-I)$ … splits off a unit factor $I-1$ of 2-power norm $2^{\varphi(p)/2}$". $I-1$ has norm $2^{\varphi(p)/2}\neq\pm1$; it is not a unit.
- **O-8.5 (stale status lines).** O-4.1 and O-4.2.
- **O-8.6 (LIT record header).** The LIT note at `8e2fb5cb` (line 3) says "Not reviewed by the second co-owner. Not offered to DZT." Review `5888136234` on LIT PR #100 (13 Nov 2026) reads "ACCEPT SCOPED / PI MERGE-READY", and the offer was filed as `pipes/DZT/20261113-LIT-norm-law-proof-candidate.md`. The note's text is unchanged at LIT `main`.

## 9. The norm law: LIT offer and v0.17 statements

### 9.1 Statements compared (texts as read)

- v0.17 `DZT-THM-CASCADE-ODD-SUPPORT` (line 250) and `DZT-THM-CASCADE-DENOMINATOR` (line 110): for $p=4s\ge12$, the odd part of the numerator of $N_+(M_p)$ is $\ell^2$ iff $p=8\ell^a$, $\ell$ odd prime, $\ell^a\equiv1\pmod4$, else 1; the denominator is $2^{d_p}$, $d_p=\varphi(p)/4+[p=2^k]+[p=3\cdot2^k]$.
- LIT Proposition (§4 of the LIT note): $N_+(M_p)^2=N_{\rm full}(p)=2^{-\varphi(p)/2}D(p)/(B(p)^4C(p))$, with $B=2$ iff $p=2^k$; $C=4$ iff $p=3\cdot2^k$; $D=\ell^4$ iff $p=8\ell^a$, $\ell^a\equiv1\pmod4$; $D=4$ iff $p=2^k$; otherwise 1. It states $|N_+|$ only.
- Hypotheses and range are the same: the Dyadic closed form and $Q_p=i\zeta_p^3M_p$; $p=4s\ge12$ (p = 8 vanishes).
- **Denominator.** From LIT, $v_2|N_+|=\tfrac12\big(-\varphi/2+v_2D-4v_2B-v_2C\big)$ with $v_2D=2[p=2^k]$, $v_2B=[p=2^k]$, $v_2C=2[p=3\cdot2^k]$, giving $-\big(\varphi/4+[p=2^k]+[p=3\cdot2^k]\big)=-d_p$. Same exponent.
- **Numerator mechanism.** v0.17 uses $L^2-I=L^2(1-L^{s-2})$; LIT uses $1+L^{s+2}=1-L^{3s+2}$. Since $L^{4s}=1$, $L^{3s+2}=L^{-(s-2)}$, so the two roots of unity have the same order. Both locate the mod-4 gate in that order.
- **The v0.8 `[HYP]` mechanism** (real quadratic subfield). v0.17 calls it subsumed by the theorem. LIT says it is not needed and cannot be the reason at $q=9$ ($\mathbb Q(\zeta_9)^+$ is cubic).

### 9.2 What the tables state

`dzt_casev_norm_from_closed_form.py` (both contents), line 26: "Thus N_+(M) = sqrt(abs(N_full))", and line 71 `exact_sqrt_abs_rational`. The CSV `dzt_casev_norm_closed_form_p8_1000.csv` has no negative entry. The DZT tables headed $N_+(M_p)$ (v0.8 §1, §6.3; v0.17 §1, §6.3) list these values.

### 9.3 Signed values (SESSION checks)

**Claude** (not a recovered script; Python 3.13, mpmath 1.4.1; high-precision numerics, not an exact proof; script SHA-256 `eb039665…9b6f`, output SHA-256 `4f69abdc…a53`). Command: `python3 -I signed_norm.py`.

```python
# SESSION check (Claude, DZT co-owner, 17 Nov 2026). Not a recovered script.
# Signed N_+(M_p), M_p = Q_p/(i*zeta_p^3), from the Dyadic closed form (dyad-v6.4.24 §6.11,
# DYAD-THM-Q403-PHASELAW): Q_p = L^5 (I L^2 + I - L^2 + 1) / (2 (L+1)^4 (L^2+L+1)), L = zeta_p, I = L^(p/4).
# N_+(M_p) = product of sigma_k(M_p) over k in (Z/pZ)^x / {+-1}; high-precision numerics, not an exact proof.
import sys
from fractions import Fraction
from math import gcd
from mpmath import mp, mpc, exp, pi, fabs, nstr
mp.dps = 120
def Q(L, I):
    return L**5 * (I*L**2 + I - L**2 + 1) / (2*(L + 1)**4 * (L**2 + L + 1))
ps = [int(a) for a in sys.argv[1:]] or list(range(12, 101, 4)) + [200]
for p in ps:
    s, prod = p // 4, mpc(1)
    for k in range(1, p // 2):
        if gcd(k, p) == 1:
            L = exp(2j*pi*k/p); I = L**s
            prod *= Q(L, I) / (I * L**3)
    fr = Fraction(nstr(prod.real, 80)).limit_denominator(2**400)
    print(f"p={p:4d}  N_+={fr}  |imag|<{float(fabs(prod.imag)):.0e}")
```

| p | $N_+$ | p | $N_+$ | p | $N_+$ |
|---|---|---|---|---|---|
| 12 | +1/4 | 44 | −1/32 | 76 | −1/512 |
| 16 | −1/8 | 48 | −1/32 | 80 | +1/256 |
| 20 | −1/4 | 52 | −1/64 | 84 | +1/64 |
| 24 | −1/8 | 56 | +1/64 | 88 | +1/1024 |
| 28 | +1/8 | 60 | +1/16 | 92 | +1/2048 |
| 32 | −1/32 | 64 | −1/512 | 96 | −1/512 |
| 36 | −1/8 | 68 | +1/256 | 100 | −1/1024 |
| 40 | +25/16 | 72 | +9/64 | 200 | +25/2²⁰ |

Imaginary parts below $10^{-120}$ at every point. Absolute values: 24/24 equal to the DZT CSV.

**Second co-owner (ChatGPT)**, reported to the PI on 17 Nov 2026 (EV-SRC-REPORTED; 100 digits): +1/4 (12), −1/8 (16), −1/4 (20), −1/8 (24), +25/16 (40), +9/64 (72), +1/256 (80). Equal at all seven points.

**NUMGEN memo** line 64: sign −1 at 16, 20, 24; +1 at 12, 28, 56. Consistent.

- **O-9.1** The values tabulated as $N_+(M_p)$ in DZT are $|N_+(M_p)|$. Neither v0.17 theorem nor the LIT Proposition determines the sign. No sign law is proposed here.

## 10. Not verified in this reading

- Historical identity of any recovered byte except the three cross-references of §6; which variant of any edition was final; whether any recovered edition was adopted; whether the v0.17 freeze was a PI decision.
- The "DZT v0.17 session record", v0.6, DZT-REQ-001, DZT-REQ-005, `qb_extract.py`, the Dyadic `q4_03_*` scripts and data: not available.
- Every exit code, PASS and certificate stated in the recovered DSNs (EV-SRC-REPORTED); no recovered script was run.
- Step-by-step correctness of the two recovered proof notes and of the LIT proof (read, not reviewed to a verdict); Apostol 1970 and Washington were not opened.
- Whether the B1 results survive with the averaging-operator scope (O-8.1); the $\Im c_{32}\leftrightarrow\Im\nu_5$ correspondence (§7.2).
- The LIT check output (`dzt_norm_law_check.out`, PASS) was read, not rerun.

## 11. Interpretation (SESSION; for the triage, not a disposition)

- O-8.1 bears on the premise of DZT-B1-1 and the $W^{(C)}$ argument. It does not show that they are false; it shows that the cited premise no longer has the scope the B1 text uses.
- O-8.3, O-8.4 and O-9.1 bear on the wording and scope of the norm-law statements, not on their content as read.
- The remaining rows of §7 are pins and identifiers.

## 12. Scope of this record

Received and read only. Nothing in this record changes the governing DZT edition, the status of any DZT claim, any other stream's DSN, or any pipe item.

*Check stamp: Claude, DZT co-owner, 17 Nov 2026; repository `main` `a7ccaa6`; recovery extracted from PR #289 transport, joined SHA-256 `b9e53d745c93d05066aec95a8be9e6617ddd1611c1ec2605e0637f786031b035`.*
