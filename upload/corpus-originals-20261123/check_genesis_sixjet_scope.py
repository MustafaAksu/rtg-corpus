from fractions import Fraction as F
from itertools import product
import json
zero=(0,0,0,0)
var=[{tuple(1 if j==i else 0 for j in range(4)):F(1)} for i in range(4)]
def add(*polys):
 d={}
 for p in polys:
  for k,v in p.items():d[k]=d.get(k,F(0))+v
 return {k:v for k,v in d.items() if v}
def scale(p,a):return {k:a*v for k,v in p.items() if a*v}
def mul(p,q):
 d={}
 for k,v in p.items():
  for j,w in q.items():
   h=tuple(k[i]+j[i] for i in range(4))
   if sum(h)>3:continue
   d[h]=d.get(h,F(0))+v*w
 return {k:v for k,v in d.items() if v}
def powr(p,n):
 d={zero:F(1)}
 for _ in range(n):d=mul(d,p)
 return d
def deg(p,d):return {k:v for k,v in p.items() if sum(k)==d}
def tmap(x,eta,unit2=1,unit3=1):
 # (rho-sin eta, eta+exp rho -1 - sin eta)
 rho2=powr(x,2);rho3=powr(x,3);eta3=powr(eta,3)
 return (add(x,scale(eta,-1),scale(eta3,F(unit3,6))),
         add(x,scale(rho2,F(unit2,2)),scale(rho3,F(unit3,6)),scale(eta3,F(unit3,6))))
def primitive(v,unit2=1,unit3=1):
 a=(v[0],v[1]); b=(v[2],v[3]); c=(scale(add(a[0],b[0]),-1),scale(add(a[1],b[1]),-1))
 raw=[tmap(*x,unit2=unit2,unit3=unit3) for x in [a,b,c]]
 mean=[scale(add(*[r[j] for r in raw]),F(1,3)) for j in (0,1)]
 return tuple(add(raw[i][j],scale(mean[j],-1)) for i in (0,1) for j in (0,1))
def comp6(unit2=1,unit3=1,n=6):
 x=tuple(var); ls=[]
 for i in range(n):
  x=primitive(x,unit2,unit3)
  ls.append(tuple(deg(y,2) for y in x))
 return x,ls

def cross(p,ai,bj):
 out={}
 for k,v in p.items():
  if k[ai] and k[2+bj]:
   t=list(k);t[ai]-=1;t[2+bj]-=1
   t=tuple(t)
   out[t]=out.get(t,F(0))+v*k[ai]*k[2+bj]
 return {k:v for k,v in out.items() if v}
def fmt(p):
 names=('a1','a2','b1','b2')
 return ' + '.join(f'({v})'+''.join('*'+nm+(f'^{i}' if i>1 else '') for nm,i in zip(names,k) if i) for k,v in sorted(p.items())) or '0'
results={}
for name,p2,p3 in [('full',1,1),('quad_only',1,0),('cubic_only',0,1),('linear',0,0)]:
 v,ds=comp6(p2,p3)
 diff=[add(v[k],scale(v[k+2],-1)) for k in (0,1)]
 tbl={f'a{i+1}b{j+1}':[fmt(cross(deg(x,3),i,j)) for x in diff] for i,j in product(range(2),repeat=2)}
 results[name]={'n6_quadratic_zero':all(not deg(x,2) for x in v), 'G3':[fmt(deg(x,3)) for x in v], 'omega6':tbl, 'n6_cubic_count':sum(len(deg(x,3)) for x in v)}
 print(name,'quadratic-zero:', results[name]['n6_quadratic_zero'],'terms:',results[name]['n6_cubic_count'])
 print('omega',tbl)
 if name=='full':
  assert tbl['a1b1']==['(-1/3)*b2 + (1/3)*a2','(-2/3)*b2 + (2/3)*a2'],tbl['a1b1']
  assert tbl['a2b2']==['(-2/3)*b1 + (2/3)*a1','(-1/3)*b1 + (1/3)*a1'],tbl['a2b2']
  results['full']['n6_quadratic_exact_vanish']=all(not deg(x,2) for x in v)
# As the G3 is linear in primitive F3 and quadratic in primitive F2,
# mixed product decomposition should add exactly.
f=results['full']['omega6'];q=results['quad_only']['omega6']; c=results['cubic_only']['omega6'];
# compare polynomial vectors by recomputing simpler algebra from text not necessary; exact invariant obtained with shared code
open('/mnt/data/genesis_sixjet_obstruction_audit.json','w').write(json.dumps(results,indent=2,ensure_ascii=False))
print('saved /mnt/data/genesis_sixjet_obstruction_audit.json')
# Verify additivity of two independent primitive-jet mechanisms at degree three.
def p_eq(p,q):return not add(p,scale(q,-1))
def gen6(p2,p3):
 v,_=comp6(p2,p3)
 return tuple(deg(x,3) for x in v)
Gfull=gen6(1,1);P=gen6(1,0);C=gen6(0,1)
assert all(p_eq(f,add(p,c)) for f,p,c in zip(Gfull,P,C)), 'Cubic jet is not additive!'
# Commutation of primitive linear action and the leading six-step cubic tensor.
linear_4=(add(var[0],scale(var[1],-1)), var[0], add(var[2],scale(var[3],-1)),var[2])
def substitute(poly,subs):
 out={}
 for key,coeff in poly.items():
  x={zero:coeff}
  for i,n in enumerate(key):
   for _ in range(n):x=mul(x,subs[i])
  out=add(out,x)
 return out
G3_at_A=tuple(substitute(c,linear_4) for c in Gfull)
A_G3=(add(Gfull[0],scale(Gfull[1],-1)),Gfull[0],add(Gfull[2],scale(Gfull[3],-1)),Gfull[2])
assert all(p_eq(p,q) for p,q in zip(G3_at_A,A_G3)),'A-equivariance of G3 failed'
# Cyclic permutation of three closed oriented edges represented by (a,b)->(b,-a-b).
cyclic=(var[2],var[3],scale(add(var[0],var[2]),-1),scale(add(var[1],var[3]),-1))
G3_at_C=tuple(substitute(c,cyclic) for c in Gfull)
C_G3=(Gfull[2],Gfull[3],scale(add(Gfull[0],Gfull[2]),-1),scale(add(Gfull[1],Gfull[3]),-1))
assert all(p_eq(p,q) for p,q in zip(G3_at_C,C_G3)),'Cyclic edge permutation covariance failed'
results['verified_relations']={
 'full_G3_equals_quadratic_iterate_plus_direct_cubic':True,
 'omega6_all_eight_components_from_primitive_quadratic': results['full']['omega6']==results['quad_only']['omega6'],
 'primitive_cubic_direct_omega6_zero':all(x=='0' for pair in results['cubic_only']['omega6'].values() for x in pair),
 'leading_G3_commutes_with_A':True,
 'leading_G3_covariant_under_cyclic_edge_perm':True
}
assert all(results['verified_relations'].values())
open('/mnt/data/genesis_sixjet_obstruction_audit.json','w').write(json.dumps(results,indent=2,ensure_ascii=False))
print('ALL EXACT ADDITIONAL VALIDATIONS PASS',results['verified_relations'])
