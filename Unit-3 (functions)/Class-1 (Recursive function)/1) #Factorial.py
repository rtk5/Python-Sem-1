#Recursive function
def fact(n):
    if n==0:    #terminating condition
        res=1
    else:
        res=n*fact(n-1)
    return res
d=int(input("ENTER:"))
print(fact(d))

