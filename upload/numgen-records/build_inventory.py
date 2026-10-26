import json,io,re
d=json.load(open('basefp.json')); L=io.open('base.md',encoding='utf-8').read().split('\n')
S2=(148,2121); S6=(2255,2501)
T=[b for b in d['blocks'] if S2[0]<=b['line']<S2[1] and set(b['tags'])&{'RESULT','THM','ALG'}]
h2=[(i+1,l) for i,l in enumerate(L) if S2[0]<=i+1<S2[1] and re.match(r'#{2,4} ',l)]   # module level -> destination
h2s=[(i+1,l) for i,l in enumerate(L) if S2[0]<=i+1<S2[1] and re.match(r'#{2,6} ',l)]  # deepest heading -> sub-module name (e.g. ###### L1 has its own RID)
h6={l.strip('# ').strip():i+1 for i,l in enumerate(L) if S6[0]<=i+1<S6[1] and re.match(r'#{2,4} ',l)}
def mod2(line,H=None):
    cur=None
    for n,l in (H or h2):
        if n<=line: cur=l.strip('# ').strip()
    return cur
def dest6(m):
    if m is None: return None
    rules=[(r'^Priority ordering',None),
           (r'N-1(A|B|C|A0|A2|A-MIN)?\b|N-1 —','§6.2 N-1A/N-1B/N-1C formal target'),
           (r'N-2-ORD','§6.3a N-2-ORD physical order representation — CLOSED at v1.6'),
           (r'\bN-2\b','§6.3 N-2 closed signed-history construction'),
           (r'N-3','§6.4 N-3 representation layer — closed local/abstract results'),
           (r'N-5|N5-','§6.6 N-5A / N-5 rational recurrence target'),
           (r'NG-7','§6.8 NG-7 recurrence holonomy — NG-7A closed / NG-7B open'),
           (r'NG-8','§6.9 NG-8 functorial counting compatibility'),
           (r'NG-10','§6.x NG-10 Genesis saturation and counting truncation — NEW HEADING REQUIRED (ruling pending)')]
    for pat,dst in rules:
        if re.search(pat,m): return dst
    return 'UNMAPPED'
# relationship metadata from the 24-pair review, keyed by §2 module
REL={'N-3D':'UNDER-SUMMARY-OF-MANY','N5-C1':'UNDER-SUMMARY-OF-MANY','N5-C2':'UNDER-SUMMARY-OF-MANY','N5-C3':'UNDER-SUMMARY-OF-MANY','N5-C4':'UNDER-SUMMARY-OF-MANY',
     'N5-PHYS-1':'UNDER-SUMMARY-OF-MANY','N5-C7B':'UNDER-SUMMARY-OF-MANY','N5-C7C':'UNDER-SUMMARY-OF-MANY','NG-7A':'UNDER-SUMMARY-OF-MANY','NG-8A':'UNDER-SUMMARY-OF-MANY',
     'N-2-ORD':'PARTIAL-OVERLAP-MODULE'}
STALE=re.compile(r"no explicit radius|explicit-radius gap|NUM-audited|pending \(D15\)|separate governance|provenance unresolved|v6\.4\.9|FOUNDATIONS_v0\.7|OVERVIEW_v1\.1|design only|not yet certified|relational category",re.I)
inv=[]
for b in T:
    m=mod2(b['line']); msub=mod2(b['line'],h2s); dst=dest6(m)
    body='\n'.join(L[b['line']-1:b['end']])
    status_hdr=L[b['line']-1].lstrip().startswith('**Status:**')
    one_line=(b['end']-b['line'])<=2
    if dst is None: disp='REGISTRY-ONLY'; why='§2 queue/priority line; registry material, not a theorem body'
    elif b['line']==996: disp='MIRROR-RECONCILED'; why='ORD-4 twin of §6 L2357 (review P05); retain §6 L2357, discard this copy with quote'
    elif b['line']==645: disp='MOVE'; why='status line carries a substantive residual clause (v0.9 alignment closed; branching/topology history semantics OPEN) -> must not be reduced to registry'
    elif b['line']==1735: disp='MOVE'; why='status header followed by certificate pointer; provenance must live in the §6.8 body'
    elif b['line']==2094: disp='MOVE'; why='DESTINATION-GAP: §6 has no NG-10 heading; a new structural §6 heading is required (ruling pending)'
    elif status_hdr and one_line: disp='REGISTRY-ONLY'; why='bare module status header; status migrates to the §2 registry row and INV-S'
    else: disp='MOVE'; why='theorem body relocates under its §6 module'
    rel=next((v for k,v in REL.items() if m and k in m),'NO-PRIOR-§6-SUMMARY' if disp=='MOVE' else None)
    stale=sorted(set(x.group(0) for x in STALE.finditer(body)))
    inv.append({"line":b['line'],"end":b['end'],"h":b['h'],"tags":b['tags'],"s2_module":m,"s2_submodule":msub,
                "disposition":disp,"destination_module":dst,"destination_heading_line":h6.get(dst) if dst else None,
                "relationship":rel,"status_header":status_hdr,"rationale":why,"stop_signals":stale,
                "anchor":b['anchor'][:140]})
json.dump({"base_sha256":d['file_sha256'],"generator":"build_inventory.py","n":len(inv),
           "status":"v1 — dispositions machine-assigned then manually corrected for L645, L1735, L2094 and heading depth; all 7 non-MOVE/flagged blocks read in full; NO text moved","blocks":inv},
          open('NG_V1202_REVERSE_INVENTORY_v1.json','w'),indent=1)
from collections import Counter
print("n =",len(inv)); print("dispositions:",dict(Counter(x['disposition'] for x in inv)))
print("destinations:",dict(Counter(x['destination_module'] for x in inv)))
print("unmapped:",[x['line'] for x in inv if x['destination_module']=='UNMAPPED'])
print("\nSTOP-signal hits (need manual reading):")
for x in inv:
    if x['stop_signals']: print(f"  L{x['line']:<5} [{x['s2_module'][:36]}] {x['stop_signals']}")
