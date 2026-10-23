import sqlite3
import json

DB_FILE = "hobby_app.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
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
    conn.commit()
    conn.close()

init_db()

def save_questionnaire(response_id, answers, recommendations):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO QUESTIONNAIRE_RESPONSES (
                RESPONSE_ID,
                QUESTION_1,
                QUESTION_2,
                QUESTION_3,
                QUESTION_4,
                QUESTION_5,
                RECOMMENDATIONS
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
        connection.commit()
    finally:
        connection.close()

def get_completed_lessons(session_id, hobby_name, skill):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT DISTINCT LESSON INDEX
            FROM LESSON_PROGRESS
            WHERE SESSION_ID = ? 
            AND HOBBY_NAME = ? 
            AND SKILL = ?
            AND COMPLETED = 1
            ORDER BY LESSON_INDEX
            """,
            (session_id, hobby_name, skill)
        )
        return [row[0] for row in cursor.fetchall()]
    finally:
        connection.close()

def save_lesson_progress(
    session_id,
    hobby_name,
    skill,
    lesson_index,
    reading_finished,
    video_finished
):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO LESSON_PROGRESS (
                SESSION_ID,
                HOBBY_NAME,
                SKILL,
                LESSON_INDEX,
                READING_FINISHED,
                VIDEO_FINISHED,
                COMPLETED
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, 1, CURRENT_TIMESTAMP)
            ON CONFLICT(SESSION_ID, HOBBY_NAME, SKILL_LEVEL, LESSON_INDEX) 
            DO UPDATE SET
                READING_FINISHED = READING_FINISHED OR excluded.READING_FINISHED,
                VIDEO_FINISHED = VIDEO_FINISHED OR excluded.VIDEO_FINISHED,
                COMPLETED = 1,
                UPDATED_AT = CURRENT_TIMESTAMP
            """,
            (
                session_id,
                hobby_name,
                skill,
                lesson_index,
                1 if reading_finished else 0,
                1 if video_finished else 0,
            )
        )
        connection.commit()
    finally:
        connection.close()