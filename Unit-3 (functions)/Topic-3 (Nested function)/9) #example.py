#example
def outer():
    x=10
    print(x)
    def inner():
        y='hello'
        nonlocal x
        x=20
        print(x,y)
    inner()
    print(x)
x=5
print(x)
outer()
print(x)
