from tkinter import *
from tkinter import messagebox as ms
import csv
from Authentication_module import acct

usn = acct()
class BudgetRecordWindow:
    def __init__(self, master):
        global usn
        self.master = master
        self.master.title("Centered Labels and Entries")
        self.master.attributes('-fullscreen', True)

        self.frame = Frame(self.master)
        self.frame.pack(padx=50, pady=200)

        self.labels = ["Budget Name:", "Username:", "Budget Category:", "Budget limit:", "Current Expense amount:", "Bill due date:", "Bill amount:"]
        self.entries = [Entry(self.frame) for _ in range(len(self.labels))]

        for i, label_text in enumerate(self.labels):
            label = Label(self.frame, text=label_text)
            label.config(font=(30))
            label.grid(row=i, column=0, sticky="e", pady=10)
            self.entries[i].grid(row=i, column=1, sticky="e", pady=10)

        submit = Button(self.frame, text='Submit', command=self.record, width=7, height=2)
        submit.grid(row=7, column=0, sticky='e', padx=5)
        quit_button = Button(self.frame, text='Quit', command=self.master.destroy, width=7, height=2)
        quit_button.grid(row=7, column=1, sticky='w', padx=5)

    def record(self):
        data = [entry.get() for entry in self.entries]
        with open("/home/rithvikmatta/Python/MiniProject/Budget_categories3.csv", 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if all(data):
                csv_writer.writerow(data)
                ms.showinfo('Message:', 'Data entered successfully')
            else:
                ms.showinfo('Message:', 'Please enter a value')

if __name__ == "__main__":
    root = Tk()
    app = BudgetRecordWindow(root)
    root.mainloop()



