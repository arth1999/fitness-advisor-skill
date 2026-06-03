# /food — 饮食营养建议

## 触发

- 命令: `/food`, `/food-simple`, `/food-detail`
- 自然语言关键词: 吃、饮食、营养、热量、蛋白质、碳水、脂肪、减脂餐、增肌餐、膳食、食谱、GI、补剂食物、饿了、喝

## 变体控制

读 `commands/_shared/length-rules.md` 确定输出长度。

- **simple**: 直接查询 food-database.json，给 1 条核心建议 + 1 个替代选项，不加载教材
- **default**: 按下方模板输出完整字段，加载第一优先教材 SKILL.md
- **detail**: 加载第一+第二优先教材章节，每个建议引用具体来源

## 知识库路由

| 优先级 | 教材 | 加载内容 |
|--------|------|---------|
| 第一优先 | `zhongguo-shanzhi-zhinan/SKILL.md` | 膳食宝塔、食物推荐量 |
| 减脂 | `acsm-yundong-chufang/SKILL.md` → 减重章节 | 热量缺口、宏量素配比 |
| 增肌 | `sports-nutrition-handbook/SKILL.md` | 蛋白质时机、正氮平衡 |
| 通用 | `gaoji-yundong-yingyangxue/SKILL.md` | 日内能量平衡、营养周期化 |
| 数据 | `assets/food-database.json` | 食材搜索、GI 值 |

## 输出模板

```
## 当前目标
- {增肌/减脂/维持} · 每日约 {kcal} kcal

## 建议
- {核心建议 1-2 条}
- 推荐食材: {food-database 匹配的 2-3 种食材}

## 时机
- {训练前/中/后营养策略，1-2 句}

## 注意
- {1 条关键注意事项}
```

## 安全声明

附加 `commands/_shared/safety-footer.md` 中的"饮食建议"声明。
