#find output
def f1():
    x=1
    def f2(a):
        x=4
        print(a+x)
    print(x)
    f2(2)
    print(x)
f1()
#answer == 1,6,1