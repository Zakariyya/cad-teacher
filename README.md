# cad-teacher

面向有约 7 年 Java 后端经验、正在转向工业机器人开发的学习者，记录从基础力学到机器人系统集成的课程、练习、反馈与进度。

## 从哪里继续

- [学习进度](learning/progress.md)：每次恢复学习先读这里。
- [完整学习目录与教学约定](learning/README.md)。
- [第 01 单元：静止水平支架的受力分析](learning/lesson-01.md)。
- [第 01 单元：学生作答与反馈](learning/lesson-01-review.md)。
- [教学资源来源与环境状态](learning/resources.md)。

当前进度：第 01 单元的两道练习与概念追问已完成；下一单元是支架自重与重心，尚未开始。不以本次简化练习推断已掌握复杂结构分析。

## 验证计算

第 01 单元仅需 Python 标准库：

```bash
python3 learning/lesson-01.py
```

脚本生成同目录下的受力图 SVG 和练习答案 JSON，并检查合力、合力矩残差。后续绘图与自动单位检查可安装：

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

本仓库保留教学用 SVG 和计算结果，便于直接阅读；不提交虚拟环境、依赖缓存、凭据和运行日志。答案已在课堂完成后归档；后续新课仍先让学生作答，再展开答案。

## GitHub 仓库

仓库：[Zakariyya/cad-teacher](https://github.com/Zakariyya/cad-teacher)。在其他电脑获取学习资料：

```bash
git clone https://github.com/Zakariyya/cad-teacher.git
cd cad-teacher
```

后续使用中文提交信息，持续更新同一份学习目录、课程与进度文件。

## 验证边界

几何验证、力学估算、仿真验证、实物验证分别记录。当前只有理想静力模型的计算核算，没有进行 CAD 几何、有限元或实物验证，不能据此判定实际支架安全。
