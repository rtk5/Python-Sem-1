def func_decorator(func):
    def inner_func():
        print("hello,before function is called")
        func()
        print("hello,after the function is called")
    return inner_func

def func_hello():
    print("inside hello function")

bello=func_decorator(func_hello)
bello()