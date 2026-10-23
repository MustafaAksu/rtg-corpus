#!/usr/bin/env python3
"""check_recog_v0_3_22_release.py -- checker for the v0.3.22 adoption pass (DRAFT r3 -> adopted).

Usage: python check_recog_v0_3_22_release.py DRAFT_r3.md ADOPTED.md recog_v0_3_22_release_edits.json [--controls]
Gates (exit 0 PASS, 1 FAIL, 2 input error):
  P0  input sha256 is the accepted DRAFT r3 identity
  P1  BUILD     adopted == exact-once application of the release edits to r3
  P2  POSITIVE  each release replacement occurs exactly once in the adopted file
  P3  REVERSE   undoing the release edits recovers r3 byte-exactly (no change outside the 12 declared spans)
  P4  TAGS      grade-tag sequence of the whole file identical to r3 (release adds or removes no grade)
  P5  RIDS      ordered [RID: ...] sequence identical to r3 (registration changes status wording, not identifiers)
  P6  STATUS    OPEN-registry "Status:" lines identical to r3 (R6 ACTIVE and every other OPEN status unchanged)
  P7  VOCAB     READ/WRITE/DECODE count identical to r3
  P8  SCIENCE   §6.13b identical to r3 except the single registration sentence; the R9 theorem line identical
  P9  N13       receipt and verification cells identical to r3; use cell says "in effect from adoption" and contains
                neither "accepted" nor "imported"
  P10 NUMGEN    none of the six approved-but-not-yet-canonical NUMGEN strings occurs; "RID unavailable" count unchanged
  P11 PROVEN.   §8 carries the full hashes of the final NUMGEN reply v0.1.1, its addendum and the r3 delta review
  P12 MARKERS   title, supersedes, freeze status, footer and Appendix A heading in adopted form; date free of
                "DRAFT r3"/"not adopted"/"on adoption"/"until adoption"/"proposed"; status summary labelled "(v0.3.22):" and
                free of "not adopted"/"until adoption"/"only on adoption"/"proposed"/"PI adoption pending" (it cites
                DRAFT r3 as the adopted source); §6.13b registration sentence in adopted form
"""
import sys, re, json, hashlib
R3_SHA = "8f496d3c1fd0182e058e5fd814c5530e3952d5469b3ea932d3d3f27718fbd959"
TAG = re.compile(r"`\[(?:ALG|THM|NUM|DEF|RESULT|HYP|OPEN|ENG|SESSION|HEUR|COR|FAIL|CAND|OBS|INTERP|import)[^`\]]*\]`")
RID = re.compile(r"\[RID: ([^\]]+)\]")
VOCAB = re.compile(r"\b(READ|WRITE|DECODE)\b")
MARK = ("DRAFT r3", "not adopted", "on adoption", "until adoption", "proposed")
SMARK = ("not adopted", "until adoption", "only on adoption", "proposed", "PI adoption pending")
PRE = ("NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT", "NUMGEN-DEF-N5AS1-DEFECT", "NUMGEN-RESULT-N5AS1-L-BACKBONE",
       "NUMGEN-RESULT-N5AS1-L-MONO", "NUMGEN-RESULT-N5AS1-L-PHASE", "NUMGEN-RESULT-N5AS1-INF1")
REG_OLD = "**RIDs in this subsection are proposed and are registered only on adoption of this release.**"
REG_NEW = "**RIDs in this subsection were registered on adoption of v0.3.22 (20 Oct 2026).**"
R9LINE = "`[THM]` [RID: RECOG-THM-R9-MEMORY]"

def cell(s):
    i = s.find("#### §6.13b A1a"); j = s.find("### §6.14 The $h$-Chart Ledger", i)
    return s[i:j] if i >= 0 and j > i else None

def check(r3, ad, edits, verbose=True):
    res = {}
    def g(n, ok, m=""):
        res[n] = ok
        if verbose: print(f"  {n:<4} {'PASS' if ok else 'FAIL'} {m}")
    g("P0", hashlib.sha256(r3.encode()).hexdigest() == R3_SHA)
    t = r3; ok = True
    for e in edits:
        if t.count(e["old"]) != 1: ok = False; break
        t = t.replace(e["old"], e["new"], 1)
    g("P1", ok and t == ad, "(BUILD)")
    g("P2", all(ad.count(e["new"]) == 1 for e in edits), "(POSITIVE)")
    r = ad; ok = True
    for e in reversed(edits):
        if r.count(e["new"]) != 1: ok = False; break
        r = r.replace(e["new"], e["old"], 1)
    g("P3", ok and r == r3, "(REVERSE)")
    g("P4", TAG.findall(ad) == TAG.findall(r3), "(TAGS)")
    g("P5", RID.findall(ad) == RID.findall(r3), "(RIDS)")
    st = lambda s: [l for l in s.splitlines() if l.startswith("Status:")]
    g("P6", st(ad) == st(r3), "(STATUS)")
    g("P7", len(VOCAB.findall(ad)) == len(VOCAB.findall(r3)), "(VOCAB)")
    ca, c3 = cell(ad), cell(r3)
    r9 = lambda s: [l for l in s.splitlines() if l.startswith(R9LINE)]
    g("P8", ca is not None and c3 is not None and ca.count(REG_NEW) == 1 and ca.replace(REG_NEW, REG_OLD) == c3
           and r9(ad) == r9(r3) and len(r9(ad)) == 1, "(SCIENCE)")
    n13 = lambda s: [l for l in s.splitlines() if l.startswith("| N13 (v6.4.17)")]
    a13, r13 = n13(ad), n13(r3)
    ok = len(a13) == 1 and len(r13) == 1
    if ok:
        fa, fr = a13[0].split(" | "), r13[0].split(" | ")
        ok = len(fa) == len(fr) == 4 and fa[:3] == fr[:3] and "in effect from adoption" in fa[3] \
             and not any(w in fa[3].lower() for w in ("accepted", "imported"))
    g("P9", ok, "(N13)")
    g("P10", not any(p in ad for p in PRE) and ad.count("RID unavailable") == r3.count("RID unavailable"), "(NUMGEN STRINGS)")
    s8 = ad[ad.find("## §8. Artifact and Script Registry"):ad.find("## §9. Collaboration and Provenance")]
    g("P11", all(h in s8 for h in ("a2e7bf98fe08d2d64a883b8996c285ba4b67c94f73bb53548abe206f228b1902",
                                    "582d931e0055964fccd541e9ba33defce65f57c6e1cb53385d0f1f155502ceae",
                                    "2a65093baa6a07e57faa056ecd755cc8689f94c59d5f071996b31ebb5979fc96")), "(PROVENANCE)")
    L = ad.splitlines()
    first = lambda pre: next((l for l in L if l.startswith(pre)), "")
    ok = (L[0] == "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22"
          and first("**Supersedes").startswith("**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21`")
          and first("**Freeze status:**").startswith("**Freeze status:** v0.3.22 adopted 20 Oct 2026")
          and first("*END OF DOCUMENT").strip() == "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22*"
          and first("### v0.3.22").strip() == "### v0.3.22 — 20 October 2026 (A1a scientific cell; adopted)"
          and not any(m in x for m in MARK for x in (first("**Date:**"), first("### v0.3.22")))
          and first("**Status summary (v0.3.22").startswith("**Status summary (v0.3.22):**")
          and not any(m in first("**Status summary (v0.3.22") for m in SMARK)
          and REG_NEW in ad and REG_OLD not in ad)
    g("P12", ok, "(MARKERS)")
    return all(res.values())

def controls(r3, ad, edits):
    print("\nNEGATIVE CONTROLS (each must FAIL):")
    def outside(s, a, b):
        i = s.find("### §6.7 Shear-Jet Law"); j = s.find(a, i)
        return s[:j] + b + s[j + len(a):]
    m = {}
    m["NC1 omit one release edit"] = ad.replace(edits[8]["new"], edits[8]["old"], 1)
    m["NC2 grade changed outside spans"] = outside(ad, "`[ALG]`", "`[THM]`")
    m["NC3 A1a theorem regraded"] = ad.replace("`[THM]` [RID: RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION]", "`[RESULT]` [RID: RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION]", 1)
    m["NC4 R6 status altered"] = ad.replace("Status: ACTIVE (sharpened v0.3; identifiability audited v0.3.7)", "Status: CLOSED", 1)
    m["NC5 R9 row altered"] = ad.replace("$(C_2,q_{\\max})=(517,\\tfrac1{400})$ on $|z|\\le\\tfrac1{20}$", "$(C_2,q_{\\max})=(163,\\tfrac1{400})$ on $|z|\\le\\tfrac1{20}$", 1)
    m["NC6 N13 worded as imported"] = ad.replace("in effect from adoption (v0.3.21", "imported (v0.3.21", 1)
    m["NC7 NUMGEN string cited early"] = ad.replace("[RID: (none — NUMGEN INF-1,", "[RID: NUMGEN-RESULT-N5AS1-INF1 (none — NUMGEN INF-1,", 1)
    m["NC8 final-reply hash missing"] = ad.replace("a2e7bf98fe08d2d64a883b8996c285ba4b67c94f73bb53548abe206f228b1902", "a2e7bf98…1902", 1)
    m["NC9 draft marker left in footer"] = ad.replace("*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22*", "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22 (DRAFT r3)*", 1)
    m["NC11 status summary left as proposed"] = ad.replace("with eight scientific RIDs and four artifact IDs (§8), all registered on adoption (20 Oct 2026).", "with eight proposed RIDs (registered only on adoption) and four artifact IDs (§8).", 1)
    m["NC10 OPEN-21 constant altered"] = ad.replace("$\\tfrac{3951}{1000}$ | $517$ |", "$\\tfrac{3951}{1000}$ | $163$ |", 1)
    allfail = True
    for name, txt in m.items():
        if txt == ad: print(f"  {name:<34} NOT CONSTRUCTED"); allfail = False; continue
        r = check(r3, txt, edits, verbose=False)
        print(f"  {name:<34} {'caught' if not r else 'NOT CAUGHT'}"); allfail &= not r
    return allfail

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) != 3: print(__doc__); sys.exit(2)
    try:
        r3 = open(a[0], encoding="utf-8").read(); ad = open(a[1], encoding="utf-8").read()
        edits = json.load(open(a[2], encoding="utf-8"))["edits"]
    except OSError as e:
        print(f"INPUT ERROR {e}"); sys.exit(2)
    print(f"R3      sha256 {hashlib.sha256(r3.encode()).hexdigest()}")
    print(f"ADOPTED sha256 {hashlib.sha256(ad.encode()).hexdigest()}")
    print(f"EDITS {len(edits)}\nGATES:")
    ok = check(r3, ad, edits)
    if "--controls" in sys.argv: ok &= controls(r3, ad, edits)
    print("\nRESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)

if __name__ == "__main__": main()
