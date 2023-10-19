#without argument with return

def add():
    a,b=2,3
    s=a+b
    return s,a,b
r=add()
print(r)
print(type(r))
