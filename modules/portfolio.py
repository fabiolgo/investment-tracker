import sqlite3

DB_PATH = "data/portfolio.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS investments (
                            id INTEGER PRIMARY KEY,
                            ticker TEXT,
                            quantity REAL,
                            purchase_price REAL,
                            purchase_date TEXT
                          )''')
        conn.commit()

def add_investment(ticker, quantity, purchase_price, purchase_date):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO investments (ticker, quantity, purchase_price, purchase_date) VALUES (?, ?, ?, ?)',
                       (ticker, quantity, purchase_price, purchase_date))
        conn.commit()

def get_portfolio():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM investments')
        return cursor.fetchall()