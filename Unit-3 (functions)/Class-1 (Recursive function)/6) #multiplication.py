#multiplication
def multiply(x,y):
    if (x==1):
        return y
    else:
        return multiply(x-1,y)+ y
print("Product is",multiply(int(input("Enter 1st number:")),int(input("Enter 2nd number:"))))
