# 通用数据加载流程

所有需要用户个人数据的模块，按以下顺序加载：

---

## 加载顺序

1. `assets/user-data/profile.json` → 用户画像（性别/身高/年龄/目标/训练水平/伤病）
2. `assets/user-data/body-log.json` → 身体数据时间序列（如涉及趋势分析）
3. `assets/user-data/workout-log.json` → 训练记录（如涉及训练分析）
4. `assets/body-reference.json` → 参考标准对比
5. `assets/food-database.json` → 食材推荐（1657 条，按 name_zh/category 搜索）
6. `assets/exercise-library.json` → 动作推荐（45 个动作，按 primary_muscles 搜索）

---

## 缺失数据策略

| 缺失数据 | 处理方式 |
|---------|---------|
| 身高/体重/性别 | 无法计算 BMI/热量，提示用户先记录 |
| 训练历史 | 按初学者水平给保守建议 |
| 体脂率 | 不编造，标注"未提供" |
| 围度数据 | 仅用有的数据做分析 |

---

## 知识库加载策略

1. 先读 `references_book_to_skill/index.md` 定位教材
2. 读目标教材的 `SKILL.md` 获取核心框架 + chapter index
3. 按需读 `chapters/chXX.md`（仅 -detail 模式需要）
