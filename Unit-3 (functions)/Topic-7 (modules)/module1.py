#modules
#library -- packages -- modules
#modules make the code reusable

a=10
print("Welcome to module")
def f1():
    print('in f1')
def f2():
    print('in f2')
def _f3():
    print('in f3')

if __name__=='__main__':
    print("this is module 1")
else:
    print("this is not module 1")
    
