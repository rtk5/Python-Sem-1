#**kwarg -- argument as a dictionary
def f1(**kwarg):
    print(kwarg,type(kwarg))
    for i in kwarg.items():
        print(i)
    for i in kwarg.keys():
        print(i)
    for i in kwarg.values():
        print(i)
f1(a=2,b=5,c=7)

def f2(x,y,*arg,**kwarg):
    print(x,y)
    print(arg)
    print(*arg)
    print(kwarg)
f2(6,7,8,9,3,a=34,b=23,c=56)

