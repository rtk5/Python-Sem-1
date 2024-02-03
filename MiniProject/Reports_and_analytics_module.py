
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
from Authentication_module import acct

class DataAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Reports and Analytics")
        self.root.attributes('-fullscreen', True)

        # Create a tabbed layout
        self.tabControl = ttk.Notebook(root)

        # Create a tab for plots
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Plots')

        # Create an entry for USN
        self.usn_entry_label = tk.Label(self.tab1, text="Enter USN:")
        self.usn_entry_label.pack(pady=5)

        self.usn_entry = tk.Entry(self.tab1)
        self.usn_entry.pack(pady=5)

        # Create a bar chart button
        self.bar_chart_button = tk.Button(self.tab1, text='Bar Chart', command=self.plot_bar_chart)
        self.bar_chart_button.pack(pady=10)

        # Create a pie chart button
        self.pie_chart_button = tk.Button(self.tab1, text='Pie Chart', command=self.plot_pie_chart)
        self.pie_chart_button.pack(pady=10)

        self.quit = tk.Button(self.tab1, text='Quit', command=root.destroy)
        self.quit.pack(padx=10, pady=5)

        # Pack the tab control
        self.tabControl.pack(expand=1, fill="both")

        # Create an instance of the Authentication module
        self.usn = acct()

        # Read CSV data
        self.df = pd.read_csv("/home/rithvikmatta/Python/MiniProject/Expenses.csv")

    def plot_bar_chart(self):
        usn = self.usn_entry.get()
        filtered_df = self.df[self.df['Username'] == usn]
        self.plot_chart(filtered_df, chart_type='bar')

    def plot_pie_chart(self):
        usn = self.usn_entry.get()
        filtered_df = self.df[self.df['Username'] == usn]
        self.plot_chart(filtered_df, chart_type='pie')

    def plot_chart(self, data, chart_type='bar'):
        if chart_type == 'bar':
            chart_function = self.plot_bar
        elif chart_type == 'pie':
            chart_function = self.plot_pie

        # Create a chart
        fig = Figure(figsize=(6, 4), dpi=100)
        chart_function(fig, data)

        # Embed the plot in the Tkinter application
        self.embed_plot(fig)

    def plot_bar(self, fig, data):
        ax = fig.add_subplot(111)
        ax.bar(data['Category'], data['Expense amount'])
        ax.set_title("Bar Chart")

    def plot_pie(self, fig, data):
        ax = fig.add_subplot(111)
        ax.pie(data['Expense amount'], labels=data['Category'], autopct='%1.1f%%', startangle=90)
        ax.set_title("Pie Chart")

    def embed_plot(self, fig):
        # Create a canvas to embed the Matplotlib plot in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        # Pack the canvas
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add a toolbar (optional)
        toolbar = NavigationToolbar2Tk(canvas, self.root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzer(root)
    root.mainloop()

