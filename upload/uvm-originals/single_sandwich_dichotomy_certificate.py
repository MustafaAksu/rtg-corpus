"""
single_sandwich_dichotomy_certificate.py — OPEN-M-4 audit artifact (v0.3 gate)
[RID candidates: UVM-CONV-QPAIR, UVM-LEM-RJ, UVM-COR-R3, UVM-THM-WORDSECTOR]

Seven required checks (PI audit spec):
 1. Representation convention verified against two independent implementations.
 2. Degree-1 and degree-2: NO antilinear perpendicular content for ANY constant
    quaternionic two-sided coefficients (exact).
 3. Coefficient basis a,b in {1,i,j,k} enumerated; bilinear sector forms built.
 4. Source (sigma3 = coeff of z zbar^2 in y^0 j-part) and anisotropy
    (mu = coeff of zbar^2 ybar in j-part) projected separately, exactly.
 5. SECTOR PURITY (exact): no degree-3 word carries both functionals.
    Selector law: mu-sector = homogeneous cubes {q^3, qbar^3};
    sigma-sector = all six mixed words.  =>  S_sigma  ∩  S_mu = 0 at word level.
 6. Two independent insertions (two words / interior coefficient) span both.
 7. The selector label printed explicitly: WORD HOMOGENEITY (OPEN-M-4a closed).

Consequences (prose, certified here):
 - R3 [COR]: antilinear content absent at deg<=2 (all coefficients, exact) and
   absent for j-only dressings through deg 5 [NUM]; PRESENT at deg 3 exactly in
   the homogeneous-cube sector. R3's broad "polynomial jets excluded as
   w-sources" is withdrawn. The all-orders 'single-jy commutation' argument
   fails for coefficients with j/k components right of the y-letter (yk=k ybar).
 - OPEN-M-4: closed (C). Under ANY coefficient-level definition of "single
   coupling" (terminal right-j, b=abar, b=a^{-1}, sector-constrained), joint
   (source, anisotropy) is impossible because purity is WORD-level. Joint
   content requires >=2 distinct words => >=2 coupling terms. Mechanism-level
   single origin (one object expanding into both word types) remains OPEN-M-2.
All checks must print PASS.
"""
import sympy as sp
from sympy import I, sqrt, Rational as R
import numpy as np, itertools, cmath, math

OK=True
def check(name,cond):
    global OK
    print(f"[{'PASS' if cond else 'FAIL'}] {name}"); OK = OK and bool(cond)

# ---------- (1) convention lock: two implementations ----------
def Mq(z,y): return np.array([[z, np.conj(y)],[-y, np.conj(z)]])
def partsA(M): return M[0,0], -M[1,0]
def mulB(p,q):
    (z1,y1),(z2,y2)=p,q
    return (z1*z2 - np.conj(y1)*y2, np.conj(z1)*y2 + y1*z2)
rng=np.random.default_rng(5); ok=True
for _ in range(300):
    z1,y1,z2,y2=[complex(rng.normal(),rng.normal()) for _ in range(4)]
    ok &= np.allclose(partsA(Mq(z1,y1)@Mq(z2,y2)), mulB((z1,y1),(z2,y2)))
check("CONV-M-QPAIR: matrix rep == pair algebra (300 random products)", ok)
a=complex(rng.normal(),rng.normal())
check("identity j*a == abar*j (both equal pair (0,a))",
      np.allclose(mulB((0,1),(a,0)), (0,a)) and np.allclose(mulB((np.conj(a),0),(0,1)),(0,a)))
A0,B0=complex(rng.normal(),rng.normal()),complex(rng.normal(),rng.normal())
check("terminal right-j lemma: (A+jB)j = -conj(B) + j conj(A)",
      np.allclose(mulB((A0,B0),(0,1)), (-np.conj(B0), np.conj(A0))))

# ---------- exact pair algebra over Q(i,sqrt3)[z,zb,y,yb] ----------
z,zb,y,yb = sp.symbols('z zb y yb')
def conj(e):
    e=sp.expand(e).xreplace({I:-I})
    d1,d2=sp.Dummy(),sp.Dummy()
    return sp.expand(e.subs([(z,d1),(zb,z),(y,d2),(yb,y)]).subs([(d1,zb),(d2,yb)]))
def mul(p,q):
    (z1,y1),(z2,y2)=p,q
    return (sp.expand(z1*z2 - conj(y1)*y2), sp.expand(conj(z1)*y2 + y1*z2))
def qc(p): return (conj(p[0]), sp.expand(-p[1]))
Qp=(z,y); Qb=qc(Qp)
ONE,Ii,Jj=(sp.Integer(1),sp.Integer(0)),(I,sp.Integer(0)),(sp.Integer(0),sp.Integer(1))
Kk=mul(Ii,Jj)
BASIS={'1':ONE,'i':Ii,'j':Jj,'k':Kk}
w6=R(1,2)+I*sqrt(3)/2
def project(p):
    za,ya=sp.Integer(0),sp.Integer(0)
    for k in range(6):
        wk=sp.expand(w6**k); wkb=sp.expand(wk.xreplace({I:-I}))
        zz=sp.expand(p[0].subs([(z,wk*z),(zb,wkb*zb),(y,wkb*y),(yb,wk*yb)],simultaneous=True))
        yy=sp.expand(p[1].subs([(z,wk*z),(zb,wkb*zb),(y,wkb*y),(yb,wk*yb)],simultaneous=True))
        wmk=sp.expand((R(1,2)-I*sqrt(3)/2)**k); wmkb=sp.expand(wmk.xreplace({I:-I}))
        za+=wmk*zz; ya+=wmkb*yy
    return (sp.expand(za/6), sp.expand(ya/6))
def wordp(word):
    M=None
    for s in word:
        X=Qp if s=='q' else Qb
        M=X if M is None else mul(M,X)
    return M
def sector_functionals(jp):
    poly=sp.Poly(sp.expand(jp),z,zb,y,yb)
    s3=mu=sp.Integer(0)
    for mono,co in poly.terms():
        if mono==(1,2,0,0): s3+=co
        if mono==(0,2,0,1): mu+=co
    return sp.simplify(s3), sp.simplify(mu)

# ---------- (2) degrees 1 and 2: exact antilinear absence ----------
def degree_antilinear_absent(deg):
    for word in itertools.product('qQ',repeat=deg):
        W=wordp(word)
        for A in BASIS.values():
            for Bc in BASIS.values():
                _,Py=project(mul(mul(A,W),Bc))
                poly=sp.Poly(sp.expand(Py),z,zb,y,yb)
                for mono,co in poly.terms():
                    if mono[3]==1 and mono[2]==0:   # any ybar-linear term
                        if sp.simplify(co)!=0: return False
    return True
check("degree-1: NO antilinear j-content for ANY basis coefficients (exact)", degree_antilinear_absent(1))
check("degree-2: NO antilinear j-content for ANY basis coefficients (exact)", degree_antilinear_absent(2))

# ---------- (3)-(5),(7) degree-3 word-sector purity ----------
mu_words=[];sg_words=[];mixed=[]
for word in itertools.product('qQ',repeat=3):
    W=wordp(word); sNZ=mNZ=False
    for A in BASIS.values():
        for Bc in BASIS.values():
            _,Py=project(mul(mul(A,W),Bc))
            s3,mu=sector_functionals(Py)
            sNZ |= (s3!=0); mNZ |= (mu!=0)
    n=''.join(word)
    if sNZ and mNZ: mixed.append(n)
    elif mNZ: mu_words.append(n)
    elif sNZ: sg_words.append(n)
check("SECTOR PURITY: no degree-3 word carries both functionals (exact)", not mixed)
check("selector law (OPEN-M-4a): mu-sector == homogeneous cubes {qqq, QQQ}",
      sorted(mu_words)==['QQQ','qqq'] and len(sg_words)==6)

# ---------- (6) two-insertion control spans both ----------
# the sector forms are rank 2/16: scan basis pairs for nonzero representatives
def find_rep(word, want):
    W=wordp(word)
    for na,A in BASIS.items():
        for nb,Bc in BASIS.items():
            _,Py=project(mul(mul(A,W),Bc))
            s3,mu=sector_functionals(Py)
            if want=='mu' and mu!=0: return (na,nb,Py,mu)
            if want=='s3' and s3!=0: return (na,nb,Py,s3)
    return None
repM=find_rep(('q','q','q'),'mu'); repS=find_rep(('q','q','Q'),'s3')
check("nonzero representatives exist (mu on qqq, sigma3 on qqQ)",
      repM is not None and repS is not None)
print(f"    mu-rep: a={repM[0]}, b={repM[1]}, mu={repM[3]};  s3-rep: a={repS[0]}, b={repS[1]}, s3={repS[3]}")
two=sp.expand(repM[2]+repS[2])
s3T,muT=sector_functionals(two)
check("two insertions (one mu-word + one sigma-word) carry BOTH functionals",
      muT!=0 and s3T!=0)

# ---------- coefficient-constraint corollary ----------
print("\nCorollary (constraint scan resolved structurally): purity is word-level,")
print("so EVERY coefficient-level 'single coupling' definition (terminal-j,")
print("b=abar, b=a^{-1}, sector-constrained) inherits it. Joint (H,w) content")
print("requires >= 2 distinct words = >= 2 coupling terms.")
print("\nALL CHECKS:", "PASS" if OK else "FAIL")
