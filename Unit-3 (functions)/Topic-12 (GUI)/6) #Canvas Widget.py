#Canvas Widget
#Example3
from tkinter import *
win=Tk()
cv=Canvas(win, height=700, width=700)
filename=PhotoImage(file="nature.png")
image=cv.create_image(20, 20, anchor=NW, image=filename)
cv.pack()
win.mainloop()