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

@decorator_y #Chaining Decorators
@decorator_x
def func_hello():
    print("Hello")
    
func_hello()