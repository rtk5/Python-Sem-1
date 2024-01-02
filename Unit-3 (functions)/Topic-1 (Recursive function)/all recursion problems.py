'''
1.Compute the GCD of two numbers using recursion.
2. Generate Fibonacci Series upto n_terms using recursion.
3. Solve the Tower of Hanoi Puzzle for a given n discs using recursion.
4. Calculate the length of the string using recursion.
5. Calculate the sum of first n natural numbers using recursion.
6. Write a recursive function that accepts two numbers with variables a and b and
calculate a power b or a raised to b. Test the recursive function.
7. Find the subtraction of two numbers using recursion.
8. Find the product of two numbers using recursion.
9. Find the quotient of two numbers using recursion.
10. Mimic the in operator using recursion.
'''
#1
'''
def gcd(m, n):
    if m == n :
        res = m
    elif m > n :
        res = gcd(m -n, n)
    else:
            res = gcd(m, n - m)
    return res
print("gcd :",gcd(5,25))
'''
#2
'''
def fib(n):    #Recursive Function
  	if n <= 1: #terminating condition
    	     return n
  	else:
    	     return(fib(n-1) + fib(n-2))
 
n_terms=int(input("Enter the number of terms for Fibonacci Series\n"))

for i in range(n_terms):
           print(fib(i))
'''
#3
'''
def TowerOfHanoi(n , src, aux, dest): #Recursive Function
    if n==1: #terminating condition
        print ("Move disk 1 from ",src,"to ",dest)
        return
    TowerOfHanoi(n-1, src, dest, aux)
    print ("Move disk",n,"from ",src,"to ",dest)
    TowerOfHanoi(n-1, aux, src, dest)
      
n=int(input("Enter number of disks\n"))
print("A-Source  B-Auxiliary  C-Destination\n")
TowerOfHanoi(n,'A','B','C')
'''
#4.
'''
def length(s):
	if s== "":
		return 0
	else:
		return 1+length(s[1:])
print(length("python"))
'''
#5.
'''
def sum1(n):
    if (n == 0):
        return 0
    else:
        return n + sum1(n - 1)
number = 10
print("The sum of first", number,"number is", sum1(number))
'''
#6.
'''
def exp(x,y):
if(y==1):
 		return x
else:
       	return x*exp(x,y-1)
a =2
b =4
print(a,"raised to",b,"is", exp(a,b))
'''
#7
'''
def subtract(x, y): #Recursive Function
    if(y == 0):            #terminating condition
        return x
    return subtract(x-1, y-1)
 
print("Result =", subtract(10, 20))
'''
#8
'''
def product(a,b): #Recursive Function
    if(a<b): 
        return product(b,a)
    elif(b!=0):
        return(a+product(a,b-1))
    else:                  #Stopping point
        return 0

print("Product =",product(10,20))
'''
#9
'''
def divide(x, y):   #Recursive Function
    if(x < y):             #terminating condition
        return 0
    else:
        return 1 + divide(x - y, y)

print("Result:", divide(20, 5))
'''
#10
'''
#mimic the in operator
a = [12,44,33,66]
n = int(input("enter the element to be searched"))

#iterative
'''
'''
def find_me(a,n):
    for i in a:
        if i==n:
            return True
	return False
print(find_me(a,n))
'''
#recursive code
'''
def find_me(a,n):
	if not a:		#empty data structure is False
					#Non-Empty data sturcture is True
					#Non-zero value is True
		return False
	elif a[0]==n:
		return True
	else:
		return find_me(a[1:],n)	#write the diagram
print(find_me(a,n))
'''