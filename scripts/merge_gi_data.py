"""Merge GI data into food-database.json with fuzzy name matching."""
import json

FOOD_DB = r"D:\04_claude_code\01_Fitness\fitness-advisor\assets\food-database.json"
GI_FILE = r"D:\04_claude_code\01_Fitness\fitness-advisor\temp_gi.json"

# Load GI data
with open(GI_FILE, "r", encoding="utf-8") as f:
    gi_groups = json.load(f)

# Build flat GI lookup: cleaned_name -> GI
gi_lookup = {}
for group in gi_groups:
    for item in group["list"]:
        name = item["foodName"].strip()
        # Clean: remove * prefix, normalize whitespace
        name_clean = name.lstrip("* ").strip()
        gi_lookup[name_clean] = {
            "gi": item["GI"],
            "group": group["foodGroup"],
            "original_name": name
        }

print(f"GI entries loaded: {len(gi_lookup)}")

# Load food database
with open(FOOD_DB, "r", encoding="utf-8") as f:
    db = json.load(f)

foods = db["foods"]
print(f"Food database size: {len(foods)}")

# Matching strategies
def clean(s):
    """Clean a food name for matching."""
    s = s.strip()
    # Remove parenthetical annotations that don't affect matching
    # e.g. "鸡（代表值）" -> "鸡" but keep "鸡（土鸡，家养）"
    return s

def match_gi(food_name):
    """Try to match a food name to GI data. Returns (gi_value, gi_group, match_type) or None."""
    fn = food_name.strip()

    # Strategy 1: Exact match after cleaning
    for gi_name, gi_data in gi_lookup.items():
        if fn == gi_name:
            return gi_data["gi"], gi_data["group"], "exact"

    # Strategy 2: GI name contained in food name
    for gi_name, gi_data in gi_lookup.items():
        if gi_name in fn or fn in gi_name:
            return gi_data["gi"], gi_data["group"], "substring"

    # Strategy 3: Core name match (remove everything after first bracket/parenthesis)
    fn_core = fn.split("（")[0].split("(")[0].strip()
    for gi_name, gi_data in gi_lookup.items():
        gi_core = gi_name.split("（")[0].split("(")[0].strip()
        if fn_core == gi_core and fn_core:
            return gi_data["gi"], gi_data["group"], "core_name"

    # Strategy 4: GI name contains food core name or vice versa
    for gi_name, gi_data in gi_lookup.items():
        gi_core = gi_name.split("（")[0].split("(")[0].strip()
        if len(fn_core) >= 2 and len(gi_core) >= 2:
            if fn_core in gi_core or gi_core in fn_core:
                return gi_data["gi"], gi_data["group"], "partial"

    return None

# Run matching
matched = 0
match_types = {"exact": 0, "substring": 0, "core_name": 0, "partial": 0}
unmatched_samples = []

for food in foods:
    name = food.get("name_zh", "")
    if not name:
        continue
    result = match_gi(name)
    if result:
        gi_val, gi_group, mtype = result
        food["gi"] = gi_val
        food["gi_group"] = gi_group
        matched += 1
        match_types[mtype] += 1
    else:
        food["gi"] = None
        food.pop("gi_group", None)
        if len(unmatched_samples) < 20:
            unmatched_samples.append(name)

print(f"\nMatching results:")
print(f"  Total foods: {len(foods)}")
print(f"  Matched: {matched} ({100*matched/len(foods):.1f}%)")
for t, c in match_types.items():
    print(f"    {t}: {c}")
print(f"  Unmatched: {len(foods) - matched}")

print(f"\nSample unmatched foods:")
for name in unmatched_samples[:15]:
    print(f"  - {name}")

# Write updated database
with open(FOOD_DB, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

import os
print(f"\nWritten: {FOOD_DB}")
print(f"Size: {os.path.getsize(FOOD_DB) / 1024:.0f} KB")
