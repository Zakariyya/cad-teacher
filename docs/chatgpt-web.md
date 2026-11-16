# GPT 网页端使用指南

本指南的目标是让教材与学习状态可迁移，而不是承诺每个网页端会话都具备本机 CAD、Python 和 GitHub 写入能力。核对日期：2026-11-16。

## 推荐方式：一个 Project + 一份学习包

1. 在 ChatGPT 网页端创建 `cad-teacher` Project。
2. 将 [项目教学指令](../prompts/project-instructions.md) 的正文放入项目指令。
3. 下载并上传 [chatgpt-study-pack.txt](../learning/chatgpt-study-pack.txt)。它含原始提示词、进度、课程路线、第一课及反馈、第二课讲义与公开示例、已核实的 Skill 地址、起步课 Skill/参考资料和脚本。也可直接粘贴需要的章节。
4. 发送 [恢复学习提示词](../prompts/resume-learning.md)。先让模型准确复述进度，再进入新课。
5. 若当前会话能执行 Python，可运行包内 `learning/lesson-01.py` 和 `learning/lesson-02.py`，核对第二课公开示例反力 26 N、反力矩 6.9 N·m、平衡残差为零。无执行工具时，明确记为“当前会话未运行”，不要把包中的历史结果当成本次执行结果。

Project 支持添加参考文件与项目指令；具体入口与文件数量受计划及工作区设置影响。按你的实际界面操作，不依赖固定套餐上限。[OpenAI：Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)

## 有 GitHub 连接时

在当前界面的应用/插件设置连接 GitHub，授权 `Zakariyya/cad-teacher`，要求先读取 `learning/progress.md` 与 `resources/skills.md`。仓库地址：[cad-teacher](https://github.com/Zakariyya/cad-teacher)。

GitHub 内容是按需读取，不是把所有文件自动同步进模型上下文。可用体验和权限依产品界面而异，不能假设每个网页端会话都能写入。当前能否提交，以实际暴露的工具和授权为准。[OpenAI：Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

## 能力边界与可用替代方案

| 场景 | 可做什么 | 不能据此声称 |
| --- | --- | --- |
| 只有文本/文件阅读 | 学概念、看图说明、做题、检查推理、读取内嵌 Skill 资源 | 已执行 Python、已运行 CAD |
| 有 Python 执行环境 | 运行标准库脚本；依赖可用时画图、做单位检查 | 已完成真实机械试验 |
| 只提供 GitHub 链接 | 能访问时读取对应内容；不能访问则上传学习包 | 已读完整仓库、已装 Skills |
| 有 Text-to-CAD 工具及后端 | 在实际工具支持范围内建模、导出、检查几何 | 任意普通网页聊天天然拥有本机 CAD 服务 |
| 无 GitHub 写工具 | 输出待更新文件正文，由本地或有权限的会话回写 | 已保存学习进度到仓库 |

ChatGPT Project 本身不提供对你电脑目录的直接访问；已安装到本机的 Skill 不会因为提示词提到它就出现在网页会话中。[OpenAI：Projects and chats](https://learn.chatgpt.com/docs/projects)

## 如何保持进度不丢失

仓库的 `learning/progress.md` 是权威记录，上传包是生成时的快照。每课结束后保存学生原答、反馈、未掌握点和下一步；若只能网页对话，先索取更新文本，再通过有写权限的工具提交。

提交前本地运行：

```bash
python3 tools/build_study_pack.py
python3 tools/check_project.py
```

之后重新上传生成的同名文件，并移除或替换旧上传版本。不要仅依赖跨会话记忆，也不要把旧包和新进度混为一谈。

## 网页端验收清单

- 能复述：第 01 单元已完成，第 02 单元讲义与示例已发布但练习待作答，第 03 单元尚未开始。
- 能指出：曾混淆力与力矩单位，应继续巩固方向表达。
- 能列出两个起步 Skill 的真实 GitHub 来源，并读到包内参考资料。
- 新题先等待回答，不能先给解析。
- 若能运行 Python，展示真实输出；不能运行就明确标注。
- 无写入权限时生成待回写内容，不能声称已更新仓库。

本次已检查上传包内容与本地脚本；尚未在你的 GPT 网页账号中实际上传验收。该清单用于完成真实网页端验收。
