# Ontological Foundations (OFN) v0.12 — Release Record

**Status:** ADOPTED by the PI on 30 October 2026 (§5). The published file `55ff8ba8…76aa` is the accepted round-2 candidate `5e1da260…6a42` plus the adoption-state lines only. The edition governs once the PI has merged PR #126 and created the tag `ofn-v0.12`; until then `ofn-v0.11` is the tagged edition.
**Date:** 30 October 2026
**Prepared by:** Claude, OFN co-owner session `claude012ZC8x` (builder), on branch `claude/ofn-v0.12`.
**Edition:** v0.12 under DSN Methodology v1.4. It is one content stage with no layout stage: no compaction is needed. The live file changes in place, and the v0.11 delta paragraphs are replaced by v0.12 ones; their content already sits in the Appendix C v0.11 entry.
**Predecessor:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.11`, tag `ofn-v0.11` (merge commit `886afc64…0978`), SHA-256 `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4`.

This record invents no hash, approval or review identifier. Fields marked *(to be filled)* depend on later steps.

## 1. Authorization and inputs

| Step | Source | State |
|---|---|---|
| Working note: isolation | `records/ofn/OFN_ISOLATION_INTERFACE_WORKING_NOTE.md`; review `OFN_ISOLATION_INTERFACE_CHATGPT_REVIEW.md` | ACCEPT SCOPED; merged in PR #120 (`c0573064…`) |
| Working note: REF-CLOSURE | `records/ofn/OFN_REF_CLOSURE_WORKING_NOTE.md`; review `OFN_REF_CLOSURE_CHATGPT_REVIEW.md` | ACCEPT SCOPED; merged in PR #122 (`e541ca84…`) |
| Working note: 3B independence | `records/ofn/OFN_3B_INDEPENDENCE_WORKING_NOTE.md`; review `OFN_3B_INDEPENDENCE_CHATGPT_REVIEW.md` | ACCEPT SCOPED; merged in PR #124 (`040da0e9…`) |
| PI start | "BAşla, RID yarat, henüz seçim yapılmasın" (start; create the RID; no selection yet), OFN session, 30 October 2026 | given |
| Inbox checkpoint | `pipes/OFN/` holds no open item (three closed notices) | nothing to receive |
| Change-focused review | `records/ofn/OFN_v0_12_CHATGPT_REVIEW.md` (ChatGPT, commit `7368ab29…`; PR #126 review `5711097535`), on round 1 `8230b169…3bae`. Verdict: ACCEPT SCOPED. R126-S1 and R126-S2 required; R126-N1 recommended | given |
| Round-2 correction | R126-S1, R126-S2 and R126-N1 applied in the builder (§3a); round 1 `8230b169…3bae` kept in Git history (commit `c8db47b`) | done; delta check pending |
| Delta check of round 2 | `records/ofn/OFN_v0_12_CHATGPT_REVIEW.md` §7 (commit `0ef4ff78…`; PR #126 review `5711501720`): ACCEPT SCOPED — OWNER ADOPTION READY; R126-S1, S2 and N1 CLOSED | given |
| Adoption | PI, OFN session, 30 October 2026, 14:26 +03:00: "PI olarak, bende OFN v0.12 ikinci tur adayını benimsiyorum" | **adopted** (§5) |
| Publication finalization | `evidence/ofn/scripts/release_ofn_v0_12.py`; P1–P6 PASS, X1–X6 caught | done; published SHA-256 `55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa` |
| Merge commit; tag `ofn-v0.12` | PI: merge commit `2b2573f59244851455cba16a2baa79c76cc8ec66` (30 Oct 2026, 14:32 +03:00); annotated tag `ofn-v0.12` (tag object `b313064f…`) on that commit (11:34 UTC), message naming `55ff8ba8…76aa`; the file at the tag hash-checked | done |

**PI decisions applied:**
1. One new local-result RID, `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`.
2. No choice among the 3B candidate standards (a)–(c).
3. No isolation contract is chosen. The working notes never proposed choosing one.

## 2. Identities

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v0.11) | `git show ofn-v0.11:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4` |
| Candidate, round 1 (superseded) | commit `c8db47b` | `8230b1694bf7933d4a6cf944d28487b767aa094151ae117933d072abdca33bae` |
| **Candidate, round 2 (adopted object)** | builder output (was `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` at `0ef4ff78`) | `5e1da260f944c40ebdcab29f57bdd37600f04e47a797b768ab5e0126a0e76a42` |
| **Published v0.12 (final)** | `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | `55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa` |
| Publication transform; check output | `evidence/ofn/scripts/release_ofn_v0_12.py`; `evidence/ofn/v0.12/release_check_output.txt` | `d961cc97b04a2aff729bfc896afe83f1732d772fc623ddb270040cb3d93f606b`; `14b60d8768abd4047820ba5b7043e2c8cc4f2daced5d2a449d850f8eb80de714` |
| Builder | `evidence/ofn/scripts/build_ofn_v0_12.py` | `90bc6540716f7732f90c2bf798dcd99fdbdc0c623f8ece0f39005021e86ed50b` |
| Checker | `evidence/ofn/scripts/check_ofn_v0_12.py` | `8e408a747b19a4853c2c010da22334f51b23dc1d8198fc8584d89b35027f54f5` |
| Edit log (23 edits; old and new text with hashes; document hash chain) | `evidence/ofn/v0.12/edit_log.json` | `420a7a8cafa3f4701eaa8b26c073658ac2d5bf91fd699a8fae0a572dcc4e342b` |
| Checker output (gates and controls) | `evidence/ofn/v0.12/check_output.txt` | `5cd5bed15338638cac69b38cf381d28635aa9a026a1255e1113d343aae2db679` |
| `dsn_lint` (informational) | `evidence/ofn/v0.12/dsn_lint.txt` | `f456b7b125ed55aed119f1449d9b9bd19bb20531a622a50e203d47f896eec2fd` |

**Reproduce:**
1. `git show ofn-v0.11:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md > base.md`
2. `python3 -I evidence/ofn/scripts/build_ofn_v0_12.py base.md OUT.md LOG.json` — writes `5e1da260…6a42`.
3. `python3 -I evidence/ofn/scripts/check_ofn_v0_12.py base.md OUT.md LOG.json --controls` — run from the repository root.

**Gates: K1–K11 PASS.**

| Gate | Checks |
|---|---|
| K1 | base identity |
| K2 | deterministic rebuild; hash chain intact |
| K3 | all 43 v0.11 RTG-OFN RIDs and all 101 anchors kept |
| K4 | the 21 OPEN status lines unchanged (20 ACTIVE, 1 PARTIAL) |
| K5 | the only new OFN RID is `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`, declared once with the single conclusion status `[from: ALG]` |
| K6 | the DYAD, GEN, TDRG, RECOG and NUMGEN RIDs cited resolve at their governing tags |
| K7 | stale v0.11 edition phrases and the superseded REF-CLOSURE question are absent from the live text |
| K8 | the required statements are present |
| K9 | Appendix A, Appendix B, and the Appendix C entries for v0.11 and earlier, are byte-identical |
| K10 | 40 protected lines unchanged: every `[DEF]` line, the Q1–Q6 rows and the Standard C declaration |
| K11 | no selection language |

**Negative controls: 16/16 caught.**
- C1: stale v0.11 boundary.
- C2: old REF-CLOSURE question restored.
- C3: an isolation contract declared selected.
- C4: an independence standard declared selected.
- C5: OPEN status changed.
- C6: v0.11 RID dropped.
- C7: extra OFN RID.
- C8: compound status `[from: THM + ALG]` on the new result.
- C9: a definition line edited.
- C10: Appendix B edited.
- C11: unresolved owner RID.
- C12: stale local-result count.
- C13: the edge-dependent-isomorphism caveat dropped.
- C14: NUMGEN N-1A2 closure declared imported.
- C15: the literal-identity wording of R126-S1 restored.
- C16: raw oddness given as the basis of C0 (R126-S2).

**`dsn_lint`** (informational, no gate): 201,031 bytes, 1,598 lines; +8,979 bytes (+4.7 %); 1 new RID; 1 footer line.

## 3. Edits

| Group | Edits | Site | Change |
|---|---|---|---|
| A — results | A01, A02 | §2.4 | `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` registered after the `[HYP]` (see the parts below). The `[HYP]`'s last sentence now points to the result and keeps the physical question open |
| A — results | A03 | §5.5.4 formal-properties list | Causal-interface bullet, under the list's existing `[ALG]` (recorded, not registered) status. Contents below |
| B — OPEN scopes | B01–B04 | §9 OPEN-OFN-REF-CLOSURE | Question narrowed to the physical reading. Closure criterion, dependencies and next artifact rewritten; status ACTIVE |
| B — OPEN scopes | B05 | §9 OPEN-OFN-3A | One pointer added to the next artifact: the causal interface as an operational ingredient. Completeness is not defined; full edge autonomy is noted as stronger than Q3a |
| B — OPEN scopes | B06 | §9 OPEN-OFN-3B | Evaluation-frame paragraph (recorded; no standard selected). Contents below |
| B — OPEN scopes | B07 | §9 OPEN-OFN-TRIAD-CLASS | Isolation-frame paragraph (recorded; none selected). Contents below |
| H — header and registers | H01–H07 | header | Title v0.12, DRAFT status, Supersedes v0.11 "on adoption", local-result count five, one summary sentence, governing inputs, evidence boundary |
| H — header and registers | H08, H09 | §0.1, §0.3 | v0.12 revision boundary and edition line, replacing the v0.11 ones; the scope-guard sentence is kept |
| H — header and registers | H10, H11 | §12.1, §12.3 | Evidence row for the three scripts; custody row for the new RID |
| H — header and registers | H12, H13 | Appendix C, footer | v0.12 entry above the v0.11 entry; draft footer |

**A01–A02, the new result's four parts:**
- (i) $Q_{\rm node}\cong C_0$.
- (ii) Forgetting an edge is a lossless parametrization.
- (iii) $\ker\kappa_n\cong H[n]$ and $\operatorname{coker}\kappa_n\cong H/nH$, with the $K_3$ carrier list. Edge-dependent isomorphisms are named as a different comparison.
- (iv) Node and edge actions differ.

It is followed by the evidence line and the "Not covered" list.

**A03, the causal-interface bullet:**
- Exact identity $F_e-N(z_e)=-\tfrac{\kappa}{3}(N(z_e)+b_e)$.
- One-step quotient-minimal sufficiency.
- The compensating interface on the lock surfaces, versus the $(1-\tfrac\kappa3)N$ law under zero total interface.
- One-step sufficiency is not closed dynamics, which is not shown for C2.
- NUMGEN N-1A2 is used as vocabulary only.

**B06, the 3B evaluation frame:**
- The axes U-form, U-class, C0, C1 and J.
- Class C's position on each, with the exact raw identity $T(-x)+T(x)=(0,2(\cosh\rho-1))$ and the scope of the raw no-go.
- The candidate standards (a)–(c), not selected.
- "No primacy conclusion follows."

**B07, the TRIAD-CLASS isolation frame:**
- The three contracts: I-comp (met exactly by class C), I-quiet (failed for κ ≠ 0) and I-remove (needs a size-indexed law).
- Standard C is not equivalent to $I_e\equiv0$.
- The next artifact: the contract declarations.

**Not changed:**
- the definitions, Q1–Q6, Standard C and the class-C contract;
- every OPEN status;
- §8 and `RTG-OFN-DEF-REDUCTION-TARGET`;
- Appendices A and B;
- the Appendix C entries for v0.11 and earlier.

No physical selection is made, and no primacy conclusion is drawn.

**Live-file exceptions:**
- The "Reconciliation input:" paragraphs (OPEN-3B, FRUSTRATION, OPA) and the §12.3 rows dated 19 October 2026 are inherited current text; they are left as they are.
- No Appendix B record is needed: the edition makes no `[COR]` to a definition.

## 3a. Round 2: corrections from the change-focused review

The review (`records/ofn/OFN_v0_12_CHATGPT_REVIEW.md`) accepted the scientific content and found two wording defects plus one recommended precision. Each was checked against the round-1 text before being applied, and each is applied in the builder.

| Finding | Edits | Change |
|---|---|---|
| R126-S1 (required) | A01, A02, H12 | "Closure reduction is removal of the common node origin" becomes the canonical isomorphism $Q_{\rm node}\cong C_0$. The two constructions are isomorphic, not literally the same operation. §2.4 and Appendix C now say the same |
| R126-S2 (required) | B06 | In the 3B frame, C0's failure rests on the owner no-go `RTG-OFN-ALG-RAW-STANDARD-C-NOGO` (smooth $C^3$ germs through 0, every $\kappa\ne0$, within its scope). The raw map's non-oddness is given separately: by itself it excludes only the named embedding $\iota_0$ |
| R126-N1 (recommended) | A03, B07 | "Active interface" on the lock surfaces is limited to nonzero edges; the zero edge of $\mathcal S_0$ has $b_3=0$ |

**Scope.** Six lines differ between round 1 and round 2, all inside these edits. No RID, status, definition or OPEN scope decision changes.

**Checks.** K7 and K8 now carry the new wording, and controls C15–C16 are added. The checker passes K1–K11, with 16/16 controls caught.

## 4. Affected consumers (notices after the tag)

| Consumer | Notice content |
|---|---|
| TRIAD, GEN | OPEN-OFN-REF-CLOSURE (its Notify list): the new local result `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`; the question is narrowed to the physical reading; carriers on which the global comparison fails ($U(1)$, $\mathbb Z_N$ with $3\mid N$, $\mathbb Z$) |
| FMS, RRF | OPEN-OFN-TRIAD-CLASS: the isolation frame I-comp / I-quiet / I-remove, none selected; the class-C causal-interface identity |
| DYAD | OPEN-OFN-3B: the evaluation frame and class C's position, including the raw-map identity $T(-x)+T(x)=(0,2(\cosh\rho-1))$ at `dyad-v6.4.22`; nothing asked |
| NUMGEN | Vocabulary use of §6.2 N-1A2 in OFN §5.5.4 and OPEN-OFN-3A; no import of the N-1A2 closure; nothing asked |
| Programme | OFN v0.12 remains the criteria home for P0 and P2B; no OPEN status changes |

## 5. Adoption

**Decision.** Mustafa (PI), OFN session, 30 October 2026, 14:26 +03:00: "PI olarak, bende OFN v0.12 ikinci tur adayını benimsiyorum" ("As PI, I too adopt the OFN v0.12 round-2 candidate").

The decision follows the second co-owner's final verdict, ACCEPT SCOPED — OWNER ADOPTION READY. That verdict is recorded in `records/ofn/OFN_v0_12_CHATGPT_REVIEW.md` §7 (commit `0ef4ff78…`; PR #126 review `5711501720`), on the round-2 candidate.

**Adopted object:** `5e1da260f944c40ebdcab29f57bdd37600f04e47a797b768ab5e0126a0e76a42`, with the edits of §3 and the corrections of §3a.

**Finalization.** Transform: `python3 -I evidence/ofn/scripts/release_ofn_v0_12.py CANDIDATE OUT "30 October 2026"`. It changes exactly five lines:
- the header Document status line;
- the header Supersedes line ("on adoption" dropped);
- the §12.3 new-RID row (now "Registered v0.12 … Registered 30 Oct 2026");
- the Appendix C v0.12 heading (now ADOPTED);
- the footer.

The header Date line already carries the decision date, so it is not touched.

**Checks** (`--check --controls`):
- Gates P1–P6 PASS: candidate hash; rebuild identical; exactly the 5 declared lines differ; the reverse transform recovers the candidate; no draft marker remains; every other line is byte-identical, and the claim-tag, RID and math census is unchanged.
- Controls X1–X6: all caught. They are an extra live change, a status-summary edit, a draft footer, a changed claim tag, an added RID, and an isolation contract declared selected.
- Output: `evidence/ofn/v0.12/release_check_output.txt` (`14b60d8768abd4047820ba5b7043e2c8cc4f2daced5d2a449d850f8eb80de714`).
- Transform script: `evidence/ofn/scripts/release_ofn_v0_12.py` (`d961cc97b04a2aff729bfc896afe83f1732d772fc623ddb270040cb3d93f606b`).

**Published file:** `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`, SHA-256 `55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa`. The candidate hash and the published hash are separate identities.

**BASELINE.** The OFN row now names v0.12, the published hash, this record and the tag `ofn-v0.12`, which the PI creates. The predecessor is kept as v0.11 `38a2f444…e9e4` (`ofn-v0.11`).

**After this record:**
1. The PI merges PR #126 with a merge commit and creates the annotated tag `ofn-v0.12` on that merge commit, with `55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa` in the message.
2. The §4 notices are filed as `pipes/` items.
3. "Sync now" is run in the Claude project.

This record is frozen at adoption, except for the merge-commit and tag fields in §1.
