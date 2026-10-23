#!/usr/bin/env python3
"""release_recog_v0_3_21.py -- deterministic adoption pass: RECOG v0.3.21 DRAFT r2 -> v0.3.21 (adopted).

Input : RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21_DRAFT_r2.md (sha256 be164a9f...58c2, receiving review 9a7ae8aa...31c45
        ACCEPTED FOR ADOPTION); refuses any other bytes.
Output: RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md and recog_v0_3_21_release_edits.json.
Only edition markers change (title, date, supersedes, status-summary label, freeze status, Appendix A heading and
adoption line, footer). Every edit is exact-once. PI adoption authorized 20 Oct 2026 in the RECOG co-owner conversation.
Usage: python release_recog_v0_3_21.py DRAFT_r2.md [OUT_DIR]
"""
import sys, os, json, hashlib

R2_SHA = "be164a9f7dba3943e06d76e8a9448cb9b02d395f9ab18947498bdf3a8fef58c2"
E = []
def edit(eid, old, new): E.append({"id": eid, "old": old, "new": new})

edit("P1", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21 (DRAFT r2)\n",
           "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21\n")
edit("P2", "**Date:** 20 October 2026 (v0.3.21 DRAFT r2 — synchronization release, no new mathematics; not adopted)\n",
           "**Date:** 20 October 2026 (v0.3.21 — synchronization release, no new mathematics; adopted 20 Oct 2026)\n")
edit("P3", "**Supersedes (on adoption):** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20`",
           "**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20`")
edit("P4", "**Status summary (v0.3.21 DRAFT r2):**", "**Status summary (v0.3.21):**")
edit("P5", "**Freeze status:** v0.3.21 DRAFT r2 (not adopted).",
           "**Freeze status:** v0.3.21 adopted 20 Oct 2026 (PI authorization in the RECOG co-owner conversation, after the "
           "independent receiving review `9a7ae8aa…31c45` accepted DRAFT r2 `be164a9f…58c2`; release record "
           "`RECOG_v0_3_21_RELEASE_RECORD.md`); current authoritative edition, not frozen (a freeze is a separate decision).")
edit("P6", "### v0.3.21 — DRAFT r2, 20 October 2026 (owner synchronization; not adopted)\n",
           "### v0.3.21 — 20 October 2026 (owner synchronization; adopted)\n"
           "- **Adoption:** DRAFT r2 (`be164a9f…58c2`) accepted for adoption by the independent receiving review "
           "(`9a7ae8aa…31c45`); adopted by the PI 20 Oct 2026. The adoption pass changed edition markers only "
           "(title, date, supersedes, status-summary label, freeze status, this heading and line, footer).\n")
edit("P7", "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21 (DRAFT r2; not adopted; v0.3.20 frozen `fdb8c9a7…b8df` remains authoritative until adoption)*",
           "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21*")

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    raw = open(sys.argv[1], "rb").read(); h = hashlib.sha256(raw).hexdigest()
    if h != R2_SHA: print(f"REFUSED: input sha256 {h} != {R2_SHA}"); sys.exit(2)
    out = sys.argv[2] if len(sys.argv) > 2 else "."
    t = raw.decode("utf-8")
    for e in E:
        n = t.count(e["old"])
        if n != 1: print(f"ABORT: {e['id']} anchor count {n}"); sys.exit(2)
        t = t.replace(e["old"], e["new"], 1)
    p = os.path.join(out, "RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md")
    open(p, "wb").write(t.encode("utf-8"))
    json.dump({"input_sha256": R2_SHA, "edits": E}, open(os.path.join(out, "recog_v0_3_21_release_edits.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"BUILT {p} sha256 {hashlib.sha256(t.encode('utf-8')).hexdigest()} ({len(E)} edits)")

if __name__ == "__main__": main()
