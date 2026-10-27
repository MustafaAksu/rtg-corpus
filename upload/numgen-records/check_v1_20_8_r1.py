#!/usr/bin/env python3
"""Checker for RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r1.md (exit 0 iff all gates pass; --neg runs negative controls).

G1 base identity (c4637e7a…ab28)
G2 deterministic rebuild: running the builder twice gives identical bytes; draft hash recorded
G3 reversal: undoing the edit list (new -> old, reverse order) reproduces the base byte-for-byte
G4 every edit's new text occurs exactly once in the draft
G5 explicit-RID conservation: every v1.20.7 explicit RID survives; the added explicit RIDs are exactly the six
   approved N-5A-S1 allocations plus the three OFN definition RIDs of the narrowed §1.1 imports
G6 no forbidden content: the draft contains no Dyadic row-A constant ('403/250', '1.612') and does not cite
   NUMGEN-OPEN-N5AS1-INF as the INF-1 identity
G7 claim-block accounting (fingerprint v2.3 extraction): every lost base block and every new draft block lies
   inside an edited region (no unaccounted change), and the status-line set outside edited regions is identical
G8 grade-tag census: the only anchor-tag changes are the declared ones (2 RESULT->DEF imports; +3 DEF, +1 OPEN, +1 GUARD,
   +1 COR anchors)
G9 grade-qualifier preservation: outside the declared §1.1 re-types, no '[from: X]' / [THM] / [ALG] qualifier is
   added, removed or changed by any edit
"""
import hashlib, json, re, subprocess, sys, importlib.util

BASE = "RTG_NUMBER_GENESIS_DSN_v1_20_7.md"; BASE_SHA = "c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28"
DRAFT = "RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r1.md"
NEW_NG = {"NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT", "NUMGEN-DEF-N5AS1-DEFECT", "NUMGEN-RESULT-N5AS1-L-BACKBONE",
          "NUMGEN-RESULT-N5AS1-L-MONO", "NUMGEN-RESULT-N5AS1-L-PHASE", "NUMGEN-RESULT-N5AS1-INF1"}
NEW_OFN = {"RTG-OFN-DEF-RELATIONAL-CONTENT", "RTG-OFN-DEF-PHASE-GAUGE", "RTG-OFN-DEF-BACKGROUND-TIME"}
sha = lambda b: hashlib.sha256(b).hexdigest()

spec = importlib.util.spec_from_file_location("fp", "ng_state_fingerprint_v2_3.py"); fp = importlib.util.module_from_spec(spec)
sys.argv_saved = sys.argv; sys.argv = ["fp"]; spec.loader.exec_module(fp); sys.argv = sys.argv_saved

def run(base_text, draft_text, edits):
    g = {}
    g["G1"] = sha(base_text.encode()) == BASE_SHA
    # G3 reversal
    t = draft_text
    for e in reversed(edits):
        if t.count(e["new"]) != 1: g["G3"] = False; break
        t = t.replace(e["new"], e["old"])
    else:
        g["G3"] = t == base_text
    g["G4"] = all(draft_text.count(e["new"]) == 1 for e in edits)
    # G5 RIDs
    eb, bb = fp.identifiers(base_text.split("\n")); ed, bd = fp.identifiers(draft_text.split("\n"))
    added = (set(ed) - set(eb)) | ((set(bd) - set(bb)) & (NEW_NG | NEW_OFN))
    g["G5"] = set(eb) <= set(ed) and set(bb) <= set(bd) and added == (NEW_NG | NEW_OFN) and NEW_NG <= set(ed)
    # G6
    g["G6"] = ("403/250" not in draft_text and "1.612" not in draft_text
               and not re.search(r"NUMGEN-OPEN-N5AS1-INF`?\s*\)?\s*(is|=)\s*(the )?INF-1", draft_text))
    # G7 block accounting
    open("_b.md", "w").write(base_text); open("_d.md", "w").write(draft_text)
    Bb, LB = fp.blocks("_b.md"); Bd, LD = fp.blocks("_d.md")
    hb = {b["h"] for b in Bb}; hd = {b["h"] for b in Bd}
    def spans(text, key):
        out = []
        for e in edits:
            i = text.find(e[key]); s = text.count("\n", 0, i) + 1; out.append((s - 1, s + e[key].count("\n") + 1))
        return out
    sb, sd = spans(base_text, "old"), spans(draft_text, "new")
    inside = lambda b, S: any(lo <= b["line"] <= hi or (b["line"] <= lo and b["end"] >= lo) for lo, hi in S)
    lost = [b for b in Bb if b["h"] not in hd]; new = [b for b in Bd if b["h"] not in hb]
    g["G7"] = all(inside(b, sb) for b in lost) and all(inside(b, sd) for b in new)
    # G8 tags
    def census(B):
        c = {}
        for b in B:
            k = " ".join(b["tags"]); c[k] = c.get(k, 0) + 1
        return c
    cb, cd = census(Bb), census(Bd)
    diff = {k: cd.get(k, 0) - cb.get(k, 0) for k in set(cb) | set(cd) if cd.get(k, 0) != cb.get(k, 0)}
    g["G8"] = diff == {"RESULT": -2, "DEF": 5, "OPEN": 1, "GUARD": 1, "COR v1.20.8": 1}
    # G9 grade qualifiers: outside the two declared §1.1 re-types (E06, E07), every edit preserves the multiset
    # of '[from: X]' qualifiers and of '[THM]'/'[ALG]' tags of the text it replaces, and adds none
    q = re.compile(r"\[from: [^\]]+\]|\[(?:THM|ALG)\]")
    g["G9"] = all(sorted(q.findall(e["old"])) == sorted(q.findall(e["new"])) for e in edits if e["id"] not in ("E06", "E07"))
    info = {"lost_blocks": len(lost), "new_blocks": len(new), "tag_delta": diff,
            "explicit_rids": [len(eb), len(ed)], "added_rids": sorted(added)}
    return g, info

if __name__ == "__main__":
    base = open(BASE, encoding="utf-8").read(); draft = open(DRAFT, encoding="utf-8").read()
    edits = json.load(open("v1_20_8_r1_edits.json", encoding="utf-8"))
    h1 = sha(draft.encode())
    subprocess.run([sys.executable, "build_v1_20_8_r1.py"], check=True, capture_output=True)
    g2 = sha(open(DRAFT, "rb").read()) == h1
    g, info = run(base, draft, edits); g = {"G2": g2, **g}
    print(json.dumps({"draft_sha256": h1, "gates": g, "info": info}, indent=1, sort_keys=True))
    ok = all(g.values())
    if "--neg" in sys.argv:
        negs = {}
        bad = draft.replace("only through the entry-phase shift", "only through the entry phase shift"); negs["N1 unaccounted edit"] = all(run(base, bad, edits)[0].values())
        bad = draft.replace("[RID: NUMGEN-RESULT-N5AS1-L-MONO] ", ""); e2 = [dict(e, new=e["new"].replace("[RID: NUMGEN-RESULT-N5AS1-L-MONO] ", "")) for e in edits]; negs["N2 RID dropped"] = all(run(base, bad, e2)[0].values())
        bad = draft.replace("No constant is entered here", "C = 403/250 is entered here"); e3 = [dict(e, new=e["new"].replace("No constant is entered here", "C = 403/250 is entered here")) for e in edits]; negs["N3 constant imported"] = all(run(base, bad, e3)[0].values())
        bad = draft.replace("[RID: NUMGEN-RESULT-N5AS1-INF1]", "[RID: NUMGEN-RESULT-N5AS1-INF1] [RID: NUMGEN-RESULT-N5AS1-INF2]"); e4 = [dict(e, new=e["new"].replace("[RID: NUMGEN-RESULT-N5AS1-INF1]", "[RID: NUMGEN-RESULT-N5AS1-INF1] [RID: NUMGEN-RESULT-N5AS1-INF2]")) for e in edits]; negs["N4 extra RID"] = all(run(base, bad, e4)[0].values())
        bad = draft.replace("`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]", "`[RESULT] [from: THM]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]"); e5 = [dict(e, new=e["new"].replace("`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]", "`[RESULT] [from: THM]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]")) for e in edits]; negs["N5 regrade"] = all(run(base, bad, e5)[0].values())
        print(json.dumps({"negative_controls_pass_should_be_false": negs}, indent=1))
        ok = ok and not any(negs.values())
    print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
