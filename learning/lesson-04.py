"""Lesson 04: resolve an oblique force and check fixed-support equilibrium.

Educational model only: a horizontal rigid cantilever fixed at A.
A 100 N force acts at the free end, 53.1301 degrees below +x.
SI units; right/up positive; counterclockwise moments positive.
"""
from math import atan2, cos, degrees, isclose, sin

G_M_S2 = 10.0
L_M = 0.60
BEAM_MASS_KG = 1.0
FORCE_N = 100.0

# A 3-4-5 triangle: cos(theta)=3/5, sin(theta)=4/5.
theta_rad = atan2(4.0, 3.0)
theta_deg = degrees(theta_rad)
Fx_N = FORCE_N * cos(theta_rad)          # right, positive
Fy_N = -FORCE_N * sin(theta_rad)         # down, negative
beam_weight_N = BEAM_MASS_KG * G_M_S2
beam_cg_x_m = L_M / 2.0

# Fixed-support reactions make the total force and moment zero.
Ax_N = -Fx_N
Ay_N = beam_weight_N - Fy_N
# The horizontal component is collinear with the beam centreline and A.
horizontal_component_moment_Nm = 0.0
MA_Nm = -(L_M * Fy_N + beam_cg_x_m * (-beam_weight_N))

residual_Fx_N = Ax_N + Fx_N
residual_Fy_N = Ay_N + Fy_N - beam_weight_N
residual_MA_Nm = MA_Nm + L_M * Fy_N - beam_cg_x_m * beam_weight_N

assert isclose(theta_deg, 53.13010235415598, abs_tol=1e-10)
assert isclose(Fx_N, 60.0, abs_tol=1e-12)
assert isclose(Fy_N, -80.0, abs_tol=1e-12)
assert isclose(beam_weight_N, 10.0, abs_tol=1e-12)
assert isclose(Ax_N, -60.0, abs_tol=1e-12)
assert isclose(Ay_N, 90.0, abs_tol=1e-12)
assert isclose(MA_Nm, 51.0, abs_tol=1e-12)
assert isclose(horizontal_component_moment_Nm, 0.0, abs_tol=1e-12)
assert isclose(residual_Fx_N, 0.0, abs_tol=1e-12)
assert isclose(residual_Fy_N, 0.0, abs_tol=1e-12)
assert isclose(residual_MA_Nm, 0.0, abs_tol=1e-12)

print(f"Force angle = {theta_deg:.4f} degrees below +x")
print(f"Applied force = {FORCE_N:.1f} N down-right")
print(f"Fx = {Fx_N:.1f} N right; Fy = {abs(Fy_N):.1f} N down")
print(f"Beam self-weight = {beam_weight_N:.1f} N at x = {beam_cg_x_m:.2f} m")
print(f"Fixed support Ax = {Ax_N:.1f} N (left)")
print(f"Fixed support Ay = {Ay_N:.1f} N (up)")
print(f"Fixed support MA = {MA_Nm:.2f} N·m (counterclockwise)")
print("Horizontal force component moment about A = 0 N·m (line of action passes through A)")
print(f"Equilibrium residuals: Fx={residual_Fx_N:.1f} N, Fy={residual_Fy_N:.1f} N, MA={residual_MA_Nm:.1f} N·m")
