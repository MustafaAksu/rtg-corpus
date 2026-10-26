#!/usr/bin/env python3
"""Release checker for RTG_NUMBER_GENESIS_DSN_v1_20_8.md (exit 0 iff all gates pass; --neg runs negative controls).

P0 input identity: DRAFT r3 = 9d59cfa1…e7b3; base v1.20.7 = c4637e7a…ab28 (unchanged)
P1 deterministic release: rerunning the transform gives identical bytes
P2 reversal: undoing the release edits gives r3 byte-exactly (no change outside the declared spans)
P3 each release edit's new text occurs exactly once
P4 claim-block census (fingerprint v2.3): status-tag multiset identical to r3
P5 RID sets (explicit and bare) identical to r3
P6 OPEN-tagged claim blocks identical to r3 (text hashes)
P7 no row-A constant ('403/250', '1.612')
P8 edition markers in adopted form: no 'DRAFT r3 — not adopted', no 'Supersedes on adoption'; title is the edition title
P9 INV-LIVE: 0 live hits
"""
import hashlib, json, subprocess, sys, importlib.util

R3 = "RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r3.md"; R3_SHA = "9d59cfa1edf15c4e263494c9fbc615dc915ed3b84e556df8ade61fd1fa7de7b3"
BASE = "RTG_NUMBER_GENESIS_DSN_v1_20_7.md"; BASE_SHA = "c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28"
OUT = "RTG_NUMBER_GENESIS_DSN_v1_20_8.md"
sha = lambda b: hashlib.sha256(b).hexdigest()
spec = importlib.util.spec_from_file_location("fp", "ng_state_fingerprint_v2_3.py"); fp = importlib.util.module_from_spec(spec)
_a = sys.argv; sys.argv = ["fp"]; spec.loader.exec_module(fp); sys.argv = _a

def run(r3, fin, edits):
    g = {}
    g["P0"] = sha(r3.encode()) == R3_SHA and sha(open(BASE, "rb").read()) == BASE_SHA
    t = fin
    for e in reversed(edits):
        if t.count(e["new"]) != 1: g["P2"] = False; break
        t = t.replace(e["new"], e["old"])
    else:
        g["P2"] = t == r3
    g["P3"] = all(fin.count(e["new"]) == 1 for e in edits)
    open("_r3.md", "w", encoding="utf-8").write(r3); open("_f.md", "w", encoding="utf-8").write(fin)
    Ba, _ = fp.blocks("_r3.md"); Bb, _ = fp.blocks("_f.md")
    cen = lambda B: sorted(" ".join(b["tags"]) for b in B)
    g["P4"] = cen(Ba) == cen(Bb)
    ea, ba = fp.identifiers(r3.split("\n")); eb, bb = fp.identifiers(fin.split("\n"))
    g["P5"] = set(ea) == set(eb) and set(ba) == set(bb)
    op = lambda B: sorted(b["h"] for b in B if "OPEN" in b["tags"])
    g["P6"] = op(Ba) == op(Bb)
    g["P7"] = "403/250" not in fin and "1.612" not in fin
    g["P8"] = ("DRAFT r3 — not adopted" not in fin and "Supersedes on adoption" not in fin
               and fin.startswith("# RTG Number Genesis DSN v1.20.8\n") and "**Document status:** ADOPTED owner ledger" in fin)
    open("_f.md", "w", encoding="utf-8").write(fin)
    r = subprocess.run([sys.executable, "ng_inv_live_v1_1.py", "_f.md"], capture_output=True, text=True)
    g["P9"] = r.returncode == 0 and "0 live hit" in r.stdout
    return g

if __name__ == "__main__":
    r3 = open(R3, encoding="utf-8").read(); fin = open(OUT, encoding="utf-8").read()
    edits = json.load(open("release_v1_20_8_edits.json", encoding="utf-8"))
    h = sha(fin.encode())
    subprocess.run([sys.executable, "release_v1_20_8.py"], check=True, capture_output=True)
    g = {"P1": sha(open(OUT, "rb").read()) == h, **run(r3, fin, edits)}
    print(json.dumps({"final_sha256": h, "gates": g}, indent=1, sort_keys=True))
    ok = all(g.values())
    if "--neg" in sys.argv:
        def neg(a, b):
            assert fin.count(a) >= 1, a
            return all(run(r3, fin.replace(a, b, 1), edits).values())
        n = {
            "M1 body edit outside release spans": neg("only through the entry-phase shift", "only through the entry phase shift"),
            "M2 regrade": neg("`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]", "`[RESULT] [from: THM]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE]"),
            "M3 RID dropped": neg("[RID: NUMGEN-RESULT-N5AS1-L-MONO] ", ""),
            "M4 constant entered": neg("No constant is entered in this edition", "C = 403/250 is entered in this edition"),
            "M5 OPEN sub-item closed": neg("`[OPEN]` `[target: THM]` `[v1.20.8]` **L-PHASE explicit constant", "`[RESULT]` `[v1.20.8]` **L-PHASE explicit constant"),
        }
        # M6 stale edition marker: release edit list kept, marker reinserted
        e6 = [dict(e, new=e["new"].replace("# RTG Number Genesis DSN v1.20.8\n", "# RTG Number Genesis DSN v1.20.8 — DRAFT r3\n")) for e in edits]
        n["M6 stale title"] = all(run(r3, fin.replace("# RTG Number Genesis DSN v1.20.8\n", "# RTG Number Genesis DSN v1.20.8 — DRAFT r3\n", 1), e6).values())
        print(json.dumps({"negative_controls_pass_should_be_false": n}, indent=1))
        ok = ok and not any(n.values())
    print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
