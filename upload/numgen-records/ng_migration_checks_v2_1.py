#!/usr/bin/env python3
# =============================================================================
# NUMBER GENESIS MIGRATION CHECKS  v2.1 — INV-S v2, INV-P v2 (v2.1: documentation only)
# =============================================================================
# v1 -> v2 [COR], per co-owner ruling 2026-09-25:
#  INV-S v1 keyed status identity by full heading path and demanded the path be
#   unchanged. A LEGITIMATE verbatim relocation (N-1B status §2 -> §6.2, an
#   inventory MOVE) therefore failed with exit 1. v2 is relocation-aware:
#     S1  multiset of normalized status texts conserved (no loss, no invention,
#         no rewording) modulo an explicit TAG-NORM allowlist that preserves the
#         living-state keywords and [scope: ...] brackets;
#     S2  a status whose base line lies in an inventory MOVE block must appear
#         under the EXACT destination heading;
#     S3  a status in a REGISTRY-ONLY block must appear on a <!-- REGISTRY --> row;
#     S4  a status outside the inventory (registry-native: ACTIVE/OPEN/PARTIAL/
#         BLOCKED/SPLIT modules) must keep its module identity — RID if present,
#         else the deepest enclosing heading — either as a heading ancestor or on
#         a REGISTRY row naming that module.
#  INV-P v1 accepted any destination sharing a 24-character prefix with a real
#   heading (`dm.startswith(h[:24])`): a valid prefix + "THIS IS BOGUS" PASSED.
#   v2 uses EXACT normalized heading equality; the only exception is an
#   explicit APPROVED_NEW_HEADINGS allowlist. v2 adds a POST-WRITE mode that
#   resolves every MOVE block hash under its destination, requires every
#   MIRROR-RECONCILED discarded copy to be absent and its retained twin present,
#   and requires each approved new heading to exist.
#   [v2.1 doc correction] INV-Ppost does NOT check REGISTRY-ONLY placement; that
#   is enforced by INV-S --mode final (rule S3). No logic change.
#
# COMPOSITE MIGRATION GATE (v2.1): no single checker is the certificate.
#   FP-v2        PRIMARY no-content-change gate: claim-block loss / invention /
#                rewording, identifier conservation.
#   INV-S final  all 29 living statuses at their correct location / registry row.
#   INV-Ppost    MOVE hash placement; mirror elimination and twin retention;
#                approved headings present.
#   INV-LIVE     SECONDARY semantic lint for known withdrawn wording and source
#                pins. It excludes [COR] lines by design (quotations), so it is
#                not a universal stale-state proof.
# Usage:
#   ng_migration_checks_v2.py invS BASE.md NEW.md INVENTORY.json [LEDGER.json] [--mode final|partial]
#     final   (default) every inventory status must be AT its disposition target.
#     partial each status is either UNMOVED (same text, same heading path) or AT its
#             target; wrong destination or rewording still fails. For incremental
#             commits and single-relocation tests. On the unmigrated base, final mode
#             must fail with exactly the number of inventory-governed statuses.
#   ng_migration_checks_v2.py invP INVENTORY.json BASE.md FINGERPRINT.json
#   ng_migration_checks_v2.py invPpost INVENTORY.json NEW.md NEW_FINGERPRINT.json
# =============================================================================
import re, sys, json, io
from collections import Counter

APPROVED_NEW_HEADINGS = {"§6.9a NG-10 — Genesis saturation and counting truncation"}
LIVING = ("CLOSED", "OPEN", "ACTIVE", "PARTIAL", "HOLD", "BLOCKED", "SPLIT")
REG = re.compile(r"<!--\s*REGISTRY\s*-->")

def nrm(t): return re.sub(r"\s+", " ", t.strip())
def nhead(h): return nrm(h.lstrip("#"))

def scan_status(path):
    L = io.open(path, encoding="utf-8").read().split("\n")
    stack = {}; rid_of = {}; out = []
    for i, l in enumerate(L):
        m = re.match(r"(#{2,6}) (.*)", l)
        if m:
            d = len(m.group(1)); stack = {k: v for k, v in stack.items() if k < d}
            stack[d] = nhead(m.group(2)); continue
        rm = re.search(r"\*\*RID:\*\*\s*`?([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)", l)
        if rm: rid_of[tuple(sorted(stack.items()))] = rm.group(1)
        if re.match(r"\s*(<!--\s*REGISTRY\s*-->\s*)?\*\*Status:\*\*|^Status:", l):
            heads = [v for _, v in sorted(stack.items())]
            txt = nrm(REG.sub("", l))
            out.append({"line": i + 1, "text": txt, "heads": heads,
                        "deepest": heads[-1] if heads else "",
                        "rid": rid_of.get(tuple(sorted(stack.items())), ""),
                        "registry": bool(REG.search(l)), "raw": l})
    return out

def living(t): return tuple(sorted(w for w in LIVING if re.search(r"\b" + w + r"\b", t)))
def scopes(t): return tuple(re.findall(r"\[scope:[^\]]*\]", t))

def invS(base, new, inv_path, ledger=None, mode='final'):
    B = scan_status(base); N = scan_status(new)
    blocks = json.load(open(inv_path))["blocks"]
    allow = {}
    if ledger:
        for t in json.load(open(ledger)).get("tag_norm", []):
            allow[nrm(t["before_text"])] = nrm(t["after_text"])
    fail = []
    # S1 multiset conservation modulo TAG-NORM
    bt = Counter(allow.get(x["text"], x["text"]) for x in B)
    nt = Counter(x["text"] for x in N)
    for k, v in allow.items():
        if living(k) != living(v) or scopes(k) != scopes(v):
            fail.append(f"S1 TAG-NORM changes living state or scope: '{k[:60]}'")
    if bt != nt:
        for t in (bt - nt): fail.append(f"S1 status lost/reworded: '{t[:90]}'")
        for t in (nt - bt): fail.append(f"S1 status invented/reworded: '{t[:90]}'")
    def disp_of(line):
        for x in blocks:
            if x["line"] <= line < x["end"]: return x
        return None
    for b in B:
        want = allow.get(b["text"], b["text"])
        cands = [n for n in N if n["text"] == want]
        x = disp_of(b["line"])
        if mode == "partial" and any(c["heads"] == b["heads"] for c in cands):
            continue   # unmoved: same text, same heading path -> acceptable mid-migration
        if x and x["disposition"] == "MOVE":
            dst = x["destination_module"]
            if not any(dst in c["heads"] for c in cands):
                fail.append(f"S2 MOVE status (base L{b['line']}) not under destination '{dst[:50]}'")
        elif x and x["disposition"] == "REGISTRY-ONLY":
            if not any(c["registry"] for c in cands):
                fail.append(f"S3 REGISTRY-ONLY status (base L{b['line']}) not on a REGISTRY row")
        else:
            ident = b["rid"] or b["deepest"]
            ok = any(ident and (ident in c["heads"] or ident == c["rid"] or (c["registry"] and ident in c["raw"]))
                     for c in cands)
            if not ok:
                fail.append(f"S4 registry-native status (base L{b['line']}) lost module identity '{ident[:50]}'")
    for f in fail: print("  [FAIL]", f)
    print(f"INV-S v2 [{mode}]: base {len(B)} / new {len(N)} status lines -> {'PASS' if not fail else 'FAIL'} ({len(fail)})")
    return not fail

def heads6(path):
    L = io.open(path, encoding="utf-8").read().split("\n")
    s6 = next(i for i, l in enumerate(L) if l.startswith("## §6."))
    s7 = next(i for i, l in enumerate(L) if l.startswith("## §7."))
    return {nhead(l) for l in L[s6:s7] if re.match(r"#{2,6} ", l)}

def invP(inv_path, base, fp_path):
    I = json.load(open(inv_path)); blocks = I["blocks"]
    H6 = heads6(base); FP = json.load(open(fp_path))
    s6h = {b["h"] for b in FP["blocks"] if b.get("region") == "§6"}
    inv3 = {b["h"] for b in FP["blocks"] if b.get("region") == "§2" and set(b["tags"]) & {"RESULT", "THM", "ALG"}}
    f = []
    for x in blocks:
        d = x["disposition"]
        if d not in {"MIRROR-RECONCILED", "MOVE", "REGISTRY-ONLY", "STOP"}: f.append(f"P1 L{x['line']} {d}")
        if d in ("MOVE", "MIRROR-RECONCILED"):
            dm = nrm(x["destination_module"] or "")
            if dm not in H6 and dm not in APPROVED_NEW_HEADINGS:
                f.append(f"P2 L{x['line']} destination is not an exact §6 heading nor approved: '{dm[:60]}'")
        if d == "MIRROR-RECONCILED" and x.get("retained_twin_h") not in s6h:
            f.append(f"P3 L{x['line']} retained twin missing in §6")
        if d == "REGISTRY-ONLY" and not (x.get("status_header") or (x.get("s2_module") or "").startswith("Priority")):
            f.append(f"P4 L{x['line']} REGISTRY-ONLY is not a bare status header or the queue")
    ih = {x["h"] for x in blocks}
    if ih != inv3: f.append(f"P5 inventory/INV-3 mismatch: missing {len(inv3-ih)}, extra {len(ih-inv3)}")
    for e in f: print("  [FAIL]", e)
    print(f"INV-P v2 (pre-write): {len(blocks)} blocks -> {'PASS' if not f else 'FAIL'}")
    return not f

def invPpost(inv_path, new, fp_new):
    I = json.load(open(inv_path)); blocks = I["blocks"]
    FP = json.load(open(fp_new)); byh = {}
    for b in FP["blocks"]: byh.setdefault(b["h"], []).append(b)
    L = io.open(new, encoding="utf-8").read().split("\n")
    def heads_at(line):
        stack = {}
        for l in L[:line]:
            m = re.match(r"(#{2,6}) (.*)", l)
            if m:
                d = len(m.group(1)); stack = {k: v for k, v in stack.items() if k < d}; stack[d] = nhead(m.group(2))
        return [v for _, v in sorted(stack.items())]
    H6 = heads6(new); f = []
    for h in APPROVED_NEW_HEADINGS:
        if any(nrm(x["destination_module"] or "") == h for x in blocks) and h not in H6:
            f.append(f"POST approved new heading not written: '{h}'")
    for x in blocks:
        d = x["disposition"]
        if d == "MOVE":
            occ = byh.get(x["h"], [])
            if len(occ) != 1: f.append(f"POST L{x['line']} MOVE block occurs {len(occ)}x (want exactly 1)")
            elif nrm(x["destination_module"]) not in heads_at(occ[0]["line"]):
                f.append(f"POST L{x['line']} MOVE block not under its destination")
        elif d == "MIRROR-RECONCILED":
            if x["h"] in byh: f.append(f"POST L{x['line']} discarded mirror still present")
            if x.get("retained_twin_h") not in byh: f.append(f"POST L{x['line']} retained twin absent")
    for e in f: print("  [FAIL]", e)
    print(f"INV-P v2 (post-write): {len(blocks)} blocks -> {'PASS' if not f else 'FAIL'}")
    return not f

if __name__ == "__main__":
    a = sys.argv
    if a[1] == "invS":
        mode = a[a.index("--mode") + 1] if "--mode" in a else "final"
        pos = [x for x in a[5:] if x not in ("--mode", mode)]
        ok = invS(a[2], a[3], a[4], pos[0] if pos else None, mode)
    elif a[1] == "invP": ok = invP(a[2], a[3], a[4])
    elif a[1] == "invPpost": ok = invPpost(a[2], a[3], a[4])
    sys.exit(0 if ok else 1)
