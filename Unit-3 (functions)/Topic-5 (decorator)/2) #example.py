#example
def func_decorator(func):
    def inner_func():
        print("hello,before function is called")
        func()
        print("hello,after the function is called")
    return inner_func

@func_decorator
def func_hello():
    print("inside hello function")

func_hello()