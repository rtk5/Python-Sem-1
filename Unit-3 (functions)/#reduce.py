#find sum of all elements of given list

import functools
list1=[7,1,2,3,10]
def f1(x,y):
    return x+y
s = functools.reduce(f1,list1)      #list 1 becomes[8,2,3,10],[10,3,10],[13,10],[23]
print(s)
