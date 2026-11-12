# Discrete Genesis (TDR-G) v2.12.15 — Release Record

**Status:** DRAFT. The candidate is built and checked. It awaits the ChatGPT co-owner's change-focused review, the atlas owner's row check and the PI's adoption.
**Date:** 12 November 2026
**Prepared by:** Claude, TDR-G co-owner session `claude01SKePJ` (branch `claude/tdrg-v2-12-15-stage1`).
**Edition:** v2.12.15, a scientific scope edition built in one stage. Methodology v1.2 stays as declared; there is no layout compaction and nothing is rerun. The Methodology v1.4 migration remains v2.13.
**Predecessor:** `RTG_DISCRETE_GENESIS_DSN_v2.12.14`, tag `tdrg-v2.12.14`, SHA-256 `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`.

Fields marked *(to be filled)* depend on steps that have not happened yet. Every hash below was computed on the branch files by `evidence/tdrg/scripts/fill_tdrg_v2_12_15_record.py`; none is typed by hand.

## 1. Authorization and reviews

| Step | Source | State |
|---|---|---|
| Inbox items | `pipes/TDRG/` items of 29 Oct, 30 Oct, 4 Nov, 11 Nov and 12 Nov 2026 | read at `main` `65491fa` |
| Owner records | `records/tdrg/TDRG_OWNER_INBOX_DISPOSITION_20261112_claude01SKePJ.md` (§§1–4; round 2, §7, after the ChatGPT review) | merged (PR #243, `e8d317d`) |
| ChatGPT co-owner | triage and review of 12 Nov 2026, relayed in the session; its agreement and its requested limits (N4 as a scope correction, TDR-6 PARTIAL, evidence scope) are recorded in §7 of the owner record | not a repository record |
| PI decision | "v2.12.15 bilimsel sürümü başlatılabilir"; "OFN v0.11 ve AZ v0.7 bildirimlerini `no action` ile kapatılabilir"; "PR 243 merge edildi" (12 Nov 2026, 16:37 +03:00, in the session) | given |
| Change-focused review | ChatGPT co-owner | *(to be filled)* |
| Row check and rerun | atlas owner | *(to be filled)* |
| Adoption, merge commit, tag `tdrg-v2.12.15` | PI | *(to be filled)* |

## 2. Identities

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v2.12.14) | `git show tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md` | `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392` |
| **Candidate v2.12.15** | `dsn/RTG_DISCRETE_GENESIS_DSN.md` | `429a57f220b32ccc6559abc26f146d5db4fbf081bcd02529f286723f37b54f19` |
| Builder | `evidence/tdrg/scripts/build_tdrg_v2_12_15.py` | `e14f465f9e3a5f6cb7b7d606cc6366b55d88531bacc774203efbb1926bbb526d` |
| Checker | `evidence/tdrg/scripts/check_tdrg_v2_12_15.py` | `b633738baacc99e70ccff18bbf1102d716d63ea30c75abb70d24d807565b52d4` |
| Edit log (32 edits) | `evidence/tdrg/v2.12.15/edit_log.json` | `35824f8c3deebee23ae0413efecc1e3cbf4ff062c828bd640058d67f462d0815` |
| Checker output (gates) | `evidence/tdrg/v2.12.15/check_output.txt` | `43e90a0abc36be0c02a694c8f970188f954e5f4bd9e50893ef270c78b0c7ae18` |
| Checker output (negative controls) | `evidence/tdrg/v2.12.15/controls_output.txt` | `9983aec8873fd5b2f9b1465dc56b4a93f34af3dd8ec3f47460cf66d8c43dd2f4` |
| Owner token-law check v2 and output | `evidence/tdrg/inbox_20261112/owner_token_law_check_v2.py`, `…_v2_output.json` | `491cee3b30d9020899d1028b89ff5a67fb79fded6eead292005d2d7ac9b91151`, `acbc55dbcb17b769e7ec7db822e2a7b08521ec4850cbf90ab8ad5a8e9329dd84` |
| AZ source of §6.13 | `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` | `198d2f4af9ae338fec007874d003c755674ac90da087411c57c51d63714fb829` |
| Pinned engine | `upload/tdrg-records/genesis_mode_b_mc_v18.py` | `9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e` |

**Reproduce.**
1. `git show tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md > base.md`
2. `python3 -I evidence/tdrg/scripts/build_tdrg_v2_12_15.py base.md OUT.md LOG.json` writes the candidate (`429a57f2…4f19`) and the edit log.
3. `python3 -I evidence/tdrg/scripts/check_tdrg_v2_12_15.py base.md dsn/RTG_DISCRETE_GENESIS_DSN.md evidence/tdrg/v2.12.15/edit_log.json` runs the gates; add `--controls` for the negative controls. The checker needs the tags and commit `e8d317d` to be present; no branch name is consulted.

No publication transform is planned: the candidate carries no DRAFT marker.

## 3. Edits by decision

| Item / finding | Disposition | Edits | What changed |
|---|---|---|---|
| N4: star event domain (owner finding; ChatGPT review: a scope correction, not wording) | accept | E15, E16, E17 | TDRG-DEF-STAR states the domain the engines always used: a valid centre (≥3 pairwise non-adjacent defect neighbours); a single-star component has exactly one valid centre, any shape; only the centre and the newborn change. TDRG-DEF-MULTISTAR is stated with the same precision; CONV-TICK step 4 gives the precedence. The declared event domain is widened; no dynamics or result changes. |
| AZ token-alphabet offer (`pipes/TDRG/20261112-…`) | accept with change | E18, E19, E28 | New §6.13. Seven `[ALG]` results are registered as TDR-G results credited to AZ: event inventory (E), narrow-band classes, census law, birth injection, $n$-node birth-free conservation, not-closed counterexample, parent–child phase law. Also the owner check `[NUM]` and the artifact RID. The LEM-SPECCONS $n$-node conjecture is resolved. The Stage 1 campaign numbers are not included. |
| TDR-6 and OPEN-SPECCONS-STAR (owner record §7.2) | partial | E07, E09, E10, E13 | TDR-6 becomes ACTIVE — PARTIAL: its pairwise-multiset sub-item is resolved as a predictable-change law, conditional on the centre token and the census. OPEN-SPECCONS-STAR gets a current-status paragraph. SG-12 is updated. |
| OFN token-sum finding (`pipes/TDRG/20261029-…`) | accept with change | E08, E11, E12, E30 | SG-3, the TDR-6 row and Appendix B now say: $P$ is not conserved at births ($\Delta P\equiv-x$), is invariant under the declared gauge and under relabelling, and is not a gauge quantity. The SG-3 Violation clause is extended. |
| Programme v1.4 notice (`pipes/TDRG/20261104-…`) | accept | E27, E04, E22, E24 | The §7 export row `TDRG-EXPORT-DISCRETE-TRIAD` now names TDR-24A → 24B → 24C. Companion, context and pins move to Programme v1.4. |
| OFN v0.11 / AZ v0.7 notices | no action (closed, PR #247) | E14, E20, E21, E23 | The pins move to the current editions after checking that the imported statements are byte-identical: Finding A at `ofn-v0.10`/`ofn-v0.12`; `AZ-ALG-ANTIPODAL-LOWORDER` at `az-v0.6`/`az-v0.7`. The consumers table is updated. |
| Registry | — | E01–E03, E05, E06, E25, E26, E29, E31, E32 | Header, status summary, RID map rows, Appendix A entry, footer. |

## 4. Checks

**Gates** (`check_output.txt`): RESULT: PASS (11/11 gates) — C0 BASE; C1 BUILD; C2 REVERSE; C3 HISTORY; C4 RIDS; C5 TAGS; C6 CONTENT; C7 NUMBERS; C8 EVIDENCE; C9 SOURCES; C10 DYNAMICS.

**Negative controls** (`controls_output.txt`):

```
[CAUGHT] K1 K_{1,3}-only star text restored: failing ['C1 BUILD', 'C2 REVERSE', 'C6 CONTENT', 'C7 NUMBERS']
[CAUGHT] K2 'gauge artifact' restored in TDR-6: failing ['C1 BUILD', 'C2 REVERSE', 'C6 CONTENT']
[CAUGHT] K3 unlogged change: failing ['C1 BUILD', 'C2 REVERSE']
[CAUGHT] K5 one new RID declaration dropped: failing ['C1 BUILD', 'C2 REVERSE', 'C4 RIDS']
[CAUGHT] K6 Appendix A history edited: failing ['C1 BUILD', 'C2 REVERSE', 'C3 HISTORY']
[CAUGHT] K4 wrong number, consistent log: failing ['C7 NUMBERS']
[CAUGHT] K7 star map without centre flip: C10 FAIL
CONTROLS: PASS (all caught)
```

## 5. What the change touches

- **No result is recomputed or changed.** N4 states the domain under which every number was produced. §6.13 adds statements, and its numbers come from the owner check placed with PR #243.
- **Narrowed readings.** Two older phrasings are superseded, and both are recorded in the DSN:
  - any reading of "star" as $K_{1,3}$ only;
  - "$P$ is a gauge artifact".

## 6. Live-file exceptions kept on purpose

- The engine is not patched. Under SG-14, `largest_center` remains outside covariance (N1); it is unaffected by the token laws.
- Layout is untouched: the §2 TDR-24B overlays, the Appendix A order and the footer chain stay as they are (v2.13).
- The claim-specific historical pins (OFN v0.6/v0.7, Programme v1.1) stay.
- XFER-O08-01 custody stays deferred to v2.13.

## 7. Pipe items (`pipes/TDRG/`)

| Item | State on this branch | Disposition |
|---|---|---|
| `20261029-OFN-token-sum-gauge-label.md` (finding) | dispositioned | `2026-11-12 · accept with change · records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md` |
| `20261104-PROG-v1-4-adopted.md` (notice) | dispositioned | `2026-11-12 · accept · records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md` |
| `20261112-AZ-token-alphabet-law-offer.md` (offer) | dispositioned | `2026-11-12 · accept with change · records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md` |
| `20261030-OFN-v0-11-adopted.md`, `20261111-AZ-v0-7-adopted.md` (notices) | closed (PR #247) | `no action` |

The three dispositioned items are closed after the tag.

## 8. Notices after the tag

Each notice is `kind: notice`, and filing one is a queue event, not adoption.

| Consumer | Notice contents |
|---|---|
| `pipes/OFN/` | SG-3 wording; Finding A repinned; TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED cites Finding A. |
| `pipes/AZ/` | §6.13 registered, credited; TDR-6 PARTIAL; the §6.2 citation at `az-v0.7`; no Stage 1 numbers adopted. |
| `pipes/PROG/` | The export row repaired; pin `programme-v1.4`. |
| `pipes/NUMGEN/` | TDRG-DEF-STAR scope statement (no effect on its panels); new RIDs. |

## 9. Size

| File | Bytes | Lines |
|---|---|---|
| v2.12.14 (adopted) | 178,909 | 1,387 |
| v2.12.15 candidate | 194,602 | 1,431 |

Net change: +15,693 bytes (+8.8 %), almost all of it the new §6.13 and the TDRG-DEF-STAR statement.

## 10. Steps after adoption

| # | Step | Who | State |
|---|---|---|---|
| 1 | Change-focused review | ChatGPT co-owner | *(to be filled)* |
| 2 | Row check and rerun | atlas owner | *(to be filled)* |
| 3 | Adoption decision (§11) | PI | *(to be filled)* |
| 4 | Merge commits (not squash): #247, then this PR | PI | *(to be filled)* |
| 5 | Annotated tag `tdrg-v2.12.15` on the merge commit of this PR, with the candidate SHA-256 in the message | PI | *(to be filled)* |
| 6 | `BASELINE.md` TDRG row | this branch: row entered | entered |
| 7 | Notices (§8); close the three dispositioned items | TDR-G co-owner, after the tag | *(to be filled)* |

## 11. Adoption decision

*(to be filled by the PI)*

## 12. Open items carried forward

- **TDR-6:** a purely relational invariant across births (none known).
- **OPEN-SPECCONS-STAR:** an invariant of the full dynamics, and which centre tokens fire.
- **N4 follow-up:** the share of non-pure single-star events in the canonical scans is not measured. It needs only a log reading, no rerun, and can be done in a later campaign.
- **Mechanism of the AZ Stage 1 effect:** design only (PI decision); not carried to TDR-26.
- **v2.13:** Methodology v1.4 migration and compaction; XFER-O08-01 custody; `largest_center` with TDR-19.
