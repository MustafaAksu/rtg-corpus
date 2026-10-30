#include "rtg_core.hpp"
#include <iostream>

int main() {
    std::cout << "[ENG] Initializing Poincaré Jet Engine..." << std::endl;
    
    DyadState state;
    state.rho.set("0.4");
    state.eta.set("0.4");
    
    std::cout << "\n[NUM] Step 0 (Initial):" << std::endl;
    state.print();

    // We want to simulate 600 steps (100 hexagonal orbits)
    int total_steps = 600;
    int batch_size = 60; // Print every 10 orbits
    
    std::cout << "\n[ENG] Firing Jet Engine (Target: " << total_steps << " steps)..." << std::endl;
    
    for (int i = 0; i < total_steps; i += batch_size) {
        bool stable = state.advance(batch_size, 1e-5);
        
        std::cout << "\n[NUM] Jet Checkpoint at Step " << (i + batch_size) << ":" << std::endl;
        state.print();
        
        if (!stable) {
            std::cout << "\n[FATAL] Proof engine stalled due to Lyapunov expansion." << std::endl;
            break;
        }
    }

    std::cout << "\n[STATUS] Jet Engine Execution Complete." << std::endl;
    return 0; 
}
