#!/usr/bin/env python3
"""check_recog_v0_3_21_release.py -- checker for the v0.3.21 adoption pass (DRAFT r2 -> adopted).

Usage: python check_recog_v0_3_21_release.py DRAFT_r2.md ADOPTED.md recog_v0_3_21_release_edits.json [--controls]
Gates (exit 0 PASS, 1 FAIL, 2 input error):
  P0 input sha256 is the accepted DRAFT r2 identity
  P1 BUILD    adopted == exact-once application of the release edits to r2
  P2 POSITIVE each release replacement occurs exactly once in the adopted file
  P3 REVERSE  undoing the release edits recovers r2 byte-exactly (no change outside the marker spans)
  P4 TAGS     grade-tag sequence of the whole file identical to r2 (release adds no grade)
  P5 RIDS     ordered [RID: ...] sequence identical to r2
  P6 STATUS   OPEN-registry "Status:" lines identical to r2
  P7 VOCAB    READ/WRITE/DECODE count identical to r2
  P8 N13      N13 receipt row identical to r2 (still conditional)
  P9 MARKERS  edition-marker lines are in adopted form: title, supersedes, freeze status, footer exact;
              date, v0.3.21 status-summary and Appendix A heading free of "DRAFT r2"/"not adopted"/"on|until adoption"
"""
import sys, re, json, hashlib
R2_SHA = "be164a9f7dba3943e06d76e8a9448cb9b02d395f9ab18947498bdf3a8fef58c2"
TAG = re.compile(r"`\[(?:ALG|THM|NUM|DEF|RESULT|HYP|OPEN|ENG|SESSION|HEUR|COR|FAIL|CAND|OBS|INTERP|import)[^`\]]*\]`")
RID = re.compile(r"\[RID: ([^\]]+)\]")
VOCAB = re.compile(r"\b(READ|WRITE|DECODE)\b")
MARK = ("DRAFT r2", "not adopted", "on adoption", "until adoption")

def check(r2, ad, edits, verbose=True):
    res = {}
    def g(n, ok, m=""):
        res[n] = ok
        if verbose: print(f"  {n:<4} {'PASS' if ok else 'FAIL'} {m}")
    g("P0", hashlib.sha256(r2.encode()).hexdigest() == R2_SHA)
    t = r2; ok = True
    for e in edits:
        if t.count(e["old"]) != 1: ok = False; break
        t = t.replace(e["old"], e["new"], 1)
    g("P1", ok and t == ad, "(BUILD)")
    g("P2", all(ad.count(e["new"]) == 1 for e in edits), "(POSITIVE)")
    r = ad; ok = True
    for e in reversed(edits):
        if r.count(e["new"]) != 1: ok = False; break
        r = r.replace(e["new"], e["old"], 1)
    g("P3", ok and r == r2, "(REVERSE)")
    g("P4", TAG.findall(ad) == TAG.findall(r2), "(TAGS)")
    g("P5", RID.findall(ad) == RID.findall(r2), "(RIDS)")
    st = lambda s: [l for l in s.splitlines() if l.startswith("Status:")]
    g("P6", st(ad) == st(r2), "(STATUS)")
    g("P7", len(VOCAB.findall(ad)) == len(VOCAB.findall(r2)), "(VOCAB)")
    n13 = lambda s: [l for l in s.splitlines() if l.startswith("| N13 (v6.4.17)")]
    g("P8", n13(ad) == n13(r2) and len(n13(ad)) == 1, "(N13)")
    L = ad.splitlines()
    first = lambda pre: next((l for l in L if l.startswith(pre)), "")
    ok = (L[0] == "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21"
          and first("**Supersedes").startswith("**Supersedes:** ")
          and first("**Freeze status:**").startswith("**Freeze status:** v0.3.21 adopted")
          and first("*END OF DOCUMENT").strip() == "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21*"
          and not any(m in x for m in MARK for x in (first("**Date:**"), first("**Status summary (v0.3.21"), first("### v0.3.21"))))
    g("P9", ok, "(MARKERS)")
    return all(res.values())

def controls(r2, ad, edits):
    print("\nNEGATIVE CONTROLS (each must FAIL):")
    i = ad.find("### §6.7 Shear-Jet Law"); j = ad.find("`[ALG]`", i)
    m = {
      "RC1 release edit omitted": ad.replace(edits[6]["new"], edits[6]["old"], 1),
      "RC2 grade changed in body": ad[:j] + "`[THM]`" + ad[j + 7:],
      "RC3 OPEN status altered": ad.replace("Status: ACTIVE\n", "Status: CLOSED\n", 1),
      "RC4 N13 worded as acceptance": ad.replace("none decided; conditional receipt only", "accepted for use", 1),
      "RC5 RID renamed": ad.replace("[RID: RECOG-ALG-SHEAR-JET]", "[RID: RECOG-ALG-SHEAR-JET-X]", 1),
      "RC6 body text changed outside markers": ad.replace("rows not mixed", "rows mixed", 1),
      "RC7 draft marker left in title": ad.replace("# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21\n", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21 (DRAFT r2)\n", 1),
    }
    allc = True
    for n, x in m.items():
        if x == ad: print(f"  {n:<40} NOT CONSTRUCTED"); allc = False; continue
        c = not check(r2, x, edits, verbose=False); allc &= c
        print(f"  {n:<40} {'caught' if c else 'NOT CAUGHT'}")
    return allc

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) != 3: print(__doc__); sys.exit(2)
    try:
        r2 = open(a[0], encoding="utf-8").read(); ad = open(a[1], encoding="utf-8").read()
        edits = json.load(open(a[2], encoding="utf-8"))["edits"]
    except OSError as e: print(f"INPUT ERROR {e}"); sys.exit(2)
    print(f"R2      sha256 {hashlib.sha256(r2.encode()).hexdigest()}")
    print(f"ADOPTED sha256 {hashlib.sha256(ad.encode()).hexdigest()}")
    print(f"EDITS {len(edits)}\nGATES:")
    ok = check(r2, ad, edits)
    if "--controls" in sys.argv: ok &= controls(r2, ad, edits)
    print("\nRESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)

if __name__ == "__main__": main()
