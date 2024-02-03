'''import tkinter as tk
from tkinter import messagebox
import csv
import datetime

class BudgetApp(tk.Tk):
    def __init__(self, csv_file_path):
        super().__init__()
        self.csv_file_path = csv_file_path
        self.read_csv()
        self.create_widgets()

    def read_csv(self):
        try:
            with open(self.csv_file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.data = list(reader)
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            self.data = []

    def create_widgets(self):
        tk.Button(self, text="Check Budget Limits", command=self.check_budget_limits).pack()
        tk.Button(self, text="Check Upcoming Bills", command=self.check_upcoming_bills).pack()

    def check_budget_limits(self):
        for row in self.data:
            try:
                actual, budget = float(row['Actual']), float(row['Budget limit'])
                if actual > budget:
                    message = f"Budget Limit Exceeded!\nCategory: {row['Budget Category']}\nActual: ${actual}\nBudget: ${budget}"
                    messagebox.showwarning("Budget Limit Exceeded", message)
            except (KeyError, ValueError) as e:
                print(f"Error processing budget limit: {e}")

    def check_upcoming_bills(self):
        today = datetime.date.today()
        for row in self.data:
            try:
                due_date = datetime.datetime.strptime(row['due_date'], '%d-%m-%Y').date()
                if due_date > today:
                    message = f"Upcoming Bill/Expense!\nCategory: {row['Budget Category']}\nDue Date: {due_date}\nAmount: ${float(row['amount'])}"
                    messagebox.showinfo("Upcoming Bill/Expense", message)
            except (KeyError, ValueError) as e:
                print(f"Error processing upcoming bills: {e}")

if __name__ == "__main__":
    app = BudgetApp(r"C:/Users/rithv/WORK/PES/Miniproject/Budget_categories3.csv")
    app.mainloop()'''

import tkinter as tk
from tkinter import messagebox
import csv
import datetime

class BudgetApp(tk.Tk):
    def __init__(self, csv_file_path):
        super().__init__()
        self.csv_file_path = csv_file_path
        self.data = []
        self.read_csv()
        self.create_widgets()

    def read_csv(self):
        try:
            with open(self.csv_file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.data = list(reader)
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            self.data = []

    def update_csv_path(self, new_csv_file_path):
        self.csv_file_path = new_csv_file_path
        self.read_csv()

    def create_widgets(self):
        tk.Button(self, text="Check Budget Limits", command=self.check_budget_limits).pack()
        tk.Button(self, text="Check Upcoming Bills", command=self.check_upcoming_bills).pack()

    def check_budget_limits(self):
        for row in self.data:
            try:
                actual, budget = float(row['Actual']), float(row['Budget limit'])
                if actual > budget:
                    message = f"Budget Limit Exceeded!\nCategory: {row['Budget Category']}\nActual: ${actual}\nBudget: ${budget}"
                    messagebox.showwarning("Budget Limit Exceeded", message)
            except (KeyError, ValueError) as e:
                print(f"Error processing budget limit: {e}")

    def check_upcoming_bills(self):
        today = datetime.date.today()
        for row in self.data:
            try:
                due_date = datetime.datetime.strptime(row['due_date'], '%d-%m-%Y').date()
                if due_date > today:
                    message = f"Upcoming Bill/Expense!\nCategory: {row['Budget Category']}\nDue Date: {due_date}\nAmount: ${float(row['amount'])}"
                    messagebox.showinfo("Upcoming Bill/Expense", message)
            except (KeyError, ValueError) as e:
                print(f"Error processing upcoming bills: {e}")

# Example usage
if __name__ == "__main__":
    app = BudgetApp(r"/home/rithvikmatta/Python/MiniProject/Budget_categories3.csv")
    app.mainloop()

