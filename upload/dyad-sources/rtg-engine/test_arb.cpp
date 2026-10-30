#include <iostream>
#include <flint/arb.h>

int main() {
    std::cout << "[ENG] RTG Interval Engine Initializing..." << std::endl;
    
    // Initialize an Arb interval
    arb_t pi_interval;
    arb_init(pi_interval);
    
    // Set it to Pi with 53 bits of precision
    arb_const_pi(pi_interval, 53);
    
    std::cout << "Strict Interval for Pi: ";
    arb_printn(pi_interval, 15, 0);
    std::cout << std::endl;
    
    // Clean up memory
    arb_clear(pi_interval);
    
    std::cout << "[STATUS] Toolchain Verified." << std::endl;
    return 0;
}
