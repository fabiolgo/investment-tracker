from modules.portfolio import init_db, add_investment, get_portfolio, delete_investment
from modules.metrics import calculate_portfolio_value
from modules.reports import generate_report
from modules.api import fetch_price

def add_investment_with_check():
    """
    Adds an investment after validating and correcting the ticker symbol.
    """
    ticker = input("Enter ticker symbol: ")
    quantity = float(input("Enter quantity: "))
    purchase_price = float(input("Enter purchase price: "))
    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")

    # Validate ticker
    price, valid_ticker = fetch_price(ticker)
    if not valid_ticker:
        print(f"Could not find ticker {ticker}. Please try again.")
        return
    
    add_investment(valid_ticker, quantity, purchase_price, purchase_date)
    print(f"Investment added for ticker: {valid_ticker}")

def main():
    """
    Main application loop for the investment tracker.
    """
    init_db()
    print("Welcome to the Investment Tracker!")
    
    while True:
        print("\nMenu:")
        print("1. Add Investment")
        print("2. View Portfolio")
        print("3. Calculate Portfolio Value")
        print("4. Generate Report")
        print("5. Delete Investment")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_investment_with_check()
        
        elif choice == "2":
            portfolio = get_portfolio()
            for row in portfolio:
                print(row)
        
        elif choice == "3":
            value = calculate_portfolio_value()
            print(f"Total portfolio value: ${value:.2f}")
        
        elif choice == "4":
            portfolio = get_portfolio()
            generate_report("portfolio_report.pdf", portfolio)
        
        elif choice == "5":
            ticker = input("Enter the ticker symbol to delete: ")
            delete_investment(ticker)
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()