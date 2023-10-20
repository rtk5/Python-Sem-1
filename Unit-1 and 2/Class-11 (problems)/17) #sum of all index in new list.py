#p=[1,2,3]
#q=[4,5,6]
#r=[7,8,9]
#print output[[1,4,7],[2,5,8],[3,6,9]]
#sum of all index in new list[1+4+7,2+5+8,3+6+9]

l=input("enter:").split()
j=input("enter:").split()
k=input("enter:").split()
m=[]
for i in range(len(j)):
    l[i]=int(l[i])
    j[i]=int(j[i])
    k[i]=int(k[i])
l1=[sum(l)]
j1=[sum(j)]
k1=[sum(k)]
m.append(l1)
m.append(j1)
m.append(k1)
print(m)
