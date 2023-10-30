# convert decimal number to binary
n=int(input('enter decimal number-'))
res=""
while(n!=0):
    rem=n%2
    n=n//2
    res+=str(rem)
print('binary number is =',res)





