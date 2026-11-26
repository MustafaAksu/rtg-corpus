# [NUM] review diagnostic for PR #386 (not a proof input): on the canonical seed (1/100, 1/250) in U_D,base,
# how often is each directed channel token exactly the k-step translate of the P_+ token (k = ray index)?
from mpmath import mp, mpf, sin, exp
from collections import Counter
mp.dps = 30
N = 120000
def T(r, e): return r - sin(e), e + exp(r) - 1 - sin(e)
f = {'P': lambda r, e: e, 'M': lambda r, e: r, 'H': lambda r, e: exp(r) - 1 - sin(e)}
order = ['P+', 'H-', 'M-', 'P-', 'H+', 'M+']          # limiting rays 0, pi/3, ..., 5pi/3
xs = [(mpf(1)/100, mpf(1)/250)]
for n in range(N + 1): xs.append(T(*xs[-1]))
vals = {c: [f[c](*x) for x in xs] for c in 'PMH'}
ev = {nm: set() for nm in order}
for n in range(N):
    for nm in order:
        a, b = vals[nm[0]][n], vals[nm[0]][n + 1]
        if (nm[1] == '+' and a < 0 <= b) or (nm[1] == '-' and a > 0 >= b): ev[nm].add(n)
src = sorted(ev['P+'])
print("steps", N, {nm: len(ev[nm]) for nm in order})
for k, nm in enumerate(order[1:], 1):
    lag = Counter()
    for n in src:
        d = next((d for d in range(0, 9) if n + d in ev[nm]), None); lag[d] += 1
    hit = lag[k]
    print(f"P+ at n -> {nm} at n+{k}: {hit}/{len(src)} ({100*hit/len(src):.2f}%); lag distribution {dict(sorted(lag.items(), key=lambda z: (z[0] is None, z[0])))}")
