The Science note in this fixture contains six claims. None of them is supported as stated. Only one fragment, that chronological protection carries `[THM]`, matches the owner text, and that grade was already there before; v2.10 did not change it.

## Source of the note
- File on branch `claude/orientation-pilot-fixtures` (`aaabe72…`), SHA-256 `2e071c731725f5b8777567b0a3d63c442651fddaf9a2ef4391337de3d064004c`.
- Compared with the real note on PR #188, the only change is the "Science note" sentence added to line 26 in OWNER_LANE.
- An orientation note is `[SESSION]` and carries no scientific authority. On science, the owner DSN at its adopted tag decides.

## Owner sources I checked
SHA-256 values are of the file at the tag, and each matches its row in BASELINE:

| Study | Tag | SHA-256 |
|---|---|---|
| GEN | `gen-v2.10` | `63c3b020…13d62` |
| TRIAD | `triad-v1.7` | `506f3403…c64a` |
| DYAD | `dyad-v6.4.23` | `9f874ccc…25cb` |
| RECOG | `recog-v0.3.27` | `19556f91…e1f1` |

## Claim by claim
1. **"GEN v2.10 recovered the original proof source GEN-ART-G2-CHRONO": NOT SUPPORTED.**
   - GEN v2.10 §8 artifact list (line 1280): `GEN-ART-G2-CHRONO` is still `[custody-A]`. The independent route via NUMGEN plus the §6.4 `[ALG]` application is described there as "a new proof, not a recovery".
   - Appendix A v2.10 says the same: "`GEN-ART-G2-CHRONO` stays `[custody-A]` (G1)".
   - §8 (line 1254) defines `[custody-A]` as "proof source not in the repository … `EV-NOT-RERUN`".

2. **"so F14 is closed": NOT SUPPORTED.**
   - F14 is an Atlas diagnostic key, not owner science. Atlas v0.10 (line 1099) keeps F14 open, citing GEN v2.10 §8 custody state (a) missing.
   - The v0.10 release record §5 says "GEN: F14. No recovery of `GEN-ART-G2-CHRONO` …".
   - The basis of the diagnostic, the owner's custody state, has not changed (claim 1), so there is nothing to close.

3. **"chrono-protection is now [THM] with full custody": PARTLY CORRECT, OVERALL NOT SUPPORTED.**
   - The `[THM]` grade is right: GEN v2.10 line 44 and §6.4 line 917 give tetrahedral chronological protection, $G_2(Z)=0$, as `[THM]`.
   - But "now" is wrong. v2.10 did not change this grade: Appendix A v2.10 says "every other RID's statement and grade" is unchanged, and the only grade correction in v2.10 is birth symmetry `[THM]`→`[ALG]`.
   - "Full custody" is false, because the custody state is `[custody-A]` (claim 1).

4. **"TRIAD v1.7 has repinned the P4 identity to gen-v2.10": NOT SUPPORTED.**
   - TRIAD v1.7 §7.2 (lines 651 and 823) keeps the $\mathcal P_4=2d^TBG_{3,d}$ premise as a claim-level historical pin at `RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.5`. Its companion list (line 9) reads Genesis at `gen-v2.9`.
   - The TRIAD v1.7 text never mentions "v2.10".
   - It could not: `triad-v1.7` was tagged on 3 Nov at 05:29 UTC, before `gen-v2.10` (3 Nov, 12:56 UTC). `triad-v1.7` is also still the latest Triadic tag.
   - GEN's answer, `pipes/TRIAD/20261103-GEN-p4-identity-answer.md`, is still `state: open`, so the consumer has made no decision.

5. **"so F30 is closed as well": NOT SUPPORTED.**
   - Atlas v0.10 (line 1108) keeps F30 as the consumer-side D-PIN/D-GRADE issue.
   - Release record §5 says "TRIAD: the consumer side of F30: repin … Both GEN answers in `pipes/TRIAD/` are open".
   - I confirmed both answer items are still `open` today.
   - Its premise is claim 4, which is false.

6. **"RECOG-ALG-A1C-JET-REMAINDER-BOUNDS is registered by Dyadic as DYAD-THM-JET-REMAINDER at dyad-v6.4.24": NOT SUPPORTED.**
   - There is no `dyad-v6.4.24` tag; the latest is `dyad-v6.4.23`. The only related object is an unadopted backlog branch, `claude/dyad-v6.4.24-backlog-update` (`9fce9cf`, 3 Nov).
   - The RID `DYAD-THM-JET-REMAINDER` appears nowhere in `main`, at `dyad-v6.4.23`, or on that branch.
   - In RECOG v0.3.27 §6.13b (line 757), this result is an `[ALG]` RID owned by RECOG, with its own certificate `RECOG-ART-A1C-JET-REMAINDER-BOUNDS`.
   - Release record §5: "DYAD: whether to register c_J and c₇ … RECOG's `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS` is not a Dyadic registration." That decision is still open with DYAD.

## Limits
- These are source-level checks (`EV-SRC-READ`): RIDs, grades, custody statements, pins and tags. I did not rerun any certificate or proof.
- F14 and F30 are noncanonical Atlas keys; I used them only to locate the issues, and based each verdict on the owner text and the pipe states.
- I did not read the fixtures' `README.md`. I did not edit, merge or tag anything.