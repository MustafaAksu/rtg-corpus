# Independent jet check for PR #386 §4: SymPy with explicit truncation at t^4 after every step
# (a different route from the author's Fraction script). Exact rational coefficients.
import sympy as sp
t = sp.symbols('t'); K = 5
def tr(p): return sp.expand(sp.series(sp.expand(p), t, 0, K).removeO()) if p.has(t) else p
def trunc(p):
    p = sp.expand(p); return sum(p.coeff(t, n) * t**n for n in range(K))
def sin_(u): return trunc(u - u**3/6)            # u = O(t): terms to t^4
def exp1(u): return trunc(u + u**2/2 + u**3/6 + u**4/24)
def T(r, e): return trunc(r - sin_(e)), trunc(e + exp1(r) - sin_(e))
f = {'P': lambda r, e: e, 'M': lambda r, e: r, 'H': lambda r, e: trunc(exp1(r) - sin_(e))}
asin_ = lambda u: trunc(u + u**3/6)
src = [('P+', (t, 0)), ('H-', (t, asin_(exp1(t)))), ('M-', (0, t)), ('P-', (-t, 0)), ('H+', (-t, asin_(exp1(-t)))), ('M+', (0, -t))]
names = [s[0] for s in src]
for i, (nm, x) in enumerate(src):
    assert trunc(f[nm[0]](*x)) == 0, nm         # source point lies on its own zero curve to t^4
    row = []
    for k in range(1, 6):
        x = T(*x); tgt = names[(i + k) % 6]; v = trunc(f[tgt[0]](*x))
        n0 = min(n for n in range(K) if v.coeff(t, n) != 0); row.append(f"{tgt}:{v.coeff(t, n0)}*t^{n0}")
    print(nm, ' '.join(row))
r, e = sp.symbols('r e')
print("eta(Tx) - rho(x)  =", sp.expand(sp.series(e + sp.exp(r) - 1 - sp.sin(e) - r, r, 0, 3).removeO()), "+ O(e^3)")
print("h(x) - rho(Tx)    =", sp.simplify((sp.exp(r) - 1 - sp.sin(e)) - (r - sp.sin(e))))
