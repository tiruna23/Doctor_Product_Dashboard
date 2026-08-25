import sqlite3
import pandas as pd


# =====================================================
# DATABASE CONNECTION
# =====================================================

def get_connection():

    return sqlite3.connect(
        "database/doctor_dashboard.db"
    )


# =====================================================
# TOTAL PRODUCTS
# =====================================================

def get_total_products():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM products"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# TOTAL DOCTORS
# =====================================================

def get_total_doctors():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM doctors"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# TOTAL ASSIGNMENTS
# =====================================================

def get_total_assignments():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM doctor_products"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# TOTAL COMPANIES
# =====================================================

def get_total_companies():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT company_name)
        FROM products
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# TOTAL PATIENTS
# =====================================================

def get_total_patients():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM patients
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# AVAILABLE BEDS
# =====================================================

def get_available_beds():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM beds
        WHERE status = 'Available'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# TOTAL AMBULANCES
# =====================================================

def get_total_ambulances():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM ambulances
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# RECENT PRODUCTS
# =====================================================

def get_recent_products():

    conn = get_connection()

    query = """
        SELECT
            product_name,
            company_name
        FROM products
        ORDER BY id DESC
        LIMIT 5
    """

    data = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return data


# =====================================================
# RECENT DOCTORS
# =====================================================

def get_recent_doctors():

    conn = get_connection()

    query = """
        SELECT
            doctor_name,
            hospital_name
        FROM doctors
        ORDER BY id DESC
        LIMIT 5
    """

    data = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return data


# =====================================================
# RECENT ASSIGNMENTS
# =====================================================

def get_recent_assignments():

    conn = get_connection()

    query = """
        SELECT
            doctors.doctor_name,
            products.product_name
        FROM doctor_products

        INNER JOIN doctors
            ON doctor_products.doctor_id = doctors.id

        INNER JOIN products
            ON doctor_products.product_id = products.id

        ORDER BY doctor_products.id DESC

        LIMIT 5
    """

    data = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return data


# =====================================================
# PRODUCTS BY COMPANY
# =====================================================

def get_company_wise_products():

    conn = get_connection()

    query = """
        SELECT
            company_name,
            COUNT(*) AS Total
        FROM products
        GROUP BY company_name
    """

    data = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return data


# =====================================================
# DOCTORS BY SPECIALTY
# =====================================================

def get_specialty_wise_doctors():

    conn = get_connection()

    query = """
        SELECT
            specialty,
            COUNT(*) AS Total
        FROM doctors
        GROUP BY specialty
    """

    data = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return data

    # =====================================================
# BED STATUS
# =====================================================

def get_bed_status():

    conn = get_connection()

    query = """
        SELECT
            status,
            COUNT(*) AS Total
        FROM beds
        GROUP BY status
    """

    data = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return data


# =====================================================
# AMBULANCE STATUS
# =====================================================

def get_ambulance_status():

    conn = get_connection()

    query = """
        SELECT
            status,
            COUNT(*) AS Total
        FROM ambulances
        GROUP BY status
    """

    data = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return data