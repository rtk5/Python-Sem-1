#Given list add number n to each element of list
n=int(input("enter:"))
l=input("enter list:").split()
l1=[]
for i in range(len(l)):
    l[i]=int(l[i])
    l1.append(l[i]+n)
print(l1)


