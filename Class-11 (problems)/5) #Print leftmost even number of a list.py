#Print leftmost even number of a list
l1=[1,5,72,3,1,3,5,7,9,11,12,13,15]
for i in range(len(l1)):
    if l1[i] %2==0:
        print(l1[i])
        break

