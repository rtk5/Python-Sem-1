import module1

module1.f1()
module1.f2()
module1._f3()
print(module1.a)
module1.a=module1.a+2
print(module1.a)

print()
from module1 import f1,a,f2,_f3
f1()
print(a)
f2()
_f3()

print()
from module1 import *       #   (* represents all)
print(a)
_f3()
