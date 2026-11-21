# RTG State Atlas v0.15 — acceptance record

**Status:** ACCEPTED by the PI, 21 Nov 2026 (§4). Review: `6004985736` on head `46a4105`, ACCEPT SCOPED, no correction asked. `atlas-v0.14` stays the tagged Atlas until the PI accepts a candidate, the PR of branch `claude/atlas-v0.15` is merged, and the annotated tag `atlas-v0.15` exists and is verified.
**Object:** a derived, NONCANONICAL Atlas. Acceptance adopts no owner science.
**Recorded by:** Claude, Atlas owner, 21 November 2026, on branch `claude/atlas-v0.15`.
**Method:** Atlas Method v0.3 (`atlas-method-v0.3`).
**How it started:** in the project conversation of 21 Nov 2026 the Atlas owner proposed v0.15 at 00:07 +03:00. At 00:17 the PI relayed the Atlas co-owner's recommendation (start now, do not wait for the DZT B1 result of PR #347; four acceptance criteria). The candidate is built on that recommendation. Whether to proceed, and acceptance, are the PI's decisions; neither is recorded here.

## 1. Object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md`, v0.15 candidate | `483e60034ff3bb644216c5123d28b8bca253d3ba1b72cdf68bfb0056518d02df` (542,028 bytes, 1,540 lines) |
| base `atlas-v0.14` | `d34e5697ae47201133f513bce5f6b2b8438ed2f4e654fe33a73048a5ca7b1e85` (541,061 bytes, 1,545 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.3) | `a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f` |
| `evidence/atlas/v0.15/source_manifest.json` | `5fadeb234b11bc0a2e756c5a95361b4e664910ae5de7818b2f649817272c46cd` |

Source snapshot: `main` `357b963f4a8e33a2dd962952330761bda73a7c05` (merge of PR #345; `dzt-v0.19` → `5f3b205` is an ancestor). One source moved against the v0.14 manifest. The other seventeen are byte-identical and were not re-extracted.

| Source | v0.14 | v0.15 | File SHA-256 | Authority |
|---|---|---|---|---|
| DZT | `dzt-v0.8` | `dzt-v0.19` | `2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce` | `records/dzt/DZT_v0_19_RELEASE_RECORD.md` (PI adopted 20 Nov 2026 on the candidate bytes `50f58c88…7442`; the published file differs from them in three status lines) |

The Atlas was at `dzt-v0.8`, so this refresh carries two DZT editions: v0.18 (corrections and the Methodology v1.4 migration, no new claim, adopted 19 Nov) and v0.19 (one theorem). The tag is annotated. The builder asserts, for every source, that tag bytes = manifest hash = snapshot bytes and that no newer tag exists.

**Build:** `python3 -I evidence/atlas/build/refresh_v0_15.py`. It starts from the bytes of `atlas-v0.14`, applies 27 anchored operations (`evidence/atlas/v0.15/edit_log.json`, ids AR15-001 … AR15-027) and replays them inside the run with an identical result. Two runs gave the same hash. **Evidence:** `evidence/atlas/v0.15/`.

## 2. What changed (27 operations; −5 lines, +967 bytes)

| Kind | Operations |
|---|---|
| identity | 5 |
| locator/source wording | 1 |
| DZT v0.18/v0.19 | 8 |
| reviewed items | 12 |
| pipes | 1 |

No Method §4.1 span deletion and no §4.7 operation.

### 2.1 The new theorem (AR15-014)

`DZT-THM-CASCADE-NORM-LAW THM (assuming: DYAD-THM-Q403-PHASELAW; proof: written derivation)`, homed in D2.L2 after the finite rows, locator `@DZT§6.3`. It states the owner's law for every p=4s≥12: |N_+(M_p)|=ℓ(p)²/2^{d_p}, d_p=φ(p)/4+[p=2^k]+[p=3·2^k], with ℓ(p)=ℓ exactly at p=8ℓ^a, ℓ^a≡1 mod 4.
- Kept outside, as the owner states: the sign of N_+(M_p); p=8 (Q₈=0); the law without its Dyadic assumption; any RH or prime-distribution reading.
- One dependency: `<DYAD-THM-Q403-PHASELAW`.
- Named on the node: the finite cases (DZT-ALG-CASCADE-NORM, DZT-ALG-CASCADE-ANOMALY-SET), the closure of DZT-OPEN-NORM-LAW, the retired mod-4 reading (owner key DZT19-C01) and the proof sources of the owner's §9.
- Certificate: `cert DZT-ART-NORMLAW-CHECK`, the repository script `evidence/dzt/norm_law_review/dzt_norm_law_review_check.py` (SHA-256 `566867bb…cebb7`, asserted). The node says that it was not rerun here and that it is a finite check, not the proof.

### 2.2 The co-owner's four criteria

| Criterion | Where |
|---|---|
| 1 — the theorem's full scope: `[THM] [assuming: DYAD-THM-Q403-PHASELAW]`, p=4s≥12, \|N_+(M_p)\|; no sign law; p=8 outside | AR15-014; scope guards; controls W1–W3 |
| 2 — `*DZT:mechanism HYP` no longer current; `DZT-HYP-MAHLER-NEARMISS` FAIL kept apart | AR15-015 removes the `[HYP]` line and names DZT19-C01 on the theorem node; the FAIL node and the D2 FAIL list are unchanged in what they record (AR15-018 corrects only the denominator wording); controls W9, W10 |
| 3 — full L5 disposition: DZT.Q1, Q4, Q5, and the DZT part of METH.M1 and PROG.G6, each with a reason | §2.4; `dispositions.json` (8 entries) |
| 4 — traceability: the old "no denominator law" and the historical Dyadic strings corrected against the owner text; the closed OPEN keeps its RID and result; the remaining unresolved links are real debts | AR15-013, AR15-018 (the note's value 2^{−φ(q)} is wrong; on the anomaly set only its denominator exponent is right; denominators in general belong to the theorem); AR15-007, AR15-008, AR15-017 (owner RIDs only); AR15-019 (`DZT-OPEN-NORM-LAW (0B-R) CLOSED by DZT-THM-CASCADE-NORM-LAW`); §3 links count |

### 2.3 Other DZT rows

- **Reverse relation** on `DYAD-THM-Q403-PHASELAW` (AR15-007): DZT is now a consumer through its owner RID, as the assumption of the theorem and of the norm object. The note label and the pointer to DZT.Q1 leave.
- **Import record** (AR15-008): `*DZT:imports-dyad-note THM(import; phantom RIDs !)` becomes `*DZT:imports-dyad (import record; no DZT claim; grades are the owner's)`. It is restated at DZT §7: owner RIDs only; the parts of the phase law are named without separate RIDs, as DYAD App F classifies them; the extractor corresponds by content only, with no byte identity claimed; the p=8 and p=12 values are cited as text.
- **p=12 norm** (AR15-009): "Mahler mechanism HYP only" is replaced by its owner history: the RESULT voice was retracted, the family form DZT-HYP-MAHLER-NEARMISS was falsified at p=40, and the value survives.
- **Norm object** (AR15-010): the compound head `THM/ALG(import)·all p` becomes the owner's `ALG (sc: object level, all p=4s≥12)`; the factorization stays DYAD's [THM]; M_p is real and its sign is not asserted.
- **Cascade norm, anomaly set** (AR15-011–013): the values are \|N_+\| (owner v0.18); the table's scope is p=12–64 (14 points); both rows are finite cases of the theorem.
- **p=40 courtesy flag** (AR15-016): removed; it is not in the owner text at v0.18 or v0.19.
- **OPEN 9 micro row** (AR15-017): DZT cites the p=12 value as text and no longer prints the unmatched string.
- **High-risk ledger** (AR15-020): "no k_p formula" leaves. The law is [THM] only under the Dyadic assumption and says nothing about the sign (owner §5).
- **D2 header** (AR15-005, AR15-006): DZT v0.19, Methodology v1.4, Level A; the owner's local alias is `[NUM diagnostic]`, and `[import-ref]` is a reference label, not a status tag.

### 2.4 L5 and headlines

| Key | Disposition | Reason (full text in `dispositions.json`) |
|---|---|---|
| DZT.Q1 | retired | DZT §7 cites owner RIDs only; none of the nine strings occurs in the owner text |
| DZT.Q4 | retired | no compound grade token at `dzt-v0.19`; the anomaly set is [ALG] in every section |
| DZT.Q5 | retired | §1 states the table as p=12–64 and states the all-p law with its 20 anomaly points p≤1000 |
| H3 | retired (headline) | it summarised DZT.Q1 only; H4–H12 keep their numbers (display order only) |
| METH.M1 | reworded | DZT leaves the row; TDR-G and DZT declare Methodology v1.4 and carry no compound tags |
| PROG.G6 | reworded | after the Programme record, the DZT edition of this snapshot declares Methodology v1.4, after a reactivation triage and the v0.18 corrections edition |
| NUMGEN.N-I1 | reworded | pipe census at the new snapshot |
| AZ.A5 | retained | the anomaly set and the 4\|q rule stay apart (SG-DZT-1, SG-AZ-7); the theorem creates no relation |

The cumulative retired list grows from 156 to 162 entries: the three keys, each in its dotted and spaced form.

### 2.5 Pipes

NUMGEN.N-I1 is restated at `357b963`: 147 items in 20 inboxes, of which 80 are closed, 5 dispositioned and 62 open. ATLAS, AZ, DZT and TDRG have no open item. DZT v0.19 sent its notices to PROG, DYAD and NUMGEN (present at the snapshot). No ATLAS item exists for this edition.

## 3. Checks, limits, and points for the reviewer

**Shared checker** (`tools/atlas_check.py`, run with this edition's manifest, coverage map and cumulative retired list): 0 FAIL.

| Check | v0.15 | `atlas-v0.14` with its own manifest, today |
|---|---|---|
| sources | 72 PASS | 71 PASS, 1 FAIL (the BASELINE DZT row has moved to v0.19, as expected) |
| coverage | 137 PASS | 137 PASS |
| qualifiers | 4 PASS | 4 PASS |
| links | 531 PASS, **1** documented-unresolved, 2 UNVERIFIED | 527 PASS, 10 documented-unresolved, 2 UNVERIFIED |
| artifacts | 124 PASS, 2 UNVERIFIED | 121 PASS, 2 UNVERIFIED |
| keys | 162 PASS | 156 PASS |
| wording | 13 WARN | 13 WARN |

The nine DZT note strings leave the documented-unresolved links. The one that remains is `DYAD-CAND-PHISTAR-ENTRY-PHASE` (never a Dyadic identifier; not DZT). The two UNVERIFIED links (NUMGEN declaration forms) and the two UNVERIFIED artifacts (GEN `cm.py`, `fit.py`) are as at v0.14. The 18 shared controls behave as expected.

**Builder assertions:**
- No DZT-owned RID of `dzt-v0.8` is missing at `dzt-v0.19`. The DZT-owned identifiers new since v0.8 are exactly `DZT-THM-CASCADE-NORM-LAW` and `DZT-ART-NORMLAW-CHECK`, each with one declared home. The Dyadic RIDs DZT newly cites already have Dyadic homes.
- 24 owner-text facts hold (`verification_summary.json`). Among them: the theorem's tags and formula; the sign outside the statement; the gate as the order of L^{s−2}; `[SUPERSEDED]` DZT19-C01; both FAIL records; the finite-case sentences; the note's wrong value; no compound token; none of the note strings; the check script's hash in the repository; Level A; B1 and B2 open.
- Scope guards for the theorem, the finite rows, the frontier, the import record, the reverse relation, METH.M1, PROG.G6, H3, AZ.A5 and the high-risk sign caveat.
- 22 focused negative controls, all detected (`negative_controls.json`).

**Limits.** These are structural checks only. No owner certificate was rerun, and DZT-ART-NORMLAW-CHECK was not rerun here.
- DZT v0.19 was read in full. The v0.8 → v0.18 changes were read through the v0.19 text, its Appendices A and B, and the v0.18 and v0.19 release records.
- DYAD's OPEN 9 frontier line (near-cancellation of −13+15√3/2; exact large-p behaviour of |Q_p| OPEN) is a DYAD statement and is not changed. DZT's theorem is about \|N_+(M_p)\|, not \|Q_p\|.
- `BASELINE.md` was not changed while the candidate was under review. Its ATLAS row was set at acceptance (§5).

**Points for the change-focused review:**
1. The theorem node against DZT §6.3 (statement, scope, negatives, the one dependency, the certificate wording).
2. Removing `*DZT:mechanism HYP` and `*DZT:p40-flag`, rather than keeping them as historical lines. The Atlas holds current state; the owner's Appendix B and the theorem node keep the trace.
3. Retiring H3 together with DZT.Q1.
4. The denominator wording of AR15-013 and AR15-018 against DZT §6.3 "Correction of the imported note".

## 4. Decision

**Reviewer (ChatGPT, Atlas co-owner):** review `6004985736` on PR #349, head `46a4105ce9f77def098186763133e715fe27d9c4`, 21 Nov 2026 (11:41 UTC): **ACCEPT SCOPED, no blocking correction**, for the exact candidate bytes `483e6003…02df`. One round; the candidate is unchanged since it was built.

Confirmed independently by the reviewer:
- the hashes of the base, the candidate and the manifest;
- all 27 operations applied in order to the tag's bytes: each old span occurs exactly once, the 54 old/new digests match, and the result is byte-identical to the candidate;
- only DZT differs between the two manifests; the tagged DZT file equals the snapshot's;
- between the snapshot `357b963` and `main` `2788ebf` nothing changed under `dsn/`, `atlas/`, `pipes/` or in `BASELINE.md`;
- the six new retired entries are the dotted and spaced spellings of DZT.Q1, Q4, Q5, and the earlier 156 are kept.

Source fidelity, read against DZT v0.19 (§§1, 2, 5, 6.3, 7–9, Appendix B), its release record and DYAD v6.4.24 §6.11: the four criteria of §2.2 and the four review points of §3 all pass. That includes the removal of `*DZT:mechanism HYP` and `*DZT:p40-flag`, the retirement of H3 with DZT.Q1, and the denominator wording.

The reviewer's evidence boundary: the builder, the shared checker, the 22 focused controls and the owner's norm-law certificate were not run by the reviewer. Their results were read and remain producer records. The 17 unchanged owner DSNs were not reread.

**PI:** accepted. Mustafa, project conversation, 21 Nov 2026, 14:51 +03:00: "benimsiyorum" ("I adopt it"), in answer to the Atlas owner's question of the same conversation whether he adopts Atlas v0.15 with the bytes SHA-256 `483e60034ff3bb644216c5123d28b8bca253d3ba1b72cdf68bfb0056518d02df`. Accepted bytes: `atlas/RTG_STATE_ATLAS.md` with that SHA-256, the candidate reviewed in `6004985736`.

## 5. Publication (the PI executes)

1. `BASELINE.md`: the ATLAS row is set to v0.15, with the hash of §1 and this record. This was done on the branch, together with the decision.
2. Merge PR #349 into `main` with a merge commit, not squash.
3. Check the file hash on `main`, then create the annotated tag `atlas-v0.15` on that merge commit.
4. The Atlas owner writes the tag verification.

**Publication bytes** equal the accepted bytes: the Atlas has no status line that publication would change. A merge, a tag or a passing check is not an adoption.

## 6. Carried forward

- The four Atlas-side compound heads in D5 (from v0.14).
- The coverage check of the shared tool for non-Dyadic sources (done by builder assertions).
- DZT B1 (PR #347, question to RECOG): a later DZT edition enters through the next refresh.
