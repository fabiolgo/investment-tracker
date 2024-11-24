import sqlite3

DB_PATH = "data/portfolio.db"

def init_db():
    """
    Initializes the database by creating the investments table if it doesn't exist.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS investments (
                id INTEGER PRIMARY KEY,
                ticker TEXT,
                quantity REAL,
                purchase_price REAL,
                purchase_date TEXT
            )
        ''')
        conn.commit()

def add_investment(ticker, quantity, purchase_price, purchase_date):
    """
    Adds a new investment to the database.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO investments (ticker, quantity, purchase_price, purchase_date)
            VALUES (?, ?, ?, ?)
        ''', (ticker, quantity, purchase_price, purchase_date))
        conn.commit()

def delete_investment(ticker):
    """
    Deletes an investment by its ticker symbol from the database.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM investments WHERE ticker = ?', (ticker,))
        if cursor.rowcount == 0:
            print(f"No investment found for ticker {ticker}.")
        else:
            print(f"Investment for ticker {ticker} deleted.")
        conn.commit()

def get_portfolio():
    """
    Fetches all investments from the database.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM investments')
        return cursor.fetchall()