# Triadic DSN — pass-1 migration inventory (Methodology v1.3 bounded → v1.4)

Object: `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` at `triad-v1.6.1` (= main = HEAD of `claude/atlas-advisory-dyad-inbox`), SHA-256 `95340abe…451f` verified, 1202 lines. All line numbers below are in that file.
Rules read: `methodology-v1.4` §§1, 1.1, 3.2–3.5, 4, 8, 12, 13; `CONVENTIONS.md` §§1–7. Comparator: OFN v0.11 (`ofn-v0.11`) header L3–20, alias table L22–29.
Counting method: words = Python `str.split()` (Unicode whitespace); `wc -w` gives 18 989 for the whole file, the split count 19 169. Classification of "history" vs "scope label" is manual (Atlas judgement, not a lint result).
Read-only: nothing in the repository was edited.

---

## 1. Header (L1–17)

v1.4 §1 required order: Title, Date, Scope, Document class, Document status, Supersedes, Companion documents, DSN Methodology, Status summary; one line per field; current state only; Supersedes = immediate predecessor + hash; no "History —", previous status, draft chain or dated release-boundary text; one footer.

| L | Field (as named) | Words | Carries history / non-current content | v1.4 note |
|---|---|---|---|---|
| 1 | `# RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6.1` | – | – | ok |
| 3 | Title | 8 | – | ok |
| 4 | Date | 21 | yes — "DRAFT r2 19 October, DRAFT r1 18 October 2026); v1.6 adopted 5 October 2026" (draft chain + predecessor date) | date of this revision only |
| 5 | Scope | 23 | describes the revision task ("Integrate the accepted T-6s/t/u successor scope with … consumer reconciliation notices") rather than a one-sentence scientific scope | v1.4: "[one-sentence scientific scope]" |
| 6 | Document class | 5 | – "Technical scientific ledger" is a valid §0.5 profile | ok |
| 7 | Document status | 126 | yes — PI quote, review verdict, DRAFT r2 hash, build scripts `release_v1_6_1.py`/`check_release_v1_6_1.py`, "The v1.6 approval … is not reused", and "**History — v1.6 status text (5 Oct 2026):** …" | current status + pointer to adoption record only; no pointer to a `records/triad/…RELEASE_RECORD.md` |
| 8 | Supersedes | 25 | yes — names `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6.md` (versioned filename, no tag) + hash `c768687c…5b36`, then "v1.6 superseded `…_v1_5.md` … preserved as historical evidence" (an earlier edition) | immediate predecessor + hash only; no `triad-v1.6` tag exists in the repo (only `triad-v1.6.1`); the same v1.6 hash is cited by RER (`noncanonical/RTG_RELATIONAL_EMERGENCE_REGISTRY.md` L668) |
| 9 | Companion documents **(v1.6.1 refresh)** | 130 | yes — versioned filenames with adoption dates, "r1 pinned released v6.4.12.1", "v1.6 pointed to OFN v0.8, Dyadic v6.4.10, Genesis v2.8.4, OPEN-M v0.6 and RRF v0.6", and a dated **Release note (19 Oct 2026)** with hashes of Genesis v2.8.8 / Dyadic v6.4.14 / RRF v0.8.3 and a deferral ("repinning is deferred to the next Triadic maintenance pass") | field name carries a suffix; dated overlay; OFN form is "governing editions read for this edition — … (`tag`)" |
| 10 | DSN Methodology | 28 | states v1.3 "bounded migration … unchanged v1.2-era blocks retain their former forms" | to become v1.4 (tag) at migration |
| 11 | Status summary | 95 (5 sentences) | partly — "remains unchanged from reviewed r3", "The former safety-wedge/no-basin/phase-steering obstruction chain is not a current corrected-model result" | v1.4: 2–4 sentences, present state |
| 12 | Release base (v1.6.1) | 41 | entirely history — draft chain v1.6 → r1 (`31b87c3e…`) → r2 (`dd67907f…`), "**History — v1.6 release base:** r4.2 candidate `420eaf3e…`", v1.5 hash `07e9f00b…`, "Intermediate drafts remain in the preserved evidence/history" | release-record material (CONVENTIONS §3, v1.4 §13.7) |
| 13 | Co-owners (v1.6.1) | 64 | yes — "**History — v1.6:** Maintaining co-owner: ChatGPT … review-closure receipt …" | current roles may stay (OFN has Revision editor/Authors lines); history part is release-record material |
| 14 | Adoption record (v1.6.1) | 22 | yes — current pointers `records/OWNER_ADOPTION_v1_6_1.json`, `records/RELEASE_RECORD_v1_6_1.md` (neither in repo, §6 below) + "**History — v1.6 adoption record:** `records/OWNER_ADOPTION.json` … `records/RELEASE_RECORD.md`" | v1.4/CONVENTIONS path form `records/triad/TRIAD_v<version>_RELEASE_RECORD.md`; no such directory exists |
| 15 | Evidence location | 42 | partly — `evidence/accepted_r4_2/` (not in repo); "Historical package statuses retain their original dates …" | v1.4 layout `evidence/triad/…` |
| 16 | Programme tier | 15 | – "Tier 3 … no maturity regrade" | consistent with Programme v1.3 L265 (tier 3) |
| 17 | Preservation boundary (v1.6.1) | 105 | entirely release-delta text + "**History — v1.6 preservation boundary:** … all 49 RIDs …" | release-record material |

Header totals: 15 fields, 752 words. Five "History —" labels (L7, L12, L13, L14, L17). Fields carrying history: L4, L7, L8, L9, L11 (partly), L12, L13, L14, L15 (partly), L17.
Required fields present: all nine; "Companion documents" carries the suffix "(v1.6.1 refresh)". Fields present that v1.4 does not list: Release base, Co-owners, Adoption record, Evidence location, Programme tier, Preservation boundary (v1.4 allows "authorship, revision editor, owner, programme pointer, archive locator" to follow). Absent relative to the OFN v0.11 shape: Authors line, Revision editor line, Programme document/placement line (here "Programme tier"), Governing inputs, Evidence boundary.
§1 word count: 347 words (L32–51) — within the 200–400 target; no profile exception needed.
Footer (L1200–1202): **two footers** — v1.6.1 footer ending "The v1.6 footer below is history." followed by the full v1.6 footer (L1201–1202, citing `records/OWNER_ADOPTION.json`, "Revised blocks use Methodology v1.3; inherited v1.2 forms remain explicitly unmigrated"). v1.4 requires exactly one.

---

## 2. Live-text history in Local Tag Aliases and §§1–9 (L19–954)

Raw occurrence counts (L19–954): "histor*" 143 (110 lines); "former" 8; "superseded" 3; "no longer" 7; "r4.2" 10; "DRAFT r" 1; "v1.5" 10; "History —" 1; "v1.6.1" 33 (31 lines); "v1.6" 52 (42 lines); "previous/prior/earlier" 8. Most "historical" hits are scope labels (category C).

### A. Edition / draft / review / repin narrative (≈77 lines)

- **Aliases:** L27 "documents retained v1.5 aliases … inherited mixed-tag blocks await their separate migration" (and "canonical forms from `DSN_METHODOLOGY_v1.3`").
- **§1 (1):** L50 "No new numerical sweep is required for this r4 model-contract correction."
- **§2 (14):** L56 "T-6s/t/u retain the r3 successor statements"; L73 / L80 "Source v1.5 status: CLOSED `[ALG]`; the reviewed v1.6 … is now adopted"; L87 "Source v1.5 status … Revised v1.6 statement: ADOPTED"; L90 "rerun unchanged as historical evidence … registered by this owner release; no new identity is added beyond the accepted candidate"; L91 "Exact-candidate review and owner publication are complete"; L97 "historical RID `TRIAD-OPEN-T6M` remains preserved in the base/history"; L108 "… preserved in Appendix B/history"; L136 "Status: ACTIVE after r4 correction"; L144 heading "historical form superseded"; L149 "The historical protocol remains in the version record"; L192/193/194 "Historical predecessor verdict retained in Appendix B."
- **§3 (2):** L237 "Violation: using T-6p's historical export table after the r4 correction."; L251 SG-18 "(GCL-06; v1.6.1 D3)".
- **§4 (1):** L268 "CN-01–CN-05 scientific reconciliation against adopted v1.6".
- **§5 (1):** L300 row label "Birth remainder order (v1.6.1)".
- **§6 (21):** L316 "v1.6 stated the fifth-order remainder unconditionally; that was the Genesis v2.8.4 wording, narrowed by Genesis v2.8.5 GCL-06 and retained in v2.8.6/v2.8.7"; L317 "(r1 stated that no downstream T-6 result used the remainder order; that assurance was too broad.)"; L484 table header "Model/status after r4"; L489 "no numerical trajectory campaign for this release"; L552 / L589 / L618 "Adopted successor claim; scientific scope unchanged from accepted r4.2."; L553 / L590 "in the adopted v1.6 ledger"; L561 "The v1.5 equality … omitted the signed birth amplitude"; L567 "The v1.6 bounds … are the p=5 case" and "(co-owner receiving review, 19 Oct 2026)"; L572 "v1.6.1 r2 repin, definition unchanged"; L583 "The v1.5 phrase …"; L585 "(v1.6.1 r2 repin; record unchanged for this use since v2.8.4) … The earlier v2.8.3 live pointer … superseded"; L621 "unchanged from reviewed r1 … review findings through r4.1 remain historical; exact r4.2 sign-off is accepted and owner publication is recorded separately"; L632 / L639 "v1.6.1 r2 repin … unchanged"; L648 "This explains why v1.5 used 7/1024"; L656 "written here in v1.6"; L707 table header "This revision's answer"; L753–772 "Per-module dispositions" table headed "Adopted v1.6 disposition (accepted r4.2 scope)" (L755), incl. task wording L757 "Attach recovered producer and fresh output to the existing artifact identity" and L769 "replace with the remaining corrected state/carrier/test contract".
- **§7 (27):** L779 heading "Retained dyadic import block — historical source pins"; L781 "pinned in v1.5/v1.6 to … v6.4.8.1 … v1.6.1 (Dyadic notice N2 …) … (v1.6.1 r2, erratum E1; r1 pinned released v6.4.12.1, SHA-256 `36e7ef58…`)"; L785 "*(v1.6.1 repin from `DYAD-ALG-LIEGAUGE-NORM` …)*"; L786 "*(v1.6.1 repin, same source)*"; L787 "*(v1.6.1 RID fill, Dyadic notice N1 / OFN CUST-O09-01)*"; L801 "(v1.6.1 pointer refresh from v0.8 …)"; L802 "(v1.6.1 pointer refresh from v0.6 …)"; L803 "**v1.6.1 receipt:** Genesis v2.8.5 … retained unchanged in v2.8.6/v2.8.7"; L811 "REQ-T16-METRIC resolved in v1.6.1 — owner RIDs assigned by Genesis v2.8.5 §6.1 and retained in v2.8.7"; L812, L815, L816, L817, L818, L819, L820, L821, L822 "v1.6.1 repin, … unchanged" inside the `[import: …]` tag; L813 "wording retained from v2.8.5 GCL-06"; L814 "v1.6 imported the fifth-order form unconditionally from v2.8.4"; L824 "have been recovered and rerun with their original bytes"; L826 heading "Exports — adopted v1.6"; L833 "at their r3 scopes"; L835 "remain retrievable in the base/history"; L841 "**v1.6.1 consumer receipt …** Genesis v2.8.5 (adopted 5 Oct 2026; retained in v2.8.6/v2.8.7) … `[v1.6.1 r2 — H-R1]` …"; L864 CN-05 "**From:** Triadic v1.6, adopted owner release of accepted r4.2 science; exact source identity is in `records/OWNER_ADOPTION.json`"; L888 "Exact r4.2 revision-editor review is accepted and this owner release is issued at the user's instruction".
- **§8 (5):** L923 "The prior 14-count was a reporting error"; L927 "Inputs: byte-pinned Genesis v2.8.4 … Triadic v1.5 base, preserved r1"; L932 "Review state: r1–r4 reviews and the supplied r4.1 review reports … R4.2 corrects … exact r4.2 sign-off is accepted …"; L937 "`[DEF]` **R3 verification addendum.**"; L939 "`[DEF]` **R4.2 review-closure and owner-release addendum.**" (L918 contains r4_2 file names and "The pinned audit bytes remain unchanged" — partly).
- **§9 (4):** L945 "**History — v1.6 release:** …"; L947 "**Evidence history:** … The r1 availability claim is corrected as a former local-access limitation … The peer explicitly accepted responsibility …"; L948 "Historical project pointer inherited from v1.5: Zenodo DOI 10.5281/zenodo.17568897"; L953 "`[COR]` **R4 recovered-producer provenance.**" (block sits after §9's `---`, before Appendix A).
- Also stale fact in §9: L949 "Repository: `rtg-resonance-2025`" (current repository is `rtg-corpus`).

### B. Change-narrative wording inside live claims ("former / prior / previous / no longer / withdrawn") (≈26 lines)
These state current scope by contrast with an earlier claim; v1.4 §1.1 puts the change record in Appendix A/B and keeps the current statement live.
L36 ("global-explosiveness inference from T-1 alone is withdrawn"), L44 ("T-6j2's prior 0/120 … is withdrawn"), L46, L61 ("it no longer controls"), L121 ("no longer a safety-wedge … test"), L138 (`[COR]` "The former closed sub-item … is reopened"), L166 ("the old mirrored-x_* heuristic is historical"), L215 ("The old argument …"), L224 ("It no longer carries …"), L329 ("The ledger no longer uses 96:1 …"), L359 ("An inherited point-of-use line wrote …"), L417 ("The previous argument … is withdrawn"), L432 ("The prior chiral-heavy T-6b seeds …"), L448, L495 ("The prior synthesis …"), L501–505 ("Revoked current-use overclaims:" list), L517, L519, L521 ("no longer gates"), L529 (`[RETRACTED]` block in live §6.13), L535, L548 ("T-6r now concerns …"), L605 ("T-6t's former … wording"), L701 ("The former headline …"), L719 ("The prior B_3-isometric number …").

### C. Legitimate scope labels (not counted as history)
"historical executed mis-scaled (orientation) model" / "historical diagnostic" / "historical root-closed session" naming preserved diagnostics and their models: L40, L42, L110, L113, L171, L185, L187–191, L200, L206 (`M_{j2}^{hist}`), L209, L218, L221, L239, L263, L265, L267, L290, L294, L325, L368, L434, L450, L464, L466 (heading), L468, L470, L472, L482 (heading "Historical Protocol Reference"), L486–488, L491, L523 (heading), L525, L745, L790–791, L910–917, L922–924 ("**Historical evidence only:**").

---

## 3. Tags (v1.4 §§3.2, 3.4, 3.5, 8.4)

### 3.1 Local Tag Aliases table (L19–28)
- Column names "Local alias | Expands to | Used for" (v1.4 §8.4: "Local alias | Canonical expansion | Use"; OFN v0.11 L24 uses the v1.4 names).
- L23 `[ALG diagnostic]` → `` `[ALG]` `[scope: diagnostic]` `` (qualifier in backticks). Used 27× (live: L99, 176–186, 339–397, 406, 412, 415, 442, 460; App A/B: L1041, 1164, 1168).
- L24 `[NUM diagnostic]` → `` `[NUM]` `[scope: diagnostic]` ``. Used 12× (live: L179, 182, 183, 348, 368, 421, 430, 438, 440, 482; App A L1054).
- L25 `[ALG/NUM synthesis]` → "`[ALG]` co-interpreted with `[NUM]`" — the slash-combination §8.4 says must be unpacked. **Not used in any live claim**; only other occurrence is App A v1.0 L1083 (history).
- L27–28: two `[DEF]` lines that are tag-usage/administrative notes (v1.3 reference; "inherited mixed-tag blocks await their separate migration").

### 3.2 Undeclared or compound tags
| Tag | Lines | Note |
|---|---|---|
| `[ALG+NUM diagnostic]` | L916 (live §8, `TRIAD-ART-T6M-BIRTH`); L1068 (App A v1.1) | compound, not declared |
| `[NUM historical]` | L1165 (App B table) | not declared; live L525 uses `[NUM]` + scope |
| `[DEF/ALG]` | L575, L821 | quoting Genesis source status of the HINDEX norm row ("Source status: … `[DEF/ALG]`") |
| `[ALG, exact]` | L1047 (App A v1.4, quoted history) | history only |
| `[ALG]` `[scope: structure]` rendering of source `[ALG structure]` | L319, L815 ("rendered canonically above without a grade change"), L816 | v1.4 §8.4: an alias "cannot override a canonical tag, including `[ALG structure]`"; listed only |
| App B status column vs live tag | L1164 `[ALG diagnostic]` for `TRIAD-ALG-T6M-REFERENCE-QUARTER-TURN` (live L509: `[ALG]` `[scope: declared reference initialization]`); L1168 `[ALG diagnostic]` for `TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION` (live §6.18 heading `[COR / ALG]`, blocks `[ALG]`) | rendering differs between live and App B |
| Untagged module record | L191 "T-6l :: historical algebra retained …" (no truth tag) | – |
| `[COR]` paired with a claim tag | L38 `` `[COR]` `[ALG]` `[scope: …]` `` | – |

### 3.3 Section-heading grade tags (v1.4 §3.5 form: `` `[ALG]` — mixed content ``)
L310 `[ALG / mixed]`; L337, L350, L370, L507 `[ALG diagnostic / mixed]`; L406 `[ALG diagnostic]`; L421, L482 `[NUM diagnostic]`; L436, L454, L466 `[ALG/NUM diagnostic / mixed]` (compound); L493 `[COR / mixed]`; L523 `[NUM / PARTIAL]` (workflow word inside the tag); L533 `[DEF]`; L723 `[COR / ALG]` (compound). No heading tag: L550 §6.15, L587 §6.16, L614 §6.17, L623/650/673/703 §6.17.1–4 (also no anchors), L753 "Per-module dispositions" (no anchor), L886 "Export protocol" (no anchor). (Precedent note: OFN v0.11 has no `[X / mixed]` headings; Dyadic v6.4.22 uses "— entry grades: …" prose; Genesis v2.9 still has 11 `` `[X / mixed]` `` headings.)

### 3.4 Qualifier style (v1.4 §3.2: truth tags in backticks, qualifiers in plain brackets)
- **Backticked qualifiers** (v1.2-era form) — 56 occurrences (54 in live text; L1081, L1094 are Appendix A), e.g. L36, L38, L42, L44, L46, L99, L110, L147, L173–174, L185–190, L321, L325, L331, L450, L464, L468, L470, L474, L497, L509, L513, L525, L747, L790–796, L899–917; incl. `` `[scope: conditional on the selected child functional]` `` L316, L567, L656, L814 and `` `[conv: …]` `` L790, L791, L796.
- **Plain-bracket qualifiers** (v1.3-revised blocks) — 24 occurrences: L87, L192–194, L319, L552, L559, L563, L567, L569, L577, L580, L589, L596, L607, L618, L625, L658, L667, L686, L695, L714, L815, L816.
- **Dash-style / version-stamped qualifiers** (OFN v0.11 L29: "compound dash spellings are not used in live claims"): `` `[COR v1.6.1 — D3]` `` L316, L656, L814 (+L978 App A); `` `[COR v1.6.1 r2 — D3-R1]` `` L317, L567, L849 (+L970 App A); `` `[v1.6.1 r2 — H-R1]` `` L841. Plus SG-18 text "(GCL-06; v1.6.1 D3)" L251.
- **Local typing sentinels** `(rep: [...])`, not in the §3.2 registry: 21 lines (L566, 571, 574, 579, 582, 602, 609, 629, 636, 647, 657, 663, 670, 680, 684, 700, 716, 732, 736, 848, 855) — `[UNREGISTERED-TRIADIC-PRIMITIVE]` 13, `-SOURCE` 4, `-JACOBI` 1, `[ABSTRACT]` 1, two free-text (L732, L736). L630 declares them "local typing sentinels, not assigned RRF profile identifiers".

### 3.5 `[RESULT]`
Live claims: L497 and L747, each `` `[RESULT]` `[from: ALG]` `` — single `from`, compliant (qualifier backticked). Other occurrences are prose about Genesis (L803, L841) or history (L979, L1020; App B L1158 records `[from: HEUR]`→`[from: NUM]`). **No bare `[RESULT]` and no multi-status `from` in live text.**

### 3.6 Other
Live `[COR]` blocks: 19 (L28, 38, 138, 329, 359, 404, 417, 434, 495, 519, 561, 583, 605, 648, 665, 701, 719, 728, 953) plus the 8 version-stamped `[COR v1.6.1 …]` uses. `[DEF]` used for administrative/addendum text: L27, L28, L888, L890, L892, L937, L939. Live `[RETRACTED]`: L529 (§6.13). Live `[FAIL]`: L408.

---

## 4. RIDs

### 4.1 TRIAD namespace
46 distinct `TRIAD-*` RIDs (every one appears at least once in `[RID: …]` form). By category: ALG 13 (incl. retired), ART 22, NUM 2, OPEN 7, EXPORT 2.
- Live current: `TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY` (L71…), `-T6T-JACOBI-MODE-SIGNS`, `-T6U-APEX-SEED-DIAGNOSTIC`, `-T6M-REFERENCE-QUARTER-TURN` (L95, 509), `-T6E-ORIENTATION-NORMALIZATION` (L725), `-T6L-NORMALIZED-TORSION-SIGN` (L474), `TRIAD-NUM-T6J2-ROOT-CLOSED-EXCURSION` (L106, 525), `TRIAD-EXPORT-PROTOCOL-2` (L144, 535), OPEN `T6M2`, `T6N`, `T6O`, `T6R`, `T6Q` (L117–162), 22 `TRIAD-ART-*` (L899–925, L726).
- Retired/historical (cited in live and App B): `TRIAD-ALG-T6S-INPLANE-CHIRALITY`, `-T6T-CHIRALITY-COUNT`, `-T6U-APEX-SOURCE`, `-T6M-BIRTH-OBSTRUCTION`, `TRIAD-NUM-T6J2-NO-BASIN`, `TRIAD-EXPORT-PROTOCOL-1`, `TRIAD-OPEN-T6M`, `TRIAD-OPEN-T6J2`, `TRIAD-ALG-SAFETY-WEDGE`, `TRIAD-ALG-VERDICT`, `TRIAD-ALG-ISC-ATTRACTOR` (App B L1175 only).
- The text asserts "all 49 RIDs" (L17, L980, L986); 46 distinct TRIAD strings appear in v1.6.1. **Could not determine** the other three: the v1.5/v1.6 bytes are not in the repository.
- Format: `TRIAD-EXPORT-PROTOCOL-1/-2` use "EXPORT", which is not a §4.2 category (listed only).
- `RER-TRIAD-BIRTH-GRAPH-INVOLUTION` (L814, L970) is an RER navigation key, not a TRIAD RID (v1.4 §4.2).

### 4.2 Other-namespace identifiers cited, checked at the governing tag ("RID: X" present?)
| ID | Triadic lines | Owner @ tag | Result |
|---|---|---|---|
| DYAD-THM-C21 | 783 | dyad-v6.4.22 | ✓ L467 (§6.2) |
| DYAD-ALG-BRIDGE-LEMMA | 784 | dyad-v6.4.22 | ✓ L629 (§6.9) |
| DYAD-DEF-BRIDGE-EXPORT-CONTRACT | 781, 785, 979 | dyad-v6.4.22 | ✓ L710 (§6.12) |
| DYAD-ALG-PROTECTION-MATRIX | 786, 979 | dyad-v6.4.22 | ✓ L699 (§6.11) |
| DYAD-DEF-PRIMITIVE-MAP | 787, 979 | dyad-v6.4.22 | ✓ L436 (§6.1); §1 readout L47. Triadic cites "Dyadic v6.4.13 §1" |
| DYAD-ALG-LIEGAUGE-NORM | 785 | dyad-v6.4.22 | ✓ |
| DYAD-THM-FORMAL-Z6-GENERATOR | 781 (named as not imported) | dyad-v6.4.22 | ✓ |
| RECOG-ALG-LEADING-RETURN-EQUIVARIANCE | 784 | recog-v0.3.26 | ✓ L39 |
| GEN-DEF-PRIMITIVE-MAP | 787 | gen-v2.9 | ✓ L31 (alias of DYAD-DEF-PRIMITIVE-MAP) |
| GEN-DEF-PRIMITIVE-METRIC | 811, 979 | gen-v2.9 | ✓ L655 |
| GEN-THM-PRIMITIVE-METRIC-INVARIANCE | 811, 979 | gen-v2.9 | ✓ L657 |
| GEN-THM-DELTA-QC | 822, 851 | gen-v2.9 | ✓ L953 (§6.5) |
| GEN-THM-K3-PLANAR-FACTOR-NOGO | 804 | gen-v2.9 | ✓ |
| GEN-THM-K3-SIXSTEP-FACTOR-NOGO | 804 | gen-v2.9 | ✓ |
| GEN-OPEN-APEX-SLOT | 612, 803, 843, 979 | gen-v2.9 | ✓ as `[RID preserved: …]` `[RETRACTED]` L378, L1255 |
| GEN-OPEN-HINDEX | 575, 821 | gen-v2.9 | ✓ L383 (module locator) |
| GEN-OPEN-WPHASE | 845 | gen-v2.9 | ✓ L173 |
| GEN-OPEN-WPHASE-GSPLIT | 585, 851 (+1049) | gen-v2.9 | ✓ L208 |
| GEN-ART-G3D-SEED / -JQ-PHASEDRIFT / -PHI-2TO3 / -WPHASE | 637, 819 / 812, 820 / 314, 813 / 845, 849 | gen-v2.9 | ✓ each declared once |
| TDRG-OPEN-CHI-SCALING | 805 | tdrg-v2.12.14 | ✓ L272 |
| Non-RID keys (exist as names, no "RID:"): | | | |
| OPEN-GEN-II-HINDEX | 572, 821 | gen-v2.9 | name present (L99, L383) |
| GCL-03, GCL-05, GCL-06 | 821; 803, 841; 17 lines | gen-v2.9 | correction keys present (4/2/11 mentions) |
| HYP-M-PREFRACTURE, R-CHIRALITY-RECONCILIATION, R-CHIRALITY-CLOSURE, AUDIT-1-DIMENSIONAL | 841, 858; 841; 845, 858; 845 | uvm-v0.7.1 | names present; no "RID:" form in OPEN-M |
| CUST-O09-01 | 787 | ofn-v0.11 | present ("answered", L270, L1067) |
| SG-PROG-1 | 800 | programme-v1.3 | present (guard) |
| OPEN-A / OPEN-B-E1 | 802 | rrf-v0.8.4 | OPEN-A present; **"OPEN-B-E1" not found verbatim** — RRF spells "OPEN-B/E1" / "OPEN-B → OPEN-E1" |
| REQ-T16-* (10 keys) | 811–821 | local tracking keys | none appear in gen-v2.9 |
| CN-01…CN-05 | many | local notice keys | – |

"RID unavailable" import exceptions in live text: 14 (L314, 572, 632, 639, 652, 812–820). At gen-v2.9 §§6.1–6.6 no new RID was found for those statements (birth theorem, J_Q, shear/recoil, chronological protection, P4, vector seeds, birth symmetry); the exceptions are still open as recorded.

---

## 5. Companion / import pins vs governing editions (listing only)

| Study (governing tag) | Pins in Triadic (line) |
|---|---|
| Methodology (`methodology-v1.4`) | v1.3 — L10, L27; footer L1202 |
| Programme (`programme-v1.3`) | v1.2 — L9, L705 (§6.17.4 "Programme v1.2 §6.3's questions"), L800, L841 |
| OFN (`ofn-v0.11` per caller and BASELINE; note tag `ofn-v0.12` also exists in the repo, not yet in BASELINE) | v0.9 — L9, L801, L841; v0.8 (history) — L9, L801 |
| Dyadic (`dyad-v6.4.22`) | v6.4.13 (with hash `5958f7fe…542`) — L9, L781, L783–787; v6.4.12.1 (r1, hash) — L9, L781; v6.4.11 (statement source) — L781; v6.4.8.1 (history) — L781; v6.4.10 (history) — L9; v6.4.14 (release note, hash) — L9 |
| Genesis (`gen-v2.9`) | v2.8.7 — L9, L314, L567, L572, L585, L632, L639, L652, L804 (with hash `d5d1e57c…361`), L811–822; v2.8.8 (release note, hash `9abd3616…`) — L9, L781; v2.8.6 — L787, L803, L804; v2.8.5 — L316, L803, L811, L813, L821, L841; v2.8.4 — L9, L316, L585, L814, L843 (CN-01 target), L845 (CN-02 target, "source line 907"), L851 (CN-03), L927 (evidence input); v2.8.3 — L585 |
| OPEN-M (`uvm-v0.7.1`) | v0.7.1 — L9, L841 (current); v0.6 — L9 (history), L845 (CN-02 target), L858 (CN-04 target) |
| RRF (`rrf-v0.8.4`) | v0.8.2 §3.1 — L9, L802, L841; v0.8.3 (release note, hash) — L9; **v0.6 — L612 (live §6.16 "RRF v0.6 is likewise cited …")**, L9/L802 (history) |
| TDRG (`tdrg-v2.12.14`) | v2.12.13 — L9, L805 |
| RECOG (`recog-v0.3.26`) | RECOG-ALG-LEADING-RETURN-EQUIVARIANCE cited unpinned via Dyadic — L784 |
| Triadic self | v1.6 — L8, L268, L826 heading, L864 (CN-05 "From"); v1.5 — L8, L12, L73, L80, L87, L927 |

Cited Genesis anchors `#sec-6-1-primitive`, `#sec-6-3-triad`, `#sec-6-4-tetrahedral`, `#sec-6-5-quartic`, `#sec-6-6-phase` all exist at `gen-v2.9`. No judgement on repin safety is made here.

---

## 6. Evidence custody

Repository facts: `records/triad/` and `evidence/triad/` do not exist; no Triadic release record, adoption record, script or output is in `git ls-files` at HEAD or main, nor (by basename) in any commit on any ref, except as noted. BASELINE.md L17 registers `triad-v1.6.1` by "XREF: RER v0.2 §7 (`TRIAD161`, byte-verified there)". `pipes/TRIAD/` inbox is empty.

| Path / file (Triadic lines) | In repo? |
|---|---|
| `records/RELEASE_RECORD_v1_6_1.md`, `records/OWNER_ADOPTION_v1_6_1.json` (L14) | **No** (any ref) |
| `records/OWNER_ADOPTION.json` (L14, 864, 939, 984, 1202), `records/RELEASE_RECORD.md` (L14), `records/METADATA_EDITS.json` (L945) | **No** |
| `evidence/accepted_r4_2/` (L15) | **No** |
| `evidence/EXECUTION_MANIFEST.json`, `evidence/FILE_IDENTITIES.json` (L925), `evidence/EXECUTION_MANIFEST_R4_2.json` (L918), `evidence/t6u_certificate.json` (L929), `RECOVERED_HISTORICAL_RUNS.json` (L922–924), `environment.json` (L929) | **No** |
| `triad_t6_producers.zip`, `SHA256_MANIFEST.csv`, `t6c2_out.json`, `t6e_out.json`, `triad_orientation_normalization_audit.py`, `scripts/triad_torsion_object_check_r4_2.py` (L918) | **No** |
| `tetrahedral_six_step_cross_phase_t6c2_patched.py` (L903, hash `afb4525c…d80e`) | **Not in current tree**; bytes exist in commit `9df0319` (`upload/tdrg-records/`, ancestor of main) and **match the recorded SHA-256 exactly**; removed by `07df334` ("remove 12 unrelated and duplicate files before custody merge") |
| `triad_analytic_phase_steering_t6l_patched.py` (L915, hash `2e0317bf…11cd`) | same as above — in `9df0319`, **hash matches**, removed by `07df334` |
| `tetrahedral_six_step_omega_t6e.py` (L904), `t6b_orthogonal_ode.py` (L908), `t6d_generalized_ode.py` (L909), `triad_direct_orientation_ode_t6f_v2.py` (L910), `triad_free_qc_dimensionless_ode_t6h_v2.py` (L911), `triad_safe_arc_basin_search_t6j.py` (L913) | **No** |
| `triad_t6s_chirality.py`, `triad_thread4_chirality_count.py`, `triad_t6u_apex_source.py` (L922–924; `inputs/historical/…`) | **No** |
| `triad_t6u_apex_source_v1_6.py` (L90, 621, 925, 929 as `scripts/…`), `triad_v1_6_r2_point_use_checks.py` (L621, 925), `scripts/run_all.py` (L929), `T6U_PROOF_AND_SCOPE.md`, `triad_v1_6_r3_scope_checks.py`, `validate_r3.py`, `inputs/r2/` (L937), `inputs/r1/` (L1035) | **No** |
| `release_v1_6_1.py`, `check_release_v1_6_1.py` (L7, 961); `build_v1_6_1_r2.py`, `check_v1_6_1_r2.py` (L969); `build_v1_6_1_draft.py`, `check_v1_6_1_draft.py` (L977) | **No** |
| `TRIAD_RER_R2_R41_RECEIVING_REVIEW_20261019.md` (L960), `TRIAD_D3_RECEIVING_REVIEW_20261019.md` (L969) | **No** |
| `dyad_triad_antisymmetric_bridge_v1_1.md` (L781; text itself says "still not in this package") | **No** |
| `apex_ratio_setup.py` (L89, 824, 947), `genesis_k4_route_census.py` (L818) | **No** (text says unavailable) |
| `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_5.md`, `…_v1_6.md` (L8, L12) | **No** (no `triad-v1.5`/`triad-v1.6` tags) |
| Session-only artifacts `TRIAD-ART-T6M-BIRTH` (L916), `TRIAD-ART-T6J2-PROXY` (L917); placeholders "proof-source reference required" L899–902, L905 | stated as unavailable/placeholder in text |

Related external note: RER registry cites Triadic sources at `sources/current/TRIAD_R4/…` (e.g. RER L871–872, L956–959, L1002) — those paths are also not in the repository.

### T-3a Arb enclosure
- **The Triadic text (all 1202 lines) contains no reference to T-3a, to an Arb/FLINT enclosure, or to any interval-arithmetic certificate.** There is no T-3 module at all (modules are T-1, T-2b, T-4h, T-6*). No `[ALG via IA]`/`[THM-ALG via IA]` tag occurs. So there is no place where Triadic cites it, and no grade to report.
- The file `upload/dyad-sources/rtg-engine/triad_t3a_arb_enclosure_v4g.cpp` (SHA-256 `430015bb…fd32`; header comment "Module Status: [ENG / ALG target - Strict Arb Interval Certification]") is in commit `59b3f87`, contained in `claude/atlas-advisory-dyad-inbox` and also in `origin/upload/dyad-sources` (not on main). Its manifest (`MANIFEST_rtg-engine.txt` L40–41, L77–78) also lists a compiled binary `triad_t3a_arb_enclosure` (`7962be55…`) that was not uploaded.
- `records/dyad/DYAD_UPLOAD_HASH_CHECK_20261030.md` L30 classifies it "not a certificate as written" (placeholder forcing `dz`=0 at L91–96, dummy `+1` Q_c step at L125–130, still prints `[CERTIFIED …]` at L135), and routes it "to the Triadic custody review"; `records/dyad/DYAD_OWNER_ENTRY_NOTE_INBOX_20261030.md` L56 agrees. No pipe item for TRIAD exists.

---

## 7. Size and structure

Whole file 19 169 words (split count). By section: Header 752; Aliases 120; §1 347; §2 1 707; §3 699; §4 295; §5 378; §6 5 867; §7 3 100; §8 1 187; §9 (+L953) 333; Appendix A 3 165; Appendix B 1 126; footers 93.

### Appendix A (L955–1131) — 18 entries, by edition
| Edition | Entries (lines) | Words |
|---|---|---|
| v1.6.1 | owner release L957–966 (232), DRAFT r2 L967–974 (261), DRAFT r1 L975–981 (249) | 742 |
| v1.6 | owner release L982–989 (163), r4.2 L990–996 (167), r4.1 L997–1004 (131), r4 L1005–1015 (153), r3 L1016–1023 (240), r2 L1024–1033 (299), r1 L1034–1039 (134, incl. `[COR]` count notice L1038) | 1 287 |
| v1.5 | L1040–1045 | 137 |
| v1.4 | L1046–1052 | 157 |
| v1.3 | L1053–1058 | 86 |
| v1.2 | L1059–1064 | 84 |
| v1.1 | L1065–1072 | 88 |
| v1.0 | L1073–1109 (two errata lists) | 441 |
| v0.15 | L1110–1121 | 101 |
| v0.14 and earlier | L1122–1131 | 35 |

Content that v1.4 §1 / CONVENTIONS §3 assigns to release records: draft-round entries (r1–r4.2, v1.6.1 r1/r2: 10 of 18 entries, ~1 640 words), review verdicts (L960, L969, L985, L995), build/check script names (L961, L969, L977), the L964 note "Dated draft text below: 'not adopted' labels … are history of the draft stage".

### Appendix B (L1132–1198) — 4 subsections
1. "Adopted v1.6 successor lifecycle" L1134–1145 (223 w): `[DEF]` preamble + 3-row table (historical RID → successor, reason) + `[COR]` Thread-4 count.
2. "Adopted v1.6 corrections" L1146–1159 (332 w): 6 `[COR]` paragraphs, no RIDs, no "Recorded in:".
3. "Adopted v1.6 orientation-chain lifecycle (reviewed r4–r4.2 dispositions)" L1160–1183 (330 w): 5-row table, `[DEF]` list of 5 retained historical RIDs (L1172–1176), 3 `[COR]` paragraphs.
4. "Preserved v1.5 rejected-claim record" L1184–1198 (232 w): 5 `[RETRACTED]` + 6 `[FAIL]` bullets without RIDs or "Replacement/Recorded in" fields. Listed without judgement: several bases cite items the live text withdraws (L1187–1188 "phase steering drives toward fatal Plücker sectors"; L1192 "7.8× outside torsion-safe wedge" vs live L417; L1195–1196 wedge-based bases).
v1.4 §1 template form (`` `[SUPERSEDED]`/`[RETRACTED]`/`[FAIL]` [RID: …] Original: … Reason: … Replacement: … Recorded in: vX.Y ``) is not used.

---

## Not determined
- Identity of the 3 RIDs behind "all 49 RIDs" (v1.5/v1.6 bytes absent).
- Whether any Triadic evidence package exists outside the repository (only the text's own claims are available).
- Whether `ofn-v0.12` (tag present, not in BASELINE) should replace `ofn-v0.11` as the OFN comparator/governing edition — left to the caller.
