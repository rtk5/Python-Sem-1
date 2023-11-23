#map    -parameter as function and list/tuple/set
        # basically performs function across the list

#to add 1 to each element
list1=[12,2,4,6,11]
def f1(x):
    return x+1
list1_new=list(map(f1,list1))
print(list1_new)    #[13, 3, 5, 7, 12]

#to add lists
list2=[2,4,7]
list3=[5,6,8]
def f2(x,y):
    return x+y
l1_new=list(map(f2,list2,list3))
print(l1_new)   #[7, 10, 15]

#using inbuilt function
l1=[2,4,6]
l2=[5,6,8]
l1_new=list(map(int.__add__,l1,l2))
print(l1_new)   #[7, 10, 14]

m=[[13,14],[56],9]
n=[[3,4],[2]]
print(list(map(list.__add__,m,n)))  #[[13, 14, 3, 4], [56, 2]]

m=[[13,14],56,9]
def f2(x):
    return x*2
print(list(map(f2,m)))  #   [[13, 14, 13, 14], 112, 18]
