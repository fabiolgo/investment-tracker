import yfinance as yf

ticker = "VWCE.DE"  # Replace with the correct ticker if needed
stock = yf.Ticker(ticker)
print(stock.history(period="1d"))