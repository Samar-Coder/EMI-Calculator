import tkinter as tk
from tkinter import messagebox, ttk
from emi_logic import calculate_emi
from pie_chart import plot_pie_chart
from amortization import generate_amortization_table

def calculate_and_display():
    """Handle button click and update results."""
    try:
        P = float(entry_principal.get())
        rate = float(entry_rate.get())
        tenure = int(entry_tenure.get())

        emi, total_interest, total_payment = calculate_emi(P, rate, tenure)

        label_emi.config(text=f"Monthly EMI: ₹{emi:.2f}")
        label_interest.config(text=f"Total Interest: ₹{total_interest:.2f}")
        label_total.config(text=f"Total Payment: ₹{total_payment:.2f}")

        plot_pie_chart(frame_chart, P, total_interest)
        generate_amortization_table(table, P, rate / 100 / 12, tenure * 12, emi)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

window = tk.Tk()
window.title("EMI Calculator")
window.geometry("600x600")

frame_input = tk.Frame(window)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Loan Amount (₹):").grid(row=0, column=0)
entry_principal = tk.Entry(frame_input)
entry_principal.grid(row=0, column=1)

tk.Label(frame_input, text="Interest Rate (% per annum):").grid(row=1, column=0)
entry_rate = tk.Entry(frame_input)
entry_rate.grid(row=1, column=1)

tk.Label(frame_input, text="Loan Tenure (Years):").grid(row=2, column=0)
entry_tenure = tk.Entry(frame_input)
entry_tenure.grid(row=2, column=1)

calculate_btn = tk.Button(frame_input, text="Calculate EMI", command=calculate_and_display)
calculate_btn.grid(row=3, column=0, columnspan=2, pady=10)

label_emi = tk.Label(window, text="Monthly EMI: ₹0", font=("Arial", 12, "bold"))
label_emi.pack()

label_interest = tk.Label(window, text="Total Interest: ₹0", font=("Arial", 12, "bold"))
label_interest.pack()

label_total = tk.Label(window, text="Total Payment: ₹0", font=("Arial", 12, "bold"))
label_total.pack()

frame_chart = tk.Frame(window)
frame_chart.pack()

table_frame = tk.Frame(window)
table_frame.pack(pady=10)

table = ttk.Treeview(table_frame, columns=("Month", "EMI", "Principal", "Interest", "Balance"), show="headings")
for col in ("Month", "EMI", "Principal", "Interest", "Balance"):
    table.heading(col, text=col)
    table.column(col, width=100)

table.pack()

window.mainloop()
