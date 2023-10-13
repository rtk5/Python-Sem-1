#update
d1={'a':'apple','b':'bat','c':'cat'}
d1.update({'e':'elephant'})
print(d1)

d1['e']='egge'
print(d1)

print(len(d1))  #no. of keys

d2={1:'a',2:'b',(3,4):'c',5:['d','e']}
print(d2)
print(d2[(3,4)])
print(d2[5])

d3=dict()
d3.update({'s1':'address1','s2':'address2'})
print(d3)

d3.setdefault('s3') #initializes the key
print(d3)

d3['s3']='add3'
print(d3)

