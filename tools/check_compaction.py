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

Operations: edit (classes ref-subst, history-removal), replace-section (history-section,
history-appendix; tag_examples/navigation with a registered region), replace-header,
replace-footer, and move (class reorder: a whole block reinserted byte-identical before a
unique anchor inside the same section; added for RECOG v0.3.24 stage 2).

Profile key base_history_from (added for NUMGEN v1.21 stage 2): a study whose base keeps its version
history after the appendices under its own heading (e.g. "## Changelog", followed by legacy notes)
instead of in "## Appendix A" may declare that heading. The base's live text then ends at that
heading, as a base Appendix A region would. The heading must occur exactly once in the base as a
whole line, no live section heading ("## §") or appendix heading may follow it, and the whole
region must be removed by declared operations and found in a named archive (checked as
"base history region"). The key changes nothing when absent.

Profile key history_appendix (added for OFN v0.11 stage 2): the letter of the appendix that holds the
version history, when it is not Appendix A (OFN: "C"; its Appendix A holds historical scenarios). The
history region then runs from "## Appendix <letter>" to the next "## " heading or the footer, in base and
candidate alike; it is excluded from the live text, and a history-appendix operation must replace exactly
that appendix. Without the key the region is Appendix A, bounded by Appendix B, as before.
With the key (revision after the PR #113 receiving review): the heading "## Appendix <letter>" must occur
exactly once in base and candidate; exactly one history-appendix operation must remove exactly the base
region (plus, at most, the trailing rule and footer lines) and insert exactly the candidate region (plus
the same kind of tail), with no other "## " heading in its new text. A source hash that leaves the live
text passes only when the key is set and an operation that removes it declares it in "relocate_hashes"
and the history-appendix text carries it; without the key, hashes are protected as before.

RID pattern (OFN v0.11 stage 2): the programme namespaces `RTG-…` and `RTG-OFN-…` (Methodology v1.4 §4.2)
are tracked when an identifier has at least a category and a description (`RTG-OFN-DEF-X`, `RTG-OPEN-X-Y`);
the bare namespace word `RTG-OFN` is not an identifier.
"""
import argparse, hashlib, json, re, sys

# ---------------------------------------------------------------- vocabulary
STATUS = r"THM|ALG|DEF|NUM|CAND|HYP|HEUR|SPEC|INTERP|OPEN|FAIL|RETRACTED|COR|ENG|OBS|RESULT|SESSION|THM-ALG via IA|ALG via IA"
RE_STATUS = re.compile(r"`\[(?:%s)\]`" % STATUS)
RE_QUAL = re.compile(r"`\[(?:scope|assuming|conv|family|import|proof|target|from|provenance|cert):[^`]*\]`")
RE_RID = re.compile(r"(?<![A-Z]-)\b(?:RTG-[A-Z0-9]+-[A-Z0-9](?:[A-Z0-9-]*[A-Z0-9])?|(?:DYAD|RECOG|GEN|TRIAD|NUMGEN|OFN|UVM|RRF|DZT|AZ|TDRG|LEG|PRE|FMS|RER|ERB|PROG|OPENM)-[A-Z0-9][A-Z0-9-]*[A-Z0-9])\b")
RE_MATH = re.compile(r"\$\$.+?\$\$|\$[^$\n]+\$", re.S)
RE_HASH = re.compile(r"\b[0-9a-f]{64}\b|\b[0-9a-f]{8}…[0-9a-f]{4}\b")
RE_ANCHOR = re.compile(r"\{#[A-Za-z0-9_-]+\}")
RE_TAGREF = re.compile(r"`(?:[a-z0-9]+-v[0-9][0-9.]*(?:-r[0-9]+)?)`")
RE_APPREF = re.compile(r"Appendix ([A-Z])\b")
RE_HLABEL = re.compile(r"\bH-(?:P2-)?\d+\b")
HISTORY_WORDS = ("relocated", "text:", "wording:", "paragraph:", "former", "historical", "superseded", "v6.", "v5.")
# words whose silent removal narrows or widens a statement
PROTECTED_WORDS = re.compile(r"\b(?:assuming|conditional|unless|only if|pending|requires|restricted|not established)\b", re.I)

# A reference substitution may change only reference text: these tokens and punctuation.
REF_WORDS = {"Appendix", "of", "in", "the", "to", "its", "version", "history", "relocated", "list", "lists",
             "below", "tag", "tagged", "edition", "normalization", "map", "Local", "Tag", "Aliases", "See",
             "see", "COR", "items", "and", "at"}
RE_REF_TOKEN = re.compile(r"`[a-z0-9]+-v[0-9][0-9.]*(?:-r[0-9]+)?`|H-(?:P2-)?\d+|v\d+(?:\.\d+)*|[A-G]\b|[A-Za-z]+|[()\[\],;:.*\s–-]")

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
    """header | body (live) | history appendix. Returns dict of (start, end) offsets.
    The history appendix is Appendix A bounded by Appendix B (default), or the appendix named by the
    profile key history_appendix, bounded by the next '## ' heading or the footer line."""
    first_rule = s.index("\n## ")
    x = PROFILE.get("history_appendix")
    if not x:
        a = s.find("\n## Appendix A")
        b = s.find("\n## Appendix B")
        return {"header": (0, first_rule), "appA": (a, b) if a >= 0 and b > a else None}
    heads = history_heads(s, x)
    if len(heads) != 1:
        return {"header": (0, first_rule), "appA": None}
    a = heads[0] - 1
    nxt = s.find("\n## ", a + 1)
    m = re.search(r"^\*END OF DOCUMENT", s[a + 1:], re.M)
    ends = [e for e in (nxt, (a + 1 + m.start() - 1) if m else -1) if e >= 0]
    return {"header": (0, first_rule), "appA": (a, min(ends) if ends else len(s))}


def history_heads(s, x):
    """Offsets of the lines '## Appendix <x>' (followed by a space, a dash or end of line)."""
    return [m.start() for m in re.finditer(r"^## Appendix %s(?=[ \u2014\u2013-]|$)" % re.escape(x), s, re.M)]


def is_tail(t):
    """Only blank lines and horizontal rules, then (optionally) the footer block: the line
    '*END OF DOCUMENT…' and whatever follows it to the end of the file (a base footer may span lines)."""
    lines = t.split("\n")
    for i, l in enumerate(lines):
        if FOOTER.match(l):
            return not any(x.startswith("#") or RE_STATUS.search(x) or RE_RID.search(x) for x in lines[i:])
        if l.strip() and l.strip() != "---":
            return False
    return True


def check_history_appendix(base, cand, mp):
    """Profile key history_appendix: the history region is unique and the declared operation replaces exactly it."""
    x = PROFILE["history_appendix"]
    nb, nc = len(history_heads(base, x)), len(history_heads(cand, x))
    if nb != 1 or nc != 1:
        return False, f"heading '## Appendix {x}' occurs {nb} times in the base and {nc} times in the candidate (exactly once each required)"
    ops = [op for op in mp["operations"] if op.get("class") == "history-appendix"]
    if len(ops) != 1:
        return False, f"{len(ops)} history-appendix operations (exactly one required)"
    op = ops[0]
    rb, rc = split_regions(base)["appA"], split_regions(cand)["appA"]
    region_b, region_c = base[rb[0] + 1:rb[1]], cand[rc[0] + 1:rc[1]]
    removed, new = op.get("_removed", ""), op.get("new", "")
    if not removed.startswith(region_b) or not is_tail(removed[len(region_b):]):
        return False, "the history-appendix operation does not remove exactly the base history region (beyond it only rule and footer lines may go)"
    if not new.startswith(region_c) or not is_tail(new[len(region_c):]):
        return False, "the history-appendix operation does not insert exactly the candidate history region"
    heads = [l for l in new.split("\n") if l.startswith("## ")]
    if len(heads) != 1 or not re.match(r"## Appendix %s(?=[ \u2014\u2013-]|$)" % re.escape(x), heads[0]):
        return False, f"the new history text carries headings other than its own: {heads[:3]}"
    return True, f"Appendix {x} is the unique history region in base and candidate; operation {op['id']} replaces exactly it"


def base_history_start(s):
    """Offset of the declared base history heading (profile key base_history_from), or -1."""
    h = PROFILE.get("base_history_from")
    if not h or s is not BASE_TEXT:
        return -1
    i = s.find("\n" + h + "\n")
    return i


def live_text(s):
    r = split_regions(s)
    h_end = r["header"][1]
    cut = base_history_start(s)
    if cut >= 0:
        s = s[:cut + 1]
    t = s[h_end:]
    if r["appA"] and r["appA"][1] <= len(s):
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
        res = "PENDING" if ok == "PENDING" else ("PASS" if ok is True else "FAIL")
        self.items.append({"check": name, "result": res, "detail": detail})
        return ok

    @property
    def ok(self):
        return all(i["result"] == "PASS" for i in self.items)

    @property
    def failed(self):
        return any(i["result"] == "FAIL" for i in self.items)


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
        elif k == "move":
            # byte-preserving reorder of one whole block inside the live text: the block (exactly once in the
            # base, bounded by blank lines) is cut and reinserted, byte-identical, before a unique anchor that
            # itself starts a block. Nothing else changes; prose is never rewritten.
            blk, anchor = op["block"], op["before"]
            n = s.count(blk)
            if n != 1:
                raise ValueError(f'{op["id"]}: block occurs {n} times in base')
            i = s.index(blk)
            if not (i == 0 or s[i - 2:i] == "\n\n") or s[i + len(blk):i + len(blk) + 2] != "\n\n":
                raise ValueError(f'{op["id"]}: block is not a whole blank-line-delimited block')
            s2 = s[:i] + s[i + len(blk) + 2:]
            m = s2.count(anchor)
            if m != 1:
                raise ValueError(f'{op["id"]}: anchor occurs {m} times after removal')
            j = s2.index(anchor)
            if not (j == 0 or s2[j - 2:j] == "\n\n"):
                raise ValueError(f'{op["id"]}: anchor does not start a block')
            s = s2[:j] + blk + "\n\n" + s2[j:]
            op["_moved"] = blk
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
    ap.add_argument("--report"); ap.add_argument("--regions", help="reviewed-regions registry (JSON)")
    a = ap.parse_args()
    try:
        base_b = open(a.base, "rb").read(); cand_b = open(a.candidate, "rb").read()
        mp = json.load(open(a.map, encoding="utf-8"))
        arch = load_archives(mp)
    except Exception as e:
        print("input error:", e); return 2
    base, cand = base_b.decode("utf-8"), cand_b.decode("utf-8")
    if a.regions:
        for r in json.load(open(a.regions, encoding="utf-8"))["regions"]:
            REGIONS[r["id"]] = r
    PROFILE.update(mp.get("profile", {}))
    global BASE_SECTION1, BASE_TEXT
    BASE_TEXT = base
    i = base.find("\n## §1.")
    BASE_SECTION1 = base[i:base.find("\n## ", i + 1)] if i >= 0 else ""
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
        res = "PENDING" if ok == "PENDING" else ("PASS" if ok is True else "FAIL")
        ops_report.append({"id": op["id"], "op": op["op"], "class": op.get("class"), "result": res, "detail": why})
        C.add(f'operation {op["id"]} ({op.get("class", op["op"])})', ok, why)
    rep["operations"] = ops_report

    # 3. qualified claim preservation (block level, live text)
    if PROFILE.get("base_history_from"):
        ok, why = check_base_history(base, cand, mp, arch)
        C.add("base history region", ok, why)
    if PROFILE.get("history_appendix"):
        ok, why = check_history_appendix(base, cand, mp)
        C.add("history appendix region", ok, why)
    lb, lc = live_text(BASE_TEXT), live_text(cand)
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
    # with history_appendix only: a hash may leave the live text if an operation that removes it declares it
    # ("relocate_hashes") and the history-appendix text carries it
    relocated, bad_decl = [], []
    if PROFILE.get("history_appendix"):
        hist_new = "".join(op.get("new", "") for op in mp["operations"] if op.get("class") == "history-appendix")
        for op in mp["operations"]:
            gone = op.get("_removed", "") if op["op"].startswith("replace") else (removed_part(op.get("old", ""), op.get("new", "")) or "")
            for h in op.get("relocate_hashes", []):
                if h in gone and h in hist_new and h in hb - hc:
                    relocated.append(h)
                else:
                    bad_decl.append(f"{op['id']}:{h}")
    lost = sorted(hb - hc - set(relocated))
    C.add("source hashes preserved in live text", not lost and not bad_decl,
          f"missing: {lost}" + (f"; declared relocations to the history appendix: {sorted(relocated)}" if relocated else "")
          + (f"; invalid relocation declarations: {bad_decl}" if bad_decl else ""))
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

    rep["profile"] = PROFILE
    rep["checks"] = C.items
    rep["warnings"] = WARNINGS
    rep["result"] = "FAIL" if C.failed else ("PASS" if C.ok else "PENDING")
    rep["limitations"] = [
        "Blocks are compared as bytes; equivalence of rewritten prose is not assessed (Methodology v1.4 §12.4).",
        "Claim tags, qualifiers, RIDs, math spans and hashes are found by regular expressions; LaTeX is not parsed.",
        "RID pattern covers the registered namespace prefixes listed in the script (RTG-… and RTG-OFN-… with category and description; DYAD, RECOG, GEN, TRIAD, NUMGEN, UVM, RRF, DZT, AZ, TDRG and the other listed prefixes); other identifiers (e.g. PL, L0L1, L2) are not tracked.",
        "History region: Appendix A bounded by Appendix B, or the appendix named by profile key history_appendix up to the next '## ' heading or the footer; it is excluded from the live text. With the key, its heading is unique in base and candidate, one history-appendix operation replaces exactly it, and hashes leave the live text only by declared relocation (relocate_hashes).",
        "Reference resolution: in the sentence of each tagged-edition pointer, H-labels (as '**H-n** —' definitions), 'Appendix X' headings, 'Local Tag Aliases' and version entries ('### vX') are looked up in the pinned archive; section numbers (§n.m) are not resolved.",
        "Reference substitutions may change only reference vocabulary (REF_WORDS, labels, versions, tags, punctuation); any other changed word fails.",
        "tag_examples/navigation relocations need a registered region (hash, kind) and a reviewer confirmation; unconfirmed regions give PENDING. In a tag_examples region an identifier may occur only inside a tag spelling in a table row (and must survive in the live text); a navigation region may carry no identifier and only [DEF] tags.",
        "An H-label resolves if the archive defines it ('**H-n** —') or defines its lettered group ('**H-na** —').",
        "Archive membership is a byte-substring test against the named archive files.",
        "Study profile (map key 'profile'): extra history words, extra reference words and the status-summary source (base header summary, optionally base §1) are calibration inputs declared in the map and printed in the report.",
        "A 'move' (class reorder) cuts one whole blank-line-delimited block and reinserts it byte-identical before a unique block-starting anchor inside the same section of the live text; it can change no text, tag, RID, math or hash (re-derivation and the block-multiset test).",
    ]
    if a.report:
        json.dump(rep, open(a.report, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for i in C.items:
        print(f'{i["result"]}  {i["check"]}' + (f'  — {i["detail"]}' if i["detail"] else ""))
    for w in WARNINGS:
        print("WARN ", w)
    print("RESULT:", rep["result"])
    return {"PASS": 0, "FAIL": 1, "PENDING": 3}[rep["result"]]


BASE_TEXT = ""


def enclosing_heading(s, blk):
    """The nearest markdown heading line (## or ###) preceding the block in s."""
    i = s.find(blk)
    if i < 0:
        return None
    head = s[:i]
    k = max(head.rfind("\n## "), head.rfind("\n### "))
    if k < 0:
        return None
    return head[k + 1:head.index("\n", k + 1)]


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
            so, sn = changed_spans(old, new)
            for span in (so, sn):
                bad = ref_grammar_violations(span)
                if bad:
                    return False, f"changed text is not reference text: {span[:100]!r} (offending: {bad[:5]})"
            fo, fn = features(old), features(new)
            if fo != fn:
                return False, f"load-bearing features changed: {diff_feat(fo, fn)}"
            if PROTECTED_WORDS.findall(old) != PROTECTED_WORDS.findall(new):
                return False, "qualifying words changed"
            if not (RE_TAGREF.search(new) or RE_APPREF.search(new) or "release record" in new):
                return False, "replacement names no resolvable target"
            return True, f"reference substitution only ({so!r} → {sn!r})"
        if cls == "history-removal":
            removed = removed_part(old, new)
            if removed is None:
                return False, "new text is not old text with one span removed"
            if RE_STATUS.search(removed) or RE_QUAL.search(removed) or RE_RID.search(removed) or RE_MATH.search(removed):
                return False, f"removed span carries a claim tag, qualifier, RID or math: {removed[:120]!r}"
            if PROTECTED_WORDS.search(removed):
                return False, f"removed span carries a qualifying word: {removed[:120]!r}"
            if not any(w in removed for w in HISTORY_WORDS + tuple(PROFILE.get("history_words", []))):
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
        if op.get("tag_examples") or op.get("navigation"):
            ok, why = check_region(op, removed, rids)
            if ok is not True:
                return ok, why
        lost = sorted(r for r in rids if r not in live_text(cand))
        if lost and cls != "history-appendix":
            return False, f"live identifiers lost with the section: {lost[:8]}"
        if cls == "history-section" and RE_STATUS.search(removed) and not (op.get("tag_examples") or op.get("navigation")):
            return False, "section carries claim tags; a live result cannot be relocated"
        if cls == "history-appendix":
            x = PROFILE.get("history_appendix")
            if x and not op.get("start", "").startswith("## Appendix %s" % x):
                return False, f"history-appendix operation does not replace the declared history appendix {x}"
            # identifiers named in the new history text must exist in the live text
            missing = sorted(r for r in set(RE_RID.findall(new)) if r not in live_text(cand))
            if missing:
                return False, f"history entry names identifiers absent from the live text: {missing}"
        elif RE_STATUS.search(new) or RE_MATH.search(new):
            return False, "pointer text carries claim tags or math"
        note = ""
        if op.get("tag_examples") or op.get("navigation"):
            note = f"; reviewed region {op.get('region')} confirmed by {REGIONS[op['region']]['confirmed_by']}"
        return True, f"section relocated ({len(removed)} chars), found in {names}{note}"
    if k == "replace-header":
        removed = op.get("_removed", "")
        if not in_archive(removed, arch, names):
            return False, "old header not found in archive"
        old_sum = summary_field(removed); new_sum = field(op["new"], "Status summary")
        if new_sum is None:
            return False, "no Status summary"
        if old_sum is None:
            return False, "base header has no status summary"
        pool = [old_sum]
        src = PROFILE.get("summary_from", ["header"])
        if "section1" in src:
            pool.append(BASE_SECTION1)
        extra = [x for x in sentences(new_sum) if not any(x in p for p in pool)]
        if extra:
            return False, f"status summary adds text not in the base summary ({'/'.join(src)}): {extra[:2]}"
        return True, f"header replaced; status-summary sentences are a subset of the base summary ({'/'.join(src)})"
    if k == "move":
        blk = op["block"]
        if cls != "reorder":
            return False, "a move must be of class reorder"
        if op.get("new") is not None or op.get("old") is not None:
            return False, "a move carries no old/new text"
        lb, lc = live_text(BASE_TEXT), live_text(cand)
        if lb.count(blk) != 1 or lc.count(blk) != 1:
            return False, "moved block must occur exactly once in the live text of base and candidate"
        if blk in BASE_TEXT[:split_regions(BASE_TEXT)["header"][1]] or blk in cand[:split_regions(cand)["header"][1]]:
            return False, "moved block lies in the header"
        hb, hc = enclosing_heading(BASE_TEXT, blk), enclosing_heading(cand, blk)
        if hb != hc or not hb:
            return False, f"moved block changes section ({hb!r} -> {hc!r}); a reorder stays inside its section"
        if blocks(lb) != blocks(lc) and sorted(blocks(lb)) != sorted(blocks(lc)):
            return False, "block multiset of the live text changed"
        return True, f"block reordered inside {hb!r} ({len(blk)} chars, byte-identical)"
    if k == "replace-footer":
        if not in_archive(op.get("_removed", "").strip(), arch, names):
            return False, "old footer not found in archive"
        return True, "footer replaced"
    return False, "unknown operation"


REGIONS = {}


def check_base_history(base, cand, mp, arch):
    """Validate a declared base history region (profile key base_history_from)."""
    h = PROFILE["base_history_from"]
    if not h.startswith("## ") or base.count("\n" + h + "\n") != 1:
        return False, f"declared base history heading {h!r} is not a unique '## ' line of the base"
    i = base.index("\n" + h + "\n") + 1
    region = base[i:]
    later = [l for l in region.split("\n")[1:] if l.startswith("## ")]
    bad = [l for l in later if l.startswith("## §") or l.startswith("## Appendix")]
    if bad:
        return False, f"live or appendix headings follow the declared history heading: {bad[:3]}"
    if h in cand:
        return False, "the declared history heading survives in the candidate"
    covered = any(op["op"] == "replace-section" and region in op.get("_removed", "") for op in mp["operations"])
    if not covered:
        return False, "the base history region is not removed by a declared replace-section"
    names = [n for op in mp["operations"] if op["op"] == "replace-section" for n in (op.get("archive") or [])]
    if not in_archive(region, arch, names):
        return False, "the base history region is not found byte-identical in a named archive"
    return True, f"base live text ends at {h!r}; region of {len(region)} chars relocated and archived"

# Study profile (map key "profile"; Methodology v1.4 §13.6 calibration). Defaults reproduce the DYAD pilot.
#   history_words  extra markers that identify a removed span as history (history-removal)
#   ref_words      extra words allowed in a reference substitution
#   checked_tag_prefixes, known_tags  tag pointers with these prefixes must name an archive or a known tag
#   summary_from   ["header"] (default) or ["header", "section1"]: where the candidate's status-summary
#                  sentences may come from (base header summary; base §1 text, which the block checks cover)
PROFILE = {}


def check_region(op, removed, rids):
    """tag_examples / navigation are allowed only for a registered, structurally checked,
    reviewer-confirmed source region whose bytes match its registered hash."""
    rid = op.get("region")
    if not rid or rid not in REGIONS:
        return False, "tag_examples/navigation requires a registered region (regions file)"
    r = REGIONS[rid]
    kind = "tag_examples" if op.get("tag_examples") else "navigation"
    if r.get("kind") != kind:
        return False, f"region {rid} is registered as {r.get('kind')}, not {kind}"
    if sha(removed) != r.get("sha256"):
        return False, f"region {rid}: removed bytes do not match the registered hash"
    for x in rids:
        for l in removed.split("\n"):
            if x not in l:
                continue
            outside = re.sub(r"`\[[^`]*\]`", "", l)
            if not l.startswith("|") or x in outside:
                return False, f"region {rid}: identifier {x} occurs outside a tag spelling in a table row; a region carrying results cannot be relocated"
    if "$$" in removed:
        return False, f"region {rid} contains display math"
    if kind == "tag_examples":
        stray = [l for l in removed.split("\n") if RE_STATUS.search(l) and not l.startswith("|")]
        if stray:
            return False, f"region {rid}: claim tags outside table rows: {stray[0][:100]!r}"
    else:
        if not set(RE_STATUS.findall(removed)) <= {"`[DEF]`"}:
            return False, f"region {rid}: navigation region carries non-[DEF] tags"
    if not r.get("confirmed_by"):
        return "PENDING", f"region {rid} structurally eligible; reviewer confirmation pending"
    return True, ""


def changed_spans(old, new):
    """Minimal differing spans of old/new, widened to word boundaries."""
    i = 0
    while i < min(len(old), len(new)) and old[i] == new[i]:
        i += 1
    j = 0
    while j < min(len(old), len(new)) - i and old[-1 - j] == new[-1 - j]:
        j += 1
    while i > 0 and old[i - 1].isalnum():
        i -= 1
    while j > 0 and old[len(old) - j].isalnum():
        j -= 1
    return old[i:len(old) - j], new[i:len(new) - j]


def ref_grammar_violations(span):
    bad, pos = [], 0
    for m in RE_REF_TOKEN.finditer(span):
        if m.start() != pos:
            bad.append(span[pos:m.start()])
        t = m.group(0)
        if t.isalpha() and len(t) > 1 and t not in REF_WORDS and t not in PROFILE.get("ref_words", []):
            bad.append(t)
        pos = m.end()
    if pos != len(span):
        bad.append(span[pos:])
    return bad


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


def summary_field(h):
    """The base status summary: '**Status summary:**', else the first (newest) '**Status summary (…):**'."""
    v = field(h, "Status summary")
    if v is not None:
        return v
    m = re.search(r"^\*\*Status summary \([^)]*\):\*\*\s*(.*)$", h, re.M)
    return m.group(1).strip() if m else None


BASE_SECTION1 = ""


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
    resolved = 0
    for m in RE_TAGREF.finditer(lt):
        t = m.group(0).strip("`")
        pref = ("dyad-",) + tuple(PROFILE.get("checked_tag_prefixes", []))
        if t.startswith(pref) and t not in arch and t not in KNOWN_TAGS and t not in PROFILE.get("known_tags", []):
            bad.append(f"unknown tag {t}"); continue
        if t not in arch:
            continue
        at = arch[t]["text"]
        ctx = sentence_at(lt, m.start())
        for h in RE_HLABEL.findall(ctx):
            resolved += 1
            if f"**{h}** —" not in at and not re.search(r"\*\*%s[a-z]\*\* —" % re.escape(h), at):
                bad.append(f"{h} not defined in {t}")
        for x in RE_APPREF.findall(ctx):
            resolved += 1
            if f"\n## Appendix {x} " not in at:
                bad.append(f"Appendix {x} not in {t}")
        if "Local Tag Aliases" in ctx:
            resolved += 1
            if "\n## Local Tag Aliases" not in at:
                bad.append(f"Local Tag Aliases not in {t}")
        own = t.split("-v", 1)[1]
        for v in re.findall(r"\bv(\d+(?:\.\d+)+)\b", ctx):
            if v == own:
                continue
            resolved += 1
            if not re.search(r"^### v%s\b" % re.escape(v), at, re.M):
                bad.append(f"v{v} has no Appendix {PROFILE.get('history_appendix', 'A')} entry in {t}")
    return (not bad), ("; ".join(bad[:6]) if bad else f"Appendix references, H-labels and tags resolve; {resolved} archive targets found in the pinned archive")


def sentence_at(t, i):
    a = max(t.rfind(". ", 0, i), t.rfind("\n", 0, i)) + 1
    b_candidates = [x for x in (t.find(". ", i), t.find("\n", i)) if x >= 0]
    b = min(b_candidates) if b_candidates else len(t)
    return t[a:b]


WARNINGS = []
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
        WARNINGS.append("Document status longer than 60 words (advisory; no size gate)")
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
