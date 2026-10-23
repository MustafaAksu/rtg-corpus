# RTG State Atlas v0.2 — refresh-plan review

**Date:** 23 October 2026  
**Reviewer:** ChatGPT  
**Status:** SESSION / NONCANONICAL plan review; no Atlas acceptance, source adoption or repository mutation.  
**Decision:** **ACCEPT WITH SCOPED EDITS.** Proceed with one v0.2 build after incorporating the clarifications below. No additional plan-review round or full scientific certificate replay is requested. Final acceptance concerns the built Atlas and its declared source snapshot, not this plan.  
**Plan:** `records/atlas/ATLAS_REFRESH_PLAN.md`, branch `claude/atlas-plan`, inspected branch head `f23b16d1b36847316415d60ff5886124844584aa`. Supplied file: 5,400 bytes, 67 lines, SHA-256 `d94f7112555156ea29191bed293ff02641b0b88e9325cce14574dde87db0c33b`; locally computed Git blob `1dd1f7fdae47ad512e65baa9586baecb2bbdbb59` matches the GitHub file response.

## 1. Decisions on the four questions

| Question | Review decision | Boundary |
|---|---|---|
| Size/compression | Defer a separate global compression pass. | Current-state cleanup and removal of obsolete diagnostics remain in v0.2. Do not keep obsolete wording merely because compression is deferred. Preserve qualified scientific content. Report bytes and the counting/tokenization method; an estimated token count is not a measured count or a release gate. |
| Artifact identifiers | Normally cite artifact IDs in `cert`/evidence fields, not as independent scientific-result nodes. | Exclude them from the result-node denominator, not from identity, evidence-link and custody checks. An independently substantive engineering claim is represented according to its actual content, not excluded just because an identifier contains ART/ENG. |
| Atlas tag | Use an annotated `atlas-v0.2` tag and a compact acceptance/release record. | The tag identifies a noncanonical derived artifact. It does not adopt owner science or confer canonical status. Pin the Atlas, Method and source-manifest identities used for the release. |
| Next stream | Begin with RECOG after v0.2 acceptance. | Keep advisories/dispositions under `records/`; use one batched owner packet. Verify current owner sources at dispatch. No automatic sending, repinning, owner edit or scientific adoption follows from this plan. |

## 2. Sources actually inspected

- Full attached plan and full repository plan; matching Git blob identity as above.
- Full `atlas/RTG_STATE_ATLAS_METHOD.md` v0.1 from the plan branch; Git blob `687703a14d4511348ae9edfec606a91eeaaf2717`.
- Full `BASELINE.md` from the plan branch; Git blob `f5f9f831fe560d8695186967f7e97f63bb2f0785`.
- Atlas v0.1 source table, L0 and headline diagnostic passages, through GitHub's retrieved excerpt; not a new full-Atlas reread.
- Adopted Methodology v1.4: §§3.3–3.6 and identifier-registry passages, lines 290–415 of the tagged file; the relevant adoption/compaction/custody rules were also available in the prior receiving record. Not a fresh full-Methodology review.
- Full `records/dyad/RTG_DYADIC_v6_4_22_RELEASE_RECORD.md` at the inspected snapshot, and lines 1–15 of the tagged DYAD source.
- `dyad-v6.4.22` annotated-tag object `2c50b7a2946b48a4f4ca21f3f051366c312a077f`, pointing to commit `7130978f43b417d335622d2072abe9e571b4e142`. Its message records file SHA-256 `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`, agreeing with the release record and baseline manifest. The complete tagged DYAD file was not downloaded/rehashed in this plan review.

Not performed: fresh full reading of the three changed owners; byte comparison of all 15 proposed unchanged extraction inputs; re-extraction; certificate replay; execution of the proposed `atlas_check.py`; repository writes. The plan's identifier counts and phrase count remain reported planning figures, not independently audited coverage statistics.

## 3. Required clarifications

### ARP-01 — Current knowledge is not only unresolved questions

**Locations:** plan §1; steps 1, 5 and 6; Method §4.1 and §4.2.

Delete obsolete diagnostics from the new live Atlas rather than retaining a resolved-items ledger. Keep the removal reason and exact evidence in the review packet/Git history. However, retain all currently valid results and definitions, current negative constraints, conditional hypotheses, source-access limitations and the exact pins needed for a present use.

Current source class/adoption scope is epistemic metadata, not forbidden process narrative: RER's scoped acceptance and its two blocked records must remain distinguishable. Likewise, "source-reported", "not independently rerun" and "artifact unavailable" are evidence boundaries, not disposable history. Do not erase mathematical meanings of words such as history, resolved or return through a keyword blacklist.

A formerly OPEN module may disappear from L3 when nothing remains open, but its presently valid theorem/constraint and import edges stay in the appropriate layers. A valid FAIL constraint is retained at its scope. A RETRACTED/withdrawn assertion is not automatically a theorem of falsity. Dropping an obsolete L5 entry must not also drop an independently useful established relation.

**Suggested rule text:**

> The Atlas describes the current scientific state at its frozen source snapshot: definitions, established and conditional claims, operative negative constraints, unresolved scientific interfaces and current evidence limitations. It excludes the chronology of edits, reviews, advisory dispositions and notice handling. Obsolete diagnostics are absent from the live Atlas; their removal and justification remain in the versioned review record. Source identity, source class and scoped acceptance are retained as metadata, not narrated as release history.

### ARP-02 — Pin sources and distinguish unchanged bytes from unchanged scientific context

**Locations:** plan §2; steps 1–3 and 7.

At build start freeze the repository/BASELINE snapshot. For each source record its owner key, path, edition, class/status, selected tag, resolved commit, full file SHA-256, and available authority record. Keep a compact table in the Atlas and detailed identities in a source manifest under `records/atlas/` or `evidence/atlas/`. Update Method §4.1's blanket exclusion of hashes to permit that provenance mechanism.

Use the adopted governing edition for canonical sources. For PI-selected noncanonical sources, use the explicitly selected tagged snapshot and retain SESSION/DRAFT/noncanonical status: a tag alone does not establish adoption. A BASELINE row is a navigation/identity record, not a replacement for the scientific owner or a missing adoption record.

For an "unchanged" source, the relevant comparison is **old extraction-source bytes versus new tagged-source bytes**, not merely new BASELINE versus new tag. If an old extraction hash is unavailable, mark that equality unverified and inspect the affected content; do not invent a prior pin or certify all 15 unchanged by name alone. This does not demand arbitrary re-execution of certificates.

A change after the build starts produces a declared snapshot divergence; it does not silently change inputs halfway through the build.

### ARP-03 — Keep actual import pins; do not delete edges mechanically

**Locations:** step 3 and link integrity in step 7.

Represent current owner knowledge and a consumer's actual imported edition separately. Updating the owner node to v6.4.22 does not mean that an unchanged consumer has adopted v6.4.22. Join it to the same claim only with a documented same-claim/same-scope relation; preserve its actual proof-source pin.

Replace "re-pointed or removed if their target no longer exists" with:

> For each affected edge, verify the owner, claim identity, actual imported edition, scope and current disposition. Resolve owner-approved aliases explicitly. A still-used archived claim, an unresolved identifier or an unproved bridge is retained as an appropriately typed reference or diagnostic; absence from the latest file alone is not grounds for deletion or silent repinning.

A cited RID must resolve to the designated owner's actual declaration at the declared version, not merely occur as text somewhere in the corpus. A phantom identifier in L5 remains an unresolved diagnostic reference; documenting it is not successful target resolution. Local RER keys, representation-profile identifiers and temporary `RID unavailable` records are different types, not invented scientific RIDs.

### ARP-04 — Update Method semantics, not just L0's edition label

**Locations:** Method §§6–7; plan steps 1–2 and 5.

The present Method v0.1 has overbroad diagnostic definitions that conflict with the more careful Methodology rules:

- **D-GRADE:** a completely proved implication with an explicit unproved hypothesis may be THM. Flag an omitted premise, unjustified unconditional application or actual grading discrepancy, not the mere presence of HYP/OPEN upstream. Preserve RESULT's explicit `from` status. Do not propagate grades by RID prefix or a total ordering of all tag types.
- **D-PIN:** an older intentional source pin is not automatically invalid. Diagnose a demonstrated content/scope mismatch, unresolved identity or incorrect present-use representation. Source age can prompt inspection but is not itself a mathematical defect.
- **D-PROOF:** separate a missing argument from an unavailable certificate attachment and from a check that was not rerun. The latter states alone do not withdraw an adopted result.
- **PASS:** do not retain a review-history list in L5. Keep useful exact facts at their proper content layer and, where needed, a scoped evidence pointer. Atlas-derived links remain `~` unless justified at their explicitly reported scope; a successful Atlas computation does not confer owner adoption.

Step 5 currently says both "every L5 item is checked" and "unchanged-source items stay as they are". Use: every L5 item receives a current-snapshot disposition; unchanged-source text may be carried forward only when its dependencies and governing diagnostic semantics are also unchanged. No complete mathematical re-audit is required.

Update Method §7's "full rebuild when the method changes" clause to support the intended impact-based refresh: changes to tags, schemas or diagnostic semantics trigger validation of all affected records; they do not automatically require rereading all unchanged owners. Method §8's dated work-status narrative belongs in `records/`, not the Atlas body.

### ARP-05 — Typed coverage, not RID substring coverage

**Locations:** steps 3–4 and 7; Q2.

The reported 72 versus 164 identifier counts are not comparable coverage denominators until imports, owner results, definitions, OPEN-module IDs, aliases, artifacts and historical mentions are classified. They do not alone show 92 missing scientific claims.

Use a small machine-readable coverage map. Each extracted live owner item maps to an appropriate node, an owner-approved alias/shared node, a certificate/evidence reference, or an explicitly justified historical/out-of-scope disposition. Include live definitions and OPEN obligations, not only THM/ALG strings. Methodology contributes rule/section keys to L0; RER contributes its local record keys, not newly minted RIDs. Artifact IDs are checked even when no independent artifact node is created.

Coverage is per qualified claim: a source RID present only in a diagnostic, bibliography or unrelated `cert` field does not cover its scientific statement. Grouping remains allowed; every distinct scoped result must be accounted for. Existing unnumbered results remain source-located; the checker does not invent owner identifiers.

`atlas_check.py` may remain report-only. It must separate PASS, FAIL and unverified/unparsed cases, name parser limits and report known unresolved diagnostic references separately from accidental dangling edges. Include bounded negative controls for: omitted live claim with its RID retained elsewhere; wrong-owner/imported-only RID match; lost qualifier; invalid archived target; missing artifact linkage; and an unknown RID accepted merely because it appears in L5. This is not a request for a universal semantic verifier. Content fidelity remains part of the change-focused review.

The final acceptance condition is zero **unexplained** content losses or new broken references; documented owner gaps and properly typed open scientific questions may remain.

## 4. Minimal adjusted implementation sequence

1. Freeze source identities; apply ARP-01–05 in Method v0.2 and the extraction/check contract.
2. Re-extract changed DYAD/RER content and update Methodology-derived L0; keep the seven subject-domain layout, with streams as provenance rather than partitions.
3. Inspect affected dependency/consumer edges and all diagnostics whose truth or meaning depends on changed inputs. Remove obsolete L5 entries without reusing their stable keys. Headline order may change; record any display-number mapping in the review packet only.
4. Perform current-state wording cleanup. Do not combine this with a separate general compression campaign.
5. Produce source, coverage and link reports plus the scoped checker controls. Store process history and per-diagnostic retained/reworded/deleted/new dispositions under `records/atlas/`, not in Atlas content.
6. Submit one change-focused packet: Method diff, L0/source-table delta, DYAD/RER deltas, changed cross-domain edges, diagnostic dispositions and reports. The whole Atlas diff remains available through Git. Unchanged scientific certificates are not rerun solely for an Atlas refresh.
7. PI accepts the derived NONCANONICAL v0.2; publish one pinned acceptance record and `atlas-v0.2`. Then prepare the RECOG advisory from the accepted snapshot and checked owner sources.

No full DSN adoption cycle is imposed on the Atlas. A short acceptance record and immutable identities are still required for traceability. Atlas refresh and downstream stream adoption remain separate tasks.

## 5. Specific scientific-interface reminders for this refresh

- Extract from adopted DYAD v6.4.22, not the previously reviewed v6.4.21 draft or a review notice. Its release record explicitly distinguishes RECOG R11 from OPEN-M R11; no global R11 substitution is legitimate.
- The exact archival h4 field and its computational evidence, finite versus smooth charts, formal versus analytic realization, and the scopes of OPEN 20/21 must be taken from the owner body. Release metadata is used only to locate/authenticate that source.
- RER's 18 scoped accepted records and two blocked ER-2B records are not 20 universally accepted new owner theorems. Preserve source-import boundaries and local-key typing.
- For RECOG rollout, useful affected interfaces include R9 → DYAD phase transfer/OPEN 21 → A1a, N11's actual scientific use, finite involution jets versus exact smooth objects, and actual source pins. No consumer acceptance is inferred from updated Atlas edges.

**Outcome:** the four proposed choices are supported, with ARP-01–05 incorporated in the same build. No Atlas, Method, plan, branch, source file, PR or tag was changed by this review.
