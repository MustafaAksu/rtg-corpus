# RTG State Atlas v0.14 — acceptance record (draft)

**Status:** DRAFT — second candidate, after review round 1 (review `5933660459`, ACCEPT WITH CHANGES; §3a). Not accepted. `atlas-v0.13` is the tagged Atlas until the PI accepts this candidate, the PR of branch `claude/atlas-v0.14` is merged, and the annotated tag `atlas-v0.14` exists and is verified.
**Object:** a derived, NONCANONICAL Atlas. Acceptance adopts no owner science.
**Recorded by:** Claude, Atlas owner, 17 November 2026, on branch `claude/atlas-v0.14`.
**Method:** Atlas Method v0.3 (`atlas-method-v0.3`).
**Decision that started it:** PI, project conversation, 17 Nov 2026, 08:30 +03:00: "v0.14'e şimdi başlayalım" ("let us start v0.14 now").

## 1. Object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md`, v0.14 candidate | `d34e5697ae47201133f513bce5f6b2b8438ed2f4e654fe33a73048a5ca7b1e85` (541,061 bytes, 1,545 lines) |
| first candidate (reviewed, superseded) | `acab587128ede70c779948288e97ceac76042bb6477d098f46aca7517937e5e4` (head `464cf02`) |
| base `atlas-v0.13` | `208ddd9622b2ea9d291b40dbc103d6eaa3f357aa0e23b2de6190df2c0f879045` (537,046 bytes, 1,545 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.3) | `a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f` |
| `evidence/atlas/v0.14/source_manifest.json` | `fe2faa915c5417ee0a76074a197f6c0f7875b9f5402c660979468416e0d643c4` |

Source snapshot: `main` `a5826ace61f14065b5c386efc817c883cdc775c0` (merge of PR #292). Two sources moved against the v0.13 manifest. The other sixteen are byte-identical and were not re-extracted.

| Source | v0.13 | v0.14 | File SHA-256 | Authority |
|---|---|---|---|---|
| TDRG | `tdrg-v2.12.15` | `tdrg-v2.13` | `98b4cba5ecb30f23f9dd97be27a7896191aa514ddefc402fd129ea673f0357f6` | `records/tdrg/TDRG_v2_13_RELEASE_RECORD.md` (PI adopted 16 Nov 2026, on the candidate bytes `6a4b94d5…de88`; the published file differs from them only in its *Document status* line) |
| AZ | `az-v0.9` | `az-v0.10` | `0cc84c9a587bab270624a824d5e004a327f20f41f0c03307e01a6725afe80e6e` | `records/az/AZ_v0_10_RELEASE_RECORD.md` (PI adopted 16 Nov 2026) |

Both tags are annotated. The builder asserts, for every source, that tag bytes = manifest hash = snapshot bytes and that no newer tag exists.

**Build:** `python3 -I evidence/atlas/build/refresh_v0_14.py`. It starts from the bytes of `atlas-v0.13`, applies 31 anchored operations (`evidence/atlas/v0.14/edit_log.json`) and replays them inside the run with an identical result. Two runs gave the same hash. **Evidence:** `evidence/atlas/v0.14/`.

## 2. What changed (31 operations; net 0 lines, +4,015 bytes)

| Kind | Operations |
|---|---|
| identity | 8 |
| TDR-G | 5 |
| AZ | 9 |
| reviewed items | 5 |
| Method §4.1 span deletions | 3 |
| pipes | 1 |

### 2.1 TDR-G v2.13 (maintenance edition)

The owner changes no result, RID declaration (81, the same set) or grade in §§2–9. The Atlas follows the parts it depends on:
- **D5 header:** Methodology v1.4 declared. §1 holds readouts with the owner grades, RIDs and pointers.
- **XFER-O08-01:** in TDR-G's own terms it is now "open, a separate decision of both owners" (TDR-G §7). This applies on the OFN star-shift node and on `TDRG-DEF-STAR`. The OFN admin-queue row keeps OFN's own record ("deferred to TDR-G v2.13"), with TDR-G's current state added beside it.
- **Owner's AZ pin** on `TDRG-THM-NARROW-BAND-EXCLUSION`: `az-v0.10`.
- **PROG.G6:** Programme v1.4 §9.2 records the TDR-G migration as planned for v2.13. The TDR-G edition of this snapshot is that migration.

### 2.2 AZ v0.10

- **New node `AZ-NUM-TOKRES-S2`** (`NUM·dx`, locator `@AZ§4.2.2`, `cert AZ-ART-TOKRES-S2`) records:
  - the full scope and convention;
  - the ten contrasts of the confirmatory family, each with its interval;
  - the coverage caveat of the intervals and the near-quarter control;
  - the owner's negatives, among them: no mechanism; no N-dependence or N-independence; the endpoints are not the same event at different N; not a TDR-G result; it does not widen S1.
- **Relations of the new node,** typed as for S1 (review `5915598211`, R1):
  - one dependency, `<TDRG-DEF-ORIENT`;
  - the phase law as context;
  - the census law as checked law.
  - The three TDR-G nodes name both diagnostics in their reverse relations. No AZ number is on a TDR-G node.
- **Pointers that named one diagnostic now name both:** AZ threads, the B ledger's local use, the AZ frontier (PROMO), and AZ.A5 in both rows.

### 2.3 Reviewed items (Method §7)

| # | Item | Change | Owner evidence |
|---|---|---|---|
| R1 | `*TDRG:policies` | One `NUM strong` for all branches → no common grade on the head; each statement carries the owner's grade: crystallization `[NUM]`, continuous inflation `[NUM]` (ms_bpe `[ALG]` definitional), avalanche `[HEUR strong]` (ms_bpe `[NUM]`), ordering `[NUM]`, multi-birth `[NUM strong]`. Locator `@TDRG§6.6`. | TDR-G §6.6. The v2.13 record (§3, "Typing of the summary") states that the old §1 gave all three branches one `[NUM strong]`; the Atlas node had taken that typing. |
| R2 | `*BIND3:d-table` | `ALG/NUM strong` → `ALG (sc: N=24, k=1; conv: v18 path orientation)` | TDR-G §6.12, the d-resolved anatomy: `[ALG]` `[scope: N=24, k=1]` `[conv: v18 path orientation]`. This was an Atlas fidelity error, not a source movement. |
| R3 | `*TDRG:crystallization` | The clause "no plateau through N=1080" leaves. The owner's grade question is recorded: the TDR-24B `[ADMIN]` note says `[HEUR strong]`, TDR-22b and the readouts say `[HEUR]`. The node keeps `HEUR` and the SG-6 ceiling. | The v2.13 record §3 calls the sentence stale: §6.8 extends to N=1440, and the owner no longer carries it. The grade question is in §6 of that record (found, not changed). |
| R4 | TDRG.G8 | **retired**: the footer chain, the Appendix A order and the v1.2 declaration are all resolved | `tdrg-v2.13`: one footer line, Appendix A in edition order, Methodology v1.4 declared (asserted by the builder) |
| R5 | METH.M1 | TDR-G leaves the list | `tdrg-v2.13` carries no compound grade tag (asserted) |

No L5 key is new. The cumulative retired list has 156 entries (154 at v0.13, plus TDRG.G8 in its two spellings). Dispositions of all D5 L5 rows and the other touched rows are in `evidence/atlas/v0.14/dispositions.json` (5 reworded, 1 retired, 5 retained).

### 2.4 Method §4.1 span deletions (3 operations, 48 bytes)

Three edition labels on TDR-G nodes, each asserted to be one contiguous deletion:
- `[COR v2.12.14]` on `TDRG-DEF-ORIENT` (the owner removed its own correction labels);
- "v2.12.14 wording;" on `TDRG-ALG-LEM-RETRIG`;
- "since v2.12.14" in D5.X1.

Labels that say what two editions state differently are kept (rule 4.1, third sentence): the superseded completion of v2.12.13, the "editions through v2.12.14" note on the star node, the consumer pins. Rule 4.7 was not applied.

### 2.5 Pipes

NUMGEN.N-I1 is restated at the snapshot `a5826ac`: 135 items in 20 inboxes, of which 72 are closed, 1 dispositioned and 62 open. The open ATLAS item (`pipes/ATLAS/20261116-AZ-v0-10-adopted.md`) is dispositioned on this branch (accept) and is closed after the tag.

## 3. Checks, limits, and points for the reviewer

**Shared checker** (`tools/atlas_check.py`, run with this edition's manifest, coverage map and cumulative retired list): 0 FAIL.

| Check | Result |
|---|---|
| sources | 72 PASS |
| coverage | 137 PASS |
| qualifiers | 4 PASS |
| links | 527 PASS, 10 documented-unresolved, 2 UNVERIFIED |
| artifacts | 121 PASS, 2 UNVERIFIED |
| keys | 156 PASS |
| wording | 13 WARN, as at v0.13 |

The 18 shared controls behave as expected.

**Builder assertions:**
- `tdrg-v2.13` declares the same RID set as `tdrg-v2.12.15`.
- No RID of `az-v0.9` is missing at `az-v0.10`.
- The two new AZ identifiers have exactly one declared home each.
- 20 owner-text facts hold. Among them: the S1 block is byte-identical at v0.9 and v0.10, and AZ's TDR-G pin is unchanged.
- Each §4.1 operation is one contiguous deletion.
- 27 focused negative controls are all detected (`negative_controls.json`).

**Limits.** These are structural checks only; no owner certificate was rerun.
- AZ v0.10 was read in its full diff against v0.9 (every changed line, §4.2.2 in full).
- TDR-G v2.13 was read through its release record, its stage-1 edit list and the four rounds of the Atlas row check, which reran both stages byte-identically. Where an Atlas line depends on the text, it was read at statement level. It was not reread in full.
- Four Atlas-side compound heads in D5 that the movement does not touch are left for a D5 opening: `*TDRG:TDR-24-factorization ALG/NUM`, `*TDRG:edge-builder ENG/ALG`, `*TDRG:slot-volume ALG/NUM strong`, `*NUMGEN:imp-DISC DEF/THM import`.

**Points for the change-focused review:**
1. R1–R5, each against its owner evidence. R1 and R2 change grades on the Atlas side; R3 removes a clause and records an owner question.
2. `AZ-NUM-TOKRES-S2`: is the statement the owner's (the ten intervals, the coverage caveat, the near-quarter control, the negatives)? Are the relation types those of S1?
3. The OFN admin-queue row: is it right to keep OFN's record ("deferred to TDR-G v2.13") beside TDR-G's current state, instead of replacing it?
4. Whether the four compound heads named under Limits should be handled now or at a D5 opening.

## 3a. Review round 1 (review `5933660459` on head `464cf02`, ACCEPT WITH CHANGES)

The reviewer independently confirmed several things: the base, candidate and manifest hashes; the 31 operations (62 old/new hashes); a byte-identical replay; the retired list (154 → 156); the ten S2 risk differences with their 20 bounds against AZ v0.10 §4.2.2; and the policy and d-table grades against TDR-G §§6.6, 6.12. R3–R5, S2, the OFN queue row and the four carried-forward heads were accepted.

| Finding | Change in the second candidate | Check |
|---|---|---|
| 1 — the head `*TDRG:policies NUM (graded per statement …)` could read as one grade for statements graded `[HEUR strong]`, `[ALG]` and `[NUM strong]` | The head is grade-neutral: `*TDRG:policies (no common grade; each statement carries the owner's grade, §6.6) \|`. The statements and their grades are unchanged. | A scope guard requires one `*TDRG:policies` line with no grade token after the key. Control W26 (a common grade put back on the head) is detected by that guard. |
| 2 — the BIND3 d-table lacked the owner's `[conv: v18 path orientation]` | The head is `*BIND3:d-table ALG (sc: N=24, k=1; conv: v18 path orientation) \|`. | The scope guard requires the convention. Control W27 (convention dropped) is detected by that guard. |

Both are changes to the text of operations AR14-014 and AR14-015. The number and order of operations are unchanged, so the ids AR14-001 … AR14-031 keep their meaning. The manifest is unchanged (`fe2faa91…43c4`). Two runs give the same hash.

## 4. Decision

Pending. To be completed with the reviewer's result and the PI's decision.

## 5. Publication (pending; the PI executes)

After acceptance: the BASELINE row for ATLAS; the merge (merge commit) and the annotated tag `atlas-v0.14` in one CLI block; the tag verification record; the closure of the ATLAS inbox item.

## 6. Carried forward

- The four Atlas-side compound heads in D5 (§3).
- The coverage check of the shared tool for non-Dyadic sources (done by builder assertions).
- Seven other multi-line identifiers; a comparator mode for heading renames; an AZ profile for `tools/orient.py`; F4.
- DZT: its first edition after the onboarding enters through the next refresh.
