import sqlite3


def get_connection():
    return sqlite3.connect("database/doctor_dashboard.db")


# -------------------------
# Add Product
# -------------------------
def add_product(product_name, company_name, molecule, specialty, description):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products
        (product_name, company_name, molecule, specialty, description)
        VALUES (?, ?, ?, ?, ?)
    """, (
        product_name,
        company_name,
        molecule,
        specialty,
        description
    ))

    conn.commit()
    conn.close()


# -------------------------
# View All Products
# -------------------------
def get_all_products():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            product_name,
            company_name,
            molecule,
            specialty,
            description
        FROM products
        ORDER BY id DESC
    """)

    products = cursor.fetchall()

    conn.close()

    return products


# -------------------------
# Get Single Product
# -------------------------
def get_product_by_id(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE id=?",
        (product_id,)
    )

    product = cursor.fetchone()

    conn.close()

    return product


# -------------------------
# Update Product
# -------------------------
def update_product(
    product_id,
    product_name,
    company_name,
    molecule,
    specialty,
    description
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET
            product_name=?,
            company_name=?,
            molecule=?,
            specialty=?,
            description=?
        WHERE id=?
    """, (
        product_name,
        company_name,
        molecule,
        specialty,
        description,
        product_id
    ))

    conn.commit()
    conn.close()


# -------------------------
# Delete Product
# -------------------------
def delete_product(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id=?",
        (product_id,)
    )

    conn.commit()
    conn.close()