#super constructor
class Sample:
    def __init__(self,m,n,o,p):
        self.m=m
        self.n=n
        self.o=o
        self.p=p
class child_sample(Sample):
    def __init__(self,m,n,o,p,q):
        super().__init__(m,n,o,p)
        self.q=q
    def display(self):
        print(self.m,self.n,self.p,self.q)
c=child_sample(5,7,8,12,45)
c.display()     