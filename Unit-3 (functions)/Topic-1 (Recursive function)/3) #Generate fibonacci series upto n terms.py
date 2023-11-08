#Generate fibonacci series upto n terms
def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
n=int(input("enter no. of terms:"))
for i in range(n):
    print(fib(i))
    

