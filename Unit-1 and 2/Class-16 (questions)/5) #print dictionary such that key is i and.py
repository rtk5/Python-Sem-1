#print dictionary such that key is i and value is i*i
#d={1:1,2:4,3:9}

n=int(input("ENTER NO-"))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)