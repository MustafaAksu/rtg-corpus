#!/usr/bin/env python3
"""release_recog_v0_3_22.py -- deterministic adoption pass: RECOG v0.3.22 DRAFT r3 -> v0.3.22 (adopted).

Input : RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22_DRAFT_r3.md (sha256 8f496d3c...d959; independent delta review
        RECOG_v0_3_22_DRAFT_r3_DELTA_RECEIVING_REVIEW_20261020.md 2a65093b...fc96: READY FOR PI ADOPTION); refuses other bytes.
Output: RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22.md and recog_v0_3_22_release_edits.json.
PI adoption authorized 20 Oct 2026 in the RECOG co-owner conversation ("ADOPTION APPROVED -- PROCEED WITH CONTROLLED
RELEASE"). Scope of this pass: edition markers, adoption information, §8 provenance metadata. No scientific statement,
grade, domain, RID or evidence limit changes. Every edit is exact-once.
Usage: python release_recog_v0_3_22.py DRAFT_r3.md [OUT_DIR]
"""
import sys, os, json, hashlib

R3_SHA = "8f496d3c1fd0182e058e5fd814c5530e3952d5469b3ea932d3d3f27718fbd959"
E = []
def edit(eid, kind, old, new): E.append({"id": eid, "kind": kind, "old": old, "new": new})

edit("P1", "marker", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22 (DRAFT r3)\n", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22\n")
edit("P2", "marker",
 "**Date:** 20 October 2026 (v0.3.22 DRAFT r3 — A1a scientific cell: asymptotic phase and the Number Genesis constant $C_D$; not adopted)\n",
 "**Date:** 20 October 2026 (v0.3.22 — A1a scientific cell: asymptotic phase and the Number Genesis constant $C_D$; adopted 20 Oct 2026)\n")
edit("P3", "marker", "**Supersedes (on adoption):** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21`", "**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21`")
edit("P4", "adoption",
 "**Status summary (v0.3.22 DRAFT r3):** One new scientific cell, §6.13b (A1a), with eight proposed RIDs (registered only on adoption) and four artifact IDs (§8).",
 "**Status summary (v0.3.22):** One new scientific cell, §6.13b (A1a), with eight scientific RIDs and four artifact IDs (§8), all registered on adoption (20 Oct 2026).")
edit("P5", "adoption",
 "canonical repin of the two NUMGEN imports pending NUMGEN v1.20.8; PI adoption pending.",
 "canonical repin of the two NUMGEN imports pending NUMGEN v1.20.8; adopted by the PI 20 Oct 2026 on DRAFT r3 `8f496d3c…d959` after the independent delta review `2a65093b…fc96`.")
edit("P6", "marker",
 "**Freeze status:** v0.3.22 DRAFT r3 (not adopted; v0.3.21 remains the authoritative edition until adoption). *Earlier:* v0.3.21 adopted",
 "**Freeze status:** v0.3.22 adopted 20 Oct 2026 (PI authorization in the RECOG co-owner conversation, after the independent delta review `2a65093b…fc96` accepted DRAFT r3 `8f496d3c…d959`; release record `RECOG_v0_3_22_RELEASE_RECORD.md`); current authoritative edition, not frozen (a freeze is a separate decision). *Earlier:* v0.3.21 adopted")
edit("P7", "adoption",
 "**RIDs in this subsection are proposed and are registered only on adoption of this release.**",
 "**RIDs in this subsection were registered on adoption of v0.3.22 (20 Oct 2026).**")
edit("P8", "adoption",
 "| v0.3.22 draft: proposed use in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (§6.13b) at the v6.4.18 pin, R9 premise discharged by RECOG's own R9; takes effect only on adoption (v0.3.21 state: conditional receipt only) |",
 "| v0.3.22 (adopted 20 Oct 2026): used in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION (§6.13b) at the v6.4.18 pin, R9 premise discharged by RECOG's own R9; in effect from adoption (v0.3.21 state: conditional receipt only) |")
edit("P9", "provenance",
 "draft pending the string ruling — the final dispatched copy, same body with updated header, to be recorded on receipt);",
 "draft pending the string ruling); final reply `NUMGEN_REPLY_TO_RECOG_A1A_RID_REQUEST_20261020_v0_1_1.md` (`a2e7bf98fe08d2d64a883b8996c285ba4b67c94f73bb53548abe206f228b1902`; final for dispatch; body byte-identical to v0.1, header and title only) with addendum `RECOG_A1A_G1_DISPOSITION_ADDENDUM_FINAL_REPLY_20261020.md` (`582d931e0055964fccd541e9ba33defce65f57c6e1cb53385d0f1f155502ceae`);")
edit("P10", "provenance",
 "integrated receiving review of DRAFT r2 `RECOG_v0_3_22_DRAFT_r2_INDEPENDENT_RECEIVING_REVIEW_20261020.md` (`fee7e519f3e6cd8bf32aa2be0402bef667178148ea43c9fa8521159a1d500efe`);",
 "integrated receiving review of DRAFT r2 `RECOG_v0_3_22_DRAFT_r2_INDEPENDENT_RECEIVING_REVIEW_20261020.md` (`fee7e519f3e6cd8bf32aa2be0402bef667178148ea43c9fa8521159a1d500efe`); independent delta receiving review of DRAFT r3 `RECOG_v0_3_22_DRAFT_r3_DELTA_RECEIVING_REVIEW_20261020.md` (`2a65093baa6a07e57faa056ecd755cc8689f94c59d5f071996b31ebb5979fc96`);")
edit("P11", "adoption",
 "### v0.3.22 — DRAFT r3, 20 October 2026 (A1a scientific cell; not adopted)\n",
 "### v0.3.22 — 20 October 2026 (A1a scientific cell; adopted)\n"
 "- **Adoption:** DRAFT r3 (`8f496d3c…d959`) accepted by the independent delta review (`2a65093b…fc96`: release candidate ready for PI adoption decision); adopted by the PI 20 Oct 2026 (\"ADOPTION APPROVED — PROCEED WITH CONTROLLED RELEASE\"). The adoption pass changed edition markers, adoption information and §8 provenance metadata only: title, date, supersedes, status-summary label and release state, freeze status, the §6.13b registration sentence, the §7.2 N13 use field, the §8 governance row (final NUMGEN reply v0.1.1 and addendum; r3 delta review), this heading and line, footer. Registered on adoption: the eight scientific RIDs of §6.13b and the four artifact RIDs of §8. Carried open: canonical repin of the two NUMGEN imports after NUMGEN v1.20.8 adoption (separate RECOG revision); R6 ACTIVE; G3 notices to OFN, RRF and RER unsent.\n"
 "- *Draft history (r1–r3) follows.*\n")
edit("P12", "marker",
 "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22 (DRAFT r3; not adopted; v0.3.21 `a3459522…0ae3` remains authoritative until adoption)*",
 "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22*")

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    raw = open(sys.argv[1], "rb").read(); h = hashlib.sha256(raw).hexdigest()
    if h != R3_SHA: print(f"REFUSED: input sha256 {h} != {R3_SHA}"); sys.exit(2)
    out = sys.argv[2] if len(sys.argv) > 2 else "."
    t = raw.decode("utf-8")
    for e in E:
        n = t.count(e["old"])
        if n != 1: print(f"ABORT: {e['id']} anchor count {n}"); sys.exit(2)
        t = t.replace(e["old"], e["new"], 1)
    p = os.path.join(out, "RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22.md")
    open(p, "wb").write(t.encode("utf-8"))
    json.dump({"input_sha256": R3_SHA, "edits": E}, open(os.path.join(out, "recog_v0_3_22_release_edits.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"BUILT {p} sha256 {hashlib.sha256(t.encode('utf-8')).hexdigest()} ({len(E)} edits)")

if __name__ == "__main__": main()
