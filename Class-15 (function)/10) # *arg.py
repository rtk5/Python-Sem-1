# *arg
def f1(*arg):
    print(arg,type(arg))
    for ele in arg:
        print(ele)
f1(2,4,5,6)
