> **[SUPERSEDED 2026-09-25] Four corrections per co-owner ruling (duplicate count, line-vs-block hashing, RID coverage, INV-2/TAG-NORM conflict). Canonical: NG_V1201_MIGRATION_SPEC_v1_1.md.**

# v1.20.1 — Methodology-Only §2/§6 Migration Specification

**Doc ID:** `NG_V1201_MIGRATION_SPEC_v1` · **Date:** 2026-09-25 · **Auditor:** Claude
**Base:** frozen `RTG_NUMBER_GENESIS_DSN_v1_20.md` (`f5ed40f5…3b636`)
**Version naming:** `v1.20.1` — patch level, so it cannot read as a new-result release. If governance rejects patch versions, `v1.21` with the changelog header "methodology-only; scientific state identical to v1.20".
**Governing rule:** **zero scientific change**, and — new here — that rule is **mechanically verified**, not asserted.

---

## 1. What the fingerprint shows about the actual shape of the debt

The baseline fingerprint (`RTG_NUMBER_GENESIS_DSN_v1_20_fingerprint.json`) extracts every status-tagged claim line: **493** in total. Their distribution inverts the intended architecture:

| region | lines | statused claims | role today | role after |
|---|---|---|---|---|
| §2 (148–2121) | ~1970 | ≈290 (headers `CLOSED …` 114, `OPEN …` 62, module blocks ≈115) | the *real* theorem ledger | compact ACTIVE / PARTIAL / OPEN registry |
| §6 (2255–2501) | ~246 | ≈60 | thin mirror | authoritative scientific ledger |

So the migration is not "trim §2 to pointers" — it is **relocate the closed theorem bodies from §2 into §6**, then reduce §2 to a registry. §6 grows; §2 shrinks.

**The critical finding: only 1 exact-duplicate claim line exists between §2 and §6.** Every other §2/§6 pair is worded differently. That is precisely how S6 (`[NUM-audited]` vs `[ALG]`) and S7 (mod-`N`) drifted apart across versions. It means the migration **cannot** be a mechanical dedupe. Each mirror pair must be reconciled explicitly, and the reconciliation must be recorded.

## 2. Target structure

- **§2 — Active registry.** One entry per RID/module: `status ∈ {ACTIVE, PARTIAL, OPEN, HOLD}`, one-line claim summary, dependencies, next action, pointer to the §6 body. **No theorem bodies, no proofs, no `[RESULT]` lines** — a `[RESULT]` in §2 after migration is a defect.
- **§6 — Scientific ledger.** Authoritative statements with full status tags, imports, proofs/certificate pointers, guards. All CLOSED bodies live here and only here.
- **§8** keeps mirroring §2's queue (already enforced); §9 registries unchanged.

## 3. Rules

1. **Move, never rewrite.** A claim line is relocated verbatim. Wording changes are forbidden except under rule 2.
2. **Mirror reconciliation.** Where §2 and §6 carry different wordings of the same claim, keep **exactly one**, record the pair in the reconciliation ledger with the discarded wording quoted, and justify the choice (normally the *more recent* or the one carrying the certificate pointer). If the two wordings differ in **status or content**, that is an undiscovered drift: **STOP**, log it as a `[COR]` candidate, and route it to a scientific pass — it is out of scope for v1.20.1.
3. **No status change** on any claim. No `[OPEN]→[CLOSED]`, no grade change, no scope change.
4. **Changelog / Appendix A history untouched**, except one v1.20.1 entry describing the migration.
5. **Touched-block Methodology v1.3 tagging** may be completed (single canonical status, `[import:]` grammar) only where the block is already being moved — the same touched-block scope as v1.20.

## 4. Mechanical invariance check (the point of this pass)

Run `ng_state_fingerprint_v1.py` on the migrated file and compare to the baseline:

- **INV-1 (no loss):** every baseline claim hash appears in the migrated fingerprint **or** in the reconciliation ledger as a recorded discard with a retained twin.
- **INV-2 (no invention):** every migrated claim hash appears in the baseline, except lines whose only change is the §2→§6 relocation of a section header (which alters `section`, not `text`/`h`).
- **INV-3 (no §2 theorem bodies):** zero `[RESULT]` / `[THM]` / `[ALG]`-graded lines remain inside §2.
- **INV-4 (RID conservation):** the set of RIDs in the baseline equals the set in the migrated file.
- **INV-5 (§2 ⇔ §8 queue identity):** unchanged from v1.20.
- **INV-6:** stale-state greps from the v1.20 acceptance list still return zero on live text.

A migration that passes INV-1…6 has, by construction, changed no scientific claim. One that fails INV-1 or INV-4 has silently dropped something and is rejected.

## 5. Procedure

1. Generate the **reconciliation ledger skeleton**: for each §6 statused line, find its §2 counterpart by RID (or by module heading where no RID), list both wordings. Expect ≈60 pairs.
2. Reconcile per rule 2. Any status/content mismatch → STOP list.
3. Relocate §2 CLOSED bodies into §6 under the reconciled headings; replace each in §2 with a registry row.
4. Run INV-1…6. Iterate only on mechanical failures; never on wording.
5. Emit `v1.20.1` + diff + reconciliation ledger + fingerprint delta report + hashes. Banner v1.20 as superseded **for structure only** (scientific state identical).

## 6. Bounded scope, explicitly

Not in this pass: any of the v1.20 "not changed" list; the G3 migration debt *outside* moved blocks (record it, don't clear it); `AI_CONTEXT_CORE_END` and header compression (G5) unless trivially co-located with a moved block.

## 7. After this pass — C7C-M2, one caveat to record now

The proposed micro-module **`C7C-M2 — Interface Object / Saturated Domain`**, with an interface type `𝔍_B = (B, 𝒫_B, ι_L, ι_R, 𝒯, Π)` and the theorem question *"does `(x,y) ∈ D_𝔍`, `x ≡_Q x'`, `y ≡_Q y'` force `(x',y') ∈ D_𝔍` under interface equivalence?"*, is the right next scientific object. One constraint should be written into its preregistration before any construction: **interface equivalence must be defined without reference to `ρ_Q`.** If the interface type is allowed to consult the label, saturation under `≡_Q` becomes circular and a PASS would be manufactured rather than found — the same failure the WD-REP rule guards against for the product formula. Both outcomes remain valuable: PASS ⇒ a typed quotient operation may exist; FAIL ⇒ `ρ_Q`-quotient arithmetic needs a richer representation object.
