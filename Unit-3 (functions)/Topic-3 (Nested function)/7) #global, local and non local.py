#global, local and non local
def f1():
    global s
    s='K section'   #overwrites s value
    print(s)
s='hello class'
f1()
print(s)
