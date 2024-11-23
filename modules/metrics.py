from modules.api import fetch_price
from modules.portfolio import get_portfolio

def calculate_portfolio_value():
    portfolio = get_portfolio()
    total_value = 0
    for investment in portfolio:
        ticker, quantity, purchase_price, _ = investment[1:]  # Skip `id`
        current_price = fetch_price(ticker)
        if current_price:
            total_value += current_price * quantity
    return total_value