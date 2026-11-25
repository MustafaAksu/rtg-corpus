#!/usr/bin/env python3
"""DRAFT (design stage, not a release tool): preservation manifest for an Atlas compaction.

Reads one Atlas file and emits, for every record line, its typed fields bound to the source text: each field keeps its
byte span in the line, the SHA-256 of its exact text and its class. A field the parser cannot classify is kept as
class UNVERIFIED with its span and hash, never dropped and never counted as preserved. An empty field set is not a PASS.

usage: python3 -I atlas_manifest_draft.py ATLAS.md OUT.json [--only ID_PREFIX ...]
Compare stage (not written yet): two manifests + a movement map -> per-field PRESERVED / MOVED / CHANGED / UNVERIFIED.
"""
from __future__ import annotations
import hashlib, json, re, sys
from collections import Counter

GRADES = 'THM ALG DEF CAND HYP RES NUM HEUR INTERP OPEN FAIL RET CONV'.split()
RID = re.compile(r'\b(?:[A-Z][A-Z0-9]*-)+(?:THM|ALG|DEF|CAND|HYP|RES|RESULT|NUM|HEUR|INTERP|OPEN|FAIL|RET|CONV|ART|EXPORT|COR|LEM)-[A-Z0-9][A-Z0-9-]*\b')
PIN = re.compile(r'\b(?:dyad|triad|gen|tdrg|recog|numgen|ofn|programme|methodology|uvm|rrf|legacy|prelegacy|dzt|az|rer|er2b|fms|atlas)-v\d+(?:\.\d+)*\b|\b(?:DYAD|TRIAD|GEN|TDRG|TDR-G|RECOG|NUMGEN|OFN|PROG|UVM|RRF|LEGACY|PREL|DZT|AZ|RER) v\d+(?:\.\d+)*\b')
MARK = re.compile(r'\[custody-[A-Z]\]|\[indep-[A-Z]+\]|\bEV-[A-Z]+(?:-[A-Z]+)*\b|\[assuming:|\bFORMAL_ONLY\b|\bNONCANONICAL\b|\bSESSION\b|\bnot a recovery\b|\bnot rerun\b|\bsource-reported\b')
NUMBER = re.compile(r'(?<![\w.])\d+(?:\.\d+)?(?:/\d+)?(?![\w])')
HEAD = re.compile(r'^(?P<id>\*[A-Z0-9-]+:[A-Za-z0-9₀-₉.+−-]+|(?:[A-Z][A-Z0-9]*-)+[A-Z0-9][A-Za-z0-9-]*)\s+(?P<grade>(?:' + '|'.join(GRADES) + r')(?:\[[A-Z]+\])?(?:·(?:c|s|dx))*(?:\s+nc)?)(?P<rest>.*)$')
L5 = re.compile(r'^(?P<id>(?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?|NUMGEN\.N-[A-Z*]+\d*|RECOG\.R-[A-Z]+\d+[a-z]?|F\d+|H\d+))(?: \+ [A-Z0-9.]+)?\s+(?P<cls>~?\s*D-[A-Z]+(?:/D-[A-Z]+)*)')
FIELD = [('scope', re.compile(r'^sc:')), ('premise', re.compile(r'^if:|^\[assuming:|^import:')), ('dep', re.compile(r'^<')),
         ('consumer', re.compile(r'^>')), ('negative', re.compile(r'^¬')), ('cert', re.compile(r'^cert\b|^art\b')),
         ('locator', re.compile(r'^@')), ('alias', re.compile(r'^≡')), ('derived', re.compile(r'^~')),
         ('tension', re.compile(r'^!')), ('collision', re.compile(r'^⊥')), ('evidence', re.compile(r'^atlas-checked|^EV-|^exact evaluation|^\[indep-'))]

def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()

def fields(line, start):
    out, pos, first = [], start, True
    for seg in line[start:].split(' | '):
        text = seg.strip(); a = line.index(seg, pos) + (len(seg) - len(seg.lstrip())); b = a + len(text); pos = a + len(seg.rstrip()) - (len(seg) - len(seg.lstrip())) if text else pos
        if not text: continue
        cls = next((n for n, r in FIELD if r.match(text)), None)
        if cls is None: cls = 'statement' if first else 'UNVERIFIED'   # a second untyped segment is not assumed to be statement text
        out.append(dict(cls=cls, span=[a, b], sha256=sha(text), rids=sorted(set(RID.findall(text))), pins=sorted(set(PIN.findall(text))), markers=sorted(set(MARK.findall(text))),
                        numbers=NUMBER.findall(text) if cls in ('statement', 'scope', 'premise', 'negative') else None))
        if cls == 'statement': first = False
    return out

def parse(text):
    recs, sec = [], None
    for n, line in enumerate(text.split('\n'), 1):
        if line.startswith('#'): sec = line.strip('# ').strip(); continue
        if not line.strip(): continue
        m = HEAD.match(line); d = L5.match(line)
        if m and ' | ' in line:
            fs = fields(line, m.start('rest'))
            recs.append(dict(kind='node', id=m.group('id'), grade=m.group('grade').strip(), line=n, section=sec, line_sha256=sha(line), fields=fs,
                             conditional='·c' in m.group('grade') or any(f['cls'] == 'premise' for f in fs)))
        elif d:
            recs.append(dict(kind='diagnostic', id=d.group('id'), cls=d.group('cls').strip(), line=n, section=sec, line_sha256=sha(line),
                             rids=sorted(set(RID.findall(line))), pins=sorted(set(PIN.findall(line))), markers=sorted(set(MARK.findall(line))), body_sha256=sha(line[d.end():].strip())))
        else:
            recs.append(dict(kind='UNPARSED', line=n, section=sec, line_sha256=sha(line), head=line[:60], rids=sorted(set(RID.findall(line)))))
    return recs

def main():
    src, out, *rest = sys.argv[1:]
    only = rest[rest.index('--only') + 1:] if '--only' in rest else None
    text = open(src, encoding='utf-8').read(); recs = parse(text)
    kinds = Counter(r['kind'] for r in recs); fc = Counter(f['cls'] for r in recs if r['kind'] == 'node' for f in r['fields'])
    ids = Counter(r['id'] for r in recs if r['kind'] == 'node')
    summary = dict(source_sha256=hashlib.sha256(text.encode('utf-8')).hexdigest(), records=dict(kinds), node_fields=dict(fc),
                   duplicate_node_ids=sorted(k for k, v in ids.items() if v > 1),
                   nodes_with_unverified_field=sum(any(f['cls'] == 'UNVERIFIED' for f in r['fields']) for r in recs if r['kind'] == 'node'),
                   conditional_nodes=sum(r.get('conditional', False) for r in recs),
                   note='UNPARSED lines and UNVERIFIED fields are not covered by a field-level comparison; they need the line-level hash or review.')
    if only: recs = [r for r in recs if any(str(r.get('id', '')).startswith(p) for p in only)]
    json.dump(dict(schema='atlas-preservation-manifest/draft-0', summary=summary, records=recs), open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
