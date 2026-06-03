---
name: jichu-jidongxue
description: 基础肌动学知识库 — 生物力学、关节运动学、肌肉功能、步态分析。当需要分析人体运动的生物力学原理、评估关节功能、理解肌肉拉线力学、或解释步态异常时使用。
version: 1.0
source: 基础肌动学（第4版）Mansfield & Neumann
source_type: textbook
domain: kinesiology, biomechanics, physical therapy, rehabilitation
language: zh-CN
chapters: 13
---

# 基础肌动学（第4版）— 技能知识库

## 使用场景
- 在分析某个关节运动时，调取对应章节 biomechanical 框架
- 在评估步态异常时，使用 Ch12 的异常步态分类与代偿逻辑
- 在面对肌肉功能问题时，使用 Ch3 的长度-张力关系、主动/被动不足
- 在进行关节松动术时，参考 Ch1 的凹凸运动学规则
- 在设计训练方案时，使用 Ch1 的杠杆系统分析和开链/闭链选择

## 章节索引

| 章节 | 文件 | 核心内容 |
|------|------|---------|
| Ch01 | chapters/ch01-jibenyuanli.md | 运动平面/旋转轴/凹凸规则/杠杆系统/力矩/拉力线/开闭链 |
| Ch02 | chapters/ch02-guanjie-jiegou-gongneng.md | 关节分类/滑膜关节7型/结缔组织/关节稳定性 |
| Ch03 | chapters/ch03-gugeji-jiegou-gongneng.md | 收缩类型/长度-张力/力量-速度/主动不足/被动不足/力偶 |
| Ch04 | chapters/ch04-jian-guanjie.md | 肩关节复合体/肩肱节律/肩峰下撞击/肩袖 |
| Ch05 | chapters/ch05-zhou-guanjie.md | 肘关节/前臂旋前旋后/提携角 |
| Ch06 | chapters/ch06-wan-guanjie.md | 桡腕关节/腕骨间关节/腕管 |
| Ch07 | chapters/ch07-shou-jiegou.md | 手弓/拇指CMC/内在肌/外在肌/抓握模式 |
| Ch08 | chapters/ch08-jizhu-jiegou.md | 脊柱曲度/椎间盘/关节突关节/核心稳定 |
| Ch09 | chapters/ch09-kuan-guanjie.md | 髋臼/股骨头/外展肌力臂/Trendelenburg |
| Ch10 | chapters/ch10-xi-guanjie.md | 交叉韧带/半月板/髌股机制/锁定机制 |
| Ch11 | chapters/ch11-huai-zu.md | 距下关节/跗横关节/旋前旋后/足弓 |
| Ch12 | chapters/ch12-buxing-yuanli.md | 步行周期8时相/肌肉激活序列/10种异常步态 |
| Ch13 | chapters/ch13-jujue-tongqi.md | 颞下颌关节/胸廓通气力学 |

## 辅助文件
- `glossary.md` — 核心术语速查，按概念群组织
- `patterns.md` — 可复用的生物力学分析模式、抗代偿模式、常见错误
- `cheatsheet.md` — 杠杆类型速查表、力矢量判断表、关节凹凸面规则、步态时序表

## 核心分析框架

### 受力分析四步法
1. 确定旋转轴（内外轴/前后轴/垂直轴）
2. 确定力（内力=肌肉，外力=重力+外在负荷）
3. 确定力臂（内部力臂=肌肉到轴的距离，外部力臂=外力到轴的距离）
4. 计算力矩方向与大小：内部力矩 vs 外部力矩

### 肌肉功能判断三步法
1. 画拉力线 — 相对于关节旋转轴的位置
2. 判方向 — 拉力线在轴前方→屈曲/在轴后方→伸展
3. 找力偶 — 多块肌肉不同拉线方向，但产生同一旋转力矩

### 步态分析框架
1. 确定步行周期时相（0%~100%）
2. 识别支撑腿/摆动腿
3. 按关节逐一分析：髋→膝→踝的矢状面运动、冠状面稳定、水平面旋转
4. 比正常激活序列，找出异常肌肉激活或代偿
