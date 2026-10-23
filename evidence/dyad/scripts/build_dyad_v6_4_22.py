#!/usr/bin/env python3
"""DYAD v6.4.22 (errata draft candidate): single-stage, assertion-gated build from adopted v6.4.21.

Scope (owner review records/dyad/DYAD_OWNER_REVIEW_v6_4_21.md, accepted by the co-owner review of 23 Oct 2026,
"OWNER REVIEW ACCEPTED — v6.4.22 ERRATA DRAFT AUTHORIZED"):
  F1     §7.0 Dyadic row names the current edition and its predecessor
  F2/F3  notice-table intro and Appendix F intro: N16–N21 prepared, not sent
  F4     every live "R11" names its owner (RECOG R11 / OPEN-M R11), classified one by one; Appendix C row
  F5     P2B provenance replay status at its recorded level (§6.14, §8)
  W1–W3  two "superseded" sentences removed; §6.13 heading-tag sentence
  H4     second-route h4 check cited (§1, §8, Appendix E)
  ED     edition/status lines (title, date, status, supersedes, release record, Appendix A entry, Appendix G note, footer)
No compaction, no RID/grade/statement/OPEN-status change. Appendix A history is not edited (one entry is added).
Every edit asserts exactly one occurrence of its old text in the current working text.
usage: build_dyad_v6_4_22.py BASE OUT EDITLOG_JSON
"""
import hashlib, json, sys

BASE_SHA = "a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d"
H4R = "dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6d"
REC = "records/dyad/RTG_DYADIC_v6_4_22_RELEASE_RECORD.md"
NOT = "`records/dyad/DYAD_NOTICES_N16_N21.md`"

EDITS = [
# ---- ED: edition/status lines ----
("ED-1", "title", "# RTG_DYADIC_OSCILLATOR_DSN_v6.4.21\n", "# RTG_DYADIC_OSCILLATOR_DSN_v6.4.22\n"),
("ED-2", "header date", "**Date:** 22 October 2026  \n", "**Date:** 23 October 2026  \n"),
("ED-3", "header status",
 "**Document status:** ADOPTED — PI, 22 October 2026 (closeout errata and Methodology v1.4 compaction pilot). Adoption record: `records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md`.",
 "**Document status:** DRAFT — v6.4.22 candidate (owner errata: current-state wording, owner labels for RECOG R11 and OPEN-M R11, three wordings, second-route $h_4$ evidence); not adopted."),
("ED-4", "header supersedes",
 "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.20` (SHA-256 `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`; tag `dyad-v6.4.20`).",
 "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.21` (SHA-256 `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d`; tag `dyad-v6.4.21`)."),
("ED-5", "header release record",
 "**Release record:** `records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md`. Version history: Appendix A.",
 "**Release record:** `" + REC + "`. Version history: Appendix A."),
("ED-6", "Appendix G note",
 "v6.4.21 keeps every heading anchor of v6.4.20.", "v6.4.21 and v6.4.22 keep every heading anchor of v6.4.20."),
("ED-7", "footer",
 "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.21 (ADOPTED, 22 October 2026).*",
 "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 (DRAFT candidate, 23 October 2026).*"),
# ---- F1 ----
("F1", "§7.0 Dyadic row",
 "| Dyadic (this ledger) | v6.4.19 | ADOPTED 20 Oct 2026; superseded by v6.4.20 (this edition, adopted 21 Oct 2026; its SHA-256 is in `RTG_DYADIC_v6_4_20_RELEASE_RECORD.md`) | `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9` | release record; verification record | base of P1/P2 |",
 "| Dyadic (this ledger) | v6.4.22 | this edition; status in the header; its SHA-256 is in its release record | predecessor v6.4.21: `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d` | tag `dyad-v6.4.21`; release records in `records/dyad/` | earlier editions by tag (`dyad-v6.4.20`, `dyad-v6.4.19`; v6.4.19 is the base of the ATLAS P1/P2 work) |"),
# ---- F2 / F3 ----
("F2", "§7 notice-table intro",
 "\"Where recorded\" names the consumer record read for this edition; \"NOT RECORDED\" means no receipt was found there, not that the notice was refused. Notices N16–N20 (ATLAS disposition §6) are prepared only after external verification of this edition's SHA-256; none is prepared in this edition.",
 "\"Where recorded\" names the consumer record read when the row was last updated; \"NOT RECORDED\" means no receipt was found there, not that the notice was refused. Notices N16–N21 are prepared and not yet sent (" + NOT + ", routed through the PI); their states per recipient (sent, received, statement accepted, adopted use) are kept there and entered in this table when a state is recorded."),
("F3", "Appendix F intro",
 "consumer repins are requested by planned notice N17, after external verification of this edition's SHA-256.",
 "consumer repins are requested by notice N17 (prepared, not yet sent; " + NOT + ")."),
# ---- F5 ----
("F5a", "§6.14 L-PHASE distinctions (iv)",
 "negative-control exit codes recorded separately; **reviewer full replay pending**.",
 "negative-control exit codes recorded separately. Reviewer replay (v6.4.19 release verification, 21 Oct 2026): G14 and the G15 main gate each replayed separately; the combined G14–G15 run and the separate-process M1–M4 exit codes are **not completed**."),
("F5b", "§8 DYAD-ART-LPHASE-P2B-PROV",
 "4 negative controls (exit 1 each; crash exits 3); owner replay; reviewer full replay pending ::",
 "4 negative controls (exit 1 each; crash exits 3); owner replay; reviewer replay of the main gate separately (v6.4.19 release verification), combined G14–G15 run and separate-process M1–M4 exit codes not completed ::"),
# ---- W1–W3 ----
("W1", "§1 one-block burst",
 "(it is $P_5$ restricted to the ray, §6.14); earlier statements omitting it are superseded. Coefficient",
 "(it is $P_5$ restricted to the ray, §6.14). Coefficient"),
("W2", "§6.5 half-power term",
 "(§6.14); the earlier form without it is superseded. The $Q_0^3$ coefficient",
 "(§6.14). The $Q_0^3$ coefficient"),
("W3", "tag tables: §6.13 heading",
 "keeps its former heading tag.", "keeps its `[ENG]` heading tag."),
# ---- H4 ----
("H4a", "§1 OPEN 13 entry",
 "exact recomputation `dyad_h4_archival_exact_check.py`, v6.4.21)",
 "exact recomputation `dyad_h4_archival_exact_check.py`, v6.4.21; second route `dyad_h4_real_route_check.py`, exact rational $T^6$ in the real chart, v6.4.22)"),
("H4b", "§8 DYAD-ART-NORM-P6",
 "its $h_4$ closed forms are confirmed exactly by `dyad_h4_archival_exact_check.py`)",
 "its $h_4$ closed forms are confirmed exactly by `dyad_h4_archival_exact_check.py` and, by a second route (exact rational $T^6$ in the real chart), by `dyad_h4_real_route_check.py`, SHA-256 `" + H4R + "`)"),
("H4c", "Appendix E.1 LIEGAUGE-NORM row",
 "| `normalize_p6_liegauge_exact.py` (DYAD-ART-NORM-P6, `[ENG]`, 120 dps) | not recorded | mpmath, tolerance-pruned |",
 "| `normalize_p6_liegauge_exact.py` (DYAD-ART-NORM-P6, `[ENG]`, 120 dps); $h_4$ field: `dyad_h4_archival_exact_check.py`, `dyad_h4_real_route_check.py` (exact) | not recorded | mpmath, tolerance-pruned; sympy and exact rationals for $h_4$ |"),
("H4d", "Appendix E.2 LIEGAUGE-NORM row",
 "| `DYAD-ALG-LIEGAUGE-NORM` | historical | not recorded | not recorded | not recorded | gauge-universal form OPEN |",
 "| `DYAD-ALG-LIEGAUGE-NORM` | historical; $h_4$ closed forms recomputed exactly (v6.4.21; second route v6.4.22) | not recorded | not recorded | second route: different composition engine and chart, same definitions | gauge-universal form OPEN |"),
# ---- F4: R11 owner labels, one by one ----
("F4-01", "§1 P0-DYADIC entry (OPEN-M)", "The R11 cascade-gate arithmetic conversion is `[ALG]`;", "The OPEN-M R11 cascade-gate arithmetic conversion is `[ALG]`;"),
("F4-02", "§1 P0-DYADIC entry (OPEN-M)", "`[scope: conditional]`: R11 treats $h$ as an external amplitude (Audit-1 = OPEN-M v0.7.1 R16,", "`[scope: conditional]`: OPEN-M R11 treats $h$ as an external amplitude (Audit-1 = OPEN-M v0.7.1 R16,"),
("F4-03", "§3 SG-15 (OPEN-M)", "However R11 treats $h$ as an external amplitude parameter", "However OPEN-M R11 treats $h$ as an external amplitude parameter"),
("F4-04", "§3 SG-19 violation (RECOG)", "into the conjugacy chart without the R11 reconciliation;", "into the conjugacy chart without the RECOG R11 reconciliation (final-chart ledger);"),
("F4-05", "§5 cascade-gate row (OPEN-M)", "| R11 cascade gate $4/125$ |", "| OPEN-M R11 cascade gate $4/125$ |"),
("F4-06", "§6.2 angular optimum (OPEN-M)", "$\\theta_f=2\\pi/3$ (R11 `[ALG]`) equals the face flux", "$\\theta_f=2\\pi/3$ (OPEN-M R11 `[ALG]`) equals the face flux"),
("F4-07", "§6.11 face-flux entry (OPEN-M)", "(Pre-Legacy §1.8). The R11 cascade-gate conversion is `[ALG]`: at", "(Pre-Legacy §1.8). The OPEN-M R11 cascade-gate conversion is `[ALG]`: at"),
("F4-08", "§6.11 h-transfer (OPEN-M)", "**h-transfer:** R11 treats $h$ as an external amplitude (Audit-1:", "**h-transfer:** OPEN-M R11 treats $h$ as an external amplitude (Audit-1:"),
("F4-09", "§6.11 SU(2) factor (OPEN-M)", "or not at all is undetermined by R11 and blocked", "or not at all is undetermined by OPEN-M R11 and blocked"),
("F4-10", "§6.12 calibration route (OPEN-M)", "via the R11 factor $3/4$ at $\\theta_f=2\\pi/3$;", "via the OPEN-M R11 factor $3/4$ at $\\theta_f=2\\pi/3$;"),
("F4-11", "§6.12 calibration route (OPEN-M)", "status. R11's source formula $|H|_B=hr^2$", "status. OPEN-M R11's source formula $|H|_B=hr^2$"),
("F4-12", "§6.12 calibration route (OPEN-M)", "source scaling, which R11 does not fix", "source scaling, which OPEN-M R11 does not fix"),
("F4-13", "§6.14 boundaries (RECOG)", "R10 acceptance and R11 final-chart ledger (amplitude,", "R10 acceptance and RECOG R11 final-chart ledger (amplitude,"),
("F4-14", "§6.14 boundaries (RECOG)", "R10 delivered/accepted, R11 chart ledger (RECOG v0.3.20;", "R10 delivered/accepted, RECOG R11 chart ledger (RECOG v0.3.20;"),
("F4-15", "§7 RECOG consumer line (RECOG)", "Consumer outcomes at RECOG grades: R11 CLOSED,", "Consumer outcomes at RECOG grades: RECOG R11 CLOSED,"),
("F4-16", "Appendix E.1 P0-DYADIC row (OPEN-M)", "face-flux identity and R11 factor $3/4$ under", "face-flux identity and OPEN-M R11 factor $3/4$ under"),
("F4-17", "Appendix C: R11 row",
 "| $r$, $r_m$ | polar radius $z=re^{i\\Theta}$; L-PHASE remainder $r_m$ | §6.14 | — |\n",
 "| $r$, $r_m$ | polar radius $z=re^{i\\Theta}$; L-PHASE remainder $r_m$ | §6.14 | — |\n"
 "| R11 | (i) RECOG OPEN R11 (`RECOG-OPEN-QUINTIC-FRAME`), the final-chart ledger, CLOSED (RECOG v0.3.2); (ii) OPEN-M R11, the OPEN-M-2B assembly formulas: cascade-gate conversion, source/stiffness maps, angular optimum $\\theta_f=2\\pi/3$ (OPEN-M v0.7.1) | (i) §1, SG-19, §6.5, §6.9, §6.14, §7; (ii) §1, SG-15, §5, §6.2, §6.11, §6.12, Appendix E | always written with its owner: \"RECOG R11\" or \"OPEN-M R11\" |\n"),
]

APPA_ANCHOR = "### v6.4.21 — 22 October 2026 — Adopted\n"
APPA_ENTRY = (
 "### v6.4.22 — 23 October 2026 — DRAFT candidate\n\n"
 "- **Errata [status/wording] (owner review of v6.4.21, F1–F3, F5):** §7.0 Dyadic row names this edition and its predecessor; the notice-table and Appendix F intros state that N16–N21 are prepared and not sent; the P2B provenance replay status is stated at its recorded level (§6.14, §8).\n"
 "- **Labels [notation] (F4):** every live \"R11\" names its owner — RECOG R11 (final-chart ledger, CLOSED) or OPEN-M R11 (cascade-gate/assembly formulas); Appendix C row.\n"
 "- **Wording:** two \"superseded\" sentences removed (§1 one-block burst, §6.5); §6.13 heading-tag sentence.\n"
 "- **Evidence:** second-route exact check of the archival $h_4$ coefficients, `evidence/dyad/scripts/dyad_h4_real_route_check.py` (§1, §8, Appendix E).\n"
 "- No RID, grade, statement or OPEN status changed. Release record `" + REC + "`; predecessor tag `dyad-v6.4.21`.\n\n")


def main(base, out, log):
    raw = open(base, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, "base is not adopted v6.4.21"
    s = raw.decode("utf-8")
    i = s.index("## Appendix A — Version History"); j = s.index("## Appendix B —")
    appA = s[i:j]; MARK = "\x00APPENDIX-A\x00"; s = s[:i] + MARK + s[j:]
    record = []
    for k, loc, old, new in EDITS:
        n = s.count(old)
        assert n == 1, f"{k}: expected 1 match, found {n}"
        s = s.replace(old, new)
        record.append({"key": k, "location": loc, "old": old, "new": new,
                       "old_sha256": hashlib.sha256(old.encode()).hexdigest(), "new_sha256": hashlib.sha256(new.encode()).hexdigest()})
    assert appA.count(APPA_ANCHOR) == 1
    appA = appA.replace(APPA_ANCHOR, APPA_ENTRY + APPA_ANCHOR)
    record.append({"key": "ED-8", "location": "Appendix A entry", "old": "", "new": APPA_ENTRY,
                   "old_sha256": None, "new_sha256": hashlib.sha256(APPA_ENTRY.encode()).hexdigest()})
    s = s.replace(MARK, appA)
    data = s.encode("utf-8")
    open(out, "wb").write(data)
    with open(log, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"base_sha256": BASE_SHA, "out_sha256": hashlib.sha256(data).hexdigest(), "edits": record}, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(hashlib.sha256(data).hexdigest(), len(record), "edits", len(data), "bytes")


if __name__ == "__main__":
    main(*sys.argv[1:4])
