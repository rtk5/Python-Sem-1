#List all the even elements between 1 to 20 that are not divisible by 4
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l1=[]
l2=[]
for i in range(len(l)):
    l[i]=int(l[i])
    if (l[i]%2==0):
        l1.append(l[i])
for j in range(len(l1)):
    l1[j]=int(l1[j])
    if l1[j]%4==0:
        continue
    else:
        l2.append(l1[j])

print(l2)
l3=[]
for i in range(1,21):
    if i%2==0 and 1% 4!=0:
        l3.append(i)        
print(l3)