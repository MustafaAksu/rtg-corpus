# OFN receiving disposition — Claude co-owner, 24 November 2026

**Status:** [SESSION] / NONCANONICAL / PROPOSAL of the second OFN co-owner. This is an independent readback for joint reconciliation with the ChatGPT co-owner's record (PR #378). It is not an owner decision on its own, not a pipe-state change, not a successor-edition authorization and not an adoption. No DSN, pipe item, BASELINE, tag or upload is changed.
**Prepared by:** Claude, OFN co-owner (session `claude012ZC8x`), on branch `claude/ofn-receiving-disposition-20261124`.
**Independence statement.** This record was written before opening `records/ofn/OFN_RECEIVING_DISPOSITION_CHATGPT_20261124.md`. Before the pass I had seen:
- the PI-relayed chat summary of that record, which named the F3 census identity and the S-P4 headline;
- the merged Atlas advisory `records/ofn/ATLAS_ADVISORY_OFN_SYNC_20261124.md`, which is a reviewed advisory and not an owner disposition.

Every verdict below rests on my own reading of the producer tags and of `ofn-v0.12`.
**Live state (queried 24 Nov 2026, ~18:10 +03:00):**

| Item | State |
|---|---|
| `main` | `9c51ba8` |
| Governing OFN | `ofn-v0.12`. BASELINE row: SHA-256 `55ff8ba8…76aa`; the file at the tag hashes to that value |
| `pipes/OFN/` | 12 items: 9 open, 3 closed |
| Open OFN PRs | #378 (ChatGPT receiving disposition, DRAFT, head `5838fbba`) |
| Governing producer editions (BASELINE) | DYAD v6.4.24, GEN v2.10, TRIAD v1.7, TDRG v2.13, RECOG v0.3.27, Programme v1.4, DZT **v0.19**, AZ **v0.10**; RRF v0.8.4 and NUMGEN v1.21 unchanged since `ofn-v0.12` |

**Evidence:**

| Script | Output |
|---|---|
| `evidence/ofn/scripts/ofn_receiving_source_compare_claude.py` (`4a318f82…15b8`, r2) | `evidence/ofn/receiving_20261124_claude/source_compare_output.txt` (`e107d025…58fa`, r2) |
| `evidence/ofn/scripts/ofn_p4_ideal_check_claude.py` (`83853f00…d074`) | `…/p4_ideal_check_output.txt` (`11592209…86cd`); inputs `…/p4_inputs_sha256.txt` (`f5cb0eb3…63e4`) |

All runs used Python 3.13.18 and SymPy 1.14.0.

## 1. Source comparisons (S1–S6 of the comparison script)

**S1 — owner RID declarations that `ofn-v0.12` cites, from OFN's pin to the governing tag:**

| Producer | Result |
|---|---|
| DYAD, 15 RIDs (v6.4.22 → v6.4.24) | All declaring lines identical, including `DYAD-DEF-PRIMITIVE-MAP`. Its scope tag sits in the custody note, not on the declaring line, so it is checked separately (§2, P06) |
| GEN, 10 RIDs (v2.9 → v2.10) | All identical |
| RECOG, 14 RIDs (v0.3.26 → v0.3.27) | All identical |
| TDRG, 18 RIDs (v2.12.14 → v2.13) | 11 identical; 7 changed, detailed below. The script also lists two prefixes, `TDRG-ALG-LEM` and `TDRG-DEF-CONV`, which are family names and declare nothing |

The seven changed TDRG lines:
- Six lose only Methodology v1.4 edition labels, such as "(v2.12)" or "*(v2.12.14 `[COR]` …)*". `LEM-NOANNIHIL` also repoints its consumer note to OFN v0.12 IMP-O08-06. No statement changes:
  - `TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK`
  - `TDRG-ALG-LEM-NOANNIHIL`
  - `TDRG-ALG-LEM-REACH`
  - `TDRG-ALG-LEM-RETRIG`
  - `TDRG-DEF-CONV-P3CYC`
  - `TDRG-DEF-ORIENT`
- **`TDRG-DEF-STAR`** carries a declared-domain `[COR]` at v2.12.15. The event domain becomes every single-star component with one valid centre (pure $K_{1,m}$, $m\ge3$; trees with longer branches; components containing a cycle). The centre/newborn map is unchanged: $\theta_E=\theta_A+N/2$, $\delta_E=\delta_A$, $\delta_A\mapsto-\delta_A$, read from the CONV-TICK snapshot. TDR-G states that no result changes, because the engines always used this domain.

**S2 — Triadic, triad-v1.6.1 → triad-v1.7.** `[COR r2]` The r1 report said §§6.15–6.18 were byte-identical. That was a false pass: the r1 extractor searched `### 6.15` while the headings read `### §6.15`, so it compared None with None (found in the ChatGPT co-owner readback, R379-2). The r2 extractor stops on a missing, ambiguous or empty span and compares each section to the next heading of the same or higher level, nested subsections included, and the full CN blocks. r2 results:
- §6.16 and SG-18: identical.
- §6.15 (5,459 → 5,445 chars): `[COR v1.6.1 r2 — D3-R1]` → `[COR]` labels and the Genesis source reference (v2.8.7 → v2.9, "re-read at `gen-v2.9`").
- §6.17 (12,121 → 12,205): labels, consumer state moved to §7.4, Genesis source metadata (historical P4 premise versus seed norms re-read at `gen-v2.9`).
- §6.18 (5,485 → 8,679): **substantive scope additions.** These are the type of the Gram relation, its domain $Q_s,Q_c>0$, and coefficient-ODE time in units of one six-step block (not tick time). The off-root extension is not unique, and $f_s,f_c$ depend on it. v1.7 also adds a diagnostic remark $D=\mathcal G/Q_s=Q_c(1-K)$.
- CN-01, CN-03 and CN-04 full blocks: identical once the consumer-state sentence is removed.
- CN-02: v1.7 removes one label and adds a "Requested action" sentence (update sign, extent, symbol and artifact interpretation at each use).
- CN-05 full block (3,364 chars): identical.

The T-6s/t/u statement text is unchanged. §6.18 is not unchanged. A move of RF-O08-02 to `triad-v1.7` must record the §6.18 coefficient-clock and extension boundary, with no stronger stability or physical conclusion.

**S3 — GEN §6.3a–§6.3c** (24,176 characters): identical at gen-v2.9 and gen-v2.10.

**S4 — RECOG §6.6a** (6,151 characters): identical. This covers the IMP-O09-01/02/03 source blocks.

**S5 — Programme OPEN-P0 (`RTG-OPEN-GENERATOR-SELECTION`).** The record differs only in its OFN pointer ("OFN v0.10 §§5, 9" → "OFN v0.12 §§5, 9"). Status, question and definition are unchanged.

**S6 — `ofn-v0.12` sites whose wording no longer matches the governing editions:**

| Wording | Lines in `ofn-v0.12` | Governing source |
|---|---|---|
| XFER-O08-01 "deferred (by TDR-G) to v2.13" / "until TDR-G v2.13 decides" / "defers … to v2.13" | 56, 246, 248, 1018, 1058, 1146, 1378, 1399, 1420 | `tdrg-v2.13` §7: Finding A imported at `ofn-v0.12`; "custody transfer XFER-O08-01 open", a separate decision of both owners (`records/tdrg/TDRG_DECISION_NOTE_XFER_O08_01.md`, SESSION) |
| §10 token-sum row: TDR-G labels "referred back to TDR-G" | 986 | `tdrg-v2.12.15`/`v2.13` SG-3: $P=\sum\delta_i$ changes by $-x$ at a birth with centre token $x$; it is invariant under the declared phase gauge and relabelling, so it is not a gauge quantity; "gauge-like"/"gauge artifact" withdrawn as a wrong reason; $P$ not adopted as an observable |
| IMP-O08-12 "registered provisional" | 1074 | `dyad-v6.4.24` §1 custody note: `[v6.4.11]` `[scope: the Programme's reference map …; the selection of the generator is open (RTG-OPEN-GENERATOR-SELECTION, OPEN-P0)]` |
| RF-O09-02 A1c chain "under (D5)" and "R9 and (D5) are not removed" | 1249 | `recog-v0.3.27`: "(D5) discharged by RECOG-ALG-A1C-JET-REMAINDER-BOUNDS" for the known-$a$ chain and the decoder (ADMISSIBLE-REGION, JOINT-CONTRACTOR: "the former (D5) qualifier is discharged"). R9 is untouched |
| κ table: "γ ≡ κ is the declared parameter convention of Genesis §6.3c and RRF §6.2a" | 478 | GEN §6.3a–c makes no γ≡κ identification. RRF v0.8.4 writes "`γ≡κ` in the OFN class-C parameter convention" |
| §12.3 consumer row "Triadic v1.6.1 \| OFN v0.9 (pinned by Triadic)" | 1402 | `triad-v1.7` companion line and T-6r C1 cite `ofn-v0.12` |
| IMP-O10-05 "not re-verified line by line for this draft" | 1294 | The draft-tense residue survived adoption (Atlas OFN.O9) |
| RF-O08-13 "DZT v0.8 charter/§7; AZ v0.6 §0.1 and Thread C" | 1217 | BASELINE: DZT v0.19, AZ v0.10. DZT §§1, 7 and AZ §0.1 and Thread C still exist under those numbers |

## 2. Dispositions of the nine open notices (keys as in the Atlas matrix)

| Key | Item | Proposed verdict | OFN consequence at the next edition |
|---|---|---|---|
| P01 | DYAD v6.4.23 | **accept** (receipt; no action needed beyond pins) | Record the receipt in the §12.3 consumer register: DYAD names OFN v0.12 with IMP-O08-12/20 and IMP-O10-03…07. Its statement that the raw-map identity follows from `DYAD-DEF-PRIMITIVE-MAP` is consistent with OFN §9 (3B frame). Pins: see P06 |
| P02 | GEN v2.10 | **accept** | Repin the Genesis imports (IMP-O08-01/10/11/13, IMP-O10-01/02, narrow-Q6 dependency) to `gen-v2.10`; their statements are unchanged (S1, S3). Record that Genesis uses neither OFN11-C01 nor OFN11-C02 and prints no edges-minus-closure count. The old Genesis v2.8.5 claim-level pins in RF-O08-02/03/08 stay labelled as not re-read (see §4) |
| P03 | TRIAD v1.7 | **accept** | Repin the Triadic components of RF-O08-02/03/08 to `triad-v1.7`, scoped: record the §6.18 coefficient-clock/extension boundary (S2 r2); Genesis v2.8.5 components keep their claim pins. Correct the §12.3 row: Triadic now pins `ofn-v0.12` and its T-6r C1 cites `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` as an interface constraint, not an import. The current Triadic planar carrier is real. No carrier is selected by OFN |
| P04 | Programme v1.4 | **accept** | Move the companion pin to `programme-v1.4`; OPEN-P0 changes only its OFN pointer (S5). Programme IF03 still names OFN v0.10 for Finding A while TDR-G imports it at v0.12. That is a Programme-side current-use item and is not OFN's to edit (agrees with the Atlas F7 note) |
| P05 | RECOG v0.3.27 | **accept with change** | Repin RECOG imports to `recog-v0.3.27` (S1, S4). In RF-O09-02, replace "under (D5)" for the decoder chain with the v0.3.27 reading: the (D5) qualifier is discharged by RECOG-ALG-A1C-JET-REMAINDER-BOUNDS with DYAD-THM-LPHASE-ROWA-BRIDGE and DYAD-THM-OPEN3-SPIRAL-REM imported. Keep the chart/domain and at-least-two-usable-slip conditions. Keep R9 wherever a claim depends on it — the Dyadic T1/T2 and OPEN 21 transfer statements and RECOG-THM-A1A-CD-IDENTIFICATION. The discharge concerns (D5) only, not R9. No event principle, injectivity, write-through or OPA verdict follows |
| P06 | DYAD v6.4.24 | **accept** | Repin DYAD imports to `dyad-v6.4.24` (15 declaring lines identical, S1). In IMP-O08-12, replace "registered provisional" with the owner's scope marker: the Programme's reference map, generator selection open under RTG-OPEN-GENERATOR-SELECTION / OPEN-P0. This does not select the generator |
| P07 | TDRG v2.12.15 | **accept with change** | §10 token-sum row: the referral is answered (S6), and the OFN decision boundary stays as it is — nonconservation at births; no physical momentum; common token shift not a gauge of the full model. Record that TDR-G imports Finding A at `ofn-v0.12` and cites it in `TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED`. That result is a candidate reference-only illustration for §4.1 (SG-OFN-STATE: a shift-invariant reduced quantity need not carry closed dynamics). It is not an import of a physical principle. STAR domain: see P08 |
| P08 | TDRG v2.13 | **accept with change** | (i) XFER-O08-01: at all nine sites (S6), "deferred to TDR-G v2.13" becomes "custody open; a transfer is a separate decision of both owners; the RID remains OFN's". No transfer and no choice among the options of the TDR-G decision note. REQ-O09-05's endpoint component stays fulfilled.<br>(ii) Repin the TDR-G imports to `tdrg-v2.13`. Six of the seven changed declarations are label-only (S1).<br>(iii) `TDRG-DEF-STAR` (IMP-O08-09, §3.4): OFN's import text ("the star rule creates a node at the centre's antipodal shadow … and inverts the centre token"; "depends on the selected star component") is domain-neutral and stays true on the corrected domain. Finding A depends only on the centre/newborn map, which is unchanged: $(\delta_A',\delta_E')=(-\delta_A,\delta_A)$, so $d'_{AE}(B_cX)-d'_{AE}(X)=-2c$ on every single-star component. The proposed edit adds the declared-domain pointer ("single-star components with one valid centre, `tdrg-v2.13` §6.3") to IMP-O08-09 and keeps Finding A's fixed-component hypothesis.<br>(iv) The OPEN-OFN-2 and IMP-O08-06/14 consumer pins at TDR-G are receipts only |
| P09 | DZT v0.18 | **accept with change** | RF-O08-13 is a reference-only pointer. Repin it to the governing `dzt-v0.19` (not only v0.18: v0.19 was adopted on 20 Nov and filed no OFN notice) and to `az-v0.10` (no AZ notice). Both keep the cited sections. DZT v0.19's new conditional DZT-THM-CASCADE-NORM-LAW is not used by OFN. The no-ontology/no-bridge sentence stays. "DZT v0.17 … not supplied" becomes "received history, not adopted (DZT v0.18 record §7)" |

After the edition is tagged and the corresponding OFN text is published, all nine items would close with these verdicts. Until then they stay open; a disposition entry is the receiver's act, made at reconciliation.

## 3. Atlas keys and further corrections

**O14 (γ/κ attribution) — agree, wording correction.** κ table (line 478): "γ ≡ κ is OFN's class-C parameter convention (also recorded by RRF §6.2a); Genesis §6.3c names its family parameter γ". It is not a model identity, and not $\kappa_f$.

**O9 (IMP-O10-05 "for this draft") — agree.** Replace with a dated, accurate limitation: "section anchors as located in the owner OPEN 3 record; statements read at `dyad-v6.4.24` (S1); not re-verified line by line". The identical declaring lines in S1 support exactly that, and nothing more.

**O6, O10, O11 — agree with the Atlas treatment as stated:**
- no new RID for orientation vocabulary or §7.3 without a separate decision;
- the RF-O10-02 universal-κ statement stays source-reported (see §5 for what this pass adds);
- the R9-free RECOG phase-existence route is not a discharge of R9 in the Dyadic theorems.

**F9 evidence custody.** The Genesis v2.8.5 original is now in `upload/corpus-originals-20261123/`. A claim-by-claim comparison of OFN's RF-O08-02/03/08 v2.8.5 pins can now be done from those bytes. I have not done it in this pass, so the "not re-read" labels stay.

## 4. Proposed scope of the next edition (v0.13), for reconciliation

One content stage, built by an assertion-gated builder as in v0.11/v0.12. **No scientific claim, grade, RID, definition or OPEN status changes.** Content:
1. **Custody wording** (P08 i): nine sites.
2. **Answered referrals and receipts:** P07 (§10 row; Finding A at `ofn-v0.12` in TDR-G); P01, P02, P03 and P05 receipts in §12.3; the Triadic consumer row.
3. **Premise and scope updates:**
   - P05 (D5) wording in RF-O09-02, with R9 kept;
   - P06 IMP-O08-12 label;
   - P08 iii STAR domain pointer;
   - O14 γ attribution;
   - O9 dated limitation.
4. **Repins**, each only where the statements were matched (S1–S5):
   - DYAD v6.4.24, GEN v2.10, TRIAD v1.7, TDRG v2.13, RECOG v0.3.27, Programme v1.4;
   - RF-O08-13 to DZT v0.19 and AZ v0.10.

   The governing-editions line is updated to match.
5. **Not in scope:**
   - any custody transfer;
   - any physical selection or 3B/isolation standard;
   - promotion of the TDR-G spectrum results to ontology;
   - a v2.8.5 comparison, unless done first;
   - an FMS P4 regrade (see §5);
   - edits to other streams' files.

Checker gates on the pattern of v0.12: base identity; rebuild; RIDs, anchors and 21 OPEN statuses kept; no new RID; stale-phrase census (S6) absent; protected `[DEF]`/Q1–Q6/Standard C lines unchanged; Appendix A/B unchanged; negative controls. After adoption, notices go to TDRG (custody wording, STAR receipt), RECOG ((D5) reading), DYAD (label), TRIAD/GEN/PROG/DZT/AZ (receipts or pins).

## 5. S-P4 — FMS P4 success predicate (independent check)

**Source.** The unchanged `FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1.py` (`5af23da9…f409`) with its two dependencies (`550adcb8…`, `2849e32f…`), copied from `upload/corpus-originals-20261123/`; hashes in `p4_inputs_sha256.txt` agree with the intake manifest. The OFN v0.12 §12.1 short digest for the reflection test agrees.

**Finding (agrees with the headline relayed by the PI).** At line 349 the P4 gate accepts when every generator $g$ of the elimination ideal $I_{\rm el}=I\cap\mathbb Q(\sqrt3,i)[r,t]$ is a multiple of $L=1026r-17\sqrt3-72\sqrt3\,t$. That tests $I_{\rm el}\subseteq\langle L\rangle$. The "only if" direction of the SESSION theorem needs $L\in I_{\rm el}$, the opposite containment: only then does every solution lie on $L=0$. The control $g=L(r-1)$ passes the gate's form of the test and fails the needed one (C3). The gate is therefore inadequate as written.

**What the rerun shows.** I ran the unchanged script (exit 0, ALL PASS, about 17 s) inside a wrapper that records its two P4 Gröbner bases. In both swap branches the elimination basis is the single generator
$$r-\tfrac{4\sqrt3}{57}t-\tfrac{17\sqrt3}{1026}=L/1026.$$
So $I_{\rm el}=\langle L\rangle$, and both containments hold (C1, C2). For this run the P4 conclusion — the elimination ideal is exactly the fixed-point line — is supported by the actual ideal, not merely by the gate.

Evidence state: EV-RUN with the same CAS (SymPy 1.14.0); not an independent engine.

**Limits:**
- The "f5 bilinear in (r,t)" premise is interpolated from four points and checked at one further point. The note argues it from exact degree-5 linearity; the script's check is a single-point consistency test, not a proof.
- The universal-κ claim rests on the other FMS scripts, which this pass did not review. OFN's own reflection checks remain sampled at κ ∈ {1, 1/2, 3}.
- **Grade.** RF-O10-02 stays SESSION, reference-only.

**Recommendation.** File the gate finding to FMS as a `finding` item after reconciliation: replace the line-349 predicate with a two-sided test, i.e. reduced elimination basis equals $\{L\}$ up to a unit, or $L$ reduces to 0 modulo the elimination basis together with every generator a multiple of $L$. OFN changes no wording for S-P4 in v0.13. If the co-owners prefer, RF-O10-02's evidence sentence may add "elimination ideal checked two-sided in an OFN rerun (SESSION)".

## 6. Claude co-owner lane — proposed entry-note text

*To add to `records/ofn/OFN_COOWNER_ENTRY_NOTE.md` under "Claude co-owner lane" once PR #378's structure is agreed. It is kept here so that two PRs do not edit the same file.*

> **24 November 2026 checkpoint.** Independent readback of the nine open notices: `records/ofn/OFN_RECEIVING_DISPOSITION_CLAUDE_20261124.md` (branch `claude/ofn-receiving-disposition-20261124`). Source comparisons S1–S6 and the S-P4 two-sided ideal check are in `evidence/ofn/receiving_20261124_claude/`. Held: v0.13 scope as in that record §4 (maintenance only; no RID or status change); S-P4 = gate defect confirmed, actual ideal $=\langle L\rangle$ in both branches (EV-RUN, same CAS), no regrade. Next: (1) read the ChatGPT record and reconcile row by row; (2) on agreement, build the v0.13 stage-1 candidate with gates as in v0.12; (3) file the S-P4 gate finding to `pipes/FMS/` after reconciliation. PI_PENDING: none yet (start of the v0.13 build needs PI authorization after reconciliation).

## 7. What this record does not do

- It does not change any pipe state.
- It does not decide or propose a custody transfer.
- It does not choose among X1/X2/X3 (TDR-G decision note).
- It does not select a generator, carrier, isolation contract or independence standard.
- It does not promote TDR-G spectrum results or DZT/AZ diagnostics to OFN principles.
- It does not regrade the FMS P4 theorem.
- It reads no historical approval contents.
- It does not edit `records/ofn/OFN_COOWNER_ENTRY_NOTE.md`.
