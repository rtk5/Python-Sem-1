#Difference between successive elements of a list
#l1=[2,5,7] output=[3,2]

l=input("ENTER:").split()
l1=[]
for i in range (len(l)):
    l[i]=int(l[i])
    a = l[i+1]-l[i]
    l1[i]=int(l1[i])    
    l1.append(a)
print(l1)

)