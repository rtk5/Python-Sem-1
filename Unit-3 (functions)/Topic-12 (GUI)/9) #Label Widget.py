#Label Widget
from tkinter import *
win=Tk()
win.geometry("400x300")
username=Label(win, text = "Username").place(x = 30,y = 50)
password=Label(win, text = "Password").place(x = 30, y = 90) 
submitbutton=Button(win, text = "Submit",activebackground = "red", activeforeground =
"blue").place(x = 150, y = 150)
e1=Entry(win,width = 20).place(x = 120, y = 50)
e2=Entry(win, width = 20).place(x = 120, y = 90)
win.mainloop()