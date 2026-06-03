# 数据输入引导模板

当用户想手动记录身体数据或训练数据时，按以下格式引导。

---

## 身体数据输入

向用户询问以下信息（必填项标注*）：

```
请提供以下身体数据（可只填你有的项目）：

* 日期：____年__月__日（默认今天）
* 体重：____kg
  体脂率：____%（如有体脂秤数据）
  腰围：____cm（呼气末、肚脐水平）
  臀围：____cm
  胸围：____cm
  上臂围：____cm（屈臂/放松？）
  大腿围：____cm
  小腿围：____cm
  颈围：____cm
  静息心率：____bpm（早晨起床前测量）
  血压：____/____mmHg（如有）
  备注：__________
```

确认后写入 `assets/user-data/body-log.json`。

---

## 训练记录输入

向用户询问：

```
请描述今天的训练：

* 日期：____年__月__日
* 训练部位/重点：____（如"胸+三头"、"腿"、"5km跑"）
* 整体感受 RPE (1-10)：____

动作1：________
  组1：重量____kg × ____次  RPE____
  组2：重量____kg × ____次  RPE____
  组3：重量____kg × ____次  RPE____

动作2：________
  ...

备注：__________
```

确认后写入 `assets/user-data/workout-log.json`。

---

## 外部导入

引导用户使用导入脚本：

```
你可以从以下来源导入数据：

1. 🍎 Apple Health：从 Health.app → 导出 → 获取 export.zip
   运行：python scripts/import_apple_health.py export.zip

2. 📱 训记 App：导出 CSV
   运行：python scripts/import_csv_workout.py 训记导出.csv --format xunji

3. 🏋️ Strong / Hevy：导出 CSV
   运行：python scripts/import_csv_workout.py 导出.csv --format strong

4. 📊 任意 CSV：确保包含 date, exercise, weight_kg, reps 列
   运行：python scripts/import_csv_workout.py 文件.csv
```
