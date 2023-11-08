#division of 2 numbers using recursion
def div(x,y):
    if (x==0):
        return 0
    else:
        return div(x-y,y)+ 1
print("Quotient is",div(int(input("Enter 1st number:")),int(input("Enter 2nd number:"))))
