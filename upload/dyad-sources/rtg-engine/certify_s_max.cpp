#include "rtg_core.hpp"
#include <iostream>

// The F1 shear generator: g(\rho) = exp(\rho) - 1 - \rho^2 / 2
void compute_g(ArbReal& result, const ArbReal& rho_interval) {
    ArbReal exp_rho, rho_sq, half_rho_sq, temp;
    
    // exp(rho)
    arb_exp(exp_rho.val, rho_interval.val, RTG_PREC);
    
    // rho^2 / 2
    arb_mul(rho_sq.val, rho_interval.val, rho_interval.val, RTG_PREC);
    arb_div_ui(half_rho_sq.val, rho_sq.val, 2, RTG_PREC);
    
    // temp = exp(rho) - 1
    arb_sub_ui(temp.val, exp_rho.val, 1, RTG_PREC);
    
    // result = temp - (rho^2 / 2)
    arb_sub(result.val, temp.val, half_rho_sq.val, RTG_PREC);
}

int main() {
    std::cout << "[ENG] Initializing s_max^{F1} Constant Enclosure..." << std::endl;
    
    // The maximum occurs exactly at the upper domain boundary
    ArbReal upper_boundary;
    upper_boundary.set("0.50");
    
    std::cout << "\n[NUM] Evaluating g(rho) strictly at rho:" << std::endl;
    std::cout << "  "; upper_boundary.print(15); std::cout << std::endl;

    ArbReal s_max;
    compute_g(s_max, upper_boundary);

    std::cout << "\n========================================================" << std::endl;
    std::cout << "[RESULT] CERTIFIED ENCLOSURE: s_max^{F1}" << std::endl;
    std::cout << "  "; s_max.print(25); std::cout << std::endl;
    std::cout << "========================================================" << std::endl;

    return 0;
}
