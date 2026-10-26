#!/usr/bin/env python3
# =============================================================================
# NUMBER GENESIS SCIENTIFIC-STATE FINGERPRINT  v2.1
# v2 -> v2.1: literal 'RID' placeholder no longer enters the explicit set.
# =============================================================================
# v1 -> v2 [COR], per co-owner ruling 2026-09-25:
#   (1) v1's "exact duplicate" count was file-wide, not a §2<->§6 pair test.
#       v2 reports duplicates per region pair. Measured on v1.20: §2<->§6 = 0;
#       the single file-wide duplicate is intra-§2 (NG-8A / NG-8B status lines).
#   (2) v1 hashed only the status-tagged LINE. A formula/code/list body under an
#       anchor was invisible: the anchor sentence could survive while the
#       equation beneath it changed. v2 hashes the full CLAIM BLOCK — from a
#       status anchor to the next status anchor or heading — with full SHA-256.
#   (3) v1's RID regex covered five prefixes and missed 80 RID-like identifiers
#       (e.g. RTG-OPEN-GENERATOR-SELECTION, GEN-ART-SATURATION,
#       RECOG-ALG-LATTICE-CLOCK). v2 conserves (a) explicit RID fields
#       (RID:, Sub-RID:, Active architecture RID:, [import: ... | RID]) and
#       (b) a broad set of every RID-like identifier in the file.
#   (4) New §2 registry rows are STRUCTURAL records, not scientific claims:
#       they are parsed by a separate pointer-integrity check and excluded from
#       the scientific fingerprint. Tag normalization in moved blocks is allowed
#       only through an explicit TAG-NORM allowlist (before->after pairs).
#   Also: truncated SHA-1 replaced by full SHA-256 throughout.
#
# Usage:
#   ng_state_fingerprint_v2.py fingerprint FILE [--s2 A:B --s6 C:D]
#   ng_state_fingerprint_v2.py compare BASE.json NEW.json LEDGER.json
# Exit 0 iff (compare mode) all invariants pass.
# =============================================================================
import re, sys, json, hashlib

STATUS = r"\[(RESULT|OPEN|DEF|HYP|GUARD|COR[^\]]*|REJECTED[^\]]*|HOLD|THM|ALG|NUM|CLOSED|HEUR|INTERP|POSTHOC-DIAG)\]"
REGISTRY = r"^\s*<!--\s*REGISTRY\s*-->"          # marker for structural §2 rows
RID_FIELD = re.compile(r"\b(?:Sub-RID|Active architecture RID|RID)s?\b[:\*\s`]*([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)")
# covers **RID:** X, **Sub-RID:** X, RID `X`, RID: X, Active architecture RID: X
RID_IMPORT = re.compile(r"\[import:[^\]|]*\|\s*([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)\s*\]")  # v2.1: require a hyphenated identifier
RID_BROAD = re.compile(r"\b[A-Z][A-Z0-9]{1,}(?:-[A-Z0-9]+){1,}\b")

def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def norm(t): return re.sub(r"[ \t]+", " ", t.strip())

def blocks(path):
    L = open(path, encoding="utf-8").read().split("\n")
    heads = [i for i, l in enumerate(L) if l.startswith("#")]
    anchors = [i for i, l in enumerate(L) if re.search(STATUS, l) and not re.match(REGISTRY, l)]
    stops = sorted(set(heads) | set(anchors) | {len(L)})
    sec = "preamble"; hi = 0; out = []
    for a in anchors:
        while hi < len(heads) and heads[hi] <= a:
            sec = L[heads[hi]].strip("# ").strip()[:60]; hi += 1
        end = next(s for s in stops if s > a)
        body = "\n".join(norm(x) for x in L[a:end]).strip()
        out.append({"line": a + 1, "end": end, "section": sec,
                    "tags": sorted(set(re.findall(STATUS, L[a]))),
                    "h": sha(body), "anchor": norm(L[a])[:160]})
    return out, L

def identifiers(L):
    full = "\n".join(L)
    explicit = set(RID_FIELD.findall(full)) | set(RID_IMPORT.findall(full))
    explicit -= {"RID"}   # v2.1: drop the literal placeholder from '[import: ... | RID unavailable]'
    broad = set(RID_BROAD.findall(full))
    return sorted(explicit), sorted(broad)

def region_of(line, s2, s6):
    if s2[0] <= line < s2[1]: return "§2"
    if s6[0] <= line < s6[1]: return "§6"
    return "other"

def cmd_fingerprint(path, s2, s6):
    bl, L = blocks(path)
    ex, br = identifiers(L)
    for b in bl: b["region"] = region_of(b["line"], s2, s6)
    from collections import defaultdict
    byh = defaultdict(set)
    for b in bl: byh[b["h"]].add(b["region"])
    dup_26 = sum(1 for v in byh.values() if {"§2", "§6"} <= v)
    dup_any = sum(1 for h in byh if sum(1 for b in bl if b["h"] == h) > 1)
    out = {"file": path, "file_sha256": sha(open(path, encoding="utf-8").read()),
           "n_blocks": len(bl), "dup_s2_s6": dup_26, "dup_any": dup_any,
           "explicit_rids": ex, "broad_identifiers": br, "blocks": bl}
    op = path.rsplit(".", 1)[0] + "_fingerprint_v2.json"
    json.dump(out, open(op, "w"), indent=1)
    print(f"{len(bl)} claim blocks | dup §2<->§6: {dup_26} | dup anywhere: {dup_any} | "
          f"explicit RIDs: {len(ex)} | broad identifiers: {len(br)} -> {op}")

def cmd_compare(base_p, new_p, ledger_p):
    B = json.load(open(base_p)); N = json.load(open(new_p)); G = json.load(open(ledger_p))
    fail = []
    def ck(n, c, detail=""):
        print(f"[{'PASS' if c else 'FAIL'}] {n} {detail}")
        if not c: fail.append(n)
    bh = {b["h"] for b in B["blocks"]}; nh = {b["h"] for b in N["blocks"]}
    discards = {d["discarded_h"] for d in G.get("reconciled", [])}
    retained_twins = {d["retained_h"] for d in G.get("reconciled", [])}
    tagnorm = {t["after_h"]: t["before_h"] for t in G.get("tag_norm", [])}
    stops = G.get("stop", [])
    # INV-0: no unresolved STOP items
    ck("INV-0 no unresolved STOP (status/scope/content drift)", not stops, f"({len(stops)} open)")
    # INV-1 no loss
    lost = [h for h in bh if h not in nh and h not in discards and h not in tagnorm.values()]
    ck("INV-1 no loss: every baseline block retained, reconciled, or TAG-NORM'd", not lost, f"({len(lost)} lost)")
    # INV-1b every discard has a retained twin present in NEW
    orphan = [d for d in G.get("reconciled", []) if d["retained_h"] not in nh]
    ck("INV-1b every discarded mirror has its retained twin in the new file", not orphan, f"({len(orphan)})")
    # INV-2 no invention
    invented = [h for h in nh if h not in bh and h not in tagnorm]
    ck("INV-2 no invention: every new block is a baseline block or an allowlisted TAG-NORM", not invented, f"({len(invented)})")
    # INV-3 no theorem bodies in §2
    s2_bodies = [b for b in N["blocks"] if b.get("region") == "§2"
                 and set(b["tags"]) & {"RESULT", "THM", "ALG"}]
    ck("INV-3 no [RESULT]/[THM]/[ALG] claim blocks remain in §2", not s2_bodies, f"({len(s2_bodies)})")
    # INV-4 identifier conservation (explicit AND broad)
    ck("INV-4a explicit RID set conserved", set(B["explicit_rids"]) == set(N["explicit_rids"]),
       f"(missing {sorted(set(B['explicit_rids'])-set(N['explicit_rids']))[:5]})")
    ck("INV-4b broad identifier set conserved", set(B["broad_identifiers"]) <= set(N["broad_identifiers"]),
       f"(missing {sorted(set(B['broad_identifiers'])-set(N['broad_identifiers']))[:5]})")
    print("-" * 70)
    if fail: print("MIGRATION REJECTED:", fail); sys.exit(1)
    print("INV-0..4 PASS. Pair with the separate pointer-integrity check (registry) and INV-5/6.")
    sys.exit(0)

if __name__ == "__main__":
    a = sys.argv
    if a[1] == "fingerprint":
        s2 = tuple(map(int, a[a.index("--s2") + 1].split(":"))) if "--s2" in a else (0, 0)
        s6 = tuple(map(int, a[a.index("--s6") + 1].split(":"))) if "--s6" in a else (0, 0)
        cmd_fingerprint(a[2], s2, s6)
    elif a[1] == "compare":
        cmd_compare(a[2], a[3], a[4])
