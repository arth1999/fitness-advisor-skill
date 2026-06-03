"""Initialize SQLite database for fitness-advisor user data.

Creates tables: profile, body_log, workout_sessions, workout_sets.
Run once: python scripts/db_init.py
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "user-data", "fitness.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS profile (
    id INTEGER PRIMARY KEY DEFAULT 1,
    name TEXT,
    birth_date TEXT,
    sex TEXT,
    height_cm REAL,
    goals TEXT,
    training_level TEXT,
    injuries TEXT,
    medical_conditions TEXT,
    created_at TEXT DEFAULT (datetime('now','localtime')),
    updated_at TEXT DEFAULT (datetime('now','localtime'))
);

CREATE TABLE IF NOT EXISTS body_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    source TEXT DEFAULT 'manual',
    weight_kg REAL,
    body_fat_pct REAL,
    bmi REAL,
    waist_cm REAL,
    hip_cm REAL,
    chest_cm REAL,
    arm_cm REAL,
    thigh_cm REAL,
    calf_cm REAL,
    neck_cm REAL,
    resting_hr REAL,
    systolic_bp REAL,
    diastolic_bp REAL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS workout_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    start_time TEXT,
    end_time TEXT,
    duration_min INTEGER,
    source TEXT DEFAULT 'manual',
    type TEXT,
    focus TEXT,
    rpe_session REAL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS workout_sets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    exercise_name TEXT NOT NULL,
    exercise_id TEXT,
    set_number INTEGER,
    weight_kg REAL,
    reps INTEGER,
    rpe REAL,
    rir REAL,
    FOREIGN KEY (session_id) REFERENCES workout_sessions(id)
);

CREATE INDEX IF NOT EXISTS idx_body_log_date ON body_log(date);
CREATE INDEX IF NOT EXISTS idx_workout_sessions_date ON workout_sessions(date);
CREATE INDEX IF NOT EXISTS idx_workout_sets_session ON workout_sets(session_id);
"""


def init_db(db_path: str = None) -> str:
    """Create database and tables. Returns path to the created db."""
    path = db_path or DB_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()
    return path


if __name__ == "__main__":
    path = init_db()
    print(f"Database initialized: {path}")
    print("Tables created: profile, body_log, workout_sessions, workout_sets")
