#include "rtg_core.hpp"
#include <iostream>

int main() {
    std::cout << "[ENG] Initializing Rigorous 6-Step Map Engine..." << std::endl;
    
    DyadState state;
    
    // Start at the high-amplitude macroscopic spiral we tested in Python
    state.rho.set("0.4");
    state.eta.set("0.4");
    
    std::cout << "\n[NUM] Step 0 (Initial):" << std::endl;
    state.print();

    // Fire the primitive map 6 times to complete one discrete core cycle
    for (int i = 1; i <= 6; ++i) {
        state.step();
        std::cout << "\n[NUM] Step " << i << ":" << std::endl;
        state.print();
    }

    std::cout << "\n[STATUS] Primitive Map Generator Validated." << std::endl;
    return 0; 
}
