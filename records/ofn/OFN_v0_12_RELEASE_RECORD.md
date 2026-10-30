# Ontological Foundations (OFN) v0.12 — Release Record

**Status:** DRAFT. The candidate is built and checked; review is pending. Nothing here is adopted. Until the PI adopts and the tag exists, `ofn-v0.11` remains the governing edition.
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
| Change-focused review | the second OFN co-owner (ChatGPT) | *(to be filled)* |
| Adoption | PI | *(to be filled)* |
| Merge commit; tag `ofn-v0.12` | PI | *(to be filled)* |

**PI decisions applied:**
1. One new local-result RID, `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`.
2. No choice among the 3B candidate standards (a)–(c).
3. No isolation contract is chosen. The working notes never proposed choosing one.

## 2. Identities

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v0.11) | `git show ofn-v0.11:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4` |
| **Candidate** | `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | `8230b1694bf7933d4a6cf944d28487b767aa094151ae117933d072abdca33bae` |
| Builder | `evidence/ofn/scripts/build_ofn_v0_12.py` | `dd6385914a105f1a6e0ca733b598032f0cb1d7299baa290309233728ce0ef37f` |
| Checker | `evidence/ofn/scripts/check_ofn_v0_12.py` | `78ed4c92971f9f4dd0e65e5b817ddd6d396fb14a18b29b55dc5c9a8abdde980f` |
| Edit log (23 edits; old and new text with hashes; document hash chain) | `evidence/ofn/v0.12/edit_log.json` | `ea3040d98c0256f048714e2fc8913a6681898d1b62f9cc6e8eb91889362f4960` |
| Checker output (gates and controls) | `evidence/ofn/v0.12/check_output.txt` | `b4039f4efb0fdeb54d7842e87d00cea412a904d683579c53e27f41b598505c00` |
| `dsn_lint` (informational) | `evidence/ofn/v0.12/dsn_lint.txt` | `b54955e24635de63745d6a86255d0b7962802b6f5b148ec562b01371f441589a` |

**Reproduce:**
1. `git show ofn-v0.11:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md > base.md`
2. `python3 -I evidence/ofn/scripts/build_ofn_v0_12.py base.md OUT.md LOG.json` — writes `8230b169…3bae`.
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

**Negative controls: 14/14 caught.**
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

**`dsn_lint`** (informational, no gate): 200,529 bytes, 1,598 lines; +8,477 bytes (+4.4 %); 1 new RID; 1 footer line.

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

## 4. Affected consumers (notices after the tag)

| Consumer | Notice content |
|---|---|
| TRIAD, GEN | OPEN-OFN-REF-CLOSURE (its Notify list): the new local result `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`; the question is narrowed to the physical reading; carriers on which the global comparison fails ($U(1)$, $\mathbb Z_N$ with $3\mid N$, $\mathbb Z$) |
| FMS, RRF | OPEN-OFN-TRIAD-CLASS: the isolation frame I-comp / I-quiet / I-remove, none selected; the class-C causal-interface identity |
| DYAD | OPEN-OFN-3B: the evaluation frame and class C's position, including the raw-map identity $T(-x)+T(x)=(0,2(\cosh\rho-1))$ at `dyad-v6.4.22`; nothing asked |
| NUMGEN | Vocabulary use of §6.2 N-1A2 in OFN §5.5.4 and OPEN-OFN-3A; no import of the N-1A2 closure; nothing asked |
| Programme | OFN v0.12 remains the criteria home for P0 and P2B; no OPEN status changes |

## 5. Adoption *(to be filled)*

After the change-focused review and the PI's adoption, a publication transform changes the adoption-state lines only, and a checker confirms that nothing else differs. The lines are:
- the header Date, Document status and Supersedes lines;
- the §12.3 new-RID row;
- the Appendix C v0.12 heading;
- the footer.

Then BASELINE is updated, and the PI merges and tags `ofn-v0.12`.
