#!/usr/bin/env python3
"""Checker for RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r3.md (exit 0 iff all gates pass; --neg runs negative controls).

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
G8 grade-tag census: the only anchor-tag changes are the declared ones (2 RESULT -> 3 single-RID DEF imports; +3 DEF, +1 OPEN, +1 GUARD,
   +1 COR anchors; +1 NUM anchor = the artifact-role label of the new §9.2 sampling row, as in existing
   registry rows)
G10 claim-level import discipline: no [import: ...] carries more than one RID
G11 receipt-replay provenance: replay record, certificate, helpers, JSON and interface record pinned in §9.2
G9 grade-qualifier preservation: outside the declared §1.1 re-types, no '[from: X]' / [THM] / [ALG] qualifier is
   added, removed or changed by any edit
G12 r2 -> r3 delta confinement: the r3 edit list equals the reviewed r2 edit list (r2 draft 423cd719…7b78) except the
   declared fact-sync edits E01-E05, E16, E27-E30; for those the base anchor ('old') is unchanged; and every r2 -> r3
   changed line lies inside one of their spans
G13 fact-sync content: the L-PHASE OPEN sub-item names DYAD-THM-LPHASE-ROWA-REMAINDER and Dyadic v6.4.19 and no longer
   says 'owner adoption pending'; N15 receipt row present; RECOG v0.3.22 (0dcce9e4…) and RRF v0.8.4 (2fb0a0fe…) rows present;
   no live import pin names Dyadic v6.4.19 (pins stay at v6.4.18 in this edition)
"""
import hashlib, json, re, subprocess, sys, importlib.util

BASE = "RTG_NUMBER_GENESIS_DSN_v1_20_7.md"; BASE_SHA = "c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28"
DRAFT = "RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r3.md"
R2 = "RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r2.md"; R2_SHA = "423cd7198c75ab7f39d3e1608c5e3bb85c0230dee795d13e03915dc0d4857b78"
FACT = {"E01", "E02", "E03", "E04", "E05", "E16", "E27", "E28", "E29", "E30"}
import difflib
NEW_NG = {"NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT", "NUMGEN-DEF-N5AS1-DEFECT", "NUMGEN-RESULT-N5AS1-L-BACKBONE",
          "NUMGEN-RESULT-N5AS1-L-MONO", "NUMGEN-RESULT-N5AS1-L-PHASE", "NUMGEN-RESULT-N5AS1-INF1"}
NEW_OFN = {"RTG-OFN-DEF-RELATIONAL-CONTENT", "RTG-OFN-DEF-PHASE-GAUGE", "RTG-OFN-DEF-BACKGROUND-TIME"}
sha = lambda b: hashlib.sha256(b).hexdigest()

spec = importlib.util.spec_from_file_location("fp", "ng_state_fingerprint_v2_3.py"); fp = importlib.util.module_from_spec(spec)
sys.argv_saved = sys.argv; sys.argv = ["fp"]; spec.loader.exec_module(fp); sys.argv = sys.argv_saved

def run(base_text, draft_text, edits, r2_text=None, r2_edits=None):
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
    g["G8"] = diff == {"RESULT": -2, "DEF": 6, "OPEN": 1, "GUARD": 1, "COR v1.20.8": 1, "NUM": 1}
    # G9 grade qualifiers: outside the two declared §1.1 re-types (E06, E07), every edit preserves the multiset
    # of '[from: X]' qualifiers and of '[THM]'/'[ALG]' tags of the text it replaces, and adds none
    q = re.compile(r"\[from: [^\]]+\]|\[(?:THM|ALG)\]")
    g["G9"] = all(sorted(q.findall(e["old"])) == sorted(q.findall(e["new"])) for e in edits if e["id"] not in ("E06", "E07"))
    # G10 claim-level import discipline: every [import: ...] in the draft carries at most one RID
    g["G10"] = all(";" not in m for m in re.findall(r"\[import: [^\]]*\|([^\]]*)\]", draft_text))
    # G11 receipt-replay provenance: the replay record and every execution pin appear in the §9.2 registry
    pins = ["71bfc4c597b4be502129a6d0da0b1c987723979eec1701b9c1b4187140c4b66f", "117484ae1a2509b6f6065d395840bfdfe2b0c977af0505f9fe6de68c13959cdb",
            "3a913062c1cdc6d151a2fb5b2f76d5354a367d1fa55df43f1f31d06e1b94cce8", "f007d42cde36d2a70115b9db25f47b107c446735fa31c66664f620c3247a5609",
            "8697c6970bd908327c66ef2ce3b2d38386947899033ef7f720bc096c4c3ad4fa", "7a91c223691b3705c2560fca452e671442939452e11cf98820512b182f46f78f"]
    reg = draft_text[draft_text.find("### §9.2"):draft_text.find("## Appendix A")]
    g["G11"] = all(p in reg for p in pins)
    # G12 delta confinement against the reviewed r2
    if r2_text is not None:
        e2 = {e["id"]: e for e in r2_edits}; e3 = {e["id"]: e for e in edits}
        same_ids = list(e2) == list(e3)
        unchanged = all(e3[i] == e2[i] for i in e3 if i not in FACT)
        anchors = all(e3[i]["old"] == e2[i]["old"] for i in FACT)
        sp = []
        for i in FACT:
            k = draft_text.find(e3[i]["new"]); s = draft_text.count("\n", 0, k); sp.append((s, s + e3[i]["new"].count("\n")))
        a, b = r2_text.split("\n"), draft_text.split("\n")
        hunks = [op for op in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op[0] != "equal"]
        conf = all(any(lo <= j <= hi for lo, hi in sp) for op in hunks for j in (range(op[3], op[4]) if op[4] > op[3] else [op[3]]))
        g["G12"] = same_ids and unchanged and anchors and conf and sha(r2_text.encode()) == R2_SHA
    # G13 fact-sync content
    sub = [l for l in draft_text.split("\n") if l.startswith("`[OPEN]` `[target: THM]` `[v1.20.8]` **L-PHASE explicit constant")]
    pins = re.findall(r"\[import: [^\]]*\]", draft_text)
    g["G13"] = (len(sub) == 1 and "DYAD-THM-LPHASE-ROWA-REMAINDER" in sub[0] and "v6.4.19" in sub[0]
                and "owner adoption pending" not in sub[0]
                and "| N15 — `DYAD-THM-LPHASE-ROWA-REMAINDER` |" in draft_text
                and "`RECOG v0.3.22` (adopted 20 Oct 2026, `0dcce9e4…bcd9`" in draft_text
                and "`RTG_RRF_REPRESENTATION_REGISTRY_v0.8.4` (adopted working standard, 20 Oct 2026, `2fb0a0fe…afce`" in draft_text
                and not any("v6.4.19" in p for p in pins))
    info = {"lost_blocks": len(lost), "new_blocks": len(new), "tag_delta": diff,
            "explicit_rids": [len(eb), len(ed)], "added_rids": sorted(added)}
    return g, info

if __name__ == "__main__":
    base = open(BASE, encoding="utf-8").read(); draft = open(DRAFT, encoding="utf-8").read()
    edits = json.load(open("v1_20_8_r3_edits.json", encoding="utf-8"))
    r2 = open(R2, encoding="utf-8").read(); r2e = json.load(open("v1_20_8_r2_edits.json", encoding="utf-8"))
    h1 = sha(draft.encode())
    subprocess.run([sys.executable, "build_v1_20_8_r3.py"], check=True, capture_output=True)
    g2 = sha(open(DRAFT, "rb").read()) == h1
    g, info = run(base, draft, edits, r2, r2e); g = {"G2": g2, **g}
    print(json.dumps({"draft_sha256": h1, "gates": g, "info": info}, indent=1, sort_keys=True))
    ok = all(g.values())
    if "--neg" in sys.argv:
        negs = {}
        bad = draft.replace("only through the entry-phase shift", "only through the entry phase shift"); negs["N1 unaccounted edit"] = all(run(base, bad, edits)[0].values())
        bad = draft.replace("[RID: NUMGEN-RESULT-N5AS1-L-MONO] ", ""); e2 = [dict(e, new=e["new"].replace("[RID: NUMGEN-RESULT-N5AS1-L-MONO] ", "")) for e in edits]; negs["N2 RID dropped"] = all(run(base, bad, e2)[0].values())
        bad = draft.replace("No constant is entered in this edition", "C = 403/250 is entered in this edition"); e3 = [dict(e, new=e["new"].replace("No constant is entered in this edition", "C = 403/250 is entered in this edition")) for e in edits]; assert bad != draft; negs["N3 constant imported"] = all(run(base, bad, e3)[0].values())
        bad = draft.replace("[RID: NUMGEN-RESULT-N5AS1-INF1]", "[RID: NUMGEN-RESULT-N5AS1-INF1] [RID: NUMGEN-RESULT-N5AS1-INF2]"); e4 = [dict(e, new=e["new"].replace("[RID: NUMGEN-RESULT-N5AS1-INF1]", "[RID: NUMGEN-RESULT-N5AS1-INF1] [RID: NUMGEN-RESULT-N5AS1-INF2]")) for e in edits]; negs["N4 extra RID"] = all(run(base, bad, e4)[0].values())
        bad = draft.replace("`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]", "`[RESULT] [from: THM]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]"); e5 = [dict(e, new=e["new"].replace("`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]", "`[RESULT] [from: THM]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]")) for e in edits]; negs["N5 regrade"] = all(run(base, bad, e5)[0].values())
        bad = draft.replace("RTG-OFN-DEF-RELATIONAL-CONTENT]` **Relational primacy.**", "RTG-OFN-DEF-RELATIONAL-CONTENT; RTG-OFN-DEF-PHASE-GAUGE]` **Relational primacy.**"); e6 = [dict(e, new=e["new"].replace("RTG-OFN-DEF-RELATIONAL-CONTENT]` **Relational primacy.**", "RTG-OFN-DEF-RELATIONAL-CONTENT; RTG-OFN-DEF-PHASE-GAUGE]` **Relational primacy.**")) for e in edits]; negs["N6 merged import"] = all(run(base, bad, e6)[0].values())
        bad = draft.replace("(`3a913062c1cdc6d151a2fb5b2f76d5354a367d1fa55df43f1f31d06e1b94cce8`)", "(pin omitted)"); e7 = [dict(e, new=e["new"].replace("(`3a913062c1cdc6d151a2fb5b2f76d5354a367d1fa55df43f1f31d06e1b94cce8`)", "(pin omitted)")) for e in edits]; negs["N7 helper pin missing"] = all(run(base, bad, e7)[0].values())
        e8 = [dict(e, new=e["new"].replace("v6.4.18 §6.11", "v6.4.19 §6.11")) if e["id"] == "E10" else e for e in edits]
        bad = draft.replace(next(e["new"] for e in edits if e["id"] == "E10"), next(e["new"] for e in e8 if e["id"] == "E10")); negs["N8 undeclared r2 edit changed"] = all(run(base, bad, e8, r2, r2e)[0].values())
        s9 = "Dyadic row-A theorem adopted upstream; NUMGEN import deferred."; t9 = "Dyadic row-A certificate, owner adoption pending."
        bad = draft.replace(s9, t9); e9 = [dict(e, new=e["new"].replace(s9, t9)) for e in edits]; negs["N9 stale L-PHASE sub-item"] = all(run(base, bad, e9, r2, r2e)[0].values())
        bad = draft.replace("| N15 — `DYAD-THM-LPHASE-ROWA-REMAINDER` |", "| N15 — (row removed) |"); e10 = [dict(e, new=e["new"].replace("| N15 — `DYAD-THM-LPHASE-ROWA-REMAINDER` |", "| N15 — (row removed) |")) for e in edits]; negs["N10 N15 receipt missing"] = all(run(base, bad, e10, r2, r2e)[0].values())
        print(json.dumps({"negative_controls_pass_should_be_false": negs}, indent=1))
        ok = ok and not any(negs.values())
    print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
