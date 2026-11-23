#!/usr/bin/env python3
"""
Shared Stage-2 contract: config identity, exact plan, record validation, duplicate/conflict policy.
Imported by BOTH triad_stage2_driver.py (resume) and triad_stage2_coverage.py (aggregation), so a row that does not
count for coverage can never cause a job to be skipped (finding G1c).

Config identity (finding G2): the semantic hash is SHA-256 of the canonical JSON of the config with the purely
operational key 'results' removed.  Output paths are chosen with --results and never change the identity.
Scope pins (finding G3): KT must be '1' and the coefficient table must have the pinned SHA-256; the engine itself
re-checks the table it actually loads (engine v3.2 configure()).

Record policy (G1a/G1b):
  * every numeric field must parse as a finite decimal; norms, radii, remainders and constants must be >= 0;
  * radii are checked against the exact planned geometry, not only against each other;
  * published constants: <= 4 significant digits, K_up >= K_raw, and K_up * R_eff^(N+1) >= bound_B_up / (1+1e-3);
  * a (box, N) key counts only if it has at least one valid PASS row and all its valid PASS rows carry the same
    canonical scientific payload; two different valid payloads quarantine the key permanently (resolution = an
    explicit manual edit of the result files, which changes nothing in the identity hashes but is visible);
  * FAIL rows never count and never block a later valid PASS (retry allowed); invalid PASS rows never count and are
    listed.
A complete, conflict-free record set means RECORD COVERAGE COMPLETE for engine-reported bounds.  It does NOT by itself
mean independently mathematically certified: the Taylor-model lemma review is a separate gate.
"""
import json, hashlib
from pathlib import Path
from fractions import Fraction as Fr
from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 60
PINNED_POLY_SHA256 = '03042f84016aa2128ca7ac425a0782d84a617e4b74c490d4f0c7b912c300d83c'
SUPPORTED_KT = '1'
OPERATIONAL_KEYS = ('results',)
REQUIRED_CFG = ('R_LO', 'R_MID', 'R_HI', 'H_IN', 'H_OUT', 'TAU_LO', 'TAU_HI', 'HTAU', 'K', 'DPS', 'N_LIST', 'KT', 'engine', 'poly')

sha_file = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

def load_config(path):
    path = Path(path); cfg = json.loads(path.read_text())
    missing = [k for k in REQUIRED_CFG if k not in cfg]
    if missing: raise ValueError(f'config missing {missing}')
    if str(cfg['KT']) != SUPPORTED_KT: raise ValueError(f"KT={cfg['KT']!r} unsupported; this study is pinned to kappa_tilde={SUPPORTED_KT}")
    here = path.resolve().parent
    poly = here / cfg['poly']
    if sha_file(poly) != PINNED_POLY_SHA256: raise ValueError(f'coefficient table {poly.name} is not the pinned table')
    sem = {k: v for k, v in cfg.items() if k not in OPERATIONAL_KEYS}
    ident = dict(config_semantic_sha256=hashlib.sha256(json.dumps(sem, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
                 engine_sha256=sha_file(here / cfg['engine']), poly_sha256=sha_file(poly))
    return cfg, ident, here

# ---------------------------------------------------------------- exact plan
def tiles(h, rlo, rhi):
    h = Fr(h); rlo = Fr(rlo); rhi = Fr(rhi); side = 2*h; n = int(rhi/side) + 2; out = []
    for i in range(-n, n):
        for j in range(-n, n):
            x0, x1, y0, y1 = i*side, (i+1)*side, j*side, (j+1)*side
            dx = 0 if x0 <= 0 <= x1 else min(abs(x0), abs(x1)); dy = 0 if y0 <= 0 <= y1 else min(abs(y0), abs(y1))
            dmin2 = dx*dx + dy*dy; dmax2 = max(abs(x0), abs(x1))**2 + max(abs(y0), abs(y1))**2
            if dmin2 <= rhi*rhi and dmax2 >= rlo*rlo:
                out.append(dict(x0=x0, x1=x1, y0=y0, y1=y1, cx=x0+h, cy=y0+h, h=h,
                                # engine's box radii use |centre| -/+ h per coordinate (clipped at 0): exact squares
                                lower_sq=max(abs(x0+h)-h, Fr(0))**2 + max(abs(y0+h)-h, Fr(0))**2,
                                upper_sq=(abs(x0+h)+h)**2 + (abs(y0+h)+h)**2))
    return out
def tau_layers(cfg):
    lo, hi, ht = Fr(cfg['TAU_LO']), Fr(cfg['TAU_HI']), Fr(cfg['HTAU']); L = []; t = lo
    while t < hi: L.append((t, t + 2*ht)); t += 2*ht
    return L
def plan(cfg):
    P = {}
    for ring, h, rlo, rhi in (('inner', cfg['H_IN'], cfg['R_LO'], cfg['R_MID']), ('outer', cfg['H_OUT'], cfg['R_MID'], cfg['R_HI'])):
        for sq in tiles(h, rlo, rhi):
            for (ta, tb) in tau_layers(cfg):
                bid = f"{ring}_x{sq['x0']}_y{sq['y0']}_t{ta}"
                P[bid] = dict(id=bid, ring=ring, sq=sq, tau=(ta, tb), R_floor=Fr(rlo))
    return P

# ---------------------------------------------------------------- record validation
def D(sv):
    d = Decimal(str(sv))
    if not d.is_finite(): raise InvalidOperation('nonfinite')
    return d
def dsqrt(fr): return (Decimal(fr.numerator) / Decimal(fr.denominator)).sqrt()
def sigdigits(sv):
    d = D(sv).normalize(); return len(d.as_tuple().digits) if d != 0 else 1
NONNEG_FIELDS = ('K_up', 'K_raw', 'bound_B_up', 'centre_abs_up', 'trans_B_up', 'K_perp_up', 'rho_s', 'rho_c', 'lam_last',
                 'L_C', 'Rm_postmap', 'R_eff', 'Rmin', 'Rmax')
STEP_FIELDS = ('edge_bound', 'lam', 'fresh_s', 'fresh_c', 'rho_s', 'rho_c')
PUBLISHED = ('K_up', 'bound_B_up', 'centre_abs_up', 'trans_B_up', 'K_perp_up')
def validate(r, P, cfg, ident):
    """returns list of reasons; empty list = valid PASS record under this contract."""
    why = []
    if r.get('status') != 'PASS': return ['not PASS']
    if r.get('engine_sha256') != ident['engine_sha256']: why.append('engine_sha256')
    if r.get('poly_sha256') != ident['poly_sha256']: why.append('poly_sha256')
    if r.get('config_sha256') != ident['config_semantic_sha256']: why.append('config_sha256')
    b = P.get(r.get('box_id'))
    if b is None: return why + ['unknown box_id']
    sq = b['sq']; ta, tb = b['tau']; tol = Decimal(10) ** (-(int(cfg['DPS']) - 4))
    try:
        ep = r['endpoints']
        if [Fr(x) for x in ep['r']] != [sq['x0'], sq['x1']] or [Fr(x) for x in ep['e']] != [sq['y0'], sq['y1']] \
           or [Fr(x) for x in ep['tau']] != [ta, tb]: why.append('endpoints')
    except Exception: why.append('endpoints-parse')
    if r.get('N') not in cfg['N_LIST']: why.append('N')
    if r.get('K_deg') != int(cfg['K']): why.append('K_deg')
    if r.get('dps') != int(cfg['DPS']): why.append('dps')
    if str(r.get('kt')) != SUPPORTED_KT: why.append('kt')
    try:
        if Fr(r['R_floor']) != b['R_floor']: why.append('R_floor')
        if [Fr(x) for x in r['tau_plus']] != [ta + 1, tb + 1]: why.append('tau_plus')
    except Exception: why.append('R_floor/tau_plus-parse')
    try:
        v = {k: D(r[k]) for k in NONNEG_FIELDS}
        for k, x in v.items():
            if x < 0: why.append(f'{k}<0')
        # radii against the exact planned geometry
        rmin_true = dsqrt(sq['lower_sq']); rmax_true = dsqrt(sq['upper_sq']); rfl = Decimal(b['R_floor'].numerator) / Decimal(b['R_floor'].denominator)
        reff_true = max(rmin_true, rfl)
        if not (v['Rmin'] <= rmin_true + tol and v['Rmin'] >= rmin_true - tol): why.append('Rmin vs plan')
        if not (v['Rmax'] >= rmax_true - tol and v['Rmax'] <= rmax_true + tol): why.append('Rmax vs plan')
        if not (v['R_eff'] <= reff_true + tol and v['R_eff'] >= reff_true - tol): why.append('R_eff vs plan')
        if v['R_eff'] > v['Rmax']: why.append('R_eff>Rmax')
        # published constants
        for k in PUBLISHED:
            if sigdigits(r[k]) > 4: why.append(f'{k} digits')
        if v['K_up'] < v['K_raw']: why.append('K_up<K_raw')
        Np1 = int(r['N']) + 1
        if v['K_up'] * v['R_eff'] ** Np1 < v['bound_B_up'] / Decimal('1.001'): why.append('K_up inconsistent with bound_B_up/R_eff^(N+1)')
        if v['K_perp_up'] * v['R_eff'] ** Np1 < v['trans_B_up'] / Decimal('1.001'): why.append('K_perp_up inconsistent with trans_B_up')
        # six step records
        st = r['steps']
        if not isinstance(st, list) or len(st) != 6: why.append('steps!=6')
        else:
            for x in st:
                for k in STEP_FIELDS:
                    if D(x[k]) < 0: why.append(f'step {k}<0')
                cb = x['comp_bounds']
                if not isinstance(cb, list) or len(cb) != 4: why.append('comp_bounds len')
                else:
                    for c in cb:
                        if D(c) < 0: why.append('comp_bound<0')
            if D(st[-1]['rho_c']) != v['rho_c'] or D(st[-1]['rho_s']) != v['rho_s'] or D(st[-1]['lam']) != v['lam_last']:
                why.append('step/record mismatch')
    except (KeyError, TypeError, ValueError, InvalidOperation) as ex:
        why.append(f'field:{type(ex).__name__}:{str(ex)[:40]}')
    return why

def payload_hash(r):
    return hashlib.sha256(json.dumps({k: v for k, v in r.items() if k != 'seconds'}, sort_keys=True).encode()).hexdigest()

def collect(paths, P, cfg, ident):
    """returns accepted {key: record}, quarantined {key: [payload hashes]}, rejected [(key, reasons)], fails [(key, err)]."""
    valid = {}; rejected = []; fails = []
    for p in paths:
        p = Path(p)
        if not p.exists(): continue
        for ln, line in enumerate(p.read_text().splitlines(), 1):
            try: r = json.loads(line)
            except Exception: rejected.append(((str(p.name), ln), ['unparsable JSON'])); continue
            key = (r.get('box_id'), r.get('N'))
            if r.get('status') == 'FAIL': fails.append((key, r.get('error'))); continue
            why = validate(r, P, cfg, ident)
            if why: rejected.append((key, why)); continue
            valid.setdefault(key, {})[payload_hash(r)] = r
    accepted = {}; quarantined = {}
    for key, by in valid.items():
        if len(by) == 1: accepted[key] = next(iter(by.values()))
        else: quarantined[key] = sorted(by)
    return accepted, quarantined, rejected, fails
