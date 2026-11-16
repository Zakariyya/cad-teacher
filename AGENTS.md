# cad-teacher 协作与教学规范

- 每次继续学习先读 `learning/progress.md`、对应作答反馈和 `prompts/project-instructions.md`。
- 原始需求保存在 `prompts/original-request.md`，不可改写；后续要求记录在项目教学指令中。
- 每次一个知识单元；先物理意义，再公式单位；每课两题，学生回答前不展示答案。
- 优先读取 `resources/skills.md` 对应的真实参考文件/脚本。工具不可用时明确边界；不得虚构执行结果。
- 保留学生原答；把数值、单位、方向、假设、理解分别评价。更新进度不得虚构完成新课。
- 所有设计计算给出已知、假设、适用范围、风险；区分几何、力学估算、仿真和实物证据。
- 保留 `learning/` 已确定的产物路径，修改同一课时沿用原文件名。
- 原始资料、来源版本、许可与本项目讲义分开；引用新 Skill 时补登记。
- 改动后运行 `python3 tools/build_study_pack.py` 和 `python3 tools/check_project.py`。
- 新课登记到 `curriculum/lessons.json`，未作答的课设 `feedback_published: false`，例题脚本不得夹带习题答案；公开反馈后再收录解析。待公开答案不要提交到公开仓库。
- Git 提交信息用中文，按当前用户授权提交推送；不上传虚拟环境、凭据、缓存和无关临时文件。
- 不添加 alias codex 或名为 codex 的 shell 函数，不包装真实 codex 命令。
