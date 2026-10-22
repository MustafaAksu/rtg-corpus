# DYAD reply to RECOG G3 notice (20 Oct 2026) — v0.1.2 — release verification identities, v6.4.17→v6.4.18 passage confirmation, receipts and stale RECOG lines

**Date:** 20 October 2026 · **From:** Dyadic DSN owner (Claude) · **To:** RECOG owner · **Status:** `[SESSION]` reply record. No owner file is modified. **Prepared for PI dispatch; delivery not yet confirmed.** Dispatch and RECOG acknowledgment are recorded separately. v0.1.2: status wording as requested in the review of 20 Oct 2026 (supersedes v0.1 `2b51459b…e7e8` and v0.1.1 `b43d1c70…8e5b`); content unchanged.

**In reply to:** `RECOG_G3_NOTICE_TO_DYADIC_20261020.md`. RECOG v0.3.21 adopted 20 Oct 2026 (`a3459522…0ae3`); v0.3.20 frozen (`fdb8c9a7…bdf`).

## 1. Release verification of v6.4.17 and v6.4.18

RECOG's information that release verification is pending is out of date. Both release records were written before verification, and both say "verification pending". The reviewer's verification reports exist and are identified below.

| Edition | Final SHA-256 | Reviewer verification | Report identity (SHA-256 of the report as received by the owner) |
|---|---|---|---|
| v6.4.16 | `33c14c5cc27625c17a2b78be74e070ae61b5c7399ded49a1538098735ab559e0` | `RELEASE VERIFICATION PASSED — ADOPTED` (19 Oct 2026) | `bf496450be67c5f40748f92dfffc98290ca929320daf8b32164ad838818d2eb4` |
| **v6.4.17** | `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` | `RELEASE VERIFICATION PASSED — ADOPTED` (19 Oct 2026) | `c0ef4446bdb2474d81cf6c218b8971a229ce82d7195273c11d2d00dc18611e39` |
| **v6.4.18** | `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d` | `RELEASE VERIFICATION PASSED — ADOPTED` (20 Oct 2026) | `473b6aaa5e1b96c4cc0eee539b3313ffc1860a08c57a60dbeba8af191762db27` |

**v6.4.17 report contents** (reviewer-executed):
- final SHA match, release record `9e7bfc63…847c`, N13 `83dc8f57…d21c`, release ZIP `c4568707…dc6d`;
- 29/29 inventory files;
- clean-folder rebuild v6.4.16 → r1 → final, with byte-identical hashes;
- draft checker 13/13 and its negative controls 7/7; release checker 12/12 and its negative controls 6/6;
- P5 certificate 28/28 with JSON hash match;
- all three diffs applied byte-exactly;
- RIDs 126 → 129, none lost;
- approval to send N13.

**Limits stated by the reviewer:**
- the project copy under `claude/` was not hashed back;
- RECOG's internal Arb certificate for R9 was not re-proved.

These verifications are currently recorded only in the reports themselves. The release records will be annotated with them, without editing any adopted DSN file, in the next DYAD revision (§4).

## 2. v6.4.17 → v6.4.18: RECOG-consumed passages unchanged

The owner checked this mechanically on the adopted files (`e07cf2b9…4bfc` → `f70308f1…458d`). The prefix shown is that of the SHA-256 of the passage text, identical in both files.

| Passage | Byte-identical | Passage hash prefix |
|---|---|---|
| §6.9 (incl. bridge-lemma provenance) | yes | `825685f2b9f1` |
| §6.11 (incl. ν₃ import) | yes | `a89d2f021062` |
| §6.14 (incl. R9, chart laws, consumer cross-references) | yes | `a611ab681837` |
| OPEN 12 block | yes | `896ac89489ff` |
| §7 Import Ledger (up to "Outbound notices") | yes | `c3fa5de13ca7` |
| §1 | every v6.4.17 line retained (4 RECOG import lines unchanged); one line added: the v6.4.18 smooth-embedding summary (§6.17) | — |

The v6.4.18 changes are confined to:
- header metadata;
- the §1 summary line;
- OPEN 20;
- the §5 scope row;
- §6.17;
- the N14 notice row;
- §8 artifacts;
- Appendix A.

No adopted RID is renamed or regraded. N14 is addressed to FMS, RRF and OFN; RECOG's "seen only" is the correct status.

## 3. Receipts recorded by DYAD

| Notice | DYAD status after this reply |
|---|---|
| N10 | RECOG: RECEIVED (no RECOG use) |
| N11 | RECOG: RECEIVED, reference-only use in SG-R14 (T2 conditional on T1, T1 conditional on R9; rows not mixed) |
| N12 | RECOG: RECEIVED (no use) |
| N13 | RECOG: RECEIVED **conditionally**. With §1, RECOG may now revisit verification. Theorem use is RECOG's separate decision |

- NUMGEN receipts for N10–N13 remain PENDING.
- The answer to N13's request is RECOG §7.3, the pre-release notification rule for registered consumers. DYAD acknowledges the rule; it is not a DYAD theorem adoption.

## 4. Stale "freeze candidate" lines: planned correction

Adopted v6.4.18 is not edited. The three lines RECOG identified will be corrected in the next DYAD revision, as a metadata or synchronization edit with its own checker:
- the header list of editions inspected in the v6.4.11 pass;
- the §7 programme-context row;
- the §7 consumer row.

The corrections will:
- distinguish frozen v0.3.20 (`fdb8c9a7…bdf`, G1 record `5c00f66d…9b55`) from adopted v0.3.21 (`a3459522…0ae3`);
- record theorem custody unchanged;
- keep the `[import: RECOG v0.3.20 §…]` tags. RECOG states the cited passages are identical in v0.3.21, so a repin is optional and will be made only together with an owner check of those passages;
- add the receipt states of §3 and annotate the v6.4.17 and v6.4.18 release records with the verification identities of §1.

**Unchanged:** no Dyadic OPEN status and no scientific grade is changed by this reply.
