# Ontological Foundations (OFN) — owner disposition of the v0.10 advisories (co-owner session claude012ZC8x)

**Date:** 29 October 2026.
**By:** Claude, OFN co-owner session `claude012ZC8x`. This is the session that wrote the v0.8.2 handoff, OFN v0.10 Draft 1 and Draft 2, `release_ofn_v0_10.py` and the v0.10 release record.
**Status:** owner disposition record, written separately (step 2 of the entry note). Nothing is built, adopted or released by this record. The other co-owner session writes its own; I have **not** read it. The joint reconciliation follows, and the PI decides what remains open.

**Object.** `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` at `ofn-v0.10`, SHA-256 `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`, recomputed from the tag (`EV-HASH`). Line numbers below refer to that file.

**List dispositioned.** The 29 merged rows of `records/ofn/ATLAS_ADVISORY_OFN_v0_10_RECONCILIATION.md` §3, read with its §5 correction.

**Inputs read (`EV-SRC-READ`, at `main` `b0dc6dbe`):**
- `CONVENTIONS.md`; `pipes/README.md`;
- `records/ofn/OFN_COOWNER_ENTRY_NOTE.md`;
- the two atlas advisories and their reconciliation;
- the three `pipes/OFN/` notices;
- `records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`.

**Owner statements checked at their tags myself, not taken from the advisories:**
- `dyad-v6.4.22` §1 L47–49, OPEN 20 L258–266, §6.17 L1026–1040, §7 notice table L1113–1138;
- `gen-v2.9` §6.3a–§6.3c L53–59, L865–903;
- `rrf-v0.8.4` §6.2 L403–424 and §6.2a L426–437;
- `tdrg-v2.12.14` SG-3 L445, SG-14 L478, §6.1–§6.5 RID blocks, §6.3 L586–592, §7 L865–915;
- `numgen-v1.21` L59–73, L2154–2156, L2773–2774;
- `recog-v0.3.26` header, the twelve RID blocks OFN cites or may cite, and the R9 table L643–662;
- `triad-v1.6.1` L9, L67, L787, L864–888.

**Evidence for this record.** `evidence/ofn/disposition/ofn_v0_10_owner_disposition_checks.py` (SHA-256 `bb62a6c8…7bff`) with its output `…_output.txt` (`537419c2…25f7`); exit 0, ALL PASS.
- It recomputes the SHA-256 of the eight files at their tags; all equal `BASELINE.md`.
- It finds the 60 owner phrases and RID blocks this record relies on.
- It checks the RECOG freeze record hash and its "Fulfils REQ-O09-02" line.
- It checks two one-line algebraic facts (rows 1 and 11).
- It runs four negative controls, which fail as required.

This is an independent contribution under Methodology v1.4 §12.3, not a rerun of any owner certificate.

## 1. Row 1 (P0) — class-C realization: **accept with change**

**Owner state, verified.**
- **DYAD v6.4.22, OPEN 20 (L260):** "PARTIAL — B-∞ existence **CLOSED (v6.4.18)** by `DYAD-THM-SMOOTH-EMBEDDING` … B-an and B-6 ACTIVE".
- **`DYAD-THM-SMOOTH-EMBEDDING` (L1028), E3–E4:** the $C^\infty$ germs $K_6=F^{1/6}$ and $J=T\circ K_6^{-1}$ exist, with $J^6=\mathrm{id}$, $DJ(0)=A$, $JT=TJ$. They are unique only in the F2/F3 sense; E2 gives uniqueness only among generators with $DX'(0)=0$, and the radius is qualitative.
- **`DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (L1034):** $\Phi=\tfrac16\sum_k A^{-k}J^k$ is a $C^\infty$ local diffeomorphism with $\Phi J=A\Phi$ and $[\Phi T\Phi^{-1},A]=0$. Scope: "inherits none of the finite-chart bounds of §6.14 (SG-19); no analyticity". The owner leaves the decision to us: "whether Genesis C2 or OFN class C uses it is their owners' decision".
- **Genesis v2.9 G-20 existence note (L899):** "(C2) is non-vacuous at $C^\infty$".
- **RRF v0.8.4 §6.2a regularity field:** transporting class C into that chart is "a conditional RRF reading; OFN/Genesis have **not** separately adopted the resulting class-C family".

**Decision.**

1. **Import both RIDs at `dyad-v6.4.22`.** They become new ledger entries IMP-O10-06 (`DYAD-THM-SMOOTH-EMBEDDING`) and IMP-O10-07 (`DYAD-THM-SMOOTH-EQUIVARIANT-CHART`). Final numbering is the build's choice; I recommend continuing the IMP-O10 series because the import grammar is unchanged. IMP-O10-04 keeps Lemma F and F3, and its OPEN 20 status line is restated to the owner's current line.

2. **One regularity table** at §5.5.4, replacing the current Regularity row (L475). The other sites point to it.

   | Heading | Status | Basis |
   |---|---|---|
   | Formal | holds | §5.5.4 formal construction; IMP-O10-03 |
   | Real polynomial representatives (instance C1) | real $C^3$ germs, Q6 by narrow-Q6 (ii) | IMP-O10-02 |
   | Exact transported $C^\infty$ realization (instance C2) | **exists**: $\mathcal F_{\kappa,\Phi}=(\Phi^{-1})^{\times3}\circ P_\kappa\circ N_\Phi^{\times3}\circ\Phi^{\times3}$ with the owner's $\Phi$ | IMP-O10-06/07; the OFN algebra below |
   | Analytic realization | OPEN (DYAD B-an, B-6) | IMP-O10-04 |
   | Physical realization or selection | OPEN | OPEN-OFN-TRIAD-CLASS; SG-OFN-SELECTION |

3. **New OFN-local algebra, stated with its grade.** `[ALG]` If $[N_\Phi,A]=0$ then $N_\Phi$ is odd ($A^3=-I$) and $\omega$-equivariant ($\omega=A^2$). So the exact Standard C statements on $\mathcal S_0$ and $\mathcal S_\pm$, and the invariance of those surfaces, hold for $\mathcal F_{\kappa,\Phi}$ by the same two-line computation as in the formal case. The lock surfaces of the $C^\infty$ member are therefore real $C^\infty$ invariant submanifolds. In raw coordinates $G=J^2$ and $R_0=J^3$ are $C^\infty$.

   This is a consequence the importing owner derives, not a new Dyadic claim, and it adds no RID. My check script verifies only $A^3=-I$; the rest is the two-line identity.

4. **Restate the nine sites at this scope.**
   - §5.5.3 (ii), L463: drop "whose existence is not asserted"; C2 is non-vacuous at $C^\infty$ by IMP-O10-07.
   - §5.5.4, Regularity row and Realization bullet.
   - §5.5.5, class-C row: "primary formal candidate class; a real $C^\infty$ realization exists (mathematical); analytic membership open; not physical".
   - §5.5.6, "conditional on the real surfaces (J)": the surfaces exist in $C^\infty$.
   - §5.5.8: "no analytic or physical realization asserted".
   - IMP-O10-04.
   - OPEN-OFN-3B input: the witness is a $C^\infty$ witness. Whether it is an *independently specified* $T_3$ (§8) stays undecided, and 3B stays ACTIVE.
   - OPEN-OFN-TRIAD-CLASS dependencies: "DYAD OPEN 20 (realization of $J$)" becomes "DYAD B-an/B-6, only if an analytic model is wanted".
   - OPEN-OFN-OPA input: "existence remains open" becomes "analytic existence remains open; a $C^\infty$ realization exists". The pole-exchange contract stays required.

5. **Scope that must travel with it.** Row 4 is one part. In addition:
   - uniqueness of $J$, $K_6$ and $R$ only in the DYAD F2/F3 sense;
   - no statement that class C is analytic, physical or unique;
   - Q1–Q6, Standard C, the raw-carrier no-go and the FMS ranking logic are unchanged.

6. **Receipts and notices.** Record receipt of DYAD notice N14. Notices after the tag go to DYAD, GEN, RRF and FMS/ER-2B (rows 27–28).

7. **Observation, no claim.** $J$ is unique and $\Phi$ is a fixed average of $J$. The $C^\infty$ member $\mathcal F_{\kappa,\Phi}$ therefore has a definite ψ-modulus value $m$, relative to the reference normal form; the cubic part of the equivariant change between $N_\Phi$ and $N$ is a single $a\,z^2\bar z$ term.
   - This is a *mathematically* distinguished member. It is not a physical selection (SG-OFN-SELECTION; OPEN-OFN-TRIAD-CLASS).
   - Computing that $m$ is a well-posed FMS or OFN SESSION task, which I propose to list under OPEN-OFN-TRIAD-CLASS "Next required artifact" as optional.
   - It does not enter the live text as a claim.

## 2. Row 2 (P1) — test-class admissibility: **accept with change**

**The issue.** §5.5.1 (L435) declares "Real-analytic laws form the admitted continuous FMS test class". §5.5.4 (L475) has always contemplated a $C^\infty$ class-C realization. The two rows were already in tension in v0.10, and row 1 makes the tension live.

**Decision.** Keep analytic laws as the **default** FMS test class. Record that **class C declares its own regularity in its §5.5.4 contract**, where the exact transported $C^\infty$ member is admitted *as a class-C model*. A $C^\infty$ member is therefore not a member of the analytic default class, and neither is it excluded from class C.

Reasons:
- **Nothing load-bearing needs analyticity.** Q1–Q6 and every theorem used (Q6-REG, Lemma S, the Genesis RIDs) are stated at local $C^3$.
- **RRF v0.8.4 §6.2 already takes the same position:** "A $C^\infty$ carrier may be studied as a **candidate**; this does not choose it over an analytic carrier". This decision matches it.
- **Widening the default class for all FMS tests is a separate decision** that would admit flat perturbations of the raw family. It changes FMS and ER-2B dispositions and needs no decision now. I record it as **defer**, to be taken only if a consumer asks.

**Wording proposal** (§5.5.1 Regularity row; one sentence added):

> "Class C declares its own regularity row in §5.5.4; its exact transported $C^\infty$ member is admitted under that contract and is not a member of the analytic default class."

**Edition.** The corrections edition, as a point-of-use limitation with this decision. It is a scope statement that removes an existing inconsistency, not a widening of the default class. If the other co-owner prefers to hold the decision for the migration edition, I accept the limitation note alone in the corrections edition.

## 3. Row 3 (P1) — Standard C's "nonempty": **accept with change; a `[COR]`**

**The issue.** `RTG-OFN-DEF-STANDARD-C` (L453) asks for "a nonempty $F$-invariant regime $\mathcal R$ on which $I_e=O(|r|^4)$".

The wording is defective in two ways, not one:
- the singleton $\{0\}$ satisfies it vacuously ($T(0)=0$, $F_\kappa(0)=0$, $I_e(0)=0$), as pass 2 found;
- an invariant set **bounded away from 0**, for example a periodic orbit, satisfies a big-O bound vacuously with a large constant.

The intended content is local at 0. It is exactly what the raw-carrier no-go excludes (positive-dimensional $C^3$ invariant submanifolds through 0) and what the class-C lock surfaces satisfy.

**Decision.** A `[COR]` (Methodology v1.4 §7), in the corrections edition.

Old text:

> "Standard C holds if there is a nonempty $F$-invariant regime $\mathcal R$ on which $I_e=O(|r|^4)$ for every edge $e$"

New text:

> "Standard C holds if there is a nontrivial local $F$-invariant regime $\mathcal R$ — an $F$-invariant set with $0\in\overline{\mathcal R\setminus\{0\}}$ — on which $I_e(X)=O(|r|^4)$ as $X\to0$ in $\mathcal R$, for every edge $e$. Its smooth form, used by `RTG-OFN-ALG-RAW-STANDARD-C-NOGO`, is a positive-dimensional $C^3$ invariant submanifold through 0."

Why this is a correction and not a strengthening:
- **The intended meaning is unchanged.** The no-go already quantifies over positive-dimensional submanifolds. The class-C surfaces $\mathcal S_0$ and $\mathcal S_\pm$ meet the new text. §5.5.5 already lists non-manifold invariant sets as a loophole of the no-go, and they stay one: the new text admits them as regimes, and the no-go does not exclude them.
- **The FMS disposition is unchanged.**
- **One question is deliberately not decided here:** whether every edge must be nonzero on $\mathcal R$. $\mathcal S_0$ has $r_3=0$, and coincidence is part of the contract (Q5). Any stronger "physically admissible isolation" reading stays under OPEN-OFN-TRIAD-CLASS, which already names it.

The old and new text go to Appendix B with the build hash.

## 4. All 29 rows

Editions: **C** is the corrections edition and **M** the Methodology v1.4 migration edition (staging in §5).

| # | P | Verdict | Edition | Change, reason or condition |
|---|---|---|---|---|
| 1 | P0 | **accept with change** | C | §1. Import both DYAD RIDs (IMP-O10-06/07); five-row regularity table; OFN-local `[ALG]` lock-surface statement for $\mathcal F_{\kappa,\Phi}$; nine sites restated; N14 receipt. The Bochner-member $m$ observation is listed as an optional task, not a claim |
| 2 | P1 | **accept with change** | C | §2. Analytic stays the default FMS test class; class C's own §5.5.4 contract admits the $C^\infty$ member. Widening the default class: **defer** |
| 3 | P1 | **accept with change** | C | §3. `[COR]` with old/new text: nontrivial local regime ($0$ an accumulation point), with the smooth form named. "All edges nonzero" not decided; stays under OPEN-OFN-TRIAD-CLASS |
| 4 | P1 | accept | C | Verified at L1036. In the Φ chart the IMP-O10-05 statements hold qualitatively; their constants stay edgewise in the dyad chart where they were proved. R9 stays a stated assumption (OPEN 21 / T1 / T2). No off-surface or basin transfer |
| 5 | P1 | **accept with change** | C | Record RRF §6.2a as the delivered model-contract row (§5.5.4 Registration row; RF-O10-01; O10-P3 done). I judge §6.2a's second entry to be the **representation-level** readout contract (clock, chart, reflection limit, no promotion to chirality); it is not a physical readout. OPEN-OFN-TRIAD-CLASS "Next required artifact" becomes: "a physical selection criterion; RRF §6.2a supplies the representation-level readout contract; the sign scalar for $m-m_*$ is needed only if a physical readout is sought". γ≡κ is a parameter convention, not raw/transported identity |
| 6 | P1 | accept | C | One κ-value table in §5.5.4; §5.5.3 (i), §5.5.5 and IMP-O10-01 point to it. No content change |
| 7 | P1 | accept | C | Verified at L872/L880. At the six sites: "statement accepted by TDR-G (tdrg-v2.12.14 §7, `EV-CODE` against the engine); custody XFER-O08-01 deferred by TDR-G to v2.13; RID remains OFN's". The proposal stays open and is not re-asked |
| 8 | P1 | **accept with change** | C | Verified at L586–592, L478. Record REQ-O09-05 as answered **at the owner's scope**: canonical branch `bound_symmetric`; other policy branches "only once their covariance is separately established" (SG-14); the N=24 equivariance check is finite (`TDRG-NUM-…`); `largest_center` is a recorded exception. IMP-O08-15 "endpoint question not discharged" becomes "discharged on the canonical branch at SG-14 scope". OPEN-OFN-2: covariance record delivered, six-constraint list not recovered. 2c=0 is not a covariance theorem for all policies |
| 9 | P1 | **accept with change** | C | Repin the TDR-G imports to `tdrg-v2.12.14` with the owner RIDs. I checked all fourteen RID blocks; the statements are unchanged except LEM-RETRIG (row 10). Keep OFN's existing caveat at IMP-O08-02, because `TDRG-DEF-PHYSICAL-STATE` still says "Only $\Delta_{ij}$ are physical" (L533) and OFN does not use that phrase to delete tokens. Numerical uses carry `[conv: v18]` and `EV-NOT-RERUN`. Legacy names stay as ledger aliases |
| 10 | P1 | accept | C | LEM-RETRIG now reads "a 2-cycle for $d\ne0$, a fixed point for $d=0$". OFN text already matches. Close the request; keep the OFN08-C12 archive entry |
| 11 | P1 | **accept with change** | C | New §10 reading (L984): the owner names rule, action and observable. The common token shift is outside $G_{\rm cov}$ and is "a symmetry of the birth-free sector only, not a gauge" (SG-14). By TDRG-DEF-STAR, $\Sigma\delta$ changes by $-\delta_A \pmod N$ at a star event and is conserved by the token permutations (checked). The operative reason $P$ is not a conserved physical quantity is therefore **nonconservation at births, not gauge dependence**. Row text: "rejected as an exactly conserved physical quantity on the birth-capable model (nonconservation at star events); not a gauge artifact under the owner's SG-14". **Finding for TDR-G**, by `kind: finding` item after the joint reconciliation: SG-3 (L445) and §2/Appendix still label $P$ a "gauge artifact", in tension with SG-14. TDR-G decides |
| 12 | P1 | accept | C | REQ-O09-03 fulfilled (`NUMGEN-RESULT-N5AS1-L-BACKBONE`; $q_m$ typed at L2154). Consumer rows go to v1.21. "Dedicated L-BACKBONE RID requested" retires. No domain inclusion is inferred. NUMGEN inbox notice: `accept` |
| 13 | P2 | accept | C (pin) | NG-7A navigation only; FRUSTRATION PARTIAL and HOLONOMY-RANK ACTIVE unchanged |
| 14 | P1 | accept | C | Per §5 of the reconciliation: REQ-O09-02 is fulfilled by `records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (`5c00f66d…9b55`, recomputed; "Fulfils REQ-O09-02"). The six "freeze candidate" qualifications are replaced by that citation, keeping its evidence qualification (verbatim exchange not retained). The repin is row 23 |
| 15 | P1 | accept | M (optional in C) | Record RECOG's new witnesses by exact claim in RF-O09-02 (record-only decoder, record fibers). No event principle, and no removal of R9 or (D5). If that row is touched in C, `RECOG-THM-R9-SHARPENED-ROWS` may be cited beside the unchanged RF-O09-01 table, which I verified still holds at v0.3.26 (L651–652) |
| 16 | P1 | accept | C | IMP-O08-12 gets `DYAD-DEF-PRIMITIVE-MAP` (verified L47–49, L436); the GEN alias is recorded. CUST-O09-01 / REQ-O09-04 closed at §4.2, §6.3 and §12.3. Receipts of DYAD N4 and N6. L1392 Programme navigation made current |
| 17 | P2 | accept (no action) | — | REQ-O09-06 and REQ-O08-01 unchanged |
| 18 | P2 | **accept with change** | M | One-way pointer from Q3b route C-a to RRF-CND-01's Identity/Action row as the representation gate for any declared designation variable. I do **not** assert that the two issues are the same: CND-01 is coincidence-realization admissibility, Q3b is partial-autonomy covariance, and the common root is complete-state covariance (RTG-OFN-DEF-STATE-COMPLETENESS) |
| 19 | P2 | **accept with change** | C | One-line convention note in §5.5.4 (chiral ratio $\rho=S/N$ and normal form $N$ versus dyad $\rho$ and §4 symbols). No renaming. It goes in C only because §5.5.4 is edited there anyway |
| 20 | P1 | accept | C | Repin Triadic to v1.6.1 (RF-O08-02/03/08). Record the OFN half of "Programme/OFN pass two" (§7.4, L864–888): local algebra, former numerical outcomes and physical interpretation kept distinct; no ontology selection. §8 reading unchanged; no Triadic release needed |
| 21 | P1 | accept | M | v1.4 migration: current-only cleanup, tag spellings, single status for `[from: THM + ALG]`, the L674 count ("twenty" becomes "twenty-one"), Appendix A compaction, header. Two stages (layout checked by `tools/check_compaction.py`). Where C touches a site anyway it uses v1.4 spellings |
| 22 | P2 | **accept with change** | M | Register RIDs for the externally citable DEFs named (zero-origin, discrete reduction boundary, continuous representation, finite description, OFN-DIST-ZN, reduction target). The two homeless OPEN blocks get **pointers** to existing §9 records (continuous closure → OPEN-OFN-FRUSTRATION / 3C; null-ledger → OPEN-OFN-IQP), not new OPEN RIDs. `OPEN-C19-L` stays a scope label inside `RTG-OFN-ALG-RAW-STANDARD-C-NOGO` |
| 23 | P1 | accept | C | Add a governing-editions line. Repin where the statement moved (rows 1, 5, 9, 12, 16, 20) and, for RECOG, to the current adopted edition: all eleven cited RECOG RIDs are declared at `recog-v0.3.26` and the statements I spot-checked are unchanged. Pins on unchanged statements keep their v1.4 §1.1 rule-4 label |
| 24 | P1 | **accept with change** | C | Custody table in the DRAFT release record (placed / held / missing). **This session holds the originals listed in §6**, with hashes equal to those OFN prints. I propose placing them unchanged on `upload/ofn-records/`; the branch is the PI's, or mine at his instruction, since Claude sessions push only `claude/*`. BASELINE authority becomes the OFN release record once placed. The 13 Oct narrowing package stays *not integrated* |
| 25 | P1 | **accept with change** | C (custody) | I do **not** hold ER-2B v0.3.1. Until the exact bytes are supplied, RF-O10-03 cites `er2b-v0.3` (`80669c69…a134`) explicitly. Its v0.3.1 hash `711e427a…81b4` stays "reported (FMS v0.6.4)". No stronger ER-2B-dependent use; SESSION and P4 qualifications kept |
| 26 | P2 | accept | M | One sentence in §0.4 naming the appendix map; relettering is stage-2 layout |
| 27 | P1 | accept | after C | Notices to `pipes/FMS/` and `pipes/ER2B/` after the tag, citing the row-1 table; their co-owners edit |
| 28 | P1 | accept | after C | `kind: notice` items after the tag: DYAD (N4, N6, N14 receipts; IMP-O10-06/07 adopted use), GEN (G-20 note received; C2 used), RRF (§6.2a "OFN has not separately adopted" is now stale; OFN adopted the $C^\infty$ reading at row-1 scope) |
| 29 | P1 | accept | C | Inbox states in §7, closed after the tag; `python3 -I tools/pipes_index.py --check` in the PR that changes them |

## 5. Staging preference

**Two editions.**

**v0.10.1 — corrections only, stage 1 only.**
- Methodology v1.3 stays declared; no layout change.
- Rows: 1–14, 16, 19, 20, 23, 24, 25, 29, plus 15 if the build touches RF-O09-02.
- It is assertion-gated (exact-once edits logged with hashes) and carries the negative controls the entry note asks for: a reintroduced "conditional on DYAD OPEN 20" / "existence not asserted" phrase, a reintroduced "freeze candidate" phrase, and a reintroduced "nonempty $F$-invariant" phrase must each be caught.
- Rows 1–3 enter here: row 1 is P0, four consumers (DYAD, GEN, RRF, FMS) carry stale text that waits on it, and rows 2–3 are statement-level (a scope sentence and a `[COR]`), not layout.

**v0.11 — Methodology v1.4 migration, two stages.**
- Stage 1: rows 15 (if not in C), 18, 22, and the content part of 21.
- Stage 2: layout-only compaction of 21 and 26, checked by `tools/check_compaction.py` against the stage-1 hash, with a movement map.

I accept a single two-stage edition instead if the other co-owner prefers it, provided rows 1–3 sit in stage 1 and no claim enters stage 2. The PI decides by need.

## 6. Custody — what this session holds (row 24)

All hashes recomputed in this session (`EV-HASH`). Every one equals the value or prefix OFN v0.10 and its release record print.

| Artifact | SHA-256 | State |
|---|---|---|
| `RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_RELEASE_RECORD.md` (incl. N-O10-1–4) | `10a1ec6b2bcdb7d7198891c6f1c993c3ed9ebc0aad09267fe799f06e37800844` | held |
| `build_ofn_v0_10_draft1.py` | `6a4fe7afc1384ae8763eba5f2bf091db0160d39bb3be5b5f6165873de66258ff` | held |
| `build_ofn_v0_10_draft2.py` | `930b0aefe7b123d36ae6376a7ada05881680f69075a0756652aa69423c665c82` | held |
| `release_ofn_v0_10.py` | `2aca119f95df7b8274f1df40d37fca9495887850c7201e2e870e6fe2e07a4f5f` | held |
| Draft 1 | `d94e1e39f90fd66a485be0e40b614bf36a16a07324aa4e29397ed4be04db8c36` | held |
| Draft 2 (approved object) | `58e2dec54ad600dec189119adc16c8ca89872e74419f78ae317f33558a913610` | held |
| `iso_check.py` | `b92f66597e0c65385876df55e8925ad2133c6d58d87f07c5d753694e12d0d75e` | held |
| `iso_quadratic_nogo.py` | `91fd63f463facd0b3399ed7f1fdde8905b2fe1df9b05c983746b31311d945308` | held |
| `transported_pq.py` | `2dcd43312ab69811a88004017df8f44e3321029af0d20ed87935a308d8b20bf6` | held |
| `transported_sim.py` | `95a86e4576f3dc040128ff943ae0e1f320d97207e2815f2b168e311281e181db` | held |
| `basin_test.py` | `569f14306c80b4b438e39f6b7c7f5167bb9d257f2bc62aee928b0f3b1715e4ff` | held |
| `k3_six_step_factor_check.py` | `7d761090378781c5c74ec64abc1f215cc951cec21f139a231ee1bd8ed18ad4ff` | held |
| `OFN_PSI_KAPPA_EXTENSION_v0_1.py` | `6566009c6ae8a9ca57a8e4a13bf42025cbd98f589f4f908fc477bc3fe1a25f88` | held |
| `OFN_PSI_KAPPA_ALL_MINOR_CHECK_v0_1.py` | `c56a01aca30953ff5f9ca5a1ee19a161f003764431768a31118100efd755a9e3` | held |
| `OFN_PSI_INVARIANT_C_CHECK_v0_1.py` | `18f10aa40cedb9352e405add7353a730565f3f9a1f66a3cad96a69172417b114` | held |
| `OFN_PSI_INVARIANT_C_GAUGE_CHECK_v0_1.py` | `d3e5cedf7c5ae1943298077ba0203ececd863b3e7bca4bd06f166f36f2929781` | held |
| `OFN_PSI_REFLECTION_AUDIT_v0_1.py` | `e6d9b089505b2a16ee24eed98ccdd3478e703ce85ecd26d8c8b4cd6a9376235a` | held |
| `OFN_STAB_F3_CHECK_v0_1.py` | `8b41546115c8cfce77b8eae45f4889db56163dcd70261171665c3b11d3ae5ea9` | held |
| `OFN_SOURCE_REVIEW_ER2B_GEN288_OPEN3_v0_1_1.md` (v0.8 input) | `8d18640f5ab6808440e240d39e80210a021cc95852e79b24c7960b1297780944` | held |
| `OFN_SOURCE_REVIEW_ADDENDUM_FMS062_DYAD6414_RRF083_v0_1.md` (v0.8 input) | `f86cd4837e1756f853715aba69170356ae9bd89fb1d9fe094dc22b89a14ec5b8` | held |
| `transported_chiral_pq.py` (`09129ffc…73ac`) | — | **not held by this session** |
| FMS ψ scripts (`ad44f66a…`, `5af23da9…`); ER-2B v0.3.1 | — | not held by this session (FMS/PI) |
| `REVIEW_FINDINGS.md`, `OFN_TDRG_FINDING_A_HANDOFF.md`, `OFN_v0_9_PROGRAMME_AND_OWNER_SYNC_REQUEST.md`, v0.9 validation files, v0.8/v0.9 release records and ZIPs | — | not held by this session (v0.9 editor / PI) |

Note: the `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md` held here has the same hash as the repository copy (`6e4fc3c3…4b1d`).

## 7. Inbox `pipes/OFN/` — proposed dispositions

States change only in the joint step; closing follows after the tag.

| Item | Proposed disposition |
|---|---|
| `20261026-NUMGEN-v1-21-adopted.md` | `accept` — rows 12, 13; pointer: the OFN release record |
| `20261028-TDRG-v2-12-14-adopted.md` | `accept with change` — rows 7–11. The change: custody stays deferred by TDR-G; the repin is OFN's; the §10 finding goes back to TDR-G (row 11) |
| `20261029-RECOG-v0-3-26-adopted.md` | `accept` — rows 14, 15, 23. The retracted order sentences are not quoted by OFN (checked: neither string occurs in `ofn-v0.10`) |

## 8. Not decided here

- No regrading of any OFN claim.
- Q1–Q6, Standard C (except the row-3 `[COR]`), the raw-carrier no-go and the FMS ranking are unchanged.
- OPEN-OFN-3B stays ACTIVE.
- The universal-κ finite-$a$ statement keeps its FMS P4 qualification.
- No physical carrier, ψ value or chirality is selected.
- No historical SESSION computation is rerun.
- Nothing missing is reconstructed.
