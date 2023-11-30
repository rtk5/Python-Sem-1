#pdb
def fact(n):
    f=1
    for i in range(1,n+1):
        #pdb.set_trace()
        print (i)
        f=f*i
    return i

print("Factorial of 5 =",fact(5))