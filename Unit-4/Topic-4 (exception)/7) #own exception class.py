class MyException(Exception):
    def __init__(self,msg):
        self.msg=msg
a=3
b=int(input("Enter number-"))
try:
    if(b==3):
        raise MyException("b is 3")
except MyException as m:
    print(m)
else:
    print(a/b)
finally:
    print("Thank you")

    