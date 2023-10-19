print('hello')
def f():
    print('python')
    return 'hi'
print('welcome')
print(f)    #id
print(f())  
k=f()
print(k)

x=[22,23,67]
def f5(y):
    y=y+[2,3]
    print('inside',y)
f5(x)
print('outside',x)


