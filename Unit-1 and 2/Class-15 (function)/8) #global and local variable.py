#global and local variable
x=10
def f2():
    print('inside',x)
f2()
print('outside',x)

#x is global variable
#a is local variable

y=10
def f3():
    global y
    y=y+1
    q=45
    print('q',q)
    print('inside',y)
f3()
print('outsise',y)
