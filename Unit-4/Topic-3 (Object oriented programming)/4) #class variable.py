#class variable
class Student:
    b=10    #b is class variable
    def __init__(self,s,n,m):   #s,n,m --> parameter
        self.srn=s      #srn --> instance variable
        self.name=n
        self.marks=m
    def display(self):
        Student.b=Student.b+2
        self.b=self.b+2
        print('SRN-->',self.srn,', NAME-->',self.name,', MARKS-->',self.marks)
s1=Student(12,'abc',78)
s2=Student(13,'acvb',23)

s1.display()
s2.display()

print('current',Student.b)
Student.b+=10
print('after',Student.b)       # classname.variablename


    
