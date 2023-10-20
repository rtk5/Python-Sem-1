#Create list of rows such that 0th row contains 1 to n
#1st row contains square of 1 to n
#3rd row contains cube of 1 to n
'''
L=[]
for i in range(1,11):
    L.append(i)
L.append([])
L.append([])
for i in range(len(L)):
    L[i]=int(L[i])
    L[10][i].append(L[i]*L[i])
print(L)

'''

p=[]
q=[]
r=[]
output=[]
n=int(input("ENTER:"))
for i in range(1,n+1):
    p.append(i)
output.append(p)
for i in range(1,n+1):
    q.append(i*i)
output.append(q)
for i in range(1,n+1):
    r.append(i*i*i)
output.append(r)
print(output)
