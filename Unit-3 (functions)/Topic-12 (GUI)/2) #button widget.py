#button widget
from tkinter import *
win=Tk()
win.title("Tkinter Demonstration")
win.geometry('700x900')
b=Button(win,text='Submit')
c=Button(win,text='Exit')
b.pack()
c.pack()
win.mainloop()
