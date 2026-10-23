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
