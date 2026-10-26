#!/usr/bin/env python3
# INV-LIVE v1.1 — whole-document scan of LIVE text for withdrawn wording and
# [v1.1 doc] ROLE: SECONDARY semantic lint. It catches KNOWN withdrawn phrases and
# pins only, and excludes [COR] lines by design to avoid quotation false positives,
# so it is not a universal stale-state proof. The PRIMARY no-content-change gate
# is the FP-v2 claim-block fingerprint. No logic change from v1.
# superseded source pins. Excluded (quote withdrawn text by design):
#   the changelog; the Appendix A "Historical status narrative" block;
#   Appendix B rejected formulations; any line carrying a [COR ...] tag.
# The inventory generator could not see §6/§7, which is how STOP-02/03 escaped.
import re, sys, io
WITHDRAWN = [
 ("relational-category architecture", "S5: C_NG is a typed relational architecture with partial physical composition"),
 ("relational category architecture", "S5"),
 ("v6.4.9", "G1: live Dyadic pointer is v6.4.10"),
 ("FOUNDATIONS_v0.7", "G1: live OFN pointer is v0.8"),
 ("OVERVIEW_v1.1", "G1: live Programme pointer is v1.2"),
 ("NUM-audited", "S6: reflection is [ALG] via P3"),
 ("pending (D15)", "S8: D15 SYNC COMPLETE"),
 ("separate governance edit", "STOP-01: D15 SYNC COMPLETE"),
 ("provenance unresolved upstream", "S3: resolved in Dyadic v6.4.10"),
 ("trivial for unary maps", "v1.18.1: WD-DOM trivial only for the TOTAL map S"),
 ("vanishes identically", "v1.19 I6a: bounded remainder"),
 ("no existing L1/N-1 theorem supplies a numeric radius", "S2: explicit tube DYAD-THM-PRIM-CTR"),
 ("Mod-N completeness is not claimed", "v1.19: Z_N completeness certified"),
 ("normal-form real-ray", "S3/P1: typed-object guard"),
 ("differ from six-block indices only by", "v1.19 I6b: n_k = 6 M_k + O(1)"),
 ("C7C-M design is the next", "v1.20: queue head is interface-typed WD-DOM"),
]
def live_lines(path):
    L = io.open(path, encoding="utf-8").read().split("\n")
    out = []; skip = False; in_hist = False; in_B = False
    for i, l in enumerate(L):
        if l.startswith("## Changelog"): skip = True
        if l.startswith("## Appendix B"): in_B = True
        elif l.startswith("## "): in_B = False
        if "Historical status narrative" in l: in_hist = True
        elif in_hist and l.startswith("Historical (v1."): in_hist = False
        if skip or in_B or in_hist: continue
        if l.startswith("Historical (v"): continue   # explicitly version-scoped historical record
        if re.search(r"\[COR[^\]]*\]", l): continue
        out.append((i + 1, l))
    return out
def scan(path):
    hits = []
    for n, l in live_lines(path):
        for w, why in WITHDRAWN:
            if w in l: hits.append((n, w, why, l.strip()[:110]))
    return hits
if __name__ == "__main__":
    h = scan(sys.argv[1])
    for n, w, why, t in h: print(f"  [HIT] L{n}  '{w}'  ({why})\n        {t}")
    print(f"INV-LIVE: {len(h)} live hit(s) -> {'PASS' if not h else 'FAIL'}")
    sys.exit(0 if not h else 1)
