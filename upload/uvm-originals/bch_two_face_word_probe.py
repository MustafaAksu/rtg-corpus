"""
bch_two_face_word_probe.py — CAND-M-BCH audit certificate (OPEN-M-2B gate)
[RID candidate: UVM-CAND-BCH]

Scope: two-face frame, child transport variants q_C in {u q ubar, ubar q u,
u qbar ubar}; sector-FUNCTIONAL normalization (word-basis coefficients of
z zbar^2 [sigma3] and zbar^2 ybar [mu] after Z6-equivariant projection).
NOT claimed: physical mu/Lambda ratio, HYP-IDENT, cascade success, OPEN M closure.

Seven checks (PI audit spec):
 1. v0.3 sector extractors reproduced (R10 word-purity spot checks).
 2. D1 similarity-transport sterility control.
 3. B2/B4/B5 coefficients symbolic.
 4. sigma3 = 2cs = sin(th), mu = s^2 = sin^2(th/2)  [B2 normalization].
 5. ratio mu/sigma3 = (1/2) tan(th/2).
 6. limits th->0 (both vanish), th=pi (sigma3=0, mu=1).
 7. child-frame variants: sign/ratio stability report.
All checks must print PASS.
"""
import sympy as sp
from sympy import I, sqrt, Rational as R

OK=True
def check(name,cond):
    global OK
    print(f"[{'PASS' if cond else 'FAIL'}] {name}"); OK=OK and bool(cond)

z,zb,y,yb=sp.symbols('z zb y yb'); c,s=sp.symbols('c s',real=True)
def trunc(e):
    e=sp.expand(e); out=sp.Integer(0)
    for t in sp.Add.make_args(e):
        d=(sp.degree(t,y) if t.has(y) else 0)+(sp.degree(t,yb) if t.has(yb) else 0)
        if d<=1: out+=t
    return out
def conj(e):
    e=sp.expand(e).xreplace({I:-I}); d1,d2=sp.Dummy(),sp.Dummy()
    return sp.expand(e.subs([(z,d1),(zb,z),(y,d2),(yb,y)]).subs([(d1,zb),(d2,yb)]))
def mul(p,q):
    (z1,y1),(z2,y2)=p,q
    return (trunc(z1*z2-conj(y1)*y2), trunc(conj(z1)*y2+y1*z2))
def qc(p): return (conj(p[0]),sp.expand(-p[1]))
def sub(p,q): return (sp.expand(p[0]-q[0]),sp.expand(p[1]-q[1]))
def add(p,q): return (sp.expand(p[0]+q[0]),sp.expand(p[1]+q[1]))
Qp=(z,y); Qb=qc(Qp); u=(c,s); ub=(c,-s)
w6=R(1,2)+I*sqrt(3)/2
def pj(p):
    ya=sp.Integer(0)
    for k in range(6):
        wk=sp.expand(w6**k); wkb=sp.expand(wk.xreplace({I:-I}))
        yy=sp.expand(p[1].subs([(z,wk*z),(zb,wkb*zb),(y,wkb*y),(yb,wk*yb)],simultaneous=True))
        ya+=sp.expand(((R(1,2)-I*sqrt(3)/2)**k).xreplace({I:-I}))*yy
    return sp.expand(ya/6)
def SM(p):
    jp=pj(p)
    if jp==0: return sp.Integer(0),sp.Integer(0)
    poly=sp.Poly(jp,z,zb,y,yb)
    s3=mu=sp.Integer(0)
    for m,co in poly.terms():
        if m==(1,2,0,0): s3+=co
        if m==(0,2,0,1): mu+=co
    return sp.simplify(s3),sp.simplify(mu)

# (1) R10 extractor reproduction: word purity spot checks (j-coefficient reps)
Jq=(sp.Integer(0),sp.Integer(1))
def sandwich(a,W,b): return mul(mul(a,W),b)
W_cube=mul(mul(Qp,Qp),Qp); W_mix=mul(mul(Qp,Qp),Qb)
found_mu=False; found_s3=False; pure=True
for a in [(1,0),(I,0),(0,1),(0,-I)]:
    for b in [(1,0),(I,0),(0,1),(0,-I)]:
        a_=(sp.sympify(a[0]),sp.sympify(a[1])); b_=(sp.sympify(b[0]),sp.sympify(b[1]))
        s3,mu=SM(sandwich(a_,W_cube,b_))
        if mu!=0: found_mu=True
        if s3!=0: pure=False
        s3,mu=SM(sandwich(a_,W_mix,b_))
        if s3!=0: found_s3=True
        if mu!=0: pure=False
check("(1) R10 reproduced: qqq mu-pure with nonzero rep; qqQ sigma-pure with nonzero rep",
      found_mu and found_s3 and pure)

# (2) D1 sterility control: similarity transport of twist lift
tau=sp.symbols('tau',real=True); lam=R(1,2)+I*sqrt(3)/2
def smulc(cc,p):
    cb=sp.expand(sp.sympify(cc).xreplace({I:-I}))
    return (trunc(cc*p[0]),trunc(cb*p[1]))
def T(p):
    pb=qc(p)
    S3=add(add(mul(mul(p,pb),p),mul(mul(p,p),pb)),mul(mul(pb,p),p))
    return add(smulc(lam,p),smulc(I*tau*lam,(sp.expand(S3[0]/3),sp.expand(S3[1]/3))))
child=mul(mul(u,T(mul(mul(ub,Qp),u))),ub)
s3,mu=SM(child)
check("(2) D1 control: similarity-transported twist generator is sector-sterile", s3==0 and mu==0)

# (3)-(5) BCH words
def C(p): return mul(mul(u,p),ub)
def comm(p,q): return sub(mul(p,q),mul(q,p))
B2=mul(Qp,comm(Qp,C(Qp))); B4=mul(comm(Qb,C(Qp)),Qb); B5=mul(comm(Qp,C(Qb)),Qb)
s3_2,mu_2=SM(B2); s3_4,mu_4=SM(B4); s3_5,mu_5=SM(B5)
print(f"    B2: sigma3={s3_2}, mu={mu_2};  B4: {s3_4},{mu_4};  B5: {s3_5},{mu_5}")
check("(3) B2/B4/B5 computed symbolically; all carry BOTH functionals",
      all(x!=0 for x in [s3_2,mu_2,s3_4,mu_4,s3_5,mu_5]))
th=sp.symbols('theta',real=True)
sub_t=[(c,sp.cos(th/2)),(s,sp.sin(th/2))]
check("(4) B2 normalization: sigma3 = 2cs = sin(theta); mu = s^2 = sin^2(theta/2)",
      sp.simplify(s3_2.subs(sub_t)-sp.sin(th))==0 and sp.simplify(mu_2.subs(sub_t)-sp.sin(th/2)**2)==0)
r2=sp.simplify((mu_2/s3_2).subs(sub_t)); r4=sp.simplify((mu_4/s3_4).subs(sub_t)); r5=sp.simplify((mu_5/s3_5).subs(sub_t))
tgt=sp.tan(th/2)/2
check("(5) ratio mu/sigma3 = (1/2) tan(theta/2) for B2, B4, B5",
      all(sp.simplify(r-tgt)==0 for r in [r2,r4,r5]))

# (6) limits
check("(6) theta->0: both vanish; theta=pi: sigma3=0, mu=1",
      s3_2.subs(sub_t).subs(th,0)==0 and mu_2.subs(sub_t).subs(th,0)==0
      and sp.simplify(s3_2.subs(sub_t).subs(th,sp.pi))==0
      and sp.simplify(mu_2.subs(sub_t).subs(th,sp.pi))==1)

# (7) child-frame variants
def Cinv(p): return mul(mul(ub,p),u)          # q_C = ubar q u
def Cbar(p): return mul(mul(u,qc(p)),ub)      # q_C = u qbar ubar
rows=[]
for name,Cv in [("uqub",C),("ubqu",Cinv),("uQbub",Cbar)]:
    for wname,W in [("q[q,C(q)]",mul(Qp,comm(Qp,Cv(Qp)))),
                    ("[qb,C(q)]qb",mul(comm(Qb,Cv(Qp)),Qb)),
                    ("[q,C(qb)]qb",mul(comm(Qp,Cv(Qb)),Qb))]:
        s3v,muv=SM(W)
        if s3v==0 or muv==0:
            rows.append((name,wname,s3v,muv,None)); continue
        rv=sp.simplify((muv/s3v).subs(sub_t))
        rows.append((name,wname,sp.simplify(s3v.subs(sub_t)),sp.simplify(muv.subs(sub_t)),rv))
stable=True
for name,wname,s3v,muv,rv in rows:
    print(f"    child={name:6s} word={wname:12s} sigma3={s3v}, mu={muv}, ratio={rv}")
    if rv is not None and sp.simplify(sp.Abs(rv)-sp.Abs(tgt))!=0: stable=False
check("(7) child-frame variants: |ratio| stable at (1/2)|tan(theta/2)| (signs may flip)", stable)

print("\nALL CHECKS:","PASS" if OK else "FAIL")
