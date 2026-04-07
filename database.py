import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    employee_no TEXT PRIMARY KEY,
    name TEXT,
    telegram_id INTEGER
)
""")

conn.commit()


def add_user(emp, name):
    cursor.execute(
        "INSERT OR REPLACE INTO users (employee_no, name) VALUES (?, ?)",
        (emp, name)
    )
    conn.commit()


def get_users():
    cursor.execute("SELECT employee_no, name FROM users")
    return cursor.fetchall()


def bind_user(emp, tg_id):
    cursor.execute(
        "UPDATE users SET telegram_id=? WHERE employee_no=?",
        (tg_id, emp)
    )
    conn.commit()


def get_user_by_tg(tg_id):
    cursor.execute(
        "SELECT employee_no, name FROM users WHERE telegram_id=?",
        (tg_id,)
    )
    return cursor.fetchone()
