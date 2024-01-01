#polymorphism method overloading and method overriding
'''class A:
    def add(self,a ,b,c):
        return a+b+c
    def add(self,a,b):
        return a+b
print(A().add(10,20,30))
#print(A().add(10,20))
'''
class A:
    def add(self,*args):    #can take 
        sum=0
        for i in args:
            sum=sum+i
        return sum
print(A().add(10,20,30))
print(A().add(10,20))
print(A().add(34.5,12.3,78.9))
