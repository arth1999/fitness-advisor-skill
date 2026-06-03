# /log — 数据记录

## 触发

- 命令: `/log`
- 自然语言关键词: 记录、数据、测量、体重、围度、今天练了、记录训练、导入

## 变体

仅 default 模式——数据记录是结构化对话，不需要简版/详版。

## 行为

### 首次使用

检查 `assets/user-data/fitness.db` 是否存在。如不存在，引导运行：
```bash
python scripts/db_init.py
```
如有旧 JSON 数据，再运行：
```bash
python scripts/db_migrate.py
```

### 身体数据记录

引导用户提供以下字段，确认后用 `scripts/db_query.py` 或直接 INSERT 写入 `fitness.db` 的 `body_log` 表：

```
日期: ____年__月__日（默认今天）
体重: ____kg  体脂率: ____%
腰围: ____cm  臀围: ____cm
胸围: ____cm  上臂围: ____cm  大腿围: ____cm
静息心率: ____bpm  血压: ____/____mmHg
备注: __________
```

写入 SQL 示例（直接用 sqlite3 执行）：
```sql
INSERT INTO body_log (date, weight_kg, body_fat_pct, waist_cm)
VALUES ('2024-06-01', 75.0, 18.5, 85);
```

### 训练记录

引导用户描述训练内容，写入 `fitness.db` 的 `workout_sessions` 和 `workout_sets` 表：

```
训练部位: ____  整体RPE: ____/10
动作1: ____  组1: ____kg×____次 RPE____
             组2: ____kg×____次 RPE____
动作2: ____  ...
```

### JSON 备份

同时更新 `assets/user-data/body-log.json` 和 `workout-log.json` 作为备份。

### 外部导入

引导使用导入脚本：
- Apple Health: `python scripts/import_apple_health.py export.zip`
- 训记 CSV: `python scripts/import_csv_workout.py 文件.csv --format xunji`
- Strong/Hevy: `python scripts/import_csv_workout.py 文件.csv --format strong`

## 数据加载

按 `commands/_shared/data-loading.md` 加载用户档案。

## 安全声明

无需附加（纯数据记录）。
