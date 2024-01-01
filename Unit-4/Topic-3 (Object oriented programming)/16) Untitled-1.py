
class A:
    def __init__(self,name = "Shaun"):
        self.__name=name
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
x=A()
print(x.getname())
x.setname("Joe")
print(x.getname())
