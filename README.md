# cad-teacher · 机械工程与工业机器人学习教材

为具有约 7 年 Java 后端经验的学习者，从机械、电路与动力学基础逐步走向机械设计、CAD、嵌入式、控制与 ROS 2 集成。

**这是一份持续编写的教材。第一课已完成讲解与反馈；第二课「支架自重与重心」已完成；第三课「多载荷平衡」讲义、示例和练习已发布，等待作答；其余课程仍是培养路线。**

## 开始阅读

| 你要做什么 | 入口 |
| --- | --- |
| 继续上次学习 | [当前进度](learning/progress.md) |
| 在 GPT 网页端使用 | [使用指南](docs/chatgpt-web.md) · [单文件上传包](learning/chatgpt-study-pack.txt) |
| 查看最初要求 | [原始提示词，保留原文](prompts/original-request.md) |
| 设置网页端导师 | [项目教学指令](prompts/project-instructions.md) · [恢复学习提示词](prompts/resume-learning.md) |
| 查看完整培养路线 | [课程路线与能力检查](curriculum/roadmap.md) |
| 阅读第一课 | [讲义](learning/lesson-01.md) · [作答反馈](learning/lesson-01-review.md) |
| 阅读第二课：支架自重与重心 | [讲义](learning/lesson-02.md) · [作答反馈](learning/lesson-02-review.md) · [示例代码](learning/lesson-02.py) · [验证记录](learning/lesson-02-verification.md) |
| 学习第三课：多载荷平衡 | [讲义](learning/lesson-03.md) · [受力图](learning/lesson-03-fbd.svg) · [示例代码](learning/lesson-03.py) |
| 找 Skill GitHub 地址 | [41 个 Skill 来源索引](resources/skills.md) · [版本登记表](resources/skill-sources.json) |
| 维护与编写教材 | [目录职责](docs/project-structure.md) · [质量标准](docs/teaching-standard.md) · [新课模板](templates/lesson.md) |

## Skill 来源

- [BaratiLab/mechanical-engineering-skills](https://github.com/BaratiLab/mechanical-engineering-skills)：基础图示、习题、材料、机械元件、CAD 与工程分析辅助工具。
- [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)：CAD、工程图、FEA、机器人模型等工具。

当前起步使用 [mechanics-visuals](https://github.com/BaratiLab/mechanical-engineering-skills/tree/main/skills/mechanics-visuals) 与 [worked-problem-generator](https://github.com/BaratiLab/mechanical-engineering-skills/tree/main/skills/worked-problem-generator)。本仓库收录最小许可快照和固定版本链接；不把提示词或源码链接等同于工具安装。

## GPT 网页端最短使用路径

1. 建立 `cad-teacher` Project，将 [项目教学指令](prompts/project-instructions.md) 放入项目指令。
2. 下载并上传 [chatgpt-study-pack.txt](learning/chatgpt-study-pack.txt)。包含原始需求、当前进度、已完成课程反馈、当前课程讲义与示例、来源和起步 Skill 资源。
3. 发送 [恢复学习提示词](prompts/resume-learning.md)，先确认进度，再开始一个知识单元。

有 GitHub 连接时可按需读仓库；没有也能用上传包开展阅读、讲解与问答。Python、CAD 和仓库写入取决于当前实际工具，不保证任意网页会话都具备。网页端尚未在你的账号中实测，验收清单见使用指南。

## 目录

```text
prompts/       原始请求、项目指令、恢复学习提示词
curriculum/    课程路线与阶段能力目标
learning/      讲义、作答、进度、图与代码、固定上传包
resources/     Skill GitHub 地址、固定版本、最小许可快照
templates/     讲义、反馈与验证模板
tools/         上传包生成、文档与计算检查
docs/          网页端指南、教学标准与维护设计
```

已有第一课文件及产物保持原路径。进度集中维护，上传包自动生成，避免多处手改产生不同版本。

## 运行与验证

仅需 Python 3.10+ 标准库即可执行当前课程和维护工具：

```bash
python3 learning/lesson-01.py
python3 learning/lesson-02.py
python3 learning/lesson-03.py
python3 tools/build_study_pack.py
python3 tools/check_project.py
```

后续需要绘图和自动单位检查时，安装可选依赖：

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

计算脚本检查静力平衡和均匀杆自重示例；检查工具验证本地链接、Skill 固定版本格式、第三方文件哈希、教学计算、SVG 和上传包新鲜度。它不代替 CAD、FEA、实物或网页端验收。

## 更新与同步

```bash
git clone https://github.com/Zakariyya/cad-teacher.git
cd cad-teacher
```

每课保留原答和纠正，更新 `learning/progress.md`，重建上传包后用中文提交。已有仓库可运行 `bash publish-github.sh` 检查、提交本教材文件并推送，不创建仓库、不强推。上传包也应替换为最新版本。

[第三方许可声明](resources/THIRD_PARTY_NOTICES.md)。不提交虚拟环境、缓存、凭据或无关临时文件。工程判断区分几何验证、力学估算、仿真验证和实物验证。
