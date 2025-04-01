import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_pie_chart(frame, principal, interest):
    """Generate and display the pie chart."""
    fig, ax = plt.subplots()
    sizes = [principal, interest]
    labels = ["Principal", "Interest"]
    colors = ["lightblue", "red"]

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Principal vs. Interest")

    for widget in frame.winfo_children():
        widget.destroy()  

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()
    canvas.draw()
