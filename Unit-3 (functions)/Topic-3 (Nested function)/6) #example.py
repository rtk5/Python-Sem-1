#example
def f1():
    a=[10,20,30,40]
    print(a[0])
    def f2():
        a[0]=500
        print(a[0])
        print(a)
    f2()
    print(a)    #a becomes 500, beacause list is mutable
f1()