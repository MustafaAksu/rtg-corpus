# DZT v0.19 — release record

**Status:** DRAFT, for review. **Not adopted.** `dzt-v0.18` governs until the PI adopts this edition and the annotated tag `dzt-v0.19` exists. This draft is completed at adoption (§9) and frozen then.
**Candidate file:** `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`, SHA-256 `00a6921437787e77bc8af5fcd50663fca4b4440ea564ea7c1054640d22464268`, 46,444 bytes.
**Predecessor:** v0.18, tag `dzt-v0.18`, SHA-256 `04581d1e8d8a187ec231d670d9639591e2b8d3aefb9834d5dd9f5cdf792a8dee`, 43,448 bytes (release record `records/dzt/DZT_v0_18_RELEASE_RECORD.md`).
**Prepared by:** the DZT co-owner (Claude), 20 November 2026. Second co-owner and independent reviewer: ChatGPT.

This record invents no hash, approval or review identifier. Steps after adoption are listed in §8.

**Authority.**
- **PI decisions, 20 November 2026, 00:55 +03:00**, project conversation, verbatim: "1- Evet 2- yeni RID açılsın 3- yeni sürümle girsin". They answer the three questions put to the PI after review `5983698371` (owner review record §8):
  1. **Yes:** the combined statement enters as `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]`.
  2. **A new RID** is opened for it.
  3. **It enters by a new edition.** That edition closes `DZT-OPEN-NORM-LAW`, retires the `[HYP]` mechanism and records the corrections of triage rows 4 and 5.
- **Basis:** the owner review `records/dzt/DZT_NORM_LAW_OWNER_REVIEW.md` (merged in PR #332, `6e70332`), with the second co-owner's review `5983698371` (ACCEPT SCOPED). It answers triage row 2 (a)–(d). These decisions are row 2 (e).

## 1. Bytes and how to rebuild

| Stage | SHA-256 | Bytes |
|---|---|---|
| base — `dzt-v0.18` | `04581d1e8d8a187ec231d670d9639591e2b8d3aefb9834d5dd9f5cdf792a8dee` | 43,448 |
| candidate | `00a6921437787e77bc8af5fcd50663fca4b4440ea564ea7c1054640d22464268` | 46,444 |
| published (status lines only) | pending adoption | — |

```bash
python3 -I evidence/dzt/v0.19/build_dzt_v0_19.py --out /tmp/c.md --log /tmp/log.txt
sha256sum /tmp/c.md                                       # 00a69214…4268
diff /tmp/log.txt evidence/dzt/v0.19/edit_log.txt         # empty
git diff dzt-v0.18 -- dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md
python3 -I evidence/dzt/norm_law_review/dzt_norm_law_review_check.py 4000 1000 100000   # PASS (about 100 s)
```

**What the builder does.** `evidence/dzt/v0.19/build_dzt_v0_19.py` reads the base with `git show dzt-v0.18:…` and asserts its hash. It applies 27 edits; each replaces a span that must occur exactly once (log: `evidence/dzt/v0.19/edit_log.txt`).

**It stops on:**
- a missing or repeated span;
- superseded wording left in the live text: the ACTIVE status line of `DZT-OPEN-0B-R`, the candidate mechanism, "no denominator law/formula is asserted", "any $k_p$ formula", "prove or reject the anomaly rule", "To be settled by the DZT-OPEN-0B-R";
- the loss of any of the 24 DZT RIDs or SG-DZT-1–8;
- a theorem RID declared other than once.

**No compaction stage.** The layout is already Methodology v1.4 (v0.18), so there is no second stage and no movement map. The edit is reviewed as a whole.

## 2. What changes

| Edits | Section | Change |
|---|---|---|
| S6a, S6b | §6.3 | **New record `DZT-THM-CASCADE-NORM-LAW`** `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` `[proof: written derivation]`: $\lvert N_+(M_p)\rvert=\ell(p)^2/2^{d_p}$ for every $p=4s\ge12$, with the proof in five steps (owner review §3, steps P1–P11). The sign is outside the statement. The heading's primary status becomes `[THM]`; its anchor is kept |
| S2a, S2d, S2e | §2 | `DZT-OPEN-NORM-LAW` closes (Methodology §5.2). The ACTIVE block is removed. Its finite-horizon statement and the correction of the imported note were already in §6.3; its `[HYP]` goes to Appendix B. The priority list and a one-line closed reference at the end of §2 name the result |
| S1a, S1b, H5 | §1, header | Readout of the theorem, which has one home, §6.3. The frontier now names B1 and B2. The status summary keeps four sentences |
| S6c | §6.3 | The `[OPEN]` paragraph "What survives the falsification … DZT-OPEN-0B-R …" is removed: the question it names is closed, and its other contents are stated at their homes (§6.3, §2 0A) |
| S6d, S6e | §6.3 | `DZT-ALG-CASCADE-ANOMALY-SET` is kept as the $p\le1000$ finite record, with a pointer to the theorem. The correction of the imported note now says that the general denominator law is the theorem |
| S6f, B | §6.3, Appendix B | **`[HYP]` mechanism retired** as `[SUPERSEDED]` (triage row 3). Reason: the gate is the order of $L^{s-2}$. The quadratic-subfield reading fails at $q=9$ ($p=72$) and at every $q=\ell^{2b}$ |
| S5 | §5 | High-risk row: the valid form is the theorem with its assumption. "Any $k_p$ formula" is replaced by "the law without its Dyadic assumption" |
| S7 | §7 | The PHASELAW row names its new consumer, the assumption of the theorem. Pin check: no Dyadic tag newer than `dyad-v6.4.24` |
| S8a | §8 | **New registry entry `DZT-ART-NORMLAW-CHECK`** for the review check (repository path, hashes, negative controls). The closing sentence of §8 distinguishes the recovered exit codes from this run |
| S9a, S9b | §9 | Provenance of the theorem (recovered notes S1, S2 with hashes; LIT note; owner and independent review; PI decision) and of the retired `[HYP]` |
| H1–H4, A, footer | header, Appendix A | Edition number and date; DRAFT status; one predecessor (`dzt-v0.18`, with hash); the v0.19 entry; the lineage line; a one-line footer |

**Corrections of triage rows 4 and 5.** The wrong sentences are in recovered texts that are not part of the lineage: S1 line 173, and v0.17 line 248 of `…_v0_17.md`. They are not in `dzt-v0.18`. v0.19 states the correct values in the proof, step (iv): $N(L+1)=2$ iff $p=2^k$; $I-1$ is not a unit, with norm $2^{\varphi(p)/2}$. The corrections themselves are recorded in the owner review §7. No Appendix B record is needed, since no DSN claim is retired by them.

**Unchanged:**
- every other claim and grade;
- the pins (`programme-v1.4`, `dyad-v6.4.24`, `az-v0.10`, `ofn-v0.12`, `methodology-v1.4`);
- maturity Level A (any change of level is a separate PI decision);
- the sign of $N_+$, which stays outside the theorem; the LIT sign count and pattern are not entered.

## 3. New identifiers

| RID | Kind | Home | Decision |
|---|---|---|---|
| `DZT-THM-CASCADE-NORM-LAW` | theorem | §6.3 | PI, 20 Nov 2026 (decision 2: "yeni RID açılsın"). The name was chosen by the preparer for review |
| `DZT-ART-NORMLAW-CHECK` | artifact registry entry | §8 | Routine registry entry for the check cited by the theorem; adopted with the edition |

The recovered identifiers `DZT-THM-CASCADE-ODD-SUPPORT` and `DZT-THM-CASCADE-DENOMINATOR` are **not** used. They remain names in the unadopted v0.9–v0.17 texts; §9 of the DSN names the proof notes by path and hash.

## 4. Checks

- **Builder.** Assertions PASS. A rebuild is byte-identical: the candidate and the log equal those of a second run.
- **`tools/dsn_lint.py --prev`** (informational):

  | Metric | `dzt-v0.18` | v0.19 candidate |
  |---|---|---|
  | bytes | 43,448 | 46,444 (+6.9 %) |
  | §1 words | 609 | 606 |
  | Appendix A editions | 3 | 4 (max 104 words) |
  | footer lines | 1 | 1 |
  | near-duplicate paragraphs | 0 | 0 |
  | new RIDs | — | 2 |

- **Mathematics.**
  - The theorem statement is the combined statement of the owner review §3, accepted in review `5983698371`.
  - The proof in §6.3 is a condensation of steps P1–P11.
  - `DZT-ART-NORMLAW-CHECK` verifies every norm in it exactly for $12\le p\le4000$ (check A1–A10).

## 5. Points for the change-focused review

1. The theorem block (S6b): statement, the five proof steps against owner review §3, the assumption tag and the scope ($p=4s\ge12$, $p=8$ excluded).
2. The closure form in §2 (S2a, S2d, S2e) against Methodology §5.2.
3. The removals S6c and S6f, and the Appendix B record.
4. The RID name `DZT-THM-CASCADE-NORM-LAW`.
5. The §9 provenance row: the credit to the LIT note and to the recovered notes.

## 6. Inbox (`pipes/DZT/`)

These dispositions are entered by the publication commit after adoption, with this record as pointer:

| Item | Disposition | Basis |
|---|---|---|
| `20261113-LIT-norm-law-proof-candidate.md` | `accept`, state `dispositioned` | The Proposition enters as part of `DZT-THM-CASCADE-NORM-LAW`. The `[HYP]` is retired as the LIT note proposed (its §4, Mechanism) |
| the other four items | unchanged | Dispositioned or closed at v0.18 |

## 7. Notices after the tag

Each notice is one item, filed after the tag `dzt-v0.19` exists. The receivers decide.

- **LIT** (`pipes/LIT/`), a report of use. Contents:
  - DZT verified the 13 Nov offer and adopted it as part of `DZT-THM-CASCADE-NORM-LAW`.
  - The corrections in the owner review §7 concern the recovered DZT notes, not the LIT note.
  - The status lines of the two LIT notes are out of date (owner review §7.5; triage row 19). This is a LIT action.
  - The sign note's real form and count were verified, and its pattern was checked to $p\le100000$. Neither enters DZT.
- **PROG** (`pipes/PROG/`): DZT now holds an all-$p$ theorem, conditional on `DYAD-THM-Q403-PHASELAW`. Level A is unchanged. IF18 and IF19 are unchanged.
- **NUMGEN** (`pipes/NUMGEN/`): the `[PROVENANCE]` paragraph names an audit-reported "v0.17" with all-$p$ odd-support and denominator theorems. Both statements are now covered by the adopted `DZT-THM-CASCADE-NORM-LAW`, which has a different RID and the explicit Dyadic assumption.
- **DYAD** (`pipes/DYAD/`): the closed form of `DYAD-THM-Q403-PHASELAW` is the assumption of a DZT theorem. This is for Dyadic's consumer register. Nothing is asked.

## 8. Steps, in order

| # | Step | By | State |
|---|---|---|---|
| 1 | Candidate, checks, this draft | DZT co-owner | done (this PR) |
| 2 | Change-focused review (§5) | second co-owner | requested |
| 3 | Adoption decision (§9) | PI | pending |
| 4 | Publication commit on this branch: status lines only, by a reviewed transform as for v0.18; the dispositions (§6); this record completed and frozen; the `BASELINE.md` DZT row | DZT co-owner | pending |
| 5 | Merge by a merge commit (not squash) | PI | pending |
| 6 | Annotated tag `dzt-v0.19` on that merge commit | PI | pending |
| 7 | Notices (§7); lane in the orientation note | DZT co-owner, after the tag | pending |
| 8 | Tag verification and Atlas refresh | atlas owner | pending |

## 9. Adoption decision

Not given. To be completed with:
- the PI's verbatim decision and its time;
- the adopted object (candidate hash and published hash);
- what the adoption covers and does not cover.

Order: decision → this record → merge → tag.
