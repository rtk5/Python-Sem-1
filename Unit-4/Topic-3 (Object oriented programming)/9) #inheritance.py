#inheritance
class A:
    def disp(self):
        print("In class A")
class B(A):
    def disp1(self):
        print("In class B")
b=B()
b.disp()
b.disp1()

a=A()
a.disp()
#a.disp1()      #AttributeError: 'A' object has no attribute 'disp1'
print()
class A:
    def disp(self):
        print("In class A")
class B(A):
    def disp(self):
        A().disp()
        super().disp()
        print("In class B")
B().disp()  #prints the 2nd set ie from class B(A)
print()
B().disp()