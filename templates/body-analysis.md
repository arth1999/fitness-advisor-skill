# 身体数据分析报告模板

基于用户档案和身体数据生成的分析报告。加载以下数据后填充。

---

## 数据加载清单

- [ ] `assets/user-data/profile.json` — 用户画像
- [ ] `assets/user-data/body-log.json` — 身体数据时间序列
- [ ] `assets/user-data/workout-log.json` — 训练记录
- [ ] `assets/body-reference.json` — 东亚人群参考标准
- [ ] `references_book_to_skill/index.md` → 相关教材章节

---

## 报告模板

```
📊 身体数据分析报告 — {date}

## 基本画像
- 性别：{sex} | 身高：{height_cm}cm | 年龄：{age}岁
- 训练水平：{training_level} | 目标：{goals}

## 当前身体数据 ({latest_date})
| 指标 | 数值 | 参考范围 | 评估 |
|------|------|---------|------|
| 体重 | {weight}kg | — | {trend} |
| BMI | {bmi} | 18.5-23.9(东亚) | {status} |
| 体脂率 | {bf}% | {ref_range} | {status} |
| 腰围 | {waist}cm | <85(男)/<80(女) | {risk_level} |
| 腰臀比 | {whr} | <0.90(男)/<0.85(女) | {risk_level} |
| 静息心率 | {hr}bpm | 50-80 | {fitness_level} |
| 血压 | {bp}mmHg | <120/80 | {risk_level} |

## 趋势分析 (最近 {n} 次测量)
- 体重变化：{start}kg → {end}kg ({delta}kg / {period})
- 体脂率变化：{delta_bf}%
- 去脂体重变化：{delta_ffm}kg（体重变化 - 脂肪变化）

## 训练概况
- 近4周训练次数：{count}次
- 平均每周：{avg}/周
- 主要训练类型：{types}
- 训练一致性：{consistency}%

## 建议
{基于教材规则的个性化建议——训练调整、营养优化、数据跟踪建议}

## ⚠️ 预警
{如有超出参考范围的指标，列出并引用来源}
```

---

## 分析规则

1. **BMI 评估**：使用 body-reference.json 中的 `china_cotf` 标准（非 WHO 国际标准）
2. **体脂率评估**：使用 `body_fat_percentage` 中的东亚调整值（+2%）
3. **腰围风险**：使用 `waist_circumference` 中的中国标准（男≥85cm 女≥80cm 为增加风险）
4. **体重变化速率**：
   - 健康减重：0.5-1.0 kg/周 → `acsm-yundong-chufang`
   - 健康增肌：0.25-0.5 kg/周 → `nsca-cscs`
   - 异常变化：>2kg/周 → 建议评估水分波动或饮食因素
5. **训练频率评估**：对比 `nsca-cscs` 按训练水平的推荐频率
6. **力量趋势**：取每个动作的最重组的 e1RM 估算（Epley公式），计算趋势
