#!/usr/bin/env python3
# NUMBER GENESIS SCIENTIFIC-STATE FINGERPRINT  v1
# Extracts every status-tagged claim line from an owner file, normalized, with
# its section and RID(s). Purpose: make "zero scientific change" MECHANICALLY
# checkable across the methodology-only §2/§6 migration. The migration passes
# iff every statused claim in the baseline appears in the migrated file (moved
# is fine), and every claim removed as a §2/§6 duplicate has a retained twin
# recorded in the migration ledger — no silent drops, no silent rewording.
import re, sys, json, hashlib
TAGS=r"\[(RESULT|OPEN|DEF|HYP|GUARD|COR[^\]]*|REJECTED[^\]]*|HOLD|THM|ALG|NUM|CLOSED|HEUR|INTERP|POSTHOC-DIAG)\]"
def norm(t): return re.sub(r"\s+"," ",t.strip())
def fingerprint(path):
    sec="preamble"; rows=[]
    for i,l in enumerate(open(path,encoding='utf-8'),1):
        if l.startswith("## ") or l.startswith("### "): sec=l.strip("# \n")[:60]
        if re.search(TAGS,l):
            tags=sorted(set(re.findall(TAGS,l)))
            rids=sorted(set(re.findall(r"(NUMGEN-[A-Z0-9\-]+|DYAD-[A-Z0-9\-]+|RTG-OFN-[A-Z0-9\-]+|C7B-ALG-T\d|SG-NG-\d+)",l)))
            rows.append({"line":i,"section":sec,"tags":tags,"rids":rids,
                         "text":norm(l),"h":hashlib.sha1(norm(l).encode()).hexdigest()[:12]})
    return rows
if __name__=="__main__":
    p=sys.argv[1]; rows=fingerprint(p)
    out=p.rsplit('.',1)[0]+"_fingerprint.json"
    json.dump(rows,open(out,"w"),indent=1)
    from collections import Counter
    by=Counter(r["section"].split(" ")[0] for r in rows)
    print(f"{len(rows)} statused claim lines -> {out}")
    print("by top-level section:",dict(sorted(by.items())))
    # duplicate-text detection: same normalized text in two sections = §2/§6 mirror
    txt=Counter(r["h"] for r in rows)
    print("exact duplicate claim lines (mirror candidates):",sum(1 for h,c in txt.items() if c>1))
