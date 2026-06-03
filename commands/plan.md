# /plan — 训练方案设计

## 触发

- 命令: `/plan`, `/plan-detail`
- 自然语言关键词: 方案、计划、周期、阶段、长期、program、周期化、下个周期、设计计划

## 变体控制

读 `commands/_shared/length-rules.md` 确定输出长度。

- **default**: 给出 4-12 周周期化框架（阶段划分 + 每阶段目标 + 关键动作）
- **detail**: 完整周期化方案，macrocycle → mesocycle → microcycle，每阶段变量参数

## 知识库路由

| 优先级 | 教材 | 加载内容 |
|--------|------|---------|
| 第一优先 | `nsca-cscs/SKILL.md` | ch18 训练设计, ch22 周期化 |
| 第二优先 | `nasm-cpt/SKILL.md` | OPT 5 阶段模型 |
| 中国语境 | `zhongguo-tineng-xunlian/SKILL.md` | 周期训练、冬训概念 |
| 数据 | `assets/exercise-library.json` | 动作选择 |
| 数据 | `assets/user-data/profile.json` | 用户画像 |

## 输出模板

```
## 方案概览
- 周期: {N}周 · 阶段数: {N} · 目标: {goal}

## 阶段划分
### 阶段1: {名称} (第1-{N}周)
- 目标: {xxx}
- 频率: {N}次/周
- 核心动作: {动作列表}
- 强度区间: {xx-xx%1RM}

### 阶段2: ... (同上)

## 进阶逻辑
- {阶段间如何过渡和加重}

## 注意事项
- {1-2 条关键提醒}
```

## 安全声明

附加 `commands/_shared/safety-footer.md` 中的"训练建议"声明。
