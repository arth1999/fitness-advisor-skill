---
name: acsm-yundong-chufang
description: >
  ACSM运动测试与运动处方指南（第十一版）结构化知识库。
  提供基于FITT-VP原则的运动处方制订指导，覆盖运动前健康筛查与危险分层、
  健康体适能测试、临床运动测试、各类慢性疾病的运动处方（心血管、代谢、肺部、
  神经系统、骨骼肌肉等）、特殊人群（儿童青少年、老年人、妊娠期）、
  环境因素（高原、寒冷、热环境）以及行为改变策略。
  When to use:
  - 用户询问运动处方的FITT-VP参数或运动强度/频率/时间/方式建议
  - 用户需要针对特定慢性疾病（高血压、糖尿病、肥胖、冠心病、COPD等）的运动建议
  - 用户咨询运动前健康筛查流程或心血管疾病危险分层
  - 用户询问老年人、孕妇、儿童青少年等特殊人群的运动注意事项
  - 用户需要了解高原/寒冷/热环境中的运动调整策略
  - 用户询问运动测试方案（心肺耐力、肌肉适能、柔韧性测试等）
  - 用户需要行为改变策略以提高运动依从性
source_book:
  title: "ACSM运动测试与运动处方指南（第十一版）"
  title_en: "ACSM's Guidelines for Exercise Testing and Prescription, 11th Edition"
  editor: "Gary Liguori, PhD, FACSM (Senior Editor)"
  translator: "王正珍"
  publisher: "北京体育大学出版社"
  year: 2026
  original_year: 2022
  organization: "American College of Sports Medicine (ACSM)"
language: zh-CN
version: "1.0"
---

# ACSM运动测试与运动处方指南（第十一版）— 结构化技能

## 知识库概述

本技能将ACSM运动测试与运动处方指南（第十一版）全面转化为结构化知识库，涵盖从运动前评估到各类人群运动处方的完整临床决策链。核心框架围绕ACSM的FITT-VP原则构建，并结合每类特殊人群的循证调整建议。

## 使用方式

基于用户的查询，确定最相关的章节或速查表：
- **通用运动处方** → ch05 + cheatsheet FITT表格
- **运动前筛查/危险分层** → ch02 + patterns.md 决策模式
- **特定疾病运动处方** → ch08(ch09, ch10, ch11) + cheatsheet 特殊人群表格
- **特殊健康人群** → ch06 + cheatsheet
- **环境因素** → ch07 + cheatsheet 环境表格
- **测试方法和标准** → ch03(ch04) + glossary
- **行为改变** → ch12

## 核心临床决策链

```
运动前评估 (ch02)
  ├── 知情同意书
  ├── ACSM运动前健康筛查流程 (2步骤)
  ├── CVD危险因素分析 (8项)
  └── 危险分层 (AACVPR低/中/高危)
        │
        ▼
体适能测试 (ch03/ch04)
  ├── 健康体适能测试 (安静HR/BP → 身体成分 → CRF → 肌适能 → 柔韧 → 平衡)
  └── 临床运动测试 (适应证 → 禁忌证 → 方案选择 → 监测 → 终止指征 → 结果分析)
        │
        ▼
运动处方Ex Rx (ch05-ch12)
  ├── FITT-VP通用框架 (ch05)
  │   ├── 有氧运动: F≥3d/wk, I=40-89% HRR, T≥150min/wk, T=A-D组, V≥500-1000 MET-min/wk
  │   ├── 抗阻训练: F≥2-3d/wk, I=60-80% 1-RM, T=8-12rep×1-3组, T=多关节+单关节+核心
  │   └── 柔韧性: F≥2-3d/wk, I=紧绷/轻微不适, T=10-30s×2-4次, T=静力/动力/PNF
  └── 特殊调整 (ch06-ch12)
      ├── 人群调整: 儿童↑ 老年人← 妊娠← (ch06)
      ├── 环境调整: 高原↓ 寒冷← 热↓ (ch07)
      ├── 心血管/肺部疾病 (ch08)
      ├── 代谢性疾病 (ch09)
      ├── 其他慢性病 (ch10)
      ├── 脑健康/脑部疾病 (ch11)
      └── 行为改变策略 (ch12)
```

## 关键数值速记 (Must-Know Numbers)

| 参数 | 数值 |
|-----|------|
| 有氧最低推荐量 | ≥150min/周中等强度 或 ≥75min/周较高强度 |
| 额外获益目标 | 300min/周中等强度 或 150min/周较高强度 |
| 中等强度范围 | 40%-59% HRR, RPE 12-13, 3.0-5.9 METs |
| 较高强度范围 | 60%-89% HRR, RPE 14-17, 6.0-8.7 METs |
| 抗阻训练 | ≥2天/周, 60%-80% 1-RM, 8-12次×1-3组 |
| 柔韧性 | 保持10-30s, 每个动作2-4次 |
| MET-min目标 | ≥500-1,000 MET-min/wk |
| 每日步数 | 7,000-8,000步/天, ≥3,000步快走 |
| 低强度定义 | <30% HRR, <2.0 METs, RPE<9 |
| 血压运动终止 | SBP>250或DBP>115mmHg |
| 最大心率公式(推荐) | 208-(0.7×年龄) (Tanaka) 或 207-(0.7×年龄) (Gellish) |
| 体重管理运动量 | 减重: >250min/周; 维持: 200-300min/周 |

## 章节索引

| 章节 | 文件 | 主题 |
|-----|------|------|
| 第一章 | chapters/ch01-benefits-risks.md | 体力活动的益处和风险 |
| 第二章 | chapters/ch02-pre-exercise-evaluation.md | 运动前评估与筛查 |
| 第三章 | chapters/ch03-fitness-testing.md | 健康体适能测试 |
| 第四章 | chapters/ch04-clinical-exercise-testing.md | 临床运动测试与结果分析 |
| 第五章 | chapters/ch05-exercise-prescription-principles.md | FITT-VP运动处方基本原则 |
| 第六章 | chapters/ch06-special-populations.md | 健康特殊人群(儿童/老年人/妊娠) |
| 第七章 | chapters/ch07-environment.md | 环境因素(高原/寒冷/热环境) |
| 第八章 | chapters/ch08-cardiovascular-pulmonary.md | 心血管与肺部疾病处方 |
| 第九章 | chapters/ch09-metabolic-diseases.md | 代谢性疾病处方 |
| 第十章 | chapters/ch10-other-chronic-conditions.md | 其他慢性疾病处方 |
| 第十一章 | chapters/ch11-brain-health.md | 脑健康和脑部疾病处方 |
| 第十二章 | chapters/ch12-behavior-change.md | 行为改变和运动促进策略 |

## 支持资源

| 文件 | 内容 |
|-----|------|
| glossary.md | 中英文术语表，含核心概念定义 |
| patterns.md | 临床决策流程图，含筛查、处方、进阶、环境模式 |
| cheatsheet.md | 综合速查表，含FITT-VP总览、危险分层、全部特殊人群处方对照 |
