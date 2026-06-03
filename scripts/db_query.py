"""Common queries for fitness user data in SQLite.

Can be imported or run standalone for quick reports.

Usage:
    python scripts/db_query.py trend --days 90          # weight/bf trend
    python scripts/db_query.py latest                    # latest measurements
    python scripts/db_query.py training --weeks 4        # training summary
    python scripts/db_query.py progress --exercise 杠铃卧推  # strength progress
"""

import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "user-data", "fitness.db")


def get_conn():
    if not os.path.exists(DB_PATH):
        print(f"Database not found: {DB_PATH}")
        print("Run: python scripts/db_init.py")
        sys.exit(1)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def latest():
    """Get the most recent body measurement."""
    conn = get_conn()
    row = conn.execute("SELECT * FROM body_log ORDER BY date DESC LIMIT 1").fetchone()
    conn.close()
    if not row:
        print("No body data yet.")
        return None
    return dict(row)


def trend(days: int = 90):
    """Get weight and body fat trend over N days."""
    conn = get_conn()
    rows = conn.execute(
        "SELECT date, weight_kg, body_fat_pct, waist_cm "
        "FROM body_log WHERE date >= date('now', ?) "
        "ORDER BY date ASC",
        (f"-{days} days",)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def weight_stats(days: int = 30):
    """Get weight min/max/avg/change over N days."""
    conn = get_conn()
    row = conn.execute(
        "SELECT MIN(weight_kg) as min_kg, MAX(weight_kg) as max_kg, "
        "ROUND(AVG(weight_kg), 1) as avg_kg, "
        "ROUND(MAX(weight_kg) - MIN(weight_kg), 1) as change_kg, "
        "COUNT(*) as measurements "
        "FROM body_log WHERE date >= date('now', ?) AND weight_kg IS NOT NULL",
        (f"-{days} days",)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def training_summary(weeks: int = 4):
    """Training sessions count, volume, frequency over N weeks."""
    conn = get_conn()
    sessions = conn.execute(
        "SELECT COUNT(*) as count FROM workout_sessions "
        "WHERE date >= date('now', ?)",
        (f"-{weeks * 7} days",)
    ).fetchone()

    total_sets = conn.execute(
        "SELECT COUNT(*) as count FROM workout_sets ws "
        "JOIN workout_sessions s ON ws.session_id = s.id "
        "WHERE s.date >= date('now', ?)",
        (f"-{weeks * 7} days",)
    ).fetchone()

    by_type = conn.execute(
        "SELECT type, COUNT(*) as count FROM workout_sessions "
        "WHERE date >= date('now', ?) GROUP BY type",
        (f"-{weeks * 7} days",)
    ).fetchall()

    conn.close()
    return {
        "weeks": weeks,
        "sessions": sessions["count"],
        "avg_per_week": round(sessions["count"] / weeks, 1),
        "total_sets": total_sets["count"],
        "by_type": {r["type"]: r["count"] for r in by_type}
    }


def exercise_progress(exercise: str, days: int = 90):
    """Track strength progress for a specific exercise (e1RM)."""
    conn = get_conn()
    rows = conn.execute(
        "SELECT s.date, ws.set_number, ws.weight_kg, ws.reps, ws.rpe "
        "FROM workout_sets ws "
        "JOIN workout_sessions s ON ws.session_id = s.id "
        "WHERE ws.exercise_name LIKE ? AND s.date >= date('now', ?) "
        "ORDER BY s.date ASC, ws.set_number",
        (f"%{exercise}%", f"-{days} days")
    ).fetchall()
    conn.close()

    results = []
    for r in rows:
        d = dict(r)
        if d["weight_kg"] and d["reps"]:
            d["e1rm"] = round(d["weight_kg"] * (1 + d["reps"] / 30), 1)
        results.append(d)
    return results


def print_trend(days: int = 90):
    rows = trend(days)
    if not rows:
        print("No data.")
        return
    print(f"\nBody Trend (last {days} days)\n{'-'*50}")
    print(f"{'Date':<12} {'Weight':>8} {'BF%':>8} {'Waist':>8}")
    for r in rows:
        print(f"{r['date']:<12} {str(r['weight_kg'] or '-'):>8} "
              f"{str(r['body_fat_pct'] or '-'):>8} {str(r['waist_cm'] or '-'):>8}")


def print_training(weeks: int = 4):
    s = training_summary(weeks)
    print(f"\nTraining Summary (last {s['weeks']} weeks)\n{'-'*40}")
    for k, v in s.items():
        print(f"  {k}: {v}")


def print_progress(exercise: str, days: int = 90):
    rows = exercise_progress(exercise, days)
    if not rows:
        print(f"No data for: {exercise}")
        return
    print(f"\nProgress: {exercise} (last {days} days)\n{'-'*50}")
    print(f"{'Date':<12} {'Set':>4} {'kg':>6} {'Reps':>5} {'e1RM':>7}")
    for r in rows:
        print(f"{r['date']:<12} {r['set_number']:>4} "
              f"{str(r['weight_kg'] or '-'):>6} {str(r['reps'] or '-'):>5} "
              f"{str(r.get('e1rm', '-')):>7}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "latest":
        d = latest()
        if d:
            for k, v in d.items():
                if v is not None:
                    print(f"  {k}: {v}")

    elif cmd == "trend":
        days = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].startswith("--") else 90
        # parse --days N
        for i, a in enumerate(sys.argv):
            if a == "--days" and i + 1 < len(sys.argv):
                days = int(sys.argv[i + 1])
        print_trend(days)

    elif cmd == "training":
        weeks = 4
        for i, a in enumerate(sys.argv):
            if a == "--weeks" and i + 1 < len(sys.argv):
                weeks = int(sys.argv[i + 1])
        print_training(weeks)

    elif cmd == "progress":
        if len(sys.argv) < 3:
            print("Usage: python db_query.py progress --exercise <name> [--days N]")
            sys.exit(1)
        ex = sys.argv[-1]
        days = 90
        for i, a in enumerate(sys.argv):
            if a == "--days" and i + 1 < len(sys.argv):
                days = int(sys.argv[i + 1])
        print_progress(ex, days)

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
