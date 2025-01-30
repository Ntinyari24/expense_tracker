import sqlite3

def initialize_database():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT,
        transaction_type TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

def add_transaction(transaction):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO transactions (user_id, amount, category, description, date, transaction_type) 
    VALUES (?, ?, ?, ?, ?, ?)
    """, (transaction.user_id, transaction.amount, transaction.category, transaction.description, transaction.date, transaction.transaction_type))

    conn.commit()
    conn.close()
