#multilevel inheritance
class A:
    def disp(self):
        print("In class A")
class B(A):
    def disp1(self):
        print("In class B")
class C(B):
    def disp2(self):
        print("In class C")

c=C()
c.disp2()
c.disp1()
c.disp()

