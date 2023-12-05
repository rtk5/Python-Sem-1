#hasattr    (has attribute)
class Student:
    i=23
    def __init__(self,n,s,b):
        self.name=n
        self.srn=s
        self.branch=b
    def display(self):
        print('display dat')
        print(self.name,"--",self.srn,"--",self.branch)
s1=Student("abc",23,'Ec')
print(hasattr(s1,"name"))
print(hasattr(s1,"i"))
s1.display()
s1.srn=34
s1.display()
if(not hasattr(s1,"marks")):
    s1.marks=100
s1.display()
print(s1.marks)
setattr(s1,"name","pqr")
s1.display()
