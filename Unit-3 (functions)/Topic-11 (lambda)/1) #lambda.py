#lambda
def add(x,y):
    return x+y
print(add(5,6))

x=lambda x:x*x
print(x(5))
m=lambda x,y:x+y
print(m(3,4))

l1=[1,2,3,4,5]
l2=list(map(lambda x:x+1,l1))
print(l2)

l4=[1,2]
l5=[11,22]
l3=list(map(lambda x,y:x+y,l1,l2))
print(l3)
l3=list(map(lambda x,y,z,d:x+y+z+d,l1,l2,l4,l5))
print(l3)

l1=[1,2,3,57,9]
l2=list(filter(lambda x:x>2,l1))
print(l2)
