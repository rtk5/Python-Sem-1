from tkinter import *
from tkinter import messagebox as ms
from Authentication_module import verification, click
from Budget_category_module import BudgetRecordWindow
from Expense_entry_module import open_expense_entry_window
from Reports_and_analytics_module import DataAnalyzer
from Budget_history_module import ExpenseHistory
from notification_and_alerts_module import BudgetApp
from user_profile_module import UserProfileApp

def auth():
    verification()

def opt1():
    open_expense_entry_window()

def opt2():
    root2 = Tk()
    root2.title('Budget Category')
    BudgetRecordWindow(root2)
    root2.mainloop()

def opt3():
    root = Tk()
    root.title('Reports and analytics')
    DataAnalyzer(root)
    root.mainloop()

def opt4():
    root = Tk()
    root.title('Expense History')
    ExpenseHistory(root)
    root.mainloop()
    
def opt5():
    root = Tk()
    root.title('Notification and alerts')
    BudgetApp(r"/home/rithvikmatta/Python/MiniProject/Budget_categories3.csv")
    root.mainloop()

def opt6():
    root = Tk()
    root.title('User Profile')
    UserProfileApp(root)
    root.mainloop()

def main_mod():
    root = Tk()
    root.title('Budget tracker')
    root.attributes('-fullscreen', True)
    menu_bar = Menu(root, font=24)
    root.config(menu=menu_bar)
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Menu', menu=file_menu)
    file_menu.add_command(label='Expense Entry', command=opt1)
    file_menu.add_command(label='Budget Category', command=opt2)
    file_menu.add_command(label='Expense History', command=opt4) 
    file_menu.add_command(label='Reports and analytics', command=opt3)
    file_menu.add_command(label='Notification and Alerts', command=opt5)
    file_menu.add_command(label='User Profile', command=opt6)
    file_menu.add_command(label='Quit', command=root.destroy) 
    frame = Frame(root)
    frame.pack(padx=200,pady=250)
    Expense_entry = Button(frame, text = 'Expense Entry', command=opt1, width=17, height=5)
    Expense_entry.grid(row=0,column=0,padx=10,pady=10)
    budget_category = Button(frame, text = 'Budget Category', command=opt2, width=17, height=5)
    budget_category.grid(row=0,column=1,padx=10,pady=10)
    Expense_history = Button(frame, text = 'Expense History', command=opt4, width=17, height=5)
    Expense_history.grid(row=0,column=2,padx=10,pady=10)
    repo_analysis = Button(frame, text = 'Reports and Analytics', command=opt3, width=17, height=5)
    repo_analysis.grid(row=1,column=0,padx=10,pady=10)
    notif = Button(frame, text = 'Notification and Alerts', command=opt5, width=17, height=5)
    notif.grid(row=1,column=1,padx=10,pady=10)
    profile = Button(frame, text = 'User Profile', command=opt6, width=17, height=5)
    profile.grid(row=1,column=2,padx=10,pady=10)
    root.mainloop()

def main_func():
    auth()
    if verification():  
        main_mod()

if __name__ == "__main__":
    main_func()


