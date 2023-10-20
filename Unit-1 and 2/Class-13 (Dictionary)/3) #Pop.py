#Pop
d1={'a':'apple','b':'bat','c':'cat'}
d1.pop('a')
print(d1)

d1.popitem()
print(d1)

d1.clear()
print(d1)

del d1      
#print(d1)       #NameError: name 'd1' is not defined

d6={'a':'A','b':'B','c':'C'}
d7=d6.copy()
print(d7)

d8={}
d8=dict.fromkeys(d6,'hello')    #copies keys
print(d8)

