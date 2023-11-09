#Callback
#function that is passed to another function as an argument

def printname(name):
    return f'My name is {name}'

def calfunc(name,func):
    msg=func(name)
    print(msg)

print(calfunc('Rithvik',func=printname))
