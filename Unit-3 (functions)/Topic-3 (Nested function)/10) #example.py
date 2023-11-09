
def outer(a,b):
    sq=a**2
    def inner(a,b):
        return a+b
    add=inner(a,b)
    print(add)
    return(sq+5)
res=outer(5,10)
print(res)
