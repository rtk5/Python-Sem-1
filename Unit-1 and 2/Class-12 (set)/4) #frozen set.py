#frozen set

s1=frozenset()
#print(type(s1)) #<class 'frozenset'>
s1={1,2,3}

s2={2,3,4}

#print(s2)

for ele in s2:
    print(ele)
'''
s2.add(78)      #AttributeError: 'frozenset' object has no attribute 'add'
print(s2)   '''

print(s1|s2)        #only 1 can be frozen set to make these commands work
print(s1&s2)
print(s1-s2)
print(s2-s1)
print(s1^s2)

