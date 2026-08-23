from database.main_db import get_connection


def save_user(name, age, phone):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, age, phone)
        VALUES (?, ?, ?)
        """,
        (name, age, phone)
    )

    conn.commit()
    conn.close()


def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, age, phone FROM users"
    )

    users = cursor.fetchall()

    conn.close()

    return users