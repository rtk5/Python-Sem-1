#Create list of numbers from 1 to n except n//2

l=[]
n=int(input("enter:"))
a=n//2
for i in range(1,n+1):
    if i==a:
        continue
    else:
        l.append(i)
print(l)