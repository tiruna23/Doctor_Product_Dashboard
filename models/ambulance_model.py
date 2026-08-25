import sqlite3

DB_NAME = "hospital.db"

def init_ambulance_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ambulances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_number TEXT NOT NULL,
            driver_name TEXT NOT NULL,
            driver_phone TEXT NOT NULL,
            category TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_ambulance(vehicle_number, driver_name, driver_phone, category, status):
    init_ambulance_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ambulances (vehicle_number, driver_name, driver_phone, category, status)
        VALUES (?, ?, ?, ?, ?)
    """, (vehicle_number, driver_name, driver_phone, category, status))
    conn.commit()
    conn.close()

def get_all_ambulances():
    init_ambulance_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, vehicle_number, driver_name, driver_phone, category, status FROM ambulances")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_ambulance(amb_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ambulances WHERE id = ?", (amb_id,))
    conn.commit()
    conn.close()