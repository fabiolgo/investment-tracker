import yfinance as yf

def fetch_price(ticker):
    """
    Fetches the current price for a ticker symbol.
    Tries adding common suffixes if the ticker is not recognized.
    
    Returns:
        - price: The latest closing price (float) if available, None otherwise.
        - valid_ticker: The valid ticker symbol (str) with suffix if found, None otherwise.
    """
    # List of possible suffixes
    suffixes = ["", ".DE", ".L", ".HK"]  # Extend based on common exchanges
    for suffix in suffixes:
        try:
            stock = yf.Ticker(ticker + suffix)
            history = stock.history(period="1d")
            
            # Check if data is available
            if not history.empty:
                print(f"Ticker found: {ticker + suffix}")
                return history['Close'].iloc[-1], ticker + suffix  # Return price and valid ticker
        except Exception as e:
            print(f"Error fetching data for {ticker + suffix}: {e}")
    
    # If no valid ticker is found
    print(f"Ticker {ticker} not found with any suffix.")
    return None, None

if __name__ == "__main__":
    # Example usage
    test_ticker = "VWCE"
    price, valid_ticker = fetch_price(test_ticker)
    if price:
        print(f"Price for {valid_ticker}: ${price:.2f}")
    else:
        print(f"Ticker {test_ticker} not found.")