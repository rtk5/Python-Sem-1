# for

t3=(45,'python',89,12,True)     # capital T for true
for ele in t3:
    print(ele,end=" ")

for i in range(len(t3)):
    print(i,t3[i])          #indexing always uses []

print(t3[1+2])