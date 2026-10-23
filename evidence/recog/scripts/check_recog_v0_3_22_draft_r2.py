#!/usr/bin/env python3
"""check_recog_v0_3_22_draft_r2.py -- deterministic checker for RECOG v0.3.22 DRAFT r2 (A1a scientific cell).
r2 change vs the r1 checker: C10 requires "dedicated RID request prepared, not yet dispatched" in §6.13b and forbids
"dedicated RID requested" in §6.13b, §7 and the companion line (historical Appendix lines excepted) (L2); NC9 now reinserts the r1 wording; C12 requires the L1 header typing.

Usage:
  python check_recog_v0_3_22_draft.py BASE_v0_3_21.md DRAFT.md recog_v0_3_22_edits_r1.json             # check
  python check_recog_v0_3_22_draft.py BASE_v0_3_21.md DRAFT.md recog_v0_3_22_edits_r1.json --controls  # + negative controls

Gates (all must pass; exit 0 = PASS, 1 = FAIL, 2 = input error):
  C0  base sha256 is the adopted v0.3.21 identity
  C1  BUILD      draft == exact-once application of the edit list to the base (byte-exact)
  C2  POSITIVE   every edit's replacement text occurs exactly once in the draft
  C3  REVERSE    undoing every edit recovers the base byte-exactly (no change outside the declared spans; every
                 existing grade tag, RID-to-statement association, R9 statement and OPEN status preserved in place)
  C4  SPAN TAGS  per edit, old grade-tag sequence is a subsequence of the new one; added tags are declared
  C5  SPAN RIDS  per edit, every [RID: ...] of the old text survives; added RIDs are declared
  C6  STATUS     ordered OPEN-registry "Status:" lines identical to the base
  C7  RID SET    RECOG RID set == base set + 8 proposed scientific RIDs + 4 artifact RIDs (declared in the JSON)
  C8  VOCAB      no READ / WRITE / DECODE vocabulary introduced
  C9  N13        N13 row keeps three fields: "owner-reported", "source check", "takes effect only on adoption";
                 contains neither "accepted" nor "imported"
  C10 A1A CELL   §6.13b anchor exactly once; each proposed scientific RID registered exactly once there as [RID: X];
                 owner qualifier "[ALG — formal second order; remainder not certified]" carried in §6.13b and §7;
                 "RID unavailable" >= 2 in §6.13b with "dedicated RID requested" and "unresolved identifier governance"
  C12 HEADER     L1: the v0.3.22 status summary names the local extension D_M^U, not NUMGEN's D_M
  C11 ROWS       the (c) row table reproduces the OPEN 21 per-row constants exactly (rows not mixed)
"""
import sys, re, json, hashlib

BASE_SHA = "a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3"
TAG = re.compile(r"`\[(?:ALG|THM|NUM|DEF|RESULT|HYP|OPEN|ENG|SESSION|HEUR|COR|FAIL|CAND|OBS|INTERP|import)[^`\]]*\]`")
RID = re.compile(r"\[RID: (RECOG-[A-Z0-9-]+)")
ANYRID = re.compile(r"\[RID: ([A-Z][A-Z0-9-]+)")
VOCAB = re.compile(r"\b(READ|WRITE|DECODE)\b")

def tags(s): return [m.group(0) for m in TAG.finditer(s)]
def is_subseq(a, b):
    it = iter(b); return all(x in it for x in a)

SCI, ART = [], []

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
    gate("C7", set(RID.findall(draft)) == set(RID.findall(base)) | set(SCI) | set(ART), "(RID SET)")
    gate("C8", len(VOCAB.findall(draft)) == len(VOCAB.findall(base)), "(VOCAB)")
    row = [l for l in draft.splitlines() if l.startswith("| N13 (v6.4.17)")]
    ok = len(row) == 1 and all(w in row[0] for w in ("owner-reported", "source check", "takes effect only on adoption")) \
         and not any(w in row[0].lower() for w in ("accepted", "imported"))
    gate("C9", ok, "(N13)")
    a = "#### §6.13b A1a"; i = draft.find(a); j = draft.find("### §6.14 The $h$-Chart Ledger", i)
    cell = draft[i:j] if i >= 0 and j > i else ""
    q = "`[ALG — formal second order; remainder not certified]`"
    s7 = draft[draft.find("## §7. Import Ledger"):draft.find("### §7.1")]
    ok = draft.count(a) == 1 and all(cell.count(f"[RID: {r}]") == 1 for r in SCI) \
         and q in cell and q in s7 and cell.count("RID unavailable") >= 2 \
         and "dedicated RID request prepared, not yet dispatched" in cell and "dedicated RID requested" not in cell and "dedicated RID requested" not in s7 \
         and not any("dedicated RID requested" in l for l in draft.splitlines() if l.startswith("**Companion documents:**")) and "unresolved identifier governance" in cell
    gate("C10", ok, "(A1A CELL)")
    rows = [r"| A | $0<\lvert W_0\rvert\le\tfrac1{25}$ | $\tfrac3{64}$ | $\lvert z\rvert\le\tfrac1{20}$ | $\tfrac{3951}{1000}$ | $517$ |",
            r"| B | $0<\lvert W_0\rvert\le\tfrac3{128}$ | $\tfrac3{128}$ | $\lvert z\rvert\le\tfrac1{40}$ | $\tfrac{971}{250}$ | $163$ |"]
    gate("C11", all(cell.count(r) == 1 for r in rows), "(ROWS)")
    hs = [l for l in draft.splitlines() if l.startswith("**Status summary (v0.3.22")]
    gate("C12", len(hs) == 1 and "local extension $D_M^U$" in hs[0] and "Number Genesis's primitive phase defect $D_M$ and Dyadic" not in hs[0], "(L1 HEADER TYPING)")
    return all(res.values())

def controls(base, draft, edits):
    print("\nNEGATIVE CONTROLS (each must FAIL):")
    def first_outside(s, a, b):
        i = s.find("### §6.7 Shear-Jet Law"); j = s.find(a, i)
        return s[:j] + b + s[j + len(a):]
    muts = {}
    e0 = next(e for e in edits if e["id"] == "I1")
    muts["NC1 omit one edit"] = draft.replace(e0["new"], e0["old"], 1)
    muts["NC2 grade changed outside spans"] = first_outside(draft, "`[ALG]`", "`[THM]`")
    m = first_outside(draft, "`[ALG]`", "`[THM]`")
    k2 = m.find("`[THM]`", m.find("### §6.11"))
    muts["NC3 compensating pair of grade changes"] = m[:k2] + "`[ALG]`" + m[k2 + 7:]
    muts["NC4 OPEN status altered"] = draft.replace("Status: ACTIVE\n", "Status: CLOSED\n", 1)
    muts["NC5 READ/DECODE vocabulary inserted"] = draft.replace("Owner editions that consume RECOG RIDs", "Owner editions that DECODE RECOG RIDs", 1)
    muts["NC6 N13 worded as acceptance"] = draft.replace("takes effect only on adoption", "accepted for use", 1)
    a, b = "[RID: RECOG-ALG-SHEAR-JET]", "[RID: RECOG-ALG-CUBIC-RETURN-RIGIDITY]"
    i, j = draft.find(a), draft.find(b)
    muts["NC7 RID swapped between statements"] = draft[:i] + b + draft[i + len(a):j] + a + draft[j + len(b):] if i < j else None
    muts["NC8 owner qualifier promoted to [THM]"] = draft.replace("`[ALG — formal second order; remainder not certified]`", "`[THM]`", 1)
    muts["NC9 RID-governance wording dropped"] = draft.replace("dedicated RID request prepared, not yet dispatched (`RECOG_TO_NUMGEN", "dedicated RID requested (`RECOG_TO_NUMGEN", 1)
    muts["NC10 rows mixed (C2 of row B in row A)"] = draft.replace(r"$\tfrac{3951}{1000}$ | $517$ |", r"$\tfrac{3951}{1000}$ | $163$ |", 1)
    muts["NC11 R9 statement altered"] = draft.replace("$(C_2,q_{\\max})=(517,\\tfrac1{400})$ on $|z|\\le\\tfrac1{20}$", "$(C_2,q_{\\max})=(163,\\tfrac1{400})$ on $|z|\\le\\tfrac1{20}$", 1)
    muts["NC13 L1 reverted in header"] = draft.replace("A1a's local extension $D_M^U$ of the Number Genesis defect formula aligns exactly with Dyadic's block phase", "Number Genesis's primitive phase defect $D_M$ and Dyadic's block phase align exactly", 1)
    muts["NC12 extra undeclared RECOG RID"] = draft.replace("[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE]", "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE-X]", 1)
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
        J = json.load(open(a[2], encoding="utf-8")); edits = J["edits"]
        global SCI, ART; SCI, ART = J["proposed_scientific_rids"], J["new_artifact_rids"]
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
