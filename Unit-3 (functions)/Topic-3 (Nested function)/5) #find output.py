#find output

x=7
def one(x):
    x=x+1
    print(x)
    def two(x):
        x=x+2
        print(x)
    two(x)
print(x)
one(x)
print(x)