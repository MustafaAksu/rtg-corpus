# RRF S1 — reviewer verdict on PR #400

**Date:** 26 November 2026.
**Status:** [SESSION] / NONCANONICAL. Reviewer lane (Claude, independent reviewer / second co-owner). This is a source/interface verdict only: no scientific grade, adoption, DSN edit, pipe disposition or release. The PI decides.
**Reviewed:** PR #400 `chatgpt/rrf-s1-source-sync-20261126`, exact head `8b5245b1a87ed27e2cc65dc81653cf8052032b00`. Base `main` `024a2d3ef09cd4cefe4eeb9d58f2117b1d44418e` (#394, #397, #396 and #399 merged: `b9e3fbbc`, `d7e401e4`, `f216bcd2`, `024a2d3e`). Object: `records/rrf/RRF_S1_SOURCE_INTERFACE_MATRIX_20261126.md`, 28 rows. Criteria: S1-A1–A4 as stated in that record, §4.
**Method:** native checkout. Each row was compared against the owner DSN at its governing tag, by RID, formula and grade text. The Atlas was not used. No owner certificate was rerun.

## Verdict

**ACCEPT WITH CHANGES.** S1-A1, A3 and A4 are met. S1-A2 is met for 24 of 28 rows. Four rows (D1, O2, O4, T1) need the corrections in §2 before they are carried into S2. They can be applied either by amending #400 or as binding S2 stage-1 entry conditions; the preparer chooses, and the PI's S2 decision records which. No row is rejected. No scientific disagreement with an owner was found.

## 1. Checks performed

| Criterion | Result |
|---|---|
| S1-A1 governing identities | All 12 tags (rrf, methodology, programme, dyad, ofn, recog, gen, triad, numgen, uvm, tdrg, rer) are the newest by version sort. Tag commit equals the matrix value, published-file SHA-256 equals the matrix value, and the `main` file is byte-equal to the tag file. TDRG is `dsn/RTG_DISCRETE_GENESIS_DSN.md`, UVM is `dsn/RTG_OPEN_M_DSN.md`. All cited release records exist. The RER adoption record prints `58feee5f…` (1 hit). |
| S1-A2 row comparison | 24 rows agree with owner text, including RIDs, numerical rows, conditions and stated non-claims. The four exceptions are in §2. Spot results: G1 theorem block gen-v2.8.9 L859–878 is byte-identical to gen-v2.10 L867–886 (`diff` empty); R2/R3 constants (517/163; 259.2/81.49; 221.4/75.69; 3.456e-5, 1.010e-4 outward displays) match RECOG §6.13a; D2 inverse chart R=1/10, `R−M(R)>9/100`, 15/16 and 17/16 bounds, and D7 K₀ rows 1101/1000 and 533/500 match DYAD §6.14; D6 "B-6 ⟺ (B-an and B-3)" is verbatim; N3 counts 0/22, 20/136, 124/136 and the C7C-M4 hold reason match NUMGEN v1.22; E1 has 18 + 2 records with the two ER-2B exclusions; U1 matches UVM OPEN-M-6 and the RRF reference block. |
| S1-A3 queue | 10/10 `pipes/RRF/` items mapped; none closed or state-changed. |
| S1-A4 protected scope | 0 files changed under `upload/ dsn/ noncanonical/ BASELINE.md pipes/ evidence/`; `pipes_index.py --check` reports 197/20. The Claude lane is unchanged (no diff line). |

## 2. Required row corrections

**C1 — D1 (DYAD §1 table L59; §6.17 proof L961).** The wrapped-cylinder fixed points $(\log(1+2\pi k),0)$ and $(\log(1+2\pi k),\pi)$ are stated for **winding $k\ge1$**. At $k=0$ they are the lifted points $(0,0)$ and $(0,\pi)$. Replace "k≥0" with "k≥1".
*Acceptance:* the row reads "winding k≥1" and keeps lift fixed points $(0,m\pi)$ as a separate statement.

**C2 — O2 (OFN v0.13 §5.5.4–5.5.5 L481–499; RRF v0.8.4 §6.2a L433).** The RRF sentence "OFN/Genesis have not separately adopted the resulting class-C family, lock surfaces or physical model realization" is stale for one of its three objects only.
- **Class-C family:** OFN §5.5.5 now registers class C as the "primary realized smooth mathematical candidate family" (realization through IMP-O10-06/07; narrow-Q6 case (ii) covers C2). This part is to be updated.
- **Lock surfaces:** these, together with cycle-defect capacity, the six-step cubic and the causal interface, sit under "Formal properties `[ALG]` [provenance: OFN co-owner SESSION computation, recorded, not registered]". They stay not registered.
- **Physical realization:** not selected; it stays not selected.

*Acceptance:* the S2 wording updates only the family clause, and keeps "lock surfaces not registered" and "physical realization not selected" explicit.

**C3 — O4 (OFN §5.5.4 L487 and §9 L969).**
- The identity $F_e-N(z_e)=-\tfrac{\kappa}{3}(N(z_e)+b_e)$ is inside the same SESSION "recorded, not registered" block.
- The I-comp / I-quiet / I-remove frame is "recorded; none selected".
- For the ψ-modulus (L1334), only the "not conjugate" direction carries over to full transported models ($\kappa\notin\{0,2\}$). The universal finite-$a$ statement rests on FMS P4, which is source-reported and which OFN has not audited.

*Acceptance:* any ADD REF carries these grades and qualifiers verbatim, cites no RID for the identity, and imports nothing as owner-registered.

**C4 — T1 (TRIAD v1.7 §6.18 L774).** The metric-unit identification block is tagged **`[OPEN]`**: the $B_T=2B_G$ family is a typed planar-metric convention, and the birth/mode identification is recorded as unresolved.
*Acceptance:* the row and any S2 ADD REF state the `[OPEN]` grade alongside "convention-only".

## 3. Non-blocking notes

- **N1 — TD1.** The star/token-shift condition is $2c\equiv0\pmod N$ (TDRG L875, imported OFN v0.12 `RTG-OFN-ALG-STAR-TOKEN-SHIFT`, state "statement accepted"), not "2c=0".
- **N2 — P1.** Following the notice (IF29/31/32) is correct. Two more interfaces matter:
  - Programme **IF30** lists RRF's verbatim-import pins (DYAD v6.4.18, RECOG v0.3.21, OFN v0.10, GEN v2.8.9). These become stale on any S2 repin, so the S2 release record should file a PROG notice for IF30.
  - IF33 covers RRF → RER.
- **N3 — R3.** `RECOG-THM-R9-SHARPENED-ROWS-C7` imports `DYAD-THM-NF-REM-C7-SHARP` at v6.4.23. The values at v6.4.24 are identical (checked). S2 cites the DYAD owner at v6.4.24 and records RECOG's own pin as given.
- **N4 — orientation.** The shared ENTRY line still says "BR-Q2 first bounded scientific question after S0", while the S1 record §4 says "next after S1 review". Harmonize them at the next owner edit. This is not a reviewer-lane change.

## 4. Gate state after this verdict

S1 is accepted once C1–C4 are applied or bound as S2 entry conditions and the PI merges. S2 stays HOLD pending a PI decision on S2 workflow. BR-Q2 can be opened as a separate scoped scientific item. This record opens nothing.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## 5. Correction readback — corrected head `2c087763e94ac23768c8b778aecc3bb8a57e508d`

**Verdict: ACCEPT SCOPED.** S1-A1–A4 are met at this head. The preparer applied C1–C4 directly to the matrix. Each corrected row was rechecked against the owner text:

| Item | Readback against owner text |
|---|---|
| C1 D1 | Matches the DYAD §1 fixed-point table L55–59 verbatim in content: lift points $(0,m\pi)$, $m\in\mathbb Z$; zero-winding $P_1=(0,0)$, $P_2=(0,\pi)$; winding $k\ge1$ wrapped points not fixed in the lift. |
| C2 O2 | Only the family clause is updated, quoting OFN §5.5.5 "primary realized smooth mathematical candidate family; analytic exact realization and physical selection open". Lock surfaces and the related properties keep the SESSION "recorded, not registered" provenance. No Genesis adoption of class C is inferred. |
| C3 O4 | The identity carries its SESSION `[ALG]` provenance and no RID. The isolation frame is "recorded; none selected", with I-quiet failing for κ≠0. The ψ-modulus is classified through degree 5 within the reduced-map scope, with only the "not conjugate" direction carried to full models (κ∉{0,2}). FMS P4 is source-reported, unaudited by OFN. The sampled κ∈{1,1/2,3} matches OFN L1334. |
| C4 T1 | The owner `[OPEN]` tag is retained alongside convention-only; birth/mode identification is unresolved. |
| N1 TD1 | `2c≡0 (mod N)`, with `RTG-OFN-ALG-STAR-TOKEN-SHIFT` marked "statement accepted" and custody transfer open. Matches TDRG L875. |
| N2 P1 | IF30 and IF33 are added. Notices are deferred to an authorized successor release; acceptable. |
| N3 R3 | RECOG's v6.4.23 pin is kept; the owner is attributed at v6.4.24. |
| N4 | The orientation ENTRY now places BR-Q2 after S1 acceptance and the PI merge. |
| R4 locator | The §6.13a → §6.13b change is correct: A1a is RECOG §6.13b, L667. No statement change. |

Checks on the corrected head:
- **Scope:** the only changed paths against `main` `024a2d3e` are `README.md` and the two `records/rrf/` files. There are no changes under `dsn/`, `noncanonical/`, `upload/`, `pipes/`, `evidence/` or `BASELINE.md`.
- **Pipes:** `pipes_index.py --check` reports 197 items in 20 inboxes.
- **Claude lane:** unchanged against `main`.
- **Merge order:** `main` + #400 at `2c087763` + #401 merges without conflict. Pipes then still pass, and the Claude lane carries the S1 stamp.

S1 is ACCEPTED SCOPED on the PI's merge of #400 and #401. The scope is source/interface synchronization only. The matrix is a receiving recommendation for S2a, not adopted use.
