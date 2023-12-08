#heirachical inheritance

class A:
    def disp1(self):
        print("In class A")
class B(A):
    def disp2(self):
        print("In class B")
class C(A):
    def disp3(self):
        print("In class C")

b=B()
b.disp2()
b.disp1()

c=C()
c.disp3()
c.disp1()

