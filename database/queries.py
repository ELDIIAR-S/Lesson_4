from database.main_db import get_connection


def add_user(name, age, city):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, age, city)
        VALUES (?, ?, ?)
        """,
        (name, age, city)
    )

    conn.commit()
    conn.close()


def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        """
    )

    users = cursor.fetchall()

    conn.close()

    return users


def get_all_users():
    return get_users()