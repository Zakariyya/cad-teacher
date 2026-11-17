"""Check teaching links, upstream snapshots, portable pack and lesson arithmetic."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from build_study_pack import lesson_sources

ROOT = Path(__file__).resolve().parents[1]


def main():
    checked = 0
    documents = [ROOT / 'README.md', ROOT / 'AGENTS.md']
    for folder in ['prompts', 'curriculum', 'learning', 'resources', 'templates', 'docs']:
        documents.extend(p for p in (ROOT / folder).glob('*.md'))
    for path in documents:
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith(('#', 'mailto:')):
                continue
            resolved = (path.parent / target.split('#')[0]).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                raise SystemExit(f'FAIL: broken/local-only link: {path}: {target}')
            checked += 1
    catalog = json.loads((ROOT / 'curriculum/lessons.json').read_text(encoding='utf-8'))
    registered = {entry['lesson'] for entry in catalog['lessons']}
    actual_lessons = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'learning').glob('lesson-*.md')
                      if re.fullmatch(r'lesson-\d+\.md', p.name)}
    if registered != actual_lessons:
        raise SystemExit('FAIL: 讲义与 curriculum/lessons.json 登记不一致')
    for path in lesson_sources(catalog):
        if not (ROOT / path).is_file():
            raise SystemExit(f'FAIL: missing registered teaching source: {path}')
    data = json.loads((ROOT / 'resources/skill-sources.json').read_text(encoding='utf-8'))
    for repo in data['repositories']:
        if not re.fullmatch('[0-9a-f]{40}', repo['commit']):
            raise SystemExit('FAIL: invalid upstream commit')
        for skill in repo['skills']:
            expected = f"https://github.com/{repo['repository']}/blob/{repo['commit']}/{skill['path']}"
            if skill['url'] != expected:
                raise SystemExit(f'FAIL: unpinned skill URL: {skill["name"]}')
    for snapshot in data['snapshots']:
        raw = (ROOT / snapshot['path']).read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if blob != snapshot['git_blob_sha']:
            raise SystemExit(f'FAIL: upstream snapshot changed: {snapshot["path"]}')
    subprocess.run([sys.executable, 'learning/lesson-01.py'], cwd=ROOT, check=True)
    key = json.loads((ROOT / 'learning/lesson-01-answer-key.json').read_text(encoding='utf-8'))
    for name, expected in [('basic', (10, 2)), ('application', (20, 5)), ('application_longer', (20, 10))]:
        actual = key[name]
        if (actual['Ry_N'], actual['MA_Nm']) != expected:
            raise SystemExit(f'FAIL: lesson result {name}')
        if any(abs(value) > 1e-12 for value in actual['residuals_Fx_N_Fy_N_MA_Nm']):
            raise SystemExit(f'FAIL: equilibrium residual {name}')
    lesson_two = next(entry for entry in catalog['lessons'] if entry['id'] == '02')
    if not lesson_two['feedback_published'] or not lesson_two.get('feedback') or not lesson_two.get('answer_key'):
        raise SystemExit('FAIL: 第二课作答反馈与答案记录尚未登记')
    key_two = json.loads((ROOT / lesson_two['answer_key']).read_text(encoding='utf-8'))
    submitted = key_two['application_camera_submitted_position']
    if (submitted['camera_weight_N'], submitted['camera_moment_Nm'],
            submitted['support_vertical_reaction_N'], submitted['support_reaction_moment_Nm']) != (15, 1.5, 21, 2.7):
        raise SystemExit('FAIL: 第二课工程应用结果')
    if any(abs(value) > 1e-12 for value in submitted['equilibrium_residuals'].values()):
        raise SystemExit('FAIL: 第二课平衡残差')
    subprocess.run([sys.executable, 'learning/lesson-02.py'], cwd=ROOT, check=True)
    ET.parse(ROOT / 'learning/lesson-01-fbd.svg')
    ET.parse(ROOT / 'learning/lesson-02-fbd.svg')
    subprocess.run([sys.executable, 'tools/build_study_pack.py', '--check'], cwd=ROOT, check=True)
    print(f'PASS: {checked} local links; {sum(len(r["skills"]) for r in data["repositories"])} pinned Skill URLs; '
          f'{len(data["snapshots"])} exact upstream snapshots; lessons 01/02 arithmetic and lesson 03 example; SVG; current upload pack')
    print('Not checked: live ChatGPT upload, CAD geometry, FEA, hardware.')


if __name__ == '__main__':
    main()
\n