#!/usr/bin/env python3
"""
Import Apple Health export.xml into fitness-advisor's body-log.json and workout-log.json.

Usage:
  python scripts/import_apple_health.py export.zip
  python scripts/import_apple_health.py export.xml

The script:
  1. If .zip, extracts export.xml from apple_health_export/export.xml
  2. Parses XML for HKQuantityTypeIdentifier records
  3. Maps to body-log.json schema
  4. Parses HKWorkout records → workout-log.json
  5. Merges with existing data (dedup by date)
"""
import json
import os
import sys
import xml.etree.ElementTree as ET
import zipfile
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BODY_LOG = PROJECT_ROOT / "assets" / "user-data" / "body-log.json"
WORKOUT_LOG = PROJECT_ROOT / "assets" / "user-data" / "workout-log.json"
IMPORTS_DIR = PROJECT_ROOT / "assets" / "user-data" / "imports"

# HealthKit type → body-log field mapping
BODY_TYPE_MAP = {
    "HKQuantityTypeIdentifierBodyMass": "weight_kg",
    "HKQuantityTypeIdentifierBodyFatPercentage": "body_fat_pct",
    "HKQuantityTypeIdentifierBodyMassIndex": "bmi",
    "HKQuantityTypeIdentifierWaistCircumference": "waist_cm",
    "HKQuantityTypeIdentifierHeight": None,  # handled separately → profile
    "HKQuantityTypeIdentifierRestingHeartRate": "resting_hr",
    "HKQuantityTypeIdentifierBloodPressureSystolic": "systolic_bp",
    "HKQuantityTypeIdentifierBloodPressureDiastolic": "diastolic_bp",
}


def extract_xml(input_path):
    """Get export.xml from zip or direct file."""
    path = Path(input_path)
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as zf:
            # Try common paths for export.xml
            candidates = [
                "apple_health_export/export.xml",
                "export.xml",
            ]
            for c in candidates:
                try:
                    data = zf.read(c)
                    print(f"  Extracted: {c} ({len(data):,} bytes)")
                    return data.decode("utf-8")
                except KeyError:
                    continue
        print("ERROR: Could not find export.xml in zip", file=sys.stderr)
        sys.exit(1)
    else:
        return path.read_text(encoding="utf-8")


def parse_records(xml_text):
    """Parse HealthKit records from XML, grouped by date."""
    print("  Parsing XML...")
    root = ET.fromstring(xml_text)

    daily = {}  # date → {field: value}
    workout_records = []

    for record in root.iter("Record"):
        rtype = record.get("type", "")
        if rtype in BODY_TYPE_MAP:
            field = BODY_TYPE_MAP[rtype]
            if field is None:
                continue
            date_str = record.get("startDate", "")[:10]  # YYYY-MM-DD
            value = record.get("value", "")
            unit = record.get("unit", "")

            if not value:
                continue
            try:
                val = float(value)
            except ValueError:
                continue

            # Unit conversions → our schema units
            if unit == "lb":
                val = val * 0.453592  # lb → kg
            elif unit == "oz":
                val = val * 0.0283495
            elif unit == "st":
                val = val * 6.35029
            elif unit == "mmHg" or unit == "bpm" or unit == "cm" or unit == "kg" or unit == "%" or unit == "count":
                pass  # already in correct units
            else:
                pass

            if date_str not in daily:
                daily[date_str] = {}
            daily[date_str][field] = round(val, 1)
            daily[date_str]["source"] = "apple-health"

    for workout in root.iter("Workout"):
        wtype = workout.get("workoutActivityType", "")
        duration_str = workout.get("duration", "0")
        start = workout.get("startDate", "")
        end = workout.get("endDate", "")
        duration_min = round(float(duration_str) / 60, 0) if duration_str else 0

        # Map Apple workout type to our type
        type_map = {
            "HKWorkoutActivityTypeTraditionalStrengthTraining": "strength",
            "HKWorkoutActivityTypeRunning": "cardio",
            "HKWorkoutActivityTypeCycling": "cardio",
            "HKWorkoutActivityTypeSwimming": "cardio",
            "HKWorkoutActivityTypeWalking": "cardio",
            "HKWorkoutActivityTypeHighIntensityIntervalTraining": "hiit",
            "HKWorkoutActivityTypeFlexibility": "flexibility",
            "HKWorkoutActivityTypeYoga": "flexibility",
        }

        workout_records.append({
            "date": start[:10] if start else "",
            "start_time": start[11:16] if len(start) > 16 else "",
            "end_time": end[11:16] if len(end) > 16 else "",
            "duration_min": duration_min,
            "source": "apple-health",
            "type": type_map.get(wtype, "other"),
            "focus": wtype.replace("HKWorkoutActivityType", ""),
            "rpe_session": None,
            "notes": f"Apple Watch 自动记录 [{wtype}]",
            "exercises": []
        })

    print(f"  Found {len(daily)} days with body data, {len(workout_records)} workouts")
    return daily, workout_records


def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def merge_body_log(existing, daily_data):
    """Merge new daily data into existing body-log, dedup by date."""
    entries = existing.get("entries", []) if existing else []
    existing_dates = {e["date"] for e in entries}

    for date_str in sorted(daily_data.keys()):
        if date_str in existing_dates:
            # Update existing entry
            for e in entries:
                if e["date"] == date_str:
                    for field, val in daily_data[date_str].items():
                        if val is not None:
                            e[field] = val
                    break
        else:
            entry = {"date": date_str,
                     "source": "apple-health",
                     "weight_kg": None, "body_fat_pct": None, "bmi": None,
                     "waist_cm": None, "hip_cm": None,
                     "chest_cm": None, "arm_cm": None, "thigh_cm": None, "calf_cm": None, "neck_cm": None,
                     "resting_hr": None, "systolic_bp": None, "diastolic_bp": None,
                     "notes": ""}
            entry.update(daily_data[date_str])
            entries.append(entry)

    # Sort by date
    entries.sort(key=lambda e: e["date"])
    existing["entries"] = entries
    return existing


def merge_workout_log(existing, workout_records):
    """Merge workout records, dedup by date+type."""
    sessions = existing.get("sessions", []) if existing else []

    for w in workout_records:
        # Simple dedup: if same date and type exists, skip
        exists = any(s["date"] == w["date"] and s.get("type") == w.get("type") for s in sessions)
        if not exists:
            sessions.append(w)

    sessions.sort(key=lambda s: s["date"], reverse=True)
    existing["sessions"] = sessions
    return existing


def main():
    if len(sys.argv) < 2:
        print("Usage: python import_apple_health.py <export.zip|export.xml>")
        sys.exit(1)

    input_path = sys.argv[1]
    print(f"Importing Apple Health data from: {input_path}")

    # Step 1: Extract
    xml_text = extract_xml(input_path)

    # Step 2: Parse
    daily_data, workout_records = parse_records(xml_text)

    # Step 3: Save import file for archive
    IMPORTS_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = IMPORTS_DIR / f"apple-health-{datetime.now().strftime('%Y%m%d')}.xml"
    archive_path.write_text(xml_text, encoding="utf-8")
    print(f"  Archived: {archive_path}")

    # Step 4: Merge into body-log
    body_log = load_json(BODY_LOG) or {"_description": "", "_source_options": "", "_fields": {}, "entries": []}
    body_log = merge_body_log(body_log, daily_data)
    save_json(BODY_LOG, body_log)
    print(f"  Body log: {len(body_log['entries'])} entries → {BODY_LOG}")

    # Step 5: Merge into workout-log
    workout_log_data = load_json(WORKOUT_LOG) or {"_description": "", "_source_options": "", "_fields": {}, "sessions": []}
    workout_log_data = merge_workout_log(workout_log_data, workout_records)
    save_json(WORKOUT_LOG, workout_log_data)
    print(f"  Workout log: {len(workout_log_data['sessions'])} sessions → {WORKOUT_LOG}")

    print("\nImport complete!")


if __name__ == "__main__":
    main()
