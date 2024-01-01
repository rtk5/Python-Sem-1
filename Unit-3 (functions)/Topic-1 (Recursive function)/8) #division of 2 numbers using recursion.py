#division of 2 numbers using recursion
def divide(x, y):   #Recursive Function
    if(x < y):             #terminating condition
        return 0
    else:
        return 1 + divide(x - y, y)

print("Result:", divide(20, 5))