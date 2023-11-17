#exmple 3
import math
def calculate(f): #decorator function
    def inner1(*args): #*args is variable length argument
        print("Decorator")
        f(*args) # this is being decorated by decorator
        print("***********************")
    return inner1
@calculate
def factorial(num): #factorial() getting decorated
    print(math.factorial(num)) 
    
@calculate
def squareroot(num): #squareroot() getting decorated
    print(math.sqrt(num))
    
@calculate
def maximum(*num): #maximum() getting decorated
    print(max(num[0],num[1],num[2]))
    
factorial(5) #calls decorated factorial()
squareroot(16) #calls decorated sqrt1()
maximum(23,9,78) #calls decorated maximum()