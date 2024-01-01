#own exception class

class MyException(Exception):
    def __init__(self,str):
        self.str=str
    def __str__(self):
        return self.str
n=int(input("Enter a number:"))
try:
    if not i<=n<=100:
        raise MyException("number not in range")
    print("number is fine:",n)
except MyException as e:
    print(e)
