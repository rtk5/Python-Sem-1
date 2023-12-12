#__str__()
class Car:
    def __init__(self,color):
        self.color=color
    def __str__(self):
        return "A "+self.color+" Car"
a=Car("Black")
print(a)