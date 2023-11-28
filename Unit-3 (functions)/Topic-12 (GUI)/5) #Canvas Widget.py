#Canvas Widget
#Example2
import tkinter
win=tkinter.Tk()
win.title("Tkinter Canvas Widget")
# creating canvas
cv=tkinter.Canvas(win, bg="yellow", height=300, width=300)
# drawing two arcs
coord = 10, 10, 300, 300
arc1=cv.create_arc(coord, start=0, extent=150, fill="pink")
arc2=cv.create_arc(coord, start=150, extent=215, fill="green")

# adding canvas to window and display it
cv.pack()
win.mainloop()