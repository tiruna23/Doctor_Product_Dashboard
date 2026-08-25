import sqlite3


# =====================================================
# DATABASE CONNECTION
# =====================================================

def get_connection():

    return sqlite3.connect(
        "database/doctor_dashboard.db"
    )


# =====================================================
# ADD SCHEDULE
# =====================================================

def add_schedule(
    doctor_id,
    patient_id,
    schedule_date,
    schedule_time,
    schedule_type,
    status,
    notes
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO schedules(
            doctor_id,
            patient_id,
            schedule_date,
            schedule_time,
            schedule_type,
            status,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            doctor_id,
            patient_id,
            schedule_date,
            schedule_time,
            schedule_type,
            status,
            notes
        )
    )

    conn.commit()

    conn.close()


# =====================================================
# GET ALL SCHEDULES
# =====================================================

def get_all_schedules():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            schedules.id,
            doctors.doctor_name,
            patients.patient_name,
            schedules.schedule_date,
            schedules.schedule_time,
            schedules.schedule_type,
            schedules.status,
            schedules.notes

        FROM schedules

        LEFT JOIN doctors
            ON schedules.doctor_id = doctors.id

        LEFT JOIN patients
            ON schedules.patient_id = patients.id

        ORDER BY
            schedules.schedule_date DESC,
            schedules.schedule_time DESC
        """
    )

    schedules = cursor.fetchall()

    conn.close()

    return schedules


# =====================================================
# GET SCHEDULE BY ID
# =====================================================

def get_schedule_by_id(schedule_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            doctor_id,
            patient_id,
            schedule_date,
            schedule_time,
            schedule_type,
            status,
            notes

        FROM schedules

        WHERE id = ?
        """,
        (schedule_id,)
    )

    schedule = cursor.fetchone()

    conn.close()

    return schedule


# =====================================================
# UPDATE SCHEDULE
# =====================================================

def update_schedule(
    schedule_id,
    doctor_id,
    patient_id,
    schedule_date,
    schedule_time,
    schedule_type,
    status,
    notes
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE schedules

        SET
            doctor_id = ?,
            patient_id = ?,
            schedule_date = ?,
            schedule_time = ?,
            schedule_type = ?,
            status = ?,
            notes = ?

        WHERE id = ?
        """,
        (
            doctor_id,
            patient_id,
            schedule_date,
            schedule_time,
            schedule_type,
            status,
            notes,
            schedule_id
        )
    )

    conn.commit()

    conn.close()


# =====================================================
# DELETE SCHEDULE
# =====================================================

def delete_schedule(schedule_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM schedules
        WHERE id = ?
        """,
        (schedule_id,)
    )

    conn.commit()

    conn.close()


# =====================================================
# GET TOTAL SCHEDULES
# =====================================================

def get_total_schedules():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM schedules
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total