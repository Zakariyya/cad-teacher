#!/usr/bin/env bash
# Existing-repository publishing only. No creation, forced push or history rewrite.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if [[ "$(git rev-parse --show-toplevel)" != "$(pwd -P)" ]]; then
  echo 'Git 根目录不是当前教材目录，停止。' >&2
  exit 1
fi
if [[ "$(git branch --show-current)" != main ]]; then
  echo '当前分支不是 main，停止。' >&2
  exit 1
fi
case "$(git remote get-url origin)" in
  https://github.com/Zakariyya/cad-teacher.git|git@github.com:Zakariyya/cad-teacher.git) ;;
  *) echo 'origin 不是预期的 cad-teacher 仓库，停止。' >&2; exit 1 ;;
esac
git fetch origin
if ! git merge-base --is-ancestor origin/main HEAD; then
  echo '远端存在尚未整合的提交，请先同步并解决冲突。' >&2
  exit 1
fi
python3 tools/build_study_pack.py
python3 tools/check_project.py
git add -- .gitignore .gitattributes AGENTS.md README.md requirements.txt publish-github.sh \
  prompts curriculum learning resources templates tools docs
python3 - <<'PY'
import subprocess
from pathlib import PurePosixPath
allowed_files = {'.gitignore', '.gitattributes', 'AGENTS.md', 'README.md', 'requirements.txt', 'publish-github.sh'}
allowed_dirs = {'prompts', 'curriculum', 'learning', 'resources', 'templates', 'tools', 'docs'}
paths = filter(None, subprocess.check_output(['git', 'diff', '--cached', '--name-only', '-z']).decode().split('\0'))
for path in paths:
    if path not in allowed_files and PurePosixPath(path).parts[0] not in allowed_dirs:
        raise SystemExit('清单外暂存文件，停止：' + path)
PY
git diff --cached --check
git diff --cached --stat
if ! git diff --cached --quiet; then
  git commit -m "更新机器人教材内容、资源与学习进度"
fi
git push -u origin main
local_sha=$(git rev-parse HEAD)
remote_sha=$(git ls-remote origin refs/heads/main | cut -f1)
[[ "$local_sha" == "$remote_sha" ]] || { echo '远端提交不一致，未通过同步验证。' >&2; exit 1; }
echo "已同步：https://github.com/Zakariyya/cad-teacher/commit/$local_sha"
