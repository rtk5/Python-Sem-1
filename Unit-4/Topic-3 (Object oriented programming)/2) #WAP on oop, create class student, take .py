#WAP on oop, create class student, take phy,chem,math marks and display marks and total marks
#for three students
class Student:  #class
    def __init__(self,phy,chem,maths):  #constructor
        self.p=phy  #p--> instatnce variable -variable accessed by the object
        self.c=chem
        self.m=maths
    def total(self):
        print("total marks-",self.p+self.c+self.m)
    def marks(self):
        print('phy marks-',self.p,'chem marks-',self.c,'maths marks-',self.m)
s1=Student(56,67,45)    #objects are s1,s2,s3
s2=Student(76,89,34)
s3=Student(98,43,65)
s1.marks()
s1.total()
s2.marks()
s2.total()
s3.marks()
s3.total()
