'''csv files must be password protected. forgot password feature.'''
from tkinter import *
from tkinter import messagebox as ms
import csv

pass_verified = False
username = ""
def click():
    global pass_verified, username
    username = e1.get()
    password = e2.get()

    d = dict()
    with open("/home/rithvikmatta/Python/MiniProject/user_acct_info.csv",'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for line in csv_reader:
            d[line[0]] = line[1]
        if (username in d) and d[username] == password:
            pass_verified = True 
            ms.showinfo('Message','Password verified')
        else:
            ms.showinfo('Message','Incorrect password')

def verification():
    return pass_verified

def acct():
    return username

def acct_creation():
    def add():
        new_data = [e1.get(), e2.get()]
        with open("/home/rithvikmatta/Python/MiniProject/user_acct_info.csv",'a',newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if new_data[0] != '' and new_data[1] != '':
                csv_writer.writerow(new_data)
                ms.showinfo('SUCCESS!', 'Account created')
            else:
                ms.showinfo('Message:', 'Please enter something.')
    root2 = Toplevel(root)
    root2.title('User registration')
    root2.geometry('1200x900')
    root2.resizable(False,False)
    frame = Frame(root2)
    frame.pack(padx=350,pady=300)
    username = Label(frame, text='Enter Username:')
    username.config(font=24)
    username.grid(row=0,column=0,sticky='e',pady=10)
    password = Label(frame, text='Enter Password:')
    password.config(font=24)
    password.grid(row=1,column=0,sticky='e',pady=10)
    e1 = Entry(frame, width=20)
    e1.grid(row=0,column=1,sticky='w',pady=10)
    e2 = Entry(frame, width=20, show='*')
    e2.grid(row=1,column=1,sticky='w',pady=10)
    create = Button(frame, text='Sign up',command=add, activeforeground='Black', activebackground='Red',width=6,height=2)
    create.grid(row=2,column=0,sticky='e',padx=5,pady=10)
    quit = Button(frame,text='Back',command=root2.destroy,width=6,height=2)
    quit.grid(row=2,column=1,sticky='w',padx=5,pady=10)
root = Tk()
root.title('Authentication:')
root.geometry('1200x900')
root.resizable(False,False)
image_path = '/home/rithvikmatta/Python/MiniProject/demo2.png'  
img = PhotoImage(file=image_path)
background_pic = Label(root, image=img)
background_pic.place(relwidth=1, relheight=1)
frame = Frame(root)
frame.pack(padx=350,pady=300)
username = Label(frame, text='Username:')
username.config(font=24)
username.grid(row=0,column=0,sticky='e',pady=10)
e1 = Entry(frame, width=20)
e1.grid(row=0,column=1,sticky='w',padx=10,pady=10)
password = Label(frame, text='Password:')    
password.config(font=24)
password.grid(row=1,column=0,sticky='e',pady=10)
e2 = Entry(frame, width=20, show='*')
e2.grid(row=1,column=1,sticky='w',padx=10,pady=10)
submit = Button(frame, text='Submit', command=click, activeforeground='Black', activebackground='Red',width=6,height=2)
submit.grid(row=2,column=0,sticky='e',padx=3,pady=15)
quit = Button(frame,text='Quit',command=root.destroy,width=6,height=2)
quit.grid(row=2,column=1,sticky='w',padx=3,pady=15)
register_label = Label(frame,text="Don't have an account?")
register_label.config(font=24)
register_label.grid(row=3,column=0,sticky='e',padx=5,pady=10)
register = Button(frame,text='Register',command=acct_creation, activeforeground='Black', activebackground='Blue',width=6,height=2)
register.grid(row=3,column=1,sticky='w',padx=3,pady=10)
root.mainloop()
