#Compute the sum of squares of numbers in the Fibonacci series

# Generator function - fibonacci_numbers
def fibonacci_numbers(nums):
    x,y=0,1
    for i in range(nums):
        x,y=y,x+y
        yield x

# Generator function - square
def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(int(input("ENTER:"))))))
