# RTG State Atlas v0.5 — change-focused review packet

**Date:** 25 October 2026. **Prepared by:** Claude, Atlas owner.
**Status:** DRAFT / NONCANONICAL — second candidate; receiving review REVISE (AV05-R1, AV05-R2) applied, focused readback requested (ChatGPT, Atlas co-owner); no PI acceptance or owner-science adoption. `atlas-v0.4` governs until acceptance.

## 1. Inputs and identities

Base `atlas-v0.4`, SHA-256 `b63eaf8b85dbb1f4a8fbee61cb82f2af089276797c387e6a8a0b13922805c35b`. Source snapshot `origin/main` `75f8dc95520aaceac6a36614016902b408a8b52e` (after PR #56). Two moved sources: **Genesis v2.9** (`gen-v2.9`, commit `9c98f7a966dd…`, file `9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac`) and **RECOG v0.3.24** (`recog-v0.3.24`, commit `091baaffd748…`, file `8c64bea231b3691b737f4143f6f4105030ee183fcc90d7f604ec83a4c869e7c1`). The other 16 sources are byte-equal to their v0.4 inputs (manifest `v0_4_input_equality`). Dyadic is unchanged at v6.4.22; its new records (`records/dyad/`, OPEN 20 LH2012 assessments) change no owner edition and are not atlas sources. Method edition v0.2, unchanged.

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate) | `cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5` (477,266 bytes, 1,549 lines; second candidate, §6) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.5/source_manifest.json` | `923e87cc59c803359ed44dc87f333cf10911b3bf887c59d7f9f0fa8c38cc9ce3` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_5.py` | `b08fafa347a0a316dae21749b801482338949e9ad70a1696eae70201d1fa212e` |

Decision basis: the Genesis cycle records (`records/gen/ATLAS_ADVISORY_GEN_v2_8_9_RECONCILIATION.md`, the two owner dispositions, `ATLAS_ROW_CHECK_GEN_v2_9_STAGE1.md` §4 and `…STAGE2.md` §4 "atlas-side notes", `GEN_v2_9_RELEASE_RECORD.md`) and the RECOG v0.3.24 release record (`records/recog/RECOG_v0_3_24_RELEASE_RECORD.md`).

## 2. Review scope

Impact refresh of two domains; 68 exact-once operations (`evidence/atlas/v0.5/edit_log.json`); no other domain re-extracted.

**Genesis v2.9 (D1, D2, D4a, D4b, H1, H6, H8).**
- SOURCES/D4a/D4b headers to v2.9; GEN header node records Methodology v1.4 with the bounded `[RESULT]` migration (new row GEN.D17).
- κ_f is owner notation (GEN §6.8 `[DEF]`): every "atlas label κ_f" phrase removed (H8, D1 κ line, RRF.F5, D4a κ line, F1, D4b κ line, FACE-LIFT, secular-K−, SCALARM nodes); FACE-LIFT node rewritten from the owner DEF (N̂, sgn(m), B_* undefined by owner declaration).
- Sourced junction: node renamed to `GEN-THM-SOURCED-JUNCTION` with the w=0 algebraic statement, two antipodal solutions, Δ₃>0 hypothesis, physical branch OPEN (GCL-02), RET pointer to the retracted minimizer clause (GEN Appendix B). `GEN-THM-QH-NOGO`, `GEN-THM-SINGLE-FACE-METRIC` replace the `*GEN:` surrogates; the D4b exports line names the RIDs and the consumers block of GEN §7.
- 9A node rewritten in the sign-explicit form; 9-downgrades node and the OPEN-GEN-II-9 frontier item carry the scalar-M scope words; MSPIN2-ANISO drops its `! GEN.D14` flag.
- §6.3c: TRANSPORTED node and D2 `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` node record the G-20 existence note (C^∞ imported; analytic and physical/network open); H1, OFN.O1, DYAD.X1, F5 drop GEN from the "fix" list (OFN, FMS, ER-2B remain).
- D4a nodes that pointed to retired F rows (GSPLIT, T6U, moment-closure, c_θ, sign-split) now state the v2.9 resolution in place.
- H6 rewritten and downgraded to **med**: convention settled; remaining owner OPENs (GCL-02 physical branch, B_*), custody state of the nine proof sources, c_θ archival status; keys GEN.D3, GEN.D6, RECOG.R-L6.
- Retired: GEN.D1, D2, D4, D14; F9, F10, F15, F16, F17, F19 (reasons in `dispositions.json`). Reworded: GEN.D3 (custody keys), D5, D6 (owner-declared), D7 (narrowed), F1, F5, F14, F20 (TRIAD-only), OFN.O1, DYAD.X1. New: GEN.D17; PROG.G8 (Programme §8.2 lacks a κ_f row; E-P13-1).

**RECOG v0.3.24 (D3, H5).**
- New nodes: `RECOG-THM-A1B-SLIP-SCHEDULE-U` ((A) events = lift crossings, (C′) six-step deficit bounds, (B) alphabet {6,7} with s(M)=(3τ/π)log M+O(1), (S) digamma schedule with the explicit ε_k ceiling; dependencies and nonclaims as stated), `RECOG-RESULT-A1C-RECORD-PHASE-READOUT` (record determines L and Ψ_∞ mod 2π; no reconstruction of a; no R_ind downgrade), `RECOG-ALG-QUADRATURE-TYPING` (unipotent shear on 𝒬; comparator-geometric content; Ω-area-neutral locus; type not chart-invariant), `RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY` (e^ρ−1=mπ; odd-m period-2 family; complete inside Σ only).
- R4 record: sub-item 1 answered in reframed form, inventory complete inside Σ; R6 record: two OPEN sub-items A1c-Q1′, A1c-decoder. Export protocol extended. H5 names the two new U-theorems.
- MNT: the v0.3.23 live-file exception is resolved → RECOG.R-P3 and R-T1 retired; R-D1 notes the two new artifacts (naming only, not rerun); A1a node locator loses its edition pin.

## 3. Dispositions and mechanical checks

25 touched L5 rows: 12 retired, 11 reworded, 2 new (`dispositions.json`, hashes). Retired keys added to `retired_l5_keys.json`, not reused (guarded). Two builds give identical bytes; reproduce with `python3 -I evidence/atlas/build/refresh_v0_5.py` (asserts base hash, every source tag's hash and commit, tag/snapshot equality, no "atlas label κ_f" phrase, no stale `v2.8.9`/`v0.3.23` section references, every new-node RID present in its tagged source).

Shared checker: **zero FAIL** (the two `sources` FAILs of the moved rows cleared); PASS sources 72, coverage 128, qualifiers 3, links 419, artifacts 99, keys 77. Carried, unchanged by text from v0.4: 4 link UNVERIFIED + 3 artifact UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording WARN. Shared negative controls 18/18; focused controls 6/6 (retired key cited by an H; retired key reused; SOURCES row older than manifest; "atlas label" wording reintroduced; misspelled new-node RID; stale edition reference). H→L5 map: 12 H lines, 127 L5 rows, 0 dangling, 0 high rows without H.

## 4. Questions for receiving review

1. GEN extraction: are the FACE-LIFT, SOURCED-JUNCTION and SCALARM-EIGEN nodes faithful to GEN v2.9 §6.8/§6.9 (sgn(m) map, Δ₃>0, antipodal solutions, OPEN wording), and is H6's downgrade to med justified?
2. RECOG extraction: do the four new D3 nodes carry the owner scopes and nonclaims (U-only, a-priori tails, no decoding of a, no R_ind downgrade, inventory complete inside Σ only)? Anything load-bearing in §6.13b/§6.16e/§6.3/§6.5 omitted?
3. Retirements: any of the 12 retired rows still live in the owner text?
4. PROG.G8 and GEN.D17: appropriate as atlas diagnostics (owner-recorded items), or should they be routed only through the Programme/Genesis records?
5. Anything in the 121-line diff outside the scope of §2.

## 5. Publication boundary

Not accepted by this build. Acceptance needs the receiving review, then PI acceptance identifying the bytes `cf250c91…b0e5`, a merge commit (not squash) of `claude/atlas-v0.5` into `main`, and an annotated `atlas-v0.5` tag naming the hash. No owner DSN, grade, source tag, Method edition or consumer adoption is changed. `atlas-v0.4` remains the accepted Atlas until that decision.

## 6. Correction pass after the receiving review (25 October 2026)

Receiving review `records/atlas/ATLAS_V0_5_RECEIVING_REVIEW.md` (ChatGPT, PR #58, commit `9a419073`): REVISE on the first candidate `3479e046…7cec`. Both findings verified against `recog-v0.3.24`:
- **AV05-R1** — the A1c node ended its positive statement with "without a"; owner §6.16e: "without the value of a" (the record determines the phase limit without the value of a; not a non-recoverability theorem). Fixed.
- **AV05-R2** — the A1b node quoted the ε_k ceiling without saying that Q is the largest primitive amplitude of the k-th slip block and that the tails are a-priori quantities, and omitted the owner's consequence M_{k+1}/M_k → e^{π/(3τ)}; both added, with the owner's caveat that no computable finite-record decoder guarantee follows. Fixed.
- Accepted suggestion: PROG.G8 labelled as an atlas reading (of Programme §8.2 against GEN §6.8 and OFN/RRF) rather than "owner-recorded"; E-P13-1 remains cited as the Programme owner's own record.

Three lines changed against the first candidate (D3 A1b node, D3 A1c node, D1.L5 PROG.G8). Second candidate `atlas/RTG_STATE_ATLAS.md` SHA-256 `cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5`; builder `b08fafa3…212e`; checker zero FAIL, carried rows unchanged; 18/18 + 6/6 controls; two builds identical.
