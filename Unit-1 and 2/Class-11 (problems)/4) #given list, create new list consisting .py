#given list, create new list consisting of square of all elements in the list
l1=input("enter list-").split()
l2=[]
for i in range(len(l1)):
    l1[i]=int(l1[i])
    l2.append(l1[i]*l1[i])
print(l2)
