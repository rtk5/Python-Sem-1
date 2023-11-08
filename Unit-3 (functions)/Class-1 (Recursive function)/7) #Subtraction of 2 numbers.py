#Subtraction of 2 numbers
def sub(x,y):
    if (y==0):
        return x
    else:
        return sub(x-1,y-1)
print("Difference is",sub(int(input("Enter 1st number:")),int(input("Enter 2nd number:"))))
