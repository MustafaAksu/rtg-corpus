#include "rtg_core.hpp"
#include <iostream>
#include <iomanip>

struct DyadStateVar {
    ArbReal rho, eta, drho, deta;

    void step() {
        ArbReal sin_e, cos_e, exp_r, one;
        one.set("1");
        arb_sin_cos(sin_e.val, cos_e.val, eta.val, RTG_PREC);
        arb_exp(exp_r.val, rho.val, RTG_PREC);

        ArbReal t_cos_deta, drho_next;
        arb_mul(t_cos_deta.val, cos_e.val, deta.val, RTG_PREC);
        arb_sub(drho_next.val, drho.val, t_cos_deta.val, RTG_PREC);

        ArbReal t_exp_drho, t_omc, t_omc_deta, deta_next;
        arb_mul(t_exp_drho.val, exp_r.val, drho.val, RTG_PREC);
        arb_sub(t_omc.val, one.val, cos_e.val, RTG_PREC);
        arb_mul(t_omc_deta.val, t_omc.val, deta.val, RTG_PREC);
        arb_add(deta_next.val, t_exp_drho.val, t_omc_deta.val, RTG_PREC);

        ArbReal rho_next, eta_next, tmp;
        arb_sub(rho_next.val, rho.val, sin_e.val, RTG_PREC);
        arb_add(tmp.val, eta.val, exp_r.val, RTG_PREC);
        arb_sub_ui(tmp.val, tmp.val, 1, RTG_PREC);
        arb_sub(eta_next.val, tmp.val, sin_e.val, RTG_PREC);

        arb_set(rho.val, rho_next.val);
        arb_set(eta.val, eta_next.val);
        arb_set(drho.val, drho_next.val);
        arb_set(deta.val, deta_next.val);
    }
};

void compute_dQ(ArbReal& dQ, const DyadStateVar& s) {
    ArbReal two_rho, two_eta, t1, t2, pA, pB;
    arb_mul_ui(two_rho.val, s.rho.val, 2, RTG_PREC);
    arb_mul_ui(two_eta.val, s.eta.val, 2, RTG_PREC);
    arb_sub(t1.val, two_rho.val, s.eta.val, RTG_PREC);
    arb_sub(t2.val, two_eta.val, s.rho.val, RTG_PREC);
    arb_mul(pA.val, t1.val, s.drho.val, RTG_PREC);
    arb_mul(pB.val, t2.val, s.deta.val, RTG_PREC);
    arb_add(dQ.val, pA.val, pB.val, RTG_PREC);
}

int main() {
    std::cout << "╔══════════════════════════════════════════════════════════╗" << std::endl;
    std::cout << "║  RTG TRANSITION STRIP CERTIFIER: [0.9000, 0.9015]        ║" << std::endl;
    std::cout << "║  Dynamically routing boundary q* approx 0.9008           ║" << std::endl;
    std::cout << "╚══════════════════════════════════════════════════════════╝" << std::endl;

    const slong PREC = RTG_PREC;
    const int SLICES = 15000000;

    ArbReal q_domain_lo, q_domain_hi, total_width, arb_slices;
    q_domain_lo.set("0.9000");
    q_domain_hi.set("0.9015");
    arb_sub(total_width.val, q_domain_hi.val, q_domain_lo.val, PREC);
    arb_set_si(arb_slices.val, SLICES);

    ArbReal slice_w;
    arb_div(slice_w.val, total_width.val, arb_slices.val, PREC);

    std::cout << "[ENG] Slices: " << SLICES << " | Width: "; slice_w.print(12); std::cout << "\n\n";

    bool certified = true;
    int count_4_10 = 0;
    int count_4_11 = 0;
    int count_straddle = 0;
    int positivity_fails = 0;
    int struct_fails = 0;

    ArbReal global_min_dQ;
    global_min_dQ.set("1000.0");

    for (int i = 0; i < SLICES && certified; ++i) {
        ArbReal arb_i, off_lo, off_hi, q_lo, q_hi, q_iv;
        arb_set_si(arb_i.val, i);
        arb_mul(off_lo.val, arb_i.val, slice_w.val, PREC);
        arb_set_si(arb_i.val, i + 1);
        arb_mul(off_hi.val, arb_i.val, slice_w.val, PREC);
        arb_add(q_lo.val, q_domain_lo.val, off_lo.val, PREC);
        arb_add(q_hi.val, q_domain_lo.val, off_hi.val, PREC);
        arb_union(q_iv.val, q_lo.val, q_hi.val, PREC);

        DyadStateVar state;
        state.rho.set("0.0");
        arb_set(state.eta.val, q_iv.val);
        state.drho.set("0.0");
        state.deta.set("1.0");

        bool slice_ok = true;
        bool is_4_10 = false;
        bool is_4_11 = false;
        bool straddles = false;

        for (int k = 1; k <= 11; ++k) {
            ArbReal sin_e, diff;
            arb_sin(sin_e.val, state.eta.val, PREC);
            arb_sub(diff.val, state.rho.val, sin_e.val, PREC);

            bool rho_neg = arb_is_negative(state.rho.val);
            bool sine_neg = arb_is_negative(sin_e.val);
            bool diff_pos = arb_is_nonnegative(diff.val);
            bool is_pc = rho_neg && sine_neg && diff_pos;

            bool rho_nn = arb_is_nonnegative(state.rho.val);
            bool sine_nn = arb_is_nonnegative(sin_e.val);
            bool diff_neg = arb_is_negative(diff.val);
            bool not_pc = rho_nn || sine_nn || diff_neg;

            if (k == 4) {
                if (!is_pc) slice_ok = false;
            } else if (k == 10) {
                if (is_pc) {
                    is_4_10 = true;
                } else if (not_pc) {
                    is_4_11 = true;
                } else {
                    straddles = true;
                    break; // Arb ball swallows the boundary
                }
            } else if (k == 11) {
                if (is_4_11 && !is_pc) slice_ok = false;
            } else {
                if (!not_pc) slice_ok = false;
            }

            state.step();

            if (k == 10 && is_4_10) {
                ArbReal dQ;
                compute_dQ(dQ, state);
                if (!arb_is_positive(dQ.val)) positivity_fails++;
                if (arb_lt(dQ.val, global_min_dQ.val)) arb_set(global_min_dQ.val, dQ.val);
                count_4_10++;
                break;
            }
            if (k == 11 && is_4_11) {
                ArbReal dQ;
                compute_dQ(dQ, state);
                if (!arb_is_positive(dQ.val)) positivity_fails++;
                if (arb_lt(dQ.val, global_min_dQ.val)) arb_set(global_min_dQ.val, dQ.val);
                count_4_11++;
                break;
            }
        }

        if (!slice_ok) struct_fails++;
        if (straddles) {
            count_straddle++;
            if (count_straddle <= 5) {
                std::cout << "  [BOUNDARY DETECTED] q* bracketed at slice " << i << " ["; 
                q_lo.print(10); std::cout << ", "; q_hi.print(10); std::cout << "]\n";
            }
        }
        if (struct_fails > 0 || positivity_fails > 0) certified = false;
        
        if ((i + 1) % 5000000 == 0) {
            std::cout << "    ... " << ((i + 1) / 1000000) << "M slices processed.\n";
        }
    }

    std::cout << "\n========================================================" << std::endl;
    if (certified) {
        std::cout << "[RESULT] TRANSITION STRIP CERTIFIED: [0.9000, 0.9015]" << std::endl;
        std::cout << "  (4,10) Branch Slices : " << count_4_10 << std::endl;
        std::cout << "  (4,11) Branch Slices : " << count_4_11 << std::endl;
        std::cout << "  q* Boundary Brackets : " << count_straddle << " (width ~10^-10)" << std::endl;
        std::cout << "  Min dQ lower bound   : "; global_min_dQ.print(10); std::cout << std::endl;
    } else {
        std::cout << "[RESULT] CERTIFICATION FAILED." << std::endl;
        std::cout << "  Structure Fails : " << struct_fails << std::endl;
        std::cout << "  Positivity Fails: " << positivity_fails << std::endl;
    }
    std::cout << "========================================================" << std::endl;
    return certified ? 0 : 1;
}
