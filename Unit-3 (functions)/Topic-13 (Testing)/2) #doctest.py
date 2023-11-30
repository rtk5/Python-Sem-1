#doctest
from doctest import testmod
def fact (n):
    '''
    >>> fact(5)
    120
    >>> fact(0)
    1
    '''
    if n==0:
        res=1
    else:
        res=n*fact(n-1)
    return res

testmod(name='fact',verbose=True)
'''
Trying:
    fact(5)
Expecting:
    120
ok
Trying:
    fact(0)
Expecting:
    1
ok
1 items had no tests:
    fact
1 items passed all tests:
   2 tests in fact.fact
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
'''
testmod(name='fact',verbose=False)
'''Trying:
    fact(5)
Expecting:
    120
ok
Trying:
    fact(0)
Expecting:
    1
ok
1 items had no tests:
    fact
1 items passed all tests:
   2 tests in fact.fact
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
'''

