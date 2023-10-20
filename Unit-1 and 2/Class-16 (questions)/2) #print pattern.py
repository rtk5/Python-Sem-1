#print pattern
'''
1
22
333
444
'''
n=int(input("no. of rows="))
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()
