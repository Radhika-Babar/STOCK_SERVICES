import sqlite3
from app.config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            timestamp TEXT UNIQUE,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER
        )
    """)
    conn.commit()
    conn.close()
