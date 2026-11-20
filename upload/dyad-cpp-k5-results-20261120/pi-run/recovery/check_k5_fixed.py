#!/usr/bin/env python3
"""[SESSION] Independent exact-integer 676-box k5 FIFO cover audit.

Checks numerical C1-C2 identity, partition, prior-cover containment, halt/stop,
report and checkpoint continuity. It does NOT implement the complex map.
"""
import argparse
from collections import deque, Counter
from pathlib import Path

S=1 << 256
FHEAD='id depth re_lo re_hi im_lo im_hi'
EVHEAD=('k id depth source_re_lo source_re_hi source_im_lo source_im_hi '
        'necessary_re_lo necessary_re_hi necessary_im_lo necessary_im_hi '
        'final_re_lo final_re_hi final_im_lo final_im_hi '
        'M_256 Dr_256 D_256 r_256 lower_abs_b_256 recenter_error_256 necessary_radius_256 evaluation action')
STHEAD=('k input evaluated excluded split retained unresolved budget_pending budget_valid_no_split '
        'depth_cap frontier_cap prior_L1_256 final_L1_256 median_ratio_256 Dr_gt_M stop')

def ceil(a,b):
    assert b>0
    return -(-a//b)

def boxhit(a,b):
    v=(max(a[0],b[0]),min(a[1],b[1]),max(a[2],b[2]),min(a[3],b[3]))
    return v if v[0]<=v[1] and v[2]<=v[3] else None

def subset(a,b):
    return a[0]<=b[0]<=b[1]<=a[1] and a[2]<=b[2]<=b[3]<=a[3]

def cut(a,j):
    assert j in (0,1,2,3)
    x,y=divmod(j,2)
    dx=a[1]-a[0];dy=a[3]-a[2]
    return (a[0]+dx*x//2,a[0]+ceil(dx*(x+1),2),
            a[2]+dy*y//2,a[2]+ceil(dy*(y+1),2))

def load(path,head):
    lines=Path(path).read_text().splitlines()
    assert lines and lines[0]==head,('bad header',str(path))
    assert all(line and line.strip()==line for line in lines[1:])
    return [line.split() for line in lines[1:]]

def frontier(path):
    res=[];ids=set()
    for w in load(path,FHEAD):
        assert len(w)==6
        ident=w[0]; d=int(w[1]);v=tuple(map(int,w[2:6]))
        assert ident not in ids and d>=0 and v[0]<=v[1] and v[2]<=v[3]
        ids.add(ident);res.append((ident,d,v))
    return res

def events(path):
    res=[];ids=set()
    for w in load(path,EVHEAD):
        assert len(w)==24
        k=int(w[0]);id=w[1];d=int(w[2]);s=list(map(int,w[3:22]))
        b=tuple(s[:4]);n=tuple(s[4:8]);f=tuple(s[8:12]);M,Dr,D,r,lb,e,R=s[12:19]
        assert k==5 and d>=0 and id not in ids and b[0]<=b[1] and b[2]<=b[3]
        ids.add(id);res.append((id,d,b,n,f,M,Dr,D,r,lb,e,R,w[22],w[23]))
    return res

def hull_rad(v):
    assert v
    l=min(b[0] for b in v);h=max(b[1] for b in v)
    ll=min(b[2] for b in v);hh=max(b[3] for b in v)
    mx=(l+h)//2;my=(ll+hh)//2
    return max(abs(l-mx),abs(h-mx))+max(abs(ll-my),abs(hh-my))

def verify(oldfront,newinitial,new_events,stagefile,newfinal,summaryfile,budget,maxdepth,cap):
    frozen=frontier(oldfront);init=frontier(newinitial)
    assert len(frozen)==676 and len(init)==676
    assert all(x[1]==2 for x in frozen)
    assert [(i,b) for i,d,b in init]==[(i,b) for i,d,b in frozen]
    assert all(d==0 for i,d,b in init)
    ev=events(new_events);stage=load(stagefile,STHEAD)
    assert len(stage)==1 and len(stage[0])==16
    q=deque(init);kept=[];j=total=split=excl=ret=unres=pending=vb=dc=fc=gt=0;rat=[]
    prior=hull_rad([b for _,_,b in init]); actions=Counter()
    while q:
        assert j<len(ev),('truncated events',j)
        id,depth,b=q.popleft()
        row=ev[j];j+=1
        nid,d,ib,n,f,M,Dr,D,r,lb,e,R,evalstate,act=row
        assert (nid,d,ib)==(id,depth,b),('FIFO',j,id,nid)
        assert depth<=maxdepth and all(ib[x]<=ib[x+1] for x in (0,2))
        actions[(evalstate,act)]+=1
        if total>=budget:
            assert evalstate=='NOT_EVALUATED' and act=='BUDGET_KEEP'
            assert (n,f)==(b,b) and all(v==0 for v in (M,Dr,D,r,lb,e,R))
            pending+=1;kept.append((id,depth,b));continue
        total+=1
        if evalstate=='UNRESOLVED':
            assert act=='RETAINED' and (n,f)==(b,b)
            assert all(v==0 for v in (M,Dr,D,r,lb,e,R))
            unres+=1;ret+=1;kept.append((id,depth,b));continue
        assert evalstate=='VALID' and act in ('SPLIT','RETAINED','EXCLUDED')
        assert M>0 and lb>0 and all(v>=0 for v in (D,Dr,r,e,R))
        assert Dr==ceil(D*r,S) and R==e+ceil((M+Dr)*S,lb)
        assert n[1]-n[0]==2*R and n[3]-n[2]==2*R
        hit=boxhit(b,n)
        assert f==(hit if hit is not None else (0,0,0,0))
        assert (act=='EXCLUDED')==(hit is None)
        rat.append(ceil(Dr*S,M));gt+=Dr>M
        if hit is None:
            excl+=1;continue
        high=2*Dr>M
        canfront=len(q)+len(kept)+4<=cap
        canbudget=total+len(q)+4<=budget
        if high and depth<maxdepth and canfront and canbudget:
            assert act=='SPLIT'
            split+=1
            for h in range(4):q.append((id+'/'+str(h),depth+1,cut(hit,h)))
        else:
            assert act=='RETAINED';ret+=1
            if high:
                if depth>=maxdepth:dc+=1
                elif not canfront:fc+=1
                else:vb+=1
            kept.append((id,depth,hit))
    assert j==len(ev) and total<=budget
    assert kept==frontier(newfinal)
    now=hull_rad([b for _,_,b in kept]);assert now<=prior
    stop=('BUDGET' if pending or vb else 'REFINEMENT_CAP' if dc or fc else 'DOMAIN' if unres else 'READY')
    rat.sort();med=rat[len(rat)//2] if rat else 0
    w=stage[0]
    expected=(5,676,total,excl,split,ret,unres,pending,vb,dc,fc,prior,now,med,gt,stop)
    actual=tuple(map(int,w[:15]))+(w[15],)
    assert expected==actual,('stage mismatch',expected,actual)
    text=Path(summaryfile).read_text()
    assert f'STATUS={stop}' in text and f'evaluations={total}' in text
    assert f'final_boxes={len(kept)}' in text and f'L1_256={now}' in text
    assert 676+4*split==total+pending,('evaluation accounting',total,split,pending)
    assert 676+3*split-excl==len(kept),('leaf accounting',len(kept))
    print('K5_INDEPENDENT_INTEGER_PASS',f'initial=676 events={j} evaluated={total}',
          f'excluded={excl} split={split} final={len(kept)} unresolved={unres}',
          f'L1_256={now} stop={stop}')
    print('SESSION_ONLY: conditional C1C2 exclusions; not a graph/tube proof, jump or stage3c-b')
    return stop

def main():
    p=argparse.ArgumentParser()
    for n in ('oldfront','initial','events','stages','final','summary'):p.add_argument(n)
    for n in ('budget','depth','cap'):p.add_argument('--'+n,type=int,required=True)
    a=p.parse_args()
    verify(a.oldfront,a.initial,a.events,a.stages,a.final,a.summary,a.budget,a.depth,a.cap)

if __name__=='__main__':main()
