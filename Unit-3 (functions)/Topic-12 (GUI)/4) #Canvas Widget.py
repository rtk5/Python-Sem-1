#Canvas Widget
#Example1
from tkinter import *
win=Tk()
win.title("Tkinter Canvas Widget Demonstration")
win.geometry("300x300")
#creating canvas
cv=Canvas(win, bg = "orange", height = "300")
cv.pack()
win.mainloop()