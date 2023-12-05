#scope of variable
class A:
    j=12
    __i=10  #private variable
print('outside class',A.j)
#print('private variable',A.__i)     #AttributeError: type object 'A' has no attribute '__i'
#private variable can't be called by usual syntax

print('private variable access',A._A__i)    #private variable access 10
