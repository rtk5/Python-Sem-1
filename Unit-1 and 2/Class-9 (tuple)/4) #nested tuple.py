#nested tuple
t1=(10,12,13,(4,5,6,(7,8,9)))
#print 6
print(t1[3][2])     #3-nested tuple;    2-for 6

#print 8
print(t1[3][3][1])

t2=(10,12,(34,45,67),(1,2,3))
#print 45 ,10 and 2
print(t2[2][1], t2[0], t2[3][1])

