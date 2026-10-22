# Note to the Dyadic co-owners — v6.4.21 and the new working method

**Date:** 22 October 2026. **From:** the atlas owner (Claude), with the PI. **To:** the Dyadic DSN co-owners. **Status:** working note.

## 1. What happened

The Dyadic DSN has a new adopted edition, **v6.4.21** (PI, 22 Oct 2026; SHA-256 `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d`; tag `dyad-v6.4.21`). It was prepared in the **atlas stream**, not by the Dyadic owners, under the closeout of the v6.4.19 atlas advisory. ChatGPT reviewed it in two rounds; the PI adopted it. It is also the pilot of DSN Methodology v1.4.

It changes no RID, no grade and no OPEN status. It contains:
- **Errata (stage 1):** current status at every point of use for OPEN 3, P4, OPEN 21, RECOG R11 and the P2B v2 coefficient check; closed OPEN 9 items moved out of the active list; N11 recorded as RECOG's adopted use; subclaim dependencies of DYAD-ALG-OPEN3-PHASE-OFFSET (§7); notation overloads (Appendix C); RAW-CUBIC provenance caveat and range $p\ge3$; unrecovered OPEN 9 definitions named where used; FC-DYAD-34 cross-reference (§6.12).
- **One correction you should know about:** the archival Lie-gauge $h_4$ of OPEN 13 was labelled "exact over $\mathbb Q(\sqrt3)$". Its coefficients are complex (e.g. $h_4^{(1,3)}=\tfrac13+\tfrac{\sqrt3}9i$), so the field is $\mathbb Q(i\sqrt3)$. Your script `normalize_p6_liegauge_exact.py` is now in the repository, and `dyad_h4_archival_exact_check.py` confirms the closed forms exactly. The `[ALG]` grade and $c_\theta^{(6)}$ are unchanged.
- **Compaction (stage 2):** current-only header with a §1 profile exception; one footer; Appendix A reduced from 150k to 4k characters. The full older history stays in v6.4.20 (tag `dyad-v6.4.20`). File size 411,765 → 256,508 bytes, with no scientific statement removed. A checker verified the stage-2 delta.

Records: `records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md` (what changed, checks, adoption); `records/dyad/DYAD_v6_4_21_TARGETED_REVIEW.md` (review); `records/dyad/DYAD_ADVISORY_v6_4_19_COMPLETION_MATRIX.md` (state of the 34 advisory rows).

## 2. Please look at

These were done on your file without you. Confirm or correct them in your next release; nothing here is urgent.
1. **The stage-1 diff:** `git diff dyad-v6.4.20 6622dcd -- dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, about 30 edits. Each is listed in the release record §2.
2. **The $h_4$ field label** (§1 OPEN 13 entry; §8 DYAD-ART-NORM-P6).
3. **R11 wording** (§1 backbone entry, §6.5): RECOG R11 is CLOSED; what stays OPEN is the identification of the historical fitted backbone. Check this reads as you intend.
4. **The §1 profile exception.** §1 is about 1,500 words. You may prefer to shorten it in your next release instead of keeping the exception.
5. **Remaining history phrases.** The live text still has about 50 "historical"/"superseded" phrases. Most describe historical objects (fits, archival normalizations) and are current statements. The pilot did not review them one by one.

## 3. How we work now

The full rules are in `CONVENTIONS.md` and in Methodology v1.4 (`dsn/DSN_METHODOLOGY.md`). The short version for this stream:

- **The repository is the source.** The current Dyadic DSN is `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` in `MustafaAksu/rtg-corpus`, and the governing edition is the latest tag `dyad-v…`. The Claude project mirrors the repository; there are no hand-uploaded copies. Older editions come from tags. There are no `_v6_4_x` copies.
- **Keep the file current-only.** Edit statuses, pins and scopes in place. Record each change once in a compact Appendix A entry. Put draft-round records and review correspondence in the release record, not in the DSN.
- **Releases go through a branch, a review, a release record, PI adoption, merge and tag** (`CONVENTIONS.md` §4). If a release also reorganizes layout, build it in two stages and check stage 2 with `tools/check_compaction.py`.
- **Evidence lives with the claims.** New certificates go to `evidence/dyad/scripts/` with their outputs, cited in §8 by path and hash. The goal: anyone can test a Dyadic claim from the repository alone.
- **Files from your sessions** go unchanged to an `upload/…` branch. If you have no repository access, hand them to the PI. They are hash-checked before placement.

## 4. Open items you inherit

| Item | State | Where |
|---|---|---|
| Missing source files (143 cited files not yet in the repository) | **Deferred by the PI**; collected later from the PI's machine | `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md` |
| Notices N16–N21 | Prepared, not sent; to be settled during the coming DSN tour; record states per recipient | `records/dyad/DYAD_NOTICES_N16_N21.md` |
| RAW-CUBIC historical identity; eight unrecovered OPEN 9 definitions | Need the v5.4.x OPEN 9 working files (in the recovery list) | §2, §6.11, Appendix D |
| FC-DYAD-31, FC-DYAD-32 | Research; FC-32 stays SESSION, and OPEN 21 keeps R9 | completion matrix |
| FC-DYAD-33 lag-sign corollary | Offered to NUMGEN in N18 | notices |
| Installation read-back of v6.4.21 | After the project sync | completion matrix C-4 |

The atlas will be refreshed from v6.4.21. The next atlas advisory for Dyadic, if any, starts from this edition.
