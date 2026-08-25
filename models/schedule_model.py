import sqlite3
import pandas as pd

DB_FILE = "hospital.db"

def get_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_schedule_table():
    """Initializes the schedules table if it does not already exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_name TEXT NOT NULL,
            patient_name TEXT NOT NULL,
            department TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)
    conn.commit()
    conn.close()

# Automatically initialize database table on load
init_schedule_table()

def get_total_schedules():
    """Returns the total number of scheduled appointments."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM schedules")
        count = cursor.fetchone()[0]
    except Exception:
        count = 0
    finally:
        conn.close()
    return count

def get_all_schedules():
    """Fetches all schedules as a Pandas DataFrame."""
    conn = get_connection()
    try:
        df = pd.read_sql_query("SELECT * FROM schedules ORDER BY id DESC", conn)
    except Exception:
        df = pd.DataFrame()
    finally:
        conn.close()
    return df

def add_schedule(doctor_name, patient_name, department, appointment_date, appointment_time, status="Confirmed"):
    """Inserts a new appointment record into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO schedules (doctor_name, patient_name, department, appointment_date, appointment_time, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (doctor_name, patient_name, department, str(appointment_date), str(appointment_time), status))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

def delete_schedule(schedule_id):
    """Deletes an appointment record by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM schedules WHERE id = ?", (schedule_id,))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()