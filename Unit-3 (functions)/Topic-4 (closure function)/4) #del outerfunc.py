
def outerfunc(x):
    def innerfunc():
        print(x)
    return innerfunc

myfunc=outerfunc(7)
myfunc()    #refers to innerfunc
del outerfunc
myfunc()    #still refers to inner func
