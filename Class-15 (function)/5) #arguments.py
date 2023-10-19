#arguments
def add(a,b):
    s=a+b
    print(s)
add(5,3)    #positional argument
x,y=7,8
add(x,y)         #no need of print for functions
d,f,g=2,3,4
#add(d,f,g)  #TypeError: add() takes 2 positional arguments but 3 were given

def add(a,b=4):     #keyword argument
    s=a+b
    print(s)
add(5)

def add(a,b):
    s=a+b
    print(s)
add(5,b=4)  #5 is positional argument, b=4 is keyword argument

def add(a,b):
    s=a+b
    print(s)
#add(a=5,b)     #SyntaxError: positional argument follows keyword argument

