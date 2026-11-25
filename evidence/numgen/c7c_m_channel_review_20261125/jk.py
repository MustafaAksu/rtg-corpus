# [NUM] review diagnostic for #386 §9.2: full-word disagreement J_k(N) on the canonical seed (no selection).
from mpmath import mp, mpf, sin, exp
mp.dps = 30
N = int(__import__('sys').argv[1]); ck = [N // 8, N // 4, N // 2, N]
f = {'P': lambda r, e: e, 'M': lambda r, e: r, 'H': lambda r, e: exp(r) - 1 - sin(e)}
order = ['P+', 'H-', 'M-', 'P-', 'H+', 'M+']
def ind(nm, a, b): return (a < 0 <= b) if nm[1] == '+' else (a > 0 >= b)
r, e = mpf(1)/100, mpf(1)/250
win = []  # sliding window of (vals) for last 7 states
from collections import deque
W = deque(maxlen=7); J = [0]*6; out = []
def vals(r, e): return {c: f[c](r, e) for c in 'PMH'}
W.append(vals(r, e))
for n in range(N + 6):
    r, e = r - sin(e), e + exp(r) - 1 - sin(e); W.append(vals(r, e))
    if len(W) == 7:  # W[0] = state m, compare E_0 at m with E_k at m+k
        m = n - 5
        e0 = ind('P+', W[0]['P'], W[1]['P'])
        for k in range(1, 6):
            nm = order[k]; J[k] += abs(int(ind(nm, W[k][nm[0]], W[k+1][nm[0]])) - int(e0))
        if m + 1 in ck: out.append((m + 1, J[1:]))
for n_, j in out: print("N", n_, "J_1..J_5", j)
