"""Lesson 03: multi-load static equilibrium worked-example check.

Educational model only: a horizontal rigid cantilever, fixed at A, with
three vertical downward gravity loads. SI units; CCW support moment is positive.
"""
from math import isclose

G_M_S2 = 10.0
loads = [
    {"name": "bracket self-weight", "mass_kg": 0.8, "x_m": 0.30},
    {"name": "camera", "mass_kg": 1.5, "x_m": 0.50},
    {"name": "sensor", "mass_kg": 0.5, "x_m": 0.60},
]

for load in loads:
    load["weight_N"] = load["mass_kg"] * G_M_S2
    load["clockwise_moment_Nm"] = load["weight_N"] * load["x_m"]

total_downward_N = sum(load["weight_N"] for load in loads)
total_clockwise_Nm = sum(load["clockwise_moment_Nm"] for load in loads)

# Equilibrium: Ay balances all downward loads; MA balances all clockwise moments.
Ay_N = total_downward_N
MA_Nm = total_clockwise_Nm
x_combined_cg_m = total_clockwise_Nm / total_downward_N

residual_Fy_N = Ay_N - total_downward_N
residual_MA_Nm = MA_Nm - total_clockwise_Nm

assert isclose(total_downward_N, 28.0, abs_tol=1e-12)
assert isclose(total_clockwise_Nm, 12.9, abs_tol=1e-12)
assert isclose(x_combined_cg_m, 0.4607142857142857, abs_tol=1e-12)
assert isclose(residual_Fy_N, 0.0, abs_tol=1e-12)
assert isclose(residual_MA_Nm, 0.0, abs_tol=1e-12)

print("Loads:")
for load in loads:
    print(
        f"{load['name']}: W={load['weight_N']:.1f} N, "
        f"x={load['x_m']:.2f} m, "
        f"M_A={load['clockwise_moment_Nm']:.2f} N·m clockwise"
    )
print(f"Total downward force = {total_downward_N:.1f} N")
print(f"Fixed support reaction Ay = {Ay_N:.1f} N upward")
print(f"Fixed support reaction moment MA = {MA_Nm:.2f} N·m counterclockwise")
print(f"Equivalent combined CG x_G = {x_combined_cg_m:.4f} m from A")
print(f"Equilibrium residuals: ΣFy={residual_Fy_N:.1f} N, ΣM_A={residual_MA_Nm:.1f} N·m")
\n