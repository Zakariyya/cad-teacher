"""Build one UTF-8 upload document from the authoritative teaching files."""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'learning/chatgpt-study-pack.txt'
REPO = 'https://github.com/Zakariyya/cad-teacher/blob/main/'
SOURCES = [
    'prompts/project-instructions.md',
    'prompts/original-request.md',
    'prompts/resume-learning.md',
    'learning/progress.md',
    'curriculum/roadmap.md',
    'curriculum/lessons.json',
    'learning/resources.md',
    'docs/teaching-standard.md',
    'resources/skills.md',
    'resources/THIRD_PARTY_NOTICES.md',
    'resources/vendor/baratilab/LICENSE',
    'resources/vendor/baratilab/skills/mechanics-visuals/SKILL.md',
    'resources/vendor/baratilab/skills/mechanics-visuals/references/fbd_style.md',
    'resources/vendor/baratilab/skills/mechanics-visuals/scripts/mech_plots.py',
    'resources/vendor/baratilab/skills/worked-problem-generator/SKILL.md',
    'resources/vendor/baratilab/skills/worked-problem-generator/references/problem_template.md',
]


def lesson_sources(catalog):
    """Only explicitly published feedback/solutions belong in student uploads."""
    sources, ids = [], set()
    for lesson in catalog['lessons']:
        identifier = lesson['id']
        if not re.fullmatch(r'\d{2,}', identifier) or identifier in ids:
            raise ValueError(f'Invalid/duplicate lesson ID: {identifier}')
        ids.add(identifier)
        if type(lesson['feedback_published']) is not bool:
            raise ValueError('feedback_published must be a boolean')
        sources.append(lesson['lesson'])
        if lesson.get('example_script'):
            sources.append(lesson['example_script'])
        if lesson['feedback_published']:
            if not lesson.get('feedback'):
                raise ValueError(f'Published feedback missing: {identifier}')
            sources.append(lesson['feedback'])
            sources.extend(lesson[key] for key in ['solution_script', 'answer_key'] if lesson.get(key))
    if len(sources) != len(set(sources)):
        raise ValueError('Duplicate lesson source file')
    for path in sources:
        if not (ROOT / path).resolve().is_relative_to(ROOT):
            raise ValueError(f'Lesson source outside repository: {path}')
    return sources


def portable_links(text, source):
    def replace(match):
        label, target = match.groups()
        if '://' in target or target.startswith(('#', 'mailto:')):
            return match.group(0)
        path, separator, anchor = target.partition('#')
        resolved = (ROOT / source).parent.joinpath(path).resolve()
        try:
            relative = resolved.relative_to(ROOT)
        except ValueError:
            raise ValueError(f'Link outside repository: {source}: {target}')
        return f'[{label}]({REPO}{relative.as_posix()}{separator}{anchor})'
    return re.sub(r'\[([^\]]*)\]\(([^)]+)\)', replace, text)


def build():
    catalog = json.loads((ROOT / 'curriculum/lessons.json').read_text(encoding='utf-8'))
    sources = SOURCES[:7] + lesson_sources(catalog) + SOURCES[7:]
    contents = [(path, (ROOT / path).read_bytes()) for path in sources]
    fingerprint = hashlib.sha256()
    for path, raw in contents:
        fingerprint.update(path.encode() + b'\0' + raw + b'\0')
    lines = [
        '# cad-teacher 网页端学习包',
        '',
        '这是可上传或粘贴的静态 UTF-8 学习资料，不是已安装的 Skill 或工具。',
        '先读项目指令和进度，再进入一个知识单元。原始提示词是历史需求，不要求重上第一课。',
        '包中解析只来自明确标记已公开反馈的课；新课仍须等待学生回答后再揭示答案。',
        '本包附历史验证说明；只有本次真正执行的程序才能称作本次验证。',
        '缺少运行工具时明确未运行；不能写 GitHub 时输出待回写更新。',
        '图的链接供在线查看；离线时使用讲义中的对象、尺寸、方向和方程重画受力图。',
        '权威进度：https://github.com/Zakariyya/cad-teacher/blob/main/learning/progress.md',
        f'源文件集合 SHA-256：{fingerprint.hexdigest()}',
        '',
        '## 内嵌源文件与 SHA-256',
    ]
    for path, raw in contents:
        lines.append(f'- {path}: {hashlib.sha256(raw).hexdigest()}')
    for path, raw in contents:
        text = raw.decode('utf-8').rstrip()
        if path.endswith('.md'):
            text = portable_links(text, path)
        if path.endswith(('.py', '.json')):
            text = '````' + ('python' if path.endswith('.py') else 'json') + '\n' + text + '\n````'
        lines.extend(['', '---', '', f'## 源文件：{path}', '', text])
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the committed pack is stale.')
    args = parser.parse_args()
    expected = build()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding='utf-8') != expected:
            raise SystemExit('FAIL: 学习包缺失或过期，请运行 python3 tools/build_study_pack.py')
        print('PASS: 学习包与全部源文件一致')
    else:
        OUTPUT.write_text(expected, encoding='utf-8', newline='\n')
        print(f'Built {OUTPUT.relative_to(ROOT)} ({len(expected.encode())} bytes)')


if __name__ == '__main__':
    main()
