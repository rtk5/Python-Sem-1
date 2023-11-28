import tkinter
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Tkinter Button Widget Demonstration")
win.geometry('500x500')
def click():
    messagebox.showinfo("Message", "Green Button clicked")
def click1():
    messagebox.showinfo("Message", "Yellow Button clicked")

    
a=Button(win, text="yellow",command=click1, activeforeground="yellow", activebackground="orange", pady=10)

b=Button(win, text="Blue", activeforeground="blue", activebackground="orange", pady=10)
# adding click function to the below button
c=Button(win, text="Green", command=click, activeforeground = "green",
activebackground="orange", pady=10)
d=Button(win, text="red", activeforeground="red", activebackground="orange", pady=10)
a.pack(side=LEFT)
b.pack(side=RIGHT)
c.pack(side=TOP)
d.pack(side=BOTTOM)
win.mainloop()