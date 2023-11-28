#Entry widget
from tkinter import *
win=Tk()
win.geometry("400x250")
name=Label(win, text = "Name").place(x = 30,y = 50)
email=Label(win, text = "Email").place(x = 30, y = 90)
password=Label(win, text = "Password").place(x = 30, y = 130)
submitbtn=Button(win, text = "Submit",activebackground = "red", activeforeground =
"blue").place(x = 30, y = 170)
entry1=Entry(win).place(x = 90, y = 50)
entry2=Entry(win).place(x = 90, y = 90)
entry3=Entry(win).place(x = 115, y = 130)
win.mainloop()
