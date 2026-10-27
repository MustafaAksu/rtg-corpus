# [SUPERSEDED 2026-09-25] by ng_migration_checks_v2.py: v1 INV-S could not represent
# a legitimate relocation; v1 INV-P accepted a 24-char prefix match (false pass).
#!/usr/bin/env python3
# =============================================================================
# NUMBER GENESIS MIGRATION CHECKS  v1 — INV-S and INV-P
# =============================================================================
# INV-S  status/registry conservation. Covers ALL "Status:" lines, anchored by the
#        block fingerprint or not (on v1.20.1: 29 lines, of which 9 are invisible
#        to the block regex). Each status line is keyed by its enclosing heading
#        path (depth <= 6) and any RID on the heading's RID line. The normalized
#        status TEXT must be conserved per key. Living states (ACTIVE, PARTIAL,
#        OPEN, HOLD, BLOCKED, SPLIT, CLOSED) cannot change silently. A change is
#        permitted only through an explicit TAG-NORM ledger entry that leaves the
#        living-state keyword set and the scope brackets unchanged.
# INV-P  pointer/inventory integrity, checked BEFORE any file is written:
#        (P1) every inventory block has exactly one disposition in the allowed set;
#        (P2) every MOVE / MIRROR-RECONCILED destination is an existing §6 heading,
#             or an explicitly flagged NEW-HEADING that awaits ruling;
#        (P3) every MIRROR-RECONCILED block names a retained twin that exists in §6;
#        (P4) every REGISTRY-ONLY block is a bare status header or the §2 queue;
#        (P5) the inventory covers exactly the INV-3 set (no block missing, none extra).
# Usage:  ng_migration_checks_v1.py invS BASE.md NEW.md [LEDGER.json]
#         ng_migration_checks_v1.py invP INVENTORY.json BASE.md FINGERPRINT.json
# =============================================================================
import re, sys, json, io

LIVING = ("CLOSED", "OPEN", "ACTIVE", "PARTIAL", "HOLD", "BLOCKED", "SPLIT")

def status_map(path):
    L = io.open(path, encoding="utf-8").read().split("\n")
    stack = {}; out = {}; rid_for_head = {}
    for i, l in enumerate(L):
        m = re.match(r"(#{2,6}) (.*)", l)
        if m:
            d = len(m.group(1)); stack = {k: v for k, v in stack.items() if k < d}
            stack[d] = m.group(2).strip()
        rm = re.search(r"\*\*RID:\*\*\s*`?([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)", l)
        if rm: rid_for_head[tuple(sorted(stack.items()))] = rm.group(1)
        if re.match(r"\s*\*\*Status:\*\*|^Status:", l):
            path_key = " > ".join(v for _, v in sorted(stack.items()))
            rid = rid_for_head.get(tuple(sorted(stack.items())), "")
            key = f"{rid or '-'} | {path_key}"
            txt = re.sub(r"\s+", " ", l.strip())
            living = tuple(sorted(w for w in LIVING if re.search(r"\b" + w + r"\b", txt)))
            scopes = tuple(re.findall(r"\[scope:[^\]]*\]", txt))
            out.setdefault(key, []).append({"line": i + 1, "text": txt, "living": living, "scopes": scopes})
    return out

def invS(base, new, ledger=None):
    B, N = status_map(base), status_map(new)
    allow = set()
    if ledger:
        for t in json.load(open(ledger)).get("tag_norm", []):
            allow.add((t.get("before_text"), t.get("after_text")))
    fails = []
    nb = sum(len(v) for v in B.values()); nn = sum(len(v) for v in N.values())
    print(f"INV-S: base {nb} status lines under {len(B)} keys | new {nn} under {len(N)} keys")
    for k, bl in B.items():
        nl = N.get(k)
        if nl is None:
            fails.append(f"key lost: {k}"); continue
        bt = [x["text"] for x in bl]; nt = [x["text"] for x in nl]
        if bt == nt: continue
        for b_, n_ in zip(bl, nl):
            if b_["text"] == n_["text"]: continue
            if (b_["text"], n_["text"]) in allow and b_["living"] == n_["living"] and b_["scopes"] == n_["scopes"]:
                continue
            fails.append(f"status changed at {k}: '{b_['text'][:70]}' -> '{n_['text'][:70]}'")
        if len(bl) != len(nl): fails.append(f"status line count changed at {k}: {len(bl)} -> {len(nl)}")
    for k in N:
        if k not in B: fails.append(f"new status key without baseline: {k}")
    for f in fails: print("  [FAIL]", f)
    print("[PASS] INV-S" if not fails else f"[FAIL] INV-S ({len(fails)})")
    return not fails

def invP(inv_path, base, fp_path):
    I = json.load(open(inv_path)); blocks = I["blocks"]
    L = io.open(base, encoding="utf-8").read().split("\n")
    h6 = {l.strip("# ").strip() for i, l in enumerate(L) if 2255 <= i + 1 < 2501 and re.match(r"#{2,6} ", l)}
    FP = json.load(open(fp_path))
    s6h = {b["h"] for b in FP["blocks"] if 2255 <= b["line"] < 2501}
    inv3 = {b["h"] for b in FP["blocks"] if 148 <= b["line"] < 2121 and set(b["tags"]) & {"RESULT", "THM", "ALG"}}
    OK = {"MIRROR-RECONCILED", "MOVE", "REGISTRY-ONLY", "STOP"}
    f = []
    for x in blocks:
        if x["disposition"] not in OK: f.append(f"P1 L{x['line']} bad disposition {x['disposition']}")
        if x["disposition"] in ("MOVE", "MIRROR-RECONCILED"):
            dm = x["destination_module"] or ""
            head = dm.split(" — NEW HEADING")[0]
            if "NEW HEADING REQUIRED" in dm: pass
            elif not any(dm == h or dm.startswith(h[:24]) for h in h6): f.append(f"P2 L{x['line']} destination not a §6 heading: {dm[:60]}")
        if x["disposition"] == "MIRROR-RECONCILED":
            tw = x.get("retained_twin_h")
            if not tw or tw not in s6h: f.append(f"P3 L{x['line']} retained twin missing in §6")
        if x["disposition"] == "REGISTRY-ONLY" and not (x.get("status_header") or (x["s2_module"] or "").startswith("Priority")):
            f.append(f"P4 L{x['line']} REGISTRY-ONLY is not a bare status header or the queue")
    ih = {x["h"] for x in blocks}
    if ih != inv3: f.append(f"P5 inventory/INV-3 mismatch: missing {len(inv3-ih)}, extra {len(ih-inv3)}")
    new_heads = sorted({x["destination_module"] for x in blocks if x["destination_module"] and "NEW HEADING" in x["destination_module"]})
    for e in f: print("  [FAIL]", e)
    print(f"INV-P: {len(blocks)} blocks; pending NEW-HEADING rulings: {len(new_heads)}")
    for h in new_heads: print("   ruling needed:", h)
    print("[PASS] INV-P" if not f else f"[FAIL] INV-P ({len(f)})")
    return not f

if __name__ == "__main__":
    a = sys.argv
    ok = invS(a[2], a[3], a[4] if len(a) > 4 else None) if a[1] == "invS" else invP(a[2], a[3], a[4])
    sys.exit(0 if ok else 1)
