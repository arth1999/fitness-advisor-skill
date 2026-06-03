# /log — 数据记录

## 触发

- 命令: `/log`
- 自然语言关键词: 记录、数据、测量、体重、围度、今天练了、记录训练、导入

## 变体

仅 default 模式——数据记录是结构化对话，不需要简版/详版。

## 行为

### 身体数据记录

引导用户提供以下字段（只填有的），确认后写入 `assets/user-data/body-log.json`：

```
日期: ____年__月__日（默认今天）
体重: ____kg  体脂率: ____%
腰围: ____cm  臀围: ____cm
胸围: ____cm  上臂围: ____cm  大腿围: ____cm
静息心率: ____bpm  血压: ____/____mmHg
备注: __________
```

### 训练记录

引导用户描述训练内容，确认后写入 `assets/user-data/workout-log.json`：

```
训练部位: ____  整体RPE: ____/10
动作1: ____  组1: ____kg×____次 RPE____
             组2: ____kg×____次 RPE____
动作2: ____  ...
```

### 外部导入

引导使用导入脚本：
- Apple Health: `python scripts/import_apple_health.py export.zip`
- 训记 CSV: `python scripts/import_csv_workout.py 文件.csv --format xunji`
- Strong/Hevy: `python scripts/import_csv_workout.py 文件.csv --format strong`

## 数据加载

按 `commands/_shared/data-loading.md` 加载用户档案。

## 安全声明

无需附加（纯数据记录）。
