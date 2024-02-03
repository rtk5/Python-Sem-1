from tkinter import *
from tkinter import messagebox as ms
import csv
from Authentication_module import acct

usn = acct()
def entry(e1, e2, e3, e4):
    global usn
    data = [usn,e1.get(), e2.get(), e3.get(), e4.get()]
    with open("/home/rithvikmatta/Python/MiniProject/Expenses.csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if all(data):
            csv_writer.writerow(data)
            ms.showinfo('Message', 'Entry successful')
        else:
            ms.showinfo('Warning!', 'Please enter a value')

def open_expense_entry_window():
    expense_window = Toplevel()
    expense_window.title('Expense Entry')
    expense_window.attributes('-fullscreen',True)

    frame = Frame(expense_window)
    frame.pack(padx=350, pady=300)

    amount = Label(frame, text='Expense amount:')
    amount.config(font=(24))
    amount.grid(row=0, column=0, sticky='e', pady=10)
    e1 = Entry(frame, width=20)
    e1.grid(row=0, column=1, sticky='w', pady=10)
    category = Label(frame, text='Category:')
    category.config(font=(24))
    category.grid(row=1, column=0, sticky='e', pady=10)
    e2 = Entry(frame, width=20)
    e2.grid(row=1, column=1, sticky='w', pady=10)
    date = Label(frame, text='Date:')
    date.config(font=(24))
    date.grid(row=2, column=0, sticky='e', pady=10)
    e3 = Entry(frame, width=20)
    e3.grid(row=2, column=1, sticky='w', pady=10)
    description = Label(frame, text='Description:')
    description.config(font=24)
    description.grid(row=3, column=0, sticky='e', pady=10)
    e4 = Entry(frame, width=20)
    e4.grid(row=3, column=1, sticky='w', pady=10)

    enter = Button(frame, text='Enter', command=lambda: entry(e1, e2, e3, e4), width=10, height=2)
    enter.grid(row=4, column=0, sticky='e', padx=5, pady=15)
    quit_button = Button(frame, text='Quit', command=expense_window.destroy, width=10, height=2)
    quit_button.grid(row=4, column=1, sticky='w', padx=5, pady=15)

if __name__ == "__main__":
    root3 = Tk()
    root3.title('Expense entry')
    root3.attributes('-fullscreen', True)

    frame = Frame(root3)
    frame.pack(padx=350, pady=300)

    menu_button = Button(root3, text='Open Expense Entry', command=open_expense_entry_window)
    menu_button.pack(pady=20)

    root3.mainloop()
