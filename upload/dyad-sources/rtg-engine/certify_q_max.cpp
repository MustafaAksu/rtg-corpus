#include "rtg_core.hpp"
#include <iostream>

// Compute Q = rho^2 - rho*eta + eta^2
void compute_Q(ArbReal& Q, const DyadState& state) {
    ArbReal rho_sq, eta_sq, rho_eta;
    
    arb_mul(rho_sq.val, state.rho.val, state.rho.val, RTG_PREC);
    arb_mul(eta_sq.val, state.eta.val, state.eta.val, RTG_PREC);
    arb_mul(rho_eta.val, state.rho.val, state.eta.val, RTG_PREC);

    arb_add(Q.val, rho_sq.val, eta_sq.val, RTG_PREC);
    arb_sub(Q.val, Q.val, rho_eta.val, RTG_PREC);
}

int main() {
    std::cout << "╔══════════════════════════════════════════════════════════╗" << std::endl;
    std::cout << "║  RTG CONSTANT CERTIFIER: Q_max = Q^(2)(2.0)              ║" << std::endl;
    std::cout << "╚══════════════════════════════════════════════════════════╝" << std::endl;

    // Pulling DyadState directly from your rtg_core.hpp
    DyadState state;
    
    // Initialize exact point at q = 2.0 (Zero initial error)
    state.rho.set("0.0");
    state.eta.set("2.0");

    std::cout << "\n[ENG] Initializing exact point state (q = 2.0):" << std::endl;
    std::cout << "  rho_0: "; state.rho.print(15); std::cout << std::endl;
    std::cout << "  eta_0: "; state.eta.print(15); std::cout << std::endl;

    // Sub-branch (5,12) exits at exactly Step 12
    std::cout << "\n[ENG] Firing 12-step rigorous base map trajectory..." << std::endl;
    for (int k = 1; k <= 12; ++k) {
        state.step();
    }

    std::cout << "\n[ENG] Step 12 Exit Coordinates:" << std::endl;
    std::cout << "  rho_12: "; state.rho.print(25); std::cout << std::endl;
    std::cout << "  eta_12: "; state.eta.print(25); std::cout << std::endl;

    ArbReal Q_max;
    compute_Q(Q_max, state);

    std::cout << "\n========================================================" << std::endl;
    std::cout << "[RESULT] ARB-CERTIFIED INTERVAL CONSTANT" << std::endl;
    std::cout << "  Q_max = Q^(2)(2.0)" << std::endl;
    std::cout << "  Value: "; Q_max.print(25); std::cout << std::endl;
    std::cout << "========================================================" << std::endl;

    return 0;
}
