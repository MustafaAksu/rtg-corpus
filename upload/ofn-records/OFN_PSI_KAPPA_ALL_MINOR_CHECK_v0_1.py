# OFN_PSI_KAPPA_ALL_MINOR_CHECK_v0_1 (OFN co-owner SESSION, 19 Oct 2026)
# All-kappa check of the first-order-in-a quintic psi-obstruction (a in i*R*mu) on the centre-manifold-reduced
# transported model. Entries of [A|d5] are affine in t=(1-kappa)/kappa with only 8 t-dependent columns, so every
# 32x32 minor is a polynomial of degree <= 8 in t. PASS iff (i) rank A = 31 at 21 distinct t (all 32-minors of A
# vanish identically) and (ii) one fixed 32x32 minor of [A|d5] takes the same nonzero value at 21 distinct t
# (it is a nonzero constant). Then the obstruction holds for every t, i.e. every real kappa != 0; kappa = 2 is
# excluded by the scope of the centre-manifold reduction. Independent of FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py
# (different minor, different elimination). Requires OFN_PSI_KAPPA_EXTENSION_v0_1.py in the same folder.
import os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'OFN_PSI_KAPPA_EXTENSION_v0_1.py')).read().split("ok=True\ndef check")[0]
exec(src)
from fractions import Fraction as Fr
import sys
def columns(kap):
    E=extra(kap); f5k=[padd(f5base[i],E[i]) for i in range(2)]
    cols=[]
    for kind,P in basis:
        if kind=='3': v5=L3_of(P); v3=[{},{}]
        else: v5=L1_of(P,f5k); v3=L1_of(P,f3)
        cols.append(flatten(v3,v5))
    return cols
c0=columns(Fr(1)); c1=columns(Fr(1,2))   # t=0, t=1
fa=onC(dyad_model(iu*mu)); d5=flatten([{},{}],[padd(degpart(fa[i],5),f5base[i],-1) for i in range(2)])
c3=columns(Fr(3)); t3=Fr(-2,3)
keys=sorted(set().union(*[c.keys() for c in c0+c1+c3],d5.keys()),key=str)
ncol=len(c0)
def mat(t):
    T=R(t)
    return [[c0[j].get(k,R())+(c1[j].get(k,R())-c0[j].get(k,R()))*T for j in range(ncol)]+[d5.get(k,R())] for k in keys]
aff=all((c0[j].get(k,R())+(c1[j].get(k,R())-c0[j].get(k,R()))*R(t3)-c3[j].get(k,R())).iszero() for j in range(ncol) for k in keys)
tdep=[j for j in range(ncol) if any(not (c1[j].get(k,R())-c0[j].get(k,R())).iszero() for k in keys)]
print('entries affine in t (checked at kappa=3):',aff,'; t-dependent columns:',len(tdep),'; rows:',len(keys))
def pivrows(M):
    ech=[]; chosen=[]
    for i,row in enumerate(M):
        r=row[:]
        for pc,er in ech:
            if not r[pc].iszero():
                f=r[pc]; r=[a-f*b for a,b in zip(r,er)]
        pc=next((c for c,x in enumerate(r) if not x.iszero()),None)
        if pc is not None:
            inv=r[pc].inv(); r=[x*inv for x in r]
            ech=[(p,[a-e[pc]*b for a,b in zip(e,r)]) for p,e in ech]
            ech.append((pc,r)); chosen.append(i)
    return chosen
def det(M):
    M=[r[:] for r in M]; n=len(M); d=R(1)
    for c in range(n):
        piv=next((r for r in range(c,n) if not M[r][c].iszero()),None)
        if piv is None: return R()
        if piv!=c: M[c],M[piv]=M[piv],M[c]; d=-d
        d=d*M[c][c]; inv=M[c][c].inv()
        for r in range(c+1,n):
            if not M[r][c].iszero():
                f=M[r][c]*inv; M[r]=[a-f*b for a,b in zip(M[r],M[c])]
    return d
rows=pivrows(mat(Fr(8,7)))
print('rank of [A|d5] at a generic t:',len(rows))
_B=[mat(Fr(8,7))[r] for r in rows]
cols=pivrows([[_B[i][j] for i in range(len(_B))] for j in range(ncol+1)])
print('chosen columns:',len(cols),'includes d5 column:',ncol in cols)
ok=aff and len(rows)==ncol and len(cols)==ncol and ncol in cols
deg=len(tdep)   # minor is a polynomial in t of degree <= number of t-dependent columns
ts=[Fr(k,3) for k in range(-(deg+2),deg+3)]
def minor(t):
    M=mat(t); return det([[M[r][c] for c in cols] for r in rows])
vals=[minor(t) for t in ts]
const=all((v-vals[0]).iszero() for v in vals)
print('fixed minor at',len(ts),'points (degree bound',deg,'): constant =',const,'; value =',vals[0],'; nonzero =',not vals[0].iszero())
def rank(M):
    return len(pivrows(M))
rA=[rank([r[:-1] for r in mat(t)]) for t in ts]
print('rank A at the same points:',sorted(set(rA)))
ok=ok and const and not vals[0].iszero() and set(rA)=={ncol-1}
print('ALL-KAPPA OBSTRUCTION (first order in a, kappa not in {0,2}):','PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
