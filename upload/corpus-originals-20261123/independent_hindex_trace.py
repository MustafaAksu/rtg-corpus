import sympy as sp

# Initialize symbolic variables
h11, h12, h21, h22 = sp.symbols('h11 h12 h21 h22', real=True)
x1, x2 = sp.symbols('x1 x2', real=True)

# Define the canonical background metric B
B = sp.Matrix([[1, sp.Rational(-1, 2)], 
               [sp.Rational(-1, 2), 1]])
B_inv = B.inv()

# Define the covector-valued source block matrix H and input vector x
H = sp.Matrix([[h11, h12], 
               [h21, h22]])
x = sp.Matrix([x1, x2])

# 1. Compute input vector amplitude squared: ||x||_B^2 = x^T * B * x
input_amp_sq = (x.T * B * x)[0, 0]

# 2. Compute output covector mapping: S = H * x
S = H * x

# 3. Compute output amplitude squared using dual inverse-metric contraction
output_amp_sq = (S.T * B_inv * S)[0, 0]

# 4. Extract the core quadratic form matrix: output_amp_sq = x^T * (H^T * B_inv * H) * x
Core_Matrix = H.T * B_inv * H

# 5. Formulate the characteristic matrix for the generalized eigenvalue problem
# det(Core_Matrix - lambda * B) = 0  ==> det(B_inv * Core_Matrix - lambda * I) = 0
Combined_Matrix = B_inv * Core_Matrix

print("Highly Covariant Matrix Object (B_inv * H^T * B_inv * H):")
sp.pprint(sp.simplify(Combined_Matrix))

# Verify that if H = sigma * B, the characteristic roots collapse perfectly to sigma^2
sigma = sp.symbols('sigma', real=True)
H_test = sigma * B
Combined_Test = sp.simplify(B_inv * (H_test.T) * B_inv * H_test)
char_poly = Combined_Test.charpoly()
# Change line 41 to:
print(f"\nTest case roots for H = sigma * B: {char_poly.all_roots()}")