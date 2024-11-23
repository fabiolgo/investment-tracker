from modules.portfolio import init_db, add_investment, get_portfolio
from modules.metrics import calculate_portfolio_value
from modules.reports import generate_report

def main():
    init_db()
    print("Welcome to the Investment Tracker!")
    
    while True:
        print("\nMenu:")
        print("1. Add Investment")
        print("2. View Portfolio")
        print("3. Calculate Portfolio Value")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            ticker = input("Enter ticker symbol: ")
            quantity = float(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
            add_investment(ticker, quantity, purchase_price, purchase_date)
            print("Investment added!")
        
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()