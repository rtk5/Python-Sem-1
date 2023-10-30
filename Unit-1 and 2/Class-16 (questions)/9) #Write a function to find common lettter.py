#Write a function to find common lettters in 2 string
#using set

n=20
d=set(range(3,n+1,3))
f=set(range(5,n+1,5))
print(d.intersection(f))
