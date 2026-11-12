# Discrete Genesis v2.12.15 — atlas row check (candidate `1e35be54…2e64`)

**Date:** 12 November 2026. **By:** Claude, atlas owner (advises; does not adopt). **Object:** PR #248 `claude/tdrg-v2-12-15-stage1` (head `db0a1993`, round 2): candidate `dsn/RTG_DISCRETE_GENESIS_DSN.md` SHA-256 `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64` (196,268 bytes, 1,432 lines) built from `tdrg-v2.12.14` (`3be72923…2392`) by `evidence/tdrg/scripts/build_tdrg_v2_12_15.py` (`e1332fec…3234`) with 32 logged edits and 9 new RIDs; checker `check_tdrg_v2_12_15.py` (`df9b0195…d414`); DRAFT release record `records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md`. ChatGPT change-focused review: GitHub review 5875732026 and PR #250, CONDITIONAL PASS on the round-1 candidate (`429a57f2…4f19`), conditions R1 and R2.
**Status:** record. **Verdict: ACCEPT FOR ADOPTION (atlas side), with one publication condition (§4.1) and one recommendation before adoption (§4.2).**
**Reruns:** `evidence/atlas/rowcheck/tdrg_v2_12_15/` (summary, gate and control outputs). Owner sources read at their tags (`EV-SRC-READ`). Not rerun: the owner token-law campaign (223,651 ticks), AZ's Stage 1 campaign, any earlier campaign (`EV-NOT-RERUN`). The proofs of §6.13 were read and checked by hand; no independent implementation was written.

## 1. Independent rerun

| Step | Result |
|---|---|
| `git show tdrg-v2.12.14:…` → builder | candidate `1e35be54…2e64` and edit log `a3c79ba6…3cf1` **byte-identical** to the branch files; 32 edits, 9 new RIDs |
| `check_tdrg_v2_12_15.py` C0–C10 | 11/11 PASS; output byte-identical to the committed `check_output.txt` (C10 on the pinned engine: 12,635 ticks, 0 violations, no residual class, fixtures F1 and F2 as expected) |
| `--controls` K1–K8 | all caught; output byte-identical |
| `tools/pipes_index.py --check` on the branch | OK, 110 items |
| Pinned engine `genesis_mode_b_mc_v18.py` (`9d787b43…675e`) | `star_centers` returns the nodes with at least three component neighbours that are pairwise non-adjacent; `classify_component` tests in the order isolated, single edge, one centre (star), several centres (multistar), path, cycle, then the residual classes — the domain and the precedence the candidate now states |
| Owner sample numbers in §6.13 | equal to `owner_token_law_check_v2_output.json` (223,651 ticks; 21,838 birth ticks; 33,121 births; 201,813 birth-free; 765,224 phase checks; 17,466 = 4,648 + 9,045 + 3,773; 3,773 = 1,944 + 1,829; M_post ≤ 136) |

## 2. Row checks — the 32 edits against the decisions (release record §3, §3a; PI decision of 12 Nov 2026, 16:37 +03:00)

| Item | Edits | Check | Result |
|---|---|---|---|
| N4 — star event domain | E15, E16, E17 | `TDRG-DEF-STAR`: valid centre = at least three defect neighbours, pairwise non-adjacent; single-star component = exactly one valid centre, any shape; only centre and newborn change, read from the snapshot. Agrees with the engine (§1). The earlier K₁,₃ wording is recorded as superseded, with the statement that the declared domain is widened and no result changes (`EV-CODE`). `TDRG-DEF-MULTISTAR` and CONV-TICK step 4 carry the same precision and the engine's precedence. | ✓ |
| AZ offer — §6.13 | E18, E19, E26, E28 | Seven `[ALG]` statements, one `[NUM]`, one artifact RID. Read line by line: (E) from the DEFs under CONV-TICK; narrow-band classes from `TDRG-THM-NARROW-BAND-EXCLUSION` (adjacent neighbours of a degree-3 node would close a defective K₃); census law (i)–(iii) by induction, $S_0=-S_0$; birth injection $D(C_{t+1})=D(C_t)\uplus\{|x_a+y|_c\}\uplus\{|x_a-x_b|_c\}$ with $mM_t+\binom m2$ new entries — recomputed; birth-free conservation; the $N=24$ counterexample — recomputed: $D(1,3,4,5)=D(2,4,5,6)=\{1,1,2,2,3,4\}$, additions $\{2,4,5,6\}$ and $\{4,6,7,8\}$; phase law $\theta_E-\theta_A\equiv N/2+2jx$, order classification $4x\equiv0$, with $x\in\{N/4,3N/4\}$ only when $4\mid N$ — rederived. Registered as TDR-G results credited to AZ; AZ's Stage 1 numbers are not in the DSN. `[scope:]` tags on (E) and on the phase law state their hypotheses. | ✓ |
| TDR-6, OPEN-SPECCONS-STAR, SG-12 | E07, E09, E10, E13 | TDR-6 is ACTIVE — PARTIAL, not closed. The predictable-change law is stated with what it needs (centre token and census). OPEN-SPECCONS-STAR stays ACTIVE with a current-status paragraph. | ✓ |
| Review R1 | E09, E19 | The universal negative ("no purely relational quantity is preserved across births") is gone from the candidate (C6 asserts it; K8 restores it and is caught). What replaces it is what is proved: the spectrum is not preserved at births and $D_{t+1}$ is not a function of $D_t$. The signed-class set $\mathcal I(X)$ is registered as census law (iii) with its proof and credited to the review; the candidate leaves open whether it meets the "purely relational" condition and does not close TDR-6 with it. | ✓ |
| Owner's extension of R1 | E10, E13, E18 | Three phrasings that named "an invariant of the full dynamics" as open now name a **spectrum-level** invariant, or a law closed on the spectrum. This follows: (iii) is an invariant of the full dynamics at token level, so the old phrasing would have been false in the same edition. The added remark that (iii) is not a function of the spectrum is true by the same $N=24$ pair ($D$ equal, class sets $\{1,3,4,5\}$ and $\{2,4,5,6\}$ different); the candidate states it without that one-line reason. | ✓ (see §4.2) |
| Review R2 | E19 | Parent–child order statement quantified along the free orbit (every $j\ge0$); $j=1$ already forces $2x\in\{0,N/2\}$; a window without an advance imposes nothing. | ✓ |
| OFN token-sum finding | E08, E11, E12, E30 | $P$: changes by $-x$ at a birth (centre $x\to-x$, newborn $x$); invariant under the declared phase gauge and under relabelling; "gauge artifact" withdrawn as a wrong reason in SG-3, the TDR-6 row and Appendix B; "not adopted as a physical observable" kept as a model commitment. | ✓ |
| Programme v1.4 notice | E27, E04, E22, E24 | Export row names TDR-24A → 24B → 24C and TDR-T0; Programme v1.4 line 318 has the same chain. Companion and context editions moved. | ✓ |
| OFN v0.11 / AZ v0.7 notices | E14, E20, E21, E23 | Finding A at `ofn-v0.10` and `ofn-v0.12`: the entry differs only in OFN's scope tag, as the candidate says. `AZ-ALG-ANTIPODAL-LOWORDER`: entry identical at `az-v0.6` and `az-v0.7`. Consumers table updated. | ✓ (remark §4.3) |
| Registry | E01–E03, E05, E06, E25, E29, E31, E32 | Header, declared Methodology v1.2 kept by the PI decision of 27 Oct, status summary, RID map, Appendix A entry, footer. No grade of an existing result moved; the only tag changes are the `[COR]` markers and the TDR-6 sub-items. | ✓ |

## 3. Side files

`tools/` unchanged. `BASELINE.md` TDRG row on the branch already names v2.12.15, the candidate hash and the tag `tdrg-v2.12.15`: correct once merged and tagged, as at v2.12.14. `pipes/TDRG/`: three items dispositioned with a pointer to the release record, two closed by PR #247; `20261112-AZ-v0-8-adopted.md` is on `main` only and is open.

## 4. Condition, recommendation, remarks

1. **Publication condition — the PR does not merge.** A trial merge onto `main` `e3fafc8` (after #247) conflicts in `pipes/TDRG/INDEX.md`: `main` gained the AZ v0.8 notice after the branch was cut. GitHub reports `mergeable: false`. The co-owner takes `main` into the branch and regenerates the index with `tools/pipes_index.py`. The DSN is not touched by `main`, so the candidate hash and this check stay valid; the PR head changes and the PI's CLI block must name the new head.
2. **Recommendation before adoption — a round-2 readback.** The only recorded review (5875732026) is on the round-1 bytes. Round 2 applies R1 and R2 and adds the owner's extension of R1, which the co-owner itself submits for review. This check finds all three correct, but the atlas owner is not the stream's reviewer; a short readback by the ChatGPT co-owner on `db0a1993` (three sentences, the proof of (iii), the R2 quantifier) would put the edition on the same footing as v2.12.14, where the round-2 PASS preceded the row check. The PI decides whether to wait for it.
3. **AZ pin (non-blocking).** AZ v0.8 was adopted on the same day (`az-v0.8`). The candidate pins `az-v0.7`, which is valid and intentional; the cited entry is byte-identical at `az-v0.8`. The open notice is dispositioned by the owners after the tag or with v2.13; no rebuild is needed for it.
4. **Review record path (non-blocking).** The release record cites `records/tdrg/TDRG_v2_12_15_CHATGPT_CHANGE_FOCUSED_REVIEW_20261112.md`, which exists only on the PR #250 branch. Merging #250 before or with #248 makes the cited path exist on `main`.
5. **Open item kept visible (non-blocking).** "No result changes" for N4 rests on reading the engine (`EV-CODE`); the share of non-pure single-star events in the canonical scans is not measured, and the release record carries that as an open follow-up. In the owner sample it is 3,773 of 17,466.

## 5. For the atlas

Not atlas content until the tag. At the tag, an impact refresh (with AZ v0.8, already adopted) will touch: `TDRG-DEF-STAR`, `TDRG-DEF-MULTISTAR`, CONV-TICK, the LEM-SPECCONS node, SG-3 and SG-12, the TDR-6 and OPEN-SPECCONS-STAR frontier lines, the `P` rows, the export row, and nine new RIDs.

## 6. Asked of the PI

After §4.1 is done (and §4.2 if the PI wants it): adoption of v2.12.15 on the bytes `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64`; merge order #247, (#250), #248 as merge commits; annotated tag `tdrg-v2.12.15` on the PR #248 merge commit naming the hash. The CLI block is the TDR-G co-owner's to issue with the final PR head.
