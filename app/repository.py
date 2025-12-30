from app.database import get_connection

def insert_stock(data: dict):
    conn = get_connection()
    try:
        conn.execute("""
            INSERT OR IGNORE INTO stocks
            (ticker, timestamp, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, tuple(data.values()))
        conn.commit()
    finally:
        conn.close()

def get_last():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM stocks ORDER BY timestamp DESC LIMIT 1")
    row = cur.fetchone()
    conn.close()
    return row

def get_history(ticker: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM stocks WHERE ticker = ?", (ticker,))
    rows = cur.fetchall()
    conn.close()
    return rows
