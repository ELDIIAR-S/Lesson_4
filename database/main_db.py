import sqlite3

DB_NAME = "sqlite3.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect(DB_NAME)