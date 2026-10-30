// open18_arb_cert.cpp
// Independent Arb/C++ certification for RTG OPEN 18
// Formally verifies micro/macro branch first-footprint monotonicity via Adaptive Bisection.

#include "flint/arb.h"
#include <stdio.h>

void step_arb(arb_t r1, arb_t e1, arb_t dr1, arb_t de1, 
              arb_t d2r1, arb_t d2e1, arb_t d3r1, arb_t d3e1,
              const arb_t r, const arb_t e, const arb_t dr, const arb_t de,
              const arb_t d2r, const arb_t d2e, const arb_t d3r, const arb_t d3e, slong prec) {
    arb_t s, c, ex;
    arb_init(s); arb_init(c); arb_init(ex);
    
    arb_sin_cos(s, c, e, prec);
    arb_exp(ex, r, prec);
    
    arb_t t1, t2, t3;
    arb_init(t1); arb_init(t2); arb_init(t3);
    
    // r1 = r - s
    arb_sub(r1, r, s, prec);
    
    // e1 = e + ex - 1 - s
    arb_sub_ui(t1, ex, 1, prec);
    arb_add(e1, e, t1, prec);
    arb_sub(e1, e1, s, prec);
    
    // dr1 = dr - c * de
    arb_mul(t1, c, de, prec);
    arb_sub(dr1, dr, t1, prec);
    
    // de1 = de + ex * dr - c * de
    arb_mul(t2, ex, dr, prec);
    arb_add(t3, de, t2, prec);
    arb_sub(de1, t3, t1, prec);
    
    // d2r1 = d2r + s * de**2 - c * d2e
    arb_t de2; arb_init(de2);
    arb_mul(de2, de, de, prec);
    arb_mul(t2, s, de2, prec);
    arb_mul(t3, c, d2e, prec);
    arb_add(d2r1, d2r, t2, prec);
    arb_sub(d2r1, d2r1, t3, prec);
    
    // d2e1 = d2e + ex * dr**2 + ex * d2r + s * de**2 - c * d2e
    arb_t dr2; arb_init(dr2);
    arb_mul(dr2, dr, dr, prec);
    
    arb_t term1, term2; arb_init(term1); arb_init(term2);
    arb_mul(term1, ex, dr2, prec);
    arb_mul(term2, ex, d2r, prec);
    
    arb_add(d2e1, d2e, term1, prec);
    arb_add(d2e1, d2e1, term2, prec);
    arb_add(d2e1, d2e1, t2, prec); 
    arb_sub(d2e1, d2e1, t3, prec); 
    
    // minus_d3_sin = c * de**3 + 3 * s * de * d2e - c * d3e
    arb_t minus_d3_sin, de3;
    arb_init(minus_d3_sin); arb_init(de3);
    
    arb_mul(de3, de2, de, prec);
    arb_mul(t1, c, de3, prec); 
    
    arb_mul(t2, s, de, prec);
    arb_mul(t2, t2, d2e, prec);
    arb_mul_ui(t2, t2, 3, prec); 
    
    arb_mul(t3, c, d3e, prec); 
    
    arb_add(minus_d3_sin, t1, t2, prec);
    arb_sub(minus_d3_sin, minus_d3_sin, t3, prec);
    
    // d3_exp = ex * (dr**3 + 3 * dr * d2r + d3r)
    arb_t d3_exp, dr3;
    arb_init(d3_exp); arb_init(dr3);
    
    arb_mul(dr3, dr2, dr, prec);
    arb_mul(t1, dr, d2r, prec);
    arb_mul_ui(t1, t1, 3, prec);
    
    arb_add(t2, dr3, t1, prec);
    arb_add(t2, t2, d3r, prec);
    arb_mul(d3_exp, ex, t2, prec);
    
    // d3r1 = d3r + minus_d3_sin
    arb_add(d3r1, d3r, minus_d3_sin, prec);
    
    // d3e1 = d3e + d3_exp + minus_d3_sin
    arb_add(d3e1, d3e, d3_exp, prec);
    arb_add(d3e1, d3e1, minus_d3_sin, prec);
    
    arb_clear(s); arb_clear(c); arb_clear(ex);
    arb_clear(t1); arb_clear(t2); arb_clear(t3);
    arb_clear(de2); arb_clear(dr2); arb_clear(term1); arb_clear(term2);
    arb_clear(minus_d3_sin); arb_clear(de3);
    arb_clear(d3_exp); arb_clear(dr3);
}

void evaluate(arb_t r, arb_t e, arb_t dr, arb_t de, arb_t d2r, arb_t d2e, arb_t d3r, arb_t d3e, arb_t q_iv, int n, slong prec) {
    arb_zero(r);
    arb_set(e, q_iv);
    arb_zero(dr);
    arb_one(de);
    arb_zero(d2r);
    arb_zero(d2e);
    arb_zero(d3r);
    arb_zero(d3e);
    
    arb_t r1, e1, dr1, de1, d2r1, d2e1, d3r1, d3e1;
    arb_init(r1); arb_init(e1); arb_init(dr1); arb_init(de1);
    arb_init(d2r1); arb_init(d2e1); arb_init(d3r1); arb_init(d3e1);
    
    for (int i = 0; i < n; i++) {
        step_arb(r1, e1, dr1, de1, d2r1, d2e1, d3r1, d3e1, r, e, dr, de, d2r, d2e, d3r, d3e, prec);
        arb_swap(r, r1); arb_swap(e, e1);
        arb_swap(dr, dr1); arb_swap(de, de1);
        arb_swap(d2r, d2r1); arb_swap(d2e, d2e1);
        arb_swap(d3r, d3r1); arb_swap(d3e, d3e1);
    }
    
    arb_clear(r1); arb_clear(e1); arb_clear(dr1); arb_clear(de1);
    arb_clear(d2r1); arb_clear(d2e1); arb_clear(d3r1); arb_clear(d3e1);
}

void d2Q_calc(arb_t res, arb_t r, arb_t e, arb_t dr, arb_t de, arb_t d2r, arb_t d2e, slong prec) {
    arb_t t1, t2, t3;
    arb_init(t1); arb_init(t2); arb_init(t3);
    
    arb_mul(t1, dr, dr, prec);
    arb_mul(t2, dr, de, prec);
    arb_mul(t3, de, de, prec);
    
    arb_sub(t1, t1, t2, prec);
    arb_add(t1, t1, t3, prec);
    arb_mul_ui(t1, t1, 2, prec);
    
    arb_mul_ui(t2, r, 2, prec);
    arb_sub(t2, t2, e, prec);
    arb_mul(t2, t2, d2r, prec);
    
    arb_mul_ui(t3, e, 2, prec);
    arb_sub(t3, t3, r, prec);
    arb_mul(t3, t3, d2e, prec);
    
    arb_add(res, t1, t2, prec);
    arb_add(res, res, t3, prec);
    
    arb_clear(t1); arb_clear(t2); arb_clear(t3);
}

void d2Ntheta_calc(arb_t res, arb_t r, arb_t e, arb_t dr, arb_t de, arb_t d2r, arb_t d2e, arb_t d3r, arb_t d3e, slong prec) {
    arb_t t1, t2, t3, t4;
    arb_init(t1); arb_init(t2); arb_init(t3); arb_init(t4);
    
    arb_mul(t1, dr, d2e, prec);
    arb_mul(t2, r, d3e, prec);
    arb_mul(t3, de, d2r, prec);
    arb_mul(t4, e, d3r, prec);
    
    arb_add(res, t1, t2, prec);
    arb_sub(res, res, t3, prec);
    arb_sub(res, res, t4, prec);
    
    arb_clear(t1); arb_clear(t2); arb_clear(t3); arb_clear(t4);
}

void dQ_calc(arb_t res, arb_t r, arb_t e, arb_t dr, arb_t de, slong prec) {
    arb_t t1, t2;
    arb_init(t1); arb_init(t2);
    
    arb_mul_ui(t1, r, 2, prec);
    arb_sub(t1, t1, e, prec);
    arb_mul(t1, t1, dr, prec);
    
    arb_mul_ui(t2, e, 2, prec);
    arb_sub(t2, t2, r, prec);
    arb_mul(t2, t2, de, prec);
    
    arb_add(res, t1, t2, prec);
    
    arb_clear(t1); arb_clear(t2);
}

void Ntheta_calc(arb_t res, arb_t r, arb_t e, arb_t dr, arb_t de, slong prec) {
    arb_t t1, t2;
    arb_init(t1); arb_init(t2);
    
    arb_mul(t1, r, de, prec);
    arb_mul(t2, e, dr, prec);
    arb_sub(res, t1, t2, prec);
    
    arb_clear(t1); arb_clear(t2);
}

void set_interval(arb_t res, arb_t a, arb_t b, slong prec) {
    arb_t mid, rad;
    arb_init(mid); arb_init(rad);
    
    arb_add(mid, a, b, prec);
    arb_mul_2exp_si(mid, mid, -1);
    
    arb_sub(rad, b, a, prec);
    arb_mul_2exp_si(rad, rad, -1);
    
    arb_set(res, mid);
    mag_t mrad; mag_init(mrad);
    arb_get_mag(mrad, rad);
    arb_add_error_mag(res, mrad);
    
    arb_clear(mid); arb_clear(rad); mag_clear(mrad);
}

// Single-box logic
int check_box(arb_t a, arb_t b, int n_step, slong prec) {
    arb_t q_iv; arb_init(q_iv);
    set_interval(q_iv, a, b, prec);
    
    arb_t r, e, dr, de, d2r, d2e, d3r, d3e, res_dQ, res_N;
    arb_init(r); arb_init(e); arb_init(dr); arb_init(de);
    arb_init(d2r); arb_init(d2e); arb_init(d3r); arb_init(d3e);
    arb_init(res_dQ); arb_init(res_N);
    
    evaluate(r, e, dr, de, d2r, d2e, d3r, d3e, q_iv, n_step, prec);
    dQ_calc(res_dQ, r, e, dr, de, prec);
    Ntheta_calc(res_N, r, e, dr, de, prec);
    
    int ok = arb_is_positive(res_dQ) && arb_is_negative(res_N);
    
    arb_clear(r); arb_clear(e); arb_clear(dr); arb_clear(de);
    arb_clear(d2r); arb_clear(d2e); arb_clear(d3r); arb_clear(d3e);
    arb_clear(res_dQ); arb_clear(res_N);
    arb_clear(q_iv);
    
    return ok;
}

// Bisection logic: recursive zoom-in for intervals that fail standard overestimation widths
int adaptive_sweep_rec(arb_t a, arb_t b, int n_step, int depth, slong prec, int &count, int &fail_flag) {
    if (fail_flag) return 0;
    
    if (check_box(a, b, n_step, prec)) {
        count++;
        return 1;
    }
    
    // Safety break at depth 50 ensures bounding widths down to ~10^-15
    if (depth > 50) {
        printf("\n  -> [FAIL] Arb bisection reached max depth at interval bounds: [");
        arb_printn(a, 15, 0); printf(", "); arb_printn(b, 15, 0); printf("]\n");
        fail_flag = 1;
        return 0;
    }
    
    arb_t mid; arb_init(mid);
    arb_add(mid, a, b, prec);
    arb_mul_2exp_si(mid, mid, -1);
    
    int ok = adaptive_sweep_rec(a, mid, n_step, depth + 1, prec, count, fail_flag);
    if (ok) {
        ok = adaptive_sweep_rec(mid, b, n_step, depth + 1, prec, count, fail_flag);
    }
    
    arb_clear(mid);
    return ok;
}

int sweep_macro_adaptive(int n_step, const char* q_lo_str, const char* q_hi_str, slong prec) {
    arb_t q_lo, q_hi;
    arb_init(q_lo); arb_init(q_hi);
    
    arb_set_str(q_lo, q_lo_str, prec);
    arb_set_str(q_hi, q_hi_str, prec);
    
    int count = 0;
    int fail_flag = 0;
    int ok = adaptive_sweep_rec(q_lo, q_hi, n_step, 0, prec, count, fail_flag);
    
    if (ok) {
        printf("[SUCCESS] Certified strictly using %d adaptively refined boxes.\n", count);
    } else {
        printf("[FAIL] Adaptive sweep could not certify bounding signs.\n");
    }
    
    arb_clear(q_lo); arb_clear(q_hi);
    return ok;
}

int certify_micro(slong prec) {
    arb_t q_iv, a, b;
    arb_init(q_iv); arb_init(a); arb_init(b);
    
    arb_set_ui(a, 0);
    arb_set_str(b, "0.001", prec);
    
    set_interval(q_iv, a, b, prec);
    
    arb_t r, e, dr, de, d2r, d2e, d3r, d3e;
    arb_init(r); arb_init(e); arb_init(dr); arb_init(de);
    arb_init(d2r); arb_init(d2e); arb_init(d3r); arb_init(d3e);
    
    evaluate(r, e, dr, de, d2r, d2e, d3r, d3e, q_iv, 3, prec);
    
    arb_t res_d2Q, res_d2N;
    arb_init(res_d2Q); arb_init(res_d2N);
    
    d2Q_calc(res_d2Q, r, e, dr, de, d2r, d2e, prec);
    d2Ntheta_calc(res_d2N, r, e, dr, de, d2r, d2e, d3r, d3e, prec);
    
    printf("--- Micro Certificate: q in (0, 0.001] ---\n");
    printf("d^2Q_3/dq^2 interval:   "); arb_printn(res_d2Q, 15, 0); printf("\n");
    printf("d^2N_Th,3/dq^2 int.:    "); arb_printn(res_d2N, 15, 0); printf("\n");
    
    int ok = arb_is_positive(res_d2Q) && arb_is_negative(res_d2N);
    
    arb_clear(q_iv); arb_clear(a); arb_clear(b);
    arb_clear(r); arb_clear(e); arb_clear(dr); arb_clear(de);
    arb_clear(d2r); arb_clear(d2e); arb_clear(d3r); arb_clear(d3e);
    arb_clear(res_d2Q); arb_clear(res_d2N);
    
    return ok;
}

int main() {
    slong prec = 400; // ~120 decimal digits matching IA spec

    printf("========================================================================\n");
    printf("OPEN 18 Arb/C++ Independent Certification (Adaptive Bisection)\n");
    printf("========================================================================\n\n");

    int ok1 = certify_micro(prec);
    if (ok1) printf("[SUCCESS] Micro-strip bounds strictly verified via Arb MVT.\n\n");
    else printf("[FAIL] Micro-strip bounds failed.\n\n");
    
    printf("--- Macro Sweeps (Adaptive Bounds) ---\n");
    printf("Gamma_3 macro sweep (n=3): ");
    fflush(stdout);
    int ok2 = sweep_macro_adaptive(3, "0.001", "1.26021320256", prec);
    
    printf("Gamma_4 macro sweep (n=4): ");
    fflush(stdout);
    int ok3 = sweep_macro_adaptive(4, "1.26021520256", "2.0", prec);
    
    if (ok1 && ok2 && ok3) {
        printf("\n[THM-READY] All interval phase pieces natively closed in FLINT/Arb!\n");
    }
    
    return 0;
}
