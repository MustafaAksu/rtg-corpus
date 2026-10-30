#pragma once
#include <iostream>
#include <flint/arb.h>

// Standard precision for the RTG Proof Engine (256 bits = ~77 decimal places)
const slong RTG_PREC = 256;

class ArbReal {
public:
    arb_t val;

    // Constructor: Automatically initializes the C-struct
    ArbReal() {
        arb_init(val);
    }

    // Destructor: Automatically frees the memory when variable goes out of scope
    ~ArbReal() {
        arb_clear(val);
    }

    // Disable copy constructor for now to strictly prevent accidental double-frees
    ArbReal(const ArbReal&) = delete;
    ArbReal& operator=(const ArbReal&) = delete;

    // Helper: Set from string
    void set(const char* str) {
        arb_set_str(val, str, RTG_PREC);
    }

    // Helper: Print the bounded interval
    void print(int decimals = 10) const {
        arb_printn(val, decimals, 0);
    }
};

// The Dyad Phase Space Vector
struct DyadState {
    ArbReal rho;
    ArbReal eta;

    void print(int decimals = 15) const {
        std::cout << "  rho: "; rho.print(decimals); std::cout << std::endl;
        std::cout << "  eta: "; eta.print(decimals); std::cout << std::endl;
    }

    // OPEN 16: The Rigorous Primitive Map
    void step() {
        // 1. Compute rigorous transcendentals
        ArbReal sin_e;
        arb_sin(sin_e.val, eta.val, RTG_PREC);

        ArbReal exp_r;
        arb_exp(exp_r.val, rho.val, RTG_PREC);

        // 2. rho_next = rho - sin(eta)
        ArbReal rho_next;
        arb_sub(rho_next.val, rho.val, sin_e.val, RTG_PREC);

        // 3. eta_next = eta + exp(rho) - 1 - sin(eta)
        ArbReal eta_next;
        arb_add(eta_next.val, eta.val, exp_r.val, RTG_PREC);
        arb_sub_ui(eta_next.val, eta_next.val, 1, RTG_PREC); // Subtract exact unsigned int 1
        arb_sub(eta_next.val, eta_next.val, sin_e.val, RTG_PREC);

        // 4. Overwrite current state with the new rigorous bounds
        arb_set(rho.val, rho_next.val);
        arb_set(eta.val, eta_next.val);
    }

// OPEN 17: The Poincaré Jet Engine
    // Advances the state by N steps and returns true if the bounds are still tight
    bool advance(int N, double max_error_tolerance = 1e-5) {
        for (int i = 0; i < N; ++i) {
            step();
            
            // Extract the current uncertainty radius of rho
            ArbReal rad_rho;
            arb_get_rad_arb(rad_rho.val, rho.val);
            
            // Convert the interval radius to a standard double for checking
            double error_bound = arf_get_d(arb_midref(rad_rho.val), ARF_RND_UP);
            
            // If our mathematical uncertainty exceeds the tolerance, the proof fails
            if (error_bound > max_error_tolerance) {
                std::cout << "[WARN] Precision collapsed at step " << (i + 1) << std::endl;
                std::cout << "  Error Bound: " << error_bound << std::endl;
                return false; 
            }
        }
        return true;
    }
};
