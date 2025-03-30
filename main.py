import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def calculate_emi():
    try:
        P = float(entry_principal.get())
        rate = float(entry_rate.get()) / 100 / 12  # Monthly interest rate
        tenure = int(entry_tenure.get()) * 12  # Convert years to months
        
        emi = (P * rate * (1 + rate) ** tenure) / ((1 + rate) ** tenure - 1)
        total_payment = emi * tenure
        total_interest = total_payment - P
        
        label_emi.config(text=f"Monthly EMI: ₹{emi:.2f}")
        label_interest.config(text=f"Total Interest: ₹{total_interest:.2f}")
        label_total.config(text=f"Total Payment: ₹{total_payment:.2f}")
        
        plot_pie_chart(P, total_interest)
        generate_amortization_table(P, rate, tenure, emi)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def plot_pie_chart(principal, interest):
    fig, ax = plt.subplots()
    sizes = [principal, interest]
    labels = ["Principal", "Interest"]
    colors = ["lightblue", "red"]
    
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Principal vs. Interest")
    
    for widget in frame_chart.winfo_children():
        widget.destroy()  # Clear previous charts
    
    canvas = FigureCanvasTkAgg(fig, master=frame_chart)
    canvas.get_tk_widget().pack()
    canvas.draw()

def generate_amortization_table(P, rate, tenure, emi):
    for row in table.get_children():
        table.delete(row)
    
    balance = P
    for month in range(1, tenure + 1):
        interest = balance * rate
        principal = emi - interest
        balance -= principal
        table.insert("", "end", values=(month, f"₹{emi:.2f}", f"₹{principal:.2f}", f"₹{interest:.2f}", f"₹{balance:.2f}"))

# GUI Setup
window = tk.Tk()
window.title("EMI Calculator")
window.geometry("600x600")

frame_input = tk.Frame(window)
frame_input.pack(pady=10)

# Input Fields
tk.Label(frame_input, text="Loan Amount (₹):").grid(row=0, column=0)
entry_principal = tk.Entry(frame_input)
entry_principal.grid(row=0, column=1)

tk.Label(frame_input, text="Interest Rate (% per annum):").grid(row=1, column=0)
entry_rate = tk.Entry(frame_input)
entry_rate.grid(row=1, column=1)

tk.Label(frame_input, text="Loan Tenure (Years):").grid(row=2, column=0)
entry_tenure = tk.Entry(frame_input)
entry_tenure.grid(row=2, column=1)

# Calculate Button
calculate_btn = tk.Button(frame_input, text="Calculate EMI", command=calculate_emi)
calculate_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Output Labels
label_emi = tk.Label(window, text="Monthly EMI: ₹0", font=("Arial", 12, "bold"))
label_emi.pack()

label_interest = tk.Label(window, text="Total Interest: ₹0", font=("Arial", 12, "bold"))
label_interest.pack()

label_total = tk.Label(window, text="Total Payment: ₹0", font=("Arial", 12, "bold"))
label_total.pack()

# Pie Chart Frame
frame_chart = tk.Frame(window)
frame_chart.pack()

# Amortization Table
table_frame = tk.Frame(window)
table_frame.pack(pady=10)

table = ttk.Treeview(table_frame, columns=("Month", "EMI", "Principal", "Interest", "Balance"), show="headings")
for col in ("Month", "EMI", "Principal", "Interest", "Balance"):
    table.heading(col, text=col)
    table.column(col, width=100)

table.pack()

window.mainloop()
