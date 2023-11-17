#hypotenuse
import math
def compute(func): #decorator function
    def inner(a,b):
        print("Computing hypotenuse")
        func(a,b) # this is being decorated by decorator
        print("*****************")
    return inner
@compute
def hypotenuse(a, b): # hypotenuse() is getting decorated
    h=math.sqrt(a*a+b*b)
    print(h)

hypotenuse(3,4) #calls decorated hypotenuse