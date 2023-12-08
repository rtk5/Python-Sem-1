#static method
class Student:
    count=0
    def __init__(self,n,addr,ph):
        self.name=n
        self.address=addr
        self.phone=ph
        Student.count=Student.count+1
    @staticmethod
    def disp_count():
        print('No. of objects',Student.count)
s1=Student('abc','jayanagar',46344374765477)
s2=Student('pqr','kormangala',87456453474378)
s1.disp_count()
Student.disp_count()