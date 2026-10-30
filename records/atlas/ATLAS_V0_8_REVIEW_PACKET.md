# RTG State Atlas v0.8 — change-focused review packet

**Date:** 30 October 2026. **Prepared by:** Claude, Atlas owner.
**Status:** DRAFT / NONCANONICAL — candidate for receiving review (ChatGPT, Atlas co-owner). It has no PI acceptance, and it adopts no owner science. `atlas-v0.7` governs until acceptance.
**Scope decision:** PI and ChatGPT, 30 October 2026: one change-focused refresh carrying OFN v0.11 and RECOG v0.3.26. There is no general compaction and no Methodology migration of the atlas. Tool maintenance (PR #113) runs separately and does not block this edition.

## 1. Inputs and identities

Base: `atlas-v0.7`, SHA-256 `8ebfbd1008ce96e167ec90931468d166c568294a66453824667fba88e3f49c6c`; tag object `643120ce…`, commit `8ece2a59a0962e6433d19f3c8203345ab22d4c1b`.

Source snapshot: `origin/main` `f8f3b5b172649c69236e327af1f12f93e2307b1d`, after PR #117 (OFN v0.11 post-tag records and notices).

**Two sources moved:**

| Source | Tag | Tag object | Commit | File SHA-256 | Verified |
|---|---|---|---|---|---|
| Ontological Foundations v0.11 | `ofn-v0.11` | `2018dfd078dd90287632a8c942f35ec1f20aaded` | `886afc64573579165170bff682de21d5acf60978` | `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4` | `records/ofn/OFN_v0_11_TAG_VERIFICATION.md` (PR #118, open); the builder also asserts the file hash at the tag and at the snapshot |
| RECOG v0.3.26 | `recog-v0.3.26` | `1ad769146a7afa76882cb27a0e634d4ed6d2fbe4` | `2c076a75518ee4235a31261b2c1ef8fff987b1eb` | `45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34` | the builder asserts the file hash is equal at the tag and at the snapshot; no separate atlas tag-verification record exists for this tag |

The other 16 sources are byte-equal to their v0.7 inputs. The builder asserts this through the manifest field `v0_7_input_equality`: 16 EQUAL and 2 CHANGED, and the CHANGED set is exactly {OFN, RECOG}.

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate) | `450d8e7127beef06d07f4b2315b23233085b5766ffd2cb4894418780bd198e46` (502,219 bytes, 1,540 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.8/source_manifest.json` | `1e698a08bf47a3648caa27c29c4e1329b71a44c26dde0987ca158fe420c83c6e` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_8.py` | `6d6c77feacd40e11829d8fefba16f34bf6368991feaf49e5efaa939b2fd5c926` |
| `evidence/atlas/v0.8/edit_log.json` (94 operations) | `cc93022be0e3ba7cedf5611336cb5330705f49a10084c15058117592f48f1faa` |
| `evidence/atlas/v0.8/dispositions.json` | `cb04c326dddadeba522693b82618ca57deb68ad81567c44efd77f66177d12e6a` |

**Decision basis — OFN:**
- `records/ofn/OFN_v0_11_RELEASE_RECORD.md`: §3 lists the edits by row, §3a round 2, §3b the Atlas receipt and the bounded dispositions.
- `records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md`: the fixed dispositions.
- `records/ofn/ATLAS_ROW_CHECK_OFN_v0_11.md`: the row check of the 165 edits.
- The OFN v0.11 text at the tag.

**Decision basis — RECOG:**
- `records/recog/RECOG_v0_3_26_RELEASE_RECORD.md`: §0 the correction, §1 the groups, §8 the adoption of CORR, DRIFT and ENV.
- The RECOG v0.3.26 text at the tag: §6.13b and Appendix B.
- `pipes/ATLAS/20261029-RECOG-v0-3-26-adopted.md`: the row-update notice to the Atlas owner.

## 2. Review scope

This is an impact refresh of two domains: 94 exact-once operations, listed in `evidence/atlas/v0.8/edit_log.json`. No other domain was re-extracted. The diff against the base is 73 insertions and 78 deletions. In net terms:
- removed: 8 OFN L5 rows and one D-WRONG line;
- added: OFN.O14, one new OFN definition node, and two RECOG nodes.

**OFN v0.11 — D1 and its consumers (H1, H4, H8, D-WRONG, D2, D3, D4a, OPEN M).**

*Identity and counts.*
- The SOURCES row and the D1 header carry v0.11: 17 DEF RIDs, 1 HYP RID, 4 local RESULT RIDs and 21 OPEN (20 ACTIVE + 1 PARTIAL).
- The builder asserts 43 OFN RIDs at the tag.

*RIDs.*
- Four atlas labels are renamed to the RIDs registered in v0.11. The atlas label is kept in the head:
  - `RTG-OFN-DEF-ZERO-ORIGIN`
  - `-DIST-ZN`
  - `-DISCRETE-REDUCTION-BOUNDARY`
  - `-CONTINUOUS-REPRESENTATION`
- There is one new node, `RTG-OFN-DEF-FINITE-DESCRIPTION`; the atlas had no node for it before.
- The P2B node names `RTG-OFN-DEF-REDUCTION-TARGET`.
- The discrete imports carry the TDR-G v2.12.14 owner RIDs, as OFN's §11.2 has them. That covers the discrete-state node and the seven `*OFN:` discrete facts. The legacy names stay as aliases.

*Class C.*
- The five-row regularity table:
  - formal family;
  - real polynomial C1;
  - exactly transported C^∞ C2, which exists and is used;
  - analytic realization OPEN;
  - physical realization OPEN.
- SG-19 and the qualitative radius travel with it.
- The single κ table.
- The registration by RRF §6.2a.
- The lock node and its OFN-local `[ALG]` (real C^∞ lock surfaces, provenance SESSION).
- Realization: E2 holds only among generators with DX′(0)=0.
- FMS disposition: "primary realized smooth mathematical candidate family". Non-manifold sets and finite-amplitude regimes are outside the test.
- Lock imports carry SG-19, and the R9-conditional statements keep their assumption.

*Contract.*
- **Standard C:** the corrected local C³ manifold-germ test, with the physical-isolation scope sentence. The RID is retained (OFN11-C01).
- **Test class:** real C^∞ germs, with real-analytic laws as a distinguished subclass; Q6-REG stays C³ (OFN11-C02). The RID is retained as the same versioned contract, and consumers must assess the amendment.
- **Q3a / Q3b:** corrected-form wording; RRF-CND-01 is necessary, not sufficient.
- **Narrow-Q6:** single status `[from: ALG]` (OFN11-C03), the C^∞ C2 instance, and "¬ analytic or physical realization".

*Frontier.*
- OPA: smooth realization exists; identifying it with pole exchange needs its own contract.
- BANDWIDTH and SECTOR: dependencies carry the RIDs.
- TIME-INDEX: `NUMGEN-RESULT-N5AS1-L-BACKBONE`.
- P2B: the C^∞ witness, not closure.
- TRIAD-CLASS: next artifact as in v0.11; RRF §6.2a supplies the readout contract.
- Continuous closure: registry home FRUSTRATION / HOLONOMY-RANK.

*Admin queue (§12.3–§12.4).*
- XFER-O08-01 is deferred to TDR-G v2.13.
- REQ-O09-02, -03 and -04 are fulfilled.
- REQ-O09-05: the endpoint component is fulfilled; the custody component is deferred.
- REQ-O09-06 and REQ-O08-01 are open.
- The custody state follows §4 of the release record.

*Other D1 text.*
- Token-sum row: as in OFN §10. Σδ changes by −δ_A at a star event; nonconservation is not gauge dependence; the label question was referred to TDR-G.
- Notation: χ, N_ch in the chiral convention and in chiral attraction. The general ⊥ ρ/N line stays.
- Links line: PRIM-CTR is pinned at `dyad-v6.4.22`; L-BACKBONE carries its RID and the q_m typing.

*Consumers.*
- **H1:** the OFN side is fixed, with the five-row table. FMS and ER-2B residue remains (F5, DYAD.X1).
- **H4:** OFN repinned the twelve TDR-G imports.
- **H8:** the single κ table.
- **D2:** the `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` node and DYAD.X1 record OFN consumption.
- **D3:** the comparator consumer is v0.11.
- **D4a:** chiral coordinates name OFN's symbols. F2 and F5: the OFN side is fixed. F8 (i): OFN cites `er2b-v0.3`, and v0.3.1 stays source-reported.
- **OPENM.U7:** pinned at v0.11.

*L5 dispositions.*
- **Retired:** OFN.O1, O3, O4, O5, O7, O8 with co-key RRF.F6, O12, O13. Reasons are in `dispositions.json`; the GEN zero-origin residue of O5 moves to METH.M2.
- **Reworded:** OFN.O6 (residue: orientation vocabulary, §7.3 joint selection, OPEN-C19-L label), O9 (only the owner-kept IMP-O10-05 exception), O11, RRF.F5, DYAD.X1, F2, F5, F8, METH.M2, OPENM.U7, NUMGEN.N-I1.
- **Retained:** OFN.O10 (FMS P4, SESSION — unchanged in v0.11) and PROG.G8 (Programme not moved; OFN §11.4 still carries the convention).
- **New:** OFN.O14, a low-priority wording item. The v0.11 κ table calls γ≡κ "the declared parameter convention of Genesis §6.3c and RRF §6.2a", but `gen-v2.9` §6.3b–c contain no κ symbol (only the script name `kappa_pq_symbolic.py`). The declaration is OFN's and RRF's, so this is for the next OFN edition.

**RECOG v0.3.26 — D3 and H5.**
- **Identity:** the SOURCES row and the D3 header are moved to v0.3.26.
- **A1b node.** The atlas v0.7 node quoted the order sentence "E‴ = O_a((1+log(a+M_k))/(a+M_k))" for the v0.3.25 forms — the sentence RECOG retracted. It now reads:
  - |ε‴_k| ≤ E‴;
  - `[COR v0.3.26]`: the order holds for the corrected closed forms (Lg_corr, M-dependent bracket), and a pure O((a+M)⁻¹) is not claimed;
  - the v0.3.25 sentence is retracted (`RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325`), and the inequality and the grid values at M ≤ 10⁵ are unaffected;
  - the tail-harmonics limits were restated, and the v0.3.25 limits retracted (`RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325`);
  - it cites `RECOG-ART-A1C-CORRECTED-GRID`.
- **New nodes:**
  - `RECOG-ALG-A1C-RECIPROCAL-DRIFT` uses adopted Dyadic rows only: −29/216 exact, γ₂ = 212.6, K_ε = 0.7203/0.4513/0.1860, and the centring identity.
  - `RECOG-ALG-A1C-LOGFREE-ENVELOPE` is `[assuming: (D5)]`: ten non-negative terms, E^(5) ≤ C(a,r)/(a+M) for M ≥ 1, C = 58.0/61.0/75.1. The grid limit and the 73/73 containment are observations.
- **FAIL line:** lists the two retracted-statement identifiers. They are not live RIDs.
- **RECOG.R-D1:** names the two v0.3.26 artifacts; the owner ran the drift certificates.
- **RECOG.R-A1:** ENV joins the (D5)-conditional blocks, and DRIFT is unconditional on Dyadic proof constants. RECOG's two registration requests to DYAD are now filed as pipe items, open. In v0.7 the atlas said "not filed as pipe items", which was true at that snapshot.
- **H5:** one sentence for v0.3.26.

**Pipes (NUMGEN.N-I1).** The row is rewritten as a state summary at the snapshot: 33 items in 19 inboxes — 6 closed, 3 dispositioned, 24 open. The builder asserts the counts from the item files; `tools/pipes_index.py --check` passes.

The RECOG→ATLAS notice is dispositioned "accept", and this edition carries it. It is to be closed by the Atlas owner **after** the `atlas-v0.8` tag, not on this branch.

**Not changed on purpose:**
- the `*ATLAS:checked-D1` evidence record. It is dated ("sources as then read", EV-NOT-RERUN) and keeps its v0.1 wording, including the "OFN owner counts 11 DEF" line and the ρ notation; the stale guard skips `*ATLAS:checked-*` lines;
- the `*PROG:IF-register` (Programme not moved);
- RECOG's NUMGEN v1.20.8 pin (owner text);
- RRF's own κ=2 wording and "existence open" text (RRF.F3; RRF not moved);
- the D4a ER-2B/FMS rows beyond the OFN pointers;
- the R6 node (v0.3.26 changes no OPEN status).

## 3. Mechanical checks

**Build.** Two builds give identical bytes for the atlas and for all ten evidence files. Reproduce with `python3 -I evidence/atlas/build/refresh_v0_8.py`.

The builder asserts:
- the base hash;
- every source tag's hash and commit, and tag/snapshot equality;
- the OFN file = `38a2f444…e9e4` and the RECOG file = `45e307f8…dd34`;
- the presence of `RID: X` in the tagged sources for every newly cited RID: 6 OFN, 6 RECOG (4 live and the 2 retracted-statement identifiers), 14 TDRG and 1 NUMGEN;
- the 43 OFN RIDs;
- 10 record and pipe paths at the snapshot;
- the pipe-state counts;
- that no retired key is referenced;
- the stale-phrase guard (20 patterns);
- the retracted-sentence guard: "E‴=O_a(" only next to "corrected closed forms", and none of the three retracted limits.

**Shared checker:** zero FAIL.

| Check | PASS | Notes |
|---|---|---|
| sources | 72 | |
| coverage | 129 | |
| qualifiers | 3 | |
| links | 486 | |
| artifacts | 101 | |
| keys | 123 | |

Carried unchanged from v0.7:
- 5 link UNVERIFIED and 3 artifact UNVERIFIED;
- 11 DOCUMENTED-UNRESOLVED;
- 14 wording WARN, all at inherited sites. Two v0.7 WARN sites left with the reworded OFN rows ("pending TDRG", "N12 was not read"), and no new WARN site was introduced.

**H→L5 map:** no dangling key, no high row without an H, 118 L5 rows.

**Negative controls:** shared 18/18 and focused 8/8. The focused controls are:
- U1: H cites the retired OFN.O1;
- U2: a retired key is reused;
- U3: the SOURCES row is older than the manifest;
- U4, U7: a misspelled new OFN or RECOG RID. The shared checker's links check FAILs, "absent from owner … at its tag";
- U5: the retracted order sentence is left unqualified;
- U6: the stale class-C wording returns;
- U8: the compound narrow-Q6 status returns.

**Fidelity checks** were done by hand against the tagged files, not by the checker. Each is `EV-SRC-READ`, with the line numbers at the tags.

*OFN v0.11:*
- the six new DEF RIDs, by set difference with `ofn-v0.10`;
- IMP-O08-02…16 with their TDR-G RIDs (L1002–1087);
- the regularity table and the κ table (L466–475);
- Standard C and the physical-isolation scope (L444–446);
- narrow-Q6 and OFN11-C03 (L454–456, L1535);
- the C^∞ lock-surface `[ALG]` (L479);
- OPEN-3B, OPA and TRIAD-CLASS (L734–744, L902–918, L952–960);
- the §10 token-sum row (L978);
- §12.4 REQ states (L1394–1413);
- RF-O10-03 on `er2b-v0.3` (L1325–1327);
- the "for this draft" exception (L1286).

*GEN:* `gen-v2.9` L814–906 (§6.3b–c) contain no κ, and L1013 holds the κ_f remark.

*RECOG v0.3.26:*
- the corrected order sentence (L763);
- the corrected limits (L753);
- the drift and envelope blocks (L769–775);
- the two retractions (L1457, L1459);
- the artifact rows (L1269–1270);
- 13 occurrences of v1.20.8 and none of v1.21.

*Pipes:* the 33 item files' `state:` fields at `f8f3b5b`.

## 4. Questions for receiving review

1. **Class C.** Do the CLASS-C node, the realization, FMS-disposition and lock-import nodes, and H1 state OFN v0.11 at its scope? The scope points are:
   - C^∞ existence is used, while analytic and physical realization stay open;
   - SG-19 and the qualitative radius are stated where the constants travel;
   - E2 uniqueness holds only for DX′(0)=0;
   - nothing is promoted to analytic or physical.
2. **Contract amendments.** Do the Standard C and test-class texts reproduce OFN11-C01/C02 without strengthening? Is the atlas phrasing of the C02 RID retention ("same versioned contract — consumers assess the amendment") faithful to release record §3b item 1?
3. **Retirements.** Is any of OFN.O1, O3, O4, O5, O7, O8/RRF.F6, O12 or O13 still live in the owner text at `ofn-v0.11`? In particular:
   - RRF.F6 is retired as a co-key, although RRF did not move;
   - O5's zero-origin residue is moved to METH.M2.
4. **OFN.O14.** Is the γ≡κ attribution an atlas diagnostic, or owner wording below the atlas threshold?
5. **RECOG.**
   - Is the A1b correction faithful to the `[COR]` and to Appendix B: the order holds for the corrected forms; the v0.3.25 sentence is retracted; the inequality is unaffected; no pure O(1/(a+M))?
   - Do the DRIFT and ENV nodes keep the three distinctions — exact algebra, certified bound under `[assuming: (D5)]`, numerical observation?
6. Is anything in the 151-line diff outside the scope of §2?

## 5. Publication boundary

This build accepts nothing. Acceptance needs, in order:
1. the receiving review;
2. PI acceptance identifying the bytes `450d8e71…8e46`;
3. a merge commit (not squash) of `claude/atlas-v0.8` into `main`;
4. an annotated `atlas-v0.8` tag naming the hash.

After the tag:
- atlas tag verification;
- the release record `records/atlas/RTG_STATE_ATLAS_v0.8_RELEASE_RECORD.md`;
- closing `pipes/ATLAS/20261029-RECOG-v0-3-26-adopted.md`.

This build changes no owner DSN, grade, source tag, Method edition or consumer adoption. PR #118 (OFN tag verification) and PR #113 (tool) are independent of this candidate. `atlas-v0.7` remains the accepted Atlas until the acceptance decision.
