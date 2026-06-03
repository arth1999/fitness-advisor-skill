---
name: advanced-nutrition-metabolism
description: >
  Practitioner-level reference skill for Advanced Nutrition and Human Metabolism (Gropper, Smith, Carr, 8th Edition).
  Covers macronutrient metabolism, micronutrient biochemistry, energy expenditure, body composition, exercise metabolism,
  and metabolic integration across the fed-fast cycle. Use when answering questions about nutrient digestion, absorption,
  transport, metabolic pathways, vitamin/mineral functions, hormone regulation, exercise fuel selection, or energy balance.
  Provides 14 chapter summaries, a metabolic patterns library, glossary, and practitioner cheatsheet.
version: 1.0.0
tags:
  - nutrition
  - metabolism
  - biochemistry
  - exercise-physiology
  - vitamins
  - minerals
  - energy-balance
  - macronutrients
license: Reference work; original content copyright Cengage Learning
authors:
  - Sareen S. Gropper
  - Jack L. Smith
  - Timothy P. Carr
source: "Advanced Nutrition and Human Metabolism, 8th Edition (Cengage Learning, 2018)"
---

# Advanced Nutrition and Human Metabolism — Agent Skill

## Purpose

This skill provides structured access to the frameworks, metabolic patterns, and reference data from Gropper, Smith & Carr's *Advanced Nutrition and Human Metabolism, 8th Edition*. It is organized for practitioner use: find the framework, apply it to the problem, and provide actionable guidance.

## How to Use This Skill

1. **For metabolic pathway questions**: Start with `chapters/ch03-carbohydrates.md`, `ch05-lipids.md`, or `ch06-protein.md` for pathway details, then use `patterns.md` to identify which metabolic pattern applies.

2. **For exercise and fuel selection questions**: Start with `chapters/ch07-integration-regulation-exercise.md` and `chapters/ch08-energy-expenditure-body-composition.md`. Use `patterns.md` Pattern 8 (Exercise Intensity Fuel Shift) and refer to the cheatsheet tables.

3. **For vitamin/mineral questions**: Start with `chapters/ch09-water-soluble-vitamins.md` through `chapters/ch14-nonessential-trace-minerals.md`. Use `glossary.md` for definitions and `cheatsheet.md` for deficiency red flags and absorption enhancers/inhibitors tables.

4. **For clinical nutrition questions**: Use `cheatsheet.md` for lab values and deficiency signs. Cross-reference with `patterns.md` for absorption competition patterns (Pattern 5) and co-requirement patterns (Pattern 6).

5. **For weight management/energy balance questions**: Start with `chapters/ch08-energy-expenditure-body-composition.md` for BMR equations, PAL categories, appetite hormones, and metabolic syndrome criteria. Apply Pattern 10 (Leptin-Ghrelin Appetite Axis).

## File Map

| File | Content | Use When |
|------|---------|----------|
| `chapters/ch01-the-cell.md` | Cell structure, enzyme regulation, energy principles | Understanding cellular foundations of metabolism |
| `chapters/ch02-digestive-system.md` | GI tract anatomy, digestive secretions, regulation | Questions about digestion, absorption, GI disorders |
| `chapters/ch03-carbohydrates.md` | CHO classification, digestion, glycolysis, TCA, ETC | Carbohydrate metabolism questions |
| `chapters/ch04-fiber.md` | Fiber chemistry, properties, health effects | Dietary fiber questions, GI health |
| `chapters/ch05-lipids.md` | Fatty acids, TAGs, phospholipids, cholesterol, lipoproteins | Lipid metabolism, CVD risk |
| `chapters/ch06-protein.md` | Amino acids, protein digestion, synthesis, turnover | Protein/amino acid questions |
| `chapters/ch07-integration-regulation-exercise.md` | Fed-fast cycle, hormonal regulation, exercise metabolism | Exercise nutrition, metabolic integration |
| `chapters/ch08-energy-expenditure-body-composition.md` | BMR, RQ, body composition, appetite hormones, obesity | Energy balance, weight management |
| `chapters/ch09-water-soluble-vitamins.md` | B-complex vitamins and vitamin C | Water-soluble vitamin questions |
| `chapters/ch10-fat-soluble-vitamins.md` | Vitamins A, D, E, K | Fat-soluble vitamin questions |
| `chapters/ch11-major-minerals.md` | Calcium, phosphorus, magnesium | Major mineral questions |
| `chapters/ch12-water-electrolytes.md` | Water, sodium, potassium, chloride, acid-base balance | Fluid/electrolyte questions |
| `chapters/ch13-essential-trace-minerals.md` | Iron, zinc, copper, selenium, iodine, chromium, manganese, molybdenum | Trace mineral questions |
| `chapters/ch14-nonessential-trace-minerals.md` | Fluoride, arsenic, boron, nickel, silicon, vanadium | Nonessential trace element questions |
| `glossary.md` | 60+ key terms with definitions | Quick definition lookup |
| `patterns.md` | 10 reusable metabolic patterns | Applying metabolic principles to novel problems |
| `cheatsheet.md` | Quick-reference tables: metabolic states, hormones, enzymes, deficiencies, lab values | Rapid clinical reference |

## Key Frameworks (Top 5 Most Practically Useful)

1. **Fed-Fast Cycle (Chapter 7)**: Precisely predicts fuel selection and hormonal profile based on time since last meal. Use for meal timing, fasting, and starvation questions.

2. **Exercise Intensity Fuel Shift (Chapter 7)**: Maps fuel selection to % VO₂ max. Use for sports nutrition, endurance training, and weight management exercise prescription.

3. **Malonyl-CoA Fuel Switch (Chapter 7)**: The molecular mechanism determining whether cells oxidize fat or synthesize it. Use to explain why high-carb diets suppress fat oxidation and why fasting enables it.

4. **AMPK Master Energy Sensor (Chapter 7)**: The kinase that coordinates catabolic/anabolic balance in response to cellular energy status. Use to explain metabolic effects of exercise, fasting, and metformin.

5. **Hepcidin-Ferroportin Iron Axis (Chapter 13)**: The only regulated step in human iron metabolism. Use to interpret iron studies and explain anemia of chronic disease.

## Practitioner Voice Guidelines

- **Use "When X, do Y" formulations**, not "The book explains X."
- **Reference exact values** from the text: RDA/AI numbers, enzyme Km values, time frames in the fed-fast cycle, % VO₂ max thresholds.
- **Name frameworks by their author-derived names**: "AMPK as Master Energy Sensor," "Malonyl-CoA Fuel Switch," "Hepcidin-Ferroportin Axis."
- **Distinguish established mechanisms from hypotheses**: Use "is known to" for confirmed pathways; use "is believed to" or "current evidence suggests" for emerging or uncertain mechanisms.
- **Highlight anti-patterns explicitly**: Common errors in application are as important as correct applications.

## Validation

This skill was generated by systematically reading all 14 chapters of the source textbook, extracting named frameworks, exact definitions, enzyme names, RDA values, and patterns. Each chapter file preserves the book's original terminology, framework names, and quantitative data. The patterns file synthesizes cross-cutting principles that appear across multiple chapters.
