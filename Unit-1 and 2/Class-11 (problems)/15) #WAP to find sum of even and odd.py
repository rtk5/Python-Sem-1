#WAP to find sum of even and odd numbers seperately for input n
n=int(input("ENTER:"))
e=0
o=0
for i in range(1,n+1):
    if i%2:
        e=e+i
    else:
        o=o+i
print('even=',e)
print('odd=',o)