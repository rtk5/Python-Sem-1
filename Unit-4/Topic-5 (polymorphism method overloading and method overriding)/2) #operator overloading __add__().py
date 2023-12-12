#operator overloading __add__()
class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x
a=A(10)
b=A(20)
print(a+b)
c=A('hello')
d=A('python')
print(c+d)
