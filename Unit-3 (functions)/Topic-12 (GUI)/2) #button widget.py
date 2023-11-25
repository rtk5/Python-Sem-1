#button widget
from tkinter import *
win=Tk()
win.title("Tkinter Demonstration")
win.geometry('300x200')
b=Button(win,text='Submit')
b.pack()
win.mainloop()