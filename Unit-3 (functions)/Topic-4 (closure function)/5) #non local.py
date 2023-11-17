#
def f1():
    x=0
    def f2():
        nonlocal x
        x+=1
        return x
    return f2

func=f1()
retval=func()
print("x=",retval)
retval=func()
print("x=",retval)
