#print srn,name and marks of a student
class Student:  #class
    def __init__(self,phy,chem,maths,srn):  #constructor
        self.p=phy  #instatnce variable -variable accessed by the object
        self.c=chem
        self.m=maths
        self.srn=srn
    def id(self):
        print('SRN-',self.srn)
    def total(self):
        print("total marks-",self.p+self.c+self.m)
    def marks(self):
        print('phy marks-',self.p,'chem marks-',self.c,'maths marks-',self.m)
s1=Student(56,67,45,'PES2UG23CS485')    #objects are s1,s2,s3
s2=Student(76,89,34,'PES2UG23CS486')
s3=Student(98,43,65,'PES2UG23CS489')
s1.id()
s1.marks()
s1.total()
s2.id()
s2.marks()
s2.total()
s3.id()
s3.marks()
s3.total()