#include "rtg_core.hpp"
#include <iostream>

struct DyadStateVar {
    ArbReal rho, eta, drho, deta;

    void step() {
        ArbReal sin_e, cos_e, exp_r, one;
        one.set("1");
        
        arb_sin_cos(sin_e.val, cos_e.val, eta.val, RTG_PREC);
        arb_exp(exp_r.val, rho.val, RTG_PREC);

        // Variational
        ArbReal t_cos_deta, drho_next;
        arb_mul(t_cos_deta.val, cos_e.val, deta.val, RTG_PREC);
        arb_sub(drho_next.val, drho.val, t_cos_deta.val, RTG_PREC);

        ArbReal t_exp_drho, t_one_minus_cos, t_omc_deta, deta_next;
        arb_mul(t_exp_drho.val, exp_r.val, drho.val, RTG_PREC);
        arb_sub(t_one_minus_cos.val, one.val, cos_e.val, RTG_PREC);
        arb_mul(t_omc_deta.val, t_one_minus_cos.val, deta.val, RTG_PREC);
        arb_add(deta_next.val, t_exp_drho.val, t_omc_deta.val, RTG_PREC);

        // Base Map
        ArbReal rho_next, eta_next, temp;
        arb_sub(rho_next.val, rho.val, sin_e.val, RTG_PREC);
        
        arb_add(temp.val, eta.val, exp_r.val, RTG_PREC);
        arb_sub_ui(temp.val, temp.val, 1, RTG_PREC);
        arb_sub(eta_next.val, temp.val, sin_e.val, RTG_PREC);

        arb_set(rho.val, rho_next.val);
        arb_set(eta.val, eta_next.val);
        arb_set(drho.val, drho_next.val);
        arb_set(deta.val, deta_next.val);
    }
};

void compute_dQ(ArbReal& dQ, const DyadStateVar& state) {
    ArbReal two_rho, two_eta, term1, term2, partA, partB;
    arb_mul_ui(two_rho.val, state.rho.val, 2, RTG_PREC);
    arb_mul_ui(two_eta.val, state.eta.val, 2, RTG_PREC);

    arb_sub(term1.val, two_rho.val, state.eta.val, RTG_PREC);
    arb_sub(term2.val, two_eta.val, state.rho.val, RTG_PREC);

    arb_mul(partA.val, term1.val, state.drho.val, RTG_PREC);
    arb_mul(partB.val, term2.val, state.deta.val, RTG_PREC);

    arb_add(dQ.val, partA.val, partB.val, RTG_PREC);
}

struct CertZone {
    const char* q_lo;
    const char* q_hi;
    int slices;
};

int main() {
    std::cout << "[ENG] Initializing IA Certifier: Sub-branch (4,10)" << std::endl;
    std::cout << "[ENG] FIX 1: Arb slice boundaries (no double accumulation)" << std::endl;
    std::cout << "[ENG] FIX 2: Orbit structure certified (pre-crossing at steps 4,10 only)" << std::endl;
    std::cout << "[ENG] FIX 3: 5-Zone Fibonacci Grid (Mathematically bounded Signal-to-Noise)" << std::endl;
    std::cout << std::endl;

    const slong PREC = RTG_PREC;
    
    // The exact analytical grid to ensure 2700*delta < q^2/2
    CertZone zones[5] = {
        {"0.001", "0.002", 10000000}, // Zone 1: delta = 1.0e-10 (Crushes the core noise)
        {"0.002", "0.005", 10000000}, // Zone 2: delta = 3.0e-10
        {"0.005", "0.02",  10000000}, // Zone 3: delta = 1.5e-9
        {"0.02",  "0.1",   10000000}, // Zone 4: delta = 8.0e-9
        {"0.1",   "0.9",   20000000}  // Zone 5: delta = 4.0e-8 (Macroscopic branch)
    };

    bool certified = true;
    int structure_fails = 0;
    int positivity_fails = 0;
    ArbReal global_min_dQ;
    global_min_dQ.set("1000.0");

    for (int z = 0; z < 5; ++z) {
        ArbReal q_domain_lo, q_domain_hi, total_width, arb_slices;
        q_domain_lo.set(zones[z].q_lo);
        q_domain_hi.set(zones[z].q_hi);
        arb_sub(total_width.val, q_domain_hi.val, q_domain_lo.val, PREC);

        arb_set_si(arb_slices.val, zones[z].slices);
        ArbReal slice_width;
        arb_div(slice_width.val, total_width.val, arb_slices.val, PREC);

        std::cout << "[ENG] ----------------------------------------------------" << std::endl;
        std::cout << "[ENG] Processing Zone " << (z+1) << ": [" << zones[z].q_lo << ", " << zones[z].q_hi << "]" << std::endl;
        std::cout << "[ENG] Slices: " << zones[z].slices << " | Width: "; slice_width.print(12); std::cout << std::endl;

        for (int i = 0; i < zones[z].slices; ++i) {
            ArbReal arb_i, q_lo, q_hi, q_interval;
            arb_set_si(arb_i.val, i);

            ArbReal offset_lo, offset_hi;
            arb_mul(offset_lo.val, arb_i.val, slice_width.val, PREC);
            arb_set_si(arb_i.val, i + 1);
            arb_mul(offset_hi.val, arb_i.val, slice_width.val, PREC);

            arb_add(q_lo.val, q_domain_lo.val, offset_lo.val, PREC);
            arb_add(q_hi.val, q_domain_lo.val, offset_hi.val, PREC);
            arb_union(q_interval.val, q_lo.val, q_hi.val, PREC);

            DyadStateVar state;
            state.rho.set("0.0");
            arb_set(state.eta.val, q_interval.val);
            state.drho.set("0.0");
            state.deta.set("1.0");

            bool slice_ok = true;

            for (int k = 1; k <= 10; ++k) {
                ArbReal sin_eta_val, diff_val;
                arb_sin(sin_eta_val.val, state.eta.val, PREC);
                arb_sub(diff_val.val, state.rho.val, sin_eta_val.val, PREC);

                bool rho_strictly_neg = arb_is_negative(state.rho.val);
                bool sineta_strictly_neg = arb_is_negative(sin_eta_val.val);
                bool diff_nonneg = arb_is_nonnegative(diff_val.val);

                bool is_pc_certified = rho_strictly_neg && sineta_strictly_neg && diff_nonneg;

                bool rho_nonneg = arb_is_nonnegative(state.rho.val);
                bool sineta_nonneg = arb_is_nonnegative(sin_eta_val.val);
                bool diff_strictly_neg = arb_is_negative(diff_val.val);
                bool not_pc_certified = rho_nonneg || sineta_nonneg || diff_strictly_neg;

                if (k == 4 || k == 10) {
                    if (!is_pc_certified) {
                        slice_ok = false;
                        structure_fails++;
                        if (structure_fails <= 5) {
                            std::cout << "[STRUCT FAIL] Step " << k << " should be PC at slice " << i << std::endl;
                        }
                        break;
                    }
                } else {
                    if (!not_pc_certified) {
                        slice_ok = false;
                        structure_fails++;
                        if (structure_fails <= 5) {
                            std::cout << "[STRUCT FAIL] Step " << k << " should not be PC at slice " << i << std::endl;
                        }
                        break;
                    }
                }
                state.step();
            }

            if (!slice_ok) { certified = false; break; }

            ArbReal dQ;
            compute_dQ(dQ, state);

            if (!arb_is_positive(dQ.val)) {
                positivity_fails++;
                certified = false;
                std::cout << "[FATAL] dQ/dq not certified > 0 at slice " << i << std::endl;
                break;
            }

            if (arb_lt(dQ.val, global_min_dQ.val)) {
                arb_set(global_min_dQ.val, dQ.val);
            }

            // Print progress for larger zones
            if ((i + 1) % 5000000 == 0) {
                std::cout << "  ... " << ((i + 1) / 1000000) << "M slices certified in Zone " << (z+1) << "." << std::endl;
            }
        }
        if (!certified) break;
    }

    std::cout << "\n========================================================" << std::endl;
    if (certified) {
        std::cout << "[RESULT] [ALG via IA] CERTIFIED: dQ^(2)/dq > 0 for sub-branch (4,10)." << std::endl;
        std::cout << "  Domain:  q in [0.001, 0.9] (5-Zone SNR Guarded)" << std::endl;
        std::cout << "  Orbit:   pre-crossings at steps {4,10} only — certified per slice" << std::endl;
        std::cout << "  Min dQ lower bound (Arb): "; global_min_dQ.print(10); std::cout << std::endl;
        std::cout << "\n  DSN entry: [ALG via IA] T1 sub-branch (4,10)" << std::endl;
        std::cout << "    Q^(2)(q) strictly increasing on (0.001, 0.9]" << std::endl;
    } else {
        std::cout << "[RESULT] CERTIFICATE FAILED." << std::endl;
        std::cout << "  Structure failures: " << structure_fails << " | Positivity failures: " << positivity_fails << std::endl;
    }
    std::cout << "========================================================" << std::endl;
    
    return certified ? 0 : 1;
}
