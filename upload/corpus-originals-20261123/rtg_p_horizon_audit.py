#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RTG p-Horizon Audit Orchestrator
================================
Master CLI for OPEN 9 Arithmetic Horizon sub-studies.
Status: [ENG/NUM audit orchestrator with ALG micro-certification mode]
"""

import argparse
import rtg_p_core as core
import rtg_p_subgroup as subgroup
import rtg_p_normalform as normalform
import rtg_p_certs as certs

def run_subgroup(args):
    print(f"\n--- RTG Subgroup Extra-Jet Audit (D={args.D}) ---")
    print("Convention: raw Birkhoff-strobe")
    print("Object: J_extra_raw = Π_extra[τ≤D(L_p^(-s) f_p^s) - Id]")

    for p in args.p:
        res = subgroup.analyze_subgroups(p, args.D, args.tol)
        print("=" * 60)
        print(f"Horizon p={p} | Prime: {res['is_prime']}")

        if res["is_prime"]:
            print("  Proper subgroup domain: empty")
            print("  C_sub_mult=0, C_sub_uniq=0, Delta_overlap=0 vacuously")
            continue

        print(
            f"  Aggregates: C_sub_mult={res['C_sub_mult']}, "
            f"C_sub_uniq={res['C_sub_uniq']}, "
            f"Delta={res['Delta_overlap']}"
        )
        print(f"  L2 Mass: {res['mass_mult_L2']:.6e}")

        for q, d in res["q_data"].items():
            print(f"  -> Subgroup q={q} (s={d['s']})")
            print(f"     K_extra: {d['K_extra']} | B_extra Size: {d['B_extra_size']}")
            print(f"     Support: {d['supp']} | Z_miss: {d['Z_miss']} | R_occ: {d['R_occ']:.4f}")

            if d["sanity_pass"]:
                print("     Sanity: supp(J_extra_raw) ⊆ B_extra : PASS")
            else:
                print(f"     [!] SANITY FAIL: Support outside B_extra: {d['outside_slots']}")

            if "mass_L1" in d:
                print(f"     Mass L1: {d['mass_L1']:.6e}")
            if "mass_L2" in d:
                print(f"     Mass L2: {d['mass_L2']:.6e}")

            if d["Z_miss"] > 0:
                print(f"     Missing Slots: {d['missing_slots']}")

def run_normalform(args):
    print(f"\n--- RTG 1-Step Normal Form & Bridge Gap Audit (D={args.D}) ---")
    for p in args.p:
        res = normalform.analyze_normal_form(p, args.D, args.tol, backend=args.backend, dps=args.dps)
        print("=" * 60)
        print(f"Horizon p={p}")
        
        # Strict backend hygiene
        dps_str = f" (dps={res.get('dps', 'NA')})" if res.get('backend') != 'native-float' else ""
        print(f"  Backend: {res.get('backend', 'unknown')}{dps_str}")
        print(f"  Object: bridge_gap = F_1^p - F_raw^p")
        print(f"  Convention: one-step homological normalized vs raw accumulated")
        print(f"  Resonant Channels Retained (Raw vs NF): {len(res['raw_retained_coeffs'])} vs {len(res['nf_retained_coeffs'])}")
        
        if res['lattice_visible']:
            val = res['gap_lattice']
            print(f"  Lattice Harmonic (0, {p-1}) visible. Bridge Gap: {abs(val):.6e}")
        else:
            print(f"  Lattice Harmonic (0, {p-1}) requires D>={p-1} (Not visible at D={args.D})")
            
        print(f"  Bridge Gap L1 over reported support: {sum(abs(v) for v in res['bridge_gap'].values()):.6e}")

def run_certify(args):
    print("\n--- RTG Exact Symbolic Certification ---")
    if getattr(args, 'list_cases', False):
        certs.list_cases()
        return
    if not getattr(args, 'case', None):
        raise ValueError("Provide --case <id> or --list-cases.")
    certs.run_cert(args.case)

def run_all(args):
    print("\n[Executing Full OPEN 9 Baseline Audit]")
    run_subgroup(args)
    run_normalform(args)
    print("\n--- RTG Exact Symbolic Certification (Smoke Tests) ---")
    certs.run_cert("p6_q3_02")
    certs.run_cert("p12_q4_03")

def main():
    parser = argparse.ArgumentParser(description="RTG p-Horizon Audit Master CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    p_sub = subparsers.add_parser("subgroup", help="Audit proper subgroup strobes (J_extra)")
    p_sub.add_argument("--p", nargs='+', type=int, required=True)
    p_sub.add_argument("--D", type=int, default=7)
    p_sub.add_argument("--tol", type=float, default=1e-11)
    
    p_nf = subparsers.add_parser("normalform", help="Audit 1-step normalization and bridge gaps")
    p_nf.add_argument("--p", nargs='+', type=int, required=True)
    p_nf.add_argument("--D", type=int, default=5)
    p_nf.add_argument("--tol", type=float, default=1e-11)
    p_nf.add_argument("--backend", choices=["native-float", "mpmath", "exact"], default="native-float")
    p_nf.add_argument("--dps", type=int, default=80)
    
    p_cert = subparsers.add_parser("certify", help="Execute exact symbolic micro-proofs")
    p_cert.add_argument("--case", type=str, default=None, help="e.g., p6_q3_02")
    p_cert.add_argument("--list-cases", action="store_true", help="List all available exact certification cases")

    p_all = subparsers.add_parser("all", help="Run subgroup, normalform, and core certifications")
    p_all.add_argument("--p", nargs='+', type=int, required=True)
    p_all.add_argument("--D", type=int, default=7) 
    p_all.add_argument("--tol", type=float, default=1e-11)
    p_all.add_argument("--backend", choices=["native-float", "mpmath", "exact"], default="native-float")
    p_all.add_argument("--dps", type=int, default=80)
    
    args = parser.parse_args()
    
    if args.command == "subgroup": run_subgroup(args)
    elif args.command == "normalform": run_normalform(args)
    elif args.command == "certify": run_certify(args)
    elif args.command == "all": run_all(args)

if __name__ == "__main__":
    main()