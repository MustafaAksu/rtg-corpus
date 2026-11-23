# generate_block_csv.py
#
# Generates the m,Q,Theta (and optional dTheta) CSV required by spiral_phase_fit.py.
# Runs the exact primitive map at dps=120, samples every p steps,
# records block index m, amplitude Q_Z, and phase Theta_Z.
#
# Usage:
#   python generate_block_csv.py --p 6 --r0 0.5 --blocks 500000 --warmup 10000 --compute-dtheta --out p6_blocks.csv
#   python generate_block_csv.py --p 5 --r0 0.5 --tau 1.5200741649688346 --blocks 500000 --warmup 10000 --out p5_blocks.csv
#
# DSN compliance:
#   - Uses Q_true = rho^2 - rho*eta + eta^2 for p=6 (K6=1)
#   - Uses Q_Z    = rho^2 - rho*eta + eta^2/K5 for p=5
#   - Theta_Z = atan2(Im(Z_p), Re(Z_p)) in the correct frame
#   - All at dps=120

import argparse, csv, os
import mpmath as mp

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--p',              type=int,   required=True)
    parser.add_argument('--r0',             type=float, default=0.5)
    parser.add_argument('--eta0',           type=float, default=0.0)
    parser.add_argument('--blocks',         type=int,   default=500000)
    parser.add_argument('--warmup',         type=int,   default=10000)
    parser.add_argument('--out',            type=str,   required=True)
    parser.add_argument('--dps',            type=int,   default=120)
    parser.add_argument('--stride',         type=int,   default=1,
                        help='Write every stride-th block (reduces file size)')
    parser.add_argument('--compute-dtheta', action='store_true',
                        help='Compute and append dTheta column for phase increment fitting')
    args = parser.parse_args()

    mp.mp.dps = args.dps
    p = args.p

    sqrt5 = mp.sqrt(5)
    s5    = mp.sqrt(10 + 2*sqrt5)
    K5    = (5 - sqrt5)/2
    sqrt3 = mp.sqrt(3)

    if p == 6:
        K = mp.mpf(1)
        def one_step(r, e):
            s = mp.sin(e); ex = mp.exp(r)-1
            return r-s, e+ex-s
        def QZ(r, e): return r**2 - r*e + e**2
        def ThZ(r, e): return mp.atan2(sqrt3/2*e, r-e/2)
        tau_dsn = mp.nstr(2*sqrt3/3, 20)
        C_dsn   = '6'
    elif p == 5:
        K = K5
        def one_step(r, e):
            s = mp.sin(e); ex = mp.exp(r)-1
            return r-s, e+K5*(ex-s)
        def QZ(r, e): return r**2 - r*e + e**2/K5
        def ThZ(r, e):
            return mp.atan2(mp.sin(2*mp.pi/5)/K5*e, r-e/2)
        tau5  = (115-50*sqrt5)*s5/8
        tau_dsn = mp.nstr(tau5, 20)
        # C_5 = (7+3*sqrt5)/5 [ALG]
        C5 = (7+3*sqrt5)/5
        C_dsn = mp.nstr(C5, 20)
    else:
        raise ValueError(f"p={p} not supported; add K_p and frame formulas.")

    rho = mp.mpf(str(args.r0))
    eta = mp.mpf(str(args.eta0))

    if args.compute_dtheta and args.stride != 1:
        print("[WARNING] --compute-dtheta used with stride != 1. dTheta will represent phase change over multiple blocks.")

    print(f"Generating p={p} block CSV: {args.blocks} blocks, warmup={args.warmup}")
    print(f"  r0={args.r0}, eta0={args.eta0}, dps={args.dps}, stride={args.stride}")
    print(f"  DSN tau={tau_dsn},  C={C_dsn}")
    print(f"  Output: {args.out}")

    # Warmup
    print(f"  Warming up ({args.warmup} blocks)...")
    for _ in range(args.warmup):
        for _ in range(p): rho, eta = one_step(rho, eta)

    os.makedirs(os.path.dirname(args.out) if os.path.dirname(args.out) else '.', exist_ok=True)

    # If computing dTheta, capture the phase immediately after warmup as the baseline
    prev_Th = None
    if args.compute_dtheta:
        prev_Th = ThZ(rho, eta)

    written = 0
    with open(args.out, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        headers = ['m', 'Q', 'Theta']
        if args.compute_dtheta:
            headers.append('dTheta')
        writer.writerow(headers)
        
        print(f"  Collecting {args.blocks} blocks...")
        for blk in range(args.blocks):
            for _ in range(p): rho, eta = one_step(rho, eta)
            
            if blk % args.stride == 0:
                Q  = QZ(rho, eta)
                Th = ThZ(rho, eta)
                
                row = [blk + 1, mp.nstr(Q, 30), mp.nstr(Th, 30)]
                
                if args.compute_dtheta:
                    # Calculate phase difference and handle 2pi wrapping safely
                    dTh = (Th - prev_Th + mp.pi) % (2 * mp.pi) - mp.pi
                    row.append(mp.nstr(dTh, 30))
                    prev_Th = Th
                    
                writer.writerow(row)
                written += 1
                
            if blk % 50000 == 0 and blk > 0:
                Q_val = QZ(rho, eta)
                print(f"    block {args.warmup+blk}: Q={float(Q_val):.4e}")

    print(f"  Done. Wrote {written} rows to {args.out}")
    print(f"  Suggested fit command (using relative block indices):")
    if p == 6:
        print(f"    python spiral_phase_fit_route2_corrected.py --input {args.out} "
              f"--m-min 1 --m-max {args.blocks} "
              f"--json-out outputs/p{p}_spiral_fit.json")
    else:
        print(f"    python spiral_phase_fit_route2_corrected.py --input {args.out} "
              f"--m-min 1 --m-max {args.blocks} "
              f"--json-out outputs/p{p}_spiral_fit.json")

if __name__ == '__main__':
    main()