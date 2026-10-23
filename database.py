import sqlite3
import json
from pathlib import Path


# Local SQLite database file
DB_FILE = Path(__file__).resolve().parent / "hobby_app.db"


def get_connection():
    conn = sqlite3.connect(DB_FILE, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:

        # Store questionnaire answers
        conn.execute("""
            CREATE TABLE IF NOT EXISTS questionnaire_responses (
                response_id TEXT PRIMARY KEY,
                question_1 TEXT,
                question_2 TEXT,
                question_3 TEXT,
                question_4 TEXT,
                question_5 TEXT,
                recommendations TEXT
            )
        """)

        # Store completed lessons
        conn.execute("""
            CREATE TABLE IF NOT EXISTS lesson_progress (
                session_id TEXT NOT NULL,
                hobby_name TEXT NOT NULL,
                skill_level TEXT NOT NULL,
                lesson_number INTEGER NOT NULL,
                reading_finished INTEGER DEFAULT 0,
                video_finished INTEGER DEFAULT 0,
                completed INTEGER DEFAULT 0,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

                PRIMARY KEY (
                    session_id,
                    hobby_name,
                    skill_level,
                    lesson_number
                )
            )
        """)



def save_questionnaire(
    response_id,
    answers,
    recommendations
):
    if len(answers) != 5:
        raise ValueError("Exactly five answers are required")

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO questionnaire_responses (
                response_id,
                question_1,
                question_2,
                question_3,
                question_4,
                question_5,
                recommendations
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                response_id,
                answers[0],
                answers[1],
                answers[2],
                answers[3],
                answers[4],
                json.dumps(recommendations)
            )
        )



def get_completed_lessons(
    session_id,
    hobby_name,
    skill
):
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT DISTINCT lesson_number
            FROM lesson_progress
            WHERE session_id = ?
              AND hobby_name = ?
              AND skill_level = ?
              AND completed = 1
            ORDER BY lesson_number
            """,
            (
                session_id,
                hobby_name,
                skill
            )
        ).fetchall()

    return [row["lesson_number"] for row in rows]


def save_lesson_progress(
    session_id,
    hobby_name,
    skill,
    lesson_number,
    reading_finished,
    video_finished
):
    if not 1 <= lesson_number <= 10:
        raise ValueError("Lesson number must be between 1 and 10")

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO lesson_progress (
                session_id,
                hobby_name,
                skill_level,
                lesson_number,
                reading_finished,
                video_finished,
                completed
            )
            VALUES (?, ?, ?, ?, ?, ?, 1)

            ON CONFLICT (
                session_id,
                hobby_name,
                skill_level,
                lesson_number
            )
            DO UPDATE SET
                reading_finished = MAX(
                    lesson_progress.reading_finished,
                    excluded.reading_finished
                ),
                video_finished = MAX(
                    lesson_progress.video_finished,
                    excluded.video_finished
                ),
                completed = 1,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                session_id,
                hobby_name,
                skill,
                lesson_number,
                int(reading_finished),
                int(video_finished)
            )
        )



init_db()
