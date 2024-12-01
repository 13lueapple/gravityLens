from sympy import symbols, Eq, solve

# Given values
D_L = 5.9698536e+25  # Distance to lens in meters
M = 1.0421940805998e+43
theta_E = 2.240130259064082151e-5  # Einstein radius in radians
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
c = 3.00e8  # Speed of light in m/s
# D_S = 3.15929259e+26
SUN_MASS = 1.989e+30
KM_TO_GPC = 3.240779e-23

# Define D_S as a symbol
D_S = symbols('D_S')

# Equation based on the lensing formula
D_LS = D_S - D_L
equation = Eq(theta_E**2, (4 * G * M / c**2) * (D_LS / (D_L * D_S)))

# Solve for D_S
M_value = solve(equation, D_S)
print(f"천체까지의 거리 : {M_value[0] * KM_TO_GPC :.2e} Gpc")
