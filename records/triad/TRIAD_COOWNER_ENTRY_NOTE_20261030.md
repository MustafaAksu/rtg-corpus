# Triadic co-owners — entry note for the v1.7 round

**Date:** 30 October 2026.
**From:** Claude, Atlas owner.
**To:** the Triadic co-owners, Claude and ChatGPT, with a copy to the PI. The Claude co-owner works in its own owner session, not in this Atlas session.
**Status:** coordination note. It decides nothing. The co-owners decide each item and the PI adopts.

## 0. Can the round start before the missing files arrive?

**Yes.** The missing files block no content decision.

- **Rows 1–23** of the merged list work from the tagged DSN text (`triad-v1.6.1`, `95340abe…451f`). They also use pass 2's algebra script, which reran with PASS here, and the two recovered producer scripts.
- **Nothing in rows 1–23 regrades a claim** whose evidence is missing. Every evidence-backed result keeps its present grade, scope and historical pin.

What the missing files *do* constrain:

- **(a) Custody statements must be true.** The v1.7 header and §8 must not say that `evidence/accepted_r4_2/` "is preserved" as if it were in the repository. They state where the evidence is (held by the PI, not in the repository), point to the recovery ledger, and keep the printed hashes as identities.
- **(b) No upgrade that needs a rerun.** Examples are re-running the T-6u certificate, the T-6b–T-6j producers or the 15-check normalization audit. Such upgrades wait for the evidence. No row asks for one.
- **(c) The v1.6 records stay cited by name.** These are `records/OWNER_ADOPTION.json`, `records/RELEASE_RECORD.md` and `records/METADATA_EDITS.json`. They are history only and are not needed to adopt v1.7.

## 1. Read first

1. **`records/triad/ATLAS_ADVISORY_TRIAD_v1_6_1_RECONCILIATION.md`** (PR #131): the 29-row merged list, staged 0 / 1 / 2. This is the working list.
2. **`records/triad/ATLAS_ADVISORY_TRIAD_v1_6_1.md`** (PR #131): pass 1, TA/TB/TC/TD, with line references.
3. **`records/triad/ATLAS_ADVISORY_TRIAD_v1_6_1_INDEPENDENT_CHATGPT.md`** (PR #133): blind pass 2, TRI16-I01–I15, and `evidence/triad/scripts/triad_blind_algebra_checks_20261030.py`.
4. **`records/triad/TRIAD_UPLOAD_HASH_CHECK_20261030.md`** (with this note): what arrived (2 of 11 package files, both OK), what was recovered (T-6c2 and T-6l, hashes equal to L903 and L915), and what is still missing.

Items 1–3 are on `main`: #131 was merged at `c5fac7d` and #133 at `ab8749b`. Item 4 and this note are on branch `claude/triad-custody-entry` until it merges.

## 2. Priority

Pass 2's priority stands, and both passes agree: **settle the model contract before any new trajectory campaign.**

1. **Row 1 (U1).** The conditional first integral D = 𝒢/Q_s = Q_c(1 − K) at L742.
2. **Row 2 (U2).** The differential Gram identity versus the exact finite six-step increment.
3. **Row 4 (A4).** The T-6r carrier contract C1–C6.

After these come rows 5–11 (scope and currency), then the form rows 13–15, then stage 2.

## 3. Points for the co-owners' own judgement

- **f_s and f_c (row 1).** L742 uses them without defining them. The Atlas found that the two displayed identities agree if and only if f_c = Q̇_c, and with f_s = Q̇_s, D is constant. State the definitions, the domain (Q_s, Q_c > 0) and the clock. Then decide whether D is:
  - a remark at ODE scope; or
  - an exported RID.

  If it is exported, its scope says that D belongs to the truncated diagnostic field and is not a physical conserved mode.
- **Finite-step typing (row 2).** Type `TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION` as a first-variation identity, and give the order of the discarded quadratic increments ΔQ_sΔQ_c − (ΔI)² − (ΔΩ)². This narrows how the identity is read. It is not a refutation. Under §4.4 this is the same proposition, so the RID is kept, unless the owners decide the proposition itself changes.
- **Coercive bound (row 3).** 6(√3 − 1)K ≤ A_θ^corr ≤ 6(√3 + 1)K, from the eigenvalues 6√3 ± 6. Decide between:
  - a registered local algebraic corollary; or
  - a remark.

  Either way, there is no persistence at finite u/r without a remainder smaller than the margin.
- **T-6r contract (row 4).** Write C1–C6 as the current acceptance contract: carrier and metric; encoding and reduction; full evolution; clock and phase convention; event predicates and regularity; covariance. Use current-state form, not a waiting list.
- **96:1 (row 7).** Keep it OPEN, stated once, as arithmetic history. Add the metric-dictionary caveat (B_T = 2B_G would make it 192).
- **Consumer matrix (row 9).** It replaces §7.4's aggregated statuses. A v1.6 receipt is not acceptance of a v1.6.1 delta. Programme v1.3 *is* pass two (row 10).
- **RID set (row 13).** The text says "all 49 RIDs" but 46 `TRIAD-*` RIDs are present. State the set. Also fix the RRF key spelling to `OPEN-B/E1`.
- **Placement of the release records (row 24).** `upload/triad-records/` holds `OWNER_ADOPTION_v1_6_1.json` and `RELEASE_RECORD_v1_6_1.md`. Their hashes match the package checksum list, and they name the tagged DSN. The intake manifest says that placement under `records/triad/` is the owners' call. Until then, v1.7 cites them at their upload path.

## 4. Suggested working order

This mirrors the OFN and Dyadic rounds.

1. **Separate dispositions.** Each co-owner writes accept / accept-with-change / decline, with the reason, for rows 1–29. Then they reconcile into one fixed list.
2. **v1.7 stage 1 (content).** Rows 1–15 as fixed, plus the true custody statements (§0(a)). Then a change-focused co-owner review.
3. **v1.7 stage 2 (layout only).** Rows 17–23: v1.4 header, narrative moved to Appendix A/B and the release record, one footer. Checked with `tools/check_compaction.py` and a movement map; no claim moves without a map entry. Row 29 is applied only if PR #113 has merged.
4. **Atlas row check, PI adoption, merge and tag** (CONVENTIONS §4: decision → release record → merge → tag).
5. **After the tag.** Send notices (row 12):
   - to Genesis, about its `[CAND]` import of T-6t and the v1.6 pin;
   - to OPEN M, Programme, OFN and RRF.

   Then close the Triadic items in the consumer matrix as receivers answer.

## 5. Boundaries

- Nothing here changes Triadic text, grades, RIDs or pipe states.
- The Atlas reruns (pass 2's script; the hash checks) confirm algebra and identity. They are not owner audits of the arguments.
- The two recovered scripts have not been run. The DSN cites them as producer bytes, and nothing is regraded on them.
- The T-3a file (`upload/dyad-sources/rtg-engine/triad_t3a_arb_enclosure_v4g.cpp`) is an incomplete scaffold, not a certificate. No Triadic claim cites it. It goes in the custody ledger only (row 26).
- Custody rows 24–28 stay open until the PI uploads the rest of `accepted_r4_2/` and the release package. They do not hold up stages 1 and 2.
