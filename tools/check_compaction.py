#!/usr/bin/env python3
"""Mechanical-preservation checker for a DSN compaction change (Methodology v1.4 §13.6).

    check_compaction.py BASE CANDIDATE MAP [--report OUT.json]

BASE      the corrected intermediate (stage-1 output), not the adopted predecessor.
CANDIDATE the compacted file.
MAP       the movement map (JSON) that declares every change. Archives named in the map
          ("path": a file, or "git": "<tag>:<path>" read with git show from the current
          directory) hold the bytes of everything removed.

The checker re-derives the candidate from BASE + MAP and requires byte equality, so
no undeclared change can pass. It then checks each declared operation against its
class rules (qualified claim preservation, removal accounting, integrity,
presentation). Exit 0 = PASS, 1 = FAIL, 2 = usage or input error.

It does not prove mathematical truth or the semantic equivalence of rewritten prose
(§12.4). Parser limits are listed in the report.
"""
import argparse, hashlib, json, re, sys

# ---------------------------------------------------------------- vocabulary
STATUS = r"THM|ALG|DEF|NUM|CAND|HYP|HEUR|SPEC|INTERP|OPEN|FAIL|RETRACTED|COR|ENG|OBS|RESULT|SESSION|THM-ALG via IA|ALG via IA"
RE_STATUS = re.compile(r"`\[(?:%s)\]`" % STATUS)
RE_QUAL = re.compile(r"`\[(?:scope|assuming|conv|family|import|proof|target|from|provenance|cert):[^`]*\]`")
RE_RID = re.compile(r"(?<![A-Z]-)\b(?:DYAD|RECOG|GEN|TRIAD|NUMGEN|OFN|UVM|RRF|DZT|AZ|TDRG|LEG|PRE|FMS|RER|ERB|PROG|OPENM)-[A-Z0-9][A-Z0-9-]*[A-Z0-9]\b")
RE_MATH = re.compile(r"\$\$.+?\$\$|\$[^$\n]+\$", re.S)
RE_HASH = re.compile(r"\b[0-9a-f]{64}\b|\b[0-9a-f]{8}…[0-9a-f]{4}\b")
RE_ANCHOR = re.compile(r"\{#[A-Za-z0-9_-]+\}")
RE_TAGREF = re.compile(r"`(?:[a-z0-9]+-v[0-9][0-9.]*(?:-r[0-9]+)?)`")
RE_APPREF = re.compile(r"Appendix ([A-Z])\b")
RE_HLABEL = re.compile(r"\bH-(?:P2-)?\d+\b")
HISTORY_WORDS = ("relocated", "text:", "wording:", "paragraph:", "former", "historical", "superseded", "v6.", "v5.")
# words whose silent removal narrows or widens a statement
PROTECTED_WORDS = re.compile(r"\b(?:assuming|conditional|unless|only if|pending|requires|restricted|not established)\b", re.I)

FOOTER = re.compile(r"^\*END OF DOCUMENT")
HEADER_FIELDS = ["Title", "Date", "Scope", "Document class", "Document status", "Supersedes",
                 "Companion documents", "DSN Methodology", "Status summary"]


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()


def features(t):
    """Load-bearing features of a text span: claim tags, qualifiers, RIDs, math, hashes."""
    return {
        "status": sorted(RE_STATUS.findall(t)),
        "qual": sorted(RE_QUAL.findall(t)),
        "rid": sorted(RE_RID.findall(t)),
        "math": sorted(m.group(0) for m in RE_MATH.finditer(t)),
        "hash": sorted(RE_HASH.findall(t)),
    }


def split_regions(s):
    """header | body (live) | appendix A (history). Returns dict of (start, end) offsets."""
    first_rule = s.index("\n## ")
    a = s.find("\n## Appendix A")
    b = s.find("\n## Appendix B")
    return {"header": (0, first_rule), "appA": (a, b) if a >= 0 and b > a else None}


def live_text(s):
    r = split_regions(s)
    h_end = r["header"][1]
    t = s[h_end:]
    if r["appA"]:
        a, b = r["appA"]
        t = s[h_end:a] + s[b:]
    return "\n".join(l for l in t.split("\n") if not FOOTER.match(l))


def blocks(t):
    """Paragraph blocks; each table row and list item is its own block."""
    out, cur = [], []
    for line in t.split("\n"):
        if not line.strip():
            if cur:
                out.append("\n".join(cur)); cur = []
            continue
        if line.startswith("|") or re.match(r"^\s*[-*] |^\s*\d+\. ", line) or line.startswith("#"):
            if cur:
                out.append("\n".join(cur)); cur = []
            out.append(line)
        else:
            cur.append(line)
    if cur:
        out.append("\n".join(cur))
    return out


def is_claim_block(b):
    return bool(RE_STATUS.search(b) or RE_RID.search(b))


class Check:
    def __init__(self):
        self.items = []

    def add(self, name, ok, detail=""):
        self.items.append({"check": name, "result": "PASS" if ok else "FAIL", "detail": detail})
        return ok

    @property
    def ok(self):
        return all(i["result"] == "PASS" for i in self.items)


def load_archives(mp):
    arch = {}
    for a in mp.get("archives", []):
        if a.get("git") and not a.get("path"):
            import subprocess
            data = subprocess.run(["git", "show", a["git"]], capture_output=True, check=True).stdout
        else:
            data = open(a["path"], "rb").read()
        arch[a["name"]] = {"text": data.decode("utf-8"), "sha256": sha(data), "declared": a.get("sha256")}
    return arch


def apply_ops(base, mp):
    """Re-derive the candidate from the base and the declared operations."""
    s = base
    log = []
    for op in mp["operations"]:
        k = op["op"]
        if k in ("edit",):
            n = s.count(op["old"])
            if n != 1:
                raise ValueError(f'{op["id"]}: old text occurs {n} times in base')
            s = s.replace(op["old"], op["new"])
        elif k == "replace-section":
            i = s.find(op["start"])
            j = s.find(op["end"], i + len(op["start"])) if op.get("end") else len(s)
            if i < 0 or j < 0 or s.count(op["start"]) != 1:
                raise ValueError(f'{op["id"]}: section bounds not found uniquely')
            op["_removed"] = s[i:j]
            s = s[:i] + op["new"] + s[j:]
        elif k == "replace-header":
            r = split_regions(s)["header"]
            op["_removed"] = s[r[0]:r[1]]
            s = op["new"] + s[r[1]:]
        elif k == "replace-footer":
            lines = s.split("\n")
            idx = [n for n, l in enumerate(lines) if FOOTER.match(l)]
            if not idx:
                raise ValueError("no footer in base")
            i = idx[0]
            op["_removed"] = "\n".join(lines[i:])
            s = "\n".join(lines[:i]) + "\n" + op["new"]
        else:
            raise ValueError(f'{op["id"]}: unknown op {k}')
        log.append(op["id"])
    return s, log


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("candidate"); ap.add_argument("map")
    ap.add_argument("--report")
    a = ap.parse_args()
    try:
        base_b = open(a.base, "rb").read(); cand_b = open(a.candidate, "rb").read()
        mp = json.load(open(a.map, encoding="utf-8"))
        arch = load_archives(mp)
    except Exception as e:
        print("input error:", e); return 2
    base, cand = base_b.decode("utf-8"), cand_b.decode("utf-8")
    C = Check()
    rep = {"base_sha256": sha(base_b), "candidate_sha256": sha(cand_b), "map_sha256": sha(open(a.map, "rb").read())}

    # 0. identities
    C.add("base identity", mp.get("base_sha256") == rep["base_sha256"], "map base_sha256 vs file")
    C.add("candidate identity", mp.get("candidate_sha256") == rep["candidate_sha256"], "map candidate_sha256 vs file")
    for n, v in arch.items():
        C.add(f"archive identity {n}", v["declared"] == v["sha256"], v["sha256"])

    # 1. mechanical scope: re-derive candidate exactly
    try:
        derived, _ = apply_ops(base, mp)
        same = derived == cand
        detail = "candidate equals base + declared operations" if same else first_diff(derived, cand)
        C.add("mechanical scope (re-derivation)", same, detail)
    except ValueError as e:
        C.add("mechanical scope (re-derivation)", False, str(e))
        derived = None

    # 2. per-operation class rules
    ops_report = []
    for op in mp["operations"]:
        ok, why = check_op(op, arch, cand)
        ops_report.append({"id": op["id"], "op": op["op"], "class": op.get("class"), "result": "PASS" if ok else "FAIL", "detail": why})
        C.add(f'operation {op["id"]} ({op.get("class", op["op"])})', ok, why)
    rep["operations"] = ops_report

    # 3. qualified claim preservation (block level, live text)
    lb, lc = live_text(base), live_text(cand)
    bb, cb = blocks(lb), set(blocks(lc))
    edited_old = {}
    for op in mp["operations"]:
        if op["op"] == "edit":
            edited_old[op["id"]] = op["old"]
    claim = [b for b in bb if is_claim_block(b)]
    kept = [b for b in claim if b in cb]
    touched = [b for b in claim if b not in cb]
    unexplained = []
    for b in touched:
        # a touched claim block must be covered by a declared edit inside it, or lie in a replaced section
        cov = any(o in b or b in o for o in edited_old.values()) or any(
            b in op.get("_removed", "") for op in mp["operations"] if op["op"].startswith("replace"))
        if not cov:
            unexplained.append(b[:160])
    C.add("qualified claim blocks", not unexplained,
          f"{len(claim)} claim blocks in base live text: {len(kept)} byte-identical, {len(touched)-len(unexplained)} changed by declared operations, {len(unexplained)} unexplained")
    rep["claim_blocks"] = {"base": len(claim), "identical": len(kept), "declared_change": len(touched) - len(unexplained), "unexplained": unexplained}

    # 4. integrity
    rb, rc = set(RE_RID.findall(lb)), set(RE_RID.findall(lc))
    C.add("RID set preserved in live text", rb <= rc, f"missing: {sorted(rb - rc)}")
    ab, ac = heading_anchors(base), heading_anchors(cand)
    C.add("heading anchors preserved", ab <= ac, f"missing: {sorted(ab - ac)}")
    hb, hc = set(RE_HASH.findall(lb)), set(RE_HASH.findall(lc))
    C.add("source hashes preserved in live text", hb <= hc, f"missing: {sorted(hb - hc)}")
    qb, qc = sorted(RE_QUAL.findall(lb)), sorted(RE_QUAL.findall(lc))
    lost_q = multiset_minus(qb, qc)
    allowed_q = []
    for op in mp["operations"]:
        if op["op"] == "replace-section" and op.get("tag_examples"):
            allowed_q += RE_QUAL.findall(op.get("_removed", ""))
    C.add("qualifier tags preserved", not multiset_minus(lost_q, allowed_q), f"lost: {multiset_minus(lost_q, allowed_q)}")
    ok, why = check_links(cand, arch)
    C.add("references resolve", ok, why)

    # 5. presentation
    ok, why = check_presentation(cand, mp)
    C.add("presentation (header, footer)", ok, why)

    rep["checks"] = C.items
    rep["result"] = "PASS" if C.ok else "FAIL"
    rep["limitations"] = [
        "Blocks are compared as bytes; equivalence of rewritten prose is not assessed (Methodology v1.4 §12.4).",
        "Claim tags, qualifiers, RIDs, math spans and hashes are found by regular expressions; LaTeX is not parsed.",
        "RID pattern covers the registered namespace prefixes listed in the script; other identifiers are not tracked.",
        "Reference resolution covers 'Appendix X', H-labels and repository tags; section numbers (§n.m) are not resolved.",
        "Archive membership is a byte-substring test against the named archive files.",
    ]
    if a.report:
        json.dump(rep, open(a.report, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for i in C.items:
        print(f'{i["result"]}  {i["check"]}' + (f'  — {i["detail"]}' if i["detail"] else ""))
    print("RESULT:", rep["result"])
    return 0 if C.ok else 1


def heading_anchors(s):
    return {a for l in s.split("\n") if l.startswith("#") for a in RE_ANCHOR.findall(l)}


def multiset_minus(a, b):
    b = list(b); out = []
    for x in a:
        if x in b:
            b.remove(x)
        else:
            out.append(x)
    return out


def first_diff(x, y):
    n = next((i for i, (p, q) in enumerate(zip(x, y)) if p != q), min(len(x), len(y)))
    ln = x.count("\n", 0, n) + 1
    return f"first difference at line {ln}: derived {x[n:n+80]!r} / candidate {y[n:n+80]!r}"


def in_archive(text, arch, names):
    return any(text in arch[n]["text"] for n in names if n in arch)


def check_op(op, arch, cand):
    k, cls = op["op"], op.get("class")
    names = op.get("archive", [])
    if isinstance(names, str):
        names = [names]
    if k == "edit":
        old, new = op["old"], op["new"]
        if cls == "ref-subst":
            fo, fn = features(old), features(new)
            if fo != fn:
                return False, f"load-bearing features changed: {diff_feat(fo, fn)}"
            if PROTECTED_WORDS.findall(old) != PROTECTED_WORDS.findall(new):
                return False, "qualifying words changed"
            if not (RE_TAGREF.search(new) or RE_APPREF.search(new) or "release record" in new):
                return False, "replacement names no resolvable target"
            return True, "reference substitution; claim features unchanged"
        if cls == "history-removal":
            removed = removed_part(old, new)
            if removed is None:
                return False, "new text is not old text with one span removed"
            if RE_STATUS.search(removed) or RE_QUAL.search(removed) or RE_RID.search(removed) or RE_MATH.search(removed):
                return False, f"removed span carries a claim tag, qualifier, RID or math: {removed[:120]!r}"
            if PROTECTED_WORDS.search(removed):
                return False, f"removed span carries a qualifying word: {removed[:120]!r}"
            if not any(w in removed for w in HISTORY_WORDS):
                return False, f"removed span is not marked as history: {removed[:120]!r}"
            if not in_archive(removed.strip(), arch, names):
                return False, "removed span not found byte-identical in the named archive"
            return True, f"history span removed ({len(removed)} chars), found in {names}"
        return False, f"unknown edit class {cls}"
    if k == "replace-section":
        removed, new = op.get("_removed", ""), op["new"]
        if not removed:
            return False, "section bounds not resolved"
        if not in_archive(removed, arch, names):
            return False, "removed section not found byte-identical in the named archive"
        rids = set(RE_RID.findall(removed))
        lost = sorted(r for r in rids if r not in live_text(cand))
        if lost and cls != "history-appendix":
            return False, f"live identifiers lost with the section: {lost[:8]}"
        if cls == "history-section" and RE_STATUS.search(removed) and not op.get("tag_examples"):
            only_def = set(RE_STATUS.findall(removed)) <= {"`[DEF]`"}
            if not (op.get("navigation") and only_def and not rids):
                return False, "section carries claim tags; a live result cannot be relocated"
        if cls == "history-appendix":
            # identifiers named in the new history text must exist in the live text
            missing = sorted(r for r in set(RE_RID.findall(new)) if r not in live_text(cand))
            if missing:
                return False, f"history entry names identifiers absent from the live text: {missing}"
        elif RE_STATUS.search(new) or RE_MATH.search(new):
            return False, "pointer text carries claim tags or math"
        note = " (claim tags present only as notation examples; declared)" if op.get("tag_examples") else ""
        if op.get("navigation"):
            note = f" (navigation section: only [DEF] tags, no identifiers, {len(RE_MATH.findall(removed))} symbol mentions; declared)"
        return True, f"section relocated ({len(removed)} chars), found in {names}{note}"
    if k == "replace-header":
        removed = op.get("_removed", "")
        if not in_archive(removed, arch, names):
            return False, "old header not found in archive"
        old_sum = field(removed, "Status summary"); new_sum = field(op["new"], "Status summary")
        if new_sum is None:
            return False, "no Status summary"
        extra = [x for x in sentences(new_sum) if x not in old_sum]
        if extra:
            return False, f"status summary adds text not in the base summary: {extra[:2]}"
        return True, "header replaced; status-summary sentences are a subset of the base summary"
    if k == "replace-footer":
        if not in_archive(op.get("_removed", "").strip(), arch, names):
            return False, "old footer not found in archive"
        return True, "footer replaced"
    return False, "unknown operation"


def removed_part(old, new):
    """If new == old with one contiguous span deleted, return that span."""
    if len(new) >= len(old):
        return None
    i = 0
    while i < len(new) and old[i] == new[i]:
        i += 1
    j = 0
    while j < len(new) - i and old[-1 - j] == new[-1 - j]:
        j += 1
    if i + j != len(new):
        return None
    return old[i:len(old) - j]


def diff_feat(a, b):
    return {k: {"-": multiset_minus(a[k], b[k]), "+": multiset_minus(b[k], a[k])} for k in a if a[k] != b[k]}


def field(h, name):
    m = re.search(r"^\*\*%s:\*\*\s*(.*)$" % re.escape(name), h, re.M)
    return m.group(1).strip() if m else None


def sentences(t):
    return [x.strip() for x in re.split(r"(?<=[.;])\s+(?=[A-Z`$(])", t) if x.strip()]


def check_links(cand, arch):
    bad = []
    apps = set(re.findall(r"^## Appendix ([A-Z])\b", cand, re.M))
    lt = live_text(cand)
    for m in RE_APPREF.finditer(lt):
        ctx = lt[max(0, m.start() - 60):m.end() + 60]
        if m.group(1) not in apps and not RE_TAGREF.search(ctx):
            bad.append(f"Appendix {m.group(1)} (no such appendix): {ctx!r}")
    for m in RE_HLABEL.finditer(lt):
        ctx = lt[max(0, m.start() - 160):m.end() + 40]
        if not RE_TAGREF.search(ctx):
            bad.append(f"{m.group(0)} without a tagged edition: {ctx!r}")
    for m in RE_TAGREF.finditer(cand):
        t = m.group(0).strip("`")
        if t.startswith("dyad-") and t not in arch and t not in KNOWN_TAGS:
            bad.append(f"unknown tag {t}")
    return (not bad), ("; ".join(bad[:6]) if bad else "Appendix references, H-labels and tags resolve")


KNOWN_TAGS = {"dyad-v6.4.19", "dyad-v6.4.20", "methodology-v1.3", "methodology-v1.4"}


def check_presentation(cand, mp):
    probs = []
    head = cand[:split_regions(cand)["header"][1]]
    for f in HEADER_FIELDS:
        v = field(head, f)
        if v is None:
            probs.append(f"missing header field {f}")
    sup = field(head, "Supersedes") or ""
    if len(re.findall(r"[0-9a-f]{64}", sup)) != 1 or sup.count("RTG_") != 1:
        probs.append("Supersedes must name exactly one predecessor with one full hash")
    if re.search(r"History —|previous status|r\d+\.\d+ was", head):
        probs.append("history text in header")
    st = field(head, "Document status") or ""
    if len(st.split()) > 60:
        probs.append("Document status longer than 60 words")
    feet = [l for l in cand.split("\n") if FOOTER.match(l)]
    if len(feet) != 1:
        probs.append(f"{len(feet)} footer lines (exactly one required)")
    tail = cand.split("\n")
    i = next((n for n, l in enumerate(tail) if FOOTER.match(l)), None)
    if i is not None and any(l.strip() for l in tail[i + 1:]):
        probs.append("text after the footer line")
    return (not probs), ("; ".join(probs) if probs else "required fields present; one predecessor; one footer")


if __name__ == "__main__":
    sys.exit(main())
