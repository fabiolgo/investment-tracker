import sqlite3
from datetime import datetime

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
                average_purchase_price REAL,
                purchase_dates TEXT  -- Store all purchase dates as a string
            )
        ''')
        conn.commit()

def add_investment(ticker, quantity, purchase_price, purchase_date):
    """
    Adds or updates an investment in the database by ticker symbol.
    """
    try:
        # Ensure the date is in DD-MM-YYYY format
        purchase_date = datetime.strptime(purchase_date, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        raise ValueError("Purchase date must be in DD-MM-YYYY format.")

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        # Check if the investment already exists
        cursor.execute('SELECT id, quantity, average_purchase_price, purchase_dates FROM investments WHERE ticker = ?', (ticker,))
        result = cursor.fetchone()

        if result:
            # Update the investment if it already exists
            investment_id, existing_quantity, existing_avg_price, purchase_dates = result
            new_quantity = existing_quantity + quantity
            # Calculate the new average purchase price
            total_cost = existing_avg_price * existing_quantity + purchase_price * quantity
            new_avg_price = total_cost / new_quantity
            # Append new purchase date to the existing record
            updated_dates = purchase_dates + "," + purchase_date

            cursor.execute('''
                UPDATE investments
                SET quantity = ?, average_purchase_price = ?, purchase_dates = ?
                WHERE id = ?
            ''', (new_quantity, new_avg_price, updated_dates, investment_id))
            print(f"Updated {ticker} with additional {quantity} units.")
        else:
            # Add a new investment if it doesn't exist
            cursor.execute('''
                INSERT INTO investments (ticker, quantity, average_purchase_price, purchase_dates)
                VALUES (?, ?, ?, ?)
            ''', (ticker, quantity, purchase_price, purchase_date))
            print(f"Added new investment for {ticker}.")
        
        conn.commit()

def get_portfolio():
    """
    Fetches all investments from the database.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT ticker, quantity, average_purchase_price, purchase_dates FROM investments')
        return cursor.fetchall()

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