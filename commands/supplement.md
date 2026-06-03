# /supplement — 补剂证据评估

## 触发

- 命令: `/supplement`, `/supplement-simple`, `/supplement-detail`
- 自然语言关键词: 补剂、蛋白粉、肌酸、咖啡因、BCAA、HMB、beta-alanine、有用吗、副作用、剂量、怎么吃

## 变体控制

读 `commands/_shared/length-rules.md` 确定输出长度。

- **simple**: 直接给结论（有效/无效/证据不足） + 推荐剂量 + 1 条注意事项
- **default**: 五问框架摘要版
- **detail**: 完整五问框架 + ISSN 立场声明引用 + 同类补剂对比

## 知识库路由

| 优先级 | 教材 | 加载内容 |
|--------|------|---------|
| 第一优先 | `issn-supplements/SKILL.md` | 五问框架、8 篇立场声明 |
| 第二优先 | `acsm-yundong-yingyangxue/SKILL.md` | ch13 补剂章节 |
| 补充 | `nsca-yundong-yingyang/SKILL.md` | 补剂评估视角 |
| 数据 | `assets/food-database.json` | 食物 vs 补剂对比 |

## 输出模板（ISSN 五问框架）

```
## {补剂名称} 评估

### 1. 生理效果
- {声称效果 + 实际机制}

### 2. 证据等级
- {强/中等/弱/证据不足}
- 来源: ISSN 立场声明 / ACSM

### 3. 剂量方案
- 推荐: {x}g/天，{时机}
- 周期: {是否需要循环}

### 4. 安全性
- 副作用: {已知 + 未知}
- 禁忌: {人群/药物交互}

### 5. 适用性
- 对 {增肌/力量/耐力/减脂} 的效果
- 结论: {一句话总结}
```

## 安全声明

附加 `commands/_shared/safety-footer.md` 中的"补剂建议"声明。
