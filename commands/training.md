# /training — 训练建议

## 触发

- 命令: `/training`, `/training-simple`, `/training-detail`
- 自然语言关键词: 训练、练、动作安排、加重、组数、次数、减载、今天练什么、练胸、练背、练腿、推拉腿

## 变体控制

读 `commands/_shared/length-rules.md` 确定输出长度。

- **simple**: 直接给动作+重量+组数，不展开原理
- **default**: 按下方模板输出，加载第一优先教材 SKILL.md
- **detail**: 加载教材章节全文，展开训练科学原理

## 知识库路由

| 优先级 | 教材 | 加载内容 |
|--------|------|---------|
| 第一优先 | `nsca-cscs/SKILL.md` | ch18 训练设计，%1RM 表，加重规则 |
| 增肌 | `nasm-cpt/SKILL.md` | OPT 模型阶段对应 |
| 力量 | `yundong-shenglixue/SKILL.md` | 神经适应、肌纤维募集 |
| 减脂 | `acsm-yundong-chufang/SKILL.md` | 减重期训练调整 |
| 规则 | `references/strength-training.md` | 加重规则、%1RM 表 |
| 数据 | `assets/exercise-library.json` | 动作选择 |
| 数据 | `assets/user-data/workout-log.json` | 训练历史 |

## 输出模板

```
## 本次训练
| 动作 | 重量 | 组数×次数 | 休息 |
|------|------|----------|------|
| {动作1} | {kg} | {组}×{次} | {秒} |
| {动作2} | {kg} | {组}×{次} | {秒} |
| ... | | | |

## 调整
- {相比上次的变化 + 依据}

## 要点
- {1-2 条关键提示}
```

## 安全声明

附加 `commands/_shared/safety-footer.md` 中的"训练建议"声明。
