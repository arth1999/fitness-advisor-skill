# NASM CPT 7th Edition — Reusable Design Patterns

This document catalogs the key program design patterns and decision-making frameworks from the NASM CPT textbook. These patterns should be referenced when an agent needs to design fitness programs, select exercises, or make programming decisions.

## Pattern 1: OPT Phase Selection by Goal

**When to use**: Client requests a specific fitness goal. Use this pattern to determine which OPT phases are appropriate.

```
Goal: General Fitness / Health
→ Phase 1 (Stabilization Endurance) → Phase 2 (Strength Endurance)
→ Cycle between Phases 1 and 2
→ Focus: Movement quality, function, adherence

Goal: Fat Loss
→ Phase 1 (2–4 weeks, foundation) → Phase 2 (primary, 4–8 weeks)
→ Optionally Phase 3 (Muscular Development) for metabolic effect
→ Cardio: Zone 1 progressing to Zone 2
→ Emphasis: Caloric expenditure, adherence, nutrition guidance

Goal: Muscle Gain (Hypertrophy)
→ Phase 1 (2–4 weeks, foundation) → Phase 3 (primary)
→ Cycle Phase 3 and Phase 2 for variety/recovery
→ Cardio: Zone 1–2, Stage II

Goal: Strength
→ Phase 1 (2–4 weeks) → Phase 2 (4 weeks) → Phase 4 (primary)
→ Cardio: Zone 1–2, Stage II–III

Goal: Athletic Performance / Power
→ Phase 1 → Phase 2 → Phase 4 → Phase 5
→ Use linear periodization for off-season; undulating for in-season
→ Cardio: Zone 2–3, Stage II–III
```

## Pattern 2: Acute Variable Assignment by OPT Phase

**When to use**: Need to set training parameters (reps, sets, intensity, rest, tempo) for a given phase.

```
Phase 1 — Stabilization Endurance
  Reps: 12–20 | Sets: 1–3 | Intensity: 50–70% 1RM | Rest: 0–90s | Tempo: 4/2/1

Phase 2 — Strength Endurance
  Reps: 8–12 | Sets: 2–4 | Intensity: 70–80% 1RM | Rest: 0–60s | Tempo: 2/0/2 (strength) + 4/2/1 (stability)
  Key: Superset strength exercise → stabilization exercise

Phase 3 — Muscular Development (Hypertrophy)
  Reps: 6–12 | Sets: 3–5 | Intensity: 75–85% 1RM | Rest: 0–60s | Tempo: 2/0/2

Phase 4 — Maximal Strength
  Reps: 1–5 | Sets: 4–6 | Intensity: 85–100% 1RM | Rest: 3–5 min | Tempo: X/X/X

Phase 5 — Power
  Reps: 1–5 (strength) + 8–10 (power) | Sets: 3–5 | Intensity: 85–100% (strength) + 30–45% or 10% BW (power)
  Rest: 3–5 min | Tempo: X/X/X
  Key: Superset heavy strength → explosive power exercise
```

## Pattern 3: Integrated Training Component Progressions

**When to use**: Need to assign core, balance, plyometric, SAQ, flexibility, and cardio exercises that match the client's OPT phase.

```
             Phase 1        Phase 2         Phase 3-4       Phase 5
Core:        Stabilization  Strength        Strength        Power
Balance:     Stabilization  Strength        Strength        Power
Plyometric:  Stabilization  Strength        Strength        Power
SAQ:         Stabilization  Strength        Strength        Power
Flexibility: SMR+Static     SMR+Active      SMR+Active+Dynamic  SMR+Dynamic
Cardio:      Zone 1/Stage I Zone 1-2/II     Zone 2/II-III    Zone 2-3/III
```

### Exercise Examples by Component and Level

**Core:**
- Stabilization: Marching, floor bridge, plank, cobra, standing cable push/pull
- Strength: Ball crunch, back extension, cable rotation, reverse crunch
- Power: Med ball rotation chest pass, soccer throw, woodchop throw, overhead throw

**Balance:**
- Stabilization: Single-leg balance, single-leg balance reach, single-leg hip rotation
- Strength: Single-leg squat, single-leg RDL, step-up to balance, lunge to balance
- Power: Multiplanar hop with stabilization, box hop-up/down with stabilization, ice skaters

**Plyometric:**
- Stabilization: Squat jump with stabilization hold, box jump-up/down with stabilization
- Strength: Continuous squat jumps, tuck jumps, butt kicks, power step-ups
- Power: Depth jumps, single-leg hop progression, box-to-box jumps, plyometric push-ups

**SAQ:**
- Stabilization: Cone shuffles, slow controlled ladder drills, backpedal
- Strength: 5-10-5 drill, T-drill, linear runs with directional changes
- Power: Timed 5-0-5, 40-yard dash, pro-agility shuttle, reactive mirror drill

## Pattern 4: Assessment-to-Program Flow

**When to use**: Starting with a new client. Determines the intake and program design workflow.

```
1. Health Screening → PAR-Q+, health history, medical clearance if needed
2. Subjective Assessment → Goals, exercise history, lifestyle, preferences
3. Objective Assessment → RHR, BP, body composition, cardiorespiratory test
4. Static Postural Assessment → Identify deviations (upper crossed, lower crossed, pes planus)
5. Movement Assessment → OHSA, single-leg squat, push/pull assessments
6. Performance Assessment (optional) → Push-up test, strength test, vertical jump, agility
7. Synthesize Findings → Identify overactive/underactive muscles, movement impairments
8. Apply Corrective Exercise Continuum → Inhibit → Lengthen → Activate → Integrate
9. Design Program → Select OPT phase, assign acute variables, select exercises
10. Implement → Coach, cue, provide feedback
11. Reassess → Every 4–6 weeks; compare to baseline
```

## Pattern 5: Corrective Exercise Continuum

**When to use**: A client has identified muscle imbalances or postural deviations.

```
Step 1 — INHIBIT
  Purpose: Decrease overactive muscle tension
  Technique: Self-myofascial release (foam rolling)
  Hold: 30–60 seconds on tender areas
  Targets: Identified overactive muscles from assessment

Step 2 — LENGTHEN
  Purpose: Increase extensibility of short/overactive muscles
  Technique: Static stretching (Phase 1) or active stretching (Phases 2+)
  Duration: Static hold 30+ seconds; Active 5–10 reps × 1–2 sec hold each
  Targets: Same overactive muscles

Step 3 — ACTIVATE
  Purpose: Increase neural drive to underactive muscles
  Technique: Isolated strengthening exercises, positional isometrics
  Reps/Sets: 1–2 sets × 10–15 reps with slow tempo (4/2/1)
  Targets: Identified underactive muscles from assessment

Step 4 — INTEGRATE
  Purpose: Retrain the movement pattern with proper muscle recruitment
  Technique: Multi-joint, functional movements requiring coordination
  Reps/Sets: Low sets; focus on quality
  Targets: The full kinetic chain movement pattern (e.g., squat, push, pull)
```

## Pattern 6: Common Muscle Imbalance Solution Map

**When to use**: A specific postural distortion or compensation pattern is identified.

```
Upper Crossed Syndrome (Forward head, rounded shoulders, thoracic kyphosis)
  Overactive → SMR/Static Stretch: Upper trapezius, levator scapulae, sternocleidomastoid, pectoralis major/minor
  Underactive → Activate: Deep cervical flexors, lower trapezius, serratus anterior, rhomboids

Lower Crossed Syndrome (Anterior pelvic tilt, lumbar lordosis)
  Overactive → SMR/Static Stretch: Hip flexors (iliopsoas, rectus femoris, TFL), erector spinae, latissimus dorsi
  Underactive → Activate: Gluteus maximus, hamstrings, abdominals (transverse abdominis, internal obliques)

Pes Planus Distortion (Flat feet, knee valgus, internally rotated femurs)
  Overactive → SMR/Static Stretch: Peroneals, gastrocnemius, soleus, adductors, TFL, iliopsoas
  Underactive → Activate: Posterior tibialis, anterior tibialis, gluteus medius, gluteus maximus

OHSA — Feet Turn Out
  Overactive: Gastrocnemius + soleus, biceps femoris (short head), TFL

OHSA — Knees Move Inward (Valgus)
  Overactive: Adductors (all), TFL, biceps femoris (short head), vastus lateralis
  Underactive: Gluteus medius/maximus, vastus medialis oblique (VMO)

OHSA — Excessive Forward Lean
  Overactive: Hip flexors (all), gastrocnemius + soleus, abdominals

OHSA — Low Back Arches
  Overactive: Hip flexors (all), erector spinae, latissimus dorsi
  Underactive: Gluteus maximus, hamstrings, abdominals

OHSA — Arms Fall Forward
  Overactive: Pectoralis major/minor, latissimus dorsi, teres major
  Underactive: Lower trapezius, serratus anterior, posterior deltoid, rotator cuff
```

## Pattern 7: Cardiorespiratory Zone Assignment

**When to use**: Need to prescribe cardio intensity and method.

```
Zone 1 (Below VT1)
  Intensity: Low-to-moderate | RPE: 1–4 | Talk: comfortable conversation
  Fuel: Primarily fat | Purpose: Aerobic base, recovery, general health
  Stage: I (Aerobic Base)

Zone 2 (VT1 to VT2)
  Intensity: Moderate-to-vigorous | RPE: 5–6 | Talk: short sentences only
  Fuel: Mixed → progressing to more carb | Purpose: Aerobic capacity, lactate threshold
  Stage: II (Aerobic Efficiency)

Zone 3 (Above VT2)
  Intensity: Vigorous-to-maximal | RPE: 7–10 | Talk: unable to speak
  Fuel: Primarily carbohydrate | Purpose: Anaerobic capacity, speed, power, peak performance
  Stage: III (Aerobic Power)

Intensity Monitoring Methods:
- HRmax %: Zone 1 < ~75%, Zone 2 ~75–85%, Zone 3 > ~85%
- Talk test: Most practical for client self-monitoring
- RPE: 1–10 modified scale; correlate with talk test
```

## Pattern 8: Special Population Modifications

**When to use**: Client presents with a specific health condition.

```
All Special Populations:
  1. Start at Phase 1 (Stabilization Endurance)
  2. Progress more slowly than healthy clients
  3. Obtain medical clearance
  4. Monitor closely; adjust based on individual response

Hypertension (SBP ≥ 130 or DBP ≥ 80):
  Avoid: Valsalva, isometric exercises, heavy loads, rapid position changes
  Include: Zone 1 cardio, Phase 1 resistance, breathing focus

Type 2 Diabetes:
  Check: Blood glucose pre/during/post; have fast-acting carbs available
  Include: Consistency in timing; post-meal sessions; foot inspection

Osteoporosis/Osteopenia:
  Avoid: Spinal flexion (crunching), excessive spinal rotation/twisting
  Include: Weight-bearing exercise, balance training, posture focus

Arthritis:
  Avoid: During acute flare-ups; painful ranges
  Include: Low-impact, water-based, ROM exercises, warm up thoroughly

Pregnancy:
  Avoid: Supine after 1st trimester, Valsalva, fall risk, contact sports, excessive heat
  Include: Phase 1, moderate intensity, pelvic floor and core stabilization

Older Adults:
  Priority: Fall prevention, balance training, functional strength
  Include: Phase 1–2, slower progression, bone-loading activities

Low Back Pain:
  Avoid: Painful movements; loaded spinal flexion
  Include: Core activation (drawing-in), stabilization emphasis, walking for cardio
```

## Pattern 9: Warm-Up and Cool-Down Template

```
WARM-UP (5–10 minutes)
  Phase 1:
    1. SMR (foam roll) — 30–60 sec per muscle, target overactive areas
    2. Static stretching — hold 30+ sec per stretch
    3. Optional: light cardio (5 min)

  Phase 2–4:
    1. SMR (foam roll) — 30 sec per muscle
    2. Active stretching — 5–10 reps, 1–2 sec hold
    3. Dynamic stretching — 10–15 reps per movement
    4. Light cardio (5 min) progressing toward workout intensity

  Phase 5:
    1. SMR (foam roll) — targeted
    2. Dynamic stretching — full ROM, sport-specific
    3. Progressive cardio — build to near-workout intensity

COOL-DOWN (5–10 minutes)
  All Phases:
    1. Light cardio — gradually reduce intensity (3–5 min)
    2. Static stretching — hold 30+ sec per muscle, target all major groups
    3. Optional: SMR if time allows
```

## Pattern 10: Exercise Selection Decision Tree

**When to use**: Need to choose appropriate exercises for a given client, goal, and phase.

```
START
  ↓
What phase? → Phase 1 → Multi-joint; stable surface; body weight or light load; slow tempo
  ↓             Phase 2 → Superset: compound strength → stabilization variant
  ↓             Phase 3 → Compound + isolation; moderate-heavy; moderate volume
  ↓             Phase 4 → Heavy compound; low reps; full recovery
  ↓             Phase 5 → Superset: heavy compound → explosive variant
  ↓
What goal? → General fitness → Multiplanar, functional, varied
  ↓          Fat loss → Compound, high metabolic demand, circuit-friendly
  ↓          Muscle gain → Compound + isolation, progressive overload focus
  ↓          Strength → Heavy compound, long rest, progressive overload
  ↓          Power → Olympic lifts, plyometrics, medicine ball, explosive
  ↓
What level? → Beginner → Machines → Body weight → Light free weights → Cables
  ↓          Intermediate → Free weights → Cables → Moderate plyo → Kettlebell
  ↓          Advanced → Heavy free weights → Olympic lifts → Maximal plyo
  ↓
Any conditions? → Apply Pattern 8 (Special Population Modifications)
  ↓
Select exercises → Follow the integrated component progression (Pattern 3)
```
