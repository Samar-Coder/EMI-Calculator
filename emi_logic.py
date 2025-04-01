def calculate_emi(principal, rate, tenure):
    """Calculate EMI, total interest, and total payment."""
    rate = rate / 100 / 12  
    tenure = tenure * 12 
    
    if rate == 0:
        emi = principal / tenure
    else:
        emi = (principal * rate * (1 + rate) ** tenure) / ((1 + rate) ** tenure - 1)
    
    total_payment = emi * tenure
    total_interest = total_payment - principal
    
    return emi, total_interest, total_payment
