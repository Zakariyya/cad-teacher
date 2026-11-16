"""Lesson 02 teaching example: uniform horizontal bracket self-weight.

All inputs use SI units: kg, m, m/s^2. Outputs: N, N*m.
This script contains ONLY the published example, not exercise answers.
Ideal static rigid cantilever; no CAD, FEA, or physical verification.
"""

import json
from math import isclose


def bracket_example(bracket_mass_kg, length_m, camera_mass_kg, camera_x_m, g_m_s2=10.0):
    """Return the uniform-bracket center of mass and fixed support reactions."""
    if bracket_mass_kg < 0 or camera_mass_kg < 0 or length_m <= 0:
        raise ValueError('Masses must be nonnegative and length must be positive')
    if not 0 <= camera_x_m <= length_m or g_m_s2 <= 0:
        raise ValueError('Camera must lie on the bracket and g must be positive')

    bracket_cg_x_m = length_m / 2
    bracket_weight_N = bracket_mass_kg * g_m_s2
    camera_weight_N = camera_mass_kg * g_m_s2
    support_Ry_N = bracket_weight_N + camera_weight_N
    support_MA_Nm = bracket_weight_N * bracket_cg_x_m + camera_weight_N * camera_x_m
    # Positive force: upward; positive moment about A: counterclockwise.
    residual_Fy_N = support_Ry_N - bracket_weight_N - camera_weight_N
    residual_MA_Nm = (support_MA_Nm - bracket_weight_N * bracket_cg_x_m
                      - camera_weight_N * camera_x_m)
    assert isclose(residual_Fy_N, 0, abs_tol=1e-12)
    assert isclose(residual_MA_Nm, 0, abs_tol=1e-12)
    return {
        'bracket_cg_x_m': bracket_cg_x_m,
        'bracket_weight_N': bracket_weight_N,
        'camera_weight_N': camera_weight_N,
        'support_Ry_up_N': support_Ry_N,
        'support_MA_ccw_Nm': support_MA_Nm,
        'residual_Fy_N': residual_Fy_N,
        'residual_MA_Nm': residual_MA_Nm,
    }


def independent_distributed_moment_Nm(mass_kg, length_m, g_m_s2=10.0, slices=1000):
    """Midpoint integration of uniform self-weight as independent check."""
    if slices < 1 or length_m <= 0 or mass_kg < 0 or g_m_s2 <= 0:
        raise ValueError('Invalid distributed-load inputs')
    piece_weight_N = mass_kg * g_m_s2 / slices
    return sum(piece_weight_N * (i + 0.5) * length_m / slices
               for i in range(slices))


if __name__ == '__main__':
    demo = bracket_example(0.6, 0.30, 2.0, 0.30)
    expected = {
        'bracket_cg_x_m': 0.15,
        'bracket_weight_N': 6.0,
        'camera_weight_N': 20.0,
        'support_Ry_up_N': 26.0,
        'support_MA_ccw_Nm': 6.9,
    }
    for key, value in expected.items():
        assert isclose(demo[key], value, abs_tol=1e-12), (key, demo[key])
    integral = independent_distributed_moment_Nm(0.6, 0.30)
    assert isclose(integral, 0.9, abs_tol=1e-12), integral
    # With massless bracket, recover the lesson-01 external load result.
    no_self_weight = bracket_example(0, 0.30, 2.0, 0.30)
    assert isclose(no_self_weight['support_MA_ccw_Nm'], 6.0, abs_tol=1e-12)
    # With no camera, only the bracket's weight remains.
    no_camera = bracket_example(0.6, 0.30, 0, 0.30)
    assert isclose(no_camera['support_MA_ccw_Nm'], integral, abs_tol=1e-12)
    print(json.dumps({'example': demo,
                      'self_weight_moment_midpoint_Nm': integral,
                      'checks': 'PASS: equilibrium, midpoint integral, zero-mass limits'},
                     ensure_ascii=False, indent=2))
    print('Units: kg*m/s^2 = N; N*m = moment. No Pint-based unit checking.')
