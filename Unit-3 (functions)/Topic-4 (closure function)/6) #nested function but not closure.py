#nested function but not closure
def outer(msg):
    def inner(m=msg):
        print(m,"world")
    return inner

different=outer(msg="hello")
different()