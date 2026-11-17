# DZT — Reactivation triage

**[SESSION] Working record of the DZT stream (Dyadic Arithmetic-Resonance Transform). It has no scientific or release authority, and nothing in it is adopted.** It classifies every drift row, inbox item and Atlas finding on DZT, and proposes dispositions within the scope the PI has already set (§7). The DZT DSN is not edited by this record. No pipe state is changed and no tag is created.
**Date:** 18 November 2026. **By:** Claude, DZT co-owner session (BOOTSTRAP message 2 of `records/dzt/DZT_COOWNER_SESSION_ORIENTATION.md`).
**Subject edition:** `dzt-v0.8` — `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`, SHA-256 `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2` (equal on `main` `6c5a74a`). Line numbers marked "v0.8" are lines of that file.
**Evidence base:** `records/dzt/DZT_RECOVERY_READING_RECORD.md` (merged in PR #309, `b4ebe61`; cited below as **RR**) and its companion `records/dzt/DZT_RECOVERY_VARIANT_DIFFS.md`. Recovered files are under `upload/dzt-recovery-20261116/received/originals/downloads/` (PR #308, `5fa09bd`). Line numbers marked "v0.17" are lines of `…_v0_17 (1).md`.

## 1. Basis

- **Governing edition:** `dzt-v0.8`. It has no release record (tagged at the 22 Oct 2026 baseline, verified by BASELINE as "PI").
- **Answer to the note's FIRST QUESTION:** DZT v0.1–v0.17 exist and were received unchanged (PR #289), with v0.6 missing. Several editions have more than one variant (RR §2, §4). Every edition from v0.9 on is built on the tagged v0.8 text (RR O-3.2). None of them was ever adopted (RR O-3.5).
- **How they enter (PI decision D1, §7):** the triage runs against `dzt-v0.8` as the edition basis. v0.9–v0.17 are sources to be verified, not a basis. A row below that concerns only recovered content is marked "recovered".
- **Read for this record:** RR in full; `dzt-v0.8` in full; the reading list of the orientation note at the tags RR names (`methodology-v1.4`, `programme-v1.4`, `dyad-v6.4.24`, `az-v0.10`, `ofn-v0.12`, `numgen-v1.21`, `atlas-v0.14`); `pipes/DZT/` (four open items). What could not be verified is listed in RR §10. That list is unchanged.

## 2. Classification

**Class** (the frame the PI accepted, §7):

- **C1 claim/scope:** the row changes what DZT asserts — a statement, a definition, a scope or a status — or concerns a proof.
- **C2 identifier/pin:** an identifier, a version pin, a grade token or a section pointer only.
- **C3 evidence/provenance:** availability, identity or history of files, and evidence states.
- **C4 no scientific change:** DZT's text already agrees with the current owner text.

**List:**

- **(i)** next edition, no new science, no grade raised. **S1** is Stage 1 (claim, scope and import corrections). **S2** is Stage 2 (Methodology v1.4 structure only).
- **(ii)** new work this cycle. Its outcome enters an edition only by a separate PI decision.
- **—** no action.

Every row gives an acceptance criterion: what must be true before the row is done.

## 3. Rows

### 3.1 C1 — claim and scope

| # | Item | Finding (source) | Proposed action | Acceptance criterion | List |
|---|---|---|---|---|---|
| 1 | Norm object. v0.8 line 212: "$M_p=\lvert Q_p\rvert\in\mathbb Q(\zeta_p)^+$". Tables headed $N_+(M_p)$: v0.8 §1 (lines 53–57) and §6.3 (lines 212–232) | $M_p$ is defined as $Q_p/(i\zeta_p^3)$ (v0.8 line 53), a real algebraic number whose Galois conjugates take both signs. The canonical audit script computes `sqrt(abs(N_full))` (RR §9.2). Three independent session checks give signed values, for example $-1/8$ at $p=16$ (RR §9.3). The tables therefore hold $\lvert N_+(M_p)\rvert$. | Keep $M_p:=Q_p/(i\zeta_p^3)$ and the signed $N_+(M_p)$ as the defined object; remove "$M_p=\lvert Q_p\rvert$". Label every tabulated value and every finite-horizon statement as $\lvert N_+(M_p)\rvert$. **Open no sign OPEN now** (D3). | No DZT text identifies $M_p$ with $\lvert Q_p\rvert$. Each table and each norm statement says either $\lvert N_+\rvert$ or signed. Values unchanged. | (i) S1 |
| 2 | `DZT-OPEN-NORM-LAW` ("DZT-OPEN-0B-R", v0.8 lines 95–100): ACTIVE; all-$p$ proof open | *Recovered:* v0.9 and v0.16 state `DZT-THM-CASCADE-ODD-SUPPORT` and `DZT-THM-CASCADE-DENOMINATOR`. The LIT offer states the same law (RR §9.1; the denominator exponent agrees in one line). Proof texts: two recovered notes and the LIT note (rtg-lit `8e2fb5cb`). | **Owner proof review this cycle (D3)**, using the recovered notes and the LIT derivation together with rows 4 and 5. The grade and the closure of the OPEN are a later PI decision. | (a) Each proof step checked, including $p=2^k$, $p=3\cdot2^k$, the range $p\ge12$ (with $p=8$ the zero degeneracy), rationality and the $\lvert N_+\rvert$ scope. (b) Definition as in row 1. (c) Evidence stated as in row 16: which script variant, what is `EV-BYTES` and what is not rerun. A missing artifact is not a refutation. (d) Independent review by the second co-owner. (e) PI grade decision. | (ii) |
| 3 | `[HYP]` mechanism, v0.8 lines 67, 100, 230: "the ≡1 (mod 4) gate is the reality of $\mathbb Q(\sqrt q)\subset\mathbb Q(\zeta_q)^+$" | *Recovered* v0.9: "subsumed" by the order condition. LIT: not needed, and it cannot be the reason at $q=9$ ($\mathbb Q(\zeta_9)^+$ is cubic) (RR §9.1). | Decided with row 2's verdict: retire the hypothesis with its reason (owner decision, recorded in Appendix B). | The verdict names the reason (the order condition, and the $q=9$ case). | (ii), with row 2 |
| 4 | Odd-support proof note, line 173: "$N(L+1)=\lvert\Phi_p(-1)\rvert=1$ for $4\mid p$" (recovered) | For $p=2^k$ the value is 2. The odd part is unaffected, but the note contradicts the denominator proof (RR O-8.3). | Correct within row 2's review. | The corrected statement agrees with the denominator proof. | (ii), with row 2 |
| 5 | v0.17 line 250: "$I-1$ … unit factor" (recovered) | $N(I-1)=2^{\varphi(p)/2}$; it is not a unit (RR O-8.4). | Correct within row 2's review. | The wording names $I-1$ as a 2-power-norm factor. | (ii), with row 2 |
| 6 | Track B1. v0.8: `DZT-OPEN-LOCAL-FORMAL-ZETA` (lines 105–111). *Recovered* v0.10–v0.17: DZT-B1-0, DZT-B1-1, $W^{(A)}$, $W^{(B)}$, $W^{(C)}$ | The B1 results rest on the pointwise recurrence $Q_{m+1}=Q_m-Q_m^2+\tfrac{47}{54}Q_m^3$ (v0.17 lines 127, 287; REQ-004 response lines 26–27). At `dyad-v6.4.24`, $47/54$ belongs to the fixed-radius angular mean `DYAD-ALG-RAW-ANGULAR-MEAN` (lines 523–527). `[COR] [v6.4.10]` (line 529) supersedes the unqualified recurrence. On the positive ray the difference is $-\tfrac5{24}Q^{5/2}$ (RR O-8.1). | **Re-examination required (D4).** First fix the dynamical object: $\mathcal A_{\rm raw}$ or $Q(T^{6m}x)$, with its scope pinned at the Dyadic tag. Then re-examine B1-0, B1-1 and $W^{(A,B,C)}$ against it. | No B1 result enters until (a) the object and its scope are stated with Dyadic RIDs at the pinned tag, and (b) either the result is proved for that object, or a proved link between the averaged and the pointwise laws is cited. Independent review. | (ii); v0.8's `DZT-OPEN-LOCAL-FORMAL-ZETA` stays as stated |
| 7 | Channel universality (recovered v0.9 (2)–v0.10): `DZT-OPEN-CHANNEL-UNIV`, `DZT-ALG-ADMISSIBILITY` (v0.17 line 116), `DZT-RESULT-CHANNEL-NONUNIV` | The gate is stated as "iff $q\mid(b+1)$". Dyadic Appendix D (line 1444) has $q\mid(b+1)$ and $p\nmid(b+1)$, with the first form valid for $b+1<p$ (RR O-8.2). | Only if the PI brings it forward: restate the gate with the Dyadic condition, check NONUNIV against it, and cite the REQ-002 response by path and hash (its hash equals Dyadic Appendix D line 1426, RR §6). | Gate as Dyadic states it; NONUNIV re-derived under it. | (ii) |
| 8 | Atlas DZT.Q5. v0.8 line 13: "$p=40$ stands as the **sole** anomaly across 14 points"; line 55: "Pure 2-powers at all points **except $p=40$**". §1 validation table (p=12–52, lines 53–55) against §6.3 table (p=12–64) | Both tables hold values already present in v0.8. The p ≤ 1000 audit (line 53, `DZT-ALG-CASCADE-ANOMALY-SET`) finds 20 anomaly points $p=8\ell^a$. | State each finite table with its range, and give the anomaly set by pointer in the same paragraph. Make the §1 validation table the same 14 values as §6.3 (no new values). If S2 moves line 13 into history, the scope moves with it. | No sentence calls $p=40$ the sole anomaly without its finite-table range. The two tables agree. | (i) S1 |

### 3.2 C2 — identifiers and pins

| # | Item | Finding (source) | Proposed action | Acceptance criterion | List |
|---|---|---|---|---|---|
| 9 | Header pins, v0.8 lines 6, 7, 10: Programme v1.1, Dyadic v6.4.8.1, AZ v0.6, OFN v0.7, Methodology v1.2 | Current: `programme-v1.4`, `dyad-v6.4.24` (or the governing Dyadic tag when the edition is built), `az-v0.10`, `ofn-v0.12`, `methodology-v1.4` (RR §7.1) | S1: repin Programme, Dyadic, AZ and OFN to the governing tags at build time. S2: the Methodology pin with the v1.4 migration (D5). | Every pin names an adopted tag and is checked against BASELINE at build time. | (i) S1 / S2 |
| 10 | §7 Dyadic import rows, v0.8 lines 236–247, and their uses in live sections (lines 13, 53, 82, 178, 193, 208, 212) | Dyadic Appendix F classifies each string and creates no alias (RR §7.2). `DYAD-OPEN-B5-ALLP` is a closed OPEN, result `DYAD-ALG-B5-ALLP-NONVANISHING`. VANISH-B2/B3/B4 are three RIDs. `DYAD-ALG-CASCADE-P12` is unmatched (value in §6.11). `DYAD-ART-CASCADE-Q4-03` matches `DYAD-ART-Q403-EXTRACT` by content only. P1, REALITY, LEAD, R and CF-Q403 are components of `DYAD-THM-Q403-PHASELAW`. `DYAD-THM-Q403-PHASE-ALLP` maps to `DYAD-THM-Q403-PHASELAW` `[THM]`. `DYAD-ALG-PHASELAW` is historical. | Repin each row to the Appendix F target. Cite the p=12 value as §6.11 text, without a RID. Cite the cascade artifact as `DYAD-ART-Q403-EXTRACT` "by content; no byte identity; files not in the repository". Cite the components as parts of PHASELAW, not as rows of their own. Import grades as the owner states them (`[THM]`, not `[THM/ALG]`). | Every Dyadic-pattern string in the live sections resolves to a `dyad-v*` RID at the pinned tag, or is marked as non-RID text. No alias is created. | (i) S1 |
| 11 | Certificate `q4_03_R_identity_certificate.py` (v0.8 lines 244, 301) | It is `DYAD-ART-Q403-CERT` and is not in the repository (RR §7.2) | Cite as `DYAD-ART-Q403-CERT`, with "not in the repository". | Citation by Dyadic RID; availability stated. | (i) S1 |
| 12 | `DYAD-RESP-DZT-002/003/004` registered as RIDs in DZT §8 (recovered v0.17 lines 285–288) | No such Dyadic RIDs; DYAD namespace (RR §7.2) | Only if rows 6 or 7 come forward: cite the response files by path and hash, not as RIDs. | No DYAD-pattern string registered by DZT. | (ii) |
| 13 | Atlas DZT.Q4. Compound grade tokens in v0.8: `[THM/ALG]`, `[ALG finite horizon]/[HEUR]`, `[HEUR/ALG finite horizon]`, `[ALG fin-hor]`; undeclared alias `[HEUR diagnostic]`. `DZT-ALG-CASCADE-ANOMALY-SET` carries ALG and HEUR in different sections. | Methodology v1.4 §8.4: compound grades are unpacked (RR §7.1) | Unpack each compound into separately graded statements. Each component keeps the grade it already has: the finite-horizon set is `[ALG]` with scope p ≤ 1000, and the mechanism stays `[HYP]` (row 3). | No compound token is left. No component is raised. A grep finds no `/`-joined grades. | (i) S1 (touches claim lines; S2 only moves) |
| 14 | Programme IF18 (pin v6.4.8.1) and IF19 (open) | Programme-owned (RR §7.1) | With the edition, file a notice to `pipes/PROG/`: the Dyadic tag DZT now pins; IF19 unchanged. | Notice filed; the receiver decides. | (i), with the release |

### 3.3 C3 — evidence and provenance

| # | Item | Finding (source) | Proposed action | Acceptance criterion | List |
|---|---|---|---|---|---|
| 15 | Recovered editions v0.1–v0.17: 25 files, with variants of v0.4, v0.8, v0.9, v0.10, v0.11, v0.16 and v0.17; v0.6 absent (RR §2, §4) | No adoption record for any of them (RR O-3.5) | **No retrospective tags (D2).** The next edition's release record lists every received file with path and full SHA-256 as "received, not adopted". v0.6 is listed as `NOT RECEIVED`. | The list equals RR §2 (25 files plus the legacy duplicate of v0.8) and names v0.6. | (i), in the release record |
| 16 | v0.8 §8 artifacts (lines 255–261): seven scripts and one CSV. v0.8 says nothing of their availability. | Recovered copies are now in the repository. Three scripts have two contents. DZT cites no hashes. No historical run output exists (RR §5.2, O-5.2). | Cite each script by the recovered path and SHA-256 as `EV-BYTES`, with "historical execution evidence not available; `EV-NOT-RERUN`". Where two contents exist, cite both and say which text matches the DSN's description, without asserting identity. Copy a script to `evidence/dzt/` only when it is rerun for a grade (row 2). | Every §8 row has path, hash and evidence state. No script is described as recreated. | (i) S1 |
| 17 | Missing material: v0.6; the "v0.17 session record"; DZT-REQ-001; DZT-REQ-005; `qb_extract.py`; Dyadic `q4_03_cascade_extract.py`, `q4_03_cascade_coeffs_p8_200.csv`, `q4_03_R_identity_certificate.py` | Not in the recovery or the repository (RR §5, §10) | **Targeted search (D7), in priority order:** P1 — the Dyadic `q4_03` certificate, extractor and data; P2 — `qb_extract.py` and DZT-REQ-001, only if a claim or a check depends on them; P3 — v0.6 and the v0.17 session record (history; not blocking); P4 — DZT-REQ-005, first whether it was ever sent (v0.17 records it as not sent). | Each item ends as received (with a hash) or `UNVERIFIED / NOT RECEIVED`. Nothing is regenerated and presented as recovered. The triage and the edition do not wait. | (ii) |
| 18 | "Closure freeze v0.17" (recovered `…_v0_17 (1).md` lines 59–61 only) | No record says it was a PI decision (RR O-4.3) | **An unverified historical status record (D4)**, listed under row 15. It is not carried into any edition and is not cited as a decision. | No DZT text treats the freeze as a decision. | (i), in the release record |
| 19 | LIT record header at `8e2fb5cb` says "not reviewed / not offered" (RR O-8.6) | Review `5888136234` exists and the offer was filed | Mention it in DZT's reply to the LIT item (row 2). DZT does not edit `rtg-lit`. | The reply names the discrepancy. | (ii), with row 2 |
| 20 | NUMGEN provenance (DSN line 2742) and OFN RF-O08-13 cite DZT v0.8 and the "v0.17" report | Owner-held text | With the edition, file notices to `pipes/NUMGEN/` and `pipes/OFN/`: the new DZT edition, and that v0.9–v0.17 are received history and not adopted. | Notices filed; the receivers decide. | (i), with the release |

### 3.4 C4 — no scientific change

| # | Item | Finding | Proposed action | List |
|---|---|---|---|---|
| 21 | AZ separation: SG-DZT-1 (v0.8 line 122), Atlas AZ.A5, AZ SG-AZ-7, Programme §6.7 | Unchanged at `az-v0.10` and `programme-v1.4`. AZ v0.9 and v0.10 sent DZT no item. | No change beyond the AZ pin (row 9). | — |
| 22 | p=12 value | DZT writes $-13+\tfrac{15\sqrt3}{2}$, the sign Dyadic restored | No change (citation per row 10) | — |
| 23 | `DYAD-THM-RAW-CUBIC` caveat | DZT does not cite it | No change | — |
| 24 | VANISH-B2 holds for all $p\ge4$ | v0.8 line 81 (`DZT-ALG-B234-STRUCTURAL`) states $p\ge b+2$, which is $p\ge4$ for $b=2$ | No change (repin per row 10) | — |

## 4. Inbox items (`pipes/DZT/`)

The items are not changed by this record. Each disposition below is entered when the edition is adopted, or when row 2 is decided.

| Item | Rows | Proposed disposition |
|---|---|---|
| `20261103-DYAD-notices-n16-n21.md` | 10, 11, 22, 23, 24 | `accept` · pointer: the next edition's release record. Adopted use is then DZT §7 at the pinned Dyadic tag. |
| `20261111-AZ-v0-7-adopted.md` | 9, 21 | `no action` · superseded by the AZ v0.8 item. |
| `20261112-AZ-v0-8-adopted.md` | 9, 21 | `accept` · AZ companion pin moves to the governing AZ tag; SG-DZT-1 unchanged. |
| `20261113-LIT-norm-law-proof-candidate.md` | 2, 3, 4, 5, 19 | Verdict after row 2's review, as a reply item to LIT. Not part of list (i). |

## 5. Atlas findings (`atlas-v0.14`; noncanonical)

| Key | Finding | Rows |
|---|---|---|
| DZT.Q1 (D-RID; advisory row 2 of 10 Nov) | §7 strings that are not owner RIDs | 10, 11 |
| DZT.Q4 (D-GRADE) | compound grades; ANOMALY-SET ALG/HEUR split | 13 |
| DZT.Q5 (D-SCOPE) | §1 versus §6.3 table range; "sole anomaly" wording | 8 |
| AZ.A5 | no DZT–AZ link | 21 |

## 6. The split

**(i) Next DZT edition — no new science, no grade raised (D1, D5).** Its number is decided by the PI when the edition is started (§8).

- **Stage 1** (claim, scope and import corrections; built by an assertion-gated script; the intermediate hash is recorded):
  - row 1 (norm object and $\lvert N_+\rvert$ labels);
  - row 8 (table scope);
  - row 9 (pins except Methodology);
  - row 10 (Appendix F repins);
  - row 11 (certificate citation);
  - row 13 (compound grades);
  - row 16 (§8 evidence states).
- **Stage 2** (Methodology v1.4 structure only; movement map, `tools/check_compaction.py` against the Stage 1 hash, negative controls). Scope:
  - the Methodology pin;
  - the live-file rule (history out of §1 and the version log);
  - RID grammar and the local alias table.

  No new claim and no grade change.
- **Release record:** row 15 (received-history list), row 18 (freeze as unverified history), and the inbox dispositions of §4. Notices with the release: rows 14 and 20.
- **Review:** Claude prepares, ChatGPT is the independent receiving reviewer, and the PI decides adoption and publication (D6).

**(ii) New work this cycle (D3, D4, D7):**

- Rows 2–5 and 19: the norm-law proof review and the verdict on the LIT offer.
- Row 6: B1, starting with the dynamical object.
- Rows 7 and 12: channel universality, only if brought forward.
- Row 17: the targeted search.

None of it blocks list (i). A result of (ii) enters an edition only by a separate PI decision after its review.

## 7. PI decisions

**Decided by the PI, 18 November 2026, 00:00 +03:00 (project conversation), verbatim:** "aşağıdaki tüm önerileri PI olarak kabul ediyorum" ("as PI, I accept all of the proposals below"). The proposals are the second DZT co-owner's (ChatGPT) "DZT — BOOTSTRAP 2 için karar önerilerim", relayed to this session by the PI. That text is not in the repository; its content is recorded here.

| # | Question | Decision |
|---|---|---|
| D1 | Basis of the next edition | Mixed. The adopted `dzt-v0.8` is the edition basis. v0.17 is a source to be verified. Track A comes first; B1 gets a separate scientific review. |
| D2 | Intermediate editions and v0.6 | No retrospective tags. v0.9–v0.17 are recorded as history with full hashes and locations. v0.6 is kept as `NOT RECEIVED`. |
| D3 | LIT offer and norm sign | Review the LIT offer in this cycle. Keep the signed definition of the norm. Label the existing tables explicitly as $\lvert N_+\rvert$. Open no sign OPEN for now. |
| D4 | B1 and the closure freeze | Scientific re-examination of B1 is mandatory. The freeze is an unverified historical status record, not a PI decision. |
| D5 | Methodology v1.4 | Same release cycle, separate stage: scientific corrections, then a fixed intermediate hash, then structure/compaction only. Stage 2 carries no new claim or grade change. If the scientific review runs long, the PI may limit the scope to synchronization; this is not chosen now. |
| D6 | Co-owners | Claude and ChatGPT. Claude prepares; ChatGPT is the independent receiving reviewer; the PI decides scientific adoption and publication. |
| D7 | Search for missing sources | Targeted, in the order of row 17. Triage does not wait for it. Material not found is recorded as `UNVERIFIED / NOT RECEIVED`; regenerating a missing file is not historical recovery. |

**Framework for this record**, from the same proposal:

- classes C1–C4;
- each row with source location, current state, proposed action, acceptance criterion and edition effect;
- maintenance kept apart from new proof work;
- the triage PR adopts no claim, closes no pipe item and creates no tag;
- the edition's full content, its number and the grade of the two theorems remain later, separate PI decisions.

The orientation note's BOOTSTRAP 4 line ("the Methodology v1.4 migration is a separate, PI-decided edition unless the PI joins them") is answered by D5: the PI joined them as two stages of one edition.

## 8. Left for the PI after this record is reviewed

1. The scope of the edition: list (i) as written, or as amended by the review.
2. The edition number. The recovered chain used v0.9–v0.17, so reusing those numbers would make two different texts share one version label. Proposal: start above the recovered chain.

Rows 2–7 and 17 run as (ii) under D3, D4 and D7 and need no further decision to start.

## 9. Review

Requested: the second DZT co-owner (ChatGPT), change-focused, on this PR.

## 10. What this record does not do

It edits no DSN and changes no pipe state. It adopts nothing and regrades nothing. Every proposed change is made in the next edition through the ordinary cycle (branch, PR, review, PI decision, release record, merge, tag), or through the separate (ii) work and its own PI decision.
