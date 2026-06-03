# 🏋️ Fitness Advisor

面向东亚人群的 AI 运动医学与营养学顾问。基于 **26 本专业教材的结构化知识库**，提供训练计划设计、营养建议、动作分析、伤病判断、补剂评估等决策支持。

## 📚 知识库

采用 [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) 方法论构建：**提取结构，而非摘要** —— 每本教材编译为命名框架、心智模型、决策模式，按章组织，按需加载。

### 覆盖领域

| 领域 | 教材数 | 核心教材 |
|------|--------|---------|
| 🫀 运动生理学 | 2 | 运动生理学(邓树勋)、Advanced Nutrition & Metabolism |
| 🦴 解剖与肌动学 | 3 | 运动解剖学、基础肌动学、解剖列车(Myers) |
| 🏋️ 训练与处方 | 5 | NSCA CSCS、NASM CPT、ACE IFT、ACSM运动处方指南、体能训练(中国) |
| 🥗 运动营养学 | 8 | 中国居民膳食指南2022、ACSM运动营养学、NSCA运动营养指南、高级运动营养学(Benardot)、Sports Nutrition Handbook、临床运动营养学、营养学概念与争论(Sizer)、中国营养科学全书 |
| 💊 运动补剂 | 1 | 8篇 ISSN 立场声明（肌酸/蛋白/咖啡因/β-丙氨酸/HMB/女性运动员） |
| 🏥 运动医学 | 2 | Brukner & Khan 临床运动医学 v1 + v2 |
| 🔧 康复与纠正 | 3 | 重返巅峰(中国)、纠正性训练、功能性动作科学(FMS/SFMA) |
| 👥 特殊人群 | 1 | NSCA Essentials of Training Special Populations (40+疾病) |
| 🗣️ 执教沟通 | 1 | 执教的语言 |

### 知识库架构

```
references_book_to_skill/          ← 26本教材的完整知识库 (455 files, 2.5MB)
├── index.md                       ← 总路由索引
├── <book-slug>/
│   ├── SKILL.md                   ← 核心框架 + 章节索引 (~4K tokens)
│   ├── chapters/                  ← 按章按需加载 (~1K tokens/章)
│   ├── glossary.md                ← 术语表
│   ├── patterns.md                ← 可复用决策模式 ("Use X when Y")
│   └── cheatsheet.md              ← 快速参考表

references/                        ← 跨教材编译决策规则 (95 rules, 82KB)
assets/
├── food-database.json             ← 1657种中国常见食物 (32个营养字段 + GI)
├── exercise-library.json          ← 45个标准动作 (6类运动模式)
└── body-reference.json            ← 东亚人群体测参考值 (20个数据模块)
```

## 🚀 使用方式

安装为 Claude Code Skill：

```bash
git clone https://github.com/arth1999/fitness-advisor.git
cp -r fitness-advisor ~/.claude/skills/fitness-advisor
```

然后在 Claude Code 中通过 `/fitness-advisor` 或自然语言触发。Skill 会根据意图自动路由到相应的教材章节。

## 🔬 方法论

### 知识工程流水线

```
PDF 教材
  → MinerU OCR (KU Leuven HPC, ~50MB MD输出)
  → book-to-skill 结构化提取 (per-agent 处理, 5-30 min/book)
  → SKILL.md + chapters/ + glossary + patterns + cheatsheet

每个 agent 的提取步骤:
  1. 阅读原文 → 识别章节结构
  2. 每章提取: 核心观点 + 命名框架 + 心智模型 + 反模式 + 关键结论
  3. 生成术语表 + 决策模式 + 速查表
  4. 编译为带 YAML 元数据的可加载 Skill
```

### 设计原则

- **提取结构，不写摘要** — 保留作者的命名框架、精确表述和决策规则
- **按需加载** — SKILL.md (~4K tokens) 包含完整索引；章节文件 (~1K tokens) 仅在需要时加载
- **实践者语气** — "Use X when Y"，不是"The book explains X"
- **可追溯** — 每个框架和术语标注来源章节

### 加载流程

```
用户查询
 → 读 index.md 匹配意图 → 定位目标 skill
 → 读 <skill>/SKILL.md (核心框架 + chapter index)
 → 按 topic index 定位到具体 chapter
 → 读 <skill>/chapters/<chXX>.md
 → 跨域验证时加载第二优先 skill
 → 查询 assets/*.json 获取数据
 → 输出建议
```

## 🌏 东亚适配

- **BMI 切点**: 正常 18.5-23.9，超重 24-27.9，肥胖 ≥28（WHO西太平洋标准 + 中国COTF标准）
- **食材数据**: 基于《中国食物成分表》（第6版），非 USDA 数据
- **膳食指南**: 中国居民膳食宝塔（2022），非 MyPlate
- **训练传统**: 整合"三从一大"、基本功、举国体制等中国特色训练方法
- **常见体态**: 东亚人群高发的上交叉综合征、骨盆前倾评估和纠正方案
- **康复方法**: 中西结合——McGill 方法与中医筋膜视角互补

## 📊 项目统计

```
教材总数:     26 本
知识库文件:   455 个
知识库大小:   2.5 MB
数据资产:     1,657 食物 + 45 动作 + 20 体测模块
编译规则:     95 条 (旧版 references/)
总覆盖领域:   11 个
```

## ⚠️ 声明

本知识库提供运动科学和营养学教育信息，**不构成医疗诊断或治疗建议**。如有伤病、疼痛或健康问题，请咨询执业医师或物理治疗师。

## 📄 License

MIT
