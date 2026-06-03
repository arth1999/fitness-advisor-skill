"""Migrate JSON user data into SQLite database.

Usage:
    python scripts/db_migrate.py                # migrate all JSON data
    python scripts/db_migrate.py --dry-run       # preview without writing
    python scripts/db_migrate.py --profile-only  # only migrate profile
"""

import sqlite3
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(SCRIPT_DIR, "..")
USER_DATA = os.path.join(PROJECT_DIR, "assets", "user-data")
DB_PATH = os.path.join(USER_DATA, "fitness.db")


def load_json(filename: str) -> dict | None:
    path = os.path.join(USER_DATA, filename)
    if not os.path.exists(path):
        print(f"  [skip] {filename} not found")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def migrate_profile(conn: sqlite3.Connection, dry: bool = False):
    data = load_json("profile.json")
    if not data:
        return
    fields = {k: v for k, v in data.items() if not k.startswith("_")}
    if isinstance(fields.get("goals"), list):
        fields["goals"] = json.dumps(fields["goals"], ensure_ascii=False)
    if isinstance(fields.get("injuries"), list):
        fields["injuries"] = json.dumps(fields["injuries"], ensure_ascii=False)
    if isinstance(fields.get("medical_conditions"), list):
        fields["medical_conditions"] = json.dumps(fields["medical_conditions"], ensure_ascii=False)

    columns = list(fields.keys())
    placeholders = [f":{c}" for c in columns]
    sql = f"INSERT OR REPLACE INTO profile ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"

    if dry:
        print(f"  [dry] INSERT profile: {fields}")
    else:
        conn.execute(sql, fields)
        print(f"  [ok] profile migrated")


def migrate_body_log(conn: sqlite3.Connection, dry: bool = False):
    data = load_json("body-log.json")
    if not data:
        return
    entries = data.get("entries", [])
    count = 0
    for entry in entries:
        fields = {k: v for k, v in entry.items() if k in [
            "date", "source", "weight_kg", "body_fat_pct", "bmi",
            "waist_cm", "hip_cm", "chest_cm", "arm_cm", "thigh_cm",
            "calf_cm", "neck_cm", "resting_hr", "systolic_bp",
            "diastolic_bp", "notes"
        ]}
        if not dry:
            conn.execute(
                "INSERT OR IGNORE INTO body_log (date, source, weight_kg, "
                "body_fat_pct, bmi, waist_cm, hip_cm, chest_cm, arm_cm, "
                "thigh_cm, calf_cm, neck_cm, resting_hr, systolic_bp, "
                "diastolic_bp, notes) VALUES (:date, :source, :weight_kg, "
                ":body_fat_pct, :bmi, :waist_cm, :hip_cm, :chest_cm, :arm_cm, "
                ":thigh_cm, :calf_cm, :neck_cm, :resting_hr, :systolic_bp, "
                ":diastolic_bp, :notes)",
                fields
            )
        count += 1
    print(f"  {'[dry]' if dry else '[ok]'} body_log: {count} entries")


def migrate_workouts(conn: sqlite3.Connection, dry: bool = False):
    data = load_json("workout-log.json")
    if not data:
        return
    sessions = data.get("sessions", [])
    session_count = 0
    set_count = 0
    for session in sessions:
        s_fields = {k: v for k, v in session.items() if k in [
            "date", "start_time", "end_time", "duration_min",
            "source", "type", "focus", "rpe_session", "notes"
        ]}
        if dry:
            session_count += 1
            set_count += len(session.get("exercises", []))
        else:
            cur = conn.execute(
                "INSERT INTO workout_sessions (date, start_time, end_time, "
                "duration_min, source, type, focus, rpe_session, notes) "
                "VALUES (:date, :start_time, :end_time, :duration_min, "
                ":source, :type, :focus, :rpe_session, :notes)",
                s_fields
            )
            sid = cur.lastrowid
            session_count += 1
            for ex in session.get("exercises", []):
                for s in ex.get("sets", []):
                    conn.execute(
                        "INSERT INTO workout_sets (session_id, exercise_name, "
                        "exercise_id, set_number, weight_kg, reps, rpe, rir) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (sid, ex.get("exercise_name", ""),
                         ex.get("exercise_id", ""), s.get("set"),
                         s.get("weight_kg"), s.get("reps"),
                         s.get("rpe"), s.get("rir"))
                    )
                    set_count += 1
    print(f"  {'[dry]' if dry else '[ok]'} workouts: {session_count} sessions, {set_count} sets")


def main():
    dry = "--dry-run" in sys.argv
    profile_only = "--profile-only" in sys.argv

    print(f"Migrating JSON -> SQLite {'(dry run)' if dry else ''}")
    print(f"  DB: {DB_PATH}")

    conn = None if dry else sqlite3.connect(DB_PATH)

    try:
        migrate_profile(conn, dry)
        if not profile_only:
            migrate_body_log(conn, dry)
            migrate_workouts(conn, dry)

        if not dry:
            conn.commit()
            print("Migration complete.")
        else:
            print("Dry run complete. Run without --dry-run to write.")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
