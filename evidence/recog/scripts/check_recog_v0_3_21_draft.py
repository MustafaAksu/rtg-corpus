#!/usr/bin/env python3
"""check_recog_v0_3_21_draft.py -- deterministic checker for RECOG v0.3.21 DRAFT r1 (G2 synchronization).

Usage:
  python check_recog_v0_3_21_draft.py BASE_v0_3_20.md DRAFT.md recog_v0_3_21_edits.json            # check
  python check_recog_v0_3_21_draft.py BASE_v0_3_20.md DRAFT.md recog_v0_3_21_edits.json --controls # + negative controls

Gates (all must pass; exit 0 = PASS, 1 = FAIL, 2 = input error):
  C0  base sha256 is the frozen v0.3.20 identity
  C1  BUILD      draft == exact-once application of the edit list to the base (byte-exact)
  C2  POSITIVE   every edit's replacement text occurs exactly once in the draft (intended change present)
  C3  REVERSE    undoing every edit in the draft recovers the base byte-exactly
                 => no change outside the declared spans; location-sensitive preservation of every grade
                    tag, RID-to-statement association and OPEN status outside the spans (a compensating
                    pair of grade changes or a swapped RID fails here)
  C4  SPAN TAGS  within each edit, the grade-tag sequence of the old text is a subsequence of the new
                 text's sequence, and every added tag is declared in that edit's allowed list
  C5  SPAN RIDS  within each edit, every [RID: ...] of the old text survives; added RIDs are declared
  C6  STATUS     the ordered list of OPEN-registry "Status:" lines is identical to the base
  C7  RID SET    RECOG RID set of the draft == base set plus the declared new artifact RIDs
  C8  VOCAB      no READ / WRITE / DECODE vocabulary is introduced (count equals the base)
  C9  N13        the N13 receipt row is conditional (contains "pending" and "conditional receipt only")
                 and contains none of "accepted", "imported", "adopted"
"""
import sys, re, json, hashlib

BASE_SHA = "fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df"
TAG = re.compile(r"`\[(?:ALG|THM|NUM|DEF|RESULT|HYP|OPEN|ENG|SESSION|HEUR|COR|FAIL|CAND|OBS|INTERP|import)[^`\]]*\]`")
RID = re.compile(r"\[RID: (RECOG-[A-Z0-9-]+)")
ANYRID = re.compile(r"\[RID: ([A-Z][A-Z0-9-]+)")
VOCAB = re.compile(r"\b(READ|WRITE|DECODE)\b")

def tags(s): return [m.group(0) for m in TAG.finditer(s)]
def is_subseq(a, b):
    it = iter(b); return all(x in it for x in a)

def check(base, draft, edits, verbose=True):
    res = {}
    def gate(name, ok, msg=""):
        res[name] = ok
        if verbose: print(f"  {name:<10} {'PASS' if ok else 'FAIL'} {msg}")
    gate("C0", hashlib.sha256(base.encode()).hexdigest() == BASE_SHA)
    t = base; ok = True
    for e in edits:
        if t.count(e["old"]) != 1: ok = False; break
        t = t.replace(e["old"], e["new"], 1)
    gate("C1", ok and t == draft, "(BUILD)")
    pos = [e["id"] for e in edits if draft.count(e["new"]) != 1]
    gate("C2", not pos, f"(POSITIVE) missing/repeated: {pos}" if pos else "(POSITIVE)")
    r = draft; ok = True
    for e in reversed(edits):
        if r.count(e["new"]) != 1: ok = False; break
        r = r.replace(e["new"], e["old"], 1)
    gate("C3", ok and r == base, "(REVERSE)")
    bad = []
    for e in edits:
        to, tn = tags(e["old"]), tags(e["new"])
        if not is_subseq(to, tn): bad.append(e["id"]); continue
        extra = list(tn)
        for x in to: extra.remove(x)
        if any(x.strip("`") not in e["allowed_new_tags"] for x in extra): bad.append(e["id"])
    gate("C4", not bad, f"(SPAN TAGS) {bad}" if bad else "(SPAN TAGS)")
    bad = []
    for e in edits:
        ro, rn = ANYRID.findall(e["old"]), ANYRID.findall(e["new"])
        if any(x not in rn for x in ro) or any(x not in ro and x not in e["allowed_new_rids"] for x in rn):
            bad.append(e["id"])
    gate("C5", not bad, f"(SPAN RIDS) {bad}" if bad else "(SPAN RIDS)")
    st = lambda s: [l for l in s.splitlines() if l.startswith("Status:")]
    gate("C6", st(base) == st(draft), "(STATUS)")
    allowed = set(x for e in edits for x in e["allowed_new_rids"])
    gate("C7", set(RID.findall(draft)) == set(RID.findall(base)) | allowed, "(RID SET)")
    gate("C8", len(VOCAB.findall(draft)) == len(VOCAB.findall(base)), "(VOCAB)")
    row = [l for l in draft.splitlines() if l.startswith("| N13 (v6.4.17)")]
    ok = len(row) == 1 and "pending" in row[0] and "conditional receipt only" in row[0] \
         and not any(w in row[0].lower() for w in ("accepted", "imported", "adopted"))
    gate("C9", ok, "(N13)")
    return all(res.values())

def controls(base, draft, edits):
    print("\nNEGATIVE CONTROLS (each must FAIL):")
    def first_outside(s, a, b):
        i = s.find("### §6.7 Shear-Jet Law"); j = s.find(a, i)
        return s[:j] + b + s[j + len(a):]
    muts = {}
    e0 = edits[9]
    muts["NC1 omit one edit"] = draft.replace(e0["new"], e0["old"], 1)
    muts["NC2 grade changed outside spans"] = first_outside(draft, "`[ALG]`", "`[THM]`")
    m = first_outside(draft, "`[ALG]`", "`[THM]`")
    k = m.find("### §6.10"); k2 = m.find("`[THM]`", m.find("### §6.11"))
    muts["NC3 compensating pair of grade changes"] = m[:k2] + "`[ALG]`" + m[k2 + 7:]
    muts["NC4 OPEN status altered"] = draft.replace("Status: ACTIVE\n", "Status: CLOSED\n", 1)
    muts["NC5 READ/DECODE vocabulary inserted"] = draft.replace("Owner editions that consume RECOG RIDs", "Owner editions that DECODE RECOG RIDs", 1)
    muts["NC6 N13 worded as acceptance"] = draft.replace("none decided; conditional receipt only", "accepted for use", 1)
    a, b = "[RID: RECOG-ALG-SHEAR-JET]", "[RID: RECOG-ALG-CUBIC-RETURN-RIGIDITY]"
    i, j = draft.find(a), draft.find(b)
    sw = draft[:i] + b + draft[i + len(a):j] + a + draft[j + len(b):] if i < j else None
    muts["NC7 RID swapped between statements"] = sw
    muts["NC8 grade changed inside an edit span"] = draft.replace("`[THM — conditional on T1]`", "`[THM]`", 1)
    allfail = True
    for name, mtxt in muts.items():
        if mtxt is None or mtxt == draft:
            print(f"  {name:<42} NOT CONSTRUCTED"); allfail = False; continue
        r = check(base, mtxt, edits, verbose=False)
        print(f"  {name:<42} {'caught' if not r else 'NOT CAUGHT'}")
        allfail &= not r
    return allfail

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) != 3: print(__doc__); sys.exit(2)
    try:
        base = open(a[0], encoding="utf-8").read(); draft = open(a[1], encoding="utf-8").read()
        edits = json.load(open(a[2], encoding="utf-8"))["edits"]
    except OSError as e:
        print(f"INPUT ERROR {e}"); sys.exit(2)
    print(f"BASE  sha256 {hashlib.sha256(base.encode()).hexdigest()}")
    print(f"DRAFT sha256 {hashlib.sha256(draft.encode()).hexdigest()}")
    print(f"EDITS {len(edits)}\nGATES:")
    ok = check(base, draft, edits)
    if "--controls" in sys.argv:
        ok &= controls(base, draft, edits)
    print("\nRESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
