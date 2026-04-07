import sqlite3

conn = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    employee_no TEXT PRIMARY KEY,
    name TEXT,
    telegram_id INTEGER,
    role TEXT DEFAULT 'employee'
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS schedules (
    employee_no TEXT,
    days TEXT,
    start INTEGER,
    end INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    employee_no TEXT,
    timestamp TEXT
)
""")

conn.commit()


def add_user(emp, name):
    cursor.execute("INSERT INTO users VALUES (?, ?, NULL, 'employee')", (emp, name))
    conn.commit()


def delete_user(emp):
    cursor.execute("DELETE FROM users WHERE employee_no=?", (emp,))
    conn.commit()


def get_users():
    cursor.execute("SELECT employee_no, name FROM users")
    return cursor.fetchall()


def bind_user(emp, tg):
    cursor.execute("UPDATE users SET telegram_id=? WHERE employee_no=?", (tg, emp))
    conn.commit()


def get_emp(tg):
    cursor.execute("SELECT employee_no FROM users WHERE telegram_id=?", (tg,))
    r = cursor.fetchone()
    return r[0] if r else None


def set_schedule(emp, days, start, end):
    cursor.execute("DELETE FROM schedules WHERE employee_no=?", (emp,))
    cursor.execute("INSERT INTO schedules VALUES (?, ?, ?, ?)", (emp, days, start, end))
    conn.commit()


def get_schedule(emp):
    cursor.execute("SELECT days, start, end FROM schedules WHERE employee_no=?", (emp,))
    return cursor.fetchone()


def add_event(emp, ts):
    cursor.execute("INSERT INTO events VALUES (?, ?)", (emp, ts))
    conn.commit()


def event_exists(emp, ts):
    cursor.execute("SELECT 1 FROM events WHERE employee_no=? AND timestamp=?", (emp, ts))
    return cursor.fetchone() is not None


def get_events(emp, date):
    cursor.execute("""
    SELECT timestamp FROM events
    WHERE employee_no=? AND date(timestamp)=?
    ORDER BY timestamp
    """, (emp, date))
    return [x[0] for x in cursor.fetchall()]
