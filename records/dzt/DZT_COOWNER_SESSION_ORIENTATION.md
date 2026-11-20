# DZT — Co-owner Session Orientation

**[SESSION] Operational working memory of the DZT stream (Dyadic Arithmetic-Resonance Transform). It has no scientific or release authority.**

Created 16 November 2026 by the Atlas owner (Claude) at the PI's request. The stream has had no owner session since June 2026 and was never opened after the repository baseline of 22 October 2026. The shared sections below are a starting state for the DZT owners to take over and correct. From the first DZT checkpoint on, the DZT owners maintain them (CONVENTIONS §9).
**Owner per `BASELINE.md`:** PI. Co-owner lanes are added by the sessions the PI assigns.
**Decision that opened this note:** `records/atlas/ATLAS_ADVISORY_STREAM_ONBOARDING_20261116.md` §6 (PI, 16 Nov 2026, 16:19 +03:00: "DZT ile başlayalım").

## ENTRY — discovery and authority

Read **from GitHub**, repository `MustafaAksu/rtg-corpus`, fixed path `records/dzt/DZT_COOWNER_SESSION_ORIENTATION.md` on `main`. Project synchronization does not include `records/`, `pipes/`, `evidence/` or `tools/`. Start with:
- `CONVENTIONS.md`;
- this note;
- `BASELINE.md`;
- `pipes/DZT/INDEX.md`.

Failure to access a source means **UNVERIFIED**, not an empty queue.

The governing DZT edition is the adopted tag `dzt-v0.19` (file `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`, SHA-256 `2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce`; merge `5f3b205`; release record `records/dzt/DZT_v0_19_RELEASE_RECORD.md`). Its predecessors are `dzt-v0.18` (`04581d1e…8dee`, record `records/dzt/DZT_v0_18_RELEASE_RECORD.md`) and `dzt-v0.8` (`cad20982…92ff2`, tagged on 22 October 2026 from the project copy, BASELINE "PI" only, no release record). Memory of earlier chats, project copies and file headers are not authority. The reading list below is dated 16 November 2026 and describes v0.8.

## FIRST QUESTION — DZT editions after v0.8 (before any triage)

A record in the repository says DZT went further than the tagged file. It is `upload/numgen-records/RTG_NG_PROGRAMME_REVIEW_AUDIT_v1.md` (lines 6, 13, 49–64, 175, 192, 205), a NUMGEN-held audit uploaded on 26 Oct 2026. It reports, from "DZT v0.8 (project copy) + DZT v0.17 session record", that:
- DZT reached editions **v0.9–v0.17**, ending in a "closure freeze v0.17";
- the corrected anomaly law was **closed at `[THM]`** there, as `DZT-THM-CASCADE-ODD-SUPPORT` (the odd part of the numerator of N₊(M_p) is ℓ² iff p = 8ℓᵃ with ℓᵃ ≡ 1 (mod 4), otherwise 1; all p);
- **`DZT-THM-CASCADE-DENOMINATOR`** gives d_p = φ(p)/4 + [p=2ᵏ] + [p=3·2ᵏ], all p;
- the audit reproduced both from the imported closed form at 60 points p = 12…248 (`ng_review_dzt_independent_audit_v1.py`, 0 mismatches);
- it recommended uploading DZT v0.17.

No DZT file after v0.8 is in the repository. NUMGEN (§ provenance, DSN line 2742) and OFN (RF-O08-13) both record this and keep citing v0.8.

This decides the shape of the whole cycle:
- **If the v0.9–v0.17 files (or at least v0.17 and its session record) exist:** they arrive unchanged on an `upload/dzt-…` branch and are hash-checked (CONVENTIONS). The PI then decides how they enter. Options: a review and adoption of v0.17 as the next governing edition, or a corrections edition of v0.8 that records them as history. The triage is done against them, not against v0.8.
- **If they cannot be found:** the cycle starts from v0.8. The two theorem statements are then only reported by a third party (EV-SRC-REPORTED). DZT-OPEN-0B-R / DZT-OPEN-NORM-LAW stays as v0.8 states it, and the LIT offer below is the live route to the same result.

Until the PI answers, nothing beyond reading (BOOTSTRAP 1) starts.

**Answered (17–18 Nov 2026):** v0.1–v0.17 exist, without v0.6, and were received unchanged (PR #289; plain files PR #308). Reading record: `records/dzt/DZT_RECOVERY_READING_RECORD.md` (PR #309). The PI chose the mixed route: `dzt-v0.8` is the edition basis and v0.9–v0.17 are sources to verify (decision D1, `records/dzt/DZT_REACTIVATION_TRIAGE.md` §7).

## LIVE_STATE — generated, never copied here

`git fetch origin --tags && python3 -I tools/orient.py DZT --tag-prefix dzt-v --file dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md --paths dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md records/dzt pipes/DZT`

Without a shell: obtain the same facts through the GitHub connection and say what could not be covered. The facts are the tag, the file hash, open PRs touching these paths and the `pipes/DZT/` states.

## WHAT CHANGED AROUND DZT SINCE v0.8 — reading list, dated 16 November 2026

A map for the first reading, not a substitute for it. Every row is to be verified at the named tag.

| DZT v0.8 states or pins | Now | Read |
|---|---|---|
| DSN Methodology v1.2 | `methodology-v1.4`; repository rules in `CONVENTIONS.md` (branches, PRs, release records, tags, pipes, §9 working memory) | `CONVENTIONS.md` in full. Methodology §8.4: compound grades such as `[THM/ALG]` and `[ALG finite horizon]/[HEUR]` are unpacked |
| Programme Overview v1.1 | `programme-v1.4`. §9.2: the maintenance sequence was **not executed** for DZT; IF18 (Dyadic → DZT, pin v6.4.8.1) and IF19 (DZT → Dyadic feedback, open); §6.7: AZ and DZT are not to be merged for shared vocabulary | Programme v1.4 §§6.7, 9.2, the interface table |
| Dyadic v6.4.8.1 (all §7 `[import-ref]` rows; "source of truth for all OPEN 9 arithmetic") | `dyad-v6.4.24`. **Appendix F** classifies every Dyadic-pattern string of DZT v0.8 §7 and creates no alias. Repins: `DYAD-THM-Q403-PHASE-ALLP` → `DYAD-THM-Q403-PHASELAW`; P1, REALITY, LEAD, R and CF-Q403 are components of PHASELAW without separate RIDs; `DYAD-ALG-PHASELAW` is a historical label; `DYAD-ALG-CASCADE-P12` is unmatched (the p=12 value −13+15√3/2 has no RID); `DYAD-ART-CASCADE-Q4-03` matches `DYAD-ART-Q403-EXTRACT` by content, without byte identity; `DYAD-OPEN-B5-ALLP` is closed by `DYAD-ALG-B5-ALLP-NONVANISHING`; VANISH-B2/B3/B4 are three RIDs. §2 OPEN 9: p=12 value with the sign restored (v6.4.20) | `pipes/DZT/20261103-DYAD-notices-n16-n21.md`; Dyadic Appendix F, §6.11, §2 OPEN 9, Appendix E (RAW-CUBIC caveat) |
| AZ v0.6 (quarantined companion; SG-DZT-1) | `az-v0.10`. Thread C and the static-geometry reading of the `4|q` rule are unchanged; AZ asserts no relation to the DZT anomaly set (SG-AZ-7). v0.9–v0.10 add the AZ-owned diagnostics `AZ-NUM-TOKRES-S1/S2`, which also state "no relation to Dyadic/DZT q = 4" | `pipes/DZT/20261111-AZ-v0-7-adopted.md`, `…20261112-AZ-v0-8-adopted.md`; AZ §3 SG-AZ-7, §4.2.1–4.2.2 "what it is not" |
| OFN v0.7 | `ofn-v0.12`. RF-O08-13 keeps DZT v0.8 as the supplied version and does not install older review deductions as DZT corrections | OFN RF-O08-13 |
| — | Number Genesis v1.21 imports nothing from DZT. Its provenance block (line 2742) records the "v0.17" report | NUMGEN line 2742; the audit memo named above |
| DZT §8 artifacts (seven scripts, `[ENG]` exit codes) | **none of them is in the repository**; only the NUMGEN audit script `upload/numgen-records/ng_review_dzt_independent_audit_v1.py` is | DZT §8 |

**Atlas findings on DZT** (`atlas-v0.13`; noncanonical, the owner decides):
- **DZT.Q1 D-RID:** the §7 strings above.
- **DZT.Q4 D-GRADE:** compound grades; ANOMALY-SET carries ALG and HEUR in different sections.
- **DZT.Q5 D-SCOPE:** the §1 table runs p=12–52 against §6.3's p=12–64; §1 says "pure 2-powers except p=40" without the p≤1000 correction in the same paragraph.
- **AZ.A5:** no link between the DZT anomaly set p=8ℓᵃ and AZ's `4|q` rule.

Advisory row 2 of `records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md` (PI: "with the stream's rework") is DZT.Q1. DZT.Q1 accounts for most of the documented-unresolved links in every Atlas check.

**Inbox** (`pipes/DZT/`, four open items; the receiver decides, a notice is not an adoption):
- DYAD notices N16–N21 (3 Nov): the Appendix F crosswalk, the p=12 value, VANISH-B2, the RAW-CUBIC caveat.
- AZ v0.7 (11 Nov) and AZ v0.8 (12 Nov): the companion pin and SG-DZT-1. A later AZ notice may follow.
- **LIT offer (13 Nov):** an elementary all-p proof candidate, with a closed form, for the corrected rule (DZT-OPEN-NORM-LAW / DZT-OPEN-0B-R). The statement is N₊(M_p)² = 2^(−φ(p)/2)·D(p)/(B(p)⁴C(p)), with odd support exactly at p = 8ℓᵃ, ℓᵃ ≡ 1 (mod 4). The note is in the private repository `rtg-lit` at commit `8e2fb5cb…`, co-owner reviewed. It asks DZT for a verdict and leaves the grade and the fate of the `[HYP]` mechanism to DZT. **Compare it with the two theorems reported for v0.17 before anything else is decided.** The LIT denominator exponent should equal the v0.17 formula d_p; that check is one line.

## BOOTSTRAP — messages for the DZT session, in order

Each message asks for one bounded product. The PI sends the next one after reading the result.

**0. To the PI (before BOOTSTRAP 2):** locate DZT v0.9–v0.17 and the v0.17 session record, and the scripts of DZT §8, if they exist. Hand them over unchanged; they go to an `upload/dzt-…` branch with a hash list.

**1. Entry and reading (no edits).**
> Act as DZT co-owner (stream: Dyadic Arithmetic-Resonance Transform). From GitHub `MustafaAksu/rtg-corpus`, read `CONVENTIONS.md` and `records/dzt/DZT_COOWNER_SESSION_ORIENTATION.md`. Then read the DZT DSN at tag `dzt-v0.8` in full, the NUMGEN audit memo named in the note's FIRST QUESTION, and the sources in the note's reading list. Verify governing sources and live work yourself. Report:
> (a) the governing edition, what the record says about v0.9–v0.17, and what you could not verify;
> (b) a drift table: every pin, import and cited identifier in DZT v0.8 against the current adopted tags;
> (c) the open inbox items in your own words;
> (d) whether the LIT offer and the two v0.17 theorems state the same law, as far as the texts allow.
> Temporary files and clones, hashes and the reviewed reporter are permitted. Nothing is edited.

**2. Triage (one record, on a branch; after the PI's answer to question 0).**
> For every drift row, inbox item and Atlas finding on DZT, classify the effect on DZT: changes a claim or grade / identifier or pin only / none. If v0.9–v0.17 were supplied, triage against them and state how they relate to v0.8. Propose a disposition for each row. Split them into (i) a corrections or synchronization edition with no new science and (ii) items that need new work, such as a verdict on the LIT proof or a grade for the norm law. Write this as `records/dzt/DZT_REACTIVATION_TRIAGE.md` on a branch of yours and open a PR. Fill your lane in this note. Nothing is adopted by this record.

**3. Edition (after the PI's decision on the triage).**
> Prepare the next DZT edition, limited to what the PI decided: list (i) first, then answers to the inbox. No new scientific claim and no grade raised unless the PI put it in scope. Follow CONVENTIONS for the edit, the PR, the review request, the release record and the reply items in the senders' pipes. The PI merges and tags.

**4. Own work (only after that edition is adopted).**
> State the DZT frontier as it stands and propose the next one to three actions with acceptance criteria. The Methodology v1.4 migration is a separate, PI-decided edition unless the PI joins them; do not mix it into scientific work.

## OWNER / CO-OWNER LANES

*(Each session writes its own lane under its own heading with a check stamp. The lane covers: goal, last durable work, decisions held, tried and set aside, evidence, resume, next 1–3 actions, reopen trigger.)*

### CO-OWNER LANE — Claude

**Checked:** 20 November 2026, 12:40 +03:00. `main` `5f3b205` (merge of PR #334). Tag `dzt-v0.19` (annotated, on `5f3b205`) governs; file `2b959f46…f6ce` equal on `main`. `pipes/DZT/`: five items, none open (the AZ v0.7 item `closed`, the other four `dispositioned`). Open DZT PR: the v0.19 notices (branch `claude/dzt-v0.19-notices`).
**Role:** DZT co-owner, preparer. The second co-owner (ChatGPT) is the independent receiving reviewer. The PI decides adoption and publication (D6).
**Shared sections:** this lane's session updated the governing-edition paragraph and PI_PENDING on 20 Nov.
**Goal / current question:** triage list (ii), row 6: the B1 re-examination, starting from the dynamical object. Each item enters an edition only by a separate PI decision.
**Last durable work:** PR #308, #309, #317, #321, #319, #327, #332, #334 (merged); tags `dzt-v0.18`, `dzt-v0.19`. `DZT-THM-CASCADE-NORM-LAW` adopted (v0.19). Notices to LIT, PROG, NUMGEN and DYAD on `claude/dzt-v0.19-notices`.
**Decisions held:** PI, 18 Nov, 00:00 +03:00, D1–D7 (triage §7). PI, 18 Nov: scope list (i), number v0.18. PI, 19 Nov, 15:03: v0.18 adopted. PI, 20 Nov, 00:55: norm law `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]`, new RID, by a new edition. PI, 20 Nov, 12:19: v0.19 adopted.
**Tried and set aside:** treating any recovered variant as final from its file name, size or time stamp (no basis; RR §4). Reusing the DZT script outputs as signed norms: they are `sqrt(abs)` (RR §9.2). Reading the imported note's $2^{-\varphi(q)}$ as right in value on the anomaly set (only its exponent is; review `5984329391` R1).
**Evidence:** `evidence/dzt/v0.18/`, `evidence/dzt/v0.19/`, `evidence/dzt/norm_law_review/`; RR §§2–9; recovered files under `upload/dzt-recovery-20261116/received/`.
**Resume:** the LIVE_STATE command; v0.19 record §7 (notices); triage rows 6, 7, 12, 17.
**Next 1–3 actions / acceptance:**
1. Answer the review of the notices PR; after the PI's merge, the LIT, PROG, NUMGEN and DYAD inboxes hold the items. Acceptance: `tools/pipes_index.py --check` OK.
2. Row 6 (ii): the B1 re-examination. Define the dynamical object B1 is about, checked against Dyadic `dyad-v6.4.24`, with no recovered B1 result carried (the 47/54 value is `DYAD-ALG-RAW-ANGULAR-MEAN`, not a pointwise recurrence). Acceptance: a written object definition in `records/dzt/`, reviewed.
3. Rows 7 and 12 (channel universality), then row 17 (targeted search for missing sources).

**Reopen trigger:** a review of the notices PR; a new `pipes/DZT/` item; a receiver disposition on a DZT notice; a Dyadic edition that changes §6.5, §6.11 (the closed form assumed by `DZT-THM-CASCADE-NORM-LAW`) or Appendix D/F; any material found by the row 17 search.

## PI_PENDING

- 16 Nov 2026, 16:19 +03:00: the PI decided to start the onboarding with DZT; the other onboarding questions are deferred (advisory §6).
- **Done, 17–18 Nov 2026:** question 0 answered (PR #289, #308, #309). D1–D7 decided by the PI on 18 Nov, 00:00 +03:00 (triage §7). Triage merged (PR #317). Scope (list (i)) and number (v0.18) decided by the PI on 18 Nov.
- **Done, 19 Nov 2026, 15:03 +03:00:** v0.18 adopted by the PI (release record §12).
- **Done, 19 Nov 2026:** PR #319 merged by the PI (`9a75aaa`), annotated tag `dzt-v0.18`.
- **Done, 20 Nov 2026, 00:55 +03:00:** norm-law grade, new RID, entry by v0.19 (v0.19 record, Authority).
- **Done, 20 Nov 2026, 12:19 +03:00:** v0.19 adopted (v0.19 record §9).
- **Done, 20 Nov 2026:** PR #334 merged by the PI (`5f3b205`), annotated tag `dzt-v0.19`.
- **Open with the PI:** none for DZT beyond the notices PR.
- No CLI block is pending for DZT.
