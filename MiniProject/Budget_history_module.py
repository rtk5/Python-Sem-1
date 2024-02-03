from tkinter import *
from tkinter import messagebox as ms
import csv
from Authentication_module import acct

class ExpenseHistory:
    def __init__(self, root):
        self.root = root
        self.root.title('Expense History')
        self.root.attributes('-fullscreen', True)

        self.usn = acct()
        self.history()

    def history(self):
        with open("/home/rithvikmatta/Python/MiniProject/Expenses.csv", 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            frame = Frame(self.root)
            frame.pack(padx=300, pady=200)
            count = 0
            for line in csv_reader:
                if line[0] == self.usn:
                    labels = [line[1], line[2], line[3], line[4]]
                    for i, label_text in enumerate(labels):
                        label = Label(frame, text=label_text, font=24)
                        label.grid(row=count, column=i + 1, sticky='w', padx=10, pady=5)
                    count += 1

        quit_button = Button(frame, text='Quit', command=self.root.destroy, width=7, height=2)
        quit_button.grid(row=count + 1, column=4, sticky='e', pady=10)

if __name__ == "__main__":
    root = Tk()
    app = ExpenseHistory(root)
    root.mainloop()
