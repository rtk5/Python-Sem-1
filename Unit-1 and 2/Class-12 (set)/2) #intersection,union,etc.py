#intersection,union,etc
s1={1,3}
s2={2,3}
print(s1|s2)
print(s1.union(s2))
print()
print(s1&s2)
print(s1.intersection(s2))
print(s1.intersection_update(s2))   #puts intersection value in s1
print(s1)
print()
s7={1,2,3}
s8={2,5,6}
print(s7-s8)
print(s7.difference(s8))
print(s7)

print(s7^s8)        #union - difference
print(s7.symmetric_difference(s8))

s3={2,3,4,5}
s4={2,3,4}
print(s3.issubset(s4))
print(s3.issuperset(s4))

print(s3==s4)

print(s3.isdisjoint(s4))
