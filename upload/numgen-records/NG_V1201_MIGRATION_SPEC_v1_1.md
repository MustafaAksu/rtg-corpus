# v1.20.1 — Methodology-Only §2/§6 Migration Specification

**Doc ID:** `NG_V1201_MIGRATION_SPEC_v1_1` · **Date:** 2026-09-25 · **Auditor:** Claude · supersedes `_v1`
**Co-owner ruling (2026-09-25):** v1.20 FREEZE CLOSED/APPROVED · reconciliation-ledger skeleton GO · structural rewrite HOLD until fingerprint v2 + this spec v1.1 carry four corrections — **incorporated below**.
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

`[COR v1.1]` **v1 said "only 1 exact-duplicate claim line exists between §2 and §6". Wrong.** The v1 script counted file-wide repeated hashes, not §2↔§6 pairs. Measured correctly: **§2↔§6 exact duplicates = 0**; the one file-wide duplicate was *intra-§2* (NG-8A / NG-8B share a status line, lines 1794 and 1813). The architectural conclusion is unchanged and stronger: **no** §2/§6 pair is worded identically. That is precisely how S6 (`[NUM-audited]` vs `[ALG]`) and S7 (mod-`N`) drifted apart across versions. It means the migration **cannot** be a mechanical dedupe. Each mirror pair must be reconciled explicitly, and the reconciliation must be recorded.

## 2. Target structure

- **§2 — Active registry.** One entry per RID/module: `status ∈ {ACTIVE, PARTIAL, OPEN, HOLD}`, one-line claim summary, dependencies, next action, pointer to the §6 body. **No theorem bodies, no proofs, no `[RESULT]` lines** — a `[RESULT]` in §2 after migration is a defect.
- **§6 — Scientific ledger.** Authoritative statements with full status tags, imports, proofs/certificate pointers, guards. All CLOSED bodies live here and only here.
- **§8** keeps mirroring §2's queue (already enforced); §9 registries unchanged.

## 3. Rules

1. **Move, never rewrite.** A claim block is relocated verbatim. Wording changes are forbidden except under rule 2 or rule 5.
2. **Mirror reconciliation.** Where §2 and §6 carry different wordings of the same claim, keep **exactly one**, record the pair in the reconciliation ledger with the discarded wording quoted, and justify the choice (normally the *more recent* or the one carrying the certificate pointer). If the two wordings differ in **status or content**, that is an undiscovered drift: **STOP**, log it as a `[COR]` candidate, and route it to a scientific pass — it is out of scope for v1.20.1.
3. **No status change** on any claim. No `[OPEN]→[CLOSED]`, no grade change, no scope change.
4. **Changelog / Appendix A history untouched**, except one v1.20.1 entry describing the migration.
5. **TAG-NORM.** `[COR v1.1]` Rule 1 and tag normalization conflicted: normalization changes the hash. Tag normalization (single canonical status, `[import:]` grammar) is permitted **only** in moved blocks and **only** as an explicit ledger entry `{class: TAG-NORM, before_h, after_h, before_text, after_text}`. INV-1/INV-2 honour exactly this allowlist and nothing else. A TAG-NORM that changes a truth status, grade, or scope is not TAG-NORM — it is a STOP.

## 4. Mechanical invariance check (the point of this pass)

Run `ng_state_fingerprint_v1.py` on the migrated file and compare to the baseline:

`[COR v1.1]` The gate now runs on **`ng_state_fingerprint_v2.py`**, which (a) hashes full **claim blocks** — anchor through the next anchor/heading, so formula/code/list bodies are inside the hash — with **full SHA-256**; (b) conserves identifiers in two sets, **explicit** (`RID:`, `Sub-RID:`, `Active architecture RID:`, bare ``RID `X` ``, `[import: … | RID]`; 39 on v1.20) and **broad** (every RID-like token; 149 on v1.20); (c) treats §2 registry rows as structural records marked `<!-- REGISTRY -->`, excluded from the scientific fingerprint. v1 hashed single lines, saw only 5 RID prefixes (80 identifiers missed), and used 12-hex SHA-1.

- **INV-0 (no open STOP):** the ledger's `stop` list is empty.
- **INV-1 (no loss):** every baseline claim-block hash is retained, recorded as a discarded mirror, or the `before` side of an allowlisted TAG-NORM. **INV-1b:** every discarded mirror's retained twin is present in the new file.
- **INV-2 (no invention):** every new claim-block hash is a baseline hash or the `after` side of an allowlisted TAG-NORM. New §2 registry rows are **not** scientific blocks and cannot trigger or evade INV-2.
- **INV-3 (no §2 theorem bodies):** zero `[RESULT]`/`[THM]`/`[ALG]` claim blocks inside §2. Baseline measurement: **119** — this is the migration workload.
- **INV-4a / 4b (identifier conservation):** explicit RID set equal; broad identifier set contained.
- **INV-P (pointer integrity, separate parser):** every `<!-- REGISTRY -->` row resolves to an existing RID/module **and** to exactly one §6 authoritative body — no orphans, no double authority.

**Self-tests, run on v1.20 before any migration:** a formula-only mutation beneath an unchanged anchor (M-1A's defect identity) **fails INV-1 and INV-2**; deleting `GEN-ART-SATURATION` **fails INV-4a and INV-4b**; the baseline compared with itself passes INV-0/1/1b/2/4 and fails only INV-3 at 119, as it must before migration.
- **INV-5 (§2 ⇔ §8 queue identity):** unchanged from v1.20.
- **INV-6:** stale-state greps from the v1.20 acceptance list still return zero on live text.

A migration that passes INV-1…6 has, by construction, changed no scientific claim. One that fails INV-1 or INV-4 has silently dropped something and is rejected.

## 5. Procedure

1. **Reconciliation ledger skeleton — DONE** (`NG_V1201_RECONCILIATION_LEDGER_SKELETON.json`). 61 §6 claim blocks against 230 §2 blocks. Automatic pairing (shared identifiers + heading key): **9 HIGH, 15 AMBIGUOUS, 37 NONE**. The 37 NONE are §6-only blocks with no §2 twin; they stay in §6 and need no reconciliation — §6 is not merely a mirror. Six HIGH pairs have differing tag sets; inspection shows several are **mis-pairings** (a §6 `[DEF]` against a §2 `[RESULT]`; three §6 blocks matched to the §2 queue line), so they are **review targets, not STOP verdicts**. Every pairing must be confirmed by a human before any `decision` is recorded; the automatic score is a starting point only.
2. Reconcile per rule 2. Any status/content mismatch → STOP list.
3. Relocate §2 CLOSED bodies into §6 under the reconciled headings; replace each in §2 with a registry row.
4. Run INV-1…6. Iterate only on mechanical failures; never on wording.
5. Emit `v1.20.1` + diff + reconciliation ledger + fingerprint delta report + hashes. Banner v1.20 as superseded **for structure only** (scientific state identical).

## 6. Bounded scope, explicitly

Not in this pass: any of the v1.20 "not changed" list; the G3 migration debt *outside* moved blocks (record it, don't clear it); `AI_CONTEXT_CORE_END` and header compression (G5) unless trivially co-located with a moved block.

## 7. After this pass — C7C-M2, one caveat to record now

The proposed micro-module **`C7C-M2 — Interface Object / Saturated Domain`**, with an interface type `𝔍_B = (B, 𝒫_B, ι_L, ι_R, 𝒯, Π)` and the theorem question *"does `(x,y) ∈ D_𝔍`, `x ≡_Q x'`, `y ≡_Q y'` force `(x',y') ∈ D_𝔍` under interface equivalence?"*, is the right next scientific object. One constraint should be written into its preregistration before any construction: **interface equivalence must be defined without reference to `ρ_Q`.** If the interface type is allowed to consult the label, saturation under `≡_Q` becomes circular and a PASS would be manufactured rather than found — the same failure the WD-REP rule guards against for the product formula. Both outcomes remain valuable: PASS ⇒ a typed quotient operation may exist; FAIL ⇒ `ρ_Q`-quotient arithmetic needs a richer representation object.
