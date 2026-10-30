#include "rtg_core.hpp"
#include <iostream>
#include <vector>

// The rigorous derivative: g'(\rho) = exp(\rho) - 1 - \rho
void compute_g_prime(ArbReal& result, const ArbReal& rho_interval) {
    ArbReal exp_rho;
    arb_exp(exp_rho.val, rho_interval.val, RTG_PREC);

    ArbReal temp;
    arb_sub_ui(temp.val, exp_rho.val, 1, RTG_PREC); 
    arb_sub(result.val, temp.val, rho_interval.val, RTG_PREC); 
}

int main() {
    std::cout << "[ENG] Initializing g(rho) Monotonicity Certifier (Subdivision Method)..." << std::endl;
    
    // Define the domain and subdivision density
    double start_domain = 0.05;
    double end_domain = 0.50;
    int slices = 1000;
    double step = (end_domain - start_domain) / slices;

    bool strictly_monotonic = true;

    std::cout << "\n[ENG] Scanning " << slices << " rigorous interval slices..." << std::endl;

    for (int i = 0; i < slices; ++i) {
        double slice_start = start_domain + (i * step);
        double slice_end = slice_start + step;

        // Convert doubles to strings to safely initialize the Arb types without float-loss
        char start_str[32], end_str[32];
        snprintf(start_str, sizeof(start_str), "%.6f", slice_start);
        snprintf(end_str, sizeof(end_str), "%.6f", slice_end);

        ArbReal lower, upper, domain_slice, g_prime;
        lower.set(start_str);
        upper.set(end_str);
        
        // Create the rigorous sub-interval
        arb_union(domain_slice.val, lower.val, upper.val, RTG_PREC);

        // Evaluate the derivative on this specific tiny slice
        compute_g_prime(g_prime, domain_slice);

        // If even a single slice contains 0 or goes negative, the proof fails
        if (!arb_is_positive(g_prime.val)) {
            strictly_monotonic = false;
            std::cout << "[FATAL] Monotonicity broken at slice [" << start_str << ", " << end_str << "]" << std::endl;
            break;
        }
    }

    if (strictly_monotonic) {
        std::cout << "\n========================================================" << std::endl;
        std::cout << "[RESULT] CERTIFIED: g'(rho) > 0 across the ENTIRE domain." << std::endl;
        std::cout << "Formal proof secured: g(rho) is strictly monotonic increasing." << std::endl;
        std::cout << "The F2 team is formally authorized to use boundary-value theorems." << std::endl;
        std::cout << "========================================================" << std::endl;
    }

    return 0;
}
