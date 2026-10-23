import sys,json; sys.path.insert(0,'.')
from lib import A
a=A(); DISP=json.load(open('disp.json'))
L=a.t.split('\n')
def find(pred,start=0,dflt=None):
    for i in range(start,len(L)):
        if pred(L[i]): return i
    if dflt is not None: return dflt
    raise Exception('nf')
HDR="| evidence record: exact or high-precision recomputations by the atlas owner during the build (EV-INDEP at the stated scope; not owner certification, adopts nothing; owner wins on conflict) | "
moves=[]  # (domain, list of line indices, text)
def dom_bounds(d):
    l2=find(lambda s:s.startswith(f'### {d}.L2')); l3=find(lambda s:s.startswith(f'### {d}.L3'),l2)
    l5=find(lambda s:s.startswith(f'### {d}.L5'),l3); end=find(lambda s:s.startswith('## ') or s=='---' or s.startswith('*END'),l5+1,len(L))
    return l2,l3,l5,end
plan={}
for d in ['D1','D2','D3','D4a','D4b','D5','D6']:
    l2,l3,l5,end=dom_bounds(d); idx=[]; parts=[]
    i=l5+1
    while i<end:
        s=L[i]
        if d=='D2' and s.startswith('**PASS'):
            idx.append(i); j=i+1
            while j<end and L[j].split(':')[0] in ('DYAD','NUMGEN','DZT','AZ Thread A'):
                idx.append(j); parts.append(L[j]); j+=1
            i=j; continue
        if d=='D3' and s.startswith('RECOG.PASS'):
            idx.append(i); j=i+1
            while j<end and L[j].startswith('- '):
                idx.append(j); parts.append(L[j][2:]); j+=1
            i=j; continue
        if s.startswith('PASS (atlas-checked') or s.startswith('D5.X2 PASS'):
            idx.append(i); parts.append(s.split(':',1)[1].strip()); 
        i+=1
    plan[d]=(l3,idx,parts)
# apply from bottom
for d in ['D6','D5','D4b','D4a','D3','D2','D1']:
    l3,idx,parts=plan[d]
    for i in sorted(idx,reverse=True): del L[i]
    rec=f"*ATLAS:checked-{d} "+HDR+" · ".join(p.rstrip('.') for p in parts)
    # insert before L3 heading, after last nonblank L2 line
    k=l3
    while L[k-1].strip()=='' : k-=1
    L.insert(k,rec)
    DISP.append((f'PASS block {d}','moved',f'PASS list removed from {d}.L5 (Method v0.2 §6: atlas-checked facts at content layer); placed as evidence record *ATLAS:checked-{d} at the end of {d}.L2; per-node distribution deferred to the compression pass'))
a.t='\n'.join(L)
a.rep("F3 PASS + ~ D-LINK (ER2B.Z1, FMS.M5; high value):","F3 ~ D-LINK (atlas-checked; ER2B.Z1, FMS.M5; high value):")
a.rep("ΔQ₅≡P₅ exactly (sympy PASS);","ΔQ₅≡P₅ exactly (atlas-checked, sympy);")
a.line("NUMGEN.N-C D-PIN/PASS |","NUMGEN.N-C D-SCOPE (minor; atlas-checked) | tube bound 0.0665 is valid but loose (sharp 0.05427); NUMGEN's PRIM-CTR and Q403 import values agree with DYAD; Q₁₂ is negative (modulus 0.0096).")
DISP=[x for x in DISP if x[0]!='NUMGEN.N-C']+[['NUMGEN.N-C','reworded','PASS wording replaced by atlas-checked scope note']]
a.save(); json.dump(DISP,open('disp.json','w'),ensure_ascii=False,indent=0)
for d in plan: print(d,len(plan[d][1]))
