#closure
def outer(msg):
    def inner():    #nested function
        print(msg)
        print(id(inner))
    return inner    #returns nested

different = outer("This is an example of closure")
different()     #reffers to inner()
print(id(different))
#print(id(inner()))