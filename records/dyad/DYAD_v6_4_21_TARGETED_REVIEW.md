# DYAD v6.4.21 — targeted receiving review

**Date:** 22 October 2026  
**Reviewer:** ChatGPT  
**Status:** SESSION / NONCANONICAL; no owner adoption, canonical edit, remote write, PR, merge, notice transmission or tag action.  
**Target:** the supplied stage-1 and stage-2 deltas, candidate `31523bd8…d12d`, branch `claude/dyad-v6.4.21`.  
**Decision:** **Stage 1: ACCEPT WITH MINOR EDITS for the submitted corrections; S-6a remains unverified. Compaction-checker implementation: REVISE. Overall pilot/adoption: NOT READY.** This does not reopen unchanged scientific results or their certificates.

## 1. Evidence actually inspected and reproduced

Read both supplied diffs, all three supplied JSON reports and the completion matrix in full. Retrieved the branch's release record, movement map and checker source; inspected the adopted Methodology v1.4 §§12.4 and 13.1–13.9 and the revised closeout instructions at the affected points of use. Checked relevant unchanged passages in DYAD, RECOG v0.3.22 §6.13b and Genesis v2.8.9 §6.3; no new full-corpus or inherited certificate audit.

The supplied differences were applied to the mounted, hash-verified v6.4.20 file, with `git apply --check` followed by `git apply`. Both reconstructed files match the reported hashes. GitHub's returned blob IDs also match the independently computed Git blob identities of the available bytes.

| Object | Bytes | SHA-256 | Git blob identity |
|---|---:|---|---|
| Adopted v6.4.20 | 411,765 | `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852` | `dd1d12fdee3a4cd8ca42ff8d147f27a2c8f64d66` |
| Stage-1 intermediate, `649441a` | 415,154 | `0572120aa6ad74b520d8338e10a712838f5a0b97c00f37e921f1915e16f836b5` | `9da289b3196ce3800eaaab3fc62b0ad893ba383d` |
| Stage-2 candidate, `a5b1a12` | 255,492 | `31523bd87de9e55dd719a35f4f665caf88608e3dc16f0ecb36a319374104d12d` | `3e35ad1d38afb45e21cbd35f52826b380cca2223` |
| Owner checker | 19,158 | `3eb52064f7cb2602d01138663f6ffc91e9b46538eeb4c514bda6b5e6b3ff72f6` | `f88abc56be60451cf149d5088290d41f1218d93a` |
| Owner movement map | 12,639 | `320e7abb6fe4596d7c7d11f044d1bf3c1ebe3c40a848c2d03893c1c8bf92c98b` | `bc6d753071428c20f9f91c19212be769898cd5f9` |

**Checker replay:** the GitHub-retrieved checker text and movement map were materialized locally and authenticated by the identities above. The checker logic is unchanged. Only its archive loader was adapted to read the independently hash-verified mounted v6.4.20 bytes instead of `git show`; no local or remote Git tag was created. The resulting positive-control JSON is **byte-identical** to the delivered `check_compaction_report.json`.

Thus the 19-operation reconstruction and the reported `609 = 573 + 36 + 0` block accounting are reproducible **under this checker's implementation**. This is not evidence that every operation the checker permits preserves scientific content; §3 supplies counterexamples. The owner's separate 12-negative-control report was read, not replayed in this review; three additional controls were executed against the source-identical checker.

## 2. Stage-1 disposition

### R21-01 — submitted corrections accepted in substance; small residual edits

The following changes are appropriate at their stated scopes:

- S-1 current-state corrections for OPEN 3/P4/OPEN 21, tangent-to-identity centralizer qualification, and reviewer-replay attribution. The P2B passage correctly says **exact coefficient equality**, not file-byte identity.
- S-2 N11 adopted use: RECOG v0.3.22's `RECOG-THM-A1A-CD-IDENTIFICATION` explicitly depends on Dyadic T1/T2. The older receipt state is preserved by its source pointer; no new receipt or repin is invented.
- S-3 static-offset versus R9-dependent primitive-memory expansion is now distinguished. R9 remains load-bearing for the quantitative transferred results.
- S-4 the `J_Q` correction and added overload rows are useful, subject to the U wording below.
- S-5 historical RAW-CUBIC identity and unrecovered projector definitions are disclosed at the points of use. No historical source is reconstructed from the Atlas.
- S-6b requires no additional edit: the requested OPEN-M/Genesis qualification is already in the specified paragraph.
- FC-34 is an arithmetic/leading-graph cross-reference only. Genesis's coefficients give `(4/3)/(1/4) = 16/3`; no policy is selected.

Stage 1 preserves Appendix A and Appendix B byte-for-byte. The live RID-tag sets are unchanged across both stages. No new owner RID or grade promotion is established by this review.

**Required small text corrections, in the same target:**

1. **Appendix C, candidate line 1351:** the added U row calls `{0<Q<=1/625}` “the tube”. The neighboring existing row and the owner contract distinguish the start/base-point set `U` from the invariant six-phase tube `U_T = union_{j=0}^5 T^j(U)`. Replace the new phrase with:
   > the start/base-point set $U=\{0<Q\le\tfrac1{625}\}$; the invariant six-phase tube is $U_T$ (see the $U,U_T$ row)
   The earlier closeout's loose phrase “tube U” should be clarified too; this is not a newly introduced domain theorem.
2. **Backbone entries, candidate lines 73 and 529:** resolve the observation already recorded by the preparer. The fitted-backbone identification stays OPEN; RECOG R11 does not. Suggested terminal wording for §1:
   > Its identification with $\mathcal A_{\rm raw}$ or with a final-chart observable remains `[OPEN]` as a fitted-backbone identification problem. RECOG R11 is CLOSED at its final-chart ledger scope; SG-19's non-transfer guard remains.
   Replace the §6.5 sentence “This revision does not ... close RECOG R11” with:
   > RECOG R11 is CLOSED at its final-chart ledger scope. That closure does not identify the historical fitted backbone with the exact dynamics or transfer it through $h$.
   The nearby “§6.5/R11 qualification” may be made explicit as “§6.5 and SG-19 non-transfer qualifications”. No blanket replacement of every `R11` string: OPEN-M's R11 is a different record.

### Exact check of the newly stated RAW-CUBIC range

**[ALG] [SESSION; not owner adopted]** The displayed raw one-step coefficient holds for every integer `p>=3` in the stated family. This is stronger evidence than the finite floating-point check, but it does not establish the identity of an absent historical proposition.

Let `theta=2*pi/p`, `c=cos(theta)`, `s=sin(theta)`, `K=2-2c`, and

\[
 u=\frac1{1-\lambda},\quad
 \rho=uZ+\bar u\bar Z,\quad \eta=Z+\bar Z,
 \quad Z=\frac{\rho-\bar u\eta}{u-\bar u}.
\]

The cubic pieces of the declared map are `rho'_3=eta^3/6`, `eta'_3=K(rho^3+eta^3)/6`. Consequently,

\[
 [Z^2\bar Z]Z'_3
 =\frac{1-K\bar u(u^2\bar u+1)}{2(u-\bar u)}
 =\frac K4+i\frac{2c^2-2c+1}{4s}.
\]

Substitute `t=tan(pi/p)`, `c=(1-t^2)/(1+t^2)`, `s=2t/(1+t^2)`, `u=(1+i/t)/2`. The difference is exactly zero in rational symbolic arithmetic. For integer `p>=3`, `t` is positive and finite and `s>0`, so these denominators do not vanish. No normalizer or homological divisor is used. In particular,

\[
 p=3:\ \frac34+\frac{5i\sqrt3}{12},\qquad
 p=4:\ \frac12+\frac i4.
\]

The delivered script `raw_cubic_exact_check.py` passes **7 coefficient/frame checks and 1 shear/recoil ratio check**. This does not extend RECOG's normalized all-p theorem to p=3 or p=4, and it does not settle RAW-CUBIC's historical provenance.

## 3. R21-02 — checker false positives (pilot engineering blocker)

The supplied positive-control report reproduces exactly, but three declared bad changes also return **PASS, exit 0**. These are local negative-control files only, never proposed source edits.

| Control | Bad change | Required result | Actual result |
|---|---|---|---|
| REVIEW-N1 | Remove “with zero linear part” from smooth-generator uniqueness; declare it a `ref-subst` edit and add a valid archive-tag reference | FAIL | **PASS** |
| REVIEW-N2 | Change the `H-7` archive target to nonexistent `H-999`, keeping the valid `dyad-v6.4.20` tag | FAIL | **PASS** |
| REVIEW-N3 | Replace the live §6.7 cubic-jet result body by an archive pointer; set `tag_examples: true` and retain its heading anchor | FAIL | **PASS** |

**N1 mechanism.** `check_op(..., class='ref-subst')` compares status/qualifier/RID/math/hash features and a short list of protected words. It does not require unchanged prose outside an exact reference span. The zero-linear-part hypothesis is untagged prose and falls outside the protected-word list. Declaring the edit makes the block “explained”, so both per-operation and block checks accept the widened assertion.

Exact control:

```text
old: unique among $C^\infty$ generators with zero linear part; hence
new: unique among $C^\infty$ generators; see tag `dyad-v6.4.20`; hence
```

**N2 mechanism.** `check_links` checks the presence of a nearby tag, not whether `H-999` exists in that archive. The mutated target is absent from the hash-verified archive but passes. A limitation about unparsed section numbers does not cover a claimed successful H-label resolution.

**N3 mechanism.** `tag_examples: true` bypasses the live-result protection. The retained anchor and RID mentions elsewhere satisfy the global existence checks. An unverified classification supplied by the movement map is being treated as proof that the deleted section contains only examples/history.

These failures do **not** prove that the submitted candidate has lost its §6.7 result or its smooth-uniqueness hypothesis: it has not. They show that the current checker cannot support the asserted general preservation gate. The distinction is between **the reviewed particular diff** and **the admitted transformation class**.

### Minimal repair within this pilot

- For reference substitutions, specify exact reference spans and verify that all surrounding protected bytes remain identical. Do not try to solve unrestricted semantic equivalence by expanding a keyword list. A separately reviewed substantive edit belongs to stage 1.
- Resolve archive targets in the actual pinned archive: tag + path + heading/anchor/label, not merely tag presence. Report unsupported target types as unverified, not PASS.
- Make `tag_examples` / `navigation` classification depend on a bounded, reviewed source-region identity (locator and hash), not an unchecked Boolean. Arbitrary sections cannot acquire archival eligibility through that switch.
- Run the original negative controls plus these three controls after the repair. This is a narrow engineering correction, not a restart of the scientific certificate campaigns.

A movement map is an inventory of changes, not independent authorization of their scientific admissibility. “No semantic equivalence is proved” is an appropriate limitation; it does not excuse accepting unrestricted scientific rewrites as exact reference substitutions.

**Nonblocking tooling cleanup:** `check_presentation` has a hard 60-word limit on Document status. No such numerical gate is justified by the inspected v1.4 rules; keep this as a size warning, not a release-failing condition. The supplied size JSON should state its counting method and include orientation-core size under §13.8. Neither observation rejects this candidate on account of size.

## 4. R21-03 — S-6a source not available; no original h4 execution

**[OPEN] [source-access scope]** `normalize_p6_liegauge_exact.py` is not present in the mounted input files, the recursively inspected members of the three supplied ZIPs, or the inspected branch tree. The C-2 named sources were not recovered from those inputs either. See `results/source_availability.json`. This is a bounded availability finding, not a claim that the originals never existed or are globally lost.

The current owner registry itself describes `DYAD-ART-NORM-P6` as `mp.dps=120`, numerical and tolerance-pruned, not an exact-arithmetic certificate. Therefore a successful numerical replay would establish only its numerical output; it would not, by itself, certify exact coefficients in either `Q(sqrt(3))` or `Q(i sqrt(3))`.

Keep three tasks separate:

1. recover and authenticate the original script, its dependencies/inputs and invocation;
2. inspect/replay its actual archival h4 output and identify the coordinate/output convention;
3. establish the exact field claim by an exact symbolic derivation or an already existing exact owner source, or obtain an explicit owner correction of that claim.

Do **not** substitute the quartic term of the finite polynomial normalizer in `DYAD-ALG-NF6`: SG-19 identifies it as a different object from the archival transformation. Do not retag the historical owner result solely because the source is unavailable here.

No h4 coefficients are supplied by this review. S-6a remains OPEN. The point-of-use record may explicitly state source-verification pending, but that is not a completed coefficient-field check and cannot silently satisfy the unchanged closeout criterion. Any alternative limited release needs an explicit owner/PI disposition of that residual.

## 5. Records, installation and source routing

### R21-04 — completion accounting and closeout

The supplied matrix has **34 distinct rows**. Its primary-state entries count as:

`18 DONE v6.4.20 + 9 DONE v6.4.21(candidate) + 5 OPEN + 2 RESEARCH = 34`.

The displayed 19+9+5+2 count includes FA-05 twice. Keep FA-05's implemented sub-scope in a sub-item field, with one primary state for that row. The nine candidate-complete rows are not nine newly adopted rows; FA-02/FB-23 also need the small residual edits in §2 above before being unqualified DONE. Record this review's checker issues separately as pilot engineering residuals, not extra scientific RIDs.

**M14R-05:** the point-of-use closeout instructions are now aligned: replace stale statements rather than stack overlays; distinguish N11 current use from receipt history; meet E-1 by compaction or a declared exception; execute E-2; use the corrected intermediate for stage 2. Git/tag custody replaces the earlier separate HISTORY-file proposal. Historical v6.4.20 text need not be duplicated into a new supplement. Later facts/corrections still require their own recorded release entry; a Git pointer cannot supply a missing original artifact.

**C-2:** the missing original files were not found; none was uploaded or reconstructed from prose. Supply the source package under its own hashes, preserving original bytes.

**C-3:** prepared notices are not sent notices. No messages were transmitted by this review. Routing remains through the PI, with `sent`, `received`, `statement accepted`, and `adopted use` recorded separately. Other streams' pending decisions do not block a correctly scoped DYAD adoption.

**C-4:** the mounted ChatGPT-side v6.4.20 copy hashes correctly. Its computed Git blob matches both the GitHub `main` response and the `dyad-v6.4.20` response (`dd1d12f…64d66`). This verifies this available copy and its repository identity; it does not claim a byte read-back from Claude's project synchronization. Recheck the successor after actual publication.

## 6. Next receiving boundary

Keep one target, v6.4.21. Apply the small point-use repairs and any owner-approved S-6a correction to **stage 1**, record its new hash, then regenerate stage 2 and its movement map. Repair and rerun only the affected engineering checks. Do not rewrite just the final candidate while retaining stale intermediate/map identities.

The next submission needs only the changed stage-1 lines, the S-6a evidence or explicit owner disposition, the corrected checker/control reports, and the updated completion records. No full NF, interval-arithmetic, smooth-embedding or unrelated research campaign is requested.

Scientific review acceptance, editorial eligibility, owner/PI adoption, publication and consumer synchronization remain distinct. Do not set `ADOPTED`, merge or create `dyad-v6.4.21` merely because S-6a receives a response. This review does not grant that decision, and the checker issue remains independently open.

*End of targeted review. Repository unchanged; no PR, merge, tag or notice action.*
