# 通用数据加载流程

所有需要用户个人数据的模块，按以下顺序加载。

## 数据存储

项目使用 **SQLite 数据库** (`assets/user-data/fitness.db`) 作为主存储。JSON 文件 (`profile.json`, `body-log.json`, `workout-log.json`) 作为导入源和备份存在。

### 初始化（首次使用）

```bash
python scripts/db_init.py                                    # 创建数据库
python scripts/db_migrate.py                                 # 从 JSON 迁移数据
```

### 查询

```bash
python scripts/db_query.py latest                            # 最新身体数据
python scripts/db_query.py trend --days 90                   # 体重/体脂趋势
python scripts/db_query.py training --weeks 4                # 训练概况
python scripts/db_query.py progress --exercise 杠铃卧推       # 力量进步
```

---

## 加载顺序

1. 检查 `assets/user-data/fitness.db` 是否存在 → 如不存在，引导用户运行 `python scripts/db_init.py`
2. 运行 `python scripts/db_query.py latest` 获取最新身体数据
3. 需要趋势时运行 `python scripts/db_query.py trend --days N`
4. 需要训练分析时运行 `python scripts/db_query.py training --weeks N`
5. 需要力量进展时运行 `python scripts/db_query.py progress --exercise <名称>`
6. `assets/body-reference.json` → 参考标准对比
7. `assets/food-database.json` → 食材推荐（1657 条，按 name_zh/category 搜索）
8. `assets/exercise-library.json` → 动作推荐（45 个动作，按 primary_muscles 搜索）

---

## 缺失数据策略

| 缺失数据 | 处理方式 |
|---------|---------|
| fitness.db 不存在 | 提示运行 `python scripts/db_init.py` |
| 身高/体重/性别 | 无法计算 BMI/热量，提示用户先记录 |
| 训练历史 | 按初学者水平给保守建议 |
| 体脂率 | 不编造，标注"未提供" |
| 围度数据 | 仅用有的数据做分析 |

---

## 知识库加载策略

1. 先读 `references_book_to_skill/index.md` 定位教材
2. 读目标教材的 `SKILL.md` 获取核心框架 + chapter index
3. 按需读 `chapters/chXX.md`（仅 -detail 模式需要）
