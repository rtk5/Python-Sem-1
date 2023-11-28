#Frame widget – Nested Frames
#Example 4
from tkinter import *
win=Tk()
win.geometry("1000x1000")
# Frame 1
frame1=Frame(win,bg="black",width=500,height=300)
frame1.pack()
# Frame 2 is created within Frame 1
frame2=Frame(frame1,bg="Grey",width=100,height=100)
frame2.pack(pady=20,padx=20)
win.mainloop()
