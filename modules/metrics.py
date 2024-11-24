import sqlite3
from modules.api import fetch_price
from modules.portfolio import DB_PATH

def calculate_portfolio_value():
    """
    Calculates the total value of all investments in the portfolio.
    """
    total_value = 0.0

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        # Ensure the query selects all the necessary columns
        cursor.execute('SELECT ticker, quantity, average_purchase_price FROM investments')
        investments = cursor.fetchall()

        for investment in investments:
            ticker, quantity, average_purchase_price = investment
            price, _ = fetch_price(ticker)  # Assuming fetch_price returns (price, valid_ticker)
            total_value += price * quantity

    return total_value