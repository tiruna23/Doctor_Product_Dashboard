import sqlite3


# =====================================================
# DATABASE CONNECTION
# =====================================================

def get_connection():

    return sqlite3.connect(
        "database/doctor_dashboard.db"
    )


# =====================================================
# ADD DOCTOR
# =====================================================

def add_doctor(
    doctor_name,
    specialty,
    whatsapp_number
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO doctors
        (
            doctor_name,
            hospital_name,
            specialty,
            whatsapp_number
        )
        VALUES (?, ?, ?, ?)
    """, (
        doctor_name,
        "MediCare Hospital",
        specialty,
        whatsapp_number
    ))

    conn.commit()
    conn.close()


# =====================================================
# GET ALL DOCTORS
# =====================================================

def get_all_doctors():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            doctor_name,
            specialty,
            whatsapp_number
        FROM doctors
        ORDER BY id DESC
    """)

    doctors = cursor.fetchall()

    conn.close()

    return doctors


# =====================================================
# GET SINGLE DOCTOR
# =====================================================

def get_doctor_by_id(doctor_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            doctor_name,
            specialty,
            whatsapp_number
        FROM doctors
        WHERE id=?
    """, (
        doctor_id,
    ))

    doctor = cursor.fetchone()

    conn.close()

    return doctor


# =====================================================
# UPDATE DOCTOR
# =====================================================

def update_doctor(
    doctor_id,
    doctor_name,
    specialty,
    whatsapp_number
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE doctors
        SET
            doctor_name=?,
            specialty=?,
            whatsapp_number=?
        WHERE id=?
    """, (
        doctor_name,
        specialty,
        whatsapp_number,
        doctor_id
    ))

    conn.commit()
    conn.close()


# =====================================================
# DELETE DOCTOR
# =====================================================

def delete_doctor(doctor_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM doctors WHERE id=?",
        (doctor_id,)
    )

    conn.commit()
    conn.close()