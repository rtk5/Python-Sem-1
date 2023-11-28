#Frame widget
#Example1
from tkinter import *
win = Tk()
win.geometry("300x250")
w=Label(win, text ='Frame Demonstration', font = "50")
w.pack()

frame=Frame(win,bd=6,relief=SUNKEN)
frame.pack()

b1= Button(frame, text ="Python", fg ="red")
b1.pack( side = LEFT)
b2 = Button(frame, text ="Java", fg ="brown")
b2.pack( side = LEFT )
b3 = Button(frame, text =".Net", fg ="blue")
b3.pack( side = LEFT )

bottomframe=Frame(win)
bottomframe.pack( side = BOTTOM )

b4 = Button(bottomframe, text ="C", fg ="green")
b4.pack( side = BOTTOM)
b5 = Button(bottomframe, text ="C++", fg ="green")
b5.pack( side = BOTTOM)
b6 = Button(bottomframe, text ="Fortran", fg ="green")
b6.pack( side = BOTTOM)
win.mainloop()