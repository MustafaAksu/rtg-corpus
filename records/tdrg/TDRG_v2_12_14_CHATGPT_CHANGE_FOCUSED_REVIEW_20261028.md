# TDR-G v2.12.14 candidate — ChatGPT change-focused review

**Date:** 2026-10-28  
**Status:** REVIEW — CONDITIONAL PASS after two bounded corrections; neither owner adoption nor atlas row check.  
**Target:** PR #92, `claude/tdrg-v2-12-14-stage1`, head `6a5aebdfe149185b40db65fc8043126217230f4a`; candidate SHA-256 **source-reported and checker-reported** `b8317a75e5fb335075828f706f42f14708538fc15ff958b6acd4ef5402295a61`.  
**Baseline:** `tdrg-v2.12.13`, `dsn/RTG_DISCRETE_GENESIS_DSN.md`, SHA-256 `aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f`.  
**Authority:** governing Methodology v1.4 at `methodology-v1.4` (target DSN retains declared v1.2 under PI decision); `CONVENTIONS.md`; disposition reconciliation §3 in PR #91; owners' disposition PRs #88/#89; the source-reported testing/evidence in PR #92.

## 1. Extent and method

Changed source contents and affected dependencies reviewed through GitHub: the candidate against `tdrg-v2.12.13` (101 difference regions; 105 exact-once edits reported by builder), with targeted full-text inspection at header/§1, §2, SG-14, §6.3, §§6.5–6.12, §7 Imports/Consumers/RID map, §8 artifact custody, Appendix A/B/C and footer. Read the complete DRAFT release record, the orientation reference implementation, checker C0–C10 including negative controls, and their committed logs. Read the fixed dispositions in PR #91 and owner evidence from PR #89. Historical Appendix A content beyond changed locations was not re-reviewed scientifically.

The candidate hash, 105-edit reconstruction, 11-gate pass, 7/7 negative controls and N=24 full three-node k=1 result are **owner-run reports read in the repository**, not computations rerun by this reviewer. The GitHub PR diff API does not provide the oversized DSN patch; old/new source texts were compared through line-based matching of their fetched contents. An independent bounded spot check used the byte-matching legacy engine `genesis_mode_b_mc.py` (`4c94d874…a608`) available locally, with an independently coded option-(b) selector: the explicit v18 antipodal permutation fixture fails, option (b) passes, and 3,000 random permutation comparisons pass. This is not a full independent owner checker or BIND3/NKSCAN rerun.

## 2. Positive findings — scope accepted

**[SESSION]** The candidate implements fixed orientation option (b), namely the balanced tie at `S=0, E in {0,N/2}`; it adds exact `signed_centered` and `signed_defect_error` definitions, the no-go under the selected (S,E) inputs, and keeps centre-relative G only as a covariant alternative. The pinned engine is NOT silently modified. The §6.12 statement differentiates node relabeling from ±mirror *inventory* matching; the latter is not a dynamics symmetry. N1 is explicitly recorded for the `largest_center` ID selector. This is consistent with PR #91 and does not close TDR-19 or the alternative-rule sensitivity campaign.

The `d=0` least-period-one exception in LEM-RETRIG and the strictly one-way `LEM-SPECCONS -> gcd classes` correction are present. The new scaling statement makes the full-range `-0.869` a window-dependent finite fit, retains the owner-source `-0.730` high-N window, removes the superseded `chi=0.836` consistency relation, and leaves the thermodynamic limit at HEUR. TDR-24D/F mechanism-level closure and A/B/C gate are aligned.

All earlier OPEN modules are retained according to the owner checker. The RID map explicitly maps older consumer spellings `TDRG-ORIENT` and `TDRG-ZN-STATE` to typed owner RIDs `TDRG-DEF-ORIENT` and `TDRG-DEF-ZN-STATE`; this is supported by Methodology v1.4 §§4.2/4.5 and is preferable to silently declaring the bare names theorem/definition RIDs. Consumer acceptance, statement acceptance and custody are distinct. The four originally cited certificate suites and v6 outputs are explicitly `missing`; two v17 files have byte-exact replay evidence, while the remainder have narrower schema-consistency/held status.

The choice (b) changes the model on its degenerate stratum, not merely prose. Historic BIND3 and motif results remain pinned to the v18 orientation and `EV-NOT-RERUN`. The numerical atlas census is reported only at N=24 and does not become a many-node exposure bound. The preserved 96.4%, 3.6%, 81.8% outcomes are *historical v18 results*, not results certified for option (b). No campaign rerun is requested.

## 3. Required bounded corrections

### R1 — SG-14: remove the unqualified universal covariance demand and declare the newborn-node action

**Location:** candidate §3 SG-14, first sentence and branch scope. Current text opens “The TDR-G step must commute with G_cov = Sym(V) × Z_N^phase” while its own final clause correctly states `largest_center` is not covariant under equal-degree centre relabeling. The tests compare newborn nodes **as a multiset**, not by fixed fresh numeric IDs. Because the state-space size varies under star birth, the action on newborn identities must be identified to make “commute” meaningful.

**Acceptance:** scope the normative requirement explicitly to the canonical `bound_symmetric` rule and any other *qualified* branch satisfying the required controls; list `largest_center` as a known violation at equal-degree ties, not merely as a qualified universal law. For a birth, equality is up to the induced bijection of freshly created nodes (including their full recorded states), not equality of arbitrary fresh numeric labels. Retain the tested-vs-general distinction: the finite N=24 evidence is a check, not a proof of universal covariance for all N and policies. No new number or campaign is needed.

### R2 — C8 checker: replace ephemeral upload-branch dependency with immutable commit/tree verification

**Location:** `evidence/tdrg/scripts/check_tdrg_v2_12_14.py`, constants `SESSION_REF = "origin/upload/tdrg-session-scripts"`, `SESSION_COMMIT = 386e9d44…`, and C8. The checker requires `git rev-parse origin/upload/tdrg-session-scripts == SESSION_COMMIT` and loads the SHA256SUMS only through that branch. Once the independently verified upload is merged and its temporary branch is deleted or moves, the **unchanged adopted candidate fails C8** despite all necessary objects being retained in Git.

**Acceptance:** validate the manifest and each member by **immutable commit SHA**, `386e9d44f1f819d89b5b0e0ce4f6cb18c6e08c8b`, or by the hash-checked placed tree after its authorized merge, with the custody state still accurately describing whether files are only held on a staging branch versus placed on `main`. Check that expected path members are preserved. A deleted/advanced upload branch must not invalidate reproducibility of the published proof checks. Continue using the existing negative control for a wrong file hash. The release-record reproduction command must not require an ephemeral remote-tracking branch after publication. **Re-run only the small checker gates/negative controls after this change, not the scientific campaigns.**

## 4. Pre-publication conditions and nonblocking limits

- **Staged BASELINE row:** PR #92 currently writes `v2.12.14`, tag `tdrg-v2.12.14` and the candidate hash to `BASELINE.md` before the tag exists. This is acceptable **only as a prepared publication row on an unmerged branch**. It must not be treated as the governing edition until the PI adopts, merges and creates the annotated tag. If merges/tags are separated, ensure the repository's public current-state manifest does not falsely announce an adopted edition in the interval.
- **Merge prerequisites:** PRs #87 and #91 remain open as inspected in this review. Merge them in the PI's fixed order before #92; revalidate the checker on the prospective merged tree, especially source/collision/path checks.
- **Evidence:** existing BIND3/NKSCAN/N-scaling campaigns were not rerun and must remain marked `EV-NOT-RERUN`; the four original certificate suites are missing. No missing original may be 'recovered' by recomputation. The atlas owner's independent row check is still required.
- **Numerical status:** the statement “no scientific number changed” applies to historical campaign values, not to the new orientation fixture/census numbers or to the newly displayed existing high-N fit; those have separate provenance.
- **Appendix history/footer:** retained under PI's explicit v2.13 deferral; not a v2.12.14 blocker. Likewise, further polish of the remaining legacy qualifiers is not a reason to reopen a science review.

## 5. Review verdict

**[SESSION] CONDITIONAL PASS; two localized pre-adoption fixes R1/R2.** No objection to option (b), no objection to the typed-RID aliases, no need for a new scientific proof, coefficient optimization, BIND3 rerun or scaling refit. Once the two corrections and relevant targeted negative controls pass, the atlas row check and the PI adoption can follow. This review does not adopt the edition, approve the scientific results beyond their pre-existing scopes or authorize any merge/tag.


## 6. Round-2 disposition — 28 October 2026

**Reviewed target:** PR #92 commit `e3f55c70c51bce4787ddd450b39e0e2ed58a14cb` (round-2 owner reply to reviewer comment 6454252077). **[SESSION] Both R1 and R2 are CLOSED at their prescribed acceptance criteria. The change-focused co-owner review is now PASS at this candidate identity, subject to the separately required atlas row check and PI adoption.**

**R1 SG-14: CLOSED.** The revised guard explicitly binds the covariance requirement to `bound_symmetric` and separately qualified policies; compares birth-containing outputs modulo a one-to-one relabelling of newly born nodes (the checked multiset of `(theta, delta)`); restricts finite N=24 controls to their tested scope; and states the `largest_center` noncovariance and applicable policy-specific violation clause. This corrects the former universal wording without strengthening the scientific claim.

**R2 C8: CLOSED.** The checker uses immutable upload commit `386e9d44f1f819d89b5b0e0ce4f6cb18c6e08c8b` and pins the session-script `SHA256SUMS.txt` hash `00ce64d9b9fc8039e81eb5cc2489248f3b71f5e0de33740f85bb0cb3696ac6e3`. It checks each manifest member against the hash list. If the file set is placed in the working tree, it instead checks that tree against the same pinned manifest. Pending cited paths resolve through immutable `c359e21…`/`386e9d44…` commits rather than transient remote refs. K8 injects a false manifest hash and the owner-run log reports C8 rejecting it.

**Independent source/identity inspection:** The source files were fetched directly from GitHub at commit `e3f55c7`; their SHA-256 values were recomputed in this review from the fetched text and **match exactly**:
- candidate `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`;
- builder `71d990b3579adaa2cecaa4308064af0a5e5c8ff127636609c757c4f0921f286e`;
- checker `d27b946bd1e0ed2a40edf26da2c83d35401dae7f7e887eb4cdd9f53c762af847`;
- edit log `c94ff966ffe1f707c0e25cba3df83d6daad38c16074ab1ee7348224541c2edcb`.

Comparing round-1 and round-2 edit log objects: 105 edits retained, **only edit E32 (group TA03, SG-14)** changes its replacement text and replacement hash; no source-match key, old text, other replacement, group or declared RID was changed. The candidate global hash changes as expected; builder/checker and logs were updated accordingly.

**Execution provenance:** The owner's round-2 logs, read at `e3f55c7`, report 11/11 gates, 8/8 caught negative controls, `--exhaustive` at N=24,k=1 (v18 failures [72,72], amended rule [0,0]) and a distinct 11/11 run without the two local remote-tracking branch refs. The `check_output_no_branch_refs.txt` log is proof of the source session's run, **not** an independently repeated Git checkout and full local execution by this reviewer. These logs and source logic meet the original requested bounded checks; no BIND3/NKSCAN/scaling campaigns were rerun.

**Publication-only dependency:** An immutable Git commit hash is stable *while the object is retained*. Once the atlas has hash-checked the session files, their authorized placement on a reachable merged history is preferable for a fresh-clone reproduction; the release should not rely on deleting the last ref to an unmerged upload commit before it is preserved. This is an evidence-custody/publication requirement, **not a new R2 code defect**.

**Final scoped review verdict:** **PASS / REVIEW-CLOSED for candidate SHA-256 `3be72923…2392`.** Atlas independent row check/replay, PI adoption, merge order and annotated tag remain separate. No adoption, tag, merge, or release-status change is made by this review.
