"""Static rigid bracket; SI input only. Python standard-library fallback.
Sources: mechanics-visuals/references/fbd_style.md and
worked-problem-generator/references/problem_template.md.
No pint available: units checked explicitly, not automatically.
No beam self-weight, acceleration, elasticity, FEA or physical testing.
"""
from pathlib import Path
import json
OUT = Path(__file__).resolve().parent

def solve(force_N, length_m):
    ry_N = force_N
    ma_Nm = force_N * length_m
    residuals = [0.0, ry_N - force_N, ma_Nm - force_N * length_m]
    assert all(abs(v) < 1e-12 for v in residuals)
    # Cross-product component: rx*Fy - ry*Fx (N*m).
    cross_z_Nm = length_m * (-force_N) - 0 * 0
    assert abs(ma_Nm + cross_z_Nm) < 1e-12
    return dict(Rx_N=0, Ry_N=ry_N, MA_Nm=ma_Nm,
                residuals_Fx_N_Fy_N_MA_Nm=residuals)

demo = solve(20, .30)
print('Demo:', json.dumps(demo))
key = {'basic': solve(10,.20), 'application': solve(2*10,.25),
       'application_longer': solve(2*10,.50)}
assert key['application_longer']['MA_Nm'] == 2 * key['application']['MA_Nm']
(OUT/'lesson-01-answer-key.json').write_text(json.dumps(key,indent=2)+'\n')
print('All exercises computed; force and moment residuals are zero.')
print('Unit check: kg*m/s^2 = N; N*m = moment. No automatic unit checker.')
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="440" viewBox="0 0 1000 440">
<defs><marker id="red" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6" fill="#c0392b"/></marker><marker id="blue" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6" fill="#1f4e79"/></marker></defs>
<rect width="1000" height="440" fill="white"/>
<g font-family="sans-serif" font-size="22" fill="#2c3e50">
<text x="500" y="40" text-anchor="middle">水平支架的受力图（已移除墙体）</text>
<rect x="270" y="180" width="450" height="30" fill="#d9dde3" stroke="#2c3e50" stroke-width="2"/>
<circle cx="270" cy="195" r="4"/><text x="275" y="240">A</text>
<g fill="none" stroke="#c0392b" stroke-width="3"><path d="M720 195 V310" marker-end="url(#red)"/></g>
<text x="740" y="285" fill="#c0392b">W = 20 N</text>
<g fill="none" stroke="#1f4e79" stroke-width="3"><path d="M270 195 V80" marker-end="url(#blue)"/>
<path d="M305 140 A65 65 0 0 0 220 240" marker-end="url(#blue)"/></g>
<text x="285" y="100" fill="#1f4e79">Ay = 20 N</text>
<text x="35" y="135" fill="#1f4e79">MA = 6 N·m</text>
<text x="35" y="165" fill="#1f4e79">逆时针</text>
<text x="390" y="165" fill="#1f4e79">Ax = 0 N</text>
<path d="M270 330 V350 M270 340 H720 M720 330 V350" fill="none" stroke="#888"/>
<text x="495" y="375" text-anchor="middle">垂直力臂 d = 0.30 m</text>
<path d="M75 350 V290 M75 350 H135" fill="none" stroke="#2c3e50" stroke-width="2"/>
<text x="65" y="280">+y ↑</text><text x="140" y="360">+x →</text>
<text x="500" y="420" text-anchor="middle" font-size="18">静止、平面刚体、固定支撑、忽略支架自重；逆时针力矩为正</text>
</g></svg>'''
(OUT/'lesson-01-fbd.svg').write_text(svg)
print('SVG saved; this standard-library script does not render PNG. Not FEA.')
