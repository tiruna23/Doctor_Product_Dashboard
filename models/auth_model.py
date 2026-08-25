import sqlite3
import hashlib

DB_FILE = "medicare.db"

def get_db_connection():
    return sqlite3.connect(DB_FILE)

def init_auth_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            security_question TEXT NOT NULL,
            security_answer TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password, sec_question, sec_answer):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password, security_question, security_answer)
            VALUES (?, ?, ?, ?, ?)
        """, (
            username, email, 
            hash_password(password), 
            sec_question, 
            hash_password(sec_answer.lower().strip())
        ))
        conn.commit()
        conn.close()
        return True, "Account created successfully!"
    except sqlite3.IntegrityError:
        return False, "Username or Email already exists!"

def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    return user

def verify_security_answer(username, sec_answer):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND security_answer = ?", (username, hash_password(sec_answer.lower().strip())))
    user = cursor.fetchone()
    conn.close()
    return user

def reset_password(username, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hash_password(new_password), username))
    conn.commit()
    conn.close()
    return True