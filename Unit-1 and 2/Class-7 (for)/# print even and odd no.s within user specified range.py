# print even and odd no.s within user specified range
a=int(input('enter first number-'))
b=int(input('enter last number-'))
for i in range(a,b):
    if (i%2):
        print('even no.=',i)
    else:
        print('odd  no.=',i)
      