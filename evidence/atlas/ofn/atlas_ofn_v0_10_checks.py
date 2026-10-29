#!/usr/bin/env python3
"""Atlas advisory OFN v0.10 — mechanical checks against the governing tags (ofn-v0.10 vs gen-v2.9, dyad-v6.4.22, recog-v0.3.25, tdrg-v2.12.14, numgen-v1.21, rrf-v0.8.4, triad-v1.6.1): owner-RID resolution, legacy labels, RID-unavailable sites, version strings, [RESULT] pairing, tag census, draft-tense residue, cited anchors, OFN-own RID inventory. Run from the repository root: python3 -I evidence/atlas/ofn/atlas_ofn_v0_10_checks.py > evidence/atlas/ofn/atlas_ofn_v0_10_checks_output.txt"""
import re, subprocess, collections, json, sys
ROOT='/home/claude/rtg-corpus'
def at(ref,path): return subprocess.check_output(['git','-C',ROOT,'show',f'{ref}:{path}']).decode()
ofn=at('ofn-v0.10','dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md')
src={'GEN':at('gen-v2.9','dsn/RTG_GENESIS_GEOMETRY_DSN.md'),'DYAD':at('dyad-v6.4.22','dsn/RTG_DYADIC_OSCILLATOR_DSN.md'),
 'RECOG':at('recog-v0.3.25','dsn/RTG_RELATIONAL_RECOGNITION_DSN.md'),'TDRG':at('tdrg-v2.12.14','dsn/RTG_DISCRETE_GENESIS_DSN.md'),
 'NUMGEN':at('numgen-v1.21','dsn/RTG_NUMBER_GENESIS_DSN.md'),'RRF':at('rrf-v0.8.4','dsn/RTG_RRF_REPRESENTATION_REGISTRY.md'),
 'TRIAD':at('triad-v1.6.1','dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md')}
# 1 RID resolution
rids=sorted(set(re.findall(r'\b((?:GEN|DYAD|RECOG|TDRG|NUMGEN|RRF|UVM|TRIAD)-(?:DEF|THM|ALG|RESULT|CAND|OPEN|HYP|ART|NUM|CND|NET|DYAD)-[A-Z0-9-]+)\b',ofn)))
print('# RID resolution (OFN-cited owner RIDs vs governing tags)')
for r in rids:
    p=r.split('-')[0]; s=src.get(p)
    if s is None: print(f'{r}: owner source not loaded'); continue
    dec=('[RID: '+r+']' in s) or ('`[RID: '+r+']`' in s) or ('[RID: '+r+' ' in s)
    print(f'{r}: {"DECLARED" if dec else ("PRESENT-UNDECLARED" if r in s else "ABSENT")} in {p}')
# legacy labels
print('\n# legacy labels in OFN:', {k:ofn.count(k) for k in ['LEM-REACH','LEM-NOANNIHIL','LEM-RETRIG','LEM-SPECCONS','CONV-TICK','CONV-P3CYC']})
print('# RID unavailable count:', ofn.count('RID unavailable'))
for i,l in enumerate(ofn.split('\n'),1):
    if 'RID unavailable' in l: print('  ',i,l[:150])
# 2 version pins
print('\n# version strings cited in OFN')
c=collections.Counter(re.findall(r'(?:RTG_[A-Z_]+_v?\d[\d.]*|(?:Programme|Methodology|Genesis|Dyadic|DYAD|RECOG|Triadic|TRIAD|TDR-G|NUMGEN|RRF|OPEN M|Legacy|Pre-Legacy|DZT|AZ|UVM)\s+v\d[\d.]*)',ofn))
for k,v in sorted(c.items()): print(f'  {v:3d}  {k}')
# 3 RESULT pairing
res=[(i,l[:120]) for i,l in enumerate(ofn.split('\n'),1) if '[RESULT]' in l and '[from' not in l]
print('\n# [RESULT] without [from:]:',res)
# 4 grade tags census
tags=collections.Counter(re.findall(r'`\[(?!RID|import|scope|source|part of|assuming|SG-|Guard|Local|v0|OWNER)([^\]`]{1,60})\]`',ofn))
print('\n# tag census'); [print(f'  {v:3d}  [{k}]') for k,v in tags.most_common(40)]
# 5 draft residue
print('\n# draft-tense residue')
for i,l in enumerate(ofn.split('\n'),1):
    if re.search(r'Draft 1 revision boundary|Until then|was not read|for this draft|this draft|adoption pending|remains proposed|not yet an exact|freeze candidate|freeze-candidate',l): print('  ',i,l[:170])
# 6 anchors cited in imports vs sources
print('\n# anchors cited')
anc=collections.Counter(re.findall(r'(RTG_[A-Z_]+_v[\d.]+) (§[\d.a-z/ §and]+?) (#[a-z0-9-]+)',ofn))
for (doc,sec,a),v in sorted(anc.items()):
    p={'RTG_DISCRETE_GENESIS_DSN':'TDRG','RTG_GENESIS_GEOMETRY_DSN':'GEN','RTG_RELATIONAL_RECOGNITION_DSN':'RECOG','RTG_DYADIC_OSCILLATOR_DSN':'DYAD'}.get(doc.rsplit('_v',1)[0])
    ok = (a in src[p]) if p else None
    print(f'  {v:2d} {doc} {sec} {a}: anchor {"present" if ok else "ABSENT"} at governing tag')
# 7 OFN own RIDs
own=re.findall(r'\[RID: (RTG-OFN-[A-Z0-9-]+)\]',ofn); print('\n# OFN own RIDs declared:',len(own)); print(sorted(set(own)))
print('# DEF blocks without RID (line starts with `[DEF]` and no [RID: on line):')
for i,l in enumerate(ofn.split('\n'),1):
    if l.startswith('`[DEF]`') and '[RID:' not in l and 'import:' not in l: print('  ',i,l[:110])
print('# OPEN/HYP blocks without RID:')
for i,l in enumerate(ofn.split('\n'),1):
    if (l.startswith('`[OPEN]`') or l.startswith('`[HYP]`')) and '[RID:' not in l and 'import:' not in l: print('  ',i,l[:110])
