#filter

#map
l1=[13,-16,119,12]
def f2(x):
    if x<0:
        return x
print(list(map(f2,l1)))     #[None, -16, None, None]

#filter
def f2(x):
    if x <0:
        return x
print(list(filter(f2,l1)))      #[-16]      (deletes all false output)

def f3(x):
    return x<0
print(list(filter(f3,l1)))      ##[-16]

list1=[13,-16,119,12,0,11,1]
def f2(x):
    return x<20
print("Original list",list1)
print("new list",list(filter(f2,list1)))        
#output:
#       Original list [13, -16, 119, 12, 0, 11, 1]
#       new list [13, -16, 12, 0, 11, 1]

