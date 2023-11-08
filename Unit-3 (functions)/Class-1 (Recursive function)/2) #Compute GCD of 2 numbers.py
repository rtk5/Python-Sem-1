#Compute GCD of 2 numbers (GCD-greatest common divisor)
def gcd(m,n):
    if m==n:    #terminating condition
        res=m
    elif m>n:
        res=gcd(m-n,n)
    else:
        res=gcd(m,n-m)
    return res
d=int(input("ENTER 1st NUMBER:"))
e=int(input("ENTER 2nd NUMBER:"))
print(gcd(d,e))