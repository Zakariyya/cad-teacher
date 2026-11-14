#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

command -v gh >/dev/null
command -v git >/dev/null
login=$(gh api user --jq .login)
if [[ "$login" != "Zakariyya" ]]; then
  echo "当前 GitHub 账号不是预期的 Zakariyya，停止发布。" >&2
  exit 1
fi
python3 learning/lesson-01.py
if [[ ! -f .git/HEAD ]]; then
  git init -b main
fi
if [[ "$(git rev-parse --show-toplevel)" != "$(pwd -P)" ]]; then
  echo "Git 仓库根目录与项目目录不符，停止发布。" >&2
  exit 1
fi
if [[ -n "$(git remote)" ]]; then
  echo "已有 Git 远端，停止自动创建；请先核对已有仓库。" >&2
  exit 1
fi
if [[ "$(git branch --show-current)" != main ]]; then
  echo "当前分支不是 main，停止发布。" >&2
  exit 1
fi
git add -- .gitignore README.md requirements.txt publish-github.sh \
  learning/README.md learning/progress.md learning/resources.md \
  learning/lesson-01.md learning/lesson-01-review.md learning/lesson-01.py \
  learning/lesson-01-fbd.svg learning/lesson-01-answer-key.json
python3 - <<'PY'
import subprocess
allowed = {'.gitignore','README.md','requirements.txt','publish-github.sh',
 'learning/README.md','learning/progress.md','learning/resources.md',
 'learning/lesson-01.md','learning/lesson-01-review.md','learning/lesson-01.py',
 'learning/lesson-01-fbd.svg','learning/lesson-01-answer-key.json'}
staged = set(filter(None, subprocess.check_output(
 ['git','diff','--cached','--name-only','-z']).decode().split('\0')))
extra = staged - allowed
if extra:
 raise SystemExit('存在本次清单以外的暂存文件，停止提交：'+repr(sorted(extra)))
print('已审查提交清单：', *sorted(staged), sep='\n')
PY
git diff --cached --check
if ! git diff --cached --quiet; then
  git commit -m "初始化机器人学习项目，归档力学第一课与学习进度"
fi
gh repo create Zakariyya/cad-teacher --private \
  --description "机械工程与工业机器人循序渐进学习：课程、练习、计算验证和学习进度" \
  --source=. --remote=origin --push
local_sha=$(git rev-parse HEAD)
remote_sha=$(git ls-remote origin refs/heads/main | cut -f1)
if [[ "$local_sha" != "$remote_sha" ]]; then
  echo "远端 main 与本地提交不一致，发布尚未验证。" >&2
  exit 1
fi
echo "已验证提交：$local_sha"
gh repo view Zakariyya/cad-teacher --json url,isPrivate --jq '{url,isPrivate}'
