# Atlas v0.4 — receiving review (ChatGPT co-owner)

**Date:** 24 October 2026. **Status:** SESSION, NONCANONICAL receiving review, not owner adoption.  
**Object:** PR #33, `claude/atlas-v0.4` at `1ad2f6c45ba934fb6447b638b1f546b74f828541`; candidate `atlas/RTG_STATE_ATLAS.md`, producer SHA-256 `988d0fa93e4962240ecbe8dc296acf7626e7b47e05c302c749d9fe82d1c6b3c4`.  
**Verdict: REVISE — two corrections required, then scoped re-read; one independent observation can be deferred to the next audit.** No re-review of unchanged scientific owner certificates is requested.

## 1. Sources and verification extent

- Read the complete `records/atlas/ATLAS_V0_4_REVIEW_PACKET.md`, all reconciliation decisions in `records/atlas/ATLAS_V0_4_RECONCILIATION.md`, PR metadata and affected Atlas regions, and the Programme v1.3 source §6.1, §7.1–7.2 and §8.2. Inspected the PR diff at the affected sites.
- Independently checked `ofn-v0.10` §5.5.3–5.5.4 and §11.4 import IMP-O10-01, `rrf-v0.8.4` §6.2a, and `gen-v2.8.9` §6.3b and SG-16. Targeted source examination, not new reproof.
- Producer run reported 35 exact-once edits, identical dual builds, zero checker FAIL, 18/18 shared tests, 6/6 focused negatives and H→L5 map (12 headlines / 137 diagnostics, no dangling and no high orphan). This review **read those statements and the submitted report; it did not independently rerun the build or mathematical certificates**. Do not treat PASS as a mathematical certificate.
- Read `CONVENTIONS.md` and the Atlas Method v0.2 previously at the tagged source. Consumer pins and unresolved v0.3 limitations are to be preserved.

## 2. Blocking receiving findings

### V04-01 — stale source identity in a live domain introduction (D1 introduction, candidate line 82)

[SESSION / SOURCE VERIFIED] Although the SOURCES table, PROG-TIERS and H10 now identify adopted Programme v1.3, the D1 domain introduction still says:

> Programme Overview v1.2 adopted 2026-09-20, Tier 0 navigation

That is **not** the governing Programme edition at the v0.4 source freeze. It is a direct contradiction within the candidate's live Atlas; it was omitted by the closed-list edit.

**Required replacement:** use `Programme Overview v1.3 adopted 2026-10-24, Tier 0 navigation` (the adoption date from the tagged Programme header), retaining the existing qualification `no physical theorem by appearance`.

**Acceptance criterion:** new SOURCE table, D1 introduction, PROG-TIERS, H10 and manifest all name `programme-v1.3`; no unrelated historical consumer pin is repinned. Add a scoped regression/negative control for stale live domain introductions; archive the additional correction in v0.4 dispositions. No new scientific calculation.

### V04-02 — parameter equivalence is not equality of raw and transported models (D1 CLASS-C and cross-domain index)

[OWNER: OFN v0.10 §5.5.4] The OFN explicitly defines
`F^N_κ(z)_e = N(z_e) - (κ/3) Σ_j N(z_j)`
by **re-imposing** feedback in transported coordinates, and says it is a **different conditional model, not passive transport of the raw κ-family**. [OWNER: RRF v0.8.4 §6.2a] RRF repeats that model-identity guard and uses `γ≡κ` **only in the OFN class-C parameter convention** for a conditional imported Q6 factor result, under the named hypotheses. [OWNER: OFN §11.4 IMP-O10-01] its Genesis `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` import associates `γ≡κ` as a parameter dictionary for the *raw* family; the same row explicitly states `Does not cover class C`. [OWNER: GEN v2.8.9 §6.3b / SG-16] GEN calls `γ` a model parameter without physical identification.

**Partly correct prior reconciliation:** Claude is right that `γ≡κ` is not wholly an unsupported Atlas invention: an owner-stated **parameter convention** exists. The initial A04-03 view must be narrowed accordingly. However, its presence **does not authorize** the candidate's unqualified model equality.

**Current candidate issue:** Cross-domain index (candidate line 67) reads
`CLASS-C node (D1) ≡ GEN F_γ ... ≡ FMS model C ≡ RRF class-C contract`.
D1 CLASS-C (line 107) reads
`CLASS-C DEF ... ≡ GEN F_γ/G^N_γ (γ≡κ)`.
As written, these identify GEN's raw mean-feedback model and OFN's transported/re-imposed class-C family *as the same dynamical model*, in direct tension with the owner's explicit guard. RRF.F5 (line 252) is now correctly narrowed to `parameter convention` but the more visible object index and D1 node still overstate identity. This is a **model-identity/scope** defect rather than an error in the symbol dictionary.

**Required correction:** retain the owner-stated `γ↔κ` parameter convention, `(H_spec)`, the exceptional parameter values and the distinct raw/transported clock/profile guards, but replace the `≡ GEN F_γ` model arrows by an explicit typed **parameter/conditional result** edge (not map conjugacy or passive transport). The D1 CLASS-C node should identify `G^N_κ` / `F^N_κ` as class-C's declared operation and separately reference GEN's **raw** `F_γ` theorem under its own scope; do not conflate `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` and `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`. Preserve the other legitimately supported RRF/OFN class-C contract aliases.

**Acceptance criterion:** no source-facing model `≡` equates raw `F_γ` and transported `F^N_κ` without an owner-supplied conjugacy, which OFN says is not the model definition. The `γ≡κ` **parameter convention** remains supported by OFN/RRF and is not misrepresented as physical identification. Check H8, D1 CLASS-C, cross-domain index, RRF.F5 and D4a model-family references together. One scoped structural negative control should reject a raw/transported model equality inserted into the visible index.

## 3. Review of packet §4 six questions

1. **Programme extraction:** ACCEPT SCOPED for inventory class/tier count (15 DSN files including RRF working standard, three noncanonical plus one derived), IF01–IF36 including IF17 settled custody, and distinction between consumer pins and governing editions. **Exception V04-01**: the D1 domain intro still reads Programme v1.2, so fidelity is not complete.
2. **κ / γ owner ruling:** ACCEPT the parameter-convention correction to my first-pass audit, **REVISE** the model identity of the D1 CLASS-C and cross-domain index (V04-02). A programme source's `atlas reading` wording is too broad but it does not license ignoring OFN's explicit different-model guard.
3. **RER flat-sector narrowing:** ACCEPT SCOPED. `~` plus “per-record hypotheses not verified” preserves map-level evidence without claiming all RER Triadic contracts are excluded by OFN. Leave per-record transfer matrix to the RER owner.
4. **κ_f:** ACCEPT SCOPED as an explicitly labelled **Atlas disambiguation**, never owner notation. The GEN form κ remains visible at the FACE-LIFT home; no silent owner symbol rename.
5. **H↔L5:** ACCEPT the **many-to-one** row-id convention and producer's 12/137, zero dangling/high-orphan checks as structural evidence; do not equate textual key coverage with scientific completeness. No request for a new H merely to mirror each high line.
6. **Outside closed reconciliation edit list:** **V04-01** is an omitted live-domain source identity. **V04-02** concerns stronger inference in a touched area. One nonblocking pre-existing edge merits a later targeted audit (below).

## 4. Nonblocking prospective audit item

[SESSION / NOT OWNER VERIFIED] D3 `RECOG-ALG-SHEAR-WEIGHT-IDENTIFICATION` contains an apparent `~ ≡ programme κ-family (κ≡γ, D4a)` link. The local RECOG shear weight `k` and the mean-feedback family coupling `κ` are different parameters unless a model-level map is established. The `~` already marks this Atlas inference, so it is **not** a release blocker, but it should be checked or explicitly disambiguated during the next RECOG/Genesis owner-facing dependency review. Do not promote it to an owner identity.

The existing 7 UNVERIFIED, 11 DOCUMENTED-UNRESOLVED and 16 wording warnings stay as reported; no assumed closure of Genesis sign tensions, physical selection, historical evidence, notice status or consumer repins.

## 5. Efficient next step

Make **one combined, source-pinned correction pass** for V04-01 and V04-02; update the deterministic refresh builder, committed Atlas, affected dispositions and acceptance draft, and add bounded regression fixtures. Re-run the common structural checker and existing negative tests. Return the candidate hash and 2-site diff for a focused readback; no full campaign replay and no unnecessary new review cycle. PI adoption, main merge and `atlas-v0.4` tag follow only after receiving acceptance.

**Verdict:** `REVISE — two precise corrections then receiving ACCEPT review`. No changes to the scientific owners or Atlas were made by this review.
