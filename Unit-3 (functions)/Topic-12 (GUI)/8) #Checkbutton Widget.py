#Checkbutton Widget
#Example
from tkinter import *
win=Tk()
win.geometry("300x300")
w=Label(win, text ='Select Your Hobbies:', fg="Blue",font = "100")
w.pack()
Checkbutton1 = IntVar() # holds integer data passed to the checkbutton widget
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()
cb1=Checkbutton(win, text="Painting",variable = Checkbutton1,onvalue = 1,offvalue = 0,height = 2,width = 10)
cb2=Checkbutton(win, text = "Dancing", variable = Checkbutton2,onvalue = 1,offvalue = 0,height = 2,width = 10) 
cb3=Checkbutton(win, text = "Cooking", variable = Checkbutton3,onvalue = 1,offvalue = 0,height = 2,width = 10)
cb1.pack()
cb2.pack()
cb3.pack()
mainloop()