import hashlib
import sqlite3

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    hashed_password = hash_password(password)

    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return "User created successfully."
    except sqlite3.IntegrityError:
        conn.close()
        return "Username already exists."

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    hashed_password = hash_password(password)

    cur.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cur.fetchone()
    conn.close()

    return user[0] if user else None
