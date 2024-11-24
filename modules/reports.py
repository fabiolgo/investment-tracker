from reportlab.pdfgen import canvas

def generate_report(file_name, portfolio_data):
    """
    Generates a PDF report for the investment portfolio.
    """
    c = canvas.Canvas(file_name)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Investment Portfolio Report")
    c.drawString(100, 730, "---------------------------------------")

    y = 700
    for investment in portfolio_data:
        ticker, quantity, purchase_price, purchase_date = investment[1:]  # Skip `id`
        c.drawString(100, y, f"{ticker}: {quantity} units @ ${purchase_price:.2f} (purchased {purchase_date})")
        y -= 20

    c.save()
    print(f"Report saved to {file_name}")