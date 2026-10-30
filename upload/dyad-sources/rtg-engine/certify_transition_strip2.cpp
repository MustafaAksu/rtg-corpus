#include "flint/arb.h"
#include "flint/arb_mat.h"
#include <iostream>

// The dyad step with variational propagation (safe from aliasing if inputs != outputs)
void dyad_step_with_variational(arb_t rho_next, arb_t eta_next, arb_t V_rho_next, arb_t V_eta_next, 
                                const arb_t rho, const arb_t eta, const arb_t V_rho, const arb_t V_eta, slong prec) {
    arb_t sin_eta, cos_eta, exp_rho, term1, term2;
    arb_init(sin_eta); arb_init(cos_eta); arb_init(exp_rho);
    arb_init(term1); arb_init(term2);

    arb_sin_cos(sin_eta, cos_eta, eta, prec);
    arb_exp(exp_rho, rho, prec);

    // Base State
    arb_sub(rho_next, rho, sin_eta, prec); 
    arb_sub(term1, exp_rho, sin_eta, prec); 
    arb_sub_ui(term1, term1, 1, prec);      
    arb_add(eta_next, eta, term1, prec);    

    // Variational State (J * V)
    // J11 = 1, J12 = -cos(eta)
    arb_mul(term1, cos_eta, V_eta, prec);
    arb_sub(V_rho_next, V_rho, term1, prec); // V_rho - cos(eta)*V_eta

    // J21 = exp(rho), J22 = 1 - cos(eta)
    arb_mul(term1, exp_rho, V_rho, prec);
    arb_sub_ui(term2, cos_eta, 1, prec);
    arb_neg(term2, term2); // 1 - cos(eta)
    arb_mul(term2, term2, V_eta, prec);
    arb_add(V_eta_next, term1, term2, prec);

    arb_clear(sin_eta); arb_clear(cos_eta); arb_clear(exp_rho);
    arb_clear(term1); arb_clear(term2);
}

// Function to propagate a single launch interval 'q_init'
void evaluate_orbit(arb_t F, arb_t Fprime, const arb_t q_init, slong prec) {
    arb_t rho, eta, V_rho, V_eta;
    arb_init(rho); arb_init(eta); arb_init(V_rho); arb_init(V_eta);

    arb_zero(rho);
    arb_set(eta, q_init);
    arb_zero(V_rho);
    arb_one(V_eta);

    for (int n = 0; n < 9; n++) {
        arb_t rho_new, eta_new, Vr_new, Ve_new;
        arb_init(rho_new); arb_init(eta_new); arb_init(Vr_new); arb_init(Ve_new);

        dyad_step_with_variational(rho_new, eta_new, Vr_new, Ve_new, rho, eta, V_rho, V_eta, prec);

        arb_set(rho, rho_new); arb_set(eta, eta_new);
        arb_set(V_rho, Vr_new); arb_set(V_eta, Ve_new);

        arb_clear(rho_new); arb_clear(eta_new); arb_clear(Vr_new); arb_clear(Ve_new);
    }

    arb_t cos_eta10, term;
    arb_init(cos_eta10); arb_init(term);
    
    // F(q) = rho_10 - sin(eta_10)
    arb_sin_cos(term, cos_eta10, eta, prec);
    arb_sub(F, rho, term, prec);

    // F'(q) = V_rho_10 - cos(eta_10) * V_eta_10
    arb_mul(term, cos_eta10, V_eta, prec);
    arb_sub(Fprime, V_rho, term, prec);

    arb_clear(rho); arb_clear(eta); arb_clear(V_rho); arb_clear(V_eta);
    arb_clear(cos_eta10); arb_clear(term);
}

int main() {
    slong prec = 256; 
    
    // The straddle interval: [q_minus, q_plus]
    // Width ~ 4e-7 around 0.900491389
    arb_t q_interval, q_minus, q_plus;
    arb_init(q_interval); arb_init(q_minus); arb_init(q_plus);

    arb_set_str(q_minus, "0.9004911", prec);
    arb_set_str(q_plus, "0.9004916", prec);
    
    // Create the interval ball enclosing the entire strip
    arb_union(q_interval, q_minus, q_plus, prec);

    arb_t F_minus, Fprime_minus, F_plus, Fprime_plus, F_interval, Fprime_interval;
    arb_init(F_minus); arb_init(Fprime_minus); arb_init(F_plus); arb_init(Fprime_plus);
    arb_init(F_interval); arb_init(Fprime_interval);

    // 1. Check endpoints for sign separation
    evaluate_orbit(F_minus, Fprime_minus, q_minus, prec);
    evaluate_orbit(F_plus, Fprime_plus, q_plus, prec);

    std::cout << "F(q_minus) at step 10: "; arb_printn(F_minus, 10, 0); std::cout << "\n";
    std::cout << "F(q_plus) at step 10:  "; arb_printn(F_plus, 10, 0); std::cout << "\n";

    // 2. Check full interval for strict monotonicity
    evaluate_orbit(F_interval, Fprime_interval, q_interval, prec);
    
    std::cout << "F'(q_interval) over full strip: "; arb_printn(Fprime_interval, 10, 0); std::cout << "\n";

    if ((arb_is_positive(F_plus) && arb_is_negative(F_minus)) || (arb_is_negative(F_plus) && arb_is_positive(F_minus))) {
        std::cout << "[SUCCESS] Endpoint sign separation verified. Root exists.\n";
    } else {
        std::cout << "[FAIL] Endpoints do not strictly separate zero.\n";
    }

    if (arb_is_positive(Fprime_interval) || arb_is_negative(Fprime_interval)) {
        std::cout << "[SUCCESS] 0 not in F'(I). Monotonicity verified. Transversality proven. IFT applies.\n";
    } else {
        std::cout << "[FAIL] F'(I) encloses zero. Cannot prove transversality over the full interval.\n";
    }

    arb_clear(q_interval); arb_clear(q_minus); arb_clear(q_plus);
    arb_clear(F_minus); arb_clear(Fprime_minus); arb_clear(F_plus); arb_clear(Fprime_plus);
    arb_clear(F_interval); arb_clear(Fprime_interval);
    
    return 0;
}
