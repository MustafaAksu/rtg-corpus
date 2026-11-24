#!/usr/bin/env python3
"""OFN receiving pass (Claude co-owner, 24 Nov 2026) — source comparisons for the open pipes/OFN notices. SESSION evidence.

usage: python3 -I evidence/ofn/scripts/ofn_receiving_source_compare_claude.py      (from the repository root; reads tags with git show)

S1  For every DYAD / GEN / TDRG / RECOG RID that ofn-v0.12 cites, compare the source line(s) declaring that RID
    ("[RID: X]" or "**RID:** `X`") at OFN's pin and at the producer's governing tag. Report SAME / CHANGED / NOT-DECLARED.
S2  Triadic triad-v1.6.1 → triad-v1.7: §§6.15–6.18 (heading to next same-or-higher heading), the SG-18 guard and the full
    CN-01..CN-05 blocks; edit runs are listed. r2 fixes the r1 heading false pass (R379-2); missing, ambiguous or empty
    spans now stop the script with exit 1.
S3  GEN §6.3a–§6.3c span (the "### §6.3a" heading to the "### §6.4" heading) compared gen-v2.9 → gen-v2.10.
S4  RECOG §6.6a span compared recog-v0.3.26 → recog-v0.3.27.
S5  Programme OPEN-P0 / RTG-OPEN-GENERATOR-SELECTION lines compared programme-v1.3 → programme-v1.4.
S6  ofn-v0.12 sites whose wording no longer matches the governing producer editions (stale-wording census).
A comparison is a text check, not a proof or certificate replay. Exit 0 unless an S2 span cannot be extracted (exit 1).
"""
import re, subprocess, hashlib

def show(tag, path): return subprocess.run(["git", "show", f"{tag}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")
def h(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

OFN = show("ofn-v0.12", "dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md")
PROD = {"DYAD": ("dyad-v6.4.22", "dyad-v6.4.24", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md"),
        "GEN": ("gen-v2.9", "gen-v2.10", "dsn/RTG_GENESIS_GEOMETRY_DSN.md"),
        "TDRG": ("tdrg-v2.12.14", "tdrg-v2.13", "dsn/RTG_DISCRETE_GENESIS_DSN.md"),
        "RECOG": ("recog-v0.3.26", "recog-v0.3.27", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md")}

print("S1 owner RID declarations cited by ofn-v0.12 (pin -> governing tag)")
for key, (a, b, f) in PROD.items():
    A, B = show(a, f).split("\n"), show(b, f).split("\n")
    rids = sorted(set(re.findall(rf"\b{key}-(?:THM|ALG|DEF|CAND|RESULT|NUM|OPEN)-[A-Z0-9]+(?:-[A-Z0-9]+)*", OFN)))
    for r in rids:
        pat = re.compile(r"(RID: |\*\*RID:\*\* `)" + re.escape(r) + r"[\]`]")
        la = [l for l in A if pat.search(l)]; lb = [l for l in B if pat.search(l)]
        st = "NOT-DECLARED" if not la and not lb else ("SAME" if la == lb else "CHANGED")
        print(f"  {key:6} {r:52} {a} -> {b}: {st} ({len(la)}/{len(lb)} declaring lines)")
        if st == "CHANGED":
            import difflib
            for x, y in zip(la, lb):
                ops = [(o, x[i1:i2], y[j1:j2]) for o, i1, i2, j1, j2 in difflib.SequenceMatcher(None, x, y).get_opcodes() if o != "equal"]
                print(f"      {len(ops)} edit(s); first: {ops[0][0]} {ops[0][1][:80]!r} -> {ops[0][2][:80]!r}")

print("\nS2 Triadic triad-v1.6.1 -> triad-v1.7")
# r2 (24 Nov 2026): the r1 extractor searched "### 6.15" while the headings are "### §6.15", so all four section
# comparisons compared None == None (false pass found in the ChatGPT co-owner readback R379-2). The extractor now
# requires exactly one heading match and a nonempty span, or the script stops with exit 1.
import difflib, sys
TA, TB = show("triad-v1.6.1", "dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md"), show("triad-v1.7", "dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md")
def heading_span(s, num):
    """Span from the unique heading '#{2,4} §<num> ' to the next heading of the same or higher level (nested subsections included)."""
    L = s.split("\n")
    hits = [i for i, l in enumerate(L) if re.match(rf"^(#{{2,4}}) §{re.escape(num)} ", l)]
    if len(hits) != 1:
        sys.exit(f"S2 FAIL: heading §{num}: {len(hits)} matches")
    i = hits[0]; lev = len(re.match(r"^#+", L[i]).group())
    j = next((k for k in range(i + 1, len(L)) if re.match(rf"^#{{1,{lev}}} ", L[k])), len(L))
    span = "\n".join(L[i:j]).rstrip()
    if len(span) <= len(L[i]):
        sys.exit(f"S2 FAIL: heading §{num}: empty span")
    return span
def cn_block(s, k):
    """Full CN-0k block: from its '**CN-0k —' line to the next CN line or heading (all paragraphs, display math included)."""
    L = s.split("\n")
    hits = [i for i, l in enumerate(L) if l.startswith(f"**CN-0{k} —")]
    if len(hits) != 1:
        sys.exit(f"S2 FAIL: CN-0{k}: {len(hits)} matches")
    i = hits[0]
    j = next((m for m in range(i + 1, len(L)) if L[m].startswith("**CN-0") or re.match(r"^#{1,4} ", L[m])), len(L))
    return "\n".join(L[i:j]).rstrip()
def edits(a, b):
    ops = [(o, a[i1:i2], b[j1:j2]) for o, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if o != "equal"]
    return ops
def report(label, a, b):
    if a == b:
        print(f"  {label}: SAME ({len(a)} chars, {h(a)})"); return
    ops = edits(a, b)
    print(f"  {label}: CHANGED ({len(a)}/{len(b)} chars, {h(a)}/{h(b)}, {len(ops)} edit run(s))")
    for o, x, y in ops[:12]:
        print(f"      {o}: {x[:110]!r} -> {y[:110]!r}")
    if len(ops) > 12:
        print(f"      ... {len(ops) - 12} further edit run(s)")
for num in ("6.15", "6.16", "6.17", "6.18"):
    report(f"§{num} (to next same-or-higher heading)", heading_span(TA, num), heading_span(TB, num))
sg = lambda s: [l for l in s.split("\n") if l.startswith("**[SG-18]**")]
a18, b18 = sg(TA), sg(TB)
if len(a18) != 1 or len(b18) != 1:
    sys.exit("S2 FAIL: SG-18 not unique")
report("SG-18", a18[0], b18[0])
strip = lambda t: re.sub(r"\*\*Consumer (status|state)[^*]*\*\*[^\n]*", "", t)
for k in range(1, 6):
    a, b = cn_block(TA, k), cn_block(TB, k)
    report(f"CN-0{k} full block, raw", a, b)
    if a != b:
        report(f"CN-0{k} full block, consumer-state sentences removed", strip(a), strip(b))

print("\nS3 GEN §6.3a–§6.3c span gen-v2.9 -> gen-v2.10")
def span(s, start, end):
    i = s.find(start); j = s.find(end, i + len(start)); return s[i:j] if i >= 0 and j > i else None
GA, GB = show("gen-v2.9", "dsn/RTG_GENESIS_GEOMETRY_DSN.md"), show("gen-v2.10", "dsn/RTG_GENESIS_GEOMETRY_DSN.md")
hA = [l for l in GA.split("\n") if l.startswith("### §6.3a ")]
if hA:
    sa, sb = span(GA, hA[0], "\n### §6.4"), span(GB, hA[0], "\n### §6.4")
    print(f"  heading {hA[0][:60]!r}: {'SAME' if sa == sb and sa else 'CHANGED'} ({len(sa or '')}/{len(sb or '')} chars, {h(sa or '')}/{h(sb or '')})")
else:
    print("  §6.3a heading not found")

print("\nS4 RECOG §6.6a span recog-v0.3.26 -> recog-v0.3.27")
RA, RB = show("recog-v0.3.26", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md"), show("recog-v0.3.27", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md")
hR = [l for l in RA.split("\n") if l.startswith("### §6.6a ")]
if hR:
    sa, sb = span(RA, hR[0], "\n### §6.7"), span(RB, hR[0], "\n### §6.7")
    print(f"  {hR[0][:50]!r}: {'SAME' if sa == sb and sa else 'CHANGED'} ({len(sa or '')}/{len(sb or '')} chars)")

print("\nS5 Programme programme-v1.3 -> programme-v1.4")
PA, PB = show("programme-v1.3", "dsn/RTG_PROGRAMME_OVERVIEW.md"), show("programme-v1.4", "dsn/RTG_PROGRAMME_OVERVIEW.md")
def pblock(s):
    i = s.find("**RID:** `RTG-OPEN-GENERATOR-SELECTION`"); j = s.find("\n\n", i)
    k = s.rfind("\n\n", 0, i); return s[k:j] if i >= 0 else None
print(f"  RTG-OPEN-GENERATOR-SELECTION record block: {'SAME' if pblock(PA) == pblock(PB) and pblock(PA) else 'CHANGED'} ({len(pblock(PA) or '')}/{len(pblock(PB) or '')} chars)")

print("\nS6 ofn-v0.12 wording census against the governing producer editions")
checks = [
    ("XFER-O08-01 'deferred ... v2.13' (TDR-G v2.13: custody open, separate joint decision)", r"deferred[^.|]{0,40}v2\.13|until TDR-G v2\.13 decides|defers the custody transfer XFER-O08-01 to v2\.13"),
    ("token-sum label 'referred back to TDR-G' (answered at tdrg-v2.12.15 SG-3)", r"referred back to TDR-G"),
    ("IMP-O08-12 'registered provisional' (DYAD v6.4.24 label: scope marker, not provisional)", r"registered provisional"),
    ("A1c chain 'under (D5)' / '(D5) are not removed' (RECOG v0.3.27: (D5) discharged for the decoder chain)", r"under \(D5\)|\(D5\) are not removed"),
    ("'γ ≡ κ is the declared parameter convention of Genesis §6.3c' (GEN does not declare it; RRF calls it OFN's)", r"γ ≡ κ is the declared parameter convention of Genesis"),
    ("'Triadic v1.6.1 | OFN v0.9 (pinned by Triadic)' (Triadic v1.7 pins ofn-v0.12)", r"OFN v0\.9 \(pinned by Triadic\)"),
    ("'not re-verified line by line for this draft' (IMP-O10-05 residue)", r"for this draft"),
    ("RF-O08-13 'DZT v0.8' / 'AZ v0.6' (governing dzt-v0.19, az-v0.10)", r"DZT v0\.8 charter|AZ v0\.6 §0\.1"),
]
lines = OFN.split("\n")
for label, pat in checks:
    hits = [i + 1 for i, l in enumerate(lines) if re.search(pat, l)]
    print(f"  {label}: lines {hits}")
