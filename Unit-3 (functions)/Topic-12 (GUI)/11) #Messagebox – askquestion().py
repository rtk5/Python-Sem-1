#Messagebox – askquestion()
#Example1
from tkinter import *
from tkinter import messagebox
win=Tk()
# function to use the askquestion() function
def Submit():
    messagebox.askquestion("Form", "Do you want to Submit")
win.geometry("300x300")
# creating Submit Button
b=Button(win, text = "Submit", command = Submit)
b.pack()
win.mainloop()

#showinfo() To display some important information
#showwarning() To display some type of Warning
#showerror() To display some Error Message
#askquestion() To display a dialog box that asks with two options YES or NO
#askokcancel() To display a dialog box that asks with two options OK or CANCEL
#askretrycancel() To display a dialog box that asks with two options RETRY or CANCEL
#askyesnocancel()
