
def f1():
    def f2():
        print("Hello")
        print("World")
    print('f2=',id(f2))
    return f2
c=f1()  #refers to f2()
c()
print('c-',id(c))   #id of f2() and c() are same
