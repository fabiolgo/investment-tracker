from modules.api import fetch_price
from modules.portfolio import get_portfolio

def calculate_portfolio_value():
    """
    Calculates the total current value of the portfolio.
    """
    portfolio = get_portfolio()
    total_value = 0

    for investment in portfolio:
        ticker, quantity, purchase_price, _ = investment[1:]  # Skip `id`
        current_price, valid_ticker = fetch_price(ticker)

        if current_price:
            total_value += current_price * quantity
            print(f"{valid_ticker}: {quantity} units @ ${current_price:.2f} each")
        else:
            print(f"Could not fetch current price for {ticker}.")
    
    return total_value