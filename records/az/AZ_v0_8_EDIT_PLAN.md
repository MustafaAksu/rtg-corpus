# AZ v0.8 — edit plan (scope and decisions before the candidate)

**[SESSION] NONCANONICAL. A plan, not an edition: it changes no DSN text, grade, pin or RID.** Prepared by the AZ co-owner (Claude) on 12 November 2026. The v0.8 cycle was started by the PI on 12 Nov 2026, 11:30 +03:00 ("başlatalım"; `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md` §11 item 6). Its content was fixed earlier: PI decision of 11 Nov 2026, 18:15 +03:00, row 5 (`records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` §5) — "v0.8 is the Programme §6.7 reduction together with the Methodology v1.4 migration" — and the open items of `records/az/AZ_v0_7_RELEASE_RECORD.md` §14. This note turns that into edit rows and names the decisions that are the PI's. v0.7 was made the same way (triage, PI decisions, then the edition).

Governing sources: AZ `az-v0.7` (file SHA-256 `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94`); Methodology `methodology-v1.4`; Programme `programme-v1.4`; `CONVENTIONS.md` on `main` `4138aa4`.

## 1. What was read for this plan, and what was not

- AZ DSN at `az-v0.7`: header, aliases, §§0–3, §4.1, §4.2, §4.3.2, §§6–10 read; the other Thread C subsections (§4.3.1, §4.3.3–§4.3.6), §5 and the appendices by outline and size only. They are AZ-owned and are not reduced by this plan; they will be read in full before the candidate.
- Methodology v1.4: §0.5, §1, §1.1, §4.2, §8.4, §13.6 read. §§3, 5, 10, 12 and the rest of §13 not reread for this plan; they will be before the candidate.
- Programme v1.4 §6.7 and the lines that name AZ; `CONVENTIONS.md` in full; `AZ_v0_7_RELEASE_RECORD.md` §14 and the triage rows 33–34; `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md` (written by this lane).
- `tools/dsn_lint.py` was run on the file (informational; §2).
- Added later on 12 Nov, after the second co-owner's evaluation (§7): the proof of PROP-AZ-CORE-EQUIV was checked step by step and a new finite check was run (§8).

## 2. Measured state of the file at `az-v0.7`

83,281 bytes, 600 lines. §1: 981 words (target 200–400). Header "Status summary": 1,486 characters. No `AI_CONTEXT_CORE_END` marker. Seven Appendix A entries. History phrases in live sections: 25 (`historical` 15, `superseded` 5, `no longer` 3, `was:` 1, `retained as` 1). 67 distinct RIDs. Sizes by block: Thread A (§4.1) 10,090 bytes; Thread B (§4.2) 7,149; Thread C (§4.3) 13,156; §1.2 3,581; Import Ledger (§8) 4,955.

Structure against Methodology §1: the file has ten sections, not the standard nine — its ledger is §4 "Three Threads", §6 is "Bridge-Candidate Connections", §7 is a note on the Programme, the Import Ledger is §8, the artifact registry §9, provenance §10. There is no Layer Routing section and no "Current Canonical State"; §1 is "Study Goal and Historical Origin".

## 3. Edit rows

### A. Methodology v1.4 migration (layout and grammar)

| # | Item | Proposed edit |
|---|---|---|
| A1 | Profile and section map | The file's class is *Infrastructure / diagnostic ledger*, for which Methodology §0.5 allows "standard layout or declared section map". **Decision D1.** |
| A2 | Header | v1.4 field order with **Scope** and **Document status**; *Status summary* reduced to 2–4 present-state sentences; "Major update (v0.6 at a glance)" removed (history; recoverable at `az-v0.6`); *Supersedes* = `az-v0.7` and its hash only; *DSN Methodology* = v1.4. |
| A3 | §1 | A "Current canonical state" of 200–400 words: what AZ owns and at what grade (engine `[ENG PASS]`, PROP-AZ-CORE-EQUIV, the low-order obstruction, the `4\|q` diagnostic as static geometry, Level A, AZ-2 not met), with pointers. Goal, success criterion and forbidden interpretation keep their statements (they are current `[DEF]`/`[OPEN]`/`[FAIL]` records) and move to the ledger; milestone narratives lose their version-by-version history. |
| A4 | Live-file rule §1.1 | Remove from live sections: version-scoped headings and notes ("§0.1 v0.6 Distributed-Ownership Map", "v0.6 note", "REVISED v0.6", "Resolved since v0.5", "Was: ACTIVE", the carried `[COR] v0.3` overlay in §4.1.2), §7 "Note on Programme Overview Update" (a pin, not a section), and the dated list of §10 (to one provenance paragraph plus Appendix A). Every removed passage is history recoverable at a tag; no current statement, scope, grade, RID, OPEN obligation or evidence pointer is removed. |
| A5 | Aliases (§8.4) | "All tags follow v1.2" → v1.4. `[ENG-planned]` expands to `[ENG]`, which §8.4 forbids for planned work: replace by an artifact status. `[NUM diagnostic]` is a Methodology alias and is declared as such. Mixed tags in live claims (`[THM-ALG]`, `[HEUR/NUM strong]`, `[ALG/FAIL]`, `[THM/ALG in source]`) are unpacked into the exact assertion and its corroboration. For PROP-AZ-CORE-EQUIV this is **Decision D3**. |
| A6 | Identifier owner map (§4.2) | No rename. One owner-map block: `PROP-AZ-CORE-EQUIV`, `TDRG-AZ-STATIC-ZN-4Q`, `DEF-AZ-CORE`, the `CONV-AZ-*` keys, `SG-AZ-0.4` and the exporter's self-identifier `TDRG-AZ-EXPORT-BASELINE` are AZ identifiers; a `TDRG-` prefix in two of them names the object they describe, not the custodian (TDR-G declares no such RID). |
| A7 | Layer routing and context-core marker | A short routing table (three threads: model, state space, owner, allowed use, required bridge) built from the existing §0.1 map and the guards, and the `AI_CONTEXT_CORE_END` marker. No new statement; **mapped row by row to its source lines**. |
| A8 | Appendix A | One compact entry per edition; the v0.6 and v0.7 entries shortened to what §1 "Appendix A" requires, their full text staying at the tags and in the release records. Appendix B unchanged. |

### B. Programme §6.7 reduction (duplicated owner-science summaries)

| # | Item | Proposed edit |
|---|---|---|
| B1 | Thread A §4.1.1 | Seventeen Dyadic results are restated in full here (statement, formulas, boundary cases) **and** listed as rows in §8. Proposed: the full restatements go; §8 keeps one row per RID with a short readout that carries the load-bearing qualifications now in §4.1.1 — the row wording is fixed in stage 1, see §5 — (e.g. the `p ≥ b+2` boundary, "raw one-step map, not the `p`-step map", "dyadic-map scope; all-`b ≥ 5` OPEN", "OPEN-M transfer `[CAND/conditional]`"). Thread A becomes: ownership line, pointer to §8, and AZ's own `[HEUR]` reading (§4.1.3). **Decision D2** (depth of the reduction). |
| B2 | §1.2 | Five of the same Dyadic results are stated a third time as "historical motivation". Proposed: keep the `[HEUR]` motivation and scope statement; cite the five by RID. |
| B3 | Thread A §4.1.2 | The owner's open frontier (five bullets) is Dyadic's OPEN 9 list. Proposed: one sentence and the pointer to Dyadic §2. |
| B4 | Thread B §4.2 | Nine TDR-G items restated (state space, reachability, retrigger, spectrum conservation, BIND3, `k/N` scaling with the fitted exponent, TDR-26, TDR-24). Proposed: as B1 — §8 rows with the qualifications (e.g. "window-dependent exponent, not a structural constant", "period dividing 2", "gcd multiset as a consequence only", "classifier `[HEUR]`"). Kept in the thread: the bridge-candidate status, `AZ-OPEN-SCOPE-ARITH` with its question, and "What Thread B does not contain". |
| B5 | §6 | Bridge-candidate connections keep their records (they are AZ's `[bridge-candidate]` / `[bridge-disqualified]` / `[OPEN]` items); restated owner facts inside them are cut to RID and pointer. |
| B6 | Not touched | Thread C (§4.3), §3 guards, §5, Appendix B. No merge with DZT (Programme §6.7). |

Expected size after A and B: roughly 60–65 KB (from 83 KB). The figure is an estimate, not a target.

### C. Corrections with content (stage 1)

| # | Item | Proposed edit |
|---|---|---|
| C1 | §9 availability | v0.7 says none of the artifacts is in the repository. Since 11 Nov a partial recovery is on `main` (`upload/az-records/`, hash-checked in `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md`). Per artifact: `AZ-ART-AZV5-REGISTRY` — registry file and nine of its ten entries present with equal hashes, the tenth (benchmark report) regenerated, not the original bytes; `AZ-ART-AZ1B-CERTIFY` — present, hash-equal; `AZ-ART-CONVENTIONS-FROZEN` — a file of that name is present but is not shown to be the frozen state the DSN cites (C2); AZ-1A and the synthetic scope of AZ-1B replayed (`evidence/az/az_v5_replay/`). Still not in the repository: `phase2_harness`, AZ-1C, `AZ-ART-SPECTRAL-RADIUS-PATCH`, `AZ-ART-PROP-CORE-EQUIV` (prover and certificates), `AZ-ART-ANTIPODAL-LOWORDER`, `AZ-ART-PHASE2-N120-CORE` (the registered reports; one unregistered smoke report is present), `AZ-ART-THETA-CORE-MATCHED`, `AZ-ART-ZETA-V3`; these stay source-reported (`EV-SRC-REPORTED`, `EV-NOT-RERUN`). Evidence states by the v1.4 keys. No grade is changed by availability; what each `[ENG PASS]` rests on is stated. |
| C2 | Conventions file | The recovered `CONVENTIONS_FROZEN.md` does not contain `CONV-AZ-ANGLE-ZERO` (which the §9 row lists among its contents) nor `CONV-AZ-MANIFEST`. Stated as found: the row says what the deposited bytes contain and that the frozen state the DSN cites is not available; the conventions themselves stay as the DSN states them. |
| C3 | `G_birth(w)` | The conventions file and the exporter define it differently (hash-check record §3). Both definitions are recorded with their locators; none is chosen; SG-AZ-5 already requires the graph object to be declared per result. An `[AZ-OPEN]` or an issue line names the mismatch. |
| C4 | Exporter | Its identity (`TDRG-AZ-EXPORT-BASELINE`, A6), its hash, and the fact that `lib/graphio` does not load its output without an adapter (replay record). |
| C5 | Pins | Dyadic is at `dyad-v6.4.24`; AZ pins v6.4.23. The diff between the two tags touches lines that carry eleven of the thirteen cited Dyadic RIDs. Stage 1 reads each against the Dyadic v6.4.24 release record and repins row by row; a changed owner statement is taken over as the owner states it. Not done in this plan. TDR-G, Genesis, OPEN-M, Programme: unchanged since v0.7. |
| C6 | Action 1 diagnostic | Only by **Decision D4**. If it enters: one `[NUM diagnostic]` block, AZ-owned, with a new RID (proposed `AZ-NUM-TOKRES-S1`), stating PC1 and PC2 with their intervals, the engine, profile, cell, horizon and threshold, the scope of the report §7 verbatim in substance (no mechanism, no `N`-scaling, no TDR-26, no OPEN-P1 link, no relation to the `4\|q` rule or to DZT `q = 4`), evidence by path and hash, and the outcome rule. AZ-2 and `AZ-OPEN-PROMO` are not changed by it. Built as a separable commit. |

## 4. Decisions for the PI

- **D1 — section map.** (a) *Declared section map*: keep the three-thread ledger and the current numbering, add the missing functions (current state, routing, marker) and declare the map in the header. Consumers' pointers stay valid (Programme IF20/IF21 cite "AZ §8"; TDR-G cites an AZ RID). (b) *Standard layout*: renumber to §0–§9; the Import Ledger becomes §7 and the registry §8, and Programme §7.2 then points at the wrong section until its next edition. Recommended: (a). Both are allowed by §0.5.
- **D2 — depth of the reduction.** (a) *Ledger rows only* (B1, B4 as written): the largest reduction; a reader needs the owner DSN for any formula. (b) *One-line readouts kept in the threads* as well as in §8: about 5 KB larger; the threads stay readable alone, at the price of a second place to keep in step with the owners. Recommended: (a), because every drift corrected in v0.7 came from restated owner text.
- **D3 — PROP-AZ-CORE-EQUIV under v1.4.** The bare `[THM-ALG]` is not a v1.4 tag. The text gives a proof sketch for all finite simple graphs and an exhaustive machine check up to seven vertices; the prover and certificates are not in the repository (C1). Options: (a) `[THM]` for the statement with the written proof as its basis, and the enumeration recorded separately as corroboration; (b) `[ALG]` scoped to the checked range with the general statement `[HYP]` until the proof is written out in the repository. This is a grade decision and therefore the PI's. **Recommended since §8: (a)**, with the complete proof of §8.2 in the DSN, the lost certificate kept as source-reported and not described as rerun, and the new check of §8.3 cited as what it is. The proof was proposed by the second co-owner and checked by this lane; the candidate's review is its independent reading.
- **D4 — Action 1 diagnostic in v0.8 or not** (the outcome rule makes it eligible; it does not decide). Entering it now ties v0.8's review to an empirical block; leaving it out keeps v0.8 a pure migration. Recommended: leave it out of v0.8. Its entry in a later edition is a separate PI decision on the Stage 1 result in its own scope; it does not wait for Stage 2.

## 5. Procedure

Two stages (Methodology §13.6, `CONVENTIONS.md` §4): **stage 1** = rows C1–C5, A5, A6, the proof text of D3, the wording of the §8 ledger rows that B1, B2, B4 and B5 will rely on, and the routing table of A7 (and C6 if D4 says so), built by an assertion-gated script, intermediate hash recorded, change-focused review; **stage 2** = rows A1–A4, A8 and the removals of B1–B5 with a movement map checked by `tools/check_compaction.py` and its negative controls against the intermediate. Then PR, review by the second co-owner, PI decision, release record, status-lines commit; the PI merges and tags `az-v0.8`. Notices by pipe items to PROG (its §6.7 and §9.2 rows for AZ), TDRG, DYAD, DZT and ATLAS, listed in the release record. `pipes/AZ/` is read again before the stage-1 freeze.

Why the ledger wording is in stage 1 (condition of the second co-owner, §7, accepted): Methodology §13.6 lets no new substantive statement enter through the compaction stage, and its checker does not certify paraphrase. A readout that states an owner result with its qualifications is a scientific statement. So every §8 row that has to carry a qualification now stated only in a thread is worded in stage 1 and reviewed there against the owner text at the pinned tag; the same holds for the routing table, which is new text even though it states nothing new. Stage 2 then only removes: each removed restatement maps to an unchanged stage-1 row and to the owner locator, and a removal that would lose a qualification fails the check.

## 6. Not in v0.8

AZ-2 (a dynamical, non-substrate observable), the analytic completion of the `4|q` mechanism and transfer-zeta poles; Stage 2 and Stage 3 of Action 1; the still missing Thread C files; any change to Level A.

## 7. Second co-owner's evaluation of this plan (12 Nov 2026)

Source: a text by the second co-owner (ChatGPT), relayed by the PI to this session on 12 Nov 2026 at 12:42 +03:00; no review of PR #236 was on GitHub when this section was written. It says of itself that it does not replace the PI's decisions. Its recommendations: D1 (a); D2 (a); D3 (a), on condition of a complete general proof; D4: not in v0.8. Its conditions and how they are taken up here:

1. *D2: no new scientific statement through the compaction stage.* Accepted; §5 now puts the ledger wording into stage 1.
2. *D3: the missing certificates neither demote the general statement nor can a finite scan to seven vertices stand in for a written proof; a complete proof goes into the DSN and is reviewed; the old scan stays as separate, historical support and is not shown as rerun.* Accepted. The proof it proposes was checked and written out (§8).
3. *D4: the diagnostic's later entry is not tied to Stage 2.* Accepted; D4 reworded.

Both co-owners now recommend the same four choices. They remain the PI's decisions.

## 8. PROP-AZ-CORE-EQUIV — proof and a new finite check (for D3)

**[SESSION] Proposed text and a session check; nothing here changes the grade in the adopted file.**

### 8.1 Statement and what it depends on

Let `G` be a finite simple undirected graph (no loops, no multiple edges), exported with both orientations: every edge `{a,b}` gives the directed edges `(a,b)` and `(b,a)`. The Hashimoto transition digraph has these directed edges as its vertices and a transition `(u,v) → (v,w)` whenever `w ≠ u`. Let `R(G)` be the set of directed edges that lie on a directed cycle of that digraph — DEF-AZ-CORE as written in the deposited `upload/az-records/CONVENTIONS_FROZEN.md` ("directed edges that belong to at least one directed cycle under the non-backtracking transition rule"). Let `H = core₂(G)` be the 2-core: the largest subgraph of `G` in which every vertex has degree at least 2 (possibly empty).

**Claim.** `R(G)` is the set of both orientations of the edges of `H`.

A directed cycle of the transition digraph is the same thing as a closed walk `v₀, v₁, …, v_L = v₀` in `G` with `v_{i+1} ≠ v_{i−1}` for **every** `i`, indices mod `L` — non-backtracking also where the walk closes. That reading is essential: if backtracking is allowed at the closing point, a pendant path attached to a cycle is covered by a closed walk and the claim is false (§8.3, negative control). The claim also needs both orientations and a simple graph.

### 8.2 Proof

*Two standard facts.* (i) The union of two subgraphs of minimum degree ≥ 2 has minimum degree ≥ 2, so `H` exists and contains every subgraph of minimum degree ≥ 2. (ii) Deleting vertices of degree ≤ 1 with their edges until none is left yields `H`: a vertex of `H` never reaches degree ≤ 1, and what is left has minimum degree ≥ 2. An edge is deleted only with one of its endpoints, so `H` is the subgraph induced on its vertex set — which is what the exporter's `recurrent_core_directed` keeps.

*`R(G)` lies in the orientations of `E(H)`.* Let `W = v₀, …, v_L = v₀` be a closed walk, non-backtracking at every index mod `L`, and let `S` be the subgraph formed by its edges. At each `v_i` the walk uses the edges `{v_{i−1}, v_i}` and `{v_i, v_{i+1}}`; they are distinct because `v_{i−1} ≠ v_{i+1}` and `G` has no multiple edges. So every vertex of `S` has degree ≥ 2 in `S`, and `S ⊆ H` by (i).

*Every orientation of every edge of `H` is in `R(G)`.* Let `e = {u,v} ∈ E(H)`.

Case 1: `e` is not a bridge of `H`. Then `e` lies on a simple cycle of `H`, of length ≥ 3 because `G` is simple. Traversed in either direction it is a closed walk that is non-backtracking at every index, and the two directions contain `(u,v)` and `(v,u)`.

Case 2: `e` is a bridge of `H`. Let `A` and `B` be the components of `H − e` containing `u` and `v`. `A` contains a cycle: otherwise `A` is a tree; if `A` is the single vertex `u`, then `deg_H(u) = 1`; if `A` has at least two vertices it has at least two leaves, one of them `x ≠ u`, and `deg_H(x) = deg_A(x) = 1`; both contradict minimum degree ≥ 2 in `H`. Likewise `B` contains a cycle. Choose simple cycles `C_A ⊆ A`, `C_B ⊆ B`, a shortest path `P_A` in `A` from `u` to `C_A` ending at `a ∈ C_A`, and a shortest path `P_B` in `B` from `v` to `C_B` ending at `b ∈ C_B` (either path may have length 0). A shortest path to a cycle meets it only in its last vertex. Consider the closed walk

`u →(e)→ v →(P_B)→ b →(once around C_B)→ b →(P_B reversed)→ v →(e reversed)→ u →(P_A)→ a →(once around C_A)→ a →(P_A reversed)→ u`.

It is non-backtracking at every index, including the closing one: inside a simple path or a simple cycle of length ≥ 3 no step reverses the previous one; at `v` the edge `e` is followed by the first edge of `P_B` or, if `P_B` is empty, by an edge of `C_B`, both in `B` and so different from `e`; at `b` the walk arrives by the last edge of `P_B`, which is not in `C_B`, leaves along `C_B`, returns by the other edge of `C_B` at `b`, and leaves by the last edge of `P_B` again — consecutive edges differ each time (if `P_B` is empty, the edges at `b = v` are `e`, the two cycle edges, and `e`, and consecutive ones differ); on the way back the last edge before `e` reversed is the first edge of `P_B` or an edge of `C_B`, different from `e`. The `A` side is the same, and the walk closes at `u` arriving by an edge of `A` and continuing with `e`. The walk contains `(u,v)` and `(v,u)`.

So both inclusions hold. ∎

Remarks for the DSN text. No strong connectivity of the whole transition digraph is used or claimed (a single cycle gives two components, one per direction); the claim is membership in *some* directed cycle. The proof is of the equality of edge sets; it says nothing about spectra.

### 8.3 New finite check (`EV-CODE`, `EV-RUN` in this session; not the lost certificate)

`evidence/az/core_equiv_check/az_core_equiv_check.py` (SHA-256 `bd1ee6f7bf31a3db35f88d45006ff7c1f8ac32960a2bf9cf178ed228d6170b9a`), output `evidence/az/core_equiv_check/output_nmax7.txt`; Python 3.13.18, session container, 12 Nov 2026; command `python3 -I evidence/az/core_equiv_check/az_core_equiv_check.py --nmax 7 --jobs 2 --hashimoto upload/az-records/az_v5/lib/hashimoto.py --exporter upload/az-records/export/conv_az_graph_export.py`, exit code 0.

- `R(G)` computed from the definition (transitions, strongly connected components by an own Tarjan) against the 2-core by leaf stripping, on **all labelled simple graphs with 1 to 7 vertices: 2,131,019 graphs, 0 mismatches** (2,097,152 of them on 7 vertices; 2,060,191 of those with a non-empty 2-core — the remaining 36,961 are the labelled forests, as they must be).
- On all 1,099 labelled graphs with at most 5 vertices: the own transition relation equals the deposited library's `build_hashimoto` (`9cc21379…1b70`), and the deposited exporter's `recurrent_core_directed` (`fab14ae1…fe1e`) equals both sets. 0 mismatches.
- Named cases (lollipop, barbell, dumbbell, theta, figure-8, a cycle hanging on a tree): equal.
- Negative controls, each reporting a difference as it must: closed walks allowed to backtrack at the closing point (lollipop; 410 of the 1,024 labelled graphs on 5 vertices); no stripping (path); one directed edge per pair instead of both orientations (triangle).

What this is not: it is not `prove_core_equiv.py` or its certificates, whose bytes are not available, and the source-reported figure of 2,141,014 graphs is not reproduced or explained by it. A finite check corroborates the statement on the checked range; the basis of a `[THM]` grade would be the proof of §8.2.
