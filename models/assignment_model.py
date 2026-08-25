import sqlite3


def get_connection():
    return sqlite3.connect("database/doctor_dashboard.db")


# -------------------------
# Assign Product to Doctor
# -------------------------
def assign_product(doctor_id, product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO doctor_products
        (doctor_id, product_id)
        VALUES (?, ?)
    """, (
        doctor_id,
        product_id
    ))

    conn.commit()
    conn.close()


# -------------------------
# View Assigned Products
# -------------------------
def get_all_assignments():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            doctor_products.id,
            doctors.doctor_name,
            products.product_name,
            products.company_name
        FROM doctor_products
        INNER JOIN doctors
            ON doctor_products.doctor_id = doctors.id
        INNER JOIN products
            ON doctor_products.product_id = products.id
        ORDER BY doctor_products.id DESC
    """)

    assignments = cursor.fetchall()

    conn.close()

    return assignments


# -------------------------
# Delete Assignment
# -------------------------
def delete_assignment(assignment_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM doctor_products WHERE id=?",
        (assignment_id,)
    )

    conn.commit()
    conn.close()