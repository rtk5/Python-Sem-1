#sum of n numbers using for loop but decrement counter
n=int(input('Enter number-'))
sum=0
for i in range(n,0,-1):
    sum=sum+i
print(sum)