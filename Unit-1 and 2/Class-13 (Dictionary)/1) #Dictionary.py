#Dictionary
'''
d1={}    #is a dictionary, not a set (empty)
print(type(d1))
d2=dict()
print(type(d2))

d1={'a':'apple','b':'bat','c':'cat'}
print(d1)

print(d1.items())   #items = keys+values

v=d1.values()
k=d1.keys()
print(v)
print(k)
'''
employee={}
for i in range(2):
    name=input("ENTER NAME:")
    sal=input("ENTER SAL:")
    employee[name]=sal
print(employee)

for ele in employee:
    print(ele)      #print keys

for ele in employee.items():
    print(ele)

print(employee.get('abc'))  #value  and abc--name




