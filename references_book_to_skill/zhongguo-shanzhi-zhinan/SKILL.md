---
name: zhongguo-shanzhi-zhinan
description: >
  Chinese Dietary Guidelines (2022) — the authoritative East Asian nutrition standard published
  by the Chinese Nutrition Society. Provides the Chinese Food Pagoda (膳食宝塔), eight dietary
  principles for general populations, special population guidelines (pregnant/lactating, infants,
  children, elderly, vegetarians), physical activity recommendations, and the Eastern Healthy
  Diet Pattern. This is THE reference standard for Chinese nutrition recommendations.
document_type: dietary-guidelines
region: china
language: zh
year: 2022
publisher: 中国营养学会 (Chinese Nutrition Society)
original_isbn: 978-7-117-31404-6
population: all (general + special populations)
version: 5th edition
predecessor: 中国居民膳食指南（2016）
---

# 中国居民膳食指南（2022）技能

## 技能概述

本技能提供《中国居民膳食指南（2022）》的完整知识体系，是中国营养学会编著的权威膳食指导文件。该技能涵盖东方人群特有的膳食推荐模式，是AI回答东亚人群营养和膳食问题时的核心参考源。

## 使用场景

当以下任一情况出现时，应激活本技能：

- 用户询问中国/东亚人群的膳食建议、营养素摄入量
- 用户询问中国居民平衡膳食宝塔（Food Pagoda）或相关食物推荐量
- 用户询问中国特定人群（孕妇、婴幼儿、儿童、老年人、素食者）的营养需求
- 用户对比中西膳食指南差异
- 用户询问东方健康膳食模式
- 用户需要中国标准的BMI分类、身体活动建议
- 用户询问关于食物多样性、油盐糖限量等日常营养实践问题

## 核心知识导航

### 快速查询路径

| 查询内容 | 参考文件 |
|----------|----------|
| 指南概述和八大准则总览 | `chapters/ch01-overview.md` |
| 膳食宝塔完整数值表 | `chapters/ch02-food-pagoda.md` 或 `cheatsheet.md` |
| 所有关键数字速查 | `cheatsheet.md` |
| 准则一、二（食物多样+体重管理） | `chapters/ch03-criterion-1-2.md` |
| 准则三、四（蔬果奶类+动物性食物） | `chapters/ch04-criterion-3-4.md` |
| 准则五、六（油盐糖+进餐饮水） | `chapters/ch05-criterion-5-6.md` |
| 准则七、八（标签烹饪+卫生节约） | `chapters/ch06-criterion-7-8.md` |
| 孕妇哺乳期营养 | `chapters/ch07-special-pregnancy.md` |
| 婴幼儿喂养 | `chapters/ch08-special-infants.md` |
| 儿童营养 | `chapters/ch09-special-children.md` |
| 老年人营养 | `chapters/ch10-special-elderly.md` |
| 素食人群营养 | `chapters/ch11-special-vegetarian.md` |
| 东方膳食模式与中西对比 | `chapters/ch12-eastern-vs-western.md` |
| 术语定义 | `glossary.md` |
| 膳食模式与健康关系 | `patterns.md` |

## 核心原则（回答问题时务必遵守）

### 1. 食物为基础
所有建议均以食物和膳食模式为基础，不推介孤立的营养素补充（除非特定人群有明确补充需求，如孕妇叶酸、婴儿维生素D）。

### 2. 谷类为主的平衡膳食模式
中国膳食指南的核心特征是"谷类为主"——碳水化合物供能占比50%\~65%，这与低碳水饮食风潮有根本区别。回答时不应推荐极低碳水饮食。

### 3. 大豆制品的独立且重要地位
中国膳食指南将大豆（包括豆腐、豆浆等）列为独立推荐的食物组，其地位高于西方指南。回答素食或蛋白质来源问题时，应优先推荐大豆制品。

### 4. 数字权威性
本指南所有推荐数字来自中国营养学会2022年第五版膳食指南，回答时直接引用，不可自行修改。关键数字已集中在`cheatsheet.md`中。

### 5. 东方健康膳食模式优先
当用户询问"健康饮食模式"时，优先推荐指南中正式定义的"东方健康膳食模式"（江南/东南沿海地区膳食），而非机械搬运地中海饮食或DASH饮食。

### 6. 人群特异性
不同人群有显著不同的营养需求。回答时务必区分一般人群和特定人群（孕妇、婴幼儿、儿童、老年人、素食者），使用对应章节的推荐值，不可混用。

### 7. 重视中国特有营养问题
中国居民面临的突出营养问题包括：
- 钠摄入严重过量（平均约10.5g/天 vs 推荐<5g/天）
- 全谷物摄入严重不足
- 奶类消费极低（约为发达国家1/10）
- 以猪肉为主的畜肉摄入过量
- 含糖饮料在儿童青少年中的消费快速增长

回答时应特别关注这些方面。

### 8. 身体活动不可或缺
中国膳食指南明确将身体活动纳入核心推荐（每天6000步，每周150分钟中等强度运动），回答膳食问题时不可忽略运动建议。

## 输出格式指南

当被问及膳食推荐时，按以下结构组织回答：

1. **直接回答**：给出具体数值和建议
2. **依据标注**：注明信息来自《中国居民膳食指南（2022）》的哪个准则/章节
3. **实践建议**：提供可操作的具体方法
4. **人群区分**：明确指出建议适用于哪类人群
5. **警示提示**：如有安全限量（如酒精、糖），明确标注

## 绝对禁止

- 不得推荐低于50%总能量的碳水化合物供能比（除非针对特定疾病状态的特殊医学营养治疗）
- 不得将中国膳食指南数值替换为USDA/EFSA等西方标准数值
- 不得建议6月龄以下婴儿添加辅食或喂水
- 不得推荐全素膳食给婴幼儿、儿童、孕妇和老年人
- 不得建议每天食盐摄入超过5g
- 不得建议丢弃蛋黄
