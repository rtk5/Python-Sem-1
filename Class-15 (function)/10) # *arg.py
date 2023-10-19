# *arg    -- argument as a list or touple
def f1(*arg):
    print(arg,type(arg))
    for ele in arg:
        print(ele)
f1(2,4,5,6)
L=[2,3,4,5]
f1(L)
