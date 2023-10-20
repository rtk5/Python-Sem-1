#WAP to count all numbers in a list which is divisible by 3
l=input("enter:").split()
sum=0
for i in range(len(l)):
    l[i]=int(l[i])
    if l[i] % 3 == 0:
        sum=sum+1
print(sum)