#!/usr/bin/env python3
"""RECOG v0.3.24, stage 2: layout-only compaction of the reviewed stage-1 intermediate (round 2).

One operation: the scope guard SG-R12 is moved from after SG-R14 to its numerical place before SG-R13
(§3), byte-identical, with tools/check_compaction.py's `move` operation (class reorder; added for this
stage). No claim, grade, qualifier, RID, OPEN status, evidence pointer or header field changes; the
header identity lines and the Appendix A DRAFT entry stay as in stage 1 (the release script sets them
at adoption, as for v0.3.23).

usage: build_recog_v0_3_24_stage2.py BASE OUT MAP_JSON
  BASE = the stage-1 round-2 intermediate (SHA-256 881be125…e03c; commit e42c81c)
"""
import hashlib, json, sys

BASE_SHA = "881be125201180b987e1f430390507c10f4167df29c19c0b19fbd07eb6dee03c"
STAGE1_COMMIT = "e42c81c"

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()

def main(argv):
    base_p, out_p, map_p = argv[1:4]
    raw = open(base_p, "rb").read()
    assert sha(raw) == BASE_SHA, "base is not the reviewed stage-1 round-2 intermediate"
    s = raw.decode("utf-8")
    i = s.index("**[SG-R12]**")
    j = s.index("\n\n", i)
    block = s[i:j]
    assert s.count(block) == 1 and s[i - 2:i] == "\n\n"
    anchor = "**[SG-R13]**"
    assert s.count(anchor) == 1
    s2 = s[:i] + s[j + 2:]
    k = s2.index(anchor)
    assert s2[k - 2:k] == "\n\n"
    cand = s2[:k] + block + "\n\n" + s2[k:]
    data = cand.encode("utf-8")
    open(out_p, "wb").write(data)
    mp = {
        "study": "RECOG", "target": "v0.3.24", "stage": "compaction",
        "base": f"corrected intermediate (stage 1, round 2; commit {STAGE1_COMMIT})",
        "base_sha256": BASE_SHA, "candidate_sha256": sha(data),
        "archives": [],
        "archives_note": "nothing is removed or relocated by this stage, so no archive is named. The stage-1 history pointers to `recog-v0.3.23` were verified by the stage-1 checker (gate C22: every moved passage exists at that tag); the tag is listed in known_tags. Naming the tag as an archive here would make the checker read the version strings in those pointer sentences (v0.3.1, v0.3.2, v0.3.3: the era of the relocated specifications) as Appendix A entries, which the compact Appendix A of v0.3.23 does not carry.",
        "profile": {"study": "RECOG", "ref_words": ["template"], "history_words": [],
                    "checked_tag_prefixes": ["recog-", "numgen-", "methodology-", "gen-", "ofn-", "rrf-", "rer-"],
                    "known_tags": ["dyad-v6.4.19", "dyad-v6.4.20", "dyad-v6.4.21", "dyad-v6.4.22", "numgen-v1.20.8", "methodology-v1.3", "methodology-v1.4", "gen-v2.8.9", "ofn-v0.10", "rrf-v0.8.4", "rer-v0.2", "recog-v0.3.22", "recog-v0.3.23"],
                    "summary_from": ["header", "section1"]},
        "operations": [
            {"id": "M01", "op": "move", "class": "reorder", "block": block, "before": anchor,
             "what": "SG-R12 moved to its numerical place before SG-R13 (§3 Scope Guards); byte-identical",
             "why": "v0.3.23 release record §2a: 'the SG order (R13 and R14 before R12), because the checker has no move operation'"},
        ],
    }
    json.dump(mp, open(map_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(sha(data), "1 operation (move SG-R12 before SG-R13)", len(block), "chars")

if __name__ == "__main__":
    main(sys.argv)
