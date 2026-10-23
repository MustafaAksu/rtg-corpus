import sys
G1 = "`RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (SHA-256 `5c00f66dae7d4de6ccd4a04d642a23edfc861bbd6bd55e432513747fbd679b55`)"
STATUS_OLD = "**Status:** [SESSION] OUTBOUND DRAFT — NOT SENT."
STATUS_NEW = ("**Status:** [SESSION] OUTBOUND NOTICE — FINAL FOR DISPATCH, NOT SENT. Drafted by the contributor; "
              "owner corrections by the RECOG co-owner (Claude), listed at the end. The PI sends it; dispatch and acknowledgment "
              "are recorded in `RECOG_G3_DISPATCH_RECORD_20261020.md`.")
def fin(name, reps, tail):
    s = open(f"RECOG_G3_NOTICE_TO_{name}_20261020_DRAFT.md").read()
    for a, b in [(STATUS_OLD, STATUS_NEW)] + reps:
        n = s.count(a)
        if n != 1: sys.exit(f"{name}: anchor count {n}: {a[:70]!r}")
        s = s.replace(a, b)
    s = s.rstrip("\n") + "\n\n## Owner corrections to the contributor draft\n\n" + tail.strip() + "\n"
    open(f"RECOG_G3_NOTICE_TO_{name}_20261020.md", "w").write(s)

# ---------------- Dyadic
fin("DYADIC", [
 ("**Recipient:** Dyadic Oscillator owner (verified available v6.4.16; reported current source v6.4.17).",
  "**Recipient:** Dyadic Oscillator owner. Editions known to RECOG: v6.4.16 (`33c14c5c…59e0`, release-verified); "
  "v6.4.17 (`e07cf2b9…4bfc`, adopted 19 Oct 2026) and v6.4.18 (`f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d`, "
  "adopted 20 Oct 2026), both with reviewer release verification pending according to Dyadic's own release records."),
 ("RECOG v0.3.21 was **adopted** 20 October 2026 (**not frozen**).",
  "RECOG v0.3.21 was **adopted** 20 October 2026 (**not frozen**)."),
 ("G1 record `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`.", f"G1 record {G1}."),
 ("Dyadic OPEN 12 was reported as PARTIAL;",
  "Dyadic OPEN 12 was reported as PARTIAL;"),
 ("## Reverse dependency and source-status request",
  "**v6.4.18.** RECOG's claim-level audit was run against v6.4.17. v6.4.18 is not claim-audited by RECOG. Its release record states that the "
  "changes are confined to OPEN 20 B-∞ existence (§6.17, `DYAD-THM-SMOOTH-EMBEDDING`) and that no adopted RID is renamed or regraded. "
  "RECOG records this as owner-reported and asks the owner to confirm that the RECOG-consumed passages (§1 import lines, §6.9 bridge-lemma "
  "provenance, §6.11 ν₃ import, OPEN 12, §6.14 and its consumer cross-references) are unchanged from v6.4.17. N14 (v6.4.18) is addressed to "
  "FMS, RRF and OFN, not to RECOG; RECOG records it as seen only.\n\n"
  "## Reverse dependency and source-status request"),
 ("Please update stale Dyadic RECOG “freeze candidate” status lines",
  "N13 asked RECOG to flag any change of the R9 statement, rows or $C_2$; the §7.3 notification rule is RECOG's answer, and no such change is made by v0.3.21.\n\n"
  "Please update the stale Dyadic “freeze candidate” lines for RECOG. In v6.4.18 they are: the header list of editions inspected in the v6.4.11 pass "
  "(“RECOG v0.3.20 (live header: freeze candidate)”); the §7 programme-context row (“`RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20` (freeze candidate)”); "
  "and the §7 consumer row (“live header: freeze candidate; final freeze record not inspected”). Please"),
 (" to distinguish frozen v0.3.20 from adopted v0.3.21, without changing theorem custody.",
  " distinguish frozen v0.3.20 from adopted v0.3.21, without changing theorem custody. Import tags of the form `[import: RECOG v0.3.20 §…]` "
  "may stay as they are or be repinned: the cited RECOG passages are identical in v0.3.21."),
],
"""
- Recipient line: added the adopted v6.4.18 edition and its hash. Both v6.4.17 and v6.4.18 have reviewer release verification pending, according to Dyadic's own release records.
- New v6.4.18 paragraph. RECOG audited v6.4.17, not v6.4.18. The v6.4.18 change summary is recorded as owner-reported, and Dyadic is asked to confirm that the RECOG-consumed passages are unchanged. N14 is recorded as seen, not received.
- N13's request to flag R9 changes is answered by the §7.3 notification rule.
- The stale "freeze candidate" lines are now named by location in v6.4.18. The import tags may stay pinned to v0.3.20, because the cited text is identical in v0.3.21.
- The G1 record is cited with its hash.
""")

# ---------------- RER
fin("RER", [
 ("see `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`.", f"see {G1}."),
 ("If repinning source excerpts, remeasure their locations in the exact adopted v0.3.21 bytes.",
  "If repinning source excerpts, remeasure their locations in the exact adopted v0.3.21 bytes. RECOG's own measurement uses the same section-boundary rule, which reproduces RER's v0.3.20 ranges exactly. "
  "§6.6a is at lines 521–546 in v0.3.21 (517–542 in v0.3.20). §6.16g is at lines 1006–1046 in v0.3.21 (1002–1042 in v0.3.20). "
  "Both sections are byte-identical between the two editions; only the line offset (+4) changes."),
 ("RER G9 should retain the **same-space** RECOG W3 as owner scope.",
  "RER G9 should retain the **same-space** RECOG W3 as owner scope. Its current r4.6 [DEF] line paraphrases W3 as "
  "“a shared pre/post comparison space”, which is close to RRF's transported-space reading. Please quote RECOG §6.16g W3 at source scope: "
  "“event-indexed cochains $a^-$, $a^+$ in the **same** cohomology space, so that $\\Delta[a]=[a^+]-[a^-]$ is defined”. "
  "W1 likewise requires one fixed directed graph, coefficient module and edge cochain."),
],
"""
- The G1 record is cited with its hash.
- Added the measured v0.3.21 line ranges for the two RER source excerpts. The cited text itself is byte-identical between the editions.
- RER G9's own paraphrase of W3 ("a shared pre/post comparison space") is flagged. RER is asked to quote RECOG's same-space W3 verbatim, with W1's fixed-graph requirement alongside. This is the same drift as RF-1 in a weaker form.
""")

# ---------------- OFN
fin("OFN", [
 ("G1 evidence record `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`.", f"G1 evidence record {G1}."),
 ("the antipodal-band guard remains as scoped.",
  "the antipodal-band guard (OFN v0.10 §7.3, imported by RECOG §7; §7.3 identical v0.8 → v0.10 in the G2 audit) remains as scoped."),
 ("by citing the G1 freeze record for v0.3.20,",
  "by citing the G1 freeze record and its hash above for v0.3.20 (REQ-O09-02 asks for the final freeze/adoption record and the exact source hash; "
  "v0.3.20's frozen hash is `fdb8c9a7…b8df`),"),
 ("then update current-use RECOG references to *adopted v0.3.21* where appropriate.",
  "then update current-use RECOG references to *adopted v0.3.21* where appropriate. In OFN v0.10 these include the “RECOG's live v0.3.20 metadata still says freeze candidate” sentence (RF-O08-06 action line, §11.3) and the RECOG v0.3.20 row of the §12.1 evidence and release-state register (also REQ-O09-02 in its request list)."),
],
"""
- The G1 record is cited with its hash, so that REQ-O09-02 (record plus exact source hash) can be closed from the notice itself.
- The antipodal-band guard is identified by its OFN section (v0.10 §7.3).
- The two OFN v0.10 places that still describe RECOG v0.3.20 as a freeze candidate are named.
""")

# ---------------- RRF
fin("RRF", [
 ("with external `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (G1).", f"with external {G1} (G1)."),
 ("and uses a *v0.3.20 freeze-candidate* qualification in §0.2.",
  "and uses a *v0.3.20 freeze-candidate* qualification in §0.2 and in the §4.2a import provenance. The §6.3 imports also pin v0.3.20 (§6.16b, §6.16g). "
  "The §0.1 receipts are marked by RRF as preserved draft-stage records, so they and the §10 and history entries are historical."),
 ("For example, conditional on a defined map `P: H^1(G_-,F_-)->H^1(G_+,F_+)`, the extended expression would be `[a^+]-P([a^-])`.",
  "For example, conditional on a defined map `P: H^1(G_-;F_-)->H^1(G_+;F_+)` (RECOG's notation is $H^1(G;F)$), the extended expression would be `[a^+]-P([a^-])`. "
  "An extension with $G_-\\ne G_+$ also departs from W1, which fixes one directed graph, coefficient module and cochain. W1 would then have to be stated at the extended scope as well."),
],
"""
- The G1 record is cited with its hash.
- Added to the list of live pins: §4.2a (v0.3.20 freeze-candidate provenance) and §6.3 (v0.3.20 pins). §0.1 is classed as historical, following RRF's own label.
- The RF-1 candidate map now uses RECOG's $H^1(G;F)$ notation. The notice also records that distinct pre- and post-birth graphs would depart from W1 as well as W3.
""")
print("OK")
