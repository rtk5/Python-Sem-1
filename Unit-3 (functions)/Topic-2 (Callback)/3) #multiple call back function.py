#multiple call back function
def function(func_list,x,y):
    print("Inside function")
    for func in func_list:
        func(x,y)

def add(x,y):
    z=x+y
    print('sum =',z)

def divide(x,y):
    z=x/y
    print('Quotient is',)

cb_list=[add,divide]
function(cb_list,10,5)
