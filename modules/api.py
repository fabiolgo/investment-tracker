import yfinance as yf

def fetch_price(str(ticker)):
    try:
        stock = yf.Ticker()
        return stock.history(period="1d")['Close'][-1]  # Latest closing price
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None