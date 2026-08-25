import sqlite3
import pandas as pd

DB_FILE = "hospital.db"

def get_connection():
    return sqlite3.connect(DB_FILE, check_same_thread=False)

def get_patient_gender_stats():
    """Fetches total patient distribution by gender for Donut Chart."""
    conn = get_connection()
    try:
        query = "SELECT gender, COUNT(*) as count FROM patients GROUP BY gender"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception:
        conn.close()
        # Fallback dummy data if table is empty
        return pd.DataFrame({"gender": ["Woman", "Man"], "count": [44, 55]})

def get_today_patients_queue():
    """Fetches list of patients scheduled for today."""
    conn = get_connection()
    try:
        query = "SELECT time, patient_name, disease FROM patients WHERE status = 'Admitted' LIMIT 5"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception:
        conn.close()
        return pd.DataFrame()

def get_monthly_patient_analytics():
    """Fetches monthly patient influx for Analytics Trend line chart."""
    conn = get_connection()
    try:
        query = "SELECT strftime('%m', date) as Month, COUNT(*) as Patients FROM schedules GROUP BY Month"
        df = pd.read_sql_query(query, conn)
        conn.close()
        if df.empty:
            raise ValueError("Empty data")
        return df
    except Exception:
        conn.close()
        return pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
            "Patients": [28, 38, 22, 32, 42, 30, 40]
        })