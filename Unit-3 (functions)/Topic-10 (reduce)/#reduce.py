#find sum of all elements of given list

import functools
list1=[7,1,2,3,10]
def f1(x,y):
    return x+y
s = functools.reduce(f1,list1)
print(s)