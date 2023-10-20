#WAP to create a set of all even numbers between 1 and 20 that are not divisible by 4

n=20
s=set(range(2,n+1,2))
d=set(range(4,n+1,4))
print(s-d)

