# OPEN M (UVM) — Cross-Comparison of the Two Entry Reading Reports: Discrepancy List

**Status:** [SESSION] / NONCANONICAL. **Preparer's draft, awaiting the second co-owner's review.** This is the "single owner-controlled discrepancy list" that §5 (Deliverable A) of `records/atlas/ATLAS_ADVISORY_UVM_REACTIVATION_20261121.md` asks the two UVM co-owners to write after both reading reports exist. It is not Deliverable B: it assigns no issue class (i)–(iv), disposes of no inbox item, and proposes no edit.
**By:** Claude, UVM co-owner (preparer and triage owner, PI assignment of 21 November 2026). Rows marked *open* are not decided here on the second co-owner's behalf.
**Date:** 22 November 2026. `main` `a79e420c7ea0e1fde189e2ca0caeb67747e9d97b`.

**Inputs**

| Report | PR | Head | File SHA-256 |
|---|---|---|---|
| `records/uvm/UVM_ENTRY_READING_REPORT_CLAUDE.md` (322 lines) | #357, draft | `4413d65cfa6da353f392acae3c960e6f905890bf` | `bbe86bac6629679bc8765dfb2b1d9047311ce9cde11cee2aa55805bc9144f9bd` |
| `records/uvm/UVM_ENTRY_READING_REPORT_CHATGPT.md` (81 lines) | #358, draft | `efe87230af580c358b12f99acab58b67639bc14c` | `c140d3b45c216f9b2827a79c1f1cc35e7319d091211c5f6d9436ad8fda733fc1` |

Both were read in full for this comparison. Where the two differ on a checkable fact, I re-checked the tagged bytes and state the result (`EV-SRC-READ` / `EV-RUN`, this session).

**Still unopened by this session:** §3 and §4 of the 21 November advisory, `atlas/RTG_STATE_ATLAS.md`, and the Atlas L5 rows `OPENM.U1–U11`. This list compares the two reports with each other and with owner bytes only. The comparison against §3 is the next step and is kept separate on purpose.

---

## 1. Independence limits

- **Claude report:** PR #357 opened 14:15:36 UTC; no `chatgpt/uvm-entry-reading-report` branch existed when its branch was pushed (PR #358 opened 14:24:02 UTC). No exposure to the other report.
- **ChatGPT report:** states that its open-PR search returned PR #357 and its description, and that no finding from that description is used as evidence. That description named five points: adoption is header-reported only; Genesis v2.8.5 can be derived and hash-matched; the imported Genesis statements are byte-identical in `gen-v2.10`; the `0.403` attribution occurs at lines 271 and 107; and "O1–O4 have scientific content", without saying what O1–O4 are.
- **Consequence for this list:** agreement on the adoption state and on the two `0.403` sites is agreement, but not two blind findings. The content of O1–O5, O7–O9 was not in the description, so the ChatGPT report's silence on them is an independent silence, not a rejection.
- Both sessions read the orientation note first and therefore the same Atlas bundle names (U1–U11). Neither is Atlas-blind.

## 2. Same bytes

The ChatGPT report identifies its sources by GitHub blob id; the Claude report by SHA-256. Checked here: all eleven blob ids it lists equal the git object ids of the files I read (`git rev-parse <tag>:<path>`), for `uvm-v0.7.1`, `rer-v0.2`, `methodology-v1.4`, `programme-v1.4`, `gen-v2.10`, `dyad-v6.4.24`, `triad-v1.7`, `ofn-v0.12`, `prelegacy-v0.8`, and `CONVENTIONS.md` and the orientation note at `main`. For the UVM DSN: blob `805335e8eb2b46e8007159f965489f5669352eaf` ↔ SHA-256 `0a51644d…f53e`. The two reports read identical bytes; the ChatGPT report's "not `EV-HASH`" caveat for UVM identity is closed by this cross-check.

## 3. Agreements

| # | Point | Claude | ChatGPT |
|---|---|---|---|
| A1 | v0.7.1 is identified by tag and recorded hash; its adoption is header-reported, release/adoption records absent → adoption provenance UNVERIFIED | §(a).2 | §(a) |
| A2 | The four v0.7.1 and six v0.7 governance originals, the certificate scripts, outputs and packs are not in the repository; every "PASS" is source-reported; nothing was rerun | §(a).3, §(d).3 | §(a), §(d) |
| A3 | Dyadic v6.4.10, Triadic v1.6, OFN v0.8: no bytes; old → new comparison UNVERIFIED. `programme-v1.2` exists as a tag | §(a).4, §(b).1 | §(a) |
| A4 | Programme v1.4 keeps UVM's historical pins as the consumer's declared state; a newer producer tag does not repin UVM | §(b).1 | §(b) |
| A5 | `0.403` belongs to Pre-Legacy v0.8 §1.9 (grown `N=175`); UVM calls it "Legacy" in R12 **and** in OPEN-M-2D; citation-only repair, number unchanged; PI decision of 10 November puts it with the rework | §(b).6, O6 | §(d) |
| A6 | All four `pipes/UVM/` items are open notices; none changes a UVM number or grade; the DYAD item is disambiguation only; the TRIAD item leaves T-6s/t/u intact | §(c) | §(c) |
| A7 | `B_*` has no certified sign and `κ_f` is a renaming; this reaches UVM formulas beyond notation (extent differs: D3) | §(c), O2 | §(b), §(c) |
| A8 | R15: `h` cancels; `0.007–0.008` is a proxy/calibration diagnostic, not a physical deficit | §(d).1, §(d).3 | §(b), §(d) |
| A9 | `K_vac` (log-conformal) is not identified with Genesis `g`; the large-`g` replacement is not justified at `g=1` | §(d).2 | stated in the session summary the PI relayed; in the report file only through frontier item (3) and the "large-g" condition in §(b) |
| A10 | `0.024` and `4/125` are conditional targets (reduced wrapper, 9C premise, large `g`, state/window), not universal gates | §(d).1 | §(b) |
| A11 | R10 is category-scoped; the old R3 no-go, R9's invariance conclusion and the T-6 obstruction imports are withdrawn; THM-M-LOCK is conditional on HYP-IDENT, 9C and the `K_-` branch | §(d).2 | §(d) |
| A12 | R12–R14 are finite numerics; R14's single trajectory does not establish corridor-preferential localization; RUN10 is defect-carried | §(d).2, §(d).3 | §(d) |
| A13 | `θ_f = 2π/3` (R11) and the ESM face flux `F_f = 2π/3` are numerically equal objects with no proved identification | O10 | §(d) |
| A14 | Compound status tags need unpacking under Methodology §8.4 in a future scoped revision; nothing is regraded now | §(b).4 | §(b) |
| A15 | The owner frontier is §9 in its stated order | §(d).6 | §(d) |

## 4. Discrepancies

**D1 — Genesis v2.8.5 bytes. *Open; needs the second co-owner's reproduction and a PI custody decision.***
ChatGPT: no authenticated bytes; old → new Genesis comparison UNVERIFIED; "whether and exactly how GEN v2.8.5's original bytes differed remains UNVERIFIED". Claude: reverse-applying `GENESIS_v2_8_5_to_v2_8_6_DRAFT.diff` to the v2.8.6 draft, both inside `upload/gen-records/GENESIS_V2_8_6_DRAFT_PACKAGE.zip`, gives SHA-256 `41ed76602c1c87c42972ac5b3f0a53f6973ac484427473ac371c57db1ab475cf`, the value recorded for adopted v2.8.5 in RER v0.2 §7 and in the Genesis v2.8.6 release record; on that copy the imported statements were compared line by line with `gen-v2.10`. The two positions are compatible in time (the ChatGPT pass did no tree or zip search), but they leave the list with two different evidence states for the same pin.
*Resolves by:* the second co-owner running the five-line recipe in the Claude report §(a).4 and confirming or refuting the hash; then the PI's decision on whether a derived, hash-matched copy counts as the comparison source.

**D2 — does UVM v0.7.1 import the sourced-junction theorem? *Open; a factual point for the second co-owner.***
ChatGPT §(b): "The UVM quoted older `valid minimizer` clause therefore must not be reaffirmed"; §(c) item 1: "audit … the sourced-junction import". Claude §(b).2 and §(c): UVM v0.7.1 does not cite the theorem. Re-checked for this list on the tagged bytes: the strings `minimizer`/`minimiser`, `junction` and `sourced` each occur **zero** times in `uvm-v0.7.1:dsn/RTG_OPEN_M_DSN.md`. The "valid minimizer" wording is in Genesis v2.8.5 (derived) lines 62 and 866, not in UVM.
*Resolves by:* the second co-owner naming the UVM line that carries the import, or withdrawing the clause. It matters for part (3) of the first inbox item: "no UVM statement affected" versus "an import to audit".

**D3 — which UVM statements depend on the sign of `m`. *Open; both lists need checking.***
ChatGPT §(c): "audit R2's `m=2Q_sB_*`, R5/R8 sign". Claude O2: `B_*` is literal only in R2 (line 239); an unstated `m>0` sits in HYP-IDENT (`μr² = m|w|`, line 136), R8 and the THM-M-LOCK corollary (`g_soft = 2m|ℜw|`, lines 136, 289, 301) and the R11 stiffness map (`m|w| = ℓ sin²(θ_f/2) r²`, line 265); sign-safe form `g_soft = 2|m||ℜw|` from `K = [[g, D−mℜw],[D−mℜw, g]]`. Re-checked: R5 (line 297, the HINDEX norm in `λ`, `χ`) contains no `m`.
*Resolves by:* the second co-owner saying what in R5 is meant (possibly R6, `cos 2θ = −m ℑ(w)/(μr²)`, which Claude's list does not name and should), and checking the 2×2 algebra independently.

**D4 — first bounded science question. *Not a factual discrepancy; a PI choice (Deliverable D).***
ChatGPT recommends, as the earliest high-value calculation, "a symbolic finite-`g` R11/9C normalization contract with explicit covariant block and matched `Q_s` state" (owner priority 3, OPEN-M-3C). Claude notes that priority 1 (OPEN-M-6, the full-map `h_3` audit) has all its inputs at a tag in Dyadic v6.4.24 §6.14, and that 3C needs two prior decisions: the matched state (O5) and the status of `c_0 = ‖H‖/‖M‖` (O1). Both agree that the ESM campaigns (priorities 5, 6) should not be rerun first. Both views are recorded; neither is chosen here.

**D5 — small transcription points in the ChatGPT report. *No action beyond this note.***
(a) Triadic v1.6 hash is abbreviated "`c768687c…9b36`"; RER v0.2 §7 records `c768687c…c4595b36`. (b) `open_m_3g_mini_protocol.py` is listed among "the §8 scripts"; the DSN names it only in §7 and gives it no §8 row (Claude O3). (c) "445 lines" against 444 newline-terminated lines: a counting convention.

No point was found on which the ChatGPT report shows the Claude report to be wrong. That is an observation about two documents, not a clearance.

## 5. Findings made by one report only

Each needs the other co-owner's check before it enters a triage row.

**Claude only** (section references are to the Claude report):

| Ref | Finding | What the check is |
|---|---|---|
| O1 | The `0.024` target is derived in Genesis with `α_f = c_0|w|` under "9C raw-array modelling HYP + single-jet HYP"; UVM's six condition lists for the target omit single-jet (compare A10: the ChatGPT list has the same four conditions) | read Genesis `gen-v2.10` lines 342–350 and `GEN-OPEN-UVJET-SCOPE`; then UVM lines 68, 101, 163, 215, 267, 289 |
| O3 | `THM-3G` has no claim block, tag, RID, hypotheses or §8 row; RESULT-M-3A depends on it | search the DSN for `THM-3G` (lines 11, 124, 197, 285, 317, 420, 426) |
| O4 | `T100`: `nm=2` at line 110, `nm=0` at line 277, same `σ_{h,int}=0.252` | read the two lines; resolution needs the original panel output |
| O5 | Genesis control-loss values are recorded for `Q_{s,0} ≤ 5×10⁻²`; the assembler evaluates at `Q_s = 0.1` | Genesis `gen-v2.10` §6.6 and the 7B block |
| O6 (part) | "Legacy" is also credited with the `β₁` motivation at lines 271, 273, 293; Legacy v0.7 has no such statement; nearest source is Pre-Legacy §1.9 | string search in `legacy-v0.7` and `prelegacy-v0.8` |
| O7 | `UVM-OPEN-2F` declared on two objects; R1–R11 have no result RIDs while consumers cite them by label | RID census of the DSN |
| O8 | Locators `§RG` and `§1.12`; `[from: HYP]` over a `[HEUR]` chain | Pre-Legacy §1.9, §1.12, §6.2 |
| O9 | The no-go `[THM]` that motivates the branch has its proof artifact declared "not in the repository" since Genesis v2.9 | `gen-v2.10` line 1006 |
| §(b).1–2 | Line-level identity of the imported Genesis statements v2.8.5 (derived) → v2.10; SG-PROG-1–4 identical v1.2 → v1.4; Methodology §3.3, §3.4, §4.3, §8.1, §8.4 identical v1.3 → v1.4 | depends on D1 for Genesis; the other two are tag-to-tag |
| §(d).3 | R14: `n=9`, `r=0.654` is `p≈0.06`; R15 carries one pack-derived number (`ℓ ≈ 0.7–0.8`) | arithmetic |

**ChatGPT only** (section references are to the ChatGPT report):

| Ref | Finding | Claude's check so far |
|---|---|---|
| §(b), §(d) | R15 cancellation domain: `h` cancels only where `gC_mh ≠ 0`; the zero-source limit cannot be read off the cancelled quotient | agree on the algebra; not in my report |
| §(d) | Pre-Legacy §1.8 gives `E_full = 4E_half` as a half/full-angle energy convention, not an equality with `‖H‖_B²`; R16's double bridge is required | source line confirmed for this list (`prelegacy-v0.8` line 282, under "Energy normalization", `EV-SRC-READ`); I had not read §1.8 in my report |
| §(d) | The preserved R12 sentence "the harmonic component … is the physical source" is superseded at current use only by the adjacent `[COR]`; a current-only layout should remove the ambiguity | consistent with my §(b).7 on overlays; same lines |
| §(b) | T-6s gain statement restricted to `0 ≤ g_2 ≤ 2`; T-6t labels are mode labels, not physical UV directions | not checked by me beyond the T-6 lines being unchanged v1.6.1 → v1.7 |

## 6. What this list leaves for later

- No comparison with advisory §3 or the Atlas L5 rows. Both reports are filed, so both co-owners may now open §3; I have not, so that this list stays a two-report comparison.
- No issue class, no owner action, no acceptance criterion: those are Deliverable B (`records/uvm/UVM_REACTIVATION_TRIAGE.md`).
- The three PI questions of the Claude report stand unchanged: custody of the UVM originals; status of the derived Genesis v2.8.5 copy (D1); whether the 10 November `0.403` decision also covers line 107 and the neighbouring "Legacy" attributions. A5 shows both co-owners found the second `0.403` site.

## 7. Asked of the second co-owner

1. D1: run the recipe and report the hash.
2. D2: name the UVM line, or withdraw the "valid minimizer" / "sourced-junction import" wording.
3. D3: say what is meant by the R5 sign; check `g_soft = 2|m||ℜw|`.
4. Check O1, O3 and O4 on the cited lines and say agree / disagree / cannot verify.
5. Mark any row of §3 or §5 that misstates the ChatGPT report.

*End of list. No UVM statement, pin, grade, pipe state or evidence file is changed by it.*
