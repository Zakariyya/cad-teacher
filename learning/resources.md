# 教学资源与环境状态

## 本课实际使用的资源

- `mechanics-visuals/SKILL.md`：教学图工作流。
- `mechanics-visuals/references/fbd_style.md`：隔离研究对象、外载荷与反力颜色、支撑等效、坐标与力矩方向规范。
- `worked-problem-generator/SKILL.md`：先计算核对，再设计习题与解析。
- `worked-problem-generator/references/problem_template.md`：情境、已知、求解、假设、分析、常见错误与难度分级。

上述是本机安装的 Skill 资源，不是本仓库自带文件。本仓库不复制第三方 Skill 全文；跨机器使用时需另行安装。第一课的讲义、习题、图和脚本均在本仓库，可以独立阅读和运行。

后续课程资源索引见 [学习目录](README.md)。Text-to-CAD 与机械工程 Skills 已由学习者安装，但未对每个工具的可运行性或上游版本逐一验收。

## 2026-11-14 环境状态

- 项目 `.venv` 使用 Python 3.14.4，虚拟环境不提交。
- Matplotlib 3.11.2 及依赖从本机缓存安装成功，实际生成 PNG 验证通过；该临时验证图不作为教学交付。
- Pint 在本次会话中尚未安装成功：没有找到本地缓存，命令执行环境无法解析 PyPI。
- 这不代表学习者的整台机器不能联网，也不能据此判断系统代理或 TUN 无效。
- 第 01 单元脚本使用 Python 标准库，实际生成教学 SVG 并核算平衡；单位人工逐项检查，不宣称使用 Pint 自动验证。

后续在联网终端按根目录 requirements.txt 安装即可；以上记录是本次会话状态，不代表以后仍然如此。
