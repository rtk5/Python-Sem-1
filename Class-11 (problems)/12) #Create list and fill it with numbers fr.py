#Create list and fill it with numbers from n to 1 and then 2 to n
l=[]
n=int(input("ENTER:"))
for i in range(n,0,-1):
    l.append(i)
for i in range(2,n+1):
    l.append(i)
print(l)