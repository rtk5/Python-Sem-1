#division
def division(y):
    def divide(x):
        return x/y
    return divide

d1=division(2)
d2=division(3)

print(d1(20))
print(d2(96))
