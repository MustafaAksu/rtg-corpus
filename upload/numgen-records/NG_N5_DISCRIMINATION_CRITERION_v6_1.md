# N-5 Discrimination v6.1 — Label-Neutrality Ruling Recorded; Pre-Data Design Closed

**Memo ID:** `NG_N5_DISCRIMINATION_CRITERION_v6_1` · patches §7 of `_v6`; all other v6 content unchanged
**Certificate:** `ng_n5_discrimination_identity_cert_v5.py` / `.log` — unchanged and final
**New artifact:** `disc1_labelneutral_regression_v1.py` / `.log` (8 rows, exit 0)
**Date:** 2026-08-31 · **Auditor:** Claude

---

## 1. `[PI-RULING]` recorded — DISC-1D is label-neutral

> Every dual-active base class, including `1:1`, is eligible for the frozen discrimination gate. DISC-1B failure records failure of the non-`1` SWAP/P3 breadth search only and does not halt DISC-1D. A `1:1` DISC-1D pass admits `1 ∈ Q^dyn` but does not repair DISC-1B, establish a non-`1` class, close C7B breadth, or unblock C7C.

The ruling resolves the last open pre-data item, and the reasoning is the load-bearing part: excluding `1:1` would reintroduce the **written numeral** as an admission criterion, when the whole correction sequence established that *mechanism*, not label value, carries dynamical content. `Q^bd` and `Q^dyn` are sets of labels with admission per-label-via-some-realization, so a dynamically discriminating realization of `1` is a different object from N5-PHYS-1's `1`, which was a positive control. Same numeral, different epistemic status — and the report must show both.

## 2. Both mixed verdicts are meaningful, and neither is a contradiction

| DISC-1B | DISC-1D | Reading |
|---|---|---|
| FAIL | PASS at `1:1` | SWAP/P3 produced no non-`1` breadth at the base horizon, but its `1:1` class was a genuinely dynamics-dependent invariant rather than a predicate-multiplicity artifact |
| PASS | FAIL | a non-`1` rational label exists as a bounded periodic control but does not meet the genesis-grade discrimination criterion |

The second row is precisely why the two tests were separated, and it is the outcome the pre-audit v1.15 design would have mislabelled as success.

## 3. The ruling is now enforced mechanically, not just documented

`disc1_labelneutral_regression_v1.py` runs the frozen harness against constructed panels and certifies:

- **L1/L5** — with every dual-active base cycle at `1:1`, DISC-1B FAILS and *stays* failed; a subsequent DISC-1D pass does not repair it (`n_non1 = 0` preserved).
- **L2/L3** — DISC-1D still runs on `1:1` candidates and passes for a same-realization seed stable at `k=2` and destroyed at `k=3`, admitting `1 ∈ Q^dyn`.
- **L4** — the admitted class is reported *as* `1:1`, so a label-`1` admission is visible rather than absorbed into a generic pass.
- **L6/L7** — the converse verdict (DISC-1B PASS, DISC-1D FAIL) is representable and diagnosed observationally.
- **L8** — the decisive one: an identical transport pattern passes identically whether the base class is `1:1` or `3:2`. Admission is mechanism-determined, not numeral-determined.

I added this because a documented ruling is not a guarantee — a later harness edit could reintroduce a label filter silently. The regression makes that a test failure. No harness change was required by the ruling itself; the frozen code was already independent of the DISC-1B verdict.

## 4. Queue effects, as ruled

A `1:1` DISC-1D pass does **not** remove the need for another owner-native event-pair search if the scientific target remains breadth beyond `1`, and does **not** unblock C7C: a single discriminating class supplies no nontrivial rational arithmetic, and v1.15 keeps physical addition and multiplication separate even after multiple rational invariants are realized.

## 5. State

**No remaining pre-data interpretation choices.** Criterion design is closed; both the criterion and the analysis code are frozen, and the label-neutrality ruling is regression-locked.

Next operations, in order: owner-compatible per-cycle enumeration at `N = 24` for `k ∈ {0,1,2,3}` over the frozen raw seed panel → DISC-1B → the frozen DISC-1D transport audit. The harness consumes the enumeration under the declared contract with no further edits.
