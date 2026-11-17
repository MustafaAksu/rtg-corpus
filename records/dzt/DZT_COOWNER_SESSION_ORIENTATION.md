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

The governing DZT edition is the adopted tag `dzt-v0.8` (file `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`, SHA-256 `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2`, equal on `main`). It has **no release record**. The tag was created on 22 October 2026 when the corpus moved to Git, from the project copy, and BASELINE verifies it as "PI" only. Memory of earlier chats, project copies and file headers are not authority.

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

**Checked:** 18 November 2026, 00:10 +03:00. `main` `6c5a74a`. Tag `dzt-v0.8` governs (`cad20982…92ff2`). `pipes/DZT/`: four items open. Open DZT PR: this lane's triage PR (branch `claude/dzt-triage`).
**Role:** DZT co-owner, preparer. The second co-owner (ChatGPT) is the independent receiving reviewer. The PI decides adoption and publication (D6).
**Shared sections:** this lane's session updated FIRST QUESTION ("Answered") and PI_PENDING on 18 Nov.
**Goal / current question:** BOOTSTRAP 2 is done once the triage is reviewed. Next comes BOOTSTRAP 3, the edition (list (i), two stages), with the (ii) work running alongside.
**Last durable work:** PR #308 (recovery placed as plain files, `5fa09bd`); PR #309 (reading record and variant diffs, `b4ebe61`); triage `records/dzt/DZT_REACTIVATION_TRIAGE.md` (branch `claude/dzt-triage`, unmerged).
**Decisions held:** PI, 18 Nov, 00:00 +03:00, D1–D7 (triage §7): mixed basis on v0.8; no retrospective tags, v0.6 `NOT RECEIVED`; LIT reviewed this cycle, tables labelled $\lvert N_+\rvert$, no sign OPEN; B1 re-examined, freeze = unverified history; Methodology v1.4 in the same cycle as Stage 2; Claude prepares, ChatGPT reviews; targeted search.
**Tried and set aside:** treating any recovered variant as final from its file name, size or time stamp (no basis; RR §4). Reusing the DZT script outputs as signed norms: they are `sqrt(abs)` (RR §9.2).
**Evidence:** RR §§2–9; session sign check script and output reproduced in RR §9.3; recovered files under `upload/dzt-recovery-20261116/received/`.
**Resume:** the LIVE_STATE command; the triage PR and its review; triage §6 for the split, §3 for acceptance criteria.
**Next 1–3 actions / acceptance:**
1. After the triage review and the PI's scope and number decisions (triage §8): build Stage 1 by an assertion-gated script (rows 1, 8–11, 13, 16), then record the intermediate hash. Acceptance: the per-row criteria of triage §3.
2. Row 2 (ii): an owner proof review of the norm law against the recovered notes and the LIT note, written to `records/dzt/`. Acceptance: criteria (a)–(d) of row 2. Grade left to the PI.
3. Row 6 (ii): a note fixing the B1 dynamical object at the Dyadic tag before any B1 result is reconsidered.

**Reopen trigger:** a review point on the triage; a new `pipes/DZT/` item; a Dyadic edition that changes §6.5, §6.11 or Appendix D/F; any material found by the row 17 search.

## PI_PENDING

- 16 Nov 2026, 16:19 +03:00: the PI decided to start the onboarding with DZT; the other onboarding questions are deferred (advisory §6).
- **Done, 17–18 Nov 2026:** question 0 answered (PR #289, #308, #309). D1–D7 decided by the PI on 18 Nov, 00:00 +03:00 (triage §7).
- **Open with the PI:** after the triage review, the scope of the next edition (list (i)) and its number (triage §8).
- No CLI block is pending for DZT.
