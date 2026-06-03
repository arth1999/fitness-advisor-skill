# Fitness Advisor

An AI-powered sports medicine and nutrition advisor built on a structured knowledge base of 26 academic textbooks.

## Command Modules

| Command | Function | Variants |
|------|------|------|
| `/food` | Nutrition and diet advice | `-simple` (~100 words) / default / `-detail` |
| `/training` | Workout planning and programming | `-simple` / default / `-detail` |
| `/exercise` | Exercise technique analysis | `-simple` / default |
| `/supplement` | Supplement evidence evaluation | `-simple` / default / `-detail` |
| `/analysis` | Body data and training analytics | `-simple` / default |
| `/plan` | Long-term training program design | default / `-detail` |
| `/log` | Log body measurements and workouts | — |

Short commands return core conclusions. Detail mode expands reasoning with textbook citations.

## Knowledge Base

Built using the [book-to-skill](https://github.com/virgiliojr94/book-to-skill) methodology: extracts named frameworks, mental models, and decision patterns from source texts, organized by chapter for on-demand loading.

### Architecture

```
references_book_to_skill/          # 26 textbooks (455 files, 2.5 MB)
  index.md                         # Master routing index
  <book-slug>/
    SKILL.md                       # Core framework + chapter index
    chapters/                      # Per-chapter files, loaded on demand
    glossary.md                    # Terminology
    patterns.md                    # Reusable decision patterns
    cheatsheet.md                  # Quick reference

commands/                          # 7 command modules
  food.md / training.md / log.md
  analysis.md / plan.md / exercise.md / supplement.md
  _shared/                         # Shared rules (length / safety / data loading)

scripts/                           # Utility scripts
  db_init.py                       # Initialize SQLite database
  db_migrate.py                    # Migrate JSON data to SQLite
  db_query.py                      # Trend / training / strength queries
  import_apple_health.py           # Apple Health XML import
  import_csv_workout.py            # Workout CSV import (Strong, Hevy, etc.)
  merge_gi_data.py                 # Glycemic index data matching

assets/
  food-database.json               # 1,657 foods (32 nutrition fields + GI)
  exercise-library.json            # 45 standard exercises
  body-reference.json              # Population reference standards
  user-data/                       # User data (SQLite + JSON backup)

templates/                         # Output templates
.claude/commands/                  # Slash command registration (16 wrappers)
```

## Installation

```bash
git clone https://github.com/arth1999/fitness-advisor-skill.git
cp -r fitness-advisor-skill ~/.claude/skills/fitness-advisor
```

Initialize the database on first use:

```bash
python scripts/db_init.py
```

If you have existing JSON data, migrate to SQLite:

```bash
python scripts/db_migrate.py
```

## Tools and Methodology

This project was built with the following open-source tools and methods. All third-party contributions are credited.

| Tool / Method | Purpose | Source |
|-----------|------|------|
| [book-to-skill](https://github.com/virgiliojr94/book-to-skill) | Knowledge extraction methodology: named frameworks, mental models, decision patterns, chapter-organized on-demand loading | virgiliojr94 |
| [MinerU](https://github.com/opendatalab/MinerU) | PDF OCR and structured extraction, converting scanned textbooks to Markdown | OpenDataLab, Shanghai AI Lab |
| [Sanotsu/china-food-composition-data](https://github.com/Sanotsu/china-food-composition-data) | OCR extraction of China Food Composition Table (6th ed.) using Qwen2.5-VL-72B vision model | Sanotsu |
| [Sanotsu/fetch-glycemic-index](https://github.com/Sanotsu/fetch-glycemic-index) | Glycemic index systematic review data | Sanotsu |
| [Qwen2.5-VL-72B](https://github.com/QwenLM/Qwen2.5-VL) | Vision-language model for food composition OCR | Alibaba Cloud / Tongyi Lab |
| [cc-connect](https://github.com/chenhg5/cc-connect) | Multi-platform message bridge for Claude Code | chenhg5 |
| [pypdf](https://github.com/py-pdf/pypdf) | PDF splitting (textbook chapter segmentation) | py-pdf |
| [wger-project/wger](https://github.com/wger-project/wger) | Fitness data model reference (training cycles, body measurement schema) | wger |
| [Apple HealthKit](https://developer.apple.com/documentation/healthkit) | Health data export format (export.xml), Apple Health import reference | Apple Inc. |

### Health Reference Standards

Cutoff values used in body data analysis are derived from the following guidelines and studies:

| Standard | Source |
|------|------|
| BMI cutoffs (Asian) | WHO Western Pacific Region + China Working Group on Obesity (COTF) |
| Body fat percentage (Asian adjustment) | ACSM body fat classification; Gallagher 2000 (Am J Clin Nutr) Asian cohort data |
| Waist circumference risk thresholds | China COTF + IDF East Asian standards |
| Waist-to-hip / waist-to-height ratio | WHO; Browning 2010; China cardiovascular risk assessment |
| Blood pressure classification | Chinese Guidelines for Hypertension Prevention and Control 2018 |
| Blood lipids reference | Chinese Guidelines for Prevention and Treatment of Dyslipidemia 2016 |
| Blood glucose reference | Chinese Guidelines for Type 2 Diabetes Prevention and Treatment 2020 |
| Maximum heart rate formulas | ACSM; Tanaka (2001); Gellish (2007) |
| Basal metabolic rate | Mifflin-St Jeor equation (1990) |
| Grip strength reference | China National Physical Fitness Standards 2023; Dodds 2014 |
| Micronutrient reference | Chinese Dietary Reference Intakes (DRIs) 2013; Endocrine Society |
| Macronutrient distribution range | Chinese Dietary Guidelines 2022 |

## Data Sources

### Textbook Knowledge Base

The knowledge base is compiled from the following textbooks, using the book-to-skill methodology to extract structure and decision rules.

**Exercise Physiology**

| Textbook | Authors | Edition | Publisher | Year |
|------|------|------|--------|------|
| Exercise Physiology (运动生理学) | Deng Shuxun, Wang Jian, Qiao Decai, Hao Xuanming | 3rd | Higher Education Press | 2015 |
| Advanced Nutrition and Human Metabolism | Sareen S. Gropper, Jack L. Smith, Timothy P. Carr | 8th | Cengage Learning | 2018 |

**Anatomy and Kinesiology**

| Textbook | Authors | Edition | Publisher | Year |
|------|------|------|--------|------|
| Sports Anatomy (运动解剖学) | Li Shichang | 3rd | Higher Education Press | 2015 |
| Essentials of Kinesiology (基础肌动学) | Paul J. Mansfield, Donald A. Neumann | 4th | Elsevier | 2019 |
| Anatomy Trains (解剖列车) | Thomas W. Myers | 3rd | Beijing Science & Technology Press | 2016 |

**Training and Exercise Prescription**

| Textbook | Authors | Edition | Publisher | Year |
|------|------|------|--------|------|
| NSCA Essentials of Strength Training and Conditioning | G. Gregory Haff, N. Travis Triplett (eds.) | 5th | Human Kinetics | 2023 |
| NASM Essentials of Personal Fitness Training | Brian G. Sutton (ed.), NASM | 7th | Jones & Bartlett | 2022 |
| ACE Personal Trainer Manual | Todd Galati et al., ACE | 5th | American Council on Exercise | 2014 |
| ACSM's Guidelines for Exercise Testing and Prescription (ACSM运动测试与运动处方指南) | Gary Liguori (ed.), ACSM; trans. Wang Zhengzhen | 11th | Beijing Sport University Press | 2026 |
| Strength and Conditioning (体能训练) | Cao Jingwei (ed.), China Sport Science Society | — | Posts & Telecom Press | 2024 |

**Sports Nutrition**

| Textbook | Authors | Edition | Publisher | Year |
|------|------|------|--------|------|
| Chinese Dietary Guidelines (中国居民膳食指南) | Chinese Nutrition Society | 2022 | People's Medical Publishing House | 2022 |
| Encyclopedia of Chinese Nutrition Science (中国营养科学全书) | Yang Yuexin, Ge Keyou (eds.) | 2nd | People's Medical Publishing House | 2019 |
| ACSM's Nutrition for Exercise Science (ACSM运动营养学) | Dan Benardot; trans. Gao Binghong | — | Science Press | 2021 |
| NSCA's Guide to Sport and Exercise Nutrition (NSCA运动营养指南) | Bill Campbell (ed.), NSCA | — | Human Kinetics / Posts & Telecom Press | 2019 |
| Sports Nutrition: A Handbook for Professionals | Christine Karpinski, Christine A. Rosenbloom (eds.) | 6th | Academy of Nutrition and Dietetics | 2017 |
| Advanced Sports Nutrition (高级运动营养学) | Dan Benardot | 2nd | Beijing Science & Technology Press | 2019 |
| Clinical Sports Nutrition (临床运动营养学) | Louise Burke, Vicki Deakin; trans. Wang Qirong | 4th | World Publishing Xi'an | 2011 |
| Nutrition: Concepts and Controversies (营养学: 概念与争论) | Frances S. Sizer, Eleanor N. Whitney; trans. Chen Wei | 15th | Tsinghua University Press | 2024 |

**Sports Supplements**

| Source | Description | Years |
|------|------|------|
| ISSN Position Stands (8 papers) | Creatine, protein, caffeine, beta-alanine, HMB, female athletes, and more | 2013–2021 |
| [Examine.com](https://examine.com) | Supplement evidence level cross-validation | — |

**Sports Medicine**

| Textbook | Authors | Edition | Publisher | Year |
|------|------|------|--------|------|
| Brukner & Khan's Clinical Sports Medicine, Vol 1: Injuries | Peter Brukner, Ben Clarsen, Jill Cook, Ann Cools, Kay Crossley, Mark Hutchinson, Paul McCrory, Roald Bahr, Karim Khan | 5th | McGraw-Hill | 2017 |
| Brukner & Khan's Clinical Sports Medicine, Vol 2: The Medicine of Exercise | Peter Brukner, Karim Khan | 5th | McGraw-Hill | 2019 |
| Rebuilding Milo (重返巅峰) | Aaron Horschig, Kevin Sonthana | — | — | — |

**Corrective Exercise and Assessment**

| Textbook | Authors | Publisher | Year |
|------|------|--------|------|
| The BioMechanics Method for Corrective Exercise (基于生物力学的纠正性训练) | Justin Price; trans. Wang Xiong | Posts & Telecom Press | 2019 |
| Functional Movement Systems (功能性动作科学) | Gray Cook, Jeremy Hall, Matt Cook; trans. Zhang Danyue | Posts & Telecom Press | 2024 |

**Special Populations**

| Textbook | Authors | Edition | Publisher | Year |
|------|------|------|--------|------|
| NSCA's Essentials of Training Special Populations | Patrick L. Jacobs (ed.), NSCA | — | Human Kinetics | 2018 |

**Coaching and Communication**

| Textbook | Authors | Publisher | Year |
|------|------|--------|------|
| The Language of Coaching (执教的语言) | Nick Winkelman; trans. Wang Xiong, Wu Junwei | Posts & Telecom Press | 2022 |

### Nutrition Database

- **Food composition**: China Food Composition Table, Standard Edition, 6th ed. — ed. Yang Yuexin, Peking University Medical Press, 2019. 1,657 common Chinese foods, 32 nutrition fields per 100 g edible portion.
- **Glycemic index**: [Sanotsu/fetch-glycemic-index](https://github.com/Sanotsu/fetch-glycemic-index) — systematic review data published in 2021, merged into the food database via fuzzy matching. Currently 489 of 1,657 foods have GI values.

### Exercise Library

45 standard strength training exercises, compiled from NSCA CSCS 5th, NASM CPT 7th, ACE 5th, Essentials of Kinesiology 4th, and Functional Movement Systems. Includes target muscles, joint actions, equipment type, difficulty level, and safety notes.

### Body Reference Standards

| Metric | Source | Criteria |
|------|---------|------|
| BMI cutoffs | WHO Western Pacific + China COTF | Normal 18.5–23.9, Overweight 24–27.9, Obese >=28 |
| Body fat percentage | ACSM, Asian adjustment | ~2% higher than Western at same BMI |
| Waist circumference risk | China standard | Male >=85 cm, Female >=80 cm |
| Blood pressure | Chinese Hypertension Guidelines 2018 | <120/80 normal |
| Dietary structure | Chinese Dietary Pagoda 2022 | — |
| Training parameters | ACSM, NSCA, NASM | %1RM tables, FITT-VP, progression rules |

## Project Statistics

```
Textbooks:            26
Knowledge base files: 455
Knowledge base size:  2.5 MB
Command modules:      7 (16 variants)
Food entries:         1,657
Exercise entries:     45
```

## Disclaimer

This knowledge base provides educational information in sports science and nutrition. It does not constitute medical diagnosis or treatment advice. Consult a licensed physician or physiotherapist for any injury, pain, or health concerns.

## License

MIT
