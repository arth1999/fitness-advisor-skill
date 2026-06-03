# /analysis — 身体数据分析

## 触发

- 命令: `/analysis`, `/analysis-simple`
- 自然语言关键词: 分析、趋势、变化、报告、进度、评估、身体数据

## 变体控制

读 `commands/_shared/length-rules.md` 确定输出长度。

- **simple**: 仅输出关键指标 + 趋势一句话 + 1 条建议
- **default**: 按下方完整模板输出

## 知识库路由

| 优先级 | 教材 | 用途 |
|--------|------|------|
| 第一优先 | `acsm-yundong-chufang/SKILL.md` | 减重速率、运动处方参数 |
| 第二优先 | `nsca-cscs/SKILL.md` | 增肌速率、训练频率标准 |
| 特殊人群 | `nsca-special-populations/SKILL.md` | 如有疾病史 |
| 数据 | `assets/user-data/profile.json` | 用户画像 |
| 数据 | `assets/user-data/body-log.json` | 身体数据序列 |
| 数据 | `assets/user-data/workout-log.json` | 训练记录 |
| 数据 | `assets/body-reference.json` | 参考标准 |

## 输出模板

```
## 基本画像
{性别} · {身高}cm · {年龄}岁 · {训练水平} · 目标: {goals}

## 当前数据 ({日期})
| 指标 | 数值 | 参考范围 | 评估 |
|------|------|---------|------|
| 体重 | {kg} | — | {趋势} |
| BMI | {值} | 18.5-23.9 | {评估} |
| 体脂率 | {%} | — | {评估} |
| 腰围 | {cm} | <85(男)/<80(女) | {评估} |

## 趋势 (近{n}次)
体重: {start}→{end}kg ({delta})
体脂: {delta}%
训练: 近4周{count}次，平均{avg}/周

## 建议
- {1-3 条基于教材的针对性建议}

## 预警
{如有超标指标列出}
```

## 安全声明

附加 `commands/_shared/safety-footer.md` 中的"训练建议"声明。
