#!/usr/bin/env python3
"""Self-contained controls for two tools/check_compaction.py rules added after OFN v0.11 stage 2:
(1) the RID pattern tracks the programme namespaces `RTG-…` / `RTG-OFN-…` (Methodology v1.4 §4.2);
(2) profile key history_appendix: the version history may sit in an appendix other than A (OFN: C).

    python3 -I tools/test_check_compaction_profile.py

Builds a small synthetic DSN (header, live text naming RTG-OFN and DYAD identifiers and a draft hash,
Appendices A/B/C, footer), compacts it with declared operations, and runs the checker on positive and
mutated triples. Each mutation keeps the re-derivation exact (candidate and map changed together), so only
the targeted rule can reject it. Exit 0 only if every case gives its expected result.
"""
import hashlib, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKER = os.path.join(HERE, "check_compaction.py")
H64 = "a" * 64
DRAFT = "58e2dec5…3610"

HEADER = f"""# RTG_TEST_DSN_v0.2

**Title:** Test document
**Date:** 1 January 2026
**Scope:** test
**Document class:** test ledger
**Document status:** ADOPTED
**Supersedes:** `RTG_TEST_DSN_v0.1` (SHA-256 `{H64}`)
**Companion documents:** none
**DSN Methodology:** v1.4
**Status summary:** One test document.
"""

BETA = "Recorded in v0.9 (superseded): `RTG-OFN-DEF-BETA` was renamed.\n\n"
BARE = "In v0.9 the namespace `RTG-OFN` was named (superseded wording).\n\n"
DRAFTP = f"The superseded draft hash `{DRAFT}` of v0.9.\n\n"


def base_text():
    return (HEADER + "\n## 0. Purpose\n\n"
            "`[DEF]` [RID: RTG-OFN-DEF-ALPHA] Alpha is a defined thing.\n\n"
            "`[DEF]` [RID: RTG-OFN-DEF-BETA] Beta is a defined thing.\n\n"
            "The text cites `RTG-OFN-DEF-ALPHA` and `DYAD-THM-PRIM-CTR`.\n\n"
            + BETA + BARE + DRAFTP +
            "## Appendix A — Historical Scenarios\n\n```text\nan old scenario\n```\n\n"
            "## Appendix B — Retired Claims\n\nNone.\n\n"
            "## Appendix C — Version History\n\n### v0.2 — long entry\n\nMany words of history.\n\n"
            "### v0.1 — first\n\nMore history.\n\n---\n\n*END OF DOCUMENT — RTG_TEST_DSN_v0.2*\n")


def new_appendix(extra=""):
    return ("## Appendix C — Compact Version History\n\n"
            f"### v0.2 — compact; draft `{DRAFT}`; names `RTG-OFN-DEF-ALPHA`.{extra}\n\n"
            "### v0.1 — first.\n\n---\n\n*END OF DOCUMENT — RTG_TEST_DSN_v0.2*\n")


def ops(base_path, appendix_new, removals):
    o = [{"id": f"E{i+1}", "op": "edit", "class": "history-removal", "archive": ["base"], "old": r, "new": ""}
         for i, r in enumerate(removals)]
    o.append({"id": "T", "op": "replace-section", "class": "history-appendix", "archive": ["base"],
              "start": "## Appendix C — Version History\n", "end": None, "new": appendix_new})
    return o


def derive(base, op_list):
    s = base
    for op in op_list:
        if op["op"] == "edit":
            assert s.count(op["old"]) == 1, op["id"]
            s = s.replace(op["old"], op["new"])
        else:
            i = s.index(op["start"])
            s = s[:i] + op["new"]
    return s


def run(tmp, name, profile, appendix_new, removals):
    base = base_text()
    bp = os.path.join(tmp, "base.md")
    open(bp, "w", encoding="utf-8").write(base)
    op_list = ops(bp, appendix_new, removals)
    cand = derive(base, op_list)
    cp = os.path.join(tmp, name + ".md")
    open(cp, "w", encoding="utf-8").write(cand)
    sh = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()
    mp = {"base_sha256": sh(base), "candidate_sha256": sh(cand),
          "archives": [{"name": "base", "path": bp, "sha256": sh(base)}],
          "profile": profile, "operations": op_list}
    mpp = os.path.join(tmp, name + ".json")
    json.dump(mp, open(mpp, "w", encoding="utf-8"), ensure_ascii=False)
    r = subprocess.run([sys.executable, "-I", CHECKER, bp, cp, mpp], capture_output=True, text=True)
    return r.returncode, [l for l in r.stdout.splitlines() if l.startswith("FAIL")], r.stdout


def main():
    C = {"history_appendix": "C", "history_words": ["v0.9"]}
    D = {"history_words": ["v0.9"]}
    cases = [
        ("P1", "PASS", "history_appendix C: history paragraph and draft hash relocated", C, new_appendix(), [DRAFTP]),
        ("P2", "PASS", "bare namespace word `RTG-OFN` is not an identifier (removable as history)", C, new_appendix(), [DRAFTP, BARE]),
        ("P3", "PASS", "default profile (history in Appendix A) still accepts the same triple", D, new_appendix(), [DRAFTP]),
        ("N1", "FAIL", "history entry names an RTG-OFN identifier absent from the live text", C, new_appendix(" `RTG-OFN-DEF-PHANTOM`."), [DRAFTP]),
        ("N2", "FAIL", "history entry names a DYAD identifier absent from the live text", C, new_appendix(" `DYAD-THM-PHANTOM`."), [DRAFTP]),
        ("N3", "FAIL", "draft hash deleted, not relocated", C, new_appendix().replace(f"; draft `{DRAFT}`", ""), [DRAFTP]),
        ("N4", "FAIL", "history-appendix operation replaces an appendix other than the declared one", {**C, "history_appendix": "B"}, new_appendix(), [DRAFTP]),
        ("N5", "FAIL", "an RTG-OFN identifier removed as history (default profile)", D, new_appendix(), [DRAFTP, BETA]),
        ("N6", "FAIL", "an RTG-OFN identifier removed as history (history_appendix C)", C, new_appendix(), [DRAFTP, BETA]),
    ]
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for cid, want, what, prof, app, rem in cases:
            code, fails, out = run(tmp, cid, prof, app, rem)
            got = {0: "PASS", 1: "FAIL"}.get(code, f"EXIT{code}")
            ok = got == want
            bad += not ok
            print(f"{'ok ' if ok else 'BAD'} {cid:3s} expect {want} got {got:5s} {what}")
            for f in fails[:2]:
                print("         " + f[:200])
            if not ok and want == "PASS":
                print(out)
    print("RESULT:", "PASS" if not bad else f"FAIL ({bad} case(s))")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
