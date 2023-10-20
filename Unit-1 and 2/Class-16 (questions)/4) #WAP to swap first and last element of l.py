#WAP to swap first and last element of list
#input=[2,3,4,5] output=[5,3,4,2]
l1=[6,7,2,9]
n=len(l1)
temp=l1[0]
l1[0]=l1[n-1]
l1[n-1]=temp
print(l1)

l2=[2,3,7,4]
l2[0],l2[-1]=l2[-1],l2[0]
print(l2)
