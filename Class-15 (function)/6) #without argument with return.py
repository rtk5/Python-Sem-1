#without argument with return

def add():
    a,b=2,3
    s=a+b
    return s,a,b
r=add()
print(r)
print(type(r))

def area_rect():
    x,y=4,10
    a=x*y
    return a
r=area_rect()
print("Area =",r)
