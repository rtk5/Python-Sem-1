#example

a=10
def f1():
    a=20
    print(a)
def f2():
    global a
    a=99
    print(a)
print(a)
f1()
f2()
print(a+1)
