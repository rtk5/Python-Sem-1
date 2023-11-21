#Genaerator function = function that returns a range of numbers
def generator_func():
    yield 1
    yield 2
    yield 3
    
#code to check above generator function
for value in generator_func():
    print(value)

print()
#using without for loop
obj=generator_func()
print(next(obj))
print(next(obj))
print(next(obj))
