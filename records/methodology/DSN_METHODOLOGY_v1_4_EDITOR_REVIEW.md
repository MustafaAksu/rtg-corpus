# DSN Methodology v1.4 — editorial review of assembled draft

**Date:** 22 October 2026  
**Reviewer:** ChatGPT (Methodology revision editor)  
**Decision:** **ACCEPT WITH EDITS** — correct the two normative ambiguities below before PI adoption. No scientific owner result, proof grade, or OPEN is changed here.  
**Status:** SESSION / NONCANONICAL review of the DRAFT, not an adoption or release approval.  
**Target:** `dsn/DSN_METHODOLOGY.md` at commit `327629e300505a2a09465fb464afc1c5a4c138c2` (merged into `main` by PR #3, candidate SHA-256 as reported in the request: `d9f52d8c9f98055ab2fe815d9e8a57985862f868ec0adeb994930be7a9381505`). Baseline: `methodology-v1.3`, SHA-256 `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e`.

## 1. Evidence and limits

Read the full assembled v1.4 candidate on `claude/m14-review-request`, the review request, the previous editor review, and the relevant repository conventions. Inspected §1.1, §4.2, §12.2, §§13.1–13.9, Appendices A/B and the intervening methodology contracts. Retrieved commit `327629e` from GitHub: its changed-file list contains only `dsn/DSN_METHODOLOGY.md`. The request states +148/−76 lines and a single candidate SHA-256; these counts and the SHA-256 were not independently recomputed from downloaded bytes in this review. This is an editorial/consistency review, not a complete new governance-policy proof or verification of future compaction tooling.

## 2. Verdict on previous findings

| Finding | Disposition |
|---|---|
| **M14R-01** Git/history custody | **ACCEPT revised policy.** The later repository decision supersedes the earlier separate `<STUDY>_HISTORY.md` proposal. Immutable tagged commits + hash-pinned release records meet the preservation objective, provided tags and history remain retrievable and are never rewritten. See §3.2 below. |
| **M14R-02** qualified claim-block preservation | **SATISFIED in normative text** (§13.6 items 1–5). The per-block movement map, assumptions, domains, status and evidence are protected. The proposed checker is not thereby implemented or tested. |
| **M14R-03** correction versus compaction | **SATISFIED** (§13.6 two-stage intermediate baseline). Its hash must be recorded in the release record. |
| **M14R-04** live-file scope / aliases / pins | **SATISFIED** (§1.1); current negative constraints, historical owner pins used for present claims, OPEN obligations and functional appendices remain protected. |
| **M14R-05** DYAD closeout point-of-use edits | **OUTSTANDING IN ITS OWN FILE**. This is not a Methodology defect. Apply to `records/dyad/ATLAS_CLOSEOUT_DYAD_v6_4_20.md` before declaring the DYAD v6.4.21 pilot complete; do not count this item as already implemented. |
| **M14R-06** integrated size/evidence/adoption rules | **SUBSTANTIALLY SATISFIED**: §6.1 800-line rule reconciled, §1 summary consistency retained, evidence keys defined, and size reporting advisory. Two final editorial corrections concern §4.2 attribution and unadopted draft authority. |

The proposed `dsn_lint.py` and `check_compaction.py` require executable implementation, negative controls and a recorded coverage limitation before a pilot may report their gates PASS. Acceptance of their *contract* is not certification of their implementation.

## 3. Decisions on the four requested questions

### 3.1 Pilot authority — ACCEPT planned sequence; no blanket early activation

Adopt Methodology v1.4 **before** the DYAD v6.4.21 build/release if the PI approves it after these changes; then the pilot uses the adopted rule and needs no special authorization. Until that adoption, v1.3 remains governing for adopted corpus documents. A draft can be tested experimentally, but cannot be cited as generally operative. If the DYAD pilot must precede v1.4 adoption, record a **scoped PI pilot authorization**, including the affected sections, version, tests and non-transfer limits. The absence of a special pilot clause is not itself blocking if adoption precedes pilot execution.

**Optional §13.4 one-sentence insertion:**

> The DYAD v6.4.21 compaction pilot uses v1.4 only after v1.4 adoption; if executed earlier, its pilot-only use requires a separate recorded PI authorization and does not make v1.4 governing for other studies.

### 3.2 Historical provenance — ACCEPT Git-only model, with durability guard

Git annotated tags and byte-exact files give a stronger, simpler historical mechanism than a mutable cumulative history file. Explicit conditions: adopted release tags identify immutable commits; the release manifest records the adopted file's SHA-256 and predecessor tag; original evidence/packages remain retrievable; no force-push, tag movement, rewritten annotated tags or destructive history-pruning of published releases. Working notes can evolve via new commits; **released records and adopted source snapshots cannot be overwritten**. If a referenced artifact is external, its hash and durable locator must still be preserved—Git alone cannot recover data never committed.

§13.7's “no redundant copies” should be read as a **repository housekeeping rule**, not permission to discard required byte-complete external certificate bundles, original independently meaningful archival records, or provenance referenced by a published claim. The frozen-package exception already handles this; no mandatory new `HISTORY.md` is needed.

### 3.3 Working note versus immutable release record — sufficient concept, sharpen one sentence

A review/disposition/advisory note remains a **working record** until frozen as an adopted release input; subsequent working rounds may update its fixed path while the commit identifies the reviewed bytes. A release record becomes **immutable once adoption occurs**; discovered later facts must go in a dated, separately pinned addendum. Most importantly, if an adoption cites a working-note version, preserve the exact cited commit/blob (prefer a release manifest locator); updating the working path must never retroactively change what was reviewed.

**Proposed §13.7 addition immediately after “Release record”:**

> Working records may be updated at fixed paths, but every adopted release cites the immutable commit/blob of the exact working-note revision it relied on. Release records and accepted certificate identities are frozen on adoption; corrections are dated, hash-pinned addenda, not edits to the historical record.

### 3.4 Draft merged to `main` — REQUIRE explicit authority guard; prefer branch-only drafts

A `DRAFT` header is necessary but **not sufficient** for AI project synchronization, since §13.9 currently says AI contexts load `main` and that the tagged repository file governs. A main-branch draft may be mistaken for the governing DSN simply because its path is the canonical one. Accordingly:

- For **future releases**, keep draft modifications to `dsn/` on a named review branch; open PR; PI decision and release record precede merge to `main` and annotated adoption tag. This matches §13.1 and `CONVENTIONS.md`.
- The currently merged v1.4 **remains DRAFT**. Do not describe it as adopted; `methodology-v1.3` remains governing until v1.4's authorized adoption. No destructive rollback or forced rewrite is necessary solely to repair this staging mistake; either move the draft back to a branch in a normal follow-up commit or ensure selectors explicitly pin v1.3 until adoption.
- On repository synchronization, resolve authoritative scientific status using **adopted tags + adoption records**, not latest `main` content or header alone. A future synchronization checker should report `main` DRAFT and adopted tag mismatch as **PENDING / not canonical**, not silently ingest the draft as active.

**Replacement §13.9 (recommended):**

> AI working contexts may mirror files from `main` for navigation, but the governing edition of each canonical study is the most recent **PI/owner-adopted tagged release supported by its adoption record**. A file on `main` that remains DRAFT, REVIEW-READY, SESSION or otherwise unadopted is visible working material, not the active scientific/methodological authority. The project baseline records both the current working-tree edition and the governing adopted tag and reports any divergence. Draft DSN updates normally remain on review branches until adoption; PR approval, merge, repository visibility, a status header or a CI PASS alone do not create adoption. Historical imports remain pinned to their actual owner versions. No unadopted file is silently substituted for a tagged adopted source.

Also amend §13.1's repository paragraph if needed to state **decision → completed release record → merge/tag** as the normal order; avoid interpreting a proposed PR as release approval. This is a release-workflow restriction, not an endorsement of the current draft's presence on `main`.

## 4. Mandatory attribution fix — §4.2

The existing sentence wrongly attributes all namespace additions beyond v1.2 to adopted v1.3, although the `RRF` row is a v1.4 addition. Replace the entire paragraph after the namespace table with:

> The namespaces introduced beyond v1.2 in the adopted v1.3 registry are retained at their established owner scopes. **v1.4 additionally registers `RRF` for representation-profile/interface identifiers**; this recognizes an existing working registry and does not create or transfer scientific theorem ownership, certify a physical representation, or change programme maturity. Shortnames such as OFN are not automatic aliases of `RTG-OFN`; noncanonical `RER-*` keys remain local navigation keys, not scientific RIDs. Preserve historical nonstandard IDs with an explicit owner mapping rather than rewriting them.

Use “proposes to register” instead of “registers” **while the file is still a DRAFT** if the candidate's body is intended to report only currently operative rules. In the final adopted edition, “registers” is appropriate. The `RRF` namespace row itself is acceptable as a governance assignment; it is not scientific adoption.

## 5. Release disposition and acceptance tests

**ACCEPT WITH EDITS.** No re-examination of owner scientific certificates is requested.

Before finalization:
1. Correct §4.2 attribution and §13.9 source-selection / draft-authority ambiguity. Retain the precise §13.7 working-note freeze pointer; §13.4 pilot sentence is optional if v1.4 is adopted before the pilot.
2. Update the v1.4 release record to itemize M14-C01–C04, the added `RRF` namespace, repository governance and project-sync source selection. Recompute the candidate SHA-256 after any edits; preserve `327629e` and the preceding assembled draft as immutable Git history.
3. Verify by diff that these are governance-only edits: existing Methodology grammar, proof tags, import rules, scientific-owner identities and all scientific DSN files remain unchanged.
4. For DYAD v6.4.21 separately, implement M14R-05 at every conflicting closeout instruction; maintain the two-stage correction-versus-compaction test and record the actual checker negative controls.
5. PI/owner approval → immutable release record → `main` merge and annotated `methodology-v1.4` tag. Do not create the adoption tag or mark v1.4 ADOPTED from this review.

**No adoption, canonical Methodology modification, DYAD edit, merge or release tag is authorized by this review.**
