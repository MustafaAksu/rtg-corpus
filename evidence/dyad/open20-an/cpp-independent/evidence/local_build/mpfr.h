/* Local test-only public-ABI declarations. Not a project header.
   Types/signatures checked against GNU MPFR's public mpfr.h; runtime 4.2.2.
   Production builds must use the system libmpfr-dev header. */
#pragma once
#include <gmp.h>
#include <stddef.h>
#if __GMP_MP_SIZE_T_INT
typedef int mpfr_prec_t; typedef int mpfr_exp_t;
#else
typedef long mpfr_prec_t; typedef long mpfr_exp_t;
#endif
typedef int mpfr_sign_t;
typedef enum {MPFR_RNDN=0,MPFR_RNDZ,MPFR_RNDU,MPFR_RNDD,MPFR_RNDA,MPFR_RNDF,MPFR_RNDNA=-1} mpfr_rnd_t;
typedef struct {mpfr_prec_t _mpfr_prec;mpfr_sign_t _mpfr_sign;mpfr_exp_t _mpfr_exp;mp_limb_t *_mpfr_d;} __mpfr_struct;
typedef __mpfr_struct mpfr_t[1];
typedef __mpfr_struct *mpfr_ptr; typedef const __mpfr_struct *mpfr_srcptr;
extern "C" {
const char *mpfr_get_version(void);
void mpfr_init2(mpfr_ptr,mpfr_prec_t); void mpfr_clear(mpfr_ptr); void mpfr_swap(mpfr_ptr,mpfr_ptr);
int mpfr_set(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_set_si(mpfr_ptr,long,mpfr_rnd_t); int mpfr_set_str(mpfr_ptr,const char*,int,mpfr_rnd_t);
int mpfr_add(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_sub(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_mul(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_div(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_div_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t);
int mpfr_neg(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_abs(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_cmp(mpfr_srcptr,mpfr_srcptr); int mpfr_cmp_si(mpfr_srcptr,long);
int mpfr_number_p(mpfr_srcptr); int mpfr_zero_p(mpfr_srcptr);
int mpfr_exp(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_log(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_sqrt(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_sin(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_cos(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_sinh(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_cosh(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_atan(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_const_pi(mpfr_ptr,mpfr_rnd_t);
char *mpfr_get_str(char*,mpfr_exp_t*,int,size_t,mpfr_srcptr,mpfr_rnd_t); void mpfr_free_str(char*);
double mpfr_get_d(mpfr_srcptr,mpfr_rnd_t); void mpfr_free_cache(void);
}
