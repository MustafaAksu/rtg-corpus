# RER r4.2 — independent receiving delta review (19 October 2026)

**Document state:** Review note; NOT owner adoption, RER freeze, DSN change or PI authorization. **Basis:** exact archive `RER_v0_2_DRAFT_r4_2_PACKAGE_20261019.zip`, original r4.1 archive and locally supplied Triadic r2, Methodology v1.3. **Source reading:** complete 99-line diff and 14 edit locations; RER §0–1, affected §6 RER-F3-N7N8, §7/§9 and checker/build scripts; relevant owner source headers/claims. Historical r3.1 tables inspected for preservation, not full original science reproduction.

## [SESSION] Integrity and deterministic reconstruction

- ZIP SHA-256: `c0c3f325c0326d5e7004bcbc9a8651cbf7837c9879b19bf25d0e9e21b44bbbf8`.
- r4.2 registry SHA-256: `a443cc8233516f385818a7fffb010dcbacda09825edb2eccd5debd025ed77079`.
- r4.1 verified base SHA-256: `19f16436a747a8ef836f0cb46e4374318dbbbaa75a6540f3ef61130936e3be42`. The packaged base matches r4.1 of the previous RER archive byte-for-byte.
- Manifest 12/12; `check_r4_2_draft.py --tamper`: 16/16 gates PASS, four independent mutations each rejected, r4.1 fails all U1–U4. Builder/reversal/r3.1 contract-table preservation checks pass.

## [SESSION] Scientific delta assessment

- **R41-SUM-01 corrected** in header and §1; the preserved r3.1 table's old closure cell at §6 line 698 has an explicit adjacent r4.2 current-use overlay (line 701). RER-F3-N7N8 §6 finite-order and Stage-2 current-gate statements are updated at lines 702,746,748. G5 owner-import grade and assumptions, G6 OPEN, the four registry record contracts and scientific grades are unchanged.
- **E2:** r4.2 declares Genesis v2.8.8 adopted 19 Oct, but states evidence `OWNER-REPORTED` and pins theorem imports to the directly supplied, adopted Genesis v2.8.7. The v2.8.8 source bytes/release record are not mounted here. The claim that §6.3a–b and SG-15/16 are byte-identical has **not** been independently verified in this receiving session; r4.2 correctly retains the owner-reported provenance label. No v2.8.8 theorem upgrade inferred.
- **Stage-2:** reviewed one-step TM lemmas are RECEIVER-REPORTED, not a global proof or engine deployment. `a≤1` decided for validator but not yet installed in active RTG workspace; K=6 pilot 8/8 subset, K=8 one received, regional K_N and global certificate OPEN.

## R42-U5 — minor current-use wording repair requested

Two live statements still require one-line clarification; neither calls for rerunning proofs or changing grades:

1. **§6 line 749** says `[OPEN] independent proof review and separately authorized full governing-region work`. Read alone, the unspecific *independent proof review* appears still open although lines 701/702/748 explicitly report the scoped independent Taylor-model lemma review completed. Distinguish **future end-to-end governing-region certificate review** from the **already completed scoped one-step lemma review**. The new U4 gate checks the literal phrase `lemma review` and does not detect this unnamed statement.
2. **§6 line 753** begins `Next test: (r4.1)` although it appears in the r4.2 current technical body. This is an editorial current-version pointer; say `r4.2 current use`. Retain original r4.1 under §9 history.

A **non-installed proposal** is in `R42_U5_EDITORIAL_PROPOSAL.diff`. Frozen r3.1 contract tables and older revision entries remain untouched. The proposal is not part of accepted r4.2 bytes.

**Receiving disposition:** `SCIENTIFIC DELTA ACCEPT SCOPED; MINOR CURRENT-USE CORRECTION REQUESTED (R42-U5)`. Do not claim final r4.2 receiving closeout until this wording is ruled by the preparer/co-owner. Not a change to RER theorem status or scientific owner grade.

## [SESSION] Guard A1 decision and handoff

- Correct route: shared record validator, not engine assertion. Require six stages with finite decimal-string `edge_bound` and exact `0≤a≤1`; no float tolerance. Original SHA `8af038c85241d889b8f50d7e5da18cf8a1b572d6e8f544d3efc1080ab811746c`, candidate SHA `827c64598a36413c930aa290dbea724df5105a7f3f35db8dc8099e1051bd07cf`.
- **Independent receiver reruns:** record-guard checks 54/54 PASS (nine pilot rows retained; 54 per-step records), infrastructure regression **41/41 PASS under proposed A1 contract**, exit 0. Regression executes one K=4 coarse retry, not K6/8 pilot recomputation or full regional sweep. Detatched receipt pins contract revision/hash.
- **Installation** is *not* performed in RTG's live working system. A transfer kit with complete replacement contract, unified diff, hash-checked explicit opt-in installer, test fixtures, receipt, regression log and SHA256 manifest is `STAGE2_A1_GUARD_HANDOFF_20261019.zip`. The kit's own unpacked tests/install dry run and temporary installation were successfully checked. Historic hash-pinned source archives should remain immutable.

## PI decision: Triadic v1.6.1

[SESSION: proposal, not PI approval] Triadic r2 scientific receiving review was already accepted. Prefer a **metadata-only owner release** once PI explicitly authorizes it. Separate v1.6.1 adoption record; mark inherited v1.6 acceptance/header/footer as historical; include a dated statement that Genesis v2.8.8 adoption is owner-reported and reviewed v2.8.7 theorem pins remain deliberate pending byte-level source comparison/next maintenance. Avoid asserting unverified exact byte equality as independently established. No r3 repin is required to publish the already-reviewed v2.8.7 imports under Methodology v1.3. No authorization to publish arises from this co-owner review.

**Not performed:** no RER draft modifications; no Triadic owner release/adoption; no RRF import acceptance; no original exact-kernel replay; no G6 closure, degree-7 graph completion, or Stage-2 regional sweep.
