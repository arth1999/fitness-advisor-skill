#!/usr/bin/env python3
"""
Import workout data from CSV/Excel into workout-log.json.
Supports exports from 训记, Strong, Hevy, and generic CSV formats.

Usage:
  python scripts/import_csv_workout.py <file.csv> [--format xunji|strong|hevy|generic]
  python scripts/import_csv_workout.py <file.csv> --interactive  (field-by-field mapping)

Generic CSV expected columns (order doesn't matter, auto-detected):
  date, exercise, set, weight_kg, reps, rpe, duration_min, notes
"""
import csv
import json
import os
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
WORKOUT_LOG = PROJECT_ROOT / "assets" / "user-data" / "workout-log.json"
IMPORTS_DIR = PROJECT_ROOT / "assets" / "user-data" / "imports"

# Known app formats
FORMAT_COLUMNS = {
    "xunji": {  # 训记 typical export
        "date": ["日期", "date", "训练日期"],
        "exercise": ["动作", "exercise", "训练动作"],
        "set": ["组", "set", "组数"],
        "weight_kg": ["重量kg", "weight", "重量"],
        "reps": ["次数", "reps", "重复"],
        "notes": ["备注", "note", "notes"],
    },
    "strong": {
        "date": ["Date"],
        "exercise": ["Exercise Name"],
        "set": ["Set Order"],
        "weight_kg": ["Weight (kg)"],
        "reps": ["Reps"],
        "rpe": ["RPE"],
        "notes": ["Notes"],
    },
    "hevy": {
        "date": ["start_time", "date"],
        "exercise": ["exercise_name", "exercise_title"],
        "set": ["set_index", "set_order"],
        "weight_kg": ["weight_kg"],
        "reps": ["reps"],
        "rpe": ["rpe"],
        "notes": ["notes", "note"],
    },
}


def detect_format(headers):
    """Detect CSV format by matching headers."""
    scores = {}
    for fmt, mapping in FORMAT_COLUMNS.items():
        score = 0
        for field, candidates in mapping.items():
            for h in headers:
                if h in candidates:
                    score += 1
                    break
        scores[fmt] = score
    best = max(scores, key=scores.get)
    if scores[best] >= 3:
        return best
    return "generic"


def column_mapping(headers, fmt):
    """Build column index → field mapping."""
    if fmt == "generic":
        # Auto-detect by common names
        mapping = {}
        for i, h in enumerate(headers):
            h_lower = h.lower().strip()
            if any(k in h_lower for k in ["date", "日期"]):
                mapping["date"] = i
            elif any(k in h_lower for k in ["exercise", "动作"]):
                mapping["exercise"] = i
            elif any(k in h_lower for k in ["set", "组"]):
                mapping["set"] = i
            elif any(k in h_lower for k in ["weight", "重量"]):
                mapping["weight_kg"] = i
            elif any(k in h_lower for k in ["rep", "次数"]):
                mapping["reps"] = i
            elif any(k in h_lower for k in ["rpe", "感知"]):
                mapping["rpe"] = i
            elif any(k in h_lower for k in ["rir"]):
                mapping["rir"] = i
            elif any(k in h_lower for k in ["duration", "时长", "时间"]):
                mapping["duration_min"] = i
            elif any(k in h_lower for k in ["note", "备注", "备注"]):
                mapping["notes"] = i
        return mapping
    else:
        config = FORMAT_COLUMNS[fmt]
        mapping = {}
        for field, candidates in config.items():
            for i, h in enumerate(headers):
                if h in candidates:
                    mapping[field] = i
                    break
        return mapping


def safe_float(val):
    try:
        return round(float(val), 1)
    except (ValueError, TypeError):
        return None


def safe_int(val):
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return None


def parse_csv(filepath):
    """Parse CSV into grouped workout sessions."""
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        headers = next(reader, [])

    fmt = detect_format(headers)
    print(f"  Detected format: {fmt}")
    mapping = column_mapping(headers, fmt)

    print(f"  Columns mapped: {list(mapping.keys())}")

    # Read all rows, group by date
    sessions = {}  # date_key → exercises dict
    rows = []
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    for row in rows:
        date_key = row.get(headers[mapping["date"]], "") if "date" in mapping else ""
        if not date_key:
            date_key = "unknown"
        # Normalize date
        date_key = date_key.strip()[:10]

        ex_name = row.get(headers[mapping["exercise"]], "") if "exercise" in mapping else "Unknown"
        if not ex_name:
            continue

        if date_key not in sessions:
            sessions[date_key] = {"date": date_key, "source": f"csv-import-{fmt}", "exercises": {}}

        if ex_name not in sessions[date_key]["exercises"]:
            sessions[date_key]["exercises"][ex_name] = []

        set_data = {"set": len(sessions[date_key]["exercises"][ex_name]) + 1}
        if "weight_kg" in mapping:
            set_data["weight_kg"] = safe_float(row.get(headers[mapping["weight_kg"]]))
        if "reps" in mapping:
            set_data["reps"] = safe_int(row.get(headers[mapping["reps"]]))
        if "rpe" in mapping:
            set_data["rpe"] = safe_float(row.get(headers[mapping["rpe"]]))
        if "rir" in mapping:
            set_data["rir"] = safe_int(row.get(headers[mapping["rir"]]))
        if "set" in mapping:
            set_data["set"] = safe_int(row.get(headers[mapping["set"]])) or set_data["set"]

        sessions[date_key]["exercises"][ex_name].append(set_data)

    # Convert to workout-log format
    result = []
    for date_key, session in sorted(sessions.items()):
        exercises = []
        for ex_name, sets in session["exercises"].items():
            exercises.append({
                "exercise_id": "",
                "exercise_name": ex_name,
                "sets": sorted(sets, key=lambda s: s.get("set", 0))
            })
        result.append({
            "date": date_key,
            "start_time": "",
            "end_time": "",
            "duration_min": None,
            "source": f"csv-import-{fmt}",
            "type": "strength",
            "focus": ", ".join(list(session["exercises"].keys())[:3]),
            "rpe_session": None,
            "notes": f"从 {fmt} CSV 导入",
            "exercises": exercises
        })

    return result, fmt


def main():
    if len(sys.argv) < 2:
        print("Usage: python import_csv_workout.py <file.csv> [--format xunji|strong|hevy|generic]")
        sys.exit(1)

    filepath = sys.argv[1]
    fmt_override = None
    if "--format" in sys.argv:
        idx = sys.argv.index("--format")
        fmt_override = sys.argv[idx + 1]

    print(f"Importing workout CSV: {filepath}")

    # Parse
    sessions, detected_fmt = parse_csv(filepath)
    fmt = fmt_override or detected_fmt
    print(f"  Parsed {len(sessions)} sessions")

    # Save archive
    IMPORTS_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = IMPORTS_DIR / f"csv-import-{fmt}-{datetime.now().strftime('%Y%m%d')}.csv"
    import shutil
    shutil.copy(filepath, archive_path)
    print(f"  Archived: {archive_path}")

    # Load existing
    if os.path.exists(WORKOUT_LOG):
        with open(WORKOUT_LOG, "r", encoding="utf-8") as f:
            log = json.load(f)
    else:
        log = {"sessions": []}

    # Merge (dedup by date)
    existing_dates = {(s["date"], s.get("source", "")) for s in log["sessions"]}
    new_count = 0
    for s in sessions:
        key = (s["date"], s["source"])
        if key not in existing_dates:
            log["sessions"].append(s)
            existing_dates.add(key)
            new_count += 1

    log["sessions"].sort(key=lambda s: s["date"], reverse=True)

    # Save
    with open(WORKOUT_LOG, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

    print(f"  Added {new_count} new sessions (skipped {len(sessions) - new_count} duplicates)")
    print(f"  Workout log: {len(log['sessions'])} total sessions")
    print(f"\nImport complete!")


if __name__ == "__main__":
    main()
