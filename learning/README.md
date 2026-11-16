# 工业机器人学习目录

固定产出目录：本目录 `learning/`。按学习单元保存，修改同一单元时沿用原文件名。
学习背景：约 7 年 Java 后端经验；机械、电路从基础开始。

## 教学约定

- 每次一个知识单元：物理意义 → 机器人对象 → 公式及单位 → 示例 → 两道题 → 根据回答反馈。
- 练习答案先不展示；检查过程、单位、方向和物理解释后再推进。
- 计算实际运行 Python；输入、假设、适用范围和未验证项必须明确。
- 区分几何验证、力学估算、仿真验证、实物验证。
- 默认使用 SI 单位、右为 x 正向、上为 y 正向、平面内逆时针力矩为正；可按用户教材调整。

## 学习路线（每个阶段拆成多节课）

本页保留首版学习目录；详细知识单元与阶段能力检查见 [长期课程路线](../curriculum/roadmap.md)。全部 Skill 的 GitHub 地址与固定版本见 [来源索引](../resources/skills.md)。原始教学要求见 [原始提示词](../prompts/original-request.md)。

| 阶段 | 顺序与机器人对象 | 优先资源 |
| --- | --- | --- |
| 1 静力学入门 | 力与单位 → 力矩 → 支撑与受力图 → 平衡 → 多载荷与重心；相机支架、机械臂 | mechanics-visuals/references/fbd_style.md；worked-problem-generator/references/problem_template.md |
| 2 材料与变形 | 应力、应变、弹性模量 → 拉压、弯曲、扭转 → 刚度、强度与安全系数；连杆与轴 | mechanics-visuals/scripts/mech_plots.py；material-selection/references/materials.csv、indices.md；quick-fea/references/hand_calcs.md |
| 3 参数化 CAD 与图纸 | 基准、草图约束、拉伸、孔与圆角 → 装配接口与工程图；支架、法兰、轴套 | parametric-part-cad/scripts/example_flanged_bushing.py、build_part.py；references/design_defaults.md；Text-to-CAD 工具在实际使用时读取对应 Skill |
| 4 机械传动 | 螺栓 → 轴 → 轴承 → 齿轮 → 公差链；机器人关节 | machine-element-sizing/scripts/me_sizing.py、references/materials.md；tolerance-stackup/scripts/example_chain.csv、stackup.py |
| 5 运动学与动力学 | 位置、速度、加速度 → 转动惯量 → 转矩与功率 → 坐标变换、正逆运动学；单关节到双连杆 | worked-problem-generator；linkage-synthesis/scripts/linkage.py（仅平面刚性连杆运动学，无动力学） |
| 6 电路与嵌入式 | 电压电流电阻 → 驱动与供电 → PWM、编码器 → MCU 定时器与通信 | 当前扫描的机械 Skill 不覆盖完整课程；按具体硬件补充官方数据手册与例程 |
| 7 控制与 ROS 2 | 反馈、采样、PID、轨迹 → URDF、TF、节点通信、ros2_control 与系统集成 | 已安装 robot-simulation 可作为建模辅助，使用前读取；控制与 ROS 2 版本相关内容需查官方文档 |
| 8 综合设计与验证 | 小型机械臂：需求 → 计算 → CAD → 仿真 → 制造装配 → 实测 | quick-fea/scripts/fea.py；dfm-review/references/rules.md；engineering-calc-report/scripts/calc_template.py；design-review-package |

## 扫描边界

检查了本机 `/home/anan/.codex/skills` 的 SKILL.md 与文件树，并重点阅读上述机械基础相关 Skill。资源是分散安装的 Skill 目录，不将其表述为已验证版本的上游完整仓库。未对所有计算器做运行验收，也未把专业增材制造、CFD、逆向设计工具作为零基础前置课。

已完成单元：01、02。第二课「支架自重与重心」的讲解、概念检查、基础题、工程应用题和力矩物理解释均已完成。下一单元：03「多载荷平衡」。详见 [进度](progress.md) 与 [第二课反馈](lesson-02-review.md)。
