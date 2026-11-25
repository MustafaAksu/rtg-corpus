#!/usr/bin/env python3
"""Self-contained controls for two tools/check_compaction.py rules added after OFN v0.11 stage 2:
(1) the RID pattern tracks the programme namespaces `RTG-…` / `RTG-OFN-…` (Methodology v1.4 §4.2);
(2) profile key history_appendix: the version history may sit in an appendix other than A (OFN: C);
(3) revision after the PR #113 receiving review (PR #114): the history region is unique and replaced
exactly by one operation; hashes leave the live text only by declared relocation (relocate_hashes).

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


def ops(base_path, appendix_new, removals, relocate=True):
    o = [{"id": f"E{i+1}", "op": "edit", "class": "history-removal", "archive": ["base"], "old": r, "new": ""}
         for i, r in enumerate(removals)]
    for op in o:
        if relocate and DRAFT in op["old"]:
            op["relocate_hashes"] = [DRAFT]
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
            j = s.index(op["end"], i + len(op["start"])) if op.get("end") else len(s)
            s = s[:i] + op["new"] + s[j:]
    return s


def run(tmp, name, profile, appendix_new, removals, base=None, relocate=True, op_list=None):
    base = base or base_text()
    bp = os.path.join(tmp, "base.md")
    open(bp, "w", encoding="utf-8").write(base)
    op_list = op_list or ops(bp, appendix_new, removals, relocate)
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
    # cases carried over from the PR #113 receiving review (PR #114, ChatGPT), with the same intent
    H64PARA = f"The proof source uses `{H64}`; historical provenance is audited.\n\n"
    dup_base = base_text().replace(DRAFTP, DRAFTP + H64PARA).replace("an old scenario", f"an old scenario\n\nhistorical duplicate `{H64}`")
    ext_base = base_text().replace("\n---\n\n*END", "\n## Appendix D — Live theorem\n\n`[THM]` [RID: DYAD-THM-PRIM-CTR] A live theorem.\n\n---\n\n*END")
    extra = [
        ("N7", "FAIL", "candidate renames the history appendix (C -> D); phantom in it", C, new_appendix(" `DYAD-THM-PHANTOM`.").replace("## Appendix C —", "## Appendix D —"), [DRAFTP], {}),
        ("N8", "FAIL", "history replacement injects a new live section with a theorem", C, new_appendix().replace("\n---\n\n*END", "\n## 9. Added\n\n`[THM]` [RID: DYAD-THM-PHANTOM] New.\n\n---\n\n*END"), [DRAFTP], {}),
        ("N9", "FAIL", "history replacement to end of file deletes a following live appendix", C, new_appendix(), [DRAFTP], {"base": ext_base}),
        ("N10", "FAIL", "a second Appendix C heading in the candidate", C, new_appendix().replace("\n---\n\n*END", "\n## Appendix C — Second history\n\n`DYAD-THM-PHANTOM`.\n\n---\n\n*END"), [DRAFTP], {}),
        ("N11", "FAIL", "single-character programme RID description in the history entry", C, new_appendix(" `RTG-OPEN-X`."), [DRAFTP], {}),
        ("N12", "FAIL", "default profile: a live source hash deleted; a copy already in history must not mask it", D, None, None,
         {"base": dup_base, "op_list": [{"id": "DROP", "op": "edit", "class": "history-removal", "archive": ["base"], "old": H64PARA, "new": ""}]}),
        ("N13", "FAIL", "history_appendix C: hash relocated without a declaration", C, new_appendix(), [DRAFTP], {"relocate": False}),
        ("N14", "FAIL", "history_appendix C: a declared relocation whose hash is not in the history text", C, new_appendix().replace(f"; draft `{DRAFT}`", ""), [DRAFTP], {}),
    ]
    # round-2 receiving review (PR #114, ChatGPT): source and target binding of relocate_hashes
    hist_base = base_text().replace("Many words of history.", f"Many words of history; draft `{DRAFT}`.")
    t_decl = ops(None, new_appendix(), [DRAFTP], relocate=False)
    t_decl[-1]["relocate_hashes"] = [DRAFT]
    foot = new_appendix().replace(f"; draft `{DRAFT}`", "").replace("*END OF DOCUMENT — RTG_TEST_DSN_v0.2*", f"*END OF DOCUMENT — RTG_TEST_DSN_v0.2 (draft `{DRAFT}`)*")
    extra += [
        ("N15", "FAIL", "relocation declared on the history-appendix operation (old and new both carry the hash) authorizes an undeclared live deletion", C, None, None, {"base": hist_base, "op_list": t_decl}),
        ("N16", "FAIL", "a declared relocation whose only target is the footer line", C, foot, [DRAFTP], {}),
    ]
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for cid, want, what, prof, app, rem, *kw in cases + extra:
            code, fails, out = run(tmp, cid, prof, app, rem, **(kw[0] if kw else {}))
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
