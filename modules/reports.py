from reportlab.pdfgen import canvas

def generate_report(file_name, portfolio_data):
    c = canvas.Canvas(file_name)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Investment Portfolio Report")
    c.drawString(100, 730, "---------------------------------------")

    y = 700
    for investment in portfolio_data:
        c.drawString(100, y, f"{investment[1]}: {investment[2]} units @ ${investment[3]}")
        y -= 20

    c.save()
    print(f"Report saved to {file_name}")