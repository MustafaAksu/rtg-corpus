#!/usr/bin/env python3
"""Negative controls for the `move` operation of tools/check_compaction.py (RECOG v0.3.24 stage 2).

    python -I evidence/recog/scripts/test_check_compaction_move.py BASE CANDIDATE MAP [--report OUT.json]

The real triple must PASS; each mutated triple must FAIL. The controls attack the move operation itself:
a word changed inside the moved block, a block moved into another section, into the header, a duplicated
block, a block deleted under cover of a move, an anchor that splits a paragraph, an anchor that is not
unique, a declared block that differs from the base by one byte, a second undeclared reorder, and a move
whose class is not reorder. Run from the repository root.
"""
import argparse, copy, json, os, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import test_check_compaction as T  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("candidate"); ap.add_argument("map"); ap.add_argument("--report")
    a = ap.parse_args()
    base = open(a.base, encoding="utf-8").read(); cand = open(a.candidate, encoding="utf-8").read()
    mp = json.load(open(a.map, encoding="utf-8"))
    mv = [o for o in mp["operations"] if o["op"] == "move"][0]
    blk, anchor = mv["block"], mv["before"]
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        rc, f = T.run(base, cand, mp, tmp, "P0")
        out.append({"id": "P0", "what": "unmutated inputs", "expect": "PASS", "got": "PASS" if rc == 0 else "FAIL", "fails": f})

        def control(cid, what, mutate):
            res = mutate()
            if res is None:
                out.append({"id": cid, "what": what, "expect": "FAIL", "got": "NOT APPLICABLE", "fails": []}); return
            b2, c2, m2 = res
            rc, f = T.run(b2, c2, m2, tmp, cid)
            out.append({"id": cid, "what": what, "expect": "FAIL", "got": "FAIL" if rc != 0 else "PASS", "fails": f})

        def move_to(c, b, before):
            """candidate with block b (once in c) cut and reinserted before `before`."""
            i = c.index(b); c2 = c[:i] + c[i + len(b) + 2:]; j = c2.index(before)
            return c2[:j] + b + "\n\n" + c2[j:]

        # N1: a word changed inside the moved block (candidate only)
        def n1():
            w = "linear eigenframe"
            if w not in blk: return None
            return base, cand.replace(blk, blk.replace(w, "linear frame", 1), 1), mp
        control("N1", "word changed inside the moved block (candidate)", n1)
        # N2: the same word changed in both the candidate and the declared block (map lies with the candidate)
        def n2():
            w = "linear eigenframe"
            m2 = copy.deepcopy(mp); nb = blk.replace(w, "linear frame", 1)
            m2["operations"][0]["block"] = nb
            return base, cand.replace(blk, nb, 1), m2
        control("N2", "word changed inside the block, declared block changed to match", n2)
        # N3: block moved into another section (before §4 heading) and declared so
        def n3():
            tgt = "| Layer | Canonical objects | Owner | Bridge required for |"
            if cand.count(tgt) != 1: return None
            c2 = move_to(cand, blk, tgt); m2 = copy.deepcopy(mp); m2["operations"][0]["before"] = tgt
            return base, c2, m2
        control("N3", "block moved into another section (declared)", n3)
        # N4: block moved into the header (declared)
        def n4():
            tgt = "**Status summary:**"
            if tgt not in cand: return None
            c2 = move_to(cand, blk, tgt); m2 = copy.deepcopy(mp); m2["operations"][0]["before"] = tgt
            return base, c2, m2
        control("N4", "block moved into the header (declared)", n4)
        # N5: block duplicated (kept at the old place and inserted at the new one)
        def n5():
            j = base.index(anchor); c2 = base[:j] + blk + "\n\n" + base[j:]
            return base, c2, mp
        control("N5", "block duplicated instead of moved", n5)
        # N6: block deleted under cover of a declared move
        def n6():
            i = base.index(blk); c2 = base[:i] + base[i + len(blk) + 2:]
            return base, c2, mp
        control("N6", "block deleted, move declared", n6)
        # N7: anchor inside a paragraph (splits a block)
        def n7():
            tgt = "Three operations are all historically called"
            if tgt not in cand: return None
            c2 = move_to(cand, blk, tgt); m2 = copy.deepcopy(mp); m2["operations"][0]["before"] = tgt
            return base, c2, m2
        control("N7", "anchor splits a paragraph (declared)", n7)
        # N8: anchor not unique
        def n8():
            tgt = "Violation:"
            if base.count(tgt) < 2: return None
            m2 = copy.deepcopy(mp); m2["operations"][0]["before"] = tgt
            return base, cand, m2
        control("N8", "anchor occurs more than once", n8)
        # N9: declared block differs from the base by one byte
        def n9():
            m2 = copy.deepcopy(mp); m2["operations"][0]["block"] = blk[:-1] + ("." if blk[-1] != "." else ";")
            return base, cand, m2
        control("N9", "declared block is not the base block (one byte)", n9)
        # N10: a second, undeclared reorder (SG-R5 moved before SG-R4)
        def n10():
            i = cand.index("**[SG-R5]**"); j = cand.index("\n\n", i); b5 = cand[i:j]
            if cand.count(b5) != 1 or "**[SG-R4]**" not in cand: return None
            return base, move_to(cand, b5, "**[SG-R4]**"), mp
        control("N10", "second reorder not declared", n10)
        # N11: move declared with a class other than reorder
        def n11():
            m2 = copy.deepcopy(mp); m2["operations"][0]["class"] = "history-section"
            return base, cand, m2
        control("N11", "move declared with class history-section", n11)
        # N12: a tag changed elsewhere in the live text, outside the move
        def n12():
            pat = "`[ALG]` [RID: RECOG-ALG-QUADRATURE-TYPING]"
            if pat not in cand: return None
            return base, cand.replace(pat, "`[THM]` [RID: RECOG-ALG-QUADRATURE-TYPING]", 1), mp
        control("N12", "grade changed outside the move", n12)

    ok = out[0]["got"] == "PASS" and all(o["got"] == "FAIL" for o in out[1:])
    for o in out:
        flag = "ok " if (o["expect"] == o["got"]) else "BAD"
        print(f"{flag} {o['id']:<4} expect {o['expect']} got {o['got']:<14} {o['what']}")
        for f in o["fails"][:3]:
            print("         " + f[:150])
    n = sum(1 for o in out[1:] if o["got"] == "FAIL")
    print(f"RESULT: {'PASS' if ok else 'FAIL'} ({n}/{len(out)-1} controls rejected)")
    if a.report:
        json.dump({"controls": out, "result": "PASS" if ok else "FAIL"}, open(a.report, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
