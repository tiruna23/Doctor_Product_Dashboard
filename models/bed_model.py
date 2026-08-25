import sqlite3


# =====================================================
# DATABASE CONNECTION
# =====================================================

def get_connection():

    return sqlite3.connect(
        "database/doctor_dashboard.db"
    )


# =====================================================
# ADD BED
# =====================================================

def add_bed(
    bed_number,
    ward,
    bed_type,
    status
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO beds
        (
            bed_number,
            ward,
            bed_type,
            status
        )
        VALUES (?, ?, ?, ?)
    """, (
        bed_number,
        ward,
        bed_type,
        status
    ))

    conn.commit()
    conn.close()


# =====================================================
# GET ALL BEDS
# =====================================================

def get_all_beds():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            bed_number,
            ward,
            bed_type,
            status,
            patient_id
        FROM beds
        ORDER BY id DESC
    """)

    beds = cursor.fetchall()

    conn.close()

    return beds


# =====================================================
# GET SINGLE BED
# =====================================================

def get_bed_by_id(bed_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM beds WHERE id=?",
        (bed_id,)
    )

    bed = cursor.fetchone()

    conn.close()

    return bed


# =====================================================
# UPDATE BED
# =====================================================

def update_bed(
    bed_id,
    bed_number,
    ward,
    bed_type,
    status
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE beds
        SET
            bed_number=?,
            ward=?,
            bed_type=?,
            status=?
        WHERE id=?
    """, (
        bed_number,
        ward,
        bed_type,
        status,
        bed_id
    ))

    conn.commit()
    conn.close()


# =====================================================
# DELETE BED
# =====================================================

def delete_bed(bed_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM beds WHERE id=?",
        (bed_id,)
    )

    conn.commit()
    conn.close()


# =====================================================
# AVAILABLE BEDS
# =====================================================

def get_available_beds():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM beds
        WHERE status='Available'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total