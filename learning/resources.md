# 教学资源与环境状态

## 本课实际使用的资源

- `mechanics-visuals/SKILL.md`：教学图工作流。
- `mechanics-visuals/references/fbd_style.md`：隔离研究对象、外载荷与反力颜色、支撑等效、坐标与力矩方向规范。
- `worked-problem-generator/SKILL.md`：先计算核对，再设计习题与解析。
- `worked-problem-generator/references/problem_template.md`：情境、已知、求解、假设、分析、常见错误与难度分级。

首次课堂读取的是本机安装资源。本次为跨设备学习补充了上述两个 Skill 及参考资料的固定版本快照，另附 mechanics-visuals 绘图脚本与完整 MIT 许可证。见 [来源索引](../resources/skills.md)、[快照说明](../resources/README.md) 和 [许可](../resources/THIRD_PARTY_NOTICES.md)。快照是阅读与复现材料，不等于已安装执行工具。

后续课程资源索引见 [学习目录](README.md)。Text-to-CAD 来源是 [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)；机械工程 Skills 来源是 [BaratiLab/mechanical-engineering-skills](https://github.com/BaratiLab/mechanical-engineering-skills)。本次核对了 Skill 路径及固定版本，但未对每个工具逐一运行验收。

## 2026-11-14 首课环境记录（历史状态）

- 项目 `.venv` 使用 Python 3.14.4，虚拟环境不提交。
- Matplotlib 3.11.2 及依赖从本机缓存安装成功，实际生成 PNG 验证通过；该临时验证图不作为教学交付。
- Pint 在本次会话中尚未安装成功：没有找到本地缓存，命令执行环境无法解析 PyPI。
- 这不代表学习者的整台机器不能联网，也不能据此判断系统代理或 TUN 无效。
- 第 01 单元脚本使用 Python 标准库，实际生成教学 SVG 并核算平衡；单位人工逐项检查，不宣称使用 Pint 自动验证。

以上是首课发生时的历史记录。之后本地 Git 写入与网络权限已恢复，并完成本地/远端同步；不再用首课网络失败描述当前环境。Pint 是否可用应在实际需要单位检查的课程中重新检测。网页端用法见 [使用指南](../docs/chatgpt-web.md)。
