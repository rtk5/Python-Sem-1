#lambda inside reduce
import functools
l1=[1,2,5,8]
s=functools.reduce(lambda x,y:x+y,l1)
t=functools.reduce(int.__add__,l1)
u=functools.reduce(int.__mul__,l1)
print(s,t,u,sep = "\n")

l1=[2,5,8,12]
k = lambda s:s+1
print(k)
print(list(map(k,l1)))

s1=lambda s:print('hello '+s)
s1('python')

#display reverse of a string in uppercase
str2=lambda s:s.upper()[::-1]
print(str2('hello'))

#find max of 2 numbers
max=lambda a,b:a if (a>b) else b
print(max(4,5))
