#class method
class Maths:
    @staticmethod
    def addnum(num1,num2):
        return num1+num2
if __name__=="--main__":
    res=Maths.addnum(10,20)
    print(res)