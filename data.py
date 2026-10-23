import os
import json
import snowflake.connector


def connect_to_snowflake():
    return snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        database="HOBBY_APP",
        schema="PUBLIC",
        autocommit=False
    )


def save_questionnaire(response_id, answers, recommendations):
    connection = connect_to_snowflake()

    try:
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO QUESTIONNAIRE_RESPONSES (
                    RESPONSE_ID,
                    QUESTION_1,
                    QUESTION_2,
                    QUESTION_3,
                    QUESTION_4,
                    QUESTION_5,
                    RECOMMENDATIONS
                )
                SELECT
                    %s, %s, %s, %s, %s, %s,
                    PARSE_JSON(%s)
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
            cursor.close()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def get_completed_lessons(session_id, hobby_name, skill):
    connection = connect_to_snowflake()

    try:
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT DISTINCT LESSON_INDEX
                FROM LESSON_PROGRESS
                WHERE SESSION_ID = %s
                  AND HOBBY_NAME = %s
                  AND SKILL_LEVEL = %s
                  AND COMPLETED = TRUE
                ORDER BY LESSON_INDEX
                """,
                (session_id, hobby_name, skill)
            )

            return [row[0] for row in cursor.fetchall()]

        finally:
            cursor.close()

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
    connection = connect_to_snowflake()

    try:
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                MERGE INTO LESSON_PROGRESS AS target
                USING (
                    SELECT
                        %s AS SESSION_ID,
                        %s AS HOBBY_NAME,
                        %s AS SKILL_LEVEL,
                        %s AS LESSON_INDEX
                ) AS source

                ON target.SESSION_ID = source.SESSION_ID
                   AND target.HOBBY_NAME = source.HOBBY_NAME
                   AND target.SKILL_LEVEL = source.SKILL_LEVEL
                   AND target.LESSON_INDEX = source.LESSON_INDEX

                WHEN MATCHED THEN
                    UPDATE SET
                        READING_FINISHED =
                            target.READING_FINISHED
                            OR %s,
                        VIDEO_FINISHED =
                            target.VIDEO_FINISHED
                            OR %s,
                        COMPLETED = TRUE,
                        UPDATED_AT = CURRENT_TIMESTAMP()

                WHEN NOT MATCHED THEN
                    INSERT (
                        SESSION_ID,
                        HOBBY_NAME,
                        SKILL_LEVEL,
                        LESSON_INDEX,
                        READING_FINISHED,
                        VIDEO_FINISHED,
                        COMPLETED
                    )
                    VALUES (
                        source.SESSION_ID,
                        source.HOBBY_NAME,
                        source.SKILL_LEVEL,
                        source.LESSON_INDEX,
                        %s,
                        %s,
                        TRUE
                    )
                """,
                (
                    session_id,
                    hobby_name,
                    skill,
                    lesson_index,
                    reading_finished,
                    video_finished,
                    reading_finished,
                    video_finished
                )
            )

            connection.commit()

        finally:
            cursor.close()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
