#Chaining Decorators - Decorating a function with multiple decorators.
def decorator_x(func):
    def inner_func():
        print("X"*20) #Printing X 20 times
        func()
        print("X"*20) #Printing X 20 times
    return inner_func

def decorator_y(func):
    def inner_func():
        print("Y"*20) #Printing Y 20 times
        func()
        print("Y"*20) #Printing Y 20 times
    return inner_func

def func_hello():
    print("Hello")
    
hello = decorator_y(decorator_x(func_hello)) #Chaining Decorators
hello()