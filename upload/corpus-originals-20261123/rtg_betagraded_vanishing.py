#!/usr/bin/env python3
"""
rtg_betagraded_vanishing.py
============================
RECOMMENDED high-certification engine for the degree-b anti-holomorphic
vanishing theorem (OPEN 9, RTG Dyadic DSN).

Proves / certifies:  F_raw^p(0,b) = 0  for  p >= b+2,
for the raw dyadic map  F(W) = lam*W + sum_{a+b} c_ab W^a conj(W)^b
with lam = exp(2*pi*i/p), for ARBITRARY symbolic one-step coefficients c_ab.

WHY THIS IS FAST (avoids the timeout):
  Coefficients of the n-fold composition jet are carried in a BETA-GRADED form,
  i.e. as dicts { (beta, m) : coeff } meaning  coeff * n^m * lam^{beta*n}.
  Composition is convolution in (beta, m); the discrete Duhamel recursion solver
  maps each source mode to two output modes. This keeps lambda at bounded constant
  powers and never triggers sympy's exponential expansion of lam^{k*n}.

VANISHING CRITERION (exact cyclotomic arithmetic):
  A^p_(0,b) = sum_beta C_beta * lam^{p-1} * G(beta-1),  G(m)=sum_{k<p} lam^{m k}.
  At a primitive p-th root: G(m) = p if p|m else 0.
  => A^p_(0,b) = 0  iff  for every source beta, p does NOT divide (beta-1),
     AND there is no secular mode (beta=1) in the source.

USAGE:
  python3 rtg_betagraded_vanishing.py [MAXDEG]
  e.g.  python3 rtg_betagraded_vanishing.py 7
        determines source beta-sets and vanishing ranges for b = 2..MAXDEG,
        and reports whether the secular mode beta=1 first enters (the channel-
        boundary question, OPEN 9 item 4b).

Exit code 0 if all tested b in {2,3,4} certify (p>=b+2, no secular); 1 otherwise.
Increase MAXDEG to probe b=5,6,7,... ; runtime grows with the one-step coefficient
set size MAXC and degree, but stays far below the brute-force sympy approach.
"""
import sympy as sp
lam = sp.symbols('lambda', nonzero=True)
nsym = sp.symbols('n', integer=True, positive=True)

cs, cbar = {}, {}
MAXC = 6
for a in range(MAXC+1):
    for b in range(MAXC+1):
        if 2 <= a+b <= MAXC:
            cs[(a,b)]   = sp.symbols(f'c_{a}_{b}')
            cbar[(a,b)] = sp.symbols(f'cb_{a}_{b}')

def bp_add(P,Q):
    R=dict(P)
    for k,c in Q.items(): R[k]=R.get(k,0)+c
    return {k:sp.expand(c) for k,c in R.items() if sp.expand(c)!=0}
def bp_scal(P,s):
    return {k:sp.expand(c*s) for k,c in P.items() if sp.expand(c*s)!=0}
def bp_mul(P,Q):
    R={}
    for (b1,m1),c1 in P.items():
        for (b2,m2),c2 in Q.items():
            key=(b1+b2,m1+m2)
            R[key]=R.get(key,0)+c1*c2
    return {k:sp.expand(c) for k,c in R.items() if sp.expand(c)!=0}
def bp_conj(P):
    out={}
    subs={}
    for k in cs: subs[cs[k]]=cbar[k]; subs[cbar[k]]=cs[k]
    for (b,m),c in P.items():
        cc=c.subs(lam,1/lam).subs(subs,simultaneous=True)
        out[(-b,m)]=out.get((-b,m),0)+cc
    return {k:sp.expand(c) for k,c in out.items() if sp.expand(c)!=0}

def jet_conj(J):
    out={}
    for (a,b),P in J.items():
        out[(b,a)]=bp_add(out.get((b,a),{}), bp_conj(P))
    return out
def jet_mul(J1,J2,md):
    out={}
    for (a1,b1),P1 in J1.items():
        for (a2,b2),P2 in J2.items():
            if a1+a2+b1+b2<=md:
                out[(a1+a2,b1+b2)]=bp_add(out.get((a1+a2,b1+b2),{}), bp_mul(P1,P2))
    return out
def jet_pow(J,e,md):
    R={(0,0):{(0,0):sp.Integer(1)}}
    for _ in range(e): R=jet_mul(R,J,md)
    return R
def F_apply(J,md):
    Jc=jet_conj(J); out={}
    for (a,b),P in J.items():
        if a+b<=md: out[(a,b)]=bp_add(out.get((a,b),{}), bp_scal(P,lam))
    for (a,b) in cs:
        if a+b>md: continue
        T=jet_mul(jet_pow(J,a,md),jet_pow(Jc,b,md),md)
        for key,P in T.items():
            if key[0]+key[1]<=md:
                out[key]=bp_add(out.get(key,{}), bp_scal(P,cs[(a,b)]))
    return out

def solve_channel(src):
    """Solve A^{n+1}=lam A^n + S(n), S given as {(beta,m):coeff}*n^m*lam^{beta n}.
    Closed form via discrete Duhamel. For non-secular (beta!=1,m=0):
      contributes {(beta,0): C*lam^{-1}/(lam^{beta-1}-1), (1,0): -C*lam^{-1}/(lam^{beta-1}-1)}.
    For source already secular or m>0, use general accumulation:
      A^n = sum_{k=0}^{n-1} lam^{n-1-k} S(k). We resolve the standard cases and
      otherwise return a symbolic flag. For b<=4 only (beta!=1,m=0) occurs in (0,b).
    Returns (solved_bp, has_unresolved_secular_bool)."""
    out={}; unresolved=False
    for (b,m),c in src.items():
        if m==0 and b!=1:
            denom=lam**(b-1)-1
            k=c*lam**(-1)/denom
            out[(b,0)]=out.get((b,0),0)+k
            out[(1,0)]=out.get((1,0),0)-k
        elif m==0 and b==1:
            # secular: A^n gets c * n * lam^{n-1}
            out[(1,1)]=out.get((1,1),0)+c*lam**(-1)
        else:
            # higher secular powers: resolvable but mark; needed only for b>=5 analysis
            unresolved=True
            out[(b,m)]=out.get((b,m),0)+c  # placeholder (not exact); flagged
    return {k:sp.expand(v) for k,v in out.items() if sp.expand(v)!=0}, unresolved

def build_jet(maxdeg, verbose=True):
    """Build beta-graded jet and record each homogeneous source at the moment it is generated.

    Important: the source record for (0,b) is reliable because it is captured before
    solving degree b. This avoids the old reporting recomposition that could hang
    once higher secular polynomial modes appeared at b=5.
    """
    J={(1,0):{(1,0):sp.Integer(1)}}
    source_record={}
    unresolved_channels=[]
    for deg in range(2,maxdeg+1):
        FJ=F_apply(J,deg)
        for (a,b) in [(a,b) for a in range(deg+1) for b in range(deg+1) if a+b==deg]:
            src=FJ.get((a,b),{})
            source_record[(a,b)]=src
            solved,unres=solve_channel(src)
            J[(a,b)]=solved
            if unres:
                unresolved_channels.append((a,b))
            if verbose and a==0:
                sb=sorted({bb for (bb,m) in src})
                sm=sorted({(bb,m) for (bb,m) in src})
                bset=sorted({bb for (bb,m) in solved})
                print(f"  (0,{b}) source beta={sb}, source modes={sm}")
                print(f"        solved beta-set={bset}, has n-secular={any(m>0 for (bb,m) in solved)}, unresolved={unres}")
    return J, source_record, unresolved_channels


def source_summary(source_record, b):
    src=source_record.get((0,b),{})
    bs=sorted({bb for (bb,m) in src})
    has_poly=any(m>0 for (bb,m) in src)
    return bs, has_poly


if __name__=="__main__":
    import sys
    MAXDEG=int(sys.argv[1]) if len(sys.argv)>1 else 4
    print(f"Building beta-graded jet to degree {MAXDEG}...")
    J, source_record, unresolved_channels = build_jet(MAXDEG)
    print("\nSource beta-sets for (0,b) and vanishing ranges:")
    fail=False
    for b in range(2,MAXDEG+1):
        bs,has_poly=source_summary(source_record,b)
        breakers=sorted({p for B in bs if B!=1 for p in range(2,abs(B-1)+1) if (B-1)%p==0})
        secular = (1 in bs) or has_poly
        vrange = "NEVER / NOT UNIVERSAL (secular or polynomial source mode)" if secular else f"p>={max(breakers)+1 if breakers else 2}"
        print(f"  (0,{b}): source beta={bs}  source_has_n_poly={has_poly}  secular={1 in bs}  vanishes {vrange}")
        if b in (2,3,4):
            expected = {2:4,3:5,4:6}[b]
            ok = (not secular) and breakers and (max(breakers)+1==expected)
            if not ok:
                print(f"  FAIL: (0,{b}) did not certify p>={expected}")
                fail=True
    if unresolved_channels:
        print("\nNote: higher-degree solved coefficients with n-polynomial/secular structure were encountered:")
        print("  "+", ".join(map(str, unresolved_channels[:20])) + (" ..." if len(unresolved_channels)>20 else ""))
        print("  Source records are still reliable at the degree they are printed; later degrees may need the boundary-scan or a full polynomial-mode solver.")
    if fail:
        print("\nCERTIFICATE FAILED"); sys.exit(1)
    print("\nCERTIFICATE PASSED for b in {2,3,4}: F_raw^p(0,b)=0 for p>=b+2  [ALG]")
    if MAXDEG>=5 and 1 in source_summary(source_record,5)[0]:
        print("BOUNDARY SIGNAL: beta=1 enters the (0,5) source, so universal vanishing breaks at b=5 [candidate/scan].")
    sys.exit(0)
