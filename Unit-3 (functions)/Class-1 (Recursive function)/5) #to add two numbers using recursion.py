#to add two numbers using recursion
def add(x,y):
    if (y==0):
        return x
    return add(x,y-1)+1
print("sum=",add(int(input("Enter 1st number:")),int(input("Enter 2nd number:"))))
