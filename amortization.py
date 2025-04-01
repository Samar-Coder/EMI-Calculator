def generate_amortization_table(table, principal, rate, tenure, emi):
    """Generate the amortization schedule and insert it into the table."""
    for row in table.get_children():
        table.delete(row)
    
    balance = principal
    for month in range(1, tenure + 1):
        interest = balance * rate
        principal_payment = emi - interest
        balance -= principal_payment
        table.insert("", "end", values=(
            month, f"₹{emi:.2f}", f"₹{principal_payment:.2f}", f"₹{interest:.2f}", f"₹{balance:.2f}"
        ))
