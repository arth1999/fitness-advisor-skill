# Fitness Advisor

基于 26 本专业教材的 AI 运动医学与营养学顾问。支持 Claude Code 终端和微信 Bot 两种使用方式。

## 功能模块

| 命令 | 功能 | 变体 |
|------|------|------|
| `/food` | 饮食营养建议 | `-simple` (100字) / 默认 / `-detail` |
| `/training` | 训练计划与安排 | `-simple` / 默认 / `-detail` |
| `/exercise` | 动作技术解析 | `-simple` / 默认 |
| `/supplement` | 补剂证据评估 | `-simple` / 默认 / `-detail` |
| `/analysis` | 身体与训练数据分析 | `-simple` / 默认 |
| `/plan` | 长期训练方案设计 | 默认 / `-detail` |
| `/log` | 记录身体数据/训练记录 | — |

短命令返回核心结论，detail 命令展开原理并引用教材来源。

## 知识库

采用 [book-to-skill](https://github.com/virgiliojr94/book-to-skill) 方法论构建：从原文提取命名框架、心智模型、决策模式，按章组织，按需加载。

### 覆盖教材

| 领域 | 数量 | 代表教材 |
|------|------|---------|
| 运动生理学 | 2 | 运动生理学 (邓树勋), Advanced Nutrition & Metabolism |
| 解剖与肌动学 | 3 | 运动解剖学, 基础肌动学, 解剖列车 (Myers) |
| 训练与运动处方 | 5 | NSCA CSCS, NASM CPT, ACE IFT, ACSM运动处方指南, 体能训练 |
| 运动营养学 | 8 | 中国居民膳食指南2022, ACSM运动营养学, 高级运动营养学 (Benardot) 等 |
| 运动补剂 | 1 | 8 篇 ISSN 立场声明 |
| 运动医学 | 2 | Brukner & Khan 临床运动医学 v1 + v2 |
| 康复与纠正性训练 | 3 | 重返巅峰, 纠正性训练, 功能性动作科学 (FMS/SFMA) |
| 特殊人群 | 1 | NSCA Essentials of Training Special Populations (40+ 疾病) |
| 执教沟通 | 1 | 执教的语言 |

### 架构

```
references_book_to_skill/          # 26 本教材 (455 文件, 2.5 MB)
  index.md                         # 总路由索引
  <book-slug>/
    SKILL.md                       # 核心框架 + 章节索引
    chapters/                      # 按章按需加载
    glossary.md                    # 术语表
    patterns.md                    # 决策模式
    cheatsheet.md                  # 快速参考

commands/                          # 7 个命令模块
  food.md / training.md / log.md
  analysis.md / plan.md
  exercise.md / supplement.md
  _shared/                         # 共享规则（长度/安全/数据加载）

assets/
  food-database.json               # 1657 种中国常见食物 (32 字段 + GI)
  exercise-library.json            # 45 个标准动作
  body-reference.json              # 东亚人群体测参考值

templates/                         # 输出模板
```

## 安装

### 终端使用

```bash
git clone https://github.com/arth1999/fitness-advisor.git
cp -r fitness-advisor ~/.claude/skills/fitness-advisor
```

在 Claude Code 终端中用 `/food`、`/training` 等命令触发，或自然语言提问自动路由。

### 微信 Bot (cc-connect)

1. 安装 cc-connect:
```bash
npm install -g cc-connect@beta
```

2. 绑定微信:
```bash
cc-connect weixin setup
```

3. 编辑 `~/.cc-connect/config.toml`:
```toml
[[projects]]
name = "fitness-advisor"
path = "/path/to/fitness-advisor"

[projects.agent]
type = "claudecode"

[projects.agent.options]
mode = "default"

[[projects.platforms]]
type = "weixin"
[projects.platforms.options]
token = "你的bot_token"
base_url = "https://ilinkai.weixin.qq.com"
account_id = "你的account_id"

# 注册命令
[[commands]]
name = "food"
prompt = "读 commands/food.md，按 default 模式回答：{{1}}"
# ... 其余命令同上
```

4. 启动:
```bash
cc-connect
```

## 数据资产

- 食物数据库: 1657 种中国常见食物，含热量、三大宏量素、维生素、矿物质、GI 值等 32 个字段
- 动作库: 45 个标准力量训练动作，含目标肌群、关节运动、器械类型、难度分级
- 身体参考: 东亚人群 BMI/体脂/腰围/血压等参考标准

## 项目统计

```
教材总数:     26 本
知识库文件:   455 个
知识库大小:   2.5 MB
命令模块:     7 个 (16 个变体)
食物数据:     1,657 条
动作数据:     45 条
```

## 声明

本知识库提供运动科学和营养学教育信息，不构成医疗诊断或治疗建议。如有伤病或健康问题，请咨询执业医师。

## License

MIT
