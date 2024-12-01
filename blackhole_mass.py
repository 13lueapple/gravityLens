from sympy import symbols, Eq, solve

# Given values
D_L = 5.8698536e+25  # Distance to lens in meters
theta_E = 2.365309760759550742e-5  # Einstein radius in radians
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
c = 3.00e8  # Speed of light in m/s
D_S = 3.15929259e+26
SUN_MASS = 1.989e+30

# Define D_S as a symbol
M = symbols('M')

# Equation based on the lensing formula
D_LS = D_S - D_L
equation = Eq(theta_E**2, (4 * G * M / c**2) * (D_LS / (D_L * D_S)))

# Solve for D_S
M_value = solve(equation, M)
print(f"렌즈의 질량 : {M_value[0] / SUN_MASS:.2e} M☉")
