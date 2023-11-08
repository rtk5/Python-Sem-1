#Tower of hanoi
def toh(n,src,aux,dest):
    if n==1:
        print("Move disc 1 from source",src,"to destination",dest)
        return
    toh(n-1,src,dest,aux)
    print("Move disc",n,"from source",src,"to destination",dest)
    toh(n-1,aux,src,dest)
n=int(input("Enter number of discs:"))
toh(n,'A','B','C')
