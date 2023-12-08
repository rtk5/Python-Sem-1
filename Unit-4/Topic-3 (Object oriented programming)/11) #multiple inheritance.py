#multiple inheritance
class A:
    def disp(self):
        print("In class A")
class B:
    def disp1(self):
        print("In class B")
class C(A,B):
    def disp2(self):
        print("In class C")

c=C()
c.disp()
c.disp1()
c.disp2()

print()
class A:
    def disp1(self):
        print("In class A")
class B:
    def disp1(self):
        print("In class B")
class C(A,B):
    def disp1(self):
        super().disp1()     #super refers to A since (A,B) ie A is mentioned 1st
        print("In class C")

c=C()
c.disp1()

print()

class D(B,A):       #super becomes class B
    def disp1(self):
        super().disp1()
        print("In class D")

d=D()
d.disp1()