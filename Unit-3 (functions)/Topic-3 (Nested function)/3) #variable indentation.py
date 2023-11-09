#variable indentation

a=10
b=20
def first():
    a=20
    print(a)
    def second():
        c=30
        print(c)
    second()
    print(a,b)  #a=20
first()
print(a,b)      #a=10

