#create list with only single element(remove duplicate)
#l1=[2,3,4,4,5,5] l2=[2,3,4,5]

l1=[]
l2=[2,3,4,5,5,6,7,8,3]
for i in range (len(l2)):
    if l2[i] not in l1:
        l1.append(l2[i])
print(l1)
